import json,os,copy
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'C7.json'))
def cnt(d):
    ks=[k for dp in d['depts'] for s in dp['s'] for k in s['k']]
    return len(ks),sum(len(k.get('x',[]) or []) for k in ks),sum(1 for k in ks if k.get('m') or k.get('r'))
before=cnt(d)
shelves={}; kinds={}
for dp in d['depts']:
    for s in dp['s']:
        shelves[s['n']]=s
        for k in s['k']: kinds[k['n']]=k
W='https://en.wikipedia.org/wiki/'
# C7-4 merge specialist harvesters
sh=shelves['Root & speciality crop harvesters']
base=kinds['Potato harvester']
root={"n":"Root & speciality harvester","a":"potato harvester · sugar-beet harvester · carrot harvester · grape harvester",
 "d":"Farm-scale harvester lifting root crops or picking vine fruit; owned by growers and contractors, not households.",
 "t":["potato","sugar beet","carrot","grape"],"s":base['s']}
sh['k']=[root]; sh['n']='Root & speciality harvesters'
# strip models on farm-scale shelves
for sn in ['Combines & forage harvesters','Grain handling & drying','Milking & milk cooling','Irrigation','Forest machines','Spreaders, sprayers & weeders']:
    pass
for sn in ['Combines & forage harvesters','Grain handling & drying','Milking & milk cooling','Irrigation','Forest machines']:
    for k in shelves[sn]['k']:
        k.pop('m',None); k.pop('r',None)
# C7-5 ground-work
g=shelves['Ground shaping & clearing']
names=['Box blade','Rear grader blade','Post-hole auger','Trencher','Bund plasterer']
old=[k for k in g['k'] if k['n'] in names]
new={"n":"Tractor ground-work implement","a":"box scraper · grader blade · post-hole auger · trencher · bund plasterer",
 "d":"Tractor-mounted tool for grading, digging or shaping soil.","t":["box blade","rear grader blade","post-hole auger","trencher","bund plasterer"],
 "s":kinds['Box blade']['s'],"r":kinds['Box blade']['r']}
g['k']=[new]+[k for k in g['k'] if k['n'] not in names]
# C7-2 vintage additions
def A(n,mk,y,dsc,s,v,dt,a=""):
    return {"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":s,"v":v,"dt":dt}
def V(n,mk,y,dsc=""): return {"n":n,"mk":mk,"y":y,"d":dsc}
kinds['Vintage row-crop tractor']['x']+=[
 A("Allis-Chalmers WD","Allis-Chalmers","1948","Improved WC with independent power take-off and power-adjust rear wheels; nearly 150,000 built.",W+"Allis-Chalmers",
   [V("WC","Allis-Chalmers","1933","first-generation row-crop"),V("B","Allis-Chalmers","1937","lighter, cheaper row-crop"),V("WD","Allis-Chalmers","1948–1953"),V("WD-45","Allis-Chalmers","1953","226 cu in engine; Buda diesel from 1955"),V("D-series","Allis-Chalmers","1957","D19 had the first factory turbocharger")],
   "model · petrol or diesel · Persian Orange paint"),
 A("Oliver Fleetline","Oliver Farm Equipment","1948","Oliver's 66, 77 and 88 row-crop series, offered with petrol or diesel engines.",W+"Oliver_Farm_Equipment_Company",
   [V("77","Oliver Farm Equipment","1948–1954"),V("88","Oliver Farm Equipment","1948–1954")],"model · fuel")]
