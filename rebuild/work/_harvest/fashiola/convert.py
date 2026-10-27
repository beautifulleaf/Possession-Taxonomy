import json, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
S = 'https://www.fashiola.com/brands/'
rows = [l.rstrip('\n').split('\t') for l in open('work/_harvest/fashiola/decisions.tsv')][1:]
by = collections.defaultdict(list)
for name, a, n, cat, seg, kf, c, f in rows:
    if a != 'add': continue
    e = {'n': n, 'seg': seg, 'kf': kf, 's': S}
    if c: e['c'] = c
    if f: e['f'] = f
    by[cat].append(e)
for cat, es in sorted(by.items()):
    p = f'work/_harvest/{cat}.json'
    cur = json.load(open(p)) if os.path.exists(p) else {'b': []}
    have = {b['n'].strip().lower() for b in cur['b']}
    add = [e for e in es if e['n'].lower() not in have]
    cur['b'] += add
    with open(p + '.tmp', 'w') as fh: json.dump(cur, fh, ensure_ascii=False, indent=0)
    os.replace(p + '.tmp', p)
    print(cat, 'appended', len(add), 'of', len(es), 'total now', len(cur['b']))
