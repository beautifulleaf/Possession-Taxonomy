import json,collections
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/V4_J2/J2.new.json'))
# merge brand entries into existing named product entries with same mk
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      xs=k.get('x') or []
      out=[]
      for x in xs:
        if x.get('own') and not x.get('_f'):
          tw=[o for o in xs if o is not x and not o.get('own') and o.get('mk')==x['n']]
          if tw:
            t=tw[0]; t['v']=(t.get('v') or [])+x['v']
            for f in('own','tier','cty','own_y'):
              if f in x: t[f]=x[f]
            continue
        out.append(x)
      if xs: k['x']=out
      # hagoromo
      for x in out:
        if x['n']=='Sea Chicken':
          x.update({'own':'Hagoromo Foods Corporation','tier':'National champion','cty':'Japan','g':'National champion'})
          x['d']="Japanese tuna flakes launched 1958 by Hagoromo, described as one of Japan's leading canned tuna brands."
        if x['n']=='Birds Eye fish fingers' and 'own' not in x: pass
      if out:
        o=lambda g:(0 if g.startswith('Global') else 1 if g=='National champion' else 2 if g=='Independent' else 3 if g=='Own label' else 4 if g.startswith('Brands') else 5)
        out.sort(key=lambda x:(o(x['g']),x['g'],x.get('y') or '9999',x['n'].lower()))
fm='https://www.foodnavigator.com/Article/2023/01/30/euromonitor-cracks-the-lid-on-canned-seafood-tiktok-craze/'
note='share of US canned seafood, Euromonitor figure quoted by FoodNavigator; value or volume not stated'
ms=[
 {"mkt":"US canned seafood","who":"StarKist (Dongwon Industries)","share":"33 %","yr":2022,"s":fm,"note":note},
 {"mkt":"US canned seafood","who":"Bumble Bee (FCF Co, Ltd.)","share":"25.5 %","yr":2022,"s":fm,"note":note},
 {"mkt":"US canned seafood","who":"Chicken of the Sea (Thai Union Group)","share":"about 10 %","yr":2022,"s":fm,"note":note},
 {"mkt":"US canned seafood","who":"Private label","share":"13.9 %","yr":2022,"s":fm,"note":"share at 31 December 2022, up from 12.9 % on 1 January 2020; "+note},
 {"mkt":"US canned seafood","who":"Artisanal brands","share":"about 11 %","yr":2022,"s":fm,"note":note},
 {"mkt":"Italian canned fish","who":"Bolton Group (Rio Mare)","share":"38 %","yr":2016,"s":"https://en.wikipedia.org/wiki/Bolton_Group","note":"share of the Italian canned fish sector, as the Wikipedia page states"},
 {"mkt":"Spanish canned fish","who":"Jealsa Rianxeira","share":"first operator (no figure)","yr":2018,"s":"https://www.alimarket.es/alimentacion/noticia_amp/298766/grupo-calvo-redujo-sus-ventas-un-5-7--en-2018","note":"Alimarket ranks Jealsa Rianxeira first and Grupo Calvo second; no percentage is given. Jealsa turnover close to 650 million euro in 2018"},
 {"mkt":"Spanish canned fish","who":"Grupo Calvo (Calvo family 77.8 %, Bolton Group 22.2 %)","share":"second operator (no figure)","yr":2018,"s":"https://www.alimarket.es/alimentacion/noticia_amp/298766/grupo-calvo-redujo-sus-ventas-un-5-7--en-2018","note":"ownership split from the Wikipedia page on Grupo Calvo (https://en.wikipedia.org/wiki/Grupo_Calvo)"},
 {"mkt":"Global canned tuna","who":"Thai Union Group","share":"largest producer (no figure)","yr":2010,"s":"https://en.wikipedia.org/wiki/John_West_Foods","note":"the page says Thai Union became the world's largest canned-tuna producer after buying MWBrands (John West) in 2010"},
 {"mkt":"UK tinned food","who":"Princes (NewPrinces)","share":"largest supplier (no figure)","yr":2013,"s":"https://en.wikipedia.org/wiki/Princes_Group","note":"by 2013 the UK's largest supplier of tinned food; owned by NewPrinces since July 2024, before that Mitsubishi Corporation"},
]
sup=[]
src='https://www.aol.com/articles/dock-doorbell-9-best-freshest-174700667.html'
names=["Alaskan Salmon Company","Citarella","Sea2Table","Sizzlefish","Get Maine Lobster","LobsterAnywhere","VitalChoice","Omaha Steaks","Fulton Fish Market"]
notes=["wild-caught Alaskan seafood (labelled brand spotlight)","never-frozen fish from the Fulton Fish Market","traceable domestic wild-caught seafood","portioned frozen fillets and subscription boxes","Maine lobster and lobster kits","large lobster tails and shellfish","wild seafood, canned goods and supplements","seafood alongside beef","wide variety including sushi-grade fish"]
for i,(n,t) in enumerate(zip(names,notes),1):
  sup.append({"mkt":"US online seafood delivery (AOL list of nine services, 3 April 2026)","who":n,"share":f"listed {i} of 9","yr":2026,"s":src,"note":t+"; an editorial list, not a scored ranking. Delivery services themselves belong to I3"})
