import json,os,copy
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'D2.json')); B=json.load(open(R+'D2_brands.json'))
W='https://en.wikipedia.org/wiki/'
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return dp,s,k
def V(n,mk,y='',dd=None):
    v={'n':n,'mk':mk,'y':y}
    if dd: v['d']=dd
    return v
def A(n,d_,mk,y,s,v,dt=None,a=''):
    x={'n':n,'a':a,'d':d_,'mk':mk,'y':y,'s':s,'v':v}
    if dt: x['dt']=dt
    return x
def arch(k,n):
    for x in k['x']:
        if x['n']==n: return x
def olddesc(k,n):
    return {v['n']:v.get('d') for v in arch(k,n)['v']}
# D2-1 generations
_,_,k=find('Touchscreen smartphone')
ip=arch(k,'iPhone'); od=olddesc(k,'iPhone')
L=[('iPhone (1st generation)','2007'),('iPhone 3G','2008'),('iPhone 3GS','2009'),('iPhone 4','2010'),('iPhone 4s','2011'),('iPhone 5','2012'),('iPhone 5c / 5s','2013'),('iPhone 6 / 6 Plus','2014'),('iPhone 6s / 6s Plus','2015'),('iPhone SE (1st generation)','2016'),('iPhone 7 / 7 Plus','2016'),('iPhone 8 / 8 Plus','2017'),('iPhone X','2017'),('iPhone XS / XS Max','2018'),('iPhone XR','2018'),('iPhone 11 / 11 Pro / 11 Pro Max','2019'),('iPhone SE (2nd generation)','2020'),('iPhone 12 / 12 mini / 12 Pro / 12 Pro Max','2020'),('iPhone 13 / 13 mini / 13 Pro / 13 Pro Max','2021'),('iPhone SE (3rd generation)','2022'),('iPhone 14 / 14 Plus / 14 Pro / 14 Pro Max','2022'),('iPhone 15 / 15 Plus / 15 Pro / 15 Pro Max','2023'),('iPhone 16 / 16 Plus / 16 Pro / 16 Pro Max','2024'),('iPhone 16e','2025'),('iPhone 17','2025'),('iPhone Air','2025'),('iPhone 17 Pro / 17 Pro Max','2025'),('iPhone 17e','2026'),('iPhone 18 Pro / 18 Pro Max','2026')]
notes={'iPhone (1st generation)':'original','iPhone X':'first full-screen model without home button'}
ip['v']=[V(n,'Apple',y,notes.get(n)) for n,y in L]
gs=arch(k,'Galaxy S')
G=[('Galaxy S','2010','original'),('Galaxy S II','2011'),('Galaxy S III','2012'),('Galaxy S4','2013'),('Galaxy S5','2014'),('Galaxy S6','2015'),('Galaxy S7','2016'),('Galaxy S8','2017'),('Galaxy S9','2018'),('Galaxy S10','2019'),('Galaxy S20','2020'),('Galaxy S21','2021'),('Galaxy S22','2022','Ultra gains the S Pen'),('Galaxy S23','2023'),('Galaxy S24','2024'),('Galaxy S25','2025'),('Galaxy S26 / S26+ / S26 Ultra','2026')]
gs['v']=[V(g[0],'Samsung',g[1],g[2] if len(g)>2 else None) for g in G]
px=arch(k,'Pixel')
P=[('Pixel / Pixel XL','2016','original'),('Pixel 2','2017'),('Pixel 3','2018'),('Pixel 3a','2019','first budget a-model'),('Pixel 4','2019'),('Pixel 4a','2020'),('Pixel 5','2020'),('Pixel 5a','2021'),('Pixel 6 / 6 Pro','2021'),('Pixel 6a','2022'),('Pixel 7','2022'),('Pixel 7a','2023'),('Pixel Fold','2023'),('Pixel 8 / 8 Pro','2023'),('Pixel 8a','2024'),('Pixel 9 / 9 Pro / 9 Pro XL','2024'),('Pixel 9 Pro Fold','2024'),('Pixel 9a','2025'),('Pixel 10 / 10 Pro / 10 Pro XL','2025'),('Pixel 10 Pro Fold','2025'),('Pixel 10a','2026'),('Pixel 11 / 11 Pro / 11 Pro XL','2026'),('Pixel 11 Pro Fold','2026')]
px['v']=[V(p[0],'Google',p[1],p[2] if len(p)>2 else None) for p in P]
# Lumia
k['x'].append(A('Lumia','Nokia and Microsoft Windows Phone line known for bright colours and PureView cameras.','Nokia','2011',W+'Nokia_Lumia_series',
 [V('Lumia 800 / 710','Nokia','2011','first Lumia, Windows Phone 7.5'),V('Lumia 900','Nokia','2012','LTE flagship for AT&T'),V('Lumia 920','Nokia','2012','PureView, wireless charging'),V('Lumia 520','Nokia','2013','best-selling Windows Phone'),V('Lumia 1020','Nokia','2013','41-megapixel camera'),V('Lumia 1520','Nokia','2013','first large Lumia'),V('Lumia 950','Microsoft','2015','first Windows 10 Mobile flagship'),V('Lumia 650','Microsoft','2016','last Lumia')],'colours · Windows Phone version'))
