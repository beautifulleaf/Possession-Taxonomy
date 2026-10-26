import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a='',dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[]
kinds.append({"n":"Lounge chair","a":"easy chair · design lounge chair","d":"A designer easy chair made for relaxed, slightly reclined sitting, usually known by its designer and maker.","s":W+"Chair",
 "x":[
  X("Eames Lounge Chair and Ottoman","Herman Miller","1956",W+"Eames_Lounge_Chair","Charles and Ray Eames's moulded-plywood and leather lounge chair with matching ottoman.",
    [("670 and 671 (original)","Herman Miller","1956","US production, continuous since launch"),
     ("Vitra licensed version","Vitra","","European production with Fritz Becker KG"),
     ("Hille licensed version","Hille","1957","ten-year UK licence"),
     ("50th-anniversary edition","Herman Miller","2006","sustainably sourced palisander veneer"),
     ("Tall / XL","Herman Miller","2008","larger size, also made by Vitra as XL"),
     ("Plycraft and other copies","Plycraft","","unlicensed chairs in its style; only Herman Miller and Vitra may use the Eames name")],
    a="Eames Lounge (670) and Ottoman (671)",dt="veneer: Brazilian rosewood (to early 1990s), cherry, walnut, palisander · leather colour · standard or tall/XL · label style dates a chair"),
  X("Barcelona chair","Knoll","1929",W+"Barcelona_chair","Mies van der Rohe and Lilly Reich's steel-framed chair with leather cushions, made for the 1929 Barcelona Pavilion.",
    [("Original bolted frame","","1929","ivory pigskin upholstery"),
     ("Seamless stainless-steel frame","","after 1950","redesign with bovine leather"),
     ("Knoll production","Knoll","1964","chrome or stainless frame; made by Knoll since 1964"),
     ("Barcelona ottoman","Knoll","","matching stool"),
     ("Unlicensed replicas","","","sold under various names")],dt="frame chrome or stainless · leather colour · tufted cushions"),
  X("Grand Confort (LC2 / LC3)","Cassina","1928",W+"Grand_confort","Perriand, Le Corbusier and Jeanneret's 'cushion basket': leather cushions held in a tubular steel frame.",
    [("LC2 Petit Modèle","Cassina","1928","narrower, higher seat and back"),
     ("LC3 Grand Modèle","Cassina","1928","wider and lower")],a="Fauteuil Grand Confort · LC2 · LC3",dt="chrome-plated steel frame · leather colour · armchair or sofa"),
  X("Wassily Chair","Knoll","1925–26",W+"Wassily_Chair","Marcel Breuer's steel-framed chair with stretched straps, designed at the Bauhaus in Dessau.",
    [("Model B3","Thonet","late 1920s","first production; rarest, discontinued in the Second World War"),
     ("Gavina version","Gavina","after 1945","introduced the familiar black leather straps"),
     ("Knoll version","Knoll","1968","Knoll bought Gavina and owns the Wassily name")],a="Model B3",dt="straps: Eisengarn fabric or leather · folding or fixed frame"),
  X("Egg chair","Fritz Hansen","1958–59","https://en.wikipedia.org/wiki/Egg_(chair)","Arne Jacobsen's enclosing high-backed shell chair, created for the SAS Royal Hotel, Copenhagen.",
    [("SAS Royal Hotel original","Fritz Hansen","1958–59","steel frame with fabric cover"),
     ("Egg couch","Fritz Hansen","","very few made, later special edition")],dt="fabric or leather · colour · with or without footstool"),
  X("Swan chair","Fritz Hansen","1958","https://en.wikipedia.org/wiki/Swan_(chair)","Arne Jacobsen's curved shell lounge chair with no straight lines, for the SAS Royal Hotel.",
    [("Swan chair","Fritz Hansen","1958","satin-polished aluminium star base"),
     ("Swan sofa","Fritz Hansen","","two-seat version, still in production")],dt="leather or fabric · colour"),
  X("Womb chair","Knoll","1948","https://www.knoll.com/product/womb-chair","Eero Saarinen's fibreglass-shell lounge chair made to be sat in any position.",
    [("Womb chair, standard","Knoll","1948",""),("Womb chair, medium","Knoll","","smaller size"),("Womb ottoman","Knoll","","standard and medium")],dt="steel frame black, chrome or gold · fabric, suede or leather"),
  X("Paimio chair","Artek","c. 1929–33",W+"Paimio_Chair","Alvar Aalto's cantilevered bent-birch chair designed for the Paimio Sanatorium.",dt="birch frame · lacquered seat colour"),
  X("Red and Blue Chair","","1917–23",W+"Red_and_Blue_Chair","Gerrit Rietveld's wooden armchair, painted black with primary colours from about 1923.",
    [("Unstained beech original","","1917",""),("Painted version","","c. 1923","black with primary colours suggested by Bart van der Leck")],dt="painted or natural wood · no authoritative measurements"),
  X("Ball chair","","1963",W+"Ball_Chair","Eero Aarnio's fibreglass sphere on a pedestal, open on one side and upholstered inside.",
    [("Aarnio prototype","","1963","plywood mould, fibreglass and upholstery"),
     ("Asko exhibition chair","Asko","1966","shown on the Asko stand at the Cologne fair"),
     ("Later versions","","","larger, some with built-in speakers")],a="Globe chair",dt="shell colour · interior upholstery"),
  X("Tongue chair","Artifort","1960s",W+"Artifort","Pierre Paulin's low upholstered lounge chair for Artifort.",dt="stretch fabric colour · sources differ on year"),
  X("Ribbon chair","Artifort","1966",W+"Artifort","Pierre Paulin's upholstered ribbon-form lounge chair for Artifort.",[("Model 582","Artifort","1966","")],dt="fabric colour"),
  X("Mushroom chair","Artifort","1959–60",W+"Pierre_Paulin","Pierre Paulin's lounge chair, the design that made his name at Artifort."),
  X("Coconut chair","Herman Miller","1955","https://en.wikipedia.org/wiki/George_Nelson_(designer)","George Nelson office's lounge chair for Herman Miller, credited to George Mulhauser."),
  X("Diamond chair","Knoll","early 1950s",W+"Harry_Bertoia","Harry Bertoia's lounge chair designed for Knoll.",[("Diamond Lounge Chair","Knoll","","")],dt="wire finish · seat pad or full cover"),
  X("Platner chair","Knoll","1966",W+"Warren_Platner","Warren Platner's nickel-plated steel-rod chairs with upholstered seats, the 'sheaf of wheat' base.",
    [("Easy chair and ottoman","Knoll","1966","reissued"),("Platner Arm Chair","Knoll","","")],dt="over 1,000 welds per base · fabric colour"),
  X("Safari chair","Carl Hansen & Søn","1933",W+"Kaare_Klint","Kaare Klint's lounge chair, made today by Carl Hansen & Søn.",[("KK47000","Carl Hansen & Søn","","current production")],dt="wood · canvas or leather"),
  X("Papa Bear chair","PP Møbler","1950",W+"Hans_Wegner","Hans Wegner's upholstered armchair.",
    [("AP19","Getama","1950","original production; now PP Møbler")],dt="fabric or sheepskin · wood arms"),
  X("Shell chair","Carl Hansen & Søn","1963",W+"Hans_Wegner","Hans Wegner's lounge chair for Carl Hansen & Søn.",[("CH07","Carl Hansen & Søn","1963","designed 1960, short first run")]),
  X("CH25","Carl Hansen & Søn","1949",W+"Hans_Wegner","Hans Wegner's easy chair, presented 1949 and in production from 1950."),
  X("Ox chair","Erik Jørgensen","1960",W+"Hans_Wegner","Hans Wegner's lounge chair, first made by Johannes Hansen.",[("Johannes Hansen original","Johannes Hansen","1960","now made by Erik Jørgensen")]),
 ],
 "m":[["654W Lounge Chair","Knoll"]]})
