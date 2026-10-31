import json, copy, os
SRC = '/home/user/Possession-Taxonomy/rebuild/out/A3.json'
OUT = '/home/user/Possession-Taxonomy/rebuild/out/A3_parts/ALL.json'
d = json.load(open(SRC))
brands_old = {b['n'] for b in json.load(open('/home/user/Possession-Taxonomy/rebuild/out/A3_brands.json'))['b']}

REPL = [dp['n'] for dp in d['depts']]
WIKI = 'https://en.wikipedia.org/wiki/'

# ---------- market data from fetched pages ----------
HOUSE = {
 'Cartier': ('Richemont', 'Global group', 'France', ''),
 'Van Cleef & Arpels': ('Richemont', 'Global group', 'France', '1999'),
 'Chaumet': ('LVMH', 'Global group', 'France', '1999'),
 'Messika': ('Messika', 'Independent', 'France', ''),
 'Bulgari': ('LVMH', 'Global group', 'Italy', '2011'),
 'Pomellato': ('Kering', 'Global group', 'Italy', '2013'),
 'Tiffany & Co.': ('LVMH', 'Global group', 'United States', '2021'),
 'David Yurman': ('David Yurman', 'Independent', 'United States', ''),
 'Chopard': ('owner not stated', 'Independent', 'Switzerland', ''),
 'Piaget': ('Richemont', 'Global group', 'Switzerland', '1988'),
 'Pandora': ('Pandora', 'Global group', 'Denmark', ''),
 'Swarovski': ('Swarovski', 'Global group', 'Austria', ''),
 'Boucheron': ('Kering', 'Global group', 'France', ''),
}

def mkt(x):
    h = HOUSE.get(x.get('mk', ''))
    if h:
        x['own'], x['tier'], x['cty'], = h[0], h[1], h[2]
        if h[3]:
            x['own_y'] = h[3]

# ---------- clean existing departments ----------
removed_m = []
cov_notes = {}
for dp in d['depts']:
    dp.pop('b', None) if False else None
    for sh in dp['s']:
        for k in sh['k']:
            if k.get('m'):
                removed_m.append((dp['n'], k['n'], k['m']))
            k.pop('m', None)
            xs = k.get('x') or []
            for x in xs:
                mkt(x)
                x.setdefault('v', [])
            if xs:
                k['nl'] = ('One entry is a named jewellery line or design that a buyer asks for by name; sizes, metals and '
                           'stone variants are versions.')
                k['sel'] = ('No whole-space reference exists for this kind. Entries are the lines and designs named by the pages '
                            'cited on each entry. Covers %d lines named by those pages, not a total.' % len(xs))
                k['xg'] = 'by house or maker'

# ---------- Cartier Love pendant model becomes a version in the houses department ----------

def ent(n, mk, s, y='', d_='', g='', a='', v=None, role=None):
    e = {'n': n, 'mk': mk, 's': s, 'v': v or [], 'g': g}
    if y: e['y'] = y
    if d_: e['d'] = d_
    if a: e['a'] = a
    if role: e['role'] = role
    mkt(e)
    return e

def ver(n, d_='', y='', mk=''):
    r = {'n': n, 'y': y, 'd': d_}
    if mk: r['mk'] = mk
    return r

# ---------- Rings: stone cuts ----------
CUT = WIKI + 'Diamond_cut'
hist = [
 ('Point cut', 'mid-14th century', '', 'origin'), ('Table cut', 'mid-15th century', '', None),
 ('Old single cut', '', 'Also called the old eight cut.', None),
 ('Pendeloque', 'c. 1476', 'Briolette-type cut credited on the page to Lodewyk van Bercken.', None),
 ('Rose cut', 'mid-16th century', 'Introduced in Antwerp.', None),
 ('Mazarin cut', 'mid-17th century', '', None), ('Peruzzi cut', '', 'Triple-cut brilliant credited to Vincent Peruzzi.', None),
 ('Old mine cut', 'early 18th century', 'Cushion-shaped cut, common by the early 18th century.', None),
 ('Old European cut', 'c. 1870', 'Credited to Henry Dutton Morse.', None),
 ('Mogul cut', '', '', None), ('Lasque cut', '', '', None), ('Carré cut', '', '', None)]
