import json,copy
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/J6.json'))
ren={}
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
    raise KeyError(n)
def shelf(dn,sn):
    for dp in d['depts']:
        if dp['n']==dn:
            for s in dp['s']:
                if s['n']==sn: return s
    raise KeyError(sn)

d['ax']="Which drink is it for: coffee, tea, a herbal or grain infusion, or cocoa?"
d['key']=["1. Is it the seed of the coffee plant, green, roasted or made into capsules, instant or concentrate? → Coffee",
"2. Is it the leaf of the tea plant (black, green, oolong, white, yellow, dark), blended, flavoured or scented? → Tea",
"3. Is it any other plant, flower, fruit, grain, leaf or root steeped as a drink, including mate, rooibos, kava and roasted-grain substitutes? → Herbal & fruit infusions",
"4. Is it made from cacao for a hot drink, such as cocoa powder, drinking chocolate, malted powder, nibs or paste? → Cocoa & drinking chocolate",
"<i>Precedence: flavoured and scented tea stays in Tea; a roasted chicory or grain coffee substitute goes with herbal infusions (step 3); a ready-to-drink bottle or can → soft drinks, and a chocolate bar → chocolate confectionery.</i>"]

DT={
'Coffee':("Roasted or green coffee beans and the forms made from them, bought to brew at home; a ready-to-drink coffee → soft drinks (J9); a coffee machine → B5.",
 "What does the buyer choose by: where and how the coffee was grown and processed, how it was blended, or how it is packed for convenience?"),
'Tea':("Leaf of the tea plant sold to brew, including blends and scented tea made from it; a herbal infusion → Herbal & fruit infusions; a teapot or caddy → B5.",
 "Is it a blend for daily bags, a single class of leaf (black, green, oolong, white, yellow, dark) sold by country, or a tea scented or flavoured afterwards?"),
'Herbal & fruit infusions':("Plants other than tea steeped as a drink: herbs, flowers, fruit, spices, mate, rooibos, kava and roasted grains; true tea leaf → Tea.",
 "What is steeped: dried herb and flower, fruit or spice and blends, a drink plant with its own tradition, or roasted grain and root?"),
'Cocoa & drinking chocolate':("Cocoa powders, drinking chocolates and cacao products bought to make a hot drink; a chocolate bar or sweet → chocolate confectionery (J8).",
 "Is it a powder made up into a drink, or the cacao itself before it becomes chocolate?"),
}
for dp in d['depts']:
    dp['t'],dp['ax']=DT[dp['n']]

