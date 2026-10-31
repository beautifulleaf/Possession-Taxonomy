import json, os
W = 'https://en.wikipedia.org/wiki/'
SC = 'https://classictypewriter.substack.com/p/an-overview-of-smith-corona-typewriters'
SM = 'https://www.stephenlloydwebber.com/typewriter-buying/olympia-sm3'
MV = 'https://collections.museumsvictoria.com.au/items/394007'
HEM = 'https://www.sliderulemuseum.com/srtco/HemmiChronology.shtml'
DP = 'https://sliderulemuseum.com/REF/Dennert.shtml'
NASM = 'https://airandspace.si.edu/collection-objects/slide-rule-5-inch-pickett-n600-es-apollo-13/nasm_A19840160000'
FC = 'https://www.stefanv.com/calculators/fc283n.html'
ZS = 'https://ich.unesco.org/en/RL/zhusuan-knowledge-and-practices-of-mathematics-with-abacus-in-china-00853'
BS = 'https://www.dento-tokyo.metro.tokyo.lg.jp/english/items/92.html'
IPSJ = 'https://museum.ipsj.or.jp/en/heritage/Casio_Mini.html'
SR10 = 'https://si.edu/object/texas-instruments-sr-10-handheld-electronic-calculator:nmah_334394'


def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o

OL, HE, RO, SCN, UN, RE, IBM, BL, OLY = 'Olivetti', 'Hermes', 'Royal', 'Smith Corona', 'Underwood', 'Remington', 'IBM', 'Blickensderfer', 'Olympia'
tw = {'n': 'Typewriter', 'a': 'manual typewriter · portable typewriter · electric typewriter',
 'd': 'Machine that prints characters on paper as keys are struck, manual or electric; collected by maker, model and era.',
 't': ['standard (desktop) manual', 'portable', 'ultra-portable', 'electric', 'electronic (daisywheel)', 'typewheel / index', 'typeface (pica, elite, script)', 'keyboard layout (QWERTY, QWERTZ, AZERTY)'],
 's': 'https://www.staples.com/shredders-projectors-office-machines/cat_SC1681',
 'x': [
  X('Sholes and Glidden', 'The first commercially successful typewriter, made by Remington, which introduced the QWERTY layout.', RE, '1873', W + 'Typewriter',
    [('Sholes and Glidden', RE, '1873', 'production began 1 March 1873'), ('Remington No. 2', RE, '1878', 'introduced the shift key')]),
  X('Underwood No. 5', 'Front-strike office typewriter called the first truly modern typewriter; about two million sold by the early 1920s.', UN, '1900', W + 'Underwood_Typewriter_Company',
    [('Underwood No. 1', UN, '1896', 'fully visible typing area'), ('Underwood No. 5', UN, '1900', ''), ('Underwood Universal Portable', UN, '', 'used by William Faulkner')]),
  X('Blickensderfer', 'Compact typewheel machine whose interchangeable cylindrical type wheel changes the typeface.', BL, '1893', W + 'Blickensderfer_typewriter',
    [('No. 5', BL, '1893', 'shown at the World\'s Columbian Exposition'), ('No. 7', BL, '1897', 'deluxe'), ('No. 8', BL, '1908', 'tabulator'), ('Featherweight', BL, '', 'aluminium "Five-Pound Secretary"'), ('Blickensderfer Electric', BL, '1901', 'early electric, commercial failure')]),
  X('Remington Portable', 'First truly portable typewriter with a four-row keyboard, with typebars that fold flat for the case.', RE, '1920', MV,
    [('Portable No. 1', RE, '1920', 'museum example dated 1923')]),
  X('Corona Three', 'Folding three-row portable made for over thirty years under three company names.', SCN, '1909', SC,
    [('Standard Folding Typewriter', '', '1909', 'to 1914'), ('Corona Three', 'Corona', '1914', 'Corona Typewriter Co., to 1925'), ('L.C. Smith & Corona Three', SCN, '1925', 'to 1941')]),
  X('Smith-Corona Silent / Sterling', 'Smith-Corona\'s 1930s–50s portables; the Silent adds sound-proofing and an interchangeable platen to the Sterling.', SCN, '', SC,
    [('Sterling (4C)', SCN, '', 'gloss black c.1938'), ('Silent (4S)', SCN, '', 'gloss maroon c.1937'), ('Silent Super', SCN, '', 'art-deco body, plastic keys, tab keys')], dt='Speedline body · gloss or crinkle paint'),
  X('Royal Quiet De Luxe', 'Royal\'s most popular portable, used by many writers including Ernest Hemingway.', RO, '1939', W + 'Royal_Typewriter_Company',
    [('Quiet De Luxe', RO, '1939', 'made to 1959 with a wartime gap')]),
  X('Hermes Baby', 'Swiss ultra-portable from Paillard, made for over fifty years.', HE, '1935', W + 'Hermes_Baby',
    [('Hermes Baby', HE, '1935', 'made to 1989')]),
  X('Olivetti Lettera 22', 'Italian portable designed by Marcello Nizzoli, Compasso d\'Oro winner of 1954.', OL, '1949', W + 'Olivetti_Lettera_22',
    [('Lettera 22', OL, '1949', 'Nizzoli design'), ('Lettera 32', OL, '1963', 'successor')]),
  X('Olympia SM3', 'West German portable that made Olympia\'s name in the 1950s, nicknamed the Mercedes-Benz of portables.', OLY, '1955', SM,
    [('SM3', OLY, '1955', 'to 1964, carriage shift'), ('SM9', OLY, '', 'later, more precise')], dt='about 6 kg · chrome-wrapped base'),
  X('Hermes 3000', 'Swiss portable succeeding the Hermes 2000, on which Sylvia Plath typed The Bell Jar.', HE, '1958', W + 'Hermes_3000',
    [('Hermes 3000 Model 1', HE, '1958', 'to 1966'), ('later Hermes 3000', HE, '', 'made into the 1980s')]),
  X('IBM Selectric', 'Electric typewriter with a swappable spherical typeball instead of typebars, designed by Eliot Noyes.', IBM, '1961', W + 'IBM_Selectric',
    [('Selectric I', IBM, '1961', ''), ('Selectric II', IBM, '1971', 'dual pitch'), ('Correcting Selectric II', IBM, '1973', 'built-in correction tape'), ('Selectric III', IBM, '1980', '96-character element')]),
  X('Olivetti Valentine', 'Red ABS portable typewriter by Ettore Sottsass with Perry King, held by MoMA.', OL, '1969', W + 'Olivetti_Valentine',
    [('Valentine', OL, '1969', 'designed 1968')], dt='red, also other colours'),
 ],
 'm': [['Royal KMM', RO]]}

