import json, os, copy
W = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(W + 'out/J7.json'))
OLD = {d['n']: d for d in old['depts']}
KIND = {}
for dn in ['Sake & rice wine', 'Cider, perry & mead', 'Ready-to-drink & mixed packs', 'No & low alcohol']:
    for s in OLD[dn]['s']:
        for k in s['k']:
            KIND[k['n']] = k
def oe(kind, name):
    for e in KIND[kind].get('x', []):
        if e['n'] == name:
            return copy.deepcopy(e)
    raise KeyError(name)
def keep(kind, **over):
    k = copy.deepcopy(KIND[kind]); k.pop('m', None); k.pop('r', None)
    k.update(over); return k
def clean(o):
    return {a: b for a, b in o.items() if b not in ('', None, [])}

WP = 'https://en.wikipedia.org/wiki/'
JREF = 'https://jref.com/articles/japanese-sake-breweries.694/'

# ---------------- SAKE ----------------
vers = {}  # brewery -> list of versions
def addv(b, n, d='', y='', mk=''):
    vers.setdefault(b, []).append(clean({'n': n, 'mk': mk, 'y': y, 'd': d}))
def fromold(kind, name, b):
    e = oe(kind, name)
    for v in e.get('v', []):
        vers.setdefault(b, []).append(v)
    return e
SK = 'Sake (junmai, honjozo, ginjo & daiginjo)'
fromold(SK, 'Dassai', 'Asahi Shuzō (Yamaguchi)')
addv('Asahi Shuzō (Yamaguchi)', 'Dassai 45 Nigori', 'cloudy sake')
addv('Asahi Shuzō (Yamaguchi)', 'Dassai Blue Yuzu', 'infused sake')
addv('Asahi Shuzō (Yamaguchi)', 'Dassai 23 Umeshu', 'infused sake')
fromold(SK, 'Gekkeikan', 'Gekkeikan Brewery')
fromold(SK, 'Kokuryu Daiginjo Ryu', 'Kokuryū Shuzō')
vers['Kokuryū Shuzō'].insert(0, {'n': 'Kokuryu Daiginjo Ryu', 'y': '', 'd': 'Fukui daiginjo described as the first daiginjo sold nationwide'})
fromold(SK, 'Hakkaisan', 'Hakkai Jōzō')
fromold('Sparkling sake', 'Awa Hakkaisan', 'Hakkai Jōzō')
vers['Hakkai Jōzō'].append({'n': 'Awa Hakkaisan', 'd': "bottle-fermented sparkling sake made with white koji"})
fromold(SK, 'Kubota', 'Asahi Shuzō (Niigata)')
vers['Dewazakura Shuzō'] = [{'n': 'Dewazakura Oka Ginjo', 'y': '1980', 'd': "ginjo at an everyday price, credited with starting Japan's ginjo boom"}]
fromold('Nigori sake', 'Sho Chiku Bai Nigori', 'Takara Shuzō')
vers['Hakutsuru Shuzō'] = [{'n': 'Hakutsuru Sayuri', 'd': 'Nada-brewed cloudy sake'}, {'n': 'Hakutsuru Awayuki', 'd': 'sparkling sake'}]
addv('Kikusui Shuzō', 'Kikusui Honjozo Shiroki Tenryu', 'honjozo')
addv('Niigata Meijō Brewery', 'Black Chosan'); addv('Niigata Meijō Brewery', 'Koshino Kanchubai Gold Label')
addv('Raifuku Shuzō', 'Raifuku Junmai Daiginjo Aiyama', 'junmai daiginjo')
addv('Heiwa Shuzō', 'Kid Junmai', 'junmai')
addv('Matsui Shuzōten', 'Junmai Kagura Unfiltered Undiluted Midnight Blue', 'unfiltered, undiluted')
addv('Nakano Shuzō (Ōita)', 'Chiebijin Junmaishu', 'junmai')
# extras kept from the previous edition (not on the list)
extras = {
    'Yamagata': [dict(n='Takagi Shuzō', a='Juyondai', d="Maker of Juyondai, the 'fourteenth generation' label, among the most sought-after Yamagata sake.",
                      s='https://www.skurnik.com/producer/takagi-shuzo/',
                      v=[{'n': 'Juyondai Bessen Junmai Daiginjo'}, {'n': 'Juyondai Tokujo Omachi Junmai Daiginjo', 'd': 'Omachi rice'}])],
    'Hyōgo': [dict(n='Akashi Sake Brewery', a='Akashi-Tai', d='Family brewery in Akashi, Hyōgo, making Akashi-Tai, named after the Akashi sea bream and widely exported.',
                   s='https://www.diffordsguide.com/producers/287/akashi-sake-brewery-company-ltd',
                   v=[{'n': 'Akashi-Tai Junmai Daiginjo Genshu', 'd': 'undiluted'}, {'n': 'Akashi-Tai Junmai Tokubetsu'}, {'n': 'Akashi-Tai Junmai Ginjo'},
                      {'n': 'Akashi-Tai Daiginjo Genshu'}, {'n': 'Akashi-Tai Ginjo Yuzushu', 'd': 'infused sake'}, {'n': 'Akashi-Tai Shiraume Ginjo Umeshu', 'd': 'infused sake'}])],
}
roles = {'Asahi Shuzō (Yamaguchi)': None}
dup = {}
rows = []
for line in open(W + 'work/V4_J7_OTHER/sake.txt', encoding='utf-8'):
    pref, names = line.strip().split('|')
    for n in names.split(';'):
        rows.append((pref, n))
from collections import Counter
cnt = Counter(n for _, n in rows)
mapname = {('Niigata', 'Asahi Shuzō'): 'Asahi Shuzō (Niigata)', ('Yamaguchi', 'Asahi Shuzō'): 'Asahi Shuzō (Yamaguchi)',
           ('Ōita', 'Nakano Shuzō'): 'Nakano Shuzō (Ōita)'}
sake_x = []
for pref, n in rows:
    nm = mapname.get((pref, n)) or (f'{n} ({pref})' if cnt[n] > 1 else n)
    cty = 'United States' if pref == 'United States' else 'Japan'
    where = 'in the United States' if pref == 'United States' else f'in {pref} Prefecture' if pref != 'Hokkaidō' and pref != 'Tokyo' else f'in {pref}'
    if pref == 'Oregon': where = ''
    e = {'n': nm, 'd': f'Sake brewery {where}.'.replace(' .', '.'), 's': JREF, 'cty': cty, 'g': pref if pref != 'United States' else 'United States (Oregon and California breweries named by the list)'}
    if nm in vers:
        e['v'] = vers[nm]
    sake_x.append(e)
    for ex in extras.get(pref, []):
        if pref in extras and ex and extras[pref]:
            x = dict(ex); x['g'] = pref; x['cty'] = 'Japan'
            x['d'] = x['d']
            sake_x.append(x)
        extras[pref] = []
