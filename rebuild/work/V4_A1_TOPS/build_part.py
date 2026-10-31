import json, re, copy, os
ROOT = '/home/user/Possession-Taxonomy/'
OLD = json.load(open(ROOT + 'rebuild/out/A1.json'))
REG = {e['n']: e for e in json.load(open(ROOT + 'rebuild/out/A1_brands.json'))['b']}
W = 'https://en.wikipedia.org/wiki/'
DEPTS = ['Tops', 'Trousers, jeans & shorts', 'Dresses', 'Skirts, jumpsuits & sets']

# owners stated on the brand register's own description (register d), with year where stated
OWN = {'A Bathing Ape': ('I.T Group', ''), 'Bonds': ('Gildan', ''), 'Champion': ('Authentic Brands', ''),
       'DAKS': ('Sankyo Seiko', '1991'), 'Dale of Norway': ('Rossignol', '2018'), 'Hanes': ('Hanesbrands', ''),
       'Hervé Léger': ('BCBG Max Azria', ''), 'Lacoste': ('Maus Frères', ''), 'Stubbies': ('Workwear Group', ''),
       'Icebreaker': ('VF Corporation', '')}

NEWB = {}  # new brand register entries: name -> (segment, description, source, country)


def norm_c(c):
    if not c:
        return ''
    c = re.sub(r'\s*\(.*?\)', '', c)
    return c.split(' / ')[0].strip()


def cty(mk):
    e = REG.get(mk)
    return norm_c(e.get('c','')) if e else ''


old_entries = {}
for dp in OLD['depts']:
    if dp['n'] in DEPTS:
        for s in dp['s']:
            for k in s['k']:
                for x in k.get('x', []):
                    old_entries[(k['n'], x['n'])] = x


def V(mk, items):
    return [{'n': n, 'mk': mk, 'y': y, 'd': d} for n, y, d in items]


def N(n, mk, y, d, s=None, g=None, role=None, v=None, a=None, dt=None):
    """new entry"""
    if s is None:
        s = REG[mk].get('s') or ''
    e = {'n': n, 'a': a or '', 'd': d, 'mk': mk, 'y': y, 's': s}
    e['_g'] = g
    if role:
        e['role'] = role
    if v:
        e['v'] = v
    if dt:
        e['dt'] = dt
    return e


def K(kind, name, **ov):
    e = copy.deepcopy(old_entries[(kind, name)])
    for k, v in ov.items():
        e[k] = v
    e['_g'] = ov.get('_g')
    return e


def finish(e, kindname):
    mk = e.get('mk', '')
    g = e.pop('_g', None) or cty(mk) or 'Country not stated'
    e['g'] = g
    c = cty(mk) or (g if g != 'Country not stated' else '')
    if c:
        e['cty'] = c
    if mk in OWN:
        e['own'] = OWN[mk][0]
        if OWN[mk][1]:
            e['own_y'] = OWN[mk][1]
    e['y'] = e.get('y') or ''
    return e


def sortkey(e):
    y = re.search(r'\d{4}', e.get('y') or '')
    return (e['g'], e.get('mk', ''), int(y.group()) if y else 9999, e['n'])


KINDS = {}  # kind name -> dict(x=[...], nl=, sel=, xg=)


def kind(name, nl, ref, entries, xg='by brand country, then brand'):
    KINDS[name] = dict(nl=nl, ref=ref, entries=entries, xg=xg)


# ---------------------------------------------------------------- TOPS
kind('T-shirt',
     'One entry is a T-shirt sold under its own name by the brand that makes it, or a T-shirt design the Wikipedia article names with its originator; sizes, colours and sleeve lengths are versions.',
     'the T-shirt article (Wikipedia, fetched)',
     [K('T-shirt', 'Hanes Beefy-T'), K('T-shirt', 'Champion T1011', v=[
         {'n': 'T1011 short sleeve', 'mk': 'Champion', 'y': '', 'd': 'Made-in-USA heavyweight crew, plain or pocket'},
         {'n': 'Heritage Jersey Tee', 'mk': 'Champion', 'y': '', 'd': 'Champion line name in the brand register'}]),
      N('Hanes Essential-T', 'Hanes', '', 'Essential-T is a named Hanes tee line in the brand register.', v=V('Hanes', [('Hanes 5280 Essential-T', '', 'Essential-T style number 5280')])),
      K('T-shirt', 'Sunspel Classic T-shirt'), K('T-shirt', 'Supreme Box Logo tee'), K('T-shirt', 'Merz b. Schwanen 215'),
      N('Camber 301 Max-Weight tee', 'Camber', '', 'Camber lists the 301 as its Max-Weight tee.'),
      N('Katharine Hamnett slogan T-shirt', 'Katharine Hamnett', '1980s', 'In the early 1980s Hamnett pioneered outsize T-shirts with large-print slogans.', s=W + 'T-shirt', g='United Kingdom', role='origin'),
      N('Hypercolor T-shirt', 'Global Hypercolour', '1980s', 'Colour-change T-shirt brand that was one of the most popular youth brands in the US and UK.', s=W + 'T-shirt', g='United States')])

kind('Polo shirt',
     'One entry is a polo shirt sold under its own name by its originating brand; colours, sleeve lengths and fits are versions.',
     'the Polo shirt article (Wikipedia, fetched)',
     [K('Polo shirt', 'Lacoste L.12.12', role='origin'), K('Polo shirt', 'Fred Perry M3'), K('Polo shirt', 'Fred Perry M12 twin-tipped'),
      K('Polo shirt', 'Ralph Lauren mesh polo'), K('Polo shirt', 'Sunspel Riviera polo'), K('Polo shirt', 'John Smedley Isis'),
      K('Polo shirt', 'Munsingwear Grand Slam'),
      N('Brooks Brothers button-down polo', 'Brooks Brothers', '1896', 'John Brooks began producing a polo shirt with a button-down collar in 1896, per the Polo shirt article.', s=W + 'Polo_shirt')])

kind('Breton shirt',
     'One entry is a striped marinière sold under its own name by a French maker; weights and stripe widths are versions.',
     'the Breton shirt article (Wikipedia, fetched), which names Saint James, Armor Lux and Orcival; Le Minor and Petit Bateau come from the brand register',
     [K('Breton shirt', 'Saint James marinière', v=V('Saint James', [('Meridien', '', 'named model in the Saint James marinière range'), ('Minquiers', '', 'named model in the Saint James marinière range'), ('Levant', '', 'named model in the Saint James marinière range'), ('Naval', '', 'named model in the Saint James marinière range')])),
      K('Breton shirt', 'Armor-Lux marinière'),
      K('Breton shirt', 'Orcival marinière', v=V('Orcival', [('Rachel', '', 'named model in the Orcival range'), ('Heavy weight cotton', '', 'Orcival cloth weight'), ('Medium weight cotton', '', 'Orcival cloth weight')])),
      K('Breton shirt', 'Le Minor marinière'), K('Breton shirt', 'Petit Bateau marinière')])

