import json, copy, re, os
W = '/home/user/Possession-Taxonomy/rebuild/work/V4_G1_COMMERCIAL/'
OUT = '/home/user/Possession-Taxonomy/rebuild/out/G1_parts/COMMERCIAL.json'
src = json.load(open('/home/user/Possession-Taxonomy/rebuild/out/G1.json'))
NAMES = ["Vans, trucks & buses", "Caravans, motorhomes & trailers", "Off-road & leisure vehicles", "Heritage rail & horse-drawn"]
dept = {x['n']: copy.deepcopy(x) for x in src['depts'] if x['n'] in NAMES}
brands_old = {b['n']: b for b in json.load(open('/home/user/Possession-Taxonomy/rebuild/out/G1_brands.json'))['b']}
WP = 'https://en.wikipedia.org/wiki/'
U_PICK = WP + 'List_of_pickup_trucks'
U_VANS = WP + 'List_of_vans'
U_TRUCKS = WP + 'List_of_trucks'
U_HDV = WP + 'Horse-drawn_vehicle'
U_RVM = WP + 'List_of_recreational_vehicle_manufacturers'
U_BRP = WP + 'List_of_Bombardier_recreational_and_snow_vehicles'
U_POL = WP + 'Polaris_Inc.'
U_ARC = WP + 'Arctic_Cat'
U_CLUB = WP + 'Club_Car'
U_THOR = WP + 'Thor_Industries'
U_HYM = WP + 'Hymer'
U_WIN = WP + 'Winnebago_Industries'
U_AIR = WP + 'Airstream'
U_SWIFT = WP + 'Swift_Leisure'
U_KNAUS = 'https://www.knaustabbert.de/en/press/press-releases/knaus-tabbert-at-the-caravan-salon-duesseldorf/'
U_ATV = WP + 'All-terrain_vehicle'
U_UTV = WP + 'Utility_terrain_vehicle'
U_VW = WP + 'Volkswagen_Transporter'
U_SPR = WP + 'Mercedes-Benz_Sprinter'
U_SNOW = WP + 'Snowmobile'
U_OB = WP + 'Bedford_OB'
U_RV = WP + 'Recreational_vehicle'
U_PU = WP + 'Pickup_truck'
U_GOLF = WP + 'Golf_cart'

def norm(s): return re.sub(r'[^a-z0-9]+', '', s.lower())

def E(n, mk='', y='', d='', s='', a='', g='', v=None, role=None, own=None, tier=None, cty=None, own_y=None, dt=None):
    e = {'n': n}
    if a: e['a'] = a
    e['d'] = d
    e['mk'] = mk
    e['y'] = y
    e['s'] = s
    e['v'] = v or []
    if dt: e['dt'] = dt
    if g: e['g'] = g
    if role: e['role'] = role
    if own: e['own'] = own
    if tier: e['tier'] = tier
    if cty: e['cty'] = cty
    if own_y: e['own_y'] = own_y
    return e

def V(n, y='', d='', mk=''):
    return {'n': n, 'mk': mk, 'y': y, 'd': d}

def find_kind(dp, kn):
    for s in dp['s']:
        for k in s['k']:
            if k['n'] == kn: return k
    raise KeyError(kn)

def all_names(k):
    S = set()
    for e in k.get('x', []):
        S.add(norm(e['n']))
        for al in re.split(r'\s*·\s*', e.get('a', '')):
            if al: S.add(norm(al))
        for v in e.get('v', []): S.add(norm(v['n']))
    return S

def add(k, e):
    """append entry unless a same-named entry or version already exists"""
    S = all_names(k)
    if norm(e['n']) in S: return False
    k.setdefault('x', []).append(e)
    return True

def drop_m(k):
    k.pop('m', None)

def sort_kind(k, order):
    """order entries by group order list, then year, then name"""
    def key(e):
        g = e.get('g', '')
        gi = order.index(g) if g in order else len(order)
        y = re.search(r'\d{4}', e.get('y', '') or '')
        return (gi, g, int(y.group()) if y else 9999, e['n'].lower())
    k['x'].sort(key=key)

def groups(k):
    seen = []
    for e in k.get('x', []):
        if e.get('g') and e['g'] not in seen: seen.append(e['g'])
    return seen

# ---------------------------------------------------------------- owners
OWN = {
    'Ford': ('Ford Motor Company', 'Global group', 'United States'),
    'Chevrolet': ('General Motors', 'Global group', 'United States'),
    'GMC': ('General Motors', 'Global group', 'United States'),
    'Ram': ('Stellantis', 'Global group', 'United States'),
    'Dodge': ('Stellantis', 'Global group', 'United States'),
    'Jeep': ('Stellantis', 'Global group', 'United States'),
    'Fiat': ('Stellantis', 'Global group', 'Italy'),
    'Fiat Professional': ('Stellantis', 'Global group', 'Italy'),
    'Citroën': ('Stellantis', 'Global group', 'France'),
    'Peugeot': ('Stellantis', 'Global group', 'France'),
    'Opel': ('Stellantis', 'Global group', 'Germany'),
    'Opel/Vauxhall': ('Stellantis', 'Global group', 'Germany'),
    'Vauxhall': ('Stellantis', 'Global group', 'United Kingdom'),
    'Toyota': ('Toyota Motor Corporation', 'Global group', 'Japan'),
    'Daihatsu': ('Toyota Motor Corporation', 'Global group', 'Japan'),
    'Hino': ('Toyota Motor Corporation', 'Global group', 'Japan'),
    'Nissan': ('Nissan Motor Corporation', 'Global group', 'Japan'),
    'Honda': ('Honda Motor Company', 'Global group', 'Japan'),
    'Mitsubishi': ('Mitsubishi Motors', 'Global group', 'Japan'),
    'Mazda': ('Mazda Motor Corporation', 'Global group', 'Japan'),
    'Isuzu': ('Isuzu Motors', 'Global group', 'Japan'),
    'Suzuki': ('Suzuki Motor Corporation', 'Global group', 'Japan'),
    'Subaru': ('Subaru Corporation', 'Global group', 'Japan'),
    'Hyundai': ('Hyundai Motor Group', 'Global group', 'South Korea'),
    'Kia': ('Hyundai Motor Group', 'Global group', 'South Korea'),
    'Volkswagen': ('Volkswagen Group', 'Global group', 'Germany'),
    'Mercedes-Benz': ('Mercedes-Benz Group', 'Global group', 'Germany'),
    'Renault': ('Renault Group', 'Global group', 'France'),
    'Dacia': ('Renault Group', 'Global group', 'Romania'),
    'Tata': ('Tata Motors', 'National champion', 'India'),
    'Tata Motors': ('Tata Motors', 'National champion', 'India'),
    'Mahindra': ('Mahindra & Mahindra', 'National champion', 'India'),
    'Mahindra & Mahindra': ('Mahindra & Mahindra', 'National champion', 'India'),
    'Land Rover': ('Jaguar Land Rover', 'Independent', 'United Kingdom'),
    'GAZ': ('GAZ Group', 'National champion', 'Russia'),
    'UAZ': ('UAZ', 'National champion', 'Russia'),
    'Great Wall': ('Great Wall Motor', 'National champion', 'China'),
    'Tesla': ('Tesla, Inc.', 'Independent', 'United States'),
    'Rivian': ('Rivian', 'Independent', 'United States'),
    'Maxus': ('SAIC Motor', 'National champion', 'China'),
    'MG': ('SAIC Motor', 'National champion', 'United Kingdom'),
    'BYD': ('BYD Company', 'National champion', 'China'),
    'SAIC-GM-Wuling': ('SAIC-GM-Wuling', 'National champion', 'China'),
    'Wuling': ('SAIC-GM-Wuling', 'National champion', 'China'),
    'Ineos': ('Ineos Automotive', 'Independent', 'United Kingdom'),
    'Freightliner': ('Daimler Truck', 'Global group', 'United States'),
    'International': ('Traton', 'Global group', 'United States'),
    'Iveco': ('Iveco Group', 'Global group', 'Italy'),
    'Kia ': None,
}

def own_fields(mk):
    o = OWN.get(mk)
    if not o: return {}
    return {'own': o[0], 'tier': o[1], 'cty': o[2]}

def mkgroup(mk):
    return {'Opel/Vauxhall': 'Opel / Vauxhall', 'Fiat Professional': 'Fiat / Fiat Professional', 'Fiat': 'Fiat / Fiat Professional',
            'Mahindra & Mahindra': 'Mahindra', 'Tata Motors': 'Tata'}.get(mk, mk)

# ================================================================ DEPT 1
d1 = dept['Vans, trucks & buses']
d1['t'] = ('Vans, minibuses, taxis, pickups, lorries and coaches that a person owns or converts; a family car or SUV → Cars; '
           'a van converted for living in → Caravans, motorhomes & trailers.')
d1['note'] = ('Vans, pickups and preserved buses are named by marque; heavy trucks stay kind-level because lorries and tractor units are trade equipment (RULES scope rule).')
shelf_van, shelf_truck = d1['s'][0], d1['s'][1]
shelf_van['t'] = 'Van-bodied vehicles for people or goods: load vans, seated vans, minibuses and taxis; a lorry → Trucks & buses; a pickup → Pickups.'
shelf_truck['t'] = 'Heavy vehicles: lorries, tractor units, buses and special-purpose trucks; a pickup → Pickups.'

panel = find_kind(d1, 'Panel van'); window = find_kind(d1, 'Window van')
minibus = find_kind(d1, 'Minibus'); taxi = find_kind(d1, 'Taxi')
for k in (panel, window, minibus, taxi, find_kind(d1, 'Bus or coach')):
    drop_m(k)
for k in (panel, window, taxi):
    for e in k['x']:
        e['g'] = mkgroup(e.get('mk', ''))
        e.update({kk: vv for kk, vv in own_fields(e.get('mk', '')).items() if kk not in e})

# generation versions from fetched pages
for e in panel['x']:
    if e['n'] == 'Mercedes-Benz Sprinter':
        names = {norm(v['n']) for v in e['v']}
        e['v'] += [V('eSprinter 1.0', '2019–2023', 'battery-electric, front-wheel drive', 'Mercedes-Benz'),
                   V('eSprinter 2.0', '2023–', 'Electric Versatility Platform, rear motor', 'Mercedes-Benz'),
                   V('Sprinter Classic (Russia)', '2013–2020', 'first generation kept in Russia only', 'Mercedes-Benz')]
        e['s'] = U_SPR
        e['role'] = 'landmark' if False else e.get('role')
for e in window['x']:
    if e['n'] == 'Volkswagen Type 2':
        e['n'] = 'Volkswagen Transporter'
        e['a'] = 'Type 2 · VW Bus · Kombi · Vanagon · Eurovan · Caravelle · Multivan · T25'
        e['v'] = [V('T1', '1950–1967', 'derived from the Beetle (Type 1); also called Type 2', 'Volkswagen'),
                  V('T2', '1967–1979', 'air-cooled rear engine; Type 4 engine option from 1972', 'Volkswagen'),
                  V('T3', '1979–1992', 'T25 in the UK, Vanagon in the US; water-cooled from 1983, Syncro 4WD from January 1985; South African production to 2002', 'Volkswagen'),
                  V('T4', '1990–2003', 'front-engine, front-wheel drive, water-cooled; Eurovan in North America', 'Volkswagen'),
                  V('T5', '2003–2015', 'facelift late 2009 added common-rail diesels and 7-speed DSG; not sold in the US or Canada', 'Volkswagen'),
                  V('T6 / T6.1', '2015–2024', 'based on the T5; T6.1 refresh 2019', 'Volkswagen'),
                  V('T7 Multivan', '2021–', 'MQB platform minivan; replaces the Caravelle', 'Volkswagen'),
                  V('T7 Transporter', '2024–', 'panel van and chassis cab based on the Ford Transit Custom, built in Turkey', 'Volkswagen')]
        e['s'] = U_VW
        e['role'] = 'origin'
        e['d'] = 'Volkswagen\'s van line from the 1950 T1, derived from the Beetle; the T7 Transporter of 2024 is based on the Ford Transit Custom.'

def van_entry(row):
    t, mk, name, cls, yrs = row.split('|')
    nm = name if name.lower().startswith(mk.lower()) else f'{mk} {name}'
    y = ''
    if yrs:
        y = yrs.replace('present', '').strip()
        if 'present' in yrs: y = y.rstrip('–') + '–'
        y = y.lstrip('–') if y.startswith('–') and False else y
    d = ''
    if cls and yrs: d = f'{cls[0].upper()+cls[1:]}, {yrs.replace("present","to present")}.'
    elif cls: d = f'{cls[0].upper()+cls[1:]}.'
    return E(nm, mk=mk, y=y, d=d, s=U_VANS, g=mkgroup(mk), **own_fields(mk))

n_new = {'P': 0, 'W': 0}
for row in open(W + 'raw_vans.txt', encoding='utf-8').read().strip().split('\n'):
    e = van_entry(row)
    k = panel if row[0] == 'P' else window
    if add(k, e): n_new[row[0]] += 1

