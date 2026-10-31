import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/V4_C5/bak/C5.pass1.json'))
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
seen=set()
for k in K.values():
    for x in k.get('x',[]):
        seen.add(norm(x['n']))
        for v in x.get('v',[]): seen.add(norm(v['n']))
added={}
def add(kn,n,mk,y,s,dd,v=None,role=None,a=''):
    if norm(n) in seen: return False
    e={'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':s}
    if v: e['v']=[{'n':a_,'mk':mk,'y':b_,'d':c_} for a_,b_,c_ in v]
    if role: e['role']=role
    K[kn].setdefault('x',[]).append(e); seen.add(norm(n)); added.setdefault(kn,[]).append(n); return True
def addv(kn,en,n,y='',dd='',mk=None):
    for x in K[kn]['x']:
        if x['n']==en:
            if norm(n) in seen: return
            x.setdefault('v',[]).append({'n':n,'mk':mk or x.get('mk',''),'y':y,'d':dd}); seen.add(norm(n)); added.setdefault(kn,[]).append(en+' / '+n); return
W='https://en.wikipedia.org/wiki/'
CC='Cartridge-converter fountain pen'; PI='Piston-filling fountain pen'; VA='Vacuum and plunger-filling fountain pen'; SA='Sac-filling fountain pen'; RE='Retractable-nib fountain pen'
NS='filling system not stated on the page read'
# Pelikan
PS='https://thepelikansperch.com/2018/08/26/pelikan-fountain-pen-infographic/'; PG='https://goldspot.com/pages/pelikan-pens'
add(PI,'Pelikan Classic M200 / M205','Pelikan','',PG,'Resin piston-filling Classic line; M200, M205, M215 and M250 are listed on the Pelikan infographic.',v=[('M200','',''),('M205','',''),('M215','',''),('M250','','')])
add(CC,'Pelikan Classic P200 / P205','Pelikan','',PS,'Cartridge-filling Classic line (P for Patronenfüller), with a matching mechanical pencil.',v=[('P200','',''),('P205','','')])
add(PI,'Pelikan Classic M100 / M150','Pelikan','',PS,'Classic-line pens listed as M100 and M150 on the infographic; '+NS+'.',v=[('M100','',''),('M150','','')])
add(PI,'Pelikan M101N','Pelikan','',PS,'Pelikan line shown in four versions on the infographic; '+NS+'.')
add(PI,'Pelikan M120 Iconic Blue','Pelikan','',PS,'Special edition named on the infographic; '+NS+'.')
add(PI,'Pelikan M900 Toledo','Pelikan','',PS,'Pelikan Toledo pen named on the infographic; '+NS+'.')
add(PI,'Pelikan M481','Pelikan','',PS,'Pelikan model named on the infographic; '+NS+'.')
add(PI,'Pelikan M75 Go!','Pelikan','',PS,'Pelikan model named on the infographic; '+NS+'.')
add(PI,'Pelikan P16 Stola III','Pelikan','',PS,'Pelikan model named on the infographic; '+NS+'.')
add(CC,'Pelikan Ineo','Pelikan','',PG,'Minimalist Pelikan collection; '+NS+'.')
add(CC,'Pelikan Pura','Pelikan','',PG,'Aluminium-bodied Pelikan pen with a stainless steel nib; '+NS+'.')
add(CC,'Pelikan Twist','Pelikan','',PG,'Ergonomic coloured pen for younger writers and beginners.')
add(CC,'Pelikano','Pelikan','',PG,'Student pen with an ergonomic grip and stainless steel nib.',v=[('Pelikano Junior','','version for young or new writers')])
for n in ('M300','M320','M350','M605','M620','M625','M630','M640','M650'): addv(PI,'Pelikan Souverän',n,'','named on the Pelikan infographic; piston-filled')
addv(PI,'Pelikan Souverän','M805 Clear Demonstrator','2015','piston-filled')
# Montblanc
MB='https://en.wikipedia.org/wiki/Montblanc_(company)'
wr=[('Ernest Hemingway',1992),('Agatha Christie',1993),('Oscar Wilde',1994),('Voltaire',1995),('Alexandre Dumas',1996),('Fyodor Dostoevsky',1997),('Edgar Allan Poe',1998),('Marcel Proust',1999),('Friedrich Schiller',2000),('Charles Dickens',2001),('F. Scott Fitzgerald',2002),('Jules Verne',2003),('Franz Kafka',2004),('Miguel de Cervantes',2005),('Virginia Woolf',2006),('William Faulkner',2007),('George Bernard Shaw',2008),('Thomas Mann',2009),('Mark Twain',2010),('Carlo Collodi',2011),('Jonathan Swift',2012),('Honoré de Balzac',2013),('Daniel Defoe',2014),('Leo Tolstoy',2015),('William Shakespeare',2016),('Antoine de Saint-Exupéry',2017),('Homer',2018),('Rudyard Kipling',2019),('Victor Hugo',2020),('Sir Arthur Conan Doyle',2021),('Brothers Grimm',2022),('Robert Louis Stevenson',2023),('Jane Austen',2024),('Johann Wolfgang von Goethe',2025),('Bram Stoker',2026)]
add(PI,'Montblanc Writers Edition','Montblanc','1992',MB,'Annual limited edition honouring a writer, from 1992; '+NS+'.',v=[(n,str(y),'') for n,y in wr])
gc=[('Mahatma Gandhi',2009),('Alfred Hitchcock',2011),('Albert Einstein',2012),('Leonardo da Vinci',2013),('John F. Kennedy',2014),('Andy Warhol',2015),('Miles Davis',2016),('The Beatles',2017),('James Dean',2018),('Walt Disney',2019),('Elvis Presley',2020),('Enzo Ferrari',2021)]
add(PI,'Montblanc Great Characters','Montblanc','2009',MB,'Annual limited edition honouring a public figure, from 2009; '+NS+'.',v=[(n,str(y),'') for n,y in gc])
add(PI,'Montblanc Rouge et Noir','Montblanc','1909',MB,'First Montblanc pen model, 1909 (a safety fountain pen); '+NS+'.',role='origin') if False else add(PI,'Montblanc Rouge et Noir','Montblanc','1909',MB,'First Montblanc pen model, 1909; '+NS+'.')
add(PI,'Montblanc Monaco Rainier III','Montblanc','2007',MB,'Limited edition of 81 fountain pens, 2007; '+NS+'.')
# Pilot
PW=W+'Pilot_(pen_company)'
for n,y,dd in [('Custom K','1971','resin version added 1972'),('Custom Grandee Tomo','1978',''),('Custom 67','1985',''),('Custom 823','2000','plunger ink suction')]: addv(CC,'Pilot Custom',n,y,dd)
add(CC,'Pilot Falcon','Pilot','',PW,'Pilot flexible-nib pen named on the Pilot article; '+NS+'.')
add(CC,'Pilot Prera','Pilot','',PW,'Pilot compact pen named on the Pilot article; '+NS+'.')
add(CC,'Pilot Varsity','Pilot','',PW,'Disposable pen pre-loaded with ink.')
# Sailor
SG='https://www.gouletpens.com/blogs/fountain-pen-blog/sailor-brand-overview'
add(CC,'Sailor Compass 1911','Sailor','',SG,'Lighter entry-level 1911 style with steel nibs in translucent colours and a colour-matched converter.')
addv(CC,'Sailor 1911','1911 Maki-e','','decorated versions')
addv(CC,'Sailor 1911','1911 King of Pens','','largest Sailor pen, 21k nib in medium or broad')
addv(CC,'Sailor Pro Gear','Pro Gear King of Pens','','oversized, 21k nib in medium or broad')
# Platinum
PL=W+'Platinum_Pen_Company'
add(CC,'Platinum President','Platinum','1994',PL,'Platinum pen launched 1994; '+NS+'.')
add(CC,'Platinum Izumo','Platinum','2010',PL,'Platinum pen launched 2010; '+NS+'.')
# Visconti
VI=W+'Visconti_(company)'
for n,y in [('Visconti Classic',''),('Visconti Urushi',''),('Visconti Rembrandt','2009'),('Visconti Opera Masters','2009'),('Visconti Divina Royale','2009'),('Visconti Templari','2009')]:
    add(PI,n,'Visconti',y,VI,'Visconti collection named on the Visconti article; '+NS+'.')