kinds.append({"n":"Armchair","a":"easy chair · accent chair","d":"An upholstered or framed single seat with arms and back for everyday sitting.","t":["swivel chair","accent chair","tub chair"],
 "s":"https://www.ikea.com/us/en/cat/armchairs-16239/",
 "x":[X("Poäng","IKEA","1976",W+"Poäng","Noboru Nakamura's bent-beech cantilever armchair with cushion, IKEA's mass-market icon.",
       [("Poem","IKEA","1976","original name"),("Poäng","IKEA","1992","renamed"),("Poäng footstool","IKEA","","matching ottoman"),("Poäng low-back","IKEA","","low back with rocking base")],dt="veneer: birch, natural, black-brown · fabric or leather cushion"),
      X("Louis Ghost","Kartell","2000",W+"Philippe_Starck","Philippe Starck's armchair for Kartell; over two million sold.")],
 "m":[["UPPLAND","IKEA"],["EKENASET","IKEA"],["SALTSJOBADEN","IKEA"],["STOCKHOLM 2025","IKEA"],["MORABO","IKEA"],["HAVBERG","IKEA"],["DYVLINGE","IKEA"],["SKALBODA","IKEA"],["4801 armchair","Kartell"],["Ghost chair","Fiam Italia"]]})
kinds.append({"n":"Wingback chair","a":"wing chair · wing-back","d":"A high-backed upholstered easy chair with side wings that block draughts.","t":["flat wing","scroll wing","bat wing","butterfly wing"],
 "s":W+"Wing_chair","m":[["STRANDMON","IKEA"],["OSKARSHAMN","IKEA"]]})
