import json, re, copy, sys
OLD = json.load(open('/home/user/Possession-Taxonomy/rebuild/work/V4_E2_RACKET/bak/E2.json'))
NAMES = ['Racket sports', 'Golf', 'Team sports', 'Target & precision sports', 'Protective gear']
WIKI = 'https://en.wikipedia.org/wiki/'
SRC = {
    'telstar': WIKI + 'Adidas_Telstar', 'adidas': WIKI + 'Adidas', 'wilson': WIKI + 'Wilson_Sporting_Goods',
    'spalding': WIKI + 'Spalding_(company)', 'gilbert': WIKI + 'Gilbert_Rugby', 'provi': WIKI + 'Titleist_Pro_V1',
    'callaway': WIKI + 'Callaway_Golf_Company', 'bertha': 'https://www.golfmagic.com/equipment-news/4-callaway-big-bertha-driver',
    'cameron': 'https://www.parwestgolf.com/blogs/content/scotty-cameron-putters-every-2026-model-explained',
    'scotty': WIKI + 'Scotty_Cameron', 'taylormade': WIKI + 'TaylorMade', 'bauer': WIKI + 'Bauer_Hockey',
    'amer': WIKI + 'Amer_Sports', 'acushnet': WIKI + 'Acushnet_Company', 'nike': WIKI + 'Nike,_Inc.',
    'decathlon': WIKI + 'Decathlon_(retailer)', 'babolat': WIKI + 'Babolat', 'yonex': WIKI + 'Yonex', 'head': WIKI + 'Head_(company)',
}
# maker table: short maker -> (own, tier, cty, own_y)
GG, IND = 'Global group', 'Independent'
MAKER = {
    'Wilson': ('Amer Sports', GG, 'United States', '1989'),
    'Titleist': ('Acushnet Company', GG, 'United States', ''),
    'Scotty Cameron': ('Acushnet Company', GG, 'United States', '2011'),
    'FootJoy': ('Acushnet Company', GG, 'United States', ''),
    'Callaway': ('Topgolf Callaway Brands', GG, 'United States', ''),
    'Odyssey': ('Topgolf Callaway Brands', GG, 'United States', '1997'),
    'TaylorMade': ('Centroid Investment Partners', IND, 'United States', '2022'),
    'Head': ('Head Austria GmbH', IND, 'Austria', ''),
    'Penn': ('Head Austria GmbH', IND, 'United States', ''),
    'Babolat': ('Babolat', IND, 'France', ''),
    'Yonex': ('Yonex', IND, 'Japan', ''),
    'Spalding': ('Fruit of the Loom', IND, 'United States', '2006'),
    'Gilbert': ('Grays International', IND, 'United Kingdom', '2002'),
    'Nike': ('Nike, Inc.', GG, 'United States', ''),
    'adidas': ('Adidas AG', GG, 'Germany', ''),
    'Bauer': ('Peak Achievement Athletics', IND, 'Canada', '2017'),
    'DeMarini': ('Amer Sports', GG, 'United States', ''),
    'Louisville Slugger': ('Amer Sports', GG, 'United States', ''),
}
def short(m):
    m = re.sub(r'\s*\(.*?\)', '', m).strip()
    for suf in (' Golf Company', ' Sporting Goods', ' Golf', ' Hockey', ' Sports', ' Sport'):
        if m.endswith(suf) and m not in ('Tour Edge Golf',):
            m = m[:-len(suf)]
    if m == 'Tour Edge': m = 'Tour Edge'
    if m == 'Ping': m = 'Ping'
    return m
def market(e, mk):
    t = MAKER.get(mk) or MAKER.get(short(mk))
    if t:
        e['own'], e['tier'], e['cty'] = t[0], t[1], t[2]
        if t[3]: e['own_y'] = t[3]

KEEP = {'Tennis string', 'Tennis ball', 'Badminton racket', 'Squash racket', 'Squash ball', 'Table tennis bat', 'Padel racket', 'Padel ball',
        'Pickleball paddle', 'Pickleball ball', 'Golf driver', 'Fairway wood', 'Hybrid', 'Driving iron', 'Golf iron set', 'Golf wedge', 'Putter',
        'Golf ball', 'Rugby ball', 'Cricket ball', 'Cricket bat', 'Baseball bat', 'Softball bat', 'Ice hockey stick', 'Goalie stick',
        'Field hockey stick', 'Lacrosse stick', 'Hurley', 'Pétanque boules', 'Lawn bowls', 'Disc golf disc', 'Airsoft gun', 'Paintball gun',
        'Dartboard', 'Darts', 'Pool cue'}
