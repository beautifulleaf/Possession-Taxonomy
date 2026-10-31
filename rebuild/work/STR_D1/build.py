import json, os, sys, copy
ROOT = '/home/user/Possession-Taxonomy/rebuild/'
W = ROOT + 'work/STR_D1/'
sys.path.insert(0, W)
from tt_data import TT
d = json.load(open(W + 'bak/D1.json'))   # always from backup
before = dict(depts=len(d['depts']), shelves=sum(len(x['s']) for x in d['depts']),
              kinds=sum(len(s['k']) for x in d['depts'] for s in x['s']),
              arch=sum(len(k.get('x', [])) for x in d['depts'] for s in x['s'] for k in s['k']))
K = {k['n']: k for dp in d['depts'] for s in dp['s'] for k in s['k']}
OLDB = {dp['n']: dp.get('b', []) for dp in d['depts']}
used = set()
WP = 'https://en.wikipedia.org/wiki/'

def kd(n):
    used.add(n); return K[n]

def newkind(n, dfn, s, a='', x=None, see=None):
    k = {'n': n, 'a': a, 'd': dfn, 's': s}
    if x: k['x'] = x
    K[n] = k; used.add(n); return k

def arch(n, dfn, s, mk='', y='', a=''):
    return {'n': n, 'a': a, 'd': dfn, 'mk': mk, 'y': y, 's': s, 'v': []}

def to_range(kname, anames):
    k = K[kname]; keep = []
    r = k.setdefault('r', [])
    have = {x[0].lower() for x in r}
    for x in k.get('x', []):
        if x['n'] in anames:
            if x['n'].lower() not in have: r.append([x['n'], x.get('mk', '')]); have.add(x['n'].lower())
        else: keep.append(x)
    if keep: k['x'] = keep
    else: k.pop('x', None)

def move_x(src, dst, names):
    s, t = K[src], K[dst]; keep = []
    for x in s.get('x', []):
        (t.setdefault('x', []) if x['n'] in names else keep).append(x) if x['n'] not in names else t.setdefault('x', []).append(x)
    s['x'] = keep
    if not keep: s.pop('x')

def move_m(src, dst, names):
    s, t = K[src], K[dst]; keep = []
    for m in s.get('m', []):
        if m[0] in names: t.setdefault('m', []).append(m)
        else: keep.append(m)
    s['m'] = keep
    if not keep: s.pop('m')

# ---------------------------------------------------------------- renames
RENAMES = {'Home computer (keyboard computer)': 'Home computer', 'Keyboard': 'Mechanical keyboard'}
for old, new in RENAMES.items():
    K[new] = K.pop(old); K[new]['n'] = new
K['Mechanical keyboard']['a'] = 'enthusiast keyboard · computer keyboard'
K['Mechanical keyboard']['d'] = 'Ready-built keyboard sold for its feel and sound, with mechanical, Topre, buckling-spring or Hall-effect switches.'
K['Home computer']['a'] = 'keyboard computer · 8-bit micro'

# ---------------------------------------------------------------- re-homing of archetypes / models
# Workstation split out of Tower PC
newkind('Workstation', 'Desktop computer built for one professional user, with workstation processors, memory and graphics; a gaming tower → Tower PC.',
        WP + 'Workstation', a='professional desktop · deskside workstation')
move_x('Tower PC', 'Workstation', {'Mac Pro', 'HP Z workstation'})
move_m('Tower PC', 'Workstation', {'Precision 3680', 'Precision 5860', 'Precision 7960'})
K['Tower PC']['d'] = 'Complete desktop computer in a tower case with the parts fitted, sold for gaming, office or creative work; a professional machine → Workstation.'
K['Workstation'].setdefault('r', []).append(['Z series', 'HP']) if False else None
# Convertible laptop split out of Laptop; Netbook added
newkind('Convertible laptop', 'Laptop whose hinge lets the screen fold, rotate or slide so the machine works as a tablet; the keyboard stays attached.',
        WP + '2-in-1_PC', a='2-in-1 laptop · flip laptop · tablet PC',
        x=[arch('IBM ThinkPad 360P', 'Pen-operated notebook whose display rotates backward and closes over the keyboard as a tablet.', WP + '2-in-1_PC', mk='IBM', y='1994')])
