import json,os,unicodedata,re
J='/home/user/Possession-Taxonomy/rebuild/out/J7.json'
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
def load(): return json.load(open(J))
def save(d):
    t=J+'.tmp'; json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,J)
def dept(d,n): return next(x for x in d['depts'] if x['n']==n)
def findkind(dp,n):
    for s in dp['s']:
        for k in s['k']:
            if k['n']==n: return s,k
def allnames(dp):
    r={}
    for s in dp['s']:
        for k in s['k']:
            for e in k.get('x',[]):
                r[norm(e['n'])]=(k['n'],e)
                for a in (e.get('a') or '').split(';'):
                    if a.strip(): r.setdefault(norm(a),(k['n'],e))
    return r
def add(dp,kname,entry,names=None):
    s,k=findkind(dp,kname)
    names=names if names is not None else allnames(dp)
    if norm(entry['n']) in names: return False
    e={'n':entry['n'],'a':entry.get('a',''),'d':entry.get('d',''),'mk':'','y':entry.get('y',''),'s':entry['s'],'v':[]}
    for kk in ('g','dt'):
        if kk in entry: e[kk]=entry[kk]
    k.setdefault('x',[]).append(e); names[norm(entry['n'])]=(kname,e); return True
def cover(k,sentence):
    if sentence not in k.get('sel',''): k['sel']=(k.get('sel','').rstrip()+' '+sentence).strip()
