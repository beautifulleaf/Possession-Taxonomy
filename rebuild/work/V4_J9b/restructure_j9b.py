import json, re, os, collections
R = '/home/user/Possession-Taxonomy/rebuild/'
W = R + 'work/V4_J9b/'
d = json.load(open(W + 'bak/J9.json'))
brands = json.load(open(W + 'bak/J9_brands.json'))
oldren = json.load(open(W + 'bak/J9_renames.json'))
WU = 'https://en.wikipedia.org/wiki/'

REG = {}
def reg(r, cs):
    for c in cs.split(';'): REG[c.strip()] = r
reg('Africa', 'Algeria;Egypt;Libya;Morocco;Tunisia;South Africa;DR Congo;Ethiopia')
reg('East Asia', 'China;Hong Kong;Japan;South Korea;Taiwan')
reg('South & Southeast Asia', 'Afghanistan;Bangladesh;India;Pakistan;Sri Lanka;Indonesia;Malaysia;Myanmar;Philippines;Singapore;Thailand;Vietnam')
reg('Middle East', 'Iran;Israel;Jordan;Kuwait;Lebanon;Oman;Saudi Arabia;United Arab Emirates;Turkey;Middle East')
reg('Europe', 'Albania;Armenia;Austria;Azerbaijan;Belgium;Bosnia and Herzegovina;Bulgaria;Croatia;Czech Republic;Denmark;Estonia;Finland;France;Georgia;Germany;Gibraltar;Greece;Hungary;Iceland;Ireland;Italy;Kosovo;Lithuania;Malta;Netherlands;Norway;Poland;Portugal;Romania;Russia;Serbia;Slovakia;Slovenia;Spain;Sweden;Switzerland;Ukraine;United Kingdom')
reg('Latin America & Caribbean', 'Argentina;Bahamas;Bermuda;Brazil;Chile;Colombia;Costa Rica;Cuba;Dominican Republic;Ecuador;El Salvador;Guatemala;Haiti;Honduras;Jamaica;Mexico;Panama;Paraguay;Peru;Puerto Rico;Suriname;Trinidad and Tobago;Uruguay')
reg('North America', 'Canada;United States')
reg('Oceania', 'Australia;Fiji;New Zealand;Papua New Guinea')
REGIONS = ['Africa', 'East Asia', 'South & Southeast Asia', 'Middle East', 'Europe', 'Latin America & Caribbean', 'North America', 'Oceania']

# old kind -> department (new) ; department short names
DEPT_SHORT = {'Sodas': 'soda', 'Water': 'water', 'Energy & sports drinks': 'energy and sports drink', 'Tonic & mixers': 'mixer',
              'Juices & smoothies': 'juice', 'Syrups & cordials': 'syrup and cordial', 'Fermented soft drinks': 'fermented drink',
              'Ready-to-drink coffee & tea': 'coffee and tea'}
GLOBAL = ['The Coca-Cola Company', 'PepsiCo', 'Keurig Dr Pepper', 'Nestlé', 'Danone', 'Suntory']
def is_global(o):
    return o in GLOBAL or o.startswith('Coca-Cola') or o.startswith('Frucor-Suntory')
def gowner(o):
    if o.startswith('Coca-Cola'): return 'The Coca-Cola Company'
    if o.startswith('Frucor-Suntory'): return 'Suntory'
    return o

