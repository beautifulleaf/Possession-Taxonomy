import json, re
P = '/home/user/Possession-Taxonomy/rebuild/out/B4_parts/ALL.json'
W = 'https://en.wikipedia.org/wiki/'
part = json.load(open(P))
D = {d['n']: d for d in part['depts']}
K = {}; S = {}
def reindex():
    K.clear(); S.clear()
    for d in part['depts']:
        for s in d['s']:
            S[s['n']] = s
            for k in s['k']:
                K[k['n']] = k
reindex()

def E(n, d, s, mk='', y='', g=None, a='', v=None, dt='', role=None, own=None, tier=None, cty=None, own_y=None):
    e = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}
    for k_, v_ in (('g', g), ('role', role), ('own', own), ('tier', tier), ('cty', cty), ('own_y', own_y)):
        if v_: e[k_] = v_
    return e
def addx(k, es):
    have = {x['n'].lower() for x in k.get('x', [])}
    for e in es:
        if e['n'].lower() not in have:
            k.setdefault('x', []).append(e)
def kind(shelf, n, d, s, xs, nl, sel, xg, tt, a='', see=None):
    k = {"n": n, "a": a, "d": d, "s": s, "x": xs, "nl": nl, "sel": sel, "xg": xg, "tt": tt}
    if see: k['see'] = see
    shelf['k'].append(k); K[n] = k; return k
FOLK = [["F2", "Folk craft tradition", "craft traditions are described in the visual-art taxonomy"]]

VA = W  # placeholder
# ---------- 1. Pysanka / Alebrije: read to the end ----------
ee = K['Decorated Easter egg']
addx(ee, [E("Podillya black-and-red egg", "Pysanka in the harsh black-and-red pairing used for serpent and goddess motifs.", W + 'Pysanka', g='Ukraine (Podillya)')])
ee['sel'] = ("Follows Wikipedia's Pysanka article, read to the end (162,291 characters). Complete: %d types named on the page (the Vegreville egg, Sorbian and Rusyn eggs are links without detail)." % len(ee['x']))
al = K['Alebrije']
al['sel'] = ("Follows Wikipedia's Alebrije article, read to the end (109,921 characters). Complete: 3 traditions the article names (Mexico City, Arrazola, San Martín Tilcajete); the rest of the page lists related crafts and museums.")
ma = K['Matryoshka']

# ---------- 2. Erzgebirge, Christmas, festival decor ----------
ore = S['Ore Mountains Christmas craft']
kind(ore, "Erzgebirge maker figure", "Hand-painted wooden figure or music box from a named Ore Mountains workshop.", W + 'Wendt_%26_K%C3%BChn',
     [E("Grünhainichen angel", "Wendt & Kühn angel with green wings and eleven white dots, from the firm founded in 1915 by Grete Wendt and Margarete Kühn at Grünhainichen; about 400 figures in the range.",
        W + 'Wendt_%26_K%C3%BChn', mk='Wendt & Kühn', y='1915', g='Germany (Erzgebirge)', dt='hand-painted wood · green wings · eleven white dots'),
      E("Wendt & Kühn flower children", "Hand-painted wooden flower-child figures, the firm's second best-known figure after the angels.", W + 'Wendt_%26_K%C3%BChn', mk='Wendt & Kühn', y='1915', g='Germany (Erzgebirge)'),
      E("Seiffen matchbox miniature", "'Miniature in a Matchbox' created at Seiffen in 1890 after an export tax change based on weight.", W + 'Seiffen', y='1890', g='Germany (Erzgebirge)'),
      E("Seiffen wooden toy", "Wooden toys from Seiffen, taken to the Nuremberg market by Johann Friedrich Hiemann in 1699 after mining declined.", W + 'Seiffen', y='1699', g='Germany (Erzgebirge)', role='origin')],
     "One entry is a named maker's figure line or a Seiffen toy type; characters and sizes are versions.",
     "Follows Wikipedia's Wendt & Kühn and Seiffen articles. Covers 4 entries; Steinbach and Ulbricht are held under Nutcracker figure, and no fetched page names their histories.",
     "by region", [["Material", ["Wood"]], ["Form", ["Angel", "Figure", "Music box"]]], see=FOLK)
