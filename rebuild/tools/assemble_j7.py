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
KEY = [('Is it alcohol-free or low alcohol and made only that way, with no full-strength parent', 'No & low alcohol'),
       ('Is it a grape variety you are looking up rather than a bottle', 'Grape varieties'),
       ('Is it a wine with a protected place name from France', 'Wine of France'), ('… from Italy', 'Wine of Italy'), ('… from Spain or Portugal', 'Wine of Spain & Portugal'),
       ('… from Germany, Austria or Switzerland', 'Wine of Germany, Austria & Switzerland'), ('… from Hungary or Central Europe', 'Wine of Hungary & Central Europe'),
       ('… from the Balkans', 'Wine of the Balkans'), ('… from Eastern Europe', 'Wine of Eastern Europe'), ('… from Greece or Cyprus', 'Wine of Greece & Cyprus'),
       ('… from Turkey, the Caucasus or the Levant', 'Wine of Turkey, the Caucasus & the Levant'), ('… from the United States', 'Wine of the United States'),
       ('… from Canada or Mexico', 'Wine of Canada & Mexico'), ('… from South America', 'Wine of South America'), ('… from South Africa', 'Wine of South Africa'),
       ('… from Australia or New Zealand', 'Wine of Australia & New Zealand'), ('… from England or Wales', 'Wine of England & Wales'), ('… from China, Japan or India', 'Wine of China, Japan & India'),
       ('Is it a wine sold by style rather than place (sparkling method, rosé, orange, sweet, fortified or aromatised)', 'Wine styles across countries'),
       ('Is it beer', 'Beer'), ('Is it whisky', 'Whisky'), ('Is it brandy', 'Brandy'), ('Is it rum or another cane spirit', 'Rum & cane spirits'), ('Is it an agave spirit', 'Agave'),
       ('Is it gin, vodka or aquavit', 'Gin, vodka & aquavit'), ('Is it an anise spirit or absinthe', 'Anise & absinthe'), ('Is it an Asian spirit (baijiu, shōchū, soju…)', 'Asian spirits'),
       ('Is it a liqueur', 'Liqueurs'), ('Is it sake or another rice wine', 'Sake & rice wine'), ('Is it cider, perry or mead', 'Cider, perry & mead'), ('Otherwise: a ready-to-drink or mixed pack', 'Ready-to-drink & mixed packs')]
dn = {d['n'] for d in new['depts']}
new['key'] = [f"{i+1}. {q}? → {d}" for i, (q, d) in enumerate([x for x in KEY if x[1] in dn])] + ['<i>Precedence: a protected wine name (Champagne, Port, Tokaji) is placed by its country before its style; alcohol-free versions of full-strength drinks stay with their parent and appear in the No & low view.</i>']
# coordinator: old multi-country style kinds go to one cross-country department, carried as they were
STYLE = [('Sparkling wine', 'Sparkling wines made the same way in many countries; a protected sparkling wine (Champagne, Cava, Franciacorta) is under its country.',
          ['Traditional-method sparkling wine', 'Sekt', 'Cap Classique', 'Sparkling Shiraz']),
         ('Rosé & orange wine', 'Wines defined by how long the juice stays on the skins, from pale rosé to skin-contact orange wine.', ['Rosé', 'Orange wine']),
         ('Sweet wine', 'Wines made sweet by late picking or frozen grapes; protected sweet wines (Sauternes, Tokaji) are under their country.', ['Late-harvest wine', 'Ice wine']),
         ('Fortified & aromatised wine', 'Wines strengthened with spirit or flavoured with botanicals; Port, Sherry and Madeira are under Spain & Portugal.',
          ['Regional fortified wine', 'Vermouth', 'Quinquina & americano', 'Sangria & mulled wine'])]
oldk = {k['n']: k for d in old['depts'] for s in d['s'] for k in s['k']}
style = {'n': 'Wine styles across countries', 'mode': 'mixed', 'ax': 'How the wine is made: sparkling, skin contact, sweet, or fortified and aromatised.',
         't': 'Wine styles made in many countries and sold by style rather than place; a wine with its own protected name is under its country.',
         's': [{'n': n, 't': t, 'k': [oldk[k] for k in ks if k in oldk]} for n, t, ks in STYLE]}
for sh in style['s']:
    if len(sh['k']) > 3: sh['ax'] = 'by style'
if not missing: new['depts'].insert(sum(1 for d in new['depts'] if d['n'].startswith('Wine of')), style)
ren = {}; brands = []; moves = []
for p in parts.values():
    ren.update(p.get('renames') or {}); brands += p.get('brands') or []; moves += p.get('moves') or []
# coordinator: grape kinds of the old edition fold into the grape register's kind that holds the variety
gk = {}
for d in new['depts']:
    if d['n'] == 'Grape varieties':
        for sh in d['s']:
            for k in sh['k']:
                for x in k.get('x') or []:
                    for nm in [x['n']] + [a.strip() for a in (x.get('a') or '').replace(' · ', ',').split(',') if a.strip()]: gk.setdefault(nm.lower(), k['n'])
GR = {'Pinot Grigio': 'pinot gris', 'Petite Sirah': 'durif', 'Red blend': None}
for d in old['depts']:
    if d['n'] in ('Red wine', 'White wine'):
        for sh in d['s']:
            for k in sh['k']:
                if k['n'] in ren: continue
                key = GR.get(k['n'], k['n'].lower())
                if key and key in gk: ren[k['n']] = gk[key]
# coordinator: producer icons that sat in grape kinds become versions of their appellation, keeping their earlier sources
ICONS = {'Screaming Eagle': 'Napa Valley', 'Penfolds Grange': 'Barossa Valley', 'Tignanello': 'Toscana', 'Egon Müller Scharzhofberger': 'Mosel'}
src = {x['n']: x for d in old['depts'] for sh in d['s'] for k in sh['k'] for x in k.get('x') or []}
for icon, app in ICONS.items():
    hit = next((x for d in new['depts'] for sh in d['s'] for k in sh['k'] for x in k.get('x') or [] if x['n'].lower().startswith(app.lower())), None)
    if hit and icon in src and not any(v.get('n') == icon for v in hit.get('v') or []):
        o = src[icon]; hit.setdefault('v', []).append({'n': icon, 'y': o.get('y', ''), 'd': (o.get('d') or 'Producer icon.') + ' (source: ' + (o.get('s') or '') + ')'}); print('icon', icon, '->', hit['n'])
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
