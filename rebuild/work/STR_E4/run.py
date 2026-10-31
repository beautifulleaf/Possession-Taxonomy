import json, copy, os, sys
ROOT = '/home/user/Possession-Taxonomy/rebuild'
old = json.load(open(ROOT + '/work/STR_E4/bak/E4.json'))
K = {}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k
USED = set()
WIKI = 'https://en.wikipedia.org/wiki/'

def mod(name, new_name=None, a=None, d=None, tt=None, drop_x=(), add_x=(), m=None, r=None, see=None, s=None, keep_x=None, x_order=None):
    k = copy.deepcopy(K[name]); USED.add(name)
    if new_name: k['n'] = new_name
    if a is not None: k['a'] = a
    if d is not None: k['d'] = d
    if s is not None: k['s'] = s
    k.pop('t', None)
    if tt is not None: k['tt'] = tt
    if drop_x or keep_x is not None:
        xs = []
        for x in k.get('x', []):
            if x['n'] in drop_x: continue
            if keep_x is not None and x['n'] not in keep_x: continue
            xs.append(x)
        k['x'] = xs
    if add_x:
        k['x'] = list(k.get('x', [])) + list(add_x)
    if x_order:
        by = {x['n']: x for x in k['x']}
        k['x'] = [by[n] for n in x_order if n in by] + [x for x in k['x'] if x['n'] not in x_order]
    if m is not None: k['m'] = m
    if r is not None: k['r'] = r
    if see: k['see'] = see
    for key in ('x', 'm', 'r'):
        if key in k and not k[key]: k.pop(key)
    return k

def nk(n, d, s, a='', tt=None, x=None, m=None, see=None, r=None):
    k = {'n': n, 'a': a, 'd': d, 's': s}
    if tt: k['tt'] = tt
    if x: k['x'] = x
    if m: k['m'] = m
    if r: k['r'] = r
    if see: k['see'] = see
    return k

def X(n, d, s, y='', mk='', dt=None):
    x = {'n': n, 'a': '', 'd': d, 'mk': mk, 'y': y, 's': s, 'v': []}
    if dt: x['dt'] = dt
    return x

def xold(kind, name):
    for x in K[kind]['x']:
        if x['n'] == name: return copy.deepcopy(x)
    raise KeyError((kind, name))

def moved_x(kind, names):
    return [xold(kind, n) for n in names]

def S(n, t, ax, kinds):
    s = {'n': n, 't': t}
    if ax: s['ax'] = ax
    s['k'] = kinds
    return s

def D(n, mode, t, ax, shelves, note=None, b=None):
    dp = {'n': n, 'mode': mode, 't': t, 'ax': ax}
    if note: dp['note'] = note
    if b: dp['b'] = b
    else:
        od = [x for x in old['depts'] if x['n'] == n]
        if od and od[0].get('b'): dp['b'] = od[0]['b']
    dp['s'] = shelves
    return dp

AGE = ['Age and making']
def age_tt(extra=None, labels=None):
    g = [['Age and making', ['Antique (kotō, shintō, shinshintō)', 'Gendaitō', 'Shinsakutō (licensed smith, since 1953)', 'Production replica']]]
    return (extra or []) + g

depts = []

def OD(n):
    return [x for x in old['depts'] if x['n'] == n][0]

# ================= SWORDS =================
AM = age_tt
eu = [
 mod('Short sword', a='gladius · xiphos · shortsword', d='Straight double-edged one-handed sword with a blade clearly shorter than an arming sword, as used in classical Greece and Rome.'),
 nk('Spatha', 'Long straight Roman sword of the 1st to 6th centuries, first a cavalry weapon and later the standard infantry sword; the ancestor of the Viking and knightly swords.', WIKI + 'Spatha', a='Roman long sword',
    tt=[['Era', ['Roman Imperial', 'Migration Period', 'Byzantine']]]),
 mod('Viking sword'),
 mod('Arming sword'),
 mod('Falchion'),
 nk('Katzbalger', 'Short, sturdy arming sword with an S-shaped or figure-eight guard, carried by the German Landsknecht mercenaries in the 16th and 17th centuries.', WIKI + 'Katzbalger', a='Landsknecht sword',
    x=[X('Landsknecht Katzbalger', 'Broad flat-bladed sword of 70-80 cm with a figure-eight guard, the signature sidearm of the Landsknechte.', WIKI + 'Katzbalger', y='16th-17th century')]),
 mod('Longsword', see=[['E2', 'HEMA training sword', 'blunt sparring copy']]),
 mod('Greatsword'),
 mod('Estoc', tt=[['Grip', ['Two-handed', 'One-handed']]]),
 mod('Basket-hilted broadsword', tt=[['Edges', ['Double-edged broadsword', 'Single-edged backsword']]]),
 mod('Rapier'),
 mod('Smallsword', tt=[['Blade', ['Triangular hollow-ground', 'Colichemarde (wide at the forte)']], ['Hilt', ['Shell guard', 'Ceremonial cross-hilt']]]),
 mod('Sabre'),
 mod('Cutlass'),
]
ja_age = [['Age and making', ['Antique (kotō, shintō, shinshintō)', 'Gendaitō', 'Shinsakutō (licensed smith, since 1953)', 'Production replica']]]
ja = [
 mod('Ōdachi'),
 mod('Tachi', tt=[['Size', ['Tachi', 'Kodachi (short tachi)']]] + ja_age),
 mod('Katana', tt=ja_age, drop_x=['Shinsakutō katana'], see=[['E2', 'Bokken', 'wooden practice sword']]),
 mod('Wakizashi', tt=[['Size', ['Ō-wakizashi', 'Ko-wakizashi']]] + ja_age),
 mod('Tantō', tt=[['Blade form', ['Hira-zukuri (flat)', 'Yoroi-dōshi (armour-piercing)', 'Kaiken (short carried dagger)']], ['Mount', ['Aikuchi (guardless)']]] + ja_age),
 mod('Ken (tsurugi)', drop_x=['Bronze tsurugi', 'Iron tsurugi', 'Offering tsurugi'], tt=[['Material and use', ['Bronze', 'Iron', 'Shrine offering']]]),
 mod('Iaitō', tt=[['Blade material', ['Aluminium-zinc alloy', 'Steel']]], see=[['E2', 'Bokken', 'wooden practice sword']]),
]
asia = [
 mod('Jian', drop_x=['Shuangshou jian', 'Taijijian', 'Wushu jian'],
     tt=[['Material', ['Bronze', 'Steel']], ['Grip', ['One-handed', 'Two-handed (shuangshou jian)']], ['Use', ['Combat', 'Wushu performance', 'Taijijian (tai chi)']]]),
 mod('Dao (Chinese sabre)'),
 mod('Khanda', tt=[['Grip', ['One-handed', 'Two-handed']]]),
 mod('Talwar', drop_x=['Classic talwar'], tt=[['Form', ['Classic talwar']]]),
 mod('Shamshir', drop_x=['Classic shamshir'], tt=[['Form', ['Classic shamshir']]]),
 mod('Kilij', drop_x=['Ottoman kilij', 'Early Turkic kilij'], tt=[['Era', ['Early Turkic', 'Ottoman']]]),
 mod('Yataghan', drop_x=['Balkan yataghan', 'Anatolian yataghan'], tt=[['Region', ['Balkan', 'Anatolian']]]),
 mod('Dha'),
 mod('Kampilan'),
 mod('Takoba'),
 mod('Shotel'),
]
guard = mod('Sword guard', a='cross guard · quillon block', d='Loose guard for a European or other sword hilt, sold apart from the blade; the Japanese form is the tsuba.', drop_x=[x['n'] for x in K['Sword guard']['x']], m=[])
tsuba = mod('Sword guard', new_name='Tsuba', a='Japanese sword guard', d='Japanese sword guard of iron or soft metal, collected as an art object by school and maker.',
            tt=[['Size', ['Katana size (c. 7.5-8 cm)', 'Wakizashi size', 'Tantō size']], ['Material', ['Iron', 'Soft metal (shakudō, shibuichi, copper, brass)']]])
tsuba['m'] = [['Tsuba', '']] if False else []
tsuba.pop('m')
scab = mod('Scabbard', a='sheath', d='Sheath for a European or other sword or knife; the Japanese form is the saya.', drop_x=['Saya', 'Shirasaya'], m=[],
           tt=[['Material', ['Wood covered in leather or fabric', 'Leather with chape and locket', 'Steel or brass', 'Polymer (Kydex)']]])