# fix: SakéOne is in Oregon
for e in sake_x:
    if e['n'] == 'SakéOne': e['d'] = 'Sake brewery in Oregon, United States.'
    if e['n'].startswith('Gekkeikan Sake'): e['d'] = 'California brewery of Gekkeikan, named by the list as a United States sake brewery.'
    if e['n'].startswith('Ozeki Sake'): e['d'] = 'United States brewery of Ozeki, named by the list as a United States sake brewery.'
    if e['n'] == 'Gekkeikan Brewery':
        e['role'] = 'landmark'
        e['d'] = 'Fushimi, Kyoto house of one of the oldest sake brewers, with a sister brewery in California.'
        e['s'] = WP + 'Gekkeikan'
        e['a'] = 'Gekkeikan'
        e['y'] = '1637'
        e['mk'] = 'Gekkeikan 1637'
    if e['n'] == 'Asahi Shuzō (Yamaguchi)':
        e['a'] = 'Dassai'; e['d'] = "Yamaguchi brewery making Dassai, a junmai daiginjo whose label number gives the polishing ratio."; e['y'] = '1990'
        e['s'] = 'https://www.nippon.com/en/features/c00618/dassai-how-a-rural-sake-brewery-took-on-the-world.html'
    if e['n'] == 'Asahi Shuzō (Niigata)':
        e['a'] = 'Kubota'; e['d'] = "Niigata brewery making Kubota, sold in named tiers."; e['s'] = 'https://palateproject.co/collections/niigata-prefecture'
    if e['n'] == 'Hakkai Jōzō':
        e['a'] = 'Hakkaisan'; e['d'] = 'Minami-Uonuma, Niigata brewery making Hakkaisan in small batches with handmade koji, from honjozo to snow-aged daiginjo.'
        e['s'] = 'https://en.imadeya.co.jp/blogs/brewery/hatsukaisan'
    if e['n'] == 'Kokuryū Shuzō': e['a'] = 'Kokuryu'; e['s'] = 'https://openers.jp/en/lounge/9883'; e['d'] = 'Fukui brewery making Kokuryu; its daiginjo Ryu is described as the first daiginjo sold nationwide.'
    if e['n'] == 'Dewazakura Shuzō': e['a'] = 'Dewazakura'; e['s'] = 'https://www.dewazakura.co.jp/en/dewazakura/01.html'; e['d'] = 'Tendō, Yamagata brewery making Dewazakura.'
    if e['n'] == 'Takara Shuzō': e['a'] = 'Sho Chiku Bai'; e['d'] = 'Kyoto brewer behind Sho Chiku Bai, with a Berkeley brewery making nigori for the United States.'; e['s'] = 'https://shop.takarasake.com/products/nigori-silky-mild'
    if e['n'] == 'Hakutsuru Shuzō': e['a'] = 'Hakutsuru'; e['d'] = 'Nada, Kobe brewery making Hakutsuru.'; e['s'] = 'https://palateproject.co/collections/hakutsuru-brewing-company'
for e in sake_x:
    e.pop('mk', None)

sake_kinds_style = lambda n, d: keep(n, nl='No named entries: sake of this style is a version under its brewery in Sake breweries (kura).', d=d if d else KIND[n]['d'])
sake_shelf1 = {'n': 'Sake', 't': OLD['Sake & rice wine']['s'][0]['t'], 'ax': 'kinds from the brewery to the style of sake it makes',
               'k': [keep(SK, n='Sake breweries (kura)',
                          d='A sake brewery (kura) and the sake it sells, graded by polishing ratio and added alcohol: junmai, honjozo, ginjo and daiginjo.',
                          nl='One entry is a sake brewery (kura); its grades, brand lines and styles are versions where its page states them.',
                          sel='Every brewery named in the fetched Japanese sake breweries list (jref.com, by prefecture, including the three United States breweries it names); two breweries kept from the previous edition (Takagi Shuzō, Akashi Sake Brewery) are marked as added. Versions are given only for breweries whose product pages were already sourced.',
                          xg='by prefecture', x=sake_x),
                     sake_kinds_style('Futsūshu', ''), sake_kinds_style('Nigori sake', ''), sake_kinds_style('Sparkling sake', ''),
                     sake_kinds_style('Infused sake', ''), sake_kinds_style('Kijōshu', ''), sake_kinds_style('Doburoku', '')]}
for k in sake_shelf1['k']:
    k.pop('x', None) if k['n'] != 'Sake breweries (kura)' else None
# Korean and Chinese
def kr(name, **o):
    e = oe(name[0], name[1]); e.update(o); return e
mk_x = [oe('Makgeolli', 'Dongdong-ju'), oe('Makgeolli', 'Ihwa-ju'), oe('Makgeolli', 'Geumjeongsanseong Makgeolli'),
        kr(('Makgeolli', 'Jangsu Saeng Makgeolli'), cty='South Korea', own='Seoul Jangsu', tier='National champion', role='landmark'),
        kr(('Makgeolli', 'Kooksoondang Makgeolli'), cty='South Korea', own='Kooksoondang')]
for e in mk_x: e['g'] = 'Traditional types' if not e.get('own') else 'Brands'
mk_k = keep('Makgeolli', nl='One entry is a named makgeolli type or a brand sold under its own name; flavours and strengths are versions.',
            sel='No whole-space reference exists; follows the fetched Wikipedia pages Makgeolli and Kooksoondang and the Asiae article on Jangsu Saeng. Brand models without a source page were removed.',
            xg='traditional types, then brands', x=mk_x)
ch_x = [oe('Cheongju', 'Gyodong Beopju'), oe('Cheongju', 'Hansan Sogok-ju'), oe('Cheongju', 'Myeoncheon Dugyeon-ju'),
        kr(('Cheongju', 'Baekseju'), cty='South Korea', own='Kooksoondang')]
for e in ch_x: e['g'] = 'Designated traditional wines' if not e.get('own') else 'Brands'
ch_k = keep('Cheongju', nl='One entry is a named cheongju or yakju, traditional or branded; flavoured editions are versions.',
            sel='No whole-space reference exists; follows the fetched Wikipedia pages Beopju and Korean alcoholic drinks. Two retail models (Sulseam Seosul, Yangchon Premium) were removed as unsourced.',
            xg='designated traditional wines, then brands', x=ch_x)
