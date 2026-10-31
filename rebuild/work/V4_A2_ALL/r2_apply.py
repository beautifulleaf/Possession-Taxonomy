import json, os, re, sys
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/V4_A2_ALL')
R = '/home/user/Possession-Taxonomy/rebuild/'
exec(open(R + 'work/V4_A2_ALL/r2_data1.py').read())
exec(open(R + 'work/V4_A2_ALL/r2_data2.py').read())
exec(open(R + 'work/V4_A2_ALL/r2_data3.py').read())
part = json.load(open(R + 'out/A2_parts/ALL.json'))
BR = json.load(open(R + 'out/A2_brands.json'))['b']
BL = {b['n'].lower(): b for b in BR}
LIST = W + 'List_of_shoe_styles'

def kinds(dp): return [k for s in dp['s'] for k in s['k']]
def allk(): return [(dp, k) for dp in part['depts'] for k in kinds(dp)]
def find_dept(n): return [d for d in part['depts'] if d['n'].startswith(n)][0]
def find_kind(n): return [k for dp, k in allk() if k['n'] == n][0]

# ---- 1. silhouettes ----
def merge_v(x, vs, mk):
    have = {v['n'].lower() for v in x.get('v', [])}
    x.setdefault('v', [])
    for n, y, d in vs:
        if n.lower() not in have:
            x['v'].append({'n': n, 'mk': mk, 'y': y, 'd': d})
SILALL = {}
for D in (SIL, SIL2, SIL3): SILALL.update(D)
touched = set()
for dp, k in allk():
    for x in k.get('x', []):
        key = x['n']
        if key in SILALL and not dp['n'].startswith('Traditional'):
            u = SILALL[key]
            if x.get('mk', '') == 'Reebok' and key == 'Pump': pass
            for f in ('y', 'd', 's', 'role'):
                if u.get(f): x[f] = u[f]
            if 'v' in u: merge_v(x, u['v'], x.get('mk', ''))
            if 'v_add' in u: merge_v(x, u['v_add'], x.get('mk', ''))
            touched.add(key)
print('silhouettes updated', len(touched), sorted(set(SILALL) - touched))
# roles
def setrole(kind, name, role):
    for x in find_kind(kind)['x']:
        if x['n'] == name: x['role'] = role
setrole('Basketball sneaker', 'Air Force 1', 'origin')
setrole('Heritage running sneaker', 'Cortez', 'origin')
setrole('Court sneaker', 'Stan Smith', 'landmark')
setrole('Terrace sneaker', 'Suede', 'origin')
# AF1 sits in which kind? 'Air Force 1' in Basketball sneaker; Stan Smith in Court
# Stan Smith d must carry the landmark basis
for x in find_kind('Court sneaker')['x']:
    if x['n'] == 'Stan Smith':
        x['d'] += ' Donald Dell called it the biggest-selling tennis shoe ever.'
# NB 990 series versions
nb = [x for x in find_kind('Heritage running sneaker')['x'] if x['n'] == '990 series'][0]
nb['y'] = '1982'
nb['s'] = W + 'New_Balance_99X_Series'
nb['d'] = "New Balance's premium runner, made in the USA; the 99X page numbers later models from 991 to 999 and generations v2 to v7."
vers = []
for n, y in NB99.items():
    d = ''
    if n == '990v3': d = 'led by Andrew Nyssen'
    if n in ('996', '997'): d = 'sources differ by a year'
    vers.append({'n': '990 (original)' if n == '990' else n, 'mk': 'New Balance', 'y': y, 'd': d})
nb['v'] = vers
# new entries: On, Paraboot Michael, C&J Albert
run = find_kind('Running shoe')
run['x'] += [
  {'n': 'Cloudracer', 'mk': 'On', 'y': '2012', 'd': 'Performance shoe released in 2012, the first Cloud model named on the On page.', 's': W + 'On_(company)', 'g': 'Switzerland · On'},
  {'n': 'Cloudmonster', 'mk': 'On', 'y': '2022', 'd': 'Launched on 31 March 2022 with a larger sole than earlier On designs.', 's': W + 'On_(company)', 'g': 'Switzerland · On'},
]
find_kind('Derby')['x'].append({'n': 'Michael', 'mk': 'Paraboot', 'd': 'Derby shoe that Esquire called "perhaps the most reliably stylish shoe of all time".', 's': W + 'Paraboot', 'g': 'France · Paraboot'})
for x in find_kind('Evening slipper')['x']:
    if x['n'] == 'Albert slipper':
        x['mk'] = 'Crockett & Jones'; x['d'] = "Wholecut model by Crockett & Jones that won the Diploma d'Onore in Turin in 1911."
        x['y'] = '1911'; x['s'] = W + 'Crockett_%26_Jones'; x['g'] = 'United Kingdom · Crockett & Jones'

