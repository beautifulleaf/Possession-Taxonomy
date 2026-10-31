import json, os, sys, shutil, copy, re
R = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(R + 'work/STR_B4/bak/B4.json'))
W = 'https://en.wikipedia.org/wiki/'
S_VASE, S_GARD, S_CAND, S_INC = W+'Vase', W+'Garden_ornament', W+'Candle', W+'Incense'
S_XMAS, S_FW, S_PW, S_AF = W+'Christmas_decoration', W+'Fireworks', W+'Paperweight', W+'Air_freshener'
S_FRAME, S_FLAG, S_ART, S_POP = W+'Picture_frame', W+'Flag', W+'Artificial_flower', W+'Party_popper'

okinds = {}
oarch = {}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']:
            okinds[k['n']] = k
            for x in k.get('x', []):
                oarch[x['n']] = x
used_arch = set()
used_kinds = set()

def K(n, frm=None, d=None, a=None, tt=None, x=(), see=(), s=None, r_add=(), tg=None, xnew=()):
    base = okinds.get(frm or n)
    k = {'n': n}
    if base:
        used_kinds.add(base['n'])
        k['a'] = base.get('a', '')
        k['d'] = base['d']
        k['s'] = base.get('s', '')
        for key in ('m', 'r'):
            if base.get(key):
                k[key] = copy.deepcopy(base[key])
        if base.get('tg'):
            k['tg'] = base['tg']
    if a is not None: k['a'] = a
    if d: k['d'] = d
    if s: k['s'] = s
    if tg: k['tg'] = tg
    k.setdefault('a', '')
    xs = []
    for nm in x:
        if isinstance(nm, tuple):
            src, newn = nm
            xo = copy.deepcopy(oarch[src]); xo['n'] = newn; used_arch.add(src)
        else:
            xo = copy.deepcopy(oarch[nm]); used_arch.add(nm)
        xs.append(xo)
    xs += list(xnew)
    if xs: k['x'] = xs
    if r_add:
        k.setdefault('r', [])
        k['r'] += [list(r) for r in r_add]
    k['tt'] = [[g, v] for g, v in tt]
    if see: k['see'] = [list(v) for v in see]
    return k

def SH(n, t, ax, ks):
    sh = {'n': n, 't': t}
    if ax: sh['ax'] = ax
    sh['k'] = ks
    return sh

def odept(name):
    return [d for d in old['depts'] if d['n'] == name][0]

def D(name, t, ax, shelves):
    o = odept(name)
    d = {'n': name, 'mode': o['mode']}
    for key in ('note', 'b', 's'):
        if o.get(key): d[key] = o[key]
    d['t'] = t; d['ax'] = ax; d['s'] = shelves if False else None
    return d, shelves

depts = []
def add(name, t, ax, shelves):
    o = odept(name)
    d = {'n': name, 'mode': o['mode']}
    if o.get('note'): d['note'] = o['note']
    if o.get('b'): d['b'] = o['b']
    d['t'] = t; d['ax'] = ax; d['s'] = shelves
    if o.get('s'): d['src'] = o['s']
    depts.append(d)

