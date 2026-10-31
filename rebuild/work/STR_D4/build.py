import json, copy, os, shutil, sys
R = '/home/user/Possession-Taxonomy/rebuild/'
W = R + 'work/STR_D4/'
SRC = R + 'out/D4.json'
BAK = W + 'bak/'
os.makedirs(BAK, exist_ok=True)
if not os.path.exists(BAK + 'D4.json'):
    shutil.copy(SRC, BAK + 'D4.json')
    shutil.copy(R + 'out/D4_brands.json', BAK + 'D4_brands.json')
    shutil.copy(R + 'out/D4_moves.json', BAK + 'D4_moves.json')
d = json.load(open(BAK + 'D4.json'))   # always rebuild from the backup of the pre-pass file

old = {}
for D in d['depts']:
    for S in D['s']:
        for K in S['k']:
            old[K['n']] = K

WIKI = 'https://en.wikipedia.org/wiki/'
used = set()


def models(src, names):
    out = []
    for nm in names:
        hit = [m for m in old[src].get('m', []) if m[0] == nm]
        assert hit, (src, nm)
        out.append(copy.deepcopy(hit[0]))
    return out


def arch(src, names):
    out = []
    for nm in names:
        hit = [a for a in old[src].get('x', []) if a['n'] == nm]
        assert hit, (src, nm)
        out.append(copy.deepcopy(hit[0]))
    return out


def K(n, src=None, a=None, d_=None, tt=None, x='all', m='all', r='all', see=None, s=None):
    """Kind built from an old kind (src defaults to n) with overrides."""
    src = src or n
    o = copy.deepcopy(old[src])
    k = {'n': n, 'a': a if a is not None else o.get('a', ''), 'd': d_ or o['d']}
    if src == n or True:
        used.add(src)
    k['s'] = s or o.get('s', '')
    if tt:
        k['tt'] = tt
    if x == 'all':
        x = o.get('x', [])
    if x:
        k['x'] = x
    if m == 'all':
        m = o.get('m', [])
    if m:
        k['m'] = m
    if r == 'all':
        r = o.get('r', [])
    if r:
        k['r'] = r
    if see:
        k['see'] = see
    return k


def N(n, a, d_, tt, s, x=None, m=None, r=None, see=None):
    k = {'n': n, 'a': a, 'd': d_, 's': s, 'tt': tt}
    if x:
        k['x'] = x
    if m:
        k['m'] = m
    if r:
        k['r'] = r
    if see:
        k['see'] = see
    return k


def X(n, d_, mk, y, s, v=None, dt='', a=''):
    o = {'n': n, 'a': a, 'd': d_, 'mk': mk, 'y': y, 's': s}
    if v:
        o['v'] = v
    if dt:
        o['dt'] = dt
    return o


def V(n, mk='', y='', d_=''):
    return {'n': n, 'mk': mk, 'y': y, 'd': d_}


def SH(n, t, ax, ks):
    sh = {'n': n, 't': t}
    if ax:
        sh['ax'] = ax
    sh['k'] = ks
    return sh


def DP(n, mode, note, t, ax, shelves, b=None):
    return {'n': n, 'mode': mode, 'note': note, 'b': b if b is not None else [], 't': t, 'ax': ax, 's': shelves}

# ---------------------------------------------------------------- DIGITAL
# dedupe PowerShot G: premium keeps it; carry compact's extra versions
prem_g = [a for a in old['Premium fixed-lens camera']['x'] if a['n'] == 'Canon PowerShot G'][0]
cmp_g = [a for a in old['Compact camera']['x'] if a['n'] == 'Canon PowerShot G'][0]
have = {v['n'] for v in prem_g.get('v', [])}
for v in cmp_g.get('v', []):
    if v['n'] not in have:
        prem_g.setdefault('v', []).append(v)
        have.add(v['n'])

mirrorless = K('Mirrorless camera', d_=old['Mirrorless camera']['d'], tt=[
    ['Sensor size', ['Full frame', 'APS-C', 'Micro Four Thirds', 'Medium format']],
    ['Body style', ['Rangefinder-style', 'SLR-style', 'Box-style video body']]],
    see=[['E6', 'Astronomy camera', 'cooled astronomy cameras are made for telescopes']])
dslr = K('DSLR camera', tt=[
    ['Sensor size', ['Full frame', 'APS-C', 'APS-H', 'Four Thirds']],
    ['Mirror design', ['Moving mirror and prism', 'Fixed semi-transparent mirror (SLT)']]])
drf = K('Digital rangefinder camera', tt=[
    ['Sensor size', ['APS-H', 'APS-C', 'Full frame']],
    ['Sensor type', ['Colour', 'Monochrome']]],
    see=[['D4', 'Film rangefinder camera', 'the film bodies these digital rangefinders follow']])
dback = K('Digital back', tt=[
    ['Sensor type', ['Colour', 'Monochrome']],
    ['Capture', ['Single-shot', 'Multi-shot']]],
    see=[['D4', 'Medium-format SLR camera', 'the film bodies a back replaces the film in']])
prem = K('Premium fixed-lens camera', tt=[
    ['Sensor size', ['1-inch', 'Micro Four Thirds', 'APS-C', 'Full frame']],
    ['Lens', ['Fixed prime', 'Fixed zoom']],
    ['Sensor type', ['Colour', 'Monochrome']]])
comp = K('Compact camera', x=[a for a in old['Compact camera']['x'] if a['n'] != 'Canon PowerShot G'],
         d_='Small digital stills camera with a non-removable lens and mostly automatic operation, built for pocket or carry use; a phone camera is not listed.',
         tt=[['Intended use', ['Point-and-shoot', 'Travel zoom', 'Vlogging']],
             ['Lens', ['Short zoom', 'Long travel zoom']]])
rugged = N('Rugged compact camera', 'tough camera · waterproof compact · underwater compact',
           'Compact camera built to resist water, cold, heat, shock or pressure, for beaches, snow, diving and hiking.',
           [['Built to resist', ['Water', 'Cold', 'Heat', 'Shock', 'Pressure']]],
           WIKI + 'Digital_camera',
           see=[['D4', 'Underwater housing', 'a housing waterproofs a camera that is not built for it']])
bridge = K('Bridge camera', tt=[['Sensor size', ['1-inch', 'Small (1/2.3-inch)']],
                                ['Zoom aperture', ['Constant aperture', 'Variable aperture']]])
camcorder = K('Camcorder', tt=[
    ['Recording medium', ['Tape (Video8, Hi8, MiniDV)', 'DVD', 'Hard disk', 'Memory card']],
    ['Resolution', ['Standard definition', 'Full HD', '4K']]],
    see=[['F1', 'Camcorder cassette', 'the tape a vintage camcorder records on']])
action = K('Action camera', tt=[['Build', ['Waterproof body', 'Modular body']],
                                 ['Price tier', ['Entry-level', 'Flagship']]])
cam360 = K('360-degree camera', tt=[['Lenses', ['Two back-to-back lenses', 'Multi-lens rig']],
                                     ['Sensor size', ['Small sensor', '1-inch']]])
pocket = N('Pocket gimbal camera', 'handheld gimbal camera · stabilised pocket camera',
           'Pocket-sized camera built into a three-axis gimbal on a handle, for smooth handheld video.',
           [['Sensor size', ['Small sensor', '1-inch']], ['Axes', ['Three-axis']]],
           'https://www.photographyblog.com/news/dji_osmo_pocket',
           x=[X('DJI Osmo Pocket', 'Three-axis stabilised 4K camera on a handle, announced as the world\'s smallest of its kind.',
                'DJI', '2018', 'https://www.photographyblog.com/news/dji_osmo_pocket',
                v=[V('Osmo Pocket 2', 'DJI', '', 'from old data'), V('Osmo Pocket 3', 'DJI', '', 'from old data'),
                   V('Pocket 4', 'DJI', '', 'from old data')])],
           see=[['D4', 'Gimbal stabiliser', 'a gimbal that carries a separate camera']])
drone = K('Camera drone', tt=[['Weight class', ['Sub-250 g', 'Over 250 g']],
                              ['Frame', ['Folding', 'Fixed']],
                              ['Flight style', ['Stabilised camera flight', 'First-person view (FPV)']]])
trail = K('Trail camera', tt=[['Data', ['Cellular', 'SD card only']],
                              ['Power', ['Battery', 'Solar panel']],
                              ['Night flash', ['No-glow infrared', 'Low-glow infrared']]],
          see=[['E2', 'Trail camera', 'the same object sold for hunting'],
               ['B8', 'Security camera', 'a fixed camera for watching property']])