# lookups from fetched pages: name -> dict(own, own_y, role, versions(list of (n,d)), s)
LK = {
 'Jarritos': dict(own='Novamex', s=WU + 'Jarritos', v=[(f, 'flavour') for f in ['Fruit Punch', 'Grapefruit', 'Guava', 'Jamaica (hibiscus tea)', 'Lemon Lime', 'Lime', 'Mandarin', 'Mango', 'Apple', 'Mexican Cola', 'Passion Fruit', 'Pineapple', 'Strawberry', 'Tamarind', 'Watermelon', 'Mandarin Zero']], y='1950'),
 'Guaraná Antarctica': dict(own='Ambev', s=WU + 'Guaran%C3%A1_Antarctica', v=[(f, 'variant') for f in ['Zero', 'Ice', 'Champagne', 'Seleção', 'Diet', 'Light', 'Açaí']], y='1921', note='page lists Ambev as manufacturer, not explicitly owner'),
 'Vimto': dict(own='Nichols plc', s=WU + 'Vimto', v=[('Fizzy Vimto', 'carbonated'), ('Vimto Cordial', 'dilutable'), ('Still Vimto', 'premixed'), ('Vimto Energy', 'sugar and sugar-free'), ('Cherry Vimto', ''), ('Strawberry Vimto', ''), ('Vimto Remix', 'flavour mixes 2016 to 2019')], y='1908'),
 'Cheerwine': dict(own='Carolina Beverage Corporation', s=WU + 'Cheerwine', v=[('Cheerwine Zero Sugar', ''), ('Diet Cheerwine', 'caffeine free'), ('Retro Cheerwine', 'glass bottles, cane sugar'), ('Holiday Cheerwine Punch', ''), ('Cheerwine Kreme', 'Krispy Kreme flavour')], y='1917'),
 'Faygo': dict(own='National Beverage', s=WU + 'Faygo', v=[(f, 'flavour') for f in ['Cola', 'Creme Soda', 'Fruit Punch', 'Black Cherry', 'Root Beer', 'Rock & Rye', 'Redpop', 'Ginger Ale', 'Grape', 'Orange', 'Peach', 'Pineapple', 'Cotton Candy', 'Moon Mist', 'Zero Sugar range']], y='1907'),
 'Almdudler': dict(own='Klein family', s=WU + 'Almdudler', role='landmark', v=[('Original', ''), ('Light', 'sugar-free'), ('Still', 'uncarbonated'), ("G'spritzt", 'mixed with mineral water')], y='1957', note='page calls it the national drink of Austria'),
 'Kinnie': dict(own='Simonds Farsons Cisk', s=WU + 'Kinnie', role='landmark', v=[('Diet Kinnie', ''), ('Kinnie Zest', ''), ('Kinnie Vita', 'sugar and stevia')], y='1952', note="page calls it Malta's favourite non-alcoholic beverage"),
 'Kofola': dict(own='Kofola ČeskoSlovensko', s=WU + 'Kofola', role='landmark', v=[(f, 'flavour') for f in ['Original', 'Apricot', 'Watermelon', 'Raspberry', 'Blackberry', 'Gooseberry', 'Guarana', 'Zero sugar', 'Sour cherry', 'Citrus', 'Vanilla', 'Pineapple', 'Blackcurrant', 'Grapefruit']], y='1960', note='page calls it the principal rival of Coca-Cola and Pepsi in the Czech Republic and Slovakia'),
 'Fanta': dict(own='The Coca-Cola Company', s=WU + 'Fanta', v=[(a, b) for a, b in [('Orange', 'standard flavour, 1955'), ('Citrus', 'Russia, as Shokata'), ('Lemon', 'South Africa, Philippines'), ('Grape', 'South Africa, Brazil'), ('Pineapple & Grapefruit', 'UK'), ('Exotic', 'South Africa, Scandinavia'), ('Strawberry', 'Algeria'), ('Fruit Twist', 'UK'), ('Zero Sugar', '')]], y='1940'),
 'Sprite': dict(own='The Coca-Cola Company', s=WU + 'Sprite_(drink)', v=[(a, b) for a, b in [('Sprite Zero Sugar', '1974'), ('Sprite Ice', '2002'), ('Sprite Cranberry', '2013'), ('Sprite Cherry', '2017'), ('Sprite Ginger', '2020'), ('Sprite Lemon+', '2022'), ('Sprite Chill Cherry Lime', '2024')]], y='1959'),
 'Orangina': dict(own='Suntory', own_y='2009', s=WU + 'Orangina', v=[('Orangina Sanguine', 'blood orange'), ('Miss O', 'sugar-free'), ('Orangina Rouge', 'Tunisia'), ('Orangina Light', 'Tunisia')], y='1935'),
 'Club-Mate': dict(own='Brauerei Loscher', s=WU + 'Club-Mate', v=[('Club-Mate Cola', '2009'), ('Club-Mate Granat', '2013, pomegranate'), ('Club-Mate Winter Edition', 'seasonal'), ('Club-Mate Zero', '2022')], y='1924'),
 'Rivella': dict(own='Rivella SA', s=WU + 'Rivella', role='landmark', v=[('Red', ''), ('Blue', ''), ('Green Tea', ''), ('Refresh', '2018'), ('Grapefruit', '2021'), ('Swiss Mint', '2021')], y='1952', note="page calls it Switzerland's national beverage"),
 'Postobón': dict(own='Grupo Mariposa', s=WU + 'Postob%C3%B3n', v=[], y='1904'),
}
OWNER_FIX = {'Manzana Postobón': ('Postobón', 'Grupo Mariposa'), 'Colombiana': ('Postobón', 'Grupo Mariposa')}
LKALT = {'Kofola': ['Kofola'], 'Guaraná Antarctica': ['Guaraná Antarctica']}

