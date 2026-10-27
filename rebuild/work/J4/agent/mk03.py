import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
AZ="https://extension.arizona.edu/sites/extension.arizona.edu/files/pubs/az1925-2021.pdf"
OR=[x("Washington navel","","1873",W+"Navel_orange","Seedless navel orange from a Bahia, Brazil, mutation; Washington trees reached Riverside, California, in 1873.",
  [v("Cara Cara","","1976","Red-fleshed navel found at Hacienda Caracara, Valencia, Venezuela; likely a bud sport of Washington navel"),
   v("Navelina (Newhall)","","","Old-data entry"),v("Navelate","","","Old-data entry")],a="Navel",dt="seedless · propagated by grafting"),
 x("Valencia","","1865",W+"Oranges","Late-season juicing orange catalogued in England in 1865 as Excelsior after import from the Azores.",
  [v("Valencia","","","Old-data name"),v("Smith Red Valencia","","","Old-data entry")]),
 x("Cara Cara","","1976",W+"Cara_Cara_navel_orange","Pink-fleshed navel, sweet and low in acid, coloured by lycopene, sometimes sold as Power Orange.",[]),
]
OR=[OR[0],OR[1]]
BO=[x("Moro","","c.1800",W+"Blood_orange","Deepest-red blood orange, a bud mutation of Sanguinello Moscato from Lentini, Sicily."),
 x("Tarocco","","",W+"Blood_orange","Lighter-pigmented Sicilian blood orange, a mutation of Sanguinello and Italy's most popular table orange."),
 x("Sanguinello","","",W+"Blood_orange","Full-blood orange close to Moro in character.",[]),
 x("Arancia Rossa di Sicilia","","",W+"Blood_orange","Multi-cultivar PGI for blood oranges (Tarocco, Moro, Sanguinello) from eastern Sicily.",
   [v("Arancia Rossa di Sicilia PGI","","","EU Protected Geographical Indication")])]
MA=[x("Dekopon","Sumo Citrus","1972",W+"Dekopon","Large bumpy Japanese mandarin hybrid of Kiyomi x Ponkan, sold in the US as Sumo Citrus.",
   [v("Sumo Citrus","Sumo Citrus","2011","US brand; first sold early 2011, budwood imported 1998"),v("Dekopon","","","Only fruit above 13 degrees Brix and under 1.0% acid may be sold as dekopon")],a="Shiranui · Sumo Citrus"),
 x("Ponkan","","",W+"Mandarin_orange_varieties","Mandarin-pomelo hybrid and parent of Dancy and Dekopon."),
 x("Murcott","","",W+"Mandarin_orange_varieties","Mandarin x sweet orange hybrid (tangor).",
   [v("Murcott (Honey)","","","Old-data name"),v("Tango (Tangold)","","","Seedless irradiated selection of Murcott from the University of California Citrus Breeding Program")]),
 x("Kinnow","","",W+"Mandarin_orange_varieties","King x Willowleaf cross developed by H. B. Frost."),
 x("Dancy","","",W+"Mandarin_orange_varieties","Ponkan x hybrid mandarin; the most common US tangerine until the 1970s.")]
CL=[x("Clementine","","1902",W+"Clementine","Mandarin x sweet orange hybrid from Misserghin, Algeria, named after Clément Rodier in 1902.",
   [v("Clemenules (Nules)","","","Mutation of Fina; most widely planted clementine in Spain"),v("Fina","","","Spanish cultivar"),
    v("Clementine di Calabria","","","Italian PGI"),v("Clementine del Golfo di Taranto","","","Italian PGI"),
    v("Clémentine de Corse PGI","","2007","Corsican PGI, old data")])]
SA=[x("Owari","","",W+"Citrus_unshiu","Most widely grown satsuma, taken to the US in 1878; the base for most other satsuma cultivars.",[v("Owari","","","Old-data name")]),
 x("Miyagawa Wase","","",W+"Citrus_unshiu","Early Japanese satsuma, one of three cultivars making nearly half of Japan's output."),
 x("Okitsu Wase","","",W+"Citrus_unshiu","Early Japanese satsuma, one of the three leading Japanese satsuma cultivars."),
 x("Aoshima Unshu","","",W+"Citrus_unshiu","Leading Japanese satsuma cultivar.",[v("Aoshima Unshu","","","Old-data name")])]
GR=[x("Marsh","","1862",AZ,"Seedless white grapefruit that arose before 1862 as a root sprout in Florida; the cultivar that eclipsed Duncan.",[]),
 x("Ruby Red","","1929",AZ,"Red grapefruit from a Thompson mutation in McAllen, Texas; sold also as Redblush.",[v("Redblush","","1931","Same type found in McAllen in 1931")],a="Redblush"),
 x("Star Ruby","","1970",AZ,"Intensely red grapefruit developed by irradiating Hudson seed; released by Texas A&I.",[]),
 x("Rio Red","","1976",AZ,"Texas budsport from Ruby Red descent in 1976; the leading red grapefruit alongside Flame.",[]),
 x("Flame","","1973",AZ,"Red grapefruit from a Ruby Red mutation near Houston, released by USDA in 1987.",[])]
