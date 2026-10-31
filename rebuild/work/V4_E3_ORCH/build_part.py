import json, re, copy
R = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(R + 'out/E3.json'))
brands_old = {b['n'] for b in json.load(open(R + 'out/E3_brands.json'))['b']}
D = {d['n']: d for d in old['depts']}
W = 'https://en.wikipedia.org/wiki/'
HS = W + 'List_of_musical_instruments_by_Hornbostel%E2%80%93Sachs_number:_'
S_STR = W + 'List_of_Stradivarius_instruments'
S_AERO = W + 'List_of_aerophones_by_Hornbostel%E2%80%93Sachs_number'
S_REED = W + 'Reed_aerophone'
S_32, S_31, S_421 = HS + '32', HS + '31', HS + '421'
S_CHORD = W + 'List_of_chordophones_by_Hornbostel%E2%80%93Sachs_number'
report = {}

def norm(s): return re.sub(r"[\s'_\[\]\"‘’]+", ' ', s.lower()).strip()

def clean(n): return n.strip().strip('_').strip('[]').strip('_').strip()

def kind_find(dept, name):
    for s in dept['s']:
        for k in s['k']:
            if k['n'] == name: return k
    raise KeyError(name)

# ---------------------------------------------------------------- ORCHESTRAL
o = copy.deepcopy(D['Orchestral & band instruments'])
OWN_LABEL = {'Thomann', 'Startone'}
removed_o = []; made_o = 0; vers_o = 0

def model_to_entry(k, name, maker, dept_label):
    """loose model -> version of a matching entry or a new entry"""
    global made_o, vers_o
    full = name if (maker and maker.lower().split()[0] in name.lower()) or not maker else f'{maker} {name}'
    nf = norm(full)
    for e in k.get('x', []):
        ne = norm(e['n'])
        if nf == ne: return
        if nf.startswith(ne) or ne.startswith(nf) or (len(nf) > 4 and nf in ne):
            e.setdefault('v', []).append({'n': full, 'mk': maker, 'y': '', 'd': ''}); vers_o += 1; return
    k.setdefault('x', []).append({'n': full, 'a': '', 'd': f'{maker} model of the {k["n"].lower()}.' if maker else f'Named model of the {k["n"].lower()}.',
                                  'mk': maker, 'y': '', 's': k.get('s', ''), 'v': []})
    made_o += 1

for s in o['s']:
    for k in s['k']:
        for m in k.pop('m', []) or []:
            if m[1] in OWN_LABEL:
                removed_o.append(f'{m[0]} ({m[1]}, retailer own label)'); continue
            model_to_entry(k, m[0], m[1], 'o')

# violin makers
violin = kind_find(o, 'Violin'); viola = kind_find(o, 'Viola'); cello = kind_find(o, 'Cello')
dbass = kind_find(o, 'Double bass')

STR_VIOLIN_EARLY = """Alumnas Amati, Ashby, Silvestre, Serdet|1666
ex-Sachs|c. 1666
ex Back|c. 1666
Aranyi|1667
Dubois|1667
ex-Captain Saville|1667
Ex Jenkins, Jenkins-Thompson|1667
Piet – Beare-Biddulph|1667
Amatese|1668
Canadian|1668
Golden Bell|c. 1668
Clisbee, Francalucci|1669
Hill|1669
Oistrakh|1671
Sellière|1672
Spanish; ex-Faltin|1678
Hellier|1679
Paganini-Desaint|1680
Fleming|1681
Bucher|1683
Derpinina|1683
Cipriani Potter|1683
Cobbett; ex-Holloway|1683
ex-Croall|1684
ex-Elphinstone|1684
The Marquis|1685
ex-Arma Senkrah|1685
ex-Castelbarco|1685
Eugenie, ex-Mackenzie|1685
ex-Nachez|1686
Rosenheim|1686
Goddard|1686
Ex Bello, Marie Law|1687
Ole Bull|1687
Mercur-Avery|1687
Baumgartner|1689
Arditi|1689
Spanish I|c. 1689
Spanish II|c. 1689
Ex-Leopold Auer|1690
Bingham|1690
Theodor|1690
Boissier-Sarasate|1690
Ex-Ries|1691
Czar of Russia, Albrecht, Avery Fisher|1692
Guttmann|1692
Bennett|1692
Falmouth|1692
Queux de Saint-Hilaire|c. 1692
Gould|1693
Harrison|1693
Baillot–Pommerau|1694
ex-Halíř|1694
Francesca|1694
Rutson|1694
Fetzer|1695
Lincoln|1695
ex-Kym|1696
Haddock, Cator, Rostal|1697
Paganini|1697
Molitor|1697
Cecilia C A (Capitulum Agriense)|1697
Cabriac|1698
Baron Knoop|1698
Joachim-Kortschak-Field|1698
Duc de Camposelice|1699
Lady Tennant; Lafont|1699
Countess Polignac|1699
Castelbarco|1699
Kustendyke|1699
Crespi|1699
ex-Berglund|1699
ex-Beatrice Mulgan|1699"""
STR_VIOLIN_LATE = """Berger|1700
The Penny|1700
Petri|1700
Dragonetti|1700
Jupiter|1700
Russian, Margaret, Berson|1700
Taft; ex-Emil Heermann|1700
Circle, Nachez|1701
Court Strad|1701
Deveault|1701
Dushkin, Sandler|1701
Ferraresi|1701
Kreutzer, von Hautem|1701
Markees|1701
Brodsky|1702
Irish|1702
Conte de Fontana; ex-Oistrakh|1702
De La Taille|1702
La Rouse Boughton|1703
Allegretti|1703
Alsager|1703
Aurora, ex-Foulis|1703
Cobbett, Dickson-Poynder|1703
Emiliani|1703
Ford|1703
Lady Harmsworth|1703
de Rougemont, Gordon, Hart|1703
Rynberger, Prince Friedrich Wilhelm of Prussia|1703
Schoofs, Vidoudez, Huber, Steiner-Schweitzer|1703
Betts|1704
Davidoff|1708
Viotti; ex-Bruce|1709
The Antonius|1711
Viotti|1712
Boissier-Sarasate|1713
Lady Ley|1713
Dolphin (Delfino)|1714
Soil|1714
Hubermann|1714
Titian|1715
Messiah|1716
Lady Blunt|1721
Lady Jeanne|1731
Herkules; Ysaÿe; ex-Szeryng|1734"""
STR_VIOLA = """Mahler|1672
Tuscan-Medici Tenor|1690
Tuscan-Medici|1690
Axelrod|1695
Archinto|1696
Spanish Court|1696
Lux; Castelbarco|1714
The Russian|1715
MacDonald|1719
Cassavetti|1727
Paganini-Mendelssohn|1731"""
STR_CELLO = """ex Vatican Stradivarius|1703
ex-Du Pré; ex-Harrell|1673
General Kyd; ex-Leo Stern|1684
Marylebone|1688
Medici|1690
Barjansky|1690
ex-Gendron; ex-Lord Speyer|1693
Spanish Court or Decorado|1694
Bonjour|1696
Lord Aylesford|1696
Cholmondeley Cello|1698
Castelbarco|1699
Bajo Palatino|1700
Stauffer; ex-Cristiani|1700
Servais|1701
Paganini-Countess of Stanlein|1707
Boni-Hegar|1707
Boccherini; Romberg|1709
Markevitch; Delphino|1709
Gore Booth; Baron Rothschild|1710
Duport|1711
Mara|1711
Batta-Piatigorsky|1714
de Vaux|1717
Amaryllis Fleming|1717
Becker|1719
Piatti|1720
Vaslin, La Belle Blonde|1723
Yusupov|1736
Paganini-Ladenburg|1736"""

