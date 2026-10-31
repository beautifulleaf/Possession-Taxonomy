import json,re,os,collections
W='/home/user/Possession-Taxonomy/rebuild/work/CMP_PLANTS/'
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(W+'bak/C3.json'))
kinds={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
def norm(n):
    n=n.lower(); n=re.sub(r"[’'\"‘`]",'',n); n=re.sub(r'\b(apple|potato|rose)$','',n.strip())
    return re.sub(r'\s+',' ',n).strip()
def keys(x):
    ks={norm(x['n'])}
    for t in re.split(r'[·;,]',x.get('a') or ''):
        if t.strip(): ks.add(norm(t))
    return ks
WD='https://www.wikidata.org/wiki/'
added=collections.defaultdict(list); dup=collections.Counter(); cnt=collections.Counter()
def add(kind,q,n,y,phrase,dtv=None):
    k=kinds[kind]; h=set()
    for x in k['x']: h|=keys(x)
    e0={'n':n}; ks=keys(e0)
    cnt[kind]+=1
    if ks&h: dup[kind]+=1; return
    dt=k['x'][0].get('dt','') if k['x'] else ''
    dd=phrase+(', dated '+y if y else '')+'; Wikidata lists it with an English Wikipedia article.'
    k['x'].append({"n":n,"a":"","d":dd,"mk":"","y":y,"s":WD+q,"dt":dt,"v":[]}); added[kind].append(n)
ph={'Hybrid tea rose':'Hybrid tea rose cultivar','Floribunda rose':'Floribunda or grandiflora rose cultivar','English rose':'English rose cultivar','Shrub rose':'Shrub rose cultivar','Climbing rose':'Climbing rose cultivar','Rambler rose':'Rambler rose cultivar','Old garden rose':'Old garden rose cultivar',
 'Dahlia tuber':'Dahlia cultivar','Clematis':'Clematis cultivar','Lily bulb':'Lily cultivar','Rhododendron & azalea':'Rhododendron cultivar','Olive tree':'Olive cultivar','Apple tree':'Apple cultivar','Seed potato':'Potato variety','Cannabis plant':'Cannabis strain'}
for fn in ('wd_roses.tsv','wd_c3other.tsv'):
    for line in open(W+fn):
        kind,q,n,y=line.rstrip('\n').split('|')
        if fn=='wd_roses.tsv': n="'%s'"%n
        add(kind,q,n,y,ph[kind])
cov={'Hybrid tea rose':'rose cultivar','Floribunda rose':'rose cultivar','English rose':'rose cultivar','Shrub rose':'rose cultivar','Climbing rose':'rose cultivar','Rambler rose':'rose cultivar','Old garden rose':'rose cultivar'}
for kind,k in kinds.items():
    s=None
    if kind in cov:
        s="Roses added from Wikidata's 'rose cultivar' items with an English Wikipedia article (230 rows queried 2026-10-31, grouped by the item's description; 132 rows with a clear group were placed across the seven rose kinds, the rest have no stated group and are left out). Not claimed complete."
    elif kind=='Dahlia tuber': s="Complete: 12 of 12 in Wikidata's 'Dahlia cultivar' items with an English Wikipedia article (queried 2026-10-31)."
    elif kind=='Olive tree': s="Covers 35 of 37 in Wikidata's 'olive cultivar' items with an English Wikipedia article (queried 2026-10-31); the other two are a list page and the protected-origin table olive Oliva Ascolana del Piceno."
    elif kind=='Cannabis plant': s="Covers 28 of 29 in Wikidata's 'strain of cannabis' items with an English Wikipedia article (queried 2026-10-31); the generic item 'kush' is left out."
    elif kind in('Clematis','Lily bulb','Rhododendron & azalea'): s="Wikidata's cultivar items with an English Wikipedia article for this genus (queried 2026-10-31) are all listed; Wikidata holds very few."
    elif kind in('Apple tree','Seed potato'): s="Three apple and one potato variety removed in the light pass were re-added after Wikidata confirmed them (queried 2026-10-31); the full canons are in the fresh-produce kinds."
    if s: k['sel']=(k.get('sel','').rstrip()+' '+s).strip()
json.dump(d,open(W+'C3.tmp','w'),ensure_ascii=False,indent=1); os.replace(W+'C3.tmp',R+'out/C3.json')
print({k:len(v) for k,v in added.items()},'total',sum(len(v) for v in added.values()),'dups',dict(dup))