# keyboard smartphones
_,_,kb=find('Keyboard smartphone')
kb['x']+= [
 A('Nokia N900','Nokia\'s Maemo Linux phone with a three-row slide-out keyboard and resistive touchscreen.','Nokia','2009',W+'Nokia_N900',[V('Nokia N900','Nokia','2009','original; follows the N810 internet tablet')]),
 A('Palm Pre','Palm\'s first webOS phone with a slide-out keyboard and multi-touch screen.','Palm','2009',W+'Palm_Pre',[V('Palm Pre','Palm','2009','original, Sprint'),V('Pre Plus','Palm','2010','double the memory'),V('Pre 2','HP','2010','webOS 2.0'),V('Pre 3','HP','2011')]),
 A('HTC Dream','The first commercial Android phone, with a slide-out keyboard and trackball; sold as the T-Mobile G1.','HTC','2008',W+'HTC_Dream',[V('T-Mobile G1','HTC','2008','US version'),V('Android Dev Phone 1','HTC','2008','unlocked developer version')],a='T-Mobile G1')]
# keypad phones
_,_,kp=find('Keypad phone')
n51=arch(kp,'Nokia 5110'); n51['a']='5110'; n51['v']=[v for v in n51['v'] if v['n']!='Nokia 6110']
n51['d']='Consumer GSM bar phone that introduced Xpress-on covers and Snake.'
kp['x'].insert(2,A('Nokia 6110','First of Nokia\'s business 6xxx series: first GSM phone with an ARM processor and Nokia\'s first with infrared.','Nokia','1998',W+'Nokia_6110',[V('Nokia 6110','Nokia','1998','original'),V('Nokia 6130','Nokia','','GSM 1800 variant'),V('Nokia 6150','Nokia','','dual-band successor'),V('Nokia 6190','Nokia','','North American, no infrared')]))
kp['x'].insert(3,A('Nokia 8210','Featherweight Nokia bar phone with no external antenna, sold on its Xpress-on covers.','Nokia','1999',W+'Nokia_8210',[V('Nokia 8210','Nokia','1999','original'),V('Nokia 8250','Nokia','2001','Asia-Pacific, blue backlight'),V('Nokia 8290','Nokia','','North American GSM 1900'),V('Nokia 8260','Nokia','','North American TDMA/AMPS')]))
kp['x'].append(A('Sony Ericsson T68i','Compact bar phone, Ericsson\'s first with a colour screen, with Bluetooth and GPRS.','Sony Ericsson','2001',W+'Sony_Ericsson_T68i',[V('T68','Sony Ericsson','2001','original'),V('T68i','Sony Ericsson','2002','adds email client and MMS'),V('T68m','Sony Ericsson'),V('T68ie','Sony Ericsson'),V('T68a','Sony Ericsson')]))
kp['m']=[m for m in kp['m'] if m[0]!='Siemens S25']+[m for m in kp['m'] if m[0]=='Siemens S25']
# slider
_,_,sl=find('Slider phone')
a8=arch(sl,'Nokia 8110'); a8['v']=[v for v in a8['v'] if v['n'] not in('Nokia 8810','Nokia 7110')]
sl['x'].insert(1,A('Nokia 7110','Slider with a spring-loaded cover, Navi-roller and T9; the first phone with a WAP browser.','Nokia','1999',W+'Nokia_7110',[V('Nokia 7110','Nokia','1999','original, GSM 900/1800'),V('Nokia 7160','Nokia','','TDMA/AMPS'),V('Nokia 7190','Nokia','','American GSM 1900')]))
sl['x'].insert(2,A('Nokia 8810','Chrome-bodied slider among the first mainstream phones with an internal antenna.','Nokia','1998',W+'Nokia_8810',[V('Nokia 8810','Nokia','1998','original')]))
# smartwatch
_,_,sw=find('Smartwatch')
sw['x']+= [
 A('Moto 360','Motorola\'s round Android Wear smartwatch with a steel case.','Motorola','2014',W+'Moto_360_(1st_generation)',[V('Moto 360 (1st generation)','Motorola','2014','original'),V('Moto 360 (2nd generation)','Motorola','2015'),V('Moto 360 (3rd generation)','Motorola','2019','built under licence by eBuyNow')]),
 A('Sony SmartWatch','Sony\'s Android companion watch line, from silicone band to Android Wear.','Sony','2012',W+'Sony_SmartWatch',[V('SmartWatch','Sony','2012','original'),V('SmartWatch 2','Sony','2013'),V('SmartWatch 3','Sony','2014','Android Wear, GPS')]),
 A('Microsoft SPOT watch','Early smartwatch that received data over FM sub-carrier broadcasts (MSN Direct); service ended in 2012.','Microsoft','2004',W+'Microsoft_SPOT',[V('Fossil SPOT watch','Fossil','2004','first SPOT watches, with Suunto'),V('Suunto SPOT watch','Suunto','2004'),V('Tissot SPOT watch','','','first touchscreen SPOT watch'),V('Swatch SPOT watch','','','aimed at younger buyers')],a='MSN Direct watch')]