for dp in d['depts']:
  if dp['n']=='Tinned & jarred fish': dp['ms']=ms
  if dp['n']=='Fresh & frozen fish': dp['ms']=sup
json.dump(d,open(R+'work/V4_J2/J2.final.json','w'),ensure_ascii=False,indent=1)
# brand register
b=json.load(open(R+'work/V4_J2/bak/J2_brands.json'))
have={x['n'] for x in b['b']}
def ent(n,c,f,seg,kf,desc,s):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":desc,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s}
W='https://en.wikipedia.org/wiki/'
new=[ent("Thai Union Group","Thailand","","Global group","Tinned tuna","Seafood group that owns Chicken of the Sea (since 2000), John West (2010), King Oscar (2014), Petit Navire and Mareblu.",W+"Thai_Union_Group"),
 ent("Bolton Group","Italy","","Global group","Tinned tuna","Italian group that owns Rio Mare, Saupiquet (1999), Wild Planet (2021) and Conservas Garavilla (2016) and holds 22.2 % of Grupo Calvo.",W+"Bolton_Group"),
 ent("Dongwon Industries","South Korea","","Global group","Tinned tuna","Korean seafood group that bought StarKist from Del Monte Foods on 24 June 2008.",W+"StarKist"),
 ent("FCF Co, Ltd.","Taiwan","","Global group","Tinned tuna","Taiwanese seafood company that bought Bumble Bee in March 2020.",W+"Bumble_Bee_Foods"),
 ent("Century Pacific Food, Inc.","Philippines","1978","Independent","Tinned tuna","Philippine food company (parent founded 1978 as Century Canning Corporation) that makes Century Tuna and 555 and agreed to buy Ligo in December 2021.",W+"Century_Pacific_Food"),
 ent("Princes","United Kingdom","1880","National champion","Tinned tuna","Liverpool tinned food company; owned by NewPrinces since July 2024, before that Mitsubishi Corporation.",W+"Princes_Group"),
 ent("Grupo Calvo","Spain","1940","National champion","Tinned tuna","Spanish canner from Carballo, Galicia; Calvo family 77.8 %, Bolton Group 22.2 %; brands Calvo, Razo, Nostromo, Gomes da Costa, San Marco.",W+"Grupo_Calvo"),
 ent("Hagoromo Foods Corporation","Japan","","National champion","Sea Chicken","Japanese maker of Sea Chicken canned tuna.","https://www.encyclopedia.com/books/politics-and-business-magazines/hagoromo-foods-corporation"),
]
for e in new:
    if e['n'] not in have: b['b'].append(e)
# enrich existing: Ortiz, Chicken of the Sea, John West, StarKist already present
json.dump(b,open(R+'work/V4_J2/J2_brands.new.json','w'),ensure_ascii=False,indent=1)
print('ok')