# Kaweco, TWSBI
KA=W+'Kaweco'
add(CC,'Kaweco Perkeo','Kaweco','1889',KA,'Brand name listed on early Kaweco products; the article gives no launch year for it as a line.')
addv(CC,'Kaweco Sport','Sport set','1971','licensed writing instrument for the Munich Olympics')
addv(CC,'Kaweco Sport','AL Sport','','aluminium body, named on the Goulet Pens guide','Kaweco')
TW='https://cultpens.com/pages/twsbi-range-guide'
for n,kn,dd in [('TWSBI Diamond 580',PI,'Piston-filled; nib unit removable.'),('TWSBI Diamond Mini',PI,'Smaller piston-filled sibling of the 580.'),('TWSBI Vac Mini',VA,'Vacuum-filled; smaller than the Vac 700.'),('TWSBI GO',PI,'Spring-loaded piston filler.'),('TWSBI Swipe',CC,'Takes standard cartridges or standard converters.'),('TWSBI Precision',PI,'Piston-filled; hexagonal aluminium barrel styled on draughting pencils.'),('TWSBI Classic',PI,'Piston-filled with a traditional look.'),('TWSBI Kai',PI,'Piston-filled with a traditional look.')]:
    add(kn,n,'TWSBI','',TW,dd)
# Lamy
LA='https://endlesspens.com/blogs/endless-journal/the-best-lamy-products'
for n,dd in [('Lamy Studio','Lamy pen line named on the Endless Pens list.'),('Lamy Scala','Lamy pen line named on the Endless Pens list.'),('Lamy Aion','Lamy pen line named on the Endless Pens list.'),('Lamy Accent','Lamy pen line named on the Endless Pens list.'),('Lamy Logo','Lamy pen line named on the Endless Pens list.'),('Lamy Nexx','Cartridge or Z 28 converter.'),('Lamy ABC','Lamy pen line named on the Endless Pens list.')]:
    add(CC,n,'Lamy','',LA,dd)