dep_digital = DP('Digital cameras', 'mixed',
    'Variety at the enthusiast end (camera-wiki axis maker → system/mount → model → generation); tier for everyday video and compact kit.',
    'Cameras that record to a memory card, from interchangeable-lens bodies and compacts to camcorders, action, 360, drone and trail cameras; a phone → D2, a webcam → D1.',
    'Is the lens changed on the body, fixed on a still camera, or is the camera built for video, rough use or remote placement?',
    [SH('Interchangeable-lens cameras',
        'Digital bodies that take different lenses: mirrorless, DSLR and digital rangefinder cameras, and sensor backs for medium-format bodies; a camera with a fixed lens → Fixed-lens still cameras.',
        'kinds by how the picture is framed and focused: electronic finder, mirror and prism, rangefinder window, or a sensor back on a studio body',
        [mirrorless, dslr, drf, dback]),
     SH('Fixed-lens still cameras',
        'Digital stills cameras with a lens that cannot be removed, from large-sensor premium compacts to pocket, rugged and long-zoom bridge cameras; a body with changeable lenses → Interchangeable-lens cameras.',
        'kinds by sensor size and lens reach: large sensor with a prime or short zoom, pocket compact, rugged compact, superzoom bridge',
        [prem, comp, rugged, bridge]),
     SH('Video, action & remote cameras',
        'Cameras made mainly for moving pictures or unattended use: camcorders, action, 360-degree and pocket gimbal cameras, drones and trail cameras; a stills compact that also films → Fixed-lens still cameras.',
        'kinds by how the camera is carried or placed: held for long takes, mounted on the body, spherical, on a gimbal, flown, or left outdoors',
        [camcorder, action, cam360, pocket, drone, trail])])

# ---------------------------------------------------------------- FILM CAMERAS
fslr = K('Film SLR camera', tt=[['Exposure and focus', ['Manual mechanical', 'Electronic auto-exposure', 'Autofocus']],
                                 ['Viewfinder', ['Waist-level', 'Eye-level pentaprism']],
                                 ['Shutter', ['Focal-plane', 'Leaf shutter']]])
frf = K('Film rangefinder camera', tt=[['Lens', ['Interchangeable', 'Fixed']],
                                        ['Lens mount', ['Screw mount (M39)', 'Bayonet']],
                                        ['Body', ['Rigid', 'Folding']]],
        see=[['D4', 'Digital rangefinder camera', 'digital bodies in the same mount tradition']])
f35c = K('35 mm compact film camera', tt=[['Focus', ['Autofocus', 'Zone or scale focus', 'Fixed focus']],
                                           ['Lens', ['Fixed prime', 'Zoom']],
                                           ['Body material', ['Plastic', 'Metal', 'Titanium']]])
half = K('Half-frame camera', tt=[['Body type', ['Compact', 'SLR']],
                                   ['Exposure', ['Fixed exposure', 'Auto-exposure']]])
minox = N('Subminiature camera', 'spy camera · Minox camera · miniature camera',
          'Tiny camera for very small film, such as the Minox with its 8×11 mm frames on 9.2 mm film.',
          [['Film', ['9.2 mm Minox film', '16 mm cassette film']], ['Viewing', ['Folding viewfinder', 'Reflex']]],
          WIKI + 'Minox',
          x=[X('Minox', 'Spy-style subminiature camera invented by Walter Zapp, with 8×11 mm frames on 9.2 mm film.',
               'Minox', '1936', WIKI + 'Minox',
               v=[V('Minox Riga', 'Minox', '1938', 'made by VEF in Riga, to 1943'),
                  V('Minox IIIs', 'Minox', '1954', 'added flash sync'),
                  V('Minox B', 'Minox', '1958', 'built-in selenium meter; the most widely produced'),
                  V('Minox LX', 'Minox', '1978', 'electronic, redesigned controls'),
                  V('Minox EC', 'Minox', '1981', 'economical electronic model, the smallest Minox')])],
          see=[['D4', 'Single-use camera', 'another cheap, tiny-format camera']])
cart = N('Cartridge-film camera', 'Instamatic camera · 110 camera · 126 camera · APS camera · disc camera',
         'Easy-load camera that takes a drop-in film cartridge: 126, 110, APS or disc film.',
         [['Film cartridge', ['126', '110', 'APS', 'Disc']], ['Body', ['Fixed-focus box', 'Compact', 'SLR']]],
         WIKI + 'Instamatic',
         x=[X('Kodak Instamatic', 'Kodak\'s line of easy-load point-and-shoot cameras for 126 cartridges, later 110.',
              'Kodak', '1963', WIKI + 'Instamatic',
              v=[V('Instamatic 50', 'Kodak', '1963', 'first model, UK'),
                 V('Instamatic 100', 'Kodak', '', 'first US model, built-in flashgun'),
                 V('Instamatic Reflex', 'Kodak', '1969', 'SLR, top of the line'),
                 V('Pocket Instamatic 60', 'Kodak', '1972', 'top 110 model'),
                 V('Instamatic X-15F', 'Kodak', '', 'last Instamatic sold in the US, to 1988')]),
            X('Kodak Disc camera', 'Camera for 10×8 mm frames on a flat film disc; fifteen exposures per disc.',
              'Kodak', '1982', WIKI + 'Disc_camera',
              v=[V('Minolta Disc-7', 'Minolta', '1983', 'convex selfie mirror')])])

mfslr = K('Medium-format SLR camera', tt=[['Frame size', ['6×4.5 cm (645)', '6×6 cm', '6×7 cm']],
                                           ['Shutter', ['Leaf shutter in the lens', 'Focal-plane shutter']]],
          see=[['D4', 'Digital back', 'a digital back replaces the film back']])
mfrf = K('Medium-format rangefinder camera', tt=[['Frame size', ['6×4.5 cm (645)', '6×6 cm', '6×7 cm', '6×9 cm']],
                                                   ['Lens', ['Fixed', 'Interchangeable']],
                                                   ['Body', ['Folding', 'Rigid']]])
tlr = K('Twin-lens reflex camera', tt=[['Film', ['120 (6×6 cm)', '127 (4×4 cm)']],
                                        ['Lens', ['Fixed', 'Interchangeable']]])
box = K('Box camera', src='Box or folding camera', a='box film camera · Brownie-type camera',
        d_='Simple box-shaped roll-film camera with a fixed single lens and few or no controls.',
        tt=[['Film', ['120', '620', '127']], ['Lens', ['Single meniscus lens', 'Focusing lens']]],
        x=arch('Box or folding camera', ['Kodak Brownie', 'Zeiss Ikon Box-Tengor']),
        m=models('Box or folding camera', ['Panda']), r=[])
fold = K('Folding camera', src='Box or folding camera', a='folder · folding roll-film camera · bellows camera',
         d_='Roll-film or 35 mm camera whose lens and bellows fold into a flat body.',
         tt=[['Film', ['120', '620', '127', '35 mm']], ['Focusing', ['Scale focus', 'Coupled rangefinder']]],
         x=arch('Box or folding camera', ['Zeiss Ikon Ikonta', 'Zeiss Ikon Nettar', 'Kodak Retina (folding)', 'Voigtländer Bessa']),
         m=models('Box or folding camera', ['Midget model 22', 'Pocket Kodak', 'Model 203']), r=[])
view = K('View camera', d_='Large-format camera with bellows, ground-glass focusing and lens movements, for sheet film; monorail, field and technical types.',
         tt=[['Film size', ['4×5 in', '5×7 in', '8×10 in', 'Larger']],
             ['Body', ['Monorail (studio)', 'Field (folding flatbed)', 'Technical (hand-holdable)']]],
         x=[a for a in old['View camera']['x'] if a['n'] != 'Graflex Speed Graphic'])
press = N('Press camera', 'Speed Graphic type · press-type camera',
          'Folding sheet-film camera with a rangefinder and focal-plane shutter, made for news photographers; 4×5 in was the main size.',
          [['Focusing', ['Ground glass', 'Coupled rangefinder']], ['Shutter', ['Focal-plane', 'Lens shutter']]],
          WIKI + 'Large-format_camera',
          x=arch('View camera', ['Graflex Speed Graphic']))
pano = K('Panoramic film camera', tt=[['Mechanism', ['Swing lens', 'Full rotation', 'Fixed wide lens']],
                                       ['Film', ['35 mm', '120 roll film']]])
integral = K('Integral instant camera', tt=[
    ['Film format', ['SX-70', '600', 'Spectra', 'i-Type', 'Instax Mini', 'Instax Wide', 'Instax Square']],
    ['Body', ['Folding SLR', 'Box camera']],
    ['Focus', ['Sonar autofocus', 'Fixed focus']]],
    see=[['F2', 'Instant print', 'the print the camera makes'],
         ['D4', 'Integral instant film', 'the film these cameras load']])
peel = K('Peel-apart instant camera', tt=[['Film', ['Roll film', 'Pack film']],
                                           ['Body', ['Folding', 'Rigid']],
                                           ['Focusing', ['Coupled rangefinder', 'Scale focus']]],
         see=[['D4', 'Peel-apart instant film', 'the pack film these cameras load']])
hybrid = K('Hybrid instant camera', tt=[['Film format', ['Instax Mini', 'Instax Square', 'Instax Wide']]],
           see=[['D4', 'Integral instant camera', 'the all-film version of the same prints']])
toy = K('Toy camera', tt=[['Film', ['120', '35 mm']], ['Lens', ['Plastic', 'Glass']], ['Frame', ['Square', 'Panoramic']]])
single = K('Single-use camera', tt=[['Film', ['Colour 35 mm', 'Black-and-white 35 mm', '110 or APS']],
                                     ['Flash', ['With flash', 'Without flash']],
                                     ['Housing', ['Standard', 'Waterproof']]])