ST={
('Coffee','Speciality & single-origin coffee'):("Coffee sold for what it is rather than a blend: place, cultivar, process, species or raw bean; a house blend → Blends & everyday coffee.","kinds by what names the lot: place, cultivar, process, species, raw state"),
('Coffee','Blends & everyday coffee'):("Roasted coffee sold by blend, purpose or tradition, such as espresso blends, supermarket ground coffee, decaf and Turkish coffee; a single-origin lot → Speciality shelf.","kinds by purpose: espresso, filter, caffeine-free, regional method"),
('Coffee','Capsules, instant & cold brew'):("Coffee sold ready to make in seconds: sealed capsules, soluble powder or liquid concentrate; the machine → B5.","kinds by form of delivery: sealed single-serve, dissolved powder, liquid extract"),
('Tea','Everyday & breakfast tea'):("Blended black tea for daily cups, and instant or iced-tea mixes; a single-estate tea → Black tea.",""),
('Tea','Black tea'):("Fully oxidised tea sold by country, region and estate, such as Darjeeling, Assam, Ceylon and Keemun; a flavoured black tea → Scented, flavoured & spiced tea.","kinds by country or region: India, Sri Lanka, China and Taiwan, Africa and the Black Sea"),
('Tea','Japanese green tea'):("Unoxidised tea fixed by steam, in the forms Japanese shops sell: sencha, gyokuro, matcha, hojicha, genmaicha; Chinese green tea → next shelf.","kinds by how the leaf is grown or finished: steamed in sun, shaded, ground, stem, roasted, blended with rice"),
('Tea','Chinese, Korean & yellow green teas'):("Pan-fired green teas of China and Korea, and the rarer yellow teas; steamed Japanese green tea → Japanese green tea.","kinds by country and finish: Chinese green, Korean green, yellow"),
('Tea','Oolong & white tea'):("Partly oxidised oolongs and lightly processed white teas, such as Da Hong Pao, Tieguanyin, Oriental Beauty and Silver Needle.","kinds by region of the oolong, then white tea: Wuyi, Anxi, Phoenix, Taiwan, white"),
('Tea','Pu-erh & dark tea'):("Post-fermented tea pressed into cakes, bricks and baskets, led by Yunnan pu-erh, Liu Bao and Fu brick.","kinds by how it ferments: raw aged, wet-piled ripe, other dark tea"),
('Tea','Scented, flavoured & spiced tea'):("Tea given a scent or flavour after processing: Earl Grey, jasmine, fruit blends, masala chai, tied blooming tea.","kinds by what is added: bergamot oil, blossoms, fruit or smoke, spices, tied flowers"),
('Herbal & fruit infusions','Herb & flower infusions'):("Dried leaves, flowers and seeds of a single plant steeped alone, such as mint, chamomile, hibiscus and tulsi; a mixed blend → Fruit, spice & blended infusions.","kinds by plant part: leaf, flower, flowering stem, seed"),
('Herbal & fruit infusions','Fruit, spice & blended infusions'):("Dried fruit, spice roots and mixed herbal blends steeped as a drink, such as fruit tea, rose hip and ginger; a single herb → Herb & flower infusions.","kinds from one fruit to mixed blends: hip, fruit pieces, root and spice, blend"),
('Herbal & fruit infusions','Mate, rooibos & kava'):("Plants with their own drinking traditions: yerba mate, guayusa, yaupon, rooibos, honeybush and kava.","kinds by plant: holly leaf, South African shrub, pepper root"),
('Herbal & fruit infusions','Grain teas & coffee substitutes'):("Roasted grains, roots and seeds brewed in place of tea or coffee, such as barley tea, chicory and dandelion root.",""),
('Cocoa & drinking chocolate','Drinking chocolate & cocoa powder'):("Chocolate and cocoa made up with milk or water as a hot drink: drinking chocolate, instant mix, cocoa powder, malted powder.","kinds from real chocolate to powder: melted chocolate, instant mix, plain cocoa, malted powder"),
('Cocoa & drinking chocolate','Cacao beans & cacao products'):("Cacao before it is made into chocolate: beans, shells, nibs, paste and butter; a finished chocolate bar → chocolate confectionery (J8).","kinds by stage of processing, from bean to fat"),
}
for (dn,sn),(t,ax) in ST.items():
    s=shelf(dn,sn); s['t']=t
    if ax: s['ax']=ax
    elif 'ax' in s: del s['ax']