def ysort(v):
    m = re.search(r'\d{4}', v['y']); return (int(m.group()) if m else 9999, v['n'])

def add_versions(entry, rows, typ, mk, seen=None):
    have = {norm(v['n']) for v in entry.get('v', [])}
    n = 0
    for line in rows.split('\n'):
        nm, y = line.split('|')
        if norm(nm) in have: continue
        have.add(norm(nm))
        entry.setdefault('v', []).append({'n': nm, 'mk': mk, 'y': y, 'd': typ}); n += 1
    return n

def ent(k, name):
    for e in k['x']:
        if e['n'] == name: return e
    raise KeyError(name)

strad = ent(violin, 'Stradivari pattern')
strad['a'] = 'Strad · Stradivarius · Stradivari pattern · Strad model'
strad['n'] = 'Antonio Stradivari'
strad['d'] = 'Cremonese maker, c. 1644-1737; his violin outline is the model most modern violins copy.'
strad['y'] = 'c. 1666–1737'
strad['s'] = S_STR
strad['role'] = 'origin'
strad['v'] = [v for v in strad['v'] if 'Golden-period violins' not in v['n']]
nv1 = add_versions(strad, STR_VIOLIN_EARLY, 'violin', 'Antonio Stradivari')
nv2 = add_versions(strad, STR_VIOLIN_LATE, 'violin', 'Antonio Stradivari')
strad['v'].sort(key=ysort)
n_str_violin = nv1 + nv2

gdg = ent(violin, 'Guarneri del Gesù pattern')
gdg['n'] = 'Giuseppe Guarneri del Gesù'; gdg['a'] = 'Guarneri del Gesù · del Gesù model · Guarneri copy'
gdg['d'] = "Cremonese maker, 1698-1744; his bolder violins are prized for a darker, more robust tone."
gdg['s'] = W + 'Giuseppe_Guarneri'; gdg['y'] = '1698–1744'
add_versions(gdg, "Il Cannone|1743\nLord Wilton|1742\nVieuxtemps Guarneri|1741\nOle Bull|1744", 'violin', 'Giuseppe Guarneri del Gesù')
# drop duplicates written with quotes
seen = set(); nv = []
for v in gdg['v']:
    if norm(v['n']) in seen: continue
    seen.add(norm(v['n'])); nv.append(v)
gdg['v'] = sorted(nv, key=ysort)

am = ent(violin, 'Amati pattern')
am['n'] = 'Amati'; am['a'] = 'Amati pattern · Amati model'
am['d'] = 'Cremonese family of makers from Andrea Amati (c. 1505-1577) to Girolamo II (1649-1740); the first Cremona violin school.'
am['s'] = W + 'Amati'; am['y'] = 'c. 1505–1740'; am['role'] = 'origin'
have = {norm(v['n']) for v in am['v']}
for nm in ['The King', 'The Henry IV', 'The Medici', 'The Crocifisso', 'The Witten', 'The IX Charles']:
    if norm(nm) not in have:
        am['v'].append({'n': nm, 'mk': 'Amati', 'y': '', 'd': 'named Amati instrument on the Amati page'})

