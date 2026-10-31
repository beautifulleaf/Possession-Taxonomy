"""Assemble a category split into parts: rebuild/out/<CODE>_parts/<PART>.json, each
{"replaces":[old dept names], "depts":[...], "brands":[...], "renames":{...}, "moves":[...], "key":[optional]}.
New departments take the place of the first department they replace (order kept); old departments no part replaces stay.
Usage: python3 tools/assemble_parts.py CODE [--write]"""
import json, os, sys, shutil, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
code = sys.argv[1]; write = '--write' in sys.argv
old = json.load(open(f'out/{code}.json'))
parts = {os.path.basename(f)[:-5]: json.load(open(f)) for f in sorted(glob.glob(f'out/{code}_parts/*.json'))}
at = {}  # old dept name -> part
for p, d in parts.items():
    for n in d.get('replaces') or [x['n'] for x in d['depts']]:
        if n in at: sys.exit(f'{n} replaced by both {at[n]} and {p}')
        at[n] = p
depts, done = [], set()
for d in old['depts']:
    p = at.get(d['n'])
    if not p: depts.append(d)
    elif p not in done: depts += parts[p]['depts']; done.add(p)
for p in parts:
    if p not in done: depts += parts[p]['depts']
names = [d['n'] for d in depts]
dup = {n for n in names if names.count(n) > 1}
if dup: sys.exit(f'duplicate departments {dup}')
oldk = {k['n'] for d in old['depts'] for s in d['s'] for k in s['k']}
newk = {k['n'] for d in depts for s in d['s'] for k in s['k']}
ren = {}; brands = []; moves = []
for p in parts.values():
    ren.update(p.get('renames') or {}); brands += p.get('brands') or []; moves += p.get('moves') or []
moved = {m['kind']['n'] for m in moves if isinstance(m.get('kind'), dict)}
lost = sorted(oldk - newk - set(ren) - moved)
print(code, 'parts', list(parts), 'depts', len(old['depts']), '->', len(depts), 'kinds', len(oldk), '->', len(newk), 'lost', len(lost), lost[:30])
key = [k for p in parts.values() for k in (p.get('key') or [])]
for p in parts.values():
    for dn, facts in (p.get('dept_ms') or {}).items():
        for d in depts:
            if d['n'] == dn: d['ms'] = (d.get('ms') or []) + facts
new = dict(old, depts=depts)
if write:
    os.makedirs(f'work/ASM_{code}', exist_ok=True)
    for f in (f'{code}.json', f'{code}_brands.json', f'{code}_renames.json', f'{code}_moves.json'):
        if os.path.exists('out/' + f): shutil.copy('out/' + f, f'work/ASM_{code}/{f}')
    if key: new['key'] = key
    json.dump(new, open(f'out/{code}.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    b = json.load(open(f'out/{code}_brands.json')) if os.path.exists(f'out/{code}_brands.json') else {'b': []}
    have = {x['n'].lower() for x in b['b']}; b['b'] += [x for x in brands if x.get('n') and x['n'].lower() not in have]
    upd = {}
    for p in parts.values(): upd.update({k.lower(): v for k, v in (p.get('brand_updates') or {}).items()})
    for x in b['b']:
        if x['n'].lower() in upd: x.update(upd[x['n'].lower()])
    print('brand updates', sum(1 for x in b['b'] if x['n'].lower() in upd), 'of', len(upd))
    json.dump(b, open(f'out/{code}_brands.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    r = json.load(open(f'out/{code}_renames.json')) if os.path.exists(f'out/{code}_renames.json') else {}
    r.update(ren); json.dump(r, open(f'out/{code}_renames.json', 'w'), ensure_ascii=False, indent=1)
    m = json.load(open(f'out/{code}_moves.json')) if os.path.exists(f'out/{code}_moves.json') else {'out': []}
    m['out'] += moves; json.dump(m, open(f'out/{code}_moves.json', 'w'), ensure_ascii=False, indent=1)
    print('written')