# ---------------------------------------------------------------- 1 VASES
add('Vases & decorative glass and ceramics',
    'Vessels and glass pieces kept to hold flowers or to be looked at; a vessel for food or drink → Kitchen & Dining; a garden planter → Garden & Grounds.',
    'What shape of display piece is it: an open vase, a lidded jar or bottle, a bowl or urn, or a solid glass ornament?',
    [
     SH('Vases', 'Open-mouthed vessels made to hold cut flowers or to stand as an ornament; a lidded jar or stoppered bottle → Jars & bottles; art glass signed by a studio artist → F2.',
        'kinds by what the vase is made of: glass, porcelain, earthenware or stoneware, metal',
        [K('Glass vase', frm='Vase', a='crystal vase · art glass vase · flower vase',
           d='Vase blown, cast or pressed from glass or lead crystal, from everyday tumblers to art glass.',
           x=['Aalto vase', 'Fazzoletto', 'Bacchantes', 'Graal vase', 'Ariel vase', 'Banjo vase', 'Hobnail vase'],
           r_add=[['Coloured crystal vases', 'Moser'], ['Textured range', 'Whitefriars Glass'], ['Carnaby series', 'Holmegaard Glasværk'], ['Designer vases (Winslow Anderson era)', 'Blenko Glass Company']],
           tt=[['Shape', ['Bud vase', 'Table vase', 'Floor vase', 'Cylinder', 'Bottle', 'Tulip']],
               ['Glass type', ['Clear', 'Coloured', 'Cased (overlay)', 'Iridescent', 'Lead crystal']],
               ['Decoration', ['Plain', 'Wheel-cut', 'Engraved (Bohemian)', 'Moulded', 'Hand-painted']]],
           see=[('F2', 'Art glass', 'studio and art-glass houses'), ('F2', 'Studio glass', 'signed studio pieces')],
           s=S_VASE),
         K('Porcelain vase', frm='Vase', a='porcelain vase · china vase',
           d='Vase of fine white fired porcelain, hard-paste or soft-paste, plain or painted.',
           x=['Snowball vase', 'Meiping'],
           tt=[['Shape', ['Bud vase', 'Table vase', 'Floor vase', 'Gourd', 'Bottle', 'Urn-shaped']],
               ['Paste', ['Hard-paste', 'Soft-paste', 'Bone china']],
               ['Decoration', ['Plain white', 'Underglaze blue', 'Overglaze enamel', 'Applied relief', 'Gilt']]],
           see=[('F2', 'Art pottery', 'collected ceramics by house')], s=S_VASE),
         K('Earthenware & stoneware vase', frm='Vase', a='pottery vase · ceramic vase · delftware vase',
           d='Vase of fired clay other than porcelain, glazed or unglazed, from tin-glazed delftware to studio-style stoneware.',
           x=['Delft tulip vase', 'Portland vase', 'Rimini Blu vase'],
           tt=[['Shape', ['Bud vase', 'Table vase', 'Floor vase', 'Wall vase (flat-backed)', 'Tulip (tiered spouts)', 'Pitcher']],
               ['Clay body', ['Earthenware', 'Stoneware', 'Jasperware', 'Fritware']],
               ['Glaze or finish', ['Tin glaze (delftware)', 'Glossy glaze', 'Matt glaze', 'Mid-century West German glazes', 'Iznik-style underglaze floral', 'Unglazed']]],
           see=[('F2', 'Art pottery', 'collected ceramics by house'), ('F2', 'Studio pottery', 'signed studio pieces')], s=S_VASE),
         K('Metal vase', frm='Vase', a='brass vase · bronze vase · cloisonné vase',
           d='Vase of brass, bronze, copper, steel or aluminium, including enamelled cloisonné.',
           tt=[['Shape', ['Bud vase', 'Table vase', 'Floor vase', 'Cylinder', 'Urn-shaped']],
               ['Metal', ['Brass', 'Bronze', 'Copper', 'Stainless steel', 'Aluminium']],
               ['Surface', ['Polished', 'Patinated', 'Hammered', 'Cloisonné enamel']]], s=S_VASE),
        ]),
     SH('Jars & bottles', 'Lidded jars and stoppered bottles made to stand on display; a jar made to store food → Kitchen & Dining; a scent bottle → Fragrance.',
        'kinds by what the container was first made to hold: ginger or tea, drugs, drink or snuff',
        [K('Ginger jar', x=['Blue-and-white prunus ginger jar'],
           tt=[['Decoration', ['Blue-and-white', 'Coloured glaze', 'Famille rose', 'Plain']], ['Lid', ['With lid', 'Without lid', 'Wooden lid']], ['Material', ['Porcelain', 'Earthenware']]]),
         K('Apothecary jar', x=['Albarello'],
           tt=[['Material', ['Glass', 'Ceramic']], ['Foot', ['Footed', 'Flat-based']], ['Lid', ['Glass lid', 'Cork stopper', 'Ceramic lid']]],
           see=[('B5', 'Preserving jar', 'a jar for storing food')]),
         K('Decorative bottle', x=['Snuff bottle', 'Venini stoppered bottle'],
           tt=[['Material', ['Glass', 'Ceramic', 'Porcelain']], ['Closure', ['With stopper', 'Open neck', 'Cork']], ['Form', ['Flask', 'Carafe-shaped', 'Gourd']]],
           see=[('H4', 'Czech crystal perfume bottle', 'a bottle made to hold scent')]),
        ]),
     SH('Bowls & urns', 'Bowls and footed vessels made to be looked at; a bowl made to hold food → Kitchen & Dining; a cremation urn → Religious & Ceremonial Objects.',
        'kinds by whether the vessel is an open bowl or a footed urn',
        [K('Decorative bowl', x=[('Carnival glass bowl', 'Carnival glass'), ('Depression glass bowl', 'Depression glass'), 'Provence bowl'],
           tt=[['Material', ['Art glass', 'Ceramic', 'Wood', 'Metal']], ['Foot', ['Footed', 'Flat-based', 'Pedestal']], ['Use', ['Centrepiece', 'Potpourri bowl', 'Display only']]],
           see=[('B5', 'Serving bowl', 'a bowl made to serve food')]),
         K('Decorative urn', x=['Medici vase', 'Borghese vase'],
           tt=[['Material', ['Stone', 'Cast stone', 'Metal', 'Ceramic']], ['Setting', ['Indoor', 'Garden']], ['Handles', ['Two-handled', 'Handleless']]],
           see=[('F4', 'Cremation urn', 'an urn made for ashes')]),
        ]),
     SH('Glass paperweights', 'Solid glass domes enclosing decoration, kept on a desk or shelf; a scholar\'s weight for a writing table → Pens, Ink & Calligraphy.',
        None,
        [K('Glass paperweight', x=['Crown paperweight'],
           xnew=[{'n': 'Millville rose', 'a': '', 'd': 'Crimped glass flower, usually a rose, set in a weight; the form originated in Millville, New Jersey.', 'mk': '', 'y': '', 's': S_PW, 'v': []}],
           tt=[['Enclosed decoration', ['Millefiori canes', 'Lampwork flower or fruit', 'Sulphide cameo', 'Swirl', 'Marbrie', 'Portrait or advertising']],
               ['Size', ['Miniature (under 5 cm)', 'Standard', 'Magnum (over 8 cm)']],
               ['Base', ['Domed', 'Footed', 'Faceted']]],
           see=[('C5', "Scholar's paperweight", 'a weight for a writing table'), ('B4', 'Snow globe', 'water-filled globes began as paperweights')],
           s=S_PW)]),
    ])
used_arch |= {'Overmantel mirror', 'Millefiori paperweight', 'Lampwork paperweight', 'Sulphide paperweight', 'Bohemian cut-glass vase', 'West German pottery vase', 'Iznik-style vessel', 'Moser coloured crystal vase', 'Textured range', 'Carnaby series', 'Blenko designer vase'}
used_kinds.add('Vase')

# ---------------------------------------------------------------- 2 MIRRORS
add('Mirrors & wall decor',
    'Mirrors, frames and wall pieces hung or stood in a room for effect; a picture or print → Art; a clock → Watches & Clocks; a wall shelf → Furniture; a grooming mirror → Personal Care & Beauty.',
    'Does the piece reflect, frame a picture, or fill a wall as ornament?',
    [
     SH('Mirrors', 'Glass mirrors made to hang, lean or stand in a room; a mirror for grooming → Personal Care & Beauty; a mirror with a light → Lighting.',
        'kinds by where the mirror hangs or stands: on the wall, on the floor, on a table',
        [K('Wall mirror', x=['Sunburst mirror', 'Venetian mirror', 'Girandole mirror', 'Adnet Circulaire'],
           tt=[['Shape', ['Round', 'Oval', 'Rectangular', 'Arched', 'Convex']], ['Frame', ['Frameless', 'Gilt wood', 'Metal', 'Wood', 'Leather-wrapped']], ['Placement', ['Overmantel', 'Over console or hall table', 'Full-length wall-hung']]],
           see=[('B3', 'Mirror light', 'a mirror with a built-in light')], s=W+'Mirror'),
         K('Floor mirror', x=['Ultrafragola', 'Cheval mirror'],
           tt=[['Support', ['Leaner', 'Cheval (on stand)', 'Free-standing frame']], ['Frame', ['Frameless', 'Wood', 'Metal', 'Arched']]]),
         K('Table mirror',
           tt=[['Support', ['Swing (cheval) toilet mirror', 'Fixed stand']], ['Storage', ['Plain', 'With drawers', 'Jewellery box']]],
           see=[('H1', 'Grooming mirror', 'a mirror made for personal care')]),
        ]),
     SH('Frames & wall pieces', 'Frames and fixed ornaments that decorate a wall; a framed print sold as art → Art.',
        'kinds by what goes on the wall: a framed picture, a carved or moulded panel, an adhesive motif',
        [K('Picture frame',
           tt=[['Shape', ['Rectangular', 'Square', 'Round', 'Oval']], ['Moulding', ['Carved', 'Mitred strips on a panel', 'Scoop']], ['Layout', ['Single aperture', 'Multi-aperture', 'Box frame', 'Clip frame']], ['Display', ['Tabletop', 'Wall-hung']]],
           see=[('F2', 'Canvas and framed art print', 'a print sold already framed')], s=S_FRAME),
         K('Decorative wall panel', tt=[['Material', ['Carved wood', 'Metal', 'Plaster', 'Resin']], ['Making', ['Carved', 'Fretwork', 'Moulded']]]),
         K('Wall sticker', tt=[['Content', ['Motif', 'Lettering', 'Pattern']], ['Surface', ['Wall', 'Window film', 'Furniture']]]),
        ]),
    ])

