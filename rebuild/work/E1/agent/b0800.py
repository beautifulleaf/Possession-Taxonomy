import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
BR=WP+'Brio_(company)'; PL=WP+'Plarail'; TO=WP+'Tonka'; BD=WP+'Bruder_(toy_manufacturer)'; CC=WP+'Cozy_Coupe'; FP=WP+'Fisher-Price'; RFH='https://www.radioflyer.com/heritage/'; ST='https://striderbikes.com/?p=178820'; WO='https://woom.com/en_BE/company/history-of-woom'; RF=WP+'Radio_Flyer'; LT=WP+'Little_Tikes'; TR=WP+'Tricycle'; GT='https://trellis.net/article/milk-jugs-toy-trucks-green-toys-hit-whole-foods-moms/'; BA=WP+'Balance_bike'
pv=K('Push-along or pull-back toy vehicle','A small plastic, metal or wooden vehicle the child pushes or that runs by pull-back, friction or a small battery motor without a track or remote.',TO,a='Mini 4WD · pull toy · toy truck',
 t=['Steel construction truck','Plastic 1:16 farm and construction vehicle','Recycled-plastic vehicle','Pull-back / friction','Wooden pull-along','Die-cast (see Models, kits & railways)'],
 x=[X('Tonka truck','Pressed-steel construction trucks from Mound Metalcraft, Minnesota; in the Toy Hall of Fame since 2001.','Tonka','1946',TO,[('Mound Metalcraft toy sideline','Tonka','1946',''),('Renamed Tonka Toys Incorporated','Tonka','1955',''),('Sold to Hasbro','Tonka','1991',''),('Basic Fun! licence','Basic Fun!','2019','Funrise held it 1998-2019')],dt='size · steel or plastic · vehicle type'),
    X('Bruder 1:16 vehicles','German plastic farm, construction and emergency vehicles in 1:16 scale.','Bruder','1926',BD,[('Small plastic toys','Bruder','1958',''),('bworld play system','Bruder','2011','figures and accessories'),('Professional series','Bruder','','Caterpillar, John Deere, Scania models'),('Roadmax series','Bruder','','simpler, for younger children')]),
    X('Fisher-Price pull toys','Wood and steel push-pull toys with lithographed labels, first sold in 1931.','Fisher-Price','1930',FP,[('Dr. Doodle','Fisher-Price','1931','first toy sold'),('Play Family / Little People','Fisher-Price','1960s','')]),
    X('Green Toys','Trucks, rockets and tea sets from recycled HDPE milk jugs.','Green Toys','2007',GT)])
wr=K('Wooden toy railway','A wooden toy train with its wooden track system.',BR,
 t=['Magnetic couplings','Battery locomotive','Licensed (Thomas & Friends)','Starter set','Expansion pack'],
 x=[X('BRIO railway','Swedish wooden train and track system, sold in Europe since 1958.','Brio','1958',BR,[('BRIO acronym name','Brio','1908','Bröderna Ivarsson i Osby'),('Thomas & Friends licence in Europe','Brio','1996','to 2001; Learning Curve held the US licence'),('Ravensburger takes over BRIO','Ravensburger','2015','8 January')],dt='track type · locomotive · licensed theme · set size'),
    X('Thomas & Friends Wooden Railway','Wooden trains of the Thomas range; US rights were with Learning Curve while BRIO held parts of Europe.','Learning Curve','',BR)],
 m=[['BRIO Railway Starter Set','Brio'],['BRIO Space Deluxe Train Set','Brio'],['BRIO Expansion Pack Beginner','Brio']],r=[['BRIO World','Brio']])
pr=K('Plastic toy railway','A plastic toy train, usually battery-driven, with its own snap-together plastic track system, not built to a model scale.',PL,
 t=['Battery locomotive','Hand-pushed','Thomas range (TrackMaster)','Shinkansen / real-train range','Track-compatible with wooden rail'],
 x=[X('Plarail','Japanese plastic train and track system from Tomy, launched 1959 with three hand-powered trains.','Takara Tomy','1959',PL,
      [('Plastic Railroad Set','Tomy','1959','steam locomotive, three freight cars, figure-8 track'),('Electric Pla-Train Set','Tomy','1961','battery-powered, October'),('D51 Kisha','Tomy','1971','first train based on a real locomotive'),('Thomas & Friends line','Tomy','1992','later TrackMaster under other companies'),('Shinkalion','Takara Tomy','2015','robot train range')],dt='range (Advance, Big Plarail) · battery · licensed theme'),
    X('GeoTrax','Fisher-Price plastic railway, 2002-2011, compatible with the earlier Flip Track.','Fisher-Price','2002',FP)])
rc=K('Ride-on car','A child-sized car pushed, pedalled or powered, that the child sits in.',CC,
 t=['Foot-powered','Pedal','Battery-powered','Push-along with handle'],
 x=[X('Cozy Coupe','Red-and-yellow moulded-plastic foot-powered car designed by Jim Mariol; one of the best-selling cars.','Little Tikes','1979',CC,[('Cozy Coupe II','Little Tikes','1998','thicker roof pillars, remote with sounds'),('1996 range extensions','Little Tikes','1996','roadster, minivan, SUV, pickups, Grand Coupe')]),
    X('Power Wheels','Long-running battery ride-on line by Fisher-Price.','Fisher-Price','1985',FP)],
 m=[['Little Tikes Cozy Coupe','Little Tikes'],['Freddo Beast XL','Freddo Toys'],['Freddo Rocket','Freddo Toys']])
