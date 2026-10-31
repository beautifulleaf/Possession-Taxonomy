import json, os, shutil, re, sys
R = '/home/user/Possession-Taxonomy/rebuild/'
W = R + 'work/STR_D2/'
src = json.load(open(W + 'bak/D2.json'))
bidx = {x[0].lower() for x in json.load(open(R + 'reader/_brand_index.json'))['b']}

# ---------- pool of existing kinds ----------
pool = {}
for dp in src['depts']:
    for s in dp['s']:
        for k in s['k']:
            pool[k['n']] = k
before = dict(depts=len(src['depts']), shelves=sum(len(d['s']) for d in src['depts']), kinds=len(pool),
              arch=sum(len(k.get('x', [])) for k in pool.values()))

WP = 'https://en.wikipedia.org/wiki/'
S = dict(form=WP + 'Mobile_phone_form_factor', tab=WP + 'Tablet_computer', ereader=WP + 'E-reader',
         watch=WP + 'Smartwatch', track=WP + 'Activity_tracker', gps=WP + 'GPS_navigation_device',
         sat=WP + 'Satellite_phone', plb=WP + 'Personal_locator_beacon', pda=WP + 'Personal_digital_assistant',
         acc=WP + 'Mobile_phone_accessories', chg=WP + 'Battery_charger', cordless=WP + 'Cordless_telephone',
         tel=WP + 'Telephone', hr=WP + 'Heart_rate_monitor', rugged=WP + 'Rugged_computer',
         pop=WP + 'PopSockets', palm=WP + 'Palmtop_PC', hro='https://www.hamradio.com/',
         doro='https://uk.doro.com/en-gb/')


def take(name, new_name=None):
    k = pool.pop(name)
    if new_name:
        k['n'] = new_name
    return k


def tt(k, groups):
    k.pop('t', None)
    k['tt'] = groups
    return k


def nk(n, d, s, groups, a='', **kw):
    k = {'n': n, 'a': a, 'd': d, 's': s, 'tt': groups}
    k.update(kw)
    return k


def arch(k, n):
    for a in k.get('x', []):
        if a['n'] == n:
            return a
    raise KeyError(n)


def demote(k, n):
    a = arch(k, n)
    k['x'].remove(a)
    k.setdefault('r', []).append([a['n'], a.get('mk', '')])


def fold(parent, children, notes):
    """Move archetypes (children, in parent's kind) into parent's versions."""
    p = None
    for c in children:
        a = arch(parent, c)
        p = p or arch(parent, notes['parent'])
        parent['x'].remove(a)
        p.setdefault('v', []).append({'n': a['n'], 'mk': a.get('mk', ''), 'y': a.get('y', ''), 'd': notes.get(c, a.get('d', ''))[:110]})
        for v in a.get('v', []) or []:
            p['v'].append(v)


def addx(k, n, mk, y, d, s, a=''):
    if mk and mk.lower() not in bidx:
        raise SystemExit('brand not in index: ' + mk)
    k.setdefault('x', []).append({'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': []})


def addm(k, model, maker):
    k.setdefault('m', []).append([model, maker])


def sh(n, t, k, ax=None):
    o = {'n': n, 't': t}
    if ax:
        o['ax'] = ax
    o['k'] = k
    return o


def see(k, *links):
    k['see'] = [list(l) for l in links]


# =============== PHONES ===============
ts = take('Touchscreen smartphone')
ts['n'] = 'Touchscreen smartphone'
ts['d'] = 'Phone that runs apps on one rigid touchscreen slab, with no physical keyboard; the everyday smartphone.'
tt(ts, [['Screen size', ['Compact', 'Standard', 'Large (phablet)']],
        ['Operating system', ['iOS', 'Android', 'HarmonyOS']],
        ['Price tier', ['Flagship', 'Mid-range', 'Budget']]])
ts['s'] = ts['s']
demote(ts, 'OnePlus numbered series')
demote(ts, 'Xiaomi numbered series')
# IBM Simon first
ts['x'].insert(0, {'n': 'IBM Simon', 'a': 'Simon Personal Communicator', 'd': 'The first commercial touchscreen phone with stylus-driven apps, sold with a cellular network service.',
                   'mk': 'IBM', 'y': '1994', 's': S['form'], 'v': []})

kb = take('Keyboard smartphone')
kb['d'] = 'Smartphone with a physical QWERTY keyboard, fixed below the screen or slid out from behind it.'
tt(kb, [['Keyboard', ['Fixed below the screen', 'Slide-out', 'Folding']], ['Screen', ['Touchscreen', 'Non-touch screen']]])

ru = take('Rugged phone')
demote(ru, 'Ulefone Armor')
tt(ru, [['Protection', ['IP68 water and dust sealing', 'MIL-STD-810 drop rating']],
        ['Built-in tool', ['Thermal camera', 'Walkie-talkie mode', 'Night-vision camera', 'Extra-large battery']]])

ga = take('Gaming phone')
tt(ga, [['Cooling', ['Built-in fan', 'Vapour chamber only']], ['Controls', ['Shoulder triggers', 'Touch only']]])

smart = sh('Smartphones',
           'Phones that run apps on one rigid body, sold for everyday use or for a harder job; a folding body → Folding smartphones, a keypad-only phone → Feature phones.',
           [ts, kb, ru, ga], 'kinds by what the rigid body is built for: everyday touch use, typing, toughness or gaming')

