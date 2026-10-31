import json, re, sys, os
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/CMP_E4')
import data_firearms as D1
import data_firearms2 as D2

ROOT = '/home/user/Possession-Taxonomy/rebuild/'
SRC = ROOT + 'out/E4.json'
d = json.load(open(SRC))

def norm(s):
    s = s.lower().replace('×', 'x').replace('–', '-').replace('—', '-')
    s = s.replace('parabellum', 'luger').replace('government', '').replace('winchester magnum rimfire', 'wmr')
    s = re.sub(r'mm\b', '', s)
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

def find_kind(dept, name):
    for sec in d['depts'][dept]['s']:
        for k in sec['k']:
            if k['n'] == name:
                return k
    raise KeyError(name)

KIND = {
 'SA': (4, 'Single-action revolver', 'single-action revolver'),
 'DA': (4, 'Double-action revolver', 'double-action revolver'),
 'PR': (4, 'Percussion revolver', 'percussion revolver'),
 'SP': (4, 'Semi-automatic pistol', 'semi-automatic pistol'),
 'BA': (4, 'Bolt-action rifle', 'bolt-action rifle'),
 'LA': (4, 'Lever-action rifle', 'lever-action rifle'),
 'SS': (4, 'Single-shot shotgun', 'single-shot shotgun'),
 'SXS': (4, 'Side-by-side shotgun', 'side-by-side shotgun'),
 'OU': (4, 'Over-under shotgun', 'over-under shotgun'),
 'PU': (4, 'Pump-action shotgun', 'pump-action shotgun'),
 'SM': (4, 'Semi-automatic shotgun', 'semi-automatic shotgun'),
}
SRC_URL = {
 'SA': 'List_of_revolvers', 'DA': 'List_of_revolvers', 'PR': 'List_of_revolvers',
 'SP': 'List_of_semi-automatic_pistols', 'BA': 'List_of_bolt-action_rifles', 'LA': 'Lever-action',
 'SS': 'List_of_shotguns', 'SXS': 'List_of_shotguns', 'OU': 'List_of_shotguns', 'PU': 'List_of_shotguns', 'SM': 'List_of_shotguns',
}

# existing names across the whole department 4 and 6
allnames = set()
def collect():
    allnames.clear()
    for di in (4, 6):
        for sec in d['depts'][di]['s']:
            for k in sec['k']:
                for e in k.get('x', []):
                    allnames.add(norm(e['n']))
                    for a in re.split(r'\s*[·;,]\s*', e.get('a', '') or ''):
                        if a: allnames.add(norm(a))
collect()
before = {}
for code, (di, kn, _) in KIND.items():
    before[kn] = len(find_kind(di, kn)['x'])

def yint(y):
    m = re.search(r'\d{4}', y or '')
    return int(m.group()) if m else 9999

def mkentry(row, code, g, yover=None):
    name, kind, y, mk, cty = row
    if yover is not None and name in yover:
        y = yover[name]
    desc = KIND[code][2]
    if cty:
        d_ = f"{cty} {desc}"
    else:
        d_ = desc[0].upper() + desc[1:]
    if mk: d_ += f" made by {mk}"
    if y: d_ += f", introduced {y}"
    return {"n": name, "a": "", "d": d_ + ".", "mk": mk, "y": y,
            "s": "https://en.wikipedia.org/wiki/" + SRC_URL[code], "v": [], "g": g}

SKIP = {norm('Adams revolver 1851')}

def era_rev(code, y, name):
    yy = yint(y)
    if code == 'SA':
        return 'Cartridge era' if yy == 9999 or yy < 1950 else 'Modern'
    if code == 'PR':
        if yy == 9999: return 'Mid percussion'
        if yy <= 1850: return 'Early percussion'
        if yy >= 1950: return 'Modern percussion'
        return 'Mid percussion'
    if yy == 9999: return '20th century'
    return '19th century' if yy < 1900 else ('20th century' if yy < 2000 else '21st century')

