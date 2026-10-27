"""Category rebuild orchestrator (Claude API workers).

  python3 tools/run.py go  B5 B6 ...    full pipeline per code: plan -> shelves -> assemble -> validate -> merge
  python3 tools/run.py plan B5 ...      plan only          (Message Batches API, no web)
  python3 tools/run.py shelves B5 ...   shelf workers      (web shelves: Messages API + server web tools; no-web shelves: Batches)
  python3 tools/run.py assemble B5 ...  build out/<CODE>*.json from finished shelves

Resumable: finished steps leave files in work/<CODE>/ and are skipped on re-run.
Every URL a worker actually retrieves (server web_fetch result, Wikipedia/Wikidata API record)
is logged to work/<CODE>/sources.tsv; only those URLs are accepted as `s` for archetypes,
new kinds, brands and traditions."""
import anthropic, concurrent.futures as cf, datetime, fcntl, json, os, re, subprocess, sys, threading, time, traceback, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import netlib  # noqa: E402

os.chdir(ROOT)
MODEL = os.environ.get('PT_MODEL', 'claude-fable-5-1')
EFFORT = os.environ.get('PT_EFFORT', 'high')
WEB_SLOTS = int(os.environ.get('PT_SLOTS', '16'))
client = anthropic.Anthropic(api_key=os.environ['PT_ANTHROPIC_API_KEY'], max_retries=10, timeout=3600)
TODAY = datetime.date.today().isoformat()
OLDCODE = {'J10': 'B9', 'E5': 'D5', 'E6': 'C6'}
# static donor -> receiver map from FINDINGS (used only to order work inside one run)
RECEIVES = {'C2': ['B5'], 'C8': ['C2'], 'G3': ['B5', 'B6', 'B7', 'B8', 'C8', 'G2', 'C2'], 'H4': ['H1'],
            'A4': ['H2'], 'J8': ['H2', 'J5'], 'J3': ['J5'], 'A2': ['B6'], 'E2': ['A1', 'A4', 'B1'],
            'C1': ['A1'], 'E4': ['A4', 'B4', 'C1'], 'H1': ['A3', 'B2'], 'B3': ['B4'], 'G1': ['B6', 'C1'],
            'H3': ['B6'], 'E1': ['E6'], 'B7': ['E6'], 'F3': ['B1'], 'F5': ['B1'], 'C4': ['A3']}
LOG_LOCK = threading.Lock()
MERGE_LOCK = threading.Lock()
class Slots:
    """Concurrency cap for web workers; the limit is re-read from work/slots.txt so it can be changed while running."""
    def __init__(self): self.n = 0; self.c = threading.Condition()
    def limit(self):
        try: return int(open(os.environ.get('PT_SLOTS_FILE', 'work/slots.txt')).read().strip())
        except Exception: return WEB_SLOTS
    def __enter__(self):
        with self.c:
            while self.n >= self.limit(): self.c.wait(timeout=30)
            self.n += 1
    def __exit__(self, *a):
        with self.c: self.n -= 1; self.c.notify_all()


SLOTS = Slots()


def log(*a):
    with LOG_LOCK:
        print(time.strftime('%H:%M:%S'), *a, flush=True)
        with open('work/run.log', 'a') as f: f.write(time.strftime('%H:%M:%S ') + ' '.join(map(str, a)) + '\n')


def W(code, *p):
    d = os.path.join('work', code, *p[:-1]) if len(p) > 1 else os.path.join('work', code)
    os.makedirs(d, exist_ok=True)
    return os.path.join('work', code, *p)


def jdump(o, p):
    tmp = p + '.tmp'
    json.dump(o, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, p)


# ---------------------------------------------------------------- documents
SCHEMA = open('SCHEMA.md').read()
RULES = open('RULES.md').read()
FINDINGS = open('FINDINGS.md').read()
META = json.load(open('meta.json'))
SEGMENTS = json.load(open('SEGMENTS.json'))['domains']


ALL_SEGS = {x for d in SEGMENTS.values() for x in d['segs']}


def seg_domain(code):
    return next((d for d, v in SEGMENTS.items() if code in v['cats']), 'general')


def seg_vocab(code):
    return SEGMENTS[seg_domain(code)]['segs']


def findings_row(code):
    want = OLDCODE.get(code, code)
    for line in FINDINGS.split('\n'):
        m = re.match(r'\|\s*([A-J]\d+)(?:\s*\(new\))?\s*\|', line)
        if m and m.group(1) == want: return line
    return ''


def cat_name(code):
    return next((c['n'] for c in META['cats'] if c['c'] == code), code)


def codes_list():
    return '\n'.join(f"{c['c']} {c['n']}" for c in META['cats'])


# ---------------------------------------------------------------- sources
def norm(u):
    if not u: return ''
    u = u.strip()
    try:
        p = urllib.parse.urlsplit(u)
    except Exception:
        return u
    host = p.netloc.lower().replace('www.', '').replace('.m.wikipedia.org', '.wikipedia.org')
    path = urllib.parse.unquote(p.path).rstrip('/').replace(' ', '_')
    q = ('?' + p.query) if p.query else ''
    return host + path + q


SRC_LOCK = threading.Lock()


def log_source(code, item, url, status):
    if not url: return
    with SRC_LOCK:
        p = W(code, 'sources.tsv')
        new = not os.path.exists(p)
        with open(p, 'a') as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            if new: f.write('item\turl\tretrieved\tstatus\n')
            f.write(f"{item}\t{url}\t{TODAY}\t{status}\n")
            fcntl.flock(f, fcntl.LOCK_UN)