mod = [
 ('Round brilliant', 'c. 1900', 'Developed around 1900 and analysed by Marcel Tolkowsky in 1919.', 'landmark'),
 ('Princess cut', '1960', 'Credited to A. Nagy of London.', None),
 ('Princess 144', '1960s', '', None), ('Oval brilliant', '1960s', 'Credited to Lazare Kaplan.', None),
 ('Barion cut', '1971', 'Credited to Basil Watermeyer.', None), ('Passion cut', '2009', 'Patented by Yariv Har.', None),
 ('High-Light cut', '', 'Credited to M. Westreich.', None), ('King cut', '', '', None), ('Magna cut', '', '', None),
 ('Radiant cut', '', '', None), ('Asscher cut', '', '', None), ('Emerald cut', '', '', None), ('Baguette cut', '', '', None),
 ('Marquise cut', '', '', None), ('Heart cut', '', '', None), ('Trilliant cut', '', '', None), ('Pear cut', '', '', None),
 ('Flanders cut', '', '', None)]
cut_x = []
for n, y, dd, role in hist:
    cut_x.append(ent(n, '', CUT, y, dd, 'Historic cuts', role=role))
for n, y, dd, role in mod:
    cut_x.append(ent(n, '', CUT, y, dd, 'Modern cuts', role=role))
cut_kind = {
 'n': 'Stone cut',
 'a': 'diamond cut · gem cut · stone shape',
 'd': 'Shape and facet pattern a stone is cut to; the cut is declared once for every stone-set ring, earring and pendant.',
 's': CUT,
 'nl': 'One entry is a named cut of diamond or gemstone, listed as historic or modern; settings are on the ring kinds, not here.',
 'sel': ("Every cut named in the historic and modern cut lists of Wikipedia's Diamond cut article as returned by the fetch (%d of them: %d historic, %d modern). "
         "Complete: %d of %d in that article's two lists; fancy-cut variants such as the cut-cornered cushion are not separate entries there."
         % (len(cut_x), len(hist), len(mod), len(cut_x), len(cut_x))),
 'xg': 'by historic or modern period',
 'x': cut_x,
 'tt': [['Outline', ['Round', 'Square', 'Rectangular', 'Oval', 'Pear', 'Heart']],
        ['Facet style', ['Brilliant', 'Step', 'Mixed', 'Rose']]],
 'see': [['A3', 'Solitaire ring', 'cut shown in the centre stone'], ['A3', 'Halo ring', 'centre stone cut']],
}
rings = next(dp for dp in d['depts'] if dp['n'] == 'Rings')
rings['s'].append({'n': 'Stone cuts', 't': 'The cuts a stone is shaped to before it is set, as a canon of named cuts; the setting is on the ring kinds.', 'k': [cut_kind]})

# ---------- Traditional: new kinds ----------
trad = next(dp for dp in d['depts'] if dp['n'] == 'Traditional & regional jewellery')
NA = WIKI + 'Native_American_jewelry'
na_kinds = [
 ('Concho belt', 'conchas · conchos', 'Belt of metal discs; the page places it with the Navajo.', 'Navajo, Southwest'),
 ('Bolo tie', 'bola tie', 'Cord tie with a decorated slide; the page names the Navajo, Hopi and San Carlos Apache.', 'Navajo, Hopi, San Carlos Apache'),
 ('Hair pipe breastplate', '', 'Breastplate of long tubular beads; the page places it on the Plains.', 'Plains'),
 ('Heishe necklace', 'heishi', 'Necklace of thin shell or stone discs, listed under Santo Domingo (Kewa Pueblo).', 'Kewa Pueblo, Southwest'),
 ('Shell gorget', '', 'Engraved shell pendant of the Southeastern Woodlands, listed for the Muscogee, Chickasaw and Cherokee.', 'Southeastern Woodlands'),
 ('Dentalium necklace', '', 'Necklace of dentalium shell, listed for the Kwakwakaʼwakw and Nuu-chah-nulth.', 'Northwest Coast'),
 ('Wampum', '', 'Shell-bead work listed for the Northeastern Woodlands (Wampanoag).', 'Northeastern Woodlands'),
]
na_shelf = {'n': 'Native American jewellery',
            't': 'Forms named for a Native American people or region and listed by the page cited; the squash blossom necklace is under European, American & Oceanic jewellery.',
            'ax': 'Which people or region does the form belong to: Southwest, Plains, Woodlands or Northwest Coast?',
            'k': [{'n': n, 'a': a, 'd': dd, 's': NA, 'see': [] } for n, a, dd, g in na_kinds]}
for k in na_shelf['k']:
    k.pop('see')
