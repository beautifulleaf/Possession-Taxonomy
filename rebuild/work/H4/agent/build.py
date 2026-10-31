import json, os
W = 'https://en.wikipedia.org/wiki/'
LP = W + 'List_of_perfumes'
CONC = 'concentration (EDC, EDT, EDP, parfum/extrait) · reformulation and batch · bottle size and edition'


def X(n, d, mk, y, s, v=(), a='', dt=CONC):
    return {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s,
            'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v], 'dt': dt}


def K(n, a, d, s, x, m=None, t=None, r=None):
    k = {'n': n, 'a': a, 'd': d, 's': s, 'x': x}
    if t: k['t'] = t
    if m: k['m'] = m
    if r: k['r'] = r
    return k


kinds = [
 K('Floral fragrance', 'fine fragrance · alcohol-based perfume · floral perfume',
   'Alcohol-based perfume whose heart is one flower or a bouquet of flowers.',
   'https://www.fragrantica.com/designers/Diptyque.html',
   [X('Chanel No. 5', 'Aldehydic floral bouquet that set the template for the modern abstract floral.', 'Chanel', '1921', W + 'Chanel_No._5',
      [('Parfum', 'Chanel', '1921', 'original extrait; Ernest Beaux'), ('Eau de Parfum', 'Chanel', '1980s', 'modern version by Jacques Polge'),
       ('Eau de Toilette', 'Chanel', '', 'separate composition'), ('Eau Première', 'Chanel', '', 'major flanker'),
       ('L\'Eau', 'Chanel', '', 'flanker by Olivier Polge')], a='No 5'),
    X('Joy', 'Landmark rich floral built on jasmine and rose.', 'Jean Patou', '1929', W + 'Joy_(perfume)',
      [('Original', 'Jean Patou', '1929', 'Henri Almeras; no longer produced')]),
    X('Arpège', 'Classic aldehydic floral bouquet.', 'Lanvin', '1927', W + 'Arp%C3%A8ge',
      [('Original', 'Lanvin', '1927', 'André Fraysse and Paul Vacher')]),
    X('L\'Air du Temps', 'Spicy floral, among the first to use large amounts of benzyl salicylate.', 'Nina Ricci', '1948', W + 'L%27Air_du_Temps_(perfume)',
      [('Original', 'Nina Ricci', '1948', 'Francis Fabron with Robert Ricci; Lalique bottle')]),
    X('Fracas', 'The reference tuberose white floral, much imitated.', 'Robert Piguet', '1948', W + 'Fracas_(perfume)',
      [('Original', 'Robert Piguet', '1948', 'Germaine Cellier')]),
    X('Diorissimo', 'Single-floral recreation of lily of the valley.', 'Dior', '1956', W + 'Diorissimo',
      [('Original', 'Dior', '1956', 'Edmond Roudnitska')]),
    X('L\'Interdit', 'Aldehydic floral.', 'Givenchy', '1957', LP, [('Original', 'Givenchy', '1957', 'Francis Fabron')]),
    X('White Linen', 'Crisp aldehydic floral.', 'Estée Lauder', '1978', LP, [('Original', 'Estée Lauder', '1978', 'Ernest Shiftan and Sophia Grojsman')]),
    X('Trésor', 'Powdery rose-apricot floral.', 'Lancôme', '1990', LP, [('Original', 'Lancôme', '1990', 'Sophia Grojsman')]),
    X('J\'adore', 'Bright floral bouquet, Dior\'s modern flagship.', 'Dior', '1999', LP, [('Original', 'Dior', '1999', 'Calice Becker')]),
    X('Chance', 'Fresh floral.', 'Chanel', '2002', LP, [('Original', 'Chanel', '2002', 'Jacques Polge')]),
    X('Do Son', 'Tuberose floral.', 'Diptyque', '2004', W + 'Diptyque'),
    X('Flowerbomb', 'Sweet floral bouquet.', 'Viktor & Rolf', '2005', LP, [('Original', 'Viktor & Rolf', '2005', 'Olivier Polge, Carlos Benaim and Domitille Bertier')]),
    X('Daisy', 'Light fruity floral.', 'Marc Jacobs', '2007', LP, [('Original', 'Marc Jacobs', '2007', 'Alberto Morillas')]),
    X('Infusion d\'Iris', 'Soft iris floral.', 'Prada', '2007', LP, [('Original', 'Prada', '2007', 'Daniela Andrier')]),
    X('Hiris', 'Iris-centred floral.', 'Hermès', '1999', LP, [('Original', 'Hermès', '1999', 'Olivia Giacobetti')]),
    X('Portrait of a Lady', 'Dense rose and patchouli scent, a modern niche reference.', 'Frédéric Malle', '2010', LP,
      [('Original', 'Frédéric Malle', '2010', 'Dominique Ropion')])],
   t=['single floral', 'floral bouquet', 'aldehydic floral', 'white floral', 'fruity floral', 'powdery floral'],
   m=[['Eau Rose', 'Diptyque'], ['Eau Capitale', 'Diptyque'], ['Orphéon', 'Diptyque'], ['Desert Dawn', 'BYREDO'],
      ['A Kiss of Bliss Eau de Parfum', 'Penhaligon\'s'], ['Sunkissed Goddess', 'By Kilian'], ['Paradigme', 'Prada Beauty'],
      ['Miutine', 'Miu Miu'], ['Fleur de Lait', 'Miu Miu'], ['Born in Roma Donna Extradose', 'Valentino'], ['Her Intense', 'Burberry'],
      ['Le Vestiaire des Parfums Muse', 'Yves Saint Laurent'], ['Replica Afternoon Delight', 'Maison Margiela'], ['Debaser In Bloom', 'D.S. & Durga']],
   r=[['Eau Rose', 'Diptyque'], ['Eau Capitale', 'Diptyque'], ['Orphéon', 'Diptyque']]),

 K('Chypre fragrance', 'chypre', 'Perfume built on citrus top notes, labdanum and an oakmoss base.', W + 'Chypre',
   [X('Chypre de Coty', 'The bergamot–labdanum–oakmoss accord that named the family; now discontinued, kept at the Osmothèque.', 'Coty', '1917', LP,
      [('Original', 'Coty', '1917', 'François Coty')], a='Chypre'),
    X('Shipr', 'Earlier Russian chypre from Brocard.', '', '1889', LP, [('Original', 'Brocard and Co. (now Novaya Zarya)', '1889', 'Henri Brocard')]),
    X('Mitsouko', 'The defining fruity chypre.', 'Guerlain', '1919', W + 'Mitsouko', [('Original', 'Guerlain', '1919', 'Jacques Guerlain')]),
    X('Femme', 'Fruity chypre.', 'Rochas', '1944', LP, [('Original', 'Rochas', '1944', 'Edmond Roudnitska')]),
    X('Miss Dior', 'Dior\'s first perfume, a green floral chypre.', 'Dior', '1947', LP, [('Original', 'Dior', '1947', 'Jean Carles and Paul Vacher')]),
    X('Pour Monsieur', 'Masculine citrus chypre.', 'Chanel', '1955', LP, [('Original', 'Chanel', '1955', 'Henri Robert')]),
    X('Aromatics Elixir', 'Woody floral or green chypre.', 'Clinique', '1971', W + 'Aromatics_Elixir',
      [('Aromatics', 'Clinique', '1971', 'first name'), ('Aromatics Elixir', 'Clinique', '1974', 'renamed; Bernard Chant')]),
    X('Diorella', 'Fruity-citrus chypre.', 'Dior', '1972', LP, [('Original', 'Dior', '1972', 'Edmond Roudnitska')]),
    X('Paloma Picasso', 'Rich floral chypre.', '', '1984', LP, [('Original', 'Paloma Picasso', '1984', 'Francis Bocris')]),
    X('Coco Mademoiselle', 'Modern patchouli chypre for younger wearers.', 'Chanel', '2001', W + 'Coco_Mademoiselle',
      [('Original', 'Chanel', '2001', 'Jacques Polge')]),
    X('Aventus', 'Fruity chypre that became the most cloned niche scent.', 'Creed', '2010', W + 'Aventus',
      [('Eau de Parfum', 'Creed', '2010', 'Jean-Christophe Hérault and Olivier Creed; 250th anniversary'),
       ('Club De Nuit Intense Man', 'Armaf', '', 'clone'), ('Supremacy Silver', 'Afnan', '2013', 'clone'),
       ('Rumz Al Rasasi 9325 Pour Lui', 'Al Rasasi', '', 'clone'), ('L\'Aventure', 'Al Haramain', '', 'clone'),
       ('Executive No.26', 'ALT Fragrances', '', 'clone')])],
   t=['classic chypre', 'fruity chypre', 'floral chypre', 'green chypre', 'leather chypre'],
   m=[['Barenia Eau de Parfum', 'Hermès']]),

 K('Fougère fragrance', 'fougère · aromatic fougère', 'Perfume built on lavender, oakmoss and coumarin, mostly worn by men.', W + 'Foug%C3%A8re',
   [X('Fougère Royale', 'Originator that gave the family its name.', 'Houbigant', '1882', LP, [('Original', 'Houbigant', '1882', 'Paul Parquet')]),
    X('Jicky', 'Lavender-led Guerlain, the oldest perfume in continuous production.', 'Guerlain', '1889', W + 'Jicky', [('Original', 'Guerlain', '1889', 'Aimé Guerlain')]),
    X('Brut', 'Mass-market aromatic fougère.', 'Fabergé', '1964', LP, [('Original', 'Fabergé', '1964', 'Jean Carles')]),
    X('Azzaro pour Homme', 'Anise-lavender aromatic fougère.', 'Azzaro', '1978', LP, [('Original', 'Azzaro', '1978', 'Gerard Anthony, Martin Heiddenreich and Richard Wirtz')]),
    X('Kouros', 'Animalic aromatic fougère.', 'Yves Saint Laurent', '1981', LP, [('Original', 'Yves Saint Laurent', '1981', 'Pierre Bourdon')]),
    X('Drakkar Noir', 'Best-selling men\'s prestige scent of 1991.', 'Guy Laroche', '1982', W + 'Drakkar_Noir',
      [('Drakkar', 'Guy Laroche', '1972', 'predecessor'), ('Drakkar Noir', 'Guy Laroche', '1982', 'Pierre Wargnye; FiFi award 1985')]),
    X('Le Male', 'Lavender-vanilla fougère in the torso bottle.', 'Jean Paul Gaultier', '1995', W + 'Le_Male',
      [('Original', 'Jean Paul Gaultier', '1995', 'Francis Kurkdjian'), ('Le Male In Blue', 'Jean Paul Gaultier', '2026', 'newest flanker')]),
    X('Sauvage', 'Ambroxan-heavy aromatic fougère, a best-seller.', 'Dior', '2015', LP, [('Original', 'Dior', '2015', 'François Demachy')])],
   t=['classic fougère', 'aromatic fougère', 'sweet fougère']),

 K('Amber fragrance', 'oriental (former name) · amber', 'Warm perfume of resins, vanilla, spices and balsams, formerly called oriental.', W + 'Fragrance_wheel',
   [X('Shalimar', 'Vanilla-citrus amber, Guerlain\'s flagship.', 'Guerlain', '1921', W + 'Shalimar_(perfume)',
      [('Original', 'Guerlain', '1921', 'Jacques Guerlain'), ('Continuous production', 'Guerlain', '1925', 'commercial launch')]),
    X('L\'Heure Bleue', 'Powdery floral amber.', 'Guerlain', '1912', LP, [('Original', 'Guerlain', '1912', 'Jacques Guerlain')]),
    X('Tabu', 'Dark spicy amber.', 'Dana', '1932', LP, [('Original', 'Dana', '1932', 'Jean Carles')]),
    X('Youth-Dew', 'Powdery amber that began as a bath oil.', 'Estée Lauder', '1953', W + 'Youth-Dew', [('Bath oil', 'Estée Lauder', '1953', 'Joséphine Catapano')]),
    X('Habit Rouge', 'Amber for men.', 'Guerlain', '1965', LP, [('Original', 'Guerlain', '1965', 'Jean-Paul Guerlain')]),
    X('Opium', 'Spicy amber that defined the 1970s–80s powerhouse.', 'Yves Saint Laurent', '1977', W + 'Opium_(perfume)',
      [('Original', 'Yves Saint Laurent', '1977', 'Jean Amic and Jean-Louis Sieuzac')]),
    X('Coco', 'Spicy floral amber.', 'Chanel', '1984', LP, [('Original', 'Chanel', '1984', 'Jacques Polge')]),
    X('Obsession', 'Heavy amber of the 1980s.', 'Calvin Klein', '1985', LP, [('Original', 'Calvin Klein', '1985', 'Robert Slattery')]),
    X('Poison', 'Bold fruity-spicy amber with a long flanker line.', 'Dior', '1985', W + 'Poison_(perfume)',
      [('Tendre Poison', 'Dior', '', 'flanker'), ('Hypnotic Poison', 'Dior', '', 'flanker'), ('Pure Poison', 'Dior', '', 'flanker'),
       ('Midnight Poison', 'Dior', '', 'flanker'), ('Poison Girl', 'Dior', '', 'flanker')]),
    X('Ambre Sultan', 'Resinous amber.', 'Serge Lutens', '1993', LP, [('Original', 'Serge Lutens', '1993', 'Christopher Sheldrake')]),
    X('Black Orchid', 'Tom Ford Beauty\'s first fragrance, a dark floral amber.', 'Tom Ford', '2006', W + 'Tom_Ford_(brand)'),
    X('1 Million', 'Spicy sweet amber for men in an ingot bottle.', 'Rabanne', '2008', LP)],
   t=['soft amber', 'floral amber', 'spicy amber', 'woody amber'],
   m=[['Black Lacquer', 'Tom Ford']]),

 K('Woody fragrance', 'woody', 'Perfume centred on woods such as sandalwood, cedar or vetiver, or woody aroma chemicals.', W + 'Sandalwood',
   [X('Vétiver', 'Reference vetiver scent.', 'Guerlain', '1961', LP, [('Original', 'Guerlain', '1961', 'Jean-Paul Guerlain')], a='Guerlain Vétiver'),
    X('Fahrenheit', 'Leathery violet-leaf woody.', 'Dior', '1988', LP, [('Original', 'Dior', '1988', 'Jean-Louis Sieuzac and Maurice Roger')]),
    X('Égoïste', 'Spicy sandalwood woody.', 'Chanel', '1990', LP, [('Original', 'Chanel', '1990', 'Jacques Polge')]),
    X('Féminité du Bois', 'Cedar woody that opened woods to women\'s perfume.', 'Serge Lutens', '1992', LP,
      [('Original', 'Shiseido-Serge Lutens', '1992', 'Christopher Sheldrake and Pierre Bourdon')]),
    X('Tam Dao', 'Sandalwood woody.', 'Diptyque', '2003', W + 'Diptyque'),
    X('Timbuktu', 'Smoky dry woody.', 'L\'Artisan Parfumeur', '2004', LP, [('Original', 'L\'Artisan Parfumeur', '2004', 'Bertrand Duchaufour')]),
    X('Terre d\'Hermès', 'Mineral orange-vetiver woody.', 'Hermès', '2006', W + 'Terre_d%27Herm%C3%A8s', [('Original', 'Hermès', '2006', 'Jean-Claude Ellena')]),
    X('Encre Noire', 'Dark vetiver woody.', 'Lalique', '2006', LP, [('Original', 'Lalique', '2006', 'Nathalie Lorson')]),
    X('Bleu de Chanel', 'Woody aromatic best-seller.', 'Chanel', '2010', LP,
      [('Original', 'Chanel', '2010', 'Jacques Polge'), ('Parfum', 'Chanel', '', 'Olivier Polge')]),
    X('Voyage d\'Hermès', 'Fresh woody.', 'Hermès', '2010', LP, [('Original', 'Hermès', '2010', 'Jean-Claude Ellena')]),
    X('Santal 33', 'Sandalwood niche scent that became a status signal.', 'Le Labo', '2011', LP, [('Original', 'Le Labo', '2011', 'Frank Voelkl')]),
    X('Baccarat Rouge 540', 'Saffron, ambroxan and cedar woody, widely duped.', 'Maison Francis Kurkdjian', '2015', W + 'Baccarat_Rouge_540',
      [('Baccarat limited edition', 'Baccarat', '2014', 'original edition for the crystal maker'),
       ('Maison Francis Kurkdjian', 'Maison Francis Kurkdjian', '2015', 'Francis Kurkdjian')])],
   t=['sandalwood', 'cedar', 'vetiver', 'woody aromatic', 'woody aroma-chemical (Iso E Super, ambroxan)'],
   m=[['Bois Pacifique', 'Tom Ford'], ['Vetyverio', 'Diptyque'], ['34 Boulevard Saint Germain', 'Diptyque']]),

 K('Citrus & eau de cologne', 'eau de Cologne · hesperidic · citrus', 'Light citrus perfume of lemon, orange, bergamot and neroli in dilute alcohol.', W + 'Eau_de_Cologne',
   [X('Eau de Cologne (Farina)', 'The original eau de Cologne, which gave the genre its name.', 'Farina', '1709', W + 'Eau_de_Cologne',
      [('Original', 'Farina', '1709', 'Johann Maria Farina')]),
    X('4711 Eau de Cologne', 'Classic Cologne eau de Cologne.', 'Mäurer & Wirtz', '1803', LP, [('Original', 'Mäurer & Wirtz', '1803', 'Wilhelm Mülhens')]),
    X('Eau de Cologne Impériale', 'Guerlain\'s imperial cologne.', 'Guerlain', '1853', LP, [('Original', 'Guerlain', '1853', 'Pierre-François-Pascal Guerlain')]),
    X('Eau Sauvage', 'Citrus-aromatic, Dior\'s first men\'s scent.', 'Dior', '1966', W + 'Eau_Sauvage', [('Original', 'Dior', '1966', 'Edmond Roudnitska')]),
    X('Eau de Guerlain', 'Citrus cologne.', 'Guerlain', '1974', LP, [('Original', 'Guerlain', '1974', 'Jean-Paul Guerlain')]),
    X('CK One', 'Unisex citrus aromatic.', 'Calvin Klein', '', W + 'CK_One', [('Original', 'Calvin Klein', '', 'Alberto Morillas and Harry Fremont')])],
   t=['classic cologne', 'citrus aromatic', 'eau fraîche'],
   m=[['Taormina Orange Eau de Parfum', 'Tom Ford'], ['Eau de Tarocco', 'Diptyque']]),

 K('Gourmand fragrance', 'gourmand', 'Perfume built on edible-smelling notes such as vanilla, praline and caramel.', W + 'Ethyl_maltol',
   [X('Angel', 'The first modern gourmand: patchouli, praline, berries and vanilla.', 'Thierry Mugler', '1992', W + 'Angel_(perfume)',
      [('Original', 'Thierry Mugler', '1992', 'Olivier Cresp and Yves de Chiris; star bottle'), ('A*Men', 'Thierry Mugler', '1996', 'men\'s counterpart; Jacques Huclier')]),
    X('Tonka Impériale', 'Tonka gourmand.', 'Guerlain', '2010', LP, [('Original', 'Guerlain', '2010', 'Thierry Wasser')]),
    X('La Vie est Belle', 'Iris-praline gourmand.', 'Lancôme', '', W + 'Olivier_Polge', [('Original', 'Lancôme', '', 'co-created by Olivier Polge')]),
    X('Lost Cherry', 'Cherry-almond Private Blend gourmand.', 'Tom Ford', '2018', LP)],
   t=['vanilla', 'praline & caramel', 'fruity gourmand', 'boozy gourmand'],
   m=[['Vanilla Candy Rock Sugar | 42', 'Kayali Fragrances'], ['Raspberry Ripple', 'Jo Malone London']]),

 K('Leather fragrance', 'leather · cuir', 'Perfume evoking tanned leather, often via birch tar and isobutyl quinoline.', W + 'Cuir_de_Russie',
   [X('Tabac Blond', 'Early leather-tobacco scent.', 'Caron', '1919', LP, [('Original', 'Caron', '1919', 'Ernest Daltroff')]),
    X('Knize Ten', 'Men\'s leather.', '', '1925', LP, [('Original', 'Kniže & Comp.', '1925', 'François Coty and Vincent Roubert')]),
    X('Cuir de Russie', 'Russia-leather scent from Chanel.', 'Chanel', '1927', W + 'Cuir_de_Russie', [('Original', 'Chanel', '1927', 'Ernest Beaux')]),
    X('Bandit', 'Bitter green leather.', 'Robert Piguet', '1944', LP, [('Original', 'Robert Piguet', '1944', 'Germaine Cellier')]),
    X('Cabochard', 'Leather chypre.', 'Grès', '1959', LP, [('Original', 'Grès', '1959', 'Bernard Chant')]),
    X('Aramis', 'Men\'s leather chypre.', 'Estée Lauder', '1963', LP, [('Original', 'Aramis (Estée Lauder)', '1963', 'Bernard Chant')]),
    X('Antaeus', 'Animalic men\'s leather.', 'Chanel', '1981', LP, [('Original', 'Chanel', '1981', 'Jacques Polge')]),
    X('Cuir Cannage', 'Modern leather.', 'Dior', '2014', LP, [('Original', 'Dior', '2014', 'François Demachy')]),
    X('Ombre Leather', 'Modern leather.', 'Tom Ford', '2018', LP)],
   t=['Russian leather', 'suede', 'leather chypre', 'tobacco-leather']),

 K('Aquatic & ozonic fragrance', 'aquatic · marine · ozonic', 'Fresh perfume evoking sea air and water, built on Calone and similar molecules.', W + 'Calone',
   [X('New West', 'Early ozonic-marine scent.', 'Estée Lauder', '1990', LP,
      [('New West Skinscent for Her', 'Aramis (Estée Lauder)', '1990', 'Annie Buzantian and Harry Frémont')]),
    X('Cool Water', 'Aquatic men\'s scent that set the 1990s fresh trend.', 'Davidoff', '1988', W + 'Cool_Water_(perfume)',
      [('Original', 'Davidoff', '1988', 'Pierre Bourdon; licence Coty')]),
    X('L\'Eau d\'Issey', 'Aquatic floral with lotus and melon.', 'Issey Miyake', '1992', W + 'L%27eau_d%27Issey',
      [('Original', 'Issey Miyake', '1992', 'Jacques Cavallier'), ('Pour Homme', 'Issey Miyake', '1994', 'men\'s flanker')]),
    X('Acqua di Giò', 'Marine men\'s scent, Fragrance Foundation Hall of Fame 2012.', 'Armani', '1996', W + 'Acqua_di_Gi%C3%B2',
      [('Original', 'Armani', '1996', 'Alberto Morillas; licence L\'Oréal')]),
    X('Light Blue', 'Citrus-aquatic summer scent.', 'Dolce & Gabbana', '2001', LP,
      [('Original', 'Dolce & Gabbana', '2001', 'Olivier Cresp'), ('Pour Homme', 'Dolce & Gabbana', '2007', '')]),
    X('Wood Sage & Sea Salt', 'Mineral salty fresh scent.', 'Jo Malone London', '2014', LP, [('Original', 'Jo Malone London', '2014', 'Christine Nagel')])],
   t=['marine', 'ozonic', 'aquatic floral', 'salty mineral'],
   m=[['Replica Beach Walk Eau de Toilette', 'Maison Margiela'], ['Beach Blossom', 'Jo Malone London'], ['L\'Ombre dans l\'Eau', 'Diptyque']],
   r=[['L\'Ombre dans l\'Eau', 'Diptyque']]),

 K('Green fragrance', 'green', 'Perfume smelling of crushed leaves, stems and grass, often built on galbanum.', W + 'Galbanum',
   [X('Vent Vert', 'Galbanum-heavy originator of the green family.', 'Balmain', '1945', LP, [('Original', 'Balmain', '1945', 'Germaine Cellier')]),
    X('Chanel No. 19', 'Balsamic-green iris scent.', 'Chanel', '1971', W + 'Chanel_No._19', [('Original', 'Chanel', '1971', 'Henri Robert')]),
    X('Philosykos', 'Fig-leaf green.', 'Diptyque', '1996', W + 'Diptyque', [('Original', 'Diptyque', '1996', 'Olivia Giacobetti')]),
    X('Un Jardin sur le Nil', 'Green mango and lotus.', 'Hermès', '2005', LP, [('Original', 'Hermès', '2005', 'Jean-Claude Ellena')])],
   t=['galbanum green', 'fig', 'tea & leaf', 'grassy'],
   m=[['L\'Eau Papier', 'Diptyque'], ['Eau Duelle', 'Diptyque'], ['Seeking Virēre Eau de Parfum', 'Aesop']],
   r=[['Philosykos', 'Diptyque'], ['L\'Eau Papier', 'Diptyque']]),

 K('Musk & skin scent', 'white musk · skin scent', 'Close-wearing perfume built on musks or a single aroma chemical that blends with the skin.', W + 'Musk',
   [X('Jovan Musk', 'Mass-market musk oil.', '', '1972', LP, [('Original', 'Jōvan', '1972', 'Denis McAdam and Murray Moscona')]),
    X('Musc Ravageur', 'Animalic musk-amber.', 'Frédéric Malle', '2000', LP, [('Original', 'Frédéric Malle', '2000', 'Maurice Roucel')]),
    X('Molecule 01', 'Single-molecule scent made only of Iso E Super.', 'Escentric Molecules', '', 'https://escentric.com/pages/about-escentric-molecules',
      [('Molecule 02', 'Escentric Molecules', '', 'numbered line'), ('Molecule + range', 'Escentric Molecules', '', 'Molecule 01 plus one molecule')]),
    X('Glossier You', 'Ambrette, ambrox and musk "skin smell enhancer".', 'Glossier', '2017', 'https://www.refinery29.com/2017/10/181412/glossier-you-fragrance',
      [('Eau de Parfum', 'Glossier', '2017', 'Dora Baghriche')]),
    X('Fleur de Peau', 'Musky skin scent.', 'Diptyque', '2018', W + 'Diptyque')],
   t=['white musk', 'animalic musk', 'single-molecule', 'skin scent']),

 K('Oud fragrance (Western niche)', 'oud · agarwood perfume', 'Alcohol-based perfume built around agarwood (oud), real or synthetic; oil ouds sit with attars.', W + 'Agarwood',
   [X('M7', 'Early designer oud.', 'Yves Saint Laurent', '2002', LP, [('Original', 'Yves Saint Laurent', '2002', 'Alberto Morillas and Jacques Cavallier')]),
    X('Oud Wood', 'Private Blend oud that made oud a Western niche staple.', 'Tom Ford', '2007', 'https://scentgrail.com/holy-grail-scents/tom-ford-oud-wood-review/',
      [('Eau de Parfum', 'Tom Ford', '2007', 'Richard Herpin; original Private Blend line'), ('Intense flanker', 'Tom Ford', '2017', '')])],
   t=['rose-oud', 'smoky oud', 'woody oud'],
   m=[['Oud Voyager', 'Tom Ford'], ['Oud Palao', 'Diptyque']]),
]

for k in kinds:
    for x in k['x']:
        for v in x['v']:
            for f in ('mk', 'y', 'd'):
                if not v.get(f): v.pop(f, None)


def B(n, c, f, seg, d, s, sig=(), lines=(), eras=(), rel=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'd': d, 'lines': list(lines), 'eras': list(eras), 'sig': list(sig), 'sc': [], 'rel': list(rel), 's': s}


H = 'Perfume house'
brands = [
 B('Chanel', 'France', '1910', 'Luxury fashion house', 'Paris house founded by Coco Chanel; owned by the Wertheimer family.', W + 'Chanel',
   ['Chanel No. 5', 'Coco Mademoiselle', 'Bleu de Chanel', 'Chanel No. 19', 'Cuir de Russie'], eras=['Ernest Beaux', 'Henri Robert', 'Jacques Polge, 1978–2015', 'Olivier Polge']),
 B('Guerlain', 'France', '1828', H, 'Paris house founded by Pierre-François Pascal Guerlain; LVMH since 1994; known for the Guerlinade.', W + 'Guerlain',
   ['Jicky', 'Mitsouko', 'Shalimar', 'L\'Heure Bleue', 'Habit Rouge', 'Vétiver'], eras=['Aimé Guerlain', 'Jacques Guerlain', 'Jean-Paul Guerlain', 'Thierry Wasser, from 2008']),
 B('Dior', 'France', '', 'Luxury fashion house', 'Parfums Christian Dior, the perfume and cosmetics arm of Christian Dior, part of LVMH.', W + 'Parfums_Christian_Dior',
   ['Miss Dior', 'Diorissimo', 'Eau Sauvage', 'Poison', 'J\'adore', 'Sauvage'], eras=['Edmond Roudnitska', 'François Demachy']),
 B('Hermès', 'France', '1837', 'Luxury goods house', 'Paris luxury house founded by Thierry Hermès, with perfumery as one line.', W + 'Herm%C3%A8s',
   ['Terre d\'Hermès', 'Un Jardin sur le Nil', 'Voyage d\'Hermès'], eras=['Jean-Claude Ellena, 2004–2016']),
 B('Creed', 'France', '1760', 'Niche perfume house', 'Paris-based house claiming a 1760 London tailoring origin (disputed).', W + 'Creed_(perfume_house)',
   ['Aventus'], eras=['Olivier Creed and Erwin Creed']),
 B('Frédéric Malle', 'France', '2000', 'Niche perfume publisher', 'Editions de Parfums Frédéric Malle, which publishes perfumes under the perfumer\'s name.', W + 'Fr%C3%A9d%C3%A9ric_Malle',
   ['Portrait of a Lady', 'Musc Ravageur']),
 B('Diptyque', 'France', '1961', 'Niche perfume and candle house', 'Paris house founded by Yves Coueslant, Christiane Gautrot and Desmond Knox-Leet.', W + 'Diptyque',
   ['Philosykos', 'Tam Dao', 'Do Son', 'Fleur de Peau', 'L\'Ombre dans l\'Eau'], lines=['L\'Eau (1968)', 'Eaux de toilette', 'Eaux de parfum']),
 B('Serge Lutens', 'France', '', 'Niche perfume house', 'House named after the perfume creator Serge Lutens.', W + 'Serge_Lutens', ['Féminité du Bois', 'Ambre Sultan']),
 B('Le Labo', 'United States', '', 'Niche perfume house', '"Slow perfumery" brand born in Grasse and based in New York; owned by Estée Lauder.', W + 'Le_Labo', ['Santal 33'], rel=['Estée Lauder']),
 B('Tom Ford', 'United States', '2005', 'Luxury fashion house', 'New York house founded by Tom Ford; fragrances owned by Estée Lauder.', W + 'Tom_Ford_(brand)',
   ['Black Orchid', 'Oud Wood', 'Lost Cherry', 'Ombre Leather'], lines=['Private Blend (2007)'], rel=['Estée Lauder']),
 B('Coty', 'France', '1904', 'Beauty group', 'Founded in Paris by François Coty; now a multinational beauty company.', W + 'Coty', ['Chypre de Coty']),
 B('Houbigant', 'France', '1775', H, 'Paris house founded by Jean-François Houbigant.', W + 'Houbigant_Parfum', ['Fougère Royale'], eras=['Paul Parquet']),
 B('Caron', 'France', '1904', H, 'Parfums Caron, founded by Ernest Daltroff.', W + 'Parfums_Caron', ['Tabac Blond']),
 B('Robert Piguet', 'France', '1933', 'Couture house', 'Paris couture house of Swiss designer Robert Piguet (1933–1951).', W + 'Robert_Piguet', ['Fracas', 'Bandit'], eras=['Germaine Cellier']),
 B('Balmain', 'France', '1945', 'Couture house', 'Paris fashion house founded by Pierre Balmain.', W + 'Balmain_(fashion_house)', ['Vent Vert']),
 B('Jean Patou', 'France', '', 'Couture house', 'Paris house of designer Jean Patou.', W + 'Jean_Patou', ['Joy']),
 B('Nina Ricci', 'France', '1932', 'Couture house', 'Paris house of Nina Ricci and her son Robert; Puig since 1998.', W + 'Nina_Ricci_(brand)', ['L\'Air du Temps']),
 B('Lanvin', 'France', '1889', 'Couture house', 'Paris house founded by Jeanne Lanvin.', W + 'Lanvin', ['Arpège']),
 B('Rochas', 'France', '1925', 'Couture house', 'Paris house founded by Marcel Rochas.', W + 'Rochas', ['Femme']),
 B('Yves Saint Laurent', 'France', '1961', 'Luxury fashion house', 'Paris house of Yves Saint Laurent and Pierre Bergé; YSL Beauty belongs to L\'Oréal.', W + 'Yves_Saint_Laurent_(fashion_house)', ['Opium', 'Kouros', 'M7']),
 B('Armani', 'Italy', '', 'Luxury fashion house', 'Milan house of Giorgio Armani; fragrances licensed to L\'Oréal.', W + 'Armani', ['Acqua di Giò']),
 B('Calvin Klein', 'United States', '1968', 'Fashion house', 'New York fashion house, PVH-owned since 2003.', W + 'Calvin_Klein_(fashion_house)', ['CK One', 'Obsession']),
 B('Estée Lauder', 'United States', '', 'Beauty group', 'New York beauty group owning Clinique, Jo Malone London, Le Labo and Tom Ford Beauty.', W + 'Est%C3%A9e_Lauder_Companies', ['Youth-Dew', 'White Linen', 'Aramis', 'New West']),
 B('Lancôme', 'France', '', 'Beauty brand', 'French beauty brand owned by L\'Oréal.', W + 'Lanc%C3%B4me', ['Trésor', 'La Vie est Belle']),
 B('Jo Malone London', 'United Kingdom', '1990', 'Perfume and home-scent brand', 'Founded by Jo Malone; owned by Estée Lauder since 1999.', W + 'Jo_Malone_London', ['Wood Sage & Sea Salt'], rel=['Estée Lauder']),
 B('Glossier', 'United States', '2014', 'Beauty brand', 'Beauty brand founded by Emily Weiss.', W + 'Glossier', ['Glossier You']),
 B('Escentric Molecules', 'United Kingdom', '2006', 'Niche perfume house', 'London house founded by Geza Schoen and Paul White around single aroma molecules.', 'https://escentric.com/pages/about-escentric-molecules', ['Molecule 01'], lines=['Molecule 01–05', 'Molecule +']),
 B('Maison Francis Kurkdjian', 'France', '', 'Niche perfume house', 'House co-founded by Francis Kurkdjian; bought by LVMH in 2017.', W + 'Francis_Kurkdjian', ['Baccarat Rouge 540']),
 B('Baccarat', 'France', '', 'Crystal maker', 'Crystal maker for which Baccarat Rouge 540 was first created.', W + 'Baccarat_(company)', ['Baccarat Rouge 540']),
 B('Farina', 'Germany', '1709', H, 'Johann Maria Farina gegenüber dem Jülichs-Platz, the Cologne house that created eau de Cologne; run by the founding family.', W + 'Johann_Maria_Farina_gegen%C3%BCber_dem_J%C3%BClichs-Platz', ['Eau de Cologne (Farina)']),
 B('Lattafa', 'United Arab Emirates', '1980s', 'Arabian-style perfume house', 'Family-owned Sharjah house founded by Shahid Ahmed, known for low-priced Arabian-style perfumes.', W + 'Lattafa', ['Khamrah', 'Yara', 'Asad']),
 B('Amouage', 'Oman', '1983', 'Niche perfume house', 'Omani niche house owned by Oman Perfumery LLC (SABCO Group).', W + 'Amouage'),
 B('Byredo', 'Sweden', '', 'Niche perfume house', 'Swedish house making fragrances, leather goods and accessories.', W + 'Byredo'),
 B('Penhaligon\'s', 'United Kingdom', '1860s', H, 'London house founded by William Henry Penhaligon.', W + 'Penhaligon%27s'),
]
P = 'Perfumer'
perf = [
 ('Ernest Beaux', 'Russia / France', '1881', 'Creator of Chanel No. 5.', 'Ernest_Beaux', ['Chanel No. 5', 'Cuir de Russie']),
 ('Jacques Guerlain', 'France', '1874', 'Third-generation Guerlain perfumer.', 'Jacques_Guerlain', ['L\'Heure Bleue', 'Mitsouko', 'Shalimar']),
 ('Edmond Roudnitska', 'France', '1905', 'Founder of Art et Parfum; worked for Dior and Rochas.', 'Edmond_Roudnitska', ['Femme', 'Diorissimo', 'Eau Sauvage', 'Diorella']),
 ('Germaine Cellier', 'France', '1909', 'Perfumer of bold mid-century classics.', 'Germaine_Cellier', ['Bandit', 'Vent Vert', 'Fracas']),
 ('Jean-Claude Ellena', 'France', '1947', 'Hermès in-house perfumer 2004–2016.', 'Jean-Claude_Ellena', ['Terre d\'Hermès', 'Un Jardin sur le Nil', 'Voyage d\'Hermès']),
 ('Dominique Ropion', 'France', '1955', 'IFF perfumer working for many houses.', 'Dominique_Ropion', ['Portrait of a Lady']),
 ('Francis Kurkdjian', 'France', '1969', 'Perfumer and co-founder of Maison Francis Kurkdjian.', 'Francis_Kurkdjian', ['Le Male', 'Baccarat Rouge 540']),
 ('Olivier Cresp', 'France', '1955', 'Firmenich perfumer.', 'Olivier_Cresp', ['Angel', 'Light Blue']),
 ('Alberto Morillas', 'Spain', '1950', 'Firmenich perfumer; own line Mizensir.', 'Alberto_Morillas', ['CK One', 'Acqua di Giò', 'Daisy', 'M7']),
 ('Jacques Polge', 'France', '1943', 'Chanel head perfumer 1978–2015.', 'Jacques_Polge', ['Coco', 'Égoïste', 'Coco Mademoiselle', 'Bleu de Chanel']),
 ('Olivier Polge', 'France', '1974', 'Chanel house perfumer.', 'Olivier_Polge', ['Chanel No. 5 L\'Eau', 'Flowerbomb']),
 ('Jean Carles', 'France', '1892', 'Roure perfumer and founder of its perfumery school.', 'Jean_Carles', ['Miss Dior', 'Tabu', 'Brut']),
 ('François Coty', 'France', '1874', 'Founder of Coty.', 'Fran%C3%A7ois_Coty', ['Chypre de Coty']),
 ('Johann Maria Farina', 'Italy / Germany', '1685', 'Creator of the first eau de Cologne.', 'Johann_Maria_Farina', ['Eau de Cologne (Farina)']),
 ('Ernest Daltroff', 'France', '1867', 'Founder of Parfums Caron.', 'Ernest_Daltroff', ['Tabac Blond']),
 ('Paul Parquet', 'France', '1856', 'Houbigant perfumer and joint owner.', 'Paul_Parquet', ['Fougère Royale']),
 ('Sophia Grojsman', 'United States', '1945', 'IFF perfumer.', 'Sophia_Grojsman', ['Trésor', 'White Linen']),
 ('Jacques Cavallier', 'France', '1962', 'Perfumer, now at Louis Vuitton.', 'Jacques_Cavallier', ['L\'Eau d\'Issey', 'M7']),
 ('Thierry Wasser', 'Switzerland', '', 'Guerlain in-house perfumer from 2008.', 'Thierry_Wasser', ['Tonka Impériale']),
]
for n, c, f, d, t, sig in perf:
    brands.append(B(n, c, f, P, d, W + t, sig))

trads = [{'n': 'Grasse perfumery', 'g': 'Perfume & incense', 'r': 'Grasse, Provence, France', 'p': 'Middle Ages (tanning, scented gloves) to present',
          'd': 'The Provençal town that grew from glove tanning into the centre of French perfume raw materials and manufacture.',
          'tech': 'cold enfleurage of dawn-picked flowers; essential oils, concretes, absolutes, resinoids and molecular distillation',
          'mat': 'jasmine (from the 16th century), rose, lavender, myrtle, orange blossom, mimosa',
          'forms': ['Floral fragrance', 'Absolute & CO2 extract'], 'ctr': ['Galimard (1747)', 'Molinard (1849)', 'Fragonard (1926)', 'International Perfume Museum (1989)'],
          'auth': 'Grasse-grown flower materials are scarce (under 30 tonnes of flowers a year by 2000), so origin claims need documentation.',
          's': W + 'Grasse'}]

notes = ('Old k1 "Alcohol-based perfume" became Floral fragrance; its ~70 models were redistributed: icons became archetypes (Portrait of a Lady, 1 Million, '
         'Diptyque Philosykos/Tam Dao/Do Son/Fleur de Peau), notable house scents stay as flat models in the family kinds (Diptyque range split by family; Tom Ford, Byredo, '
         'Penhaligon\'s, Kilian, Margiela Replica, Jo Malone, designer releases). Dropped as celebrity/micro-indie/SKU noise with no standing: 19-69 American Psycho, '
         'Billie Eilish Your Turn, Caeleste, DedCool (x2), Heretic, House of Mammoth, LBTY, Lore, Maya Njie, Octavia Morgan, OrdioLab, Param Sara, '
         'Phlox, Premiere Peau, Rare Beauty, Rivendare, SIAM1928, Soulvent, TALE, TERRA•T, Tory Burch, Vacation, Veronique Gabai, Victoria Beckham, YSL Babycat/MYSLF, '
         'Ralph Lauren Polo \'67, L\'Artisan 33 Abyssae, Diptyque Eau Nabati/Eau Rihla/Tempo/Volutes. Family placement of the flat models follows their names/house notes '
         '(to verify against a reference DB). Fragrantica and Parfumo returned HTTP 403 (bot wall) and were not worked around, so the axis is Michael Edwards\'s wheel via '
         'Wikipedia and Wikipedia\'s List of perfumes (house/year/perfumer). Left out for lack of a retrievable source: Amouage and Lattafa signature scents as archetypes, '
         'Baccarat Rouge 540 named clones, Miss Dior/Habit Rouge own pages, Aventus flankers, Molecule 01 launch year, CK One year. '
         'Perfumers are entered in the brands file with seg "Perfumer".')

out = {'kinds': kinds, 'brands': brands, 'traditions': trads, 'notes': notes}
p = 'work/H4/shelves/00_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print(len(kinds), 'kinds', sum(len(k['x']) for k in kinds), 'archetypes', len(brands), 'brands', os.path.getsize(p), 'bytes')
