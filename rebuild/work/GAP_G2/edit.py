import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'G2.json'))
W='https://en.wikipedia.org/wiki/'
info={ # name:(own,tier,cty,own_y)
'Ritz-Carlton Residences':('Marriott International','Global group','United States',1998),
'Mandarin Oriental Residences':('Jardine Matheson','Independent','Hong Kong',None),
'Fairmont Residences':('Accor','Global group','Canada',2016),
'St Regis Residences':('Marriott International','Global group','United States',2016),
'Kempinski Residences':('Kempinski AG','Independent','Germany',None),
'Banyan Tree Residences':('Banyan Group','Independent','Singapore',None),
'Marriott International residences':('Marriott International','Global group','United States',None),
'Accor residences':('Accor','Global group','France',None),
'Hilton residences':('Hilton','Global group','United States',None),
'Banyan Group residences':('Banyan Group','Independent','Singapore',None),
'Missoni residences':('Missoni family and Fondo Strategico Italiano','Independent','Italy',None),
'Aston Martin residences':('Aston Martin Lagonda Global Holdings PLC','Independent','United Kingdom',None),
'Pininfarina residences':('Mahindra Group','Independent','Italy',2015),
'Armani residences':(None,None,'Italy',None),
'Elie Saab residences':(None,None,'Lebanon',None),
}
yrs={'Ritz-Carlton Residences':None}
k=d['depts'][1]['s'][1]['k'][0]
for e in k['x']:
    i=info.get(e['n'])
    if not i: continue
    own,t,c,oy=i
    if own: e['own']=own
    if t: e['tier']=t
    if c: e['cty']=c
    if oy: e['own_y']=oy
k['sel']=k['sel']+" Covers 20 of an unknown total: the article lists no whole-space register (Knight Frank counts 903 schemes worldwide), so brands named on no fetched page are left out. Trump International has no fetched owner; Tonino Lamborghini page returned 404."
# Houses market
h=d['depts'][0]
S='https://projectscot.com/2024/07/barratt-delivers-strong-operational-performance-despite-sector-challenges'
h['ms']+= [
 {"mkt":"UK housebuilding","who":"Barratt Developments","share":"14,004 homes completed","yr":2024,"s":S,"note":"year to 30 June 2024, including 536 from joint ventures; completions, not a share"},
 {"mkt":"UK housebuilding","who":"Vistry","share":"17,225 homes completed","yr":2024,"s":W+"Vistry_Group","note":"total completions, up 7 % on 2023; completions, not a share"},
 {"mkt":"UK housebuilding","who":"Taylor Wimpey","share":"10,593 homes completed","yr":2024,"s":"https://www.investegate.co.uk/announcement/rns/taylor-wimpey--tw./taylor-wimpey-plc-full-year-results/9459165","note":"group completions including joint ventures (9,972 UK homes excluding them), as the 2025 results state; completions, not a share"},
]
h['msum']+=" 2024 completions: Vistry 17,225, Barratt 14,004 (year to June), Taylor Wimpey 10,593 and Persimmon 10,664; these are counts, not shares, and the reporting years differ."
json.dump(d,open(P+'G2.json.tmp','w'),indent=1,ensure_ascii=False); os.replace(P+'G2.json.tmp',P+'G2.json')
b=json.load(open(P+'G2_brands.json'))
f={'Ritz-Carlton':('United States','1983'),'Mandarin Oriental':('Hong Kong','1963'),'Fairmont':('Canada','1886'),'St Regis':('United States','1998'),'Kempinski':('Germany','1862'),'Banyan Tree':('Singapore','1994'),'Banyan Group':('Singapore','1994'),'Marriott International':('United States','1993'),'Accor':('France','1967'),'Hilton':('United States','1919'),'Armani':('Italy','1975'),'Missoni':('Italy','1953'),'Elie Saab':('Lebanon','1982'),'Aston Martin':('United Kingdom','1913'),'Pininfarina':('Italy','1930')}
for x in b['b']:
    if x['n'] in f:
        x['c'],x['f']=f[x['n']]
json.dump(b,open(P+'G2_brands.json.tmp','w'),indent=1,ensure_ascii=False); os.replace(P+'G2_brands.json.tmp',P+'G2_brands.json')
