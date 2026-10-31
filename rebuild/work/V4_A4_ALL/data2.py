from data import *
import data
H='Handbags'
GEN='Shoulder bag'
def b(kind,n,mk,y,s,d='',al='',v=None,dept=H):
    a(dept,kind,n,mk,y,s,d,al,v)
GU='https://www.gucci.com/us/en/ca/women/handbags-c-women-handbags'
for n in ['Borsetto','Brera','GG Emblem','GG Marmont','Gossip','Gucci Aperitivo','Gucci Beatrix','Gucci Giglio','Gucci Infinity','Gucci Londra','Gucci Melrose','Gucci Siena','Gucci Tag','Gucci Tribeca','Gucci Venice','Gucci Madison','Gucci Mercato','Ophidia','Paparazzo','Starlet','Web Trademark']:
    nm=n if n.startswith('Gucci') else 'Gucci '+n
    b(GEN,nm,'Gucci','',GU,'Line listed in the Lines filter of Gucci\'s women\'s handbag page.')
b(GEN,'Gucci Lady Lunetta','Gucci','',GU,'Line listed in the Lines filter of Gucci\'s women\'s handbag page.',v=[('Lunetta','',''),('Lady Lunetta Chain','','')])
YS='https://www.ysl.com/en-sk/shop-women/handbags/all-handbags'
for n in ['Mombasa','Amalia','Icare','Jamie','Le 5 à 7','Shopping Saint Laurent','Niki','Gaby','Solferino','Envelope','Kate','Puffer','Le 37','Sac de Jour','Simone','Sunset']:
    b(GEN,'Saint Laurent '+n,'Saint Laurent','',YS,'Line listed on Saint Laurent\'s all handbags page.')
BV='https://www.bottegaveneta.com/en-us/women-collection-us/women-bags'
for n in ['Madison','Campana','Barbara','Giorno','Corso','Veneta','Pinacoteca']:
    b(GEN,'Bottega Veneta '+n,'Bottega Veneta','',BV,'Line listed on Bottega Veneta\'s women\'s bags page.')
BA='https://www.balenciaga.com/en-us/women/bags-for-women'
for n in ['Rodeo','Hourglass Avenue','Le 7','Le Cagole','Fan']:
    b(GEN,'Balenciaga '+n,'Balenciaga','',BA,'Line listed on Balenciaga\'s women\'s bags page.')
VA='https://www.valentino.com/en-us/women/bags'
for n in ['Alltime','Antibes','Berthe','Carry Secrets','DeVain','Djuna','Flutterby','Laseine','Locò','Nellcote','Panthea','Vain','VLogo Signature','Vsling']:
    b(GEN,'Valentino '+n,'Valentino','',VA,'Line listed on Valentino\'s women\'s bags page.')
GV='https://www.givenchy.com/us/en-US/women/bags/'
for n in ['Voyou','Pinch','The Snatch','Facet','Pout','Snap','Show','Day','Lucky Charms']:
    b(GEN,'Givenchy '+n,'Givenchy','',GV,'Line listed on Givenchy\'s women\'s bags page.')
MM='https://www.miumiu.com/ww/en/bag-lines/arcadie/c/10384EU'
for n in ['Arcadie','Wander','Spirit','Ivy','Beau','Vivant','Rendez-vous','Aventure']:
    b(GEN,'Miu Miu '+n,'Miu Miu','',MM,'Line listed under bag lines on Miu Miu\'s site.')
JQ='https://www.jacquemus.com/en_fr/bambinos-bags'
for n in ['Valérie','Rond Carré','Turismo','Bisou','Salon','Chiquito','Berlingot']:
    b(GEN,'Jacquemus '+n,'Jacquemus','',JQ,'Line listed in the bag menu of Jacquemus\'s site.')
PO='https://eng.polene-paris.com/collections/numero-un'
for n in ['Boky','Cyme','Numéro Neuf','Mokki','Numéro Dix','Numéro Un','Shuldo','Tonca','Béri','Nodde','Neyu','Osmo','Tsubi','Solé']:
    b(GEN,'Polène '+n,'Polène','',PO,'Collection listed under Bags by collection on Polène\'s site.')
GY='https://www.goyard.com/us_en/bags.html'
b('Tote bag','Saïgon','Goyard','',GY,'Listed on Goyard\'s bags page as the Saïgon tote bag.')
b('Hobo bag','Hobo Bohème','Goyard','',GY,'Listed on Goyard\'s bags page as the Hobo Bohème bag.')
b('Messenger bag','Coursier','Goyard','',GY,'Listed on Goyard\'s bags page as the Coursier messenger bag.')
b('Pochette','Hirondelle','Goyard','',GY,'Listed on Goyard\'s bags page as the Hirondelle pouch bag.')
for n in ['Musette','Bonbonnière','Bezons']:
    b(GEN,'Goyard '+n,'Goyard','',GY,'Listed on Goyard\'s bags page.')