kinds.append({"n":"Club chair","a":"fauteuil club · leather club chair","d":"A deep, low, enveloping armchair, traditionally covered in leather, first made in France.","t":["round back","chapeau de gendarme back","square back","cloud back","moustache back"],
 "s":W+"Club_chair"})
kinds.append({"n":"Recliner","a":"reclining chair · lift chair","d":"An armchair whose back tilts and footrest rises, manually or by motor.","t":["manual","power","rocker recliner","swivel recliner","lift chair"],
 "s":"https://www.ikea.com/us/en/cat/armchairs-16239/",
 "x":[X("Morris chair","Morris & Co.","c. 1866",W+"Morris_chair","Early reclining chair: a hinged back between open arms, set by pegs or notches in the arms.",
        [("Morris & Co. original","Morris & Co.","c. 1866","dark-stained wood, turned spindles"),
         ("American traditional","","c. 1890–1930","carved; cheaper versions from Larkin, Sears, Montgomery Ward; Horner at the top"),
         ("Mission / Craftsman","Gustav Stickley","1904","plain oak, loose leather or fabric cushions")],dt="wood and finish · peg or bar adjustment · cushion cover"),
      X("La-Z-Boy recliner","La-Z-Boy","1928",W+"La-Z-Boy","The American mechanism recliner that grew from Knabusch and Shoemaker's reclining porch chair.",
        [("Wooden reclining chair","La-Z-Boy","1928","patented"),("Upholstered mechanical recliner","La-Z-Boy","1930","patented")],dt="manual or power · lift models")],
 "m":[["GRYTERYD","IKEA"],["ARNASVALL","IKEA"]]})
kinds.append({"n":"Chaise longue","a":"chaise lounge · day sofa","d":"An upholstered indoor seat long enough to support the legs.","s":"https://www.ikea.com/us/en/cat/sofas-armchairs-700640/",
 "x":[X("Récamier","","c. 1800",W+"Chaise_longue","Empire-style chaise with two raised ends and open long sides, named after Madame Récamier."),
      X("Méridienne","","early 1800s",W+"Chaise_longue","Asymmetric daybed with a high head end, low foot end and a sloping back joining them."),
      X("Duchesse brisée","","",W+"Chaise_longue","'Broken' chaise in two or three parts: a chair with a long stool, or two chairs with a stool between."),
      X("LC4 chaise longue","Cassina","1928","https://en.wikipedia.org/wiki/Chaise_Longue_(Le_Corbusier)","Perriand, Le Corbusier and Jeanneret's adjustable steel chaise on a separate base.",
        [("Chaise longue B 306","","1928–30","original model"),("LC4","Cassina","1964","renamed and made by Cassina")],a="B 306")]})
