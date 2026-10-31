import json, os, sys, shutil
R = '/home/user/Possession-Taxonomy/rebuild'
SRC = R + '/work/STR_B8/bak/B8.json'   # always rebuild from the backup of the original
OUT = R + '/out/B8.json'
d = json.load(open(SRC))

# ---- index existing kinds
kinds = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            kinds[k['n']] = k

WP = 'https://en.wikipedia.org/wiki/'
def new(n, dd, s, tt, a=''):
    return {'n': n, 'a': a, 'd': dd, 's': s, 'tt': tt}

kinds['Electronic padlock'] = new('Electronic padlock', 'A padlock opened by phone, NFC, fingerprint or a programmed electronic key instead of a metal key.', WP + 'Padlock',
    [['Power', ['Active (battery or rechargeable)', 'Passive (powered by the key)']], ['Opening', ['Phone Bluetooth', 'NFC', 'Fingerprint', 'Programmed electronic key']]], 'smart padlock · Bluetooth padlock')
kinds['Diversion safe'] = new('Diversion safe', 'A small safe built into an ordinary-looking object such as a book, can or wall outlet, hidden in plain sight.', WP + 'Safe',
    [['Made to look like', ['Book', 'Can', 'Candle', 'Wall outlet']]], 'hidden safe · book safe')
kinds['Alarm control panel & keypad'] = new('Alarm control panel & keypad', 'The unit that reads the sensors, tracks whether the alarm is set and sounds it, with the keypad or fob that sets and unsets it.', WP + 'Security_alarm',
    [['Form', ['Panel with built-in keypad', 'Separate panel and keypad', 'Wireless keypad', 'Key fob or tag reader']], ['Connection', ['Wired', 'Wireless', 'Hybrid']]], 'alarm panel · alarm keypad')
kinds['Driveway alarm'] = new('Driveway alarm', 'A sensor and receiver that sound a chime when a vehicle or person approaches along a drive or path.', WP + 'Security_alarm',
    [['Sensor', ['Magnetic probe', 'Infrared beam', 'Motion sensor']], ['Connection', ['Wireless', 'Hard-wired']]], 'driveway sensor · approach alarm')
kinds['Door knob cover & latch'] = new('Door knob cover & latch', 'A cover over a door knob or a latch high on the door that stops a young child opening it to a hazardous room.', WP + 'Childproofing',
    [['Design', ['Door knob cover', 'Top-of-door latch (works from both sides)', 'Door lever lock']]], 'door knob cover · child door latch')