pinhole = K('Pinhole camera', tt=[['Film', ['35 mm', '120', '4×5 in sheet film or paper']],
                                   ['Body material', ['Wood', 'Plastic', 'Metal']]])
s8 = K('Super 8 camera', src='Cine film camera', a='Super 8 cine camera · Super 8 movie camera',
       d_='Hand-held movie camera for Super 8 cartridges, mostly battery-driven with automatic exposure.',
       tt=[['Sound', ['Silent', 'Sound']], ['Lens', ['Fixed', 'Zoom']]],
       x=arch('Cine film camera', ['Beaulieu 4008', 'Canon 514XL', 'Nizo Super 8']),
       see=[['D3', 'Cine film projector', 'the projector for the film it shoots']])
d8 = K('Double 8 camera', src='Cine film camera', a='8 mm cine camera · regular 8 camera',
       d_='Spring-wound movie camera for double-run 8 mm film, which is turned over and run twice.',
       tt=[['Drive', ['Spring-wound', 'Battery-driven']], ['Lens', ['Single lens', 'Turret lens']]],
       x=arch('Cine film camera', ['Bolex H8']),
       see=[['D3', 'Cine film projector', 'the projector for the film it shoots']])
c16 = K('16 mm cine camera', src='Cine film camera', a='16 mm movie camera',
        d_='Hand-held movie camera for 16 mm film, used by serious amateurs and low-budget film-makers.',
        tt=[['Drive', ['Spring-wound', 'Battery-driven']], ['Lens', ['Single lens', 'Turret lens']]],
        x=arch('Cine film camera', ['Bolex H16', 'Beaulieu R16']),
        see=[['D3', 'Cine film projector', 'the projector for the film it shoots']])

dep_film = DP('Film cameras', 'variety',
    'Organised as maker → system/mount → model → generation, following camera-wiki.',
    'Cameras that expose film, from 35 mm SLRs and rangefinders to medium- and large-format, instant, cine and novelty cameras; film itself → Film & darkroom, a digital body → Digital cameras.',
    'What does the camera make the picture on: 35 mm or smaller film, roll or sheet film, instant film, motion-picture film, or a wide or lo-fi frame?',
    [SH('35 mm film cameras',
        'Cameras for 35 mm film in cassettes: SLR, rangefinder and compact bodies, and half-frame cameras; a camera for 120 roll film → Medium & large format cameras.',
        'kinds by how the photographer frames and focuses: through the lens, by coupled rangefinder, by a compact finder, or on a half-size frame',
        [fslr, frf, f35c, half]),
     SH('Subminiature & cartridge cameras',
        'Cameras for tiny or drop-in film: Minox-style subminiatures, and 126, 110, APS or disc cartridge cameras; a 35 mm cassette camera → 35 mm film cameras.',
        '', [minox, cart]),
     SH('Medium & large format cameras',
        'Cameras for 120 roll film or sheet film: reflex, rangefinder, twin-lens, box, folding, view and press cameras; an instant-film camera → Instant cameras.',
        'kinds by film size and how you frame: reflex through the lens, rangefinder, twin lenses, simple box or folder finder, ground-glass view, press',
        [mfslr, mfrf, tlr, box, fold, view, press]),
     SH('Instant cameras',
        'Cameras that make a self-developing print: integral-film Polaroid and Instax types, peel-apart pack-film cameras and digital hybrids that print; the film itself → Film & darkroom.',
        '', [integral, peel, hybrid]),
     SH('Panoramic, toy & single-use cameras',
        'Film cameras defined by a deliberate limit: a very wide frame, a cheap plastic lens, no lens at all or a pre-loaded roll; a standard 120 camera → Medium & large format cameras.',
        'kinds by what makes the picture unusual: a very wide frame, a plastic lens, a bare aperture, or a pre-loaded disposable',
        [pano, toy, pinhole, single]),
     SH('Cine film cameras',
        'Hand-held movie cameras that expose Super 8, Double 8 or 16 mm film; professional 35 mm cinema cameras are not listed; a camcorder → Digital cameras.',
        '', [s8, d8, c16])])

# ---------------------------------------------------------------- LENSES
prime = K('Prime lens', tt=[['Focal length', ['Wide-angle', 'Standard', 'Short telephoto (portrait)', 'Telephoto']],
                             ['Focusing', ['Manual focus', 'Autofocus']],
                             ['Size', ['Pancake', 'Full-size']]])
zoom = K('Zoom lens', tt=[['Range', ['Wide zoom', 'Standard zoom', 'Telephoto zoom', 'Superzoom']],
                           ['Aperture', ['Constant aperture', 'Variable aperture']]])
macro = K('Macro lens', tt=[['Magnification', ['1:2', '1:1 (life size)', '2:1 and higher']],
                             ['Focal length', ['Short (50–60 mm)', 'Medium (90–105 mm)', 'Long (150–200 mm)']]],
          see=[['D4', 'Extension tube', 'a cheaper way to focus closer with an ordinary lens'],
               ['D4', 'Close-up lens', 'a screw-on way to focus closer']])
fish_x = [a for a in old['Fisheye lens']['x'] if a['n'] != 'Sigma fisheyes']
sig = [a for a in old['Fisheye lens']['x'] if a['n'] == 'Sigma fisheyes'][0]
fish_m = copy.deepcopy(old['Fisheye lens'].get('m', [])) + [[v['n'], 'Sigma'] for v in sig.get('v', [])
                                                              if [v['n'], 'Sigma'] not in old['Fisheye lens'].get('m', [])]
fish = K('Fisheye lens', tt=[['Image circle', ['Circular', 'Diagonal (full-frame)']], ['Zoom', ['Prime', 'Zoom']]],
         x=fish_x, m=fish_m, r=[['Fisheye lenses', 'Sigma']])
ts = K('Tilt-shift lens', tt=[['Movements', ['Shift only', 'Tilt and shift']]])
mirror = N('Mirror lens', 'catadioptric lens · reflex lens · CAT lens',
           'Compact long lens that folds the light path with mirrors, giving a fixed aperture and ring-shaped out-of-focus highlights.',
           [['Focal length', ['250–500 mm', '500–1000 mm', 'Over 1000 mm']],
            ['Aperture', ['Fixed f/8', 'Fixed f/11']],
            ['Focusing', ['Manual focus', 'Autofocus']]],
           WIKI + 'Catadioptric_system',
           x=[X('Reflex-Nikkor', 'Nikon\'s mirror lenses, sold as Mirror-Nikkor and Reflex-Nikkor, including a 500 mm f/8.',
                'Nikon', '', WIKI + 'Catadioptric_system'),
              X('Minolta AF Reflex 500mm f/8', 'The only autofocus mirror lens from a major brand, later sold by Sony for Alpha cameras.',
                'Minolta', '', WIKI + 'Catadioptric_system',
                v=[V('Minolta RF Rokkor-X 250mm f/5.6', 'Minolta', '', 'earlier manual lens with Mangin mirrors')])],
           m=[['500mm f/8 mirror lens', 'Samyang Optics']],
           see=[['E6', 'Maksutov-Cassegrain telescope', 'the same folded mirror optics in a telescope']])
ana = K('Anamorphic lens', tt=[['Squeeze', ['1.33x', '1.6x', '1.8x', '2x']], ['Flare colour', ['Blue', 'Amber']]])
fx = K('Special-effect lens', tt=[['Effect', ['Soft focus', 'Swirly bokeh', 'Selective focus (tilt)', 'Edge blur']]])

uv = K('UV and clear protection filter', tt=[['Type', ['UV or haze', 'Clear protector']], ['Mount', ['Screw-in', 'Magnetic']]])
pol = K('Polarising filter', tt=[['Type', ['Circular', 'Linear']], ['Mount', ['Screw-in', 'Square or slot system', 'Magnetic']]])
nd = K('Neutral density filter', tt=[['Type', ['Solid ND', 'Graduated ND', 'Variable ND']], ['Mount', ['Screw-in', 'Square or slot system']]])
colf = N('Colour and contrast filter', 'colour filter · conversion filter · contrast filter · didymium filter',
         'Coloured filter that lightens its own colour in black-and-white film, converts or corrects colour temperature, or boosts reds and greens.',
         [['Purpose', ['Contrast for black-and-white', 'Colour conversion', 'Colour correction', 'Colour enhancement (didymium)']],
          ['Colour', ['Yellow', 'Orange', 'Red', 'Green', 'Blue']]],
         WIKI + 'Photographic_filter')
irf = N('Infrared filter', 'IR filter · infrared pass filter',
        'Dark filter that blocks visible light and passes infrared, used with infrared film or converted cameras.',
        [['Grade', ['87-type', '88-type', '89-type']]],
        WIKI + 'Photographic_filter',
        see=[['D4', 'Infrared film', 'film sensitive to the light this filter passes']])
dif = K('Diffusion filter', src='Soft-effect filter', a='mist filter · soft-focus filter · pro-mist',
        d_='Filter that softens detail and adds a glow around highlights.',
        tt=[['Effect', ['Mist', 'Diffusion', 'Soft focus']], ['Strength', ['Light', 'Medium', 'Heavy']]])
