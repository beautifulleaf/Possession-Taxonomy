import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'E2.json')); br=json.load(open(P+'E2_brands.json'))
reg={b['n']:b for b in br['b']}
F={ # mk: (cty, own, tier, own_y)
'Hilleberg':('Sweden',None,'Independent',None),
'Daiwa':('Japan','Globeride, Inc.','Independent',None),
'Rossignol':('France','Altor Equity Partners and the Boix-Vives family','Independent','2013'),
'Mammut':('Switzerland','Jacobs Capital','Independent','2021'),
'Lib Tech':('United States','Altamont Capital','Independent','2013'),
'MSR':('United States','Cascade Designs','Independent','2001'),
'Therm-a-Rest':('United States','Cascade Designs','Independent',None),
'Wild Country':('United Kingdom','Oberalp','Independent','2012'),
'Mizuno':('Japan','Mizuno Corporation','Independent',None),
'Ping':('United States','Karsten Manufacturing Corporation','Independent',None),
'La Sportiva':('Italy',None,None,None),
'Dunlop':('United Kingdom','SRI Sports (Sumitomo Rubber Industries)','Global group','2017'),
'Cobra':('United States','Puma','Global group','2010'),
'CCM':('Canada','Sport Maska Inc.','Independent','2024'),
'K2':('United States','Kohlberg & Company','Independent','2017'),
'Head':('Austria',None,None,None),
'Rawlings':('United States','Seidler Equity Partners and MLB Properties','Independent','2018'),
'Easton':('United States',None,None,None),
'Warrior':('United States','New Balance','Global group','2004'),
'Coleman':('United States','Newell Brands','Global group','2015'),
'Rollerblade':('United States','Tecnica Group','Independent',None),
'Orvis':('United States','Perkins family','Independent','1965'),
'Tokyo Marui':('Japan','Tokyo Marui Co.','Independent',None),
'Garmin':('United States','Garmin Ltd.','Independent',None),
}
n=0;nreg=0
for dpt in d['depts']:
  for s in dpt['s']:
    for kk in s['k']:
      for e in kk.get('x',[]):
        mk=e.get('mk')
        if not mk: continue
        f=F.get(mk)
        if f:
          for key,val in zip(('cty','own','tier','own_y'),f):
            if val and not e.get(key): e[key]=val; n+=1
        elif not e.get('cty') and mk in reg and reg[mk].get('c'):
          e['cty']=reg[mk]['c']; nreg+=1
# brand register
for mk,f in F.items():
  b=reg.get(mk)
  if b is None: continue
  for key,val in zip(('c','own','tier'),f[:3]):
    if val and not b.get(key): b[key]=val
print(n,nreg)
for fn,o in (('E2.json',d),('E2_brands.json',br)):
  t=P+fn+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,P+fn)
