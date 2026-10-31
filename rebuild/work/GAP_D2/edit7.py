exec(open('rebuild/work/GAP_D2/edit2.py').read().split("# OnePlus")[0])
# Surface Pro / Go generations
sv=[('Surface Pro 3','2014'),('Surface Pro 4','2015'),('Surface Pro (2017)','2017'),('Surface Pro 6','2018'),('Surface Pro 7','2019'),('Surface Pro X','2020'),('Surface Pro 8','2021'),('Surface Pro 9','2022'),('Surface Pro 10','2024'),('Surface Go 2','2020'),('Surface Go 3','2021'),('Surface Go 4','2024')]
addv('Tablet','Microsoft Surface',sv)
# Xiaomi names
xi=[('Xiaomi 13',''),('Xiaomi 14',''),('Xiaomi 15',''),('Xiaomi 17',''),('Redmi Note 13',''),('Redmi Note 14',''),('Redmi Note 15',''),('Redmi K80',''),('Mix Flip',''),('Mix Flip 2','')]
addv('Touchscreen smartphone','Xiaomi',xi)
fix_years('Touchscreen smartphone','Xiaomi',{'Xiaomi 14':'2023'}) if False else None
# OnePlus extra
addv('Touchscreen smartphone','OnePlus',[('OnePlus Open','')])
adde('Tablet',{'n':'OnePlus Pad','d':"OnePlus's Android tablet line: Pad, Pad 2, Pad 3, Pad Go and Pad Lite.",'mk':'OnePlus','y':'','s':W+'OnePlus','g':'OnePlus','v':[{'n':n,'y':''} for n in ('OnePlus Pad','OnePlus Pad 2','OnePlus Pad 3','OnePlus Pad Go','OnePlus Pad Go 2','OnePlus Pad Lite')],'cty':'China','own':'Oppo'})
# Poco names
addv('Touchscreen smartphone','Poco',[('Poco F5 Pro',''),('Poco F6 Pro',''),('Poco F7 Ultra',''),('Poco X8 Pro Max',''),('Poco X8 Power','')])
# Mi Band years
fix_years('Fitness band','Xiaomi Smart Band',{'Mi Band 3':'2018','Mi Band 4':'2019','Mi Band 5':'2020','Mi Band 6':'2021','Smart Band 7':'2022','Smart Band 8':'2023'})
# Garmin Rino, Icom, Tile, SPOT, Baofeng
fix_years('Handheld GPS','Garmin Rino',{'Rino 755t':'2016'}); addv('Handheld GPS','Garmin Rino',[('Rino 750','2016')])
ent('Handheld GPS','Garmin Rino')['s']='https://www.garmin.com/en-US/newsroom/?p=1493'
ent('Handheld GPS','Garmin Rino')['y']='2016'
fix_years('HF base transceiver','Icom HF transceivers',{'IC-718':'2000','IC-7200':'2008','IC-7000':'2006','IC-7700':'2008','IC-9100':'2011'})
fix_years('HF base transceiver','Icom IC-7610',{'IC-7600':'2009'})
fix_years('HF base transceiver','Icom IC-7800 / IC-7851',{'IC-7800':'2004'})
ent('HF base transceiver','Icom HF transceivers')['s']='https://www.radiomuseum.org/m/icom_j_en_2~model.html'
for n,y in (('Tile Mate','2019'),('Tile Pro','2019')): pass
fix_years('Bluetooth item tracker','Tile',{'Tile Mate':'2019','Tile Pro':'2019'}); addv('Bluetooth item tracker','Tile',[('Tile Slim','2019'),('Tile Sticker','2019')])
e=ent('Bluetooth item tracker','Tile'); e['s']=W+'Tile_(company)'; e['own']='Life360' if False else e.get('own','')
if not e['own']: del e['own']
fix_years('Satellite messenger','SPOT satellite messengers',{'SPOT X':'2018'})
ent('Satellite messenger','SPOT satellite messengers')['s']=W+'SPOT_Satellite_Messenger'
ent('Satellite messenger','SPOT satellite messengers')['own']='Globalstar'
addv('Satellite messenger','SPOT satellite messengers',[('SPOT Connect','')])
fix_years('Amateur handheld transceiver','Baofeng UV-5R',{'UV-5R':'2012'})
ent('Amateur handheld transceiver','Baofeng UV-5R')['s']=W+'Baofeng_UV-5R'
# remove unsourced Motorola global-group tier
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      for x in k.get('x',[]):
        if x.get('mk')=='Motorola' and x.get('tier')=='Global group': del x['tier']
# market panels
idc='https://www.idc.com/resource-center/blog/global-tablet-shipments-rise-1-9-in-4q25-as-seasonal-demand-offsets-cooling-replacement-cycle/'
cp='https://counterpointresearch.com/cn/insights/global-smartphone-shipments-share'
for dp in d['depts']:
  if dp['n'].startswith('Tablets'):
    dp['ms']=[m for m in dp['ms'] if m['yr']!=2024]
    dp['ms']+= [{'mkt':'Global tablets, full year','who':'All vendors','share':'151.9 million units, up 5 %','yr':2025,'s':idc,'note':'IDC; the page gives no full-year vendor table'},{'mkt':'Global tablets, fourth quarter','who':'Apple','share':'17.1 million of 40.9 million units (41.9 %)','yr':2025,'s':idc,'note':'IDC, shipments up 8 % on the year'},{'mkt':'Global tablets, fourth quarter','who':'Samsung','share':'6.4 million units','yr':2025,'s':idc,'note':'IDC, down 7.5 %'},{'mkt':'Global tablets, fourth quarter','who':'Lenovo','share':'3.9 million units','yr':2025,'s':idc,'note':'IDC, up 35.3 %'}]
  if dp['n'].startswith('Phones'):
    dp['ms'].append({'mkt':'Global smartphones, full year','who':'All vendors','share':'1,255 million units, up 3 %','yr':2025,'s':cp,'note':'Counterpoint Research; vendor shares are in a spreadsheet not readable from the page'})
json.dump(d,open('rebuild/work/GAP_D2/D2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('rebuild/work/GAP_D2/D2.tmp','rebuild/out/D2.json')
print(len(log))
