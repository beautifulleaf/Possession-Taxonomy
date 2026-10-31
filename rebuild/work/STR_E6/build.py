import json, re, os, shutil
R = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(R + 'work/STR_E6/bak/E6.json'))
K = {}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k

WP = 'https://en.wikipedia.org/wiki/'
OPT = 'https://www.optcorp.com/telescope-accessories.html'
HST = 'https://www.homesciencetools.com/chemistry/lab-equipment/'
NAV = WP + 'Navigational_instrument'
OUT = 'https://windy.app/blog/weather-instruments.html'
REFL = WP + 'Reflecting_telescope'
REFR = WP + 'Keplerian_telescope'
BIN = WP + 'Binoculars'

def yr(x):
    m = re.search(r'(\d{4})', x.get('y', '') or '')
    return int(m.group(1)) if m else 9999

def A(n, d, mk, y, s, a='', v=None, dt=None):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': v or []}
    if dt: o['dt'] = dt
    return o

def kind(old_name, name=None, d=None, tt=None, drop_x=(), add_x=(), m=None, r=None, see=None, s=None, a=None, add_r=(), sortx=True):
    k = json.loads(json.dumps(K[old_name]))
    if name: k['n'] = name
    if d: k['d'] = d
    if s: k['s'] = s
    if a is not None: k['a'] = a
    k.pop('t', None)
    if tt: k['tt'] = tt
    xs = [x for x in k.get('x', []) or [] if x['n'] not in drop_x] + list(add_x)
    if sortx: xs.sort(key=yr)
    if xs: k['x'] = xs
    else: k.pop('x', None)
    if m is not None:
        if m: k['m'] = m
        else: k.pop('m', None)
    if r is not None:
        if r: k['r'] = r
        else: k.pop('r', None)
    if add_r: k['r'] = (k.get('r') or []) + list(add_r)
    if see: k['see'] = see
    return k

def new(n, d, s, tt, a='', x=None, m=None, r=None, see=None):
    k = {'n': n, 'a': a, 'd': d, 's': s, 'tt': tt}
    if x: k['x'] = x
    if m: k['m'] = m
    if r: k['r'] = r
    if see: k['see'] = see
    return k

def filt(k, key, names):
    return [t for t in (K[k].get(key) or []) if t[0] in names]

demoted = []

# ---------------- TELESCOPES ----------------
refractor = kind('Refractor telescope',
    d='Telescope that gathers light with a lens objective; sold by aperture, colour correction and focal ratio, from pocket scopes to large apochromats.',
    tt=[['Colour correction', ['Achromat', 'ED apochromat', 'Fluorite apochromat']],
        ['Lens elements', ['Doublet', 'Triplet', 'Quadruplet', 'Petzval astrograph']],
        ['Aperture', ['50-80 mm', '80-100 mm', '100-130 mm', 'Over 130 mm']],
        ['Tube material', ['Aluminium', 'Carbon fibre']]],
    add_x=[A('Galilean telescope', 'Convex objective with a concave eyepiece, giving an upright image and a narrow field; the first astronomical telescope.', 'Galileo Galilei', 'c. 1609', REFR),
           A('Keplerian telescope', 'Convex objective and convex eyepiece, giving a wider field and an inverted image; the basis of modern refractors.', 'Johannes Kepler', '1611', REFR)])
newtonian = kind('Newtonian & Dobsonian telescope', name='Newtonian reflector',
    d='Telescope with a concave primary mirror and a flat secondary at the side of the tube, on an equatorial, alt-azimuth or tabletop mount.',
    tt=[['Mount', ['Equatorial', 'Alt-azimuth', 'Tabletop']],
        ['Focal ratio', ['Fast f/4-f/5', 'Standard f/6-f/8']],
        ['Aperture', ['76-114 mm', '130-150 mm', '200 mm and over']],
        ['Corrector', ['None', 'Coma corrector', 'Schmidt corrector', 'Maksutov corrector']]],
    drop_x=("Newton's reflector", 'Dobsonian', 'Coulter Odyssey', 'Obsession truss Dobsonian'),
    m=[t for t in K['Newtonian & Dobsonian telescope']['m'] if t[0] in ('Explorer P', 'SpaceProbe 130ST EQ', 'AstroMaster 114 EQ', 'StarSense Explorer DX 130AZ', 'VX Newtonian')],
    r=[['StarSense Explorer', 'Celestron']],
    see=[['E6', 'Dobsonian telescope', 'a Newtonian on a rocker box']])
demoted.append("Newton's reflector (folded into kind definition)")
dobsonian = kind('Newtonian & Dobsonian telescope', name='Dobsonian telescope', a='Dob · Dobsonian · light bucket',
    d='Newtonian reflector on a simple rocker box that turns by hand, devised by John Dobson in 1965; the cheapest way to a large aperture.',
    tt=[['Tube construction', ['Solid tube', 'Collapsible tube', 'Truss tube']],
        ['Size', ['Tabletop 100-130 mm', 'Mid-size 150-250 mm', 'Large 300 mm and over']],
        ['Drive', ['Manual push', 'GoTo', 'Tracking platform']]],
    drop_x=("Newton's reflector",),
    add_x=[], sortx=True,
    m=[t for t in K['Newtonian & Dobsonian telescope']['m'] if t[0] in ('Skyliner Classic', 'Heritage FlexTube Virtuoso GTi', 'AD6', 'ProDob', 'Pro Truss', 'Z10 Deluxe')],
    r=[['SkyQuest', 'Orion Telescopes & Binoculars']],
    see=[['E6', 'Newtonian reflector', 'same optics on an equatorial or tabletop mount']])
dobsonian['x'] = [x for x in K['Newtonian & Dobsonian telescope']['x'] if x['n'] in ('Coulter Odyssey', 'Obsession truss Dobsonian')]
dobsonian['x'].sort(key=yr)
newtonian['x'] = [x for x in K['Newtonian & Dobsonian telescope']['x'] if x['n'] == 'Edmund Astroscan']
demoted.append("Dobsonian (1965) archetype (now the kind Dobsonian telescope)")
cass = kind('Cassegrain telescope',
    d='Telescope whose concave primary and convex secondary mirror fold the light back through a hole in the primary, giving a long focal length in a short tube.',
    tt=[['Mirror shapes', ['Parabolic and hyperbolic', 'Two hyperbolic', 'Ellipsoidal and spherical']],
        ['Tube', ['Closed', 'Open truss']],
        ['Aperture', ['150-250 mm', '250-400 mm', 'Over 400 mm']]],
    drop_x=('Classical Cassegrain',),
    add_x=[A('Dall-Kirkham telescope', 'Cassegrain with an ellipsoidal primary and a spherical secondary, easy to make; named after its 1930 magazine description.', 'Horace Dall', '1928', REFL)])