for x in K['Erzgebirge maker figure']['x']:
    pass
getn = K['Nutcracker figure']
getn['sel'] += " Steinbach (1991) and Ulbricht (1928) rest on the earlier maker pages; their own histories could not be fetched."
K['Tree ornament']['x'][0]['s'] = W + 'Lauscha'
K['Tree ornament']['x'][0]['d'] = "Blown-glass baubles from Lauscha in Thuringia, a town known for glassblowing and for Christmas tree decorations."
K['Tree ornament']['x'][0]['g'] = 'Germany (Thuringia)'

home = S['Christmas around the home']
kind(home, "Nativity scene", "Crib or nativity model set up for Christmas, here as a named regional type.", W + 'Szopka',
     [E("Kraków szopka", "Nativity scene built with Kraków's historic buildings as backdrop, 19th-century tradition of masons and woodworkers; a competition since December 1937; UNESCO listed in 2018.",
        W + 'Szopka', y='19th century', g='Poland (Kraków)', role='landmark', dt='about 2 m high and 3 m wide · St Mary\'s Basilica most common model')],
     "One entry is a named regional nativity tradition; sizes and builders are versions.", "Follows Wikipedia's Szopka article. Complete: 1 of 1 tradition the article describes.", "by region",
     [["Material", ["Wood", "Cardboard", "Foil"]]], see=FOLK)
kind(home, "Christmas lantern", "Lantern hung at Christmas as a decoration, here as a named regional type.", W + 'Parol',
     [E("Parol", "Philippine Christmas lantern, from Spanish farol, adapted from the lit processions of Simbang Gabi; the five-pointed star came in the American period.", W + 'Parol', g='Philippines', dt='bamboo frame · Japanese or crepe paper · capiz shell'),
      E("Pampanga rotor parol", "Parol with a rotor system invented by Rodolfo David in 1957, sold commercially from 1964; San Fernando, Pampanga, is the home of the giant lanterns.", W + 'Parol', mk='Rodolfo David', y='1957', g='Philippines (Pampanga)', role='origin')],
     "One entry is a named parol type; sizes and light systems are versions.", "Follows Wikipedia's Parol article. Complete: 2 of 2 types the article names.", "by region",
     [["Frame", ["Bamboo", "Plastic", "Metal"]]], see=FOLK)
# Latin America and South Asia
sh = {"n": "Festival decor of Mexico and India", "t": "Cut paper, floor patterns and door hangings made for festivals in Mexico and India; a religious object for worship → Religious & Ceremonial Objects.", "k": []}
kind(sh, "Papel picado", "Tissue-paper banner cut with patterns, hung for festivals and on Day of the Dead altars.", W + 'Papel_picado',
     [E("Huixcolotla papel picado", "Papel de China cut with chisels in San Salvador Huixcolotla, Puebla, 'considered the birthplace of papel picado'; recognised as state heritage in 1998.", W + 'Papel_picado', y='mid-1800s', g='Mexico (Puebla)', role='origin'),
      E("Puebla and Tlaxcala papel picado", "Papel picado spread from Huixcolotla to Puebla and Tlaxcala around 1930, and reached Mexico City in the 1960s.", W + 'Papel_picado', y='c. 1930', g='Mexico (Puebla, Tlaxcala)')],
     "One entry is a regional papel picado tradition; patterns and colours are versions.", "Follows Wikipedia's Papel picado article. Complete: 2 of 2 regional traditions the article names.", "by region",
     [["Material", ["Tissue paper", "Plastic"]]], see=FOLK)
RANG = [("Raangoli", "Maharashtra"), ("Muggu", "Andhra Pradesh and Telangana"), ("Rangoli (Karnataka)", "Karnataka"), ("Kolam", "Tamil Nadu"), ("Mandana", "Rajasthan"),
        ("Alpana", "West Bengal and Bangladesh"), ("Aripan", "Bihar"), ("Muruja", "Odisha"), ("Chowkpurana", "Chhattisgarh"), ("Chowkpujan", "Uttar Pradesh"),
        ("Chowk poorana", "Punjab"), ("Pookkalam", "Kerala"), ("Saathiyo", "Gujarat"), ("Aipan", "Uttarakhand")]
