import json, re, unicodedata, glob, os
os.chdir('/home/user/Possession-Taxonomy/rebuild')
def nk(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]', '', s)
names = [(r[0], 'reg') for r in json.load(open('reader/_brand_index.json'))['b']]
for p in glob.glob('work/_harvest/*.json'):
    names += [(b['n'], os.path.basename(p)[:-5]) for b in json.load(open(p))['b']]
keys = [(nk(n), n, s) for n, s in names]
pre = json.load(open('work/_harvest/lists/work/pre.json'))
for l, n, hit in pre:
    if hit: continue
    k = nk(n); words = [nk(w) for w in re.split(r'[\s/]+', n) if len(nk(w)) >= 4]
    c = []
    for kk, nn, s in keys:
        if len(kk) < 3: continue
        if (len(k) >= 4 and (k in kk or kk in k)) or (words and nk(words[0]) == kk[:len(words[0])] and len(words[0])>=5):
            c.append(f'{nn}[{s}]')
    print(f'{l} | {n} || ' + '; '.join(c[:8]))