saya = mod('Scabbard', new_name='Saya', a='Japanese scabbard · koshirae mount', d='Japanese scabbard of lacquered or plain wood, made in a mounting style for the blade.',
           keep_x=['Shirasaya'], m=[], tt=[['Material', ['Lacquered wood', 'Plain wood']], ['Mounting style', ['Tachi koshirae', 'Han-dachi', 'Aikuchi']]])
tosogu = [
 mod('Habaki'),
 tsuba,
 mod('Fuchi-kashira'),
 mod('Menuki'),
 saya,
 mod('Kozuka and kōgai', tt=[['Fitting', ['Kozuka', 'Kōgai']]]),
]
swords = D('Swords', 'variety',
 'Swords and sword fittings of any age, antique, modern-made or replica; a polearm → Polearms, axes & martial arts weapons; a dagger or knife → Knives & daggers; a sword that cannot cut → Militaria & replicas.',
 'Which tradition made it (European, Japanese or other), and is it a whole blade or a fitting sold apart?',
 [
  S('European swords', 'Straight and curved swords of Europe from Roman times to the 18th century, such as the arming sword, longsword, rapier and sabre; Asian blades → their own shelves.',
    'kinds by the period they were carried, earliest first', eu),
  S('Japanese swords (nihontō)', 'Blades made in the Japanese tradition, such as the katana, tachi, wakizashi and tantō; Japanese fittings → Japanese sword fittings.',
    'kinds by blade length, longest first, then the straight ancient ken and the unsharpened practice iaitō', ja),
  S('Swords of Asia, Africa & the Middle East', 'Swords of China, India, the Middle East, Southeast Asia and Africa, such as the jian, talwar, kilij and takoba; Japanese blades → Japanese swords.',
    'kinds by region, from China westwards through India and the Middle East to Southeast Asia and Africa', asia),
  S('Sword guards & scabbards', 'Loose guards and sheaths for European and other swords; the Japanese equivalents → Japanese sword fittings.', None, [guard, scab]),
  S('Japanese sword fittings (tosogu)', 'Loose metal and wooden fittings of a Japanese sword, such as the tsuba, fuchi-kashira and menuki, collected by school and maker.',
    'kinds by position on the sword, from the blade collar to the scabbard', tosogu),
 ], note=OD('Swords').get('note'))
depts.append(swords)

# ================= KNIVES =================
dag_src = WIKI + 'List_of_daggers'
dagger = mod('Dagger', a='poniard', d='Short double-edged thrusting blade with a hilt; named European and Asian forms are collected by period and region.',
  add_x=[X('Misericorde', 'Slender medieval dagger used to give a mortal wound to a fallen knight.', dag_src, y='Middle Ages'),
         X('Cinquedea', 'Broad, short Italian Renaissance dagger shaped like a wide tapering blade.', dag_src, y='Renaissance'),
         X('Ear dagger', 'European dagger whose pommel is formed of two disc-like lobes.', dag_src, y='15th-16th century'),
         X('Parrying dagger', 'Left-hand dagger used with the rapier in 17th- to 18th-century fencing.', dag_src, y='17th-18th century'),
         X('Khanjali', 'Double-edged curved dagger of the Caucasus.', dag_src)],
  x_order=['Pugio', 'Rondel dagger', 'Baselard', 'Bollock dagger', 'Misericorde', 'Cinquedea', 'Ear dagger', 'Stiletto', 'Parrying dagger', 'Scottish dirk', 'Khanjar', 'Khanjali', 'Pesh-kabz', 'Fairbairn–Sykes fighting knife'])
bowie = mod('Bowie knife', a='fighting knife · combat knife', tt=[['Blade back', ['Plain', 'Sawback']]], drop_x=['Sawback survival Bowie'],
  add_x=[X('Arkansas toothpick', 'Long double-edged American fighting knife of the 19th century, related to the Bowie.', dag_src, y='19th century')])
push = mod('Push dagger', add_x=[X('Katar', 'Indian punch dagger with an H-shaped grip that places the blade above the knuckles; earliest forms link to 14th-century Vijayanagara.', WIKI + 'Katar', y='14th century')],
  x_order=['Katar'])
daggers_shelf = [dagger, mod('Seax'), bowie, mod('Trench knife'), mod('Kris', tt=[['Blade', ['Straight (lurus)', 'Wavy (luk)']]]), mod('Karambit', tt=[['Build', ['Fixed', 'Folding']]]), push]
hunting_shelf = [
 mod('Hunting knife', tt=[['Build', ['Fixed blade', 'Folding lockback']], ['Job', ['Skinning', 'Caping']]], see=[['C1', 'Fixed-blade EDC & bushcraft knife', 'general-use fixed blade']]),
 mod('Kukri', tt=[['Blade profile', ['Eastern (slim)', 'Western (broad)']]], see=[['C2', 'Machete', 'chopping blade for the garden']]),
 nk('Sgian-dubh', 'Small Scottish knife worn tucked into the top of the kilt hose with the hilt showing, part of Highland dress.', WIKI + 'Sgian-dubh', a='sgian dubh · skean dhu'),
]
bay_src = WIKI + 'Bayonet'
bay = [
 nk('Plug bayonet', 'Early bayonet pushed into the muzzle of a musket, which stopped the gun firing while it was fitted.', bay_src, a='muzzle plug bayonet'),
 mod('Bayonet', new_name='Socket bayonet', a='ring bayonet', d='Bayonet mounted round the barrel on a socket, so the gun can still be fired with it fitted.', drop_x=[x['n'] for x in K['Bayonet']['x']], tt=None,
     m=[['Mosin-Nagant M1891/30 bayonet', '']]),
]
sw_bay = [xold('Bayonet', n) for n in ['Pattern 1800 Baker sword bayonet', 'Seitengewehr 98', 'Type 30 bayonet', 'Pattern 1907 bayonet', 'US M1905 bayonet']]
sp_bay = [xold('Bayonet', 'Épée-Baïonnette Modèle 1886')]
kn_bay = [xold('Bayonet', n) for n in ['US M5/M6/M7 bayonets', 'M9 bayonet', 'AKM bayonet']]
bay += [
 nk('Sword bayonet', 'Long single- or double-edged bayonet that doubles as a short sword, made from the 18th century onward.', bay_src, x=sw_bay),
 nk('Spike bayonet', 'Bayonet with a long thin spike or quadrangular blade and no cutting edge, such as the French Lebel type.', bay_src, x=sp_bay),
 nk('Knife bayonet', 'Short knife-bladed bayonet issued after the Second World War, often with a scabbard that works as a wire cutter.', bay_src, a='bayonet · modern bayonet', x=kn_bay,
    tt=[['Blade back', ['Plain', 'Sawback']]], m=[['Mauser 98K bayonet', '']]),
]
trick = [
 mod('Throwing knife', tt=[['Balance', ['Balanced', 'Unbalanced', 'Adjustable-weight']]]),
 mod('Shuriken'),
 mod('Butterfly knife', tt=[['Handle', ['Sandwich', 'Channel']], ['Edge', ['Sharp', 'Blunt trainer']]]),
 mod('Automatic knife', tt=[['Opening', ['Side-opening (OTS)', 'Out-the-front double action', 'Out-the-front single action', 'Gravity (falls open)']]]),
]
knives = D('Knives & daggers', 'mixed',
 'Daggers, fighting, hunting and dress knives, bayonets and thrown or flicked blades; an everyday or bushcraft knife → C1, a kitchen knife → B5, a sword → Swords, a polearm → Polearms.',
 'What was the blade made to do: thrust and fight, work in the field, fit to a gun, or be thrown or flicked?',
 [
  S('Daggers & fighting knives', 'Blades made for close combat, such as the dagger, Bowie knife, kris and push dagger; a hunting knife → Hunting, field & dress knives.',
    'kinds by blade form and grip, from the straight thrusting dagger to curved and fist-held blades', daggers_shelf),
  S('Hunting, field & dress knives', 'Knives for dressing game, chopping or wearing with dress, such as the hunting knife, kukri and sgian-dubh; a general-use knife → C1.', None, hunting_shelf),
  S('Bayonets', 'Blades made to fix to the muzzle of a gun, from the plug and socket bayonets of the 17th century to modern knife bayonets.',
    'kinds by how the blade is built and fixed, oldest first', bay),
  S('Throwing & trick knives', 'Blades thrown or opened by a flick, spring or swing, such as the throwing knife, shuriken, butterfly knife and automatic knife.',
    'kinds by how the blade is put to work, from thrown to flicked to spring-opened', trick),
 ], note=OD('Knives & daggers').get('note'))
depts.append(knives)