move_m('Laptop', 'Convertible laptop', {'Envy x360'})
newkind('Netbook', 'Compact, low-cost laptop built mainly for the internet, with a 5–12 inch screen and no optical drive.',
        WP + 'Netbook', a='mini-notebook · ultra-portable',
        x=[arch('Asus Eee PC 700', 'First mass-produced netbook, with a 7-inch screen and a custom Linux.', WP + 'Netbook', mk='ASUS', y='2007')])
K['Laptop']['d'] = 'Portable computer with its screen and keyboard in one folding clamshell body; a hinge that turns it into a tablet → Convertible laptop.'
# Compaq Concerto promoted to archetype of Detachable 2-in-1
move_m('Detachable 2-in-1', 'Detachable 2-in-1', {'Compaq Concerto'}) if False else None
K['Detachable 2-in-1']['m'] = [m for m in K['Detachable 2-in-1']['m'] if m[0] != 'Compaq Concerto']
K['Detachable 2-in-1']['x'].insert(0, arch('Compaq Concerto', 'Earliest device that counts as a detachable 2-in-1, with a cabled detachable keyboard.', WP + '2-in-1_PC', mk='Compaq', y='1993'))
# Home server stays. Vintage additions
K['Home computer']['x'] += [
    arch('Commodore 128', 'Commodore home computer listed with the 8-bit keyboard micros of the 1980s.', WP + 'Home_computer', mk='Commodore'),
    arch('Acorn Atom', 'Acorn keyboard micro that came before the BBC Micro.', WP + 'Home_computer', mk='Acorn Computers')]
K['Vintage desktop computer']['x'] += [
    arch('IBM PCjr', 'IBM home-market PC of 1984.', WP + 'Home_computer', mk='IBM', y='1984'),
    arch('Tandy 1000', 'IBM-compatible home PC from Tandy.', WP + 'Home_computer', mk='Tandy Corporation', y='1984'),
    arch('Amstrad PC1512', 'Budget IBM-compatible PC from Amstrad.', WP + 'Home_computer', mk='Amstrad', y='1986')]
# SBC archetypes
K['Single-board computer']['x'] += [
    arch('Odroid', 'Korean line of ARM single-board computers; the first board appeared in 2009.', WP + 'ODROID', mk='Hardkernel', y='2009'),
    arch('Banana Pi', 'Raspberry Pi-style board line; first board BPI-M1 released in 2014.', WP + 'Banana_Pi', mk='Shenzhen SINOVOIP', y='2014'),
    arch('Pine64 boards', 'Single-board computers from Pine64, named among the hobby SBC families.', WP + 'Single-board_computer', mk='Pine64')]
# demote ranges/makers
to_range('Motherboard', {x['n'] for x in K['Motherboard']['x']})
to_range('Memory (RAM)', {x['n'] for x in K['Memory (RAM)']['x']})
to_range('Artisan keycap', {x['n'] for x in K['Artisan keycap']['x']})
to_range('Custom liquid-cooling parts', {'EK custom loop parts'})
to_range('Security key', {'Yubico Security Key'})
to_range('Mouse', {'Apple mouse'})
# new kinds: peripherals, keyboards, printing
newkind('External trackpad', 'Separate touch surface that moves the pointer by finger, for a desktop or beside a laptop; a trackball → Trackball.',
        WP + 'Touchpad', a='standalone touchpad · wireless trackpad')
K['External trackpad']['r'] = [['Magic Trackpad', 'Apple']]
newkind('Wrist rest', 'Cushion or block that supports the wrists in front of a keyboard, sold in wood, resin or foam.', 'https://kbdfans.com/', a='palm rest')
newkind('Keyboard PCB', 'Circuit board that holds the switches and sends keypresses, sold separately for custom keyboards.', 'https://kbdfans.com/', a='keyboard circuit board')
newkind('Keyboard case', 'Outer shell of a custom keyboard, sold on its own in aluminium, plastic, acrylic or wood.', 'https://kbdfans.com/', a='keyboard chassis')
newkind('Switch tester', 'Small board or set of keyboard switches for trying their feel before buying a pack.', 'https://kbdfans.com/', a='switch sampler')
newkind('Label printer', 'Printer for self-adhesive labels and tags; one with its own keyboard and display is a label maker. A document printer → Printer.',
        WP + 'Label_printer', a='label maker · thermal label printer',
        x=[arch('Brother P-touch', 'Label-maker line that prints on tape cartridges; the P-Touch 540 and 65 are shown among label makers.', WP + 'Label_printer', mk='Brother')])