effect = N('Effect filter', 'star filter · cross-screen filter · multi-image filter',
           'Filter that adds a visible effect: star-shaped streaks from highlights, repeated images or graduated colour.',
           [['Effect', ['Star or cross-screen', 'Multi-image', 'Graduated colour']],
            ['Star points', ['4-point', '6-point', '8-point']]],
           WIKI + 'Photographic_filter')
closeup = K('Close-up lens', tt=[['Construction', ['Single-element', 'Achromatic (two-element)']],
                                  ['Type', ['Full close-up lens', 'Split diopter']],
                                  ['Strength (dioptres)', ['+1', '+2', '+4', '+10']]],
            see=[['D4', 'Macro lens', 'a lens designed to focus close']])

madapt = K('Mount adapter', tt=[['Electronics', ['Manual (no electronics)', 'Electronic (autofocus and aperture control)']]],
           see=[['E6', 'Telescope camera adapter', 'T-rings fit a camera to a telescope']])
fred = K('Focal reducer', tt=[['Reduction', ['0.64x', '0.71x', '0.75x']],
                               ['Electronics', ['Manual', 'Electronic']]])
tc = K('Teleconverter', tt=[['Magnification', ['1.4x', '2x']], ['Maker', ['Camera maker\'s own', 'Third-party']]])
ext = K('Extension tube', a='macro extension tube',
        d_='Lensless spacer fitted between body and lens so the lens focuses closer.',
        tt=[['Electronics', ['Manual', 'Electronic contacts']], ['Set', ['Single tube', 'Stack of three']]])
bell = N('Bellows', 'macro bellows · focusing bellows',
         'Pleated, expandable light-tight tube set between body and lens, giving extreme close focus; also used on view cameras and enlargers.',
         [['Pleating', ['Bag bellows', 'Accordion bellows']], ['Fitted to', ['Camera and lens (macro)', 'View camera', 'Enlarger']]],
         WIKI + 'Bellows_(photography)')
rail = N('Focusing rail', 'macro rail · focus-stacking rail',
         'Geared rail that moves the camera and lens in small steps for macro focus and focus stacking.',
         [['Axes', ['Single-axis', 'Two-axis']]],
         'https://www.adorama.com/cm/l/Photography/Camera-Accessories?startAt=72')

dep_lens = DP('Lenses & filters', 'mixed',
    'Lenses are grouped by optical type (prime, zoom, macro and so on); mount is a detail on each archetype, not a grouping axis. Filters and adapters are tier.',
    'Lenses for interchangeable-lens cameras and the filters and adapters used with them; a lens built into a camera is part of that camera, an enlarger lens → Film & darkroom.',
    'Does the item form the image (a lens), change the light entering it (a filter) or change how a lens fits or reaches (an adapter)?',
    [SH('Camera lenses',
        'Detachable lenses sold by focal length and purpose: prime and zoom lenses, macro, fisheye, tilt-shift, mirror, anamorphic and effect lenses; a filter → Filters, a telescope eyepiece → E6.',
        'kinds by what the lens is built to do: fixed or variable focal length, close focus, extreme wide view, perspective control, long compact reach, cinema squeeze, creative effect',
        [prime, zoom, macro, fish, ts, mirror, ana, fx]),
     SH('Filters',
        'Glass or resin elements fitted in front of a lens to protect it or change the light: UV and clear, polarising, neutral density, colour, infrared, diffusion and effect filters, and close-up lenses.',
        'kinds by what the filter does: protects, removes glare, darkens evenly, shifts colour, passes infrared, softens, adds an effect, or lets the lens focus closer',
        [uv, pol, nd, colf, irf, dif, effect, closeup]),
     SH('Adapters & converters',
        'Rings and optics between lens and body: mount adapters, focal reducers, teleconverters, extension tubes, bellows and focusing rails; a telescope adapter → E6.',
        'kinds by what they change: only the mount, mount and brightness, focal length, or the closest focusing distance',
        [madapt, fred, tc, ext, bell, rail])])

# ---------------------------------------------------------------- FLASH & LIGHT
speed = K('Speedlight', tt=[['Form', ['Hot-shoe speedlight', 'Round-head flash', 'Mini flash']],
                             ['Control', ['Manual only', 'TTL', 'Built-in radio']]],
          m=old['Speedlight']['m'])
ringf = N('Ring flash', 'macro flash · ring light flash',
          'Flash that circles the lens for shadow-free portrait and macro work.',
          [['Use', ['Portrait', 'Macro']], ['Light source', ['Flash tube', 'LED']]],
          WIKI + 'Flash_(photography)',
          see=[['D4', 'Ring light', 'the constant-light version']])
studio = K('Studio flash', s=WIKI + 'Flash_(photography)', tt=[['Form', ['Monolight', 'Battery location flash', 'Pack and head']],
                                                                 ['Power', ['Mains', 'Battery']]])
trig = N('Flash trigger', 'radio trigger · flash slave · wireless flash trigger',
         'Transmitter and receiver that fire off-camera flashes by optical, infrared or radio link.',
         [['Link', ['Optical slave', 'Infrared', 'Radio']], ['Role', ['Transmitter', 'Receiver', 'Transceiver']]],
         WIKI + 'Flash_(photography)',
         r=[['Radio triggers', 'PocketWizard']])

ledp = K('LED panel', tt=[['Colour', ['Daylight', 'Bi-colour', 'RGB']]])
cob = K('COB LED light', tt=[['Colour', ['Daylight', 'Bi-colour', 'RGB']]])
tube = K('LED tube light', tt=[['Colour', ['Daylight', 'Bi-colour', 'RGB']]])
ring = K('Ring light', tt=[['Use', ['Phone and selfie', 'Portrait', 'Macro']], ['Colour', ['Daylight', 'Bi-colour']]],
         see=[['D4', 'Ring flash', 'the flash version']])
fres = K('Fresnel light', tt=[['Light source', ['LED', 'Tungsten']]])
tung = K('Tungsten light', tt=[['Wattage class', ['Redhead (about 800 W)', 'Blonde (about 2000 W)']]])

softbox = K('Softbox', src='Softbox & umbrella', a='softbox · octabox · strip light',
            d_='Fabric box fitted over a light that spreads and softens it through a diffusion panel.',
            tt=[['Shape', ['Rectangular', 'Strip box', 'Octabox', 'Parabolic', 'Lantern']],
                ['Mount', ['Speed ring', 'Speedlight bracket']]],
            m=models('Softbox & umbrella', ['Glow ParaSnap']), r=[])
umb = K('Umbrella', src='Softbox & umbrella', a='shoot-through umbrella · reflective umbrella',
        d_='Folding umbrella that bounces or passes light to give a broad, soft spread.',
        tt=[['Type', ['Reflective', 'Shoot-through', 'Convertible']], ['Shape', ['Standard', 'Deep parabolic']]],
        m=models('Softbox & umbrella', ['Profoto Deep Umbrella', 'Profoto Shallow Umbrella']), r=[])
refl = K('Reflector', src='Reflectors & dishes', a='fill reflector · 5-in-1 reflector',
         d_='Flat panel or disc that bounces light back to fill shadows.',
         tt=[['Form', ['Collapsible disc', '5-in-1 disc', 'Framed panel']],
             ['Surface', ['White', 'Silver', 'Gold', 'Black', 'Translucent']]],
         m=models('Reflectors & dishes', ['Westcott Illuminator']), r=[])
beauty = K('Beauty dish', src='Reflectors & dishes', a='beauty reflector',
           d_='Shallow dish with a centre baffle that gives soft but contrasty portrait light.',
           tt=[['Build', ['Rigid', 'Collapsible']], ['Finish', ['White interior', 'Silver interior']]],
           m=models('Reflectors & dishes', ['Profoto Softlight Reflector', 'Godox BDR-S55 Pro', 'Godox BDR-S550']), r=[])
rdish = K('Reflector dish', src='Reflectors & dishes', a='hard reflector · standard reflector',
          d_='Metal dish that fits a flash head and directs its light as a wide, zoomed or narrow beam.',
          tt=[['Beam', ['Wide', 'Zoom', 'Narrow']]],
          m=models('Reflectors & dishes', ['Profoto TeleZoom Reflector', 'Profoto SpillKill Reflector', 'Godox BeamLight Max90']), r=[])

grid = K('Grid and honeycomb', src='Beam shapers & gels', a='honeycomb grid · egg crate',
         d_='Honeycomb of cells that narrows a beam and cuts spill; also sold as a fabric grid for softboxes.',
         tt=[['Construction', ['Metal honeycomb', 'Fabric softbox grid']], ['Cell angle', ['10°', '20°', '30°', '40°']]],
         m=models('Beam shapers & gels', ['Profoto Softgrid', 'DoPchoice SnapGrid']), r=[])
snoot = K('Snoot', src='Beam shapers & gels', a='optical snoot',
          d_='Cone or tube that concentrates light into a small, focused circle.',
          tt=[['Optics', ['Plain cone', 'Optical (projecting) snoot']]],
          m=models('Beam shapers & gels', ['Elinchrom Snoot 26425', 'Godox Witstro Snoot AD-S9', 'Flashpoint Snoot Kit']), r=[])
