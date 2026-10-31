import json,os,re,copy
SRC='/home/user/Possession-Taxonomy/rebuild/work/GAP_D1/bak/D1.json'
BR='/home/user/Possession-Taxonomy/rebuild/work/GAP_D1/bak/D1_brands.json'
OUT='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(SRC)); br=json.load(open(BR))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k
def ent(k,n):
  for e in k['x']:
    if e['n']==n: return e
def add(k,e):
  if any(x['n'].lower()==e['n'].lower() for x in k['x']): return
  k['x'].append(e)
def addv(e,v):
  if any(x['n'].lower()==v['n'].lower() for x in e.setdefault('v',[])): return
  e['v'].append(v)
def setv(e,n,y):
  for v in e['v']:
    if v['n']==n and not v.get('y'): v['y']=y
HC='https://en.wikipedia.org/wiki/List_of_home_computers'
def hobby(n,mk=''):
  return {"n":n,"a":"","d":"Hobby, kit or trainer computer named on Wikipedia's List of home computers.","mk":mk,"y":"","s":HC,"v":[]}
NOREF="No complete list exists; follows the maker and Wikipedia articles cited on each entry."
# ---- sel rewrites
for n,k in K.items():
  if k.get('x'):
    sel=k.get('sel','')
    if 'No whole-space reference exists; ' in sel and 'entries keep the structure pass sources' in sel or sel.startswith('No whole-space reference exists; the entry keeps'):
      k['sel']=NOREF
# ---- Laptop
K['Laptop']['sel']="No complete list exists; follows Wikipedia's List of laptop brands and manufacturers for the makers (it lists brands, not models) and each maker's own article for its lines."
# ---- Processor
pc=K['Processor']
e=ent(pc,'Bobcat, Jaguar and Puma'); e['y']='2011'; setv(e,'Bobcat','2011'); setv(e,'Jaguar','2013'); setv(e,'Puma','2014')
e['s']='https://en.wikipedia.org/wiki/Bobcat_(microarchitecture)'
ent(pc,'Zen 6')['y']='2026'; ent(pc,'Zen 6')['d']='Sixth Zen generation on 3 nm; EPYC "Venice" was announced in July 2026 and desktop parts are expected in 2027.'
e=ent(pc,'Bulldozer (FX)'); 
for v in e['v']:
  if v['n']=='FX (Zambezi)': v['y']='2011'
e=ent(pc,'AMD K6'); setv(e,'K6-2','1998')
e=ent(pc,'Phenom (K10)'); setv(e,'Phenom II','2008')
IL='https://en.wikipedia.org/wiki/List_of_Intel_CPU_microarchitectures'
add(pc,{"n":"Westmere","a":"","d":"32 nm shrink of Nehalem, the first Core i3 and Clarkdale desktop parts.","mk":"Intel","y":"2010","s":IL,"v":[],"g":"Intel"})
add(pc,{"n":"Nova Lake","a":"","d":"Intel's 2026 desktop generation named on the microarchitecture list.","mk":"Intel","y":"2026","s":IL,"v":[],"g":"Intel"})
at=ent(pc,'Intel Atom')
for n,y in [('Saltwell','2011'),('Airmont','2015'),('Goldmont Plus','2017'),('Darkmont','2026')]: addv(at,{"n":n,"mk":"Intel","y":y,"d":""})
# order: Intel by year then AMD
def key(e):
  g={'Intel':0,'AMD':1}.get(e.get('g'),2); y=re.match(r'\d{4}',e.get('y') or '')
  return (g,int(y.group()) if y else 9999)
pc['x'].sort(key=key)
pc['sel']=pc['sel']+" Covers 70 of about 74 rows in List of Intel CPU microarchitectures (read to 100,000 of 118,738 characters) and List of AMD CPU microarchitectures (25 rows, no years stated, years from the Bobcat, Jaguar, Bulldozer, K6-2 and Phenom II articles); the performance-core codenames (Sunny Cove, Golden Cove, Lion Cove and the like) are named inside the generation they power, K9 never shipped, and Cougar Cove onward and the unread page end are future designs."
# ---- GPU
g=K['Graphics card']; tu=ent(g,'Turing (GeForce RTX 20 and GTX 16)')
addv(tu,{"n":"GeForce GTX 1660 Ti","mk":"Nvidia","y":"2019","d":"Launched Feb 22, 2019."})
addv(tu,{"n":"GeForce GTX 1660 Super","mk":"Nvidia","y":"2019","d":"Launched Oct 29, 2019."})
for e in g['x']:
  if e['n'].startswith('Tesla (GeForce 8'):
    addv(e,{"n":"GeForce 9500 GT","mk":"Nvidia","y":"2008","d":"Launched July 29, 2008."})
    addv(e,{"n":"GeForce 9400 GT","mk":"Nvidia","y":"2008","d":"Launched Aug 27, 2008."})
