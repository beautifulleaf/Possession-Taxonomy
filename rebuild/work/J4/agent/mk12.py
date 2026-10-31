import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
FG=W+"Fig"; PE=W+"Persimmon"; DP=W+"Date_palm"
kinds=[
K("Fig","Fresh fig; dried figs are in Pantry Staples.","https://www.regione.calabria.it/wp-content/uploads/2023/06/DOP__IGP_e_STG_Registrati_agg_23.03.23.pdf",
 [x("Black Mission","","1768",W+"Mission_fig","Dark, Spanish-origin fig carried to San Diego by Franciscans in 1768; both breba and main crop, skin often cracks when ripe.",[],a="Mission · Franciscana"),
  x("Brown Turkey","","",FG,"Common-type fig that needs no pollination; holds the RHS Award of Garden Merit in the UK."),
  x("Dottato","","",FG,"Common-type fig known as Kadota, mentioned by Pliny the Elder.",[v("Dottato (Kadota)","","","Alternative name")],a="Kadota"),
  x("Brunswick","","",FG,"Common-type fig cultivar."),
  x("Celeste","","",FG,"Common-type fig cultivar.")],
 ["Fico Bianco del Cilento PGI","Figue de Solliès AOP","Fico monnato di Prignano Cilento","Purandar Fig GI","تين دجبة / Figues de Djebba AOC","大竹いちじく GI"]),
K("Date","Dates sold as fresh fruit (khalal, rutab, fresh soft dates on the branch or chilled); packed dried dates are in Pantry Staples.","https://en.wikipedia.org/wiki/Geographical_indications_in_India",
 [x("Medjool","","",W+"Medjool","Large soft Tafilalt, Morocco, date called the king of dates; about 25% of world date trade.",[v("Medjool","","","Also Medjoul, Mejhoul, Majhool")]),
  x("Deglet Nour","","",W+"Deglet_Nour","Soft, translucent, honey-flavoured date from the oasis of Tolga, Algeria; spread to Tunisia in the late 17th century.",[v("Deglet Nour Tunisienne IP","","","Old-data Tunisian IP")]),
  x("Ajwa","","",W+"Ajwa_(date)","Small dark Medina date eaten at Ramadan iftar.",[]),
  x("Sukkari","","",W+"Sukkari","Soft, extremely sweet light-golden date from Al-Qassim, Saudi Arabia.",[])],
 ["Kachchhi Kharek GI","Barhi"],["khalal","rutab","fresh soft"]),
K("Persimmon","Fresh persimmon (kaki), astringent or non-astringent.","https://plu.pro/commodity/persimmon",
 [x("Hachiya","","",PE,"Heart-shaped astringent Japanese persimmon that must be fully ripe before eating.",[v("Hachiya","","","Old-data name"),v("Dojo Hachiya","","","Old-data entry")]),
  x("Fuyu","","",PE,"Squat non-astringent persimmon, the most commonly sold type.",[v("Fuyu","","","Old-data name"),v("California Fuyu","","","Old-data entry")]),
  x("Jiro","","",PE,"Non-astringent Japanese persimmon with medium to large fruit; grown in California as California Maru.",[v("Jiro","","","Old-data name"),v("California Maru","","","Old-data entry")]),
  x("Triumph","","",PE,"Israeli-bred seedless persimmon marketed as Sharon fruit and always CO2-treated; about 30,000 tonnes a year in Israel.",[v("Triumph","","","Old-data name")],a="Sharon fruit"),
  x("Rojo Brillante","","",W+"Diospyros_kaki","Spain's main persimmon, astringent until CO2-treated, grown mostly in the Ribera del Xúquer area of Valencia and marketed as Persimon.",
    [v("Kaki Ribera del Xúquer PDO","","","Spanish PDO"),v("Rojo Brillante","","","Old-data name")],a="Persimon")],
 ["Great Wall","Gosho","Hyakume","Fudegaki","Giombo","Midia","Cioccolatino","Vainiglia","Tipo","Maru","Ormond","Fankio","Saijo","Tamopan","Taishu","Soshu","Suruga","Izu","Hana Fuyu","Hanagosho","Ichida","Matsumoto Wase","Tone Wase","Shogatsu","Dan gam","Hongsi","Sheng","Bảo Lâm GI","Bắc Kạn GI","こおげ花御所柿 GI"],["astringent","non-astringent"],a="Kaki"),
K("Pomegranate","Fresh pomegranate, whole or as packed arils.","https://en.wikipedia.org/wiki/Geographical_indications_in_India",None,["Solapur Pomegranate GI","Grenade de Gabès IP","고흥석류 GI (지리적표시)","Mollar de Elche"],["whole","arils"]),
K("Prickly pear","Fresh Opuntia fruit (tuna, cactus fig); the pad is nopal.","https://www.regione.calabria.it/wp-content/uploads/2023/06/DOP__IGP_e_STG_Registrati_agg_23.03.23.pdf",None,["Ficodindia dell'Etna PGI","Ficodindia di San Cono PGI","Prickly Pear Fruit of Ait Baâmrane GI"],a="Cactus fig · Tuna"),
K("Jujube","Fresh Ziziphus jujuba fruit; dried red dates are in Pantry Staples.","https://www.melissas.com/products/organic-jujubes",
 [x("Li","","",W+"Jujube","North American jujube cultivar.",[]),x("Lang","","",W+"Jujube","North American jujube cultivar.",[]),
  x("Silverhill","","",W+"Jujube","North American jujube also called Tiger Tooth.",[],a="Tiger Tooth")],["Sherwood","So","Shui Men"],a="Chinese date · Red date"),
]
notes="Dried fig entries (Dried Atessa Reale Fig, Fico secco di Carmignano) moved to notes for J5 as the brief directs. Wonderful, Bhagwa, Mollar de Elche PDO: Wikipedia Pomegranate names only Mollar de Elche (as a reference title), so pomegranate has no archetypes; Solapur GI kept flat. Barhi, Hongsi, many Japanese persimmon cultivars kept flat from old data (trimmed 50 to 26). Ficodindia and Ajwa have no GI versions;"
urls=[FG,W+"Mission_fig",W+"Medjool",W+"Deglet_Nour",W+"Ajwa_(date)",W+"Sukkari",DP,PE,W+"Diospyros_kaki",W+"Cactus_fig",W+"Pomegranate",W+"Jujube"]
write("00_12",kinds,[],[],notes,urls)
