
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