# luxury
_,_,lx=find('Luxury phone')
lx['x']+= [
 A('TAG Heuer Meridiist','Luxury feature phone in steel, rose gold or python skin, with a GMT function and dual SIM.','TAG Heuer','','https://www.hautetime.com/tag-heuer-unveils-meridiist-smartphone/',[V('Meridiist','TAG Heuer','','original')],'diamond-set · python skin · rose gold · steel'),
 A("Porsche Design P'9981",'BlackBerry Bold 9900 in a stainless steel frame with leather back, made with Porsche Design.','Porsche Design','2011',W+'BlackBerry_Porsche_Design_P%279981',[V("P'9981",'Porsche Design','2011','original'),V("P'9982",'Porsche Design','','successor'),V("P'9983",'Porsche Design')]),
 A('Mobiado Professional 105GMT','Mobiado luxury phone with two mechanical watch movements in a gold-plated or gun-metal case.','Mobiado','2008','https://www.ablogtowatch.com/general/hideous-melding-of-mobile-phone-mechanical-watches-and-painful-design-the-mobiado-professional-105gmt-gold-discovery-phone/',[V('Professional 105GMT','Mobiado','2008','gold-plated and gun-metal versions')])]
# smart glasses: XREAL lives in E5
_,_,sg=find('Smart glasses')
sg['x']=[x for x in sg['x'] if x['n']!='XREAL Air']
sg['d']=sg['d'].rstrip('.')+'; screen-style display glasses such as XREAL are in VR & XR.'
# ham
_,hs,_=find('Linear amplifier')
_,_,la=find('Linear amplifier')
la['x']=[A('Heathkit SB-200','Grounded-grid HF amplifier kit with two 572B tubes for 80–10 m; among the most popular amateur amplifiers.','Heathkit','1964','https://radiomuseum.org/r/heath_sb_200.html',[V('SB-200','Heathkit','1964','about 600 W output; made to 1978')]),
 A('Ameritron AL-811','Four-tube HF amplifier of 800 W PEP, 160–15 m.','Ameritron','','https://www.gigaparts.com/al-811hd-hf-amplifier-800w-572b-tubes-x4-us-120vac.html',[V('AL-811H','Ameritron'),V('AL-811HD','Ameritron','','four 572B tubes, tougher tank circuit')])]