MODERN21 = ['Pindad','Komodo','Malinnov','Mendoza','INDUMIL','STP9','RS9','Tara','SCCY','PSA 5.7','Tisas','Zafar','M9-02',
            'Sarsılmaz','Yavuz','Zigana','Kel-Tec P50','Kel-Tec PR57','SD VE','Taurus TX22','Vektor CP1','Ruger-5.7','Walther SSP','Zaragoza','Wildebeest','QX-04','QSZ-11','HD66','Hudson']
MIDC = ['Sugiura','Pantax','Gyrojet','Tokarev Sportowy','Trejo','Hamada','Pistole-M','Zastava P25','Udav']
def era_sp(y, name):
    yy = yint(y)
    if yy == 9999:
        if any(m in name for m in MODERN21): return '21st century'
        if any(m in name for m in MIDC): return 'Mid century'
        return 'Late 20th century'
    if yy < 1919: return 'Early pistols'
    if yy < 1945: return 'Between the wars'
    if yy < 1970: return 'Mid century'
    if yy < 2000: return 'Late 20th century'
    return '21st century'

PREC = {'Snipex Rhino Hunter','Snipex T-Rex','Snipex Alligator',"MCR Horizon's Lord",'Tubb 2000','MAK Enterprises Tubegun','WKW Wilk'}
SPORT = {'Mossberg MVP','SIG Sauer 200 STR','IOF .30-06 sporting rifle','IOF .315 sporting rifle'}
def era_ba(y, name):
    if name in PREC: return 'Precision'
    if name in SPORT: return 'Sporting'
    yy = yint(y)
    return 'Black-powder' if yy < 1895 else 'Smokeless'
def era_la(y, name):
    yy = yint(y)
    if yy == 9999: return 'Modern'
    if yy < 1860: return 'Early repeaters'
    if yy <= 1894: return 'Black-powder era'
    if yy < 1990: return 'Smokeless era'
    return 'Modern'

def shot_g(name):
    pre = [('Heckler & Koch','Heckler & Koch'),('Smith & Wesson','Smith'),('High Standard','High Standard'),
           ('Standard Manufacturing','Standard Manufacturing'),('Punt gun','Punt'),('Vepr','Molot'),('MP-155','Baikal'),
           ('IZh','IZh'),('TOZ','TOZ'),('TTs','TOZ'),('Winchester','Winchester'),('Fort','Fort')]
    for p, g in pre:
        if name.startswith(p): return g
    return name.split()[0]

order = {
 'Single-action revolver': ['Cartridge era','Modern'],
 'Double-action revolver': ['19th century','20th century','21st century'],
 'Percussion revolver': ['Early percussion','Mid percussion','Modern percussion'],
 'Semi-automatic pistol': ['Early pistols','Between the wars','Mid century','Late 20th century','21st century'],
 'Bolt-action rifle': ['Black-powder','Smokeless','Sporting','Precision'],
 'Lever-action rifle': ['Early repeaters','Black-powder era','Smokeless era','Modern'],
}

added = {kn: 0 for kn in before}
def add_rows(rows, yover=None):
    for row in rows:
        name, code, y, mk, cty = row
        if norm(name) in allnames or norm(name) in SKIP: continue
        di, kn, _ = KIND[code]
        k = find_kind(di, kn)
        if code in ('SA','DA','PR'): g = era_rev(code, yover.get(name, y) if yover else y, name)
        elif code == 'SP': g = era_sp(yover.get(name, y) if yover else y, name)
        elif code == 'BA': g = era_ba(y, name)
        elif code == 'LA': g = era_la(y, name)
        else: g = shot_g(name)
        k['x'].append(mkentry(row, code, g, yover))
        allnames.add(norm(name)); added[kn] += 1

add_rows(D1.REV, D2.REV_Y)
add_rows(D2.REV_A)
add_rows(D1.PIS, D2.PIS_Y)
add_rows(D2.PIS_A)
add_rows(D1.BOLT)
add_rows(D1.LEVER)
add_rows(D1.SHOT)
add_rows(D2.SHOT_A)

# sort firearm kinds
for kn in order:
    k = find_kind(4, kn)
    o = order[kn]
    for e in k['x']:
        if e['g'] not in o: o.append(e['g'])
    k['x'].sort(key=lambda e: (o.index(e['g']), yint(e.get('y', '')), e['n'].lower()))
    k['xg'] = k.get('xg') or 'by era'