# vans listed by name in the existing set under different spelling
minibus.setdefault('x', [])
add(minibus, E('Toyota Coaster', mk='Toyota', y='', d='Minibus in the Toyota van list on Wikipedia.', s=U_VANS, g='Toyota', **own_fields('Toyota')))
mb = [e for e in minibus['x']]
minibus['nl'] = 'One entry is a minibus model line sold under its own name; vans sold with a minibus seating plan stay under their van line.'
minibus['sel'] = 'Wikipedia\'s List of vans names the Toyota Coaster as the one minibus; other minibuses are seating plans of the vans (Transit, Sprinter, Trafic) in Panel van and Window van. Complete: 1 of 1 minibus in List of vans.'
minibus['xg'] = 'by marque'

taxi.setdefault('x', [])
for k, nl in ((panel, 'One entry is a van model line (cargo, panel or combined cargo-and-passenger van) sold under its own name, with a generation or electric version as a version; kei and micro vans are included, minivans and MPVs are not.'),
              (window, 'One entry is a van model line built mainly to seat passengers, with its generations as versions; minivans and MPVs belong to Cars.')):
    k['nl'] = nl
taxi['nl'] = 'One entry is a purpose-built taxi model; generations and colour or body variants are versions.'
taxi['sel'] = 'Kept from the structure pass (Wikipedia pages of each cab); Wikipedia\'s List of vans names no taxis, so no further taxis were added. Covers 2 of the 2 purpose-built taxis found in the reference pages used.'
taxi['xg'] = 'by marque'

bus = find_kind(d1, 'Bus or coach')
add(bus, E('Bedford OB', mk='Bedford', y='1939–1951', d='Bedford coach chassis restarted in 1945 at Dunstable; about 180 survive and nearly 70 are roadworthy.', s=U_OB,
           v=[V('Duple Vista coachwork', '', 'Duple co-developed the Vista body, which became its standard OB body', 'Duple'),
              V('Wartime OWB', '1942–1945', 'bodied by Charles H. Roe, Mulliners and Scottish Motor Traction', '')], g='Bedford', role='landmark', dt='coachbuilder · seats · operator livery'))
for e in bus['x']:
    e['g'] = mkgroup(e.get('mk', ''))
bus['nl'] = 'One entry is a bus or coach model line that preserved-vehicle owners buy and run; body variants are versions.'
bus['sel'] = 'The two preserved British buses of the structure pass plus the Bedford OB (Wikipedia, Bedford OB). Wikipedia has no general list of bus models, so the canon is limited to buses a private owner can preserve; Covers 3 entries; Wikipedia has no whole-space bus-model list to count against.'
bus['xg'] = 'by maker'

# trucks: scope cut
rt = find_kind(d1, 'Rigid truck'); tu = find_kind(d1, 'Tractor unit')
for k in (rt, tu): drop_m(k)

# ---- pickups shelf
raw = [l.split('|') for l in open(W + 'raw_pickups.txt', encoding='utf-8').read().strip().split('\n')]
pk = {}   # entry key -> entry
order_pk = []
FOLD = {  # (marque,name) -> (entry name, version text)
}
def pk_entry(status, mk, name, cls, info):
    cls_l = cls[0].lower() + cls[1:] if cls and cls != 'unspecified' else ''
    if status == 'C':
        d = f'{cls_l[0].upper()+cls_l[1:] if cls_l else "Pickup"} pickup in production at the time of the list (February 2026); sold in {info}.' if info and info != 'not listed' else f'{cls_l.capitalize() if cls_l else "Pickup"} pickup in production at the time of the list (February 2026).'
        y = ''
    else:
        d = f'{cls_l.capitalize()} pickup, {info}.' if cls_l and info else (f'Pickup, {info}.' if info else 'Pickup; years not listed.')
        y = info
    nm = name if name.lower().startswith(mk.lower().split()[0].lower()) else f'{mk} {name}'
    return nm, E(nm, mk=mk, y=y, d=d, s=U_PICK, g=mkgroup(mk), **own_fields(mk))

for st, mk, name, cls, info in raw:
    if mk == 'International' and name.startswith('Harvester '):
        key = 'International Harvester pickups'
        if key not in pk:
            pk[key] = E(key, mk='International Harvester', y='1940–1975', d='International Harvester pickup series from the K and KB Series of 1940 to the D-Series of 1975.', s=U_PICK, g='International')
            order_pk.append(key)
        pk[key]['v'].append(V(name.replace('Harvester ', ''), info, cls if cls != 'unspecified' else '', 'International Harvester'))
        continue
    nm, e = pk_entry(st, mk, name, cls, info)
    if nm in pk:  # duplicate rows (e.g. Cenntro)
        continue
    pk[nm] = e; order_pk.append(nm)

def addv(key, *vs):
    pk[key]['v'] += [V(*v) for v in vs]

pk['Ford F-Series']['n'] = 'Ford F-Series'
pk['Ford F-Series']['a'] = 'F-150 · F-250 · F-350 · Super Duty'
pk['Ford F-Series']['y'] = '1948–'
pk['Ford F-Series']['y'] = ''
pk['Ford F-Series']['d'] = 'Ford\'s full-size pickup line, listed from F-150 to F-750; the F-150 is called the best-selling vehicle in the US since 1982.'
pk['Ford F-Series']['role'] = 'landmark'
pk['Ford F-Series']['s'] = U_PU
addv('Ford F-Series', ('F-150', '', 'luxury or full-size light pickup', 'Ford'), ('F-150 Raptor', '', 'off-road full-size', 'Ford'), ('F-150 Lightning', '2022–2025', 'electric', 'Ford'),
     ('F-250', '', 'heavy-duty', 'Ford'), ('F-350', '', 'heavy-duty', 'Ford'), ('F-450', '', 'heavy-duty', 'Ford'), ('F-550', '', 'heavy-duty', 'Ford'), ('F-650', '', 'heavy-duty', 'Ford'), ('F-750', '', 'heavy-duty', 'Ford'))
addv('Chevrolet Silverado', ('Silverado 1500', '', 'luxury or full-size', 'Chevrolet'), ('Silverado 1500 Hybrid', '', '', 'Chevrolet'), ('Silverado 2500 HD', '', 'heavy-duty', 'Chevrolet'),
     ('Silverado 3500 HD', '', 'heavy-duty', 'Chevrolet'), ('Silverado EV', '', 'electric', 'Chevrolet'))
addv('GMC Sierra', ('Sierra 1500', '', '', 'GMC'), ('Sierra 2500', '', 'heavy-duty', 'GMC'), ('Sierra 3500', '', 'heavy-duty', 'GMC'), ('Sierra Hybrid', '', '', 'GMC'))
pk['Ram Pickup']['a'] = 'Ram 1500 · Ram 2500 · Ram 3500 · Power Wagon'
addv('Ram Pickup', ('Ram 1500', '', 'full-size', 'Ram'), ('Ram 1500 Laramie Limited', '', 'luxury', 'Ram'), ('Ram 1500 Rebel', '', 'off-road', 'Ram'), ('Ram 2500', '', 'heavy-duty', 'Ram'),
     ('Ram 3500', '', 'heavy-duty', 'Ram'), ('Ram 4500', '', 'heavy-duty', 'Ram'), ('Ram 5500', '', 'heavy-duty', 'Ram'), ('Power Wagon', '', 'heavy-duty', 'Ram'))
addv('Great Wall Wingle', ('Wingle 3', '2006–2010', 'full-size', 'Great Wall'), ('Wingle 5', '2010–2021', 'full-size', 'Great Wall'), ('Wingle 6', '2010–2021', 'full-size', 'Great Wall'), ('Wingle 7', '', 'mid-size, in production', 'Great Wall'))
addv('Toyota Hilux', ('Hilux Champ', '', 'mid-size, Asia and South America', 'Toyota'))
addv('Nissan Frontier', ('Frontier Pro', '', 'mid-size, China', 'Nissan'))
pk['Toyota Hilux']['a'] = 'Hilux'
# Gladiator appears twice (2020s and 1962) – keep both, the old one by its own key
for nm in order_pk[:]:
    pass
pk['Ford Ranger']['a'] = 'Ranger'
pk['Ford North American Ranger']['d'] = 'Compact pickup, 1983–2012, not counting the 2019 reintroduction.'
pk['Ford North American Ranger']['y'] = '1983–2012'

# roles from fetched pages
for key, why in (('Ford Model T Pickup', None),):
    pass

# Land Cruiser 79 and Defender pickup keep specific makers
pk['Toyota Land Cruiser 79']['d'] = 'Off-road full-size pickup sold in Australia, New Zealand, Africa, Central America, the Caribbean and the Middle East.'

pickup_k = {
    'n': 'Utility pickup',
    'a': 'ute · pickup truck · bakkie · coupe utility',
    'd': 'Road vehicle with an open load bed behind the cab, from kei trucks to heavy-duty work pickups; a pickup used as an everyday car → Cars.',
    's': U_PICK,
    'x': [pk[n] for n in order_pk],
    'tt': [['Cab', ['Single cab', 'Extended cab', 'Crew cab']], ['Class', ['Mini', 'Compact', 'Mid-size', 'Full-size', 'Heavy-duty']], ['Drive', ['Two-wheel drive', 'Four-wheel drive']], ['Power', ['Petrol', 'Diesel', 'Hybrid', 'Battery electric']]],
    'see': [['G1', 'Pickup truck', 'the same vehicles as an everyday car']],
    'nl': 'One entry is a pickup model line sold under its own name; weight ratings (F-150, F-250), trims and electric editions are versions of the line, and a regional rebadge is an alias.',
    'sel': ('Every pickup in Wikipedia\'s List of pickup trucks (current-production table, custom and conversion builders, and the discontinued table), read in two windows to the end of the page text (characters 0-173,911); '
            'concept vehicles listed at the end of that page are out of scope, and the same marque\'s weight ratings are folded into one line. '),
    'xg': 'by marque, then first year',
}
pickup_k['sel'] += f'Complete: {len(order_pk)} entries from {len(raw) + 0} table rows (production and discontinued) in List of pickup trucks.'
shelf_pick = {'n': 'Pickups', 't': 'Open-bed pickups and utes of every size, from kei trucks to heavy-duty work pickups; a pickup bought as an everyday car → Cars.',
              'k': [pickup_k]}
d1['s'].insert(1, shelf_pick)
d1['ax'] = 'Does the vehicle carry a load, passengers or a special job, and on what chassis?'
d1['ms'] = [
    {'mkt': 'US vehicle sales', 'who': 'Ford F-150', 'share': 'best-selling vehicle since 1982', 'yr': 1982, 's': U_PU, 'note': 'no unit count on the page'},
    {'mkt': 'European light vehicles', 'who': 'Ford Ranger', 'share': '27,300 units', 'yr': 2015, 's': U_PU, 'note': 'most popular pickup in Europe; all pickups under 1 % of light vehicles sold'},
    {'mkt': 'China pickups', 'who': 'Chinese pickups led by the Great Wall Wingle', 'share': '378,000 units, up 48 %', 'yr': 2010, 's': U_PU, 'note': 'from the page\'s ChinaAutoWeb reference'},
]
d1['ms'] = [m for m in d1['ms']]
for m in d1['ms']:
    if m['yr'] == 0: m['yr'] = None
d1['msum'] = 'Pickup sales are shown by market from the Wikipedia pickup article; the page gives no group shares for vans or buses.'

for k in (panel, window):
    pass
order_vans = sorted({e['g'] for e in panel['x']})
for k in (panel, window, taxi):
    k['xg'] = 'by marque, then first year'
    sort_kind(k, [])
panel['sel'] = ('Every cargo, panel and combined cargo-and-passenger van in Wikipedia\'s List of vans (the table through Honda and the bulleted list from Hyundai to Volkswagen), '
                'plus the structure-pass entries; the page is dated 2013, so later vans are missing. Passenger-only vans are in Window van; minivans and MPVs (Chrysler Pacifica, Honda Odyssey, Toyota Sienna and the like) are left to Cars. Covers '+str(len(panel['x']))+' cargo and combined vans of about 350 rows on the page (table of about 160 rows plus about 190 list items); the other rows are minivans, MPVs and passenger vans (Window van).')
window['sel'] = 'Passenger vans in Wikipedia\'s List of vans plus the structure-pass entries; vans sold as both cargo and passenger are under Panel van. Minivans and MPVs are left to Cars. Covers '+str(len(window['x']))+' passenger vans.'

