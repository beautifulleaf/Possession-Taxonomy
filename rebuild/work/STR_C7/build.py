import json,os,shutil
R='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open(R+'work/STR_C7/bak/C7.json'))
K={}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
before=(len(old['depts']),sum(len(d['s']) for d in old['depts']),len(K),sum(len(k.get('x',[])) for k in K.values()))

TT={
'Sub-compact tractor':[["Transmission",["Hydrostatic","Gear"]],["Protection",["Open with ROPS","Cab"]],["Fitted with",["Front loader","Backhoe (TLB)"]],["Origin",["New","Japanese grey import"]]],
'Compact tractor':[["Transmission",["Hydrostatic","Gear or shuttle"]],["Drive",["2WD","4WD"]],["Protection",["Open with ROPS","Cab"]],["Fitted with",["Front loader","Backhoe (TLB)"]],["Origin",["New","Japanese grey import"]]],
'Utility tractor':[["Drive",["2WD","4WD (MFWD)"]],["Transmission",["Shuttle","Powershift or CVT"]],["Protection",["Open with ROPS","Cab"]],["Fitted with",["Front loader"]]],
'Two-wheel tractor':[["Machine",["Power tiller (fixed rotary tiller)","PTO walking tractor"]],["Fuel",["Petrol","Diesel"]],["Drive",["Gear","Hydrostatic"]],["Operator position",["Walk-behind","With riding sulky"]]],
'Mouldboard plough':[["Mounting",["Mounted","Semi-mounted"]],["Turning",["Conventional","Reversible"]]],
'Chisel and tine cultivator':[["Tine",["Rigid","Spring"]]],
'Disc harrow':[["Layout",["Compact disc","Tandem disc"]]],
'Land roller':[["Roller type",["Flat","Ring","Packer"]]],
'Tractor ground-work implement':[["Tool",["Box blade","Rear grader blade","Post-hole auger","Trencher","Bund plasterer"]]],
'Stone picker':[["Machine",["Stone picker","Stone windrower"]]],
'Tractor snow blade and blower':[["Tool",["Snow blade","Snow blower"]]],
'Seed drill':[["Coulter",["Tine","Disc"]],["Sowing method",["Conventional","No-till"]]],
'Rice transplanter':[["Operator position",["Walk-behind","Ride-on"]]],
'Disc mower':[["Cutter",["Disc","Drum"]],["Conditioning",["Plain","With conditioner"]],["Mounting",["Front-mounted","Rear-mounted","Trailed"]]],
'Rotary cutter':[["Deck",["Single-spindle","Flex-wing"]]],
'Loader attachment':[["Tool",["Bucket","Pallet forks","Bale spike","Grab"]]],
'Tractor tyre and wheel':[["Part",["Tyre","Rim","Complete wheel"]],["Fitting",["Single","Dual"]]],
'Tractor ballast weight':[["Position",["Wheel weight","Front ballast weight"]]],
'Guidance and auto-steer system':[["Part",["Receiver","Display","Auto-steer kit"]]],
'Livestock trailer':[["Hitch",["Bumper-pull","Gooseneck"]],["Capacity",["Single-animal","Multi-animal"]]],
'Cattle crush':[["Restraint",["Headgate only","Full crush","Hoof-trimming crush"]]],
'Cattle race and handling system':[["Part",["Race","Forcing pen","Circular tub"]]],
'Sheep handler':[["Operation",["Manual handler","Auto handler","Auto drafter"]]],
'Livestock scales':[["Part",["Load bars","Platform","Indicator"]]],
'Livestock EID reader':[["Form",["Stick reader","Panel reader"]]],
'Feed mixer wagon':[["Mixing",["Vertical auger","Horizontal auger","Reel"]],["Power",["Trailed","Self-propelled"]]],
'Shearing machine':[["Drive",["Overhead drive","Portable"]]],
'Captive-bolt stunner':[["Bolt",["Penetrating","Non-penetrating"]]],
'Cream separator':[["Drive",["Hand-cranked","Electric"]],["Placement",["Table-top","Floor model"]]],
'Butter churn':[["Mechanism",["Plunger","Paddle","Barrel"]]],
'Hand grain mill':[["Mechanism",["Rotary quern","Hand-cranked burr mill"]]],
'Row-crop tractor':[["Drive",["Two-wheel drive","Mechanical front-wheel drive"]]],
'Crawler tractor':[["Track",["Rubber-belted","Steel-tracked"]]],
'Four-track tractor':[["Frame",["Articulated","Rigid"]]],
'Orchard and vineyard tractor':[["Crop",["Vineyard (V)","Orchard (F)","Plantation (P)"]]],
'Fertiliser spreader':[["Spreading",["Twin-disc","Pneumatic boom"]]],
'Manure spreader':[["Beater",["Vertical","Horizontal"]],["Discharge",["Side discharge"]]],
'Slurry injector':[["Tool",["Disc","Tine"]]],
'Crop sprayer':[["Carriage",["Mounted","Trailed","Self-propelled"]]],
'Inter-row hoe and tine weeder':[["Tool",["Tine weeder","Inter-row hoe"]]],
'Centre-pivot and linear irrigator':[["Movement",["Centre pivot","Linear move"]]],
'Irrigation pump':[["Power",["PTO-driven","Engine-driven","Electric"]]],
'Combine harvester':[["Threshing",["Conventional (straw walker)","Axial rotor","Hybrid","Head-feeding"]]],
'Combine header':[["Header",["Grain","Draper","Corn","Pick-up"]]],
'Forage harvester':[["Power",["Self-propelled","Trailed"]]],
'Root & speciality harvester':[["Crop",["Potato","Sugar beet","Carrot","Grape"]]],
'Grain auger and conveyor':[["Mover",["Tube auger","Belt conveyor","Chain conveyor","Bucket elevator (grain leg)"]]],
'Grain dryer':[["Design",["Tower","Mixed-flow","Batch"]]],
'Hay tedder':[["Carriage",["Mounted","Trailed"]]],
'Hay rake':[["Rake",["Rotary rake","Wheel rake","Belt merger"]]],
'Baler':[["Bale shape",["Round","Large square","Small square"]]],
'Bale wrapper':[["Wrap",["Round-bale","Square-bale","In-line"]]],
'Milking parlour':[["Layout",["Static (herringbone, parallel)","Rotary","Trigon","Polygon","Pipeline in stalls"]]],
'Bulk milk cooling tank':[["Lid",["Open","Closed"]]],
'Forest harvester':[["Chassis",["Wheeled","Tracked","Harwarder"]],["Processing",["Harvester head","Delimber"]]],
'Skidder':[["Pulling",["Cable","Grapple"]]],
'Feller buncher':[["Reach",["Drive-to-tree","Swing-boom"]]],
'Forestry crane and grapple':[["Mounting",["Forwarder or trailer crane","Knuckleboom loader"]],["Tool",["Grapple and rotator"]]],
'Forestry winch':[["Drive",["Mechanical (PTO, cable brake)","Electro-hydraulic"]],["Drums",["Single drum","Double drum"]],["Control",["Manual","Radio-controlled"]]],
'Timber trailer with crane':[["Frame",["Single frame","Double frame"]],["Axle",["Tandem bogie","Hydraulic drive"]],["Crane tool",["Rotator and grapple"]],["Hydraulics",["Own pump","Tractor hydraulics"]]],
'Tractor wood chipper':[["Rotor",["Disc","Drum"]],["Feed",["Gravity","Hydraulic roller"]]],
'Tractor log splitter':[["Position",["Vertical","Horizontal"]],["Power",["PTO pump","Tractor hydraulics"]],["Mounting",["Three-point mounted"]]],
'Firewood processor':[["Saw",["Circular saw","Chainsaw bar"]],["Drive",["PTO","Electric","PTO and electric combi"]],["Carriage",["Mobile (road trailer)"]],["Outfeed",["With outfeed conveyor"]]],
'Portable sawmill':[["Mill type",["Band sawmill (manual)","Band sawmill (hydraulic)","Chainsaw frame mill","Alaskan-type chainsaw jig"]],["Fitting",["Trailer-mounted","Wide-slab"]]],
'Stump grinder':[["Carriage",["Walk-behind","Tracked self-propelled","Tractor PTO","Towable"]]],
'Forestry mulcher':[["Carrier",["Tractor PTO","Skid-steer or excavator mounted"]],["Teeth",["Fixed teeth","Swinging hammers"]]],
'Early tractor (pre-1930)':[["Wheels",["Steel wheels"]],["Fuel",["Kerosene","Petrol"]],["Cylinders",["Single-cylinder","Two-cylinder","Four-cylinder"]]],
'Vintage row-crop tractor':[["Front end",["Narrow (tricycle)","Single front wheel","Wide front"]],["Clearance",["High-crop"]],["Finish",["Unstyled","Styled"]]],
'Vintage standard tractor':[["Fuel",["Petrol","TVO / paraffin","Lamp oil","Diesel"]],["Build",["Vineyard or narrow","Industrial"]]],
'Hot-bulb and semi-diesel tractor':[["Starting",["Blowlamp","Cartridge","Electric"]],["Wheels",["Steel wheels","Rubber tyres"]]],
'Vintage European diesel tractor':[["Cooling",["Air-cooled","Water-cooled"]],["Cylinders",["Single-cylinder","Multi-cylinder"]],["Width",["Narrow or vineyard"]]],
'Vintage crawler tractor':[["Power",["Steam","Petrol","Diesel"]],["Running gear",["Tiller wheel","Fully tracked"]]],
'Steam traction and ploughing engine':[["Build and use",["General-purpose (agricultural)","Ploughing engine (pairs)","Road locomotive","Showman's engine","Steam roller","Steam tractor","Portable engine"]],["Expansion",["Single-cylinder","Compound"]]],
'Vintage garden tractor':[["Drive",["Wheel-driven","Hydrostatic"]],["Fitted with",["Mower deck","Attachments"]]],
'Hit-and-miss engine':[["Layout",["Horizontal","Vertical"]],["Cooling",["Hopper-cooled","Tank-cooled","Air-cooled"]],["Cylinder head",["Headless","Headed"]],["Fuel",["Kerosene","Petrol (gasoline)","Gas"]]],
'Throttle-governed stationary engine':[["Fuel",["Petrol/paraffin","Diesel"]],["Cooling",["Air-cooled","Water-cooled (hopper)"]],["Crank",["Open crank","Enclosed crank"]],["Mounting",["Portable on trolley"]]],
'Hot-bulb stationary engine':[["Cycle",["Four-stroke","Two-stroke (crankcase-scavenged)"]],["Use",["Stationary","Marine"]],["Cylinders",["Single-cylinder","Multi-cylinder"]]],
'Threshing machine':[["Power",["Hand or horse-powered","Steam-driven","Tractor belt-driven"]],["Siting",["Stationary barn thresher","Portable threshing drum"]]],
'Horse-drawn implement':[["Implement",["Plough","Reaper","Reaper-binder","Mower","Hay rake","Tedder","Roller","Cart"]]],
}

