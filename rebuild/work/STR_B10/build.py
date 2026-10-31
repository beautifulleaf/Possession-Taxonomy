# -*- coding: utf-8 -*-
import json, copy, sys, os, shutil, re, time
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/STR_B10')
from spec_tt import KT
from spec_layout import DEPTS, CAT_AX, CAT_KEY
R = '/home/user/Possession-Taxonomy/rebuild/'
src = R + 'work/STR_B10/bak/B10.orig.json'
if not os.path.exists(src):
    shutil.copy(R + 'out/B10.json', src)
d = json.load(open(src))
K = {}
oldshelf = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = copy.deepcopy(k); oldshelf[k['n']] = (dp['n'], s['n'])
before = dict(depts=len(d['depts']), shelves=sum(len(dp['s']) for dp in d['depts']), kinds=len(K),
              arch=sum(len(k.get('x', [])) for k in K.values()))
LOG = {'split': [], 'merged': [], 'renamed': [], 'added': [], 'demoted': [], 'moved': []}

def addm(k, name, mk):
    m = k.setdefault('m', [])
    if not any(p[0] == name for p in m):
        m.append([name, mk or ''])

def demote(kn, names):
    k = K[kn]; keep = []
    for x in k.get('x', []):
        if x['n'] in names:
            for v in x.get('v', []) or []:
                addm(k, v['n'], v.get('mk') or x.get('mk'))
            LOG['demoted'].append(f"{kn}: {x['n']}")
        else:
            keep.append(x)
    miss = [n for n in names if n not in [x['n'] for x in k.get('x', [])]]
    assert not miss, (kn, miss)
    k['x'] = keep
    if not keep: k.pop('x')

def newkind(n, a, dd, s, base=None, **kw):
    k = copy.deepcopy(base) if base else {}
    for f in ('t', 'tt', 'x', 'm', 'r'):
        k.pop(f, None) if base is None else None
    k.update({'n': n, 'a': a, 'd': dd, 's': s}); k.update(kw)
    return k

def pull(kn, pred):
    """remove from K[kn]['x'] entries named in pred, return them"""
    out = [x for x in K[kn].get('x', []) if x['n'] in pred]
    K[kn]['x'] = [x for x in K[kn].get('x', []) if x['n'] not in pred]
    return out

# ---------- renames ----------
def rename(old, new, alias=None, dd=None):
    k = K.pop(old); k['n'] = new
    if alias is not None: k['a'] = alias
    if dd: k['d'] = dd
    K[new] = k; oldshelf[new] = oldshelf[old]; LOG['renamed'].append(f"{old} -> {new}")
rename('Dog waste bags', 'Dog waste bags and scoopers', 'poop bags · poo bags · dog poop scooper', 'Bags, dispensers and scoopers made for picking up and disposing of a dog\'s droppings.')
rename('Giant hood', 'Hawk box', 'giant hood · transport box', 'A box in which a hooded or unhooded raptor travels in the dark, called a giant hood in the UK.')

# ---------- splits ----------
# Dog treats and chews -> Dog treats + Dog chew
t = K.pop('Dog treats and chews'); S = t['s']
K['Dog treats'] = dict(n='Dog treats', a='dog snacks · dental treats · training treats', d='Small snacks given to a dog as a reward or for its teeth, not a complete diet.', s=S,
                       m=[p for p in t['m'] if p[0] not in ('Redbarn Bully Slims', 'Yakers Dog Chew')])
K['Dog chew'] = dict(n='Dog chew', a='long-lasting chew · natural chew · bully stick · rawhide', d='A hard, long-lasting chew of rawhide, bone, antler or dried animal part that a dog gnaws for an hour or more.', s=S,
                     m=[p for p in t['m'] if p[0] in ('Redbarn Bully Slims', 'Yakers Dog Chew')])
for n in ('Dog treats', 'Dog chew'): oldshelf[n] = ('Dogs', 'Dog food & treats')
LOG['split'].append('Dog treats and chews -> Dog treats + Dog chew')