newkind('3D scanner', 'Device that records the shape of a real object as a point cloud or mesh that becomes a 3D model.', WP + '3D_scanning', a='3D scanning device')

# ---------------------------------------------------------------- see links
SEE = {
 'Detachable 2-in-1': [['D2', 'Tablet', 'a tablet sold on its own']],
 'Convertible laptop': [['D2', 'Tablet', 'a tablet without a laptop base']],
 'Mini PC': [['E5', 'Handheld gaming PC', 'handheld with a built-in screen and controls']],
 'Retro computer re-creation': [['E5', 'Handheld gaming PC', 'modern handheld that emulates old games']],
 'CRT monitor': [['D3', 'CRT television and video monitor', 'television-type tube for video']],
 'Floppy disk drive': [['E5', 'Optical drive emulator', 'solid-state replacement for a console drive']],
 'Memory card': [['E5', 'Console memory card', 'card made for one games console']],
 'Pen tablet': [['D2', 'Stylus', 'pen for a phone or tablet'], ['D2', 'Tablet', 'tablet with a built-in computer']],
 'Microphone': [['E3', 'Dynamic microphone', 'studio and stage microphones']],
 'Macro pad': [['E3', 'Pad controller', 'pads for playing music']],
 'Multi-device charger': [['D2', 'Power bank', 'portable battery'], ['D2', 'Charging dock', 'dock for one phone']],
 'Sound card': [['E3', 'Audio interface', 'music-recording interface']],
 'Monitor arm or stand': [['B3', 'Monitor light bar', 'lamp that sits on the screen']],
 'Laptop accessory': [['A4', 'Laptop backpack', 'bag that carries the laptop']],
 'Home server': [['I1', 'Home server software', 'the software it runs']],
 '3D printer': [['I1', '3D printing slicer', 'software that prepares the print']],
 'Breadboard & prototyping board': [['C1', 'Soldering iron', 'tool for fixing the parts']],
 'Passive components': [['C1', 'Multimeter', 'tool for testing them']],
 'Everyday keyboard': [['D2', 'Tablet keyboard cover', 'keyboard made for one tablet']],
 'UPS': [['D2', 'Power bank', 'small portable battery']],
 'Video capture device': [['I1', 'Screen recorder and streaming software', 'software capture']],
 'Internal PC cable': [['C8', 'Cable', 'cable sold by length']],
 'Laptop charger & battery': [['C8', 'Battery charger', 'charger for loose batteries']],
 'Optical drive': [['E5', 'Optical drive emulator', 'solid-state replacement for a console drive']],
 'Workstation': [['D1', 'Tower PC', 'gaming and office tower']],
 'Tower PC': [['D1', 'Workstation', 'professional desktop']],
 'Mechanical keyboard': [['D1', 'Keyboard kit', 'same keyboard sold unbuilt']],
 'Keyboard kit': [['D1', 'Mechanical keyboard', 'same keyboard sold built']],
 'Everyday keyboard ': [],
 'Webcam': [['B8', 'Security camera', 'camera for watching a space']],
}
for n, v in SEE.items():
    if v: K[n]['see'] = v

# ---------------------------------------------------------------- tt
for n, tt in TT.items():
    k = K[n]; k['tt'] = tt; k.pop('t', None)
for n, k in K.items():
    if 't' in k and 'tt' not in k: print('NO TT', n)

# ---------------------------------------------------------------- structure
def shelf(n, t, ax, names):
    for x in names: assert x in K, x
    used.update(names)
    o = {'n': n, 't': t}
    if ax: o['ax'] = ax
    o['s_'] = None; o.pop('s_')
    o['k'] = [K[x] for x in names]
    return o

