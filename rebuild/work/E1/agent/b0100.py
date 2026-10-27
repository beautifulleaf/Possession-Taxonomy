import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
M = 'Mattel'
BQ = WP + 'Bisque_doll'
BJ = WP + 'Ball-jointed_doll'
AG = WP + 'American_Girl'
fashion = K('Fashion doll', 'A styled doll with a slim adult-like or teen body, made to be dressed and posed.',
  'https://shop.mattel.com/products/barbie-fashionistas-doll-in-green-gingham-dress-hyt96', a='teen doll',
  t=['Play line', 'Collector edition', 'Mini doll'],
  x=[X('Barbie', 'The 11½-inch teen fashion doll created by Ruth Handler, with friends, family and collector editions.', M, '1959', WP + 'Barbie',
       [('Barbie Teen-age Fashion Model (#1)', M, '1959', 'zebra swimsuit, blonde or brunette'), ('Ken', M, '1961', ''),
        ('Skipper', M, '', 'sister doll'), ('Christie', M, '1968', 'first African-American friend doll'),
        ('Barbie Fashionistas', M, '2016', 'tall, petite and curvy bodies'), ('Collector colour tiers', M, '2004', 'pink, silver, gold, platinum'),
        ('Barbie Fashion Model Collection', M, '', 'collector line'), ('Bob Mackie', M, '', 'designer collector dolls'),
        ('Happy Holidays / Holiday Barbie', M, '', 'annual collector doll'), ('Dolls of the World', M, '', ''),
        ('Porcelain Treasures', M, '', 'porcelain collector dolls'), ('Vintage Reproductions', M, '', ''), ('My First Barbie', M, '', ''),
        ('Barbie Basics', M, '', ''), ('Shani', M, '', '')], dt='face mould · hair · outfit · box condition (NRFB)'),
     X('Sindy', 'British fashion doll launched as a rival to Barbie.', 'Pedigree', '1963', WP + 'Sindy',
       [('Sindy', 'Pedigree', '1963', 'launch'), ('Hasbro Sindy', 'Hasbro', '1986', 'remodelled'), ('Relaunch', 'Pedigree', '1999', ''),
        ('40th-anniversary doll', '', '2003', ''), ('60th-anniversary doll', '', '2023', '')]),
     X('Licca-chan', 'Japanese 21 cm girl doll supervised by manga artist Miyako Maki.', 'Takara Tomy', '1967', WP + 'Licca-chan',
       [('Licca-chan (first generation)', 'Takara Tomy', '1967', ''), ('Fourth generation', 'Takara Tomy', '1987', '22 cm')]),
     X('Blythe', 'Large-headed doll whose eyes change colour with a pull-string.', 'Kenner', '1972', WP + 'Blythe_(doll)',
       [('Blythe (Kenner)', 'Kenner', '1972', 'sold one year in the US'), ('Neo Blythe', 'Takara Tomy', '2001', 'revival editions')], dt='eye chips · custom face-ups'),
     X('Bratz', 'Fashion dolls with large heads and lips, launched as four friends.', 'MGA Entertainment', '2001', WP + 'Bratz',
       [('Yasmin', 'MGA Entertainment', '2001', ''), ('Cloe', 'MGA Entertainment', '2001', ''), ('Jade', 'MGA Entertainment', '2001', ''), ('Sasha', 'MGA Entertainment', '2001', '')]),
     X('Monster High', 'Teen dolls styled as children of classic monsters.', M, '2010', WP + 'Monster_High',
       [('Frankie Stein', M, '2010', ''), ('Draculaura', M, '2010', ''), ('Clawdeen Wolf', M, '2010', ''), ('Cleo de Nile', M, '2010', ''),
        ('Reboot', M, '2016', ''), ('Relaunch', M, '2022', '')]),
     X('Polly Pocket', 'Tiny dolls in a compact-shaped playset, later larger dolls.', 'Bluebird Toys', '1989', WP + 'Polly_Pocket',
       [('Compact playsets', 'Bluebird Toys', '1989', ''), ('Mattel redesign', M, '1998', 'larger doll')])])