# merges: dept-level brand merge: target name -> (list of source names, version labels)
MERGE = {
 'Fanta': ['Fanta Orange'],
 'Schweppes': ['Schweppes Tonic Water', 'Schweppes Bitter Lemon', 'Schweppes Ginger Ale', 'Schweppes Soda Water', 'Schweppes Lemonade'],
 'Fever-Tree': ['Fever-Tree Indian Tonic Water', 'Fever-Tree Ginger Beer', 'Fever-Tree Ginger Ale'],
 'Q Mixers': ['Q Tonic', 'Q Club'],
 'Canada Dry': ['Canada Dry Pale Dry Ginger Ale'],
 'Fentimans': ['Curiosity Cola', 'Victorian Lemonade', 'Fentimans Traditional Ginger Beer'],
 'Lucozade': ['Lucozade Sport'],
 'Orange Crush': ['Crush'],
 'Lipton Ice Tea': ['Lipton Brisk'],
 'Georgia': ['Georgia Cafe au Lait'],
 'Robinsons': ['Robinsons barley water and squash'],
 'Sprite': [],
 'Minute Maid': ['Hi-C'],
}
MERGE_RENAME = {'Canada Dry': 'Canada Dry', 'Schweppes': 'Schweppes', 'Fever-Tree': 'Fever-Tree', 'Fentimans': 'Fentimans', 'Robinsons': 'Robinsons'}
CANON_ENTRY_NAME = {'Fanta Orange': 'Fanta'}
CRAFT = {'Jones Soda', "Dr. Brown's", "Capt'n Eli's", 'Sprecher', 'Boylan Bottling Company', 'Squamscot', 'Grown-Up Soda', 'Maine Root', "Henry Weinhard's",
         "Dang! That's Good", 'Kutztown Soda Works', "Virgil's", 'Olipop', 'Ale-8-One', 'Fritz-kola', 'Brooklyn Soda Works', 'Fordham & Dominion',
         'Ozark Mountain', "Bickford's", 'Green River', 'Fentimans'}
OWNLABEL = {'Kirkland Signature', 'Classic Cola', 'Pirkka-cola', 'Rainbow-cola', 'Happy Cola', 'zX Cola', 'LamaTee', 'Kult Ice Tea', 'Big 8', 'Slades'}
# landmark per fetched pages
LANDMARK = {'Coca-Cola': 'best-selling soft drink in most countries (Coca-Cola Company page)', 'Irn-Bru': 'most popular soft drink in Scotland (Irn-Bru page)',
            'Inca Kola': 'about 26 % of Peru (Wharton)', 'Thums Up': '85 % of India in 1993 (Thums Up page)'}
NATCHAMP_KEEP_NATIONAL = {'Thums Up', 'Inca Kola', 'Irn-Bru', 'Almdudler', 'Kinnie', 'Kofola', 'Rivella'}  # sit in National & regional brands even if owned by a group

# ---- gather every old entry with its old dept/kind
depts_out = []
allx = []  # (dept, oldkind, entry)
oldkinds = collections.OrderedDict()
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            oldkinds[k['n']] = dp['n']
            for x in k.get('x', []):
                allx.append((dp['n'], k['n'], x))

byd = collections.defaultdict(dict)  # dept -> name -> (entry, oldkind)
dups = []
for dn, ok, x in allx:
    n = CANON_ENTRY_NAME.get(x['n'], x['n'])
    if n in byd[dn]:
        dups.append((dn, n)); continue
    x['_ok'] = ok
    byd[dn][n] = x