def dept(n, mode, note, t, ax, shelves, b=None):
    o = {'n': n, 'mode': mode}
    if note: o['note'] = note
    o['b'] = b or []; o['t'] = t; o['ax'] = ax; o['s'] = shelves
    return o

D = []
D.append(dept('Computers', 'mixed', 'Tier for everyday laptops and desktops; named lines for the classics.',
  'Finished modern computers you switch on and use, from laptops to desktops, workstations and home servers; loose parts → PC components, old machines → Vintage & retro computing.',
  'What form is the machine: carried, on the desk, or serving other machines?',
  [shelf('Laptops & 2-in-1s', 'Portable computers with the screen and keyboard together: laptops, convertibles, detachables, Chromebooks and netbooks; a plain tablet → D2 tablets.',
         'kinds by how the screen and keyboard relate: fixed clamshell, hinge that flips, screen that detaches, ChromeOS, small and cheap',
         ['Laptop', 'Convertible laptop', 'Detachable 2-in-1', 'Chromebook', 'Netbook']),
   shelf('Desktops & mini PCs', 'Complete desktop machines sold ready to use, from towers and all-in-ones to small boxes and unbuilt kits; a professional machine → Workstations & servers.',
         'kinds by size and build: tower, all-in-one, low desktop, small box, kit',
         ['Tower PC', 'All-in-one PC', 'Small-form-factor desktop', 'Mini PC', 'Barebone kit']),
   shelf('Workstations & servers', 'Machines built for professional work or for serving other devices: workstations for 3D, video and engineering; servers kept at home for storage and virtual machines.',
         None, ['Workstation', 'Home server'])],
  OLDB['Computers']))
D.append(dept('Vintage & retro computing', 'variety', 'Collectors browse by machine family, then by model and version.',
  'Computers and period add-ons from the 1970s to the 1990s, and modern re-creations of them; a current machine → Computers.',
  'Is it a machine of the period, a modern re-creation, or a period peripheral?',
  [shelf('Period machines', 'Complete computers of the 1970s to 1990s, from keyboard micros and desktops to workstations, portables and bare kits; a modern copy → Re-creations.',
         'kinds by body and size: keyboard-case micro, desktop with separate unit, workstation, carried, pocket, bare board',
         ['Home computer', 'Vintage desktop computer', 'Vintage workstation', 'Luggable & vintage portable', 'Pocket computer', 'Trainer & single-board kit (vintage)']),
   shelf('Re-creations', 'New machines that copy a classic computer in emulation or programmable logic, such as THEC64 or the ZX Spectrum Next; a restored original → Period machines.',
         None, ['Retro computer re-creation']),
   shelf('Period peripherals', 'Displays and drives made for the old machines, still used with them: tube monitors and floppy drives, plus modern floppy emulators.',
         None, ['CRT monitor', 'Floppy disk drive'])]))
D.append(dept('PC components', 'mixed', 'Parts department: builders compare and upgrade; variety for CPU and GPU lines, tier for the rest.',
  'Parts fitted inside a desktop PC that builders choose and swap: processor, board, memory, cards, case, power and cooling; storage → Storage.',
  'What job does the part do in the build: compute, add a function, house and power, or cool?',
  [shelf('Processors, motherboards & memory', 'The platform that does the computing: the processor, the board it sits in and the memory beside it; a graphics chip on a card → Graphics & expansion cards.',
         None, ['Processor', 'Motherboard', 'Memory (RAM)']),
   shelf('Graphics & expansion cards', 'Cards and boxes that add a function to the platform: graphics first, then sound, capture, network, ports and TV.',
         'kinds by what the card adds: graphics, graphics outside the case, audio, video capture, network, ports, broadcast TV',
         ['Graphics card', 'External GPU enclosure', 'Sound card', 'Video capture device', 'Network card', 'I/O expansion card', 'TV tuner card']),
   shelf('Cases, power & cabling', 'What houses the parts and feeds them: the case, the power supply and the cables inside.', None,
         ['PC case', 'PC power supply', 'Internal PC cable']),
   shelf('Cooling', 'Parts that move heat away: coolers, fans and the paste between chip and cooler.',
         'kinds from the chip outward: interface material, air cooler, liquid cooler, fans, controllers',
         ['Thermal paste & pads', 'CPU air cooler', 'AIO liquid cooler', 'Custom liquid-cooling parts', 'Case fan', 'Fan controller'])],
  OLDB['PC components']))
