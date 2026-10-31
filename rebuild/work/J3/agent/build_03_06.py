import json, os
W='https://en.wikipedia.org/wiki/'
def A(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(x) for x in v],"dt":dt}
def V(n,mk='',y='',d=''):
    o={"n":n}
    if mk:o["mk"]=mk
    if y:o["y"]=y
    if d:o["d"]=d
    return o
kinds=[]
kinds.append({"n":"Roquefort","a":"Roquefort AOP · blue cheese","d":"Sheep's-milk blue cheese from Lacaune ewes, ripened in the Combalou caves of Roquefort-sur-Soulzon; rindless, moist and crumbly.",
 "s":"https://www.cheese.com/roquefort/",
 "x":[A("Roquefort PDO","Blue sheep's-milk cheese that may bear the name only if aged in the natural Combalou caves; the first French AOC.","","AOC 1925",W+"Roquefort",
   [V("Roquefort Société","Société des Caves de Roquefort",d="Largest-volume brand by far; a Lactalis subsidiary since 1990."),
    V("Papillon","Papillon"),V("Carles","Carles"),V("Gabriel Coulet","Gabriel Coulet"),
    V("Fromageries occitanes","Fromageries occitanes"),V("Vernières","Vernières"),V("Le Vieux Berger","Le Vieux Berger")],
   "wheel 2.5–3 kg, about 10 cm high · raw Lacaune ewe's milk · aged about 5 months · producer (seven in 2009)","Roquefort AOC")]})
kinds.append({"n":"Stilton","a":"Blue Stilton · White Stilton","d":"English PDO cheese from pasteurised local milk made only in Derbyshire, Leicestershire and Nottinghamshire; the blue form is crumbly and veined.",
 "t":["Blue Stilton","White Stilton (unveined)","organic"],
 "s":"https://www.cheese.com/colston-bassett-stilton/",
 "x":[A("Blue Stilton PDO","Pasteurised cow's-milk blue from licensed dairies in three counties, matured at least nine weeks.","","PDO 1996 (certification trade mark 1966)",W+"Stilton",
   [V("Colston Bassett Blue Stilton","Colston Bassett Dairy"),V("Cropwell Bishop Blue Stilton","Cropwell Bishop Creamery",d="Also an organic version."),
    V("Blue Stilton","Long Clawson Dairy"),V("Hartington Creamery Stilton","Hartington Creamery",y="2014",d="Smallest of the six licensed makers."),
    V("Tuxford & Tebbutt Stilton","Tuxford & Tebbutt",d="Melton Mowbray creamery; ended production in 2024.")],
   "matured 9–12 weeks · pasteurised cow's milk · maker (six licensed dairies in 2016)","Stilton"),
  A("Stichelton","Raw-milk, animal-rennet cheese made to the old Stilton method; it cannot use the Stilton name because the PDO requires pasteurised milk.","","2006",W+"Stichelton",
   [V("Stichelton",y="2006",d="Made by Randolph Hodgson of Neal's Yard Dairy and Joe Schneider on the Welbeck Estate, Nottinghamshire.")],
   "unpasteurised Friesian-Holstein milk from Collinthwaite Farm · hand-ladled")]})
kinds.append({"n":"Gorgonzola","a":"Gorgonzola DOP · blue cheese","d":"Italian PDO blue cheese of unskimmed cow's milk from Piedmont and Lombardy, sold young and creamy (dolce) or aged and firm (piccante).",
 "s":"https://www.belgioioso.com/Products/",
 "x":[A("Gorgonzola Dolce PDO","Less aged, buttery and slightly sweet Gorgonzola with a milder bite.","","DOC 1955 · PDO 1996",W+"Gorgonzola",
   [V("Mario Costa Gorgonzola","Granarolo"),V("Vigor Gorgonzola","Vigor"),V("Gorgonzola Dolce PDO")],"aged about three months · spoonable texture · producer","dolce"),
  A("Gorgonzola Piccante PDO","More aged Gorgonzola, firm and crumbly with a pungent flavour.","","DOC 1955 · PDO 1996",W+"Gorgonzola",
   [V("Gorgonzola DOP Piccante","Caseificio Brusati"),V("Gorgonzola Piccante Nero – long seasoning","Igor"),V("Gorgonzola Piccante PDO")],"longer ageing · firm, crumbly paste · producer","piccante · mountain Gorgonzola")],
 "m":[["CreamyGorg","BelGioioso"]]})