# ================= POLEARMS, AXES & MARTIAL ARTS =================
PA = WIKI + 'Polearm'
pol = [
 mod('Spear', drop_x=['Pike', 'Winged spear', 'Sarissa'], tt=[['Use', ['Thrusting', 'Throwing (javelin)']], ['Head', ['Leaf-shaped', 'Lance-point', 'Winged']]]),
 nk('Pike', 'Very long infantry spear held in massed ranks, used from the Macedonian sarissa to the 17th century.', PA, a='infantry pike · half-pike',
    x=[xold('Spear', 'Sarissa'), xold('Spear', 'Pike')]),
 mod('Partisan', drop_x=['Partisan'], tt=[['Use', ['Fighting', 'Ceremonial']]]),
 nk('Corseque', 'Polearm with a three-bladed head on a 6-8 ft haft, popular in Europe in the 16th and 17th centuries.', PA),
 mod('Glaive', tt=[['Form', ['Plain', 'With back hook (glaive-guisarme)']]]),
 nk('Fauchard', 'Polearm with a curved blade on a 6-7 ft pole, cutting on the convex side, used in Europe from the 11th to the 14th century.', PA),
 nk('Voulge', 'Polearm with a single- or double-edged tapering blade on a socket, used widely in France and Burgundy in the 15th century.', PA, a='vouge'),
 mod('Naginata', drop_x=['Koryū naginata', 'Shiai naginata'], tt=[['Use', ['Antique blade', 'Practice (iaidō)', 'Competition (shiai)']]],
     see=[['E2', 'Shinai', 'bamboo practice blade']] if False else None),
 mod('Guandao', drop_x=['Yanyuedao'], tt=[['Use', ['Practice (wushu)', 'Heavy testing weapon']]]),
 nk('Guisarme', 'Polearm with a pruning-hook blade on a spear-like shaft, used to pull knights from the saddle in Europe c. 1000-1400.', PA, a='guisarme · gisarme'),
 mod('Bill', drop_x=['English bill'], tt=[['Pattern', ['Black bill', 'Brown bill', 'Forest bill']]]),
 mod('Halberd', tt=[['Use', ['Fighting', 'Ceremonial']]]),
 mod('Poleaxe', drop_x=['Knightly poleaxe'], tt=[['Head', ['Axe head', 'Hammer head']]]),
 mod('Bardiche'),
]
axes = [
 mod('Battle axe', tt=[['Grip', ['One-handed', 'Two-handed']], ['Use', ['War', 'Throwing']]], see=[['C1', 'Axe', 'felling and splitting axe']]),
 mod('Tomahawk', drop_x=['Pipe tomahawk'], tt=[['Head', ['Trade', 'Pipe', 'Spike']], ['Use', ['Tactical', 'Throwing']]], see=[['C1', 'Axe', 'general-use axe']]),
 mod('Mace', drop_x=['Flanged mace'], tt=[['Head', ['Flanged', 'Knobbed', 'Spiked']]]),
 mod('War hammer', drop_x=['Long war hammer'], tt=[['Length', ['Long (polearm)', "Short (horseman's)"]]]),
 mod('Flail', drop_x=['Peasant flail', 'Military flail'], tt=[['Form', ['Short ball-and-chain', 'Long two-handed']], ['Origin', ['Peasant tool', 'Military']]]),
]
ma = [
 mod('Staff', drop_x=['Gun', 'Quarterstaff'], tt=[['Name by tradition', ['Bō', 'Gùn', 'Quarterstaff', 'Hanbō (short)']], ['Taper', ['Tapered', 'Non-tapered']], ['Material', ['Wood', 'Rattan', 'Carbon fibre (competition)']]]),
 mod('Jō', tt=[['Style', ['Jōdō', 'Aiki-jō']]]),
 mod('Escrima sticks', tt=[['Material', ['Rattan', 'Kamagong', 'Bahi', 'Fibreglass, plastic or aluminium']]]),
 mod('Tonfa', tt=[['Material', ['Oak', 'Polymer']]]),
 mod('Sai', drop_x=['Manji sai'], tt=[['Form', ['Standard', 'Manji sai']]]),
 mod('Kama', tt=[['Edge', ['Sharp', 'Blunt training (kata kai)']]], see=[['C2', 'Sickle', 'garden sickle']]),
 mod('Nunchaku', tt=[['Section', ['Octagonal', 'Round']], ['Joint', ['Cord (himo)', 'Chain (kusari)']], ['Use', ['Foam training']]]),
 mod('Three-section staff', tt=[['Material', ['Wood', 'Rattan or bamboo', 'Aluminium']]]),
 mod('Chain whip', tt=[['Sections', ['Nine-section', 'Seven-section', 'Three-section']]]),
 mod('Rope dart', tt=[['Form', ['Rope dart', 'Meteor hammer']]]),
]
polearms = D('Polearms, axes & martial arts weapons', 'variety',
 'Hand weapons of shaft, axe, mace or chain, from medieval polearms to martial arts training weapons; a sword → Swords, a blade without a shaft → Knives & daggers, a wooden practice sword → E2.',
 'How is the weapon built: a head on a long shaft, a striking head on a short haft, or sticks, blades and chains used in pairs or joined?',
 [
  S('Polearms', 'Weapons with a blade, point or axe head on a long shaft, such as the spear, halberd, glaive and naginata; a short-hafted axe → Axes, maces & hammers.',
    'kinds by head, from the plain point through single blades and hooks to the combined axe, spike and hook', pol),
  S('Axes, maces & hammers', 'Short-hafted weapons with a blade, club or hammer head, such as the battle axe, tomahawk, mace and war hammer; a felling axe → C1.',
    'kinds by head: blade, club head, hammer, or swinging head', axes),
  S('Martial arts weapons', 'Sticks, blades and chain weapons used in martial arts, such as the staff, escrima sticks, sai and nunchaku; a wooden practice sword → E2.',
    'kinds by build, from plain sticks through handled and bladed weapons to those joined by chain or cord', ma),
 ])
depts.append(polearms)