demoted.append("Classical Cassegrain (folded into kind definition)")
gregorian = new('Gregorian & off-axis reflector',
    'Reflector built to an older or unobstructed layout, such as the Gregorian, Herschelian, Schiefspiegler or Yolo; rare, mostly amateur-made or sold as reproductions.',
    REFL,
    [['Tilt', ['On-axis', 'Off-axis (tilted mirrors)']], ['Mirror count', ['Two', 'Three']], ['Origin', ['Amateur-built', 'Reproduction brass', 'Kit']]],
    a='Gregorian · Herschelian · Schiefspiegler',
    x=[A('Gregorian telescope', 'Reflector with a concave primary and a concave secondary, giving an upright image; first built by Robert Hooke.', 'James Gregory', '1663', REFL),
       A('Herschelian telescope', 'Reflector with a tilted primary so the observer looks in without a secondary mirror, used for the 40-foot telescope.', 'William Herschel', '1789', REFL),
       A('Schiefspiegler', 'Tilted-mirror reflector with no central obstruction, in the Kutter style.', 'Anton Kutter', '', REFL),
       A('Yolo telescope', 'Unobstructed tilted reflector.', 'Arthur S. Leonard', 'mid-1960s', REFL)])

sct = kind('Schmidt-Cassegrain telescope',
    d='Catadioptric telescope with a thin Schmidt corrector plate and a folded mirror path in a short, portable tube.',
    tt=[['Package', ['Optical tube only', 'Fork-mounted GoTo', 'Equatorial GoTo']],
        ['Corrector', ['Standard', 'Aplanatic']],
        ['Aperture', ['5-6 in', '8 in', '9.25-11 in', '14 in']]])
mct = kind('Maksutov-Cassegrain telescope',
    d='Catadioptric telescope with a deep meniscus corrector and a folded mirror path, giving a sharp, long-focus tube for the Moon and planets.',
    tt=[['Secondary mirror', ['Aluminised spot on the corrector (Gregory)', 'Separate mirror (Rumak)']],
        ['Aperture', ['90-102 mm', '127 mm', '150-180 mm']],
        ['Package', ['Tube only', 'GoTo fork', 'Tabletop']]],
    drop_x=('Rutten Maksutov (Rumak)',))
demoted.append('Rutten Maksutov (Rumak) (now a type of Maksutov-Cassegrain)')
astrograph = kind('Schmidt astrograph',
    d='Catadioptric imaging telescope with a full-aperture Schmidt corrector and a camera at prime focus inside the tube; very fast, for deep-sky photography.',
    tt=[['Aperture', ['8 in', '11 in', '14 in']], ['Focus', ['Prime focus', 'Prime focus with filter drawer']]])
smart = kind('Smart telescope',
    d='Self-aligning telescope with a camera and no eyepiece, or an electronic eyepiece, that shows the sky in an app.',
    tt=[['Optics', ['Refractor', 'Reflector']], ['Viewing', ['App only', 'Electronic eyepiece']], ['Aperture', ['Under 60 mm', '60-120 mm']]])
solar_t = kind('Solar telescope',
    tt=[['Etalon stack', ['Single', 'Double']], ['Wavelength', ['Hydrogen-alpha', 'Calcium-K']], ['Aperture', ['40 mm', '60-70 mm', '80 mm and over']]])
solar_f = kind('Solar filter',
    tt=[['Passes', ['White light', 'Hydrogen-alpha', 'Calcium-K']], ['Fits', ['Telescope front', 'Binoculars', 'Camera lens', 'Eyepiece']], ['Material', ['Polymer film', 'Coated glass']]])
eclipse = kind('Eclipse glasses',
    tt=[['Frame', ['Card', 'Plastic']], ['Form', ['Glasses', 'Handheld viewer', 'Clip-on']]])

telescopes = {'n': 'Telescopes', 'mode': 'variety', 'b': K and old['depts'][0]['b'], 'note': old['depts'][0]['note'],
    't': 'Instruments that gather light into an eyepiece or camera to show the sky, built from a lens, a mirror or both, plus solar and self-operating forms; a part that fits one → Telescope mounts & accessories; a handheld viewer → Binoculars & spotting scopes.',
    'ax': 'What gathers the light (lens, mirror or both), and is the telescope built for a special job: running itself or viewing the Sun?',
    's': [
     {'n': 'Refractors & reflectors', 't': 'Telescopes that gather light with a single lens or a single mirror system: the refractor, the Newtonian and Dobsonian, the Cassegrain and older mirror layouts; lens-and-mirror designs → Catadioptric telescopes.',
      'ax': 'kinds by what gathers the light: a lens, then mirrors in a flat-secondary, folded or tilted layout',
      'k': [refractor, newtonian, dobsonian, cass, gregorian]},
     {'n': 'Catadioptric telescopes', 't': 'Short-tube telescopes that combine a corrector lens with mirrors, such as the Schmidt-Cassegrain, Maksutov-Cassegrain and Schmidt astrograph; a plain mirror telescope → Refractors & reflectors.',
      'ax': 'kinds by the corrector and its job: a thin plate, a deep meniscus, or a full-aperture plate for imaging',
      'k': [sct, mct, astrograph]},
     {'n': 'Smart telescopes', 't': 'Self-aligning telescopes with a camera and app that show the sky on a screen, such as the Vaonis Stellina and Unistellar eVscope; a manual telescope with a camera → Astrophotography.',
      'k': [smart]},
     {'n': 'Solar observing', 't': 'Telescopes and filters made to view the Sun safely, such as an H-alpha telescope, a white-light film filter or eclipse glasses; ordinary night telescopes need a filter to join this shelf.',
      'ax': 'kinds by how much of the Sun they show: a dedicated telescope, a filter for your own optics, or glasses for the naked eye',
      'k': [solar_t, solar_f, eclipse]}]}

# ---------------- MOUNTS & ACCESSORIES ----------------
mnt_models = K['Mount accessory']['m']
tripod_models = [t for t in mnt_models if t[1] in ('Berlebach',) or t[0] == 'TC40 tripod']
tripod = new('Telescope tripod & pier',
    'Legs or a fixed column that stand under a mount head; sold with a mount or separately, in aluminium, steel, wood or carbon fibre.', OPT,
    [['Support', ['Tripod', 'Pier', 'Pier extension']], ['Leg material', ['Aluminium', 'Steel', 'Wood', 'Carbon fibre']], ['Head fitting', ['Flat plate', 'Threaded bolt']]],
    a='tripod · pier', m=tripod_models, see=[['D4', 'Tripod', 'camera tripod, lighter and for lenses']])
