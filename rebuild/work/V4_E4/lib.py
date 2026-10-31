import json,copy,re
SRC=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/V4_E4/bak/E4.json'))
D={dp['n']:dp for dp in SRC['depts']}
KIND={}
SHELF={}
for dp in SRC['depts']:
    for s in dp['s']:
        SHELF[s['n']]=s
        for k in s['k']: KIND[k['n']]=k
WP='https://en.wikipedia.org/wiki/'
REMOVED=[]  # (kind, what, why)
def e(n,d,y='',a='',g='',s='',v=None,mk='',role=''):
    o={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':[{'n':t[0],'y':t[1] if len(t)>1 else '','d':t[2] if len(t)>2 else ''} for t in (v or [])]}
    if g:o['g']=g
    if role:o['role']=role
    return o
def newkind(shelf,name,a,d,s,pos=None):
    k={'n':name,'a':a,'d':d,'s':s,'x':[]}
    L=SHELF[shelf]['k']
    if pos is None: L.append(k)
    else: L.insert(pos,k)
    KIND[name]=k
    return k
def add(kind,entries,nl=None,sel=None,xg=None):
    k=KIND[kind]; x=k.setdefault('x',[])
    have={t['n'].lower():t for t in x}
    for en in entries:
        t=have.get(en['n'].lower())
        if t:
            if en.get('g') and not t.get('g'): t['g']=en['g']
            for vv in en['v']:
                if vv['n'].lower() not in {q['n'].lower() for q in t.setdefault('v',[])}: t['v'].append(vv)
        else:
            x.append(en); have[en['n'].lower()]=en
    if nl:k['nl']=nl
    if sel:k['sel']=sel
    if xg:k['xg']=xg
def dropm(kind,why):
    k=KIND[kind]
    if k.get('m'):
        REMOVED.append((kind,[a for a,b in k['m']],why)); k['m']=[]
        del k['m']
def setg(kind,default=None,mapping=None):
    for x in KIND[kind].get('x',[]):
        if mapping and x['n'] in mapping: x['g']=mapping[x['n']]
        elif default and not x.get('g'): x['g']=default
def rows(text,s,y=''):
    out=[]
    for ln in text.strip().split('\n'):
        p=[q.strip() for q in ln.split('|')]
        n,dd,g=p[0],p[1],p[2]
        yy=p[3] if len(p)>3 else y
        out.append(e(n,dd,yy,g=g,s=s))
    return out
