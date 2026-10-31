import json, copy, os, sys
R = '/home/user/Possession-Taxonomy/rebuild/'
d = json.load(open(R + 'work/STR_B3/bak/B3.json'))

kinds = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            kinds[k['n']] = k
before = dict(depts=len(d['depts']), shelves=sum(len(dp['s']) for dp in d['depts']),
              kinds=len(kinds), arch=sum(len(k.get('x', [])) for k in kinds.values()))

WIKI_LF = 'https://en.wikipedia.org/wiki/Light_fixture'
WIKI_FL = 'https://en.wikipedia.org/wiki/Flashlight'
WIKI_LA = 'https://en.wikipedia.org/wiki/Lantern'
WIKI_LS = 'https://en.wikipedia.org/wiki/Landscape_lighting'

# ---------- demotions of generic archetypes ----------
log = {'demoted': [], 'merged': [], 'added_kinds': [], 'added_arch': [], 'renamed': []}

def pop_arch(kn, an):
    k = kinds[kn]
    for i, a in enumerate(k['x']):
        if a['n'] == an:
            return k['x'].pop(i)
    raise KeyError((kn, an))

def demote(kn, an, to_models=False):
    a = pop_arch(kn, an)
    log['demoted'].append(f'{an} ({kn})')
    if to_models:
        k = kinds[kn]
        have = {tuple(m) for m in k.get('m', [])}
        for v in a.get('v', []):
            m = [v['n'], v.get('mk') or a.get('mk')]
            if m[1] and tuple(m) not in have:
                k.setdefault('m', []).append(m); have.add(tuple(m))
        r = k.setdefault('r', [])
        rr = [a['n'], a.get('mk')]
        if a.get('mk') and rr not in r:
            r.append(rr)

# Tiffany floor lamp becomes versions of Tiffany lamp
tf = pop_arch('Floor lamp', 'Tiffany floor lamp')
tl = [a for a in kinds['Table lamp']['x'] if a['n'] == 'Tiffany lamp'][0]
tl['v'].append({'n': 'Floor lamp with leaded shade', 'mk': 'Tiffany Studios', 'y': 'c. 1904-15', 'd': 'standing lamp on a bronze base'})
for v in tf.get('v', []):
    tl['v'].append(v)
log['merged'].append('Tiffany floor lamp -> version of Tiffany lamp')

demote('Floor lamp', 'Torchère')
demote('Desk lamp', 'Gooseneck lamp')
demote('Pendant light', 'Billiard pendant')
demote('Pendant light', 'Paper lantern shade')
demote('Chandelier', 'Birdcage chandelier')
demote('Chandelier', 'Genoese beaded chandelier')
demote('Chandelier', 'Wheel chandelier')
demote('Oil & kerosene lamp', 'Victorian parlour lamp')
demote('Oil & kerosene lamp', 'Moroccan pierced brass lantern')
demote('Oil & kerosene lamp', 'Duplex lamp')
demote('Fibre-optic lamp', 'Space-age fibre-optic table lamp')
demote('Safety & miner\'s lamp', 'Carbide lamp')
# maker ranges -> r (versions to models)
demote('EDC flashlight', 'Nitecore EDC series', True)
demote('EDC flashlight', 'Zebralight SC series', True)
demote('EDC flashlight', 'Ledlenser P-series', True)
demote('Thrower', 'Nitecore Tiny Monster', True)
demote('Headlamp', 'Nitecore NU', True)
demote('Headlamp', 'Ledlenser H-series', True)
# tidy r duplicates
for k in kinds.values():
    if k.get('r'):
        seen = []
        for r in k['r']:
            if r not in seen: seen.append(r)
        k['r'] = seen

# ---------- new archetypes ----------
def add_arch(kn, a, pos=None):
    k = kinds[kn]
    a.setdefault('a', ''); a.setdefault('v', [])
    if pos is None: k['x'].append(a)
    else: k['x'].insert(pos, a)
    log['added_arch'].append(a['n'])

add_arch('Table lamp', dict(n='Wagenfeld lamp', a='WG 24 - Bauhaus lamp', d='Glass-and-metal Bauhaus table lamp designed by Wilhelm Wagenfeld with Carl Jakob Jucker; a design classic still in production.',
    mk='', y='1924', s='https://en.wikipedia.org/wiki/Wilhelm_Wagenfeld', dt='glass or metal base - glass shade'), 1)
