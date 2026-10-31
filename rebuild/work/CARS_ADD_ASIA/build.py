import json,re,collections
D='/home/user/Possession-Taxonomy/rebuild/'
cars=json.load(open(D+'out/G1_parts/CARS.json'))
ks=[x for sh in cars['depts'][0]['s'] for x in sh['k']]
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
exist=collections.defaultdict(set)
for k in ks:
    for e in k.get('x',[]):
        exist[e.get('g')].add(norm(e['n'])); 
        for v in e.get('v',[]): exist[e.get('g')].add(norm(v['n']))
CAT='https://en.wikipedia.org/wiki/Category:'
# header lines: marque -> (g, source, prefix)
hdr={'Chery':'Chery','Haval':'Haval','Changan':'Changan','FAW':'FAW','Hongqi':'Hongqi','Roewe':'Roewe','Trumpchi':'Trumpchi','Aion':'Aion','BAIC':'BAIC','JAC':'JAC','Baojun':'Baojun','Li Auto':'Li Auto','Zeekr':'Zeekr','Leapmotor':'Leapmotor','Xiaomi':'Xiaomi','Jetour':'Jetour','Proton':'Proton','Perodua':'Perodua','VinFast':'VinFast','Holden':'Holden','Daewoo':'Daewoo','Isuzu':'Isuzu','Mitsuoka':'Mitsuoka','Genesis':'Genesis','Iran Khodro':'Iran Khodro','Saipa':'Saipa','Daihatsu':'Daihatsu','Tata':'Tata','Great Wall':'Great Wall','Maruti Suzuki':'Maruti Suzuki','Hindustan':'Hindustan','Dongfeng':'Dongfeng','Wuling':'Wuling','Xpeng':'XPeng','Ora':'Ora','HSV':'HSV','SsangYong':'SsangYong','Renault Samsung':'Renault Samsung','Naza':'Naza','Nio':'NIO'}
src={}
rows=[] # (g,title,desc,src)
unc=[]  # (g,title,src)
pick=collections.defaultdict(list)
cur=None
for fn in ['data1.txt','data2.txt','data3.txt']:
    for line in open(fn):
        line=line.rstrip('\n')
        if not line: continue
        if line.startswith('#UNCLASSIFIED'): continue
        if line.startswith('#PICKUP'):
            a,b=line[8:].split('|');pick[a.strip()]+=b.split(',');continue
        if line.startswith('#'):
            h=line[1:].split('|');cur=hdr[h[0]];src[cur]=h[1].split(' (')[0];continue
        t,d=line.split('|',1);rows.append((cur,t,d))
def kind(d):
    x=d.lower()
    if re.search(r'pick|van\b|truck|bus\b|microvan|motorcycle|armou?red|military|robotaxi|weapon',x) and not re.search(r'minivan|mini-van',x): return None
    if re.search(r'coup[eé](?: |-)?utility|coupe utility',x): return 'Utility coupé'
    if 'sports utility from' in x: return 'NS'
    if 'off-road' in x or 'offroad' in x: return 'Off-roader'
    if 'kei car' in x and 'suv' not in x and 'microvan' not in x: return 'Kei car'
    if 'sports car' in x or 'sports sedan' in x or 'performance car' in x and 'luxury' not in x: return 'Sports car'
    if 'convertible' in x: return 'Convertible'
    if 'coupé' in x or 'coupe' in x and 'suv' not in x: return 'Coupé'
    if 'minivan' in x or 'mpv' in x or 'multi purpose' in x or 'multi-purpose' in x: return 'MPV'
    if 'suv' in x or 'crossover' in x or 'cuv' in x or 'sport utility' in x or 'compact liftback'==x: 
        return 'SUV' if 'hatchback' not in x else 'Hatchback'
    if 'luxury' in x and ('sedan' in x or 'saloon' in x or 'car' in x): return 'Luxury saloon'
    if 'executive' in x: return 'Luxury saloon'
    if 'city car' in x or 'mini-car' in x or 'city' in x: return 'City car'
    if 'hatchback' in x or 'liftback' in x or 'supermini' in x or 'subcompact car' in x or 'compact car' in x or 'small family' in x or 'small car' in x or 'subcompact' in x: return 'Hatchback'
    if 'sedan' in x or 'saloon' in x or 'mid-size car' in x or 'large family' in x or 'mid-sized car' in x: return 'Saloon'
    if 'station wagon' in x: return 'Estate'
    if 'sports utility' in x: return 'SUV'
    return 'NS'
