import json, copy, os
R = '/home/user/Possession-Taxonomy/rebuild/'
src = json.load(open(R + 'out/A2.json'))
BR = json.load(open(R + 'out/A2_brands.json'))['b']
BL = {b['n'].lower(): b for b in BR}

WP = 'https://en.wikipedia.org/wiki/'
LIST = WP + 'List_of_shoe_styles'
LISTB = WP + 'List_of_boots'
FM = 'https://footwearmagazine.com/2026-footwear-brand-power-rankings/'

# ---------- owner facts (each from a page fetched in this batch) ----------
OWN = {
 'Nike': ('Nike, Inc.', 'Global group', '', 'United States'),
 'Jordan Brand': ('Nike, Inc.', 'Global group', '', 'United States'),
 'Converse': ('Nike, Inc.', 'Global group', '2003', 'United States'),
 'adidas': ('adidas AG', 'Global group', '', 'Germany'),
 'Puma': ('Puma SE', 'Global group', '', 'Germany'),
 'New Balance': ('Jim Davis', 'Global group', '1972', 'United States'),
 'ASICS': ('ASICS Corporation', 'Global group', '', 'Japan'),
 'Onitsuka Tiger': ('ASICS Corporation', 'Global group', '', 'Japan'),
 'Reebok': ('Authentic Brands Group', 'Independent', '2022', 'United Kingdom'),
 'Vans': ('VF Corporation', 'Global group', '2004', 'United States'),
 'Timberland': ('VF Corporation', 'Global group', '2011', 'United States'),
 'Altra': ('VF Corporation', 'Global group', '2018', 'United States'),
 'Skechers': ('3G Capital', 'Global group', '2025', 'United States'),
 'UGG': ('Deckers Brands', 'Global group', '1995', 'Australia'),
 'Hoka': ('Deckers Brands', 'Global group', '2013', ''),
 'Teva': ('Deckers Brands', 'Global group', '2002', 'United States'),
 'Merrell': ('Wolverine World Wide', 'Global group', '1997', 'United States'),
 'Saucony': ('Wolverine World Wide', 'Global group', '2012', 'United States'),
 'Chaco': ('Wolverine World Wide', 'Global group', '2009', 'United States'),
 'Stride Rite': ('Wolverine World Wide', 'Global group', '2012', 'United States'),
 'Hush Puppies': ('Wolverine World Wide', 'Global group', '', 'United States'),
 'Wolverine': ('Wolverine World Wide', 'Global group', '', 'United States'),
 'Brooks': ('Berkshire Hathaway', 'Independent', '2006', 'United States'),
 'Dr. Martens': ('Dr. Martens plc', 'Independent', '', 'United Kingdom'),
 'Birkenstock': ('L Catterton', 'Independent', '2021', 'Germany'),
 'Crocs': ('Crocs, Inc.', 'Independent', '', 'United States'),
 'Hey Dude': ('Crocs, Inc.', 'Independent', '2022', 'United States'),
 'Red Wing': ('Red Wing Shoes (private)', 'Independent', '', 'United States'),
 "Church's": ('Prada', 'Independent', '1999', 'United Kingdom'),
 'Li-Ning': ('Li-Ning Company Limited', 'National champion', '', 'China'),
 'Anta': ('Anta Sports', 'National champion', '', 'China'),
 'Bata': ('Bata Corporation', 'Independent', '', 'Czech Republic'),
 'Stuart Weitzman': ('Caleres', 'Independent', '2025', 'United States'),
 'Jimmy Choo': ('Capri Holdings', 'Global group', '2017', 'United Kingdom'),
 'Salomon': ('Amer Sports', 'Global group', '', 'France'),
 'Keds': ('owner not stated', 'Independent', '', 'United States'),
 'Sperry': ('owner not stated', 'Independent', '', 'United States'),
 'Sebago': ('owner not stated', 'Independent', '', 'Italy'),
}
for k, v in OWN.items():
    if k.lower() not in BL:
        print('WARN brand not in register', k)

BORDER = {}

def cty_of(mk):
    if not mk: return ''
    b = BL.get(mk.lower())
    if mk in OWN and OWN[mk][3]: return OWN[mk][3]
    return (b or {}).get('c', '') or ''

