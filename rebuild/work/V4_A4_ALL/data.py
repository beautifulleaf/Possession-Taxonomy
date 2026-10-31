# new entries: (dept, kind, name, aliases, d, mk, y, source, versions[(n,y,d)], dt)
W='https://en.wikipedia.org/wiki/'
HER='https://www.hermes.com/dk/en/content/310339-hermes-iconic-bag-lines/'
DIOR='https://www.dior.com/en_us/fashion/bags/womens-bags-line'
CHA='https://www.chanel.com/us/fashion/handbags/the-chanel-handbag/'
CEL='https://www.celine.com/en-us/celine-shop-women/handbags/'
PRA='https://www.prada.com/ww/en/womens/bags/c/10062EU/page/3'
LOE='https://www.loewe.com/usa/en/women/bags/bags-by-line'
FEN='https://www.fendi.com/us-en/woman/bags?start=0&sz=24'
LV='https://us.louisvuitton.com/eng-us/women/handbags'
H='Handbags'
N=[]
def a(dept,kind,n,mk,y,s,d='',al='',v=None,dt=''):
    N.append(dict(dept=dept,kind=kind,n=n,mk=mk,y=y,s=s,d=d,a=al,v=[dict(n=x[0],mk=mk,y=x[1],d=x[2]) for x in (v or [])],dt=dt))
# Hermès
for n,k in [('Della Cavalleria','Shoulder bag'),('Herbag','Tote bag'),('Jypsiere','Crossbody bag'),('24/24','Top-handle bag'),('In-The-Loop','Shoulder bag'),('Geta','Shoulder bag')]:
    a(H,k,n,'Hermès','',HER,'Line named on Hermès women\'s bag collection page.')
# Dior
for n,k in [('Dior Promenade','Shoulder bag'),('Dior Toujours','Top-handle bag'),('Lady D-Joy','Top-handle bag'),('Dior Médaillon','Shoulder bag'),('Dior Bow','Top-handle bag'),('Diorly','Shoulder bag'),('Dior Milly-La-Forêt','Top-handle bag'),('Dior Cigale','Hobo bag'),('D-Journey','Top-handle bag'),('30 Montaigne','Flap bag'),('Dior Caro','Shoulder bag')]:
    a(H,k,n,'Dior','',DIOR,'Line named on Dior\'s Bags by Line page.')
# Chanel
a(H,'Flap bag','Classic Flap','Chanel','1983',W+'Chanel','Quilted flap bag; Chanel\'s own page calls it Classic 11.12, and Wikipedia dates 11.12 to 1983.','Classic 11.12 · Timeless Classic',[('Classic 11.12','1983','named as Classic on Chanel\'s handbag page')])
a(H,'Tote bag','Chanel 22','Chanel','',CHA,'Line named on Chanel\'s handbag page.')
a(H,'Tote bag','Chanel 25','Chanel','',CHA,'Line named on Chanel\'s handbag page.')
# Celine
for n,k in [('Celine Flair','Flap bag'),('Celine Le 17','Shoulder bag'),('Celine Nino','Shoulder bag'),('Celine Frame','Shoulder bag'),('Celine Le 16','Shoulder bag'),('Celine Trio','Crossbody bag'),('Celine Drop','Shoulder bag'),('Celine Doctor\'s Pouch','Top-handle bag'),('Celine Lulu','Shoulder bag')]:
    a(H,k,n,'Celine','',CEL,'Line named on Celine\'s women\'s handbag page.')
# Loewe
for n,k in [('Flamenco','Shoulder bag'),('Pebble','Bucket bag'),('Squeeze','Hobo bag'),('Hammock','Hobo bag'),('Amazona','Top-handle bag')]:
    a(H,k,n,'Loewe','',LOE,'Line named on Loewe\'s bags by line page.')
# Fendi
a(H,'Shoulder bag','Croissant','Fendi','',FEN,'Line named on Fendi\'s women\'s bag page.')
# Prada
for n in ['Route','Bonnie','Carry','Explore','Aimée','Arqué','Avoir','Boogie','Box','Buckle','Chérie','Cleo','Coffret','Corsaire','Double','Duet','Evasion','Karin','Midi','Nova','Ouvert','Panier','Passage','Prelude','Signet','Traveller','Wish']:
    a(H,'Shoulder bag','Prada '+n,'Prada','',PRA,'Collection named in the filter of Prada\'s women\'s bag page.')