hj_x = [oe('Huangjiu', n) for n in ['Shaoxing wine', 'Huiquan jiu', 'Fujian nuomijiu', 'Honglu jiu', 'Gu Yue Long Shan', 'Kuaijishan']]
for e in hj_x:
    if e['n'] in ('Gu Yue Long Shan', 'Kuaijishan'): e['g'] = 'Shaoxing brands'; e['cty'] = 'China'
    else: e['g'] = 'Regional types'
hj_k = keep('Huangjiu', nl='One entry is a named regional type of huangjiu or a Shaoxing brand; sugar classes and age statements are versions.',
            sel='No whole-space reference exists; follows the fetched Wikipedia pages Huangjiu and Shaoxing wine.', xg='regional types, then brands', x=hj_x)
sake_shelf2 = {'n': 'Korean & Chinese rice wine', 't': OLD['Sake & rice wine']['s'][1]['t'],
               'k': [mk_k, ch_k, hj_k]}
d_sake = {'n': 'Sake & rice wine', 'mode': 'variety', 't': OLD['Sake & rice wine']['t'], 'ax': OLD['Sake & rice wine']['ax'],
          'note': 'Sake is listed by brewery and prefecture; Korean and Chinese rice wines by type and brand.',
          's': [sake_shelf1, sake_shelf2], 'b': OLD['Sake & rice wine']['b']}

# ---------------- CIDER ----------------
CIDER = WP + 'Cider'
def mkt(e, own, tier, cty=None, own_y=None, g=None, role=None):
    e['own'] = own; e['tier'] = tier
    if cty: e['cty'] = cty
    if own_y: e['own_y'] = str(own_y)
    if g: e['g'] = g
    if role: e['role'] = role
    return e
br = []
e = oe('British & Irish cider', 'Strongbow'); mkt(e, 'Heineken N.V. (through H. P. Bulmer)', 'Global group', 'United Kingdom', 2008, 'Global group · Heineken'); br.append(e)
e = oe('British & Irish cider', 'Scrumpy Jack'); mkt(e, 'Heineken N.V. (through H. P. Bulmer)', 'Global group', 'United Kingdom', None, 'Global group · Heineken'); e['s'] = WP + 'Scrumpy_Jack'; br.append(e)
e = oe('British & Irish cider', 'Aspall Suffolk Cyder'); mkt(e, 'Molson Coors', 'Global group', 'United Kingdom', 2018, 'Global group · Molson Coors'); br.append(e)
e = oe('British & Irish cider', 'Magners Irish cider'); mkt(e, 'C&C Group', 'Independent', 'Ireland', None, 'Independent · C&C Group'); e['y'] = '1999'; e['d'] = 'Irish cider from Clonmel, County Tipperary, sold as Bulmers in Ireland and as Magners elsewhere; made by C&C Group.'; br.append(e)
e = oe('British & Irish cider', 'Thatchers Somerset cider'); mkt(e, 'Thatchers', 'Independent', 'United Kingdom', None, 'Independent · family-owned'); br.append(e)
e = oe('British & Irish cider', 'Westons Herefordshire cider'); mkt(e, 'H. Weston & Sons', 'Independent', 'United Kingdom', None, 'Independent · family-owned'); br.append(e)
e = oe('British & Irish cider', "Henney's Herefordshire cider"); e['g'] = 'Independent · family-owned'; e['cty'] = 'United Kingdom'; br.append(e)
e = oe('British & Irish cider', 'Kingston Black single-variety cider'); e['g'] = 'Single-variety style'; br.append(e)
brit = keep('British & Irish cider',
            nl='One entry is a cider brand sold under its own name in Britain or Ireland; ranges, strengths and flavours are versions.',
            sel='No whole-space reference exists. Follows the fetched Wikipedia pages for Strongbow, Scrumpy Jack, Aspall Cyder, Magners, Thatchers and Westons, with the Cider article for the other brands named. Hawkstone models were removed as unsourced.',
            xg='by market tier and owner group', x=br)
fr = []
fr.append(mkt(oe('French cider', "Cidre Pays d'Auge"), '', 'x') and None) if False else None
e = oe('French cider', "Cidre Pays d'Auge"); e['g'] = 'Protected designation (Normandy)'; e['d'] = "Normandy cider appellation: pure apple juice, unpasteurised, slow-fermented and naturally conditioned in the bottle."; e['s'] = e['s']; fr.append(e)
fr.append(dict(n='Cidre Cotentin', a='Cotentin', d='Normandy cider with a protected designation of origin, named alongside Pays d\'Auge on the France.fr cider guide.', s='https://www.france.fr/en/article/cider-essential-guide-normandy-brittany/', g='Protected designation (Normandy)', cty='France'))
fr.append(dict(n='Cidre de Cornouaille', a='Cornouaille', d='Breton cider from the Cornouaille area, the only Breton cider with a protected designation of origin.', s='https://www.france.fr/en/article/cider-essential-guide-normandy-brittany/', g='Protected designation (Brittany)', cty='France'))
fr.append(dict(n='Cidre du Perche', a='Perche', d='Cider of the Perche area, recognised as a national PDO in 2020 and registered by the European Commission on 23 June 2022.', y='2022', s='https://www.inao.gouv.fr/en/cidre-du-perche-ou-perche-reconnu-aop', g='Protected designation (Normandy)', cty='France'))
e = oe('French cider', 'Eric Bordelet cidre and poiré'); e['g'] = 'Grower cider'; e['cty'] = 'France'; e['v'].append({'n': 'Bordelet Poire Granit', 'd': 'perry'}); fr.append(e)
french = keep('French cider', nl='One entry is a French cider appellation or a named grower cider; vintages and sweetness levels are versions.',
              sel='Cider appellations named by the fetched France.fr cider guide and the INAO page on Cidre du Perche; Pays d\'Auge and Bordelet from the previous edition. No complete appellation register was reached, so the list may be incomplete. Galipette Brut was removed as unsourced.',
              xg='by protected designation, then growers', x=fr)
sp = []
sa = oe('Spanish cider', 'Asturian sidra natural')
sa.update(n='Sidra de Asturias', a='Asturian sidra · sidra natural', d='Cider of Asturias with a protected designation of origin, recognised on 23 December 2005 and covering the whole principality.',
          y='2005', s='https://puninwine.com/pages/glossary/asturian-sidra', g='Protected designation', cty='Spain')
