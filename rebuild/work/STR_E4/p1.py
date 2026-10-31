
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
 ], note=old['depts'][0].get('note'))
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
 ], note=old['depts'][1].get('note'))
depts.append(knives)
