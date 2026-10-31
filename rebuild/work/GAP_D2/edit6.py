import json,os
P='rebuild/out/D2.json'
d=json.load(open(P))
cty={'Casio':'Japan','BlackBerry':'Canada','Barnes & Noble':'United States','Globalstar':'United States','Asus':'Taiwan','ASUS':'Taiwan','HTC':'Taiwan','Fujitsu':'Japan','Alinco':'Japan','Elecraft':'United States','Franklin':'United States','Doogee':'China','Ericsson':'Sweden','Baofeng':'China','Atari':'United States','Amazon':'United States','Apple':'United States','Garmin':'United States','Google':'United States','IBM':'United States','Huawei':'China','Inmarsat':'United Kingdom','Hallicrafters':'United States','HP':'United States','Kyocera':'Japan','Lenovo':'China','Meta':'United States','Microsoft':'United States','Motorola':'United States','NEC':'Japan','Nokia':'Finland','Nubia':'China','Kobo':'Canada','OnePlus':'China','Oura':'Finland','Palm':'United States','Pebble':'United States','Pine64':'Hong Kong','Poco':'China','Polar':'Finland','Porsche Design':'Germany','Samsung':'South Korea','Seiko':'Japan','Siemens':'Germany','Snap':'United States','Sony':'Japan','Suunto':'Finland','T-Mobile':'United States','TAG Heuer':'Switzerland','Tennelec':'United States','Thuraya':'United Arab Emirates','Tile':'United States','Timex':'United States','TomTom':'Netherlands','Ulefone':'China','Ultrahuman':'India','Uniden':'Japan','Unihertz':'China','Vertu':'Hong Kong','Western Electric':'United States','Whoop':'United States','Withings':'France','Xiaomi':'China','ZTE':'China','iQOO':'China','iriver':'South Korea','reMarkable':'Norway','Fairphone':'Netherlands','Bookeen':'France','Doro':'Sweden','Icom':'Japan','Iridium':'United States','Kenwood':'Japan','Magellan':'United States','Handspring':'United States','ACR Electronics':'United States','DeWALT':'United States','Cat':'United States','Drake':'United States','Compaq':'United States','Collins Radio':'United States','Bell System':'United States','Sony Ericsson':'Sweden'}
own={'Apple':('Apple Inc.',''),'Casio':('Casio Computer Co., Ltd.',''),'Asus':('Asustek Computer Inc.',''),'ASUS':('Asustek Computer Inc.',''),'Meta':('Meta Platforms, Inc.',''),'Microsoft':('Microsoft Corporation',''),'Nokia':('Nokia Corporation',''),'OnePlus':('Oppo',''),'Poco':('Xiaomi',''),'iQOO':('Vivo',''),'Kenwood':('JVCKenwood',''),'iriver':('Dreamus',''),'TAG Heuer':('LVMH','1999'),'T-Mobile':('Deutsche Telekom',''),'Timex':('Timex Group B.V.','2008'),'Western Electric':('AT&T Corporation',''),'Realistic':('RadioShack',''),'Fitbit':('Google',''),'Amazfit':('Zepp Health',''),'Honor':('',''),'Sony Ericsson':('Sony','2012')}
glob={'Apple','Samsung','Xiaomi','Poco','vivo','iQOO','Oppo','OnePlus','Huawei','Lenovo','Motorola'}
ind={'Garmin','Casio','Fujitsu','Kyocera','NEC','Asus','ASUS','HTC','Elecraft','Fairphone','TomTom','Polar','Seiko','Snap','Bookeen','Alinco','ACR Electronics','Doro','Midland','Withings','Suunto','Oura'}
n=0
def tag(o,mk):
  global n
  if mk in cty: o['cty']=cty[mk]
  if mk in own and own[mk][0]:
    o['own']=own[mk][0]
    if own[mk][1]: o['own_y']=own[mk][1]
  if mk in glob: o['tier']='Global group'
  elif mk in ind: o['tier']='Independent'
  if mk in cty or mk in own: n+=1
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      for e in k.get('x',[]):
        if e.get('mk'): tag(e,e['mk'])
print(n)
json.dump(d,open('rebuild/work/GAP_D2/D2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('rebuild/work/GAP_D2/D2.tmp',P)