kind(sh, "Rangoli", "Floor pattern made from rice flour, powder, sand or petals outside the entrance, mostly for festivals.", W + 'Rangoli',
     [E(n_, "Regional name and style of floor pattern: " + g_ + ".", W + 'Rangoli', g='India (%s)' % g_) for n_, g_ in RANG],
     "One entry is a regional name for floor pattern art; materials and motifs are versions.", "Follows Wikipedia's Rangoli article. Complete: 14 of 14 regional names in its list.", "by region",
     [["Material", ["Rice flour", "Coloured powder", "Sand", "Petals"]], ["Method", ["Dry", "Wet"]]], a='kolam · alpana · muggu', see=FOLK)
kind(sh, "Toran", "Door hanging of mango leaves and marigolds, or imitations in fabric and metal, as a symbol of good fortune.", W + 'Toran_(art)',
     [E("Mango-leaf and marigold toran", "Traditional toran of mango leaves and marigold garlands tied across a main entrance.", W + 'Toran_(art)', g='India'),
      E("Gujarat toran", "Embroidered cotton toran with mirror work; a 20th-century example is held by the Honolulu Museum of Art.", W + 'Toran_(art)', g='India (Gujarat)'),
      E("Thoranam", "South Indian form of the door hanging, in Tamil Nadu.", W + 'Toran_(art)', g='India (Tamil Nadu)')],
     "One entry is a regional toran type; materials and sizes are versions.", "Follows Wikipedia's Toran (art) article. Complete: 3 of 3 types it names (Gujarat, Rajasthan are noted without a distinct design).", "by region",
     [["Material", ["Mango leaf", "Marigold", "Fabric", "Metal", "Plastic"]]], see=FOLK)
# add shelf after East Asian festival decor
d = D["Seasonal, festive & folk decor"]
idx = [s['n'] for s in d['s']].index('East Asian festival decor') + 1
d['s'].insert(idx, sh)
# East Asian
east = S['East Asian festival decor']
cp = K['Spring Festival couplet']
cp['x'] = [E("Chunlian", "Spring couplet hung on door frames; the article credits Meng Chang, a Later Shu emperor (935–965), with an early example, and the custom spread widely in the Song dynasty.", W + 'Chinese_New_Year', y='935–965', g='China', role='origin')]
pc = K['Paper-cut window decoration']
pc['x'] = [E("Red window paper-cut", "Red paper-cut with auspicious themes pasted on windows and doors at Chinese New Year, such as the character 春 (spring).", W + 'Chinese_New_Year', g='China')]
for k_ in (cp, pc):
    k_['nl'] = "One entry is a named Chinese New Year decoration type; motifs are versions."
    k_['sel'] = "Follows Wikipedia's Chinese New Year article, read to 100,000 of 272,995 characters. Covers %d entry; the unread part, which holds nianhua, was not searched." % len(k_['x'])
    k_['xg'] = 'by region'
    k_['see'] = (k_.get('see') or []) + FOLK
kind(east, "Red lantern", "Red paper lantern hung at Chinese New Year; in the Nian myth the beast feared the colour red.", W + 'Chinese_New_Year',
     [E("Chinese New Year red lantern", "Red lantern hung with spring scrolls on windows and doors in the Nian myth.", W + 'Chinese_New_Year', g='China')],
     "One entry is a named lantern type for the festival; sizes are versions.", "Follows Wikipedia's Chinese New Year article. Covers 1 entry.", "by region", [["Material", ["Paper", "Silk", "Plastic"]]])
ENG = [("Kumade", "bamboo rake for raking in fortune"), ("Hagoita", "paddle that wards off evil, especially for girls"), ("Hamaya", "arrow that breaks evil"),
       ("Akabeko", "red cow of Aizu, Fukushima, that protects children"), ("Shisa", "Okinawan guardian lion that protects households from evil and fire"),
       ("Treasure ship", "ship of good dreams and fortune, crafted in Toyama Prefecture"), ("Koma spinning top", "top for things going smoothly"),
       ("Fukuwarai", "face game for laughter and good luck (Meiji period)"), ("Shimenawa", "rope for purification and a good New Year"), ("Koinobori", "carp streamers for a child's success (Edo period)")]