barn = K('Barn doors', src='Beam shapers & gels', a='barndoors',
         d_='Hinged metal flaps on a light that block spill and sharpen the beam edge.',
         tt=[['Leaves', ['2-leaf', '4-leaf']], ['Fits', ['Speedlight', 'Studio head']]],
         m=models('Beam shapers & gels', ['Profoto 4-Leaf Barndoors', 'Godox BD-100 Barndoor']), r=[])
flag = N('Flag and net', 'flag · cutter · scrim · butterfly frame',
         'Opaque or mesh panel set between light and subject to block spill or cut intensity; large overhead frames soften sunlight.',
         [['Light control', ['Flag (blocks)', 'Cutter (narrow flag)', 'Net (reduces)', 'Overhead frame (butterfly)']],
          ['Net strength', ['Single net', 'Double net']]],
         old['Beam shapers & gels']['s'])
gobo = K('Gobo', src='Beam shapers & gels', a='gobo holder · pattern projector',
         d_='Stencil or cut-out placed in front of a light to project a shape or texture.',
         tt=[['Material', ['Metal', 'Glass']], ['Holder', ['Gobo holder', 'Built-in slot']]],
         m=models('Beam shapers & gels', ['Dedolight DP-1 Gobo Holder', 'Godox VSA-GS4 Gobo Set']), r=[])
gel = K('Colour gel', src='Beam shapers & gels', a='lighting gel · colour filter sheet',
        d_='Coloured or colour-correcting sheet placed over a light to change its colour.',
        tt=[['Purpose', ['Effect colour', 'Colour correction']], ['Form', ['Sheet', 'Pre-cut set']]],
        m=models('Beam shapers & gels', ['Godox VSA-11C Color Effect Set', 'Flashpoint V-11C Color Effect Filter Set']), r=[])

lstand = K('Light stand', tt=[['Size class', ['Compact', 'Standard', 'Heavy-duty (C-stand)']], ['Base', ['Tripod base', 'Wheeled base']]])
boom = K('Boom arm', tt=[['Support', ['Stand-mounted', 'Wall- or rail-mounted']], ['Balance', ['Sandbag counterweight', 'Built-in counterweight']]])
bstand = K('Backdrop stand', tt=[['Frame', ['Two stands and crossbar', 'Wall-mounted', 'Pop-up frame']], ['Rolls held', ['Single roll', 'Multiple rolls']]])
bdrop = K('Studio backdrop', tt=[['Material', ['Paper roll', 'Muslin', 'Vinyl']], ['Form', ['Rolled', 'Collapsible']]])

dep_light = DP('Flash & studio lighting', 'tier', '',
    'Lights for photography and video: flash units and triggers, constant lights, the modifiers that shape them and the stands that hold them; a torch → B3.',
    'Does the item make the light (flash or constant), shape it (a modifier) or hold it up (a stand)?',
    [SH('Flash',
        'Lights that fire a brief burst: on-camera speedlights, ring flashes, studio flash heads and the triggers that fire them; a light that stays on → Continuous lights.',
        'kinds by size and place: small on-camera unit, ring around the lens, studio head, and the trigger that fires them',
        [speed, ringf, studio, trig]),
     SH('Continuous lights',
        'Lights that stay on while you shoot, from LED panels and COB lights to tubes, rings, Fresnels and tungsten lamps; a flash → Flash.',
        'kinds by the shape of the light head: flat panel, point source, tube, ring, focusing lens, open lamp',
        [ledp, cob, tube, ring, fres, tung]),
     SH('Softening & bouncing modifiers',
        'Fabric or reflective modifiers that spread, soften or bounce light: softboxes, umbrellas, reflectors, beauty dishes and reflector dishes; a grid or snoot → Shaping & colouring modifiers.',
        'kinds by how the light is changed: through diffusion fabric, off an umbrella, off a flat panel, off a dish',
        [softbox, umb, refl, beauty, rdish]),
     SH('Shaping & colouring modifiers',
        'Attachments that narrow, block, pattern or colour a beam: grids, snoots, barn doors, flags, gobos and gels; a softbox → Softening & bouncing modifiers.',
        'kinds by what they do to the beam: narrow it, trim its edge, block it, pattern it, colour it',
        [grid, snoot, barn, flag, gobo, gel]),
     SH('Stands & backdrops',
        'Stands that hold lights and modifiers, and the backdrops and frames behind a subject; a camera tripod → Tripods, heads & plates.',
        'kinds by what is held up: a light on a stand, a light overhead on a boom, a background on a stand, or the background itself',
        [lstand, boom, bstand, bdrop])])

# ---------------------------------------------------------------- SUPPORT
tri = K('Tripod', s=WIKI + 'Tripod_(photography)', tt=[['Size', ['Full-size', 'Travel']],
                                                         ['Material', ['Aluminium', 'Carbon fibre']],
                                                         ['Leg locks', ['Twist', 'Flip']]])
flex = N('Flexible and table-top tripod', 'GorillaPod-type tripod · tablepod · mini tripod',
         'Small tripod with short or bendable legs that sits on a table or grips a pole, rail or branch.',
         [['Legs', ['Bendable ball-and-socket legs', 'Short fixed legs']],
          ['Carries', ['Compact camera', 'Mirrorless or DSLR camera']]],
         WIKI + 'Tripod_(photography)',
         x=[X('Joby GorillaPod', 'Flexible tripod with bendable ball-and-socket legs and rubber feet, first shown in 2006.',
              'Joby', '2006', 'https://reviewed.com/cameras/news/joby-inc-develops-flexible-tripod-for-point-and-shooters')])
mono = K('Monopod', tt=[['Material', ['Aluminium', 'Carbon fibre']], ['Foot', ['Single foot', 'Small three-foot base']]])
head = K('Tripod head', tt=[['Mechanism', ['Ball head', 'Pan-and-tilt (2-way or 3-way)', 'Fluid head', 'Geared head', 'Gimbal head', 'Panoramic head']],
                             ['Use', ['Stills', 'Video']]])
qr = K('Quick-release plate', tt=[['System', ['Arca-type', 'Proprietary']], ['Form', ['Plate', 'L-bracket', 'Clamp', 'Lens collar']]])

gimbal = K('Gimbal stabiliser', m=models('Gimbal stabiliser', ['DJI RS 2', 'DJI RS 4 Mini', 'Zhiyun WEEBILL 5']),
           r=[], tt=[['Carries', ['Mirrorless or DSLR camera', 'Compact camera', 'Phone']]],
           d_='Motorised handheld stabiliser that keeps a camera level; models that carry a phone are listed with phone gear.',
           see=[['D2', 'Phone camera & creator add-on', 'phone gimbals and creator gear'],
                ['D4', 'Pocket gimbal camera', 'a camera built into the gimbal']])
mech = N('Mechanical stabiliser', 'Steadicam-type stabiliser · spring-arm stabiliser',
         'Non-motorised stabiliser that isolates the camera from the operator\'s movement with springs and counterweights, worn on the body or held.',
         [['Carried', ['Body-worn vest and arm', 'Handheld post']], ['Balance', ['Spring arm', 'Counterweight']]],
         WIKI + 'Camera_stabilizer',
         x=[X('Steadicam', 'Body-mounted spring-arm camera stabiliser invented by camera operator Garrett Brown.', '', '',
              WIKI + 'Camera_stabilizer'),
            X('Glidecam', 'Handheld camera stabiliser invented by Martin Philip Stevens.', '', '1991', WIKI + 'Camera_stabilizer')])
cage = K('Camera cage', src='Camera rig & cage', a='camera rig · cage',
         d_='Frame that wraps a camera body and adds mounting points for monitors, microphones and handles.',
         tt=[['Fit', ['Model-specific', 'Universal']], ['Material', ['Aluminium', 'Carbon fibre']]],
         m=models('Camera rig & cage', ['edelkrone PocketRIG v2']), r=[])
sho = K('Shoulder rig', src='Camera rig & cage', a='shoulder support · chest rig · body-worn camera support',
        d_='Shoulder pad, harness or chest rig that moves a camera\'s weight onto the body and frees the hands.',
        tt=[['Worn on', ['Shoulder', 'Chest', 'Vest']]],
        m=models('Camera rig & cage', ['SmallRig HawkLock Shoulder Rig Pro SR007', 'Tilta Tiltaing Lightweight Shoulder Rig', 'Zacuto Recoil Rig']), r=[])
clamp = K('Clamp and magic arm', src='Camera rig & cage', a='camera clamp · super clamp · articulating arm',
          d_='Clamp and friction arm that hold a camera, light or monitor on a pole, rail or table.',
          tt=[['Grip', ['Super clamp', 'Spring clamp', 'Suction cup']], ['Arm', ['Fixed arm', 'Articulating friction arm']]],
          m=models('Camera rig & cage', ['Manfrotto Super Clamp', 'Manfrotto Magic Arm', 'Manfrotto Variable Friction Arm 244']), r=[])
