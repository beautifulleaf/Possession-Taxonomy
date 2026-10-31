import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
CB=W+"Cultivated_blueberries"
BL=[x("Bluecrop","","1952",CB,"Northern highbush blueberry from the USA, described as the world market leader.",[v("Bluecrop","","","Old-data name")]),
 x("Duke","USDA","1987",W+"Duke_blueberry","Early northern highbush from USDA Beltsville, Maryland, parents Ivanhoe and Earliblue; RHS Award of Garden Merit.",[v("Duke","","","Old-data name")]),
 x("Earliblue","","1952",CB,"Early northern highbush from the USA, parent of Duke.",[v("Earliblue","","","Old-data name")]),
 x("Coville","","1949",CB,"Northern highbush from the USA, named for Frederick Coville.",[v("Coville","","","Old-data name")]),
 x("Berkeley","","1949",CB,"Northern highbush from the USA.",[v("Berkeley","","","Old-data name")]),
 x("Polaris","","1996",CB,"Northern highbush from the USA.",[v("Polaris","","","Old-data name")]),
 x("Lowbush wild blueberry","","",CB,"Wild Vaccinium angustifolium populations, harvested mainly in Maine, small and under 0.7 m high.",[])]
RA=[x("Glen Ample","","",W+"Raspberry","Mid-summer fruiting red raspberry.",[]),
 x("Tulameen","","",W+"Raspberry","Late-summer fruiting red raspberry.",[]),
 x("Autumn Bliss","","",W+"Raspberry","Autumn-fruiting raspberry cropping on first-year canes.",[]),
 x("Munger","","",W+"Rubus_occidentalis","Main black raspberry cultivar, grown around Oregon's Willamette Valley.",[],a="Black raspberry")]
BK=[x("Marionberry","","1956",W+"Marionberry","Oregon trailing blackberry from Chehalem x Olallie by George Waldo, the most planted trailing blackberry.",[v("Marion","USDA-ARS","1956","OSC 928, released with Oregon State University")]),
 x("Boysenberry","","1932",W+"Boysenberry","Large maroon bramble hybrid from Anaheim, California, popularised by Walter Knott in 1932.",[]),
 x("Loganberry","","1881",W+"Loganberry","Blackberry x raspberry hybrid raised accidentally by James Harvey Logan at Santa Cruz, California.",[v("American Thornless","","1933","Thornless mutation")]),
 x("Triple Crown","","",W+"Blackberry","Semi-erect thornless blackberry for trellises.",[],dt="thornless · semi-erect"),
 x("Loch Ness","","",W+"Blackberry","Semi-erect thornless blackberry with an RHS garden award.",[],dt="thornless · semi-erect")]
BC=[x("Ben Lomond","Scottish Crop Research Institute","1975",W+"Blackcurrant","First of the Scottish Ben series of cold-hardy blackcurrants.",[v("Ben Hope","","1998","gall mite tolerance"),v("Ben Gairn","","1998","gall mite tolerance")]),
 x("Ben Sarek","Scottish Crop Research Institute","",W+"Blackcurrant","Large-berried Ben cultivar for gardens and pick-your-own.",[v("Ben Connan","","","RHS Award of Garden Merit"),v("Big Ben","","","RHS Award of Garden Merit")]),
 x("Baldwin","","",W+"Blackcurrant","Long-time industry mainstay, now largely superseded."),
 x("Titania","","",W+"Blackcurrant","North American cultivar for yield, disease resistance and machine harvest.")]
GO=[x("Invicta","","",W+"Gooseberry","Mildew-resistant gooseberry with the RHS Award of Garden Merit."),
 x("Careless","","",W+"Gooseberry","Gooseberry with the RHS Award of Garden Merit."),
 x("Leveller","","",W+"Gooseberry","Gooseberry with the RHS Award of Garden Merit."),
 x("Whinham's Industry","","",W+"Gooseberry","Gooseberry with the RHS Award of Garden Merit."),
 x("Greenfinch","","",W+"Gooseberry","Gooseberry with the RHS Award of Garden Merit.")]
CR=[x("Stevens","","",W+"Cranberry","Most grown cranberry, from 1920s-50s US breeding with Franklin, more insect-resistant than Howes."),
 x("Howes","","",W+"Cranberry","Older US cranberry cultivar, more insect-susceptible than Stevens."),
 x("Early Black","","1847",W+"Cranberry","Planted by Cyrus Cahoon near Harwich, Massachusetts, in 1847."),
 x("Crimson Queen","Rutgers University","",W+"Cranberry","High-yield cultivar bred from the 1980s, many by Nicholi Vorsa at Rutgers.",[v("Mullica Queen","","","Companion high-yield cultivar")])]