kind(east, "Engimono", "Lucky charm bought at a shrine, temple or new-year market, each tied to a wish.", 'https://en.thebecos.com/blogs/column/50-traditional-japanese-lucky-charms-and-their-origins',
     [E(n_, "Japanese lucky charm: " + d_ + ".", 'https://en.thebecos.com/blogs/column/50-traditional-japanese-lucky-charms-and-their-origins', g='Japan' + (' (Okinawa)' if n_ == 'Shisa' else ' (Fukushima)' if n_ == 'Akabeko' else '')) for n_, d_ in ENG],
     "One entry is a named lucky-charm object; sizes and paint styles are versions. Daruma, maneki-neko and hina dolls are held in their own kinds.",
     "Follows a retailer's list of 50 Japanese lucky charms, read to item 47 of 100,525 characters; it lists animals, plants and stones as well as objects. Covers 10 of 47 read items that are made objects; the others are creatures or materials, not made decor.", "by region",
     [["Material", ["Wood", "Papier-mâché", "Bamboo", "Ceramic"]]], see=FOLK)

# ---------- 3. Vases: design collections ----------
VAB = 'https://collections.vam.ac.uk/context/organisation/A455/venini'
LAB = 'https://collections.vam.ac.uk/context/organisation/A274/lalique-glassworks'
gv = K['Glass vase']
VEN = [("Thomas vase", "Thomas Stearns", "1961", "Italy"), ("Medusa vase", "Tapio Wirkkala", "c. 1966", "Italy"), ("Gondolieri vase", "Tapio Wirkkala", "1966", "Italy"),
       ("Patchwork vase", "Fulvio Bianconi", "1950", "Italy"), ("Inciso vase", "Paolo Venini", "1956", "Italy"), ("Occhi vase", "Tobia Scarpa", "c. 1959", "Italy"),
       ("Chinese vase", "Carlo Scarpa", "1938", "Italy"), ("Veronese vase", "Vittorio Zecchin", "1921", "Italy"), ("Simeon vase", "Marco Zanini", "1991", "Italy")]
ven_es = []
for n_, des, y_, g_ in VEN:
    s_ = 'https://collections.vam.ac.uk/item/O6116/gondolieri-vase-wirkkala-tapio/' if n_ == 'Gondolieri vase' else 'https://collections.vam.ac.uk/item/O6900/veronese-vase-zecchin-vittorio/' if n_ == 'Veronese vase' else VAB
    d_ = "Venini glass vase designed by %s, held by the V&A." % des
    if n_ == 'Gondolieri vase': d_ = "20 cm glass vase made on Murano by the incalmo technique, designed by Tapio Wirkkala for Venini; V&A CIRC.1062-1967."
    if n_ == 'Veronese vase': d_ = "Murano vase designed by Vittorio Zecchin in 1921 and made 1930–1935, inspired by Veronese's Annunciation; V&A CIRC.481-1971."
    ven_es.append(E(n_, d_, s_, mk='Venini', y=y_, g=g_, own='Damiani S.p.A.', tier='Independent', cty='Italy', own_y='2016'))
LAL = [("Ceylan vase", "1924"), ("Archers vase", "1921"), ("Oranges vase", "1926"), ("Bornéo vase", "1930"), ("Tanega vase", "1988"), ("Beauvais vase", "1931"),
       ("Actinia vase", "1934"), ("Thistles vase", "1926"), ("Oran vase", "1927"), ("Bay laurel vase", "1922")]
lal_es = [E(n_, "Lalique vase held by the V&A (%s)." % ("designed by Marie-Claude Lalique" if n_ == 'Tanega vase' else "designed by René Lalique"), LAB, mk='Lalique', y=y_, g='France',
            own='Art & Fragrance (Lalique Group)', tier='Independent', cty='France', own_y='2010') for n_, y_ in LAL]