# apply merges
for dn in byd:
    for tgt, srcs in MERGE.items():
        present = [s for s in srcs if s in byd[dn]]
        base = byd[dn].get(tgt)
        if not present and base is None: continue
        if base is None:
            first = byd[dn][present[0]]
            base = json.loads(json.dumps(first)); base['n'] = tgt; base['mk'] = tgt
            base['a'] = ''; base['d'] = first['d']
            byd[dn][tgt] = base
        for sname in present:
            sx = byd[dn].pop(sname) if sname != tgt else None
            if sx is None: continue
            base.setdefault('v', [])
            base['v'].append({'n': sname, 'mk': tgt, 'y': sx.get('y', ''), 'd': (sx.get('dt') or sx['d'])[:120] if sname.startswith('Schweppes') or True else ''})
            for v in sx.get('v', []) or []:
                base['v'].append(v)
            if not base.get('own') and sx.get('own'): base['own'] = sx['own']
        base['d'] = base['d']

# lookups
used_lk = []
for dn in byd:
    for n, x in byd[dn].items():
        key = n if n in LK else None
        if key is None and n in ('Guaraná Antarctica', ):
            key = n
        if key:
            L = LK[key]
            if L.get('own'): x['own'] = L['own']
            if L.get('own_y'): x['own_y'] = L['own_y']
            if L.get('role'): x['role'] = L['role']
            have = {v['n'].lower() for v in x.get('v', [])}
            for a, b in L['v']:
                if a.lower() in have: continue
                x.setdefault('v', []).append({'n': a, 'mk': n, 'y': '', 'd': b})
            x['s'] = L['s']
            if L.get('y') and not x.get('y'): x['y'] = L['y']
            used_lk.append(n)
        if n in OWNER_FIX:
            x['own'] = OWNER_FIX[n][1]
        if n in LANDMARK: x['role'] = 'landmark'
for k in ('Postobón',): pass

# ---- tiering
def place(x, n):
    own = x.get('own', '')
    if n in CRAFT: return 'Craft & indie'
    if n in OWNLABEL: return 'Own label'
    if n in NATCHAMP_KEEP_NATIONAL: return 'National & regional brands'
    if own and is_global(own): return 'Global groups'
    if own: return 'Independents'
    return 'National & regional brands'

TIERVAL = {'Global groups': 'Global group', 'Independents': 'Independent', 'Craft & indie': 'Craft & indie', 'Own label': 'Own label'}
def region(x):
    return REG.get(x.get('cty') or x.get('g') or '', 'Origin not stated')

def clean(x, n, shelf):
    o = {k: v for k, v in x.items() if not k.startswith('_')}
    if o.get('own') and is_global(o['own']): o['own'] = gowner(o['own'])
    o['n'] = n; o.setdefault('mk', n)
    ok = x.get('_ok')
    if ok and ok in oldkinds and ok not in ('Cola',):
        pass
    # keep the old kind as a descriptor
    dt = (o.get('dt') or '').strip()
    o['dt'] = (ok.lower() + (' · ' + dt if dt else '')) if ok else dt
    if shelf in TIERVAL: o['tier'] = TIERVAL[shelf]
    elif n in NATCHAMP_KEEP_NATIONAL or o.get('role') == 'landmark': o['tier'] = 'National champion'
    else: o.pop('tier', None)
    if n in LANDMARK or (o.get('role') == 'landmark'): o['role'] = 'landmark'
    else: o.pop('role', None)
    o['g'] = o.get('cty') or o.get('g') or 'Origin not stated'
    if not o.get('own_y'): o.pop('own_y', None)
    return o

def yk(x):
    m = re.search(r'\d{4}', x.get('y', '') or '')
    return int(m.group()) if m else 9999