sa['v'] = [{'n': 'Sidra Natural Tradicional', 'd': 'unfiltered and still'}, {'n': 'Sidra Natural Filtrada', 'd': 'filtered still cider'}, {'n': 'Sidra Espumosa', 'd': 'sparkling'},
           {'n': 'Trabanco Tradicional Natural', 'd': 'natural cider'}, {'n': 'Trabanco Selección', 'd': 'natural cider'}, {'n': 'Trabanco Sobre la Madre', 'd': 'natural cider'},
           {'n': 'Poma Áurea D.O.P.', 'd': 'top of range'}, {'n': 'Trabanco Pecado Natural', 'd': 'natural cider'}]
sp.append(sa)
e = oe('Spanish cider', 'Basque sagardoa'); e['g'] = 'Traditional cider'; e['cty'] = 'Spain'; sp.append(e)
spanish = keep('Spanish cider', nl='One entry is a Spanish cider designation or regional tradition; styles and producers are versions.',
               sel='The Asturian DOP (fetched Punin glossary page) and the Basque tradition (Wikipedia Sagardotegi) from the previous edition. No Spanish cider register was reached.', xg='by protected designation, then tradition', x=sp)
ice = keep('Ice cider', nl='One entry is a named ice cider tradition or protected designation; producers are versions.', sel='Wikipedia Ice cider; Québec is the only protected ice cider named.', xg='by region', x=[dict(oe('Ice cider', 'Québec cidre de glace'), g='Quebec', cty='Canada')])
apf = keep('Apfelwein & Most', nl='No named entries: the kind is the end.')
intl = []
e = dict(n='Angry Orchard', d='American hard cider brand of the Boston Beer Company; about half of the US hard cider market in 2021.', y='', s=WP + 'Angry_Orchard')
mkt(e, 'Boston Beer Company', 'National champion', 'United States', None, 'North America', 'landmark'); intl.append(e)
e = dict(n='Somersby', d='Carlsberg cider launched in 2008, 4.7 % ABV.', y='2008', s=CIDER)
mkt(e, 'Carlsberg', 'Global group', 'Denmark', None, 'Europe', None); intl.append(e)
intl_k = {'n': 'International cider brands', 'a': 'Hard cider', 'd': 'Mass-market cider brands from outside Britain and France, sold under their own name.',
          'nl': 'One entry is a cider brand sold under its own name outside Britain, France and Spain; flavours and strengths are versions.',
          'sel': 'No whole-space reference exists. Brands named with an owner on the fetched Wikipedia pages Angry Orchard and Cider. Stella Artois Cidre, Cult and others on that page were left out because no owner was stated.',
          'xg': 'by region', 's': CIDER, 'tt': [['Sweetness', ['Dry', 'Medium', 'Sweet']], ['Flavour', ['Apple', 'Pear', 'Fruit']]], 'x': intl}
ff = []
e = oe('Fruit & flavoured cider', 'Kopparberg fruit cider'); mkt(e, 'Kopparbergs Bryggeri', 'Independent', 'Sweden', None, 'Independent'); ff.append(e)
e = oe('Fruit & flavoured cider', 'Rekorderlig'); mkt(e, 'Åbro Bryggeri', 'Independent', 'Sweden', None, 'Independent'); e['s'] = WP + 'Rekorderlig'; ff.append(e)
fruit = keep('Fruit & flavoured cider', nl='One entry is a fruit or flavoured cider brand sold under its own name; flavours are versions.',
             sel='Kopparberg and Rekorderlig from the previous edition; Rekorderlig checked on its fetched Wikipedia page. Ace High and Secret Seven models were removed as unsourced.', xg='by owner', x=ff)
pom = keep('Pommeau', nl='One entry is a pommeau appellation; ages and producers are versions.',
           sel='Wikipedia Pommeau and the Cider article, which describes pommeau as a Normandy aperitif of apple juice and apple brandy. Appellation status is not confirmed on a fetched page for Maine or Brittany.',
           xg='by region', x=[dict(oe('Pommeau', n), g=g, cty='France') for n, g in [('Pommeau de Normandie', 'Normandy'), ('Pommeau de Bretagne', 'Brittany'), ('Pommeau du Maine', 'Maine')]])
pe = []
e = dict(n='Herefordshire Perry', a='Three Counties perry', d='Traditional perry from perry pears grown in Herefordshire, Worcestershire and Gloucestershire, 4.0–8.5 % ABV, with a protected geographical indication.',
         s='https://assets.publishing.service.gov.uk/media/5fd363108fa8f54d6480f4fb/pfn-herefordshire-perry.pdf', g='Protected designation', cty='United Kingdom')
e['v'] = [{'n': 'Henry Westons Vintage Pear Cider', 'mk': 'Westons', 'd': 'pear cider in the same range'}]; pe.append(e)
e = oe('Perry', 'Domfrontais poiré'); e.update(n='Poiré Domfront', a='Domfrontais poiré · Poiré Domfront AOC', cty='France', g='Protected designation'); e['d'] = 'Normandy perry from the Domfront area with at least 40 % Plant de Blanc pears; AOC 2002, PDO 2006, the smallest French PDO.'; pe.append(e)
e = oe('Perry', 'Babycham'); mkt(e, 'Brothers Drinks', 'Independent', 'United Kingdom', 2021, 'Brands', 'origin'); e['y'] = '1953'; pe.append(e)
e = dict(n='Lambrini', d='Sweet sparkling perry made in Liverpool for many years by Halewood International; owned by Accolade Wines since 2021.', s=WP + 'Perry'); mkt(e, 'Accolade Wines', 'Independent', 'United Kingdom', 2021, 'Brands'); pe.append(e)
e = oe('Perry', 'Pear cider'); e['g'] = 'Brands'; pe.append(e)
perry = keep('Perry', nl='One entry is a perry designation or a perry brand sold under its own name; pear varieties and ranges are versions.',
             sel='Herefordshire Perry from its fetched UK product specification; Domfront, Babycham and Lambrini from the fetched Wikipedia pages Perry and Babycham. No register of perry brands exists. Ace Perry Cider was removed as unsourced; Bordelet Poire Granit became a version of Eric Bordelet.',
             xg='by protected designation, then brands', x=pe)
shelf_c = {'n': 'Cider & perry', 't': OLD['Cider, perry & mead']['s'][0]['t'], 'ax': 'kinds by country of tradition, then by designation or brand',
           'k': [brit, french, spanish, apf, ice, intl_k, fruit, pom, perry]}
