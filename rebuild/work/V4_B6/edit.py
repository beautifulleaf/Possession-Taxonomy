import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/B6.json'))
reg=json.load(open(R+'out/B6_brands.json'))
names={b['n'] for b in reg['b']}
need=set(); removed={'m':0,'r':0,'x':0}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for f in ('m','r'):
                for m in k.pop(f,[]): need.add(m[1]); removed[f]+=1
            for x in k.pop('x',[]):
                removed['x']+=1; need.add(x.get('mk'))
                for v in x.get('v',[]): need.add(v.get('mk'))
            k.pop('xg',None)
need.discard(None); need.discard('')
G='https://www.gminsights.com/industry-analysis/'
dep={x['n']:x for x in d['depts']}
dep['Vacuums & floor machines']['ms']=[
 {"mkt":"Household vacuum cleaners, worldwide","who":"Dyson Ltd","share":"over 15 %","yr":2025,"s":G+"household-vacuum-cleaners-market","note":"market share as the page states it"},
 {"mkt":"Household vacuum cleaners, worldwide","who":"Dyson, Ecovacs, SharkNinja, Roborock and Dreame Technology together","share":"54.5 %","yr":2025,"s":G+"household-vacuum-cleaners-market","note":"combined share of the five largest"},
 {"mkt":"Robot vacuum cleaners, worldwide","who":"Beijing Roborock Technology","share":"17.0 %","yr":2025,"s":G+"robotic-vacuum-cleaner-market","note":"estimated share"},
 {"mkt":"Robot vacuum cleaners, worldwide","who":"Ecovacs","share":"11.5 %","yr":2025,"s":G+"robotic-vacuum-cleaner-market","note":"estimated share"},
 {"mkt":"Robot vacuum cleaners, worldwide","who":"SharkNinja","share":"10.5 %","yr":2025,"s":G+"robotic-vacuum-cleaner-market","note":"estimated share"},
 {"mkt":"Robot vacuum cleaners, worldwide","who":"Dreame Technology","share":"7.5 %","yr":2025,"s":G+"robotic-vacuum-cleaner-market","note":"estimated share"},
 {"mkt":"Smart vacuums, worldwide, first quarter","who":"Roborock","share":"19.3 %","yr":2025,"s":"https://my.idc.com/getdoc.jsp?containerId=prUS53637025","note":"units shipped, IDC; rank 1"},
 {"mkt":"Smart vacuums, worldwide, first quarter","who":"Ecovacs","share":"13.6 %","yr":2025,"s":"https://my.idc.com/getdoc.jsp?containerId=prUS53637025","note":"units shipped, IDC; rank 2"},
 {"mkt":"Smart vacuums, worldwide, first quarter","who":"Dreame","share":"11.3 %","yr":2025,"s":"https://my.idc.com/getdoc.jsp?containerId=prUS53637025","note":"units shipped, IDC; rank 3"},
 {"mkt":"Smart vacuums, worldwide, first quarter","who":"Xiaomi","share":"9.9 %","yr":2025,"s":"https://my.idc.com/getdoc.jsp?containerId=prUS53637025","note":"units shipped, IDC; rank 4"},
 {"mkt":"Smart vacuums, worldwide, first quarter","who":"iRobot","share":"9.3 %","yr":2025,"s":"https://my.idc.com/getdoc.jsp?containerId=prUS53637025","note":"units shipped, IDC; rank 5"}]
dep['Vacuums & floor machines']['msum']="Dyson leads household vacuums overall; for robot vacuums Roborock leads on both a market-research estimate and IDC unit shipments, ahead of Ecovacs."
dep['Washing machines & dryers']['ms']=[
 {"mkt":"Washing machines, worldwide","who":"Haier","share":"16.6 %","yr":2025,"s":G+"washing-machine-market","note":"market leader as the page states it"},
 {"mkt":"Washing machines, worldwide","who":"Haier, Samsung, Whirlpool, LG and Midea together","share":"38.1 %","yr":2025,"s":G+"washing-machine-market","note":"combined share of the five largest; the page also gives 38.2 %"}]
dep['Washing machines & dryers']['msum']="Haier is the largest washing-machine maker, and the five largest makers hold about 38 % of the world market."
dep['Laundry products']['ms']=[
 {"mkt":"Laundry care, worldwide","who":"Procter & Gamble","share":"35.1 %","yr":2025,"s":G+"laundry-care-products-market","note":"share of the market as the page states it"},
 {"mkt":"Laundry care, worldwide","who":"Unilever","share":"15.0 %","yr":2025,"s":G+"laundry-care-products-market","note":"share of the market as the page states it"},
 {"mkt":"Laundry care, worldwide","who":"Henkel","share":"7.5 %","yr":2025,"s":G+"laundry-care-products-market","note":"share of the market as the page states it"}]
dep['Laundry products']['msum']="Procter & Gamble holds more than a third of world laundry care, followed by Unilever and Henkel."
info={"Procter & Gamble":("United States","1837","https://en.wikipedia.org/wiki/Procter_%26_Gamble"),
"Unilever":("United Kingdom","1930","https://en.wikipedia.org/wiki/Unilever"),
"Reckitt":("United Kingdom","1999","https://en.wikipedia.org/wiki/Reckitt"),
"Church & Dwight":("United States","1847","https://en.wikipedia.org/wiki/Church_%26_Dwight"),
"3M":("United States","1902","https://en.wikipedia.org/wiki/3M")}
need.add('Henkel')
for n in sorted(need-names):
    c,f,s=info.get(n,("","",""))
    reg['b'].append({"n":n,"c":c,"f":f,"seg":"Mainstream","d":"Maker or brand named in the cleaning and laundry kinds; country and founding year not yet sourced." if not c else "Company that makes cleaning, laundry or household products.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s,"kf":"household goods"})
def w(p,o):
    t=p+'.tmp'; json.dump(o,open(t,'w'),indent=1,ensure_ascii=False); os.rename(t,p)
w(R+'out/B6.json',d); w(R+'out/B6_brands.json',reg)
print(removed,len(need-names))