D.append(dept('Storage', 'tier', 'People pick a reliable drive; brands covering the market plus test winners.',
  'Devices that keep files, from drives fitted inside to portable drives, cards and network storage; a cloud service → Online Services.',
  'Where does the data live: in a drive inside the computer, in a portable store, or on the network?',
  [shelf('Internal drives', 'Drives fitted inside a computer: solid-state and hard disk drives, and disc drives; one in its own case → External & portable storage.',
         None, ['Internal SSD', 'Internal HDD', 'Optical drive']),
   shelf('External & portable storage', 'Storage you carry or plug in from outside: drives in a case, flash sticks, memory cards and the cases that make a bare drive external.',
         'kinds from drive to card: external SSD, external hard disk, case for a bare drive, flash stick, memory card',
         ['External SSD', 'External HDD', 'Drive enclosure', 'USB flash drive', 'Memory card']),
   shelf('Network storage', 'Storage that serves files over the home network; a general computer kept as a server → Workstations & servers.',
         None, ['NAS'])], OLDB['Storage']))
D.append(dept('Monitors & desk setup', 'tier', 'Tier for monitors and desk gear; independent tests decide.',
  'Screens and the things that hold, cushion or capture at the desk; a mouse or keyboard → Pointing & input devices, a television → D3.',
  'What is it for at the desk: showing the picture, holding the gear, or capturing you?',
  [shelf('Displays', 'Screens made to be used with a computer; a television or projector → D3.', None, ['Monitor']),
   shelf('Stands, mounts & desk surfaces', 'Things that hold or lie under the gear: monitor arms, laptop stands and desk mats.', None,
         ['Monitor arm or stand', 'Laptop accessory', 'Mouse pad or desk mat']),
   shelf('Webcams & microphones', 'Devices that capture you for calls and streaming; studio microphones for music → E3.', None, ['Webcam', 'Microphone'])],
  OLDB['Monitors & peripherals'][:2]))
D.append(dept('Pointing & input devices', 'mixed', 'Tier for everyday devices; variety at the pen-tablet and pointing-device end.',
  'Devices the hand moves, draws with or types on at a computer, other than enthusiast keyboards → Enthusiast keyboards; a console controller → E5.',
  'What does the hand do: point, draw, type or trigger shortcuts?',
  [shelf('Pointing & drawing devices', 'Devices moved or touched to steer a pointer or draw: mice, trackballs, trackpads and pen tablets.',
         'kinds by what the hand does: move over a surface, spin a ball, stroke a pad, draw with a pen',
         ['Mouse', 'Trackball', 'External trackpad', 'Pen tablet']),
   shelf('Typing & shortcut devices', 'Office keyboards, number pads and shortcut pads; a keyboard bought for its feel → Enthusiast keyboards.', None,
         ['Everyday keyboard', 'Numeric keypad', 'Macro pad'])],
  OLDB['Monitors & peripherals'][2:]))
D.append(dept('Enthusiast keyboards', 'variety', 'Collector and custom-build view: layout, board, switch, keycap set.',
  'Keyboards bought for their feel and sound, and the kits and parts to build or tune them; an office keyboard → Pointing & input devices.',
  'Is it a whole keyboard, a kit to build one, or a part that changes how it feels?',
  [shelf('Finished keyboards', 'Ready-built keyboards sold for their feel: mechanical boards and split or ergonomic designs.', None,
         ['Mechanical keyboard', 'Split & ergonomic keyboard']),
   shelf('Kits & board parts', 'The body of a custom keyboard, sold as a kit or as case and circuit board separately.',
         None, ['Keyboard kit', 'Keyboard case', 'Keyboard PCB']),
   shelf('Switches, keycaps & feel parts', 'Parts under and on the fingers that change how a keyboard types and sounds, plus the tools and extras around it.',
         'kinds from the finger down: keycap, switch, plate and stabiliser, then cable and rest',
         ['Keycap set', 'Artisan keycap', 'Keyboard switches', 'Switch tester', 'Keyboard plate', 'Keyboard stabiliser', 'Coiled keyboard cable', 'Wrist rest'])]))
