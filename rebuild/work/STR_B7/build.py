import json,copy,os
P='/home/user/Possession-Taxonomy/rebuild/out/B7.json'
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/STR_B7/bak/B7.json'))
K={}
dept={dp['n']:dp for dp in d['depts']}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
before=(len(d['depts']),sum(len(dp['s']) for dp in d['depts']),len(K),sum(len(k.get('x',[])) for k in K.values()))
def tt(n,groups,see=None):
    k=K[n]; k.pop('t',None); k['tt']=groups
    if see: k['see']=see
# ---- tt and see
tt('Fan heater',[["Shape",["Desk or personal","Floor-standing","Oscillating tower","Bladeless"]],["Function",["Heat only","Hot and cool fan"]],["Fuel",["Mains electric","Gas cartridge"]],["Moisture protection",["Bathroom-safe, splash-rated (IP21)"]]])
tt('Convector heater',[["Shape",["Freestanding on feet","Slim panel","Wall-mountable plug-in"]],["Element",["Standard convector","Micathermic (mica-sheet)"]],["Airflow",["Natural convection","With turbo fan"]],["Control",["Smart / Wi-Fi"]]])
tt('Oil-filled radiator',[["Size",["Full-size finned column on castors","Mini / desktop"]],["Filling",["Sealed oil","Oil-free (dry core)"]],["Control",["Digital thermostat and timer","Smart / Wi-Fi"]]])
tt('Radiant heater',[["Element",["Quartz","Halogen","Carbon fibre","Ceramic"]],["Shape",["Bar heater","Freestanding heat lamp"]],["Head",["Fixed","Oscillating"]]],[["C2","Patio heater","outdoor radiant heater"]])
tt('Infrared panel heater',[["Finish",["White panel","Mirror","Glass","Printed picture"]],["Mounting",["Wall","Ceiling panel or tile","Portable on feet"]],["Control",["Smart / Wi-Fi"]]])
tt('Electric fireplace',[["Mounting",["Freestanding stove","Portable fireplace suite"]],["Heat source",["Fan coil","Infrared"]],["Flame effect",["LED flame","Water-mist (3D flame and smoke)"]]],[["G3","Pellet stove","fixed stove, flued"],["G3","Flued stove","fixed stove, flued"]])
tt('Kerosene heater',[["Burner",["Wick convection (round)","Wick radiant","Gasification blue-flame"]],["Airflow",["Natural","Fan-forced"]]])
tt('Portable gas heater',[["Gas supply",["Butane bottle inside cabinet","Propane 1 lb cylinder"]],["Burner",["Catalytic","Radiant ceramic plaque","Blue flame"]],["Shape",["Wheeled cabinet","Compact unit","Flame-effect cabinet"]]],[["C2","Patio heater","outdoor gas heater"]])
tt('Window air conditioner',[["Mounting",["Standard window","U-shaped / saddle (sash closes through the gap)","Through-the-wall sleeve"]],["Compressor",["Fixed-speed","Inverter (variable-speed)"]],["Function",["Cool only","Heat and cool (heat pump)"]],["Control",["Smart / Wi-Fi"]]],[["G3","Split air conditioner","fixed indoor and outdoor units"]])
tt('Portable air conditioner',[["Hose",["Single-hose","Dual-hose / hose-in-hose"]],["Function",["Cool only","Heat and cool (heat pump)","4-in-1 (cool, fan, dehumidify, heat)"]],["Compressor",["Fixed-speed","Inverter"]],["Power source",["Mains","Battery or portable power station"]],["Control",["Smart / Wi-Fi"]]],[["G3","Split air conditioner","fixed alternative"]])
tt('Evaporative cooler',[["Size and mounting",["Portable room cooler (tank on castors)","Personal / tower","Desert cooler (window or wall)","Outdoor / patio with hose feed"]],["Cycle",["Direct (adds humidity)","Indirect or two-stage (no added humidity)"]]])
K['Misting fan']={"n":"Misting fan","a":"mist fan · water-spray fan · patio misting fan","d":"Fan that sprays a fine water mist into its airflow to cool by evaporation, for patios and hot dry rooms; a plain fan → Fans.","s":"https://en.wikipedia.org/wiki/Evaporative_cooler","tt":[["Size",["Handheld spray fan","Floor-standing"]],["Water feed",["Tank","Garden hose"]]]}
tt('Desk fan',[["Motor",["AC","DC"]],["Power",["Mains","USB"]],["Blades",["Bladed","Bladeless"]],["Mounting",["Table-standing","Clip-on"]],["Style",["Retro metal"]]])
K['Floor fan']={"n":"Floor fan","a":"low-profile fan · drum fan · high-velocity fan","d":"Fan that sits on the floor with no stand and blows across the room, larger than a desk fan; on a stand → Pedestal fan.","s":"https://www.jbhifi.com.au/collections/home-appliances/fans","tt":[["Shape",["Low-profile round","Drum / high-velocity"]],["Head",["Fixed","Oscillating"]]]}
tt('Box fan',[["Size",["20-inch"]],["Build",["Standard","Weather-resistant motor","Slim low-profile"]],["Speeds",["3-speed"]]])
tt('Pedestal fan',[["Motor",["AC oscillating","DC quiet and energy-saving"]],["Blades",["Bladed","Bladeless"]],["Height",["Fixed pedestal","Convertible to tabletop"]],["Power",["Mains","Cordless battery"]],["Control",["Smart / app"]]],[["G3","Ceiling fan","fixed overhead fan"]])
tt('Tower fan',[["Blades",["Bladed impeller","Bladeless"]],["Height",["Fixed","Height-adjustable"]],["Added function",["Ioniser","Purifier combination"]]],[["B7","Air purifier","tower with filter"]])
tt('Air circulator',[["Size",["Compact / personal","Medium whole-room","Large heavy-duty"]],["Head",["Fixed","Oscillating or multi-directional"]],["Motor",["AC","DC quiet"]]])
tt('Window fan',[["Fans",["Single","Twin"]],["Airflow",["Reversible intake and exhaust","Fixed direction"]],["Control",["Remote","Thermostat"]]],[["G3","Extractor fan","fixed, ducted"]])
tt('Wall or clip fan',[["Mounting",["Wall-mounted oscillating","Clip-on","Stroller or cot clip"]],["Blades",["Bladed","Soft-blade","Bladeless"]],["Power",["Mains","Rechargeable"]]])
hf=K['Handheld fan']; hf['a']='hand fan (powered) · mini fan'; hf['d']='Powered fan held in the hand; a plain folding hand fan is a fashion accessory.'
tt('Handheld fan',[["Folding",["Fixed","Foldable"]],["Stand",["Handheld only","With desk stand"]],["Power",["Rechargeable","Battery"]]],[["A4","Folding fan","unpowered hand fan"]])
nf={"n":"Neck fan","a":"wearable fan · neck air conditioner · waist fan","d":"Powered fan worn on the neck, waist or a clip so it cools hands-free; a hand-held fan → Handheld fan.","s":"https://jisulife.com/collections/handheld-fan","m":[],"tt":[["Wear",["Neck","Waist or clip"]],["Blades",["Bladed","Bladeless"]],["Cooling",["Air only","Semiconductor cooling plate (neck air conditioner)"]]]}
nm=[m for m in hf['m'] if m[0].startswith('Neck') or m[0].startswith('COOLiFY')]
hf['m']=[m for m in hf['m'] if m not in nm]; nf['m']=nm; K['Neck fan']=nf
tt('Air purifier',[["Shape",["HEPA tower or console","Desktop / compact","Bladeless purifier-fan"]],["Technology",["HEPA with activated carbon","UV-C","Ioniser / plasma","Photoelectrochemical oxidation","Hypochlorous-acid deodoriser"]],["Grade",["Domestic","Medical-grade HEPA with heavy carbon"]],["Combined function",["Purifier-humidifier","Purifier-heater"]],["Control",["Smart / app with sensors"]]],[["G3","Ventilation unit","fixed, whole-home air"]])
tt('Replacement air filter',[["Filter",["HEPA particle","Activated carbon / odour","Combined 3-in-1 cartridge","Washable pre-filter","Humidifier wick or demineralisation cartridge","Dehumidifier dust filter"]],["Speciality",["Pet allergy","Smoke","Toxin absorber"]],["Supply",["Genuine maker","Third-party"]]])
tt('Indoor air quality monitor',[["Sensor",["CO2 (NDIR)","PM2.5 particles","Multi-sensor (PM2.5, CO2, VOC, temperature, humidity)","Radon"]],["Display",["E-ink screen","App only"]],["Connection",["Standalone","Smart-home (Zigbee, Matter, HomeKit)"]]],[["B8","CO alarm","alarm, not a monitor"],["E6","Hygrometer","humidity only"]])
seen=set(); u=[]
for m in K['Indoor air quality monitor']['m']:
    if tuple(m) not in {tuple(x) for x in u} and m[0].lower().replace('home','Home').lower() not in {x[0].lower() for x in u}: u.append(m)