trad['s'].append(na_shelf)
BER = WIKI + 'Jewellery_of_the_Berber_cultures'
af = next(sh for sh in trad['s'] if sh['n'] == 'African jewellery')
af['k'] += [
 {'n': 'Khamsa', 'a': 'khmissa · hamsa', 'd': 'Hand-shaped amulet worn in the Maghreb; the page lists it for Morocco, Algeria and Tunisia.', 's': BER},
 {'n': 'Cross of Trarza', 'a': '', 'd': 'Cross pendant of Mauritania and the western Sahara.', 's': BER},
 {'n': 'Tizerzaï', 'a': '', 'd': 'Maghreb Berber jewellery form named on the page; the page names no single region for it.', 's': BER},
]
sa = next(sh for sh in trad['s'] if sh['n'] == 'South Asian jewellery')
sa['k'].append({'n': 'Jadanagam', 'a': '', 'd': 'South Indian hair adornment.', 's': 'https://krishnapearls.com/blogs/article/36-types-indian-jewellery'})
# coverage lines on the regional kinds that carry entries
for sh in trad['s']:
    for k in sh['k']:
        if k.get('x'):
            k['nl'] = 'One entry is a named design or type of one regional form; maker, size or metal variants are versions.'
            k['sel'] = ('Types named by the pages cited on each entry; no whole-space list exists for regional jewellery. Covers %d types named by those pages, not a total.' % len(k['x']))
            k['xg'] = 'by people or region'
trad['note'] = ('Forms from fetched lists: Wikipedia Native American jewelry (31 forms listed; 7 added here as kinds, squash blossom, naja and bolo tie already held), '
                'Wikipedia Jewellery of the Berber cultures (first 100,000 characters), the 36-type Indian jewellery guide, Wikipedia Claddagh ring. '
                'Techniques (kundan, jadau, polki, meenakari, temple, Zuni inlay, filigree) live in the traditions register; craft traditions link to visual art.')

# ---------- New department: houses & collections ----------
CAR = 'https://www.cartier.com/en-us/jewelry/collections'
CARW = WIKI + 'Cartier_(jeweler)'
VCA = 'https://www.vancleefarpels.com/us/en/collections/jewelry.html'
BUL = 'https://www.bulgari.com/en-us/jewelry'
BULW = WIKI + 'Bulgari'
TIF = 'https://www.tiffany.com/jewelry/shop/'
TIFW = WIKI + 'Tiffany_%26_Co.'
PAN = 'https://uk.pandora.net/en/collections/'
MES = 'https://www.messika.com/us_en'
CHO = 'https://www.chopard.com/intl/jewellery'

cartier_cur = ['Love', 'Juste un Clou', 'Clash de Cartier', 'Trinity', 'Panthère de Cartier', 'Grain de Café', "Cartier d'Amour",
               'Cartier Libre', 'Santos de Cartier', 'Maillon Panthère', 'C de Cartier', 'Agrafe', 'Les Berlingots de Cartier',
               'Tuttitutti', 'Écrou de Cartier']
cx = []
for n in cartier_cur:
    e = ent(n, 'Cartier', CAR, g='On the collections page')
    if n == 'Love':
        e['y'] = '1969'; e['d'] = 'Love bracelet, the line the Wikipedia Cartier article dates to 1969.'
        e['s'] = CARW
        e['v'] = [ver('LOVE pendant', 'Pendant version of the line.')]
        e['dt'] = 'bracelet · pendant'
    if n == 'Juste un Clou':
        e['y'] = '1971'; e['d'] = 'Nail-shaped line begun as a bracelet in 1971, per the Wikipedia Cartier article.'
        e['s'] = CARW
    cx.append(e)
for n, y, dd in [('Tank ring', '1996', 'Ring dated 1996 in the Wikipedia Cartier article.'),
                 ('Paris Nouvelle Vague', '1999', ''), ('Délices de Cartier', '2001', ''),
                 ('Le Baiser du Dragon', '2003', ''), ('Les Délices de Goa', '2003', '')]:
    cx.append(ent(n, 'Cartier', CARW, y, dd, 'Earlier lines named by Wikipedia'))
cart = {'n': 'Cartier jewellery lines', 'a': '',
        'd': 'The Paris maison’s jewellery collections page lists 18 collections; 15 are lines, and three are groupings (Diamond collection, Symbols and logos, Precious coloured stones).',
        's': CAR,
        'nl': 'One entry is a Cartier jewellery line a buyer asks for by name (Love, Trinity, Juste un Clou); a piece in it is not an entry.',
        'sel': "Every line on Cartier's own US jewellery collections page (15), then the earlier jewellery lines named in Wikipedia's Cartier article. The three grouping pages on the collections page are left out. Complete: 15 of 15 lines on the page.",
        'xg': 'by source: current collections page, earlier lines', 'x': cx,
        'see': [['A3', 'Bangle', 'Love and Juste un Clou bracelets'], ['A3', 'Solitaire ring', 'Solitaire 1895']]}

