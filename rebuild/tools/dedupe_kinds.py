"""Fold duplicate kind names inside one category file (out/<CODE>.json): the copy with more entries is kept, the other's
entries (by name), types and see-links are added to it, and the empty copy is dropped. Usage: python3 tools/dedupe_kinds.py CODE"""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
code = sys.argv[1]; p = f'out/{code}.json'; d = json.load(open(p))
by = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: by.setdefault(k['n'], []).append((dp['n'], s['n'], k))
for n, locs in by.items():
    if len(locs) < 2: continue
    keep = max(locs, key=lambda t: len(t[2].get('x') or []))[2]
    have = {x['n'].lower() for x in keep.get('x') or []}
    for _, _, k in locs:
        if k is keep: continue
        for x in k.get('x') or []:
            if x['n'].lower() not in have: keep.setdefault('x', []).append(x); have.add(x['n'].lower())
        for s in k.get('see') or []:
            if s not in (keep.get('see') or []): keep.setdefault('see', []).append(s)
    print('folded', n, [(a, b) for a, b, _ in locs])
    for dp in d['depts']:
        for s in dp['s']: s['k'] = [k for k in s['k'] if k['n'] != n or k is keep]
for dp in d['depts']: dp['s'] = [s for s in dp['s'] if s['k']]
json.dump(d, open(p + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(p + '.tmp', p)
