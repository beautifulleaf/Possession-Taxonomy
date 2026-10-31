import json,re,copy,sys
R='/home/user/Possession-Taxonomy/'
A=json.load(open(R+'rebuild/out/A1.json'))
REG={x['n']:x for x in json.load(open(R+'rebuild/out/A1_brands.json'))['b']}
REGL={k.lower():v for k,v in REG.items()}
DEPTS=('Coats & jackets','Suits & formalwear','Workwear & uniform clothing')
W='https://en.wikipedia.org/wiki/'
FORMS='Named forms without a brand'
# countries for makers not in the register (country from the fetched page or the maker's own name)
EXTRA={'Eddie Bauer':('United States',''),'Peter Storm':('United Kingdom',''),'Castell & Son':('United Kingdom','1846'),
 'Hudson\'s Bay Company':('Canada',''),'Blue Bell':('United States','1904'),'Grenfell':('United Kingdom',''),
 'Le Coq Sportif':('France',''),'One-In-Hand Tie Company':('United States',''),'Gannex':('United Kingdom',''),
 'Driza-Bone':('Australia',''),'Jesse Langsdorf':('United States',''),'George Key':('United Kingdom',''),
 'Malden Mills':('United States',''),'Brooks Brothers':('United States','1818'),'Henry Poole & Co':('United Kingdom','')}
OWN={ # from the register's own description (fetched in the brand pass)
 'Aquascutum':('Shandong Ruyi','Independent',''),"Arc'teryx":('Amer Sports','Global group',''),
 'Mackintosh':('Yagi Tsusho','Independent',''),'Napapijri':('VF Corporation','Global group','2004'),
 'Rab':('Equip','Independent',''),'Stone Island':('Moncler','Global group','2020'),
 'The North Face':('VF Corporation','Global group','2000'),'DAKS':('Sankyo Seiko','Independent','1991'),
 "OshKosh B'gosh":("Carter's",'Global group',''),'Stubbies':('Workwear Group','Independent',''),
 'Fjällräven':('Fenix Outdoor','Independent',''),'Lacoste':('Maus Frères','Independent',''),
}
def reg(b): return REGL.get(b.lower())
def country(b):
    r=reg(b)
    if r and r.get('c'):
        return re.split(r' / ',r['c'])[0]
    if b in EXTRA: return EXTRA[b][0]
    return None

# ---- new entries: kind -> list of dicts. s='REG' uses the brand's register page.
def E(n,mk='',y='',d='',s='REG',a='',role=None,v=None,g=None):
    return dict(n=n,mk=mk,y=y,d=d,s=s,a=a,role=role,v=v or [],g=g)