# mead etc
mead = keep('Mead', nl='One entry is a named regional mead tradition; strengths and honey drinks of lower alcohol are versions.', sel='No whole-space reference exists; follows the fetched Wikipedia pages Mead, Tej, Chouchen and Medovukha. Lyme Bay mead and the mead-type models (cyser, pyment and others) were removed: the types are listed in the additions attribute.', xg='by region')
for e in mead['x']: pass
fw = keep('Fruit wine', nl='One entry is a named fruit wine tradition; no brands are listed.', sel='No whole-space reference exists; follows the fetched Wikipedia page Fruit wine. Eight brand models were removed as unsourced.', xg='by region')
pw = keep('Palm wine', nl='One entry is a named regional palm wine; palms and ages are versions.', sel='No whole-space reference exists; follows the fetched Wikipedia pages Palm wine and Tubâ. Nkulenu\'s Palm Drink was removed as a retail model.', xg='by region')
pq = keep('Pulque', nl='No named entries: the kind is the end.')
shelf_m = {'n': 'Mead, fruit & sap wines', 't': OLD['Cider, perry & mead']['s'][1]['t'], 'ax': 'kinds by what is fermented: honey, other fruit or plant sap', 'k': [mead, fw, pw, pq]}
d_cider = {'n': 'Cider, perry & mead', 'mode': 'variety', 't': OLD['Cider, perry & mead']['t'], 'ax': OLD['Cider, perry & mead']['ax'],
           'note': 'Cider and perry are listed by protected designation and by brand with owner; mead and sap wines by tradition.',
           'msum': 'Hard cider is the one cider market with a published brand share: Angry Orchard held half of US hard cider in 2021. No world cider ranking was found on a fetched page.',
           'ms': [{'mkt': 'US hard cider', 'who': 'Angry Orchard (Boston Beer Company)', 'share': '60 %', 'yr': 2016, 's': WP + 'Angry_Orchard', 'note': 'share of the US hard cider market, as the page states'},
                  {'mkt': 'US hard cider', 'who': 'Angry Orchard (Boston Beer Company)', 'share': '50 %', 'yr': 2021, 's': WP + 'Angry_Orchard', 'note': 'share of the US hard cider market, as the page states'}],
           's': [shelf_c, shelf_m], 'b': [x for x in []] or OLD['Cider, perry & mead']['b']}

# ---------------- RTD ----------------
rt = []
e = oe('Ready-to-drink cocktail', 'Strong Zero'); mkt(e, 'Suntory', 'Global group', 'Japan', None, 'Suntory'); rt.append(e)
e = oe('Ready-to-drink cocktail', 'Finnish long drink'); e['g'] = 'Regional style'; e['cty'] = 'Finland'; rt.append(e)
rtd_c = keep('Ready-to-drink cocktail', nl='One entry is a pre-mixed spirit drink sold under a brand or regional style; flavours and strengths are versions.',
             sel='No whole-space reference exists; the two entries come from the previous edition and the fetched Wikipedia pages Strong Zero and Lonkero. Three retail models (Mixer\'s Barcraft Paloma, Teranino Orange, The Bellini Project) were removed.', xg='by owner group, then regional styles', x=rt)
fm = []
e = oe('Flavoured malt beverage', 'Smirnoff Ice'); mkt(e, 'Diageo', 'Global group', None, 1997, 'Diageo'); fm.append(e)
e = oe('Flavoured malt beverage', 'Bacardi Breezer'); mkt(e, 'Bacardi', 'Global group', None, None, 'Bacardi'); fm.append(e)
e = oe('Flavoured malt beverage', "Mike's Hard Lemonade"); mkt(e, 'Mark Anthony Group', 'Independent', None, None, 'Mark Anthony Group'); fm.append(e)
e = oe('Flavoured malt beverage', 'Twisted Tea'); mkt(e, 'Boston Beer Company', 'Independent', 'United States', None, 'Boston Beer Company'); fm.append(e)
e = oe('Flavoured malt beverage', 'WKD'); mkt(e, 'SHS Drinks', 'Independent', 'United Kingdom', None, 'Independent'); fm.append(e)
e = dict(n='Two Dogs', d='Alcoholic lemonade launched in Australia in 1993.', y='1993', s=WP + 'Hard_seltzer', g='Independent', cty='Australia'); fm.append(e)
e = dict(n='Garage Hard Lemonade', d='Hard lemonade made by the Finnish brewery Sinebrychoff, 4.6 % ABV.', s=WP + 'Alcopop', g='Independent', cty='Finland', own='Sinebrychoff'); fm.append(e)
fmb = keep('Flavoured malt beverage', nl='One entry is a flavoured malt or spirit-based premix brand sold under its own name; flavours and strengths are versions.',
           sel='No whole-space reference exists. Owners from the fetched Wikipedia pages Smirnoff Ice, Bacardi Breezer, Mike\'s Hard Lemonade, Twisted Tea, Hard seltzer and Alcopop; WKD from the previous edition. Not Your Father\'s Root Beer was removed as unsourced.',
           xg='by owner group', x=fm)
hs = []
e = oe('Hard seltzer', 'White Claw'); mkt(e, 'Mark Anthony Group', 'National champion', 'United States', None, 'Mark Anthony Group', 'landmark')
e['d'] = 'Market-leading US hard seltzer, 60 % of the category in 2019; 5 % in the US and Canada, 4.5 % elsewhere.'; e['s'] = WP + 'White_Claw'
hs.append(e)
e = dict(n='Truly', a='Truly Hard Seltzer', d='Boston Beer Company hard seltzer launched in 2016.', y='2016', s=WP + 'Truly_Hard_Seltzer', v=[{'n': 'Truly Hard Seltzer'}, {'n': 'Truly Extra'}])
mkt(e, 'Boston Beer Company', 'National champion', 'United States', None, 'Boston Beer Company'); hs.append(e)
hs.append(dict(n='AIR', a='Alcohol Inspired Refresher', d='San Francisco hard seltzer brand of McKenzie River Corporation, launched in 2012.', y='2012', s=WP + 'Hard_seltzer', own='McKenzie River Corporation', tier='Independent', cty='United States', g='Independent'))
hs.append(dict(n='Spiked Seltzer', d='Hard seltzer from Westport, Connecticut, developed by Nick Shields; first commercial batches in November 2013.', y='2013', s=WP + 'Hard_seltzer', tier='Craft & indie', cty='United States', g='Independent'))
hsk = keep('Hard seltzer', nl='One entry is a hard seltzer brand sold under its own name; flavours and strengths are versions.',
           sel='Brands named on the fetched Wikipedia pages Hard seltzer, White Claw and Truly Hard Seltzer. High Noon was left out because no owner was stated on a fetched page. High Noon and Truly retail models became a version or were removed.', xg='by owner group', x=hs)
ws = keep('Wine spritzer', nl='One entry is a wine-based premix tradition; no brands are listed.', sel='Wikipedia Wine cooler.', xg='by origin',
          x=[dict(oe('Wine spritzer', 'Wine cooler'), g='United States', role='origin', cty='United States')]) if False else keep('Wine spritzer')