add_arch('Pendant light', dict(n='PH Artichoke', a='PH Kogle', d='Poul Henningsen\'s glare-free pendant of overlapping copper or steel leaves, first made for the Langelinie Pavilion.',
    mk='Louis Poulsen', y='1958', s='https://en.wikipedia.org/wiki/Poul_Henningsen', dt='finish - diameter'), 1)

# ---------- new kinds ----------
def newkind(n, a, dd, s, x=None):
    k = dict(n=n, a=a, d=dd, s=s)
    if x: k['x'] = x
    kinds[n] = k
    log['added_kinds'].append(n)

newkind('Linear pendant', 'billiard light - island pendant - bar pendant',
        'Long bar or rail with two or more shades hung over a table, island or counter; the billiard light is the classic form.',
        'https://edisonlightglobes.com.au/shop/fittings/billiard-lights')
# source for linear pendant: reuse the one already carried on the demoted billiard archetype
kinds['Linear pendant']['s'] = [a for a in d['depts'][1]['s'][0]['k'][0].get('x', []) if a['n'] == 'Billiard pendant'][0]['s'] if False else kinds['Linear pendant']['s']
newkind('UV & coloured-light torch', 'blacklight torch - UV torch - red torch',
        'Hand torch that shines ultraviolet, red, green or infrared light instead of white, for inspection, night vision or hobby use.', WIKI_FL)
newkind('Railway lantern', 'railroad lantern - signal lantern',
        'Kerosene hand lantern with coloured lenses that trainmen carried to signal; now collected.', WIKI_LA)
newkind('Ship\'s lantern', 'ship lantern - marine lantern',
        'Iron or brass lantern used on ships for navigation and deck light, now collected and used as decoration.', WIKI_LA)
newkind('Deck & step light', 'deck light - stair light - post-cap light',
        'Small low-voltage or solar light fixed on a deck, step edge or post cap to mark the way.', WIKI_LS)

# billiard pendant source: get from backup
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for a in k.get('x', []):
                pass
bp = None
for dp in json.load(open(R + 'work/STR_B3/bak/B3.json'))['depts']:
    for s in dp['s']:
        for k in s['k']:
            for a in k.get('x', []):
                if a['n'] == 'Billiard pendant': bp = a['s']
kinds['Linear pendant']['s'] = bp

# ---------- renames ----------
def rename(old, new):
    k = kinds.pop(old); k['n'] = new; kinds[new] = k
    log['renamed'].append(f'{old} -> {new}')
rename('Light panels', 'Light panel')
rename('Duty & heavy-duty torch', 'Duty torch')

# ---------- definitions updated ----------
D_ = lambda n, t: kinds[n].__setitem__('d', t)
D_('Table lamp', 'Lamp with a base and a shade or head that stands on a table, sideboard or bedside cabinet; a tall one on the floor is a floor lamp.')
D_('Floor lamp', 'Tall lamp that stands on the floor beside furniture, lighting the room directly, upward (torchère) or over a seat.')
D_('Desk lamp', 'Lamp with an adjustable arm, neck or head for task light, standing or clamped on a desk; a monitor-top bar is a light bar.')
D_('Wall light', 'Fitting fixed to a wall that lights a room, a wall or a passage, whatever its source: sconce, swing-arm, reading or picture light.')
D_('Linear pendant', 'Long bar or rail with two or more shades hung over a table, island or counter; the billiard light is the classic form.')
D_('Spot bulb', 'Small directional bulb with pin or twist-lock caps (GU10, MR16), for spot fittings; the reflector bulb has a screw cap and a wider beam.')
D_('Reflector bulb', 'Bulb with a built-in reflector and a screw cap (R, BR, PAR) that throws light forward, for downlights and floodlights.')
D_('Candle lantern', 'Enclosed lantern with a handle that holds a candle, carried or hung; the dark lantern has a shutter and the bull\'s-eye lantern a focusing lens.')
D_('Paper lantern', 'Collapsible or rigid paper-covered lantern lit by a candle or LED and carried as a light; one hung only for decoration is a decorative lantern.')
D_('Electric lantern', 'Carried lantern lit by a battery, rechargeable cell or solar panel; includes the plug-in power-failure light.')
D_('Dive light', 'Watertight light carried or head-mounted by a diver, as a primary, backup or canister light; a camera video light is a camera accessory.')