mount = kind('Telescope mount',
    d='Head that carries a telescope and turns it to follow the sky, by hand or motor; the choice of axis arrangement decides how it tracks.',
    tt=[['Axis arrangement', ['German equatorial', 'Fork equatorial', 'Alt-azimuth', 'Dual-mode alt-az and equatorial']],
        ['Drive', ['Manual', 'Tracking only', 'GoTo']],
        ['Gearing', ['Worm gear', 'Belt drive', 'Strain-wave (harmonic)']],
        ['Load class', ['Under 5 kg', '5-15 kg', '15-30 kg', 'Over 30 kg']]],
    drop_x=('German equatorial mount',), add_x=[])
mount['x'] = sorted(K['Telescope mount']['x'], key=yr)
star_tracker = kind('Star tracker',
    tt=[['Control', ['Tracking only', 'With GoTo']], ['Payload', ['Under 3 kg', '3-5 kg', 'Over 5 kg']]])
mfit = kind('Mount accessory', name='Mount fitting', a='equatorial wedge · polar scope · counterweight · tube rings',
    d='Wedge, polar scope, counterweight, tube rings or dovetail bar that fits between a telescope and its mount to align, balance and hold it.',
    tt=[['Fitting', ['Equatorial wedge', 'Polar scope or polar camera', 'Counterweight', 'Tube rings', 'Dovetail bar']],
        ['Dovetail standard', ['Vixen-style', 'Losmandy-style']]],
    m=[t for t in mnt_models if t not in tripod_models])
finder = kind('Telescope finder',
    d='Small sighting device fitted on a telescope tube to aim it: a red-dot or ring sight, or a small finderscope.',
    tt=[['Sight type', ['Red-dot', 'Reflex ring', 'Straight-through finderscope', 'Right-angle finderscope']], ['Image', ['Inverted', 'Correct-image']]])

focuser = kind('Telescope focuser',
    tt=[['Mechanism', ['Rack and pinion', 'Crayford', 'Helical', 'Dual-speed']], ['Drive', ['Manual', 'Motorised']], ['Barrel size', ['1.25-inch', '2-inch', '3-inch']]])
diag = kind('Star diagonal',
    tt=[['Reflecting part', ['Aluminium mirror', 'Dielectric mirror', 'Glass prism']], ['Image', ['Mirror-reversed', 'Upright and correct-handed']], ['Barrel size', ['1.25-inch', '2-inch']]])
barlow = kind('Barlow lens',
    tt=[['Power', ['2x', '2.5x', '3x', '5x']], ['Barrel size', ['1.25-inch', '2-inch']], ['Design', ['Fixed', 'Adjustable', 'Telecentric']]])
bino = kind('Binoviewer',
    tt=[['Nosepiece', ['1.25-inch', '2-inch']], ['Glass path', ['With corrector', 'Without corrector']]])
eyep = kind('Telescope eyepiece',
    tt=[['Barrel size', ['0.965-inch', '1.25-inch', '2-inch']], ['Focal length', ['Under 6 mm', '6-15 mm', '15-30 mm', 'Over 30 mm']], ['Apparent field', ['Narrow 40-50 degrees', 'Wide 60-70 degrees', 'Ultra-wide 80-110 degrees']], ['Zoom', ['Fixed', 'Zoom']]],
    drop_x=('Explorer Scientific wide-field series', 'Explore Scientific wide-field series'),
    add_r=[['wide-field series', 'Explore Scientific']])
demoted.append('Explore Scientific wide-field series (now a range)')

reducer = new('Focal reducer & field flattener',
    'Lens that shortens a telescope\'s focal length for a faster image, or flattens the field so stars stay sharp to the edge of a camera sensor.', OPT,
    [['Part', ['Focal reducer', 'Field flattener', 'Reducer-flattener', 'Coma corrector']], ['Factor', ['0.5x', '0.63x', '0.7x', '0.8x']]],
    a='reducer · corrector · flattener')
cam_adapter = kind('Telescope camera adapter',
    d='T-ring, T-adapter or off-axis guider that joins a camera to a telescope.',
    tt=[['Part', ['T-ring', 'T-adapter', 'Off-axis guider']], ['Camera mount', ['Canon EF', 'Nikon F', 'Sony E', 'Micro Four Thirds']]])
phone = new('Smartphone adapter',
    'Bracket or clamp that holds a phone camera over a telescope eyepiece, binocular or microscope for quick photographs.', OPT,
    [['Fits', ['Eyepiece', 'Binocular', 'Microscope']], ['Attachment', ['Clamp', 'Bracket mount', 'Case']]],
    a='phone adapter · digiscoping bracket')
afilter = kind('Astronomical filter',
    d='Filter for a telescope eyepiece barrel, filter wheel or camera that passes chosen wavelengths: colour and moon filters for the eye, light-pollution and narrowband filters for imaging.',
    tt=[['Passband', ['Broadband light-pollution', 'Dual-band', 'Tri- or quad-band', 'Narrowband single line', 'LRGB', 'Visual colour', 'Moon']],
        ['Mounting', ['Threaded 1.25-inch', 'Threaded 2-inch', 'Unmounted 31 mm', 'Unmounted 36 mm', 'Unmounted 50 mm']]])
fwheel = kind('Filter wheel',
    tt=[['Positions', ['5', '7', '8']], ['Filter size', ['1.25-inch / 31 mm', '36 mm', '2-inch / 50 mm']], ['Control', ['Manual', 'Motorised']]])
acam = kind('Astronomy camera',
    tt=[['Cooling', ['Cooled', 'Uncooled']], ['Sensor colour', ['Monochrome', 'One-shot colour']], ['Sensor type', ['CMOS', 'CCD']], ['Role', ['Deep-sky imaging', 'Planetary imaging', 'Guiding']]],
    drop_x=('ZWO ASI Pro cooled camera', 'ZWO ASI planetary camera'),
    add_r=[['ASI Pro cooled cameras', 'ZWO'], ['ASI planetary cameras', 'ZWO']])
demoted.append('ZWO ASI Pro cooled camera and ZWO ASI planetary camera (now ranges)')
fmotor = kind('Focus motor', tt=[['Fit', ['Clamp on the focus knob', 'Built into the focuser']], ['Control', ['Hand box', 'Computer']]])
acontrol = kind('Astrophotography controller', tt=[['Control from', ['Phone or tablet app', 'Laptop software']]],
    see=[['I1', 'Astrophotography software', 'the software side']])

collim = kind('Collimator', tt=[['Method', ['Sight tube', 'Cheshire eyepiece', 'Laser', 'Autocollimator']], ['Barrel size', ['1.25-inch', '2-inch']]])
dew = kind('Dew shield & heater', tt=[['Device', ['Rigid shield', 'Flexible shield', 'Heater strip', 'Heated shield', 'Dew controller']], ['Fits', ['Front of tube', 'Eyepiece', 'Finder']]])
power = new('Telescope power supply',
    'Battery pack or mains adapter that powers a mount, camera and dew heaters in the field or at a fixed site.', OPT,
    [['Source', ['Battery pack', 'Mains adapter']], ['Output', ['12 V DC', 'USB 5 V']]], a='power tank · field battery')