violin['x'].append({'n': 'Jacob Stainer', 'a': 'Stainer model · Absam school', 'd': 'Tyrolean maker, c. 1618-1683, working in Absam; his violins set the German and Austrian model.',
                    'mk': 'Jacob Stainer', 'y': 'c. 1618–1683', 's': W + 'Jacob_Stainer', 'v': [], 'g': 'Tyrol'})
violin['x'].append({'n': 'Jean-Baptiste Vuillaume', 'a': 'Vuillaume copy', 'd': 'French maker, 1798-1875, whose Paris workshop made more than 3,000 instruments, including exact copies of Cremonese violins.',
                    'mk': 'Jean-Baptiste Vuillaume', 'y': '1798–1875', 's': W + 'Jean-Baptiste_Vuillaume',
                    'v': [{'n': 'Il Cannone copy', 'mk': 'Jean-Baptiste Vuillaume', 'y': '', 'd': 'copy of the Guarneri del Gesù violin'},
                          {'n': 'Messiah copy', 'mk': 'Jean-Baptiste Vuillaume', 'y': '', 'd': 'copy of the Stradivari Messiah'}], 'g': 'France'})
# assign sections
for e in violin['x']:
    e['g'] = {'Antonio Stradivari': 'Cremona', 'Giuseppe Guarneri del Gesù': 'Cremona', 'Amati': 'Cremona'}.get(e['n'], e.get('g', 'Cremona'))
for e in violin['x']:
    e.pop('dt', None) if False else None
# strad viola / cello
sv = ent(viola, 'Stradivari viola'); sv['s'] = S_STR; sv['g'] = 'Cremona'
n_str_viola = add_versions(sv, STR_VIOLA, 'viola', 'Antonio Stradivari'); sv['v'].sort(key=ysort)
sc = ent(cello, 'Stradivari cello'); sc['s'] = S_STR; sc['g'] = 'Cremona'
n_str_cello = add_versions(sc, STR_CELLO, 'cello', 'Antonio Stradivari'); sc['v'].sort(key=ysort)
dbass['x'].append({'n': 'Vuillaume octobass', 'a': 'octobasse', 'd': "Vuillaume's giant three-string bass, taller than a double bass.", 'mk': 'Jean-Baptiste Vuillaume',
                   'y': '', 's': W + 'Jean-Baptiste_Vuillaume', 'v': [], 'g': 'France'})

# grouping field g for all orchestral entries: maker or school
for s in o['s']:
    for k in s['k']:
        for e in k.get('x', []):
            if not e.get('g'):
                e['g'] = e.get('mk') or 'Pattern or school'
        if k.get('x'): k['x'].sort(key=lambda e: (e['g'], e['n']))

# badges: origin / landmark from data already on the page
for s in o['s']:
    for k in s['k']:
        for e in k.get('x', []):
            if e['n'] == 'Selmer Mark VI': e['role'] = 'landmark'
# Strad mandolins: put into folk Mandolin later
STR_MAND = [('Lauterbach', '1719'), ('Ex-Kavakos', '1724'), ('Cutler-Challen Choral Mandolino', '1680')]

# kind metadata for orchestral
total_str = n_str_violin + n_str_viola + n_str_cello + 3  # three mandolins added in folk part
o_meta = {
    'Violin': ('One entry is a historical violin maker or school; the instruments the reference names are its versions.',
               "Follows Wikipedia's List of Stradivarius instruments and the maker pages for Guarneri del Gesù, Amati, Stainer and Vuillaume. Modern maker lines are entries too. "),
    'Viola': ('One entry is a viola maker or school; named instruments are versions.', "Follows Wikipedia's List of Stradivarius instruments for the Stradivari violas. "),
    'Cello': ('One entry is a cello maker or school; named instruments are versions.', "Follows Wikipedia's List of Stradivarius instruments for the Stradivari cellos. "),
}
generic_nl = {
    'Orchestral strings': 'One entry is a maker, school or model line of the instrument; revisions are versions.',
}
FLUTE_SEL = 'Follows the maker model lines named on the cited page for each entry; student lines are entries where the page lists them. '
for s in o['s']:
    for k in s['k']:
        if not k.get('x'): continue
        if k['n'] in o_meta:
            nl, sel = o_meta[k['n']]
        else:
            nl = 'One entry is a maker model line named on a fetched page; generations and sizes are versions.'
            sel = 'Follows the maker model lines named on the cited page of each entry; student lines are included where the page lists them. '
        k['nl'] = nl; k['sel'] = sel
        k['xg'] = 'maker or school'
orch_counts = {'Violin Stradivari versions': n_str_violin}
violin['sel'] += (f"Covers {n_str_violin} Stradivari violins from the list (every row the page extract returned; the list is much longer and the extraction dropped part of the 1703-1731 rows), the Guarneri del Gesù instruments the maker page names, and the named Amati instruments; "
                  "the list's other Strad violins are not listed.")
viola['sel'] += f'Covers {n_str_viola} of the 11 violas in the list.' if False else f'Covers {n_str_viola} Stradivari violas of the violas the list tabulates (11 rows returned).'
cello['sel'] += f'Covers {n_str_cello} Stradivari cellos of the cellos the list tabulates (30 rows returned).'
o['note'] = 'Kind → maker or model line (Stradivari, Selmer Mark VI, Bach Stradivarius) → version (named instrument, revision) → detail.'
# fill missing kind-level nl/sel for entry-less kinds: nothing to add

orch_part = o

