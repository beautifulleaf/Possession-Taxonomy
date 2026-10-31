import json
P = '/home/user/Possession-Taxonomy/rebuild/out/A3_parts/ALL.json'
part = json.load(open(P))
brands_old = {b['n'] for b in json.load(open('/home/user/Possession-Taxonomy/rebuild/out/A3_brands.json'))['b']}
WIKI = 'https://en.wikipedia.org/wiki/'
houses = next(dp for dp in part['depts'] if dp['n'] == 'Jewellery houses & collections')

# owner data: house -> (own, tier, country, own_y)
H = {
 'Boucheron': ('Kering', 'Global group', 'France', ''), 'Qeelin': ('Kering', 'Global group', 'China', ''),
 'Fred': ('owner not stated', None, 'France', ''), 'Buccellati': ('Richemont', 'Global group', 'Italy', '2019'),
 'DoDo': ('Kering', 'Global group', 'Italy', ''), 'Pomellato': ('Kering', 'Global group', 'Italy', '2013'),
 'Chaumet': ('LVMH', 'Global group', 'France', '1999'), 'Piaget': ('Richemont', 'Global group', 'Switzerland', '1988'),
 'Messika': ('Messika', 'Independent', 'France', ''), 'David Yurman': ('David Yurman', 'Independent', 'United States', ''),
 'Harry Winston': ('owner not stated', None, 'United States', ''), 'Graff': ('owner not stated', 'Independent', 'United Kingdom', ''),
 'De Beers': ('Anglo American', 'Global group', 'United Kingdom', ''), 'Monica Vinader': ('owner not stated', 'Independent', 'United Kingdom', ''),
 'Georg Jensen': ('owner not stated', 'Independent', 'Denmark', ''), 'Swarovski': ('Swarovski', 'Global group', 'Austria', ''),
 'Thomas Sabo': ('owner not stated', 'Independent', 'Germany', ''), 'Mikimoto': ('owner not stated', 'Independent', 'Japan', ''),
 'Mejuri': ('owner not stated', 'Independent', 'Canada', ''), 'Chow Tai Fook': ('Chow Tai Fook Jewellery Group', 'Global group', 'Hong Kong', ''),
 'Chow Sang Sang': ('owner not stated', 'Independent', 'Hong Kong', ''), 'Tanishq': ('owner not stated', 'National champion', 'India', ''),
 'Kalyan Jewellers': ('owner not stated', 'National champion', 'India', ''), 'Malabar Gold & Diamonds': ('owner not stated', 'National champion', 'India', ''),
}

def ent(n, mk, s, y='', d='', g='', a='', v=None):
    e = {'n': n, 'mk': mk, 's': s, 'v': v or [], 'g': g}
    if y: e['y'] = y
    if d: e['d'] = d
    if a: e['a'] = a
    h = H.get(mk)
    if h:
        e['own'] = h[0]
        if h[1]: e['tier'] = h[1]
        e['cty'] = h[2]
        if h[3]: e['own_y'] = h[3]
    return e

def ver(n, d='', y=''):
    return {'n': n, 'y': y, 'd': d}

def kind(n, d, s, nl, sel, x, xg='single section', a='', see=None):
    k = {'n': n, 'a': a, 'd': d, 's': s, 'nl': nl, 'sel': sel, 'xg': xg, 'x': x}
    if see: k['see'] = see
    return k

def shelf(country, kinds, t=None):
    s = {'n': country, 't': t or 'Houses based in %s.' % country, 'k': kinds}
    if len(kinds) > 3:
        s['ax'] = 'Which house makes the line?'
    return s

# ---------- rebuild partial kinds with official menus ----------
def get_kind(name):
    for sh in houses['s']:
        for k in sh['k']:
            if k['n'] == name:
                return k

# Chaumet
CH = 'https://www.chaumet.com'
chx = []
for n, y, d in [('Joséphine', '2010', 'Launched in 2010, per the Wikipedia Chaumet article.'), ('Bee de Chaumet', '', ''), ('Liens', '1970s', 'First Liens collection in the 1970s; the Lien ring dates to 1977.'),
                ('Nature', '', 'Listed as Jewels by Nature on the site.'), ('Torsade de Chaumet', '', 'Listed under bridal on the site.'), ('Acrostiches', '', 'Bracelet product page on the site.')]:
    e = ent(n, 'Chaumet', CH, y, d, 'On the Chaumet site')
    if n in ('Joséphine', 'Liens'):
        e['s'] = CH
    chx.append(e)
for n, y, d in [('Premiers Liens', '2007', 'Sub-line of Liens.'), ('Attrape-moi', '2007', ''), ('12 Vendôme', '2012', 'Created for the 26th Biennale des Antiquaires.'),
                ('Bee my love', '', ''), ('Anneau', '', ''), ('Le Grand Frisson', '', ''), ('Class One', '', '')]:
    chx.append(ent(n, 'Chaumet', WIKI + 'Chaumet', y, d, 'Named in Wikipedia'))
