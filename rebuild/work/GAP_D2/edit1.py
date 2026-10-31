import json,os,re
P='rebuild/out/D2.json'
d=json.load(open(P))
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
K={}
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']: K[k['n']]=k
def ent(kind,name): 
  for e in K[kind]['x']:
    if e['n']==name: return e
  raise KeyError(name)
log=[]
def addv(kind,name,vs,mk=None):
  e=ent(kind,name); have={norm(v['n']):v for v in e['v']}
  for n,y in vs:
    key=norm(n)
    if key in have:
      if not have[key].get('y') and y: have[key]['y']=y; log.append(f'year {n}')
      continue
    v={'n':n,'y':y}
    if mk: v['mk']=mk
    e['v'].append(v); have[key]=v; log.append(f'+v {name}: {n}')
def adde(kind,e):
  if norm(e['n']) in {norm(x['n']) for x in K[kind]['x']}: return
  e.setdefault('a','');e.setdefault('v',[]);K[kind]['x'].append(e); log.append(f'+e {kind}: {e["n"]}')
W='https://en.wikipedia.org/wiki/'
# Kobo
addv('E-reader','Kobo eReader',[('Kobo Wi-Fi','2010'),('Kobo Touch','2011'),('Kobo Glo','2012'),('Kobo Mini','2012'),('Kobo Aura HD','2013'),('Kobo Aura','2013'),('Kobo Aura H2O','2014'),('Kobo Glo HD','2015'),('Kobo Touch 2.0','2015'),('Kobo Aura One','2016'),('Kobo Aura Edition 2','2016'),('Kobo Aura H2O Edition 2','2017'),('Forma','2018'),('Nia','2020'),('Clara BW','2024')])
e=ent('E-reader','Kobo eReader'); e['s']=W+'Kobo_eReader'
addv('E-paper writing tablet','Kobo Elipsa',[('Elipsa 2E','2023')])
# Razr
addv('Flip foldable phone','Motorola razr (foldable)',[('Motorola Razr (2022)','2022'),('Motorola Razr 40','2023'),('Motorola Razr 40 Ultra','2023'),('Motorola Razr 50','2024'),('Motorola Razr 50 Ultra','2024'),('Motorola Razr 60','2025'),('Motorola Razr 60 Plus','2025'),('Motorola Razr 60 Ultra','2025'),('Motorola Razr 70','2026'),('Motorola Razr 70 Plus','2026'),('Motorola Razr 70 Ultra','2026')])
addv('Flip phone','RAZR V3',[('RAZR V3xx','2006'),('RAZR2 (V8, V9, V9m, V9x)','2007')])
# Fitbit
addv('Fitness band','Fitbit models',[('Tracker','2009'),('Ultra','2011'),('Flex','2013'),('One','2012'),('Zip','2012'),('Force','2013'),('Surge','2015'),('Blaze','2016'),('Alta','2016'),('Flex 2','2016'),('Alta HR','2017'),('Ace','2018'),('Ace 2','2019'),('Inspire 2','2020'),('Luxe','2021'),('Ace 3','2021'),('Ace LTE','2024')])
ent('Fitness band','Fitbit models')['s']=W+'List_of_Fitbit_products'
addv('Fitness band','Fitbit Charge',[('Charge 4','2020'),('Charge 5','2021')])
# Forerunner / fenix
fr=[('101','2003'),('201','2003'),('301','2005'),('205','2006'),('305','2006'),('50','2007'),('405','2008'),('60','2009'),('405CX','2009'),('310XT','2009'),('110','2010'),('210','2010'),('410','2010'),('610','2011'),('910XT','2011'),('10','2012'),('220','2013'),('620','2013'),('15','2014'),('920XT','2014'),('225','2015'),('25','2015'),('230','2015'),('235','2015'),('630','2015'),('735XT','2016'),('35','2016'),('935','2017'),('30','2017'),('645','2018'),('645 Music','2018'),('45','2019'),('45S','2019'),('245','2019'),('245 Music','2019'),('945','2019'),('745','2020'),('55','2021'),('945 LTE','2021'),('255','2022'),('255 Music','2022'),('955','2022'),('955 Solar','2022'),('265','2023'),('965','2023'),('158','2023'),('165','2024'),('570','2025'),('970','2025'),('70','2026'),('170','2026')]
addv('Multisport GPS watch','Forerunner',[('Forerunner '+n,y) for n,y in fr])
ent('Multisport GPS watch','Forerunner')['s']=W+'Garmin_Forerunner'
addv('Multisport GPS watch','fēnix',[('fēnix 3 HR','2016'),('fēnix 5 Plus','2018'),('fēnix 6 Solar','2020'),('fēnix 7 Pro','2023')])
ent('Multisport GPS watch','fēnix')['s']=W+'Garmin_Fenix'
# BlackBerry
bb='https://en.wikipedia.org/wiki/List_of_BlackBerry_products'
for n,y,v in [('BlackBerry Pearl','2006',[('Pearl 8100','2006')]),('BlackBerry Classic','2014',[('Classic','2014'),('Q5','2013'),('Z30','2013')])]:
  adde('Keyboard smartphone',{'n':n,'d':'BlackBerry phone line.' if 0 else ('BlackBerry\'s compact keyboard handset with a trackball.' if 'Pearl' in n else 'BlackBerry\'s 2014 return to the classic keyboard layout.'),'mk':'BlackBerry','y':y,'s':bb,'v':[{'n':a,'y':b} for a,b in v],'g':'BlackBerry'})
