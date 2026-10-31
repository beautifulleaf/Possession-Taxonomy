import json,re,collections
D='/home/user/Possession-Taxonomy/rebuild/'
P=D+'out/G1_parts/cars_add/ASIA.json'
out=json.load(open(P)); cars=json.load(open(D+'out/G1_parts/CARS.json'))
ks=[x for sh in cars['depts'][0]['s'] for x in sh['k']]
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower().replace('é','e').replace('ë','e'))
ex={}
for k in ks:
    for e in k.get('x',[]):
        ex.setdefault((e['g'],norm(e['n'])),e)
        for v in e.get('v',[]): ex.setdefault((e['g'],norm(v['n'])),e)
def kind2(c):
    x=c.lower()
    if not x: return 'NS'
    R=[(r'coupe utility|coupé utility','Utility coupé'),(r'\bkei\b','Kei car'),(r'microcar','Microcar'),(r'muscle','Muscle car'),(r'roadster','Roadster'),(r'off-roader','Off-roader'),(r'minivan|mpv','MPV'),(r'suv|crossover','SUV'),(r'luxury|executive','Luxury saloon'),(r'sports car','Sports car'),(r'coupe|coupé','Coupé'),(r'city car','City car'),(r'hatchback|liftback','Hatchback'),(r'sedan|saloon','Saloon'),(r'wagon','Estate')]
    for r,k in R:
        if re.search(r,x): return k
    return 'NS'
NSK='Car, body style not stated'
kinds=out['kinds']
loc={}  # (g,norm)->(kind,entry)
for k,v in kinds.items():
    for e in v: loc[(e['g'],norm(e['n']))]=(k,e)
F=json.load(open('facts.json')) if False else None
def facts(g):
    for k,v in kinds.items():
        for e in v:
            if e['g']==g:
                return {a:e[a] for a in ('cty','own','tier') if a in e}
    return {}
yup={}; added=collections.Counter(); filled=collections.Counter()
cur=None; src=None
SRC={}
rows=[]
for line in open('lists.txt'):
    line=line.rstrip('\n')
    if line.startswith('#'):
        h=line[1:].split('|'); cur=h[0]; SRC[cur]=h[1]; continue
    p=line.split('|'); rows.append((cur,p[0],p[1] if len(p)>1 else '',p[2] if len(p)>2 else ''))
GF={}
def gf(g):
    if g not in GF: GF[g]=facts(g)
    return GF[g]
for sec,name,yr,cls in rows:
    if name in ('Holden',) and sec=='Holden': continue
    if yr in ('0',''): yr=''
    g=sec
    if sec=='Nissan' and name.startswith(('Datsun','Dat ')): g='Datsun'
    if sec=='Mazda' and name.startswith('Autozam'): g='Autozam'
    full=name if (name.startswith(g) or (g=='Mazda' and name.startswith(('Eunos','Efini','Amati','Xedos','Autozam')))) else g+' '+name
    if g=='Mazda' and name.startswith('Efini'): pass
    variants=[v for v in name.split('/')] if '/' in name and not name.startswith('Wagon') else [name]
    keys=[]
    for v in variants:
        vv=v if v.startswith(g) else g+' '+v
        keys.append((g,norm(vv))); keys.append((g,norm(v)))
    hit=None
    for kk in keys:
        if kk in loc: hit=('asia',loc[kk]);break
        if kk in ex: hit=('cars',ex[kk]);break
    if hit and hit[0]=='asia':
        k,e=hit[1]
        if yr: e['y']=yr
        if k==NSK and kind2(cls)!='NS':
            kinds[NSK].remove(e); nk=kind2(cls); e['d']=cls; kinds.setdefault(nk,[]).append(e); loc[(e['g'],norm(e['n']))]=(nk,e)
        filled[g]+=1
    elif hit:
        e=hit[1]
        if yr and not e.get('y'): yup[e['g']+'|'+e['n']]=yr
    else:
        nm=variants[0] if variants[0].startswith(g) or g=='Mazda' and name.startswith(('Eunos','Efini','Amati','Xedos')) else g+' '+variants[0]
        nk=kind2(cls)
        if nk=='NS': nk=NSK
        ent={'n':nm,'mk':g,'y':yr,'g':g,'s':SRC.get(sec,''),'v':[],'sec':g}
        if len(variants)>1: ent['a']=' · '.join(variants[1:])
        if nk!=NSK and cls: ent['d']=cls
        ent.update(gf(g))
        kinds.setdefault(nk,[]).append(ent); loc[(g,norm(nm))]=(nk,ent); added[g]+=1
        for v in variants[1:]:
            loc[(g,norm(v if v.startswith(g) else g+' '+v))]=(nk,ent)
out['y_updates']=yup
json.dump(out,open(P,'w'),ensure_ascii=False)
print({k:len(v) for k,v in kinds.items()}); print('added',dict(added)); print('yfilled',sum(filled.values()),'y_updates',len(yup))
print(sum(len(v) for v in kinds.values()), sum(1 for v in kinds.values() for e in v if e['y']))
