"""Fold whole departments into another department of the same category, shelf by shelf: kinds join the target's
shelf of the same name (a new shelf is added after the target's shelves when there is none). Records the old->new
department names in work/DEPT_RENAMES.json so filed brands follow (tools/brand_depts.py).
Usage: python3 tools/merge_depts.py CAT "Target" "Source 1" ["Source 2" ...]
Key steps that route to a source are removed (the caller rewrites the target's step)."""
import json, os, re, shutil, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
c, tgt, srcs = sys.argv[1], sys.argv[2], sys.argv[3:]
p = f'{R}/out/{c}.json'; os.makedirs(f'{R}/work/MERGE_DEPTS', exist_ok=True)
shutil.copy(p, f'{R}/work/MERGE_DEPTS/{c}.json.before-' + re.sub(r'\W+', '_', tgt))
d = json.load(open(p)); dep = {x['n']: x for x in d['depts']}; T = dep[tgt]
for sn in srcs:
    S = dep[sn]
    for s in S['s']:
        t = next((x for x in T['s'] if x['n'] == s['n']), None)
        if t is None: T['s'].append(dict(s))
        else:
            have = {k['n'] for k in t['k']}
            t['k'] += [k for k in s['k'] if k['n'] not in have]
    d['depts'].remove(S)
steps = [re.sub(r'^\d+\.\s*', '', k) for k in d['key'] if re.match(r'^\d+\.', k)]
notes = [k for k in d['key'] if not re.match(r'^\d+\.', k)]
steps = [b for b in steps if not any(b.rstrip().endswith('→ ' + sn) for sn in srcs)]
d['key'] = [f'{i + 1}. {b}' for i, b in enumerate(steps)] + notes
json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
rp = f'{R}/work/DEPT_RENAMES.json'; rn = json.load(open(rp)) if os.path.exists(rp) else {}
for sn in srcs: rn.setdefault(c, {})[sn] = tgt
json.dump(rn, open(rp, 'w'), ensure_ascii=False, indent=1)
print(c, tgt, '<-', srcs, '| departments', len(d['depts']))
