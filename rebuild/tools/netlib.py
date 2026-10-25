"""Shared throttled HTTP helper for every rebuild worker.
Global spacing per host group via a file lock (works across threads and processes),
exponential backoff on 429/503 honouring Retry-After. Never bypasses bot walls:
403/401 and challenge pages are returned as failures, not retried."""
import fcntl, json, os, random, time, urllib.parse, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCKDIR = os.path.join(ROOT, 'work', '_net')
os.makedirs(LOCKDIR, exist_ok=True)
UA = 'possession-taxonomy/1.0 (noreply@anthropic.com)'
SPACING = {'wikipedia': 2.0, 'wikidata': 1.0, 'default': 1.0}
CA = '/root/.ccr/ca-bundle.crt'


def _group(url):
    h = urllib.parse.urlparse(url).netloc
    if h.endswith('wikipedia.org'): return 'wikipedia'
    if h.endswith('wikidata.org'): return 'wikidata'
    return 'default'


def _wait_turn(group):
    """Block until this group's global spacing has elapsed, then stamp the time."""
    p = os.path.join(LOCKDIR, group + '.lock')
    with open(p, 'a+') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0); s = f.read().strip()
        last = float(s) if s else 0.0
        gap = SPACING[group] - (time.time() - last)
        if gap > 0: time.sleep(gap)
        f.seek(0); f.truncate(); f.write(str(time.time())); f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)


def _penalise(group, seconds):
    """Push the group's next slot into the future after a 429 so all workers back off."""
    p = os.path.join(LOCKDIR, group + '.lock')
    with open(p, 'a+') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0); f.truncate(); f.write(str(time.time() + seconds - SPACING[group])); f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)


MAX_QUEUE = 20  # seconds; if the group's next slot is further away than this, fail fast instead of queueing


def _queue_wait(group):
    p = os.path.join(LOCKDIR, group + '.lock')
    try:
        s = open(p).read().strip()
        return float(s) + SPACING[group] - time.time() if s else 0
    except Exception:
        return 0


def get(url, params=None, tries=6, timeout=40, accept='application/json'):
    """Return (status, text). status 0 = network failure; 429 = rate limited (callers fall back to other fetchers)."""
    if params: url = url + ('&' if '?' in url else '?') + urllib.parse.urlencode(params)
    g = _group(url); delay = 4.0
    if g == 'wikipedia': tries = min(tries, 2)
    if _queue_wait(g) > MAX_QUEUE: return 429, ''
    import ssl
    ctx = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else None
    for i in range(tries):
        _wait_turn(g)
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': accept})
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
                return r.status, r.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and i < tries - 1 and _queue_wait(g) < MAX_QUEUE:
                ra = e.headers.get('Retry-After')
                wait = float(ra) if ra and ra.isdigit() else delay
                wait = min(wait, 120) + random.uniform(0, 1)
                _penalise(g, wait); delay *= 2
                continue
            return e.code, ''
        except Exception:
            if i < tries - 1:
                time.sleep(delay); delay *= 2; continue
            return 0, ''
    return 429, ''


def get_json(url, params=None, **kw):
    st, t = get(url, params, **kw)
    try:
        return st, json.loads(t) if t else None
    except Exception:
        return st, None


WP = 'https://en.wikipedia.org/w/api.php'
WD = 'https://www.wikidata.org/w/api.php'


def wiki_search(q, n=5):
    st, j = get_json(WP, {'action': 'query', 'list': 'search', 'srsearch': q, 'format': 'json', 'srlimit': n})
    if not j: return st, []
    return st, [{'title': r['title'], 'snippet': r.get('snippet', '')} for r in j['query']['search']]


def wiki_pages(titles):
    """Retrieve intro extracts for up to 20 titles; returns list of {title,url,exists,extract}."""
    out = []
    for i in range(0, len(titles), 20):
        st, j = get_json(WP, {'action': 'query', 'titles': '|'.join(titles[i:i + 20]), 'prop': 'extracts|info',
                              'exintro': 1, 'explaintext': 1, 'inprop': 'url', 'redirects': 1, 'format': 'json'})
        if not j:
            out += [{'title': t, 'error': st} for t in titles[i:i + 20]]; continue
        for p in j['query']['pages'].values():
            if 'missing' in p or 'invalid' in p:
                out.append({'title': p.get('title'), 'exists': False})
            else:
                out.append({'title': p['title'], 'exists': True, 'url': p.get('fullurl'),
                            'extract': (p.get('extract') or '')[:700]})
    return st, out


def wd_search(q, n=5):
    st, j = get_json(WD, {'action': 'wbsearchentities', 'search': q, 'language': 'en', 'format': 'json', 'limit': n})
    if not j: return st, []
    return st, [{'id': r['id'], 'label': r.get('label'), 'description': r.get('description', '')} for r in j.get('search', [])]


def wd_entities(ids):
    st, j = get_json(WD, {'action': 'wbgetentities', 'ids': '|'.join(ids[:50]), 'props': 'labels|descriptions|claims|sitelinks',
                          'languages': 'en', 'sitefilter': 'enwiki', 'format': 'json'})
    if not j: return st, []
    out = []
    for q, e in (j.get('entities') or {}).items():
        if 'missing' in e: out.append({'id': q, 'exists': False}); continue
        c = e.get('claims', {})
        def vals(p):
            r = []
            for s in c.get(p, [])[:5]:
                dv = s.get('mainsnak', {}).get('datavalue', {}).get('value')
                if isinstance(dv, dict): dv = dv.get('id') or dv.get('time') or dv.get('text') or dv.get('amount')
                r.append(dv)
            return r
        out.append({'id': q, 'exists': True, 'url': 'https://www.wikidata.org/wiki/' + q,
                    'label': e.get('labels', {}).get('en', {}).get('value'),
                    'description': e.get('descriptions', {}).get('en', {}).get('value'),
                    'instance_of': vals('P31'), 'country': vals('P17') or vals('P495'), 'inception': vals('P571'),
                    'manufacturer': vals('P176'), 'enwiki': e.get('sitelinks', {}).get('enwiki', {}).get('title')})
    return st, out


def wd_sparql(query):
    st, j = get_json('https://query.wikidata.org/sparql', {'format': 'json', 'query': query}, accept='application/sparql-results+json')
    if not j: return st, []
    rows = []
    for b in j['results']['bindings'][:300]:
        rows.append({k: v.get('value') for k, v in b.items()})
    return st, rows