# ---------------------------------------------------------------- 3 CANDLES
INC_BURN = ('F4', 'Incense burner', 'burner made for rites')
add('Candles & home fragrance',
    'Things burned, heated or sprayed to light or scent a room; a candle or incense for rites → Religious & Ceremonial Objects; a lantern or lamp → Lighting; a perfume to wear → Fragrance.',
    'Does the light or scent come from burning wax, from a flame-free diffuser or spray, or from smouldering incense?',
    [
     SH('Candles & holders', 'Wax candles, flame-free imitations and the holders and tools used with them; a candle for a rite → F4.',
        'kinds from the candle to what holds or tends it: container, free-standing, flameless, holder, snuffer, trimmer',
        [K('Container candle', x=['Baies', 'Feu de Bois', 'Ernesto', 'Abd El Kader', 'Santal 26', 'Original Jar', 'Baltic Amber', 'Real Luxury'],
           r_add=[['3-Wick Candle', 'Bath & Body Works']],
           tt=[['Wicks', ['Single-wick', 'Three-wick']], ['Vessel', ['Glass jar', 'Tin', 'Ceramic or stone']], ['Wax', ['Paraffin', 'Beeswax', 'Blended']]],
           see=[('F4', 'Ritual candle', 'candle burned for rites')], s=S_CAND),
         K('Free-standing candle', a='pillar candle · taper · tealight · votive · floating candle',
           tt=[['Shape', ['Pillar', 'Taper (dinner candle)', 'Tealight', 'Votive', 'Floating']], ['Wax', ['Paraffin', 'Beeswax', 'Stearin', 'Tallow']], ['Scent', ['Scented', 'Unscented']], ['Burn', ['Dripless', 'Standard']]],
           see=[('F4', 'Ritual candle', 'candle burned for rites')], s=S_CAND),
         K('Flameless candle', tt=[['Body', ['Wax-bodied', 'Plastic-bodied']], ['Light', ['Flame-effect bulb', 'Flickering LED']], ['Control', ['Remote', 'Timer', 'Switch only']], ['Setting', ['Indoor', 'Outdoor']]]),
         K('Candle holder', x=['Nagel candleholder', 'Kubus'],
           tt=[['Form', ['Candlestick', 'Chamberstick', 'Candelabrum', 'Sconce', 'Girandole', 'Tealight holder', 'Votive holder', 'Pillar holder']], ['Material', ['Metal', 'Glass', 'Ceramic', 'Wood']]],
           see=[('B3', 'Candle lantern', 'an enclosed holder'), ('B3', 'Hurricane lantern', 'a glass shield round the flame'), ('F4', 'Altar candlestick', 'holder made for rites')], s=S_CAND),
         K('Candle snuffer', tt=[['Form', ['Bell snuffer', 'Scissor snuffer']], ['Handle', ['Long handle', 'Short handle']]], s=S_CAND),
         K('Wick trimmer', d='Scissor-like tool that trims a candle wick so the flame burns cleanly.', a='wick cutter',
           tt=[['Form', ['Scissor trimmer', 'Wick dipper']], ['Finish', ['Steel', 'Brass', 'Gilt']]], s=S_CAND),
        ]),
     SH('Diffusers, melts & sprays', 'Flame-free ways to scent a room by evaporation, heat, power or spray; a candle that scents as it burns → Candles & holders.',
        'kinds by how the scent is released: left to evaporate, heated, powered, sprayed',
        [K('Reed diffuser', tt=[['Vessel', ['Glass', 'Ceramic']], ['Reeds', ['Rattan', 'Fibre']], ['Supply', ['Refillable set', 'Sealed']]], s=S_AF),
         K('Potpourri & scented sachet', tt=[['Form', ['Loose potpourri', 'Drawer sachet', 'Lavender bag']]], s=S_AF),
         K('Scented beads & gel', d='Fragrance-loaded beads or gel that release scent as they evaporate, kept in a jar or dish.', a='fragrance beads · air freshener gel',
           tt=[['Form', ['Beads', 'Gel']], ['Container', ['Jar', 'Dish', 'Pouch']]], s=S_AF),
         K('Wax melt', tt=[['Shape', ['Clamshell', 'Bar', 'Cube']]], see=[('B4', 'Wax warmer', 'needed to melt it')]),
         K('Wax warmer', tt=[['Heat source', ['Electric hotplate', 'Bulb', 'Tealight', 'Plug-in']]]),
         K('Catalytic fragrance lamp', x=['Lampe Berger'], tt=[['Body', ['Crystal or glass', 'Porcelain or ceramic']], ['Edition', ['Standard', 'Designer']]]),
         K('Electric diffuser', x=['Ultrasonic aroma diffuser (MUJI)', 'Hourglass diffuser'],
           tt=[['Mechanism', ['Ultrasonic (water mist)', 'Nebulising (pure oil, no water)', 'Heated plug-in oil', 'Timed aerosol spray', 'Fan']], ['Power', ['Mains', 'Battery', 'USB']]], s=S_AF),
         K('Room spray', tt=[['Delivery', ['Aerosol', 'Pump spray']], ['Purpose', ['Scenting', 'Odour-neutralising']]], s=S_AF),
         K('Diffuser oil', tt=[['Oil', ['Essential oil', 'Fragrance oil']], ['Fits', ['Reed diffuser', 'Plug-in unit', 'Catalytic lamp', 'Ultrasonic diffuser']]]),
        ]),
     SH('Incense', 'Scented material burned directly or on heat to perfume a room; an incense for rites → F4.',
        'kinds by form, from direct-burning shapes to material heated on charcoal: stick, cone, coil, rope, loose, paste, bundle',
        [K('Stick incense', frm='Stick and cone incense', a='joss stick · senkō · agarbatti · cored stick · dhoop stick',
           d='Self-burning incense shaped as a stick, with a bamboo core or solid, lit and left to smoulder.',
           x=['Mainichi-Koh', 'Kobunboku', 'Reiryokoh', 'Nag champa'],
           r_add=[['Daily Incense', 'Shoyeido'], ['Premium Incense', 'Shoyeido'], ['Traditional Series', 'Nippon Kodo'], ['Seiun', 'Nippon Kodo'], ['Morning Star', 'Nippon Kodo']],
           tt=[['Core', ['Bamboo-core', 'Coreless (dhoop)']], ['Making', ['Masala (rolled in paste)', 'Dipped', 'Pressed']], ['Length', ['Short', 'Long']], ['Smoke', ['Standard', 'Low-smoke']]],
           see=[('F4', 'Ritual incense', 'incense burned for rites')], s=S_INC),
         K('Cone incense', frm='Stick and cone incense', d='Self-burning incense shaped as a cone, which burns faster than a stick; backflow cones make smoke pour downward.', a='incense cone',
           tt=[['Smoke path', ['Standard', 'Backflow']], ['Size', ['Small', 'Large']]], s=S_INC),
         K('Coil incense', tt=[['Size', ['Small coil', 'Large hanging coil']], ['Use', ['Indoor', 'Temple', 'Insect-repelling']]], s=S_INC),
         K('Incense rope & paper', d='Twisted incense rope used in Tibet and Nepal, and resin-infused paper strips folded or torn and burned.', a='rope incense · Carta d\'Armenia',
           tt=[['Form', ['Rope', 'Paper']]], s=S_INC),
         K('Loose incense', x=['Oud chips', 'Kyara and jinkō pieces', 'Gozan-kōh', 'Tibetan incense'],
           d='Unmixed wood chips, resin or powder heated on charcoal or a heater to scent a room (incense for religious rites is in Religious & Ceremonial Objects).',
           tt=[['Material', ['Wood chips', 'Resin', 'Powder', 'Granules']], ['Heat', ['Charcoal', 'Electric heater', 'Mica plate']]],
           see=[('F4', 'Ritual incense', 'incense burned for rites')], s=S_INC),
         K('Paste incense', d='Binder-mixed pastilles, chips or balls of scented material, heated rather than lit, such as Arabian bakhoor and Japanese nerikō.', a='bakhoor · nerikō · pastille',
           x=['Bakhoor'], tt=[['Form', ['Chips', 'Pastilles', 'Balls']], ['Tradition', ['Arabian bakhoor', 'Japanese nerikō']]], s=S_INC),
         K('Smudge bundle', tt=[['Plant', ['White sage', 'Cedar']], ['Form', ['Bundle', 'Loose leaf']]], see=[('F4', 'Ritual incense', 'material burned for a named rite')]),
        ]),
     SH('Incense burners', 'Holders and burners made to burn incense at home; a burner made for religious rites → F4.',
        None,
        [K('Incense burner', x=['Kōro', 'Boshanlu'],
           tt=[['Burns', ['Sticks', 'Cones', 'Loose material on charcoal']], ['Form', ['Stick holder', 'Ash catcher', 'Censer', 'Backflow burner']]],
           see=[INC_BURN], s=S_INC),
         K('Mabkhara', x=['Dabqaad'], tt=[['Form', ['Traditional cuboid', 'Rounded modern metal']], ['Material', ['Wood and metal', 'Metal', 'Ceramic']]], see=[INC_BURN], s=S_INC),
         K('Kōdō utensil set', tt=[['Piece', ['Kōro (censer)', 'Gin-yō (mica plate)', 'Jūkōbako (incense box)', 'Hidōgu (fire tools)', 'Honkōban (display board)', 'Nagabon (tray)']]]),
        ]),
    ])