# ================================================================ DEPT 2: caravans
d2 = dept['Caravans, motorhomes & trailers']
touring = find_kind(d2, 'Touring caravan'); fifth = find_kind(d2, 'Fifth-wheel caravan'); tear = find_kind(d2, 'Teardrop trailer')
fold = find_kind(d2, 'Folding camper'); toy = find_kind(d2, 'Toy hauler'); offr = find_kind(d2, 'Off-road camper trailer')
camper = find_kind(d2, 'Campervan'); truckc = find_kind(d2, 'Truck camper'); lowp = find_kind(d2, 'Low-profile motorhome')
over = find_kind(d2, 'Overcab motorhome'); acl = find_kind(d2, 'A-class motorhome'); expd = find_kind(d2, 'Expedition vehicle')
util = find_kind(d2, 'Utility trailer'); horsebox = find_kind(d2, 'Horsebox')
for k in (touring, fifth, tear, fold, toy, offr, camper, truckc, lowp, over, acl, expd, util, horsebox): drop_m(k)

THOR = ('Thor Industries', 'Global group', None)
def rv(n, grp, own, tier, cty, own_y=None, **kw):
    return E(n, own=own, tier=tier, cty=cty, own_y=own_y, g=grp, **kw)

# group labels = owner group
G_THOR, G_HYM, G_KT, G_SW, G_WIN, G_IND = 'Thor Industries', 'Erwin Hymer Group brands (Thor)', 'Knaus Tabbert', 'Swift Group', 'Winnebago Industries', 'Independent makers'
# existing entries: set group/owners
setg = {'Airstream Clipper': (G_THOR, 'Thor Industries', 'Global group', 'United States', '1980'), 'Airstream Flying Cloud': (G_THOR, 'Thor Industries', 'Global group', 'United States', '1980'),
        'Airstream Bambi': (G_THOR, 'Thor Industries', 'Global group', 'United States', '1980'),
        'Eriba Touring': (G_HYM, 'Thor Industries', 'Global group', 'Germany', '2019'), 'Sprite': (G_SW, 'Swift Group', 'Independent', 'United Kingdom', None),
        'Shasta Airflyte': ('Forest River', 'Forest River RV', 'Global group', 'United States', None), 'Boler': (G_IND, None, 'Craft & indie', 'Canada', None),
        'Bailey Pageant': (G_IND, 'Bailey of Bristol', 'Independent', 'United Kingdom', None), 'Adria Adora': (G_IND, 'Adria Mobil', 'Independent', 'Slovenia', None),
        'nuCamp T@B': (G_IND, 'nuCamp RV', 'Independent', 'United States', None), 'Classic plywood teardrop': (G_IND, None, None, None, None),
        'Jayco fold-down camper': (G_THOR, 'Thor Industries', 'Global group', 'United States', '2016'),
        'Conqueror UEV-440': (G_IND, 'Conqueror', 'Craft & indie', None, None), 'Patriot X1': (G_IND, 'Patriot Campers', 'Craft & indie', 'Australia', None),
        'Volkswagen Westfalia Camper': ('Volkswagen Group', 'Volkswagen Group', 'Global group', 'Germany', None), 'Volkswagen California': ('Volkswagen Group', 'Volkswagen Group', 'Global group', 'Germany', None),
        'Mercedes-Benz Marco Polo': ('Mercedes-Benz Group', 'Mercedes-Benz Group', 'Global group', 'Germany', None), 'Bedford Dormobile': (G_IND, None, None, 'United Kingdom', None),
        'Four Wheel Campers pop-up': (G_IND, 'Four Wheel Campers', 'Independent', 'United States', None), 'Lance hard-side camper': (G_IND, 'Lance', 'Independent', 'United States', None),
        'GMC Motorhome': (G_IND, None, None, 'United States', None), 'Winnebago Brave': (G_WIN, 'Winnebago Industries', 'National champion', 'United States', None),
        'Blue Bird Wanderlodge': (G_IND, 'Blue Bird', 'Independent', 'United States', None), 'Hymer B-Klasse': (G_HYM, 'Thor Industries', 'Global group', 'Germany', '2019'),
        'Unimog expedition camper': ('Mercedes-Benz Group', 'Mercedes-Benz Group', 'Global group', 'Germany', None), 'EarthRoamer': (G_IND, 'EarthRoamer', 'Craft & indie', 'United States', None)}
for k in (touring, fifth, tear, fold, toy, offr, camper, truckc, lowp, over, acl, expd):
    for e in k.get('x', []):
        g, own, tier, cty, oy = setg.get(e['n'], (G_IND, None, None, None, None))
        e['g'] = g
        if own: e['own'] = own
        if tier: e['tier'] = tier
        if cty: e['cty'] = cty
        if oy: e['own_y'] = oy

def thor(n, k, mk, y, d, s, grp=G_THOR, oy='', **kw):
    return add(k, E(n, mk=mk, y=y, d=d, s=s, g=grp, own='Thor Industries', tier='Global group', cty='United States', own_y=oy or None, **kw))

# --- Airstream (Thor 1980)
thor('Airstream Argosy', touring, 'Airstream', '1972–1979', 'Painted travel trailer built at Versailles, Ohio; a rectangular version followed in 1986–1988. Airstream also used the name for a motorhome from 1974.', U_AIR, oy='1980')
thor('Airstream Land Yacht', touring, 'Airstream', '', 'Rectangular Airstream travel trailers; years not stated on the page.', U_AIR, oy='1980')
thor('Airstream International', touring, 'Airstream', '', 'Travel trailers (534, 604, 684 and 25) built for Europe and the UK.', U_AIR, oy='1980')
thor('Airstream Tradewind', touring, 'Airstream', '1961', 'Travel trailer; the page shows a 1962 example custom-ordered in 1961.', U_AIR, oy='1980')
thor('Airstream Nest', touring, 'Airstream', '2016–2020', 'Moulded fibreglass trailer, acquired from Nest Caravans in 2016 and withdrawn in September 2020.', U_AIR, oy='1980')
add(acl, E('Airstream Argosy motorhome', mk='Airstream', y='1974', d='Class A motorhome from 1974 sharing the Argosy name with the painted trailer.', s=U_AIR, g=G_THOR, own='Thor Industries', tier='Global group', cty='United States', own_y='1980'))
add(acl, E('Airstream Classic', mk='Airstream', y='1979', d='Class A motorhome with an unpainted aluminium body.', s=U_AIR, g=G_THOR, own='Thor Industries', tier='Global group', cty='United States', own_y='1980'))
add(acl, E('Airstream Excella', mk='Airstream', y='1983', d='Motorhome of 1983, modified as the Astrovan from 1984.', s=U_AIR, g=G_THOR, own='Thor Industries', tier='Global group', cty='United States', own_y='1980'))

# --- other Thor brands (Thor Industries article)
tb = [
 (touring, 'Heartland BigHorn', 'Heartland', 'Fifth-wheel and travel-trailer line of the Heartland brand, acquired 2010.', '2010'),
 (touring, 'Heartland Sundance', 'Heartland', 'Towable line of the Heartland brand, acquired 2010.', '2010'),
 (touring, 'Heartland Cyclone', 'Heartland', 'Towable line of the Heartland brand, acquired 2010.', '2010'),
 (touring, 'Dutchmen Aerolite', 'Dutchmen', 'Towable line of the Dutchmen brand, acquired 1991.', '1991'),
 (touring, 'Dutchmen Coleman', 'Dutchmen', 'Towable line of the Dutchmen brand, acquired 1991.', '1991'),
 (touring, 'Dutchmen Denali', 'Dutchmen', 'Towable line of the Dutchmen brand, acquired 1991.', '1991'),
 (touring, 'Dutchmen Kodiak', 'Dutchmen', 'Towable line of the Dutchmen brand, acquired 1991.', '1991'),
 (touring, 'Dutchmen Aspen Trail', 'Dutchmen', 'Towable line of the Dutchmen brand, acquired 1991.', '1991'),
 (touring, 'Keystone Cougar', 'Keystone RV', 'Towable line of Keystone, acquired 2001.', '2001'),
 (touring, 'Keystone Laredo', 'Keystone RV', 'Towable line of Keystone, acquired 2001.', '2001'),
 (touring, 'Keystone Passport', 'Keystone RV', 'Towable line of Keystone, acquired 2001.', '2001'),
 (touring, 'Keystone Sprinter', 'Keystone RV', 'Towable line of Keystone, acquired 2001.', '2001'),
 (fifth, 'Keystone Montana', 'Keystone RV', 'Fifth-wheel line of Keystone, acquired 2001.', '2001'),
 (fifth, 'DRV', 'DRV', 'Luxury fifth-wheel maker, acquired 2015.', '2015'),
 (touring, 'K-Z', 'K-Z Inc.', 'Travel-trailer maker, acquired 2014.', '2014'),
 (touring, 'CrossRoads RV', 'CrossRoads RV', 'Towable maker acquired 2004; Redwood RV is its subsidiary.', '2004'),
 (touring, 'Komfort', 'Komfort', 'Travel-trailer maker, acquired 1995.', '1995'),
 (touring, 'Starcraft RV', 'Jayco', 'Fold-down camping-trailer brand, a Jayco subsidiary acquired with Jayco in 2016.', '2016'),
 (touring, 'Highland Ridge', 'Jayco', 'Towable brand, a Jayco subsidiary acquired in 2016.', '2016'),
 (touring, 'Livin\' Lite RV', 'Livin\' Lite RV', 'RV maker acquired 2013.', '2013'),
 (fold, 'Skamper', 'Skamper', 'Folding travel-trailer brand, acquired 1995.', '1995'),
 (acl, 'Thor Motor Coach', 'Thor Motor Coach', 'Thor\'s motorhome brand, consolidated in 2010; formerly Damon Motor Coach and Four Winds International.', '2010'),
 (acl, 'Four Winds International', 'Four Winds International', 'Motorhome maker, acquired 1992.', '1992'),
 (acl, 'Damon Motor Coach', 'Damon', 'Motorhome maker, acquired 2003; Breckenridge park trailers are its subsidiary.', '2003'),
 (acl, 'Entegra Coach', 'Jayco', 'Motorhome brand, a Jayco subsidiary acquired in 2016.', '2016'),
 (acl, 'Tuscany', 'Thor Industries', 'Luxury motorhomes; the RV list describes it as building only diesel pushers in the US and Canada.', ''),
 (acl, 'Tiffin Motorhomes', 'Tiffin Motorhomes', 'Luxury motorhome maker, acquired by Thor in 2020.', '2020'),
]
for k, n, mk, d, oy in tb:
    src_u = U_RVM if n == 'Tuscany' else U_THOR
    thor(n, k, mk, '', d, src_u, oy=oy)
# Thor knows camper vans: Bison Coach horse trailers, ignore.

# --- Winnebago (Winnebago article)
def win(k, n, y, d, oy=None, role=None):
    add(k, E(n, mk='Winnebago', y=y, d=d, s=U_WIN, g=G_WIN, own='Winnebago Industries', tier='National champion', cty='United States', own_y=oy, role=role))
win(over, 'Winnebago Minnie Winnie', '1973–', 'Motorhome on a Dodge chassis, then Chevrolet or Ford after 1980; still sold in the 21st century.')
win(camper, 'Winnebago Winnie Wagon', '', 'Small low-profile pop-top motorhome; years not stated on the page.')
win(camper, 'Winnebago LeSharo', '', 'Small campervan on the Renault Trafic, sold in the 1980s and 1990s.')
win(camper, 'Winnebago Rialta', '', 'Campervan on the Volkswagen T4, sold in the 1980s and 1990s.')
win(acl, 'Winnebago Elanté', '', 'Motorhome model used in a 2002 German campaign.')
win(acl, 'Winnebago Heli-Home', '1970s', 'Helicopter-based RV from the late 1970s on a Sikorsky S-58 with Orlando Helicopter Airways; six or seven built on the S-55.', role='origin')
add(acl, E('Newmar', mk='Newmar', y='', d='Luxury RV maker bought by Winnebago Industries in 2019.', s=U_WIN, g=G_WIN, own='Winnebago Industries', tier='National champion', cty='United States', own_y='2019'))
add(toy, E('Grand Design', mk='Grand Design', y='', d='RV maker that is a Winnebago Industries subsidiary; the page gives no purchase year.', s=U_WIN, g=G_WIN, own='Winnebago Industries', tier='National champion', cty='United States'))
for e in toy.get('x', []): pass

# --- Hymer group (Hymer article)
def hym(k, n, mk, y, d, a='', oy='2019', cty='Germany', role=None, s=U_HYM, v=None):
    add(k, E(n, mk=mk, y=y, d=d, s=s, a=a, g=G_HYM, own='Thor Industries', tier='Global group', cty=cty, own_y=oy, role=role, v=v))
