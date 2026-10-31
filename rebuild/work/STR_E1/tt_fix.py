import json, os, sys
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/STR_E1')
import tt_data
R = '/home/user/Possession-Taxonomy/rebuild/'
d = json.load(open(R + 'out/E1.json'))
bak = json.load(open(R + 'work/STR_E1/bak/E1.json'))
K = {k['n']: k for dp in d['depts'] for s in dp['s'] for k in s['k']}
B = {k['n']: k for dp in bak['depts'] for s in dp['s'] for k in s['k']}
V = {'Scale or size', 'Edition and condition', 'Form and use', 'Named forms', 'Other', 'Misc'}
TT = dict(tt_data.TT)
TT['Spinner'] = [['Body', ['Three-lobe', 'Two-lobe']], ['Material', ['Metal', 'Plastic']], ['Wear', ['Held', 'Spinner ring']]]
TT['Slider & haptic fidget'] = [['Shape', ['Magnetic slider', 'Haptic slider', 'Haptic coin']], ['Material', ['Stainless steel', 'Titanium', 'Ultem (PEI)']]]
TT['Paper doll'] = [['Sale format', ['Book of cut-outs', 'Boxed set', 'Magnetic set']]]
TT['Clicker & switch fidget'] = [['Product', ['Fidget cube', 'Button keychain', 'Click pad']], ['Control', ['Buttons', 'Switches', 'Dials', 'Joystick']]]
TT['Popper'] = [['Product', ['Bubble board', 'Popper keychain', 'Spinner-popper', 'Push popper']], ['Outline', ['Round', 'Square', 'Animal or character']]]
TT['Squishy'] = [['Filling', ['Slow-rise foam', 'Silicone mochi', 'Gel']]]
TT['Stretch fidget'] = [['Product', ['Water snake', 'Stretchy string', 'Fidget band', 'Bouncy band']]]
TT['Fold fidget'] = [['Shape', ['Cube']]]
TT['Begleri'] = [['Link between beads', ['Cord', 'Rigid bar', 'Chain']]]
for n, tt in TT.items():
    K[n]['tt'] = tt
# restore sourced archetypes that are named things
RESTORE = {'Interlocking puzzle': ['Six-piece burr', 'High-level burr', 'Diagonal burr'],
           'Impossible object': ['Ship in a bottle', 'Fruit in a bottle'],
           'Toy kite': ['Delta kite', 'Diamond kite', 'Box kite', 'Sled kite', 'Parafoil kite', 'Malay kite', 'Rokkaku kite', 'Fighter kite'],
           'Draughts set': ['International draughts set', 'English draughts set', 'Russian draughts set', 'Brazilian draughts set', 'Canadian checkers set'],
           'Domino set': ['Chinese domino set'],
           'Marble': ['German handmade glass marble', 'Clay and china marble']}
restored = []
for kn, names in RESTORE.items():
    src = {x['n']: x for x in B[kn]['x']}
    K[kn].setdefault('x', [])
    have = {x['n'] for x in K[kn]['x']}
    for n in names:
        if n not in have:
            K[kn]['x'].append(src[n]); restored.append((kn, n))
# brand ranges posing as archetypes -> r
RANGES = {'Scale model kit': None, 'Die-cast model': ['Bburago 1:18', 'Maisto', 'AUTOart', 'Minichamps'],
          'Radio-controlled vehicle': ['Axial AX10 and SCX10 crawlers', 'Kyosho Mini-Z'],
          'Slot-car racing set': ['Carrera', 'Ninco'],
          'Building brick set': ['Mega (Mega Bloks / Mega Construx)', 'COBI', 'BlueBrixx'],
          'Card sleeve': None, 'Playmat & card binder': None}
to_r = []
for kn, names in RANGES.items():
    k = K[kn]
    sel = [x for x in k.get('x', []) if names is None or x['n'] in names]
    assert names is None or len(sel) == len(names), (kn, names)
    for x in sel:
        k.setdefault('r', [])
        e = [x['n'], x.get('mk', '') or '']
        if e not in k['r']: k['r'].append(e)
        to_r.append((kn, x['n']))
    k['x'] = [x for x in k.get('x', []) if x not in sel]
    if not k['x']: k.pop('x')
# final check on vague labels
bad = [(k['n'], g[0]) for k in K.values() for g in k.get('tt', []) if g[0] in V]
assert not bad, bad
tmp = R + 'out/E1.json.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, R + 'out/E1.json')
print('restored', len(restored), 'to_r', len(to_r))
json.dump({'restored': restored, 'to_r': to_r}, open(R + 'work/STR_E1/log_ttfix.json', 'w'), indent=1)