# ================= ARCHERY & SLINGS =================
BW = WIKI + 'Bow_(weapon)'
CB = WIKI + 'Crossbow'
bows = [
 mod('Longbow', tt=[['Build', ['Self bow (one stave)', 'Laminated']], ['Limb section', ['D-section (English)', 'Rectangular-section (American)']]]),
 mod('Flatbow', tt=[['Build', ['Wooden self bow', 'Laminated', 'Fibreglass']]]),
 mod('Yumi', tt=[['Material', ['Bamboo', 'Synthetic (laminated wood with fibreglass or carbon)']], ['Length', ['Daikyū (full length)', 'Hankyū (short)']]]),
 mod('Horse bow', tt=[['Build', ['Traditional horn-and-sinew', 'Modern laminated or fibreglass']], ['Draw', ['Thumb draw']]]),
 mod('Recurve bow', tt=[['Assembly', ['One-piece', 'Take-down']], ['Style', ['Olympic (ILF fitting)', 'Barebow', 'Hunting']]]),
 mod('Compound bow', tt=[['Cam system', ['Single cam', 'Hybrid cam', 'Dual cam', 'Binary cam']], ['Fit', ['Adult', 'Youth']]]),
]
xb = [
 mod('Historical crossbow', tt=[['Spanning', ['Hand-spanned', 'Windlass', 'Cranequin']]]),
 nk('Repeating crossbow', 'Chinese crossbow with a magazine on top that feeds bolts and is worked by a lever, known as the chu-ko-nu.', CB, a='chu-ko-nu · chuguo nu',
    x=[X('Chu-ko-nu', 'Lever-worked repeating crossbow of the Chu state, China.', CB, y='Warring States')]),
 nk('Pistol crossbow', 'Smallest crossbow, held in one hand, made from the Warring States period in China and again in early 19th-century Europe.', CB, a='hand crossbow'),
 mod('Recurve crossbow'),
 mod('Compound crossbow', tt=[['Limb layout', ['Standard limbs', 'Reverse-draw']]]),
]
xb[-1]['x'][0]['dt'] = 'cams turn on the rail (HeliCoil) · draw weight · speed'
other_l = [
 mod('Sling', drop_x=['Staff sling'], tt=[['Type', ['Hand sling', 'Staff sling']], ['Cord', ['Wool', 'Flax or hemp', 'Polyester']]]),
 nk('Atlatl', 'Hand-held lever that launches a dart or javelin faster than the arm alone, in use for some 30,000 years.', WIKI + 'Atlatl', a='spear-thrower · woomera',
    tt=[['Region of use', ['Woomera (Australia)', 'Estólica (Andes)', 'Nuqaq (Yup’ik)']]]),
 mod('Blowgun', tt=[['Calibre', ['.40', '.50', '.625']], ['Tube', ['Cane or bamboo', 'Metal or plastic']]]),
 mod('Slingshot', drop_x=['Wrist-braced slingshot'], tt=[['Bands', ['Flat bands', 'Latex tubing']], ['Frame', ['Natural wood fork', 'Metal or polymer frame', 'Wrist-braced']]]),
]
proj = [
 mod('Arrow', tt=[['Shaft material', ['Wood (e.g. cedar)', 'Bamboo or reed', 'Aluminium', 'Carbon', 'Aluminium-carbon']], ['Fletching', ['Feather', 'Plastic vane']]], see=[['E2', 'Quiver', 'carries the arrows']]),
 mod('Crossbow bolt', tt=[['Shaft', ['Carbon', 'Aluminium']], ['Nock', ['Plain', 'Lighted']]]),
 mod('Arrowhead', tt=[['Use', ['Field point', 'Target point', 'Judo point', 'Blunt']], ['Broadhead design', ['Fixed-blade', 'Mechanical', 'Hybrid']], ['Historical material', ['Stone or bronze']]]),
]
acc = [
 mod('Bowstring', tt=[['Construction', ['Flemish twist', 'Endless loop']], ['Fits', ['Bow', 'Crossbow', 'Compound cable']]]),
 mod('Release aid', tt=[['Trigger', ['Wrist trigger', 'T-handle', 'Thumb button', 'Back tension (hinge)', 'Resistance (tension)']], ['Attachment', ['Caliper jaw', 'Rope or D-loop']]],
     see=[['E2', 'Archery finger tab', 'fingers instead of a release aid']]),
 mod('Bow riser', tt=[['Bow style', ['Olympic recurve', 'Barebow', 'Hunting take-down']]]),
 mod('Arrow rest', tt=[['Design', ['Containment (brush)', 'Drop-away', 'Blade', 'Stick-on or shelf']]]),
 mod('Bow sight', tt=[['Pin layout', ['Fixed-pin', 'Slider (movable pin)', 'Single-pin']], ['Fits', ['Compound', 'Recurve target']]]),
 mod('Stabiliser', tt=[['Mount position', ['Front rod', 'Side rods', 'V-bar']], ['Use', ['Target', 'Hunting']]]),
]
archery = D('Archery & slings', 'mixed',
 'Muscle-powered launchers, the arrows and bolts they shoot, and fittings for bows; target butts, quivers and tabs → E2, a toy bow → E1, a firearm → Firearms.',
 'Is it the launcher, the projectile it shoots, or a fitting for the launcher?',
 [
  S('Bows', 'Hand-drawn bows, from the self-wood longbow and horse bow to the modern recurve and compound; a bow on a stock → Crossbows.',
    'kinds by limb shape and build, from the plain wooden bow to the cam-driven compound', bows),
  S('Crossbows', 'Bows mounted on a stock with a lock that holds the drawn string, from the medieval crossbow to modern recurve and compound types.',
    'kinds by build, from hand-spanned historical types to cam-driven modern ones', xb),
  S('Slings, slingshots & blowguns', 'Other hand-powered launchers: the sling, atlatl, blowgun and slingshot; a toy one is in Toys & Games.',
    'kinds by what powers the throw: whirled cord, lever arm, breath, elastic bands', other_l),
  S('Arrows, bolts & points', 'What a bow or crossbow shoots: arrows, crossbow bolts and the heads fitted to them.', None, proj),
  S('Bow accessories', 'Fittings that go on a bow or its string, such as the bowstring, release aid, riser, rest, sight and stabiliser; a quiver or arm guard → E2.',
    'kinds by where they fit on the bow, from the string to the front rod', acc),
 ], note=OD('Archery & slings').get('note'))
depts.append(archery)

# ================= FIREARMS =================
RF = WIKI + 'Rifle'
FL = WIKI + 'Flintlock'
mm_ml_pistol = nk('Muzzle-loading pistol', 'Single-shot handgun loaded with powder and ball from the muzzle, fired by flintlock or percussion lock.', FL, a='flintlock pistol · percussion pistol · duelling pistol',
    tt=[['Ignition', ['Flintlock', 'Percussion']]],
    x=[xold('Single-shot pistol', 'Philadelphia Deringer'),
       X('Queen Anne pistol', 'Flintlock pocket pistol with a cannon-shaped barrel and screw-off breech.', FL, y='18th century'),
       X('Duelling pistol', 'Matched flintlock or percussion pistol made in cased pairs for formal duels.', FL, y='18th-19th century')])
perc_rev = mod('Single-action revolver', new_name='Percussion revolver', a='cap-and-ball revolver', d='Revolver whose cylinder chambers are loaded with powder and ball and fired with percussion caps.',
    keep_x=['Colt 1851 Navy', 'Remington Model 1858'], tt=[['Frame', ['Open-top', 'Solid-frame']]])
perc_rev['tt'] = [['Ignition', ['Percussion cap']]]
perc_rev.pop('m', None)
blunder = nk('Blunderbuss', 'Muzzle-loading smoothbore with a short wide barrel and flared muzzle, loaded with multiple shot for close range, from the 17th to mid-19th century.', WIKI + 'Blunderbuss', a='dragon (pistol form)')
handguns = [
 mod('Single-shot pistol', a='derringer', d='Handgun with no magazine or cylinder, loaded by hand with a cartridge into one or two barrels.', drop_x=['Philadelphia Deringer'], tt=[['Action', ['Break-open']]]),
 mod('Single-action revolver', a='cowboy revolver', d='Handgun with a revolving cylinder whose hammer is cocked by hand before each shot, loaded with metallic cartridges.', drop_x=['Colt 1851 Navy', 'Remington Model 1858']),
 mod('Double-action revolver'),
 mod('Semi-automatic pistol', tt=[['Size', ['Full-size', 'Compact', 'Subcompact']], ['Firing mechanism', ['Striker-fired', 'Hammer-fired']]]),
]
rifles = [
 mod('Single-shot rifle', tt=[['Action', ['Falling block', 'Break action', 'Rolling block']]],
     add_x=[X('Snider–Enfield', 'British breech-loading conversion of the Enfield muzzle-loader to take metallic cartridges.', RF, y='1864')]),
 mod('Lever-action rifle',
     add_x=[X('Spencer repeating rifle', 'Lever-action repeater with a tube magazine in the butt, designed by Christopher Spencer.', RF, y='1860'),
            X('Winchester Model 1866', 'Lever-action rifle with a loading gate, the first to carry the Winchester name.', RF, y='1866')],
     x_order=['Spencer repeating rifle', 'Henry 1860', 'Winchester Model 1866', 'Winchester Model 1873', 'Winchester Model 1894', 'Marlin Model 336']),
 mod('Bolt-action rifle', tt=[['Bolt', ['Rotating bolt', 'Straight-pull']], ['Feed', ['Controlled-round feed', 'Push feed']]],
     add_x=[X('Dreyse needle gun', 'First military bolt-action breech-loader, firing a paper cartridge with a needle through the powder.', RF, y='1836'),
            X('Chassepot', 'French bolt-action needle rifle that out-ranged the Dreyse in 1866.', RF, y='1866'),
            X('Arisaka Type 30', 'Japanese bolt-action service rifle of the Russo-Japanese War era.', RF, y='1897')],
     x_order=['Dreyse needle gun', 'Chassepot', 'Mauser 98', 'Lee–Enfield', 'Mosin–Nagant', 'Arisaka Type 30', 'Springfield M1903', 'Winchester Model 70', 'Remington Model 700', 'Tikka T3', 'Blaser R8']),
 mod('Semi-automatic rifle', a='self-loading rifle'),
]
shotguns = [
 mod('Single-shot shotgun', tt=[['Action', ['Break-open', 'Bolt-action']]]),
 mod('Side-by-side shotgun', tt=[['Lock', ['Sidelock', 'Boxlock', 'Hammer gun']], ['Opening', ['Standard', 'Self-opening']]]),
 mod('Over-under shotgun', tt=[['Use', ['Field', 'Sporting', 'Trap', 'Skeet']]]),
 mod('Pump-action shotgun'),
 mod('Semi-automatic shotgun', tt=[['Operating system', ['Gas-operated', 'Inertia-operated', 'Recoil-operated']]]),
 mod('Combination gun', drop_x=['Drilling', 'Cape gun'], tt=[['Layout', ['Over-under', 'Drilling (three barrels)', 'Vierling (four barrels)', 'Cape gun (side-by-side)']]]),
]
muzz = [
 mm_ml_pistol, perc_rev, blunder,
 mod('Musket', a='flintlock musket', tt=[['Ignition', ['Matchlock', 'Flintlock', 'Percussion']]]),
 mod('Muzzle-loading shotgun', tt=[['Ignition', ['Flintlock', 'Percussion']]]),
 mod('Muzzle-loading rifle', tt=[['Ignition', ['Flintlock', 'Percussion', 'Inline']]],
     add_x=[X('Jäger rifle', 'German flintlock rifle for hunting and light infantry.', FL, y='18th century'),
            X('Jezail', 'Long flintlock rifle of Afghanistan, India, Central Asia and the Middle East.', FL),
            X('Pattern 1853 Enfield', 'British rifled percussion musket, the main infantry arm of the 1850s and 1860s.', RF, y='1853'),
            X('Springfield Model 1861', 'US rifled percussion musket of the Civil War.', RF, y='1861')]),
]
firearms = D('Firearms', 'mixed',
 'Sporting, collector and antique guns fired by burning powder, sorted by gun type; a gun that fires air or gas → Air guns, one made inert → Militaria & replicas, a blank-only pistol → Self-defence.',
 'Is it a handgun, a rifle or a shotgun, or does it load at the muzzle whatever its shape?',
 [
  S('Handguns', 'Cartridge guns held in one hand, such as semi-automatic pistols and revolvers; muzzle-loading pistols → Muzzle-loading guns.',
    'kinds by action, from the single-shot to the self-loading pistol', handguns),
  S('Rifles', 'Cartridge long guns with a rifled barrel, such as bolt-action, lever-action and semi-automatic rifles; muzzle-loaders → Muzzle-loading guns.',
    'kinds by action, from single-shot to self-loading', rifles),
  S('Shotguns & combination guns', 'Cartridge long guns with a smooth bore for shot, such as over-under and pump guns, and guns that join a rifle and a shotgun barrel.',
    'kinds by action and barrel layout, from the single-shot to the combination gun', shotguns),
  S('Muzzle-loading guns', 'Guns loaded with powder and ball from the muzzle, such as flintlock pistols, percussion revolvers, muskets and blunderbusses.',
    'kinds by gun type, from pistols through the short smoothbore to long guns', muzz),
 ], note=OD('Firearms').get('note'))