used_kinds.add('Stick and cone incense')
used_arch |= {'Shoyeido Daily Incense', 'Shoyeido Premium Incense', 'Nippon Kodo Traditional Series', 'Seiun', 'Morning Star', 'Masala agarbatti', 'Dhoop', '3-Wick Candle'}

# ---------------------------------------------------------------- 4 SEASONAL
add('Seasonal, festive & folk decor',
    'Decorations made for one festival or for a folk craft kept all year; a religious object for worship → Religious & Ceremonial Objects; a toy → Toys; string lights → Lighting.',
    'Which festival is it made for, or is it a folk craft kept out all year?',
    [
     SH('Christmas trees & ornaments', 'The tree and what is hung on or round it; a real tree → Plants & Living Cultures.',
        'kinds from the tree outwards: tree, ornament, topper, skirt, hook',
        [K('Artificial Christmas tree', x=['Feather tree', 'Brush tree', 'Aluminium tree', 'Fibre-optic tree', 'Flip Tree'],
           tt=[['Needle material', ['PVC', 'PE moulded tips', 'Feather', 'Aluminium']], ['Lighting', ['Pre-lit LED', 'Pre-lit incandescent', 'Unlit']], ['Finish', ['Green', 'Flocked', 'White']], ['Shape and size', ['Full', 'Slim', 'Tabletop or mini']]],
           see=[('C3', 'Christmas tree', 'a real tree')], s=S_XMAS),
         K('Tree ornament', x=['Lauscha blown-glass ornament', 'Shiny Brite ball', 'Christmas pickle', 'Keepsake Ornament'],
           tt=[['Material', ['Glass', 'Shatterproof plastic', 'Wood', 'Fabric or felt', 'Metal']], ['Shape', ['Ball', 'Figural', 'Icicle', 'Finial']], ['Issue', ['Open range', 'Dated annual']]], s=S_XMAS),
         K('Tree topper', tt=[['Shape', ['Star', 'Angel', 'Finial or spire', 'Bow']], ['Material', ['Glass', 'Fabric', 'Metal', 'Lit plastic']]], s=S_XMAS),
         K('Tree skirt', tt=[['Form', ['Skirt', 'Rigid collar']], ['Material', ['Fabric', 'Knitted', 'Faux fur', 'Wicker']]]),
         K('Ornament hook', tt=[['Form', ['Wire hook', 'Clip', 'Ribbon loop']]]),
        ]),
     SH('Christmas around the home', 'Christmas pieces for the door, fireplace, table, window and shelf; a nativity scene or Advent wreath for worship → F4.',
        'kinds by where it goes: door, fireplace, wall, table, shelf, window',
        [K('Wreath', tt=[['Material', ['Evergreen', 'Holly', 'Harvest (grain, straw)', 'Dried', 'Artificial']], ['Lighting', ['Unlit', 'Pre-lit']]],
           see=[('C3', 'Fresh wreath', 'a fresh-cut wreath'), ('F4', 'Advent wreath', 'a wreath made for worship')], s=S_XMAS),
         K('Christmas stocking', tt=[['Material', ['Knitted', 'Felt', 'Needlepoint', 'Velvet']], ['Personalisation', ['Plain', 'Personalised']]], s=S_XMAS),
         K('Reusable Advent calendar', tt=[['Form', ['Fabric pockets', 'Wooden box with cubby holes', 'Card with doors', 'Stand-up']]],
           see=[('F4', 'Advent wreath', 'a wreath made for worship')]),
         K('Christmas cracker', x=['Tom Smith cracker'], tt=[['Grade', ['Standard', 'Luxury']], ['Filling', ['Pre-filled', 'Fill-your-own']]]),
         K('Christmas village', x=['Moravian putz', 'Cardboard putz house', 'Original Snow Village', "Dickens' Village"],
           tt=[['Material', ['Porcelain or ceramic', 'Resin', 'Cardboard']], ['Features', ['Lit', 'Animated', 'Unlit']], ['Piece', ['Building', 'Figures', 'Accessories']]], s=S_XMAS),
         K('Snow globe', x=['Viennese snow globe', 'Water-filled paperweight globe', 'Plastic snow globe'],
           tt=[['Material', ['Glass', 'Plastic']], ['Feature', ['Still', 'Musical', 'Lit']]],
           see=[('B4', 'Glass paperweight', 'the water-filled globe began as a paperweight')], s=S_XMAS),
         K('Moravian star', d='Faceted, many-pointed star lantern hung in a window or hall at Christmas, often lit from inside.', a='Herrnhut star · Advent star',
           tt=[['Material', ['Paper', 'Plastic', 'Glass']], ['Points', ['Fewer than 26', '26', 'More than 26']], ['Lighting', ['Lit', 'Unlit']]], s=S_XMAS),
        ]),
     SH('Ore Mountains Christmas craft', 'Wooden Christmas figures and holders from the Erzgebirge, collected as folk craft; a nutcracker made as a toy → Toys.',
        'kinds by what the carved piece does: cracks nuts, smokes, turns, holds candles',
        [K('Nutcracker figure', x=['Erzgebirge soldier or king nutcracker', 'Steinbach collectible character nutcracker', 'Christian Ulbricht nutcracker'],
           tt=[['Function', ['Working', 'Decorative only']], ['Subject', ['Soldier', 'King', 'Miner', 'Character']], ['Size', ['Table', 'Floor-standing']]]),
         K('Smoking figure', x=['Räuchermann', 'Edge-sitter smoker', 'Räucherfrau', 'Multi-figure smoker scene'],
           tt=[['Subject', ['Craftsman', 'Woman', 'Group scene']], ['Posture', ['Standing', 'Edge-sitter']]]),
         K('Christmas pyramid', x=['Ore Mountains table pyramid'], tt=[['Drive', ['Candle-driven', 'Electric']], ['Tiers', ['One tier', 'Several tiers']]]),
         K('Candle arch', x=['Johanngeorgenstadt forged arch', "Schwarzenberg miners' arch"], tt=[['Material', ['Wood', 'Metal']], ['Light', ['Candle', 'Electric']]]),
        ]),
     SH('Halloween', 'Decorations for Halloween, collected by maker and era; a costume → Clothing.',
        'kinds by how it is made: flat card, hollow container, lit plastic figure',
        [K('Halloween die-cut', x=['Beistle Halloween die-cut'], tt=[['Subject', ["Jack-o'-lantern", 'Black cat', 'Witch', 'Skeleton']], ['Paper', ['Plain stock', 'Embossed']], ['Era', ['Pre-war', 'Mid-century', 'Modern reprint']]]),
         K("Halloween jack-o'-lantern container", x=["German pressed-cardboard jack-o'-lantern", "US pulp jack-o'-lantern"], tt=[['Material', ['Pressed cardboard', 'Papier-mâché', 'Pulp', 'Composition']], ['Fitting', ['With wire handle', 'Without handle']]]),
         K('Blow-mould figure', x=['Vintage Halloween blow mould'], tt=[['Subject', ["Jack-o'-lantern", 'Ghost', 'Witch', 'Skeleton', 'Black cat']], ['Light', ['Lit', 'Unlit']]]),
        ]),
     SH('Easter', 'Decorations made for Easter; chocolate eggs are food.',
        None,
        [K('Decorated Easter egg', x=['Pysanka', 'Drapanka', 'Malovanka'], tt=[['Egg', ['Blown hen egg', 'Goose egg', 'Wooden']], ['Decoration', ['Wax-resist', 'Scratched', 'Painted']]]),
         K('Easter tree', tt=[['Form', ['Outdoor tree or bush', 'Tabletop twigs']], ['Hung with', ['Blown eggs', 'Ornament eggs']]]),
        ]),
     SH('East Asian festival decor', 'Decorations for Lunar New Year, Japanese New Year and Japanese doll festivals; a Buddhist altar piece → F4.',
        'kinds by festival: Lunar New Year, Japanese New Year, doll festivals',
        [K('Spring Festival couplet', tt=[['Piece', ['Couplet pair', 'Horizontal scroll (hengpi)', 'Square fu or chun (doufang)']], ['Making', ['Hand-written', 'Printed']], ['Material', ['Paper', 'Cloth', 'Plastic']]]),
         K('Paper-cut window decoration', tt=[['Style', ['Northern (Yu county)', 'Southern (Foshan)']], ['Cut with', ['Scissors', 'Knife']]]),
         K('New Year entrance decoration', frm='Entrance decoration', a='kadomatsu · gate pine', x=['Kadomatsu'], tt=[['Material', ['Bamboo and pine', 'Bamboo, pine and plum']], ['Size', ['Full-size pair', 'Tabletop']]]),
         K('Festival doll display', x=['Hina-ningyō', 'Gogatsu-ningyō'], tt=[['Festival', ['Hinamatsuri (3 March)', "Children's Day (5 May)"]], ['Layout', ['Imperial pair only', 'Tiered set (hinadan)', 'Cased display']]],
           see=[('E1', 'Traditional doll', 'dolls made for play')]),
        ]),
     SH('Folk dolls & figures', 'Hand-turned or carved figures from named folk crafts, kept on display all year; a doll made for play → Toys.',
        'kinds by craft region: Japan, Russia, Sweden',
        [K('Kokeshi', x=['Tōgatta kokeshi', 'Naruko kokeshi', 'Tsuchiyu kokeshi', 'Yajirō kokeshi', 'Sakunami kokeshi', 'Zaō Takayu kokeshi', 'Hijiori kokeshi', 'Kijiyama kokeshi', 'Nambu kokeshi', 'Tsugaru kokeshi', 'Sōsaku kokeshi'],
           tt=[['Type', ['Traditional (dentō)', 'Creative (sōsaku)']], ['Size', ['Miniature', 'Standard', 'Large']]], see=[('E1', 'Traditional doll', 'dolls made for play')]),
         K('Daruma', x=['Takasaki daruma', 'Matsukawa daruma', 'Hime daruma', 'Triangle daruma', 'Goshiki daruma'], tt=[['Colour', ['Red', 'Blue', 'White', 'Gold']], ['Eyes', ['Blank', 'Painted']]]),
         K('Matryoshka', x=['Malyutin–Zvyozdochkin original', 'Sergiev Posad matryoshka', 'Semyonov matryoshka', 'Polkhovsky Maidan matryoshka', 'Kirov (Vyatka) matryoshka'], tt=[['Pieces', ['Three', 'Five', 'Seven', 'Ten or more']], ['Decoration', ['Traditional peasant girl', 'Themed', 'Landscape']]], see=[('E1', 'Traditional doll', 'dolls made for play')]),
         K('Dala horse', x=['Nusnäs Dala horse'], tt=[['Size', ['Miniature', 'Standard', 'Large']], ['Colour', ['Red', 'Blue', 'Natural']]]),
        ]),
    ])
