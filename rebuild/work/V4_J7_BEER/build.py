import json, re, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data1 import U, SEL_GROUP
import data3
from data2 import ENT, GR, NT, CF, IN, OLB
R = '/home/user/Possession-Taxonomy/rebuild/'
W = R + 'work/V4_J7_BEER/'
old = json.load(open(W + 'bak/J7.json'))
beer = [x for x in old['depts'] if x['n'] == 'Beer'][0]
FETCHED = set(U.values())

OLDE = {}   # name -> (entry, oldkind)
OLDK = {}
for sh in beer['s']:
    for k in sh['k']:
        OLDK[k['n']] = k
        for e in k.get('x', []) or []:
            OLDE[e['n']] = (e, k['n'])

def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())
STRIP = r'\b(brewing|brewery|brewers|breweries|company|co|inc|brasserie|brouwerij|brauerei|gesellschaft|bräu|brau|and sons|sons|family|gruppe|group)\b'
def nk(s): return norm(re.sub(STRIP, '', re.sub(r'\(.*?\)', '', s.lower())))
def alc_of(name):
    return 'alcohol-free' if re.search(r'0[.,]0|zero', name, re.I) else ''

KINDS = [
 # key, name, shelf
 ('AB', 'AB InBev brands', 'G'), ('HE', 'Heineken brands', 'G'), ('SN', 'China Resources Snow brands', 'G'), ('CA', 'Carlsberg brands', 'G'),
 ('MC', 'Molson Coors brands', 'G'), ('AS', 'Asahi brands', 'G'), ('KI', 'Kirin brands', 'G'), ('TS', 'Tsingtao brands', 'G'),
 ('EU', 'Europe: national and regional brands', 'N'), ('NA', 'North America: national and regional brands', 'N'),
 ('LA', 'Latin America: national and regional brands', 'N'), ('AF', 'Africa and the Middle East: national and regional brands', 'N'),
 ('SA', 'South Asia: national and regional brands', 'N'), ('EA', 'East Asia: national and regional brands', 'N'),
 ('SE', 'Southeast Asia: national and regional brands', 'N'), ('OC', 'Oceania: national and regional brands', 'N'),
 ('IE', 'Independent brewers in Europe', 'I'), ('IA', 'Independent brewers in the Americas', 'I'), ('IW', 'Independent brewers in Asia, Africa and Oceania', 'I'),
 ('CU', 'United States craft breweries', 'C'), ('CB', 'Belgian craft and abbey breweries', 'C'), ('CG', 'British and Irish heritage and craft breweries', 'C'),
 ('OL', 'Own-label beers', 'O'),
]
KN = {k: n for k, n, s in KINDS}

# ---- entries ----
used = set()
byk = collections.defaultdict(list)
styles = collections.defaultdict(set)
alcs = collections.defaultdict(set)
tiers = collections.defaultdict(set)
for E in ENT:
    olds = [OLDE[o] for o in E['old']]
    for o in E['old']:
        assert o in OLDE, o
        used.add(o)
    e = {'n': E['n'], 'a': E['a'], 'd': E['d'] or (olds[0][0]['d'] if olds else ''), 'mk': E['own'], 'y': E['y'] or (olds[0][0]['y'] if olds and len(olds) == 1 else ''),
         's': E['src'] if (E['src'] in FETCHED or not olds) else olds[0][0]['s'], 'v': [], 'dt': olds[0][0].get('dt', '') if olds else '',
         'own': E['own'], 'cty': E['cty'], 'g': E['g'] or E['cty'] or 'Other'}
    if E['tier']: e['tier'] = E['tier']
    if E['own_y']: e['own_y'] = E['own_y']
    if E['role']: e['role'] = E['role']
    if E['alc']: e['alc'] = E['alc']
    seen = set()
    def addv(n, d, y='', alc=''):
        if not n or n in seen or n == e['n'] and not d: return
        seen.add(n)
        v = {'n': n, 'y': y, 'd': d}
        a = alc or alc_of(n)
        if a: v['alc'] = a; alcs[E['kind']].add(a)
        e['v'].append(v)
    for oe, ok in olds:
        st = ok
        styles[E['kind']].add(st)
        addv(oe['n'], f"{st}. {oe['d']}".strip(), oe.get('y', ''))
        for ov in oe.get('v', []):
            if ov['n'] in ('Bud Zero', 'Dry Zero'): continue
            addv(ov['n'], (ov.get('d') or ''), ov.get('y', ''))
    for t in E['v']:
        addv(t[0], t[1], '', t[2] if len(t) > 2 else '')
    if E['style']: styles[E['kind']].add(E['style'])
    if E['alc']: alcs[E['kind']].add(E['alc'])
    if E['tier']: tiers[E['kind']].add(E['tier'])
    # an entry whose only version repeats the entry adds nothing
    e['_olds'] = [o[1] for o in olds]
    byk[E['kind']].append(e)