ff = take('Flip foldable phone')
ff['d'] = 'Smartphone whose flexible screen folds across its width into a compact square.'
tt(ff, [['Cover screen', ['Small cover display', 'Large cover display']], ['Price tier', ['Flagship', 'Mid-range']]])
see(ff, ['D2', 'Flip phone', 'the keypad clamshell that came first'])
bf = take('Book foldable phone')
tt(bf, [['Fold direction', ['Inward', 'Outward', 'Tri-fold']], ['Open size', ['Small tablet (7–8 in)', 'Large tablet (10 in)']]])
ds = take('Dual-screen phone')
tt(ds, [['Screen join', ['Hinge between two screens', 'Swivelling second screen']],
        ['Screens', ['Two equal touchscreens', 'Main screen with a small second screen']]])
fold_sh = sh('Folding smartphones',
             'Smartphones whose body or screen folds or splits in two; a rigid single slab → Smartphones, a keypad clamshell → Feature phones.',
             [ff, bf, ds], 'kinds by how the screen opens: folded across the width, along the length, or two separate screens')

kp = take('Keypad phone')
kp['d'] = 'Basic mobile phone in one rigid body with a keypad and no app store; includes the one-piece taco shape and large-button senior phones.'
tt(kp, [['Shape', ['Candy bar', 'Taco']], ['Use', ['Standard', 'Senior large-button', 'Rugged', 'Smart feature phone (KaiOS)']]])
addm(kp, 'Leva E10', 'Doro')
kp['s'] = kp['s']
fl = take('Flip phone')
fl['d'] = 'Basic mobile phone whose body folds shut on a hinge (clamshell).'
tt(fl, [['Hinge', ['Flip-up clamshell', 'Flip-down', 'Reverse-hinged']], ['Use', ['Standard', 'Senior large-button']]])
addm(fl, 'Leva E22', 'Doro')
sl = take('Slider phone')
tt(sl, [['Slide direction', ['Vertical', 'Sideways']], ['Reveals', ['Numeric keypad', 'QWERTY keyboard', 'Game controls']]])
sw = take('Swivel phone')
tt(sw, [['Pivot', ['Screen half rotates', 'Keypad half twists']], ['Reveals', ['Numeric keypad', 'QWERTY keyboard']]])
feat = sh('Feature phones',
          'Basic mobile phones for calls and texts, without an app store; a smartphone → Smartphones, a 1980s brick or a luxury handset → Collector\'s handsets.',
          [kp, fl, sl, sw], 'kinds by how the body is built: one block, folding hinge, sliding halves or a swivel')

em = take('Early mobile phone')
em['d'] = 'Large handheld, car-fitted or bag-carried mobile phone of the 1980s and early 1990s, often called a brick.'
tt(em, [['Carried as', ['Brick handset', 'Bag phone', 'Car-fitted phone']], ['Network generation', ['Analogue (1G)', 'Early digital (2G)']]])
lx = take('Luxury phone')
tt(lx, [['Maker type', ['Hand-built luxury marque', 'Precious-material edition of a mainstream phone']],
        ['Material', ['Titanium', 'Gold', 'Platinum', 'Sapphire crystal', 'Leather']]])
coll = sh('Collector\'s handsets',
          'Mobile phones collected for history or luxury rather than daily use; ordinary old keypad phones stay in Feature phones.',
          [em, lx], 'kinds by why they are collected: first-generation size or precious build')

ll = take('Landline phone')
old_models = ll.pop('m')
vint = take  # placeholder
vt = ll
vt['n'] = 'Vintage telephone'
vt['a'] = 'antique telephone · classic landline'
vt['d'] = 'Wired telephone of a classic design from the candlestick era to the 1980s, collected or used as a period piece.'
vt['s'] = S['tel']
vt['x'] = [a for a in vt['x']]
addx(vt, 'Ericsson DBH 1001', 'Ericsson', 'c. 1931', 'First telephone with the transmitter and receiver in a single Bakelite handset.', S['tel'])
addx(vt, 'Model 2500', 'Western Electric', '', 'Push-button desk telephone from the Bell System.', S['tel'])
tt(vt, [['Mounting', ['Candlestick stand', 'Desk set', 'Wall set']], ['Dial', ['Hand-cranked magneto', 'Rotary dial', 'Push-button']],
        ['Housing', ['Bakelite', 'Plastic', 'Wood', 'Metal']]])
vt['tg'] = vt.get('tg', [])

cd = nk('Corded phone', 'Telephone joined to the line by a cord, for the desk or the wall, sold new for home or office.', S['tel'],
        [['Mounting', ['Desk', 'Wall']], ['Keys', ['Standard keypad', 'Large-button']], ['Extras', ['Caller display', 'Built-in answering machine']]],
        m=[['Desk 400', 'Gigaset']])
cl = nk('Cordless phone', 'Telephone whose handset talks by radio to a base on the line and recharges in it.', S['cordless'],
        [['Radio standard', ['DECT', 'DECT 6.0 (North America)', 'Analogue (older)']], ['Handsets', ['Single', 'Multiple']],
         ['Link', ['Landline only', 'Bluetooth link to a mobile']], ['Unit', ['Handset and base', 'Extra handset', 'Range repeater']]],
        m=[['KX-TG6761GB', 'Panasonic'], ['FRITZ!DECT Repeater 100', 'AVM']])