used_kinds.add('Entrance decoration')

# ---------------------------------------------------------------- 5 PARTY
add('Party & celebration effects',
    'Things set off, switched on or hung up to mark a celebration; party lights bought as lighting → Lighting; a toy cap gun → Toys.',
    'What does it do at a celebration: go off in the air or on the ground, throw fog and light, or dress the room?',
    [
     SH('Fireworks', 'Consumer pyrotechnics that burn or burst for show; professional display shells are out of scope.',
        'kinds by where the effect happens: fired from a tube, self-launched, on the ground, in the hand, novelty',
        [K('Firework cake & barrage', tt=[['Layout', ['Single-shot barrage', 'Compound (several cakes fused)', 'Roman candle (single long tube)']], ['Effect', ['Peony', 'Willow', 'Palm', 'Crossette', 'Crackle']], ['Class', ['EU F2', 'EU F3', 'UK Category 2', 'UK Category 3']]], s=S_FW),
         K('Firework shell & mine', tt=[['Launch', ['Reloadable shell kit with tube', 'Single mine', 'Multi-shot mine']], ['Build', ['Single break', 'Multi-break']], ['Burst pattern', ['Peony', 'Chrysanthemum', 'Dahlia', 'Willow', 'Kamuro', 'Palm', 'Crossette', 'Horsetail', 'Ring', 'Spider', 'Fish', 'Time rain']], ['Report', ['Salute (flash and bang)']], ['Size', ['Small calibre', 'Large calibre']]], s=S_FW),
         K('Firework rocket', x=['Bottle rocket', 'Whistle rocket'], tt=[['Stabiliser', ['Stick', 'Fin']], ['Pack', ['Single', 'Pack']], ['Size', ['Small', 'Large (UK motor weight)']]], s=S_FW),
         K('Fountain & wheel', frm='Ground firework', a='fountain · gerb · Catherine wheel · ground spinner · cone · volcano',
           d='Firework that stays on the ground or its post and throws sparks, flame or spin: fountain, wheel, ground spinner.',
           tt=[['Motion', ['Stationary fountain', 'Ground spinner', 'Flying spinner', 'Wheel on a post']], ['Mount', ['Ground', 'Hand-held or stake', 'Nailed to a post']], ['Effect', ['Coloured', 'Crackling', 'Glitter']], ['Setting', ['Outdoor', 'Indoor (ice fountain)']]], s=S_FW),
         K('Firecracker & banger', frm='Ground firework', a='firecracker · banger · salute · cannon',
           d='Firework made to give a loud report, from a pea-sized bang snap to a flash-powder salute.',
           x=['Mandarin cracker string', 'Flash cracker', 'Cherry bomb', 'Bang snap'],
           tt=[['Powder', ['Black powder', 'Flash powder', 'Silver fulminate']], ['Pack', ['Single cracker', 'String or roll']], ['Ignition', ['Fuse', 'Thrown or pulled']]], s=S_FW),
         K('Sparkler', x=['Wire sparkler', 'Senko hanabi'], tt=[['Length', ['Short', 'Standard', 'Long']], ['Sparks', ['White', 'Gold', 'Coloured']], ['Wire', ['Straight', 'Heart and shaped']]], s=S_FW),
         K('Smoke & novelty firework', d='Small fireworks made for show on the ground that do not burst: coloured smoke, Pharaoh\'s serpent and similar novelties.', a='smoke bomb · pharaoh\'s serpent',
           tt=[['Effect', ['Coloured smoke', 'Growing ash serpent', 'Snaps']]], see=[('B4', 'Party popper', 'a hand-held party effect')], s=S_FW),
        ]),
     SH('Stage & party effects', 'Machines and lights that throw fog, light or reflections at a party; a lamp for a room → Lighting.',
        'kinds by what the effect produces: fog or haze, scattered reflections, coloured beams and washes',
        [K('Fog and haze machine', tt=[['Output', ['Fog (heated)', 'Haze', 'Low-lying fog (chilled)']], ['Fluid', ['Glycol', 'Oil', 'Water-based']], ['Control', ['Wired remote', 'DMX', 'Wireless']]]),
         K('Mirror ball', x=['Rotating disco mirror ball'], tt=[['Drive', ['Motorised', 'Static']], ['Use', ['Party', 'Home decor']]]),
         K('Party & DJ light', tt=[['Fixture', ['PAR can', 'Moving head', 'Pinspot', 'Beam', 'Wash', 'Laser', 'Strobe']], ['Control', ['Sound-activated', 'DMX', 'Remote']]], see=[('B3', 'Neon light', 'a lit sign made as decoration')]),
        ]),
     SH('Party decorations', 'Decorations hung, thrown or burst at a party; a firework → Fireworks.',
        'kinds by how it is used: floated, hung up, thrown or popped, broken open',
        [K('Balloon', tt=[['Material', ['Latex', 'Foil (metallised)']], ['Fill', ['Air', 'Helium', 'Water']], ['Type', ['Round', 'Modelling (twisting)', 'Printed']]], s=W+'Balloon'),
         K('Garland', tt=[['Material', ['Foliage', 'Tinsel', 'Bead', 'Paper', 'Balloon']]], s=S_XMAS),
         K('Bunting', tt=[['Material', ['Fabric', 'Paper', 'Plastic']], ['Flag shape', ['Triangular pennant', 'Rectangular']]]),
         K('Paper streamer', tt=[['Form', ['Crepe paper roll', 'Tassel garland', 'Throw streamer']]]),
         K('Confetti', tt=[['Material', ['Paper', 'Foil', 'Biodegradable', 'Dried petal']], ['Delivery', ['Handful or table scatter', 'Confetti cannon']]]),
         K('Party popper', tt=[['Mechanism', ['String-pull friction charge', 'Compressed air', 'Twist-off cannon']], ['Content', ['Streamers', 'Confetti']]], s=S_POP),
         K('Piñata', x=['Seven-pointed star piñata', 'Character piñata'], tt=[['Body', ['Clay pot', 'Papier-mâché', 'Cardboard']], ['Opening', ['Hit with a stick', 'Pull-string']]], see=[('E1', 'Piñata', 'sold as a toy')]),
        ]),
    ])
