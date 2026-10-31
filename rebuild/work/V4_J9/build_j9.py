import json, re, os, sys
R = '/home/user/Possession-Taxonomy/rebuild/'
W = R + 'work/V4_J9/'
d = json.load(open(W + 'bak/J9.json'))
brands = json.load(open(W + 'bak/J9_brands.json'))

U = {
 'WSD': 'https://en.wikipedia.org/wiki/List_of_soft_drinks_by_country',
 'WBW': 'https://en.wikipedia.org/wiki/List_of_bottled_water_brands',
 'WCC': 'https://en.wikipedia.org/wiki/List_of_Coca-Cola_brands',
 'PEP': 'https://en.wikipedia.org/wiki/List_of_PepsiCo_brands',
 'KDP': 'https://en.wikipedia.org/wiki/Keurig_Dr_Pepper',
 'BNS': 'https://en.wikipedia.org/wiki/List_of_brand_name_soft_drink_products',
 'CSW': 'https://en.wikipedia.org/wiki/Craft_soda',
 'DM': 'https://www.thedailymeal.com/1275460/best-craft-soda-brands-market',
}
KM = dict(NM='Natural mineral water', SPR='Spring water', AG='Artesian & glacier water', PU='Purified & table water',
 SM='Sparkling mineral water', FS='Flavoured sparkling water', AF='Alkaline & functional water', FW='Flavoured still water',
 CO='Cola', PS='Pepper & spiced soda', CM='Cola-orange mix (Spezi)', LL='Lemon-lime soda', CI='Citrus soda', OR='Orange soda',
 SL='Sparkling lemonade', CH='Chinotto & bitter soda', RA='Ramune & marble soda', FR='Fruit soda', CY='Cherry soda', AP='Apple soda',
 MF='Mixed-fruit soda', GU='Guaraná soda', BG='Bubblegum & tutti-frutti soda', RB='Root beer & birch beer', CR='Cream soda',
 HS='Herbal & sarsaparilla soda', TW='Tonic water', BL='Bitter lemon & citrus mixer', GB='Ginger beer', GA='Ginger ale',
 SW='Soda water & club soda', CMX='Cocktail mix', JD='Juice drink', OJ='Orange juice', AJ='Apple juice', GJ='Grape juice',
 TO='Tropical & exotic juice', TV='Tomato & vegetable juice', SQ='Squash & fruit cordial', SH='Sharbat & rose syrup',
 PM='Powdered drink mix', KO='Kombucha', BGB='Brewed ginger beer', KV='Kvass', BO='Boza', MA='Malta & malt soft drink',
 LA='Lactic soft drink', EN='Energy drink', MS='Mate soda', SP='Sports drink', FU='Functional & vitamin drink',
 PF='Prebiotic & functional soda', CC='Canned coffee', BLT='Bottled latte & coffee drink', IT='Iced tea',
 GT='Bottled green & oolong tea', YM='Yerba mate & guayusa drink')

def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())

kinds = {}
kdept = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            kinds[k['n']] = k; kdept[k['n']] = dp['n']
regmap = {b['n']: b for b in brands['b']}

GLOBAL = {'The Coca-Cola Company', 'PepsiCo', 'Keurig Dr Pepper', 'Nestlé', 'Danone', 'Suntory'}
def is_global(o):
    return o in GLOBAL or o.startswith('Coca-Cola') or o.startswith('Frucor-Suntory')
NC = {'Irn-Bru': 'Scotland', 'Inca Kola': 'Peru', 'Thums Up': 'India'}
CRAFT = {'Jones Soda', 'Dr. Brown\'s', "Capt'n Eli's", 'Sprecher', 'Boylan Bottling Company', 'Squamscot', 'Grown-Up Soda',
 'Maine Root', "Henry Weinhard's", 'Dang! That\'s Good', 'Kutztown Soda Works', "Virgil's", 'Olipop', 'Ale-8-One', 'Fritz-kola',
 'Brooklyn Soda Works', 'Fordham & Dominion', 'Ozark Mountain', "Bickford's", 'Green River', 'Curiosity Cola', 'Victorian Lemonade',
 'Fentimans Traditional Ginger Beer', 'Fritz-Kola'}