def E(n, mk='', y='', d='', s=WP, a='', v=None, role=None):
    e = {'n': n}
    if a: e['a'] = a
    if d: e['d'] = d
    if mk: e['mk'] = mk
    if y: e['y'] = y
    e['s'] = s
    if v: e['v'] = v
    if role: e['role'] = role
    return e

def V(n, mk='', y='', d=''):
    return {'n': n, 'mk': mk, 'y': y, 'd': d}

NIKEP = WP + 'Nike,_Inc.'
NBP = WP + 'New_Balance'
RBK = WP + 'Reebok'
ADP = WP + 'Adidas'
PUMAP = WP + 'Puma_(brand)'
SKP = WP + 'Skechers'
CVP = WP + 'Converse_(shoe_company)'
WD = 'https://www.wikidata.org/wiki/'
AJP = WP + 'Air_Jordan'
AMP = WP + 'Nike_Air_Max'

# ---------- Air Jordan numbered line (Wikipedia Air_Jordan) ----------
AJY = {1: '1984', 2: '1986', 3: '1988', 4: '1989', 5: '1990', 6: '1991', 7: '1992', 8: '1993', 9: '1993', 10: '1994',
       11: '1995', 12: '1996', 13: '1997', 14: '1998'}
AJNEW = [
 ('Air Jordan 15', '1999', ''), ('Air Jordan 16', '2001', ''), ('Air Jordan 17', '2002', ''),
 ('Air Jordan 18', '2003', 'Designed by Tate Kuerbis.'), ('Air Jordan 19', '2004', ''), ('Air Jordan 20', '2005', ''),
 ('Air Jordan 21', '2006', "Designed by D'Wayne Edwards."), ('Air Jordan 22 (XX2)', '2007', ''),
 ('Air Jordan 23 (XX3)', '2008', 'Designed by Tinker Hatfield.'), ('Air Jordan 2009', '2009', 'Year-named model; designed by Jason Mayden.'),
 ('Air Jordan 2010', '2010', 'Year-named model.'), ('Air Jordan 2011', '2011', 'Year-named model.'), ('Air Jordan 2012', '2012', 'Year-named model.'),
 ('Air Jordan 28 (XX8)', '2013', 'Designed by Tinker Hatfield.'), ('Air Jordan 29 (XX9)', '2014', 'Designed by Tinker Hatfield.'),
 ('Air Jordan 30 (XXX)', '2016', 'Designed by Tinker Hatfield.'), ('Air Jordan 31', '2016', ''), ('Air Jordan 32', '2017', ''),
 ('Air Jordan 33', '2018', ''), ('Air Jordan 34', '2019', ''), ('Air Jordan 35', '2020', ''), ('Air Jordan 36', '2021', ''),
 ('Air Jordan 37', '2022', ''), ('Air Jordan 38', '2023', ''), ('Air Jordan 39', '2024', ''), ('Air Jordan 40', '2025', ''),
]
AJD = {1: 'Peter B. Moore', 2: 'Peter Moore and Bruce Kilgore', 4: 'Tinker Hatfield', 5: 'Tinker Hatfield', 11: 'Tinker Hatfield',
       13: 'Tinker Hatfield', 14: 'Tinker Hatfield and Mark Smith'}

# ---------- Air Max (Wikipedia Nike_Air_Max) ----------
AMY = {'Air Max 1': '1986', 'Air Max 90': '1990', 'Air Max BW': '1991', 'Air Max 180': '1991', 'Air Max 93': '1993',
       'Air Max 95': '1995', 'Air Max 97': '1997', 'Air Max Plus': '1998', 'Air VaporMax': '2017'}
AMNEW = [('Air Max Light', '1989', ''), ('Air Max2 CB 94', '1994', 'Tracy Teague (designer).'), ('Air Max 360', '2006', ''),
         ('Air Max 270', '2018', ''), ('Air Max 200', '2019', ''), ('Air Max 720', '2019', ''), ('Air Max 2090', '2020', ''),
         ('Air Max Pre-Day', '2021', ''), ('Air Max Scorpion', '2022', ''), ('Air Max Pulse', '2023', ''), ('Air Max DN', '2024', '')]