# ---------------------------------------------------------------- FOLK
f = copy.deepcopy(D['Folk & world instruments'])
REG_DEFAULT = {'Ukulele': 'Oceania', 'Cavaquinho': 'Europe', 'Banjo': 'Americas', 'Mandolin': 'Europe', 'Bouzouki': 'Europe', 'Balalaika': 'Europe', 'Charango': 'Americas',
 'Bağlama (saz)': 'Middle East & North Africa', 'Oud': 'Middle East & North Africa', 'Sitar': 'South Asia', 'Tanpura': 'South Asia', 'Veena': 'South Asia', 'Pipa': 'East Asia',
 'Shamisen': 'East Asia', 'Kora': 'Sub-Saharan Africa', 'Kantele': 'Europe', 'Autoharp': 'Americas', 'Appalachian dulcimer': 'Americas', 'Hammered dulcimer': 'Europe',
 'Koto': 'East Asia', 'Guzheng': 'East Asia', 'Hardanger fiddle': 'Europe', 'Nyckelharpa': 'Europe', 'Hurdy-gurdy': 'Europe', 'Erhu': 'East Asia', 'Sarangi': 'South Asia',
 'Taus': 'South Asia', 'Kokyu': 'East Asia', 'Piano accordion': 'Europe', 'Button accordion': 'Europe', 'Bandoneon': 'Europe', 'Concertina': 'Europe', 'Harmonium': 'Europe',
 'Shruti box': 'South Asia', 'Diatonic harmonica': 'Europe', 'Chromatic harmonica': 'Europe', 'Melodica': 'Europe', 'Sheng': 'East Asia', 'Bagpipes': 'Europe', 'Tin whistle': 'Europe',
 'Native American flute': 'Americas', 'Ocarina': 'Europe', 'Shakuhachi': 'East Asia', 'Ney': 'Middle East & North Africa', 'Pan flute': 'Europe', 'Bansuri': 'South Asia', 'Dizi': 'East Asia',
 'Duduk': 'Middle East & North Africa', 'Hichiriki': 'East Asia', 'Didgeridoo': 'Oceania', 'Jaw harp': 'Europe', 'Music box': 'Europe', 'Barrel organ': 'Europe', 'Musical saw': 'Americas',
 'Glass harmonica': 'Americas', 'Omnichord': 'East Asia', 'Stylophone': 'Europe'}
REG_ENTRY = {'Cajun accordion': 'Americas', 'Bayan': 'Europe', 'Indian santoor': 'South Asia', 'Yangqin': 'East Asia', 'Concert cimbalom': 'Europe', 'Siku': 'Americas',
 'Khomus': 'Central Asia', 'Morsing': 'South Asia', 'Yamaha Pianica': 'East Asia', 'Suzuki Melodion': 'East Asia', 'Suzuki harmonicas': 'East Asia', 'Persian barbat': 'Middle East & North Africa',
 'Irish bouzouki': 'Europe', 'Franklin glass armonica': 'Americas', 'Stradivarius saw': 'Americas', 'Speliplari': 'Europe', 'Suzuki Omnichord OM-27': 'East Asia',
 'Saraswati veena': 'South Asia', 'Tsugaru shamisen': 'East Asia', 'Hohner Melodica': 'Europe', 'Steirische Harmonika': 'Europe', 'Alfred Arnold (AA) bandoneon': 'Europe',
 'Gibson F-5': 'Americas', 'Gibson Mastertone resonator banjo': 'Americas', 'Vega Tu-ba-Phone': 'Americas', 'Vega Pete Seeger long-neck': 'Americas', 'Vega cylinder-back mandolin': 'Americas',
 'Andreyev orchestral balalaika': 'Europe', 'Ravi Shankar style sitar': 'South Asia', 'Vilayat Khan style sitar': 'South Asia', 'Miraj tanpura': 'South Asia', 'Tanjore tanpura': 'South Asia',
 'Concert kantele': 'Europe', 'Fuke shakuhachi': 'East Asia', 'Romanian nai': 'Europe', 'Syrinx': 'Europe', 'Great Highland bagpipe': 'Europe',
 'Galician gaita': 'Europe', 'Uilleann pipes': 'Europe', 'Zimmermann autoharp': 'Americas', 'Oscar Schmidt autoharp': 'Americas', 'Orthey Autoharp No. 136': 'Americas', 'Courting dulcimer': 'Americas'}

FOLK_OK_MAKERS = {'Wheatstone', 'Lachenal', 'Paolo Soprani', 'Scandalli', 'Hohner', 'Seydel', 'Suzuki', 'Symphonion', 'Polyphon', 'Regina', 'Reuge', 'Giuseppe Donati', 'John Taylor',
                  'Hiren Roy', 'Rikhi Ram', 'August Bohlin', 'Eric Sahlström', 'Gibson', 'Antoine Favre-Salomon', 'Peter Harlan', 'Richard Pockrich', 'Francis Hopkinson Smith', 'Bruno Hoffmann', 'Mason & Hamlin', 'Estey'}
