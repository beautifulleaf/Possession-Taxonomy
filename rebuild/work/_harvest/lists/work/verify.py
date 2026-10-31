import sys, os, json, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
SEGS = json.load(open(R + 'SEGMENTS.json'))['domains']
dom = {c: d for d, v in SEGS.items() for c in v['cats'] if c != '*'}
reg, harv = register()
regn = {r[0].strip().lower() for r in json.load(open(R + 'reader/_brand_index.json'))['b']}
rows = [l.rstrip('\n').split('\t') for l in open(R + 'work/_harvest/lists/decisions.tsv')]
assert rows[0] == ['name', 'list', 'action', 'n', 'cat', 'seg', 'kf', 'c', 'f', 'reason'], rows[0]
rows = rows[1:]; errs = []
want = collections.Counter(items()); got = collections.Counter((r[1], r[0]) for r in rows)
if want != got: errs.append(f'coverage mismatch: missing {list((want-got).items())[:5]} extra {list((got-want).items())[:5]}')
seen = set()
for r in rows:
    if len(r) != 10: errs.append(f'bad cols {r}'); continue
    name, l, a, n, cat, seg, kf, c, f, why = r
    if a not in ('add', 'skip'): errs.append(f'{name}: action {a}')
    if a == 'skip' and not why: errs.append(f'{name}: skip without reason')
    if a == 'add':
        if seg not in SEGS[dom.get(cat, 'general')]['segs']: errs.append(f'{name}: seg {seg} invalid for {cat}')
        if nk(n) in seen: errs.append(f'{name}: duplicate add n {n}')
        seen.add(nk(n))
        if n.lower() in regn or nk(n) in reg: errs.append(f'{name}: n {n} already in register ({reg.get(nk(n))})')
        if nk(n) in harv: errs.append(f'{name}: n {n} already harvested')
        if not kf or len(kf.split()) > 3 or kf != kf.lower() and not re.search(r'[A-Z]', kf[:1] + kf) : pass
        if not kf or len(kf.split()) > 3: errs.append(f'{name}: kf {kf!r}')
        if f and not re.fullmatch(r'\d{4}', f): errs.append(f'{name}: year {f}')
print('\n'.join(errs) or 'OK', len(rows))
sys.exit(1 if errs else 0)
