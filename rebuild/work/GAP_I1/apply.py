import json,sys,os,re,glob
P='/home/user/Possession-Taxonomy/rebuild/out/I1.json'
d=json.load(open(P))
kinds={}
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']: kinds[k['n']]=k
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
log=[]
lastcov={}
B=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/GAP_I1/bak/I1.json'))
orig={}
for dp in B['depts']:
  for sh in dp['s']:
    for k in sh['k']: orig[k['n']]=k.get('sel','')

for f in sorted(glob.glob('/home/user/Possession-Taxonomy/rebuild/work/GAP_I1/adds_*.json')):
    for job in json.load(open(f)):
        k=kinds[job['kind']]
        x=k.setdefault('x',[])
        have=set()
        for e in x:
            have.add(norm(e['n']))
            if e.get('a'): have.add(norm(e['a']))
        added=0
        for r in job.get('rows',[]):
            n,y,mk=(r+['','',''])[:3] if isinstance(r,list) else (r,'','')
            g=None
            if isinstance(r,list) and len(r)>3: g=r[3]
            if norm(n) in have: continue
            e={"n":n,"a":"","d":"","mk":mk,"y":y,"s":job['ref'],"v":[],"dt":""}
            if g: e['g']=g
            x.append(e); have.add(norm(n)); added+=1
        lastcov[job['kind']]=(job,)
        sel=None
        log.append((job['kind'],added,len(x)))
        if job.get('xg'): k['xg']=job['xg']
        for nm,g in job.get('setg',{}).items():
            for e in x:
                if norm(e['n'])==norm(nm): e['g']=g
        if job.get('defaultg'):
            for e in x:
                if not e.get('g'): e['g']=job['defaultg']
        if 'entries' in job: pass
for kn,(job,) in lastcov.items():
    k=kinds[kn]; x=k['x']
    base=job.get('base') or orig.get(kn,'')
    base=re.sub(r'\s*No whole-space reference list for this kind was fetched, so coverage is open and not claimed complete\.','',base)
    base=re.sub(r'\s*Entries: \d+\.?\s*$','',base)
    base=re.sub(r'\s*A search for a Wikipedia comparison or list page.*$','',base)
    base=re.sub(r'\s*Covers the clients of that page.*$','',base)
    base=re.sub(r'\s*Covers the clients of the page.*$','',base)
    base=re.sub(r'\s*Covers part of the 204 pages.*$','',base)
    base=base.strip()
    if base and base[-1] not in '.;': base+='.'
    k['sel']=(base+' '+job['cov'].replace('{N}',str(len(x)))).strip()
    if not k['sel'].endswith('.'): k['sel']+='.'
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False); os.replace(tmp,P)
for l in log: print(l)
