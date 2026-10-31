import json,os
P='rebuild/out/B1.json'; PB='rebuild/out/B1_brands.json'
d=json.load(open(P)); bd=json.load(open(PB))
O={'GUBI':('GUBI A/S (Chr. Augustinus Fabrikker holds 24%)','Independent','Denmark','2018','1967'),
'Fredericia':('Fredericia Furniture A/S (Graversen family)','Independent','Denmark','','1911'),
'Erik Jørgensen':('Fredericia Furniture A/S','Independent','Denmark','2020',''),
'Graco':('Newell Brands','Global group','United States','1999','1942'),
'Arflex':('owner not stated','Independent','Italy','','1948'),
'Vitsœ':('owner not stated','Independent','United Kingdom','','1959')}
bs={x['n']:x for x in bd['b']}
n=0
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x',[]):
                m=e.get('mk')
                if m in O and (not e.get('own') or not e.get('tier')):
                    o=O[m]; e['own']=o[0]; e['tier']=o[1]; e['cty']=o[2]
                    if o[3]: e['own_y']=o[3]
                    n+=1
for m,o in O.items():
    b=bs.get(m)
    if b:
        b['own']=o[0]; b['tier']=o[1]
        if not b.get('c'): b['c']=o[2]
        if not b.get('f') and o[4]: b['f']=o[4]
for nm,c in [('Newell Brands','United States'),('Fredericia Furniture A/S','Denmark')]:
    if nm not in bs: bd['b'].append({'n':nm,'c':c,'seg':'Mainstream','d':'Owner named on a fetched page for a brand in this category.','s':'','kf':'furniture'})
for p,o in ((P,d),(PB,bd)):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(n)