SHELF_T = {
 'Global groups': ('Brands owned by the multinational groups that dominate the category.', 'kinds by owner group'),
 'National & regional brands': ('Brands that lead or are known in one country or region, with the owner given where a fetched page states it.', 'kinds by world region of the brand'),
 'Independents': ('Established brands owned by a named company that is not one of the global groups.', 'kinds by world region of the brand'),
 'Craft & indie': ('Small-batch and new-wave brands named by a fetched craft or independent overview.', 'kinds by world region of the brand'),
 'Own label': ('Retailer and supermarket brands sold under the shop\'s own name.', 'kinds by retailer or region'),
}
SEL = {
 'soda': 'Wikipedia "List of soft drinks by country", the "List of brand name soft drink products", the Coca-Cola, PepsiCo and Keurig Dr Pepper brand lists and two craft-soda overviews, all fetched 2026-10-31',
 'water': 'Wikipedia "List of bottled water brands", "List of soft drinks by country" and the Coca-Cola, PepsiCo and Keurig Dr Pepper brand lists, fetched 2026-10-31',
}
def seltext(short, tier):
    base = SEL.get(short, 'Wikipedia "List of soft drinks by country" and the Coca-Cola, PepsiCo and Keurig Dr Pepper brand lists, fetched 2026-10-31')
    return (f'Follows {base}. Every listed brand in scope is included once in this department, in the shelf of its stated owner; '
            'flavours and variants are versions. Where no page states the owner it is left blank. Discontinued brands and generic drink names are left out.')

def cap(s): return s[0].upper() + s[1:]
deptdata = {dp['n']: dp for dp in d['depts']}
new_depts = []
newkind_of_old = {}  # old kind -> Counter(new kinds)
used_names = set()
stats = collections.Counter(); regstats = collections.Counter()
AXES = {
 'Sodas': 'Who sells it: the global groups, then each region\'s national brands, then independents, craft and own label?',
 'Water': 'Who sells it: the global groups, then each region\'s national brands, then independents, craft and own label?',
 'Energy & sports drinks': 'Who sells it: the global groups, then each region\'s national brands, then independents?',
 'Tonic & mixers': 'Who sells it: the global groups, then national brands, then independents and craft?',
 'Juices & smoothies': 'Who sells it: the global groups, then national brands, then independents?',
 'Syrups & cordials': 'Who sells it: the global groups, then national brands, then independents?',
 'Fermented soft drinks': 'Who sells it: national and regional brands, then independents and craft?',
 'Ready-to-drink coffee & tea': 'Who sells it: the global groups, then each region\'s national brands, then independents?',
}
for dp in d['depts']:
    dn = dp['n']; short = DEPT_SHORT[dn]
    ents = byd[dn]
    shelves = collections.OrderedDict((t, collections.defaultdict(list)) for t in SHELF_T)
    for n, x in ents.items():
        t = place(x, n)
        if t == 'Global groups': key = gowner(x['own'])
        elif t in ('National & regional brands', 'Independents', 'Craft & indie', 'Own label'): key = region(x)
        shelves[t][key].append(clean(x, n, t))
        newkind_of_old.setdefault(x['_ok'], collections.Counter())
        stats[(dn, t)] += 1
        regstats[(dn, t, key)] += 1
    outs = []
    for t, kd in shelves.items():
        if not kd: continue
        kinds = []
        # small tiers: merge regions into one kind when few entries
        total = sum(len(v) for v in kd.values())
        if t != 'Global groups' and t != 'National & regional brands' and total < 30:
            kd = {'All regions': [e for v in kd.values() for e in v]}
        for key in (GLOBAL if t == 'Global groups' else REGIONS + ['Origin not stated', 'All regions']):
            if key not in kd: continue
            es = sorted(kd[key], key=lambda e: (e['g'], yk(e), e['n'].lower()))
            if t == 'Global groups': nm = f'{key} {short} brands'
            elif key == 'All regions': nm = {'Independents': f'Independent {short} brands', 'Craft & indie': f'Craft and indie {short} brands', 'Own label': f'Own-label {short} brands', 'National & regional brands': f'National {short} brands'}[t]
            else:
                pre = {'National & regional brands': 'National', 'Independents': 'Independent', 'Craft & indie': 'Craft and indie', 'Own label': 'Own-label'}[t]
                nm = f'{pre} {short} brands: {key}'
            assert nm not in used_names, nm
            used_names.add(nm)
            who = {'Global groups': f'brands of {key}', 'National & regional brands': f'brands from {key}', 'Independents': f'independent brands ({key})', 'Craft & indie': 'craft and indie brands', 'Own label': 'own-label brands'}[t]
            dsent = f'{cap(short)} {who}, sectioned by country.' if t != 'Global groups' else f'The {short} brands of {key}, sectioned by country of origin.'
            k = dict(n=nm, d=dsent, nl=f'One entry is a {short} brand sold under its own name; its flavours, diet and zero-sugar versions and sizes are versions.' if short not in ('water',) else 'One entry is a bottled-water brand sold under its own name; sizes, materials and flavours are versions.',
                     sel=seltext(short, t), xg='country of the brand', x=es)
            kinds.append(k)
        if kinds:
            sh = dict(n=t, t=SHELF_T[t][0], k=kinds)
            if len(kinds) > 3: sh['ax'] = SHELF_T[t][1]
            outs.append(sh)
    nd = {k: v for k, v in dp.items() if k != 's'}
    nd['ax'] = AXES[dn]
    nd['s'] = outs
    new_depts.append(nd)