kind('Tank top',
     'One entry is a sleeveless top sold under its own name by its brand; colours and sizes are versions.',
     'the brand register; the Tank top article on Wikipedia is a disambiguation page and names no maker',
     [K('Tank top', 'Bonds Chesty singlet', v=V('Bonds', [('Chesty Organics', '', 'organic-cotton version listed by the brand')])),
      K('Tank top', 'Lululemon Align tank'),
      N('Hanes Cotton Tank', 'Hanes', '', 'Cotton tank named in the Hanes entry of the brand register.', v=V('Hanes', [('Cotton Muscle Tank', '', 'cut-off sleeve version'), ('Essentials Cotton Tank Top', '', 'basics version')]))])

kind('Bodysuit',
     'One entry is a bodysuit sold or designed under a named brand or designer; colours and sizes are versions.',
     'the Bodysuit article (Wikipedia, fetched), which names Claire McCardell, Azzedine Alaïa and Donna Karan',
     [K('Bodysuit', 'Donna Karan bodysuit'),
      N('Claire McCardell bodysuit', 'Claire McCardell', '1950s', 'The Bodysuit article says it was presented in the United States after 1950 by designer Claire McCardell.', s=W + 'Bodysuit', g='United States', role='origin'),
      N('Alaïa bodysuit', 'Azzedine Alaïa', '1980s', 'The Bodysuit article says Azzedine Alaïa and Donna Karan helped make the bodysuit a fashion item in the 1980s.', s=W + 'Bodysuit')])

kind('Baby bodysuit',
     'One entry is a baby bodysuit sold under its own name by its brand.',
     'the brand register',
     [K('Baby bodysuit', 'Gerber Onesies')])

kind('Football shirt',
     'One entry is a football shirt template or named kit sold under a maker\'s name; seasons and club versions are versions.',
     'the Football kit article (Wikipedia, fetched), which names Adidas, Puma, Umbro, Hummel and Kappa; adidas templates are carried over from the earlier pass',
     [K('Football shirt', 'adidas Equipment'), K('Football shirt', 'adidas Ascend'), K('Football shirt', 'adidas Horizon'),
      K('Football shirt', 'Hummel halved shirt (Denmark 1986)', role='landmark'),
      N('Kappa skin-tight Italy shirt', 'Kappa', '', 'Skin-tight shirts designed for the Italian national team by Kappa were highly successful, per the Football kit article.', s=W + 'Football_kit', g='Italy'),
      N('Umbro Tottenham 1991 FA Cup Final shirt', 'Umbro', '1991', 'Designed by Umbro, who had just signed a contract with Tottenham mid-season.', s=W + 'Football_kit', g='United Kingdom'),
      N('Puma Cameroon one-piece kit', 'Puma', '2002', 'Puma later supplied Cameroon with one-piece singlet-style tops after the sleeveless kit was ruled illegal.', s=W + 'Football_kit', g='Germany')])

kind('Rugby shirt',
     'One entry is a rugby shirt sold under its own name by its brand; teams and seasons are versions.',
     'the brand register',
     [K('Rugby shirt', 'Canterbury rugby jersey', v=V('Canterbury of New Zealand', [('Uglies', '', 'Canterbury line named in the brand register'), ('Harlequin', '', 'Canterbury line named in the brand register')])),
      K('Rugby shirt', 'Barbarian heavyweight rugby shirt'), K('Rugby shirt', 'Polo Ralph Lauren Iconic Rugby')])

kind('Basketball jersey',
     'One entry is a basketball jersey line sold under its maker\'s name; teams and eras are versions.',
     'the earlier pass sources, kept; no Wikipedia list names further originators',
     [K('Basketball jersey', 'Hardwood Classics', v=V('Mitchell & Ness', [('Authentic Throwback', '', 'on-court replica version of the Hardwood Classics jersey')])), K('Basketball jersey', 'Sleeved NBA jersey')])

kind('Ice-hockey jersey',
     'One entry is an ice-hockey jersey line sold under its maker\'s name; teams and eras are versions.',
     'the earlier pass sources, kept',
     [K('Ice-hockey jersey', 'Reebok Edge jersey'),
      K('Ice-hockey jersey', 'adidas NHL jersey', v=[{'n': 'Reverse Retro', 'mk': 'adidas', 'y': '', 'd': 'alternate-jersey programme'}])])

kind('Baseball jersey',
     'One entry is a baseball jersey line sold under its maker\'s name; teams and eras are versions.',
     'the earlier pass sources, kept',
     [K('Baseball jersey', 'Mitchell & Ness wool-flannel throwback'), K('Baseball jersey', 'Nike-designed MLB jersey')])

kind('Cricket shirt',
     'One entry is a cricket shirt sold under its own name by its brand.',
     'the brand register, which names no cricket shirt', [])

kind('Team jersey',
     'One entry is a licensed fan jersey line sold under its maker\'s name.',
     'the brand register',
     [N('Fanatics Breakaway jersey', 'Fanatics', '', 'Breakaway is the licensed fan jersey line named in the Fanatics entry of the brand register.')])

kind('Dress shirt',
     'One entry is a dress shirt sold under its own name by its brand or shirtmaker; collars, cuffs and fabrics are versions.',
     'the Dress shirt article (Wikipedia, fetched), which names Brooks Brothers and Turnbull & Asser; Charvet and Hilditch & Key come from the brand register',
     [K('Dress shirt', 'Charvet shirt'),
      K('Dress shirt', 'Turnbull & Asser shirt', v=V('Turnbull & Asser', [('Portofino cuff', '', 'cocktail cuff first made by Turnbull & Asser, per the Dress shirt article')])),
      K('Dress shirt', 'Hilditch & Key shirt'),
      N('Brooks Brothers Non-Iron dress shirt', 'Brooks Brothers', '1953', 'Wrinkle-free shirts were first introduced by Brooks Brothers in 1953, per the Dress shirt article.', s=W + 'Dress_shirt', role='origin')])

kind('Button-up shirt',
     'One entry is a casual button-up shirt sold under its own name by its brand; fabrics and collars are versions.',
     'the brand register, confirmed on each brand\'s page; no Wikipedia list of button-up shirts was fetched',
     [K('Button-up shirt', 'Oxford cloth button-down (OCBD)', mk='Brooks Brothers'), K('Button-up shirt', 'Ben Sherman button-down'),
      K('Button-up shirt', 'Kamakura Vintage Ivy'), K('Button-up shirt', 'Pendleton Board Shirt'), K('Button-up shirt', 'Seditionaries Anarchy shirt'),
      N('Gant Oxford cloth button-down', 'Gant', '', 'Gant\'s Oxford cloth button-down is the signature piece named in its register entry.', g='United States')])

kind('Overshirt',
     'One entry is an overshirt sold under its own name by its brand.',
     'the brand register',
     [K('Overshirt', 'CPO shirt', mk="Buzz Rickson's"), K('Overshirt', 'Swanndri bush shirt'), K('Overshirt', 'Pendleton 49er')])

kind('Western shirt',
     'One entry is a Western shirt sold under its own name by its brand; snaps, yokes and fabrics are versions.',
     'the Western wear article (Wikipedia, fetched), which names Rockmount Ranch Wear, H Bar C, Levi\'s and Wrangler',
     [K('Western shirt', 'Rockmount sawtooth snap shirt', role='origin'), K('Western shirt', 'H Bar C Denver shirt'),
      K('Western shirt', "Levi's Western shirt"), K('Western shirt', 'Wrangler snap shirt')])