PO=[x("Banpeiyu","","1920",W+"Banpeiyu","Very large nearly spherical pomelo that reached Japan via Taiwan in 1920; record fruit 4.86 kg at Yatsushiro, Kumamoto.",
   [v("八代特産晩白柚 GI","","","Japanese GI, old data")])]
for a in (OR,BO,GR): pass
BO[2]["d"]="Full-blood Sicilian orange close to Moro in character."
kinds=[
K("Orange","Fresh sweet orange, organised by navel, Valencia and other cultivars and their protected origins.","https://plu.pro/commodity/oranges",OR,["Hamlin","Pera","Salustiana","Shamouti","Lima","Midknight","Temple","Delta Seedless","Arancia del Gargano PGI","Arancia di Ribera PGI","Πορτοκάλια Μάλεμε Χανίων Κρήτης PDO","Trebisacce Late Harvest Blonde Orange","Jalna Sweet Orange GI","永兴冰糖橙"] if False else ["Pera","Salustiana","Shamouti","Lima","Midknight","Temple","Delta Seedless","Arancia del Gargano PGI","Arancia di Ribera PGI","Πορτοκάλια Μάλεμε Χανίων Κρήτης PDO","Trebisacce Late Harvest Blonde Orange","Jalna Sweet Orange GI","永兴冰糖橙","Cao Phong GI"],["navel","Valencia/juicing","common"]),
K("Blood orange","Red-fleshed sweet orange, mainly Sicilian Moro, Tarocco and Sanguinello.","https://plu.pro/commodity/oranges",BO,["Doblafina","Entrefina","Washington Sanguine","Vaccaro","Bream Tarocco"]),
K("Mandarin","Fresh mandarin or tangerine other than clementine and satsuma, including mandarin hybrids sold as mandarins.","https://plu.pro/commodity/tangerinesmandarins",MA,["C37 (Noble Juicy Crunch)","Fairchild","Imperial","Ellendale","Nova","Sunburst","Fall Glo","Nagpur","Coorg orange GI","Khasi Mandarin GI","Neretvanska mandarina PDO","桜島小みかん GI"],["tangor","tangelo"]),
K("Clementine","Small seedless, easy-peel mandarin type sold as clementine.","https://plu.pro/commodity/tangerinesmandarins",CL,["Marisol" if False else "Fortune","Monreal","Sweetclems","Clementinas de las Tierras del Ebro o Clementines de les Terres de l'Ebre PGI"]),
K("Satsuma","Loose-skinned, seedless mandarin type sold as satsuma or mikan.","https://plu.pro/commodity/tangerinesmandarins",SA,["Yatsushiro","Wenzhou migana","香川小原紅早生みかん GI"],a="Mikan · Unshiu"),
K("Grapefruit","Fresh grapefruit, white or red fleshed.","https://plu.pro/commodity/grapefruit",GR,[["Sweet Scarletts","The Wonderful Company"]]),
K("Pomelo","Fresh pomelo (pummelo), the large thick-skinned citrus.","https://plu.pro/commodity/grapefruit",PO,["Dangyuja","Pomelo de Corse PGI","Devanahalli Pomello GI","Bình Minh GI","Đoan Hùng GI","Phúc Trạch GI","Tân Triều GI","Luận Văn GI"],a="Pummelo · Shaddock"),
]
brands=[
B("Sumo Citrus","United States","Specialist","club mandarin brand","US trade name for the Dekopon mandarin, first sold in early 2011 from budwood imported in 1998.",W+"Dekopon",sig=["Dekopon"]),
B("Sunkist","United States","Specialist","growers' co-operative","California-based citrus growers' co-operative marketing fresh oranges, lemons and grapefruit.","knowledge"),
B("The Wonderful Company","United States","Specialist","Halos mandarins","Privately held US grower whose Wonderful Citrus unit sells Halos mandarins and Sweet Scarletts grapefruit.","knowledge",lines=["Halos","Sweet Scarletts"]),
B("Outspan","South Africa","Specialist","citrus export brand","South African citrus export brand of fresh oranges and other citrus.","knowledge"),
]
notes="Orange list trimmed to cultivars with retrieved pages (Washington navel, Valencia) plus flat GIs. Not confirmed by any retrieved page and so left out as archetypes: Lane Late, Hamlin, Shamouti/Jaffa, Nadorcott, Ortanique, Setoka, Beni Madonna, Kanpei, Marisol, Thong Dee, Nam Roi (Vietnamese GIs kept flat), Oroblanco/Sweetie, Mikkabi, Arida, Ehime mikan GIs (Wikipedia does not list these as cultivars). Cara Cara kept as a version of Washington navel because Wikipedia says it is a likely bud sport."
urls=[W+p for p in ["Navel_orange","Cara_Cara_navel_orange","Oranges","Blood_orange","Mandarin_orange_varieties","Dekopon","Clementine","Citrus_unshiu","Banpeiyu","Pomelo"]]+[AZ]
write("00_03",kinds,brands,[],notes,urls)
