# round 2 data; exec'd inside build.py after ADD/VADD are defined
WB=lambda s:'https://watchbase.com/'+s
M.update({
 'Sinn':('Germany','Lothar Schmidt','Independent','1994'),
 'Oris':('Switzerland','Oris SA (privately held)','Independent','1982'),
 'Orient':('Japan','Seiko Epson','Independent','2001'),
 'F.P. Journe':('Switzerland','F.P. Journe (Chanel holds 20 %)','Independent',''),
 'MB&F':('Switzerland','Maximilian Büsser and partners (Chanel holds 25 %)','Independent',''),
 'Richard Mille':('Switzerland','Richard Mille Group (private)','Independent',''),
 'Glashütte Original':('Germany',SW,'Global group','2000'),
 'Rado':('Switzerland',SW,'Global group','1968'),
 'Montblanc':('Germany',RI,'Global group','1993'),
 'Piaget':('Switzerland',RI,'Global group','1988'),
 'Breguet':('France',SW,'Global group','1999'),
 'Waltham':('United States',NS,'',''),
 'ETA':('Switzerland',SW,'Global group',''),
 'Valjoux':('Switzerland',SW,'Global group',''),
 'Miyota':('Japan','Citizen Watch Co.','National champion',''),
 'Sellita':('Switzerland',NS,'',''),
})
CTY['Urwerk']='Switzerland'
def A(kind,*es): ADD.setdefault(kind,[]).extend(es)
P=S
# --- Sinn
SI=WP+'Sinn_(watchmaker)'
A('Chronograph',N('142 S','Sinn','1992','Chronograph flown on the Mir \'92 mission.',SI),N('140 S','Sinn','1985','Sinn chronograph of 1985.',SI),N('EZM 10 TESTAF','Sinn','','Pilot chronograph.',SI))
A('Dive watch',N('U2 (EZM 5)','Sinn','','Sinn diving watch.',SI),N('UX','Sinn','','Sinn diving watch.',SI),N('EZM 3','Sinn','','Sinn tool watch listed on the maker page.',SI))
A('Pilot watch',N('356 Flieger II','Sinn','','Sinn pilot watch.',SI),N('900 Pilot','Sinn','2010','Award-winning Sinn pilot watch.',SI))
A('GMT & world-time watch',N('144 GMT','Sinn','','Sinn GMT watch.',SI),N('857 UTC','Sinn','','Sinn UTC chronograph.',SI))
A('Dress watch',N('6100 Regulateur','Sinn','2008','Regulator-dial Sinn in rose gold.',SI),N('Frankfurt Financial District Watch','Sinn','2006','Sinn watch honoured in 2006 (white gold) and 2012 (platinum).',SI))
# --- Oris
OR=WP+'Oris_SA'
A('Dive watch',N('Aquis','Oris','2011','Oris diver launched in 2011.',OR),N('Divers Sixty-Five','Oris','2015','Oris diver of 2015.',OR))
A('Pilot watch',N('Big Crown','Oris','1938','Oris pilot line, with the Pointer Date as a later model.',OR),N('ProPilot','Oris','2023','ProPilot Altimeter of 2023.',OR))
A('GMT & world-time watch',N('Artelier Worldtimer','Oris','2004','Oris world-time watch of 2004.',OR))
# --- Nomos
NO=WP+'Nomos_Glash%C3%BCtte'
A('Dress watch',*[N(n,'Nomos Glashütte',y,'Nomos line, founded 1990.',NO) for n,y in [('Club','2007'),('Orion','1992'),('Ludwig','1992'),('Metro','2014'),('Zürich','2009'),('Lambda','2013')]])
# --- Orient
A('Dress watch',N('Orient Star','Orient','1951','Orient\'s upper line, first released 1951; Retro-Future collection 2005.',WP+'Orient_Watch'))
# --- F.P. Journe
FJ=WP+'F.P._Journe'
A('Calendar watch',N('Octa Calendrier','F.P. Journe','2002','Octa calendar, GPHG Special Jury Prize 2002.',FJ),N('Octa Lune','F.P. Journe','2003','Octa moon-phase watch, GPHG Men\'s Watch Prize 2003.',FJ))
# --- Urwerk
UW='https://urwerk.com/story'
A('Avant-garde watch',N('UR-101','Urwerk','1997','Urwerk\'s first model, launched at Baselworld 1997.',UW),N('UR-202','Urwerk','2008','Urwerk watch of 2008.',UW),N('UR-105','Urwerk','2014','UR-105M is the earliest UR-105.',UW),N('UR-210','Urwerk','2012','Urwerk watch of 2012.',UW),N('EMC','Urwerk','2013','Urwerk EMC of 2013.',UW),N('AMC','Urwerk','2017','Urwerk AMC of 2017.',UW))
# --- Richard Mille
RM=WP+'Richard_Mille'
A('Tourbillon watch',N('RM 027 Rafael Nadal','Richard Mille','2007','Weighed 20 g with strap.',RM,v=[{'n':'RM 27-03 Tourbillon Rafael Nadal','y':'2017'}]),N('RM 006 Felipe Massa Tourbillon','Richard Mille','2004','48 g without strap.',RM),N('RM 009 Felipe Massa Tourbillon','Richard Mille','2005','29 g.',RM),N('RM 50-03 McLaren F1','Richard Mille','2017','Shown at SIHH; 38 g with strap.',RM),N('RM 71-01 Talisman','Richard Mille','2018','Automatic tourbillon, late 2018.',RM))
A('Avant-garde watch',N('RM 011','Richard Mille','2007','RM 011 Starck made for Only Watch 2007; Felipe Massa editions followed.',RM),N('RM 67-02','Richard Mille','2026','Topuria is ambassador.',RM))
# --- MB&F versions
VADD['Horological Machine']=[('HM1','2007',''),('HM4 Thunderbolt','2010','award year'),('HM6','2015','Red Dot award year'),('HM10 Bulldog','2020','')]
VADD['Legacy Machine']=[('LM1','2011',''),('LM Perpetual','2015',''),('LM FlyingT','2019',''),('LM Sequential EVO','2022','')]
# --- Glashutte Original
GO=WP+'Glash%C3%BCtte_Original'
A('Dress watch',N('Senator','Glashütte Original','','Glashütte Original range; Senator Sixties is a named model.',GO),N('PanoMaticLunar','Glashütte Original','','Pano range model.',GO),N('Spezialist','Glashütte Original','','Glashütte Original range.',GO),N('Vintage','Glashütte Original','','Glashütte Original range.',GO))
# --- Rado
RA=WP+'Rado_(watchmaker)'
A('Everyday watch',N('DiaStar 1','Rado','1962','Rado\'s first scratch-proof watch, 1962.',RA),N('Ceramica','Rado','1990','Rado ceramic line, 1990.',RA),N('HyperChrome','Rado','','Rado line named on the maker page.',RA))
A('Dive watch',N('Captain Cook','Rado','1962','Rado diver of 1962.',RA))
# --- Montblanc
MBL=WP+'Montblanc_(company)'
A('Field watch',N('1858','Montblanc','2007','Villeret 1858 collection, released 2007.',MBL))
A('Chronograph',N('Star Nicolas Rieussec','Montblanc','','Monopusher chronograph, the first Montblanc-branded watch made entirely at Le Locle.',MBL))
# --- Piaget / Breguet / Blancpain
PI=WP+'Piaget_SA'
A('Dress watch',N('Altiplano','Piaget','','Piaget ultra-thin line from the 1990s; the 900P followed in 2014.',PI))
A('Jewellery watch',N('Limelight','Piaget','','Piaget line from the 1990s.',PI),N('Possession','Piaget','','Piaget line from the 1990s.',PI))
A('Shaped watch',N('Emperador','Piaget','1957','Piaget cushion line launched 1957, relaunched 1999.',PI))
BR=WP+'Breguet_(brand)'
A('Dress watch',N('Classique','Breguet','','Round Breguet pieces.',BR),N('Tradition','Breguet','','Breguet line similar to the Souscription.',BR))
A('Dive watch',N('La Marine','Breguet','','Water-resistant Breguet with crown guards.',BR))
A('Jewellery watch',N('Reine de Naples','Breguet','','Breguet ladies\' line.',BR))
A('Shaped watch',N('Heritage','Breguet','','Breguet line with tonneau cases.',BR))
BL=WP+'Blancpain'
A('Dress watch',N('Villeret','Blancpain','','Blancpain flagship line since the 1980s.',BL),N('Léman','Blancpain','1994','Blancpain line from 1994 to 2019.',BL))
# --- TAG Heuer (Watchbase + wiki)
TH=WB('tag-heuer'); HW_=S['heuer']
A('Chronograph',*[N(n,'Heuer',y,d,s) for n,y,d,s in [
 ('Monza','','Heuer line listed on Watchbase; Monza is also named among the early-1970s automatics.',TH),
 ('Silverstone','','Early-1970s Heuer automatic chronograph.',HW_),
 ('Montreal','','Early-1970s Heuer automatic chronograph.',HW_),
 ('Jarama','','Early-1970s Heuer automatic chronograph.',HW_),
 ('Cortina','','Mid-1970s Heuer chronograph with the Lemania 5100.',HW_),
 ('Calculator','','Early-1970s Heuer automatic chronograph.',HW_),
 ('Kentucky','1977','Heuer chronograph with the Valjoux 7750.',HW_),
 ('Pasadena','1977','Heuer chronograph with the Valjoux 7750.',HW_),
 ('Seafarer','','Early-1950s Heuer model.',HW_),
 ('Auto-Graph','1953','Heuer model of 1953 to 1954.',HW_),
 ('Mareographe','','Early-1950s Heuer model.',HW_),
 ('Targa Florio','',"Heuer line listed on Watchbase.",TH),
 ('Grand Carrera','','TAG Heuer line listed on Watchbase.',TH)]])