# Graf von Faber-Castell
GF=W+'Graf_von_Faber-Castell'
for n,y in [('Graf von Faber-Castell Guilloche',''),('Graf von Faber-Castell Intuition',''),('Graf von Faber-Castell Pen of the Year','2003')]:
    add(CC,n,'Graf von Faber-Castell',y,GF,'Graf von Faber-Castell line named on the maker article; '+NS+'.')
add(CC,'Faber-Castell E-Motion','Faber-Castell','',W+'Faber-Castell','Faber-Castell fountain pen line named on the maker article.')
# Sheaffer
SH=W+'Sheaffer'
addv(SA,'Sheaffer Snorkel','Pen For Men (PFM)','1959','last Snorkel pen')
for n,y,dd in [('Sheaffer Targa','1976','cartridge or converter'),('Sheaffer Connaisseur','1986','cartridge or converter'),('Sheaffer Legacy','',''),('Sheaffer Prelude','',''),('Sheaffer Sentinel','',''),('Sheaffer Taranis','',''),('Sheaffer Sagaris','',''),('Sheaffer Intensity','',''),('Sheaffer VFM','',''),('Sheaffer Valor','',''),('Sheaffer Ion','2017',''),('Sheaffer Pop','2017',''),('Sheaffer No-Nonsense','','low-cost line'),('Sheaffer School Pen','','low-cost line'),('Sheaffer 100','',''),('Sheaffer 300','',''),('Sheaffer 500','','')]:
    add(CC,n,'Sheaffer',y,SH,('Sheaffer line named on the maker article'+(': '+dd if dd else '')+'.'))
add(CC,'Cross Townsend','Cross','',W+'A._T._Cross_Company','Cross line named on the maker article; '+NS+'.')
# Waterman
WA=W+'Waterman_S._A.'
for n in ('Exception','Philéas','Edson','Harmonie','Charleston','Ici et Là','Audace','Sérénité','Liaison'): add(CC,'Waterman '+n,'Waterman','',WA,'Waterman line named on the maker article without a year; '+NS+'.')
# Esterbrook, Aurora, Parker
ES=W+'Esterbrook'
for n in ('Dollar Pen','Relief','Estie','Safari'): add(CC,'Esterbrook '+n,'Esterbrook','',ES,'Esterbrook pen named on the maker article; '+NS+'.')
add(CC,'Aurora Hastil','Aurora','1969',W+'Aurora_(pen_manufacturer)','Aurora pen launched 1969; '+NS+'.')
PK=W+'Parker_Pen_Company'
add(CC,'Parker Classic','Parker','1967',PK,'Parker pen of 1967; '+NS+'.')
add(CC,'Parker 100','Parker','2004',PK,'Parker pen of 2004; '+NS+'.')
add(CC,'Parker Arrow','Parker','1982',PK,'Parker pen of 1982; '+NS+'.')
for n in ('IM','Ingenuity','Urban','Premier','Frontier','Facet','Esprit','Reflex','Executive'): add(CC,'Parker '+n,'Parker','',PK,'Parker line in the 2012 product list on the maker article; no year given.')
# Inks
SI='Fountain pen ink'
for n,dd,v in [('Sailor Standard inks','Basic black, blue and blue-black in 50 ml bottles and cartridges.',None),('Sailor Pigmented inks','Waterproof inks: Kiwa-guro black, Seiboku and Souboku blue-black.',[('Kiwa-guro','','black'),('Seiboku','','blue-black'),('Souboku','','blue-black')]),('Sailor Jentle','Six colours in 50 ml round bottles; discontinued.',None),('Sailor Manyo','Flower-inspired colours in 50 ml bottles; sold overseas only.',None),('Sailor Ink Studio','About 100 colours named by three-digit numbers; sold at select US retailers.',None),('Sailor Yurameku','Multi-tonal, colour-shifting inks in 20 ml bottles; newest as of 2022.',None)]:
    add(SI,n,'Sailor','',SG,dd,v=v)
