import json,os
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'B7.json')); br=json.load(open(R+'B7_brands.json'))
have={b['n'] for b in br['b']}
removed={}; rep=[]
def kinds():
    for dep in d['depts']:
        for s in dep['s']:
            for k in s['k']: yield dep,k
for dep,k in kinds():
    if k['n'].startswith('Electric fan (design'):
        for e in k['x']:
            e['g']={'Emerson Northwind':'Early electric fans, 1890s to 1950s','Vornado air circulator':'Early electric fans, 1890s to 1950s'}.get(e['n'],'Designer fans, 2009 onward')
        k['x'][0]['role']='origin'
        k['xg']='Era'
        k['nl']='One entry is a named electric fan model line collected or chosen for its maker and design; generations and revivals are versions.'
        k['sel']='No whole-space reference exists for collectable and designer fans. The list follows the maker histories on Wikipedia (Emerson Electric, Vornado Air, the Dyson Air Multiplier and Balmuda pages) and names one origin and three design landmarks of the kind.'
        continue
    n=0
    for f in('m','r'):
        for it in k.pop(f,[]):
            n+=1
            removed.setdefault(it[1],[]).append(it[0])
    k.pop('x',None)
    rep.append((k['n'],n))
new=[]
for mk in sorted(removed):
    if mk not in have:
        new.append(mk); br['b'].append({'n':mk,'c':'','f':'','seg':'','d':'','lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':'','kf':''})
print(rep); print('new brands',new)
ms={
'Air cleaning & monitoring':([{"mkt":"Global air purifiers","who":"Honeywell","share":"over 4.5 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/air-purifiers-market","note":"market revenue; leader"},
 {"mkt":"Global air purifiers","who":"Coway","share":"4.0 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/air-purifiers-market","note":"market revenue"},
 {"mkt":"Global air purifiers","who":"Dyson","share":"3.8 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/air-purifiers-market","note":"market revenue"},
 {"mkt":"Global air purifiers","who":"Honeywell, Coway, Dyson, Levoit and Xiaomi together","share":"17.3 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/air-purifiers-market","note":"market revenue; the page gives no separate shares for Levoit or Xiaomi"}],
 "Air purifiers are a fragmented market: the five largest makers hold about 17 per cent of world revenue, with Honeywell, Coway and Dyson each near 4 per cent (one market-research firm, 2025)."),
'Air conditioners & coolers':([{"mkt":"Global portable air conditioners","who":"LG Electronics","share":"18.2 %","yr":2026,"s":"https://www.verifiedmarketresearch.com/blog/leading-portable-air-conditioner-companies/","note":"estimate from a Q1 2026 vendor report; basis and year of data not stated"},
 {"mkt":"Global portable air conditioners","who":"Haier Group","share":"15.8 %","yr":2026,"s":"https://www.verifiedmarketresearch.com/blog/leading-portable-air-conditioner-companies/","note":"estimate, comparison table only; basis not stated"},
 {"mkt":"Global portable air conditioners","who":"Midea Group","share":"13.9 %","yr":2026,"s":"https://www.verifiedmarketresearch.com/blog/leading-portable-air-conditioner-companies/","note":"estimate, comparison table only; basis not stated"},
 {"mkt":"Global portable air conditioners","who":"Daikin","share":"11.5 %","yr":2026,"s":"https://www.verifiedmarketresearch.com/blog/leading-portable-air-conditioner-companies/","note":"estimate, comparison table only; basis not stated"}],
 "One vendor report estimates LG, Haier, Midea and Daikin as the four largest portable air-conditioner makers, together near 59 per cent; its method is not stated."),
'Fans':([{"mkt":"Global bladeless fans","who":"Dyson","share":"28.5 %","yr":2025,"s":"https://dataintelo.com/report/bladeless-fan-market","note":"estimated global share; the page does not say whether by revenue"},
 {"mkt":"Global bladeless fans","who":"Dyson, Midea Group, Xiaomi, Honeywell International and Panasonic together","share":"57.3 %","yr":2025,"s":"https://dataintelo.com/report/bladeless-fan-market","note":"estimated share of total global market revenue"}],
 "No ranking was found for fans as a whole. In bladeless fans one research firm estimates Dyson at 28.5 per cent of the world market in 2025."),
'Humidity control':([{"mkt":"Global residential portable dehumidifiers","who":"Midea","share":"approx. 15 %","yr":2025,"s":"https://www.businessresearchinsights.com/market-reports/residential-portable-dehumidifier-market-104994","note":"unit shipments; page has a 2025 base year, no year on the figure"},
 {"mkt":"Global residential portable dehumidifiers","who":"Haier","share":"approx. 13 %","yr":2025,"s":"https://www.businessresearchinsights.com/market-reports/residential-portable-dehumidifier-market-104994","note":"unit shipments"},
 {"mkt":"Global residential portable dehumidifiers","who":"Top five manufacturers together","share":"approx. 54 %","yr":2025,"s":"https://www.businessresearchinsights.com/market-reports/residential-portable-dehumidifier-market-104994","note":"unit shipments"}],
 "For portable dehumidifiers one vendor report puts Midea first with about 15 per cent of world unit shipments and Haier second with about 13 per cent."),
}
for dep in d['depts']:
    if dep['n'] in ms: dep['ms'],dep['msum']=ms[dep['n']]
for fn,o in(('B7.json',d),('B7_brands.json',br)):
    json.dump(o,open(R+fn+'.tmp','w'),ensure_ascii=False,indent=1); os.rename(R+fn+'.tmp',R+fn)
if not os.path.exists(R+'B7_renames.json'): open(R+'B7_renames.json','w').write('{}\n')
