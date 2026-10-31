"""Match a retailer directory (name<TAB>slug) against the brand register and the Depop unmatched list.
usage: match.py <dir.txt> <expected category codes, comma-separated e.g. H1,H4>"""
import json,re,sys,collections
def norm(s):
    import unicodedata
    s=''.join(c for c in unicodedata.normalize('NFKD',s) if not unicodedata.combining(c))
    s=s.lower().replace('&','and'); s=re.sub(r'\(.*?\)','',s)
    return re.sub(r'[^a-z0-9]','',s)
f,exp=sys.argv[1],set(sys.argv[2].split(','))
bi=json.load(open('/home/user/Possession-Taxonomy/rebuild/reader/_brand_index.json'))['b']
idx={}
for r in bi: idx.setdefault(norm(r[0]),r)
SUF0=r'\s+(by .*|haircare|hair care|hair|lashes|nailcare|organics|skincare|skin care|beauty|cosmetics|fragrances?|parfums?|perfumes?|paris|london|new york|professionals?|makeup)$'
for r in bi:
    m=re.sub(SUF0,'',r[0],flags=re.I).strip()
    if m!=r[0]: idx.setdefault(norm(m),r)
dmiss={norm(n):n for n in open('/home/user/Possession-Taxonomy/verify/depop/missing.txt').read().split('\n') if n}
rows=[l.split('\t') for l in open(f).read().split('\n') if l and not l.startswith('#')]
c=collections.Counter(); out={'in_expected':[],'in_other':[],'new':[]}
SUF=r'\s+(by .*|haircare|hair care|hair|lashes|nailcare|organics|hairscience|skincare|skin care|beauty|cosmetics|fragrances?|parfums?|perfumes?|paris|london|new york|professional|makeup)$'
def look(n):
    r=idx.get(norm(n))
    m=n
    for _ in range(2):
        if r: break
        m=re.sub(SUF,'',m,flags=re.I).strip(); r=idx.get(norm(m))
    return r
EXP=[(norm(r[0]),r) for r in bi if exp&set(r[3])]
def prefix(n):
    k=norm(n)
    if len(k)<3: return None
    def toks(x): return [norm(t) for t in re.split(r'[\s\-/]+',x) if norm(t)]
    a=toks(n)
    def wp(x,y): return len(x)<len(y) and y[:len(x)]==x
    c=[r for rk,r in EXP if wp(a,toks(r[0])) or wp(toks(r[0]),a)]
    return c[0] if len(c)==1 else None
PFX=set()
for n,s in rows:
    r=look(n)
    if not r or not (exp&set(r[3])):
        r2=prefix(n)
        if r2: r=r2; PFX.add(n)
    k='new' if not r else ('in_expected' if exp&set(r[3]) else 'in_other')
    out[k].append({'homonym_check':k=='in_other','prefix_match':n in PFX,'n':n,'slug':s,'reg':r[0] if r else None,'cats':r[3] if r else [],'depop_unmatched':norm(n) in dmiss})
for k,v in out.items(): print(k,len(v),'of which Depop-unmatched',sum(x['depop_unmatched'] for x in v))
oc=collections.Counter(tuple(x['cats']) for x in out['in_other']); print('in_other cats',oc.most_common(10))
json.dump(out,open(f[:-4]+'.match.json','w'),ensure_ascii=False,indent=0)