la['m']=[m for m in la['m']]
_,_,an=find('Amateur antenna')
an['x']=[A('Half-wave dipole','Centre-fed wire antenna just under half a wavelength long; the reference amateur antenna.','','',W+'Dipole_antenna',[],'band · wire or rod · flat-top, inverted-V or sloper'),
 A('Yagi–Uda beam','Directional antenna with a driven element, reflector and directors, mounted on a rotator.','','1926',W+'Yagi%E2%80%93Uda_antenna',[],'elements · bands · trapped multiband',a='Yagi'),
 A('G5RV','Multiband dipole fed by a ladder-line section; designed by Louis Varney.','','1946',W+'G5RV_antenna',[V('G5RV (full size, 102 ft)','','1946'),V('ZS6BKW','','','variant matching more bands without a tuner'),V('W0BTU','','','variant')],'length · feeder 300 or 450 ohm')]
for x in an['x']: x.pop('v') if not x['v'] else None
# new kinds in ham shelf
_,hsh,_=find('HF base transceiver')
ks=hsh['k']
ks.insert(ks.index(find('Morse key')[2]),{'n':'Communications receiver','a':'shortwave receiver · general-coverage receiver','d':'Receive-only radio covering the shortwave bands, from wartime valve sets to military surplus.','s':W+'Hallicrafters_SX-28','x':[
 A('Hallicrafters SX-28','Art deco shortwave receiver, 550 kHz–43 MHz in six bands, used by amateurs, governments and the military.','Hallicrafters','1940',W+'Hallicrafters_SX-28',[V('SX-28 (Super Skyrider)','Hallicrafters','1940','original'),V('SX-28A','Hallicrafters','1944','Navy AN/GRR-2 version')]),
 A('Collins R-390A','Military general-coverage HF receiver, 0.5–32 MHz, 23 valves; built by several makers.','Collins Radio','1955',W+'R-390A',[V('R-390A (Collins-built)','Collins Radio','1955'),V('R-390A (Electronic Assistance Corp)','','','largest maker by output'),V('R-390A (Motorola)','Motorola'),V('R-390A (Fowler Industries)','','1984','small restart run')],'maker · cabinet and finish')]})
ks.insert(ks.index(find('Morse key')[2]),{'n':'Antenna analyser & SWR meter','a':'VNA · vector network analyser','d':'Handheld instrument that measures an antenna\'s SWR and impedance across a band.','t':['SWR meter','antenna analyser','vector network analyser'],'s':'https://nanovna.com/','x':[
 A('NanoVNA','Low-cost handheld vector network analyser designed by edy555, widely used as an antenna analyser.','','','https://nanovna.com/',[V('NanoVNA (edy555)','','','original, 50 kHz–300 MHz'),V('NanoVNA-H','','','Hugen improvements, to 900 MHz'),V('NanoVNA-H4','','','about 40 dB dynamic range to 1.5 GHz')],'version · screen size · frequency range')]})
