import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C4.json'
B='/home/user/Possession-Taxonomy/rebuild/out/C4_brands.json'
def load(p=P): return json.load(open(p))
def save(d,p=P):
    t=p+'.tmp'; json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.rename(t,p)
def kind(d,n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
    raise KeyError(n)
def shelf(d,n):
    for dp in d['depts']:
        for s in dp['s']:
            if s['n']==n: return s
    raise KeyError(n)
def dept(d,n):
    for dp in d['depts']:
        if dp['n']==n: return dp
    raise KeyError(n)
def arch(n,mk,d,s,y='',dt='',v=None,a=''):
    o={"n":n,"d":d,"mk":mk,"s":s}
    if a:o['a']=a
    if y:o['y']=y
    if dt:o['dt']=dt
    o['v']=v or []
    return o
def ver(n,mk,d,y=''): return {"n":n,"mk":mk,"y":y,"d":d}