hym(acl, 'Hymer Caravano', 'Hymer', '1961', 'Hymer\'s first motorhome.', role='origin')
hym(acl, 'Hymer Exsis', 'Hymer', '', 'Hymer motorhome model; years not stated.')
hym(camper, 'Roadtrek', 'Roadtrek', '', 'Class B campervans; acquired by Hymer in 2016 and sold to the Rapido Group in 2019.', cty='Canada', oy='')
hym(touring, 'Dethleffs Wohnauto', 'Dethleffs', '1931', 'Early caravan of Dethleffs; a replica was built in 1974.', oy='2019')
hym(touring, 'Bürstner', 'Bürstner', '', 'Caravan and motorhome brand acquired by Hymer in 1998.', oy='1998')
hym(touring, 'Carado', 'Carado', '', 'Caravan brand distributed through Capron Ltd. with Dethleffs in 2005-2006.')
hym(touring, 'Sunlight', 'Sunlight', '', 'Caravan brand distributed through Capron Ltd. in 2005-2006.')
hym(touring, 'Elddis', 'Elddis', '', 'UK caravan brand of the Explorer Group, acquired by Hymer in February 2017.', cty='United Kingdom', oy='2017')
hym(touring, 'Buccaneer', 'Buccaneer', '', 'UK caravan brand of the Explorer Group, acquired in February 2017.', cty='United Kingdom', oy='2017')
hym(touring, 'Compass', 'Compass', '', 'UK caravan brand of the Explorer Group, acquired in February 2017.', cty='United Kingdom', oy='2017')
hym(touring, 'Xplore', 'Xplore', '', 'UK caravan brand of the Explorer Group, acquired in February 2017.', cty='United Kingdom', oy='2017')
hym(acl, 'Laika', 'Laika', '', 'Italian motorhome brand acquired by Hymer in 2000.', cty='Italy', oy='2000')
hym(acl, 'Niesmann + Bischoff', 'Niesmann+Bischoff', '', 'Motorhome brand acquired by Hymer in 1996.', oy='1996')
hym(acl, 'LMC', 'LMC', '', 'Motorhome brand in the Hymer group; no years given.')
hym(touring, 'Etrusco', 'Etrusco', '', 'Brand in the Hymer group; no years given.')

# --- Swift (Swift Leisure article)
def sw(k, n, y, d, role=None):
    add(k, E(n, mk='Swift Group', y=y, d=d, s=U_SWIFT, g=G_SW, own='Swift Group', tier='Independent', cty='United Kingdom', role=role))
sw(touring, 'Swift caravans', '1964–', 'Swift\'s caravans, founded in 1964 and known for the tri-front window design.')
sw(touring, 'Abbey', '', 'Caravan brand acquired by Swift in 1992; a group list gives caravans until 2008.')
sw(touring, 'Bessacarr caravans', '', 'Caravan brand acquired in 1996; the group list gives it until 2006.')
sw(touring, 'Sterling', '1995–', 'Name given to Sprite Leisure in 1995.')
sw(touring, 'Ace caravans', '2001–2008', 'Caravan brand acquired in 2001 and dropped in 2008.')
sw(acl, 'Swift Kon-Tiki', '1986', 'Named motorhome launched with Swift Motorhomes in 1986.')
sw(acl, 'Bessacarr motorhomes', '1997–', 'Motorhome line launched in 1997.')
sw(acl, 'Ace motorhomes', '2001–2008', 'Motorhome line launched in 2001 and dropped in 2008.')
sw(acl, 'Autocruise', '', 'Motorhome brand acquired in 2008 (timeline) or 2007 (group list).')
sw(acl, 'Swift Escape', '', 'Swift motorhome line; no years given.')
sw(acl, 'Swift Mondial', '', 'Swift motorhome line; no years given.')

# --- Knaus Tabbert (press release)
def kt(k, n, mk, y, d, role=None, a=''):
    add(k, E(n, mk=mk, y=y, d=d, s=U_KNAUS, a=a, g=G_KT, own='Knaus Tabbert', tier='Independent', cty='Germany', role=role))
kt(touring, 'Knaus Schwalbennest', 'Knaus', '1961', 'First Knaus caravan, built for the VW Beetle.')
kt(touring, 'Knaus Südwind', 'Knaus', '1962', 'Knaus caravan model since 1962; a 60 Years Knaus edition exists.')
kt(touring, 'Knaus Deseo', 'Knaus', '', 'Variable caravan with a full-LED rear after its facelift.')
kt(touring, 'Knaus Travelino', 'Knaus', '2016', 'First ultra-lightweight caravan with fibre-frame technology.', role='origin')
kt(touring, 'Tabbert Rossini', 'Tabbert', '', 'Entry model of Tabbert\'s premium range; a Finest Edition adds equipment.')
kt(touring, 'Tabbert Da Vinci', 'Tabbert', '', 'Upper-middle-class Tabbert with a lighter 48 mm GRP roof.')
for n in ('Vivaldi', 'Puccini', 'Bottesini', 'Bellini', 'Bellissimo', 'Cellini Slide-Out'):
    kt(touring, f'Tabbert {n}', 'Tabbert', '', f'Tabbert caravan updated for 2021 (press release).')
kt(touring, 'Weinsberg CaraCito', 'Weinsberg', '', 'First Weinsberg caravan without gas cylinders; priced from 10,990 euros in the press release.')
kt(tear, 'Knaus Tabbert T@B', 'T@B', '', 'Teardrop caravan with retro styling in the styles Basic, Mexican Sunset, Metropolis and Offroad.')
kt(camper, 'Knaus Boxstar', 'Knaus', '', 'Camping-van (CUV) line with panorama roof window or pop-up roof options.')
kt(camper, 'Knaus Boxdrive', 'Knaus', '', 'Camping van on the MAN TGE chassis.')
kt(camper, 'Knaus Boxlife', 'Knaus', '', 'Camping van with panorama window and pop-up roof options.')
kt(camper, 'Weinsberg CaraBus', 'Weinsberg', '', 'Camping van with panorama window option.')
kt(camper, 'Weinsberg CaraTour', 'Weinsberg', '', 'Camping van with a light silver-grey interior.')
kt(lowp, 'Knaus Sky TI', 'Knaus', '', 'Partially integrated motorhome; the best-selling of its type in Germany according to the press release.')
kt(lowp, 'Knaus Van TI', 'Knaus', '', 'Semi-integrated motorhome on the Fiat Ducato; a Van TI Plus is built on the MAN TGE.')
kt(lowp, 'Weinsberg CaraLoft', 'Weinsberg', '', 'Semi-integrated motorhome with LFI roof hood.')
kt(lowp, 'Weinsberg CaraSuite', 'Weinsberg', '', 'Semi-integrated motorhome with LFI roof hood.')
kt(lowp, 'Weinsberg CaraHome', 'Weinsberg', '', 'Motorhome on the Fiat Ducato with an optional stepless-opening rear window.')
kt(acl, 'Knaus Traveller', 'Knaus', '1988', 'First Knaus motorhome; it won the Motorhome of the Year title.')
kt(acl, 'Knaus Sky I', 'Knaus', '2012', 'Integrated motorhome introduced in 2012.')
kt(acl, 'Knaus Sun I', 'Knaus', '', 'Luxury liner with a redesigned front for 2021; three axles on the 900 LEG and 900 LX layouts.')
kt(acl, 'Knaus L!VE I', 'Knaus', '', 'Entry-level L!VE series motorhome.')
kt(acl, 'Knaus Van I', 'Knaus', '', 'Integrated van motorhome; a Platinum Selection exists.')
kt(acl, 'Knaus Sky Wave', 'Knaus', '', 'Family motorhome for up to six berths.')
kt(acl, 'Knaus L!VE Wave', 'Knaus', '', 'Part of the L!VE series; interior refreshed for 2021.')
kt(acl, 'Knaus L!VE TI', 'Knaus', '', 'Part of the L!VE series; interior refreshed for 2021.')

# --- RV list makers (List of recreational vehicle manufacturers)
def rvm(k, n, cty, d, grp=G_IND, own=None, tier='Independent', oy=None, y=''):
    add(k, E(n, mk=n, y=y, d=d, s=U_RVM, g=grp, own=own or n, tier=tier, cty=cty, own_y=oy))
rvm(touring, 'Casita', 'United States', 'RV maker in Texas.')
rvm(touring, 'Coachman Caravans', 'United Kingdom', 'UK caravan maker.')
rvm(touring, 'Fendt Caravan', 'Germany', 'German caravan maker.')
rvm(touring, 'Jurgens Ci Caravans', 'South Africa', 'South African caravan maker.')
rvm(touring, 'Boles Aero', 'United States', 'Defunct California maker of travel trailers, 1946-1980.', y='1946–1980')
rvm(touring, 'Cortes Molded Fiberglass Trailer', 'United States', 'Defunct Ohio maker of moulded fibreglass trailers.', tier='Craft & indie')
rvm(touring, 'Caravans International', 'United Kingdom', 'Defunct British maker formed by Sam Alper; its assets were sold to Cosalt.')
rvm(touring, 'Cosalt', 'United Kingdom', 'Bought the collapsed Caravans International; sold its touring-caravan assets to Swift Leisure.')
rvm(touring, 'Giottiline', 'Italy', 'Italian RV maker.')
rvm(touring, 'SEA Group', 'Italy', 'Italian RV maker.')
rvm(touring, 'Tonke', 'Netherlands', 'Dutch RV maker.')
rvm(touring, 'Toppola', 'Sweden', 'Swedish RV maker.')
rvm(touring, 'Caraboat', 'Australia', 'Australian maker in New South Wales.')
rvm(touring, 'Zone RV', 'Australia', 'Australian RV maker.')
rvm(touring, 'Kimberley Kampers', 'United States', 'RV maker with operations in the United States and Australia.')
rvm(touring, 'Grand River RV', 'Canada', 'Ontario RV maker.')
rvm(touring, 'Triple E Recreational Vehicles', 'Canada', 'Manitoba RV maker.')
rvm(touring, 'Blue Mountain Camper Co.', 'United States', 'Builds tiny rot-free composite campers.', tier='Craft & indie')
rvm(touring, 'Vixen (RV)', 'United States', 'Michigan RV maker.')
rvm(touring, 'AEONrv', 'United States', 'Reno, Nevada RV maker.')
rvm(touring, 'Forest River RV', 'United States', 'Indiana RV maker owned by Berkshire Hathaway; the Shasta brand is a division.', grp='Forest River', tier='Global group')
rvm(fold, 'Aliner', 'United States', 'Original A-frame trailer manufacturer, privately owned.')
rvm(fifth, 'Spacecraft Manufacturing', 'United States', 'Builds the largest fifth-wheel trailers as full-size semi-trailers, 40 to 57 ft.')
rvm(camper, 'Auto-Sleepers', 'United Kingdom', 'UK motorhome and campervan maker.')
rvm(camper, 'Sportsmobile', 'United States', 'Indiana maker of van conversions.')
rvm(camper, 'Mini Wildgoose', 'United Kingdom', 'UK maker.')
rvm(camper, 'Holdsworth Motorhomes', 'United Kingdom', 'Defunct UK maker.')
rvm(camper, 'Martin Walter of Folkestone', 'United Kingdom', 'Made the Dormobile products.')
rvm(acl, 'Auto-Trail', 'United Kingdom', 'UK motorhome maker.')
rvm(acl, 'Travco', 'United States', 'Michigan maker of motorhomes.')
rvm(acl, 'Beaver Motorcoach Corporation', 'United States', 'Oregon motorcoach maker.')
rvm(acl, 'Safari Motorcoach Corporation', 'United States', 'Oregon motorcoach maker.')
rvm(acl, 'Safari Trek Motorhome', 'United States', 'Oregon motorhome maker.')
rvm(acl, 'Holiday Rambler', 'United States', 'Oregon motorhome maker, part of REV Group.', grp='REV Group', tier='Independent', own='REV Group')
rvm(acl, 'Monaco Coach Corporation', 'United States', 'Indiana motorhome maker, part of REV Group.', grp='REV Group', own='REV Group')
rvm(acl, 'Fleetwood Enterprises', 'United States', 'Californian maker merged into Allied Specialty Vehicles in 2010; part of REV Group.', grp='REV Group', own='REV Group', oy='2010')
rvm(acl, 'Gulfstream Coach', 'United States', 'Indiana motorhome maker.')
rvm(acl, 'Mauck Special Vehicles', 'United States', 'Ohio maker of special vehicles.')
rvm(acl, 'Millennium Luxury Coaches', 'United States', 'Florida coach converter.')
rvm(acl, 'Xplorer Motorhomes', 'United States', 'Indiana motorhome maker.')
add(acl, E('Tuscany Luxury Motorhomes', mk='Tuscany', y='', d='Thor subsidiary building only diesel pushers in the US and Canada.', s=U_RVM, g=G_THOR, own='Thor Industries', tier='Global group', cty='United States')) if False else None
rvm(acl, 'Adria Supersonic', 'Slovenia', 'Adria Mobil motorhome.') if False else None

# role badges (<= 1 in 5) from fetched pages
for e in acl['x']:
    if e['n'] in ('Winnebago Brave',): pass

# tidy: sort each kind by group order then year
GORD = [G_THOR, G_HYM, G_KT, G_SW, G_WIN, 'Forest River', 'REV Group', 'Volkswagen Group', 'Mercedes-Benz Group', G_IND]
for k in (touring, fifth, tear, fold, toy, offr, camper, truckc, lowp, over, acl, expd):
    if k.get('x'): sort_kind(k, GORD)