# Dog collar: head collar types out to new Dog head halter
halti = pull('Dog collar', ['Halti Headcollar', 'Gentle Leader'])
K['Dog head halter'] = dict(n='Dog head halter', a='head collar · head halter · no-pull head collar', d='A strap system with a loop over the muzzle and a strap behind the ears, so the walker steers the dog\'s head to stop pulling.',
                            s=K['Dog collar']['s'], x=halti)
oldshelf['Dog head halter'] = oldshelf['Dog collar']; LOG['split'].append('Dog collar -> Dog collar + Dog head halter (Halti, Gentle Leader moved)')

# Dog training aids -> whistle, clicker, treat pouch
t = K.pop('Dog training aids'); S = t['s']
whistle_x = pull_x = [x for x in t['x'] if x['n'] == 'Acme 210.5 whistle']
K['Dog whistle'] = dict(n='Dog whistle', a='gundog whistle · silent whistle · recall whistle', d='A whistle that signals a recall or turn to a dog at a distance, in audible or high-pitch silent form.', s=S, x=whistle_x)
K['Dog clicker'] = dict(n='Dog clicker', a='training clicker · box clicker', d='A small hand-held noisemaker sounded the instant a dog does the right thing, so it learns which action earned the reward.', s=S,
                        x=[x for x in t['x'] if x['n'] == 'Box clicker'], m=t['m'])
K['Treat pouch'] = dict(n='Treat pouch', a='training pouch · treat bag', d='A pouch worn at the waist that holds treats within quick reach of the handler during training.', s=S)
for n in ('Dog whistle', 'Dog clicker', 'Treat pouch'): oldshelf[n] = ('Dogs', 'Collars, leads & harnesses')
LOG['split'].append('Dog training aids -> Dog whistle + Dog clicker + Treat pouch (target stick folded into clicker types)')

# Litter mat and scoop -> two kinds
t = K.pop('Litter mat and scoop'); S = t['s']
K['Litter mat'] = dict(n='Litter mat', a='litter trapper · litter trapping mat', d='A mat set outside the litter box that catches litter tracked out on a cat\'s paws.', s=S, m=t['m'][:5])
K['Litter scoop'] = dict(n='Litter scoop', a='litter sifter · scoop', d='A slotted scoop that lifts clumps and waste out of the litter and lets clean litter fall back.', s=S, m=t['m'][5:])
for n in ('Litter mat', 'Litter scoop'): oldshelf[n] = ('Cats', 'Litter & toilets')
LOG['split'].append('Litter mat and scoop -> Litter mat + Litter scoop')

# Lunge roller and side reins -> three kinds
t = K.pop('Lunge roller and side reins'); S = t['s']
byn = {x['n']: x for x in t['x']}
K['Lunge roller'] = dict(n='Lunge roller', a='surcingle · roller · lungeing roller', d='A padded girth band with rings up the sides, put on a horse to hold side reins and other aids when lungeing or long-lining.', s=S)
K['Lungeing cavesson'] = dict(n='Lungeing cavesson', a='lunging cavesson · longeing cavesson', d='A headpiece with a reinforced noseband and rings on which the lunge line is clipped, so the bit is not pulled on.', s=S)
K['Side reins and lunging aids'] = dict(n='Side reins and lunging aids', a='side reins · Pessoa · Chambon · de Gogue', d='Reins and pulley or strap systems clipped between the horse\'s headgear and a roller to shape its head carriage while it is lunged.', s=S, x=[byn['Pessoa lungeing system']])
for n in ('Lunge roller', 'Lungeing cavesson', 'Side reins and lunging aids'): oldshelf[n] = ('Horses & riding', 'Headcollars, lungeing & driving')
for nm in ('Training surcingle', 'Side reins', 'Lungeing cavesson'):
    LOG['demoted'].append(f"Lunge roller and side reins: {nm} (became a kind)")