kinds.append({"n":"French blue cheese","a":"bleu · fourme","d":"French blue cheeses other than Roquefort, mostly cow's-milk PDO cheeses of the Massif Central and the Jura and Alps.",
 "s":W+"Bleu_d%27Auvergne",
 "x":[A("Bleu d'Auvergne PDO","Cow's-milk blue of the Auvergne, developed by pricking curd to admit rye-bread mould.","","mid-1850s (Antoine Roussel)",W+"Bleu_d%27Auvergne",[],"cow's milk · AOC · wheel"),
  A("Fourme d'Ambert PDO","Tall narrow cylinder of semi-hard raw cow's-milk blue from the Auvergne, aged at least 28 days.","","Roman times; own AOC 2002",W+"Fourme_d%27Ambert",[],"tall cylinder · raw cow's milk · at least 28 days"),
  A("Fourme de Montbrison PDO","Near-twin of Fourme d'Ambert from the Loire, with a chestnut rind; separate AOC since 2002.","","AOC 2002",W+"Fourme_de_Montbrison",[],"cylinder 13 × 19 cm, 1.5–2 kg · cow's milk"),
  A("Bleu des Causses PDO","Whole cow's-milk blue aged three to six months in limestone caves of the Gorges du Tarn; a milder Roquefort cousin.","","AOC",W+"Bleu_des_Causses",[],"aged 3–6 months in natural caves · 45% fat"),
  A("Bleu de Gex PDO","Mild, creamy raw-milk blue of the Haut-Jura from Montbéliarde milk, each wheel stamped 'Gex'.","","AOC",W+"Bleu_de_Gex",[],"raw Montbéliarde milk · aged at least three weeks","Bleu du Haut-Jura · Bleu de Septmoncel"),
  A("Bleu du Vercors-Sassenage PDO","Mild pasteurised natural-rind cow's-milk blue of the Vercors massif, first made by monks.","","14th century; AOC 1998",W+"Bleu_du_Vercors-Sassenage",[],"Montbéliarde, Abondance or Villard milk · natural rind")],
 "m":[["Bleu du Queyras",""]]})
kinds.append({"n":"Spanish blue cheese","a":"queso azul","d":"Blue cheeses of the Picos de Europa in Asturias, León and Cantabria, often of mixed milks and ripened in limestone caves.",
 "s":W+"Cabrales_cheese",
 "x":[A("Cabrales PDO","Strong Asturian blue from raw cow's milk or blended with goat and sheep milk, ripened in natural limestone caves.","","traditional",W+"Cabrales_cheese",[],"2–5 months in caves at about 90% humidity · foil-wrapped with PDO stamp (leaf-wrapped not exported)"),
  A("Queso de Valdeón PGI","Intense blue from Posada de Valdeón, León, wrapped in sycamore or chestnut leaves.","","PGI",W+"Valde%C3%B3n_cheese",[],"leaf-wrapped · cow's milk, or mixed","Valdeón"),
  A("Picón Bejes-Tresviso PDO","Blue cheese from the Liébana valley of Cantabria, formerly called Picón de Tresviso.","","DO 1994",W+"Pic%C3%B3n_Bejes-Tresviso",[],"Liébana municipalities"),
  A("Gamonéu PDO","Lightly smoked Asturian cheese of mixed milks whose rind moulds slightly invade the paste.","","PDO",W+"Gamon%C3%A9u_cheese",[V("Asturias Gamonéu PDO","CAPSA")],"truckle from 500 g · smoked · natural rind","Gamonedo")],
 "m":[["Queso Azul El Roano","Quesería El Roano"],["Quevedo Azul Adictivo","Quesos Quevedo"]]})
kinds.append({"n":"Danish blue","a":"Danablu · Danish Blue Cheese","d":"Semi-soft, strong cow's-milk blue from Denmark, PGI-protected as Danablu.",
 "s":W+"Danish_Blue_Cheese",
 "x":[A("Danablu PGI","Drum- or block-shaped blue of full-fat milk and homogenised cream, pierced with copper rods and aged eight to twelve weeks.","","early 20th century (Marius Boel)",W+"Danish_Blue_Cheese",
   [V("Castello Danablu","Arla Foods")],"aged 8–12 weeks · 50–60% fat in dry matter · drum or block","Danish Blue")]})
