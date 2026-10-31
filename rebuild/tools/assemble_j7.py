"""Assemble the V4 J7 pilot from rebuild/out/J7_parts/<PART>.json into out/J7.json (+ brands, renames, moves).
Order of departments follows ORDER; old departments not replaced by any part are kept as they were.
Usage: python3 tools/assemble_j7.py [--write]"""
import json, os, sys, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
ORDER = ['WFR', 'WIT', 'WIB', 'WCE', 'WNW', 'GRAPES', 'BEER', 'SPIRITS', 'OTHER']
REPLACED = {'Red wine', 'White wine', 'Sparkling, rosé & orange wine', 'Sweet & fortified wine', 'Beer', 'Whisky', 'Spirits', 'Liqueurs',
            'Sake & rice wine', 'Cider, perry & mead', 'Ready-to-drink & mixed packs', 'No & low alcohol'}
old = json.load(open('out/J7.json'))
parts = {p: json.load(open(f'out/J7_parts/{p}.json')) for p in ORDER if os.path.exists(f'out/J7_parts/{p}.json')}
missing = [p for p in ORDER if p not in parts]
depts = [d for p in ORDER if p in parts for d in parts[p]['depts']]
kept = [d for d in old['depts'] if d['n'] not in REPLACED] if not missing else []
if missing:  # partial assembly: keep the old departments that the missing parts would replace
    kept = [d for d in old['depts'] if d['n'] in REPLACED]
    print('missing parts', missing, '- old departments kept for checking only')
new = dict(old, depts=depts + kept)
new['ax'] = 'What it is and where it comes from: wine by country and appellation, the grape varieties, beer by who makes it, spirits by protected category, then sake, cider, ready-to-drink and no & low alcohol.'
new['key'] = [f"{i+1}. {q}? → {d}" for i, (q, d) in enumerate([
    ('Is it alcohol-free or low alcohol and made only that way (no full-strength parent)', 'No & low alcohol'),
    ('Is it a wine from France', 'France'), ('from Italy', 'Italy'), ('from Spain or Portugal', 'Spain & Portugal')])]
new['key'] = [s for s in new['key'] if s.split('→ ')[1] in {d['n'] for d in new['depts']}]  # refined after assembly
ren = {}; brands = []; moves = []
for p in parts.values():
    ren.update(p.get('renames') or {}); brands += p.get('brands') or []; moves += p.get('moves') or []
names = {k['n'] for d in new['depts'] for s in d['s'] for k in s['k']}
bad = {o: n for o, n in ren.items() if n not in names}
print('departments', len(new['depts']), 'kinds', len(names), 'entries', sum(len(k.get('x') or []) for d in new['depts'] for s in d['s'] for k in s['k']),
      'renames', len(ren), 'renames to missing kinds', len(bad), 'brands', len(brands), 'moves', len(moves))
if '--write' in sys.argv and not missing:
    os.makedirs('work/V4_J7/bak', exist_ok=True)
    for f in ('J7.json', 'J7_brands.json', 'J7_renames.json', 'J7_moves.json'):
        if os.path.exists('out/' + f): shutil.copy('out/' + f, 'work/V4_J7/bak/' + f)
    json.dump(new, open('out/J7.json.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace('out/J7.json.tmp', 'out/J7.json')
    b = json.load(open('out/J7_brands.json')) if os.path.exists('out/J7_brands.json') else {'b': []}
    have = {x['n'].lower() for x in b['b']}; b['b'] += [x for x in brands if x.get('n') and x['n'].lower() not in have]
    json.dump(b, open('out/J7_brands.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    r = json.load(open('out/J7_renames.json')) if os.path.exists('out/J7_renames.json') else {}
    r.update(ren); json.dump(r, open('out/J7_renames.json', 'w'), ensure_ascii=False, indent=1)
    m = json.load(open('out/J7_moves.json')) if os.path.exists('out/J7_moves.json') else {'out': []}
    m['out'] += moves; json.dump(m, open('out/J7_moves.json', 'w'), ensure_ascii=False, indent=1)
    print('written')