MU='https://www.mulberry.com/us/shop/women/bags'
b('Satchel','Amberley','Mulberry','',MU,'Listed on Mulberry\'s women\'s bags page as the Amberley satchel and top handle.')
b('Top-handle bag','Stevie','Mulberry','',MU,'Listed on Mulberry\'s women\'s bags page as the Stevie top handle.')
b('Crossbody bag','Darley','Mulberry','',MU,'Listed on Mulberry\'s women\'s bags page as the Darley camera bag.')
b('Messenger bag','Piccadilly','Mulberry','',MU,'Listed on Mulberry\'s women\'s bags page as the Piccadilly messenger and holdall.')
b(GEN,'Mulberry Roxanne','Mulberry','',MU,'Listed on Mulberry\'s women\'s bags page as the Roxanne shoulder bag.')
b(GEN,'Mulberry Lily','Mulberry','',MU,'Listed on Mulberry\'s women\'s bags page.',v=[('Medium Lily','','')])
b(GEN,'Mulberry Antony','Mulberry','',MU,'Listed on Mulberry\'s women\'s bags page and its men\'s classics.')
b('Bucket bag','Mulberry Drawstring Bucket','Mulberry','',MU,'Listed on Mulberry\'s women\'s bags page as the Mini Drawstring Bucket.')
CO='https://www.coach.com/shop/women/handbags/view-all'
b('Shoulder bag','Brooklyn','Coach','',CO,'Listed on Coach\'s women\'s handbag page as the Brooklyn shoulder bag.',v=[('Pillow Brooklyn','','')])
b('Shoulder bag','Coach Juliet','Coach','',CO,'Listed on Coach\'s women\'s handbag page as the Juliet shoulder bag.')
b('Shoulder bag','Coach Lana','Coach','',CO,'Listed on Coach\'s women\'s handbag page as the Lana shoulder bag.')
LC='https://www.longchamp.com/us/en/le-pliage/005/le-pliage-by-collection/005col/'
for n in ['Le Smart','Le Cadence','Le Foulonné','Complice','Le Roseau','Looong','Re-Play','Épure','Daylong','Longchamp 3D','Boxford','Longchamp sur Seine']:
    nm=n if n.startswith('Longchamp') else 'Longchamp '+n
    b(GEN,nm,'Longchamp','',LC,'Collection listed on Longchamp\'s bags by collection page.')
MK='https://www.michaelkors.com/women/handbags/'
b('Satchel','Hamilton','Michael Kors','',MK,'Listed on Michael Kors\'s women\'s handbag page as a satchel and crossbody bag.')
b('Tote bag','Jet Set Travel','Michael Kors','',MK,'Listed on Michael Kors\'s women\'s handbag page as a tote bag.')
b(GEN,'Nolita','Michael Kors','',MK,'Named as a shoulder bag on Michael Kors\'s site.')
MJ='https://www.marcjacobs.com/us-en/the-marc-jacobs/marcdown/bags/'
b(GEN,'The Snapshot','Marc Jacobs','',MJ,'Camera bag listed as the Snapshot Convertible Shoulder Bag.')
b('Tote bag','The Tote Bag','Marc Jacobs','',MJ,'Listed on Marc Jacobs\'s site in medium and large sizes.')
LVm='https://us.louisvuitton.com/eng-us/men/bags/all-bags/_/N-t1uezqf4'
b(GEN,'Nil','Louis Vuitton','',LVm,'Listed on Louis Vuitton\'s men\'s bags page.')
b(GEN,'Vagabond','Louis Vuitton','',LVm,'Listed on Louis Vuitton\'s men\'s bags page.')
b('Hobo bag','Verso','Louis Vuitton','',LVm,'Listed on Louis Vuitton\'s men\'s bags page as Verso Hobo.')
b('Laptop backpack','Christopher','Louis Vuitton','',LVm,'Backpack with laptop padding, listed on Louis Vuitton\'s men\'s bags page.',dept='Backpacks & belt bags')
b('Daypack','Discovery','Louis Vuitton','','https://us.louisvuitton.com/eng-us/men/bags/backpacks/_/N-t19j8ybj','Backpack range listed on Louis Vuitton\'s men\'s backpack page.',dept='Backpacks & belt bags')
# eyewear
E='Eyewear'
OK='https://www.oakley.com/en-us/category/sunglasses'
for n in ['Holbrook','Flak','EVZero','Jawbreaker','Actuator','BXTR','Bisphaera','Capacitor','Caveat','Corridor','Crosshair','De Soto','Drop In','Drop Point','Ellipse','Encoder','Gascan','Gauge','HSTN','Helux','Highland','Hold Out','Inverter','Kaast','Kato','Lateralis','Leadline','Mainlink','Ojector','RSLV','Radar Plate','RadarLock','Reedmace','Resistor','Sielo','Siphon','Split Shot','Sutro','Sylas','Tailend','Terraforma','Thurso','Unstoppable','Valve','Whisker']:
    a(E,'Shield & wrap sunglasses','Oakley '+n,'Oakley','',OK,'Model listed in the style filter of Oakley\'s sunglasses page.')