g['sel']=re.sub(r"Covers 228 .*$","Complete: 27 of 27 consumer architecture generations named in Wikipedia's Nvidia, AMD and Intel Arc articles. The cards are versions: about 230 GeForce and Titan desktop models from the Nvidia GPU list and the GeForce 20, 30, 40 and 50 series articles; the dated gaps (GeForce 9400 and 9500 GT, GTX 1660 Super and Ti) are now filled, and rebrand, workstation, data-centre and mobile rows are out of scope.",g['sel'],flags=re.S)
# ---- Home computer
hc=K['Home computer']
bm=ent(hc,'BBC Micro'); addv(bm,{"n":"BBC Master","y":"1986","d":"Successor with 128 KB of memory."})
sch=[("Commodore SuperPET / SP9000","Commodore"),("Compis","Telenova"),("IQ 151","ZPA Nový Bor"),("LINK 480Z","Link Electronics"),("Regency Systems R2C",""),("Research Machines 380Z","Research Machines"),("Tiki 100","Tiki Data"),("TIM-011",""),("Unisys ICON","Unisys")]
for n,mk in sch:
  mk=''  # makers not stated by the page
  add(hc,{"n":n,"a":"","d":"School computer named on Wikipedia's List of home computers.","mk":mk,"y":"","s":HC,"v":[],"g":"School computers (no year given)"})
hc['sel']=hc['sel']+" Complete: 146 of 146 named machines in the page's main table (the row 'Various models' names none), plus 9 more of the 12 school computers (the other three, Acorn Archimedes, BBC Micro and Aster CT-80, are already entries). Hobby, kit and trainer rows are in Trainer & single-board kit (vintage); the five cardboard and relay demonstrators (Digi-Comp, Geniac, Minivac 601, CARDboard Illustrative Aid) are teaching toys, out of scope."
# ---- Vintage desktop
K['Vintage desktop computer']['sel']="No complete list exists; follows Wikipedia's List of home computers (its hobby and kit rows, such as the Altair 8800, are kept here or in Trainer & single-board kit) and the Apple Lisa article."
# ---- Trainer kit
tk=K['Trainer & single-board kit (vintage)']
for n,mk in [("Applix 1616",""),("Compukit UK101",""),("Dick Smith Super-80",""),("Educ-8",""),("Elektor Junior Computer","Elektor"),("Elektor TV Games Computer","Elektor"),("Ferguson Big Board",""),("Galaksija",""),("Heathkit H8","Heathkit"),("Heathkit H11","Heathkit"),("Heath ET-100 8088 trainer","Heath Company"),("Kenbak-1",""),("LNW-80",""),("MK14",""),("Mark-8",""),("Nascom 1 and Nascom 2",""),("Newbear 77-68",""),("Powertran Cortex",""),("Processor Technology SOL-20",""),("PSI Comp 80",""),("SCELBI",""),("Tangerine Microtan 65",""),("TEC-1","")]:
  add(tk,hobby(n,mk))
EO='https://en.wikipedia.org/wiki/Single-board_computer'
for n,y,mk in [("Intel SIM4-01","1971","Intel"),("Intel SIM8-01","1972","Intel"),("MYCRO-1","1974",""),("Intel SDK-80","1975","Intel"),("Motorola MEK6800D1","1975","Motorola")]:
  add(tk,{"n":n,"a":"","d":"Early single-board computer named in Wikipedia's Single-board computer article.","mk":mk,"y":y,"s":EO,"v":[]})
tk['sel']="Follows the hobby, kit and trainer rows of Wikipedia's List of home computers and the early single-board computers named in its Single-board computer article. Complete: 23 of 23 hobby and kit rows not already entries elsewhere (the Altair 8800, Apple I, KIM-1, Micro-Professor MPF-I and Z1013 are held in other kinds, ZX80 kit is a version of the ZX80) and 5 of 6 early boards (KIM-1 already here). The page gives no years for hobby rows."
# ---- SBC
sb=K['Single-board computer']
for n,mk in [("NanoPi",""),("ASUS Tinker Board","Asus"),("Cubieboard",""),("Intel Galileo","Intel"),("Intel Edison","Intel"),("Gumstix",""),("OLinuXino",""),("PandaBoard",""),("Parallella",""),("CHIP",""),("Arndale Board",""),("Cotton Candy",""),("Hawkboard",""),("IGEPv2",""),("Rascal",""),("Snowball",""),("Ampro Little Board","Ampro")]:
  add(sb,{"n":n,"a":"","d":"Single-board computer family named in Wikipedia's Single-board computer article.","mk":mk,"y":"","s":EO,"v":[]})