ADD = {  # kind -> new entries
 'Basketball sneaker': [
  E('Clyde', 'Puma', '1973', 'Walt Frazier signature shoe, listed on the Puma Wikipedia page as the Puma Clyde.', PUMAP),
  E('Question', 'Reebok', '1996', 'Reebok basketball shoe listed with its year on the Reebok page.', RBK),
  E('Shaq Attaq', 'Reebok', '1992', 'Reebok basketball shoe listed with its year on the Reebok page.', RBK),
  E('Weapon', 'Converse', '1986', 'Basketball shoe called The Weapon; The Weapon EVO followed in 2009.', CVP),
  E('Forum', 'adidas', '', 'Adidas Originals sneaker with its own Wikidata item.', WD + 'Q123347106'),
  E('Mag', 'Nike', '2015', 'Released in 2015 by auction, with proceeds to the Michael J. Fox Foundation.', NIKEP, a='Nike Mag'),
 ],
 'Court sneaker': [
  E('Smash Leather', 'Puma', '', 'Lifestyle court shoe shown on the Puma page.', PUMAP),
  E('Startas', 'Borovo', '1976', 'Athletic shoe with its own Wikidata item.', WD + 'Q29168432'),
 ],
 'Heritage running sneaker': [
  E('Moon Shoe', 'Nike', '1972', 'Named with its year on the Nike page.', NIKEP),
  E('Trackster', 'New Balance', '1960', 'Named with its year on the New Balance page.', NBP),
  E('550', 'New Balance', '', 'Named model on the New Balance page.', NBP),
  E('480', 'New Balance', '', 'Named model on the New Balance page.', NBP),
  E('1906', 'New Balance', '', 'Named model on the New Balance page.', NBP),
  E('2002', 'New Balance', '', 'Named model on the New Balance page.', NBP),
  E('576', 'New Balance', '', 'Named model on the New Balance page.', NBP),
  E('NMD R1', 'adidas', '2016', 'Released with the NMD XR1 in September 2016.', ADP),
  E('EQT Support 93/17', 'adidas', '2017', 'Released in January 2017 with the EQT Support ADV and Ultra.', ADP),
  E('Freestyle', 'Reebok', '1982', 'Listed with its year on the Reebok page and with its own Wikidata item.', RBK),
  E('Classic Leather', 'Reebok', '', 'Named model on the Reebok page.', RBK),
  E('Workout', 'Reebok', '1984', 'Listed with its year on the Reebok page.', RBK),
  E('Ventilator', 'Reebok', '1990', 'Listed with its year on the Reebok page.', RBK),
  E("D'Lites", 'Skechers', '', 'Named Skechers line on the Skechers page.', SKP),
 ],
 'Chunky sneaker': [
  E('Instapump Fury', 'Reebok', '1994', 'Listed with its year on the Reebok page.', RBK),
 ],
 'Skate shoe': [
  E('One Star', 'Converse', '1974', 'Converse model introduced in 1974.', CVP),
 ],
 'Running shoe': [
  E('Air Zoom Vomero', 'Nike', '2006', 'Introduced in 2006 according to the Nike page.', NIKEP),
  E('GT-2000', 'ASICS', '', 'Named on the ASICS page alongside the 1993 Gel-Kayano.', WP + 'Asics'),
 ],
 'Walking shoe': [
  E('GO WALK', 'Skechers', '', 'Named Skechers walking line on the Skechers page.', SKP),
  E('Slip-ins', 'Skechers', '', 'Named Skechers design; a 2024 patent suit concerns it.', SKP),
  E('Shape-Ups', 'Skechers', '', 'Rocker-bottom line tied to a 2012 FTC-related settlement.', SKP),
 ],
}