SEG = E("9822 large blue-ruby vase", "Large blue-ruby glass vase by Flavio Poli for Seguso, Compasso d'Oro 1954; the jury praised its essential form and unity of colour, clarity and thickness.",
        'https://www.adidesignmuseum.org/en/collection/grande-vaso-in-vetro-blu-rubino-9822/', mk='Seguso', y='1954', g='Italy', role='landmark', dt='Compasso d\'Oro 1954 · ADI Design Museum collection')
addx(gv, ven_es + lal_es + [SEG])
fz = [x for x in gv['x'] if x['n'] == 'Fazzoletto'][0]
fz['v'].append({"n": "Handkerchief vase, V&A", "mk": "Venini", "y": "1949", "d": "designed by Fulvio Bianconi; held by the V&A"})
gv['sel'] = ("Follows the V&A's Venini (38 objects) and Lalique glassworks (47 objects) records, every vase listed on each; the ADI Design Museum's Compasso d'Oro collection (Seguso 9822, 1954); and the house pages already cited. "
             "Complete: %d named vases, the 9 Venini and 10 Lalique vases not already listed plus the Seguso vase; bowls, bottles, goblets and figures on those V&A pages are held under their own kinds or left out." % len(gv['x']))
gv['sel'] = re.sub(r'Complete: \d+ named', 'Complete: %d named' % len(gv['x']), gv['sel'])
# Omaggio
eth = K['Earthenware & stoneware vase']
addx(eth, [E("Omaggio vase", "Kähler stoneware-glaze vase designed by Ditte Reckweg and Jelena Schou Nordentoft of Stilleben, sold in H 20 cm and H 31 cm.",
             'https://www.connox.com/categories/accessories/home-decor/vases/kahler-design-omaggio-vase.html', mk='Kähler', g='Denmark', own='Rosendahl Design Group', tier='Independent', cty='Denmark', own_y='2018',
             dt='H 20 cm · H 31 cm')])
eth['x'][-1]['d'] = "Kähler vase designed by Ditte Reckweg and Jelena Schou Nordentoft of Stilleben, sold in H 20 cm and H 31 cm; the page gives no year or material."
# MoMA
MOMA = 'https://www.moma.org/collection/works/?q=vase&classifications=3'
shv = S['Vases']
M = [("Soft Vase", "Hella Jongerius", "1994", "Netherlands", 'seven records of the same design'),
     ("Colored Vase", "Hella Jongerius", "2010", "Netherlands", 'numbered 3/15, 6/15 and X/15'),
     ("The Honeycomb Vase 'Made by Bees'", "Tomáš Gabzdil Libertíny", "2006", "Netherlands", 'prototype'),
     ("Square Vase", "Ronan and Erwan Bouroullec", "1999", "France", ''),
     ("Grcic Vase", "Konstantin Grcic", "2000", "Germany", 'titled Vase'),
     ("Kom BV Vases", "Vincent de Rijk", "1986", "Netherlands", ''),
     ("Waterspout 4 Vase", "Toots Zynsky", "1994", "United States", ''),
     ("Flower Vase", "Shiro Kuramata", "1989", "Japan", ''),
     ("Petite Étrangeté Contre un Mur Vase", "Philippe Starck", "1988", "France", 'with Petite Étrangeté Sous un Mur Vase'),
     ("Crinkle Vase", "Makoto Komatsu", "1974–1979", "Japan", 'KNS-2, KNS-3, Super Bag V-1 and K-2'),
     ("'Big' Vase", "Jiří Pelcl", "2009", "Czech Republic", ''),
     ("Ovalis Vase", "Tapio Wirkkala", "1958", "Finland", ''),
     ("Yantra Vases (model Y31)", "Ettore Sottsass", "c. 1969", "Italy", ''),
     ("Shiva Vase", "Ettore Sottsass", "1973", "Italy", ''),
     ("Samos Vase (model U)", "Enzo Mari", "1973", "Italy", ''),
     ("Bambù Vases (model 3084)", "Enzo Mari", "1969", "Italy", ''),
     ("Vetro Soffiato Vase", "Lino Sabattini", "1973", "Italy", ''),
     ("Marco flower vase", "Sergio Asti", "1962", "Italy", "Compasso d'Oro 1962, producer Salviati & C.")]
