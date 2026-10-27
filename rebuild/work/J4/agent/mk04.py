import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
LE=[x("Eureka","","",W+"Lemon","The common year-round supermarket lemon, developed in 19th-century California from Italian stock.",
   [v("Eureka","","","Old-data name"),v("Variegated pink Eureka","","1931","Pink-fleshed sport found in Burbank, California")],a="Four Seasons"),
 x("Lisbon","","",W+"Lemon","Thin-skinned, smoother, juicier lemon similar to Eureka, brought to California by Portuguese immigrants."),
 x("Meyer","","1908",W+"Meyer_lemon","Sweeter, rounder citron x mandarin/pomelo hybrid collected in China by Frank Meyer and introduced to the US in 1908.",
   [v("Improved Meyer","","1975","Virus-free University of California selection")]),
 x("Femminello","","",W+"Siracusa_lemon","Italian lemon cultivar and its clones; the base of several Sicilian and Sorrento lemons.",
   [v("Femminello St. Teresa (Sorrento)","","","Zest high in lemon oils, traditional for limoncello"),
    v("Limone di Siracusa PGI","","2011","EU PGI for femminello lemons from ten comuni of Siracusa, no post-harvest wax or fungicide")],a="Sorrento · Sfusato"),
]
LI=[x("Persian lime","","1895",W+"Persian_lime","Seedless triploid Key lime x lemon hybrid, the lime most commonly sold; also Tahiti or Bearss lime.",[],a="Tahiti lime · Bearss lime"),
 x("Key lime","","",W+"Key_lime","Small, thin-skinned, seedy and aromatic West Indian lime named for the Florida Keys; used in Key lime pie.",[],a="Mexican lime · West Indian lime"),
 x("Makrut lime","","",W+"Kaffir_lime","Bumpy Citrus hystrix grown mainly for its leaves and rind in Southeast Asian cooking.",[],a="Kaffir lime · Thai lime")]
YU=[x("Yuzu","","",W+"Yuzu","Fragrant frost-hardy East Asian citrus of Chinese origin, used for juice and zest.",[v("木頭ゆず GI","","","Japanese GI, old data")])]
SU=[x("Sudachi","","",W+"Sudachi","Small green Japanese citrus hybrid, about 98% grown in Tokushima.",[v("徳島すだち GI","","","Japanese GI, old data")])]
KA=[x("Kabosu","","",W+"Kabosu","Larger green Japanese citrus (100-140 g) native to Ōita, about 99% of national output.",[])]
BI=[x("Seville orange","","",W+"Bitter_orange","The bitter orange of marmalade, high in pectin.",[v("Seville (marmalade orange)","","","Old-data name")],a="Marmalade orange"),
 x("Chinotto","","",W+"Bitter_orange","Myrtle-leaved bitter orange variety used for the soft drink of the same name."),
 x("Bergamot","","",W+"Bitter_orange","Probably a bitter orange x limetta hybrid grown in Italy for bergamot oil, used in Earl Grey tea.")]
KU=[x("Nagami","","",W+"Kumquat","Oval kumquat, the common eating kumquat in China and Japan."),
 x("Meiwa","","",W+"Kumquat","Rounder kumquat grown in China and Japan."),
 x("Marumi","","",W+"Kumquat","Round kumquat grown in China and Japan.")]
CI=[x("Etrog","","",W+"Citron","Acidic-pulp citron used in the Sukkot ritual.",[]),
 x("Buddha's hand","","",W+"Citron","Fingered citron without pulp, used for aroma and zest, native to China.",[]),
 x("Diamante citron","","",W+"Citron","Italian acidic-pulp citron (cedro), candied as succade.",[])]
FL=[x("Rainforest Pearl","","",W+"Australian_lime","Pink-fruited finger lime form from Bangalow, New South Wales."),
 x("Australian Blood","","",W+"Australian_lime","Red-fruited cross of finger lime and an acid mandarin."),
 x("Australian Sunrise","","",W+"Australian_lime","Finger lime x calamondin hybrid with orange pear-shaped fruit.")]
kinds=[
K("Lemon","Fresh lemon, organised by cultivar with its protected origin.","https://plu.pro/commodity/lemons",LE,["Bonnie Brae","Wonderful Seedless","Yen Ben","Citron de Menton PGI","Limone Costa d'Amalfi PGI","Limone di Sorrento PGI","Limone dell'Etna PGI","Limone Femminello del Gargano PGI","Limone Interdonato Messina PGI","Limone di Rocca Imperiale PGI","Kachai Lemon GI","安岳柠檬"]),
K("Lime","Fresh lime, Persian (Tahiti), Key (Mexican) or makrut.","https://plufinder.com/plu/4048",LI,["Damnoen Saduak lime GI","Indi Limbe GI","Limón de Pica IG"],["Persian","Key","makrut"]),
K("Yuzu","Fresh yuzu (Citrus junos).","https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",YU),
K("Sudachi","Fresh Citrus sudachi, a small acid citrus.","https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",SU),
K("Kabosu","Fresh Citrus sphaerocarpa from Ōita, a green citrus for ponzu and grilled fish.",W+"Kabosu",KA),
K("Bitter orange","Fresh Citrus aurantium, sold for marmalade and seasoning.","https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",BI,["辺塚だいだい GI"]),
K("Kumquat","Fresh kumquat (Fortunella), eaten whole.","https://www.legislation.gov.uk/eur/1996/1107/2008-11-20/data.xht",KU,["宁波金柑 地理标志产品"]),
K("Citron","Fresh Citrus medica: etrog, Buddha's hand and cedro, used for peel and aroma.",W+"Citron",CI),
K("Finger lime","Fresh Citrus australasica, the caviar-like Australian lime.",W+"Australian_lime",FL),
]
notes="Femminello archetype carries the Siracusa PGI and Sorrento form as versions; other Italian lemon PGIs kept flat (not individually retrieved). Verna, Menton, Amalfi unconfirmed as cultivars. Lime and yuzu GIs only from old data. Etrog/Greek citron variety separate page not fetched."
urls=[W+p for p in ["Lemon","Meyer_lemon","Siracusa_lemon","Persian_lime","Key_lime","Kaffir_lime","Yuzu","Sudachi","Kabosu","Bitter_orange","Kumquat","Citron","Australian_lime"]]
write("00_04",kinds,[],[],notes,urls)