# explicit unclassified lists: (g, prefix, [names])
U={
'Chery':('Chery',['A1','A3','Fulwin 2','Arrizo 3','Arrizo 5','Arrizo 7','Arrizo 8','Arrizo 5 Plus','Arrizo M7','Explore 06','Cowin','E3','E5','G5','J3','Kimo','QQ6','Tiggo 2','Tiggo 5','Eastar Cross']),
'Haval':('Haval',['F5','F7','H1','H2','H2s','H5','H6 Coupe','H8','Shenshou']),
'Changan':('Changan',['Oshan X70A',"Chang'an Z-Shine",'Deepal L07','Nevo A05','Oshan Changxing','Ruixing M80','Ruixing M90','Ruixing S50','Chana CX70']),
'FAW':('FAW',['Jetta VS5','Junpai A70','Oley','Senia R7','Weizhi V2','SiTech DEV1']),
'Hongqi':('Hongqi',['CA72','CA770','E-HS3','H6','H7','H9','Shengshi','HQE','HS3','S9','Tiangong 07']),
'Roewe':('Roewe',['350','360','550' if False else '750','950','Clever','E50','i5','i6','Jing','M7','Marvel X','RX3','W5']),
'Trumpchi':('Trumpchi',['GS4 Coupe','Xiangwang E8','Xiangwang M8']),
'Aion':('Aion',['Hyptec S600','i60']),
'BAIC':('BAIC',['Beijing X5','Beijing EX3','BJEV EC3','Huansu H2','Huansu H5','Huansu S2','Huansu S3','Ruixiang X5']),
'JAC':('JAC',['Heyue A20','Heyue A30','Heyue Tongyue','Heyue Binyue','iEV6E','iEVA50','J2','J3','Refine M2','Refine M3','Refine M4','Refine M5','Refine L6 MAX','Refine A60','Refine R3','Refine S2','Refine S3','Refine S4','Refine S5','Refine S7','Rein','Sehol E10X','Sehol E20X','QX','Sunray','Yueyue']),
'Baojun':('Baojun',['310','360','560','610','E100','E200','KiWi EV','Lechi','RC-6']),
'Leapmotor':('Leapmotor',['C-More']),
'Proton':('Proton',['Compact','eMas 5','eMas 7','eMas 7 PHEV','Ertiga','Inspira','Iriz','Juara','M21','Prevé','Putra','Savvy','Satria','Tiara','X90','Jumbuck']),
'Perodua':('Perodua',['Aruz','Ativa','Kembara','Nautica']),
'VinFast':('VinFast',['VF MPV 7','VF 2','President']),
'Holden':('Holden',['Acadia','Adventra','Belmont','Berlina','Business','Calais','Calibra','Cascada','Combo','Commodore','Crewman','Cruze','Drover','Epica','Equinox','Frontera','GTS','Insignia','Jackaroo','Limited Edition','Lincah','Malibu','Monterey','One Tonner','Piazza','Premier','Raider','Scurry','Shuttle','Spark','SS','Standard','Statesman','Suburban','Sunbird','Tigra','TrailBlazer','Trax','Vectra','Volt','Zafira']),
'Daewoo':('Daewoo',['1.5i','Alpheon','Arcadia','Brougham','Chairman','Damas','Espero','Fantasy','FX212 Super Cruiser','G2X','Heaven','Imperial','Korando','Lacetti Premiere','Lanos','Leganza','Matiz','Mirae','Musiro','Musso','Nexia','Nubira','Pointer','Prince','Racer','Royale','Saehan Camina','Speedster','Super Salon','Tacuma','Tico','Tosca','Veritas','Winstorm']),
'Isuzu':('Isuzu',['4200R','Alterra','Amigo','Ascender','Bellel','Bellett','Bellett Gemini','Bison','Como','Cubic','Fargo','Florian','Geminett','Geminett II','Gemini','Hillman Minx','I-Mark','i-Series','Impulse','MU Wizard','MU-7','Oasis','Reach','Rodeo Denver','Spark','Statesman De Ville','Stylus','Unicab','Wasp','WFR','Wizard']),
'Mitsuoka':('Mitsuoka',['Buddy','Cute','Galue','Himiko','Le-Seyde','MC-1','Nouera','Orochi','Ray','Ryoga','Ryugi','Viewt']),
'Iran Khodro':('IKCO',['Arisun','Dena','Runna','Samand','Soren','Reera','Tara']),
'Saipa':('Saipa',['111','131','132','141','151','Atlas','Nasim','Quik','Saba','Safari','Saina','Tiba']),
'Daihatsu':('Daihatsu',['Altis','Applause','Bee','Be-go','Ceria','Compagno','Coo','Cuore','Domino','Esse','Extol','Fellow','Feroza','Fourtrak','Gran Max','Grand Move','Leeza','Materia','Max','Midget','Mira Cocoa','Mira Gino','Mira Tocot','Move Conte','Move Latte','Opti','Pyzar','Rugger','Scat','Sirion','Sonica','Sportrak','Storia','Taft','Taruna','Terios Kid','Trevis','Wildcat','Xenia','YRV','Zebra']),
'Great Wall':('Great Wall',['Coolbear','Cowry','Deer','Florid','Haval H3','Pegasus','Peri','Safe','Sailor','SoCool','Voleex C10','Voleex C20R','Voleex C50']),
'Maruti Suzuki':('Maruti',['800','1000','Alto','Baleno','Brezza','Celerio','Ciaz','Eeco','Ertiga','Esteem','Grand Vitara','Gypsy','Ignis','Omni','S-Presso','Versa','Wagon R','XA Alpha','XL6','Zen']),
'Hindustan':('Hindustan',['Contessa']),
'Dongfeng':('Dongfeng',['Aeolus AX3','Aeolus AX4','Aeolus AX5','Aeolus AX7','Aeolus E30','Aeolus E30L','Aeolus Haohan','Aeolus L60','Aeolus S30','A9','E-Star','Fengdu MX5','Fengguang 330S','Forthing Jingyi S50','Forthing Jingyi X5','Forthing Jingyi X6','Forthing Lingzhi','Forthing S500','Forthing SX6','Huashen Tianlai','Rich','Yufeng','Voyah i-Land','Voyah Passion L','Voyah Taishan X8']),
'Wuling':('Wuling',['Almaz','Alvez','Confero','Cortez','Dragon','Formo','Hongtu','LZ110','Rongguang','Sunshine']),
'Ora':('Ora',['5','Black Cat','Cherry Cat','iQ','White Cat']),
'HSV':('HSV',['Avalanche','Caprice','Clubsport','Jackaroo','Manta','Statesman','SV88','SV91','VXR','W427','XU6']),
'SsangYong':('SsangYong',['Actyon','Actyon Sports','Chairman','Istana','Korando','Korando Family','Kyron','Musso','Rhino','Rodius','Tivoli','Transstar','WZ','KGM Torres']),
'Renault Samsung':('Renault Samsung',['QM3','QM5','SM3','SM5','SM6','SM7','XM3']),
'Naza':('Naza',['Sutera']),
# covered marques (names from fetched category extracts; class-less ones only)
'Toyota':('Toyota',['Agya','Allex','Altezza','Altezza Gita','Camry Solara','Carina E','Celica Supra','Crown Kluger','Crown Vellfire','Cynos','Echo','Estima','Frontlander','GR86','GranAce','IZOA','Lexcen','Lingshang','Majesty','Mark II Blit','Mark II Qualis','Mark X ZiO','Pixis Joy','Pixis Mega','Pixis Space','Prius Prime','Reiz','Rukus','Scepter','Soluna','Soluna Vios','Tamaraw FX','Tiara','Transmover','Unser','Urban Cruiser Hyryder','Urban Cruiser Taisor','Urban Cruiser (BEV)','Venture','Ventury','Verso-S','Vienta','Vista Ardeo','Voltz','Wigo','WiLL Cypha','WiLL Vi','WiLL VS','Yaris iA','Yaris R','Zace','Zelas','Corsa','Cavalier','Condor','Copen GR Sport','Sprinter Marino','Toyopet Master','COMS','bZ4X Touring','Masterline']),
'Mazda':('Mazda',['121','616','618','800','808','818','1000','1200','1300','1500','1800','2000','5','8','Allegro','Artis','Astina','Atenza','Axela','AZ-3','AZ-550','Chantez','Flair','Flair Crossover','Flair Wagon','GLC','Isamu Genki','Laputa','Metro','Miata','Mizer','Montrose','Precedia','Proceed Levante','Proceed Marvie','Protegé','R130','R360','RX-2','RX-4','RX-5','RX-9','Rustler','Savanna','Spiano','Traveller','VX-1']),
'Honda':('Honda',['EV Plus','FCX','That\'s','Vamos','GT','P7']),
'Nissan':('Nissan',['Rasheen','S-Cargo']),
'Mitsubishi':('Mitsubishi',['500','Freeca','Model A']),
'Subaru':('Subaru',['Elaion','Sumo','R1e']),
'Suzuki':('Suzuki',['CV1','GSX-R/4']),
'Hyundai':('Hyundai',['E4U']),
'Mahindra':('Mahindra',['Goa','Maxx']),
}
# classified additions for covered marques
extra=[('Toyota','Toyota bZ5','Battery electric compact crossover SUV'),('Toyota','Toyota bZ7','Battery electric full-size sedan for Chinese market'),
('Honda','Honda GT','Battery electric mid-size sedan'),('Honda','Honda P7','Battery electric mid-size crossover SUVs'),
('Nissan','Nissan Jonga','Mid-size off road vehicle'),('Nissan',"Nissan R'nessa",'Crossover station wagon produced by Nissan (1997-2001)'),
('Mitsubishi','Mitsubishi 380','Australian mid-size car (2005–2008)'),('Mitsubishi','Mitsubishi Zinger','Compact MPV'),
('Suzuki','Suzuki e Sky','Battery electric kei car'),
('Daihatsu','Daihatsu Hijet','x')]
extra=extra[:-1]
rows=[r for r in rows]+extra
# facts: g -> (cty, own, tier, source)
W='https://www.wikidata.org/wiki/Special:EntityData (SPARQL query.wikidata.org, fetched 2026-10-31)'
F={'Chery':('China','Chery Holding','Independent'),'Hindustan':('India','',''),'Great Wall':('China','', ''),'Haval':('','Great Wall Motor','Independent'),'Changan':('China','China South Industries Group','Independent'),'Dongfeng':('China','State-owned Assets Supervision and Administration Commission of the State Council','Independent'),'FAW':('China','State-owned Assets Supervision and Administration Commission of the State Council','Independent'),'Hongqi':('China','',''),'BAIC':('China','',''),'Zeekr':('China','',''),'Jetour':('China','Chery','Independent'),'Wuling':('China','Guangxi Automobile Group','Independent'),'Proton':('Malaysia','DRB-HICOM','Independent'),'VinFast':('Vietnam','Vingroup','Independent'),'Holden':('Australia','General Motors','Global group'),'Isuzu':('Japan','',''),'Saipa':('Iran','',''),'Iran Khodro':('Iran','',''),'Naza':('Malaysia','',''),'Lexus':('Japan','Toyota','Global group'),'Daihatsu':('Japan','Toyota','Global group'),'Genesis':('South Korea','Hyundai Motor Company','Global group'),'Kia':('South Korea','Hyundai Motor Group','Global group'),'Hyundai':('South Korea','Hyundai Motor Group','Global group'),'Nissan':('Japan','',''),'Maruti Suzuki':('India','Suzuki Motor Corporation','Global group'),'Mitsubishi':('Japan','',''),'Subaru':('Japan','Subaru Corporation','Independent'),'Mahindra':('India','','Independent'),'Honda':('Japan','',''),'Mazda':('Japan','',''),'Toyota':('Japan','',''),'Acura':('Japan','American Honda Motor Company',''),'MG':('United Kingdom','SAIC Motor','Global group'),'Suzuki':('Japan','',''),'Geely':('China','',''),'BYD':('China','',''),'SsangYong':('South Korea','KG Mobility → KG Group','Independent'),'Datsun':('','',''),'Infiniti':('','','')}
F['SsangYong']=('South Korea','KG Group','Independent')
kinds=collections.defaultdict(list); skipped=collections.Counter(); NSn=collections.Counter(); pk=collections.defaultdict(list)
def mk_entry(g,name,y,s,d):
    e={'n':name,'mk':g,'y':y,'g':g,'s':s,'v':[],'sec':g}
    if d: e['d']=d
    f=F.get(g)
    if f:
        if f[0]: e['cty']=f[0]
        if f[1]: e['own']=f[1]
        if f[2]: e['tier']=f[2]
    return e