removed_f = []; made_f = 0
def kind_region(kn): return REG_DEFAULT.get(kn, 'Europe')
for s in f['s']:
    for k in s['k']:
        ms = k.pop('m', []) or []
        k.pop('r', None) if False else None
        for nm, mk in ms:
            if mk in FOLK_OK_MAKERS or mk == '':
                if mk == '' and nm in ('Iraqi school', 'Syrian oud', 'Egyptian oud'):
                    k.setdefault('x', []).append({'n': nm, 'a': '', 'd': 'Regional school of oud making.', 'mk': '', 'y': '', 's': k['s'], 'v': [], 'g': 'Middle East & North Africa'}); made_f += 1; continue
                nf = norm(nm)
                if any(norm(e['n']) == nf for e in k.get('x', [])): continue
                if any(nf in norm(e['n']) or norm(e['n']) in nf for e in k.get('x', [])) and mk:
                    tgt = [e for e in k['x'] if nf in norm(e['n']) or norm(e['n']) in nf][0]
                    tgt.setdefault('v', []).append({'n': nm, 'mk': mk, 'y': '', 'd': ''}); continue
                k.setdefault('x', []).append({'n': nm, 'a': '', 'd': f'{mk} {k["n"].lower()} model or system.' if mk else f'{k["n"]} form.', 'mk': mk, 'y': '', 's': k['s'], 'v': []}); made_f += 1
            else:
                removed_f.append(f'{nm} ({mk})')
        # regions
        for e in k.get('x', []):
            e['g'] = e.get('g') or REG_ENTRY.get(e['n']) or kind_region(k['n'])

def sec(shelf):
    return next(s for s in f['s'] if s['n'] == shelf)

def add_rows(k, rows, src, tp):
    """rows: list of (name, region, alias, desc)"""
    global made_f
    have = {norm(e['n']) for e in k.get('x', [])}
    n = 0
    for name, region, alias, desc in rows:
        if norm(name) in have: continue
        have.add(norm(name)); n += 1
        k.setdefault('x', []).append({'n': name, 'a': alias, 'd': desc, 'mk': '', 'y': '', 's': src, 'v': [], 'g': region})
    made_f += n
    return n

def new_kind(shelf, name, d, rows, src, tt=None, see=None, nl=None, xg='region of origin'):
    k = {'n': name, 'a': '', 'd': d, 's': src, 'x': [], 'nl': nl or 'One entry is an instrument type named in the reference list; regional variants are versions.',
         'xg': xg}
    if tt: k['tt'] = tt
    if see: k['see'] = see
    add_rows(k, rows, src, '')
    sec(shelf)['k'].append(k)
    return k

ME = 'Middle East & North Africa'; AF = 'Sub-Saharan Africa'; SA = 'South Asia'; EA = 'East Asia'; SEA = 'Southeast Asia'; CA = 'Central Asia'; EU = 'Europe'; AM = 'Americas'; OC = 'Oceania'; NS = 'Region not stated'

# --- additions to existing kinds
def to(kn, rows, src):
    k = None
    for s in f['s']:
        for kk in s['k']:
            if kk['n'] == kn: k = kk
    return add_rows(k, rows, src, '')
mand = kind_find(f, 'Mandolin')
to('Mandolin', [('Mandola', EU, 'tenor mandolin', 'Larger, lower-pitched member of the mandolin family.'), ('Octave mandolin', EU, '', 'Mandolin-family instrument pitched an octave below the mandolin.'),
               ('Mandocello', EU, '', 'Cello-range member of the mandolin family.'), ('Mandobass', EU, '', 'Bass member of the mandolin family.')], S_32)
for nm, y in STR_MAND:
    pass
mand['x'].append({'n': 'Antonio Stradivari mandolins', 'a': 'Stradivari mandolino', 'd': 'Mandolins made in the Stradivari workshop; the list names three.', 'mk': 'Antonio Stradivari', 'y': '1680–1724',
                  's': S_STR, 'g': EU, 'v': [{'n': nm, 'mk': 'Antonio Stradivari', 'y': y, 'd': 'mandolin'} for nm, y in sorted(STR_MAND, key=lambda t: t[1])]})
to('Charango', [('Charangon', AM, '', 'Large, lower-pitched charango.'), ('Hatun charango', AM, '', 'Large charango.'), ('Hualaycho', AM, '', 'Small, high-pitched charango.'), ('Ronroco', AM, '', 'Large Andean charango-family instrument.')], S_32)
to('Pipa', [('Đàn tỳ bà', SEA, 'Vietnamese pipa', 'Vietnamese lute of the pipa type.')], S_32)
to('Hammered dulcimer', [('Santur', ME, 'santoor · santur', 'Hammered dulcimer of Iran and neighbouring regions.'), ('Khim', SEA, '', 'Hammered dulcimer of Thailand.')], S_32)
to('Melodica', [('Accordina', EU, '', 'Blown free-reed instrument with accordion-style buttons.')], S_AERO)
to('Pan flute', [('Diple', EU, '', 'Double flute listed with pan flutes.'), ('Paixiao', EA, '', 'Chinese pan flute.')], S_421)

# --- new kinds, shelf 1
SH1 = 'Plucked lutes & fretted strings'
new_kind(SH1, 'European lutes & citterns', 'Plucked European lutes, citterns and Ukrainian and Russian folk lutes listed in the lute class of the H-S system.',
  [('Cittern', EU, '', 'Wire-strung plucked lute of Renaissance Europe.'), ('Archlute', EU, '', 'Baroque lute with extended bass strings.'), ('Theorbo', EU, '', 'Large bass lute with a second pegbox.'),
   ('Laud', EU, '', 'Spanish plucked lute listed in the lute class.'), ('Kobza', EU, '', 'Ukrainian plucked lute.'), ('Bandura', EU, '', 'Ukrainian plucked lute-zither.'), ('Torban', EU, '', 'Ukrainian bass lute.'),
   ('Domra', EU, '', 'Russian long-necked plucked lute.')], S_32, tt=[['Origin', ['Renaissance', 'Baroque', 'Folk']]], see=[['E3', 'Lute', 'the early lute']])
