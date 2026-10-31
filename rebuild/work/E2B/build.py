import json,copy,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/E2.json'))
MINE=["Fishing & hunting","Camping & hiking","Climbing & caving","Air sports","Water sports","Snow, ice & skate"]
W='https://en.wikipedia.org/wiki/'
def A(n,d_,mk='',y='',s='',v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk='',y='',d_=''): return {"n":n,"mk":mk,"y":y,"d":d_}
kinds={}
for dp in d['depts']:
    if dp['n'] in MINE:
        for sh in dp['s']:
            for k in sh['k']: kinds[k['n']]=(dp['n'],sh['n'],k)
def K(n): return kinds[n][2]
def pre(kn,*xs):
    k=K(kn); k['x']=list(xs)+k.get('x',[])
def app(kn,*xs):
    k=K(kn); k['x']=k.get('x',[])+list(xs)
def after(kn,anchor,*xs):
    k=K(kn); i=[x['n'] for x in k['x']].index(anchor)+1; k['x'][i:i]=list(xs)
def arch(kn,n): return [x for x in K(kn)['x'] if x['n']==n][0]
def newkind(dept,shelf,after_kind,k):
    for dp in d['depts']:
        if dp['n']==dept:
            for sh in dp['s']:
                if sh['n']==shelf:
                    i=[x['n'] for x in sh['k']].index(after_kind)+1 if after_kind else len(sh['k'])
                    sh['k'].insert(i,k); return
    raise Exception(shelf)

# ---------- FISHING ----------
newkind("Fishing & hunting","Rods & reels","Baitcasting reel",{
 "n":"Spincast reel","a":"closed-face reel · push-button reel","d":"Fixed-spool reel with the spool enclosed in a nose cone and a push-button line release.",
 "t":["push-button","underspin (triggerspin)","rod-and-reel combo"],"s":W+"Fishing_reel",
 "x":[A("Zebco 33","The best-known spincast reel; sold from 1954 and still in production.","Zebco","1954","https://www.zebco.com/about-us/history",
        [V("Zebco Standard","Zebco","1949","first spincast reels off the line, before the 33"),V("Zebco 33 (50th anniversary redesign)","Zebco","2004"),V("Zebco 33 Platinum","Zebco","2004","all-metal body and gears"),V("Zebco 33 (60th anniversary)","Zebco","2014","all-new redesign")],
        "size · combo or reel only · colour"),
      A("Zebco 202","Smaller Zebco spincast first sold in 1961 as the 'ZeeBee'.","Zebco","1961","https://www.zebco.com/about-us/history",
        [V("Zebco 202 ZeeBee","Zebco","1961"),V("Zebco 202, 404 and 606 (redesign)","Zebco","2009")],"size · combo"),
      A("Zebco Omega","Spincast design introduced in 2003, later extended as the Omega Pro.","Zebco","2003","https://www.zebco.com/about-us/history",
        [V("Omega Pro","Zebco","2011")],"size · combo")]})
app("Spinning reel",A("Mitchell 300","Open-face fixed-spool reel from Cluses, France, dated 1948 on Wikipedia's reel history.","Mitchell Reel Company","1948",W+"Fishing_reel",[],"size · gear ratio"))
k=arch("Baitcasting reel","Shimano Curado"); k['v'].append(V("Curado DC","Shimano","2003","electronically braked version"))
app("Baitcasting reel",A("Abu Garcia Revo","Baitcasting reel series from Abu Garcia, listed alongside the Ambassadeur.","Abu Garcia","",W+"Fishing_reel",[],"gear ratio · left or right hand"))
app("Fly reel",
    A("Orvis CFO","Exposed-rim, ventilated-spool fly reel with spring-and-pawl drag, named for Charles F. Orvis.","Orvis","1971","https://www.orvis.co.uk/blogs/explore-orvis/two-icons-the-orvis-battenkill-and-c-f-o-reels",
      [V("CFO (Wikipedia date)","Orvis","1972","Wikipedia dates the introduction to 1972; Orvis says 1971")],"size · English or US made · limited editions"),
    A("Orvis Battenkill","Machined-aluminium fly reel series first made for Orvis by Hardy; disc-drag models added in the 1990s.","Orvis","1960s","https://www.orvis.co.uk/blogs/explore-orvis/two-icons-the-orvis-battenkill-and-c-f-o-reels",
      [V("Hardy-made Battenkill","Hardy","1960s","click-and-pawl drag"),V("US-made disc-drag Battenkill","Orvis","1990s")],"size · click-and-pawl or disc drag"))