# kind texts
cov = [
 (touring, 'One entry is a touring caravan or travel-trailer model line, or the maker where the page names no line; sizes and layouts are versions.',
           'Model lines and makers named in the Thor Industries, Hymer, Swift Leisure, Airstream and Winnebago Wikipedia articles, the Knaus Tabbert press release and Wikipedia\'s List of recreational vehicle manufacturers, plus the structure-pass entries. Makers in the RV list without a stated line are maker entries. Covers all caravan-type rows of those pages; the list itself is non-exhaustive (about 60 names).'),
 (fifth, 'One entry is a fifth-wheel line or maker.', 'Fifth-wheel rows of the Thor Industries article and the RV manufacturers list. Complete for those two pages.'),
 (tear, 'One entry is a teardrop trailer model line or maker.', 'Teardrop rows of the Knaus Tabbert press release and the structure pass; Wikipedia\'s RV list has none. Covers 3 of 3 teardrop rows found.'),
 (fold, 'One entry is a folding camper maker or line.', 'Folding rows of the Thor Industries article (Skamper, Starcraft) and the RV list (Aliner), plus the structure pass. Covers all rows found.'),
 (toy, 'One entry is a toy-hauler line or maker.', 'Structure-pass entry plus Grand Design, the subsidiary Winnebago Industries named on its article. No toy-hauler list exists on Wikipedia; covers 1 of about 1.'),
 (offr, 'One entry is an off-road camper trailer model.', 'Structure-pass entries only; no list page covers them.'),
 (camper, 'One entry is a campervan (a van converted or built for living) model line or maker; fit-outs are versions.', 'Campervan rows of the Hymer, Winnebago, Knaus Tabbert and RV list pages plus the structure pass. Covers all rows on those pages.'),
 (truckc, 'One entry is a truck-camper model line.', 'Structure-pass entries only; none of the fetched pages names truck campers.'),
 (lowp, 'One entry is a semi-integrated (low-profile) motorhome line.', 'Knaus Tabbert press release (Sky TI, Van TI, Weinsberg CaraLoft, CaraSuite, CaraHome). Covers all semi-integrated rows on that page.'),
 (over, 'One entry is an alcove or Class C motorhome line.', 'Winnebago Minnie Winnie from the Winnebago Industries article. Covers 1 of the 1 Class C rows found.'),
 (acl, 'One entry is a coach-sized or integrated motorhome line, or the maker where the page names no line.', 'Motorhome rows of the Airstream, Winnebago, Hymer, Swift Leisure, Thor Industries and RV list pages and the Knaus Tabbert press release, plus the structure pass. Covers all motorhome rows on those pages.'),
 (expd, 'One entry is an expedition vehicle build.', 'Structure-pass entries only.'),
]
for k, nl, sel in cov:
    k['nl'] = nl
    n = len(k.get('x', []))
    k['sel'] = sel + f' Total {n} entries.'
    k['xg'] = 'by owner group, then first year'
util['nl'] = ''; horsebox['nl'] = ''
for k in (util, horsebox, expd, offr, truckc):
    if k is util or k is horsebox:
        k.pop('nl'); k.pop('sel', None)
util.pop('r', None)
util['r'] = util.get('r', [])
util.pop('r')
d2['ms'] = [
 {'mkt': 'US households', 'who': 'RV owners', 'share': '11.3 million households', 'yr': 2021, 's': U_RV, 'note': 'up 26 % over the prior ten years'},
 {'mkt': 'North American RV production', 'who': 'RV manufacturers', 'share': '58,000 units in one month', 'yr': 2021, 's': U_RV, 'note': 'October 2021, highest single-month total on record'},
 {'mkt': 'US RV shipments to dealers', 'who': 'RV manufacturers', 'share': 'down 4 %', 'yr': 2018, 's': U_RV, 'note': 'followed by a 22 % fall in the first five months of 2019'},
 {'mkt': 'US RV sales', 'who': 'Indiana-built RVs', 'share': 'about 85 %', 'yr': 2019, 's': U_RV, 'note': 'Reuters figure cited by the page; Elkhart County is about two-thirds of Indiana output'},
 {'mkt': 'US RV owners', 'who': 'Average owner age', 'share': '45 years', 'yr': 2016, 's': U_RV, 'note': 'three years younger than in 2015'},
]
d2['msum'] = 'RV market figures are from the Wikipedia article on recreational vehicles; the page gives no maker shares, so owner groups come from each maker\'s own article.'
for k in (util, horsebox): pass

# ================================================================ DEPT 3: off-road
d3 = dept['Off-road & leisure vehicles']
quad = find_kind(d3, 'Quad bike'); sxs = find_kind(d3, 'Side-by-side'); dune = find_kind(d3, 'Dune buggy'); snow = find_kind(d3, 'Snowmobile')
amph = find_kind(d3, 'Amphibious vehicle'); golf = find_kind(d3, 'Golf cart'); kart = find_kind(d3, 'Go-kart')
air = find_kind(d3, 'Airboat'); hov = find_kind(d3, 'Hovercraft')
for k in (quad, sxs, dune, snow, amph, golf, kart, air, hov): drop_m(k)
OWNM = {'Honda': ('Honda Motor Company', 'Global group', 'Japan'), 'Yamaha Motor': ('Yamaha Motor Company', 'Global group', 'Japan'), 'Yamaha': ('Yamaha Motor Company', 'Global group', 'Japan'),
        'Suzuki': ('Suzuki Motor Corporation', 'Global group', 'Japan'), 'Kawasaki': ('Kawasaki Heavy Industries', 'Global group', 'Japan'),
        'Polaris': ('Polaris Inc.', 'Global group', 'United States'), 'Can-Am': ('Bombardier Recreational Products', 'Global group', 'Canada'),
        'Ski-Doo': ('Bombardier Recreational Products', 'Global group', 'Canada'), 'Lynx': ('Bombardier Recreational Products', 'Global group', 'Finland'),
        'Arctic Cat': ('Brad Darling and an investment group', 'Independent', 'United States'), 'Club Car': ('Platinum Equity', 'Independent', 'United States'),
        'Bombardier': ('Bombardier Recreational Products', 'Global group', 'Canada')}
OWNY = {'Arctic Cat': '2025', 'Club Car': '2021', 'Lynx': '1988'}
def oe(k, n, mk, y, d, s, a='', role=None, v=None, g=None):
    o = OWNM.get(mk)
    kw = {}
    if o: kw = dict(own=o[0], tier=o[1], cty=o[2], own_y=OWNY.get(mk))
    return add(k, E(n, mk=mk, y=y, d=d, s=s, a=a, role=role, v=v, g=g or mk.replace('Yamaha Motor', 'Yamaha'), **kw))
for k in (quad, sxs, dune, snow, amph, golf, kart):
    for e in k.get('x', []):
        mk = e.get('mk', '')
        e['g'] = (mk or 'Other makers').replace('Yamaha Motor', 'Yamaha')
        o = OWNM.get(mk)
        if o:
            e['own'], e['tier'], e['cty'] = o
            if OWNY.get(mk): e['own_y'] = OWNY[mk]
# --- quad bikes (ATV article, Polaris, BRP)
oe(quad, 'Honda US90', 'Honda', '1969', 'First sit-on straddle three-wheeled ATV, a 1970 model introduced in 1969.', U_ATV, role='origin')
oe(quad, 'Honda ATC200E Big Red', 'Honda', '1982', 'First utility ATC with suspension and racks.', U_ATV)
oe(quad, 'Honda ATC250R', 'Honda', '1981', 'First Sport ATC built for competition; liquid-cooled version in 1985-1986.', U_ATV)
oe(quad, 'Honda ATC350X', 'Honda', '1985', 'Sport ATC with the largest displacement of the line.', U_ATV)
oe(quad, 'Honda FourTrax TRX250R', 'Honda', '1986', 'Sport ATV of about 1986.', U_ATV)
oe(quad, 'Yamaha Tri-Moto', 'Yamaha Motor', '1979', 'Yamaha\'s first ATC, the YZ125 Tri-Moto of about 1980.', U_ATV)
oe(quad, 'Yamaha Tri-Z 250', 'Yamaha Motor', '1985', 'Liquid-cooled 250 cc two-stroke three-wheeler.', U_ATV)
oe(quad, 'Yamaha Warrior 350', 'Yamaha Motor', '1987', 'Sport quad introduced in 1987.', U_ATV)
oe(quad, 'Yamaha Yamahauler', 'Yamaha Motor', '', 'Utility ATC; year not stated.', U_ATV)
oe(quad, 'Kawasaki KLT200', 'Kawasaki', '1981', 'Kawasaki\'s first ATC.', U_ATV)
oe(quad, 'Kawasaki KXT250 Tecate', 'Kawasaki', '1984', 'Liquid-cooled 250 cc two-stroke ATC.', U_ATV)
oe(quad, 'Kawasaki Tecate-4', 'Kawasaki', '1986', 'Four-wheeled sport ATV of about 1986.', U_ATV)
oe(quad, 'Suzuki ALT125', 'Suzuki', '1982', 'Suzuki\'s first ATC.', U_ATV)
oe(quad, 'Suzuki QuadRunner LT125', 'Suzuki', '1982', 'First mass-produced four-wheeled ATV, aimed at beginners.', U_ATV, role='origin')
oe(quad, 'Suzuki LT50', 'Suzuki', '1984–1987', 'First four-wheeled mini ATV.', U_ATV)
oe(quad, 'Suzuki LT80', 'Suzuki', '1987–2006', 'First ATV with a CVT transmission.', U_ATV)
oe(quad, 'Suzuki LT500R QuadRacer', 'Suzuki', '1988–1990', '500 cc two-stroke nicknamed Quadzilla; discontinued 1990.', U_ATV)
oe(quad, 'Adventure Vehicles Avenger 400', 'Adventure Vehicles', '1980', 'First quad ATV.', U_ATV, g='Other makers')
oe(quad, 'Tiger 500', 'Tiger ATV LTD', '', 'Custom-built ATC in 80-500 cc two-stroke models; the company was liquidated in 1991.', U_ATV, g='Other makers')
oe(quad, 'Polaris Magnum 425', 'Polaris', '1995', 'Polaris four-stroke ATV of 1995.', U_POL)
oe(quad, 'Polaris Sportsman', 'Polaris', '', 'Polaris ATV line; the Sportsman MV850 is its military version with an 850 lb payload.', U_POL, v=[V('Sportsman MV850', '', 'military ATV, smallest military vehicle of Polaris', 'Polaris')])
oe(quad, 'Polaris Sport ATV (KTM-powered)', 'Polaris', '2005', 'Sport ATV announced in 2005 with KTM 525 and 450 engines.', U_POL)
oe(quad, 'Polaris Big Boss 6x6', 'Polaris', '', 'Six-wheeled utility ATV; four were used by Norwegian forces in Afghanistan.', U_ATV)
oe(quad, 'Royal Enfield Quadricycle', 'Royal Enfield', '1893', 'First powered four-wheeler of 1893; an 1898 model is shown.', U_ATV, role='origin', g='Other makers')
for n, y, d in (('Can-Am DS', '1998–', 'Sport and youth ATVs DS50, DS70, DS90, DS90X, DS250, DS450, DS450X, DS650 and DS650 Baja.'),
                ('Can-Am Quest', '1998–', 'Can-Am ATV model.'), ('Can-Am Rally 200', '1998–', 'Can-Am ATV model.'), ('Can-Am Traxter', '1998–', 'Can-Am ATV model, later the Defender.')):
    oe(quad, n, 'Can-Am', y, d, U_BRP)
for e in quad['x']:
    if e['n'] == 'Can-Am Outlander and Renegade':
        e['v'] = e.get('v', [])
        if not any(norm(v['n']) == norm('Outlander 450/500/570/650/700/800/1000') for v in e['v']):
            e['v'] += [V('Outlander 450/500/570/650/700/800/1000', '', 'series named in the BRP list', 'Can-Am'), V('Renegade 570/650/850/1000', '', 'series named in the BRP list', 'Can-Am')]
oe(quad, 'John Deere Buck', 'John Deere', '', 'ATV made under licence by Bombardier.', U_BRP, g='Other makers')
oe(quad, 'Allis-Chalmers Terra Tiger', 'Allis-Chalmers', '1960s–1970s', 'Six-wheeled amphibious ATV, mid-1960s to early 1970s.', U_ATV, g='Other makers')
# --- side-by-sides
oe(sxs, 'Yamaha YXZ1000R', 'Yamaha', '', 'Sport side-by-side.', U_UTV)
oe(sxs, 'Polaris Ranger', 'Polaris', '', 'Polaris utility side-by-side; Monterrey, Mexico builds it from 2010; the Ranger XP Kinetic electric version came in 2023.', U_POL, v=[V('Ranger XP Kinetic', '2023', 'electric', 'Polaris')])
oe(sxs, 'Polaris MRZR', 'Polaris', '2016', 'Military RZR-based vehicle; MRZR-D contract in November 2016, delivered 2017.', U_POL)
oe(sxs, 'Polaris Xpedition', 'Polaris', '2023', 'Overlanding side-by-side lineup of 2023.', U_UTV)
oe(sxs, 'Squad Solar', 'Squad Mobility', '', 'Solar electric side-by-side.', U_UTV, g='Other makers')
oe(sxs, 'Can-Am Maverick R', 'Can-Am', '2010–', 'Can-Am UTV model.', U_BRP) if False else None
for e in sxs['x']:
    if e['n'] == 'Can-Am Maverick':
        e['v'] = e.get('v', []) + [V('Maverick R', '', 'Can-Am UTV model in the BRP list', 'Can-Am')]
    if e['n'] == 'Can-Am Commander and Defender':
        pass