RBH='https://www.ray-ban.com/usa/ray-ban-glasses-history'
data.ADDV[(E,'Wayfarer')]=[('New Wayfarer','2003',''),('Wayfarer Optics','2017',''),('Mega Wayfarer','2022',''),('Wayfarer Reverse','2023','')]
data.ADDV[(E,'Ray-Ban Aviator')]=data.ADDV.get((E,'Ray-Ban Aviator'),[])+[('Aviator Optics','2016',''),('New Aviator','2022',''),('Aviator Reverse','2023','')]
data.ADDV[(E,'Ray-Ban Round Metal')]=[('Round Metal Optics','2014',''),('Round Double Bridge','2016',''),('New Round','2022',''),('RB3809','2023','')]
data.ADDV[(E,'Clubmaster')]=[('Clubmaster Classic','1986',''),('Clubmaster Optics','2009',''),('Clubmaster Metal','2017',''),('New Clubmaster','2022',''),('Mega Clubmaster','2023','')]
# luggage
L='Luggage & travel'
MN='https://monos.com/blogs/articles/about-monos-designed-for-the-journey'
a(L,'Suitcase','Monos Carry-On','Monos','',MN,'Canadian brand founded in 2018; the line has Carry-On, Pro, Plus and Pro Plus versions.',v=[('Carry-On Pro','',''),('Carry-On Plus','',''),('Carry-On Pro Plus','',''),('Expandable Carry-On','',''),('Expandable Carry-On Pro','','')])
a(L,'Suitcase','Monos Check-In','Monos','',MN,'Check-in line in Medium and Large sizes.',v=[('Check-In Medium','',''),('Check-In Large','',''),('Expandable Check-In Medium','','')])
for n in ['Classic','Hybrid','Aluminum']:
    a(L,'Suitcase','Monos '+n,'Monos','',MN,'Collection listed on the Monos about page.')
a(L,'Weekender','Monos Metro','Monos','',MN,'Bag line listed on the Monos about page.')
GT='https://us.globe-trotter.com/blogs/journal/123-years-and-counting-the-history-of-the-centenary-collection'
for n in ['Safari','Metropolis','Original','Cruise','Leather Crafted','Renewed','Cotswolds','Orient','Caviar']:
    a(L,'Suitcase','Globe-Trotter '+n,'Globe-Trotter','',GT,'Collection listed on Globe-Trotter\'s journal page.')
data.ADDV[(L,'The Carry-On')]=[('The Bigger Carry-On','2016',''),('The Medium','2016',''),('The Large','2016','')]
data.ADDV[(L,'Keepall')]=[('Keepall Bandoulière 45','',''),('Keepall Bandoulière 50','',''),('Keepall Bandoulière 55','','')]
data.ADDV[('Handbags','Gucci Jackie')]=data.ADDV.get(('Handbags','Gucci Jackie'),[])+[('Jackie Slim','','listed on Gucci\'s page')]
data.ADDV[('Handbags','Rockstud')]=[('Rockstud Spike','',''),('Rockstud Maxxing','','')]
data.ADDV[('Handbags','Andiamo')]=[('Andiamo clutch','','')]
data.ADDV[('Handbags','Coach Tabby')]=[('Soft Tabby','','')]
data.ADDV[('Handbags','Mulberry Alexa')]=[('Mini Alexa','','')]
data.ADDV[('Handbags','Bayswater')]=[('Bayswater Satchel','',''),('Mini Bayswater','',''),('East West Bayswater','','')]
data.ADDV[('Handbags','Le Pliage')]=data.ADDV.get(('Handbags','Le Pliage'),[])+[(x,'','') for x in ['Le Pliage Original','Le Pliage One','Le Pliage Collection','Le Pliage du Monde','Le Pliage Energy','Le Pliage Filet','Le Panier Pliage','Le Pliage Travel','My Pliage','Le Pliage Xtra']]
data.ADDV[('Handbags','Telfar Shopping Bag')]=[('Melissa x Telfar Jelly Shopper','',' ')]
# owners
data.OW.update({
 'Balenciaga':('Kering','Global group','','2001'),
 'Givenchy':('LVMH','Global group','France',''),
 'Miu Miu':('Prada Group','Global group','Italy',''),
 'Michael Kors':('Capri Holdings','Global group','United States',''),
 'Osprey':('Helen of Troy Limited','Independent','','2021'),
 'Fjällräven':('Fenix Outdoor International AG','Independent','Sweden','2014'),
 'Eastpak':('VF Corporation','Global group','United States','2000'),
 'JanSport':('VF Corporation','Global group','United States','1986'),
 'Bellroy':('Bellroy','Independent','Australia',''),
 'Ergobaby':('Compass Management Group','Independent','United States','2010'),
 'Gregory':('Samsonite International S.A.','Global group','United States','2014'),
})

for e in data.N:
    if e['n']=='Ray-Ban Outdoorsman': e['y']='1939'; e['s']=RBH; e['d']='Ray-Ban line dated 1939 on the maker\'s history page.'
    if e['n']=='Ray-Ban Olympian': pass