kinds.append({"n":"Blue brie & soft blue","a":"blue brie · creamy blue · bleu à croûte fleurie","d":"Soft, creamy blue cheeses, often with a white mould rind over the veining, as in blue brie.",
 "s":W+"Cambozola",
 "x":[A("Cambozola","German soft-ripened cow's-milk blue with a white camembert-type rind and extra cream.","Käserei Champignon","1983",W+"Cambozola",[],"pasteurised cow's milk · white rind · triple-cream style","blue brie"),
  A("Saint Agur","Double-cream pasteurised cow's-milk blue from Beauzac in the Monts du Velay, aged 60 days.","Savencia Fromage & Dairy","",W+"Saint_Agur_Blue",[],"60% butterfat · aged 60 days"),
  A("Blue Castello","Danish triple-cream cow's-milk blue from the Castello brand.","Castello","1960s",W+"Castello_cheeses",[],"triple cream · cow's milk"),
  A("Bleu de Bresse","Soft blue with a white mushroom-scented coat and brie-like interior, first made in Bresse after the Second World War.","","after 1945",W+"Bleu_de_Bresse",[],"rounds 125–500 g · whole milk","Bresse Bleu")],
 "m":[["Castello Creamy Blue","Arla Foods"],["Abbey Blue Brie","Abbey Cheese Company"],["Dalewood Blue Brie","Dalewood Fromage"]]})
kinds.append({"n":"Farmhouse blue","a":"British blue · Irish blue · American blue · artisan blue","d":"Named blues from British, Irish and North American farmhouse makers, plus other regional blues without their own entry.",
 "s":"https://www.cheese.com/blue-vein-cheese/",
 "x":[A("Shropshire Blue","Orange, annatto-coloured Stilton-style blue first made at Castle Stuart dairy, Inverness; not from Shropshire.","","1970s",W+"Shropshire_Blue",
   [V("Colston Bassett Shropshire Blue","Colston Bassett Dairy"),V("Cropwell Bishop Blue Shropshire","Cropwell Bishop Creamery"),V("Blue Shropshire","Long Clawson Dairy"),V("Sparkenhoe Shropshire Blue","Leicestershire Handmade Cheese Company")],
   "annatto colour · cow's milk","Inverness-shire Blue · Blue Stuart"),
  A("Cashel Blue","Irish farmhouse cow's-milk blue first made by the Grubb family near Fethard, County Tipperary.","J&L Grubb","1984",W+"J%26L_Grubb",[V("Organic Cashel Blue","Cashel Farmhouse Cheesemakers")],"cow's milk"),
  A("Beenleigh Blue","Unpressed soft blue of pasteurised ewe's milk from Ticklemore in Devon, pioneered by Robin Congdon.","Ticklemore Cheese Dairy","1980s",W+"Beenleigh_Blue_cheese",[],"ewe's milk · vegetarian rennet"),
  A("Lanark Blue","Scottish blue from Humphrey Errington's own ewes, among the first British ewe's-milk blues since the Middle Ages.","Errington Cheese","1985",W+"Lanark_Blue",[],"ewe's milk · flavour varies with season"),
  A("Dorset Blue Vinny","Hard, crumbly cow's-milk blue from near Sturminster Newton, formerly of skimmed milk; PGI.","","traditional",W+"Dorset_Blue_Vinney",[],"often unpasteurised","Dorset Blue Vinney"),
  A("Buxton Blue","Russet, lightly veined Stilton relative made around Buxton; PDO.","","PDO",W+"Buxton_Blue",[],"cylinder · cow's milk"),
  A("Dovedale Blue","Soft, mild, brine-dipped cow's-milk blue from near the Dovedale valley; PDO 2007.","Hartington Creamery","PDO 2007",W+"Dovedale_cheese",[V("Dovedale Blue","Staffordshire Cheese Company")],"brine-salted · full-fat cow's milk"),
  A("Cornish Blue","Cornish cow's-milk blue from Upton Cross; World Cheese Awards winner 2010.","Cornish Cheese Company","",W+"Cornish_Blue",[],""),
  A("Oxford Blue","Creamy Stilton-style blue created by Baron Robert Pouget in Burford, Oxfordshire.","","1995",W+"Oxford_Blue_(cheese)",[],""),
  A("Bayley Hazen Blue","Vermont raw-milk blue named World's Best Unpasteurized Cheese at the 2014 World Cheese Awards.","Jasper Hill Farm","",W+"Jasper_Hill_Farm",[],"unpasteurised"),
  A("Point Reyes Original Blue","Raw-milk California blue, the only blue made in the state when introduced.","Point Reyes Farmstead Cheese Company","",W+"Point_Reyes_Farmstead_Cheese_Company",[],"raw cow's milk"),
  A("Rogue River Blue","Oregon blue from Rogue Creamery; first American cheese named World Champion at the World Cheese Awards (2019).","Rogue Creamery","",W+"Rogue_Creamery",[],"")],
 "m":[["Yorkshire Blue","Shepherds Purse Cheeses"],["Devon Blue","Ticklemore Cheese Dairy"],["Harbourne Blue","Ticklemore Cheese Dairy"],["Crozier Blue","J & L Grubb"],["Bath Blue","Bath Soft Cheese Co"],["Dunsyre Blue","Errington Cheese"],["Wensleydale Blue","Wensleydale Creamery"],["Exmoor Blue Cheese UK PGI",""],["Withersbrook Blue","Cellars at Jasper Hill"],["Kapiti Kikorangi Blue","Lactalis Mainland New Zealand"],["Kraftkar","Tingvollost"],["Jihočeská Niva PGI",""],["Erzurum küflü civil peyniri GI",""],["Tcherni Vit Green Cheese",""]]})