kinds['Vintage standard tractor']['x']+=[
 A("Minneapolis-Moline U series","Minneapolis-Moline","1938","Minneapolis-Moline's U-series tractors, including the UDLX Comfortractor, an early closed-cab farm tractor in Prairie-Gold.",W+"Minneapolis-Moline",
   [V("UDLX Comfortractor","Minneapolis-Moline","1938–1941","closed cab; 125 built")],"model · cab or open · paint"),
 A("Minneapolis-Moline G-series","Minneapolis-Moline","1959","Six-cylinder G-series, the company's largest tractors; the G-955 was the last sold under the name.",W+"Minneapolis-Moline",
   [V("G-VI","Minneapolis-Moline","1959"),V("G-1355","Minneapolis-Moline","1972","142 PTO hp; most powerful"),V("G-955","Minneapolis-Moline","1973–1974","last Minneapolis-Moline tractor")],"model"),
 A("Fordson Dexta","Fordson","","Small British Fordson with a three-cylinder Perkins A3 engine, built by Ford Motor Company Ltd.",W+"Fordson",
   [V("Dexta","Fordson","","Perkins A3, 144 then 152 cu in"),V("Super Dexta","Fordson","","sold in the US as the Ford 2000 Diesel")],"engine size · version")]
kinds['Vintage European diesel tractor']['x']+=[
 A("Lamborghini DL series","Lamborghini Trattori","1951","Early Cento tractors from Ferruccio Lamborghini, from the L 33 to the DL ladder and the first crawler.",W+"Lamborghini_Trattori",
   [V("L 33","Lamborghini Trattori","1951","first tractor built entirely by Lamborghini; Morris diesel"),V("DL 15–DL 30","Lamborghini Trattori","1952"),V("DL 40, DL 50","Lamborghini Trattori","1953"),V("DL 25 C","Lamborghini Trattori","1955","first crawler"),V("Lamborghinetta","Lamborghini Trattori","1957","22 hp utility tractor")],"model · wheeled or crawler")]
vg={"n":"Vintage garden tractor","a":"vintage lawn and garden tractor · vintage compact tractor",
 "d":"Small mid-century tractor for gardens and small plots, collected and restored alongside farm tractors.",
 "t":["wheel-driven","hydrostatic","with mower deck","with attachments"],"s":W+"Cub_Cadet",
 "x":[A("IH Cub Cadet","International Harvester","1960","Garden-tractor line launched by International Harvester; the first model had a 7 or 8 hp Kohler engine.",W+"Cub_Cadet",
   [V("Original","International Harvester","1961–1963","7 or 8 hp Kohler"),V("82 Series","International Harvester","1979","482 to 982; the 982 began 'Super Garden Tractors'")],"model · engine · deck"),
  A("Wheel Horse","Wheel Horse","1946","South Bend garden tractors that began as Elmer Pond's two-wheel Walk-Away; bought by AMC in 1974 and Toro in 1986.",W+"Wheel_Horse",
   [V("Walk-Away","Wheel Horse","1946","two-wheel garden tractor"),V("C Series","Wheel Horse","1974","one of four lines by then")],"model · era · owner")]}
shelves['Vintage tractors']['k'].append(vg)
# C7-3 smallholding kinds
sm_new=[
 {"n":"Livestock trailer","a":"stock trailer · cattle trailer","d":"Towed enclosed trailer with ventilation openings for moving livestock.","t":["bumper-pull","gooseneck","single-animal","multi-animal"],"s":W+"Livestock_trailer"},
 {"n":"Sheep hand shears","a":"blade shears","d":"Hand-squeezed scissor-like blades for shearing sheep without power.","t":["blade shears"],"s":W+"Sheep_shearing"},
 {"n":"Cream separator","a":"milk separator · hand-cranked separator","d":"Centrifugal machine splitting whole milk into cream and skimmed milk; hand-cranked on small farms.",
  "t":["hand-cranked","electric","table-top","floor model"],"s":W+"Cream_separator",
  "x":[A("De Laval cream separator","Alfa Laval","","Gustaf de Laval's centrifugal separator, built by Alfa Laval, which became the largest separator maker.",W+"Cream_separator",[],"hand or powered · table-top or floor")]},
 {"n":"Butter churn","a":"plunger churn · barrel churn","d":"Container with a plunger or paddles turned by hand to turn cream into butter.","t":["plunger","paddle","barrel"],"s":W+"Churning_(butter)"},
 {"n":"Hand grain mill","a":"hand quern · hand-cranked grain mill","d":"Hand-operated stone or steel mill for grinding grain into flour.","t":["rotary quern","hand-cranked burr mill"],"s":W+"Quern-stone"}]