eighteen = K('18-inch play doll', 'A soft-bodied play doll about 18 inches tall, sold with books, outfits and furniture.', AG,
  a='18-inch doll', t=['Historical character', 'Contemporary or look-alike doll'],
  x=[X('American Girl', '18-inch dolls with historical characters and their books, later contemporary and custom dolls.', 'American Girl', '1986', AG,
       [('Kirsten Larson', 'American Girl', '1986', 'first historical character'), ('Samantha Parkington', 'American Girl', '1986', ''),
        ('Molly McIntire', 'American Girl', '1986', ''), ('Girl of the Year (Lindsey Bergman)', 'American Girl', '2001', 'annual series'),
        ('Truly Me', 'American Girl', '', 'custom look-alike line, earlier American Girl of Today')]),
     X('Our Generation', '18-inch cloth-bodied dolls sized like American Girl, sold mainly through Target.', 'Battat', '',
       'https://www.pixiefaire.com/blogs/doll-tips-and-tutorials/our-generation-doll-review')])
baby = K('Baby doll', 'A doll made to look like an infant or toddler, for nurturing play.', 'https://www.americangirl.com/products/bitty-baby-twins-btd01',
  a='baby-doll', t=['Soft-bodied', 'All-vinyl', 'Interactive (drinks, wets, cries)', 'Reborn doll'], tg=['baby'],
  x=[X('Cabbage Patch Kids', 'Soft-bodied dolls sold with adoption papers, each slightly different.', 'Coleco', '1982', WP + 'Cabbage_Patch_Kids',
       [('Little People (Xavier Roberts)', '', '', 'hand-stitched originals, Babyland General Hospital'), ('Coleco Cabbage Patch Kids', 'Coleco', '1982', 'plastic heads'),
        ('Hasbro era', 'Hasbro', '1988', ''), ('Mattel era', M, '1994', ''), ('Wicked Cool Toys era', '', '2015', '')]),
     X('BABY born', 'Interactive baby doll that drinks, cries and wets.', 'Zapf Creation', '1991', WP + 'Zapf_Creation',
       [('BABY born', 'Zapf Creation', '1991', ''), ('Baby Annabell', 'Zapf Creation', '1998', ''), ('BABY born Annabell', 'Zapf Creation', '', 'from old data')]),
     X('Corolle', 'French vanilla-scented soft-bodied baby dolls.', 'Corolle', '1979', 'https://shop.corolle.com/corolle_en/about-corolle/',
       [('Calin', 'Corolle', '', '12-inch soft-bodied baby'), ('Mon Premier Poupon', 'Corolle', '', ''), ('Mon Grand Poupon', 'Corolle', '', '')]),
     X('Bitty Baby', '15-inch baby doll for children from three.', 'American Girl', '', AG, [('Bitty Baby', 'American Girl', '', ''), ('Bitty Baby twins', 'American Girl', '', 'from old data')]),
     X('Reborn doll', 'Vinyl or silicone doll repainted and weighted by an artist to look like a real newborn.', '', '1990s', WP + 'Reborn_doll',
       dt='vinyl or silicone · rooted or painted hair · weighting')])
bjd = K('Ball-jointed doll', 'A doll whose limbs and torso are joined by ball joints on elastic or string, made for posing and customising.',
  'https://volksusa.store/collections/super-dollfie', a='BJD', t=['Full size (SD, about 60 cm)', 'Mini (MSD, about 40 cm)', 'Yo-SD (about 25 cm)', 'Tiny (under 30 cm)'],
  x=[X('Super Dollfie', 'Volks resin ball-jointed doll, the first of the modern Asian BJDs.', 'Volks', '1999', WP + 'Super_Dollfie',
       [('Super Dollfie (SD)', 'Volks', '1999', 'original 57 cm, sculptor Akihiro Enku'), ('SD13', 'Volks', '2001', ''), ('Mini Super Dollfie (MSD)', 'Volks', '2001', '42 cm'),
        ('Yo-SD', 'Volks', '2004', '26.5 cm'), ('DearSD', 'Volks', '2015', ''), ('Super Dollfie Girl Ena', 'Volks', '', ''), ('Super Dollfie Girl Honoka', 'Volks', '', ''),
        ('Super Dollfie Girl Maki', 'Volks', '', ''), ('SD Boy The Happy Prince', 'Volks', '', ''), ('Super Dollfie Midi Girl Chiyo', 'Volks', '', ''),
        ('Super Dollfie Midi Girl Coco', 'Volks', '', ''), ('Super Dollfie Midi Girl Saki', 'Volks', '', ''), ('Yo-SD Boy Little Swallow', 'Volks', '', '')],
       dt='size · resin skin tone · face-up · eyes · wig'),
     X('Korean BJD', 'Resin ball-jointed dolls from Korean makers from about 2002.', '', '2002', BJ,
       [('Delf', 'Luts', '', ''), ('Minifee', 'Fairyland', '', ''), ('Dream of Doll', '', '', ''), ('Elfdoll', '', '', '')]),
     X('Chinese BJD', 'Resin ball-jointed dolls from Chinese studios.', '', '2006', BJ,
       [('Dollzone', 'Dollzone', '2006', 'original sculpts'), ('Ringdoll', '', '', '')])])