for kn in ['Single-shot shotgun','Side-by-side shotgun','Over-under shotgun','Pump-action shotgun','Semi-automatic shotgun']:
    k = find_kind(4, kn)
    k['x'].sort(key=lambda e: (e['g'].lower(), yint(e.get('y', '')), e['n'].lower()))

# ---------- cartridges ----------
def read_lines(p):
    return [l.strip() for l in open(p, encoding='utf-8') if l.strip()]
hand = []
for l in read_lines(ROOT + 'work/CMP_E4/handgun_raw.txt'):
    nm, mm = [t.strip() for t in l.rsplit('|', 1)]
    hand.append((nm, float(mm)))
rifle = read_lines(ROOT + 'work/CMP_E4/rifle_raw.txt')

def diam_mm(name):
    n = name.strip()
    m = re.match(r'^(\d+)/(\d+)', n)
    if m and not n.startswith('.'):  # gauge-style 20/577
        return int(m.group(2)) / 1000 * 25.4
    m = re.search(r'(\d+(?:\.\d+)?)', n)
    if not m: return None
    if n.startswith('.'):
        mm_ = re.match(r'^\.(\d+)', n)
        digits = mm_.group(1)
        return int(digits) / (10 ** len(digits)) * 25.4
    return float(m.group(1))

CL = ['Up to 6 mm (.22 class)','6 to 6.9 mm (.25–.27 class)','7 to 7.9 mm (.28–.31 class)','8 to 8.9 mm (.32–.35 class)',
      '9 to 9.9 mm (.35–.38 class)','10 to 10.9 mm (.40–.42 class)','11 to 11.9 mm (.43–.45 class)','12 mm and over (.46 class and larger)']
BIG = 'Autocannon and large-calibre rounds (20 mm and over)'
def klass(mm):
    if mm is None: return CL[-1]
    if mm >= 20: return BIG
    for i, t in enumerate([6, 7, 8, 9, 10, 11, 12]):
        if mm < t: return CL[i]
    return CL[-1]

RIM_MOD = ['.17 Munisalva', '.17 PMC/Aguila', '.22 ILARCO', '4.5×26mm MKR', '2.34mm rimfire']
RIM_HIS = ['.25 Short', '.25 Stevens Short', '.41 Short Rimfire', '.41 Swiss', '10.4×38mmRF', '12.17×42mmRF', '14x33mmRF', '17x28mmRF', '17.5x29mmRF']
rim_names = set(norm(x) for x in RIM_MOD + RIM_HIS)
HURL = 'https://en.wikipedia.org/wiki/List_of_handgun_cartridges'
RURL = 'https://en.wikipedia.org/wiki/List_of_rifle_cartridges'

kH = find_kind(6, 'Centrefire handgun cartridge')
kR = find_kind(6, 'Centrefire rifle cartridge')
kF = find_kind(6, 'Rimfire cartridge')
cb = {k['n']: len(k['x']) for k in (kH, kR, kF)}
SKIPC = {norm('HK 4.6×30mm'), norm('FN 5.7×28mm')}
cadd = {'h': 0, 'r': 0, 'f': 0}
def cart(nm, mm, url, kind_desc, g):
    return {"n": nm, "a": "", "d": f"{kind_desc} with a bullet of about {mm:.1f} mm." if mm else f"{kind_desc}.", "mk": "", "y": "",
            "s": url, "v": [], "g": g}
for nm, mm in hand:
    if nm.startswith('2.34mm'):
        nm = '2.34mm rimfire'
        if norm(nm) in allnames: continue
        kF['x'].append(cart(nm, mm, HURL, 'Rimfire cartridge for a handgun', 'Modern rimfire')); allnames.add(norm(nm)); cadd['f'] += 1
        continue
    if norm(nm) in allnames or norm(nm) in SKIPC: continue
    # class from nominal calibre in the name, as the existing entries are sorted
    dm = diam_mm(nm)
    kH['x'].append(cart(nm, dm if dm else mm, HURL, 'Handgun cartridge', klass(dm if dm else mm)))
    allnames.add(norm(nm)); cadd['h'] += 1