def retrieved_set():
    s = set()
    for d in os.listdir('work'):
        p = os.path.join('work', d, 'sources.tsv')
        if not os.path.exists(p): continue
        for line in open(p):
            f = line.rstrip('\n').split('\t')
            if len(f) >= 4 and f[3] in ('fetched', 'api'): s.add(norm(f[1]))
    # the approved pilot's log, if present
    return s


# ---------------------------------------------------------------- old data
def old_kinds(code):
    d = json.load(open(f'reader/{code}.json'))
    out = []; n = 0
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                n += 1; out.append({'id': f'k{n}', 'dept': dp['n'], 'shelf': s['n'], 'kind': k})
    return d, out


def old_view(code):
    """Old file with an id on every kind, for the planner."""
    d, ks = old_kinds(code)
    it = iter(ks)
    for dp in d['depts']:
        for s in dp['s']:
            s['k'] = [dict(id=next(it)['id'], **k) for k in s['k']]
    return d, ks


def counts(d):
    k = a = m = 0
    for dp in d.get('depts', []):
        for s in dp['s']:
            for x in s['k']:
                k += 1; a += len(x.get('x') or []); m += len(x.get('m') or [])
                m += sum(len(ar.get('v') or []) for ar in x.get('x') or [])
    return k, a, m


def flat_models(d):
    return sum(len(x.get('m') or []) for dp in d.get('depts', []) for s in dp['s'] for x in s['k'])


def brand_count(d):
    b = set()
    for dp in d.get('depts', []):
        for s in dp['s']:
            for x in s['k']:
                for t in (x.get('m') or []) + (x.get('r') or []):
                    if len(t) == 2 and t[1]: b.add(t[1].lower())
                for ar in x.get('x') or []:
                    if ar.get('mk'): b.add(ar['mk'].lower())
    return len(b)


# ---------------------------------------------------------------- API helpers
def text_of(msg):
    return ''.join(b.text for b in msg.content if b.type == 'text')


def parse_json(t):
    m = re.search(r'```(?:json)?\s*(\{.*\})\s*```', t, re.S)
    s = m.group(1) if m else t[t.find('{'): t.rfind('}') + 1]
    return json.loads(s)


def run_batch(reqs, tag):
    """reqs: list of (custom_id, params). Returns {custom_id: text}. Resumable via work/_batches/<tag>.id."""
    os.makedirs('work/_batches', exist_ok=True)
    tag = os.environ.get('PT_TAG', '') + tag
    idp = f'work/_batches/{tag}.id'
    if os.path.exists(idp):
        bid = open(idp).read().strip()
    else:
        b = client.messages.batches.create(requests=[{'custom_id': c, 'params': p} for c, p in reqs])
        bid = b.id; open(idp, 'w').write(bid)
        log('batch', tag, bid, len(reqs), 'requests')
    while True:
        b = client.messages.batches.retrieve(bid)
        if b.processing_status == 'ended': break
        time.sleep(30)
    out = {}
    for r in client.messages.batches.results(bid):
        if r.result.type == 'succeeded':
            msg = r.result.message
            out[r.custom_id] = text_of(msg) if msg.stop_reason != 'refusal' else ''
            if msg.stop_reason not in ('end_turn',): log('batch', tag, r.custom_id, 'stop', msg.stop_reason)
        else:
            log('batch', tag, r.custom_id, r.result.type)
    os.remove(idp)
    return out


def stream_call(**kw):
    with client.beta.messages.stream(model=MODEL, max_tokens=kw.pop('max_tokens', 64000),
                                     output_config={'effort': EFFORT}, cache_control={'type': 'ephemeral'},
                                     betas=['server-side-fallback-2026-07-01'], fallbacks='default', **kw) as st:
        return st.get_final_message()


# ---------------------------------------------------------------- planning
PLAN_SPEC = """Return ONLY a JSON object (in a ```json fence) with this shape:
{"lead": "one sentence: what the category holds and how it is organised",
 "b": [],
 "depts": [{"n": "Dept name", "mode": "variety|tier|mixed", "note": "optional one line",
            "b": [{"m": "buying/quality criterion", "v": "ladder (optional)", "w": "why / where it comes from"}],
            "s": [{"n": "Shelf name", "web": true,
                   "brief": "instructions for the shelf worker: icons, archetypes, makers, traditions to add; trims; merges",
                   "k": [{"n": "Kind name", "old": ["k12", "k40"], "brief": "optional kind-level note"}]}]}],
 "moves": [{"old": "k33", "to": "<target category code>", "dept": "suggested dept in the target"}],
 "drop": [{"old": "k77", "why": "short reason"}]}
Planning rules:
- Every old kind id (k1, k2, …) must appear EXACTLY ONCE across depts[].s[].k[].old, moves[].old and drop[].old. Merging several old kinds into one kind is done by listing several ids in "old".
- A kind with "old": [] is a NEW kind; new kinds are allowed only on shelves with "web": true (the worker must source them).
- "web": false only for shelves that need no new kinds and no archetypes (pure restraint: trims, merges, renames, types). Every hobbyist/variety shelf is "web": true.
- Keep each web shelf to at most ~14 kinds (split big shelves) so one worker can research it properly.
- Department and shelf names readers would guess; order departments, shelves and kinds by significance.
- Moves only where RULES.md / the findings send a kind to another category. Valid target codes:
{codes}
- Drop only what the rules put out of scope (trade/institutional, SKU noise, duplicates already merged elsewhere)."""


