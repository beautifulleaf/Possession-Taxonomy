import json,os
p='rebuild/out/B5.json'
d=json.load(open(p))
U={ # name-prefix: (own, tier, own_y, cty, src)
"Anova Precision":("Electrolux","Global group","2017","United States","https://en.wikipedia.org/wiki/Anova_Culinary"),
"Blendtec":("Wasatch Group","Independent","2021","United States","https://en.wikipedia.org/wiki/Blendtec"),
"AeroPress":("Tiny Capital","Independent","2021","United States","https://en.wikipedia.org/wiki/AeroPress"),
"Instant Pot":("Centre Lane Partners","Independent","2023","Canada","https://en.wikipedia.org/wiki/Instant_Pot"),
"La Marzocco":("De'Longhi S.p.A.","Global group","2023","Italy","https://en.wikipedia.org/wiki/La_Marzocco"),
"Rancilio Silvia":("Ali Group","Independent","2013","Italy","https://en.wikipedia.org/wiki/Rancilio"),
"Dualit Classic":(None,"Independent",None,"United Kingdom","https://en.wikipedia.org/wiki/Dualit"),
"Chemex":(None,None,None,"United States","https://en.wikipedia.org/wiki/Chemex_Coffeemaker"),
}
ch=[]
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      for e in k.get('x',[]):
        for pre,(o,t,oy,c,s) in U.items():
          if e['n'].startswith(pre):
            before=(e.get('own'),e.get('tier'),e.get('own_y'),e.get('cty'))
            if o and e.get('own') in (None,'','owner not stated'): e['own']=o; e['tier']=t or e.get('tier')
            if t and not e.get('tier'): e['tier']=t
            if oy and not e.get('own_y'): e['own_y']=oy
            if c and not e.get('cty'): e['cty']=c
            if not e.get('s'): e['s']=s
            ch.append((e['n'],before,(e.get('own'),e.get('tier'),e.get('own_y'),e.get('cty')),e['s']))
for c in ch: print(c)
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.rename(p+'.tmp',p)