adde('Touchscreen smartphone',{'n':'BlackBerry Storm and Z10','d':'BlackBerry touchscreen phones, from the 2008 Storm to the BlackBerry 10 Z10.','mk':'BlackBerry','y':'2008','s':bb,'v':[{'n':'Storm 9500','y':'2008'},{'n':'Z10','y':'2013'},{'n':'Leap','y':'2015'}],'g':'BlackBerry'})
adde('Touchscreen smartphone',{'n':'BlackBerry Android phones','d':'BlackBerry\'s Android-based handsets, starting with the Priv slider.','mk':'BlackBerry','y':'2015','s':bb,'v':[{'n':'Priv','y':'2015'},{'n':'DTEK50 / DTEK60','y':'2016'},{'n':'Motion','y':'2017'}],'g':'BlackBerry'})
addv('Keyboard smartphone','BlackBerry Curve',[('Curve 8300','2007')])
# Surface, Fire
addv('Tablet','Microsoft Surface',[('Surface RT','2012'),('Surface Pro','2013'),('Surface Go','2018')])
ent('Tablet','Microsoft Surface')['s']=W+'Microsoft_Surface'
addv('Tablet','Amazon Fire',[('Fire HD (4th generation)','2014'),('Fire HDX (4th generation)','2014'),('Fire 7 (7th generation)','2017'),('Fire HD 8+','2020'),('Fire HD 10+','2021'),('Fire 7 (12th generation)','2022'),('Fire HD 8 (2024)','2024')])
ent('Tablet','Amazon Fire')['s']=W+'Amazon_Fire_tablet'
# Android Wear
adde('Smartwatch',{'n':'LG G Watch','d':'Early Android Wear smartwatch; the G Watch and G Watch R launched in 2014.','mk':'LG','y':'2014','s':W+'Wear_OS','v':[{'n':'G Watch','y':'2014'},{'n':'G Watch R','y':'2014'},{'n':'Watch Urbane','y':''}],'g':'LG'})
adde('Smartwatch',{'n':'Asus ZenWatch','d':'Android Wear smartwatch from Asus, launched in 2014.','mk':'Asus','y':'2014','s':W+'Wear_OS','v':[],'g':'Asus'})
addv('Smartwatch','Galaxy Watch',[('Gear Live','2014'),('Gear 2',''),('Gear Fit',''),('Gear S',''),('Gear Sport',''),('Galaxy Watch Ultra 2','')])
ent('Smartwatch','Galaxy Watch')['s']=W+'Samsung_Galaxy_Watch'
# Nokia
addv('Keypad phone','Nokia three-digit feature phones',[('Nokia 225','2014'),('Nokia 225 4G (2020)','2020'),('Nokia 225 4G (2024)','2024'),('Nokia 230','2015'),('Nokia 230 (2024)','2024'),('Nokia 235 4G','2024'),('Nokia 301','2013'),('Nokia 515','2013')])
addv('Keypad phone','Nokia N-Gage and other phones',[('N-Gage','2003'),('N-Gage QD','2004')])
json.dump(d,open('rebuild/work/GAP_D2/D2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('rebuild/work/GAP_D2/D2.tmp','rebuild/out/D2.json')
print(len(log)); print('\n'.join(log[:15]),'...')
