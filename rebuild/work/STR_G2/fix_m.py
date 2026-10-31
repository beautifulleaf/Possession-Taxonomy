import json, os
R='/home/user/Possession-Taxonomy/rebuild/'
b=json.load(open(R+'work/STR_G2/bak/G2.json'))
d=json.load(open(R+'out/G2.json'))
dem={'Castle & tower house':['Fortified house'],'Palazzo':['Piano nobile apartment'],'Chalet':['Alpine chalet'],
'Multi-unit residential building':['Tenement block'],'Fractional & timeshare':['Points-based vacation club','Fractional apartment share'],
'Private island':['Caribbean resort cay','Aegean private island','Whole populated island'],'Sporting estate':['Highland sporting estate'],
'Equestrian property':['Kentucky bluegrass stud farm'],'Vineyard & wine estate':['Bordeaux first-growth château estate','Tuscan coastal tenuta'],
'Ranch & station':['Texas cattle ranch','Outback cattle station'],'Airpark home & private airstrip':['Residential fly-in airpark'],
'Oast house':['Converted oast'],'Bunker':['Home fallout shelter','Missile silo conversion'],
'Beach hut':['Bournemouth beach hut','Mudeford Spit hut','Brighton bathing box']}
B={k['n']:k for p in b['depts'] for s in p['s'] for k in s['k']}
D={k['n']:k for p in d['depts'] for s in p['s'] for k in s['k']}
added=0
for kn,names in dem.items():
    for a in B[kn]['x']:
        if a['n'] in names:
            ms=D[kn].setdefault('m',[])
            ents=[[v['n'],v.get('mk') or a.get('mk') or ''] for v in a.get('v',[])] or [[a['n'],a.get('mk','')]]
            for e in ents:
                if e not in ms: ms.append(e); added+=1
print('added',added)
json.dump(d,open(R+'work/STR_G2/G2.fix.json','w'),ensure_ascii=False,indent=1)
os.replace(R+'work/STR_G2/G2.fix.json',R+'out/G2.json')
