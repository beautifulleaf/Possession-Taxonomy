import json,re,copy,sys
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_B5_APPL')
from brands_table import B
R='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open(R+'work/V4_B5_APPL/bak/B5.json'))
NAMES=["Kitchen appliances","Coffee","Tea & kettles","Brewing, fermenting & preserving","Food storage & on-the-go","Spare parts"]
depts=[copy.deepcopy(d) for d in old['depts'] if d['n'] in NAMES]
D={d['n']:d for d in depts}
W='https://en.wikipedia.org/wiki/'
report={'removed':[],'m_to_entry':0,'m_removed':[],'new':[]}
def kinds(d):
    for s in d['s']:
        for k in s['k']: yield s,k
def kind(dn,kn):
    for s,k in kinds(D[dn]):
        if k['n']==kn: return k
    raise KeyError(kn)
def ent(k,n):
    for e in k.get('x',[]):
        if e['n']==n: return e
    raise KeyError(n)
def addE(dn,kn,_n,e=None):
    e=e if e is not None else _n
    k=kind(dn,kn); e.setdefault('v',[]); k.setdefault('x',[]).append(e); report['new'].append(e['n'])
YFIX={ # messy year strings -> clean
'catering origins 1952; domestic use from the 1990s':'1952','2010s':'','2020s':'','2000s':'','20th c.':'','current':'','Smeg 2014':'2014',
'c. 2012 (to verify)':'','late 18th–early 19th century':'late 18th century','1695':'', '1854 (brand)':'1854','200-year-old foundry; modern Classic range':'',
'1908 (paper filter); cone filter bags 1936–37':'1908','1958 (Melior patent)':'1958','1905':'1905','1842':'1842',
'1966 (company)':'1966','1955 (first mass-market home machine)':'1955','2018 (Australian launch)':'2018','1987 (company)':'1987',
'1908 (company); MoMA 1993':'1908','late 1990s (lab bottles earlier)':'1990s','2010 (brand)':'2010','2021 (current version)':'2021',
'by 2014':'2014','by 2017':'2017','1988–1989':'1988','1983 (production 1984 per Alessi)':'1983','1930s':'1930','c. 2004':'2004','c. 2018':'2018',
'1995–':'1995','mid-Muromachi period':'','mid-Muromachi period':'','1778 (first factory, Lisitsyn brothers)':'1778',
'red clay found in Stoke-on-Trent area 1695':'','from c. 4000–5000 BCE; in continuous use':'c. 4000 BCE','20th century (Germany)':'20th century',
'17th century (Morioka)':'17th century','Higashiyama era origin':'','1930 1930s':'1930'}
def cleany(e):
    y=str(e.get('y') or '').strip()
    mk=e.get('mk') or ''
    # old data sometimes has the year text inside mk
    if mk and re.search(r'\d{4}',mk) and not y:
        m=re.match(r'^(.*?)\s+(\d{4}.*|current|by .*|catering.*|20th.*|c\. .*)$',mk); 
    y=YFIX.get(y,y)
    y=re.sub(r'\s*\(to verify\)','',y)
    e['y']=y
for dn in NAMES:
    for s,k in kinds(D[dn]):
        for e in k.get('x',[]): cleany(e)
# mk fixes: old data stored 'Maker year' in mk? check below
MKFIX={}
for dn in NAMES:
    for s,k in kinds(D[dn]):
        for e in k.get('x',[]):
            mk=e.get('mk','')
            if mk in('All American 1930',): e['mk']='All American'
# ---------- fixed facts from pages fetched in this batch ----------
def setE(dn,kn,en,**kw): ent(kind(dn,kn),en).update(kw)
KA='Kitchen appliances'; CO='Coffee'; TE='Tea & kettles'; BR='Brewing, fermenting & preserving'; FS='Food storage & on-the-go'
setE(KA,'Toaster',"Smeg 50's Style toaster",y='2014',d="Retro-styled toaster from the Smeg 50's Style range, which added small appliances in 2014.")
setE(KA,'Refrigerator','Smeg FAB',y='1997',d="Smeg's first refrigerators styled on 1950s models, launched under the FAB name in 1997.")
setE(KA,'Air fryer','Philips Airfryer',own='Versuni')
setE(CO,'Semi-automatic espresso machine','La Marzocco Linea Mini',y='2015',v=[
 {'n':'Linea Mini','y':'2015','d':'Home version of the Linea.'},{'n':'GS/3','y':'2007','d':'La Marzocco home model with paddle control.'},{'n':'Linea Micra','y':'2022','d':'Smaller sibling launched November 2022.'}])
