import json,copy,os
src=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/E2.json'))
reg={x['n'] for x in json.load(open('/home/user/Possession-Taxonomy/rebuild/out/E2_brands.json'))['b']}
WP=lambda t:'https://en.wikipedia.org/wiki/'+t
S_PEL=WP('Peloton_Interactive');S_C2=WP('Concept2');S_TG=WP('Technogym');S_LF=WP('Life_Fitness');S_BF=WP('Bowflex')
S_NT=WP('NordicTrack');S_SM=WP('StairMaster');S_RG=WP('Rogue_Fitness')
S_TON='https://www.silicon.co.uk/press-release/tonal-ushers-in-the-future-of-fitness-with-tonal-2-designed-to-improve-performance-and-build-muscle-faster'
# brand info: maker -> (own, tier, cty, own_y)
BI={
'Peloton':('Peloton Interactive','National champion','United States',''),
'Concept2':('Concept2','Independent','United States',''),
'Technogym':('Technogym S.p.A.','Independent','Italy',''),
'Life Fitness':('KPS Capital Partners','Global group','United States','2019'),
'Bowflex':('Johnson Health Tech','Independent','United States','2024'),
'NordicTrack':('iFIT Inc.','Global group','United States','1998'),
'StairMaster':('Core Health & Fitness','Independent','United States','2009'),
'Rogue Fitness':('Rogue Fitness','Independent','United States',''),
'Tonal':('Tonal','Independent','United States',''),
'Everlast':('Frasers Group','Independent','United States','2007'),
'Cleto Reyes':('Cleto Reyes','Independent','Mexico',''),
'Winning':('Winning','Independent','Japan',''),
'Twins Special':('Twins Special','Independent','Thailand',''),
'Freed of London':('Onward Holdings','National champion','United Kingdom','1993'),
'Bloch':('Bloch','Independent','Australia',''),
'Capezio':('Capezio','Independent','United States',''),
'Gaynor Minden':('Gaynor Minden','Independent','United States',''),
'Grishko':('Grishko','Independent','Russia',''),
'Repetto':('Repetto','National champion','France',''),
'Mizuno':('Mizuno','Independent','Japan',''),
'adidas':('adidas','Global group','Germany',''),
'Tokaido':('Tokaido','Independent','Japan',''),
'Shureido':('Shureido','Independent','Japan',''),
'Nike':('Nike','Global group','United States',''),
'Puma':('Puma','Global group','Germany',''),
'Polanik':('Polanik','Independent','Poland',''),
'Gill Athletics':('Gill Athletics','Independent','United States',''),
'Leon Paul':('Leon Paul','Independent','United Kingdom',''),
'Allstar':('Allstar','Independent','Germany',''),
'Uhlmann':('Uhlmann','Independent','Germany',''),
'Keiser':('Keiser','Independent','United States',''),
}
def ent(n,mk,y,d,s,g=None,v=(),a='',dt=None,role=None):
    e={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':[{'n':x[0],'mk':mk,'y':x[1],'d':x[2]} for x in v]}
    if dt:e['dt']=dt
    e['g']=g or mk
    if role:e['role']=role
    b=BI.get(mk)
    if b:
        e['own'],e['tier'],e['cty'],e['own_y']=b
        if not e['own_y']:del e['own_y']
    return e
def maker(mk,models,s,kindword,cty=None,own=None):
    """maker entry: loose models as versions"""
    e=ent(mk+' '+kindword,mk,'',f"{mk} {kindword} models named on the retailer category page cited; each is a version.",s,v=[(m,'','') for m in models])
    if mk not in BI and own is not False:
        e['own']=own or mk;e['tier']='Independent'
        if cty:e['cty']=cty
    return e
def kindfix(k,x,nl,sel,xg='by maker',tt=None):
    k.pop('m',None);k.pop('r',None)
    k['x']=x;k['nl']=nl;k['sel']=sel;k['xg']=xg
    if tt is not None:k['tt']=tt
NL_MODEL="One entry is a named model line sold by one maker; sizes, model years and revisions are versions, and a maker with no named line appears as one maker entry whose models are versions."
def sel(ref,n,extra=''):
    return f"No whole-space list of {ref} exists; entries follow the maker pages cited on each entry and the retailer category page cited for the kind. {extra}Covers {n} lines and makers from those pages, not every product on the market."
dept_f=copy.deepcopy([d for d in src['depts'] if d['n']=='Fitness & home gym'][0])
dept_a=copy.deepcopy([d for d in src['depts'] if d['n']=='Athletics, dance & combat'][0])
K={k['n']:k for s in dept_f['s'] for k in s['k']}
KA={k['n']:k for s in dept_a['s'] for k in s['k']}
def put(k,x,extra=''):
    kindfix(k,x,NL_MODEL,sel(k['n'].lower()+'s',len(x),extra))
# ---- cardio
k=K['Treadmill']
put(k,[
 ent('Peloton Tread','Peloton','2018','Connected treadmill with subscription classes; the Tread+ was unveiled at CES in January 2018, a lower-priced Tread followed in September 2020.',S_PEL,v=[('Tread+','2018','unveiled as the Tread, 32-inch touchscreen, slatted belt; recalled May 2021'),('Tread','2020','lower-priced model; recalled May 2021 over touchscreen screws')],dt='belt or slat deck · screen · subscription'),
 ent('NordicTrack incline trainer','NordicTrack','2009','Incline treadmill line that NordicTrack pioneered in 2009, now sold by iFIT.',S_NT,a='X Series',v=[('X24','','')],role='origin'),
 ent('NordicTrack T Series','NordicTrack','','NordicTrack treadmill line named Best Overall at-home treadmill by one review in August 2019.',S_NT,v=[('T Series 10','','')]),
 ent('NordicTrack Commercial series','NordicTrack','','NordicTrack treadmill line; the Commercial 1750 earned a Consumer Reports Recommended Buy in 2016.',S_NT,v=[('Commercial 1750','','Consumer Reports Recommended Buy 2016'),('Commercial 2450','','')]),
 ent('Technogym Excite','Technogym','2002','Technogym cardio line, the first with an integrated TV screen; includes treadmills.',S_TG),
 maker('Sole Fitness',['F63'],k['s'],'treadmills','United States'),
 maker('ProForm',['Pro 2000'],k['s'],'treadmills','United States'),
 maker('Horizon Fitness',['T101'],k['s'],'treadmills','United States'),
 ent('Bowflex Treadmill','Bowflex','','Bowflex treadmill range sold under the Bowflex name.',k['s'],v=[('Treadmill 10','','')]),
])
k=K['Upright exercise bike']
put(k,[
 ent('Life Fitness LifeCycle','Life Fitness','1977','Exercise bike line from the company founded as Lifecycle, Inc. in 1977 on Keene Dimick\'s 1968 design.',S_LF,v=[('C1 LifeCycle','',''),('C3 LifeCycle','','')]),
 ent('Technogym Personal bike','Technogym','2014','Home bike of Technogym\'s Personal Line, designed with Antonio Citterio and launched in 2014.',S_TG,v=[('Bike Personal','2014',''),('Cycle Upright Bike','','')]),
 ent('TRUE Performance Series upright bike','TRUE Fitness','','Upright bike of the TRUE Performance Series commercial-grade range.',k['s'],v=[('Performance Series Upright Bike','','')]),
 maker('NordicTrack',['G LE Upright Bike'],S_NT,'upright bikes'),
 maker('Marcy Pro',['Magnetic Upright Exercise Bike NS-40504U'],k['s'],'upright bikes','United States'),
])
k['x'][3]=ent('NordicTrack upright bikes','NordicTrack','','NordicTrack upright exercise bike range.',S_NT,v=[('G LE Upright Bike','','')])
k=K['Recumbent exercise bike']
put(k,[
 ent('Life Fitness LifeCycle recumbent','Life Fitness','','Recumbent models of the LifeCycle line.',S_LF,v=[('RS1 LifeCycle Recumbent','',''),('RS3 LifeCycle Recumbent','','')]),
 ent('Technogym Recline Personal','Technogym','2014','Recumbent bike of the Personal Line.',S_TG,v=[('Recline Personal','2014','')]),
 ent('TRUE Performance Series recumbent bike','TRUE Fitness','','Recumbent bike of the TRUE Performance Series.',k['s'],v=[('Performance Series Recumbent Bike','','')]),
 ent('NordicTrack recumbent bikes','NordicTrack','','NordicTrack recumbent bike range.',S_NT,v=[('10 Recumbent Bike','',''),('G LE Recumbent Bike','','')]),
])
k=K['Spin bike']
put(k,[
 ent('Peloton Bike','Peloton','2014','Connected stationary bike with a built-in screen and subscription classes; early-bird sale on Kickstarter in 2013 at $1,500.',S_PEL,v=[('Bike','2014','21.5-inch touchscreen'),('Bike+','2020','23.8-inch rotating touchscreen, auto-resistance')],role='origin',dt='screen size · resistance · subscription'),
 ent('Technogym Bike','Technogym','2019','Indoor bike offering live and on-demand cycling classes.',S_TG,v=[('Ride Indoor Cycle','',''),('Group Cycle Connect','','')]),
 maker('Keiser',['M3i Indoor Bike'],k['s'],'indoor bikes'),
 maker('Schwinn Fitness',['IC4'],k['s'],'indoor bikes','United States'),
 ent('NordicTrack studio bikes','NordicTrack','','NordicTrack connected indoor bikes.',S_NT,v=[('S24 Bike','',''),('S22i','','')]),
 ent('Bowflex C6','Bowflex','','Bowflex connected indoor bike.',k['s'],v=[('C6 Bike','','')]),
 maker('Echelon',['EX-8s'],k['s'],'indoor bikes','United States'),
 maker('MyxFitness',['Myx II'],k['s'],'indoor bikes','United States'),
 maker('NOHrD',['Bike Indoor Cycle'],k['s'],'indoor bikes','Germany'),
])
k=K['Air bike']
put(k,[
 ent('Rogue Echo Bike','Rogue Fitness','','Fan-braked exercise bike with moving arms from Rogue Fitness, founded in 2007 in Toledo, Ohio.',S_RG),
 ent('Concept2 BikeErg','Concept2','2017','Air-braked bike ergometer from Concept2, introduced in 2017.',S_C2,v=[('BikeErg','2017','PM5 monitor')]),
 ent('Assault AirBike','Assault Fitness','','Assault Fitness fan bike range.',k['s'],v=[('AirBike Classic','','')]),
 ent('Schwinn Airdyne','Schwinn Fitness','','Schwinn fan bike line named on the retailer page cited.',k['s'],v=[('Airdyne AD7','','')]),
 maker('Titan Fitness',['Fan Bike'],k['s'],'air bikes','United States'),
 maker('Bells of Steel',['Blitz Air Bike 2.0'],k['s'],'air bikes','United States'),
 maker('Fringe Sport',['Raptor Air Bike'],k['s'],'air bikes','United States'),
])
k=K['Rowing machine']
put(k,[
 ent('Concept2 RowErg','Concept2','2003','Air-and-flywheel indoor rower from Concept2; Model D (2003) and Model E (2006) were renamed RowErg and RowErg with Tall Legs in 2021.',S_C2,a='Concept2 Model D',v=[('Model A','1981','made mainly from bicycle parts'),('Model B','1986',''),('Model C','1993',''),('Model D','2003','renamed RowErg, 14-inch legs, in 2021'),('Model E','2006','renamed RowErg with Tall Legs, 20-inch legs, in 2021'),('Dynamic','2010','moving foot stretcher instead of a moving seat; Dynamic RowErg')],dt='PM5 monitor (from 2014) · standard or tall legs'),
 ent('Peloton Row','Peloton','2022','Connected indoor rower announced May 2022 and launched September 2022.',S_PEL),
 maker('WaterRower',['M1 HiRise'],k['s'],'rowing machines','United States'),
 ent('Hydrow','Hydrow','','Connected rowers with streamed on-water classes.',k['s'],v=[('Wave','',''),('Rower','','')]),
 maker('Ergatta',['Ergatta Rower'],k['s'],'rowing machines','United States'),
 ent('Rogue Echo Rower','Rogue Fitness','','Rowing machine sold by Rogue Fitness.',k['s'],v=[('Echo Rower','','')]),
 ent('Assault AssaultRower','Assault Fitness','','Assault Fitness rowing machine.',k['s'],v=[('AssaultRower Pro','','')]),
 ent('NordicTrack RW900','NordicTrack','','NordicTrack connected rower.',k['s'],v=[('RW900','','')]),
 ent('ProForm Pro R10','ProForm','','ProForm connected rower.',k['s'],v=[('Pro R10','','')]),
 ent('Echelon Row-S','Echelon','','Echelon connected rower.',k['s'],v=[('Row-S','','')]),
])
k=K['Ski ergometer']
put(k,[ent('Concept2 SkiErg','Concept2','2009','Wall- or stand-mounted ergometer simulating a double-pole ski stroke; introduced in 2009.',S_C2,v=[('SkiErg','2009','PM5 monitor')],a='')])
k=K['Elliptical cross trainer']
put(k,[ent('NordicTrack elliptical','NordicTrack','','NordicTrack elliptical range.',S_NT,v=[('X16 Elliptical','','')]),
 maker('Sole Fitness',['E25'],k['s'],'ellipticals','United States'),
 ent('Bowflex Max Trainer','Bowflex','','Bowflex stepping cross trainer line.',k['s'],v=[('Max Trainer M6','','')]),
 maker('Horizon Fitness',['Andes 7.1'],k['s'],'ellipticals','United States')])
k=K['Recumbent cross trainer']
put(k,[maker('Teeter',['FreeStep LT1 Recumbent Step Bike'],k['s'],'recumbent cross trainers','United States')])
k=K['Stair climber']
put(k,[
 ent('StairMaster StepMill','StairMaster','1983','Revolving-staircase machine from StairMaster, launched in 1983 at a National Sporting Goods Association show.',S_SM,v=[('StairMaster 5000','1983',''),('StairMaster 6000','1984',''),('Gauntlet','1988',''),('StepMill 7000PT','1991',''),('StepMill 916','2008',''),('StepMill 5 (SM5)','2011',''),('StepMill 3 (SM3)','2012','')]),
 ent('StairMaster StairClimber','StairMaster','1986','Independent-pedal stepper line from StairMaster.',S_SM,v=[('StairMaster 4000 PT','1986',''),('StairMaster 4400 PT & CL','1998',''),('StairMaster 4600 PT & CL','1999',''),('StairClimber 916','2008',''),('StairClimber 5 (SC5)','2011','')])])
k['x'][0]['a']='Stepmill';k['x'][1]['a']='StairClimber'
k=K['Skipping rope'];k.pop('m',None)
k=K['Fitness trampoline']
put(k,[ent('JumpSport fitness rebounders','JumpSport','','JumpSport fitness trampoline range.',k['s'],v=[('220 Fitness Rebounder','',''),('350','','')]),
 maker('bellicon',['Bungee Rebounder'],k['s'],'rebounders','Germany'),
 maker('Needak',['Soft-Bounce'],k['s'],'rebounders','United States'),
 maker('Forza',['Exercise Trampoline 40in'],k['s'],'rebounders','France')])
# ---- strength: commodity kinds lose m
for n in ['Barbell','Weight plate','Power rack','Weight bench','Pull-up bar','Gymnastic rings','Yoga block','Foam roller','Exercise ball','Balance board','Vibration plate','Resistance band']:
    K[n].pop('m',None);K[n].pop('r',None)
k=K['Dumbbell'];k.pop('m',None)
kindfix(k,[ent('Bowflex SelectTech','Bowflex','','Selectorized adjustable dumbbells from Bowflex; the SelectTech 552 is one model.',S_BF,v=[('SelectTech 552','','')],a='')],"One entry is a named adjustable-dumbbell line sold by one maker; models are versions. Plain fixed dumbbells have no named line.",
 "Dumbbells are a commodity kind with no whole-space list. Under the icon rule only the maker line named in the brief is kept, sourced to Bowflex's own Wikipedia page, which describes its adjustable dumbbells. Covers 1 line.")
k=K['Kettlebell'];k.pop('m',None)
k['tt']=[["Competition colour (kg)",["Pink 8","Blue 12","Yellow 16","Purple 20","Green 24","Orange 28","Red 32","Grey 36","White 40","Silver 44","Gold 48"]],["Material",["Cast iron","Cast steel","Vinyl-coated","Adjustable"]]]
k['d']=k['d']+" The Russian girya, used to weigh crops in the 18th century, is the forerunner; competition bells are colour-coded by weight."
k=K['Home multi-gym']
b=k['x'][0];b['n']='Bowflex home gym';b['g']='Bowflex'
b.update({'own':'Johnson Health Tech','tier':'Independent','cty':'United States','own_y':'2024'})
put(k,[b,
 ent('Technogym Unica','Technogym','1986','Home training multistation, Technogym\'s 1986 home product.',S_TG),
 ent('Tonal','Tonal','2015','Wall-mounted electromagnetic-resistance trainer with a subscription; company founded in 2015, Tonal 2 unveiled 8 January 2025 with a built-in camera.',S_TON,v=[('Tonal','2015',''),('Tonal 2','2025','camera form coaching, drop sets, up to 250 lb')]),
 maker('Speediance',['Gym Monster'],k['s'],'home gyms'),maker('REP Fitness',['Ares 2.0'],k['s'],'home gyms','United States'),
 maker('Titan Fitness',['Functional Trainer'],k['s'],'home gyms','United States'),maker('Force USA',['G12 All-in-One Trainer','G20 Pro All-in-One Trainer'],k['s'],'home gyms'),
 maker('Major Fitness',['F22'],k['s'],'home gyms'),maker('Beyond Power',['Voltra I'],k['s'],'home gyms'),maker('MaxPRO',['SmartConnect'],k['s'],'home gyms')])
k['x'][1]['v']  # noqa
k=K['Suspension trainer']
k['x'][0].update({'g':'TRX','role':'origin'})
k['nl']="One entry is a suspension-trainer system sold under its own name; strap lengths and anchors are versions."
k['sel']="The origin of suspension training as given on Wikipedia's Suspension training page. Covers 1 system; other straps are commodity."
k['xg']='by maker'
k=K['Yoga mat']
k['x']=[ent('Hugger Mugger yoga mat','Hugger Mugger','1990s','First purpose-made yoga mat, made after imported sticky mats crumbled; Angela Farmer\'s 1982 carpet underlay was the forerunner.',WP('Yoga_mat'),role='origin')]
k['nl']="One entry is the origin product of a commodity kind."
k['sel']="Commodity kind: kept to the origin entry named on Wikipedia's Yoga mat page; no design-collection landmark was found. Covers 1 of 1."
k['xg']='by maker'
k=K['Pilates reformer']
k['x']=[ent('Universal Reformer','Joseph Pilates','','Joseph Pilates\'s original reformer, named for universally reforming the body.',WP('Pilates'),role='origin')]
k['nl']="One entry is the origin apparatus of a commodity kind."
k['sel']="Commodity kind: kept to the origin entry named on Wikipedia's Pilates page; no design-collection landmark was found. Covers 1 of 1."
k['xg']='by maker'
for kk in K.values():
    kk.pop('m',None);kk.pop('r',None)
    if kk['n'] in('Treadmill',): pass
dept_f['xg_note']=None;dept_f.pop('xg_note')
dept_f['msum']="Home fitness figures come from a credit-card-spend analysis and company pages; market-research firms give conflicting sizes, so no size is quoted."
dept_f['ms']=[
 {"mkt":"US at-home fitness spend (card data)","who":"Peloton","share":"51 %","yr":2024,"s":"https://www.earnestanalytics.com/insights/pelotons-leads-at-home-fitness","note":"up from 49 % two years earlier; the page calls the category shrinking and does not define it formally"},
 {"mkt":"US at-home fitness spend (card data)","who":"BODi","share":"11 %","yr":2024,"s":"https://www.earnestanalytics.com/insights/pelotons-leads-at-home-fitness","note":"second-largest share on the page"},
 {"mkt":"US at-home fitness spend (card data)","who":"Hydrow, Bowflex, Mirror","share":"under 2 % each","yr":2024,"s":"https://www.earnestanalytics.com/insights/pelotons-leads-at-home-fitness","note":"Rogue Fitness, iFIT, Tonal, NordicTrack and Concept2 follow Peloton and BODi on the chart, with no percentages in the text"},
 {"mkt":"Company revenue","who":"Peloton Interactive","share":"$2.491 billion","yr":2025,"s":S_PEL,"note":"infobox figure; net loss $119 million"},
 {"mkt":"Company revenue","who":"Technogym","share":"EUR 509 million","yr":2020,"s":S_TG,"note":"about 55,000 installations: 35,000 wellness centres, 20,000 homes"},
 {"mkt":"Ownership change","who":"Life Fitness","share":"$490 million","yr":2019,"s":S_LF,"note":"KPS Capital Partners bought it from Brunswick; brands include Hammer Strength and Cybex"},
 {"mkt":"Ownership change","who":"Bowflex","share":"$37.5 million","yr":2024,"s":S_BF,"note":"Johnson Health Tech bought it after the March 2024 Chapter 11 filing"},
]
dept_f['b']=dept_f['b']+[]
# ---- Athletics
k=KA['Starting block'];k.pop('m',None)
k=KA['Athletics hurdle']
k['tt']=[["Height",["110 m men 106.7 cm","100 m women 83.8 cm","400 m men 91.4 cm","400 m women 76.2 cm","Veteran men under 50 and younger boys 99.1 cm","Some youth and veteran events 68.6 cm"]]]+k['tt']
k['d']=k['d']+" Ten hurdles stand in a 110 m, 100 m or 400 m race."
k=KA['Track spike']
sp=k['x'][1]
for n,dd in [('Berserker NITRO Elite 2','throw'),('Mid Distance NITRO Elite 3','middle distance'),('Long Distance NITRO Elite 3','long distance')]:
    sp['v'].append({'n':n,'mk':'Puma','y':'','d':dd})
for e in k['x']:
    e['g']=e['mk'];b=BI[e['mk']];e['own'],e['tier'],e['cty'],_=b
k.pop('m',None)
k['nl']="One entry is a named spike family sold by one maker; event models and revisions are versions."
k['sel']="No whole-space list of track spikes exists; entries are the two families named on the cited review and Puma pages. Covers 2 families, not the whole market."
k['xg']='by maker'
STD="World Athletics throwing-implement weights as tabulated in Neuff's guide to the throwing weight rules"
k=KA['Shot put']
k['tt']=[["Men (weight and diameter)",["Senior and U23 7.26 kg, 110–130 mm","U20 6 kg, 105–125 mm","U17 and U18 5 kg, 100–120 mm","U15 and U16 4 kg, 95–110 mm","U13 and U14 3 kg, 85–110 mm"]],["Women (weight and diameter)",["Senior and U23 4 kg, 95–110 mm","U20 4 kg, 95–110 mm","U15 to U18 3 kg, 85–110 mm","U13 and U14 2.72 kg, 85–110 mm"]],["Masters men",["35–49 7.26 kg","50–59 6 kg","60–69 5 kg","70–79 4 kg","80+ 3 kg"]],["Masters women",["35–49 4 kg","50–74 3 kg","75+ 2 kg"]]]+k['tt']
k['sel']=f"Standards canon: {STD}; the weights are types, not entries."
k=KA['Discus']
k['tt']=[["Men",["Senior and U23 2 kg","U20 1.75 kg","U17 and U18 1.5 kg","U15 and U16 1.25 kg","U13 and U14 1 kg"]],["Women",["Senior to U20 1 kg","U15 to U18 1 kg","U12 to U14 0.75 kg"]],["Masters men",["35–49 2 kg","50–59 1.5 kg","60+ 1 kg"]],["Masters women",["35–74 1 kg","75+ 0.75 kg"]]]+k['tt']
k['sel']=f"Standards canon: {STD}; the weights are types. Polanik is the one maker entry, from its retailer page. Covers 1 maker line."
k['nl']="One entry is a competition discus line from one maker; weights are versions."
k['xg']='by maker'
k['x'][0]['g']='Polanik';k['x'][0].update({'own':'Polanik','tier':'Independent','cty':'Poland'})
k=KA['Javelin']
k['tt']=[["Men (weight and length)",["Senior and U23 800 g, 260–270 cm","U20 800 g, 260–270 cm","U17 and U18 700 g, 240–250 cm","U15 and U16 600 g, 220–230 cm","U14 500 g, 200–210 cm"]],["Women (weight and length)",["Senior and U20 600 g, 220–230 cm","U15 to U18 500 g, 200–210 cm","U14 and younger 400 g, 170–195 cm"]],["Masters men",["35–49 800 g","50–59 700 g","60–69 600 g","70–79 500 g","80+ 400 g"]],["Masters women",["35–49 600 g","50–74 500 g","75+ 400 g"]]]+k['tt']
k['nl']="One entry is a javelin line from one maker; weights and tips are versions."
k['sel']=f"Standards canon: {STD}; the weights are types. Entries are makers' lines from the retailer and history pages cited. Covers 3 lines."
k['xg']='by maker'
for e in k['x']:
    e['g']=e['mk']
    if e['mk'] in BI: e['own'],e['tier'],e['cty'],_=BI[e['mk']]
k['x'][1]['cty']='Sweden' if False else None
for e in k['x']:
    if e.get('cty') is None: e.pop('cty',None)
for e in k['x']:
    if e['mk']=='Nordic Sport': e['own']='Nordic Sport';e['tier']='Independent'
# hammer
hm={'n':'Hammer','a':'hammer throw','d':'Metal ball on a wire and handle thrown from a circle; 7.26 kg for senior men, 4 kg for senior women.','s':'https://www.neuff.co.uk/blogs/athletics-product-guides/throwing-weight-rules-for-shot-discus-javelin-hammer-throw',
 'tt':[["Men (weight, diameter, maximum length)",["Senior and U23 7.26 kg, 110–130 mm, 121.5 cm","U20 6 kg, 105–125 mm, 121.5 cm","U17 and U18 5 kg, 100–120 mm, 120 cm","U15 and U16 4 kg, 95–110 mm, 119.5 cm","U13 and U14 3 kg, 85–100 mm, 119.5 cm"]],["Women (weight, diameter, maximum length)",["Senior, U23 and U20 4 kg, 95–110 mm, 119.5 cm","U13 to U18 3 kg, 85–100 mm, 119.5 cm","U12 2 kg, 80–90 mm, 119.5 cm"]],["Masters men",["35–49 7.26 kg","50–59 6 kg","60–69 5 kg","70–79 4 kg","80+ 3 kg"]],["Masters women",["35–49 4 kg","50–74 3 kg","75+ 2 kg"]]]}
tf=[s for s in dept_a['s'] if s['n']=='Track & field'][0]
i=[x['n'] for x in tf['k']].index('Shot put');tf['k'].insert(i+2,hm)  # after discus? position
# order: Shot, Discus, Hammer
tf['k'].sort(key=lambda x:{'Shot put':0,'Discus':1,'Hammer':2,'Javelin':3}.get(x['n'],-1)+ (0 if x['n'] in('Shot put','Discus','Hammer','Javelin') else -10)) if False else None
# ---- dance
k=KA['Pointe shoe'];sp_=k['s']
fr=ent('Freed pointe shoe','Freed of London','1929','Handmade London turn-shoe; the company was founded in 1929 by Frederick Freed and has belonged to Onward since 1993.',WP('Freed_of_London'),g='United Kingdom',a='Freeds',v=[('Classic DV','','')],dt="maker's mark · shank · vamp")
cp=ent('Capezio Pavlova','Capezio','c. 1910','Pointe shoe Salvatore Capezio designed in honour of Anna Pavlova; Capezio was founded in New York in 1887.',WP('Capezio'),g='United States',a='The Pavlova')
bl=ent('Bloch pointe shoe','Bloch','1932','Pointe shoes made in Sydney since Jacob Bloch began in 1932; paste A, paste B and heat-moulded TMT are the box pastes.',WP('Bloch_(company)'),g='Australia',v=[('Serenade','',''),('Balance European','',''),('Elegance','',''),('Raffine','',''),('Amelie Soft','',''),('RP Collection (Russian Pointe)','2024','acquired by Bloch in January 2024')],dt='shank · width · satin colour')
gr=ent('Grishko pointe shoe','Grishko','1989','Moscow-made pointe shoes in 26 models on four lasts.',WP('Grishko'),g='Russia',a='Grishko 2007',v=[('2007 Pro','',''),('Nova 2007','',''),('DreamPointe','','on the 2007 last'),('Fouette last','',''),('Vaganova last','',''),('Elite last','','')],dt='shank · width · vamp')
gm=ent('Gaynor Minden','Gaynor Minden','1993','Pointe shoe with an injection-moulded elastomer shank and box; the company was founded by John Minden and Eliza Gaynor Minden in New York in 1993.',WP('Gaynor_Minden'),g='United States',v=[('Classic','',''),('Sculpted','','')],dt='shank stiffness · box · heel')
rp=ent('Repetto pointe shoe','Repetto','1947','French ballet shoemaker founded in 1947 by Rose Repetto, who first made shoes for her son Roland Petit.',WP('Repetto'),g='France',v=[('Alicia','',''),('Julieta','','')])
mer=maker('Merlet',['Belle S1','Cloe'],k['s'],'pointe shoes','France');mer['g']='France'
for e in (fr,cp,bl,gr,gm,rp): pass
k['x']=[fr,rp,mer,bl,gm,cp,gr]
k['x'].sort(key=lambda e:(e['g'],e['y'] or 'z',e['n']))
k.pop('m',None)
k['nl']="One entry is a pointe-shoe maker's range; lasts and models are versions."
k['sel']="No whole-space list of pointe-shoe makers exists; entries follow each maker's Wikipedia page (Freed of London, Bloch, Grishko, Gaynor Minden, Repetto, Capezio) and the retailer category page for Merlet. Covers 7 makers, not every maker."
k['xg']='by maker\'s home country'
for kn in ['Ballet shoe','Character shoe','Jazz shoe','Tap shoe']:
    KA[kn].pop('m',None)
# ---- fencing
k=KA['Fencing foil'];k.pop('m',None);k.pop('r',None)
k['x']+= [ent('Leon Paul Maraging FIE blade','Blaise Frères','','Maraging steel FIE foil blade from Blaise Frères.',k['s'],g='Blaise Frères')]
k['x'][0]['g']=k['x'][1]['g']='Leon Paul'
k['x'][1]['n']='Golubitsky-Pro blade'
k['x'][2]['n']='Blaise Frères maraging blade'
for e in k['x']:
    if e['mk']=='Leon Paul': e['own'],e['tier'],e['cty'],_=BI['Leon Paul']
k['nl']="One entry is a weapon or blade line from one maker; blade and grip variants are versions.";k['xg']='by maker'
k['sel']="No whole-space list of fencing weapons exists; entries follow the retailer and guide pages cited. Covers 3 lines."
k=KA['Fencing epee'];k.pop('r',None);k.pop('m',None)
kindfix(k,[ent('Leon Paul Mag-Tec FIE épée','Leon Paul','','Leon Paul épée line on the Mag-Tec blade.',k['s'],g='Leon Paul',v=[('Mag-Tec FIE Epee','',''),('Advanced Lightweight','',''),('Extra Reach','',''),('Project Zer0','',''),('Sub Zer0','',''),('Slimline Carbon French Grip FIE','',''),('Standard','','')])],"One entry is a weapon line from one maker; models are versions.","No whole-space list of épées exists; the entry follows Leon Paul's épée category page. Covers 1 maker line.")
k=KA['Fencing sabre'];k.pop('r',None);k.pop('m',None)
kindfix(k,[ent('Leon Paul Apex sabre','Leon Paul','','Leon Paul sabre line.',k['s'],g='Leon Paul',v=[('Apex FIE Sabre','',''),('Standard Sabre','','')])],"One entry is a weapon line from one maker; models are versions.","No whole-space list of sabres exists; the entry follows Leon Paul's sabre category page. Covers 1 maker line.")
for e in KA['Fencing sabre']['x']+KA['Fencing epee']['x']: e['own'],e['tier'],e['cty'],_=BI['Leon Paul']
k=KA['HEMA training sword'];k.pop('m',None)
H=k['s']
extra={'Fabri Armorum':['Gothic Arming Sword'],'Kingston Arms':['Practical Bastard Sword'],'Krieger Armory':['Sentry Longsword'],'Landsknecht Emporium':['Noestalgic Feder','Volker type M5C Messer Blunt Trainer'],'Viktor Berbekucz':['Gymnasium Saber','Spatulated Tip Feder'],'Chlebowski':['Standard Feder'],'Ensifer':['Ensifer Long'],'Arms & Armor':['Fechtbuch Longsword Trainer']}
for mk,ms in extra.items(): k['x'].append(maker(mk,ms,H,'HEMA trainers',None))
for e in k['x']:e['g']=e['mk']
k['nl']="One entry is a HEMA training-sword line from one maker; models are versions."
k['sel']=f"No whole-space list of HEMA trainers exists; entries follow the retailer category and maker pages cited. Covers {len(k['x'])} makers' lines."
k['xg']='by maker'
for kn,spec in {'Fencing mask':None,'Fencing jacket':None,'Fencing underarm protector':None,'Fencing glove':None,'Fencing shoe':None}.items():
    K2=KA[kn]
    m=K2.pop('m',None) or [];K2.pop('r',None)
    for e in K2.get('x',[]):
        e['g']=e['mk']
        if e['mk'] in BI: e['own'],e['tier'],e['cty'],_=BI[e['mk']]
    if kn=='Fencing mask':
        K2['x'][0]['v']+= [{'n':n,'mk':'Leon Paul','y':'','d':''} for n in ['Horizon','Arena','Club']]
    if kn=='Fencing jacket':
        lp=ent('Leon Paul jackets','Leon Paul','','Leon Paul fencing jackets.',K2['s'],v=[('Phoenix 350N Jacket','',''),('Team FIE Jacket','','')]);K2['x'].append(lp)
        K2['x'][0]['v']+=[{'n':'Lightweight Foil Lamé','mk':'Leon Paul','y':'','d':''}]
        K2['x'].append(maker('SPES',['Officer Jacket','FG Gambeson PRO 350N'],K2['s'],'HEMA jackets',None,own=False)) if False else None
        K2['x'][1]['v']+=[{'n':'Officer Jacket','mk':'SPES','y':'','d':''},{'n':'FG Gambeson PRO 350N','mk':'SPES','y':'','d':''}]
        K2['x'].append(maker('Lynx',['Lynx Jacket','Fighting Pants'],K2['s'],'HEMA clothing',None))
    if kn=='Fencing underarm protector':
        K2['x'][0]['v']+=[{'n':'Lightweight FIE Plastron','mk':'Leon Paul','y':'','d':'Leon Paul model'}]
    K2['nl']="One entry is a protective-gear line from one maker; ratings and models are versions."
    K2['sel']=f"No whole-space list of fencing protection exists; entries follow the maker, guide and retailer pages cited. Covers {len(K2['x'])} lines; loose retail models of other makers are not entries."
    K2['xg']='by maker'
for kn in ['Fencing gorget','Fencing chest protector','Fencing breeches']: KA[kn].pop('m',None)
KA['Fencing glove'].pop('m',None)
# ---- boxing
k=KA['Boxing glove'];k.pop('m',None)
cr=k['x'][0];cr['d']='Mexican glove maker; Cleto Reyes gloves are made in lace-up and hook-and-loop styles.';cr['g']='Cleto Reyes'
ev=ent('Everlast boxing gloves','Everlast','1917','Gloves from the New York brand founded in 1910 (swimwear), which began boxing gear in 1917 when Jack Dempsey asked for lasting headgear.',WP('Everlast_(brand)'),v=[('Prostyle 2','',''),('Elite ProStyle Training','',''),('Core 2','',''),('Protex','',''),('Spark Training','',''),('Titan Hybrid','','')])
win=k['x'][1];win['n']='Winning gloves';win['a']='MS-600'
tw,hb=k['x'][2],k['x'][3]
others=[maker('Ringside',['IMF Tech','Apex Flash'],k['s'],'gloves','United States'),maker('Fairtex',['BGV1'],k['s'],'gloves','Thailand'),maker('Sanabul',['Essential Gel Boxing Gloves'],k['s'],'gloves','United States'),maker('Venum',['Classic','Contender','Elite Boxing'],k['s'],'gloves'),ent('adidas boxing gloves','adidas','','adidas glove range.',k['s'],v=[('Hybrid 80','','')])]
k['x']=[cr,ev,win,tw,hb]+others
for e in k['x']:
    e['g']=e['mk']
    if e['mk'] in BI: e['own'],e['tier'],e['cty'],oy=BI[e['mk']]
    if e['mk']=='Everlast': e['own_y']='2007'
    if e['mk'] in('Hayabusa',): e['own']='Hayabusa';e['tier']='Independent'
k['nl']="One entry is a boxing-glove line from one maker; models and fastening variants are versions."
k['sel']=f"No whole-space list of boxing gloves exists; entries follow the maker and review pages cited. Covers {len(k['x'])} makers; weight classes are types."
k['xg']='by maker'
for kn in ['Punch bag','Boxing headguard']: KA[kn].pop('m',None)
KA['Punch bag']['x'][0]['g']='Everlast';KA['Punch bag']['x'][0].update({'own':'Frasers Group','tier':'Independent','cty':'United States','own_y':'2007'})
KA['Punch bag'].update({'nl':'One entry is a punch-bag line from one maker.','sel':'No whole-space list exists; the one line is from the retailer page cited. Covers 1 line.','xg':'by maker'})
# ---- budo: split uniforms
mu=KA['Martial arts uniform'];mu.pop('m',None)
ex={e['n']:e for e in mu['x']}
def mk_(e,g=None,**kw):
    e['g']=e['mk'];b=BI.get(e['mk'])
    if b:e['own'],e['tier'],e['cty'],_=b
    return e
FIT='https://www.fitshop.gr/boxing-and-martial-arts/judo-jiu-jitsu/page-2/'
my=mk_(ex['Mizuno Yusho']);my['n']='Mizuno Yusho';my['v']+= []
mz=ent('Mizuno judogi','Mizuno','','Mizuno judo uniforms for training and competition.',FIT,v=[('Shiai','',''),('Keiko','',''),('Kodomo Plus','','')])
ad=mk_(ex['adidas Champion']);ad['v']+=[{'n':'J350','mk':'adidas','y':'','d':''},{'n':'J250','mk':'adidas','y':'','d':''}]
jx=[my,mz,ad,maker('Fighterz',['Fuji','Tori Gold'],FIT,'judogi'),maker('Kappa',['Atlanta'],FIT,'judogi'),maker('Olympus Sport',['Competition 730','Nippon 2'],FIT,'judogi'),maker('Rage',['Entori'],FIT,'judogi')]
for e in jx:e['g']=e['mk']
mu['n']='Judogi';mu['a']='judo uniform · keikogi';mu['d']='Judo uniform of a heavy jacket, canvas trousers and an obi belt; Kano Jigoro derived it from the kimono around 1900.'
mu['s']='https://en.wikipedia.org/wiki/Judogi'
mu['x']=jx
mu['tt']=[["Weave",["Single weave (about 300–550 g/m²)","Double weave (about 650–1050 g/m²)"]],["Colour",["White","Blue (competition)"]],["Belt (obi) rank",["White","Yellow","Orange","Green","Blue","Brown (kyu grades)","Black (1st–5th dan)","Red and white or red (higher dan)"]],["Approval",["IJF competition","Club"]]]
mu['nl']="One entry is a judo-uniform line from one maker; models and weights are versions."
mu['sel']="No whole-space list of judogi exists; entries follow the Wikipedia Judogi page for the garment and the retailer category page for makers. Covers 7 makers; belt colours are types."
mu['xg']='by maker'
kg={'n':'Karate gi','a':'karategi','d':'Karate uniform, a lighter weave than the judogi with strings to hold the jacket closed.','s':'https://en.wikipedia.org/wiki/Gi_(clothing)','x':[mk_(ex['Tokaido karategi']),mk_(ex['Shureido K-10'])],
 'tt':[["Weave",["Single","Double","Gold","Platinum"]],["Belt (obi) rank",["Colours differ by style","Kyokushin adds a stripe per dan on the black belt","Shito-ryu uses dark blue for 10th–15th dan"]],["Colour",["White","Black","Blue","Indigo"]]],
 'nl':'One entry is a karate-uniform line from one maker; models are versions.','sel':'No whole-space list of karate gi exists; the two lines are from the maker and forum pages cited. Covers 2 lines.','xg':'by maker'}
kg['x'][0]['n']='Tokaido karate gi'
db={'n':'Taekwondo dobok','a':'dobok','d':'Korean martial-arts uniform; World Taekwondo uses a V-neck jacket, ITF-style jackets close vertically.','s':'https://en.wikipedia.org/wiki/Dobok',
 'tt':[["Jacket style",["World Taekwondo V-neck","Traditional cross-over","ITF-style vertical closing"]],["Belt (tti) rank",["White","Yellow","Orange","Green","Blue","Purple","Red","Brown","Black (dan)"]],["Colour",["White","Black"]]]}
bj={'n':'Brazilian jiu-jitsu gi','a':'BJJ gi','d':'Jiu-jitsu uniform, lighter than a judogi with tighter cuffs so an opponent has less fabric to grab.','s':'https://en.wikipedia.org/wiki/Brazilian_jiu-jitsu',
 'tt':[["Weave",["Single","Double","Gold","Platinum"]],["Adult belt",["White","Blue","Purple","Brown","Black","Black and red (7th degree)","Red and white (8th degree)","Red (9th–10th degree)"]],["Youth belt",["White","Grey","Yellow","Orange","Green"]]]}
si=[s for s in dept_a['s'] if s['n']=='Budo & martial arts'][0]
i=si['k'].index(mu);si['k'][i+1:i+1]=[kg,db,bj]
for kn in ['Kendo armour','Shinai','Bokken','Iaito']:KA[kn].pop('m',None)
KA['Iaito']['x'][0]['g']='Minosaka'
dept_a['note']=dept_a['note']
dept_a['ax']=dept_a['ax']
out={'replaces':['Fitness & home gym','Athletics, dance & combat'],'depts':[dept_f,dept_a],'renames':{'Martial arts uniform':'Judogi'},'moves':[]}
# brands
newb=[];upd={}
used={}
def walk(d):
    for s in d['s']:
        for k in s['k']:
            for e in k.get('x',[]) or []:
                used[e['mk']]=e
for d in out['depts']:walk(d)
for mk,e in used.items():
    if not mk:continue
    if mk in reg:
        if mk in BI:
            b=BI[mk];upd[mk]={'own':b[0],'tier':b[1],'c':b[2]}
    else:
        nb={'n':mk,'c':e.get('cty',''),'f':'','seg':'Mainstream','kf':'fitness and combat equipment','d':f"Maker named on the retailer pages cited for {mk} entries.",'s':e['s']}
        newb.append(nb)
for own in {b[0] for b in BI.values()}:
    if own not in reg and own not in used and own not in {x['n'] for x in newb}:
        newb.append({'n':own,'c':'','f':'','seg':'Mainstream','kf':'owner company','d':'Current owner of brands in Fitness and Combat entries.','s':S_PEL if own=='Peloton Interactive' else WP('Life_Fitness') if own.startswith('KPS') else S_BF if own.startswith('Johnson') else 'https://en.wikipedia.org/wiki/Everlast_(brand)' if own.startswith('Frasers') else S_NT if own.startswith('iFIT') else S_SM if own.startswith('Core') else WP('Freed_of_London')})
out['brands']=newb;out['brand_updates']=upd
os.makedirs('/home/user/Possession-Taxonomy/rebuild/out/E2_parts',exist_ok=True)
json.dump(out,open('/home/user/Possession-Taxonomy/rebuild/out/E2_parts/FIT.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace('/home/user/Possession-Taxonomy/rebuild/out/E2_parts/FIT.json.tmp','/home/user/Possession-Taxonomy/rebuild/out/E2_parts/FIT.json')