ip = nk('IP phone', 'Telephone that carries calls over an internet connection, or an adapter that joins an ordinary phone to it.', S['tel'],
        [['Connection', ['Ethernet', 'Wi-Fi', 'USB to a computer']], ['Form', ['Desk phone', 'Analogue telephone adapter']]])
fixed = sh('Fixed-line telephones',
           'Telephones that work through a home or office line or internet connection; a mobile handset → Phones above, a satellite handset → Navigation, trackers & safety beacons.',
           [cd, cl, ip, vt], 'kinds by how the handset reaches the line: a cord, a radio base, the internet or an antique wired design')

phones = dict(n='Phones', mode='mixed', note='Tier for everyday buyers; variety for collectors of classic and iconic handsets.',
              t='Handsets for calls and messages: smartphones, basic mobiles, collector handsets and fixed-line telephones; a satellite phone → Navigation, trackers & safety beacons, a smartwatch → Wearables.',
              ax='What kind of handset is it: a smartphone, a folding smartphone, a basic mobile, a collector\'s mobile or a fixed-line telephone?',
              s=[smart, fold_sh, feat, coll, fixed])

# =============== TABLETS & E-READERS ===============
tb = take('Tablet')
tb['d'] = 'Touchscreen computer in one flat body, sold without a keyboard; a keyboard cover is sold separately.'
tt(tb, [['Screen size', ['Mini (7–8 in)', 'Standard (10–11 in)', 'Large (12–13 in)']],
        ['Operating system', ['iPadOS', 'Android', 'Fire OS', 'Windows']],
        ['Edition', ['Standard', 'Kids\' edition with bumper case']], ['Connectivity', ['Wi-Fi only', 'Wi-Fi and cellular']]])
fold(tb, ['iPad mini', 'iPad Air', 'iPad Pro'], {'parent': 'iPad', 'iPad mini': 'smaller 7–8 inch iPad', 'iPad Air': 'mid-range iPad', 'iPad Pro': 'top-end iPad with the fastest chip'})
addx(tb, 'Nokia 770', 'Nokia', '2005', 'Nokia\'s first Internet tablet, a Maemo Linux device for browsing.', S['tab'])
addx(tb, 'BlackBerry PlayBook', 'BlackBerry', '2011', 'Seven-inch tablet running BlackBerry Tablet OS.', S['tab'])
addx(tb, 'Nexus 7', 'Google', '2012', 'Google\'s seven-inch mini tablet, made with ASUS.', S['tab'])
addx(tb, 'Microsoft Surface', 'Microsoft', '2012', 'Windows 8 tablet with a clip-on keyboard cover, the start of the Surface line.', S['tab'])
see(tb, ['D1', 'Detachable 2-in-1', 'a tablet sold as a laptop with a keyboard'])
rt = nk('Rugged tablet', 'Tablet built for field work, with sealed casing and often a barcode scanner; owned by outdoor users and tradespeople.', S['rugged'],
        [['Protection', ['Semi-rugged', 'Fully rugged']], ['Field feature', ['Barcode scanner', 'Hot-swap battery', 'Glove-touch screen']]])
tab_sh = sh('Tablets', 'Backlit LCD or OLED tablets that run apps; an E Ink device → E-paper devices, a laptop with a detachable screen → D1.',
            [tb, rt])

er = take('E-reader')
er['d'] = 'Device sold for reading e-books, usually on a glare-free E Ink screen with weeks of battery.'
tt(er, [['Screen', ['Black-and-white E Ink', 'Colour E Ink']], ['Size', ['6 in', '7 in', '10 in']],
        ['Feature', ['Waterproof', 'Warm front light', 'Page-turn buttons']]])
fold(er, ['Kindle Paperwhite', 'Kindle Voyage', 'Kindle Oasis', 'Kindle Colorsoft'],
     {'parent': 'Kindle', 'Kindle Paperwhite': 'backlit waterproof Kindle', 'Kindle Voyage': 'flush-front Kindle with page-press sensors',
      'Kindle Oasis': 'metal Kindle with page buttons', 'Kindle Colorsoft': 'first colour Kindle'})
er['x'].insert(0, {'n': 'Sony Librie', 'a': '', 'd': 'First e-reader to use electronic paper, sold in Japan before the Sony Reader.', 'mk': 'Sony', 'y': '2004', 's': S['ereader'], 'v': []})
demote(er, 'Boox reader')
wt = take('E-paper writing tablet')
tt(wt, [['Size', ['Notepad (6–8 in)', 'Standard (10–11 in)', 'Large (13 in)']], ['Screen', ['Black-and-white', 'Colour']],
        ['Pen', ['Passive pen', 'Active pen']]])
addm(wt, 'PineNote', 'Pine64')
see(wt, ['D1', 'Pen tablet', 'a drawing tablet that needs a computer'])
at = nk('Android E Ink tablet', 'E Ink tablet that runs the full Android app store, for reading, notes and apps.', S['ereader'],
        [['Screen', ['Black-and-white', 'Colour']], ['Size', ['7 in', '10 in', '13 in']], ['Apps', ['Google Play built in', 'Apps sideloaded']]],
        m=[['Boox Max2', 'Onyx']])
epaper = sh('E-paper devices', 'Devices with an E Ink screen that stays readable in sunlight; an LCD tablet → Tablets.',
            [er, wt, at], 'kinds by what the E Ink screen is for: reading books, writing by hand or running apps')
