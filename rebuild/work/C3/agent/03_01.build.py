import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'; OLD='https://mountaincrestgardens.com/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='plant size · pot size',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
LS='https://scrapbooklithops.com/lsb5-book.html'
kinds=[
 {"n":"Crassula","a":"jade plant · money plant · string of buttons","d":"Living succulent of the genus Crassula, including the jade plant (C. ovata); cultivated kinds come mostly from South Africa's Eastern Cape.",
  "t":["shrubby","stacked","trailing","variegated"],"s":OLD,"x":[
  X("Crassula ovata","jade plant · lucky plant · money plant · money tree","Southern African evergreen shrub with thick shiny jade-green leaves in opposite pairs and winter star flowers.",W+"Crassula_ovata",
    v=[("'Gollum'","","","tubular leaves; synonym of 'Monstruosa'; "+AGM),("'Hobbit'","","","tubular, red-tinted leaves; synonym of 'Monstruosa'"),("'Hummel's Sunset'","","",AGM),("'Tricolor'","","","cream, white and green variegation; 'Lemon & Lime'"),("'Crosby's Compact'","","","miniature with small red leaves"),("'Undulata'","","","curly leaves")],dt="leaf form · variegation · bush or tree-trained"),
  X("Crassula perforata","string of buttons · sosatieplakkie","Stacked-leaf crassula known as string of buttons.",W+"Crassula"),
  X("Crassula arborescens","silver dollar plant · beestebul","Shrubby crassula known as silver dollar plant.",W+"Crassula"),
  X("Crassula muscosa","rattail crassula · watch chain · zipper plant · C. lycopodioides","Crassula known as rattail crassula or watch chain.",W+"Crassula"),
  X("Crassula capitella","","Crassula with the cultivars 'Campfire' and 'Red Pagoda'.",W+"Crassula",v=[("'Campfire'","","",""),("subsp. thyrsiflora 'Red Pagoda'","","","")]),
  X("Crassula pellucida var. marginalis 'Petite Bicolor'","Calico Kitten","Trailing variegated crassula cultivar, sometimes sold as 'Calico Kitten'.",W+"Crassula"),
  ],"m":[["'Buddha's Temple'",""],["'Ivory Pagoda'",""],["'Morgan's Beauty'",""],["'Tom Thumb'",""]]},
 {"n":"Kalanchoe","a":"flaming Katy · panda plant · mother of thousands","d":"Living succulent of the genus Kalanchoe, from florist flowering kalanchoes to foliage species.",
  "t":["single-flowered","double-flowered","foliage","plantlet-bearing"],"s":OLD,"x":[
  X("Kalanchoe blossfeldiana","flaming Katy · Christmas kalanchoe · florist kalanchoe","Bushy Madagascan succulent with four-petalled flowers in red to white, introduced by Robert Blossfeld in 1932.",W+"Kalanchoe_blossfeldiana",y="1932",
    v=[("Calandiva","","","double-flowered cultivar line")],dt="flower colour · single or double · pot size"),
  X("Kalanchoe daigremontiana","mother of thousands · alligator plant · Mexican hat plant · devil's backbone","Southwest Madagascan succulent that spreads by plantlets on its leaf margins; toxic.",W+"Kalanchoe_daigremontiana",
    v=[("× houghtonii","","","hybrid with K. delagoensis; narrower leaves")]),
  X("Kalanchoe tomentosa","panda plant","Species known as panda plant.",W+"Kalanchoe"),
  X("Kalanchoe luciae","paddle plant","Species known as paddle plant.",W+"Kalanchoe"),
  X("Kalanchoe thyrsiflora","flapjacks · desert cabbage · white lady","Species with flat leaves, known as flapjacks.",W+"Kalanchoe"),
  X("Kalanchoe beharensis","velvet leaf · felt plant · felt bush","Species with felted leaves.",W+"Kalanchoe"),
  ],"m":[["'Tessa'",""],["'Wendy'",""]]},
 {"n":"Sedum","a":"stonecrop","d":"Living succulent of the genus Sedum (stonecrop), hardy and tender, with allied Phedimus and Hylotelephium sold as sedums.",
  "t":["trailing","ground cover","upright","tender","hardy"],"s":OLD,"x":[
  X("Sedum morganianum","donkey tail · burro's tail","Micro-endemic Veracruz succulent with trailing stems of fleshy blue-green leaves; "+AGM+".",W+"Sedum_morganianum",
    v=[("'Burrito'","","","")],dt="trail length · hanging pot"),
  X("Phedimus spurius","Sedum spurium · Caucasian stonecrop · two-row stonecrop","Creeping Caucasian stonecrop with red-edged leaves and flat flower clusters.",W+"Phedimus_spurius",
    v=[("'Schorbuser Blut' ('Dragon's Blood')","","","red-edged leaves darkening in autumn; "+AGM),("'Voodoo'","","","very dark red leaves"),("'Tricolor'","","","green, cream and wine-red leaves"),("'Fulda Glut'","","",""),("'Red Carpet'","","",""),("'Album'","","","")],dt="leaf colour · flower colour"),
  X("Sedum rubrotinctum","jellybeans · pork and beans · Christmas cheer","Widely grown ornamental stonecrop with bean-like leaves.",W+"Sedum"),
  X("Sedum acre","biting stonecrop · wall-pepper · goldmoss stonecrop","European stonecrop with a peppery taste.",W+"Sedum"),
  X("Sedum nussbaumerianum","golden sedum · S. adolphii","Golden stonecrop.",W+"Sedum"),
  X("Hylotelephium 'Herbstfreude'","Sedum 'Autumn Joy'","Tall border stonecrop hybrid, often sold as Sedum; "+AGM+".",W+"Sedum",v=[("'Matrona'","","",AGM),("'Ruby Glow'","","",AGM),("'Bertram Anderson'","","",AGM)]),
  ]},
 {"n":"Living stones","a":"Lithops · pebble plants · flowering stones","d":"Living stone-like succulent of the genus Lithops from Namibia and South Africa, each body a pair of fused leaves.",
  "t":["species form","registered cultivar"],"s":OLD,"x":[
  X("Lithops lesliei","","Summer-rainfall South African species growing in rocky grassland.",W+"Lithops_lesliei",
    v=[("var. venteri","","",""),("var. rubrobrunnea 'Roasted Chestnut'","","","registered cultivar")],dt="Cole (C) colony number · window pattern · colour"),
  X("Lithops karasmontana","","Namibian species named after the Great Karas Mountains; "+AGM+".",W+"Lithops",dt="Cole (C) colony number · colour form"),
  X("Lithops optica","","Critically endangered Lüderitz species with rounded eye-like windows.",W+"Lithops_optica",
    v=[("'Rubra'","","","purple-red; most commonly cultivated form")],dt="Cole (C) colony number · colour"),
  X("Lithops aucampiae","","Species named after Juanita Aucamp; listed as Vulnerable.",W+"Lithops",dt="Cole (C) colony number · colour form"),
  X("Lithops bromfieldii","","Accepted Lithops species with the registered cultivar 'Dome'.",LS,v=[("'Dome'","","","")]),
  X("Lithops pseudotruncatella","","Accepted Lithops species with the registered cultivar 'Winter Forest'.",LS,v=[("subsp. groendrayensis 'Winter Forest'","","","")]),
  ]},
 {"n":"Succulent euphorbia","a":"Euphorbia · baseball plant · African milk tree · crown of thorns","d":"Living succulent or cactus-like spurge of the genus Euphorbia; toxic latex.",
  "t":["globular","columnar","shrubby","variegated"],"s":OLD,"x":[
  X("Euphorbia obesa","baseball plant","Thornless ball-shaped Karoo euphorbia with eight ridges; CITES Appendix II; "+AGM+".",W+"Euphorbia_obesa",
    v=[("subsp. obesa","","",""),("subsp. symmetrica","","1941","discovered 1941")],dt="size · male or female"),
  X("Euphorbia trigona","African milk tree · cathedral cactus · Abyssinian euphorbia","Upright Central African succulent shrub with ridged stems, known only from cultivation.",W+"Euphorbia_trigona",
    v=[("'Royal Red'","","","")],dt="height · green or red"),
  X("Euphorbia milii","crown of thorns · Christ plant · Christ's thorn","Spiny Madagascan subshrub with red, pink or white bracts, introduced to France in 1821; "+AGM+".",W+"Euphorbia_milii",y="1821",
    v=[("var. splendens","","",AGM),("Thai hybrids","","","much thicker stems"),("var. hislopii","","","")],dt="bract colour · stem thickness · variegation"),
  ]},
 {"n":"String-of-pearls","a":"Curio · Senecio rowleyanus · string of beads · string of bananas","d":"Living trailing succulent of the genus Curio (formerly Senecio) with bead-like leaves.",
  "t":["green","variegated"],"s":W+"Curio_rowleyanus","x":[
  X("Curio rowleyanus","string-of-pearls · string-of-beads · Senecio rowleyanus","Creeping South African succulent vine with pea-sized windowed leaves on trailing stems.",W+"Curio_rowleyanus",
    v=[("'Variegata'","","","")],dt="trail length · hanging pot"),
  X("Curio radicans","string of bananas","Close relative with banana-shaped windowed leaves.",W+"Curio_rowleyanus"),
  X("Curio herreanus","string of watermelons · string of beads","Relative with teardrop-shaped leaves.",W+"Curio_rowleyanus"),
  ]},
 {"n":"Conophytum","a":"cone plants · dumplings · button plants · knopies","d":"Living dwarf succulent of the genus Conophytum (Aizoaceae), each body a pair of fused leaves, from Namibia and the Cape.",
  "t":["globular","bilobed","tubular"],"s":W+"Conophytum","x":[
  X("Conophytum calculus","","Conophytum species.",W+"Conophytum"),
  X("Conophytum burgeri","","Conophytum species.",W+"Conophytum"),
  X("Conophytum bilobum","","Conophytum species.",W+"Conophytum"),
  X("Conophytum obcordellum","","Conophytum species.",W+"Conophytum"),
  X("Conophytum ectypum","","Conophytum species.",W+"Conophytum"),
  ]},
 {"n":"Caudiciform","a":"caudex plant · fat plant · pachycaul","d":"Living succulent with a swollen water-storing stem or root (caudex), grown by collectors.",
  "t":["tree-like","above-ground caudex","climbing"],"s":W+"Caudiciform","x":[
  X("Adenium obesum","desert rose · Sabi star · impala lily · mock azalea","African and Arabian succulent shrub with a swollen basal caudex and pink-red flowers; popular as bonsai; "+AGM+".",W+"Adenium_obesum",
    v=[("subsp. socotranum","","","Socotra; very wide base"),("subsp. arabicum","","",""),("subsp. somalense","","",""),("subsp. oleifolium","","","smallest"),("subsp. swazicum","","","")],dt="caudex shape · flower colour · grafted or seed-grown"),
  X("Pachypodium lamerei","Madagascar palm","Spiny Madagascan pachycaul tree.",W+"Pachypodium",dt="height"),
  X("Pachypodium brevicaule","mini Pachypodium","Pachypodium sold as mini Pachypodium.",W+"Pachypodium"),
  X("Pachypodium gracilius","graceful Pachypodium","Madagascan pachypodium with a swollen trunk.",W+"Pachypodium"),
  X("Pachypodium namaquanum","halfmens","Southern African pachypodium.",W+"Pachypodium"),
  X("Dioscorea elephantipes","elephant's foot yam · Hottentot bread","South African winter-growing climber with a corky, partly buried caudex; "+AGM+".",W+"Dioscorea_elephantipes",dt="caudex size"),
  ]},
]
w('C3','03_01',{"kinds":kinds,"brands":[],"traditions":[],"notes":"All five planned old kinds kept with old s; three new kinds (String-of-pearls, Conophytum, Caudiciform) sourced to Wikipedia. Specific Lithops Cole (C) numbers left out: BCSS field-number database blocked (403) and llifle mirror failed; C-number kept as a detail axis. Calandiva breeder not named on retrieved page, so no brand entry. No traditions."})
