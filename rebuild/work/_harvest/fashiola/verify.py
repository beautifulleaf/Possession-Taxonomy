import json, re, unicodedata, collections, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
D = 'work/_harvest/fashiola/'
def nk(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]', '', s)
SEGS = json.load(open('SEGMENTS.json'))['domains']
dom = {c: d for d, v in SEGS.items() for c in v['cats'] if c != '*'}
new = json.load(open(D + 'names.json'))['new']
reg = {r[0].strip().lower() for r in json.load(open('reader/_brand_index.json'))['b']}
regk = {nk(r[0]): r[0] for r in json.load(open('reader/_brand_index.json'))['b']}
rows = [l.rstrip('\n').split('\t') for l in open(D + 'decisions.tsv')]
assert rows[0] == ['name', 'action', 'n', 'cat', 'seg', 'kf', 'c', 'f'], rows[0]
rows = rows[1:]; errs = []
c = collections.Counter(r[0] for r in rows)
if sorted(c) != sorted(new) or any(v != 1 for v in c.values()): errs.append('name coverage mismatch')
seen = set()
for r in rows:
    if len(r) != 8: errs.append(f'bad cols {r}'); continue
    name, a, n, cat, seg, kf, cc, f = r
    if a not in ('add', 'skip'): errs.append(f'{name}: action {a}')
    if a == 'add':
        if seg not in SEGS[dom.get(cat, 'general')]['segs']: errs.append(f'{name}: seg {seg} invalid for {cat}')
        if n.lower() in seen: errs.append(f'{name}: duplicate add n {n}')
        seen.add(n.lower())
        if n.lower() in reg: errs.append(f'{name}: n {n} already in register')
        if nk(n) in regk: errs.append(f'{name}: n {n} ~ register {regk[nk(n)]}')
        if not kf or len(kf.split()) > 3: errs.append(f'{name}: kf {kf!r}')
        if f and not re.fullmatch(r'\d{4}', f): errs.append(f'{name}: year {f}')
print('\n'.join(errs) or 'OK', len(rows))
sys.exit(1 if errs else 0)
