import json, re, copy, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data_houses as H

ROOT = '/home/user/Possession-Taxonomy/'
old = json.load(open(ROOT + 'rebuild/out/B5.json'))
OD = {d['n']: d for d in old['depts']}
W = H.W
LOG = []

def yr(y):
    m = re.search(r'\d{4}', y or '')
    return int(m.group()) if m else 9999

def ver(n, y='', d='', mk=''):
    return {'n': n, 'mk': mk, 'y': y, 'd': d}

def clean_v(v):
    v = dict(v)
    if v.get('d') in ('From old data',):
        v['d'] = ''
    return v

def find_kind(dept, name):
    for s in dept['s']:
        for k in s['k']:
            if k['n'] == name:
                return k
    raise KeyError(name)

# ---------- Tableware ----------
tw = copy.deepcopy(OD['Tableware'])
cp = find_kind(tw, 'China pattern')
old_patterns = cp.pop('x')

house_for_mk = {
    'Meissen': 'Meissen', 'Spode': 'Spode', 'Royal Copenhagen': 'Royal Copenhagen', 'Herend': 'Herend',
    'Wedgwood': 'Wedgwood', 'Villeroy & Boch': 'Villeroy & Boch', 'Portmeirion': 'Portmeirion',
    'Bing & Grøndahl': 'Bing & Grøndahl', 'Homer Laughlin China Company': 'Fiesta',
    'Steubenville Pottery': 'Steubenville Pottery', 'T. G. Green': 'T. G. Green', 'Arabia': 'Arabia',
    'Iittala': 'Iittala', 'Heath Ceramics': 'Heath Ceramics', 'Rosenthal': 'Rosenthal', 'Noritake': 'Noritake',
    'Corelle': 'Corelle', 'Royal Albert': 'Royal Albert', 'Emma Bridgewater': 'Emma Bridgewater',
    'Hornsea': 'Hornsea', 'Midwinter': 'Midwinter', 'Anchor Hocking': 'Anchor Hocking', 'Pyrex': 'Pyrex',
    '': 'Deruta',
}
pat_versions = {}   # house -> list of versions
for p in old_patterns:
    h = house_for_mk[p.get('mk', '')]
    lst = pat_versions.setdefault(h, [])
    lst.append(ver(p['n'], p.get('y', ''), p['d'], p.get('mk', '')))
    for v in p.get('v', []):
        v = clean_v(v)
        if v['n'] != p['n']:
            lst.append(v)

def addv(h, n, y='', d='', mk=None):
    pat_versions.setdefault(h, []).append(ver(n, y, d, h if mk is None else mk))

# patterns from pages fetched in this pass
addv('Meissen', 'Swan Service', '1737-1743', 'Made for Count Heinrich von Brühl; more than a thousand pieces.')
addv('Meissen', 'Osier', '1745', 'Relief border imitating woven wicker, presumed to be by Kaendler.')
addv('Meissen', 'Möllendorff Dinner Service', '1760s', 'Large service of the 1760s.')
addv('Meissen', 'Court Dragon', 'c. 1734', 'Chinese-style dragon design.')
addv('Wedgwood', "Queen's Ware", '1767', 'Creamware whose name Queen Charlotte approved in 1767.')
addv('Wedgwood', 'Frog Service', '1774', 'Dinner and dessert service made for Catherine the Great of Russia.')
addv('Noritake', 'Sedan', '1914', "The company's first Western-style dinner set.")
addv('Villeroy & Boch', 'Brindille', '1770', 'Gadrooned decor later sold as Alt Luxemburg or Vieux Luxembourg.')
addv('Villeroy & Boch', 'Kugel', '1971', 'Sphere-shaped pack holding a 19-piece dinner service, by Helen von Boch.')
addv('Villeroy & Boch', 'Mariposa', '1989', 'Forty-one-piece coffee service.')
addv('Rosenthal', 'Service 2000', '1954', 'Designed by Raymond Loewy and Richard Latham.')
addv('Rosenthal', 'Romanze', '1959', 'Service designed by Bjørn Wiinblad.')
addv('Rosenthal', 'TAC tea service', '', 'Tea service designed by Walter Gropius.')
addv('Royal Crown Derby', 'Imari-style patterns', '', 'Brightly coloured Japanese Imari patterns produced under Robert Bloor.')
addv('Richard-Ginori', 'Tulip', '', 'Large stylised peony in iron-red shades, despite the name.')
addv('Richard-Ginori', 'Rooster', '', 'Black, red and gold, later red and gold; after Kangxi-period Chinese porcelain.')
addv('Denby', 'Chevron', '1950s-1960s', 'Designed by Gill Pemberton.')
addv('Kutani ware', 'Ko-Kutani', '17th century', 'Old Kutani of the 17th and early 18th centuries, in aote and iroe styles.', mk='')
addv('Kutani ware', 'Kutani Gosai', '', 'Classical five-colour style of green, blue, yellow, purple and red.', mk='')
addv('Kutani ware', 'Saikō-Kutani', '19th century', 'Revived Kutani with red and gold decoration.', mk='')
addv('Arita ware', 'Imari', 'late 17th century', 'Underglaze blue with red, gold and black overglaze, shipped from Imari.', mk='')
addv('Arita ware', 'Kakiemon', '', 'Brightly coloured overglaze style, widely imitated in Europe.', mk='')
addv('Arita ware', 'Nabeshima', 'late 17th century', 'Overglaze wares for the Nabeshima lords; never exported at the time.', mk='')
addv('Iittala', 'Teema', '1952', 'Designed by Kaj Franck as Kilta; renamed Teema in 1981.')
addv('Chelsea', 'Rabbit tureen', '', 'Chelsea porcelain tureen in the form of a rabbit.', mk='Chelsea porcelain')
# Kilta/Teema belongs to Arabia in the old data; avoid the Iittala duplicate
pat_versions['Iittala'] = [v for v in pat_versions['Iittala'] if v['n'] != 'Teema']
addv('Georg Jensen', '', '')  # placeholder removed below
pat_versions.pop('Georg Jensen')

