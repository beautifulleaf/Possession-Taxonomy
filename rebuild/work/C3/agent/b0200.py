import json, os, sys
W='https://en.wikipedia.org/wiki/'; D='https://www.wikidata.org/wiki/'
QIDS=json.loads(sys.argv[1]) if len(sys.argv)>1 else {}
def X(n,d,s,a='',mk='',y='',v=None,dt=''):
    o={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: o["v"]=[dict(zip(("n","mk","y","d"),vv)) for vv in v]
    if dt: o["dt"]=dt
    return o
OS="https://orchids-shop.com/collections/popular-orchids?page=3"
PH=W+"Phalaenopsis"; PA=W+"Paphiopedilum"; CY=W+"Cymbidium"; CA=W+"Cattleya"; DE=W+"Dendrobium"
moth=[X("Phalaenopsis amabilis","Type species, described by Blume in 1825; holds the RHS Award of Garden Merit.",PH,y="1825"),
      X("Phalaenopsis Doris","Tetraploid hybrid grex that made moth orchids easy to grow at home.",PH,dt="flower size · colour · spike count")]
if 'Phalaenopsis schilleriana' in QIDS:
    moth.append(X("Phalaenopsis schilleriana","Philippine endemic with mottled leaves and large pink flowers, over 100 per spike on mature plants.",QIDS['Phalaenopsis schilleriana'],v=[("Phalaenopsis schilleriana × philippinensis","","","primary hybrid")]))
moth+= [X("Phalaenopsis aphrodite","Moth orchid species.",PH),
      X("Phalaenopsis philippinensis","Philippine species with white flowers.",PH),
      X("Phalaenopsis violacea","Fragrant species whose petals turn green after pollination.",PH),
      X("Phalaenopsis stuartiana","Species with mottled leaves, naturalised in Central and South America.",PH)]
if 'Phalaenopsis equestris' in QIDS:
    moth.append(X("Phalaenopsis equestris","Small-flowered, variable species from the Philippines and Taiwan, often used in breeding.",v=[("var. alba","","","white"),("var. aurea","","","yellow lip"),("var. rosea","","","red")],s=QIDS['Phalaenopsis equestris']))
moth.append(X("RHS award hybrids","Modern grexes holding the RHS Award of Garden Merit.",PH,v=[("Brother Pico Sweetheart","","","grex"),("Yellow Lightning","","","grex")]))
mothm=[] if 'Phalaenopsis schilleriana' in QIDS else [["Phalaenopsis schilleriana x philippinensis",""]]
slip=[X("Paphiopedilum insigne","Type species of the genus, from Assam and Meghalaya.",PA),
      X("Maudiae","Primary hybrid grex of P. callosum × P. lawrenceanum; the classic mottled-leaf paph.","https://www.sunsetvalleyorchids.com/htm/archive_paph1-2023.html",
        v=[("'Los Osos' AM/AOS","","","awarded clone")],dt="album, coloratum and vinicolor colour forms · mottled leaves"),
      X("Paphiopedilum rothschildianum","Multifloral species from north-west Borneo.",PA),
      X("Paphiopedilum sanderianum","Borneo species from Gunung Mulu.",PA),
      X("Paphiopedilum armeniacum","Golden slipper orchid, discovered 1979 and described 1982.",PA,a="golden slipper orchid",y="1982"),
      X("Paphiopedilum micranthum","Silver slipper orchid.",PA,a="silver slipper orchid · hard-leaved pocket orchid"),
      X("Paphiopedilum callosum","Mottled-leaf species from Indochina to Malaysia.",PA),
      X("Paphiopedilum fairrieanum","Himalayan species.",PA),
      X("Paphiopedilum hirsutissimum","Species from Assam to southern China.",PA),
      X("Paphiopedilum hangianum","Species from Yunnan to Vietnam.",PA),
      X("Paphiopedilum lowii","Species of western and central Malesia.",PA,v=[("var. semi alba","","","")]),
      X("Paphiopedilum venustum","Species from eastern Nepal to Bangladesh.",PA),
      X("Paphiopedilum thaianum","Species from Thailand.",PA),
      X("Paphiopedilum charlesworthii","Listed species.",PA),
      X("Paphiopedilum fowliei","Listed species.",PA),
      X("Pinocchio","Grex of P. primulinum × P. glaucophyllum.",PA)]
cym=[X("Cymbidium goeringii","East Asian Jensoa cymbidium, known as chun lan in China and shunran in Japan.",W+"Cymbidium_goeringii",a="noble orchid · chun lan · shunran"),
     X("Cymbidium ensifolium","Fragrant Jensoa species from Japan to Java.",CY,v=[("'Peach Charm'","","","cultivar")]),
     X("Cymbidium sinense","Jensoa species of southern China, Taiwan and Vietnam.",CY),
     X("Cymbidium kanran","Jensoa species of China, Japan and Korea.",CY),
     X("Cymbidium faberi","Jensoa species of China and Taiwan.",CY)]
if 'Cymbidium insigne' in QIDS:
    cym.append(X("Cymbidium insigne","Species central to breeding standard-sized hybrids.",QIDS['Cymbidium insigne']))
cym+=[X("Cymbidium eburneum","Cyperorchis species from the Himalaya to Vietnam, a parent of standard hybrids.",CY),
     X("Cymbidium lowianum","Cyperorchis species from Myanmar to Vietnam.",CY),
     X("Cymbidium tracyanum","Cyperorchis species from China, Thailand and Myanmar.",CY),
     X("Cymbidium devonianum","Pendent-flowered species from India to South-East Asia.",CY),
     X("Cymbidium floribundum","Small species from Yunnan, Taiwan and Vietnam.",CY)]
catt=[X("Cattleya labiata","Type species, found in Pernambuco, Brazil, in 1817 and flowered by William Cattley.",CA,y="1817"),
      X("Cattleya trianae","National flower of Colombia.",CA,v=[("var. coerulea 'Cielo Azul'","","","awarded clone")]),
      X("Cattleya mossiae","Cattleya species.",CA),
      X("Cattleya dowiana","Cattleya species.",CA),
      X("Cattleya lueddemanniana","Cattleya species.",CA),
      X("Cattleya maxima","Species.",CA,v=[("var. coerulea","","","")]),
      X("Cattleya walkeriana","Cattleya species.",CA),
      X("Cattleya warscewiczii","Cattleya species.",CA)]
kinds=[
 {"n":"Moth orchid","a":"Phalaenopsis · Phal","d":"Living moth orchid of the genus Phalaenopsis, the most common orchid.","t":["standard","miniature","multiflora"],"s":OS,"x":moth,**({"m":mothm} if mothm else {})},
 {"n":"Slipper orchid","a":"Paphiopedilum · Venus slipper · paph","d":"Living slipper orchid of the genus Paphiopedilum, with a pouch-shaped lip.","t":["mottled-leaf","plain-leaf","multifloral","Parvisepalum"],"s":OS,"x":slip,
  "m":[["Paphiopedilum Prince Edward of York",""]]},
 {"n":"Cymbidium","a":"boat orchid · lan","d":"Living orchid of the genus Cymbidium, from large standard hybrids to small fragrant Asian lan.","t":["standard hybrid","miniature hybrid","Chinese/Japanese lan (section Jensoa)"],"s":OS,"x":cym,
  "m":[["Cymbidium Cali Night 'Geyserland'",""],["Cymbidium Cliff Hutchings 'New Horizon'",""],["Cymbidium Sarah Jean 'Ice Cascade'",""]]},
 {"n":"Cattleya","a":"","d":"Living orchid of the genus Cattleya, with large showy flowers on pseudobulbs bearing one or two leaves.","t":["species","× Rhyncholaeliocattleya hybrid","× Brassolaeliocattleya hybrid"],"s":OS,"x":catt},
 {"n":"Dendrobium","a":"","d":"Living orchid of the large Asian and Australasian genus Dendrobium, with cane-like stems.","t":["nobile-type","Phalaenanthe section","Spatulata section"],"s":DE,
  "x":[X("Dendrobium moniliforme","Type species; Sekikoku in Japan, emblem of Matsushima.",DE,a="Sekikoku"),
       X("Dendrobium nobile","Noble dendrobium, widely bred for high flower count.",DE,a="noble dendrobium"),
       X("Dendrobium bigibbum","Cooktown orchid, emblem of Queensland.",DE,a="Cooktown orchid"),
       X("Dendrobium kingianum","Australian species.",DE),
       X("Dendrobium densiflorum","Species, a parent of the hybrid Chet's Choice.",DE,v=[("Chet's Choice","","","hybrid with D. farmeri")]),
       X("Berry","Grex holding the RHS Award of Garden Merit.",DE)]},
 {"n":"Oncidium alliance","a":"dancing-lady orchid · Oncidium · Odontoglossum · Brassia hybrids","d":"Living orchids of Oncidium and related genera, many with sprays of small yellow or patterned flowers.","t":["× Brassidium","× Odontioda","× Wilsonara"],"s":W+"Oncidium",
  "x":[X("Oncidium sphacelatum","Oncidium species.",W+"Oncidium"),
       X("Oncidium ornithorhynchum","Oncidium species.",W+"Oncidium")]},
 {"n":"Vanda","a":"","d":"Living orchid of the genus Vanda, an epiphyte usually grown bare-rooted in a basket.","t":["strap-leaved","terete-leaved","former × Ascocenda"],"s":W+"Vanda",
  "x":[X("Vanda coerulea","Blue orchid, notable for its rare blue flowers.",W+"Vanda",a="blue orchid"),
       X("Vanda sanderiana","Large-flowered species from Mindanao, Philippines.",W+"Vanda"),
       X("Vanda dearei","Chief source of yellow in Vanda hybrids.",W+"Vanda"),
       X("Miss Joaquim","Papilionanthe teres × hookeriana, credited to Agnes Joaquim in 1893; Singapore's national flower since 1981.",W+"Papilionanthe_Miss_Joaquim",a="Vanda Miss Joaquim · Singapore orchid",y="1893")]},
 {"n":"Pansy orchid","a":"Miltoniopsis","d":"Living orchid of the genus Miltoniopsis, with flat pansy-like flowers.","s":W+"Miltoniopsis",
  "x":[X("Miltoniopsis vexillaria","Type species, from Colombia and Ecuador.",W+"Miltoniopsis"),
       X("Miltoniopsis phalaenopsis","Colombian species.",W+"Miltoniopsis"),
       X("Miltoniopsis roezlii","Species from Panama to Peru.",W+"Miltoniopsis"),
       X("Miltoniopsis warscewiczii","Species from Costa Rica to Colombia.",W+"Miltoniopsis"),
       X("Miltoniopsis bismarckii","Species from Ecuador and Peru.",W+"Miltoniopsis")]},
 {"n":"Phragmipedium","a":"Phrag · South American slipper orchid","d":"Living slipper orchid of the American genus Phragmipedium.","s":W+"Phragmipedium",
  "x":[X("Phragmipedium besseae","Orange-red species found in Peru in 1981 and widely used in breeding.",W+"Phragmipedium",y="1981"),
       X("Phragmipedium kovachii","Large-flowered species from San Martín, Peru.",W+"Phragmipedium"),
       X("Phragmipedium caudatum","Type species with very long drooping petals.",W+"Phragmipedium"),
       X("Phragmipedium longifolium","Long-leaved species described in 1852.",W+"Phragmipedium",y="1852"),
       X("Phragmipedium schlimii","Colombian species.",W+"Phragmipedium"),
       X("Phragmipedium lindenii","Species from Venezuela to Ecuador.",W+"Phragmipedium")]},
 {"n":"Zygopetalum","a":"","d":"Living orchid of the genus Zygopetalum, with fragrant, waxy green and purple flowers.","s":W+"Zygopetalum",
  "x":[X("Zygopetalum maculatum","Type species, syn. Z. mackayi.",W+"Zygopetalum",a="Zygopetalum mackayi"),
       X("Zygopetalum maxillare","Species of Brazil, Paraguay and Argentina.",W+"Zygopetalum"),
       X("Zygopetalum crinitum","Brazilian species.",W+"Zygopetalum")]},
 {"n":"Jewel orchid","a":"Ludisia · Macodes · Anoectochilus · Goodyera","d":"Living terrestrial orchid grown mainly for velvety, veined leaves.","s":W+"Ludisia",
  "x":[X("Ludisia discolor","Jewel orchid with velvety maroon leaves and red veins.",W+"Ludisia",v=[("'Nigrescens'","","","black velvet"),("'Alba'","","","albino")])]+
      ([X("Macodes petola","South-East Asian jewel orchid with ornate veined leaves.",v=[("var. petola","","","yellow veins"),("var. argenteoreticulata","","","white netted veins")],s=QIDS['Macodes petola'])] if 'Macodes petola' in QIDS else [])},
 {"n":"Wind orchid","a":"Vanda falcata · Neofinetia falcata · fūran · fūkiran","d":"Small fragrant white East Asian orchid; its named Japanese cultivars are prized as fūkiran.","s":W+"Vanda_falcata",
  "x":[X("Vanda falcata","Wild species of China, Korea and Japan, described by Thunberg from Japan in 1784.",W+"Vanda_falcata",y="1784"),
       X("Fūkiran","Named Japanese cultivars selected since the Edo period for variegation, flower and growth form.",W+"Vanda_falcata",a="富貴蘭",y="Edo period",
         v=[("Asahiden 朝日殿","","",""),("Seikai 青海","","","")],dt="leaf variegation · flower colour and form · growth form")]}]
trads=[{"n":"Fūkiran","g":"Plants & gardens","r":"Japan","p":"Edo period (from the Kanbun era, 1661–1673)","d":"Japanese culture of named Vanda falcata cultivars, prized by daimyō and wealthy collectors.","tech":"selection and naming of mutant forms","mat":"Vanda falcata","forms":["Fūkiran"],"ctr":["Japan"],"auth":"named cultivars recognised by variegation, flower and growth traits","s":W+"Vanda_falcata"},
 {"n":"Chinese lan","g":"Plants & gardens","r":"China","p":"ancient, from Confucius's era","d":"Chinese cultivation of fragrant small cymbidiums as one of the Four Gentlemen, prized for scent and variegated foliage.","tech":"pot culture of selected Jensoa cymbidiums","mat":"Cymbidium section Jensoa","forms":["Cymbidium goeringii","Cymbidium ensifolium","Cymbidium sinense"],"ctr":["China"],"s":"https://www.gardensbythebay.com.sg/en/learn-with-us/explore-resources/whats-blooming/boat-orchids.html"}]
out={"kinds":kinds,"brands":[],"traditions":trads,"notes":"All four old kinds kept, eight new kinds added. Old grexes with no retrieved page (Prince Edward of York, Sarah Jean, Cali Night, Cliff Hutchings) stay in m. Maudiae year differs between sources (1900 vs 1908), so left out. Shunran/chōseiran Japanese pages blocked or 429; koten engei covered via fūkiran. No brands: no breeder named as archetype maker."}
p='work/C3/shelves/02_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
