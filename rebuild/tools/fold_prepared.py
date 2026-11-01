"""Owner 2026-11-01: "the frozen/prepared section is a random assortment right now, pizza rolls are a legitimately
uniquely processed frozen 'dish' that probably ends up in the snacks, but hummus is a dish and out of scope."
J5 Prepared & frozen foods is dissolved: products that only exist as processed packaged goods go to their kind's
home (frozen savoury snacks to J8, frozen potato products to J4, frozen waffles to J5 Bread); dishes go to the
Culinary hand-off (work/PREPARED/to_culinary.json) with the brands filed only under them; baby food stays as its
own J5 department."""
import json, os, re, shutil
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); W = f'{R}/work/PREPARED'; os.makedirs(W, exist_ok=True)
for f in ('J4', 'J5', 'J8', 'J5_brands', 'J4_brands', 'J8_brands'): shutil.copy(f'{R}/out/{f}.json', f'{W}/{f}.json.before')
T = {c: json.load(open(f'{R}/out/{c}.json')) for c in ('J4', 'J5', 'J8')}
dep = lambda c, n: next(x for x in T[c]['depts'] if x['n'] == n)
pf = dep('J5', 'Prepared & frozen foods'); K = {k['n']: k for s in pf['s'] for k in s['k']}
TO = {'J8': ('Crisps & savoury snacks', 'Frozen savoury snacks', ['Pizza rolls', 'Stuffed sandwiches and turnovers', 'Frozen crispy pancakes and coated savouries'],
             'Uniquely processed frozen snacks sold to heat from the packet: pizza rolls, filled pockets, coated savouries.'),
      'J4': ('Roots, tubers & bulbs', 'Frozen potato products', ['Frozen chips and fries', 'Tater tots and hash browns'], 'Potato products processed and frozen to cook from frozen.'),
      'J5': ('Bread', 'Frozen waffles & breakfast bakes', ['Frozen waffles and breakfast foods'], 'Waffles and breakfast bakes sold frozen to toast.')}
moved = {}
for c, (dn, sn, ks, t) in TO.items():
    dep(c, dn)['s'].append({'n': sn, 't': t, 'k': [K[k] for k in ks]})
    for k in ks: moved[k] = (c, dn, sn)
DISH = [k for k in K if k not in moved and not re.search(r'baby|infant|toddler', k, re.I)]
baby = [s for s in pf['s'] if s['n'] == 'Baby food']
pf.update({'n': 'Baby food', 's': baby, 't': 'Baby purées and pouches, infant cereals and toddler meals and snacks, bought packaged; infant formula and toddler milk → Dairy, Eggs & Alternatives.'})
j5k = [re.sub(r'^\d+\.\s*', '', k) for k in T['J5']['key'] if re.match(r'^\d+\.', k)]; no = [k for k in T['J5']['key'] if not re.match(r'^\d+\.', k)]
j5k = [('Is it baby food: a purée, pouch, infant cereal or toddler meal or snack? → Baby food' if b.endswith('→ Prepared & frozen foods') else b) for b in j5k]
T['J5']['key'] = [f'{i + 1}. {b}' for i, b in enumerate(j5k)] + [x.replace('a ready-to-heat meal is a prepared food (step 11) before any ingredient step;', 'a ready meal, dip or soup is a dish (Culinary taxonomy); pizza rolls and filled pockets are Bakery, Sweets & Snacks; frozen chips are Fruit & Vegetables;') for x in no]
for c in T: json.dump(T[c], open(f'{R}/out/{c}.json', 'w'), ensure_ascii=False, indent=1)
# brands filed under the kinds (work/BRAND_DEPTS/J5.json): follow moved kinds; dish-only makers go to the hand-off
dk = json.load(open(f'{R}/work/BRAND_DEPTS/J5.json'))
B = {c: json.load(open(f'{R}/out/{c}_brands.json')) for c in ('J4', 'J5', 'J8')}
keep, defer, mv = [], [], []
FIX = {"Totino's": 'Pizza rolls', 'Ore-Ida': 'Tater tots and hash browns', "Aunt Bessie's": 'Frozen chips and fries'}  # coordinator check of the dish list
for b in B['J5']['b']:
    d = dk.get(b['n'])
    if b['n'] in FIX: d = ('Prepared & frozen foods', FIX[b['n']]) if FIX[b['n']] else None
    if d and d[0] == 'Prepared & frozen foods' and d[1] in moved:
        c = moved[d[1]][0]; mv.append((b['n'], c))
        if c != 'J5':
            if not any(x['n'] == b['n'] for x in B[c]['b']): B[c]['b'].append(b)
            continue
    if d and d[0] == 'Prepared & frozen foods' and d[1] in DISH: defer.append(b); continue
    keep.append(b)
B['J5']['b'] = keep
for c in B: json.dump(B[c], open(f'{R}/out/{c}_brands.json', 'w'), ensure_ascii=False, indent=1)
json.dump({'kinds': [K[k] for k in DISH], 'brands': defer, 'why': 'dishes are the Culinary taxonomy (owner 2026-11-01)'}, open(f'{W}/to_culinary.json', 'w'), ensure_ascii=False, indent=1)
rp = f'{R}/work/DEPT_RENAMES.json'; rn = json.load(open(rp)) if os.path.exists(rp) else {}
rn.setdefault('J5', {})['Prepared & frozen foods'] = 'Baby food'; json.dump(rn, open(rp, 'w'), ensure_ascii=False, indent=1)
print('to Culinary:', DISH, '| dish brands deferred', len(defer), '| brands moved', len(mv), [m for m in mv][:8])