# birkenstock / brand year fixes: (kind, entry) -> dict
FIX = {
 ('Slide', 'Arizona'): {'y': '1973', 'd': 'Two-strap sandal listed with its year on the Birkenstock page.', 's': WP + 'Birkenstock'},
 ('Slide', 'Madrid'): {'y': '1963', 'd': 'The original footbed sandal, named Madrid from 1979.', 's': WP + 'Birkenstock', 'role': 'origin'},
 ('Clog', 'Boston'): {'y': '1976', 'd': 'First Birkenstock cork clog.', 's': WP + 'Birkenstock'},
 ('Flip-flop', 'Gizeh'): {'y': '1983', 'd': 'Thong sandal listed with its year on the Birkenstock page.', 's': WP + 'Birkenstock'},
 ('Dr. Martens lace-up', '1460'): {'y': '1960', 'd': 'Eight-eyelet boot introduced on 1 April 1960.', 's': WP + 'Dr._Martens'},
 ('Dr. Martens lace-up', '1461'): {'y': '1961', 'd': 'Three-eyelet shoe introduced a year after the 1460.', 's': WP + 'Dr._Martens'},
 ('Basketball sneaker', 'Pro Leather'): {'y': '1976', 's': CVP},
 ('Running shoe', 'Ghost'): {'y': '2008', 's': WP + 'Brooks_Sports'},
 ('Running shoe', 'Adrenaline GTS'): {'y': '1994', 's': WP + 'Brooks_Sports'},
 ('Running shoe', 'Gel-Kayano'): {'y': '1993', 's': WP + 'Asics'},
 ('Running shoe', 'Gel-Nimbus'): {'y': '1999', 's': WP + 'Asics'},
 ('Heritage running sneaker', 'Waffle Trainer'): {'y': '1974', 's': NIKEP},
 ('Heritage running sneaker', 'Air Huarache'): {'y': '1992', 's': NIKEP},
 ('Court sneaker', 'Club C 85'): {'y': '1985', 's': RBK},
 ('Basketball sneaker', 'Pump'): {'y': '1989', 's': RBK},
 ('Skate shoe', 'Classic Slip-On'): {},
}

# ---------- kind metadata ----------
BRANDSEL = ' Entries are sectioned by the brand\'s home country, then brand, then year.'
META = {
 'Basketball sneaker': ('One entry is a basketball shoe silhouette or model line sold under its own name; retros, colourways and collaborations are versions.',
   "The Wikipedia pages of the makers (Nike, Converse, Reebok, Puma, adidas) and the Air Jordan list; the Air Jordan numbered line has its own kind." + BRANDSEL),
 'Air Jordan': ('One entry is a numbered or year-named Air Jordan model; retro releases and collaborations are versions.',
   "Wikipedia's Air Jordan article, every numbered model from Air Jordan 1 to Air Jordan 40 and the year-named 2009 to 2012 models. Jordan Brand lines named after other players are not on the pages read."),
 'Court sneaker': ('One entry is a low court or tennis-derived shoe silhouette sold under its own name.', "Maker pages (Nike, Reebok, Puma, adidas, Lacoste) and Wikidata items." + BRANDSEL),
 'Canvas sneaker': ('One entry is a canvas or plimsoll silhouette sold under its own name.', "Maker pages and Wikidata (Vans Authentic, Q20058251)." + BRANDSEL),
 'Heritage running sneaker': ('One entry is an old running, training or lifestyle silhouette sold under its own name; reissues, generations and collaborations are versions.',
   "Wikipedia's Nike Air Max list (every Air Max model from the Air Max 1 to the Air Max DN), the New Balance 99X series and the maker pages of New Balance, adidas, Reebok, Nike, ASICS and Skechers." + BRANDSEL),
 'Terrace sneaker': ('One entry is a terrace or indoor-sport silhouette sold under its own name.', "Maker pages (adidas, Puma, Diadora)." + BRANDSEL),
 'Skate shoe': ('One entry is a skate shoe silhouette sold under its own name.', "Maker pages (Vans, Nike, Converse) and the Vans and Nike pages." + BRANDSEL),
 'Chunky sneaker': ('One entry is a chunky-midsole silhouette sold under its own name.', "Maker pages." + BRANDSEL),
 'Designer sneaker': ('One entry is a fashion-house or designer sneaker silhouette sold under its own name.', "Maker pages of each house." + BRANDSEL),
}
GENERIC = {}

def meta_default(k):
    return ('One entry is a model line or design of this kind sold under its own name; sizes, colours and model years are versions.',
            'Maker, Wikipedia and reference pages named on each entry.' + BRANDSEL)

# removal of aggregates
DROP = {('Heritage running sneaker', 'Later Air Max models'), ('Heritage running sneaker', '99X numbered models')}

