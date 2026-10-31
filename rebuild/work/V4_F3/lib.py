import json, os
W = '/home/user/Possession-Taxonomy/rebuild'
WP = 'https://en.wikipedia.org/wiki/'

def V(n, y='', d='', mk=''):
    return {'n': n, 'mk': mk, 'y': str(y), 'd': d}

def E(n, d, y='', mk='', g='', s='', v=None, a='', role=None, dt=None):
    e = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': str(y), 's': s}
    if v: e['v'] = v
    if dt: e['dt'] = dt
    if g: e['g'] = g
    if role: e['role'] = role
    return e

def load():
    return json.load(open(W + '/work/V4_F3/bak/F3.json'))

def kinds(d):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                yield dp, s, k

def kind(d, name):
    for dp, s, k in kinds(d):
        if k['n'] == name:
            return k
    raise KeyError(name)

def section(d, dept, sec):
    for dp in d['depts']:
        if dp['n'] == dept:
            for s in dp['s']:
                if s['n'] == sec:
                    return s
    raise KeyError(sec)

def names(k):
    return {x['n'].casefold() for x in k.get('x', [])}

def add(k, entries):
    """Append entries not already present (by name)."""
    have = names(k)
    k.setdefault('x', [])
    n = 0
    for e in entries:
        if e['n'].casefold() in have:
            continue
        k['x'].append(e); have.add(e['n'].casefold()); n += 1
    return n

def setg(k, mapping, default=None):
    for x in k.get('x', []):
        if x['n'] in mapping:
            x['g'] = mapping[x['n']]
        elif default and not x.get('g'):
            x['g'] = default(x) if callable(default) else default

def promote_m(k, report, s_override=None, g=''):
    """Promote loose models with a named maker to entries; drop the others."""
    prom = drop = 0
    out = []
    for m in k.get('m') or []:
        nm, mk = m[0], m[1]
        if mk and nm.casefold() not in names(k):
            k.setdefault('x', []).append(E(nm, f'Listed by {mk}.', mk=mk, g=g or mk, s=s_override or k.get('s', '')))
            prom += 1
        else:
            drop += 1
    k['m'] = []
    report.append((k['n'], 'promoted', prom, 'dropped', drop))

def order(k, sections):
    """sort entries by section order then year then name"""
    idx = {s: i for i, s in enumerate(sections)}
    def key(x):
        y = ''.join(c for c in str(x.get('y', ''))[:4] if c.isdigit())
        return (idx.get(x.get('g'), 999), int(y) if y else 9999, x['n'])
    k['x'].sort(key=key)

def save(d):
    p = W + '/out/F3.json'
    with open(p + '.tmp', 'w') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    os.replace(p + '.tmp', p)
