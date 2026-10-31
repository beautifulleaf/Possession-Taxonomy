
# ================= POLEARMS, AXES & MARTIAL ARTS =================
PA = WIKI + 'Polearm'
pol = [
 mod('Spear', drop_x=['Pike', 'Winged spear', 'Sarissa'], tt=[['Use', ['Thrusting', 'Throwing (javelin)']], ['Head', ['Leaf-shaped', 'Lance-point', 'Winged']]]),
 nk('Pike', 'Very long infantry spear held in massed ranks, used from the Macedonian sarissa to the 17th century.', PA, a='infantry pike · half-pike',
    x=[xold('Spear', 'Sarissa'), xold('Spear', 'Pike')]),
 mod('Partisan', drop_x=['Partisan'], tt=[['Use', ['Fighting', 'Ceremonial']]]),
 nk('Corseque', 'Polearm with a three-bladed head on a 6-8 ft haft, popular in Europe in the 16th and 17th centuries.', PA, a='ranseur · spetum'),
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