for n in ('Chaumet Royals', 'Chaumet Precious Nature'):
    chx.append(ent(n.replace('Chaumet ', ''), 'Chaumet', CH, g='High jewellery on the site'))
chk = kind('Chaumet jewellery lines', 'Paris jeweller bought by LVMH in October 1999; Investcorp had bought it in 1987.', CH,
           'One entry is a Chaumet jewellery line named on its site or in the cited article.',
           "Every jewellery and bridal collection in the menu of Chaumet's own US site (Joséphine, Bee de Chaumet, Liens, Nature, Torsade de Chaumet, Acrostiches, and two high jewellery collections: 8 in all), then the lines Wikipedia adds. Watch lines (Hortensia, Class One watches) are left out. Complete: 15 of 15 named on the site and in the Wikipedia article.",
           chx, 'by source: Chaumet site, Wikipedia, high jewellery')
chk['x'] = [e for e in chk['x'] if e['n'] != 'Torsade']

# Pomellato
PO = 'https://www.pomellato.com'
pox = []
for n in ('Iconica', 'Nudo', 'Pomellato Together', 'Sabbia', 'Pentagoni', 'Catene', 'Collezione 1967'):
    pox.append(ent(n, 'Pomellato', PO, g='On the Pomellato site'))
for n, y in [('Capri', ''), ("M'Ama Non M'Ama", ''), ('Victoria', ''), ('Tango', ''), ('Pom Pom', '2007')]:
    pox.append(ent(n, 'Pomellato', WIKI + 'Pomellato', y, g='Named in Wikipedia'))
pk = kind('Pomellato jewellery lines', 'Milan jeweller; Kering acquired it in July 2013.', PO, 'One entry is a Pomellato collection named on its site or in the cited article.',
          "Every collection in the jewelry menu and story pages of Pomellato's own US site (7), then five more named in Wikipedia. Complete: 12 of 12 named on those pages.", pox, 'by source: site, Wikipedia')

# Piaget
PI = 'https://www.piaget.com'
pgx = [ent(n, 'Piaget', PI + '/us-en', g='On the Piaget site') for n in ('Possession', 'Piaget Cocktail', 'Piaget Rose', 'Piaget Sunlight', 'Piaget Glow')]
for n in ('Limelight', 'Tanagra'):
    pgx.append(ent(n, 'Piaget', WIKI + 'Piaget_SA', '1990s', g='Named in Wikipedia'))
pgk = kind('Piaget jewellery lines', 'Swiss house bought by the Vendôme group (now Richemont) in 1988.', PI + '/us-en', 'One entry is a Piaget jewellery line.',
           "Every jewelry link on Piaget's own US home page (5), then two 1990s lines named in Wikipedia. Watch collections on the same page (Polo, Sixtie, Andy Warhol, Altiplano, Limelight Gala) are left out. Complete: 7 of 7 named on those pages.", pgx, 'by source: site, Wikipedia')

# Messika
MS = 'https://www.messika.com/us_en/jewelry'
msn = ['Move Uno', 'So Move', 'My Twin', 'Joy', 'Move Classique', 'Move Noa', 'Move Link', 'Fiery', 'Moderniste', 'Lucky Move', 'D-Vibes', 'Groove', 'Imperial Move',
       'Move Romane', 'Gatsby', 'Move Iconica', 'Move Joaillerie', 'Move Titanium', 'Move 10th', 'Lucky Eye', 'Divine Enigma', 'Glam’Azone', 'Emotion', 'Skinny', 'My Move', 'Midnight Sun', 'Paris est une Fête']
old = {e['n']: e for e in get_kind('Messika jewellery lines')['x']}
mx = []
for n in msn:
    e = ent(n, 'Messika', MS, g='On the jewelry page')
    if n in old:
        e['v'] = old[n]['v']
    mx.append(e)
mesk = kind('Messika jewellery lines', 'Paris house founded in 2005 by Valérie Messika, known for diamonds set to move.', MS, 'One entry is a Messika collection; the gold colour of a piece is a version.',
            "Every collection in the filter of Messika's own US jewelry page (27 lines; 'Accessoires' and 'Messika Care(s)' are not lines and are left out). Gold colours are shown for the five Move lines whose product links list them. Complete: 27 of 27 on the page.", mx)

