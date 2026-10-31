import json, copy, os, sys
R = '/home/user/Possession-Taxonomy/rebuild/'
d = json.load(open(R + 'work/STR_J10/bak/J10.json'))
brands = json.load(open(R + 'work/STR_J10/bak/J10_brands.json'))
WIKI = 'https://en.wikipedia.org/wiki/'
HAB = WIKI + 'Habanos_S.A.'

old = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            old[k['n']] = k

# ---- demotions: generic archetypes -> models in m
def demote(kind, names):
    k = old[kind]
    keep = []
    m = k.setdefault('m', [])
    for a in k.get('x', []):
        if a['n'] in names:
            if [a['n'], a.get('mk', '')] not in m:
                m.append([a['n'], a.get('mk', '')])
            for v in a.get('v', []):
                e = [v['n'], v.get('mk') or a.get('mk', '')]
                if e not in m:
                    m.append(e)
        else:
            keep.append(a)
    k['x'] = keep
    if not keep:
        k.pop('x')
DEM = {
 'Cheroot': ['Burmese cheroot', 'Indian cheroot'],
 'Humidor': ['Davidoff desktop humidor', 'Boveda humidor', 'Elie Bleu'],
 'Cigar cutter': ['Henckels dual-ended cutter'],
 'Meerschaum pipe': ['Turkish carved meerschaum'],
 'Corn cob pipe': ['Missouri Meerschaum cob pipe'],
 'Clay pipe': ['Clay churchwarden'],
 'Calabash pipe': ['Calabash'],
 'Kiseru': ['Rau kiseru', 'Nobe kiseru'],
 'Nasal snuff': ['German snuff'],
 'Snuff bottle': ['Imperial glass snuff bottle', 'Porcelain snuff bottle', 'Inside-painted snuff bottle'],
 'Hand pipe & chillum': ['Chillum', 'One-hitter and dugout'],
 'Pocket lighter': ['Dunhill butane', 'S.T. Dupont', 'Colibri'],
 'Bong': ['RooR', 'Illadelph'],
}
for k, n in DEM.items():
    demote(k, n)
# the heated-tobacco model list had a stray entry
hm = old['Heated-tobacco device']
hm['m'] = [e for e in hm['m'] if e[0] != 'with']
hm['m'] = [[e[0], e[1] or 'Japan Tobacco'] for e in hm['m']]

# ---- merge: hose + mouth tip
hose = old['Hookah hose']; tip = old['Hookah mouth tip']
hose['n'] = 'Hookah hose & mouth tip'
hose['a'] = 'hose · mouthpiece · mouth tip · drip tip'
hose['d'] = 'Flexible hose that carries smoke from a hookah to the mouth, with its handle and the small tip fitted over the mouthpiece.'
del old['Hookah mouth tip']
old['Hookah hose & mouth tip'] = hose; del old['Hookah hose']
old['Moist snuff']['n'] = 'Dipping tobacco'
old['Moist snuff']['a'] = 'moist snuff · dip · dipping snuff'
old['Dipping tobacco'] = old.pop('Moist snuff')
RENAMES = {'Hookah mouth tip': 'Hookah hose & mouth tip', 'Hookah hose': 'Hookah hose & mouth tip',
           'Moist snuff': 'Dipping tobacco'}

# ---- new kinds
def new(n, a, dd, s):
    old[n] = {'n': n, 'a': a, 'd': dd, 's': s}
LT = WIKI + 'List_of_tobacco_products'; ST = WIKI + 'Smokeless_tobacco'
new('Cigalike', 'e-cigarette · cig-a-like', 'First-generation vape shaped like a cigarette, disposable or with a rechargeable battery and replaceable cartridge.', WIKI + 'Construction_of_electronic_cigarettes')
new('Vape drip tip', 'mouthpiece · drip tip', 'Mouthpiece that fits a vape tank or atomiser; swapped for comfort, airflow and looks.', WIKI + 'Construction_of_electronic_cigarettes')
new('Permanent match', 'everlasting match · forever match', 'Naphtha-filled metal shell with a removable striker rod, lit by rubbing and used instead of a lighter.', WIKI + 'Lighter')
new('Creamy snuff', 'toothpaste snuff', 'Fluid tobacco paste marketed as a dental aid but used as an oral tobacco.', ST)
new('Gutkha', 'gutka', 'South Asian mix of tobacco, areca nut and flavourings, chewed from a sachet.', ST)
new('Naswar', 'nasvay', 'Afghan oral tobacco, close to dipping tobacco, placed under the tongue or lip.', ST)
new('Iqmik', 'Alaskan chew', 'Alaskan oral tobacco mixed with punk ash.', ST)
new('Rapé', 'hapé · shamanic snuff', 'Brazilian nasal snuff of ground tobacco blended with other plant ash and powders.', LT)
new('Khansar', 'Iranian hookah tobacco', 'Special tobacco used in Iran for the water pipe, sold apart from molasses shisha.', WIKI + 'Hookah')

# ---- new archetypes (variety departments only)
def arch(kind, n, dd, mk, y, s, v=None):
    old[kind].setdefault('x', []).append({'n': n, 'a': '', 'd': dd, 'mk': mk, 'y': y, 's': s, 'v': v or []})