K['Indoor air quality monitor']['m']=u
tt('Humidifier',[["Mist method",["Ultrasonic cool-mist","Evaporative wick","Air washer (rotating discs)","Warm-mist / steam vaporiser","Hybrid ultrasonic-evaporative"]],["Tank",["Top-fill"]],["Use",["Nursery cool-mist"]],["Added function",["Humidifier-purifier"]],["Control",["Smart / app"]]],[["B4","Electric diffuser","scent, not moisture"],["E6","Hygrometer","measures humidity"]])
tt('Dehumidifier',[["Method",["Compressor (refrigerant)","Desiccant rotor","Thermoelectric (Peltier)"]],["Drainage",["Tank","Built-in pump / continuous drain"]],["Added function",["Laundry-drying mode","Purifier combination"]],["Control",["Smart / app"]]],[["G3","Whole-house dehumidifier","fixed, ducted"],["B6","Clothes airer","drying laundry without power"]])
tt('Desiccant moisture absorber',[["Container",["Refillable tub","Disposable tub","Hanging bag","360-degree device with refill tab"]],["Refill",["Granules","Tabs"]]])
# ---- structure
def shelf(n,t,ax,kinds):
    s={"n":n,"t":t}
    if ax: s["ax"]=ax
    s["k"]=[K[x] for x in kinds]; return s
