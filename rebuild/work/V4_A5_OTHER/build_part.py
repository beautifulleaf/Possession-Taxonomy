import json, copy, re, sys
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/V4_A5_OTHER')
from data_rail import E as RAIL, SRC, MK
from data_makers import CM, US, BF, LCM, USL, BFL

ROOT = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(ROOT + 'out/A5.json'))
OLD = {d['n']: copy.deepcopy(d) for d in old['depts']}
WIKI = 'https://en.wikipedia.org/wiki/'
report = {}

def kind(dept, name):
    for s in dept['s']:
        for k in s['k']:
            if k['n'] == name:
                return k
    raise KeyError(name)

def drop(k, *keys):
    for key in keys:
        k.pop(key, None)

def cov(n, ref):
    return f' Complete: {n} of {n} in {ref}.'

def ent(n, d, s, y='', mk='', g=None, role=None, v=None, a=None, dt=None):
    e = {'n': n, 'd': d, 's': s}
    if a: e['a'] = a
    if mk: e['mk'] = mk
    if y: e['y'] = y
    if g: e['g'] = g
    if role: e['role'] = role
    if v: e['v'] = v
    if dt: e['dt'] = dt
    return e

def period(years):
    m = re.search(r'(\d{4})', years or '')
    if not m:
        if 'present' in (years or ''):
            return 'Active today'
        return 'Undated'
    y = int(m.group(1))
    return ('Before 1700' if y < 1700 else '1700s' if y < 1800 else '1800s' if y < 1900 else '1900 onward')

def maker_entry(name, place, years, note, src, g, role=None):
    bits = [f'Clockmaker of {place}' if place else 'Clockmaker']
    if years:
        bits.append(years)
    d = ', '.join(bits) + '.'
    if note:
        d += ' ' + note
    return ent(name, d, src, y=years, g=g, role=role)

# ---------------- Pocket watches ----------------
pw = OLD['Pocket watches']
POCKET = WIKI + 'Pocket_watch'
k = kind(pw, 'Nuremberg egg')
drop(k, 'm', 'r')
k['x'] = [ent('Henlein clock-watch', 'Peter Henlein\'s 1510 example is cited as an early Nuremberg egg; he was making pocket watches by 1526.', POCKET, y='1510')]
k['nl'] = 'One entry is a named early clock-watch worn on a chain.'
k['sel'] = 'Follows Wikipedia\'s Pocket watch article, the only reference fetched for the form.' + cov(1, 'that article')

k = kind(pw, 'Early pocket watch')
drop(k, 'm')
for e in k['x']:
    if e['n'] == 'Souscription':
        e['g'] = 'Verge and cylinder era'
k['x'].append(ent('Graham cylinder watch', 'Cylinder escapement devised by the Abbé de Hautefeuille and applied by George Graham in the early 18th century.', POCKET, y='early 18th c.', g='Verge and cylinder era'))
k['nl'] = 'One entry is a named pocket watch type or maker\'s series from before the lever escapement took over; versions are its series or later tributes.'
k['sel'] = 'Follows Wikipedia\'s Pocket watch article for the escapements and Sotheby\'s for the Souscription; no whole-space list of early watches exists.' + cov(2, 'those two pages')
k['xg'] = 'by escapement'

k = kind(pw, 'Lever pocket watch')
drop(k, 'm')
k['x'] = [ent('Mudge lever watch', 'First lever escapement invented by Thomas Mudge in 1755; made in limited numbers late in the 18th century and common after about 1820.', POCKET, y='1755', g='English lever'),
          ent('Model 1857', 'American Watch Company movement, the first watch made with interchangeable parts.', POCKET, y='1857', mk='Waltham', g='American lever')]
k['nl'] = 'One entry is a named lever pocket watch or movement; revisions are versions.'
k['sel'] = 'Follows Wikipedia\'s Pocket watch article; railroad grades are in their own kind.' + cov(2, 'that article')
k['xg'] = 'by origin'

k = kind(pw, 'Dollar watch')
k['nl'] = 'One entry is a named dollar watch sold by a maker under its own name.'
k['sel'] = 'Follows Wikipedia\'s Ingersoll Watch Company page; no other dollar watch was fetched.' + cov(1, 'that page')
for e in k['x']:
    e['role'] = 'origin'

# railroad canon
k = kind(pw, 'Railroad-grade pocket watch')
entries = []
perm = {}
for mk, n, y, d, vs in RAIL:
    full = f'{mk} {n}' if mk not in ('United States Watch Company',) else n
    if mk == 'Ball':
        full = 'Ball Official Railroad Standard'
        y = '1890s'
    elif mk in ('Waltham', 'Elgin', 'Illinois', 'Hamilton', 'Rockford', 'South Bend', 'Hampden', 'Columbus', 'Aurora', 'Peoria'):
        full = f'{mk} {n}'
    elif mk == 'Howard':
        full = f'E. Howard {n}'
    elif mk == 'United States Watch Company':
        full = n
    key = full.lower()
    if key in perm:
        full = full + ' (' + (vs[0][0] if vs else mk) + ')'
    perm[full.lower()] = 1
    src = SRC[mk]
    if mk == 'United States Watch Company' and ('Waltham' in n or n == 'The President'):
        src = 'http://www.railswest.com/time/uswatchwaltham.html'
    e = ent(full, d, src, y=y, mk=MK.get(mk, mk), g=('E. Howard' if mk == 'Howard' else mk if mk != 'United States Watch Company' else 'United States Watch Co.'))
    if vs:
        e['v'] = [{k2: v2 for k2, v2 in (('n', a), ('y', b), ('d', c)) if v2} for a, b, c in vs]
    entries.append(e)
