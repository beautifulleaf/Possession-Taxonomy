import json, re, unicodedata, glob, os, sys
os.chdir('/home/user/Possession-Taxonomy/rebuild')
def nk(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]', '', s)
reg = {}
for r in json.load(open('reader/_brand_index.json'))['b']:
    reg.setdefault(nk(r[0]), r[0])
    if r[4]: reg.setdefault(nk(r[4]), r[0])
    m = re.match(r'(.*?) \(', r[0])
    if m: reg.setdefault(nk(m.group(1)), r[0])
harv = {}
for p in glob.glob('work/_harvest/*.json'):
    c = os.path.basename(p)[:-5]
    for b in json.load(open(p))['b']: harv.setdefault(nk(b['n']), f"{c}:{b['n']}")
L = ['end','ssense','sephora','watchcharts','rebag','luckyscent','fragrantica_popular']
items = []
for l in L:
    for n in open(f'work/_harvest/lists/{l}.txt').read().strip().split('|'):
        items.append((l, n.strip()))
fd = [l.rstrip('\n').split('\t') for l in open('work/_harvest/fashiola/decisions.tsv')][1:]
for r in fd:
    if r[5] == 'scope': items.append(('fashiola', r[0]))
out = []
for l, n in items:
    k = nk(n)
    hit = reg.get(k) and 'reg:' + reg[k] or harv.get(k)
    out.append((l, n, hit or ''))
json.dump(out, open('work/_harvest/lists/work/pre.json', 'w'), ensure_ascii=False, indent=0)
import collections
print(len(out), collections.Counter((o[0], bool(o[2])) for o in out))
for o in out:
    if not o[2]: print(o[0], '|', o[1])
