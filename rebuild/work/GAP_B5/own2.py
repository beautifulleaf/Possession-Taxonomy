import json,os,sys
p='rebuild/out/B5.json'
d=json.load(open(p))
W='https://en.wikipedia.org/wiki/'
U=[
("SodaStream","PepsiCo","Global group","2018",None,W+"SodaStream"),
("CamelBak","Vista Outdoor","Independent","2015","United States",W+"CamelBak"),
("Viking Professional","The Middleby Corporation","Independent","2013","United States",W+"Viking_Range"),
("AGA cooker","The Middleby Corporation","Independent","2015","United Kingdom",W+"Aga_Rangemaster_Group"),
("Rangemaster","The Middleby Corporation","Independent","2015","United Kingdom",W+"Aga_Rangemaster_Group"),
("Falcon range","The Middleby Corporation","Independent","2015","United Kingdom",W+"Aga_Rangemaster_Group"),
("La Cornue","The Middleby Corporation","Independent",None,None,W+"Aga_Rangemaster_Group"),
("Cuisinart","Conair Corporation","Independent","1989","United States",W+"Cuisinart"),
("Hamilton Beach","Hamilton Beach Brands Holding Company","Independent",None,"United States",W+"Hamilton_Beach_Brands"),
("Sunbeam Mixmaster","Newell Brands","Global group",None,"United States",W+"Sunbeam_Products"),
("Russell Hobbs K2","Spectrum Brands","Global group","2010","United Kingdom",W+"Russell_Hobbs"),
("Bodum Santos","Bodum","Independent",None,None,W+"Bodum"),
("Chambord","Bodum","Independent",None,None,W+"Bodum"),
("Melitta","Melitta Group","Independent",None,"Germany",W+"Melitta"),
]
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      for e in k.get('x',[]):
        for pre,o,t,oy,c,s in U:
          if e['n'].startswith(pre) and e.get('own') in (None,'','owner not stated'):
            e['own']=o;e['tier']=e.get('tier') if e.get('tier') in('Global group','National champion') and t!='Global group' else t
            if oy:e['own_y']=oy
            if c and not e.get('cty'):e['cty']=c
            print(e['n'],e['own'],e['tier'],e.get('own_y'),e['s'][:60]);
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.rename(p+'.tmp',p)