# keep older entries verified by earlier pass but not on Rails West
for e in entries:
    if e['n'] == 'Hamilton 992 / 992B':
        e['role'] = 'landmark'
        e['a'] = '992B · Railway Special'
    if e['n'] == 'Ball Official Railroad Standard':
        e['role'] = 'landmark'
# groups sorted by maker then years
order = ['Aurora', 'Ball', 'Columbus', 'Elgin', 'Hamilton', 'Hampden', 'E. Howard', 'Illinois', 'Peoria', 'Rockford', 'South Bend', 'United States Watch Co.', 'Waltham']
entries.sort(key=lambda e: (order.index(e['g']),))
k['x'] = entries
k['nl'] = 'One entry is a named or numbered railroad-grade pocket watch line of one maker; open-face and hunting-case pairs, models and jewel counts are versions.'
k['sel'] = ('Follows the maker pages of Rails West (Aurora, Ball, Columbus, Elgin, Hamilton, Hampden, E. Howard, Illinois, Peoria, Rockford, South Bend, U.S. Watch Co. Marion and Waltham, plus the Santa Fe 1938 and Union Pacific 1946 approved lists) and the Wikipedia article Railroad chronometer for the 1893 standard. '
            'The Seth Thomas page was not read; wrist railroad watches are not included. Not every grade listed on those pages was railroad approved.'
            f' Covers {len(entries)} of about {len(entries)} lines on the Rails West pages read.')
k['xg'] = 'by maker'
k['tt'] = [['Size', ['16-size', '18-size']], ['Setting', ['Lever-set', 'Pendant-set']], ['Case', ['Open-face', 'Hunting case']], ['Jewels', ['15', '17', '19', '21', '23']]]
RAIL_N = len(entries)

k = kind(pw, 'Complicated pocket watch')
drop(k, 'm', 'r')
pw_c = k
for e in k['x']:
    if e['n'].startswith('No. 160'):
        e['n'] = 'Breguet No. 160 "Marie Antoinette"'
        e['d'] = 'Breguet pocket watch begun in 1783, probably for Marie Antoinette, finished in 1802 with twelve functions including perpetual calendar and minute repeater.'
        e['y'] = '1802'
        e['s'] = WIKI + 'Marie_Antoinette_(watch)'
        e['role'] = 'landmark'
        e['v'] = [{'n': 'Stolen from the L.A. Mayer Institute for Islamic Art', 'y': '1983', 'd': 'recovered in 2007'}]
    if e['n'].startswith('Henry Graves'):
        e['d'] = 'Patek Philippe pocket watch with 24 complications, commissioned in 1925 by Henry Graves Jr. and delivered in 1933.'
        e['role'] = 'landmark'
        e['v'] = [{'n': 'Sotheby\'s New York sale', 'y': '1999', 'd': 'US$11,002,500'}, {'n': 'Geneva sale', 'y': '2014', 'd': 'CHF 23,237,000'}]
    if e['n'] == 'Calibre 89':
        e['s'] = WIKI + 'Pocket_watch'
        e['d'] = 'Patek Philippe watch of 1989 with 33 complications.'
    if e['n'] == 'Reference 57260':
        e['d'] = 'Vacheron Constantin watch of 2015 with 57 complications.'
        e['s'] = WIKI + 'Pocket_watch'
    e['g'] = 'Grand complication'
k['nl'] = 'One entry is a single named grand-complication pocket watch, or a numbered series of them.'
k['sel'] = 'Follows the three most complicated watches that Wikipedia\'s Pocket watch article names, plus the Breguet and Graves pieces from their own articles; no whole-space list was fetched (Wikipedia\'s list of complicated watches returned an error). Daniels co-axial pocket watches are removed for lack of a fetched page.' + ' Covers 4 of about 4 named pieces on the fetched pages.'

k = kind(pw, 'Coin watch')
k['nl'] = 'One entry is a coin-watch brand or maker\'s series.'
k['sel'] = 'Follows Wikipedia\'s Coin watch article.' + cov(1, 'that article')
for e in k['x']:
    e.pop('g', None)

