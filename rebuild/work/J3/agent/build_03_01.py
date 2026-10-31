import json, os
W='https://en.wikipedia.org/wiki/'
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
brie={"n":"Brie","a":"brie de Meaux · brie de Melun · coulommiers",
 "d":"Large, flat soft cow's-milk cheese with a white Penicillium rind, from the Brie region east of Paris and made widely elsewhere.",
 "t":["farmhouse (fermier), raw milk","dairy (laitier), pasteurised","aged black brie (brie noir)","truffled","smoked","double-cream"],
 "s":"https://presidentcheese.com/products/brie-cheese/president-brie-round/",
 "x":[
  A("Brie de Meaux PDO","Raw-milk brie of the Brie region, about 36–37 cm across and 2.8 kg; the reference brie, AOC since 1980.",W+"Brie_de_Meaux",y="AOC 1980",a="Brie de Meaux AOP",
    v=[V("Brie de Meaux PDO","Sodiaal",d="Dairy-made PDO brie (old data).")],dt="wheel c. 36–37 cm, c. 2.8 kg · raw cow's milk · ripening at least four to five weeks · farmhouse or dairy"),
  A("Brie de Melun PDO","Smaller, stronger raw-milk brie, about 27 cm across and 1.5 kg on average, AOC since 1980.",W+"Brie_de_Melun",y="AOC 1980",a="Brie de Melun AOP",
    v=[V("Brie noir (old brie)",d="Aged several months to a year until dark and strong; not AOC.")],dt="wheel c. 27 cm, c. 1.5 kg · raw cow's milk · young to long-aged"),
  A("Coulommiers","Smaller, thicker brie-type disc from Coulommiers, older than brie and nuttier; ripened four to six weeks when pasteurised.",W+"Coulommiers_cheese",
    dt="disc · raw (farmhouse, reddish blush) or pasteurised · 40% fat"),
  A("Brie de Nangis","Raw-milk bloomy-rind brie of the Nangis area, about 22 cm and 1 kg; name not protected.","https://fr.wikipedia.org/wiki/Brie_de_Nangis",
    v=[V("Brie de Nangis","Laiterie Rouzaire",d="Made year-round at Tournan-en-Brie; pasteurised version for export.")],dt="c. 22 cm, 3 cm thick, c. 1 kg · about one month in cellar"),
  A("Dairy brie","Industrial pasteurised brie made by large dairies in France and abroad, mild and stable.",W+"Brie",
    v=[V("Président Brie","Président"),V("Castello Organic Brie","Castello"),V("Brie (Kolb-Lena plant)","Savencia Fromage & Dairy",d="Alouette, Delice de France and Dorothy's brands (Illinois, US).")],dt="round or wedge · pasteurised · plain, double-cream, truffled"),
  A("British and Irish farmhouse brie","Brie-style cheeses made by British and Irish creameries, often from single-herd milk.",W+"Brie",
    v=[V("Baron Bigod",d="Suffolk."),V("Cornish Brie"),V("Somerset Brie"),V("Cenarth brie",d="Wales."),V("Morangie brie",d="Scotland."),V("Wicklow Bán brie",d="Ireland."),
       V("Bath Soft Cheese Co Bath Brie","Bath Soft Cheese Co"),V("Tipperary Brie","Cooleeney Farmhouse Cheese"),V("Ballybrie","Fivemiletown Creamery"),V("Eden Valley Organic Brie","Appleby Creamery")])
 ]}
