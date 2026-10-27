import json,os,sys
def load(j): return json.load(open(f'work/J2/shelves/{j}.json'))
def save(j,d):
    p=f'work/J2/shelves/{j}.json'; t=p+'.tmp'
    json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def kind(d,n):
    return next(k for k in d['kinds'] if k['n']==n)
def rename_model(j,old,new):
    d=load(j); c=0
    for k in d['kinds']:
        for m in k.get('m',[]):
            if m[0]==old: m[0]=new; c+=1
    assert c==1,(j,old,c); save(j,d)
def note(j,txt):
    d=load(j); d['notes']+=' | DEEP: '+txt; save(j,d)
def addx(j,kn,n,d,s,mk='',y='',a='',v=None,dt=''):
    D=load(j); k=kind(D,kn)
    if any(x['n']==n for x in k.setdefault('x',[])): return
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: x["v"]=v
    if dt: x["dt"]=dt
    k['x'].append(x); save(j,D)
def addm(j,kn,n,mk=''):
    D=load(j); k=kind(D,kn); k.setdefault('m',[])
    if [n,mk] not in k['m']: k['m'].append([n,mk])
    save(j,D)
def addb(j,n,c,seg,kf,d,s,f='',sig=None):
    D=load(j)
    if any(b['n']==n for b in D['brands']): return
    D['brands'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":[],"eras":[],"sig":sig or [],"sc":[],"rel":[],"s":s}); save(j,D)