SRC_FIX = {}
tw_entries = []
for r in H.T:
    e = {'n': r['n'], 'a': r['a'], 'd': r['note'], 'mk': '', 'y': r['y'], 's': r['s'], 'v': [], 'g': r['c'], 'cty': r['c']}
    if r['own']:
        e['own'] = r['own']
        e['tier'] = r['tier']
        if r['oy']:
            e['own_y'] = r['oy']
    tw_entries.append(e)
by_name = {e['n']: e for e in tw_entries}
missing = [h for h in pat_versions if h not in by_name]
assert not missing, missing
for h, vs in pat_versions.items():
    seen = set(); out = []
    for v in vs:
        if v['n'] in seen: continue
        seen.add(v['n']); out.append(v)
    by_name[h]['v'] = out
assert len(by_name) == len(tw_entries), 'duplicate tableware house'
# Arabia: pattern versions; Kilta/Teema keep
tw_entries.sort(key=lambda e: (e['g'], yr(e['y']), e['n'].lower()))
cp['n'] = 'Tableware house'
cp['a'] = 'porcelain house · pottery · china manufacturer · china pattern'
cp['d'] = 'Porcelain, bone china, earthenware or stoneware house, or the kiln tradition behind one, collected by house and then by named pattern.'
cp['s'] = H.PM
cp['x'] = tw_entries
cp['nl'] = 'One entry is a porcelain or pottery house (or a kiln tradition) sold under its own name; its famous patterns, services and shapes are versions.'
cp['sel'] = ("Every manufacturer in Wikipedia's List of porcelain manufacturers and in the section tables of Porcelain manufacturing companies in Europe, "
             "plus the pattern makers of the earlier edition (Fiesta, Royal Albert, Corelle and others) and Kutani and Arita wares from their own articles; "
             "the patterns of the earlier China pattern list became versions of their house. Rows that name a place without a maker (such as Jingdezhen porcelain) are kept as kiln traditions. "
             "Studio ceramics belong to visual art. COVERLINE")
cp['xg'] = 'by country of the house, then year founded, then name'
cp['tt'] = [['Body', ['Porcelain', 'Bone china', 'Earthenware', 'Stoneware']],
            ['Status', ['Working house', 'Closed house', 'Kiln tradition']],
            ['Decoration', ['Printed', 'Hand-painted', 'Gilded', 'Plain glaze']]]