for e in sb['x']: e['g']='Raspberry Pi' if e['n'].startswith('Raspberry Pi') else 'Other makers'
sb['x'].sort(key=lambda e:(e['g']!='Raspberry Pi',))
sb['xg']='by maker'
sb['sel']="Follows the families named in Wikipedia's Single-board computer article. Complete: 27 of 27 named families (25 here, Arduino is under Microcontroller board, Nvidia Drive is an automotive platform and out of scope); years are blank where the article gives none."
# ---- Microcontroller
mc=K['Microcontroller board']; AL='https://en.wikipedia.org/wiki/List_of_Arduino_boards_and_compatible_systems'
def ard(n,y,d,mk='Arduino',v=None): add(mc,{"n":n,"a":"","d":d,"mk":mk,"y":y,"s":AL,"v":v or []})
ent(mc,'Arduino Mega')['y']='2009'; ent(mc,'Arduino Nano')['y']='2008'
ard("Arduino Leonardo","2012","Board whose chip handles USB itself, so it can act as a keyboard or mouse.")
ard("Arduino Due","2012","First Arduino with a 32-bit ARM chip.")
ard("Arduino Zero","2015","32-bit ARM board in the Uno form factor.")
ard("Arduino MKR","2016","Small 32-bit boards with wireless or other radios.",v=[{"n":"Arduino MKR1000","mk":"Arduino","y":"2016","d":""},{"n":"Arduino MKR WiFi 1010","mk":"Arduino","y":"2018","d":""}])
ard("Arduino Portenta","2023","Industrial-grade Arduino boards.",v=[{"n":"Arduino Portenta X8","mk":"Arduino","y":"2023","d":""}])
ard("Arduino Micro","2012","Small USB-capable board, co-designed by Adafruit.")
ard("Arduino Pro Mini","2008","Minimal board for permanent installation, made by SparkFun.","SparkFun Electronics")
ard("Arduino Pro","2008","Board for semi-permanent installation.")
ard("Arduino Mega ADK","2011","Mega with a USB host for Android devices.")
ard("Arduino Ethernet","2011","Board with a built-in Ethernet port.")
ard("Arduino Fio","2010","Board with a wireless socket and battery charger.")
ard("Arduino Yún","2013","Board that adds a Linux side and Wi-Fi.")
ard("Arduino 101","2015","Board with Intel Curie, a Bluetooth chip and a motion sensor.")
ard("Arduino Esplora","2012","Gamepad-style board with built-in sensors.")
ard("LilyPad Arduino","2007","Sewable board for wearable projects.")
ard("Early Arduino boards","2005","Superseded boards: Serial Arduino 2005, NG, BT 2007, Diecimila 2007, Duemilanove 2008, Mini 2008.",v=[{"n":"Serial Arduino","mk":"Arduino","y":"2005","d":""},{"n":"Arduino NG","mk":"Arduino","y":"","d":""},{"n":"Arduino BT","mk":"Arduino","y":"2007","d":""},{"n":"Arduino Diecimila","mk":"Arduino","y":"2007","d":""},{"n":"Arduino Duemilanove","mk":"Arduino","y":"2008","d":""},{"n":"Arduino Mini","mk":"Arduino","y":"2008","d":""}])
add(mc,{"n":"STM32 Nucleo","a":"Nucleo boards · Blue Pill","d":"ST's development boards with Arduino-style headers; the Blue Pill is a cheap STM32 clone board.","mk":"STMicroelectronics","y":"","s":AL,"v":[]})
for e in mc['x']: e['g']='Arduino' if e['n'].startswith(('Arduino','LilyPad','Early Arduino')) else 'Other makers'
mc['x'].sort(key=lambda e:(e['g']!='Arduino',))
mc['xg']='by maker'
mc['sel']="Follows Wikipedia's List of Arduino boards and compatible systems (read to 200,000 of 210,594 characters) for the official Arduino boards, plus the ESP, micro:bit, Teensy, Pico, Adafruit and Seeed boards from the structure pass. Complete: 27 of 27 official Arduino boards on the list (current and superseded); the page's long clone and compatible section is out of scope and non-Arduino boards follow no single list."
# ---- keyboard switches
K['Keyboard switches']['sel']="No complete list exists; follows Wikipedia's Keyboard technology for the mechanisms and the enthusiast switch families from the structure pass; loose retail models are versions of their maker's family."
# ---- market
mk=[d['depts'][0],d['depts'][2]]
dn={x['n']:x for x in d['depts']}
H='https://hwbusters.com/news/amd-x86-market-share-tops-30-for-the-first-time-and-desktop-shipments-still-fell-20/'
for who,sh,m in [("AMD","34.9 %","x86 desktop processors, Q2 2026 (Mercury Research)"),("AMD","28.9 %","x86 notebook processors, Q2 2026 (Mercury Research)"),("AMD","34.5 %","x86 server processors, Q2 2026 (Mercury Research)")]:
  dn['PC components']['ms'].append({"mkt":m,"who":who,"share":sh,"yr":2026,"s":H,"note":"unit share; Intel's share of the segment is not stated on the page"})