# ---- types, grouped by one named question each (written by hand)
TT = {
 'Mortice lock': [['Function', ['Sashlock (latch and bolt)', 'Deadlock (bolt only)', 'Latch only (tubular)', 'Bathroom lock with thumb-turn']], ['Key mechanism', ['3-lever', '5-lever (BS 3621)', 'Euro-profile cylinder']]],
 'Night latch & rim lock': [['Type', ['Night latch', 'Rim sashlock', 'Rim deadlock']], ['Security', ['Standard', 'Deadlocking (BS 3621)']], ['Door stile', ['Standard', 'Narrow, for glazed doors']]],
 'Deadbolt': [['Cylinders', ['Single cylinder (thumb-turn inside)', 'Double cylinder (key both sides)', 'Thumb-turn only']], ['ANSI/BHMA grade', ['Grade 1', 'Grade 2', 'Grade 3']], ['Keying', ['Standard', 'Re-keyable (SmartKey)']]],
 'Keyed lockset': [['Handle', ['Knob', 'Lever', 'Handleset with deadbolt']], ['Function', ['Keyed entry', 'Privacy (thumb-turn)', 'Passage (no lock)']], ['ANSI/BHMA grade', ['Grade 1', 'Grade 2', 'Grade 3']]],
 'Multipoint lock': [['Locking point', ['Hook', 'Roller', 'Deadbolt']], ['Operation', ['Single spindle', 'Split spindle']]],
 'Lock cylinder': [['Profile', ['Euro single', 'Euro double', 'Euro thumb-turn', 'Oval', 'Scandinavian oval', 'Rim', 'Key-in-knob']], ['Security', ['Standard', 'Anti-snap', 'TS 007 1-star', 'TS 007 3-star', 'Sold Secure SS312 Diamond']], ['Keying', ['Keyed different', 'Keyed alike']]],
 'Smart lock': [['Fitting', ['Retrofit thumb-turn module (keeps existing deadbolt)', 'Full-replacement smart deadbolt', 'Euro-cylinder smart lock', 'Smart handle for multipoint doors']], ['Entry', ['Phone app', 'Keypad', 'Fingerprint', 'Apple Home Key']], ['Connection', ['Bluetooth', 'Wi-Fi', 'Thread or Matter']]],
 'Keypad door lock': [['Keypad', ['Mechanical push-button', 'Electronic keypad']], ['Body', ['Lever', 'Knob', 'Heavy-duty exterior']], ['Override', ['Key override', 'No key']]],
 'Cabinet lock': [['Fitted to', ['Cupboard (cam lock)', 'Drawer', 'Locker', 'Mailbox', 'Sliding-glass showcase']], ['Keying', ['Keyed different', 'Keyed alike', 'Master-keyed']]],
 'Door bolt': [['Bolt design', ['Barrel bolt (straight or necked)', 'Tower bolt', 'Flush bolt (lever or slide)', 'Rack (mortice) bolt', 'Pad bolt', 'Espagnolette bolt']], ['Locking', ['Plain', 'Key-operated', 'Combination', 'Padlockable']]],
 'Door chain & guard': [['Design', ['Chain', 'Swing-bar guard', 'Hinged door guard']]],
 'Door security bar': [['Design', ['Adjustable floor bar', 'Floor-wedge door jammer', 'Latch-clip travel lock', 'Barricade with alarm']], ['Door', ['Inward-opening hinged door', 'Sliding patio door']]],
 'Patio door lock': [['Design', ['Sliding-door push bolt', 'French-door bolt', 'Foot-pedal lock', 'Add-on security bar', 'Keyed clamp lock']]],
 'Window lock': [['Window', ['Vertical sliding sash', 'Casement', 'Horizontal sliding', 'PVCu']], ['Lock', ['Sash stop', 'Surface lock', 'Lockable handle (inline or offset)', 'Push-button lock']]],
 'Gate, garage & shutter lock': [['Fitted to', ['Garden gate', 'Up-and-over garage door', 'Roller shutter']], ['Design', ['Latch lock', 'Long-throw lock', 'Bullet lock', 'Handle lock', 'Keyed bolt']]],
 'Shed & garage security': [['Design', ['Hinged shed bar', 'Hasp bar (padbar)', 'Long bar for double doors', 'Ground post with hinged arm', 'T-bar floor defender']], ['Anchor', ['Bolt-down floor anchor', 'Concrete-in floor anchor', 'Wall anchor']], ['Grading', ['Sold Secure graded', 'Ungraded']]],
 'Padlock': [['Shackle', ['Open', 'Closed (shrouded)']], ['Body', ['Laminated steel', 'Solid brass', 'Aluminium', 'Disc (round body, hidden shackle)']], ['Opening', ['Key', 'Combination']], ['Made for', ['Roller shutters', 'Luggage (TSA)', 'Outdoor use (weatherproof)']]],
 'Hasp and staple': [['Strength', ['Standard', 'High-security']], ['Pivot', ['Fixed', 'Hinged (swivel)']]],
 'Security chain': [['Sold Secure grade', ['Bronze', 'Silver', 'Gold', 'Diamond']], ['End', ['Noose (loop-end)', 'Straight']]],
 'Cable lock': [['Closure', ['Looped cable (padlock-closed)', 'Integrated key', 'Integrated combination']], ['Build', ['Armoured', 'Coiled']]],
 'Door viewer': [['Type', ['Optical peephole (fisheye, 160–200 degrees)', 'Digital viewer with camera and screen']]],
 'Security window film': [['Purpose', ['Clear safety film', 'Solar-safety tinted film']], ['Thickness', ['4 mil', '8 mil', '13 mil']], ['Fitting', ['Professionally installed', 'DIY self-adhesive sheet']]],
 'Anti-climb spike': [['Design', ['Rotating roller barrier (non-aggressive)', 'Plastic spike strip for fences and walls', 'Steel razor spike (restricted siting)']]],
 'Property marking kit': [['Marking', ['Forensic liquid with unique code', 'Synthetic DNA and microdot', 'UV marker pen', 'Etched or engraved postcode']], ['Registration', ['Immobilise-registered kit', 'Unregistered']], ['Visible warning', ['Alarm or CCTV warning sign or sticker']]],
 'High-security lock cylinder': [['Mechanism', ['Disc detainer', 'Telescoping pin with sidebar', 'Rotating pin with sidebar', 'Magnetic rotor', 'Dimple']], ['Format', ['Euro profile', 'Key-in-knob or key-in-lever', 'Mortice or rim', 'Padlock', 'Cam lock']]],
 'Antique lock & key': [['Period', ['Roman and medieval', 'Georgian', 'Victorian']], ['Item', ['Padlock', 'Door or chest lock', 'Key']]],
 'Practice & cutaway lock': [['Body', ['Clear acrylic', 'Cutaway production lock', 'Re-pinnable kit lock']], ['Teaching format', ['Progressive pinning set (one pin added at a time)', 'Challenge lock (custom-pinned, swapped between pickers)']], ['Mechanism', ['Pin tumbler', 'Disc detainer']]],
 'Lock pick set': [['Tool', ['Hook', 'Rake (short hook, diamond, ball, snake, city, Bogota)', 'Tension tool (top-of-keyway, bottom-of-keyway, pry bar)', 'Bypass tool or shim', 'Decoder (Lishi type)', 'Pick gun or snap gun', 'Bump key']], ['Lock type', ['Pin tumbler', 'Dimple', 'Disc detainer', 'Tubular', 'Lever and warded']], ['Accessory', ['Pinning tweezers, mat and vice']]],
 'Safe': [['Fitting', ['Freestanding', 'Wall', 'Floor (underfloor)', 'Furniture or hotel']], ['Lock', ['Key', 'Combination dial', 'Electronic keypad', 'Time lock', 'App-connected']], ['Use', ['Home', 'Jewellery', 'Deposit (drop-slot)']], ['Rating', ['EN 14450 cabinet', 'EN 1143-1 grade 0 to X', 'UL RSC Level I to III', 'UL TL-15 and TL-30']]],
 'Fire-resistant safe': [['Form', ['Document chest', 'Fire file cabinet', 'Media or data safe', 'Fire-resistant document bag', 'Fire-and-water safe']], ['Protects', ['Paper (Class 350)', 'Film (Class 150)', 'Magnetic media and drives (Class 125)']], ['Fire rating', ['30 minutes', '1 hour', '2 hours', '4 hours']]],
 'Gun safe': [['Form', ['Rifle or long-gun cabinet', 'Pistol box or quick-access vault', 'Ammunition box']], ['Fire protection', ['Fire-rated', 'Not fire-rated']], ['Opening', ['Key', 'Combination dial', 'Electronic keypad', 'Biometric']]],
 'Cash box': [['Opening', ['Key', 'Combination', 'Electronic']], ['Size', ['Pocket', 'Desktop']]],
 'Key safe': [['Opening', ['Push-button', 'Dial combination', 'Bluetooth or app']], ['Fitting', ['Wall-mounted', 'Over-door (portable)']], ['Approval', ['Sold Secure', 'LPS 1175']]],
 'Key cabinet': [['Locking', ['Key-locking', 'Combination']], ['Fitting', ['Wall-mounted']]],
 'Letterbox': [['Fitting', ['Wall-mounted', 'Post-mounted', 'Through-wall']], ['Security', ['Open', 'Locking', 'Anti-fishing']]],
 'Parcel box': [['Opening', ['Key or code', 'Smart (app-locking)']], ['Delivery', ['Drop-slot (one-way)', 'Lift-lid']]],
 'Wireless alarm kit': [['Monitoring', ['Bells-only', 'Self-monitored', 'Professionally monitored subscription']], ['Hub', ['Standard hub', 'Cellular and Wi-Fi back-up hub', 'Hub with built-in camera']], ['Control', ['App-connected', 'Keypad and fob only']]],
 'Alarm sensor': [['Detects', ['Movement (PIR)', 'Door or window opening (magnetic contact)', 'Breaking glass (acoustic)', 'Vibration or shock']], ['Sounds or signals', ['Siren (indoor or outdoor)', 'Panic button']], ['Hub', ['Hub-linked', 'Stand-alone battery alarm']]],
 'Personal attack alarm': [['Trigger', ['Pull-pin', 'Button']], ['Features', ['LED or strobe light', 'Gas-powered horn', 'App-connected with location alert']]],
 'Security camera': [['Siting', ['Indoor', 'Outdoor']], ['Power', ['Mains', 'Battery', 'Solar', 'Power over Ethernet']], ['Connection', ['Wi-Fi', '4G or LTE', 'Wired Ethernet']], ['Lens and movement', ['Fixed', 'Pan-tilt', 'Dual-lens']], ['Function', ['Recording camera', 'Dummy (decoy) camera']]],
 'Floodlight camera': [['Power', ['Wired', 'Battery', 'Solar']]],
 'Wired camera system': [['Recorder', ['PoE NVR', 'Coax DVR']], ['Channels', ['4-channel', '8-channel', '16-channel']]],
 'Video doorbell': [['Power', ['Battery', 'Wired (mains or transformer)']], ['Form', ['Doorbell button', 'Peephole camera']], ['Chime', ['Wireless chime bundle', 'Phone alert only']]],
 'Doorbell and chime': [['Power', ['Wired', 'Battery', 'Kinetic (battery-free push)']], ['Receiver', ['Hard-wired chime', 'Plug-in chime', 'Portable chime']]],
 'Smoke alarm': [['Sensor', ['Photoelectric (optical)', 'Ionisation', 'Dual-sensor', 'Combined smoke and CO']], ['Power', ['Mains with battery back-up', 'Sealed 10-year battery', 'Replaceable battery']], ['Linking', ['Stand-alone', 'Interlinked (wireless or mains)', 'Smart (app-connected)']]],
 'Heat alarm': [['Sensing', ['Fixed temperature', 'Rate-of-rise']], ['Power', ['Mains interlinked', 'Sealed battery']]],
 'CO alarm': [['Power', ['Sealed 7–10 year battery', 'Plug-in with battery back-up', 'Replaceable battery']], ['Display', ['Digital display', 'No display']], ['Linking', ['Stand-alone', 'Interlinked']]],
 'Gas detector': [['Gas', ['Natural gas (methane)', 'LPG (propane or butane)', 'Combined gas and CO']]],
 'Water-leak detector': [['Alerting', ['Stand-alone sounder', 'Smart (app or hub-connected)', 'Whole-home monitor with automatic shut-off valve']], ['Sensing', ['Floor sensor', 'Sensor cable', 'With freeze warning']]],
 'Fire extinguisher': [['Agent', ['Water', 'Foam', 'Dry powder (ABC)', 'CO2', 'Wet chemical (class F or K)', 'Water mist', 'Lithium-battery agent (AVD)', 'All-fires single agent']], ['Form', ['Hand-held cylinder', 'Aerosol can', 'Automatic stove-top or range-hood suppressor']], ['Servicing', ['Rechargeable', 'Service-free composite (10-year)']]],
 'Fire blanket': [['Size', ['1.0 x 1.0 m kitchen', '1.2 x 1.2 m', '1.2 x 1.8 m heavy-duty']], ['Standard', ['BS EN 1869 kitemarked', 'Unmarked']], ['Pouch', ['Wall pouch', 'Quick-release pouch']]],
 'Fire escape ladder': [['Height', ['Two-storey (about 4 m)', 'Three-storey (about 7.6 m)']], ['Build', ['Steel anti-slip rungs', 'Rope or chain rails']]],
 'Safety sign': [['Sign category (ISO 7010)', ['Fire equipment', 'Safe condition (exit)', 'Warning', 'Prohibition', 'Mandatory']]],
 'Door stop & finger guard': [['Design', ['Wedge', 'Floor or wall stop', 'Foam slam stopper', 'Hinge-side finger guard']]],
 'Baby gate': [['Fixing', ['Hardware-mounted', 'Pressure-mounted', 'Freestanding']], ['Opening', ['Swing-open', 'Retractable']], ['Width', ['Standard', 'Extra-wide or configurable']], ['Site', ['Stairs', 'Doorway', 'Hearth and play-yard']]],
 'Cabinet & appliance latch': [['Mount', ['Adhesive', 'Screw-fit']], ['Mechanism', ['Magnetic lock with key', 'Sliding lock', 'Spring catch']], ['Fits', ['Cupboard or drawer', 'Toilet lid', 'Fridge or freezer', 'Oven door']]],
 'Furniture anti-tip strap': [['Design', ['Nylon strap kit', 'Rigid bracket or hinged anchor']], ['Fixing', ['Screw-in', 'No-drill adhesive']], ['Secures', ['Dresser or bookcase', 'Television']]],
 'Corner and edge guard': [['Form', ['Corner cushion', 'Edge strip']], ['Material', ['Foam', 'Clear silicone']]],
 'Socket cover': [['Design', ['Plug-in cover', 'Sliding or self-closing plate', 'Box cover over plugged-in lead']]],
 'Stove knob cover': [['Design', ['Knob cover', 'Oven door guard or lock', 'Hob guard rail']]],
 'Blind cord safety device': [['Design', ['Cord cleat', 'Cord tidy or chain tensioner', 'Breakaway chain or cord connector', 'Multi-cord breakaway']]],
 'Baby monitor': [['Picture', ['Audio only', 'Video']], ['Display', ['Dedicated parent unit', 'Smartphone app (Wi-Fi)']], ['Sensing', ['Movement or breathing sensor (pad, sock or band)']]],
 'Rodent trap': [['Mechanism', ['Snap', 'Glue board', 'Electronic']], ['Target', ['Mouse', 'Rat']]],
 'Live-catch cage trap': [['Design', ['Single-door', 'Two-door', 'Multi-catch mouse trap']]],
 'Rodenticide bait & bait station': [['Bait', ['Block', 'Pellet or grain']], ['Station', ['Tamper-resistant station', 'Bait only']]],
 'Pest repeller': [['Method', ['Ultrasonic or electronic', 'Chemical granule or spray', 'Moth repellent (cedar, mothballs, sachets)']]],
 'Bird deterrent': [['Method', ['Netting', 'Spike', 'Coil or wire', 'Gel dish', 'Decoy or scarer']]],
 'Insecticide': [['Form', ['Aerosol spray', 'Crack-and-crevice foam', 'Powder or dust (including diatomaceous earth)', 'Fogger']]],
 'Insect bait': [['Form', ['Gel or paste', 'Granules', 'Pre-filled bait station']]],
 'Insect trap': [['Insect', ['Wasp', 'Fruit fly', 'Clothes moth', 'Flying insects in general']], ['Method', ['Bait dome or bag', 'Pheromone', 'Fly paper', 'UV glue board']]],
 'Fly swatter & electric fly killer': [['Design', ['Hand swatter', 'Electric racket', 'UV grid (mains or rechargeable)']]],
 'Mosquito vaporiser & coil': [['Device', ['Plug-in liquid vaporiser', 'Plug-in mat vaporiser', 'Battery or fan unit', 'Mosquito coil']]],
 'Mosquito net & insect screen': [['Fits', ['Bed', 'Door', 'Window']], ['Design', ['Hanging bed net', 'Magnetic door screen', 'Window mesh kit (self-adhesive or hook-and-loop)']]],
 'Door knob cover & latch': None, 'Electronic padlock': None, 'Diversion safe': None, 'Alarm control panel & keypad': None, 'Driveway alarm': None,
}
for n, tt in TT.items():
    if tt is None: continue
    k = kinds[n]
    k['tt'] = tt
    k.pop('t', None)
