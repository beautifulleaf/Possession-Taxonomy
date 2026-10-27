import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,s,mk='',y='',v=(),dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
AGM="RHS Award of Garden Merit"; BT=["loose bulbs","pre-packed","bulk sack","prepared for forcing","top size"]
TU,NA,GA,HY,DA=W+"Tulip",W+"Narcissus_(plant)",W+"Galanthus",W+"Hyacinthus_orientalis",W+"Dahlia"
kinds=[
 {"n":"Tulip bulb","a":"Tulipa bulb","d":"Dormant tulip bulb sold for autumn planting in beds or pots.","t":BT,"s":"https://www.rareseeds.com/store/plants-seeds",
  "m":[["Tulip 'Black Hero'",""]],"x":[
  X("Single Late group","Division 5 · includes old Darwin tulips","Cup- or goblet-shaped late tulips 45–75 cm tall.",TU,v=[("'Queen of the Night'","","","near-black glossy maroon-purple; a parent of the first truly black tulip")],dt="colour · height · flowering time"),
  X("Darwin Hybrid group","Division 4","Ovoid-flowered mid-to-late tulips 50–70 cm tall, distinct from the older Darwin tulips.",TU,dt="colour · height"),
  X("Triumph group","Division 3","Cup-shaped mid-to-late tulips 35–60 cm tall.",TU),
  X("Lily-flowered group","Division 6","Tulips with a narrow waist and pointed, reflexed petals; a separate group since 1958.",TU,y="1958"),
  X("Parrot, Fringed and Viridiflora groups","Divisions 7, 8, 10","Tulips with fringed, feathered or green-streaked petals.",TU),
  X("Single and Double Early groups","Divisions 1, 2","Early tulips, cup-shaped or fully double.",TU),
  X("Double Late group","Division 11 · peony-flowered","Late tulips with large, heavy double blooms 46–56 cm tall.",TU),
  X("Kaufmanniana, Fosteriana and Greigii groups","Divisions 12–14 · Emperor tulips","Early-flowering groups derived from these species; Greigii has brown-mottled leaves.",TU),
  X("Species tulips","Division 15 · botanical tulips","Wild tulip species, less showy but more reliably perennial.",TU),
  X("Rembrandt tulips","Division 9 · broken tulips","Feathered virus-broken tulips of the tulip-mania era, such as 'Semper Augustus'.",TU,y="17th century",v=[("'Semper Augustus'","","17th century","most expensive tulip of the mania, reportedly 10,000 guilders")]),
 ]},
 {"n":"Daffodil bulb","a":"Narcissus bulb","d":"Dormant Narcissus bulb sold for planting; the RHS division (flower type) is a further detail.","t":BT+["miniature"],"s":"https://www.rareseeds.com/store/plants-seeds","x":[
  X("'Tête-à-Tête'","","Yellow miniature cyclamineus daffodil (Division 6), the most widely grown cultivar in the Netherlands by area.",NA,dt="Division 6 · 663 ha in 2009/10"),
  X("'Carlton'","","Yellow large-cupped daffodil (Division 2), among the most numerous individual plants with over 9 billion bulbs.",NA,y="1927"),
  X("'King Alfred'","","Tetraploid yellow trumpet daffodil that helped establish the trumpet-led trade.",NA,y="1899",v=[("'Dutch Master'","","","yellow trumpet, Division 1"),("'Golden Harvest'","","1927","yellow trumpet, Division 1")]),
  X("'Ice Follies'","","White large-cupped daffodil (Division 2).",NA,y="1953"),
  X("'Jetfire'","","Yellow-and-orange cyclamineus daffodil (Division 6).",NA),
  X("'Thalia'","","White triandrus daffodil, coded 5 W-W.",NA),
 ]},
 {"n":"Snowdrop","a":"Galanthus bulb","d":"Galanthus bulb sold dry or 'in the green' for planting, including named cultivars traded by collectors.",
  "t":["dry bulb","in the green","single","double","yellow-marked"],"s":GA,"x":[
  X("Galanthus nivalis","common snowdrop","Type species of the genus, 7–15 cm tall, flowering January to April.",GA,y="1753",v=[("'Flore Pleno'","","","double form, extremely common")]),
  X("Galanthus elwesii","giant snowdrop","Large-flowered snowdrop about 23 cm tall, named after Henry John Elwes.",GA),
  X("Galanthus plicatus","Crimean snowdrop","Snowdrop about 30 cm tall with leaves folded back at the edges.",GA,v=[("'Wendy's Gold'","","","yellow markings and ovary")]),
  X("Collectors' AGM cultivars","galanthophile snowdrops","Named cultivars traded among galanthophiles; over 500 are described.",GA,v=[("'S. Arnott'","","",AGM),("'Atkinsii'","","",AGM),("'Magnet'","","",AGM)]),
 ]},
 {"n":"Hyacinth bulb","a":"Hyacinthus orientalis bulb","d":"Dormant Hyacinthus bulb sold for planting or forcing.","t":BT+["prepared (forcing)","for hyacinth glass"],"s":"https://www.rareseeds.com/store/plants-seeds","x":[
  X("'Delft Blue'","","Blue garden hyacinth; "+AGM+".",HY),
  X("'Jan Bos'","","Deep pink hyacinth; "+AGM+".",HY),
  X("'Gipsy Queen'","","Salmon-pink hyacinth; "+AGM+".",HY),
 ]},
 {"n":"Crocus corm","a":"","d":"Dormant Crocus corm sold for planting.","t":BT+["spring-flowering","autumn-flowering","large-flowered Dutch"],"s":"https://www.rareseeds.com/store/plants-seeds","x":[
  X("Crocus tommasinianus","tommies · woodland crocus · early crocus","Early, freely naturalising Balkan crocus; the species holds the "+AGM+".",W+"Crocus_tommasinianus",
    v=[("'Barr's Purple'","","","amethyst violet"),("'Ruby Giant'","","","purple"),("'Whitewell Purple'","","","silvery reddish-purple"),("'Roseus'","","","pink"),("'Lilac Beauty'","","","purple")]),
 ]},
 {"n":"Lily bulb","a":"Lilium bulb","d":"Dormant Lilium bulb sold for planting in borders or pots.","t":BT+["Oriental","Asiatic","trumpet","species"],"s":W+"Lilium_regale","x":[
  X("Lilium regale","regal lily","Scented trumpet lily from western Sichuan introduced to England by E. H. Wilson; "+AGM+".",W+"Lilium_regale",y="1903"),
  X("'Stargazer'","Lilium 'Stargazer'","Fragrant upward-facing Oriental hybrid lily bred by Leslie Woodriff in California.",W+"Lilium_'Stargazer'",y="1974",dt="up to 36 in · 4–5 flowers per stem"),
 ]},
 {"n":"Allium bulb","a":"ornamental onion bulb","d":"Dormant bulb of an ornamental Allium sold for its globe flower heads.","t":BT,"s":W+"Allium_hollandicum","x":[
  X("'Purple Sensation'","Allium hollandicum 'Purple Sensation' · Persian onion · Dutch garlic","Purple globe-headed ornamental onion up to about 90 cm; "+AGM+".",W+"Allium_hollandicum"),
 ]},
 {"n":"Amaryllis bulb","a":"Hippeastrum bulb · amaryllis","d":"Large Hippeastrum bulb sold to flower indoors in winter, often waxed or boxed.",
  "t":["single","double","miniature","trumpet","jumbo","waxed","boxed kit"],"s":W+"Hippeastrum","x":[
  X("Hippeastrum hybrids","florists' amaryllis","Large-flowered hybrids bred mainly in the Netherlands and South Africa.",W+"Hippeastrum",
    v=[("Reginae strain","","","Dutch-bred"),("Leopoldii hybrids","","","Veitch nursery, England"),("'Apple Blossom'","","",""),("'Lemon Sorbet'","","",""),("'Pink Diamond'","","",""),("'Clown'","","","")]),
 ]},
 {"n":"Dahlia tuber","a":"","d":"Dormant Dahlia tuber sold for planting; a potted dahlia already in growth is among the garden plants.",
  "t":["single","anemone","collerette","waterlily","decorative","ball","pompon","cactus","semi-cactus","fimbriated","orchid","peony"],"s":"https://www.crocus.co.uk/plants/_/","x":[
  X("'Bishop of Llandaff'","","Scarlet peony-flowered dahlia with near-black foliage, raised by Cardiff nurseryman Fred Treseder; AGM 1928.",W+"Dahlia_'Bishop_of_Llandaff'",y="1924",v=[("'Bishops Children'","","","seed strain with dark foliage, varied flowers")]),
  X("'Café au Lait'","'Cafe au lait'","Decorative-group dahlia.",DA),
  X("RHS group examples","","Reference cultivars for RHS dahlia groups (International Register of Dahlia Names since 1969).",DA,
    v=[("'Twyning's After Eight'","","","Single"),("'Apple Blossom'","","","Collerette"),("'Cameo'","","","Waterlily"),("'Karma Sangria'","","","Cactus"),("'Small World'","","","Pompon"),("'Pink Giraffe'","","","Double Orchid")]),
 ]},
 {"n":"Seed potato","a":"","d":"Potato tuber sold for planting, not for eating.","t":["first early","second early","maincrop","salad","certified","chitted"],"s":"https://www.ufseeds.com/collections/seed-potatoes",
  "m":[["Red Pontiac",""]],"x":[
  X("'Maris Piper'","","All-rounder maincrop bred by H. W. Howard at the Plant Breeding Institute; the most widely grown UK potato since 1980.",W+"Maris_Piper",y="1966",dt="floury · cyst-nematode resistant"),
  X("'Yukon Gold'","","Yellow-fleshed potato bred by Gary Johnston at Guelph, Canada.",W+"Yukon_Gold_potato",y="1980"),
  X("'Charlotte'","","Waxy second-early salad potato bred in north-west France from Hansa × Danae; AGM 1998.","https://www.justgardencentres.com/aagcal/vegetable/potato/second-early-charlotte.php",y="1981"),
 ]},
 {"n":"Seed garlic","a":"garlic bulb","d":"Garlic bulb or clove sold for planting, not for eating.","t":["autumn-planted","spring-planted"],"s":"https://www.starkbros.com/products/fruit-trees","x":[
  X("Hardneck garlic","Allium sativum var. ophioscorodon","Garlic for cooler climates with relatively large cloves.",W+"Garlic",v=[("Porcelain","","",""),("Rocambole","","",""),("Purple stripe","","","")]),
  X("Softneck garlic","Allium sativum var. sativum","Garlic for milder climates with small, tightly packed cloves.",W+"Garlic",v=[("Artichoke","","",""),("Silverskin","","",""),("Creole","","","")]),
 ]},
 {"n":"Onion set","a":"onion sets · starter bulbs","d":"Small part-grown onion bulb sold to plant for a full-sized onion.","t":["brown","red","heat-treated","autumn-planted","spring-planted","shallot set"],"s":W+"Onion"},
]
trads=[{"n":"Dutch bulb growing","g":"Plants & gardens","r":"Duin- en Bollenstreek, western Netherlands (Lisse, Hillegom)","p":"late 16th century to present",
 "d":"Commercial flower-bulb cultivation on the cleared coastal dunes between Haarlem and Leiden, shaped by the 17th-century tulip mania.",
 "tech":"field cultivation and lifting of bulbs on sandy dune soil; trade through flower auctions","mat":"tulip, hyacinth, daffodil and other bulbs",
 "forms":["Tulip bulb","Hyacinth bulb","Daffodil bulb"],"ctr":["Lisse","Hillegom","Keukenhof","Rijnsburg auction","Aalsmeer auction"],"auth":"","s":W+"Bollenstreek"}]
w('C3','07_01',{"kinds":kinds,"brands":[],"traditions":trads,"notes":"All seven old kinds kept with old sources; Snowdrop, Lily, Allium, Amaryllis and Onion set added from Wikipedia. Tulips organised by the divisions on the Wikipedia Tulip page; 'Black Hero' and 'Red Pontiac' kept as flat models from old data (no retrieved page). Not included for lack of a retrieved page: 'February Gold', 'Café au Lait' breeder, onion-set cultivars, KAVB register page. No brand entries: archetype originators are individual breeders, recorded in descriptions."})