we = oe('Wine spritzer', 'Wine cooler') if 'x' in KIND['Wine spritzer'] else None
ws = keep('Wine spritzer', nl='One entry is a wine-based premix type; no brands are listed (two spritzer models were removed as unsourced).', sel='Wikipedia Wine cooler.', xg='by origin')
ws['x'] = [dict(oe('Wine spritzer', 'Wine cooler'), g='United States', role='origin', cty='United States')] if 'x' in KIND['Wine spritzer'] else []
if not ws['x']: ws.pop('x')
rad = keep('Radler & shandy', nl='One entry is a radler or shandy brand sold under its own name; flavours are versions.', sel='Stiegl from the previous edition (Wikipedia Stiegl). Monteith\'s Radler was removed as unsourced.', xg='by country',
           x=[dict(oe('Radler & shandy', 'Stiegl Radler'), g='Austria', cty='Austria')])
rtd_s = {'n': 'Ready-to-drink', 't': OLD['Ready-to-drink & mixed packs']['s'][0]['t'], 'ax': 'kinds by alcoholic base and style, then entries by owner group',
         'k': [rtd_c, fmb, hsk, ws, rad]}
d_rtd = {'n': 'Ready-to-drink & mixed packs', 'mode': 'variety', 't': OLD['Ready-to-drink & mixed packs']['t'], 'ax': OLD['Ready-to-drink & mixed packs']['ax'],
         'note': 'Market-first: brands are grouped by owner group, with the US hard seltzer shares the pages state.',
         'msum': 'In the US, White Claw and Truly together held 85 % of hard seltzer in 2019 and 75 % in 2021. Smirnoff Ice and Bacardi Breezer sit with Diageo and Bacardi; no non-US share figure was found on a fetched page.',
         'ms': [{'mkt': 'US hard seltzer', 'who': 'White Claw (Mark Anthony Group)', 'share': '60 %', 'yr': 2019, 's': WP + 'White_Claw', 'note': 'share of the category, as the page states'},
                {'mkt': 'US hard seltzer', 'who': 'White Claw and Truly together', 'share': '85 %', 'yr': 2019, 's': WP + 'Truly_Hard_Seltzer', 'note': 'combined share, as the page states'},
                {'mkt': 'US hard seltzer', 'who': 'White Claw and Truly together', 'share': '75 %', 'yr': 2021, 's': WP + 'Truly_Hard_Seltzer', 'note': 'combined share, as the page states'}],
         's': [rtd_s], 'b': OLD['Ready-to-drink & mixed packs'].get('b', [])}

# ---------------- NO & LOW ----------------
ATH = WP + 'Athletic_Brewing_Company'
BD = 'https://www.beveragedaily.com/Article/2026/03/27/alcohol-free-brand-building-athletic-and-lucky-saint'
NBC = 'https://www.nbcnews.com/business/consumer/non-alcoholic-beer-projected-overtake-ale-second-largest-beer-category-rcna209785'
nb = []
e = oe('Alcohol-free beer', 'Athletic Brewing'); e.update(d='US brewer making only non-alcoholic beer, fully fermented to under 0.5 % ABV; top-selling US non-alcoholic beer brand.', s=ATH)
mkt(e, 'Athletic Brewing Company', 'Craft & indie', 'United States', None, 'Specialist brewers', 'landmark'); e['alc'] = 'de-alcoholised'; e['y'] = '2017'
e['v'].append({'n': 'Athletic Daypack', 'y': '2021', 'd': 'sparkling hop water'}); e.pop('mk', None); nb.append(e)
nb.append(dict(n='Lucky Saint', a='Lucky Saint lager', d='UK alcohol-free lager brewed in Germany, founded by Luke Boase in 2018; described as the UK\'s top independent alcohol-free beer.', y='2018',
               s=BD, own='Lucky Saint', tier='Craft & indie', cty='United Kingdom', g='Specialist brewers', alc='de-alcoholised',
               v=[{'n': 'Lucky Saint unfiltered lager', 'd': 'flagship, bottle and draught'}]))
nb.append(dict(n='sörzero', d='Australian beer released in 2023 as "molecularly brewed" at 0.00 % ABV, developed by scientists at the University of New South Wales.', y='2023',
               s=WP + 'Low-alcohol_beer', tier='Craft & indie', cty='Australia', g='Specialist brewers', alc='alcohol-free'))
nbk = keep('Alcohol-free beer', n='Alcohol-free beer specialists', a='Alcohol-free brewers',
           d='Brewer that makes only alcohol-free or de-alcoholised beer.',
           nl='One entry is a brewer or brand that makes only alcohol-free beer; its beers are versions.',
           sel='Specialists named on the fetched pages Athletic Brewing Company, the Beverage Daily article on Athletic and Lucky Saint, and Low-alcohol beer. Alcohol-free versions of mainstream beers (Heineken 0.0, Erdinger Alkoholfrei, Guinness 0.0) stay under their parent beer in the Beer part. Eight retail models (Clausthaler, Budweiser Prohibition Brew, Beck\'s Blue, Estrella Galicia 0,0, Gösser NaturGold, Anchor Small Beer and others) belong under their parent beers or were removed.',
           xg='by owner type', x=nb)
tw = []
e = oe('Alcohol-free wine', 'Torres Natureo'); mkt(e, 'Familia Torres', 'Independent', 'Spain', None, 'Wine producers', None); e['alc'] = 'de-alcoholised'; e.pop('mk', None); e['y'] = '2008'; tw.append(e)
wk = keep('Alcohol-free wine', nl='One entry is an alcohol-free wine brand; colours and grapes are versions.',
          sel='No whole-space reference exists; Torres Natureo from the previous edition. Leitz Eins-Zwei-Zero and others were not added because no fetched page described them.', xg='by producer type', x=tw)