cam={"n":"Camembert","a":"camembert de Normandie",
 "d":"Small round soft cow's-milk cheese with a white bloomy rind, first made in Camembert, Normandy, in the late 18th century.",
 "t":["raw milk (au lait cru)","pasteurised","smoked","boxed whole or portions"],
 "s":"https://www.cheese.com/camembert/",
 "x":[
  A("Camembert de Normandie PDO","Raw-milk camembert from Normande cows' milk, ladled into moulds in at least five passes and ripened at least three weeks.","https://fr.wikipedia.org/wiki/Camembert_de_Normandie",y="AOC 1983",a="Camembert de Normandie AOP",
    v=[V("Camembert de Normandie","Gillot",d="Saint-Hilaire-de-Briouze, Orne."),V("Camembert de Normandie","Isigny Sainte-Mère",d="Co-operative, Isigny-sur-Mer."),
       V("Jort","Lactalis",d="Société fromagère de Jort, Bernières-d'Ailly."),V("Moulin de Carel","Lactalis",d="Saint-Pierre-sur-Dives."),
       V("Domaine de Saint Loup",d="Saint-Loup-de-Fribois."),V("Fromagerie du Val d'Ay (Réaux)",d="Lessay, Manche."),V("Ferme de la Mondière",d="Farm producer, Orbec.")],
    dt="c. 250 g wheel in wooden box · raw milk only · about 10% of camembert output · farm or dairy"),
  A("Dairy camembert","Pasteurised camembert made industrially in Normandy and abroad, the bulk of camembert sold.",W+"Camembert",
    v=[V("Président Camembert (fabriqué en Normandie)","Président"),V("Castello Camembert","Castello",d="North American market.")]),
  A("Neufchâtel PDO","Grainy, saltier bloomy-rind cheese of the Pays de Bray, usually heart-shaped, matured 8–10 weeks; among France's oldest cheeses.",W+"Neufch%C3%A2tel_cheese",a="cœur de Neufchâtel",
    dt="heart, log, square, brick · 100–600 g · 8–10 weeks"),
  A("Altenburger Ziegenkäse PDO","Thuringian-Saxon soft cheese of cow's milk with at least 15% goat's milk, camembert-mould rind, often with caraway.","https://de.wikipedia.org/wiki/Altenburger_Ziegenk%C3%A4se",
    dt="small wheels · with or without caraway"),
  A("Bonchester PDO","Scottish soft white-rind cheese of unpasteurised Jersey milk from Bonchester Bridge, Roxburghshire.",W+"Bonchester_cheese")
 ]}
dc={"n":"Double- & triple-cream cheese","a":"double-crème · triple-crème · Brillat-Savarin · Chaource",
 "d":"Rich bloomy-rind cheese made with added cream; double-cream has at least 60%, triple-cream at least 72–75% fat in dry matter.",
 "t":["double-cream","triple-cream","fresh (frais)","affiné","truffled"],
 "s":"https://en.wikipedia.org/wiki/Bloomy_rind",
 "x":[
  A("Brillat-Savarin PGI","Triple-cream cow's-milk cheese of at least 72% fat in dry matter, created 1890 by the Dubuc family and renamed by the Androuëts in the 1930s.",W+"Brillat-Savarin_cheese",y="1890",
    a="Excelsior · Délice des gourmets",v=[V("Brillat-Savarin","Fromagerie Lincet")],dt="wheel 12–13 cm, c. 4 cm thick · fresh or affiné one to several weeks · Normandy, Burgundy"),
  A("Chaource PDO","Cylindrical cow's-milk cheese from Chaource in Champagne, soft and slightly crumbly under a Penicillium candidum rind.",W+"Chaource_cheese",
    v=[V("Chaource","Fromagerie Lincet")],dt="c. 10 cm across, 6 cm high · 250 g or 450 g"),
  A("Délice de Bourgogne","Burgundian triple-cream of milk enriched with crème fraîche, created 1975 by Jean Lincet at Saligny.",W+"D%C3%A9lice_de_Bourgogne",mk="Fromagerie Lincet",y="1975",
    dt="small rounds one week, larger rounds two weeks or more"),
  A("Explorateur","Île-de-France triple-cream of about 75% fat in dry matter, created in the 1950s and named after the Explorer satellite.",W+"Explorateur",y="1950s",dt="squat cylinder · trademark name"),
  A("Saint-André","Branded triple-cream cylinder of about 200 g, developed by the Soulié dairy in Aveyron and now made in Vire, Normandy.",W+"Saint-Andr%C3%A9_cheese",dt="200 g cylinder, 6 × 5 cm"),
  A("Cremont","Vermont double-cream aged cheese of cow's and goats' milk with added cream and a wrinkled geotrichum rind.","https://www.vermontcreamery.com/products/cremont",mk="Vermont Creamery",dt="5 oz round")
 ],
 "m":[["Wigmore","Village Maid Cheese"]]}
