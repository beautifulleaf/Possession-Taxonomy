import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
FK = WP + 'Funko'; PM = WP + 'Pop_Mart'; AT = WP + 'Art_toy'; GSC = WP + 'Good_Smile_Company'; BH = WP + 'Bobblehead'
def T(n, g, r, p, d, tech, mat, forms, ctr, auth, s):
    return {'n': n, 'g': g, 'r': r, 'p': p, 'd': d, 'tech': tech, 'mat': mat, 'forms': forms, 'ctr': ctr, 'auth': auth, 's': s}
vinyl = K('Vinyl collectible figure', 'A stylised, non-articulated vinyl figure of a licensed character, sold boxed for display.', FK,
  a='Funko Pop · vinyl figure', t=['Common release', 'Chase variant', 'Convention exclusive', 'Retailer exclusive (sticker)', 'Boxed or out of box'],
  x=[X('Funko Pop!', 'Square-headed, black-eyed vinyl figures of licensed characters in numbered window boxes.', 'Funko', '2010', FK,
       [('DC Comics preview', 'Funko', '2010', 'San Diego Comic-Con'), ('Full line launch', 'Funko', '2011', 'New York Toy Fair'),
        ('Chase variant', 'Funko', '', 'rare variant, once 1 in 36, now 1 in 6'), ('Convention exclusive', 'Funko', '2006', 'Funko convention exclusives began at SDCC'),
        ('Retailer exclusive', 'Funko', '', 'exclusive stickers or labels'), ('Bitty Pop!', 'Funko', '2023', '1-inch minis')],
       dt='licence · box number · exclusive sticker · box condition'),
     X('Funko Vinyl Soda', 'Vinyl figures packed in a soda-can-style tin, with chase chances.', 'Funko', '', FK),
     X('Funko Mystery Minis', 'Small blind-boxed vinyl figures with a random character inside.', 'Funko', '', FK)])
designer = K('Designer toy', "A figure made as a collectible art object, often vinyl, from a designer's or brand's own character, often blind-packed.",
  'https://www.kidrobot.com/collections/art-toys?page=3', a='art toy · designer figure · urban vinyl',
  t=['Vinyl', 'Resin', 'Plush with vinyl face', 'Blind box', 'Secret figure', 'Platform (DIY) toy', 'Size (100% / 400% / 1000%)'],
  x=[X('Bounty Hunter Kid Hunter and Skull-Kun', 'Harajuku vinyl figures by Hikaru Iwanaga, counted among the first art toys.', 'Bounty Hunter', '1997', AT,
       [('Kid Hunter', 'Bounty Hunter', '1997', ''), ('BxH Skull-Kun', 'Bounty Hunter', '1997', '')]),
     X('Companion', "KAWS's Mickey-like figure with crossed bones on its head and with hands over its face.", 'KAWS', '1999', WP + 'Kaws',
       [('Bounty Hunter Companion', 'Bounty Hunter', '1999', "KAWS's first vinyl toy"), ('OriginalFake releases', 'Medicom Toy', '2006', 'OriginalFake store to 2013'),
        ('MoMA Companion', 'KAWS', '2017', '$200, sold out')]),
     X('Be@rbrick', 'Bear-shaped block figure in standard percentage sizes, endlessly re-decorated with collaborations.', 'Medicom Toy', '2001', WP + 'Bearbrick',
       [('First Be@rbrick', 'Medicom Toy', '2001', 'gift at World Character Convention 12, Tokyo'), ('Blind-box series', 'Medicom Toy', '', '18 figures per series in fixed themes'),
        ('400%', 'Medicom Toy', '', '28 cm'), ('1000%', 'Medicom Toy', '', '70 cm')], a='Bearbrick', dt='size (50–1000%) · series · collaboration'),
     X('Dunny', 'Rabbit-eared platform figure printed by guest artists in limited runs.', 'Kidrobot', '2004', WP + 'Kidrobot',
       [('3-inch blind-box series', 'Kidrobot', '', ''), ('8-inch', 'Kidrobot', '', 'full releases')]),
     X('Munny', 'Blank vinyl platform figure sold for owners to customise.', 'Kidrobot', '2004', WP + 'Kidrobot',
       [('Micro Munny', 'Kidrobot', '', '2 in'), ('Mini Munny', 'Kidrobot', '', '4 in'), ('Munny', 'Kidrobot', '', '7 in'), ('Mega Munny', 'Kidrobot', '', '18 in')]),
     X('Qee', 'Small keychain-size platform figure with interchangeable animal heads.', 'Toy2R', '', AT),
     X('Molly', 'Girl character by Kenny Wong, one of Pop Mart\'s main blind-box lines.', 'Pop Mart', '', PM),
     X('The Monsters (Labubu)', 'Toothy elf-rabbit monster by Kasing Lung, sold as vinyl figures and vinyl-faced plush key rings.', 'Pop Mart', '2015', WP + 'Labubu',
       [('How2Work figurines', '', '2015', 'first figures'), ('Pop Mart partnership', 'Pop Mart', '2019', ''),
        ('Exciting Macaron', 'Pop Mart', '2023', 'first key-ring line'), ('Have a Seat', 'Pop Mart', '', ''), ('Massive into Energy', 'Pop Mart', '2025', '')],
       a='Labubu', dt='series · colour · secret or regular · fakes ("Lafufu")')],
  r=[['SKULLPANDA', 'Pop Mart'], ['DIMOO', 'Pop Mart'], ['HIRONO', 'Pop Mart'], ['CRYBABY', 'Pop Mart'], ['PUCKY', 'Pop Mart'], ['Labbit', 'Kidrobot'], ['Art Giants', 'Kidrobot']])