slider = K('Camera slider', src='Slider, dolly & crane', a='slider · motion-control slider',
           d_='Short rail that slides a camera smoothly along a line.',
           tt=[['Drive', ['Manual', 'Motorised']], ['Material', ['Aluminium', 'Carbon fibre']]],
           m=models('Slider, dolly & crane', ['MoveOver8B', 'P1 Carbon Slider', 'Magic Carpet', 'ALX S4', 'Hot Dog Carbon Fiber Slider']), r=[])
dolly = K('Camera dolly', src='Slider, dolly & crane', a='track dolly · skater dolly',
          d_='Wheeled platform that rolls a camera along a floor or track.',
          tt=[['Runs on', ['Track', 'Smooth floor (skater)']]],
          m=models('Slider, dolly & crane', ['DollyONE v2', 'SYL-960', 'Swift Camera Track Dolly']), r=[])
jib = K('Jib and crane', src='Slider, dolly & crane', a='camera jib · camera crane',
        d_='Counterweighted arm that swings or lifts a camera through a shot.',
        tt=[['Arm', ['Jib arm', 'Crane']], ['Mount', ['Tripod-mounted', 'Dolly-mounted']]],
        m=models('Slider, dolly & crane', ['JibONE v3', 'JB40', 'Comet']), r=[])

dep_support = DP('Tripods & camera support', 'tier', '',
    'Supports that hold a camera still or move it smoothly: tripods, heads, monopods, plates, gimbals, rigs, sliders, dollies and jibs; a light stand → Stands & backdrops.',
    'Does the support hold the camera still, or move it through the shot?',
    [SH('Tripods, heads & plates',
        'Supports that keep a camera still: tripods, flexible tripods, heads, monopods and quick-release plates; a rig that moves the camera → Rigs & camera movement.',
        'kinds by part of the support: full legs, short or bendable legs, one leg, the head, the attachment plate',
        [tri, flex, mono, head, qr]),
     SH('Rigs & camera movement',
        'Gear that carries a camera and moves it: gimbals, mechanical stabilisers, cages, shoulder rigs, clamps, sliders, dollies and jibs; a tripod → Tripods, heads & plates.',
        'kinds by how the camera is moved: stabilised in the hand, held on a frame, clamped, or carried along a track or arm',
        [gimbal, mech, cage, sho, clamp, slider, dolly, jib])])

# ---------------------------------------------------------------- FILM & DARKROOM
FILMFMT = ['35 mm (135)', '120', 'Sheet film']
cneg = K('Colour negative film', tt=[['Film format', FILMFMT + ['110']],
                                      ['Speed class', ['Low (ISO 50–100)', 'Medium (ISO 200–400)', 'High (ISO 800 and up)']],
                                      ['Light balance', ['Daylight', 'Tungsten']]],
         see=[['D4', 'Colour process kit', 'the C-41 chemistry for this film']])
tri_x = [a for a in old['Black-and-white film']['x'] if a['n'] == 'Kodak Tri-X'][0]
tri_x.setdefault('v', []).append(V('Tri-X reversal processing', 'Kodak', '', 'Tri-X processed to slides, moved from the reversal shelf'))
bwx = [a for a in old['Black-and-white film']['x'] if a['n'] != 'Kodak Tri-X']
bwx.insert([a['n'] for a in old['Black-and-white film']['x']].index('Kodak Tri-X'), tri_x)
bw = K('Black-and-white film', x=bwx, tt=[['Film format', FILMFMT],
                                           ['Packaging', ['Cartridge', 'Bulk roll']],
                                           ['Grain structure', ['Traditional grain', 'Tabular grain']],
                                           ['Colour sensitivity', ['Panchromatic', 'Orthochromatic']]])
slide = K('Slide film', tt=[['Film format', FILMFMT + ['Super 8']], ['Process', ['E-6', 'K-14 (discontinued)']],
                             ['Light balance', ['Daylight', 'Tungsten']]],
          see=[['D3', 'Slide projector', 'shows the slides this film makes'], ['F5', 'Slide', 'a slide as a collected object']])
bwrev = K('Black-and-white reversal film', x=[a for a in old['Black-and-white reversal film']['x'] if a['n'] != 'Kodak Tri-X reversal'],
          tt=[['Film format', ['35 mm', '16 mm', 'Super 8', '8 mm']]])
irfilm = N('Infrared film', 'IR film · infrared black-and-white film',
           'Film sensitive to infrared light, giving pale foliage and dark skies, used with a dark red or infrared filter.',
           [['Film format', FILMFMT], ['Image', ['Black-and-white', 'Colour infrared']]],
           WIKI + 'Photographic_film')
cine = K('Cine colour negative film', tt=[['Film format', ['35 mm', '16 mm', 'Super 8', '120 (respooled)']],
                                           ['Light balance', ['Daylight', 'Tungsten']],
                                           ['Backing', ['With remjet', 'Remjet-free']]])
inti = K('Integral instant film', tt=[['Film format', ['SX-70', '600', 'Spectra', 'i-Type', 'Instax Mini', 'Instax Wide', 'Instax Square']],
                                       ['Image', ['Colour', 'Black-and-white']],
                                       ['Frame', ['Standard white frame', 'Special-edition frame']]],
          see=[['D4', 'Integral instant camera', 'the cameras that load it'], ['F2', 'Instant print', 'the print it makes']])
peelf = K('Peel-apart instant film', tt=[['Film format', ['Roll film', 'Pack film 100-series', 'Pack film 80-series (square)', '4×5 in sheet']],
                                          ['Image', ['Colour', 'Black-and-white']]],
          see=[['D4', 'Peel-apart instant camera', 'the cameras that load it']])

bagc = N('Changing bag', 'film changing bag · darkroom bag',
         'Light-proof bag with sleeved arm holes for loading film onto reels without a darkroom.',
         [['Size', ['Small (one tank)', 'Large (several reels or sheet holders)']]],
         WIKI + 'Darkroom', m=models('Tanks, reels & film handling', ['Paterson Changing Bag PTP125']))
tank = K('Developing tank and reels', src='Tanks, reels & film handling', a='developing tank · film reel · Paterson tank',
         d_='Light-tight tank and reels that hold film while chemicals are poured in and out.',
         tt=[['Tank material', ['Plastic', 'Stainless steel']], ['Agitation', ['Inversion tank', 'Rotary drum']],
             ['Capacity', ['One 35 mm reel', 'Two reels', 'Several reels']],
             ['Reel loading', ['Auto-load plastic reel', 'Hand-loaded stainless reel']]],
         m=models('Tanks, reels & film handling', ['Paterson Super System 4', 'Jobo Expert Drum', 'Arista Premium Double Reel Tank', 'Arista Classic Double Reel Tank',
                                                    'Paterson Auto Load Adjustable Reel', 'Jobo Duo Set Adjustable Reel', 'Hewes Pro Stainless Steel Reel',
                                                    'AGO Processor Reel', 'ARS-IMAGO LAB-BOX Reel']))
therm = K('Thermometer and graduate', src='Tanks, reels & film handling', a='darkroom thermometer · measuring jug',
          d_='Thermometer and measuring jug for mixing chemistry and holding it at the right temperature.',
          tt=[['Instrument', ['Thermometer', 'Graduated jug']], ['Sensor', ['Dial', 'Digital probe']]],
          m=models('Tanks, reels & film handling', ['PTP381 Color Thermometer', 'Plastic Graduate']), r=[], x=[])
fdev = K('Film developer', src='Darkroom chemistry', a='film developer · developer concentrate',
         d_='Chemical that turns exposed film into a visible black-and-white image.',
         tt=[['Form', ['Liquid concentrate', 'Powder']], ['Use', ['One-shot', 'Reusable']]],
         m=models('Darkroom chemistry', ['Ilford ID-11', 'Ilford Ilfotec DD-X', 'Ilford Ilfosol 3', 'Ilford Perceptol', 'Ilford Phenisol', 'Ilford Simplicity']),
         r=old['Darkroom chemistry'].get('r', []))
stopfix = K('Stop bath and fixer', src='Darkroom chemistry', a='stop bath · fixer · hypo clear',
            d_='Chemicals that halt development and then fix the image so the film no longer reacts to light.',
            tt=[['Step', ['Stop bath', 'Fixer', 'Hypo clearing agent', 'Wetting agent']], ['Form', ['Liquid', 'Powder']],
                ['Speed', ['Standard', 'Rapid']]],
            m=models('Darkroom chemistry', ['Ilford Ilfostop', 'Ilford Rapid Fixer', 'Ilford Hypam', 'Arista Premium Odorless Stop Bath', 'Arista Premium Odorless Rapid Fixer']), r=[])
ckit = N('Colour process kit', 'C-41 kit · E-6 kit · RA-4 kit',
         'Boxed chemistry for home developing colour negative (C-41), slide (E-6) or colour paper (RA-4).',
         [['Process', ['C-41 colour negative', 'E-6 slide', 'RA-4 colour paper']], ['Kit size', ['Small home kit', 'Large lab kit']]],
         WIKI + 'Photographic_processing')
fdry = K('Film dryer', src='Tanks, reels & film handling', a='film drying cabinet',
         d_='Heated cabinet or hanging rig that dries developed film without dust or water marks.',
         tt=[['Method', ['Heated drying cabinet', 'Hang and air dry']]],
         m=models('Tanks, reels & film handling', ['Mistral 3']), r=old['Tanks, reels & film handling'].get('r', []), x=[])
