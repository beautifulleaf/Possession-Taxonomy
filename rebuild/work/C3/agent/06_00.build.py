import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
A=lambda n,d="",y="",mk="":(n,mk,y,d)
OLD="https://www.starkbros.com/products/fruit-trees"
RT='rootstock · tree form (standard, half-standard, bush, cordon, fan, espalier) · pot or bare-root'
SB,RV,UM="Stark Bro's","Rivers Nursery","University of Minnesota"
kinds=[
 {"n":"Apple tree","a":"Malus domestica","d":"Living apple tree (Malus) grown for fruit.","t":["dessert","cooking","cider","dual-purpose","columnar","family tree (multi-cultivar)"],"s":OLD,"x":[
  X("Cox's Orange Pippin","Cox","English dessert apple raised by Richard Cox, a retired brewer, at Colnbrook, Buckinghamshire.",W+"Cox's_Orange_Pippin",y="1830",dt=RT,
    v=[A("Queen Cox","sport"),A("Crimson Cox","sport"),A("Cherry Cox","sport"),A("Cox La Vera","sport"),A("King Cox","sport")]),
  X("Bramley's Seedling","Bramley","English cooking apple grown from a pip planted by Mary Ann Brailsford in Southwell, Nottinghamshire; "+AGM+".",W+"Bramley_apple",y="1809",dt=RT,
    v=[A("Crimson Bramley","bud mutation")]),
  X("Granny Smith","","Green, tart apple from a chance seedling propagated by Maria Ann Smith at Eastwood, New South Wales.",W+"Granny_Smith",y="1868",dt=RT),
  X("Golden Delicious","Mullins' Yellow Seedling","Yellow dessert apple found by J. M. Mullins in Clay County, West Virginia, introduced by Stark Bro's in 1914.",W+"Golden_Delicious",y="1905",mk=SB,dt=RT,
    v=[A("Jonagold","Golden Delicious × Jonathan","1943"),A("Pink Lady","Cripps Pink; Golden Delicious offspring"),A("Gala","Golden Delicious offspring"),A("Elstar","Golden Delicious offspring")]),
  X("Honeycrisp","MN1711","Crisp dessert apple from the University of Minnesota, US Plant Patent 7197 (expired 2008).",W+"Honeycrisp",y="1991",mk=UM,dt=RT,
    v=[A("SweeTango","Honeycrisp offspring"),A("Cosmic Crisp","Honeycrisp offspring"),A("EverCrisp","Honeycrisp offspring")]),
  X("Braeburn","","Dessert apple found by O. Moran at Waiwhero near Motueka, New Zealand.",W+"Braeburn",y="1952",dt=RT,
    v=[A("Jazz","Scifresh; Braeburn offspring"),A("Kanzi","Nicoter; Braeburn offspring"),A("Envy","Scilate; Braeburn offspring")]),
  ],"m":[["Ben Davis",""],["Cortland",""],["Empire",""]]},
 {"n":"Pear tree","a":"Pyrus","d":"Living pear tree (Pyrus), European and Asian, grown for fruit.","t":["European pear","Asian pear (nashi)","perry pear"],"s":OLD,"x":[
  X("Conference","","English pear raised by Thomas Rivers at Sawbridgeworth; named after first prize at the 1885 National British Pear Conference.",W+"Conference_pear",y="1885",mk=RV,dt=RT),
  X("Doyenné du Comice","Comice","Large, melting French pear found at the Comice Horticole of Angers.",W+"Doyenné_du_Comice",y="c. 1849",dt=RT),
  X("Williams' Bon Chrétien","Williams · Bartlett","English pear from Aldermaston, spread by a nurseryman Williams; sold as Bartlett in the USA.",W+"Williams_pear",y="c. 1765–1770",dt=RT,
    v=[A("Max Red Bartlett","red sport"),A("Sensation Red Bartlett","red sport"),A("Rosired Bartlett","red sport")]),
  X("Nashi","Asian pear · Pyrus pyrifolia · sand pear","Round, crisp East Asian pear species grown in cultivar form.",W+"Pyrus_pyrifolia",dt=RT,
    v=[A("Nijisseiki","Japan","1898"),A("Chojuro","Japan"),A("Kosui","Japan","1959"),A("Hosui","Japan","1972"),A("Niitaka","Japan","1927"),A("Hwangkeum","Korea","1984")]),
  ]},
 {"n":"Plum tree","a":"gage · damson","d":"Living plum tree (Prunus domestica, P. salicina and allies) grown for fruit.","t":["European plum","Japanese plum","gage","damson","bullace"],"s":OLD,"x":[
  X("Victoria","Denyer's Victoria","English egg plum, self-fertile, named after Queen Victoria and introduced by the nurseryman Denyer.",W+"Victoria_plum",y="1844",dt=RT),
  X("Czar","","Early, self-fertile cooking plum bred by Rivers of Sawbridgeworth from Prince Engelbert × Early Prolific.",
    "https://www.orangepippin.com/varieties/plums/czar",y="1874",mk=RV,dt=RT),
  X("Santa Rosa","","Japanese plum bred by Luther Burbank at Santa Rosa, California.","https://www.starkbros.com/products/fruit-trees/plum-trees/santa-rosa-plum",y="1906",dt=RT),
  ]},
 {"n":"Cherry tree","a":"sweet or sour cherry","d":"Living sweet or sour cherry tree grown for fruit; ornamental cherries are Flowering cherry.","t":["sweet cherry","sour cherry","self-fertile","dwarf"],"s":OLD,"x":[
  X("Stella","","First self-fertile sweet cherry, Lambert × John Innes Seedling 2420, from the Summerland Research Station, British Columbia.",W+"Stella_cherry",y="1968",dt=RT,
    v=[A("Compact Stella","semi-dwarf irradiation mutant","1973")]),
  X("Bing","","Dark sweet cherry raised by Seth Lewelling and Sit Ah Bing at Milwaukie, Oregon.",W+"Bing_cherry",y="1875",dt=RT),
  X("Morello","sour cherry · Prunus cerasus","Dark-red sour cherry group, the main sour cherry of Central Europe.",W+"Prunus_cerasus",dt=RT,
    v=[A("Montmorency","Amarelle type; main US sour cherry"),A("North Star","dwarf")]),
  ]},
 {"n":"Peach tree","a":"nectarine","d":"Living peach tree (Prunus persica), nectarines included, grown for fruit.","t":["peach","nectarine","flat peach","freestone","clingstone","dwarf patio"],"s":OLD,"x":[
  X("Peregrine","","English peach still widely grown for its reliability outdoors.","https://realenglishfruit.co.uk/peregrine/",y="1906",dt=RT),
  X("Elberta","","Yellow freestone peach raised by Samuel H. Rumph at Marshallville, Georgia, from Chinese Cling seed; named for his wife.","https://peaches.caes.uga.edu/history.html",y="1875",dt=RT),
  ]},
 {"n":"Apricot tree","a":"Prunus armeniaca","d":"Living apricot tree (Prunus armeniaca) grown for fruit.","s":OLD,"x":[
  X("US apricot cultivars","","Apricot cultivars popular in the United States.",W+"Apricot",dt=RT,
    v=[A("Blenheim"),A("Wenatchee Moorpark"),A("Tilton"),A("Perfection"),A("Moongold","needs a pollinator"),A("Sungold","needs a pollinator")]),
  ]},
 {"n":"Fig tree","a":"Ficus carica","d":"Living fig tree (Ficus carica) grown for fruit.","t":["common (self-fruiting)","Smyrna","San Pedro"],"s":OLD,"x":[
  X("Brown Turkey","","Self-fruiting common fig; "+AGM+".",W+"Common_fig",dt="pot or wall-trained · crop (breba, main)"),
  X("Chicago Hardy","","One of the most cold-hardy figs, with brown medium fruit; zones 5–10.","https://www.phoenixperennials.com/?p=9170",dt="pot or open ground"),
  X("Other common figs","","Self-fruiting common-type cultivars.",W+"Common_fig",
    v=[A("Celeste"),A("Brunswick"),A("Dottato","Kadota"),A("Black Mission")]),
  ]},
 {"n":"Quince tree","a":"Cydonia oblonga","d":"Living quince tree (Cydonia oblonga) grown for its aromatic fruit.","s":W+"Quince","x":[
  X("Vranja","Bereczki","Quince cultivar holding the "+AGM+".",W+"Quince",dt=RT),
  X("Serbian Gold","","Quince cultivar holding the "+AGM+".",W+"Quince",dt=RT),
  X("Meech's Prolific","Meeches Prolific","Old quince cultivar, illustrated in 1909.",W+"Quince",dt=RT,v=[A("Champion"),A("Portugal","Lusitanica"),A("Smyrna")]),
  ]},
 {"n":"Mulberry tree","a":"Morus · black mulberry","d":"Living mulberry tree (Morus) grown for fruit.","s":W+"Morus_nigra","x":[
  X("Chelsea","King James","Black mulberry cultivar, female and self-fertile; "+AGM+".",W+"Morus_nigra",dt="tree form · pot or open ground"),
  X("Jerusalem","","Black mulberry cultivar, female and self-fertile; "+AGM+".",W+"Morus_nigra"),
  ]},
 {"n":"Olive tree","a":"Olea europaea","d":"Living olive tree (Olea europaea) grown for fruit, also kept as an ornamental.","t":["oil cultivar","table cultivar","dual-purpose","standard","multi-stem"],"s":OLD,"x":[
  X("Arbequina","","Spanish oil and table olive from Arbeca.",W+"List_of_olive_cultivars",dt="pot size · trunk girth"),
  X("Picual","","Southern Spanish oil olive from Jaén.",W+"List_of_olive_cultivars"),
  X("Manzanilla","","Spanish table olive from Dos Hermanas, Seville.",W+"List_of_olive_cultivars"),
  X("Kalamata","","Greek table olive.",W+"List_of_olive_cultivars"),
  X("Koroneiki","","Greek oil olive of the southern Peloponnese.",W+"List_of_olive_cultivars"),
  X("Frantoio","","Tuscan oil olive.",W+"List_of_olive_cultivars",v=[A("Leccino","Tuscan oil olive")]),
  ]},
 {"n":"Pomegranate tree","a":"Punica granatum","d":"Living pomegranate tree or bush (Punica granatum) grown for fruit.","s":OLD,"x":[
  X("Nana","dwarf pomegranate · var. nana","Dwarf pomegranate for containers and bonsai; "+AGM+".",W+"Pomegranate"),
  ]},
 {"n":"Persimmon tree","a":"kaki · sharon fruit","d":"Living persimmon tree (Diospyros kaki, D. virginiana) grown for fruit.","t":["astringent (PCA)","non-astringent (PCNA)"],"s":OLD,"x":[
  X("Fuyu","","Non-astringent Japanese persimmon eaten firm like an apple.",W+"Diospyros_kaki"),
  X("Hachiya","","Widely grown Japanese astringent persimmon eaten soft.",W+"Diospyros_kaki"),
  X("Triumph","Sharon","Astringent persimmon grown in Israel's Plain of Sharon and sold as Sharon fruit.",W+"Diospyros_kaki"),
  X("Rojo Brillante","Spanish Persimon","Spain's main astringent persimmon, from Valencia.",W+"Diospyros_kaki"),
  ]},
 {"n":"Banana plant","a":"Musa","d":"Living banana plant (Musa) grown for fruit, dwarf indoor ones included.","t":["hardy ornamental","dwarf fruiting","indoor"],"s":OLD,"x":[
  X("Musa basjoo","Japanese banana · hardy banana","Hardy banana from Sichuan, root-hardy to about −12 °C if mulched; "+AGM+".",W+"Musa_basjoo",dt="pot size · stem height"),
  X("Dwarf Cavendish","Cavendish","Cavendish banana first grown by Joseph Paxton at Chatsworth for the Duke of Devonshire.",W+"Cavendish_banana",y="c. 1834",dt="pot size · stem height",
    v=[A("Dwarf Cavendish","","1888"),A("Grand Nain","Grande Naine; Chiquita banana")]),
  ]},
]
brands=[
 {"n":SB,"c":"United States","f":"1816","seg":"Specialist","kf":"fruit trees","d":"Missouri fruit-tree nursery that introduced Golden Delicious and Red Delicious.","sig":["Golden Delicious"],"s":"knowledge"},
 {"n":RV,"c":"United Kingdom","seg":"Heritage manufactory","kf":"fruit breeding","d":"Rivers nursery of Sawbridgeworth, Hertfordshire, raiser of Conference pear and Czar plum.","eras":["Thomas Rivers, 19th century"],"sig":["Conference","Czar"],"s":"https://www.orangepippin.com/varieties/plums/czar"},
 {"n":UM,"c":"United States","f":"1851","seg":"Institution & issuer","kf":"cold-hardy apples","d":"Public university whose fruit-breeding programme released Honeycrisp.","sig":["Honeycrisp"],"s":W+"Honeycrisp"},
]
w('C3','06_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"All 11 old kinds kept with old s; Quince tree and Mulberry tree added (brief) from Wikipedia. Old apple models Cox, Braeburn, Golden Delicious, Granny Smith, Honeycrisp, Pink Lady became archetypes/versions; Ben Davis, Cortland, Empire stay in m. Fig Celeste kept as a version. Peregrine raiser not stated on the retrieved page (GRIN record returned 502), so no mk. Apricot, pomegranate cultivars thin: Wikipedia names few. Luther Burbank, Summerland Research Station named in definitions, not as register brands."})
