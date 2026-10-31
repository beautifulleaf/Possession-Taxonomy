import json,os
P='rebuild/out/E1.json'
d=json.load(open(P))
F={'Kyosho Optima':dict(own='Kyosho',cty='Japan'),'Kyosho Inferno':dict(own='Kyosho',cty='Japan'),
'Traxxas Maxx':dict(own='Mike Jenkins',cty='United States'),'Traxxas Slash':dict(own='Mike Jenkins',cty='United States'),'Traxxas TRX-4':dict(own='Mike Jenkins',cty='United States'),
'McFarlane Toys figures':dict(own='Todd McFarlane Productions, Inc.',cty='United States'),
'Action Man':dict(own='Hasbro',cty='United Kingdom',y='1966',tier='Global group'),
'Marvel Legends':dict(cty='United States',y='2002'),
'Hot Toys Movie Masterpiece Series':dict(own='Hot Toys',cty='Hong Kong'),
'Toniebox and Tonies':dict(own='Tonies SE',cty='Luxembourg',y='2016')}
c=0
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x') or []:
                f=F.get(e['n'])
                if not f: continue
                c+=1
                for a,b in f.items():
                    if a=='own':
                        if e.get('own') in(None,'','owner not stated'): e['own']=b; e.setdefault('tier','Independent')
                    elif a=='tier': e['tier']=b
                    elif not e.get(a): e[a]=b
print(c)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
