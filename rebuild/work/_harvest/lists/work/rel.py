import json, re, unicodedata, os
os.chdir('/home/user/Possession-Taxonomy/rebuild')
def nk(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]', '', s)
STRIP = r'\b(by|the|maison|parfums?|perfumes?|perfumery|parfumerie|parfumeur|fragrances?|profumi|profumo|paris|london|nyc|co\.?|editions de parfums|prives|privés|australia|los angeles)\b'
def ck(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(STRIP, ' ', s)
    return nk(s)
def rd(p): return open(p).read().strip().split('|')
LS = rd('work/_harvest/lists/luckyscent.txt'); FP = rd('work/_harvest/lists/fragrantica_popular.txt'); SE = rd('work/_harvest/lists/sephora.txt')
FA = json.load(open('work/_harvest/fashiola/names.json'))['all']
H4 = [b['n'] for b in json.load(open('work/_harvest/H4.json'))['b']]
sets = {k: {ck(x) for x in v} | {nk(x) for x in v} for k, v in dict(luckyscent=LS, sephora=SE, fashiola=FA, H4=H4, fragrantica=FP).items()}
pre = json.load(open('work/_harvest/lists/work/pre.json'))
res = {}
for l, n, h in pre:
    if l not in ('luckyscent', 'fragrantica_popular'): continue
    on = [k for k, s in sets.items() if ck(n) in s or nk(n) in s]
    res[f'{l}|{n}'] = on
    if not h: print(l, '|', n, '|', ','.join(on))
json.dump(res, open('work/_harvest/lists/work/rel.json', 'w'), indent=0)