FCN, KE, PK, AR, HM, OK = 'Faber-Castell', 'Keuffel & Esser', 'Pickett', 'Aristo', 'Hemmi', 'Otis King'
sr = {'n': 'Slide rule', 'a': 'slipstick · Rechenschieber',
 'd': 'Pair of sliding logarithmic scales with a cursor for multiplying, dividing and more; linear, circular or cylindrical.',
 't': ['simplex', 'duplex', 'log-log', 'Darmstadt', 'Rietz', 'pocket (5 in / 12.5 cm)', 'circular', 'cylindrical', 'specialist (electrical, flight computer)'],
 's': 'https://www.sphere.bc.ca/type/slide-rules/',
 'x': [
  X('K&E Log Log Duplex Decitrig 4081-3', 'Keuffel & Esser duplex rule, the mainstay of American engineering students and engineers from the 1940s to 1960s.', KE, '', W + 'Keuffel_and_Esser',
    [('4081-3', KE, '', '10-inch'), ('Deci-Lon 68-1100', KE, '', 'later K&E rule')]),
  X('Pickett N600-ES', 'Five-inch aluminium pocket log-log rule carried on Apollo missions, including Aldrin\'s on Apollo 11.', PK, '', NASM,
    [('N600-ES', PK, '', 'Apollo 13 example held by the National Air and Space Museum')], dt='aluminium and plastic'),
  X('Faber-Castell 2/83N Novo-Duplex', 'All-plastic full-size duplex rule with about 31 scales, often called the finest slide rule ever made.', FCN, '1972', FC,
    [('2/83', FCN, '', 'older, fewer scales'), ('2/83N', FCN, '1972', 'about 1972–1975'), ('62/83N', FCN, '', 'rare pocket version')], dt='25 cm scales · W scales'),
  X('Aristo Studio', 'Dennert & Pape\'s professional rule made under the Aristo brand from 1949.', AR, '1949', DP,
    [('Scholar', AR, '1949', 'school rule'), ('Studio', AR, '1949', ''), ('Multi log', AR, '1953', '8 log scales'), ('Studiolog', AR, '1967', '8 log-log scales'), ('Aviat', AR, '1954', 'flight computer')]),
  X('Hemmi bamboo slide rule', 'Japanese rule of celluloid-clad laminated bamboo (patented 1912), also sold under the Post brand in the US.', HM, '1912', HEM,
    [('86K', HM, '', 'extra-fine divisions'), ('64T', HM, '', 'over-range scales'), ('250', HM, '1960', 'small bamboo rule'), ('259D', HM, '', ''), ('Sun Hemmi 80K Electro', HM, '', 'electrical'), ('Post (US-branded Hemmi)', 'Frederick Post', '1931', '')]),
  X('Otis King calculator', 'Pocket cylindrical slide rule with helical scales equal to a 66-inch rule, made by Carbic of London.', OK, '1922', W + 'Otis_King',
    [('Model K', OK, '', 'multiplication and division')]),
 ],
 'm': [['Aristo 99', AR], ['Faber-Castell 2/82', FCN], ['Faber-Castell 1/22 Business-Commerce', FCN], ['Faber-Castell 111/98 Elektro', FCN], ['Faber-Castell 163/84 Novo-Mentor', FCN],
       ['K&E 4092-3', KE], ['K&E Jet Log 4181-1 (pocket)', KE], ['K&E Polyphase 4053-3', KE], ['Pickett 800ES', PK], ['Pickett Model 20', PK], ['Pickett N500T', PK],
       ['Nestler 23R', 'Nestler'], ['Nestler Elemath RS', 'Nestler'], ['Dietzgen 1734 LogLog', 'Dietzgen'], ['Logarex 27403 System Darmstadt', 'Logarex'],
       ['Concise Model 90', 'Concise'], ['Concise Model 600CE', 'Concise'], ['Concise Model 700 MM Metric Marvel', 'Concise'], ['Acumath 400', 'Acumath']]}