# Boucheron
BO = 'https://www.boucheron.com/us/jewelry'
bk = kind('Boucheron jewellery lines', 'Paris house founded by Frédéric Boucheron; part of Kering, whose jewellery maisons are Boucheron, Pomellato, DoDo and Qeelin.', BO,
          'One entry is a Boucheron jewellery line.',
          "Every collection link in the menu of Boucheron's own US site that names a line (Quatre, Serpent Bohème, Jack de Boucheron, Animaux de Collection); the menu's four theme pages (Nature, Couture, Architecture, Timeless) are groupings and are left out. The page returned a 404 body but carried the menu. Complete: 4 of 4 lines in the menu.",
          [ent(n, 'Boucheron', BO, g='In the site menu') for n in ('Quatre', 'Serpent Bohème', 'Jack de Boucheron', 'Animaux de Collection')], see=[['A3', 'Ring', 'Quatre ring']])
bk.pop('see', None)
# Fred
FR = 'https://www.fred.com/en_FR/home/'
fk = kind('Fred jewellery lines', 'Paris jeweller whose home page shows three collections.', FR, 'One entry is a Fred jewellery collection.',
          "Every collection linked on Fred's own French-market English home page (3). The page names no owner. Complete: 3 of 3 on the page.",
          [ent(n, 'Fred', FR, g='On the home page') for n in ('Chance Infinie', 'Force 10', 'Ombre Féline')])
# Qeelin
QE = 'https://www.qeelin.com'
qk = kind('Qeelin jewellery lines', 'Chinese-heritage fine jewellery house; part of Kering Jewelry.', QE, 'One entry is a Qeelin collection.',
          "The two collections linked on Qeelin's own home page (Yu Yi, Miracle Garden); the site has no collections index in the retrieved page. Covers 2 collections linked on the page, not a total.",
          [ent(n, 'Qeelin', QE, g='On the home page') for n in ('Yu Yi', 'Miracle Garden')])

# Italy: Buccellati, DoDo
BU = 'https://www.buccellati.com'
bux = [ent(n, 'Buccellati', BU, g='Icona collections') for n in ('Ramage', 'Rombi', 'Tulle', 'Ghirlanda', 'Macri', 'Opera', 'Hawaii', 'Étoilée')]
bux.append(ent('Romanza', 'Buccellati', BU, g='Bridal'))
buk = kind('Buccellati jewellery lines', 'Milan house; Richemont acquired 100 % in 2019 from Gansu Gangtai.', BU, 'One entry is a Buccellati collection.',
           "Every Icona collection linked on Buccellati's own home page (8) and the bridal collection Romanza; the page also links an Eternelle category, which is a category and is left out. Complete: 9 of 9 collections linked.", bux, 'by section: Icona, bridal')
DD = 'https://www.dodojewels.com/us_en'
dk = kind('DoDo jewellery lines', 'Italian charm and jewellery house; part of Kering Jewelry.', DD, 'One entry is a DoDo collection.',
          "Every collection in the menu of DoDo's own site (10); 'new-in' and 'all-collections' are listings and are left out. Complete: 10 of 10 collections.",
          [ent(n, 'DoDo', DD, g='In the site menu') for n in ('Granelli', 'Nature', 'Bollicine', 'Nodo', 'Essentials', 'Rondelle', 'Cuore', 'Luck', 'Universe', 'Pepita')])
for k in (dk,):
    pass

# US: David Yurman, Harry Winston
DY = 'https://www.davidyurman.com'
dyx = [ent('Cable', 'David Yurman', WIKI + 'David_Yurman', '', 'Signature form of the house; Rizzoli published David Yurman Cable in 2017.', 'Named in Wikipedia'),
       ent('Wedding Collection', 'David Yurman', WIKI + 'David_Yurman', '2006', '', 'Named in Wikipedia')]
for n in ('Sculpted Cable', 'Chevron', 'DY Madison', 'Chain collection (Curb Chain)'):
    dyx.append(ent(n, 'David Yurman', DY + '/collections/featured-collections.html', g='On the site'))
dyk = kind('David Yurman lines', 'New York house founded in 1980 by David and Sybil Yurman; privately held.', DY, 'One entry is a David Yurman collection.',
           "The three Featured Collections on David Yurman's own site (Chevron, DY Madison, Sculpted Cable), the Curb Chain collection linked on its home page, and Cable and the Wedding Collection from Wikipedia. Covers 6, not a total: the site has no complete collections index in the retrieved pages.",
           dyx, 'by source: site, Wikipedia')
HW = 'https://www.harrywinston.com/en/fine-jewelry'
hwn = ['Forget-Me-Not', 'Lily Cluster', 'Sunflower', 'Winston Cluster', 'HW Logo', 'Classics', 'Sparkling Cluster', 'Diamond Loop', 'Belle', 'Winston Gates', 'Winston Candy',
       'Winston Kaleidoscope', 'Traffic', 'Charms', 'Diamond Links', 'Lotus Cluster', 'Pirouette', 'Art Deco', 'Symbols']
