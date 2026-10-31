import json, os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src import SRC, SEG
R = '/home/user/Possession-Taxonomy/rebuild/'
reg = {b['n'].strip().lower(): b for b in json.load(open(R+'reader/_brands.json'))['b']}
a2 = {k for k, b in reg.items() if 'A2' in (b.get('cats') or [])}
out, seen, skipped, linked = [], set(), [], []
for f in sorted(glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/d*.txt')):
    for line in open(f, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip(): continue
        p = [x.strip() for x in line.split('|')]
        p += [''] * (7 - len(p))
        n, sg, kf, c, fy, s, d = p[:7]
        k = n.lower()
        if k in a2: skipped.append(n); continue
        if k in seen: continue
        seen.add(k)
        b = {'n': n, 'seg': SEG[sg], 'kf': kf, 's': SRC[s]}
        if c: b['c'] = c
        if fy: b['f'] = fy
        if d: b['d'] = d
        if k in reg: linked.append(n)
        out.append(b)
tmp = R + 'work/_harvest/A2.json.tmp'
json.dump({'b': out}, open(tmp, 'w'), ensure_ascii=False, indent=0)
os.replace(tmp, R + 'work/_harvest/A2.json')
from collections import Counter
print(len(out), 'written; skipped existing A2:', skipped)
print('linked (in register under other cats):', len(linked), linked)
print(Counter(b['seg'] for b in out))