# ---- 2. owners ----
OWNR = {}
for k, (own, y, tier, c, s) in OWN2.items(): OWNR[k] = (own, tier, y, c)
for k, (own, y, s) in OWN3.items():
    tier = 'Global group' if own in ('Kering', 'LVMH') else 'Independent'
    OWNR[k] = (own, tier, y, '')
def bcty(mk):
    b = BL.get(mk.lower()); return (b or {}).get('c', '') or ''
for dp, k in allk():
    for x in k.get('x', []):
        mk = x.get('mk', '')
        if mk in OWNR:
            own, tier, y, c = OWNR[mk]
            x['own'], x['tier'] = own, tier
            x['cty'] = c or x.get('cty') or bcty(mk)
            x.pop('own_y', None)
            if y: x['own_y'] = y
            x['g'] = (x['cty'] or 'Country not stated') + ' · ' + mk
bu = part['brand_updates']
for mk, (own, tier, y, c) in OWNR.items():
    b = BL.get(mk.lower())
    if not b: print('WARN no register', mk); continue
    bu[b['n']] = {'own': own, 'tier': tier, 'c': c or b.get('c', '')}
    if y: bu[b['n']]['own_y'] = y
newb = [
 {'n': 'Kering', 'seg': 'Luxury house', 'd': 'Owner of Gucci (1999), Balenciaga and Alexander McQueen (2001) per its Wikipedia page.', 's': W + 'Kering', 'kf': 'owner group'},
 {'n': 'LVMH', 'seg': 'Luxury house', 'd': 'Owner of Louis Vuitton (merger of 1987) and Dior (2017).', 's': W + 'LVMH', 'kf': 'owner group'},
 {'n': 'Tecnica Group', 'c': 'Italy', 'f': '1960', 'seg': 'Outdoor & technical', 'd': 'Owner of Lowa (1993) and Moon Boot, among others.', 's': W + 'Tecnica_Group', 'kf': 'owner group'},
 {'n': 'Columbia Sportswear', 'seg': 'Outdoor & technical', 'd': 'Owner of Sorel (2000), Mountain Hardwear (2003) and prAna (2014).', 's': W + 'Columbia_Sportswear', 'kf': 'owner group'},
 {'n': 'Misto Holdings', 'seg': 'Athletic & sportswear', 'd': 'Listed as the current parent of Fila on its Wikipedia page.', 's': W + 'Fila_(company)', 'kf': 'owner group'},
 {'n': 'S. C. Johnson & Son', 'seg': 'Value & basics', 'd': 'Completed the purchase of Sara Lee\'s global shoe care business, including Kiwi, in April 2011.', 's': W + 'Kiwi_(shoe_polish)', 'kf': 'owner group'},
 {'n': 'Viva Goods Company', 'seg': 'High street', 'd': 'Holds 51 % of Clarks, with the Clark family holding 49 %.', 's': W + 'Clarks_(shoe_retailer)', 'kf': 'owner group'},
]
have = {b['n'] for b in part['brands']}
for b in newb:
    if b['n'] in have: continue
    for f, v in (('c', ''), ('f', ''), ('lines', []), ('sig', []), ('rel', []), ('eras', []), ('sc', [])): b.setdefault(f, v)
    part['brands'].append(b)

# ---- 3. traditional footwear ----
trad = find_dept('Traditional')
facts = {  # name: (region, fact, kind-target)
 'Namaksin': ('Korea', 'Traditional Korean wooden shoe made for muddy and rainy conditions.'),
 'Balgha': ('North Africa (Maghreb and Egypt)', 'Heelless leather slipper worn by men and women of all social classes; called the babouche in Morocco.'),
 'Galesh': ('Iran', 'Handwoven overshoe from the northern provinces.'),
 'Pulhoer': ('Kashmir', 'Straw shoe made entirely of straw, so unusable in the wet season.'),
 'Pointinini': ("Cote d'Ivoire", 'Pointed shoe with a slightly upturned toe, made in leather, deerskin or synthetic fibre.'),
 'Tsarouchi': ('Greece', 'Stiff hand-sewn leather moccasin-style shoe topped with a woollen pompon; worn today by the Evzones of the Presidential Guard.'),
 'Pampootie': ('Aran Islands, Ireland', 'Single piece of untanned hide wrapped round the foot and stitched with twine or a leather strap.'),
 'Opinga': ('Albania', 'Single piece of leather shaped to the foot with leather or wool strips; also worn in Kosovo, North Macedonia and Montenegro.'),
 'Upanah': ('Ancient India', 'The most common footwear of ancient India, of leather, wood, wool or grass and named in the Yajurveda and Atharvaveda.'),
}
pages = {n: W + n for n in facts}
# remove the unplaced shelf, move entries to proper kinds
def kind_in(name): return [k for dp, k in allk() if k['n'] == name][0]
def pop_entry(kind, name):
    k = kind_in(kind); e = [x for x in k['x'] if x['n'] == name]
    k['x'] = [x for x in k['x'] if x['n'] != name]
    return e[0] if e else {'n': name, 's': LIST}