newkind("Fishing & hunting","Rods & reels","Fly rod",{
 "n":"Tenkara rod","a":"keiryu rod","d":"Long telescopic rod fished with a line tied to the tip and no reel; usually 3.3–4.5 m.",
 "t":["carbon","fixed length","zoom (adjustable length)","handle wood or cork"],"s":W+"Tenkara_fishing","x":[]})
app("Artificial fly",A("Muddler Minnow","Sculpin imitation with a spun deer-hair head; spawned many variants.","Don Gapen","1937",W+"Muddler_Minnow",
    [V("Original Muddler Minnow","Don Gapen","1937","turkey-quill wing, gold tinsel body, spun deer-hair head"),V("Marabou Muddler"),V("Spuddler"),V("Muddler Hopper"),V("Mizzoulian Spook"),V("Searcy Muddler"),V("Keel Muddler")],
    "hook size 2–12 · weighted or unweighted"))
app("Hard lure",A("Rapala Shad Rap","Shallow-diving crankbait whose 1982 release raised Rapala's demand; still a best seller.","Rapala","1982",W+"Rapala",[],"size · diving depth · colour"))
# ---------- CAMPING ----------
after("Tent","Hilleberg Akto",A("Hilleberg Nallo","Two-pole tunnel tent of Hilleberg's Red Label range, in two- to four-person sizes.","Hilleberg","","https://hilleberg.com/nallo-2/",
    [V("Nallo 2","Hilleberg"),V("Nallo 3","Hilleberg"),V("Nallo 4","Hilleberg"),V("Nallo 2 GT","Hilleberg","","extended vestibule, second entrance"),V("Nallo 3 GT","Hilleberg")],"Red Label · persons · GT vestibule"))
after("Tent","Hilleberg Akto",A("Hilleberg Keb","Hilleberg's 1973 double-wall tent whose inner and outer tents pitch together.","Hilleberg","1973",W+"Hilleberg",[],"inner and outer pitched together"))
app("Tent",A("Pup tent","Small two-person tent, issued by many armies as paired shelter halves.","","WWII",W+"Tent",[],"canvas or nylon · shelter half"))
app("Bell tent",A("Sibley tent","Conical tent patented in 1856 and used by the US military before and during the Civil War.","","1856",W+"Tent",[],"centre pole · canvas"))
app("Sleeping bag",A("Euklisia Rug","Early patented sleeping bag of 1876 by Pryce Pryce-Jones.","Pryce Pryce-Jones","1876",W+"Sleeping_bag",[],"wool"))
pre("Camping stove",
    A("Primus pressure stove","First portable pressurised-burner stove, introduced in 1892 by F. W. Lindqvist; Primus was set up with J. V. Svensson.","Primus","1892",W+"Camping_stove",[],"kerosene · size"),)