def plan_params(code):
    d, ks = old_view(code)
    sys_txt = f"{SCHEMA}\n\n---\n{RULES}"
    recv = ''
    if not ks:
        recv = '\nThis is a NEW category with no data yet: plan it from the findings row, with every shelf "web": true.'
    user = (f"Category {code} {cat_name(code)}.\nOwner-approved findings row for this category:\n{findings_row(code)}\n\n"
            f"STEP 1 of the rebuild: plan the new structure. Workers will then rebuild each shelf with web research.{recv}\n\n"
            + PLAN_SPEC.replace('{codes}', codes_list()) +
            f"\n\nCurrent data (schema v1, every kind tagged with an id):\n```json\n{json.dumps(d, ensure_ascii=False)}\n```")
    return {'model': MODEL, 'max_tokens': 100000, 'output_config': {'effort': EFFORT},
            'system': sys_txt, 'messages': [{'role': 'user', 'content': user}]}, ks


def check_plan(plan, ks):
    ids = [k['id'] for k in ks]; seen = {}
    for dp in plan.get('depts', []):
        if dp.get('mode') not in ('variety', 'tier', 'mixed'): dp['mode'] = 'mixed'
        for s in dp.get('s', []):
            for k in s.get('k', []):
                for o in k.get('old', []): seen[o] = seen.get(o, 0) + 1
    for m in plan.get('moves', []) + plan.get('drop', []):
        seen[m['old']] = seen.get(m['old'], 0) + 1
    missing = [i for i in ids if i not in seen]
    dup = [i for i, n in seen.items() if n > 1]
    unknown = [i for i in seen if i not in set(ids)]
    return missing, dup, unknown


def fix_plan(plan, ks):
    """Mechanical clean-up after the model's repair attempt: drop dup/unknown refs, park missing ids on their old shelf name."""
    ids = {k['id'] for k in ks}; used = set()
    for dp in plan['depts']:
        for s in dp['s']:
            for k in s['k']:
                k['old'] = [o for o in k.get('old', []) if o in ids and not (o in used or used.add(o))]
    plan['moves'] = [m for m in plan.get('moves', []) if m['old'] in ids and not (m['old'] in used or used.add(m['old']))]
    plan['drop'] = [m for m in plan.get('drop', []) if m['old'] in ids and not (m['old'] in used or used.add(m['old']))]
    miss = [k for k in ks if k['id'] not in used]
    if miss:
        dp = plan['depts'][-1] if plan['depts'] else None
        if dp is None:
            dp = {'n': 'Unsorted', 'mode': 'mixed', 'b': [], 's': []}; plan['depts'].append(dp)
        sh = {'n': 'Kept as found', 'web': False, 'brief': 'Kinds the planner did not place; tidy only.', 'k': []}
        for k in miss: sh['k'].append({'n': k['kind']['n'], 'old': [k['id']]})
        dp['s'].append(sh)
        plan.setdefault('_notes', []).append(f"{len(miss)} unplaced kinds parked")


def plan_codes(codes):
    todo = [c for c in codes if not os.path.exists(W(c, 'plan.json'))]
    if not todo: return
    reqs = []; kss = {}
    for c in todo:
        p, ks = plan_params(c); reqs.append((c, p)); kss[c] = ks
    res = run_batch(reqs, 'plan_' + '_'.join(todo))
    for c in todo:
        t = res.get(c, '')
        try:
            plan = parse_json(t)
        except Exception:
            log(c, 'plan parse failed; retrying with streaming'); p, _ = plan_params(c)
            p.pop('model'); p.pop('output_config')
            plan = parse_json(text_of(stream_call(**p)))
        missing, dup, unknown = check_plan(plan, kss[c])
        if missing or dup or unknown:
            log(c, 'plan repair', len(missing), 'missing', len(dup), 'dup', len(unknown), 'unknown')
            names = {k['id']: k['kind']['n'] for k in kss[c]}
            ask = (f"Your plan below has problems. Missing ids: {[(i, names[i]) for i in missing]}. "
                   f"Ids used more than once: {dup}. Unknown ids: {unknown}. Return the corrected full plan JSON.\n\n```json\n{json.dumps(plan, ensure_ascii=False)}\n```")
            p, _ = plan_params(c); p.pop('model'); p.pop('output_config')
            p['messages'] = [p['messages'][0], {'role': 'assistant', 'content': '```json\n' + json.dumps(plan, ensure_ascii=False) + '\n```'},
                             {'role': 'user', 'content': ask}]
            try:
                plan = parse_json(text_of(stream_call(**p)))
            except Exception as e:
                log(c, 'plan repair failed', e)
        fix_plan(plan, kss[c])
        jdump(plan, W(c, 'plan.json'))
        n_sh = sum(len(dp['s']) for dp in plan['depts'])
        log(c, 'planned', len(plan['depts']), 'depts', n_sh, 'shelves', len(plan.get('moves', [])), 'moves', len(plan.get('drop', [])), 'drops')