setE(CO,'Semi-automatic espresso machine','Breville Barista Express',d='Semi-automatic machine with built-in grinder; the Sage Barista Express in Europe.')
setE(CO,'Capsule coffee machine','Nespresso Original',y='1986',v=[{'n':'Original Line launch','y':'1986','d':'Tested in Japan, sold in Switzerland, France, Italy and Japan.'},{'n':'Inissia','y':'','d':'Entry-level range named on the Nespresso page.'},{'n':'Pixie','y':'','d':'Entry-level range.'},{'n':'U','y':'','d':'Entry-level range.'},{'n':'Lattissima','y':'','d':"Milk-system models made by De'Longhi."}])
setE(CO,'Capsule coffee machine','Nespresso Vertuo',y='2014',s=W+'Nespresso',d='Second Nespresso system, launched in the United States and Canada in February 2014 and in France in 2016.')
setE(CO,'Capsule coffee machine','Keurig K-Cup brewer',s=W+'Keurig_Dr_Pepper',d='Single-serve pod brewer; Green Mountain bought Keurig in 2006 and the brand has sat under Keurig Dr Pepper since the 2018 merger.')
setE(CO,'Capsule coffee machine','Nescafé Dolce Gusto',y='2006',s=W+'Dolce_Gusto',v=[
 {'n':'KP2000 series','y':'2006','d':'First series: KP2000, KP2002, KP2006.'},{'n':'Melody2 (KP21xx)','y':'2008','d':'15-bar pressure rating.'},
 {'n':'Circolo','y':'2009','d':'Series launched mid-2009.'},{'n':'Piccolo (KP10xx)','y':'2010','d':'Compact manual model.'},{'n':'Fontana (KP30xx)','y':'2010','d':'Launched September 2010.'},
 {'n':'Creativa Melody2','y':'2010','d':'Version with LCD display.'},{'n':'Genio S','y':'','d':'Range that includes Genio S Plus and Genio S Touch.'}],
 d='Nestlé capsule system launched in 2006; machines are made by Krups or De\'Longhi.')
setE(CO,'Super-automatic espresso machine','Jura E-line',d='Swiss automatic machine line; Jura was founded in 1931 in Niederbuchsiten.')
setE(CO,'Hand coffee grinder','Comandante C40',s=ent(kind(CO,'Hand coffee grinder'),'Comandante C40')['s'])
setE(CO,'Electric coffee grinder','Baratza Encore',y='')
setE(CO,'Electric coffee grinder','Mazzer Mini',y='',v=[{'n':'Mini Electronic Type A / Type B','y':'','d':'Timer and doser versions.'},{'n':'Mini g','y':'','d':'Variant named on the Mazzer page.'}],s='https://shop.mazzer.com/pages/about',d='Mazzer is a family company near Venice that took the Mazzer name in 1948 and builds professional-grade grinders.')
setE(TE,'Kettle','Russell Hobbs K2',y='1960',s=W+'Kettle')
# new entries
addE(KA,'Multicooker','Ninja Foodi',dict(n='Ninja Foodi',a='Foodi · TenderCrisp',d='Pressure cooker with a second crisping lid that air fries, introduced by SharkNinja in 2018.',mk='Ninja',y='2018',s='https://s202.q4cdn.com/977000893/files/doc_news/Ninja-Foodi-Sets-A-New-Standard-For-Pressure-Cooking-2018.pdf',dt='capacity · lid type · OP300 series'))
addE(CO,'Manual lever espresso machine','Gaggia piston lever machine',dict(n='Gaggia piston lever machine',a='Gaggia lever',d='Achille Gaggia developed the piston lever machine in Italy in 1945.',mk='Gaggia',y='1945',s=W+'Espresso_machine',role='origin',dt='spring or hand lever'))
addE(CO,'Semi-automatic espresso machine','Faema E61',dict(n='Faema E61',a='E61 group',d='Pump-driven machine of 1961 and the first heat-exchanger design; its group head is copied by many home machines.',mk='Faema',y='1961',s=W+'Espresso_machine',role='origin',dt='heat exchanger · E61 group head'))
addE(CO,'Semi-automatic espresso machine','La Marzocco Linea Classic',dict(n='La Marzocco Linea Classic',a='Linea · Linea PB',d="Piero Bambi's Linea, in production by 1990, later called Linea Classic; the Linea PB followed in 2013.",mk='La Marzocco',y='1990',s=W+'La_Marzocco',v=[{'n':'Linea Classic','y':'1990','d':'Original Piero Bambi design.'},{'n':'Linea PB','y':'2013','d':'Successor model.'}],dt='group count · dual boiler'))
addE(CO,'Capsule coffee machine','Tassimo',dict(n='Tassimo',a='T-Disc system',d='Barcode-read T-Disc pod system launched in France in 2004; originally made by Saeco and, from 2008, by Bosch.',mk='Tassimo',y='2004',s=W+'Tassimo',v=[{'n':'T20','y':'','d':'Current home model.'},{'n':'T46','y':'','d':'Home model.'},{'n':'T47','y':'','d':'Home model.'},{'n':'T55','y':'','d':'Home model.'},{'n':'T65','y':'','d':'Home model.'}],dt='disc type'))
addE(CO,'Electric coffee grinder','Mazzer Philos',dict(n='Mazzer Philos',d='Mazzer grinder named on the maker\'s own page beside the Mini and Omega.',mk='Mazzer',y='',s='https://shop.mazzer.com/pages/about'))
# ---------- loose models -> entries ----------
MAKER_FIX={'SharkNinja':'Ninja','Sage (Breville)':'Breville','Mazzer':'Mazzer','Aqua':'Aqua'}
def m_to_entries(dn,k,keepflag=True):
    ms=k.pop('m',None) or []
    for model,maker in ms:
        if not keepflag or not maker:
            report['m_removed'].append(f'{dn}/{k["n"]}: {model} ({maker or "no maker"})'); continue
        mk=MAKER_FIX.get(maker,maker)
        n=model if mk.lower() in model.lower() else f'{mk} {model}'
        if any(e['n'].lower()==n.lower() for e in k.get('x',[])): continue
        k.setdefault('x',[]).append({'n':n,'d':f'{model} is a model line from {mk} named on the page cited for this kind.','mk':mk,'y':'','s':k.get('s'),'v':[]})
        report['m_to_entry']+=1
