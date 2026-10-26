import json, os
W='https://en.wikipedia.org/wiki/'
FR='https://fr.wikipedia.org/wiki/'
def A(n,d,s,mk="",y="",a="",v=None,dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or []}
    if dt: x["dt"]=dt
    return x
def V(n,mk="",y="",d=""):
    o={"n":n}
    if mk:o["mk"]=mk
    if y:o["y"]=y
    if d:o["d"]=d
    return o
EP=W+'%C3%89poisses'; EPFR=FR+'Époisses_(fromage)'
kinds=[]
kinds.append({"n":"Époisses","a":"Époisses de Bourgogne · Burgundian washed-rind cheese · Langres · Soumaintrain",
 "d":"Small, soft, pungent Burgundian and Champagne cow's-milk cheeses with a sticky orange rind washed in brine or marc.",
 "t":["raw milk","pasteurised","farmhouse (fermier)","dairy (laitier)","small (c. 250 g)","large (c. 18 cm)"],
 "s":"https://franschhoek.org.za/artisan/dalewood-fromage/",
 "x":[
  A("Époisses PDO","Smear-ripened Burgundian cheese washed in brine and marc de Bourgogne; the reference strong washed-rind cheese.",EP,y="AOC 1991, AOP 1996",a="Époisses de Bourgogne",
    v=[V("Époisses (Berthaut)","Fromagerie Berthaut",d="Dairy in the village of Époisses (Savencia group)."),
       V("Époisses (Gaugry)","Fromagerie Gaugry",d="Dairy at Brochon (Lincet group)."),
       V("Époisses (Germain)","Fromagerie Germain",d="Dairy at Chalancey (Triballat Rians)."),
       V("Époisses fermier","GAEC des Marronniers",d="The one farmhouse producer, at Origny.")],
    dt="c. 10 cm (c. 250 g) or c. 18 cm · raw or pasteurised · rind washed with marc · no colourants"),
  A("L'Ami du Chambertin","Burgundian marc-washed cheese created by Raymond Gaugry at Brochon; a commercial cousin of Époisses.",FR+'Ami_du_Chambertin',mk="Fromagerie Gaugry",y="1950",
    dt="cylinder c. 9 × 4 cm · 200 g"),
  A("Affidélice","Burgundian commercial washed-rind cheese whose rind is washed with Chablis.",EPFR),
  A("Langres PDO","Small cylinder from the Langres plateau with an orange rind and a hollow top (the fontaine); milder than Époisses.",W+'Langres_cheese',y="AOC 1991",
    v=[V("Langres PDO",d="Old data.")],dt="c. 180 g cylinder · about 5 weeks ageing · rind coloured with annatto"),
  A("Soumaintrain PGI","Brine-washed cheese from Soumaintrain in the Yonne, with its own protected geographical indication.",W+'Soumaintrain',
    v=[V("Soumaintrain PGI",d="Old data.")])
 ]})
kinds.append({"n":"Munster","a":"Munster-Géromé · Minschterkaas · petit-munster",
 "d":"Soft, strong-smelling washed-rind cow's-milk cheese from the Vosges, ripened in humid cellars.",
 "t":["standard (450 g–1.5 kg)","petit-munster (from 120 g)","farmhouse (fermier)","dairy (laitier)","raw milk"],
 "s":W+'Munster_cheese',
 "x":[A("Munster PDO","Vosges cheese named after the Alsatian town of Munster, where monks matured it; Géromé is the Lorraine name from Gérardmer.",W+'Munster_cheese',y="AOC 1969, AOP 1996",a="Munster-Géromé PDO",
    v=[V("Munster; Munster-Géromé PDO",d="Old data."),V("Petit-Munster",d="Smaller format, 7–12 cm, ripened at least 14 days."),V("Munster fermier",d="Farm-made in the Vosges; about 6% of output (2017).")],
    dt="13–19 cm, 450 g–1.5 kg · at least 21 days ripening · rubbed and turned every two days")]})
