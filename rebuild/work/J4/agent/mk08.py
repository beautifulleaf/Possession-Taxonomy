import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
ME=W+"Melon"
MX=[x("Cantaloupe","","",W+"Cantaloupe","Orange-fleshed melon: the ribbed European cantaloupe and the netted North American muskmelon (rockmelon in Australasia, spanspek in southern Africa).",
   [v("Cantaloupe (Muskmelon, Rockmelon)","","","Old-data name"),v("Cantaline (Orange Flesh)","","","Old-data name"),v("Sugar melon","","","Small silvery ribbed cantaloupe type")],a="Muskmelon · Rockmelon"),
 x("Charentais","","",W+"Charentais_melon","Small, intensely aromatic French cantaloupe from the Charentes, most grown melon in France and poor at shipping.",[v("Melon du Quercy PGI","","","Old-data PGI"),v("Melon de Cavaillon PGI","","","Old-data PGI"),v("Melon du Haut-Poitou PGI","","","Old-data PGI")]),
 x("Galia","","1973",W+"Galia_melon","Israeli F1 hybrid of Ha'Ogen x Krymka bred by Zvi Karchi at Ne've Yaar and released in 1973.",[v("Galia","","","Old-data name")],a="Sarda"),
 x("Honeydew","","",ME,"Smooth pale inodorus melon with sweet green flesh.",[v("Honeydew","","","Old-data name"),v("Honey Green (Papaya Melon)","","","Old-data name")]),
 x("Piel de Sapo","","",W+"Santa_Claus_melon","Spanish toad-skin melon, green striped, mild and keeping until Christmas.",[v("Piel de Sapo","","","Old-data name"),v("Tendral (Spanish)","","","Old-data entry")],a="Santa Claus melon · Christmas melon"),
 x("Canary","","",ME,"Yellow-skinned inodorus melon of the casaba type.",[v("Canary (Yellow Honeydew)","","","Old-data name")]),
 x("Hami melon","","",W+"Hami_melon","Sweet crisp melon from Xinjiang, China, known since the Han dynasty; also called snow melon.",[v("Hami (Snow Melon)","","","Old-data name")],a="Snow melon"),
 x("Yubari King","","",W+"Yubari_King","Hokkaido greenhouse cantaloupe from Earl's Favourite x Burpee's Spicy; top melons sell for millions of yen.",[v("夕張メロン GI","","","Japanese GI, old data"),v("Yubari King","","","Old-data name")]),
 x("Crenshaw","","",ME,"Casaba x Persian hybrid melon.",[v("Crenshaw","","","Old-data name")]),
]
WA=[x("Charleston Gray","","1954",W+"Watermelon","Oblong grey USDA watermelon by Charles Andrus, resistant to anthracnose and fusarium wilt.",[v("Charleston Gray","","","Old-data name")]),
 x("Jubilee","","1963",W+"Watermelon","University of Florida watermelon by J. M. Crall.",[v("Jubilee watermelon","","","Old-data name")]),
 x("Crimson Sweet","","1964",W+"Watermelon","Kansas State watermelon by C. V. Hall, whose lineage fed modern hybrids.",[v("Crimson Sweet","","","Old-data name")]),
 x("Moon and Stars","","1926",W+"Watermelon","Heirloom purple-black watermelon with yellow star and moon spots, fruit about 9-23 kg.",[v("Moon and Stars","","","Old-data name")]),
 x("Densuke","","",W+"Watermelon","Black unstriped watermelon grown only on Hokkaido; a 2008 fruit sold for 650,000 yen.",[v("Densuke","","","Old-data name")]),
 x("Golden Midget","","",W+"Watermelon","Small golden-rinded icebox watermelon with pink flesh.",[v("Golden Midget","","","Old-data name")]),
 x("Cream of Saskatchewan","","",W+"Watermelon","Small cool-climate icebox watermelon about 25 cm across.",[v("Cream of Saskatchewan","","","Old-data name")])]
kinds=[K("Melon","Fresh melon other than watermelon, sold whole or cut.","https://plu.pro/commodity/melon",MX,["Argos","Banana melon","Gaya","Kolkhoznitsa","Korean melon","Persian","Ogen","Sharlyn","Pixie","Honeymoon","Casaba","Melone Mantovano PGI","Melon de Guadeloupe PGI","Torres de Berrellén Melon","Alcamo Purceddu Melon","Paceco Cartucciaru Melon","Antichi meloni reggiani","Melone di Calvenzano"],["cantaloupe","honeydew","netted","smooth"]),
K("Watermelon","Fresh watermelon, sold whole or cut.","https://plu.pro/commodity/melon",WA,["Anguria Reggiana PGI","Sugar Baby","Black Diamond","Carolina Cross","Georgia Rattlesnake","Orangeglo","Kherson watermelon GI","入善ジャンボ西瓜 GI","Tom Watson"],["seeded","seedless","mini","red flesh","yellow flesh"])]
notes="Quincy, Andes, Crown Melon (Shizuoka), Chamoe/Korean melon and Asian netted melons not on fetched pages: Korean melon kept flat. Sugar Baby not on any fetched page so flat. Anguria Reggiana PGI kept flat (not retrieved). Cut melon list to cultivars with sources plus 18 flat models. Charentais page doesn't mention the PGIs; they're old-data versions."
urls=[ME]+[W+p for p in ["Galia_melon","Yubari_King","Charentais_melon","Hami_melon","Santa_Claus_melon","Cantaloupe","Watermelon","Sugar_melon"]]
write("00_08",kinds,[],[],notes,urls)