hwk = kind('Harry Winston jewellery lines', 'New York diamond jeweller; its fine jewelry page links 19 collections.', HW, 'One entry is a Harry Winston fine-jewelry collection.',
           "Every collection linked on Harry Winston's own fine jewelry page (19). Complete: 19 of 19 on the page. The page does not name the owner.",
           [ent(n if n != 'HW Logo' else 'HW Logo', 'Harry Winston', HW, g='On the fine jewelry page') for n in hwn])

# UK: Graff, De Beers, Monica Vinader
GR = 'https://www.graff.com/uk-en/graff-signature-collections.html'
grk = kind('Graff jewellery lines', 'London diamond jeweller; its signature collections page links six jewellery collections and four engagement lines.', GR, 'One entry is a Graff collection.',
           "Every collection linked on Graff's own signature collections page: Butterfly, Tilda's Bow, Laurence Graff Signature, Icon, Icon 8, Classic Graff, and the engagement lines Paragon, Promise, Flame (Icon also has an engagement ring). Complete: 9 of 9 distinct lines linked.",
           [ent(n, 'Graff', GR, g='Jewellery collections') for n in ('Butterfly', "Tilda's Bow", 'Laurence Graff Signature', 'Icon', 'Icon 8', 'Classic Graff')] +
           [ent(n, 'Graff', GR, g='Engagement lines') for n in ('Paragon', 'Promise', 'Flame')], 'by type: jewellery, engagement')
DB = 'https://www.debeers.com'
dbk = kind('De Beers jewellery lines', 'Jewellery arm of the diamond company; De Beers Jewellers was set up in 2001 as a 50:50 venture with LVMH and renamed De Beers London in 2025.', DB, 'One entry is a De Beers jewellery collection.',
           "The collections linked on De Beers' own US home page (Lotus by De Beers, Undulation, Talisman, and a high jewellery thematic page). The page has no full collections index. Covers 3 lines linked on the page, not a total.",
           [ent('Lotus by De Beers', 'De Beers', DB, g='On the home page'), ent('Undulation', 'De Beers', DB, g='On the home page'), ent('Talisman', 'De Beers', DB, g='On the home page')])
MV = 'https://www.monicavinader.com/shop/sterling-silver-jewellery'
mvn = ['Heart Jewellery', 'Odyssey', 'MV Siren', 'Birthstones', 'MV Alta', 'Signature Link', 'Nura', 'Riva Diamonds', 'MV Linear', 'Heirloom', 'Diamond Essentials', 'Corda', 'Signature', 'Alphabet', 'Mini Gem', 'Nomade', 'Deia', 'Nura Pearl']
mvk = kind('Monica Vinader lines', 'London fine-silver and vermeil jeweller.', MV, 'One entry is a Monica Vinader collection.',
           "Every collection in the filter of the sterling silver page on Monica Vinader's own site (18). Complete: 18 of 18 in that filter; collections sold only in gold are not in this filter.",
           [ent(n, 'Monica Vinader', MV, g='In the silver filter') for n in mvn])

# Denmark: Georg Jensen
GJ = 'https://www.georgjensen.com/en-us/jewelry'
gjn = ['Archive', 'Curve', 'Daisy', 'Fusion', 'GJ Signature Diamonds', 'Hearts', 'Heritage', 'Infinity', 'Magic', "Men's Classic", 'Mercy', 'Moonlight Blossom', 'Moonlight Grapes', 'Offspring', 'Reflect', 'The Collector', 'Torun', 'WEFT']
gjk = kind('Georg Jensen jewellery lines', 'Copenhagen silversmith; its jewelry page filters 18 collections and lists the designers behind them.', GJ, 'One entry is a Georg Jensen jewellery collection.',
           "Every collection in the ProductCollection filter of Georg Jensen's own US jewelry page (18). Complete: 18 of 18 in the filter.",
           [ent(n, 'Georg Jensen', GJ, g='In the collection filter') for n in gjn])
# Germany: Thomas Sabo
TS = 'https://unternehmen.thomassabo.com/brandworld-en.html'
tsx = []
for n, y in [('Charm Club', '2005'), ('Charming Collection', ''), ('Generation Charm Club', '2018'), ('Karma Beads', '2014'), ('Love Bridge', '2015'), ('Glam & Soul', ''),
             ('Rebel at Heart', '2007'), ('Fine Jewellery Collection', '2014'), ('Sterling Silver', ''), ('TS Exclusive', '')]:
    tsx.append(ent(n, 'Thomas Sabo', TS, y, g='Named on the brand world page'))
tsk = kind('Thomas Sabo jewellery lines', 'German jeweller founded in 1984.' if False else 'German jewellery house that launched Charm Club in 2005.', TS, 'One entry is a Thomas Sabo collection named on the brand page.',
           "Every jewellery collection named on Thomas Sabo's company brand world page (10); the Thomas Sabo Edition car models are not jewellery and are left out. Complete: 10 of 10 named.", tsx)