sw = []
e = oe('Alcohol-free sparkling wine', 'Noughty'); e['own'] = 'Thomson & Scott'; e['tier'] = 'Craft & indie'; e['alc'] = 'alcohol-free'; e['g'] = 'Wine producers'; e['cty'] = 'United Kingdom'; e.pop('mk', None); sw.append(e)
e = oe('Alcohol-free sparkling wine', 'Natureo Sparkling'); mkt(e, 'Familia Torres', 'Independent', 'Spain', None, 'Wine producers'); e['alc'] = 'de-alcoholised'; e.pop('mk', None); sw.append(e)
swk = keep('Alcohol-free sparkling wine', nl='One entry is an alcohol-free sparkling wine brand; colours are versions.', sel='Both entries from the previous edition.', xg='by producer type', x=sw)
ns = []
e = oe('Non-alcoholic spirit', 'Seedlip'); mkt(e, 'Diageo', 'Global group', 'United Kingdom', 2019, 'Global group · Diageo', 'origin'); e['alc'] = 'alcohol-free'; e.pop('mk', None); ns.append(e)
e = oe('Non-alcoholic spirit', "Lyre's"); e.update(own="Lyre's Non-Alcoholic Spirit Co.", tier='Craft & indie', cty='Australia', y='2019', g='Independent', alc='alcohol-free',
    s='https://www.businesswire.com/news/home/20200928005201/en'); e['d'] = "Range of alcohol-free analogues for classic spirits, launched in Australia in July 2019 by Mark Livings and Carl Hartmann."; e.pop('mk', None); ns.append(e)
e = oe('Non-alcoholic spirit', 'Pentire'); e.update(own='Pentire', tier='Craft & indie', cty='United Kingdom', g='Independent', alc='alcohol-free'); e.pop('mk', None); ns.append(e)
ns.append(dict(n='Ritual Zero Proof', d='Chicago zero-alcohol gin and whiskey alternatives founded by Marcus Sakey, GG Sakey and David Crooch; Diageo took a minority stake through Distill Ventures in January 2020.',
               s='https://archive.foodbev.com/news/diageo-invests-in-alcohol-free-spirits-brand-ritual-zero-proof/', own='Ritual Zero Proof', tier='Craft & indie', cty='United States', g='Independent', alc='alcohol-free'))
nsk = keep('Non-alcoholic spirit', nl='One entry is a brand of alcohol-free spirit alternatives; its expressions are versions.',
           sel='Brands from the previous edition (Seedlip, Lyre\'s, Pentire) and Ritual Zero Proof from the fetched FoodBev article; ownership checked on the Seedlip Wikipedia page and the Business Wire release for Lyre\'s.', xg='by owner type', x=ns)
ap = []
e = oe('Alcohol-free aperitif', 'Sanbittèr'); e['alc'] = 'alcohol-free'; e['own'] = 'Sanpellegrino'; e['cty'] = 'Italy'; e['g'] = 'Italian bitters'; e.pop('mk', None); ap.append(e)
e = oe('Alcohol-free aperitif', 'Crodino'); mkt(e, 'Campari Group', 'Global group', 'Italy', None, 'Italian bitters'); e['alc'] = 'alcohol-free'; e['d'] = 'Orange non-alcoholic bitter of herbal extracts in a 10 cl bottle, produced since 1965 and made by Gruppo Campari since 1995.'; e.pop('mk', None); ap.append(e)
e = oe('Alcohol-free aperitif', 'Everleaf'); e.update(own='Everleaf', tier='Craft & indie', cty='United Kingdom', g='Botanical aperitifs', alc='alcohol-free'); e['d'] = 'British zero-proof botanical aperitif made for spritzes by conservation biologist Paul Mathew; Forest, Marine and Mountain.'; e['s'] = 'https://tastingtable.com/1274537/alcohol-free-spirit-everleaf-was-inspired-by-nature'; e.pop('mk', None); ap.append(e)
apk = keep('Alcohol-free aperitif', nl='One entry is an alcohol-free aperitif brand; its expressions are versions.', sel='Three brands from the previous edition; Crodino and Everleaf checked on fetched pages.', xg='by style', x=ap)
lo = {'n': 'Low-alcohol beer & wine', 'a': 'Reduced-alcohol drinks', 'd': 'Beer, wine or cider with a stated alcohol level above 0.5 % and up to 1.2 % (UK band for low alcohol).',
      'nl': 'No named entries: the kind is the band between de-alcoholised and ordinary drinks.', 's': 'https://www.diffordsguide.com/encyclopedia/3941/bws/alcohol-free-non-alcoholic-and-low-alcohol-defined',
      'tt': [['Drink', ['Beer', 'Wine', 'Cider']], ['Band', ['Low alcohol (up to 1.2 %)', 'De-alcoholised (up to 0.5 %)', 'Alcohol-free (0.05 % or less)']]]}
NL = OLD['No & low alcohol']
d_nl = {'n': 'No & low alcohol', 'mode': 'variety',
        't': 'Brands that make only alcohol-free drinks: beer, wine, spirit alternatives and aperitifs, plus the low-alcohol band; alcohol-free versions of mainstream brands stay under their parent beer and appear in the No & low view.',
        'ax': 'What does the brand make without alcohol: beer, wine, a spirit alternative, an aperitif or a low-alcohol drink?',
        'note': 'Alcohol level (alc) follows the UK bands: alcohol-free is 0.05 % or less (or 0.0 as labelled), de-alcoholised up to 0.5 %, low alcohol up to 1.2 % (Difford\'s Guide).',
        'msum': 'IWSR figures reported in 2025 put non-alcoholic beer at about 2 % of world beer, growing 9 % in 2024 while total beer fell about 1 %. Athletic Brewing led US non-alcoholic beer with 17 % of volume.',
        'ms': [
            {'mkt': 'World non-alcoholic beer', 'who': 'Non-alcoholic beer', 'share': '2 %', 'yr': 2025, 's': NBC, 'note': 'share of world beer volume, IWSR via CNBC article of 29 May 2025; data year not stated'},
            {'mkt': 'World non-alcoholic beer', 'who': 'Non-alcoholic beer volume growth', 'share': '+9 %', 'yr': 2024, 's': NBC, 'note': 'volume growth against about -1 % for all beer, IWSR'},
            {'mkt': 'World non-alcoholic beer', 'who': 'Retail sales', 'share': 'over $17 billion', 'yr': 2023, 's': NBC, 'note': 'worldwide retail sales, Bernstein; largest buyers Germany, Spain and Japan'},
            {'mkt': 'US non-alcoholic beer', 'who': 'Athletic Brewing', 'share': '17 %', 'yr': 2025, 's': NBC, 'note': 'share of category volume, up from 4 % three years earlier; article of May 2025'},
            {'mkt': 'US non-alcoholic craft beer', 'who': 'Athletic Brewing', 'share': '61 %', 'yr': 2020, 's': ATH, 'note': 'share of US non-alcoholic craft beer'},
            {'mkt': 'US beer', 'who': 'Non-alcoholic beer', 'share': 'about 2 %', 'yr': 2026, 's': BD, 'note': 'share of total US beer sales, as stated by Athletic\'s marketing chief in a March 2026 article'},
            {'mkt': 'No-alcohol drinks, ten leading markets', 'who': 'No-alcohol segment', 'share': '7 % a year', 'yr': 2028, 's': 'https://www.foodnavigator.com/Article/2025/03/20/the-biggest-opportunities-for-alcohol-free-and-low-alcohol-drinks', 'note': 'forecast volume growth 2024 to 2028, IWSR; low and no combined 4 % a year'},
            {'mkt': 'UK alcohol-free beer', 'who': 'Alcohol-free beer', 'share': '+30 % since 2016', 'yr': 2020, 's': WP + 'Low-alcohol_beer', 'note': 'sales growth as of March 2020'}],
        's': [
            {'n': 'Alcohol-free beer specialists', 't': 'Brewers that make only alcohol-free beer, such as Athletic Brewing and Lucky Saint.', 'k': [nbk]},
            {'n': 'Alcohol-free wine', 't': 'Wine with the alcohol removed or fermentation stopped, still and sparkling.', 'k': [wk, swk]},
            {'n': 'Zero-proof spirits and aperitifs', 't': 'Alcohol-free spirit alternatives and aperitifs such as Seedlip, Lyre\'s and Crodino.', 'k': [nsk, apk]},
            {'n': 'Low-alcohol drinks', 't': 'Drinks above 0.5 % and up to 1.2 % ABV.', 'k': [lo]}],
        'b': NL.get('b', [])}