# the three Paterson/Jobo ranges stay with tanks
tank['r'] = old['Tanks, reels & film handling'].get('r', [])
fdry['r'] = []

enl = K('Enlarger', d_='Projector that exposes a negative onto paper; sold with a lens, negative carrier and filters.',
        tt=[['Light source', ['Condenser', 'Diffusion', 'Colour (dichroic) head']], ['Film size', ['35 mm', 'Medium format', 'Large format']]],
        m=models('Enlarger', ['Beseler 23CIII-XL', 'Beseler 45MXT', 'Beseler 67XL', 'Beseler Printmaker 67 VC']))
enlens = K('Enlarging lens', src='Enlarger', a='enlarger lens', d_='Lens made for an enlarger, matched to the film size it covers.',
           tt=[['Film size covered', ['35 mm', 'Medium format', 'Large format']]],
           m=models('Enlarger', ['Schneider Componon-S']), r=[], x=[])
cfilt = N('Contrast filter set', 'multigrade filters · variable-contrast filters',
          'Set of filters that changes the contrast of variable-contrast paper, fitted under the lens or in a head drawer.',
          [['Fitting', ['Under-lens', 'Filter drawer']], ['Paper', ['Variable-contrast black-and-white', 'Colour printing']]],
          WIKI + 'Darkroom', m=models('Enlarger', ['Ilford Multigrade Filter Set']))
easel = K('Enlarging easel', src='Easel & focus aids', a='print easel',
          d_='Frame that holds paper flat under the enlarger and masks the borders.',
          tt=[['Style', ['Bladed (adjustable borders)', 'Multi-size (4-in-1)', 'Quick (speed) easel']]],
          m=models('Easel & focus aids', ['Arista 4-in-1 Enlarging Easel']), r=[])
focus = K('Focus finder', src='Easel & focus aids', a='grain focuser · grain magnifier',
          d_='Magnifying aid that shows the film grain on the easel so the enlarger can be focused sharply.',
          tt=[['Method', ['Mirror grain focuser', 'Microscope-style finder']]],
          m=models('Easel & focus aids', ['Paterson Major Focus Finder', 'LegacyPro 10x Grain Focuser']), r=[])
timer = K('Darkroom timer', src='Easel & focus aids', a='enlarger timer · process timer',
          d_='Timer that switches the enlarger lamp for exposures or counts development steps.',
          tt=[['Role', ['Enlarger timer', 'Process timer']], ['Display', ['Digital', 'Analogue']]],
          m=models('Easel & focus aids', ['GraLab 300', 'GraLab 451R', 'Paterson Digital Timer', 'Kaiser Digital Darkroom Exposure Timer',
                                           'Beseler Digital Darkroom Timer 8197', 'CatLABS Universal Digital Darkroom Enlarger Timer', 'CatLABS Tank Top Timer',
                                           'Time-O-Lite GR-90', 'Time-O-Lite M-72R']), r=[])

cframe = N('Contact printing frame', 'contact printer · proof frame',
           'Glass-topped frame that presses a negative flat on paper to make a contact sheet or a print the size of the negative.',
           [['Cover', ['Glass-topped', 'Glassless']], ['Film size', ['35 mm strips', 'Medium format', 'Large format']]],
           WIKI + 'Darkroom')
paper = K('Photographic paper', tt=[['Base', ['Fibre-based', 'Resin-coated']], ['Contrast', ['Variable contrast', 'Graded']],
                                     ['Print process', ['Black-and-white darkroom', 'Colour (RA-4)', 'Inkjet']]])
pdev = N('Paper developer', 'print developer',
         'Chemical that brings up the image on exposed photographic paper.',
         [['Form', ['Liquid concentrate', 'Powder']], ['Image tone', ['Neutral', 'Warm']]],
         old['Darkroom chemistry']['s'],
         m=models('Darkroom chemistry', ['Ilford Multigrade Paper Developer', 'Ilford Bromophen', 'Arista Premium Liquid Paper Developer']))
tray = K('Developing tray', src='Trays, tongs & washers', a='print tray',
         d_='Shallow tray that holds paper in developer, stop bath, fixer or wash.',
         tt=[['Material', ['Plastic', 'Stainless steel']], ['Size', ['8×10 in', '11×14 in', '16×20 in']]],
         m=models('Trays, tongs & washers', ['Cesco Dimpled Bottom Developing Tray']), r=[])
tongs = K('Print tongs', src='Trays, tongs & washers', a='darkroom tongs', d_='Tongs that move paper between trays without touching the chemistry.',
          tt=[['Material', ['Plastic', 'Stainless steel']]],
          m=models('Trays, tongs & washers', ['Print Tongs PTP341']), r=[])
pwash = N('Print washer', 'archival print washer',
          'Tray or tank that washes fixer out of prints with running water.',
          [['Design', ['Archival washer', 'Tray siphon']]], old['Trays, tongs & washers']['s'])
pdry = K('Print dryer', src='Trays, tongs & washers', a='print drying rack',
         d_='Rack or heated dryer that dries washed prints.',
         tt=[['Method', ['Air-drying rack', 'Heated dryer']]],
         m=models('Trays, tongs & washers', ['Paterson Rapid Print Drying Rack']), r=[])
safe = K('Safelight', src='Trays, tongs & washers', a='darkroom lamp',
         d_='Dim coloured lamp that lights a darkroom without fogging black-and-white paper.',
         tt=[['Light source', ['LED', 'Filtered bulb']], ['Colour', ['Red', 'Amber']]],
         m=models('Trays, tongs & washers', ['Paterson Red Dome Safelight', 'ARS-IMAGO LED Darkroom Safelight', 'LegacyPro Safelight 5.5x6.5', 'Arista Darkroom Safelight']), r=[])
fscan = N('Film scanner', 'negative scanner · slide scanner',
          'Scanner that digitises negatives and slides by passing light through the film; some flatbeds do this with a transparency unit.',
          [['Scanner type', ['Dedicated film scanner', 'Flatbed with film adapter', 'Drum scanner']],
           ['Film size', ['35 mm', 'Medium format', 'Large format']]],
          WIKI + 'Image_scanner',
          see=[['D1', 'Scanner', 'flatbed scanners for prints and documents']])

dep_film2 = DP('Film & darkroom', 'mixed',
    'Film is variety (maker → stock → format, discontinued stocks included); darkroom equipment and chemistry are tier.',
    'Film to shoot and the kit to develop, print and scan it: film stocks, tanks and chemistry, enlargers, paper and scanners; a film camera → Film cameras, finished prints → F2.',
    'Which step is the item for: shooting the film, developing it, printing it or scanning it?',
    [SH('Photographic film',
        'Light-sensitive film sold by process and format: colour negative, black-and-white, slide, infrared, cine and instant film; the camera that loads it → Film cameras.',
        'kinds by process the film needs and what it records: colour negative, black-and-white, slide, reversal, infrared, cine, integral and peel-apart instant',
        [cneg, bw, slide, bwrev, irfilm, cine, inti, peelf]),
     SH('Film developing',
        'Kit for developing film at home: changing bags, tanks and reels, thermometers, developer, stop bath, fixer, colour kits and dryers; printing kit → Enlarging or Printing & finishing.',
        'kinds by the order of the workflow: load, develop and measure, chemistry, dry',
        [bagc, tank, therm, fdev, stopfix, ckit, fdry]),
     SH('Enlarging',
        'Equipment for projecting a negative onto paper: enlargers, enlarging lenses, contrast filters, easels, focus finders and timers; chemistry and trays → Printing & finishing.',
        'kinds by the order of the printing set-up: enlarger, lens, contrast control, paper holder, focus, exposure timing',
        [enl, enlens, cfilt, easel, focus, timer]),
     SH('Printing & finishing',
        'Paper and the darkroom items that develop, wash, dry and light a print: paper, paper developer, trays, tongs, washers, dryers and safelights.',
        'kinds by the order of the print workflow: contact, paper, developer, trays and tongs, wash, dry, light',
        [cframe, paper, pdev, tray, tongs, pwash, pdry, safe]),
     SH('Scanning', 'Equipment for digitising film: dedicated film scanners and flatbeds with a film adapter; a plain document scanner → D1.', '', [fscan])])

# ---------------------------------------------------------------- ACCESSORIES
bag = K('Camera bag', tt=[['Style', ['Shoulder bag', 'Messenger', 'Sling', 'Waist pack']], ['Interior', ['Removable insert', 'Fixed dividers']]])
pack = K('Camera backpack', tt=[['Access', ['Top-loading', 'Back-panel access', 'Side access']], ['Capacity', ['Under 20 L', '20–35 L', 'Over 35 L']]])
roll = K('Rolling camera case', a='roller bag · hard camera case',
         d_='Wheeled or hard-shell case with a pull handle for a large camera kit.',
         tt=[['Shell', ['Hard shell', 'Soft']], ['Carry', ['Wheeled', 'Hand-carried']]])
strap = K('Camera strap', tt=[['Style', ['Neck strap', 'Sling (cross-body)', 'Wrist strap', 'Harness']], ['Attachment', ['Lug loops', 'Tripod-screw anchor', 'Quick-release anchor']]])

