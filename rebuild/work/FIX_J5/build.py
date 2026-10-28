import json,os,sys,copy
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'J5.json')); br=json.load(open(R+'J5_brands.json')); mv=json.load(open(R+'J5_moves.json'))
W='https://en.wikipedia.org/wiki/'
def A(n,dd,s,mk='',y='',v=None,dt='',a=''):
    return {"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
def kind(n,dd,s,x=None,t=None,m=None,r=None,a='',tg=None):
    k={"n":n,"a":a,"d":dd,"s":s}
    if t:k['t']=t
    if tg:k['tg']=tg
    if x:k['x']=x
    k['m']=m or []
    if r:k['r']=r
    return k
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return s,i,k
    raise KeyError(n)
def remove(n):
    s,i,k=find(n); s['k'].pop(i); return k
def shelf(dn,sn):
    for dp in d['depts']:
        if dp['n']==dn:
            for s in dp['s']:
                if s['n']==sn: return s
    raise KeyError(sn)
def addx(kn,arch,pos=None):
    k=find(kn)[2]; k.setdefault('x',[])
    if pos is None: k['x'].append(arch)
    else: k['x'].insert(pos,arch)
counts=lambda: (sum(len(s['k']) for dp in d['depts'] for s in dp['s']), sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k']))
before=counts()

# ---- J5-1 olive producers
s=shelf('Oils, vinegars & fats','Olive oil')
s['k'].append(kind('Estate olive oils','Extra virgin oils sold under a producer or estate name and judged in competitions, not under a protected origin.',
 W+'New_York_International_Olive_Oil_Competition',
 t=['early harvest','single variety','organic / biodynamic','competition award'],
 x=[
 A('Castillo de Canena','Jaén family estate that launched a premium extra virgin brand in 2003 from olive-growing dating to 1780.','https://www.origenoliva.com/en/blogs/noticias-aceite-de-oliva/dentro-de-cada-casa-castillo-de-canena','Castillo de Canena','2003',
   [V('Family Reserve','Castillo de Canena','','Yearly Arbequina and Picual selection'),V('First Day of Harvest','Castillo de Canena','','Limited early-harvest edition, artist labels'),V('Biodynamic Organic','Castillo de Canena','','Demeter-certified Picual and Arbequina'),V('Primero Royal Early Harvest','Castillo de Canena','','From the Royal variety'),V('Arbequina Amontillado','Castillo de Canena','','Aged in sherry casks')],'Picual · Arbequina · Royal · Jaén'),
 A('Laudemio','Tuscan oil brand created by the Frescobaldi family in 1986 after the 1985 frost; first harvest 1989.','https://taste.pittimmagine.com/en/exhibitors/F/laudemio-frescobaldi','Laudemio Frescobaldi','1986',[],'early-picked Tuscan olives · Castello Nipozzano mill',a='Laudemio Frescobaldi'),
 A('Cobram Estate','Australian producer (formerly Boundary Bend) that expanded into California in 2014–15 and wins NYIOOC medals.','https://news.nyiooc.org/release/cobram-estate-wins-silver-at-2026-nyiooc-for-everyday-essentials-classic','Cobram Estate','',
   [V('California Select','Cobram Estate','','Gold, 2026 NYIOOC'),V('Mission','Cobram Estate','','Silver, 2026 NYIOOC'),V('Picual','Cobram Estate','','Silver, 2026 NYIOOC'),V('Coratina','Cobram Estate','','Silver, 2026 NYIOOC')],'Australia and California'),
 A('California Olive Ranch','Californian producer founded in 1998 making extra virgin oil from Arbequina, Arbosana and Koroneiki.','https://lifeandthyme.com/food/profiles/california-olive-ranch','California Olive Ranch','1998',[],'Arbequina · Arbosana · Koroneiki'),
 ]))
d['b'].append({"m":"Olive oil competition award","v":"NYIOOC Gold > Silver > none","w":"The New York International Olive Oil Competition, founded 2013, judges entries from producers worldwide."})

# ---- J5-2 pasta
PL=W+'List_of_pasta'
addx('Short and twisted pasta',A('Trofie','Thin twisted durum-and-water pasta from Liguria.',PL))
addx('Short and twisted pasta',A('Strozzapreti','Strips rolled across their width, from Tuscany and Emilia-Romagna.',PL))
addx('Short and twisted pasta',A('Cavatelli','Short solid hand-shaped pieces from southern Italy and Sicily, sold in three sizes.',PL))
addx('Tube pasta',A('Garganelli','Square egg pasta rolled into a tube, from Emilia-Romagna.',PL))
addx('Tube pasta',A('Calamarata','Wide ring-shaped pasta from Naples.',PL))
addx('Egg pasta, ribbons and nests',A('Mafaldine','Short ribbons with ruffled sides.',PL))
addx('Filled pasta',A('Cannelloni','Sheets wrapped round a filling to form tubes, usually baked in sauce; the name means large reeds.',W+'Cannelloni',dt='spinach and ricotta · meat'))
s=shelf('Rice, pasta & noodles','Pasta')
i=[k['n'] for k in s['k']].index('Filled pasta')
s['k'].insert(i,kind('Sheet pasta','Flat square or rectangular pasta sheets layered and baked, sold dried or fresh.',W+'Lasagne',
 t=['dried durum','fresh egg','no pre-cook','ruffled edge','long narrow sheet'],
 x=[A('Lasagne','Wide flat sheets of pasta layered with fillings and baked; first written reference dates to 1282.',W+'Lasagne',dt='dried durum semolina · fresh egg sfoglia',v=[],a='lasagna'),
    A('Lasagna riccia','Mass-produced sheets with ruffled edges, also called doppio festone.',W+'Lasagne'),
    A('Lasagna a nastro','Long narrow modern baking sheets.',W+'Lasagne')]))
# makers as models on kinds
k=find('Long-strand pasta')[2]
k['m'].append(['Gragnano IGP spaghetti','Pastificio Faella'])
find('Tube pasta')[2]['m'].append(['Monograno Felicetti pasta','Felicetti'])
find('Egg pasta, ribbons and nests')[2]['m'].append(['Rustichella d\'Abruzzo bronze-die pasta',"Rustichella d'Abruzzo"])

# ---- J5-3/5 beans & merges
rem=[remove(n) for n in ['Black beans','Pinto beans','Small red beans','Black-eyed peas','Dried broad beans','Dried soybeans','Adzuki beans']]
CB=W+'Common_bean'
sh=shelf('Grains, pulses & seeds','Dried beans')
sh['k'].insert(0,kind('Dried beans','Dried seeds of common, runner and other beans, sold by market class or as heirloom and protected varieties.',CB,
 a='haricot types · heirloom beans',
 t=['black (turtle)','pinto','small red','black-eyed pea','broad (fava)','soybean','adzuki'],
 x=[A('Tarbais bean','White Phaseolus vulgaris from the Hautes-Pyrénées; Label Rouge 1997, PGI 2000.',W+'Tarbais_bean','', '2000',dt='PGI · south-west France'),
    A('Judiones de la Granja','Large white runner beans from La Granja, Spain.',W+'Runner_bean',dt='runner bean'),
    A('Anasazi bean','Dappled red-and-white beans first grown by Ancestral Puebloan people; sold commercially from the 1980s.',CB),
    A("Jacob's Cattle",'Speckled heirloom bean like Anasazi but with dots; also called Trout.',CB,a='Trout bean'),
    A('Appaloosa bean','Ivory at one end and speckled reddish-purple and mocha at the other.',CB),
    A("Tiger's eye bean",'Bush bean thought to come from Chile or Argentina.',CB),
    A('Cranberry bean','Speckled bean from Colombia (cargamanto); the borlotti is a thick-skinned Italian relative.',CB,a='borlotti'),
    A('Marcella bean','Heirloom bean named in 2015 by Rancho Gordo for the cookbook author Marcella Hazan.',W+'Rancho_Gordo','Rancho Gordo','2015')]))
# lentils shelf
rem2=[remove(n) for n in ['Split peas','Mung beans','Black gram','Pigeon peas','Horse gram']]
sl=shelf('Grains, pulses & seeds','Lentils, peas & dals')
sl['k'].append(kind('Split pulses and dals','Husked split peas and small pulses cooked as dal or soup.',rem2[0]['s'],
 t=['split peas','mung (moong)','black gram (urad)','pigeon pea (toor)','horse gram (kulthi)']))
# flours
rem3=[remove(n) for n in ['Chickpea flour','Maize flour','Buckwheat flour','Millet flour','Urad and moong flour']]
sf=shelf('Flour, sugar & baking','Other flours & starches')
sf['k'].insert(0,kind('Pulse and grain flours','Single-pulse and single-grain flours for batters, flatbreads and gluten-free baking.',rem3[0]['s'],
 t=['chickpea (besan)','maize','buckwheat','millet','urad and moong']))
# icing sugar
rem4=remove('Icing sugar'); ks=find('White sugar')[2]; ks['t']=(ks.get('t') or [])+['granulated','caster','icing']
# vinegar
rem5=remove('Distilled vinegar'); kv=find('Malt vinegar')[2]
kv['n']='Malt and distilled vinegar'; kv['a']=(kv.get('a','')+' · ' if kv.get('a') else '')+'malt vinegar · white vinegar · spirit vinegar'
kv['d']='Brown malt vinegar for chips and pickling, and clear distilled (white) vinegar for cleaning and pickles.'
kv['t']=(kv.get('t') or [])+['malt (brown)','distilled (white)']
# konjac
rem6=remove('Konjac noodles'); kg=find('Glass noodles')[2]; kg['t']=(kg.get('t') or [])+['konjac (shirataki)']
# syrup (J5-7)
remove('Flavoured syrup')

# ---- J5-4 hot sauce
HS='Hot sauce'
addx(HS,A('Secret Aardvark','Portland, Oregon habanero sauce; Secret Aardvark Trading Co. was founded in 2004 by Scott Moritz.','https://secretaardvark.com/about/','Secret Aardvark','2004',dt='habanero · tomato'))
addx(HS,A("Melinda's",'Habanero sauces started in New Orleans in 1989 by the Figueroa brothers; now made in Dallas.','https://www.foxnews.com/world/brothers-bringing-habanero-sauces-to-u-s-since-1989-ready-to-turn-up-the-heat.amp',"Melinda's",'1989',dt='habanero · carrot · garlic'))
addx(HS,A('Yellowbird','Austin, Texas craft sauce brand started by Erin and George as a farmers market product.','https://thedieline.com/yellowbird/','Yellowbird','',dt='fresh chilli · everyday heat'))

# ---- J5-6 new department
sD='https://en.wikipedia.org/wiki/'
dept={"n":"Prepared & frozen foods","mode":"mixed","note":"Packaged ready-to-heat foods bought as products, organised by product type and brand; restaurant and home dishes belong to the Culinary taxonomy.","s":[]}
def sh_(n,k): dept['s'].append({"n":n,"k":k})
sh_('Frozen ready meals',[
 kind('Frozen ready meals','Single-serve or family meals sold frozen and heated before eating, also called TV dinners or microwave meals.',W+'Ready_meal',
  t=['single-serve tray','family size','vegetarian / vegan','reduced-calorie'],
  x=[A('TV dinner','Frozen compartment-tray meal; Swanson sold its turkey TV Dinner in 1953 for 98 cents.',W+'TV_dinner','Swanson','1953',
       [V('Swanson desserts tray','Swanson','1960','Four-compartment tray'),V('Hungry-Man','Swanson','1973','Larger portions'),V('Microwave-safe tray','Campbell\'s','1986','Introduced by Campbell Soup')],'compartment tray · turkey original',a='Swanson TV Dinner'),
     A("Stouffer's lasagna",'Frozen lasagna from the Stouffer\'s line, with macaroni and cheese and meatloaf among its staples.',W+'Stouffer%27s',"Stouffer's",'',dt='lasagna · macaroni and cheese · meatloaf'),
     A('Lean Cuisine','Lower-fat frozen meals launched in 1981 as an alternative to Stouffer\'s; vegan meals added in 2018.',W+'Lean_Cuisine','Lean Cuisine','1981',dt='reduced-calorie single-serve'),
     A("Amy's vegetable pot pie","Amy's Kitchen's first product, an organic vegetable pot pie.",W+"Amy%27s_Kitchen","Amy's Kitchen",'1987',dt='organic · vegetarian'),
     A("Marie Callender's frozen entrées","Frozen and shelf-stable entrées and sides sold under a restaurant name licensed to ConAgra from 1994.",W+'Marie_Callender%27s',"Marie Callender's",'1994',dt='pot pies · entrées')],
  r=[['Frozen meals','Banquet'],['Ready meals','Aunt Bessie\'s'],['Ready meals','Findus'],['Ready meals','Birds Eye']]),
 kind('Frozen Yorkshire puddings and accompaniments','Frozen side items such as Yorkshire puddings, roast potatoes and vegetables sold to go with a meal.',W+'Aunt_Bessie%27s',
  x=[A('Aunt Bessie\'s Yorkshire puddings','The line that launched Aunt Bessie\'s in 1995, made at first by Tryton Foods.',W+'Aunt_Bessie%27s',"Aunt Bessie's",'1995')]),
 kind('Frozen crispy pancakes and coated savouries','Breadcrumb-coated frozen pancakes and similar snacks.',W+'Findus',
  x=[A('Crispy Pancakes','Findus breadcrumb-coated filled pancakes; Wikipedia gives conflicting dates (1958 or early 1970s).',W+'Findus','Findus')]),
])
sh_('Frozen pizza',[
 kind('Frozen pizza','Mass-manufactured pizza frozen before sale and baked at home.',W+'Frozen_pizza',
  t=['thin crust','rising crust','deep pan','stone-baked'],
  x=[A('Totino\'s frozen pizza','First national-scale US frozen pizza, mass-manufactured from 1962 and bought by Pillsbury in 1975.',W+'Totino%27s',"Totino's",'1962'),
     A('Tombstone','US frozen pizza brand founded in 1966 and sold to Kraft in 1984.',W+'Frozen_pizza','Tombstone','1966'),
     A('Red Baron','Frozen pizza imprint of Schwan\'s, launched in 1976.',W+'Frozen_pizza','Red Baron','1976'),
     A('DiGiorno','First brand with a self-rising crust, launched by Kraft in the mid-1990s; owned by Nestlé since 2010.',W+'DiGiorno','DiGiorno','1995',dt='rising crust'),
     A('Freschetta','Schwan\'s self-rising crust pizza introduced after DiGiorno.',W+'Freschetta','Freschetta','',dt='rising crust'),
     A('Mama Celeste','Chicago pizza line begun in 1962, sold to Quaker Oats in 1969 and discontinued by Conagra in 2026.',W+'Mama_Celeste','Mama Celeste','1962')],
  m=[['Chicago Town pizza','Dr. Oetker'],['Ristorante pizza','Dr. Oetker'],['Goodfella\'s pizza','Goodfella\'s']]),
 kind('Pizza rolls','Small crisp-fried or baked rolls filled with pizza toppings, sold frozen as snacks.',W+'Totino%27s',
  x=[A("Totino's Pizza Rolls",'Totino\'s best-known frozen snack.',W+'Totino%27s',"Totino's")]),
])
sh_('Frozen potato products',[
 kind('Frozen chips and fries','Pre-cut, blanched and frozen potato sticks finished in the oven, air fryer or fryer.',W+'French_fries',
  t=['straight cut','crinkle cut','skinny','wedges','oven chips'],
  r=[['Frozen fries','McCain'],['Potato products',"Aunt Bessie's"],['Potato waffles','Birds Eye'],['Frozen fries','Ore-Ida']]),
 kind('Tater tots and hash browns','Frozen shaped potato products: grated-potato nuggets and shredded hash brown patties.',W+'Hash_browns',
  x=[A('Tater Tots','Grated-potato nuggets developed in 1953 from leftover slivers and sold from 1956; a registered Ore-Ida trademark.',W+'Tater_tots','Ore-Ida','1953'),
     A('Frozen hash browns','Shredded potato sold frozen as loose shreds or shaped patties for toasters and ovens.',W+'Hash_browns')]),
])
sh_('Frozen dumplings & dim sum',[
 kind('Frozen dumplings','Filled dough parcels sold frozen to be boiled, steamed or pan-fried at home.',W+'Jiaozi',
  t=['pork','vegetable','chicken','pan-fry','steam-in-bag'],
  x=[A('Gyoza','Japanese pan-fried dumpling descended from jiaozi, sold frozen or ready to eat.',W+'Gyoza',
       v=[V('Ajinomoto frozen gyoza','Ajinomoto','','Ajinomoto entered frozen foods in 1972')],a='potsticker'),
     A('Jiaozi','Chinese dumpling of ground meat or vegetables in thin dough; store-bought frozen versions are boiled then fried.',W+'Jiaozi'),
     A('Pierogi','Unleavened-dough dumplings filled with potato, cheese, sauerkraut, meat or fruit; frozen in US supermarkets by the 1960s.',W+'Pierogi',
       v=[V("Mrs. T's Pierogies","Mrs. T's",'1952','Largest US pierogi maker, Shenandoah, Pennsylvania')]),
     A('Dim sum','Small Cantonese dishes, including dumplings, shumai and pork buns, sold frozen in grocery stores.',W+'Dim_sum')]),
])
sh_('Chilled dips & spreads',[
 kind('Hummus','Chickpea dip with tahini, lemon juice and garlic, sold chilled.',W+'Hummus',t=['classic','flavoured','houmous (UK)'],
  m=[['Sabra hummus','Sabra'],['Meadow Fresh houmous','Lidl']]),
 kind('Tzatziki','Cold dip of strained yogurt with cucumber, garlic and olive oil.',W+'Tzatziki',a='cacık · tarator'),
 kind('Guacamole','Avocado dip sold chilled, frozen or high-pressure pasteurised.',W+'Guacamole',t=['chilled','frozen','high-pressure processed']),
 kind('Taramasalata','Greek and Turkish spread of salted cured fish roe with oil, lemon and bread or potato.',W+'Taramasalata',t=['smooth (commercial)','traditional grainy']),
])
sh_('Baby food',[
 kind('Baby purées and pouches','Smooth fruit, vegetable and meat purées for weaning, sold in jars, pouches or frozen.',W+'Baby_food',tg=['baby'],
  t=['jar','pouch','organic','frozen'],
  x=[A('Gerber baby food','Jarred baby food from Daniel Gerber\'s Fremont Canning Company; Gerber held about 70% of the US market in 1996.',W+'Gerber_Products_Company','Gerber','1927',tg=None) if False else A('Gerber baby food','Jarred baby food from Daniel Gerber\'s Fremont Canning Company; about 70% of the US market in 1996.',W+'Gerber_Products_Company','Gerber','1927'),
     A("Clapp's baby food","Harold Clapp's US baby food, sold from the 1920s.",W+'Baby_food',"Clapp's",'1920s'),
     A('Beech-Nut baby food','Beech-Nut entered the US baby food market in 1931; owned by Hero since 2005.',W+'Beech-Nut','Beech-Nut','1931'),
     A('Heinz baby food','Heinz sold ready-to-serve soups and baby food through the 1930 Depression and later made dehydrated baby food.',W+'Heinz','Heinz','1930'),
     A("Earth's Best",'The first organic baby food brand, launched in 1987 and owned by Hain Celestial since 1999.',W+'Earth%27s_Best',"Earth's Best",'1987',dt='organic'),
     A("Ella's Kitchen",'British organic baby food brand founded in 2004; the first to bring pouches to the baby food market.',W+'Ella%27s_Kitchen',"Ella's Kitchen",'2004',dt='pouch')]),
 kind('Infant cereals','Iron-fortified baby cereals, usually the first commercial food given to babies in developed countries.',W+'Baby_food',tg=['baby'],
  x=[A('Pablum','Pablum was the first precooked dried baby food, made in the 1930s for sick children.',W+'Baby_food','', '1930s')],
  m=[['Infant cereal','Cow & Gate']]),
 kind('Toddler meals and snacks','Foods for children from about 12 months: small microwaveable meals, cereals, baked goods and drinks.',W+'Baby_food',tg=['baby']),
])
sh_('Chilled & instant soups',[
 kind('Dried and instant soup','Packet and cup soups made from dried ingredients, marketed for home use since the mid-20th century.',W+'Soup',
  m=[['Dried soup','Knorr'],['Dried soup','Heinz']]),
])
d['depts'].append(dept)

# ---- brands
def B(n,c,f,seg,kf,dd,s,lines=None): 
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"s":s,**({"lines":lines} if lines else {})}
have={b['n'].lower() for b in br['b']}
new=[
 B('Swanson','United States','1953','Mainstream','TV dinners','Brand whose 1953 turkey TV Dinner popularised the frozen meal.',W+'TV_dinner',['Hungry-Man']),
 B("Stouffer's",'United States','1922','Mainstream','frozen lasagna','Cleveland brand bought by Nestlé in 1973.',W+'Stouffer%27s'),
 B('Lean Cuisine','United States','1981','Mainstream','diet meals','Nestlé line of lower-fat frozen meals.',W+'Lean_Cuisine'),
 B("Marie Callender's",'United States','1948','Mainstream','pot pies','Restaurant name licensed for frozen entrées and sides.',W+'Marie_Callender%27s'),
 B("Amy's Kitchen",'United States','1987','Premium','organic frozen','Petaluma maker of organic and non-GMO frozen foods.',W+"Amy%27s_Kitchen"),
 B("Totino's",'United States','1951','Mainstream','pizza rolls','Minneapolis pizza maker owned by General Mills.',W+'Totino%27s'),
 B('DiGiorno','United States','1991','Mainstream','rising crust','Nestlé frozen pizza brand with self-rising crust.',W+'DiGiorno'),
 B('Tombstone','United States','1966','Mainstream','frozen pizza','US frozen pizza brand sold to Kraft in 1984.',W+'Frozen_pizza'),
 B('Red Baron','United States','1976','Mainstream','frozen pizza','Schwan\'s frozen pizza imprint.',W+'Frozen_pizza'),
 B('Freschetta','United States','','Mainstream','rising crust','Schwan\'s self-rising crust pizza.',W+'Freschetta'),
 B('Mama Celeste','United States','1962','Mainstream','frozen pizza','Chicago pizza line discontinued by Conagra in 2026.',W+'Mama_Celeste'),
 B('Dr. Oetker','Germany','1891','Mainstream','baking and pizza','Bielefeld firm selling Chicago Town and Ristorante pizza in the UK.',W+'Dr._Oetker',['Chicago Town','Ristorante']),
 B("Goodfella's",'Ireland','','Mainstream','frozen pizza','Irish-founded frozen pizza brand owned by Nomad Foods.',W+'Nomad_Foods'),
 B('McCain','Canada','1957','Mainstream','frozen chips','Florenceville, New Brunswick maker of frozen fries and oven meals.',W+'McCain_Foods'),
 B('Ore-Ida','United States','1952','Mainstream','Tater Tots','Pittsburgh potato brand owned by Kraft Heinz.',W+'Ore-Ida'),
 B("Aunt Bessie's",'United Kingdom','1995','Mainstream','Yorkshire puddings','UK frozen accompaniments brand owned by Nomad Foods.',W+'Aunt_Bessie%27s'),
 B('Birds Eye','United States','1922','Mainstream','fish fingers','Frozen food brand founded by Clarence Birdseye.',W+'Birds_Eye'),
 B('Findus','Sweden','1945','Mainstream','frozen fish','Swedish frozen food brand owned by Nomad Foods in much of Europe.',W+'Findus'),
 B('Sabra','United States','','Mainstream','hummus','Leading US hummus maker (62% share in 2016).',W+'Hummus'),
 B("Mrs. T's",'United States','1952','Mainstream','pierogi','Shenandoah, Pennsylvania frozen pierogi brand of Ateeco.',W+'Mrs._T%27s_Pierogies'),
 B('Ajinomoto','Japan','1917','Mainstream','frozen gyoza','Tokyo food group in frozen foods since 1972.',W+'Ajinomoto'),
 B('Gerber','United States','1927','Mainstream','baby food','Michigan baby food maker owned by Nestlé since 2007.',W+'Gerber_Products_Company'),
 B('Beech-Nut','United States','1891','Mainstream','baby food','New York baby food company owned by Hero since 2005.',W+'Beech-Nut'),
 B("Earth's Best",'United States','1987','Premium','organic baby food','First organic baby food brand.',W+'Earth%27s_Best'),
 B("Ella's Kitchen",'United Kingdom','2004','Premium','baby pouches','Organic baby food brand owned by Hain Celestial.',W+'Ella%27s_Kitchen'),
 B('Cow & Gate','United Kingdom','1882','Mainstream','baby foods','Guildford dairy that became a baby food brand owned by Danone.',W+'Cow_%26_Gate'),
 B("Clapp's",'United States','','Heritage manufactory','early baby food','Harold Clapp\'s baby food of the 1920s.',W+'Baby_food'),
 B("Rustichella d'Abruzzo",'Italy','1924','Artisan & independent','bronze-die pasta','Penne, Abruzzo pasta maker, relaunched in 1981.','https://taste.pittimmagine.com/18/exhibitors/R/rustichella-d-abruzzo'),
 B('Felicetti','Italy','','Premium','Monograno pasta','Predazzo pasta maker; Monograno single-grain line from 2004.','https://www.linkiesta.it/2021/06/pasta-felicetti-monograno/'),
 B('Secret Aardvark','United States','2004','Artisan & independent','habanero sauce','Portland, Oregon hot sauce company.','https://secretaardvark.com/about/'),
 B("Melinda's",'United States','1989','Mainstream','habanero sauce','New Orleans-founded hot sauce maker, now in Dallas.','https://www.foxnews.com/world/brothers-bringing-habanero-sauces-to-u-s-since-1989-ready-to-turn-up-the-heat.amp'),
 B('Yellowbird','United States','','Artisan & independent','craft hot sauce','Austin, Texas hot sauce brand.','https://thedieline.com/yellowbird/'),
 B('Castillo de Canena','Spain','2003','Premium','Jaén EVOO','Vañó family premium extra virgin oil brand, family olive growers since 1780.','https://www.origenoliva.com/en/blogs/noticias-aceite-de-oliva/dentro-de-cada-casa-castillo-de-canena'),
 B('Laudemio Frescobaldi','Italy','1986','Premium','Tuscan EVOO','Frescobaldi olive oil brand created after the 1985 frost.','https://taste.pittimmagine.com/en/exhibitors/F/laudemio-frescobaldi'),
 B('Cobram Estate','Australia','','Premium','NYIOOC winner','Australian olive oil producer, formerly Boundary Bend, also in California.','https://news.nyiooc.org/release/cobram-estate-wins-silver-at-2026-nyiooc-for-everyday-essentials-classic'),
 B('California Olive Ranch','United States','1998','Premium','Californian EVOO','Californian extra virgin oil producer.','https://lifeandthyme.com/food/profiles/california-olive-ranch'),
]
for b in new:
    if b['n'].lower() not in have: br['b'].append(b)
# archetype mk with names not in register: fix
reg={b['n'] for b in br['b']}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for x in k.get('x',[]):
                if x.get('mk') and x['mk'] not in reg: print('MK missing',x['mk'],x['n'])
# moves
pass
print('before',before,'after',counts())
if '--write' in sys.argv:
    for f,o in (('J5.json',d),('J5_brands.json',br),('J5_moves.json',mv)):
        json.dump(o,open(R+f+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+f+'.tmp',R+f)
