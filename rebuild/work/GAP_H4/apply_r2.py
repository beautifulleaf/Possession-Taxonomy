import json,re,os,csv
P='/home/user/Possession-Taxonomy/rebuild/out/H4.json'
d=json.load(open(P))
kinds={}
for dep in d['depts']:
  for sh in dep['s']:
    for k in sh['k']: kinds[k['n']]=k
src=kinds['Alcohol-based perfume']
ORDER=['Before 1900','1900 to 1949','1950 to 1979','1980 to 1999','2000 to 2009','2010 onwards','Year not stated']
def period(y):
    m=re.search(r'\d{4}',y or '')
    if not m: return 'Before 1900' if 'century' in (y or '') else 'Year not stated'
    v=int(m.group())
    return ORDER[0] if v<1900 else ORDER[1] if v<1950 else ORDER[2] if v<1980 else ORDER[3] if v<2000 else ORDER[4] if v<2010 else ORDER[5]
def key(x):
    m=re.search(r'\d{4}',x.get('y') or '')
    return (ORDER.index(period(x.get('y'))), int(m.group()) if m else 0, x['n'])
rows=[l.rstrip('\n').split('\t') for f in ('r2hits.tsv','r3hits.tsv') for l in list(open(f))[1:]]
moved=[]
for n,tk,words,url in rows:
    hit=[x for x in src['x'] if x['n']==n]
    if len(hit)!=1: print('skip',n,len(hit)); continue
    x=hit[0]; src['x'].remove(x)
    x['d']=f"Perfume Intelligence describes it as {words}. "+x['d']
    x['s']=url
    kinds[tk]['x'].append(x); moved.append(n)
FAM=('Floral fragrance','Fruity fragrance','Amber fragrance','Gourmand fragrance','Oud fragrance','Musk & skin scent','Woody fragrance','Chypre fragrance','Leather fragrance','Citrus & eau de cologne','Green fragrance','Aquatic & ozonic fragrance','Fougère fragrance')
for n in FAM:
    k=kinds[n]
    for x in k['x']: x['g']=period(x.get('y'))
    k['x'].sort(key=key)
src['x'].sort(key=key)
cnt=len(src['x'])
src['sel']=re.sub(r'Covers \d+ of the 611 named perfumes in this department[^.]*\.',f'Covers {cnt} of the 611 named perfumes in this department (the other {611-cnt} sit in family kinds).',src['sel'])
if 'Round two' not in src['sel']:
    src['sel']+=" Round two placed more from Perfume Intelligence house pages (perfumeintelligence.co.uk/library); its A-Z pages and the other houses were only partly read."
# owners
OW={'Dana Perfumes':('Dana Classic Fragrances','2003'),'Dana':('Dana Classic Fragrances','2003'),'Britney Spears':('Elizabeth Arden',''),'Gloria Vanderbilt':('Selective Beauté International',''),'Prince Matchabelli':('DeCoeur Fragrances',''),'Guy Laroche':('L\'Oréal',''),'Giorgio Beverly Hills':('Avon Products','1987'),'Elizabeth Taylor':('Parfums International',''),'Acqua di Parma':('LVMH','2005')}
ONAME={'Rebelle':'Parlux Fragrances','Rogue by Rihanna':'Parlux Fragrances','Fame':'Coty','Glowing by JLo':'Coty','Celine Dion Parfums':'Coty','Rise':'Coty'}
on=0
for k in kinds.values():
  for x in k.get('x',[]):
    if x.get('own')=='owner not stated':
        o=None
        if x['n'] in ONAME: o=(ONAME[x['n']],'')
        elif x.get('mk') in OW: o=OW[x['mk']]
        if o:
            x['own']=o[0]
            if o[1]: x['own_y']=o[1]
            on+=1
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
print(len(moved),'moved; owners set',on,'; left',cnt)
