"""Assemble E2 from the two audit-batch-2 parts (E2A, E2B) and fold their brand files into E2_brands.json.
Brand countries the E2B agent took from general knowledge (flagged "to verify") are blanked: unsourced facts stay out.
Usage: python3 tools/e2_assemble.py   (rewrites out/E2.json and out/E2_brands.json; backups in bak/)"""
import json, os, shutil, time
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ts = time.strftime('%Y%m%d%H%M%S'); os.makedirs('bak', exist_ok=True)
for f in ('out/E2.json', 'out/E2_brands.json'): shutil.copy(f, f'bak/{os.path.basename(f)}.{ts}')
d = json.load(open('out/E2.json'))
parts = {dp['n']: dp for p in ('E2A', 'E2B') for dp in json.load(open(f'out/{p}_part.json'))['depts']}
assert set(parts) <= {dp['n'] for dp in d['depts']}, set(parts) - {dp['n'] for dp in d['depts']}
d['depts'] = [parts.get(dp['n'], dp) for dp in d['depts']]
UNSOURCED_COUNTRY = {'airtec', 'uwatec', 'poseidon', 'raichle', 'rottefella', 'lange', 'zebco'}
b = json.load(open('out/E2_brands.json')); have = {x['n'].lower() for x in b['b']}
for p in ('E2A', 'E2B'):
    for x in json.load(open(f'out/{p}_brands.json'))['b']:
        if p == 'E2B' and x['n'].lower() in UNSOURCED_COUNTRY: x['c'] = ''
        if x['n'].lower() not in have: b['b'].append(x); have.add(x['n'].lower())
for f, o in (('out/E2.json', d), ('out/E2_brands.json', b)):
    json.dump(o, open(f + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(f + '.tmp', f)
print('depts', len(d['depts']), 'brands', len(b['b']))