batt = K('Camera battery and charger', tt=[['Make', ['Maker\'s own', 'Third-party']], ['Charger', ['Single', 'Dual', 'USB']]])
grip = K('Battery grip', tt=[['Cells', ['One battery', 'Two batteries', 'AA holder']]])
cgrip = N('Camera grip', 'hand grip · camera handle',
          'Add-on handle that gives a camera body a firmer hold.',
          [['Fit', ['Model-specific', 'Universal']], ['Material', ['Aluminium', 'Leather', 'Rubber']]],
          'https://www.adorama.com/cm/l/Photography/Camera-Accessories?startAt=72',
          see=[['D4', 'Battery grip', 'a grip that also holds a second battery']])
remote = K('Remote shutter release', tt=[['Link', ['Mechanical cable', 'Electronic cable', 'Wireless or infrared']], ['Timing', ['Plain release', 'Intervalometer']]])
cmic = N('Camera microphone', 'shotgun microphone · on-camera microphone',
         'Microphone that mounts on the camera shoe or a boom to record sound with video.',
         [['Pickup pattern', ['Shotgun', 'Stereo']], ['Connection', ['3.5 mm jack', 'USB-C', 'Digital hot shoe']]],
         'https://www.adorama.com/cm/l/Photography/Camera-Accessories?startAt=72',
         see=[['E3', 'Small-diaphragm condenser microphone', 'studio microphones of a similar pickup type']])

meter = K('Light meter', tt=[['Measures', ['Incident light', 'Reflected light', 'Spot (about 1°)', 'Flash', 'Colour']],
                              ['Sensor', ['Selenium cell', 'CdS', 'Silicon photodiode']]], s=WIKI + 'Light_meter')
vf = K('Viewfinder or eyepiece', tt=[['Type', ['Optical external finder', 'Electronic viewfinder', 'LCD loupe', 'Eyecup or magnifier']]])
fscreen = K('Focusing screen', tt=[['Pattern', ['Plain matte', 'Split-image', 'Grid']]])

hood = K('Lens hood', src='Lens hood and cap', a='lens shade',
         d_='Shade on the front of a lens that cuts flare and guards against knocks.',
         tt=[['Shape', ['Petal', 'Round']], ['Material', ['Plastic', 'Collapsible rubber', 'Metal']]])
cap = K('Lens and body cap', src='Lens hood and cap', a='lens cap · rear cap · body cap',
        d_='Cap that covers the front or rear of a lens, or the empty mount of a camera body.',
        tt=[['Position', ['Front cap', 'Rear cap', 'Body cap']], ['Fit', ['Snap-on', 'Pinch', 'Screw-in']]], x=[], m=[])
clean = K('Camera cleaning kit', tt=[['Part cleaned', ['Lens', 'Sensor']], ['Tool', ['Swabs', 'Blower', 'Brush', 'Fluid']]])
sprot = K('Screen protector', tt=[['Material', ['Tempered glass', 'Film']]],
          see=[['D2', 'Screen protector', 'the same sheet for a phone or tablet']])
uwh = K('Underwater housing', tt=[['Build', ['Hard housing', 'Soft waterproof bag']]],
        see=[['D4', 'Rugged compact camera', 'a camera built to go underwater without a housing']])
dry = K('Camera dry cabinet', tt=[['Humidity control', ['Electronic dehumidifier', 'Desiccant']], ['Size', ['Countertop box', 'Large cabinet']]])

dep_acc = DP('Camera accessories & parts', 'tier',
    'Tier mode: kinds and market-covering makers only, no archetypes. Listed by kind, not by SKU.',
    'Bags, power, grips, remotes, meters, viewfinders and care items that go with a camera; a lens → Lenses & filters, a tripod → Tripods & camera support.',
    'What does the item do for the camera and its owner: carry it, power or control it, measure light or view through it, or protect it?',
    [SH('Bags & straps',
        'Ways to carry a camera and lenses: shoulder bags, backpacks, wheeled cases and straps.',
        'kinds by how you carry: bag on the shoulder, pack on the back, wheeled case, strap on the body',
        [bag, pack, roll, strap]),
     SH('Power, grips & plug-ins',
        'Items that power or extend the body: batteries and chargers, grips, remote releases and microphones.',
        'kinds by what they add to the body: power, a firmer hold, remote firing or sound',
        [batt, grip, cgrip, remote, cmic]),
     SH('Metering & viewing',
        'Items that help judge or see the picture: light meters, add-on viewfinders and focusing screens.',
        'kinds by how you judge the picture: measure the light, look through an add-on finder, or change the focusing screen',
        [meter, vf, fscreen]),
     SH('Care & protection',
        'Items that guard a camera against glare, knocks, dust, scratches, water and damp.',
        'kinds by the threat they guard against: glare and knocks, dust, scratches, water, damp',
        [hood, cap, clean, sprot, uwh, dry])])

depts = [dep_digital, dep_film, dep_lens, dep_light, dep_support, dep_film2, dep_acc]

# every old kind must be used
missing = [n for n in old if n not in used]
assert not missing, missing

d['ax'] = 'What part of making a picture does the object do: capture it digitally or on film, form it with a lens, light it, steady the camera, process the film and prints, or carry and protect the kit?'
d['key'] = [
    '1. Does it record pictures to a memory card (a camera with a changeable or fixed lens, a camcorder, action, 360, drone or trail camera)? → Digital cameras',
    '2. Does it record pictures on film (35 mm, roll or sheet, instant, cine, toy or single-use)? → Film cameras',
    '3. Is it a lens, filter, close-up lens or adapter that goes on or behind a lens? → Lenses & filters',
    '4. Is it a flash, a constant light, a modifier that shapes light, or a stand or backdrop? → Flash & studio lighting',
    '5. Does it hold the camera still or move it (tripod, head, gimbal, rig, slider)? → Tripods & camera support',
    '6. Is it film itself, or kit to develop, print or scan film? → Film & darkroom',
    '7. Is it a bag, battery, grip, remote, meter, finder or care item for a camera? → Camera accessories & parts',
    '<i>Precedence: instant film is film (step 6) before the instant camera that loads it (step 2); a gimbal with its own camera is a camera (step 1); a lens built into a camera belongs to that camera; a phone or webcam → D2 or D1.</i>']
d['lead'] = ('Cameras, lenses and the gear around them, grouped by what each object does in making a picture; cameras and lenses by body type, system and mount, '
             'and film by process and format; flash, support, darkroom and accessories are kept to what a good buy needs.')
d['depts'] = depts

# validate see targets
import re
names = {k['n'] for D in depts for S in D['s'] for k in S['k']}
bad = []
for D in depts:
    for S in D['s']:
        for k in S['k']:
            for sv in k.get('see', []):
                if sv[0] == 'D4':
                    if sv[1] not in names:
                        bad.append((k['n'], sv))
                else:
                    tg = json.load(open(R + f'reader/{sv[0]}.json'))
                    tn = {kk['n'] for DD in tg['depts'] for SS in DD['s'] for kk in SS['k']}
                    if sv[1] not in tn:
                        bad.append((k['n'], sv))
assert not bad, bad

tmp = SRC + '.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, SRC)

renames = {
    'Softbox & umbrella': 'Softbox', 'Reflectors & dishes': 'Reflector', 'Beam shapers & gels': 'Grid and honeycomb',
    'Soft-effect filter': 'Diffusion filter', 'Box or folding camera': 'Folding camera', 'Cine film camera': 'Super 8 camera',
    'Slider, dolly & crane': 'Camera slider', 'Camera rig & cage': 'Camera cage', 'Tanks, reels & film handling': 'Developing tank and reels',
    'Darkroom chemistry': 'Film developer', 'Easel & focus aids': 'Enlarging easel', 'Trays, tongs & washers': 'Developing tray',
    'Lens hood and cap': 'Lens hood'}
json.dump(renames, open(R + 'out/D4_renames.json', 'w'), ensure_ascii=False, indent=1)

# brands
bp = R + 'out/D4_brands.json'
bj = json.load(open(BAK + 'D4_brands.json'))
have = {b['n'].lower() for b in bj['b']}
add = [
    {'n': 'Minox', 'c': 'Germany', 'seg': 'Specialist', 'kf': 'subminiature cameras',
     'd': 'Maker of the Minox subminiature camera invented by Walter Zapp, first built in Riga and later in West Germany.',
     's': WIKI + 'Minox', 'lines': ['Minox B', 'Minox LX', 'Minox EC']},
    {'n': 'Joby', 'c': 'United States', 'seg': 'Mainstream', 'kf': 'flexible tripods',
     'd': 'Santa Cruz, California maker of the GorillaPod flexible tripod, first shown in 2006.',
     's': 'https://reviewed.com/cameras/news/joby-inc-develops-flexible-tripod-for-point-and-shooters', 'lines': ['GorillaPod']},
]
for b in add:
    if b['n'].lower() not in have:
        bj['b'].append(b)
tmpb = bp + '.tmp'
json.dump(bj, open(tmpb, 'w'), ensure_ascii=False, indent=1)
os.replace(tmpb, bp)
print('built', len(names), 'kinds')