# loose models -> versions of a matching entry, else removed
dropped = []; attached = 0
allentries = [e for k in byk.values() for e in k]
def keys(e):
    ks = {nk(e['n'])}
    for E_ in [x for x in ENT if x['n'] == e['n']]:
        for o in E_['old']: ks.add(nk(OLDE[o][0].get('mk', '')))
    return {k for k in ks if len(k) >= 4}
KEYS = [(e, keys(e)) for e in allentries]
for kname, k in OLDK.items():
    for model, br in k.get('m', []) or []:
        b = nk(br)
        hit = None
        if len(b) >= 4:
            for e, ks in KEYS:
                if b in ks:
                    hit = e; break
        if hit and model not in {v['n'] for v in hit['v']}:
            hit['v'].append({'n': model, 'y': '', 'd': f'{kname}. Earlier loose model, now a version of this entry.'})
            attached += 1
            for E_ in ENT:
                if E_['n'] == hit['n']: styles[E_['kind']].add(kname)
        else:
            dropped.append((model, br, kname))
    for rr in k.get('r', []) or []:
        dropped.append((rr[0], rr[1], kname + ' (range)'))

missed = [n for n in OLDE if n not in used and OLDE[n][1] not in ('Sorghum beer', 'Millet beer', 'Maize beer', 'Banana beer', 'Rye beer', 'Sahti')]
print('old entries not absorbed:', missed)