# Austria: Swarovski (replace)
SW = 'https://www.swarovski.com/en-BE/s-swarovski-hero-families'
swx = [ent(n, 'Swarovski', SW, g='Signature collections') for n in ('Millenia', 'Matrix', 'Lucent', 'Constella', 'Dextera')]
swx += [ent('Atelier Swarovski', 'Swarovski', WIKI + 'Swarovski', '', 'Designer label; the article cites a WWD report of 28 February 2014 on Viktor & Rolf designing for it.', 'Named in Wikipedia'),
        ent('Snowflake', 'Swarovski', WIKI + 'Swarovski', '2004', 'Pendant and brooch collection dated 2004 in an image caption.', 'Named in Wikipedia')]
swk = kind('Swarovski jewellery lines', 'Austrian family-held company founded in 1895; its crystal business had about €2.7 billion sales in 2018.', SW, 'One entry is a Swarovski jewellery collection.',
           "The five signature collections on Swarovski's own Belgian-market page, then two collections from Wikipedia. Complete: 5 of 5 signature collections; the US collections page was not retrievable, so other lines are missing.",
           swx, 'by source: signature page, Wikipedia')
# Japan: Mikimoto
MK = 'https://www.mikimoto.com/jp_en/jewellery/collections/mikimoto-m-collection'
mkk = kind('Mikimoto jewellery lines', 'Japanese pearl jeweller.', MK, 'One entry is a Mikimoto jewellery collection.',
           "Every collection in the menu of Mikimoto's own Japan-market page (8). Complete: 8 of 8 in that menu; other collections in the site's navigation (Jeux de Rubans, Fortune Leaves, Mikimoto Bloom, Conch Pearl) did not appear in the retrieved page.",
           [ent(n, 'Mikimoto', MK, g='In the menu') for n in ('Les Pétales Place Vendôme', 'Lucky Arrows', 'Bow Charm', 'Mikimoto Ocean', 'V Code', 'M Collection', 'M Signature', 'Kofuku no ki')])
# Canada: Mejuri
MJ = 'https://mejuri.com'
mjk = kind('Mejuri lines', 'Toronto jeweller of everyday fine jewellery.', MJ, 'One entry is a Mejuri collection.',
           "The one collection named in a menu link on Mejuri's own home page (Open Dome); the other links are product pages (Vera, Mina, Etta, Lucia) and sale or category pages. Covers 1, not a total.",
           [ent('Open Dome', 'Mejuri', MJ, g='In the menu')])
# Hong Kong: CTF, CSS
CT = 'https://www.chowtaifook.com/zh-hk/eshop/jewellery/collections'
ctn = ['傳頌', '傳喜', '傳福', '萬相', '傳承', '鎖願', '韓美林', '故宮', 'ING', '牽囍', 'MONOLOGUE', 'HEARTS ON FIRE', '迪士尼', 'chiikawa', '多啦A夢', '蠟筆小新', '櫻桃小丸子', '角落小夥伴',
       '無盡對決', '敢愛', '花月佳期', '情約', '串串心思', '祈福飾品', '寓意飾品', '招財貓', '貔貅', 'CTF HOME', '至真系列 - LUNA玥', '周大福 x MCM聯名系列', '鈴蘭', '金漚浮釘', '星旅', '黑神話', '友禮系列',
       'CTF Pet', '周大福 x NBA', '周大福 x 海洋公園聯名系列', 'Coco Cat', '迪士尼公主', '迪士尼經典', '迪士尼小熊維尼', '唯愛', '驕人', '經典', 'Forevermark 婚嫁', '怦然', 'Forevermark 擁諾',
       'Forevermark 八‧玲瓏', '小心意', 'Forevermark 心欣愛', '愛相牽', '漫威', '星球大戰', '迪士尼 Tsum Tsum', '迪士尼與彼思「反斗奇兵」', '晶鑽光芒', '17916', '愛在心弦', '情繫系列', '相綴',
       'LIT', 'Vera Wang Love', 'Memoire', 'DD', '夜空', 'The Dream Series', 'Pixar', '471', '周大福「愛・燦若星辰」', 'Forevermark Icon', '小點滴', 'Forevermark Avaanti', 'MONOLOGUE Light Boom',
       'MONOLOGUE 當局者潮', '周大福國韻•傳承', '觸動愛', '周大福韓美林藝術 • 生肖', '周大福藏蘊•傳承', '周大福如來敦煌•傳承', '周大福韓美林 • 傳承', 'MONOLOGUE 北緯三十度', '599',
       '周大福人生四美', '周大福流金歲月', 'CTF ING x D', '小心意 - 幻變隨心', '周大福盛世華彩·傳承', 'ING 諾', 'ING 圓', '敢愛系列', '周大福 x CLOT', '天圓地方系列', '周大福傳承·新春', '萬相系列', 'SOINLOVE']