# demotion of generic archetypes -> models
DEMOTE={
'Single-origin coffee':['Ethiopia','Indonesia','Brazil','Rwanda','Tanzania','Panama Boquete'],
'Espresso blends':['Classic Italian espresso blend'],
'Instant coffee':['Freeze-dried instant','White coffee 3-in-1'],
'Iced tea mixes & tea concentrates':['Instant tea powder'],
'Darjeeling tea':['Darjeeling first flush','Darjeeling second flush','Darjeeling autumnal flush'],
'Assam & Indian black tea':['Assam second-flush tippy tea'],
'Ceylon tea':['Ceylon orthodox black tea'],
'Kenyan, African & Black Sea tea':['Kenyan CTC black tea'],
'Sencha & steamed green tea':['Shizuoka and Kagoshima sencha','Fukamushi sencha'],
'Hojicha':['Hojicha'],'Genmaicha':['Genmaicha'],'Phoenix Dancong oolong':['Phoenix Dancong'],
"Ripe pu-erh (shou)":["Wet-piled ripe pu'er"],
'Flavoured tea':['Russian Caravan smoked blend'],
'Masala chai blends':['Masala chai'],'Blooming tea':['Flowering tea'],
'Rooibos':['Rooibos (South African GI)'],'Honeybush':['Honeybush'],'Guayusa':['Ecuadorian guayusa'],
'Roasted grain tea':['Barley tea','Sobacha (buckwheat tea)'],
'Cocoa powder':['Natural cocoa','Black cocoa'],
'Green coffee':["Sweet Maria's green coffee range"],
}
demoted=[]
for kn,names in DEMOTE.items():
    k=find(kn); keep=[]
    for x in k.get('x',[]):
        if x['n'] in names:
            if kn=='Green coffee':
                k.setdefault('r',[]).append(["green coffee range","Sweet Maria's"]); demoted.append((kn,x['n'],'r')); continue
            m=k.setdefault('m',[])
            ents=[[v['n'],v.get('mk','')] for v in x.get('v',[])] or [[x['n'],x.get('mk','')]]
            for e in ents:
                if e not in m: m.append(e)
            demoted.append((kn,x['n'],'m'))
        else: keep.append(x)
    k['x']=keep
# illy blend: a house blend of one maker -> r
k=find('Espresso blends')
k['x']=[x for x in k['x'] if x['n']!='illy blend']; k.setdefault('r',[]).append(["illy classico blend","illy"]); demoted.append(('Espresso blends','illy blend','r'))
# pu-erh: factory archetypes -> recipe archetypes, factories into r
k=find('Raw pu-erh (sheng)')
for x in k['x']:
    if x['n']=='Menghai factory recipes':
        x['n']='7542 (Menghai recipe)'; x['a']='Dayi 7542'; x['d']='Menghai Tea Factory raw cake recipe of 1975, the model for four-digit pu-erh recipe numbers: year, leaf grade, factory digit.'
    if x['n']=='Xiaguan tea factory':
        x['n']='8653 (Xiaguan recipe)'; x['a']='Xiaguan 8653 tuocha'; x['d']='Raw recipe number from the Xiaguan factory, known for tuocha.'
k.setdefault('r',[]); k['r']+= [["Dayi recipes","Menghai Tea Factory"],["Xiaguan tuocha","Xiaguan Tea Factory"]]
find('Ripe pu-erh (shou)')['d']=find('Ripe pu-erh (shou)')['d']

# kind renames/merges: none. add new kinds
def kind(n,a,dd,s,**kw):
    k={'n':n,'a':a,'d':dd,'s':s}; k.update(kw); return k