# ---- kind metadata ----
NL = {
 'AB': 'One entry is a beer brand or brewery in the AB InBev portfolio; its beers and zero versions are versions.',
 'HE': 'One entry is a beer brand or brewery owned by Heineken; its beers and zero versions are versions.',
 'SN': 'One entry is a beer brand of China Resources Snow Breweries; its beers are versions.',
 'CA': 'One entry is a beer brand or brewery owned by Carlsberg Group; its beers and zero versions are versions.',
 'MC': 'One entry is a beer brand or brewery owned by Molson Coors; its beers are versions.',
 'AS': 'One entry is a beer brand or brewery owned by Asahi; its beers and zero versions are versions.',
 'KI': 'One entry is a beer brand or brewery owned by Kirin; its beers are versions.',
 'TS': 'One entry is the Tsingtao brand; its beers are versions.',
 'EU': 'One entry is a beer brand or brewery that is tied to a European home market and is not in a global group.',
 'NA': 'One entry is a beer brand tied to a North American home market and not in a global group.',
 'LA': 'One entry is a beer brand tied to a Latin American home market and not in a global group.',
 'AF': 'One entry is a beer brand tied to an African or Middle Eastern home market and not in a global group.',
 'SA': 'One entry is a beer brand tied to the Indian market; its owner and market share are recorded where a page states them.',
 'EA': 'One entry is a beer brand tied to a home market in East Asia and not in a global group.',
 'SE': 'One entry is a beer brand tied to a home market in Southeast Asia and not in a global group.',
 'OC': 'One entry is a beer brand tied to an Oceanian home market and not in a global group.',
 'IE': 'One entry is a beer brand or brewery owned by an established European company that is not a global group; its beers are versions.',
 'IA': 'One entry is a beer brand or brewery owned by an established company in the Americas that is not a global group.',
 'IW': 'One entry is a beer brand or brewery owned by an established company in Asia, Africa or Oceania that is not a global group.',
 'CU': 'One entry is a craft brewery; its beers, with BJCP style, are versions.',
 'CB': 'One entry is a Belgian abbey, lambic or craft brewery; its beers, with BJCP style, are versions.',
 'CG': 'One entry is a British or Irish heritage or craft brewery, or a historic beer of one; its beers, with BJCP style, are versions.',
 'OL': 'One entry is a beer sold under a retailer\'s own name, or a retailer\'s own beer line; its beers are versions.',
}
SEL = {k: SEL_GROUP[k] for k in SEL_GROUP}
SEL.update({
 'EU': 'No whole-space reference exists. Follows Wikipedia "Beer and breweries by region" (fetched 2026-10-31), the first 100,000 characters: brands named for Albania, Armenia, Lithuania, Slovakia, Spain and Ukraine, plus Sinebrychoff. Brands of the global groups sit in their group kind.',
 'NA': 'No whole-space reference exists. Follows Wikipedia "Beer in Canada" and the Brewers Association 2024 list (fetched 2026-10-31); heritage US brands from the earlier list. Canadian brands of the global groups sit in their group kind.',
 'LA': 'No whole-space reference exists. Follows Wikipedia "Beer in Brazil" and "Beer and breweries by region" (fetched 2026-10-31); most Latin American brands belong to AB InBev or Heineken and sit in those kinds.',
 'AF': 'No whole-space reference exists. Follows Wikipedia "Beer in Kenya", "Beer in South Africa" and "Heineken brands" (fetched 2026-10-31); SAB brands sit under AB InBev.',
 'SA': 'Follows Wikipedia "Beer in India" (fetched 2026-10-31, first 100,000 characters): the brands with a stated 2014 market share, excluding those of the global groups.',
 'EA': 'Follows Wikipedia "Beer in China" and "Beer and breweries by region" (fetched 2026-10-31): the major Chinese brands outside the global groups, and North Korea\'s top brand. Japanese brewers are under Independents and the groups.',
 'SE': 'Follows Wikipedia "Beer in Thailand", "Beer in Vietnam", "San Miguel Brewery" and "Beer and breweries by region" (fetched 2026-10-31). Tiger, Larue and Huda sit with their owners.',
 'OC': 'Follows Wikipedia "Beer in Australia" (fetched 2026-10-31, first 100,000 characters): the one major Australian-owned brewery outside the groups.',
 'IE': 'Follows the VinePair 2024 ranking of the 40 largest brewing groups (BarthHaas data), Wikipedia "Beer in Germany", "Mahou-San Miguel Group" and "Swinkels Family Brewers" (fetched 2026-10-31); German specialist breweries carried over from the earlier list. Groups owned by Heineken, Carlsberg or the others sit in their own kinds.',
 'IA': 'Follows the VinePair 2024 ranking, Wikipedia "Beer in Canada" and "Beer and breweries by region" (fetched 2026-10-31). Brewers outside the top 40 are not listed.',
 'IW': 'Follows Wikipedia "Sapporo Breweries" and "Groupe Castel" (fetched 2026-10-31). Kirin, Asahi and Tsingtao have their own kinds.',
 'CU': 'Follows the Brewers Association 2024 ranking of the top 50 US craft brewing companies (fetched 2026-10-31); every one of the 50 is included. Earlier craft entries outside the list are in the last section.',
 'CB': 'No ranked list exists. Keeps the Belgian abbey, lambic and gueuze breweries of the earlier selection, with sources from the earlier passes.',
 'CG': 'No ranked list exists. Keeps the British, Irish and Scandinavian heritage breweries of the earlier selection, with sources from the earlier passes.',
 'OL': 'No whole-space reference exists. Follows the Punch article on grocery-store craft beer (fetched 2026-10-31): Aldi, Trader Joe\'s, Costco and Stewart\'s. Lidl and Tesco ranges were not on a fetched page.',
})
XG = {k: 'country of the brand' for k in KN}
XG.update({'CU': 'rank in the Brewers Association 2024 list', 'AB': 'country of the brand', 'IE': 'country of the brewery'})
DK = {
 'AB': 'Beers owned by Anheuser-Busch InBev, the world\'s largest brewer, from Budweiser and Corona to local champions in Brazil, Colombia and South Africa.',
 'HE': 'Beers owned by Heineken, the second-largest brewer, from Heineken and Amstel to Tecate and the Mexican, Brazilian and European units.',
 'SN': 'Beers of China Resources Snow Breweries, the third-largest brewer, led by Snow.',
 'CA': 'Beers owned by Carlsberg Group, from Carlsberg and Tuborg to Kronenbourg 1664 and the Baltic, Nordic and Asian breweries.',
 'MC': 'Beers owned by Molson Coors, from Coors Light and Miller Lite to Molson Canadian and the central European breweries.',
 'AS': 'Beers owned by Asahi, from Asahi Super Dry to the Peroni, Pilsner Urquell and Australian brands bought since 2013.',
 'KI': 'Beers owned by Kirin, from Kirin Lager to Bell\'s and New Belgium in the United States and Lion in Australia.',
 'TS': 'Beers of Tsingtao Brewery Group, China\'s export champion.',
 'EU': 'Beer brands tied to a European home market that no global group owns, from the Baltic states to Spain.',
 'NA': 'Beer brands tied to the United States or Canada that no global group owns.',
 'LA': 'Beer brands tied to a Latin American market that no global group owns.',
 'AF': 'Beer brands tied to an African or Middle Eastern market that no global group owns.',
 'SA': 'Indian beer brands outside the global groups, led by Kingfisher.',
 'EA': 'Chinese and North Korean beer brands outside the global groups.',
 'SE': 'Thai, Filipino, Vietnamese and Burmese beer brands outside the global groups.',
 'OC': 'Australian-owned beer brands outside the global groups.',
 'IE': 'Established European brewers owned by neither a global group nor a craft start-up: German groups, Swinkels, Mahou San Miguel, Efes, Diageo\'s Guinness and Czech and Spanish houses.',
 'IA': 'Established brewers in the Americas outside the global groups.',
 'IW': 'Established brewers in Asia, Africa and Oceania outside the global groups: Sapporo and the Castel group.',
 'CU': 'The United States craft breweries on the Brewers Association 2024 top 50, plus earlier craft entries.',
 'CB': 'Belgian abbey, lambic and gueuze breweries.',
 'CG': 'British and Irish heritage and craft breweries, and the historic beers they brew.',
 'OL': 'Beers sold under a supermarket\'s or retailer\'s own name.',
}

