import json,os
P='rebuild/out/B1.json'; PB='rebuild/out/B1_brands.json'
d=json.load(open(P)); bd=json.load(open(PB))
O={ # mk: (own, tier, cty, own_y, founded)
'Vitra':('Vitra (Swiss family-owned)','Independent','Switzerland','','1950'),
'Steelcase':('HNI Corporation','Independent','United States','2025','1912'),
'La-Z-Boy':('La-Z-Boy Incorporated','Independent','United States','','1927'),
'Kartell':('Felofin','Independent','Italy','','1949'),
'Emeco':('Gregg Buchbinder','Independent','United States','1998','1944'),
'Artifort':('Lande Group','Independent','Netherlands','1998','1890'),
'Secretlab':('Ian Ang, Alaric Choo and Heliconia Capital Management','Independent','Singapore','','2014'),
'Isokon':('Isokon (licensed from the Pritchard family)','Independent','United Kingdom','','1929'),
'Gufram':('Italian Radical Design Group','Independent','Italy','2012','1966'),
'Memphis':('Italian Radical Design Group','Independent','Italy','','1980'),
}
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
    if b is None: continue
    b['own']=o[0]; b['tier']=o[1]
    if not b.get('c'): b['c']=o[2]
    if not b.get('f'): b['f']=o[4]
for nm,c,f,dd in [('HNI Corporation','United States','','Bought Steelcase in a deal announced in 2025 and closed December 2025.'),('Felofin','Italy','','Owner of Kartell.'),('Lande Group','Netherlands','','Owner of Artifort since 1998.'),('Italian Radical Design Group','Italy','','Vazza family group that owns Gufram and Memphis.')]:
    if nm not in bs: bd['b'].append({'n':nm,'c':c,'seg':'Mainstream','d':dd,'s':'https://en.wikipedia.org/wiki/Gufram' if 'Radical' in nm else '','kf':'furniture'})
for p,o in ((P,d),(PB,bd)):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(n)
