import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":mk,"y":b,"d":c} for a1,b,c in v],"dt":dt}
k1={"n":"Sparkling mineral water","a":"eau gazeuse · acqua frizzante · Sprudel · agua con gas","d":"Mineral water from a recognised source sold sparkling, either naturally carbonated at source or with CO2 added at bottling.",
 "t":["naturally sparkling (gas from the source)","source gas re-added","carbonated with added CO2","fine or light bubbles","intense or extra sparkling","glass bottle","PET bottle","can"],
 "s":W+"Carbonated_water","x":[
 X("Selters","Naturally carbonated water from the Taunus wells at Selters, Hesse; the prototype that gave 'seltzer' its name.","Selters","772",W+"Selters",
   [("Niederselters well","1999","historic main well, closed 1999"),("Selters-Löhnberg well","","current production")],"naturally carbonated > 250 mg/L CO2 · sparkling and still"),
 X("Apollinaris","Naturally sparkling mineral water from a spring at Bad Neuenahr, Germany; 'The Queen of Table Waters'.","Apollinaris","1852",W+"Apollinaris_(water)",
   [("'The Queen of Table Waters' trademark","1895","British trademark"),("'Baby Polly' small bottle","","UK and Ireland")],"naturally sparkling · glass bottles"),
 X("Gerolsteiner Sprudel","Naturally carbonated, very hard bicarbonate mineral water from Gerolstein in the Eifel; TDS 2,488 mg/L.","Gerolsteiner","1888",W+"Gerolsteiner_Brunnen",
   [("Gerolsteiner Sprudel","1888","original naturally carbonated water"),("Lower-carbonation variant","1986",""),("Reusable PET deposit bottle","1998","Germany's first")],"TDS 2,488 mg/L · bicarbonate 1,816, Ca 348, Mg 108 mg/L · pH 5.9–6.0"),
 X("Perrier","Sparkling mineral water from Vergèze, Gard, France, in a green teardrop bottle; source gas is captured separately and re-added.","Perrier","1898",W+"Perrier",
   [("Glass teardrop bottle","","signature green"),("PET bottle","2001",""),("Eau de Perrier","2002","less carbonated, blue bottle, France"),("Andy Warhol limited edition","2013","150th anniversary"),("Perrier Fluo","","flavoured line, France")],"glass, PET, can · natural, lemon, lime"),
 X("Badoit","Naturally sparkling, bicarbonate-rich mineral water from Saint-Galmier, Loire, France, with fine bubbles.","Badoit","1838",W+"Badoit",
   [("Green Badoit","","original"),("Red Badoit","2004","more sparkling"),("PET bottle","1999",""),("Can","2015","")],"bicarbonate 1,250, Na 180, Ca 153 mg/L · pH 6 · glass, PET, can"),
 X("S.Pellegrino","Medium-mineral water from San Pellegrino Terme, Lombardy, with CO2 added at bottling; star-label 'Vichy' glass bottle.","Sanpellegrino","1899",W+"Sanpellegrino",
   [("Vichy-shape glass bottle","1899","unchanged design"),("PET bottle","late 1990s","50 cl; 33, 75, 100 cl from 2006"),("'Meets Italian Talents' labels","2010","with Missoni, Bulgari; also 2011, 2013")],"TDS 854 mg/L · sulphate 402, Ca 164 mg/L · glass 25–100 cl, PET",a="San Pellegrino"),
 X("Ferrarelle","Italian mineral water trademark dating from 1893.","Ferrarelle","1893","https://www.wikidata.org/wiki/Q1407592"),
 X("Topo Chico","Sparkling mineral water from Monterrey, Mexico, naturally carbonated at source and further carbonated; glass bottles.","Topo Chico","1895",W+"Topo_Chico",
   [("130th-anniversary 12-pack","2025","labels from 1895 to 2025")],"glass bottle · strong carbonation"),
 X("Vichy Catalan","Highly mineralised sodium-bicarbonate sparkling water from Caldes de Malavella, Girona, Catalonia.","Vichy Catalan","1890",W+"Vichy_Catalán",[],"dry residue 3,052 mg/L · Na 1,097, bicarbonate 2,081 mg/L · glass, can"),
 X("Borjomi","Naturally carbonated, highly mineralised volcanic water from the Borjomi Gorge, Georgia; TDS 5,000–7,500 mg/L.","Borjomi","1890",W+"Borjomi_(water)",
   [("First bottling plant","1854","1,350 bottles"),("Deer-image packaging","2011",""),("Minimalist silver-stripe design","2019",""),("Classic-look redesign","2024","by Osborne Pike")],"TDS 5,000–7,500 mg/L · bicarbonate 3,500–5,000, Na 1,000–2,000 mg/L"),
 X("Mattoni","Czech mineral water from Kyselka near Karlovy Vary, bottled by Heinrich Mattoni from 1867; sparkling and flavoured.","Mattoni","1873",W+"Mattoni",[("First bottling by Heinrich Mattoni","1867","")],"plain and flavoured"),
 X("Saratoga","Spring water from Saratoga Springs, New York, sold sparkling and still in a cobalt-blue bottle.","Saratoga","1872",W+"Saratoga_Spring_Water",
   [("Saratoga Vichy","1872","original name"),("Aluminium bottle","2024","")],"cobalt-blue glass · sparkling and still"),
 ]}
k2={"n":"Seltzer & carbonated water","a":"seltzer · soda water · sparkling water · fizzy water","d":"Plain water with carbon dioxide injected under pressure, not from a named mineral source; unflavoured.",
 "t":["plain seltzer","minerals added","glass bottle","can","PET bottle","multipack"],"s":W+"Carbonated_water",
 "m":[["Polar Seltzer","Polar Beverages"],["LaCroix Pure","LaCroix"],["justbubly","Bubly"]]}
