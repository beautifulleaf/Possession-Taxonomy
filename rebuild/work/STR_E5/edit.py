import json, shutil, os, copy, re
R = '/home/user/Possession-Taxonomy/rebuild/'
W = R + 'work/STR_E5/'
os.makedirs(W + 'bak', exist_ok=True)
for f in ('out/E5.json', 'out/E5_brands.json', 'out/E5_moves.json'):
    b = W + 'bak/' + os.path.basename(f)
    if not os.path.exists(b):
        shutil.copy(R + f, b)
d = json.load(open(W + 'bak/E5.json'))  # always start from backup

GC = 'https://en.wikipedia.org/wiki/Game_controller'
MC = 'https://en.wikipedia.org/wiki/List_of_microconsoles'
AC = 'https://en.wikipedia.org/wiki/Arcade_cabinet'
VR = 'https://en.wikipedia.org/wiki/List_of_virtual_reality_headsets'
NS = 'https://en.wikipedia.org/wiki/Nintendo_Selects'
CX = 'https://en.wikipedia.org/wiki/Atari_CX40_joystick'
DB = 'https://dragonbox.de/en/other-mod-kits'

K = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k
renames = {}
def A(n, d_, mk='', y='', s='', v=None, dt=None, a=''):
    x = {'n': n, 'a': a, 'd': d_, 'mk': mk, 'y': y, 's': s, 'v': v or []}
    if dt: x['dt'] = dt
    return x
def kind(n, d_, s, tt=None, x=None, a='', m=None):
    k = {'n': n, 'a': a, 'd': d_, 's': s}
    if tt: k['tt'] = tt
    if x: k['x'] = x
    if m: k['m'] = m
    K[n] = k
    return k

# ---- merges / renames -------------------------------------------------
# Joy-Con into Gamepad
jc = K.pop('Detachable split controller')
K['Gamepad']['x'].extend(jc['x'])
renames['Detachable split controller'] = 'Gamepad'
K['Gamepad']['d'] = 'A hand-held pad of buttons, d-pad and thumbsticks for a console or PC, from the NES pad to the split Joy-Con pair and adaptive pads.'
K['Gamepad']['x'].append(A('NeGcon', 'Namco twist-handled PlayStation pad for racing games.', 'Namco', '', GC))

# Pinball machine -> Modern pinball machine
K['Pinball machine']['n'] = 'Modern pinball machine'
K['Modern pinball machine'] = K.pop('Pinball machine')
K['Modern pinball machine']['d'] = 'A new-production pinball machine with a colour screen, sold by makers such as Stern and Jersey Jack, and licensed to films and bands.'
renames['Pinball machine'] = 'Modern pinball machine'

# XR display glasses -> XR glasses
K['XR display glasses']['n'] = 'XR glasses'
K['XR glasses'] = K.pop('XR display glasses')
renames['XR display glasses'] = 'XR glasses'
K['XR glasses']['see'] = [['D2', 'Smart glasses', 'worn as eyewear; this kind is a screen for a game or PC']]

# HDMI / RGB split
h = K['Internal HDMI or RGB mod kit']
h['n'] = 'Internal HDMI mod kit'
h['d'] = 'A board fitted inside a retro console, or an adapter on its digital port, that gives a digital HDMI picture.'
K['Internal HDMI mod kit'] = K.pop('Internal HDMI or RGB mod kit')
renames['Internal HDMI or RGB mod kit'] = 'Internal HDMI mod kit'
kind('RGB mod board', 'A small board that cleans up or amplifies a console\'s analogue RGB picture and sync for a SCART or component display.', DB,
     tt=[['Board type', ['RGB amplifier board', 'Sync-fix board', 'Universal RGB board']]])

# Rhythm "other" split
t = K.pop('Turntable, drum and other rhythm controller')
renames['Turntable, drum and other rhythm controller'] = 'DJ turntable controller'
xs = {x['n']: x for x in t['x']}
mods = {m[0]: m for m in t['m']}
kind('DJ turntable controller', 'A turntable or keys-and-turntable deck for DJ rhythm games.',
     'https://en.wikipedia.org/wiki/Rhythm_game_accessories',
     x=[xs['beatmania turntable controller'], xs['DJ Hero turntable']])
kind('Hand percussion controller', 'A drum, bongo, maraca or tambourine played with the hands for a rhythm game.',
     'https://en.wikipedia.org/wiki/Rhythm_game_accessories',
     tt=[['Instrument', ['Hand drum', 'Maracas', 'Tambourine']]],
     x=[xs['DK Bongos'], xs['Taiko drum controller'], xs['Samba de Amigo maracas']],
     m=[mods['Shakatto Tambourine']])
kind('Keyboard, baton & button-pad controller', 'A rhythm-game controller shaped like a keyboard, conductor\'s baton or arcade button pad rather than a guitar, drum or deck.',
     'https://en.wikipedia.org/wiki/Rhythm_game_accessories',
     tt=[['Instrument', ['Keyboard', 'Baton', 'Button pad']]],
     m=[mods["Pop'n Music controller"], mods['Rock Band 3 Wireless Pro Keyboard'], mods['Rock Band MIDI Pro-Adapter'], mods['Mad Maestro baton controller']])