kinds.append({"n":"Reblochon","a":"Reblochon de Savoie · petit reblochon · Chevrotin",
 "d":"Soft washed-rind raw-milk cheese of the Savoy Alps, sold as farmhouse (green tag) or dairy (red tag).",
 "t":["fermier (green casein tag)","laitier (red casein tag)","standard (450–550 g)","petit reblochon (240–280 g)"],
 "s":W+'Reblochon',
 "x":[A("Reblochon PDO","Raw cow's-milk cheese first made in the Thônes and Arly valleys of the Aravis massif.",W+'Reblochon',y="AOC 1958",a="Reblochon de Savoie",
    v=[V("Reblochon fermier",d="One herd's raw milk, made on the farm after each milking; green tag."),V("Reblochon laitier",d="Pooled milk made in a dairy (fruitière); red tag."),
       V("Petit reblochon",d="c. 9 cm, 240–280 g."),V("Reblochon; Reblochon de Savoie PDO",d="Old data."),
       V("Dunnes Stores Simply Better French Reblochon De Savoie PDO","Dunnes Stores",d="Retailer own label (old data).")],
    dt="c. 14 cm, 450–550 g · raw cow's milk · Haute-Savoie and parts of Savoie"),
  A("Rebruchon and Reblò alpino","Italian Alpine cheeses of Reblochon type, sold under these names after Italian production of Reblochon ended in 1964.",W+'Reblochon'),
  A("Chevrotin PDO","Soft goat's-milk cheese of Savoy made like Reblochon.",W+'Chevrotin',y="AOC 2002",v=[V("Chevrotin PDO",d="Old data.")]),
  A("Abbaye de Tamié","Reblochon-style raw cow's-milk cheese made only by the monks of Tamié Abbey near Albertville.",W+'Abbaye_de_Tami%C3%A9')]})
kinds.append({"n":"Taleggio","a":"Taleggio DOP · Quartirolo Lombardo",
 "d":"Square, semi-soft Italian washed-rind cow's-milk cheese with a thin pinkish rind and a mild, fruity paste.",
 "t":["whole square","portion","raw milk","pasteurised"],
 "s":W+'Taleggio_cheese',
 "x":[A("Taleggio PDO","Washed-rind cheese named after Val Taleggio; PDO cheese must come from Lombardy or Piedmont.",W+'Taleggio_cheese',
    v=[V("Taleggio DOP","Caseificio Taddei S.r.l.",d="Old data."),V("Taleggio PDO",d="Old data.")],dt="square · pinkish-brown rind · creamy pale yellow paste"),
  A("Quartirolo Lombardo PDO","Soft Lombard cow's-milk cheese with PDO status.",W+'Quartirolo_lombardo',v=[V("Quartirolo Lombardo PDO",d="Old data.")])]})
VMO=W+'Vacherin_Mont_d%27Or'
kinds.append({"n":"Vacherin Mont-d'Or","a":"Mont d'Or · Vacherin du Haut-Doubs · spruce-bark cheese",
 "d":"Seasonal soft washed-rind cow's-milk cheese of the Jura, girdled with spruce bark and eaten with a spoon.",
 "t":["boxed whole cheese","French or Swiss origin"],
 "s":VMO,
 "x":[A("Mont d'Or (Vacherin du Haut-Doubs) PDO","French version from the Haut-Doubs, wrapped in a strap of Norway spruce cambium.",VMO,a="Mont d'Or AOP",v=[V("Mont d'Or; Vacherin du Haut-Doubs PDO",d="Old data.")],
    dt="seasonal · spruce strap · greyish-yellow washed rind"),
  A("Vacherin Mont-d'Or AOP","Swiss version from the Vaud Jura, sold locally simply as Vacherin.",VMO,v=[V("Vacherin Mont-d'Or AOP",d="Old data.")]),
  A("Winnimere","Raw-milk spruce-wrapped washed-rind cheese made in winter from hay-fed Ayrshire milk in Vermont.","https://www.jasperhillfarm.com/winnimere",mk="Jasper Hill Farm",
    dt="13 oz wheel · 60 days · washed in cultured brine · spruce cambium strips"),
  A("Rush Creek Reserve","Wisconsin raw-milk cheese in the style of Vacherin Mont d'Or, wrapped in spruce bark and made only in autumn.","https://culturecheesemag.com/cheese-library/rush-creek-reserve",mk="Uplands Cheese Company",y="2010",
    v=[V("Rush Creek Reserve","Uplands Cheese Company",y="2010",d="Made by Andy Hatch from the farm's own herd; washed with Pleasant Ridge mother culture.")],
    dt="c. 4 in wheel · made September–November · released after at least two months")]})