parts = {'depts': [d_sake, d_cider, d_rtd, d_nl], 'brands': [], 'renames': {
    'Sake (junmai, honjozo, ginjo & daiginjo)': 'Sake breweries (kura)', 'Alcohol-free beer': 'Alcohol-free beer specialists'}, 'moves': []}

# strip empty strings
def strip(o):
    if isinstance(o, dict):
        return {k: strip(v) for k, v in o.items() if v not in ('', None) and not (k in ('v', 'x') and v == [])}
    if isinstance(o, list):
        return [strip(i) for i in o]
    return o
parts['depts'] = strip(parts['depts'])

# brand register
exist = {b['n'] for b in json.load(open(W + 'out/J7_brands.json'))['b']}
B = [
 ('Strongbow', 'United Kingdom', '1960', 'Mainstream', 'cider', 'Heineken cider made by H. P. Bulmer.', WP + 'Strongbow_(cider)'),
 ('Scrumpy Jack', 'United Kingdom', '', 'Mainstream', 'cider', 'Strong Herefordshire cider, H. P. Bulmer since 1989.', WP + 'Scrumpy_Jack'),
 ('Aspall', 'United Kingdom', '1728', 'Premium', 'cyder', 'Suffolk cyder from Aspall Hall, Molson Coors since 2018.', WP + 'Aspall_Cyder'),
 ('Magners', 'Ireland', '1999', 'Mainstream', 'cider', 'Irish cider of C&C Group, sold as Bulmers in Ireland.', WP + 'Magners_Irish_Cider'),
 ('Thatchers', 'United Kingdom', '1904', 'Premium', 'cider', 'Family-owned Somerset cider maker.', WP + 'Thatchers_Cider'),
 ('Westons', 'United Kingdom', '1880', 'Premium', 'cider', 'Family-owned Herefordshire cider maker.', WP + 'Westons_Cider'),
 ('Angry Orchard', 'United States', '', 'Mainstream', 'hard cider', 'Boston Beer Company hard cider, about half the US market in 2021.', WP + 'Angry_Orchard'),
 ('Rekorderlig', 'Sweden', '1996', 'Mainstream', 'fruit cider', 'Swedish fruit cider made by Åbro Bryggeri.', WP + 'Rekorderlig'),
 ('Babycham', 'United Kingdom', '1953', 'Mainstream', 'perry', 'Sparkling perry, Brothers Drinks since 2021.', WP + 'Babycham'),
 ('White Claw', 'United States', '2016', 'Mainstream', 'hard seltzer', 'Mark Anthony Group hard seltzer, 60 % of US category in 2019.', WP + 'White_Claw'),
 ('Truly', 'United States', '2016', 'Mainstream', 'hard seltzer', 'Boston Beer Company hard seltzer.', WP + 'Truly_Hard_Seltzer'),
 ('Twisted Tea', 'United States', '2000', 'Mainstream', 'hard tea', 'Boston Beer Company malt-based hard iced tea.', WP + 'Twisted_Tea'),
 ("Mike's Hard Lemonade", 'United States', '1996', 'Mainstream', 'hard lemonade', "Malt-based hard lemonade started by Anthony von Mandl.", WP + 'Mike%27s_Hard_Lemonade_Co.'),
 ('Athletic Brewing', 'United States', '2017', 'Specialist', 'non-alcoholic beer', 'Connecticut brewer making only non-alcoholic beer.', ATH),
 ('Lucky Saint', 'United Kingdom', '2018', 'Specialist', 'alcohol-free lager', 'UK alcohol-free lager brand founded by Luke Boase.', 'https://www.raconteur.net/marketing-sales/lucky-saint-alcohol-free-beer'),
 ('Seedlip', 'United Kingdom', '2014', 'Specialist', 'non-alcoholic spirit', 'Distilled non-alcoholic spirits, Diageo majority-owned since 2019.', WP + 'Seedlip'),
 ("Lyre's", 'Australia', '2019', 'Specialist', 'non-alcoholic spirit', 'Alcohol-free spirit analogues launched in July 2019.', 'https://www.businesswire.com/news/home/20200928005201/en'),
 ('Ritual Zero Proof', 'United States', '', 'Specialist', 'zero-proof spirit', 'Chicago zero-alcohol gin and whiskey alternatives.', 'https://archive.foodbev.com/news/diageo-invests-in-alcohol-free-spirits-brand-ritual-zero-proof/'),
 ('Everleaf', 'United Kingdom', '', 'Specialist', 'botanical aperitif', 'Zero-proof aperitif by Paul Mathew.', 'https://tastingtable.com/1274537/alcohol-free-spirit-everleaf-was-inspired-by-nature'),
 ('Crodino', 'Italy', '1965', 'Mainstream', 'bitter aperitif', 'Non-alcoholic bitter aperitif, Gruppo Campari.', WP + 'Crodino'),
]
for n, c, f, seg, kf, d, s in B:
    if n in exist: continue
    parts['brands'].append(clean({'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 's': s}))
os.makedirs(W + 'out/J7_parts', exist_ok=True)
tmp = W + 'out/J7_parts/OTHER.json.tmp'
json.dump(parts, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, W + 'out/J7_parts/OTHER.json')
# counts
for d in parts['depts']:
    print(d['n'], [(k['n'], len(k.get('x', []))) for s in d['s'] for k in s['k']])
print(len(parts['brands']), 'brands')