LOG['split'].append('Lunge roller and side reins -> Lunge roller + Lungeing cavesson + Side reins and lunging aids')

# ---------- archetype demotions ----------
D = {
 'Dog bed': ['Orthopaedic memory-foam bed', 'Calming donut bed'],
 'Dog crate': ['Folding wire crate', 'Plastic airline kennel'],
 'Gundog training dummy': ['Canvas dummy'],
 'Dog clicker': ['Box clicker'],
 'Protein skimmer': ['Needle-wheel skimmer', 'Cone skimmer', 'Beckett skimmer'],
 'Aquarium hardscape rock': ['Seiryu stone', 'Dragon Stone (Ohko)'],
 'Aquarium driftwood': ['Spider wood', 'Manzanita wood', 'Malaysian driftwood', 'Cholla wood'],
 'English saddle': ['Close-contact jumping saddle', 'Dressage saddle', 'General-purpose saddle', 'Endurance saddle', 'Showing saddle', 'Saddle seat saddle', 'Racing saddle', 'Polo saddle'],
 'Western saddle': ['Roping saddle', 'Barrel racing saddle', 'Reining saddle', 'Cutting saddle', 'Bronc saddle', 'Trail saddle', 'Western endurance saddle', 'Western show saddle', 'Ranch saddle'],
 'Australian stock saddle': ['Swinging-fender stock saddle', 'Cross-breed saddle'],
 'Stirrup': ['Safety stirrup', 'Jointed stirrup', 'Icelandic stirrup', 'Side-saddle stirrup'],
 'Bridle': ['Snaffle bridle', 'Double bridle', 'Pelham bridle', 'Western headstall', 'Barcoo bridle', 'Halter bridle', 'Driving bridle'],
 'Snaffle bit': ['Loose-ring snaffle', 'Eggbutt snaffle', 'D-ring snaffle', 'Full-cheek snaffle', 'Half-cheek snaffle', 'Bradoon'],
 'Curb bit': ['Western curb'],
 'Gag bit': ['Running gag', 'Dutch gag', 'American gag'],
 'Bitless bridle': ['Sidepull', 'Jumping cavesson', 'Wheel hackamore'],
 'Headcollar': ['Working headcollar', 'Rope halter', 'Show halter', 'Breakaway headcollar'],
 'Driving harness': ['Breast-collar harness', 'Full-collar harness', 'Hybrid-collar harness'],
 'Turnout rug': ['Amigo turnout'],
 'Fly rug': ['Rambo fly rug', 'Amigo fly rug'],
 'Falconry hood': ['Moulded ultra-light hood'],
 'Falconry glove': ['Falcon glove', 'Hawk gauntlet', 'Eagle glove'],
 'Jesses and anklets': ['Traditional jesses', 'False Aylmeri'],
 'Falconry perch': ['Block perch', 'Bow perch', 'Ring perch', 'Screen perch', 'Shelf perch'],
 'Hawking bag and vest': ["Falconer's bag", 'Hawking vest'],
 'Falconry telemetry': ['Radio transmitter and receiver', 'GPS falconry tracker'],
 'Pigeon timing system': ['Mechanical printing pigeon clock'],
 'Vivarium': ['Wooden vivarium', 'PVC reptile enclosure', 'Paludarium', 'Bioactive vivarium'],
 'Reptile food': ['Crested gecko meal-replacement powder'],
 'Invertebrate enclosure': ['Acrylic tarantula enclosure'],
 'Formicarium': ['Ytong formicarium'],
 'Framed vertical hive': ['Polystyrene hive'],
 'Beekeeping suit and veil': ['Apiarist suit'],
 'Bee smoker': ['Bellows smoker'],
 'Hive tool': ['Standard hive tool', 'J-hook hive tool'],
 'Honey extractor': ['Tangential extractor', 'Radial extractor'],
}
for kn, names in D.items(): demote(kn, names)
# ranges for demoted maker lines
def addr(kn, pair):
    r = K[kn].setdefault('r', [])
    if pair not in r: r.append(pair)