kinds.append({"n":"Pont-l'Évêque & Livarot","a":"Norman washed-rind cheese · Pont-l'Évêque · Livarot · colonel",
 "d":"Soft washed-rind cow's-milk cheeses of the Pays d'Auge in Normandy: the square Pont-l'Évêque and the reed-banded Livarot.",
 "t":["raw milk","pasteurised","full size","half or small formats"],
 "s":W+'Pont-l%27%C3%89v%C3%AAque_cheese',
 "x":[A("Pont-l'Évêque PDO","Square, unpressed cow's-milk cheese from around Pont-l'Évêque; probably the oldest Norman cheese still made.",W+'Pont-l%27%C3%89v%C3%AAque_cheese',v=[V("Pont-l'Évêque PDO",d="Old data.")],dt="c. 10 cm square, 3 cm high, 400 g · white to orange-brown rind"),
  A("Livarot PDO","Pungent Normande-milk cheese wrapped in three to five bands of dried reedmace, hence the nickname colonel.",W+'Livarot_cheese',y="AOC 1975",v=[V("Livarot PDO",d="Old data.")],dt="cylinder, usually 450 g, other weights · orange rind · reed or paper bands")]})
kinds.append({"n":"Maroilles","a":"Marolles · Sorbais · Rollot · Bergues",
 "d":"Square, moist, orange-rinded cow's-milk cheeses of northern France with a strong smell, led by Maroilles.",
 "t":["Maroilles (c. 700 g)","Sorbais (3/4 size)","smaller regulated sizes"],
 "s":W+'Maroilles_cheese',
 "x":[A("Maroilles PDO","Rectangular washed-rind cheese named after the village of Maroilles; sold in four regulated sizes.",W+'Maroilles_cheese',a="Marolles",
    v=[V("Maroilles / Marolles PDO",d="Old data."),V("Sorbais",d="12–12.5 cm square, 4 cm high, 550 g.")],dt="c. 13 cm square, 6 cm high, c. 700 g · moist orange-red rind"),
  A("Rollot","Round or heart-shaped Picardy cheese washed in salted water and cellar-aged three to six weeks.",FR+'Rollot_(fromage)',dt="c. 8–9 cm, c. 300 g · orange rind"),
  A("Bergues","Farmhouse raw-milk cheese from around Bergues near Dunkirk, washed regularly with beer.",FR+'Bergues_(fromage)',y="recorded 1554",dt="c. 20 cm · at least three weeks in a raised cellar"),
  A("Vieux-Boulogne","Unpasteurised, unpressed Pas-de-Calais cheese developed in 1982 by Antoine Bernard and Philippe Olivier.",W+'Vieux-Boulogne',y="1982",a="Sablé du Boulonnais",
    v=[V("Vieux-Boulogne","Philippe Olivier",y="1982",d="Developed with Antoine Bernard.")])]})
kinds.append({"n":"Saint-Nectaire","a":"Saint-Nectaire fermier · Saint-Nectaire laitier",
 "d":"Cow's-milk cheese of the Auvergne in central France, made there since at least the 17th century.",
 "t":["fermier (farmhouse)","laitier (dairy)"],
 "s":W+'Saint-Nectaire',
 "x":[A("Saint-Nectaire PDO","Auvergne cheese made since at least the 17th century.",W+'Saint-Nectaire',v=[V("Saint-Nectaire PDO",d="Old data.")])]})
