"""Species register (owner decision, batch 4): rare mineral species are kept out of the F6 tree and listed here instead.
  python3 tools/species.py      rebuild reader/_species.json from every category whose plan drops kinds to the species register
Each entry keeps the old kind exactly as it was (name, aliases, definition, models, old source); nothing is added."""
import json, os, glob, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
out = []
for pp in sorted(glob.glob('work/*/plan.json')):
    c = pp.split('/')[1]; plan = json.load(open(pp))
    drop = {d['old'] for d in plan.get('drop', []) if 'species register' in d.get('why', '')}
    if not drop: continue
    old = json.load(open(f'work/{c}/old.json'))
    for dp in old['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k.get('id') in drop:
                    cls = re.search(r'specimen \((\w[\w -]*);', k.get('d', ''))
                    out.append({'c': c, 'g': (cls.group(1).capitalize() + 's') if cls else dp['n'], 'n': k['n'], 'a': k.get('a', ''), 'd': k.get('d', ''),
                                'm': [m[0] for m in k.get('m', [])], 's': k.get('s', '')})
out.sort(key=lambda e: (e['c'], e['g'], e['n'].lower()))
tmp = 'reader/_species.json.tmp'
json.dump({'i': out}, open(tmp, 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(tmp, 'reader/_species.json')
print('species', len(out))
