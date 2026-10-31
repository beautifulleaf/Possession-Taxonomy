import sys; sys.path.insert(0,'work/C3/agent'); from w import w
def X(n,a,d,s,y='',v=(),dt='',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if dt: x["dt"]=dt
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
WP="https://en.wikipedia.org/wiki/"
NS="https://northspore.com/collections/oyster/products/specialty-strains"
COR="https://smallfarms.cornell.edu/projects/mushrooms/methods-of-commercial-mushroom-cultivation-in-the-northeastern-united-states/3-inoculating-logs"
FD="https://www.farmanddairy.com/?p=229392"; GC="https://shop.grocycle.com/products/grocycle-mushroom-kit"
FF="https://insightonbusiness.com/an-art-and-a-science/"; AM="https://www.farminguk.com/agricultural-directory/ann-miller-s-mushrooms-ltd-_57433.html"
T=["grain spawn","sawdust spawn","plug spawn","liquid culture","agar plate or slant"]
DT="carrier · quantity · certified organic or not"
kinds=[
 {"n":"Oyster mushroom spawn","a":"Pleurotus spawn","d":"Living oyster-mushroom mycelium on a carrier, sold to inoculate straw, logs, sawdust or coffee grounds.","t":T,
  "s":"https://northspore.com/pages/spawn-faq","x":[
  X("Grey oyster","Pleurotus ostreatus · pearl oyster · hiratake","Temperate oyster mushroom, first cultivated commercially in Germany during World War I.",WP+"Pleurotus_ostreatus",dt=DT,
    v=[("King Blue Oyster","North Spore","","blue-capped, thick-stemmed cross of blue and king oysters, from Mossy Creek"),("Popham Elm Oyster","North Spore","","branched off-white to tan clusters; fruits in cold and warm temperatures")]),
  X("Pink oyster","Pleurotus djamor","Tropical oyster mushroom with pink fruit bodies, grown at 25–30 °C on straw or sawdust.",WP+"Pleurotus_djamor",dt=DT),
  X("King oyster","Pleurotus eryngii · king trumpet · eryngi","Thick-stemmed oyster mushroom with a long shelf life, widely cultivated on organic wastes.",WP+"Pleurotus_eryngii",dt=DT),
 ]},
 {"n":"Shiitake spawn","a":"Lentinula edodes spawn","d":"Living shiitake mycelium on sawdust or wooden plugs, sold mainly to inoculate hardwood logs.","t":T+["thimble spawn"],
  "s":WP+"Shiitake","x":[
  X("Wide-range shiitake strains","WR strains","Reliable strains with fast spawn run that force-fruit easily; the usual first choice.",COR,dt=DT),
  X("Warm-weather shiitake strains","WW strains","Strains that fruit best in hot summers and early autumn and tolerate warm soak water.",COR,dt=DT,
    v=[("WW70","Field & Forest Products","","warm/cool strain fruiting at 50–80 °F in late summer and early autumn")]),
  X("Cold-weather shiitake strains","CW strains","Strains with a longer spawn run that fruit in early spring and late autumn on natural temperature swings.",COR,dt=DT,
    v=[("Snowcap","Field & Forest Products","","fruits from early April through cold snaps"),("Cold weather juniper","Field & Forest Products","","fruits at 35–55 °F in early spring")]),
 ]},
 {"n":"Lion's mane spawn","a":"Hericium erinaceus · yamabushitake · bearded tooth","d":"Living lion's mane mycelium sold to inoculate supplemented sawdust or logs.","t":T,"s":WP+"Hericium_erinaceus"},
 {"n":"Wine cap spawn","a":"Stropharia rugosoannulata · king stropharia · garden giant","d":"Living wine cap mycelium sold to inoculate wood-chip beds in the garden.","t":["sawdust spawn","grain spawn"],"s":WP+"Stropharia_rugosoannulata"},
 {"n":"Button mushroom spawn","a":"Agaricus bisporus · champignon de Paris","d":"Living Agaricus bisporus mycelium on grain, sold to inoculate composted manure.","t":["grain spawn","white","brown (chestnut, cremini)"],
  "s":WP+"Agaricus_bisporus","x":[
  X("White button","common mushroom · champignon de Paris","White strain descended from a mutant found at Louis Lambert's Keystone Mushroom Farm, Coatesville, Pennsylvania.",WP+"Agaricus_bisporus",y="1925",dt=DT),
  X("Brown (chestnut)","cremini · Swiss brown · portobello when mature","Brown form; picked immature as chestnut or cremini, mature as portobello.",WP+"Agaricus_bisporus",dt=DT),
 ]},
 {"n":"Reishi spawn","a":"lingzhi · Ganoderma lingzhi · Ganoderma sichuanense","d":"Living reishi mycelium sold to inoculate hardwood logs, sawdust or wood chips.","t":T+["antler form"],"s":WP+"Lingzhi_(mushroom)"},
 {"n":"Mushroom grow kit","a":"","d":"Inoculated log, block or bag of substrate sold to fruit mushrooms at home; species and substrate vary.","t":["bag or block kit","log kit","garden bed kit","spray-and-grow"],
  "s":"https://northspore.com/pages/spawn-faq",
  "m":[["Pink Oyster 'Spray & Grow' Mushroom Growing Kit","North Spore"],["Pink Oyster 'Plant & Grow' Mushroom Starter Block","North Spore"],["Wine Cap Garden Bed Kit","North Spore"],["GroCycle Oyster Mushroom Grow Kit","GroCycle"]]},
]
brands=[
 {"n":"North Spore","c":"United States","seg":"Specialist","kf":"mushroom spawn","d":"US supplier of organic grain, sawdust and plug spawn, cultures and grow kits.","sig":["Pink Oyster 'Spray & Grow' kit"],"s":NS},
 {"n":"Field & Forest Products","c":"United States","f":"1983","seg":"Specialist","kf":"shiitake spawn","d":"Peshtigo, Wisconsin spawn lab and farm founded by Joe Krawczyk and Mary Ellen Kozak, selling spawn for about a dozen species.","sig":["WW70","Snowcap"],"s":FF},
 {"n":"Ann Miller's Mushrooms","c":"United Kingdom","seg":"Specialist","kf":"mushroom spawn","d":"Spawn maker at Insch, Aberdeenshire, producing a large range of spawn for amateur and professional growers.","s":AM},
 {"n":"GroCycle","c":"United Kingdom","seg":"Artisan & independent","kf":"oyster grow kits","d":"UK maker of oyster mushroom grow kits on sawdust and bran.","sig":["GroCycle Oyster Mushroom Grow Kit"],"s":GC},
]
w('C3','10_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Old carrier kinds (grain, sawdust, plug, liquid culture) and 'Other mushroom spawn' dissolved into t types on every spawn kind. Blue oyster as a separate archetype not added: no retrieved page; North Spore's King Blue Oyster recorded as a version. Lion's mane, wine cap and reishi have no sourced named strains, so kept at kind level. Ann Miller's site not fetched; established from FarmingUK directory. Species identities also logged from Wikidata entities."})
