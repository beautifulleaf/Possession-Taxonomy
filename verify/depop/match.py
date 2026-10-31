import json,re,glob,os,collections
D='/home/user/Possession-Taxonomy/verify/depop/'
def norm(s):
    s=s.lower().replace('&','and'); s=re.sub(r'\(.*?\)','',s)
    return re.sub(r'[^a-z0-9]','',s)
bi=json.load(open('/home/user/Possession-Taxonomy/rebuild/reader/_brand_index.json'))['b']
idx={}
for r in bi: idx.setdefault(norm(r[0]),r)
# Depop names that are a register brand plus a line suffix
SUF=r'\s+(kids|plus|petite|tall|curve|maternity|jeans|originals|performance|sport|sportswear|collection|outdoor|by .*)$'
tot=hit=0; per=collections.Counter(); miss=[]
for f in sorted(glob.glob(D+'*.txt')):
    for n in open(f).read().split('\n'):
        if not n or n.startswith('#'): continue
        tot+=1; r=idx.get(norm(n)) or idx.get(norm(re.sub(SUF,'',n,flags=re.I)))
        if r: hit+=1; per[tuple(r[3])[:1]]+=1
        else: miss.append(n)
print('Depop names',tot,'already in a register',hit,'not found',len(miss))
print('matched by first category',per.most_common(12))
open(D+'missing.txt','w').write('\n'.join(miss)+'\n')