OWNLABEL = {'Kirkland Signature', 'Classic Cola', 'Pirkka-cola', 'Rainbow-cola', 'Happy Cola', 'zX Cola', 'LamaTee', 'Kult Ice Tea', 'Big 8', 'Slades'}
NCOUNTRY_NOTE = {}

# existing entries: (own, cty, own_y, role)
EX = {
 'Evian': ('Danone', 'France', '', ''), 'Vittel': ('Nestlé', 'France', '', ''), 'Contrex': ('Nestlé', 'France', '', ''),
 'Volvic': ('Danone', 'France', '', ''), 'Gerolsteiner Still (Naturell)': ('Gerolsteiner Brunnen', 'Germany', '', ''),
 'Highland Spring': ('Highland Spring Group', 'United Kingdom', '', ''), 'Spa': ('Spadel', 'Belgium', '', ''),
 'Ramlösa': ('Carlsberg Group', 'Sweden', '', ''), 'Tŷ Nant': ('Tŷ Nant Spring Water Ltd.', 'United Kingdom', '', ''),
 'Tipperary Natural Mineral Water': ('Tipperary Natural Mineral Water Ltd.', 'Ireland', '', ''),
 'Poland Spring': ('BlueTriton Brands', 'United States', '', ''), 'Icelandic Glacial': ('Icelandic Water Holdings ehf.', 'Iceland', '', ''),
 'Mountain Valley Spring Water': ('Primo Brands', 'United States', '', ''), 'Malvern': ('Holywell Water Co. Ltd.', 'United Kingdom', '', ''),
 'Nongfu Spring': ('Nongfu Spring', 'China', '', ''), 'Fiji Water': ('The Wonderful Company', 'Fiji', '', ''),
 'Voss': ('VOSS of Norway AS', 'Norway', '', ''), 'Dasani': ('The Coca-Cola Company', 'United States', '', ''),
 'Aquafina': ('PepsiCo', 'United States', '', ''), 'Nestlé Pure Life': ('Nestlé', 'Switzerland', '', ''),
 'Selters': ('Selters Mineralquelle Augusta Victoria GmbH', 'Germany', '', ''), 'Apollinaris': ('The Coca-Cola Company', 'Germany', '', ''),
 'Gerolsteiner Sprudel': ('Gerolsteiner Brunnen', 'Germany', '', ''), 'Perrier': ('Nestlé', 'France', '', ''),
 'Badoit': ('Danone', 'France', '', ''), 'S.Pellegrino': ('Nestlé', 'Italy', '', ''), 'Topo Chico': ('The Coca-Cola Company', 'Mexico', '', ''),
 'Borjomi': ('IDS Borjomi International', 'Georgia', '', ''), 'Mattoni': ('Mattoni 1873', 'Czech Republic', '', ''),
 'Farris': ('Ringnes', 'Norway', '', ''), 'Sairme': ('Sairme Mineral Waters LLC', 'Georgia', '', ''),
 'Acqua Panna': ('Nestlé', 'Italy', '', ''),
 'LaCroix': ('National Beverage', 'United States', '', ''), 'Bubly': ('PepsiCo', 'United States', '', ''),
 'Polar Seltzer': ('Polar Beverages', 'United States', '', ''), 'Smartwater': ('The Coca-Cola Company', 'United States', '', ''),
 'Coca-Cola': ('The Coca-Cola Company', 'United States', '', 'landmark'), 'Pepsi': ('PepsiCo', 'United States', '', ''),
 'RC Cola': ('Keurig Dr Pepper', 'United States', '', ''), 'Thums Up': ('The Coca-Cola Company', 'India', '1993', 'landmark'),
 'Kofola': ('Kofola ČeskoSlovensko', 'Czech Republic', '', ''), 'Fritz-kola': ('', 'Germany', '', ''), 'Curiosity Cola': ('Fentimans', 'United Kingdom', '', ''),
 'Dr Pepper': ('Keurig Dr Pepper', 'United States', '', ''), 'Mr. Pibb': ('The Coca-Cola Company', 'United States', '', ''),
 'Spezi': ('Riegele', 'Germany', '', ''), 'Mezzo Mix': ('The Coca-Cola Company', 'Germany', '', ''),
 '7 Up': ('Keurig Dr Pepper', 'United States', '', ''), 'Sprite': ('The Coca-Cola Company', 'Germany', '', ''),
 'Limca': ('The Coca-Cola Company', 'India', '', ''), 'Mountain Dew': ('PepsiCo', 'United States', '', ''),
 'Orange Crush': ('Keurig Dr Pepper', 'United States', '', ''), 'Orangina': ('', 'France', '', ''),
 'Fanta Orange': ('The Coca-Cola Company', 'Germany', '', ''), 'Aranciata': ('Nestlé', 'Italy', '', ''),
 'Tango': ('Britvic', 'United Kingdom', '', ''), 'Sinalco': ('', 'Germany', '', ''), 'Mirinda': ('PepsiCo', 'Spain', '', ''),
 "R. White's Lemonade": ('Britvic', 'United Kingdom', '', ''), 'Limonata': ('Nestlé', 'Italy', '', ''),
 'Victorian Lemonade': ('Fentimans', 'United Kingdom', '', ''), 'Sanbittèr': ('Nestlé', 'Italy', '', ''),
 'Kinnie': ('', 'Malta', '', ''), 'Ramune': ('', 'Japan', '', ''), 'Faygo': ('National Beverage', 'United States', '', ''),
 'Jarritos': ('', 'Mexico', '', ''), 'Cheerwine': ('', 'United States', '', ''), 'Sidral Mundet': ('', 'Mexico', '', ''),
 'Manzana Postobón': ('Postobón', 'Colombia', '', ''), 'Vimto': ('', 'United Kingdom', '', ''),
 'Guaraná Antarctica': ('', 'Brazil', '', ''), 'Irn-Bru': ('A.G. Barr', 'United Kingdom', '', 'landmark'),
 'Inca Kola': ('The Coca-Cola Company', 'Peru', '1999', 'landmark'), 'Colombiana': ('Postobón', 'Colombia', '', ''),
 'Big Red': ('Keurig Dr Pepper', 'United States', '2018', ''), 'Hires Root Beer': ('Keurig Dr Pepper', 'United States', '', ''),
 'A&W Root Beer': ('Keurig Dr Pepper', 'United States', '', ''), 'Barq\'s Root Beer': ('The Coca-Cola Company', 'United States', '', ''),
 'Moxie': ('The Coca-Cola Company', 'United States', '', ''), 'Almdudler': ('', 'Austria', '', ''),
 'Schweppes Ginger Ale': ('Keurig Dr Pepper', 'United States', '', ''),
 'Canada Dry Pale Dry Ginger Ale': ('Keurig Dr Pepper', 'Canada', '', ''), 'Vernors': ('Keurig Dr Pepper', 'United States', '', ''),
 'Ale-8-One': ('', 'United States', '', ''), 'Old Jamaica Ginger Beer': ('', 'Jamaica', '', ''),
 'Welch\'s Concord grape juice': ('Keurig Dr Pepper', 'United States', '', ''), 'Hi-C': ('The Coca-Cola Company', 'United States', '', ''),
 'SunnyD': ('Keurig Dr Pepper', 'United States', '', ''), 'Appletiser': ('The Coca-Cola Company', 'South Africa', '', ''),
 'Robinsons barley water and squash': ('Britvic', 'United Kingdom', '', ''), 'Ribena': ('Suntory', 'United Kingdom', '', ''),
 'Rooh Afza': ('Hamdard Laboratories', 'India', '', ''), 'Gatorade': ('PepsiCo', 'United States', '', ''),
 'Powerade': ('The Coca-Cola Company', 'United States', '', ''), 'BodyArmor': ('The Coca-Cola Company', 'United States', '', ''),
 'Pocari Sweat': ('Otsuka Pharmaceutical', 'Japan', '', ''), 'Vitaminwater': ('The Coca-Cola Company', 'United States', '', ''),
 'Lucozade Sport': ('Suntory', 'United Kingdom', '', ''), 'Red Bull': ('Red Bull GmbH', 'Austria', '', ''),
 'Monster Energy': ('Monster Beverage', 'United States', '', ''), 'Rockstar': ('PepsiCo', 'United States', '', ''),
 'Poppi': ('PepsiCo', 'United States', '', ''), 'Olipop': ('', 'United States', '', ''),
 'Georgia': ('The Coca-Cola Company', 'Japan', '', ''), 'Boss': ('Suntory', 'Japan', '', ''),
 'Snapple iced tea': ('Keurig Dr Pepper', 'United States', '', ''), 'AriZona Iced Tea': ('Arizona Beverage Company', 'United States', '', ''),
 'Lipton Ice Tea': ('PepsiCo', 'United States', '', ''), 'Oi Ocha': ('Ito En', 'Japan', '', ''),
 'Milkis': ('Lotte Chilsung', 'South Korea', '', ''), 'Fentimans Traditional Ginger Beer': ('Fentimans', 'United Kingdom', '', ''),
 'Bundaberg Ginger Beer': ('Bundaberg family-owned', 'Australia', '', ''), 'Club-Mate': ('', 'Germany', '', ''),
 'Materva': ('', 'Cuba', '', ''), 'Supermalt': ('Royal Unibrew', 'Denmark', '', ''),
}
# which existing: sources of owner facts
EXSRC = {}