tabs = dict(n='Tablets & e-readers', mode='mixed', note='Tier for tablets; variety for e-readers and e-paper devices.',
            t='Flat screens held in the hands for apps, reading or handwriting; a phone → Phones, a graphics tablet for a computer → D1.',
            ax='What is the screen for: general apps, reading, or writing by hand?',
            s=[tab_sh, epaper])

# =============== WEARABLES ===============
sm = take('Smartwatch')
sm['d'] = 'Wrist device with a display that runs apps and shows phone notifications; dedicated sport watches are a separate kind.'
bounce = [m for m in sm.pop('m', []) if m[0] == 'Bounce']
fold(sm, ['Apple Watch SE', 'Apple Watch Ultra'], {'parent': 'Apple Watch', 'Apple Watch SE': 'lower-priced Apple Watch', 'Apple Watch Ultra': 'large rugged Apple Watch for outdoor sport'})
addx(sm, 'Timex Datalink', 'Timex', '1994', 'First watch to receive data wirelessly from a computer.', S['watch'])
addx(sm, 'Seiko Ruputer', 'Seiko', '1998', 'Often called the first smartwatch, with graphics and third-party apps.', S['watch'], 'Matsucom onHand PC')
addx(sm, 'Galaxy Gear', 'Samsung', '2013', 'Samsung\'s first smartwatch, linked to Galaxy phones.', S['watch'])
tt(sm, [['Operating system', ['watchOS', 'Wear OS', 'One UI / Tizen', 'Maker\'s own system']], ['Connectivity', ['Bluetooth to a phone', 'Built-in LTE']],
        ['Case size', ['Small (40–41 mm)', 'Large (44–49 mm)']], ['Screen', ['OLED', 'Memory LCD', 'E-paper']]])
see(sm, ['A5', 'Digital watch', 'a watch with no apps'], ['D2', 'Kids\' smartwatch', 'made for children'])
ms = take('Multisport GPS watch')
tt(ms, [['Built for', ['Running', 'Triathlon', 'Outdoor', 'Golf', 'Aviation']], ['Screen', ['AMOLED', 'Memory-in-pixel']], ['Charging', ['Solar assisted', 'Standard']]])
see(ms, ['E2', 'Golf GPS', 'a golf-only distance unit'], ['E2', 'Cycling computer', 'a bike-mounted unit'])
hy = take('Hybrid smartwatch')
tt(hy, [['Display', ['Analogue hands only', 'Hands with a small digital window']], ['Sensors', ['Activity', 'Heart rate', 'ECG']]])
see(hy, ['A5', 'Quartz watch', 'an analogue watch with no sensors'])
ks = nk('Kids\' smartwatch', 'Limited-function watch for children that makes calls and reports location to a parent.', S['watch'],
        [['Contact', ['Calls and messages', 'Location only']], ['Network', ['Own SIM', 'Paired with a parent\'s phone']]],
        m=bounce)
wrist = sh('Smartwatches & sport watches', 'Wrist devices with a screen that run apps or train you; a plain analogue or digital watch → A5.',
           [sm, ms, hy, ks], 'kinds by purpose: everyday apps, sport training, analogue look or a child\'s first watch')

fb = take('Fitness band')
tt(fb, [['Screen', ['Colour touchscreen', 'Monochrome', 'No screen but LEDs']], ['Sensors', ['Heart rate', 'Blood oxygen', 'Built-in GPS']]])
demote(fb, 'Fitbit clip-on trackers')
sb = take('Screenless band')
tt(sb, [['Worn on', ['Wrist', 'Upper arm']], ['Measures', ['Strain and recovery', 'Sleep', 'Heart rate']]])
rg = take('Smart ring')
tt(rg, [['Material', ['Titanium', 'Ceramic', 'Gold-plated']], ['Charging', ['Charging case', 'Wireless dock']], ['Subscription', ['None', 'Membership for full data']]])
demote(rg, 'RingConn')
hs = nk('Heart-rate strap', 'Chest or arm strap that senses heart rate and sends it to a watch, phone or bike computer.', S['hr'],
        [['Worn on', ['Chest', 'Upper arm']], ['Sensor', ['Electrical (ECG)', 'Optical (PPG)']], ['Connection', ['Bluetooth', 'ANT+', 'Both']]],
        m=[['H10', 'Polar'], ['H9', 'Polar'], ['Verity Sense', 'Polar']])
sens = sh('Bands, rings & straps', 'Wearable body sensors with little or no screen; a watch with a screen → Smartwatches & sport watches.',
          [fb, sb, rg, hs], 'kinds by how the sensor is worn: screen band, screenless band, finger ring or strap')
sg = take('Smart glasses')
tt(sg, [['Function', ['Camera and audio', 'Display', 'Augmented reality']], ['Lenses', ['Clear', 'Sunglass', 'Prescription']]])
see(sg, ['E5', 'XR display glasses', 'display glasses used as a monitor'])
eyes = sh('Smart glasses', 'Glasses with a see-through display, camera or speakers; a headset that encloses the eyes → E5.', [sg])
wear = dict(n='Wearables', mode='mixed', note='Tier for fitness bands; variety for smartwatch and smart ring history.',
            t='Electronics worn on the wrist, finger, chest or face that track the body or show notifications; headphones → D3, a mechanical or quartz watch → A5.',
            ax='Where is it worn and what does it do there: apps and training at the wrist, body sensing, or a display at the eyes?',
            s=[wrist, sens, eyes])

