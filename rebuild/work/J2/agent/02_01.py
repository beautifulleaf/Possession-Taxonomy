import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
W="https://en.wikipedia.org/wiki/"
K=[
{"n":"Kipper & smoked herring","a":"kipper · bloater · buckling · smoked herring","d":"Herring split or whole and smoked: kipper (split, cold-smoked), bloater (whole, cold-smoked), buckling (hot-smoked).",
 "t":["undyed","dyed","fillet","whole","vacuum-packed"],"s":"https://www.thefishsociety.co.uk/collections/smoked-cured",
 "x":[
 A("Craster kipper","Undyed kipper smoked in the stone smokehouses of Craster, Northumberland, over oak for sixteen hours.",W+"Craster_kipper",mk="L. Robson & Sons",dt="oak and white wood shavings · golden skin"),
 A("Manx kipper","Undyed, longer-smoked Isle of Man kipper from the kipper houses of Peel.",W+"Kipper",mk="Moore's Kipper Yard",y="1882",dt="Peel · second house Devereau and Son, 1884",a="skeddan jiarg",v=[{"n":"Moore's Kipper Yard","mk":"Moore's Kipper Yard","y":"1882","d":"Peel kipper house"},{"n":"Devereau and Son","mk":"","y":"1884","d":"Peel kipper house"}]),
 A("Loch Fyne kipper","Well-known Scottish kipper named for the Argyll sea loch.",W+"Kipper",dt="Scotland"),
 A("Yarmouth bloater","Whole, ungutted herring salted and lightly cold-smoked, tied to Great Yarmouth and now rare.",W+"Bloater_(herring)",dt="gamey flavour"),
 A("Buckling","Hot-smoked herring, headed and gutted with roe or milt left in, eaten warm or cold.",W+"Buckling_(fish)",dt="Bückling in German")
 ],
 "m":[["Cured and Smoked Sunnmøre Herring",""]]},
{"n":"Smoked haddock","a":"finnan haddie · Arbroath smokie · Finnan · Räucherschellfisch","d":"Haddock cold- or hot-smoked, sold as fillets or whole split fish.",
 "t":["undyed","dyed","fillet","whole","cold-smoked","hot-smoked"],"s":"https://www.thefishsociety.co.uk/products/grimsby-smoked-haddock-fillet-steaks",
 "x":[
 A("Arbroath smokie PGI","Whole haddock tied in pairs and hot-smoked in a covered barrel over hardwood; EU PGI registered 2004, made within about 8 km of Arbroath.",W+"Arbroath_smokie",y="2004",dt="ready in under an hour · originated at Auchmithie",a="Arbroath smokies"),
 A("Finnan haddie","Haddock cured with green-wood or peat smoke, said to come from Findon near Aberdeen, used for Cullen skink and kedgeree.",W+"Finnan_haddie",dt="Findon or Findhorn origin claims")
 ]},
{"n":"Smoked mackerel","a":"Räuchermakrele","d":"Mackerel smoked cold or hot, sold as fillets or whole fish.","t":["hot-smoked","peppered","fillet","whole"],"s":"https://www.knuspr.de/26505-pappudio-geraucherte-makrele?defaultProductTab=2&itemPosition=9","m":[["Hot Smoked Mackerel Fillets","East Neuk Kilnhouse"]]},
{"n":"Smoked trout","a":"Räucherforelle","d":"Trout smoked cold or hot, sold as fillets or whole fish.","t":["hot-smoked","cold-smoked","fillet","whole"],"s":"https://www.knuspr.de/18176-lachsforellenfilet-natur-hei-gerauchert","m":[["Hot Smoked Rainbow Trout Fillets","Goatsbridge Fish Processors"],["Stone Kiln Cold Smoked Rainbow Trout Fillet","Kuopion Perinnetuote"]]},
{"n":"Smoked eel","a":"Räucheraal · Spickaal","d":"Eel smoked whole or in pieces.","t":["whole","fillet","hot-smoked"],"s":"https://formanandfield.com/product/h-forman-son-smoked-eel-fillets/",
 "x":[A("Räucheraal","Whole eel hot-smoked with the head on, a centuries-old north German and Dutch speciality; Steinhuder Rauchaal and Smoortaal are named regional forms.","https://www.yumda.com/en/encyclopedia/R%C3%A4ucheraal.html",dt="eel about 28% fat · increasingly imported eel",a="Spickaal")]},
{"n":"Smoked sprats","a":"Sprotten · Kieler Sprotten","d":"Sprats Sprattus sprattus smoked whole and sold chilled; tinned smoked sprats are in Tinned & jarred fish.","t":["chilled","whole"],"s":"https://www.knuspr.de/c893-raucherfisch"},
{"n":"Smoked shad","a":"scrumbie afumată","d":"Shad (Alosa) salted and smoked, cold or hot, sold whole or as fillets; tinned smoked shad is in Tinned & jarred fish.","t":["whole","fillet","cold-smoked"],"s":"https://www.digi24.ro/stiri/economie/comisia-europeana-scrumbia-afumata-de-dunare-a-devenit-al-cincilea-produs-recunoscut-oficial-1042255","m":[["Scrumbie de Dunăre afumată PGI",""]]},
{"n":"Smoked milkfish","a":"tinapang bangus","d":"Milkfish Chanos chanos smoked whole or butterflied, sold chilled or frozen; tinned smoked milkfish is in Tinned & jarred fish.","t":["whole","butterflied","chilled","frozen"],"s":"https://www.accessdata.fda.gov/cms_ia/importalert_49.html",
 "x":[A("Tinapang bangus","Filipino smoked milkfish: cleaned, brined five to six hours, air-dried and smoked; tinapa is a pre-colonial preparation.",W+"Tinapa",dt="also made with blackfin scad")]},
{"n":"Smoked dogfish belly","a":"Schillerlocke","d":"Smoked belly flaps of dogfish, known by the German name Schillerlocke.","t":["MSC-certified"],"s":"https://www.fiedlers-fischmarkt.de/raeucherfisch/schillerlocke-msc.html",
 "x":[A("Schillerlocke","Skinned spiny dogfish belly flaps about 20 cm long that curl into tubes when smoked; the dogfish is listed Vulnerable.","https://www.yumda.com/de/lexikon/Schillerlocke+%28Fisch%29.html",dt="Goldlocke tilapia substitute · methylmercury warning")]}
]
B=[
{"n":"L. Robson & Sons","c":"United Kingdom","f":"","seg":"Heritage manufactory","kf":"Craster kippers","d":"Craster smokehouse, the only firm still producing commercial Craster kippers.","lines":[],"eras":[],"sig":["Craster kipper"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Craster_kipper"},
{"n":"Moore's Kipper Yard","c":"Isle of Man","f":"1882","seg":"Heritage manufactory","kf":"Manx kippers","d":"Peel kipper house, one of two on the Isle of Man.","lines":[],"eras":[],"sig":["Manx kipper"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Kipper"}]
out={"kinds":K,"brands":B,"traditions":[],"notes":"All nine planned kinds kept. Arbroath smokies PGI and Arbroath smokie deduped into one archetype. Manx and Craster kipper models became archetypes; Sunnmore herring stays a flat model (Slow Food page returned empty). Kieler Sprotten, Danube shad PGI and Cullen not turned into archetypes for lack of a successfully retrieved page (shad and sprats keep old sources). Smoked mackerel and trout keep the few old models (already three or fewer)."}
p='work/J2/shelves/02_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