chibi = K('Chibi figure', 'A figure with an oversized head and small body, usually with swappable faces or parts.', 'https://www.goodsmile.com/en/product/8409',
  a='super-deformed figure · Nendoroid', t=['Swappable faces and parts', 'Mini or petite'],
  x=[X('Nendoroid', 'Good Smile Company\'s chibi figures of anime, manga and game characters.', 'Good Smile Company', '', GSC,
       [('Nendoroid Denji', 'Good Smile Company', '', 'from old data')], dt='character · number · bonus parts')])
static = K('Static figure', 'A figure fixed in one pose, from prize figures to scale figures and statues, sold finished or as a kit.',
  'https://www.goodsmile.com/en/product/8950/POP+UP+PARADE+Popp', a='scale figure · statue · prize figure · garage kit',
  t=['1/7 or 1/8 scale', 'Prize figure', 'Statue', 'Garage kit (unpainted resin)', 'Loose game miniature'],
  x=[X('Good Smile scale figures', 'Painted PVC scale figures of anime, manga and game characters.', 'Good Smile Company', '', GSC,
       [('POP UP PARADE', 'Good Smile Company', '', 'lower-price range; e.g. POP UP PARADE Popp (old data)')]),
     X('Banpresto prize figures', 'Figures made as crane-game (UFO catcher) prizes, later also a high-end line.', 'Banpresto', '1990', WP + 'Banpresto',
       [('UFO catcher prizes', 'Banpresto', '1990', 'Ultraman and Kamen Rider among the first'), ('High-end Banpresto figures', 'Bandai Spirits', '2019', '')])])
bob = K('Bobblehead', 'A figure with a head on a spring or pin so that it nods.', 'https://www.figureland.co.uk/bobbleheads-382-c.asp',
  a='nodder · wobbler · nodding dog', t=['Sports giveaway', 'Licensed character', 'Custom portrait', 'Dashboard nodder'],
  x=[X('Temple nodder', 'Asian nodding figures of the Buddha and other religious figures, the earliest bobbleheads.', '', '17th century', BH),
     X('Thanjavur head-shaking doll', 'Painted clay or wood nodding doll from Tamil Nadu, shown at Navaratri.', '', '', BH, a='Thanjavur Thalayatti Bommai'),
     X('Baseball bobblehead', 'Papier-mâché and later plastic nodders of teams and players, now stadium giveaways.', '', '1960', BH,
       [('MLB team set', '', '1960', 'papier-mâché, one per team'), ('World Series player figures', '', '1960', 'Clemente, Mantle, Maris, Mays'),
        ('Birmingham Barons giveaway', '', '1997', 'minor-league stadium giveaway'), ('Willie Mays giveaway', '', '1999', 'San Francisco Giants, 35,000 made')]),
     X('Wacky Wobblers', "Funko's first line: bobbleheads of advertising and cartoon characters.", 'Funko', '1998', FK)],
  r=[['Cosbaby', 'Hot Toys'], ['Head Knockers', 'NECA']])