MU=[x("Chelsea","","",W+"Morus_nigra","Female self-fertile black mulberry with the RHS Award of Garden Merit, also called King James.",[],a="King James"),
 x("Jerusalem","","",W+"Morus_nigra","Female self-fertile black mulberry with the RHS Award of Garden Merit.")]
SB=[x("Leikora","","",W+"Sea_buckthorn","Dense-fruiting female sea buckthorn with RHS Award of Garden Merit.",[v("Pollmix","","","Male pollinator cultivar with RHS award")])]
kinds=[
K("Blueberry","Fresh blueberry, mainly northern and southern highbush, rabbiteye, half-high and wild lowbush types.","https://plu.pro/commodity/berries",BL,["Bluetta","Bluerose","Denise Blue","Elizabeth","Gila","Greta","Patriot","Rahi","Reka"],["highbush","rabbiteye","lowbush/wild","bilberry"]),
K("Raspberry","Fresh raspberry, red, yellow or black, summer or autumn fruiting.","https://www.cosmos.com.mx/empresa/magromex-3vyl.html",RA,["Ariljska malina GI (PDO/PGI per brochure, not itemised)","고창복분자 GI (지리적표시)"],["red","golden","black","summer-bearing","autumn-fruiting"]),
K("Blackberry","Fresh blackberry, including trailing hybrid brambles sold as blackberries.","https://www.cosmos.com.mx/empresa/magromex-3vyl.html",BK,None,["thornless","trailing hybrid brambles"]),
K("Cranberry","Fresh Vaccinium macrocarpon berries, about 5% of the crop sold fresh.",W+"Cranberry",CR),
K("Blackcurrant","Fresh or frozen blackcurrant (Ribes nigrum).","https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",BC,["あおもりカシス GI"]),
K("Redcurrant & white currant","Fresh or frozen red or white currants (Ribes rubrum).","https://www.producemarketguide.com/produce/specialty-berries/berries/red-currants?page=21",None),
K("Gooseberry","Fresh or frozen gooseberry (Ribes uva-crispa).","https://www.waitrose.com/ecom/shop/browse/groceries/fresh_and_chilled/fresh_fruit/berries/gooseberries",GO),
K("Lingonberry","Fresh Vaccinium vitis-idaea, cowberry, usually cooked and sweetened.",W+"Vaccinium_vitis-idaea",[x("Koralle Group","","",W+"Vaccinium_vitis-idaea","Lingonberry group grown mainly for ornament, with the RHS Award of Garden Merit.")],a="Cowberry"),
K("Cloudberry","Fresh Rubus chamaemorus, wild-picked in the Nordics and not commercially cultivated.",W+"Rubus_chamaemorus",None,a="Bakeapple · Multebær"),
K("Mulberry","Fresh mulberry (Morus).","https://www.mafra.go.kr/bbs/home/792/576894/download.do",MU,["부안오디 GI (지리적표시)"]),
K("Elderberry","Fresh or frozen elderberries (Sambucus), eaten cooked.","https://instacart.com/categories/316-food/317-fresh-produce/318-fresh-fruit/363-berries/2147-elderberries",None),
K("Sea buckthorn","Fresh or frozen Hippophae berries.","https://en.wikipedia.org/wiki/Geographical_indications_in_India",SB,["Ladakh Seabuckthorn GI"]),
]
notes="Rebuilt with sourced cultivars only. No cultivar pages fetched for redcurrant/white currant, elderberry (Wikipedia lists no fruit cultivars), cloudberry (no named cultivars); these have no archetypes. Heritage/Meeker, Jersey, Brigitta, Powderblue, Hinnonmaki, Ben Lear, Red Pearl not confirmed so omitted. Cranberry Ben Lear only in search snippets. Cut blueberry flat list to 9 minor cultivars."
urls=[CB]+[W+p for p in ["Duke_blueberry","Raspberry","Rubus_occidentalis","Blackberry","Marionberry","Boysenberry","Loganberry","Blackcurrant","Gooseberry","Vaccinium_vitis-idaea","Morus_nigra","Sambucus_nigra","Sea_buckthorn","Cranberry","Rubus_chamaemorus"]]
write("00_06",kinds,[],[],notes,urls)
