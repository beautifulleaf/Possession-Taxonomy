import json, sys
p = 'out/H1_parts/SKIN.json'; d = json.load(open(p))
TIERS = {'Global groups', 'National champions', 'Independents', 'Craft & indie', 'Own label', 'Owner not stated'}
NAME = {'Skincare': 'Skin-care brand', 'Make-up': 'Make-up brand'}
for dp in d['depts']:
    tier_sh = [s for s in dp['s'] if s['n'] in TIERS]; rest = [s for s in dp['s'] if s['n'] not in TIERS]
    ents, seen, sels = [], set(), []
    for s in tier_sh:
        for k in s['k']:
            sels.append(k.get('sel', ''))
            for x in k.get('x') or []:
                if x['n'].lower() in seen: continue
                seen.add(x['n'].lower())
                x['g'] = x.get('own') if s['n'] == 'Global groups' and x.get('own') else (s['n'] if s['n'] != 'Global groups' else k['n'])
                ents.append(x)
    order = {n: i for i, n in enumerate(['Global groups', 'National champions', 'Independents', 'Craft & indie', 'Own label', 'Owner not stated'])}
    kind = {'n': NAME[dp['n']], 'd': f"Brands sold under their own name in {dp['n'].lower()}, grouped by owner group, then national champions, independents, craft and indie, own label, and brands whose owner no fetched page states.",
            'nl': 'One entry is a brand sold under its own name; its product lines are versions.',
            'sel': 'Follows each global group\'s brand pages and fetched national, independent and indie overviews; ' + ' '.join(sorted({s.split(';')[-1].strip() for s in sels if 'Covers' in s}))[:400],
            'xg': 'by owner group, then market tier', 'x': ents}
    shelf = {'n': 'Brands by market', 't': f"Every {dp['n'].lower()} brand on the fetched group, national and indie lists; the product kinds below say what each product is.", 'k': [kind]}
    dp['s'] = [shelf] + rest
    print(dp['n'], len(ents))
json.dump(d, open(p + '.tmp', 'w'), ensure_ascii=False); import os; os.replace(p + '.tmp', p)
