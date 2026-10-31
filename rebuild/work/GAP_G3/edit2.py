import json,os
p='rebuild/out/G3.json'
d=json.load(open(p))
b=d['depts'][1]
u='https://www.reportprime.com/sanitary-ware-r18528/company'
for who,sh,rev in [('Kohler Co.','12.7 %','US$ 7.1 billion'),('TOTO Ltd.','11.6 %','US$ 6.5 billion'),('LIXIL Corporation','9.3 %','US$ 5.2 billion'),('Geberit AG','7.5 %','US$ 4.2 billion'),('Roca Sanitario SA','6.8 %','US$ 3.8 billion')]:
    b['ms'].append({"mkt":"Global sanitaryware","who":who,"share":sh,"yr":2024,"s":u,"note":"market share as the Report Prime table states, 2024 revenue "+rev+"; other publishers give lower combined shares, so treat the ranking as indicative"})
b['msum']=b['msum']+' One publisher ranks Kohler (12.7 %), TOTO (11.6 %) and LIXIL (9.3 %) first for 2024.'
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            if k['n']=='Staircase':
                k['x']=[{"n":"Cantilevered (floating) stair","a":"floating stair","d":"Stair whose treads are anchored at one end only, so they appear to float; used by Inigo Jones and Nicholas Stone in the Tulip Staircase and later by Robert Adam.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Cantilevered_stairs","v":[]}]
                k['nl']="One entry is a named historic originator or period type of this kind, each traceable to its own cited page; current makers are in the brand register."
                k['sel']="No whole-space reference exists for this kind; entries are the traceable types named by the cited page. No complete list exists; follows the Wikipedia article on cantilevered stairs (en.wikipedia.org)."
open(p+'.tmp','w').write(json.dumps(d,ensure_ascii=False,indent=1)); os.rename(p+'.tmp',p)