# ---------- types (tt) ----------
TT = {
 'Table lamp': [['Power source', ['Mains', 'Rechargeable cordless', 'USB']], ['Control', ['Switch', 'Touch dimmer', 'App or voice (smart)']], ['Base material', ['Ceramic', 'Glass', 'Metal', 'Wood', 'Resin', 'Marble or stone']]],
 'Floor lamp': [['Light direction', ['Uplighter', 'Downward reading light', 'Arc over a seat', 'Uplighter with reading arm']], ['Support', ['Single stem', 'Tripod', 'Arc stand', 'Multi-arm']]],
 'Desk lamp': [['Arm mechanism', ['Balanced spring arm', 'Counterweighted arm', 'Gooseneck', 'Fixed or jointed stem']], ['Mounting', ['Weighted base', 'Clamp-on']], ['Light source', ['Integrated LED', 'Bulb (E14 or E27)']], ['Power source', ['Mains', 'USB']]],
 'Monitor light bar': [['Optics', ['Asymmetric beam', 'Symmetric beam']], ['Control', ['Auto-dimming sensor', 'Wireless dial remote', 'Touch buttons']], ['Power source', ['USB', 'Mains adaptor']]],
 'Night light': [['Power source', ['Plug-in', 'Rechargeable portable', 'Battery']], ['Trigger', ['Always on', 'Motion sensor', 'Dusk-to-dawn sensor', 'Sleep-trainer clock']], ['Light pattern', ['Plain glow', 'Star projector']]],
 'Wake-up light': [['Sound', ['None', 'Radio', 'Sleep sounds']], ['Light schedule', ['Sunrise only', 'Sunrise and sunset dimming']], ['Control', ['Buttons', 'App']]],
 'Pendant light': [['Hanging method', ['Cord', 'Chain', 'Rod', 'Plug-in swag', 'Rise-and-fall']], ['Number of lights', ['Single', 'Multi-light cluster']], ['Light source', ['Bulb', 'Integrated LED']]],
 'Linear pendant': [['Number of heads', ['Two', 'Three', 'Four or more']], ['Shade material', ['Metal', 'Glass', 'Fabric']], ['Hanging method', ['Chain', 'Rod']]],
 'Chandelier': [['Material', ['Crystal', 'Glass', 'Brass', 'Wrought iron', 'Glass beads', 'Antler', 'Wood']], ['Frame shape', ['Tiered', 'Birdcage', 'Wheel (corona)', 'Basket or sphere']], ['Light source', ['Candle', 'Bulb', 'Integrated LED']]],
 'Flush ceiling light': [['Distance from ceiling', ['Flush', 'Semi-flush']], ['Diffuser', ['Bowl', 'Drum', 'Dome', 'Flat panel']], ['Light source', ['Bulb', 'Integrated LED', 'Smart LED']]],
 'Ceiling spotlight': [['Number of heads', ['Single', 'Bar', 'Plate']], ['Light source', ['GU10 bulb', 'Integrated LED', 'Smart LED']], ['Head', ['Fixed', 'Swivelling']]],
 'Wall light': [['Arm', ['Fixed', 'Swing-arm']], ['Light direction', ['Up and down', 'Downward only', 'Upward only']], ['Connection', ['Hard-wired', 'Plug-in with cord']]],
 'Mirror light': [['Position', ['Bar above mirror', 'Side lights', 'Clip-on on cabinet']], ['Water protection', ['IP44 bathroom-rated', 'Dry rooms only']]],
 'Salt lamp': [['Shape', ['Natural rough-cut', 'Carved shape', 'Bowl of chunks']], ['Power source', ['Mains', 'Mini USB']]],
 'Plasma lamp': [['Shape', ['Globe', 'Tube', 'Mini night light']]],
 'Fibre-optic lamp': [['Shape', ['Fountain spray', 'Globe', 'Flower', 'Tree']]],
 'Lava lamp': [['Size', ['Mini', 'Standard', 'Large']], ['Light source', ['Incandescent bulb', 'LED']]],
 'Neon light': [['Tube material', ['Glass neon tube', 'LED neon flex']], ['Mounting', ['Wall-mounted on backboard', 'Hanging', 'Free-standing']], ['Power source', ['Mains transformer', 'Battery or USB']]],
 'Light panel': [['Tile shape', ['Triangle', 'Square', 'Hexagon', 'Bar']], ['Control', ['Touch', 'App', 'Music-reactive']]],
 'String light': [['Bulb style', ['Fairy (micro LED)', 'Festoon (globe bulbs)', 'Curtain', 'Icicle', 'Net']], ['Power source', ['Mains', 'Battery', 'Solar', 'USB']], ['Weather rating', ['Indoor only', 'Outdoor rated']]],
 'Decorative lantern': [['Material', ['Metal', 'Glass', 'Paper', 'Stone', 'Wood']], ['Light source', ['Candle', 'Battery LED', 'Mains']], ['Placement', ['Standing', 'Hanging']]],
 'Wall lantern': [['Power source', ['Mains', 'Solar']], ['Sensor', ['Always on', 'Motion sensor', 'Dusk-to-dawn sensor']], ['Light direction', ['Downward only', 'Up and down']]],
 'Floodlight': [['Sensor', ['Motion (PIR) security', 'Dusk-to-dawn', 'Switched only']], ['Power source', ['Mains', 'Solar']], ['Number of heads', ['Single', 'Twin']]],
 'Post light': [['Form', ['Lamp post', 'Post-top lantern']], ['Power source', ['Mains', 'Solar']]],
 'Path light': [['Form', ['Bollard', 'Mushroom', 'Pillar']], ['Power source', ['Mains', 'Low-voltage', 'Solar']]],
 'Spike light': [['Power source', ['Solar', 'Low-voltage plug system', 'Mains']], ['Beam', ['Spot', 'Flood']], ['Control', ['Switched', 'Smart']]],
 'Deck & step light': [['Power source', ['Solar', 'Low-voltage', 'Mains']], ['Fixing', ['Surface-mounted on deck', 'Fixed to step edge', 'Post cap']]],
 'EDC flashlight': [['Cell', ['AA or AAA', '14500, 16340 or 18350', '18650 or 21700', 'Built-in battery']], ['Switch', ['Tail clicky', 'Side e-switch', 'Twist']], ['Body material', ['Aluminium', 'Titanium', 'Copper or brass']], ['Body shape', ['Cylinder', 'Flat']]],
 'Tactical flashlight': [['Mounting', ['Handheld', 'Pistol-mounted', 'Long-gun mounted']], ['Cell', ['CR123A', '18650 or 21700']], ['Switch', ['Two-stage tail switch', 'Momentary tail switch', 'Side switch']]],
 'Thrower': [['Optic', ['Deep reflector', 'TIR lens', 'Laser-excited phosphor']], ['Cell', ['18650', '21700', 'Built-in pack']]],
 'Right-angle flashlight': [['Cell', ['D-cell', '18650', 'AA']], ['Carry', ['Belt clip', 'Headband', 'Magnetic tail']]],
 'Duty torch': [['Cell', ['D or C cell', 'Rechargeable pack', 'AA']], ['Charging', ['Charger holder', 'USB', 'Disposable cells']], ['Hazard rating', ['Standard', 'Intrinsically safe']]],
 'Dive light': [['Role', ['Primary', 'Backup']], ['Battery location', ['In the head', 'Canister on cable']], ['Mounting', ['Handheld', 'Head-mounted']]],
 'Keychain light': [['Cell', ['Button cell', 'AAA or 10440', 'Built-in rechargeable']], ['Light colour', ['White only', 'White plus UV', 'White plus red']]],
 'Penlight': [['Use', ['Medical pupil check', 'Inspection']], ['Cell', ['AAA', 'AAAA', 'Rechargeable']]],
 'Hand searchlight': [['Grip', ['Pistol grip', 'Lantern-style handle']], ['Power source', ['12 V cord', 'Rechargeable pack']]],
 'UV & coloured-light torch': [['Light colour', ['Ultraviolet', 'Red', 'Green', 'Infrared']], ['Cell', ['AAA', '18650 or 21700', 'Built-in battery']]],
 'Headlamp': [['Power source', ['AAA', 'Rechargeable pack', 'Hybrid (rechargeable or AAA)', '18650 or 21700', 'Battery pack on cable']], ['Beam control', ['Fixed', 'Reactive sensor', 'Focusing']], ['Light colour', ['White only', 'White plus red night mode']], ['Weight class', ['Ultralight', 'Standard']]],
 'Clip-on light': [['Clip position', ['Cap brim', 'Pocket or strap', 'Bag']], ['Power source', ['Button cell', 'Rechargeable']]],
 'Hurricane lantern': [['Airflow', ['Dead-flame', 'Hot-blast (tubular)', 'Cold-blast (tubular)']]],
 'Oil & kerosene lamp': [['Burner', ['Flat wick', 'Central draught (round wick)', 'Side draught', 'Duplex (two wicks)', 'Mantle']], ['Mounting', ['Table', 'Hanging', 'Wall bracket']], ['Condition', ['Original burner', 'Electrified antique']]],
 'Railway lantern': [['Fuel', ['Kerosene', 'Carbide', 'Electric']], ['Lens', ['Clear', 'Red', 'Green']]],
 'Ship\'s lantern': [['Material', ['Iron', 'Brass', 'Copper']], ['Fuel', ['Oil', 'Candle', 'Electric']]],
 'Candle lantern': [['Light control', ['Open', 'Shuttered (dark lantern)', 'Bull\'s-eye lens']], ['Body', ['Collapsible', 'Rigid']]],
 'Paper lantern': [['Frame', ['Collapsible spiral', 'Folding ribs', 'Rigid']], ['Light source', ['Candle', 'Battery LED insert']]],
 'Gas & pressure lantern': [['Fuel', ['Kerosene (paraffin)', 'White gas (Coleman fuel)', 'Dual fuel', 'Propane', 'Gas cartridge']], ['Mantles', ['Single mantle', 'Double mantle']]],
 'Safety & miner\'s lamp': [['Fuel', ['Oil', 'Carbide', 'Candle']], ['Flame guard', ['Wire gauze', 'Glass and gauze']]],
 'Electric lantern': [['Power source', ['Disposable battery', 'Rechargeable', 'Solar', 'Hand-crank', 'Power-bank output']], ['Light source', ['LED', 'Fluorescent']], ['Build', ['Rigid', 'Collapsible', 'Inflatable']]],
 'Work light': [['Mounting', ['Clamp', 'Hook or magnet', 'Tripod', 'Handheld']], ['Power source', ['Corded', 'Cordless battery']], ['Light source', ['LED', 'Halogen']]],
 'Standard bulb': [['Cap', ['E27 screw', 'E26 screw', 'B22 bayonet']], ['Filament', ['Hidden', 'Visible filament']], ['Control', ['Plain', 'Smart (Zigbee, Matter or Wi-Fi)']], ['Dimming', ['Non-dimmable', 'Dimmable']]],
 'Candle bulb': [['Cap', ['E14 screw', 'E12 screw', 'B15 bayonet']], ['Tip', ['Plain', 'Flame tip']], ['Filament', ['Hidden', 'Visible filament']]],
 'Globe bulb': [['Diameter', ['G25', 'G95', 'G125']], ['Filament', ['Hidden', 'Visible filament']], ['Control', ['Plain', 'Smart']]],
 'Spot bulb': [['Cap', ['GU10', 'GU5.3']], ['Shape', ['MR16', 'PAR16']], ['Control', ['Plain', 'Smart']]],
 'Reflector bulb': [['Reflector type', ['R (blown glass)', 'BR (bulged reflector)', 'PAR (pressed glass)']], ['Cap', ['E27', 'E14']]],
 'Capsule bulb': [['Cap', ['G4', 'G9']], ['Voltage', ['12 V', '230 V']]],
 'Tube light': [['Tube size', ['T5', 'T8']], ['Technology', ['Fluorescent', 'LED retrofit', 'Compact fluorescent']]],
 'Strip light': [['Colour range', ['Single white', 'Tunable white', 'Colour (RGB)']], ['Chip style', ['Dotted LEDs', 'COB (continuous)']], ['Build', ['Flat tape', 'Rope light', 'Neon flex']], ['Control', ['Remote', 'Smart']]],
 'Lamp shade': [['Shape', ['Drum', 'Empire', 'Bell', 'Coolie', 'Square']], ['Material', ['Fabric', 'Paper', 'Glass', 'Parchment']], ['Fitter', ['Spider', 'Uno', 'Clip-on', 'Pendant ring']]],
 'Lamp base': [['Lamp it carries', ['Table lamp', 'Floor lamp']], ['Material', ['Ceramic', 'Glass', 'Metal', 'Wood', 'Bronze']]],
 'Lamp spare parts': [['Part', ['Cord set', 'Pendant cord set', 'Lamp holder', 'Harp and finial', 'Chandelier crystals', 'Glass diffuser']]],
}
for n, k in kinds.items():
    assert n in TT, n
    k['tt'] = TT[n]; k.pop('t', None)
