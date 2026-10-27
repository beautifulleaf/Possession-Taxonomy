import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
C=W+"Cabbage"
cab=[A("White cabbage",C,"Smooth, pale green Dutch-type head cabbage.",a="Dutch · Winter White",dt="white/green head"),
A("Red cabbage",C,"Smooth red leaves, used for pickling or stewing.",dt="red head"),
A("Savoy cabbage",C,"Crimped, curly leaves with mild flavour and tender texture.",dt="crinkled"),
A("Spring greens",C,"Loose-headed cabbage, sliced and steamed.",dt="loose head"),]
nap=[A("Napa cabbage",W+"Napa_cabbage","Brassica rapa pekinensis, oblong crinkly light-green head with white veins, from near Beijing.",a="wong bok · hakusai · baechu · Chinese leaf",v=[("Yuki","","","fall cultivar, RHS AGM 2003"),("Dong-Pung","","1992","Korean winter cultivar"),("Nae-Seo-beak-ro","","1973","Korean summer cultivar")])]
bro=[A("Calabrese",W+"Broccoli","The familiar green-headed broccoli, named after Calabria.",dt="10-20 cm heads"),
A("Sprouting broccoli",W+"Broccoli","White or purple broccoli with many heads on thin stalks.",a="purple sprouting"),
A("Broccolini",W+"Broccoli","Cross of broccoli and kai-lan.",a="Tenderstem · baby broccoli",mk="Sakata"),
A("Beneforté",W+"Broccoli","High-glucoraphanin broccoli bred using wild Brassica oleracea var. villosa.")]
cau=[A("White cauliflower",W+"Cauliflower","The most common colour, white curd in green leaves.",dt="white"),
A("Orange cauliflower",W+"Cauliflower","Beta-carotene colour from a Canadian mutant.",v=[("Cheddar",),("Orange Bouquet",)]),
A("Green cauliflower",W+"Cauliflower","Green curd, sometimes sold as broccoflower.",v=[("Alverda",),("Green Goddess",),("Vorda",)]),
A("Purple cauliflower",W+"Cauliflower","Anthocyanin-coloured curd.",v=[("Graffiti",),("Purple Cape",)]),
A("Romanesco",W+"Cauliflower","Green variety with spiral fractal curds.",v=[("Minaret",),("Veronica",)])]
kale=[A("Lacinato",W+"Kale","Bumpy-leaf black cabbage.",a="cavolo nero · Tuscan kale · dinosaur kale",v=[("Tuscan kale (Lacinato)",)]),
A("Curly kale",W+"Kale","Curly-leaved kale group.",a="Scots kale · blue curled",v=[("Scots kale",),("Blue curled kale",)]),
A("Red Russian",W+"Kale","Flat-leaf kale introduced to North America by Russian traders in the 19th century.",v=[("White Russian",)]),
A("Ornamental kale",W+"Kale","Kale grown for coloured centres; edible but tougher.")]
coll=[A("Georgia Southern",W+"Collard_(plant)","Popular US collard cultivar.",v=[("Vates",),("Morris Heading",),("Blue Max",),("Top Bunch",)]),
A("Butter collard",W+"Collard_(plant)","Couve manteiga of Brazil and Portugal, Tronchuda Group.",a="couve manteiga · couve tronchuda")]
koh=[A("White Vienna",W+"Kohlrabi","Common pale green kohlrabi.",v=[("White Danube",)]),
A("Purple Vienna",W+"Kohlrabi","Purple-skinned kohlrabi with pale flesh.",v=[("Purple Danube",)]),
A("Gigante",W+"Kohlrabi","Very large kohlrabi that stays tender.",a="Superschmelz")]
pak=[A("White-stemmed pak choi",W+"Bok_choy","Dark green leaves with white stems, grown mainly in South China.",a="baak choi · buk choy"),
A("Green-stemmed pak choi",W+"Bok_choy","Lighter leaves and green stems, more common in East China.",a="Shanghai green · pak choy")]
kinds=[K("Cabbage","Fresh cabbage of any head type: white, red, savoy, pointed, spring greens.",x=cab,t=["white/green","red","savoy","pointed","spring greens"],s="https://plu.pro/commodity/cabbage",m=["Dithmarscher Kohl PGI","Filderkraut PGI","Varaždinsko zelje PDO","Pointed cabbage","Futoški sveži i kiseli kupus","Rosolini Cavolo Vecchio"]),
K("Chinese cabbage","Fresh Chinese cabbage (Brassica rapa, Pekinensis group); ordinary head cabbage is separate.",x=nap,s="https://www.melissas.com/products/bok-choy-and-napa-cabbage-leaves-asian-essentials",m=["해남겨울배추"]),
K("Broccoli","Fresh or frozen broccoli.",x=bro,t=["calabrese","sprouting","tenderstem","Romanesco"],s="https://plu.pro/commodity/broccoli",m=["Broccolo aprilatico di Paternopoli","Broccolo di Torbole","大山ブロッコリー GI"]),
K("Cauliflower","Fresh or frozen cauliflower, whole head or florets, of any curd colour.",x=cau,t=["white","coloured curd"],s="https://plufinder.com/plu/4571"),
K("Brussels sprout","Fresh or frozen Brussels sprouts.",x=[A("Red Brussels sprout",W+"Brussels_sprout","Purple types from purple cabbage × green sprouts, sweeter than green.",v=[("Ruby Crunch",),("Red Bull",)])],s="https://extension.usu.edu/vegetableguide/brassica/varietal-selection"),
K("Kale","Fresh or frozen kale.",x=kale,s="https://plu.pro/commodity/kale",m=["Jersey kale","Chiacchietegli di Priverno"]),
K("Collard greens","Fresh Brassica oleracea var. viridis leaves.",x=coll,s=W+"Collard_(plant)"),
K("Cime di rapa","Fresh broccoli rabe (Brassica rapa, Ruvo group).",s=W+"Rapini",a="broccoli rabe · rapini · broccoletti"),
K("Kohlrabi","Fresh kohlrabi.",x=koh,s="https://extension.usu.edu/vegetableguide/brassica/varietal-selection",m=["Aci Trunzu Kohlrabi"]),
K("Pak choi","Fresh pak choi (Brassica rapa, Chinensis group).",x=pak,t=["baby"],s="https://www.melissas.com/products/bok-choy-and-napa-cabbage-leaves-asian-essentials",a="bok choy"),
K("Gai lan","Fresh Brassica oleracea var. alboglabra.",t=["baby gai lan"],s="https://www.epicgardening.com/types-of-broccoli/",a="Chinese broccoli · kai-lan"),
K("Komatsuna","Fresh komatsuna (Brassica rapa var. perviridis).",x=[A("Goseki bansei",W+"Komatsuna","Old komatsuna variety said to have been served to the shogun; fewer, larger, spicy leaves.")],s="https://www.goodeggs.com/vvlakesideorganics/organic-komatsuna/69a5c002bac93c08916cc269",a="Japanese mustard spinach"),
]
brands=[{"n":"Sakata","c":"Japan","f":"1913","seg":"Specialist","kf":"vegetable seed breeding","d":"Japanese seed company, breeder of the Tenderstem/broccolini broccoli.","s":"knowledge"}]
save("01_09",kinds,brands,[],"Head cabbage kinds merged. January King, Hispi, Golden Acre not on retrieved page (dropped). Napa moved into Chinese cabbage. Sakata brand from knowledge (founding year to verify).")