SHELVES = [
 ('G', 'Global groups', 'Beers owned by the multinational brewing groups that dominate the category worldwide, one kind per group.', 'kinds from the largest group by 2024 volume down',
  ['AB', 'HE', 'SN', 'CA', 'MC', 'TS', 'AS', 'KI']),
 ('N', 'National & regional brands', 'Home-market brands outside the global groups, one kind per world region.', 'kinds by world region, from Europe round to Oceania',
  ['EU', 'NA', 'LA', 'AF', 'SA', 'EA', 'SE', 'OC']),
 ('I', 'Independents', 'Established brewers that are neither global groups nor craft start-ups, by region.', None, ['IE', 'IA', 'IW']),
 ('C', 'Craft & indie', 'Small and independent craft and artisan breweries, by country.', None, ['CU', 'CB', 'CG']),
 ('O', 'Own label', 'Beers sold under a retailer\'s own name.', None, ['OL']),
]

def tt_for(key):
    out = []
    if styles.get(key): out.append(['BJCP style', sorted(styles[key])])
    if tiers.get(key): out.append(['Owner tier', sorted(tiers[key])])
    if alcs.get(key): out.append(['Alcohol level', sorted(alcs[key])])
    return out

def sort_entries(key, es):
    if key == 'CU':
        def rk(e):
            m = re.search(r'ranked (\d+)', e['d'])
            return (0, int(m.group(1))) if m and e['g'].startswith('Ranks') else (1, 0)
        return sorted(es, key=lambda e: (rk(e), e['n']))
    return sorted(es, key=lambda e: (e['g'], e.get('own_y', '9999') or '9999', e['n']))