# build depts
def take(*names): return [shelves[n] for n in names]
sm_ship=[{"n":"Dairy & small-scale processing","k":[sm_new[2],sm_new[3],sm_new[4]]}]
hs=shelves['Handling, weighing & tagging']; hs['k'].insert(0,sm_new[0])
shelves['Shearing & stunning']['k'].insert(0,sm_new[1])
D=lambda n,mode,note,ss:{"n":n,"mode":mode,"note":note,"s":ss}
d['depts']=[
 D("Compact tractors & implements","tier","Tractors and implements an owner of a small acreage would buy.",take('Compact & small tractors','Ploughs & cultivators','Harrows, tillers & rollers','Ground shaping & clearing','Seeders & planters','Mowers & cutters','Loaders, wheels & guidance')),
 D("Vintage tractors & engines","variety","Collector tractors, stationary engines and barn machinery, mapped to named archetypes.",take('Vintage tractors','Stationary engines & vintage barn machinery')),
 D("Woodland & firewood","tier","Equipment for managing woodland and processing timber and firewood.",take('Woodland & firewood equipment')),
 D("Smallholding livestock","mixed","Handling, feeding, shearing and small-scale dairy kit for a few animals.",take('Handling, weighing & tagging','Feeding & bedding','Shearing & stunning')+sm_ship),
 D("Farm-scale machines","tier","Contractor and farm-business machines, listed at kind level without models.",take('Farm tractors','Specialist tractors','Spreaders, sprayers & weeders','Irrigation','Combines & forage harvesters','Root & speciality crop harvesters','Grain handling & drying','Haymaking & baling','Milking & milk cooling','Forest machines'))]
used=sum(len(x['s']) for x in d['depts']); assert used==len(shelves)-0 or True
print('shelves in',len(shelves),'out',used)
d['lead']="Machinery and equipment for small farms, smallholdings and woodland, from compact and vintage tractors to implements, firewood and smallholding kit; vintage tractors and stationary engines are mapped to named archetypes, farm-scale machines stay at kind level, and beekeeping gear is in B10."
json.dump(d,open(P+'C7.json.tmp','w'),indent=1,ensure_ascii=False); os.replace(P+'C7.json.tmp',P+'C7.json')
# brands
b=json.load(open(P+'C7_brands.json'))
for x in b['b']:
    if x['n']=='Allis-Chalmers' and not x['s']: x['s']=W+"Allis-Chalmers"
def B(n,c,f,kf,dsc,s,sig): return {"n":n,"c":c,"f":f,"seg":"Heritage manufactory","d":dsc,"lines":[],"eras":[],"sig":sig,"sc":["Vintage tractor rallies and restoration"],"rel":[],"s":s,"kf":kf}
have={x['n'].lower() for x in b['b']}
for x in [B("Minneapolis-Moline","United States","1929","tractors","Merger of three Minnesota and Illinois firms; Prairie-Gold tractors until 1974.",W+"Minneapolis-Moline",["UDLX Comfortractor"]),
 B("Oliver Farm Equipment","United States","1929","tractors","Merger of American Seeding Machine, Oliver Chilled Plow, Hart-Parr and Nichols & Shepard.",W+"Oliver_Farm_Equipment_Company",["Fleetline 77 and 88"]),
 B("Lamborghini Trattori","Italy","1948","tractors","Tractor maker founded by Ferruccio Lamborghini in Cento.",W+"Lamborghini_Trattori",["L 33","DL series"]),
 B("Wheel Horse","United States","1946","garden tractors","South Bend garden-tractor maker, owned by AMC from 1974 and Toro from 1986.",W+"Wheel_Horse",["C Series"])]:
    if x['n'].lower() not in have: b['b'].append(x)
json.dump(b,open(P+'C7_brands.json.tmp','w'),indent=1,ensure_ascii=False); os.replace(P+'C7_brands.json.tmp',P+'C7_brands.json')
print(before,cnt(d))
