import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='basket or pot size · planting depth',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
A=lambda n,d="",y="",mk="":(n,mk,y,d)
NY,NN,NL,NA,NC=W+"Nymphaea",W+"Nelumbo_nucifera",W+"Nelumbo_lutea",W+"Nymphaea_alba",W+"Nymphaea_caerulea"
DBG="https://www.botanicgardens.org/node/4895"; LMH="https://shop.latour-marliac.com/content/8-history"
BG="https://www.brookgreen.org/plant-collection/name/nelumbo-mrs-perry-d-slocum"
IP,PC,CP,CD,EC=W+"Iris_pseudacorus",W+"Pontederia_cordata",W+"Caltha_palustris",W+"Ceratophyllum_demersum",W+"Elodea_canadensis"
LM="Latour-Marliac"
kinds=[
 {"n":"Water lily","a":"Nymphaea · nenuphar","d":"Living hardy or tropical water lily of the genus Nymphaea sold to grow in a pond or tub.",
  "t":["hardy","tropical","day-blooming","night-blooming","miniature"],"s":"https://playitkoi.com/collections/hardy-water-lilies.oembed?page=3","x":[
  X("'Marliacea Chromatella'","Nymphaea × marliacea 'Chromatella'","Pale yellow hardy water lily from Latour-Marliac's nursery; "+AGM+".",DBG,y="1880",mk=LM,dt="basket size · planting depth"),
  X("Latour-Marliac hardy hybrids","Marliac water lilies","Coloured hardy water lilies raised at Le Temple-sur-Lot from 1875, shown at the 1889 Exposition Universelle and bought by Monet for Giverny.",DBG,y="1880s",mk=LM,
    v=[A("'Marliacea Carnea'","","1880",LM),A("'Sulfurea Grandiflora'","yellow","1888",LM),A("'Laydekeri Rosea'","pink","1892",LM),A("'Laydekeri Fulgens'","","1893",LM),A("'Gloriosa'","","1896",LM),A("'Atropurpurea'","dark red","1901",LM),A("'Escarboucle'","orange-red; "+AGM,"1909",LM),A("'Attraction'","","1910",LM),A("'Albatros'","","1910",LM),A("'Gonnère'","double white, scented; introduced after his death; "+AGM,"1914",LM)]),
  X("'James Brydon'","","Hardy water lily with cupped rose-red flowers; "+AGM+".",NY),
  X("Nymphaea alba","white water lily · European white water lily","European native water lily of still or slow water.",NA,v=[A("f. rosea","red form discovered at Fagertärn, Sweden","early 19th century")]),
  X("Other AGM hardy water lilies","","Hardy water lilies holding the "+AGM+".",NY,v=[A("'Gladstoniana'","double white"),A("'Pygmaea Helvola'","miniature fragrant yellow")]),
  X("Nymphaea caerulea","blue lotus · Egyptian lotus","Tropical day-blooming water lily of the Nile, sacred in ancient Egypt.",NC,v=[A("'Valentina's Pale Blue Eyes'","bred in Italy, registered 2018","2018")],dt="tuber · minimum water temperature"),
  ]},
 {"n":"Lotus","a":"Nelumbo · sacred lotus","d":"Living lotus of the genus Nelumbo sold as a tuber or potted plant to grow in water.",
  "t":["flower lotus","bowl lotus (miniature)","seed lotus","rhizome lotus","single","double","multi-petalled"],"s":"https://playitkoi.com/products/the-president","x":[
  X("Nelumbo nucifera","sacred lotus · Indian lotus · padma","Asian lotus; flower lotus cultivars are the shortest and most floriferous, the bowl lotus (wanlian) miniature.",NN,
    v=[A("Bowl lotus","wanlian; 5–8 cm flowers"),A("'Ohmi Myoren'","Japanese; 2,000–5,000 petals")],dt="tuber · bowl or pond size"),
  X("'Mrs Perry D. Slocum'","","Hybrid of Nelumbo lutea and 'Rosea Plena' crossed by Perry Slocum.",BG,y="1964"),
  X("Nelumbo lutea","American lotus · yellow lotus","North American lotus, crossed with N. nucifera to give many hybrids.",NL),
  X("'Osiris'","Nelumbium 'Osiris'","Lotus raised by Latour-Marliac.",LMH,y="c. 1890",mk=LM),
  ]},
 {"n":"Marginal pond plant","a":"bog plant · emergent plant","d":"Living plant grown in shallow water or wet soil at the edge of a pond.",
  "t":["shallow-water","bog","variegated"],"s":IP,"x":[
  X("Iris pseudacorus","yellow flag · water flag","Aquatic or marginal iris; invasive outside its native range.",IP,v=[A("'Variegata'","white-striped leaves; "+AGM),A("'Roy Davidson'",AGM),A("'Alba'","pale cream"),A("'Golden Fleece'","dark yellow")],dt="pot size"),
  X("Pontederia cordata","pickerelweed","American emergent plant of pond and lake margins; "+AGM+".",PC),
  X("Caltha palustris","marsh-marigold · kingcup","Northern-hemisphere marsh plant grown in ponds and wildlife gardens.",CP,v=[A("'Flore Pleno'","double; "+AGM),A("'Yellow Giant'","single")]),
  ]},
 {"n":"Oxygenating plant","a":"oxygenator · submerged pond plant","d":"Living submerged plant sold to grow under water in ponds and aquaria.",
  "t":["rooted","free-floating","bunched cuttings"],"s":CD,"x":[
  X("Ceratophyllum demersum","hornwort · coontail","Rootless, submerged free-floating plant for coldwater and tropical water.",CD,dt="bunch size"),
  X("Elodea canadensis","Canadian waterweed · pondweed","Fast-growing submerged plant sold from cuttings; invasive in Europe since 1836.",EC,dt="bunch size"),
  ]},
]
brands=[{"n":"Latour-Marliac","c":"France","f":"1875","seg":"Heritage manufactory","kf":"water lilies","d":"Water-lily nursery at Le Temple-sur-Lot founded by Joseph Bory Latour-Marliac, supplier of Monet's Giverny lilies; owned by Robert Charles Sheldon since 2007.","eras":["Joseph Bory Latour-Marliac, 1875–1911","Stapeley Water Gardens, from 1991","Robert Charles Sheldon, from 2007"],"sig":["'Marliacea Chromatella'","'Escarboucle'","'Attraction'"],"s":LMH}]
w('C3','05_04',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Two old kinds kept with old s; marginal and oxygenating kinds added from Wikipedia. Hybrid dates from Denver Botanic Gardens and the Latour-Marliac history page. Oxygenating role is not stated on the retrieved pages, so definitions say submerged only. No separate lotus tradition: retrieved pages lacked enough on Japanese/Chinese lotus-viewing; IWGS register not fetched."})