SU='https://en.wikipedia.org/wiki/'
NEW={
'Sickle-bar mower':dict(n='Sickle-bar mower',a='finger-bar mower · cutter bar mower',d='Mower whose back-and-forth sickle slides between fixed finger guards on a long bar, the older cutter for hay and rough grass.',s=SU+'Sickle_bar_mower',tt=[["Carriage",["Tractor-mounted","Walk-behind","Horse-drawn"]]]),
'Hedge cutter':dict(n='Hedge cutter',a='boom hedge trimmer · tractor hedgecutter',d='Hydraulic boom arm carrying a hedge-trimming head, fitted to a tractor; a reach flail mower is a different machine.',s=SU+'Hedge_trimmer',tt=[["Cutting head",["Flail","Cutter bar"]]],see=[["C2","Hedge trimmer","hand-held garden version"]]),
'Windrower':dict(n='Windrower',a='swather · mower-conditioner windrower',d='Machine that cuts hay or small grain and lays it in rows to dry, self-propelled or driven from a tractor.',s=SU+'Windrower',tt=[["Power",["Self-propelled","Tractor PTO-driven"]],["Cutter",["Sickle bar","Rotating discs"]]]),
'Chaff cutter':dict(n='Chaff cutter',a='chaff box · straw chopper',d='Machine that chops straw or hay into short lengths so animals can digest it, turned by hand or driven by belt or tractor.',s=SU+'Chaff_cutter'),
'Vintage combine harvester':dict(n='Vintage combine harvester',a='header-harvester · antique combine',d='Early grain harvester that reaps and threshes in one pass, from horse-drawn machines to the first self-propelled models.',s=SU+'Combine_harvester',
  tt=[["Power",["Horse-drawn","Tractor-drawn","Self-propelled"]]],
  x=[
  dict(n='Sunshine Header-Harvester',a='Sunshine Harvester',d="Hugh Victor McKay's commercial Australian combine, an early header-harvester sold in numbers.",mk='H. V. McKay',y='1885',s=SU+'Combine_harvester',v=[],dt='horse-drawn · header type'),
  dict(n='Holt self-propelled harvester',a='',d="Holt Manufacturing's self-propelled combine from California.",mk='Holt',y='1911',s=SU+'Combine_harvester',v=[],dt='steam or petrol drive · rare survivors'),
  dict(n='Gleaner self-propelled harvester',a='Gleaner Baldwin combine',d="The Baldwin brothers' self-propelled combine, built with the Gleaner Manufacturing Company in Kansas.",mk='Gleaner Manufacturing Company',y='1923',s=SU+'Combine_harvester',v=[],dt='model · condition and originality'),
  dict(n='Massey-Harris self-propelled combine',a='Massey-Harris No. 20',d="Massey-Harris's self-propelled grain combine designed by Thomas Carroll.",mk='Massey-Harris',y='1937–1940',s=SU+'Combine_harvester',v=[],dt='model · cutting width'),
  dict(n='Claas Hercules',a='',d="Claas's self-propelled combine of 1953.",mk='Claas',y='1953',s=SU+'Combine_harvester',v=[],dt='model · condition and originality'),
  ]),
}
SEE={
'Tractor log splitter':[["C1","Log splitter","hand and engine splitters"]],
'Tractor wood chipper':[["C2","Wood chipper","garden-scale chipper"]],
'Tractor snow blade and blower':[["C2","Snow blower","walk-behind version"]],
'Rotary tiller':[["C2","Garden tiller","walk-behind garden version"]],
'Two-wheel tractor':[["C2","Garden tiller","lighter garden tiller"]],
'Flail mower':[["C2","Hedge trimmer","hand-held hedge cutters"]],
'Forestry winch':[["C1","Winch","hand and vehicle winches"]],
'Crop sprayer':[["C2","Garden sprayer","hand-pumped garden version"]],
'Irrigation pump':[["C1","Surface pump","site and garden pumps"]],
'Livestock trailer':[["G1","Utility trailer","general towed trailer"]],
'Rotary cutter':[["C4","Rotary cutter","different object: fabric cutting wheel"]],
'Vintage garden tractor':[["C2","Riding mower","current lawn tractor"]],
'Hit-and-miss engine':[["E1","Model engine","scale working models"]],
}