kind('Aloha shirt',
     'One entry is an aloha shirt sold under its own name by a Hawaiian or Hawaii-linked maker; prints and years are versions.',
     'the Aloha shirt article (Wikipedia, fetched), which names Musa-Shiya, King-Smith, Kamehameha, Branfleet (Kahala), Shaheen, Tori Richard and Spooner\'s of Waikiki (Reyn Spooner); the rest come from the brand register',
     [K('Aloha shirt', 'Kahala aloha shirt'), K('Aloha shirt', 'Reyn Spooner reverse-print shirt'), K('Aloha shirt', 'Tori Richard East-West print'),
      K('Aloha shirt', 'Sun Surf reproduction'), K('Aloha shirt', 'Sig Zane shirt'),
      N('Musa-Shiya aloha shirt', 'Musa-Shiya the Shirtmaker', '1920s', 'The Honolulu shop under Kōichirō Miyamoto is said to have started making shirts from colourful Japanese prints.', s=W + 'Aloha_shirt', g='United States'),
      N('King-Smith aloha sportswear', 'King-Smith Clothiers and Dry Goods', '1936', 'Ellery Chun\'s company registered "aloha sportswear" as a trademark in 1936, though the article calls his invention claim a myth.', s=W + 'Aloha_shirt', g='United States'),
      N('Kamehameha aloha shirt', 'Kamehameha', '1936', 'Named with Branfleet as one of two notable manufacturers founded in 1936.', s=W + 'Aloha_shirt', g='United States'),
      N('Shaheen aloha shirt', 'Shaheen', '1948', 'Shaheen began business in 1948 and was a significant manufacturer of aloha shirts.', s=W + 'Aloha_shirt', g='United States')])

kind('Blouse',
     'One entry is a blouse sold under its own name by its brand.',
     'the brand register, which names no blouse as a signature piece', [])

kind('Sweater',
     'One entry is a sweater sold under its own name by its brand; yarns, colours and necklines are versions. Regional traditions have their own kinds.',
     'the brand register; the Sweater article (Wikipedia, fetched) names no maker',
     [K('Sweater', 'Shaggy Dog'), K('Sweater', 'Poor Boy sweater'), K('Sweater', 'Iconic Flag sweater'), K('Sweater', 'John Smedley fine-gauge knit', v=V('John Smedley', [('Dorset', '', 'John Smedley line named in the brand register')]))])

kind('Cardigan',
     'One entry is a cardigan sold under its own name by its brand.',
     'the Cardigan article (Wikipedia, fetched), which names the 7th Earl of Cardigan and Coco Chanel only as namesake and popularizer; the entries come from the brand register',
     [K('Cardigan', 'Westerley'), K('Cardigan', '4-Bar cardigan'), K('Cardigan', 'Letterman cardigan', mk='Dehen 1920')])

kind('Sweater vest',
     'One entry is a sleeveless sweater sold under its own name by its brand.',
     'the brand register, which names no sweater vest', [])

kind('Aran jumper',
     'One entry is an Aran jumper sold by an Aran maker under its own name; stitch patterns and yarns are versions.',
     'the Aran jumper article (Wikipedia, fetched), which names no maker of a jumper (Patons patterns and Ardfinnan yarn are not garments); the makers come from the brand register',
     [N('Aran Sweater Market Aran jumper', 'Aran Sweater Market', '', 'Inis Mór business selling hand- and machine-knit Aran jumpers.', v=V('Aran Sweater Market', [('Dun Aonghasa heavyweight Aran wool sweater', '', 'named style'), ("Inisheer men's traditional merino Aran sweater", '', 'named style')])),
      N('Aran Woollen Mills Aran jumper', 'Aran Woollen Mills', '1965', 'Westport maker established as Carraig Donn Manufacturing by the Hughes family.', v=V('Aran Woollen Mills', [('Carraig Donn Aran', '', 'trading name')])),
      N('Inis Meáin Aran jumper', 'Inis Meáin', '', 'Knitwear maker on Inis Meáin selling the traditional Aran fisherman\'s jumper.'),
      N('Inverallan hand-knit Aran jumper', 'Inverallan', '', 'Hand-knit Aran fisherman\'s jumper listed in the brand register.')])

kind('Guernsey (gansey)',
     'One entry is a guernsey or gansey sold under its own name by a maker in the Channel Islands or on the Yorkshire coast; patterns are versions.',
     'the Guernsey article (Wikipedia, fetched), which names no maker; the makers come from the brand register',
     [N('Le Tricoteur guernsey', 'Le Tricoteur', '', 'Guernsey maker of the traditional guernsey.', v=V('Le Tricoteur', [('Rocquaine striped guernsey', '', 'striped style')])),
      N('Guernsey Woollens traditional jumper', 'Guernsey Woollens', '', 'Guernsey maker of the traditional guernsey.'),
      N('Flamborough Marine gansey', 'Flamborough Marine', '', 'Maker of the Yorkshire coast gansey.', v=V('Flamborough Marine', [('Filey gansey', '', 'Yorkshire coast pattern'), ('Humber Keel', '', 'Yorkshire coast pattern')]))])

kind('Fair Isle jumper',
     'One entry is a Fair Isle jumper sold under its own name by a maker; patterns and yarns are versions.',
     'the Fair Isle article (Wikipedia, fetched), which names no maker (the Prince of Wales is named only as a wearer in 1921); the makers come from the brand register',
     [N("Jamieson's of Shetland Fair Isle jumper", "Jamieson's of Shetland", '', 'Shetland maker of the Fair Isle allover jumper.', v=V("Jamieson's of Shetland", [('Crew neck saddle shoulder sweater', '', 'named style')])),
      N('Harley of Scotland Fair Isle jumper', 'Harley of Scotland', '', 'Maker of the Fair Isle allover jumper.'),
      N('Mati Ventrillon Fair Isle jumper', 'Mati Ventrillon', '', 'Designer-maker of the Fair Isle allover jumper.')])

kind('Lopapeysa',
     'One entry is a lopapeysa or yoke sweater sold under its maker\'s name; yoke patterns are versions.',
     'the Lopapeysa article (Wikipedia, fetched), which names Annichen Sibbern; the makers come from the brand register',
     [N('Sibbern yoke-sweater pattern', 'Annichen Sibbern', '1930', 'Norwegian designer Annichen Sibbern published the design in the women\'s magazine URD in 1930, per the Lopapeysa article.', s=W + 'Lopapeysa', g='Norway', role='origin'),
      N('Handknitting Association of Iceland lopapeysa', 'Handknitting Association of Iceland', '', 'Hand-knit lopapeysa yoke sweater.'),
      N('Icewear lopapeysa', 'Icewear', '', 'Machine-made lopapeysa yoke sweater.'),
      N('Farmers Market lopapeysa', 'Farmers Market', '', 'Lopapeysa yoke sweater from the Reykjavik label.')])