new={
('Herbal & fruit infusions','Herb & flower infusions'):[
 kind('Tulsi (holy basil)','holy basil · tulasi','Dried leaves of holy basil (Ocimum tenuiflorum) sold for infusion, alone or blended.','https://en.wikipedia.org/wiki/Herbal_tea'),
 kind('Butterfly pea flower','blue tea · clitoria','Dried flowers of Clitoria ternatea that turn the drink blue.','https://en.wikipedia.org/wiki/Herbal_tea'),
 kind('Seed infusions','fennel · anise · caraway','Dried fennel, anise or caraway seeds sold for infusion.','https://en.wikipedia.org/wiki/Herbal_tea')],
('Herbal & fruit infusions','Mate, rooibos & kava'):[
 kind('Yaupon','yaupon holly · Ilex vomitoria','Dried leaves of Ilex vomitoria, the one caffeinated holly native to North America, sold for infusion.','https://en.wikipedia.org/wiki/Herbal_tea')],
('Tea','Japanese green tea'):[
 kind('Kukicha (twig tea)','twig tea · karigane','Japanese green tea made from stems and twigs left from sencha or gyokuro.','https://ratetea.com/style.php')],
('Cocoa & drinking chocolate','Drinking chocolate & cocoa powder'):[
 kind('Instant hot chocolate mix','hot cocoa mix','Cocoa powder with sugar, milk powder and stabilisers, sold in sachets or tubs to stir into hot water or milk.','https://thenibble.com/reviews/main/beverages/cocoas/hot-chocolate-overview3.asp')],
}
for (dn,sn),ks in new.items(): shelf(dn,sn)['k']+=ks
# Nesquik archetype -> instant mix
dc=find('Drinking chocolate'); inst=find('Instant hot chocolate mix')
nes=[x for x in dc['x'] if x['n']=='Nesquik']; dc['x']=[x for x in dc['x'] if x['n']!='Nesquik']; inst['x']=nes
dc['d']='Chocolate or sweetened cocoa sold to make a hot drink, richest when it keeps its cocoa butter; a plain unsweetened powder is cocoa powder.'
# coffee cultivars added
gk=find('Geisha & rare-variety coffee')
gk['x']+= [{"n":"SL14","a":"","d":"Kenyan arabica variety of the Typica group listed in the World Coffee Research catalog.","mk":"","y":"","s":"https://worldcoffeeresearch.org/work/catalog/varieties","v":[]},
 {"n":"Batian","a":"","d":"Kenyan arabica variety named in the World Coffee Research catalog update.","mk":"","y":"","s":"https://worldcoffeeresearch.org/work/catalog/varieties","v":[]}]

# reorder
def reorder(dn,sn,names):
    s=shelf(dn,sn); idx={k['n']:k for k in s['k']}; assert set(idx)==set(names),(set(idx)^set(names))
    s['k']=[idx[n] for n in names]
reorder('Herbal & fruit infusions','Herb & flower infusions',['Peppermint & mint','Lemongrass & lemon verbena','Tulsi (holy basil)','Nettle, birch & garden leaves','Kuding','Chamomile','Hibiscus','Chrysanthemum','Garden & meadow flowers','Butterfly pea flower','Mountain tea','Seed infusions'])
reorder('Herbal & fruit infusions','Fruit, spice & blended infusions',['Rose hip','Fruit tea','Ginger, turmeric & spice infusions','Herbal blend'])
reorder('Herbal & fruit infusions','Mate, rooibos & kava',['Yerba mate','Guayusa','Yaupon','Rooibos','Honeybush','Kava'])
reorder('Tea','Japanese green tea',['Sencha & steamed green tea','Gyokuro & kabusecha','Matcha','Kukicha (twig tea)','Hojicha','Genmaicha'])
reorder('Cocoa & drinking chocolate','Drinking chocolate & cocoa powder',['Drinking chocolate','Instant hot chocolate mix','Cocoa powder','Malted chocolate drink powder'])
reorder('Cocoa & drinking chocolate','Cacao beans & cacao products',['Cacao beans','Cocoa shells','Cocoa nibs','Cocoa paste & ceremonial cacao','Cocoa butter'])