NEW={
'Overcoat':[
 E('Greatcoat','', 'mid-1760s','Long military overcoat; Russian and Soviet forces used greatcoats from the mid-1760s, and the 19th-century name was watchcoat.',W+'Overcoat','watchcoat'),
 E('Ulster coat','', '','Long loose overcoat that later evolved into the polo coat when it lost its cape.',W+'Overcoat'),
 E('Paddock coat','','','Overcoat type named in the article, with no date or origin given.',W+'Overcoat'),
 E('British Warm','','First World War','Short wool coat first designed for British officers and made famous by Winston Churchill.',W+'Overcoat'),
 E('Petersham coat','','','Overcoat named after Viscount Petersham.',W+'Overcoat'),
 E('Redingote','','','Overcoat whose name comes through French from the English riding coat.',W+'Overcoat','riding coat'),
 E('Frock overcoat','','Regency era (1795-1837)','Overcoat of the Regency era.',W+'Overcoat'),
 E('Paletot','','Regency era','Regency-era overcoat type.',W+'Overcoat'),
 E('Burberry Camden car coat','Burberry','','',s='REG'),
],
'Pea coat':[
 E('Schott 740 Pea Coat','Schott NYC','','',s='REG'),
 E('Sterlingwear Authentic Peacoat','Sterlingwear','','',s='REG'),
 E('Reefer jacket','','','Officer or chief petty officer version of the pea coat with gold buttons and epaulettes.',W+'Pea_coat'),
 E('Bridge coat','','','Longer reefer jacket reaching the thighs.',W+'Pea_coat'),
],
'Trench coat':[ E('Sanyo Shokai 100-Year Coat','Sanyo Shokai','','',s='REG') ],
'Raincoat':[
 E('Gannex raincoat','Gannex','','Style of raincoat listed in the article, with no date given.',W+'Raincoat'),
 E('Driza-Bone oilskin coat','Driza-Bone','','Style of oilskin raincoat listed in the article, with no date given.',W+'Raincoat'),
 E('Mino','','','Japanese straw raincoat.',W+'Raincoat'),
 E('Kamleika','','','Aleut waterproof outer garment.',W+'Raincoat'),
 E('Pake (hieke)','','','New Zealand rain cape made from flax.',W+'Raincoat'),
 E('Kui la\'i (Ahu La\'i)','','','Hawaiian rain cape made from ti leaves.',W+'Raincoat'),
 E('Slicker','','1910s-1920s','Stiff, fully rubber raincoat.',W+'Raincoat'),
],
'Parka':[
 E('M-48 fishtail parka','','1948','First standardised fishtail parka; the M stands for model and the number is the year it was standardised.',W+'Parka'),
 E('M-65 fishtail parka','','1968','Fishtail parka that went into production in 1968.',W+'Parka'),
 E('Amauti','','','Traditional Inuit women\'s parka with a built-in baby pouch.',W+'Parka'),
 E('The North Face Arctic Parka','The North Face','','',s='REG'),
 E('Rains Fishtail Parka','Rains','','',s='REG'),
 E('Canada Goose Langford Parka','Canada Goose','','',s='REG'),
],
'Puffer coat':[ E('Uniqlo Ultra Warm Down','Uniqlo','','',s='REG') ],
'Cape':[
 E('Tilmatli','','','Mesoamerican cloak worn by Aztec nobles and elite warriors.',W+'Cape'),
 E('Ferraiolo','','','Cape worn by Catholic clergy at formal events outside ritual.',W+'Cape'),
 E('Cope','','','Liturgical vestment in the form of a cape.',W+'Cape'),
 E('Chaperon','','medieval','Medieval combination of a cape with a hood.',W+'Cape'),
 E('Caped ulster','','Victorian era','Ulster coat with one or more layered capes; the cape was dropped in the 1920s.',W+'Cape'),
 E('Gas cape','','20th century','Military cape issued with gas masks against liquid chemical agents.',W+'Cape'),
 E('Otavalo alpaca poncho','Ecualama','','',s='REG'),
],
'Flight jacket':[
 E('B-16 WASP','','','Flight jacket the article links to the Women Airforce Service Pilots.',W+'Flight_jacket'),
 E('M-445','','','US Navy flight jacket style.',W+'Flight_jacket'),
 E('CWU-36/P','','','Current Nomex military flight jacket.',W+'Flight_jacket'),
 E('Canada Goose Chilliwack Bomber','Canada Goose','','',s='REG'),
 E('Avirex leather bomber jacket','Avirex','','',s='REG'),
 E('Cockpit USA CWU-55/P','Cockpit USA','','',s='REG'),
],
'Field jacket':[
 E('Denison smock','','Second World War','Shorter field jacket worn by British commandos, paratroopers and snipers.',W+'Trench_coat'),
 E('Sahariana','','1943','Spanish Army model of 1943 used in Spanish Sahara; the article treats it as a safari jacket.',W+'Safari_jacket'),
],
'Souvenir jacket':[ E('Wacko Maria Souvenir Jacket','Wacko Maria','','',s='REG') ],
'Biker jacket':[
 E('Lewis Leathers Dominator','Lewis Leathers','','',s='REG'),
 E('Lewis Leathers Cyclone','Lewis Leathers','','',s='REG'),
 E('Schott Cafe Racer','Schott NYC','','',s='REG'),
 E('Langlitz Cascade','Langlitz Leathers','','',s='REG'),
 E('Buco J-24','Buco','','',s='REG'),
],
'Waxed cotton jacket':[
 E('Belstaff Roadmaster','Belstaff','','',s='REG'),
 E('Lewis Leathers Aviakit Wax Cotton Jacket','Lewis Leathers','','Wax cotton jacket from the Aviakit range, shown in the article.',W+'Waxed_jacket'),
],
'Mackinaw':[
 E('Fort St Joseph greatcoat','John Askin Jr.','1811','First forty woollen greatcoats, designed and made for the British Army at Fort St. Joseph; the short mackinaw followed in 1812.',W+'Mackinaw_coat',role='origin',g='United States'),
 E('Hudson\'s Bay point blanket coat','Hudson\'s Bay Company','','Commercial version of the point blanket coat, sold more than a century after 1811; a 1936 catalogue shows it.',W+'Mackinaw_coat',
   v=[{'n':'Filson mackinaw','mk':'C.C. Filson Co.','y':'late 20th century','d':'Modern maker named by the article'},{'n':'Johnson Woolen Mills mackinaw','mk':'Johnson Woolen Mills','y':'late 20th century','d':'Modern maker named by the article'}]),
 E('Pendleton 49er','Pendleton Woolen Mills','','',s='REG'),
 E('Swanndri bush shirt','Swanndri','','',s='REG'),
],
'Norfolk jacket':[
 E('Half Norfolk jacket','','','Norfolk jacket with fewer pleats and a half belt.',W+'Norfolk_jacket'),
 E('Norfolk suit','','1930s-1940s','Norfolk jacket paired with matching trousers; popular in the 1930s and 1940s, now rare.',W+'Norfolk_jacket'),
],
'Harrington jacket':[ E('Grenfell golf jacket','Grenfell','','Grenfell (formerly Haythornthwaite and Sons) claims to have made an identical jacket around the same time, from its golf jackets.',W+'Harrington_jacket') ],
'Varsity jacket':[
 E('Harvard letter sweater','Harvard University baseball team','1865','Letter sweater introduced by the Harvard baseball team, the origin of the letterman jacket.',W+'Letterman_(sports)',role='origin',g='United States'),
 E('Dehen 1920 Letterman jacket','Dehen 1920','','',s='REG'),
 E('Golden Bear Letterman jacket','Golden Bear','','',s='REG'),
],
'Track jacket':[],
'Bolero':[
 E('Shrug','','','Cropped cardigan-like garment; the bolero is its more formal, stiffer-fabric version.',W+'Bolero_jacket'),
 E('Chaquetilla','','','Matador jacket that inspired the bolero.',W+'Bolero_jacket'),
],
'Tracksuit':[ E('Le Coq Sportif Sunday suit','Le Coq Sportif','1920','Sweatpants-and-matching-top combination; Le Coq Sportif is said to have first made sweatpants in 1920.',W+'Tracksuit',role='origin') ],
'Shell jacket':[
 E('Rab Downpour','Rab','','',s='REG'),
 E('Berghaus Paclite','Berghaus','','',s='REG'),
 E('Mammut Eiger Nordwand','Mammut','','',s='REG'),
],
'Anorak':[
 E('Peter Storm cagoule','Peter Storm','early 1960s','Lightweight British anorak; Noel Bibby of Peter Storm Ltd is credited with inventing the cagoule.',W+'Parka',role='origin'),
 E('Fjällräven Vardag Anorak','Fjällräven','','',s='REG'),
 E('Fjällräven Singi X-Anorak','Fjällräven','','',s='REG'),
],
'Puffer jacket':[
 E('Eddie Bauer Skyliner','Eddie Bauer','1936','Down jacket Bauer made after a hazardous fishing trip, first sold as the Skyliner; he is said to have patented the design in 1939.',W+'Down_jacket',role='origin'),
 E('Charles James pneumatic jacket','Charles James','1937','Quilted white satin jacket developed for haute couture and labelled the pneumatic jacket.',W+'Down_jacket'),
 E('Herno Laminar','Herno','','',s='REG'),
 E("Arc'teryx Atom",'Arc\'teryx','','',s='REG'),
],
'Fleece jacket & pullover':[
 E('PolarFleece','Malden Mills','1979','Polar fleece developed by Malden Mills (now Polartec); the PolarFleece trademark was filed in 1981.',W+'Polar_fleece',role='origin'),
 E('Patagonia Better Sweater','Patagonia','','',s='REG'),
 E('Columbia Benton Springs','Columbia Sportswear','','',s='REG'),
 E('Columbia Steens Mountain','Columbia Sportswear','','',s='REG'),
 E('Rab Ascendor','Rab','','',s='REG'),
],
'Business suit':[
 E('Brooks Brothers ready-to-wear suit','Brooks Brothers','','Brooks Brothers is credited with first offering the ready-to-wear suit.',W+'Suit',role='origin'),
 E('Zoot suit','','','Exaggerated high-waisted suit named in the list of suit types.',W+'Suit'),
 E('Mao suit (Zhongshan suit)','Hongdu','20th century','Suit from 20th-century China; Hongdu still makes bespoke Zhongshan suits.',W+'Suit'),
 E('Nehru suit','Tasva','','Five-button suit made from khadi, worn by Indian men after independence.',W+'Suit'),
 E('Kariba suit','','','Jamaican suit named in the list of suit types.',W+'Suit'),
 E('Senator suit','','','Nigerian suit named in the list of suit types.',W+'Suit'),
 E('Bocskai suit','','','Hungarian suit named in the list of suit types.',W+'Suit'),
 E('Chokha','','','Georgian and Caucasian suit named in the list of suit types.',W+'Suit'),
 E('Nudie suit','','','Embroidered Western suit named in the list of suit types.',W+'Suit'),
],
'Blazer':[
 E('Lady Margaret Boat Club boating jacket','Lady Margaret Boat Club','1825','Red boating jacket of the St John\'s College club, Cambridge, that gave the blazer its name.',W+'Blazer',role='origin',g='United Kingdom'),
 E('Half-blue blazer','','','University sports blazer, shown for Cambridge and Oxford.',W+'Blazer'),
 E('Regimental blazer','','','Blazer worn by armed-service veterans\' associations.',W+'Blazer'),
 E('Striped Mod blazer','','early 1960s','Striped blazer of the Mod scene, revived in the late 1970s.',W+'Blazer'),
],
'Waistcoat':[
 E('Favourbrook odd waistcoat','Favourbrook','','',s='REG'),
 E('M.B. waistcoat','','c. 1830','Clerical waistcoat.',W+'Waistcoat'),
 E('Fringed vest','','1960s','Folk-style vest of the 1960s.',W+'Waistcoat'),
],
'Morning dress':[ E('Stroller','','','Black lounge suit, the daytime counterpart of black tie.',W+'Tuxedo') ],
'Tailcoat':[
 E('Shadbelly','','18th century','Daytime riding coat of the eighteenth century.',W+'Tailcoat'),
 E('Levee dress coat','','','Court coat worn until the mid-twentieth century.',W+'Tailcoat'),
 E('Frock coat','','','Formal day coat replaced by the morning coat in the early twentieth century.',W+'Tailcoat'),
],
'Smoking jacket':[
 E('Banyan','','18th century','Knee-length 18th-century night gown with shawl collars.',W+'Smoking_jacket'),
 E('Robe de chambre','','17th century','Silk gown fashionable in 17th-century portraits.',W+'Smoking_jacket'),
],
'Tie':[
 E('Castell & Son necktie','Castell & Son','1870','Oxford firm opened in 1846, credited with the first modern-style necktie.',W+'Necktie',role='origin'),
 E('Langsdorf bias-cut tie','Jesse Langsdorf','1922','New York tie maker who introduced bias-cut ties.',W+'Necktie'),
 E('One-In-Hand clip-on tie','One-In-Hand Tie Company','1930s-1950s','Clinton, Iowa, firm that made pre-tied and clip-on neckties.',W+'Necktie'),
 E('College tie','','1880','Collegiate tie, with precursors in the 1880 Exeter College rowers.',W+'Necktie'),
 E('Six-fold tie','','','Modern alteration of the seven-fold tie.',W+'Necktie'),
 E("Drake's tie","Drake's",'','',s='REG'),
 E('Charvet tie','Charvet','','',s='REG'),
 E('Polo Ralph Lauren tie','Ralph Lauren','','',s='REG'),
 E('Tootal tie','Tootal','','',s='REG'),
],
'Bow tie':[ E('Lido Grip bow tie','', '1950s-1960s','Clip-on bow tie style of the 1950s and 1960s.',W+'Bow_tie') ],
'Ascot & cravat':[
 E('Lavalliere','','19th century','Similar cravat with a larger knot and drooping ends, from 19th-century France.',W+'Bow_tie'),
 E('Stock tie','','1715','Stiff neckcloth.',W+'Necktie'),
 E('Solitaire','','18th century','Neckwear variation of the bag-wig style.',W+'Necktie'),
],
'Cummerbund & collar stay':[
 E('Kamarband','','','Hindustani term for the cummerbund, used for dress uniforms in South Asian armies.',W+'Cummerbund'),
 E('Zeybek kushak','','','Turkish sash shown in the article\'s etymology section.',W+'Cummerbund'),
],
'Pocket square':[
 E("Drake's pocket square","Drake's",'','',s='REG'),
 E('Rubinacci pocket square','Rubinacci','','',s='REG'),
],
'Braces':[ E('Trafalgar braces','Trafalgar','','',s='REG') ],
'Work trousers':[
 E('Age of Glory Service Pant','Age of Glory','','',s='REG'),
 E('Elizabeth Suzann Clyde Work Pant','Elizabeth Suzann','','',s='REG'),
 E('Pike Brothers 1962 OG-107 Pant','Pike Brothers','1962','',s='REG'),
 E('Stubbies workwear shorts','Stubbies','','',s='REG'),
],
'Overalls':[
 E('Blue Bell overalls','Blue Bell','1904','North Carolina firm popular with railroad workers; Big Ben bought it in 1926 and continued under the Blue Bell name.',W+'Overalls'),
 E('Salopettes','','','French term for bib-and-brace overalls, also heavy-duty versions for sailing, skiing and diving.',W+'Overalls'),
 E('Shortalls','','','Overalls with the lower part adapted into shorts.',W+'Overalls'),
],
'Boiler suit':[
 E('Siren suit','','Second World War','Boiler suit popularised by Winston Churchill.',W+'Boilersuit'),
 E('Lee Union-All','Lee','','',s='REG'),
 E('Tyvek suit','DuPont','','Disposable boilersuit made of DuPont Tyvek.',W+'Boilersuit'),
 E('Student boilersuit','','','Boilersuit worn by university students in some Nordic countries.',W+'Boilersuit'),
],
'Chore coat':[
 E('Le Mont Saint Michel 1913 Work Jacket','Le Mont Saint Michel','','',s='REG'),
 E('Le Laboureur Moleskin Work Jacket','Le Laboureur','','',s='REG'),
 E('Vetra Workwear Jacket','Vétra','','',s='REG'),
 E('Carhartt chore coat','Carhartt','1917','American mass-produced version of 1917 with a corduroy-lined collar.',W+'Chore_jacket'),
 E('Pointer Brand chore coat','Pointer Brand','','',s='REG'),
],
'Donkey jacket':[ E('Key donkey jacket','George Key','1888','Developed in Rugeley, Staffordshire, for navvies building the Manchester Ship Canal; named after the steam donkey engines.',W+'Donkey_jacket',role='origin') ],
'Lab coat':[
 E('Howie-style lab coat','','1978','Named after James Howie, who chaired a 1978 UK report; the older wrap-around coat is the Howie-style coat.',W+'Lab_coat'),
 E('Black lab coat','','until mid-1920s','Worn by students examining cadavers until the mid-1920s.',W+'Lab_coat'),
],
}
# extra versions appended to existing entries
ADDV={ ('Biker jacket','Schott Perfecto'):[
   {'n':'613 One Star','mk':'Schott NYC','y':'late 1940s','d':'Shoulder stars; discontinued mid-1980s and reintroduced late 1980s or early 1990s'},
   {'n':'618','mk':'Schott NYC','y':'early 1950s','d':'The 613 without the shoulder stars'},
   {'n':'118','mk':'Schott NYC','y':'1977','d':'Naked cowhide; fuller fit from the early 1990s'},
   {'n':'Beck 333 Northeaster','mk':'Schott NYC','y':'','d':'Similar jacket Schott made for the Beck label'}],
 ('Trucker jacket',"Levi's Type III (557 / 70505)"):[
   {'n':'Jacquard by Google connected jacket','mk':"Levi's",'y':'2014','d':'Connected jacket made with Google; a second version followed in late 2019'}],
}
ROLE={'Burberry Heritage trench':'origin','Aquascutum trench':'origin','Mackintosh':'origin',"Levi's Type I (506XX)":'origin',
 'Baracuta G9':'origin','Yokosuka sukajan':'origin','Dinner jacket':'origin','Bleu de travail':'origin'}