cp['see'] = [['F2', 'Studio ceramics and glass art']]
n_pm = len(tw_entries)
from collections import Counter as _C
_c = _C('world list' if r['s']==H.PM else 'Europe list' if r['s']==H.EU else 'own article' for r in H.T)
cp['sel'] = cp['sel'].replace('COVERLINE', f"Complete: every row of both Wikipedia lists (the two link rows excepted), with rows named in both listed once; {n_pm} entries in all, {_c['world list']} citing the world list, {_c['Europe list']} the Europe list and {_c['own article']} their own article.")

# shelf rename and dinner service text
for s in tw['s']:
    if s['n'] == 'Services & patterns':
        s['n'] = 'Services & houses'
        s['t'] = 'Matching sets, and the porcelain and pottery houses they are collected by.'
        s['ax'] = 'kinds from the matched set to the house that makes it'
        for k in s['k']:
            if k['n'] == 'Dinner service':
                k['d'] = 'Matching set of plates, bowls and cups, sold by place setting; houses and their patterns are under Tableware house.'

# generic nl/sel for retained kinds with entries
GEN_SEL = 'Carried over from the previous edition: the entries are those named on the cited pages; no whole-space reference list exists for this kind.'
def gen(k, nl):
    if k.get('x') and 'nl' not in k:
        k['nl'] = nl
        k['sel'] = GEN_SEL
nl_map = {
    'Plate': 'One entry is a named annual or commemorative plate series.',
    'Cutlery set': 'One entry is a named cutlery design sold as a matched set; sizes of set and finishes are versions.',
    'Steak knife': 'One entry is a named table knife design for steak.',
    'Chopsticks': 'One entry is a named chopstick tradition or maker.',
    'Serving bowl': 'One entry is a named serving bowl design.',
    'Serving tray': 'One entry is a named tray design.',
    'Cheese board': 'One entry is a named cheese board design.',
    'Butter dish': 'One entry is a named butter dish design.',
    'Sugar bowl and creamer': 'One entry is a named sugar bowl and creamer design.',
    'Cruet set': 'One entry is a named cruet design.',
    'Coaster': 'One entry is a named coaster design.',
}
for s in tw['s']:
    for k in s['k']:
        if k['n'] in nl_map: gen(k, nl_map[k['n']])
        k.pop('m', None) if k['n'] != 'Children\'s cutlery' else None

# children's cutlery: models become versions or are dropped
ck = find_kind(tw, "Children's cutlery")
ck.pop('m', None)
cs = find_kind(tw, 'Cutlery set')
def add_cutlery_version(name, v):
    for e in cs['x']:
        if e['n'] == name:
            e.setdefault('v', []).append(v); return
    raise KeyError(name)
add_cutlery_version('Acorn', ver("Acorn children's cutlery set", '', 'Three-piece children\'s set.', 'Georg Jensen'))
add_cutlery_version('Radford', ver("Radford Bright children's set", '', 'Three-piece children\'s set.', 'Robert Welch'))
add_cutlery_version('Pride', ver("Child's cutlery", '', "Children's set by David Mellor.", 'David Mellor'))
ck['d'] = ck['d'] if ck.get('d') else "Small knife, fork and spoon sized for a child."

# cruet m dropped; tureen m moved above
tw['note'] = 'Organised kind of piece, then house (country) → pattern (version); the traditions register carries kilns and silversmithing centres.'
tw['t'] = ("Pieces used to serve and eat a meal, bought by house and pattern: plates, cutlery and serving pieces; glasses → Glassware & bar, "
           "table linen → Soft Furnishings; studio ceramics → visual art.")
tw['msum'] = ('Many famous tableware houses now sit in two groups: Fiskars (Finland) and Portmeirion Group (United Kingdom); '
              'the counts below are those the cited pages state.')
tw['ms'] = [
    {'mkt': 'Tableware houses owned by Fiskars', 'who': 'Fiskars Corporation', 'share': '6 houses with stated years', 'yr': 2015,
     's': W + 'Fiskars', 'note': 'Iittala 2007; Royal Copenhagen 2013; Wedgwood, Waterford and Royal Doulton 2015, as the page states. Arabia is a subsidiary taken over in 2007 per its own page.'},
    {'mkt': 'Tableware houses owned by Portmeirion Group', 'who': 'Portmeirion Group', 'share': '2 houses', 'yr': 2009,
     's': W + 'Portmeirion_Pottery', 'note': 'Royal Worcester and Spode, bought on 23 April 2009 after administration the previous November'},
    {'mkt': 'German porcelain houses owned by Rosenthal', 'who': 'Rosenthal (Sambonet Paderno Industrie)', 'share': '3 houses', 'yr': 2013,
     's': W + 'Rosenthal_(company)', 'note': 'Thomas since 1908, Hutschenreuther since 2000, Arzberg since 2013; Rosenthal itself bought by Sambonet Paderno in 2009'},
]

