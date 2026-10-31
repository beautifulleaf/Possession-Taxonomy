import json,re,os
P='/home/user/Possession-Taxonomy/rebuild/out/D4.json'
d=json.load(open(P))
KN={'BW':'Black-and-white film','CN':'Colour negative film','CR':'Slide film','BR':'Black-and-white reversal film'}
TY={'BW':'Black-and-white film','CN':'Colour negative film','CR':'Slide film','BR':'Black-and-white reversal film'}
DIS='https://en.wikipedia.org/wiki/List_of_discontinued_photographic_films'
kinds={k['n']:k for dep in d['depts'] for sh in dep['s'] for k in sh['k']}
GEN=set('film films color colour kodak fuji fujifilm fujicolor fujichrome agfa agfacolor agfachrome ilford ilfocolor konica foma forte foton series professional pro and plus the plan pan'.split())
def toks(s):
    return [t for t in re.findall(r'[a-z0-9]+',s.lower()) if t not in GEN]
allx=[(k['n'],e) for n,k in kinds.items() if n in KN.values() for e in k['x']]
def exists(mk,name):
    t=toks(name)
    if not t: return False
    key=set(t[:2])
    for kn,e in allx:
        et=set(toks(e['n']))|{w for v in e.get('v',[]) for w in toks(v['n'])}
        if key<=et: return True
    return False
def yr(t):
    m=re.search(r'\d{4}',t); return m.group(0) if m else ''
def status(y):
    y=y.strip()
    if y in('','?','not listed'): return ''
    if '–' in y:
        a,b=y.split('–',1)
        if b=='?': return 'made from '+a
        if a=='?': return 'made until '+b
        return 'made '+a+'–'+b
    return 'dated '+y
EXIST={'Fujifilm','Kodak'}
added=[];skipped=[]
for line in open('rows.txt',encoding='utf8'):
    line=line.rstrip('\n')
    if not line: continue
    c,mk,name,yy=line.split('|')
    if exists(mk,name): skipped.append(name); continue
    kind=kinds[KN[c]]
    g=mk
    # reuse g spellings
    gs={e['g'] for e in kind['x']}
    for cand in gs:
        if cand.lower()==mk.lower(): g=cand
    st=status(yy)
    desc=f"{TY[c]} from {mk}"+(f", {st}." if st else ", dates not given.")
    desc=desc.replace('Colour negative film from','Colour negative film from')
    e={'n':name,'a':'','d':desc,'mk':mk,'y':yr(yy),'s':DIS,'v':[],'dt':'','g':g}
    kind['x'].append(e); added.append((KN[c],name))
    allx.append((KN[c],e))
def ykey(x):
    v=yr(x.get('y','')); return int(v) if v else 9999
for n in KN.values():
    k=kinds[n]; first={}
    for x in k['x']: first[x['g']]=min(first.get(x['g'],9999),ykey(x))
    k['x'].sort(key=lambda x:(first[x['g']],x['g'],ykey(x),x['n']))
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print(len(added),'added',len(skipped),'skipped'); print('SKIPPED:',skipped)
import collections; print(collections.Counter(a[0] for a in added))