mes = []
for n_, des, y_, g_, note in M:
    mes.append(E(n_, "Vase designed by %s, in MoMA's Design classification%s." % (des, (' (' + note + ')') if note else ''), MOMA, mk=des, y=y_, g=g_))
for e in mes:
    if e['n'] == 'Marco flower vase':
        e['s'] = 'https://www.adidesignmuseum.org/en/collection/marco-flower-vase/'
        e['d'] = "Flower vase designed by Sergio Asti for Salviati & C., Compasso d'Oro 1962; held in the ADI Design Museum collection."
        e['mk'] = 'Salviati & C.'; e['role'] = 'landmark'
STUDIO = [("Vase Form", "Paul Chaleff", "1984", "United States"), ("Pipe Vase", "Paul Chaleff", "1983", "United States"), ("Sliced Vase", "Paul Chaleff", "1980", "United States"),
          ("Monolith Wall Vase", "Otto Natzler", "1980", "United States"), ("Vase (Price)", "Ursula Morley Price", "1981", "United Kingdom"), ("Vase (Cash)", "Sydney Cash", "1981", "United States"),
          ("Solar Bronze Riser Vase", "Thomas Patti", "1978", "United States"), ("Vase (Patti)", "Thomas Patti", "1976", "United States"), ("Bud Vase", "Mary Rogers", "c. 1975", "United Kingdom"),
          ("Vase (Coper)", "Hans Coper", "c. 1963", "United Kingdom")]
for n_, des, y_, g_ in STUDIO:
    mes.append(E(n_, "Studio vase by %s, in MoMA's Design classification." % des, MOMA, mk=des, y=y_, g=g_))
kind(shv, "Design-collection vase", "Vase in a design museum's collection whose material the collection record does not fix here, mostly 1960s to 2010s design objects.", MOMA, mes,
     "One entry is a named vase design held by a design collection; numbered editions and prototypes are versions.",
     "Follows MoMA's Design classification search for 'vase' (178 works online), read through Firecrawl for the first window of 42 works; 'Show more' loads the rest and MoMA item pages return 403. Plus the ADI Design Museum's Compasso d'Oro record for the Marco vase. "
     "Covers %d designs from the first 42 of 178 MoMA results; the other 136 were not read." % len(mes),
     "by country of origin", [["Material", ["Glass", "Ceramic", "Metal", "Wax", "Plastic"]]],
     see=[["F2", "Studio pottery", "studio potters' vases (Coper, Natzler, Price) are collected as studio ceramics"]])
D["Vases & decorative glass and ceramics"]['note'] += " Compasso d'Oro winners found: Seguso 9822 (1954) and Marco (1962); the Design Museum (London) and Vitra pages fetched or found named no vases."