def have(g,name):
    n=norm(name); p=norm(g)
    return n in exist[g] or n.replace(p,'',1) in {x.replace(p,'',1) for x in exist[g]}
for g,t,d in rows:
    kd=kind(d)
    if kd is None: pk[g].append(t);continue
    if have(g,t): skipped[g]+=1;continue
    y=''
    yrs=[]
    if kd!='NS': yrs=[int(a) for a in re.findall(r'(?<!\d)(1[89]\d\d|20[0-2]\d)(?!\d)',d)]
    if yrs: y=str(min(yrs))
    if kd=='NS': kd='Car, body style not stated'; NSn[g]+=1
    kinds[kd].append(mk_entry(g,t,y,src.get(g,CAT+g.replace(' ','_')+'_vehicles'),d if kd!='Car, body style not stated' else ''))
S={'Toyota':CAT+'Toyota_vehicles','Mazda':CAT+'Mazda_vehicles','Honda':CAT+'Honda_vehicles','Nissan':CAT+'Nissan_vehicles','Mitsubishi':CAT+'Mitsubishi_Motors_vehicles','Subaru':CAT+'Subaru_vehicles','Suzuki':CAT+'Suzuki_vehicles','Hyundai':CAT+'Hyundai_vehicles','Mahindra':CAT+'Mahindra_vehicles'}
for g,(pre,names) in U.items():
    for n in names:
        full=n if (n.startswith(pre) or n.startswith('KGM') or n.startswith('Toyopet')) else pre+' '+n
        if have(g,full) or have(g,n): skipped[g]+=1;continue
        if any(norm(full)==norm(e['n']) for e in kinds['Car, body style not stated']): continue
        kinds['Car, body style not stated'].append(mk_entry(g,full,'',src.get(g,S.get(g,CAT+g.replace(' ','_')+'_vehicles')),''))
        NSn[g]+=1
