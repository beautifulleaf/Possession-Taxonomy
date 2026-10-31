import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'A5.json')); br=json.load(open(P+'A5_brands.json'))
O={'Lorier':('Worn & Wound','Craft & indie','2026'),'Chanel':('Wertheimer family','Independent','')}
def f(o):
    mk=o.get('mk') or o.get('n')
    if mk in O and 'not stated' in o.get('own','not stated'):
        a,b,c=O[mk]; o['own']=a; o['tier']=b
        if c:o['own_y']=c
for dep in d['depts']:
    for sh in dep['s']:
        for k in sh['k']:
            for e in k.get('x',[]): f(e)
for b in br['b']: f(b)
json.dump(d,open(P+'A5.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'A5.json.tmp',P+'A5.json')
json.dump(br,open(P+'A5_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'A5_brands.json.tmp',P+'A5_brands.json')