TT={
'Single-origin coffee':[["Form",["Whole bean","Ground","Drip bag"]],["Roast",["Light","Medium","Dark"]],["Process",["Washed","Natural","Honey"]]],
'Geisha & rare-variety coffee':[["Form",["Whole bean","Ground"]],["Process",["Washed","Natural","Honey"]]],
'Special-process coffee':[["Fermentation",["Anaerobic","Carbonic maceration","Co-fermented","Black honey"]]],
'Speciality Robusta, Liberica & Excelsa':[["Species",["Fine Robusta","Liberica","Excelsa"]],["Form",["Whole bean","Ground"]]],
'Green coffee':[["Species",["Arabica","Robusta"]],["Process",["Washed","Natural","Honey"]],["Pack",["Sample 1 lb","Bag 5–20 lb"]]],
'Espresso blends':[["Roast",["Medium","Dark","Italian dark"]],["Composition",["100% arabica","Arabica with robusta"]],["Form",["Whole bean","Ground","Pressurised tin"]]],
'Everyday ground & filter coffee':[["Form",["Roast and ground","Whole bean","Pods compatible"]],["Roast",["Light","Medium","Dark"]],["Pack",["Brick","Can","Bag"]]],
'Decaffeinated coffee':[["Decaffeination method",["Swiss Water process","Supercritical CO2","Ethyl acetate","Dichloromethane (methylene chloride)","Triglyceride process"]],["Form",["Whole bean","Ground","Instant"]]],
'Traditional regional coffee':[["Grind",["Powder-fine","Coarse","Medium"]],["Form",["Ground","Whole bean","Pre-spiced"]]],
'Coffee capsules & pods':[["Material",["Aluminium capsule","Plastic capsule","Compostable capsule","Paper pod"]],["System",["Original line","Vertuo line","Dolce Gusto","Tassimo","A Modo Mio","Senseo","K-Cup","E.S.E."]]],
'Instant coffee':[["Drying method",["Spray-dried","Freeze-dried","Agglomerated granules"]],["Mix",["Pure coffee","3-in-1 with milk and sugar"]]],
'Cold brew & coffee concentrate':[["Brewing",["Cold brew concentrate","Hot-brewed concentrate"]],["Pack",["Bottle","Single-serve pod","Bag-in-box"]]],
'Breakfast & everyday black tea':[["Form",["Tea bag","Pyramid bag","Loose"]],["Caffeine",["Regular","Decaf"]],["Style",["English Breakfast","Irish Breakfast","Scottish Breakfast","Afternoon blend"]]],
'Iced tea mixes & tea concentrates':[["Type",["Unsweetened instant tea","Sweetened iced-tea mix","Tea concentrate"]]],
'Darjeeling tea':[["Flush",["First flush","Second flush","Autumnal","Monsoon"]],["Grade",["FTGFOP","TGFOP","FOP","Broken"]]],
'Assam & Indian black tea':[["Manufacture",["Orthodox","CTC"]],["Region",["Assam","Nilgiri","Kangra","Dooars"]],["Flush",["First flush","Second flush"]]],
'Ceylon tea':[["Manufacture",["Orthodox","CTC"]],["Elevation",["High-grown","Mid-grown","Low-grown"]]],
'Chinese & Taiwanese black tea':[["Leaf style",["Whole leaf","Golden buds","Broken"]],["Smoking",["Unsmoked","Pine-smoked"]]],
'Kenyan, African & Black Sea tea':[["Manufacture",["CTC","Orthodox"]],["Origin",["Kenya","Malawi","Rize (Turkey)","Ilam (Nepal)"]]],
'Sencha & steamed green tea':[["Harvest",["Shincha (first flush)","Ichibancha","Nibancha"]],["Steaming",["Asamushi (light)","Chumushi","Fukamushi (deep)"]],["Grade",["Sencha","Bancha","Tamaryokucha"]]],
'Gyokuro & kabusecha':[["Shading",["Gyokuro (about 20 days)","Kabusecha (about a week)"]],["Origin",["Uji","Yame","Shizuoka"]]],
'Matcha':[["Grade",["Ceremonial (usucha)","Ceremonial (koicha)","Culinary"]],["Pack",["Tin","Sachet","Bulk bag"]]],
'Kukicha (twig tea)':[["Base",["Sencha stems","Gyokuro stems","Roasted stems"]]],
'Hojicha':[["Base leaf",["Bancha","Kukicha","Sencha"]],["Form",["Leaf","Powdered"]]],
'Genmaicha':[["Addition",["Roasted rice","Popped rice","Matcha"]]],
'Chinese green tea':[["Shape",["Flat","Needle","Curled","Pellet","Melon-seed"]],["Harvest",["Pre-Qingming","Spring","Summer"]]],
'Korean green tea':[["Harvest",["Ujeon","Sejak","Jungjak","Daejak"]]],
'Yellow tea':[["Leaf",["Buds","Bud and leaf"]]],
'Wuyi rock oolong':[["Roast",["Light","Medium","Heavy charcoal"]],["Cultivar group",["Named cultivars","Blends"]]],
'Tieguanyin & Anxi oolong':[["Style",["Green (jade)","Traditional charcoal roast"]],["Grade",["Premium","Standard"]]],
'Phoenix Dancong oolong':[["Aroma",["Honey orchid","Almond","Ginger flower","Tree-type old bush"]]],
'Taiwanese oolong':[["Oxidation",["Light","Medium","Heavy"]],["Altitude",["Lowland","High mountain"]]],
'White tea':[["Plucking",["Buds only","Bud and leaves","Mature leaf"]],["Form",["Loose","Cake"]]],
'Raw pu-erh (sheng)':[["Form",["Bing cake 357 g","Tuocha","Brick","Loose"]],["Leaf source",["Plantation","Old tree","Wild arbor"]],["Age",["Young","Aged"]]],
'Ripe pu-erh (shou)':[["Form",["Bing cake","Tuocha","Brick","Loose"]],["Leaf grade",["Fine bud","Broken"]]],
'Dark tea (hei cha)':[["Form",["Loose","Brick","Basket","Tile"]],["Fermentation",["Fungal (Fu)","Bacterial","Aged"]]],
'Earl Grey & bergamot tea':[["Base",["Black","Green","White","Rooibos"]],["Variant",["Classic","Lady Grey","Cream","Russian"]]],
'Jasmine & scented tea':[["Base",["Green","White","Black"]],["Shape",["Loose","Pearls","Pressed"]],["Blossom",["Jasmine","Osmanthus","Rose"]]],
'Flavoured tea':[["Base",["Black","Green","Oolong","White"]],["Flavour",["Fruit","Vanilla and caramel","Smoked","Mint","Floral"]]],
'Masala chai blends':[["Form",["Loose blend","Tea bag","Powder","Concentrate"]],["Spice mix",["Cardamom and ginger","Cinnamon and clove","Black pepper"]]],
'Blooming tea':[["Base",["Green","White","Black"]],["Flower",["Jasmine","Lily","Osmanthus","Amaranth"]]],
'Peppermint & mint':[["Species",["Peppermint","Spearmint","Nana (Moroccan) mint"]],["Form",["Loose","Tea bags"]]],
'Lemongrass & lemon verbena':[["Plant",["Lemongrass","Lemon verbena"]],["Form",["Loose","Tea bags"]]],
'Tulsi (holy basil)':[["Variety",["Rama","Krishna","Vana"]],["Form",["Loose","Tea bags"]]],
'Nettle, birch & garden leaves':[["Plant",["Nettle","Birch leaf","Marjoram"]]],
'Kuding':[["Plant",["Ilex (large-leaf)","Ligustrum (small-leaf)"]]],
'Chamomile':[["Species",["German chamomile","Roman chamomile"]],["Form",["Whole flowers","Tea bags"]]],
'Hibiscus':[["Cut",["Whole calyces","Cut","Tea bags"]]],
'Chrysanthemum':[["Form",["Whole flowers","Buds"]],["Colour",["White","Yellow"]]],
'Garden & meadow flowers':[["Flower",["Lavender","Elderflower","Calendula","Yarrow"]]],
'Butterfly pea flower':[["Form",["Whole flowers","Powder"]]],
'Mountain tea':[["Cut",["Whole stems","Cut"]]],
'Seed infusions':[["Seed",["Fennel","Anise","Caraway"]]],
'Rose hip':[["Cut",["Whole","Cut and sifted"]],["Blend",["Pure","With hibiscus"]]],
'Fruit tea':[["Form",["Tea bag","Loose"]],["Fruit base",["Berry","Citrus","Apple","Hibiscus-rose hip"]]],
'Ginger, turmeric & spice infusions':[["Root or spice",["Ginger","Turmeric","Cinnamon","Liquorice root"]],["Form",["Dried slices","Powder","Instant powder"]]],
'Herbal blend':[["Purpose",["Relaxing","Digestive","Morning","Night"]],["Form",["Tea bag","Loose"]]],
'Yerba mate':[["Cut",["Con palo (with stem)","Despalada (without stem)"]],["Drying",["Barbacuá smoke-dried","Air-dried"]],["Style",["Traditional","Flavoured"]]],
'Guayusa':[["Form",["Cut leaf","Tea bags"]]],
'Yaupon':[["Roast",["Green","Roasted"]]],
'Rooibos':[["Oxidation",["Red (oxidised)","Green (unoxidised)"]],["Cut",["Super grade","Long cut","Fine cut"]]],
'Honeybush':[["Species",["Cyclopia intermedia","Cyclopia genistoides"]],["Cut",["Cut","Fine cut"]]],
'Kava':[["Cultivar group",["Noble","Tudei"]],["Form",["Root powder","Micronised"]]],
'Roasted grain tea':[["Grain",["Barley (mugicha, boricha)","Corn (oksusu-cha)","Buckwheat (soba-cha)","Brown rice"]],["Form",["Loose","Tea bags"]]],
'Coffee substitutes':[["Plant",["Roasted chicory","Dandelion root","Grain coffee"]],["Form",["Granules","Ground"]]],
'Drinking chocolate':[["Form",["Flakes","Shavings","Block","Powder"]],["Style",["Italian thick","Spanish a la taza","Mexican table","British"]]],
'Instant hot chocolate mix':[["Pack",["Sachet","Tub"]],["Sweetening",["Sugar","Reduced sugar","Sugar-free"]]],
'Cocoa powder':[["Treatment",["Natural","Dutch-process","Black cocoa"]],["Fat content",["Low-fat (10–12%)","High-fat (20–22%)"]]],
'Malted chocolate drink powder':[["Pack",["Tub","Sachet"]],["Malt base",["Barley malt","Wheat malt"]]],
'Cacao beans':[["Stage",["Raw","Fermented and dried","Roasted"]],["Genetic group",["Criollo","Forastero","Trinitario","Nacional"]],["Grade",["ICCO fine or flavour","Bulk"]]],
'Cocoa shells':[["Form",["Whole","Ground"]]],
'Cocoa nibs':[["Roast",["Raw","Roasted"]]],
'Cocoa paste & ceremonial cacao':[["Form",["Block","Drops"]]],
'Cocoa butter':[["Treatment",["Natural","Deodorised"]]],
}
allk=[k for dp in d['depts'] for s in dp['s'] for k in s['k']]
missing=[k['n'] for k in allk if k['n'] not in TT]
assert not missing,missing
for k in allk:
    k['tt']=TT[k['n']]; k.pop('t',None)

SEE={
'Cold brew & coffee concentrate':[["J9","Cold brew & iced coffee","bottled ready-to-drink"]],
'Green coffee':[["B5","Home coffee roaster","machine to roast it"]],
'Coffee capsules & pods':[["B5","Capsule coffee machine","machine for the capsules"]],
'Matcha':[["B5","Matcha whisk and scoop","tools to whisk it"]],
'Roasted grain tea':[["J9","Barley & grain tea","bottled ready-to-drink"]],
'Yerba mate':[["J9","Yerba mate & guayusa drink","bottled ready-to-drink"]],
'Iced tea mixes & tea concentrates':[["J9","Iced tea","bottled ready-to-drink"]],
'Drinking chocolate':[["J8","Hot chocolate bomb & drinking flakes","chocolate confectionery form"]],
}
for n,v in SEE.items(): find(n)['see']=v
json.dump(ren,open(R+'out/J6_renames.json','w'))
json.dump(demoted,open(R+'work/STR_J6/demoted.json','w'))
json.dump(d,open(R+'work/STR_J6/J6.tmp','w'),ensure_ascii=False,indent=1)