D.append(dept('Printing & 3D printing', 'mixed', 'Tier for home printers; variety at the 3D-printing hobby end.',
  'Machines that put a design on paper, labels or into objects, and what they use; a scanner is here because it sits beside the printer.',
  'What does the machine make or read: pages and labels, scans, or 3D objects?',
  [shelf('Printers, scanners & supplies', 'Machines that print or scan pages and labels, with their ink and toner; a 3D printer → 3D printing.',
         'kinds by job: print, print and scan, label, scan only, supplies',
         ['Printer', 'Multifunction printer', 'Label printer', 'Scanner', 'Ink & toner cartridge']),
   shelf('3D printing', 'Machines that build objects layer by layer, the material they use, upgrades and scanners that capture an object to copy.',
         'kinds along the print chain: scan, machine, material, upgrade',
         ['3D scanner', '3D printer', '3D-printer filament', '3D-printing resin', '3D-printer upgrade parts'])]))
D.append(dept('Networking', 'tier', 'People pick a reliable box; market brands plus test winners.',
  'Boxes and cables that connect the home to the internet and its devices to each other; a phone hotspot → D2.',
  'Where does it sit: at the line from the provider, spreading wireless, or on the wired links?',
  [shelf('Internet entry', 'Devices that bring the provider line in and share it: modems and Wi-Fi routers; a router built into a modem counts as the modem.',
         None, ['Modem', 'Wi-Fi router']),
   shelf('Wireless coverage', 'Devices that carry the network to rooms the router does not reach: access points, extenders and powerline adapters.', None,
         ['Access point', 'Range extender', 'Powerline adapter']),
   shelf('Wired network', 'Devices and cables for wired links: switches and Ethernet cables.', None, ['Network switch', 'Ethernet cable'])]))
D.append(dept('Cables, hubs & power', 'tier', 'Quality-of-life accessories; a few trusted brands per kind.',
  'Cables, hubs, docks and chargers that connect or power a computer; a cable sold by the metre → C8.',
  'What does it carry or supply: signal on a cable, more ports from one, or power?',
  [shelf('Cables', 'Cables that carry data or video between devices; a network cable → Networking.', None, ['USB cable', 'Display cable']),
   shelf('Hubs, docks & switches', 'Devices that give one computer more ports or let several computers share them.', None,
         ['USB hub & adapter', 'Docking station', 'KVM switch']),
   shelf('Chargers & backup power', 'Chargers for many devices, a laptop’s own charger and battery, and backup power for a mains cut.', None,
         ['Multi-device charger', 'Laptop charger & battery', 'UPS'])]))
D.append(dept('Security & crypto hardware', 'mixed', 'Small devices that prove identity or hold keys.',
  'Pocket devices that prove who you are when signing in or keep cryptocurrency keys offline; a house lock → B8.',
  'What does the device protect: a sign-in or a cryptocurrency balance?',
  [shelf('Security keys & hardware wallets', 'Security keys for signing in and hardware wallets for crypto keys.', None, ['Security key', 'Hardware wallet'])]))
D.append(dept('Electronics & maker boards', 'mixed', 'Variety for maker boards; components kept kind-level for hobby builders.',
  'Boards, kits and loose parts for learning electronics and building projects; a finished computer → Computers.',
  'Is it a ready board that runs code, a way to build circuits, or a loose part?',
  [shelf('Maker boards', 'Ready boards that run programs: full single-board computers, microcontroller boards and the add-ons that plug onto them.',
         'kinds by what runs on the board: an operating system, one program, an add-on for either',
         ['Single-board computer', 'Microcontroller board', 'Maker add-on board']),
   shelf('Kits & prototyping', 'Boxed learning sets and boards for trying circuits before soldering.', None,
         ['Electronics starter kit', 'Breadboard & prototyping board']),
   shelf('Electronic components', 'Loose parts for circuits: passive parts, chips and LEDs, then connectors, relays and sensors.',
         None, ['Passive components', 'Semiconductors & LEDs', 'Connectors, relays & modules'])]))