K['Drum kit controller'].setdefault('m', []).append(mods['DrumMania controller'])
K['Guitar controller'].setdefault('m', []).append(mods['GuitarFreaks controller'])
assert not (set(xs) - {'beatmania turntable controller', 'DJ Hero turntable', 'DK Bongos', 'Taiko drum controller', 'Samba de Amigo maracas'})

# Motion cabinet split out of cockpit
cp = K['Cockpit arcade cabinet']
motion_m = [m for m in cp['m'] if m[0] in ('Sega R-360', 'Sega Storm-G', 'Sega VR-1', 'Simuline Cycraft')]
cp['m'] = [m for m in cp['m'] if m not in motion_m]
cp['d'] = 'Cabinet built around a seated player, enclosed or open, with vehicle-style controls and a fixed base.'
kind('Motion simulator arcade cabinet', 'A cabinet on hydraulics or motors that tilts, turns or shakes the seated player to match the screen.', AC,
     x=[A('Sega R360', 'Gyroscope cabinet that spins the player through full rotations; named on the arcade-cabinet page as a motion simulator.', 'Sega', '', AC)],
     m=motion_m)
kind('Deluxe vehicle-style arcade cabinet', 'A large sit-down cabinet with a replica seat, wheel or handlebars, made for driving and riding games.', AC,
     tt=[['Vehicle', ['Car', 'Motorbike', 'Aircraft']]])

# Generic archetypes -> dropped into types
def drop_arch(kn, an):
    k = K[kn]; k['x'] = [x for x in k['x'] if x['n'] != an]
drop_arch('Cassette or floppy game', 'Home-computer cassette game')
drop_arch('Game disc', 'Blu-ray game disc')
# Ranges -> r
def to_range(kn, an, maker=None):
    k = K[kn]
    for x in k['x']:
        if x['n'] == an:
            k['x'].remove(x)
            k.setdefault('r', []).append([an, maker or x.get('mk') or ''])
            return
    raise KeyError((kn, an))
RANGES = [
 ('FPGA & clone console', 'Analogue FPGA consoles', 'Analogue'), ('FPGA & clone console', 'Hyperkin RetroN', 'Hyperkin'),
 ('Plug-and-play & mini console', 'Plug It In & Play TV Games', 'Jakks Pacific'), ('Plug-and-play & mini console', 'Radica Play TV', 'Radica Games'),
 ('Plug-and-play & mini console', 'Atari Flashback', 'Atari'), ('LCD handheld game', 'Tiger handheld LCD games', 'Tiger Electronics'),
 ('Collector\'s edition', 'Limited Run Games release', 'Limited Run Games'),
 ('Racing wheel', 'Logitech Driving Force and G-series wheels', 'Logitech'), ('Racing wheel', 'Thrustmaster T-series wheels', 'Thrustmaster'),
 ('Racing wheelbase', 'Fanatec direct-drive bases', 'Fanatec'), ('Racing wheelbase', 'Moza R-series', 'Moza Racing'),
 ('Pedal set', 'Heusinkveld pedals', 'Heusinkveld Engineering'), ('Gear shifter', 'Heusinkveld shifters', 'Heusinkveld Engineering'),
 ('Sim cockpit or wheel stand', 'Playseat', 'Playseat'),
 ('Tethered VR headset', 'Pimax wide-FOV headsets', 'Pimax'),
 ('Candy (sit-down) arcade cabinet', 'SNK Neo Geo candy cabinets', 'SNK'),
 ('Home replica arcade cabinet', 'Arcade1Up cabinet', 'Arcade1Up'), ('Digital pinball cabinet', 'Arcade1Up pinball', 'Arcade1Up'),
]
demoted = []
for kn, an, mk in RANGES:
    to_range(kn, an, mk); demoted.append(an)
demoted += ['Home-computer cassette game (to type)', 'Blu-ray game disc (to type)']

# ---- new kinds --------------------------------------------------------
kind('Microconsole', 'A small, cheap set-top box that plays games from an app store, usually on Android, such as Ouya and Fire TV.', MC,
     tt=[['Operating system', ['Android', 'Fire OS', 'Apple tvOS', 'Proprietary']], ['Form', ['Box', 'Stick', 'Cube']]],
     x=[A('Ouya', 'Android microconsole from Ouya Inc., funded by crowdfunding.', '', '2013', MC),
        A('PlayStation TV', 'Sony set-top version of the Vita that plays Vita and PSP games on a TV.', 'Sony', '2013', MC),
        A('Fire TV', 'Amazon set-top box and stick with a games store.', '', '2014', MC),
        A('Nvidia Shield TV', 'Android TV box from Nvidia with game streaming.', '', '2015', MC)])
