# kind|name|first-flight year|maker|source id (Wikidata QID or page key)|extra
# kinds: SEP single piston, MEP multi piston, TP turboprop, JET jet, LSA, HB homebuilt, AERO, FLOAT, WAR, GLI, MG motor-glider, HELI, GYRO
W="https://www.wikidata.org/wiki/"
RAW="""
SEP|Cessna 150|1957|Cessna|Q1057117
SEP|Cessna 152||Cessna|Q2348731
SEP|Cessna 140|1945|Cessna|Q1057084
SEP|Cessna 170|1948|Cessna|Q767382
SEP|Cessna 180 Skywagon|1952|Cessna|Q1057101
SEP|Cessna 185 Skywagon|1960|Cessna|Q1057123
SEP|Cessna 195|1945|Cessna|Q1057137
SEP|Cessna 206||Cessna|Q1057183
SEP|Cessna 177 Cardinal|1966|Cessna|Q1057100
SEP|Cessna 210 Centurion|1957|Cessna|Q1057193
SEP|Cessna 162 Skycatcher|2006|Cessna|Q1057063
SEP|Cessna 160|1962|Cessna|Q5065560
SEP|Cessna 187|1968|Cessna|Q5065561
SEP|Cessna 188|1965|Cessna|Q5065564
SEP|Cessna 207|1968|Cessna|Q10447208
SEP|Cessna Model A|1927|Cessna|Q3665640
SEP|Piper PA-12 Super Cruiser||Piper|Q2096450
SEP|Piper PA-15 Vagabond|1948|Piper|Q740146
SEP|Piper PA-18 Super Cub|1949|Piper|Q672488
SEP|Piper PA-20 Pacer||Piper|Q7197310
SEP|Piper PA-25 Pawnee||Piper|Q1650274
SEP|Piper PA-38 Tomahawk||Piper|Q1419887
SEP|Piper PA-46 Malibu, Mirage and Meridian|1979|Piper|Q1809515
SEP|Taylor Cub||Piper|Q2397869
SEP|Piper J-4 Cub Coupe||Piper|Q4046989
SEP|Beechcraft Musketeer|1963|Beechcraft|Q814007
SEP|Beechcraft Skipper|1975|Beechcraft|Q455074
SEP|Beechcraft Staggerwing|1932|Beechcraft|Q814004
SEP|Beechcraft Travel Air|1956|Beechcraft|Q752104
SEP|Cirrus SR20|1995|Cirrus|PAGE:Cirrus
SEP|Diamond DA20|1991|Diamond|Q929944
SEP|Diamond DA40 Diamond Star|1997|Diamond|Q1208678
SEP|Mooney M-18 Mite|1947|Mooney|PAGE:Mooney
SEP|Mooney M22 Mustang|1964|Mooney|PAGE:Mooney
SEP|Aeronca 11 Chief||Aeronca|Q2825653
SEP|Aeronca 15 Sedan||Aeronca|Q2825654
SEP|Aeronca C-2||Aeronca|Q2825658
SEP|Aeronca C-3||Aeronca|Q4033480
SEP|Aeronca L-3||Aeronca|Q381590
SEP|Aeronca L-16||Aeronca|Q4688374
SEP|Luscombe 8||Luscombe|Q3267782
SEP|Maule M-5||Maule|Q6792452
SEP|Tecnam P92||Tecnam|Q1335867
SEP|Tecnam P96 Golf|1996|Tecnam|Q3982418
SEP|Tecnam P2010|2012|Tecnam|Q2399653
SEP|Grob G 115||Grob|Q671321
SEP|Lancair 320||Lancair|Q6482962
SEP|Lancair Legacy||Lancair|Q6482967
SEP|Lancair ES||Lancair|Q6482964
SEP|Lancair Evolution||Lancair|Q6482966
MEP|Beechcraft Twin Bonanza|1949|Beechcraft|Q814003
MEP|Beechcraft Queen Air|1958|Beechcraft|Q814005
MEP|Beechcraft Duke|1966|Beechcraft|Q814001
MEP|Beechcraft Duchess|1974|Beechcraft|Q2893628
MEP|Beechcraft 18|1937|Beechcraft|Q814006
MEP|Cessna 310 and 320|1953|Cessna|Q1057187
MEP|Cessna 335|1970|Cessna|Q2530939
MEP|Cessna 401 and 402||Cessna|Q1057203
MEP|Cessna 404 Titan|1975|Cessna|Q1057252
MEP|Cessna 414|1968|Cessna|Q1057233
MEP|Cessna 421 Golden Eagle|1965|Cessna|Q164293
MEP|Cessna Skymaster|1961|Cessna|Q1057388
MEP|Piper PA-23 Apache and Aztec|1952|Piper|Q441585
MEP|Piper PA-30 Twin Comanche|1962|Piper|Q1414859
MEP|Piper PA-31 Navajo|1964|Piper|Q745036
MEP|Piper Aerostar|1967|Piper|Q175092
MEP|Diamond DA42 Twin Star|2002|Diamond|Q370418
TP|Beechcraft Super King Air 200|1972|Beechcraft|Q1094597
TP|Beechcraft Starship|1986|Beechcraft|Q814015
TP|Cessna 208 Caravan|1982|Cessna|Q1056131
TP|Cessna 425 Conquest I|1978|Cessna|Q1057259
TP|Cessna 441 Conquest II|1974|Cessna|Q1057265
TP|Piper PA-42 Cheyenne III and 400|1979|Piper|Q268269
TP|Piper PA-31T Cheyenne|1969|Piper|Q1582144
TP|Pilatus PC-6 Porter|1959|Pilatus|Q689011
JET|Beechcraft Premier|1998|Beechcraft|Q753672
JET|Hawker 400||Beechcraft|Q1591669
JET|Diamond D-Jet|2006|Diamond|Q285545
JET|Cirrus Vision SF50|2008|Cirrus|PAGE:Cirrus
WAR|Beechcraft T-34 Mentor|1948|Beechcraft|Q2343923
WAR|Cessna O-1 Bird Dog|1949|Cessna|Q541116
WAR|Cessna T-50 Bobcat|1939|Cessna|Q2667635
WAR|Cessna T-37 Tweet|1954|Cessna|Q495337
WAR|Cessna A-37 Dragonfly|1963|Cessna|Q488204
WAR|Cessna L-19/O-2 Skymaster|1967|Cessna|Q2622196
HB|Rutan VariEze||Rutan|Q370967
HB|Rutan Quickie||Rutan|Q3453595
HB|Rutan Defiant||Rutan|Q3453591
HB|Rutan VariViggen||Rutan|Q1583082
MG|Pipistrel Virus||Pipistrel|Q2096497
MG|Pipistrel Velis Electro||Pipistrel|Q96399449
MG|Pipistrel Panthera||Pipistrel|Q3389032
MG|Grob G 109 (additional record)||Grob|Q1417838
HELI|Robinson R66|2007|Robinson|PAGE:Robinson
"""
CIT_VERS=[("Citation I","1969","Q937707"),("Citation II","1977","Q1057340"),("Citation III","1979","Q1057324"),("Citation X","1993","Q1057430"),("Citation Excel","1996","Q673038"),("Citation Sovereign","2002","Q848809"),("Citation Mustang","2005","Q1057385"),("CitationJet 526","1993","Q5065566"),("Citation Latitude","2014","Q1057283"),("Citation Longitude","2016","Q5065573"),("Citation M2","","Q2030444"),("Citation CJ2","","Q9737563")]
KINGAIR_V=[("King Air 90","1963","Q15838655"),("King Air 65-90","1965","Q15838789"),("King Air 100","1969","Q15838892"),("King Air E90","1972","Q15838878"),("King Air F90","1978","Q15838880"),("Super King Air 200","1972","Q1094597"),("King Air 300","","Q15618511"),("King Air 360","","Q106340724")]
BON_V=[("Bonanza 35","","Q18177033"),("Bonanza A35","","Q18177035"),("Model 33 Debonair/Bonanza","","Q15888160"),("Bonanza G36","","Q29369836"),("A36TC Bonanza","","Q29369568")]
BARON_V=[("Baron 55","1960","Q18194200"),("Baron 56","","Q18194305"),("Baron A55","","Q18194488"),("Baron B55","","Q18194493"),("Baron C55","","Q18194579"),("Baron D55","","Q18194663"),("Baron E55","","Q18194665")]
# Schleicher page (no years): name|class|maker-fact
SCHL="""
Ka 1|single-seat trainer
Ka 2|two-seat trainer
Ka 3|single-seat trainer
Ka 4|two-seat trainer
Ka 6|Standard Class
K 7|two-seat trainer
K 10|Standard Class
ASK 13|two-seat trainer
ASK 18|Club Class
ASK 23|Club Class
ASW 12|Open Class
ASW 15|Standard Class
ASW 17|Open Class
ASW 19|Standard Class
ASW 20|15 metre Class
ASW 22|Open Class
ASW 24|Standard Class
ASW 27|15 metre Class
ASH 25|two-seat Open Class
ASH 26|18 metre Class, often motorised
ASH 31|Open and 18 metre Classes
ASG 32|two-seater
AS 33|15 and 18 metre Classes, successor to the ASG 29
"""
SCHL_MG="""
ASK 14|single-seat touring motor glider
ASK 16|two-seat touring motor glider
ASH 30 Mi|two-seat Open Class, motorised, replaces the ASH 25
AS 34 Me|15/18 metre Classes, self-launching electric motor glider
AS 35 Mi|18 metre and Open Classes, self-launching, replaces the ASH 31
"""
SCHH="""
Göppingen Gö 1 Wolf|1935|first product, meant to rival the Grunau Baby
Göppingen Gö 3 Minimoa|1936|brought the company its success
Göppingen Gö 4|1938|two-seat sailplane
Standard Austria||wooden
SHK||wooden
Open Cirrus||GRP
Standard Cirrus||GRP
Mini-Nimbus||GRP
Janus||GRP
Quintus||GRP
"""
# versions of existing Schempp-Hirth entries (page lists them as separate models, no years except Wikidata)
SH_VERS={"Discus":[("Discus-2","1998","Q7888128")],"Ventus":[("Ventus-2","","Q7887991"),("Ventus-3","2016","Q27901564")],"Nimbus":[("Nimbus-2","",""),("Nimbus-3","",""),("Nimbus-4","1990","Q3475327")]}
MAVIC=[("Mavic Pro","2016","first in the series, with a foldable design"),("Mavic Pro Platinum","2017","longer flight time (30 minutes) and quieter propellers"),("Mavic 2 Pro and Zoom","2018","Pro has a 20 MP Hasselblad camera; Zoom has 4x zoom"),("Mavic 2 Enterprise","2018","swappable modules and a 6x zoom camera"),("Mavic 2 Enterprise Dual","2018","adds a FLIR thermal camera"),("Mavic 2 Enterprise Advanced","2021","48 MP camera and RTK support"),("Mavic 3","2021","first with a telephoto camera beside the wide-angle camera; up to 46 minutes"),("Mavic 3 Cine","2021","ProRes 422 HQ video to a 1 TB internal SSD"),("Mavic 3 Classic","2022","cheaper version without the telephoto camera"),("Mavic 3E and 3T Enterprise","2022","3T adds a thermal camera"),("Mavic 3M Multispectral","2022","agriculture model with a four-lens multispectral camera"),("Mavic 3 Pro and Pro Cine","2023","first DJI drone with three optical cameras"),("Mavic 3T Advanced","2025","upgraded thermal camera"),("Mavic 4 Pro","2025","three cameras on a 360-degree gimbal; 51 minutes"),("Raptor and Raptor T (licensed)","2024","Malaysia-built licensed Mavic 3E and 3T by Anzu Robotics; discontinued February 2026")]
MOONEY_M20=[("M20","1953","11,000+ built"),("M20A","1958","first with 180 hp; last wooden wing and tail"),("M20B","1960","first all-metal M20"),("M20C Ranger","1962",""),("M20D Master","1963","fixed-gear trainer; 141 built"),("M20E Super 21","1964","fuel-injected 200 hp"),("M20E Chaparral","1969","electric flaps and landing gear"),("M20F Executive","1974","revived the line after Republic Steel bought the company"),("M20J 201","1970s","first production aircraft to reach 201 mph on 200 hp"),("M20K 231","1979","turbocharged"),("M20M TLS","1989","turbocharged Lycoming Sabre; produced to 1995"),("M20R Ovation","1994","280 hp Continental IO-550"),("M20M Bravo","1996",""),("M20K Encore","1997",""),("M20TN Acclaim","2006","Garmin G1000 glass cockpit"),("M20TN Acclaim Type S","2007","242 knots, fastest single-piston production aircraft at the time"),("M20V Acclaim Ultra / M20U Ovation Ultra","2017","newest models on the page")]
