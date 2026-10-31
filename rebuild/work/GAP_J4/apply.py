import json,re,os,collections
W='/home/user/Possession-Taxonomy/rebuild/work/GAP_J4/'
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(W+'bak/J4.json'))
K={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
WP='https://en.wikipedia.org/wiki/'
def norm(n):
    n=n.lower(); n=re.sub(r'\(.*?\)|\[.*?\]','',n); n=re.sub(r"[’'\"‘`]",'',n)
    n=re.sub(r'\b(pdo|pgi|gi|aop|cultivar|strawberry|banana|plantain|lemon|cucumber|basil)\b','',n)
    n=re.sub(r'[^\w ]+',' ',n)
    return re.sub(r'\s+',' ',n).strip()
def keys(x):
    ks={norm(x['n'])}
    for t in re.split(r'[;·,]',x.get('a') or ''):
        if t.strip(): ks.add(norm(t))
    return {k for k in ks if k}
added=collections.defaultdict(list)
def add(kind,n,d_,s,y='',a='',dt=None,mk='',**kw):
    k=K[kind]; k.setdefault('x',[])
    e={'n':n,'a':a,'d':d_,'mk':mk,'y':y,'s':s,'v':[]}
    if dt: e['dt']=dt
    e.update(kw)
    have=set()
    for x in k['x']: have|=keys(x)
    if keys(e)&have: return
    k['x'].append(e); added[kind].append(n)
def bulk(kind,rows,src,tpl,y_in=True):
    for r in rows:
        n,y,o=(list(r)+['',''])[:3]
        add(kind,n,tpl.format(n=n,o=o,y=y).replace(' from ,',',').replace('  ',' '),src,y=y)
# Pear
P=WP+'List_of_pear_cultivars'
bulk('Pear',[('Alexander Lucas','1870','Loire-et-Cher, France'),('Beurré Hardy','c1820','Boulogne-sur-Mer, France'),('Blanquilla','','Spain'),('Louise Bonne','1778','Normandy, France'),('Merton Pride','1941','England'),('Santa Maria','1951','Italy'),('Passe Crassane','1855','Rouen, France'),('Starkrimson','1939','Michigan, United States'),('Moonglow','1960',''),('Comtesse de Paris','1884','Eure-et-Loir, France'),('Glou Morceau','1750','Belgium'),('Josephine de Malines','1830','Mechelen, Belgium')],P,'Pear cultivar listed in Wikipedia\'s list of pear cultivars; origin {o}.')
bulk('Asian pear',[('Chojuro','1895','Japan'),('Kikusui','',''),('Shinseki','',''),('Tsu Li','',''),('Yakumo','','')],P,'Asian pear cultivar listed in Wikipedia\'s list of pear cultivars; origin {o}.')
# Apple
add('Apple','Worcester Pearmain','Table apple named in Wikipedia\'s list of apple cultivars.',WP+'List_of_apple_cultivars')
# Tomato full list
T=WP+'List_of_tomato_cultivars'
tom="""Alicante|UK trade|Amish Paste||Azoychka|Russia|Aunt Ruby's German Green|Germany, grown in Tennessee|Beefsteak||Better Boy||Berkeley Tie-Dye Green|California|Big Beef|1994|Big Rainbow||Blaby Special|Blaby, England|Black Beauty|Napa, California|Black Cherry||Black Icicle||Black Krim|Crimea|Brandywine|1885|Carbon||Campari||Canario||Celebrity|1998|Cherokee Purple|North Carolina|Cherry Bambelo||Cherry Nebula||Chocolate Pear||Dad's Sunset||Dester|Germany|Dr. Wyche's Yellow|1985|Early Girl||Ed's Millennium|California|Emerald Evergreen|1950|Enchantment||Ferris Wheel|1894|Flamenco||Fourth of July||Gardener's Delight||Garden Peach||German Johnson||German Lunchbox|Missouri|German Pink|1883|Giulietta||Granadero||Great White||Green Doctors|2002|Green Giant|Germany|Green Zebra|1983|Hanover||Henderson's Pink Ponderosa|1891|Hillbilly||Hungarian Heart|1901|Japanese Black Trifele||Jersey Boy|2015|Jubilee|1943|Juliet|1999|Kellogg's Breakfast|West Virginia|Kentucky Beefsteak||Kumato||Lillian's Yellow|Tennessee|Malakhitovaya Shkatulka|Siberia|McDreamy||Matt's Wild Cherry|Mexico|Micro Tom||Millionaire|1950|Moneymaker||Monterosa||Montserrat||Mortgage Lifter|1920|Mr. Stripey||Mushroom Basket|Russia|Napa Rose Blush|Napa, California|Orange Hat||Orange Icicle||Pantano Romanesco||Paul Robeson|Russia|Pink Boar||Raf||Raspberry Lyanna||Rebekah Allen||Rebellion||Red Currant||Rosa de Barbastro||Rosella||Rutgers|New Jersey|Sasha Altai|1989|Scorpio|Queensland|Stupice||Thorburn's Terra-cotta|1893|Tigerella||Tiny Tim|1945|Tomkin||Traveller (Arkansas Traveler)||True Black Brandywine|1920|Tomaccio|Israel|Violet Jasper||Yellow Brandywine|1991|Wagner Blue Green||White Queen||Yellow Pear||Ailsa Craig||Indigo Rose||Marglobe||Pomodorino del Piennolo del Vesuvio||Pomodoro di Pachino||Siberian||Three Sisters||Tomberry||Super Sweet 100||Pomodorino di Manduria||Santorini|Greece||San Marzano||Roma"""
toks=tom.split('|')
rows=[];i=0
# parse as name|origin/year pairs
import itertools
pairs=[]
it=iter(toks)
for n in it:
    o=next(it,'')
    pairs.append((n,o))
for n,o in pairs:
    y=o if re.fullmatch(r'\d{4}',o) else ''
    org='' if y or not o else o
    desc='Tomato cultivar listed in Wikipedia\'s list of tomato cultivars'+(f'; origin {org}' if org else '')+(f'; dated {y}' if y else '')+'.'
    add('Tomato',n,desc,T,y=y)
# Chilli full list
C=WP+'List_of_Capsicum_cultivars'
chi={'Capsicum annuum':"Aleppo|Anaheim|Baklouti|Banana|Bird's Eye|Black Heart|Black Hungarian|Cascabel|Cascabella|Cayenne|Cheongyang|Cherry|Chilaca|Chiltepin|Chilhuacle|Chimayó|Cubanelle|Dangjo|De Árbol|Elephant Trunk|Facing Heaven|Fish|Fresno|Friggitelli|Guntur Sannam|Hungarian Wax|Italian Sweet|Jalapeño|Jwala|Korean chili|Medusa|Mirasol|NuMex Twilight|Peter Pepper|Peperoncino|Peperone crusco|Pimiento|Pequin|Piment d'Espelette|Padrón|Poblano|Prairie Fire|Prik Kee Nu|Puya|Santa Fe Grande|Serrano|Shishito|Siling Mahaba|Xcatic|Almora Lakhori Mirchi|Banaras Lal Bharwamirch|Beaver Dam|Bhiwapur|Big Jim|Byadagi|Chocolate habanero|Dragon's Breath|Diavoletto d'Abruzzo|Dundicut|Edayur|Er jing tiao|Guajillo|Habanaga|Harmal|Kashmiri red|Khola|Mulato|Nandurbar Mirchi|No. 9|Piquillo|Ramnathapuram Mundu|Sandia|Sirarakhong Hathei|Sweet piquanté pepper",
'Capsicum baccatum':"Bishop's Crown|Aji Limon|Piquante pepper|Sugar Rush Peach|Sugar Rush Stripey|Brazilian Starfish",
'Capsicum chinense':"Adjuma|Ají Dulce|Bhut Jolokia|Carolina Reaper|Datil|Fatalii|Habanero|Hainan Yellow Lantern|Infinity chili|Madame Jeanette|Naga Morich|Naga Viper|NuMex Suave Orange|Pepper X|Red Savina|Scotch Bonnet|Trinidad Moruga Scorpion|Trinidad Scorpion Butch T|Aji Charapita|7 Pot Primo|Nagabon|Naga Mircha",
'Capsicum frutescens':"Kambuzi|Labuyo|Peri-peri|Malagueta|Tabasco|Xiao mi la pepper|Mizo",
'Capsicum pubescens':"Canário|Rocoto"}
for sp,s in chi.items():
    for n in s.split('|'):
        add('Chilli',n,f'Chilli cultivar named in Wikipedia\'s list of Capsicum cultivars, species {sp[9:]}.',C,dt=sp)
# Persimmon
PS=WP+'Persimmon'
bulk('Persimmon',[('Great Wall','','Chinese variant with medium-sized orange fruit'),('Gosho','','giant Fuyu'),('Hyakume','','brown sugar'),('Giombo','','large fruit, pollination variant'),('Midia','','large fruit with an indented ring'),('Cioccolatino','',''),('Vainiglia','','traditional variety from Campania, Italy'),('Tipo','','Italian variety'),('Maru','','cinnamon'),('Ormond','','also known as Christmas persimmon'),('Fankio','','large golden fruit'),('Saijo','','sweet conical fruit'),('Tamopan','','large and flat'),('Taishu','',''),('Soshu','',''),('Suruga','','sweet and spicy fruit'),('Izu','','medium fruit'),('Hana Fuyu','','grown in California, marketed as Giant Fuyu'),('Hanagosho','','large tree with good crop regulation'),('Matsumoto Wase','','bud sport of Fuyu'),('Tone Wase','',''),('Shogatsu','','similar to Hanagosho'),('Dan gam','','Korean sweet persimmon'),('Hongsi','','Korean ripe persimmon')],PS,'Persimmon cultivar named in Wikipedia\'s persimmon article{o_}.')
for e in K['Persimmon']['x']:
    if e['s']==PS and e['d'].endswith('{o_}.'): pass
# fix template for persimmon
for e in K['Persimmon']['x']:
    if '{o_}' in e['d']: e['d']=e['d'].replace('{o_}','')
# the bulk template used {o}; rebuild persimmon descs
orig={('Great Wall'):'Chinese variant with medium-sized orange fruit'}
# Citrus etc
add('Orange','Midknight','Valencia orange cultivar named in Wikipedia\'s list of citrus fruits as "Midknight Valencia".',WP+'List_of_citrus_fruits')
add('Mandarin','Fairchild','Mandarin cultivar named in Wikipedia\'s list of citrus fruits.',WP+'List_of_citrus_fruits')
add('Pomelo','Dangyuja','Korean pomelo cultivar named in Wikipedia\'s list of citrus fruits.',WP+'List_of_citrus_fruits')
add('Lime','Makrut lime','Lime species with fragrant leaves and rind, named in Wikipedia\'s list of citrus fruits as kaffir lime.',WP+'List_of_citrus_fruits',a='Kaffir lime')
# sweet potato
SP=WP+'List_of_sweet_potato_cultivars'
add('Sweet potato','Ayamurasaki','Purple-fleshed Okinawan sweet potato, also called beniimo.',SP)
add('Sweet potato','Stokes Purple','Purple sweet potato of unknown origin in North Carolina, made publicly available in 2012.',SP,y='2012')
add('Sweet potato','Garnet','US sweet potato commonly sold as "yam" to distinguish it from O\'Henry.',SP)
add('Sweet potato',"O'Henry",'US sweet potato bred by Henry Wayne Bailey as a Beauregard mutation.',SP)
add('Sweet potato','Hannah Sweet','Sweet potato cultivar listed in Wikipedia\'s list of sweet potato cultivars; origin not stated.',SP)
# strawberry
ST=WP+'List_of_strawberry_cultivars'
for n,y,o in [('AC-Yamaska','2001','Agriculture and Agri-Food Canada'),('Favori','2013','Flevo Berry Holding, Netherlands'),('Florence','1997','East Malling Research, UK'),('Gaviota','1998','University of California'),('Hapil','1977','Belgium'),('Hokowase','1960','Hyogo Prefecture, Japan'),('Pegasus','1990','USDA and England'),('Sable','1998','USDA'),('Sussette','2013','Flevo Berry Holding, Netherlands'),('Symphony','1993','James Hutton Institute, Scotland'),('Wendy','2006','Agriculture and Agri-Food Canada'),('Evie 2','2006','Edward Vinson Ltd, UK'),('Cavendish','1990','Agriculture and Agri-Food Canada, Nova Scotia'),('Kent','1981','Agriculture and Agri-Food Canada, Nova Scotia'),('Rainier','1972','Washington State University'),('Alinta','',''),('Frel','','Pink Panda'),('Malling Opal','',''),('Malling Pearl','',''),('Redgauntlet','','Scotland'),('Rhapsody','',''),('Sonata','','')]:
    add('Strawberry',n,'Strawberry cultivar listed in Wikipedia\'s list of strawberry cultivars'+(f'; bred by {o}' if o else '')+'.',ST,y=y,a=('Pink Panda' if n=='Frel' else ''))
add('Strawberry','Mahabaleshwar Strawberry GI','Strawberry grown around Mahabaleshwar, Maharashtra, registered as an Indian geographical indication in 2010-11.','https://en.wikipedia.org/wiki/List_of_geographical_indications_in_India',y='2010')
# banana/plantain
B=WP+'List_of_banana_cultivars'
for n,g in [('Burro','ABB group (Bluggoe)'),('Lakatan','AA group'),('Mysore','AAB group, Mysore subgroup'),('Ney Poovan','AB group'),('Pisang Ambon','AAA group, Gros Michel subgroup'),('Señorita','AA group; also Monkoy'),('Thousand Fingers','AAB group'),('Robusta','AAA group, Cavendish subgroup'),('Red Dacca','AAA group')]:
    add('Banana',n,f'Banana cultivar, {g}, listed in Wikipedia\'s list of banana cultivars.',B)
for n,g in [('French plantain','AAB group'),('Horn plantain','AAB group'),('Dominico','AAB group, Colombia'),('Dominico-Harton','AAB group, Colombia'),('Pisang Awak','ABB group'),('Maqueño','AAB group, Maoli-Popo\'ulu subgroup'),('Pelipita','ABB group'),('Tanduk','AAB group, Indonesia')]:
    add('Plantain',n,f'Plantain or cooking banana, {g}, listed in Wikipedia\'s list of banana cultivars.',B)
# mango
M=WP+'List_of_mango_cultivars'
add('Mango','Neelam','Mango cultivar grown in India and Pakistan.',M)
add('Mango','Hoà Lộc','Vietnamese mango listed as Hoà Lộc Sand mango.',M)
add('Mango','Turpentine','Mango used in Florida as a rootstock for grafting other mangoes.',M)
# watermelon
W2=WP+'Watermelon'
add('Watermelon','Carolina Cross','Watermelon cultivar that produced the heaviest watermelon on record, 159 kg.',W2)
add('Watermelon','Orangeglo','Large oblong watermelon with very sweet orange flesh.',W2)
for n in ['Tom Watson','Georgia Rattlesnake','Black Diamond']:
    add('Watermelon',n,'Old watermelon cultivar favoured for pickling.',W2)
# potato
PO=WP+'List_of_potato_cultivars'
add('Potato','Ajanhuiri','Andean potato cultivar from Bolivia.',PO)
add('Potato','Imilla','Andean potato cultivar from Bolivia.',PO)
# cucumber, pea, corn, beet, chard, lettuce
add('Cucumber','Lemon cucumber','Round pale yellow cucumber cultivar.',WP+'Cucumber')
PE=WP+'Pea'
add('Pea','Little Marvel','Pea cultivar, 63 days, 1934 AAS winner.',PE,y='1934')
add('Pea','Wando','Pea cultivar, 68 days.',PE)
add('Pea','Tom Thumb','Extra-dwarf heirloom pea, also Half Pint, 55 days.',PE,a='Half Pint')
add('Pea','Thomas Laxton','Heirloom pea also called Laxton\'s Progress or Progress No. 9, 60-65 days.',PE,a="Laxton's Progress")
add('Pea','Tall Telephone','Tall heirloom climbing pea also called Alderman, 75 days.',PE,a='Alderman')
add('Pea','Kelvedon Wonder','Pea cultivar, 65 days, RHS Award of Garden Merit 1997.',PE,y='1997')
SC=WP+'Sweet_corn'
add('Sweetcorn','Country Gentleman','Open-pollinated white shoepeg sweet corn with small kernels in irregular rows.',SC)
add('Sweetcorn','Illini Xtra Sweet','Supersweet corn released by Illinois Foundation Seeds.',SC)
BE=WP+'Beetroot'
add('Beetroot',"Burpee's Golden",'Heirloom beetroot with a yellow root, also called Golden Beet.',BE,a='Golden Beet')
add('Beetroot','Touchstone Gold','Yellow-rooted beetroot cultivar.',BE)
add('Beetroot','Albino','White-rooted heirloom beetroot.',BE)
CH=WP+'Swiss_chard'
add('Chard','Lucullus','Green chard cultivar.',CH); add('Chard','Fordhook Giant','Green chard cultivar.',CH)
add('Chard','Ruby Chard','Red-ribbed chard cultivar.',CH); add('Chard','Rhubarb Chard','Red-ribbed chard cultivar.',CH)
LE=WP+'Lettuce'
add('Lettuce','Forellenschluss','Austrian speckled romaine lettuce.',LE)
add('Lettuce','Prajzerica','Lettuce variety from Croatia.',LE)
CA=WP+'Cauliflower'
for n,t in [('Cheddar','orange'),('Orange Bouquet','orange'),('Alverda','green'),('Green Goddess','green'),('Vorda','green'),('Graffiti','purple'),('Purple Cape','purple')]:
    add('Cauliflower',n,f'Cauliflower cultivar with {t} heads.',CA)
add('Kale','Jersey kale','Extra-tall kale variety also called cow cabbage.',WP+'Kale',a='Cow cabbage')
BA=WP+'Basil'
add('Basil','Dark Opal','Purple basil cultivar.',BA); add('Basil','Purple Ruffles','Purple basil cultivar.',BA); add('Basil','Purple Delight','Purple basil cultivar.',BA)
add('Basil','Lemon basil','Hybrid of sweet basil and American basil.',BA)
add('Basil','Purple basil','Purple-leaved sweet basil cultivar, Ocimum basilicum Purpurescens.',BA,a='Purpurescens')
KI=WP+'Kiwifruit'
for n,dd in [('Blake','Self-pollinating kiwifruit with smaller oval fruit.'),('Donghong','Red-fleshed kiwifruit cultivar, also called Oriental Red.'),('Jinyan','Yellow-fleshed kiwifruit cultivar.'),('Soreli','Yellow-fleshed kiwifruit cultivar developed in Italy.'),('Saanichton 12','Kiwifruit cultivar from British Columbia.'),('EnzaRed','Red kiwifruit cultivar descended from Hongyang.')]:
    add('Kiwifruit',n,dd,KI)
PI=WP+'Pineapple'
add('Pineapple','Kona Sugarloaf','White-fleshed pineapple of 2.5-3 kg with no woody centre.',PI)
add('Pineapple','Pernambuco','Pale-fleshed pineapple of 1-2 kg, also called Eleuthera.',PI,a='Eleuthera')
# Protected-origin names from the Indian GI register (Wikipedia list)
IN=WP+'List_of_geographical_indications_in_India'
gi=[('Grape','Table grape','Bangalore Blue Grapes GI','2012','Karnataka'),('Table grape','Table grape','Nashik Grapes GI','2010','Maharashtra'),
('Chilli','Chilli','Guntur Sannam Chilli GI','2010','Andhra Pradesh'),('Chilli','Chilli','Byadagi chilli GI','2010','Karnataka'),('Chilli','Chilli','Mizo Chilli GI','2014','Mizoram'),('Chilli','Chilli','Nandurbar Mirchi GI','2023','Maharashtra'),
('Peach','Peach','Ramgarh Nainital Aadu GI','2023','Uttarakhand'),('Apricot','Apricot','Ladakh Raktsey Karpo Apricot GI','2022','Ladakh'),('Sea buckthorn','Sea buckthorn','Ladakh Seabuckthorn GI','2023','Ladakh'),
('Orange','Orange','Jalna Sweet Orange GI','2016','Maharashtra'),('Mandarin','Mandarin','Khasi Mandarin GI','2014','Meghalaya'),('Lemon','Lemon','Kachai Lemon GI','2014','Manipur'),
('Pomelo','Pomelo','Devanahalli Pomello GI','2009','Karnataka'),('Lime','Lime','Indi Limbe GI','2022','Karnataka'),
('Litchi','Litchi','Shahi Litchi of Bihar GI','2018','Bihar'),('Litchi','Litchi','Tezpur Litchi GI','2014','Assam'),('Litchi','Litchi','Ramnagar Nainital Litchi GI','2023','Uttarakhand'),
('Pineapple','Pineapple','Vazhakulam pineapple GI','2009','Kerala'),('Pineapple','Pineapple','Tripura Queen Pineapple GI','2014','Tripura'),
('Jamun','Jamun','Bahadoli Jamun GI','2023','Maharashtra'),('Jamun','Jamun','Badlapur Jamun GI','2023','Maharashtra'),('Amla','Amla','Pratapgarh Aonla GI','2022','Uttar Pradesh'),('Karonda','Karonda','Chiraigaon Karonda of Varanasi GI','2023','Uttar Pradesh'),
('Cherimoya','Cherimoya','Beed Custard Apple GI','2016','Maharashtra'),('Tamarillo','Tamarillo','Naga Tree Tomato GI','2014','Nagaland'),('Guava','Guava','Allahabad Surkha guava GI','2007','Uttar Pradesh'),
('Sapodilla','Sapodilla','Dahanu Gholvad Chikoo GI','2016','Maharashtra'),('Fig','Fig','Purandar Fig GI','2016','Maharashtra'),('Date','Date','Kachchhi Kharek GI','2023','Gujarat'),('Pomegranate','Pomegranate','Solapur Pomegranate GI','2016','Maharashtra'),
('Ginger','Ginger','Assam Karbi Anglong Ginger GI','2014','Assam'),('Ginger','Ginger','Mizo Ginger GI','2021','Mizoram'),
('Garlic','Garlic','Kodaikanal Malai Poondu GI','2019','Tamil Nadu'),('Garlic','Garlic','Kanthalloor Vattavada Veluthulli GI','2022','Kerala'),('Garlic','Garlic','Ratlam Riyawan Lahsun GI','2023','Madhya Pradesh'),
('Bulb onion','Bulb onion','Lasalgaon Onion GI','2015','Maharashtra'),('Bulb onion','Bulb onion','Alibag White Onion GI','2022','Maharashtra'),('Bulb onion','Bulb onion','Bangalore Rose Onion GI','2014','Karnataka'),
('Aubergine','Aubergine','Jalgaon Bharit Brinjal GI','2016','Maharashtra'),('Aubergine','Aubergine','Vellore Spiny Brinjal GI','2022','Tamil Nadu'),('Aubergine','Aubergine','Udupi Mattu Gulla Brinjal GI','2011','Karnataka'),('Aubergine','Aubergine','Ramnagar Bhanta (Brinjal) GI','2022','Uttar Pradesh'),('Aubergine','Aubergine','Agsechi Vayingim (Agassaim Brinjal) GI','2023','Goa'),
('Cucumber','Cucumber','Naga Cucumber GI','2021','Nagaland')]
for _,kind,n,y,st in gi:
    add(kind,n,f'Indian geographical indication from {st}, registered in {y}-{int(y[2:])+1:02d}.',IN,y=y)
# Japan / Vietnam
EJ='https://agriculture.ec.europa.eu/system/files/2023-09/list-additional-42-gi-registered-epa_en.pdf'
add('Lotus root','大口れんこん GI','Japanese geographical indication for lotus root (Okuchi Renkon), added to the EU-Japan protected list in September 2023.',EJ,a='Okuchi Renkon',y='2023')
add('Ume','氷見稲積梅 GI','Japanese geographical indication for ume (Himi Inazumiume), added to the EU-Japan protected list in September 2023.',EJ,a='Himi Inazumiume',y='2023')
add('Dragon fruit','Bình Thuận GI','Dragon fruit from Bình Thuận province, Vietnam, granted a Japanese geographical indication by the agriculture ministry.','https://vietnamnews.vn/economy/1055907/geographical-indication-of-binh-thuan-dragon-fruit-protected-in-japan.html')
# coverage lines and sections
refs={'Tomato':"Complete: %d of %d in Wikipedia's List of tomato cultivars (table rows and sidebar names, read to the end, 2026-10-31).",
'Chilli':"Complete: %d of %d in Wikipedia's List of Capsicum cultivars (cultivar lists by species and index, read to the end, 2026-10-31)."}
nol="No complete list exists; follows the cultivars named by the pages cited on each entry%s."
for kn,k in K.items():
    x=k.get('x',[])
    if not x: continue
    if kn in refs:
        c=refs[kn]%(len(x),len(x))
    else:
        c=nol%''
        if kn in('Apple','Pear','Strawberry','Banana','Mango','Persimmon','Potato','Sweet potato','Peach','Watermelon','Kiwifruit','Pineapple','Plantain','Asian pear','Orange','Mandarin'):
            c=f"Covers {len(x)} of an open number of cultivars in Wikipedia's cultivar lists for this fruit or vegetable, read in windows to the end of the readable text; the rest have no article or no fetched page, so no total exists."
    sel=k.get('sel','')
    sel=re.sub(r'Not claimed complete\. ?','',sel).strip()
    k['sel']=(sel+' '+c).strip()
    if len(x)>12:
        k['xg']='by protected origin or cultivar'
        for e in x:
            e['g']='Protected origin' if re.search(r'\b(PDO|PGI|GI|AOP|DO|IG)\b',e['n']) else 'Cultivar'
json.dump(d,open(W+'J4.tmp','w'),ensure_ascii=False,indent=1)
os.replace(W+'J4.tmp',R+'J4.json')
json.dump({k:v for k,v in added.items()},open(W+'added.json','w'),ensure_ascii=False,indent=1)
print({k:len(v) for k,v in added.items()}, sum(len(v) for v in added.values()))