pw['ms'] = [
 {'mkt': 'Auction price of a pocket watch', 'who': 'Patek Philippe Henry Graves Supercomplication', 'share': 'CHF 23,237,000', 'yr': 2014, 's': WIKI + 'Patek_Philippe_Henry_Graves_Supercomplication', 'note': 'Geneva sale of 11 November 2014, about US$24 million; US$11,002,500 at Sotheby\'s New York on 2 December 1999'},
 {'mkt': 'Valuation of a pocket watch', 'who': 'Breguet No. 160 "Marie Antoinette"', 'share': 'US$30 million', 'yr': 2013, 's': WIKI + 'Marie_Antoinette_(watch)', 'note': 'valuation stated by the page; the watch is held by the L.A. Mayer Institute for Islamic Art in Jerusalem'},
]
pw['msum'] = 'Pocket watches have no published market shares; the two figures below are the record prices and valuations that fetched pages state.'

# ---------------- Collectible clocks ----------------
cc = OLD['Collectible clocks']
k = kind(cc, 'Longcase clock'); drop(k, 'm')
k['nl'] = 'One entry is a named longcase form or a leading maker\'s longcase.'
k['sel'] = 'Follows Wikipedia\'s Longcase clock article, with the Tompion, Knibb and Mora clock pages; makers are listed in full under Clockmakers & factories.' + cov(5, 'those pages')
k['xg'] = 'by origin'
for e, g in zip(k['x'], ['English', 'English', 'French', 'Scandinavian', 'Scandinavian']):
    e['g'] = g
k = kind(cc, 'Lantern clock'); drop(k, 'm')
k = kind(cc, 'Tavern clock')
k['nl'] = 'One entry is a named English public-room wall clock form.'
k['sel'] = 'Follows Wikipedia\'s Act of Parliament clock page.' + cov(1, 'that page')
k = kind(cc, 'Cartel clock')
drop(k, 'm', 'r')
k['nl'] = 'One entry is a named cartel clock type.'; k['sel'] = 'Follows Wikipedia\'s Bracket clock page.' + cov(1, 'that page')
k = kind(cc, 'Banjo clock')
k['nl'] = 'One entry is a patented or named banjo timepiece; makers\' copies are versions.'; k['sel'] = 'Follows Wikipedia\'s Banjo clock page.' + cov(1, 'that page')
k = kind(cc, 'Cuckoo clock')
drop(k, 'm')
k['nl'] = 'One entry is a named cuckoo clock case form.'; k['sel'] = 'Follows Wikipedia\'s Cuckoo clock page; Black Forest makers are under Clockmakers & factories.' + cov(2, 'that page')
k = kind(cc, 'Bracket clock'); drop(k, 'm')
k = kind(cc, 'Carriage clock'); drop(k, 'm')
k['nl'] = 'One entry is a named carriage clock type.'; k['sel'] = 'Follows Wikipedia\'s Carriage clock article; individual carriage-clock makers are not on a fetched list and are removed.' + cov(1, 'that article')
for e in k['x']:
    e['role'] = 'origin'
k = kind(cc, 'Mantel clock')
k['nl'] = 'One entry is a named mantel clock type.'; k['sel'] = 'Follows the Dutch Timepieces guide to French antique clockmakers.' + cov(1, 'that page')
k = kind(cc, 'American shelf clock')
k['nl'] = 'One entry is a named American shelf clock design.'; k['sel'] = 'Follows Wikipedia\'s Eli Terry and Chauncey Jerome pages; American factories are listed under Clockmakers & factories.' + cov(3, 'those pages')
k = kind(cc, 'Wadokei')
k['nl'] = 'One entry is a named Edo-period Japanese clock form.'; k['sel'] = 'Follows Wikipedia\'s Japanese clock article.' + cov(3, 'that article')
k = kind(cc, 'Skeleton clock'); drop(k, 'm')
k = kind(cc, 'Anniversary & Atmos clock')
k['nl'] = 'One entry is a torsion-pendulum clock type or the Atmos.'; k['sel'] = 'Follows Wikipedia\'s Torsion pendulum clock and Atmos clock articles.' + cov(2, 'those articles')
for e in k['x']:
    if e['n'] == 'Atmos':
        e['d'] = 'Self-winding clock powered by changes in temperature and pressure; Reutter\'s 1928 prototype, first sold as Atmos 1 in 1929, made by Jaeger-LeCoultre from 1935.'
        e['y'] = '1928'
        e['s'] = WIKI + 'Atmos_clock'
        e['mk'] = 'Jaeger-LeCoultre'
        e['v'] = [{'n': 'Atmos 0', 'y': '1928', 'd': 'Reutter\'s prototype'}, {'n': 'Atmos 1', 'y': '1929', 'd': 'first commercial model, made by CGR'}, {'n': 'Atmos 2', 'y': '1936', 'd': 'announced January 1936; later models follow its design'}, {'n': 'Atmos Mystérieuse', 'y': '2003', 'd': 'cal. 583'}]
