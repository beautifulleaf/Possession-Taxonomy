import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'; OLD='https://mountaincrestgardens.com/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='rosette size · leaf colour · pot size',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
kinds=[
 {"n":"Echeveria","a":"Mexican hens and chicks","d":"Living rosette succulent of the genus Echeveria, from Mexico, Central America and north-western South America.",
  "t":["species","hybrid cultivar","variegated","crested"],"s":OLD,"x":[
  X("Echeveria elegans","Mexican snowball · Mexican gem · white Mexican rose · E. potosina","Compact Mexican species with pale blue-green rosettes and pink, yellow-tipped flowers; "+AGM+".",W+"Echeveria_elegans",dt="rosette size · clump size"),
  X("Echeveria agavoides","lipstick echeveria","Stemless central Mexican species with pointed green leaves, often red-edged; "+AGM+".",W+"Echeveria_agavoides",
    v=[("'Lipstick'","","","neon-green leaves with red edges"),("'Ebony'","","","pale leaves with dark brown edges"),("'Victor Reiter'","","",""),("'Aquamarine'","","",""),("'Luming'","","",""),("'Oculus'","","","all burgundy-red"),("'Rose Garnet'","","",""),("'Rubra'","","",""),("'Salu'","","",""),("var. corderoyi","","",""),("var. prolifera","","","")],dt="leaf colour · edge colour · rosette size"),
  X("Echeveria lilacina","ghost echeveria · Mexican hens and chicks","Slow-growing Nuevo León species with silvery-grey rosettes and coral flowers.",W+"Echeveria_lilacina"),
  X("Echeveria 'Perle von Nürnberg'","Perle von Nurnberg","German garden hybrid of E. gibbiflora var. metallica × E. potosina with pearly purple-blue rosettes; "+AGM+".",'https://llifle.com/Encyclopedia/SUCCULENTS/Family/Crassulaceae/21882/Echeveria_cv._Perle_Von_Nurnberg',dt="rosette size · colour intensity"),
  X("Echeveria 'Lola'","Lola","Dick Wright's 1980 Californian hybrid of E. lilacina with pale grey-blue, pink-blushed rosettes.",'https://www.epicgardening.com/echeveria-lola/',y="1980",dt="rosette size"),
  X("Echeveria derenbergii","","Mexican species; "+AGM+".",W+"Echeveria"),
  X("Echeveria setosa","","Mexican species; "+AGM+".",W+"Echeveria"),
  X("Echeveria secunda var. glauca 'Compton Carousel'","Compton Carousel","Variegated cultivar of E. secunda var. glauca; "+AGM+".",W+"Echeveria"),
  X("Echeveria runyonii 'Topsy Turvy'","Topsy Turvy","Cultivar of E. runyonii; "+AGM+".",W+"Echeveria"),
  X("Echeveria × gilva","","Hybrid group including 'Blue Surprise' and 'Red'.",W+"Echeveria",v=[("'Blue Surprise'","","",""),("'Red'","","","")]),
  ],
  "m":[["'Black Prince'",""],["'Doris Taylor'",""],["'Blue Curl'",""],["'Frank Reinelt'",""],["'Painted Lady'",""],["'Worfield Wonder' (E. × derosa)",""],["'Oliver' (E. pulvinata)",""]]},
 {"n":"Haworthia","a":"Haworthiopsis · Tulista · zebra plant · window haworthia","d":"Living small southern African succulent of the genus Haworthia or its split-off genera Haworthiopsis and Tulista.",
  "t":["windowed","tuberculate (zebra)","retuse","variegated","Japanese hybrid"],"s":OLD,"x":[
  X("Haworthia truncata","horse's teeth","Little Karoo species with squared-off windowed leaves in two rows; the focus of intensive Japanese breeding.",W+"Haworthia_truncata",
    v=[("var. maughanii","","","rounded leaves in a spiral rosette, Calitzdorp"),("'Lime Green'","","","hybrid with lime-green vein netting"),("'Milky Way'","Myron Kimnach","1950s","cross of two thick-leaved clones; milky windows")],dt="window pattern · leaf colour · variegation"),
  X("Haworthia cooperi","","Highly variable Eastern Cape species forming clumps of small rosettes with translucent leaf tips.",W+"Haworthia_cooperi",
    v=[("var. pilifera","","","most common and widespread"),("var. truncata","","",""),("var. venusta","","","furry compact leaves"),("var. leightonii","","","highly proliferous"),("var. picturata","","",""),("var. dielsiana","","","")],dt="window clarity · bristles · clump size"),
  X("Haworthiopsis attenuata","zebra haworthia · Haworthia attenuata","Eastern Cape species with white-tubercled leaves on both faces; often mistaken for the rarer H. fasciata.",W+"Haworthiopsis_attenuata",
    v=[("var. attenuata","","",""),("var. radula","","","hankey dwarf aloe"),("var. glabrata","","","")],dt="tubercle banding · rosette size"),
  X("Haworthia cymbiformis","","Fairly common house and garden species.",W+"Haworthia"),
  X("Haworthia retusa","","Species shown among commonly grown haworthias.",W+"Haworthia"),
  X("Haworthia magnifica var. splendens","Haworthia splendens","Variety prized by horticulturalists.",W+"Haworthia"),
  ]},
 {"n":"Aloe","a":"aloe vera · spiral aloe","d":"Living succulent of the genus Aloe, native to Africa, Madagascar and Arabia, grown in pots and gardens.",
  "t":["species","hybrid cultivar","variegated"],"s":OLD,"x":[
  X("Aloe vera","Barbados aloe · Chinese aloe · medicinal aloe","Stemless Arabian aloe with fleshy grey-green toothed leaves, the classic houseplant aloe; "+AGM+".",W+"Aloe_vera",
    v=[("var. chinensis","","","spotted form")],dt="plant size · pot size"),
  X("Aloe polyphylla","spiral aloe · many-leaved aloe · kroonaalwyn","Lesotho mountain aloe whose leaves form a symmetrical spiral; CITES Appendix I; "+AGM+".",W+"Aloe_polyphylla",dt="spiral direction · rosette size"),
  X("Aloe 'Lizard Lips'","Lizard Lips","Ornamental aloe cultivar; "+AGM+".",W+"Aloe"),
  ]},
 {"n":"Agave","a":"century plant · maguey","d":"Living rosette succulent of the genus Agave, from small collector species to large garden century plants.",
  "t":["species","variegated","dwarf"],"s":OLD,"x":[
  X("Agave americana","century plant · maguey · American aloe","Large monocarpic Mexican and US agave with grey-green spine-tipped leaves; "+AGM+".",W+"Agave_americana",
    v=[("'Marginata'","","","yellow leaf margins; "+AGM),("'Mediopicta'","","","cream central stripe; "+AGM),("'Mediopicta Alba'","","","white central band; "+AGM),("'Variegata'","","","white leaf edges; "+AGM),("'Mediopicta Aurea'","","","yellow central band"),("'Striata'","","","multiple yellow to white stripes")],dt="variegation · size"),
  X("Agave victoriae-reginae","Queen Victoria agave · royal agave","Small Chihuahuan Desert agave with compact rosettes edged in white markings; "+AGM+".",W+"Agave_victoriae-reginae",y="1875",
    v=[("f. ornata","","",""),("f. nickelsii","","",""),("f. stolonifera","","","")],dt="white marking · rosette size"),
  X("Agave titanota","chalk agave","Oaxacan monocarpic agave with broad whitish leaves and variable spines.",W+"Agave_titanota",
    v=[("'White Ice'","","",""),("'Filigree'","","",""),("'Solar Eclipse'","","","")],dt="leaf colour · spine form"),
  ]},
 {"n":"Houseleek","a":"Sempervivum · hens and chicks · liveforever","d":"Living hardy rosette succulent of the genus Sempervivum, forming mats that spread by offsets.",
  "t":["green","red","cobwebbed","bicolour"],"s":OLD,"x":[
  X("Sempervivum tectorum","common houseleek","The common houseleek; "+AGM+".",W+"Sempervivum"),
  X("Sempervivum arachnoideum","cobwebbed houseleek · cobweb houseleek","The cobwebbed houseleek; "+AGM+".",W+"Sempervivum",v=[("subsp. tomentosum","","",AGM)]),
  X("Sempervivum calcareum","limestone houseleek","The limestone houseleek, with several AGM cultivars.",W+"Sempervivum",v=[("'Extra'","","",AGM),("'Guillaume'","","",AGM)]),
  X("Colorockz","Sempervivum Colorockz®","Series of large-rosette, bicolour hardy houseleeks bred by Belgicactus, protected by plant breeders' rights.",'https://plantipp.eu/uk/varieties/sempervivum-colorockz-coconut-crystal-belsemmag1pbr',mk="Belgicactus",
    v=[("Coconut Crystal ('Belsemmag1')","Belgicactus","","lime green and red, fading to cream and wine-red; hardy to -20 °C"),("Blushing Garnet ('Belsemmag2')","Belgicactus","",""),("Coral Red ('Belsemred1')","Belgicactus","","")],dt="colourway · rosette size"),
  ],
  "m":[["'Bronco'",""],["'Lilac Time'",""],["'Othello'",""],["'Reinhard'",""]]},
 {"n":"Aeonium","a":"tree houseleek","d":"Living rosette succulent of the genus Aeonium, often with rosettes on branching stems.",
  "t":["green","purple-black","variegated"],"s":OLD,"x":[
  X("Aeonium arboreum","tree aeonium · tree houseleek","Canary Island subshrub up to 2 m with flat leaf rosettes and yellow spring flowers.",W+"Aeonium_arboreum",
    v=[("'Zwartkop'","","","purple-black leaves; also spelled 'Schwartzkopf'; "+AGM),("'Atropurpureum'","","","purple-leaved"),("'Variegatum'","","","variegated")],dt="leaf colour · stem height · branching"),
  ]},
 {"n":"Gasteria","a":"ox tongue · lawyer's tongue","d":"Living succulent of the genus Gasteria with thick tongue-shaped leaves, mostly from South Africa's Eastern Cape.",
  "t":["two-ranked","spiral","warty","variegated"],"s":OLD,"x":[
  X("Gasteria carinata","","Species with rough, keeled leaves; var. verrucosa stays heavily tubercled.",W+"Gasteria",v=[("var. verrucosa","","","proliferous, heavily tubercled")]),
  X("Gasteria bicolor","","Species with smooth, shiny erect leaves on a short sprawling stem.",W+"Gasteria"),
  X("Gasteria nitida var. armstrongii","Gasteria armstrongii","Divergent form keeping dark, recurved, rough leaves into adulthood.",W+"Gasteria"),
  X("Gasteria 'Little Warty'","Little Warty","Warty-leaved cultivar; "+AGM+".",W+"Gasteria"),
  X("Gasteria rawlinsonii","","Species with the cultivar 'Staircase'.",W+"Gasteria",v=[("'Staircase'","","","")]),
  X("× Gasteraloe","Gasteria × Aloe","Intergeneric hybrids of Gasteria and Aloe.",W+"Gasteria"),
  ]},
 {"n":"Graptopetalum","a":"ghost plant · mother-of-pearl plant","d":"Living rosette succulent of the genus Graptopetalum, related to Echeveria and Sedum.",
  "t":["species","intergeneric hybrid"],"s":OLD,"x":[
  X("Graptopetalum paraguayense","ghost plant · mother-of-pearl plant","Creeping Tamaulipas succulent with fleshy grey-green leaves and red-spotted white flowers.",W+"Graptopetalum_paraguayense",
    v=[("Graptosedum 'Ghosty'","","","hybrid often confused with its parent")],dt="leaf colour (grey, pink) · trailing length"),
  ]},
]
brands=[{"n":"Belgicactus","c":"Belgium","seg":"Specialist","kf":"succulent breeding","d":"Belgian breeder of the Colorockz series of hardy Sempervivum houseleeks.","lines":["Colorockz"],"sig":["Colorockz"],"s":"https://plantipp.eu/uk/varieties/sempervivum-colorockz-coconut-crystal-belsemmag1pbr"}]
w('C3','03_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"All eight planned kinds kept (old s kept). Archetypes sourced to Wikipedia species/genus pages, llifle (Perle von Nürnberg), Epic Gardening (Lola, Dick Wright 1980), Huntington ISI ('Milky Way'), Plantipp (Colorockz, Belgicactus). Perle von Nürnberg breeder left out (sources disagree: Graessner/Gräser). Japanese Haworthia cultivars (Yukiguni etc.) left out: llifle page failed to load and worldofsucculents blocked (403). Colorockz 'Lemon Flare' left out (snippet only). No traditions for this shelf."})
