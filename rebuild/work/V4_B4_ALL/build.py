import json, copy
W = 'https://en.wikipedia.org/wiki/'
src = json.load(open('/home/user/Possession-Taxonomy/rebuild/out/B4.json'))
NAMES = ["Vases & decorative glass and ceramics", "Mirrors & wall decor", "Candles & home fragrance",
         "Seasonal, festive & folk decor", "Party & celebration effects", "Artificial & dried plants",
         "Garden ornaments", "Flags & signs"]
depts = [copy.deepcopy(d) for d in src['depts'] if d['n'] in NAMES]
D = {d['n']: d for d in depts}
KINDS = {}
SHELF = {}
for d in depts:
    for s in d['s']:
        SHELF[s['n']] = s
        for k in s['k']:
            KINDS[k['n']] = k

def E(n, d, s, mk='', y='', g=None, a='', v=None, dt='', role=None, own=None, tier=None, cty=None, own_y=None):
    e = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}
    if g: e['g'] = g
    if role: e['role'] = role
    if own: e['own'] = own
    if tier: e['tier'] = tier
    if cty: e['cty'] = cty
    if own_y: e['own_y'] = own_y
    return e

def getx(k, name):
    for x in k.get('x', []):
        if x['n'] == name:
            return x
    raise KeyError(name)

removed_m = []
for k in KINDS.values():
    if k.get('m'):
        removed_m.append((k['n'], len(k['m'])))
        del k['m']

# ---------- market fields on existing entries ----------
OWN = {
    'Iittala': ('Fiskars', 'National champion', 'Finland', '2007'),
    'Venini': ('Damiani S.p.A.', 'Independent', 'Italy', '2016'),
    'Lalique': ('Art & Fragrance (Lalique Group)', 'Independent', 'France', '2010'),
    'Holmegaard Glasværk': ('Rosendahl A/S', 'Independent', 'Denmark', '2008'),
    'Diptyque': ('Manzanita Capital', 'Independent', 'France', '2005'),
    'Yankee Candle': ('Newell Brands', 'Global group', 'United States', '2016'),
    'Le Labo': ('Estée Lauder Companies', 'Global group', 'United States', '2014'),
    'Jo Malone London': ('Estée Lauder Companies', 'Global group', 'United Kingdom', '1999'),
    'Cire Trudon': (None, None, 'France', None),
    'Poltronova': (None, 'Independent', 'Italy', None),
    'Grannas A. Olssons Hemslöjd': (None, 'Independent', 'Sweden', None),
}
def apply_own(e):
    o = OWN.get(e.get('mk'))
    if o and 'own' not in e:
        if o[0]: e['own'] = o[0]
        if o[1]: e['tier'] = o[1]
        if o[2]: e['cty'] = o[2]
        if o[3]: e['own_y'] = o[3]

COUNTRY = {  # g for vase entries
    'Aalto vase': 'Finland', 'Fazzoletto': 'Italy', 'Bacchantes': 'France', 'Graal vase': 'Sweden', 'Ariel vase': 'Sweden',
    'Banjo vase': 'United Kingdom', 'Hobnail vase': 'United States', 'Snowball vase': 'Germany', 'Meiping': 'China',
    'Delft tulip vase': 'Netherlands', 'Portland vase': 'United Kingdom', 'Rimini Blu vase': 'Italy',
    'Blue-and-white prunus ginger jar': 'China', 'Albarello': 'Italy', 'Snuff bottle': 'China',
    'Venini stoppered bottle': 'Italy', 'Carnival glass': 'United States', 'Depression glass': 'United States',
    'Provence bowl': 'Denmark', 'Medici vase': 'Italy', 'Borghese vase': 'Italy', 'Crown paperweight': 'France',
    'Millville rose': 'United States',
}

# ---------- 1. Vases ----------
d = D[NAMES[0]]
d['note'] = "Organised shape of display piece, then named design by country; glass and ceramic houses link to the brand register."
for k in ['Glass vase', 'Porcelain vase', 'Earthenware & stoneware vase', 'Ginger jar', 'Apothecary jar',
          'Decorative bottle', 'Decorative bowl', 'Decorative urn', 'Glass paperweight']:
    kk = KINDS[k]
    for x in kk.get('x', []):
        if x['n'] in COUNTRY: x['g'] = COUNTRY[x['n']]
        apply_own(x)
    kk['xg'] = 'by country of origin'
    kk['nl'] = "One entry is a named vase, jar, bottle, bowl or paperweight design, or a defined historic type; sizes, colours and later productions are versions."
    kk['sel'] = ("No whole-space list of decorative vases exists. Entries follow design-history pages (Wikipedia, V&A, house histories) for named designs and types, with the Nordic and Italian glass houses first. "
                 "Covers %d named designs; the rest of the canon is not listed in one reference.") % len(kk.get('x', []))