# ---------------------------------------------------------------- shelf workers
WORKER_RULES = """You are a shelf worker in the rebuild. You rebuild ONE shelf of ONE category into schema v2 kinds.
Tools: web_search and web_fetch (server side; you may call web_fetch for several URLs inside one code block),
wiki (Wikipedia search / page extracts, throttled), wikidata (search, entities, SPARQL), submit (final answer).

Everything you need (SCHEMA.md, RULES.md, findings, plan, old data) is in this prompt; the code sandbox has no repository
files, so do not look for them.

Hard rules
- Attestation: every archetype "s", every NEW kind "s", every brand "s" and every tradition "s" must be a URL you actually
  retrieved in THIS session with web_fetch (successful) or the wiki/wikidata tools (an existing page/entity). Search result
  snippets do not count. Never type a URL you have not retrieved; never guess URLs. Kinds carried over from the old data may
  keep their old "s".
- Never invent facts. Versions, years, references and makers must come from a retrieved page or the old data; leave out
  anything you cannot confirm.
- Follow SCHEMA.md exactly (KIND / ARCHETYPE / BRAND / TRADITION shapes). Archetype "mk" must equal the brand-register name
  you give the brand. Order archetypes by significance (originator, reference versions, then the rest), never alphabetically.
- Tier kinds: market-covering brands plus independent test winners, about 5–12 models; no SKU dumps. Variety kinds: kind →
  archetype → version → detail; existing models that belong to an archetype become its versions; good models with no
  archetype may stay in "m". Attribute-only variants go into "t".
- Keep every old kind listed for this shelf (merged as the plan says) unless the rules clearly put it out of scope; say
  in notes what you dropped and why.
- Brands: add a register entry for each brand that is an archetype "mk" (or a core brand of a tier kind). Cite a retrieved
  page when you have one; for a well-known brand whose facts (country, founding year, owner, segment) you know reliably,
  you may record it from your own knowledge with "s":"knowledge" (owner decision). Leave out any fact you are unsure of. Traditions: add where artisan traditions matter for this shelf.
- Blocked maker/retailer site? Do not drop the item: establish it from an independent page that names it (owner decision).
  Prefer outside databases and lists over the maker's own site: Wikipedia articles and "List of ..." pages; company
  registers (Companies House, OpenCorporates, national registers); trademark registers (WIPO Global Brand Database, USPTO,
  EUIPO/TMview); museum and collection records (V&A, Science Museum, Smithsonian, Cooper Hewitt, Met); trade-association
  member or award lists; independent test and review sites; standards/certification listings; and other retailers that
  list the product. Find them by search, never by guessing URLs; a fetched page that names the product and maker attests
  it. If WebFetch is blocked you may retry the same URL through the authenticated Firecrawl or Parallel connectors
  (owner decision 2026-10-27: they are legitimate connectors); if those fail too, use the independent sources above.
- Be efficient: batch fetches in code (fetch many URLs per call, print only the facts you need). Aim to finish within
  roughly 25 tool rounds. Wikipedia article URLs (https://en.wikipedia.org/wiki/Title) are good sources; web_fetch them
  directly when you know the exact title, or use the wiki tool to confirm titles in bulk.
- When done call submit with {"kinds": [...], "brands": [...], "traditions": [...], "notes": "what you left out and why"}.
  submit checks the output and may return errors; fix them (retrieve the page or remove the item) and submit again."""

CLIENT_TOOLS = [
    {'name': 'wiki', 'description': 'English Wikipedia via the throttled shared helper. Give "search" (a query) and/or "titles" (exact article titles, up to 40). Titles return existence, canonical URL and the intro extract; an existing page counts as retrieved.',
     'input_schema': {'type': 'object', 'properties': {'search': {'type': 'string'}, 'titles': {'type': 'array', 'items': {'type': 'string'}}}}},
    {'name': 'wikidata', 'description': 'Wikidata via the throttled helper. "search": entity search; "ids": fetch entities (labels, description, P31, country, inception, manufacturer, enwiki title) — fetched entities count as retrieved; "sparql": run a SELECT query (max 300 rows; entity URIs in results count as retrieved).',
     'input_schema': {'type': 'object', 'properties': {'search': {'type': 'string'}, 'ids': {'type': 'array', 'items': {'type': 'string'}}, 'sparql': {'type': 'string'}}}},
    {'name': 'submit', 'description': 'Submit the finished shelf. kinds = schema v2 KIND objects; brands = BRAND objects; traditions = TRADITION objects; notes = what was left out and why.',
     'eager_input_streaming': True,
     'input_schema': {'type': 'object', 'properties': {'kinds': {'type': 'array', 'items': {'type': 'object'}}, 'brands': {'type': 'array', 'items': {'type': 'object'}},
                                                         'traditions': {'type': 'array', 'items': {'type': 'object'}}, 'notes': {'type': 'string'}}, 'required': ['kinds']}},
]
WEB_TOOLS = [{'type': 'web_search_20260209', 'name': 'web_search', 'max_uses': 60},
             {'type': 'web_fetch_20260209', 'name': 'web_fetch', 'max_uses': 150}]
MAXM = {'tier': 12, 'mixed': 20, 'variety': 40}


def shelf_jobs(code, plan):
    for i, dp in enumerate(plan['depts']):
        for j, s in enumerate(dp['s']):
            yield f'{i:02d}_{j:02d}', dp, s


def shelf_context(code, plan, dp, s, ks_by_id):
    outline = []
    for d2 in plan['depts']:
        outline.append(f"- {d2['n']} [{d2['mode']}]: " + '; '.join(f"{s2['n']} ({', '.join(k['n'] for k in s2['k'])})" for s2 in d2['s']))
    old = []
    for k in s['k']:
        for o in k.get('old', []):
            if o in ks_by_id: old.append(dict(target_kind=k['n'], **ks_by_id[o]['kind']))
    return (f"Category {code} {cat_name(code)}. Category lead: {plan.get('lead', '')}\n"
            f"Owner-approved findings row:\n{findings_row(code)}\n\nWhole-category outline (for context; other workers do the other shelves):\n"
            + '\n'.join(outline) +
            f"\n\nYOUR SHELF: department \"{dp['n']}\" (mode {dp['mode']}), shelf \"{s['n']}\".\nShelf brief: {s.get('brief', '')}\n"
            f"Planned kinds (name, old ids merged in, note):\n" +
            '\n'.join(f"- {k['n']} | old: {k.get('old', [])} | {k.get('brief', '')}" for k in s['k']) +
            f"\n\nOld data for this shelf (schema v1; target_kind = the planned kind it goes into):\n```json\n{json.dumps(old, ensure_ascii=False)}\n```")