# =============== PDAs ===============
eo = take('Electronic organiser')
tt(eo, [['Input', ['Calculator-style keys', 'Small QWERTY keyboard', 'Touch pad']], ['Data link', ['None', 'Cable to a PC', 'Infrared']]])
pd = take('PDA')
tt(pd, [['Input', ['Stylus with handwriting', 'Thumb keyboard', 'Clamshell keyboard']],
        ['Operating system', ['Palm OS', 'Windows Mobile (Pocket PC)', 'EPOC', 'Newton OS', 'Linux']]])
pm = nk('Palmtop computer', 'Pocket-sized clamshell computer with a built-in keyboard that runs ordinary programs, from the late 1980s.', S['palm'],
        [['Body', ['Clamshell with keyboard', 'Slab with keyboard']], ['Operating system', ['DOS', 'Windows CE', 'EPOC']]])
addx(pm, 'Atari Portfolio', 'Atari', '1989', 'Called the first palmtop PC, running DIP DOS 2.11.', S['palm'], 'DIP Pocket PC')
addx(pm, 'HP 95LX', 'HP', '1991', 'MS-DOS palmtop with built-in Lotus 1-2-3.', S['palm'])
addx(pm, 'HP 200LX', 'HP', '1994', 'Improved MS-DOS palmtop with a faster processor.', S['palm'])
orgs = sh('Organisers & pocket computers', 'Pocket devices that hold a diary, contacts and notes; a phone → Phones.',
          [eo, pd, pm], 'kinds by how programmable they are: fixed organiser, stylus PDA, keyboard palmtop')
tr = take('Translator & electronic dictionary')
tr_models = tr.pop('m')
tr_s = tr['s']
pt = nk('Pocket translator', 'Handheld device or earbuds that translate speech or text; ordinary earbuds with a translate feature are in Audio & Video.', tr_s,
        [['Form', ['Handheld', 'Earbuds', 'Clip-on']], ['Connection', ['Online', 'Offline language packs']], ['Translates', ['Speech', 'Text and camera']]],
        m=[m for m in tr_models if 'Ex-word' not in m[0]])
ed = nk('Electronic dictionary', 'Pocket device that holds dictionaries and reference works for look-up, used by students and language learners.', tr_s,
        [['Content', ['Bilingual dictionary', 'Encyclopaedic reference', 'Language learning']], ['Input', ['Keyboard', 'Touchscreen', 'Stylus']]],
        m=[m for m in tr_models if 'Ex-word' in m[0]])
lang = sh('Language aids', 'Pocket devices that translate or look up words.', [pt, ed])
pdas = dict(n='PDAs, organisers & translators', mode='mixed', note='Collector variety for PDAs and organisers; tier for current translators.',
            t='Pocket devices that keep a diary and notes or translate words, and are not phones; a phone running a planner app → Phones.',
            ax='What does the pocket device do: run programs as a small computer, keep the diary and contacts, or translate?',
            s=[orgs, lang])

# =============== NAVIGATION ===============
hg = take('Handheld GPS')
tt(hg, [['Built-in link', ['None', 'Two-way radio', 'Satellite messaging']], ['Worn', ['Held in the hand', 'Wrist-mounted']],
        ['Power', ['AA batteries', 'Rechargeable']], ['Maps', ['Preloaded topographic maps', 'Map cards added']]])
see(hg, ['E2', 'Cycling computer', 'a bike-mounted navigator'])
cs = take('Car sat-nav')
tt(cs, [['Fitted to', ['Car', 'Motorcycle', 'Lorry or camper']], ['Screen', ['5 in', '6–7 in', '8 in or larger']], ['Updates', ['Lifetime maps', 'Live traffic']]])
navs = sh('Navigators', 'Devices that show your own position on a map; a phone map app → Phones.', [hg, cs])
bt = take('Bluetooth item tracker')
tt(bt, [['Form', ['Key-ring tag', 'Card', 'Sticker']], ['Power', ['Replaceable battery', 'Rechargeable']],
        ['Finding network', ['Apple network', 'Android network', 'Maker\'s own network']]])
see(bt, ['D2', 'GPS tracker', 'has its own GPS and SIM'])
gt = take('GPS tracker')
tt(gt, [['Carried by', ['Child or older person', 'Bag or luggage']], ['Reporting', ['Live over cellular', 'Logged and downloaded']],
        ['Power', ['Rechargeable', 'Long-life battery']]])
see(gt, ['B10', 'GPS pet tracker', 'worn by an animal'], ['D2', 'Bluetooth item tracker', 'no SIM, uses nearby phones'])
trk = sh('Trackers', 'Devices that report where an object or person is; an animal tracker → B10.', [bt, gt],
         'kinds by how the position reaches you: through nearby phones or over its own cellular link')
sp = take('Satellite phone')
tt(sp, [['Network', ['Iridium', 'Inmarsat', 'Thuraya', 'Globalstar']], ['Antenna', ['Handset with antenna', 'External antenna']]])
sm2 = take('Satellite messenger')
tt(sm2, [['Network', ['Iridium', 'Globalstar', 'Phone link via Skylo']], ['Screen', ['Own screen and keypad', 'Pairs with a phone only']]])
see(sm2, ['D2', 'Personal locator beacon', 'sends a distress call only'])
pl = take('Personal locator beacon')
tt(pl, [['Extra feature', ['AIS for boaters', 'Return link (acknowledgement)', 'Built-in display']], ['Transmit time', ['24 hours', '48 hours']]])
see(pl, ['E2', 'Avalanche transceiver', 'a short-range beacon, not satellite'], ['D2', 'Satellite messenger', 'sends texts as well'])
ep = nk('EPIRB', 'Distress beacon fixed to a boat that floats free and transmits a position when the boat sinks.', S['plb'],
        [['Release', ['Automatic float-free', 'Manual only']], ['Position', ['Built-in GPS (GPIRB)', 'Without GPS']]], a='emergency position-indicating radio beacon')