B=lambda n,lab: A(n,lab[0],lab[1],y=lab[2] if len(lab)>2 else "",a=lab[3] if len(lab)>3 else "",v=lab[4] if len(lab)>4 else None,dt=lab[5] if len(lab)>5 else "")
lg={"n":"Lactic goat cheese","a":"crottin · chèvre · lactic soft-ripened cheese · Sainte-Maure · Valençay · Picodon · Saint-Marcellin",
 "d":"Small soft cheese of slow acid-set (lactic) curd, mostly goat's milk, ripened with a natural, geotrichum, mould or ash rind.",
 "t":["ash-coated","natural rind","leaf-wrapped","fresh (frais)","aged (sec)"],
 "s":"https://www.finecheese.co.uk/st-maure-de-touraine",
 "x":[
  B("Crottin de Chavignol PDO",["Small raw goat's-milk drum from Chavignol in the Loire's Sancerre country, the archetypal crottin.",W+"Crottin_de_Chavignol","","Chavignol AOP",None,"fresh to dry and blue-moulded"]),
  B("Sainte-Maure de Touraine PDO",["Ash-rolled raw goat's-milk log of 16–17 cm with a straw through its centre, from Touraine.",W+"Sainte-Maure_de_Touraine","","",None,"log ≥ 250 g · ash rind · straw stamped with seal and producer number"]),
  B("Valençay PDO",["Truncated-pyramid raw goat's-milk cheese of Berry, charcoal-dusted with a blue-grey natural mould rind.",W+"Valen%C3%A7ay_cheese","AOC 1998","",None,"200–250 g, c. 7 cm high · fresh citric to nutty"]),
  B("Selles-sur-Cher PDO",["Small ash-dusted goat's-milk cylinder from Selles-sur-Cher, first made in the 19th century.",W+"Selles-sur-Cher_cheese","19th century","",None,"c. 150 g, 8 cm base · grey-blue mould rind"]),
  B("Pouligny-Saint-Pierre PDO",["Tall goat's-milk pyramid from the Indre, nicknamed the Eiffel Tower, first made in the 18th century.",W+"Pouligny-Saint-Pierre_cheese","18th century","pyramide",None,"6.5 cm base, 9 cm high, 250 g"]),
  B("Chabichou du Poitou PDO",["Bonde-shaped soft goat's-milk cheese of Poitou, aged 10 to 20 days; pasteurised milk permitted.",W+"Chabichou","","Chabichou",None,"bonde cylinder · 10–20 days"]),
  B("Picodon PDO",["Small flat goat's-milk discs from the Rhône valley, dry and spicy, from soft white to golden rind with age.",W+"Picodon","","",None,"5–8 cm, 40–100 g · young to long-aged"]),
  B("Pélardon PDO",["Small round goat's-milk cheese of the Cévennes with a white mould rind, about 60 g.",W+"P%C3%A9lardon","AOC 2000","paraldon · pélardou",None,"60–70 mm, c. 60 g"]),
  B("Rocamadour PDO",["Small soft goat's-milk disc from Périgord and Quercy, formerly called Cabécou de Rocamadour.",W+"Rocamadour_cheese","","Cabécou de Rocamadour",
     [V("Cabécou",d="Wider family of small goat discs from the Pyrenees to the Massif Central.")]]),
  B("Banon PDO",["Raw goat's-milk round from Provence wrapped in chestnut leaves tied with raffia.",W+"Banon_cheese","","Banon à la feuille",None,"c. 7 cm, 100 g · leaf-wrapped"]),
  B("Charolais PDO",["Soft natural-rind goat cheese from the Charolais and Brionnais hills of Burgundy.",W+"Charolais_(cheese)","AOC 2010"]),
  B("Mâconnais PDO",["Small truncated cone of goat's milk, or goat and cow, from southern Burgundy.",W+"M%C3%A2connais_cheese","AOC 2005","",None,"4–5 cm, 50–65 g"]),
  B("Rigotte de Condrieu PDO",["Small goat's-milk cheese of the Lyonnais named after Condrieu.",W+"Rigotte_de_Condrieu","AOC 2008"]),
  B("Saint-Marcellin PGI",["Small soft Dauphiné cheese, now of cow's milk, about 80 g, growing runnier with age.",W+"Saint-Marcellin","","",
     [V("Saint-Félicien",d="Larger Dauphiné cousin, about 180 g, originally goat's milk.")],"c. 80 g · young firm to runny in crock"]),
  B("Robiola di Roccaverano PDO",["Rindless raw goat's-milk robiola of the Langhe, eaten from four days old, recognised 1979.","https://it.wikipedia.org/wiki/Robiola_di_Roccaverano","1979","",None,"10–15 cm, 250–350 g"]),
  B("Murazzano PDO",["Robiola-type soft cheese from Murazzano in the Piedmont Langhe.",W+"Murazzano"]),
  B("Bûcheron",["Loire goat's-milk log ripened 5–10 weeks, with a bloomy rind, sold sliced into rounds.",W+"Bucheron","","Boucheron · Bucheron",None,"log 1.4–1.8 kg"]),
  A("Humboldt Fog","Californian pressed goat's-milk cheese with a bloomy rind and central line of edible ash.",W+"Humboldt_Fog",mk="Cypress Grove",v=[V("Humboldt Fog Original","Cypress Grove")])
 ],
 "m":[["Sinodun Hill","Norton and Yarrow"],["Rodó de cendra","La Frasera"],["Valleclaro","Quesos y Besos"],["Valleoscuro","Quesos y Besos"],["Pave Cobble","White Lake Cheese"]]}