for dn in (KA,CO,TE):
    for s,k in kinds(D[dn]):
        if dn==TE and k['n'] in('Teapot','Water filter jug'):
            m_to_entries(dn,k,False); continue
        m_to_entries(dn,k)
# ---------- icon rule pruning for commodity departments ----------
KEEP={
 (BR,'Fermentation crock'):['Onggi'],
 (BR,'Preserving jar'):['Mason jar','Weck jar','Kilner jar'],
 (FS,'Food storage container'):['Tupperware Wonder Bowl'],
 (FS,'Drink bottle'):['Sigg Traveller'],
 (FS,'Vacuum flask'):['Thermos flask'],
 (FS,'Hydration bladder'):['CamelBak reservoir'],
 (TE,'Teapot'):['Brown Betty','Bodum Assam tea press'],
 (TE,'Tea caddy'):['Georgian wooden tea caddy'],
 (TE,'Kettle'):['Russell Hobbs K2'],
 (TE,'Soda maker'):['SodaStream','Gasogene'],
 (TE,'Water filter jug'):[],(TE,'Hot water dispenser'):[],
}
for dn in (BR,FS):
    for s,k in kinds(D[dn]):
        m_to_entries(dn,k,False); k.pop('r',None)
        if k.get('x') is not None:
            keep=KEEP.get((dn,k['n']),[])
            for e in k['x']:
                if e['n'] not in keep: report['removed'].append(f'{dn}/{k["n"]}: {e["n"]}')
            k['x']=[e for e in k['x'] if e['n'] in keep]
for (dn,kn),keep in KEEP.items():
    if dn!=TE: continue
    k=kind(dn,kn)
    for e in k.get('x',[]):
        if e['n'] not in keep: report['removed'].append(f'{dn}/{kn}: {e["n"]}')
    k['x']=[e for e in k.get('x',[]) if e['n'] in keep]
# roles
ROLE={('Rice cooker','Toshiba automatic rice cooker'):'origin',('Microwave oven','Radarange'):'origin',('Kettle','Russell Hobbs K2'):'origin',
('Moka pot','Moka Express'):'origin',('Preserving jar','Mason jar'):'origin',('Preserving jar','Weck jar'):'origin',('Food storage container','Tupperware Wonder Bowl'):'origin',
('Vacuum flask','Thermos flask'):'origin',('Drink bottle','Sigg Traveller'):'landmark',('Stand mixer','KitchenAid tilt-head (Model K lineage)'):'landmark',
('Soda maker','SodaStream'):'origin',('Fermentation crock','Onggi'):'origin',('Pour-over dripper','Chemex'):'landmark',('Hydration bladder','CamelBak reservoir'):'origin'}
for dn in NAMES:
    for s,k in kinds(D[dn]):
        for e in k.get('x',[]):
            r=ROLE.get((k['n'],e['n']))
            if r: e['role']=r
# tea entries added
JTEA='Japanese tea'
japan=D[TE]['s'][2]
def newkind(shelf,after,k):
    ks=shelf['k']; i=[x['n'] for x in ks].index(after)+1; ks.insert(i,k); report['new'].append('KIND '+k['n'])