addr('Turnout rug', ['Amigo', 'Horseware Ireland'])
addr('Fly rug', ['Rambo fly sheets', 'Horseware Ireland']); addr('Fly rug', ['Amigo fly sheets', 'Horseware Ireland'])
addr('Falconry hood', ['Moulded ultra-light hood', 'High-Tech Falconry'])
addr('Hawking bag and vest', ['Hawking vest', 'Pineo Falconry Furniture'])
addr('Beekeeping suit and veil', ['Apiarist suit', 'BJ Sherriff'])
addr('Vivarium', ['Wooden vivarium', 'Vivexotic']); addr('Vivarium', ['PVC reptile enclosure', 'Kages'])
addr('Reptile food', ['Crested gecko diet', 'Repashy'])
addr('Invertebrate enclosure', ['Tarantula enclosures', 'Tarantula Cribs'])
addr('Dog bed', ['Calming donut bed', 'Best Friends by Sheri'])
addr('Dog crate', ['Folding wire crate', 'MidWest Homes for Pets']); addr('Dog crate', ['Plastic airline kennel', 'Petmate'])
# Rambo turnout rename keeps; Sandwich ant farm -> Janet nest
for x in K['Formicarium']['x']:
    if x['n'] == 'Sandwich ant farm':
        x['n'] = 'Janet nest'; x['a'] = 'sandwich ant farm · Ant Farm'; x['mk'] = 'Charles Janet'
# Acme whistle: add Box clicker note none