# ---------- 4. Candle market ----------
cd = D["Candles & home fragrance"]
cd['ms'] = [
    {"mkt": "US-led air care and candle category, by brand", "who": "Yankee Candle (Newell Brands)", "share": "20 %", "yr": 2020, "s": "https://www.berlinpackaging.com/air-care", "note": "Euromonitor International as cited by Berlin Packaging, published 13 April 2021; the page gives 2020 sales elsewhere but no explicit year for the shares"},
    {"mkt": "US-led air care and candle category, by brand", "who": "Bath & Body Works (L Brands)", "share": "18.7 %", "yr": 2020, "s": "https://www.berlinpackaging.com/air-care", "note": "same table"},
    {"mkt": "US-led air care and candle category, by brand", "who": "Glade (S. C. Johnson)", "share": "16.8 %", "yr": 2020, "s": "https://www.berlinpackaging.com/air-care", "note": "same table"},
    {"mkt": "US-led air care and candle category, by brand", "who": "Febreze (Procter & Gamble)", "share": "15.3 %", "yr": 2020, "s": "https://www.berlinpackaging.com/air-care", "note": "same table"},
    {"mkt": "US-led air care and candle category, by brand", "who": "Air Wick (Reckitt Benckiser)", "share": "10.4 %", "yr": 2020, "s": "https://www.berlinpackaging.com/air-care", "note": "same table; company shares were Newell 20 %, L Brands 18.7 %, S. C. Johnson 16.8 %, P&G 15 %, Reckitt 11.4 %"},
    {"mkt": "US home fragrance sales by product", "who": "Candles", "share": "more than 41 %", "yr": 2017, "s": "https://klinegroup.com/beauty-and-wellbeing/the-u-s-home-fragrances-market-senses-high-growth-by-embracing-e-commerce-and-new-formats/", "note": "Kline Group, share of overall market sales; Yankee Candle named category leader"},
    {"mkt": "Bath & Body Works net sales", "who": "Bath & Body Works, Inc.", "share": "US$7,291 million", "yr": 2025, "s": "https://seekingalpha.com/pr/20423305", "note": "whole-company net sales for the year ended 31 January 2026, down 0.2 % from US$7,307 million"},
    {"mkt": "Bath & Body Works store network", "who": "Bath & Body Works, Inc.", "share": "1,927 company-operated and 573 partner-operated stores", "yr": 2026, "s": "https://seekingalpha.com/pr/20423305", "note": "as of 31 January 2026"},
    {"mkt": "Reckitt Essential Home (Air Wick, Calgon, Woolite, Cillit Bang)", "who": "Reckitt, sold to Advent International", "share": "£2.0 billion", "yr": 2024, "s": "https://www.ajbell.co.uk/news/articles/reckitt-sells-essential-home-unit-advent-48-billion-deal", "note": "net revenue, about 14 % of Reckitt; US$4.8 billion enterprise value; Reckitt keeps 30 %"},
    {"mkt": "Newell Brands revenue", "who": "Newell Brands (Yankee Candle, WoodWick, Chesapeake Bay Candle, Millefiori Milano)", "share": "US$8.13 billion", "yr": 2023, "s": W + 'Newell_Brands', "note": "whole-company revenue; the Newell 2025 release returned 403 and a search excerpt gave US$7.2 billion for 2025, not a fetched page"},
    {"mkt": "Yankee Candle retail network", "who": "Yankee Candle (Newell Brands)", "share": "217 stores", "yr": 2025, "s": W + 'Yankee_Candle', "note": "as of July 2025"},
    {"mkt": "S. C. Johnson revenue", "who": "S. C. Johnson & Son (Glade, Beanpod Soy Candles, Oust)", "share": "US$11.2 billion", "yr": 2023, "s": W + 'S._C._Johnson_%26_Son', "note": "whole-company revenue"},
]
cd['msum'] = ("Euromonitor figures cited by Berlin Packaging put Yankee Candle at 20 % and Bath & Body Works at 18.7 % of the US-led air care and candle category (around 2020), ahead of Glade 16.8 %, Febreze 15.3 % and Air Wick 10.4 %. "
              "Kline put candles at over 41 % of US home fragrance sales in 2017. Company reports give totals only: Bath & Body Works US$7,291 million (year to January 2026) and Reckitt Essential Home £2.0 billion (2024). "
              "Newell's and S. C. Johnson's candle sales are not broken out on any fetched page.")
rs = K['Room spray']
addx(rs, [E("Febreze", "Procter & Gamble air freshener brand; 15.3 % of the air care and candle category in the Euromonitor table cited by Berlin Packaging.", "https://www.berlinpackaging.com/air-care",
            mk='Febreze', g='United States', own='The Procter & Gamble Company', tier='Global group', cty='United States')])
aw = [x for x in rs['x'] if x['n'] == 'Air Wick'][0]
aw['d'] = "Air freshener introduced in the United States in 1943; Reckitt bought it in 1984, and in 2025 Advent International took a majority of Reckitt's Essential Home business, Reckitt keeping 30 %."
aw['s'] = W + 'Air_Wick'
rs['sel'] = "Market-first: the brands in the Euromonitor table cited by Berlin Packaging and the Glade and Air Wick pages. Covers 3 brands; Yankee Candle, Bath & Body Works and Glade appear there as candle and air-care brands."
yc = [x for x in K['Container candle']['x'] if x['n'] == 'Original Jar'][0]
yc['d'] += " Euromonitor (cited by Berlin Packaging) gives the brand 20 % of its category."