k = kind(cc, 'Mystery clock')
k['nl'] = 'One entry is a named mystery clock.'; k['sel'] = 'Follows Wikipedia\'s Mystery clock and Cartier pages.' + cov(1, 'those pages')
k = kind(cc, 'Wall regulator')
k['nl'] = 'One entry is a named regulator type or model.'; k['sel'] = 'Follows Wikipedia and dealer pages for the Vienna regulator and the Shortt–Synchronome clock.' + cov(2, 'those pages')
k = kind(cc, 'Marine chronometer'); drop(k, 'm', 'r')
k['nl'] = 'One entry is a named marine chronometer pattern.'; k['sel'] = 'Follows Wikipedia\'s Marine chronometer and Hamilton pages.' + cov(2, 'those pages')
k = kind(cc, 'Electric synchronous clock')
drop(k, 'r')
k['x'] = [ent('Telechron', 'Maker of synchronous electric clocks, Ashland, Massachusetts, 1916–1992.', USL, y='1916–1992', mk='Telechron')]
k['nl'] = 'One entry is a maker\'s line of synchronous electric clocks.'; k['sel'] = 'Follows the Telechron entry on Wikipedia\'s List of United States clock companies.' + cov(1, 'that page')
k = kind(cc, 'Flip clock')
k['nl'] = 'One entry is a named flip or split-flap clock design.'; k['sel'] = 'Follows Wikipedia\'s Flip clock, Digital clock and Solari pages.' + cov(2, 'those pages')
for e in k['x']:
    if e['n'] == 'Plato clock':
        e['d'] = 'Flip clock patented by Eugene Fitch in 1903, made by Ansonia and shown at the 1904 St. Louis World\'s Fair.'
        e['y'] = '1903'
        e['mk'] = 'Ansonia'
        e['s'] = WIKI + 'Digital_clock'
        e['role'] = 'origin'
    if e['n'] == 'Cifra':
        e['role'] = 'landmark'

# design clock
k = kind(cc, 'Design clock')
CORE = 'https://www.core77.com/posts/24660/A-History-of-Braun-Design-Part-2-Timepieces'
BR = [('phase 1', 1971, 'Dieter Rams and Dietrich Lubs'), ('phase 2', 1972, 'Dietrich Lubs'), ('phase 3', 1972, 'Dietrich Lubs'), ('functional', 1975, 'Dietrich Lubs'), ('AB 20/20 tb', 1975, 'Dieter Rams and Dietrich Lubs'),
      ('DN 40', 1976, 'Dieter Rams and Dietrich Lubs'), ('DW 20', 1977, 'Dieter Rams and Dietrich Lubs'), ('DW 30', 1978, 'Dieter Rams and Dietrich Lubs'), ('ABR 21', 1978, 'Dieter Rams and Dietrich Lubs'),
      ('DN 50', 1979, 'Ludwig Littmann'), ('ABW21 set', 1980, 'Dietrich Lubs'), ('ABW 41', 1981, 'Dietrich Lubs'), ('ABK 30', 1982, 'Dietrich Lubs'), ('AB 2', 1984, 'Jürgen Greubel and Dieter Rams'),
      ('ABK 20', 1985, 'Dietrich Lubs'), ('AB 312 vsl', 1985, 'Dietrich Lubs'), ('AB 1', 1987, 'Dietrich Lubs'), ('ABW 35', 1988, 'Dietrich Lubs'), ('AW 10', 1989, 'Dietrich Lubs'), ('AB 5', 1990, 'Dietrich Lubs'),
      ('AW 20', 1990, 'Dietrich Lubs'), ('AW 50', 1991, 'Dietrich Lubs')]
xs = [ent('Ball Clock', 'George Nelson Associates wall clock of radiating rods tipped with balls, one of 14 clocks launched for Howard Miller in 1949.', 'https://www.vitra.com/en-ch/magazine/details/original-wall-clocks', y='1949', mk='Howard Miller', g='George Nelson', role='landmark',
          v=[{'n': 'Howard Miller', 'y': '1949', 'mk': 'Howard Miller', 'd': 'one of 14 launch clocks'}, {'n': 'Vitra reissue', 'y': '1999', 'mk': 'Vitra', 'd': 'Nelson clocks reissued from 1999'}]),
      ent('Max Bill wall clock (model 32/0389)', 'Chrome-plated and painted metal wall clock of 1957 made by Junghans, in the MoMA design collection.', 'https://www.moma.org/collection/works/3357', y='1957', mk='Junghans', g='Max Bill', role='landmark'),
      ent('Max Bill kitchen clock', 'Junghans kitchen clock designed by Max Bill with his students, forerunner of the Max Bill watches.', 'https://junghans.de/en/manufacturing', y='1956–1957', mk='Junghans', g='Max Bill')]
for n, y, des in BR:
    e = ent(f'Braun {n}', f'Braun clock of {y}, designed by {des}.', CORE, y=str(y), mk='Braun', g='Braun')
    if n == 'AB 1':
        e['d'] = 'Braun alarm clock of 1987, designed by Dietrich Lubs; collectors single it out among Braun clocks.'
        e['role'] = 'landmark'
    xs.append(e)
k['x'] = xs
k['nl'] = 'One entry is a clock model or design by a named designer, held in a design collection or named in a design history.'
k['sel'] = 'Follows Core77\'s history of Braun timepieces (all 22 models it lists), Vitra\'s account of the Nelson clocks and MoMA\'s record of the Max Bill wall clock. Other designers\' clocks are not on a fetched list.' + ' Covers 22 of 22 Braun models in Core77, and 3 other designs.'
k['xg'] = 'by designer'