bisque = K('Antique bisque doll', 'An antique doll with a head of unglazed porcelain (bisque), mostly French or German, c. 1860–1930.',
  'https://www.1stdibs.com/buy/bisque-porcelain-dolls', a='bisque or porcelain doll',
  t=['Socket head on composition body', 'Shoulder head on kid body'],
  x=[X('French bébé', 'High-quality childlike bisque doll of the French makers.', '', '1860s', BQ,
       [('Jumeau Bébé', 'Jumeau', '', ''), ('Bru Bébé', 'Bru', '', ''), ('Steiner Bébé', '', '', ''), ('S.F.B.J. Bébé', '', '', 'later consortium dolls')]),
     X('French fashion doll', 'Adult-bodied bisque lady doll with a trousseau.', '', '1860s', BQ,
       [('Jumeau', 'Jumeau', '', ''), ('Bru', 'Bru', '', ''), ('Gaultier', '', '', ''), ('Huret', '', '', ''), ('Rohmer', '', '', '')]),
     X('German dolly-face', 'Childlike bisque dolls made in quantity in Thuringia.', '', '1890', BQ,
       [('Simon & Halbig', 'Simon & Halbig', '', ''), ('Armand Marseille 370', 'Armand Marseille', '', 'from old data'),
        ('Armand Marseille 971', 'Armand Marseille', '', 'from old data'), ('Kestner 171', 'J.D. Kestner', '', 'from old data'), ('Kämmer & Reinhardt', '', '', '')],
       dt='mould number · head mark · eyes (sleep or fixed)'),
     X('German character doll', 'Realistic character-faced bisque babies and children of the early 20th century.', '', 'early 20th century', BQ,
       [('Heubach Koppelsdorf 302', 'Heubach Koppelsdorf', '', 'from old data'), ('Happy Character Baby 152', 'Hertel Schwab', '', 'from old data'),
        ('Our Baby 152/6', 'Hertel Schwab', '', 'from old data'), ('Kestner character', 'J.D. Kestner', '', ''), ('Kämmer & Reinhardt character', '', '', '')])])
trad = K('Traditional doll', 'A doll made in a regional folk or ceremonial tradition, usually for display.', WP + 'Kokeshi',
  a='folk doll', t=['Wooden', 'Cloth', 'Ceremonial display set'],
  x=[X('Kokeshi', 'Lathe-turned Japanese wooden doll with a trunk body and painted head.', '', 'Edo period', WP + 'Kokeshi',
       [('Naruko', '', '', 'most widespread type'), ('Tsuchiyu', '', '', ''), ('Tōgatta', '', '', ''), ('Yajirō', '', '', ''), ('Sakunami', '', '', ''),
        ('Zaō Takayu', '', '', ''), ('Hijiori', '', '', ''), ('Kijiyama', '', '', ''), ('Nambu', '', '', ''), ('Tsugaru', '', '', ''),
        ('Creative kokeshi', '', '1945', 'post-war artists, free form')], dt='type · maker signature · wood'),
     X('Hina dolls', 'Japanese set of emperor, empress and court figures displayed on red tiers for Hinamatsuri.', '', '1629', WP + 'Hinamatsuri',
       [('Obina and mebina pair', '', '', 'top tier'), ('Five-tier set', '', '', ''), ('Seven-tier set', '', '', 'full set of fifteen dolls')], a='hina-ningyō'),
     X('Matryoshka', 'Russian set of painted wooden dolls that nest one inside another.', '', '1890s', WP + 'Matryoshka_doll',
       [('First set (Zvyozdochkin and Malyutin)', '', '1890s', 'Abramtsevo circle'), ('Sergiyev Posad', '', '', ''), ('Semyonov', '', '', ''),
        ('Polkhovsky Maidan', '', '', '')], a='nesting doll · babushka doll')])