k3={"n":"Flavoured sparkling water","a":"flavoured seltzer · sparkling flavoured water · essence water","d":"Sparkling water flavoured with fruit essences or juice, usually unsweetened and calorie-free.",
 "t":["unsweetened essence-flavoured","with fruit juice","caffeinated","can","bottle"],"s":W+"La_Croix_Sparkling_Water","x":[
 X("LaCroix","American unsweetened, naturally essence-flavoured sparkling water in bright cans; launched by Heileman in La Crosse, Wisconsin.","LaCroix","1980",W+"La_Croix_Sparkling_Water",
   [("Pure, Lemon, Lime, Orange, Berry, Cran-Raspberry","2004",""),("Pamplemousse","2008","grapefruit"),("Coconut","2011",""),("Can redesign","2002",""),("Cúrate line","","fruit blends"),("NiCola / laCola","","cola-flavoured"),("LimonCello, Hi-Biscus!, Pastèque","2020","")],"12 fl oz cans · flavours"),
 X("Bubly","PepsiCo's sugar-free sparkling water with natural flavours, launched in the US and Canada in eight flavours.","Bubly","2018",W+"Bubly",
   [("Original eight flavours","2018",""),("Bubly Bounce","2021","caffeinated, 35 mg"),("Bubly Burst","2024","with fruit juice, 16.9 oz PET")],"cans · flavours"),
 X("Polar Seltzer","Flavoured seltzer from the family-owned Polar Beverages of Worcester, Massachusetts.","Polar Beverages","1882",W+"Polar_Beverages",[("Cranberry Lime","","")],"cans · flavours"),
 X("Perrier flavoured","Flavoured versions of Perrier sparkling mineral water.","Perrier","",W+"Perrier",
   [("Lemon, Lime","",""),("Citron Lemon-Lime, Pamplemousse Rose","2007","US"),("Green Apple","2015",""),("Saveur Menthe","2016","France"),("Strawberry, Watermelon","2017","")],""),
 ]}
br=lambda n,c,f,seg,d,s,sig,rel=(),lines=():{"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 br("Selters","Germany","","naturally sparkling mineral water","Historic Taunus mineral water whose name became the generic 'seltzer'.",W+"Selters",["Selters"]),
 br("Apollinaris","Germany","1852","sparkling mineral water","Bad Neuenahr sparkling water, owned by Coca-Cola since 2006.",W+"Apollinaris_(water)",["Apollinaris"]),
 br("Gerolsteiner","Germany","1888","mineral water","Eifel mineral water company majority-owned by Bitburger Holding.",W+"Gerolsteiner_Brunnen",["Gerolsteiner Sprudel"]),
 br("Perrier","France","1898","sparkling mineral water","Nestlé-owned sparkling water from Vergèze in a green teardrop bottle.",W+"Perrier",["Perrier"],["Sanpellegrino"]),
 br("Badoit","France","1838","sparkling mineral water","Danone-owned naturally sparkling water from Saint-Galmier.",W+"Badoit",["Badoit"]),
 br("Sanpellegrino","Italy","1899","mineral water and sodas","Nestlé-owned maker of S.Pellegrino water and Italian sodas such as Aranciata.",W+"Sanpellegrino",["S.Pellegrino"],["Perrier"],["S.Pellegrino","Aranciata","Limonata","Sanbittèr","Chinò"]),
 br("Ferrarelle","Italy","1893","sparkling mineral water","Italian mineral water trademark.","https://www.wikidata.org/wiki/Q1407592",["Ferrarelle"]),
 br("Topo Chico","Mexico","1895","sparkling mineral water","Monterrey mineral water owned by Coca-Cola since 2017.",W+"Topo_Chico",["Topo Chico"]),
 br("Vichy Catalan","Spain","1890","sparkling mineral water","Catalan sodium-bicarbonate water from Caldes de Malavella, founded by Modest Furest i Roca.",W+"Vichy_Catalán",["Vichy Catalan"]),
 br("Borjomi","Georgia","1890","sparkling mineral water","Georgian naturally carbonated mineral water from the Borjomi Gorge.",W+"Borjomi_(water)",["Borjomi"]),
 br("Mattoni","Czech Republic","1873","mineral water and soft drinks","Karlovy Vary beverage group (Mattoni 1873) owned by the Pasquale family.",W+"Mattoni",["Mattoni"]),
 br("Saratoga","United States","1872","premium spring water","Saratoga Springs water in cobalt-blue bottles, owned by BlueTriton Brands since 2021.",W+"Saratoga_Spring_Water",["Saratoga"]),
 br("LaCroix","United States","1980","flavoured sparkling water","National Beverage-owned unsweetened sparkling water from La Crosse, Wisconsin.",W+"La_Croix_Sparkling_Water",["LaCroix"]),
 br("Bubly","United States","2018","flavoured sparkling water","PepsiCo sparkling water brand.",W+"Bubly",["Bubly"]),
 br("Polar Beverages","United States","1882","soft drinks and seltzer","Family-owned Worcester, Massachusetts drinks maker known for Polar Seltzer.",W+"Polar_Beverages",["Polar Seltzer"]),
]
out={"kinds":[k1,k2,k3],"brands":brands,"traditions":[],"notes":"All three planned kinds are new (no old data). Natural vs added carbonation kept as kind types and stated per archetype. Soda water/club soda as mixer left to the Mixers shelf. Ferrarelle sourced only from Wikidata (no en-wiki page), so description is minimal. Spindrift and Polar flavour editions left out: pages 404 / not covered. Home carbonation (SodaStream, siphons) belongs to appliances, not this shelf."}
p='/home/user/Possession-Taxonomy/rebuild/work/J9/shelves/00_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
