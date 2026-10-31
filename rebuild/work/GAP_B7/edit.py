import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
load=lambda p: json.load(open(R+p))
def save(p,o):
    t=R+p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,R+p)
d=load('out/B7.json'); br=load('out/B7_brands.json'); B={x['n']:x for x in br['b']}
wd=lambda q:'https://www.wikidata.org/wiki/'+q
for n,q,c,f in [('Bresser','Q1915423','Germany','1957'),('Candy','Q2454999','Italy','1927'),('Russell Hobbs','Q3051064','United Kingdom','1952'),('Vortice Elettrosociali','Q4016476','Italy','1954'),('Davis Instruments','Q133269413','United States',None),('Momcozy','Q139790798',None,'2018')]:
    x=B[n]
    if c:x['c']=c
    if f:x['f']=f
    if not x.get('s'): x['s']=wd(q)
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if k.get('x'):
                if k['n']=='Electric fan (design & vintage)':
                    k['sel']=k['sel'].rstrip()+" No complete list exists; follows the maker histories and design-collection pages named here."
                else:
                    k['sel']=k['sel'].rstrip()+" No complete list exists; follows the design-collection and award pages named here."
H,F,Hu=d['depts'][0],d['depts'][2],d['depts'][4]
H['ms']=[{"mkt":"Space heaters, worldwide","who":"Honeywell International","share":"over 8.5 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/space-heater-market","note":"market share as the page states it; top five together 35 %"}]
H['msum']="Honeywell leads space heaters worldwide on one market-research estimate, with the top five holding 35 %."
Hu['ms']+=[{"mkt":"Humidifiers, worldwide","who":"Honeywell, Dyson, Boneco","share":"45 %","yr":2025,"s":"https://www.futuremarketinsights.com/reports/humidifier-market-share-analysis","note":"combined share of the top tier; second tier Vicks, Levoit, Crane 25 %; no per-company figures"}]
save('out/B7.json',d); save('out/B7_brands.json',br)