# clockmakers shelf
def mk_kind(name, d, nl, sel, xs, xg):
    return {'n': name, 'a': '', 'd': d, 's': xs[0]['s'], 'x': xs, 'nl': nl, 'sel': sel, 'xg': xg}

def mlist(rows, src):
    out = []
    for r in rows:
        name, place, years, note = r[:4]
        role = 'landmark' if name in ('Thomas Tompion', 'Abraham-Louis Breguet') else None
        e = maker_entry(name, place, years, note, src, None, role)
        out.append(e)
    return out

BFN = {'Johann Baptist Beha', 'Mauthe Clock Company', 'Winterhalder & Hofmeier', 'Hermle Clocks', 'Lenzkirch Clock Co'}
rows = {}
for r in CM:
    rows.setdefault(r[4], []).append(r)
def sortg(xs, key):
    xs.sort(key=lambda e: (key(e), e.get('y') or 'zzzz', e['n']))
    return xs

eng = mlist(rows['England'] + rows['Scotland'], LCM)
for e in eng: e['g'] = period(e.get('y',''))
sortg(eng, lambda e: ['Before 1700', '1700s', '1800s', '1900 onward', 'Active today', 'Undated'].index(e['g']))
fr = mlist(rows['France'], LCM)
for e in fr: e['g'] = period(e.get('y',''))
sortg(fr, lambda e: ['Before 1700', '1700s', '1800s', '1900 onward', 'Active today', 'Undated'].index(e['g']))
de_rows = [r for r in rows['Germany'] if r[0] not in BFN] + rows['Austria']
de = mlist(de_rows, LCM)
ctry = {r[0]: r[4] for r in de_rows}
for e in de: e['g'] = ctry[e['n']]
sortg(de, lambda e: e['g'])
# black forest
bf = []
cmdict = {r[0]: r for r in CM}
for name, years, note in BF:
    place = 'the Black Forest'
    e = maker_entry(name, place, years, note, BFL, None)
    bf.append(e)
for e in bf:
    e['g'] = 'Historic firms' if (e.get('y') and 'present' not in e.get('y','')) else ('Active makers' if 'present' in (e.get('y') or '') else 'Historic firms')
sortg(bf, lambda e: e['g'])
us = []
for name, place, years in US:
    e = maker_entry(name, place, years, '', USL, None)
    e['g'] = period(years)
    us.append(e)
sortg(us, lambda e: ['Before 1700', '1700s', '1800s', '1900 onward', 'Active today', 'Undated'].index(e['g']))
for e in us:
    if e['n'] == 'Eli Terry': e['role'] = 'origin'; e['d'] += ' Mass-produced shelf clocks from interchangeable parts from 1814.'
nord = mlist(rows['Denmark'] + rows['Sweden'] + rows['Russia'] + rows['Ukraine'], LCM)
cm2 = {r[0]: r[4] for r in rows['Denmark'] + rows['Sweden'] + rows['Russia'] + rows['Ukraine']}
for e in nord: e['g'] = cm2[e['n']]
sortg(nord, lambda e: e['g'])
sw = mlist(rows['Switzerland'], LCM)
for e in sw: e['g'] = period(e.get('y',''))
sortg(sw, lambda e: ['Before 1700', '1700s', '1800s', '1900 onward', 'Active today', 'Undated'].index(e['g']))
asia = mlist(rows['Australia'] + rows['Canada'] + rows['China'] + rows['Korea'], LCM)
cm3 = {r[0]: r[4] for r in rows['Australia'] + rows['Canada'] + rows['China'] + rows['Korea']}
for e in asia: e['g'] = cm3[e['n']]
sortg(asia, lambda e: e['g'])

n_lcm = len(CM)
def cmcov(n, extra=''):
    return f' Complete: {n} of {n} rows in that section of the list.{extra}'
