exec(open('rebuild/work/GAP_D2/edit2.py').read().split("# OnePlus")[0])
addv('Touchscreen smartphone','Xiaomi',[('Xiaomi 13T','2023'),('Xiaomi 14T','2024'),('Xiaomi 15T','2025'),('Mi MIX 2','2017'),('Mi MIX 3','2018'),('Mi MIX Fold','2021'),('Xiaomi MIX Fold 2','2022'),('Xiaomi MIX Fold 3','2023')])
ent('Touchscreen smartphone','Xiaomi')['s']=W+'List_of_Xiaomi_products'
a=ent('Bluetooth item tracker','Apple AirTag'); a['y']='2021'; a['s']=W+'AirTag'
addv('Bluetooth item tracker','Apple AirTag',[('AirTag (1st generation)','2021'),('AirTag (2nd generation)','2026')])
t=ent('Satellite phone','Thuraya satellite phones'); t['s']=W+'Satellite_phone'
fix_years('Satellite phone','Thuraya satellite phones',{'X5-Touch':'2018','XT Lite':'2021'})
addv('Satellite phone','Thuraya satellite phones',[('Thuraya Skyphone','2024')])
tt=ent('Car sat-nav','TomTom GO'); tt['y']='2004'; tt['s']=W+'TomTom'
tr=ent('Car sat-nav','TomTom Rider'); tr['y']='2006'; tr['s']=W+'TomTom'
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      s=k.get('sel','')
      if 'read in windows to character 250,000 of 351,000' in s:
        s=s.replace('read in windows to character 250,000 of 351,000','read to character 350,000 of 351,327, the rest being the page footer')
        s=s.replace('the Mobira, Series 30+ rows and the products page after character 300,000 and some rows without a listed year are not complete','rows without a listed year carry no year')
        k['sel']=s
json.dump(d,open('rebuild/work/GAP_D2/D2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('rebuild/work/GAP_D2/D2.tmp','rebuild/out/D2.json')
print(len(log))