A('Everyday watch',N('Kirium','Heuer','','TAG Heuer line listed on Watchbase.',TH),N('2000','Heuer','','TAG Heuer line listed on Watchbase.',TH),N('6000','Heuer','','TAG Heuer line listed on Watchbase.',TH))
A('Integrated-bracelet sports watch',N('S/EL','Heuer','','TAG Heuer line listed on Watchbase.',TH))
A('Jewellery watch',N('Alter Ego','Heuer','','TAG Heuer ladies\' line listed on Watchbase.',TH))
# --- Cartier
CW=WB('cartier')
A('Prestige everyday watch',N('Calibre de Cartier','Cartier','','Cartier line listed on Watchbase.',CW),N('Ronde de Cartier','Cartier','','Cartier line listed on Watchbase.',CW))
A('Calendar watch',N('Rotonde de Cartier','Cartier','','Cartier line listed on Watchbase, with calendar and complication versions.',CW))
A('Jewellery watch',N('Clé de Cartier','Cartier','','Cartier line listed on Watchbase.',CW))
VADD['Santos']=[('Santos de Cartier','',''),('Santos-Dumont','','')]
VADD['Tank']=VADD['Tank']+[('Tank Must','','')]
# --- Patek
PW=WB('patek-philippe')
A('Shaped watch',N('Gondolo','Patek Philippe','','Patek Philippe line listed on Watchbase.',PW))
A('Jewellery watch',N('Twenty~4','Patek Philippe','','Patek Philippe ladies\' line listed on Watchbase.',PW))
A('Integrated-bracelet sports watch',N('Cubitus','Patek Philippe','','Patek Philippe line listed on Watchbase.',PW))
# --- AP
AW=WB('audemars-piguet')
A('Shaped watch',N('Millenary','Audemars Piguet','','AP line listed on Watchbase.',AW))
A('Dress watch',N('Jules Audemars','Audemars Piguet','','AP line listed on Watchbase.',AW),N('Classique','Audemars Piguet','','AP line listed on Watchbase.',AW),N('(re)Master','Audemars Piguet','','AP line listed on Watchbase.',AW))
A('Jewellery watch',N('Haute Joaillerie','Audemars Piguet','','AP line listed on Watchbase.',AW))
A('Jumping-hours watch',N('Neo Frame','Audemars Piguet','','AP jumping-hour line listed on Watchbase.',AW))
# --- IWC
IW=WB('iwc')
A('Dive watch',N('Aquatimer','IWC Schaffhausen','','IWC line listed on Watchbase (GST Aquatimer).',IW))
A('Calendar watch',N('Da Vinci','IWC Schaffhausen','1986','IWC line; the Ref. 3750 perpetual of 1986 (Watchbase names Kurt Klaus\'s 1985 module).',IW))
A('Jumping-hours watch',N('Pallweber','IWC Schaffhausen','','IWC tribute line to the digital Pallweber pocket watch, listed on Watchbase.',IW))
# --- JLC
JW=WB('jaeger-lecoultre')
A('Dress watch',N('Master Ultra Thin','Jaeger-LeCoultre','','JLC line listed on Watchbase.',JW))
A('Grande-complication watch',N('Master Grande Tradition','Jaeger-LeCoultre','','JLC line listed on Watchbase.',JW))
A('Dive watch',N('Master Compressor','Jaeger-LeCoultre','','JLC line (Master Extreme on Watchbase), named on the JLC page as inspired by the Polaris.',JW))
A('Chronograph',N('AMVOX','Jaeger-LeCoultre','','JLC line listed on Watchbase.',JW))
A('Chronometer watch',N('Duomètre','Jaeger-LeCoultre','','JLC line listed on Watchbase.',JW))
A('Jewellery watch',N('Rendez-Vous','Jaeger-LeCoultre','','JLC ladies\' line listed on Watchbase.',JW))
# --- Omega (Watchbase + wiki)
OW=WB('omega')
A('Dive watch',N('Seamaster 120M','Omega','1998','Seamaster 120M Analog-Digital, 1998.',S['omega']))
A('Everyday watch',N('Dynamic','Omega','','Omega line listed on Watchbase.',OW))
A('Dress watch',N('Trésor','Omega','','Omega line listed on Watchbase.',OW))
A('Jewellery watch',N('LadyMatic','Omega','','Omega ladies\' line listed on Watchbase.',OW))
A('Digital watch',N('X-33','Omega','','Omega X-33 / Z-33; an X-33 was worn on Artemis II (2026).',OW))
VADD['Speedmaster Professional']=[('Speedmaster Moonwatch','1969','worn on the Moon by Buzz Aldrin'),("Speedmaster '57",'2022',''),('Speedmaster Broad Arrow','',''),('Speedmaster Chronoscope','',''),('Speedmaster Dark Side of the Moon','',''),('Speedmaster First Omega in Space','',''),('Speedmaster Pilot','',''),('Speedmaster Reduced','','')]
VADD['Constellation']=[('Constellation Observatory','',''),('Constellation Manhattan','1980s','quartz day-date')]
# --- Breitling (Watchbase)
BW=WB('breitling')
A('Pilot watch',*[N(n,'Breitling','','Breitling line listed on Watchbase.',BW) for n in ['Airwolf','Avenger','AVI','Cockpit','Skyracer','Windrider']])
A('Chronograph',N('Chrono-Matic','Breitling','','Breitling line listed on Watchbase.',BW),N('Super Chronomat','Breitling','','Breitling line listed on Watchbase.',BW))
A('GMT & world-time watch',N('Chronoliner','Breitling','','Breitling line listed on Watchbase.',BW))
A('Field watch',N('Endurance Pro','Breitling','','Breitling line listed on Watchbase.',BW))
A('Digital watch',N('Exospace','Breitling','','Breitling line listed on Watchbase.',BW))
A('Everyday watch',N('Galactic','Breitling','','Breitling line listed on Watchbase.',BW))
A('Dress watch',N('Montbrillant','Breitling','','Breitling line listed on Watchbase.',BW),N('Premier','Breitling','','Breitling line listed on Watchbase.',BW),N('Transocean','Breitling','','Breitling line listed on Watchbase.',BW))
VADD['Superocean']=[('Superocean Heritage','',''),("Superocean Heritage '57",'','')]
# --- Rolex (Watchbase)
RW=WB('rolex')
A('Everyday watch',N('Date','Rolex','','Rolex line listed on Watchbase.',RW),N('Perpetual Padellone','Rolex','','Rolex line listed on Watchbase.',RW))
A('Prestige everyday watch',N('Lady-Datejust','Rolex','','Rolex line listed on Watchbase.',RW))
A('Jewellery watch',N('Pearlmaster','Rolex','','Rolex line listed on Watchbase.',RW))
# --- trench and skeleton
A('Trench watch',N('Waltham trench watch','Waltham','1914','Waltham wristwatch with a shrapnel guard, shown in the Wikipedia trench watch article.',WP+'Trench_watch'))
A('Skeleton watch',N('Santos de Cartier Skeleton','Cartier','','Santos de Cartier Large Skeleton, listed on Watchbase.',CW),N('Crash Skeleton','Cartier','','Cartier Crash Skeleton in pink gold and platinum, listed on Watchbase.',CW),N('Monaco Skeleton Racing','Heuer','','Monaco Calibre Heuer 02 Titanium skeleton, listed on Watchbase.',TH))
# --- movement kind
MV=[
 N('ETA 2824-2','ETA','1982','Automatic, 25 jewels, 28,800 vph, about 38 h reserve; grades Standard, Elaborated, Top, Chronometer.','https://calibercorner.com/eta-caliber-2824-2/'),
 N('ETA 2892-A2','ETA','','Automatic, 21 jewels, 28,800 vph, 42 h; dates to the 1970s.',WP+'List_of_ETA_Movements'),
 N('ETA 2893','ETA','','Automatic GMT family, 21 jewels, 28,800 vph, 42 h (2893-1 to -3).',WP+'List_of_ETA_Movements'),
 N('ETA 2836-2','ETA','','Automatic day-date, 25 jewels, 28,800 vph, 38 h.',WP+'List_of_ETA_Movements'),
 N('ETA 2671','ETA','','Automatic, 25 jewels, 28,800 vph, 38 h.',WP+'List_of_ETA_Movements'),
 N('Valjoux 7750','Valjoux','1970','Automatic cam-system chronograph developed by Edmond Capt from the Valjoux 7733; 25 jewels, 28,800 vph, 48 h.',S['valjoux'] if 'valjoux' in S else WP+'Valjoux_7750'),
 N('Unitas 6497','ETA','','Hand-wound, 17 jewels; -1 at 18,000 vph and 46 h, -2 at 21,600 vph and 56 h; 6498 is the small-seconds sibling.',WP+'List_of_ETA_Movements'),
 N('Powermatic 80','ETA','2012','Announced at Baselworld 2012 with an 80-hour reserve; used by Tissot, Hamilton and Certina.',WP+'ETA_SA'),
 N('Sellita SW200-1','Sellita','2008','Automatic, 26 jewels, 28,800 vph, 38 to 41 h; an ETA 2824-2 clone.','https://calibercorner.com/sellita-caliber-sw200-1'),
 N('Seiko NH35','Seiko','2011','Made by Seiko Instruments and sold by TMI: 24 jewels, 21,600 bph, 41 h; earliest documentation is dated 2011.','https://calibercorner.com/seiko-caliber-nh35a'),
 N('Miyota 8215','Miyota','','Automatic, 21 jewels, 21,600 bph, over 40 h; 26 mm.',WP+'Miyota_(watch_movement_manufacturer)'),
 N('Miyota 9015','Miyota','','Automatic, 24 jewels, 28,800 bph, 3.90 mm thick, 42 h or more.',WP+'Miyota_(watch_movement_manufacturer)'),
 N('Rolex 3135','Rolex','1988','Automatic, 31 jewels, 28,800 vph, 48 h; in the Submariner, Sea-Dweller, Yacht-Master and Datejust.','https://calibercorner.com/rolex-caliber-3135/'),
 N('Omega 2500','Omega','1999','First mass-produced Omega with the co-axial escapement, 28,800 vph; the 2500C runs at 25,200.',WP+'Co-axial_escapement'),
 N('Zenith El Primero','Zenith','1969','Automatic chronograph movement unveiled on 10 January 1969.',S['zenith'],role='origin'),
 N('Seiko Spring Drive','Seiko','1999','Announced 1997; Grand Seiko 9R65 in 2004, 9RA5 in 2020.',S['seiko']),
 N('Grand Seiko 9S85','Grand Seiko','2009','Hi-beat movement restoring 36,000 vph; the 9S86 added a GMT in 2014.',S['gseiko']),
]