kind('Joystick', 'A single hand-held stick with one or more fire buttons, used on 1970s and 1980s consoles and home computers.', CX,
     tt=[['Handle', ['Ball-top', 'Bat-top']], ['Connection', ['Atari-style 9-pin port', 'USB']]],
     x=[A('Atari CX40 joystick', 'Atari single-button joystick that became the standard port for consoles and home computers.', 'Atari', '1978',
          CX, v=[{'n': 'CX10', 'mk': 'Atari', 'y': '1977', 'd': 'earlier joystick, replaced by the CX40'}])])
kind('Trackball controller', 'A ball turned by the palm to move a cursor or aim, used in arcade games and on some consoles.', GC)
kind('Quiz buzzer', 'A hand-held buzzer or large button pad for quiz and party games, one per player.', GC,
     tt=[['Form', ['Hand-held buzzer', 'Big button pad']]],
     x=[A('Buzz! buzzers', 'Four-player wired and wireless buzzer set for the Buzz! quiz series.', 'Sony', '2005', GC),
        A('Big Button Pad', 'Xbox 360 four-player button pad for Scene It? quiz games.', 'Microsoft', '2007', GC)])
kind('Budget re-release', 'A cheaper reprint of a best-selling game under a platform holder\'s budget label, with its own cover band or case.', NS,
     tt=[['Label type', ['Platform-holder budget label', 'Regional relabel', 'Publisher budget label']]],
     x=[A('Player\'s Choice', 'Nintendo budget label for million-selling games, renamed Nintendo Selects in 2011.', 'Nintendo', '1996', NS,
          v=[{'n': 'Nintendo Selects', 'mk': 'Nintendo', 'y': '2011', 'd': 'renamed label'},
             {'n': 'Nintendo Classics', 'mk': 'Nintendo', 'y': '', 'd': 'UK and Netherlands name'},
             {'n': 'Mario Classics', 'mk': 'Nintendo', 'y': '', 'd': 'Spanish name'}],
          dt='platform · region name · sales threshold')])
kind('Early VR head-mounted display', 'A pre-2000 headset from the first wave of virtual reality, collected as history rather than used.', VR,
     x=[A('VPL EyePhone', 'First commercial VR headset, from VPL Research.', '', '1989', VR),
        A('Virtuality 1000CS', 'Headset and pod system sold for arcades by Virtuality.', '', '1991', VR),
        A('Forte VFX1', 'Home-computer VR headset from Forte.', '', '1995', VR)])

# extra archetypes on existing kinds
K['Motion controller']['x'].append(A('Sega Activator', 'Floor ring that reads the player\'s body movement for Mega Drive games.', 'Sega', '1993', GC))
K['Paddle or spinner controller']['x'] += [
    A('Atari driving controller', 'Atari spinner dial made for Indy 500 and other driving games.', 'Atari', '1977', GC),
    A('Namco Jogcon', 'Namco PlayStation pad with a jog dial.', 'Namco', '', GC)]
K['Racing wheel']['x'] += [A('Gran Trak 10 wheel', 'First steering wheel used in a racing arcade game.', 'Atari', '1974', GC),
                           A('Wii Wheel', 'Plastic shell that holds a Wii Remote as a wheel, bundled with Mario Kart Wii.', 'Nintendo', '2008', GC)]
K['Light gun']['x'].insert(0, A('Magnavox Odyssey light gun', 'First home-console light gun.', 'Magnavox', '1972', GC))
K['Dance or balance mat']['x'] += [A('Bandai dance pad', 'Early Famicom dance pad.', 'Bandai', '1986', GC),
                                   A('Foot Craz', 'Exus floor pad for the Atari 2600.', '', '1987', GC)]
K['Standalone VR headset']['x'] += [A('Oculus Go', 'Standalone headset for media and light games.', 'Oculus', '2018', VR),
                                    A('Oculus Quest', 'First standalone headset with room-scale tracking.', 'Oculus', '2019', VR)]
K['Tethered VR headset']['x'] += [A('HTC Vive Pro', 'Higher-resolution Vive.', 'HTC', '2018', VR),
                                  A('PlayStation VR2', 'PS5 headset with eye tracking.', 'Sony', '2023', VR)]
for kn in ('Standalone VR headset', 'Tethered VR headset'):
    pass