def kind(n):
    k=json.loads(json.dumps(K[n])) if n in K else json.loads(json.dumps(NEW[n]))
    if n in TT: k['tt']=TT[n]
    k.pop('t',None) if 'tt' in k or n=='Sheep hand shears' else None
    if n in SEE: k['see']=SEE[n]
    return k
def shelf(n,t,ax,names):
    sh={"n":n,"t":t}
    if len(names)>3: sh["ax"]=ax
    elif ax: sh["ax"]=ax
    sh["k"]=[kind(x) for x in names]; return sh

D=[]
D.append({"n":"Tractors & tractor fittings","mode":"tier","note":"Tractors for a small acreage, a farm or a special crop, and what is fitted to their wheels and steering.","b":[],
 "t":"Wheeled and tracked tractors and walking tractors, with the tyres, tracks, weights and guidance fitted to them; a tractor kept for restoring or showing → Vintage tractors & engines; a garden lawn tractor → C2.",
 "ax":"What work is the tractor built for: a small acreage, field farming or a special crop or terrain, or is it a fitting for any of them?",
 "s":[
 shelf("Small-acreage tractors","Tractors sized for homeowners and smallholders, from sub-compact and compact tractors to utility tractors and walking tractors; farm-scale models → Farm tractors.","kinds by power and layout, smallest first",["Sub-compact tractor","Compact tractor","Utility tractor","Two-wheel tractor"]),
 shelf("Farm tractors","Large tractors for field farming, such as row-crop, articulated four-wheel-drive and tracked tractors; smaller models → Small-acreage tractors.","kinds by how the tractor puts power on the ground: wheels, bending frame, tracks",["Row-crop tractor","Articulated 4WD tractor","Crawler tractor","Four-track tractor","Half-track tractor"]),
 shelf("Specialist tractors","Tractors built for one crop, terrain or job, such as orchard and vineyard tractors, slope tractors and forestry tractors; general-purpose models → Farm tractors.","kinds by where the tractor works: orchard rows, vine rows, slopes, forest, or as an implement carrier",["Orchard and vineyard tractor","High-clearance tractor","Slope tractor","Forestry tractor","Implement carrier"]),
 shelf("Tractor wheels, weights & guidance","Parts fitted to a tractor to change its grip, weight or steering: tyres and wheels, rubber track units, ballast weights, auto-steer kits.","kinds by what they change: ground contact, weight, steering",["Tractor tyre and wheel","Rubber track unit","Tractor ballast weight","Guidance and auto-steer system"]),
 ]})