bh=dept['Portable heating']['b']; bc=dept['Cooling & fans']['b']; ba=dept['Air quality & humidity']['b']
vint=K['Electric fan (design & vintage)']; vint_s=[s for s in dept['Cooling & fans']['s'] if s['n']=='Design & vintage fans'][0]
depts=[]
depts.append({"n":"Portable heating","mode":"tier","note":"Plug-in or fuel-fed heaters a person moves between rooms; stoves, fires, boilers, radiators and towel rails are built-ins and move to G3.","b":bh,
 "t":"Plug-in or fuel-fed heaters moved from room to room; a fixed stove, boiler or radiator → Home Fixtures (G3); a patio heater → C2.",
 "ax":"How does the heater make and deliver warmth: by warming the air, by a radiant beam, or by a flame or fuel?",
 "s":[shelf("Warm-air heaters","Electric heaters that warm the air around them: fan heaters, convectors and oil-filled radiators; a beam of radiant heat → Radiant heaters.","kinds by how the warm air moves: blown by a fan, rising by convection, held in oil",["Fan heater","Convector heater","Oil-filled radiator"]),
      shelf("Radiant heaters","Electric heaters that beam infrared heat at people and objects: bar and halogen heaters, heat lamps and wall panels; a heater that blows warm air → Warm-air heaters.",None,["Radiant heater","Infrared panel heater"]),
      shelf("Flame & fuel heaters","Heaters with a real or imitated flame, or that burn fuel: electric fire stoves, kerosene and bottled-gas heaters; a fixed fire or stove → G3.","kinds by what makes the flame: electricity, kerosene, bottled gas",["Electric fireplace","Kerosene heater","Portable gas heater"])]})
depts.append({"n":"Air conditioners & coolers","mode":"tier","note":"Window and portable air conditioners and evaporative coolers; split, cassette and ducted systems are fixtures (G3).","b":[b for b in bc if b['m'] in ('Cooling capacity matched to the room','Efficiency','Noise','Hose and drainage')],
 "t":"Movable or window-fitted appliances that cool room air; a fixed split or ducted system → Home Fixtures (G3); a fan that only moves air → Fans.",
 "ax":"How does it cool the air: with a refrigerant circuit or by evaporating water?",
 "s":[shelf("Air conditioners","Refrigerant units that cool and dry room air: window, through-the-wall and portable hose models; a fixed split system → G3.","kinds by where the unit sits: in a window or wall, or on the floor with a hose",["Window air conditioner","Portable air conditioner"]),
      shelf("Evaporative coolers","Units that cool air by evaporating water, adding humidity: room, desert and outdoor coolers and misting fans; a refrigerant unit → Air conditioners.",None,["Evaporative cooler","Misting fan"])]})