# moves of existing entries between kinds (flagship product per fetched list)
MOVE = {'Irn-Bru': 'Citrus soda', 'Inca Kola': 'Fruit soda', 'Colombiana': 'Fruit soda', 'Big Red': 'Fruit soda'}
moved = {}
for kn, k in kinds.items():
    keep = []
    for x in k.get('x', []):
        if x['n'] in MOVE and MOVE[x['n']] != kn:
            moved.setdefault(MOVE[x['n']], []).append(x)
        else:
            keep.append(x)
    k['x'] = keep
for kn, xs in moved.items():
    kinds[kn].setdefault('x', []).extend(xs)

existing_names = set()
for k in kinds.values():
    for x in k.get('x', []):
        existing_names.add(norm(x['n']))
        if x['n'] in EX:
            o, c, oy, role = EX[x['n']]
            x['own'] = o; x['cty'] = c
            if oy: x['own_y'] = oy
            if role: x['role'] = role
        else:
            x['own'] = ''; x['cty'] = (regmap.get(x.get('mk')) or {}).get('c', '')
        x.setdefault('own', ''); x.setdefault('cty', '')

SKIP = {'Yoo-hoo', "Welch's", 'Capri-Sun', 'Starbucks Frappuccino', 'Schweppes', 'Canada Dry', "Fentiman's", "Barq's",
 'Bundaberg Brewed Drinks', 'Robinsons', 'Lipovitan', 'Boss Coffee', 'Shirley', 'Pure Leaf', 'Agthia Al Ain', 'Sting Energy',
 'Mountain Dew Baja Blast', 'Starbucks Refreshers', 'Gatorade G2', 'Nehi Peach', 'Dr Pepper Cream Soda', 'Vernors', 'Moxie', 'Ale-8-One',
 '7 Up'}