brands = [
 B('Funko', 'United States', '1998', 'Mainstream', 'Pop! vinyl', 'Everett, Washington maker of licensed vinyl figures, founded by Mike Becker.', FK, sig=['Funko Pop!', 'Wacky Wobblers']),
 B('Pop Mart', 'China', '2010', 'Mainstream', 'blind-box figures', 'Beijing designer-toy company founded by Wang Ning, selling artist characters in blind boxes.', PM, sig=['Molly', 'The Monsters (Labubu)']),
 B('Kidrobot', 'United States', '2002', 'Specialist', 'Dunny, Munny', 'Designer-toy company founded by Paul Budnitz.', WP + 'Kidrobot', sig=['Dunny', 'Munny']),
 B('Medicom Toy', 'Japan', '', 'Specialist', 'Be@rbrick', 'Japanese collectible-figure maker of Be@rbrick and Kubrick.', WP + 'Bearbrick', sig=['Be@rbrick'], rel=['KAWS']),
 B('Bounty Hunter', 'Japan', '', 'Artisan & independent', 'early art toys', 'Harajuku, Tokyo label behind early vinyl art toys.', AT, sig=['Bounty Hunter Kid Hunter and Skull-Kun']),
 B('KAWS', 'United States', '', 'Artisan & independent', 'Companion', 'Former graffiti artist whose Companion figures began urban vinyl collecting.', WP + 'Kaws', sig=['Companion'], rel=['Medicom Toy', 'Bounty Hunter']),
 B('Toy2R', 'Hong Kong', '', 'Specialist', 'Qee', 'Hong Kong maker of Qee platform figures.', AT, sig=['Qee']),
 B('Good Smile Company', 'Japan', '2001', 'Specialist', 'Nendoroid, scale figures', 'Tokyo figure maker founded by Aki Takanori; Nendoroid and scale figures, distributor of figma.', GSC, sig=['Nendoroid']),
 B('Banpresto', 'Japan', '1977', 'Mainstream', 'prize figures', 'Bandai-group maker of crane-game prize figures.', WP + 'Banpresto', sig=['Banpresto prize figures'], rel=['Bandai Spirits']),
]
trads = [T('Thanjavur dolls', 'Toys & dolls', 'Thanjavur, Tamil Nadu, India', '', 'Brightly painted head-shaking dolls displayed during the Dasara/Navaratri festival.',
  'clay or wood moulding and painting; balanced nodding head', 'clay, wood, paint, cloth', ['Bobblehead'], ['Thanjavur'], 'clay or wood body, 15–30 cm, hand-painted', BH)]
notes = ("New kind Vinyl collectible figure (Funko Pop!, Vinyl Soda, Mystery Minis). Designer toy: archetypes Bounty Hunter, KAWS Companion, Be@rbrick, Dunny, Munny, Qee, Molly, The Monsters (Labubu); "
 "Pop Mart range list cut to lines named on the Pop Mart Wikipedia page (Skullpanda, Dimoo, Hirono, Crybaby, Pucky); dropped 1001MOONS, AZURA, BUNNY, DUCKOO, HACIPUPU, INSTINCTOY, KUBO, Nyota, PINO JELLY, POLAR, Peach Riot, Sweet Bean, Twinkle Twinkle, Zsiga, inosoul (no retrieved source). "
 "Pop Mart plush now here via Labubu key-ring plush. Static figure: Good Smile scale (POP UP PARADE from old data) and Banpresto prize figures. "
 "Not added: Kotobukiya, Alter, Prime 1 Studio, garage-kit makers (no usable page retrieved; Kotobukiya Wikipedia title resolves to Suntory). Bobblehead: Wacky Wobblers moved from range to archetype.")
write('02_01', [vinyl, designer, chibi, static, bob], brands, trads, notes)