kinds = [
 mk_kind('English & Scottish clockmaker', 'Maker or firm of clocks in England or Scotland, from Tudor court clockmakers to firms still trading.', 'One entry is a clockmaker or clock firm named on the list; the maker\'s forms stay under their kinds.', f'Follows the English and Scottish sections of Wikipedia\'s List of clock manufacturers.' + cmcov(len(eng)), eng, 'by century of the maker\'s years'),
 mk_kind('French clockmaker', 'Maker or firm of clocks in France, such as the Paris masters and the Brocot family.', 'One entry is a clockmaker or clock firm named on the list.', 'Follows the French section of Wikipedia\'s List of clock manufacturers.' + cmcov(len(fr)), fr, 'by century of the maker\'s years'),
 mk_kind('German & Austrian clockmaker', 'Maker or firm of clocks in Germany or Austria, including the Vienna regulator makers and the big Schwenningen and Schramberg factories.', 'One entry is a clockmaker or clock firm named on the list; Black Forest firms that the Black Forest page also names are under Black Forest clockmaker.', 'Follows the German and Austrian sections of Wikipedia\'s List of clock manufacturers, less five firms (Beha, Mauthe, Winterhalder & Hofmeier, Hermle, Lenzkirch) held under Black Forest clockmaker.' + cmcov(len(de), ' Five rows moved to the Black Forest kind.'), de, 'by country'),
 mk_kind('Black Forest clockmaker', 'Maker or firm from the Black Forest clock industry, home of the cuckoo clock.', 'One entry is a clockmaker or firm named on Wikipedia\'s Black Forest clockmakers page.', 'Follows Wikipedia\'s Black Forest clockmakers page.' + cov(len(bf), 'that page'), bf, 'by whether the firm still trades'),
 mk_kind('American clock company', 'Connecticut shelf-clock firms, electric clock makers and the other American companies, from 1738 to today.', 'One entry is a clock company or clockmaker named on the list.', 'Follows Wikipedia\'s List of United States clock companies, every row; the page is marked as needing more citations.' + cov(len(us), 'that list'), us, 'by century of the firm\'s years'),
 mk_kind('Swiss clockmaker', 'Swiss maker of clocks, from Geneva houses to Vaud manufactures.', 'One entry is a clockmaker or clock firm named on the list.', 'Follows the Swiss section of Wikipedia\'s List of clock manufacturers.' + cmcov(len(sw)), sw, 'by century of the maker\'s years'),
 mk_kind('Northern & Eastern European clockmaker', 'Maker of clocks in Denmark, Sweden, Russia or Ukraine.', 'One entry is a clockmaker or clock firm named on the list.', 'Follows the Danish, Swedish, Russian and Ukrainian sections of Wikipedia\'s List of clock manufacturers.' + cmcov(len(nord)), nord, 'by country'),
 mk_kind('Clockmaker of Australia, Canada, China & Korea', 'Maker of clocks in Australia, Canada, China or Korea.', 'One entry is a clockmaker or clock firm named on the list.', 'Follows the Australian, Canadian, Chinese and Korean sections of Wikipedia\'s List of clock manufacturers.' + cmcov(len(asia)), asia, 'by country'),
]
total_cm = len(eng) + len(fr) + len(de) + len(bf) + len(us) + len(sw) + len(nord) + len(asia)
cc['s'].append({'n': 'Clockmakers & factories', 't': 'The makers and firms behind collectible clocks, listed by home country or region; the clock forms they made are under the other shelves.', 'ax': 'kinds by home country or region of the maker', 'k': kinds})
# update dept text
cc['t'] = 'Clocks collected for age, maker, form or design, from longcase to flip clocks, with the makers and factories behind them; a clock bought just to use → Everyday clocks, a chess clock → E1.'
cc['ax'] = 'Where does the clock stand or hang, who made it, and is it a precision, electric or designer piece?'
cc['note'] = 'By form, then maker and period. The maker shelf lists every firm on the fetched lists. English clocks 1660–1800, French 18th–19th c., German and Austrian 19th c., American factory clocks from 1814.'

# ---------------- Everyday clocks ----------------
ev = OLD['Everyday clocks']
k = kind(ev, 'Alarm clock'); drop(k, 'm')
k['x'] = [ent('Hutchins alarm clock', 'First American alarm clock, made by Levi Hutchins in Concord, New Hampshire, to ring at 4 am; Antoine Redier patented an adjustable mechanical alarm in 1847.', WIKI + 'Alarm_clock', y='1787', role='origin')]
k['nl'] = 'One entry is the origin of the kind; later alarm clocks are commodity and are not entries.'
k['sel'] = 'Follows Wikipedia\'s Alarm clock article for the origin; brand and model lists are left out under the icon rule.' + cov(1, 'that article')
k = kind(ev, 'Sunrise alarm clock'); drop(k, 'm')
k = kind(ev, 'Wall clock'); drop(k, 'r')
k = kind(ev, 'Desk clock'); drop(k, 'm')
k = kind(ev, 'Digital clock'); drop(k, 'r')
k = kind(ev, 'Travel clock'); drop(k, 'm', 'r')

# ---------------- Timers ----------------
tm = OLD['Timers & timing instruments']
k = kind(tm, 'Stopwatch'); drop(k, 'm', 'r')
k['x'] = [ent('Watson stopwatch', 'The page names the horologist Samuel Watson as maker of the first stopwatch; it gives no year.', WIKI + 'Stopwatch', role='origin')]
k['nl'] = 'One entry is the origin of the kind; later stopwatches are commodity and are not entries.'
k['sel'] = 'Follows Wikipedia\'s Stopwatch article.' + cov(1, 'that article')
k = kind(tm, 'Visual timer'); drop(k, 'm')
k['x'] = [ent('Time Timer', 'Countdown timer with a shrinking red disc, invented by Jan Rogers to help her youngest child change between routines.', 'https://www.timetimer.com/pages/our-story', mk='Time Timer', role='origin',
              v=[{'n': 'Time Timer Original 8"'}, {'n': 'Time Timer MOD'}, {'n': 'Time Timer TWIST'}])]