zod = ['鼠年生肖', '牛年生肖', '虎年生肖推廣', '兔年生肖推廣', '龍年生肖推廣', '蛇年生肖推廣', '馬年生肖推廣', '羊年生肖推廣', '猴年生肖推廣', '雞年生肖推廣', '狗年生肖推廣', '豬年生肖推廣']
ctx = []
seen = set()
for n in ctn:
    if n in seen: continue
    seen.add(n)
    ctx.append(ent(n, 'Chow Tai Fook', CT, g='On the collections page'))
ctx.append(ent('生肖 (zodiac year collections)', 'Chow Tai Fook', CT, g='On the collections page', v=[ver(z) for z in zod]))
ctk = kind('Chow Tai Fook collections', 'Hong Kong jeweller founded in 1929 per its site; the group made HK$94.4 billion in the year to March 2026.', CT, 'One entry is a Chow Tai Fook collection or series named on its collections page.',
           "Every series named on the Hong Kong collections page of Chow Tai Fook's own e-shop, in Chinese as shown (%d series, with the twelve zodiac-year promotions as versions of one entry). Watch brands listed in the same filter (Rolex, Tudor) and a technical code were left out; some entries are licensed characters (Disney, Doraemon, Chiikawa). Complete: %d of %d named on the page." % (len(ctx), len(ctx), len(ctx)), ctx, 'single section')
CS = 'https://www.chowsangsang.com/en/collections'
cs_own = ['Charme', 'Chinese Gifting Collection', 'Chinese Wedding Collection', 'Cultural Blessings', 'Daily Luxe', 'Diamond Symphony', 'EMPHASIS', 'Essence', 'g* Collection', 'Gold Rhyme',
          'IL REGALO', 'Infini Love Diamond', 'La Pelle', 'Minty Collection', 'MintyGreen', 'PROMESSA', 'Weave', 'YuYu']
cs_lic = ['Kashikey', 'Marco Bicego', 'Noir', 'Sanrio characters', 'V&A']
csx = [ent(n, 'Chow Sang Sang', CS, g='Own collections') for n in cs_own] + [ent(n, 'Chow Sang Sang', CS, g='Licensed and international selections') for n in cs_lic]
csk = kind('Chow Sang Sang collections', 'Hong Kong jeweller whose collections page lists its own series and international selections.', CS, 'One entry is a Chow Sang Sang collection.',
           "Every collection on Chow Sang Sang's own English collections page (23); the split between own and international follows the page's description of own collections and international selections but the page does not mark each line, so the grouping is by name. Complete: 23 of 23 on the page.",
           csx, 'by origin: own, licensed or international')
# India
TQ = 'https://www.tanishq.co.in/collections'
tqk = kind('Tanishq collections', 'Indian jewellery retailer; its online store lists seven collections.', TQ, 'One entry is a Tanishq collection.',
           "Every collection named on Tanishq's own online store collections page (7). Complete: 7 of 7 on the page.",
           [ent(n, 'Tanishq', TQ, g='On the collections page') for n in ('Mia', 'Rivaah', 'Zoya', 'Nakshatra', 'Diva', 'Mirai', 'Dazzling Diamonds')])
KJ = 'https://www.kalyanjewellers.net'
kjk = kind('Kalyan Jewellers collections', 'Indian jewellery retailer based in Kerala.', KJ, 'One entry is a Kalyan Jewellers named collection or sub-brand.',
           "Every named collection on Kalyan Jewellers' own home page (12), several of which are sub-brands. Complete: 12 of 12 named on the page.",
           [ent(n, 'Kalyan Jewellers', KJ, g='On the home page') for n in ('Ziah', 'Laya', 'Glo', 'Hera', 'Candere', 'Mudhra', 'Nimah', 'Anokhi', 'Rang', 'Vedha', 'Tejasvi', 'Apoorva')])
MA = 'https://www.malabargoldanddiamonds.com'
mak = kind('Malabar Gold & Diamonds collections', 'Indian jewellery retailer; the US home page names five collections.', MA, 'One entry is a Malabar named collection.',
           "Every named collection on the US home page of Malabar Gold & Diamonds (5). Covers 5; the Indian site's wider range of collections was not retrieved.",
           [ent(n, 'Malabar Gold & Diamonds', MA, g='On the US home page') for n in ('Vyana', 'Nuwa', 'Enigma', 'Zoul', 'Legendz')])