assert set(TT) == set(kinds), set(TT) ^ set(kinds)

# ---------- generic wording fixes for tt that kept types of chandelier forms ----------
# ---------- SEE links ----------
SEE = {
 'Tactical flashlight': [['E4', 'Weapon light', 'rail-mounted gun light']],
 'Wake-up light': [['H2', 'Light-therapy lamp', 'bright-light therapy lamp']],
 'Ceiling spotlight': [['G3', 'Track lighting', 'built-in track'], ['B3', 'Spot bulb', 'the bulb it takes']],
 'Spot bulb': [['B3', 'Ceiling spotlight', 'the fitting it fits']],
 'Flush ceiling light': [['G3', 'Recessed downlight', 'sunk into the ceiling']],
 'Strip light': [['G3', 'Under-cabinet light', 'built-in cabinet light']],
 'Deck & step light': [['G3', 'Step & plinth light', 'recessed built-in step light']],
 'Neon light': [['F2', 'Neon sculpture', 'neon as art']],
 'Oil & kerosene lamp': [['F4', 'Oil lamp for worship', 'ritual oil lamp']],
 'Decorative lantern': [['F4', 'Ramadan lantern', 'festive lantern'], ['B3', 'Paper lantern', 'carried paper lantern']],
 'Candle lantern': [['B4', 'Candle holder', 'holder for candles']],
 'Paper lantern': [['B3', 'Decorative lantern', 'hung for decoration only']],
 'Wall lantern': [['B3', 'Decorative lantern', 'indoor or stand-alone lantern']],
 'Right-angle flashlight': [['B3', 'Headlamp', 'worn on the head']],
 'Work light': [['B3', 'Floodlight', 'fixed outdoor flood']],
 'Floodlight': [['B3', 'Work light', 'portable job light']],
 'Standard bulb': [['G3', 'Lighting control system', 'smart-home control']],
}
for n, v in SEE.items(): kinds[n]['see'] = v