g = KINDS['Glass vase']
aal = getx(g, 'Aalto vase')
aal['d'] = "Free-form wavy-walled glass vase designed by Alvar and Aino Aalto in 1936 for a Karhula-Iittala design competition; the design belonged to the factory."
aal['s'] = W + 'Savoy_Vase'
aal['v'][0]['d'] = "140 mm; original made in a wood mould that was burned away; shown at the 1937 Paris World's Fair"
aal['v'][1]['d'] = "smaller sizes pressed with visible seams, larger sizes seamless"
fz = getx(g, 'Fazzoletto')
fz['s'] = W + 'Paolo_Venini'
fz['d'] = "Handkerchief vase from the Fazzoletto series that Paolo Venini created with designer Fulvio Bianconi; the rim falls in soft folds."
fz['mk'] = 'Venini'
for x in g['x']: apply_own(x)
# Iittala/Aalto the Savoy vase
KINDS['Earthenware & stoneware vase']['x'] = [x for x in KINDS['Earthenware & stoneware vase']['x']]
# Birds by Toikka kind
shelf = SHELF['Glass paperweights']
shelf['n'] = 'Paperweights & glass figures'
shelf['t'] = "Solid glass pieces kept to be looked at: water-filled and millefiori paperweights, and blown glass animals; a porcelain figurine → F2."
shelf['ax'] = 'kinds by form: paperweight or glass figure'
shelf['k'].append({
    "n": "Glass bird & animal figure", "a": "art glass bird · glass figurine",
    "d": "Mouth-blown solid glass animal made to stand as an ornament.",
    "s": W + 'Oiva_Toikka',
    "nl": "One entry is a named glass figure series from a glassworks; single birds, years and colours are versions.",
    "sel": "No whole-space list exists. Entries follow the designer and maker pages (Oiva Toikka, Iittala); Covers 1 series.",
    "xg": "by country of origin",
    "x": [E("Birds by Toikka", "Collection of over 400 mouth-blown glass birds designed by Oiva Toikka for Iittala, made from 1972 until his death in 2019.",
            W + 'Oiva_Toikka', mk='Iittala', y='1972', g='Finland', dt='bird species · year of issue · colour',
            own='Fiskars', tier='National champion', cty='Finland', own_y='2007',
            v=[{"n": "Annual and limited birds", "mk": "Iittala", "y": "1972", "d": "over 400 designs made 1972–2019"}])],
    "tt": [["Material", ["Clear glass", "Coloured glass"]], ["Form", ["Bird", "Other animal"]]],
    "see": [["F2", "Porcelain figurine", "Lladró and Hummel figurines are collectible figurines in F2"]]})

# ---------- 2. Mirrors ----------
d = D[NAMES[1]]
d['note'] = "Commodity kinds; the only named entries are the first manufactured mirror and design-museum pieces."
wm = KINDS['Wall mirror']
wm['x'].insert(0, E("Çatalhöyük obsidian mirror", "Polished obsidian disc found at Çatalhöyük in Anatolia, the earliest known manufactured mirror.",
                    W + 'Mirror', y='c. 6000 BCE', g='Anatolia', role='origin', dt='polished obsidian'))
fm = KINDS['Floor mirror']
ul = getx(fm, 'Ultrafragola')
ul['d'] = "Wavy-edged mirror lit by neon, from Ettore Sottsass's Mobili Grigi series; catalogued by Design Museum Brussels (Poltronova edition, 1970)."
ul['s'] = 'https://collection.designmuseum.brussels/en/node/78364'
ul['mk'] = 'Poltronova'; ul['y'] = '1970'; ul['role'] = 'landmark'
apply_own(ul)
for k in ['Wall mirror', 'Floor mirror']:
    KINDS[k]['nl'] = "One entry is the first manufactured mirror, a named period type or a design held by a museum collection; frames, sizes and finishes are versions."
    KINDS[k]['sel'] = ("Commodity kind under the icon rule: one origin entry (Wikipedia, Mirror) and design pieces held by a museum collection (Design Museum Brussels). "
                       "Covers %d entries; the period types are named by dealer pages and are not a complete list." % len(KINDS[k]['x']))
    KINDS[k]['xg'] = 'by origin or era'
getx(wm, 'Sunburst mirror')['g'] = '17th century onward'
for x in wm['x']:
    x.setdefault('g', 'Europe')
for x in fm['x']:
    x.setdefault('g', 'Europe')
getx(wm, 'Adnet Circulaire')['g'] = 'France'
fm['x'][0]['g'] = 'Italy'