# ---------- assemble shelves ----------
byname = {k['n']: k for sh in houses['s'] for k in sh['k']}
byname['Chaumet jewellery lines'] = chk
byname['Messika jewellery lines'] = mesk
byname['Pomellato jewellery lines'] = pk
byname['Piaget jewellery lines'] = pgk
byname['David Yurman lines'] = dyk
byname['Swarovski jewellery lines'] = swk
cart, vca, bul, tif, pan, cho = (byname[n] for n in ('Cartier jewellery lines', 'Van Cleef & Arpels jewellery lines', 'Bulgari jewellery lines', 'Tiffany & Co. jewellery lines', 'Pandora jewellery lines', 'Chopard jewellery lines'))
houses['s'] = [
 shelf('France', [cart, vca, chk, mesk, bk, fk, qk], 'Paris houses.'),
 shelf('Italy', [bul, pk, buk, dk]),
 shelf('United States', [tif, dyk, hwk]),
 shelf('United Kingdom', [grk, dbk, mvk]),
 shelf('Switzerland', [cho, pgk]),
 shelf('Denmark', [pan, gjk]),
 shelf('Austria', [swk]),
 shelf('Germany', [tsk]),
 shelf('Japan', [mkk]),
 shelf('Canada', [mjk]),
 shelf('Hong Kong', [ctk, csk]),
 shelf('India', [tqk, kjk, mak]),
]
for sh in houses['s']:
    if len(sh['k']) > 3:
        sh['ax'] = 'Which house makes the line?'

# ---------- market panel ----------
houses['ms'] += [
 {'mkt': 'Kering "Other Houses" (the jewellery houses are reported inside it in 2025)', 'who': 'Kering', 'share': 'EUR 2,900 million revenue', 'yr': 2025,
  's': 'https://mfn.se/all/a/kering/kering-2025-results-sequential-improvement-unlocking-the-next-phase-of-sustainable-and-profitable-growth-df4cbf96',
  'note': 'Down from EUR 3,221 million in 2024; recurring operating income EUR -112 million. The release gives no separate Kering Jewelry revenue; Boucheron grew at double-digit rate in Q4'},
 {'mkt': 'De Beers ownership', 'who': 'Anglo American', 'share': '85 % (Government of Botswana 15 %)', 'yr': 2026,
  's': WIKI + 'De_Beers', 'note': 'Wikipedia states Anglo American announced in May 2024 that it would sell or spin off De Beers; no outcome is on the page'},
]
houses['msum'] = houses['msum'].replace("Kering formed Kering Jewelry for Boucheron, Pomellato (bought 2013), DoDo and Qeelin; the cited article gives no revenue.",
    "Kering formed Kering Jewelry for Boucheron, Pomellato (bought 2013), DoDo and Qeelin; its 2025 results release does not give a separate figure for it and reports the houses inside Other Houses (EUR 2.9 billion, recurring operating loss EUR 112 million), where Boucheron grew at a double-digit rate in the fourth quarter. De Beers is 85 % Anglo American and 15 % Government of Botswana.")
houses['msum'] = houses['msum'].replace("Independents named in the houses section are Messika, Chopard and David Yurman.",
    "National jewellery chains with named collections are Chow Tai Fook and Chow Sang Sang (Hong Kong) and Tanishq, Kalyan and Malabar (India); no fetched page gives their revenue or share, except Chow Tai Fook. Independents named in the houses section include Messika, Chopard, David Yurman, Graff, Georg Jensen, Monica Vinader, Mikimoto, Thomas Sabo and Mejuri.")
houses['note'] = 'Lines come from each house’s own collections page or menu where it could be fetched (twenty-five houses), otherwise from Wikipedia. Owner groups, tiers and market figures are in the market summary. Famous single stones are not possessions anyone buys and are left out.'

# ---------- Traditional: Indian regional forms ----------
trad = next(dp for dp in part['depts'] if dp['n'] == 'Traditional & regional jewellery')
existing = {k['n'].lower() for dp in part['depts'] for sh in dp['s'] for k in sh['k']}
TN = WIKI + 'Jewellery_of_Tamil_Nadu'
AS = WIKI + 'Assamese_jewellery'
tn = [('Pattam', 'Forehead ornament worn by bride and groom at weddings.'), ('Rakkodi', 'Ornament at the back of the head that holds a bunch of tied hair.'),
      ('Thirugupoo', 'Round hair ornament with a screw-type back, worn at the centre of the head.'), ('Kunjam', 'Tassel tied at the end of the braid.'),
      ('Jimikki', 'Ear stud or bell-shaped earring.'), ('Makara kuzhai', 'Fish-shaped ear ornament.'), ('Pampadam', 'Hollow gold earring with ball and lac-filled square designs, worn by older women.'),
      ('Mookuthi', 'Nose stud.'), ('Naththu', 'Nose ring worn on the edge of a nostril.'), ('Bullakku', 'Ornament hanging from the septum.'),
      ('Thaali', 'Marriage pendant tied by the groom; its shape varies by caste.'), ('Maangamaalai', 'Long chain with mango-shaped motifs set with stones.'),
      ('Kaasu Maalai', 'Long chain of gold coins.'), ('Vettrilai Kovai', 'Long chain of betel-leaf-shaped pendants.'), ('Nagothu', 'Armband shaped like a snake.'),
      ('Oddiyanam', 'Belt that tightens the sari at the hip.'), ('Silambu', 'Hollow ring-shaped anklet that may hold stones, silver balls or beads.'),
      ('Sathangai', 'Anklet with small silver bells, used by classical dancers.'), ('Metti', 'Toe ring placed on the second toe by the groom at weddings.'),
      ('Arasala', 'Gold or silver peepal-leaf ornament worn by baby girls at the waist.')]