kinds.append({"n":"Rocking chair","a":"rocker · glider","d":"A chair on curved rockers or a glider base that rocks.","t":["glider","platform rocker","folding rocker","ladder-back rocker","pressed-back rocker","wicker rocker"],
 "s":"https://www.withflitch.com/shop/chairs-seating/rocking-chairs?page=8",
 "x":[X("Thonet rocking chair No. 1","Thonet","1860","https://www.dexigner.com/news/18475","Michael Thonet's bentwood rocker, the first rocking chair made of bentwood.",
        [("Schaukel-Fauteuil No. 1","Thonet","1860","made in Koritschan, Moravia"),("Thonet Collect limited edition","Thonet","2009","25 numbered pieces, cane seat and back"),("Michael Thonet Model 1 Rocking Chair","Thonet","","")],dt="beech stain · cane seat and back"),
      X("Boston rocker","","",W+"Rocking_chair","Connecticut-made rocker of oak and pine, painted black and decorated with fruit and flowers."),
      X("Shaker rocker","","19th century",W+"Shaker_furniture","Plain Shaker ladder-back rocking chair with woven seat, made in several sizes."),
      X("Eames RAR","Vitra","1950","https://findmy.vitra.com/en-en/products/lounge-chairs/eames-plastic-armchair-rar","Charles and Ray Eames's moulded plastic armchair shell on a rod base with rockers.",
        [("Eames Plastic Armchair Rocking chair (RAR)","Vitra","","with or without cushion, or fully upholstered")],a="Rocking Armchair Rod base",dt="shell colour · upholstery"),
      X("Iron rocker","","1830s",W+"Rocking_chair","Iron or steel-framed rocker made by R.W. Winfield & Co. and shown at the 1851 Great Exhibition.",[("R.W. Winfield & Co.","R.W. Winfield & Co.","1830s","")],a="Peter Cooper rocker")],
 "m":[["Ercol Chairmakers Rocking Chair","Ercol"],["Noah Rocking Chair","Tutti Bambini"],["Oscar Rocking Chair","Tutti Bambini"]]})
kinds.append({"n":"Slipper chair","d":"A low armless upholstered single chair, used as an occasional or bedroom seat.","s":"https://www.google.com/basepages/producttype/taxonomy.en-US.txt"})
kinds.append({"n":"Hanging chair","a":"egg chair · swing chair","d":"A single seat suspended from a ceiling or a stand.","t":["ceiling-hung","on stand","single","double"],
 "s":"https://simplyhammocks.co.uk/collections/hanging-egg-chairs",
 "x":[X("Hanging Egg Chair","Sika Design","1959","https://artilleriet.se/hanging-egg-chair-natur","Nanna and Jørgen Ditzel's egg-shaped rattan chair hung from a chain.",[("Sika Design rattan","Sika Design","","with cushion and hanging chain")],dt="rattan · cushion fabric"),
      X("Bubble Chair","","1968",W+"Bubble_Chair","Eero Aarnio's clear acrylic sphere chair hung from the ceiling by a chain.",dt="acrylic · cushion colour")],
 "m":[["Globo Single Hanging Egg Chair","Globo"],["Globo Royal Double Seater Hanging Egg Chair","Globo"]]})