depts.append({"n":"Fans","mode":"mixed","note":"Plug-in and battery fans that move air to cool a person or mix a room; ceiling fans and extractor fans are fixtures (G3).","b":[{"m":"Airflow and reach","v":"CFM or m³/min; oscillation; DC motor","w":"Fans are compared on airflow per watt and noise, not on power."},[b for b in bc if b['m']=='Noise'][0]],
 "t":"Fans that move air without heating, cooling or cleaning it; a fan that also heats → Portable heating; a fixed ceiling or extractor fan → G3.",
 "ax":"Where does the fan stand, mount or travel: on a table or floor, on a window or wall, or on the body?",
 "s":[shelf("Table, floor & stand fans","Fans with their own base that cool a person or circulate room air: desk, box, floor, pedestal and tower fans and air circulators.","kinds by where the base sits: table, floor, stand, column, then the circulator that moves room air",["Desk fan","Box fan","Floor fan","Pedestal fan","Tower fan","Air circulator"]),
      shelf("Mounted fans","Fans fixed to a window opening, wall or clip rather than standing: window fans, wall fans and clip fans.",None,["Window fan","Wall or clip fan"]),
      shelf("Personal fans","Powered fans held or worn so they cool one person on the move: handheld and neck fans.",None,["Handheld fan","Neck fan"]),
      {"n":vint_s['n'],"t":"Electric fans collected or chosen for their maker and design, from early brass-blade table fans to bladeless designer fans.","k":[vint]}]})
depts.append({"n":"Air cleaning & monitoring","mode":"tier","note":"Room appliances that filter or treat air, their filters, and monitors that measure it; whole-house and ducted units are fixtures (G3).","b":[b for b in ba if b['m'] in ('Clean-air delivery rate for the room','Filter type and running cost','Noise')],
 "t":"Appliances that clean room air, the filters made for them, and small monitors that measure it; a CO or smoke alarm → B8; a humidifier → Humidity control.",
 "ax":"Does it clean the air, supply the filters that clean it, or only measure it?",
 "s":[shelf("Purifiers & filters","Movable air cleaners and the filters made to fit them: HEPA purifiers and replacement cartridges.",None,["Air purifier","Replacement air filter"]),
      shelf("Air monitors","Small room devices that measure carbon dioxide, particles, VOCs or radon; a CO alarm → B8.",None,["Indoor air quality monitor"])]})
depts.append({"n":"Humidity control","mode":"tier","note":"Room humidifiers, dehumidifiers and moisture absorbers; whole-house units are fixtures (G3).","b":[b for b in ba if b['m'] in ('Moisture added or removed','Noise','Ease of cleaning')],
 "t":"Appliances that add moisture to room air or take it out; a scent diffuser → B4; a whole-house unit → Home Fixtures (G3).",
 "ax":"Does it add moisture to the air or take it out?",
 "s":[shelf("Adding moisture","Appliances that put water into the air as mist or steam: ultrasonic, evaporative and warm-mist humidifiers; a scent diffuser → B4.",None,["Humidifier"]),
      shelf("Removing moisture","Powered or unpowered appliances that draw water out of the air: compressor and desiccant dehumidifiers and calcium-chloride absorbers.","kinds by whether it needs power: powered dehumidifier, then unpowered absorber",["Dehumidifier","Desiccant moisture absorber"])]})
d['depts']=depts
d['ax']="What does the appliance do to the air of a room: warm it, cool it, move it, clean it or change its moisture?"
d['key']=["1. Does it make the room warmer, by plug-in element or by burning fuel? → Portable heating",
"2. Does it cool the air with a refrigerant circuit or by evaporating water? → Air conditioners & coolers",
"3. Does it only move air, to cool a person or mix the room, standing, mounted or worn? → Fans",
"4. Does it filter or treat the air, or measure its quality? → Air cleaning & monitoring",
"5. Does it add moisture to the air or draw it out? → Humidity control",
"<i>Precedence: a fan that heats is a heater (step 1); a fan with a water spray is an evaporative cooler (step 2); a purifier built into a fan is a purifier (step 4); fixed ceiling, extractor and split systems belong to Home Fixtures (G3).</i>"]
json.dump(d,open('/home/user/Possession-Taxonomy/rebuild/work/STR_B7/B7.new.json','w'),indent=1,ensure_ascii=False)
os.replace('/home/user/Possession-Taxonomy/rebuild/work/STR_B7/B7.new.json',P)
after=(len(d['depts']),sum(len(dp['s']) for dp in d['depts']),sum(len(s['k']) for dp in d['depts'] for s in dp['s']),sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k']))
print(before,after)