tnk = []
for n, dd in tn:
    if n.lower() in existing: continue
    tnk.append({'n': n, 'a': '', 'd': dd, 's': TN})
asm = [('Junbiri', 'Assamese neck ornament.'), ('Dholbiri', 'Assamese neck ornament, also called Motabiri.'), ('Dugdugi', 'Assamese neck ornament.'), ('Gamkharu', 'Assamese wrist ornament.'),
       ('Muthi Asan', 'Assamese wrist ornament.'), ('Keru', 'Assamese ear ornament.'), ('Lokaparo', 'Assamese ear ornament.'), ('Thuria', 'Assamese ear ornament.'),
       ('Senpata', 'Assamese finger ornament.'), ('Kakali', 'Assamese waist ornament.')]
ask = [{'n': n, 'a': '', 'd': dd, 's': AS} for n, dd in asm if n.lower() not in existing]
oth = [('Sarpech', 'Turban ornament worn by Hindu, Sikh and Muslim princes; 16th and 17th century versions resembled a plume on the right of the turban.', WIKI + 'Sarpech'),
       ('Chudamani', 'Lotus-shaped, often gem-set ornament worn at the centre of a knot of hair; brides in Maharashtra wear it, where it is called khopa.', WIKI + 'Chudamani'),
       ('Mohra', 'Necklace of gold coins that a Sikh bride wears at the wedding.', WIKI + 'Mohra_(necklace)'),
       ('Kolhapuri saaj', 'Necklace named after Kolhapur in Maharashtra.', WIKI + 'Kolhapuri_saaj'),
       ('Nose chain', 'Chain joining a nose piercing to an ear piercing, worn in South Asia and Sudan.', WIKI + 'Nose_chain'),
       ('Kunukku', 'Gold earring worn on the upper earlobes by Saint Thomas Christian women in Kerala.', WIKI + 'Kunukku')]
otk = [{'n': n, 'a': '', 'd': dd, 's': s} for n, dd, s in oth if n.lower() not in existing]
trad['s'].append({'n': 'Regional Indian jewellery', 't': 'Named forms of one Indian region or community, from the Wikipedia articles cited on each kind; the general forms and the pan-Indian ones are under South Asian jewellery.',
                  'ax': 'Which region or community wears the form: Tamil Nadu, Assam, Maharashtra, Kerala or a princely court?',
                  'k': tnk + ask + otk})
trad['note'] = trad['note'].replace('the 36-type Indian jewellery guide', 'Wikipedia Jewellery of Tamil Nadu, Assamese jewellery and six Category:Jewellery of India articles (Category lists 26 pages; Patwa is a caste and Safed chalwan an enamel, not forms, and Aranjanam, Chura, Kara, Payyannur Pavithra ring, Silver Filigree of Karimnagar and Swamy Jewellery were not read and are not yet kinds), the 36-type Indian jewellery guide')
trad['note'] += ' The Berber article was read to its end (the text after 100,000 characters is references only).'

# ---------- brands ----------
brands = part['brands']
names = {b['n'] for b in brands} | brands_old
def nb(n, c, seg, d, s, kf=''):
    if n in names: return
    names.add(n)
    brands.append({'n': n, 'c': c, 'f': '', 'seg': seg, 'd': d, 'lines': [], 'eras': [], 'sig': [], 'sc': [], 'rel': [], 's': s, 'kf': kf})
nb('Anglo American', '', 'Luxury house', 'Mining group that holds 85 % of De Beers.', WIKI + 'De_Beers', 'diamond owner')
nb('Titan', 'India', 'Mainstream', 'Not used: owner of Tanishq is not stated on any fetched page.', WIKI + 'De_Beers') if False else None
bu = part['brand_updates']
for k, v in H.items():
    name = {'DoDo': 'Dodo', 'Chow Tai Fook': 'Chow Tai Fook', 'De Beers': 'De Beers'}.get(k, k)
    if name in names:
        u = {'own': v[0], 'c': v[2]}
        if v[1]: u['tier'] = v[1]
        bu[name] = u
json.dump(part, open(P, 'w'), ensure_ascii=False, indent=1)
print(len(json.dumps(part)) / 1e6, 'MB')