# ---------- 3. Candles ----------
d = D[NAMES[2]]
d['note'] = "Market-first: houses and groups are the named entries, with owner and tier; the market panel gives the company figures a fetched page states."
d['ms'] = [
    {"mkt": "Yankee Candle retail network", "who": "Yankee Candle (Newell Brands)", "share": "217 stores", "yr": 2025, "s": W + 'Yankee_Candle', "note": "store count as of July 2025, as the page states"},
    {"mkt": "Newell Brands revenue", "who": "Newell Brands (Yankee Candle, WoodWick, Chesapeake Bay Candle, Millefiori Milano)", "share": "US$8.13 billion", "yr": 2023, "s": W + 'Newell_Brands', "note": "whole-company revenue, not candles alone"},
    {"mkt": "Bath & Body Works net sales", "who": "Bath & Body Works", "share": "US$2.3 billion", "yr": 2006, "s": W + 'Bath_%26_Body_Works', "note": "whole-company net sales for the year to 28 January 2006"},
    {"mkt": "Bath & Body Works store network", "who": "Bath & Body Works", "share": "1,937 stores plus 596 partner-operated", "yr": 2026, "s": W + 'Bath_%26_Body_Works', "note": "as of 1 August 2026, as the page states"},
    {"mkt": "S. C. Johnson revenue", "who": "S. C. Johnson & Son (Glade, Beanpod Soy Candles, Oust)", "share": "US$11.2 billion", "yr": 2023, "s": W + 'S._C._Johnson_%26_Son', "note": "whole-company revenue"},
]
d['msum'] = ("The home-fragrance groups named on fetched pages are Newell Brands (Yankee Candle), S. C. Johnson (Glade), Estée Lauder (Jo Malone London, Le Labo), Bath & Body Works and Advent International (Air Wick). "
             "No page fetched states a brand's share of the candle or home-fragrance market, so the panel holds company totals and store counts only.")
cc = KINDS['Container candle']
for x in cc['x']: apply_own(x)
cc['x'].extend([
    E("White Barn candle", "Scented candle line that Bath & Body Works launched in 1999 as the White Barn Candle Company.", W + 'Bath_%26_Body_Works',
      mk='Bath & Body Works', y='1999', g='United States', own='Bath & Body Works, Inc.', tier='National champion', cty='United States'),
    E("Jo Malone London candle", "Candle from the London house founded by Jo Malone in 1990, known for perfumes, candles, bath products and room scents.", W + 'Jo_Malone_London',
      mk='Jo Malone London', y='1990', g='United Kingdom'),
    E("WoodWick", "Candle brand listed among Newell Brands' home fragrance brands.", W + 'Newell_Brands', mk='WoodWick', g='United States',
      own='Newell Brands', tier='Global group', cty='United States'),
    E("Chesapeake Bay Candle", "Candle brand listed among Newell Brands' home fragrance brands.", W + 'Newell_Brands', mk='Chesapeake Bay Candle', g='United States',
      own='Newell Brands', tier='Global group', cty='United States'),
    E("Millefiori Milano", "Home fragrance brand listed among Newell Brands' home fragrance brands.", W + 'Newell_Brands', mk='Millefiori Milano', g='Italy',
      own='Newell Brands', tier='Global group', cty='Italy'),
])
for x in cc['x']:
    if 'g' not in x: x['g'] = x.get('cty') or {'Voluspa': 'United States', 'Neom': 'United Kingdom'}.get(x.get('mk'), '')
    if not x['g']: x['g'] = 'France' if x.get('mk') in ('Diptyque', 'Cire Trudon') else 'Not stated'
getx(cc, 'Original Jar')['d'] = "Yankee Candle's classic scented candle in a lidded glass jar; the company was founded in 1969 in South Hadley, Massachusetts."
getx(cc, 'Original Jar')['y'] = '1969'
getx(cc, 'Baies')['d'] = "Diptyque's blackcurrant-and-rose scented candle in the house's oval-label glass; Diptyque had introduced scented candles by 1963."
cc['nl'] = "One entry is a scented candle line or house sold under its own name; sizes and vessels are versions."
cc['xg'] = 'by home country of the house'
cc['sel'] = ("Market-first: houses named on Wikipedia pages for Yankee Candle, Newell Brands, Bath & Body Works, Diptyque, Jo Malone London, Le Labo and Cire Trudon, plus the existing house lines. "
             "Covers %d lines of about 15 houses named; no complete list of candle brands exists." % len(cc['x']))