clothes = K('Doll clothes & shoes', 'Clothes or shoes made for dolls.', 'https://www.americangirl.com/clothing', r=[['Bitty Baby', 'American Girl']])
pram = K("Dolls' pram", 'A pram or pushchair for dolls.', 'https://www.americangirl.com/products/bitty-baby-luxe-bassinet-stroller-jmb60',
  a='doll pushchair', m=[['Bitty Baby Luxe Bassinet Stroller', 'American Girl']])
TR = []
TR.append({'n': 'Kokeshi', 'g': 'Toys & dolls', 'r': 'Tōhoku, Japan', 'p': 'Edo period to present',
  'd': 'Lathe-turned wooden dolls first sold to hot-spring visitors, grouped into regional types.', 'tech': 'lathe turning, painting, waxing',
  'mat': 'cherry, dogwood, itaya-kaede maple', 'forms': ['Kokeshi'], 'ctr': ['Naruko', 'Tōgatta (Zaō)', 'Tsuchiyu', 'Yajirō'],
  'auth': "maker's signature on the base (usual since the 1950s); regional type features", 's': WP + 'Kokeshi'})
TR.append({'n': 'Hina-ningyō', 'g': 'Toys & dolls', 'r': 'Japan', 'p': '17th century to present',
  'd': 'Ornamental court-doll sets displayed on tiered red platforms for the 3 March girls\' festival.', 'tech': 'costumed figures',
  'mat': 'cloth, paper and carved figures', 'forms': ['Hina dolls'], 'ctr': [], 'auth': '', 's': WP + 'Hinamatsuri'})
TR.append({'n': 'Matryoshka', 'g': 'Toys & dolls', 'r': 'Russia', 'p': '1890s to present',
  'd': 'Painted nesting dolls turned from linden wood.', 'tech': 'woodturning and painting', 'mat': 'linden (lime) wood',
  'forms': ['Matryoshka'], 'ctr': ['Sergiyev Posad', 'Semyonov', 'Polkhovsky Maidan'], 'auth': '', 's': WP + 'Matryoshka_doll'})
