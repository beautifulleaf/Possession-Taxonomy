import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,mk,y,page,d,a='',v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+page,"v":v or [],"dt":dt}
def V(n,mk,y,d=''): return {"n":n,"mk":mk,"y":y,"d":d}
PT=["petrol","diesel","hybrid","plug-in hybrid","battery electric"]
OLD='https://www.carsupermarket.com/used-cars/body-type'
kinds=[
{"n":"Hatchback","a":"liftback · supermini · small family car","d":"Passenger car whose rear door is a top-hinged tailgate opening onto the load space.",
 "t":["three-door","five-door","supermini (B-segment)","small family (C-segment)"]+PT,"s":OLD,
 "x":[
  X("Renault 4","Renault","1961–1994","Renault_4","Economy car recognised as the world's first mass-produced hatchback, with front-wheel drive and a one-piece tailgate.",a="R4 · 4L",dt="body: short hatchback/estate · engine size · colour"),
  X("Volkswagen Golf","Volkswagen","1974–","Volkswagen_Golf","Front-engined, front-wheel-drive C-segment hatchback that replaced the Beetle; Volkswagen's bestseller over eight generations.",a="Rabbit · Caribe",
    v=[V("Golf Mk1","Volkswagen","1974","Italdesign styling by Giugiaro; sold as Rabbit in North America"),V("Golf Mk2","Volkswagen","1983–1992","larger successor"),
       V("Golf Mk3","Volkswagen","1991","launched in mainland Europe August 1991"),V("Golf Mk4","Volkswagen","1997","Type 1J; moved upmarket"),
       V("Golf Mk5","Volkswagen","2003","Typ 1K; PQ35 platform"),V("Golf Mk6","Volkswagen","2008","Typ 5K"),V("Golf Mk7","Volkswagen","2012","hatchback, estate"),V("Golf Mk8","Volkswagen","2019","MQB Evo platform")],
    dt="three/five-door · estate · trim and engine · colour"),
  X("Renault 5","Renault","1972–1996","Renault_5","Three- or five-door supermini hatchback, sold in North America as Le Car.",a="R5 · Le Car · Supercinq",
    v=[V("first generation (R5)","Renault","1972–1985","front mid-engine"),V("second generation (Super 5)","Renault","1984–1996","front engine")],dt="three/five-door · trim · colour"),
  X("Ford Fiesta","Ford","1976–2023","Ford_Fiesta","Supermini sold by Ford over seven generations, mainly developed in Europe.",dt="three/five-door · trim · engine"),
  X("Peugeot 205","Peugeot","1983–1999","Peugeot_205","Single-generation supermini that replaced the Peugeot 104 and Talbot Samba.",dt="three/five-door · trim · engine"),
  X("Honda Civic","Honda","1972–","Honda_Civic","Compact car line launched as a two-door fastback and three-door hatchback with a transverse engine and front-wheel drive.",dt="body · generation · trim"),
  X("Mazda2","Mazda","2002–","Mazda2","Supermini sold as a five-door hatchback and saloon, known in Japan as the Demio.",a="Demio · Mazda 121",v=[V("2 Hybrid","Mazda","","model listed in the old data")],dt="generation · hybrid or petrol"),
  X("Nissan Leaf","Nissan","2010–","Nissan_Leaf","Battery-electric five-door hatchback, unveiled as the first mass-market electric car.",dt="battery size · generation"),
  X("Volkswagen ID.3","Volkswagen","2019–","Volkswagen_ID.3","Battery-electric C-segment hatchback, the first Volkswagen Group car on the MEB platform.",dt="battery size · trim"),
 ]},
{"n":"Saloon","a":"sedan · three-box · notchback","d":"Passenger car with a separate boot behind a fixed roof over two rows of seats.",
 "t":["two-door saloon","four-door saloon","fastback saloon","four-door coupé","compact executive","large family (D-segment)"]+PT,"s":OLD,
 "x":[
  X("Toyota Corolla","Toyota","1966–","Toyota_Corolla","Compact car series that is the best-selling automobile nameplate of all time, over twelve generations.",
    v=[V("Corolla E210","Toyota","2018","twelfth generation; saloon, hatchback and estate; GR Corolla from 2022")],dt="generation · body · hybrid or petrol"),
  X("Mercedes-Benz W123","Mercedes-Benz","1975–1986","Mercedes-Benz_W123","Executive car range sold as saloon, coupé and estate, the most successful Mercedes-Benz of its time.",dt="saloon · coupé · estate · diesel or petrol"),
  X("BMW 3 Series","BMW","1975–","BMW_3_Series","Compact executive car line over eight generations, first sold only as a two-door saloon.",dt="saloon · coupé · convertible · estate · generation"),
  X("Ford Cortina","Ford","1962–1982","Ford_Cortina","Medium-sized family car in five marks, the United Kingdom's best-selling car of the 1970s.",a="Mark I–V",dt="mark · body · trim"),
  X("Toyota Camry","Toyota","1982–","Toyota_Camry","Mid-size saloon line, originally compact, sold internationally since 1982.",dt="generation · hybrid or petrol"),
  X("Honda Accord","Honda","1976–","Honda_Accord","Car series best known as a four-door saloon, among the best-selling cars in the United States.",a="Inspire",dt="generation · body"),
  X("Mercedes-Benz C-Class","Mercedes-Benz","1993–","Mercedes-Benz_C-Class","Compact executive car series that replaced the 190 (W201).",v=[V("W204","Mercedes-Benz","2007","third generation"),V("W206","Mercedes-Benz","2021","current generation")],dt="saloon · estate · 4MATIC"),
  X("Tesla Model 3","Tesla","2017–","Tesla_Model_3","Battery-electric mid-size fastback saloon, the world's top-selling plug-in car 2018–2020.",dt="battery and motor configuration"),
  X("Volkswagen Beetle","Volkswagen","1938–2003","Volkswagen_Beetle","Rear-engined small family car (Type 1), the best-selling single-platform car in history.",a="Type 1 · Käfer · Bug",dt="year and window shape · engine size · colour"),
 ],
 "m":[["A-Class Saloon","Mercedes-Benz"],["CLA","Mercedes-Benz"]]},
{"n":"Estate","a":"station wagon · wagon · touring · avant","d":"Passenger car with the roof carried back to the rear and a tailgate over a long load space.",
 "t":["compact estate","large estate","shooting brake","raised all-terrain estate"]+PT,"s":OLD,
 "x":[
  X("Volvo 200 Series","Volvo","1974–1993","Volvo_200_Series","Mid-size Volvo range (240 and 260) designed by Jan Wilsgaard, sold as saloon, estate and convertible.",a="Volvo 240 · 245 · 260",dt="saloon or estate · engine · trim"),
  X("Mercedes-Benz W123 estate","Mercedes-Benz","1975–1986","Mercedes-Benz_W123","Estate version of the W123 executive range, built until January 1986.",dt="diesel or petrol · trim"),
  X("Volkswagen Passat","Volkswagen","1973–","Volkswagen_Passat","D-segment family car sold as saloon, estate and hatchback, the fourth best-selling automobile of all time.",a="Dasher · Santana · Quantum",dt="generation · saloon or estate"),
  X("Škoda Octavia","Škoda","1996–","%C5%A0koda_Octavia","C-segment family car sold only as five-door liftback or estate, Škoda's best seller.",dt="generation · liftback or estate · 4x4"),
  X("Subaru Outback","Subaru","1994–","Subaru_Outback","Legacy-derived estate with off-road styling and all-wheel drive.",a="Legacy Outback",dt="generation · engine"),
 ]},
{"n":"SUV","a":"sport utility vehicle · crossover · 4x4","d":"Passenger car with a tall body, raised ground clearance and often four-wheel drive.",
 "t":["crossover","compact SUV","mid-size SUV","full-size SUV","two-wheel drive","four-wheel drive"]+PT,"s":OLD,
 "x":[
  X("Chevrolet Suburban","Chevrolet","1934–","Chevrolet_Suburban","Full-size SUV and the world's longest-produced nameplate, progenitor of the modern full-size SUV.",dt="generation · seating"),
  X("Range Rover","Land Rover","1970–","Range_Rover_Classic","Four-wheel-drive off-road vehicle that moved upmarket in the 1980s.",
    v=[V("Range Rover Classic","Land Rover","1970–1996","two-door, four-door from 1981"),V("Range Rover L322","Land Rover","2001–2012","third generation; first with unitary body and independent suspension")],dt="two/four-door · engine · trim"),
  X("Jeep Cherokee XJ","Jeep","1983–2001","Jeep_Cherokee_(XJ)","Compact unibody SUV developed by AMC, sold in two- or four-door form.",dt="two/four-door · 2WD or 4WD"),
  X("Toyota RAV4","Toyota","","Toyota_RAV4","Compact crossover often credited as the first modern compact crossover SUV; the best-selling SUV of all time.",dt="generation · hybrid or petrol"),
  X("Honda CR-V","Honda","1995–","Honda_CR-V","Compact crossover SUV first built on the Civic platform.",a="Breeze",dt="generation · hybrid"),
  X("Nissan Qashqai","Nissan","2006–","Nissan_Qashqai","Compact C-segment SUV, sold first as the Dualis in Japan and Australia.",a="Dualis",dt="generation · engine"),
  X("Audi Q7","Audi","2005–","Audi_Q7","Two- and three-row E-segment SUV, Audi's first SUV.",dt="generation · engine · seating"),
  X("Tesla Model Y","Tesla","2020–","Tesla_Model_Y","Battery-electric compact crossover, the best-selling electric vehicle of all time.",dt="battery and motor configuration"),
 ]},
{"n":"MPV","a":"minivan · people carrier · multi-purpose vehicle","d":"Passenger car with a tall one-box body and up to three rows of seats where the load space would be.",
 "t":["compact MPV","large MPV","sliding side doors","seven-seat","eight-seat"]+PT,"s":OLD,
 "x":[
  X("Renault Espace","Renault","1984–","Renault_Espace","Among the first modern MPVs; first three generations built by Matra, sixth generation a crossover.",dt="generation · seating"),
  X("Chrysler minivans","Chrysler","1984–","Chrysler_minivans","Minivan series introduced as the Dodge Caravan and Plymouth Voyager, now in its sixth generation.",a="Dodge Caravan · Plymouth Voyager · Town & Country · Pacifica",dt="generation · nameplate · wheelbase"),
  X("Mercedes-Benz V-Class","Mercedes-Benz","","Mercedes-Benz_Vito","Passenger MPV form of the mid-size Vito van, up to eight seats.",a="Vito Tourer · Viano",v=[V("Viano","Mercedes-Benz","","model listed in the old data"),V("V-Class","Mercedes-Benz","","model listed in the old data"),V("EQV","Mercedes-Benz","","electric; model listed in the old data")],dt="wheelbase · seating · electric or diesel"),
  X("Kia Carnival","Kia","1998–","Kia_Carnival","Minivan sold as the Sedona in North America, with short and long wheelbases from the second generation.",a="Sedona",dt="generation · wheelbase"),
  X("Toyota Alphard","Toyota","2002–","Toyota_Alphard","Large seven- or eight-seat MPV and Toyota's flagship people carrier, hybrid since 2003.",dt="generation · hybrid or petrol · seating"),
 ],
 "m":[["X9","XPENG"]]},
{"n":"City car","a":"A-segment · minicar","d":"Smallest class of full-size passenger car, built for town driving and parking.",
 "t":["two-seat","four-seat","three-door","five-door"]+PT,"s":W+"A-segment",
 "x":[
  X("Citroën 2CV","Citroën","1948–1990","Citro%C3%ABn_2CV","Air-cooled, front-wheel-drive French economy car conceived to motorise rural France.",a="deux chevaux",dt="engine size · colour · special editions"),
  X("Fiat 500","Fiat","1957–1975","Fiat_500","Inexpensive two-door rear-engined city car, launched as the Nuova 500.",a="Nuova 500 · Cinquecento · Bambino",
    v=[V("Fiat 500 (2007)","Fiat","2007","retro A-segment city car, Type 312; hatchback and convertible")],dt="saloon or semi-convertible · colour"),
  X("Mini","BMC","1959–2000","Mini","Two-door, four-seat small car built by BMC and successors over a single generation.",a="Austin Seven · Morris Mini-Minor",
    v=[V("Mini Hatch (new Mini)","Mini","2001","retro-styled BMW-era supermini, four generations")],dt="saloon · estate · Cooper · colour"),
  X("Fiat Panda","Fiat","1980–","Fiat_Panda","City car launched as a two-box three-door hatchback designed by Giugiaro and Mantovani.",
    v=[V("first generation","Fiat","1980–2003","4x4 from 1983"),V("second generation","Fiat","2003","five-door, Bertone design")],dt="generation · 4x4"),
  X("Renault Twingo","Renault","1992–2024","Renault_Twingo","City car made across three generations.",dt="generation · colour"),
  X("Smart Fortwo","Smart","1998–2024","Smart_Fortwo","Two-seat rear-engined city car from Mercedes-Benz and Swatch.",dt="generation · coupé or cabrio · electric"),
  X("Toyota Aygo","Toyota","2005–2022","Toyota_Aygo","A-segment city car built alongside the Citroën C1 and Peugeot 107/108 in Kolín.",dt="generation · three/five-door"),
  X("Volkswagen Up","Volkswagen","2011–2023","Volkswagen_Up","City car rebadged as the SEAT Mii and Škoda Citigo.",a="up! · SEAT Mii · Škoda Citigo",dt="three/five-door · e-up!"),
 ]},
]
def B(n,c,f,seg,d,sig): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":[],"s":"knowledge"}
brands=[
 B("Volkswagen","Germany","1937","mass-market","German volume carmaker, core brand of the Volkswagen Group.",["Volkswagen Beetle","Volkswagen Golf","Volkswagen Passat"]),
 B("Renault","France","1899","mass-market","French volume carmaker.",["Renault 4","Renault 5","Renault Espace"]),
 B("Ford","United States","1903","mass-market","American volume carmaker with a large European arm.",["Ford Fiesta","Ford Cortina"]),
 B("Toyota","Japan","1937","mass-market","Japanese volume carmaker and pioneer of mass-market hybrids.",["Toyota Corolla","Toyota RAV4"]),
 B("Peugeot","France","1810","mass-market","French carmaker, part of Stellantis.",["Peugeot 205"]),
 B("Honda","Japan","1948","mass-market","Japanese maker of cars and motorcycles.",["Honda Civic","Honda Accord"]),
 B("Mazda","Japan","1920","mass-market","Japanese carmaker.",["Mazda2"]),
 B("Nissan","Japan","1933","mass-market","Japanese volume carmaker.",["Nissan Leaf","Nissan Qashqai"]),
 B("Fiat","Italy","1899","mass-market","Italian carmaker known for small cars, part of Stellantis.",["Fiat 500","Fiat Panda"]),
 B("Citroën","France","1919","mass-market","French carmaker, part of Stellantis.",["Citroën 2CV"]),
 B("BMC","United Kingdom","1952","historic mass-market","British Motor Corporation, the merger of Austin and Morris.",["Mini"]),
 B("Mini","United Kingdom","1959","premium small car","Small-car marque owned by BMW since 1994.",["Mini Hatch"]),
 B("Smart","Germany","1994","city car","City-car marque begun by Mercedes-Benz and Swatch.",["Smart Fortwo"]),
 B("Mercedes-Benz","Germany","1926","luxury","German luxury car marque.",["Mercedes-Benz W123","Mercedes-Benz C-Class"]),
 B("BMW","Germany","1916","premium","German premium car and motorcycle maker.",["BMW 3 Series"]),
 B("Tesla","United States","2003","electric","American maker of battery-electric cars.",["Tesla Model 3","Tesla Model Y"]),
 B("Volvo","Sweden","1927","premium","Swedish carmaker known for safety and estates.",["Volvo 200 Series"]),
 B("Škoda","Czech Republic","1895","mass-market","Czech carmaker in the Volkswagen Group.",["Škoda Octavia"]),
 B("Subaru","Japan","1953","mass-market","Japanese carmaker known for all-wheel drive.",["Subaru Outback"]),
 B("Land Rover","United Kingdom","1948","off-road and luxury SUV","British maker of four-wheel-drive vehicles.",["Range Rover"]),
 B("Jeep","United States","1941","off-road and SUV","American four-wheel-drive brand, part of Stellantis.",["Jeep Cherokee XJ"]),
 B("Chevrolet","United States","1911","mass-market","American General Motors brand.",["Chevrolet Suburban"]),
 B("Audi","Germany","1909","premium","German premium marque in the Volkswagen Group.",["Audi Q7"]),
 B("Kia","South Korea","1944","mass-market","South Korean carmaker in the Hyundai Motor Group.",["Kia Carnival"]),
 B("Chrysler","United States","1925","mass-market","American carmaker, part of Stellantis.",["Chrysler minivans"]),
 B("XPENG","China","2014","electric","Chinese maker of electric cars.",[]),
]
notes=("Kept all 5 old kinds and added City car (sourced to Wikipedia A-segment). Archetypes = model lines with generations as versions (Golf Mk1–Mk8, Corolla E210, Range Rover Classic/L322, Fiat 500 1957/2007, Mini/new Mini). "
 "Powertrain and size classes moved into t. Dropped from Saloon: Maybach S-Class and S-Class Saloon (go to Luxury saloon on the Luxury cars shelf); trimmed the Mercedes-heavy list to C-Class as an archetype plus A-Class Saloon and CLA as flat models. "
 "Mercedes V-Class/Viano/EQV kept as versions of a V-Class archetype sourced to the Vito article (no separate page retrieved, so no years). XPENG X9 left as a flat model (Wikipedia page not found). "
 "Range Rover Classic is also an off-roader; listed here per shelf brief, Off-roader shelf may cross-link. Brand entries use s=knowledge (country/founding only). No traditions apply. Golf Mk3–Mk6 years from their own Wikipedia pages.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/G1/shelves/00_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
