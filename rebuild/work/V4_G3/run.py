import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/G3.json')); b=json.load(open(R+'out/G3_brands.json'))
have={x['n'].lower() for x in b['b']}
newb={}
nm=nr=0
for dep in d['depts']:
  for s in dep['s']:
    for k in s['k']:
      for f in('m','r'):
        for e in k.pop(f,[]):
          mk=e[1] if len(e)>1 else ''
          if f=='m': nm+=1
          else: nr+=1
          if mk and mk.lower() not in have: newb[mk]=1; have.add(mk.lower())
      if k.get('x'):
        k['nl']='One entry is a named historic originator or period type of this kind, each traceable to its own cited page; current makers are in the brand register.'
        k['sel']='No whole-space reference exists for this kind; entries are the traceable originators and period types named by the cited pages, and no catalogue of current models is listed.'
for n in newb:
  b['b'].append({"n":n,"c":"","f":"","seg":"","d":"","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"","kf":""})
cab='https://www.reportprime.com/kitchen-cabinet-r946/company'
def dep(n): return next(x for x in d['depts'] if x['n']==n)
rows=[("MasterBrand Cabinets","3.35","2.22"),("Cabinetworks Group","2.8","1.86"),("Masco Corporation (KraftMaid & Merillat)","2.1","1.39"),("American Woodmark","1.78","1.18"),("IKEA (kitchen segment)","1.65","1.09"),("Nobilia","1.25","0.83"),("Oppein Home Group","1.1","0.73")]
dep('Kitchen')['ms']=[{"mkt":"Global kitchen cabinets","who":w,"share":s+" %","yr":2024,"s":cab,"note":"market share of the global kitchen cabinet market; 2024 revenue US$ %s billion, as the page states"%r} for w,r,s in rows]
dep('Kitchen')['msum']="A published ranking puts the largest kitchen cabinet makers in 2024 at MasterBrand, Cabinetworks and Masco, each with under 3 % of the global market, so the market is fragmented."
san='https://www.mordorintelligence.com/industry-reports/sanitaryware-market'
dep('Bath & wellness')['ms']=[{"mkt":"Global sanitaryware","who":"Asia-Pacific (region)","share":"40.01 %","yr":2026,"s":san,"note":"share of revenue, as the page states"},{"mkt":"Global sanitaryware","who":"Toilets and cisterns (product)","share":"41.66 %","yr":2026,"s":san,"note":"largest product type by share, as the page states"}]
dep('Bath & wellness')['msum']="The report names TOTO, LIXIL (with American Standard and GROHE), Kohler, Roca and Geberit as the leading sanitaryware groups, in no particular order, and calls the market moderately fragmented."
hs=dep('Home systems')
hs['ms']=[{"mkt":"Global PV inverters","who":"Huawei","share":"176 GWac shipped","yr":2024,"s":"https://www.woodmac.com/press-releases/global-pv-inverter-shipments-grew-by-10-in-2024-to-589-gwac/","note":"Huawei and Sungrow together hold 55 % of 589 GWac shipped"},
 {"mkt":"Global PV inverters","who":"Sungrow","share":"148 GWac shipped","yr":2024,"s":"https://www.woodmac.com/press-releases/global-pv-inverter-shipments-grew-by-10-in-2024-to-589-gwac/","note":"third is Ginlong Solis, fourth Growatt"}]
eu='https://www.euromonitor.com/heat-pumps-in-germany/report'
for w,sh in(("Viessmann","17 %"),("Bosch Thermotechnik","13 %"),("Stiebel Eltron","10 %"),("Vaillant","7 %")):
  hs['ms'].append({"mkt":"Germany heat pumps","who":w,"share":sh,"yr":2025,"s":eu,"note":"retail volume sales, as the page states"})
hs['msum']="Two Chinese groups, Huawei and Sungrow, supply 55 % of the world's solar inverters (2024). In German heat pumps Viessmann leads with 17 % of retail volume (2025)."
for w in("Huawei","Sungrow","Ginlong Solis","Growatt","TOTO"):
  pass
json.dump(d,open(R+'out/G3.json.tmp','w'),ensure_ascii=False,indent=1)
json.dump(b,open(R+'out/G3_brands.json.tmp','w'),ensure_ascii=False,indent=1)
os.rename(R+'out/G3.json.tmp',R+'out/G3.json'); os.rename(R+'out/G3_brands.json.tmp',R+'out/G3_brands.json')
print(nm,nr,len(newb))
