import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
A=lambda n,d="",y="",mk="":(n,mk,y,d)
OLD="https://www.starkbros.com/products/fruit-trees"
LS=W+"List_of_strawberry_cultivars"
PL='bare-root, pot or runner · cold-stored'
BU='bare-root or pot · bush, cordon or standard'
JH="James Hutton Institute"
kinds=[
 {"n":"Strawberry plant","a":"Fragaria","d":"Living strawberry plant grown for fruit.","t":["summer-fruiting (short-day)","perpetual (day-neutral)","alpine"],"s":OLD,"x":[
  X("Cambridge Favourite","","Early English strawberry from the University of Cambridge, F. chiloensis × Blakemore; "+AGM+".",LS,y="1947",dt=PL),
  X("Elsanta","","Midseason strawberry from the Dutch Institute for Horticultural Plant Breeding, Gorella × Holiday.",LS,y="1975",dt=PL),
  X("Royal Sovereign","","Heritage English strawberry raised by Thomas Laxton.",LS,y="1891",dt=PL),
  X("Honeoye","","Early midseason strawberry from Cornell/NYSAES; "+AGM+".",LS,y="1979",dt=PL),
  X("Symphony","","Late Scottish strawberry, Rhapsody × Holiday; "+AGM+".",LS,y="1993",mk=JH,dt=PL),
  X("Albion","","Day-neutral strawberry from the University of California.",LS,y="2006",dt=PL),
  X("Alpine strawberry","woodland strawberry · Fragaria vesca","Small-fruited perpetual strawberry, mostly raised from seed.",W+"Fragaria_vesca",dt="seed or plug",
    v=[A("Baron Solemacher","seed-raised; F. C. Heinemann, Germany","1935")]),
  ]},
 {"n":"Raspberry plant","a":"Rubus idaeus · raspberry cane","d":"Living raspberry cane (Rubus idaeus) grown for fruit.","t":["summer-fruiting (floricane)","autumn-fruiting (primocane)","yellow"],"s":OLD,"x":[
  X("Glen Ample","","Mid-summer raspberry; "+AGM+".",W+"Raspberry",dt="bare-root canes or pot"),
  X("Autumn Bliss","","Autumn-fruiting primocane raspberry; "+AGM+".",W+"Raspberry",dt="bare-root canes or pot"),
  X("Tulameen","","Late-summer raspberry; "+AGM+".",W+"Raspberry"),
  X("Malling raspberries","","Malling-series summer raspberries holding the "+AGM+".",W+"Raspberry",v=[A("Malling Jewel","early summer"),A("Malling Admiral","late summer")]),
  ]},
 {"n":"Blueberry bush","a":"highbush blueberry · Vaccinium","d":"Living blueberry bush grown for fruit.","t":["northern highbush","southern highbush","rabbiteye","lowbush","dwarf patio"],"s":OLD,"x":[
  X("Bluecrop","","Mid-season northern highbush blueberry.",W+"Vaccinium_corymbosum",dt="pot size · age"),
  X("Duke","","Early northern highbush blueberry; "+AGM+".",W+"Vaccinium_corymbosum",dt="pot size · age",v=[A("Spartan","early; "+AGM),A("Patriot","early")]),
  X("Late highbush blueberries","","Late-season northern highbush cultivars.",W+"Vaccinium_corymbosum",v=[A("Chandler"),A("Elliott"),A("Jersey"),A("Darrow"),A("Aurora")]),
  ]},
 {"n":"Blackberry plant","a":"bramble · Rubus · hybrid berry","d":"Living blackberry plant (Rubus), thornless types and hybrid berries included, grown for fruit.","t":["thornless","trailing","semi-erect","erect","hybrid berry"],"s":OLD,"x":[
  X("Loch Ness","","Semi-erect thornless blackberry from the John Innes line; "+AGM+".",W+"Blackberry",dt="pot or bare-root"),
  X("Triple Crown","","Thornless USDA blackberry with large, firm fruit.",W+"Blackberry"),
  X("Black Satin","","Vigorous thornless semi-erect blackberry needing a trellis.",W+"Blackberry"),
  X("Marion","marionberry","Trailing blackberry from the USDA-ARS programme at Corvallis, Oregon, Chehalem × Olallie.",W+"Blackberry"),
  X("Loganberry","","Blackberry–raspberry hybrid raised by James Harvey Logan in Santa Cruz, California.",W+"Blackberry",y="1880",v=[A("Boysenberry","multi-species Rubus hybrid")]),
  ]},
 {"n":"Currant bush","a":"blackcurrant · redcurrant · whitecurrant · Ribes","d":"Living black, red or white currant bush (Ribes) grown for fruit.","t":["blackcurrant","redcurrant","whitecurrant","pinkcurrant"],"s":W+"Blackcurrant","x":[
  X("Ben Lomond","","First of the Scottish 'Ben' blackcurrants.",W+"Blackcurrant",y="1975",mk=JH,dt=BU,
    v=[A("Ben Sarek","large sweet berries, for gardeners",mk=JH),A("Ben Connan","large sweet berries; "+AGM,mk=JH),A("Ben Hope","gall-mite tolerant","1998",JH)]),
  X("Jonkheer van Tets","","Redcurrant; "+AGM+".",W+"Redcurrant",dt=BU,v=[A("Red Lake","redcurrant; "+AGM),A("Stanza","redcurrant; "+AGM)]),
  X("White Grape","","Whitecurrant, a pale sweet form of Ribes rubrum; "+AGM+".",W+"Redcurrant",dt=BU),
  ]},
 {"n":"Gooseberry bush","a":"Ribes uva-crispa","d":"Living gooseberry bush grown for fruit.","t":["culinary","dessert","red","yellow","green"],"s":W+"Gooseberry","x":[
  X("Invicta","","Gooseberry; "+AGM+".",W+"Gooseberry",dt=BU),
  X("Careless","","Gooseberry; "+AGM+".",W+"Gooseberry",dt=BU),
  X("Whinham's Industry","","Gooseberry; "+AGM+".",W+"Gooseberry",dt=BU,v=[A("Leveller",AGM),A("Greenfinch")]),
  ]},
 {"n":"Grapevine","a":"Vitis · vine","d":"Living grapevine (Vitis) grown for fruit, table and wine grapes.","t":["dessert (table)","wine","seedless","greenhouse","outdoor"],"s":OLD,"x":[
  X("Black Hamburg","Schiava Grossa","Black dessert grape for the glasshouse; the Great Vine at Hampton Court, planted under Capability Brown, is one.","https://www.hrp.org.uk/hampton-court-palace/explore/the-great-vine/",y="1768",dt="pot or bare-root · glasshouse or outdoor"),
  X("Concord","","Fox-grape hybrid (Vitis labrusca) raised by Ephraim Wales Bull at Concord, Massachusetts.",W+"Concord_grape",y="1849",dt="pot or bare-root"),
  X("Regent","","Disease-resistant red wine grape bred by Gerhardt Alleweldt at Geilweilerhof, Germany.",W+"Regent_(grape)",y="1967",dt="pot or bare-root"),
  ]},
 {"n":"Kiwi vine","a":"kiwifruit · Actinidia · kiwiberry","d":"Living kiwifruit or hardy kiwi vine (Actinidia) grown for fruit.","t":["female","male","self-fertile","hardy kiwi (kiwiberry)"],"s":W+"Kiwifruit","x":[
  X("Hayward","","Green kiwifruit raised by Hayward Wright at Avondale, Auckland; the most sold kiwifruit.",W+"Kiwifruit",y="c. 1924",dt="pot size · sex"),
  X("Jenny","","Self-fertile kiwifruit vine with egg-sized fruit, fruiting within about three years.","https://www.rhs.org.uk/plants/99755/actinidia-deliciosa-jenny/details",dt="pot size"),
  X("Issai","","Self-fertile hardy kiwi, Actinidia arguta × A. polygama, with relatively large fruit.",W+"Kiwifruit",dt="pot size"),
  ]},
 {"n":"Elderberry bush","a":"Sambucus","d":"Living elderberry shrub (Sambucus) grown for fruit.","t":["black-leaved","cut-leaved","golden"],"s":OLD,"x":[
  X("Black Lace","Eva · Sambucus nigra f. porphyrophylla 'Eva'","Black-leaved elder with pale pink flowers; "+AGM+".",W+"Sambucus_nigra",dt="pot size",v=[A("Gerda","black-leaved; "+AGM)]),
  X("Laciniata","cut-leaved elder","Cut-leaved form of elder; "+AGM+".",W+"Sambucus_nigra"),
  ]},
]
brands=[
 {"n":JH,"c":"United Kingdom","seg":"Institution & issuer","kf":"soft-fruit breeding","d":"Scottish crop research institute (formerly SCRI) that bred the 'Ben' blackcurrants and Symphony strawberry.","sig":["Ben Lomond","Symphony"],"s":LS},
]
w('C3','06_02',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"All 6 old kinds kept with old s; Currant bush, Gooseberry bush and Kiwi vine added from Wikipedia. Hybrid berries folded into Blackberry plant. Thornless Evergreen, Hinnonmaki, Bruno, Mignonette not on retrieved pages, left out. Glen Ample breeder not stated on retrieved page, so no mk. Kiwi Jenny origin unconfirmed. Elderberry fruiting cultivars (American Sambucus canadensis) not on retrieved pages."})