kinds.append({"n":"Chair bed","a":"sleeper chair","d":"A single armchair that unfolds or pulls out into a single bed.","s":"https://www.ikea.com/us/en/cat/armchairs-16239/","m":[["IKEA PS 2026","IKEA"]]})
kinds.append({"n":"Bean bag chair","a":"beanbag · sacco","d":"A soft seat of a fabric bag filled with loose beads that takes the sitter's shape.","t":["indoor","outdoor","children's"],
 "s":"https://shop.mohd.it/en/furniture/chaises-longues/bean-bags.html",
 "x":[X("Sacco","Zanotta","1968","https://www.zanotta.com/en-us/products/armchairs/sacco","Gatti, Paolini and Teodoro's pear-shaped bag of polystyrene pellets, the original bean bag.",
        [("Sacco 278","Zanotta","","small"),("Sacco 279","Zanotta","","medium"),("Sacco 280","Zanotta","","large")],dt="Tux or Vip fabric (outdoor) or leather"),
      X("Fatboy Original","Fatboy","1998","https://www.fatboy.com/bg-en/original-landingspagina-indoor.html","Jukka Setälä's large beanbag, the brand's founding product.",
        [("Original","Fatboy","1998","140 × 180 cm, nylon or stonewashed"),("Original Slim","Fatboy","","120 × 155 cm"),("Junior","Fatboy","","100 × 130 cm"),("Buggle-up","Fatboy","","137 × 185 cm, polyester")],dt="cover: nylon, stonewashed, velvet, cord, teddy, terry")],
 "m":[["BonBaron Slim","Fatboy"],["Arnold Bean Bag Chair","Nobodinoz"],["Ziggy Armchair Beanbag","Nobodinoz"],["Float Easy Chair","Paola Lenti"]]})
kinds.append({"n":"Ottoman","a":"pouf · pouffe · footstool · hassock","d":"A padded seat or footrest without back or arms; some have storage.","t":["footstool","pouffe","storage ottoman","hassock"],
 "s":"https://www.ikea.com/us/en/cat/sofas-armchairs-700640/",
 "x":[X("Moroccan leather pouf","","",
        "https://www.moroccancorridor.com/pages/moroccan-leather-poufs-guide","Hand-cut, hand-stitched vegetable-tanned leather pouf from Fez or Marrakech, usually sold unstuffed.",
        dt="shape: round embossed, embroidered, geometric, rectangular · leather colour · stuffed or unstuffed")],
 "m":[["STRANDMON","IKEA"],["SALTSJOBADEN","IKEA"]]})
K='knowledge'
def B(n,c,f,seg,d,sig,s=K,**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"d":d,"sig":sig,"s":s}; b.update(kw); return b
brands=[
 B("Herman Miller","United States","1905","Design furniture","American maker of modern office and home furniture, part of MillerKnoll.",["Eames Lounge Chair and Ottoman","Coconut chair"],rel=["Vitra","Knoll"]),
 B("Vitra","Switzerland","1950","Design furniture","Swiss maker licensed for Eames and Nelson designs in Europe.",["Eames Lounge Chair and Ottoman","Eames RAR"],rel=["Herman Miller"]),
 B("Knoll","United States","1938","Design furniture","American modernist maker holding rights to Mies, Breuer, Saarinen, Bertoia and Platner designs.",["Barcelona chair","Wassily Chair","Womb chair","Diamond chair","Platner chair"],rel=["Herman Miller"]),
 B("Fritz Hansen","Denmark","1872","Design furniture","Danish maker of Arne Jacobsen's furniture.",["Egg chair","Swan chair"]),
 B("Cassina","Italy","1927","Design furniture","Italian maker licensed for Le Corbusier, Jeanneret and Perriand furniture.",["Grand Confort (LC2 / LC3)","LC4 chaise longue"]),
 B("Artek","Finland","1935","Design furniture","Finnish company founded to sell Alvar Aalto's furniture.",["Paimio chair"]),
 B("Artifort","Netherlands","1890","Design furniture","Dutch upholstered-furniture maker known for Pierre Paulin's 1960s chairs.",["Tongue chair","Ribbon chair","Mushroom chair"],s=W+"Artifort"),
 B("Carl Hansen & Søn","Denmark","1908","Design furniture","Danish maker of Hans Wegner and Kaare Klint designs.",["Safari chair","Shell chair","CH25"]),
 B("PP Møbler","Denmark","1953","Design furniture","Danish cabinetmaker producing Hans Wegner designs.",["Papa Bear chair"]),
 B("Erik Jørgensen","Denmark","1954","Design furniture","Danish upholstered-furniture maker producing Wegner's Ox chair.",["Ox chair"]),
 B("IKEA","Sweden","1943","Mass-market flat-pack","Swedish flat-pack furniture retailer.",["Poäng"]),
 B("Kartell","Italy","1949","Design plastics","Italian maker of moulded-plastic furniture.",["Louis Ghost"]),
 B("Zanotta","Italy","1954","Design furniture","Italian maker of the original Sacco bean bag.",["Sacco"]),
 B("Fatboy","Netherlands","1998","Lifestyle furniture","Dutch brand built on Jukka Setälä's Original beanbag.",["Fatboy Original"]),
 B("Thonet","Germany","1819","Bentwood and tubular steel","Bentwood furniture maker founded by Michael Thonet.",["Thonet rocking chair No. 1"]),
 B("Morris & Co.","United Kingdom","1861","Arts and Crafts furnishings","William Morris's decorating firm, origin of the Morris reclining chair.",["Morris chair"]),
 B("La-Z-Boy","United States","1927","Recliners and upholstery","American recliner maker founded by Edward Knabusch and Edwin Shoemaker in Monroe, Michigan.",["La-Z-Boy recliner"],s=W+"La-Z-Boy"),
 B("Sika Design","Denmark","","Rattan furniture","Danish rattan maker producing Nanna Ditzel's Hanging Egg Chair.",["Hanging Egg Chair"]),
 B("Ercol","United Kingdom","1920","Solid-wood furniture","British solid-wood furniture maker founded by Lucian Ercolani.",[]),
]
for b in brands:
    if not b["f"]: del b["f"]
