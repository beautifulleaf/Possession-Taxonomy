import json, os, sys
W = 'https://en.wikipedia.org/wiki/'
WD = 'https://www.wikidata.org/wiki/'
PC = W + 'Persian_carpet'; TC = W + 'Turkish_carpet'; CC = W + 'Caucasian_carpets_and_rugs'
LP = 'https://little-persia.com/pages/caucasian-rug-guide'
TR = W + 'Turkmen_rug'; TB = W + 'Tibetan_rug'; SA = W + 'Sultanabad_rugs_and_carpets'
BR = W + 'Balochi_rug'; AF = W + 'Afghan_rug'; PK = W + 'Pakistani_rug'; MC = W + 'Mughal_carpet'
RN = 'https://rugsonnet.com/?p=137832'; AWM = 'https://www.awm.gov.au/collection/C999128'
AB = 'https://www.abhijna-emuseum.com/?p=1611'
EXTRA = json.load(open(os.path.join(os.path.dirname(__file__), 'extra.json'))) if os.path.exists(os.path.join(os.path.dirname(__file__), 'extra.json')) else {}


def X(n, d, s, y='', a='', mk='', v=None, dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s}
    if v: x['v'] = [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]
    if dt: x['dt'] = dt
    return x


persian = [
    X('Heriz', 'Room-size carpets from north-west Iran with bold rectilinear fields and white-outlined central medallions on a cotton foundation.', WD + 'Q2045414',
      a='Heris', dt='room sizes · cotton foundation · medallion or all-over'),
    X('Serapi', 'The higher-quality grade of Heriz carpet, with predominantly rectilinear design.', PC, y='c. 1875 (cited example)', a='Serab',
      v=[('Antique Serapi', '', 'c. 1875', 'example cited on the page')]),
    X('Tabriz', 'Carpets from the north-west market city, symmetric-knotted, whose weavers revived Persian weaving and reproduce many designs.', PC,
      y='modern industry c. 1885', v=[('Tabriz revival manufactories', '', 'c. 1885', 'start of the modern Iranian carpet industry')]),
    X('Kashan', "Central Iran's oldest carpet city, known for silk carpets with red or ivory fields and ogival medallions.", PC,
      v=[('Safavid commissions with European coats of arms', '', '1601–1602', ''), ('Late-19th-century revival', '', 'late 19th c.', '')],
      dt='wool or silk pile · red or ivory field'),
    X('Isfahan', 'Fine silk or silk-on-cotton carpets with asymmetric knots and Safavid-inspired designs in dark red and blue.', PC,
      v=[('Safavid court manufactory', '', '16th–17th c.', 'established under Shah Abbas'), ('Modern Isfahan', '', 'mid-20th c. revival', '')]),
    X('Nain', 'Finely asymmetric-knotted carpets with richly decorated medallions in light blue and ivory.', PC, y='mid-20th c.', a='Naein'),
    X('Qom', 'Asymmetric-knotted medallion carpets in light blue and ivory, often all-silk, close in style to Nain.', PC, y='mid-20th c.', a='Ghom'),
    X('Kerman', 'Finely knotted carpets in cochineal red, ivory and golden yellow, often with elaborate boteh.', WD + 'Q3515494', a='Kirman',
      v=[('Safavid vase-technique carpets (Sanguszko group)', '', '16th–17th c.', 'asymmetric knots, three wefts'),
         ('Late-19th-century Kerman', '', 'late 19th c.', 'field encroaching on the main border')]),
    X('Ravar', 'Town carpets from Ravar near Kerman, noted for fine materials and their own weaving technique.', PC, a='Laver · Lavar'),
    X('Mashad', 'Average-quality carpets from Mashhad, often in cochineal red.', PC, a='Mashhad · Meshed',
      v=[('Emogli', '', '', 'silk pieces with dense arabesques on red ground')]),
    X('Sultanabad', 'Arak-area room-size carpets with large all-over palmette and vine designs, softened for Western rooms.', SA, y='from 1883',
      a='Arak · Ziegler',
      v=[('Ziegler & Co. manufactory', 'Ziegler & Co.', '1883', 'Western-adapted designs and colours')],
      dt='large formats · deep rose-red madder grounds'),
    X('Farahan', 'Rugs from the Arak region, distinct from Sultanabad production.', SA),
    X('Sarouk', 'Western Iranian rugs, originally with a round-star medallion; later all-over florals, often washed and repainted for export.', WD + 'Q3515506',
      a='Saruq', v=[('Original medallion Sarouk', '', '', 'round-star medallion'), ('American-market Sarouk', '', '', 'all-over floral, chemically washed, repainted pile')]),
    X('Malayer', 'Single-weft, symmetric-knotted rugs on cotton from western Iran, allover or medallion, often with boteh.', PC),
    X('Hamadan', 'Rugs marketed through Hamadan, a major western Iranian production centre.', PC),
    X('Bijar', 'Heavy, densely packed "wet-woven" Kurdish rugs, symmetric-knotted, often with Garus patterns.', PC, y='since 18th c.', a='Bidjar',
      dt='60–200+ knots per sq in · Garus design'),
    X('Senneh', 'Very fine symmetric-knotted Kurdish rugs from Sanandaj with closely clipped pile, blue fields and Garus medallions.', PC, a='Sanandaj',
      dt='up to 400 knots per sq in'),
    X('Qashqai', 'All-wool tribal rugs from Fars with ivory warps, asymmetric knots and barber-pole selvedges.', PC, a='Kashkai · Ghashghai',
      v=[('Firuzabad workshop rugs', '', '19th c.', '')]),
    X('Gabbeh', 'Coarsely knotted Qashqai rugs with thick pile and simple abstract designs.', PC,
      v=[('Natural-dye revival Gabbeh', '', '1990s', 'shown at the 1992 Great Persian Exhibition')]),
    X('Khamseh', 'Rugs of a five-tribe federation in Fars, with stylised bird (murgh) motifs around lozenge medallions.', PC, y='19th c.'),
    X('Afshar', 'Semi-nomadic rugs from near Kerman, mainly runners and bags in bright and pale reds with striped flat-woven ends.', PC, a='Afshari'),
    X('Luri', 'Rugs of western and south-western Iran on dark wool foundations with star compartments and hooked lozenge medallions.', PC, a='Lori'),
    X('Bakhtiari', 'Tribal and village rugs attributed to the Bakhtiari, woven with the symmetric knot.', PC),
    X('Ardabil design', 'Copies and reworkings of the Ardabil Carpet, the most famous Persian carpet.', PC, y='1539–40 (original)',
      v=[('Ardabil Carpet', '', '1539–40', 'original, Victoria and Albert Museum'), ('Later copies', '', '', 'e.g. the copy at 10 Downing Street')]),
]
anatolian = [
    X('Ushak', 'Large workshop carpets from Uşak, chiefly the Star and Medallion types.', TC, y='16th c.', a='Usak · Oushak',
      v=[('Star Ushak', '', '16th c.', 'dark blue star medallions in infinite repeat on red'),
         ('Medallion Ushak', '', '16th c.', 'ovoid medallions and eight-lobed stars on floral trellis'),
         ('Double-niche Ushak', '', '16th c.', 'corner medallions forming niches at both ends')]),
    X('Holbein carpet', 'Anatolian carpets named after their appearance in Western paintings, with octagons and stars or large medallions.', TC, y='15th–16th c.',
      v=[('Small-pattern Holbein', '', '15th–16th c.', 'small octagons with stars'), ('Large-pattern Holbein', '', '15th–16th c.', 'two or three large medallions; linked to Bergama')]),
    X('Lotto carpet', 'Anatolian carpets with a yellow arabesque lattice on a red field.', TC, y='15th–16th c.',
      v=[('Anatolian style', '', '', 'Ellis group'), ('Kilim style', '', '', 'Ellis group'), ('Ornamental style', '', '', 'Ellis group')]),
    X('Konya', 'Rugs of the Konya region, from Seljuq fragments to later village rugs.', WD + 'Q6430443',
      v=[('Seljuq carpets', '', '13th c.', 'small geometric motifs, kufic borders'), ('Double-niche Konya', '', 'c. 1750–1800', '')]),
    X('Hereke', 'Very fine palace carpets with floral designs and corner medallions; now also a trade name for high-quality Turkish carpets.', WD + 'Q5738127',
      y='workshop 1843; carpets from 1891', dt='wool or silk-on-silk · very high knot density'),
    X('Bergama', 'Trade name for rugs of the Bergama area, with large geometric or stylised floral designs in dark red and blue.', WD + 'Q3890861',
      v=[('Kozak', '', '', 'small-format geometric rugs with latch hooks')]),
    X('Milas', 'Village rugs from the Milas area of south-west Anatolia.', WD + 'Q1934372'),
    X('Ladik', 'Rugs from the Ladik weaving centre.', TC, y='Ottoman period'),
    X('Gördes', 'Rugs from the Gördes weaving centre.', TC, y='Ottoman period', a='Ghiordes'),
    X('"Transylvanian" rug', 'Anatolian rugs with small prayer-niche fields, vases and cartouche borders, named after Transylvanian church holdings.', TC, y='16th–17th c.'),
    X('White-ground (Selendi) rug', 'Rugs with cintamani, bird or scorpion motifs on a white ground.', TC, y='17th c.'),
    X('Animal carpet', 'Early Anatolian carpets with large confronted animals or bird-and-tree medallions.', TC, y='mid-15th c.–c. 1500',
      v=[('Dragon and Phoenix rug', '', '', ''), ('Marby rug', '', '', '')]),
    X('Ottoman Cairene', 'Ottoman court designs woven in Egypt after the 1517 conquest.', TC, y='1517–early 17th c.'),
    X('Mecidi', 'Turkish baroque carpets based on French Savonnerie and Aubusson designs, used in palaces such as Dolmabahçe.', TC, y='19th c.'),
    X('Yürük', 'Coarse, long-piled nomadic rugs with latch-hooked central medallions.', TC, dt='pile up to 12 mm'),
    X('Yağcıbedir', 'Geometric rugs in subdued colours, Caucasian-like; a group label rather than a town.', TC, dt='100,000–140,000 knots per m²'),
]
caucasian = [
    X('Kazak', 'Coarse, thick-piled Caucasian rugs with bold geometric medallions and stylised animals in red, blue and green.', LP, a='Kazakh'),
    X('Shirvan', 'Finer Caucasian rugs with small geometric medallions, thinner pile and a subdued red, blue and ivory palette.', LP),
    X('Kuba', 'Finely knotted Caucasian rugs with intricate geometric patterns, stylised flowers and stars.', LP, a='Quba'),
    X('Derbent', 'Dense, finely knotted rugs with geometric designs in deep reds, blues and yellows.', LP),
    X('Karabagh', 'Rugs of the Karabakh region, one of the main Caucasian styles.', CC, a='Karabakh'),
    X('Gendje', 'Rugs of the Ganja area, one of the main Caucasian styles.', CC, a='Ganja · Genje'),
    X('Daghestan', 'Rugs of Daghestan, grouped with the North Caucasian styles.', CC, a='Dagestan'),
]
turkmen = [
    X('Tekke', 'Rugs of the Teke, whose main-carpet design is the source of the "Bukhara" export pattern.', TR, a='Teke',
      v=[('"Bukhara" export rug', '', 'from c. 1910', 'synthetic dyes, cotton foundation, after the Tekke main carpet')]),
    X('Yomut', 'Rugs and trappings of the Yomut tribe, one of the five traditional Turkmen houses.', WD + 'Q4817318', a='Yomud',
      v=[('Five Tree Yomut asmalyk', '', '18th–19th c.', 'camel trapping')]),
    X('Ersari', 'Rugs of the Ersari Turkmen, source of the octagonal "elephant\'s foot" export design.', WD + 'Q5395771', a='Arsary'),
    X('Salor', 'Rugs and trappings of the Salor (Salyr), one of the most famous Turkmen tribes.', TR, a='Salur · Salyr'),
    X('Saryk', 'Rugs of the Saryk, one of the five traditional Turkmen houses.', TR),
    X('Chodor', 'Rugs of the Chowdur, one of the five traditional Turkmen houses.', TR, a='Chowdur · Chaudor'),
]
afghan = [
    X('Baluch rug', 'Small dark-toned rugs and bags woven by Baloch tribes of eastern Iran and western Afghanistan.', BR, a='Baluchi · Balochi',
      v=[('Mehrabi prayer rug', '', '', 'mihrab at one end'), ('Camel-hair Baluch', '', '', 'camel hair in the palette')],
      dt='about 8 ft long · wool or wool and goat hair · dark red, brown, blue with white'),
    X('Afghan war rug', 'Pile rugs with tanks, guns and other military motifs, woven after the 1979 Soviet invasion.', AWM, y='from 1979',
      v=[('Baluchi war rug', '', 'c. 1980', 'tanks and armoured cars with Baluchi medallions'), ('Refugee-camp war rugs', '', '', 'Peshawar and Quetta')]),
    X("Elephant's foot (Bukhara) rug", 'The typical Afghan design: rows of octagonal guls, often on red.', AF, a='Afghan Bukhara · fil pai'),
    X('Shindand', 'Herat-province rugs with strangely elongated human and animal figures.', AF, a='Adraskan'),
    X('Aqcha', 'Mostly red rugs woven in Samangan and Kunduz provinces.', AF, a='Ahcha'),
    X('Bezeheri', 'Kunduz rugs with rows of stylised flowers or flower-shaped hexagons on light red.', AF),
]
chinese = [
    X('Ningxia', 'The oldest Chinese rug family, with Buddhist and Taoist motifs in soft golds, apricots and faded indigo.', WD + 'Q10955552',
      y='17th–19th c.', dt='thin, supple handle'),
    X('Baotou', 'A Chinese rug type from Baotou.', WD + 'Q10901666'),
    X('Peking', 'Export rugs woven around Beijing reviving classical designs in several blues on ivory.', RN, y='c. 1880–1930', a='Beijing',
      dt='central medallion · fret borders · shou medallions'),
    X('Chinese Art Deco rug', 'Tianjin export rugs with sparse asymmetric motifs on open fields in saturated jewel tones.', RN, y='1920s–1930s', a='Tientsin',
      v=[('Nichols rug', 'Nichols', '1920s–1930s', 'the most celebrated examples')]),
]
tibetan = [
    X('Khaden', 'Tibetan sleeping or sitting carpet, typically about 3 × 5 ft.', TB),
    X('Tibetan tiger rug', 'Rugs showing realistic or abstract tiger pelts, used as meditation seats.', TB,
      v=[('Realistic pelt', '', '', ''), ('Abstract stripes', '', '', ''), ('Whole pelt with legs and face', '', '', '')]),
    X('Wangden rug', 'Warp-faced Tibetan rugs with loose weave, thick pile and shaggy fringe, used on monastic benches.', TB),
]
indian = [
    X('Mughal carpet', 'Imperial Indian carpets blending Persian and Indian design, made in Agra, Lahore and Fatehpur Sikri workshops.', MC, y='16th–17th c.',
      a='Indo-Persian · Lahore',
      v=[("Girdlers' carpet", '', '17th c.', 'one of the best-documented examples'), ('Millefleur star-lattice carpet', '', '', ''),
         ('Farsh-i-chandani', '', '', 'style popularised by Nur Jahan')]),
    X('Agra', 'Persian-style Indian carpets with natural dyes and bold floral borders.', AB, y='from 1580',
      v=[('Akbar workshops', '', '1580', '')]),
    X('Jaipur', 'Fine hand-knotted wool carpets with bright colours and geometric motifs.', AB, y='17th c.'),
    X('Kashmir', 'Soft hand-knotted wool and silk carpets on Persian patterns.', AB, dt='silk pile, warp and weft in fine pieces'),
    X('Bhadohi', 'Carpets from the main Uttar Pradesh weaving belt, often with local designs.', AB),
    X('Pak Persian', 'Pakistani Senneh-knotted rugs reproducing Kashan, Kirman, Isfahan and Tabriz designs.', PK),
    X('Pakistani Bokhara', 'Ghiordes-knotted Pakistani rugs in the geometric Tekke design, in many colours.', PK),
    X('Jaldar', 'Pakistani rugs with rows of diamond-shaped guls, after Sarouk and Yomut designs.', PK),
    X('Chobi', 'Floral Pakistani rugs in handspun wool and natural dyes.', PK, a='Ziegler · Peshawar'),
    X('Lahore jail carpet', 'Carpets woven in the jails of Lahore under British rule.', PK, y='British colonial period'),
]

