import json,os,re
exec(open('rebuild/work/GAP_D2/edit1.py').read().split("# Kobo")[0].replace("P='rebuild/out/D2.json'","P='rebuild/out/D2.json'"))
W='https://en.wikipedia.org/wiki/'
def setv(kind,name,vs,s=None,y=None,d=None):
  e=ent(kind,name)
  addv(kind,name,vs)
  if s: e['s']=s
  if y: e['y']=y
  if d: e['d']=d
def fix_years(kind,name,m):
  e=ent(kind,name)
  for v in e['v']:
    if not v.get('y') and v['n'] in m: v['y']=m[v['n']]; log.append(f'year {v["n"]}')
# OnePlus
op=[('OnePlus One','2014'),('OnePlus 2','2015'),('OnePlus X','2015'),('OnePlus 3','2016'),('OnePlus 3T','2016'),('OnePlus 5','2017'),('OnePlus 5T','2017'),('OnePlus 6','2018'),('OnePlus 6T','2018'),('OnePlus 7','2019'),('OnePlus 7 Pro','2019'),('OnePlus 7T','2019'),('OnePlus 8','2020'),('OnePlus 8 Pro','2020'),('OnePlus 8T','2020'),('OnePlus 9','2021'),('OnePlus 9 Pro','2021'),('OnePlus 10 Pro','2022'),('OnePlus 10T','2022'),('OnePlus 11','2023'),('OnePlus 12','2023'),('OnePlus 12R','2024'),('OnePlus 13','2024'),('OnePlus 13R','2024'),('OnePlus 15','2025'),('OnePlus 15R','2025'),('OnePlus Nord','2020'),('OnePlus Nord 2 5G','2021'),('OnePlus Nord 3 5G','2023'),('OnePlus Nord 4','2024'),('OnePlus Nord 5','2025'),('OnePlus Nord 6','2026'),('OnePlus Ace','2022'),('OnePlus Ace 3','2024'),('OnePlus Ace 5','2024'),('OnePlus Ace 6','2025')]
setv('Touchscreen smartphone','OnePlus',op,W+'OnePlus','2014',"OnePlus's flagship numbered phones (One to 15), the Nord mid-range line and the China-only Ace line.")
fix_years('Touchscreen smartphone','OnePlus',dict(op))
# Xiaomi
xi=[('Mi 1','2011'),('Mi 2','2012'),('Mi 3','2013'),('Mi 4','2014'),('Mi 5','2016'),('Mi 6','2017'),('Mi 8','2018'),('Mi 9','2019'),('Mi 10','2020'),('Mi 11','2021'),('Xiaomi 12','2021'),('Xiaomi 12T','2022'),('Xiaomi 15 Ultra','2025'),('Mi MIX','2016')]
setv('Touchscreen smartphone','Xiaomi',xi,'https://en.wikipedia.org/wiki/List_of_Xiaomi_products','2011',"Xiaomi's numbered flagship phones, from the Mi 1 of 2011 to the Xiaomi 17 series.")
fix_years('Touchscreen smartphone','Xiaomi',dict(xi))
# Poco
po=[('Pocophone F1','2018'),('Poco F2 Pro','2020'),('Poco F3','2021'),('Poco F4','2022'),('Poco F5','2023'),('Poco F6','2024'),('Poco F7','2025'),('Poco F7 Pro','2025'),('Poco F8 Pro','2025'),('Poco F8 Ultra','2025'),('Poco X2','2020'),('Poco X3','2020'),('Poco X7 Pro','2025'),('Poco X8 Pro','2026'),('Poco M3','2020'),('Poco C3','2020')]
setv('Touchscreen smartphone','Poco',po,W+'Poco_(smartphone)','2018',"Xiaomi's Poco sub-brand of F, X, M and C series phones, launched in 2018 as Pocophone.")
fix_years('Touchscreen smartphone','Poco',dict(po))
# Garmin handhelds
G='https://gpstraining.co.uk/blogs/news/outdoor-gps-units-release-date-history'
setv('Handheld GPS','Garmin eTrex',[('eTrex (yellow)','1999'),('eTrex Summit','2000'),('eTrex Venture','2001'),('eTrex Vista','2001'),('eTrex Legend','2001'),('eTrex Vista C','2004'),('eTrex Legend CX','2006'),('eTrex H','2007'),('eTrex Legend HCX','2007'),('eTrex 10, 20 and 30','2011'),('eTrex 20x, 30x','2015'),('eTrex Touch 25 and 35','2015'),('eTrex 22x','2019'),('eTrex 32x','2019'),('eTrex SE','2023'),('eTrex Solar','2023')],G,'1999')
fix_years('Handheld GPS','Garmin eTrex',{'eTrex 22x':'2019','eTrex 32x':'2019','eTrex SE':'2023','eTrex Solar':'2023'})
setv('Handheld GPS','Garmin GPSMAP',[('GPS 12','1999'),('GPSMAP 60c / 60cs','2003'),('GPSMAP 60','2005'),('GPSMAP 60cx / 60csx','2006'),('GPSMAP 62','2010'),('GPSMAP 62sc / 62stc','2011'),('GPSMAP 64','2014'),('GPSMAP 66s / 66st','2018'),('GPSMAP 66i','2019'),('GPSMAP 65','2020'),('GPSMAP 66SR','2020')],G,'1999')
fix_years('Handheld GPS','Garmin GPSMAP',{'GPSMAP 67':'2023','GPSMAP 67i':'2023','GPSMAP 64sx':'2014'})
adde('Handheld GPS',{'n':'Garmin Oregon','d':"Garmin's touchscreen handheld GPS line, 2008 to 2016.",'mk':'Garmin','y':'2008','s':G,'g':'Garmin','v':[{'n':'Oregon 200 / 300 / 400t','y':'2008'},{'n':'Oregon 550 / 550t','y':'2009'},{'n':'Oregon 450 / 450t','y':'2009'},{'n':'Oregon 600 / 650','y':'2013'},{'n':'Oregon 700 / 750','y':'2016'}]})
setv('Handheld GPS','Garmin handheld GPS units',[('Montana 600 / 650','2011'),('Montana 610 / 680','2015'),('Montana 700 / 700i / 750i','2020')],G)
fix_years('Handheld GPS','Garmin handheld GPS units',{'Montana 710i':'2024'}) if False else None
# inReach
setv('Satellite messenger','Garmin inReach',[('inReach','2011'),('inReach SE','2013'),('inReach Explorer','2015'),('inReach SE+','2017'),('inReach Explorer+','2017'),('inReach Mini','2018'),('inReach Mini 2','2022'),('inReach Messenger','2022')],W+'Garmin_inReach','2011')
fix_years('Satellite messenger','Garmin inReach',{'inReach Mini 3':'2025','inReach Mini 3 Plus':'2025','inReach Messenger Plus':'2024'})
# Galaxy Watch years
fix_years('Smartwatch','Galaxy Watch',{'Gear Live':'2014','Gear 2':'2014','Gear Fit':'2014','Gear S':'2014','Gear Sport':'2017','Galaxy Gear':'2013','Gear S2':'2015','Gear S3':'2016'})
addv('Smartwatch','Galaxy Watch',[('Gear Fit 2','2016'),('Gear Fit 2 Pro','2017')])
ent('Smartwatch','Galaxy Watch')['s']=W+'Samsung_Gear'
# Ham radio
RL=W+'List_of_amateur_radio_transceivers'
addv('HF base transceiver','Icom HF transceivers',[('IC-7700',''),('IC-7000',''),('IC-7100',''),('IC-9100','')])
addv('Portable QRP transceiver','Yaesu FT-817',[('FT-857','2003')])
fix_years('Portable QRP transceiver','Yaesu FT-817',{'FT-818ND':'2018','FT-817':'2000'})
ent('Portable QRP transceiver','Yaesu FT-817')['s']=RL
fix_years('HF base transceiver','Yaesu FT-991A',{'FT-991A':'2016'})
ent('Mobile transceiver','Yaesu FT-857')['y']='2003'
addv('Mobile transceiver','Yaesu mobile transceivers',[('FTM-500DE','2023')])
addv('Amateur handheld transceiver','Yaesu VX series',[('FT-1DE','2012'),('FT-70DR','2017')])
addv('Amateur handheld transceiver','Baofeng UV-5R',[('UV-82HP',''),('UV-82C',''),('BF-F8+',''),('BF-888S',''),('UV-25X2',''),('UV-50X2','')])
addv('Amateur handheld transceiver','Quansheng UV-K5',[('UV-K6',''),('TG-UV2',''),('TG-UV2 Plus','')])
addv('Amateur handheld transceiver','Alinco DJ-VX11',[('DJ-VX10 / VX50',''),('DJ-VX11',''),('DJ-W100','')])
addv('Amateur handheld transceiver','Wouxun KG-UV9D',[('KG-UV6D','')])
addv('Amateur handheld transceiver','Icom IC-2AT',[('ID-51','')]) if False else None
adde('Portable QRP transceiver',{'n':'Xiegu G90','d':'Chinese portable HF transceiver line.','mk':'Xiegu','y':'','s':RL,'g':'Xiegu','v':[]}) if False else None
# Market summary
fon='https://www.fonearena.com/blog/468173/worldwide-tablet-shipments-q3-2025-idc.html'
tabs=[('Apple','13.2 million of 38 million units'),('Samsung','6.9 million of 38 million units'),('Lenovo','3.7 million of 38 million units'),('Huawei','3.4 million of 38 million units'),('Xiaomi','2.5 million of 38 million units')]
for dp in d['depts']:
  if dp['n'].startswith('Tablets'):
    dp['ms']=[{'mkt':'Global tablets, third quarter','who':w,'share':sh,'yr':2025,'s':fon,'note':'shipments as FoneArena reports them from the IDC Worldwide Quarterly Personal Computing Device Tracker; total down 4.4 % on the year'} for w,sh in tabs]
  if dp['n'].startswith('Wearables'):
    idc='https://www.idc.com/promo/wearablevendor/vendor'
    dp['ms']=[{'mkt':'Global wearable devices, second quarter','who':w,'share':sh,'yr':2026,'s':idc,'note':'share of shipments, about 148 million units in total; IDC wearable vendor results'} for w,sh in [('Apple','15.5 %'),('Xiaomi','11.7 %'),('Huawei','10.9 %'),('Samsung','6.8 %'),('Imagine Marketing','4.9 %')]]
json.dump(d,open('rebuild/work/GAP_D2/D2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('rebuild/work/GAP_D2/D2.tmp','rebuild/out/D2.json')
print(len(log))
