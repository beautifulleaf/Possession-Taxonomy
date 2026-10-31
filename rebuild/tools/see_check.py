"""Check every `see` link in reader/<CODE>.json: retarget links whose target kind was renamed (out/<CODE>_renames.json),
drop links to kinds that no longer exist, report both. Usage: python3 tools/see_check.py [--fix]"""
import json, glob, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
fix = '--fix' in sys.argv
files = sorted(p for p in glob.glob('reader/[A-J]*.json'))
data = {os.path.basename(p)[:-5]: json.load(open(p)) for p in files}
names = {c: {k['n'] for dp in d['depts'] for s in dp['s'] for k in s['k']} for c, d in data.items()}
low = {c: {n.lower(): n for n in ns} for c, ns in names.items()}
OVR = json.load(open('see_override.json')) if os.path.exists('see_override.json') else {}  # coordinator: 'CODE>kind' -> exact new target
ren = {c: json.load(open(f'out/{c}_renames.json')) for c in data if os.path.exists(f'out/{c}_renames.json')}
fixed = dropped = total = 0; changed = set()
for c, d in data.items():
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                out = []
                for sv in k.get('see') or []:
                    total += 1; tc, tn = sv[0], sv[1]
                    if tc in names and tn in names[tc]: out.append(sv); continue
                    new = OVR.get(f'{c}:{k["n"]}>{tc}:{tn}')
                    if new == '-': dropped += 1; print('removed', c, k['n'], '->', tc, tn); continue
                    new = new or (low.get(tc, {}).get(tn.lower()) or (ren.get(tc, {}).get(tn) if ren.get(tc, {}).get(tn) in names.get(tc, ()) else None))
                    if new: out.append([tc, new] + sv[2:]); fixed += 1; print('retarget', c, k['n'], '->', tc, tn, '=>', new)
                    else: dropped += 1; print('dangling', c, k['n'], '->', tc, tn)
                if out != (k.get('see') or []):
                    changed.add(c)
                    if out: k['see'] = out
                    else: k.pop('see', None)
if fix:
    for c in changed:
        p = f'reader/{c}.json'; json.dump(data[c], open(p + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(p + '.tmp', p)
        o = f'out/{c}.json'  # keep out/ in step so a later merge does not bring the bad link back
        if os.path.exists(o): json.dump(data[c], open(o + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(o + '.tmp', o)
print(f'links {total}, retargeted {fixed}, dangling {dropped}, files changed {len(changed)}' + (' (written)' if fix else ' (dry run)'))