firearms['_after'] = None
del firearms['_after']

# ================= AIR GUNS =================
AG = WIKI + 'Air_gun'
def ax(kind, names): return [xold(kind, n) for n in names]
sp_rifle = mod('Air rifle', new_name='Spring-piston air rifle', a='springer · break-barrel air rifle · BB gun',
    d='Air rifle powered by a spring or gas ram in a piston that the user cocks by hand; sold for plinking, hunting and 10 m match shooting.',
    keep_x=['Daisy Red Ryder', 'Diana Model 27', 'Diana 34', 'Webley Service Mk II', 'Weihrauch HW 35', 'Weihrauch HW 80', 'Weihrauch HW 77', 'Weihrauch HW 97', 'BSA Meteor', 'Feinwerkbau 300'],
    m=[], tt=[['Cocking', ['Break-barrel', 'Underlever', 'Side-lever']], ['Spring', ['Steel spring', 'Gas ram']], ['Ammunition', ['Pellet', 'BB']], ['Use', ['Sporting', '10 m match']]])
pump_rifle = nk('Pneumatic air rifle', 'Air rifle that stores air in a reservoir by pumping a lever, multi-stroke or single-stroke, before each shot.', AG, a='pump air rifle · multi-pump rifle · single-stroke rifle',
    tt=[['Pumping', ['Multi-pump', 'Single-stroke']], ['Ammunition', ['Pellet', 'BB']]], x=ax('Air rifle', ['Daisy Model 25', 'Walther LG match air rifle']))
co2_rifle = nk('CO2 air rifle', 'Air rifle driven by carbon dioxide from a capsule or refillable reservoir; common as repeaters and replicas of military rifles.', AG, a='gas rifle',
    tt=[['Gas source', ['Disposable capsule', 'Refillable reservoir']]], m=[['SIG MPX PCC', 'Sig Sauer']])
pcp_rifle = nk('PCP air rifle', 'Air rifle fed from a high-pressure air tank filled to about 200-300 bar, giving many consistent shots; unregulated or regulated.', AG, a='pre-charged pneumatic rifle',
    tt=[['Regulation', ['Unregulated', 'Regulated']], ['Use', ['Sporting', '10 m match']]],
    x=ax('Air rifle', ['Feinwerkbau 700', 'Daystate Huntsman', 'Air Arms S400', 'FX Impact']),
    m=[['Diana Outlaw Gen2 Synthetic', 'Diana (Mayer & Grammelspacher)'], ['Diana Stormrider Sport', 'Diana (Mayer & Grammelspacher)'], ['Gamo Urban', 'Gamo'], ['Gamo Arrow SLT', 'Gamo'],
       ['Umarex Gauntlet 2 SL', 'Umarex'], ['Benjamin Armada Semi-Auto', 'Benjamin'], ['Air Venturi Avenge-XL', 'Air Venturi'], ['Webley & Scott Nemesis X', 'Webley & Scott'],
       ['Reximex Apex', 'Reximex'], ['Norica NTX 35', 'Norica'], ['Barra 270z', 'Barra Airguns']])
co2_rifle['see'] = [['E2', 'Airsoft gun', 'plastic-pellet sport gun']]
sp_pistol = nk('Spring-piston air pistol', 'Air pistol powered by a spring piston cocked by hand, usually by breaking the barrel.', AG, a='springer pistol', tt=[['Cocking', ['Break-barrel', 'Fixed-barrel']]])
pump_pistol = mod('Air pistol', new_name='Pneumatic air pistol', a='pump air pistol · multi-pump pistol · single-stroke pistol',
    d='Air pistol that stores air in a reservoir by pumping a lever, multi-stroke or single-stroke, before each shot.', m=[], r=[],
    tt=[['Pumping', ['Multi-pump', 'Single-stroke']]])
co2_pistol = nk('CO2 air pistol', 'Air pistol driven by carbon dioxide capsules, including replica revolvers and self-loaders and precision target guns.', AG, a='gas pistol',
    tt=[['Style', ['Replica revolver', 'Replica self-loader', 'Target']]],
    m=[['Crosman 2240', 'Crosman'], ['Umarex Steel Storm', 'Umarex'], ['Colt Defender', 'Umarex'], ['Crosman SNR357', 'Crosman'], ['Crosman Silhouette', 'Crosman']],
    see=[['E2', 'Airsoft gun', 'plastic-pellet sport gun']])
pcp_pistol = nk('PCP air pistol', 'Air pistol fed from a small high-pressure air tank, regulated or unregulated, for sporting and 10 m match shooting.', AG, a='pre-charged pneumatic pistol',
    tt=[['Regulation', ['Unregulated', 'Regulated']], ['Use', ['Sporting', '10 m match']]],
    m=[['Weihrauch HW44', 'Weihrauch'], ['Benjamin Marauder Pistol', 'Benjamin'], ['Hammerli AP20', 'Hammerli'], ['Air Venturi Comp10 Match', 'Air Venturi'], ['Hatsan Jet II', 'Hatsan'],
       ['Beeman 2027', 'Beeman'], ['AirForce TalonP', 'AirForce Airguns'], ['Reximex RP11', 'Reximex'], ['Diana Bandit', 'Diana (Mayer & Grammelspacher)']],
    r=[['Marauder', 'Benjamin']])
pump_pistol['m'] = []
pump_pistol.pop('m'); pump_pistol.pop('r', None)
air_ammo = [
 mod('Air-gun pellets', tt=[['Head shape', ['Wadcutter (match)', 'Domed', 'Pointed', 'Hollow point']], ['Form', ['Diabolo', 'Slug']]]),
 mod('Air-gun BBs', tt=[['Material', ['Steel', 'Copper-plated steel', 'Lead']]]),
 mod('CO2 capsule', tt=[['Size', ['8 g', '12 g', '88 g']]]),
]
airguns = D('Air guns', 'mixed',
 'Guns driven by compressed air or gas, with the pellets, BBs and gas they use; a gun that shoots plastic airsoft pellets → E2, a toy dart or water blaster → E1.',
 'Is it a rifle-format gun, a pistol-format gun, or ammunition and gas for them?',
 [
  S('Air rifles', 'Rifle-format guns that fire pellets or BBs by spring, pumped air, gas or a charged tank, from the Daisy BB gun to 10 m match rifles.',
    'kinds by how the power is made or stored: spring piston, pump, CO2 gas, pre-charged tank', [sp_rifle, pump_rifle, co2_rifle, pcp_rifle]),
  S('Air pistols', 'Handgun-format guns that fire pellets or BBs by spring, pumped air, gas or a charged tank.',
    'kinds by how the power is made or stored: spring piston, pump, CO2 gas, pre-charged tank', [sp_pistol, pump_pistol, co2_pistol, pcp_pistol]),
  S('Air-gun ammunition & gas', 'Pellets and BBs fired by air guns, and the gas capsules that drive CO2 guns.', None, air_ammo),
 ], note=OD('Air guns').get('note'))