for n, dd, mk in [
 ('Vegas Robaina', 'Cuban line launched by Habanos S.A. and named after Alejandro Robaina\'s farm.', 'Vegas Robaina'),
 ('Diplomáticos', 'Cuban Habanos marque of full-bodied cigars in classic vitolas.', 'Diplomáticos'),
 ('Fonseca', 'Cuban Habanos marque of mild cigars.', 'Fonseca'),
 ('El Rey del Mundo', 'Cuban Habanos marque of mild cigars in classic vitolas.', 'El Rey del Mundo'),
 ('Saint Luis Rey', 'Cuban Habanos marque of full-bodied cigars.', 'Saint Luis Rey'),
 ('Juan López', 'Cuban Habanos marque of medium-bodied cigars.', 'Juan López'),
 ('Vegueros', 'Cuban Habanos marque in the volume portfolio.', 'Vegueros'),
 ('La Gloria Cubana', 'Cuban Habanos marque that is also made in the United States.', 'La Gloria Cubana'),
 ('Sancho Panza', 'Cuban Habanos marque, with the Belicoso as its best-known vitola.', ''),
]:
    arch('Habano (Cuban premium cigar)', n, dd, mk, '', HAB)
old['Habano (Cuban premium cigar)']['m'] = [e for e in old['Habano (Cuban premium cigar)']['m'] if e[1] != 'Sancho Panza']
for n, mk in [('El Rey del Mundo',), ('Saint Luis Rey',), ('Juan López',), ('Vegueros',), ('La Gloria Cubana',)] and []:
    pass
have = {b['n'].lower() for b in brands['b']}
for n, kf in [('El Rey del Mundo', 'mild Habanos'), ('Saint Luis Rey', 'full-bodied Habanos'), ('Juan López', 'medium Habanos'), ('Vegueros', 'volume Habanos'), ('La Gloria Cubana', 'Habanos and US line')]:
    if n.lower() not in have:
        brands['b'].append({'n': n, 'c': 'Cuba', 'seg': 'Heritage manufactory', 'kf': kf, 'd': 'Cuban cigar marque in the Habanos S.A. portfolio.', 's': HAB})
# lighters: sourced classics from the Lighter article
arch('Pocket lighter', 'Ronson Pist-O-Liter', 'Early Ronson pocket lighter shaped like a pistol, one of the first practical flint lighters.', 'Ronson', '1910', WIKI + 'Lighter')
arch('Pocket lighter', 'Thorens Standard Original', 'Swiss-made early flint pocket lighter.', 'Thorens', '1919', WIKI + 'Lighter')
arch('Pocket lighter', 'Ronson Wonderlite', 'Ronson lighter of the permanent-match type.', 'Ronson', '1913', WIKI + 'Lighter')
old['Pocket lighter']['x'].sort(key=lambda a: 0)  # order fixed below
# table lighter: promote Gentry to archetype
tl = old['Table lighter']
tl['m'] = [e for e in tl['m'] if e[0] != 'Gentry']
tl.setdefault('x', []).append({'n': 'Flaminaire Gentry', 'a': 'Gentry', 'd': 'Butane table lighter developed by Marcel Quercia and Georges Ferdinand.', 'mk': '', 'y': '1947', 's': WIKI + 'Lighter', 'v': []})
# pipe-shape classics from the Tobacco pipe article
arch('Briar pipe', 'Poker', 'Sitter-type pipe with a flat base and an upright, cylindrical bowl; a variant of the Sitter.', '', '', WIKI + 'Tobacco_pipe')
arch('Briar pipe', 'Tankard', 'Sitter-type pipe with a tall bowl, flat base and a short shank.', '', '', WIKI + 'Tobacco_pipe')
for a in old['Briar pipe']['x']:
    pass
# Nicaraguan / Dominican additions
arch('Nicaraguan premium cigar', 'Don Pepin Garcia', 'Nicaraguan cigar maker\'s lines, made in Estelí.', '', '', WIKI + 'List_of_cigar_brands')