report = {'m_removed': {}, 'm_total': 0}
newd = []
for dp in src['depts']:
    dp = copy.deepcopy(dp)
    for sh in dp['s']:
        for k in sh['k']:
            kn = k['n']
            if k.get('m'):
                report['m_removed'][kn] = len(k['m']); report['m_total'] += len(k['m'])
            k.pop('m', None)
            xs = [x for x in k.get('x', []) if (kn, x['n']) not in DROP]
            # merge 99X into 990
            if kn == 'Heritage running sneaker':
                nine = [x for x in k['x'] if x['n'] == '990'][0]
                nn = [x for x in k['x'] if x['n'] == '99X numbered models'][0]
                nine['n'] = '990 series'
                nine['d'] = "New Balance's grey-suede premium runner, made in the USA; the 99X page numbers later models from 991 to 999."
                nine['v'] = nine['v'] + nn['v']
                # dissolve Later Air Max
            for fk, fv in FIX.items():
                if fk[0] == kn:
                    for x in xs:
                        if x['n'] == fk[1]: x.update(fv)
            if kn == 'Air Jordan':
                for x in xs:
                    num = int(x['n'].split()[-1])
                    x['y'] = AJY[num]
                    if num in AJD and 'Michael Jordan' not in x['d'] or True:
                        pass
                    x['s'] = AJP
                    x['v'] = x.get('v', [])
                for x in xs:
                    if x['n'] == 'Air Jordan 1':
                        x['role'] = 'origin'
                for n_, y_, d_ in AJNEW:
                    xs.append(E(n_, 'Nike', y_, ('Numbered Michael Jordan signature basketball shoe. ' + d_).strip() if 'Year-named' not in d_ else d_, AJP))
                k['d'] = 'Michael Jordan\'s numbered signature basketball line, one entry per model (1 to 40, with the year-named 2009 to 2012 models).'
            if kn == 'Heritage running sneaker':
                for x in xs:
                    if x['n'] in AMY: x['y'] = AMY[x['n']]; x['s'] = AMP
                for n_, y_, d_ in AMNEW:
                    xs.append(E(n_, 'Nike', y_, d_, AMP))
            for e in ADD.get(kn, []):
                if not any(x['n'].lower() == e['n'].lower() for x in xs): xs.append(e)
            k['x'] = xs
    newd.append(dp)

# ---------- shoe care: commodity plus icon rule ----------
def kinds(dp):
    return [k for s in dp['s'] for k in s['k']]
care = [d_ for d_ in newd if d_['n'] == 'Shoe care & accessories'][0]
for k in kinds(care):
    k['x'] = []
polish = [k for k in kinds(care) if k['n'] == 'Shoe polish and conditioner'][0]
polish['x'] = [E("Warren's blacking", '', '1795', 'Thomas and Jonathan Warren began making blacking in London around 1795 to 1798, the earliest commercial maker named on Wikipedia.', WP + 'Shoe_polish', role='origin')]
polish['nl'] = 'One entry is the origin product of a commodity kind; brand polishes are not listed.'
polish['sel'] = "Commodity rule: only the first product of the kind, as Wikipedia's Shoe polish article states it. Complete: 1 of 1 qualifying (no design-collection or award landmark found for shoe care)."

# ---------- traditional footwear ----------
trad = [d_ for d_ in newd if d_['n'].startswith('Traditional')][0]
def tk(name, d, ents, tt, region, see=None):
    k = {'n': name, 'd': d, 's': LIST, 'x': ents, 'tt': tt}
    return k
def TE(n, region, d='', s=LIST):
    e = E(n, '', '', d, s); e['g'] = region; return e
tt_form = [['Material', ['Leather', 'Wood', 'Straw or fibre', 'Cloth']], ['Occasion', ['Everyday', 'Ceremonial']]]
shelves = {s['n']: s for s in trad['s']}
shelves['East Asian footwear']['k'].append(tk('East Asian named forms', 'Further shoe forms of Japan, Korea and China that Wikipedia names in its shoe-style list.', [
  TE('Gomusin', 'Korea'), TE('Namaksin', 'Korea'), TE('Hwa', 'Korea and China'), TE('Lotus shoes', 'China'), TE('Xiuhuaxie', 'China'),
  TE('Kung fu shoe', 'China'), TE('Hanfu footwear', 'China'), TE('Uwabaki', 'Japan')], tt_form, 'East Asia'))
shelves['South Asian & Middle Eastern footwear']['k'].append(tk('Mojari', 'Pointed leather slip-on of North India and Pakistan, listed apart from the jutti in the Wikipedia shoe-style list.', [
  TE('Multani khussa', 'Pakistan'), TE('Mojari (Rajasthani)', 'India')], [['Toe', ['Pointed', 'Curled']], ['Decoration', ['Plain', 'Embroidered']]], 'South Asia'))