DROPM = {'Standard Padel Cover', 'first plastic head', 'offset head patent', 'Yellow sliotar', 'Smart sliotar', 'Rebounder Training Ball',
         'Standard Padel Cover'}
OVR = {  # model -> (entry, maker)
    'M-series and carbon-face TaylorMade drivers': ('M-series', 'TaylorMade'), 'M1 and M2': ('M-series', 'TaylorMade'),
    'M3 and M4': ('M-series', 'TaylorMade'), 'M5 and M6': ('M-series', 'TaylorMade'),
    'SIM and SIM Max': ('SIM', 'TaylorMade'), 'SIM2': ('SIM', 'TaylorMade'), 'Stealth 2': ('Stealth', 'TaylorMade'),
    'Phantom 5': ('Phantom', 'Scotty Cameron'), 'Phantom 7': ('Phantom', 'Scotty Cameron'), 'Phantom 9R': ('Phantom', 'Scotty Cameron'),
    'Phantom 11R OC': ('Phantom', 'Scotty Cameron'), 'Studio Style Fastback 2': ('Studio Style', 'Scotty Cameron'),
    'Studio Style Santa Fe': ('Studio Style', 'Scotty Cameron'),
    'Plastic lacrosse head': ('plastic head', 'STX'), 'Offset head': ('offset head', 'Brine'),
    'bamboo hurley': ('bamboo hurley', 'Torpey'), 'Plastic hurley': ('plastic hurley', 'Wavin'),
}
NAMECASE = {'Natural Gut 120': 'Natural Gut'}

def models_to_entries(k, existing_names):
    groups = {}
    order = []
    for name, maker in k.get('m', []):
        if name in DROPM: continue
        if name in OVR:
            line, mk = OVR[name]
        else:
            mk = short(maker)
            nm = name
            if nm.lower().startswith(mk.lower() + ' '): nm = nm[len(mk) + 1:]
            toks = nm.split()
            line = toks[0] if toks else nm
            line = nm if len(toks) <= 1 else line
        key = (mk, line)
        if not mk: key = ('', line)
        groups.setdefault(key, []).append((name, maker))
        if key not in order: order.append(key)
    out = []
    for key in order:
        mk, line = key
        items = groups[key]
        if len(items) == 1 and items[0][0] not in OVR:
            nm = items[0][0]
            if nm.lower().startswith(mk.lower() + ' '): nm = nm[len(mk) + 1:]
            ename = f'{mk} {nm}'.strip()
            vs = []
        else:
            ename = f'{mk} {line}'.strip()
            vs = [{'n': it[0], 'mk': mk, 'y': '', 'd': ''} for it in items]
        if ename.lower() in existing_names: continue
        existing_names.add(ename.lower())
        e = {'n': ename, 'a': '', 'd': f'{mk} {k["n"].lower()} model line in the range listed on the page cited for the kind.', 'mk': mk, 'y': '',
             's': k['s'], 'v': vs}
        out.append(e)
    return out

WC = [("Tiento / T-Model", 1930), ("Federale 102", 1934), ("Allen", 1938), ("Duplo T", 1950), ("Swiss World Champion", 1954), ("Top Star", 1958),
      ("Crack", 1962), ("4-Star", 1966), ("Telstar", 1970), ("Telstar Durlast", 1974), ("Tango Durlast", 1978), ("Tango España", 1982),
      ("Azteca", 1986), ("Etrusco Unico", 1990), ("Questra", 1994), ("Tricolore", 1998), ("Fevernova", 2002), ("Teamgeist", 2006),
      ("Jabulani", 2010), ("Brazuca", 2014), ("Telstar 18", 2018), ("Al Rihla", 2022), ("Trionda", 2026)]