see(ep, ['D2', 'Personal locator beacon', 'carried by a person, not a vessel'])
hp = take('Satellite hotspot')
tt(hp, [['Network', ['Iridium', 'Inmarsat', 'Thuraya']], ['Connection', ['Wi-Fi to phones', 'Cable']]])
satl = sh('Satellite communicators & beacons', 'Devices that reach people or rescue outside phone coverage; a phone that only has satellite SOS built in → Phones.',
          [sp, sm2, pl, ep, hp], 'kinds by what they send: voice, text, a distress signal only, or a data link')
nav = dict(n='Navigation, trackers & safety beacons', mode='tier', note='Tier: market-covering brands plus independent test winners.',
           t='Devices that show where you are, report where something is, or call for help beyond phone coverage; a cycling computer → E2, a built-in car system → G1.',
           ax='Does it show your own position, report the position of a thing or person, or reach help outside phone coverage?',
           s=[navs, trk, satl])

# =============== RADIO ===============
hf = take('HF base transceiver')
tt(hf, [['Receiver design', ['Superheterodyne', 'SDR (direct sampling)', 'Valve or hybrid (vintage)']], ['Bands', ['HF only', 'HF, VHF and UHF all-mode']],
        ['Output power', ['100 W', '200 W']]])
mo = take('Mobile transceiver')
tt(mo, [['Bands', ['VHF/UHF FM', 'HF mobile']], ['Mode', ['Analogue FM', 'Digital (D-STAR, C4FM, DMR)']]])
qr = take('Portable QRP transceiver')
tt(qr, [['Build', ['Factory-built', 'Kit']], ['Bands', ['HF multiband', 'Single-band']], ['Output power', ['5 W', '10 W']]])
ht = take('Amateur handheld transceiver')
tt(ht, [['Bands', ['Single-band', 'Dual-band', 'Tri-band']], ['Mode', ['Analogue FM', 'Digital (D-STAR, C4FM, DMR)']]])
trx = sh('Amateur transceivers', 'Transmitting radios for the amateur bands; a licence-free handheld → Licence-free & citizens-band radios.',
         [hf, mo, qr, ht], 'kinds by where the radio is used: home base, vehicle, field pack or hand')

mk_ = take('Morse key')
tt(mk_, [['Mechanism', ['Straight key', 'Sideswiper (cootie)', 'Semi-automatic bug', 'Single-lever paddle', 'Iambic paddle']]])
mic = nk('Station microphone & headset', 'Microphone or headset that feeds an amateur transceiver for voice operating.', S['hro'],
         [['Form', ['Desk microphone', 'Hand microphone', 'Headset with boom microphone']], ['Element', ['Dynamic', 'Condenser']]])
dig = nk('Digital-mode interface', 'Box or cable that joins a transceiver to a computer for packet, APRS and other digital modes.', S['hro'],
         [['Link', ['USB sound-card interface', 'Terminal node controller', 'Built into the radio']], ['Use', ['Packet and APRS', 'Weak-signal modes']]])
psu = nk('Station power supply', 'Mains unit that gives the 13.8 volts a transceiver runs on.', S['hro'],
         [['Type', ['Linear', 'Switch-mode']], ['Current', ['20 A', '30 A or more']]])
la = take('Linear amplifier')
tt(la, [['Device', ['Solid-state', 'Valve (tube)']], ['Output', ['500 W', '1 kW', '1.5 kW']]])
at_ = take('Antenna tuner')
tt(at_, [['Operation', ['Manual', 'Automatic']], ['Position', ['In the shack', 'Remote (at the antenna)']], ['Circuit', ['L', 'T', 'Pi network']]])
an = take('Amateur antenna')
tt(an, [['Design', ['Dipole', 'Doublet', 'Vertical', 'Yagi beam', 'End-fed half-wave', 'End-fed long wire', 'Full-wave loop', 'Magnetic loop']],
        ['Bands', ['Single-band', 'Multiband']]])
rot = nk('Antenna rotator', 'Motor that turns a beam antenna to face a chosen direction.', S['hro'],
         [['Turns', ['Azimuth only', 'Azimuth and elevation (satellite)']], ['Load', ['Light VHF/UHF', 'Medium HF beam', 'Heavy tower-mounted']]], a='rotor')
aa = take('Antenna analyser & SWR meter')
tt(aa, [['Instrument', ['SWR meter', 'Antenna analyser', 'Vector network analyser']]])
stn = sh('Station equipment', 'Gear around the transceiver in an amateur station; the transceiver itself → Amateur transceivers.',
         [mk_, mic, dig, psu, la, at_, an, rot, aa], 'kinds by place in the chain from operator to air: key and microphone, interface, power, amplifier, tuner, antenna, rotator, measuring')