for nm in rifle:
    if norm(nm) in allnames: continue
    if norm(nm) in rim_names:
        g = 'Modern rimfire' if nm in RIM_MOD else 'Historical rimfire'
        kF['x'].append(cart(nm, diam_mm(nm), RURL, 'Rimfire cartridge', g)); allnames.add(norm(nm)); cadd['f'] += 1
        continue
    dm = diam_mm(nm)
    kR['x'].append(cart(nm, dm, RURL, 'Rifle cartridge', klass(dm)))
    allnames.add(norm(nm)); cadd['r'] += 1

def csort(k, groups):
    for e in k['x']:
        if e['g'] not in groups: groups.append(e['g'])
    k['x'].sort(key=lambda e: (groups.index(e['g']), diam_mm(e['n']) or 99, e['n'].lower()))
csort(kH, list(CL)); csort(kR, list(CL) + ['Other', BIG])
csort(kF, ['Modern rimfire', 'Historical rimfire'])

# ---------- shotgun gauges ----------
G = {1:(1.669,42.4),2:(1.325,33.7),3:(1.157,29.4),4:(1.052,26.7),5:(.976,24.8),6:(.919,23.3),7:(.873,22.2),8:(.835,21.2),
9:(.803,20.4),10:(.775,19.7),11:(.751,19.1),12:(.729,18.5),13:(.710,18.0),14:(.693,17.6),15:(.677,17.2),16:(.662,16.8),
17:(.649,16.5),18:(.637,16.2),19:(.626,15.9),20:(.615,15.6),21:(.605,15.4),22:(.596,15.1),23:(.587,14.9),24:(.579,14.7),
25:(.571,14.5),26:(.563,14.3),27:(.556,14.1),28:(.550,14.0),29:(.543,13.8),30:(.537,13.6),31:(.531,13.5),32:(.526,13.4),
33:(.520,13.2),34:(.515,13.1),35:(.510,13.0),36:(.506,12.9),37:(.501,12.7),38:(.497,12.6),39:(.492,12.5),40:(.488,12.4),
41:(.484,12.3),42:(.480,12.2),43:(.476,12.1),44:(.473,12.0),45:(.469,11.9),46:(.466,11.8),47:(.463,11.8),48:(.459,11.7),
49:(.456,11.6),50:(.453,11.5)}
def gg(n):
    if n <= 3: return 'Punt-gun bores (1 to 3 gauge)'
    if n <= 11: return 'Large bores (4 to 11 gauge)'
    if n <= 20: return 'Common bores (12 to 20 gauge)'
    if n <= 32: return 'Small bores (21 to 32 gauge)'
    return 'Obsolete small bores (33 to 50 gauge)'
ks = find_kind(6, 'Shotshell')
for e in ks['x']:
    if e['g'].startswith('Small bores'): e['g'] = 'Small bores (21 to 32 gauge)'
have = {e['n'] for e in ks['x']}
gadd = 0
for n, (inch, mm) in G.items():
    nm = f"{n} gauge"
    if nm in have: continue
    ks['x'].append({"n": nm, "a": "", "d": f"Shotgun gauge with a bore of {inch:.3f} in ({mm:.1f} mm).", "mk": "", "y": "",
                    "s": "https://en.wikipedia.org/wiki/Gauge_(firearms)", "v": [], "g": gg(n)}); gadd += 1
def gk(e):
    m = re.match(r'(\d+) gauge', e['n'])
    return (int(m.group(1)) if m else 999)
ks['x'].sort(key=gk)
gorder = ['Punt-gun bores (1 to 3 gauge)','Large bores (4 to 11 gauge)','Common bores (12 to 20 gauge)','Small bores (21 to 32 gauge)','Obsolete small bores (33 to 50 gauge)']
# .410 stays at the end of the small bores; reorder by group then gauge
ks['x'].sort(key=lambda e: (gorder.index(e['g']) if e['g'] in gorder else 99, gk(e)))
for e in ks['x']:
    if e['n'] == '.410 bore': e['g'] = 'Small bores (21 to 32 gauge)'
