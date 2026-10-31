import json,os,re
from urllib.parse import urlparse
P='rebuild/out/J10.json'
d=json.load(open(P))
kinds={K['n']:K for D in d['depts'] for S in D['s'] for K in S['k']}
NP='https://en.wikipedia.org/wiki/Nicotine_pouch'; SN='https://en.wikipedia.org/wiki/Snus'
def add(kind,n,own,cty,desc,s,y='',tier=None):
    K=kinds[kind]
    if any(e['n'].lower()==n.lower() for e in K['x']): return
    K['x'].append({'n':n,'a':'','d':desc,'mk':n,'y':y,'s':s,'own':own,'tier':tier or ('Global group' if own in('British American Tobacco','R.J. Reynolds','Swedish Match','Japan Tobacco') else 'Independent'),'cty':cty,**({'g':own} if K.get('xg') else {})})
add('Nicotine pouch','Zonnic','R.J. Reynolds','','Developed by the start-up Niconovum, registered in 2008 as a medicinal product; R.J. Reynolds bought Niconovum in 2009.',NP,'2008')
add('Nicotine pouch','Epok','British American Tobacco','Norway','Sold in Norway 2014 to 2018, then re-released in 2018 with a little bleached tobacco added.',NP,'2014')
add('Nicotine pouch','LYFT','owner not stated','Sweden','Pouch brand sold in Sweden; the page does not name the owner.',NP)
add('Nicotine pouch','Velo','owner not stated','','Pouch brand named on the page in a 2025 advertisement caption; no owner stated there.',NP)
add('Nicotine pouch','ZZU','owner not stated','South Korea','Pouch brand described as locally developed in South Korea.',NP)
add('Nicotine pouch','Nordic Spirit','owner not stated','','Tobacco-free pouch brand; a 2025 study of it was funded by Japan Tobacco International.',NP)
add('Nicotine pouch','Zone','owner not stated','','Pouch brand shown in a 2025 NASCAR advertisement caption.',NP)
add('Nicotine pouch','Garant','owner not stated','','Pouch brand named in an image caption.',NP)
add('Nicotine pouch','Engu','owner not stated','','Pouch brand named in a pricing reference.',NP)
add('Portion snus','Blue Ocean','owner not stated','','White portion snus listed on the Snus page.',SN)
add('Portion snus','Grovsnus Svart','owner not stated','','White portion snus listed on the Snus page.',SN)
add('Portion snus','General Onyx','owner not stated','','White portion snus listed on the Snus page.',SN)
add('Dipping tobacco','Makla El Hilal','owner not stated','Algeria','Algerian brand of Chemma or Makla, an oral moist snuff first made under French rule.',SN)
for k in ['Nicotine pouch']:
    kinds[k]['sel']="No complete list exists; follows Wikipedia's Nicotine pouch (read whole) and brand pages. Complete: every pouch brand the page names, 10 in all; Skruf and AG Snus are makers without a named pouch brand, and On! is not on the page."
kinds['Portion snus']['sel']="No complete list exists; follows Wikipedia's Snus (whole page), Ettan snus and Swedish Match pages. Complete: every portion snus the Snus page names with a product form; Catch, Skruf, Kronan, Camel Snus and Marlboro Snus are not on it."
# fill g where missing
for K in kinds.values():
    if K.get('xg'):
        for e in K['x']:
            if not e.get('g'): e['g']=e.get('own') or e.get('mk') or 'Not stated'
# remove loose models
removed={}
for K in kinds.values():
    if K.get('m'):
        removed[K['n']]=[m[0] for m in K['m']]
        K['m']=[]
# nl/sel
for K in kinds.values():
    if K.get('x'):
        if not K.get('nl'):
            base=re.sub(r'\s*\(.*\)','',K['n']).lower()
            K['nl']=f"One entry is a named {base} product, brand or range sold under its own name; variants the source treats separately are versions."
        if not K.get('sel'):
            doms=sorted({urlparse(e['s']).netloc for e in K['x'] if e.get('s')})
            K['sel']=f"No complete list exists; follows the pages cited on each entry ({', '.join(doms)})."
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
json.dump(removed,open('rebuild/work/GAP_J10/removed_models.json','w'),ensure_ascii=False,indent=1)
print(sum(map(len,removed.values())))