# dept t rewrite
TXT = {
 'Sodas': 'Bought soft drinks sold by brand: the global groups, each region\'s national brands, independents, craft and own label; a plain water → Water, and a spirit mixer → Tonic & mixers. Flavours are versions of the brand.',
 'Water': 'Bottled drinking water sold by brand, plain or with gas, minerals or flavour added; a drink with sugar or juice → Sodas or Juices & smoothies, and tap-water treatment → B5. The legal type is shown on each entry.',
 'Energy & sports drinks': 'Drinks sold to lift energy, replace fluid or add nutrients, listed by brand and owner; a plain flavoured soda → Sodas.',
 'Tonic & mixers': 'Fizzy drinks made to be mixed with spirits, listed by brand and owner; a soda drunk alone → Sodas, and bar syrups → Syrups & cordials.',
 'Juices & smoothies': 'Juice, nectar and juice-drink brands, plain, diluted or blended, listed by owner; a fizzy drink → Sodas, and fruit syrups → Syrups & cordials.',
 'Syrups & cordials': 'Concentrates, squashes, syrups and powders made up with water, soda or spirits, listed by brand and owner; a ready-to-drink soda → Sodas.',
 'Fermented soft drinks': 'Drinks soured or flavoured by fermentation and sold as non-alcoholic, listed by brand and owner; a brewed soda with no live ferment → Sodas.',
 'Ready-to-drink coffee & tea': 'Bottles and cans of brewed coffee, tea or mate, listed by brand and owner; dry tea and coffee → J6.',
}
for nd in new_depts:
    nd['t'] = TXT[nd['n']]
    nd['note'] = 'Market first: global groups, then national and regional brands by world region, independents, craft and own label.' if nd.get('note') is not None else nd.get('note')

# ms update
ms = {nd['n']: nd.get('ms', []) for nd in new_depts}
BD = 'https://beverage-digest.com/articles/1189-hot-topic-should-pepsico-refranchise-in-north-america'
ms['Sodas'] = [m for m in ms['Sodas']] + [
 dict(mkt='US carbonated soft drinks (retail)', who='The Coca-Cola Company', share='40 %', yr=2024, s=BD, note='first three quarters of 2024, +0.4 points; Beverage Digest as quoted on the page, labelled share of CSDs at US retail'),
 dict(mkt='US carbonated soft drinks (retail)', who='PepsiCo', share='27 %', yr=2024, s=BD, note='first three quarters of 2024, -0.7 points'),
 dict(mkt='US carbonated soft drinks (retail)', who='Keurig Dr Pepper', share='24.5 %', yr=2024, s=BD, note='first three quarters of 2024, -0.9 points'),
 dict(mkt='US carbonated soft drinks (brands)', who='Coca-Cola (brand)', share='19.1 %', yr=2024, s='https://www.tipranks.com/news/coca-cola-remains-americas-favorite-soda-as-pepsi-loses-its-pop', note='brand share; Dr Pepper 8.3 %, Sprite 8.03 %, Pepsi 7.97 %; data provider not named in the article'),
 dict(mkt='UK non-alcoholic ready-to-drink', who='Coca-Cola European Partners', share='31 % by value, 21 % by volume', yr=2019, s='https://knowledge.sharescope.co.uk/2020/11/25/finding-the-soft-drinks-companies-with-the-most-fizz/', note='company claim quoted by Sharescope; year inferred from the 2019 investor factsheet it cites'),
 dict(mkt='Switzerland soft drinks (value)', who='Rivella SA', share='15.3 %', yr=2013, s=WU + 'Rivella', note='second to Coca-Cola'),
 dict(mkt='Austria soft drinks', who='Almdudler', share='second only to Coca-Cola (no figure)', yr=2014, s=WU + 'Almdudler', note='page also says about 99 % of Austrians know the brand'),
]
for nd in new_depts:
    nd['ms'] = ms[nd['n']] if ms[nd['n']] else nd.get('ms', [])