missing = [n for n, k in kinds.items() if 'tt' not in k]
assert not missing, missing

# ---- new archetypes for the collector kind (all from fetched Wikipedia pages)
ant = kinds['Antique lock & key']
LK = WP + 'Lock_and_key'; PL = WP + 'Padlock'
ant['x'] = [
 {'n': 'Egyptian pin lock', 'a': 'Egyptian wooden pin lock', 'd': 'Wooden bolt lock whose pins fall into drilled holes and are lifted out by the key; the ancestor of the pin tumbler lock.', 'mk': '', 'y': 'ancient', 's': LK, 'v': [], 'dt': 'wooden bolt and fixture · key with pegs · find site'},
 {'n': 'Barron double-acting lever lock', 'a': 'Barron lever lock', 'd': 'First lever tumbler lock: each lever must be lifted to an exact height, so lifting too far fails as well.', 'mk': '', 'y': '1778', 's': LK, 'v': [], 'dt': 'lever count · maker\'s mark · period'},
] + ant['x'] + [
 {'n': 'Yale pin tumbler lock', 'a': 'Yale lock', 'd': 'Pin tumbler cylinder with a small flat serrated key, patented by Linus Yale Jr. and the basis of most door cylinders today.', 'mk': 'Yale', 'y': '1861', 's': LK, 'v': [], 'dt': 'pin count · key blank · maker\'s mark'},
 {'n': 'Scandinavian (Polhem) padlock', 'a': 'Polhem lock · disc padlock', 'd': 'Cast-iron padlock holding a stack of rotating notched discs, taken from Christopher Polhem\'s design and patented by McWilliams in 1871.', 'mk': '', 'y': 'mid-19th century', 's': PL, 'v': [], 'dt': 'disc count · maker · body size'},
 {'n': 'Cast heart padlock', 'a': 'heart lock · railroad heart lock', 'd': 'Heart-shaped brass or bronze lever padlock with a spring cover over the keyhole, much used by railroads.', 'mk': '', 'y': 'mid-19th century', 's': PL, 'v': [], 'dt': 'lever count · maker · railroad marking'},
]
order=['Egyptian pin lock','Roman padlock','Barron double-acting lever lock','Bramah lock','Chubb detector lock','Yale pin tumbler lock','Scandinavian (Polhem) padlock','Cast heart padlock']
ant['x'].sort(key=lambda a: order.index(a['n']))
# keep old generic wording in definition aligned with the new shelf (period view)
ant['d'] = 'Historic locks and keys collected for their mechanism and maker, viewed by period; includes ancient pin locks, Bramah and Chubb locks and old padlocks.'