for dummy in ('Ground firework',): used_kinds.add(dummy)

# ---------------------------------------------------------------- 6 PLANTS
add('Artificial & dried plants',
    'Plant decorations that need no watering: imitations, and real plant material dried or treated to last; a living plant → Plants & Living Cultures.',
    'Is the plant an imitation, or real plant material that has been dried or treated?',
    [
     SH('Imitation plants', 'Manufactured copies of flowers and plants; an artificial Christmas tree → Seasonal, festive & folk decor.',
        'kinds by what is imitated: flowers, or foliage, plants and trees',
        [K('Artificial flower', tt=[['Material', ['Polyester', 'Plastic', 'Paper', 'Clay', 'Wax']], ['Arrangement', ['Single stem', 'Bouquet', 'Arrangement in pot']]], s=S_ART),
         K('Artificial plant', tt=[['Form', ['Potted plant', 'Tree', 'Hanging or trailing', 'Foliage stem']], ['Material', ['Polyester', 'Plastic', 'Paper']]], s=S_ART),
        ]),
     SH('Dried & preserved plants', 'Real plant material kept for display; a living plant → Plants & Living Cultures.',
        'kinds by treatment: air-dried, or preserved with glycerine or dye',
        [K('Dried flowers', tt=[['Form', ['Bunch', 'Arrangement', 'Pampas and grasses']], ['Drying', ['Air-dried', 'Freeze-dried']]], see=[('C3', 'Fresh wreath', 'a fresh-cut wreath')]),
         K('Preserved plant', tt=[['Form', ['Moss wall art', 'Preserved rose', 'Preserved foliage']], ['Treatment', ['Glycerine-preserved', 'Dyed']]]),
        ]),
    ])

