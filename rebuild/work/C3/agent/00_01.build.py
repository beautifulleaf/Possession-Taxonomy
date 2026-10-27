import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,s,y='',v=(),dt='leaf size · variegation · plant size (corm, cutting, established)',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
kinds=[
 {"n":"Anthurium","a":"flamingo flower · laceleaf · velvet-leaf anthurium","d":"Living aroid of the genus Anthurium, grown either for velvety veined leaves or for glossy flowering spathes.",
  "t":["velvet-leaf collector","flowering (andraeanum hybrids)"],"s":"https://botachoku.com/foliage",
  "m":[["Anthurium luxurians",""]],"x":[
  X("Anthurium andraeanum","flamingo flower · tailflower · painter's palette · laceleaf","Ecuadorian and Colombian species whose many hybrids are grown as flowering pot plants and cut flowers.",W+"Anthurium_andraeanum",
    v=[("'Previa'","","","")],dt="spathe colour · spathe size · pot or cut"),
  X("Anthurium warocqueanum","queen anthurium","Colombian epiphyte with long velvety leaves from pale green to nearly black, up to about 1.2 m.",W+"Anthurium_warocqueanum",y="1878"),
  X("Anthurium veitchii","king anthurium","Colombian epiphyte with very large hanging leaves several feet long.",W+"Anthurium_veitchii",y="1876"),
  X("Anthurium crystallinum","","Velvety heart-shaped leaves with prominent white veins; from Colombia and Panama and widely hybridised.",W+"Anthurium_crystallinum"),
  X("Anthurium clarinervium","","Epiphyte endemic to Chiapas, Mexico, with deep green velvety heart-shaped leaves and ivory veins.",W+"Anthurium_clarinervium"),
  X("Anthurium regale","","Peruvian forest-floor species with large velvety heart-shaped leaves and white veins.",W+"Anthurium_regale"),
 ]},
 {"n":"Alocasia","a":"elephant ear · African mask plant · jewel alocasia","d":"Living cormous aroid of the genus Alocasia, grown for striking arrow-shaped leaves.",
  "t":["jewel (small velvet)","large-leaved"],"s":"https://toptropicals.com/catalog/uid/ALOCASIA_BLACKVELVET.htm","x":[
  X("Alocasia × amazonica","Alocasia × mortfontanensis · African mask plant · Amazonian elephant ear","Artificial hybrid of A. longiloba and A. sanderiana with dark, white-veined leaves; RHS Award of Garden Merit.",W+"Alocasia_%C3%97_amazonica",y="1891",
    v=[("Polly","","","")]),
  X("Alocasia zebrina","zebra plant · gabing tigre","Philippine species with glossy arrow-shaped leaves on tall petioles striped like a zebra.",W+"Alocasia_zebrina"),
  X("Alocasia micholitziana","green velvet taro","Luzon endemic with velvety, white-veined arrow-shaped leaves.",W+"Alocasia_micholitziana",
    v=[("'Frydek'","","","most popular cultivar")]),
  X("Alocasia reginula","black velvet","Small species from limestone cliffs in Sabah with dark velvety leaves; a natural species, not a cultivar.",W+"Alocasia_reginula",
    v=[("'Black Velvet'","","","trade name for the species")]),
  X("Alocasia baginda","","Kalimantan species uncommon in the trade, described in 2011.",W+"Alocasia_baginda",y="2011",
    v=[("'Dragonscale'","","",""),("'Silver Dragon'","","",""),("'Green Dragon'","","","")]),
  X("Alocasia cuprea","Alocasia metallica","Bornean species with coppery juvenile leaves and deep purple undersides.",W+"Alocasia_cuprea"),
 ]},
 {"n":"Peace lily","a":"Spathiphyllum · spath","d":"Living evergreen aroid of the genus Spathiphyllum with white spathes, grown as a houseplant.",
  "s":W+"Spathiphyllum","t":["compact","giant"],"x":[
  X("Spathiphyllum 'Mauna Loa'","","Peace lily cultivar holding the RHS Award of Garden Merit.",W+"Spathiphyllum",dt="plant height · spathe size"),
  X("Spathiphyllum × clevelandii","","Cultivated hybrid peace lily.",W+"Spathiphyllum",dt="plant height"),
 ]},
 {"n":"ZZ plant","a":"Zamioculcas zamiifolia · Zanzibar gem · eternity plant","d":"Living succulent aroid Zamioculcas zamiifolia from eastern Africa, with glossy pinnate leaves.",
  "s":W+"Zamioculcas","t":["green","black-leaved","variegated"],"x":[
  X("Zamioculcas zamiifolia","ZZ plant · Zanzibar gem · Zuzu plant · emerald palm","Evergreen succulent perennial from Kenya to South Africa, the standard ZZ plant.",W+"Zamioculcas",
    v=[("Raven ('Dowon')","Costa Farms","","licensed by Costa Farms"),("Zenzi ('HANSOTI13')","","",""),("Chameleon","","2020","US plant patent USPP32253"),("Super Nova","","","")],dt="leaf colour · plant height"),
 ]},
 {"n":"Chinese evergreen","a":"Aglaonema","d":"Living Chinese evergreen, genus Aglaonema (Araceae).","s":"https://mountaincrestgardens.com/",
  "t":["green and silver","red hybrid"],"x":[
  X("Aglaonema 'Silver Queen'","","The most common Chinese evergreen cultivar; RHS Award of Garden Merit.",W+"Aglaonema",dt="leaf pattern · plant height"),
  X("Aglaonema 'Siam Majesty'","","Thai red-veined hybrid from A. rotundum 'Giant' lines, patented in 2002.","https://patents.google.com/patent/USPP13141",mk="Ladda",y="2002",dt="leaf colour · plant height"),
 ]},
 {"n":"Dumb cane","a":"Dieffenbachia · leopard lily","d":"Living dumb cane, genus Dieffenbachia (Araceae).","s":"https://mountaincrestgardens.com/","t":["spotted","cream-centred"],"x":[
  X("Dieffenbachia seguine","dumb cane","Rainforest species from the New World tropics, the main houseplant dumb cane.",W+"Dieffenbachia",
    v=[("'Camille'","","","RHS Award of Garden Merit"),("'Tropic Snow'","","","RHS Award of Garden Merit")],dt="leaf pattern · plant height"),
 ]},
 {"n":"Caladium","a":"angel wings · heart of Jesus","d":"Living tuberous aroid of the genus Caladium grown for colourful heart- or lance-shaped leaves.",
  "s":W+"Caladium","t":["fancy-leaved","lance-leaved"],"x":[
  X("Caladium bicolor","angel wings · heart of Jesus","Tropical American species, source of over 1,000 named cultivars; bulbs mostly grown around Lake Placid, Florida.",W+"Caladium",dt="leaf shape (fancy, lance) · colour · tuber size"),
 ]},
 {"n":"Elephant ears","a":"Colocasia esculenta · taro","d":"Living taro (Colocasia esculenta) grown ornamentally for its huge leaves.","s":W+"Colocasia_esculenta","t":["green","black-leaved"],"x":[
  X("Colocasia esculenta","taro · dasheen · elephant ears","Tropical perennial aroid grown for its starchy corm and, as elephant ears, for ornament; RHS Award of Garden Merit.",W+"Colocasia_esculenta",
    v=[("'Black Magic'","","","dark, nearly black leaves")],dt="leaf colour · plant height · tuber size"),
 ]},
]
brands=[
 {"n":"Anthura","c":"Netherlands","f":"1938","seg":"Young-plant breeder (anthurium, bromeliad, orchid)","d":"Bleiswijk breeder of anthuriums, bromeliads and Phalaenopsis supplying young plants in over 70 countries.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://anthura.nl/en/who-we-are/"},
 {"n":"Ladda","c":"Thailand","f":"","seg":"Aglaonema breeder","d":"Thai breeder (Ladda Co., Ltd.) holding US plant patents for red Aglaonema hybrids such as 'Siam Majesty'.","lines":[],"eras":[],"sig":["Aglaonema 'Siam Majesty'"],"sc":[],"rel":[],"s":"https://patents.google.com/patent/USPP13141"},
 {"n":"Costa Farms","c":"United States","f":"1961","seg":"Houseplant grower","d":"Florida-based grower and marketer of houseplants.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"knowledge"},
]
notes=("Merged old per-species Anthurium and Alocasia kinds into genus kinds with species archetypes; added Peace lily, ZZ plant, Caladium, Elephant ears. "
 "A. luxurians kept in m (no retrievable page; Wikipedia 404). Further Colocasia cultivars (Mojito etc.) and Siam Aurora left out: not confirmed on a fetched page. "
 "Anthura has no named archetype here because no specific cultivar was confirmed beyond 'Previa' (breeder not stated). Wikidata rate-limited; Wikipedia, Anthura site and Google Patents used.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/C3/shelves/00_01.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