# ---- cross-links
SEE = {
 'Door bolt': [['C8', 'Door bolt', 'the ironmongery bolt sold by the trade']],
 'Insecticide': [['C2', 'Insecticide', 'spray for garden plants']],
 'Padlock': [['A4', 'Luggage lock', 'travel locks sold with luggage']],
 'Wireless alarm kit': [['G3', 'Intruder alarm system', 'professionally installed alarm']],
 'Video doorbell': [['G3', 'Door phone and video intercom', 'fixed intercom at the gate or door']],
 'Security camera': [['B10', 'Pet camera', 'camera for watching a pet']],
 'Mosquito vaporiser & coil': [['H1', 'Insect repellent', 'repellent worn on skin']],
 'Baby gate': [['B1', 'Playpen', 'a play area instead of a barrier']],
 'Lock cylinder': [['B8', 'High-security lock cylinder', 'restricted-key cylinders collected by lock pickers']],
 'High-security lock cylinder': [['B8', 'Lock cylinder', 'ordinary cylinders for home doors']],
 'Smart lock': [['B8', 'Keypad door lock', 'code lock with no app']],
 'Keypad door lock': [['B8', 'Smart lock', 'app-connected electronic lock']],
 'Fire-resistant safe': [['B8', 'Safe', 'burglary-rated safes']],
 'Gun safe': [['B8', 'Safe', 'general safes for valuables']],
 'Key safe': [['B8', 'Key cabinet', 'indoor cabinet for many keys']],
 'Key cabinet': [['B8', 'Key safe', 'outdoor box for one spare key']],
 'Door viewer': [['B8', 'Video doorbell', 'camera doorbell with a peephole form']],
 'Electronic padlock': [['B8', 'Smart lock', 'electronic door lock']],
}
def target_ok(code, name):
    for p in (R + f'/out/{code}.json', R + f'/reader/{code}.json'):
        if os.path.exists(p):
            dd = json.load(open(p))
            for dp in dd['depts']:
                for s in dp.get('s', []):
                    for k in s['k']:
                        if k['n'] == name: return True
    return code == 'B8' and name in kinds
