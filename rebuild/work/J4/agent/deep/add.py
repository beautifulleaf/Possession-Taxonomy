#!/usr/bin/env python3
"""usage: add.py JOB spec.json  -- merge additions into shelf JSON (temp+rename).
spec: {"kinds":{"Apple":{"x":[...],"m":[[n,mk]],"v":{"ArchetypeName":[{v}]},"d":..}},"newkinds":[kind...],"brands":[...],"notes":"text appended","drop_m":[["name","mk"]]}"""
import json,sys,os,shutil
job,specp=sys.argv[1:3]
p=f'work/J4/shelves/{job}.json'
d=json.load(open(p)); spec=json.load(open(specp))
os.makedirs('work/J4/agent/deep/bak',exist_ok=True)
bk=f'work/J4/agent/deep/bak/{job}.json'
if not os.path.exists(bk): shutil.copy(p,bk)
kb={k['n']:k for k in d['kinds']}
cnt={'x':0,'v':0,'m':0,'b':0,'k':0}
for kn,ops in spec.get('kinds',{}).items():
    k=kb[kn]
    if 'a' in ops and ops['a']: k['a']=(k.get('a')+' · ' if k.get('a') else '')+ops['a']
    ex={a['n'].lower() for a in k.setdefault('x',[])} if ('x' in ops) else set()
    for a in ops.get('x',[]):
        if a['n'].lower() in ex: print('skip dup arch',a['n']); continue
        a.setdefault('a',''); a.setdefault('mk',''); a.setdefault('y',''); a.setdefault('v',[]); a.setdefault('dt','')
        k['x'].append(a); cnt['x']+=1
    for an,vs in ops.get('v',{}).items():
        a=[a for a in k.get('x',[]) if a['n']==an][0]
        have={v['n'].lower() for v in a.get('v',[])}
        for v in vs:
            if v['n'].lower() in have: print('skip dup v',v['n']); continue
            v.setdefault('mk',''); v.setdefault('y',''); v.setdefault('d',''); a.setdefault('v',[]).append(v); cnt['v']+=1
    if 'drop_m' in ops:
        dm={tuple(t) for t in ops['drop_m']}
        k['m']=[t for t in k.get('m',[]) if tuple(t) not in dm]
    have={tuple(t) for t in k.get('m',[])}
    for t in ops.get('m',[]):
        if tuple(t) in have: print('skip dup m',t); continue
        k.setdefault('m',[]).append(t); cnt['m']+=1
    if ops.get('t'):
        k['t']=list(dict.fromkeys(k.get('t',[])+ops['t']))
for nk in spec.get('newkinds',[]):
    nk.setdefault('a',''); d['kinds'].append(nk); cnt['k']+=1
bn={b['n'].lower() for b in d.setdefault('brands',[])}
for b in spec.get('brands',[]):
    if b['n'].lower() in bn: print('skip dup brand',b['n']); continue
    d['brands'].append(b); cnt['b']+=1
if spec.get('notes'): d['notes']=(d.get('notes') or '')+' DEEPENING PASS: '+spec['notes']
tmp=p+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,p)
print(job,cnt)