# translators merge
dp,sh,t1=find('Pocket translator'); _,_,t2=find('Electronic dictionary'); _,_,t3=find('Translator earbuds')
t1['n']='Translator & electronic dictionary'; t1['a']='pocket translator · translator earbuds · electronic dictionary'
t1['d']='Handheld device or earbuds that translate speech or text, or hold dictionaries for look-up; ordinary earbuds with a translate feature are in Audio & Video.'
t1['t']=['pocket translator','translator earbuds','electronic dictionary']
t1['m']=t1['m']+t2['m']
sh['k']=[k for k in sh['k'] if k['n'] not in('Electronic dictionary','Translator earbuds')]
# creator add-ons merge
dp,sh,g=find('Phone gimbal'); _,_,ss=find('Selfie stick'); _,_,cl=find('Clip-on phone lens'); _,_,mic=find('Phone microphone')
g['n']='Phone camera & creator add-on'; g['a']='phone gimbal · selfie stick · clip-on lens · phone microphone'
g['d']='Gear that adds stabilising, framing, lens or sound capability to a phone camera; cameras\' own microphones are in Cameras & Photography.'
g['t']=['gimbal','selfie stick','clip-on lens','phone microphone']
g['m']=g['m']+ss['m']+cl['m']
sh['k']=[k for k in sh['k'] if k['n'] not in('Selfie stick','Clip-on phone lens','Phone microphone')]
# charging dock
_,_,cd=find('Charging dock')
cd['m']=[]; cd['r']=[['MagSafe Charger','Apple'],['MagGo','Anker'],['Zolo','Anker'],['BoostCharge','Belkin'],['UltraCharge','Belkin'],['HaloLock','ESR'],['MagFlow','Ugreen'],['Qi2 stands','Satechi'],['HyperJuice','Hyper'],['Wireless charge stands','Mophie'],['W9','elago']]
cd['d']=cd['d'].rstrip('.')+'; wired multi-port chargers are in Computers & Peripherals.'
# satellite shelf
dp,sh,sp=find('Satellite phone')
sh['k']=[k for k in sh['k'] if k['n']!='Satellite phone']
ndp,nsh,_=find('Handheld GPS')
names=['Satellite phone','Satellite messenger','Personal locator beacon','Satellite hotspot']
sat=[sp]+[k for k in nsh['k'] if k['n'] in names]
nsh['k']=[k for k in nsh['k'] if k['n'] not in names]
nsh['n']='GPS & trackers'
ndp['s'].append({'n':'Satellite & safety','k':sat})
# notes
for dn,note in {'Tablets & e-readers':'Tier for tablets; variety for e-readers and e-paper devices.','Wearables':'Tier for fitness bands; variety for smartwatch and smart ring history.','Navigation, trackers & safety beacons':'Tier: market-covering brands plus independent test winners.','Power & charging':'Tier: market-covering brands plus independent test winners.','Cases & accessories':'Tier: market-covering brands, no SKU lists.'}.items():
    for dp in d['depts']:
        if dp['n']==dn: dp['note']=note
# brands
have={b['n'] for b in B['b']}
def Br(n,c,seg,kf,dd,s,sig=None,f=''):
    if n in have: return
    b={'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':dd,'s':s}
    if sig:b['sig']=sig
    B['b'].append(b)
Br('Mobiado','','Artisan & independent','luxury phones','Maker of luxury phones in sapphire, aluminium and precious metals.','https://www.ablogtowatch.com/general/hideous-melding-of-mobile-phone-mechanical-watches-and-painful-design-the-mobiado-professional-105gmt-gold-discovery-phone/',['Mobiado Professional 105GMT'])
Br('TAG Heuer','','Premium','luxury watches','Watch maker that also sold the Meridiist luxury phone.','https://www.hautetime.com/tag-heuer-unveils-meridiist-smartphone/',['TAG Heuer Meridiist'])
Br('Porsche Design','','Premium','design goods','Design house behind the BlackBerry Porsche Design phones.',W+'BlackBerry_Porsche_Design_P%279981',["Porsche Design P'9981"])
Br('Heathkit','United States','Specialist','electronics kits','Maker of ham radio and electronics kits, including the SB-200 amplifier.','https://radiomuseum.org/r/heath_sb_200.html',['Heathkit SB-200'])
Br('Hallicrafters','','Heritage manufactory','shortwave receivers','Maker of amateur and communications receivers such as the SX-28.',W+'Hallicrafters_SX-28',['Hallicrafters SX-28'])
Br('Ameritron','United States','Specialist','ham amplifiers','Maker of HF linear amplifiers such as the AL-811.','https://www.gigaparts.com/al-811hd-hf-amplifier-800w-572b-tubes-x4-us-120vac.html',['Ameritron AL-811'])
Br('Fossil','','Mainstream','fashion watches','Watch maker that built early SPOT smartwatches with Microsoft.',W+'Microsoft_SPOT')
json.dump(d,open(R+'D2.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'D2.json.tmp',R+'D2.json')
json.dump(B,open(R+'D2_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'D2_brands.json.tmp',R+'D2_brands.json')