for n, lst in SEE.items():
    for c, nm, why in lst:
        assert target_ok(c, nm), (n, c, nm)
    kinds[n]['see'] = lst

# ---- structure
def shelf(n, t, ax, names):
    s = {'n': n, 't': t}
    if ax: s['ax'] = ax
    s['k'] = [kinds[x] for x in names]
    return s

depts = []
depts.append({'n': 'Locks & door security', 'mode': 'mixed',
 't': 'Locks, bolts, padlocks and deterrents that keep a door, window, gate or shed shut; a collectable or practice lock → Locksport & lock collecting; a box for valuables → Safes & key boxes.',
 'ax': 'Where is the protection fitted: built into the door, added onto a door or window, carried on a padlock, or placed around the property?',
 's': [
  shelf('Door & cabinet locks', 'Lock bodies, cylinders and electronic locks built into a door, gate or cabinet, such as mortice locks, deadbolts and smart locks; a bolt or bar added on the surface → Add-on door, window & gate security.',
        'kinds by what is fitted: lock in the door edge, lock on the door face, bored-through lock, the loose cylinder, electronic locks, small cabinet locks',
        ['Mortice lock', 'Night latch & rim lock', 'Deadbolt', 'Keyed lockset', 'Multipoint lock', 'Lock cylinder', 'Smart lock', 'Keypad door lock', 'Cabinet lock']),
  shelf('Add-on door, window & gate security', 'Fittings screwed or clamped onto a door, window, gate or outbuilding as extra security, such as barrel bolts, door chains, window locks and shed bars; a lock built into the door → Door & cabinet locks.',
        'kinds by what they secure: a door, a patio door, a window, a gate or shutter, an outbuilding',
        ['Door bolt', 'Door chain & guard', 'Door security bar', 'Patio door lock', 'Window lock', 'Gate, garage & shutter lock', 'Shed & garage security']),
  shelf('Padlocks & chains', 'Portable shackle locks and the hasps, chains and cables they close, such as the Master Lock No. 3 and ABUS Granit; a lock built into a door → Door & cabinet locks.',
        'kinds by what you buy: the padlock, its electronic version, the hasp it closes, the chain or cable it secures with',
        ['Padlock', 'Electronic padlock', 'Hasp and staple', 'Security chain', 'Cable lock']),
  shelf('Viewers, film & deterrents', 'Things that let you see a caller, strengthen glass, deter climbers or make stolen goods traceable, such as peephole viewers and window film; a camera that records → Cameras & recorders.',
        'kinds by how they deter: see the caller, strengthen the glass, stop climbing, make theft traceable',
        ['Door viewer', 'Security window film', 'Anti-climb spike', 'Property marking kit']),
 ]})
