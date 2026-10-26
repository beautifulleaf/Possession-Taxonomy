import json, os
WP = 'https://en.wikipedia.org/wiki/'
S = {
 'amedei': WP + 'Amedei', 'valrhona': WP + 'Valrhona', 'ruby': WP + 'Ruby_chocolate', 'white': WP + 'White_chocolate',
 'gianduja': WP + 'Gianduja_(chocolate)', 'milk': WP + 'Milk_chocolate', 'dark': WP + 'Dark_chocolate',
 'couv': WP + 'Couverture_chocolate', 'cdm': WP + 'Cadbury_Dairy_Milk', 'milka': WP + 'Milka', 'hbar': WP + 'Hershey_bar',
 'ritter': WP + 'Ritter_Sport', 'tonys': WP + 'Tony%27s_Chocolonely', 'gb': WP + 'Green_%26_Black%27s',
 'lindt': WP + 'Lindt_%26_Spr%C3%BCngli', 'toblerone': WP + 'Toblerone', 'modica': WP + 'Modica_chocolate',
 'cluizel': WP + 'Michel_Cluizel', 'domori': WP + 'Domori', 'mast': WP + 'Mast_Brothers', 'chuao': WP + 'Chuao',
 'bakers': WP + 'Baker%27s_Chocolate', 'bc': WP + 'Barry_Callebaut', 'nacional': WP + 'Nacional_(cocoa_bean)',
 'marou': WP + 'Maison_Marou', 'aoc': 'https://academyofchocolate.org.uk/about-the-awards/',
 'pump': 'https://pumpstreetchocolate.com/pages/about-us', 'pralus': 'https://www.chocolats-pralus.com/en/pages/le-chocolat',
 'dandelion': 'https://blog.dandelionchocolate.com/media-kit/', 'caffarel': WP + 'Caffarel',
 'guittard': WP + 'Guittard_Chocolate_Company', 'milkybar': WP + 'Milkybar', 'galaxy': WP + 'Galaxy_(chocolate)',
 'marabou': WP + 'Marabou_(chocolate)', 'cadbury': WP + 'Cadbury', 'meiji': WP + 'Meiji_(company)',
 'hershey': WP + 'The_Hershey_Company', 'guanaja': 'https://valrhona.com/en/our-products/for-consumers/gourmets-range/chocolate-bars-sticks/for-tasting/degustation-bar-guanaja',
 'ica': 'https://www.internationalchocolateawards.com/about-us', 'bar': WP + 'Chocolate_bar',
}