kinds_out = {}
for key, name, sh in KINDS:
    es = sort_entries(key, byk[key])
    for e in es: e.pop('_olds', None)
    k = {'n': name, 'd': DK[key], 'nl': NL[key], 'sel': SEL[key], 'xg': XG[key], 'x': es}
    t = tt_for(key)
    if t: k['tt'] = t
    kinds_out[key] = k

# traditional shelf: old kinds kept as they were, with the new fields
TRAD = ['Sorghum beer', 'Millet beer', 'Maize beer', 'Banana beer', 'Rye beer', 'Sahti']
trad_k = []
for n in TRAD:
    ok = json.loads(json.dumps(OLDK[n]))
    ok['nl'] = 'One entry is a traditional brew or a named brand of one; versions are regional or brand variants.'
    ok['sel'] = 'No whole-space reference exists; the entries are the earlier selection from Wikipedia pages on each tradition (fetched in earlier passes).'
    ok['xg'] = 'country or people of origin'
    ok.pop('m', None); ok.pop('r', None)
    if ok.get('x'):
        for e in ok['x']:
            e['g'] = 'Traditional'
    trad_k.append(ok)
for ok in trad_k:
    if not ok.get('x'): ok['x'] = []

shelves = []
for sid, sn, st, sax, ks in SHELVES:
    sh = {'n': sn, 't': st, 'k': [kinds_out[k] for k in ks]}
    if len(ks) > 3: sh['ax'] = sax
    shelves.append(sh)
shelves.append({'n': 'Traditional & non-barley brews', 't': 'Beers brewed from grains other than barley, or to a regional tradition: sorghum, millet, maize, banana and rye brews, and sahti.',
                'ax': 'kinds by the main grain or fruit used', 'k': trad_k})