cloud = kind('Cloud sensor')
sqm = kind('Sky-quality meter')

accessories = {'n': 'Telescope mounts & accessories', 'mode': 'mixed', 'b': old['depts'][1]['b'], 'note': old['depts'][1]['note'],
    't': 'Parts and tools owners add to a telescope to hold and aim it, view the image, record it and keep the kit working; the telescope itself → Telescopes; a camera lens → D4.',
    'ax': 'What job does the part do: hold and aim the telescope, deliver the image to the eye, deliver it to a camera, or keep the kit and the sky in order?',
    's': [
     {'n': 'Mounts, tripods & aiming', 't': 'Everything that supports and points a telescope: tripod or pier, mount head, star tracker, fittings and the finder; the camera tripod for photography → D4.',
      'ax': 'kinds from the ground up: legs or pier, mount head, small tracker, fittings, then the sight',
      'k': [tripod, mount, star_tracker, mfit, finder]},
     {'n': 'Eyepieces & visual accessories', 't': 'Parts between the focuser and your eye: focuser, diagonal, Barlow lens, binoviewer and eyepiece; a camera in place of the eye → Astrophotography.',
      'ax': 'kinds along the light path from telescope to eye: focuser, diagonal, Barlow lens, binoviewer, eyepiece',
      'k': [focuser, diag, barlow, bino, eyep]},
     {'n': 'Astrophotography', 't': 'Cameras, filters, adapters and controllers that record the image instead of the eye, such as a cooled camera, a filter wheel or a field flattener.',
      'ax': 'kinds along the imaging chain from telescope to computer: reducer, adapter, filter, filter wheel, camera, focus motor, controller',
      'k': [reducer, cam_adapter, phone, afilter, fwheel, acam, fmotor, acontrol]},
     {'n': 'Care & observatory', 't': 'Tools and sensors that keep optics aligned, dry and powered and measure the sky at a fixed site, such as a collimator or a sky-quality meter.',
      'ax': 'kinds by what they look after: the optics, the dew, the power, then the site and sky',
      'k': [collim, dew, power, cloud, sqm]}]}

# ---------------- BINOCULARS ----------------
opera = kind('Opera glasses',
    tt=[['Support', ['Handheld', 'Lorgnette handle', 'Folding']], ['Body', ['Metal', 'Mother-of-pearl (antique)']]])
binoc = kind('Binoculars',
    d='Pair of matched telescopes held in both hands, named by magnification times objective diameter (8x42 is the common birding size).',
    tt=[['Prism system', ['Porro', 'Roof (Schmidt-Pechan)', 'Roof (Abbe-Koenig)']],
        ['Size', ['Compact 8x25', 'Mid-size 8x32', 'Full-size 8x42 or 10x42', 'Large 7x50 or 10x50', 'Astronomy 15x70']],
        ['Stabilisation', ['None', 'Image-stabilised']],
        ['Built-in extras', ['Rangefinder reticle', 'Compass', 'Zoom']]],
    add_x=[A('Zeiss Porro binoculars', 'First commercial Porro-prism binoculars, giving a short, wide body and strong depth.', 'Carl Zeiss', '1894', BIN),
           A('Hensoldt pentaprism roof binoculars', 'Early roof-prism binoculars with a pentaprism, marketed from 1897.', 'Moritz Hensoldt', '1897', BIN),
           A('Zeiss Victory FL', 'Alpha-class binoculars with dielectric-coated Schmidt-Pechan prisms.', 'Carl Zeiss', '2004', BIN)])
giant = kind('Giant binoculars',
    tt=[['Aperture', ['70-100 mm', '100-150 mm']], ['Eyepiece angle', ['Straight-through', '45 degrees', '90 degrees']], ['Eyepieces', ['Fixed', 'Interchangeable']]])
spy = new('Spyglass',
    'Hand-held draw-tube refracting telescope for viewing things on land, collapsed to carry; sold new as nautical gifts and antique.', WP + 'Spyglass',
    [['Number of draws', ['One', 'Three', 'Four']], ['Body covering', ['Bare brass', 'Leather', 'Wood']], ['Origin', ['Antique', 'Reproduction']]],
    a='pocket telescope · hand telescope · pirate telescope')
mono = kind('Monocular', tt=[['Body', ['Pocket', 'Standard', 'Close-focus']], ['Housing', ['Waterproof', 'Not sealed']]],
    see=[['H2', 'Low-vision monocular', 'made for low vision']])
spot = kind('Spotting scope',
    tt=[['Eyepiece angle', ['Angled 45 degrees', 'Straight']], ['Eyepiece', ['Fixed', 'Zoom', 'Interchangeable']], ['Objective glass', ['Standard', 'ED or fluorite']], ['Aperture', ['50-65 mm', '80 mm', '85-95 mm']]])
nv = kind('Night-vision viewer',
    tt=[['Tube generation', ['Gen 1', 'Gen 2', 'Gen 3', 'Autogated Gen 3']], ['Technology', ['Image-intensifier', 'Digital']], ['Form', ['Monocular', 'Binocular', 'Head-mounted']]],
    see=[['E4', 'Night-vision and thermal sight', 'weapon sight version']])
th = kind('Thermal-imaging viewer',
    tt=[['Form', ['Monocular', 'Binocular']], ['Sensor resolution', ['160x120', '384x288', '640x480', '1024x768']], ['Extras', ['Laser rangefinder', 'None']]],
    see=[['E4', 'Night-vision and thermal sight', 'weapon sight version']])

binoculars = {'n': 'Binoculars & spotting scopes', 'mode': 'mixed', 'b': old['depts'][2]['b'], 'note': old['depts'][2]['note'],
    't': 'Handheld and tripod viewers for distant things on land, by day or in the dark; a telescope for the sky → Telescopes; a weapon sight → E4; a low-vision aid → H2.',
    'ax': 'How many eyes does it use, and is it made for daylight or for the dark?',
    's': [
     {'n': 'Binoculars', 't': 'Two-eyed viewers from theatre glasses to giant sky binoculars, named by magnification and aperture; a night-vision binocular → Night optics.',
      'ax': 'kinds by size and use, from the smallest to the largest: theatre, general, giant',
      'k': [opera, binoc, giant]},
     {'n': 'Monoculars & spotting scopes', 't': 'One-eyed viewers by day, from a pocket spyglass to a tripod spotting scope; a telescope for the sky → Telescopes.',
      'ax': 'kinds by size and support, from the pocket to the tripod: spyglass, monocular, spotting scope',
      'k': [spy, mono, spot]},
     {'n': 'Night optics', 't': 'Viewers that show a scene in the dark by amplifying light or by heat, for naturalists, hunters and walkers; a weapon sight → E4.',
      'k': [nv, th]}]}