new_kind(SH1, 'Asian plucked lutes', 'Plucked lutes of Vietnam, China, Okinawa and the Philippines that are not covered by a kind of their own.',
  [('Đàn đáy', SEA, '', 'Long-necked Vietnamese lute.'), ('Đàn nguyệt', SEA, 'moon lute', 'Vietnamese moon lute.'), ('Sanxian', EA, '', 'Three-stringed Chinese long-necked lute.'),
   ('Sanshin', EA, '', 'Okinawan three-stringed lute.'), ('Kutiyapi', SEA, '', 'Boat lute of the southern Philippines.')], S_32)
new_kind(SH1, 'African lutes & harp-lutes', 'West African plucked lutes and harp-lutes other than the kora.',
  [('Xalam', AF, 'khalam', 'West African plucked lute.'), ('Seperewa', AF, '', 'Ghanaian harp-lute.')], S_32)
new_kind(SH1, 'Lyres', 'Plucked lyres, with strings from a yoke fixed to the body.', [('Lyre', EU, '', 'Ancient and later European lyre.')], S_32)

# --- shelf 2
SH2 = 'Harps, zithers & dulcimers'
new_kind(SH2, 'Tube zithers & long zithers', 'Zithers with a vaulted or tube string bearer, from Madagascar to East Asia.',
  [('Valiha', AF, '', 'Tube zither of Madagascar.'), ('Ajaeng', EA, '', 'Korean bowed long zither.'), ('Đàn tranh', SEA, '', 'Vietnamese long zither.'), ('Gayageum', EA, '', 'Korean long zither.'),
   ('Geomungo', EA, '', 'Korean plucked long zither.'), ('Guqin', EA, '', 'Chinese seven-string long zither.')], S_32,
  see=[['E3', 'Koto', 'Japanese long zither'], ['E3', 'Guzheng', 'Chinese long zither']])
new_kind(SH2, 'Raft zithers', 'Zithers whose string bearer is a raft of canes.',
  [('Adjalin', AF, '', 'West African zither of Benin.'), ('Kacapi', SEA, '', 'Indonesian zither.')], S_CHORD)
new_kind(SH2, 'Board & trough zithers', 'Zithers on a board, a box or a trough, plucked or struck.',
  [('Gusli', EU, '', 'Russian trough zither.'), ('Pantalon', EU, '', 'Large German hammered dulcimer.'), ('Psaltery', EU, '', 'Medieval plucked box zither.'),
   ('Qanun', ME, 'kanun · qanun', 'Plucked board zither of the Middle East.'), ('Shahi baaja', SA, '', 'Indian zither with a keyboard.'), ('Swarmandal', SA, '', 'Indian plucked board zither.'),
   ('Tambourin de Béarn', EU, '', 'Gascon string drum, a board zither.'), ('Tautirut', AM, '', 'Inuit board zither.'), ('Aeolian harp', EU, '', 'Zither sounded by the wind.'),
   ('Overtone zither', EU, '', 'Zither listed in the simple chordophone class.')], S_CHORD)
new_kind(SH2, 'Musical bows & stick zithers', 'Zithers on a bar or a flexible stick.', [('Musical bow', AF, '', 'Hunting-bow shape sounded as a string instrument.'), ('Mvet', AF, '', 'Stick zither of Gabon, Cameroon and Guinea.')], S_CHORD)
new_kind(SH2, 'World harps', 'Harps of Africa, ancient Greece and the Celtic regions.', [('African harp', AF, '', 'Harps of Africa.'), ('Ancient Greek harp', EU, '', 'Harp of ancient Greece.'), ('Celtic harp', EU, '', 'Harp of Ireland and Scotland.')], S_32,
         see=[['E3', 'Harp', 'orchestral harp']])

# --- shelf 3
SH3 = 'Bowed & wheel strings'
new_kind(SH3, 'Spike fiddles', 'Bowed lutes from the Middle East and Mongolia not covered by a kind of their own.', [('Kamancheh', ME, '', 'Persian spike fiddle.'), ('Morin khuur', CA, 'horsehead fiddle', 'Mongolian horsehead fiddle.')], S_CHORD)
new_kind(SH3, 'European bowed lutes', 'Bowed lutes of medieval and baroque Europe.', [('Vielle', EU, '', 'Medieval European fiddle.'), ("Viola d'amore", EU, '', 'Baroque bowed lute with sympathetic strings.')], S_32,
         see=[['E3', 'Viola da gamba', 'bowed viol']])

# --- shelf 4
SH4 = 'Accordions & free reeds'
new_kind(SH4, 'Free-reed pipes', 'Mouth-blown pipes with free reeds, from China.', [('Bawu', EA, '', 'Chinese free-reed pipe held sideways.'), ('Hulusi', EA, '', 'Chinese gourd free-reed pipe.')], S_REED)

