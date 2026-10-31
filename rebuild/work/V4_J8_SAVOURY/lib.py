import json, copy, re
ROOT='/home/user/Possession-Taxonomy/rebuild/'
OLD=json.load(open(ROOT+'out/J8.json'))
OLDX={}
OLDDEPT={}
for dp in OLD['depts']:
    OLDDEPT[dp['n']]=dp
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x',[]):
                OLDX[e['n']]=e
WP='https://en.wikipedia.org/wiki/'
def E(n,d='',s='',own=None,tier=None,cty=None,y='',own_y='',g='',a='',v=None,role=None,dt='',reuse=None,mk=None):
    if reuse:
        e=copy.deepcopy(OLDX[reuse]); e['n']=n
        if d: e['d']=d
        if s: e['s']=s
        if y!='': e['y']=y
        if a: e['a']=a
        if v is not None: e['v']=v
        if dt: e['dt']=dt
    else:
        e={'n':n,'a':a,'d':d,'mk':'','y':y,'s':s,'v':v or []}
        if dt: e['dt']=dt
    if own is not None:
        e['mk']=own if mk is None else mk
        e['own']=own
    if tier: e['tier']=tier
    if cty: e['cty']=cty
    if own_y: e['own_y']=str(own_y)
    if g: e['g']=g
    if role: e['role']=role
    return e
def V(n,y='',d='',mk=''): return {'n':n,'mk':mk,'y':y,'d':d}
def K(n,d,s,x=None,nl='',sel='',xg='',tt=None,a='',see=None):
    k={'n':n,'a':a,'d':d,'s':s}
    if x is not None:
        k['x']=x
        k['nl']=nl; k['sel']=sel
        if xg: k['xg']=xg
    if tt: k['tt']=tt
    if see: k['see']=see
    return k
TIERS=["Global group","National champion","Independent","Craft & indie","Own label"]
def tt_owner(extra=None):
    t=[["Owner tier",["Global group","National champion","Independent","Craft & indie"]]]
    return t+(extra or [])
def oldkind(dept,kname):
    for sh in OLDDEPT[dept]['s']:
        for k in sh['k']:
            if k['n']==kname: return k
def form_kind(dept,kname,extra_alias=(),drop_entries=True,keep=()):
    """old kind kept as a type kind: entries demoted to aliases, models removed"""
    k=copy.deepcopy(oldkind(dept,kname))
    names=[e['n'] for e in k.get('x',[]) if e['n'] not in keep]
    al=[a.strip() for a in k.get('a','').split('·') if a.strip()]
    for n in list(names)+list(extra_alias):
        if n.lower() not in [a.lower() for a in al] and n.lower()!=k['n'].lower(): al.append(n)
    k['a']=' · '.join(al)
    for f in ('m','r'): k.pop(f,None)
    if drop_entries:
        k['x']=[e for e in k.get('x',[]) if e['n'] in keep]
        if not k['x']:
            k.pop('x')
        else:
            pass
    return k