kind('Norwegian sweater',
     'One entry is a Norwegian patterned sweater or cardigan sold under its maker\'s name; colourways are versions.',
     'the brand register',
     [K('Norwegian sweater', 'Setesdal sweater (lusekofte)', mk='Rauma'), K('Norwegian sweater', 'Marius sweater', mk='Rauma'),
      K('Norwegian sweater', 'Cortina 1956'), K('Norwegian sweater', 'Fana sweater (fanakofte)', mk='Rauma')])

kind('Cowichan sweater',
     'One entry is a Cowichan-style sweater or cardigan sold by a maker or retailer under its own name; the hand-knit Cowichan original is described in the kind.',
     'the Cowichan sweater article (Wikipedia, fetched), which names Mary Maxim, Pendleton, Ralph Lauren, Aritzia and Hudson\'s Bay; Granted and Kanata come from the brand register',
     [N('Mary Maxim Cowichan-style sweater', 'Mary Maxim', '1940s', 'Founded by Willard McPhedrain, who made imitation Cowichan sweaters after seeing one on a sales trip to British Columbia.', s=W + 'Cowichan_sweater', g='Canada'),
      N('Granted Sweater Company Cowichan-style cardigan', 'Granted Sweater Company', '', 'Cowichan-style shawl-collar cardigan.'),
      N('Kanata Cowichan-style cardigan', 'Kanata', '', 'Cowichan-style shawl-collar cardigan.'),
      N('Pendleton Cowichan-style sweater', 'Pendleton Woolen Mills', '', 'Pendleton sells its own version of the Cowichan design.', s=W + 'Cowichan_sweater'),
      N('Ralph Lauren Cowichan-style sweater', 'Ralph Lauren', '', 'Ralph Lauren sells its own version of the Cowichan design.', s=W + 'Cowichan_sweater'),
      N('Aritzia Cowichan-style sweater', 'Aritzia', '', 'Aritzia sells its own version of the Cowichan design.', s=W + 'Cowichan_sweater'),
      N("Hudson's Bay 2010 Olympic sweater", "Hudson's Bay Company", '2009', 'Clothing line for the 2010 Vancouver Winter Olympics that included a sweater resembling a Cowichan design.', s=W + 'Cowichan_sweater', g='Canada')])

kind('Hoodie',
     'One entry is a hooded sweatshirt sold under its own name by its brand; fabric weights and colours are versions.',
     'the Hoodie article (Wikipedia, fetched), which names Champion, Burberry and Adrian Nyman; the others come from the brand register',
     [K('Hoodie', 'Champion Reverse Weave hoodie', role='origin'), K('Hoodie', 'Supreme Box Logo hoodie'), K('Hoodie', 'BAPE Shark hoodie'),
      K('Hoodie', 'Nike Tech Fleece hoodie'), K('Hoodie', 'Russell Athletic Dri-Power hoodie'), K('Hoodie', 'Camber 232 heavyweight hoodie'),
      K('Hoodie', 'Loopwheel hoodie', v=V('Loopwheeler', [('LW Basic', '', 'Loopwheeler line'), ('LW Light', '', 'Loopwheeler line'), ('LW Midweight', '', 'Loopwheeler line')])),
      N('Champion Powerblend hoodie', 'Champion', '', 'Powerblend is a named Champion fleece line in the brand register.'),
      N('Hanes EcoSmart hoodie', 'Hanes', '', 'EcoSmart is a named Hanes fleece line in the brand register.'),
      N('Gildan Heavy Blend hoodie', 'Gildan', '', 'Heavy Blend is a named Gildan fleece line in the brand register.'),
      N('Carhartt Marquette full-zip sweatshirt', 'Carhartt', '', 'Marquette is a named Carhartt line in the brand register.'),
      N('Vollebak 100 Year Hoodie', 'Vollebak', '', 'Named hoodie in the Vollebak entry of the brand register.'),
      N('Vollebak Relaxation Hoodie', 'Vollebak', '', 'Named hoodie in the Vollebak entry of the brand register.'),
      N('Damien Hirst Butterfly Hoodie for Adrian Nyman', 'Adrian Nyman', '2008', 'Butterfly Hoodie by Damien Hirst for Adrian Nyman, per the Hoodie article.', s=W + 'Hoodie', g='United Kingdom')])

kind('Sweatshirt',
     'One entry is a crew-neck sweatshirt sold under its own name by its brand; fabric weights and colours are versions.',
     'the Sweatshirt article (Wikipedia, fetched), which names Russell Athletic; the others come from the brand register',
     [K('Sweatshirt', 'Russell crew sweatshirt', role='origin'), K('Sweatshirt', 'Champion Reverse Weave crewneck'),
      K('Sweatshirt', 'Loopwheel sweatshirt'), K('Sweatshirt', 'Camber 234 heavyweight crewneck'),
      N("Buzz Rickson's loopwheel sweatshirt", "Buzz Rickson's", '', 'Japanese military-reproduction maker\'s loop-wheeled sweatshirt.'),
      N('Hanes EcoSmart sweatshirt', 'Hanes', '', 'EcoSmart is a named Hanes fleece line in the brand register.'),
      N('Carhartt K288 sweatshirt', 'Carhartt', '', 'K288 is the logo sweatshirt named in the Carhartt entry of the brand register.')])

# ---------------------------------------------------------------- TROUSERS
kind('Heritage American jeans',
     'One entry is a jean pattern sold under its own name by its originating American brand; washes and sizes are versions.',
     'the Jeans article (Wikipedia, fetched), which names Levi Strauss, Jacob Davis, the 501, 505 and 517; Lee and Wrangler come from the brand register',
     [K('Heritage American jeans', "Levi's 501", role='origin', v=[{'n': "Levi's Vintage Clothing", 'mk': "Levi's", 'y': '', 'd': 'reproduction line of the brand'}]),
      K('Heritage American jeans', "Levi's 505"), K('Heritage American jeans', "Levi's 517 Bootcut"),
      K('Heritage American jeans', "Levi's 511 Slim"), K('Heritage American jeans', "Levi's 550 Relaxed"),
      K('Heritage American jeans', 'Lee 101 Riders'), K('Heritage American jeans', 'Wrangler 13MWZ Cowboy Cut')])

sel_ex = [K('Selvedge reproduction jeans', n) for n in ['Warehouse Lot 1001XX', 'Sugar Cane 1947', 'Full Count 1101', 'TCB 50s', "Studio D'Artisan SD-101", 'Iron Heart IH-634', 'Samurai S710XX', 'The Flat Head 3000 series', 'Pure Blue Japan XX-013', 'Momotaro Standard Collection', 'Japan Blue J301', 'Evisu Lot 2000 No. 2']]


def addv(entries, name, items):
    for e in entries:
        if e['n'] == name:
            e.setdefault('v', []).extend(V(e['mk'], items))
            return
    raise KeyError(name)


