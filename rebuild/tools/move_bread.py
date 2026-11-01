"""Owner 2026-11-01: "Move bread/bakery to pantry staples. Something like Little Debbie cakes definitely belongs in
the Sweets and Snacks section but not a fresh loaf of bread." J8 Bread & bakery splits: the bread shelves (bakeries,
loaves, rolls, flatbreads and enriched breads) become J5 Bread; pastries, festive bakes, cakes and the protected
names stay in J8 as Cakes & pastries. Brands filed under the bread kinds move from J8 to J5."""
import json, os, re, shutil
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); W = f'{R}/work/MOVE_BREAD'; os.makedirs(W, exist_ok=True)
for f in ('J8', 'J5', 'J8_brands', 'J5_brands'): shutil.copy(f'{R}/out/{f}.json', f'{W}/{f}.json.before')
j8, j5 = json.load(open(f'{R}/out/J8.json')), json.load(open(f'{R}/out/J5.json'))
bb = next(x for x in j8['depts'] if x['n'] == 'Bread & bakery')
BREAD = ['Bakeries', 'Loaves', 'Rolls, flatbreads & enriched breads']
bread = {'n': 'Bread', 't': 'Bread bought from a baker or shop, fresh or packaged, listed by bakery and brand, then by the forms it comes in: loaves, rolls, flatbreads and enriched breads; a cake, pastry or snack cake → Bakery, Sweets & Snacks (Cakes & pastries); a dish made from bread belongs in the Culinary Taxonomy.',
         's': [s for s in bb['s'] if s['n'] in BREAD]}
if bb.get('mode'): bread['mode'] = bb['mode']
if bb.get('ax'): bread['ax'] = 'Bakeries first, then loaves, then rolls, flatbreads and enriched breads.'
bb['s'] = [s for s in bb['s'] if s['n'] not in BREAD]; bb['n'] = 'Cakes & pastries'
bb['t'] = 'Cakes, pastries and festive bakes bought fresh or packaged, from a patisserie or as snack cakes, listed by brand and market, then by form; a loaf, roll or flatbread → Pantry Staples (Bread); a dry biscuit → Biscuits & crackers; a chocolate bar → Chocolate.'
bkinds = {k['n'] for s in bread['s'] for k in s['k']}
i = next(n for n, x in enumerate(j5['depts']) if x['n'] == 'Flour, sugar & baking'); j5['depts'].insert(i + 1, bread)
j8['key'] = [k.replace('Is it a loaf, roll, flatbread, pastry or cake sold fresh or packaged from a bakery? → Bread & bakery', 'Is it a cake, pastry, doughnut, snack cake or festive bake, sold fresh or packaged? → Cakes & pastries')
             .replace('a doughnut or cake is bakery (step 1) even when iced', 'a doughnut or cake is Cakes & pastries (step 1) even when iced; a loaf, roll or flatbread is Pantry Staples (Bread)') for k in j8['key']]
st = [re.sub(r'^\d+\.\s*', '', k) for k in j5['key'] if re.match(r'^\d+\.', k)]; no = [k for k in j5['key'] if not re.match(r'^\d+\.', k)]
st.insert(st.index(next(b for b in st if b.endswith('→ Flour, sugar & baking'))) + 1, 'Is it bread: a loaf, roll, bagel, flatbread or enriched bread, fresh or packaged? → Bread')
j5['key'] = [f'{n + 1}. {b}' for n, b in enumerate(st)] + [x.replace('before any ingredient step;', 'before any ingredient step; a cake or pastry is Bakery, Sweets & Snacks, a loaf is Bread;') for x in no]
for f, o in (('J8', j8), ('J5', j5)): json.dump(o, open(f'{R}/out/{f}.json', 'w'), ensure_ascii=False, indent=1)
# brands: those filed under a bread kind (work/BRAND_DEPTS), or under the old department with a bread known-for
dk = json.load(open(f'{R}/work/BRAND_DEPTS/J8.json'))
ALSO_SWEET = {'Pepperidge Farm', 'Grupo Bimbo'}  # cookies (Milano) and snack cakes (Entenmann's, Marinela) beside their bread
B8, B5 = json.load(open(f'{R}/out/J8_brands.json')), json.load(open(f'{R}/out/J5_brands.json'))
have5 = {b['n'] for b in B5['b']}; keep, moved = [], []
for b in B8['b']:
    d = dk.get(b['n']); kf = (b.get('kf') or '').lower()
    isbread = d and d[0] == 'Bread & bakery' and (d[1] in bkinds or (not d[1] and re.search(r'bread|bakery|bagel|loaf|tortilla|naan|pita|roll', kf) and not re.search(r'cake|pastr|panettone|stollen|biscuit|cookie|doughnut|patisser', kf)))
    if isbread:
        moved.append(b['n'])
        if b['n'] not in have5: B5['b'].append(b)
        # a baker that also makes cakes, biscuits, snacks or chocolate stays in J8 as well
        if re.search(r'cake|biscuit|cookie|cracker|chocolate|confection|snack|sweet|pastr|doughnut|patisser|wafer', (b.get('kf') or '') + ' ' + (b.get('d') or ''), re.I) or b['n'] in ALSO_SWEET: keep.append(b)
    else: keep.append(b)
B8['b'] = keep
for f, o in (('J8_brands', B8), ('J5_brands', B5)): json.dump(o, open(f'{R}/out/{f}.json', 'w'), ensure_ascii=False, indent=1)
rp = f'{R}/work/DEPT_RENAMES.json'; rn = json.load(open(rp)) if os.path.exists(rp) else {}
rn.setdefault('J8', {})['Bread & bakery'] = 'Cakes & pastries'; json.dump(rn, open(rp, 'w'), ensure_ascii=False, indent=1)
open(f'{W}/moved_brands.txt', 'w').write('\n'.join(moved) + '\n')
print('bread kinds', len(bkinds), 'brands moved to J5', len(moved), 'J8 brands kept', len(keep))