# ---------- new kinds (all sourced from pages fetched this session) ----------
WIKI = 'https://en.wikipedia.org/wiki/'
HT = WIKI + 'Horse_tack'; MA = 'https://www.themodernapprentice.com/gen_equipment.htm'
ML = 'https://www.mannlakeltd.com/hives-components/hive-accessories/'
PS = 'https://www.petsmart.com/'
NEW = [
 ('Noseband', 'cavesson · flash · drop noseband', 'A strap round the horse\'s nose, part of the bridle, that steadies the bit or closes the mouth.', HT),
 ('Spurs', 'English spurs · Western spurs', 'Metal aids worn on the rider\'s heel to refine a leg signal.', HT),
 ('Riding whip and crop', 'crop · quirt · schooling whip', 'A handheld aid carried to reinforce the rider\'s leg, from a short jumping crop to a long dressage whip.', HT),
 ('Stirrup leather', 'stirrup strap', 'The strap that hangs a stirrup iron from the saddle.', HT),
 ('Horseshoe', 'horse shoe', 'A metal or synthetic shoe fixed to a horse\'s hoof by a farrier to protect it.', HT),
 ('Hoof boot', 'horse boot (hoof)', 'A boot that fits over a horse\'s hoof, worn instead of a shoe or to protect a treated foot.', HT),
 ('Creance', 'training line', 'A long, light, non-stretch line fixed to a raptor\'s jesses to train it to fly back before it is flown free.', MA),
 ('Falconry scale', 'hawk scale · weighing perch', 'A scale, often a perch on a balance, that weighs a raptor each day to judge its condition.', MA),
 ('Cadge', 'hawk cadge', 'A frame on which several raptors are carried to the field.', WIKI + 'Falconry'),
 ('Mews', 'hawk house · moulting shed', 'A shed or room where raptors are housed, especially while they moult.', WIKI + 'Falconry'),
 ('Hive stand', 'beehive stand', 'A frame or platform that lifts a hive off the ground, away from damp and pests.', ML),
 ('Entrance reducer and mouse guard', 'entrance reducer · mouse guard · entrance cleat', 'A strip or grille that narrows a hive entrance so a small colony can defend it and mice stay out.', ML),
 ('Bee escape', 'escape board · escape screen', 'A one-way board or screen that lets bees leave a honey box but not return, to clear it for harvest.', ML),
 ('Hive floor, crown board and roof', 'bottom board · inner cover · hive cover', 'The base, the board over the top box and the roof that complete a framed hive.', WIKI + 'Beekeeping'),
 ('Observation hive', 'glass-walled hive', 'A small hive with glass sides that lets the colony be watched at work, usually indoors.', WIKI + 'Beekeeping'),
 ('Honey jar', 'honey container', 'A glass or plastic jar in which honey is stored and sold.', WIKI + 'Beekeeping'),
 ('Beekeeping gloves', 'bee gloves', 'Gloves with long cuffs that protect the beekeeper\'s hands and wrists from stings.', WIKI + 'Beekeeping'),
 ('Pond skimmer', 'surface skimmer · koi pond skimmer', 'A unit set at the pond edge that draws floating debris and dust from the surface into a basket.', 'https://www.cotswoldkoi.co.uk/?p=67650'),
 ('Pond de-icer', 'pond heater', 'A floating or immersed heater that keeps a hole open in the ice so a winter pond can exchange gas.', 'https://www.liveaquaria.com/collections/pond-supplies?page=3'),
 ('Pond vacuum', 'pond cleaner', 'A vacuum or siphon that lifts sludge and debris from the floor of a pond.', 'https://www.liveaquaria.com/collections/pond-supplies?page=3'),
 ('Aquarium hood and lid', 'tank lid · glass cover · canopy', 'A hood, glass lid or mesh cover that closes the top of a tank, often carrying lights.', WIKI + 'Aquarium'),
 ('Aquarium thermometer', 'tank thermometer', 'A thermometer, glass, adhesive-strip or digital, that shows the temperature of the tank water.', WIKI + 'Aquarium'),
 ('Vivarium stand', 'terrarium stand', 'A cabinet or frame that carries an enclosure at a convenient height.', PS + 'reptile/'),
 ('Reptile climbing décor', 'branch · vine · basking platform', 'Branches, vines, platforms and backgrounds that give a reptile something to climb and bask on.', PS + 'reptile/'),
 ('Reptile bowl', 'water dish · feeding dish', 'A shallow dish from which a reptile drinks or eats.', PS + 'reptile/'),
 ('Small-animal chew', 'gnawing block · chew stick', 'A block, stick or hay-based treat that rabbits and rodents gnaw to wear down their teeth.', PS + 'small-pet/'),
 ('Chicken nesting box', 'nest box (hens) · laying box', 'A box in the coop where a hen lays, sometimes rolling the egg out to a tray.', 'https://www.bobvila.com/articles/essentials-for-raising-backyard-chickens/'),
 ('Poultry grit and oyster shell', 'chicken grit · layer shell', 'Grit that helps a hen grind food, and crushed oyster shell that supplies calcium for eggshell.', 'https://www.bobvila.com/articles/essentials-for-raising-backyard-chickens/'),
]
for n, a, dd, s in NEW:
    assert n not in K, n
    K[n] = dict(n=n, a=a, d=dd, s=s); LOG['added'].append(n)