ab = {'n': 'Abacus', 'a': 'そろばん soroban · 算盘 suanpan · счёты schoty · counting frame',
 'd': 'Frame of beads on rods moved by hand to calculate; Chinese, Japanese and Russian forms differ in bead layout.',
 't': ['2:5 beads (suanpan)', '1:4 beads (soroban)', '10 beads, horizontal wires (schoty)', 'children\'s counting frame'],
 's': 'https://www.sphere.bc.ca/type/slide-rules/',
 'x': [
  X('Suanpan', 'Chinese abacus with two heaven beads and five earth beads per rod, used for zhusuan calculation.', '', 'Han dynasty', W + 'Suanpan',
    [('2:5 suanpan', '', 'late Ming', 'classic layout'), ('modern 1:4 with clear button', '', '', '')], dt='hardwood beads · rod count'),
  X('Soroban', 'Japanese abacus derived from the suanpan, with one five-bead and four one-beads per rod and unit-dot marks.', '', '', W + 'Soroban',
    [('1:4 soroban', '', '1940s', 'became popular'), ('Banshu soroban', '', '', 'Ono, Hyogo; ebony frame, boxwood or birch beads')], dt='13 rods standard; 21–31 for practical models'),
  X('Schoty', 'Russian abacus of ten beads per horizontal wire, held vertically, with a quarter-kopek wire.', '', '', W + 'Abacus', []),
 ]}