add(SI,'Platinum Pigment Blue','Platinum','','https://shop.gentlemanstationer.com/products/platinum-classic-inks-60ml','Pigmented blue ink sold in cartridges.')
add(SI,"Robert Oster Signature",'Robert Oster','','https://goldspot.com/collections/robert-oster-signature?aff=29','Dye-based Australian ink line in 50 ml bottles.',v=[(n,'','') for n in ('Tenth Anniversary','Gummy Shark','Steely Days','Sepia Nights','Romeo & Juliet','GoGo','Vine Leaf','Tokyo Blue Denim','Sydney Darling Harbor')])
add(SI,"Robert Oster Shake 'N' Shimmy",'Robert Oster','','https://goldspot.com/collections/robert-oster-signature?aff=29','Shimmer ink line in 50 ml bottles.',v=[(n,'','') for n in ('Skipidi',"Sinner's Dream",'Silver Dawn','Water','No Fixed Address','Violet Clouds','Blood Rose','Morning Shine','Aussie Liquid Gold')])
add(SI,'KWZ Standard inks','KWZ','','https://www.thejournalshop.com/collections/kwz-ink-brands','Standard (non-iron-gall) line of the Polish maker KWZ.')
add(SI,'KWZ Iron Gall inks','KWZ','','https://www.thejournalshop.com/collections/kwz-ink-brands','Iron-gall line of the Polish maker KWZ.')
for x in K[SI]['x']:
    if x['n']=='De Atramentis Document':
        x['v']=[{'n':n,'mk':'De Atramentis','y':'','d':''} for n in ['Black','Black Blue','Black Red','Blue','Brown','Cyan','Dark Blue','Dark Green','Dark Red','Fog Grey','Fuchsia','Gold','Green','Green Grey','Grey','Light Grey','Moss Green','Orange','Purple Violet','Red','Red Grey','Sepia Brown','Turquoise','Urban Grey','Urban Sienna','Violet','White','Yellow']]
        x['s']='https://www.gouletpens.com/collections/de-atramentis-document-inks'