def check_shelf(code, dp, s, out, ks_by_id, retrieved, final=False):
    """Return (errors, cleaned_output, dropped_notes)."""
    errs, dropped = [], []
    planned = {k['n'].lower(): k for k in s['k']}
    old_s = {}
    for k in s['k']:
        for o in k.get('old', []):
            if o in ks_by_id and ks_by_id[o]['kind'].get('s'): old_s.setdefault(k['n'].lower(), set()).add(norm(ks_by_id[o]['kind']['s']))
    all_old_s = set().union(*old_s.values()) if old_s else set()
    ok = lambda u: bool(u) and norm(u) in retrieved
    kinds = []
    for k in out.get('kinds') or []:
        if not isinstance(k, dict) or not k.get('n') or not k.get('d'):
            errs.append(f"kind {k.get('n') if isinstance(k, dict) else k}: needs n and d"); continue
        nm = k['n']; is_new = nm.lower() not in planned or not planned[nm.lower()].get('old')
        if nm.lower().startswith('other '): errs.append(f"kind {nm}: catch-all name 'Other …' not allowed")
        if is_new and not ok(k.get('s')):
            errs.append(f"kind {nm}: NEW kind needs s = a URL you retrieved (got {k.get('s')!r})")
            if final: dropped.append(f"kind {nm} (unsourced)"); continue
        elif not is_new and k.get('s') and not ok(k['s']) and norm(k['s']) not in all_old_s:
            errs.append(f"kind {nm}: s {k['s']!r} is neither the old source nor a retrieved URL")
            if final: k['s'] = ks_by_id[planned[nm.lower()]['old'][0]]['kind'].get('s', '') if planned[nm.lower()]['old'][0] in ks_by_id else ''
        xs = []
        for x in k.get('x') or []:
            if not isinstance(x, dict) or not x.get('n'):
                errs.append(f"kind {nm}: archetype without n"); continue
            if not ok(x.get('s')):
                errs.append(f"kind {nm} / archetype {x['n']}: s must be a URL you retrieved (got {x.get('s')!r})")
                if final: dropped.append(f"archetype {x['n']} in {nm} (unsourced)"); continue
            x['v'] = [v for v in (x.get('v') or []) if isinstance(v, dict) and v.get('n')]
            xs.append(x)
        if k.get('x') is not None: k['x'] = xs
        for key in ('m', 'r'):
            if key in k:
                good = []; seen = set()
                for t in k[key] or []:
                    if isinstance(t, list) and len(t) == 2 and all(isinstance(z, str) for z in t) and tuple(t) not in seen:
                        seen.add(tuple(t)); good.append(t)
                    else:
                        errs.append(f"kind {nm}: bad or duplicate {key} entry {t!r} (must be [\"model\",\"maker\"])")
                k[key] = good
        lim = MAXM[dp['mode']]
        if len(k.get('m') or []) > lim:
            errs.append(f"kind {nm}: {len(k['m'])} flat models — trim to ≤{lim} (market-covering brands + test winners) or turn families into archetypes")
            if final: dropped.append(f"{len(k['m']) - lim} flat models in {nm} (trim)"); k['m'] = k['m'][:lim]
        kinds.append(k)
    names = [k['n'].lower() for k in kinds]
    if len(names) != len(set(names)): errs.append('duplicate kind names in this shelf')
    missing = [k['n'] for k in s['k'] if k.get('old') and k['n'].lower() not in set(names)]
    if missing and not final:
        errs.append(f"planned kinds missing from your output: {missing} (keep them, or explain in notes why they are out of scope and resubmit with notes)")
        if (out.get('notes') or '') and all(m.lower() in (out.get('notes') or '').lower() for m in missing): errs.pop()
    brands = []
    vocab = seg_vocab(code)
    for b in out.get('brands') or []:
        if not isinstance(b, dict) or not b.get('n'): continue
        if b.get('seg') not in vocab and b.get('seg') not in ALL_SEGS:  # owner: controlled vocabulary (SEGMENTS.json); a brand keeps the segment of its strongest domain (e.g. Hermès = Luxury house on a saddle shelf)
            if final: b['seg'] = ''
            else: errs.append(f"brand {b.get('n')}: seg must be one of {vocab} (got {b.get('seg')!r}); put the specialty in \"kf\"")
        if b.get('s') == 'knowledge': b['s'] = ''; brands.append(b); continue  # owner: well-known brand facts may come from model knowledge
        if not ok(b.get('s')):
            errs.append(f"brand {b.get('n')}: s must be a URL you retrieved (got {b.get('s')!r})")
            if final: dropped.append(f"brand {b['n']} (unsourced)"); continue
        brands.append(b)
    trads = []
    for t in out.get('traditions') or []:
        if not isinstance(t, dict) or not t.get('n'): continue
        if not ok(t.get('s')):
            errs.append(f"tradition {t.get('n')}: s must be a URL you retrieved (got {t.get('s')!r})")
            if final: dropped.append(f"tradition {t['n']} (unsourced)"); continue
        trads.append(t)
    return errs, {'kinds': kinds, 'brands': brands, 'traditions': trads, 'notes': out.get('notes', '')}, dropped