# ---------- cross-links ----------
SEE = {
 'Dog crate': [('B10', 'Pet carrier', 'carrier for a small dog or cat')],
 'Pet carrier': [('B10', 'Dog crate', 'larger box for a dog at home or in a car')],
 'Dog harness': [('B10', 'Cat harness and lead', 'the same idea sized for cats')],
 'Cat harness and lead': [('B10', 'Dog harness', 'the same idea sized for dogs')],
 'Dog bed': [('B10', 'Cat bed', 'beds made for cats')], 'Cat bed': [('B10', 'Dog bed', 'beds made for dogs')],
 'Dog car restraint': [('B10', 'Pet carrier', 'a carrier belted into the car')],
 'Dog collar': [('B10', 'Pet ID tag', 'tag worn on the collar'), ('B10', 'Dog head halter', 'a head collar steers the head')],
 'Dog head halter': [('B10', 'Dog collar', 'collars sit on the neck'), ('B10', 'Headcollar', 'the horse headcollar it was modelled on')],
 'Pet ID tag': [('B10', 'GPS pet tracker', 'finds a lost pet by location')],
 'Pet pen': [('B10', 'Rabbit and guinea-pig run', 'run built for rabbits and guinea pigs')],
 'Rabbit and guinea-pig run': [('B10', 'Pet pen', 'foldable panels for dogs and small pets')],
 'Cat litter': [('B10', 'Small-animal bedding', 'loose material for small mammals')],
 'Small-animal bedding': [('B10', 'Cat litter', 'loose absorbent material for cats')],
 'Small-animal food': [('B10', 'Hay', 'hay as feed for horses and small animals')],
 'Hay': [('B10', 'Small-animal food', 'feeding hay for rabbits and guinea pigs')],
 'Snaffle bit': [('B10', 'Bitless bridle', 'steering without a bit')],
 'Bitless bridle': [('B10', 'Snaffle bit', 'a bit that works by direct rein pressure')],
 'Bridle': [('B10', 'Noseband', 'noseband is a part of the bridle')],
 'Noseband': [('B10', 'Bridle', 'the headgear it is fitted to')],
 'Stirrup': [('B10', 'Stirrup leather', 'the strap that hangs it')],
 'Stirrup leather': [('B10', 'Stirrup', 'the iron on the strap')],
 'Turnout rug': [('B10', 'Fly rug', 'light rug for summer turnout')],
 'Fly rug': [('B10', 'Turnout rug', 'waterproof rug for the field')],
 'Horseshoe': [('B10', 'Hoof boot', 'a boot that takes the place of a shoe')],
 'Hoof boot': [('B10', 'Horseshoe', 'a shoe nailed or glued to the hoof')],
 'Lunge line': [('B10', 'Lungeing cavesson', 'headpiece the line clips to')],
 'Aquarium filter': [('B10', 'Pond filter', 'filter for a garden pond')],
 'Pond filter': [('B10', 'Aquarium filter', 'filter for an indoor tank')],
 'Aquarium heater': [('B10', 'Pond de-icer', 'heater for a winter pond')],
 'Pond de-icer': [('B10', 'Aquarium heater', 'heater for an indoor tank')],
 'Aquarium net': [('B10', 'Koi net and bowl', 'larger nets for koi')],
 'Koi net and bowl': [('B10', 'Aquarium net', 'nets for tank fish')],
 'Fish food': [('B10', 'Koi and pond fish food', 'pellets for pond fish')],
 'Koi and pond fish food': [('B10', 'Fish food', 'flake and pellet food for tank fish')],
 'Aquarium air pump': [('B10', 'Pond aerator', 'air pump for a pond')],
 'Pond aerator': [('B10', 'Aquarium air pump', 'air pump for a tank')],
 'Pond pump': [('C2', 'Pond pump', 'same pump sold for garden water features')],
 'Platform feeder': [('B4', 'Bird bath', 'a bird bath is listed with garden ornaments')],
 'Wild bird nest box': [('B10', 'Cage-bird nest box', 'nest box fitted in a cage or aviary')],
 'Cage-bird nest box': [('B10', 'Wild bird nest box', 'nest box hung for wild birds')],
 'Chicken coop': [('B10', 'Chicken nesting box', 'laying box inside the coop')],
 'Small egg incubator': [('B10', 'Brooder heating plate', 'keeps the chicks warm after hatching')],
 'Brooder heating plate': [('B10', 'Small egg incubator', 'hatches the eggs first')],
 'Reptile thermostat': [('B10', 'Reptile heat mat', 'heat source it controls')],
 'Reptile heat mat': [('B10', 'Reptile thermostat', 'control for the mat')],
 'Honey jar': [('B10', 'Honey bottling bucket or tank', 'where honey is settled before jarring')],
 'Hive body': [('B10', 'Framed vertical hive', 'the whole hive it forms part of')],
 'Falconry glove': [('B10', 'Jesses and anklets', 'straps the glove holds')],
 'Creance': [('B10', 'Falconry lure', 'lure used once the bird is flown free')],
}
SEE_OTHER = {'C2': 'Pond pump', 'B4': 'Bird bath'}
for c, kn in SEE_OTHER.items():
    names = {k['n'] for dp in json.load(open(R + f'reader/{c}.json'))['depts'] for s in dp['s'] for k in s['k']}
    assert kn in names, (c, kn)