RENAMES = {
 'International pale lager': 'AB InBev brands', 'American light lager': 'Molson Coors brands', 'Czech pale lager': 'Asahi brands',
 'German Pils': 'Independent brewers in Europe', 'Munich Helles': 'Independent brewers in Europe', 'Dortmunder Export': 'Independent brewers in Europe',
 'Kellerbier': 'Independent brewers in Europe', 'Festbier': 'Independent brewers in Europe', 'Märzen': 'Independent brewers in Europe', 'Vienna lager': 'Asahi brands',
 'Munich Dunkel': 'Independent brewers in Europe', 'Czech dark lager': 'Independent brewers in Europe', 'Schwarzbier': 'Independent brewers in Europe',
 'Rauchbier': 'Independent brewers in Europe', 'Bock': 'Independent brewers in Europe', 'Doppelbock': 'Independent brewers in Europe', 'Eisbock': 'Independent brewers in Europe',
 'Baltic porter': 'Heineken brands', 'Blonde ale': 'United States craft breweries', 'American pale ale': 'United States craft breweries', 'American IPA': 'United States craft breweries',
 'Hazy IPA': 'United States craft breweries', 'Double IPA': 'United States craft breweries', 'English IPA': 'British and Irish heritage and craft breweries',
 'Bitter': 'British and Irish heritage and craft breweries', 'Amber & red ale': 'United States craft breweries', 'Brown ale': 'British and Irish heritage and craft breweries',
 'Mild': 'British and Irish heritage and craft breweries', 'Scottish & Scotch ale': 'British and Irish heritage and craft breweries', 'Old ale': 'British and Irish heritage and craft breweries',
 'Barleywine': 'British and Irish heritage and craft breweries', 'English porter': 'British and Irish heritage and craft breweries', 'American porter': 'United States craft breweries',
 'Irish stout': 'Independent brewers in Europe', 'Oatmeal stout': 'British and Irish heritage and craft breweries', 'Sweet stout': 'British and Irish heritage and craft breweries',
 'Foreign extra stout': 'Independent brewers in Europe', 'American stout': 'United States craft breweries', 'Imperial stout': 'United States craft breweries',
 'Weissbier': 'Independent brewers in Europe', 'Witbier': 'United States craft breweries', 'American wheat beer': 'United States craft breweries', 'Kölsch': 'Independent brewers in Europe',
 'Altbier': 'Independent brewers in Europe', 'California common': 'United States craft breweries', 'Cream ale': 'North America: national and regional brands',
 'Belgian single': 'Belgian craft and abbey breweries', 'Belgian blond ale': 'AB InBev brands', 'Saison': 'Independent brewers in Europe', 'Bière de garde': 'Independent brewers in Europe',
 'Dubbel': 'Belgian craft and abbey breweries', 'Tripel': 'Belgian craft and abbey breweries', 'Belgian golden strong ale': 'Independent brewers in Europe',
 'Belgian dark strong ale': 'Belgian craft and abbey breweries', 'Lambic': 'Belgian craft and abbey breweries', 'Gueuze': 'Belgian craft and abbey breweries',
 'Fruit lambic': 'Belgian craft and abbey breweries', 'Flanders red ale': 'Belgian craft and abbey breweries', 'Oud bruin': 'Belgian craft and abbey breweries',
 'Berliner Weisse': 'Independent brewers in Europe', 'Gose': 'Independent brewers in Europe', 'American wild ale': 'United States craft breweries',
 'Gluten-free beer': 'United States craft breweries', 'Fruit & spice beer': 'United States craft breweries',
}
allold = set(OLDK)
cover = set(RENAMES) | set(TRAD)
print('old kinds uncovered:', allold - cover)