# ---- tt for every kind ------------------------------------------------
COMP = ['Loose', 'Complete in box', 'Sealed']
TT = {
 'Home console': [['Game format', ['Cartridge', 'Optical disc', 'Digital-only']], ['Revision', ['Launch model', 'Slim or redesign', 'Special edition']], ['Region', ['NTSC-J', 'NTSC-U', 'PAL']]],
 'FPGA & clone console': [['Implementation', ['FPGA', 'Clone chip', 'Emulation']]],
 'Handheld console': [['Screen', ['Monochrome LCD', 'Colour LCD', 'Dual screen', 'Touchscreen']], ['Game format', ['Cartridge', 'Optical disc', 'Memory card']]],
 'Hybrid console': [['Play mode', ['Docked to a TV', 'Handheld', 'Tabletop']], ['Controllers', ['Detachable', 'Fixed']]],
 'Handheld gaming PC': [['Operating system', ['Windows', 'SteamOS']], ['Input', ['Gamepad only', 'With keyboard']]],
 'Emulation handheld': [['Operating system', ['Linux', 'Android']], ['Shape', ['Clamshell', 'Vertical', 'Horizontal']]],
 'Plug-and-play & mini console': [['Kind of unit', ['Pong-era dedicated', 'TV game joystick', 'Official mini', 'Computer mini']]],
 'LCD handheld game': [['Display', ['Single screen', 'Dual screen', 'Wide screen', 'Panorama', 'Colour']]],
 'Tabletop electronic game': [['Display', ['VFD', 'LCD', 'LED']]],
 'Disk or CD drive add-on': [['Storage medium', ['Floppy or Disk Card', 'CD-ROM', 'Magnetic disk']]],
 'Hardware upgrade add-on': [['Upgrade', ['Memory expansion', 'Faster processor']]],
 'Cartridge converter': [['Purpose', ['Play another system\'s games', 'Bypass a region lock']]],
 'Game cartridge': [['Completeness', COMP], ['Licence', ['Licensed', 'Unlicensed']], ['Print', ['First print', 'Later print']]],
 'Game disc': [['Disc format', ['CD-ROM', 'DVD', 'Blu-ray']], ['Completeness', COMP], ['Print', ['Black-label first print', 'Later print']]],
 'Game card': [['Completeness', COMP]],
 'Cassette or floppy game': [['Medium', ['Cassette tape', 'Floppy disk', 'Quick Disk']]],
 'Game-key or download-code card': [['Card type', ['Game-key card', 'Download-code card']]],
 "Collector's edition": [['Edition', ["Collector's edition", 'Limited edition', 'Steelbook edition']], ['Run', ['Retail', 'Limited physical print run']]],
 'Graded game': [['Item graded', ['Sealed', 'Loose cartridge or disc']]],
 'Reproduction cartridge': [['Sold as', ['Declared reproduction', 'Counterfeit']]],
 'Gamepad': [['Connection', ['Wired', 'Wireless']], ['Form', ['Standard pad', 'Detachable split pair', 'Phone clamp']], ['Extras', ['Rear paddles', 'Adaptive layout']], ['Stick technology', ['Potentiometer', 'Hall effect', 'TMR']]],
 'Arcade stick': [['Parts style', ['Japanese-style', 'American-style']], ['Panel size', ['Compact', 'Full-size']]],
 'Leverless controller': [['Switches', ['Mechanical', 'Optical']]],
 'Racing wheel': [['Drive', ['Gear', 'Belt', 'Direct-drive']], ['Build', ['Console wheel and pedals', 'Toy or motion wheel']]],
 'Racing wheelbase': [['Drive', ['Direct-drive', 'Belt', 'Gear']]],
 'Steering wheel rim': [['Shape', ['Formula', 'GT', 'Round']]],
 'Pedal set': [['Sensor', ['Potentiometer', 'Hall sensor', 'Load cell', 'Hydraulic', 'Active']]],
 'Gear shifter': [['Pattern', ['H-pattern', 'Sequential']]],
 'Handbrake controller': [['Sensor', ['Load cell', 'Hall sensor']]],
 'Sim cockpit or wheel stand': [['Frame', ['Wheel stand', 'Seat cockpit', 'Aluminium-profile rig']], ['Motion', ['Static', 'Motion platform']]],
 'Sim racing seat': [['Seat style', ['GT and touring car', 'Formula', 'Rally']], ['Motion', ['Fixed', 'Force-feedback']]],
 'Flight stick': [['Layout', ['Stick only', 'HOTAS set', 'HOSAS dual-stick set', 'Sidestick']]],
 'Rudder pedals': [['Action', ['Sliding', 'Pendular']], ['Extras', ['Toe brakes', 'Dampers']]],
 'Flight-sim control panel': [['Panel type', ['Switch', 'Radio', 'Autopilot', 'Instrument', 'MFD bezel', 'Button box']]],
 'Light gun': [['Sensing', ['CRT light-sensing', 'Infrared sensor', 'Camera-based']], ['Form', ['Stand-alone gun', 'Shell for a motion controller']]],
 'Motion controller': [['Form', ['Wand', 'Glove', 'Clip-on attachment', 'Fitness accessory']]],
 'Console camera': [['Sensing', ['Colour', 'Depth']]],
 'Paddle or spinner controller': [['Reading', ['Absolute (potentiometer paddle)', 'Relative (spinner or driving dial)']]],
 'Guitar controller': [['Neck', ['Five-fret', 'Six-button', 'Real strings or frets']], ['Instrument', ['Lead', 'Bass']]],
 'Drum kit controller': [['Pads', ['Four-pad', 'Five-pad']], ['Cymbals', ['With cymbal add-on', 'Without']]],
 'Dance or balance mat': [['Form', ['Dance pad', 'Balance board']], ['Surface', ['Soft pad', 'Hard metal pad', 'Arcade stage']]],
 'Game microphone': [['Connection', ['Wired USB', 'Wireless']]],
 'Case, screen protector or skin': [['Protects', ['Whole console', 'Screen', 'Body surface']], ['Material', ['Hard shell', 'Fabric or neoprene', 'Tempered glass', 'Plastic film', 'Vinyl']]],
 'Power, charging & dock': [['Function', ['Replacement battery', 'Mains adapter', 'Charging stand', 'TV dock']]],
 'Console stand, mount or cooler': [['Function', ['Vertical stand', 'Horizontal stand', 'Wall mount', 'Cooling stand', 'Clip-on fan']]],
 'Console cable or adapter': [['Video signal', ['RF', 'Composite', 'S-Video', 'RGB SCART', 'Component', 'VGA', 'HDMI']], ['Other connection', ['Link cable', 'Controller converter', 'Modem or network adapter']]],
 'Rumble pack': [['Contents', ['Rumble only', 'Rumble and memory combined']]],
 'Console keyboard or media add-on': [['Function', ['Full keyboard', 'Controller clip-on chatpad', 'Media remote', 'TV tuner']]],
 'Optical drive emulator': [['Storage', ['SD card', 'USB', 'SATA drive']]],
 'Modchip': [['Purpose', ['Region and copy-protection chip', 'Drive-emulating chip', 'Voltage-glitch chip']]],
 'Video scaler or upscaler': [['Method', ['Line doubler', 'Line multiplier', 'Full scaler']]],
 'Internal HDMI mod kit': [['Install', ['Internal board', 'Digital-port adapter']]],
 'Screen upgrade kit': [['Panel', ['IPS', 'Laminated IPS']]],
 'Replacement shell': [['Fit', ['Standard', 'IPS-ready']], ['Finish', ['Clear', 'Coloured']]],
 'Replacement part': [['Part', ['Battery', 'Joystick module', 'Cooling fan', 'Screen', 'Game-card reader', 'Buttons and trim', 'Fix kit']]],
 'Repair toolkit': [['Contents', ['Screwdriver set', 'Security bits', 'Pry tools']]],
 'Standalone VR headset': [['Display', ['VR only', 'Colour-passthrough mixed reality']]],
 'Tethered VR headset': [['Tracking', ['Outside-in (base stations or camera)', 'Inside-out']], ['Eye tracking', ['With', 'Without']]],
 'Phone VR viewer': [['Material', ['Cardboard', 'Plastic', 'Fabric']]],
 'XR glasses': [['Anchoring', ['Display only', '3DoF screen anchoring']], ['Lenses', ['Fixed tint', 'Electrochromic dimming']]],
 'VR controller': [['Tracking', ['Ring-tracked', 'Self-tracked']]],
 'VR tracker or base station': [['Tracks', ['The room (base station)', 'The body', 'The face']]],
 'VR head strap or facial interface': [['Part', ['Rigid strap', 'Battery strap', 'Audio strap', 'Facial interface', 'Silicone cover']]],
 'Haptic vest or glove': [['Worn on', ['Torso', 'Hand and arm', 'Face']]],
 'Upright arcade cabinet': [['Build', ['Dedicated', 'Conversion', 'Deluxe or themed']]],
 'Candy (sit-down) arcade cabinet': [['Format', ['Single', 'Versus (back-to-back) pair', 'Large-screen theatre']], ['Display', ['CRT', 'Widescreen LCD']]],
 'Cocktail table arcade cabinet': [['Seating', ['Face-to-face', 'Side-by-side']]],
 'Cockpit arcade cabinet': [['Enclosure', ['Enclosed', 'Open sit-in']]],
 'Home replica arcade cabinet': [['Scale', ['3/4 scale', 'Full size']], ['Layout', ['Upright', 'Sit-down driving', 'Head-to-head table']]],
 'Arcade system board': [['Board type', ['Dedicated board', 'Cartridge or cassette system', 'Disc or PC-based system', 'Multi-game (bootleg) board']]],
 'Supergun': [['Video output', ['SCART RGB', 'Composite or S-video', 'Component or VGA']]],
 'Arcade lever and buttons': [['Lever', ['Ball-top', 'Bat-top']], ['Button', ['Snap-in', 'Screw-in']], ['Gate', ['4-way', '8-way']]],
 'Arcade monitor': [['Display', ['15 kHz CRT', 'Multi-sync CRT', 'LCD']]],
 'Solid-state pinball machine': [['Display', ['Alphanumeric', 'Dot-matrix (DMD)', 'LCD']], ['Body', ['Standard', 'Widebody']]],
 'Electromechanical pinball machine': [['Backbox', ['Wedgehead', 'Standard backbox']], ['Players', ['Single-player', 'Multi-player']], ['Scoring rule', ['Add-a-ball', 'Replay']]],
 'Modern pinball machine': [['Display', ['Dot-matrix (DMD)', 'LCD']]],
 'Digital pinball cabinet': [['Build', ['Ready-made cabinet', 'Home-built']], ['Size', ['3/4 scale', 'Full size']]],
 'Pinball mod or topper': [['Part', ['Topper', 'Shaker motor', 'LED lighting kit', 'Colour display', 'Playfield toy', 'Side blade', 'Shooter rod or knob', 'Playfield protector']]],
 'Electromechanical arcade game': [['Theme', ['Shooting', 'Driving', 'Submarine or periscope', 'Sports']]],
}
for n, tt in TT.items():
    k = K[n]; k.pop('t', None); k['tt'] = tt