eur = kind_in('Named European forms'); sa = kind_in('South Asian and Middle Eastern named forms'); afr = kind_in('Named South-East Asian and African forms')
op = pop_entry('Named South-East Asian and African forms', 'Opinga'); eur['x'].append(op)
pu = pop_entry('Unplaced named forms', 'Pulhoer'); sa['x'].append(pu)
po = pop_entry('Unplaced named forms', 'Pointinini'); afr['x'].append(po)
trad['s'] = [s_ for s_ in trad['s'] if not s_['n'].startswith('Forms the list')]
afr['d'] = 'Further shoe forms of South-East Asia and Africa that Wikipedia names in its shoe-style list.'
afr['n'] = 'Named South-East Asian and African forms'
for dp, k in allk():
    if not dp['n'].startswith('Traditional'): continue
    for x in k.get('x', []):
        if x['n'] in facts:
            r, f = facts[x['n']]
            x['g'] = r; x['d'] = f; x['s'] = pages[x['n']]
        else:
            x['g'] = 'Region not stated'
    if k.get('x'):
        k['sel'] = ("Names from Wikipedia's List of shoe styles, read in full (about 190 names, no descriptions). Region and a one-line fact come from the entry's own Wikipedia page "
                    "where it was read (Namaksin, Balgha, Galesh, Pulhoer, Pointinini, Tsarouchi, Pampootie, Opinga, Upanah); every other entry is marked 'Region not stated' and has no description. "
                    "Entries that match a kind of this department are those kinds. Complete: every form of the list within scope is a kind or an entry here; sport, ballet, medical and novelty entries are out of scope.")
        k['xg'] = 'by region as stated on the entry page'
# Pulhoer lives under South Asian: keep region Kashmir

# ---- 4. market panel ----
sn = find_dept('Sneakers')
NK = 'https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/R24.htm'
for who, v in [('NIKE Brand North America', 19572), ('NIKE Brand Europe, Middle East & Africa', 12257), ('NIKE Brand Greater China', 6586), ('NIKE Brand Asia Pacific & Latin America', 6251), ('Converse', 1692), ('Nike, Inc. total', 46309)]:
    sn['ms'].append({'mkt': 'Nike, Inc. revenue by segment', 'who': who, 'share': f'US${v:,} million', 'yr': 2025, 's': NK,
                     'note': 'revenue for the year ended 31 May 2025 from Nike\'s 10-K segment note; revenue of one company, not a market share'})
AD = W + 'Adidas'
for who, sh in [('Europe', '32 %'), ('North America', '22 %'), ('Greater China', '15 %'), ('Latin America', '12 %'), ('Japan and South Korea', '6 %'), ('Others', '14 %')]:
    sn['ms'].append({'mkt': 'adidas sales by region', 'who': who, 'share': sh, 'yr': 2024, 's': AD, 'note': "share of adidas's own sales, as the Wikipedia page states; not a market share"})
ON = W + 'On_(company)'
for mkt, who, sh, yr in [('Running shoes, Switzerland', 'On', '40 %', 2019), ('Running shoes, Germany', 'On', '10 %', 2019), ('Athletic footwear, global (estimate)', 'On', '2 %', 2024)]:
    sn['ms'].append({'mkt': mkt, 'who': who, 'share': sh, 'yr': yr, 's': ON, 'note': 'as stated on the On Wikipedia page'})
sn['msum'] = ('Footwear Magazine estimates Nike at 26 % of global athletic and sneaker footwear in 2026, adidas at 14 %, Skechers at 9 % and Puma at 5 %. '
              'Nike\'s 10-K shows North America at US$19.6 billion of US$46.3 billion in revenue for the year to May 2025, and adidas reports Europe as 32 % of its 2024 sales. '
              'No third-party regional market shares for the whole category were found.')

# ---- kind sel updates ----
for dp, k in allk():
    if dp['n'].startswith('Traditional') or not k.get('x') or not k.get('sel'): continue
    sel = re.sub(r"Covers \d+ entries kept from the earlier pass and the pages read; the makers' catalogues are not exhausted\.",
                 f"Covers {len(k['x'])} entries; where a per-model Wikipedia page was read its year, designer and versions are used, and the makers' catalogues are not exhausted.", k['sel'])
    k['sel'] = sel
    xs = k['x']
    xs.sort(key=lambda x: (x['g'].startswith('Design'), x['g'], (x.get('y') or '9999')[:4], x['n']))

# ---- write ----
tmp = R + 'out/A2_parts/ALL.tmp'
json.dump(part, open(tmp, 'w'), ensure_ascii=False)
os.replace(tmp, R + 'out/A2_parts/ALL.json')
print('entries', sum(len(k.get('x') or []) for dp in part['depts'] for s in dp['s'] for k in s['k']), os.path.getsize(R + 'out/A2_parts/ALL.json'))
roles = [(k['n'], x['n']) for dp, k in allk() for x in k.get('x', []) if x.get('role')]
print(roles)