def wc_entries():
    out = []
    for n, y in WC:
        e = {'n': n, 'a': '', 'd': f'Official match ball of the {y} FIFA World Cup.', 'y': str(y), 's': SRC['telstar'], 'v': [],
             'g': 'Before the Adidas era (1930–1966)' if y < 1970 else 'Adidas era (1970–2026)'}
        if y >= 1970:
            e['mk'] = 'adidas'; market(e, 'adidas')
        out.append(e)
    out.append({'n': 'Beau Jeu', 'a': '', 'd': 'Adidas official match ball of UEFA Euro 2016.', 'mk': 'adidas', 'y': '2016', 's': SRC['adidas'], 'v': [], 'g': 'Other Adidas match balls', **{}})
    out.append({'n': 'Finale', 'a': '', 'd': 'Adidas ball line used for the UEFA Champions League.', 'mk': 'adidas', 'y': '', 's': SRC['adidas'], 'v': [], 'g': 'Other Adidas match balls'})
    for e in out[-2:]: market(e, 'adidas')
    return out

def add_versions(x, vs):
    have = {v['n'].lower() for v in x.get('v', [])}
    for v in vs:
        if v['n'].lower() not in have: x.setdefault('v', []).append(v)

def find(k, name):
    for x in k.get('x', []):
        if x['n'] == name: return x
    raise KeyError(name)

NL = {
    'racket': 'One entry is a racket or paddle model line a buyer asks for by name; generations and sizes are versions.',
    'club': 'One entry is a club model line a buyer asks for by name; head variants and generations are versions.',
    'ball': 'One entry is a ball model or line sold under its maker\'s name; sizes, colours and grades are versions.',
    'bat': 'One entry is a bat or stick model line sold under its maker\'s name; generations and sizes are versions.',
    'gear': 'One entry is a named product line sold under its maker\'s name; generations and sizes are versions.',
}
def nlfor(kn):
    k = kn.lower()
    if k.endswith('ball') or k in ('sliotar',): return NL['ball']
    if any(w in k for w in ('racket', 'paddle', 'bat', 'stick', 'hurley')): return NL['bat'] if any(w in k for w in ('bat', 'stick', 'hurley')) else NL['racket']
    if any(w in k for w in ('driver', 'wood', 'hybrid', 'iron', 'wedge', 'putter')): return NL['club']
    if 'ball' in k or k in ('sliotar',): return NL['ball']
    return NL['gear']