vca_names = ['Alhambra', 'Perlée', 'Frivole', 'Flowerlace', 'Flora', 'Fauna', 'Zodiaque', "Bouton d’or", 'Between the Finger Rings']
vx = []
for n in vca_names:
    e = ent(n, 'Van Cleef & Arpels', VCA, g='On the collections page')
    if n == 'Alhambra':
        e['v'] = [ver('Vintage Alhambra', 'Version name shown on the page for bracelet and pendant.')]
    vx.append(e)
vcak = {'n': 'Van Cleef & Arpels jewellery lines', 'a': '',
        'd': 'The Paris maison’s jewelry page names Alhambra, Perlée and Frivole as its iconic collections; Richemont bought the firm in 1999.',
        's': VCA,
        'nl': 'One entry is a Van Cleef & Arpels jewellery line; the vintage, magic and sweet size variants are versions.',
        'sel': "Every collection shown on the maison’s own US jewelry collections page (9); high jewellery, watches, engagement rings and fragrances are separate pages and are not listed. Complete: 9 of 9 on the page.",
        'xg': 'single section', 'x': vx, 'see': [['A3', 'Pendant', 'Alhambra pendants']]}

chx = []
for n, y, dd in [('Liens', '1970s', 'First Liens collection in the 1970s; the Lien ring dates to 1977.'),
                 ('Premiers Liens', '2007', 'Sub-line of Liens.'), ('Attrape-moi', '2007', ''),
                 ('Joséphine', '2010', ''), ('12 Vendôme', '2012', 'Created for the 26th Biennale des Antiquaires.'),
                 ('Bee my love', '', ''), ('Anneau', '', ''), ('Le Grand Frisson', '', ''), ('Class One', '', ''), ('Torsade', '', '')]:
    chx.append(ent(n, 'Chaumet', WIKI + 'Chaumet', y, dd, 'Named in Wikipedia'))
chk = {'n': 'Chaumet jewellery lines', 'a': '',
       'd': 'Paris jeweller bought by LVMH in October 1999; Investcorp had bought it in 1987.', 's': WIKI + 'Chaumet',
       'nl': 'One entry is a Chaumet jewellery line named by the cited article.',
       'sel': "Every collection named in Wikipedia's Chaumet article (10). The maison’s own collections page was not retrieved. Complete: 10 of 10 named in that article.",
       'xg': 'single section', 'x': chx}

mx = []
for n, sku in [('Move Classique', '15038 and 03995'), ('Move Uno', '15521 and 12113'), ('Move Noa', '10092 and 14481'),
               ('So Move', '12937 and 14966'), ('Baby Move', '04322')]:
    e = ent(n, 'Messika', MES, g='On the house page')
    e['v'] = [ver('Yellow gold', 'Metal listed in the page links.'), ver('White gold', 'Metal listed in the page links.'), ver('Rose gold', 'Metal listed in the page links.')]
    mx.append(e)
mesk = {'n': 'Messika jewellery lines', 'a': '',
        'd': 'Paris house founded in 2005 by Valérie Messika, known for diamonds set to move.', 's': MES,
        'nl': 'One entry is a Messika line (the Move family); the gold colour of a piece is a version.',
        'sel': "The five Move lines whose pieces appear on Messika’s own US page (the page links to product pages, not a collections list). Covers 5 lines; other Messika lines were not on the retrieved page.",
        'xg': 'single section', 'x': mx}

bx = []
bul = [('Serpenti', 'late 1940s', 'Snake motif begun on bracelet-watches in the late 1940s; emblem of the collection from 2009.',
        [ver('Serpenti Viper', 'Listed on the page as necklace, bracelet and earrings in yellow gold.')]),
       ('B.zero1', '1999', 'Ring launched in 1999.', [ver('Gold & Steel', 'Yellow gold and steel ring and bracelet.'), ver('Yellow gold'), ver('White gold'), ver('Rose gold')]),
       ("Divas' Dream", '', '', [ver('Rose gold, mother-of-pearl', 'Ring, necklace and bracelet listed on the page.')]),
       ('Bvlgari Tubogas', '', '', [ver('Gold & Steel', 'Bracelet and necklace listed on the page.')]),
       ('Bvlgari Bvlgari', '', 'The name first appears on a 1977 watch, per the Wikipedia article.', []),
       ('Bvlgari Eternal', '', '', []), ('Bvlgari Colors', '', '', []), ('Save the Children', '', '', []),
       ('Parentesi', '', 'Named in the Wikipedia Bulgari article, not on the current jewelry menu.', [])]