k['nl'] = 'One entry is the origin of the kind; later visual timers are commodity.'
k['sel'] = 'Follows the Time Timer company\'s own story, which dates the invention to almost thirty years ago without a year.' + cov(1, 'that page')
k = kind(tm, 'Hourglass'); drop(k, 'm', 'r')
k['x'] = [ent('Marine sandglass', 'Ship\'s timekeeper; the earliest certain record is a receipt of about 1345 for the King\'s ship La George.', WIKI + 'Hourglass', y='c. 1345', role='origin')]
k['nl'] = 'One entry is the earliest documented form of the kind.'
k['sel'] = 'Follows Wikipedia\'s Hourglass article.' + cov(1, 'that article')
k = kind(tm, 'Sundial'); drop(k, 'm', 'r')
k['x'] = [ent('Egyptian shadow clock', 'Oldest known sundial, from the Valley of the Kings, about 1500 BC.', WIKI + 'Sundial', y='c. 1500 BC', role='origin')]
k['nl'] = 'One entry is the origin of the kind.'
k['sel'] = 'Follows Wikipedia\'s Sundial article.' + cov(1, 'that article')
k['s'] = WIKI + 'Sundial'

# ---------------- Straps, storage & parts ----------------
sp = OLD['Straps, storage & parts']
k = kind(sp, 'Watch strap')
drop(k, 'm')
k['x'] = []
k.pop('x')
k['s'] = WIKI + 'Watch_strap'
k['tt'] = [['Style', ['Bund', 'NATO (G10)', 'Zulu', 'MN (Marine Nationale)', 'Perlon', 'Cloth', 'Velcro', 'Expanding diving']], ['Lug width', ['18 mm', '20 mm (NATO G10 standard)', '22 mm']],
           ['Material', ['Calf leather', 'Alligator or crocodile', 'Rubber', 'Silicone', 'Nylon', 'Sailcloth', 'Canvas']], ['Construction', ['Two-piece', 'Pass-through (one piece)']], ['Fastening', ['Tang buckle', 'Deployant clasp', 'Butterfly clasp']]]
k['d'] = 'Band of leather, fabric or rubber made to hold a watch on the wrist; the NATO (G10) strap was developed by the UK Ministry of Defence and introduced in 1973.'
k = kind(sp, 'Watch bracelet')
k.pop('x', None)
k['s'] = WIKI + 'Watch_strap'
k['tt'] = [['Style', ['Oyster', 'Jubilee', 'President', 'Milanese mesh', 'Oysterflex', 'Stainless steel link']], ['Construction', ['Solid link', 'Folded link', 'Mesh', 'Rubber-integrated']]]
k = kind(sp, 'Watch chain'); drop(k, 'm', 'r')
k['tt'] = [['Type', ['Albert chain', 'Fob chain', 'Sport chain']]]
k = kind(sp, 'Watch winder'); drop(k, 'm', 'r')
k = kind(sp, 'Watch box & roll'); drop(k, 'r')
k = kind(sp, 'Watch movement')
GP = 'https://www.gearpatrol.com/watches/a487095/automatic-watch-movement/'
old_x = {e['n']: e for e in k['x']}
mv = [
 ent('Eterna 1247', 'Eterna calibre of 1955 that is the base of the ETA 2824-2.', GP, y='1955', mk='Eterna', g='Swiss', role='origin'),
 ent('ETA 2824-2', 'Swiss 28,800 vph hacking automatic in production since 1982, the benchmark mid-range calibre.', GP, y='1982', mk='ETA', g='Swiss', v=[{'n': 'Hangzhou 6301', 'd': 'Chinese near-clone'}]),
 ent('ETA 7750', 'Swiss automatic chronograph calibre, Valjoux 7750 from the 1970s.', old_x['ETA 7750']['s'], y='1970s', mk='ETA', g='Swiss', a='Valjoux 7750'),
 ent('Sellita SW200', 'Sellita automatic, near-identical to the ETA 2824-2 with 26 jewels.', GP, mk='Sellita', g='Swiss'),
 ent('STP1-11', 'Automatic calibre from Swiss Technology Production, part of the Fossil Group.', GP, mk='Swiss Technology Production', g='Swiss'),
 ent('Miyota 8215', 'Miyota automatic that is the base of the 9015.', GP, mk='Miyota', g='Japanese'),
 ent('Miyota 9015', 'Japanese 28,800 vph automatic of 2009, 0.6 mm thinner than the ETA 2824.', GP, y='2009', mk='Miyota', g='Japanese'),
 ent('Seiko NH35 / NH36 family', 'TMI/Seiko automatic calibres sold for watchmaking and modding: 21,600 vph, hacking, hand-winding.', old_x['Seiko NH35 / NH36 family']['s'], mk='Seiko Instruments', g='Japanese', v=old_x['Seiko NH35 / NH36 family'].get('v')),
 ent('Seiko 7S26', 'Non-hacking 21-jewel automatic of the SKX and Seiko 5, discontinued 2019.', old_x['Seiko 7S26']['s'], y='1996', mk='Seiko Instruments', g='Japanese', v=old_x['Seiko 7S26'].get('v')),
 ent('Seiko 6R15', '21,600 vph Seiko automatic with Spron mainspring; sold as NE15.', old_x['Seiko 6R15']['s'], mk='Seiko Instruments', g='Japanese', a='NE15'),
 ent('Seagull ST19', 'Chinese hand-wound chronograph calibre of Swiss origin, used in budget chronographs.', old_x['Seagull ST19']['s'], mk='Tianjin Seagull', g='Chinese', a='ST1901'),
]
k['x'] = mv
k['nl'] = 'One entry is a movement calibre or calibre family fitted by modders; revisions are versions.'
k['sel'] = 'Follows Gear Patrol\'s guide to common automatic movements (all eight it names) plus four calibres from earlier pages (NH35/NH36, 7S26, 6R15, ST19); no whole-space list of calibres exists.' + ' Covers 8 of 8 calibres in Gear Patrol, and 4 others.'
k['xg'] = 'by country of origin'
k = kind(sp, 'Watch case')
k['nl'] = 'One entry is a named aftermarket case pattern.'; k['sel'] = 'Follows Lucius Atelier\'s SKX case listing; no whole-space list exists.' + cov(1, 'that page')

