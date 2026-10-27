import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'; OLD='https://mountaincrestgardens.com/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='plant size · pot size',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
kinds=[
 {"n":"Mammillaria","a":"pincushion cactus · old lady cactus · ladyfinger cactus","d":"Living cactus of the genus Mammillaria, mostly Mexican, with nipple-like tubercles.",
  "t":["solitary","clustering","crested"],"s":OLD,"x":[
  X("Mammillaria elongata","ladyfinger cactus · gold lace cactus","Clustering central Mexican cactus with finger-like stems and golden spines; "+AGM+".",W+"Mammillaria_elongata",
    v=[("'Copper King'","","",""),("'Cristata'","","","brain cactus; crested"),("Golden Stars","","",""),("'Julio'","","",""),("'Golden Nugget'","","","")],dt="spine colour · clump size · crested or normal"),
  X("Mammillaria hahniana","old lady cactus","Globular central Mexican cactus covered in white down and spines, with a ring of red-purple flowers; "+AGM+".",W+"Mammillaria_hahniana",dt="hair density · clump size"),
  X("Mammillaria plumosa","feather cactus","Mammillaria known as feather cactus.",W+"Mammillaria"),
  X("Mammillaria spinosissima","","Mammillaria species with the cultivar 'Un Pico'.",W+"Mammillaria",v=[("'Un Pico'","","","")]),
  X("Mammillaria bocasana","","Commonly illustrated Mammillaria species.",W+"Mammillaria"),
  ]},
 {"n":"Astrophytum","a":"star cactus · bishop's cap · sand dollar cactus","d":"Living cactus of the genus Astrophytum, six species from Texas and Mexico, often spineless and flecked with white trichomes.",
  "t":["spineless","spined","trichome pattern"],"s":OLD,"x":[
  X("Astrophytum asterias","sand dollar cactus · sea urchin cactus · star cactus · star peyote","Small spineless squat cactus of the Rio Grande Valley with woolly areoles; CITES Appendix I.",W+"Astrophytum_asterias",
    v=[("'Super Kabuto'","","","clonal selection with large trichomes in dense spots")],dt="trichome pattern · rib count · size"),
  X("Astrophytum myriostigma","bishop's cap · bishop's hat · bishop's mitre cactus","Spineless Mexican highland cactus with usually five ribs and white trichome coating; "+AGM+".",W+"Astrophytum_myriostigma",
    v=[("var. nudum","","","lacks the trichome coating"),("var. quadricostatum","","","four ribs"),("var. tricostatum","","","three ribs")],dt="rib count · trichome cover"),
  X("Astrophytum ornatum","bishop's cap · monk's hood cactus","Central Mexican plateau species.",W+"Astrophytum"),
  X("Astrophytum capricorne","goat's horn cactus","Coahuila species.",W+"Astrophytum"),
  X("Astrophytum caput-medusae","","Nuevo León species.",W+"Astrophytum"),
  ]},
 {"n":"Gymnocalycium","a":"chin cactus · moon cactus · Hibotan","d":"Living cactus of the genus Gymnocalycium, including grafted colourful moon cacti.",
  "t":["own-root","grafted"],"s":OLD,"x":[
  X("Moon cactus","Gymnocalycium mihanovichii 'Hibotan' · Hibotan · grafted cactus","Chlorophyll-less coloured mutant of G. mihanovichii grafted on a Hylocereus stock; the first such mutants were named 'Hibotan'.",W+"Gymnocalycium_mihanovichii",
    v=[("'Hibotan'","","","first totally de-chlorophyllised mutants"),("'Nishiki'","","","keeps chlorophyll; deep brown")],dt="colour (red, orange, yellow, pink, purple, white) · rootstock (Hylocereus, Trichocereus, Cereus)"),
  X("Gymnocalycium mihanovichii","chin cactus","Spherical grey-green Paraguayan and Bolivian cactus with eight narrow ribs, discovered in 1903.",W+"Gymnocalycium_mihanovichii",y="1903"),
  ]},
 {"n":"Echinopsis","a":"hedgehog cactus · Easter lily cactus · Lobivia · Trichocereus · peanut cactus","d":"Living cactus of the genus Echinopsis (including Lobivia, Chamaecereus and Trichocereus), from South America.",
  "t":["globular","clustering","columnar","hybrid"],"s":OLD,"x":[
  X("Echinopsis oxygona","E. eyriesii · Easter lily cactus","Type species of the genus under its current name, formerly E. eyriesii.",W+"Echinopsis"),
  X("Echinopsis chamaecereus","peanut cactus · Chamaecereus silvestrii","Argentine and Bolivian cactus with slender stems and orange flowers; "+AGM+".",W+"Echinopsis_chamaecereus"),
  X("Echinopsis hybrids","Trichopsis","Hybrids mostly between similar species, such as E. pachanoi × E. eyriesii.",W+"Echinopsis",v=[("'Trichopsis pachaniesii'","","","E. pachanoi × E. eyriesii; sold by Sacred Succulents")],dt="flower colour · body form"),
  ]},
 {"n":"Prickly pear","a":"Opuntia · bunny ears · nopal · paddle cactus","d":"Living prickly-pear cactus of the genus Opuntia, with flat pad-like stems.",
  "t":["hardy","tender","spined","glochid-only"],"s":OLD,"x":[
  X("Opuntia microdasys","bunny ears · angel's-wings · polka-dot cactus","Mexican shrubby prickly pear with pads bearing white or yellow glochids instead of spines; "+AGM+".",W+"Opuntia_microdasys",dt="glochid colour · pad size"),
  X("Opuntia ficus-indica","Indian fig · Barbary fig","Large trunk-forming prickly pear, the most common culinary species.",W+"Opuntia"),
  X("Opuntia humifusa","","Eastern US prickly pear of sandy coastal scrub.",W+"Opuntia"),
  X("Opuntia engelmannii","","Prickly pear species.",W+"Opuntia"),
  ]},
 {"n":"Christmas cactus","a":"Schlumbergera · Thanksgiving cactus · holiday cactus · crab cactus · Easter cactus","d":"Living epiphytic cactus of the genus Schlumbergera (and the allied Easter cactus) with flat stem segments and winter flowers.",
  "t":["Truncata Group","Buckleyi Group","Reginae Group"],"s":W+"Schlumbergera","x":[
  X("Schlumbergera × buckleyi","Christmas cactus · Buckleyi Group","Hybrid of S. truncata × S. russelliana made in England by W. Buckley, first recorded in 1852; rounded stem teeth.",W+"Schlumbergera",y="1852",
    v=[("'Buckleyi'","","1852","thought to be the original Christmas cactus")],dt="flower colour · pot size"),
  X("Schlumbergera truncata","Thanksgiving cactus · crab cactus · Truncata Group","Brazilian species with pointed stem teeth, in European cultivation by 1818; parent of the Truncata Group.",W+"Schlumbergera",y="1818",
    v=[("'Gold Charm'","","","first commercial true yellow; sterile triploid")],dt="flower colour · pot size"),
  X("Reginae Group","S. orssichiana hybrids","Cultivars derived from hybrids with S. orssichiana, used from the 1980s.",W+"Schlumbergera",y="1980s",v=[("'Bristol Queen'","","","one of the first")]),
  X("Rhipsalidopsis gaertneri","Easter cactus · Whitsun cactus · Hatiora gaertneri","Southern Brazilian epiphyte with scarlet spring flowers, a separate genus from Schlumbergera; "+AGM+".",W+"Hatiora_gaertneri",dt="flower colour"),
  ]},
 {"n":"Golden barrel cactus","a":"Kroenleinia grusonii · Echinocactus grusonii · golden ball · mother-in-law's cushion","d":"Living golden barrel cactus, a large ribbed yellow-spined globe endemic to east-central Mexico.",
  "s":W+"Echinocactus_grusonii","x":[
  X("Kroenleinia grusonii","golden barrel cactus · Echinocactus grusonii","Endangered Querétaro and Hidalgo cactus with 21–35 ribs and yellow spines, moved to its own genus in 2014; "+AGM+".",W+"Echinocactus_grusonii",
    v=[("white-spined form","","",""),("short-spined form","","",""),("'Blue barrel'","","","teal-blue"),("nearly spineless form","","","")],dt="spine colour · diameter"),
  ]},
 {"n":"Ariocarpus","a":"living rock cactus","d":"Living nearly spineless cactus of the genus Ariocarpus from Mexico and Texas, rare in the wild.",
  "s":W+"Ariocarpus","x":[
  X("Ariocarpus fissuratus","","Species of northern Mexico and Texas.",W+"Ariocarpus"),
  X("Ariocarpus kotschoubeyanus","","Coahuila and Nuevo León species.",W+"Ariocarpus"),
  X("Ariocarpus retusus","","Mexican species.",W+"Ariocarpus"),
  X("Ariocarpus trigonus","","Tamaulipas and Nuevo León species.",W+"Ariocarpus"),
  X("Ariocarpus agavoides","","Mexican species, occasionally spined.",W+"Ariocarpus"),
  X("Ariocarpus scaphirostris","","Nuevo León species.",W+"Ariocarpus"),
  ]},
 {"n":"Columnar cactus","a":"Cereus · Pilosocereus · Trichocereus · San Pedro · tree cactus","d":"Living upright column-forming cactus, such as Cereus, Pilosocereus and Trichocereus, grown in pots or gardens.",
  "t":["normal","monstrose","crested"],"s":W+"Cereus_(plant)","x":[
  X("Cereus repandus","","South American columnar cactus with edible fruits, grown as a living fence.",W+"Cereus_(plant)",dt="height · monstrose or normal"),
  X("Cereus jamacaru","","Tall Brazilian Cereus with nocturnal flowers.",W+"Cereus_(plant)"),
  X("Cereus forbesii","","Cereus species of Argentina, Bolivia and Paraguay.",W+"Cereus_(plant)"),
  X("Pilosocereus pachycladus","P. azureus","Blue columnar tree cactus with hairy areoles and golden spines.",W+"Pilosocereus",dt="height · blue intensity"),
  X("Echinopsis pachanoi","San Pedro cactus · Trichocereus pachanoi · huachuma","Fast-growing Andean columnar cactus with night-opening white flowers; grown legally as an ornamental in many countries.",W+"Echinopsis_pachanoi",
    v=[("'Ogunbodede'","","","prized cultivar"),("'Vilcabamba A'","","","prized cultivar"),("'Yowie'","","","prized cultivar"),("Predominant Cultivar (PC)","","","fast-growing rootstock")],dt="spination · stem colour · height"),
  ]},
 {"n":"Rhipsalis","a":"mistletoe cactus","d":"Living epiphytic cactus of the genus Rhipsalis (mistletoe cactus) with slender hanging stems.",
  "t":["thread-stemmed","flat-stemmed","bristly"],"s":OLD,"x":[
  X("Rhipsalis baccifera","mistletoe cactus","The widest-ranging species, native to the Americas, Africa, Madagascar and Sri Lanka.",W+"Rhipsalis",dt="trail length"),
  X("Rhipsalis cereuscula","","South American Rhipsalis species.",W+"Rhipsalis"),
  X("Rhipsalis pilocarpa","","Brazilian species with stems and fruits densely covered in bristles.",W+"Rhipsalis"),
  X("Rhipsalis paradoxa","","Brazilian Rhipsalis species.",W+"Rhipsalis"),
  X("Rhipsalis ewaldiana","","Rio de Janeiro Rhipsalis species.",W+"Rhipsalis"),
  ]},
 {"n":"Orchid cactus","a":"Epiphyllum · epis · leaf cactus · climbing cactus","d":"Living epiphytic cactus of the genus Epiphyllum or its large-flowered hybrids (epis).",
  "t":["species","hybrid"],"s":W+"Epiphyllum","x":[
  X("Epiphyllum hybrids","epis · epiphyllums","Artificial hybrids from tribe Hylocereeae, chiefly Disocactus, grown for their large flowers.",W+"Epiphyllum",dt="flower colour · flower size"),
  X("Epiphyllum oxypetalum","broad-leaved epiphyllum","Central American species with large, strongly fragrant flowers.",W+"Epiphyllum"),
  X("Epiphyllum phyllanthus","","Type species, from Mexico to Argentina.",W+"Epiphyllum"),
  ]},
]
w('C3','03_02',{"kinds":kinds,"brands":[],"traditions":[],"notes":"All six planned old kinds kept with old s; five new kinds (Christmas cactus, Golden barrel cactus, Ariocarpus, Columnar cactus, Orchid cactus) sourced to Wikipedia. Easter cactus placed in Christmas cactus kind. Japanese Astrophytum lines other than 'Super Kabuto' and Ariocarpus cultivars left out (not on retrieved pages). Sacred Succulents named as seller of an Echinopsis hybrid on Wikipedia, no brand entry. No traditions."})
