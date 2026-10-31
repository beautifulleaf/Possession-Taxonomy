import json,copy,os,sys
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/STR_J3/bak/J3.json'))
W='https://en.wikipedia.org/wiki/'
S_DAIRY=W+'List_of_dairy_products'; S_FERM=W+'List_of_fermented_milk_products'; S_PLANT=W+'Plant_milk'

# ---------- index ----------
kinds={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: kinds[k['n']]=k
shelves={s['n']:s for dp in d['depts'] for s in dp['s']}
depts={dp['n']:dp for dp in d['depts']}
stats_before=dict(depts=len(d['depts']),shelves=len(shelves),kinds=len(kinds),arch=sum(len(k.get('x',[])) for k in kinds.values()))

# ---------- demote generic archetypes into models ----------
DEMOTE={
 'Strained yoghurt':['Greek yoghurt'],'Labneh':['Labneh'],'Kefir':['Grain kefir'],
 'Buttermilk':['Cultured buttermilk','Traditional buttermilk'],'Kumys':['Kumis'],'Ryazhenka':['Ryazhenka'],
 'Quark & fromage blanc':['Quark','Fromage blanc'],'Queso fresco & fresh white cheese':['Queso fresco / queso blanco','Farmer cheese'],
 'Brie':['Dairy brie','British and Irish farmhouse brie'],'Camembert':['Dairy camembert'],'Gruyère':['Generic gruyere'],
 'Cheddar':['Artisan Somerset Cheddar','Clothbound farmhouse cheddar','Creamery block cheddar'],
 'Lancashire':['Crumbly Lancashire'],'Colby':['Washed-curd longhorn Colby'],'Monterey Jack':['Monterey Jack'],
 'Manchego':['Queso ibérico','Mexican manchego'],'Fontina':['Danish, Swedish and US fontina'],
 'Mozzarella':['Low-moisture mozzarella'],'Gouda':['Aged Gouda',"Goat's-milk Gouda"],'Edam':['Edam ball'],
 'Brined white cheese':['Feta-style white cheese'],'Chhurpi':['Hard chhurpi','Soft chhurpi'],
 'Tempeh':['Soy tempe','Oat tempeh'],
}
demoted=[]
for kn,names in DEMOTE.items():
    k=kinds[kn]; keep=[]; m=[list(x) for x in k.get('m',[])]
    have={tuple(x) for x in m}
    for x in k.get('x',[]):
        if x['n'] in names:
            vs=x.get('v') or []
            adds=[[v['n'],v.get('mk','') or ''] for v in vs] or [[x['n'],x.get('mk','') or '']]
            for a in adds:
                if tuple(a) not in have: m.append(a); have.add(tuple(a))
            demoted.append(f"{kn}: {x['n']} ({len(vs)} versions)")
        else: keep.append(x)
    assert len(keep)==len(k.get('x',[]))-len(names),(kn,names)
    if keep: k['x']=keep
    else: k.pop('x',None)
    if m: k['m']=m

# ---------- new archetypes (named things, fetched list pages) ----------
def arch(kn,n,a,dd,y,s,mk=''):
    kinds[kn].setdefault('x',[]).append({'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':s})
arch('Ghee & clarified butter','Smen','smen · sman · samn','Salted, fermented clarified butter of Morocco and North Africa, aged for strong flavour.','',S_DAIRY)
arch('Strained yoghurt','Shrikhand','srikhand','Sweet strained yoghurt of western India, eaten as a dessert.','',S_FERM)
arch('Soured milk','Leben','laban · lben','Soured milk drink of the Arab world and Middle East.','',S_FERM)
kinds['Ghee & clarified butter']['d']='Butterfat with water and milk solids removed; ghee is simmered further until the solids brown for a nutty flavour. Spiced niter kibbeh and fermented smen are regional forms.'

# ---------- new kinds (each with a fetched source) ----------
def newkind(n,a,dd,s,tt=None):
    k={'n':n,'a':a,'d':dd,'s':s}
    if tt: k['tt']=tt
    kinds[n]=k; return k
newkind('Horse, donkey & yak milk',"mare's milk · donkey milk · yak milk · reindeer milk",'Milk of less common dairy animals such as the mare, donkey, yak and reindeer, drunk or fermented and sold in small amounts.',S_DAIRY,[['Animal',['mare','donkey','yak','reindeer']]])
newkind('Half-and-half & light cream','half and half · blend cream · table cream · coffee cream','Blend of milk and cream, 10.5 to 18 per cent fat in the United States, poured into coffee and over cereal; light cream is slightly richer.',W+'Half_and_half',[['Fat level',['half-and-half (10.5–18%)','light cream (18–30%)']]])
newkind('Khoa & mawa','khoya · mawa · khova · bhuna khoya','Milk cooked down to a thick paste or crumbly solid, the base of South Asian milk sweets.',S_DAIRY,[['Cooking stage',['fresh khoa','browned (bhuna khoya)']]])
newkind('Cheese curds','squeaky cheese · fromage en grain · poutine curds','Moist pieces of fresh curd eaten as a snack or used in dishes such as poutine; they squeak against the teeth when very fresh.',W+'Cheese_curd')
newkind('Crescenza & stracchino','crescenza · stracchino · stracchino crescenza','Square, rindless, soft cow\'s-milk cheese of northern Italy, eaten very young; creamy, mild and slightly acidic.',W+'Stracchino')
newkind('Muenster (American)','American muenster · muenster','Pale, mild, semi-soft pasteurised cow\'s-milk cheese of the United States with an orange annatto rind; not the pungent French Munster.',W+'Muenster_cheese')
newkind('Grain, tuber & fruit drink','spelt milk · barley drink · potato milk · horchata de chufa · banana milk','Plant drink made from a grain other than oat or rice, or from a tuber or fruit such as potato, tiger nut or banana.',S_PLANT,[['Base',['spelt','barley','quinoa','millet','buckwheat','potato','tiger nut','banana']]])

# ---------- tt by hand ----------
TT={
"Cow's milk":[["Fat level",["whole / full cream","semi-skimmed","skimmed"]],["Treatment",["lactose-free","filtered (extended shelf life)","UHT / long-life","raw"]],["Protein or breed",["A2","Jersey / breed milk"]],["Feeding or farming",["organic","hay milk (Heumilch TSG)"]]],
"Goat's milk":[["Treatment",["fresh","UHT / long-life","powdered"]],["Feeding",["hay milk (Ziegen-Heumilch TSG)"]]],
"Sheep's milk":[["Treatment",["fresh","frozen"]]],
"Buffalo milk":[["Fat level",["full cream"]],["Protein",["A2"]]],
"Camel milk":[["Treatment",["fresh","frozen","long-life","powdered"]],["Flavour",["flavoured"]]],
"Flavoured milk drink":[["Flavour",["chocolate","strawberry","banana","coffee","vanilla","melon","malted"]],["Pack",["bottle","carton"]]],
"Cream":[["Fat level",["single / light","whipping","double / heavy"]],["Form",["pouring","thickened (spoonable)","aerosol whipped"]]],
"Clotted cream & kaymak":[["Region",["Cornish and Devon clotted cream","Turkish kaymak","Balkan kajmak"]]],
"Crème fraîche":[["Thickness",["thick (épaisse)","liquid (fluide)"]],["Fat level",["half-fat","full-fat"]]],
"Soured cream & smetana":[["Style",["soured cream","smetana"]],["Fat level",["full-fat","light"]]],
"Dairy creamer & whitener":[["Form",["liquid creamer","portion cups","powder"]]],
"Evaporated & condensed milk":[["Sugar",["unsweetened (evaporated)","sweetened (condensed)"]],["Pack",["tin","tube"]]],
"Milk powder":[["Fat level",["skimmed","whole"]],["Solubility",["instant","regular"]]],
"Dulce de leche":[["Regional name",["dulce de leche","arequipe","manjar","doce de leite"]],["Milk",["cow's milk","goat's milk (cajeta)"]]],
"Butter":[["Salt",["salted","unsalted"]],["Cream",["sweet cream","cultured (European-style)","whey butter"]],["Milk treatment",["raw-milk"]],["Additions",["flavoured / compound"]],["Region",["Indian white butter (makkhan)"]]],
"Ghee & clarified butter":[["Animal",["cow","buffalo"]],["Method",["hand-churned (bilona / A2)","plain clarified butter"]]],
"Spreadable butter":[["Fat blend",["with rapeseed or canola oil","with olive oil"]],["Salt",["slightly salted"]],["Fat level",["lighter / reduced fat"]],["Farming",["organic"]]],
"Yoghurt":[["Texture",["set","stirred","cream-top (kaymaklı)"]],["Flavour",["plain","fruit"]],["Culture",["probiotic"]],["Vessel",["clay-pot (çömlek)"]],["Milk",["cow's","sheep's","goat's","buffalo"]]],
"Strained yoghurt":[["Style",["Greek (made in Greece)","Greek-style","süzme / kese yoğurdu (Turkey)","salcë kosi (Albania)","chakka / hung curd (South Asia)"]],["Fat level",["fat-free","low-fat","full-fat"]]],
"Skyr":[["Flavour",["plain","flavoured"]],["Form",["spoonable","drinkable"]]],
"Labneh":[["Form",["labneh spread","labneh balls in oil (labaneh biz-zayt)"]]],
"Kefir":[["Milk",["cow's","goat's"]],["Flavour",["plain","flavoured"]],["Fat level",["low-fat / non-fat"]],["Farming",["organic"]]],
"Drinking yoghurt & ayran":[["Taste",["salted","sweet","fruit-flavoured","with mint or herbs"]],["Texture",["churned (frothy)","carbonated"]]],
"Buttermilk":[["Make",["cultured buttermilk","traditional churned buttermilk"]],["Taste",["spiced (masala)"]],["Fat level",["low-fat"]]],
"Soured milk":[["Texture",["drinkable","spoonable","ropy / long"]],["Culture",["probiotic"]],["Flavour",["flavoured"]],["Fat level",["low-fat"]]],
"Probiotic cultured drink":[["Sugar",["original","reduced sugar / light"]],["Bacteria count",["high-count"]]],
"Kumys":[["Milk",["mare's milk","cow's milk (industrial)"]]],
"Ryazhenka":[["Fat level",["low (from 1%)","high (up to 8.9%)"]]],
"Cream cheese":[["Fat level",["full-fat","light / reduced-fat"]],["Flavour",["plain","flavoured (herb, chive, sweet)"]],["Form",["block","whipped tub"]]],
"Ricotta & whey cheese":[["Make",["whey only","whey with added milk"]],["Finish",["fresh","salted and pressed (ricotta salata)","baked (infornata)","smoked (affumicata)","fermented (forte)"]]],
"Mascarpone":[["Fat level",["standard","reduced-fat"]]],
"Fresh goat's cheese":[["Form",["plain log","tub / spreadable","goat's fromage blanc"]],["Coating",["ash-coated","herbed or peppered"]]],
"Fresh soft cheese":[["Flavour",["plain","herbed","garlic","peppered"]],["Form",["spreadable tub","processed spread"]]],
"Quark & fromage blanc":[["Fat level",["low-fat (Magerquark)","full-fat"]],["Texture",["spoonable quark","fromage frais (live cultures)","faisselle (moulded, draining)"]],["Flavour",["flavoured"]]],
"Cottage cheese":[["Curd size",["small curd","large curd"]],["Fat level",["low-fat","full-fat"]]],
"Queso fresco & fresh white cheese":[["Texture",["crumbly","sliceable","frying cheese (queso frito)"]],["Milk",["cow's","goat's or mixed"]]],
"Paneer & chhena":[["Form",["block","cubes"]],["Fat level",["full-fat (malai)","low-fat / high-protein"]]],
"Brunost":[["Form",["block (sliced with a cheese slicer)","spread (prim / messmör)"]],["Milk",["cow's","goat's","mixed"]]],
"Brie":[["Maker",["farmhouse (fermier)","dairy (laitier)"]],["Milk",["raw","pasteurised"]],["Ripening",["aged black brie (brie noir)"]],["Flavouring",["truffled","smoked"]],["Cream content",["double-cream"]]],
"Camembert":[["Milk",["raw (au lait cru)","pasteurised"]],["Treatment",["smoked"]],["Pack",["boxed whole","portions"]]],
"Double- & triple-cream cheese":[["Fat level",["double-cream","triple-cream"]],["Ripeness",["fresh (frais)","affiné"]],["Flavouring",["truffled"]]],
"Lactic goat cheese":[["Rind",["ash-coated","natural rind","leaf-wrapped"]],["Age",["fresh (frais)","aged (sec)"]]],
"Époisses":[["Milk",["raw","pasteurised"]],["Maker",["farmhouse (fermier)","dairy (laitier)"]],["Size",["small (c. 250 g)","large (c. 18 cm)"]]],
"Munster":[["Size",["standard (450 g–1.5 kg)","petit-munster (from 120 g)"]],["Maker",["farmhouse (fermier)","dairy (laitier)"]],["Milk",["raw milk"]]],
"Reblochon":[["Maker",["fermier (green casein tag)","laitier (red casein tag)"]],["Size",["standard (450–550 g)","petit reblochon (240–280 g)"]]],
"Taleggio":[["Format",["whole square","portion"]],["Milk",["raw","pasteurised"]]],
"Vacherin Mont-d'Or":[["Origin",["French","Swiss"]],["Format",["boxed whole cheese"]]],
"Pont-l'Évêque & Livarot":[["Milk",["raw","pasteurised"]],["Size",["full size","half or small formats"]]],
"Maroilles":[["Size",["Maroilles (c. 700 g)","Sorbais (3/4 size)","smaller regulated sizes"]]],
"Saint-Nectaire":[["Maker",["fermier (farmhouse)","laitier (dairy)"]]],
"Monastery cheese":[["Maker",["abbey-made","dairy-made"]],["Milk",["pasteurised","raw"]]],
"Limburger & Herve":[["Strength",["mild (doux)","sharp (piquant)"]],["Shape",["stick or brick"]],["Fat in dry matter",["20% to 60%"]]],
"Tilsit":[["Age",["mild","matured"]],["Flavouring",["with caraway"]]],
"Harzer & sour-milk cheese":[["Ripening",["yellow (red-smear)","white (mould-ripened)"]],["Flavouring",["with caraway"]],["Shape",["roll or stick"]]],
"Farmhouse washed-rind cheese":[["Texture",["semi-soft","soft"]],["Treatment",["smoked"]],["Milk",["raw","pasteurised"]]],
"Gruyère":[["Age",["doux (mild, 6 months+)","réserve / surchoix (10 months+)","mi-salé, salé, vieux"]],["Ageing place",["cave-aged (Höhlengereift)"]],["Season",["alpage (summer)"]],["Farming",["organic"]]],
"Comté":[["Grade",["Extra (green band)","standard (brown band)"]],["Age",["young (4–8 months)","mature (12–18 months)","long-aged (24 months+)"]],["Farming",["organic"]]],
"Emmental":[["Age and grade",["classic (4 months+)","surchoix","Premier Cru (14 months+)"]],["Ripening",["cave-aged","foil-ripened block"]]],
"Beaufort & Abondance":[["Season of milk",["winter (hiver)","summer (été)","high-pasture summer (alpage / chalet)"]]],
"Appenzeller":[["Age band",["Classic (silver, 3–4 months)","Surchoix (gold, 4–6 months)","Extra (black, 6 months+)"]]],
"Bergkäse & Alpkäse":[["Where made",["Alp (summer pasture)","village dairy"]],["Texture",["extra-hard planing cheese (Hobelkäse)"]],["Milk",["raw milk, no silage"]]],
"Raclette":[["Milk",["raw","pasteurised"]],["Format",["wheel","half-wheel","slices"]],["Flavouring",["smoked","pepper","garlic"]]],
"Fontina":[["Age",["young (fondue)","mature"]]],
"Vacherin fribourgeois":[["Style",["Classic","Extra","Rustic","Alpage","Mountain"]],["Farming",["organic"]]],
"Tête de Moine":[["Format",["whole wheel","pre-pared rosettes"]]],
"Morbier":[["Milk",["raw","pasteurised"]]],
"Tomme":[["Milk",["cow","ewe","goat"]],["Fat",["skimmed","whole milk"]],["Rind",["natural","waxed"]]],
"Cheddar":[["Age",["mild","medium","mature","extra mature","vintage"]],["Rind",["clothbound (larded cloth)","block / rindless"]],["Colour",["white","coloured (annatto)"]],["Treatment",["smoked"]],["Milk",["raw","pasteurised"]],["Maker",["farmhouse","creamery"]]],
"Cheshire":[["Colour",["white","red (annatto)","blue"]],["Rind",["clothbound","waxed"]]],
"Lancashire":[["Style by age",["Creamy (4–12 weeks)","Tasty (12 weeks–24 months)","Crumbly (single-day curd)"]]],
"Wensleydale":[["Flavouring",["plain","with cranberries"]]],
"Red Leicester":[["Ripening",["cloth-matured wheel","block"]],["Age",["mild","mature"]]],
"Gloucester":[["Type",["Single","Double"]],["Colour",["coloured","natural"]]],
"Caerphilly":[["Age",["young (2 weeks)","ripened with rind (2–4 months)"]]],
"Derby & Sage Derby":[["Flavouring",["plain","sage","port wine"]]],
"Colby":[["Shape",["longhorn","block"]],["Blend",["Colby-Jack marble"]]],
"Monterey Jack":[["Age",["young (about 1 month)"]],["Flavouring",["pepper"]],["Blend",["cheddar-Jack marble"]]],
"Parmigiano Reggiano & grana":[["Form",["whole wedge","grated","shavings"]]],
"Manchego":[["Age",["fresco","semicurado","curado","viejo"]],["Milk treatment",["artesano (raw milk)","pasteurised"]]],
"Pyrenean sheep cheese":[["Milk",["raw","pasteurised"]],["Maker",["fermier"]],["Season",["estive (summer mountain)"]],["Age",["aged"]]],
"Pecorino":[["Age",["fresco/dolce","semi-aged","aged/stagionato"]],["Flavouring",["peppered"]],["Rind",["rind-treated"]]],
"Idiazábal & Roncal":[["Smoking",["smoked","unsmoked"]]],
"Mozzarella":[["Size",["bocconcini (bite-size)","ciliegine (cherry-size)","ovolini (egg-size)"]],["Shape",["treccia (plait)","nodini (knots)","fiaschetto (flask)","stick / string"]],["Treatment",["smoked (affumicata)","shredded or sliced"]],["Moisture",["fresh","low-moisture"]]],
"Burrata & stracciatella":[["Size",["burratina (small)"]],["Milk",["cow's","buffalo"]],["Flavouring",["truffled","smoked"]]],
"Provolone & caciocavallo":[["Age",["dolce (mild, short-aged)","piccante (sharp, long-aged)"]],["Shape",["pear","salame","melon"]],["Treatment",["smoked"]]],
"Scamorza & provola":[["Smoking",["bianca (unsmoked)","affumicata (smoked)"]],["Milk",["cow's","buffalo"]]],
"Kashkaval":[["Age",["fresh (taze)","aged (eski)"]],["Milk",["sheep's","cow's","mixed"]],["Treatment",["smoked"]]],
"Braided string cheese":[["Treatment",["plain","smoked","brined"]],["Shape",["braid","wound ball","spiral"]]],
"Sulguni":[["Treatment",["fresh","smoked"]],["Milk",["cow's","buffalo"]]],
"Gouda":[["Age",["young to very old (six Dutch age bands)"]],["Maker",["farmhouse raw-milk","dairy pasteurised"]],["Flavouring",["cumin, herbs or spices"]],["Milk",["cow's","goat's","sheep's"]],["Fat level",["low-fat to full-fat"]]],
"Edam":[["Age",["young (mild)","aged (firmer, sharper)"]],["Shape",["ball","block"]],["Fat level",["reduced-fat"]]],
"Leyden & spiced Dutch cheese":[["Spice",["cumin (komijn)","cloves and cumin (nagel)"]],["Maker",["farmhouse","dairy"]]],
"Maasdam & Jarlsberg":[["Age",["mild","mature"]],["Format",["slices","block","wheel"]],["Fat level",["reduced-fat"]]],
"Havarti":[["Flavouring",["plain","herbs, spices"]],["Age",["young","aged"]],["Format",["slices","block"]]],
"Danbo":[["Age",["young to mature (12–52 weeks)"]]],
"Swedish hard cheese":[["Fat content",["17% to 45%"]],["Age",["young","long-aged"]],["Format",["waxed wheel","block"]]],
"Torta cheese":[["Texture",["torta (spoonable)","firmer, longer-aged queso"]]],
"Mahón-Menorca":[["Age",["artesano (young, soft)","aged (hard)"]]],
"Spanish goat cheese":[["Age",["fresh","semicurado","curado"]],["Treatment",["smoked"]],["Rind",["rubbed with paprika, oil or gofio"]]],
"Queijo Minas artesanal":[["Age",["frescal","meia-cura","curado"]]],
"Cotija":[["Age",["young","añejo"]],["Form",["grated"]]],
"Cantal & Salers":[["Maker",["fermier (farmhouse, raw milk)","laitier (dairy, pasteurised)"]],["Age",["young","entre-deux","aged"]]],
"Greek hard cheese":[["Milk",["sheep's","sheep and goat","cow's"]],["Status",["PDO"]],["Use",["for saganaki","grating"]]],
"Tulum & skin-ripened cheese":[["Skin or vessel",["goatskin","sheepskin","plastic barrel"]],["Milk",["sheep's","goat's"]]],
"Roomi":[["Milk",["cow's","buffalo"]],["Age",["young","aged"]],["Spice",["with peppercorns"]]],
"Feta":[["Texture",["firm (tangier)","soft (spreadable)","trímma (crumble)"]],["Maturing vessel",["barrel","metal vessel / tin"]],["Pack",["block in brine","vacuum pack"]]],
"Brined white cheese":[["Milk",["sheep's","goat's","cow's","buffalo","mixed"]],["Age",["fresh","matured"]],["Flavouring",["with herbs (otlu)"]],["Make",["UF (ultrafiltered)","feta-style"]]],
"Halloumi":[["Age",["fresh","mature (brined 40+ days)"]],["Milk",["goat & sheep","cow's-milk blend"]],["Fat level",["light"]],["Flavouring",["with mint","with chilli"]]],
"Grilling cheese":[["Format",["on skewers","baked disc","pan-fried slices"]],["Milk",["cow's","goat or sheep"]]],
"Qurut & jameed":[["Shape",["balls","strips","chunks"]],["Hardness",["soft to rock-hard"]],["Sweetness",["sweetened","unsweetened"]]],
"Kashk":[["Form",["liquid","dried (soak before use)","powder"]],["Base",["grain-based"]]],
"Aaruul":[["Sweetness",["sweetened","unsweetened"]],["Texture",["firm and chewy","soft and crumbly"]]],
"Chhurpi":[["Hardness",["soft","hard (dog chew)"]],["Milk",["yak","cow"]]],
"Processed cheese":[["Format",["slices","triangles","blocks","spread","cubes"]]],
"Cheese selection":[["Presentation",["gift box","cheese board","tasting set"]]],
"Hen's egg":[["Size grade",["small","medium","large","very large"]],["Housing",["caged / enriched colony","barn","free-range","organic","pasture-raised"]],["Shell colour",["white","brown","blue or green"]],["Breed",["breed egg"]],["Feed",["enriched (omega-3)"]],["Quality grade",["AA","A","B"]]],
"Eggs from other birds":[["Bird",["duck","quail","goose","guineafowl","ostrich","emu","pheasant"]]],
"Preserved egg":[["Preserving method",["clay-and-ash cured (century egg)","salt-cured (salted duck egg)","vinegar-pickled","tea-simmered (tea egg)","boiled in the shell"]]],
"Liquid & dried egg":[["Part of the egg",["whole","white","yolk"]],["Form",["liquid","frozen","dried powder"]]],
"Infant formula":[["Form",["powder","ready-to-feed"]],["Milk",["cow's","goat's"]],["Protein",["hydrolysed"]]],
"Follow-on formula":[["Form",["powder","ready-to-feed"]],["Milk",["cow's","goat's"]]],
"Growing-up milk":[["Form",["powder","ready-to-drink"]],["Milk",["cow's","goat's"]]],
"Oat drink":[["Intended use",["standard","barista"]],["Fat level",["light","whole"]],["Sweetness",["unsweetened","original"]],["Flavour",["flavoured"]],["Storage",["chilled","long-life"]],["Farming",["organic"]]],
"Soy drink":[["Sweetness",["unsweetened","original"]],["Flavour",["flavoured"]],["Fat level",["light"]],["Intended use",["barista"]],["Bean content",["whole-bean"]],["Farming",["organic"]]],
"Almond drink":[["Sweetness",["unsweetened","original"]],["Intended use",["barista"]],["Flavour",["flavoured"]],["Almond content",["high-almond (nuts and water only)"]]],
"Coconut drink":[["Sweetness",["original","unsweetened"]],["Storage",["chilled","long-life"]],["Blend",["coconut-almond"]]],
"Rice drink":[["Sweetness",["original"]],["Fortification",["fortified"]],["Flavour",["flavoured"]],["Blend",["rice-coconut"]],["Farming",["organic"]]],
"Pea drink":[["Sweetness",["original","unsweetened"]],["Intended use",["barista","kids"]],["Flavour",["chocolate"]]],
"Nut & seed drink":[["Nut",["cashew","hazelnut","walnut","peanut","macadamia"]],["Seed",["hemp","sesame","sunflower","flax"]],["Blend",["nut-and-seed blend"]]],
"Plant yoghurt":[["Base",["oat","soy","coconut","almond & nut"]],["Style",["Greek-style / strained"]],["Flavour",["plain","flavoured"]]],
"Plant cheese":[["Form",["block","slices","grated","soft / spreadable"]],["Base",["coconut oil and starch","cultured nut"]]],
"Plant cream":[["Use",["cooking","pouring","whipping"]],["Pack",["aerosol / squirty"]]],
"Plant creamer":[["Form",["liquid","powder"]],["Flavour",["unflavoured","flavoured"]]],
"Plant egg alternative":[["Form",["liquid scramble","powdered egg replacer"]],["Base",["mung bean","aquafaba (chickpea water)"]]],
"Tofu":[["Firmness",["silken (kinugoshi)","soft","firm (momen)","extra-firm (dougan)"]],["Processing",["smoked","marinated","thick fried (atsuage)","thin fried pouch (aburaage)","frozen (kōri-dōfu)","freeze-dried","thousand-layer sheet (baiye)"]],["Packing",["fresh chilled","aseptic shelf-stable"]],["Farming",["organic"]]],
"Tempeh":[["Bean or grain",["soy","other legume or grain (e.g. oat)"]],["Flavour",["plain","marinated"]],["Wrapping",["leaf-wrapped","plastic-wrapped"]],["Storage",["fresh","frozen","pasteurised"]]],
"Yuba":[["Condition",["fresh","dried"]],["Shape",["sheet","stick","knot","roll"]]],
}
missing=[n for n,k in kinds.items() if k.get('t') and n not in TT]
assert not missing,missing
for n,tt in TT.items():
    assert n in kinds,n
    k=kinds[n]; k['tt']=tt; k.pop('t',None)
# definition touch-ups
kinds['Flavoured milk drink']['n']='Flavoured milk'
kinds['Flavoured milk']=kinds.pop('Flavoured milk drink')
kinds['Flavoured milk']['a']=(kinds['Flavoured milk'].get('a','')+' · flavoured milk drink').strip(' ·')
kinds['Dulce de leche']['d']='Milk and sugar cooked down slowly into a thick caramel-coloured spread or sauce, known by regional names.'

# ---------- see links ----------
SEE={
"Pecorino":[["J7","Pecorino","same name, the white wine grape"]],
"Kumys":[["J3","Horse, donkey & yak milk","the mare's milk it is made from"]],
"Horse, donkey & yak milk":[["J3","Kumys","fermented mare's milk"]],
"Spreadable butter":[["J5","Margarine","plant-fat spread, not dairy"]],
"Butter":[["J3","Ghee & clarified butter","butter with the water and solids removed"]],
"Ghee & clarified butter":[["J3","Butter","the churned butter it is made from"],["J5","Coconut oil","non-dairy cooking fat"]],
"Coconut drink":[["J5","Coconut milk and cream","tinned coconut for cooking"]],
"Plant cream":[["J5","Coconut milk and cream","tinned coconut for cooking"]],
"Plant creamer":[["J3","Dairy creamer & whitener","the dairy version"]],
"Dairy creamer & whitener":[["J3","Plant creamer","the dairy-free version"]],
"Yoghurt":[["J8","Frozen yogurt","yoghurt sold frozen"],["J3","Plant yoghurt","the dairy-free version"]],
"Plant yoghurt":[["J3","Yoghurt","the dairy version"]],
"Kefir":[["J9","Water kefir","same culture idea, water not milk"]],
"Plant egg alternative":[["J3","Hen's egg","the egg it replaces"]],
"Plant cheese":[["J3","Processed cheese","the dairy product it imitates"]],
"Oat drink":[["J3","Cow's milk","the dairy milk it replaces"]],
"Cow's milk":[["J3","Oat drink","a plant alternative"]],
"Cream":[["J3","Half-and-half & light cream","lighter blend of milk and cream"],["J3","Plant cream","the dairy-free version"]],
"Half-and-half & light cream":[["J3","Cream","richer pouring and whipping cream"]],
"Skyr":[["J3","Quark & fromage blanc","also strained soured milk"]],
"Quark & fromage blanc":[["J3","Skyr","strained soured milk eaten with a spoon"],["J3","Cottage cheese","fresh curd of skimmed milk"]],
"Cottage cheese":[["J3","Quark & fromage blanc","smooth acid-set fresh cheese"]],
"Labneh":[["J3","Strained yoghurt","less strained yoghurt"]],
"Strained yoghurt":[["J3","Labneh","strained longer and salted"]],
"Cream cheese":[["J3","Mascarpone","richer Italian cream product"]],
"Mascarpone":[["J3","Cream cheese","tangier spreadable cheese"]],
"Munster":[["J3","Muenster (American)","mild American cheese with a similar name"]],
"Muenster (American)":[["J3","Munster","the pungent French washed-rind cheese"]],
"Brie":[["J3","Camembert","smaller bloomy-rind cheese of Normandy"]],
"Camembert":[["J3","Brie","larger bloomy-rind cheese of the Paris basin"]],
"Fresh goat's cheese":[["J3","Lactic goat cheese","the same milk, ripened"]],
"Lactic goat cheese":[["J3","Fresh goat's cheese","the same milk, eaten fresh"]],
"Halloumi":[["J3","Grilling cheese","other cheeses made to be fried"]],
"Grilling cheese":[["J3","Halloumi","the best-known grilling cheese"]],
"Feta":[["J3","Brined white cheese","other brined white cheeses"]],
"Brined white cheese":[["J3","Feta","the protected Greek brined cheese"]],
"Mozzarella":[["J3","Burrata & stracciatella","mozzarella filled with cream"]],
"Burrata & stracciatella":[["J3","Mozzarella","the pulled-curd cheese it is made from"]],
"Provolone & caciocavallo":[["J3","Scamorza & provola","smaller young pulled-curd cheeses"]],
"Scamorza & provola":[["J3","Provolone & caciocavallo","larger aged pulled-curd cheeses"]],
"Gruyère":[["J3","Emmental","Swiss cheese with holes"]],
"Emmental":[["J3","Gruyère","Swiss cheese without holes"]],
"Parmigiano Reggiano & grana":[["J3","Pecorino","sheep's-milk grating cheese"]],
"Cheddar":[["J3","Colby","American cousin made by washing the curd"]],
"Colby":[["J3","Cheddar","the cheese it is derived from"]],
"Paneer & chhena":[["J3","Queso fresco & fresh white cheese","similar fresh pressed curd"]],
"Queso fresco & fresh white cheese":[["J3","Paneer & chhena","similar fresh pressed curd"]],
"Infant formula":[["J3","Milk powder","ordinary milk powder is not formula"]],
"Milk powder":[["J3","Infant formula","a regulated baby formula"]],
"Evaporated & condensed milk":[["J3","Dulce de leche","condensed milk cooked to caramel"]],
"Dulce de leche":[["J3","Evaporated & condensed milk","the uncooked tinned milks"]],
"Natto":[["J3","Tempeh","also fermented soya"]],
"Tempeh":[["J3","Natto","also fermented soya"]],
"Soy drink":[["J3","Tofu","made from the same milk"]],
"Tofu":[["J3","Soy drink","the milk it is curdled from"]],
"Goat's milk":[["J3","Fresh goat's cheese","the cheese made from it"]],
"Crème fraîche":[["J3","Soured cream & smetana","sourer, thinner cultured cream"]],
"Soured cream & smetana":[["J3","Crème fraîche","richer, milder cultured cream"]],
"Drinking yoghurt & ayran":[["J3","Buttermilk","also a thin sour drink"]],
"Buttermilk":[["J3","Drinking yoghurt & ayran","thinned yoghurt drinks"]],
"Khoa & mawa":[["J3","Dulce de leche","also milk cooked down with sugar"]],
}
import glob
ext={}
for f in glob.glob(R+'reader/J*.json'):
    r=json.load(open(f))
    ext[r['c']]={k['n'] for dp in r['depts'] for s in dp['s'] for k in s['k']}
for n,sv in SEE.items():
    assert n in kinds,n
    for c,t,w in sv:
        if c=='J3': assert t in kinds,(n,t)
        else: assert t in ext[c],(n,t)
    kinds[n]['see']=sv

# ---------- rebuild structure ----------
def SH(n,t,ax,order=None,newname=None):
    s=shelves[n]; s['t']=t
    if ax: s['ax']=ax
    if order:
        byn={k['n']:k for k in s['k']}
        for nm in order:
            if nm not in byn: byn[nm]=kinds[nm]
        assert set(byn)==set(order),(n,set(byn)^set(order))
        s['k']=[byn[nm] for nm in order]
    if newname: s['n']=newname
    return s
def kn(nm): return nm

SH('Milk',"Liquid milk of any dairy animal, plain or sweetened and flavoured, sold to drink; cultured milks → Yoghurt & fermented milks, plant drinks → Dairy-free alternatives.",
   "kinds by the animal it comes from, the commonest first, then flavoured milk",
   ["Cow's milk","Goat's milk","Sheep's milk","Buffalo milk","Camel milk","Horse, donkey & yak milk","Flavoured milk"])
SH('Cream',"Cream separated from milk or cultured from it, to pour, whip or spoon, and the whiteners sold in its place; butter → Butter & ghee.",
   "kinds by how thick or cultured the cream is, from pouring cream to spoonable soured cream, then creamers",
   ["Cream","Half-and-half & light cream","Clotted cream & kaymak","Crème fraîche","Soured cream & smetana","Dairy creamer & whitener"])
SH('Tinned & dried milk',"Milk with water taken out or cooked away: evaporated and condensed milk, milk powder, milk solids and dulce de leche; fresh and long-life milk → Milk shelf.",
   "kinds by how far the milk is cooked down: tinned, dried to powder, cooked to solids, cooked to caramel",
   ["Evaporated & condensed milk","Milk powder","Khoa & mawa","Dulce de leche"],newname='Concentrated & dried milk')
SH('Butter & ghee',"Milk fat for spreading, baking and frying: churned butter, clarified ghee and butter blended with oil; margarine and plant spreads → J5.",None)
SH('Yoghurt',"Spoonable cultured milk from set and stirred yoghurt to strained yoghurt, skyr and labneh; fresh cheeses such as quark → Fresh & whey cheese.",
   "kinds by how much whey is drained off: set or stirred yoghurt, strained, skyr, labneh")
SH('Fermented milk drinks',"Thin cultured milks drunk cold, from thinned yoghurt and buttermilk to kefir, kumys and probiotic bottles; spoonable yoghurts → Yoghurt shelf.",
   "kinds by what is cultured and how: thinned yoghurt, churning leftover, soured whole milk, kefir grains, a named strain, mare's milk, baked milk",
   ["Drinking yoghurt & ayran","Buttermilk","Soured milk","Kefir","Probiotic cultured drink","Kumys","Ryazhenka"])

SH('Fresh & whey cheese',"Unripened cheese eaten within days: cream cheese, mascarpone, quark, cottage cheese, paneer, ricotta; rind-ripened cheeses → Soft white-rind cheese, brined white cheeses → Feta, brined & grilling cheese.",
   "kinds by how the fresh curd is set: enriched with cream, soured and strained, pressed from drained curd, then made from whey",
   ["Cream cheese","Mascarpone","Fresh soft cheese","Crescenza & stracchino","Fresh goat's cheese","Quark & fromage blanc","Cottage cheese","Cheese curds","Queso fresco & fresh white cheese","Paneer & chhena","Ricotta & whey cheese","Brunost"])
SH('Soft white-rind cheese',"Soft cheeses ripened from the outside by a white mould: Brie, Camembert, double- and triple-creams and lactic goat cheeses; washed rinds → Washed-rind cheese.",
   "kinds by the paste under the white rind: rennet-set cow's-milk wheels, cream-enriched cheeses, then slow acid-set goat curd")
SH('Washed-rind cheese',"Soft to semi-hard cheeses whose rind is washed in brine, beer or spirit, giving an orange rind and a strong smell: Époisses, Munster, Reblochon, Taleggio; white-mould rinds → Soft white-rind cheese.",
   "kinds by origin and tradition: France and Italy first, then monastery, German and Low Countries, American, then new farmhouse makers",
   ["Époisses","Munster","Reblochon","Taleggio","Vacherin Mont-d'Or","Pont-l'Évêque & Livarot","Maroilles","Saint-Nectaire","Monastery cheese","Limburger & Herve","Tilsit","Harzer & sour-milk cheese","Muenster (American)","Farmhouse washed-rind cheese"])
SH('Blue cheese',"Cheeses veined with blue mould: Roquefort, Stilton, Gorgonzola, Cabrales, soft blues and farmhouse blues; blue-flavoured processed cheese → Processed cheese & selections.",
   "kinds by the great blue families first, then regional, soft and farmhouse blues")
SH('Alpine cheese',"Firm cooked-pressed and semi-hard cheeses of the Alps and Jura, made in large wheels: Gruyère, Comté, Emmental, Appenzeller, Raclette; Italian grana → Italian grana, pecorino & pressed cheese.",
   "kinds by size and make, from large cooked-pressed wheels to small semi-hard mountain cheeses")
SH('Cheddar & British cheese',"Pressed cow's-milk cheeses of the cheddar type, the British county cheeses and their American cousins: Cheddar, Cheshire, Lancashire, Red Leicester, Colby; blues such as Stilton → Blue cheese.",
   "kinds by family: cheddar first, then the British county cheeses, then American cheddar cousins, then new farmhouse cheeses")
SH('Italian grana, pecorino & pressed cheese',"Hard grating cheeses of the grana type and the pressed cow's-milk cheeses of northern Italy: Parmigiano Reggiano, Grana Padano, Asiago, Piave; pecorino → Sheep's-milk pressed cheese.",
   "kinds by hardness and age, from grana grating cheeses to semi-hard mountain cheeses")
SH('Pressed uncooked sheep cheese',"Firm pressed cheeses made of sheep's milk: Manchego, Ossau-Iraty, Pecorino Romano, Idiazábal, Oscypek; sheep's-milk blue and brined cheeses → Roquefort, Feta.",
   "kinds by region, Spain and the Pyrenees first, then Italy, then central Europe and the Adriatic",
   ["Manchego","Idiazábal & Roncal","Zamorano","Pyrenean sheep cheese","Pecorino","Oscypek","Pag cheese"],newname="Sheep's-milk pressed cheese")
SH('Dutch & Nordic cheese',"Round and block semi-hard cheeses of the Low Countries and Scandinavia: Gouda, Edam, Havarti, Jarlsberg, Danbo; cheddar types → Cheddar & British cheese.",
   "kinds by country and family, Dutch rind cheeses first, then Danish, Norwegian and Swedish")
SH('Spanish, Portuguese & Latin American cheese',"Cheeses of Iberia and Latin America outside the sheep's-milk press: Mahón, Tetilla, torta cheeses, Portuguese cured cheeses, Queijo Minas, Cotija; Manchego → Sheep's-milk pressed cheese.",
   "kinds by country, Spain first, then Portugal, then Brazil and Mexico")
SH('Regional pressed cheese',"Pressed cheeses of one region that fit no wider family: Cantal, Greek graviera, Tulum, Roomi, Mimolette.",
   "kinds by country, France first, then Greece, Turkey and Egypt")
SH('Stretched-curd cheese',"Cheeses whose scalded curd is kneaded and pulled: mozzarella, burrata, provolone, scamorza, kashkaval, string cheese; brined white cheeses → Feta, brined & grilling cheese.",
   "kinds by age and form: fresh mozzarella and burrata, aged provolone, small scamorza, then Balkan and Caucasian pulled cheeses")
SH('Feta, brined & grilling cheese',"Cheeses salted and kept in brine, and cheeses made to be fried or grilled: feta, other white cheeses, halloumi; fresh unsalted curd → Fresh & whey cheese.",
   "kinds by how the curd is salted and used: protected feta, other brined white cheeses, scalded halloumi, grilling cheeses")
SH('Dried cheese & curd',"Hard dried curd and sour-milk cheese of Central Asia, the Middle East and the Himalaya: qurut, kashk, aaruul, chhurpi.",
   "kinds by region of the drying tradition, from the Middle East and Iran to Mongolia and the Himalaya")
SH('Processed cheese & selections',"Cheese melted with emulsifying salts and re-formed into slices, spreads or blocks, and boxed assortments of several cheeses; natural cheeses → their make-family shelves.",None)
SH('Eggs',"Hen's eggs by size and housing, eggs of other birds, preserved eggs and liquid or dried egg; egg dishes are not products here.",
   "kinds by how the egg is sold: hen's egg in the shell, another bird's, preserved, or out of the shell")
SH('Formula & toddler milk',"Breast-milk substitutes and fortified milks for babies and young children; ordinary milk powder → Concentrated & dried milk.",None)
SH('Plant drinks',"Drinks made by blending a plant with water and straining, sold in place of milk: oat, soy, almond, coconut, rice, pea and others; tinned coconut milk for cooking → J5.",
   "kinds by the plant base, the best-selling first: oat, soy, almond, coconut, rice, pea, then nuts, seeds and other plants",
   ["Oat drink","Soy drink","Almond drink","Coconut drink","Rice drink","Pea drink","Nut & seed drink","Grain, tuber & fruit drink"])
SH('Plant yoghurt, cheese, cream & egg',"Plant products sold in place of yoghurt, cheese, cream, creamer and egg; plant drinks → Plant drinks shelf, tofu → Tofu, tempeh & yuba.",
   "kinds by the dairy or egg product they replace: yoghurt, cheese, cream, creamer, egg")
SH('Tofu, tempeh & yuba',"Foods made from soya beans by curdling, mould fermentation, skimming or whole-bean fermenting; soy milk → Soy drink, plant meat → J1.",
   None)
shelves['Tofu, tempeh & yuba']['ax']="kinds by how the bean is set: curdled and pressed, bound by mould, skimmed from hot milk, fermented whole"

# cheese departments
cheese=depts['Cheese']
bl=cheese['b']
def pick(*ms): return [b for b in bl if b['m'] in ms]
sh=lambda *ns:[shelves[n] for n in ns]
cheese_depts=[
 dict(n='Fresh, soft & blue cheese',mode='variety',
  note=cheese['note'],b=bl,
  t="Cheese eaten fresh, ripened soft from the rind inwards, or veined with blue mould; firm pressed wheels → Pressed & hard cheese, pulled, brined or dried cheese → Stretched, brined & dried cheese.",
  ax="How is the curd ripened: eaten fresh, ripened from the rind by white mould or washing, or veined inside with blue mould?",
  s=sh('Fresh & whey cheese','Soft white-rind cheese','Washed-rind cheese','Blue cheese')),
 dict(n='Pressed & hard cheese',mode='variety',
  note='Make tradition (shelf) → kind → named or protected-origin cheese (archetype) → producer or affineur (version) → age, milk and size (detail).',
  b=pick('Where the milk comes from','Maker and affineur','Protected origin (PDO / AOP / PGI)','Consortium grades','Award medal'),
  t="Firm to hard cheeses whose curd is pressed into wheels and aged, from Alpine and cheddar types to grana, sheep's-milk and regional cheeses; fresh, soft or blue cheese → Fresh, soft & blue cheese.",
  ax="Which pressed-cheese tradition does it follow: Alpine cooked-pressed, British cheddar, Italian grana, sheep's-milk press, Dutch and Nordic, Iberian, or another regional press?",
  s=sh('Alpine cheese','Cheddar & British cheese','Italian grana, pecorino & pressed cheese','Pressed uncooked sheep cheese','Dutch & Nordic cheese','Spanish, Portuguese & Latin American cheese','Regional pressed cheese')),
 dict(n='Stretched, brined & dried cheese',mode='variety',
  note='Same path as the other cheese departments: make family, kind, named or protected-origin cheese, producer, age.',
  b=pick('Where the milk comes from','Protected origin (PDO / AOP / PGI)','Award medal'),
  t="Cheese whose curd is pulled, kept in brine, dried, or melted and re-formed, plus boxed selections; pressed wheels → Pressed & hard cheese.",
  ax="How is the curd worked after it sets: pulled and kneaded, salted in brine, dried hard, or melted and re-formed?",
  s=sh('Stretched-curd cheese','Feta, brined & grilling cheese','Dried cheese & curd','Processed cheese & selections')),
]
# put them in place of Cheese
new=[]
for dp in d['depts']:
    if dp['n']=='Cheese': new+=cheese_depts
    else: new.append(dp)
d['depts']=new
# non-cheese dept texts
def D(n,t,ax):
    depts[n]['t']=t; depts[n]['ax']=ax
D('Milk & cream',"Milk, cream and their tinned or dried forms, bought to drink, cook with or whiten drinks; cultured milks → Yoghurt & fermented milks, churned fat → Butter & ghee, plant drinks → Dairy-free alternatives.",
  "How far has the milk been changed from the animal's milk: drunk as it comes, separated into cream, or cooked down and dried to keep?")
D('Butter & ghee',"Milk fat sold as a spread or cooking fat: churned butter, clarified ghee and butter blended with oil; margarine and oils → J5.",
  "How has the milk fat been treated: churned whole, clarified to pure fat, or blended with vegetable oil?")
D('Yoghurt & fermented milks',"Milk soured with a culture, spooned or drunk; soured cream → Cream shelf, fresh quark and cottage cheese → Fresh, soft & blue cheese.",
  "Is the cultured milk eaten with a spoon or drunk, and how much whey has been drained from it?")
D('Eggs',"Bird eggs in the shell, preserved, or out of the shell as liquid or powder; plant stand-ins → Dairy-free alternatives.",
  "How is the egg sold: hen's egg in the shell, another bird's, preserved, or out of the shell?")
D('Baby & toddler milks',"Formula and fortified milks for babies and young children; ordinary milk powder → Milk & cream.",
  "How old is the child: from birth, from about six months or from about one year?")
D('Dairy-free alternatives',"Plant products sold in place of milk, yoghurt, cheese, cream and egg; tofu and tempeh → Tofu, tempeh & yuba, plant meat → J1.",
  "Which dairy or egg product does it replace: the milk drink, or yoghurt, cheese, cream and egg?")
D('Tofu, tempeh & yuba',"Foods made from soya beans by curdling, skimming or fermenting, eaten as protein; soy milk → Dairy-free alternatives, plant meat → J1.",
  "How is the soya bean set: curdled and pressed, bound by mould, skimmed from hot milk, or fermented whole?")
# butter shelf is 3 kinds; ensure all shelves have t
d['ax']="What is it made of and how: milk as it comes, a cultured or churned milk, cheese, egg, a baby formula, a plant stand-in, or soya curd?"
d['key']=[
 "1. Is it formula or fortified milk made for a baby or young child? → Baby & toddler milks",
 "2. Is it a bird's egg, in the shell, preserved or out of the shell? → Eggs",
 "3. Is it made from soya beans by curdling, skimming or fermenting, such as tofu, tempeh, yuba or natto? → Tofu, tempeh & yuba",
 "4. Is it a plant-based stand-in for milk, yoghurt, cheese, cream or egg? → Dairy-free alternatives",
 "5. Is it cheese eaten fresh, ripened soft from the rind, or veined with blue mould? → Fresh, soft & blue cheese",
 "6. Is it cheese pressed into a firm or hard wheel? → Pressed & hard cheese",
 "7. Is it cheese that is pulled, kept in brine, dried, or melted and re-formed? → Stretched, brined & dried cheese",
 "8. Is it milk fat churned into butter or clarified into ghee? → Butter & ghee",
 "9. Is it milk soured with a culture, to spoon or to drink? → Yoghurt & fermented milks",
 "10. Is it liquid milk, cream, or milk cooked down, tinned or dried? → Milk & cream",
 "<i>Precedence: soured cream is cream (step 10), not a fermented milk; a plant drink is dairy-free (step 4) even when sold beside milk; tofu is soya (step 3) before plant stand-ins; dishes made with dairy belong to the culinary taxonomy.</i>"]
d['lead']="Dairy products, eggs and their plant-based alternatives. Everyday milk, cream, butter, eggs and plant drinks are kept to the right kind and what makes a good one, while cheese, the enthusiast area, is split into three departments by how the curd is made, then by make family, named or protected-origin cheese, producer or affineur, and age."

# ---------- write ----------
tmp=R+'out/J3.json.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,R+'out/J3.json')
json.dump({"Flavoured milk drink":"Flavoured milk"},open(R+'out/J3_renames.json','w'),ensure_ascii=False,indent=1)
after=dict(depts=len(d['depts']),shelves=sum(len(x['s']) for x in d['depts']),kinds=sum(len(s['k']) for x in d['depts'] for s in x['s']),arch=sum(len(k.get('x',[])) for x in d['depts'] for s in x['s'] for k in s['k']))
print(stats_before,after)
print(len(demoted),'demoted');print('\n'.join(demoted))
open(R+'work/STR_J3/demoted.txt','w').write('\n'.join(demoted))