rs = KINDS['Room spray']
rs['x'] = [
    E("Glade", "S. C. Johnson household air freshener introduced in 1956; sold as Brise in some markets, renamed Glade in Germany, France and the Netherlands in 2012.", W + 'Glade_(brand)',
      mk='Glade', y='1956', g='United States', own='S. C. Johnson & Son', tier='Global group', cty='United States'),
    E("Air Wick", "Air freshener introduced in the United States in 1943; Reckitt bought it in 1984 and Advent International took the business over on 31 December 2025.", W + 'Air_Wick',
      mk='Air Wick', y='1943', g='United States', own='Advent International', tier='Global group', cty='United States', own_y='2025',
      v=[{"n": "Reckitt ownership", "mk": "Reckitt & Colman", "y": "1984", "d": "bought from Ciba-Geigy"}]),
]
rs['nl'] = "One entry is an air-freshener or room-spray brand sold under its own name; scents, formats and refills are versions."
rs['xg'] = 'by home country of the brand'
rs['sel'] = "Market-first: the two global-group brands named on the S. C. Johnson, Glade and Air Wick pages. Covers 2 brands of about 2 named; no ranked list of room-spray brands was found."
for k in ['Candle holder', 'Catalytic fragrance lamp', 'Electric diffuser', 'Stick incense', 'Loose incense', 'Paste incense', 'Incense burner', 'Mabkhara']:
    kk = KINDS[k]
    kk['nl'] = "One entry is a named design, house line or traditional type of this kind; sizes and scents are versions."
    kk['sel'] = "No whole-space list exists. Entries follow the Wikipedia and maker pages cited on each entry. Covers %d entries; incense and holder canons are not listed in one reference." % len(kk.get('x', []))
    kk['xg'] = 'by origin'
    for x in kk.get('x', []):
        apply_own(x)
        x.setdefault('g', {'Nippon Kodo': 'Japan', 'Baieido': 'Japan', 'Kunmeido': 'Japan', 'Maison Berger Paris': 'France', 'Stoff': 'Denmark',
                            'Audo Copenhagen': 'Denmark', 'MUJI': 'Japan', 'Diptyque': 'France'}.get(x.get('mk'), 'Not stated'))
for kk in (cc,):
    pass

# ---------- 4. Seasonal, festive & folk ----------
d = D[NAMES[3]]
d['note'] = "Named folk objects are the entries, sectioned by region; craft traditions link to visual art (F2)."
FOLK = [["F2", "Folk craft tradition", "craft traditions are described in the visual-art taxonomy"]]
def folk(k, nl, sel, cov, see=True):
    k['nl'] = nl
    k['xg'] = 'by region'
    k['sel'] = sel + ' ' + cov
    if see:
        k['see'] = (k.get('see') or []) + FOLK

# Dala horse
dh = KINDS['Dala horse']
dh['x'].insert(0, E("Bergkarlås wooden horse", "Carved horse from Bergkarlås in Dalarna, where carving horses for a livelihood is thought to have begun; wooden horses for sale are recorded from 1623.",
                    W + 'Dalecarlian_horse', y='1623', g='Sweden (Dalarna)', role='origin', dt='unpainted or one colour'))
dh['x'][1]['g'] = 'Sweden (Dalarna)'
dh['x'][1]['d'] = "Pine horse carved in the Mora parish villages, now mainly Nusnäs, the centre of production; two-colour brushwork came from Stikå Erik Hansson of Risa in the 19th century."
dh['x'][1]['s'] = W + 'Dalecarlian_horse'
dh['x'].append(E("1939 New York World's Fair horse", "Dala horse chosen by architects Sven Markelius and Anders Beckman as the symbol of the Swedish pavilion; it introduced the horse to North America.",
                 W + 'Dalecarlian_horse', y='1939', g='Sweden (Dalarna)', role='landmark', dt='mass production began in the 1930s after the 1937 Paris exhibition'))
folk(dh, "One entry is a place or occasion in the history of the Dala horse; maker houses and sizes are versions.",
     "Follows Wikipedia's Dalecarlian horse article, which names the early villages, Nusnäs and the 1939 World's Fair.", "Complete: 3 of 3 stages named in the article (earliest villages, Nusnäs, 1939).")

# Matryoshka
ma = KINDS['Matryoshka']
ma['x'][0]['y'] = '1892'
ma['x'][0]['role'] = 'origin'
ma['x'][0]['d'] = "First Russian nesting set of eight dolls, designed by Sergey Malyutin and turned by Vasily Zvyozdochkin at the Children's Education Workshop, Moscow, in 1892."
for x in ma['x']: x['g'] = 'Russia'
folk(ma, "One entry is the original set or a regional matryoshka style named by the reference; piece counts and themes are versions.",
     "Follows Wikipedia's Matryoshka doll article.", "Complete: 5 of 5 sets and regional styles named in the article (the original, Sergiyev Posad, Semyonov, Polkhovsky Maidan, Kirov).")

# Nutcracker, smoker
nc = KINDS['Nutcracker figure']
for x in nc['x']:
    x['g'] = 'Germany (Erzgebirge)'
folk(nc, "One entry is a named nutcracker type or maker line; sizes and characters are versions.",
     "Follows Wikipedia's Nutcracker and the Erzgebirge maker pages cited on each entry.", "Covers %d entries; no complete list of nutcracker makers or characters exists." % len(nc['x']))
