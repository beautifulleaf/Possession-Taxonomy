import json,os,urllib.parse
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/C3.json'))
ECH='https://en.wikipedia.org/wiki/Echeveria'; SEM='https://en.wikipedia.org/wiki/Sempervivum'
def ent(n,d_,s,dt):
    return {"n":n,"a":"","d":d_,"mk":"","y":"","s":s,"dt":dt,"v":[]}
add={'Echeveria':[
 ent("Echeveria 'Black Prince'","Dark-leaved Echeveria cultivar listed among the genus's cultivars and hybrids.",ECH,"leaf colour · plant size"),
 ent("Echeveria 'Doris Taylor'","Echeveria cultivar listed among the genus's cultivars and hybrids.",ECH,"leaf colour · plant size"),
 ent("Echeveria 'Blue Curl'","Echeveria cultivar with curled leaf edges, named in the genus article.",ECH,"leaf colour · plant size"),
 ent("Echeveria 'Frank Reinelt'","Echeveria cultivar listed among the genus's cultivars and hybrids.",ECH,"leaf colour · plant size"),
 ent("Echeveria 'Painted Lady'","Echeveria cultivar listed among the genus's cultivars and hybrids.",ECH,"leaf colour · plant size"),
 ent("Echeveria 'Worfield Wonder'","Cultivar of the hybrid Echeveria × derosa.",ECH,"leaf colour · plant size"),
 ent("Echeveria 'Oliver'","Cultivar of Echeveria pulvinata.",ECH,"leaf colour · plant size")],
 'Houseleek':[ent("Sempervivum '%s'"%n,"Houseleek cultivar holding the RHS Award of Garden Merit, as listed in the genus article.",SEM,"rosette colour · rosette size") for n in('Bronco','Lilac Time','Othello','Reinhard')]}
seedkinds=set()
def nl_sel(dp,k):
    n=k['n']; dn=dp['n']; ln=n[0].lower()+n[1:] if not n[:2].isupper() else n
    doms={urllib.parse.urlparse(x['s']).netloc for x in k['x']}
    refs=[]
    if 'en.wikipedia.org' in doms: refs.append('Wikipedia genus and species pages')
    if 'www.rhs.org.uk' in doms: refs.append('RHS plant pages')
    others=len(doms-{'en.wikipedia.org','www.rhs.org.uk'})
    if others: refs.append('specialist pages')
    ref=' and '.join(refs) if refs else 'the source page cited on each entry'
    if dn=='Seeds, bulbs & cuttings' or (dn=='Grow your own'):
        nl=f"One entry is a named variety or cultivar group of {ln}; selections within it are versions."
    elif dn=='Mushrooms & living cultures':
        nl=f"One entry is a named species, strain or culture sold as {ln}; regional or supplier strains are versions."
    elif n=='Christmas tree':
        nl="One entry is a tree species sold as a Christmas tree; sizes and grades are versions."
    elif dn=='Cut flowers & Christmas trees':
        nl=f"One entry is a named cultivar or cultivar group sold as {ln}; colour forms are versions."
    else:
        nl=f"One entry is a species or named cultivar group of {ln}; cultivars and forms within it are versions."
    sel=f"No complete register of this kind was fetched. Entries follow the {ref} cited on each entry and are a representative set, not every species or cultivar."
    return nl,sel
cnt=[]
for dp in d['depts']:
  for sc in dp['s']:
    for k in sc['k']:
      b=len(k.get('x',[])); mm=len(k.get('m',[]))
      if k['n'] in add: k['x']=k.get('x',[])+add[k['n']]
      k.pop('m',None)
      if k.get('x'):
        k['nl'],k['sel']=nl_sel(dp,k)
      cnt.append((k['n'],b,len(k.get('x',[])),mm))
json.dump(d,open(R+'work/V4_C3/C3.tmp','w'),ensure_ascii=False,indent=1)
os.replace(R+'work/V4_C3/C3.tmp',R+'out/C3.json')
bp=R+'out/C3_brands.json'; B=json.load(open(bp))
names={x['n'] for x in B['b']}
new=[("Algae Research Supply","Supplier of live algae cultures for aquaria and growers.","https://www.algaeresearchsupply.com/"),
("Oregon Kombucha","Supplier of kombucha cultures.",""),
("House Plants of Australia","Named as maker of an aroid or houseplant selection in this category.",""),
("Conard Pyle Co.","Rose nursery named as maker of a rose cultivar.",""),
("Cants of Colchester","Rose nursery named as maker of a rose cultivar.","")]
for n,dd,s in new:
    if n not in names:
        e={"n":n,"seg":"Specialist","d":dd}
        if s: e["s"]=s
        B['b'].append(e)
json.dump(B,open(R+'work/V4_C3/b.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'work/V4_C3/b.tmp',bp)
json.dump(cnt,open(R+'work/V4_C3/counts.json','w'))
print(sum(c[3] for c in cnt),'m removed')
