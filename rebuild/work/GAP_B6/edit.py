import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
def load(p): return json.load(open(R+p))
def save(p,o):
    t=R+p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,R+p)
d=load('out/B6.json'); br=load('out/B6_brands.json')
B={x['n']:x for x in br['b']}
def setb(n,c=None,f=None,s=None):
    x=B[n]
    if c: x['c']=c
    if f: x['f']=f
    if s and not x.get('s'): x['s']=s
wd=lambda q:'https://www.wikidata.org/wiki/'+q
for n,q,c,f in [('Aldi','Q125054','Germany','1946'),('AEG','Q158276','Germany','1883'),('Kenmore','Q588640','United States',None),('Downy','Q903922','United States','1960'),('Febreze','Q910264','United States','1996'),('OxiClean','Q7115618','United States','1997'),('Swiffer','Q3506571',None,'1999'),('Pledge','Q7204423',None,'1956'),('O-Cedar','Q7072004','United States',None),('Magic Chef','Q6730659','United States',None),('OXO','Q7073184','United States','1990'),('Ewbank','Q21716360','United Kingdom',None),('Arm & Hammer','Q4792455','United States',None)]:
    setb(n,c,f,wd(q))
setb('Henkel','Germany','1876','https://en.wikipedia.org/wiki/Henkel')
B['Henkel']['d']="German company, founded in Aachen in 1876 as Henkel & Cie; makes Persil, Pril, Somat and other laundry and cleaning brands."
sel=" No complete list exists; follows the design-collection and award pages named here."
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if k.get('x') and not k['sel'].rstrip().endswith('exists; follows the design-collection and award pages named here.'):
                k['sel']=k['sel'].rstrip()+sel
V,C,W=d['depts'][0],d['depts'][2],d['depts'][3]
V['ms']+= [
 {"mkt":"Vacuum cleaners, Germany (retail volume)","who":"Dyson GmbH","share":"18 %","yr":2025,"s":"https://www.euromonitor.com/vacuum-cleaners-in-germany/report","note":"retail volume share, as the page states it"},
 {"mkt":"Vacuum cleaners, Germany (retail volume)","who":"Miele & Cie KG","share":"9 %","yr":2025,"s":"https://www.euromonitor.com/vacuum-cleaners-in-germany/report","note":"retail volume share; top two together 27 %"}]
C['ms']=[
 {"mkt":"Household cleaning products, worldwide","who":"The Procter & Gamble Company","share":"12.1 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/household-cleaning-products-market","note":"market share as the page states it"},
 {"mkt":"Household cleaning products, worldwide","who":"Unilever PLC","share":"5.6 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/household-cleaning-products-market","note":"market share as the page states it; the page gives two different top-five totals (32.6 % and 26.1 %)"}]
C['msum']="Procter & Gamble leads household cleaning products worldwide on one market-research estimate, ahead of Unilever; no dishwashing-only figures were found."
W['ms']+=[{"mkt":"Tumble dryers, Europe","who":"BSH Hausgeräte, Miele, Electrolux, Beko, Haier Europe","share":"combined below 50 %","yr":2025,"s":"https://www.mordorintelligence.com/industry-reports/europe-tumble-dryers-market","note":"named by the page as the listed leaders; no brand shares given"}]
save('out/B6.json',d); save('out/B6_brands.json',br)