sm = KINDS['Smoking figure']
sm['x'][0]['d'] = "Two-part wooden figure that burns cone incense and breathes smoke from its mouth; first mentioned in 1850, from toy makers in the Ore Mountains."
sm['x'][0]['role'] = 'origin'
sm['x'][0]['s'] = W + 'R%C3%A4uchermann'
for x in sm['x']: x['g'] = 'Germany (Erzgebirge)'
folk(sm, "One entry is a form of smoking figure named by the reference; characters and sizes are versions.",
     "Follows Wikipedia's Räuchermann article.", "Complete: 4 of 4 forms the article names (Räuchermann, edge-sitter, Räucherfrau, multi-figure scene).")
for k in ['Christmas pyramid', 'Candle arch']:
    for x in KINDS[k]['x']: x['g'] = 'Germany (Erzgebirge)'
    folk(KINDS[k], "One entry is a named regional type of this Ore Mountains object; makers and sizes are versions.",
         "Follows the Wikipedia pages cited on each entry.", "Covers %d entries; no complete list of types exists." % len(KINDS[k]['x']))

# Easter eggs
ee = KINDS['Decorated Easter egg']
for x in ee['x']: x['g'] = 'Ukraine'
ee['x'][0]['d'] = "Ukrainian wax-resist egg written with beeswax, dyes applied from light to dark; added to the UNESCO Intangible Cultural Heritage list in 2024 (Ukraine and Estonia)."
ee['x'][0]['y'] = '2024'
ee['x'][0]['role'] = 'landmark'
ee['x'][0]['s'] = W + 'Pysanka'
ee['x'].extend([
    E("Krashanka", "Single-colour boiled egg, eaten after blessing and used in egg-tapping games.", W + 'Pysanka', g='Ukraine'),
    E("Pisanica", "Croatian decorated egg, often inscribed 'Sretan Uskrs' with doves, crosses and flowers; Međimurje used oak and soot for a dark brown dye.", W + 'Pysanka', g='Croatia'),
    E("Pisanka", "Polish decorated egg, blessed on Holy Saturday; regional forms include oklejanki (bulrush pith, Podlaskie) and nakleianki (glued, Łowicz).", W + 'Pysanka', g='Poland'),
    E("Suhorje pirihi", "Slovenian onion-skin-dyed egg with scratched designs from the Brkini Hills, added to Slovenia's heritage register in April 2022.", W + 'Pysanka', y='2022', g='Slovenia'),
    E("Drátenické kraslice", "Egg wrapped in wire, traditionally made by men in the Czech Republic and Slovakia.", W + 'Pysanka', g='Czech Republic and Slovakia'),
    E("Lemko and Boiko pin-drop egg", "Egg decorated by a drop-pull method with a pin instead of a stylus, giving dots, tears and commas.", W + 'Pysanka', g='Ukraine (Lemko and Boiko areas)'),
])
folk(ee, "One entry is a named decorated-egg type of a region; motifs and dyes are versions.",
     "Follows Wikipedia's Pysanka article, read to 100,000 characters of 162,291 (first part, which holds the regional list).",
     "Covers 9 types by region; the unread final part of the article (about 62,000 characters) was not searched for further types.")

# Kokeshi
ko = KINDS['Kokeshi']
for x in ko['x']:
    x['g'] = 'Japan (Tōhoku)' if x['n'] != 'Sōsaku kokeshi' else 'Japan (cities)'
    x['s'] = W + 'Kokeshi'
ko['x'][0]['role'] = 'origin'
ko['x'][0]['d'] = "First kokeshi were made by lathe artisans at Shinchi Shuraku near Tōgatta Onsen in Zaō, probably in the middle of the Edo period for hot-spring visitors."
folk(ko, "One entry is a traditional (dentō) kokeshi style tied to a hot-spring area, or the creative (sōsaku) kokeshi made after 1945; artists and sizes are versions.",
     "Follows Wikipedia's Kokeshi article.", "Complete: 10 of 10 traditional styles in the article's list, plus creative kokeshi (the article says eleven, its list shows ten).")

# Daruma
da = KINDS['Daruma']
for x in da['x']: x['g'] = 'Japan'; x['s'] = W + 'Daruma_doll'
da['x'][0]['d'] = "Papier-mâché charm from Shorinzan Daruma-ji in Takasaki, where the ninth priest Togaku had wooden moulds made around 1764–72; the city produces 80% of Japan's daruma."
da['x'][0]['role'] = 'origin'
da['x'].append(E("Gold daruma", "Daruma associated with luck in financial matters.", W + 'Daruma_doll', g='Japan'))
folk(da, "One entry is a named daruma type; eye-painting state and size are versions.",
     "Follows Wikipedia's Daruma doll article.", "Complete: 6 of 6 types in the article (Takasaki, triangle, goshiki, gold, Matsukawa, hime and onna).")

# New folk kinds
fshelf = SHELF['Folk dolls & figures']
def newkind(shelf, n, a, d, s, xs, nl, sel, cov, tt=None, see=True):
    k = {"n": n, "a": a, "d": d, "s": s, "x": xs, "tt": tt or [["Material", ["Wood", "Papier-mâché", "Ceramic"]]]}
    folk(k, nl, sel, cov, see)
    shelf['k'].append(k)
    return k