for n, y, dd, vv in bul:
    e = ent(n, 'Bulgari', BUL, y, dd, 'On the jewelry page' if n != 'Parentesi' else 'Named in Wikipedia', v=vv)
    if n in ('B.zero1', 'Serpenti', 'Bvlgari Bvlgari'):
        e['s'] = BULW if n != 'B.zero1' else BULW
    if n == 'Parentesi':
        e['s'] = BULW
    bx.append(e)
bulk = {'n': 'Bulgari jewellery lines', 'a': 'Bvlgari',
        'd': 'Rome jeweller bought by LVMH in an all-share deal completed on 4 October 2011.', 's': BUL,
        'nl': 'One entry is a Bulgari jewellery line; metals and finishes listed on the page are versions.',
        'sel': "Every line in the jewelry menu of Bulgari’s own US site (Serpenti, B.zero1, Divas’ Dream, Bvlgari Tubogas, Bvlgari Bvlgari, Bvlgari Eternal, Bvlgari Colors, Save the Children; ‘Other collections’ is a link without names), plus Parentesi from Wikipedia. Complete: 8 of 8 named in the menu.",
        'xg': 'by source: jewelry menu, Wikipedia', 'x': bx, 'see': [['A3', 'Pendant', "Serpenti and Divas' Dream pendants"]]}

pox = []
for n, y, dd in [('Pandora Moments', '', 'The collection of threaded charm bracelets and charms.'), ('Pandora Timeless', '', ''), ('Pandora ME', '', ''),
                 ('Pandora Talisman', '', ''), ('Pandora Essence', '', ''), ('Pandora Signature', '', '')]:
    pox.append(ent(n, 'Pandora', PAN, y, '', 'Core lines'))
pox[0].pop('d', None)
for n in ('Disney x Pandora', 'Marvel x Pandora'):
    pox.append(ent(n, 'Pandora', PAN, g='Licensed collaborations'))
pak = {'n': 'Pandora jewellery lines', 'a': '',
       'd': 'Copenhagen firm founded in 1982; its charm bracelets went on sale in 2000.', 's': PAN,
       'nl': 'One entry is a Pandora collection a buyer asks for by name; charms and bracelets inside it are not entries.',
       'sel': "Every collection on Pandora’s own UK collections page (8). Complete: 8 of 8 on the page.",
       'xg': 'by line type: core lines, licensed collaborations', 'x': pox, 'see': [['A3', 'Charm', 'Pandora charms']]}

tx = []
tif = [('Tiffany Lock', ''), ('Tiffany T', '2014'), ('Tiffany HardWear', '2017'), ('Tiffany Knot', ''), ('Bird on a Rock', ''),
       ('Sixteen Stone by Tiffany', ''), ('Return to Tiffany', ''), ('Elsa Peretti', ''), ('Paloma Picasso', ''), ('Tiffany Victoria', ''),
       ('Tiffany Titan by Pharrell Williams', ''), ('Tiffany 1837', ''), ('Tiffany Forever', ''), ('Tiffany Soleste', ''),
       ('Tiffany Together', ''), ('Tiffany True', '2018'), ('Ziegfeld Collection', ''), ('Tiffany Enamel', ''), ('Tiffany Keys', '2009')]
for n, y in tif:
    e = ent(n, 'Tiffany & Co.', TIF, y, g='On the jewelry page')
    if n in ('Tiffany T', 'Tiffany HardWear', 'Tiffany True', 'Tiffany Keys', 'Bird on a Rock'):
        e['s'] = TIFW
    if n == 'Tiffany True':
        e['d'] = 'Engagement ring design dated 2018 in the Wikipedia article.'
    if n == 'Bird on a Rock':
        e['d'] = 'A 2025 capsule marked the brooch’s 60th anniversary.'
    tx.append(e)
tx.append(ent('Paper Flowers', 'Tiffany & Co.', TIFW, '2018', '', 'Named in Wikipedia'))
blue = ent('Tiffany Blue Book', 'Tiffany & Co.', TIF, '2023', 'Annual high jewellery collection; the 2025 edition Sea of Wonder posted record sales, per LVMH.', 'On the jewelry page',
           v=[ver('Out of the Blue', '', '2023'), ver('Tiffany Celeste', '', '2024'), ver('Sea of Wonder', 'LVMH reported record-breaking sales.', '2025'), ver('Hidden Garden', '', '2026')])
tx.append(blue)
tifk = {'n': 'Tiffany & Co. jewellery lines', 'a': '',
        'd': 'New York jeweller; LVMH acquired a majority stake, completed on 7 January 2021.', 's': TIF,
        'nl': 'One entry is a Tiffany jewellery line or designer collection; each yearly Blue Book is a version of the Blue Book entry.',
        'sel': "Every collection in the Designer & Collection filter and High Jewelry menu of Tiffany’s own jewelry page (19 lines plus Blue Book), Paper Flowers from Wikipedia. Tiffany Rope is a watch collection and is left out. The Tiffany Setting and Elsa Peretti pieces are also in the ring and pendant kinds. Complete: 20 of 20 on the page.",
        'xg': 'by source: jewelry page, Wikipedia', 'x': tx, 'see': [['A3', 'Solitaire ring', 'Tiffany Setting'], ['A3', 'Pendant', 'Return to Tiffany, Open Heart']]}

