import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
LIST=W+"List_of_pear_cultivars"
PX=[
x("Williams' Bon Chrétien","","c.1770",W+"Williams_pear","English summer pear from Aldermaston, called Bartlett in North America; the canning and Poire Williams pear.",
  [v("Bartlett (Williams)","","","Old-data name"),v("Bartlett Max Red","","","Red-skinned US sport"),v("Bartlett Red Sensation","","","Red-skinned US sport")],a="Williams · Bartlett"),
x("Conference","","1885",W+"Conference_pear","Elongated English autumn pear raised by Thomas Rivers at Sawbridgeworth; about 90% of UK pears.",
  [v("Red Conference","","","Red-skinned mutant"),v("Conference pears of Savoie PGI","","1996","EU Protected Geographical Indication")]),
x("Doyenné du Comice","","1849",W+"Doyenné_du_Comice","Large late-season dessert pear found at Angers, France; sold in the US as Royal Riviera.",
  [v("Comice (Doyenne du Comice)","","","Old-data name"),v("Taylors Gold","","","Mutation of Comice"),v("Sweet Sensation","","2010","Comice mutation discovered 1992 in the Netherlands; club pear")],a="Comice"),
x("Anjou","","",W+"D'Anjou","Short-necked green pear sold in the US since the 1850s, originally Nec Plus Meuris; Red Anjou is a bud sport.",
  [v("Anjou (D'Anjou)","","","Old-data name"),v("Anjou Red","","","Natural bud sport of Green Anjou")]),
x("Bosc","","",W+"Bosc_Pear","Long-necked cinnamon-russet pear of Belgian or French origin whose dense flesh holds its shape when baked.",
  [v("Bosc (Beurre Bosc)","","","Old-data name")],a="Beurré Bosc · Kaiser"),
x("Abate Fetel","","1865",LIST,"Elongated pear bred in France by Abbot Fetel; Italy's most produced and exported pear cultivar.",
  [v("Pera dell'Emilia Romagna PGI","","","Emilia-Romagna PGI for the cultivar, per Wikipedia's Abate Fetel article"),
   ]),
x("Pêra Rocha","","1836","https://agriculture.ec.europa.eu/farming/geographical-indications-and-quality-schemes/geographical-indications-food-and-drink/pera-rocha-do-oeste-pdo_en","Portuguese pear found by Pedro António Rocha at Sintra; melting, sugary flesh and long keeping.",
  [v("Pêra Rocha do Oeste PDO","","2003","EU Protected Designation of Origin, grown and packed in 29 municipalities of the Oeste region")],a="Rocha"),
x("Packham's Triumph","","1896",LIST,"Australian pear from Uvedale's St. Germain x Williams."),
x("QTee","","1997",LIST,"Swedish-Norwegian club pear from Colorée de Juillet x Bartlett, listed under Celina.",
  [v("Celina (QTee)","","","Cultivar name behind the QTee mark")]),
x("Angelys","","1999",LIST,"French club pear from Doyenné d'hiver x Doyenné du Comice, introduced from Angers in 1999."),
]
AX=[
x("Nijisseiki","","1898",W+"Nashi_pear","Green-skinned Japanese nashi pear whose name means 20th century.",[v("Nijisseiki (20th Century)","","","Old-data name")],a="20th Century"),
x("Kosui","","1959",W+"Nashi_pear","Russet Japanese nashi pear, the most important cultivar in Japan."),
x("Hosui","","1972",W+"Nashi_pear","Russet Japanese nashi pear, sweet and juicy."),
x("Shinko","","",W+"Nashi_pear","Russet Japanese nashi pear known before 1941."),
x("Niitaka","","1927",W+"Nashi_pear","Russet Japanese pear grown in Korea as Singo, the country's main pear.",
  [v("나주배","","","Naju pear, Singo grown at Naju, South Jeolla; exported to the US and over thirty countries")],a="Singo · Shingo"),
]
LX=[x("Mogi","","",W+"Loquat","Self-fertile Japanese loquat cultivar."),
    x("Tanaka","","",W+"Loquat","Late-ripening loquat from Portugal, grown in gardens rather than commercially."),
    x("Peluche","","",W+"Loquat","Largest and sweetest loquat, about 70 g and Brix near 16, found mainly in Spain.")]
