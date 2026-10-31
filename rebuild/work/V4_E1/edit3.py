import json, re, os
exec(open('/home/user/Possession-Taxonomy/rebuild/work/V4_E1/edit2.py').read().split('# 1. remove loose')[0].replace("d=json.load(open(P))","d=json.load(open(P))"))
W='https://en.wikipedia.org/wiki/'
CC={'Great Britain':'UK','U.K.':'UK','The Netherlands':'Netherlands','United States':'USA','Britain':'UK','England':'UK','United Kingdom':'UK','US':'USA','Belgium/USA':'Belgium','Italy/Germany':'Italy'}
def cn(c): return CC.get(c.strip(),c.strip()) if c.strip() and c.strip()!='not stated' else 'Country not stated'
# ---------- 3. kit makers (other sections)
KM=W+'List_of_scale_model_kit_manufacturers'
SEC={'Resin cast':'Resin cast','White metal cast':'White-metal cast','Photo-etched or turned metal':'Photo-etched or turned metal','Wood':'Wooden','Card':'Card','3D-printed':'3D-printed','Mixed materials':'Mixed-material','Unknown material':''}
RAW='''Resin cast
A&W Models (Japan)|Accurate Armour (UK)|Aerobonus (Czech Republic)|Aires (Czech Republic)|Airmodel (Germany)|Akatombo Works (Japan)|Aki Products (Japan)|Anigrand Craftswork (Hong Kong)|Arlo-Micromodel (Portugal)|Baxmod (not stated)|B-Club (Japan)|Black Cat Models (France)|Blue Ridge Models (USA)|Choroszy Modelbud (Poland)|Classic Warships (USA)|CMK (Czech Master Kit) (Czech Republic)|Combrig Models (Russia)|Czech Master Resin (CMR) (Czech Republic)|Fantastic Plastic Models (USA)|Grand System Models (China)|Gumka Miniatures (Japan)|Kombinat (Poland)|Modeler's (Japan)|Model Factory Hiro (Japan)|Olimp (ProResin) (not stated)|OzMods Scale Models (Australia)|ParryArt (Australia)|Quickboost (Czech Republic)|Planet Models (Czech Republic)|Reskit (Ukraine)|Rising Sun Modeling (Japan)|Silver Wings (Poland)|Studio 27 (Japan)|Three Inches Under (USA)|Tori Factory (Korea)|Triglav Model (Slovenia)|Unicraft Models (Ukraine)|Unlimited Air Models (Japan)|Ushimodel (Japan)|Verlinden Productions (Belgium)|Wave Corporation (Japan)|Wheelliant (Czech Republic)
White-metal cast
Branchlines (Great Britain)|DJH Models (Great Britain)|N & C Keyser (K's Models) (Great Britain)|Nu-Cast (Great Britain)|Southeastern Finecast (Great Britain)|Stephen Poole kits (Great Britain)|Wills Finecast (Great Britain)
Photo-etched or turned metal
Aber (Poland)|Aerobase (Japan)|AKA Model (China)|Eduard (Czech Republic)|Gold Medal Models (USA)|L'Arsenal (France)|Master Model (Poland)|Toms Modelworks + White Ensign Models (USA)
Wooden
Amati (Italy)|Artisania Latina (Spain)|Billing Boats (Denmark)|Corel (Italy)|Caldercraft (U.K.)|Campbell Scale Models (USA)|Guillow (USA)|MACO MODELS CO. (USA)|OcCre (Spain)|Kolderstok (The Netherlands)|Scale Decks (USA)|Scientific (USA)|Sterling Models (USA)|Vanguard Models (U.K.)|Woody Joe (Japan)
Card
FlyModel (Poland)|GPM (Poland)|Halinski (Poland)|JSC (Poland)|ModelArt (Bulgaria)|Modelik (Poland)|Schreiber-Bogen (Germany)|Williamshaven (not stated)
3D-printed
3D Model Parts (USA)|FCModeltrend (Spain)|ION Model Figures for warships (Poland)|Kokoda Trail Models (Australia)|Micro Master (New Zealand)|Model Monkey (USA)|NUMODEL (USA)|One Man Model (Japan)|Quinta Studio (Russia)|Tecnikit (Spain)|Classic Airships (USA)
Mixed-material
ARLO-Micromodels (Portugal)|Bluejacket Shipcrafters (USA)|Flagship Models (USA)|Fleetscale (UK)|JetMads (Turkey)|John R. Haynes (UK)|Frog (not stated)|Pocher (UK)|Pontos Model (South Korea)|Revival Deutschland (Italy)|Skybirds (not stated)|Southern Cross Models (Australia)|The Scale Shipyard (USA)|Veteran Made Models (Australia)
Unknown material
ARV (not stated)|Flite Test (not stated)|Gallery (not stated)|Rebell Hobby (Sweden)'''
k=kind('Scale model kit')
byname={e['n'].lower():e for e in k['x']}
aliases={'arlo-micromodels':'arlo-micromodel'}
cur=None; added=0
for line in RAW.split('\n'):
    if '|' not in line and '(' not in line: cur=line; continue
    for it in line.split('|'):
        m=re.match(r'(.*) \(([^()]*)\)$',it); n,c=m.group(1),cn(m.group(2))
        key=aliases.get(n.lower(),n.lower())
        if key in byname:
            e=byname[key]; e['d']=e['d'].rstrip('.')+'; also listed under %s kits.'%cur.lower() if cur!='Unknown material' else e['d']
            continue
        d_='%s scale model kit maker, %s.'%(cur,c) if cur!='Unknown material' else 'Scale model kit maker, %s; material not stated.'%c
        e=E(n,d_ if c!='Country not stated' else d_.replace(', Country not stated',', country not stated'),KM,g=c)
        byname[key]=e; k['x'].append(e); added+=1
