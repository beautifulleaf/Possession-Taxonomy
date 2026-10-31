import json, os
R = '/home/user/Possession-Taxonomy/rebuild/work/_harvest/'
fix = {('H4', 'Travalo'): 'Refillable perfume atomiser brand stocked by Notino and Nordstrom.',
       ('B4', 'P.F. Candle Co.'): 'Candle and home fragrance maker stocked by Luckyscent and Nordstrom.'}
for (c, n), d in fix.items():
    p = R + c + '.json'; cur = json.load(open(p))
    for b in cur['b']:
        if b['n'] == n: b['d'] = d; print('fixed', n)
    json.dump(cur, open(p + '.tmp', 'w'), ensure_ascii=False, indent=0); os.replace(p + '.tmp', p)