# LV
for n,k,vv in [('OnTheGo','Tote bag',[('OnTheGo PM','',''),('OnTheGo MM','',''),('OnTheGo Soft MM','','')]),('Graceful','Shoulder bag',[('Graceful PM','',''),('Graceful MM','','')]),('Carryall','Shoulder bag',[('Carryall East West','',''),('Carryall Travel','','')]),('Again','Shoulder bag',[]),('Multipass','Tote bag',[]),('All-In','Bucket bag',[('All-In BB','','')]),('Madeleine','Shoulder bag',[('Nano Madeleine','','')]),('Liv Pochette','Pochette',[]),('Vanity Chain Pouch','Pochette',[]),('Side Trunk','Shoulder bag',[('Side Trunk MM','','')]),('Petit Palais','Tote bag',[]),('All Around','Shoulder bag',[('All Around PM','','')]),('Low Key','Hobo bag',[('Low Key Hobo MM','','')]),('Félicie Pochette','Pochette',[])]:
    a(H,k,n,'Louis Vuitton','',LV,'Line shown on Louis Vuitton\'s women\'s handbag page.',v=vv)
a(H,'Top-handle bag','Capucines','Louis Vuitton','',W+'Louis_Vuitton','Louis Vuitton line named on Wikipedia, with an Artycapucines edition in 2019.')
a('Luggage & travel','Weekender','Steamer Bag','Louis Vuitton','1901',W+'Louis_Vuitton','Soft travel bag introduced by Louis Vuitton in 1901.')
# Bottega, Longchamp, others
a(H,'Shoulder bag','Kalimero','Bottega Veneta','2022',W+'Bottega_Veneta','Line named on Wikipedia\'s Bottega Veneta page, 2022.')
a(H,'Tote bag','Longchamp LM','Longchamp','1978',W+'Longchamp_(company)','First women\'s handbag collection from Longchamp, 1978.','LM line')
a(H,'Tote bag','Xtra-Bag','Longchamp','',W+'Longchamp_(company)','Predecessor of Le Pliage, named on Wikipedia.')
a(H,'Hobo bag','Eva','Tanner Krolle','2006',W+'Handbag','Hobo bag shown on Wikipedia\'s Handbag page, 2006.')
a(H,'Bucket bag','Courtauld bag','','early 1300s (tentative)',W+'Handbag','Medieval purse named on Wikipedia\'s Handbag page as an early handbag.')
a(H,'Messenger bag','Freitag messenger bag','Freitag','',W+'Handbag','Swiss messenger bag made from truck tarpaulin; shown on Wikipedia\'s Handbag page.')
# Eyewear
E='Eyewear'
RB=W+'Ray-Ban'
a(E,'Aviator frames','Ray-Ban Olympian','Ray-Ban','1965',RB,'Aviator-style Ray-Ban line named on Wikipedia, with Olympian I and II.')
a(E,'Aviator frames','Ray-Ban Outdoorsman','Ray-Ban','',RB,'Ray-Ban line seen in a 1968 advertisement, as Wikipedia states.')
a(E,'Round & panto frames','Ray-Ban Erika','Ray-Ban','',RB,'Ray-Ban line named on Wikipedia.')
a(E,'Round & panto frames','Moscot Nebb','Moscot','2008',W+'Moscot','Limited edition made with Chris Benz in 2008.')
a(E,'Square & rectangular frames','Moscot Grunya','Moscot','2014',W+'Moscot','Collaboration frame with Tariq "Black Thought" Trotter, 2014.')
a(E,'Square & rectangular frames','Moscot Mulholland Drive','Moscot','',W+'Moscot','Frame associated with Justin Theroux on Wikipedia.')
a(E,'Shield & wrap sunglasses','O-Frame','Oakley','1980',W+'Oakley,_Inc.','Oakley\'s first product, motocross goggles from 1980.')
# Backpacks
B='Backpacks & belt bags'
OS='https://www.osprey.com/gb/backpacks-bags/outdoor-backpacks/backpacking-backpacks'
OSZ='https://www.osprey.com/fitting-learning/size-fit'
for n,v in [('Atmos AG',[('Atmos AG LT','','listed on Osprey\'s sizing page')]),('Aether',[('Aether Plus','',''),('Aether Pro','','')]),('Exos',[('Exos/Eja Pro','','')]),('Talon',[('Talon Pro','',''),('Talon Velocity','',''),('Talon 11, 22, 26, 33, 44','2025','new 2025 sizes on the sizing page')]),('Kestrel',[('Kestrel LT','','')]),('Kyte',[('Kyte LT','','')]),('Ariel',[('Ariel Plus','','')]),('Aura AG',[('Aura AG LT','','')]),('Eja',[]),('Stratos',[]),('Sirrus',[]),('Fairview',[('Fairview Trek','','')]),('Renn',[]),('Rook',[]),('Ace',[])]:
    a(B,'Hiking backpack','Osprey '+n,'Osprey','',OS if n not in ('Talon',) else OSZ,'Osprey pack line listed on its backpacking range page.',v=v)