# ================= AMMUNITION & RELOADING =================
HL = WIKI + 'Handloading'
carts = [mod('Rimfire cartridge'), mod('Centrefire handgun cartridge'), mod('Centrefire rifle cartridge'), mod('Shotshell', tt=[['Load', ['Birdshot', 'Buckshot', 'Slug']]])]
comps = [
 mod('Cartridge case', tt=[['Condition', ['New', 'Once-fired']], ['Plating', ['Brass', 'Nickel-plated']]]),
 mod('Primer', tt=[['Size', ['Small pistol', 'Large pistol', 'Small rifle', 'Large rifle', '209 shotshell']], ['Strength', ['Standard', 'Magnum']]]),
 mod('Smokeless powder', tt=[['Use', ['Pistol', 'Rifle', 'Shotshell']], ['Grain form', ['Ball', 'Extruded']]]),
 mod('Black powder', tt=[['Form', ['Loose', 'Pellets']]]),
 mod('Shotshell wad', tt=[['Material', ['Plastic', 'Fibre']]]),
 mod('Loose bullet', tt=[['Bullet design', ['Full metal jacket', 'Hollow point', 'Polymer tip', 'Match']]]),
 mod('Muzzle-loading projectile', a='round ball · conical · sabot', tt=[['Shape', ['Round ball', 'Conical', 'Sabot']]]),
]
dies = mod('Reloading die set', a='loading dies · sizing die · seating die · reloading die', m=list(K['Reloading die set'].get('m', [])) + [t for t in K['Reloading die'].get('m', []) if t not in K['Reloading die set'].get('m', [])],
    tt=[['Dies in set', ['2-die (bottleneck)', '3-die (straight-wall)', '4-die']], ['Die type', ['Carbide', 'Bushing / match']]])
USED.add('Reloading die')
equip = [
 nk('Case tumbler', 'Vibratory, rotary or ultrasonic cleaner that polishes fired cases with media before reloading.', HL, a='case cleaner', tt=[['Method', ['Vibratory (dry)', 'Rotary (wet)', 'Ultrasonic']]]),
 mod('Reloading press', tt=[['Type', ['Single-stage', 'Turret', 'Progressive', 'Shotshell press']]]),
 dies,
 nk('Case trimmer', 'Tool that cuts stretched cases back to the correct length.', HL, tt=[['Drive', ['Manual hand trimmer', 'Die-based', 'Powered']]]),
 nk('Priming tool', 'Hand-held or bench tool that seats a primer in a case outside the press.', HL, a='hand primer'),
 nk('Powder measure', 'Device that throws a set volume of powder, from a dipper to an adjustable measure, dispenser or trickler.', HL, a='powder dispenser · powder trickler', tt=[['Type', ['Dipper', 'Disc or bar measure', 'Electronic dispenser', 'Trickler']]]),
 nk('Powder scale', 'Scale that weighs powder charges and bullets, mechanical or digital.', HL, a='reloading scale', tt=[['Type', ['Mechanical', 'Digital', 'Digital with dispenser']]]),
 nk('Bullet puller', 'Tool that pulls a bullet from a loaded round, by inertia hammer or collet.', HL, a='kinetic puller', tt=[['Type', ['Inertia (hammer)', 'Collet']]]),
]
ammo = D('Ammunition & reloading', 'tier',
 'Finished ammunition, the components for loading it and the equipment to do so; a bow arrow → Archery & slings, an air-gun pellet → Air guns, a cartridge that is only a display piece → Militaria & replicas.',
 'Is it a finished round, a component to load one, or equipment for loading it?',
 [
  S('Cartridges & shells', 'Finished rounds sold by the box, such as 9mm Luger, .308 Winchester, .22 Long Rifle and shotgun shells.',
    'kinds by ammunition family, from the smallest rimfire to the shotshell', carts),
  S('Reloading components', 'Parts sold separately for loading rounds: cases, primers, powder, bullets and wads.',
    'kinds by the part of the round, in loading order: case, primer, powder, wad, projectile', comps),
  S('Reloading equipment', 'Presses, dies and measuring tools for loading rounds at home; the finished round → Cartridges & shells.',
    'kinds by loading step: clean, resize, trim, prime, charge, weigh, pull', equip),
 ])

# ================= OPTICS, PARTS & ACCESSORIES =================
GS = WIKI + 'Gun_sight'
sights = [
 nk('Iron sight', 'Metal front and rear aiming pieces fitted to the gun, in open notch or closed aperture form.', GS, a='open sights · aperture sight · tang sight', tt=[['Form', ['Open (notch)', 'Aperture (closed)']]]),
 nk('Laser sight', 'Device that projects a lit aiming point onto the target, mounted on a handgun or long gun.', GS, a='laser aiming module'),
 mod('Red-dot sight', tt=[['Build', ['Tube', 'Open reflex', 'Holographic']], ['Fitted to', ['Rifle or shotgun', 'Pistol']]]),
 nk('Red dot magnifier', 'Flip-aside magnifier placed behind a non-magnifying sight to add magnification.', GS, a='sight magnifier'),
 mod('Rifle scope', tt=[['Magnification', ['Fixed power', 'Variable power', 'Low-power variable (1x bottom end)']], ['Reticle plane', ['First focal plane', 'Second focal plane']], ['Reticle', ['Plain', 'Illuminated']], ['Optical build', ['Tube', 'Prismatic']]],
     see=[['E6', 'Spotting scope', 'handheld magnified viewing']]),
 mod('Night-vision and thermal sight', tt=[['Technology', ['Thermal', 'Digital night vision', 'Image-intensifier']], ['Form', ['Weapon sight', 'Clip-on', 'With laser rangefinder']]],
     see=[['E6', 'Night-vision viewer', 'handheld night viewer'], ['E6', 'Thermal-imaging viewer', 'handheld thermal viewer']]),
 mod('Scope mount', tt=[['Part', ['Rings', 'Bases', 'One-piece cantilever']], ['Fitting', ['Quick-detach', 'Picatinny', 'Dovetail']]]),
]
parts = [
 mod('Magazine', tt=[['Fits', ['Rifle', 'Pistol']], ['Form', ['Box', 'Drum']]]),
 mod('Firearm upgrade part', tt=[['Part', ['Barrel', 'Trigger', 'Front sight', 'Rear sight', 'Suppressor']]]),
]
support = [
 mod('Weapon light', tt=[['Fits', ['Pistol', 'Long gun']], ['Function', ['Light only', 'Light/laser combination']]], see=[['B3', 'Tactical flashlight', 'handheld torch']]),
 mod('Bipod', tt=[['Mount', ['Picatinny', 'M-Lok', 'Sling-stud']], ['Head', ['Swivel', 'Fixed']]]),
 mod('Shooting rest', tt=[['Part', ['Front rest', 'Rear bag', 'Lead sled']]]),
]
carry = [
 mod('Holster', tt=[['Carry position', ['Inside-the-waistband (IWB)', 'Outside-the-waistband (OWB)', 'Appendix', 'Shoulder', 'Ankle', 'Chest']], ['Fixing', ['Belt slide', 'Paddle', 'Pancake']]]),
 mod('Gun case', tt=[['Build', ['Hard case', 'Soft case', 'Gun slip', 'Pistol rug', 'Double-rifle case']]], see=[['B8', 'Gun safe', 'storage at home']]),
 mod('Gun cleaning kit', tt=[['Fits', ['Universal', 'Pistol', 'Rifle', 'Shotgun']], ['Method', ['Rod and brush', 'Pull-through']]]),
]
optics = D('Optics, parts & shooting accessories', 'mixed',
 'Sights, replacement parts and accessories for a gun; ear and eye protection → C1, a clay thrower or target → E2, binoculars and spotting scopes → E6.',
 'Does it aim the gun, change the gun itself, support and light it, or carry and care for it?',
 [
  S('Sights & mounts', 'Ways to aim a gun, from iron sights and red dots to magnified and night-vision scopes, with the mounts that hold them.',
    'kinds by how the aim is shown: iron, laser, reflex dot, magnified, night, then the mount', sights),
  S('Firearm parts', 'Parts that fit into the gun and change how it feeds or performs, such as magazines and replacement barrels or triggers.', None, parts),
  S('Lights, rests & supports', 'Accessories mounted on or used under a gun to light the target or steady the aim.', None, support),
  S('Holsters, cases & cleaning', 'Gear for carrying, storing and cleaning a gun; a gun safe at home → B8.', None, carry),
 ])

