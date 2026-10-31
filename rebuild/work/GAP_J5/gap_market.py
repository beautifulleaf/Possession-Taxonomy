import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
j=json.load(open(R+'out/J5.json')); b=json.load(open(R+'out/J5_brands.json'))
upd={"Campbell's condensed soup":dict(own="The Campbell's Company",cty="United States",s_extra="https://en.wikipedia.org/wiki/Campbell_Soup_Company"),
"Nutella":dict(own="Ferrero International SpA",cty="Italy",own_y=None),
"Vegemite":dict(own="Bega Group",cty="Australia",own_y="2017",tier="National champion"),
}
for dp in j['depts']:
    for s in dp['s']:
        for k in s['k']:
            for e in k.get('x',[]):
                if e['n'] in upd:
                    u=upd[e['n']]
                    for a,v in u.items():
                        if a in('s_extra',) or v is None: continue
                        e[a]=v
                    if e['n']=='Nutella': e['y']=e.get('y') or '1964'
                if e['n']=='Dolmio sauce' or e['n']=='Dolmio':
                    e.update(own="Mars, Incorporated",cty="Australia",tier="Global group")
    if dp['n']=='Sauces & condiments':
        dp['ms']=(dp.get('ms') or [])+[
         {"mkt":"US ketchup","who":"Heinz (Kraft Heinz)","share":"61 %","yr":2013,"s":"https://www.sec.gov/Archives/edgar/data/0000046640/000119312514187628/d678101d424b3.htm","note":"value share, Nielsen 52-week data through late 2013, as stated in the Heinz prospectus"},
         {"mkt":"Global ketchup","who":"Heinz (Kraft Heinz)","share":"25 %","yr":2013,"s":"https://www.sec.gov/Archives/edgar/data/0000046640/000119312514187628/d678101d424b3.htm","note":"global market share stated in the Heinz prospectus"}]
have={x['n'] for x in b['b']}
for n,c,d,s in [("Ferrero","Italy","Italian maker of Nutella; owner of Nutella (Ferrero International SpA).","https://en.wikipedia.org/wiki/Nutella"),
 ("Bega Group","Australia","Australian owner of Vegemite since January 2017, bought from Mondelez International.","https://en.wikipedia.org/wiki/Vegemite"),
 ("Mars, Incorporated","United States","Owner of Dolmio, launched 1985 as Alora in Australia and renamed Dolmio in 1989.","https://en.wikipedia.org/wiki/Dolmio"),
 ("The Campbell's Company","United States","Renamed from Campbell Soup Company in November 2024; owns Pepperidge Farm (1961) and Pace (1995).","https://en.wikipedia.org/wiki/Campbell_Soup_Company")]:
    if n not in have: b['b'].append({"n":n,"c":c,"seg":"Mainstream","kf":"","d":d,"s":s})
json.dump(j,open(R+'work/GAP_J5/t.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/GAP_J5/t.json',R+'out/J5.json')
json.dump(b,open(R+'work/GAP_J5/t2.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/GAP_J5/t2.json',R+'out/J5_brands.json')