depts.append({'n': 'Locksport & lock collecting', 'mode': 'variety',
 't': 'Locks and tools kept for the mechanism rather than the door: high-security cylinders, antique locks, practice locks and pick sets; a lock fitted to protect your own home → Locks & door security.',
 'ax': 'Is the object kept for its mechanism, or used to learn to open locks?',
 's': [
  shelf('Collector locks & keys', 'Locks and keys collected for mechanism, maker or age, such as Abloy Protec2, Medeco M3, Bramah and Chubb locks; a lock to learn on → Practice locks & pick sets.',
        None, ['High-security lock cylinder', 'Antique lock & key']),
  shelf('Practice locks & pick sets', 'Locks made to be picked for practice and the picks and tension tools used on them, such as cutaway locks and the Sparrows Tuxedo set; a lock collected for its mechanism → Collector locks & keys.',
        None, ['Practice & cutaway lock', 'Lock pick set']),
 ]})
depts.append({'n': 'Safes & key boxes', 'mode': 'tier',
 't': 'Lockable containers for valuables, papers, keys and post kept at home; the lock on a door → Locks & door security; a fire-fighting aid → Fire, gas & leak safety.',
 'ax': 'What is kept inside: valuables and papers, keys, or post and parcels?',
 's': [
  shelf('Safes & cash boxes', 'Steel boxes for valuables, papers, cash or firearms, rated against theft or fire, such as wall safes, document chests and gun cabinets; a box for keys → Key boxes.',
        'kinds by the main threat they are built against: theft, fire, unauthorised access to firearms, discovery, loose cash',
        ['Safe', 'Fire-resistant safe', 'Gun safe', 'Diversion safe', 'Cash box']),
  shelf('Key boxes', 'Small lockable holders for spare keys, outdoors or indoors, such as wall-mounted key safes and key cabinets; a box for post → Post & parcel boxes.',
        None, ['Key safe', 'Key cabinet']),
  shelf('Post & parcel boxes', 'Boxes that receive letters or parcels and can be locked, such as wall letterboxes and drop-slot parcel boxes; a box for keys → Key boxes.',
        None, ['Letterbox', 'Parcel box']),
 ]})
