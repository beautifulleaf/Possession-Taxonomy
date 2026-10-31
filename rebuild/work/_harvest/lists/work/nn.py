import json, re, unicodedata, os, glob, collections
os.chdir('/home/user/Possession-Taxonomy/rebuild')
def nk(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]', '', s)
STRIP = r'\b(by|the|maison|parfums?|perfumes?|perfumery|parfumerie|parfumeur|fragrances?|profumi|profumo|paris|london|nyc|co|editions de parfums|prives|australia|los angeles|beauty|cosmetics|skincare|skin care|haircare|professional|milano|new york)\b'
def ck(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return nk(re.sub(STRIP, ' ', s)) or nk(s)
def rd(l): return [x.strip().strip('*').strip() for x in open(f'work/_harvest/lists/{l}.txt').read().strip().split('|') if x.strip()]
L = {l: rd(l) for l in ['end','ssense','sephora','watchcharts','rebag','luckyscent','fragrantica_popular','notino','nordstrom']}
L['fashiola'] = json.load(open('work/_harvest/fashiola/names.json'))['all']
L['H4'] = [b['n'] for b in json.load(open('work/_harvest/H4.json'))['b']]
keys = {l: collections.defaultdict(list) for l in L}
for l, v in L.items():
    for x in v:
        keys[l][nk(x)].append(x); keys[l][ck(x)].append(x)
def on(n):
    return sorted({l for l in L if nk(n) in keys[l] or ck(n) in keys[l]})
reg = {}
for r in json.load(open('reader/_brand_index.json'))['b']:
    for a in (r[0], r[4], re.sub(r' \(.*', '', r[0])):
        if a: reg.setdefault(nk(a), r[0])
for p in glob.glob('work/_harvest/*.json'):
    for b in json.load(open(p))['b']: reg.setdefault(nk(b['n']), b['n'])
out = []
for l in ('notino', 'nordstrom'):
    for n in L[l]:
        o = on(n); other = [x for x in o if x not in ('notino','nordstrom','H4','fragrantica_popular','watchcharts','rebag')]
        hit = reg.get(nk(n)) or reg.get(ck(n)) if len(ck(n))>3 else reg.get(nk(n))
        out.append(dict(list=l, name=n, on=o, hit=hit or ''))
json.dump(out, open('work/_harvest/lists/work/nn.json','w'), ensure_ascii=False, indent=0)
c = collections.Counter()
for r in out:
    o=r['on']; core=[x for x in o if x in ('end','ssense','sephora','luckyscent','fragrantica_popular','watchcharts','rebag')]
    if r['hit']: c[r['list'],'reg']+=1
    elif core: c[r['list'],'onmainlist']+=1
    elif ('notino' in o and 'nordstrom' in o) or 'fashiola' in o: c[r['list'],'pass']+=1
    else: c[r['list'],'fail']+=1
print(c)