MS = [
 {"mkt": "World beer output, all groups", "who": "Total of the 40 largest groups", "share": "1,638.82 million hl", "yr": 2024, "s": U['VP'], "note": "volume, BarthHaas data via VinePair; down 0.6 % on 2023"},
 {"mkt": "World beer output", "who": "Anheuser-Busch InBev", "share": "495.49 million hl", "yr": 2024, "s": U['VP'], "note": "volume, rank 1"},
 {"mkt": "World beer output", "who": "Heineken", "share": "240.70 million hl", "yr": 2024, "s": U['VP'], "note": "volume, rank 2"},
 {"mkt": "World beer output", "who": "China Resources Snow Breweries", "share": "108.80 million hl", "yr": 2024, "s": U['VP'], "note": "volume, rank 3"},
 {"mkt": "World beer output", "who": "Carlsberg", "share": "101.20 million hl", "yr": 2024, "s": U['VP'], "note": "volume, rank 4"},
 {"mkt": "World beer output", "who": "Molson Coors", "share": "79.62 million hl", "yr": 2024, "s": U['VP'], "note": "volume, rank 5"},
 {"mkt": "World beer output", "who": "Tsingtao Brewery Group", "share": "75.38 million hl", "yr": 2024, "s": U['VP'], "note": "volume, rank 6"},
 {"mkt": "World beer output", "who": "Asahi Group", "share": "65.00 million hl", "yr": 2024, "s": U['VP'], "note": "volume, rank 7"},
 {"mkt": "World beer output", "who": "Kirin", "share": "22.90 million hl", "yr": 2024, "s": U['VP'], "note": "volume, rank 14"},
 {"mkt": "World beer output", "who": "Tsingtao Beer brand", "share": "2.8 %", "yr": 2016, "s": U['TS'], "note": "share of global beer; second most consumed beer"},
 {"mkt": "Chinese beer", "who": "Snow (China Resources)", "share": "21.7 %", "yr": 2013, "s": U['CHN'], "note": "market share, best-selling beer in China"},
 {"mkt": "Chinese beer", "who": "China Resources Snow", "share": "about 21 %", "yr": 2010, "s": U['SN'], "note": "9.28 billion litres sold"},
 {"mkt": "Indian beer", "who": "United Breweries", "share": "51.1 %", "yr": 2014, "s": U['IND'], "note": "company share; Kingfisher alone 41.2 %"},
 {"mkt": "Indian beer", "who": "SABMiller", "share": "25.6 %", "yr": 2014, "s": U['IND'], "note": "company share"},
 {"mkt": "Indian beer", "who": "Carlsberg", "share": "7.6 %", "yr": 2014, "s": U['IND'], "note": "company share"},
 {"mkt": "Brazilian beer", "who": "AmBev (InBev)", "share": "70 %", "yr": 2009, "s": U['BRZ'], "note": "company share"},
 {"mkt": "Brazilian beer", "who": "Skol", "share": "32.6 %", "yr": 2005, "s": U['BRZ'], "note": "brand share"},
 {"mkt": "Vietnamese beer", "who": "Heineken", "share": "43 %", "yr": 2023, "s": U['VNM'], "note": "company share"},
 {"mkt": "Vietnamese beer", "who": "Sabeco", "share": "33.9 %", "yr": 2023, "s": U['VNM'], "note": "company share, as read from the page's sentence"},
 {"mkt": "Vietnamese beer", "who": "Carlsberg", "share": "9.2 %", "yr": 2023, "s": U['VNM'], "note": "company share"},
 {"mkt": "Thai beer", "who": "Leo (Boon Rawd)", "share": "53 %", "yr": 2018, "s": U['THA'], "note": "brand share; Chang 38 %, Singha 5 %"},
 {"mkt": "Philippine beer", "who": "San Miguel Brewery", "share": "over 95 %", "yr": 2008, "s": U['SMB'], "note": "market share"},
 {"mkt": "Australian beer", "who": "Asahi (Carlton & United Breweries)", "share": "48.5 %", "yr": 2020, "s": U['AS'], "note": "market share as cited by the page"},
 {"mkt": "Australian beer", "who": "Coopers", "share": "over 5 %", "yr": 2016, "s": U['AUS'], "note": "market share"},
 {"mkt": "Canadian beer", "who": "Budweiser (AB InBev)", "share": "13 %", "yr": 2008, "s": U['CAN'], "note": "top-selling brand; Coors Light 12 %"},
 {"mkt": "Canadian beer", "who": "Moosehead", "share": "about 3.8 %", "yr": 2016, "s": U['CAN'], "note": "largest fully Canadian-owned brewer"},
 {"mkt": "Canadian beer", "who": "The three major breweries", "share": "about 90 %", "yr": 2012, "s": U['CAN'], "note": "share of retail sales"},
 {"mkt": "Czech beer", "who": "Asahi", "share": "44 %", "yr": 2020, "s": U['AS'], "note": "beer market share, from the page's 2020 Factbook citation"},
 {"mkt": "Polish beer", "who": "Asahi", "share": "32 %", "yr": 2020, "s": U['AS'], "note": "beer market share, from the page's 2020 Factbook citation"},
 {"mkt": "Romanian beer", "who": "Asahi", "share": "36 %", "yr": 2020, "s": U['AS'], "note": "beer market share, from the page's 2020 Factbook citation"},
 {"mkt": "Italian beer", "who": "Asahi", "share": "18 %", "yr": 2020, "s": U['AS'], "note": "beer market share, from the page's 2020 Factbook citation"},
 {"mkt": "German beer", "who": "Krombacher", "share": "5.49 million hl", "yr": 2015, "s": U['GER'], "note": "brand output; Oettinger 5.39, Bitburger 3.84"},
 {"mkt": "Russian beer", "who": "All producers", "share": "102.93 million hl", "yr": 2010, "s": U['RUS'], "note": "national output; no brand shares on the page"},
 {"mkt": "US craft beer", "who": "D.G. Yuengling and Son", "share": "rank 1 of 50", "yr": 2024, "s": U['BA'], "note": "Brewers Association craft ranking by volume; Boston Beer 2, Sierra Nevada 3"},
 {"mkt": "US beer, all brewers", "who": "Anheuser-Busch", "share": "rank 1 of 50", "yr": 2024, "s": U['BA'], "note": "Brewers Association overall ranking; Molson Coors 2, Constellation 3, Heineken USA 4"},
]
MSUM = ('AB InBev brewed 495.49 million hl in 2024 and Heineken 240.70 million hl; with China Resources Snow, Carlsberg, Molson Coors, Tsingtao, Asahi and Kirin they are the shelf of global groups. '
        'Country shares come from fetched pages in 2005 to 2023: India (United Breweries 51.1 %, 2014), Brazil (AmBev 70 %, 2009), Vietnam (Heineken 43 %, 2023), Thailand (Leo 53 %, 2018), the Philippines (San Miguel over 95 %, 2008). '
        'The US is given as Brewers Association ranks (2024), not shares.')

