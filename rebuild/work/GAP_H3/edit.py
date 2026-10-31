import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
load=lambda p: json.load(open(R+p))
def save(p,o):
    t=R+p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,R+p)
d=load('out/H3.json'); br=load('out/H3_brands.json'); B={x['n']:x for x in br['b']}
wd=lambda q:'https://www.wikidata.org/wiki/'+q
for n,q,c,f in [('Fun Factory','Q510318','Germany','1996'),('Ann Summers','Q579524','United Kingdom','1972'),('TENGA','Q861358','Japan','2005'),('Lovehoney','Q6692094','United Kingdom','2002'),('LELO','Q13911700','Sweden','2003'),('Kiiroo','Q111497682','Netherlands',None),('Womanizer','Q116169861','Germany',None),('Maude','Q121189863','United States',None)]:
    x=B[n]
    if c and not x.get('c'): x['c']=c
    if f and not x.get('f'): x['f']=f
    if not x.get('s'): x['s']=wd(q)
D=d['depts'][0]
D['ms']=[{"mkt":"Sex toys, worldwide","who":"Lovehoney Group","share":"over 30 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/sex-toys-market","note":"market share as the page states it; top five (Lovehoney, LELO, Doc Johnson, We-Vibe, Tenga) 70 %; vendor estimate, method not stated"}]
D['msum']="Lovehoney Group leads sex toys worldwide on one market-research estimate; the top five hold 70 %."
save('out/H3.json',d); save('out/H3_brands.json',br)