for nd in new_depts:
    if nd['n'] == 'Sodas':
        nd['msum'] = ('Three groups hold most US soda: in the first three quarters of 2024 Beverage Digest put The Coca-Cola Company at 40 %, PepsiCo at 27 % and Keurig Dr Pepper at 24.5 % of US retail carbonated soft drinks. '
                      'Elsewhere the leader is local: Irn-Bru in Scotland, Inca Kola in Peru, Thums Up in India, Rivella in Switzerland. Craft soda was about 1 % of the US market in 2015.')

# renames: every old kind -> new kind that took most of its brands (or its department's first national kind)
ren = dict(oldren)
for dp in d['depts']:
    pass
oldmap = {}
cnt = collections.defaultdict(collections.Counter)
for nd in new_depts:
    for s in nd['s']:
        for k in s['k']:
            for e in k['x']:
                ok = (e.get('dt') or '').split(' · ')[0]
                cnt[ok][k['n']] += 1
lower2old = {k.lower(): k for k in oldkinds}
for lk, c in cnt.items():
    oldn = lower2old.get(lk)
    if oldn: oldmap[oldn] = c.most_common(1)[0][0]
for okn, dn in oldkinds.items():
    if okn not in oldmap:
        nd = [x for x in new_depts if x['n'] == dn][0]
        oldmap[okn] = nd['s'][0]['k'][0]['n'] if nd['s'] else dn
# earlier renames now point to new names
final_ren = {}
for o, k in ren.items():
    final_ren[o] = oldmap.get(k, k)
for o, k in oldmap.items():
    final_ren.setdefault(o, k)

# category key
key = d['key']
newd = dict(d)
newd['depts'] = new_depts
newd['lead'] = d['lead']
# brand register
have = {b['n'] for b in brands['b']}
OWN_C = {'Novamex': 'United States', 'Carolina Beverage Corporation': 'United States', 'Nichols plc': 'United Kingdom', 'Simonds Farsons Cisk': 'Malta',
         'Grupo Mariposa': 'Colombia', 'Kofola ČeskoSlovensko': 'Czech Republic', 'Brauerei Loscher': 'Germany', 'Rivella SA': 'Switzerland', 'Klein family': 'Austria', 'Ambev': 'Brazil'}
for nd in new_depts:
    for s in nd['s']:
        for k in s['k']:
            for e in k['x']:
                for nme, c in ((e['n'], e.get('cty', '')), (e.get('own', ''), OWN_C.get(e.get('own', ''), ''))):
                    if nme and nme not in have:
                        have.add(nme)
                        brands['b'].append(dict(n=nme, c=c, f='', seg='Mainstream', d='Drink brand or owner named by a fetched reference.', lines=[], eras=[], sig=[nme], sc=[], rel=[], s=e['s'], kf='soft drinks'))
for b in brands['b']:
    if b['n'] in OWN_C and not b['c']: b['c'] = OWN_C[b['n']]
brands['b'].sort(key=lambda b: b['n'].lower())

def wr(p, o):
    t = p + '.tmp'; json.dump(o, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
wr(R + 'out/J9.json', newd); wr(R + 'out/J9_brands.json', brands); wr(R + 'out/J9_renames.json', final_ren)
json.dump(dict(stats={f'{a}|{b}': v for (a, b), v in stats.items()}, reg={f'{a}|{b}|{c}': v for (a, b, c), v in regstats.items()}, lookups=used_lk, dups=dups),
          open(W + 'stats.json', 'w'), ensure_ascii=False, indent=1)
print('tiers', sum(stats.values()), dict(collections.Counter({b: sum(v for (a, bb), v in stats.items() if bb == b) for _, b in stats})))
print('dups', dups, 'lookups', used_lk)