oe(sxs, 'Club Car XRT', 'Club Car', '2008–', 'Personal utility vehicles XRT800, XRT850, XRT1550 and XRT1550 SE.', U_CLUB)
oe(sxs, 'Club Car Villager', 'Club Car', '', 'Personal utility vehicles Villager 2, 2+2 and 2+2 LX; the Villager 4, 6 and 8 carry passengers.', U_CLUB)
# --- dune buggy: existing only
# --- snowmobiles
sn = [
 ('Polaris Comet', 'Polaris', '1964', 'Snowmobile recalled after handling problems.', U_POL),
 ('Polaris Mustang', 'Polaris', '1965', 'Family snowmobile that boosted sales.', U_POL),
 ('Polaris Storm, XLT, XCR, Ultra and Trail', 'Polaris', '1990s', 'Indy-style snowmobile lines of the 1990s.', U_POL),
 ('Polaris Rush', 'Polaris', '2010', 'Snowmobile.', U_POL),
 ('Polaris IQR Racer', 'Polaris', '', 'Racing snowmobiles IQR 440, 600 and 700.', U_POL),
 ('Arctic Cat Boss Cat', 'Arctic Cat', '1970', 'Arctic Cat product line started in 1970.', U_ARC),
 ('Ski-Doo Summit', 'Ski-Doo', '2017', 'Fourth-generation chassis and motor line (model year 2017).', WP + 'Ski-Doo'),
 ('Ski-Doo MXZ', 'Ski-Doo', '2017', 'Fourth-generation chassis and motor line (model year 2017).', WP + 'Ski-Doo'),
 ('Ski-Doo Renegade', 'Ski-Doo', '2017', 'Fourth-generation chassis and motor line (model year 2017).', WP + 'Ski-Doo'),
 ('Ski-Doo REV', 'Ski-Doo', '', 'Ski-Doo platform named on the Snowmobile article.', U_SNOW),
 ('Bombardier B-7', 'Bombardier', '', 'Early Bombardier snow vehicle named on the Snowmobile article.', U_SNOW),
 ('Moto-Ski', 'Bombardier', '1963–1985', 'Brand produced 1963-1985; Bombardier acquired it in 1971.', U_SNOW),
 ('Arctic Cat Bearcat', 'Arctic Cat', '', 'Arctic Cat snowmobile named on the Snowmobile article.', U_SNOW),
 ('Arctic Cat T660 Turbo', 'Arctic Cat', '', 'Turbocharged four-stroke snowmobile named on the Snowmobile article.', U_SNOW),
 ('Ockelbo 8000', 'Ockelbo', '', 'Swedish snowmobile named on the Snowmobile article.', U_SNOW),
 ('Eliason Motor Toboggan', 'Eliason', '', 'Early motor toboggan named on the Snowmobile article.', U_SNOW),
 ('Taiga TS2', 'Taiga Motors', '', 'Electric snowmobile named on the Snowmobile article.', U_SNOW),
]
for n, mk, y, d, s in sn:
    oe(snow, n, mk, y, d, s, g=('Bombardier / BRP' if mk in ('Ski-Doo', 'Bombardier', 'Lynx') else (mk if OWNM.get(mk) else 'Other makers')))
for e in snow['x']:
    if e['n'] in ('Polaris Sno Traveler',): e['role'] = 'landmark'
    if e.get('g') in ('Ski-Doo', 'Lynx'): e['g'] = 'Bombardier / BRP'
oe(snow, 'Lynx', 'Lynx', '1968–', 'Finnish brand built by Velsa Oy and Nordtrac, 1968-1988; Bombardier Recreational Products bought it in 1988.', U_SNOW, g='Bombardier / BRP') if not any(e['n'] == 'Lynx' for e in snow['x']) else None
for e in snow['x']:
    if e['n'] == 'Polaris Sno Traveler':
        e['d'] = 'Polaris\'s first commercial snowmobile, introduced in 1957 by Hetteen Hoist & Derrick (later Polaris).'
        e['y'] = '1957'
# --- golf carts and course vehicles
def cc(n, y, d, v=None, role=None):
    oe(golf, n, 'Club Car', y, d, U_CLUB, v=v, role=role)
for e in golf['x']:
    if e['n'] == 'Club Car DS':
        e['role'] = 'landmark'; e['d'] = 'Golf car named after designer Dom Saporito and described as the company hallmark; 1980-2004.'
    if e['n'] == 'Club Car Precedent':
        e['v'] = [V('Precedent i2', '2008', 'new drive system, for golf courses and personal use', 'Club Car'), V('Precedent i3', '2008', 'first connected golf cart, built with GPSI', 'Club Car'), V('Precedent 4Fun', '', 'used by golf courses', 'Club Car')]
    if e['n'] == 'Club Car Onward':
        e['v'] = [V('Onward', '2017', 'personal transportation vehicle with online customisation', 'Club Car'), V('Onward LSV', '2025', 'street-legal low-speed vehicle', 'Club Car'), V('Villager PTV', '', 'personal-use version', 'Club Car')]
cc('Club Car Tempo', '2018–', 'Replaced the Precedent in 2018; a Tempo Walk is also listed.', v=[V('Tempo Walk', '', 'listed under golf cart models', 'Club Car')])
cc('Club Car CRU', '', 'Listed under Club Car golf cart models.')
cc('Club Car Urban', '', 'Listed under Club Car golf cart models.')
cc('Club Car Connect', '', 'Listed under Club Car golf cart models.')
cc('Club Car Cafe Express', '', 'Listed under Club Car golf cart models.')
oe(golf, 'E-Z-GO golf car', 'E-Z-GO', '1954', 'Start of E-Z-GO golf car production in 1954.', U_GOLF, g='E-Z-GO')
oe(golf, 'Yamaha Golf Car', 'Yamaha', '1979', 'Start of Yamaha golf car production in 1979.', U_GOLF)
# kart makers from the brand register (existing sources)
for nm in ('Tony Kart', 'Birel', 'CRG'):
    b = brands_old.get(nm)
    if b and b.get('s'):
        add(kart, E(nm, mk=nm, y=b.get('f', ''), d=b.get('d', ''), s=b['s'], g=b.get('c', '')))
for k in (quad, sxs, snow, golf, kart, dune, amph):
    if k.get('x'): sort_kind(k, ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 'Polaris', 'Can-Am', 'Bombardier / BRP', 'Arctic Cat', 'Club Car', 'E-Z-GO'])
nl3 = [
 (quad, 'One entry is an ATV or ATC model line sold under its own name; capacity classes and model years are versions.', 'Wikipedia\'s All-terrain vehicle article (Honda, Yamaha, Kawasaki, Suzuki, Polaris and others, first window of 131,840 characters), Polaris Inc., and the BRP list of Bombardier recreational vehicles. Covers the ATV rows of those pages; no whole-space ATV list exists.'),
 (sxs, 'One entry is a side-by-side (UTV) model line; trims and capacities are versions.', 'Wikipedia\'s Utility terrain vehicle article, Polaris Inc., Club Car and the BRP list. Covers all side-by-side rows of those pages; no whole-space list exists.'),
 (dune, 'One entry is a buggy design or maker.', 'Structure-pass entries; no list page was found.'),
 (snow, 'One entry is a snowmobile model line or platform; model years are versions.', 'Wikipedia\'s Snowmobile article (models and makers named), Polaris Inc., Arctic Cat, Ski-Doo and the BRP list. Covers all snowmobile rows on those pages.'),
 (amph, 'One entry is an amphibious vehicle model.', 'Structure-pass entries.'),
 (golf, 'One entry is a golf-cart or low-speed vehicle model line; trims and generations are versions.', 'Club Car\'s Wikipedia article (every named model) and the Golf cart article (E-Z-GO, Yamaha). Complete for Club Car: every personal and golf model on the page; Carryall and Transporter work vehicles are trade equipment and left out.'),
 (kart, 'One entry is a kart chassis maker or design.', 'Structure-pass entry plus the three kart makers of the brand register; no list page was found.'),
]
for k, nl, sel in nl3:
    k['nl'] = nl; k['sel'] = sel + f' Total {len(k.get("x", []))} entries.'; k['xg'] = 'by maker'
d3['ms'] = [
 {'mkt': 'North American snowmobile sales', 'who': 'All makers', 'share': '500,000 units', 'yr': 1971, 's': U_SNOW, 'note': 'annual peak; about 2 million units in 1970-1973'},
 {'mkt': 'North American snowmobile sales', 'who': 'All makers', 'share': '260,000 units', 'yr': 1997, 's': U_SNOW, 'note': 'rebound year followed by gradual decline'},
 {'mkt': 'Snowmobile makers', 'who': 'Bombardier Recreational Products, Arctic Cat, Polaris', 'share': 'three large North American makers', 'yr': 2026, 's': U_SNOW, 'note': 'no per-maker share given; Yamaha ended snowmobile production in 2025'},
]
d3['msum'] = 'Snowmobile figures are from the Wikipedia article; it gives no per-maker shares. Owners come from each maker\'s own article.'

# ================================================================ DEPT 4: heritage
d4 = dept['Heritage rail & horse-drawn']
carr = find_kind(d4, 'Horse-drawn carriage'); wag = find_kind(d4, 'Horse-drawn wagon'); vardo = find_kind(d4, 'Romani vardo'); slg = find_kind(d4, 'Sleigh')
for k in [kk for s in d4['s'] for kk in s['k']]: drop_m(k)
hv = lambda n, d, g, a='', v=None: E(n, d=d, s=U_HDV, g=g, a=a, v=v)
two = 'Two-wheeled passenger vehicles'; four = 'Four-wheeled passenger vehicles'; hire = 'Hire and public transport'
for e in carr['x']:
    e['g'] = four if e['n'] in ('Concord coach', 'Brougham', 'Landau', 'Phaeton', 'Buggy', 'Surrey') else two
    if e['n'] == 'Concord coach': e['g'] = hire
rows = open(W + 'hdv.txt', encoding='utf-8').read().strip().split('\n') if os.path.exists(W + 'hdv.txt') else []
import hdv_data
for kind, grp, n, a, d in hdv_data.ROWS:
    k = {'carriage': carr, 'wagon': wag, 'vardo': vardo, 'sleigh': slg}[kind]
    add(k, hv(n, d, grp, a))
for e in wag['x']: e.setdefault('g', 'Load-carrying vehicles')
for e in vardo['x']: e.setdefault('g', 'Romani wagons')
for e in slg['x']: e.setdefault('g', 'Sleighs')
for k, nl, sel in ((carr, 'One entry is a named type of horse-drawn passenger vehicle; builder models and sizes are versions.',
                    'Every passenger-vehicle and public-transport type in the "Passenger vehicles" and "Historic public transport" sections of Wikipedia\'s Horse-drawn vehicle article (the page has no separate list of horse-drawn vehicles), plus the structure-pass entries. Seating layouts (dos-a-dos, vis-a-vis, equipage) are not vehicles and the sleigh, vardo and troika types are under their own kinds.'),
                   (wag, 'One entry is a named type of horse-drawn load-carrying vehicle.', 'Every entry of the "Load carrying" section of Wikipedia\'s Horse-drawn vehicle article, plus the structure-pass entries. Farm implements, canal boats, rail wagonways and military types in the "Other horse-powered" section are out of scope.'),
                   (vardo, 'One entry is a named type of Romani living wagon.', 'Structure-pass entries; the Horse-drawn vehicle article names only the general Vardo.'),
                   (slg, 'One entry is a named type of sleigh.', 'Sleigh, Troika and Vozok of Wikipedia\'s Horse-drawn vehicle article plus the structure-pass entries.')):
    k['nl'] = nl; k['sel'] = sel + f' Total {len(k["x"])} entries.'; k['xg'] = 'by what it carries'
loco = find_kind(d4, 'Locomotive')
loco['nl'] = 'One entry is a locomotive class or type with preserved examples in private or society hands; individual locomotives are versions.'
loco['sel'] = 'Kept from the structure pass: each class is attested on its own Wikipedia page. No fetched page lists privately owned locomotive classes, so none were added.'
loco['xg'] = 'by builder'
for k in (find_kind(d4, 'Railcar'), find_kind(d4, 'Railway carriage'), find_kind(d4, 'Motor trolley'), find_kind(d4, 'Ride-on miniature locomotive')):
    k['nl'] = 'One entry is a rail vehicle type or design with preserved examples; examples and liveries are versions.'
    k['sel'] = 'Kept from the structure pass: each type has its own Wikipedia page. No fetched list covers privately owned rail vehicles.'
    k['xg'] = 'by builder'
