
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
