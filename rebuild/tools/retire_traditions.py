"""Retire the Traditions registers (owner, 2026-11-01): "In general I want to retire the traditions, either deferring
them or integrating them within the items proper." Food and drink traditions are in the Culinary taxonomy; garden
and flower design goes to Visual Entertainment; practices (rituals, routines, healing systems, falconry) go to the
Pleasure taxonomy, which files the practice. A tradition that names a product kept and owned becomes a named entry
nested in the kind it belongs to (e.g. Binchōtan under Barbecue fuel, "and it should show up in parenthesis").
Writes work/TRADITIONS_RETIRED/{all,to_culinary,to_ve,to_pleasure,integrated}.json and removes out/*_traditions.json.
Usage: python3 tools/retire_traditions.py ; then merge.py <cats>, registers, build."""
import json, os, glob, shutil
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = f'{R}/work/TRADITIONS_RETIRED'; os.makedirs(W, exist_ok=True)
# tradition -> [(category, kind, named entry)]; the tradition's description and source go with the entry
INTEGRATE = {
    'Arab falconry': [('B10', 'Falconry hood', 'Arab hood'), ('B10', 'Falconry glove', 'Mangalah')],
    'Kōdō': [('B4', 'Loose incense', 'Kyara and jinkō pieces')],
    'Bakhoor and oud': [('B4', 'Loose incense', 'Bakhoor'), ('B4', 'Loose incense', 'Oud chips')],
    'Tibetan incense': [('B4', 'Stick incense', 'Tibetan incense')],
    'Indian agarbatti': [('B4', 'Stick incense', 'Masala agarbatti'), ('B4', 'Stick incense', 'Nag champa'), ('B4', 'Stick incense', 'Dhoop')],
    'Liuyang fireworks': [('B4', 'Firecracker & banger', 'Liuyang firecrackers')],
    'Kishū binchōtan charcoal making': [('C2', 'Barbecue fuel', 'Binchōtan (Kishū white charcoal)')],
    'Finnish sauna': [('G3', 'Sauna cabin', 'Finnish sauna')],
    'Võro smoke sauna': [('G3', 'Sauna cabin', 'Smoke sauna (Võro)')],
    'Russian banya': [('G3', 'Sauna cabin', 'Russian banya')],
    'Turkish hammam': [('G3', 'Steam room', 'Turkish hammam')],
    'Japanese furo': [('G3', 'Wood-fired hot tub', 'Japanese furo')],
    'Mehndi': [('H1', 'Henna', 'Mehndi cone')],
    'Henna: rituals, aesthetic and social practices': [('H1', 'Henna', 'Arab and Maghrebi henna')],
    'Kohl': [('H1', 'Kohl & surma', 'Tiro')],
    'Kajal and surma': [('H1', 'Kohl & surma', 'Kajal')],
    'Sindoor and kumkum': [('H1', 'Kumkum & sindoor', 'Tilaka')],
    'Bindi': [('H1', 'Bindi', 'Painted bindi'), ('H1', 'Bindi', 'Sticker bindi')],
    'Moroccan argan oil': [('H1', 'Hair oil & serum', 'Moroccan argan oil')],
    'Miswak and teeth-cleaning twigs': [('H1', 'Manual toothbrush', 'Miswak'), ('H1', 'Manual toothbrush', 'Datun (neem twig)'), ('H1', 'Manual toothbrush', 'African chew stick')],
    'Aleppo ghar soap': [('H1', 'Bar soap', 'Aleppo soap')],
    'Nabulsi soap making': [('H1', 'Bar soap', 'Nabulsi soap')],
    'Savon de Marseille': [('H1', 'Bar soap', 'Savon de Marseille')],
    'African black soap': [('H1', 'Bar soap', 'African black soap')],
    'Traditional Chinese medicine': [('H2', 'Traditional medicine preparation', 'Chinese patent medicine')],
    'Ayurveda': [('H2', 'Traditional medicine preparation', 'Ayurvedic preparation')],
    'Kampo': [('H2', 'Traditional medicine preparation', 'Kampo extract')],
    'Unani': [('H2', 'Traditional medicine preparation', 'Unani preparation')],
    'Kannauj deg-bhapka attar distillation': [('H4', 'Attar (deg-bhapka distillate)', f) for f in ('Rooh gulab (rose attar)', 'Mitti attar', 'Shamama', 'Ruh khus (vetiver attar)', 'Kewra attar')],
    'Arabian oud and oil perfumery': [('H4', 'Musk oil', 'Musk tahara (white musk)')],
}
VE_GROUPS = {'Plants & gardens', 'Flowers & plants'}
allt, cul, ve, ple, integ = [], [], [], [], []
for p in sorted(glob.glob(f'{R}/out/*_traditions.json')):
    c = os.path.basename(p)[:-16]
    for t in json.load(open(p)).get('t', []):
        t = dict(t, cat=c); allt.append(t)
        if t.get('g') == 'Food & drink': cul.append(t)
        elif t.get('g') in VE_GROUPS: ve.append(t)
        elif t['n'] in INTEGRATE: integ.append(t)
        else: ple.append(t)  # practices: routines, rituals, healing systems, falconry, breeding, regional perfumery
missing = set(INTEGRATE) - {t['n'] for t in integ}; assert not missing, missing
trees, log = {}, []
for t in integ:
    for c, kn, en in INTEGRATE[t['n']]:
        tr = trees.setdefault(c, json.load(open(f'{R}/out/{c}.json')))
        k = next((k for d in tr['depts'] for s in d['s'] for k in s['k'] if k['n'] == kn), None)
        assert k is not None, (c, kn)
        xs = k.setdefault('x', [])
        if any(x['n'].lower() == en.lower() for x in xs): log.append(f'have {c} {kn} > {en}'); continue
        e = {'n': en, 'd': t.get('d', ''), 's': t.get('s', '')}
        if any(x.get('g') for x in xs): e['g'] = 'Traditional & regional'
        if t.get('r'): e['a'] = t['r']
        xs.append(e); log.append(f'add {c} {kn} > {en}  (from tradition {t["n"]})')
for c, tr in trees.items(): json.dump(tr, open(f'{R}/out/{c}.json', 'w'), ensure_ascii=False, indent=1)
for n, o in (('all', allt), ('to_culinary', cul), ('to_ve', ve), ('to_pleasure', ple), ('integrated', integ)):
    json.dump(o, open(f'{W}/{n}.json', 'w'), ensure_ascii=False, indent=1)
for p in glob.glob(f'{R}/out/*_traditions.json'):
    shutil.move(p, f'{W}/{os.path.basename(p)}')
open(f'{W}/LOG.txt', 'w').write('\n'.join(log) + '\n')
print(len(allt), 'traditions:', len(cul), 'to Culinary,', len(ve), 'to VE,', len(ple), 'to Pleasure,', len(integ), 'integrated as',
      sum(1 for l in log if l.startswith('add')), 'named entries in', ' '.join(sorted(trees)))