for k in K.values():
    k.pop('t', None)

# ---- see links --------------------------------------------------------
SEE = {
 'Trackball controller': [['D1', 'Trackball', 'the desktop pointing device']],
 'Game cartridge': [['I1', 'Game emulator', 'plays the same games from files']],
 'Emulation handheld': [['I1', 'Game emulator', 'the software that runs on it']],
 'Video scaler or upscaler': [['D1', 'Video capture device', 'capture cards take the same signals']],
 'Plug-and-play & mini console': [['D1', 'Retro computer re-creation', 'computer mini versions sit there']],
 'Cassette or floppy game': [['D1', 'Home computer', 'the machine that reads them']],
 'Console camera': [['D1', 'Video capture device', 'a camera is not a capture card']],
 'Standalone VR headset': [['E5', 'XR glasses', 'glasses show a screen but do not fill the view']],
 'Early VR head-mounted display': [['E5', 'Standalone VR headset', 'modern successors']],
 'Flash cartridge': [['E5', 'Reproduction cartridge', 'both carry games not made by the publisher']],
 'Reproduction cartridge': [['E5', 'Game cartridge', 'the original it copies']],
 'Slot machine': [['E1', 'Roulette wheel', 'gambling equipment for home use']],
 'Pinball mod or topper': [['E5', 'Modern pinball machine', 'the machine it fits']],
 'Motion simulator arcade cabinet': [['E5', 'Cockpit arcade cabinet', 'same seated play without motion']],
 'Dance or balance mat': [['E5', 'Hand percussion controller', 'other body-played rhythm controllers']],
 'Racing wheel': [['E5', 'Racing wheelbase', 'a base sold apart from the rim']],
 'Arcade stick': [['E5', 'Arcade lever and buttons', 'the parts inside a stick']],
 'Arcade lever and buttons': [['E5', 'Arcade stick', 'the finished controller']],
 'Hybrid console': [['E5', 'Handheld console', 'handheld only']],
 'Game disc': [['E5', 'Budget re-release', 'reprints under a budget label']],
}
for n, sv in SEE.items():
    K[n]['see'] = sv