# ---- type groups (tt), by hand
TT = {
'Habano (Cuban premium cigar)': [['Straight-sided shape (parejo)', ['Robusto', 'Toro', 'Corona', 'Churchill', 'Corona gorda', 'Petit corona', 'Panatela', 'Double corona', 'Gordo', 'Lancero', 'Lonsdale']], ['Shaped (figurado)', ['Torpedo', 'Belicoso', 'Perfecto', 'Diadema', 'Culebra']]],
'Dominican premium cigar': [['Blend', ['Puro', 'Cameroon wrapper', 'Maduro wrapper']]],
'Nicaraguan premium cigar': [['Blend', ['Puro', 'Habano wrapper', 'Maduro wrapper']]],
'Honduran premium cigar': [['Wrapper leaf', ['Corojo', 'Maduro wrapper']]],
'Mexican & Brazilian cigar': [['Leaf origin', ['Mexican puro', 'Brazilian leaf']]],
'Cigarillo': [['Mouth end', ['Tipped cigarillo', 'Plain cigarillo']], ['Flavour', ['Flavoured cigarillo', 'Natural']]],
'Little cigar': [['Mouth end', ['Filtered little cigar', 'Plain little cigar']], ['Flavour', ['Flavoured little cigar', 'Natural']]],
'Machine-made cigar': [['Filler', ['Pipe-tobacco cigar', 'Short filler', 'Reconstituted']], ['Wrapper', ['Natural leaf', 'Blunt wrap']]],
'Toscano (Italian fire-cured cigar)': [['Making', ['Machine-made', 'Hand-rolled Toscano']]],
'Cheroot': [['Origin', ['Burmese', 'Indian']]],
'Humidor': [['Size and format', ['Travel humidor', 'Desktop humidor', 'Cabinet humidor', 'Walk-in humidor']], ['Humidity control', ['Passive', 'Electric humidor']]],
'Humidifier & humidity pack': [['Humidifying medium', ['Propylene glycol', 'Silica gel', 'Two-way humidity pack']], ['Power', ['Passive', 'Electronic humidifier']]],
'Hygrometer': [['Display', ['Analog hygrometer', 'Digital hygrometer']]],
'Cigar cutter': [['Cut', ['Guillotine', 'Double guillotine', 'Punch', 'V-cut', 'Scissors']]],
'Cigar case': [['Material', ['Leather case', 'Metal tube case']], ['Capacity', ['Single', 'Three-finger', 'Five-finger']]],
'Briar pipe': [['Finish', ['Smooth', 'Sandblasted', 'Rusticated']], ['Stem shape', ['Straight', 'Bent']], ['Stem material', ['Vulcanite', 'Acrylic', 'Cumberland', 'Amber']]],
'Freehand pipe': [['Finish', ['Smooth freehand', 'Sandblasted freehand']]],
'Meerschaum pipe': [['Making', ['Block meerschaum', 'Pressed meerschaum']], ['Carving', ['Plain', 'Carved figural']]],
'Corn cob pipe': [['Stem', ['Straight', 'Bent']], ['Size', ['Standard', 'Large bowl']]],
'Clay pipe': [['Stem length', ['Long clay', 'Short clay']]],
'Calabash pipe': [['Make', ['Gourd calabash', 'Reverse calabash', 'Briar calabash']]],
'Tyrolean pipe': [['Stem', ['Long stem']]],
'Kiseru': [['Make', ['Rau kiseru', 'Nobe kiseru']]],
'Midwakh': [['Material', ['Wooden midwakh', 'Metal midwakh']]],
'Virginia blend': [['Cut', ['Ribbon', 'Flake', 'Plug', 'Rope', 'Coin', 'Cube cut']]],
'Virginia/Perique blend': [['Cut', ['Flake', 'Ribbon']]],
'English & Balkan blend': [['Cut', ['Ribbon', 'Flake']]],
'Burley blend': [['Cut', ['Ribbon', 'Cube cut']]],
'Oriental blend': [['Cut', ['Ribbon', 'Flake']]],
'Aromatic blend': [['Cut', ['Ribbon', 'Cavendish']]],
'Kizami': [['Cut', ['Very fine']]],
'Dokha': [['Strength', ['Hot', 'Warm', 'Cold']]],
'Pipe tamper & tool': [['Form', ['Pipe nail', 'Three-in-one (Czech) tool', 'Decorative tamper']]],
'Pipe cleaner': [['Shape', ['Bristle', 'Fluffy', 'Tapered']]],
'Pipe filter': [['Material', ['9 mm charcoal', '6 mm balsa', 'Paper']]],
'Pipe reamer': [['Mechanism', ['Four-head fixed reamer', 'Adjustable reamer']]],
'Pipe stand & rack': [['Capacity', ['Single stand', 'Multi-pipe rack']]],
'Pipe case & bag': [['Construction', ['Pipe bag', 'Hard case']]],
'Tobacco pouch': [['Closure', ['Roll-up', 'Zipper']], ['Material', ['Leather']], ['Contents', ['Pipe-combo']]],
'Tobacco jar': [['Material and seal', ['Glass jar', 'Tupperdor', 'Humidor']]],
'Manufactured cigarette': [['Filter', ['Filtered', 'Plain (unfiltered)', 'Charcoal filter']], ['Flavour', ['Menthol']], ['Size', ['Slims']]],
'Roll-your-own tobacco': [['Use', ['Fine-cut', 'Make-your-own (MYO)']]],
'Kretek (clove cigarette)': [['Making', ['Filtered kretek', 'Hand-rolled kretek']]],
'Bidi': [['Flavour', ['Plain bidi', 'Flavoured bidi']]],
'Rolling paper': [['Size', ['Single wide', '1¼', 'King size', 'King size slim']], ['Material', ['Hemp', 'Unbleached']], ['Form', ['Blunt wrap']], ['Flavour', ['Flavoured']]],
'Filter tip': [['Material', ['Card roach', 'Cotton or foam filter', 'Glass tip']]],
'Rolling tray': [['Material', ['Metal', 'Wood', 'Rubber']]],
'Rolling machine': [['Mechanism', ['Hand roller', 'Rollbox', 'Tube-filling machine']]],
'Cigarette tube': [['Length', ['King size', '100s']], ['Shape', ['Cone']]],
'Tube injector': [['Drive', ['Hand injector', 'Crank injector', 'Electric machine']]],
'Cigalike': [['Power', ['Disposable', 'Rechargeable']]],
'Disposable vape': [['Nicotine', ['Nicotine-salt disposable']], ['Battery', ['Rechargeable disposable']]],
'Refillable pod kit': [['Pod system', ['Closed pod', 'Open pod']]],
'Vape pen kit': [['Holder', ['Cartridge pen', 'Tank pen']]],
'Box mod kit': [['Batteries', ['Single battery', 'Dual battery']], ['Control', ['Regulated', 'Temperature control']]],
'Mechanical mod': [['Body', ['Tube mech', 'Box mech']]],
'Squonk mod': [['Control', ['Mechanical squonker', 'Regulated squonker']]],
'Vape tank': [['Draw', ['MTL clearomiser', 'Sub-ohm tank']]],
'Rebuildable tank atomiser (RTA)': [['Draw', ['Mouth-to-lung RTA', 'Direct-lung RTA']], ['Coil count', ['Single coil', 'Dual coil']]],
'Rebuildable dripping atomiser (RDA)': [['Build deck', ['Single post', 'Two-post clamp']], ['Feed', ['Squonk (BF) RDA']]],
'Refillable pod': [['Pod system', ['Open pod']]],
'Vape coil': [['Construction', ['Mesh', 'Ceramic', 'Wire-wound']], ['Draw', ['Mouth-to-lung', 'Sub-ohm']]],
'Coil-building wire & cotton': [['Wire alloy', ['Kanthal', 'Nichrome', 'Stainless steel']], ['Wire form', ['Clapton']], ['Supply', ['Wicking cotton', 'Coil jig']]],
'Vape drip tip': [['Width', ['510', '810']]],
'Vape battery cell': [['Cell size', ['18650', '20700', '21700']]],
'Vape pen battery': [['Thread', ['510 thread']]],
'E-liquid': [['Nicotine type', ['Freebase e-liquid', 'Nic-salt e-liquid', 'Zero-nicotine e-liquid']]],
'Prefilled pod': [['Nicotine type', ['Freebase', 'Nic-salt']]],
'Heated-tobacco device': [['Heating method', ['Stick-heating', 'Capsule-type (vapour passes through a tobacco capsule)']]],
'Heating stick': [['Content', ['Tobacco', 'Tobacco-free']]],
'Portion snus': [['Moisture', ['Original portion snus', 'White portion snus']], ['Pouch size', ['Mini portion']]],
'Loose snus': [['Grind', ['Fine ground', 'Coarse (grov)']]],
'Nicotine pouch': [['Pouch size', ['Slim', 'Mini']], ['Strength', ['Strong']]],
'Dissolvable nicotine product': [['Form', ['Dissolvable tobacco', 'Nicotine pearl', 'Nicotine toothpick']]],
'Dipping tobacco': [['Cut', ['Fine cut', 'Long cut']], ['Format', ['Pouch']]],
'Creamy snuff': [['Form', ['Paste']]],
'Chewing tobacco': [['Form', ['Loose leaf', 'Plug', 'Twist', 'Kautabak stick']]],
'Gutkha': [['Sale form', ['Sachet']]],
'Naswar': [['Preparation', ['Dried', 'Moist']]],
'Iqmik': [['Preparation', ['Hand-mixed']]],
'Nasal snuff': [['Grind and additive', ['Fine snuff', 'Scented snuff', 'Medicated snuff', 'Tobacco-free snuff']]],
'Rapé': [['Preparation', ['Plain', 'Blended with plant ash']]],
'Snuff box': [['Material', ['Gold', 'Silver', 'Enamel', 'Tortoiseshell', 'Papier-mâché', 'Porcelain']]],
'Snuff bottle': [['Material', ['Glass', 'Porcelain', 'Jade and hardstone', 'Enamel']], ['Decoration', ['Inside-painted']]],
'Hookah': [['Hose count', ['Single-hose', 'Multi-hose']], ['Size', ['Travel hookah']]],
'Shisha tobacco': [['Base', ['Molasses-based']], ['Flavour', ['Flavoured', 'Unflavoured']]],
'Tumbak': [['Preparation', ['Washed tumbak', 'Dry tumbak']]],
'Khansar': [['Preparation', ['Plain']]],
'Tobacco-free shisha': [['Base', ['Molasses herbal mix', 'Steam stones']]],
'Hookah bowl': [['Material', ['Egyptian clay bowl', 'Silicone bowl']], ['Design', ['Turkish/funnel bowl', 'Phunnel', 'Vortex bowl']]],
'Heat management device': [['Material', ['Aluminium HMD', 'Stainless HMD']]],
'Hookah charcoal': [['Fuel', ['Natural coconut cubes', 'Quick-light']]],
'Coal tongs, burners & windcovers': [['Item', ['Tongs', 'Windcover', 'Electric coal burner']]],
'Hookah hose & mouth tip': [['Hose material', ['Washable silicone', 'Leather/traditional']], ['Tip', ['Disposable', 'Reusable']]],
'Hookah spare parts': [['Part', ['Grommet', 'Diffuser', 'Downstem', 'Base gasket', 'Molasses catcher']]],
'Pocket lighter': [['Ignition', ['Flint-wheel', 'Piezo']], ['Fuel', ['Windproof butane']], ['Life', ['Disposable', 'Refillable']]],
'Cigar lighter': [['Flame', ['Jet/torch', 'Multi-jet', 'Soft flame']]],
'Pipe lighter': [['Flame', ['Soft flame', 'Inline']]],
'Table lighter': [['Ignition', ['Touch-tip']], ['Placement', ['Desk']]],
'Electric lighter': [['Heat source', ['Arc/plasma', 'Heating element']], ['Power', ['USB-rechargeable']]],
'Permanent match': [['Fuel', ['Naphtha']]],
'Lighter fuel, flints & wicks': [['Item', ['Naphtha fuel', 'Butane fuel', 'Flints', 'Wicks']]],
'Ashtray': [['Setting', ['Pocket ashtray', 'Standing ashtray']], ['Use', ['Cigar ashtray', 'Advertising ashtray']], ['Design', ['Covered ashtray']]],
'Cigarette case': [['Material', ['Metal', 'Leather', 'Silver', 'Enamel']], ['Form', ['Flat fifty tin']]],
'Cigarette holder': [['Length', ['Opera (16-20 in)', 'Theatre (10-14 in)', 'Dinner (4-6 in)', "Men's (up to 4 in)"]], ['Style', ['Cocktail', 'Filter holder']]],
'Cannabis flower': [['Plant type', ['Indica', 'Sativa', 'Hybrid', 'High-CBD']]],
'Pre-roll': [['Content', ['Cannabis pre-roll', 'Infused cannabis pre-roll']]],
'Hashish': [['Method', ['Dry-sift', 'Hand-rubbed charas', 'Ice-water (bubble) hash', 'Kief (loose resin glands)']]],
'Rosin': [['Source', ['Flower rosin', 'Hash rosin']]],
'Solvent-extracted concentrate': [['Texture', ['Shatter', 'Badder', 'Crumble', 'Sauce', 'Live resin']]],
'Prefilled vape cartridge': [['Contents', ['Cannabinoid oil', 'Nicotine', 'Distillate']]],
'Infused edible': [['Form', ['Gummy', 'Chocolate', 'Baked good', 'Mint', 'Hard candy']]],
'Infused drink': [['Serving', ['Drink', 'Shot']]],
'Tincture, capsule or tablet': [['Dose form', ['Tincture', 'Capsule', 'Tablet']]],
'Topical': [['Texture', ['Balm', 'Lotion', 'Cream']]],
'Bong': [['Shape', ['Beaker', 'Straight tube', 'Bubbler']], ['Filtration', ['Percolator']]],
'Dab rig': [['Design', ['Recycler', 'Mini rig', 'Concentrate bubbler']]],
'Electronic dab rig': [['Heater', ['Ceramic heater', 'Quartz heater']]],
'Hand pipe & chillum': [['Shape', ['Spoon', 'Sherlock', 'Steamroller', 'Chillum']], ['Size', ['One-hitter', 'Dugout']]],
'Water-pipe bowls & bangers': [['Part', ['Bowl slide', 'Downstem', 'Ash catcher', 'Quartz banger', 'Carb cap']]],
'Portable vaporiser': [['Heat transfer', ['Conduction', 'Convection']], ['Power', ['Butane-heated']]],
'Desktop vaporiser': [['Delivery', ['Bag-fed', 'Whip-fed']]],
'Grinder': [['Pieces', ['2-piece', '3-piece', '4-piece with kief catcher']]],
'Areca nut & betel quid': [['Preparation', ['Plain areca nut', 'Betel quid (paan)']]],
'Kratom': [['Form', ['Powder', 'Dried leaf', 'Capsules', 'Shots']]],
'Khat': [['Stem type', ['Miraa', 'Muguka']]],
'Salvia': [['Form', ['Dried leaf', 'Extract']]],
}