shelves['South Asian & Middle Eastern footwear']['k'].append(tk('South Asian and Middle Eastern named forms', 'Further shoe forms of South Asia, Iran and North Africa that Wikipedia names in its shoe-style list.', [
  TE('Upanah', 'South Asia'), TE('Galesh', 'Iran'), TE('Balgha', 'North Africa')], tt_form, 'South Asia and Middle East'))
shelves['European footwear']['k'].append(tk('Named European forms', 'Regional and historic European shoe forms that Wikipedia names in its shoe-style list.', [
  TE('Caligae', 'Ancient Rome'), TE('Calceus', 'Ancient Rome'), TE('Soccus', 'Ancient Rome'), TE('Buskin', 'Ancient Greece and Rome'),
  TE('Poulaine', 'Medieval Europe'), TE('Pigache', 'Medieval Europe'), TE('Chopine', 'Venice'), TE('Patten', 'Europe'),
  TE('Tsarouchi', 'Greece'), TE('Tzangion', 'Greece'), TE('Pampootie', 'Ireland'), TE('Ghillies', 'Scotland and Ireland'),
  TE('Avarca', 'Spain'), TE('Cantabrian albarcas', 'Spain'), TE('Flamenco shoe', 'Spain'), TE('Träskor', 'Sweden'),
  TE('Haferlschuh', 'Austria and Bavaria'), TE('Furlane', 'Italy'), TE('Ciocia', 'Italy'), TE('Sabot', 'France')], tt_form, 'Europe'))
shelves['Arctic, Philippine & African footwear']['k'].append(tk('Named South-East Asian and African forms', 'Further shoe forms of South-East Asia and southern Africa that Wikipedia names in its shoe-style list.', [
  TE('Hnyat-phanat', 'Myanmar'), TE('Peranakan beaded slippers', 'South-East Asia'), TE('Abaca slippers', 'Philippines'), TE('Opinga', 'South Africa')], tt_form, 'SE Asia and Africa'))
trad['s'].append({'n': 'Forms the list does not place', 't': 'Shoe forms named in the Wikipedia shoe-style list with no region on the list or on a page read; a modern shoe → its own department.',
  'k': [tk('Unplaced named forms', 'Shoe forms that appear only as names in the Wikipedia shoe-style list.', [TE('Pulhoer', 'Region not stated'), TE('Pointinini', 'Region not stated')], tt_form, '')]})

# regions for existing traditional entries
REG = {'East Asian footwear': 'East Asia', 'South Asian & Middle Eastern footwear': 'South Asia and Middle East', 'European footwear': 'Europe',
       'Arctic, Philippine & African footwear': 'Arctic, South-East Asia and Africa'}
for sh in trad['s']:
    for k in sh['k']:
        for x in k['x']:
            if 'g' not in x: x['g'] = REG.get(sh['n'], 'Region not stated')
        if k['x']:
            k['nl'] = 'One entry is a named regional or historic shoe form (a type within the kind); makers and sizes are not listed.'
            k['sel'] = ("Names from Wikipedia's List of shoe styles, read in full (about 190 entries, names only, no descriptions); entries that duplicate a kind of this department are those kinds. "
                        "The list gives no regions or facts, so region is placed from the form's own name and the entries carry no description. Complete: every form of the list in this department's scope is a kind or an entry here; sport, ballet, medical and novelty entries belong to other departments or are out of scope.")
            k['xg'] = 'by region'

# ---------- boots additions from List of boots ----------
boots = [d_ for d_ in newd if d_['n'] == 'Boots'][0]
for sh in boots['s']:
    if sh['n'].startswith('Dress'):
        sh['k'].append({'n': 'Pointed-toe boot', 'd': 'Boot with a long pointed toe, such as the winklepicker and the Mexican pointy boot.', 's': LIST,
            'x': [E('Winklepicker', '', '', '', LIST), E('Mexican pointy boots', '', '', '', LIST)], 'tt': [['Toe', ['Pointed', 'Extra-long']], ['Heel', ['Cuban', 'Cowboy']]]})
    if sh['n'].startswith('Work'):
        sh['k'].append({'n': 'Jackboot & Hessian boot', 'd': 'Tall military boots of the cavalry and infantry, such as the jackboot and the Hessian.', 's': LISTB,
            'x': [E('Jackboot', '', '', '', LIST), E('Hessian boot', '', '', '', LIST), E('Cavalry jackboots', '', '', '', LISTB), E('Hobnailed jackboots', '', '', '', LISTB)],
            'tt': [['Height', ['Knee-high', 'Mid-calf']], ['Sole', ['Leather', 'Hobnailed']]]})