def main():
    P = {'replaces': NAMES, 'depts': [], 'brands': [], 'brand_updates': {}, 'renames': {}, 'moves': []}
    dropped_models = []
    for d0 in OLD['depts']:
        if d0['n'] not in NAMES: continue
        d = copy.deepcopy(d0)
        for sh in d['s']:
            for k in sh['k']:
                ms = k.pop('m', [])
                k['m_old'] = ms
                xs = k.get('x', []) or []
                for x in xs:
                    mkx = short(x.get('mk', '')) if x.get('mk') else ''
                    if mkx: market(x, mkx)
                    x.setdefault('v', [])
                k['x'] = xs
        # kind specific edits
        for sh in d['s']:
            for k in sh['k']:
                kn = k['n']; names = {e['n'].lower() for e in k['x']}
                if kn in KEEP:
                    new = models_to_entries({**k, 'm': k['m_old']}, names)
                    k['x'].extend(new)
                else:
                    if k['m_old']: dropped_models.append((kn, len(k['m_old'])))
                if kn == 'Football':
                    k['x'] = wc_entries()
                    k['xg'] = 'by era: before the Adidas era, then Adidas World Cup balls, then other Adidas match balls'
                if kn == 'Basketball':
                    k['x'] = [x for x in k['x'] if x['n'] != 'NBA official game ball']
                    k['x'] += [
                        {'n': 'Spalding NBA game ball', 'a': '', 'd': 'Official NBA game ball supplied by Spalding from 1983 to 2021.', 'mk': 'Spalding', 'y': '1983', 's': SRC['spalding'], 'v': [], 'g': 'Official NBA ball by supplier'},
                        {'n': 'Wilson NBA game ball', 'a': '', 'd': 'Official NBA and WNBA game ball supplied by Wilson from 2021, after a 2020 announcement.', 'mk': 'Wilson', 'y': '2021', 's': SRC['wilson'], 'v': [], 'g': 'Official NBA ball by supplier'}]
                    for x in k['x']:
                        x.setdefault('g', 'Other basketballs')
                    for e in k['x']:
                        if e['n'] in ('Spalding NBA game ball', 'Wilson NBA game ball'): market(e, e['mk'])
                    k['xg'] = 'official NBA ball by supplier, then other basketballs'
                if kn == 'American football':
                    x = find(k, 'The Duke'); x['d'] = x['d'] if x.get('d') else ''
                    x['d'] = 'Wilson football that became the NFL official ball in 1941.'; x['mk'] = 'Wilson'; x['y'] = '1941'; x['s'] = SRC['wilson']; market(x, 'Wilson')
                if kn == 'Rugby ball':
                    k['x'] += [{'n': 'Gilbert Match-XV', 'a': '', 'd': 'Gilbert match ball launched in September 2014 for the 2015 Rugby World Cup in England.', 'mk': 'Gilbert', 'y': '2014', 's': SRC['gilbert'], 'v': []},
                               {'n': 'Gilbert Synergie', 'a': '', 'd': 'Gilbert rugby ball named on the maker page.', 'mk': 'Gilbert', 'y': '', 's': SRC['gilbert'], 'v': []}]
                    for e in k['x']:
                        if e['n'].startswith('Gilbert'): market(e, 'Gilbert')
                if kn == 'Golf driver':
                    b = find(k, 'Big Bertha')
                    b['s'] = SRC['bertha']
                    add_versions(b, [
                        {'n': 'Big Bertha', 'mk': 'Callaway', 'y': '1991', 'd': 'stainless steel, 190 cc head'},
                        {'n': 'Titanium second generation', 'mk': 'Callaway', 'y': '', 'd': 'first titanium heads, year not stated'},
                        {'n': 'Biggest Big Bertha', 'mk': 'Callaway', 'y': '1997', 'd': '290 cc head'},
                        {'n': 'Big Bertha Alpha', 'mk': 'Callaway', 'y': '2014', 'd': 'relaunch with Gravity Core'},
                        {'n': 'Great Big Bertha Epic', 'mk': 'Callaway', 'y': '', 'd': 'better-player model, year not stated'},
                        {'n': 'Big Bertha Fusion', 'mk': 'Callaway', 'y': '', 'd': 'game-improvement model, year not stated'}])
                if kn == 'Golf ball':
                    p = find(k, 'Pro V1')
                    add_versions(p, [{'n': 'Pro V1', 'mk': 'Titleist', 'y': '2000', 'd': 'first used on the PGA Tour on 11 October 2000; public from December 2000'},
                                     {'n': 'Pro V1x', 'mk': 'Titleist', 'y': '2003', 'd': 'about three years after the Pro V1; fewer dimples'}])
                if kn == 'Putter':
                    k['x'] = [e for e in k['x'] if e['n'] not in ('Scotty Cameron Phantom', 'Scotty Cameron Studio Style')]
                    for e in k['x']:
                        if e['n'] in ('Phantom',) : pass
                    k['x'] += [
                        {'n': 'Scotty Cameron Phantom', 'a': '', 'd': 'Scotty Cameron mallet line for 2026 in 5, 7, 9R and 11R heads.', 'mk': 'Scotty Cameron', 'y': '', 's': SRC['cameron'], 'v': [
                            {'n': n, 'mk': 'Scotty Cameron', 'y': '', 'd': ''} for n in ('Phantom 5', 'Phantom 5.2', 'Phantom 5.5', 'Phantom 5 OC', 'Phantom 7', 'Phantom 7.2', 'Phantom 7.5', 'Phantom 7 DB', 'Phantom 9R', 'Phantom 9.2R', 'Phantom 11R OC', 'Phantom X 11')]},
                        {'n': 'Scotty Cameron Studio Style', 'a': '', 'd': 'Milled Scotty Cameron blades and mid-mallets with an SCS face insert.', 'mk': 'Scotty Cameron', 'y': '', 's': SRC['cameron'], 'v': [
                            {'n': n, 'mk': 'Scotty Cameron', 'y': '', 'd': ''} for n in ('Studio Style Newport', 'Studio Style Newport 2', 'Studio Style Newport Plus', 'Studio Style Newport 2 Plus', 'Studio Style Fastback', 'Studio Style Fastback 2', 'Studio Style Fastback OC', 'Studio Style Squareback', 'Studio Style Squareback 2', 'Studio Style Catalina', 'Studio Style Santa Fe')]},
                        {'n': 'Scotty Cameron Super Select', 'a': '', 'd': 'Scotty Cameron line launched in 2023 with a Newport 2 Plus carried over.', 'mk': 'Scotty Cameron', 'y': '2023', 's': SRC['cameron'], 'v': [{'n': 'Super Select Newport 2 Plus', 'mk': 'Scotty Cameron', 'y': '2023', 'd': ''}]}]
                    for e in k['x']:
                        if e.get('mk') == 'Scotty Cameron': market(e, 'Scotty Cameron')
                if kn == 'Ice hockey stick':
                    pass
        # sections and kind fields
        for sh in d['s']:
            for k in sh['k']:
                k.pop('m_old', None)
                xs = k['x']
                if xs:
                    k['nl'] = nlfor(k['n'])
                    for e in xs:
                        if e.get('mk'): market(e, short(e['mk']))
                        e['mk'] = short(e['mk']) if e.get('mk') else e.get('mk', '')
                    if k['n'] != 'Football' and k['n'] != 'Basketball' and len(xs) >= 4:
                        for e in xs:
                            if 'g' not in e: e['g'] = e['mk'] or 'Maker not named'
                        xs.sort(key=lambda e: (e['g'], e.get('y') or '9999', e['n']))
                        k['xg'] = 'by maker'
                    n = len(xs)
                    if k['n'] == 'Football':
                        k['sel'] = 'Every FIFA World Cup official match ball from 1930 to 2026 in the ball list on the Adidas Telstar page, then the two further Adidas match-ball lines named on the Adidas page; club and training balls are commodity. Complete: 23 of 23 World Cup balls in the Adidas Telstar page list.'
                    elif k['n'] == 'Basketball':
                        k['sel'] = 'The official NBA ball by supplier (Spalding 1983–2021, Wilson from 2021) as the Spalding and Wilson company pages state, plus the Evolution kept from the earlier pass; other basketballs are commodity. Covers 3 balls named on those pages; no complete list of basketball models exists.'
                    elif k['n'] == 'American football':
                        k['sel'] = 'The NFL official ball as the Wilson page states; other footballs are commodity. Complete: 1 of 1 NFL official ball named on the Wilson page.'
                    elif k['n'] == 'Rugby ball':
                        k['sel'] = 'Gilbert match balls named on the Gilbert company page and its 2026 range page; training balls dropped. Covers %d Gilbert lines named on those pages; the pages do not list every World Cup ball by year.' % n
                    elif k['n'] == 'Golf driver':
                        k['sel'] = 'Driver model lines named on the shop range page cited and on the maker pages cited per entry (Callaway Big Bertha timeline from GolfMagic). Covers %d lines named on those pages; no complete list of driver lines is published, so the total is unknown.' % n
                    elif k['n'] == 'Putter':
                        k['sel'] = 'Putter lines from the shop range page cited, the Scotty Cameron 2026 model guide and the maker pages cited per entry. Covers %d lines named on those pages; no complete putter reference exists.' % n
                    elif k['n'] == 'Golf ball':
                        k['sel'] = 'Golf ball lines named on the shop range page cited and the Titleist Pro V1 page (Pro V1 and Pro V1x years). Covers %d lines named on those pages; no complete golf ball reference exists.' % n
                    else:
                        k['sel'] = 'Follows the shop range or maker page cited for the kind and the maker pages cited on each entry; lines are grouped by maker, with named variants as versions. Covers %d lines named on those pages; no complete reference list exists for this kind, so the total is unknown.' % n
                else:
                    k.pop('nl', None)
        # dept-level market panel
        if d['n'] == 'Racket sports':
            d['msum'] = 'Racket brands sit with a few companies; the figures are the revenues and owners stated on the cited pages, not market shares.'
            d['ms'] = [
                {'mkt': 'Wilson (rackets, balls)', 'who': 'Amer Sports', 'share': 'owner since 1989', 'yr': 1989, 's': SRC['wilson'], 'note': 'Wilson has been an Amer Sports subsidiary since 1989; Anta Sports has owned Amer Sports since 2018.'},
                {'mkt': 'Amer Sports revenue', 'who': 'Amer Sports', 'share': 'US$5.18 billion', 'yr': 2024, 's': SRC['amer'], 'note': 'group revenue as the page states; includes Wilson'},
                {'mkt': 'Babolat revenue', 'who': 'Babolat', 'share': 'EUR 141.2 million', 'yr': 2014, 's': SRC['babolat'], 'note': 'company revenue as the page states'},
                {'mkt': 'Head revenue', 'who': 'Head Austria GmbH', 'share': 'US$375.4 million', 'yr': 2014, 's': SRC['head'], 'note': 'company revenue as the page states; Head also owns Penn'},
                {'mkt': 'Yonex revenue', 'who': 'Yonex', 'share': 'JPY 1,636.43 billion', 'yr': 2026, 's': SRC['yonex'], 'note': 'company revenue figure as the page states'},
                {'mkt': 'Decathlon revenue', 'who': 'Decathlon', 'share': 'EUR 20.7 billion', 'yr': 2025, 's': SRC['decathlon'], 'note': 'retailer with own sports brands'}]
        if d['n'] == 'Golf':
            d['msum'] = 'Golf equipment is led by a few owner groups; the facts below are the owners and revenues stated on the cited pages, not market shares.'
            d['ms'] = [
                {'mkt': 'Golf balls, putters, wedges and shoes', 'who': 'Acushnet Company', 'share': 'Titleist, FootJoy, Scotty Cameron, Pinnacle, Vokey', 'yr': 2018, 's': SRC['acushnet'], 'note': 'brands owned per the page; Fila Korea raised its holding to 53.1% in August 2018'},
                {'mkt': 'Topgolf Callaway Brands revenue', 'who': 'Topgolf Callaway Brands', 'share': 'US$2.060 billion', 'yr': 2025, 's': SRC['callaway'], 'note': 'company revenue as the page states; subsidiaries include Callaway Golf, Odyssey, TravisMathew, OGIO'},
                {'mkt': 'TaylorMade ownership', 'who': 'Centroid Investment Partners', 'share': 'owner', 'yr': 2022, 's': SRC['taylormade'], 'note': 'the page dates the Centroid agreement to 11 May 2022; KPS Capital Partners owned it before'}]
        if d['n'] == 'Team sports':
            d['msum'] = 'Team-sport kit is sold by a few sportswear groups and one retailer brand family; the figures are revenues stated on the cited pages.'
            d['ms'] = [
                {'mkt': 'Sportswear revenue', 'who': 'Nike, Inc.', 'share': 'US$46.3 billion', 'yr': 2025, 's': SRC['nike'], 'note': 'company revenue as the page states; fiscal year ends 31 May'},
                {'mkt': 'Sportswear revenue', 'who': 'Adidas AG', 'share': 'EUR 23.683 billion', 'yr': 2024, 's': SRC['adidas'], 'note': 'company revenue as the page states; second largest after Nike per the page'},
                {'mkt': 'Sporting goods group revenue', 'who': 'Amer Sports', 'share': 'US$5.18 billion', 'yr': 2024, 's': SRC['amer'], 'note': 'owns Wilson, DeMarini, EvoShield and Louisville Slugger'},
                {'mkt': 'Sports retailer revenue', 'who': 'Decathlon', 'share': 'EUR 20.7 billion', 'yr': 2025, 's': SRC['decathlon'], 'note': 'own team-sport brand Kipsta; 1,902 stores in 82 countries'},
                {'mkt': 'Basketball (NBA ball supplier)', 'who': 'Wilson', 'share': 'official NBA ball', 'yr': 2021, 's': SRC['wilson'], 'note': 'Wilson took over from Spalding, supplier 1983 to 2021'}]
        if d['n'] == 'Protective gear':
            d['msum'] = 'Hockey protective gear is led by Bauer, owned by Peak Achievement Athletics; the facts below are owners stated on the cited pages.'
            d['ms'] = [
                {'mkt': 'Ice hockey equipment (Bauer)', 'who': 'Peak Achievement Athletics', 'share': 'owner', 'yr': 2017, 's': SRC['bauer'], 'note': 'Fairfax Financial owns Peak Achievement; it agreed in September 2024 to buy out Sagard and become sole owner'},
                {'mkt': 'Baseball and softball (EvoShield, DeMarini, Louisville Slugger)', 'who': 'Amer Sports', 'share': 'brands owned', 'yr': 2024, 's': SRC['amer'], 'note': 'brand list as the page states'}]
        if d['n'] == 'Target & precision sports':
            d['msum'] = 'No market figure for target and precision sport equipment was found on a fetched page; bows and firearms are listed under E4.'
            d['ms'] = []
        P['depts'].append(d)
    json.dump(P, open('/home/user/Possession-Taxonomy/rebuild/out/E2_parts/RACKET.json', 'w'), ensure_ascii=False, indent=0)
    print('dropped model lists', dropped_models)
    print(sum(len(json.dumps(x)) for x in P['depts']))
main()