# ---- layout: department -> shelves -> kinds
CAT_AX = 'What is the product, and how is it taken: a cigar or pipe smoked from leaf, a manufactured or hand-rolled cigarette, a vape or heated stick, an oral or nasal product, a water pipe, a cannabis product or another plant?'
KEY = [
 '1. Is it made from cannabis or hemp, or gear used for dry herb and concentrates? → Cannabis & hemp',
 '2. Is it a cigar, or a humidor, cutter or case made for cigars? → Cigars',
 '3. Is it a pipe, the tobacco burned in it or a tool or container for it? → Pipes & pipe tobacco',
 '4. Is it a water pipe, shisha or a part of one? → Hookah & shisha',
 '5. Is it a cigarette, loose tobacco, a rolling paper or hand-rolling gear? → Cigarettes & rolling',
 '6. Is it a vape device, a vape part, e-liquid or a heated-tobacco system? → Vaping & heated tobacco',
 '7. Is the tobacco held in the mouth, chewed or sniffed rather than burned or heated? → Snus, snuff & chewing tobacco',
 '8. Does it make the flame, or hold ash or cigarettes, whatever is smoked? → Lighters & smoking accessories',
 '9. Is it a chewed, smoked or brewed plant that is neither tobacco nor cannabis? → Herbal & other plant products',
 '<i>Precedence: cannabis gear is step 1 even when it looks like a pipe or vaporiser; a cigar lighter is a lighter (step 8) but a cigar cutter is a cigar tool (step 2); a nicotine pouch is step 7, not step 6.</i>',
]
L = [
 ('Cigars', 'Cigars, from the premium handmade leaf to small machine-made ones, and the gear that stores, cuts and carries them; a lighter → Lighters & smoking accessories; a dish served with cigars → none.',
  'Is it a handmade cigar by country, a small or machine-made cigar, or gear for keeping, cutting and carrying cigars?', [
  ('Cuban cigars (Habanos)', 'Handmade cigars made in Cuba and sold under the Habanos S.A. marques, such as Cohiba, Montecristo and Partagás; a cigar from another country → New World premium cigars.', 'kinds by marque tier: global marques first, then smaller ones', ['Habano (Cuban premium cigar)']),
  ('New World premium cigars', 'Handmade cigars from outside Cuba, such as Padrón from Nicaragua, Arturo Fuente from the Dominican Republic and Camacho from Honduras; a Cuban cigar → Cuban cigars.', 'kinds by country of origin: Dominican Republic, Nicaragua, Honduras, Mexico and Brazil', ['Dominican premium cigar', 'Nicaraguan premium cigar', 'Honduran premium cigar', 'Mexican & Brazilian cigar']),
  ('Small, machine-made & regional cigars', 'Cheap, small or regional cigars such as cigarillos, little cigars, Black & Mild and Toscano; a handmade premium cigar → the premium shelves.', 'kinds by size and make: small, factory-made, then regional leaf-rolled', ['Cigarillo', 'Little cigar', 'Machine-made cigar', 'Cheroot', 'Toscano (Italian fire-cured cigar)']),
  ('Humidors & humidity control', 'Boxes and devices that keep cigars at about 70% humidity: humidors, humidifiers and hygrometers; a cutter or case → Cutters & cases.', 'kinds by role: the box, what humidifies it, what measures it', ['Humidor', 'Humidifier & humidity pack', 'Hygrometer']),
  ('Cutters & cases', 'Tools and cases used on the cigar itself: cutters such as guillotines and V-cuts, and cases that carry cigars on the person; a lighter → Lighters.', 'kinds by use: cut the cap, then carry', ['Cigar cutter', 'Cigar case'])]),
 ('Pipes & pipe tobacco', 'Tobacco pipes, the tobacco made for them and the tools and containers that go with them; a water pipe → Hookah & shisha, a cannabis pipe → Cannabis & hemp.',
  'Is it the pipe, the tobacco burned in it, or a tool or container for looking after it?', [
  ('Pipes', 'Pipes for smoking tobacco, from briar and freehand to meerschaum, cob, clay and regional pipes like the kiseru; a water pipe → Hookah & shisha.', 'kinds by bowl material or regional tradition: briar, meerschaum, cob, clay, gourd, then regional', ['Briar pipe', 'Freehand pipe', 'Meerschaum pipe', 'Corn cob pipe', 'Clay pipe', 'Calabash pipe', 'Tyrolean pipe', 'Kiseru', 'Midwakh']),
  ('Pipe tobacco', 'Loose tobacco and blends made for pipes, such as Virginia flakes, English mixtures and aromatics; cigarette tobacco → Cigarettes & rolling.', 'kinds by leaf and blend: Virginia-led, Burley-led, Oriental, flavoured, then regional pipe tobaccos', ['Virginia blend', 'Virginia/Perique blend', 'English & Balkan blend', 'Burley blend', 'Oriental blend', 'Aromatic blend', 'Kizami', 'Dokha']),
  ('Pipe tools & care', 'Small tools and consumables for smoking and cleaning a pipe, such as tampers, cleaners, filters and reamers; a stand or pouch → Pipe storage & carrying.', 'kinds by task: pack and tamp, clean, filter, ream', ['Pipe tamper & tool', 'Pipe cleaner', 'Pipe filter', 'Pipe reamer']),
  ('Pipe storage & carrying', 'Holders for pipes and pipe tobacco, such as stands, cases, pouches and jars; a cleaning tool → Pipe tools & care.', 'kinds by what is held: pipes at rest, pipes on the move, tobacco on the move, tobacco at home', ['Pipe stand & rack', 'Pipe case & bag', 'Tobacco pouch', 'Tobacco jar'])]),
 ('Cigarettes & rolling', 'Manufactured and hand-rolled cigarettes and the papers, filters and machines for rolling them; a cigar → Cigars, a vape → Vaping & heated tobacco.',
  'Is it the cigarette or smoke itself, or the paper and gear used to roll one?', [
  ('Cigarettes & loose tobacco', 'Cigarettes and loose tobacco for rolling, such as Marlboro, Golden Virginia, kretek and bidi; a pipe blend → Pipe tobacco.', 'kinds by making: factory, loose for rolling, clove, leaf-wrapped', ['Manufactured cigarette', 'Roll-your-own tobacco', 'Kretek (clove cigarette)', 'Bidi']),
  ('Papers, tubes & rolling gear', 'Everything used to roll a cigarette or joint by hand, such as papers, filter tips, machines and empty tubes; the tobacco itself → Cigarettes & loose tobacco.', 'kinds by rolling method: paper and filter, aids, then the tube route', ['Rolling paper', 'Filter tip', 'Rolling tray', 'Rolling machine', 'Cigarette tube', 'Tube injector'])]),
 ('Vaping & heated tobacco', 'Electronic cigarettes, their parts and liquids, and heated-tobacco systems that warm rather than burn tobacco; a nicotine pouch → Snus, snuff & chewing tobacco.',
  'Is it a complete device, a part that holds, heats or powers, the liquid used, or a heated-tobacco system?', [
  ('Vape kits & mods', 'Complete vape devices from the first cigalikes to disposables, pod kits, pen kits and mods; a loose tank or coil → Tanks, atomisers, coils & batteries.', 'kinds by device generation and control: cigalike and disposable, pod, pen, regulated box, mechanical, squonk', ['Cigalike', 'Disposable vape', 'Refillable pod kit', 'Vape pen kit', 'Box mod kit', 'Mechanical mod', 'Squonk mod']),
  ('Tanks, atomisers, coils & batteries', 'Parts that hold liquid, heat it or power a vape, such as tanks, rebuildable atomisers, coils, drip tips and 18650 cells; a complete device → Vape kits & mods.', 'kinds by job: hold the liquid, heat it, then power it', ['Vape tank', 'Rebuildable tank atomiser (RTA)', 'Rebuildable dripping atomiser (RDA)', 'Refillable pod', 'Vape coil', 'Coil-building wire & cotton', 'Vape drip tip', 'Vape battery cell', 'Vape pen battery']),
  ('E-liquids & prefilled pods', 'Liquid made for vaping, in bottles or sealed pods; a cannabis cartridge → Flower, hash & concentrates.', 'kinds by pack: bottle to fill, sealed pod', ['E-liquid', 'Prefilled pod']),
  ('Heated tobacco', 'Devices and sticks that heat tobacco without burning it, such as IQOS and Ploom; a vape with liquid → Vape kits & mods.', 'kinds by part: the device, then the consumable', ['Heated-tobacco device', 'Heating stick'])]),
 ('Snus, snuff & chewing tobacco', 'Tobacco and nicotine taken in the mouth or nose without burning, and the boxes made for snuff; a cigarette → Cigarettes & rolling.',
  'Is it held under the lip, chewed or dipped, a regional oral mix, sniffed or the box that holds it?', [
  ('Snus & nicotine pouches', 'Pouches and loose portions held under the upper lip, from Swedish snus to tobacco-free nicotine pouches; chewing tobacco → Chewing, dipping & regional oral tobacco.', 'kinds by form: portioned snus, loose snus, tobacco-free pouch, dissolvable', ['Portion snus', 'Loose snus', 'Nicotine pouch', 'Dissolvable nicotine product']),
  ('Chewing, dipping & regional oral tobacco', 'Tobacco chewed or held in the cheek or lip, such as chewing plugs, dipping tobacco, gutkha and naswar; snus → Snus & nicotine pouches.', 'kinds by region and form: Western chew and dip first, then South Asian, Afghan and Alaskan oral tobacco', ['Chewing tobacco', 'Dipping tobacco', 'Creamy snuff', 'Gutkha', 'Naswar', 'Iqmik']),
  ('Nasal snuff', 'Powdered tobacco or tobacco-free powder sniffed through the nose, such as Wilsons of Sharrow snuffs and Brazilian rapé; oral tobacco → the oral shelves.', 'kinds by tradition: European snuff, then Amazonian rapé', ['Nasal snuff', 'Rapé']),
  ('Snuff boxes & bottles', 'Containers made to carry snuff, from European gold and enamel boxes to Chinese snuff bottles; a tobacco jar → Pipe storage & carrying.', 'kinds by container: box, then bottle', ['Snuff box', 'Snuff bottle'])]),
 ('Hookah & shisha', 'Water pipes, the tobacco burned in them and their bowls, coals and hoses; a tobacco pipe → Pipes & pipe tobacco, a cannabis water pipe → Cannabis & hemp.',
  'Is it the hookah itself, what is burned in it, the bowl and heat, or the hose and wearing parts?', [
  ('Hookahs', 'Water pipes with a base, stem, bowl and hoses, in Egyptian, Turkish, Persian, Indian and modern designs; a part of one → the parts shelves.', '', ['Hookah']),
  ('Shisha & hookah tobacco', 'What is smoked in a hookah: molasses mu\'assel, unflavoured tumbak, Iranian khansar and tobacco-free mixes; pipe tobacco → Pipe tobacco.', 'kinds by base: molasses, dry tobacco, tobacco-free', ['Shisha tobacco', 'Tumbak', 'Khansar', 'Tobacco-free shisha']),
  ('Bowls, heat & coals', 'What holds and heats the shisha: bowls, heat management devices, charcoal and the tools for handling coals; a hose → Hoses & parts.', 'kinds by order in the stack: bowl, heat device, charcoal, coal tools', ['Hookah bowl', 'Heat management device', 'Hookah charcoal', 'Coal tongs, burners & windcovers']),
  ('Hoses & parts', 'Hoses with their mouth tips and the wearing parts swapped by owners, such as grommets and downstems; a bowl → Bowls, heat & coals.', 'kinds by part: hose then spare parts', ['Hookah hose & mouth tip', 'Hookah spare parts'])]),
 ('Lighters & smoking accessories', 'Gear that makes the flame or holds ash and cigarettes whatever is smoked; a cigar cutter or humidor → Cigars, a rolling machine → Cigarettes & rolling.',
  'Does it make the flame, or hold ash and cigarettes?', [
  ('Lighters', 'Devices and matches that make a flame for tobacco, from Zippo wick lighters to butane, jet and electric ones; fuel and flints are included.', 'kinds by use and flame: pocket, cigar, pipe, table, electric, match, then consumables', ['Pocket lighter', 'Cigar lighter', 'Pipe lighter', 'Table lighter', 'Electric lighter', 'Permanent match', 'Lighter fuel, flints & wicks']),
  ('Ashtrays, cases & holders', 'Things that hold ash, spare cigarettes or a cigarette in use, such as ashtrays, cigarette cases and holders; a cigar case → Cutters & cases.', 'kinds by what is held: ash, spare cigarettes, the lit cigarette', ['Ashtray', 'Cigarette case', 'Cigarette holder'])]),
 ('Cannabis & hemp', 'Cannabis and hemp products and the gear for using them; legality varies by country and state. A rolling paper → Cigarettes & rolling, a vape pen for nicotine → Vaping & heated tobacco.',
  'Is it the plant material, a product to eat, drink or apply, or the gear that burns, heats or prepares it?', [
  ('Flower, hash & concentrates', 'Cannabis to smoke or vape, from dried flower to pressed resin and solvent extracts; edibles → Edibles, tinctures & topicals.', 'kinds by processing: flower, rolled, pressed resin, extract, cartridge', ['Cannabis flower', 'Pre-roll', 'Hashish', 'Rosin', 'Solvent-extracted concentrate', 'Prefilled vape cartridge']),
  ('Edibles, tinctures & topicals', 'Cannabis products swallowed, drunk or applied to the skin, such as gummies, drinks, capsules and balms; flower and extracts → Flower, hash & concentrates.', 'kinds by route: eaten, drunk, swallowed in a dose, applied to skin', ['Infused edible', 'Infused drink', 'Tincture, capsule or tablet', 'Topical']),
  ('Bongs, pipes & vaporisers', 'Gear for burning or heating cannabis, from bongs and dab rigs to pipes, vaporisers and grinders; a tobacco pipe → Pipes.', 'kinds by how the material is heated: water pipes, dry pipes, electric vaporisers, then preparation', ['Bong', 'Dab rig', 'Water-pipe bowls & bangers', 'Hand pipe & chillum', 'Electronic dab rig', 'Portable vaporiser', 'Desktop vaporiser', 'Grinder'])]),
 ('Herbal & other plant products', 'Chewed, smoked or brewed plant products that are neither tobacco nor cannabis; listed for completeness, with no models. Tobacco leaf → the tobacco departments.',
  'How is the plant product taken: chewed, or smoked and swallowed?', [
  ('Chewed leaf & nut', 'Plants chewed or held in the mouth, such as areca nut and betel quid, khat, kratom leaf and salvia leaf.', 'kinds by plant part: nut, leaf', ['Areca nut & betel quid', 'Khat', 'Kratom', 'Salvia']),
  ('Smoked & swallowed plant products', 'Plant products that are smoked or swallowed, such as herbal smoking blends, dried mushrooms and dried opium.', 'kinds by route: smoked, then swallowed', ['Herbal smoking blend', 'Dried opium', 'Psychoactive mushroom product'])]),
]