depts.append({'n': 'Alarms, cameras & doorbells', 'mode': 'tier',
 't': 'Devices that detect an intruder, record video or announce a caller; a professionally installed alarm → Home Fixtures; a smoke or gas alarm → Fire, gas & leak safety.',
 'ax': 'What does it do: sound an alarm on detection, record what happens, or announce a caller?',
 's': [
  shelf('Alarms & sensors', 'Self-fitted alarm kits, panels, detectors, sirens and personal alarms that sound when someone enters or attacks; a camera → Cameras & recorders.',
        'kinds from the whole system to its parts: kit, control panel, sensors, an outdoor approach alarm, a personal alarm',
        ['Wireless alarm kit', 'Alarm control panel & keypad', 'Alarm sensor', 'Driveway alarm', 'Personal attack alarm']),
  shelf('Cameras & recorders', 'Cameras that record or stream video of the home and the recorders that store it, such as indoor Wi-Fi cameras, floodlight cameras and wired recorder systems; a doorbell with a camera → Doorbells.',
        None, ['Security camera', 'Floodlight camera', 'Wired camera system']),
  shelf('Doorbells', 'Buttons and sounders that announce a caller, with or without a camera; a camera that only watches → Cameras & recorders.',
        None, ['Video doorbell', 'Doorbell and chime']),
 ]})
depts.append({'n': 'Fire, gas & leak safety', 'mode': 'tier',
 't': 'Detectors and fire-fighting aids for the home: smoke, heat, carbon monoxide, gas and water alarms, extinguishers, blankets and escape ladders; an intruder alarm → Alarms, cameras & doorbells.',
 'ax': 'Does it warn that a hazard is present, or help to put out a fire and escape from it?',
 's': [
  shelf('Detectors & alarms', 'Alarms that sense smoke, heat, carbon monoxide, gas or water and sound or send an alert, such as photoelectric smoke alarms and leak sensors; an intruder detector → Alarms & sensors.',
        'kinds by what is sensed: smoke, heat, carbon monoxide, gas, water',
        ['Smoke alarm', 'Heat alarm', 'CO alarm', 'Gas detector', 'Water-leak detector']),
  shelf('Fire-fighting & escape', 'Extinguishers, blankets, escape ladders and signs used once a fire has started; an alarm that detects it → Detectors & alarms.',
        'kinds by the step in a fire: put it out, smother it, climb out, mark the way',
        ['Fire extinguisher', 'Fire blanket', 'Fire escape ladder', 'Safety sign']),
 ]})