app("Camping stove",
    A("Optimus 8R and 111","Optimus folding-case white-gas stoves with components enclosed in a metal case.","Optimus","",W+"Camping_stove",[V("8R","Optimus"),V("111","Optimus")],"folding case"),
    A("Esbit stove","Folding stove burning hexamine or trioxane tablets; a German design from the WWII era.","Esbit","WWII",W+"Camping_stove",[],"solid fuel"),
    A("Coleman GI pocket stove","White-gas stove developed for the US Army; Coleman still makes the 442, 533 and 550B.","Coleman","WWII",W+"Camping_stove",[V("442","Coleman"),V("533","Coleman"),V("550B","Coleman")],"white gas · burners"),
    A("MSR XGK","Pressurised liquid-fuel expedition stove, introduced in 1973 as the Model 9.","MSR","1973",W+"Camping_stove",[V("Model 9","MSR","1973"),V("XGK Expedition","MSR")],"multifuel"),
    A("MSR Reactor","Pressurised catalytic canister stove from 2007.","MSR","2007",W+"Camping_stove",[],"integrated pot · canister"),
    A("Jetboil PCS","Personal Cooking System of 2004, the first Jetboil: insulated pot and heat-exchanger burner.","Jetboil","2004",W+"Jetboil",[],"pot volume"),
    A("Jetboil Sol","Compact Jetboil of 2011 in titanium (Sol TI) and aluminium (Sol Advanced) versions.","Jetboil","2011",W+"Jetboil",[V("Sol TI","Jetboil","2011","titanium cup, 5.3 oz"),V("Sol Advanced","Jetboil","2011","aluminium cup, push-button igniter")],"cup material"))
f=arch("Camping stove","Jetboil Flash"); f['y']="2009"; f['v'].append(V("Flash 2.0","Jetboil","2018","1 min 40 s boil time")); f['s']=f['s']
newkind("Camping & hiking","Camp kitchen & water","Camping stove",{
 "n":"Storm kettle","a":"volcano kettle · Kelly Kettle","d":"Kettle with a water jacket around a fire chamber, boiled on twigs through a chimney draught.",
 "t":["aluminium","stainless steel","camp set with pot stand"],"s":W+"Kelly_Kettle",
 "x":[A("Kelly Kettle","Irish storm kettle first produced in the early 1900s; the name is now a trademark.","Kelly Kettle","early 1900s",W+"Kelly_Kettle",[V("Backcountry Boiler","","","lightweight variant, 225 g")],"size · base and cook set"),
      A("Sirram Volcano Kettle","English storm kettle made by George Marris & Co of Birmingham in the 1920s.","George Marris & Co","1920s",W+"Kelly_Kettle",[],"size"),
      A("Thermette","New Zealand kettle registered by John Ashley Hart in 1929; the army's 'Benghazi boiler'.","Thermette","1929",W+"Kelly_Kettle",[],"size"),
      A("Storm Kettle","Modified version sold by the Eydon Kettle Company from the early 1970s.","Eydon Kettle Company","early 1970s",W+"Kelly_Kettle",[],"size")]})
# ---------- CLIMBING ----------
pre("Climbing shoe",
    A("PA boot","Pierre Allain's canvas boot with hard composite rubber sole, used by climbers worldwide by the late 1950s.","","late 1950s",W+"Climbing_shoe",[],"canvas · rubber sole"),
    A("EB","Edmond Bourdonneau's 1950 boot with softer rubber soles, popular in the 1960s and 1970s.","EB","1950",W+"Climbing_shoe",[],"sole rubber"))
c=arch("Camming device","Black Diamond Camalot"); c['y']="1987"
c['v']=[V("Camalot (Chouinard original)","Chouinard Equipment","1987","US patent 4643377")]+c['v']+[V("Camalot C4 (2005)","Black Diamond","2005","thumb loops, #0.4–#6"),V("Camalot C3","Black Diamond","2006","sizes #0000–#2, discontinued 2018"),V("Camalot C4 (2019 update)","Black Diamond","2019","#0.3–#8; #7 and #8 from April 2020")]
c['s']=W+"Camalot"
pre("Climbing harness",
    A("Swami belt","Webbing waist wrap devised by 1960s Yosemite climbers, with a Swami Seat variant.","","1960s",W+"Climbing_harness",[],"tubular webbing"),
    A("Whillans harness","Sit harness made by Troll for the 1970 Annapurna South Face expedition and mass-produced soon after.","Troll","1970",W+"Climbing_harness",[],"waist belt and leg loops"))