kinds.append({"n":"Monastery cheese","a":"Trappist cheese · abbey cheese · Port-Salut · Saint-Paulin · Esrom · Oka",
 "d":"Semi-soft, mild, washed-rind cow's-milk cheeses first made by Trappist and other monks, now also by large dairies.",
 "t":["abbey-made","dairy-made","pasteurised","raw milk"],
 "s":W+'Port_Salut',
 "x":[A("Port Salut","Mild orange-rinded wheel developed by Trappist monks in the 19th century at Port-du-Salut Abbey in Entrammes.",W+'Port_Salut',y="19th century",dt="c. 23 cm, c. 2 kg · pasteurised · orange rind"),
  A("Saint-Paulin","Mild, sliceable semi-soft cheese first made by Trappist monks; a cousin of Port Salut.",W+'Saint-Paulin_cheese',dt="round loaf · c. four weeks · brine-washed rind with annatto"),
  A("Esrom PGI","Danish Trappist-style semi-soft cheese, also called Danish Port Salut.",W+'Esrom',a="Danish Port Salut",v=[V("Esrom PGI",d="Old data.")]),
  A("Oka","Semi-soft washed-rind cheese first made by Trappist monks at Oka, Quebec; recipe sold to Agropur in 1981.",W+'Oka_cheese',mk="Agropur",
    v=[V("Oka","Agropur",y="1981",d="Commercial production after the sale by Les Pères Trappistes.")]),
  A("Chimay","Cheeses made by Scourmont Abbey, the Trappist monastery behind Chimay beer, in four varieties.",W+'Chimay_Brewery'),
  A("Mont des Cats","Trappist cheese made at Mont des Cats abbey since 1890, washed with annatto-coloured brine.",W+'Mont_des_Cats_cheese',y="1890",dt="at least two months · 50% fat"),
  A("Chaumes","Soft Trappist-style cheese from Saint-Antoine-de-Breuilh in the Périgord.",W+'Chaumes'),
  A("Brick","Wisconsin cheese pressed into brick shape, mild when young and stronger and nuttier when aged.",W+'Brick_cheese',dt="brick shape · pale yellow to white paste · orange rind")]})
kinds.append({"n":"Limburger & Herve","a":"Limburger · Herve · Remoudou · Romadur · Rommedoe · Weisslacker",
 "d":"Small, strong-smelling smear-ripened cow's-milk cheeses of the Limburg tradition, from Belgian Herve to Allgäu Romadur.",
 "t":["mild (doux)","sharp (piquant)","stick or brick shape","fat levels 20–60% in dry matter"],
 "s":"https://www.webstaurantstore.com/country-castle-8-oz-limburger-cheese-by-chalet-cheese-co-op-case/875RE775842.html",
 "x":[A("Fromage de Herve PDO","Belgium's only PDO cheese, from the Pays de Herve, where the Limburger type began; sold mild or sharp.",FR+'Fromage_de_Herve',y="AOP 1996",a="Herve · Remoudou",
    v=[V("Herve doux",d="Ripened 4–5 weeks."),V("Herve piquant",d="Ripened 7–8 weeks, salted more."),V("Remoudou",d="Richer, creamier variant."),V("Fromage de Herve PDO",d="Old data.")],dt="cube or block, 50–400 g"),
  A("Limburger","Smear-ripened cheese of the old Duchy of Limburg, known for the smell of Brevibacterium linens; made widely in Germany and the US.",W+'Limburger',
    v=[V("St Mang Original Allgäuer Limburger",d="Old data."),V("Country Castle Limburger","Chalet Cheese Co-op",d="Wisconsin (old data).")]),
  A("Romadur","Smaller, milder stick-shaped red-smear cheese introduced to the Allgäu by Carl Hirnbein.",'https://de.wikipedia.org/wiki/Romadur',
    dt="80–180 g sticks · 20, 40 or 60% fat in dry matter"),
  A("Liederkranz","American recreation of Limburger created in 1891 by Emil Frey in Monroe, New York.",W+'Liederkranz_cheese',y="1891"),
  A("Weisslacker","Salted, whitish surface-ripened German cheese related to Limburger, ripened seven months; also called Bierkäse.",W+'Weisslacker',a="Bierkäse · beer cheese")],
 "m":[["Odenwälder Frühstückskäse PDO",""]]})
kinds.append({"n":"Tilsit","a":"Tilsiter · Holsteiner Tilsiter",
 "d":"Semi-hard smear-ripened cheese with small holes, first made in mid-19th-century Tilsit by Swiss settlers.",
 "t":["mild","matured","with caraway"],
 "s":"https://foodcom.pl/en/products/tilsiter-cheese/",
 "x":[A("Tilsiter","Pale yellow smear-ripened cheese created by the Westphal family, Swiss settlers in Tilsit, East Prussia.",W+'Tilsit_cheese',y="mid-19th century",
    v=[V("Holsteiner Tilsiter PGI",d="Old data.")],dt="medium-firm paste with small irregular holes")]})