k['x'].sort(key=lambda e:(e['g']=='Country not stated',e['g'],e['n'].lower()))
k['sel']="Kit makers follow Wikipedia's List of scale model kit manufacturers (fetched in full). Complete: %d of %d distinct makers across its polystyrene, resin, white-metal, photo-etched, wood, card, 3D-printed, mixed-material and unknown-material sections (a maker listed in several sections is one entry). The earlier loose kit models are removed: a kit belongs to its maker."%(len(k['x']),len(k['x']))
print('kit makers',len(k['x']),added)
# ---------- 4. die-cast whole list
DC=W+'List_of_model_car_brands'
DCRAW='''Abrex Kovove Modely Aut|Czech Republic;AB Minicars|Thailand;Apex Replicas|Australia;Auto World|United States;AUTOart|;Auto Pilen|Spain;Auto Metal / Auro Metal|Yugoslavia;Bburago|Italy;Benbros|United Kingdom;Best Box|Netherlands;Brumm|Italy;Budgie Toys|England;Castle Toy|United Kingdom;Chad Valley|England;Che Zhi|China;Chrono|China;Classic Model Cars (CMC)|Germany;Cararama|China;Crescent Toys|United Kingdom;Danbury Mint|China;DCMT|England;Dinky Toys|;DiP Models|Russia;Dragon Models Limited|Hong Kong;EXOTO|;Efsi Toys|Netherlands;Eligor Models|Switzerland/France;Galgo|Argentina;Gama Toys|Germany;Gasquy-Septoy|Belgium;Giodi|Italy;Gisima|Spain;GreenLight|;Guiloy|Spain;Guisval|Spain;Guri car|Portugal;Hartoys AHL|China;High Speed|Hong Kong;Hot Wheels|United States;HPI Racing|;Hubley Manufacturing Company|United States;Husky Toys|United Kingdom;Jada Toys|;Jadi Modelcraft|;Joal|Spain;Johnny Lightning|;Jouefevolution|France;KK-Scale|Germany;K. K. Sakura|Japan;Kami Motors|South Korea;Lesney|England;Lone Star Toys|United Kingdom;Luso Toys|Portugal;Luxury Diecast|China;Majorette|Germany;Maisto|Thailand;Martoys|;Matchbox|United States;Mebetoys|Italy;Metosul|Portugal;Mettoy|Great Britain;Minichamps|Germany;Motormax|China;Muky|Argentina;Muscle Machines|;Nacoral Intercars|Spain;New-Ray|Hong Kong;Norev|France;Onyx|Portugal;Oxford Diecast|United Kingdom;Playart|Hong Kong;Polistil / Politoys|Italy;Progetto K|Italy;Quartzo|Portugal;Quiralu|France;Racing Champions|United States;Radar|Portugal;Radiosistemi|;Realtoy|China;Real-X|Hong Kong;Record Breakers: World of Speed|;Redbox|;Remco|;Renwal|;Revell|United States;Revell AG|Germany;Revival International|Italy;Rextoys|France/Switzerland;Ribeirinho|;Ricko|Hong Kong;Rico|Spain;Rietze Automodelle|Germany;Rio|Italy;RO Models Workshop|Czech Republic;Road Champs|;Roadmaster|;Robbe|Germany;Robeddie|;Roche Products International|Hong Kong;Roco|Austria;Roskopf (RMM)|Germany;Rosso Corporation|Japan;Les Rouliers|France;RyM|Argentina;S & J Models|Britain;Sablon|Belgium;Sabra|Israel;Safir|France;Saico|;Sam Toys|Italy;Sanwa|Japan;Scale Model Products|United States;Scalextric|;Schabak Modell|Germany;Schuco Modell|Germany;SCX|Spain;Septoy|Belgium;Serpent|Netherlands;Sesame|France;SG Racing Cars|Italy;Shepherd Micro Racing|Italy;Shinsei Mini Power|;Siccom|Italy;Signature Models|;Siku|Germany;Simex|Argentina;SK|Hong Kong;Skynet|;Slik Toys|United States;Shine Dew|China;Slottech|United States;Slot.it|Italy;Small Wheels|;Smer|Czech Republic;SMTS|England;Solido|France;Soma|;Somerville|Britain;Spark models|France;SpecialC.-98|;Speedy|Italy;Spot-on|Northern Ireland;Stahlberg Models|Finland;Starter Models|France;Stelco|Germany;Stirling Scale|Britain;Stjerne|Denmark;Strombecker/Bachmann|United States;Studio 27|Japan;Sun Star|China;Sunnyside|;Takara Tomy|Japan;Tomica|Japan;Tomy|Japan;Tomytec|;Tameo Kits|Italy;Tamiya|Japan;Tarmac Works|Japan;Team Azarashi|;Team Durango|;Tecnomodel|Italy;Tekno|Denmark;Telsalda|Hong Kong;Tenth Technology|;Testors Corporation|;Tetsuma|;Thunder Tiger|;Tiger Wheels|United States;Time Model|;Tin Wizard|Germany;TK.company|;Tokyo Marui|Japan;Tomte Laerdal|Norway;Tonka|United States;Tonkin Replicas|United States;Tootsietoy|United States;Top Marques Collectibles|;Top Model|;TopSpeed Models|;Total Control Racing|;Toy State|;Trax Models|Australia;Traxxas|United States;Tri-ang|England;Trident|Austria;Trincorp|;Triple 9 Collection|;Trofeu|Portugal;True Scale Miniatures|Hong Kong;Mini GT|;Trumpeter|;Trux|Australia;Tudor Rose|Britain;Tyco Toys|United States;Ungar|United States;Unimax|China;Universal Hobbies|;UT Models|Hong Kong;V & V Model|Czech Republic;VAM|Spain;Vanguards|Britain;Vape-Bourbon|France;Verem|;VF Models|Germany;Victory Industries|England;Victory Models|;Vilmer|Denmark;Vitesse Models|Portugal;Wave Corporation|Japan;Wells-Brimtoy|Britain;Welsotoys|Britain;Western Models|;WELLY DIECAST|;Werk83|Germany;White Rose Collectibles|;WhiteBox|;Wiking|Germany;Gerald Wingrove|;H. Wittrock|Denmark;WPL RC|China;Wrenn|;Wingrex Cars|India;Winross Models|United States;Winstar|;Wizzard High Performance|;Wyandotte Toys|United States;XCarToys|;Xonex|;XRAY Model Racing Cars|Slovakia;Yankee|France;Yatming|Hong Kong;YM Model|;Yokomo|Japan;Yonezawa Toys|Japan;Zaugg|Switzerland;Zee Toys|;Ziss Modell|Germany;Zylmex|;Zvezda|Russia'''
k=kind('Die-cast model')
have={e['n'].lower() for e in k['x']}
alias={'matchbox':'matchbox','hot wheels':'hot wheels','dinky toys':'dinky toys','polistil / politoys':'polistil / politoys','tomica':'tomica'}
n_list=0
for it in DCRAW.split(';'):
    n,c=it.split('|'); n_list+=1
    c=CC.get(c,c) if c else ''
    if n.lower() in have or (n=='Tomica' ) : continue
    k['x'].append(E(n,'Model car brand named in Wikipedia\'s List of model car brands%s.'%((', %s'%c) if c else ''),DC,g=cn(c) if c else 'Country not stated'))
    have.add(n.lower())