KOVER = {'Sting': 'EN', 'Sobe': 'FU', 'Vira Blåtira': 'BG', 'Mr & Mrs T': 'CMX', 'Hawaiian Punch': 'JD', 'Poppi': 'PF',
         'Frooti': 'TO', 'Prigat': 'JD', 'Bambi': 'FR', 'Dole juice': 'TO', 'Zain': 'JD'}

def cap(s): return s[0].upper() + s[1:] if s else s
raw = []
for fn in ('data_entries.txt', 'extra_entries.txt'):
    for line in open(W + fn, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'): continue
        raw.append(line)

ents = []  # dicts
for line in raw:
    if line.startswith('+'):
        n, _, note = line[1:].partition('|')
        if ents: ents[-1]['v'].append((n.strip(), note.strip()))
        continue
    p = line.split('|')
    if len(p) < 6: print('BAD', line); continue
    kc, n, cty, own, typ, src = [x.strip() for x in p[:6]]
    ents.append(dict(kc=kc, n=n, cty=cty, own=('' if own == '-' else own), typ=typ, src=src, v=[]))

seen = set(existing_names)
newcount = {}
used_names = {}
for e in ents:
    n = e['n']
    if n in SKIP or e['src'] == 'XX': continue
    kc = KOVER.get(n, e['kc'])
    if kc not in KM: print('KIND?', kc, n); continue
    key = norm(n)
    if key in seen:
        # same brand name in a different country: qualify
        if key in used_names and used_names[key] != e['cty'] and norm(n + e['cty']) not in seen:
            n = f"{n} ({e['cty']})"; key = norm(n)
        else:
            continue
    seen.add(key); used_names.setdefault(norm(e['n']), e['cty'])
    kn = KM[kc]
    own = e['own']
    d_ = cap(e['typ']) + ' from ' + e['cty']
    if own: d_ += '; owner ' + own + ' as listed'
    d_ += '.'
    if e['src'] in ('WSD',) and not e['typ']: d_ = 'Soft drink from ' + e['cty'] + '.'
    x = dict(n=n, a='', d=d_, mk=n, y='', s=U[e['src']], v=[{'n': a, 'mk': n, 'y': '', 'd': b} for a, b in e['v']],
             dt='', own=own, cty=e['cty'], g=e['cty'])
    kinds[kn].setdefault('x', []).append(x)
    newcount[kn] = newcount.get(kn, 0) + 1

# tiers, own_y, roles, craft, sorting
OWN_Y = {'Big Red': '2018', 'CORE Hydration': '2018', 'Innocent Drinks': '2013', 'Ghost': '2024 (60 % stake)', 'Green River': '2021'}
for kn, k in kinds.items():
    for x in k.get('x', []):
        o = x.get('own', ''); n = x['n']
        if n == 'Green River': x['own'] = 'Sprecher Brewing Company'; x['own_y'] = '2021'; o = x['own']
        if n in OWN_Y and n != 'Green River': x['own_y'] = OWN_Y[n]
        if n in CRAFT: x['tier'] = 'Craft & indie'
        elif n in NC: x['tier'] = 'National champion'
        elif n in OWNLABEL: x['tier'] = 'Own label'
        elif o and is_global(o): x['tier'] = 'Global group'
        elif o: x['tier'] = 'Independent'
        else: x['tier'] = ''
        if not x.get('g'): x['g'] = x.get('cty') or 'Unplaced'
        if not x['tier']: x.pop('tier')
        for f in ('own_y', 'role'):
            if not x.get(f): x.pop(f, None)
    if k.get('x'):
        def yk(x):
            m = re.search(r'\d{4}', x.get('y', ''))
            return int(m.group()) if m else 9999
        k['x'].sort(key=lambda x: (x['g'], yk(x), x['n'].lower()))
        k['xg'] = 'country of the brand'

# nl / sel
WATERK = {'Natural mineral water', 'Spring water', 'Artesian & glacier water', 'Purified & table water', 'Sparkling mineral water',
          'Flavoured sparkling water', 'Alkaline & functional water', 'Flavoured still water'}
for kn, k in kinds.items():
    if not k.get('x'): continue
    if kn in WATERK:
        k['nl'] = 'One entry is a bottled-water brand sold under its own name; size, material and flavour variants are versions.'
        k['sel'] = ('Follows the fetched Wikipedia "List of bottled water brands" and the Coca-Cola, PepsiCo and Keurig Dr Pepper brand lists, '
                    'plus the national soft-drink list for national waters; every listed brand in scope is included, placed by the legal type of its flagship water. '
                    'Where the list is silent on the spring the entry does not name one. Discontinued and historical brands are left out.')
    elif kn in ('Energy drink', 'Energy shot', 'Mate soda', 'Sports drink', 'Functional & vitamin drink', 'Prebiotic & functional soda'):
        k['nl'] = 'One entry is an energy, sports or functional drink brand sold under its own name; zero-sugar, flavour and size variants are versions.'
        k['sel'] = ('Follows the fetched national lists in Wikipedia "List of soft drinks by country" and the Coca-Cola, PepsiCo and Keurig Dr Pepper brand lists; '
                    'each brand sits under the kind of its flagship product. Discontinued brands are left out.')
    elif kn in ('Canned coffee', 'Bottled latte & coffee drink', 'Iced tea', 'Bottled green & oolong tea', 'Milk tea & bubble tea', 'Yerba mate & guayusa drink'):
        k['nl'] = 'One entry is a ready-to-drink coffee or tea brand sold under its own name; sweetness, flavour and size variants are versions.'
        k['sel'] = ('Follows the fetched national lists in Wikipedia "List of soft drinks by country" and the Coca-Cola, PepsiCo and Keurig Dr Pepper brand lists. '
                    'No whole-space reference for ready-to-drink tea and coffee was found, so the list is as complete as those lists are.')
    elif kn in ('Juice drink', 'Orange juice', 'Apple juice', 'Grape juice', 'Tropical & exotic juice', 'Tomato & vegetable juice', 'Cranberry & berry juice',
                'Juice spritzer (Schorle)', 'Squash & fruit cordial', 'Elderflower & botanical cordial', 'Lime cordial', 'Sharbat & rose syrup',
                'Powdered drink mix', 'Water enhancer', 'Cocktail mix', 'Drinking vinegar & shrub'):
        k['nl'] = 'One entry is a juice, squash, syrup or mixer brand sold under its own name; flavours and sizes are versions.'
        k['sel'] = ('Follows the fetched national lists in Wikipedia "List of soft drinks by country" and the Coca-Cola, PepsiCo and Keurig Dr Pepper brand lists; '
                    'no whole-space reference for juices and syrups exists, so those lists are the canon. Generic drink names and discontinued brands are left out.')
    else:
        k['nl'] = 'One entry is a soft-drink brand sold under its own name; diet, zero-sugar, flavour and size variants are versions.'
        k['sel'] = ('Follows the fetched Wikipedia "List of soft drinks by country", the Coca-Cola, PepsiCo and Keurig Dr Pepper brand lists, '
                    'the "List of brand name soft drink products" and two craft-soda overviews. Every listed brand in scope is included under the kind of its flagship product; '
                    'discontinued brands, generic drink names and flavour lines of one brand are left out or kept as versions.')

# market facts
DEP = {dp['n']: dp for dp in d['depts']}
PEPSI = 'https://en.wikipedia.org/wiki/Pepsi'
ms_soda = [
 dict(mkt='US carbonated soft drinks', who='The Coca-Cola Company', share='42.7 %', yr=2008, s=PEPSI, note='all brands of the company; Beverage Digest figure quoted on the Pepsi page'),
 dict(mkt='US carbonated soft drinks', who='PepsiCo', share='30.8 %', yr=2008, s=PEPSI, note='all brands of the company; Beverage Digest figure quoted on the Pepsi page'),
 dict(mkt='US carbonated soft drinks', who='The Coca-Cola Company', share='+0.4 volume share points', yr=2024, s='https://www.beverage-digest.com/articles/1164-soft-drink-performance-coca-cola-widens-us-share-gap-with-pepsico-in-first-nine-months', note='change in the first nine months; the fetched excerpt gives changes, not the level'),
 dict(mkt='US carbonated soft drinks', who='PepsiCo', share='-0.7 volume share points', yr=2024, s='https://www.beverage-digest.com/articles/1164-soft-drink-performance-coca-cola-widens-us-share-gap-with-pepsico-in-first-nine-months', note='change in the first nine months; the fetched excerpt gives changes, not the level'),
 dict(mkt='US soft drinks (retail)', who='The Coca-Cola Company', share='about double its closest competitors', yr=2024, s='https://www.foodbusinessmea.com/dr-pepper-ties-pepsi-as-americas-second-favorite-soda/', note='no figure given; Beverage Digest data reported by the Wall Street Journal, June 2024; Dr Pepper tied Pepsi for second place in regular soft drinks'),
 dict(mkt='US carbonated soft drinks', who='Keurig Dr Pepper', share='Dr Pepper second most sold soda brand', yr=2024, s=U['KDP'], note='no figure given; by retail sales, mid-2024, behind Coca-Cola'),
 dict(mkt='US craft soda', who='craft brands together', share='1 %', yr=2015, s=U['CSW'], note='trend share stated on the page; world craft-soda value USD 537.9 million in 2016 (Grand View Research)'),
 dict(mkt='India carbonated soft drinks', who='Pepsi (PepsiCo brand)', share='about 15 %', yr=2012, s=PEPSI, note='brand share; Coca-Cola brand about 8.8 %, behind Sprite and Thums Up'),
 dict(mkt='India carbonated soft drinks', who='Thums Up', share='85 %', yr=1993, s='https://en.wikipedia.org/wiki/Thums_Up', note='share when The Coca-Cola Company bought the brand in 1993'),
 dict(mkt='Peru soft drinks', who='Inca Kola', share='26 %', yr=2012, s='https://knowledge.wharton.upenn.edu/article/branding-lessons-from-inca-kola-the-peruvian-soda-that-bested-coca-cola/', note='"currently" in an October 2012 article; Coca-Cola 25.5 %'),
 dict(mkt='Peru soft drinks', who='Inca Kola', share='32.9 %', yr=1995, s='https://en.wikipedia.org/wiki/Inca_Kola', note='Coca-Cola 32 %; Coca-Cola bought half of Inca Kola Perú in 1999'),
 dict(mkt='Russia soft drinks', who='Coca-Cola', share='19.4 %', yr=2005, s=PEPSI, note='July 2005; Pepsi 13 %'),
 dict(mkt='Japan soft drinks', who='The Coca-Cola Company', share='22.4 %', yr=2018, s='https://www.foodnavigator.com/Article/2018/03/08/How-beverage-firms-can-put-the-fizz-back-into-Japan-s-flat-soft-drinks-market/', note='year not stated in the article, published March 2018; Suntory 17.1 %'),
 dict(mkt='Japan soft drinks', who='Suntory', share='17.1 %', yr=2018, s='https://www.foodnavigator.com/Article/2018/03/08/How-beverage-firms-can-put-the-fizz-back-into-Japan-s-flat-soft-drinks-market/', note='second largest after Coca-Cola'),
 dict(mkt='Middle East soft drinks', who='PepsiCo', share='about 75 %', yr=2003, s='https://en.wikipedia.org/wiki/The_Coca-Cola_Company', note='page says Coca-Cola holds almost 25 % to Pepsi\'s 75 %, around 2003'),
 dict(mkt='Scotland soft drinks', who='A.G. Barr (Irn-Bru)', share='top-selling brand for more than a century', yr=2003, s='https://en.wikipedia.org/wiki/Irn-Bru', note='no figure; Coca-Cola second and roughly equal by 2003; third best seller in the UK behind Coca-Cola and Pepsi'),
]
ms_energy = [
 dict(mkt='Global energy drinks', who='Red Bull GmbH', share='13 %', yr=2023, s='https://en.wikipedia.org/wiki/Red_Bull', note='global market share as stated on the page'),
 dict(mkt='Global energy drinks', who='Monster Beverage', share='39 %', yr=2020, s='https://en.wikipedia.org/wiki/Monster_Beverage', note='of an USD 86 billion market, as stated on the page; conflicts with the Red Bull figure, definitions differ'),
 dict(mkt='US convenience and gas energy drinks', who='Monster Beverage', share='34.7 % (36.7 % with Bang)', yr=2024, s='https://www.marketbeat.com/earnings/transcripts/110346', note='Nielsen, dollars, four weeks ended 20 July 2024, company statement'),
 dict(mkt='US convenience and gas energy drinks', who='Red Bull GmbH', share='35.9 %', yr=2024, s='https://www.marketbeat.com/earnings/transcripts/110346', note='same period; stated without the percent sign'),
 dict(mkt='US convenience and gas energy drinks', who='Celsius', share='7.9 %', yr=2024, s='https://www.marketbeat.com/earnings/transcripts/110346', note='same period as assumed in the transcript'),
]
ms_water = [
 dict(mkt='US beverage consumption', who='bottled water (category)', share='about 25 %', yr=2022, s='https://en.wikipedia.org/wiki/Bottled_water', note='consumption share against 18.7 % for soft drinks, Statista as quoted on the page'),
 dict(mkt='US bottled water (retail)', who='Primo Brands', share='number one (no figure)', yr=2024, s='https://www.sec.gov/Archives/edgar/data/2042694/000204269425000003/prmb-20241231.htm', note='company statement in its 2024 annual report'),
 dict(mkt='India bottled water', who='top five companies', share='67 %', yr=2013, s='https://en.wikipedia.org/wiki/Bottled_water', note='named as Bisleri, PepsiCo, Coca-Cola and Parle'),
]
DEP['Sodas']['ms'] = ms_soda
DEP['Energy & sports drinks']['ms'] = ms_energy
DEP['Water']['ms'] = ms_water
DEP['Sodas']['msum'] = ('Three groups hold most US soda: The Coca-Cola Company, PepsiCo and Keurig Dr Pepper. Beverage Digest figures quoted on fetched pages put Coca-Cola at 42.7 % and PepsiCo at 30.8 % in 2008; '
                        'no fetched page gives their current levels. Outside the US the leader differs by market, such as Irn-Bru in Scotland, Inca Kola in Peru and Thums Up in India. Craft soda is a small share.')
DEP['Energy & sports drinks']['msum'] = 'Red Bull and Monster lead energy drinks; the two together hold about 70 % of US convenience-store sales in the 2024 Nielsen figures a fetched company call quotes.'
DEP['Water']['msum'] = 'Bottled water has overtaken soft drinks by US consumption share. Primo Brands (Poland Spring, Deer Park and others) says it leads US retail; Nestlé, Danone, The Coca-Cola Company and PepsiCo hold the large remaining brands.'

# brand register additions
have = {b['n'] for b in brands['b']}
def addb(n, c, tier, kind, src):
    if not n or n in have: return
    have.add(n)
    seg = 'Artisan & independent' if tier == 'Craft & indie' else 'Mainstream'
    brands['b'].append(dict(n=n, c=c, f='', seg=seg, d=f'{kind} brand listed by a fetched reference.', lines=[], eras=[], sig=[n], sc=[], rel=[], s=src, kf=kind.lower()))
for kn, k in kinds.items():
    for x in k.get('x', []):
        addb(x.get('mk') or x['n'], x.get('cty', ''), x.get('tier', ''), kn, x['s'])
        o = x.get('own', '')
        if o and o not in have:
            have.add(o)
            brands['b'].append(dict(n=o, c='', f='', seg='Mainstream', d='Company named as owner of drink brands on a fetched reference.', lines=[], eras=[], sig=[o], sc=[], rel=[], s=x['s'], kf='owner'))
brands['b'].sort(key=lambda b: b['n'].lower())

def wr(path, obj):
    t = path + '.tmp'
    json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1)
    os.replace(t, path)
wr(R + 'out/J9.json', d)
wr(R + 'out/J9_brands.json', brands)
tot = sum(len(k.get('x', [])) for k in kinds.values())
print('entries', tot, 'new', sum(newcount.values()), 'brands', len(brands['b']))
import collections
print(collections.Counter(x.get('tier', '-') for k in kinds.values() for x in k.get('x', [])))