newkind(fshelf, "Alebrije", "Mexican alebrije", "Brightly painted fantastic creature, in papier-mâché from Mexico City or carved copal wood from Oaxaca.", W + 'Alebrije',
        [E("Linares alebrije", "Papier-mâché creatures made by Pedro Linares of Mexico City, who said he saw them while gravely ill.", W + 'Alebrije', mk='Pedro Linares', y='1936', g='Mexico (Mexico City)', role='origin', dt='cartonería'),
         E("Arrazola alebrije", "Carved copal-wood animals from Arrazola, Oaxaca, where Manuel Jiménez pioneered carving them; the village holds the Cuna de los Alebrijes festival in December.", W + 'Alebrije', g='Mexico (Oaxaca)'),
         E("San Martín Tilcajete alebrije", "Carved alebrijes from San Martín Tilcajete, Oaxaca, where Isidro Cruz helped build the craft; weekly market and annual Feria del Alebrije.", W + 'Alebrije', g='Mexico (Oaxaca)')],
        "One entry is an alebrije tradition tied to a maker or village; creature types and sizes are versions.",
        "Follows Wikipedia's Alebrije article, read to 100,000 characters of 109,921.", "Covers 3 traditions the article names (Mexico City, Arrazola, San Martín Tilcajete); the last 9,921 characters were not read.")
newkind(fshelf, "Maneki-neko", "lucky cat · beckoning cat", "Seated cat figure with a raised paw, displayed at shop entrances for good fortune.", W + 'Maneki-neko',
        [E("Marushime-neko", "Late-Edo maneki-neko of Imado ware, shown on sale at Sensō-ji in Hiroshige's 1852 print.", W + 'Maneki-neko', y='1852', g='Japan (Edo, Tokyo)', role='origin', dt='Imado ware'),
         E("Imado ware maneki-neko", "Cat figures of Imado ware from Edo, thought to descend from Imado dolls of the Genroku era (1688–1704).", W + 'Maneki-neko', g='Japan (Edo, Tokyo)'),
         E("Modern ceramic or plastic maneki-neko", "Ceramic or plastic cat with a raised paw, often holding a koban coin; battery and solar models wave an arm with an electromagnet.", W + 'Maneki-neko', g='Japan')],
        "One entry is a historic form of the maneki-neko; paw, colour and size are versions.",
        "Follows Wikipedia's Maneki-neko article.", "Covers 3 forms the article names; the article gives no complete list of regional variants.",
        tt=[["Raised paw", ["Left", "Right", "Both"]], ["Colour", ["White", "Black", "Red", "Gold", "Pink"]]])
newkind(fshelf, "Calavera", "sugar skull · Day of the Dead skull", "Skull or skeleton figure made for Day of the Dead, in sugar, clay, paper or print.", W + 'Calavera',
        [E("Sugar skull", "Skull moulded from sugar or clay (alfeñique), made as a treat for children and now used on ofrendas.", W + 'Calavera', g='Mexico'),
         E("Calavera Catrina", "Skeleton in a large feathered hat created by José Guadalupe Posada and developed into a full figure by Diego Rivera.", W + 'Calavera', g='Mexico', role='landmark')],
        "One entry is a named calavera type; materials and sizes are versions.",
        "Follows Wikipedia's Calavera article.", "Complete: 2 of 2 objects the article names (sugar skull, Calavera Catrina); the literary calavera is a poem, not an object.",
        tt=[["Material", ["Sugar", "Clay", "Paper"]]])
# Julbock, wycinanki
cshelf = SHELF['Christmas around the home']
newkind(cshelf, "Julbock", "Yule goat · Julbock straw goat", "Straw goat tied with red ribbons, placed on or under the Christmas tree.", W + 'Yule_goat',
        [E("Straw Yule goat", "Straw ornament tied with red ribbons, the modern form of the Scandinavian Yule goat.", W + 'Yule_goat', g='Sweden and Nordic countries'),
         E("Gävle Goat", "Giant straw goat erected in Gävle, Sweden, from 1966 and repeatedly targeted by vandals and arsonists.", W + 'Yule_goat', y='1966', g='Sweden')],
        "One entry is a named form of the Yule goat; sizes are versions.", "Follows Wikipedia's Yule goat article.", "Complete: 2 of 2 forms the article names.")