# ---------- Glassware & bar ----------
gw = copy.deepcopy(OD['Glassware & bar'])
LS = W + 'List_of_glassware'

def shape(n, g, d, a='', y='', mk='', v=None, s=LS):
    return {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': v or [], 'g': g}

old_x = {}
for s in gw['s']:
    for k in s['k']:
        for e in k.get('x', []):
            old_x[e['n']] = e

def oldver(name):
    e = old_x[name]
    return [ver(e['n'], e.get('y', ''), e['d'], e.get('mk', ''))] + [clean_v(v) for v in e.get('v', []) if v['n'] != e['n']]

# glass house version bundles from old entries and old models
gv = {
    'Riedel': oldver('Riedel Sommeliers') + oldver('Riedel Vinum') + oldver('Riedel Ouverture') + oldver('Riedel Escargot decanter'),
    'Zalto': oldver("Zalto Denk'Art") + oldver('Zalto Carafe 67') + [ver("Denk'Art Champagne", '', '', 'Zalto'), ver("Denk'Art Beer", '', '', 'Zalto')],
    'Baccarat': oldver('Baccarat Harcourt') + oldver('Baccarat Harcourt decanter'),
    'Waterford': oldver('Waterford Lismore'),
    'Iittala': oldver('Iittala Ultima Thule') + oldver('Iittala Ultima Thule tumblers')[1:] + oldver('Iittala Ultima Thule pitcher') + [ver('Kartio', '1956', 'Cone-shaped glass set by Kaj Franck.', 'Iittala'), ver('Aalto vase', '1936', 'Designed by Alvar Aalto; also called the Savoy vase.', 'Iittala')],
    'Moser': oldver('Moser Splendid') + oldver('Moser Whisky Set'),
    'Duralex': oldver('Duralex Picardie') + oldver('Duralex Gigogne'),
    'Libbey': [ver('Gibraltar', '', 'Tumbler line.', 'Libbey')],
    'Zwiesel Kristallglas': [ver('Tritan', '2002', 'Glass developed to be break-resistant.', 'Schott Zwiesel'), ver('Tritan Protect', '2012', '', 'Schott Zwiesel')],
    'Gabriel-Glas': oldver('Gabriel-Glas StandArt'),
}
# dedupe versions by name
for h, vs in gv.items():
    seen = set(); out = []
    for v in vs:
        if v['n'] in seen: continue
        seen.add(v['n']); out.append(v)
    gv[h] = out

G = list(H.G)
G.append(dict(c='Austria', n='Gabriel-Glas', y='', note='Austrian maker of the single StandArt universal wine glass.', s='https://www.mygabrielglas.com/products/standart', a='', own='', tier='', oy=''))
glass_entries = []
for r in G:
    e = {'n': r['n'], 'a': r['a'], 'd': r['note'], 'mk': '', 'y': r['y'], 's': r['s'], 'v': gv.get(r['n'], []), 'g': r['c'], 'cty': r['c']}
    if r['own']:
        e['own'] = r['own']; e['tier'] = r['tier']
        if r['oy']: e['own_y'] = r['oy']
    glass_entries.append(e)
names = [e['n'] for e in glass_entries]
assert len(names) == len(set(names)), [n for n in names if names.count(n) > 1]
for h in gv:
    assert h in names, h
glass_entries.sort(key=lambda e: (e['g'], yr(e['y']), e['n'].lower()))

# named shapes
wine_shapes = [
    old_x['INAO tasting glass'],
    shape('Chalice or goblet', 'Stemware', 'Ornate stemmed glass, often ceremonial.'),
    shape('Rummer', 'Stemware', 'Stemmed glass with a deep bowl.'),
    shape('Sherry glass', 'Stemware', 'Small stemmed glass for sherry.', a='copita'),
]
wine_shapes[0] = dict(wine_shapes[0]); wine_shapes[0]['g'] = 'Standards'
wine_shapes[0]['v'] = [clean_v(v) for v in wine_shapes[0]['v']]
champ = [shape('Champagne flute', 'Stemware', 'Stemmed glass with a tall, narrow bowl.', a='flute'),
         shape('Champagne coupe', 'Stemware', 'Stemmed glass with a wide, shallow bowl.', a='coupe · champagne saucer')]
cockt = [shape('Nick & Nora', 'Stemware', 'Small stemmed cocktail glass.', a='Nick and Nora glass'),
         shape('Hurricane glass', 'Stemware', 'Tall, curved glass for tropical drinks.', a='hurricane'),
         shape('Margarita glass', 'Stemware', 'Variant of the champagne coupe.'),
         shape('Fountain glass', 'Stemware', 'Tall fluted glass for milkshakes and ice cream sodas.'),
         shape('Sherbet', 'Stemware', 'Stemmed glass for ice cream or sorbet.'),
         shape('Dizzy cocktail glass', 'Tumblers', 'Wide, shallow glass without a stem.')]
spirits = [dict(old_x['Glencairn whisky glass'], g='Stemware'),
           shape('Snifter', 'Stemware', 'Short-stemmed glass for brandy and liquor.', a='brandy snifter'),
           shape('Absinthe glass', 'Stemware', 'Short-stemmed glass with a marked fill line for absinthe.'),
           shape('Shot glass', 'Tumblers', 'Small glass for a measure of liquor.', a='shot')]
spirits[0]['v'] = [clean_v(v) for v in spirits[0]['v']]
B = lambda n, d, a='': shape(n, 'Beer glassware', d, a=a)
beer = [B('Pint glass', 'Glass for an imperial pint.', a='pint'),
        B('Pilsner glass', 'Tall glass for pale lager.'),
        B('Wheat beer glass', 'Glass for wheat beer.', a='weizen glass'),
        B('Beer stein', 'Large mug, often with a hinged lid.', a='stein'),
        B('Tankard', 'Large drinking cup with a handle and hinged cover.'),
        B('Berkemeyer', 'Tall German beer glass.'),
        B('Beer boot', 'Boot-shaped beer vessel.', a='Das Boot'),
        B('Yard glass', 'Very tall conical glass, often hung on a wall when empty.', a='yard of ale'),
        B('Pony glass', 'Small glass for about 140 ml of beer.'),
        B('Pot glass', 'Beer glass.'),
        B('Australian glass', 'Australian beer glass of 200 ml.'),
        B('Australian middy', 'Australian beer glass of 285 ml from New South Wales.', a='middy'),
        B('Australian pot', 'Australian beer glass of 285 ml from Queensland and Victoria.', a='pot'),
        B('Australian schooner', 'Australian beer glass of 425 ml, 285 ml in South Australia.', a='schooner'),
        B('New Zealand handle', 'New Zealand beer glass of 425 ml.', a='handle'),
        B('New Zealand jug', 'Vessel of 750 to 1000 ml served in New Zealand pubs.')]
beer[0]['v'] = [ver('Nonic pint', '', 'Conical British pint glass with a bulge near the rim for grip and stacking.', '')]
beer[0]['v'][0]['d'] = old_x['Nonic pint']['d']
beer[0]['s'] = LS
beer += [dict(old_x['Willibecher'], g='Other beer glasses', v=[clean_v(v) for v in old_x['Willibecher']['v']]),
         dict(old_x['Teku'], g='Other beer glasses')]
T_ = lambda n, d, a='': shape(n, 'Tumblers', d, a=a)
tumblers = [T_('Collins glass', 'Tall glass for mixed drinks.'),
            T_('Highball glass', 'Tall glass for mixed drinks.', a='highball'),
            T_('Old fashioned glass', 'Short glass for spirits served neat or on ice.', a='rocks glass · lowball'),
            T_('Whiskey tumbler', 'Small, thin-walled glass for a straight shot.'),
            T_('Iced tea glass', 'Tall glass for iced tea.'),
            T_('Juice glass', 'Glass for fruit and vegetable juice.'),
            T_('Water glass', 'Glass for water.'),
            T_('Faceted glass', 'Tumbler with cut facets, such as the Soviet granyonyi stakan.', a='granyonyi stakan')]
vessels = [shape('Tazza', 'Drinkware', 'Shallow, wide-bowled cup on a foot.'),
           shape('Quaich', 'Drinkware', 'Shallow two-handled Scottish drinking bowl.'),
           shape('Sake cup', 'Drinkware', 'Small cup for sake.', a='ochoko'),
           shape('Trembleuse', 'Drinkware', 'Cup with a saucer ring that holds it steady.'),
           shape('Mazagran', 'Drinkware', 'Footed drinking cup for a coffee-based drink.'),
           shape('Pythagorean cup', 'Drinkware', 'Cup said to drain if overfilled.', a='greedy cup'),
           shape('Tiki mug', 'Drinkware', 'Ceramic mug for tropical drinks.'),
           shape('Dwarf ale glass', 'Drinkware', 'Short glass for ale.'),
           shape('Heavy baluster glass', 'Drinkware', 'Thick-based glass with a balustrade-style stem.'),
           shape('Vitrolero', 'Drinkware', 'Spanish glass drinking vessel.')]

def setx(kind, xs, nl, sel, xg):
    kind['x'] = xs; kind['nl'] = nl; kind['sel'] = sel; kind['xg'] = xg

SHAPE_SEL = ("Named shapes from the matching group of Wikipedia's List of glassware (fetched in full: 19 drinkware, 10 tumbler, 17 beer, 15 stemware and 9 other rows); "
             "rows for bottles, jars, cups, mugs and bongs, and vases and art glass, are not drinking-glass shapes and are left out, "
             "art glass and Peking glass belong to visual art. ")
XG_SHAPE = 'by group in the List of glassware, then name'
dr = gw['s'][0]
wk = find_kind(gw, 'Wine glass')
setx(wk, wine_shapes, 'One entry is a named shape or standard of glass for wine and fortified wine; makers\' series are under Glassware house.',
     SHAPE_SEL + 'The INAO tasting glass is kept as the standardised tasting shape. Complete: 3 of the 15 stemware rows serve wine (chalice, rummer, sherry); the rest sit under the sparkling, cocktail and spirits kinds, and the wine glass row is this kind itself.', 'standards, then stemware')
wk.pop('m', None)
ck_ = find_kind(gw, 'Champagne glass'); ck_.pop('m', None)
setx(ck_, champ, 'One entry is a named shape of glass for sparkling wine.', SHAPE_SEL + 'Complete: the 2 sparkling-wine rows of the 15 stemware rows.', XG_SHAPE)
bk = find_kind(gw, 'Beer glass'); bk.pop('m', None)
setx(bk, beer, 'One entry is a named beer glass shape; regional measures such as the Australian schooner are separate entries.',
     SHAPE_SEL + 'Complete: all 16 beer rows that name a glass or vessel of the 17 (Beer bottle is left out), plus Willibecher and Teku from the earlier edition.', 'by the beer glassware group, then name')
sk = find_kind(gw, 'Spirits glass')
setx(sk, spirits, 'One entry is a named shape of glass for spirits.',
     SHAPE_SEL + 'Complete: the 4 spirits rows (Glencairn, snifter, absinthe, shot); the whiskey tumbler is under Tumbler.', XG_SHAPE)
cg = find_kind(gw, 'Cocktail glass')
setx(cg, cockt, 'One entry is a named shape of glass for mixed drinks.',
     SHAPE_SEL + 'Complete: the 6 rows Nick & Nora, hurricane, margarita, fountain, sherbet and dizzy cocktail glass; the cocktail glass row is this kind itself and the coupe is under Champagne glass.', XG_SHAPE)
tk = find_kind(gw, 'Tumbler'); tk.pop('m', None)
setx(tk, tumblers, 'One entry is a named tumbler shape.',
     SHAPE_SEL + 'Complete: 8 of the 10 tumbler rows (the dizzy cocktail glass and shot glass are filed with cocktail and spirits glasses); makers\' tumbler lines are under Glassware house.', 'by name')
# new kind: historic vessels
vk = {'n': 'Historic & regional drinking vessel',
      'a': 'antique drinking cup · regional cup',
      'd': 'Drinking vessel known by a historic or regional name rather than by a drink.',
      's': LS, 'x': vessels,
      'nl': 'One entry is a named historic or regional drinking vessel.',
      'sel': SHAPE_SEL + 'Complete: the 10 drinkware rows that name a historic or regional vessel; stemware, tumblers and beer glassware have their own kinds, and the cup, mug, teacup, coffee cup, bottle and jar rows are not glassware shapes.',
      'xg': 'by name',
      'tt': [['Form', ['Footed bowl', 'Cup', 'Mug', 'Beaker']]]}
dr['k'].append(vk)

# Glassware house shelf
gh = {'n': 'Glassware house',
      'a': 'crystal house · glassworks · glass maker · Murano glassworks',
      'd': 'Glassworks or crystal house collected by name and then by its series and patterns.',
      's': H.CAT + 'France',
      'x': glass_entries,
      'nl': 'One entry is a glassworks or crystal house sold under its own name; its series, patterns and shapes are versions.',
      'xg': 'by country of the house, then year founded, then name',
      'tt': [['Glass', ['Lead crystal', 'Lead-free crystal', 'Soda-lime', 'Tempered']],
             ['Making', ['Hand-blown', 'Machine-made', 'Pressed']],
             ['Status', ['Working house', 'Closed house']]],
      'see': [['F2', 'Studio glass and glass art']]}
gh['sel'] = (f"Tableware and decorative glass makers named in Wikipedia's Category:Glassmaking_companies and its country pages for Austria, the Czech Republic, Denmark, Finland, France, Germany, Ireland, Italy, Norway, Poland, Sweden, the United Kingdom and the United States, "
             "in List of defunct glassmaking companies, and in the Murano glass article. Flat-glass, container, optical, insulation, lighting, architectural, stained-glass and technical makers (Saint-Gobain, Pilkington, Schott AG, AGC and similar) are out of scope as not tableware; Japan's category lists only technical makers. "
             f"Covers {len(glass_entries)} houses, every tableware or decorative maker on those pages; a few defunct American pressed-glass firms are included as collected tableware. Series of Riedel, Zalto, Baccarat, Waterford, Iittala and Moser are versions.")
gw['s'].insert(1, {'n': 'Glass houses', 't': 'Glassworks and crystal houses, collected by house and then by series or pattern.', 'k': [gh]})

# decanters: no entries now
dk = find_kind(gw, 'Decanter')
dk.pop('x', None)
jk = find_kind(gw, 'Jug and carafe'); jk.pop('x', None)

# bar tools: commodity plus icon rule
HAUCK = W + 'Cocktail_shaker'
shk = find_kind(gw, 'Cocktail shaker')
shk['m'] = []; shk.pop('m')
shk['x'] = [
    {'n': 'Hauck three-piece cocktail shaker', 'a': 'cobbler shaker', 'd': 'First three-piece cocktail shaker with a built-in strainer, patented by E. J. Hauck in 1884 (US 300867).',
     'mk': 'E. J. Hauck', 'y': '1884', 's': HAUCK, 'v': [], 'role': 'origin'},
    {'n': 'Alessi 870 cocktail shaker', 'a': 'Alessi 870', 'd': 'Stainless steel shaker designed by Luigi Massoni and Carlo Mazzeri for Alessi in 1957; held by MoMA.',
     'mk': 'Alessi', 'y': '1957', 's': 'https://www.moma.org/collection/works/4678', 'v': [], 'role': 'landmark',
     'own': 'Alessi', 'tier': 'Independent', 'cty': 'Italy'},
]
shk['nl'] = 'One entry is the first product of its kind or a design held by a named design collection.'
shk['sel'] = ('Icon rule for commodity bar tools: the origin entry per Wikipedia\'s Cocktail shaker article, and designs held by MoMA (MoMA lists the 1957 Alessi shaker, not on view). '
              'Bar-trade brands such as Koriko, Birdy and Yarai are not entries because popularity is not a reason. Complete: 2 of 2 under this rule.')
shk['xg'] = 'by year'
cs2 = find_kind(gw, 'Corkscrew')
cs2.pop('m', None)
cs2['x'] = [
    {'n': 'Henshall corkscrew', 'a': '', 'd': 'First corkscrew patent, granted to the Reverend Samuel Henshall in England in 1795.', 'mk': 'Samuel Henshall', 'y': '1795',
     's': W + 'Corkscrew', 'v': [], 'role': 'origin'},
    {'n': 'Screwpull', 'a': '', 'd': "Corkscrew introduced by Herbert Allen in 1979; the Corkscrew article says it is in MoMA's permanent collection.", 'mk': 'Screwpull', 'y': '1979',
     's': W + 'Corkscrew', 'v': [], 'role': 'landmark'},
]
cs2['nl'] = 'One entry is the first product of its kind or a design held by a named design collection.'
cs2['sel'] = ('Icon rule for commodity bar tools: the first corkscrew patent and the one corkscrew the cited article says MoMA holds. '
              'Waiter\'s friends, lever corkscrews and electric openers are not entries. Complete: 2 of 2 under this rule.')
cs2['xg'] = 'by year'
for s in gw['s']:
    for k in s['k']:
        if k['n'] in ('Bar set', 'Jigger', 'Bar spoon', 'Mixing glass', 'Cocktail strainer', 'Wine preserver', 'Ice bucket', 'Ice mould', 'Muddler'):
            k.pop('x', None); k.pop('m', None)
        elif k['n'] not in ('Cocktail shaker', 'Corkscrew'):
            k.pop('m', None)

gw['note'] = 'Everyday glasses are tier; stemware and crystal are variety by house → series; bar tools are commodities with one origin or design-collection icon where a page confirms it.'
gw['t'] = ('Glasses to drink from, vessels to pour from, and bar tools to mix, open and chill drinks; kitchen mugs → Tableware; '
           'studio glass and art glass → visual art.')
gw['msum'] = ('Crystal houses are held by a few owners and families; the counts below are those the cited pages state.')
gw['ms'] = [
    {'mkt': 'Glass houses owned by Fiskars', 'who': 'Fiskars Corporation', 'share': '2 houses', 'yr': 2015, 's': W + 'Fiskars',
     'note': 'Iittala bought 2007; Waterford bought 2015 with Wedgwood'},
    {'mkt': 'Swedish glassworks', 'who': 'New Wave Group (Orrefors Kosta Boda)', 'share': '2 houses', 'yr': 2005, 's': W + 'Kosta_Boda',
     'note': 'Orrefors bought Kosta Boda in 1990; Kosta Boda has been part of Orrefors Kosta Boda, a New Wave Group subsidiary, since 2005'},
]
for s in gw['s']:
    for k in s['k']:
        if k.get('x'):
            for e in k['x']:
                if 'cty' not in e and e.get('own'): pass

# ---------- brands ----------
oldb = {b['n'] for b in json.load(open(ROOT + 'rebuild/out/B5_brands.json'))['b']}
try:
    other = json.load(open(ROOT + 'rebuild/reader/_brands.json'))
    other_names = set()
    items = other['b'] if isinstance(other, dict) and 'b' in other else other
    for b in (items if isinstance(items, list) else items.values()):
        if isinstance(b, dict) and 'n' in b: other_names.add(b['n'])
except Exception as ex:
    other_names = set(); LOG.append(f'brands index not read: {ex}')
known = oldb | other_names
owners = {}
for d in (tw, gw):
    for s in d['s']:
        for k in s['k']:
            for e in k.get('x', []):
                if e.get('own'):
                    owners.setdefault(e['own'], e.get('cty', ''))
new_brands = []
for o, c in sorted(owners.items()):
    if o in known: continue
    new_brands.append({'n': o, 'c': c, 'f': '', 'seg': 'Heritage manufactory', 'd': 'Owner named on a cited page for a tableware or glassware house.', 'lines': [], 'eras': [], 'sig': [], 'sc': [], 'rel': [], 's': W + 'Fiskars', 'kf': 'tableware'})
# fix specific sources for register entries
reg_src = {'Fiskars Corporation': W + 'Fiskars', 'Portmeirion Group': W + 'Portmeirion_Pottery', 'Sambonet Paderno Industrie': W + 'Rosenthal_(company)'}
for b in new_brands:
    b['s'] = reg_src.get(b['n'], b['s'])
    # owner entries give their source from the first entry that names them
src_of = {}
for d in (tw, gw):
    for s in d['s']:
        for k in s['k']:
            for e in k.get('x', []):
                if e.get('own'): src_of.setdefault(e['own'], e['s'])
for b in new_brands:
    b['s'] = src_of.get(b['n'], b['s'])
    if b['n'] in ('Fiskars Corporation',): b['c'] = 'Finland'

part = {'replaces': ['Tableware', 'Glassware & bar'], 'depts': [tw, gw], 'brands': new_brands, 'brand_updates': {},
        'renames': {'China pattern': 'Tableware house'}, 'moves': []}
out = ROOT + 'rebuild/out/B5_parts/TABLE.json'
tmp = out + '.tmp'
json.dump(part, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, out)
print('tableware houses', len(tw_entries), 'glass houses', len(glass_entries), 'new brands', len(new_brands), LOG)
print('size', os.path.getsize(out))