addv(sel_ex, 'Warehouse Lot 1001XX', [('Lot 800', '', 'Warehouse & Co. lot'), ('Lot 900', '', 'Warehouse & Co. lot'), ('Duck Digger', '', 'Warehouse & Co. line')])
addv(sel_ex, 'Sugar Cane 1947', [('1966', '', 'Sugar Cane model'), ('Hawaii', '', 'Sugar Cane line')])
addv(sel_ex, 'Full Count 1101', [('0105', '', 'Full Count model'), ('1108', '', 'Full Count model')])
addv(sel_ex, 'TCB 50s', [('20s', '', 'TCB era model'), ('40s', '', 'TCB era model'), ('60s', '', 'TCB era model')])
addv(sel_ex, "Studio D'Artisan SD-101", [('SD series', '', 'range'), ('D-01', '', "Studio D'Artisan model")])
addv(sel_ex, 'Iron Heart IH-634', [('IH-666', '', 'Iron Heart model'), ('IH-888', '', 'Iron Heart model')])
addv(sel_ex, 'Samurai S710XX', [('S510', '', 'Samurai model'), ('S5000', '', 'Samurai model')])
addv(sel_ex, 'The Flat Head 3000 series', [('8004', '', 'The Flat Head model')])
addv(sel_ex, 'Pure Blue Japan XX-013', [('XX series', '', 'range')])
addv(sel_ex, 'Momotaro Standard Collection', [('Classic Collection', '', 'Momotaro collection')])
addv(sel_ex, 'Japan Blue J301', [('J series', '', 'range'), ('Circle Line', '', 'Japan Blue line')])
kind('Selvedge reproduction jeans',
     'One entry is a reproduction jean pattern sold under its own name by a Japanese or American maker; lots, years and denim weights are versions.',
     'the brand register, confirmed on each brand\'s page; no Wikipedia list of reproduction jeans was fetched',
     sel_ex + [N('Edwin 503', 'Edwin', '', 'Edwin 503 is the jean named in the Edwin entry of the brand register.'),
               N('Big John RARE', 'Big John', '', 'RARE is the jean line named in the Big John entry of the brand register.'),
               N('Rogue Territory Stanton jeans', 'Rogue Territory', '', 'Stanton is the jean named in the Rogue Territory entry of the brand register.')])

kind('Fashion & designer jeans',
     'One entry is a jean fit or line sold under its own name by a fashion or designer label; washes and sizes are versions.',
     'the brand register, confirmed on each brand\'s page',
     [K('Fashion & designer jeans', 'A.P.C. Petit Standard', v=V('A.P.C.', [('New Standard', '', 'A.P.C. fit'), ('Petit New Standard', '', 'A.P.C. fit')])),
      K('Fashion & designer jeans', 'Nudie Jeans named fits'), K('Fashion & designer jeans', 'JNCO wide-leg', v=V('JNCO', [('Cannon series', '', 'JNCO series')])),
      N('Diesel named fits', 'Diesel', '', 'Diesel names its fits Larkee, Sleenker and D-Strukt.', v=V('Diesel', [('Larkee', '', 'Diesel fit; the 1985 Larkee is an earlier cut'), ('Sleenker', '', 'Diesel fit'), ('D-Strukt', '', 'Diesel fit')])),
      N('True Religion Ricky', 'True Religion', '', 'Ricky and Billy are the named cuts in the True Religion entry of the brand register.', v=V('True Religion', [('Billy', '', 'True Religion cut')]))])

kind('Trousers',
     'One entry is a trouser pattern sold under its own name by its brand; fabrics and fits are versions.',
     'the brand register, confirmed on each brand\'s page',
     [K('Trousers', 'DAKS self-supporting trouser'), K('Trousers', "Levi's Sta-Prest"), K('Trousers', 'Bernard Zins French-cut trouser', v=V('Bernard Zins', [('BAC', '', 'Bernard Zins line'), ('BZ V2', '', 'Bernard Zins line')])),
      N('Carhartt B01 Double-Front Work Pant', 'Carhartt', '', 'Work trouser named in the Carhartt entry of the brand register.'),
      N('Dickies 874 Original Work Pant', 'Dickies', '', 'Work trouser named in the Dickies entry of the brand register.', v=V('Dickies', [('873', '', 'Dickies slim-cut work pant')])),
      N('Red Kap Dura-Kap Industrial Pant', 'Red Kap', '', 'Work trouser named in the Red Kap entry of the brand register.'),
      N('Stan Ray OG Painter Pant', 'Stan Ray', '', 'Painter pant named in the Stan Ray entry of the brand register.', v=V('Stan Ray', [('80s Painter Pant', '', 'Stan Ray cut'), ('Big Job Painter Pant', '', 'Stan Ray cut'), ('Fatigue Pant', '', 'Stan Ray cut')])),
      N('Stan Ray OG-107 fatigue trouser', 'Stan Ray', '', 'OG-107 fatigue trouser named in the Stan Ray entry of the brand register.'),
      N('Pike Brothers OG-107 fatigue trouser', 'Pike Brothers', '', 'OG-107 fatigue trouser named in the Pike Brothers entry of the brand register.', v=V('Pike Brothers', [('1962 OG-107 Pant', '', 'Pike Brothers reproduction')])),
      N('Age of Glory Service Pant', 'Age of Glory', '', 'Work-inspired French motorcycle-wear trouser.')])

kind('Chinos',
     'One entry is a chino sold under its own name by its brand; fits and washes are versions.',
     'the Chino cloth article (Wikipedia, fetched), which names no maker; the chinos come from the brand register',
     [K('Chinos', 'Dockers Original Chino', v=V('Dockers', [('Alpha Chino', '', 'Dockers chino')])),
      K('Chinos', 'Bonobos chino', v=V('Bonobos', [('The Original Chino', '', 'Bonobos fit'), ('Washed Chino', '', 'Bonobos fit')])),
      N('Bills Khakis Military khaki chino', 'Bills Khakis', '', 'Military khaki chino named in the Bills Khakis entry of the brand register.', v=V('Bills Khakis', [('M1', '', 'Bills Khakis cut'), ('M2', '', 'Bills Khakis cut')]))])

kind('Cargo trousers',
     'One entry is a cargo trouser sold under its own name by its brand.',
     'the Cargo pants article (Wikipedia, fetched), which names no maker (it credits British battle dress of 1938 and the US paratrooper uniform); the entries come from the brand register',
     [K('Cargo trousers', 'Carhartt cargo work trouser'), K('Cargo trousers', 'Craghoppers Kiwi', v=V('Craghoppers', [('NosiLife', '', 'insect-repellent Craghoppers range')]))])

kind('Harem pants', 'One entry is a harem trouser sold under its own name by its brand.', 'the brand register, which names none', [])

kind('Capri pants',
     'One entry is a capri trouser designed or sold under a named designer or brand.',
     'the Capri pants article (Wikipedia, fetched), which names Sonja de Lennart',
     [N('Sonja de Lennart capri pants', 'Sonja de Lennart', '1948', 'Capri pants were introduced by designer Sonja de Lennart in 1948.', s=W + 'Capri_pants', role='origin')])

kind('Plus fours & breeks', 'One entry is a pair of plus fours or breeks sold under its own name by its brand.', 'the brand register, which names none', [])

kind('Bondage trousers',
     'One entry is a bondage trouser sold under its own name by its maker.',
     'the brand register',
     [K('Bondage trousers', 'Seditionaries bondage trousers', mk='Vivienne Westwood')])