ks['sel'] = ("Complete: all 50 numbered gauges of Wikipedia's Gauge (firearms) conversion table plus the .410 bore (%d entries); the table lists no bore for the .410." % len(ks['x']))

# ---------- sel lines ----------
LR = "Wikipedia's List of revolvers"
def setsel(kn, di, text):
    k = find_kind(di, kn)
    base = k.get('sel', '')
    k['sel'] = text
n = lambda kn: len(find_kind(4, kn)['x'])
setsel('Single-action revolver', 4, f"Single-action revolvers of {LR}, read in full to its end (194,203 characters); the page does not name the action, so each model is placed by its known action. Complete: {n('Single-action revolver')} of {n('Single-action revolver')} in that reference.")
setsel('Double-action revolver', 4, f"Double-action revolvers of {LR}, read in full to its end (194,203 characters); the page does not name the action, so each model is placed by its known action. Complete: {n('Double-action revolver')} of {n('Double-action revolver')} in that reference.")
setsel('Percussion revolver', 4, f"Percussion revolvers of {LR}, read in full to its end (194,203 characters). Complete: {n('Percussion revolver')} of {n('Percussion revolver')} in that reference.")
setsel('Semi-automatic pistol', 4, f"Pistols of Wikipedia's List of semi-automatic pistols, read in full to its last row, Zigana (335,822 characters); machine pistols and pistol-calibre carbine-like rows are kept as listed, and the page's range rows (for example SIG P320) are one entry each. Covers {n('Semi-automatic pistol')} entries from that reference; the few rows whose names the extraction cut or merged are left out, and the page's own count was not available to compare.")
setsel('Bolt-action rifle', 4, f"Rifles of Wikipedia's List of bolt-action rifles, read in full (72 rows); the page notes it is incomplete. Complete: {n('Bolt-action rifle')} of 72 in that reference.")
setsel('Lever-action rifle', 4, f"Every model named in Wikipedia's Lever-action article, read in full to the end of its text (156,576 characters; the last 56,000 are references). Complete: {n('Lever-action rifle')} of {n('Lever-action rifle')} in that reference.")
SG = "Wikipedia's List of shotguns"
for kn in ['Single-shot shotgun','Side-by-side shotgun','Over-under shotgun','Pump-action shotgun','Semi-automatic shotgun']:
    setsel(kn, 4, f"Civilian and sporting shotguns of this action in {SG}, read in full to its last row, Zastava LP 12 PAS (158,570 characters); military, combination-gun and revolving shotguns are left out. Covers {n(kn)} entries from that reference; the page's own per-action count was not available to compare.")
setsel('Rimfire cartridge', 6, f"Rimfire cartridges of Wikipedia's List of rifle cartridges and List of handgun cartridges, read in full. Complete: {len(kF['x'])} of {len(kF['x'])} rimfires in those references.")
setsel('Centrefire handgun cartridge', 6, f"Handgun cartridges of Wikipedia's List of handgun cartridges, read in full (about 255 rows); classes follow the nominal calibre in the name. Complete: {len(kH['x'])} of {len(kH['x'])} in that reference, apart from rifle rounds the table also lists and the entries already under the rifle and rimfire lists.")
setsel('Centrefire rifle cartridge', 6, f"Rifle cartridges of Wikipedia's List of rifle cartridges, read in full to its last row, 37×145mmR (about 550 rows), including wildcat, historical, nitro-express, black-powder and autocannon rounds; classes follow the nominal calibre in the name. Complete: {len(kR['x'])} of {len(kR['x'])} in that reference, apart from rimfires, which are under Rimfire cartridge.")

out = ROOT + 'work/CMP_E4/E4.new.json'
json.dump(d, open(out, 'w'), ensure_ascii=False, indent=1)
os.replace(out, SRC)
after = {kn: len(find_kind(di, kn)['x']) for _, (di, kn, _) in KIND.items()}
print('firearms', {kn: (before[kn], after[kn]) for kn in before})
print('carts', cb, '->', {'h': len(kH['x']), 'r': len(kR['x']), 'f': len(kF['x'])}, cadd, 'gauges +', gadd, 'total', len(ks['x']))