# ---------------- MICROSCOPES ----------------
simple = new('Simple microscope',
    'Microscope with a single strong lens held close to the specimen, the form Leeuwenhoek used; sold today as replicas, brass antiques and pocket lenses on a stand.', WP + 'Optical_microscope',
    [['Form', ['Handheld lens', 'Brass pillar stand', 'Folding pocket']], ['Lens', ['Glass bead', 'Ground lens', 'Doublet or triplet']], ['Origin', ['Antique', 'Reproduction']]],
    a='single-lens microscope · Leeuwenhoek-type',
    x=[A('Leeuwenhoek microscope', 'Tiny single-lens microscope clamped between metal plates, used to see microbes.', 'Antonie van Leeuwenhoek', '17th century', WP + 'Optical_microscope')])
compound = kind('Compound light microscope',
    d='Microscope with an objective and an eyepiece in series, for thin specimens on a slide; student models to research-grade stands.',
    tt=[['Eyepieces', ['Monocular', 'Binocular', 'Trinocular']], ['Optics', ['Finite 160 mm', 'Infinity-corrected']], ['Objective quality', ['Achromat', 'Plan achromat', 'Plan apochromat']], ['Contrast method', ['Brightfield', 'Darkfield', 'Phase contrast']], ['Age', ['New', 'Antique brass']]])
stereo = kind('Stereo microscope',
    tt=[['Optical path', ['Two objectives (Greenough)', 'Common main objective']], ['Magnification', ['Fixed', 'Zoom']], ['Stand', ['Table stand', 'Boom stand', 'Pillar']], ['Eyepiece tube', ['Binocular', 'Trinocular']]])
polar = kind('Polarising microscope',
    tt=[['Light path', ['Transmitted', 'Reflected']], ['Stage', ['Rotating', 'Fixed']], ['Fittings', ['Bertrand lens', 'Compensator slot']]])
inv = new('Inverted & metallurgical microscope',
    'Microscope that views a sample from below or by reflected light, for metals, cell cultures and watch parts; mostly bench instruments for specialists.', 'https://microscopemaster.com/choosing-a-microscope.html',
    [['Viewing from', ['Below (inverted)', 'Above (upright)']], ['Light', ['Reflected', 'Transmitted']], ['Sample', ['Metal', 'Cell culture', 'Watch parts']]],
    a='metallurgical microscope · inverted microscope')
dig = kind('Digital microscope',
    tt=[['Form', ['Handheld USB', 'Stand-mounted', 'Built-in screen']], ['Link', ['USB', 'Wi-Fi', 'HDMI']]],
    drop_x=('Dino-Lite handheld USB microscope',), add_r=[['handheld USB microscopes', 'Dino-Lite']])
demoted.append('Dino-Lite handheld USB microscope (now a range)')
pocket = kind('Pocket microscope',
    tt=[['Body', ['Pocket tube', 'Paper fold-up', 'Smartphone clip']], ['Light', ['Lit', 'Unlit']], ['Magnification', ['Fixed 60-120x', 'Zoom']]])
mparts = kind('Microscope optics & parts',
    tt=[['Part', ['Objective', 'Eyepiece', 'Condenser', 'Stage', 'Illuminator']], ['Standard', ['RMS thread', 'M25 thread', 'Infinity tube lens']], ['Eyepiece barrel', ['23.2 mm', '30 mm']]])
mcam = kind('Microscope camera', tt=[['Fit', ['Eyepiece tube', 'C-mount port']], ['Link', ['USB', 'HDMI', 'Wi-Fi']]])
mslide = kind('Microscope slide', tt=[['Form', ['Plain', 'Frosted end', 'Cavity (depression)']], ['Content', ['Blank', 'Prepared set', 'Antique mounted']]])
hand = kind('Handheld magnifier', tt=[['Light', ['Plain', 'Illuminated']], ['Lens', ['Glass', 'Acrylic']], ['Form', ['Round', 'Rectangular bar', 'Folding']]],
    see=[['H2', 'Handheld magnifier', 'low-vision aid']])
stand = kind('Stand magnifier', tt=[['Stand', ['Desk base', 'Floor stand', 'Neck cord', 'Clamp arm']], ['Light', ['Plain', 'Illuminated lamp']]],
    see=[['H2', 'Stand magnifier', 'low-vision aid']])
loupe = kind('Loupe', tt=[['Wear', ['Held to the eye', 'Eye socket']], ['Fold', ['Folding', 'Fixed tube']], ['Lens', ['Singlet', 'Triplet']], ['Magnification', ['5x', '10x', '20x']]])
headm = kind('Head-worn magnifier', tt=[['Wear', ['Headband', 'Spectacle clip-on']], ['Lens', ['Single', 'Flip-up', 'Binocular']], ['Light', ['Plain', 'LED']]])

microscopes = {'n': 'Microscopes & magnifiers', 'mode': 'mixed', 'b': old['depts'][3]['b'], 'note': old['depts'][3]['note'],
    't': 'Microscopes and hand lenses that enlarge small things for home, hobby and school use, with the parts bought for them; research electron or probe microscopes are out; a low-vision magnifier → H2.',
    'ax': 'Is it a microscope on a stand, a lens held in the hand or on the head, or a part added to a microscope?',
    's': [
     {'n': 'Microscopes', 't': 'Stand instruments that show a specimen on a slide or a solid object, such as a student compound, a stereo or a USB microscope; hand lenses → Magnifiers & loupes.',
      'ax': 'kinds by how the image is made and shown: one lens, two lenses in series, two paths for depth, polarised light, reflected light from below, a sensor and screen, or a pocket body',
      'k': [simple, compound, stereo, polar, inv, dig, pocket]},
     {'n': 'Microscope parts & slides', 't': 'Objectives, eyepieces, condensers, cameras and slides bought apart from the stand to upgrade, record or load a microscope.',
      'k': [mparts, mcam, mslide]},
     {'n': 'Magnifiers & loupes', 't': 'Lenses used without a stand tube: a handled glass, a desk magnifier, a jeweller\'s loupe or a head-worn magnifier; a low-vision aid → H2.',
      'ax': 'kinds by how the lens is held: in the hand, on a stand, at the eye, on the head',
      'k': [hand, stand, loupe, headm]}]}

# ---------------- WEATHER ----------------
wstation = kind('Weather station',
    tt=[['Sensors', ['All-in-one array', 'Separate sensors']], ['Link to display', ['Cabled', 'Wireless', 'Wi-Fi app only']], ['Wind sensor', ['Cup anemometer', 'Ultrasonic']], ['Radiation shield', ['Passive', 'Fan-aspirated']]],
    drop_x=('Fine Offset all-in-one station',), add_r=[['all-in-one stations', 'Fine Offset']],
    see=[['B4', 'Weathervane', 'ornamental wind vane']])