TC, OD, BR, CM, CU = 'Thomas de Colmar', 'Odhner', 'Brunsviga', 'Felt & Tarrant', 'Contina'
mc = {'n': 'Mechanical calculator', 'a': 'arithmometer · pinwheel calculator · adding machine · comptometer',
 'd': 'Hand- or motor-driven geared machine for arithmetic, from arithmometers and pinwheel calculators to key-driven adders and the Curta.',
 't': ['stepped drum (arithmometer)', 'pinwheel', 'key-driven adder', 'slide adder', 'electric drive'],
 's': W + 'Arithmometer',
 'x': [
  X('Thomas arithmometer', 'First mechanical calculator reliable enough for daily office use, sold from 1851; widely copied.', TC, '1851', W + 'Arithmometer',
    [('Arithmometer', TC, '1851', 'patented 1820'), ('Payen arithmometer', 'Payen', '1887', 'improved re-zeroing'), ('Burkhardt', 'Burkhardt', '1878', 'German clone'), ('Layton', 'Layton', '1883', 'British clone')]),
  X('Odhner arithmometer', 'Pinwheel calculator by Willgodt Odhner, lighter than the arithmometer and copied worldwide.', OD, '1873', W + 'Odhner_Arithmometer',
    [('Odhner', OD, '1890', 'serial production in St Petersburg'), ('Original-Odhner', 'Original-Odhner', '', 'Sweden'), ('Felix', '', '', 'Soviet Moscow production')]),
  X('Brunsviga', 'German pinwheel calculator built under Odhner\'s patent in Braunschweig.', BR, '1892', W + 'Brunsviga',
    [('Model A', BR, '1892', ''), ('Trinks-Triplex', BR, '', ''), ('Brunsviga 13RK', BR, '', ''), ('Dupla', BR, '1929', 'electric')]),
  X('Comptometer', 'Key-driven adding machine of Dorr Felt where each key press adds at once; made from 1887 to the mid-1970s.', CM, '1887', W + 'Comptometer',
    [('Model A', CM, '1904', ''), ('Model E', CM, '1913', 'Controlled-Key'), ('Model K', CM, '', 'electric, mid-1930s'), ('3D11', CM, '', 'postwar mechanical'), ('992', CM, '', 'postwar electric')]),
  X('Curta', 'Hand-cranked cylindrical pocket calculator designed by Curt Herzstark, made in Liechtenstein.', CU, '1948', W + 'Curta',
    [('Curta Type I', CU, '1948', '8-digit setting, about 80,000 made'), ('Curta Type II', CU, '1954', '11-digit setting, about 60,000 made')]),
 ],
 'm': [['Faber-Castell 111/54A Addiator', FCN]]}

HP, CA, TI = 'HP', 'Casio', 'Texas Instruments'
ve = {'n': 'Vintage electronic calculator', 'a': 'LED calculator · early pocket calculator',
 'd': 'Early 1970s electronic desk and pocket calculators, collected for their LED or fluorescent displays and as firsts.',
 't': ['LED display', 'vacuum fluorescent display', 'RPN', 'programmable', 'desk'],
 's': W + 'HP-35',
 'x': [
  X('Busicom LE-120A Handy', 'Busicom\'s pocket model, among the first calculators with an LED display.', 'Busicom', '', W + 'Busicom',
    [('LE-120A Handy-LE', 'Busicom', '', ''), ('LE-120S Handy', 'Busicom', '', '')]),
  X('HP-35', 'World\'s first scientific pocket calculator, with RPN and red LED display; US$395.', HP, '1972', W + 'HP-35',
    [('HP-35', HP, '1972', 'to 1975')]),
  X('Sinclair Executive', 'First slimline and first mass-produced pocket calculator, held by MoMA.', 'Sinclair Radionics', '1972', W + 'Sinclair_Executive',
    [('Executive', 'Sinclair Radionics', '1972', '£79.95 plus VAT')]),
  X('Casio Mini', 'Low-priced six-digit personal calculator that sold over a million in its first year.', CA, '1972', IPSJ,
    [('Casio Mini', CA, '1972', '12,800 yen; vacuum fluorescent display')]),
  X('TI SR-10', 'Texas Instruments\' first scientific calculator, sold as an electronic slide rule.', TI, '1972', SR10,
    [('SR-10', TI, '1972', '12-digit LED, $149.95')]),
  X('HP-65', 'First handheld programmable calculator with magnetic-card storage; flew on Apollo–Soyuz.', HP, '1974', W + 'HP-65',
    [('HP-65', HP, '1974', 'US$795')]),
 ]}