dept = {'n': 'Beer', 'mode': 'tier',
        't': beer['t'].replace('sold by style: lagers, ales, wheat, Belgian, sour and non-barley brews', 'sold by brand and market: global groups, national and regional brands, independents, craft and own label, with style as an attribute'),
        'ax': 'Who owns the brand and how big is its market: a global brewing group, a national or regional brand, an independent, a craft brewery, or a retailer\'s own label?',
        's': shelves, 'ms': MS, 'msum': MSUM,
        'note': 'The market comes first (owner decision 2026-10-31). Style follows the BJCP Beer Style Guidelines (2021) and appears on each version and in the style list of each kind.',
        'b': beer['b']}

# brand register
reg = json.load(open(R + 'out/J7_brands.json'))['b']
have = {norm(b['n']) for b in reg}
OWNC = {'Anheuser-Busch InBev': 'Belgium', 'Heineken': 'Netherlands', 'China Resources Snow Breweries': 'China', 'Carlsberg Group': 'Denmark',
        'Molson Coors Beverage Company': 'United States', 'Asahi Group Holdings': 'Japan', 'Kirin Holdings': 'Japan', 'Tsingtao Brewery Group': 'China',
        'Diageo': 'Ireland', 'Efes Group': 'Turkey', 'Swinkels Family Brewers': 'Netherlands', 'Groupe Castel': 'France', 'Oettinger Gruppe': 'Germany',
        'Paulaner Gruppe': 'Germany', 'Krombacher Gruppe': 'Germany', 'Bitburger Braugruppe': 'Germany', 'Radeberger Gruppe': 'Germany', 'Damm': 'Spain',
        'Estrella de Galicia': 'Spain', 'Mahou San Miguel': 'Spain', 'Sapporo Holdings': 'Japan', 'Empresas Polar': 'Venezuela', 'Thai Beverages': 'Thailand',
        'Boon Rawd Brewery': 'Thailand', 'San Miguel Brewery': 'Philippines', 'Tilray': 'United States'}
newb = []
segof = {}
for E in ENT:
    if E['own']: segof.setdefault(E['own'], E['tier'] or 'Other')
for o, seg in sorted(segof.items()):
    if norm(o) in have: continue
    have.add(norm(o))
    b = {'n': o, 'seg': seg, 'd': 'Owner of beer brands in the Beer department.', 'kf': 'beer'}
    if o in OWNC: b['c'] = OWNC[o]
    newb.append(b)

out = {'depts': [dept], 'brands': newb, 'renames': RENAMES, 'moves': []}
os.makedirs(R + 'out/J7_parts', exist_ok=True)
tmp = R + 'out/J7_parts/BEER.json.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, R + 'out/J7_parts/BEER.json')
tot = sum(len(k['x']) for s in shelves for k in s['k'])
nv = sum(len(e['v']) for s in shelves for k in s['k'] for e in k['x'])
print('entries', tot, 'versions', nv, 'loose models attached', attached, 'dropped', len(dropped), 'new brands', len(newb))
json.dump(dropped, open(W + 'dropped_models.json', 'w'), ensure_ascii=False)