GR='https://eu.gregorypacks.com/uk-en/backpacks-bags/backpacking-packs/'
for n,v in [('Baltoro',[('Baltoro 65','',''),('Baltoro 75','',''),('Baltoro Pro 85','',''),('Baltoro Pro 100','','')]),('Deva',[('Deva 60','',''),('Deva 70','',''),('Deva Pro 80','','')]),('Paragon',[('Paragon 60','','')]),('Maven',[('Maven 58','','')]),('Zulu',[('Zulu 40','','')]),('Jade',[('Jade 38','','')])]:
    a(B,'Hiking backpack','Gregory '+n,'Gregory','',GR,'Gregory pack line listed on its backpacking range page.',v=v)
for n in ['Stout','Amber','Focal','Facet','Citro','Juno']:
    a(B,'Hiking backpack','Gregory '+n,'Gregory','',GR,'Collection name shown on Gregory\'s backpacking range page.')
DE='https://www.deuter.com/us-en/backpacks/backpacking-packs/'
a(B,'Hiking backpack','Deuter Aircontact','Deuter','',DE,'Deuter trekking pack family with Aircontact Core, Lite, Pro, Ultra and X.',v=[('Aircontact Core','','45+10 SL to 70+10'),('Aircontact Lite','','35+10 SL to 50+10'),('Aircontact Pro','','65+10 SL and 75+10'),('Aircontact Ultra','','35+5 SL to 50+5'),('Aircontact X','','70+15 SL and 80+15')])
a(B,'Hiking backpack','Deuter Futura Air Trek','Deuter','',DE,'Deuter trekking pack listed in 45+10 SL, 50+10 and 55+10 SL sizes.')
KA='https://www.fjallraven.com/us/en-us/bags-gear/kanken/kanken-bags/'
a(B,'Daypack','Kånken No. 2','Fjällräven','',KA,'Larger Kånken listed on Fjällräven\'s Kånken range page, with a Laptop 15 version.')
a(B,'Daypack','Kånken Outlong','Fjällräven','',KA,'Kånken daypack listed on Fjällräven\'s range page.')
EAP='https://eu.eastpak.com/en-be/collections/backpacks'
for n in ["Padded Pak'r",'Out of Office',"Day Pak'r",'Day Office','Morius','Pinnacle']:
    a(B,'Daypack','Eastpak '+n,'Eastpak','',EAP,'Eastpak backpack listed on its backpack collection page.')
a(B,'Carry-on travel backpack','Eastpak Cabin Pak\'r','Eastpak','',EAP,'Eastpak backpack listed on its backpack collection page.')
a(B,'Carry-on travel backpack','Eastpak Travelpack','Eastpak','',EAP,'Eastpak backpack listed on its backpack collection page.')
JS='https://www.jansport.com/en-us/collections/perfect-backpack-finder'
for n,d in [('Right Pack',''),('Main Campus','Largest size JanSport offers, per its FAQ.'),('SuperBreak Plus',''),('Eco Mesh Pack',''),('Big Student','Third-largest JanSport size, after Main Campus and Cool Student.'),('Cool Student','Second-largest JanSport size, per its FAQ.'),('Half Pint','Smallest style JanSport offers, per its FAQ.')]:
    a(B,'School backpack','JanSport '+n,'JanSport','',JS,d or 'Backpack listed on JanSport\'s backpack finder page.')