# ---- continuation: restored pieces (data/named_forms.tsv pages) and brand pages fetched in the second pass
RJ=json.load(open(R+'rebuild/work/V4_A1_OUTER/restore.json'))
EXC=RJ['excountry']
for r in RJ['entries']:
    NEW.setdefault(r['kind'],[]).append(E(r['n'],r['mk'],'','',s=r['s']))
for r in RJ['vers']:
    par=r['parent']
    if par: ADDV.setdefault((r['kind'],par),[]).append({'n':r['n'],'mk':r['mk'],'y':'','d':''})
def M(kind,n,mk,y,d,s,**kw): NEW.setdefault(kind,[]).append(E(n,mk,y,d,s,**kw))
M('Business suit','Ossie Clark Lamborghini trouser suit','Ossie Clark','1969','Cotton satin trouser suit with a Celia Birtwell print; Clark was among the first to produce trouser suits for women.','https://collections.vam.ac.uk/item/O86592/lamborghini-trouser-suit-clark-ossie/')
M('Trench coat',"Nobis Nord Men's Tailored Trench Coat",'Nobis','','Down trench coat with an Embrace membrane laminated construction.','https://us.nobis.com/products/nord-mens-tailored-trench-coat')
M('Waxed cotton jacket','Barbour Classic Northumbria','Barbour','','Heavyweight 8oz Sylkoil waxed cotton outer.','https://www.barbour.com/gb/classic-northumbria%C2%AE-waxed-jacket-MWX0009OL91.html')
M('Waxed cotton jacket','Barbour Corbridge','Barbour','','Made from 6oz Sylkoil waxed cotton.','https://www.barbour.com/gb/corbridge-waxed-jacket-MWX0340RU94.html')
M('Puffer coat','Patagonia Jackson Glacier','Patagonia','','Insulated with 700-fill-power recycled down.','https://www.patagoniabend.com/collections/jackson-glacier')
M('Puffer coat','Outdoor Research Coze Down Parka','Outdoor Research','','240 grams of 700-fill down insulation.','https://www.outdoorgearlab.com/reviews/clothing-womens/winter-jacket-womens/outdoor-research-coze-down-parka')
M('Puffer coat','Fjallraven Nuuk Parka','Fjällräven','','Supreme Micro Loft padding; previously known as the Yupik parka.','https://www.nordicoutdoor.co.uk/products/fjallraven-mens-nuuk-parka')
M('Puffer jacket','Eddie Bauer CirrusLite Hooded','Eddie Bauer','','Uses 650 fill power down.','https://www.outdoorgearlab.com/reviews/clothing-mens/down-jacket-men/eddie-bauer-cirruslite-hooded')
M('Puffer jacket','Decathlon Simond MT100','Decathlon','','Insulated with 800-fill-power down.','https://www.outdoorgearlab.com/reviews/clothing-mens/down-jacket-men/decathlon-simond-mt100-hooded-puffer')
M('Puffer jacket','Stio Hometown Down Hooded Jacket','Stio','','Insulated with 800-fill down.','https://elevationoutdoors.com/?p=44444')
M('Fleece jacket & pullover',"Arc'teryx Kyanite Lightweight Hoody","Arc'teryx",'','Weighs 10.8 ounces in a men\'s medium.','https://www.outdoorgearlab.com/reviews/clothing-mens/fleece-jacket-men/arcteryx-kyanite-lightweight-hoody')
M('Flight jacket','Type A1 flight jacket','Chapal','1925','Leather flight jacket created by Chapal in 1925 and standard US military issue from 1927.',W+'Leather_jacket')
M('Leather & suede jacket','Eight-ball jacket','','1990s','Leather jacket that was briefly trendy in the 1990s.',W+'Leather_jacket')
M('Cut-off vest','Battle jacket','','','Leather or denim jacket developed by the early punk movement.',W+'Leather_jacket')
M('Tailcoat','Mess jacket','','','Short formal jacket named with the tailcoat among formal day and evening wear.',W+'Tuxedo')
M('Blazer','Teba jacket','','','Jacket type named among black-tie alternatives.',W+'Tuxedo')
EXTRA.update({'Outdoor Research':('United States',''),'Decathlon':('France',''),'Stio':('United States',''),'Nobis':('Canada',''),'Ossie Clark':('United Kingdom',''),'Chapal':('France',''),'John Askin Jr.':('United States','')})
for k_,v_ in EXC.items():
    if v_: EXTRA.setdefault(k_,(v_,''))