D.append({"n":"Loaders & earthmoving","mode":"tier","note":"Machines and tools that lift loads or move and shape earth.","b":[],
 "t":"Loaders, diggers and ground-shaping tools used on a smallholding; a combine or crop machine → Field implements & crop machines; a tree-clearing machine → Woodland & firewood.",
 "ax":"What does the lifting or digging: a loader on the front of a tractor, a separate earthmoving machine, or a blade or tool towed behind?",
 "s":[
 shelf("Tractor loaders","Loader arms that fit the front of a tractor and the tools that fit them: front-end loaders, buckets, pallet forks, bale spikes; a separate loader → Earthmoving & handling machines.","kinds by what is fitted: the loader frame, then its tools",["Front-end loader","Loader attachment"]),
 shelf("Earthmoving & handling machines","Self-propelled machines that dig or lift: skid steers, backhoe loaders, excavators and telehandlers; a loader fitted to a tractor → Tractor loaders.","kinds by what does the work: skidding loader, loader with digging arm, digger, telescopic boom",["Skid steer","Backhoe loader","Excavator","Telehandler"]),
 shelf("Ground-shaping implements","Tools towed or carried behind a tractor to level, clear or shape ground: box blades, graders, stone pickers, snow blades and blowers.","kinds by the job on the ground: grade and dig, pick stones, clear snow",["Tractor ground-work implement","Stone picker","Tractor snow blade and blower"]),
 ]})