# ---------- structure ----------
def sh(n, t, kn, ax=None):
    s = dict(n=n, t=t, k=[kinds[x] for x in kn])
    if ax: s['ax'] = ax
    return s

old = {dp['n']: dp for dp in d['depts']}
def dept(n, t, ax, shelves):
    o = old[n]
    return dict(n=n, mode=o['mode'], **({'note': o['note']} if o.get('note') else {}),
                b=o.get('b', []), t=t, ax=ax, s=shelves)

depts = [
 dept('Lamps', 'Lights that stand on furniture or the floor and plug in or run from a battery; one hung from the ceiling → Ceiling lights, fixed to a wall → Wall lights, carried → Torches & lanterns.',
      'What is the lamp for: lighting the room, lighting a task at a desk, or giving dim light for sleep?',
      [sh('Table & floor lamps', 'Lamps for general room light that stand on furniture or the floor, such as the Tiffany lamp, Arco or Akari; a lamp with an adjustable arm for tasks → Desk & task lamps.', ['Table lamp', 'Floor lamp']),
       sh('Desk & task lamps', 'Lamps built to light work at a desk, such as the Anglepoise or Tizio, or a monitor light bar; a decorative table lamp → Table & floor lamps.', ['Desk lamp', 'Monitor light bar']),
       sh('Night lights & wake-up lights', 'Dim lights for the bedroom that stay on at night or brighten to wake you; a bright-light therapy lamp → H2.', ['Night light', 'Wake-up light'])]),
 dept('Ceiling lights', 'Fittings that hang from or fix to the ceiling; sunk-in downlights and track → G3, a ceiling fan → B7.',
      'How does it meet the ceiling: hung on a single cord or rod, branched on arms, or fixed against it?',
      [sh('Pendants', 'Fittings hung from one or more cords, chains or rods with the light below the ceiling, such as the PH lamp, Bubble lamp or a billiard light; a branched fitting → Chandeliers.', ['Pendant light', 'Linear pendant']),
       sh('Chandeliers', 'Branched or tiered hanging fittings that carry several light sources, such as the Maria Theresa, Murano or Sputnik; a single-shade hanging light → Pendants.', ['Chandelier']),
       sh('Fitted ceiling lights', 'Fittings fixed against the ceiling, such as a flush bowl or a swivelling spotlight; sunk-in downlights → G3.', ['Flush ceiling light', 'Ceiling spotlight'])]),
 dept('Wall lights', 'Fittings fixed to an interior wall, from design sconces to bathroom mirror lights; an outdoor wall fitting → Outdoor lights, a built-in under-cabinet light → G3.',
      'What is the wall light for: lighting a room or wall, or lighting the face at a mirror?',
      [sh('Room wall lights', 'Wall sconces and swing-arm lights that light a room, passage, bed or picture, such as the Serge Mouille wall lights or the PH wall.', ['Wall light']),
       sh('Mirror & bathroom lights', 'Wall lights made for the face at a mirror and rated for bathrooms; a lit mirror itself is not a lamp.', ['Mirror light'])]),
 dept('Decorative lighting', 'Lights owned for mood or novelty rather than to see by, such as lava lamps, neon signs and fairy lights; a lamp for light first → Lamps.',
      'What does the decoration do: glow as an object you stand, or hang and fix as a pattern on a wall, tree or room?',
      [sh('Novelty lamps', 'Free-standing glowing objects made to be watched, such as the lava lamp, plasma globe, fibre-optic lamp or salt lamp.', ['Lava lamp', 'Plasma lamp', 'Fibre-optic lamp', 'Salt lamp'], 'kinds by what glows: wax, gas, fibres, rock salt'),
       sh('Wall & hanging lights', 'Decorative lights fixed, draped or hung rather than stood, such as neon signs, Nanoleaf panels, fairy lights and lanterns for show.', ['Neon light', 'Light panel', 'String light', 'Decorative lantern'], 'kinds by how it is fixed: wall tubes, wall tiles, draped string, hung or stood lantern')]),
 dept('Outdoor lights', 'Fixed or stood lights for gardens, drives and house walls; a carried light → Torches & lanterns, built-in landscape lighting → G3.',
      'Where is it fixed: on a wall or post, or on the ground and in the soil?',
      [sh('Wall, post & flood lights', 'Outdoor lights fixed high on walls, posts or brackets, such as a wall lantern, lamp post or security floodlight.', ['Wall lantern', 'Post light', 'Floodlight'], 'kinds by height and spread: wall bracket, tall post, wide flood'),
       sh('Ground & garden lights', 'Low outdoor lights that stand on the ground, push into soil or mark a deck or step, such as bollards and solar spikes.', ['Path light', 'Spike light', 'Deck & step light'], 'kinds by how it is fixed: standing, pushed into soil, fixed on deck or step')]),
 dept('Torches & lanterns', 'Lights carried, worn or set down where needed: torches, headlamps, lanterns and work lights; a fixed outdoor fitting → Outdoor lights, a decorative lantern → Decorative lighting.',
      'How is it carried or worn, and what makes the light: a held battery beam, a worn light, a flame or a battery area light?',
      [sh('Handheld torches', 'Battery torches held in the hand, such as the Maglite, SureFire 6P or pocket EDC light; a head-worn light → Worn lights.', ['Keychain light', 'Penlight', 'EDC flashlight', 'Tactical flashlight', 'Duty torch', 'Thrower', 'Hand searchlight', 'Right-angle flashlight', 'Dive light', 'UV & coloured-light torch'], 'kinds by the job: pocket carry, defence or duty, long throw, wide search, underwater, special light'),
       sh('Worn lights', 'Lights worn on the head or clipped to clothing to leave both hands free, such as the Petzl Tikka.', ['Headlamp', 'Clip-on light']),
       sh('Flame lanterns & lamps', 'Carried or hung lanterns and lamps that burn oil, gas, candle or carbide, such as the Dietz hurricane lantern or Coleman; an electric lantern → Battery lanterns & work lights.', ['Hurricane lantern', 'Oil & kerosene lamp', 'Railway lantern', 'Ship\'s lantern', 'Candle lantern', 'Paper lantern', 'Gas & pressure lantern', 'Safety & miner\'s lamp'], 'kinds by fuel and burner: wick oil, candle, pressurised mantle, guarded flame'),
       sh('Battery lanterns & work lights', 'Battery or solar lights that light an area rather than throw a beam, such as camping lanterns and clamp or tripod work lights.', ['Electric lantern', 'Work light'])]),
 dept('Bulbs & strips', 'Replaceable light sources that go in or on a fitting: bulbs, tubes and LED strips; the fitting itself → Lamps, Ceiling lights or Wall lights.',
      'What shape is the light source: a bulb with a cap, a rigid tube or a flexible strip?',
      [sh('Bulbs', 'Bulbs with a cap that fit a lamp holder, such as the standard A-shape, candle, globe or GU10 spot; a rigid tube → Tubes & strips.', ['Standard bulb', 'Candle bulb', 'Globe bulb', 'Reflector bulb', 'Spot bulb', 'Capsule bulb'], 'kinds by bulb shape and cap: pear, candle, globe, reflector, spot, pin capsule'),
       sh('Tubes & strips', 'Long light sources: rigid fluorescent or LED tubes and flexible LED strips and rope lights.', ['Tube light', 'Strip light'])]),
 dept('Shades & lamp parts', 'Shades, bases and replacement parts sold on their own for lamps people already own; a whole lamp → Lamps.',
      'Which part of the lamp is it: the cover for the light, the stand that holds it, or the wiring and fittings?',
      [sh('Shades & lamp parts', 'Shades, bases and replacement cords, holders and crystals, sold to repair or restyle a lamp.', ['Lamp shade', 'Lamp base', 'Lamp spare parts'])]),
]
used = [k['n'] for dp in depts for s in dp['s'] for k in s['k']]
assert sorted(used) == sorted(kinds), set(kinds) ^ set(used)
# for chandelier tt: Tiered etc kept; unused demoted