demoted.append('Fine Offset all-in-one station (now a range)')
athermo = kind('Air thermometer', tt=[['Reading', ['Liquid-in-glass', 'Dial', 'Digital']], ['Place', ['Indoor', 'Outdoor', 'Indoor-outdoor wireless']], ['Record', ['Current', 'Maximum-minimum']]])
galileo = kind('Galileo thermometer', a='termometro lento · Galilean thermometer',
    tt=[['Height', ['Table 20-30 cm', 'Tall 40-70 cm']]])
hygro = kind('Hygrometer', tt=[['Sensing', ['Hair', 'Digital', 'Wet and dry bulb']], ['Record', ['Reading only', 'Data-logging']], ['Place', ['Room', 'Terrarium', 'Humidor']]],
    see=[['J10', 'Hygrometer', 'cigar humidor type'], ['B10', 'Thermometer and hygrometer', 'reptile enclosure type']])
anemo = kind('Anemometer', tt=[['Sensing', ['Cup', 'Vane (impeller)', 'Hot-wire', 'Ultrasonic']], ['Form', ['Handheld', 'Mounted']], ['Readout', ['Speed only', 'Weather meter']]])
rain = kind('Rain gauge', tt=[['Collection', ['Manual', 'Tipping-bucket']], ['Link', ['None', 'Wireless']], ['Size', ['Pocket funnel', '4-inch', '8-inch']]])
sun = new('Sunshine recorder', 'Instrument that logs the hours of bright sunshine in a day, by burning a card, exposing paper or sensing light; a classic of weather-station collecting.', WP + 'Campbell%E2%80%93Stokes_recorder',
    [['Method', ['Burn card behind a glass sphere', 'Photosensitive paper', 'Electronic sensor']]],
    a='sunshine hours recorder',
    x=[A('Campbell-Stokes recorder', 'Glass sphere that focuses sunlight to burn a trace on a card; improved by Stokes in 1879.', 'John Francis Campbell', '1853', WP + 'Campbell%E2%80%93Stokes_recorder')])
light = new('Lightning detector', 'Receiver that senses the radio pulse of lightning to warn of an approaching storm; sold as a stand-alone unit or a weather-station add-on.', WP + 'Outline_of_meteorology',
    [['Form', ['Stand-alone receiver', 'Weather-station add-on', 'Personal alert']]], a='storm detector')
steven = new('Stevenson screen', 'White louvred box that shelters a thermometer and hygrometer from sun and rain so they read true air temperature.', WP + 'Outline_of_meteorology',
    [['Venting', ['Louvred', 'Fan-aspirated']], ['Material', ['Wood', 'Plastic']], ['Mounting', ['Post', 'Wall']]], a='instrument shelter · radiation shield')
geiger = kind('Geiger counter', tt=[['Detector', ['Geiger-Muller tube', 'Scintillator']], ['Reading', ['Counts', 'Dose rate', 'Dosimeter']], ['Data', ['No log', 'Data-logging', 'GPS mapping']], ['Radiation', ['Beta and gamma', 'Alpha-sensitive']]])
seis = kind('Home seismometer', tt=[['Axes', ['Vertical', 'Three-component']], ['Sensing', ['Geophone', 'MEMS accelerometer']]])
baro = kind('Barometer',
    tt=[['Mechanism', ['Mercury cistern', 'Aneroid', 'Digital']], ['Case form', ['Stick', 'Angle (diagonal)', 'Wheel (banjo)', 'Round dial', 'Marine gimballed']]],
    drop_x=('Marine barometer',))
demoted.append('Marine barometer (now a case form of Barometer)')
barog = kind('Barograph',
    tt=[['Chart', ['Daily drum', 'Weekly drum']], ['Drive', ['Clockwork', 'Electronic']], ['Precision', ['Standard', 'Microbarograph']]],
    drop_x=('Aneroid drum barograph',))
demoted.append('Aneroid drum barograph (generic; Richard Freres kept)')
storm = kind('Storm glass', see=[['E6', 'Barometer', 'a real pressure reading']])

weather = {'n': 'Weather & Earth instruments', 'mode': 'mixed', 'b': old['depts'][4]['b'], 'note': old['depts'][4]['note'],
    't': 'Instruments a person keeps to read the weather, air pressure, radiation and ground movement at home; a barometer built into a clock → A5; a room air-quality monitor → B7.',
    'ax': 'What does it read: the weather near the ground, the air pressure, or the ground and radiation?',
    's': [
     {'n': 'Weather stations & sensors', 't': 'Whole stations and single sensors for temperature, humidity, wind, rain, sunshine and lightning, such as a Davis Vantage Pro2 or a rain gauge; pressure → Barometers & weather glasses.',
      'ax': 'kinds by what they read: everything at once, then temperature, humidity, wind, rain, sunshine and lightning, then the shelter that houses them',
      'k': [wstation, athermo, galileo, hygro, anemo, rain, sun, light, steven]},
     {'n': 'Barometers & weather glasses', 't': 'Instruments that show air pressure and the weather it forecasts, from antique mercury sticks to a storm glass; a station with a pressure sensor → Weather stations & sensors.',
      'ax': 'kinds by how pressure is shown: a pointer or column, a chart line, or crystals in a glass',
      'k': [baro, barog, storm]},
     {'n': 'Earth & radiation sensors', 't': 'Small instruments that detect ionising radiation or ground motion at home, such as a Geiger counter or a Raspberry Shake.',
      'k': [geiger, seis]}]}

# ---------------- SKY MODELS ----------------
orr = kind('Orrery', tt=[['Scope', ['Grand (all known planets)', 'Tellurion (Sun, Earth, Moon)']], ['Drive', ['Hand-cranked', 'Clockwork', 'Electric']], ['Build', ['Brass', 'Wood', 'Kit or desk model']]])
arm = kind('Armillary sphere', tt=[['Centre', ['Earth (Ptolemaic)', 'Sun (Copernican)']], ['Setting', ['Desk', 'Garden']], ['Material', ['Brass', 'Wood', 'Painted metal']]])
cel = kind('Celestial globe', tt=[['Stand', ['Table', 'Floor']], ['Light', ['Plain', 'Illuminated']], ['Age', ['Antique printed gores', 'Modern']], ['Set', ['Single', 'Pair with a terrestrial globe']]],
    see=[['F1', 'Celestial globe', 'collected as a globe']])
plan_p = kind('Home planetarium projector', tt=[['Projection', ['Optical star disc', 'LED nebula or galaxy']], ['Extras', ['Rotation', 'Shooting stars']]],
    see=[['I1', 'Planetarium software', 'the software version']])