# ---------------------------------------------------------------- 7 GARDEN
add('Garden ornaments',
    'Ornaments set in a garden for their looks; a plant pot → Garden & Grounds; a pump or pond liner → Garden & Grounds; a feeder or nest box → Pet & Animal Supplies.',
    'Is the ornament a figure, a still focal piece, or a feature moved by wind or water?',
    [
     SH('Statues & figures', 'Figures of people, animals and saints placed in a garden; a pedestal or column → Focal pieces.',
        'kinds from formal statuary to humorous lawn figures: statue, gnome, lawn ornament',
        [K('Garden statue', x=['Medici lion', 'River God (Father Thames)', 'Coade lion', 'Saint Francis of Assisi statue', 'Bathtub Madonna'],
           tt=[['Subject', ['Classical figure', 'Animal figure', 'Religious figure', 'Modern or abstract']], ['Material', ['Cast stone', 'Natural stone', 'Lead or bronze', 'Concrete', 'Resin or plastic']]],
           see=[('F4', 'Devotional statue', 'statue made for devotion')], s=S_GARD),
         K('Garden gnome', x=['Thuringian terracotta gnome', 'Lampy', 'Brienz wooden house dwarf'], tt=[['Material', ['Terracotta', 'Ceramic', 'Resin', 'PVC plastic', 'Wood']], ['Style', ['Traditional', 'Novelty or humorous']]], s=S_GARD),
         K('Lawn ornament', d='Mass-made figure or spinning novelty pushed into a lawn or border, from flamingos to jiggler flowers.', a='yard art · lawn figure',
           x=['Pink plastic flamingo'], tt=[['Subject', ['Animal figure', 'Human figure', 'Flower or insect on a spring stake', 'Miniature windmill or lighthouse']], ['Material', ['Plastic', 'Concrete', 'Metal', 'Wood']]], s=S_GARD),
        ]),
     SH('Focal pieces', 'Still garden pieces that hold up, reflect, hold water or tell the time; a figure → Statues & figures.',
        'kinds by what the piece offers: a base for another piece, a reflection, a bath for birds, the time',
        [K('Garden pedestal or column', tt=[['Form', ['Square plinth', 'Round socle', 'Column']], ['Material', ['Cast stone', 'Terracotta', 'Natural stone']]], s=S_GARD),
         K('Gazing ball', x=['Venetian blown-glass gazing ball', 'Art Deco mirror globe'], tt=[['Material', ['Glass', 'Stainless steel', 'Acrylic', 'Ceramic', 'Stained glass']], ['Mount', ['Stemmed', 'Loose', 'Ceramic stand', 'Wrought-iron stand']]], s=S_GARD),
         K('Bird bath', x=['Pedestal bird bath'], tt=[['Mount', ['Pedestal', 'Hanging', 'Ground-level']], ['Material', ['Concrete', 'Glazed terracotta', 'Glass', 'Copper', 'Mosaic', 'Marble or stone']], ['Water', ['Still', 'Solar fountain']]], s=S_GARD),
         K('Garden sundial', x=['Horizontal garden sundial'], tt=[['Dial type', ['Horizontal', 'Armillary', 'Vertical wall dial', 'Analemmatic']], ['Material', ['Bronze', 'Brass', 'Cast stone']]], see=[('A5', 'Sundial', 'a sundial kept as a timekeeper')], s=S_GARD),
        ]),
     SH('Wind & water features', 'Garden pieces moved by wind or water; a pond pump → Garden & Grounds.',
        'kinds by what moves them: wind (sound, spin, direction) or water',
        [K('Wind chime', x=['Tintinnabulum', 'Fūrin', 'Chimes of Olympos', 'Music of the Spheres pentatonic chime', 'Koshi chime', 'Zaphir chime'], tt=[['Sounding part', ['Tuned metal tube', 'Bamboo', 'Glass', 'Shell', 'Ceramic', 'Bell']], ['Tuning', ['Pentatonic', 'Tuned to a chord', 'Untuned']], ['Light', ['Plain', 'Solar-lit']]], s=S_GARD),
         K('Wind spinner', x=['Whirligig'], tt=[['Form', ['Hanging spiral', 'Staked kinetic', 'Windmill', 'Figural whirligig']]], s=S_GARD),
         K('Weathervane', x=['Weathercock', 'Running horse', 'Banner vane', 'Figural vane'], tt=[['Mount', ['Roof-mounted', 'Garden-staked']], ['Metal', ['Copper', 'Cast iron', 'Steel silhouette']], ['Compass points', ['With', 'Without']]], s=S_GARD),
         K('Garden fountain', tt=[['Form', ['Tiered', 'Wall fountain', 'Bubbler or ball', 'Cascade']], ['Power', ['Mains', 'Solar-powered']], ['Self-contained', ['Self-contained', 'Needs a pump']]], s=S_GARD),
         K('Rain chain', d='Chain or linked cups hung from a gutter to guide rainwater to the ground, a Japanese alternative to a downpipe.', a='kusari-doi',
           tt=[['Form', ['Linked cups', 'Plain chain']], ['Material', ['Copper', 'Aluminium', 'Iron']]], s=S_GARD),
        ]),
    ])