QX=[x("Vranja","","",W+"Quince","Serbian quince with the RHS Award of Garden Merit."),
    x("Serbian Gold","","",W+"Quince","Quince with the RHS Award of Garden Merit.")]
MX=[x("Nottingham","","",W+"Mespilus_germanica","Medlar cultivar holding the RHS Award of Garden Merit."),
    x("Dutch","","",W+"Mespilus_germanica","Large-fruited medlar, also called Giant or Monstrous.",a="Giant · Monstrous"),
    x("Royal","","",W+"Mespilus_germanica","High-yielding medlar cultivar."),
    x("Large Russian","","",W+"Mespilus_germanica","Medlar cultivar grown for fruit.")]
pm=["Alexander Lucas","Beurre Hardy","Blanquilla","Clapp's Favourite","Concorde","Forelle (Corella)","Louise Bonne","Merton Pride","Seckel","Santa Maria","Williams","Passe Crassane","Winter Nelis (Honey)","Pöllauer Hirschbirne PDO","Pera mantovana PGI","山形ラ・フランス GI","Starkrimson","Moonglow","Comtesse de Paris","Glou Morceau","Durondeau","Josephine de Malines"]
pm=[p for p in pm if p!="Williams"]
kinds=[
K("Pear","Fresh European pear, organised by cultivar with its protected origin or club brand.","https://plu.pro/commodity/pears",PX,pm,["European dessert","perry/cooking"]),
K("Asian pear","Fresh round, crisp-fleshed Asian pear, a different fruit from the European pear.","https://plu.pro/commodity/pears",AX,["Chinese Yali","Chojuro","Kikusui","Shinseki","Tsu Li","Yakumo","Abas Beki"],a="Nashi · Apple pear"),
K("Quince","Fresh quince (Cydonia oblonga), sold to cook.","https://producemarketguide.com/produce/specialties/quince?page=5",QX),
K("Loquat","Fresh loquat (Eriobotrya japonica).","https://www.legislation.gov.uk/eur/1996/1107/2008-11-20/data.xht",LX,["Nísperos Callosa d'En Sarriá PDO"]),
K("Medlar","Fresh Mespilus germanica fruit, eaten bletted after frost or storage.",W+"Mespilus_germanica",MX),
K("Hawthorn fruit","Fresh Crataegus fruit sold to eat or cook.","https://www.cnipa.gov.cn/art/2026/5/8/art_2089_206331.html",None,["八虎山山楂 地理标志产品"]),
]
notes="Pear list trimmed from 163 to the cultivars with sources; dropped obscure local and old English cultivars and club lines without a retrieved page. Forelle and Rocha kept; Forelle has no retrieved page so stays flat. Ya Li not confirmed so kept flat as Chinese Yali. Shingo is Singo/Niitaka per sources. Hawthorn and quince/loquat GIs kept flat (no cultivar pages)."
urls=[LIST,W+"Williams_pear",W+"Conference_pear",W+"Doyenné_du_Comice",W+"D'Anjou",W+"Bosc_Pear",W+"Abate_Fetel",W+"Nashi_pear",W+"Quince",W+"Loquat",W+"Mespilus_germanica","https://agriculture.ec.europa.eu/farming/geographical-indications-and-quality-schemes/geographical-indications-food-and-drink/pera-rocha-do-oeste-pdo_en","https://www.freshplaza.com/article/2188332/korea-s-top-export-pear-the-naju-pear/"]
write("00_01",kinds,[],[],notes,urls)