def X(n, d, mk, y, s, v=(), a='', dt=''):
    return {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': S[s],
            'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v], 'dt': dt}

kinds = [
 {'n': 'Single-origin dark chocolate', 'a': 'origin chocolate · cru · plantation chocolate · bean-to-bar origin bar',
  'd': 'Dark chocolate made from cacao of one named country, region, estate or variety, often by a bean-to-bar maker.',
  't': ['country origin', 'regional origin', 'single estate / plantation', 'single variety (criollo, Nacional)', 'vintage (single harvest)'],
  's': S['chuao'],
  'x': [
   X('Chuao', 'Venezuelan coastal-village cacao, grown since 1591 and protected as "Cacao de Chuao"; basis of the first contemporary single-origin bar.',
     '', '2000 (appellation)', 'chuao', [('Amedei Chuao', 'Amedei', '', 'popularised Chuao single-origin chocolate; held temporary exclusive use of the beans')],
     dt='village beans · c. 20 t a year · maker · cocoa %'),
   X('Porcelana', 'Venezuelan cacao (Porcelana Blanca, Lake Maracaibo) ranked among the country\'s finest beans.',
     '', '', 'amedei', [('Amedei Porcelana', 'Amedei', '2005', 'Academy of Chocolate gold, Best Bean to Bar, 2005 and 2006; described as the world\'s most expensive chocolate')],
     a='Porcelana Blanca', dt='maker · cocoa %'),
   X('Arriba Nacional', 'Ecuadorian fine-aroma Nacional cacao from the Arriba region, known for a floral aroma; pure trees are now rare.',
     '', '18th–19th century', 'nacional', [('Pure Nacional groves, Piedra de Plata valley', "To'ak Chocolate", '2013', 'old groves found and DNA-confirmed')],
     a='Nacional · fino de aroma', dt='Ecuador, Peru · purity (DNA-tested) · cocoa %'),
   X('Michel Cluizel plantation bars', 'Single-plantation dark bars, each named after the estate that grew the beans.',
     'Michel Cluizel', '', 'cluizel',
     [('Mangaro 65%', 'Michel Cluizel', '', 'Madagascar'), ('Mokaya 66%', 'Michel Cluizel', '', 'Mexico'),
      ('Los Anconès 67%', 'Michel Cluizel', '', 'Dominican Republic'), ('Vila Gracinda 67%', 'Michel Cluizel', '', 'São Tomé'),
      ('Riachuelo 70%', 'Michel Cluizel', '', 'Brazil'), ('La Laguna 70%', 'Michel Cluizel', '', 'Guatemala')],
     dt='plantation · 65–70 %'),
   X('Pyramide des Tropiques', 'Tasting set of 75% dark bars from ten origins, made bean-to-bar so origins can be compared at one percentage.',
     'Pralus', '2003', 'pralus', [('Nosy-Be plantation chocolate', 'Pralus', '', 'criollo cacao from the maker\'s own Madagascar plantation')],
     dt='ten origins · 75 %'),
   X('Vintage plantation chocolate', 'Grand cru chocolate made from a single year\'s harvest of one plantation.',
     'Valrhona', '', 'valrhona', dt='plantation · harvest year'),
   X('Criollo varietal bars', 'Bars from named criollo cacao varieties, including a 100% criollo bar without lecithin or flavourings.',
     'Domori', '', 'domori', [('Puertomar', 'Domori', '', 'criollo variety'), ('Puertofino', 'Domori', '', 'criollo variety')],
     dt='variety · up to 100 %'),
   X('Vietnamese provincial origins', 'Bean-to-bar bars made in Vietnam from cacao of six southern provinces.',
     'Maison Marou', '2011', 'marou', a='Marou', dt='province · cocoa %'),
   X('Two-ingredient origin bar', 'Single-origin bar made from only cocoa beans and organic cane sugar.',
     'Dandelion Chocolate', '2010', 'dandelion', dt='origin · cocoa %'),
  ],
  'm': [['Single-estate bars (Ecuador, Madagascar, Grenada, Honduras, Jamaica)', 'Pump Street Chocolate']]},

 {'n': 'Dark chocolate bar', 'a': 'plain chocolate · black chocolate · bittersweet · semisweet',
  'd': 'Solid bar of cocoa mass, cocoa butter and sugar without milk, usually about 40–100% cocoa.',
  't': ['50–60 %', '70 %', '85–90 %', '99–100 %', 'organic', 'Fairtrade'], 's': S['dark'],
  'x': [
   X('Guanaja', 'Bittersweet 70% dark chocolate that Valrhona calls the first chocolate to reach 70% cocoa.', 'Valrhona', '1986', 'guanaja',
     [('Dégustation bar Guanaja 70%', 'Valrhona', '', '70 g tasting bar')], dt='70 %'),
   X('Bournville', 'British plain dark chocolate bar, first sold in 1908.', 'Cadbury', '1908', 'cadbury',
     [('Bournville Classic Dark', 'Cadbury', '', '180 g bar cited as a British dark chocolate')], dt='bar size'),
   X('Hershey\'s Special Dark', 'American dark chocolate bar.', 'The Hershey Company', '1939', 'hbar',
     [('Special Dark with Almonds', 'The Hershey Company', '', ''), ('Extra Dark Pure Dark Chocolate', 'The Hershey Company', '', '')]),
   X('Green & Black\'s Organic Dark', 'Organic, Fairtrade dark chocolate from the first UK brand to carry the Fairtrade mark.', 'Green & Black\'s', '1991', 'gb',
     [('Organic Dark Chocolate 70% Cacao', 'Green & Black\'s', '', ''), ('Maya Gold', 'Green & Black\'s', '1994', 'Fairtrade cocoa from Maya farmers in Belize')],
     dt='organic · Fairtrade · cocoa %'),
   X('Cioccolato di Modica', 'Sicilian cold-worked dark chocolate, not conched, whose undissolved sugar gives a grainy texture.', '', '16th century', 'modica',
     [('PGI Cioccolato di Modica', 'Consorzio di Tutela del Cioccolato di Modica', '2018', 'EU protected geographical indication'),
      ('Antica Dolceria Bonajuto', 'Antica Dolceria Bonajuto', '', 'Ruta family house outside the consortium')],
     a='Modica chocolate', dt='45–90 % · cinnamon, vanilla, chilli, citrus'),
  ],
  'm': [['Excellence', 'Lindt & Sprüngli'], ['Extra dark chocolate 70%', "Tony's Chocolonely"], ['Signature Dark', 'Mast Brothers']]},

 {'n': 'Milk chocolate bar', 'a': 'dairy milk chocolate · Alpine milk chocolate',
  'd': 'Solid bar of chocolate with milk solids added, sweeter and milder than dark chocolate.',
  't': ['classic milk', 'dark milk (40 %+)', 'Alpine milk', 'vegan "milk"'], 's': S['milk'],
  'x': [
   X('Gala Peter', 'The first eating milk chocolate brand, from Daniel Peter, who first combined chocolate with condensed milk in 1875.', 'Daniel Peter', '1887', 'milk'),
   X('Hershey\'s Milk Chocolate Bar', 'American milk chocolate bar billed as "The Great American Chocolate Bar".', 'The Hershey Company', '1900', 'hbar',
     [('Milk Chocolate with Almonds', 'The Hershey Company', '1908', ''), ('Gold', 'The Hershey Company', '2017', '')]),
   X('Milka Alpine Milk', 'Alpine milk chocolate bar created by Suchard, advertised with the lilac cow.', 'Milka', '1901', 'milka',
     [('Lila cow advertising', 'Milka', '1972', 'cow conceived 1971')], dt='bar size · flavour'),
   X('Cadbury Dairy Milk', 'British milk chocolate bar launched in Birmingham in 1905.', 'Cadbury', '1905', 'cdm',
     [('Dairy Milk (US, under licence)', 'The Hershey Company', '', 'different formula'), ('Dairy Milk Silk', 'Cadbury', '2010', 'India'),
      ('Dairy Milk Caramel', 'Cadbury', '2003', 'relaunched under Dairy Milk')], dt='bar size · flavour'),
   X('Meiji Milk Chocolate', 'Japanese milk chocolate bar.', 'Meiji', '1926', 'milk'),
   X('Marabou Mjölkchoklad', 'Swedish milk chocolate, the first Marabou chocolate.', 'Marabou', '1916', 'marabou'),
   X('Galaxy', 'Smooth milk chocolate bar sold as Dove in the US, Canada and parts of Europe.', 'Galaxy', '1960', 'galaxy',
     [('Dove', 'Galaxy', '', 'name in US, Canada, Mexico and parts of Europe'), ('Vegan range', 'Galaxy', '2019', '')]),
   X('Tony\'s Chocolonely Milk 32%', 'Milk chocolate bar with deliberately unequal pieces, marking unequal income in the cocoa chain.', 'Tony\'s Chocolonely', '2005', 'tonys',
     [('Milk chocolate caramel sea salt 32%', "Tony's Chocolonely", '', ''), ('Milk hazelnut 32%', "Tony's Chocolonely", '2010', ''),
      ('Dark milk pretzel toffee 42%', "Tony's Chocolonely", '', '')], dt='flavour · cocoa %'),
  ],
  'm': [['Cailler Branche', 'Cailler'], ['Signature Milk', 'Mast Brothers']]},

 {'n': 'White chocolate', 'a': 'white chocolate bar · blond chocolate',
  'd': 'Chocolate of cocoa butter, sugar and milk solids with no cocoa solids; at least 20% cocoa butter under Codex.',
  't': ['plain white', 'caramelised (blond)', 'with inclusions'], 's': S['white'],
  'x': [
   X('Galak / Milkybar', 'The first commercial white chocolate tablet, sold as Galak in Europe and Milkybar in the UK.', 'Nestlé', '1936', 'milkybar',
     [('Milkybar Kid advertising', 'Nestlé', '1961', ''), ('Alpine White', 'Nestlé', '1984', 'US'), ('Milkybar Mix Ups', 'Nestlé', '2019', '')],
     a='Galak · Milkybar', dt='bar, buttons'),
   X('Hershey\'s Cookies \'n\' Creme', 'White crème bar with chocolate cookie pieces.', 'The Hershey Company', '1994', 'hbar'),
  ],
  'm': [['Snowflake', 'Cadbury'], ['Dream', 'Cadbury'], ['White Chocolate', 'Milka'], ['Blond chocolate', 'Valrhona'], ['White raspberry popping candy 28%', "Tony's Chocolonely"]]},

 {'n': 'Ruby chocolate', 'a': 'RB chocolate · pink chocolate',
  'd': 'Naturally pink chocolate from "ruby cocoa beans", with a berry-like sweet-sour taste; launched in 2017.',
  's': S['ruby'],
  'x': [X('Ruby chocolate', 'Pink chocolate presented by its maker as a "fourth natural type" alongside dark, milk and white.', 'Barry Callebaut', '2017', 'ruby',
          [('KitKat Ruby', 'Nestlé', '2018', 'first mass-market release, Japan and South Korea'), ('Ruby bar', 'Fortnum & Mason', '2018', 'UK')],
          dt='bar, coating, couverture')],
  'm': [['Ruby chocolate bar', 'Chocolove']]},

 {'n': 'Gianduja', 'a': 'gianduia · gianduiotto · hazelnut chocolate',
  'd': 'Turin blend of chocolate with about 30% hazelnut paste, sold as bars, fillings and ingots.',
  't': ['bar', 'ingot (gianduiotto)', 'cremino'], 's': S['gianduja'],
  'x': [X('Gianduiotto', 'Small ingot-shaped piece of gianduja.', 'Caffarel', '1852', 'gianduja',
          [('Gianduiotti, Paris 1878', 'Talmone', '1878', 'praised at the Paris Universal Exhibition'),
           ('Gianduiotti, Paris 1878', 'Gay-Revel', '1878', ''), ('Gianduiotti, Paris 1878', 'Moriondo', '1878', '')],
          a='giandujotto', dt='size · dark, milk'),
        X('Cremino', 'Gianduja speciality of Turin.', '', '', 'gianduja')]},

 {'n': 'Flavoured & inclusion bar', 'a': 'nut bar · fruit and nut · flavoured chocolate',
  'd': 'Solid chocolate bar flavoured or mixed with nuts, fruit, caramel, nougat, biscuit or other pieces.',
  't': ['nut', 'fruit & nut', 'caramel / toffee', 'sea salt', 'mint', 'spice', 'biscuit / crisp pieces'], 's': S['bar'],
  'x': [
   X('Whole-hazelnut bar', 'Chocolate bar packed with whole hazelnuts, first made by Kohler.', 'Kohler', '1830', 'gianduja',
     [('Dairy Milk Whole Nut', 'Cadbury', '1930', '')]),
   X('Toblerone', 'Triangular-prism Swiss milk chocolate bar with honey and almond nougat.', 'Toblerone', '1908', 'toblerone',
     [('Dark', 'Toblerone', '1969', ''), ('White', 'Toblerone', '1973', ''), ('Mint Crisp', 'Toblerone', '1985', ''),
      ('Honeycomb Crisp', 'Toblerone', '2009', ''), ('Crunchy Salted Almond', 'Toblerone', '', '')], dt='flavour · format'),
   X('Fruit & nut bar', 'Milk chocolate bar with fruit and nuts.', 'Cadbury', '1926', 'cdm',
     [('Dairy Milk Fruit and Nut', 'Cadbury', '1926', ''), ('Galaxy Fruit & Nut', 'Galaxy', '', '')]),
   X('Ritter Sport square bar', 'Square German bar sold in many filled and inclusion flavours.', 'Ritter Sport', '1932', 'ritter',
     [('Edel-Nuss Mix', 'Ritter Sport', '2012', 'centenary bar'), ('Dunkle Voll-Nuss Amaranth', 'Ritter Sport', '2017', 'first certified vegan bars'),
      ('Sesam', 'Ritter Sport', '2020', ''), ('Cacao Y Nada', 'Ritter Sport', '2021', '')], dt='flavour'),
  ],
  'm': [['Dark almond sea salt 51%', "Tony's Chocolonely"], ['Milk honey almond nougat 32%', "Tony's Chocolonely"],
        ['Broken Nuts', 'Milka'], ['Milka and Daim', 'Milka'], ['Sea Salt', 'Mast Brothers'], ['Infernal bars', 'Pralus']]},

 {'n': 'Couverture & baking chocolate', 'a': 'cooking chocolate · baking bar · callets · unsweetened chocolate',
  'd': 'Chocolate for melting, tempering, coating and baking; couverture carries extra cocoa butter (32–39%).',
  't': ['couverture (callets, drops, blocks)', 'unsweetened 100 %', 'sweet baking chocolate', 'chips', 'pre-tempered', 'untempered'], 's': S['couv'],
  'x': [
   X('Callebaut couverture', 'Belgian couverture credited with founding the modern product; shipped in liquid form from 1920.', 'Callebaut', '1911', 'couv'),
   X('Baker\'s unsweetened chocolate', 'American 100% cacao unsweetened baking chocolate.', 'Baker\'s', '1780', 'bakers',
     [('German\'s Sweet Chocolate', 'Baker\'s', '1852', 'created by employee Samuel German')]),
  ],
  'm': [['Couverture', 'Valrhona'], ['Couverture', 'Guittard'], ['Baking chips', 'Guittard'], ['Couverture', 'Cacao Barry'], ['Couverture', 'Carma']]},
]

def B(n, c, f, seg, d, s, lines=(), sig=(), rel=(), eras=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'd': d, 'lines': list(lines), 'eras': list(eras), 'sig': list(sig), 'sc': [], 'rel': list(rel), 's': S[s]}

brands = [
 B('Valrhona', 'France', '1922', 'Craft & professional', 'Tain-l\'Hermitage chocolate maker founded by pastry chef Albéric Guironnet; part of Savencia.', 'valrhona',
   ['Grand Cru', 'vintage chocolate'], ['Guanaja', 'Vintage plantation chocolate']),
 B('Amedei', 'Italy', '1990', 'Craft single origin', 'Pontedera, Tuscany maker that popularised Chuao single-origin chocolate.', 'amedei', [], ['Chuao', 'Porcelana']),
 B('Domori', 'Italy', '1997', 'Craft single origin', 'Piedmont maker founded by Gianluca Franzoni, focused on criollo cacao; part of the Illy group since 2006.', 'domori', [], ['Criollo varietal bars']),
 B('Michel Cluizel', 'France', '1948', 'Craft single origin', 'Normandy chocolate maker founded by Marc Cluizel, known for single-plantation bars.', 'cluizel', [], ['Michel Cluizel plantation bars']),
 B('Pralus', 'France', '1948', 'Craft single origin', 'Roanne house run by François Pralus, an early French bean-to-bar maker with a Madagascar plantation.', 'pralus',
   ['Pyramide des Tropiques', 'Infernal'], ['Pyramide des Tropiques']),
 B('Maison Marou', 'Vietnam', '2011', 'Craft bean-to-bar', 'Ho Chi Minh City bean-to-bar maker founded by Samuel Maruta and Vincent Mourou.', 'marou', [], ['Vietnamese provincial origins']),
 B('Dandelion Chocolate', 'United States', '2010', 'Craft bean-to-bar', 'San Francisco bean-to-bar factory founded by Todd Masonis and Cameron Ring, using two ingredients.', 'dandelion', [], ['Two-ingredient origin bar']),
 B('Mast Brothers', 'United States', '2007', 'Craft bean-to-bar', 'Brooklyn maker founded by Rick and Michael Mast, credited with popularising bean-to-bar in America.', 'mast'),
 B('Pump Street Chocolate', 'United Kingdom', '2010', 'Craft bean-to-bar', 'Orford, Suffolk bakery and chocolate maker founded by Chris and Joanna Brennan.', 'pump'),
 B('Lindt & Sprüngli', 'Switzerland', '1845', 'Premium mass market', 'Kilchberg chocolate maker; owns Ghirardelli, Caffarel and Russell Stover.', 'lindt', ['Excellence', 'Lindor'], [], ['Caffarel']),
 B('Cadbury', 'United Kingdom', '1824', 'Mass market', 'Birmingham chocolate maker founded by John Cadbury; owned by Mondelez since 2010.', 'cadbury',
   ['Dairy Milk', 'Bournville'], ['Cadbury Dairy Milk', 'Bournville', 'Fruit & nut bar'], ['Green & Black\'s', 'Milka']),
 B('Milka', 'Switzerland', '1901', 'Mass market', 'Alpine milk chocolate brand created by Suchard, now Mondelez, made in Germany, Slovakia and Argentina.', 'milka', [], ['Milka Alpine Milk']),
 B('The Hershey Company', 'United States', '1894', 'Mass market', 'Chocolate maker founded by Milton S. Hershey in Lancaster, Pennsylvania.', 'hershey', [],
   ['Hershey\'s Milk Chocolate Bar', 'Hershey\'s Special Dark', 'Hershey\'s Cookies \'n\' Creme']),
 B('Ritter Sport', 'Germany', '1912', 'Mass market', 'Waldenbuch maker founded by Clara and Alfred E. Ritter, known for its square bar since 1932.', 'ritter', [], ['Ritter Sport square bar']),
 B('Tony\'s Chocolonely', 'Netherlands', '2005', 'Mass market, ethical', 'Amsterdam brand founded by Teun van de Keuken against slavery in the cocoa trade.', 'tonys', [], ['Tony\'s Chocolonely Milk 32%']),
 B('Green & Black\'s', 'United Kingdom', '1991', 'Premium organic', 'London organic chocolate brand founded by Craig Sams and Josephine Fairley; now Mondelez.', 'gb', [], ['Green & Black\'s Organic Dark'], ['Cadbury']),
 B('Toblerone', 'Switzerland', '1908', 'Mass market', 'Bern triangular honey-almond nougat bar by Theodor Tobler and Emil Baumann; now Mondelez.', 'toblerone', [], ['Toblerone']),
 B('Barry Callebaut', 'Switzerland', '1996', 'Industrial & professional', 'Zürich cocoa processor formed by merging Cacao Barry and Callebaut; developer of ruby chocolate.', 'bc',
   ['Callebaut', 'Cacao Barry', 'Carma'], ['Ruby chocolate'], ['Callebaut']),
 B('Callebaut', 'Belgium', '1850', 'Professional couverture', 'Belgian chocolate maker credited with modern couverture; part of Barry Callebaut since 1996.', 'couv', [], ['Callebaut couverture'], ['Barry Callebaut']),
 B('Caffarel', 'Italy', '1826', 'Premium', 'Turin chocolate maker that created the gianduiotto in 1852; owned by Lindt & Sprüngli.', 'caffarel', [], ['Gianduiotto'], ['Lindt & Sprüngli']),
 B('Baker\'s', 'United States', '1780', 'Baking', 'American baking chocolate brand begun by John Hannon and Dr James Baker; owned by Kraft Heinz.', 'bakers', [], ['Baker\'s unsweetened chocolate']),
 B('Guittard', 'United States', '1868', 'Baking & professional', 'Burlingame, California maker founded by Étienne Guittard, making couverture and baking chips.', 'guittard'),
 B('Nestlé', 'Switzerland', '', 'Mass market', 'Swiss food company that launched Galak (Milkybar), the first commercial white chocolate, in 1936.', 'milkybar', [], ['Galak / Milkybar']),
 B('Galaxy', 'United Kingdom', '1960', 'Mass market', 'Mars milk chocolate brand, sold as Dove in North America and parts of Europe.', 'galaxy', [], ['Galaxy']),
 B('Marabou', 'Sweden', '1916', 'Mass market', 'Swedish chocolate brand owned by Mondelez.', 'marabou', [], ['Marabou Mjölkchoklad']),
 B('Meiji', 'Japan', '1917', 'Mass market', 'Tokyo food and dairy company that makes chocolate bars.', 'meiji', [], ['Meiji Milk Chocolate']),
]

traditions = [
 {'n': 'Cioccolato di Modica', 'g': 'Food & drink', 'r': 'Modica, Sicily, Italy', 'p': '16th century to present (PGI 2018)',
  'd': 'Sicilian cold-worked chocolate brought under Spanish rule, kept grainy because the sugar never dissolves.',
  'tech': 'worked "a freddo" below 40 °C, not conched; once rolled on lava stone, poured into pewter moulds as thick bars',
  'mat': 'cocoa with its butter, sugar; optional cinnamon, vanilla, ginger, chilli, almonds, citrus peel',
  'forms': ['Cioccolato di Modica'], 'ctr': ['Consorzio di Tutela del Cioccolato di Modica (2003)', 'Antica Dolceria Bonajuto'],
  'auth': 'PGI mark; grainy rough texture, small air bubbles, crumbly break, slightly grey bloom; no milk, vegetable fat or lecithin', 's': S['modica']},
 {'n': 'Turin gianduja', 'g': 'Food & drink', 'r': 'Turin, Piedmont, Italy', 'p': 'Napoleonic period (1796–1814) to present',
  'd': 'Turin chocolate-making that blends chocolate with hazelnut paste, giving the gianduiotto and cremino.',
  'tech': 'chocolate blended with about 30% hazelnut paste', 'mat': 'chocolate, Piedmont hazelnuts',
  'forms': ['Gianduiotto', 'Cremino'], 'ctr': ['Caffarel', 'Talmone', 'Gay-Revel', 'Moriondo'],
  'auth': 'ingot shape and hazelnut share', 's': S['gianduja']},
]

notes = ("New shelf (no old kinds). Award bodies recorded: Academy of Chocolate Awards (London, since 2005; Golden Bean top bar award) "
 + S['aoc'] + " and International Chocolate Awards (since 2012, run by IICCT; regional rounds and a World Final; bean-to-bar categories) " + S['ica'] +
 ". Left out because no page could be retrieved (cocoarunners/chocosphere 403, chocolats-de-luxe 503): Bonnat, Original Beans (brands and bars), "
 "Madagascar Sambirano, Peru and Ghana as origin archetypes, Valrhona Manjari/Caraïbe/Dulcey, Lindt Excellence launch year and percentages, "
 "Freia Melkesjokolade launch year, Côte d'Or bars. Pump Street, Mast Brothers kept as brands with bars only in m. Countlines (Kit Kat, Mars) belong to the Pralines/confections shelf.")

out = {'kinds': kinds, 'brands': brands, 'traditions': traditions, 'notes': notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/J8/shelves/02_00.json'
tmp = p + '.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, p)
print('kinds', len(kinds), 'archetypes', sum(len(k.get('x', [])) for k in kinds), 'brands', len(brands), 'traditions', len(traditions))