# dedupe within all kinds
seen=set()
for k in list(kinds):
    out=[]
    for e in kinds[k]:
        key=(e['g'],norm(e['n']))
        if key in seen: continue
        seen.add(key);out.append(e)
    kinds[k]=out
bu={}
for g,(c,o,t) in F.items():
    u={}
    if o: u['own']=o
    if c: u['c']=c
    if t: u['tier']=t
    if u: bu[g]=u
old=cars['brand_updates']
diff=[]
for g,u in bu.items():
    for kk in ('own','c'):
        if g in old and kk in u and old[g].get(kk)!=u[kk]: diff.append((g,kk,old[g].get(kk),u[kk]))
brands=[{'n':g,'c':F[g][0]} for g in F if F[g][0] and g not in old and g not in {'Maruti Suzuki'} and not any(b['n']==g for b in cars['brands'])]
out={'kinds':dict(kinds),'brands':brands,'brand_updates':bu}
import os
os.makedirs(D+'out/G1_parts/cars_add',exist_ok=True)
json.dump(out,open(D+'out/G1_parts/cars_add/ASIA.json','w'),ensure_ascii=False)
print({k:len(v) for k,v in kinds.items()});print('skipped existing',dict(skipped));print('NS',dict(NSn));print('pick',{g:len(v) for g,v in pk.items()});print('diff',diff)
print(sum(len(v) for v in kinds.values()))
json.dump({g:v for g,v in pk.items()},open('pickups.json','w'))
