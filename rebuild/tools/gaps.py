"""Gap register: per category, kinds with loose models, kinds with entries but no coverage line, and partial coverage lines.
Usage: python3 tools/gaps.py [--md out.md]"""
import json, glob, os, sys, re
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
rows = []
for f in sorted(glob.glob('reader/[A-J]*.json')):
    c = os.path.basename(f)[:-5]; d = json.load(open(f))
    m = nosel = part = comp = ents = kinds = 0; partial = []
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                kinds += 1; x = k.get('x') or []; ents += len(x)
                if k.get('m'): m += 1
                if not x: continue
                sel = k.get('sel') or ''
                if re.search(r'\bComplete\b', sel): comp += 1
                elif re.search(r'\bCovers\b|open set|no complete', sel, re.I): part += 1; partial.append(k['n'])
                else: nosel += 1
    rows.append((c, kinds, ents, m, nosel, part, comp, partial))
print('code kinds entries loose_m no_cov partial complete')
for r in rows: print(*r[:7])
if '--md' in sys.argv:
    with open(sys.argv[sys.argv.index('--md') + 1], 'w') as o:
        for r in rows:
            o.write(f"## {r[0]}: {r[2]} entries; loose-model kinds {r[3]}, no coverage line {r[4]}, partial {r[5]}, complete {r[6]}\n")
            if r[7]: o.write('Partial: ' + '; '.join(r[7]) + '\n')
            o.write('\n')
