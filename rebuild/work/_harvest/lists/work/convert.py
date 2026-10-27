import sys, os, json, shutil, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
W = os.path.dirname(os.path.abspath(__file__)) + '/'
meta = json.load(open(W + 'lists_of_adds.json'))
rows = [l.rstrip('\n').split('\t') for l in open(R + 'work/_harvest/lists/decisions.tsv')][1:]
def dtext(n, cat, src):
    ls = meta.get(n, [])
    shops = [NICE[x] for x in ['luckyscent', 'sephora', 'notino', 'nordstrom', 'fashiola'] if x in ls]
    fp = 'fragrantica_popular' in ls
    if cat != 'H4' and src not in ('luckyscent', 'fragrantica_popular'): return ''
    kind = 'Niche perfume house' if 'luckyscent' in ls else 'Perfume house' if cat == 'H4' else 'Brand'
    parts = []
    if shops: parts.append('stocked by ' + (' and '.join(shops) if len(shops) < 3 else ', '.join(shops[:-1]) + ' and ' + shops[-1]))
    if fp: parts.append("listed among Fragrantica's most popular designers")
    return kind + ' ' + '; '.join(parts) + '.' if parts else ''
by = collections.defaultdict(list)
for name, l, a, n, cat, seg, kf, c, f, why in rows:
    if a != 'add': continue
    e = {'n': n, 'seg': seg, 'kf': kf, 's': SRC[l]}
    if c: e['c'] = c
    if f: e['f'] = f
    d = dtext(n, cat, l)
    if d: e['d'] = d
    by[cat].append(e)
os.makedirs(R + 'bak/harvest_lists2', exist_ok=True)
for cat, es in sorted(by.items()):
    p = R + f'work/_harvest/{cat}.json'
    if os.path.exists(p) and not os.path.exists(R + f'bak/harvest_lists2/{cat}.json'): shutil.copy(p, R + f'bak/harvest_lists2/{cat}.json')
    cur = json.load(open(p)) if os.path.exists(p) else {'b': []}
    have = {b['n'].strip().lower() for b in cur['b']}
    add = [e for e in es if e['n'].lower() not in have]
    cur['b'] += add
    with open(p + '.tmp', 'w') as fh: json.dump(cur, fh, ensure_ascii=False, indent=0)
    os.replace(p + '.tmp', p)
    print(cat, 'appended', len(add), 'of', len(es), 'total now', len(cur['b']))