# ---------------------------------------------------------------- 8 FLAGS
add('Flags & signs',
    'Cloth flags with their poles, and signs that carry a word or motif for decoration; a safety sign → Safety; a street address plate → Hardware & Ironmongery.',
    'Is it cloth flown from a pole, or a flat or lit sign fixed to a wall?',
    [
     SH('Flags & flagpoles', 'Cloth flags flown from a pole or bracket, and the poles; a flag worn as clothing → Clothing.',
        None,
        [K('Flag', tt=[['Subject', ['National', 'State or territory', 'House', 'Garden', 'Club or interest']], ['Form', ['Rectangular', 'Pennant (tapering)', 'Swallowtail', 'Vertical banner flag', 'Windsock']]],
           see=[('F4', 'Prayer flag', 'flag hung for prayer')], s=S_FLAG),
         K('Flagpole', tt=[['Mount', ['Wall-mounted bracket', 'In-ground', 'Telescopic']], ['Fitting', ['Finial or ball truck', 'Pulley and halyard', 'Rotating ring']]], s=S_FLAG),
        ]),
     SH('Signs', 'Flat or lit signs made to carry a word or motif as decoration.',
        None,
        [K('Decorative sign or plaque', tt=[['Display', ['Wall-fixed', 'Hanging']], ['Material', ['Wood', 'Metal', 'Enamel']]]),
         K('Illuminated sign', tt=[['Light', ['Glass neon', 'LED neon-effect']], ['Content', ['Word', 'Motif']]], see=[('B3', 'Neon light', 'lit decoration'), ('F2', 'Neon sculpture', 'neon made as art')]),
        ]),
    ])

# ---------------------------------------------------------------- ASSEMBLE
new = {'c': 'B4', 'rev': True}
new['lead'] = old['lead']
new['ax'] = 'What is the object for: standing as a vessel or glass piece, lining a wall, giving off light or scent, marking a festival or party, imitating a plant, adorning the garden, or flying as a flag or sign?'
new['key'] = [
    '1. Is it a vase, jar, bottle, bowl, urn or glass weight kept to hold flowers or be looked at? → Vases & decorative glass and ceramics',
    '2. Is it a mirror, frame, panel or sticker for a wall? → Mirrors & wall decor',
    '3. Is it burned, heated or sprayed to light or scent a room (candle, holder, diffuser, incense)? → Candles & home fragrance',
    '4. Is it made for one festival, or a folk craft kept all year (tree, ornament, wreath, kokeshi)? → Seasonal, festive & folk decor',
    '5. Is it set off, switched on or hung up at a party (firework, fog machine, balloon, confetti)? → Party & celebration effects',
    '6. Does it imitate a plant, or is it real plant material dried to last? → Artificial & dried plants',
    '7. Is it placed in a garden for its looks (statue, gnome, bird bath, wind chime, fountain)? → Garden ornaments',
    '8. Is it a flag, flagpole or sign? → Flags & signs',
    '<i>Precedence: a lantern or string of lights is Lighting (step 3 does not apply); a Christmas candle holder or snow globe goes by its festival (step 4) before its form; a firework is party (step 5) even when sold for a festival; an artificial Christmas tree is step 4, not step 6.</i>',
]
new['b'] = old['b']
for d in depts:
    if 'src' in d:
        d['s_'] = d.pop('src')
# keep dept-level 's' (source) key name 's' is the shelf list; old dept-source dropped as before in schema (shelves use 's')
new['depts'] = depts

# ---- checks
missing_arch = [a for a in oarch if a not in used_arch]
missing_kinds = [k for k in okinds if k not in used_kinds]
print('arch not placed:', missing_arch)
print('kinds not placed:', missing_kinds)
def cnt(c, f):
    return sum(f(k) for d in c['depts'] for s in d['s'] for k in s['k'])
print('m/r before', cnt(old, lambda k: len(k.get('m', []))), cnt(old, lambda k: len(k.get('r', []))), 'after', cnt(new, lambda k: len(k.get('m', []))), cnt(new, lambda k: len(k.get('r', []))))
for d in new['depts']:
    d.pop('s_', None)
# see targets
bad = []
names = {k['n'] for d in new['depts'] for s in d['s'] for k in s['k']}
for d in new['depts']:
    for s in d['s']:
        for k in s['k']:
            for sv in k.get('see', []):
                c, n = sv[0], sv[1]
                if c == 'B4':
                    ok = n in names
                else:
                    r = json.load(open(R + 'reader/%s.json' % c))
                    ok = any(kk['n'] == n for dd in r['depts'] for ss in dd['s'] for kk in ss['k'])
                if not ok: bad.append(sv)
print('bad see:', bad)
json.dump(new, open(R + 'work/STR_B4/new_B4.json', 'w'), ensure_ascii=False, indent=1)