# ---------- 5. Owners ----------
OWN2 = {
    'Orrefors': (None, None, 'Sweden', None),
    'Meissen': ('Free State of Saxony', 'Independent', 'Germany', '1991'),
    'Cire Trudon': (None, None, 'France', None),
    'Maison Berger Paris': ('Emosia Group', 'Independent', 'France', None),
    'Kähler': ('Rosendahl Design Group', 'Independent', 'Denmark', '2018'),
}
for k in K.values():
    for x in k.get('x', []):
        o = OWN2.get(x.get('mk'))
        if o:
            if o[0]: x['own'] = o[0]
            if o[1]: x['tier'] = o[1]
            if o[2]: x['cty'] = o[2]
            if o[3]: x['own_y'] = o[3]
        if x.get('mk') == 'Orrefors':
            x['d'] += " Orrefors glassworks founded 1889, Sweden; the page says it closed in 2012."
        if x.get('mk') == 'Meissen':
            x['s'] = x['s']
reg = {b['n'] for b in json.load(open('/home/user/Possession-Taxonomy/rebuild/out/B4_brands.json'))['b']}
newb = []
def B(n, c, f, d, s, own=None, tier=None, seg='Owner group'):
    if n in reg or n in {b['n'] for b in part['brands']}: return
    b = {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": [], "eras": [], "sig": [], "sc": [], "rel": [], "s": s, "kf": "home decor"}
    if own: b['own'] = own
    if tier: b['tier'] = tier
    part['brands'].append(b)
B("Kähler", "Denmark", "1839", "Ceramics house founded in Næstved by Joachim Christian Herman Kähler; sold to Næstved Municipality in 1974, to Frantz Longhi in 2007 and to Rosendahl Design Group in 2018.", W + 'K%C3%A4hler_Keramik', 'Rosendahl Design Group', 'Independent')
B("Rosendahl Design Group", "Denmark", "", "Owner of Kähler from 2018; Rosendahl A/S also bought Holmegaard in 2008.", W + 'K%C3%A4hler_Keramik')
B("Emosia Group", "France", "", "Owner of Maison Berger Paris; Argos-backed since 2017.", 'https://argos.fund/?p=1916')
B("The Procter & Gamble Company", "United States", "", "Owner of Febreze.", 'https://www.berlinpackaging.com/air-care')
B("Free State of Saxony", "Germany", "", "Owner of the Meissen porcelain manufactory since 1991.", W + 'Meissen_porcelain')
B("Wendt & Kühn", "Germany", "1915", "Grünhainichen maker of hand-painted wooden angels and flower children, founded by Grete Wendt and Margarete Kühn.", W + 'Wendt_%26_K%C3%BChn', None, None, 'Mainstream') if 'Wendt & Kühn' not in reg else None
part['brand_updates'].update({
    "Meissen": {"own": "Free State of Saxony", "tier": "Independent", "c": "Germany"},
    "Orrefors": {"c": "Sweden"},
    "Maison Berger Paris": {"own": "Emosia Group", "tier": "Independent", "c": "France"},
    "Wendt & Kühn": {"c": "Germany"},
})
part['brand_updates'] = {k: v for k, v in part['brand_updates'].items() if k in reg}
# ---------- coverage line recount ----------
def recount(k):
    n = len(k.get('x', []))
    k['sel'] = re.sub(r'Covers \d+ (named designs|entries|lines|entry|brands|designs)', lambda m: 'Covers %d %s' % (n, 'entry' if n == 1 and m.group(1) in ('entries', 'entry') else m.group(1) if m.group(1) != 'entry' else 'entries'), k['sel']) if 'Covers' in k.get('sel', '') else k.get('sel')
for name in ['Earthenware & stoneware vase', 'Container candle', 'Tree ornament', 'Nutcracker figure']:
    recount(K[name])
part['depts'] = part['depts']
json.dump(part, open(P, 'w'), ensure_ascii=False, indent=1)
print('size', len(json.dumps(part)))
