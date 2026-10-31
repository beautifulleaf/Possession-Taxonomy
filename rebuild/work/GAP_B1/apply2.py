import json,os
P='rebuild/out/B1.json'; PB='rebuild/out/B1_brands.json'
d=json.load(open(P)); bd=json.load(open(PB))
U='https://scandinaviandesign.com/companies/muuto/'
R=[('Dining chair','Fiber chair','Iskos-Berlin','2014'),('Sofa','Oslo sofa','Anderssen & Voll','2013'),
('Sectional sofa','Connect Soft','Anderssen & Voll',''),('Sectional sofa','In Situ modular sofa','Anderssen & Voll',''),
('Upholstered lounge chair','Doze lounge chair','Anderssen & Voll',''),('Upholstered lounge chair','Rest lounge chair','Anderssen & Voll',''),
('Dining table','70/70 table','TAF Studio',''),('Dining table','Workshop table','Cecilie Manz',''),('Bench','Workshop bench','Cecilie Manz',''),
('Coffee table','Workshop coffee table','Cecilie Manz',''),('Coffee table','Around coffee table','Thomas Bentzen',''),
('Dining chair','Cover side chair','Thomas Bentzen',''),('Side table','Soft side table','Jens Fager',''),('Rolling cart','Flow trolley','Normal Studio','')]
kinds={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: kinds[k['n']]=k
have={e['n'].lower() for k in kinds.values() for e in k.get('x',[])}
for kn,n,des,y in R:
    if n.lower() in have: print('dup',n); continue
    k=kinds[kn]
    e={"n":n.capitalize() if n[0].isalpha() else n,"a":"","d":f"Muuto piece designed by {des}"+(f", {y}." if y else "."),"mk":"Muuto","y":y,"s":U,"v":[],"own":"MillerKnoll","tier":"Global group","cty":"Denmark","own_y":"2018","g":(y[:3]+'0s') if y else 'Undated'}
    e['n']=n[0].upper()+n[1:]
    k['x'].append(e)
    xs=k['x']; k['x']=sorted(xs,key=lambda e:(e.get('g')=='Undated',0)) if all(x.get('g') for x in xs) else xs
for x in bd['b']:
    if x['n']=='Muuto': x.update(own='MillerKnoll',tier='Global group',sig=['Fiber chair','Oslo sofa','Connect Soft','70/70 table'])
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
json.dump(bd,open(PB+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(PB+'.tmp',PB)