def B(n, c, f, seg, kf, d, s, lines=(), sig=(), rel=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': list(rel), 's': s}

HMF = 'Heritage manufactory'
brands = [
 B(RE, 'United States', '', HMF, 'typewriters', 'Remington began production of the Sholes and Glidden typewriter in 1873.', W + 'Typewriter', [], ['Sholes and Glidden', 'Remington Portable']),
 B(UN, 'United States', '1895', HMF, 'typewriters', 'New York typewriter maker founded by John Thomas Underwood; merged into Olivetti by 1963.', W + 'Underwood_Typewriter_Company', [], ['Underwood No. 5'], [OL]),
 B(BL, 'United States', '', HMF, 'typewheel typewriters', 'Stamford, Connecticut maker of George Blickensderfer\'s typewheel machines, closed 1919.', W + 'Blickensderfer_typewriter', [], ['Blickensderfer']),
 B(SCN, 'United States', '1926', HMF, 'portable typewriters', 'Formed by the 1926 merger of L. C. Smith & Bros. and Corona Typewriter.', W + 'Smith_Corona', ['Speedline', 'Super 5'], ['Corona Three', 'Smith-Corona Silent / Sterling']),
 B(RO, 'United States', '1904', HMF, 'typewriters', 'Brooklyn typewriter maker founded by Edward B. Hess and Lewis C. Myers.', W + 'Royal_Typewriter_Company', ['Quiet De Luxe', 'KMM'], ['Royal Quiet De Luxe']),
 B(HE, 'Switzerland', '', HMF, 'portable typewriters', 'Typewriter brand of Paillard SA, Yverdon.', W + 'Hermes_Baby', ['Baby', '3000'], ['Hermes Baby', 'Hermes 3000']),
 B(OL, 'Italy', '1908', HMF, 'typewriters, design', 'Ivrea office-machine maker famed for industrial design.', 'knowledge', ['Lettera', 'Valentine'], ['Olivetti Lettera 22', 'Olivetti Valentine'], [UN]),
 B(OLY, 'Germany', '', HMF, 'typewriters', 'West German typewriter maker (Olympia Werke, Wilhelmshaven) of the SM portables.', SM, ['SM'], ['Olympia SM3'], [BR]),
 B(IBM, 'United States', '', 'Professional & flagship', 'electric typewriters', 'American computing company whose typewriter division was sold to Lexmark in 1991.', W + 'Typewriter', ['Selectric'], ['IBM Selectric']),
 B(KE, 'United States', '1867', HMF, 'slide rules, drafting', 'New York and Hoboken maker of drafting instruments and slide rules (1891–1975).', W + 'Keuffel_and_Esser', ['Log Log Duplex Decitrig', 'Deci-Lon'], ['K&E Log Log Duplex Decitrig 4081-3']),
 B(PK, 'United States', '', HMF, 'aluminium slide rules', 'Pickett & Eckel, maker of aluminium slide rules used on Apollo.', NASM, ['N600-ES'], ['Pickett N600-ES']),
 B(FCN, 'Germany', '1761', HMF, 'pencils, slide rules', 'Stein pencil maker that also made slide rules.', 'knowledge', ['2/83N'], ['Faber-Castell 2/83N Novo-Duplex']),
 B(AR, 'Germany', '1862', HMF, 'slide rules', 'Brand of Dennert & Pape, Hamburg-Altona, which made slide rules from 1872 to 1978.', DP, ['Studio', 'Scholar', 'Multi log'], ['Aristo Studio']),
 B(HM, 'Japan', '1895', HMF, 'bamboo slide rules', 'Jirou Hemmi and Co., maker of laminated-bamboo slide rules until about 1975.', HEM, [], ['Hemmi bamboo slide rule']),
 B(OK, 'United Kingdom', '1922', HMF, 'cylindrical slide rules', 'Otis King\'s Patent Calculator, made by Carbic Ltd of London from about 1922 to 1972.', W + 'Otis_King', ['Model K'], ['Otis King calculator']),
 B(TC, 'France', '1851', HMF, 'arithmometers', 'Thomas de Colmar\'s arithmometer business, later run by Louis Payen.', W + 'Arithmometer', [], ['Thomas arithmometer']),
 B(OD, 'Russia', '1890', HMF, 'pinwheel calculators', 'Willgodt Odhner\'s St Petersburg works, later Original-Odhner in Sweden.', W + 'Odhner_Arithmometer', [], ['Odhner arithmometer'], [BR]),
 B(BR, 'Germany', '1892', HMF, 'pinwheel calculators', 'Grimme, Natalis & Co. of Braunschweig, later Brunsviga Maschinenwerke; Olympia from 1959.', W + 'Brunsviga', ['13 series'], ['Brunsviga'], [OD, OLY]),
 B(CM, 'United States', '1889', HMF, 'Comptometer', 'Chicago maker of Dorr Felt\'s Comptometer.', W + 'Comptometer', ['Comptometer'], ['Comptometer']),
 B(CU, 'Liechtenstein', '', HMF, 'Curta', 'Contina AG Mauren, maker of the Curta (1948–1972).', W + 'Curta', ['Curta'], ['Curta']),
 B('Busicom', 'Japan', '', HMF, 'early calculators', 'Japanese calculator maker that commissioned the Intel 4004.', W + 'Busicom', ['Handy'], ['Busicom LE-120A Handy']),
 B('Sinclair Radionics', 'United Kingdom', '', HMF, 'pocket calculators', 'Clive Sinclair\'s electronics company.', W + 'Sinclair_Executive', ['Executive'], ['Sinclair Executive']),
]

trads = [
 {'n': 'Chinese zhusuan', 'g': 'Paper & stationery', 'r': 'China', 'p': 'Han dynasty to present',
  'd': 'Knowledge and practice of calculating on the abacus with rhymed formulas, inscribed by UNESCO in 2013.',
  'tech': 'bead movements by set rhymed formulas', 'mat': 'hardwood abacus', 'forms': ['Suanpan'], 'ctr': ['Chinese Abacus and Mental Arithmetic Association'],
  'auth': '', 's': ZS},
 {'n': 'Banshu soroban', 'g': 'Paper & stationery', 'r': 'Ono, Hyogo, Japan', 'p': 'Momoyama period (1573–1600) to present',
  'd': 'Wooden soroban craft of Hyogo, learned in Otsu and prized for smooth action and fine workmanship.',
  'tech': 'hand-finished wooden frame and beads', 'mat': 'ebony frame; boxwood or birch beads', 'forms': ['Soroban'], 'ctr': ['Ono, Hyogo'],
  'auth': 'Banshu origin marking; dense hardwood frame', 's': BS},
]

notes = ('All five planned kinds kept (Mechanical and Vintage electronic calculator are new). Old Olivetti Lettera 32 became a version of Lettera 22; old slide-rule models Hemmi 259D, Sun Hemmi 80K, Otis King Model K, K&E Deci-Lon became versions; Faber-Castell 111/54A Addiator moved to Mechanical calculator (it is a slide adder). Old soroban became an archetype. '
 'Left out for lack of a retrieved page: Facit calculators (pages blocked or empty), Olympia SM4/SG-1, Smith-Corona Clipper/Galaxie, Hermes Baby designer, Remington Portable No. 2, K&E 4081 dates. Olivetti and Faber-Castell brand facts from knowledge.')
out = {'kinds': [tw, sr, ab, mc, ve], 'brands': brands, 'traditions': trads, 'notes': notes}
p = 'work/C5/shelves/04_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
