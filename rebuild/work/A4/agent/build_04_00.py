import json,os
W="https://en.wikipedia.org/wiki/"
RIM="https://www.rimowa.com/us/en/stories/rimowa-alphabet.html"
ACQ="https://acquiremag.com/style/rimowa-updated-product-line/"
COS="https://www.presseportal.ch/fr/pm/100003332/100566474"
PEAK="https://www.thepeakmagazine.com.sg/lifestyle/check-out-tumis-first-ever-aluminium-luggage-line"
ESQ="https://esquiresg.com/tumi-50th-anniversary-travel-luggage-luxury/"
GTB="https://www.globe-trotter.com/blogs/journal/123-years-and-counting-the-history-of-the-centenary-collection"
GTV="https://www.globe-trotter.com/products/centenary-vanity-case-marmalade-brown"
BR="https://onemileatatime.com/review-briggs-riley-20-carry-on-baseline/"
LVMC="https://www.lvmh.com/en/news-lvmh/louis-vuitton-family-home-presents-malle-courrier-exhibition"
HAT="https://www.1stdibs.com/fashion/handbags-purses-bags/luggage-travel-bags/louis-vuitton-monogram-round-hat-box-boite-chapeaux-50cm-french-company-1970s/id-v_3864451"
CAB="https://www.1stdibs.com/furniture/more-furniture-collectibles/home-accents/trunks-luggage/louis-vuitton-wardrobe-trunk-paris-c-1910/id-f_46525852"
PIN="https://yachtstyle.co/how-fred-pinel-of-pinel-et-pinel-transformed-the-trunk-into-an-item-of-contemporary-furnishing/"
PGD="https://digitalnomads.world/travel/patagonia-black-hole-wheeled-duffel-40l-review/"
TR=W+"Trunk_(luggage)"
def X(n,d,mk,y,s,v=(),a="",dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
kinds=[
{"n":"Suitcase","a":"luggage · roller case · spinner · carry-on · check-in case","d":"Rigid or semi-rigid case with a lid for carrying clothes on a journey, usually on wheels with a telescoping handle.",
 "t":["carry-on / cabin size","medium check-in","large check-in","four-wheel spinner","two-wheel upright","expandable","hardside aluminium","hardside polycarbonate or composite","softside nylon","vulcanised fibreboard","leather"],
 "s":"https://shop.samsonite.com/luggage",
 "x":[
  X("Rimowa Original","Grooved aluminium suitcase whose parallel ribs, added in 1950, were inspired by all-metal aircraft.","Rimowa","1950",RIM,
    [("First aluminium suitcase","Rimowa","1937","Rimowa's first aluminium case, before the grooves"),("Topas","Rimowa","","earlier name of the grooved aluminium range, dropped in 2018"),("Original","Rimowa","2018","current name for the aluminium cases"),("Original Pilot","Rimowa","",""),("Classic","Rimowa","2018","aluminium with leather handles and detailing; ex Classic Flight series")],
    a="Topas · Rimowa aluminium",dt="sizes cabin to trunk · natural silver, black, colours · leather or polymer handles"),
  X("Rimowa Essential","Grooved polycarbonate suitcase range, the lightweight counterpart of the aluminium Original.","Rimowa","2000",ACQ,
    [("Salsa","Rimowa","2000","earlier polycarbonate range name, dropped in 2018"),("Essential","Rimowa","2018","new name for all polycarbonate models"),("Essential Lite","Rimowa","",""),("Essential Sleeve","Rimowa","",""),("Hybrid","Rimowa","2018","polycarbonate shell with aluminium components")],
    a="Salsa",dt="cabin, check-in, trunk sizes · matte and gloss colours"),
  X("Samsonite tapered suitcase","Tapered vulcanised-fibre suitcase from the Shwayder Trunk Manufacturing Company that gave the Samsonite name to the firm.","Samsonite","1939",W+"Samsonite",
    [("Samsonite name in use","Samsonite","1941",""),("First wheeled suitcase","Samsonite","1974","")],dt="vulcanised fibre · colours"),
  X("Cosmolite","Shell-shaped hardside spinner made of Curv, a woven layered composite, launched as Samsonite's lightest hard case.","Samsonite","2008",COS,
    [("Cosmolite","Samsonite","2008","four spinner sizes plus a beauty case; 55 cm spinner 2.2 kg; black, silver, red"),("Cosmolite 3.0","Samsonite","","")],
    a="Samsonite Curv",dt="sizes 55–85 cm spinner · colours"),
  X("19 Degree","Tumi's first aluminium luggage, with curved lines running across every surface.","Tumi","2016",PEAK,
    [("19 Degree Aluminum","Tumi","2016","aluminium body, die-cast corners, silver or matte black"),("19 Degree Lite","Tumi","","lightest version")],dt="aluminium or lighter variants · silver, matte black"),
  X("Alpha","Tumi's core softside range in FXT ballistic nylon.","Tumi","",ESQ,
    [("Alpha Bravo","Tumi","","")],a="Tumi ballistic nylon",dt="ballistic nylon · black · carry-on to garment bag"),
  X("Centenary","Globe-Trotter's handmade vulcanised-fibreboard case with leather corners and straps, reviving a 1910 archive design.","Globe-Trotter","1997",GTB,
    [("Centenary Carry-On","Globe-Trotter","",""),("Centenary Check-In","Globe-Trotter","","")],
    dt="vulcanised fibreboard colours · leather corners · brass rivets"),
  X("The Carry-On","Direct-to-consumer hardside carry-on that launched Away and its range of sized siblings.","Away","2016",W+"Away_(company)",
    [("The Carry-On","Away","2016","shipped from February 2016"),("The Bigger Carry-On","Away","2016",""),("The Medium","Away","2016",""),("The Large","Away","2016","")],dt="polycarbonate · colours"),
  X("Baseline","Briggs & Riley's softside upright line, known for repairs free of charge even when an airline caused the damage.","Briggs & Riley","",BR,
    [("20\" Carry-On Expandable Wide-Body Upright (U420XW)","Briggs & Riley","","reviewed 2009")],dt="expandable · upright or spinner · colours")],
 "m":[["Distinct","Rimowa"],["Tegra-Lite","Tumi"],["Freeform","Samsonite"]],
 "r":[["Arrivé","Tumi"],["Silhouette","Samsonite"],["Safari","Globe-Trotter"],["Deluxe","Globe-Trotter"]]},
{"n":"Travel trunk","a":"trunk · steamer trunk · malle","d":"Large box-shaped case made to travel with its owner, now often kept as furniture or for collections.",
 "t":["flat-top","dome-top / camel-back","steamer","cabin (malle cabine)","wardrobe","hat trunk","wicker","footlocker","canvas-covered","leather-covered"],
 "s":TR,
 "x":[
  X("Malle Courrier","Louis Vuitton's flat-topped, stackable trunk on a poplar frame covered in waterproof canvas, from which the house grew.","Louis Vuitton","1858",LVMC,
    [("Flat trunk in Grey Trianon canvas","Louis Vuitton","1858",""),("Malle Courrier patent","Louis Vuitton","1867",""),("Striped canvas","Louis Vuitton","1876","beige-and-brown stripes against imitation"),("Damier canvas","Louis Vuitton","1888",""),("Monogram canvas","Louis Vuitton","1896","")],
    a="flat-top trunk · Louis Vuitton trunk",dt="canvas: Trianon, stripes, Damier, Monogram · brass or lozine trim · beech slats · serial number and label"),
  X("Malle cabine","Low cabin trunk sized to slide under a steamship bunk.","Louis Vuitton","c. 1900",CAB,
    [("Monogram jacquard malle cabine","Louis Vuitton","1899–1904","woven Monogram canvas, about 111 × 56 × 31 cm")],a="cabin trunk",dt="woven or printed canvas · brass fittings · interior lining"),
  X("Goyard trunk","Paris trunk in Goyard's hand-painted chevron Goyardine canvas, shown at the 1900 World Exposition.","Goyard","1900",W+"Goyard",
    [("Writer's trunk","Goyard","","special order for Arthur Conan Doyle with filing cabinet, typewriter and folding desk"),("Woven canvas","Goyard","1965","patented by Robert Goyard")],dt="Goyardine colours · personalised stripes and initials"),
  X("Moynat trunk","Moynat's wicker trunk, also called the English trunk.","Moynat","1870",W+"Moynat",
    [("Lightweight trunk system","Moynat","1889","by Jules Coulembier"),("Extra-light trunk","Moynat","1910",""),("Automobile trunks","Moynat","1925","Diplôme d'Honneur at the Paris Exposition")],a="English trunk",dt="wicker, canvas · Toile 1920 M"),
  X("Steamer trunk","Flat or slightly curved trunk about 14 inches tall, built to steamship rules.","","1880–1920",TR,[],dt="height about 14 in · canvas, leather, slats"),
  X("Wardrobe trunk","Trunk that stands on end to open, with drawers on one side and hangers on the other.","","",TR,[],dt="large and heavy · drawers, hangers"),
  X("Dome-top trunk","Trunk with a high curved lid of 25–30 inches.","","1870s–1900s",TR,[("Camel-back","","",""),("Barrel-top","","","")],a="camel-back · hunch-back",dt="lid profile · tin, leather, wood"),
  X("Globe-Trotter cabin trunk","Vulcanised-fibreboard cabin trunk, advertised in 1912–13 as tested by an elephant to eight tons.","Globe-Trotter","1912",W+"Globe-Trotter",[],dt="vulcanised fibreboard · leather corners"),
  X("Pinel et Pinel object trunk","Contemporary Paris trunk built round one object or pastime.","Pinel et Pinel","2004",PIN,
    [("DJ trunk","Pinel et Pinel","","turntables and laptop stand"),("Malle Arcade 80 GT","Pinel et Pinel","","1980s arcade games"),("Picnic trunk","Pinel et Pinel","",""),("Malle coffre-fort","Pinel et Pinel","2008","made for Vacheron Constantin")],dt="leather colours · fitted interiors"),
  X("Boîte Chapeaux","Louis Vuitton's round hat box in Monogram canvas.","Louis Vuitton","",HAT,
    [("Boîte Chapeaux 50","Louis Vuitton","1970s","about 50 cm; made in the USA by The French Company under licence")],a="hat box · Boîte Chapeau",dt="sizes · Monogram canvas · leather trim")]},
{"n":"Vanity case","a":"train case · beauty case · cosmetic case","d":"Small hard case for toiletries and cosmetics, usually with a top handle, lid mirror and lift-out tray.",
 "t":["hard shell","removable tray","lid mirror","lockable"],
 "s":W+"Train_case",
 "x":[
  X("Train case","Boxlike grooming case with a top handle, mirror in the lid and a tray over the main compartment.","","",W+"Train_case",
    [("Train case set","Lady Baltimore","1950s","")],dt="hard shell colours · tray, mirror"),
  X("Centenary Vanity Case","Globe-Trotter's handmade vulcanised-fibreboard vanity case with removable tray and leather-wrapped mirror.","Globe-Trotter","",GTV,[],dt="fibreboard colours · leather corners · gold or chrome fittings"),
  X("Cosmolite beauty case","Curv beauty case issued with the first Cosmolite spinners.","Samsonite","2008",COS,[],dt="black, silver, red")]},
{"n":"Wheeled duffel","a":"rolling duffel · wheeled duffle","d":"Duffel bag on a wheeled frame with a telescoping handle.",
 "t":["two wheels","rigid base","convertible backpack straps","40–100+ L"],
 "s":"https://shop.samsonite.com/luggage",
 "x":[X("Black Hole Wheeled Duffel","Patagonia's two-wheeled duffel in recycled laminated fabric with a collapsible frame and telescoping handle.","Patagonia","",PGD,
    [("Black Hole Wheeled Duffel 40L","Patagonia","","carry-on size, about 3.5 kg"),("Black Hole Wheeled Duffel 70L","Patagonia","",""),("Black Hole Wheeled Duffel 100L","Patagonia","","")],dt="capacity 40, 70, 100 L · colours")],
 "m":[["Detour","Samsonite"]]}]
def B(n,c,f,seg,d,s,sig,lines=(),rel=(),eras=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Rimowa","Germany","1898","Luxury luggage","Cologne maker of grooved aluminium and polycarbonate luggage, owned by LVMH since 2016.",W+"Rimowa",["Rimowa Original","Rimowa Essential"],["Original","Classic","Essential","Hybrid","Distinct"],["Louis Vuitton"]),
 B("Samsonite","United States","1910","Mainstream luggage","Luggage group founded in Denver as the Shwayder Trunk Manufacturing Company; owns Tumi and American Tourister.",W+"Samsonite",["Samsonite tapered suitcase","Cosmolite","Cosmolite beauty case"],["Cosmolite","Freeform","Silhouette"],["Tumi"]),
 B("Tumi","United States","1975","Premium travel and business bags","Ballistic-nylon luggage and bag maker founded by Charlie Clifford, owned by Samsonite since 2016.",W+"Tumi_Inc.",["19 Degree","Alpha"],["Alpha","Alpha Bravo","19 Degree","Tegra-Lite","Arrivé"],["Samsonite"]),
 B("Globe-Trotter","United Kingdom","1897","Luxury luggage","Maker of handmade vulcanised-fibreboard cases, founded in Dresden and now based in London.",W+"Globe-Trotter",["Centenary","Globe-Trotter cabin trunk","Centenary Vanity Case"],["Centenary","Safari","Deluxe"]),
 B("Away","United States","2015","Direct-to-consumer luggage","New York luggage brand founded by Steph Korey and Jen Rubio.",W+"Away_(company)",["The Carry-On"]),
 B("Briggs & Riley","United States","1993","Premium softside luggage","Luggage maker known for its lifetime repair guarantee and expandable cases.",W+"Briggs_%26_Riley",["Baseline"],["Baseline"]),
 B("Louis Vuitton","France","1854","Luxury fashion house","Paris trunk-maker turned fashion house, known for its Monogram and Damier canvases.",W+"Louis_Vuitton",["Malle Courrier","Malle cabine","Boîte Chapeaux"],rel=["Goyard","Moynat"]),
 B("Goyard","France","1853","Luxury trunks and leather goods","Paris trunk-maker known for its chevron Goyardine canvas.",W+"Goyard",["Goyard trunk"],rel=["Louis Vuitton","Moynat"]),
 B("Moynat","France","1849","Luxury trunks and leather goods","Paris trunk-maker, early user of gutta-percha waterproofing, owned by Bernard Arnault's holding since 2010.",W+"Moynat",["Moynat trunk"],rel=["Louis Vuitton","Goyard"]),
 B("Pinel et Pinel","France","2004","Contemporary trunks","Paris trunk and leather-goods house founded by Fred Pinel, making trunks built round objects and pastimes.",PIN,["Pinel et Pinel object trunk"]),
 B("Patagonia","United States","1973","Outdoor apparel","Ventura, California outdoor clothing and gear company founded by Yvon Chouinard.",W+"Patagonia,_Inc.",["Black Hole Wheeled Duffel"])]
traditions=[{"n":"Paris trunk-making (malletier)","g":"Leather & travel goods","r":"Paris, France","p":"19th century–present",
 "d":"French trunk-making houses that built flat, canvas-covered travelling trunks for rail and steamship travel.",
 "tech":"wooden frame covered in canvas or leather, with slats, metal corners, rivets and locks","mat":"poplar, beech, coated canvas, leather, brass",
 "forms":["Travel trunk","Vanity case"],"ctr":["Louis Vuitton","Goyard","Moynat","Au Départ"],
 "auth":"original labels, serial numbers and canvas type date a trunk","s":TR}]
notes=("Kept all four planned kinds (Suitcase k24, Travel trunk k26, Wheeled duffel k25, new Vanity case). Suitcase: 18 flat models + 8 ranges cut to 9 archetypes "
 "(Rimowa Original, Rimowa Essential, Samsonite 1939 suitcase, Cosmolite, Tumi 19 Degree, Tumi Alpha, Globe-Trotter Centenary, Away The Carry-On, Briggs & Riley Baseline); "
 "old Rimowa/Samsonite/Tumi models folded in as versions where they belong. Dropped Samsonite SKUs Elevation Plus, Essens, Hyperflex, Outline Pro, Pivot, Theorym, UpLIFT, Venue X, Voltage DLX "
 "(SKU noise, rule: no SKU lists). Travel trunk: removed Rimowa ranges as briefed; added LV Malle Courrier and malle cabine, Goyard, Moynat, Globe-Trotter, Pinel et Pinel, "
 "maker-free steamer/wardrobe/dome-top patterns and LV Boîte Chapeaux (hat box placed here as no hat-box kind is planned). "
 "Left out for lack of a retrieved page: LV wardrobe trunk (malle armoire) and Nice vanity case, LV Boîte Flacons, Rimowa Classic as a separate archetype year, Tumi Alpha launch year, "
 "Samsonite Curv-era dates beyond 2008. pineletpinel.com and globe-trotter vanity details beyond the product page not retrieved (403/denied).")
out={"kinds":kinds,"brands":brands,"traditions":traditions,"notes":notes}
p="work/A4/shelves/04_00.json"; t=p+".tmp"
json.dump(out,open(t,"w"),ensure_ascii=False,indent=1); os.replace(t,p); print("ok")
