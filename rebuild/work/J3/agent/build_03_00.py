import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,a='',mk='',y='',v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk='',y='',d=''):
    r={"n":n}
    if mk:r["mk"]=mk
    if y:r["y"]=y
    if d:r["d"]=d
    return r
kinds=[
{"n":"Cream cheese","a":"queso crema · krem peynir · queso filadelfia","d":"Soft, spreadable, unripened cheese of milk and cream, mild and slightly tangy.",
 "t":["plain","light / reduced-fat","flavoured (herb, chive, sweet)","block","whipped tub"],
 "s":"https://www.kraftheinz.com/philadelphia/products/00021000612239-original-cream-cheese",
 "x":[X("Philadelphia","The originating American cream cheese brand, first made by William Lawrence of Chester, New York, in 1872 and sold as Philadelphia from 1880.",W+"Philadelphia_Cream_Cheese",a="Philly",mk="Philadelphia",y="1872",
   v=[V("Lawrence Neufchâtel-style cream cheese",mk="Philadelphia",y="1872",d="William Lawrence's first mass-produced unripened cheese, Chester, New York."),
      V("Philadelphia Cream Cheese label",mk="Philadelphia",y="1880",d="Name given by distributor Alvah Reynolds to Lawrence & Durland cheese."),
      V("Kraft-Phenix Philadelphia",mk="Philadelphia",y="1928",d="Phenix Cheese Company (owner of the name from 1903) merged with Kraft."),
      V("Philadelphia Original Cream Cheese",mk="Philadelphia",d="Current reference block and tub.")],
   dt="block or tub · original, light, flavoured · lower fat in American cream cheese than elsewhere")],
 "m":[["Almarai Spreadable Cream Cheese","Almarai"],["Britannia Cream Cheese","Britannia Industries"],["Eker Krem Peynir","Eker Süt Ürünleri"],["Ekici Krem Peynir","Ekiciler Süt Gıda Tarım Hayvancılık"],["Pınar Cream Cheese","Pınar Süt Ürünleri"],["Sütaş Krem Peynir","Sütaş"],["Verónica Queso Crema","Verónica"],["Danubio Cream Cheese","Vigor"]]},
{"n":"Ricotta & whey cheese","a":"ricotta · whey cheese · brocciu · mizithra · requeijão · urda","d":"Soft cheese made by reheating whey, often with milk added, and lifting the fine curd; moist and mild when fresh.",
 "t":["fresh","ricotta salata (pressed, salted, aged)","ricotta infornata (baked)","ricotta affumicata (smoked)","ricotta forte (fermented)","whey only","whey with added milk"],
 "s":"https://www.cheese.com/fresh-ricotta/",
 "x":[X("Ricotta romana PDO","Protected Italian ricotta made from the whey of sheep's milk.",W+"Ricotta",a="Ricotta Romana DOP"),
  X("Ricotta di bufala campana PDO","Protected ricotta made from the whey left after making mozzarella di bufala campana.",W+"Ricotta",a="Ricotta di Bufala Campana DOP"),
  X("Brocciu PDO","Corsican ewe's-milk and whey cheese, eaten fresh or briefly ripened; Corsica's most representative food.",W+"Brocciu",a="brocciu corse · broccio",
   v=[V("Brocciu frais",d="Eaten immediately."),V("Brocciu passu / vechju",d="Ripened for a few weeks; ideal affinage 48 hours to one month.")]),
  X("Requeijão da Serra da Estrela PDO","Portuguese whey cheese of the Serra da Estrela region, protected since 2005.",W+"Requeij%C3%A3o",y="PDO 2005"),
  X("Manouri PDO","Greek semi-soft whey cheese of sheep's or goat's milk with added cream, made after feta in Thessaly and Macedonia.",W+"Manouri",dt="fat about 36–38% · salt about 0.8%"),
  X("Mizithra","Greek sheep's or goat's whey cheese, sold fresh like ricotta or salt-dried for grating; mainly Crete.",W+"Mizithra",a="myzithra",
   v=[V("Fresh mizithra"),V("Dried (grating) mizithra",d="Salt-dried, like ricotta salata.")],dt="milk to whey about 7:3"),
  X("Xynomizithra Kritis PDO","Sour Cretan variant of mizithra, whey with about 15% full-cream ewe's or goat's milk.",W+"Xinomyzithra",a="xynomyzithra"),
  X("Anthotyros","Traditional Greek fresh whey-and-milk cheese of sheep or goats, usually a truncated cone; also a dry matured form.",W+"Anthotyros",a="anthotyro",
   v=[V("Fresh anthotyros"),V("Dry anthotyros",d="Matured, similar to mizithra.")],dt="milk to whey about 9:1"),
  X("Urda","Whey cheese of Southeast Europe and Hungary.",W+"Urda_(cheese)",a="urdă · vurda · izvara · orda")],
 "m":[["Ardagh Castle Ricotta","Ardagh Castle Cheese"],["Eleftheria Ricotta","Eleftheria"],["Brousse du Rove PDO",""],["Cacioricotta del Cilento",""],["Moliterna",""],["Ricotta piemontese",""],["Valnerina Ricotta Salata",""]]},
{"n":"Mascarpone","a":"mascherpone","d":"Soft, thick fresh cream product of Lombardy set by acid and heat, rich and mild; a main ingredient of tiramisu.",
 "t":["tub","reduced-fat"],"s":"https://www.cheese.com/mascarpone/",
 "m":[["Flanders Dairy Mascarpone","Flanders Dairy"]]},
{"n":"Fresh goat's cheese","a":"chèvre frais · fresh chèvre · hvit geitost","d":"Young, unripened, rindless goat's-milk cheese sold in logs, pyramids or tubs, soft and tangy.",
 "t":["plain log","ash-coated","herbed or peppered","tub / spreadable","goat's fromage blanc"],
 "s":W+"Goat_cheese",
 "m":[["Soignon fresh goat's cheese pyramid","Soignon"],["Soignon goat's milk fromage blanc","Soignon"],["Clover Blossom Honey Goat Cheese","Vermont Creamery"]]},
{"n":"Fresh soft cheese","a":"spreadable soft cheese · Gournay cheese · cheese spread","d":"Soft, spreadable fresh or lightly ripened cheese, plain or seasoned, other than cream cheese.",
 "t":["herbed","garlic","peppered","plain","processed spread"],
 "s":"https://www.boursin.com/products/",
 "x":[X("Boursin","Gournay-style fresh cow's-milk and cream cheese with herbs, the first flavoured cheese sold nationally in France.",W+"Boursin_cheese",mk="Boursin",y="1963",
   v=[V("Boursin Garlic & Fine Herbs",mk="Boursin",y="1963",d="First flavour, by François Boursin of Normandy.")],dt="flavours: garlic & fine herbs and others · crumbly, spreadable"),
  X("Bryndza","Creamy white, tangy, crumbly sheep's-milk cheese of Central and Eastern Europe, chiefly Slovakia and Poland.",W+"Bryndza",a="brynza",
   v=[V("Bryndza Podhalańska PDO",d="Polish sheep's-milk bryndza of Podhale."),V("Slovenská bryndza PGI")]),
  X("Squacquerone di Romagna PDO","Very soft, moist, crumbly fresh cheese of Romagna.",W+"Squacquerone"),
  X("Galotyri PDO","Greek soft, spreadable acid-curd cheese of sheep's and goat's milk from Epirus and Thessaly, ripened for months.",
   "https://willstudd.com/cheese/aphrodite-galoytri/",y="PDO 1996",v=[V("Aphrodite Galotyri")]),
  X("Kopanisti PDO","Salty, peppery spreadable cheese of the Cyclades, kneaded repeatedly during ripening; made on Mykonos for 300 years.",W+"Kopanisti",a="Kopanisti Mykonou"),
  X("Liptauer","Spicy cheese spread of Slovak, Austrian and Hungarian cuisine, based on sheep's or goat's cheese, quark or cottage cheese.",W+"Liptauer"),
  X("Requeijão cremoso","Brazilian spreadable cheese of emulsified curds with cream or butter.",W+"Requeij%C3%A3o",
   v=[V("Catupiry",mk="Catupiry",y="1911",d="Leading brand, developed by Mario Silvestrini in Minas Gerais.")])],
 "m":[["Britannia Cheese Spreadz","Britannia Industries"],["Milma Spread Cheese","Kerala Co-operative Milk Marketing Federation (Milma)"],["Mother Dairy Garlic & Herbs Cheese Spread","Mother Dairy"],["Mother Dairy Piri Piri Cheese Spread","Mother Dairy"],["Prochiz Spready","Mulia Boga Raya"],["Verka Cheese Spread","Punjab Milk Producers Federation (Verka)"],["Pınar Spreadable Cheese","Pınar Süt Ürünleri"],["Quatá Creme de Queijo","Quatá"],["Casatella Trevigiana PDO",""],["Ανεβατό / Anevato PDO",""],["Κατίκι Δομοκού / Katiki Domokou PDO",""],["Ξύγαλο Σητείας / Xygalo Siteias PDO",""],["Πηχτόγαλο Χανίων / Pichtogalo Chanion PDO",""]]},
{"n":"Quark & fromage blanc","a":"Speisequark · quarg · curd cheese · fromage frais · maquée · tvorog","d":"Fresh, soft, unsalted acid-set cheese of soured, strained milk, spoonable.",
 "t":["low-fat (Magerquark)","full-fat","fromage frais (live cultures)","faisselle (moulded, draining)","flavoured"],
 "s":"https://world.openfoodfacts.org/product/4036303138467/magerquark-milram",
 "x":[X("Quark","Fresh acid-set cheese of soured, strained milk, soft, white and unsalted.",W+"Quark_(dairy_product)",a="quarg · Topfen"),
  X("Fromage blanc","Acid-set fresh cheese of northern France and southern Belgium; fromage frais must contain live cultures.",W+"Fromage_blanc",a="fromage frais · maquée",v=[V("Faisselle",d="Sold in its draining mould.")]),
  X("Tvorog","Soft white fermented-milk curd of Central, Eastern and Northern Europe, not usually counted as cheese in Russian.",W+"Tvorog",a=""),
  X("Petit-suisse","Small fresh cheese of Normandy.",W+"Petit_suisse")],
 "m":[["Käse Quark","Käse Fromagerie"],["Sek Quark","SEK"]]},
{"n":"Cottage cheese","a":"","d":"Fresh, mild curd cheese of skimmed milk in loose curds mixed with a cream and salt dressing.",
 "t":["small curd","large curd","low-fat","full-fat"],"s":"https://www.daisybrand.com/cottage-cheese/",
 "m":[["Daisy Cottage Cheese","Daisy Brand"],["KDCow Cottage Cheese","Kuwait Danish Dairy (KDCow)"],["Jihočeský cottage","Madeta"],["First Choice Chunky Cottage Cheese","Woodlands Dairy"]]},
{"n":"Queso fresco & fresh white cheese","a":"fresh white cheese · queso blanco · panela · Minas frescal · kesong puti · queijo fresco · farmer cheese",
 "d":"Fresh, unripened, salted white cheese of pressed or drained rennet or acid curd, crumbly or sliceable, mild.",
 "t":["crumbly","sliceable","frying cheese (queso frito)","cow's","goat's or mixed milk"],
 "s":"https://www.tusbuenasnoticias.com/amp/noticias/actualidad/2026/01/10/55522-profeco-revela-que-marcas-de-queso-panela-si-son-autenticas",
 "x":[X("Queso fresco / queso blanco","Latin American fresh white cheese, traditionally cow's milk (queso fresco sometimes with goat's), easy to make without careful ripening.",W+"White_cheese",
   v=[V("Queso frito (Dominican, Nicaraguan, Puerto Rican)",d="Firm, salty white cheese for frying."),V("Venezuelan quesos blancos",d="Llanero, palmita, guayanés, queso de mano.")]),
  X("Queso panela","Mexican fresh pasteurised cow's-milk cheese, also called basket cheese; holds its shape when fried.",W+"Panela_cheese",a="queso canasta · queso de la canasta"),
  X("Minas frescal","Brazilian fresh Minas cheese, eaten 4–10 days after making, juicy, soft and mild; often with goiabada.",W+"Minas_cheese",a="queijo minas frescal · queijo branco",
   v=[V("Queijo minas padrão",d="Newer supermarket version, firmer and less salty.")]),
  X("Queijo fresco","Mild, soft, creamy unaged white cheese of Portugal and the Iberian Peninsula.",W+"White_cheese"),
  X("Kesong puti","Filipino soft white cheese of unskimmed carabao's milk set with vinegar, citrus or rennet.",W+"Kesong_puti",a="quesong puti",
   v=[V("Holly's White Cheese (Quesong Puti)",mk="Real Fresh Dairy Farms (Holly's Milk)")]),
  X("Farmer cheese","Pressed or unripened curd cheese set with rennet and starter, of cow's, sheep's or goat's milk.",W+"Farmer_cheese",a="farmer's cheese · pot cheese")],
 "m":[["Burgos Líneanatural","Lácteas García Baquero"],["Cebreiro PDO",""],["Queso Camerano PDO",""],["Tomme fraîche de l'Aubrac PGI",""],["Agrì di Valtorta",""],["Caciofiore della campagna romana",""],["Fromage de Chamelle du Sahara",""],["Giuncata dei Monti Reatini",""],["Ittiri Fresa Cheese",""],["Lietuviškas varškės sūris PGI",""],["Lički škripavac PGI",""],["Marzolina",""],["Mishavinë",""],["Ser koryciński swojski PGI",""],["Stracchino all’antica delle valli orobiche",""]]},
{"n":"Paneer & chhena","a":"panir · ponir · chhana","d":"Fresh, unsalted, non-melting acid-set curd cheese of South Asia, of cow's or buffalo milk.",
 "t":["block","cubes","malai (full-fat)","high-protein / low-fat"],"s":"https://globallinker.com/products/gowardhan-fresh-paneer-5810277",
 "x":[X("Paneer","Pressed, non-aged acid-set cheese curdled with lemon juice or citric acid, central to north Indian cooking.",W+"Paneer"),
  X("Chhena","Acid-set curd of the Indian subcontinent, strained and pressed; kneaded for Bengali and Odia sweets or further pressed into paneer.",W+"Chhena",a="chhana")],
 "m":[["Amul High Protein Paneer","Amul"],["Mother Dairy Paneer","Mother Dairy"],["Gowardhan Paneer","Parag Milk Foods"],["Pride of Cows High-Protein Paneer","Parag Milk Foods"],["Milky Mist Paneer","Milky Mist Dairy Food"],["Hatsun Paneer","Hatsun Agro Product"],["Heritage Fresh Paneer","Heritage Foods"],["Verka Paneer","Punjab Milk Producers Federation (Verka)"],["Milma Paneer","Kerala Co-operative Milk Marketing Federation (Milma)"],["Vita Paneer","Vita (Haryana state dairy)"],["Akshayakalpa Organic Malai Paneer","Akshayakalpa Organic"],["Everest Paneer","Everest Dairies"]]},
{"n":"Brunost","a":"brown whey cheese · mysost · geitost · gjetost · mesost","d":"Whey with milk or cream boiled down until the milk sugars caramelise, setting into a brown, sweet, fudge-like block or spread.",
 "t":["block (for slicing with a cheese slicer)","spread (prim / messmör)","cow's","goat's","mixed milk"],
 "s":"https://en.wikipedia.org/wiki/Synn%C3%B8ve_Finden",
 "x":[X("Gudbrandsdalsost","The most popular brunost, of cow's and goat's milk, cream and whey; created by Anne Hov at Valseter, Gudbrandsdalen, in 1863.",W+"Brunost",a="Gudbrandsdal cheese · gjetost (US)",mk="Tine",y="1863",
   v=[V("Heidal cheese",d="A type of Gudbrandsdalsost.")],dt="Tine, the largest producer, markets 13 brunost varieties"),
  X("Fløtemysost","Cream whey cheese of cow's milk only, milder than Gudbrandsdalsost; the second most popular brunost.",W+"Brunost",a="cream whey cheese"),
  X("Ekte geitost","Brunost of whey and goat's milk only, with an intense, chèvre-like taste.",W+"Brunost",a="true goat's cheese"),
  X("Prim and messmör","Soft, sweet whey spread boiled down about 10:1, sold in tubes across the Nordic countries.",W+"Brunost",a="prim · messmör")],
 "m":[["Synnøve Finden brown cheese","Synnøve Finden"],["Eleftheria Brunost","Vivanda Gourmet"],["Artisanal Sognefjord Geitost",""]]},
]
brands=[
{"n":"Philadelphia","c":"United States","f":"1872","seg":"Mass-market cream cheese","d":"American cream cheese brand, first produced in 1872 and the best-selling cream cheese brand worldwide; owned by Kraft Heinz and Mondelez International.","lines":["Philadelphia Original Cream Cheese"],"eras":["William Lawrence and Alvah Reynolds, 1872–1903","Phenix Cheese Company, 1903–1928","Kraft-Phenix and successors, 1928–"],"sig":["Philadelphia"],"sc":[],"rel":["Kraft Heinz"],"s":W+"Philadelphia_Cream_Cheese"},
{"n":"Boursin","c":"France","f":"1963","seg":"Flavoured fresh cheese","d":"French brand of Gournay-style herbed fresh cheese created by François Boursin of Normandy; owned by Groupe Bel since 2007.","lines":["Garlic & Fine Herbs"],"eras":["François Boursin, 1957–1990","Unilever, 1990–2007","Groupe Bel, 2007–"],"sig":["Boursin"],"sc":[],"rel":[],"s":W+"Boursin_cheese"},
{"n":"Tine","c":"Norway","f":"","seg":"Dairy co-operative","d":"Norway's largest dairy co-operative, owned by its milk producers, and the world's largest producer of brunost.","lines":[],"eras":[],"sig":["Gudbrandsdalsost"],"sc":[],"rel":["Synnøve Finden"],"s":W+"Tine_(company)"},
{"n":"Synnøve Finden","c":"Norway","f":"","seg":"Dairy","d":"Norwegian dairy company and Tine's only domestic challenger in cheese; launched brown cheese in 1997.","lines":["yellow cheese (1996)","brown cheese (1997)"],"eras":[],"sig":[],"sc":[],"rel":["Tine"],"s":"https://en.wikipedia.org/wiki/Synn%C3%B8ve_Finden"},
{"n":"Catupiry","c":"Brazil","f":"1911","seg":"Requeijão","d":"One of Brazil's most popular brands of requeijão cremoso, developed by Italian immigrant Mario Silvestrini in Minas Gerais.","lines":[],"eras":[],"sig":["Requeijão cremoso"],"sc":[],"rel":[],"s":W+"Catupiry"},
{"n":"Soignon","c":"France","f":"1895","seg":"Goat's cheese","d":"Goat's-cheese brand founded as a farmers' co-operative dairy at Saint-Martin-de-Saint-Maixent, Deux-Sèvres; goat-only since 1932.","lines":["Bûche de chèvre (1972)","Bûche Sainte-Maure (1986)","goat's yoghurts and fromages blancs (2009)","fresh goat's cheese pyramid (2012)"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://www.soignon.fr/soignon/notre-histoire/"},
]
trads=[{"n":"Norwegian brunost (whey boiling)","g":"Food & drink","r":"Norway and Scandinavia","p":"Whey spreads for at least 2,500 years; firm cream brunost from 1863",
 "d":"Boiling whey, with milk or cream, until the milk sugars caramelise into brown whey cheese or spread.","tech":"Whey reduced about 10:1 in iron pots; cream added for the firm modern cheese","mat":"Cow's and goat's whey, milk and cream",
 "forms":["Gudbrandsdalsost","Fløtemysost","Ekte geitost","Prim and messmör"],"ctr":["Gudbrandsdalen","Valseter mountain farm, Gålå (Anne Hov)","Tine","Synnøve Finden"],
 "auth":"Ekte geitost contains no cow's milk; Gudbrandsdalsost mixes cow's and goat's milk","s":W+"Brunost"}]
notes=("Dropped Afuega'l Pitu PDO from fresh white cheese: it is a ripened Asturian cheese, hand to the Spanish shelf. Kept Cebreiro, Camerano and Tomme fraîche de l'Aubrac "
 "as plain models (fresh forms exist) since no page was retrieved to make them archetypes. Brousse du Rove kept once (in Ricotta & whey cheese), duplicate removed from fresh white cheese. "
 "Katiki Domokou, Anevato, Casatella, Xygalo and Pichtogalo stay as models: no retrievable source page (anycheese 403). Montrachet left out: retrieved snippets say it is aged at least four weeks, not fresh. "
 "Soignon's bûches are ripened logs (belong with soft white-rind / lactic goat), so only its fresh lines are listed. Duplicate Gowardhan entry merged under Parag Milk Foods. Vermont Creamery honey goat cheese moved to Fresh goat's cheese. "
 "Ricotta salata, infornata, affumicata and forte are types, not archetypes. Skyr and labneh belong to the yoghurt shelf.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/J3/shelves/03_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print('kinds',len(kinds),'arch',sum(len(k.get('x',[])) for k in kinds))