def handle_client_tool(code, job, name, inp):
    try:
        if name == 'wiki':
            res = {}
            if inp.get('search'):
                st, r = netlib.wiki_search(inp['search'], 8); res['search'] = r if r or st == 200 else f'error HTTP {st}; use web_search/web_fetch instead'
            if inp.get('titles'):
                st, r = netlib.wiki_pages(inp['titles'][:40])
                for p in r:
                    if p.get('exists') and p.get('url'): log_source(code, job, p['url'], 'api')
                res['pages'] = r
            return json.dumps(res, ensure_ascii=False)[:30000]
        if name == 'wikidata':
            res = {}
            if inp.get('search'): res['search'] = netlib.wd_search(inp['search'], 8)[1]
            if inp.get('ids'):
                st, r = netlib.wd_entities(inp['ids'])
                for e in r:
                    if e.get('exists'): log_source(code, job, e['url'], 'api')
                res['entities'] = r
            if inp.get('sparql'):
                st, r = netlib.wd_sparql(inp['sparql'])
                for row in r:
                    for v in row.values():
                        if isinstance(v, str) and v.startswith('http://www.wikidata.org/entity/Q'):
                            log_source(code, job, 'https://www.wikidata.org/wiki/' + v.rsplit('/', 1)[1], 'api')
                res['sparql'] = r if r or st == 200 else f'error HTTP {st}'
            return json.dumps(res, ensure_ascii=False)[:40000]
    except Exception as e:
        return f'tool error: {e}'
    return 'unknown tool'


def log_server_results(code, job, content):
    for b in content:
        if b.type == 'web_fetch_tool_result':
            c = b.content
            ct = getattr(c, 'type', None)
            if ct == 'web_fetch_result':
                log_source(code, job, c.url, 'fetched')
            else:
                log_source(code, job, getattr(c, 'url', '') or '-', 'fetch_error:' + str(getattr(c, 'error_code', ct)))
        elif b.type == 'web_search_tool_result' and isinstance(b.content, list):
            for r in b.content[:10]:
                if getattr(r, 'url', None): log_source(code, job, r.url, 'search')


def run_web_job(code, plan, job, dp, s, ks_by_id):
    outp = W(code, 'shelves', job + '.json')
    if os.path.exists(outp): return
    with SLOTS:
        log(code, job, 'start', dp['n'], '/', s['n'], f"({len(s['k'])} kinds)")
        system = [{'type': 'text', 'text': f"{SCHEMA}\n\n---\n{RULES}\n\n---\n{WORKER_RULES}"}]
        msgs = [{'role': 'user', 'content': shelf_context(code, plan, dp, s, ks_by_id)}]
        tpath = W(code, 'transcripts', job + '.jsonl')
        tries = 0; turns = 0; result = None; nudged = False; usage = [0, 0, 0]
        while turns < 80:
            turns += 1
            try:
                resp = stream_call(system=system, messages=msgs, tools=WEB_TOOLS + CLIENT_TOOLS)
            except anthropic.BadRequestError as e:
                log(code, job, 'bad request', str(e)[:300]); break
            except Exception as e:
                log(code, job, 'api error', repr(e)[:300]); time.sleep(30); continue
            u = resp.usage
            usage[0] += u.input_tokens + (u.cache_creation_input_tokens or 0); usage[1] += u.cache_read_input_tokens or 0; usage[2] += u.output_tokens
            log_server_results(code, job, resp.content)
            with open(tpath, 'a') as f:
                f.write(json.dumps({'turn': turns, 'stop': resp.stop_reason, 'model': resp.model,
                                    'text': text_of(resp)[:2000], 'tools': [getattr(b, 'name', '') for b in resp.content if b.type in ('tool_use', 'server_tool_use')]}) + '\n')
            msgs.append({'role': 'assistant', 'content': resp.content})
            if resp.stop_reason == 'refusal':
                log(code, job, 'refusal'); break
            if resp.stop_reason == 'pause_turn': continue
            uses = [b for b in resp.content if b.type == 'tool_use']
            if not uses:
                if resp.stop_reason == 'max_tokens':
                    msgs.append({'role': 'user', 'content': 'You hit the output limit. Continue, and call submit when ready.'}); continue
                msgs.append({'role': 'user', 'content': 'Call the submit tool with the finished shelf now.'}); continue
            results = []
            for b in uses:
                if b.name == 'submit':
                    inp = b.input if isinstance(b.input, dict) else {}
                    tries += 1
                    errs, clean, dropped = check_shelf(code, dp, s, inp, ks_by_id, retrieved_set(), final=tries >= 4)
                    if errs and tries < 4:
                        results.append({'type': 'tool_result', 'tool_use_id': b.id, 'is_error': True,
                                        'content': 'Not accepted. Fix and resubmit:\n- ' + '\n- '.join(errs[:80])})
                    else:
                        result = dict(clean, dropped=dropped, usage=usage, turns=turns, model=resp.model)
                        results.append({'type': 'tool_result', 'tool_use_id': b.id, 'content': 'Accepted.'})
                else:
                    results.append({'type': 'tool_result', 'tool_use_id': b.id, 'content': handle_client_tool(code, job, b.name, b.input or {})})
            msgs.append({'role': 'user', 'content': results})
            if result: break
            ctx = u.input_tokens + (u.cache_read_input_tokens or 0) + (u.cache_creation_input_tokens or 0)
            if not nudged and (turns >= 45 or ctx > 500000):
                msgs.append({'role': 'system', 'content': 'Budget nearly used: stop researching and call submit now with what is verified.'}); nudged = True
        if result is None:
            log(code, job, 'FAILED (no accepted submit)', f'turns={turns}'); return
        jdump(result, outp)
        log(code, job, 'done', f"kinds={len(result['kinds'])} arch={sum(len(k.get('x') or []) for k in result['kinds'])} brands={len(result['brands'])} turns={turns} in={usage[0]} cached={usage[1]} out={usage[2]}")


