import json,os,sys
sys.path.insert(0,'.')
from spec import *
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open('bak/H1.json'))
kinds={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: kinds[k['n']]=k
for o,n in RENAMES.items():
    k=kinds.pop(o); k['n']=n; kinds[n]=k
# demotions
for kn,xn,dest in DEMOTE:
    kn=RENAMES.get(kn,kn); k=kinds[kn]
    x=[a for a in k['x'] if a['n']==xn]; assert len(x)==1,(kn,xn)
    x=x[0]; k['x']=[a for a in k['x'] if a is not x]
    if not k['x']: del k['x']
    k.setdefault('m',[]); mm=[tuple(t) for t in k['m']]
    def addm(a,b):
        if a and b and (a,b) not in mm: k['m'].append([a,b]); mm.append((a,b))
    mk=x.get('mk','')
    if dest=='m': addm(x['n'],mk)
    if dest=='r':
        k.setdefault('r',[])
        if [x['n'],mk] not in k['r'] and mk: k['r'].append([x['n'],mk])
    for v in x.get('v',[]): addm(v['n'],v.get('mk') or mk)
    if not k['m']: del k['m']
for n,(a,dd,s) in NEW.items():
    kinds[n]={"n":n,"a":a,"d":dd,"s":s}
# apply tt/see
for n,k in kinds.items():
    if n in TT:
        k['tt']=TT[n]; k.pop('t',None)
    elif k.get('t'): print('no tt for',n)
    if n in SEE: k['see']=SEE[n]
for kn,sv in SEE.items():
    for t in sv:
        if t[0]=='H1': assert t[1] in kinds,t
# rebuild shelves
used=set(); out=[]
byname={dp['n']:dp for dp in d['depts']}
for dn,shs in SH.items():
    dp=byname[dn]; dp['t'],dp['ax']=DEPTS[dn]
    dp['s']=[]
    for sn,t,ax,ks in shs:
        sh={"n":sn,"t":t}
        if ax: sh['ax']=ax
        sh['k']=[kinds[x] for x in ks]; used.update(ks)
        dp['s'].append(sh)
missing=set(kinds)-used; assert not missing,missing
d['ax']=CAT_AX; d['key']=CAT_KEY
tmp='tmp_H1.json'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,R+'out/H1.json')
json.dump(RENAMES,open(R+'out/H1_renames.json','w'),ensure_ascii=False,indent=1)
print(len(kinds))