kinds = [
    {'n': 'Persian rug', 'a': 'Persian carpet · Iranian carpet', 'd': 'Hand-knotted pile rug woven in Iran, named by city, region or tribe.',
     't': ['Town or workshop', 'Village', 'Nomadic or tribal', 'Wool pile', 'Silk pile'], 's': PC, 'x': persian,
     'm': [['Zanjan', ''], ['Mehraban', '']]},
    {'n': 'Caucasian rug', 'a': 'Caucasian carpet', 'd': 'Hand-knotted village rug from the Caucasus with bold geometric designs.', 's': WD + 'Q5054266', 'x': caucasian},
    {'n': 'Anatolian rug', 'a': 'Turkish carpet · Turkish rug', 'd': 'Hand-knotted pile rug from Anatolia, mostly with the symmetric Turkish knot.', 's': TC,
     't': ['Village', 'Workshop', 'Nomadic', 'Silk'], 'x': anatolian, 'm': [['Kayseri', '']]},
    {'n': 'Turkmen rug', 'a': 'Turkoman rug', 'd': 'Hand-knotted Central Asian tribal rug or bag, identified by tribe and gul.', 's': TR,
     't': ['Main carpet', 'Tent bag', 'Door hanging', 'Camel trapping'], 'x': turkmen},
    {'n': 'Afghan & Baluch rug', 'a': 'Afghan rug · Baluchi rug', 'd': 'Hand-knotted rug from Afghanistan or by Baloch weavers of Iran and Afghanistan.', 's': AF, 'x': afghan},
    {'n': 'Chinese rug', 'a': 'Chinese carpet', 'd': 'Hand-knotted Chinese rug, often clipped in relief, named by region or period.', 's': RN, 'x': chinese},
    {'n': 'Tibetan rug', 'a': 'Tibetan carpet', 'd': 'Hand-knotted rug of highland wool woven in Tibet or by the Tibetan exile workshops of Nepal and India.', 's': TB,
     't': ['Tibet-made', 'Nepal or India-made Tibetan style'], 'x': tibetan},
    {'n': 'Indian & Pakistani rug', 'a': 'Indian carpet · Pakistani rug', 'd': 'Hand-knotted rug from India or Pakistan, from Mughal court carpets to modern export weaves.', 's': PK, 'x': indian},
]
for kn, xs in EXTRA.get('x', {}).items():
    for k in kinds:
        if k['n'] == kn: k['x'].extend(X(**x) for x in xs)
