import json, os, re, sys, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tt_data import TT
from struct_data import *

R = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(R + 'work/STR_E3/bak/E3.json'))
brands = {b['n'].lower() for b in json.load(open(R + 'out/E3_brands.json'))['b']}

# ---- tt fixes
for k in ['Dizi', 'Duduk', 'Native American flute', 'Celesta', 'Tubular bells', 'Cavaquinho', 'Kora', 'Udu', 'Sheng', 'Timecode vinyl']:
    TT.pop(k, None)
TT['Güiro and scraper'] = TT.pop('Guiro and scraper')
TT['Lap steel guitar'] = [g for g in TT['Lap steel guitar'] if g[0] != 'Double-neck pairing']
TT['Hurdy-gurdy'] = [g for g in TT['Hurdy-gurdy'] if g[0] != 'Regional name']
REP = [('B flat', 'B♭'), ('E flat', 'E♭'), ('A flat', 'A♭'), ('D flat', 'D♭'), ('F sharp', 'F♯'), ('C sharp', 'C♯'),
       ('Bodhran', 'Bodhrán'), ('Ipe or', 'Ipê or'), ('Peguri', 'Péguri'), ('Schwyzeroergeli', 'Schwyzerörgeli'),
       ('Charangon', 'Charangón'), ('Sami drum', 'Sámi drum'), ('Ganza', 'Ganzá'), ('Agogo', 'Agogô'),
       ('Guiro', 'Güiro'), ('Tekerolant', 'Tekerőlánt'), ('+/-', '±'), ('Cabasa', 'Cabasa'), ('Kokyu', 'Kokyu')]
def fix(s):
    for a, b in REP:
        s = s.replace(a, b)
    s = re.sub(r'(?<=\d)-(?=\d)', '–', s)
    return s
TT = {k: [[fix(g), [fix(t) for t in ts]] for g, ts in v] for k, v in TT.items()}

# ---- gather old kinds
kinds = {}
oldloc = {}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']:
            kinds[k['n']] = copy.deepcopy(k)
            oldloc[k['n']] = (dp['n'], s['n'])
before = dict(depts=len(old['depts']), shelves=sum(len(d['s']) for d in old['depts']), kinds=len(kinds),
              arch=sum(len(k.get('x', [])) for k in kinds.values()))

log = {'demoted': [], 'to_r': [], 'new_kinds': [], 'new_arch': [], 'missing': []}
for kn, names in DEMOTE.items():
    k = kinds[kn]
    for nm in names:
        hit = [x for x in k.get('x', []) if x['n'] == nm]
        if not hit:
            log['missing'].append(f'DEMOTE {kn}/{nm}'); continue
        k['x'] = [x for x in k['x'] if x['n'] != nm]
        log['demoted'].append(f'{kn}: {nm}')
for kn, items in TO_R.items():
    k = kinds[kn]
    for nm, rng, mk in items:
        hit = [x for x in k.get('x', []) if x['n'] == nm]
        if not hit:
            log['missing'].append(f'TO_R {kn}/{nm}'); continue
        k['x'] = [x for x in k['x'] if x['n'] != nm]
        k.setdefault('r', [])
        if [rng, mk] not in k['r']: k['r'].append([rng, mk])
        log['to_r'].append(f'{kn}: {nm} -> {rng}/{mk}')
for kn, xs in NEW_X.items():
    for x in xs:
        if x['mk'].lower() not in brands: log['missing'].append(f'brand {x["mk"]}')
        kinds[kn].setdefault('x', []).append(x)
        log['new_arch'].append(f'{kn}: {x["n"]}')
for nm, spec in NEW.items():
    k = {'n': nm, 'a': spec.get('a', ''), 'd': spec['d'], 's': spec['s']}
    if spec.get('x'):
        k['x'] = spec['x']
        for x in spec['x']:
            if x['mk'].lower() not in brands: log['missing'].append(f'brand {x["mk"]}')
    if spec.get('see'): k['see'] = spec['see']
    kinds[nm] = k
    log['new_kinds'].append(nm)

# ---- definition fixes
kinds['Cymbal']['d'] = 'Thin round plate of copper alloy struck with sticks or against another cymbal, sold in series named for alloy and finish.'
kinds['Saxophone']['d'] = 'Single-reed woodwind with a conical brass body, made in soprano, alto, tenor and baritone voices.'
kinds['Singing bowl']['d'] = 'Standing bowl bell sounded by striking or rubbing the rim; one made for worship is an altar bell.'
kinds['Tuning machines']['d'] = 'Geared pegs on the headstock that set string tension; swapped for stability, gear ratio or vintage looks.'

# ---- tt, see
nott = []
for nm, k in kinds.items():
    if nm in TT:
        k['tt'] = TT[nm]; k.pop('t', None)
    else:
        if k.get('t'): nott.append(nm)
        k.pop('t', None)
for nm, sv in SEE.items():
    k = kinds[nm]
    cur = k.get('see', [])
    for s in sv:
        if s not in cur: cur.append(s)
    k['see'] = cur
# kinds with tt entries but no kind
for nm in TT:
    if nm not in kinds: log['missing'].append(f'TT for unknown kind {nm}')

# ---- assemble
bmap = {d['n']: d for d in old['depts']}
bmap['Keyboards & electronic instruments'] = bmap['Pianos & keyboards']
placed = set()
depts = []
for dn, mode, t, ax, shelves in DEPTS:
    od = bmap[dn]
    dp = {'n': dn, 'mode': mode or od['mode']}
    if od.get('note'): dp['note'] = od['note']
    dp['t'] = t; dp['ax'] = ax
    if od.get('b'): dp['b'] = od['b']
    dp['s'] = []
    for sn, st, sax, kn in shelves:
        sh = {'n': sn, 't': st}
        if len(kn) > 3 or sax: sh['ax'] = sax
        sh['k'] = []
        for n in kn:
            if n not in kinds: log['missing'].append(f'kind {n} not defined'); continue
            sh['k'].append(kinds[n]); placed.add(n)
        dp['s'].append(sh)
    depts.append(dp)
for n in kinds:
    if n not in placed: log['missing'].append(f'UNPLACED {n}')

# check see targets
rd = {}
def tgt(code):
    if code not in rd:
        f = R + ('out/E3.json' if code == 'E3' else f'reader/{code}.json')
        rd[code] = json.load(open(f)) if code != 'E3' else None
    return rd[code]
allnames = set(kinds)
for nm, k in kinds.items():
    for code, tk, why in k.get('see', []):
        if code == 'E3':
            ok = tk in allnames
        else:
            d = tgt(code)
            ok = any(kk['n'] == tk for dp in d['depts'] for s in dp['s'] for kk in s['k'])
        if not ok: log['missing'].append(f'SEE target {code}/{tk} (from {nm})')

new = {'c': 'E3', 'rev': True, 'lead': old['lead'], 'ax': CAT_AX, 'key': CAT_KEY, 'b': old.get('b', []), 'depts': depts}
after = dict(depts=len(depts), shelves=sum(len(d['s']) for d in depts), kinds=len(kinds),
             arch=sum(len(k.get('x', [])) for k in kinds.values()))
out = R + 'out/E3.json'
tmp = out + '.tmp'
json.dump(new, open(tmp, 'w'), ensure_ascii=False, separators=(',', ':'))
os.replace(tmp, out)
json.dump({'before': before, 'after': after, 'log': log, 'no_tt_but_had_t': nott}, open(R + 'work/STR_E3/log.json', 'w'), ensure_ascii=False, indent=1)
print(before, after)
print('missing:', log['missing'])
print('no tt:', nott)
