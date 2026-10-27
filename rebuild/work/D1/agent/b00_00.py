import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a='',dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':W+s,'v':[dict(zip(('n','mk','y','d'),t)) for t in v]}
    if dt: x['dt']=dt
    return x
laptop_x=[
 X('Toshiba T1100','Toshiba','1985','Toshiba_T1100','Early IBM-compatible clamshell laptop that Toshiba calls the first mass-market laptop.',
   [('T1100','Toshiba','1985','original, 4.77 MHz 80C88, one 3.5-inch drive'),('T1100 Plus','Toshiba','1986','two 720 KB drives, RAM to 640 KB'),('T1000','Toshiba','','related smaller model')]),
 X('Compaq LTE','Compaq','1989','Compaq_LTE','Compaq\'s first notebook and the first commercially successful IBM-compatible notebook, with a standard floppy drive.',
   [('LTE','Compaq','1989','8086'),('LTE/286','Compaq','1989','80286'),('LTE/386s','Compaq','1990','first docking station'),('LTE Lite','Compaq','1992','better LCDs, power saving'),('LTE Elite','Compaq','1994','PC Card slots, built-in power adapter'),('LTE 5000','Compaq','1995','Pentium redesign; line replaced by Armada in 1997')]),
 X('DynaBook','Toshiba','1989','Dynabook_Inc.','Toshiba\'s Japanese notebook line, begun with the compact, low-priced J-3100 SS; the PC business is now Dynabook Inc.',
   [('DynaBook J-3100','Toshiba','1989','J-3100 SS001, a major hit in Japan'),('Portégé','Dynabook','','premium business ultrabooks'),('Tecra','Dynabook','','business laptops'),('Satellite Pro','Dynabook','','budget and business laptops')]),
 X('PowerBook','Apple','1991','PowerBook','Apple\'s professional notebook line whose palm-rest and pointing-device-in-front layout became the laptop norm.',
   [('PowerBook 100 series','Apple','1991','100 (built by Sony), 140, 170; then 145, 160, 180'),('PowerBook Duo','Apple','1992','thin subnotebook that docks into a desktop station'),('PowerBook 500 series','Apple','1994','68LC040 "Blackbird"'),('PowerBook 5300','Apple','','first PowerPC PowerBook'),('PowerBook 1400 / 2400 / 3400','Apple','1996–1997',''),('PowerBook G3','Apple','1997–2000','Kanga, WallStreet (1998), Lombard (1999), Pismo (2000)'),('PowerBook G4 Titanium','Apple','2001','"TiBook"'),('PowerBook G4 Aluminum','Apple','2003','12-, 15- and 17-inch; replaced by MacBook Pro in 2006')],
   dt='screen 12–17 in · titanium or aluminium shell · codenamed generations'),
 X('IBM ThinkPad 700C','IBM','1992','IBM_ThinkPad_700C','First ThinkPad generation and the first laptop with a TrackPoint pointing stick, in Richard Sapper\'s black box design.',
   [('ThinkPad 700','IBM','1992','monochrome screen'),('ThinkPad 700C','IBM','1992','10.4-inch colour active-matrix screen'),('ThinkPad 700T','IBM','1992–1993','pen tablet')]),
 X('ThinkPad T series','IBM','2000','ThinkPad_T_series','Mainstream business ThinkPad line, a reference for durable keyboards and repairability.',
   [('T20–T23','IBM','2000–2001',''),('T30','IBM','2002',''),('T40–T42','IBM','2003',''),('T43','IBM','2004','last IBM-built'),('T60','Lenovo','2006',''),('T61','Lenovo','2007',''),('T400 / T500','Lenovo','2008',''),('T410','Lenovo','2010',''),('T420','Lenovo','2011',''),('T430','Lenovo','2012',''),('T440','Lenovo','2013',''),('T450','Lenovo','2015',''),('T460','Lenovo','2016',''),('T470','Lenovo','2017',''),('T480','Lenovo','2018',''),('T490','Lenovo','2019',''),('T14 Gen 1–6','Lenovo','2020–2025','Intel and AMD')],
   dt='suffixes: s slim · p performance · u ultrabook'),
 X('ThinkPad X series','IBM','2000','ThinkPad_X_series','Compact 12–13-inch ThinkPad line for travel.',
   [('X20 / X21','IBM','2000–2001',''),('X30','IBM','2002',''),('X40','IBM','2004','first thin-and-light'),('X60','Lenovo','2005','first Lenovo-branded X'),('X200','Lenovo','2008',''),('X201','Lenovo','2010',''),('X220','Lenovo','2011',''),('X230','Lenovo','2012',''),('X240','Lenovo','2013',''),('X270','Lenovo','2017',''),('X280','Lenovo','2018',''),('X13 Gen 1–6','Lenovo','2020–2025','')]),
 X('ThinkPad X1 Carbon','Lenovo','2012','ThinkPad_X1_Carbon','Lenovo\'s flagship ultralight 14-inch business ThinkPad.',
   [('Gen 1','Lenovo','2012',''),('Gen 2','Lenovo','2014',''),('Gen 3','Lenovo','2015',''),('Gen 4','Lenovo','2016',''),('Gen 5','Lenovo','2017',''),('Gen 6','Lenovo','2018',''),('Gen 7','Lenovo','2019',''),('Gen 8','Lenovo','2020',''),('Gen 9','Lenovo','2021',''),('Gen 10','Lenovo','2022',''),('Gen 11','Lenovo','2022',''),('Gen 12','Lenovo','2024',''),('Gen 13','Lenovo','2024',''),('Gen 14','Lenovo','2026','')]),
 X('Panasonic Toughbook','Panasonic','1996','Panasonic_Toughbook','Rugged laptop line built to survive drops, water and dust.',
   [('CF-25','Panasonic','1996','first fully rugged Toughbook'),('CF-29','Panasonic','2003',''),('CF-19','Panasonic','c. 2006','rugged convertible'),('CF-30','Panasonic','',''),('CF-31','Panasonic','2010','MIL-STD-810G, IP65'),('CF-20','Panasonic','','detachable, CF-19 successor'),('Toughbook 55','Panasonic','2019',''),('Toughbook 40','Panasonic','2022','MIL-STD-810H, IP66')],
   dt='fully rugged · semi-rugged · convertible'),
 X('Toshiba Libretto','Toshiba','1996','Toshiba_Libretto','Palm-sized mini notebook, at launch the smallest commercially sold Windows PC.',
   [('Libretto 20','Toshiba','1996','Japan only, 840 g'),('Libretto 30','Toshiba','1996',''),('Libretto 50','Toshiba','1997','first Pentium'),('Libretto 70 / 100 / 110','Toshiba','1997–1998',''),('Libretto ff 1100','Toshiba','1998–1999','Japan'),('Libretto L series','Toshiba','2001–2002','Transmeta Crusoe'),('Libretto U100','Toshiba','2005',''),('Libretto W100','Toshiba','2010','dual-screen')]),
 X('iBook','Apple','1999','IBook','Apple\'s consumer notebook of 1999–2006, famous for the colourful clamshell.',
   [('iBook G3 Clamshell','Apple','1999',''),('iBook G3 Dual USB','Apple','2001','"Snow"'),('iBook G4','Apple','2003','12- and 14-inch; replaced by MacBook in 2006')]),
 X('MacBook Pro','Apple','2006','MacBook_Pro','Apple\'s professional laptop, successor to the PowerBook.',
   [('Intel aluminium','Apple','2006',''),('Unibody','Apple','2008','machined from one aluminium block'),('Retina','Apple','2012','dropped the optical drive'),('Touch Bar','Apple','2016',''),('Apple silicon 14/16-inch','Apple','2021','M1 Pro/Max, then M2–M5 chips')],
   dt='13 · 14 · 15 · 16 · 17 in · space grey, silver, space black'),
 X('MacBook Air','Apple','2008','MacBook_Air','Apple\'s thin and light laptop that set the template for the ultrabook.',
   [('Original 13.3-inch','Apple','2008',''),('Tapered unibody 11/13-inch','Apple','2010',''),('Retina','Apple','2018',''),('M1','Apple','2020','first Apple silicon Air'),('M2 redesign','Apple','2022','flat 13.6-inch design'),('15-inch','Apple','2023',''),('M3','Apple','2024',''),('M4','Apple','2025',''),('M5','Apple','2026','')],
   dt='11 · 13 · 15 in · colours'),
 X('Dell XPS','Dell','2005','Dell_XPS','Dell\'s premium consumer line, split from Inspiron for laptops in 2005; the brand was paused in 2025.',
   [('XPS 13 L321X','Dell','',''),('XPS 13 9343','Dell','',''),('XPS 13 9380','Dell','',''),('XPS 13 Plus 9320','Dell','',''),('XPS 14 9440','Dell','',''),('XPS 15 9500','Dell','',''),('XPS 17','Dell','','')],
   dt='13 · 14 · 15 · 16 · 17 in · clamshell or 2-in-1'),
 X('HP EliteBook','HP','2008','HP_EliteBook','HP\'s premium business laptop line, replacing the HP Compaq business notebooks.',
   [('xx30 series','HP','2008','2530p, 6930p, 8530p'),('xx40 series','HP','2010',''),('xx60 series','HP','2011',''),('xx70 series','HP','2012','2170p, 8470p'),('G-numbered 800 series','HP','2013','820/840/850 G1, Folio 1040 G1'),('Elite Dragonfly','HP','2019','ultralight convertible')]),
 X('Razer Blade','Razer','2012','Razer_Blade','Thin aluminium gaming laptop that started the premium slim-gaming class.',
   [('Razer Blade','Razer','2012','first model; refreshed 2014'),('Razer Blade Stealth','Razer','2016','ultrabook'),('Razer Blade 14','Razer','',''),('Razer Blade 15','Razer','',''),('Razer Blade 16','Razer','',''),('Razer Blade 18','Razer','','')]),
 X('HP Spectre','HP','2012','HP_Spectre','HP\'s premium consumer ultrabook and convertible line, begun as a high-end Envy.',
   [('Envy 14 Spectre','HP','2012','first Spectre'),('Spectre XT','HP','2012','13-inch ultrabook'),('Spectre x360','HP','2015','360° convertible'),('Spectre 13','HP','2016',''),('Spectre Folio','HP','2018','leather-clad'),('Spectre Fold','HP','2023','foldable 3-in-1')]),
 X('ASUS ROG Zephyrus','ASUS','2017','Asus_ROG','Thin gaming laptop line of ASUS\'s Republic of Gamers brand.',
   [('Zephyrus GX501','ASUS','2017','Max-Q graphics'),('Zephyrus G14','ASUS','2020','compact, AMD Ryzen 4000'),('Zephyrus G15','ASUS','',''),('Zephyrus M16','ASUS','',''),('Zephyrus Duo','ASUS','','second screen above keyboard'),('Zephyrus G16','ASUS','','')]),
 X('Microsoft Surface Laptop','Microsoft','2010s','Surface_Laptop','Microsoft\'s own clamshell Windows laptop.',
   [('Surface Laptop','Microsoft','',''),('Surface Laptop 2','Microsoft','2018',''),('Surface Laptop 3','Microsoft','2019',''),('Surface Laptop 4','Microsoft','2021',''),('Surface Laptop 5','Microsoft','2022',''),('Surface Laptop 6','Microsoft','2024',''),('Surface Laptop 7','Microsoft','2024',''),('Surface Laptop Go','Microsoft','2020','smaller, cheaper'),('Surface Laptop Studio','Microsoft','2021','pull-forward screen'),('Surface Laptop SE','Microsoft','2021','for schools')]),
 X('Framework Laptop','Framework Computer','2021','Framework_Computer','Modular, user-repairable laptop with swappable ports and upgradable mainboards.',
   [('Framework Laptop 13','Framework Computer','2021',''),('Chromebook Edition','Framework Computer','2022',''),('Framework Laptop 16','Framework Computer','2024','modular input and graphics bays'),('Framework Laptop 12','Framework Computer','2025','')]),
]
m_laptop=[["Aspire 5","Acer"],["Swift Go","Acer"],["Predator Helios 16","Acer"],["IdeaPad Slim 5","Lenovo"],["Yoga Slim 7","Lenovo"],["Legion Pro 7i","Lenovo"],["Latitude 5450","Dell"],["Inspiron 1400","Dell"],["X16","Alienware"],["Pavilion Plus 14","HP"],["Envy x360","HP"],["Omen 16","HP"],["ZenBook S UX393","ASUS"],["Vivobook S16","ASUS"],["ROG Strix Scar 16","ASUS"],["Galaxy Book4 Pro","Samsung Electronics"],["LG Gram Pro","LG"],["Katana 15","MSI"],["Lemur Pro","System76"],["InfinityBook Pro","Tuxedo Computers"]]
# verify all m in old data
old=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/D1/agent/00_00.old.json'))
allm={tuple(m) for k in old for m in k.get('m',[])}
m_laptop=[m for m in m_laptop if tuple(m) in allm]
det_x=[
 X('Microsoft Surface Pro','Microsoft','2013','Microsoft_Surface_Pro','Kickstand Windows tablet with a clip-on keyboard cover, the reference detachable.',
   [('Surface Pro','Microsoft','2013',''),('Surface Pro 2','Microsoft','2013',''),('Surface Pro 3','Microsoft','2014','3:2 screen'),('Surface Pro 4','Microsoft','2015',''),('Surface Pro (5th gen)','Microsoft','2017',''),('Surface Pro 6','Microsoft','2018',''),('Surface Pro 7','Microsoft','2019',''),('Surface Pro X','Microsoft','2019','ARM'),('Surface Pro 8','Microsoft','2021',''),('Surface Pro 9','Microsoft','2022','ARM or x86'),('Surface Pro 10','Microsoft','2024',''),('Surface Pro 11th Edition','Microsoft','2024',''),('Surface Pro 12-inch','Microsoft','2025','')],
   dt='Type Cover keyboard · pen · Intel or ARM'),
 X('Microsoft Surface Book','Microsoft','2015','Surface_Book','Laptop whose screen ("clipboard") unlocks from a keyboard base that holds a second battery and optional GPU.',
   [('Surface Book','Microsoft','2015','muscle-wire lock, dynamic fulcrum hinge'),('Surface Book 2','Microsoft','2017','13.5 and 15 in'),('Surface Book 3','Microsoft','2020','')]),
]
m_det=[["Compaq Concerto","Compaq"],["Galaxy Book 12","Samsung Electronics"],["Vaio Z Canvas","Vaio"],["ThinkPad X12 Detachable","Lenovo"],["ROG Flow Z13","ASUS"],["Spectre x2","HP"],["IdeaPad Miix 520","Lenovo"],["Galaxy Book 10.6","Samsung Electronics"]]
m_det=[m for m in m_det if tuple(m) in allm]
cb_x=[
 X('Google Cr-48','Google','2010','Chromebook','Prototype Chrome OS notebook built by Inventec and handed to about 60,000 testers.',[('Cr-48','Google','2010','plain black, unbranded')]),
 X('Google Pixelbook','Google','2017','Pixelbook','Google\'s own premium Chromebooks, from the Chromebook Pixel to the Pixelbook Go.',
   [('Chromebook Pixel','Google','','discontinued 2016'),('Pixelbook','Google','2017','convertible'),('Pixelbook Go','Google','2019','clamshell; line ended 2022')]),
]
kinds=[
 {'n':'Laptop','a':'notebook · notebook computer','d':'Portable computer with its screen and keyboard in one folding body.',
  't':['ultrabook / thin and light','gaming','mobile workstation','business','rugged','convertible (360° hinge)','budget / education'],
  's':'https://www.notebookcheck.net/Reviews-by-product-rating.160898.0.html','x':laptop_x,'m':m_laptop},
 {'n':'Detachable 2-in-1','a':'detachable 2-in-1 computer','d':'Portable computer whose screen detaches from the keyboard that comes with it. A tablet sold with an optional keyboard is in Phones, Tablets & Personal Devices.',
  's':'https://en.wikipedia.org/wiki/2-in-1_laptop','x':det_x,'m':m_det},
 {'n':'Chromebook','a':'','d':'Laptop that runs ChromeOS.','t':['clamshell','convertible','detachable','Chromebook Plus'],
  's':'https://shop.ascend.de/en/collections/chromebooks-en','x':cb_x,'m':[]},
]
K='knowledge'
brands=[
 dict(n='Apple',c='United States',f='1976',seg='Premium',kf='Mac computers',d='Californian maker of Mac computers, iPhone and iPad.',lines=['PowerBook','iBook','MacBook Air','MacBook Pro'],sig=['PowerBook','MacBook Air','MacBook Pro'],s=K),
 dict(n='IBM',c='United States',f='1911',seg='Professional & flagship',kf='business computing',d='American computing company that created the IBM PC and ThinkPad and sold its PC business to Lenovo in 2005.',lines=['ThinkPad'],sig=['IBM ThinkPad 700C','ThinkPad T series','ThinkPad X series'],rel=['Lenovo'],s=K),
 dict(n='Lenovo',c='China',f='1984',seg='Mainstream',kf='ThinkPad',d='Chinese PC maker, largest by volume, owner of ThinkPad since 2005.',lines=['ThinkPad','IdeaPad','Yoga','Legion'],sig=['ThinkPad X1 Carbon'],rel=['IBM'],s=K),
 dict(n='Toshiba',c='Japan',f='1875',seg='Heritage manufactory',kf='early laptops',d='Japanese electronics group that pioneered mass-market laptops; its PC business became Dynabook Inc.',lines=['T series','DynaBook','Libretto','Satellite','Portégé'],sig=['Toshiba T1100','DynaBook','Toshiba Libretto'],rel=['Dynabook'],s=K),
 dict(n='Dynabook',c='Japan',f='2019',seg='Mainstream',kf='business laptops',d='Sharp-owned successor to Toshiba\'s PC business, renamed Dynabook in 2019.',lines=['Portégé','Tecra','Satellite Pro','dynabook'],rel=['Toshiba'],s=W+'Dynabook_Inc.'),
 dict(n='Compaq',c='United States',f='1982',seg='Mainstream',kf='IBM-compatible PCs',d='American PC maker known for early IBM-compatible portables; bought by HP in 2002.',lines=['LTE','Armada','Presario'],sig=['Compaq LTE'],rel=['HP'],s=K),
 dict(n='Dell',c='United States',f='1984',seg='Mainstream',kf='direct-sold PCs',d='Texan PC maker selling consumer and business laptops and desktops.',lines=['XPS','Latitude','Inspiron','Precision'],sig=['Dell XPS'],rel=['Alienware'],s=K),
 dict(n='HP',c='United States',f='1939',seg='Mainstream',kf='PCs and printers',d='American maker of PCs and printers.',lines=['EliteBook','Spectre','Envy','Pavilion','Omen','ProBook'],sig=['HP EliteBook','HP Spectre'],rel=['Compaq'],s=K),
 dict(n='Microsoft',c='United States',f='1975',seg='Premium',kf='Windows and Surface',d='American software company that makes the Surface line of computers.',lines=['Surface Pro','Surface Laptop','Surface Book'],sig=['Microsoft Surface Pro','Microsoft Surface Laptop'],s=K),
 dict(n='Razer',c='Singapore',f='2005',seg='Premium',kf='gaming hardware',d='Gaming hardware brand making laptops and peripherals.',lines=['Blade'],sig=['Razer Blade'],s=K),
 dict(n='ASUS',c='Taiwan',f='1989',seg='Mainstream',kf='laptops and motherboards',d='Taiwanese maker of laptops, motherboards and graphics cards.',lines=['ROG','Zenbook','Vivobook','TUF','ExpertBook'],sig=['ASUS ROG Zephyrus'],s=K),
 dict(n='Framework Computer',c='United States',f='2020',seg='Specialist',kf='repairable laptops',d='San Francisco maker of modular, repairable laptops, founded by Nirav Patel.',lines=['Framework Laptop 13','Framework Laptop 16','Framework Laptop 12'],sig=['Framework Laptop'],s=W+'Framework_Computer'),
 dict(n='Panasonic',c='Japan',f='1918',seg='Professional & flagship',kf='rugged computers',d='Japanese electronics group whose Toughbook line leads rugged laptops.',lines=['Toughbook',"Let's Note"],sig=['Panasonic Toughbook'],s=K),
 dict(n='Google',c='United States',f='1998',seg='Premium',kf='ChromeOS',d='American technology company behind ChromeOS and the Pixelbook.',lines=['Chromebook Pixel','Pixelbook'],sig=['Google Pixelbook'],s=K),
]
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':'Cut the 3,681-model Laptop list to 20 archetype lines (historic icons, then lines by start year) whose versions are generations from the retrieved Wikipedia pages or names from the old data, plus 20 market-covering current models in m (Acer, Lenovo, Dell, Alienware, HP, ASUS, Samsung, LG, MSI, System76, Tuxedo). Dropped the long tail of vintage and regional SKUs (AST, Bondwell, NEC, Medion, Epson, Olivetti, GRiD, etc.) as SKU noise; GRiD Compass belongs with vintage portables if wanted. Detachables moved from the Laptop list (ROG Flow Z13, ThinkPad X12, Spectre x2, Miix) into Detachable 2-in-1. Dell XPS versions carry no years: the XPS page did not give per-model years. Surface Laptop first-generation year left blank (page unclear). Gaming, business, rugged, convertible kept as types.'}
p='/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/00_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(len(m_laptop),len(m_det))
