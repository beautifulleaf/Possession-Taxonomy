import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C3.json'
d=json.load(open(P))
W='https://en.wikipedia.org/wiki/'
def ent(n,pg,desc,y=''):
    return {"n":n,"a":"","d":desc,"mk":"","y":y,"s":W+pg,"v":[]}
add={
'Astrophytum':('Astrophytum',[('Astrophytum coahuilense','Cactus of Coahuila and Durango, Mexico, listed as the sixth accepted Astrophytum species.')],'Complete: 6 of 6 species in the Wikipedia Astrophytum page; it names no hybrids or cultivars.'),
'Ariocarpus':('Ariocarpus',[('Ariocarpus bravoanus','Slow-growing Mexican living-rock cactus, one of seven species on the Wikipedia Ariocarpus page.')],'Complete: 7 of 7 species in the Wikipedia Ariocarpus page; the natural hybrid Ariocarpus × drabi is not listed as a species.'),
'Clivia':('Clivia',[],'Complete: 6 of 6 species in the Wikipedia Clivia page.'),
'Pansy orchid':('Miltoniopsis',[],'Complete: 5 of 5 species in the Wikipedia Miltoniopsis page.'),
}
sp_sar=[('alabamensis','2005'),('jonesii','1929'),('rosea','1999')]
hyb_sar=[('popei','S. flava × S. rubra'),('harperi','S. flava × S. minor'),('alava','S. flava × S. alata'),('exornata','S. purpurea × S. alata'),('chelsonii','S. purpurea × S. rubra'),('swaniana','S. purpurea × S. minor'),('courtii','S. purpurea × S. psittacina'),('pureophila','S. purpurea × S. oreophila'),('readii','S. leucophylla × S. rubra'),('excellens','S. leucophylla × S. minor'),('areolata','S. leucophylla × S. alata'),('wrigleyana','S. leucophylla × S. psittacina'),('ahlesii','S. alata × S. rubra'),('rehderi','S. rubra × S. minor'),('gilpinii','S. rubra × S. psittacina'),('formosa','S. minor × S. psittacina')]
sar=[ent('Sarracenia '+n,'Sarracenia','North American pitcher plant species described in %s.'%y,y) for n,y in sp_sar]
sar+=[ent('Sarracenia × '+n,'Sarracenia','Named pitcher-plant hybrid, %s.'%p) for n,p in hyb_sar]
sar+=[ent("Sarracenia × catesbaei 'Violet'",'Sarracenia','RHS Award of Garden Merit cultivar.'),ent("Sarracenia × mitchelliana 'Victoria Morley'",'Sarracenia','RHS Award of Garden Merit cultivar.'),ent("Sarracenia × moorei 'Brooks's Hybrid'",'Sarracenia','RHS Award of Garden Merit cultivar.')]
hel=[('arenicola','2011'),('ceracea','2011'),('chimantensis','2002'),('ciliata','2009'),('collina','2011'),('elongata','2004'),('exappendiculata','2006'),('folliculata','2001'),('glabra','2006'),('hispida','2000'),('huberi','2009'),('ionasi','1978'),('macdonaldae','1931'),('neblinae','1978'),('parva','2011'),('purpurascens','2011'),('sarracenioides','2005'),('tatei','1931'),('uncinata','2009')]
heli=[ent('Heliamphora '+n,'Heliamphora','Sun pitcher species described in %s.'%y,y) for n,y in hel]
lit="amicorum:2006 coleorum:1994 comptonii dinteri divergens dorotheae francisci fulviceps gesineae geyeri gracilidelineata hallii helmutii hermetica:2000 herrei hookeri julii localis marmorata meyeri naureeniae olivacea otzeniana ruschiorum salicola schwantesii vallis-mariae verruculosa villetii viridis werneri".split()
lith=[]
for t in lit:
    n,_,y=t.partition(':'); lith.append(ent('Lithops '+n,'Lithops','Living-stone succulent species of the genus Lithops.',y))
phr="caricinum pearcei klotzschianum boissierianum cabrejosii hirtzii vittatum ramiroi lindleyanum guianense humboldtii warszewiczianum".split()
phra=[ent('Phragmipedium '+n,'Phragmipedium','South American slipper orchid species listed in the Wikipedia species table.') for n in phr]
epi="amplissimum carolinense ceramense dahlii falcifolium giganteum meeboldii moluccanum moszkowskii nobile obtusum papuanum silvaticum".split()
epia=[ent('Epipremnum '+n,'Epipremnum','Climbing aroid species of the genus Epipremnum.') for n in epi]
extra={'North American pitcher plant':(sar,'Covers all 11 species and all 20 named hybrids in the Wikipedia Sarracenia page, plus its RHS Award of Garden Merit cultivars; the last 1,199 characters of the page were not read and other cultivars are not listed.'),
'Sun pitcher':(heli,'Covers 23 of 24 species in the Wikipedia Heliamphora page; the 24th, Heliamphora tyleri, appears outside its table and is not listed.'),
'Living stones':(lith,'Complete: 37 of 37 species in the Wikipedia Lithops page; cultivars are not listed.'),
'Phragmipedium':(phra,'Covers 18 of 18 species in the Wikipedia Phragmipedium species table; six further names in its text, whose status is debated, are not listed.'),
'Pothos':(epia,'Complete: 15 of 15 species in the Wikipedia Epipremnum page.')}
log=[]
def norm(s): return s.lower().replace("'","").strip()
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if not k.get('x'): continue
      n=k['n']; ex={norm(e['n']) for e in k['x']}
      new=[]; line=None
      if n in add:
        pg,es,line=add[n]; new=[ent(a,pg,b) for a,b in es]
      elif n in extra: new,line=extra[n]
      new=[e for e in new if norm(e['n']) not in ex]
      k['x']+=new
      cnt=len(k['x'])
      if line is None:
        ref='RHS Award of Garden Merit pages' if 'RHS' in k['sel'][:90] else 'Wikipedia genus and species pages'
        line="Covers %d entries named on the cited %s; no complete register of this kind was fetched, so species, cultivars or strains not named there are not listed."%(cnt,ref)
      k['sel']=line
      if new: log.append((n,len(new)))
      if len(k['x'])>12: pass
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print(log)