# ---- structure --------------------------------------------------------
def shelf(n, t, ax, kinds):
    s = {'n': n, 't': t}
    if ax: s['ax'] = ax
    s['k'] = [K[x] for x in kinds]
    return s

oldb = {dp['n']: dp for dp in d['depts']}
def dept(name, t, ax, shelves):
    o = oldb[name]
    nd = {'n': name, 'mode': o['mode'], 't': t, 'ax': ax}
    if o.get('note'): nd['note'] = o['note']
    if o.get('b'): nd['b'] = o['b']
    nd['s'] = shelves
    return nd

D = []
D.append(dept('Consoles & handhelds',
 'Machines that play video games on a screen: TV consoles, handhelds, hybrids, built-in game units and the add-ons that extend them; a game disc or cartridge → Game media; a pad → Controllers; a gaming PC → Computers.',
 'How is the machine played: on a TV from swappable games, in the hand, from games built into the unit, or as an add-on to another system?',
 [shelf('Home consoles', 'Machines that connect to a TV and run swappable games, including set-top microconsoles and modern rebuilds of old systems; a handheld → Handhelds & hybrids.',
        'kinds by how the machine is built: original hardware, set-top microconsole, clone or FPGA rebuild',
        ['Home console', 'Microconsole', 'FPGA & clone console']),
  shelf('Handhelds & hybrids', 'Machines with their own screen and controls that run swappable games; a unit with its games built in → Built-in game units.',
        'kinds by what runs the games: a platform library, a TV dock as well, a PC operating system, or emulators',
        ['Handheld console', 'Hybrid console', 'Handheld gaming PC', 'Emulation handheld']),
  shelf('Built-in game units', 'Units whose games are fixed inside, such as plug-and-play sticks, mini revivals, Game & Watch and tabletop LCD games; a console that loads cartridges → Home consoles.',
        'kinds by where the built-in games are shown: on a TV, on a hand-held LCD, on a tabletop display',
        ['Plug-and-play & mini console', 'LCD handheld game', 'Tabletop electronic game']),
  shelf('Console add-ons & converters', 'Hardware that plugs into a console to change what it can read or do, such as disk drives, 32X-style upgrades and cartridge converters; a flash cartridge → Modding.',
        'kinds by what the add-on changes: the storage it reads, the power it adds, or the games it accepts',
        ['Disk or CD drive add-on', 'Hardware upgrade add-on', 'Cartridge converter'])]))
