import json, copy, os
R = '/home/user/Possession-Taxonomy/rebuild/out/'
d = json.load(open(R + 'B4.json'))
brands = json.load(open(R + 'B4_brands.json'))
trad = json.load(open(R + 'B4_traditions.json'))
moves = json.load(open(R + 'B4_moves.json'))

def loc(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i, k in enumerate(s['k']):
                if k['n'] == n:
                    return dp, s, i, k
    raise KeyError(n)

def pop(n):
    dp, s, i, k = loc(n)
    s['k'].pop(i)
    return k

def arch(n, d_, mk, y, s, v=None, dt='', a=''):
    return {"n": n, "a": a, "d": d_, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}

def ver(n, mk='', y='', d_=''):
    return {"n": n, "mk": mk, "y": y, "d": d_}

# ---------- B4-2 glass and pottery ----------
WIKI = 'https://en.wikipedia.org/wiki/'
vase = loc('Vase')[3]
vase['x'] += [
    arch('Rimini Blu vase', 'Stamped-pattern ceramic vase under a deep blue glaze, designed by Aldo Londi; produced continuously since 1959.',
         'Bitossi Ceramiche', '1959', 'https://www.bitossiceramiche.it/en/collections/rimini-blu',
         [ver('Handled vase', 'Bitossi Ceramiche'), ver('Egg vase', 'Bitossi Ceramiche'), ver('Ball-shaped vase', 'Bitossi Ceramiche'), ver('Bottle-shaped vase', 'Bitossi Ceramiche')],
         'height · stamped motif · blue glaze'),
    arch('West German pottery vase', 'Vase in thick, flowing glazes from West Germany, 1949–1990; base marked with shape number and height in cm.',
         '', '1949–1990', WIKI + 'West_German_Art_Pottery',
         [ver('Scheurich', 'Scheurich', '', 'prolific producer'), ver('Carstens', 'Carstens', '', 'prolific producer'), ver('Bay Keramik', 'Bay Keramik', '', 'prolific producer'), ver('Jasba', 'Jasba', '', 'well-known producer')],
         'shape number and height on base · glaze (fat lava is one subset) · maker sticker', a='fat lava vase'),
    arch('Banjo vase', 'Whitefriars vase designed by Geoffrey Baxter in the late 1960s.',
         'Whitefriars Glass', 'late 1960s', WIKI + 'Whitefriars_Glass', [], 'colour · size'),
    arch('Textured range', 'Whitefriars vases with moulded textured surfaces, introduced by Geoffrey Baxter in 1967.',
         'Whitefriars Glass', '1967', WIKI + 'Whitefriars_Glass',
         [ver('Knobbly bark vase', 'Whitefriars Glass'), ver('Drunken Bricklayer', 'Whitefriars Glass')], 'colour · size'),
    arch('Carnaby series', 'Holmegaard glass series by Per Lütken, 1969.',
         'Holmegaard Glasværk', '1969', WIKI + 'Holmegaard_Glass_Factory', [], 'colour · size'),
    arch('Hobnail vase', 'Opalescent glass moulded with raised studs; Fenton began selling its hobnail range in 1940.',
         'Fenton Art Glass Company', '1940', WIKI + 'Fenton_Art_Glass_Company',
         [ver('French Opalescent', 'Fenton Art Glass Company', '', 'first colourways, 1940'), ver('Cranberry Opalescent', 'Fenton Art Glass Company', '', 'first colourways, 1940')],
         'colour · opalescence · size'),
    arch('Blenko designer vase', 'Hand-blown West Virginia vase dated by the designer leading the studio: Winslow Anderson from 1947.',
         'Blenko Glass Company', '1947', WIKI + 'Blenko_Glass_Company',
         [ver('Winslow Anderson era', 'Blenko Glass Company', '1947', 'first full-time designer'), ver('Wayne Husted era', 'Blenko Glass Company', '', ''), ver('Joel Philip Myers era', 'Blenko Glass Company', '1963', 'succeeded Husted as design director')],
         'designer · colour · size'),
]
bowl = loc('Decorative bowl')[3]
bowl['x'] = [
    arch('Carnival glass bowl', 'Moulded or pressed glass bowl with an applied iridescent shimmer, made mostly in the USA from 1907–08.',
         '', '1907–1925', WIKI + 'Carnival_glass',
         [ver('Fenton', 'Fenton Art Glass Company', '1907', 'first carnival glass, late 1907'), ver('Wishbone', 'Northwood Glass Company', '', 'Northwood pattern'), ver('Imperial', 'Imperial Glass Company'), ver('Dugan', 'Dugan Glass Company')],
         'colour: marigold, amethyst, blue, green · pattern · maker'),
    arch('Depression glass bowl', 'Machine-made glass bowl in a named pattern, sold cheaply in North America 1929–1939.',
         '', '1929–1939', WIKI + 'Depression_glass',
         [ver('American Sweetheart', 'MacBeth-Evans Glass Company'), ver('Cherry Blossom', 'Jeannette Glass Company'), ver('Royal Lace', 'Hazel-Atlas Glass Company'), ver('Miss America', 'Hocking Glass Company'), ver('Mayfair', 'Federal Glass Company')],
         'pattern · colour: pink, green, clear, cobalt · maker'),
    arch('Provence bowl', 'Holmegaard glass bowl by Per Lütken, one of his best-known designs.',
         'Holmegaard Glasværk', '', WIKI + 'Holmegaard_Glass_Factory', [], 'colour · size'),
]
bowl['a'] = bowl.get('a', '')

# ---------- B4-4 fold near-empty candle / plant kinds ----------
ik = 'https://www.ikea.com/gb/en/cat/candles-holders-10760/'
for n in ['Pillar candle', 'Taper candle', 'Tealight', 'Votive candle', 'Floating candle']:
    pop(n)
dp, sh, i, _ = loc('Container candle')
sh['k'].insert(i + 1, {
    "n": "Free-standing candle", "a": "pillar candle · taper · tealight · votive · floating candle",
    "d": "Candle that burns without its own jar: pillar, taper, tealight, votive or floating.",
    "t": ["pillar (block)", "taper (dinner candle)", "tealight", "votive", "floating", "dripless", "scented or unscented"],
    "s": ik, "m": [["FENOMEN", "IKEA"], ["KLOKHET", "IKEA"], ["GLIMMA", "IKEA"]]})
pop('Potpourri'); pop('Scented sachet')
dp, sh, i, _ = loc('Wax warmer')
sh['k'].insert(i + 1, {
    "n": "Potpourri & scented sachet", "a": "potpourri · drawer sachet · lavender bag",
    "d": "Dried scented plant material or a scented pouch kept in a bowl, drawer or wardrobe (odour absorbers are in Cleaning & Laundry).",
    "t": ["loose potpourri", "drawer sachet", "lavender bag"],
    "s": "https://www.ikea.com/gb/en/cat/home-fragrance-42926/"})
flag = loc('Flag')[3]
flag['t'] += ['Pennant (tapering, usually triangular)', 'Decorative windsock (garden or festive streamer)']
pop('Pennant'); pop('Feather banner'); pop('Decorative windsock')

# ---------- B4-6 Kodo, Bird bath ----------
kd = loc('Kōdō utensil set')[3]
kd['d'] = "Set of utensils used in kōdō, with censer, mica plates and fire tools; the practice itself belongs to the pursuit taxonomy."
for t in trad['t']:
    if t['n'] == 'Kōdō':
        t['d'] = "Japanese incense-appreciation tradition whose utensils, incense woods and boxes are collected as objects; the practice itself belongs to the pursuit taxonomy."
bb = loc('Bird bath')[3]
bb['d'] = "Shallow water-filled basin where garden birds drink and bathe, also kept as an ornament. Bird feeders and nest boxes are in Pet & Animal Supplies."
# merge Lauscha traditions
la = [t for t in trad['t'] if t['n'] == 'Lauscha glass ornaments'][0]
lb = [t for t in trad['t'] if t['n'] == 'Lauscha glass'][0]
la['tech'] = la['tech'] + '; lamp-blowing into clay moulds, silver-nitrate silvering'
la['mat'] = la['mat'] + ', silver nitrate'
la['d'] = "Glassblowing town where moulded coloured glass ornaments and the glass bauble originated; exported worldwide from the 1840s."
la['auth'] = la['auth'] + ' Blown by one of the small family firms in Lauscha (about 20 in 2009).'
trad['t'] = [t for t in trad['t'] if t['n'] != 'Lauscha glass']

# ---------- B4-3 fireworks ----------
fs = loc('Firework cake')[1]
cake = pop('Firework cake'); rom = pop('Roman candle')
rocket = pop('Firework rocket'); shell = pop('Aerial shell'); mine = pop('Mine')
fount = pop('Firework fountain'); wheel = pop('Catherine wheel'); spin = pop('Ground spinner')
fcr = pop('Firecracker'); smoke = pop('Smoke device'); spark = pop('Sparkler')
FW = 'https://en.wikipedia.org/wiki/Fireworks'
new_fw = [
    {"n": "Firework cake & barrage", "a": "cake · barrage · compound · Roman candle",
     "d": "Cluster of tubes linked by one fuse, or one long tube, that fires a timed series of aerial effects.",
     "t": cake['t'] + ['Roman candle (single long tube, shot count)'], "s": cake['s']},
    {"n": "Firework rocket", "a": rocket['a'], "d": rocket['d'], "t": rocket['t'], "s": rocket['s'], "x": rocket['x']},
    {"n": "Firework shell & mine", "a": "aerial shell · consumer mortar · shell kit · mine · pot à feu",
     "d": "Shell fired from a mortar tube, or a mortar-launched mine, that bursts in the air into a pattern of stars.",
     "t": shell['t'] + mine['t'] + [
         "Peony (spherical burst, no tails)", "Chrysanthemum (burst with trails)", "Dahlia (few large stars)", "Willow (drooping gold or silver)",
         "Kamuro (dense glitter trail)", "Palm (thick comet tails)", "Crossette (stars split in a cross)", "Horsetail (heavy tailed stars)",
         "Ring", "Spider (radial lines)", "Fish", "Time rain", "Salute (flash and report)"],
     "s": FW},
    {"n": "Ground firework", "a": "fountain · gerb · Catherine wheel · ground spinner · smoke device · firecracker · banger",
     "d": "Firework that stays on the ground or its post: fountain, wheel, spinner, smoke device or loud cracker.",
     "t": fount['t'] + wheel['t'] + spin['t'] + smoke['t'] + fcr['t'],
     "s": fount['s'], "x": fcr['x']},
    {"n": "Sparkler", "a": spark['a'], "d": spark['d'] + " (handheld)", "t": spark['t'], "s": spark['s'], "x": spark['x']},
]
# fix firecracker archetype names kept; firecracker archetypes keep their own sources
sh_idx = [i for i, dp_ in enumerate(d['depts']) if any(s['n'] == 'Fireworks' for s in dp_['s'])][0]
seasonal = d['depts'][sh_idx]
party = [s for s in seasonal['s'] if s['n'] == 'Party decorations & effects'][0]
fireshelf = [s for s in seasonal['s'] if s['n'] == 'Fireworks'][0]
fog = [k for k in party['k'] if k['n'] == 'Fog and haze machine'][0]
mball = [k for k in party['k'] if k['n'] == 'Mirror ball'][0]
fog['m'] = fog['m']  # models are consumer-adjacent DJ fog machines; kept
party['k'] = [k for k in party['k'] if k['n'] not in ('Fog and haze machine', 'Mirror ball')]
seasonal['s'] = [s for s in seasonal['s'] if s['n'] not in ('Fireworks', 'Party decorations & effects')]

# ---------- B4-5 new department ----------
newdept = {
    "n": "Party & celebration effects", "mode": "tier",
    "note": "Fireworks, stage effects and party decorations; party lights arrive from Lighting.",
    "b": [{"m": "Legal category and safety rating", "v": "EU F1–F4 · UK Category 1–4", "w": "Fireworks are sold and regulated by category; it decides where they may be used."},
          {"m": "Fluid and heat (fog machines)", "v": "", "w": "Fog fluid type and warm-up time decide output and use."}],
    "s": [{"n": "Fireworks", "k": new_fw},
          {"n": "Stage & party effects", "k": [fog, mball]},
          party]}
party['n'] = 'Party decorations'
seasonal['s'] = seasonal['s']
d['depts'].insert(sh_idx + 1, newdept)

# ---------- B4-1 seasonal shelves ----------
BEI = 'https://hauntedattractionnetwork.com/vintage-halloween-decorations-beistle-original-vs-reissue/'
halloween = {"n": "Halloween", "k": [
    {"n": "Halloween die-cut", "a": "Beistle die-cut · cardboard cut-out",
     "d": "Flat cardboard Halloween decoration cut from printed, often embossed sheet, collected by maker and era.",
     "t": ["jack-o'-lantern", "black cat", "witch", "skeleton", "paper stock", "embossed", "size"],
     "s": BEI,
     "x": [arch('Beistle Halloween die-cut', "Cardboard cut-out from the Pennsylvania firm that made Halloween its first seasonal line; originals date from the 1920s.",
                'Beistle Company', '1921', BEI,
                [ver('German-made die-cut', '', '1919–1935', 'marked Germany'),
                 ver('Beistle original', 'Beistle Company', '1920s–early 1930s', 'top-tier originals'),
                 ver('H. E. Luhrs', 'H. E. Luhrs', '1940s–early 1950s', 'marked with his name'),
                 ver('Party Partners reissue', '', '2003', 'reissue'),
                 ver('In-house reissue', 'Beistle Company', '2012', 'two copyright dates printed on the piece')],
                'paper stock · highlight colours · size · copyright mark · condition')]},
    {"n": "Halloween jack-o'-lantern container", "a": "pulp jack-o'-lantern · candy container",
     "d": "Hollow pressed-paper or pulp jack-o'-lantern, often holding candy or a light, collected by origin and era.",
     "t": ["pressed cardboard", "papier-mâché", "pulp", "composition", "with wire handle"],
     "s": 'https://eerieemporium.com/collections/vintage-halloween-paper-mache-items',
     "x": [arch('German pressed-cardboard jack-o\'-lantern', 'Pressed-paperboard jack-o\'-lantern made in Germany.', '', '1910s–1920s',
                'https://eerieemporium.com/collections/vintage-halloween-paper-mache-items', [], 'face · size · paint · condition'),
           arch('US pulp jack-o\'-lantern', 'Moulded pulp or papier-mâché jack-o\'-lantern made in the USA.', '', '1930s–1960s',
                'https://eerieemporium.com/collections/vintage-halloween-paper-mache-items', [], 'face · size · DayGlo paint · condition')]},
    {"n": "Blow-mould figure", "a": "blowmold · lighted yard figure",
     "d": "Hollow plastic figure, often lit from inside, made for lawn or porch at Halloween or Christmas.",
     "t": ["jack-o'-lantern", "ghost", "witch", "skeleton", "black cat", "lit", "unlit"],
     "s": 'https://www.antiquetrader.com/collectibles/blow-molds-the-comeback-kids-of-halloween-decor',
     "x": [arch('Vintage Halloween blow mould', 'Plastic yard decoration from the 1950s–60s boom, collected by maker.', '', '1950s–1960s',
                'https://www.antiquetrader.com/collectibles/blow-molds-the-comeback-kids-of-halloween-decor',
                [ver('Empire Plastics', 'Empire Plastics'), ver('General Foam Plastics', 'General Foam Plastics'), ver('Union Products', 'Union Products')],
                'figure · maker mark · light cord · condition')]},
]}
easter = {"n": "Easter", "k": [
    {"n": "Decorated Easter egg", "a": "pysanka · painted egg · folk egg",
     "d": "Real or wooden egg decorated for Easter by wax resist, scratching or painting, a folk craft in Slavic countries.",
     "t": ["blown hen egg", "goose egg", "wooden", "wax-resist", "scratched", "painted"],
     "s": WIKI + 'Pysanka',
     "x": [arch('Pysanka', 'Ukrainian egg with designs written in beeswax and revealed after several dye baths.', '', '', WIKI + 'Pysanka',
                [ver('Kistka-written', '', '', 'written with a wax-funnel stylus')], 'motif · region · dyes'),
           arch('Drapanka', 'Dyed egg whose pattern is scratched through to the white shell.', '', '', WIKI + 'Pysanka', [], 'motif · dye colour'),
           arch('Malovanka', 'Egg with a design painted on a raw egg with a brush.', '', '', WIKI + 'Pysanka', [], 'motif · paint')]},
    {"n": "Easter tree", "a": "Easter egg tree · Ostereierbaum",
     "d": "Tree, bush or table twig hung with blown, painted eggs, a German tradition.",
     "t": ["outdoor tree or bush", "tabletop twigs", "blown eggs", "ornament eggs"],
     "s": WIKI + 'Easter_tree'},
]}
lunar = {"n": "Lunar New Year", "k": [
    {"n": "Spring Festival couplet", "a": "chunlian · fai chun · door couplet",
     "d": "Pair of red paper strips with auspicious verse hung either side of a door at Lunar New Year.",
     "t": ["couplet pair", "horizontal scroll (hengpi)", "square fu or chun (doufang)", "hand-written", "printed", "cloth or plastic"],
     "s": WIKI + 'Chunlian'},
    {"n": "Paper-cut window decoration", "a": "chuanghua · window flower · jianzhi",
     "d": "Red paper cut with scissors or knife into symbols and animals and pasted on windows at festivals.",
     "t": ["northern style (Yu county)", "southern style (Foshan)", "scissors-cut", "knife-cut"],
     "s": WIKI + 'Chinese_paper_cutting'},
]}
folk = [s for s in seasonal['s'] if s['n'] == 'Folk & seasonal collectibles'][0]
ci = [i for i, s in enumerate(seasonal['s']) if s['n'] == 'Christmas'][0]
seasonal['s'][ci + 1:ci + 1] = [halloween, easter, lunar]

# traditions
trad['t'].append({"n": "Chinese paper cutting", "g": "Festive & folk crafts", "r": "China (Yu county, Hebei; Foshan, Guangdong)",
                  "p": "2nd century CE to present", "d": "Paper cut with scissors or knives into symbols and animals, used on windows at festivals.",
                  "tech": "scissors and knife cutting", "mat": "paper", "forms": ["Paper-cut window decoration"],
                  "ctr": ["Yu county (northern style)", "Foshan (southern style)"],
                  "auth": "Hand-cut from a single sheet rather than printed; regional style differs", "s": WIKI + 'Chinese_paper_cutting'})

# brands
def brand(n, c, f, seg, kf, d_, s, **kw):
    b = {"n": n, "c": c, "f": f, "seg": seg, "d": d_, "lines": kw.get('lines', []), "eras": [], "sig": kw.get('sig', []), "sc": [], "rel": [], "s": s, "kf": kf}
    brands['b'].append(b)
have = {b['n'].lower() for b in brands['b']}
add = [
    ('Fenton Art Glass Company', 'United States', '1905', 'Heritage manufactory', 'carnival glass', 'Ohio glassmaker of carnival, hobnail and opalescent glass; began in Martins Ferry.', WIKI + 'Fenton_Art_Glass_Company', ['Hobnail', 'Silver Crest'], ['Hobnail vase']),
    ('Blenko Glass Company', 'United States', '1922', 'Heritage manufactory', 'West Virginia glass', 'Hand-blown glass maker in Milton, West Virginia, known for designer vases and decanters.', WIKI + 'Blenko_Glass_Company', [], ['Blenko designer vase']),
    ('Whitefriars Glass', 'United Kingdom', '', 'Heritage manufactory', '1960s art glass', 'London glassmaker of James Powell and Sons, closed 1980, known for Geoffrey Baxter vases.', WIKI + 'Whitefriars_Glass', [], ['Banjo vase', 'Textured range']),
    ('Holmegaard Glasværk', 'Denmark', '1825', 'Heritage manufactory', 'Danish glass', 'Danish glassworks whose designers Jacob Bang and Per Lütken shaped its output.', WIKI + 'Holmegaard_Glass_Factory', [], ['Carnaby series', 'Provence bowl']),
    ('Bitossi Ceramiche', 'Italy', '', 'Artisan & independent', 'Rimini Blu', 'Italian ceramics maker whose Aldo Londi created the Rimini Blu series.', 'https://www.bitossiceramiche.it/en/collections/rimini-blu', [], ['Rimini Blu vase']),
    ('Beistle Company', 'United States', '1900', 'Heritage manufactory', 'die-cut decorations', 'Pennsylvania party-goods maker whose first seasonal line was Halloween.', BEI, [], ['Beistle Halloween die-cut']),
]
for n, c, f, seg, kf, dd, s, lines, sig in add:
    if n.lower() not in have:
        brand(n, c, f, seg, kf, dd, s, lines=lines, sig=sig)

# moves: nothing new to send from B4 (Party lights arrive from B3, no B4 kind leaves)
d['lead'] = d['lead']

for fn, obj in [('B4.json', d), ('B4_brands.json', brands), ('B4_traditions.json', trad), ('B4_moves.json', moves)]:
    tmp = R + fn + '.tmp'
    json.dump(obj, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, R + fn)
print('done')