wk = take('Walkie-talkie')
tt(wk, [['Licence', ['FRS (US, licence-free)', 'GMRS (US, licensed)', 'PMR446 (Europe, licence-free)', 'UHF CB (Australia)']], ['Use', ['Adult outdoor use', 'Child\'s toy']]])
cb = take('CB radio')
tt(cb, [['Fitted to', ['Vehicle', 'Home base', 'Handheld']], ['Modulation', ['AM', 'AM/FM', 'AM/SSB']]])
lf = sh('Licence-free & citizens-band radios', 'Radios anyone can use without an amateur licence; an amateur handheld → Amateur transceivers.', [wk, cb])

cr = take('Communications receiver')
tt(cr, [['Era', ['Valve (wartime)', 'Transistor', 'Digital']], ['Origin', ['Civil', 'Military surplus']]])
see(cr, ['D3', 'Radio', 'broadcast radio for listening'])
rs = take('Radio scanner')
tt(rs, [['Format', ['Handheld', 'Base or mobile']], ['Decoding', ['Analogue', 'Digital trunking (P25, DMR, NXDN)']]])
sd = take('SDR receiver')
tt(sd, [['Coverage', ['Wideband (VHF/UHF)', 'HF only']], ['Direction', ['Receive only', 'Transmit-capable']], ['Form', ['USB dongle', 'Box with own screen']]])
pg = take('Pager')
tt(pg, [['Message', ['Tone only', 'Voice', 'Numeric', 'Alphanumeric']], ['Direction', ['One-way', 'Two-way']]])
rcv = sh('Receivers & pagers', 'Sets that only receive: shortwave and utility, scanned channels, software-tuned spectrum and paging calls.',
         [cr, rs, sd, pg], 'kinds by how it listens: tuned bands, scanned channels, software spectrum or paging calls')
radio = dict(n='Two-way & amateur radio', mode='mixed', note='Variety for amateur (ham) radio and scanners; tier for licence-free walkie-talkies; trade/public-safety radio stays kind-level only.',
             t='Radios that transmit or receive for hobby and personal use: amateur transceivers and station gear, licence-free radios, scanners and pagers; broadcast radio → D3.',
             ax='What does the radio do and under what licence: transmit on amateur bands, equip an amateur station, talk licence-free, or only receive?',
             s=[trx, stn, lf, rcv])

# =============== POWER ===============
pb = take('Power bank')
tt(pb, [['Capacity', ['Pocket (5,000–10,000 mAh)', '20,000 mAh', 'Laptop (25,000 mAh and up)']], ['Attachment', ['Magnetic (MagSafe / Qi2)', 'Built-in cable', 'Separate cable']]])
see(pb, ['D1', 'Laptop charger & battery', 'a battery for a laptop'])
bc = take('Phone battery case')
tt(bc, [['Charging in', ['Cable', 'Qi wireless']], ['Extra capacity', ['Half a charge', 'A full charge']]])
port = sh('Portable power', 'Batteries carried with the phone; a mains charger → Chargers & docks.', [pb, bc])
wc = nk('Wall charger', 'Plug-in mains adapter that charges a phone, tablet or watch through a cable.', S['chg'],
        [['Ports', ['One', 'Two', 'Three or more']], ['Output', ['20 W', '45 W', '65 W or more']], ['Chip', ['Silicon', 'Gallium nitride (GaN)']]])
see(wc, ['D1', 'Multi-device charger', 'a charger built for many devices at a desk'])
cdk = take('Charging dock')
cdk['d'] = 'Pad, puck, stand or dock that charges one or more devices, often wirelessly; wired multi-port chargers are in Computers & Peripherals.'
tt(cdk, [['Form', ['Pad or puck', 'Stand', 'Dock']], ['Devices at once', ['One', 'Two (2-in-1)', 'Three (3-in-1)']],
         ['Charges', ['Phone', 'Watch', 'Earbuds']], ['Standard', ['Qi', 'Qi2 / MagSafe']]])
see(cdk, ['D1', 'Multi-device charger', 'wired charger for many devices'])
cc = nk('Car charger', 'Adapter for the vehicle\'s 12-volt socket that charges a phone or tablet on the road.', S['chg'],
        [['Ports', ['One', 'Two']], ['Output', ['20 W', '45 W or more']]])
sc = nk('Solar charger', 'Portable solar panel that charges a power bank or phone off the grid.', S['chg'],
        [['Panel', ['Foldable', 'Rigid']], ['Output', ['5–10 W', '20–30 W or more']]])
chg = sh('Chargers & docks', 'Units that feed power to a device from the mains, a car or the sun; a battery pack → Portable power.',
         [wc, cdk, cc, sc], 'kinds by where the power comes from: a wall socket, a wireless dock, a car socket or sunlight')
power = dict(n='Power & charging', mode='tier', note='Tier: market-covering brands plus independent test winners.',
             t='Batteries and chargers that keep phones, tablets and watches running; household battery chargers → C8, laptop chargers → D1.',
             ax='Does it carry power with you, or deliver it from a wall, car or the sun?',
             s=[port, chg])

# =============== CASES & ACCESSORIES ===============
pc = take('Phone case')
tt(pc, [['Style', ['Slim shell', 'Rugged', 'Folio wallet', 'Bumper', 'Clear']], ['Material', ['Silicone', 'Leather', 'Polycarbonate', 'TPU']],
        ['Features', ['Magnetic (MagSafe-compatible)', 'Kickstand']]])