for dp in D:
    if not dp['b']: dp.pop('b')

unused = set(K) - used
assert not unused, unused
d['depts'] = D
d['ax'] = 'What is the thing for: is it a whole computer, a part inside one, something that stores, shows or captures, something you type or point with, a printer, a network box, a cable or power unit, a token, or a board for building?'
d['key'] = [
 '1. Is it an old computer, a modern copy of one, or a drive or monitor made for the old machines? → Vintage & retro computing',
 '2. Is it a finished modern computer you switch on and use (laptop, desktop, workstation, home server)? → Computers',
 '3. Is it a board, kit or loose part for building circuits or programs (maker board, breadboard, resistor)? → Electronics & maker boards',
 '4. Is it a keyboard, kit, switch or keycap bought for its feel and sound? → Enthusiast keyboards',
 '5. Is it a part fitted inside a desktop PC (processor, board, memory, card, case, power, cooling)? → PC components',
 '6. Does it keep files (drive, flash stick, memory card, NAS)? → Storage',
 '7. Does it print, scan or make objects layer by layer? → Printing & 3D printing',
 '8. Does it connect the home to the internet or devices to each other? → Networking',
 '9. Is it a pocket token or wallet that proves identity or holds crypto keys? → Security & crypto hardware',
 '10. Is it a screen, stand, desk mat, webcam or microphone? → Monitors & desk setup',
 '11. Is it a mouse, pen tablet, trackpad, office keyboard or shortcut pad? → Pointing & input devices',
 '12. Is it a cable, hub, dock, charger or backup battery? → Cables, hubs & power',
 '<i>Precedence: a keyboard bought for its feel is step 4 before an office keyboard (step 11); a replacement laptop battery is step 12; a console controller → E5, headphones and speakers → D3, a phone or tablet → D2.</i>']

# ---------------------------------------------------------------- write
after = dict(depts=len(D), shelves=sum(len(x['s']) for x in D), kinds=sum(len(s['k']) for x in D for s in x['s']),
             arch=sum(len(k.get('x', [])) for x in D for s in x['s'] for k in s['k']))
print('before', before, 'after', after)
tmp = ROOT + 'out/D1.json.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, ROOT + 'out/D1.json')
# renames
json.dump(RENAMES, open(ROOT + 'out/D1_renames.json', 'w'), ensure_ascii=False, indent=1)
# brands
bp = ROOT + 'out/D1_brands.json'
b = json.load(open(W + 'bak/D1_brands.json'))
have = {x['n'].lower() for x in b['b']}
for nb in [{'n': 'Hardkernel', 'c': 'South Korea', 'seg': 'Specialist', 'kf': 'Odroid boards', 'd': 'Korean maker of the Odroid single-board computers.', 'sig': ['Odroid'], 's': WP + 'ODROID'},
           {'n': 'Shenzhen SINOVOIP', 'c': 'China', 'seg': 'Specialist', 'kf': 'Banana Pi boards', 'd': 'Shenzhen maker of the Banana Pi single-board computers.', 'sig': ['Banana Pi'], 's': WP + 'Banana_Pi'},
           {'n': 'Pine64', 'c': 'United States', 'seg': 'Specialist', 'kf': 'open-source boards', 'd': 'Maker of Pine64 single-board computers.', 's': WP + 'Single-board_computer'},
           {'n': 'Brother', 'c': 'Japan', 'seg': 'Mainstream', 'kf': 'printers and label makers', 'd': 'Maker of printers and the P-touch label makers.', 'sig': ['Brother P-touch'], 's': WP + 'Label_printer'}]:
    if nb['n'].lower() not in have: b['b'].append(nb)
json.dump(b, open(bp + '.tmp', 'w'), ensure_ascii=False)
os.replace(bp + '.tmp', bp)
json.dump({'before': before, 'after': after}, open(W + 'counts.json', 'w'))