# ---------- apply g, nl, sel, xg, own fields ----------
used_brands = {}
for dp in newd:
    for sh in dp['s']:
        for k in sh['k']:
            xs = k.get('x') or []
            if not xs: continue
            for x in xs:
                mk = x.get('mk', '')
                if 'g' not in x:
                    if mk:
                        c = cty_of(mk)
                        x['g'] = (c or 'Country not stated') + ' · ' + mk
                    else:
                        x['g'] = 'Design with no single maker'
                if mk and mk in OWN:
                    o = OWN[mk]
                    x['own'], x['tier'], x['cty'] = o[0], o[1], cty_of(mk)
                    if o[2]: x['own_y'] = o[2]
                    used_brands[mk] = o
                elif mk:
                    c = cty_of(mk)
                    x['cty'] = c
                    x['own'] = 'owner not stated'
                    used_brands.setdefault(mk, None)
                for v in x.get('v') or []:
                    pass
            if dp['n'].startswith('Traditional'):
                continue
            nl, sel = META.get(k['n'], meta_default(k))
            if k['n'] in ('Shoe polish and conditioner',): continue
            if k['n'] in ('Pointed-toe boot', 'Jackboot & Hessian boot'):
                nl = 'One entry is a named shoe form listed by Wikipedia.'
                sel = "Names from Wikipedia's List of shoe styles and List of boots; the lists give no descriptions."
                k['xg'] = 'by design'
            k['nl'] = nl
            k['sel'] = sel
            k.setdefault('xg', 'by brand country, then brand' if any(x.get('mk') for x in xs) else 'by design')
            # order
            def key(x):
                return (x['g'].startswith('Design'), x['g'], x.get('y', '9999') or '9999', x['n'])
            if not dp['n'].startswith('Traditional'):
                xs.sort(key=lambda x: (x['g'].startswith('Design'), x['g'], (x.get('y') or '9999')[:4], x['n']))

# coverage lines
COV = {
 'Air Jordan': 'Complete: 40 numbered models plus the 4 year-named models (2009 to 2012) of 44 on the page.',
 'Heritage running sneaker': 'Complete for the Nike Air Max list (20 of 20 models) and the New Balance 99X series; other makers are a selection from their pages that name models with years. Covers about 60 of the many heritage runners; the makers\' own heritage pages were not readable enough to list the rest.',
}
for dp in newd:
    for sh in dp['s']:
        for k in sh['k']:
            if k['n'] in COV and k.get('sel'): k['sel'] += ' ' + COV[k['n']]
            elif k.get('x') and k.get('sel') and not dp['n'].startswith('Traditional') and 'Complete' not in k['sel'] and 'Covers' not in k['sel']:
                n = len(k['x'])
                k['sel'] += f' Covers {n} entries kept from the earlier pass and the pages read; the makers\' catalogues are not exhausted.'

# ---------- department level ----------
sn = [d_ for d_ in newd if d_['n'] == 'Sneakers'][0]
sn['ms'] = []
for who, sh in [('Nike', '26 %'), ('adidas', '14 %'), ('Skechers', '9 %'), ('Puma', '5 %'), ('New Balance', '4 %'), ('ASICS', '3 %'), ('Under Armour', '3 %'),
                ('Converse', '2 %'), ('Vans', '2 %'), ('On Running', '2 %'), ('HOKA', '2 %'), ('Other brands combined', '28 %')]:
    sn['ms'].append({'mkt': 'Global athletic and sneaker footwear', 'who': who, 'share': sh, 'yr': 2026, 's': FM,
                     'note': 'estimated share from aggregated industry reporting, as the page states'})
sn['msum'] = ('Footwear Magazine estimates Nike at 26 % of global athletic and sneaker footwear in 2026, adidas at 14 %, Skechers at 9 % and Puma at 5 %. '
              'Converse and Vans sit under Nike and VF Corporation. No regional shares were found on a fetched page.')