# Pencils, notebooks
ST=W+'Staedtler'
add('Wooden pencil','Staedtler Noris','Staedtler','1901',ST,'Staedtler school pencil launched 1901.')
add('Wooden pencil','Mitsubishi Uni','Mitsubishi Pencil (Uni)','1958',W+'Mitsubishi_Pencil','Mitsubishi pencil launched 1958; the Hi-Uni followed in 1966.')
add('Wooden pencil','Faber-Castell Grip 2001','Faber-Castell','',W+'Faber-Castell','Graphite pencil line named on the maker article.')
add('Mechanical pencil','Uni Alpha-gel','Mitsubishi Pencil (Uni)','2003',W+'Mitsubishi_Pencil','Mechanical pencil with gel-cushioned grip, 2003.')
add('Mechanical pencil','Tombow Mono Graph','Tombow','',W+'Tombow','Tombow mechanical pencil in the Mono family (brand introduced 1963).')
addv('Notebook','Moleskine notebook','Evernote edition','2012','partnership with Evernote')
addv('Reporter\'s notebook','Field Notes','Quarterly limited editions','2009','annual subscription')
# ---- market fields
Gl='Global group';Nc='National champion';In='Independent';Cr='Craft & indie'
M={ 'Parker':('Newell Brands',Gl,'United States'),'Waterman':('Newell Brands',Gl,'France'),'Paper Mate':('Newell Brands',Gl,'United States'),'Sharpie':('Newell Brands',Gl,'United States'),'Expo':('Newell Brands',Gl,'United States'),'Bic':('Société Bic',Gl,'France'),
 'Montblanc':('Richemont',Gl,'Germany'),'Pilot':('Pilot Corporation',Nc,'Japan'),'Namiki':('Pilot Corporation',Nc,'Japan'),'Sailor':('Sailor Pen Co.',In,'Japan'),'Platinum':('Platinum Pen Co.',In,'Japan'),'Mitsubishi Pencil (Uni)':('Mitsubishi Pencil Co.',Nc,'Japan'),'Tombow':('Tombow Pencil Co.',In,'Japan'),'Pentel':('Pentel Co.',In,'Japan'),'Zebra':('Zebra Co.',In,'Japan'),'KOKUYO':('Kokuyo Co.',Nc,'Japan'),'Midori':('Designphil',In,'Japan'),'Nakaya':('Nakaya',Cr,'Japan'),'Danitrio':('Danitrio',Cr,'Japan'),
 'Lamy':('C. Josef Lamy GmbH',In,'Germany'),'Kaweco':('Kaweco',In,'Germany'),'Pelikan':('owner not stated',In,'Germany'),'Staedtler':('Staedtler SE',In,'Germany'),'Faber-Castell':('Faber-Castell',In,'Germany'),'Graf von Faber-Castell':('Faber-Castell',In,'Germany'),'Koh-i-Noor Hardtmuth':('Vlastislav Bříza',In,'Czech Republic'),'Caran d\'Ache':('owner not stated',In,'Switzerland'),'Leuchtturm1917':('Leuchtturm Albenverlag',In,'Germany'),'Clairefontaine':('Exacompta Clairefontaine',In,'France'),'Rhodia':('Exacompta Clairefontaine',In,'France'),'Hobonichi':('Hobo Nikkan Itoi Shinbun',In,'Japan'),'Field Notes':('owner not stated',Cr,'United States'),'Moleskine':('Moleskine',In,'Italy'),'TWSBI':('TWSBI',In,'Taiwan'),'Aurora':('owner not stated',In,'Italy'),'Visconti':('owner not stated',In,'Italy'),'OMAS':('owner not stated',In,'Italy'),
 'Diamine':('M.B.F. Group',In,'United Kingdom'),'J. Herbin':('owner not stated',In,'France'),"Noodler's":("owner not stated",Cr,'United States'),'De Atramentis':('owner not stated',In,'Germany'),'Rohrer & Klingner':('owner not stated',In,'Germany'),'Robert Oster':('owner not stated',Cr,'Australia'),'KWZ':('owner not stated',Cr,'Poland'),
 'HP':('HP Inc.',Gl,'United States'),'Texas Instruments':('Texas Instruments',Nc,'United States'),'Casio':('Casio Computer Co.',Nc,'Japan'),'Olivetti':('owner not stated',In,'Italy'),'IBM':('owner not stated',In,'United States'),'Cross':('owner not stated',In,'United States'),'Sheaffer':('owner not stated',In,'United States'),'Conklin':('owner not stated',In,'United States'),'Esterbrook':('owner not stated',In,'United States'),'Dixon Ticonderoga':('owner not stated',In,'United States'),'Speedball':('owner not stated',In,'United States')}
OY={'Rhodia':1997}
cnt=0
for k in K.values():
    for x in k.get('x',[]):
        mk=x.get('mk') or ''
        if mk in M: o,t,c=M[mk]
        else: o,t,c='owner not stated',In,''
        x['own']=o; x['tier']=t
        if c: x['cty']=c
        if mk=='Rhodia': x['own_y']=1997
        cnt+=1
# coverage lines
for kn,k in K.items():
    if k.get('x'):
        n=len(k['x'])
        base=re.sub(r' (Covers|Complete)[^.]*\.[^.]*$','',k['sel'])
        k['sel']=re.sub(r'\s*Covers \d+ (lines|models|entries|traditions)[^.]*\.?','',k['sel']).strip()
        k['sel']+=' Coverage: {} entries, taken from the maker, Wikipedia and retailer pages read for this pass; lines on makers\' pages not reached are not listed.'.format(n)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print(cnt, sum(len(v) for v in added.values()))