# cross-links
SEE = {
 'Hygrometer': [['E6', 'Hygrometer', 'same gauge sold for weather stations']],
 'Rosin': [['E3', 'Rosin', 'different thing: rosin for bow hair']],
 'Salvia': [['C3', 'Salvia', 'different thing: the garden salvia plant']],
 'Cigar lighter': [['J10', 'Cigar cutter', 'cut the cap before lighting']],
 'Cigar case': [['J10', 'Cigarette case', 'same job for cigarettes']],
 'Cigarette case': [['J10', 'Cigar case', 'same job for cigars']],
 'Tobacco pouch': [['J10', 'Roll-your-own tobacco', 'pouch also carries loose rolling tobacco']],
 'Shisha tobacco': [['J10', 'Virginia blend', 'pipe tobacco is a different leaf and cut']],
 'Hookah': [['J10', 'Bong', 'cannabis water pipe']],
 'Bong': [['J10', 'Hookah', 'tobacco water pipe']],
 'Nicotine pouch': [['J10', 'Portion snus', 'tobacco version of the same pouch']],
 'Portion snus': [['J10', 'Nicotine pouch', 'tobacco-free version of the same pouch']],
 'Prefilled vape cartridge': [['J10', 'Prefilled pod', 'sealed nicotine pod for pod kits']],
 'Rolling paper': [['J10', 'Pre-roll', 'ready-rolled joint']],
 'Pre-roll': [['J10', 'Rolling paper', 'paper for rolling your own']],
 'Kiseru': [['J10', 'Kizami', 'tobacco cut made for the kiseru']],
 'Midwakh': [['J10', 'Dokha', 'tobacco smoked in the midwakh']],
 'Grinder': [['J10', 'Rolling tray', 'prepare and roll together']],
 'Permanent match': [['J10', 'Pocket lighter', 'lighter alternative']],
 'Heating stick': [['J10', 'Heated-tobacco device', 'device the stick fits']],
}