for k in [kk for s in d4['s'] for kk in s['k']]:
    for e in k.get('x', []): e.setdefault('g', e.get('mk') or 'Other')


# ================================================================ ROUND 2
U_YAM = 'https://cdn-fastly.atv.com/manufacturers/yamaha.html'
U_SUZ = 'https://www.atv.com/manufacturers/suzuki.html'
U_SUZ07 = 'https://powersportsbusiness.com/features/2007/11/12/nov-12-2007-suzuki-streamlines-atv-product-names/'
U_KAW = WP + 'List_of_Kawasaki_motorcycles'
U_WMS = 'https://winnebago.com/lifestyle/winnebagolife/showroom/winnebago-milestones-pioneering-for-65-years'
U_FSER = WP + 'Ford_F-Series'
U_BT = 'http://www.brusselstimes.com/1414185/over-1-5-million-vans-registered-in-eu-in-2024'
U_VT = 'https://www.volvotrucks.com/th-th/news/press-releases/2025/feb/volvo-trucks-leads-the-heavy-truck-market-in-europe.html'
GG, NC, IND = 'Global group', 'National champion', 'Independent'
SELL = 'Stellantis'
OWN2 = {  # marque -> (own, tier, cty, own_y); every row rests on a fetched owner page (Wikipedia articles of the company)
 'Ford': ('Ford Motor Company', GG, 'United States', None),
 'Chevrolet': ('General Motors', GG, 'United States', '1918'), 'GMC': ('General Motors', GG, 'United States', '1909'),
 'Ram': (SELL, GG, 'United States', '2021'), 'Jeep': (SELL, GG, 'United States', '2021'), 'Dodge': (SELL, GG, 'United States', '2021'), 'Chrysler': (SELL, GG, 'United States', '2021'),
 'Fiat': (SELL, GG, 'Italy', '2021'), 'Fiat Professional': (SELL, GG, 'Italy', '2021'), 'Citroën': (SELL, GG, 'France', '2021'), 'Peugeot': (SELL, GG, 'France', '2021'),
 'Opel': (SELL, GG, 'Germany', '2021'), 'Opel/Vauxhall': (SELL, GG, 'Germany', '2021'), 'Vauxhall': (SELL, GG, 'United Kingdom', '2021'),
 'Toyota': ('Toyota Motor Corporation', GG, 'Japan', None), 'Daihatsu': ('Toyota Motor Corporation', GG, 'Japan', '2016'), 'Hino': ('Archion', GG, 'Japan', '2026'),
 'Isuzu': ('Isuzu Motors', GG, 'Japan', None), 'UD Trucks': ('Isuzu Motors', GG, None, '2021'),
 'Nissan': ('Nissan Motor Corporation', GG, 'Japan', None), 'Mitsubishi': ('Mitsubishi Motors', GG, 'Japan', None),
 'Hyundai': ('Hyundai Motor Group', GG, 'South Korea', None), 'Kia': ('Hyundai Motor Group', GG, 'South Korea', '1998'),
 'Renault': ('Renault Group', GG, 'France', None), 'Dacia': ('Renault Group', GG, 'Romania', '1999'),
 'Mercedes-Benz': ('Mercedes-Benz Group', GG, 'Germany', None),
 'Freightliner': ('Daimler Truck', GG, None, None), 'Western Star': ('Daimler Truck', GG, None, None), 'Mitsubishi Fuso': ('Daimler Truck', GG, None, None),
 'Volkswagen': ('Volkswagen Group', GG, 'Germany', None), 'Volkswagen Truck & Bus': ('Traton', GG, 'Brazil', None),
 'MAN': ('Traton', GG, 'Germany', '2021'), 'Scania': ('Traton', GG, 'Sweden', '2021'), 'International': ('Traton', GG, 'United States', '2021'), 'International Motors': ('Traton', GG, 'United States', '2021'),
 'Volvo Trucks': ('Volvo Group', GG, 'Sweden', None), 'Renault Trucks': ('Volvo Group', GG, 'France', '2000'), 'Mack': ('Volvo Group', GG, None, '2000'),
 'Kenworth': ('Paccar', GG, None, None), 'Peterbilt': ('Paccar', GG, None, None), 'DAF': ('Paccar', GG, None, None),
 'Iveco': ('Iveco Group', GG, 'Italy', '2022'),
 'Tata': ('Tata Motors', NC, 'India', None), 'Tata Motors': ('Tata Motors', NC, 'India', None), 'Tata Daewoo': ('Tata Motors', NC, None, '2004'),
 'Ashok Leyland': ('Hinduja Group', NC, 'India', None), 'Mahindra': ('Mahindra Group', NC, 'India', None), 'Mahindra & Mahindra': ('Mahindra Group', NC, 'India', None),
 'KGM': ('KG Group', IND, 'South Korea', '2022'), 'Land Rover': ('Tata Motors', IND, None, '2008'),
 'Honda': ('Honda Motor Company', GG, 'Japan', None), 'Suzuki': ('Suzuki Motor Corporation', GG, 'Japan', None), 'Kawasaki': ('Kawasaki Heavy Industries', GG, 'Japan', None),
 'Polaris': ('Polaris Inc.', GG, 'United States', None),
 'Can-Am': ('Bombardier Recreational Products', GG, 'Canada', None), 'Ski-Doo': ('Bombardier Recreational Products', GG, 'Canada', None),
 'Bombardier': ('Bombardier Recreational Products', GG, 'Canada', None), 'Lynx': ('Bombardier Recreational Products', GG, 'Finland', '1988'),
 'Arctic Cat': ('Brad Darling and an investment group', IND, 'United States', '2025'), 'Club Car': ('Platinum Equity', IND, 'United States', '2021'),
}
OFFROAD_NAMES = set()
def set_own(e, key=None):
    for kk in ('own', 'tier', 'cty', 'own_y'): e.pop(kk, None)
    k = key or e.get('mk', '')
    if 'Unimog' in e['n']: o = ('Daimler Truck', GG, None, '2021')
    else: o = OWN2.get(k)
    if o:
        for kk, vv in zip(('own', 'tier', 'cty', 'own_y'), o):
            if vv: e[kk] = vv

# ---- trucks (List of trucks read to its end)
rigid = find_kind(d1, 'Rigid truck'); tu = find_kind(d1, 'Tractor unit')
heavy = {'n': 'Heavy truck', 'a': 'lorry · HGV · semi-trailer tractor · artic', 'd': 'Lorry of the heavy weight class, from road tractors to military trucks; a van-based or light lorry → Rigid truck.',
         's': U_TRUCKS, 'x': [], 'tt': [['Class', ['Heavy', 'Extra heavy']], ['Drive', ['4x2', '6x4', '8x4', 'All-wheel drive']], ['Cab', ['Day cab', 'Sleeper cab']]],
         'see': [['G1', 'Tractor unit', 'a heavy truck that hauls a semi-trailer']]}
d1['s'][2]['k'].insert(1, heavy)
existing_dept1 = set()
for kk in [k for s in d1['s'] for k in s['k']]:
    for e in kk.get('x', []):
        existing_dept1.add(norm(e['n']))
        for v in e.get('v', []): existing_dept1.add(norm(v['n']))
ntr = {'rigid': 0, 'heavy': 0, 'skipped': 0}
CL = {'L': 'Light', 'M': 'Medium', 'H': 'Heavy', 'X': 'Extra heavy'}
for line in open(W + 'trucks_raw.txt', encoding='utf-8').read().strip().split('\n'):
    st, origin, maker, items = line.split('|')
    for it in items.split(';'):
        c, name = it.split(':', 1)
        if norm(name) in existing_dept1:
            ntr['skipped'] += 1; continue
        existing_dept1.add(norm(name))
        cls = CL[c]
        if st == 'A': d = f'{cls} truck in production at the time of the list.'
        else: d = f'{cls} truck, out of production; origin {origin}.'
        e = E(name, mk=maker, y='', d=d, s=U_TRUCKS, g=maker)
        set_own(e)
        if c == 'H': heavy['x'].append(e); ntr['heavy'] += 1
        else: rigid.setdefault('x', []).append(e); ntr['rigid'] += 1
for e in rigid['x']: e.setdefault('g', e.get('mk', ''))
rigid['x'].sort(key=lambda e: (e['g'].lower(), e['n'].lower()))
heavy['x'].sort(key=lambda e: (e['g'].lower(), e['n'].lower()))
rigid['nl'] = 'One entry is a light or medium lorry model line sold under its own name; cab and chassis lengths are versions.'
heavy['nl'] = 'One entry is a heavy or extra-heavy lorry model line sold under its own name, including road tractors and military trucks that collectors buy; cab and axle variants are versions.'
for k in (rigid, heavy):
    k['xg'] = 'by maker'
    k['sel'] = (f'Every row of Wikipedia\'s List of trucks (active and discontinued tables), read in three windows to the end of the page text (characters 0-269,154), split by the page\'s own class column '
                f'(light and medium here, heavy and extra heavy under Heavy truck); rows already in the van or pickup kinds are not repeated, and the Mercedes-Benz Actros row was cut at a window edge and added from that note. '
                f'Complete: {len(k["x"])} entries here; {ntr["rigid"] + ntr["heavy"]} new entries across both kinds from the page, {ntr["skipped"]} rows skipped as duplicates.')
tu['nl'] = ''
tu.pop('nl'); tu.pop('sel', None)

# ---- owners recomputed from fetched pages only
for kk in [k for s in d1['s'] for k in s['k']]:
    for e in kk.get('x', []):
        set_own(e)
for kk in (quad, sxs, dune, snow, amph, golf, kart):
    for e in kk.get('x', []):
        set_own(e, 'Yamaha-none' if e.get('mk') in ('Yamaha', 'Yamaha Motor') else None)
# caravans: blank what no fetched page states
BLANK = {'Boler', 'nuCamp T@B', 'Classic plywood teardrop', 'Conqueror UEV-440', 'Patriot X1', 'Four Wheel Campers pop-up', 'Lance hard-side camper', 'GMC Motorhome', 'Blue Bird Wanderlodge', 'EarthRoamer', 'Bedford Dormobile'}
for kk in (touring, fifth, tear, fold, toy, offr, camper, truckc, lowp, over, acl, expd):
    for e in kk.get('x', []):
        if e['n'] in BLANK:
            for q in ('own', 'tier', 'cty', 'own_y'): e.pop(q, None)
        if e['n'] == 'Unimog expedition camper': e.update({'own': 'Daimler Truck', 'tier': GG, 'cty': 'Germany', 'own_y': '2021'}); 
        if e['n'] == 'Sprite': e['own_y'] = '1994'
        if e['n'] == 'Volkswagen Westfalia Camper': e['own'] = 'Volkswagen Group'; e['cty'] = 'Germany'; e.pop('own_y', None)
        if e['n'] == 'GMC Motorhome': e['cty'] = 'United States'
        if e['n'] == 'Mercedes-Benz Marco Polo': e['own'] = 'Mercedes-Benz Group'

# ---- Winnebago: Chieftain and dated corrections
add(acl, E('Winnebago Chieftain', mk='Winnebago', y='1969', d='Winnebago model introduced in 1969; the fetched pages do not state its class, so it sits here with the other Winnebago motorhomes.', s=U_WMS, g=G_WIN, own='Winnebago Industries', tier=NC, cty='United States'))
for kk in (camper, over, acl):
    for e in kk['x']:
        if e['n'] == 'Winnebago Winnie Wagon': e['y'] = '1974'; e['s'] = U_WMS; e['d'] = 'Small low-profile pop-top motorhome from 1974.'
        if e['n'] == 'Winnebago LeSharo': e['y'] = '1983'; e['s'] = U_WMS
        if e['n'] == 'Winnebago Rialta': e['y'] = '1995'; e['s'] = U_WMS
        if e['n'] == 'Winnebago Minnie Winnie': e['d'] = 'Motorhome on a Dodge chassis, then Chevrolet or Ford after 1980; the Winnebago Industries article dates it from 1973, while the company\'s milestones page dates the line to 1994.'
sort_kind(acl, GORD)
sort_kind(camper, GORD)

# ---- ATV and side-by-side lines from the new pages
def addo(k, n, mk, y, d, s, v=None, role=None):
    e = E(n, mk=mk, y=y, d=d, s=s, v=v, role=role, g=mk)
    set_own(e, 'Yamaha-none' if mk == 'Yamaha' else mk)
    return add(k, e)
for e in quad['x']:
    if e['n'] == 'Yamaha Grizzly':
        e['v'] += [V('Grizzly EPS SE', '2021', 'trim', 'Yamaha'), V('Grizzly EPS XT-R', '2021', 'trim', 'Yamaha'), V('Grizzly 90', '2021', 'youth model', 'Yamaha')]
        e['s'] = U_YAM
    if e['n'] == 'Yamaha Raptor':
        e['v'] += [V('Raptor 90', '2021', 'youth model', 'Yamaha'), V('Raptor 700R SE', '2021', '', 'Yamaha')]