kind('Shorts',
     'One entry is a pair of shorts sold under its own name by its brand; lengths and fabrics are versions.',
     'the Shorts article (Wikipedia, fetched), which names Quiksilver, Billabong, Rip Curl, Jacob Golomb of Everlast and Dolfin; Baggies and Stubbies come from the brand register',
     [K('Shorts', 'Patagonia Baggies'), K('Shorts', 'Stubbies'), K('Shorts', 'Dolphin shorts', mk='Dolfin'),
      N('Quiksilver boardshort', 'Quiksilver', '1970', 'Quiksilver offered a highly successful boardshort design in 1970.', s=W + 'Shorts', g='Australia'),
      N('Birdwell Beach Britches', 'Birdwell', '', 'Surf boardshort named in the Birdwell entry of the brand register.', v=V('Birdwell', [('Surfnyl boardshorts', '', 'Birdwell line'), ('Surfstretch boardshorts', '', 'Birdwell line'), ('Walkshorts', '', 'Birdwell line')])),
      N('Everlast boxing trunks', 'Everlast', '1925', 'Jacob Golomb introduced the boxing-style trunks in 1925 as an alternative to leather-belted trunks.', s=W + 'Shorts', g='United States'),
      N('Billabong boardshort', 'Billabong', '', 'Named with Rip Curl as a leading boardshort maker in the Shorts article.', s=W + 'Shorts', g='Australia'),
      N('Rip Curl boardshort', 'Rip Curl', '', 'Named with Billabong as a leading boardshort maker in the Shorts article.', s=W + 'Shorts', g='Australia')])

kind('Bermuda shorts',
     'One entry is a pair of Bermuda shorts made under a named maker; the Bermudian original is described in the kind.',
     'the Bermuda shorts article (Wikipedia, fetched), which names Nathaniel Coxon, Trimingham Bros. and H.A. & E. Smiths',
     [N('Coxon hemmed uniform shorts', 'Nathaniel Coxon', '1914', 'The Bermudian tea shop owner hemmed his employees\' uniform pants, credited as the invention of Bermuda shorts.', s=W + 'Bermuda_shorts', g='Bermuda', role='origin'),
      N('Trimingham Bros. Bermuda shorts', 'Trimingham Bros.', '', 'Improved the design of the shorts after the war and used brightly coloured materials.', s=W + 'Bermuda_shorts', g='Bermuda'),
      N('H.A. & E. Smiths Bermuda shorts', 'H.A. & E. Smiths', '', 'Improved the design of the shorts after the war.', s=W + 'Bermuda_shorts', g='Bermuda')])

kind('Denim shorts & cut-offs', 'One entry is a pair of denim shorts sold under its own name by its brand.', 'the brand register, which names none', [])

kind('Hot pants',
     'One entry is a hot pants design credited to a named maker.',
     'the Hot pants article (Wikipedia, fetched), which names Krizia and Dorothée Bis',
     [N('Krizia hot pants', 'Krizia', '1970', 'Krizia (Mariuccia Mandelli) is credited with designing the first hot pants in 1970.', s=W + 'Hot_pants', g='Italy', role='origin'),
      N('Dorothée Bis hot pants', 'Dorothée Bis', '1970', 'Women\'s Wear Daily coined the term for fashions by the French ready-to-wear company Dorothée Bis.', s=W + 'Hot_pants', g='France')])

kind('Joggers',
     'One entry is a jogger or sweatpant sold under its own name by its brand; fabrics and fits are versions.',
     'the brand register',
     [K('Joggers', 'Nike Tech Fleece jogger'),
      N('Champion grey jersey sweatpant', 'Champion', '', 'Grey jersey sweatpant named in the Champion entry of the brand register.'),
      N('Russell Athletic grey jersey sweatpant', 'Russell Athletic', '', 'Grey jersey sweatpant named in the Russell Athletic entry of the brand register.')])

kind('Leggings',
     'One entry is a legging sold under its own name by its brand; lengths and fabrics are versions.',
     'the Leggings article (Wikipedia, fetched), which names Sanko Group and Marni; the others come from the brand register',
     [K('Leggings', 'Lululemon Align'), K('Leggings', 'Disco Pant'), K('Leggings', 'Uniqlo Heattech leggings'),
      N('Uniqlo Ultra Stretch leggings', 'Uniqlo', '', 'Ultra Stretch is a named Uniqlo line in the brand register.'),
      N('Jeggings', 'Sanko Group', '', 'Jeggings is a registered brand name of Sanko Group for leggings styled like tight denim jeans.', s=W + 'Leggings', g='Turkey'),
      N('Marni men\'s leggings', 'Marni', '2007', 'Marni showed leggings designed solely for men in its Fall 2007 menswear show.', s=W + 'Leggings', g='Italy')])

# ---------------------------------------------------------------- DRESSES
kind('Wrap dress',
     'One entry is a wrap dress designed by a named maker or house; fabrics and lengths are versions.',
     'the Wrap dress article (Wikipedia, fetched), which names Elsa Schiaparelli, Claire McCardell, Charles James and Diane von Fürstenberg',
     [K('Wrap dress', 'DvF wrap dress'), K('Wrap dress', 'Popover dress'), K('Wrap dress', 'Taxi dress'),
      N('Schiaparelli wrap dress', 'Schiaparelli', '1930s', 'Wrap dresses were designed by Elsa Schiaparelli in the 1930s.', s=W + 'Wrap_dress', role='origin')])

kind('Slip dress',
     'One entry is a slip dress sold under a named designer or house; fabrics and lengths are versions.',
     'the Slip dress article (Wikipedia, fetched), which names John Galliano for Dior, Calvin Klein and Narciso Rodriguez; it names no originator',
     [K('Slip dress', 'Galliano Dior slip dress'),
      N('Calvin Klein 1990s minimalist slip dress', 'Calvin Klein', '1990s', 'Named in the Slip dress article among designers associated with slip dresses.', s=W + 'Slip_dress'),
      N('Narciso Rodriguez slip dress', 'Narciso Rodriguez', '', 'Named in the Slip dress article among designers associated with slip dresses.', s=W + 'Slip_dress', g='United States')])

kind('Sheath & bodycon dress',
     'One entry is a sheath or bodycon dress sold under a named designer or brand; fabrics and lengths are versions.',
     'the Little black dress article (Wikipedia, fetched), which names Chanel, Givenchy and Dior; the others come from the brand register',
     [K('Sheath & bodycon dress', 'Little black dress', role='origin', mk='Chanel'),
      N('Givenchy little black dress', 'Givenchy', '1961', 'Hubert de Givenchy\'s black dress for Audrey Hepburn in Breakfast at Tiffany\'s set the standard for little black dresses.', s=W + 'Little_black_dress', role='landmark'),
      K('Sheath & bodycon dress', 'Bandage dress'),
      N('Alaïa bandage dress', 'Azzedine Alaïa', '', 'Bandage dress named in the Azzedine Alaïa entry of the brand register.'),
      K('Sheath & bodycon dress', 'Latex dress'),
      N('Collectif 1950s wiggle dress', 'Collectif', '', '1950s-style wiggle dress.', v=V('Collectif', [('Dolores doll dress', '', 'Collectif wiggle style')])),
      N('Pinup Girl Clothing 1950s wiggle dress', 'Pinup Girl Clothing', '', '1950s-style wiggle dress.', v=V('Pinup Girl Clothing', [('Malia 1940s gathered wiggle dress', '', 'Pinup Girl Clothing style')]))])

