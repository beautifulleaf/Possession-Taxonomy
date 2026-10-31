import json,sys,os
# usage: apply.py JOB spec.json
job,spec=sys.argv[1],json.load(open(sys.argv[2]))
p=f'work/J10/shelves/{job}.json'
d=json.load(open(p))
kinds={k['n']:k for k in d['kinds']}
for kn,xs in spec.get('x',{}).items():
    k=kinds[kn]; have={x['n'].lower() for x in k.setdefault('x',[])}
    for x in xs:
        if x['n'].lower() in have: print('skip dup',x['n']); continue
        x.setdefault('a','');x.setdefault('y','');k['x'].append(x)
for kn,ms in spec.get('m',{}).items():
    k=kinds[kn]; k.setdefault('m',[])
    for m in ms:
        if m not in k['m']: k['m'].append(m)
for kn,n in spec.get('trim',{}).items():
    kinds[kn]['m']=kinds[kn]['m'][:len(kinds[kn]['m'])-n] if n else kinds[kn]['m']
have={b['n'].lower() for b in d['brands']}
for b in spec.get('brands',[]):
    if b['n'].lower() in have: print('skip dup brand',b['n']); continue
    d['brands'].append(b)
if spec.get('note'): d['notes']=(d['notes']+' | Deepening: '+spec['note']).strip()
tmp=p+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,p)