D.append({"n":"Field implements & crop machines","mode":"tier","note":"Implements and machines in the order of the crop year: ground, sowing, crop care, grass, harvest.","b":[],
 "t":"Machines that work the soil, sow, feed and protect crops, cut and bale grass, harvest and handle grain; a tractor loader → Loaders & earthmoving, an animal-feeding machine → Smallholding livestock.",
 "ax":"Which job in the crop year does it do: prepare the ground, sow, feed and protect the crop, cut and make hay, or harvest and store?",
 "s":[
 shelf("Ploughs & cultivators","Implements that turn or loosen the soil before sowing: mouldboard ploughs, spading machines, tine cultivators, subsoilers; surface breaking → Harrows, tillers & rollers.","kinds by what they do to the soil: turn it, dig it, loosen it, break the subsoil",["Mouldboard plough","Spading machine","Chisel and tine cultivator","Subsoiler"]),
 shelf("Harrows, tillers & rollers","Implements that break clods and firm the surface into a seedbed: disc and power harrows, rotary tillers, rollers, combination units.","kinds by how they treat the surface: cut with discs, break with tines, churn with a rotor, firm with a roller",["Disc harrow","Power harrow","Rotary tiller","Puddling harrow","Land roller","Seedbed combination"]),
 shelf("Seeders & planters","Machines that put seed, seedlings or tubers in the ground: seed drills, precision planters, transplanters, potato planters.","kinds by what is placed: seed in rows, single seeds, young plants, tubers",["Seed drill","Single-seed planter","Transplanter","Rice transplanter","Potato planter","Seed potato cutter"]),
 shelf("Spreaders, sprayers & weeders","Machines that put something on the crop or soil, or remove weeds: fertiliser, manure and slurry spreaders, sprayers, hoes.","kinds by what is applied: dry fertiliser, manure, slurry, spray liquid, or a hoe's blade",["Fertiliser spreader","Manure spreader","Slurry tanker","Slurry injector","Crop sprayer","Inter-row hoe and tine weeder"]),
 shelf("Irrigation","Equipment that brings water to field crops: centre-pivot and linear irrigators, hose reels with sprinkler guns, irrigation pumps.","",["Centre-pivot and linear irrigator","Irrigation reel","Irrigation pump"]),
 shelf("Mowers & cutters","Implements that cut standing grass, hay and rough growth: sickle-bar and disc mowers, flail mowers, rotary cutters, hedge cutters; a lawn mower → C2.","kinds by cutting action: sickle, disc, flail, rotary blades, boom-mounted head",["Sickle-bar mower","Disc mower","Flail mower","Rotary cutter","Hedge cutter"]),
 shelf("Haymaking & baling","Machines that turn cut grass into hay or silage: windrowers, tedders, rakes, balers, bale wrappers, forage wagons.","kinds by step after cutting: lay in rows, turn, rake, bale, wrap, carry",["Windrower","Hay tedder","Hay rake","Baler","Bale wrapper","Forage wagon"]),
 shelf("Harvesting & grain handling","Machines that bring in the crop and process grain: combines and headers, forage and root harvesters, grain augers, dryers, cleaners, mills.","kinds by step from field to store: cut and thresh, chop, lift, move, dry, clean, hull, mill",["Combine harvester","Combine header","Forage harvester","Root & speciality harvester","Grain auger and conveyor","Grain dryer","Grain cleaner","Rice huller","Hand grain mill"]),
 ]})