OWN.update({
 'Schott NYC':('Schott family','Independent',''),'Burberry':('Burberry Group plc','Independent',''),
 'Canada Goose':('Bain Capital and others','Independent','2013'),'Barbour':('J. Barbour & Sons Limited (family)','Independent',''),
 'Carhartt':('Carhartt (Hamilton Carhartt descendants)','Independent',''),'Dickies':('Bluestar Alliance','Independent','2025'),
 'Belstaff':('Castore','Independent','2025'),'Pendleton Woolen Mills':('Pendleton Woolen Mills (privately held)','Independent',''),
 'Lee':('Kontoor Brands','Global group','2019'),'Wrangler':('Kontoor Brands','Global group','2019'),
 'Uniqlo':('Fast Retailing','Global group',''),'Moncler':('Moncler','Global group',''),
 "Arc'teryx":('Amer Sports','Global group',''),'Stubbies':('Workwear Group','Independent',''),
 'Fjällräven':('Fenix Outdoor International AG','Independent',''),'Rab':('Equip Outdoor Technologies','Independent',''),
})
DPATCH={ # (kind,entry) -> (d, y)
 ('Biker jacket','Schott Cafe Racer'):('Single-rider jacket with a stand collar; Peter Fonda wore a cafe racer style jacket in Easy Rider (1969).',''),
 ('Trench coat','Sanyo Shokai 100-Year Coat'):('Brand name 100 Year Coat in Sanyo Shokai\'s list of brands.',''),
 ('Waxed cotton jacket','Lewis Leathers Aviakit Wax Cotton Jacket'):('Wax cotton jacket from the Aviakit range, which Lewis Leathers introduced in 1930.','1930'),
 ('Business suit','Kariba suit'):('Jamaican suit; Ivy Ralph\'s Kareeba suit joined The Met\'s collection (2025).','2025'),
 ('Mackinaw','Pendleton 49er'):('Women\'s wool jacket from the 1949 women\'s sportswear line; it proved extremely popular.','1949'),
 ('Mackinaw','Swanndri bush shirt'):('Original long heavy bush shirt of the brand: a hooded woollen garment known as the swanny.',''),
 ('Boiler suit','Lee Union-All'):('Work jumpsuit introduced in 1913 that prompted the company\'s growth.','1913'),
 ('Work trousers','Stubbies workwear shorts'):('Stubbies shorts were first introduced in Australia in 1972; the range later grew to include workwear.','1972'),
}
SEEMIL=['E4','Militaria & replicas','issued military kit is not bought by owners; surplus and replicas are listed here']
SEEKINDS={'Flight jacket','Field jacket','Deck jacket'}
EXCL_G={'Named forms without a brand'}

