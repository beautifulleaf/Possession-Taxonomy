"""Owner 2026-11-01: "The wine sections being spread across multiple different pages is unnecessary."
J7's sixteen "Wine of …" departments and "Wine styles across countries" become one department, Wine; their
shelves keep their order, prefixed with the country where the shelf name is a sub-region. Grape varieties stays."""
import json, os, re, shutil
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); p = f'{R}/out/J7.json'
os.makedirs(f'{R}/work/WINE', exist_ok=True); shutil.copy(p, f'{R}/work/WINE/J7.json.before')
d = json.load(open(p))
PFX = {'Wine of France': 'France', 'Wine of Italy': 'Italy', 'Wine of Spain & Portugal': 'Spain & Portugal',
       'Wine of the United States': 'United States', 'Wine of South Africa': 'South Africa'}
wine = [x for x in d['depts'] if x['n'].startswith('Wine of ') or x['n'] == 'Wine styles across countries']
shelves = []
for x in wine:
    for s in x['s']:
        s = dict(s)
        if x['n'] in PFX: s['n'] = PFX[x['n']] + ' · ' + s['n']
        elif s['n'] == 'Zones': s['n'] = 'Australia · Zones'
        elif x['n'] == 'Wine styles across countries': s['n'] = 'Styles · ' + s['n']
        if not s.get('t') and x.get('t'): s['t'] = x['t']
        shelves.append(s)
first = d['depts'].index(wine[0])
new = {'n': 'Wine', 't': 'Wine as bought, by country and region with appellation archetypes, then styles made across countries (sparkling, rosé and orange, sweet, fortified, alcohol-free).',
       'ax': 'Country, then region; styles that cross countries last.', 's': shelves}
for k in ('mode',):
    if wine[0].get(k): new[k] = wine[0][k]
d['depts'] = d['depts'][:first] + [new] + [x for x in d['depts'][first:] if x not in wine]
steps = [k for k in d['key'] if re.match(r'^\d+\.', k)]; notes = [k for k in d['key'] if not re.match(r'^\d+\.', k)]
out, done = [], False
for k in steps:
    b = re.sub(r'^\d+\.\s*', '', k)
    if re.search(r'→ (Wine of |Wine styles across countries)', b):
        if not done: out.append('Is it a wine, by place name or by style? → Wine'); done = True
        continue
    out.append(b)
d['key'] = [f'{i + 1}. {b}' for i, b in enumerate(out)] + [n.replace('is placed by its country before its style', 'is placed under its country before its style, inside Wine') for n in notes]
json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
print('Wine shelves', len(shelves), 'J7 departments', len(d['depts']), 'key steps', len(out))