astro = kind('Astrolabe', tt=[['Material', ['Brass', 'Wood', 'Printed card']], ['Origin', ['Antique', 'Reproduction']]])
planis = kind('Planisphere', tt=[['Sides', ['Single-sided', 'Two-sided (north and south)']], ['Latitude', ['One latitude band', 'Several bands']], ['Material', ['Card', 'Plastic']]])
noct = new('Nocturnal', 'Hand dial that tells the time at night by lining a pointer up with Polaris and a guard star; a navigators\' timepiece, sold today as brass reproductions.', NAV,
    [['Material', ['Brass', 'Wood', 'Boxwood']], ['Origin', ['Antique', 'Reproduction']]], a='night clock',
    see=[['A5', 'Sundial', 'time from the sun instead of the stars']])
quad = new('Quadrant', 'Quarter-circle instrument that measures the angle of a star or the Sun above the horizon with a plumb line or sights; pocket and observatory forms.', WP + 'Quadrant_(instrument)',
    [['Use', ['Pocket', 'Marine', 'Observatory wall (mural)']], ['Material', ['Brass', 'Wood']], ['Origin', ['Antique', 'Reproduction']]],
    x=[A("Gunter's quadrant", 'Pocket quadrant carrying projections of the tropics, equator and horizon, used to find time and day length.', 'Edmund Gunter', '1623', WP + 'Quadrant_(instrument)')])
back = new('Backstaff', 'Navigator\'s instrument that measures the Sun\'s height by the shadow it casts, so the user faces away from the Sun; replaced by the octant.', WP + 'Backstaff',
    [['Build', ['Wood', 'Ebony and brass']], ['Arcs', ['One arc', 'Two arcs (large and small)']], ['Origin', ['Antique', 'Reproduction']]], a='Davis quadrant · back staff',
    x=[A('Davis quadrant', 'Backstaff with a small and a large arc, the form most identified with the instrument.', 'John Davis', '1594', WP + 'Backstaff'),
       A('Cole quadrant', 'Late backstaff variant of the Davis quadrant.', 'Benjamin Cole', '1748', WP + 'Backstaff')])
sext = kind('Sextant', tt=[['Arc', ['Octant (one-eighth circle)', 'Sextant (one-sixth circle)']], ['Reading', ['Vernier', 'Micrometer drum']], ['Material', ['Brass', 'Aluminium', 'Plastic']]])

sky = {'n': 'Sky models & historic instruments', 'mode': 'variety', 'b': old['depts'][5]['b'], 'note': old['depts'][5]['note'],
    't': 'Models of the sky and old instruments for finding stars, time and position, collected new or antique; a telescope → Telescopes; a terrestrial globe → F1; a clock or sundial → A5.',
    'ax': 'Does it show the sky as a model to look at, or is it used to find stars, time and position?',
    's': [
     {'n': 'Sky models', 't': 'Display models of the heavens: orrery, armillary sphere, celestial globe or a home planetarium projector; a hand instrument for finding stars → Star finders & navigation instruments.',
      'ax': 'kinds by what is modelled: planets in motion, the sky as rings, the stars on a sphere, the sky projected on a ceiling',
      'k': [orr, arm, cel, plan_p]},
     {'n': 'Star finders & navigation instruments', 't': 'Hand instruments that find stars, tell the time by them or measure a star\'s height, such as an astrolabe, a planisphere or a sextant; a display model → Sky models.',
      'ax': 'kinds by what is read off: stars and time (planisphere, astrolabe, nocturnal), or an angle above the horizon (quadrant, backstaff, sextant)',
      'k': [planis, astro, noct, quad, back, sext]}]}

# ---------------- LAB ----------------
glass = kind('Laboratory glassware', tt=[['Vessel', ['Beaker', 'Erlenmeyer flask', 'Round-bottom flask', 'Test tube', 'Condenser', 'Still head']], ['Glass', ['Soda-lime', 'Borosilicate 3.3']], ['Size', ['Under 100 ml', '100-500 ml', 'Over 500 ml']]],
    see=[['E1', 'Chemistry set', 'toy version for children']])
meas = kind('Measuring & dispensing', tt=[['Device', ['Graduated cylinder', 'Volumetric flask', 'Burette', 'Pipette', 'Micropipette']], ['Accuracy class', ['Class A', 'Class B']], ['Material', ['Glass', 'Plastic']]])
mortar = new('Mortar & pestle', 'Bowl and club for grinding solids to powder at the bench.', HST, [['Material', ['Porcelain', 'Glass', 'Agate', 'Marble']]], a='pestle and mortar')
funnel = new('Funnel & filter paper', 'Funnels and paper that separate a solid from a liquid.', HST, [['Item', ['Glass funnel', 'Plastic funnel', 'Buchner funnel', 'Filter paper']], ['Paper grade', ['Qualitative', 'Quantitative']]], a='filtration')
lstand = new('Lab stand & clamp', 'Metal rod on a base with rings and clamps that hold glassware above a heater.', HST, [['Part', ['Retort stand', 'Ring', 'Boss head', 'Clamp']], ['Material', ['Steel', 'Cast iron']]], a='retort stand · ring stand')
balance_m = [t for t in K['Lab instruments']['m'] if t[0] in ('Pioneer PX', 'ME-TE', 'Accuris Compact balances')]
therm_m = [t for t in K['Lab instruments']['m'] if t[0] in ('Checktemp 1', 'H-B DURAC', 'Digi-Sense Advanced Precalibrated Thermocouple Thermometer')]
stir_m = [t for t in K['Lab instruments']['m'] if t[0] in ('RCT basic', 'Hei-PLATE', 'Cimarec+', 'Isotemp hotplate stirrer')]
cent_m = [t for t in K['Lab instruments']['m'] if t[0] in ('5452 Minispin', '5453 Minispin Plus', 'accuSpin Micro 17')]
LS = K['Lab instruments']['s']
balance = new('Laboratory balance', 'Digital scale reading to 0.1 g or finer, for weighing chemicals, cultures and brewing additions.', LS,
    [['Readability', ['0.1 g', '0.01 g', '0.001 g']], ['Capacity', ['Under 200 g', '200-1000 g', 'Over 1 kg']], ['Class', ['Compact', 'Precision', 'Analytical']]],
    a='analytical balance · precision scale', m=balance_m, see=[['B5', 'Kitchen scale', 'kitchen version, coarser']])
hotplate = new('Hot plate & stirrer', 'Heater, with or without a magnetic stirrer, that warms and mixes liquids in flasks.', LS,
    [['Heat source', ['Hot plate', 'Alcohol lamp', 'Bunsen burner']], ['Stirring', ['None', 'Magnetic stirrer built in']], ['Plate', ['Ceramic', 'Aluminium']]],
    a='magnetic stirrer · stirring hotplate', m=stir_m)