brands=[
 {"n":"Président","c":"France","f":"1933","seg":"Mass-market dairy","d":"Lactalis dairy brand for butter and industrial versions of traditional French cheeses, created by André Besnier.","lines":[],"eras":[],"sig":["Dairy brie","Dairy camembert"],"sc":[],"rel":["Lactalis"],"s":W+"Pr%C3%A9sident_(brand)"},
 {"n":"Lactalis","c":"France","f":"","seg":"Dairy group","d":"World's largest dairy group, owned by the Besnier family and based in Laval.","lines":["Président","Parmalat"],"eras":[],"sig":["Camembert de Normandie PDO"],"sc":[],"rel":["Président"],"s":W+"Lactalis"},
 {"n":"Castello","c":"Denmark","f":"","seg":"Mass-market cheese","d":"Arla Foods cheese brand covering soft-ripened, blue, semi-hard and cream cheeses.","lines":[],"eras":[],"sig":["Dairy brie","Dairy camembert"],"sc":[],"rel":[],"s":W+"Castello_cheeses"},
 {"n":"Vermont Creamery","c":"United States","f":"1984","seg":"Artisan creamery","d":"Websterville, Vermont, cheese and butter maker founded by Allison Hooper and Bob Reese.","lines":[],"eras":[],"sig":["Cremont"],"sc":[],"rel":[],"s":W+"Vermont_Creamery"},
 {"n":"Cypress Grove","c":"United States","f":"","seg":"Artisan creamery","d":"Arcata, California, goat-cheese maker known for Humboldt Fog.","lines":[],"eras":[],"sig":["Humboldt Fog"],"sc":[],"rel":[],"s":W+"Cypress_Grove_Chevre"}]
notes=("Dropped retailer SKUs and untraceable foreign brie/camembert lists (Korean, Thai, Brazilian, Chinese, Japanese, Australian SKUs; Dunnes Stores Brillat-Savarin; Crémeux des Aldudes, Capricho, Kanoya White, Sakura, Hechizo) - no retrieved page. "
 "Truffle/smoked bries become types. Wigmore (washed-curd ewe's cheese) left in m of Double-cream kind as leftover for its own make family. Sinodun Hill and Spanish lactic goats kept in m of Lactic goat cheese. "
 "Bonchester and Altenburger placed as Camembert-kind archetypes. Affineurs (Androuët etc.) not added here. Village Maid page 403; Wikidata 429; Parallel no credit. No traditions added.")
out={"kinds":[brie,cam,dc,lg],"brands":brands,"traditions":[],"notes":notes}
p='work/J3/shelves/03_01.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
