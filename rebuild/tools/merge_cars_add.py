"""Fold rebuild/out/G1_parts/cars_add/<REGION>.json into G1_parts/CARS.json: entries by kind (deduplicated by marque + name,
versions merged), the 'Car, body style not stated' kind created on a shelf of its own, brands and brand_updates carried into the
part so tools/assemble_parts.py applies them. Usage: python3 tools/merge_cars_add.py [--write]"""
import json, os, sys, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
P = 'out/G1_parts/CARS.json'; part = json.load(open(P)); dept = part['depts'][0]
kinds = {k['n']: k for s in dept['s'] for k in s['k']}
NS = 'Car, body style not stated'
if NS not in kinds:
    k = {'n': NS, 'd': 'Production cars whose body style no fetched page states; sectioned by marque.', 'nl': 'One entry is a car model sold under its own name; its generations are versions.',
         'sel': '', 'xg': 'by marque', 'x': []}
    dept['s'].append({'n': 'Body style not stated', 't': 'Car models listed on a marque reference without a stated body style.', 'k': [k]}); kinds[NS] = k
key = lambda x: ((x.get('mk') or x.get('g') or '').lower(), x['n'].lower())
have = {key(x): (kn, x) for kn, k in kinds.items() for x in k.get('x') or []}
added = {}; brands = part.setdefault('brands', []); bu = part.setdefault('brand_updates', {})
for f in sorted(glob.glob('out/G1_parts/cars_add/*.json')):
    a = json.load(open(f)); reg = os.path.basename(f)[:-5]
    for kn, xs in (a.get('kinds') or {}).items():
        tgt = kinds.get(kn) or kinds[NS]
        for x in xs:
            x.setdefault('g', x.get('mk'))
            if key(x) in have:
                old = have[key(x)][1]; vs = {v['n'] for v in old.get('v') or []}
                old.setdefault('v', []).extend(v for v in x.get('v') or [] if v['n'] not in vs)
                for fld in ('y', 'own', 'tier', 'cty', 'own_y', 's'):
                    if not old.get(fld) and x.get(fld): old[fld] = x[fld]
            else:
                tgt.setdefault('x', []).append(x); have[key(x)] = (tgt['n'], x); added[reg] = added.get(reg, 0) + 1
    yu = {k.lower(): v for k, v in (a.get('y_updates') or {}).items()}
    for kk in kinds.values():
        for x in kk.get('x') or []:
            y = yu.get(((x.get('mk') or x.get('g') or '') + '|' + x['n']).lower())
            if y and not x.get('y'): x['y'] = y
    names = {b['n'].lower() for b in brands}
    brands += [b for b in a.get('brands') or [] if b.get('n') and b['n'].lower() not in names]
    for m, u in (a.get('brand_updates') or {}).items(): bu.setdefault(m, {}).update(u)
    # sourced marque facts override general-knowledge fields on entries
    for x in (y for k in kinds.values() for y in k.get('x') or []):
        u = (a.get('brand_updates') or {}).get(x.get('mk') or '')
        if u:
            if u.get('own'): x['own'] = u['own']
            if u.get('c'): x['cty'] = u['c']
            if u.get('own_y'): x['own_y'] = u['own_y']
for k in kinds.values():
    xs = k.get('x') or []; k['x'] = sorted(xs, key=lambda x: ((x.get('g') or '').lower(), str(x.get('y') or '9999'), x['n']))
total = sum(len(k.get('x') or []) for k in kinds.values())
kinds[NS]['sel'] = f"Covers {len(kinds[NS]['x'])} models listed on marque references that state no body style."
print('added', added, 'total entries', total)
if '--write' in sys.argv:
    os.makedirs('work/ASM_G1', exist_ok=True); import shutil; shutil.copy(P, 'work/ASM_G1/CARS.before_add.json')
    json.dump(part, open(P + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(P + '.tmp', P); print('written')