kind('Shift & A-line dress',
     'One entry is a shift or A-line dress designed or sold under a named designer or brand; colours and prints are versions.',
     'the brand register, confirmed on each brand\'s page',
     [K('Shift & A-line dress', n) for n in ['Dior A-line', 'YSL Trapeze dress', 'Mary Quant minidress', 'Mondrian dress', 'Lilly shift', 'Courrèges Space Age mini']])

kind('Shirt dress',
     'One entry is a shirt dress sold under a named designer or brand.',
     'the brand register',
     [K('Shirt dress', 'Halston Ultrasuede shirtdress')])

kind('Babydoll & smock dress',
     'One entry is a babydoll or smock dress sold under a named designer or brand.',
     'the brand register',
     [K('Babydoll & smock dress', 'Batsheva smock dress'), K('Babydoll & smock dress', 'Molly Goddard tulle dress')])

kind('Pinafore dress',
     'One entry is a pinafore or jumper-skirt dress sold under its own name by its brand.',
     'the brand register, in which four Lolita brands list a JSK (jumperskirt)',
     [N('Angelic Pretty JSK', 'Angelic Pretty', '', 'Harajuku sweet Lolita brand founded 1979; the register lists its JSK.'),
      N('Baby, the Stars Shine Bright JSK', 'Baby, the Stars Shine Bright', '', 'Lolita brand; the register lists its JSK.'),
      N('Innocent World JSK', 'Innocent World', '', 'Lolita brand; the register lists its JSK.'),
      N('Victorian Maiden JSK', 'Victorian Maiden', '', 'Lolita brand; the register lists its JSK.')])

kind('Fit-and-flare & swing dress',
     'One entry is a fit-and-flare or swing dress sold under a named designer or brand; prints and sizes are versions.',
     'the brand register, confirmed on each brand\'s page',
     [K('Fit-and-flare & swing dress', 'Dior New Look dress', v=V('Christian Dior', [('New Look shirtdress', '1947', 'Dior New Look variant'), ('New Look ball gown', '1947', 'Dior New Look variant'), ('New Look cocktail dress', '1947', 'Dior New Look variant')])),
      N('Collectif 1950s swing dress', 'Collectif', '', '1950s-style swing dress.', v=V('Collectif', [('Nikita dress', '', 'Collectif swing style'), ('Sally swing dress', '', 'Collectif swing style'), ('Wanda swing dress', '', 'Collectif swing style')])),
      N('Pinup Girl Clothing 1950s swing dress', 'Pinup Girl Clothing', '', '1950s-style swing dress.', v=V('Pinup Girl Clothing', [('Amalie ballerina swing dress', '', 'Pinup Girl Clothing style')])),
      N('Hell Bunny 1950s swing dress', 'Hell Bunny', '', '1950s-style swing dress.', v=V('Hell Bunny', [('Hell Bunny swing dress', '', 'brand style')]))])

kind('Sundress & tea dress',
     'One entry is a sundress or tea dress sold under a named designer or brand.',
     'the brand register',
     [N('Lilly Pulitzer 1950s sundress', 'Lilly Pulitzer', '1950s', '1950s sundress named in the Lilly Pulitzer entry of the brand register.'),
      N('Reformation 1950s sundress', 'Reformation', '', '1950s-style sundress named in the Reformation entry of the brand register.')])

kind('Maxi dress',
     'One entry is a maxi or prairie dress sold under a named designer or brand.',
     'the brand register, confirmed on each brand\'s page',
     [K('Maxi dress', 'Thea Porter gipsy dress'),
      N('Batsheva prairie dress', 'Batsheva', '', 'Prairie dress named in the Batsheva entry of the brand register.'),
      N('Dôen prairie dress', 'Dôen', '', 'Prairie dress named in the Dôen entry of the brand register.'),
      N('Gunne Sax prairie dress', 'Gunne Sax', '', 'Prairie dress named in the Gunne Sax entry of the brand register.'),
      N('Laura Ashley prairie dress', 'Laura Ashley', '', 'Prairie dress named in the Laura Ashley entry of the brand register.')])

kind('Evening gown & cocktail dress',
     'One entry is an evening gown or cocktail dress designed by a named house or designer; collections are versions.',
     'the brand register, confirmed on each brand\'s page',
     [K('Evening gown & cocktail dress', 'Lobster dress'), K('Evening gown & cocktail dress', 'Versace safety-pin dress'),
      N('Bazza Alzouman Signature Balloon Sleeve Gown', 'Bazza Alzouman', '', 'Evening gown named in the Bazza Alzouman entry of the brand register.'),
      N('Charles James ball gown', 'Charles James', '', 'Ball gown named in the Charles James entry of the brand register.')])

kind('Wedding dress',
     'One entry is a bridal gown sold under its maker\'s name.',
     'the Wedding dress article (Wikipedia, fetched), which names Eliza Gill and Euphemia Macdonald only as dressmakers who published designs in 1816 and 1818; the bridal houses come from the brand register',
     [N('Pronovias bridal gown', 'Pronovias', '', 'Bridal gown named in the Pronovias entry of the brand register.'),
      N('Vera Wang bridal gown', 'Vera Wang', '', 'Bridal gown named in the Vera Wang entry of the brand register.')])

# ---------------------------------------------------------------- SKIRTS ETC
kind('Pencil skirt',
     'One entry is a pencil skirt designed by a named house.',
     'the Pencil skirt article (Wikipedia, fetched), which names Christian Dior; the hobble skirt is named without a maker',
     [K('Pencil skirt', 'Pencil skirt', mk='Christian Dior', role='origin', d='Christian Dior introduced the classic modern pencil skirt in his 1954 autumn-winter collection.', s=W + 'Pencil_skirt')])

kind('A-line skirt', 'One entry is an A-line skirt sold under its own name by its brand.', 'the brand register, which names none', [])

kind('Circle & poodle skirt',
     'One entry is a circle skirt designed under a named maker.',
     'the Poodle skirt article (Wikipedia, fetched), which names Juli Lynne Charlot',
     [K('Circle & poodle skirt', 'Poodle skirt', mk='Juli Lynne Charlot', role='origin', _g='United States', d='The skirt originated in 1947 in the United States, designed by Juli Lynne Charlot.', s=W + 'Poodle_skirt')])

kind('Pleated skirt', 'One entry is a pleated skirt sold under its own name by its brand.', 'the Miniskirt article (Wikipedia, fetched) mentions the Miu Miu microskirt, filed under Miniskirt; the register names no pleated skirt', [])
kind('Wrap skirt', 'One entry is a wrap skirt sold under its own name by its brand.', 'the brand register, which names none', [])
kind('Tiered & prairie skirt', 'One entry is a tiered or prairie skirt sold under its own name by its brand.', 'the brand register, which names none', [])

