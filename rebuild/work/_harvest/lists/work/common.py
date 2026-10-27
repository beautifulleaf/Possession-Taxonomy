import json, re, unicodedata, os, glob, collections
R = '/home/user/Possession-Taxonomy/rebuild/'
def nk(s):
    s = s.translate(str.maketrans({'ø':'o','Ø':'O','æ':'ae','Æ':'AE','ß':'ss','ł':'l','Ł':'L','đ':'d','œ':'oe','Œ':'OE','’':"'"}))
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]', '', s)
STRIP = r'\b(by|the|maison|parfums?|perfumes?|perfumery|parfumerie|parfumeur|fragrances?|profumi|profumo|paris|london|nyc|co|editions de parfums|prives|australia|los angeles|beauty|cosmetics|skincare|skin care|haircare|professional|milano|new york)\b'
def ck(s):
    s2 = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return nk(re.sub(STRIP, ' ', s2)) or nk(s)
MAIN = ['end', 'ssense', 'sephora', 'watchcharts', 'rebag', 'luckyscent', 'fragrantica_popular']
NN = ['notino', 'nordstrom']
SRC = {'end': 'https://www.endclothing.com/en-us/pages/menswear-brands', 'ssense': 'https://www.ssense.com/en-at/men/designers/a-a-spectrum/coats',
       'sephora': 'https://www.sephora.com/brands-list', 'watchcharts': 'https://watchcharts.com/watches/brands',
       'rebag': 'https://support.rebag.com/hc/en-us/articles/360039209512-What-designers-does-Rebag-accept',
       'luckyscent': 'https://www.luckyscent.com/brands', 'fragrantica_popular': 'https://www.fragrantica.com/designers/',
       'fashiola': 'https://www.fashiola.com/brands/', 'notino': 'https://www.notino.co.uk/beauty-brands/', 'nordstrom': 'https://www.nordstrom.com/brands-list'}
def rd(l): return [x.strip().strip('*\\').strip() for x in open(R + f'work/_harvest/lists/{l}.txt').read().strip().split('|') if x.strip().strip('*\\').strip()]
L = {l: rd(l) for l in MAIN + NN}
FD = [l.rstrip('\n').split('\t') for l in open(R + 'work/_harvest/fashiola/decisions.tsv')][1:]
SCOPE19 = [r[0] for r in FD if r[5] == 'scope']
L['fashiola'] = json.load(open(R + 'work/_harvest/fashiola/names.json'))['all']
L['H4'] = [b['n'] for b in json.load(open(R + 'work/_harvest/H4.json'))['b']]
KEYS = {l: set() for l in L}
for l, v in L.items():
    for x in v: KEYS[l] |= {nk(x), ck(x)}
FALSE = {('Odette Parfum Co.', 'nordstrom'), ('Tada Parfumeur', 'nordstrom'), ('Arte Profumi', 'end'), ('Rare London', 'notino'),
         ('Lola Cosmetics', 'nordstrom'), ('LOLA', 'notino')}
def on(n, extra=()):
    s = {l for l in L if (nk(n) in KEYS[l] or ck(n) in KEYS[l]) and (n, l) not in FALSE}
    return s | set(extra)
def items():
    out = [(l, n) for l in MAIN for n in L[l]] + [('fashiola', n) for n in SCOPE19] + [(l, n) for l in NN for n in L[l]]
    return out
def register():
    reg = {}
    for r in json.load(open(R + 'reader/_brand_index.json'))['b']:
        for a in (r[0], r[4], re.sub(r' \(.*', '', r[0])):
            if a: reg.setdefault(nk(a), r[0])
    harv = {}
    for p in glob.glob(R + 'work/_harvest/*.json'):
        for b in json.load(open(p))['b']: harv.setdefault(nk(b['n']), b['n'])
    return reg, harv
FRAG_LISTS = ['luckyscent', 'sephora', 'notino', 'nordstrom', 'fashiola', 'H4']
NICE = {'luckyscent': 'Luckyscent', 'sephora': 'Sephora', 'notino': 'Notino', 'nordstrom': 'Nordstrom', 'fashiola': 'Fashiola', 'H4': 'the earlier H4 harvest'}