for k in kinds:
    for x in k['x']:
        if 'Zanjan' in [m[0] for m in k.get('m', [])]: pass

brands = [
    {'n': 'Ziegler & Co.', 'c': 'United Kingdom', 'f': '', 'seg': 'Persian carpet manufacturer (historic)',
     'd': 'Manchester-based Anglo-Swiss firm that set up a carpet manufactory in Sultanabad (Arak) in 1883 to make rugs for Western taste.',
     'lines': ['Sultanabad (Ziegler) carpets'], 'eras': ['Sultanabad manufactory, from 1883'], 'sig': ['Sultanabad'], 'sc': [], 'rel': [], 's': SA},
    {'n': 'Nichols', 'c': 'China', 'f': '', 'seg': 'Chinese export rug workshop (historic)',
     'd': 'Tianjin workshop of American entrepreneur Walter Nichols, maker of the most celebrated Chinese Art Deco rugs.',
     'lines': [], 'eras': ['1920s–1930s'], 'sig': ['Chinese Art Deco rug'], 'sc': [], 'rel': [], 's': RN},
]
G = 'Textiles & rugs'
traditions = [
    {'n': 'Persian carpet weaving', 'g': G, 'r': 'Iran', 'p': 'Pazyryk 5th c. BC; Safavid classical 16th–17th c.; revival from c. 1885',
     'd': 'Knotted-pile carpet weaving of Iranian towns, villages and tribes; Fars and Kashan skills on the UNESCO intangible heritage list (2010).',
     'tech': 'symmetric and asymmetric knots on wool or cotton foundations', 'mat': 'sheep wool, cotton, silk, goat hair, camel wool',
     'forms': ['Persian rug'], 'ctr': ['Tabriz', 'Kashan', 'Isfahan', 'Kerman', 'Qom', 'Nain', 'Fars tribes'],
     'auth': 'Abrash and natural dyes suggest village or tribal work; chemical washing and repainting mark export pieces.', 's': PC},
    {'n': 'Caucasian rug weaving', 'g': G, 'r': 'Caucasus', 'p': 'mainly 19th–early 20th c.',
     'd': 'Village rug weaving of the Caucasus with bold geometric designs in primary colours.', 'tech': 'Turkish (Ghiordes) knot; also soumak flatweave',
     'mat': 'hand-spun local wool, natural dyes', 'forms': ['Caucasian rug'], 'ctr': ['Kazak', 'Shirvan', 'Kuba', 'Karabagh', 'Ganja', 'Daghestan'],
     'auth': 'Older pieces valued for rarity; natural dyes and hand-spun wool.', 's': LP},
    {'n': 'Anatolian carpet weaving', 'g': G, 'r': 'Anatolia (Turkey)', 'p': 'Seljuq 13th c. to present',
     'd': 'Village, nomadic and court carpet weaving of Anatolia, known in the West through Renaissance paintings.',
     'tech': 'symmetric Turkish (Ghiordes) knot; asymmetric knot in Istanbul silk workshops', 'mat': 'hand-spun naturally dyed wool; cotton and silk in workshop pieces',
     'forms': ['Anatolian rug'], 'ctr': ['Uşak', 'Konya', 'Bergama', 'Hereke', 'Ladik', 'Gördes', 'Milas'],
     'auth': 'Many labels (Transylvanian, Hereke, Bergama) are trade names rather than proven origins.', 's': TC},
    {'n': 'Turkmen rug weaving', 'g': G, 'r': 'Turkmenistan and neighbouring Central Asia', 'p': 'nomadic tradition; export production from c. 1910',
     'd': 'Tribal weaving of tent rugs, door hangings, bags and trappings, each tribe using its own geometric guls.',
     'tech': 'hand knotting on portable looms', 'mat': 'local wool, natural dyes; later cotton foundations and synthetic dyes',
     'forms': ['Turkmen rug'], 'ctr': ['Teke', 'Yomut', 'Ersari', 'Saryk', 'Salor', 'Chowdur', 'Turkmen Carpet Museum'],
     'auth': 'Export rugs have little in common with tribal pieces; irregularities typical of older nomadic work.', 's': TR},
    {'n': 'Baluch weaving', 'g': G, 'r': 'Sistan and Baluchestan, Khorasan, Nimroz', 'p': '19th c. to present',
     'd': 'Rugs, prayer rugs and bags woven by Baloch tribes in dark reds, browns and blues.', 'tech': 'hand knotting; goat-hair edges',
     'mat': 'wool, goat hair, camel hair', 'forms': ['Afghan & Baluch rug'], 'ctr': [], 'auth': '', 's': BR},
    {'n': 'Afghan carpet weaving', 'g': G, 'r': 'Afghanistan', 'p': 'traditional; war rugs from 1979',
     'd': 'Rug weaving mainly by Turkmen, Uzbek and Baloch women, from tribal designs to modern workshop pieces.',
     'tech': 'hand knotting', 'mat': 'hand-spun wool, vegetable dyes', 'forms': ['Afghan & Baluch rug'],
     'ctr': ['Herat', 'Kunduz', 'Samangan', 'Mazar-e Sharif'], 'auth': '', 's': AF},
    {'n': 'Chinese rug weaving', 'g': G, 'r': 'China', 'p': '17th c. (Ningxia) to 1930s export trade',
     'd': 'Knotted rugs for monasteries, court and export, from Ningxia to Peking and Tianjin Art Deco.', 'tech': 'hand knotting, relief clipping',
     'mat': 'wool, silk', 'forms': ['Chinese rug'], 'ctr': ['Ningxia', 'Beijing', 'Tianjin', 'Baotou'],
     'auth': 'Genuine early Ningxia pieces are scarce.', 's': RN},
    {'n': 'Tibetan rug weaving', 'g': G, 'r': 'Tibet; exile workshops in Nepal and India', 'p': 'peak 19th–early 20th c.; exile revival from 1970s',
     'd': 'Rugs for sitting, sleeping, meditation and saddles woven from highland wool.', 'tech': 'distinct Tibetan knotting method',
     'mat': 'changpel highland wool; madder, indigo, rhubarb, walnut dyes', 'forms': ['Tibetan rug'],
     'ctr': ['Gyantse', 'Lhasa', 'Shigatse', 'Wangden valley', 'Kathmandu'],
     'auth': 'Tibet-made rugs differ from South Asian "Tibetan style"; Lhasa shops sell Qinghai and polyester imitations.', 's': TB},
    {'n': 'Mughal and Indian carpet weaving', 'g': G, 'r': 'India', 'p': '16th c. to present',
     'd': 'Carpet weaving founded in Mughal imperial workshops and continued in Agra, Jaipur, Kashmir and Bhadohi.',
     'tech': 'hand knotting; hand tufting in modern production', 'mat': 'wool, silk, cotton; natural dyes', 'forms': ['Indian & Pakistani rug'],
     'ctr': ['Agra', 'Lahore', 'Fatehpur Sikri', 'Kashmir', 'Jaipur', 'Bhadohi'], 'auth': '', 's': MC},
    {'n': 'Pakistani carpet weaving', 'g': G, 'r': 'Pakistan', 'p': 'Mughal Lahore; jail weaving under British rule; growth after 1947',
     'd': 'Export-led hand-knotted rug industry reproducing Persian, Turkmen and Caucasian designs.', 'tech': 'Senneh and Ghiordes knots',
     'mat': 'handspun wool, natural dyes', 'forms': ['Indian & Pakistani rug'], 'ctr': ['Lahore', 'Multan', 'Peshawar', 'Karachi', 'Quetta'], 'auth': '', 's': PK},
]
notes = ("k29 'Rug' became Persian rug; its construction types (woven pile, tufted) and Wilton/Axminster go to the machine-made shelf, not here. "
         "Old Persian names became archetypes; Usak became the Ushak archetype and Kayseri stays an Anatolian model (no source detail); Baluchi moved to the "
         "Afghan & Baluch kind. Zanjan and Mehraban kept as plain models: no retrieved page describes them. Left out for lack of a retrieved source: "
         "Talish (Caucasian), Mahal (unless added), Amritsar and Lahore as separate archetypes (Lahore covered by Mughal carpet), Khal Mohammadi, "
         "Turkmen gul names (Turkmen_rug page names none), East Turkestan rugs. Versions limited to those stated on the source pages; no antique/new/"
         "reproduction split invented. Wikidata SPARQL was rate-limited.")
notes = EXTRA.get('notes', notes)
out = {'kinds': kinds, 'brands': brands, 'traditions': traditions, 'notes': notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/B2/shelves/00_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('kinds', len(kinds), 'archetypes', sum(len(k['x']) for k in kinds), 'bytes', os.path.getsize(p))