# --- shelf 5
SH5 = 'Pipes, flutes & folk winds'
new_kind(SH5, 'End-blown flutes', 'End-blown flutes of every region, listed in the open end-blown flute class.',
  [('Anasazi flute', AM, '', 'Ancestral Puebloan end-blown flute.'), ('Danso', EA, '', 'Korean end-blown flute.'), ('Hotchiku', EA, '', 'Japanese bamboo flute related to the shakuhachi.'),
   ('Kaval', EU, '', 'Balkan end-blown flute.'), ('Nose flute', OC, '', 'Flute blown with the nose.'), ('Palendag', SEA, '', 'Philippine end-blown flute.'), ('Quena', AM, '', 'Andean end-blown notched flute.'),
   ('Sring', SEA, '', 'Indonesian end-blown flute.'), ('Suling', SEA, '', 'Indonesian bamboo flute.'), ('Tungso', EA, '', 'Korean end-blown flute.'), ('Washint', AF, '', 'Ethiopian end-blown flute.'),
   ('Xiao', EA, '', 'Chinese end-blown flute.')], S_421, see=[['E3', 'Shakuhachi', 'Japanese end-blown flute'], ['E3', 'Ney', 'Middle Eastern end-blown flute']])
new_kind(SH5, 'Transverse flutes', 'Side-blown flutes of East Asia, South Asia and Europe, beside the concert flute.',
  [('Chi', EA, '', 'Chinese transverse flute.'), ('Daegeum', EA, '', 'Large Korean transverse flute.'), ('Dangjeok', EA, '', 'Korean transverse flute.'), ('Junggeum', EA, '', 'Medium Korean transverse flute.'),
   ('Sogeum', EA, '', 'Small Korean transverse flute.'), ('Fife', EU, '', 'Small military transverse flute.'), ('Gakubue', EA, '', 'Japanese court flute.'), ('Kagurabue', EA, '', 'Japanese Shinto flute.'),
   ('Komabue', EA, '', 'Japanese court flute.'), ('Ryuteki', EA, '', 'Japanese gagaku dragon flute.'), ('Seiteki', EA, '', 'Japanese transverse flute.'), ('Shinobue', EA, '', 'Japanese folk flute.'),
   ('Nohkan', EA, '', 'Japanese flute of Noh theatre.'), ('Minteki', EA, '', 'Japanese transverse flute.'), ('Koudi', EA, '', 'Chinese transverse flute.'), ('Sáo', SEA, '', 'Vietnamese bamboo flute.'),
   ('Paidi', EA, '', 'Chinese transverse flute.'), ('Limbe', NS, '', 'Transverse flute listed in the reference.')], S_421, see=[['E3', 'Flute', 'concert flute'], ['E3', 'Bansuri', 'Indian flute'], ['E3', 'Dizi', 'Chinese flute']])
new_kind(SH5, 'Fipple flutes & whistles', 'Duct flutes and whistles other than the tin whistle and ocarina.',
  [('Atenben', AF, '', 'Ghanaian bamboo flute.'), ('Flageolet', EU, '', 'Small European duct flute.'), ('Double flageolet', EU, '', 'Two flageolets played together.'), ('Fujara', EU, '', 'Large Slovak shepherd flute.'),
   ('Khlui', SEA, '', 'Thai duct flute.'), ('Khloy', SEA, '', 'Duct flute (alternate spelling in the reference).'), ('Tonette', AM, '', 'Plastic school flute.'), ('Gemshorn', EU, '', 'Flute made from a chamois horn.'),
   ("Boatswain's call", EU, '', 'Naval pipe.')], S_421, see=[['E3', 'Recorder', 'orchestral recorder'], ['E3', 'Tin whistle', 'Irish whistle']])
new_kind(SH5, 'Double-reed folk pipes', 'Shawms and related double-reed pipes.',
  [('Piri', EA, '', 'Korean double-reed pipe.'), ('Hne', SEA, '', 'Burmese double-reed pipe.'), ('Shawm', EU, '', 'Medieval double-reed pipe.'), ('Taepyeongso', EA, '', 'Korean conical double-reed pipe.'),
   ('Cornamuse', EU, '', 'Renaissance double-reed pipe.'), ('Crumhorn', EU, '', 'Renaissance capped double-reed pipe.')], S_REED, see=[['E3', 'Oboe', 'orchestral oboe']])
new_kind(SH5, 'Single-reed folk pipes', 'Single-reed pipes, from the alboka to the tárogató, including clarinet-family folk forms.',
  [('Albogue', EU, '', 'Iberian single-reed pipe.'), ('Alboka', EU, '', 'Basque single-reed horn pipe.'), ('Arghul', ME, '', 'Egyptian double clarinet with a drone.'), ('Chalumeau', EU, '', 'Baroque single-reed pipe, ancestor of the clarinet.'),
   ('Diplica', EU, '', 'Croatian double single-reed pipe.'), ('Hornpipe', EU, '', 'Single-reed pipe with a horn bell.'), ('Pibgorn', EU, '', 'Welsh single-reed pipe.'), ('Saxonette', AM, '', 'Single-reed instrument listed with clarinets.'),
   ('Sipsi', ME, '', 'Turkish single-reed pipe.'), ('Xaphoon', AM, '', 'Single-reed pocket instrument.'), ('Zhaleika', EU, '', 'Russian single-reed pipe.'), ('Tárogató', EU, '', 'Hungarian single-reed folk and concert pipe.'),
   ('Heckel-clarina', EU, '', 'Single-reed instrument listed in the reference.'), ('Heckelphone-clarinet', EU, '', 'Single-reed instrument listed in the reference.'), ('Octavin', EU, '', 'Single-reed instrument listed in the reference.'),
   ('Launeddas', EU, '', 'Sardinian triple clarinet.'), ('Mijwiz', ME, '', 'Levantine double clarinet.'), ('Double clarinet', NS, '', 'Pair of clarinets joined.'), ('Aulochrome', EU, '', 'Modern double-saxophone instrument.'),
   ('Sneng', NS, '', 'Single-reed instrument listed in the reference.')], S_REED, see=[['E3', 'Clarinet', 'orchestral clarinet'], ['E3', 'Saxophone', 'saxophone']])