d['depts'] = depts
d['lead'] = ('Lights a person owns for home, garden and outdoors, organised by where the light sits or how it is carried: lamps, ceiling and wall lights, '
             'decorative lights, outdoor lights, torches and lanterns (an enthusiast hobby), and the bulbs, shades and parts that serve them.')
d['ax'] = 'Where does the light sit and how is it used: stood on furniture, hung from the ceiling, fixed to a wall, owned for mood, fixed outdoors, carried, or a bulb or part for another light?'
d['key'] = [
 '1. Is it a bulb, tube or LED strip that goes in or on a fitting? → Bulbs & strips',
 '2. Is it a shade, lamp base or replacement part sold on its own? → Shades & lamp parts',
 '3. Is it carried, worn or set down where needed (torch, headlamp, lantern, work light)? → Torches & lanterns',
 '4. Is it fixed or stood outdoors (garden, drive, house wall)? → Outdoor lights',
 '5. Is it owned for mood or novelty rather than to see by (lava lamp, neon sign, fairy lights)? → Decorative lighting',
 '6. Does it hang from or fix to the ceiling? → Ceiling lights',
 '7. Is it fixed to an interior wall? → Wall lights',
 '8. Does it stand on furniture or the floor, or give dim light for sleep? → Lamps',
 '<i>Precedence: a lantern carried by hand is a torch or lantern (step 3) before a decorative lantern (step 5); a wall lantern for outdoors is an outdoor light (step 4) before a wall light (step 7); sunk-in downlights, track and under-cabinet lights are built in → G3.</i>']

tmp = R + 'out/B3.json.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, R + 'out/B3.json')
after = dict(depts=len(depts), shelves=sum(len(dp['s']) for dp in depts), kinds=len(kinds),
             arch=sum(len(k.get('x', [])) for k in kinds.values()))
print(before, after); print(json.dumps(log, indent=1))