def mkcountry(e):
    mk=(e.get('mk') or '').split(',')[0].strip()
    if not mk: return None
    c=country(mk)
    return c
def cleanentry(e):
    x={'n':e['n'],'a':e.get('a',''),'d':e.get('d',''),'mk':e.get('mk',''),'y':e.get('y',''),'s':e['s'],'v':e.get('v',[])}
    if e.get('dt'): x['dt']=e['dt']
    return x

out_depts=[];newbrands={};bu={}
stats={}
dropped=[];regm=[]
for dp in A['depts']:
    if dp['n'] not in DEPTS: continue
    nd=copy.deepcopy(dp)
    for sh in nd['s']:
        for k in sh['k']:
            old=k.get('x') or []
            before=len(old)
            ents=[copy.deepcopy(e) for e in old]
            # drop m
            for m in (k.pop('m',None) or []):
                dropped.append((k['n'],m))
            names={e['n'].lower() for e in ents}
            for ne in NEW.get(k['n'],[]):
                if ne['n'].lower() in names: continue
                s=ne['s']
                if s=='REG':
                    r=reg(ne['mk']); s=r.get('s') if r else ''
                    if not s: print('NO REG S',ne['n']); 
                ent=cleanentry(dict(ne,s=s))
                if ne.get('role'): ent['role']=ne['role']
                if ne.get('g'): ent['_g']=ne['g']
                ents.append(ent)
            for e in ents:
                dp_=DPATCH.get((k['n'],e['n']))
                if dp_:
                    e['d']=dp_[0]
                    if dp_[1]: e['y']=dp_[1]
                e.pop('dt',None) if False else None
                mk=(e.get('mk') or '').split(',')[0].strip()
                c=None
                if e.get('_g'): c=e.pop('_g')
                elif mk:
                    c=country(mk)
                    if c is None and e['mk']=='Aranda': c='Lesotho'
                if mk and c is None:
                    # brand not in the register: country from first matching register name
                    c=EXTRA.get(mk,(None,))[0]
                e['g']=c if (mk and c) else FORMS
                if mk and c:
                    e['cty']=c
                    o=OWN.get(mk)
                    if o:
                        e['own']=o[0]; e['tier']=o[1]
                        if o[2]: e['own_y']=o[2]
                if e['n'] in ROLE: e['role']=ROLE[e['n']]
                for (kn,en),vs in ADDV.items():
                    if kn==k['n'] and en==e['n']: e['v']=e.get('v',[])+vs
            # order: brand countries alpha, then brand, then year; forms last
            def key(e):
                form=e['g']==FORMS
                return (form,e['g'] if not form else '',(e.get('mk') or '').lower(),str(e.get('y')),e['n'].lower())
            ents.sort(key=key)
            if ents: k['x']=ents
            else: k.pop('x',None)
            n=len(ents)
            stats[k['n']]=(before,n)
            if n:
                k['nl']=('One entry is a signature piece: a garment sold under its own name by the brand that originated it, or a named garment form the cited Wikipedia article lists; versions are fits, generations and fabrics the brand lists.')
                refs=k.get('s','')
                cov={}
                # coverage line
                k['_cov']=n
            else:
                k['nl']=('No named entries: no fetched Wikipedia article on this garment names a brand or a list of named types, and no register signature piece matches it.')
            k['xg']='by brand home country, then brand, then year; named forms without a brand last'
            if k['n'] in SEEKINDS:
                see=k.get('see') or []
                if SEEMIL not in see: see.append(SEEMIL)
                k['see']=see
    out_depts.append(nd)
json.dump({'depts':out_depts,'stats':stats,'dropped':dropped},open(R+'rebuild/work/V4_A1_OUTER/stage1.json','w'),ensure_ascii=False)
print(len(dropped),'models dropped/folded')
for k,v in stats.items(): print(k,v)
