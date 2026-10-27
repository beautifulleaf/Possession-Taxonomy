"""usage: add.py JOB spec.json  ; spec = {"m":{kind:[[model,maker],..]}, "x":{kind:[archetype,..]}, "brands":[..], "notes":"text appended"}"""
import json,sys,os
job,spec=sys.argv[1],json.load(open(sys.argv[2]))
p=f'work/J6/shelves/{job}.json'; d=json.load(open(p))
import shutil; os.makedirs('work/J6/agent/deep/bak',exist_ok=True)
b=f'work/J6/agent/deep/bak/{job}.json'
if not os.path.exists(b): shutil.copy(p,b)
kb={k['n']:k for k in d['kinds']}
cnt={'m':0,'x':0,'b':0}
for kn,ms in spec.get('m',{}).items():
    k=kb[kn]; k.setdefault('m',[]); have={tuple(t) for t in k['m']}
    for t in ms:
        if tuple(t) not in have: k['m'].append(t); have.add(tuple(t)); cnt['m']+=1
for kn,xs in spec.get('x',{}).items():
    k=kb[kn]; k.setdefault('x',[]); have={x['n'].lower() for x in k['x']}
    for x in xs:
        if x['n'].lower() not in have:
            x.setdefault('a',''); x.setdefault('mk',''); x.setdefault('y',''); x.setdefault('v',[]); x.setdefault('dt','')
            k['x'].append(x); have.add(x['n'].lower()); cnt['x']+=1
for kn,am in spec.get('v',{}).items():
    k=kb[kn]
    for an,vs in am.items():
        a=[x for x in k['x'] if x['n']==an][0]; have={v['n'].lower() for v in a['v']}
        for v in vs:
            if v['n'].lower() not in have: a['v'].append(v); have.add(v['n'].lower()); cnt.setdefault('v',0); cnt['v']+=1
hb={x['n'].lower() for x in d['brands']}
for br in spec.get('brands',[]):
    if br['n'].lower() not in hb: d['brands'].append(br); hb.add(br['n'].lower()); cnt['b']+=1
if spec.get('notes'): d['notes']=d.get('notes','')+' DEEP: '+spec['notes']
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(job,cnt)