placed = set(); depts = []
oldmodes = {dp['n']: dp for dp in d['depts']}
for dn, dt, dax, shelves in L:
    od = oldmodes[dn]
    nd = {'n': dn, 'mode': od['mode'], 't': dt, 'ax': dax}
    if od.get('note'): nd['note'] = od['note']
    if od.get('b'): nd['b'] = od['b']
    nd['s'] = []
    for sn, st, sax, kinds in shelves:
        ks = []
        for kn in kinds:
            k = old[kn]; placed.add(kn)
            k = copy.deepcopy(k)
            if kn in TT:
                k['tt'] = TT[kn]; k.pop('t', None)
            elif k.get('t'):
                print('NO TT for', kn)
            if kn in SEE: k['see'] = SEE[kn]
            ks.append(k)
        sh = {'n': sn, 't': st}
        if len(ks) > 3 or sax: sh['ax'] = sax
        if not sh.get('ax') and len(ks) > 3: raise SystemExit('ax needed ' + sn)
        sh['k'] = ks
        nd['s'].append(sh)
    depts.append(nd)
missing = set(old) - placed
print('unplaced:', missing)
d['ax'] = CAT_AX; d['key'] = KEY
d['lead'] = 'Tobacco, nicotine, cannabis and other smokable or chewable plant products with the gear used to smoke, vape and store them, organised by how the product is taken (cigars, pipes, cigarettes, vaping, oral and nasal tobacco, shisha, cannabis, herbal), with house, line and shape for cigars and pipes.'
d['depts'] = depts
json.dump(d, open(R + 'work/STR_J10/J10.new.json', 'w'), ensure_ascii=False, indent=1)
json.dump(brands, open(R + 'work/STR_J10/J10_brands.new.json', 'w'), ensure_ascii=False, indent=1)
json.dump(RENAMES, open(R + 'work/STR_J10/J10_renames.new.json', 'w'), ensure_ascii=False, indent=1)