D.append({"n":"Woodland & firewood","mode":"tier","note":"Machines for felling, bringing out, processing and clearing timber.","b":[],
 "t":"Machines that fell, haul, split, saw or clear trees and stumps; hand axes and chainsaws → C1, a forestry tractor → Specialist tractors.",
 "ax":"Which stage of woodland work: fell and bring out trees, turn timber into logs, boards or chips, or clear stumps and scrub?",
 "s":[
 shelf("Felling & extraction","Machines and fittings that fell trees and bring logs out of the wood: harvesters, feller bunchers, skidders, forwarders, winches, timber trailers, cranes.","kinds by stage: fell, drag, carry, lift, winch",["Feller buncher","Forest harvester","Skidder","Forwarder","Forestry winch","Timber trailer with crane","Forestry crane and grapple"]),
 shelf("Timber & firewood processing","Machines that turn logs into firewood, boards or chips: firewood processors, log splitters, portable sawmills, wood chippers.","kinds by product: split and cut logs, boards, chips",["Firewood processor","Tractor log splitter","Portable sawmill","Tractor wood chipper"]),
 shelf("Clearing stumps & scrub","Machines that remove stumps and brush: stump grinders and forestry mulchers.","",["Stump grinder","Forestry mulcher"]),
 ]})
D.append({"n":"Smallholding livestock","mode":"mixed","note":"Handling, feeding, shearing and small-scale dairy kit for a few animals.","b":[],
 "t":"Equipment for holding, feeding, shearing and milking a few farm animals and making their milk into butter or cream; pet and horse gear → B10, fences → C8.",
 "ax":"What is done with the animal: move and hold it, feed it, shear or stun it, or milk it and process the milk?",
 "s":[
 shelf("Handling, weighing & tagging","Equipment that moves, restrains, weighs or identifies animals: livestock trailers, crushes, races, sheep handlers, scales, electronic ear-tag readers.","kinds by step: carry, restrain, sort, weigh, identify",["Livestock trailer","Cattle crush","Cattle race and handling system","Sheep handler","Livestock scales","Livestock EID reader"]),
 shelf("Feeding & bedding","Machines that mix and carry feed or spread bedding: feed mixer wagons, silage block cutters, bedding spreaders.","",["Feed mixer wagon","Silage block cutter","Bedding spreader"]),
 shelf("Shearing & stunning","Tools for shearing sheep and humanely stunning stock: hand shears, shearing machines, captive-bolt stunners.","",["Sheep hand shears","Shearing machine","Captive-bolt stunner"]),
 shelf("Milking & dairy","Machines for taking and processing milk, from bucket milkers and parlours to robots, bulk tanks, cream separators and butter churns.","kinds by step from udder to product: milk, cool, separate, churn",["Bucket milking machine","Milking parlour","Milking robot","Bulk milk cooling tank","Cream separator","Butter churn"]),
 ]})