kinds.append({"n":"Harzer & sour-milk cheese","a":"sour-milk cheese · Handkäse · Olomoucké tvarůžky · Graukäse · gamalost · pultost",
 "d":"Small cheeses of ripened acid curd (quark) made without rennet, ripened with a smear or mould to a pungent, translucent body.",
 "t":["yellow (red-smear)","white (mould-ripened)","with caraway","roll or stick"],
 "s":"https://www.rohlik.cz/1331433-a-w-olomoucke-tvaruzky-1",
 "x":[A("Harzer","German sour-milk cheese of low-fat curd from the Harz, sold as small rounds (Taler) or sticks, often in a roll.",W+'Harzer',
    v=[V("Harzer Käse",d="Old data."),V("Harzer Rolle",d="Small rounds packed in a cylinder.")],dt="round (Handkäse, Taler) or stick (Stangenkäse) · caraway · white or red mould"),
  A("Olomoucké tvarůžky","Ripened soft sour-milk cheese made in Loštice and named after Olomouc, where it was sold.",W+'Olomouck%C3%A9_tvar%C5%AF%C5%BEky',a="Olmützer Quargel · tvargle",v=[V("Olomoucké tvarůžky",d="Old data.")]),
  A("Handkäse","Hand-formed sour-milk cheese of southern Hesse, eaten as Handkäse mit Musik with onions.",W+'Handk%C3%A4se',v=[V("Hessischer Handkäse / Hessischer Handkäs PGI",d="Old data.")]),
  A("Nieheimer","Westphalian sour-milk cheese with caraway, dried under straw and ripened in casks packed with hops.",W+'Nieheimer',v=[V("Nieheimer Käse PGI",d="Old data.")]),
  A("Tiroler Graukäse PDO","Rennet-free, very low-fat acid-curd cheese of the Tyrolean valleys, named after its grey mould.",W+'Tyrolean_grey_cheese',a="Tyrolean grey cheese",
    v=[V("Tiroler Graukäse PDO",d="Old data.")],dt="loaf, slice or stick, 200 g–4 kg · at least ten weeks in cellar"),
  A("Gamalost","Traditional Norwegian aged sour-milk cheese.",W+'Gamalost',a="gammelost",v=[V("Gamalost frå Vik",d="Old data.")]),
  A("Pultost","Soft Norwegian sour-milk cheese of soured skimmed milk with caraway, spreadable or grainy.",W+'Pultost',mk="Tine",
    v=[V("Løiten","Tine",d="Spreadable type made at Nybergsund, Trysil."),V("Hedmark and Oppland Counties Pultost",d="Old data.")])],
 "m":[["Werdenberger Sauerkäse, Liechtensteiner Sauerkäse und Bloderkäse AOP",""],["Dambalkhacho GI",""]]})
kinds.append({"n":"Farmhouse washed-rind cheese","a":"Irish farmhouse cheese · British washed-rind · American washed-rind",
 "d":"Washed-rind cheeses created by single farms and creameries outside the old European appellations, known by maker and name.",
 "t":["semi-soft","soft","smoked","raw milk","pasteurised"],
 "s":W+'Washed-rind_cheese',
 "x":[A("Milleens","Irish farmhouse washed-rind cheese first made in 1976 near Eyeries, County Cork.",W+'Milleens',y="1976",dt="large rounds and small 'dotes' · 4–10 weeks"),
  A("Gubbeen","Semi-soft surface-ripened cheese with a pink and white rind, made since 1979 at Gubbeen Farm, Schull.",W+'Gubbeen_Farmhouse_Cheese',mk="Gubbeen Farmhouse Products",y="1979",
    v=[V("Smoked Gubbeen","Gubbeen Farmhouse Products"),V("Dunnes Stores Creamy & Nutty Gubbeen Cheese","Dunnes Stores",d="Retail pack (old data).")]),
  A("Durrus","Round semi-soft raw-milk washed-rind cheese developed by Jeffa Gill in 1979 near Durrus, County Cork.",W+'Durrus_Farmhouse_Cheese',y="1979",dt="3–5 weeks · pinkish yellow-grey rind"),
  A("Ardrahan","Washed-rind cheese first made in 1983 by Eugene and Mary Burns at Kanturk, County Cork.",W+'Ardrahan_Farmhouse_Cheese',y="1983",v=[V("Duhallow",d="Second cheese of the same farm.")]),
  A("Stinking Bishop","Gloucestershire washed-rind cheese of Old Gloucester milk, made since 1972 by Charles Martell and Son.",W+'Stinking_Bishop',y="1972")],
 "m":[["Savour","Sharpham Cheese"],["Kasuga","Bosque Cheese Lab"],["Mohant PDO",""]]})
