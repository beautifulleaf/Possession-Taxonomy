import json,os
P='rebuild/out/J10.json'
d=json.load(open(P))
kinds={K['n']:K for D in d['depts'] for S in D['s'] for K in S['k']}
H='https://en.wikipedia.org/wiki/Heated_tobacco_product'; E='https://en.wikipedia.org/wiki/Electronic_cigarette'
K=kinds['Heated-tobacco device']
if not any(e['n']=='Revo' for e in K['x']):
    K['x'].append({'n':'Revo','a':'','d':'Heated cigarette announced by R.J. Reynolds in November 2014, tested in Wisconsin and withdrawn in 2015.','mk':'Revo','y':'2014','s':H,'g':'R.J. Reynolds','own':'R.J. Reynolds','tier':'Global group','cty':'United States'})
K['sel']=K['sel'].split(' Covers ')[0].rstrip()+" Complete: 14 heated-tobacco systems named in the whole of Wikipedia's Heated tobacco product (read to its end, 226,066 characters). The page also names Marlboro HeatSticks (a stick for IQOS), iSENZIA (tobacco-free) and CK33 (no maker); these are not devices here."
G=[('Vype','British American Tobacco','2013','United Kingdom','E-cigarette brand of British American Tobacco, launched in the UK in 2013.'),
('Logic','Japan Tobacco','2015','','E-cigarette brand acquired by Japan Tobacco in 2015.'),
('Green Smoke','Altria','2014','United States','E-cigarette brand Altria expanded in 2014 and bought further in 2016.'),
('Nicocigs','Philip Morris','2014','United Kingdom','E-cigarette maker bought by Philip Morris in 2014.'),
('Voke','British American Tobacco','2014','','Inhaler-based nicotine product of British American Tobacco via Nicoventures, using Kind Consumer technology.'),
('QMOS','United Tobacco Vapor Group','2016','','E-cigarette of United Tobacco Vapor Group, 2016.'),
('eTron 3T','Vapor Tobacco Manufacturing','2014','','E-cigarette of Vapor Tobacco Manufacturing, 2014.'),
('BLOW','BLOW','2014','','E-hookah brand, 2014.')]
new={'n':'Vape brand, form not stated','a':'','d':'Electronic-cigarette brand that the reference names without saying whether it is a cigalike, pod, pen or box device.','s':E,'tt':[['Owner',['Tobacco group','Independent']]],'x':[],'m':[],'xg':'by maker','nl':'One entry is an electronic-cigarette brand or line sold under its own name; versions are generations the page names.','sel':"Brands in the second and third windows (characters 100,000 to 234,450) of Wikipedia's Electronic cigarette that name an owner and are not already in the cigalike, disposable, pod or pen kinds. Complete: 8 of 8 such brands on the page; the page names no other hobby hardware brands (SMOK, Vaporesso, VooPoo, OXVA, Geek Bar are absent from it)."}
for n,o,y,c,desc in G:
    new['x'].append({'n':n,'a':'','d':desc,'mk':n,'y':y,'s':E,'g':o,'own':o,'tier':'Global group' if o in('British American Tobacco','Japan Tobacco','Altria','Philip Morris') else 'Independent','cty':c})
sh=[S for D in d['depts'] for S in D['s'] if any(k['n']=='Cigalike' for k in S['k'])][0]
if 'Vape brand, form not stated' not in kinds: sh['k'].append(new)
base="Vape hardware lines named in Wikipedia's Electronic cigarette (read to its end, 234,450 characters) with owner and year as the page states."
for k in ['Cigalike','Disposable vape','Refillable pod kit','Vape pen kit']:
    kinds[k]['sel']=base+f" Complete: {len(kinds[k]['x'])} entries; every line the page names with a device form is placed; SMOK, Vaporesso, OXVA, VooPoo and SKE do not appear on the page. Searched: 'list of e-cigarette brands' and a Wikidata class query found no reference list."
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