yx = [ent('Cable', 'David Yurman', WIKI + 'David_Yurman', '', 'Signature form of the house; Rizzoli published David Yurman Cable in 2017.', 'Named in Wikipedia'),
      ent('Wedding Collection', 'David Yurman', WIKI + 'David_Yurman', '2006', '', 'Named in Wikipedia')]
yk = {'n': 'David Yurman lines', 'a': '', 'd': 'New York house founded in 1980 by David and Sybil Yurman; privately held.', 's': WIKI + 'David_Yurman',
      'nl': 'One entry is a David Yurman collection named by the cited article.',
      'sel': 'Collections named in Wikipedia’s David Yurman article (2). The house’s own collections page was not retrieved. Covers 2 named in the article, not a total.',
      'xg': 'single section', 'x': yx}

chp = []
for n in ['Happy Diamonds', 'Happy Hearts', 'Ice Cube', "L'Heure du Diamant", 'Precious Lace', 'Solitaire']:
    chp.append(ent(n, 'Chopard', CHO, g='In the collection filter'))
for n in ['Imperiale', 'Chopardissimo']:
    chp.append(ent(n, 'Chopard', CHO, g='Named in the page text'))
chk2 = {'n': 'Chopard jewellery lines', 'a': '', 'd': 'Swiss house whose jewellery page lists six collections in its filter and names two more in its text.', 's': CHO,
        'nl': 'One entry is a Chopard jewellery collection; the Happy Diamonds pendant is also under Pendant.',
        'sel': "Every collection in the filter of Chopard’s own jewellery page (6) and the two named in its page text. Complete: 8 of 8 on the page.",
        'xg': 'by position on the page', 'x': chp, 'see': [['A3', 'Pendant', 'Happy Diamonds pendant']]}
pgx = [ent(n, 'Piaget', WIKI + 'Piaget_SA', '1990s', '', 'Named in Wikipedia') for n in ('Possession', 'Limelight', 'Tanagra')]
pgk = {'n': 'Piaget jewellery lines', 'a': '', 'd': 'Swiss house bought by the Vendôme group (now Richemont) in 1988.', 's': WIKI + 'Piaget_SA',
       'nl': 'One entry is a Piaget jewellery line named by the cited article.',
       'sel': "The three 1990s jewellery lines in Wikipedia’s Piaget article (the article also names watch lines Altiplano, Polo, Dancer, Emperador, Black Tie, Miss Protocole, which are left out). The house’s own page was not retrieved. Covers 3, not a total.",
       'xg': 'single section', 'x': pgx}

pm = []
for n, y in [('Nudo', ''), ('Capri', ''), ('Sabbia', ''), ("M'Ama Non M'Ama", ''), ('Iconica', ''), ('Victoria', ''), ('Tango', ''), ('Pom Pom', '2007')]:
    pm.append(ent(n, 'Pomellato', WIKI + 'Pomellato', y, '', 'Named in Wikipedia'))
pk = {'n': 'Pomellato jewellery lines', 'a': '', 'd': 'Milan jeweller; Kering acquired it in July 2013.', 's': WIKI + 'Pomellato',
      'nl': 'One entry is a Pomellato collection named by the cited article.',
      'sel': "Every collection named in Wikipedia’s Pomellato article (8). The house’s own collections page was not retrieved. Complete: 8 of 8 named in that article.",
      'xg': 'single section', 'x': pm}

sw = [ent('Atelier Swarovski', 'Swarovski', WIKI + 'Swarovski', '', 'Designer label; the article cites a WWD report of 28 February 2014 on Viktor & Rolf designing for it.', 'Named in Wikipedia'),
      ent('Snowflake', 'Swarovski', WIKI + 'Swarovski', '2004', 'Pendant and brooch collection dated 2004 in an image caption.', 'Named in Wikipedia')]
swk = {'n': 'Swarovski jewellery lines', 'a': '', 'd': 'Austrian family-held company founded in 1895; its crystal business had about €2.7 billion sales in 2018.', 's': WIKI + 'Swarovski',
       'nl': 'One entry is a Swarovski jewellery collection named by the cited article.',
       'sel': "The two jewellery collections Wikipedia’s Swarovski article names. Swarovski’s own site returned no collection menu. Covers 2, not a total.",
       'xg': 'single section', 'x': sw}