trads=[
 {"n":"Moroccan leatherwork","g":"Leather & hides","r":"Morocco (Fez, Marrakech)","p":"traditional, continuing","d":"Vegetable-tanned leather hand-cut and hand-stitched into poufs and other goods.",
  "tech":"vegetable tanning with plant tannins; hand cutting; stitched embroidery on the top panel; hand assembly","mat":"cow and goat leather, thread",
  "forms":["Moroccan leather pouf"],"ctr":["Fez tanneries (Chouara, Sidi Moussa, Ain Azliten)","Marrakech"],
  "auth":"supple leather with grain variation; slightly irregular hand stitching; embroidery stitched through, not printed","s":"https://www.moroccancorridor.com/pages/moroccan-leather-poufs-guide"},
 {"n":"Shaker furniture","g":"Woodwork & furniture","r":"United States (New England, New York, Kentucky)","p":"19th century","d":"Plain, functional furniture made by Shaker communities, including ladder-back and rocking chairs.",
  "tech":"turned posts, ladder backs, woven seats","mat":"native hardwoods, woven seat material","forms":["Shaker rocker","ladder-back chair"],"ctr":["New Lebanon community","Shaker Village, Harrodsburg"],
  "auth":"","s":W+"Shaker_furniture"},
]
notes=("Lounge chair is new (design classics moved out of the old armchair list); Wingback and Club chair are new kinds. "
 "Armchair trimmed from 35 flat models (16 IKEA) to 10 plus Poäng and Louis Ghost archetypes; old IKEA 'r' range lists dropped as duplicated brand ranges. "
 "Dropped models: LILLESATER, OSKARSHAMN (moved to wingback), PERSBOL, HERRAKRA, SOTENAS, ROCKSJON (IKEA SKU noise); blank-maker 'Hanging Egg Chair' (now Ditzel archetype). "
 "Left out for lack of a retrievable source this session: Windsor rocker, Queen Anne wingback, Stressless (Ekornes), Ditzel chair's original maker (Wengler), Tongue chair model number (577) and exact year (sources say 1963/1967/1968), Red and Blue Chair's current maker (Cassina), Ball/Bubble chair makers, Pastil chair. "
 "Wikidata was rate-limited (HTTP 429); cassina.com, moma.org, brooklynmuseum.org, twentytwentyone.com blocked (403) and not retried. "
 "Archetype mk for design classics is the current licensed maker; the designer is named in d. Rocking-chair models from Tutti Bambini are nursing rockers.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B1/shelves/00_01.json'
open(p+'.tmp','w').write(json.dumps(out,ensure_ascii=False,indent=1)); os.replace(p+'.tmp',p)
print('written', len(kinds), sum(len(k.get('x',[])) for k in kinds), len(brands))