new_kind(SH5, 'Natural horns & trumpets', 'Lip-vibrated horns and trumpets without valves.',
  [('Natural trumpet', EU, '', 'Valveless trumpet.'), ('Conch shell', OC, '', 'Shell trumpet.'), ('Shofar', ME, '', 'Ram horn of Jewish tradition.'), ('Bugle', EU, '', 'Valveless military horn.'), ('Ophicleide', EU, '', 'Keyed brass bass of the 19th century.')],
  S_AERO, see=[['E3', 'Trumpet', 'orchestral trumpet'], ['E3', 'Cornett', 'early cornett']])
# --- shelf 6
SH6 = 'Mechanical & novelty instruments'
new_kind(SH6, 'Stringed novelties', 'Modern and novelty strung instruments from the zither and lute lists.',
  [('Marxophone', AM, '', 'Fretless zither with hammers.'), ('Harpejji', AM, '', 'Modern tapped string instrument.'), ('Moodswinger', EU, '', 'Modern multi-string zither.'), ('Washtub bass', AM, '', 'Folk bass made from a washtub, string and pole.')],
  S_32)
# keyboard zithers stay in Keyboards
# nl/sel/xg for existing kinds with entries
for s in f['s']:
    for k in s['k']:
        if k.get('x'):
            k.setdefault('nl', 'One entry is an instrument type, regional form or notable maker line; variants are versions.')
            k.setdefault('xg', 'region of origin')
            k['x'].sort(key=lambda e: (e['g'], e['n']))
    # sel
SEL_FOLK = {SH1: S_32, SH2: S_31, SH3: S_32, SH4: S_AERO, SH5: S_421, SH6: S_32}
for s in f['s']:
    for k in s['k']:
        if not k.get('x'): continue
        if k.get('sel'): continue
        n = len(k['x'])
        ref = {'Plucked lutes & fretted strings': "Wikipedia's List of musical instruments by Hornbostel-Sachs number: 32",
               'Harps, zithers & dulcimers': "Wikipedia's lists of chordophones by Hornbostel-Sachs number (31, 32)",
               'Bowed & wheel strings': "Wikipedia's lists of chordophones by Hornbostel-Sachs number",
               'Accordions & free reeds': "Wikipedia's List of aerophones by Hornbostel-Sachs number",
               'Pipes, flutes & folk winds': "Wikipedia's lists of aerophones by Hornbostel-Sachs number (421, reed aerophones)",
               'Mechanical & novelty instruments': 'the sources cited on each entry'}[s['n']]
        k['sel'] = f'Follows {ref}; makers appear only where the cited page calls the model or system defining. Covers {n} entries.' if k['n'] in [kk['n'] for kk in s['k']] else ''
f['note'] = 'Shelf by sound source → kind by instrument → entry by region (Europe, Middle East & North Africa, Sub-Saharan Africa, South Asia, East Asia, Southeast Asia, Central Asia, Americas, Oceania).'
f['t'] = f['t']

# overall completeness lines for folk lists (honest)
f_cov = {'Plucked lutes & fretted strings': S_32}
# ---------------------------------------------------------------- CASES
c = copy.deepcopy(D['Cases, stands & accessories'])
removed_c = []
for s in c['s']:
    for k in s['k']:
        for m in k.pop('m', []) or []: removed_c.append(f'{m[0]} ({m[1]})')
        k.pop('r', None)
        for e in k.pop('x', []) or []: removed_c.append(f'{e["n"]} (entry)')
        k.pop('nl', None); k.pop('sel', None); k.pop('xg', None)
c['note'] = 'Commodity kinds by job; no named entries, since none is a first of its kind or a design-collection landmark on a fetched page.'

# ---------------------------------------------------------------- brands
newb = []
have = set(brands_old)
def addb(n, c, f_='', d=''):
    if n in have: return
    have.add(n); newb.append({'n': n, 'c': c, 'f': f_, 'seg': 'Specialist', 'd': d, 'lines': [], 'eras': [], 'sig': [], 'sc': [], 'rel': [], 's': '', 'kf': ''})
addb('Jacob Stainer', 'Austria', '', 'Tyrolean violin maker, c. 1618-1683, working in Absam.')
for dd in (o, f):
    for s in dd['s']:
        for k in s['k']:
            for e in k.get('x', []):
                if e.get('mk'): pass
newb = [b for b in newb]
for b in newb: b['s'] = W + 'Jacob_Stainer'

part = {'replaces': ['Orchestral & band instruments', 'Folk & world instruments', 'Cases, stands & accessories'],
        'depts': [o, f, c], 'brands': newb, 'brand_updates': {}, 'renames': {}, 'moves': []}
json.dump(part, open(R + 'out/E3_parts/ORCH.json', 'w'), ensure_ascii=False, indent=0)
stats = {'strad_violin': n_str_violin, 'strad_viola': n_str_viola, 'strad_cello': n_str_cello, 'o_models_to_entries': made_o, 'o_models_to_versions': vers_o,
         'o_removed': removed_o, 'f_new_or_added': made_f, 'f_removed': len(removed_f), 'c_removed': len(removed_c)}
json.dump({**stats, 'f_removed_list': removed_f, 'c_removed_list': removed_c}, open(R + 'work/V4_E3_ORCH/stats.json', 'w'), ensure_ascii=False, indent=1)
print(stats)