eshelf = SHELF['East Asian festival decor']
wy = {"n": "Wycinanki", "a": "Polish paper cutting · vytynanky", "d": "Paper cut-outs pasted on furniture or beams, hung in windows or given as gifts.",
      "s": W + 'Wycinanki', "x": [
          E("Kurpie wycinanki", "Single-colour cut-outs from the Kurpie region of Poland.", W + 'Wycinanki', g='Poland (Kurpie)'),
          E("Łowicz wycinanki", "Multicolour cut-outs from the Łowicz region of Poland.", W + 'Wycinanki', g='Poland (Łowicz)'),
          E("Vytsinanka", "Belarusian paper cutting, added to the UNESCO Intangible Cultural Heritage list in 2024.", W + 'Wycinanki', y='2024', g='Belarus', role='landmark')],
      "tt": [["Technique", ["Cutting", "Clipping", "Punching", "Tearing", "Layered (nalepianki)"]]]}
folk(wy, "One entry is a regional paper-cutting tradition; motifs and colours are versions.", "Follows Wikipedia's Wycinanki article.", "Covers 3 of about 4 regional traditions named (the article also names Ukrainian vytynanky without a distinct style).")
SHELF['Folk dolls & figures']['k'].append(wy)
SHELF['Folk dolls & figures']['t'] = "Dolls, figures and cut-outs from named folk traditions, sectioned by region; a doll made for play → Toys; the craft traditions link to visual art."

# East Asian entries get region
for k in ['New Year entrance decoration', 'Festival doll display']:
    for x in KINDS[k]['x']: x['g'] = 'Japan'
    KINDS[k]['xg'] = 'by region'; KINDS[k]['nl'] = "One entry is a named festival decoration type; sets and sizes are versions."
    KINDS[k]['sel'] = "Follows the Wikipedia pages cited on each entry. Covers %d entries; no complete list exists." % len(KINDS[k]['x'])
# Christmas and Halloween generic nl/sel
for k, v in KINDS.items():
    if v.get('x') and 'nl' not in v:
        v['nl'] = "One entry is a named design, maker line or historic type of this kind; sizes, colours and later productions are versions."
        v['sel'] = "No whole-space list exists. Entries follow the Wikipedia and maker pages cited on each entry. Covers %d entries; the rest of the canon is not listed in one reference." % len(v['x'])
        v['xg'] = v.get('xg') or 'by origin or era'
        for x in v['x']:
            apply_own(x)
            if 'g' not in x:
                x['g'] = x.get('mk') or 'Not stated'

# ---------- Party ----------
fc = KINDS['Firecracker & banger']
fc['x'].insert(0, E("Song dynasty bianpao", "Paper tubes filled with gunpowder, fused and linked in clusters ('whip cannon'), the first gunpowder firecrackers.", W + 'Fireworks',
                    y='960–1279', g='China', role='origin', dt='paper tube · gunpowder'))
# ---------- Garden ----------
gg = KINDS['Garden gnome']
th = gg['x'][0]
th['d'] = "Terracotta gnomes made by Philipp Griebel in Thuringia; the 21 he made were brought to Britain by Sir Charles Isham in 1847, and Gräfenroda became closely associated with gnome production from about 1860."
th['role'] = 'origin'; th['s'] = W + 'Garden_gnome'; th['g'] = 'Germany (Thuringia)'
la = getx(gg, 'Lampy')
la['d'] = "Sir Charles Isham's 1847 terracotta gnome, the only survivor of the original batch, displayed at Lamport Hall, Northamptonshire."
la['s'] = W + 'Garden_gnome'; la['g'] = 'United Kingdom'
for x in gg['x']: x.setdefault('g', 'Switzerland')
gg['x'].append(E("Gräfenroda gnome", "Garden gnome of Gräfenroda in Thuringia, a ceramics town closely tied to gnome production from about 1860.", W + 'Garden_gnome', y='c. 1860', g='Germany (Thuringia)'))
for k in ['Garden statue', 'Garden gnome', 'Lawn ornament', 'Gazing ball', 'Bird bath', 'Garden sundial', 'Wind chime', 'Wind spinner', 'Weathervane']:
    kk = KINDS[k]
    if not kk.get('x'): continue
    kk['nl'] = "One entry is a named garden-ornament type, historic form or maker line; sizes, materials and finishes are versions."
    kk['xg'] = 'by origin or era'
    for x in kk['x']:
        apply_own(x)
        x.setdefault('g', x.get('mk') or 'Not stated')
    kk['sel'] = ("Commodity plus icon rule: one origin entry where a fetched page names it, plus named historic types from Wikipedia pages cited on each entry. "
                 "Covers %d entries; no complete list exists." % len(kk['x']))
KINDS['Garden gnome']['sel'] = "Commodity plus icon rule: the origin entry follows Wikipedia's Garden gnome article (Griebel, Isham 1847, Gräfenroda). Covers 4 entries; the article also credits Baehr and Maresch of Dresden (1841) with the first gnomes, a contested claim not listed here."
# ---------- Flags ----------
D[NAMES[7]]['note'] = "National flags are content, not objects: the kinds stay as kinds and carry no named flags."
D[NAMES[4]]['note'] = (D[NAMES[4]].get('note') or "Fireworks, stage effects and party decorations.") + " The piñata is a toy in E1."
D[NAMES[5]]['note'] = "Commodity kinds; the Wikipedia article names no first artificial flower, so no origin entry is held."

