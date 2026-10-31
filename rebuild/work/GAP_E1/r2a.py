import json,os
P='rebuild/out/E1.json'
d=json.load(open(P))
norm={'USA':'United States','UK':'United Kingdom','Korea':'South Korea','Czechoslovakia':'Czechoslovakia','France/Switzerland':None}
skipg={'Country not stated','Other makers','Founding lines',None}
n=0
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            if k['n'] in('Scale model kit','Die-cast model'):
                for e in k['x']:
                    g=e.get('g')
                    if g in skipg or e.get('cty'): continue
                    c=norm.get(g,g)
                    if c: e['cty']=c; n+=1
            if k['n']=='Toy soldier & animal figure':
                k.pop('xg',None)
                for e in k['x']: e.pop('g',None)
print(n)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
# queue
q=[]
seen=set()
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x') or []:
                kind=k['n']
                big=kind in('Scale model kit','Die-cast model','Toy soldier & animal figure')
                noown=e.get('own') in(None,'','owner not stated')
                if big:
                    p=1 if not e.get('cty') else 3
                    if p==3 and not noown: continue
                    if kind=='Toy soldier & animal figure' and e['n'] in('Britains hollow-cast soldiers','Schleich figures'): continue
                elif noown or not e.get('cty'):
                    p=2
                else: continue
                t=e['n'] if big else (e.get('mk') or e['n'])
                q.append((p,kind,e['n'],t))
q.sort(key=lambda x:x[0])
json.dump(q,open('rebuild/work/GAP_E1/queue.json','w'),ensure_ascii=False)
import collections
print(collections.Counter(x[0] for x in q))