centr = new('Centrifuge', 'Spinning unit that separates a liquid sample by density, from a micro-tube spinner to a bench rotor.', LS,
    [['Rotor', ['Fixed-angle', 'Swing-out']], ['Tube size', ['1.5-2 ml', '15 ml', '50 ml']], ['Speed', ['Fixed', 'Variable']]],
    a='mini centrifuge · microcentrifuge', m=cent_m)
lthermo = new('Laboratory thermometer', 'Thermometer for liquids and cultures, in glass, dial or digital probe form.', LS,
    [['Sensor', ['Liquid-in-glass', 'Dial', 'Digital probe']], ['Range', ['To 110 C', 'To 360 C']]],
    a='lab thermometer', m=therm_m, see=[['B5', 'Kitchen thermometer', 'cooking version']])
spectro = kind('Spectroscope', tt=[['Dispersion', ['Prism', 'Diffraction grating']], ['Form', ['Handheld', 'Bench', 'Gemmological']], ['Readout', ['Eye', 'Camera']]])
CS = K['Culture & sterile kit']['s']
petri = new('Petri dish', 'Shallow lidded dish for growing cultures on agar.', CS,
    [['Material', ['Plastic sterile', 'Reusable glass']], ['Diameter', ['60 mm', '90 mm', '100 mm']], ['Lid', ['Vented', 'Unvented']]],
    a='culture dish', m=[t for t in K['Culture & sterile kit']['m'] if 'Petri' in t[0]])
incub = new('Incubator', 'Small heated cabinet that holds cultures at a steady temperature.', CS,
    [['Size', ['Mini', 'Benchtop', 'Vertical']], ['Control', ['Digital', 'Analogue']], ['Cooling', ['Heat only', 'Heat and cool']]],
    a='culture incubator', m=[t for t in K['Culture & sterile kit']['m'] if 'Incubator' in t[0]])
hood = new('Laminar-flow hood', 'Cabinet that blows filtered air over the work area to keep cultures sterile.', CS,
    [['Flow', ['Horizontal', 'Vertical']], ['Size', ['Benchtop', 'Cabinet']]],
    a='clean bench · flow hood', m=[t for t in K['Culture & sterile kit']['m'] if 'Flow' in t[0] or 'Clean Bench' in t[0]])
dissect = new('Dissection set', 'Scalpel, forceps, scissors, probes and pins in a case for preparing specimens.', CS,
    [['Level', ['Student', 'Economy', 'Deluxe']], ['Contents', ['Scalpel', 'Forceps', 'Scissors', 'Probes', 'Pins', 'Tray']]],
    a='dissecting kit', m=[t for t in K['Culture & sterile kit']['m'] if 'Dissect' in t[0]])

lab = {'n': 'Home & hobby lab', 'mode': 'tier', 'b': old['depts'][6]['b'], 'note': old['depts'][6]['note'],
    't': 'Glassware, bench devices and kits that amateurs, home brewers, mycologists and students own for working on samples; industrial lab equipment is out; a toy chemistry set → E1.',
    'ax': 'What is done to the sample: holding and measuring it, treating it on the bench, or growing and preparing it?',
    's': [
     {'n': 'Glassware & labware', 't': 'Vessels and small tools that hold, measure, grind, filter and support: beakers, cylinders, mortars, funnels and stands; a powered device → Bench equipment & analysis.',
      'ax': 'kinds by job at the bench: hold and heat, measure and transfer, grind, filter, support',
      'k': [glass, meas, mortar, funnel, lstand]},
     {'n': 'Bench equipment & analysis', 't': 'Devices that weigh, heat, stir, spin or analyse a sample: balance, hot plate, centrifuge, thermometer and spectroscope; glassware → Glassware & labware.',
      'ax': 'kinds by what is done to the sample: weigh, heat and stir, spin, take its temperature, analyse its light',
      'k': [balance, hotplate, centr, lthermo, spectro]},
     {'n': 'Culture & specimen kit', 't': 'Items for growing cultures and preparing specimens: Petri dishes, an incubator, a flow hood, a dissection set; a microscope to look at them → Microscopes & magnifiers.',
      'ax': 'kinds by stage of the work: dish to grow in, incubator to keep warm, hood to keep sterile, set to dissect',
      'k': [petri, incub, hood, dissect]}]}

depts = [telescopes, accessories, binoculars, microscopes, weather, sky, lab]
cat = {
 'c': 'E6', 'rev': True, 'lead': old['lead'],
 'ax': 'What is it for: looking at the sky, at distant things on land, at the very small, reading the weather and ground, modelling or finding stars, or working with samples at a bench; and is it the instrument or a part that fits one?',
 'key': [
  '1. Is it a part, tool or sensor that fits a telescope (mount, eyepiece, camera, filter, collimator)? → Telescope mounts & accessories',
  '2. Does it gather light from the sky for you to look into on its own (refractor, reflector, catadioptric, smart, solar)? → Telescopes',
  '3. Is it a viewer for distant things on land or for the dark (binoculars, monocular, spotting scope, night vision)? → Binoculars & spotting scopes',
  '4. Does it enlarge small things, with a microscope stand or a lens held to the eye? → Microscopes & magnifiers',
  '5. Does it read the weather, air pressure, radiation or ground movement? → Weather & Earth instruments',
  '6. Is it a model of the sky or an old star-finding or navigating instrument? → Sky models & historic instruments',
  '7. Is it glassware, a bench device or a kit for working on samples? → Home & hobby lab',
  '<i>Precedence: a camera or filter made for a telescope is a telescope accessory (step 1) before a microscope camera (step 4); a low-vision magnifier → H2; a night-vision weapon sight → E4; a celestial globe sold as a map object → F1.</i>'],
 'b': old.get('b', []), 'depts': depts}

# dept 'b' for telescopes: use the original (K and ... pattern above); fix
cat['depts'][0]['b'] = old['depts'][0]['b']

# every old kind accounted for?
placed = {k['n'] for dp in depts for s in dp['s'] for k in s['k']}
renamed = {'Newtonian & Dobsonian telescope': 'Newtonian reflector', 'Mount accessory': 'Mount fitting',
           'Lab instruments': 'Laboratory balance', 'Culture & sterile kit': 'Petri dish'}
for n in K:
    if n not in placed and n not in renamed:
        print('MISSING', n)

out = R + 'out/E6.json'
tmp = out + '.tmp'
json.dump(cat, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, out)
json.dump(renamed, open(R + 'out/E6_renames.json', 'w'), indent=1, ensure_ascii=False)
json.dump(demoted, open(R + 'work/STR_E6/demoted.json', 'w'), indent=1)
print('written', os.path.getsize(out))