addo(quad, 'Yamaha Kodiak', 'Yamaha', '2021', 'Utility ATV in 450 and 700 versions, each in base, EPS and EPS SE trims.', U_YAM, v=[V('Kodiak 450', '2021', '', 'Yamaha'), V('Kodiak 700', '2021', '', 'Yamaha')])
addo(quad, 'Yamaha YFZ450R', 'Yamaha', '2021', 'Sport ATV in YFZ450R and YFZ450R SE versions.', U_YAM)
addo(sxs, 'Yamaha Wolverine', 'Yamaha', '2021', 'Side-by-side family: X2, X4 850, RMAX2 1000 and RMAX4 1000 (RMAX family new for 2021).', U_YAM)
addo(sxs, 'Yamaha Viking', 'Yamaha', '2021', 'Side-by-side in Viking, EPS, EPS Ranch Edition and six-seat Viking VI.', U_YAM)
for e in sxs['x']:
    if e['n'] == 'Yamaha YXZ1000R':
        e['v'] = [V('YXZ1000R SE', '2021', '', 'Yamaha'), V('YXZ1000R SS', '2021', '', 'Yamaha'), V('YXZ1000R SS SE', '2021', '', 'Yamaha'), V('YXZ1000R SS XT-R', '2021', '', 'Yamaha')]
        e['s'] = U_YAM
kv = lambda *a: [V(x, '', '', 'Kawasaki') for x in a]
addo(quad, 'Kawasaki Bayou', 'Kawasaki', '', 'Kawasaki utility ATV in 185, 220, 250, 300 and 400 versions.', U_KAW, v=kv('Bayou 185', 'Bayou 220', 'Bayou 250', 'Bayou 300', 'Bayou 400'))
addo(quad, 'Kawasaki Brute Force', 'Kawasaki', '', 'Kawasaki utility ATV in 300, 650 and 750 versions.', U_KAW, v=kv('Brute Force 300', 'Brute Force 650', 'Brute Force 750'))
addo(quad, 'Kawasaki Prairie', 'Kawasaki', '', 'Kawasaki utility ATV from 250 to 700; the 400 was among the first full-size ATVs with fully automatic transmission and the 650 an early V-twin ATV.', U_KAW, v=kv('Prairie 250', 'Prairie 300', 'Prairie 360', 'Prairie 400', 'Prairie 650', 'Prairie 700'))
addo(quad, 'Kawasaki KFX', 'Kawasaki', '', 'Kawasaki sport and youth ATVs; the KFX 80 and KFX 400 were rebadged Suzukis and the KFX 50 was Suzuki-based until 2006.', U_KAW, v=kv('KFX 50', 'KFX 80', 'KFX 90', 'KFX 400', 'KFX 450R', 'KFX 700 V-Force'))
addo(quad, 'Kawasaki Lakota', 'Kawasaki', '', 'Kawasaki sport ATV in Lakota 300 and Lakota Sport 300 versions.', U_KAW, v=kv('Lakota 300', 'Lakota Sport 300'))
addo(quad, 'Kawasaki Mojave', 'Kawasaki', '', 'Kawasaki sport ATV in 110 and 250 versions.', U_KAW, v=kv('Mojave 110', 'Mojave 250'))
sv = lambda *a: [V(x, '', '', 'Suzuki') for x in a]
addo(quad, 'Suzuki KingQuad', 'Suzuki', '1991', 'Utility ATV introduced in 1991 and returned in 2005 as the KingQuad 700; the Eiger name was used for the 400 class until 2008, when KingQuad replaced it.', U_SUZ,
     v=[V('KingQuad 400', '2020', '400AS and 400FS variants with swingarm and foot shift (2008)', 'Suzuki'), V('KingQuad 500', '2020', '', 'Suzuki'), V('KingQuad 750', '2019', 'overhauled for 2019; 750 AXi from 2008', 'Suzuki')])
addo(quad, 'Suzuki Eiger', 'Suzuki', '2002–2008', 'Suzuki 400-class utility ATV built from 2002 (2003 at the Rome, Georgia plant); the name was dropped for KingQuad in 2008.', U_SUZ07)
addo(quad, 'Suzuki QuadSport', 'Suzuki', '', 'Suzuki sport ATVs; the Z50 and Z90 are 2020 models and the Z400 was reviewed in 2009.', U_SUZ, v=sv('QuadSport Z50', 'QuadSport Z90', 'QuadSport Z400'))
addo(quad, 'Suzuki QuadRacer LT-R450', 'Suzuki', '2006', 'Sport quad introduced in 2006.', U_SUZ07)
sort_kind(quad, ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 'Polaris', 'Can-Am', 'Other makers'])
sort_kind(sxs, ['Yamaha', 'Polaris', 'Can-Am', 'Kawasaki', 'Club Car', 'Other makers'])
for k in (quad, sxs):
    k['sel'] = k['sel'].replace('Total', 'Yamaha lines from atv.com (2021 model year), Kawasaki lines from Wikipedia\'s List of Kawasaki motorcycles (no years given) and Suzuki lines from atv.com and Powersports Business (2007). The All-terrain vehicle article was read to its end (100,000 of 131,840 characters held no further content). Total', 1)

# ---- market facts
d1['ms'] = [
 {'mkt': 'EU new vans', 'who': 'All makers', 'share': '1,586,688 units, up 8.3 %', 'yr': 2024, 's': U_BT, 'note': 'diesel 84.5 % of registrations, electric 6.1 %; no brand shares on the page'},
 {'mkt': 'EU new trucks', 'who': 'All makers', 'share': '327,896 units, down 6.3 %', 'yr': 2024, 's': U_BT, 'note': 'diesel 95.1 % of registrations'},
 {'mkt': 'EU new buses', 'who': 'All makers', 'share': '35,579 units, up 9.2 %', 'yr': 2024, 's': U_BT, 'note': 'diesel 63.1 %, electric 18.5 %'},
 {'mkt': 'European heavy trucks (16 tonnes and above)', 'who': 'Volvo Trucks', 'share': '17.9 %', 'yr': 2024, 's': U_VT, 'note': '56,331 trucks registered; Volvo\'s own press release, no competitor figures'},
 {'mkt': 'Brazil heavy trucks', 'who': 'Volvo Trucks', 'share': '23.7 %', 'yr': 2024, 's': U_VT, 'note': 'Volvo\'s own press release'},
 {'mkt': 'North American heavy trucks', 'who': 'Volvo Trucks', 'share': '10.5 %', 'yr': 2024, 's': U_VT, 'note': 'US and Canada; 10.2 % in 2023'},
 {'mkt': 'US pickups', 'who': 'Ford F-Series', 'share': '765,649 units', 'yr': 2024, 's': U_FSER, 'note': '828,832 in 2025; best-selling pickup line in the US since 1977'},
 {'mkt': 'European pickups', 'who': 'Ford Ranger', 'share': '27,300 units', 'yr': 2015, 's': U_PU, 'note': 'most popular pickup in Europe; all pickups under 1 % of light vehicles sold'},
 {'mkt': 'China pickups', 'who': 'Chinese pickups led by the Great Wall Wingle', 'share': '378,000 units, up 48 %', 'yr': 2010, 's': U_PU, 'note': 'from the page\'s ChinaAutoWeb reference'},
]
d1['msum'] = 'Registration totals are from a news report of ACEA\'s 2024 figures, truck shares from Volvo\'s press release and pickup sales from the Ford F-Series article; no source found gives brand shares for vans or for rival truck makers.'
d1['note'] = 'Vans, pickups, lorries and preserved buses are named by marque from Wikipedia lists; owners and tiers come from each company\'s Wikipedia article.'
d1['t'] = ('Vans, minibuses, taxis, pickups, lorries and coaches that a person owns or converts; a family car or SUV → Cars; a van converted for living in → Caravans, motorhomes & trailers.')

# ================================================================ assemble
depts = [dept[n] for n in NAMES]
part_bu = {
 'Airstream': {'own': 'Thor Industries', 'tier': 'Global group', 'c': 'United States'},
 'Jayco': {'own': 'Thor Industries', 'tier': 'Global group', 'c': 'United States'},
 'Keystone RV': {'own': 'Thor Industries', 'tier': 'Global group', 'c': 'United States'},
 'Hymer': {'own': 'Thor Industries', 'tier': 'Global group', 'c': 'Germany'},
 'Eriba': {'own': 'Thor Industries', 'tier': 'Global group', 'c': 'Germany'},
 'Winnebago': {'own': 'Winnebago Industries', 'tier': 'National champion', 'c': 'United States'},
 'Grand Design': {'own': 'Winnebago Industries', 'tier': 'National champion', 'c': 'United States'},
 'Swift Group': {'own': 'Swift Group', 'tier': 'Independent', 'c': 'United Kingdom'},
 'Forest River': {'own': 'Forest River RV', 'tier': 'Global group', 'c': 'United States'},
 'Shasta': {'own': 'Forest River RV', 'tier': 'Global group', 'c': 'United States'},
 'Polaris': {'own': 'Polaris Inc.', 'tier': 'Global group', 'c': 'United States'},
 'Can-Am': {'own': 'Bombardier Recreational Products', 'tier': 'Global group', 'c': 'Canada'},
 'Ski-Doo': {'own': 'Bombardier Recreational Products', 'tier': 'Global group', 'c': 'Canada'},
 'Lynx': {'own': 'Bombardier Recreational Products', 'tier': 'Global group', 'c': 'Finland'},
 'Arctic Cat': {'own': 'Brad Darling and an investment group', 'tier': 'Independent', 'c': 'United States'},
 'Club Car': {'own': 'Platinum Equity', 'tier': 'Independent', 'c': 'United States'},
}
part = {'replaces': NAMES, 'depts': depts, 'brands': [], 'brand_updates': {k: v for k, v in part_bu.items() if k in brands_old}, 'renames': {}, 'moves': []}

# brand register: new owners / makers used as own/mk
known = set(brands_old)
newb = {}
def nb(n, c, d, s, seg='Mainstream', f=''):
    if n in known or n in newb: return
    newb[n] = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': '', 'd': d, 's': s}
nb('Thor Industries', 'United States', 'Owner of Airstream, Jayco, Keystone, Dutchmen, Heartland, Thor Motor Coach and, since 2018-2019, the Erwin Hymer Group.', U_THOR)
nb('Knaus Tabbert', 'Germany', 'Caravan and motorhome group with the brands Knaus, Tabbert, Weinsberg, T@B and Morelo.', U_KNAUS, 'Specialist')
nb('Winnebago Industries', 'United States', 'Maker of Winnebago motorhomes; owns Newmar and Grand Design.', U_WIN)
nb('Swift Leisure', 'United Kingdom', 'UK caravan and motorhome maker founded in 1964; also known as the Swift Group.', U_SWIFT, 'Specialist', '1964')
nb('Bedford', 'United Kingdom', 'Vauxhall-owned commercial-vehicle brand, founded 1931 and retired 1990; maker of the Bedford OB coach.', U_OB, 'Heritage manufactory')
nb('Platinum Equity', 'United States', 'Owner of Club Car since 2021.', U_CLUB, 'Specialist')
nb('E-Z-GO', 'United States', 'Golf-car maker that began golf car production in 1954.', U_GOLF, 'Specialist', '')
nb('Tiffin Motorhomes', 'United States', 'Luxury motorhome maker acquired by Thor in 2020.', U_THOR, 'Premium')
nb('Newmar', 'United States', 'Luxury RV maker acquired by Winnebago Industries in 2019.', U_WIN, 'Premium')
nb('Dethleffs', 'Germany', 'Caravan brand of the Hymer group; Dethleffs Wohnauto of 1931.', U_HYM, 'Specialist')
nb('Roadtrek', 'Canada', 'Class B campervan brand, acquired by Hymer in 2016 and sold to the Rapido Group in 2019.', U_HYM, 'Specialist')
nb('Casita', 'United States', 'Texas RV maker.', U_RVM, 'Specialist')
nb('Aliner', 'United States', 'Original A-frame trailer manufacturer.', U_RVM, 'Specialist')
nb('Spacecraft Manufacturing', 'United States', 'Missouri maker of the largest fifth-wheel trailers.', U_RVM, 'Specialist')
nb('Forest River RV', 'United States', 'Indiana RV maker owned by Berkshire Hathaway.', U_RVM)
nb('REV Group', 'United States', 'Wisconsin parent of Fleetwood, Monaco Coach and Holiday Rambler.', U_RVM)
part['brands'] = list(newb.values())
json.dump(part, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print({n: sum(len(k.get('x', [])) for s in dept[n]['s'] for k in s['k']) for n in NAMES})
print('new vans', n_new, 'pickups', len(order_pk), os.path.getsize(OUT))