kind('Miniskirt',
     'One entry is a miniskirt or short skirt designed or sold under a named designer or house; collections are versions.',
     'the Miniskirt article (Wikipedia, fetched to its end), which names the designers below',
     [K('Miniskirt', 'Miniskirt', mk='Mary Quant', role='origin', d='Mary Quant is credited with the invention of the 1960s miniskirt.', s=W + 'Miniskirt'),
      K('Miniskirt', 'Rah-rah skirt', mk='Norma Kamali', d='The flounced, hip-yoked style debuted by Norma Kamali and Perry Ellis in 1979 was called rah-rah in the UK.', s=W + 'Miniskirt', y='1979'),
      K('Miniskirt', 'Mini-Crini', mk='Vivienne Westwood', y='1985', d='Westwood offered her first mini-crini, an abbreviated Victorian crinoline, in 1985.', s=W + 'Miniskirt'),
      N('Courrèges miniskirt', 'Courrèges', '1964', 'André Courrèges explicitly claimed to have invented the mini and showed above-the-knee skirts in 1964 and 1965.', s=W + 'Miniskirt'),
      N('John Bates miniskirt', 'John Bates', '1965', 'Editor Marit Allen said John Bates was the first to offer fashionable miniskirts.', s=W + 'Miniskirt', g='United Kingdom'),
      N('Biba jersey miniskirt', 'Biba', '1966', 'Barbara Hulanicki\'s stretchy jersey skirts shrank in transit and sold out as ten-inch garments.', s=W + 'Miniskirt', g='United Kingdom'),
      N('Rudi Gernreich miniskirt', 'Rudi Gernreich', '1967', 'Among the first American designers to offer miniskirts.', s=W + 'Miniskirt', g='United States'),
      N('Jacques Tiffeau miniskirt', 'Jacques Tiffeau', '1960s', 'Showed above-the-knee lengths in the US shortly after Courrèges.', s=W + 'Miniskirt', g='United States'),
      N('Pierre Cardin loop-and-strip miniskirt', 'Pierre Cardin', '1967', 'Made loop-and-strip miniskirts from 1967 to 1970.', s=W + 'Miniskirt', g='France'),
      N('Kenzo miniskirt', 'Kenzo', '1976', 'Kenzo reintroduced miniskirts in 1976 and kept showing them from then on.', s=W + 'Miniskirt', g='France'),
      N('Christian Lacroix puffball skirt', 'Christian Lacroix', '1985', 'His puffball skirts were inspired by Westwood\'s mini-crini and were widely copied.', s=W + 'Miniskirt', g='France'),
      N('Alaïa mini and micromini', 'Azzedine Alaïa', '1980s', 'Began presenting mini and micromini versions of his extremely tight dress designs in the mid-1980s.', s=W + 'Miniskirt'),
      N('Emanuel Ungaro miniskirt', 'Emanuel Ungaro', '1987', 'His minis were so brief they were likened to 1950s bathing suits.', s=W + 'Miniskirt', g='France'),
      N('Miu Miu microskirt', 'Miu Miu', '2022', 'Miu Miu debuted a microskirt in Spring/Summer 22, inspired by the schoolgirl pleated skirt.', s=W + 'Miniskirt', g='Italy'),
      N('Diesel belt skirt', 'Diesel', '2022', 'The belt skirt debuted in Diesel\'s FW22 show in Milan, with leather belts made into micro-mini skirts.', s=W + 'Miniskirt')])

kind('Tutu & ballerina skirt',
     'One entry is a tutu designed or made by a named costumier or designer.',
     'the Tutu article (Wikipedia, fetched), which names Hippolyte Lecomte, Eugene Lami, Barbara Karinska, Cecil Beaton, Christian Lacroix and Isaac Mizrahi',
     [N('Lecomte Romantic tutu', 'Hippolyte Lecomte', '1827', 'Designed the basic silhouette of the Romantic tutu for Pauline Montessu in La Somnambule.', s=W + 'Tutu_(clothing)', g='France', role='origin'),
      N('Lami La Sylphide tutu', 'Eugene Lami', '1832', 'Designed the skirt first worn by Marie Taglioni in La Sylphide at the Paris Opera.', s=W + 'Tutu_(clothing)', g='France'),
      N('Karinska tutu', 'Barbara Karinska', '', 'Designed and constructed tutus of extraordinary beauty and durability.', s=W + 'Tutu_(clothing)', g='United States'),
      N('Cecil Beaton tutu', 'Cecil Beaton', '', 'Named in the Tutu article among fashion designers who have designed tutus.', s=W + 'Tutu_(clothing)', g='United Kingdom'),
      N('Christian Lacroix tutu', 'Christian Lacroix', '', 'Named in the Tutu article among fashion designers who have designed tutus.', s=W + 'Tutu_(clothing)', g='France'),
      N('Isaac Mizrahi tutu', 'Isaac Mizrahi', '', 'Named in the Tutu article among fashion designers who have designed tutus.', s=W + 'Tutu_(clothing)', g='United States')])

kind('Culottes & skort', 'One entry is a culotte or skort sold under its own name by its brand.', 'the Culottes article (Wikipedia, fetched), which names no maker', [])

kind('Jumpsuit',
     'One entry is a jumpsuit designed or sold under a named designer or brand; fabrics and colours are versions.',
     'the Jumpsuit article (Wikipedia, fetched), which names Elsa Schiaparelli, Vera Maxwell, Bonnie Cashin and Nicolas Ghesquière; the others come from the brand register',
     [N('Schiaparelli jumpsuit', 'Schiaparelli', '1930s', 'Elsa Schiaparelli began designing jumpsuits for women in the 1930s.', s=W + 'Jumpsuit', role='origin'),
      N('Vera Maxwell jumpsuit', 'Vera Maxwell', '1940s', 'Sporty jumpsuit styles by the American designer Vera Maxwell in the mid-1940s.', s=W + 'Jumpsuit', g='United States'),
      N('Bonnie Cashin evening jumpsuit', 'Bonnie Cashin', '1950s', 'American designers such as Bonnie Cashin started designing evening jumpsuits in the 1950s.', s=W + 'Jumpsuit', g='United States'),
      N('Ghesquière jumpsuit', 'Nicolas Ghesquière', '2002', 'Tried to bring the jumpsuit back in 2002 in different fabrics and patterns.', s=W + 'Jumpsuit', g='France'),
      N('Bridge & Burn Utility jumpsuit', 'Bridge & Burn', '', 'Utility jumpsuit named in the Bridge & Burn entry of the brand register.', v=V('Bridge & Burn', [('Lou jumpsuit', '', 'Bridge & Burn style')])),
      N('Elizabeth Suzann Utility jumpsuit', 'Elizabeth Suzann', '', 'Utility jumpsuit named in the Elizabeth Suzann entry of the brand register.', v=V('Elizabeth Suzann', [('Clyde jumpsuit', '', 'Elizabeth Suzann style')]))])

kind('Co-ord set', 'One entry is a matching set sold under its own name by its brand.', 'the brand register, which names none', [])

kind('Costume',
     'One entry is a costume suit sold under its own name by its brand.',
     'the brand register',
     [K('Costume', 'Morphsuit', mk='Morphsuits', v=V('Morphsuits', [('MorphKids', '', 'children\'s Morphsuits range')]))])