depts.append({'n': 'Child & home safety', 'mode': 'tier',
 't': 'Gates, latches, guards and monitors that keep babies and toddlers away from hazards at home; a cot or playpen is furniture, not a safety device.',
 'ax': 'Which hazard is it made for: stairs and doors, cupboards and furniture, sockets, cords and edges, or a baby out of sight?',
 's': [
  shelf('Stairs & doors', 'Barriers and stops that keep a child from stairs, rooms and trapped fingers, such as baby gates and door latches; a latch for a cupboard → Cupboards, appliances & furniture.',
        'kinds by what is blocked: a stair or doorway, a door handle, a door edge',
        ['Baby gate', 'Door knob cover & latch', 'Door stop & finger guard']),
  shelf('Cupboards, appliances & furniture', 'Latches, covers and straps that keep a child out of cupboards, off cooker controls and clear of toppling furniture; a barrier across a doorway → Stairs & doors.',
        None, ['Cabinet & appliance latch', 'Stove knob cover', 'Furniture anti-tip strap']),
  shelf('Sockets, cords & edges', 'Covers and cushions for electric sockets, blind cords and hard corners, such as plug-in socket covers and corner cushions; a strap for furniture → Cupboards, appliances & furniture.',
        None, ['Socket cover', 'Blind cord safety device', 'Corner and edge guard']),
  shelf('Baby monitors', 'Transmitters and parent units that let you hear, see or track a baby in another room; a camera for the house → Cameras & recorders.',
        None, ['Baby monitor']),
 ]})
depts.append({'n': 'Pest & insect control', 'mode': 'tier',
 't': 'Traps, baits, sprays, repellents and screens that kill or keep out household rodents, birds and insects; a spray for protecting garden plants → Feeds, sprays & plant protection.',
 'ax': 'What is the pest: a rodent, bird or other animal, or an insect?',
 's': [
  shelf('Rodents, birds & animals', 'Traps, baits, repellers and deterrents for mice, rats, birds and other animals around the home; a product for insects → Insects.',
        'kinds by method: kill with a trap, catch alive, poison, scare off',
        ['Rodent trap', 'Live-catch cage trap', 'Rodenticide bait & bait station', 'Pest repeller', 'Bird deterrent']),
  shelf('Insects', 'Sprays, baits, traps, vaporisers and screens for flies, wasps, mosquitoes, ants, cockroaches and moths; a product for rodents or birds → Rodents, birds & animals.',
        'kinds by method: spray or bait to kill, trap, swat, repel from the air, screen out',
        ['Insecticide', 'Insect bait', 'Insect trap', 'Fly swatter & electric fly killer', 'Mosquito vaporiser & coil', 'Mosquito net & insect screen']),
 ]})

used = {k['n'] for dp in depts for s in dp['s'] for k in s['k']}
assert used == set(kinds), (set(kinds) - used, used - set(kinds))

d['depts'] = depts
d['ax'] = 'What is the object protecting against: a person getting in, theft of valuables, fire or leaks, a child being hurt, or pests?'
d['key'] = [
 '1. Is it a lock or tool kept or used as a hobby: a collectable or antique lock, a practice lock or a pick set? → Locksport & lock collecting',
 '2. Does it keep a door, window, gate or shed shut, show who is at the door or deter a climber? → Locks & door security',
 '3. Is it a locked box for valuables, papers, keys, post or parcels? → Safes & key boxes',
 '4. Does it detect an intruder, record video or announce a caller? → Alarms, cameras & doorbells',
 '5. Does it warn of, or fight, fire, carbon monoxide, gas or a leak? → Fire, gas & leak safety',
 '6. Is it for keeping a child from a hazard or listening to a baby? → Child & home safety',
 '7. Does it trap, bait, repel or screen out rodents, birds or insects? → Pest & insect control',
 '<i>Precedence: a lock you fit to your own door is a door lock (step 2) even when a collector prizes the make; a smart lock is a lock (step 2) before an alarm (step 4); a video doorbell is a doorbell (step 4); a fire-resistant safe is a safe (step 3); a mosquito net is pest control (step 7); a baby monitor is child safety (step 6).</i>',
]
d['lead'] = 'Movable things a household owns to keep people, property and the home safe: locks and padlocks, safes and key boxes, alarms and cameras, fire and leak detection, child-proofing and pest control, plus a locksport and lock-collecting department. Organised by the threat guarded against, then by what the object is; installed alarms, intercoms and window guards live in Home Fixtures.'

tmp = OUT + '.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, separators=(',', ':'))
os.replace(tmp, OUT)
print('written', os.path.getsize(OUT))