D.append(dept('Game media',
 'The discs, cartridges and cards that hold a game, with the editions, reprints, grades and copies that collectors tell apart; the game title → Interactive Entertainment taxonomy; a flash cartridge → Modding.',
 'Is it the carrier that holds the software, the edition or reprint it was sold as, or its condition and authenticity?',
 [shelf('Carriers', 'The physical object that holds a game: cartridge, disc, card or tape.',
        'kinds by physical carrier: cartridge, optical disc, solid-state card, tape or floppy, key card',
        ['Game cartridge', 'Game disc', 'Game card', 'Cassette or floppy game', 'Game-key or download-code card']),
  shelf('Editions & reprints', 'Versions of a game sold in special or cheaper form, such as collector\'s, limited and budget reprints; the carrier itself → Carriers.',
        'kinds by how the edition differs from the standard release: dearer and scarcer, or cheaper and later',
        ["Collector's edition", 'Budget re-release']),
  shelf('Condition & authenticity', 'Third-party grading of a game and the question of whether a cartridge is original; a flash cartridge → Modding.',
        None, ['Graded game', 'Reproduction cartridge'])]))
D.append(dept('Controllers',
 'Things the player holds, steps on, sings into or sits at to drive a game; a VR controller → VR & XR; an arcade lever or button sold as a part → Arcade & coin-op.',
 'What does the player do with it: press and steer, aim or move, drive, fly, or play along to music?',
 [shelf('Pads & sticks', 'Hand-held controllers for the directions and buttons of ordinary games: pads, joysticks, arcade sticks and leverless boxes.',
        'kinds by how direction is input: thumbsticks and d-pad, a single joystick, an arcade lever, buttons only',
        ['Gamepad', 'Joystick', 'Arcade stick', 'Leverless controller']),
  shelf('Pointing & motion', 'Controllers that aim at the screen or read the body: light guns, motion wands, cameras, mice, paddles, spinners and trackballs.',
        'kinds by what is read: the aim of a gun, the movement of a wand or body, a camera view, a dial or ball',
        ['Light gun', 'Motion controller', 'Console camera', 'Console mouse', 'Paddle or spinner controller', 'Trackball controller']),
  shelf('Driving (sim racing)', 'The wheel, pedals and frame of a driving rig; a toy wheel clipped to a pad is a wheel here too.',
        'kinds by part of the rig: complete wheel, base, rim, pedals, shifter, handbrake, frame, seat',
        ['Racing wheel', 'Racing wheelbase', 'Steering wheel rim', 'Pedal set', 'Gear shifter', 'Handbrake controller', 'Sim cockpit or wheel stand', 'Sim racing seat']),
  shelf('Flying (flight sim)', 'The stick, yoke, throttle, pedals and panels of a flight rig.',
        'kinds by control: stick, yoke, throttle, rudder pedals, switch panels',
        ['Flight stick', 'Flight yoke', 'Flight throttle', 'Rudder pedals', 'Flight-sim control panel']),
  shelf('Music, dance & party', 'Controllers shaped like instruments, mats, microphones and buzzers for rhythm, dance, singing and quiz games.',
        'kinds by what the player plays or does: guitar, drums, deck, hand percussion, keys, voice, feet, a buzzer',
        ['Guitar controller', 'Drum kit controller', 'DJ turntable controller', 'Hand percussion controller', 'Keyboard, baton & button-pad controller', 'Game microphone', 'Dance or balance mat', 'Quiz buzzer'])]))
D.append(dept('Accessories',
 'Extras that protect, power, hold, connect or add a function to a console without changing how its games run; a mod that changes what plays → Modding, repair & retro video.',
 'What does it do for the console: protect it, power and hold it, connect and store, or add a function?',
 [shelf('Protection', 'Cases, screen protectors and skins that guard the console body and screen.', None, ['Case, screen protector or skin']),
  shelf('Power & stands', 'Chargers, docks, stands, mounts and coolers that keep a console running and in place.', None, ['Power, charging & dock', 'Console stand, mount or cooler']),
  shelf('Cables & memory', 'Leads, memory cards and multitaps that connect a console to a screen, a save or more players.', 'kinds by what is connected: a screen, a save, more pads',
        ['Console cable or adapter', 'Console memory card', 'Multitap']),
  shelf('Function add-ons', 'Extras that give a console a new function, such as force feedback, toy portals and keyboards.',
        'kinds by the function added: feel, toy figures, typing and media',
        ['Rumble pack', 'Toys-to-Life portal', 'Console keyboard or media add-on'])]))
D.append(dept('Modding, repair & retro video',
 'Parts, kits and tools owners fit to run other media, sharpen the picture or restore a console; a plain case or cable → Accessories.',
 'What does it change on the original machine: what it can load, what picture it shows, or its worn body and parts?',
 [shelf('Loading & unlocking', 'Devices that make a console load other media or run unlocked, from flash cartridges to cheat cartridges.',
        'kinds by what they load: cartridge games, disc games, unlocked or altered code',
        ['Flash cartridge', 'Optical drive emulator', 'Modchip', 'Cheat device']),
  shelf('Picture upgrades', 'Boards and boxes that give an old console a clean picture on a modern screen.',
        'kinds by where the picture is improved: inside the console as HDMI or RGB, or outside as a scaler',
        ['Internal HDMI mod kit', 'RGB mod board', 'Video scaler or upscaler', 'Screen upgrade kit']),
  shelf('Repair & restoration', 'Shells, parts and tools for fixing or refreshing a console or handheld.',
        None, ['Replacement shell', 'Replacement part', 'Repair toolkit'])]))
