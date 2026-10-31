# usage: python3 build.py CODE JOB  (reads work/CODE/agent/JOB.spec.json, writes work/CODE/shelves/JOB.json via temp file)
import json, os, re, sys
R = '/home/user/Possession-Taxonomy/rebuild'
c, j = sys.argv[1], sys.argv[2]
txt = open(f'{R}/work/{c}/prompts/{j}.txt').read()
blk = txt[txt.index('Old data for this shelf'):]
blk = blk[blk.index('```json') + 7:]; blk = blk[:blk.index('```')]
old = json.loads(blk)
pool = {}
for k in old:
    for key in ('m', 'r'):
        for mm, mk in k.get(key) or []:
            pool.setdefault((key, mm), []).append(mk)
oldk = {k['n']: k for k in old}
spec = json.load(open(f'{R}/work/{c}/agent/{j}.spec.json'))
def pick(key, items):
    out = []
    for it in items:
        if isinstance(it, list): mm, mk = it
        else:
            mm = it; cands = pool.get((key, mm)) or pool.get(('m' if key == 'r' else 'r', mm))
            if not cands: sys.exit(f'NOT IN OLD DATA: {key} {mm!r}')
            nz = [x for x in cands if x]; mk = nz[0] if nz else ''
        if mm not in {a for (_, a) in pool}: sys.exit(f'NOT IN OLD DATA: {mm!r}')
        out.append([mm, mk])
    return out
kinds = []
for k in spec['kinds']:
    o = oldk.get(k.get('from', k['n'])) 
    nk = {'n': k['n'], 'a': k.get('a', o.get('a', '') if o else ''), 'd': k['d']}
    if k.get('t'): nk['t'] = k['t']
    if k.get('tg'): nk['tg'] = k['tg']
    nk['s'] = k.get('s', o.get('s', '') if o else '')
    if k.get('m'): nk['m'] = pick('m', k['m'])
    if k.get('r'): nk['r'] = pick('r', k['r'])
    kinds.append(nk)
out = {'kinds': kinds, 'brands': [], 'traditions': [], 'notes': spec.get('notes', '')}
p = f'{R}/work/{c}/shelves/{j}.json'; tmp = f'{R}/work/{c}/agent/{j}.tmp.json'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1); os.replace(tmp, p)
print('wrote', p, len(kinds), 'kinds', sum(len(k.get('m', [])) for k in kinds), 'models')