# ---- dept tweaks
pw['note'] = pw['note'] + ' The railroad-grade canon follows the Rails West maker pages.'
sp['note'] = 'Straps and modding parts are variety (sorted by compatibility); storage and clock parts are tier. Strap, bracelet and chain designs are attributes of their kinds, not entries.'

depts = [pw, cc, ev, tm, sp]
out = {
 'replaces': ['Pocket watches', 'Collectible clocks', 'Everyday clocks', 'Timers & timing instruments', 'Straps, storage & parts'],
 'depts': depts,
 'brands': [],
 'brand_updates': {},
 'renames': {},
 'moves': [],
}
BRANDS = [
 ('Rockford','United States','Rockford Watch Co. railroad-grade pocket watches.','http://www.railswest.com/time/rockford.html'),
 ('South Bend','United States','South Bend Watch Co. railroad-grade pocket watches.','http://www.railswest.com/time/southbend.html'),
 ('E. Howard','United States','Boston maker of E. Howard & Co. watches and clocks, 1842 to the present.',USL),
 ('Hampden','United States','Hampden and Dueber-Hampden railroad-grade pocket watches.','http://www.railswest.com/time/hampden.html'),
 ('Columbus','United States','Columbus Watch Co. railroad-grade pocket watches.','http://www.railswest.com/time/columbus.html'),
 ('Aurora','United States','Aurora Watch Co. quick-train railroad-grade pocket watches of 1887.','http://www.railswest.com/time/aurora.html'),
 ('Peoria','United States','Peoria Watch Co., incorporated 1885; the factory closed in 1891–92.','http://www.railswest.com/time/peoria.html'),
 ('United States Watch Company','United States','Marion, Illinois maker of the 1869 18-size railroad grades.','http://www.railswest.com/time/uswatchmarion.html'),
 ('Time Timer','United States','Maker of the Time Timer visual timer.','https://www.timetimer.com/pages/our-story'),
 ('Swiss Technology Production','Switzerland','Maker of the STP1-11 automatic calibre; part of the Fossil Group.',GP),
 ('Chelsea Clock Company','United States','Boston clock company, 1887 to the present.',USL),
 ('Masterclock Inc.','United States','St. Charles, Missouri maker of master clocks, 1994 to the present.',USL),
 ('Sternreiter','United States','Berea, Ohio clock maker, 2003 to the present.',USL),
 ('Rombach & Haas','Germany','Active Black Forest clockmaker.',BFL),
 ('Adolf Herr','Germany','Active Black Forest clockmaker.',BFL),
 ('Robert Herr','Germany','Active Black Forest clockmaker.',BFL),
 ('August Schwer','Germany','Active Black Forest clockmaker.',BFL),
 ('Ansonia','United States','Ansonia Clock Company, 1851–1929, maker of the Plato flip clock.',USL),
]
reg = {e['n'].lower() for e in json.load(open(ROOT + 'out/A5_brands.json'))['b']}
for n, c, d, s in BRANDS:
    if n.lower() in reg:
        continue
    out['brands'].append({'n': n, 'c': c, 'seg': 'Traditional & regional', 'd': d, 's': s, 'kf': 'clocks and watches'})
out['brand_updates'] = {
 'Hamilton': {'own': 'Swatch Group', 'tier': 'Global group', 'c': 'United States'},
 'Breguet': {'own': 'Swatch Group', 'tier': 'Global group', 'c': 'France'},
 'Jaeger-LeCoultre': {'own': 'Richemont', 'tier': 'Global group', 'c': 'Switzerland'},
 'Vacheron Constantin': {'own': 'Richemont', 'tier': 'Global group', 'c': 'Switzerland'},
 'Patek Philippe': {'own': 'Stern family', 'tier': 'Independent', 'c': 'Switzerland'},
}
json.dump(out, open(ROOT + 'out/A5_parts/OTHER.json.tmp', 'w'), ensure_ascii=False, indent=0)
import os
os.replace(ROOT + 'out/A5_parts/OTHER.json.tmp', ROOT + 'out/A5_parts/OTHER.json')
print('rail', RAIL_N, 'makers', total_cm, [len(x) for x in (eng, fr, de, bf, us, sw, nord, asia)])