D.append(dept('VR & XR',
 'Headsets that fill the view with a virtual world and the add-ons that track, hold, fit or let you feel them; smart glasses worn as eyewear → Smart glasses.',
 'Is it the headset that shows the world, or something added to track, hold, fit or feel it?',
 [shelf('VR headsets', 'Headsets and viewers that show a virtual or mixed world.',
        'kinds by where the computing is: in a phone, in the headset, in a PC or console, or in a pair of glasses',
        ['Early VR head-mounted display', 'Phone VR viewer', 'Standalone VR headset', 'Tethered VR headset', 'XR glasses']),
  shelf('VR accessories', 'Add-ons for a headset.',
        'kinds by what they add: input, tracking, fit, feeling, movement',
        ['VR controller', 'VR tracker or base station', 'VR head strap or facial interface', 'Haptic vest or glove', 'VR treadmill'])]))
D.append(dept('Arcade & coin-op',
 'Coin-operated video cabinets, boards, pinball and prize machines owned by collectors, with home replicas; a pad or stick for the home → Controllers.',
 'What is it: a video cabinet, the electronics and controls inside one, a pinball machine, or a mechanical or prize game?',
 [shelf('Video arcade cabinets', 'Cabinets built around a video screen, from upright to cockpit and motion rides, with home replicas.',
        'kinds by cabinet shape: upright, cabaret, cocktail, bar-top, sit-down, deluxe, cockpit, motion, home copy',
        ['Upright arcade cabinet', 'Cabaret arcade cabinet', 'Cocktail table arcade cabinet', 'Bar-top arcade cabinet', 'Candy (sit-down) arcade cabinet', 'Deluxe vehicle-style arcade cabinet', 'Cockpit arcade cabinet', 'Motion simulator arcade cabinet', 'Home replica arcade cabinet']),
  shelf('Arcade boards & parts', 'The circuit boards, harnesses, levers and monitors inside a video cabinet.',
        'kinds by part: board, board-to-TV harness, controls, screen',
        ['Arcade system board', 'Supergun', 'Arcade lever and buttons', 'Arcade monitor']),
  shelf('Pinball machines', 'Flipper machines for a ball on a playfield, by scoring technology.',
        'kinds by technology era: relays and reels, solid-state, modern screens, home digital',
        ['Electromechanical pinball machine', 'Solid-state pinball machine', 'Modern pinball machine', 'Digital pinball cabinet']),
  shelf('Pinball mods', 'Add-ons fitted to a pinball machine to light, shake or protect it.', None, ['Pinball mod or topper']),
  shelf('Mechanical & prize games', 'Coin-operated games with no video screen: cranes, redemption, slot and electromechanical shooters.',
        'kinds by payout: a prize, tickets, cash, or only a score',
        ['Claw crane & redemption game', 'Slot machine', 'Electromechanical arcade game'])]))

placed = [k['n'] for dp in D for s in dp['s'] for k in s['k']]
assert len(placed) == len(set(placed)), [n for n in placed if placed.count(n) > 1]
missing = set(K) - set(placed)
assert not missing, missing

d['depts'] = D
d['lead'] = 'Video-game hardware a person owns, organised by what the object does for play: consoles and handhelds, game media, controllers, accessories, modding and repair, VR & XR, and arcade and pinball machines; game titles live in the Interactive Entertainment taxonomy.'
d['ax'] = 'What does the object do for video games: run the game, hold it, control it, protect or power the machine, alter it, put the player inside it, or stand in an arcade?'
d['key'] = [
 '1. Is it a machine that plays games on a TV, in the hand or from built-in games, or an add-on that changes what a console can read? → Consoles & handhelds',
 '2. Is it the disc, cartridge or card that holds a game, or an edition, reprint, grade or copy of one? → Game media',
 '3. Does the player drive the game through it with hands, feet or voice (pad, stick, wheel, gun, instrument)? → Controllers',
 '4. Does it protect, power, hold or connect a console without changing what plays on it? → Accessories',
 '5. Is it a part, kit or tool to load other media, sharpen the picture or repair a console? → Modding, repair & retro video',
 '6. Is it worn on the head to show a virtual world, or an add-on for such a headset? → VR & XR',
 '7. Is it a coin-operated cabinet, board, pinball machine or prize game? → Arcade & coin-op',
 '<i>Precedence: a flash cartridge is modding (step 5) before media (step 2); a VR controller stays with VR (step 6) before controllers (step 3); an arcade stick is a controller (step 3), while a bare arcade lever is an arcade part (step 7).</i>']

tmp = R + 'out/E5.json.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, R + 'out/E5.json')
# renames
rf = R + 'out/E5_renames.json'
old = json.load(open(rf)) if os.path.exists(rf) else {}
old.update(renames)
json.dump(old, open(rf, 'w'), ensure_ascii=False, indent=1)
print('demoted', demoted)