brands=[
 {"n":"Castello","c":"Denmark","f":"1893","seg":"Mass-market cheese","d":"Arla Foods cheese brand founded by Rasmus Tholstrup; its blue cheeses were developed in the 1960s.","lines":["Blue Castello","Creamy Blue","Danablu"],"eras":[],"sig":["Blue Castello"],"sc":[],"rel":["Arla Foods"],"s":W+"Castello_cheeses"},
 {"n":"Arla Foods","c":"Denmark","f":"2000","seg":"Dairy co-operative","d":"Danish-Swedish dairy co-operative formed by the merger of Arla and MD Foods; owner of Castello.","lines":["Castello"],"eras":[],"sig":["Danablu PGI"],"sc":[],"rel":["Castello"],"s":W+"Arla_Foods"},
 {"n":"Savencia Fromage & Dairy","c":"France","f":"","seg":"Industrial cheese group","d":"French family-owned cheese group, named Bongrain until 2015; owner of Saint Agur.","lines":["Saint Agur"],"eras":[],"sig":["Saint Agur"],"sc":[],"rel":[],"s":W+"Savencia_Fromage_%26_Dairy"},
 {"n":"Lactalis","c":"France","f":"","seg":"Dairy group","d":"Largest dairy group in the world; owns Société des Caves de Roquefort.","lines":["Roquefort Société"],"eras":[],"sig":["Roquefort PDO"],"sc":[],"rel":[],"s":W+"Lactalis"},
 {"n":"Käserei Champignon","c":"Germany","f":"","seg":"Cheese maker","d":"Allgäu cheese company (Hofmeister-Champignon) that patented Cambozola and has made it since 1983.","lines":["Cambozola"],"eras":[],"sig":["Cambozola"],"sc":[],"rel":[],"s":W+"Cambozola"},
 {"n":"J&L Grubb","c":"Ireland","f":"1984","seg":"Farmhouse cheesemaker","d":"Family cheesemaker near Fethard, County Tipperary, making Cashel Blue and the ewe's-milk Crozier Blue.","lines":["Cashel Blue","Crozier Blue"],"eras":[],"sig":["Cashel Blue"],"sc":[],"rel":[],"s":W+"J%26L_Grubb"},
 {"n":"Jasper Hill Farm","c":"United States","f":"","seg":"Artisan cheesemaker and affineur","d":"Greensboro, Vermont, cheesemaker run by Andy and Mateo Kehler, with the Cellars at Jasper Hill.","lines":["Bayley Hazen Blue","Withersbrook Blue"],"eras":[],"sig":["Bayley Hazen Blue"],"sc":[],"rel":[],"s":W+"Jasper_Hill_Farm"},
 {"n":"Point Reyes Farmstead Cheese Company","c":"United States","f":"2000","seg":"Farmstead cheesemaker","d":"Giacomini family cheese company at Point Reyes Station, Marin County, California.","lines":["Original Blue"],"eras":[],"sig":["Point Reyes Original Blue"],"sc":[],"rel":[],"s":W+"Point_Reyes_Farmstead_Cheese_Company"},
 {"n":"Rogue Creamery","c":"United States","f":"1933","seg":"Artisan creamery","d":"Central Point, Oregon, creamery whose Oregon Blue recipe came from Roquefort; first US exporter of raw-milk cheese to the EU.","lines":["Rogue River Blue","Oregon Blue"],"eras":["David Gremmels, from 2002"],"sig":["Rogue River Blue"],"sc":[],"rel":[],"s":W+"Rogue_Creamery"},
 {"n":"Cornish Cheese Company","c":"United Kingdom","f":"","seg":"Farmhouse cheesemaker","d":"Upton Cross, Cornwall, maker of Cornish Blue.","lines":["Cornish Blue"],"eras":[],"sig":["Cornish Blue"],"sc":[],"rel":[],"s":W+"Cornish_Blue"},
 {"n":"Ticklemore Cheese Dairy","c":"United Kingdom","f":"","seg":"Farmhouse cheesemaker","d":"Devon dairy at Ashprington making Beenleigh Blue, with Ben Harris as head cheesemaker.","lines":["Beenleigh Blue","Devon Blue","Harbourne Blue"],"eras":["Robin Congdon (founder)","Ben Harris"],"sig":["Beenleigh Blue"],"sc":[],"rel":[],"s":W+"Beenleigh_Blue_cheese"},
 {"n":"Errington Cheese","c":"United Kingdom","f":"1985","seg":"Farmhouse cheesemaker","d":"Humphrey Errington's dairy at Ogcastle near Carnwath, Lanarkshire, making Lanark Blue from its own ewes.","lines":["Lanark Blue","Dunsyre Blue"],"eras":[],"sig":["Lanark Blue"],"sc":[],"rel":[],"s":W+"Lanark_Blue"},
 {"n":"Hartington Creamery","c":"United Kingdom","f":"","seg":"Creamery","d":"Derbyshire creamery at Pikehall that originated Dovedale and was licensed to make Stilton in 2014.","lines":["Dovedale Blue","Stilton"],"eras":[],"sig":["Dovedale Blue"],"sc":[],"rel":[],"s":W+"Dovedale_cheese"}]