U=W+'Japanese_tea_utensils'
for after,(n,d,tt) in [('Hishaku',('Kensui','Bowl that takes the rinse water in the tea ceremony.',[['Material',['Ceramic','Metal','Bamboo']]])),
 ('Kensui',('Futaoki','Rest for the kettle lid and the ladle.',[['Material',['Bamboo','Ceramic','Metal']]])),
 ('Futaoki',('Furo','Portable brazier that heats the kettle in the warmer months.',[['Material',['Ceramic','Iron','Bronze']]])),
 ('Furo',('Chakin and fukusa','Linen cloth for wiping the bowl and silk cloth for cleansing the scoop and caddy.',[['Cloth',['Chakin (linen)','Fukusa (silk)']]])),
 ('Chakin and fukusa',('Chabako','Lidded portable box holding a complete tea-making set.',[['Material',['Wood','Lacquer']]]))]:
    newkind(japan,after,{'n':n,'d':d,'s':U,'tt':tt,'a':''})
# ---------- market attributes and g ----------
def enrich(e,kn):
    mk=e.get('mk','')
    b=B.get(mk)
    if b and mk:
        own,tier,cty,oy=b
        if e.get('own') is None: e['own']=own
        e['tier']=e.get('tier') or tier; e['cty']=cty
        if oy and not e.get('own_y'): e['own_y']=oy
        if e.get('own')=='Versuni' and mk=='Gaggia': e['own_y']=''
    return e
CTY_OVR={'Toastmaster pop-up toaster':'United States','Sunbeam Radiant Control':'United States','General Electric electric waffle iron':'United States','Radarange':'United States',
'Crock-Pot':'United States','Toshiba automatic rice cooker':'Japan','December Dripper':'United States','Lavazza A Modo Mio':'Italy','Brown Betty':'United Kingdom',
'Georgian wooden tea caddy':'United Kingdom','Tokoname kyusu':'Japan','Banko shidei kyusu':'Japan','Raku chawan':'Japan','Hagi chawan':'Japan','Karatsu chawan':'Japan','Shino chawan':'Japan',
'Takayama chasen':'Japan','Rikyū-gata natsume':'Japan','Katatsuki chaire':'Japan','Nasu chaire':'Japan','Bunrin chaire':'Japan','Nambu arare tetsubin':'Japan','Tula samovar':'Russia',
'Borujerd samovar':'Iran','Kashmiri samovar':'India','Gasogene':'United Kingdom','Gärtopf water-seal crock':'Germany','Onggi':'South Korea','Mason jar':'United States',
'Cornelius keg':'United States','Bodum Assam tea press':'Denmark','Alessi designer kettles (1988–89)':'Italy','Matsushita automatic bread maker':'Japan',
'Robot-Coupe / Magimix':'France','Philips/Saeco LatteGo':'Italy','Nespresso Original':'Switzerland','Starmix':'Germany','Thermomix':'Germany'}
for dn in NAMES:
    for s,k in kinds(D[dn]):
        for e in k.get('x',[]):
            enrich(e,k['n'])
            if e['n'] in CTY_OVR and not e.get('cty'): e['cty']=CTY_OVR[e['n']]
            if k['n']=='Yixing teapot': e['cty']='China'
            if k['n']=='Gaiwan' : e['cty']='China'
            e['g']=e.get('cty') or 'Country not stated'
            if not e.get('cty') and e.get('mk') in B: e['g']=B[e['mk']][2]
# dedicated fixes
ent(kind(CO,'Capsule coffee machine'),'Lavazza A Modo Mio').update(mk='Lavazza',own='Lavazza',tier='Independent',cty='Italy',g='Italy',y='2007')
ent(kind(KA,'Rice cooker'),'Toshiba automatic rice cooker').update(mk='Toshiba')
ent(kind(KA,'Slow cooker'),'Crock-Pot').update(mk='Crock-Pot',own='Newell Brands',tier='Global group',cty='United States')
ent(kind(KA,'Microwave oven'),'Radarange').update(mk='')
for s_,k_ in kinds(D[CO]):
    for e_ in k_.get('x',[]):
        if e_['n']=='WDT tool': e_['g']='No single maker'
ent(kind(KA,'Slow cooker'),'Crock-Pot').update(g='United States')
for n,own in [('Mr. Coffee','Newell Brands')]: pass
def yr(y):
    m=re.search(r'\d{4}',str(y or ''));return int(m.group()) if m else 9999
def order(k):
    xs=k.get('x')
    if xs: xs.sort(key=lambda e:(e['g'],yr(e.get('y')),e['n'].lower()))
for dn in NAMES:
    for s,k in kinds(D[dn]): order(k)
json.dump({'D':D,'report':report},open(R+'work/V4_B5_APPL/stage1.json','w'),ensure_ascii=False)
print(len(report['new']),report['m_to_entry'],len(report['m_removed']),len(report['removed']))
miss=set()
for dn in NAMES:
    for s,k in kinds(D[dn]):
        for e in k.get('x',[]):
            if e.get('mk') and e['mk'] not in B: miss.add(e['mk'])
            if not e.get('cty') : miss.add('NOCTY:'+e['n'])
print(sorted(miss))