a(B,'Daypack','Herschel Little America','Herschel Supply Co.','','https://herschel.com/products/herschel-little-america-backpack','Mountaineering-style 30 L backpack.',v=[('Little America Mid-Volume','','21 L')])
a(B,'Laptop backpack','Tumi PowerPack','Tumi','2006',W+'Tumi_Inc.','Backpack with solar charging, designed with Anish Kapoor in 2006.')
# Luggage
L='Luggage & travel'
RW=W+'Rimowa'
a(L,'Suitcase','Rimowa Classic','Rimowa','',RW,'Aluminium case with leather handles.')
a(L,'Suitcase','Rimowa Hybrid','Rimowa','',RW,'Polycarbonate shell with aluminium parts.')
a(L,'Suitcase','Rimowa Distinct','Rimowa','',RW,'Leather collection.')
a(L,'Suitcase','Rimowa Salsa','Rimowa','',RW,'Historical Rimowa polycarbonate line; Salsa Deluxe won a Travel + Leisure award in 2010.',v=[('Salsa Deluxe','2010','won a Travel + Leisure Best Luggage award')])
a(L,'Suitcase','Rimowa Topas','Rimowa','',RW,'Historical Rimowa aluminium line named on Wikipedia.')
a(L,'Suitcase','Rimowa Limbo','Rimowa','',RW,'Historical Rimowa line named on Wikipedia.')
a(L,'Suitcase','Samsonite Streamlite','Samsonite','',W+'Samsonite','Samsonite line seen in a 1960 advertisement.')
a(L,'Suitcase','Hartmann','Hartmann','1877',W+'Samsonite','Luggage maker founded in 1877; Samsonite bought it in August 2012 for US$35 million.')
a(L,'Suitcase','American Tourister','American Tourister','',W+'Samsonite','Luggage brand bought by Astrum in 1993, which rejoined Samsonite after Astrum split in 1995.')
# Umbrellas, baby
a('Umbrellas, fans & canes','Folding umbrella','Jean Marius folding umbrella','Jean Marius','1710',W+'Umbrella','First lightweight folding umbrella in Europe, introduced by a Paris merchant.')
a('Baby carriers & changing bags','Soft structured baby carrier','BabyBjörn Baby Carrier','BabyBjörn','1973',W+'BabyBj%C3%B6rn','Swedish carrier line that began with Close to Heart in 1973.',v=[('Close to Heart','1973','first baby carrier from BabyBjörn'),('Baby Carrier Original','1991',''),('Baby Carrier One','2013',''),('Baby Carrier Harmony','2021','')])
a('Baby carriers & changing bags','Soft structured baby carrier','Ergobaby carrier','Ergobaby','',"https://mauinow.com/2013/01/23/ergobaby-carrier-born-on-maui-creator-featured/",'Carrier designed by Karin Frost on Maui; she sold the company to Compass Management Group in 2010.')
# versions to add to existing entries: (dept, entry name) -> list
ADDV={
 ('Handbags','Speedy'):[('Nano Speedy','',''),('Speedy Bandoulière 20','',''),('Speedy Soft 30','','')],
 ('Handbags','Neverfull'):[('Neverfull MM','',''),('Neverfull Inside Out','','')],
 ('Handbags','Alma'):[('Alma BB','',''),('Alma MM Soft','','')],
 ('Handbags','Pochette Métis'):[('Hobo Métis','','')],
 ('Handbags','Celine Triomphe'):[('Soft Triomphe','','named on Celine\'s handbag page'),('Triomphe Canvas','','named on Celine\'s handbag page')],
 ('Handbags','Fendi Baguette'):[('Baguette Soft','','named on Fendi\'s women\'s bag page')],
 ('Handbags','Bamboo 1947'):[('New Bamboo','','named on Wikipedia\'s Gucci page')],
 ('Handbags','Gucci Jackie'):[('New Jackie','','named on Wikipedia\'s Gucci page')],
 ('Handbags','Le Pliage'):[('Green District','2020','recycled-nylon line')],
 ('Eyewear','Ray-Ban Aviator'):[('The General','1987','special edition')],
 ('Backpacks & belt bags','Kånken'):[('Kånken Mini','',''),('Kånken Laptop 15','',''),('Kånken Laptop 17','',''),('Kånken Totepack','',''),('Kånken Crossbody','',''),('Kånken Weekender','','')],
 ('Luggage & travel','Rimowa Essential'):[('Essential Lite','',''),('Essential Sleeve','','')],
}
# owner map: mk -> (own, tier, cty, own_y)
OW={
 'Hermès':('Hermès International','Independent','France',''),
 'Chanel':('Chanel Limited','Independent','France',''),
 'Louis Vuitton':('LVMH','Global group','France','1987'),
 'Dior':('LVMH','Global group','France','2017'),
 'Celine':('LVMH','Global group','France',''),
 'Fendi':('LVMH','Global group','Italy',''),
 'Loewe':('LVMH','Global group','Spain','1996'),
 'Rimowa':('LVMH','Global group','Germany','2016'),
 'Gucci':('Kering','Global group','Italy','1999'),
 'Bottega Veneta':('Kering','Global group','Italy','2001'),
 'Saint Laurent':('Kering','Global group','France','1999'),
 'Balenciaga':('Kering','Global group','','2001'),
 'Prada':('Prada Group','Global group','Italy',''),
 'Longchamp':('Longchamp','Independent','France',''),
 'Coach':('Tapestry','Global group','United States',''),
 'Samsonite':('Samsonite International S.A.','Global group','United States',''),
 'Tumi':('Samsonite International S.A.','Global group','United States','2016'),
 'Hartmann':('Samsonite International S.A.','Global group','United States','2012'),
 'American Tourister':('Samsonite International S.A.','Global group','United States',''),
 'Gregory':('Samsonite International S.A.','Global group','United States','2014'),
 'Ray-Ban':('EssilorLuxottica','Global group','United States','1999'),
 'Oakley':('EssilorLuxottica','Global group','United States','2007'),
 'Persol':('EssilorLuxottica','Global group','Italy','1995'),
 'Oliver Peoples':('EssilorLuxottica','Global group','','2007'),
 'Moscot':('Moscot','Independent','United States',''),
 'Goyard':('Goyard','Independent','France',''),
 'Cartier':('Richemont','Global group','France',''),
 'Moynat':('LVMH','Global group','France',''),
 'Jimmy Choo':('Capri Holdings','Global group','United Kingdom','2017'),
}
