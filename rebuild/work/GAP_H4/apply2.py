import json,re,os
P='/home/user/Possession-Taxonomy/rebuild/out/H4.json'
d=json.load(open(P))
kinds={}
for dep in d['depts']:
  for sh in dep['s']:
    for k in sh['k']: kinds[k['n']]=k
src=kinds['Alcohol-based perfume']
W='https://en.wikipedia.org/wiki/'
F='https://fr.wikipedia.org/wiki/'
# old, words, url)
M0={
'Estée':('Floral fragrance','a bright floral fragrance',W+'Estée_(fragrance)'),
'Blue Grass':('Floral fragrance','a floral fragrance',W+'Blue_Grass_(fragrance)'),
'Norell':('Floral fragrance','a green floral fragrance',W+'Norell_(fragrance)'),
'Private Collection':('Floral fragrance','a green floral fragrance',W+'Private_Collection_(fragrance)'),
'Charlie':('Floral fragrance','a floral aldehyde fragrance',W+'Charlie_(fragrance)'),
'White Shoulders':('Floral fragrance','a white floral fragrance',W+'White_Shoulders_(fragrance)'),
'Chanel No. 22':('Floral fragrance','classified as a floral-aldehyde with notes of white flowers',W+'Chanel_No._22'),
'Anaïs Anaïs':('Floral fragrance','a fresh floral white flower bouquet (Perfume Intelligence)','https://perfumeintelligence.co.uk/library/perfume/a/a4/a4p1.htm'),
'Halston':('Chypre fragrance','an amber woody chypre fragrance',W+'Halston_(fragrance)'),
'Polo':('Chypre fragrance','a woody chypre',W+'Polo_(fragrance)'),
'Fidji':('Chypre fragrance','of the green floral chypre kind (French: floraux verts chyprés)',F+'Fidji_(parfum)'),
'Oscar':('Amber fragrance','a floral amber fragrance',W+'Oscar_(fragrance)'),
'Classique':('Amber fragrance','described as an oriental floral fragrance',W+'Classique_(fragrance)'),
'Ambre Antique':('Amber fragrance','of the ambré-oriental family (French)',F+'Ambre_Antique'),
"L'Origan":('Amber fragrance','of the oriental floral kind (French: oriental floral)',F+"L'Origan"),
'Old Spice':('Amber fragrance','an amber fragrance with citrus notes (early American Old Spice)',W+'Old_Spice'),
'Chaz':('Fougère fragrance','an aromatic fougère',W+'Charlie_(fragrance)'),
'Escape':('Aquatic & ozonic fragrance','a floral aquatic fragrance',W+'Calvin_Klein_(fashion_house)'),
}
M={
'A*Men':('Gourmand fragrance','a gourmand scent',W+'Gourmand_(fragrance)'),
'Lolita Lempicka':('Gourmand fragrance','a gourmand scent',W+'Gourmand_(fragrance)'),
'Euphoria':('Gourmand fragrance','a gourmand scent (Calvin Klein Euphoria)',W+'Gourmand_(fragrance)'),
'Fantasy':('Fruity fragrance','in the sweet and fruity fragrance family',W+'Fantasy_(fragrance)'),
}
def period(y):
    m=re.search(r'\d{4}',y or '')
    if not m: return 'Before 1900' if 'century' in (y or '') else 'Year not stated'
    v=int(m.group())
    return 'Before 1900' if v<1900 else '1900 to 1949' if v<1950 else '1950 to 1979' if v<1980 else '1980 to 1999' if v<2000 else '2000 to 2009' if v<2010 else '2010 onwards'
def key(x):
    m=re.search(r'\d{4}',x.get('y') or '')
    return (period(x.get('y')) and ['Before 1900','1900 to 1949','1950 to 1979','1980 to 1999','2000 to 2009','2010 onwards','Year not stated'].index(period(x.get('y'))), int(m.group()) if m else 0, x['n'])
moved=[]
for n,(tk,words,url) in M.items():
    hit=[x for x in src['x'] if x['n']==n]
    if len(hit)!=1: print('skip',n,len(hit)); continue
    x=hit[0]; src['x'].remove(x)
    x['d']=f"Wikipedia describes the family as {words}. "+x['d'] if 'perfumeintelligence' not in url else f"Perfume Intelligence describes it as {words}. "+x['d']
    if url.startswith('https://fr.'): x['d']=x['d'].replace('Wikipedia describes','French Wikipedia describes')
    x['s']=url
    kinds[tk]['x'].append(x); moved.append((n,tk))
for k in kinds.values():
    if k.get('xg') and k['x'] and k['n'] not in ('Alcohol-based perfume',) and not any(x.get('g') for x in k['x']) and k['n'] in ('Floral fragrance','Fruity fragrance','Amber fragrance','Gourmand fragrance','Oud fragrance','Musk & skin scent','Woody fragrance','Chypre fragrance','Leather fragrance','Citrus & eau de cologne','Green fragrance','Aquatic & ozonic fragrance','Fougère fragrance'):
        pass
FAM=('Floral fragrance','Fruity fragrance','Amber fragrance','Gourmand fragrance','Oud fragrance','Musk & skin scent','Woody fragrance','Chypre fragrance','Leather fragrance','Citrus & eau de cologne','Green fragrance','Aquatic & ozonic fragrance','Fougère fragrance')
for n in FAM:
    k=kinds[n]
    for x in k['x']: x['g']=period(x.get('y'))
    k['x'].sort(key=key)
    k['xg']='by launch period, then year, then name'
src['x'].sort(key=key)
cnt=len(src['x'])
src['sel']=re.sub(r'Covers \d+ of the 611 named perfumes in this department[^.]*\.',f'Covers {cnt} of the 611 named perfumes in this department (the other {611-cnt} sit in family kinds).',src['sel'])
src['sel']+=f" Second gap batch 2026-10-31: Wikipedia API extracts, search snippets and French Wikipedia placed {len(moved)} more; Wikipedia has no article, or none that states a family, for the rest, and Perfume Intelligence's A-Z pages state families but were too many pages to read."
cov={
'Collectible perfume bottle':' No complete list exists; follows the museum pages fetched (Victoria and Albert Museum, Corning).',
'Bulb atomiser':' No complete list exists; follows the DeVilbiss page.',
'Absolute & CO2 extract':' Covers 32 plant materials named in Wikipedia\'s Perfume article, read in full; no complete list of absolutes exists.',
'Animalic & resin material':' No complete list exists; follows Wikipedia\'s Perfume article and its category pages.',
}

tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
print(moved,cnt)