# ---------- AIR ----------
newkind("Air sports","Paragliding, hang gliding & skydiving","Skydiving parachute",{
 "n":"Automatic activation device","a":"AAD","d":"Device that opens the reserve container automatically below a set altitude when the descent rate is too high.",
 "t":["electronic","mechanical","student","tandem"],"s":W+"Automatic_activation_device",
 "x":[A("CYPRES","Electronic AAD from Airtec that cuts the reserve closing loop with a small pyrotechnic charge.","Airtec","",W+"Automatic_activation_device",[V("CYPRES 2","Airtec")],"student, expert or tandem setting"),
      A("Vigil","Electronic AAD from Advanced Aerospace Designs.","Advanced Aerospace Designs","",W+"Automatic_activation_device",[V("Vigil 2","Advanced Aerospace Designs")],""),
      A("Argus","Electronic AAD from Aviacom.","Aviacom","",W+"Automatic_activation_device",[],""),
      A("Astra","Electronic AAD from FXC.","FXC","",W+"Automatic_activation_device",[],"")]})
newkind("Air sports","Paragliding, hang gliding & skydiving","Automatic activation device",{
 "n":"Wingsuit","a":"","d":"Jumpsuit with fabric wings between arms, torso and legs that inflate with air to produce lift.",
 "t":["tracking suit","beginner","performance","proximity"],"s":W+"Wingsuit_flying",
 "x":[A("de Gayardon wingsuit","Early-1990s self-inflating suit by Patrick de Gayardon with upper and lower wing surfaces and air inlets.","","early 1990s",W+"Wingsuit_flying",[],"air inlets · wing area"),
      A("BirdMan wingsuit","Suit by Robert Pečnik and Jari Kuosma, produced from 1999 and credited with starting the commercial wingsuit era.","BirdMan","1999",W+"Wingsuit_flying",[],"size · wing cells")]})
# ---------- WATER ----------
pre("Surfboard",
    A("Olo","Longest traditional Hawaiian wooden board, reserved for royalty; over 7 m and up to 90 kg.","","ancient",W+"Surfboard",[],"wood"),
    A("Alaia","Traditional finless Hawaiian wooden board, about 5 m long; modern versions can be 1.8 m.","","ancient",W+"Surfboard",[],"wood · length"))
after("Surfboard","Gun",A("Bonzer","Multi-fin board design by the Campbell Brothers.","Campbell Brothers","",W+"Surfboard",[],"fin set-up"),A("Hybrid","Round-profile board of 1.8–2.6 m for small waves.","","",W+"Surfboard",[],"length"))
app("Wetsuit",
    A("Beuchat isothermic suit","1953 'isothermic' rubber suit by Georges Beuchat for his Pêche-Sport range.","Beuchat","1953",W+"Wetsuit",[],"rubber"),
    A("Body Glove wetsuit","Neoprene suits developed by Bob and Bill Meistrell of Manhattan Beach from about 1953.","Body Glove","c.1953",W+"Wetsuit",[],"neoprene"),
    A("Dunlop Aquafort","Yellow neoprene wetsuit released by Dunlop in 1960.","Dunlop","1960",W+"Wetsuit",[],"neoprene"),
    A("Gul steamer","One-piece full-length 'steamer' wetsuit pioneered by Gul in the early 1970s.","Gul","early 1970s",W+"Wetsuit",[],"thickness"))
