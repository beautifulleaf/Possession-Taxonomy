import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=(),a='',dt=''):
    o={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':[dict(zip(('n','mk','y','d'),t)) for t in v]}
    if dt: o['dt']=dt
    return o
kinds=[]
kinds.append({'n':'Off-roader','a':'4×4 · four-wheel drive · off-road vehicle · overlander','d':'Four-wheel-drive vehicle built for unpaved and low-traction terrain, usually body-on-frame with low-range gearing.',
 't':['short wheelbase','long wheelbase','soft top','hard top','station wagon','pickup or cab chassis'],'s':W+'Off-road_vehicle','x':[
 X('Willys MB','Willys Jeep · Ford GPW · G-503','Second World War quarter-ton 4×4 utility vehicle; the first mass-produced four-wheel-drive car.','Willys','1941–1945',W+'Willys_MB',[('Ford GPW','Ford','1941–1945','licence-built twin of the MB')]),
 X('Jeep CJ','Civilian Jeep · Universal Jeep','Open-bodied civilian evolution of the wartime Jeep, built by successive Jeep owners.','Jeep','1945–1986',W+'Jeep_CJ',[('CJ-2A','Jeep','1945–1949','first civilian Jeep'),('CJ-3A','Jeep','1949–1953',''),('CJ-3B','Jeep','1953–1968',''),('CJ-5','Jeep','1954–1983',''),('CJ-6','Jeep','1955–1981',''),('CJ-7','Jeep','1976–1986',''),('CJ-8 Scrambler','Jeep','1981–1986','pickup')]),
 X('Land Rover Series','Series Land Rover · Series I, II, III','British aluminium-bodied box-frame 4×4 inspired by the wartime Jeep; first civilian 4×4 with doors and a hard roof.','Land Rover','1948–1985',W+'Land_Rover_series',[('Series I','Land Rover','1948–1958','80, 86, 88, 107 and 109 in wheelbases'),('Series II','Land Rover','1958–1961','88 and 109 in'),('Series IIA','Land Rover','1961–1971','88 and 109 in'),('Series III','Land Rover','1971–1985','88 and 109 in')],dt='wheelbase 80–109 in · soft top, hard top, station wagon, pickup'),
 X('Land Rover Defender','One Ten · Ninety · Defender 90/110/130','Coil-sprung successor to the Series Land Rover, built 1983–2016 and revived as a new generation in 2020.','Land Rover','1983–2016; 2020–',W+'Land_Rover_Defender',[('One Ten','Land Rover','1983','renamed Defender 110 in 1990'),('Ninety','Land Rover','1984','renamed Defender 90'),('One Two Seven','Land Rover','1985','renamed Defender 130'),('Heritage','Land Rover','1998','styled after the 1948 Series I'),('SVX','Land Rover','2008','60th anniversary edition'),('Defender Works V8 70th Anniversary','Land Rover','2018','150 built'),('Defender (L663) 90/110/130','Land Rover','2020','new generation'),('Defender OCTA','Land Rover','2024','twin-turbo V8')],dt='wheelbase 90, 110, 130 · station wagon, hard top, pickup, double cab'),
 X('Toyota Land Cruiser 40 Series','J40 · FJ40 · BJ40','Two-door body-on-frame Land Cruiser with two-speed transfer case, in short, medium and long wheelbases.','Toyota','1960–1985 (Brazil to 2001)',W+'Toyota_Land_Cruiser_(J40)',[('J40/41/42','Toyota','','short wheelbase'),('J43/44/46','Toyota','','medium wheelbase'),('J45/47','Toyota','','long wheelbase')]),
 X('Toyota Land Cruiser 70 Series','J70 · LC70','Heavy-duty Land Cruiser that replaced the 40 Series, kept in production for work and off-road use.','Toyota','1984–',W+'Toyota_Land_Cruiser_(J70)',dt='wagon, troop carrier, pickup, cab chassis'),
 X('Toyota Land Cruiser station wagon','J60 · J80 · J100 · J200 · J300','Full-size Land Cruiser wagon line that grew from utility vehicle into a luxury 4×4.','Toyota','1967–',W+'Toyota_Land_Cruiser',[('FJ55 (50 series)','Toyota','1967–1980',''),('J60','Toyota','1980–1990',''),('J80','Toyota','1990–2007',''),('J100','Toyota','1998–2007','basis of the Lexus LX 470'),('J200','Toyota','2007',''),('J300','Toyota','2021','')]),
 X('Lada Niva','VAZ-2121 · Lada 4×4 · Niva Legend','Soviet compact monocoque 4×4 with permanent four-wheel drive, in production since 1977.','Lada','1977–',W+'Lada_Niva',[('VAZ-2121','Lada','1977–1994','1.6 L original'),('VAZ-21213 / 21214','Lada','1994–','1.7 L'),('VAZ-2131','Lada','1995–','five-door long wheelbase'),('Lada 4×4 Urban','Lada','2014',''),('Niva Legend','Lada','2021','renamed original generation')]),
 X('Mercedes-Benz G-Class','G-Wagen · Geländewagen · Puch G','Boxy body-on-frame 4×4 with three locking differentials, developed as a military vehicle and later made luxurious.','Mercedes-Benz','1979–',W+'Mercedes-Benz_G-Class',[('W460','Mercedes-Benz','1979–1991','original; sold as Puch G in some markets'),('W461','Mercedes-Benz','1985–2022','utility and military'),('W463','Mercedes-Benz','1990–2018','luxury civilian'),('G 63 AMG','Mercedes-Benz','2012',''),('G 500 4×4²','Mercedes-Benz','','portal-axle variant'),('W463 second generation','Mercedes-Benz','2018–2024',''),('W465 / G 580 with EQ Technology','Mercedes-Benz','2024','electric')]),
 X('Jeep Wrangler','YJ · TJ · JK · JL','Open-bodied solid-axle Jeep that continued the CJ line from 1986.','Jeep','1986–',W+'Jeep_Wrangler',[('YJ','Jeep','1986–1995','square headlamps, leaf springs'),('TJ','Jeep','1997–2006','coil springs; Unlimited from 2004'),('JK','Jeep','2007–2018','four-door Unlimited'),('JL','Jeep','2018–','4xe plug-in hybrid; Rubicon 392')],dt='two- or four-door · Sport, Sahara, Rubicon trims'),
 X('Suzuki Jimny','LJ10 · SJ410/SJ413 Samurai · JA11 · JB23','Small ladder-frame 4×4 begun as a kei car, also built in larger export versions.','Suzuki','1970–',W+'Suzuki_Jimny',[('LJ10','Suzuki','1970','359 cc two-stroke kei'),('LJ80','Suzuki','','797 cc four-stroke'),('SJ410 / SJ413 Samurai','Suzuki','1981–1998','second generation'),('JA11','Suzuki','1990','660 cc kei'),('JB23 / JB43','Suzuki','1998–2018','third generation'),('Fourth generation','Suzuki','2018','five-door version added')]),
 X('Range Rover','Range Rover Classic','Luxury 4×4 line launched by British Leyland in 1970, now a Land Rover sub-brand.','Land Rover','1970–',W+'Range_Rover'),
]})
kinds.append({'n':'Pickup truck','a':'pickup · ute · bakkie','d':'Light truck with an enclosed cab and an open load bed behind it.',
 't':['single cab','extended cab','double cab','compact or mid-size','full-size','heavy duty'],'s':'https://www.vansdirect.co.uk/new-vans-in-stock','x':[
 X('Ford F-Series','F-100 · F-150 · Super Duty','Full-size American pickup line built since 1948; the F-150 is its best-selling model.','Ford','1948–',W+'Ford_F-Series',[('First generation (Bonus-Built)','Ford','1948–1952',''),('F-100','Ford','1953–1983','half-ton'),('F-150','Ford','1975','added in sixth generation'),('SVT Lightning','Ford','1993–1995; 1999–2004','performance'),('Super Duty','Ford','1999','F-250 to F-450'),('SVT Raptor / Raptor','Ford','2010–2014; 2017–','off-road'),('Thirteenth generation','Ford','2015–2020','aluminium body'),('F-150 Lightning','Ford','2021','electric')]),
 X('Toyota Hilux','Hi-Lux · HiLux','Japanese compact-to-mid-size pickup sold worldwide since 1968, known for durability.','Toyota','1968–',W+'Toyota_Hilux',[('N10','Toyota','1968','first generation'),('N20','Toyota','1972',''),('N30/N40','Toyota','1978','4WD from 1979'),('N50/N60/N70','Toyota','1983','Xtracab introduced'),('N80–N110','Toyota','1988',''),('AN10/AN20/AN30','Toyota','2004','IMV platform'),('AN110/AN120/AN130','Toyota','2015','eighth generation; Invincible'),('AN220/AN230','Toyota','2025','ninth generation')]),
 X('Chevrolet Silverado','C/K successor · GMC Sierra twin','Full-size GM pickup line introduced for 1999, twinned with the GMC Sierra.','Chevrolet','1999–',W+'Chevrolet_Silverado'),
 X('Ram pickup','Dodge Ram','Full-size pickup sold as the Dodge Ram from 1981 and under the Ram Trucks brand from 2010.','Ram','1981–',W+'Ram_pickup'),
 X('Ford Ranger','T6 Ranger','Compact, later mid-size, Ford pickup sold globally; the T6 version was developed by Ford Australia.','Ford','1983–',W+'Ford_Ranger'),
 X('Toyota Tacoma','','North American Toyota pickup, compact at first and mid-size since 2005.','Toyota','1995–',W+'Toyota_Tacoma'),
 X('Nissan Navara','Frontier · NP300 · D21, D22, D40, D23','Nissan pickup nameplate used across generations D21 to D27.','Nissan','',W+'Nissan_Navara'),
 X('Isuzu D-Max','','Isuzu pickup built since 2002, sharing platforms with the Chevrolet Colorado and Mazda BT-50.','Isuzu','2002–',W+'Isuzu_D-Max'),
 X('Volkswagen Amarok','','Mid-size body-on-frame Volkswagen pickup built since 2010.','Volkswagen','2010–',W+'Volkswagen_Amarok'),
 ],'m':[['Shark','BYD']]})
kinds.append({'n':'Kit car','a':'component car · self-build car','d':'Car sold as a set of parts for the owner to assemble, often with a donor engine and gearbox.',
 't':['component car','replica','donor-based','turnkey build'],'s':W+'Kit_car','x':[
 X('Caterham Seven','Lotus Seven · Caterham 7','Lightweight two-seat open sports car designed by Colin Chapman, built by Caterham since 1973 as car or kit.','Caterham','1957 (Lotus); 1973– (Caterham)',W+'Caterham_7',[('Lotus Seven','Lotus','1957','original'),('Series 3 Twin Cam','Caterham','1974–1983',''),('Superlight R500','Caterham','1999–2005',''),('CSR','Caterham','2005','independent rear suspension'),('Seven 160','Caterham','2013–2016','Suzuki kei engine'),('Seven 620','Caterham','2013','supercharged'),('Seven 360 / 420','Caterham','2015',''),('Seven 170','Caterham','2021',''),('Super Seven 600 / 2000','Caterham','2022','retro styling')],dt='SV wide or narrow chassis · Roadsport, Superlight, R trims'),
 X('Westfield Seven-type','Westfield XI · SEight · Sport','British Seven-style kit car range, from the Lotus Eleven-inspired XI to V8 SEight and motorcycle-engined Mega models.','Westfield','1982–',W+'Westfield_Sportscars',[('XI','Westfield','1982–1986; 2004–2010',''),('SEight','Westfield','1991–2010','V8'),('FW400','Westfield','1999–2002',''),('Megabusa','Westfield','','motorcycle engine'),('Sport 250','Westfield','','')]),
 X('Factory Five Roadster','Cobra replica · Mk4 Roadster','American kit replica of the 1960s Cobra roadster, the best-known Factory Five model.','Factory Five Racing','',W+'Factory_Five_Racing',[('Mark IV Roadster','Factory Five Racing','2010',''),('Mark V Roadster','Factory Five Racing','2025','Coyote 5.0 support'),('Type 65 Coupe','Factory Five Racing','2000','Daytona coupé replica'),('GTM Supercar','Factory Five Racing','',''),('818','Factory Five Racing','2013','own design'),("'33 Hot Rod",'Factory Five Racing','','')]),
 X('Ultima','Ultima GTR · Evolution','British mid-engined kit supercar line from Hinckley, sold as kit or complete car.','Ultima Sports','1983–',W+'Ultima_Sports',[('Mk3','Ultima Sports','1989','PRV V6'),('Sport','Ultima Sports','1992–1999',''),('Spyder','Ultima Sports','1992–1999','roadster'),('GTR','Ultima Sports','',''),('Can-Am','Ultima Sports','','roadster'),('Evolution','Ultima Sports','','coupé and convertible')]),
 X('Sterling Nova','Purvis Eureka','Low wedge-shaped kit coupé on a Volkswagen Beetle floorpan, about 10,000 sold.','Sterling','1972',W+'Kit_car'),
 ]})
kinds.append({'n':'Hot rod and custom car','a':'hot rod · street rod · rat rod · lowrider · kustom','d':'Older car rebuilt for speed or style, typically with a bigger engine, lowered stance and custom bodywork.',
 't':['traditional','street rod','highboy','chopped roof','channelled','pro-street'],'s':W+'Hot_rod','x':[
 X('Ford Model T speedster and T-bucket','T-bucket · T roadster','Stripped Model T roadster, the base of the first hot rods and of the open T-bucket style.','Ford','1910s–1920s',W+'Hot_rod'),
 X('Ford Model A hot rod','A-bone','Model A roadster or coupé, among the most common early hot rod bases.','Ford','1928–1931',W+'Ford_Model_A_(1927%E2%80%931932)'),
 X("1932 Ford 'Deuce'",'Deuce · Little Deuce Coupe · Model 18','The 1932 Ford, first low-priced car with a V8; the defining hot rod base after the Second World War.','Ford','1932',W+'1932_Ford',[('Model 18','Ford','1932','flathead V8'),('Model B','Ford','1932','four-cylinder'),('Roadster','Ford','1932','most sought-after body'),('Five-window coupé','Ford','1932','most common hot rod coupé'),('Three-window coupé','Ford','1932','rarer, suicide doors'),('Reproduction bodies','','','fibreglass or steel')]),
 X('Street rod','','Pre-1949-style hot rod built for road comfort rather than racing, the dominant style from the 1970s.','','1970s–',W+'Hot_rod'),
 X('Rat rod','','Custom car built from cheap or salvaged parts and left deliberately rough, often unpainted and rusty.','','early 1990s',W+'Rat_rod'),
 X('Lowrider','','Car lowered close to the ground, often with hydraulics, wire wheels and painted graphics; rooted in Chicano car culture.','','late 1940s–',W+'Lowrider',[('1958 Chevrolet Impala','Chevrolet','1958','X-frame suited to lowering'),('1964 Chevrolet Impala','Chevrolet','1964',''),('1948 Chevrolet Fleetline','Chevrolet','1948',''),('1966 Chevrolet Caprice','Chevrolet','1966',''),('1988 Cadillac Fleetwood Brougham','Cadillac','1988','')],dt='hydraulics · wire wheels and whitewalls · custom paint'),
 ]})
kinds.append({'n':'Kei car','a':'kei jidōsha · light automobile','d':'Japanese ultra-compact car class limited to 3.4 m length, 1.48 m width and 660 cc.',
 't':['kei hatchback','kei sports car','tall-roof kei','kei off-roader'],'s':W+'Kei_car','x':[
 X('Subaru 360','','Considered the first truly mass-produced kei car.','Subaru','1958–1970',W+'Kei_car'),
 X('Honda N360','N600 · NIII 360','Front-wheel-drive two-box kei saloon that spurred rapid growth in passenger kei cars.','Honda','1967–1972',W+'Honda_N360',[('N360','Honda','1967',''),('NIII 360','Honda','1970','facelift'),('N600','Honda','','larger-engined export version')]),
 X('Suzuki Alto','','Kei hatchback that set the tone for kei cars through the 1980s.','Suzuki','1979–',W+'Kei_car'),
 X('Honda Beat','','Mid-engined two-seat kei roadster designed by Pininfarina; the last car approved by Soichiro Honda.','Honda','1991–1996',W+'Honda_Beat'),
 X('Suzuki Cappuccino','','Front-engined rear-drive two-seat kei roadster with a detachable hardtop.','Suzuki','1991–1998',W+'Suzuki_Cappuccino'),
 X('Autozam AZ-1','Mazda AZ-1 · PG6SA · Suzuki Cara','Mid-engined gullwing-door kei sports car sold under Mazda\'s Autozam brand with a Suzuki turbo engine.','Autozam','1992–1994',W+'Autozam_AZ-1'),
 X('Daihatsu Copen','','Kei roadster with a folding hard top.','Daihatsu','2002–2012; 2014–',W+'Kei_car'),
 X('Honda S660','','Mid-engined kei sports car.','Honda','2015–2022',W+'Kei_car'),
 X('Honda N-Box','','High-roof kei with sliding doors, one of Japan\'s top sellers.','Honda','',W+'Kei_car'),
 ]})
kinds.append({'n':'Microcar','a':'bubble car · quadricycle · voiturette · cyclecar','d':'Very small car with three or four wheels and a tiny engine or motor, often under separate licensing rules.',
 't':['bubble car','light quadricycle','heavy quadricycle','electric'],'s':'https://www.ligier.cz/new-vehicles/new-vehicles-microcar?lang=en','x':[
 X('Isetta','Iso Isetta · BMW Isetta · bubble car','Egg-shaped bubble car with a front-opening door, designed by Iso and built under licence in many countries.','Iso','1953',W+'Isetta',[('Iso Isetta','Iso','1953–1956','original'),('BMW Isetta 250','BMW','1955',''),('BMW Isetta 300','BMW','1956',''),('VELAM Isetta','VELAM','1955–1958','France'),('Romi-Isetta','Romi','1956–1961','Brazil'),('BMW Isetta (UK three-wheeler)','BMW','1957–1962','Isetta of Great Britain'),('Microlino','Microlino','2022','electric reinterpretation')]),
 X('Messerschmitt KR200','Kabinenroller','Tandem two-seat three-wheeled bubble car with an aircraft-style canopy, designed by Fritz Fend.','Messerschmitt','1955–1964',W+'Messerschmitt_KR200'),
 X('Peel P50','','Single-seat three-wheeled microcar from the Isle of Man, listed as the smallest production car ever made.','Peel Engineering Company','1962–1965; 2010–',W+'Peel_P50'),
 X('Renault Twizy','Twizy 45 · Twizy 80','Two-seat tandem electric quadricycle sold in light (45) and heavy (80) versions.','Renault','2012–2023',W+'Renault_Twizy',[('Twizy 45','Renault','','light quadricycle, 4 kW'),('Twizy 80','Renault','','heavy quadricycle, 13 kW')]),
 X('Citroën Ami','Ami One','Two-seat electric quadricycle with a 28 mph top speed that can be driven without a car licence in France from 14.','Citroën','2020',"https://www.zapmap.com/citroen-ami-urban-ev-launched/"),
 ],'m':[['Dué','Microcar']]})
kinds.append({'n':'Three-wheeled car','a':'tricar · three-wheeler · cyclecar','d':'Car with three wheels, either one at the front or one at the rear; some are legally classed as motorcycles.',
 't':['single front wheel','single rear wheel','motorcycle-engined'],'s':W+'Three-wheeler','x':[
 X('Léon Bollée Voiturette','','Early French three-wheeled car.','Léon Bollée','1895',W+'Three-wheeler'),
 X('Morgan 3-Wheeler','Morgan three-wheeler · Super 3','Morgan\'s V-twin and four-cylinder three-wheelers, revived in 2012 with an S&S V-twin and succeeded by the Super 3.','Morgan','1911–1952; 2012–',W+'Morgan_3-Wheeler',[('V-Twin three-wheelers','Morgan','1911–1939',''),('F-Series','Morgan','1932–1952','four-cylinder'),('3 Wheeler','Morgan','2012–2021','S&S 1983 cc V-twin'),('P101','Morgan','2021','run-out edition'),('Super 3','Morgan','2022','')]),
 X('Bond Bug','','Wedge-shaped two-seat three-wheeler with a lift-up canopy, designed by Tom Karen of Ogle Design.','Bond','1970–1974',W+'Bond_Bug'),
 X('Reliant Robin','Robin Mk1, Mk2, Mk3','Fibreglass three-wheeled car from Tamworth that replaced the Reliant Regal.','Reliant','1973–2002',W+'Reliant_Robin',[('Mk1','Reliant','1973–1981','748 cc, then 850 cc'),('Mk2','Reliant','1989','revamped'),('Mk3','Reliant','1999–2001','redesign')]),
 X('Campagna T-Rex','','Canadian two-seat three-wheeled roadster.','Campagna','1996–',W+'Three-wheeler'),
 X('Vanderhall Venice','','American three-wheeled roadster.','Vanderhall','2017–',W+'Three-wheeler'),
 ]})
def B(n,c,f,seg,d,s,sig=(),lines=(),rel=()):
    o={'n':n,'c':c,'f':f,'seg':seg,'d':d,'s':s}
    if sig:o['sig']=list(sig)
    if lines:o['lines']=list(lines)
    if rel:o['rel']=list(rel)
    return o
K='knowledge'
brands=[
 B('Willys','United States','','Utility vehicles (historic)','Maker of the wartime Willys MB Jeep.',W+'Willys_MB',['Willys MB'],rel=['Jeep','Ford']),
 B('Jeep','United States','1941','Off-roaders and SUVs','American 4×4 marque descended from the wartime Willys Jeep, now part of Stellantis.',K,['Jeep CJ','Jeep Wrangler'],rel=['Willys','Ram']),
 B('Land Rover','United Kingdom','1948','Off-roaders and luxury SUVs','British 4×4 marque, now part of Jaguar Land Rover.',K,['Land Rover Series','Land Rover Defender','Range Rover']),
 B('Toyota','Japan','1937','Mass-market cars, off-roaders and pickups','Japanese carmaker.',K,['Toyota Land Cruiser 40 Series','Toyota Land Cruiser 70 Series','Toyota Hilux']),
 B('Mercedes-Benz','Germany','1926','Premium and luxury cars','German premium car marque.',K,['Mercedes-Benz G-Class']),
 B('Lada','Russia','1970','Budget cars and off-roaders','Car brand of AvtoVAZ.',K,['Lada Niva']),
 B('Suzuki','Japan','1909','Small cars, kei cars and off-roaders','Japanese maker of small cars and motorcycles.',K,['Suzuki Jimny','Suzuki Cappuccino','Suzuki Alto']),
 B('Ford','United States','1903','Mass-market cars and pickups','American carmaker.',K,['Ford F-Series','Ford Ranger',"1932 Ford 'Deuce'",'Ford Model A hot rod']),
 B('Chevrolet','United States','1911','Mass-market cars and pickups','General Motors\' mainstream marque.',K,['Chevrolet Silverado','Lowrider']),
 B('Ram','United States','2010','Pickup trucks','Pickup brand spun off from Dodge in 2010, part of Stellantis.',W+'Ram_pickup',['Ram pickup'],rel=['Jeep']),
 B('Nissan','Japan','1933','Mass-market cars and pickups','Japanese carmaker.',K,['Nissan Navara']),
 B('Isuzu','Japan','','Pickups and commercial vehicles','Japanese maker of pickups and trucks.',K,['Isuzu D-Max']),
 B('Volkswagen','Germany','1937','Mass-market cars','German carmaker.',K,['Volkswagen Amarok']),
 B('Lotus','United Kingdom','1948','Lightweight sports cars','British sports car maker founded by Colin Chapman.',K,['Caterham Seven'],rel=['Caterham']),
 B('Caterham','United Kingdom','1973','Lightweight sports and component cars','Dartford maker that bought the Lotus Seven rights in 1973 and has built the Seven since.',W+'Caterham_7',['Caterham Seven'],rel=['Lotus','Westfield']),
 B('Westfield','United Kingdom','1982','Kit cars','Seven-style kit car maker, based in Bicester since 2022.',W+'Westfield_Sportscars',['Westfield Seven-type'],rel=['Caterham']),
 B('Factory Five Racing','United States','1995','Kit cars','Wareham, Massachusetts maker of Cobra replica and original-design kit cars.',W+'Factory_Five_Racing',['Factory Five Roadster']),
 B('Ultima Sports','United Kingdom','1983','Kit supercars','Hinckley maker of mid-engined kit supercars.',W+'Ultima_Sports',['Ultima']),
 B('Subaru','Japan','1953','Mass-market cars','Japanese carmaker.',K,['Subaru 360']),
 B('Honda','Japan','1948','Cars and motorcycles','Japanese maker of cars and motorcycles.',K,['Honda N360','Honda Beat','Honda S660','Honda N-Box']),
 B('Autozam','Japan','','Small cars (historic Mazda channel)','Mazda sales brand that sold the AZ-1.',W+'Autozam_AZ-1',['Autozam AZ-1'],rel=['Suzuki']),
 B('Daihatsu','Japan','1907','Kei and small cars','Japanese small-car maker, owned by Toyota.',K,['Daihatsu Copen']),
 B('Iso','Italy','','Microcars and GT cars (historic)','Italian firm that designed and first built the Isetta.',W+'Isetta',['Isetta'],rel=['BMW']),
 B('BMW','Germany','1916','Premium cars and motorcycles','German premium carmaker that built the Isetta under licence.',K,['Isetta'],rel=['Iso']),
 B('Messerschmitt','Germany','','Aircraft; bubble cars (historic)','West German aircraft maker whose factory built the KR200.',W+'Messerschmitt_KR200',['Messerschmitt KR200']),
 B('Peel Engineering Company','Isle of Man','','Microcars','Isle of Man maker of the P50.',W+'Peel_P50',['Peel P50']),
 B('Renault','France','1899','Mass-market cars','French carmaker.',K,['Renault Twizy']),
 B('Citroën','France','1919','Mass-market cars','French carmaker, part of Stellantis.',K,['Citroën Ami']),
 B('Microcar','France','','Quadricycles','Quadricycle brand sold through Ligier dealers.','https://www.ligier.cz/new-vehicles/new-vehicles-microcar?lang=en',rel=['Ligier']),
 B('Ligier','France','','Microcars','French maker specialising in microcars, founded by Guy Ligier.',W+'Ligier',rel=['Microcar']),
 B('Morgan','United Kingdom','1910','Traditional sports cars and three-wheelers','Malvern maker of hand-built sports cars and three-wheelers.',K,['Morgan 3-Wheeler']),
 B('Reliant','United Kingdom','','Three-wheelers (historic)','Tamworth maker of fibreglass three-wheelers.',W+'Reliant_Robin',['Reliant Robin'],rel=['Bond']),
 B('Bond','United Kingdom','','Microcars and three-wheelers (historic)','British maker of the Bond Bug, later built at Reliant\'s Tamworth factory.',W+'Bond_Bug',['Bond Bug'],rel=['Reliant']),
]
notes=('Old kinds kept: Pickup truck (k12; old source kept; BYD Shark kept as flat model, Ranger and Hilux became archetypes) and Microcar (k9; old Ligier source; Microcar Dué kept). '
 'New kinds: Off-roader, Kit car, Hot rod and custom car, Kei car, Three-wheeled car. Suzuki Jimny sits under Off-roader (kei version noted). '
 'Left out: Mitsubishi Triton/L200, Westfield founder name, Highboy/T-bucket definitions as archetypes beyond the Model T entry, Land Cruiser J80 specifics beyond years, Autozam founding year, any models not confirmed on a retrieved page; Wikipedia API was rate-limited (429) so several pages were fetched via WebFetch. '
 'Brands with "s":"knowledge": Jeep, Land Rover, Toyota, Mercedes-Benz, Lada, Suzuki, Ford, Chevrolet, Nissan, Isuzu, Volkswagen, Lotus, Subaru, Honda, Daihatsu, BMW, Renault, Citroën, Morgan.')
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':notes}
p='work/G1/shelves/00_03.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
print(sum(len(k.get('x',[])) for k in kinds),'archetypes',len(brands),'brands')