# ================= SELF-DEFENCE =================
SH = WIKI + 'Blackjack_(weapon)'
sprays = [
 mod('Pepper spray', tt=[['Form', ['Spray', 'Gel']]], see=[['B8', 'Personal attack alarm', 'noise-based alternative']]),
 mod('Pepper-ball launcher'),
 mod('Stun gun', tt=[['Delivery', ['Projectile (Taser-type)', 'Contact']]]),
]
strikers = [
 mod('Baton', tt=[['Build', ['Telescoping', 'Fixed']]]),
 mod('Kubotan'),
 nk('Blackjack', 'Short, easily hidden club with a dense weight on the end, also called a sap or cosh; the flat sap has an oval head.', SH, a='sap · cosh · slapjack', tt=[['Form', ['Cylindrical blackjack', 'Flat sap', 'Soft sap (shot-filled)']]]),
 nk('Knuckle duster', 'Hand weapon worn over the knuckles, made of brass, steel or other materials; versions with spikes or blades are knuckle knives.', WIKI + 'Knuckle_duster', a='brass knuckles · knucks'),
 mod('Sword cane', see=[['H2', 'Walking stick', 'plain walking stick'], ['A4', 'Fashion cane', 'dress cane without a blade']]),
]
bf = mod('Blank-firing pistol', tt=[['Cartridge', ['Blank', 'Irritant', 'Signal']]], see=[['E4', 'Semi-automatic pistol', 'live-firing equivalent'], ['E2', 'Flare pistol', 'signal use outdoors']])
selfdef = D('Self-defence', 'tier',
 'Devices carried to stop an attacker: sprays, electric devices, strikers and blank-firing pistols; a firearm → Firearms, a personal alarm → B8, body armour → Modern body armour.',
 'How does it stop an attacker: a chemical or electric charge, a blow, or noise and fright?',
 [
  S('Sprays & electric devices', 'Devices that disable by irritant or electric shock, such as pepper spray, pepper-ball launchers and stun guns.', None, sprays),
  S('Strikers & concealed blades', 'Hand-held tools that deliver a blow, such as batons, kubotans, blackjacks and knuckle dusters, and the cane that hides a blade.',
    'kinds by build, from the rigid baton and fist rod to the weighted club, knuckle weapon and hidden blade', strikers),
  S('Blank-firing pistols', 'Pistols that fire only blank, irritant or signal cartridges, made for self-defence or to scare; a live-firing pistol → Handguns.', None, [bf]),
 ])

# ================= ARMOUR & SHIELDS =================
CA = WIKI + 'Components_of_medieval_armour'
SHD = WIKI + 'Shield'
whole = [
 mod('Plate armour harness', tt=[['Purpose', ['Field', 'Tournament or jousting']], ['Coverage', ['Three-quarter', 'Full']], ['Set', ['Garniture (with pieces of exchange)']], ['Age', ['Antique', 'Reproduction']]],
     drop_x=['Three-quarter armour']),
 mod('Japanese armour', drop_x=['Kabuto', 'Menpō'], tt=[['Age', ['Antique', 'Edo-period revival', 'Reproduction']]]),
]
heads = [
 nk('Mail coif', 'Hood of interlinked metal rings covering the head and neck, worn alone or under a helmet.', CA, a='coif · camail'),
 mod('Plate helmet', new_name='Historical helmet', a='burgonet · bascinet · sallet',
     d='Metal helmet of a named historical form, from the spangenhelm and great helm to the sallet, armet and morion.',
     tt=[['Age', ['Antique', 'Reproduction']], ['Made for', ['Display or reenactment', 'Combat sport (buhurt)']]]),
 nk('Kabuto', 'Japanese helmet of riveted plates with a laminated neck guard (shikoro).', WIKI + 'Kabuto', a='Japanese helmet', tt=[['Age', ['Antique', 'Reproduction']]],
    ),
 nk('Menpō', 'Lacquered iron or leather face mask of Japanese armour, covering nose to chin and anchoring the kabuto.', WIKI + 'Men-yoroi', a='mempo · men-yoroi'),
]
for k in heads:
    if k['n'] == 'Kabuto': k['d'] = xold('Japanese armour', 'Kabuto')['d']; k['s'] = xold('Japanese armour', 'Kabuto')['s']
    if k['n'] == 'Menpō': k['d'] = xold('Japanese armour', 'Menpō')['d']; k['s'] = xold('Japanese armour', 'Menpō')['s']
torso = [
 mod('Gambeson', drop_x=['Gambeson'], tt=[['Fabric', ['Linen', 'Wool']], ['Sleeves', ['Sleeved', 'Sleeveless']]]),
 mod('Mail shirt', drop_x=['Hauberk', 'Haubergeon'], tt=[['Ring closure', ['Riveted', 'Butted']], ['Ring section', ['Flat', 'Round']]]),
 nk('Scale armour', 'Armour of many small overlapping plates attached to a cloth or leather backing, used from ancient Egypt to Joseon Korea.', WIKI + 'Scale_armour', a='lorica squamata · scale shirt'),
 nk('Lamellar armour', 'Armour of small plates laced to each other in horizontal rows with no backing, used across Asia and eastern Europe.', WIKI + 'Lamellar_armour', a='kozane armour'),
 mod('Brigandine', drop_x=['European brigandine']),
 mod('Cuirass', tt=[['Coverage', ['Breastplate only', 'Breast and back']]]),
]
limbs = [
 mod('Gorget', drop_x=['Bevor', 'Plate gorget']),
 mod('Arm armour', tt=[['Piece', ['Vambrace', 'Couter', 'Rerebrace', 'Pauldron', 'Spaulder']]]),
 mod('Gauntlet', drop_x=['Mitten gauntlet'], tt=[['Form', ['Mitten', 'Fingered', 'Demi-gauntlet']]]),
 mod('Leg armour', tt=[['Piece', ['Greave', 'Cuisses', 'Poleyn', 'Sabaton']]]),
]
def shield(n, d, a='', y='', xs=None):
    return nk(n, d, SHD, a=a, tt=[['Material', ['Wood', 'Steel', 'Leather or hide']], ['Age', ['Antique', 'Reproduction']]], x=xs)
rnd = mod('Shield', new_name='Round shield', a='boss shield · Viking shield', d='Round shield of light wood, often leather-covered, with a central metal boss, typical of the early Middle Ages.',
          keep_x=['Aspis'], tt=[['Material', ['Wood', 'Steel', 'Leather or hide']], ['Age', ['Antique', 'Reproduction']]])
shields = [
 nk('Pavise', 'Large free-standing shield propped on a stand to shelter crossbowmen while reloading.', SHD, tt=[['Material', ['Wood', 'Leather or hide']]]),
 nk('Scutum', 'Large Roman legionary shield, oval in the early Republic and curved rectangular in the Empire.', SHD, a='Roman shield', tt=[['Shape', ['Oval', 'Curved rectangular']]]),
 nk('Nguni shield', 'Large oval ox-hide shield on a wooden spine, the Zulu form being the ishlangu.', SHD, a='ishlangu · Zulu shield'),
 nk('Kite shield', 'Long shield rounded above and pointed below, introduced by the Normans to protect mounted men.', SHD),
 nk('Heater shield', 'Smaller flat-topped triangular knightly shield that replaced the kite shield and inspired the heraldic shield.', SHD),
 rnd,
 nk('Targe', 'Small round shield used by Scottish clans into the 18th century; Italian targhe were used by fencers and knights.', SHD, a='target'),
 nk('Buckler', 'Small round fist shield of 20-40 cm, often metal, used from the Middle Ages into the 16th century.', SHD),
]
armour = D('Armour & shields', 'variety',
 'Historical and reenactment armour and shields, sorted by the part of the body they cover; modern ballistic protection → Modern body armour, a sword or weapon → its own department.',
 'Which part of the wearer does it cover (all of it, head, torso or limbs), or is it held as a shield?',
 [
  S('Whole suits', 'Complete harnesses that cover the whole body, such as a plate armour harness or a Japanese suit of armour with its helmet and mask.', None, whole),
  S('Helmets & face armour', 'Armour for the head and face, such as the mail coif, sallet, kabuto and menpō.',
    'kinds by build, from mail through the plate helmet to the Japanese helmet and face mask', heads),
  S('Torso armour', 'Armour for the body, such as the gambeson, mail shirt, brigandine and cuirass.',
    'kinds by construction, from padded cloth through rings and small plates to solid plate', torso),
  S('Neck, limb & hand armour', 'Separate armour for neck, arms, hands and legs, such as the gorget, vambrace and gauntlet.',
    'kinds by body part, from the neck down to the leg', limbs),
  S('Shields', 'Hand-held barriers, such as the scutum, kite shield, buckler and pavise; a modern ballistic or riot shield is not covered.',
    'kinds by size and shape, from the free-standing pavise to the fist-held buckler', shields),
 ], note=OD('Armour & shields').get('note'))