def run_nonweb_jobs(code, plan, jobs, ks_by_id):
    todo = [(job, dp, s) for job, dp, s in jobs if not os.path.exists(W(code, 'shelves', job + '.json'))]
    if not todo: return
    sys_txt = f"{SCHEMA}\n\n---\n{RULES}"
    reqs = []
    for job, dp, s in todo:
        user = (shelf_context(code, plan, dp, s, ks_by_id) +
                "\n\nThis is a RESTRAINT-ONLY shelf (no web research): keep, merge, rename or drop the old kinds as planned, move "
                "attribute-only variants into \"t\", trim model lists to market-covering brands plus independent test winners "
                f"(≤{MAXM[dp['mode']]} per kind), write plain one-sentence definitions, keep each kind's old \"s\". Do not add archetypes, "
                "new kinds or brand entries. Return ONLY JSON in a ```json fence: {\"kinds\": [KIND, …], \"notes\": \"what you dropped and why\"}.")
        reqs.append((job, {'model': MODEL, 'max_tokens': 32000, 'output_config': {'effort': EFFORT}, 'system': sys_txt,
                           'messages': [{'role': 'user', 'content': user}]}))
    res = run_batch(reqs, f'shelves_{code}')
    ret = retrieved_set()
    for job, dp, s in todo:
        try:
            out = parse_json(res.get(job, ''))
        except Exception:
            log(code, job, 'non-web parse failed'); continue
        for k in out.get('kinds', []):
            k.pop('x', None)
        _, clean, dropped = check_shelf(code, dp, s, out, ks_by_id, ret, final=True)
        clean['brands'] = []; clean['traditions'] = []
        jdump(dict(clean, dropped=dropped, model=MODEL, batch=True), W(code, 'shelves', job + '.json'))
        log(code, job, 'done (batch)', f"kinds={len(clean['kinds'])}")


def shelves(code):
    plan = json.load(open(W(code, 'plan.json')))
    _, ks = old_kinds(code); ks_by_id = {k['id']: k for k in ks}
    jobs = list(shelf_jobs(code, plan))
    web = [j for j in jobs if j[2].get('web', True)]
    nonweb = [j for j in jobs if not j[2].get('web', True)]
    with cf.ThreadPoolExecutor(max_workers=len(web) + 1) as ex:
        futs = [ex.submit(run_web_job, code, plan, job, dp, s, ks_by_id) for job, dp, s in web]
        if nonweb: futs.append(ex.submit(run_nonweb_jobs, code, plan, nonweb, ks_by_id))
        for f in futs:
            try: f.result()
            except Exception: log(code, 'job crashed', traceback.format_exc()[-800:])