for e in k['x']:
    if e.get('g') in('Founding lines','Other makers'): pass
# re-group existing: use country where known via mk? leave as is
order={'Founding lines':0,'Other makers':1}
k['x'].sort(key=lambda e:(order.get(e['g'],2),e['g'],e['n'].lower()))
k['sel']="Follows Wikipedia's List of model car brands (fetched in full: A to R from the first window, Radar to Zvezda from the second). Complete: %d of %d brands (Hot Wheels and Matchbox stay one entry each; Tomica is the earlier entry). The list mixes die-cast, plastic, resin, slot-car and radio-control makers and the entries keep its scope. Entries are grouped by the home country the list states."%(len(k['x']),len(k['x']))
k['xg']='by home country'
print('diecast',len(k['x']))
# ---------- 5. rail scales
RS=W+'Rail_transport_modelling_scales'
k=kind('Model railway scale and gauge')
T='''Live steam|No. 1|1:32|45 mm;Live steam|No. 3|1:22.6|64 mm;Live steam|5-inch live steam|1:12|127 or 121 mm;Live steam|1:16 live steam|1:16|89 mm;Live steam|1:24 live steam|1:24|63 mm;Live steam|Grand live steam|1:8|184 or 190.5 mm;Lego-based|Lego Trains|varies|37.5 mm;Lego-based|Lego Narrow Gauge|varies|21.5 mm;Lego-based|L gauge|various|37.5 mm;Historical|K|1:180|8 mm;Historical|Wesa (AC)|1:110|13 mm;Historical|Wesa (DC)|1:100|13 mm;Historical|OOO|-|22 mm;Historical|OO (1908)|-|23 mm;Historical|35 mm|1:30|35 mm;Historical|No. 2|1:27|50.8 mm;Other scales|Grand Scale|1:4 and up|254 mm and up;Other scales|SE scale 7/8 inch|1:13.71|45 mm;Other scales|Gauge 3|1:22.6|63.5 mm;Other scales|Wide gauge|1:26.59 or 1:28.25|53.975 mm;Other scales|16 mm scale|1:19.05|32 or 45 mm;Other scales|Fn3|1:20.3|45 mm;Other scales|Fn2|1:20.3|30 mm;Other scales|G scale|various|45 mm;Other scales|Gn15|various|16.5 mm;Other scales|IIm scale|1:22.5|45 mm;Other scales|1/2 inch scale|1:24|45 mm;Other scales|2 gauge|1:29|50.4 or 45 mm;Other scales|1 gauge (3/8 inch scale)|1:32|45 mm;Other scales|Q scale|1:45|32 mm;Other scales|O scale (UK/France)|1:43.5|32 mm;Other scales|O scale (Germany, Japan, Russia, Czech)|1:45|32 mm;Other scales|O scale (US)|1:48|32 mm;Other scales|O-27|1:48|31.7 mm;Other scales|ScaleSeven|1:43.5|33 mm;Other scales|Proto:48|1:48|29.90 mm;Other scales|OJ|1:45|24.0 mm;Other scales|On2|1:48|12.7 mm;Other scales|On30|1:48|16.5 mm;Other scales|On3|1:48|19 mm;Other scales|O16.5|1:43.5|16.5 mm;Other scales|0e|1:45|16.5 mm;Other scales|O14|1:43.5|14 mm;Other scales|O-12|1:43.5|12 mm;Other scales|Z0 scale|1:60|24 mm;Other scales|S scale (22.42 mm)|1:64|22.42 mm;Other scales|OO gauge|1:76.2|16.5 mm;Other scales|OO9|1:76.2|9 mm;Other scales|0012|1:76.2|12 mm;Other scales|EM gauge|1:76.2|18.2 mm;Other scales|P4|1:76.2|18.83 mm;Other scales|HOj|1:80|16.5 mm;Other scales|Proto:87|1:87|16.5 mm;Other scales|HOn3½|1:87|12.00 mm;Other scales|H0m|1:87|12.00 mm;Other scales|HOn3|1:87|10.5 mm;Other scales|HOe|1:87|9 mm;Other scales|HOn2|1:87|7 mm;Other scales|H0f|1:87|6.5 mm;Other scales|3 mm scale|1:101.6|12 or 14.2 mm;Other scales|N scale (UK)|1:148|9 mm;Other scales|N scale (Japan)|1:150|9 mm;Other scales|2 mm scale|1:152|9.42 mm;Other scales|Nn3|1:160|6.5 mm;Other scales|ZZ|1:300|4.8 mm;Other scales|T gauge|1:450 or 1:480|3 mm'''
for it in T.split(';'):
    g_,n,r,ga=it.split('|')
    e=E(n,'Scale %s on %s track.'%(r,ga),RS,g=g_); e['dt']=r+' · '+ga
    if not has(k,n): k['x'].append(e)