bb=K('Balance bike','A child\'s bike without pedals, pushed along with the feet.',BA,t=['12-inch wheels (2-5 years)','14-inch wheels (3+)','Aluminium','Steel','Wooden','Plastic','Wheeled ride-on (Ziggle)'],
 x=[X('Draisine / Laufmaschine','Karl Drais\'s pedal-less wooden two-wheeler of 1817, ancestor of the balance bike.','','1817',BA),
    X('KOKUA Laufrad','First commercially produced children\'s running bike.','KOKUA Bikes','1997',BA,[('Rolf Mertens','KOKUA Bikes','1997','')]),
    X('Strider','US balance bike brand, "the original balance bike truly built for kids".','Strider','2007',ST,[('12 Sport','Strider','','toddler balance bike')]),
    X('woom balance bikes','Austrian lightweight balance bikes from the woom company.','woom','2013',WO,[('woom 1','woom','2013','balance bike'),('woom WOW','woom','','balance bike')])],
 m=[['Strider 14X Sport','Strider'],['woom GO 1','woom'],['woom GO 1 PLUS','woom'],['woom WOW','woom'],['Freddo Nature Navigator Balance Bike','Freddo Toys']],r=[['woom GO','woom'],['Zoomee','TP Toys']])
tc=K("Children's tricycle","A three-wheeled pedalled cycle for a young child. A children's pedal bicycle is in Vehicles.",TR,
 t=['Front-drive','Chain-drive','With push bar','Convertible (2-in-1, 4-in-1)','Metal','Plastic','Wooden'],
 x=[X('Radio Flyer tricycle','Radio Flyer began with wooden wagons and tricycles built in a Chicago workshop.','Radio Flyer','1917',RF)],
 m=[['Zoomee 2 in 1 Trike','TP Toys'],['Zoomee 4 in 1 Deluxe Trike','TP Toys'],['Zoomee 4 in 1 Trike','TP Toys'],['Zoomee Balance Bike to Trike','TP Toys']],r=[['Zoomee','TP Toys']])
wg=K('Ride-on wagon','A child-sized pull or push wagon that children ride in or load.',RF,a='red wagon',t=['Steel','Plastic','Folding','Wood'],
 x=[X('Radio Flyer wagon','Red wagon that began as the wooden Liberty Coaster; steel and assembly-line from 1927.','Radio Flyer','1923',RF,[('Liberty Coaster Company formed','Radio Flyer','1923',''),('Stamped steel','Radio Flyer','1927',''),('Radio Steel & Manufacturing','Radio Flyer','1930','Radio Flyer name used for metal wagons')])])
brands=[B('Brio','Sweden','1884','Heritage manufactory','wooden railway','Swedish wooden toy company, best known for its railway since 1958; owned by Ravensburger.',BR,sig=['BRIO railway']),
 B('Takara Tomy','Japan','2006','Mainstream','Plarail','Japanese toy maker formed from Takara and Tomy.',PL,sig=['Plarail']),
 B('Tonka','United States','1946','Heritage manufactory','steel trucks','Minnesota toy truck brand, owned by Hasbro since 1991.',TO,sig=['Tonka truck']),
 B('Bruder','Germany','1926','Specialist','1:16 vehicles','Family-owned Fürth maker of 1:16 plastic toy vehicles.',BD,sig=['Bruder 1:16 vehicles']),
 B('Fisher-Price','United States','1930','Mainstream','preschool toys','Founded by Herman Fisher, Irving Price, Margaret Evans Price and Helen Schelle; Mattel since 1993.',FP,sig=['Fisher-Price pull toys']),
 B('Little Tikes','United States','1967','Mainstream','moulded plastic toys','Ohio maker of the Cozy Coupe; MGA Entertainment since 2006.',LT,sig=['Cozy Coupe']),
 B('Radio Flyer','United States','1917','Heritage manufactory','red wagon','Chicago maker founded by Antonio Pasin.',RF,sig=['Radio Flyer wagon']),
 B('Strider','United States','2007','Specialist','balance bikes','US balance bike brand.',ST,sig=['Strider']),
 B('woom','Austria','2013','Specialist','lightweight kids bikes','Vienna company founded by Christian Bezdeka and Marcus Ihlenfeld.',WO,sig=['woom balance bikes']),
 B('Green Toys','United States','2007','Specialist','recycled-plastic toys','Founded by Robert von Goeben and Laurie Hyman.',GT),
 B('KOKUA Bikes','Germany','','Specialist','first Laufrad','Brand of Rolf Mertens\'s 1997 running bike.',BA),
 B('Learning Curve','United States','','Mainstream','Thomas Wooden Railway','Held the US Thomas & Friends wooden railway licence.',BR)]
write('08_00',[pv,wr,pr,rc,bb,tc,wg],brands,[],'Added Ride-on wagon kind (Radio Flyer, in brief). Mini 4WD kept as alias only; Mini 4WD is listed in the Models shelf. Learning Curve and Thomas Wooden Railway years omitted (only in unfetched search snippets); cited via Brio article. TP Toys/Zoomee, Freddo kept from old data as m/r only; no retrieved page. Takara Tomy founding per prior shelf.')