for kn, lst in SEE.items():
    assert kn in K, kn
    for c, tn, why in lst:
        if c == 'B10': assert tn in K, (kn, tn)
    K[kn]['see'] = [list(x) for x in lst]

# ---------- tt ----------
missing = []
for kn, k in K.items():
    if kn in KT:
        k['tt'] = [[lab, [x.strip() for x in items.split(';') if x.strip()]] for lab, items in KT[kn]]
        k.pop('t', None)
    elif k.get('t'):
        missing.append(kn)
extra = [n for n in KT if n not in K]
assert not missing, missing
assert not extra, extra

# ---------- assemble ----------
oldb = {dp['n']: dp for dp in d['depts']}
oldA = oldb['Aquariums & ponds']
placed = set(); out_depts = []
for dn, mode, t, ax, shelves in DEPTS:
    dp = {'n': dn, 'mode': mode, 't': t, 'ax': ax}
    src_dp = oldb.get(dn) or (oldA if dn in ('Aquariums', 'Ponds & koi') else None)
    if dn == 'Small animals & backyard poultry' or dn in oldb:
        pass
    if dn == 'Reptiles, amphibians & invertebrates' or dn in oldb:
        pass
    if src_dp:
        if dn in oldb and src_dp.get('note'): dp['note'] = src_dp['note']
        bl = src_dp.get('b') or []
        if dn == 'Aquariums': bl = [b for b in bl if not re.search(r'pond|koi', json.dumps(b), re.I)]
        if dn == 'Ponds & koi': bl = [b for b in bl if re.search(r'pond|koi', json.dumps(b), re.I)]
        if bl: dp['b'] = bl
    if dn == 'Aquariums': dp['note'] = 'Tier for basic kit; variety for aquascaping and reef keeping.'
    if dn == 'Ponds & koi': dp['note'] = 'Tier for pumps and filters; variety for koi keeping.'
    dp['s'] = []
    for sn, st, sax, kinds in shelves:
        sh = {'n': sn, 't': st}
        if len(kinds) > 3: sh['ax'] = sax
        else: sh['ax'] = sax
        sh['k'] = []
        for kn in kinds:
            assert kn in K, kn
            assert kn not in placed, kn
            placed.add(kn); sh['k'].append(K[kn])
        dp['s'].append(sh)
    out_depts.append(dp)
left = [k for k in K if k not in placed]
assert not left, left
d2 = dict(c='B10', rev=True, lead=d['lead'], b=d.get('b', []), ax=CAT_AX, key=CAT_KEY, depts=out_depts)
for k0 in d:
    if k0 not in d2 and k0 != 'depts': d2[k0] = d[k0]
json.dump(d2, open('/home/user/Possession-Taxonomy/rebuild/work/STR_B10/B10.new.json', 'w'), ensure_ascii=False, indent=1)
after = dict(depts=len(out_depts), shelves=sum(len(dp['s']) for dp in out_depts), kinds=len(K), arch=sum(len(k.get('x', [])) for k in K.values()))
print('before', before, 'after', after)
json.dump(dict(before=before, after=after, log=LOG), open('/home/user/Possession-Taxonomy/rebuild/work/STR_B10/log.json', 'w'), ensure_ascii=False, indent=1)