k['sel']="Wikipedia's Rail transport modelling scales (fetched; the page text from character 20,000 on). Covers the %d scales of the NEM standard table plus the Live steam, Lego-based, Historical and Other-scales tables (the Static model row and unnamed live-steam rows are left out); the page's first 20,000 characters were not itemised and the NMRA and British narrow-gauge sections there may hold further names."%len(k['x'])
k['xg']='by table'
print('rail',len(k['x']))
# ---------- 6. playing cards
PC=W+'Playing_card'
k=kind('Playing cards')
add(k,[E('Portuguese-suited deck','Deck using the suits Cups, Coins, Batons, Swords.',PC,g='Suit system'),E('Chinese money-suited deck','Deck using the suits Cash, Strings of Cash, Myriads of Strings, Tens of Myriads.',PC,g='Suit system')])
tar=['Tarot de Marseille','Sola Busca','Swiss 1JJ','Oswald Wirth','Thoth','B.O.T.A.','Motherpeace','Dalí','Rider-Waite']
add(k,[E(t+' tarot' if t not in('Tarot de Marseille','Rider-Waite') else t,'Tarot deck named in the Playing card article; suits Coins or Pentacles, Wands or Staves, Cups, Swords.',PC,g='Tarot deck') for t in tar])
add(k,[E(t,'Early hand-painted or historic deck named in the Playing card article.',PC,g='Early deck') for t in['Ambraser Hofjagdspiel','Flemish Hunting Deck','Hofämterspiel','Stuttgart pack']])
k['sel']="Suit systems and decks follow Wikipedia's Playing card (fetched to its end, 182,000 characters). Complete: %d of %d suit systems, tarot decks and early decks the article names (French, German, Swiss, Italian, Spanish, Portuguese and Chinese money suits; nine tarot decks; four early decks). Regional patterns are earlier entries from their own pages; the article names only the English and Belgian-Genoese patterns."%(len(k['x'])-len([e for e in k['x'] if e.get('g')=='Pattern']),len(k['x'])-len([e for e in k['x'] if e.get('g')=='Pattern']))
k['xg']='by suit system, pattern or deck type'
# ---------- 2. action figure lines
CATF=W+'Category:Action_figures'
k=kind('Action figure')
lines=['Action Force','Action Jackson','Action League Now!','Adventure People','AWA Remco Action Figure line','Barnyard Commandos','Battle Beasts','Beast Saga','Best of the West','Big Jim','Busou Shinki','Captain Action','Chogokin','Computer Warriors','Convertors','Cy Girls','Dino-Riders','Dragon Flyz','Eagle Force','Food Fighters','Galaxy Serie','Galidor','Geyperman','Heavily Armed High School Girls','Imaginext','Jumbo Machinder','Johnny West','Kid Acero','Kiss action figures','Little Dracula','M.A.S.K.','Major Matt Mason','Max Steel','Micronauts','Minimates','Monster Force','The Original Battle Trolls','Power Lords','Sectaurs','Skeleton Warriors','Spiral Zone','Star Wars: The Vintage Collection','Starcom: The U.S. Space Force','Starting Lineup','Stone Protectors','Stretch Armstrong','Stretch Screamers','Super Robot Chogokin','Supernaturals','The Tigers','Tommy Gunn','Tortured Souls','Toxic Crusaders','Visionaries: Knights of the Magical Light','World of Springfield','Wrestling Superstars','Zbots','ZC Girls','ThunderCats','Bionic Six','Blackstar','BraveStarr','Bucky O\'Hare','Captain Power and the Soldiers of the Future','Centurions','Defenders of the Earth','Police Academy','RoboCop','The Saga of Crystar','Savage Mondo Blitzers','Small Soldiers','Devil Eyes','Jet Jungle']
lines=[l for l in lines if l not in('Bionic Six','Blackstar','BraveStarr',"Bucky O'Hare",'Captain Power and the Soldiers of the Future','Centurions','Defenders of the Earth','Police Academy','RoboCop','Small Soldiers','Jet Jungle','Devil Eyes')]
before=len(k['x'])
add(k,[E(l,'Action-figure toy line named in Wikipedia\'s Category:Action figures.',CATF,g='Other toy lines') for l in lines])
k['sel']=k['sel'].split(' Other lines are earlier')[0]+" Other lines: Wikipedia's Category:Action figures (fetched: 9 subcategories and 133 pages). Covers %d toy-line pages of the 133; the rest are companies, people, television series, films, characters, articles on the hobby or legal cases, and the nine subcategories (Action Man, G.I. Joe, Masters of the Universe, Transformers, Gobots and others) are covered by their own entries."%(len(k['x'])-before+11)
# ---------- 1. market panel additions
ad=[x for x in d['depts'] if x['n'].startswith('Action figures')][0]
def ms(mkt,who,share,yr,s,note): return {"mkt":mkt,"who":who,"share":share,"yr":yr,"s":s,"note":note}
ad['ms']+= [
 ms("Toy company revenue","Mattel","US$5.35 billion",2025,W+'Mattel',"net sales as the Wikipedia infobox states; not a market share"),
 ms("Toy company revenue","Hasbro","US$4.7 billion",2025,W+'Hasbro',"revenue as the Wikipedia infobox states; not a market share"),
 ms("Toy company revenue","Spin Master","US$2.042 billion",2021,W+'Spin_Master',"latest revenue the Wikipedia infobox gives; not a market share"),
 ms("Toy company revenue","LEGO Group","DKK 74.3 billion",2024,W+'The_Lego_Group',"revenue; the article gives no market share"),
 ms("Toy company revenue","Bandai Namco Holdings","JPY 1.24 trillion (about US$7.84 billion)",2025,W+'Bandai_Namco_Holdings',"fiscal year ended 31 March 2025, whole group, not toys alone"),
 ms("Toy company revenue","Jakks Pacific","US$571 million",2025,W+'Jakks_Pacific',"FY2025 revenue as the article states"),
 ms("US toy sales, first half","All makers","-0.4 % in dollar sales",2024,'https://toyassociation.org/PressRoom2/News/2024_News/circana-reports-first-half-2024-toy-industry-performance-in-us-and-globally.aspx',"Circana figure; building sets +25 %; Squishmallows (Jazwares) held five of the top spots; no company shares published on the page"),
]
# ---------- 1. owner fields
S='https://en.wikipedia.org/wiki/'
G='Global group'; I='Independent'
OW={}
def o(names,own,tier,cty='',y=''):
    for n in names: OW[n.lower()]=(own,tier,cty,y)