# ================= MODERN BODY ARMOUR =================
BA = WIKI + 'Body_armor'
soft = mod('Body armour', new_name='Soft ballistic vest', a='bulletproof vest · ballistic vest',
    d='Vest of layered woven or laminated fibre that stops handgun rounds and fragments, rated to an NIJ level.',
    s=BA, m=[['Hi-Lite', 'Point Blank Enterprises']], tt=[['NIJ level', ['IIA', 'II', 'IIIA']]])
hard = nk('Hard armour plate', 'Steel, ceramic or polyethylene plate that stops rifle rounds, worn in a plate carrier or vest pocket.', BA, a='ballistic plate',
    tt=[['NIJ level', ['III', 'IV']], ['Material', ['Steel', 'Ceramic', 'Polyethylene']]], m=[['Hercules', 'Spartan Armor Systems']])
carrier = nk('Plate carrier', 'Vest that holds hard armour plates and sometimes soft panels, worn over or without a soft vest.', BA)
stab = nk('Stab-resistant vest', 'Vest of tightly woven fibre layers or metal components that resists knife stabbing and slashing.', BA, a='stab vest', m=[['Persuader Stab Vest', 'Protech Corrections']])
bhelm = mod('Ballistic helmet', tt=[['Protection', ['NIJ Level IIIA', 'Rifle-rated']]])
modern = D('Modern body armour', 'tier',
 'Worn protection against bullets and blades, bought by rated protection level; historical armour → Armour & shields, a helmet for a sport → E2.',
 'Which part of the wearer does it protect against modern weapons: the torso or the head?',
 [
  S('Torso protection', 'Vests, plates and carriers worn on the torso, sold by the threat they stop.',
    'kinds by what stops the threat and how it is worn: soft panel, hard plate, plate carrier, stab-resistant layers', [soft, hard, carrier, stab]),
  S('Head protection', 'Helmets rated against bullets and fragments.', None, [bhelm]),
 ])

# ================= MILITARIA & REPLICAS =================
inert = [
 mod('Deactivated firearm', tt=[['Standard', ['EU-certified (from 8 April 2016)', 'Earlier national standard']]]),
 mod('Deactivated ordnance'),
]
repl = [
 mod('Non-firing replica firearm', tt=[['Period', ['Historical (flintlock, percussion)', 'Wild West', 'World-war']]]),
 mod('Decorative replica weapon'),
]
mil = D('Militaria & replicas', 'mixed',
 'Pieces that were or look like weapons but cannot fire or cut: deactivated guns and ordnance, and non-firing copies; a working weapon → its own department, a toy → E1.',
 'Is it a real weapon made safe, or a copy that never worked?',
 [
  S('Deactivated & inert pieces', 'Real guns and ordnance made permanently inoperable under a certified standard and kept for display.', None, inert),
  S('Replicas', 'Copies of guns and weapons built to be seen, not used, for collectors, reenactors and decoration.', None, repl),
 ], note=OD('Militaria & replicas').get('note'))

# ================= ASSEMBLE =================
order = [swords, knives, polearms, archery, firearms, airguns, ammo, optics, selfdef, armour, modern, mil]
cat = {'c': 'E4', 'rev': True,
 'lead': old['lead'],
 'ax': 'What does the object do: cut or strike by hand, shoot a projectile, protect the wearer, or equip and supply a gun?',
 'key': [
  '1. Is it deactivated, inert or a copy that cannot fire or cut? → Militaria & replicas',
  '2. Is it a sword, or a guard, scabbard or fitting made for one? → Swords',
  '3. Is it a dagger, knife, bayonet or thrown blade? → Knives & daggers',
  '4. Is it a spear, axe, mace, hammer, or a stick, chain or blade used in martial arts? → Polearms, axes & martial arts weapons',
  '5. Is it a bow, crossbow, sling or other muscle-powered launcher, or an arrow, bolt or bow fitting? → Archery & slings',
  '6. Is it a gun that fires by burning powder, including muzzle-loaders? → Firearms',
  '7. Is it a gun that fires by compressed air or gas, or its pellets and gas? → Air guns',
  '8. Is it a round of ammunition, a component for loading one, or loading equipment? → Ammunition & reloading',
  '9. Does it sight, replace a part of, support, carry or clean a gun? → Optics, parts & shooting accessories',
  '10. Is it a spray, electric device, striker or blank-firing pistol carried to stop an attacker? → Self-defence',
  '11. Is it historical or reenactment armour, or a shield? → Armour & shields',
  '12. Is it a vest, plate or helmet rated against bullets or blades? → Modern body armour',
  '<i>Precedence: a deactivated or non-firing copy is Militaria before any weapon department; a bayonet is a knife, not a gun part; a blank-firing pistol is Self-defence, not Firearms; a sword that is only a practice or toy copy is E2 or E1.</i>'],
 'b': old.get('b', []), 'depts': order}
names = {}
dup = []
for dp in order:
    for s in dp['s']:
        for k in s['k']:
            if k['n'].lower() in names: dup.append(k['n'])
            names[k['n'].lower()] = k
print('unused old kinds:', sorted(set(K) - USED))
print('duplicates:', dup)
# demoted-archetype accounting
alltext = json.dumps(order, ensure_ascii=False).lower()
missing = []
newx = {x['n'].lower() for dp in order for s in dp['s'] for k in s['k'] for x in k.get('x', [])}
for kn, k in K.items():
    for x in k.get('x', []):
        if x['n'].lower() not in newx:
            # accounted if it appears as a tt member, alias or kind name
            ok = False
            for dp in order:
                for s in dp['s']:
                    for kk in s['k']:
                        if x['n'].lower() == kk['n'].lower(): ok = True
                        if x['n'].lower() in kk.get('a', '').lower(): ok = True
                        for g in kk.get('tt', []):
                            if any(x['n'].lower() in t.lower() for t in g[1]): ok = True
            if not ok: missing.append((kn, x['n']))
print('archetypes not accounted:', missing)
# see targets
import glob
def rk(code):
    p = f'{ROOT}/reader/{code}.json'
    d = json.load(open(p)); return {k['n'] for dp in d['depts'] for s in dp['s'] for k in s['k']}
cache = {}
bad = []
nsee = 0
for dp in order:
    for s in dp['s']:
        for k in s['k']:
            for sv in k.get('see', []):
                nsee += 1
                if sv[0] == 'E4':
                    if sv[1].lower() not in names: bad.append((k['n'], sv))
                else:
                    cache.setdefault(sv[0], rk(sv[0]))
                    if sv[1] not in cache[sv[0]]: bad.append((k['n'], sv))
print('see count', nsee, 'bad see', bad)
renames = {"Air rifle": "Spring-piston air rifle", "Air pistol": "Pneumatic air pistol", "Bayonet": "Knife bayonet", "Body armour": "Soft ballistic vest",
           "Plate helmet": "Historical helmet", "Reloading die": "Reloading die set", "Shield": "Round shield"}
for v in renames.values(): assert v.lower() in names, v
# stats
def stats(d):
    ds = len(d['depts']); sh = sum(len(x['s']) for x in d['depts']); ks = [k for x in d['depts'] for s in x['s'] for k in s['k']]
    return ds, sh, len(ks), sum(len(k.get('x', [])) for k in ks)
print('before', stats(old), 'after', stats(cat))
OUT = ROOT + '/out'
tmp = OUT + '/E4.json.tmp'
json.dump(cat, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, OUT + '/E4.json')
json.dump(renames, open(OUT + '/E4_renames.json', 'w'), ensure_ascii=False, indent=1)
print(os.path.getsize(OUT + '/E4.json'))