TR = [{k: v for k, v in t.items() if v not in ('', [])} for t in TR]
brands = [
 B('Mattel', 'United States', '1945', 'Mainstream', 'Barbie', 'US toy company behind Barbie, Monster High, Polly Pocket and American Girl.', 'knowledge',
   lines=['Barbie', 'Monster High', 'Polly Pocket', 'American Girl'], sig=['Barbie']),
 B('Pedigree', 'United Kingdom', '', 'Mainstream', 'Sindy', 'Exeter toy maker that launched Sindy in 1963.', WP + 'Sindy', sig=['Sindy']),
 B('Takara Tomy', 'Japan', '', 'Mainstream', 'Licca-chan', 'Japanese toy maker of Licca-chan and the Blythe revival.', 'knowledge', sig=['Licca-chan', 'Blythe']),
 B('Kenner', 'United States', '', 'Mainstream', 'toys', 'US toy maker that first sold Blythe in 1972; later bought by Hasbro.', WP + 'Blythe_(doll)', rel=['Hasbro']),
 B('MGA Entertainment', 'United States', '', 'Mainstream', 'Bratz', 'US toy company behind Bratz; owner of Zapf Creation since 2024.', WP + 'Bratz', sig=['Bratz'], rel=['Zapf Creation']),
 B('Bluebird Toys', 'United Kingdom', '', 'Mainstream', 'Polly Pocket', 'Swindon toy maker that launched Polly Pocket; bought by Mattel in 1998.', WP + 'Polly_Pocket', rel=['Mattel']),
 B('American Girl', 'United States', '1986', 'Premium', '18-inch dolls', 'Pleasant Rowland\'s 18-inch historical doll company, owned by Mattel since 1998.', AG,
   lines=['Historical characters', 'Girl of the Year', 'Truly Me', 'Bitty Baby', 'WellieWishers'], rel=['Mattel']),
 B('Battat', '', '', 'Mainstream', 'Our Generation', 'Family toy business behind the Our Generation 18-inch dolls.', 'https://www.pixiefaire.com/blogs/doll-tips-and-tutorials/our-generation-doll-review'),
 B('Coleco', 'United States', '', 'Mainstream', 'Cabbage Patch Kids', 'US toy maker that mass-produced Cabbage Patch Kids 1982–1988.', WP + 'Cabbage_Patch_Kids'),
 B('Zapf Creation', 'Germany', '1932', 'Mainstream', 'BABY born', 'Rödental doll maker founded by Max and Rosa Zapf; maker of BABY born.', WP + 'Zapf_Creation', rel=['MGA Entertainment']),
 B('Corolle', 'France', '1979', 'Premium', 'vanilla baby dolls', 'Langeais maker of vanilla-scented baby dolls, part of Simba Dickie Group.', 'https://shop.corolle.com/corolle_en/about-corolle/'),
 B('Volks', 'Japan', '', 'Specialist', 'Super Dollfie', 'Japanese maker of Super Dollfie resin ball-jointed dolls.', WP + 'Super_Dollfie', sig=['Super Dollfie']),
 B('Luts', 'South Korea', '', 'Specialist', 'ball-jointed dolls', 'Korean ball-jointed doll company distributing Delf dolls.', BJ),
 B('Fairyland', 'South Korea', '', 'Specialist', 'Minifee', 'Korean ball-jointed doll company known for Minifee.', BJ),
 B('Dollzone', 'China', '', 'Specialist', 'ball-jointed dolls', 'Chinese resin ball-jointed doll maker, original sculpts from 2006.', BJ),
 B('Jumeau', 'France', '', 'Heritage manufactory', 'bébés', 'French maker of bisque bébés and fashion dolls, 1860s–1880s heyday.', BQ),
 B('Bru', 'France', '', 'Heritage manufactory', 'bébés', 'French maker of bisque bébés and fashion dolls.', BQ),
 B('Simon & Halbig', 'Germany', '', 'Heritage manufactory', 'bisque heads', 'German maker of bisque dolly-face and character dolls.', BQ),
 B('Armand Marseille', 'Germany', '', 'Heritage manufactory', 'bisque heads', 'German maker of mass-produced bisque dolly-face dolls.', BQ),
 B('J.D. Kestner', 'Germany', '', 'Heritage manufactory', 'bisque dolls', 'German bisque doll maker of dolly-face and character dolls.', BQ),
]
notes = ("Fashion doll: Barbie as lead archetype with sourced milestones plus significant old Mattel lines as versions; the 38-line flat range list cut "
 "(dropped minor series such as Birthstone Beauties, Zodiac Dolls, City Seasons, Stars 'n Stripes, The Heart Family); Licca-chan range became an archetype; "
 "added Sindy, Blythe, Bratz, Monster High, Polly Pocket. New kinds 18-inch play doll (American Girl, Our Generation) and Traditional doll "
 "(kokeshi, hina, matryoshka with tradition entries). Baby doll: Cabbage Patch Kids, BABY born, Corolle, Bitty Baby, Reborn. BJD: old Volks models became "
 "Super Dollfie versions; Iplehouse not added (no page names it as maker). Bisque: makers as versions of four patterns; old 'Porcelain Treasures' (Mattel) moved "
 "to Barbie versions as it is modern. Totally Hair, Malibu and Silkstone Barbie not added: the retrieved page gives no product facts.")
write('01_00', [fashion, eighteen, baby, bjd, bisque, trad, clothes, pram], brands, TR, notes)