K("Wetsuit")['t']=K("Wetsuit")['t']+['long john','semi-dry']
pre("Regulator",A("Rouquayrol-Denayrouze apparatus","1860s French demand-regulator diving apparatus; the first widely made demand regulator.","","1860s",W+"Diving_regulator",[],"air reservoir"))
app("Regulator",
    A("Poseidon Cyklon","Poseidon regulators including the Cyklon 200 and side-exhaust Cyklon 5000.","Poseidon","",W+"Diving_regulator",[V("Cyklon 200","Poseidon"),V("Cyklon 5000","Poseidon","","side exhaust")],"first and second stage"),
    A("Apeks TX100","Apeks second stage with heat-exchange fins on the valve seat housing.","Apeks","",W+"Diving_regulator",[],"first stage pairing"))
pre("Dive computer",A("Uwatec Aladin","Wrist-worn Uwatec computer; the Aladin Air X NitrOx was made in 1995.","Uwatec","",W+"Dive_computer",[V("Aladin Air X NitrOx","Uwatec","1995","recalled in 2003 for software fault")],"air integration · nitrox"))
app("Dive computer",
    A("Suunto D9","Watch-sized Suunto wrist computer with electronic compass; the D6 and D9 were recalled in 2006.","Suunto","",W+"Dive_computer",[V("D6","Suunto"),V("D9","Suunto")],"wrist"),
    A("Scubapro Galileo","Technical trimix computer listed under Scubapro and Uwatec.","Scubapro","",W+"Dive_computer",[],"wrist or console"))
k=arch("Dive computer","Shearwater Perdix"); k['v'].append(V("Petrel 2","Shearwater"))
app("Dive cylinder",
    A("Aluminium 80 (S80)","Most common back-gas cylinder, about 11 L nominal; aluminium, near-neutral buoyancy.","","",W+"Diving_cylinder",[V("C80","","","high-pressure equivalent, about 10.3 L"),V("C100","","","about 13 L"),V("S63","","","about 9 L")],"valve · colour"),
    A("Steel high-pressure cylinder","Steel cylinders of 65 to 130 cu ft, used by cold-water and technical divers.","","",W+"Diving_cylinder",[V("HP65","","","about 8.2 L"),V("LP80/HP80","","","about 10.1 L"),V("HP119/HP120/HP130","","","14.8–16 L")],"valve · bands"))
# ---------- SNOW ----------
pre("Alpine ski",
    A("Rossignol Olympic 41","Rossignol ski on which Émile Allais won triple world championships in 1937.","Rossignol","1937",W+"Skis_Rossignol",[],"length"),
    A("Rossignol Allais 60","Rossignol's first all-metal ski; Jean Vuarnet won the 1960 Olympic downhill on it.","Rossignol","1960",W+"Skis_Rossignol",[],"length"),
    A("Rossignol Strato","Rossignol's first fibreglass ski, released in 1964.","Rossignol","1964",W+"Skis_Rossignol",[],"length"))
k=K("Ski boot"); i=0
k['x']=[A("Henke buckle boot","1956 Swiss boot with over-centre latches patented by Hans Martin, replacing laces.","Henke","1956",W+"Ski_boot",[],"leather"),
        A("Rosemount side-entry boot","Side-entry boot introduced in 1965.","Rosemount","1965",W+"Ski_boot",[],""),
        A("Lange plastic boot","Bob Lange combined polyurethane with Henke's flap-and-buckle system in 1964; production examples from 1966.","Lange","1964",W+"Ski_boot",[V("Lange production boot","Lange","1966")],"flex"),
        A("Salomon SX 91 Equipe","Rear-entry boot popular in the 1980s; the SX 92 followed.","Salomon","1980s",W+"Ski_boot",[V("SX 92 Equipe","Salomon")],"rear entry"),
        A("Raichle Flexon","Three-piece cabrio boot introduced in 1979.","Raichle","1979",W+"Ski_boot",[],"")]+k['x']
