"""Owner decision 2026-11-01: C8 departments Timber & sheet materials, Masonry, roofing & insulation and
Heritage & reclaimed materials move to G2 Property & Structures ("intrinsic qualities of the home rather
than tools"). Moves the departments, the brands that make those kinds, and the heritage-tile regions.
Backups in work/MOVE_C8_G2/. Usage: python3 tools/move_c8_to_g2.py ; then merge.py C8 G2, registers, build."""
import json, os, re, shutil
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEPTS = ['Timber & sheet materials', 'Masonry, roofing & insulation', 'Heritage & reclaimed materials']
REGIONS = ['Mexico (Puebla)', 'Mallorca (Spain)', 'Morocco (Marrakech, Tangier)', 'Nabeul (Tunisia)']
KF = re.compile(r'^(timber|timber cladding|bricks?|fletton bricks|reclaimed brick|cement|cement tile.*|insulation.*|cladding/cement/masonry|roof.*|slate|architectural salvage|linseed oil paint|lime.*|hydraulic lime|natural hydraulic lime.*|plaster|paint / limewash|flues & chimneys|encaustic.*|delft.*|delftware|tin-glazed pottery|talavera.*|maiolica|azulejo|zellige.*|iznik tile|nabeul tile)$', re.I)
KEEP = {'Simpson Strong-Tie', 'Rotho Blaas', 'Ultrapanel', 'Infinity Drain', 'Farrow & Ball', 'Little Greene'}
EXTRA = {'Mintons', 'Nakamoto Forestry'}  # heritage tiles; timber cladding
os.makedirs(f'{R}/work/MOVE_C8_G2', exist_ok=True)
P = {k: f'{R}/out/{k}.json' for k in ('C8', 'G2', 'C8_brands', 'G2_brands')}
for p in P.values(): shutil.copy(p, f'{R}/work/MOVE_C8_G2/{os.path.basename(p)}.before')
c8, g2 = json.load(open(P['C8'])), json.load(open(P['G2']))
mv = [d for d in c8['depts'] if d['n'] in DEPTS]; assert len(mv) == 3, [d['n'] for d in mv]
c8['depts'] = [d for d in c8['depts'] if d['n'] not in DEPTS]
burial = next((i for i, d in enumerate(g2['depts']) if d['n'] == 'Burial places'), len(g2['depts']))
g2['depts'][burial:burial] = mv  # building materials sit with the homes, before burial places
rmv = [r for r in c8.get('rg', []) if r['n'] in REGIONS]
c8['rg'] = [r for r in c8.get('rg', []) if r['n'] not in REGIONS]; g2['rg'] = g2.get('rg', []) + rmv
inreg = {n for r in rmv for n in r.get('b', [])}
c8['lead'] = c8['lead'].replace('(timber, walls and roofs, period materials, ground stone,', '(ground stone,') \
    + ' The materials a home is built from (timber and sheet, masonry, roofing and insulation, heritage and reclaimed materials) live in Property & Structures.'
c8['ax'] = c8['ax'].replace('structure, shell, period character, ground,', 'ground,')
g2['lead'] = g2['lead'] + ' Property also holds the materials the home itself is made of: timber and sheet materials, masonry, roofing and insulation, and heritage and reclaimed materials (owner, 2026-11-01).'
Bc, Bg = json.load(open(P['C8_brands'])), json.load(open(P['G2_brands']))
have = {b['n']: b for b in Bg['b']}; stay, moved = [], []
for b in Bc['b']:
    go = b['n'] not in KEEP and (b['n'] in EXTRA or b['n'] in inreg or KF.match((b.get('kf') or '').strip()))
    if not go: stay.append(b); continue
    moved.append(b['n'])
    if b['n'] in have:
        for k, v in b.items(): have[b['n']].setdefault(k, v)
    else: Bg['b'].append(b); have[b['n']] = b
Bc['b'] = stay
for k, o in (('C8', c8), ('G2', g2), ('C8_brands', Bc), ('G2_brands', Bg)):
    json.dump(o, open(P[k], 'w'), ensure_ascii=False, indent=1)
open(f'{R}/work/MOVE_C8_G2.log', 'w').write('depts: ' + ', '.join(DEPTS) + '\nregions: ' + ', '.join(r['n'] for r in rmv) + '\nbrands (' + str(len(moved)) + '): ' + ', '.join(moved) + '\n')
print('moved', len(mv), 'depts,', len(rmv), 'regions,', len(moved), 'brands')
