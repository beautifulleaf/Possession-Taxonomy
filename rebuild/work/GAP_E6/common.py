import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/E6.json'
def load(): return json.load(open(P))
def save(d):
    t=P+'.tmp'; json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,P)
def kinds(d):
    for dp in d['depts']:
        for sh in dp['s']:
            for k in sh['k']: yield dp,sh,k
def find(d,name):
    for dp,sh,k in kinds(d):
        if k['n']==name: return k
    raise KeyError(name)
def ent(n,d,mk='',y='',s='',g='',v=None,dt='',a='',role=None):
    e={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':v or [],'dt':dt}
    if g: e['g']=g
    if role: e['role']=role
    return e