brands=[
 {"n":"Fromagerie Gaugry","c":"France","f":"","seg":"Burgundian cheese dairy","d":"Cheese dairy at Brochon, Côte-d'Or, maker of Époisses and of L'Ami du Chambertin, created by Raymond Gaugry in 1950.","lines":[],"eras":["Raymond Gaugry"],"sig":["L'Ami du Chambertin","Époisses PDO"],"sc":[],"rel":[],"s":FR+'Ami_du_Chambertin'},
 {"n":"Jasper Hill Farm","c":"United States","f":"","seg":"Artisan cheesemaker and affineur","d":"Artisan cheesemaker in Greensboro, Vermont, run by Andy and Mateo Kehler, with the Cellars at Jasper Hill ageing for others.","lines":["Cellars at Jasper Hill"],"eras":["Andy and Mateo Kehler"],"sig":["Winnimere"],"sc":[],"rel":[],"s":W+'Jasper_Hill_Farm'},
 {"n":"Uplands Cheese Company","c":"United States","f":"","seg":"Farmstead cheesemaker","d":"Dairy farm and artisan cheesemaker in Dodgeville, Wisconsin, known for Pleasant Ridge Reserve.","lines":[],"eras":["Andy Hatch"],"sig":["Rush Creek Reserve","Pleasant Ridge Reserve"],"sc":[],"rel":[],"s":W+'Uplands_Cheese_Company'},
 {"n":"Agropur","c":"Canada","f":"1938","seg":"Dairy co-operative","d":"Canadian dairy co-operative founded in Granby, Quebec, owner of the Oka cheese brand.","lines":["Natrel","Oka","Québon"],"eras":[],"sig":["Oka"],"sc":[],"rel":[],"s":W+'Agropur'},
 {"n":"Gubbeen Farmhouse Products","c":"Ireland","f":"1979","seg":"Farmhouse cheesemaker","d":"Ferguson family farm at Schull, County Cork, making Gubbeen cheese from its own mixed herd.","lines":["Smoked Gubbeen"],"eras":["Tom and Giana Ferguson"],"sig":["Gubbeen"],"sc":[],"rel":[],"s":W+'Gubbeen_Farmhouse_Cheese'},
 {"n":"Tine","c":"Norway","f":"","seg":"Dairy co-operative","d":"Norway's largest dairy co-operative, owned by its milk producers.","lines":[],"eras":[],"sig":["Pultost"],"sc":[],"rel":[],"s":W+'Tine_(company)'}]
notes=("Old catch-all 'Other washed-rind cheese' (k55) dissolved into Époisses, Munster, Reblochon, Taleggio, Vacherin Mont-d'Or, Pont-l'Évêque & Livarot, Maroilles, Saint-Nectaire and a new sourced kind 'Farmhouse washed-rind cheese' (Irish/British/US icons). "
 "Left for other shelves, not included here: Puzzone di Moena / Spretz Tzaorì PDO (Italian shelf; wiki page retrieved https://en.wikipedia.org/wiki/Puzzone_di_Moena) and Queso de l'Alt Urgell y la Cerdanya PDO (Spanish shelf). "
 "Mohant PDO, Odenwälder Frühstückskäse PDO, Werdenberger Sauerkäse and Dambalkhacho kept as flat models (no page retrieved). Not done: affineur versions (Mons, Cantin, Androuët) – no page retrieved; Saint-Nectaire fermier/laitier versions and Chimay variety names not confirmed. No traditions added.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/J3/shelves/03_02.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p); print('written',len(kinds))