D.append({"n":"Vintage tractors & engines","mode":"variety","note":"Collector tractors, stationary engines and barn machinery, mapped to named archetypes.","b":[],
 "t":"Old farm machines kept to restore, run or show, from steam engines and early tractors to stationary engines and horse-era implements; a current model → Tractors & tractor fittings.",
 "ax":"How was the machine powered and used: self-propelled and pulling, fixed and driving belts, or worked by horse, belt or hand?",
 "s":[
 shelf("Vintage tractors","Old self-propelled farm tractors and engines that pulled work, from steam traction engines to crawlers and garden tractors; fixed engines → Stationary engines.","kinds by build and era, oldest designs first",["Steam traction and ploughing engine","Early tractor (pre-1930)","Hot-bulb and semi-diesel tractor","Vintage row-crop tractor","Vintage standard tractor","Vintage European diesel tractor","Vintage crawler tractor","Vintage garden tractor"]),
 shelf("Stationary engines","Engines bolted down to drive pumps, saws and belts on farms, from hit-and-miss and throttle-governed to hot-bulb oil engines; a tractor engine → Vintage tractors.","kinds by how the engine governs and ignites: skip-firing, throttle, hot bulb",["Hit-and-miss engine","Throttle-governed stationary engine","Hot-bulb stationary engine"]),
 shelf("Barn & field machinery","Old machines for harvesting and preparing crops and feed: threshing machines, combines, horse-drawn implements, chaff cutters; modern equivalents → Field implements & crop machines.","kinds by job: thresh, reap and thresh, work the field, chop feed",["Threshing machine","Vintage combine harvester","Horse-drawn implement","Chaff cutter"]),
 ]})

cat=dict(old); 
cat['lead']="Machinery for small farms, smallholdings and woodland, organised by the job it does: tractors, loaders and earthmoving, field machines in crop-year order, woodland, livestock and vintage machines; farm-scale machines stay at kind level, and beekeeping gear is in B10."
cat['ax']="What job is the machine for: pulling, moving earth, working the land and crop, working trees, looking after animals, or keeping a machine from the past?"
cat['key']=["1. Is it an old machine kept to restore, run or show: a steam engine, early tractor, stationary engine, thresher or horse-drawn implement? → Vintage tractors & engines",
"2. Is it a tractor, or a tyre, track, weight or steering aid made for one? → Tractors & tractor fittings",
"3. Is it a loader, a digger or lifting machine, or a blade that shapes ground? → Loaders & earthmoving",
"4. Does it fell, haul, split, saw or clear trees and stumps? → Woodland & firewood",
"5. Does it hold, feed, shear or milk animals, or process their milk? → Smallholding livestock",
"6. Does it work the soil, sow, feed or protect crops, cut and bale hay, or harvest and handle grain? → Field implements & crop machines",
"<i>Precedence: a machine kept for restoring or showing is vintage even when it is a tractor or plough; a loader fitted to a tractor is a loader (step 3) before a tractor fitting (step 2).</i>"]
cat['depts']=D
used=set(); 
for dp in D:
    for s in dp['s']:
        for k in s['k']: used.add(k['n'])
missing=set(K)-used; print('unplaced old kinds:',missing)
out=R+'out/C7.json'; json.dump(cat,open(out+'.tmp','w'),indent=1,ensure_ascii=False); os.replace(out+'.tmp',out)

# brands
bp=R+'out/C7_brands.json'; bd=json.load(open(bp)); have={b['n'].lower() for b in bd['b']}
src=SU+'Combine_harvester'
for b in [dict(n='H. V. McKay',c='Australia',seg='Heritage manufactory',kf='Sunshine harvesters',d='Hugh Victor McKay maker of the Sunshine Header-Harvester, an early commercial combine.',sig=['Sunshine Header-Harvester'],sc=['Vintage tractor rallies and restoration'],s=src),
          dict(n='Gleaner Manufacturing Company',c='United States',seg='Heritage manufactory',kf='combines',d='Kansas maker that built the Baldwin brothers\' self-propelled combine from 1923.',sig=['Gleaner self-propelled harvester'],sc=['Vintage tractor rallies and restoration'],s=src),
          dict(n='Claas',c='Germany',seg='Specialist',kf='combines',d='German maker of the Hercules self-propelled combine of 1953.',sig=['Claas Hercules'],sc=['Vintage tractor rallies and restoration'],s=src)]:
    if b['n'].lower() not in have: bd['b'].append(b)
json.dump(bd,open(bp+'.tmp','w'),indent=1,ensure_ascii=False); os.replace(bp+'.tmp',bp)
after=(len(D),sum(len(d['s']) for d in D),len(used),sum(len(k.get('x',[])) for dp in D for s in dp['s'] for k in s['k']))
print('before',before,'after',after)