dn['PC components']['ms'].append({"mkt":"Add-in graphics boards, Q2 2026 (Jon Peddie Research)","who":"All vendors","share":"12.5 million units","yr":2026,"s":"https://www.jonpeddie.com/news/q226-pc-graphics-aib-shipments-increased-10-from-last-quarter-to-12-million-units/","note":"shipments up 10 % on the quarter; the primary release gives vendor shares only in a chart, so the vendor split above stays from the secondary page"})
U='https://www.idc.com/resource-center/blog/ethernet-switch-market-surges-43-4-to-18-9b-in-2q26-as-ai-infrastructure-demand-drives-record-datacenter-spending/'
ms=[]
for who,sh,n in [("Cisco","28.7 %","revenue $5.4 billion"),("Arista Networks","13.4 %","revenue $2.5 billion"),("Huawei","8.2 %","revenue $1.5 billion"),("HPE","6.1 %","")]:
  ms.append({"mkt":"Worldwide Ethernet switches, Q2 2026 (IDC)","who":who,"share":sh,"yr":2026,"s":U,"note":n or "revenue share"})
for who,sh,n in [("Cisco","34.7 %","revenue $1.6 billion"),("Huawei","29.9 %","revenue $1.3 billion"),("HPE","10.7 %","revenue $483 million")]:
  ms.append({"mkt":"Worldwide routers, Q2 2026 (IDC)","who":who,"share":sh,"yr":2026,"s":U,"note":n})
dn['Networking']['ms']=ms
O='https://www.uniindia.com/business-wire-india/omdia-us-pc-shipments-grew-10-in-2q26-while-full-year-market-forecast-to-decline-107-101644/173922'
for who,sh in [("HP","24.4 %"),("Dell","21.2 %"),("Apple","18.8 %"),("Lenovo","18.5 %"),("Acer","6.9 %")]:
  dn['Computers']['ms'].append({"mkt":"US PC shipments, Q2 2026 (Omdia)","who":who,"share":sh,"yr":2026,"s":O,"note":"sell-in units; total 18.8 million"})
T='https://www.trendforce.com/presscenter/news/20260901-13210.html'
dn['Storage']['ms']=[{"mkt":"Enterprise SSD revenue, Q2 2026 (TrendForce)","who":w,"share":"US$"+r,"yr":2026,"s":T,"note":"revenue, not share; top-five total US$37.59 billion"} for w,r in [("Samsung","14.35 billion"),("SK hynix Group","8.63 billion"),("Micron","6.98 billion"),("Kioxia","4.64 billion"),("SanDisk","2.98 billion")]]
# ---- brands
W='wikidata'
upd={'Fujitsu':('Japan','1935'),'NEC':('Japan','1899'),'Kyocera':('Japan','1959'),'Brother':('Japan','1908'),'Tomy':('Japan','1924'),'Elecom':('Japan','1986'),'Sharp':('Japan','1912'),'Videoton':('Hungary','1938'),'Silicon Graphics':('United States','1981'),'Exidy':('United States','1974'),'Spectravideo':('United States','1981'),'SparkFun Electronics':('United States','2003'),'Sun Microsystems':('United States','1982'),'SteelSeries':('Denmark','2001'),'Matra':('France',''),'Sinclair Research':('United Kingdom','1973'),'Espressif':('China','2008'),'Keychron':('China','2017'),'Roccat':('Germany','2007'),'Prusa Research':('Czech Republic','2017'),'Thermalright':('Taiwan','2001'),'Super Flower':('Taiwan','1991'),'Seeed Studio':('China','2008'),'Hardkernel':('South Korea',''),'Memotech':('United Kingdom','1980'),'Coleco':('United States','1932'),'Anycubic':('China',''),'DFRobot':('China','')}
nupd=0
for b in br['b']:
  for key,(c,f) in upd.items():
    if b['n']==key or b['n'].startswith(key+' ') :
      if not b.get('c') and c: b['c']=c; nupd+=1
      if not b.get('f') and f: b['f']=f
print('brands updated',nupd)
# ---- write
def wr(p,o):
  t=p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
wr(OUT+'D1.json',d); wr(OUT+'D1_brands.json',br)