# ---------------------------------------------------------------- assemble
def assemble(code):
    plan = json.load(open(W(code, 'plan.json')))
    old, ks = old_kinds(code); ks_by_id = {k['id']: k for k in ks}
    ret = retrieved_set()
    out = {'c': code, 'rev': True, 'lead': plan.get('lead', ''), 'b': plan.get('b', []), 'depts': []}
    brands, trads, notes, dropped, missing_jobs = {}, {}, [], [], []
    seen = set()
    for job, dp, s in shelf_jobs(code, plan):
        p = W(code, 'shelves', job + '.json')
        if not os.path.exists(p):
            missing_jobs.append(f"{dp['n']} / {s['n']}")
            # fall back to the old kinds, untouched, so nothing is lost
            res = {'kinds': [], 'brands': [], 'traditions': []}
            for k in s['k']:
                olds = [ks_by_id[o]['kind'] for o in k.get('old', []) if o in ks_by_id]
                if olds:
                    nk = dict(olds[0], n=k['n'])
                    for o in olds[1:]:
                        nk['m'] = (nk.get('m') or []) + [t for t in (o.get('m') or []) if t not in (nk.get('m') or [])]
                    res['kinds'].append(nk)
        else:
            res = json.load(open(p))
            _, clean, dr = check_shelf(code, dp, s, res, ks_by_id, ret, final=True)
            dropped += res.get('dropped', []) + dr; res = dict(res, **clean)
            if res.get('notes'): notes.append(f"{s['n']}: {res['notes']}")
        D = next((d for d in out['depts'] if d['n'] == dp['n']), None)
        if D is None:
            D = {'n': dp['n'], 'mode': dp['mode'], 'b': dp.get('b', []), 's': []}
            if dp.get('note'): D['note'] = dp['note']
            out['depts'].append(D)
        kinds = []
        for k in res['kinds']:
            if k['n'].lower() in seen:
                k['n'] = f"{k['n']} ({s['n']})"
                if k['n'].lower() in seen: continue
            seen.add(k['n'].lower()); kinds.append(k)
        if kinds:
            sh = next((x for x in D['s'] if x['n'] == s['n']), None)
            if sh: sh['k'] += kinds
            else: D['s'].append({'n': s['n'], 'k': kinds})
        for b in res.get('brands', []):
            o = brands.get(b['n'].lower())
            if o is None: brands[b['n'].lower()] = b
            else:
                for f in ('lines', 'eras', 'sig', 'sc', 'rel'):
                    o[f] = list(dict.fromkeys((o.get(f) or []) + (b.get(f) or [])))
                for f in ('c', 'f', 'seg', 'd', 's'):
                    if not o.get(f) and b.get(f): o[f] = b[f]
        for t in res.get('traditions', []):
            o = trads.get(t['n'].lower())
            if o is None: trads[t['n'].lower()] = t
            else: o['forms'] = list(dict.fromkeys((o.get('forms') or []) + (t.get('forms') or [])))
    out['depts'] = [d for d in out['depts'] if d['s']]
    moves = []
    for m in plan.get('moves', []):
        if m['old'] in ks_by_id:
            moves.append({'to': m['to'], 'dept': m.get('dept', ''), 'kind': ks_by_id[m['old']]['kind']})
    jdump(out, f'out/{code}.json'); jdump({'b': sorted(brands.values(), key=lambda b: b['n'].lower())}, f'out/{code}_brands.json')
    jdump({'t': list(trads.values())}, f'out/{code}_traditions.json'); jdump({'out': moves}, f'out/{code}_moves.json')
    b4 = counts(old); af = counts(out)
    modes = sorted({(d['n'], d['mode']) for d in out['depts']}, key=lambda x: x[0])
    rep = [f"# {code} {cat_name(code)} — rebuild report", '',
           '**Brand mode:** ' + '; '.join(f"{n}: {m}" for n, m in modes), '',
           f"**Counts (before → after):** {len(old['depts'])} → {len(out['depts'])} departments · {b4[0]} → {af[0]} kinds · "
           f"{b4[1]} → {af[1]} archetypes · {flat_models(old)} → {flat_models(out)} flat models · {b4[2]} → {af[2]} models+versions · "
           f"{brand_count(old)} → {brand_count(out)} brands named · register {len(brands)} brands, {len(trads)} traditions · moves out {len(moves)} · dropped kinds {len(plan.get('drop', []))}.", '',
           f"**Sources:** {len({norm(l.split(chr(9))[1]) for l in open(W(code, 'sources.tsv')).readlines()[1:] if l.split(chr(9))[3].strip() in ('fetched', 'api')}) if os.path.exists(W(code, 'sources.tsv')) else 0} distinct retrieved URLs logged in work/{code}/sources.tsv (server web_fetch, Wikipedia/Wikidata APIs).", '']
    if plan.get('drop'):
        rep.append('**Dropped (scope rule):** ' + '; '.join(f"{ks_by_id[d['old']]['kind']['n']} ({d.get('why', '')})" for d in plan['drop'] if d['old'] in ks_by_id)[:900])
    if missing_jobs: rep.append('**Shelves not rebuilt (old kinds kept as found):** ' + '; '.join(missing_jobs))
    if dropped: rep.append(f"**Left out for lack of a retrieved source or over limits:** {len(dropped)} items, e.g. " + '; '.join(dropped[:12]))
    if notes: rep.append('**Worker notes:** ' + ' | '.join(n[:220] for n in notes)[:1400])
    open(f'out/{code}_report.md', 'w').write('\n'.join(rep) + '\n')
    log(code, 'assembled', f"kinds {b4[0]}->{af[0]} arch {b4[1]}->{af[1]} flat {flat_models(old)}->{flat_models(out)} brands-register {len(brands)} missing-shelves {len(missing_jobs)}")
    return not missing_jobs


def validate_and_merge(code):
    r = subprocess.run([sys.executable, 'validate.py', f'out/{code}.json'], capture_output=True, text=True)
    log(code, 'validate', r.stdout.strip()[:500])
    if r.returncode != 0: return False
    with MERGE_LOCK, open('work/.merge.lock', 'a') as lf:
        fcntl.flock(lf, fcntl.LOCK_EX)  # serialise merges across processes
        r = subprocess.run([sys.executable, 'merge.py', code], capture_output=True, text=True)
        log(code, 'merge', (r.stdout + r.stderr).strip()[-600:])
    return r.returncode == 0


def pipeline(code, run_codes, merged, cond):
    deps = [d for d in RECEIVES.get(code, []) if d in run_codes and d != code]
    with cond:
        cond.wait_for(lambda: all(d in merged for d in deps))
    # donors being rebuilt by another process (PT_EXTERNAL="B5 B6 ..."): wait until merge.py records them in done.json
    ext = [d for d in RECEIVES.get(code, []) if d in os.environ.get('PT_EXTERNAL', '').split()]
    while ext and not all(d in json.load(open('done.json')) for d in ext):
        time.sleep(60)
    try:
        plan_codes([code]); shelves(code)
        ok = assemble(code)
        if ok and validate_and_merge(code):
            with cond: merged.add(code); cond.notify_all()
        else:
            log(code, 'NOT merged (missing shelves or validation failure)')
            with cond: merged.add(code); cond.notify_all()
    except Exception:
        log(code, 'pipeline crashed', traceback.format_exc()[-1500:])
        with cond: merged.add(code); cond.notify_all()


if __name__ == '__main__':
    cmd, codes = sys.argv[1], sys.argv[2:]
    os.makedirs('work', exist_ok=True)
    if cmd == 'plan': plan_codes(codes)
    elif cmd == 'shelves':
        with cf.ThreadPoolExecutor(len(codes)) as ex: list(ex.map(shelves, codes))
    elif cmd == 'assemble':
        for c in codes: assemble(c)
    elif cmd == 'merge':
        for c in codes: validate_and_merge(c)
    elif cmd == 'go':
        merged, cond = set(), threading.Condition()
        with cf.ThreadPoolExecutor(len(codes)) as ex:
            list(ex.map(lambda c: pipeline(c, set(codes), merged, cond), codes))