# ---------- brand updates and new register entries ----------
bu = {}
for mk, o in OWN.items():
    b = BL.get(mk.lower())
    if not b: continue
    bu[b['n']] = {'own': o[0], 'tier': o[1], 'c': o[3] or b.get('c', '')}
    if o[2]: bu[b['n']]['own_y'] = o[2]
newb = [
 {'n': 'VF Corporation', 'seg': 'Outdoor & technical', 'd': 'Owner of Vans (since 2004), Timberland (2011) and Altra (2018) per its Wikipedia page.', 's': WP + 'VF_Corporation', 'kf': 'owner group'},
 {'n': 'Deckers Brands', 'seg': 'Athletic & sportswear', 'd': 'Owner of UGG (1995), Hoka (2013), Teva (patents and trademarks 2002) and Koolaburra (2015).', 's': WP + 'Deckers_Brands', 'kf': 'owner group'},
 {'n': 'Wolverine World Wide', 'seg': 'Outdoor & technical', 'd': 'Owner of Merrell (1997), Chaco (2009), Saucony (2012), Stride Rite (2012), Hush Puppies and Wolverine; sold Keds (2023) and Sperry (2024).', 's': WP + 'Wolverine_World_Wide', 'kf': 'owner group'},
 {'n': 'Authentic Brands Group', 'seg': 'Athletic & sportswear', 'd': 'Acquired Reebok in 2022.', 's': WP + 'Reebok', 'kf': 'owner group'},
 {'n': 'Tapestry', 'seg': 'Contemporary & premium', 'd': 'Owner of Coach and Kate Spade; sold Stuart Weitzman in 2025.', 's': WP + 'Tapestry,_Inc.', 'kf': 'owner group'},
 {'n': 'Capri Holdings', 'seg': 'Contemporary & premium', 'd': 'Owner of Michael Kors and Jimmy Choo (since 2017); sold Versace to Prada in 2025.', 's': WP + 'Capri_Holdings', 'kf': 'owner group'},
 {'n': 'Amer Sports', 'seg': 'Outdoor & technical', 'd': 'Finnish sports group that includes Arc\'teryx, Salomon and Wilson; Anta holds 44.5 %.', 's': WP + 'Anta_Sports', 'kf': 'owner group'},
 {'n': 'Anta Sports', 'c': 'China', 'f': '1991', 'seg': 'Athletic & sportswear', 'd': 'Chinese sportswear group described as the third largest by revenue; largest shareholder of Puma (29.06 %, 2026).', 's': WP + 'Anta_Sports', 'kf': 'owner group'},
 {'n': 'Caleres', 'seg': 'High street', 'd': 'Completed the purchase of Stuart Weitzman from Tapestry on 4 August 2025.', 's': WP + 'Tapestry,_Inc.', 'kf': 'owner group'},
 {'n': 'Borovo', 'seg': 'Athletic & sportswear', 'd': 'Maker of the Startas shoe (1976) per Wikidata.', 's': WD + 'Q29168432', 'kf': 'sneakers'},
]
for b in newb:
    b.setdefault('c', ''); b.setdefault('f', ''); b.setdefault('lines', []); b.setdefault('sig', []); b.setdefault('rel', [])
    b.setdefault('eras', []); b.setdefault('sc', [])

part = {'replaces': [d_['n'] for d_ in src['depts']], 'depts': newd, 'brands': newb, 'brand_updates': bu, 'renames': {}, 'moves': []}
# renames: kinds renamed in this pass (none); entries renamed are not kinds
os.makedirs(R + 'out/A2_parts', exist_ok=True)
json.dump(part, open(R + 'out/A2_parts/ALL.tmp', 'w'), ensure_ascii=False)
os.replace(R + 'out/A2_parts/ALL.tmp', R + 'out/A2_parts/ALL.json')
print(report['m_total'], 'models removed')
json.dump(report, open(R + 'work/V4_A2_ALL/report_stats.json', 'w'))
print('unmapped brands', sorted(b for b, o in used_brands.items() if o is None))
tot = sum(len(k.get('x') or []) for dp in newd for s in dp['s'] for k in s['k'])
print('entries', tot, 'bytes', os.path.getsize(R + 'out/A2_parts/ALL.json'))