pre("Ski binding",
    A("Rottefella Nordic Norm","Three-pin 75 mm Nordic binding developed by Bror With in 1927 with pins and a metal bail.","Rottefella","1927",W+"Ski_binding",[V("Salomon Nordic System (SNS)","Salomon","1979","bar in the boot toe"),V("Rottefella NNN","Rottefella","","New Nordic Norm"),V("Salomon Prolink","Salomon","2016","NNN-compatible"),V("Rottefella NTN","Rottefella","2007","telemark binding with lateral release")],"Nordic Norm · NNN · SNS · NTN"),
    A("Cubco binding","First modern heel-and-toe alpine binding, from 1950 and popular about 1960.","Cubco","1950",W+"Ski_binding",[],"heel and toe"))
pre("Snowboard",
    A("Snurfer","Sherman Poppen's 1965 ski-toy board; licensed to Brunswick in 1966 and the direct predecessor of the snowboard.","Brunswick","1966",W+"Snurfer",
      [V("Original Snurfer","Brunswick","1966","rope and handle, anti-skid footrest, no bindings"),V("JEM Snurfer","JEM Corporation","1972","production continued after Brunswick stopped"),V("Bungee version","","1980","Ostatnigrosh and Melnikov"),V("Binding version","","1982","same designers")],"length"),
    A("Winterstick","Dimitrije Milovich's swallowtail board; company 1972–82, patent 1974.","Winterstick","1974",W+"Snowboard",[],"swallowtail"),
    A("Burton Backhill","Early Burton board of 1981.","Burton","1981",W+"Burton_Snowboards",[],"length"))
app("Skateboard",
    A("Penny board","Small plastic cruiser skateboard from Penny Skateboards, 2010; a 22 in Penny and larger Nickel, Cruiser and Longboard.","Penny Skateboards","2010",W+"Penny_board",
      [V("Penny","Penny Skateboards","2010",'22 in'),V("Nickel","Penny Skateboards","",'27 in'),V("Surf Skate","Penny Skateboards","",'29 in'),V("Cruiser","Penny Skateboards","",'32 in'),V("Longboard","Penny Skateboards","",'36 in')],"polycarbonate deck · 59 or 69 mm wheels"),
    A("Old school board","1970s–80s board shape, wide with often one kicktail, still copied today.","","1970s–80s",W+"Skateboard",[],"width · kicktail"))
newkind("Snow, ice & skate","Skateboards, skates & scooters","Skateboard deck",{
 "n":"Fingerboard","a":"finger skateboard","d":"Scaled-down skateboard ridden with the fingers, about 96 mm long, with a plywood deck, metal trucks and urethane wheels.",
 "t":["toy-store","professional","neoprene or sandpaper grip","complete or parts"],"s":W+"Tech_Deck",
 "x":[A("Somerville International fingerboard","First mass-produced fingerboard not meant for figurines or accessories.","Somerville International","",W+"Tech_Deck",[],"deck width 26–36 mm"),
      A("Tech Deck","Best-known toy fingerboard brand, with licensed skate-brand graphics; video games followed in 2000 and 2001.","Tech Deck","",W+"Tech_Deck",[],"graphic · 96 mm"),
      A("Blackriver fingerboard","German professional-grade fingerboards, trucks and ramps by Blackriver Ramps, founded 1999.","Blackriver Ramps","1999",W+"Tech_Deck",[],"deck · trucks · ramps"),
      A("Flatface fingerboard","American fingerboard brand founded by Mike Schneider in 2003; also a US distributor of Blackriver.","Flatface Fingerboards","2003",W+"Tech_Deck",[],"deck · trucks")]})

# ------- outputs -------
depts=[dp for dp in d['depts'] if dp['n'] in MINE]
os.makedirs(R+'work/E2B',exist_ok=True)
json.dump({"depts":depts},open(R+'out/E2B_part.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(R+'out/E2B_part.json.tmp',R+'out/E2B_part.json')
json.dump({"c":"E2","rev":True,"lead":"x","b":[],"depts":depts},open(R+'work/E2B/check.json','w'),ensure_ascii=False)
