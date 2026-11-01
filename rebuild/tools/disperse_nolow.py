"""Owner 2026-11-01: "get rid of the low and no ghettoization as it applies to only one category anyway, just
disperse it there." The J7 department "No & low alcohol" is dissolved: its shelves join their full-strength
equivalents (beer, wine styles, spirits); the cross-category No & low view is removed from the page."""
import json, os, re, shutil
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); p = f'{R}/out/J7.json'
os.makedirs(f'{R}/work/NOLOW', exist_ok=True); shutil.copy(p, f'{R}/work/NOLOW/J7.json.before')
d = json.load(open(p)); nl = next(x for x in d['depts'] if x['n'] == 'No & low alcohol')
sh = {s['n']: s for s in nl['s']}; dep = {x['n']: x for x in d['depts']}
def add(dept, name, kinds, t):
    dep[dept]['s'].append({'n': name, 't': t, 'k': kinds})
add('Beer', 'Alcohol-free & low-alcohol beer', sh['Alcohol-free beer specialists']['k'] + sh['Low-alcohol drinks']['k'],
    'Brewers that make only alcohol-free beer, and the low-alcohol band; alcohol-free versions of mainstream beers stay under their parent brand.')
add('Wine styles across countries', 'Alcohol-free wine', sh['Alcohol-free wine']['k'], 'De-alcoholised still and sparkling wine.')
add('Gin, vodka & aquavit', 'Zero-proof spirits & aperitifs', sh['Zero-proof spirits and aperitifs']['k'], 'Non-alcoholic spirit alternatives and alcohol-free aperitifs.')
d['depts'] = [x for x in d['depts'] if x is not nl]
b = dep['Beer']; b['t'] = b['t'].replace('an alcohol-free beer → No & low alcohol', 'alcohol-free and low-alcohol beer is a shelf here')
steps = [k for k in d['key'] if re.match(r'^\d+\.', k) and not k.rstrip().endswith('→ No & low alcohol')]
notes = [k.replace('alcohol-free versions of full-strength drinks stay with their parent and appear in the No & low view.',
                   'an alcohol-free or low-alcohol drink goes with its full-strength kind (beer, wine style, spirit); alcohol-free versions of a brand stay with their parent.')
         for k in d['key'] if not re.match(r'^\d+\.', k)]
d['key'] = [f'{i + 1}. ' + re.sub(r'^\d+\.\s*', '', k) for i, k in enumerate(steps)] + notes
d['lead'] = re.sub(r',? ?(and )?no[- ]and[- ]low[^,.;]*', '', d.get('lead', ''), flags=re.I)
json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
print('J7 departments', len(d['depts']), 'key steps', len(steps))