# ---------- strip empties, write ----------
for k in KINDS.values():
    for x in k.get('x', []) or []:
        for v in x.get('v', []) or []:
            pass

brands = []
def B(n, c, f, d, s, own=None, tier=None, seg='Owner group'):
    b = {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": [], "eras": [], "sig": [], "sc": [], "rel": [], "s": s, "kf": "home fragrance"}
    if own: b['own'] = own
    if tier: b['tier'] = tier
    brands.append(b)
B("Newell Brands", "United States", "", "Owner of Yankee Candle, WoodWick, Chesapeake Bay Candle and Millefiori Milano; formed in 2016 when Newell Rubbermaid bought Jarden.", W + 'Newell_Brands')
B("Yankee Candle", "United States", "1969", "Scented-candle maker founded by Michael Kittredge II in South Hadley, Massachusetts; part of Newell Brands since 2016.", W + 'Yankee_Candle', 'Newell Brands', 'Global group', 'Mainstream')
B("S. C. Johnson & Son", "United States", "", "Owner of Glade, Pledge, Windex, Raid and Ziploc; revenue US$11.2 billion in 2023.", W + 'S._C._Johnson_%26_Son')
B("Glade", "United States", "1956", "S. C. Johnson household air freshener.", W + 'Glade_(brand)', 'S. C. Johnson & Son', 'Global group', 'Mainstream')
B("Advent International", "United States", "", "Investment firm that finalised its purchase of Reckitt's Essential Home business, including Air Wick, on 31 December 2025.", W + 'Air_Wick')
B("Estée Lauder Companies", "United States", "", "Owner of Jo Malone London (since 1999) and Le Labo (since 2014).", W + 'Jo_Malone_London')
B("Manzanita Capital", "United Kingdom", "", "London private equity firm that bought Diptyque in 2005.", W + 'Diptyque')
B("Fiskars", "Finland", "", "Owner of Iittala since 2007.", W + 'Iittala')
B("Damiani S.p.A.", "Italy", "", "Acquired Venini in 2016.", W + 'Paolo_Venini')
B("Rosendahl A/S", "Denmark", "", "Bought the Holmegaard brand in 2008.", W + 'Holmegaard_Glasværk')
B("Art & Fragrance (Lalique Group)", "Switzerland", "", "Wholly owned Cristal Lalique from 2010; rebranded Lalique Group in 2016.", W + 'Lalique')
B("Poltronova", "Italy", "", "Italian maker of the Ultrafragola mirror, Sottsass's Mobili Grigi series, 1970.", 'https://collection.designmuseum.brussels/en/node/78364')
B("WoodWick", "United States", "", "Candle brand owned by Newell Brands.", W + 'Newell_Brands', 'Newell Brands', 'Global group', 'Mainstream')
B("Chesapeake Bay Candle", "United States", "", "Candle brand owned by Newell Brands.", W + 'Newell_Brands', 'Newell Brands', 'Global group', 'Mainstream')
B("Millefiori Milano", "Italy", "", "Home fragrance brand owned by Newell Brands.", W + 'Newell_Brands', 'Newell Brands', 'Global group', 'Mainstream')
B("Bath & Body Works, Inc.", "United States", "1990", "Parent of Bath & Body Works, founded in New Albany, Ohio in 1990.", W + 'Bath_%26_Body_Works')

reg = {b['n'] for b in json.load(open('/home/user/Possession-Taxonomy/rebuild/out/B4_brands.json'))['b']}
brands = [b for b in brands if b['n'] not in reg]
bu = {
    "Bath & Body Works": {"own": "Bath & Body Works, Inc.", "tier": "National champion", "c": "United States"},
    "Jo Malone London": {"own": "Estée Lauder Companies", "tier": "Global group", "c": "United Kingdom"},
    "Le Labo": {"own": "Estée Lauder Companies", "tier": "Global group", "c": "United States"},
    "Diptyque": {"own": "Manzanita Capital", "tier": "Independent", "c": "France"},
    "Air Wick": {"own": "Advent International", "tier": "Global group", "c": "United States"},
    "Iittala": {"own": "Fiskars", "tier": "National champion", "c": "Finland"},
    "Lalique": {"own": "Art & Fragrance (Lalique Group)", "tier": "Independent", "c": "France"},
    "Cire Trudon": {"c": "France"},
}
bu = {k: v for k, v in bu.items() if k in reg}
renames = {}
part = {"replaces": NAMES, "depts": [D[n] for n in NAMES], "brands": brands, "brand_updates": bu, "renames": renames, "moves": []}
json.dump(part, open('/home/user/Possession-Taxonomy/rebuild/out/B4_parts/ALL.json', 'w'), ensure_ascii=False, indent=1)
print('removed m', removed_m)
print('size', len(json.dumps(part)))
