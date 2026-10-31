import json,sys,os
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_I3')
from tt import TT
import strc
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/STR_I3/bak/I3.json'))
kinds={}; 
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: kinds[k['n']]=k
before=dict(depts=len(d['depts']),shelves=sum(len(x['s']) for x in d['depts']),kinds=len(kinds),x=sum(len(k.get('x',[])) for k in kinds.values()))
# demote Railcard
rk=kinds['Rail discount card']; keep=[]
for x in rk['x']:
    if x['n']=='Railcard':
        rk.setdefault('m',[])
        rk['m'].append(['Railcard','UK train operators'])
        for v in x['v']: rk['m'].append([v['n'],'UK train operators'])
    else: keep.append(x)
rk['x']=keep
# new kinds
sk=kinds['Season ticket']
for n,nk in strc.NEW.items():
    k={'n':n,'a':nk['a'],'d':nk['d'],'s':nk['s']}
    if nk.get('m'): k['m']=nk['m']
    if nk.get('x_from'):
        k['x']=sk.pop('x'); 
    kinds[n]=k
# fold Cloud-gaming/fitness types out of old kinds handled by tt; drop t
for n,k in kinds.items():
    if n not in TT: print('NO TT',n)
    k['tt']=TT[n]; k.pop('t',None)
    if n in strc.SEE: k['see']=strc.SEE[n]
# check see targets
for n,k in kinds.items():
    for c,tn,w in k.get('see',[]):
        if c=='I3': ok=tn in kinds
        else:
            r=json.load(open(R+f'reader/{c}.json')); ok=any(kk['n']==tn for dp in r['depts'] for s in dp['s'] for kk in s['k'])
        if not ok: print('BAD SEE',n,c,tn)
used=set(); depts=[]
for dp in d['depts']:
    nd={k:v for k,v in dp.items() if k!='s'}
    S=strc.D[dp['n']]; nd['t']=S['t']; nd['ax']=S['ax']; nd['s']=[]
    for sn,st,sa,ks in S['shelves']:
        sh={'n':sn,'t':st}
        if len(ks)>3: sh['ax']=sa
        elif len(ks)>1: sh['ax']=sa
        sh['k']=[kinds[x] for x in ks]; used|=set(ks); nd['s'].append(sh)
    depts.append(nd)
missing=set(kinds)-used
if missing: print('UNPLACED',missing)
d['depts']=depts; d['ax']=strc.CAT_AX; d['key']=strc.KEY
out=R+'out/I3.json'; json.dump(d,open(out+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(out+'.tmp',out)
print(before,dict(depts=len(depts),shelves=sum(len(x['s']) for x in depts),kinds=len(used),x=sum(len(kinds[n].get('x',[])) for n in used)))