houses = {
 'n': 'Jewellery houses & collections',
 'mode': 'variety',
 't': 'The lines a buyer asks for by name, such as Cartier Love or Van Cleef & Arpels Alhambra, grouped by the house’s country and then the house; the piece itself → the ring, earring, necklace or bracelet department.',
 'ax': 'Which house makes the line, and in which country is that house based?',
 'note': 'Lines come from each house’s own collections page where it could be fetched, otherwise from Wikipedia. Owner groups, tiers and market figures are in the market summary. Famous single stones are not possessions anyone buys and are left out.',
 'b': [{'m': 'House and ownership', 'v': 'house maison > group-owned lines > fashion-brand jewellery', 'w': 'Group ownership shows who stands behind the warranty and service network; worker to source.'}],
 's': [
  {'n': 'France', 't': 'Paris houses.', 'ax': 'Which Paris house makes the line?', 'k': [cart, vcak, chk, mesk]},
  {'n': 'Italy', 't': 'Houses based in Italy.', 'k': [bulk, pk]},
  {'n': 'United States', 't': 'Houses based in the United States.', 'k': [tifk, yk]},
  {'n': 'Switzerland', 't': 'Houses based in Switzerland.', 'k': [chk2, pgk]},
  {'n': 'Denmark', 't': 'Houses based in Denmark.', 'k': [pak]},
  {'n': 'Austria', 't': 'Houses based in Austria.', 'k': [swk]},
 ],
}
SM = 'https://theimpression.com/richemont-ends-fiscal-year-with-double-digit-growth/'
houses['ms'] = [
 {'mkt': 'Jewellery maisons of Richemont (Cartier, Van Cleef & Arpels, Buccellati, Vhernier)', 'who': 'Richemont', 'share': '€16.5 billion sales of €22.4 billion group sales', 'yr': 2026,
  's': SM, 'note': 'Year to 31 March 2026; up 14 % at constant rates; operating margin 30.5 % on €5 billion operating profit'},
 {'mkt': 'LVMH Watches & Jewelry business group (includes Tiffany and Bulgari)', 'who': 'LVMH', 'share': '€10.49 billion revenue', 'yr': 2025,
  's': 'https://www.nationaljeweler.com/articles/14647-tiffany-co-bulgari-sales-resilient-as-lvmh-s-2025-sales-slip', 'note': 'Down 1 % reported, up 3 % organic; the division also holds watch brands'},
 {'mkt': 'Pandora group revenue', 'who': 'Pandora', 'share': 'DKK 32,549 million', 'yr': 2025,
  's': 'https://pandoragroup.com/news/27811', 'note': '6 % organic growth; more than 2,800 concept stores within 7,000 points of sale in over 100 countries'},
 {'mkt': 'Pandora group revenue', 'who': 'Pandora', 'share': 'DKK 28.136 billion', 'yr': 2023,
  's': WIKI + 'Pandora_(jewelry)', 'note': 'Wikipedia cites Creditreports.dk; the page carries maintenance tags'},
 {'mkt': 'Chow Tai Fook Jewellery Group revenue', 'who': 'Chow Tai Fook', 'share': 'HK$94.4 billion (US$12.1 billion)', 'yr': 2026,
  's': 'https://idexonline.com/FullArticle?Id=51274', 'note': 'Year to 31 March 2026, up 5.3 %; 969 under-performing mainland points of sale closed'},
 {'mkt': 'Signet Jewelers revenue', 'who': 'Signet Jewelers', 'share': 'US$6.70 billion', 'yr': 2025,
  's': WIKI + 'Signet_Jewelers', 'note': 'Infobox figure; 2,642 locations; the page calls Signet the world’s largest retailer of diamond jewellery'},
 {'mkt': 'Swarovski group revenue', 'who': 'Swarovski', 'share': '€2.7 billion', 'yr': 2020,
  's': WIKI + 'Swarovski', 'note': 'Infobox figure citing a 2020 source'},
]
houses['msum'] = ("Three groups hold the big houses on the cited pages. Richemont’s jewellery maisons (Cartier, Van Cleef & Arpels, Buccellati, Vhernier) made €16.5 billion in the year to March 2026, "
                  "against €22.4 billion for the whole group. LVMH reports Tiffany, bought in 2021, and Bulgari, bought in 2011, with Chaumet (1999) inside a Watches & Jewelry division of €10.49 billion in 2025. "
                  "Kering formed Kering Jewelry for Boucheron, Pomellato (bought 2013), DoDo and Qeelin; the cited article gives no revenue. Outside the luxury groups: Pandora (DKK 32.5 billion, 2025), "
                  "Chow Tai Fook (HK$94.4 billion, year to March 2026), Signet (US$6.70 billion, 2025) and Swarovski (€2.7 billion, 2020). Independents named in the houses section are Messika, Chopard and David Yurman. "
                  "No fetched page gave a share of the whole jewellery market, so none is shown.")