spr = take('Screen protector')
tt(spr, [['Material', ['Tempered glass', 'Film (TPU)', 'Hydrogel']], ['Finish', ['Clear', 'Matte', 'Privacy']]])
see(spr, ['D4', 'Screen protector', 'the same product for a camera screen'])
tc = take('Tablet & e-reader case')
tt(tc, [['Fits', ['Tablet', 'E-reader']], ['Style', ['Folio with stand', 'Sleeve', 'Bumper shell']]])
prot = sh('Protection', 'Cases and films that guard a device\'s body and screen.', [pc, spr, tc])
ws = take('Watch strap')
tt(ws, [['Material', ['Silicone', 'Woven nylon', 'Leather', 'Metal link']], ['Attachment', ['Proprietary lug', 'Quick-release']]])
see(ws, ['A5', 'Watch strap', 'straps for mechanical watches'])
gr = nk('Phone grip & stand', 'Small grip fixed to the back of a phone that gives a hold and props it up.', S['pop'],
        [['Form', ['Pop-out collapsible grip', 'Ring', 'Loop strap']], ['Attachment', ['Adhesive', 'Magnetic', 'Part of the case']]],
        r=[['PopSockets', 'PopSockets']])
pmt = nk('Phone mount', 'Holder that fixes a phone or tablet to a dashboard, bike or desk.', S['acc'],
         [['Placed on', ['Car dashboard', 'Car air vent', 'Bike handlebar', 'Desk']], ['Hold', ['Clamp', 'Magnet', 'Wireless-charging cradle']]])
hold = sh('Holding & wearing', 'Straps, grips and mounts that let you wear, hold or place the device.', [ws, gr, pmt])
sty = take('Stylus')
tt(sty, [['Type', ['Passive capacitive', 'Active pen with pressure']], ['Fits', ['One tablet range', 'Phone with built-in slot', 'Any touchscreen']]])
kc = take('Tablet keyboard cover')
tt(kc, [['Form', ['Folio case with keyboard', 'Detachable keyboard', 'Separate Bluetooth keyboard']], ['Trackpad', ['With trackpad', 'Without']]])
see(kc, ['D1', 'Everyday keyboard', 'a keyboard for a computer'])
pca = take('Phone camera & creator add-on')
tt(pca, [['Adds', ['Gimbal stabiliser', 'Selfie stick', 'Clip-on lens', 'Microphone']]])
inp = sh('Input & creator add-ons', 'Add-ons that give a device a pen, a keyboard or better pictures and sound.', [sty, kc, pca])
cases = dict(n='Cases & accessories', mode='tier', note='Tier: market-covering brands, no SKU lists.',
             t='Add-ons made to fit a phone, tablet or watch: protection, holding and input; headphones → D3, camera lenses and tripods → D4, cables → D1.',
             ax='What does the add-on do for the device: protect it, hold or wear it, or add a capability?',
             s=[prot, hold, inp])

assert not pool, list(pool)

out = dict(src)
out['ax'] = 'What is the device mainly for: calling, apps and reading on a flat screen, wearing, organising, finding the way, radio, or powering and protecting the rest?'
out['key'] = [
    '1. Is it a handset for calls and messages, mobile or fixed-line? → Phones',
    '2. Is it a flat screen held in the hands for apps, reading or handwriting? → Tablets & e-readers',
    '3. Is it worn on the wrist, finger, chest or face to track the body or show notifications? → Wearables',
    '4. Is it a pocket device for the diary, notes or translation that is not a phone? → PDAs, organisers & translators',
    '5. Does it show where you are, report where something is, or call for rescue beyond phone coverage? → Navigation, trackers & safety beacons',
    '6. Does it send or receive by radio: an amateur station, walkie-talkie, CB, scanner or pager? → Two-way & amateur radio',
    '7. Does it store or deliver power to charge devices? → Power & charging',
    '8. Is it a case, strap, grip, stylus, keyboard or add-on made to fit a phone, tablet or watch? → Cases & accessories',
    '<i>Precedence: a sport GPS watch is a wearable (step 3) before a navigator (step 5); a satellite phone sits in step 5, not 1; a battery case is power (step 7) before a case (step 8).</i>']
out['depts'] = [phones, tabs, wear, pdas, nav, radio, power, cases]

# reorder keys sensibly
order = ['c', 'rev', 'lead', 'ax', 'key', 'b', 'depts']
out = {k: out[k] for k in order if k in out}
assert out['lead']
json.dump(out, open(W + 'D2.new.json', 'w'), ensure_ascii=False, indent=1)

kinds = [k for dp in out['depts'] for s in dp['s'] for k in s['k']]
after = dict(depts=len(out['depts']), shelves=sum(len(d['s']) for d in out['depts']), kinds=len(kinds), arch=sum(len(k.get('x', [])) for k in kinds))
print('before', before, 'after', after)
# see-target check
for k in kinds:
    for a, b, c in k.get('see', []):
        if a == 'D2':
            assert b in {x['n'] for x in kinds}, (k['n'], b)
        else:
            names = set()
            for fn in (R + f'reader/{a}.json', R + f'out/{a}.json'):
                if os.path.exists(fn):
                    d = json.load(open(fn))
                    names |= {x['n'] for dp in d['depts'] for s in dp['s'] for x in s['k']}
            rn = {x['n'] for dp in json.load(open(R + f'reader/{a}.json'))['depts'] for s in dp['s'] for x in s['k']}
            print('see check', a, b, b in rn, b in names)