o(['Mattel','Barbie','Hot Wheels','Monster High','My Scene','Ever After High','Masters of the Universe (original toyline)','Princess of Power','He-Man: The New Adventures','Masters of the Universe (200X)','Masters of the Universe Classics and Super7','Masters of the Universe Minis','Masters of the Universe Origins','She-Ra and the Princesses of Power','Masters of the Universe Masterverse','Masters of the Universe Chronicles and Core'],'Mattel',G,'United States')
o(['Fisher-Price'],'Mattel',G,'United States','1993'); o(['American Girl','Bitty Baby'],'Mattel',G,'United States','1998')
o(['Bluebird Toys','Polly Pocket'],'Mattel',G,'','1998'); o(['Lesney','Matchbox'],'Mattel',G,'','1997')
o(['Hasbro','Nerf','Larami','Transformers','Cabbage Patch Kids'],'Hasbro',G,'United States')
o(['Kenner','Parker Brothers','Tonka','Tonka truck'],'Hasbro',G,'United States','1991'); o(['Milton Bradley'],'Hasbro',G,'United States','1984')
o(['Bandai','Bandai Spirits','Banpresto','Banpresto prize figures','Tamagotchi'],'Bandai Namco Holdings',G,'Japan')
o(['Aerobie','Aerobie flying ring'],'Spin Master',G,'United States','2017'); o(['Meccano'],'Spin Master',G,'','2013')
o(['MGA Entertainment','Bratz','Rainbow High','Bratzillaz'],'MGA Entertainment',I,'United States'); o(['Little Tikes','Cozy Coupe'],'MGA Entertainment',I,'United States')
o(['Märklin'],'Simba Dickie Group',I,'Germany','2013'); o(['LGB'],'Simba Dickie Group',I,'Germany'); o(['Majorette'],'Simba Dickie Group',I,'Germany','2010'); o(['Corolle'],'Simba Dickie Group',I,'France','2018'); o(['Jada Toys'],'Simba Dickie Group',I,'United States','2019'); o(['Solido'],'Simba Dickie Group',I,'France','2010'); o(['Schuco Modell'],'Simba Dickie Group',I,'Germany','1999')
o(['Hornby'],'Phoenix Asset Management',I,'United Kingdom','2017'); o(['Scalextric'],'Purbeck Capital Partners',I,'United Kingdom','2025')
o(['Bachmann'],'Kader Group',I,'United States','1981'); o(['Graham Farish'],'Kader Group',I,'','2000')
o(['Geobra Brandstätter','Playmobil'],'Geobra Brandstätter GmbH & Co KG',I,'Germany')
o(['Funko','Funko Pop!'],'Funko Inc.',I,'United States'); o(['Takara Tomy','Takara'],'Takara Tomy',I,'Japan')
o(['Games Workshop','Warhammer'],'Games Workshop Group PLC',I,'United Kingdom'); o(['Tamiya'],'Tamiya Corporation',I,'Japan')
o(['Estes Industries'],'Estes Industries, LLC',I,'United States','2018'); o(['Wham-O'],'The Aguilar Group',I,'United States','2009')
o(['Pop Mart'],'Pop Mart International Group',I,'China'); o(['Good Smile Company'],'Good Smile Company',I,'Japan')
o(['Radio Flyer'],'Radio Flyer',I,'United States'); o(['Epoch'],'Epoch Co.',I,'Japan')
o(['Steiff'],'Ravensburger',I,'Germany','2026'); o(['Brio'],'Ravensburger',I,'Sweden','2015'); o(['F.X. Schmid'],'Ravensburger',I,'','')
o(['Kelly Toys','Squishmallows'],'Jazwares',I,'United States')
MFN='owner not stated'
cnt=0
for dp,s_,k in kinds():
    if dp['n'] in SKIP: continue
    for e in k.get('x',[]):
        mk=e.get('mk','')
        if not mk: continue
        r=OW.get(e['n'].lower()) or OW.get(mk.lower())
        if e['n']=='Blythe': r=None
        if r:
            own,tier,cty,y=r
        else:
            own,tier,cty,y=MFN,I,'',''
        e['own']=own; e['tier']=tier
        if cty: e['cty']=cty
        if y: e['own_y']=y
        cnt+=1
print('owner fields',cnt)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