d['depts'].append(houses)

# ---------- brands ----------
brands = []
def nb(n, c, seg, dd, s, kf=''):
    if n in brands_old:
        return
    brands.append({'n': n, 'c': c, 'f': '', 'seg': seg, 'd': dd, 'lines': [], 'eras': [], 'sig': [], 'sc': [], 'rel': [], 's': s, 'kf': kf})
nb('Richemont', 'Switzerland', 'Luxury house', 'Swiss group that owns Cartier, Van Cleef & Arpels, Buccellati and Vhernier.', SM, 'jewellery group')
nb('LVMH', '', 'Luxury house', 'Group that owns Tiffany & Co., Bulgari and Chaumet.', 'https://www.nationaljeweler.com/articles/14647-tiffany-co-bulgari-sales-resilient-as-lvmh-s-2025-sales-slip', 'jewellery group')
nb('Kering', '', 'Luxury house', 'Group that owns Boucheron, Pomellato, DoDo and Qeelin.', 'https://fashionunited.uk/news/business/kering-launches-dedicated-jewellery-division-to-accelerate-growth/2026031686907', 'jewellery group')
nb('Signet Jewelers', '', 'Mainstream', 'Largest retailer of diamond jewellery on the cited page; owner of Kay, Zales, Jared, Blue Nile, Ernest Jones and H. Samuel.', WIKI + 'Signet_Jewelers', 'jewellery retail group')
for n in ('Kay Jewelers', 'Zales', 'Jared', 'Blue Nile', 'Ernest Jones', 'H. Samuel'):
    nb(n, '', 'Mainstream', 'Banner listed in the Signet Jewelers infobox; owner: Signet Jewelers.', WIKI + 'Signet_Jewelers', 'jewellery retail')
bu = {
 'Cartier': ('Richemont', 'Global group', 'France'), 'Van Cleef & Arpels': ('Richemont', 'Global group', 'France'),
 'Bulgari': ('LVMH', 'Global group', 'Italy'), 'Tiffany & Co.': ('LVMH', 'Global group', 'United States'),
 'Chaumet': ('LVMH', 'Global group', 'France'), 'Pomellato': ('Kering', 'Global group', 'Italy'),
 'Boucheron': ('Kering', 'Global group', 'France'), 'Dodo': ('Kering', 'Global group', 'Italy'), 'Qeelin': ('Kering', 'Global group', 'China'),
 'Piaget': ('Richemont', 'Global group', 'Switzerland'), 'Buccellati': ('Richemont', 'Global group', 'Italy'), 'Vhernier': ('Richemont', 'Global group', 'Italy'),
 'Pandora': ('Pandora', 'Global group', 'Denmark'), 'Swarovski': ('Swarovski', 'Global group', 'Austria'),
 'Chow Tai Fook': ('Chow Tai Fook Jewellery Group', 'Global group', 'Hong Kong'),
 'Chopard': ('owner not stated', 'Independent', 'Switzerland'), 'Messika': ('Messika', 'Independent', 'France'),
 'David Yurman': ('David Yurman', 'Independent', 'United States'),
}
bupd = {k: {'own': v[0], 'tier': v[1], 'c': v[2]} for k, v in bu.items() if k in brands_old}
for n in ('Kay Jewelers', 'Zales', 'Jared', 'Blue Nile', 'Ernest Jones', 'H. Samuel'):
    bupd[n] = {'own': 'Signet Jewelers', 'tier': 'Global group', 'c': ''}
bupd['Signet Jewelers'] = {'own': 'Signet Jewelers', 'tier': 'Global group', 'c': ''}
for b in brands:
    if b['n'] in ('Richemont', 'LVMH', 'Kering'):
        bupd[b['n']] = {'own': b['n'], 'tier': 'Global group', 'c': b['c']}

part = {'replaces': REPL, 'depts': d['depts'], 'brands': brands, 'brand_updates': bupd,
        'renames': {}, 'moves': []}
json.dump(part, open(OUT, 'w'), ensure_ascii=False, indent=1)
json.dump(removed_m, open('/home/user/Possession-Taxonomy/rebuild/work/V4_A3_ALL/removed_models.json', 'w'), ensure_ascii=False, indent=1)
print(len(json.dumps(part)) / 1e6, 'MB', len(removed_m), 'kinds had m')
