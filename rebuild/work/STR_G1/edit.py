import json,os,sys,copy,re
OUT='/home/user/Possession-Taxonomy/rebuild/out/'
W='/home/user/Possession-Taxonomy/rebuild/work/STR_G1/'
def load(): return json.load(open(OUT+'G1.json'))
def save(d):
    json.dump(d,open(OUT+'G1.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(OUT+'G1.json.tmp',OUT+'G1.json')
def parse_tt(s):
    g=[]
    for part in s.split(';'):
        part=part.strip()
        if not part: continue
        lab,vals=part.split(':',1)
        g.append([lab.strip(),[v.strip() for v in vals.split('|') if v.strip()]])
    return g
POWER='Power:Petrol|Diesel|Hybrid|Plug-in hybrid|Battery electric'
def jl(p,default):
    try: return json.load(open(p))
    except Exception: return default
def apply(dname,spec):
    d=load(); dp=[x for x in d['depts'] if x['n']==dname][0]
    if dp.get('t') and not spec.get('force'): print('already done',dname); return
    pool={}
    for s in dp['s']:
        for k in s['k']: pool[k['n']]=k
    ren=jl(OUT+'G1_renames.json',{})
    for old,new in spec.get('ren',{}).items():
        k=pool.pop(old); k['n']=new; pool[new]=k; ren[old]=new
    # merges: {absorbed: kept}
    for ab,keep in spec.get('merge',{}).items():
        a=pool.pop(ab); t=pool[keep]
        for key in ('x','m','r'): t[key]=(t.get(key) or [])+(a.get(key) or [])
        al=[z for z in (t.get('a','')+' · '+a['n']+' · '+a.get('a','')).split(' · ') if z]
        t['a']=' · '.join(dict.fromkeys(al)); ren[ab]=keep
    for k in spec.get('add',[]): pool[k['n']]=k
    # demotions: (kind, archetype, 'r'|'type')
    for kn,an,to in spec.get('dem',[]):
        k=pool[kn]; ar=[a for a in k.get('x',[]) if a['n']==an]
        assert ar,(kn,an); a=ar[0]; k['x']=[z for z in k['x'] if z is not a]
        m=k.setdefault('m',[]); 
        for v in a.get('v',[]) or []:
            e=[v['n'],v.get('mk') or a.get('mk','')]
            if e not in m and v['n']!=an: m.append(e)
        if to=='r':
            r=k.setdefault('r',[]); e=[a['n'],a.get('mk','')]
            if e not in r: r.append(e)
        if not k['x']: k.pop('x')
    for kn,s in spec['tt'].items():
        k=pool[kn]; k.pop('t',None); k['tt']=parse_tt(s)
    for kn,dd in spec.get('d',{}).items(): pool[kn]['d']=dd
    for kn,sv in spec.get('see',{}).items(): pool[kn]['see']=sv
    for kn,al in spec.get('alias',{}).items(): pool[kn]['a']=al
    shelves=[]; used=set()
    for sh in spec['shelves']:
        ks=[]
        for kn in sh['k']:
            ks.append(pool[kn]); used.add(kn)
        s={'n':sh['n'],'t':sh['t']}
        if sh.get('ax'): s['ax']=sh['ax']
        s['k']=ks; shelves.append(s)
    miss=set(pool)-used; assert not miss,miss
    for k in pool.values():
        assert 'tt' in k or not k.get('t') or True
    dp['t']=spec['t']; dp['ax']=spec['ax']
    if 'note' in spec: dp['note']=spec['note']
    dp['s']=shelves
    save(d); json.dump(ren,open(OUT+'G1_renames.json','w'),ensure_ascii=False,indent=1)
    open(W+'progress.md','a').write(f'step done dept {dname}\n'); print('done',dname)