trads=[
 {"n":"Roquefort cave ripening","g":"Food & drink","r":"Roquefort-sur-Soulzon, Aveyron, France","p":"AOC since 1925","d":"Ripening of Lacaune ewe's-milk blue cheese in the natural Combalou caves, the only place where Roquefort may be aged.","tech":"Cave ageing with Penicillium roqueforti","mat":"Raw Lacaune sheep's milk","forms":["Roquefort PDO"],"ctr":["Société des Caves de Roquefort","Papillon","Carles","Gabriel Coulet"],"auth":"Roquefort PDO name and aging in the Combalou caves.","s":W+"Roquefort"},
 {"n":"Picos de Europa cave blues","g":"Food & drink","r":"Asturias, León and Cantabria, Spain","p":"traditional","d":"Mountain blue cheeses of cow's or mixed milks matured in natural limestone caves and once wrapped in leaves.","tech":"Natural cave ripening at about 90% humidity and 7–13 °C","mat":"Raw cow's milk, often blended with goat and sheep milk","forms":["Cabrales PDO","Queso de Valdeón PGI","Picón Bejes-Tresviso PDO","Gamonéu PDO"],"ctr":["Consejo Regulador D.O.P. Cabrales"],"auth":"PDO or PGI stamp on the wrapper; Cabrales in dark green foil.","s":W+"Cabrales_cheese"}]
notes=("Dissolved 'Other blue cheese' (82 models) into French, Spanish, Danish, soft-blue and farmhouse kinds. Kept as archetypes only cheeses with a retrieved page. "
 "Trimmed ~45 small British/foreign farmhouse SKUs with no retrieved page (e.g. Black Dub Blue, Cranborne, Brinkworth, Burt's, Blue Millie, Cote Hill, Daylesford, Binham, Hobnail, Adel/Leeds Blue, Isle of Wight Blue, Kodai, Ku, Blugins, Nidelven Blå, Vismann, Moo'dy Blue, Pudubec, Briacacio, Niva (Madeta), Zlatá Niva, Mezcla Reny Picot, duplicate Yorkshire Blue variants, Danish blue generic); a few notable ones remain in Farmhouse blue m. "
 "Planned-but-unconfirmed: Long Clawson as Stilton maker kept from old data; no page found for Niva, Bleu du Queyras, Dunsyre, Exmoor Blue, Yorkshire Blue. Fromageries occitanes/Vernières/Le Vieux Berger added from the Roquefort article. Stichelton maker left mk empty (Hodgson/Neal's Yard named in version note). "
 "Oxford Blue and Bleu de Bresse added. No affineur pages fetched for this shelf.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/J3/shelves/03_06.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print('ok', len(kinds), sum(len(k.get('x',[])) for k in kinds), len(brands))
