import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
L=W+"List_of_mango_cultivars"; FN="https://www.fruitnet.com/asiafruit/mangoes-sell-for-record-us4500/178404.article"
MX=[x("Alphonso","","",W+"Mango","Maharashtra's fibreless 'king of mangoes', a grafted export cultivar available February to May.",
   [v("Alphonso mango GI","","","Indian GI merged here"),v("Bennet Alphonso","","","Old-data entry")],a="Hapus"),
 x("Haden","","1902",W+"Haden_(mango)","Florida cultivar from a Mulgoba seed planted by Captain John Haden at Coconut Grove; parent of most later Florida mangoes.",[v("Haden","","","Old-data name")],a="Mulgoba seedling"),
 x("Tommy Atkins","","1940",L,"Haden seedling from south Florida, firm and long-keeping; the most commonly sold export mango in the West.",[v("Tommy Atkins","","","Old-data name")]),
 x("Kent","","1945",W+"Kent_(mango)","Fibreless Florida mango, a Brooks seedling selected and named in 1945; France's main imported cultivar.",[v("Kent","","","Old-data name")]),
 x("Keitt","","1945",W+"Keitt_(mango)","Late-season Florida mango, large and green with a light red blush, selected and named in 1945.",[v("Keitt","","","Old-data name")]),
 x("Ataulfo","","",W+"Ataulfo_(mango)","Smooth non-fibrous yellow mango from Soconusco, Chiapas, sold as honey, champagne or Manila mango; descended from the Philippine mango.",
   [v("Mango Ataulfo del Soconusco Chiapas DO","","2003","Mexican designation of origin published 2003")],a="Honey mango · Champagne mango"),
 x("Carabao","","",L,"Philippine mango traced to the Manila-Mexico galleon trade; Ataulfo and Manilita derive from it.",[v("Carabao","","","Old-data name")],a="Philippine mango · Manila mango"),
 x("Irwin","","",L,"Red, soft, juicy Florida cultivar grown in Japan, where Miyazaki fruit is sold as Taiyo no Tamago.",
   [v("Taiyo no Tamago","","","Miyazaki top grade of Irwin: at least 350 g, high sugar, at least half the skin red; a pair sold for 500,000 yen in 2019"),v("Irwin","","","Old-data name")],a="Egg of the Sun"),
 x("Nam Dok Mai","","",L,"Elongated yellow-green Thai mango with a prominent beak.",
   [v("Nam Doc Mai","","","Old-data spelling"),v("Ratchaburi Nam Dok Mai mango GI","","","Thai GI, old data"),v("Sa Kaeo Nam Dok Mai Mango GI","","","Thai GI, old data")]),
 x("Chaunsa","","",L,"Pakistani and Indian cultivar harvested June to September.",[v("Chaunsa Mango GI","","","Old-data GI"),v("Chaunsa","","","Old-data name")]),
 x("Sindhri","","",L,"Aromatic sweet mango from Mirpur Khas, Sindh.",[v("Sindhri Mango GI","","","Old-data GI")]),
 x("Anwar Ratol","","",L,"Small, yellow, very sweet, low-fibre mango from Punjab and Uttar Pradesh.",[v("Anwar Ratol","","","Old-data name"),v("Rataul Mango GI","","","Old-data GI for Rataul")]),
 x("Dasheri","","",L,"Lucknow-area mango grown widely since the 18th century.",[v("Mango Malihabadi Dusseheri GI","","","Old-data GI")]),
 x("Kesar","","",L,"Gir Kesar, known for colour and aroma.",[v("Gir Kesar Mango GI","","","Old-data GI"),v("Marathwada Kesar Mango GI","","","Old-data GI")],a="Gir Kesar"),
 x("Langra","","",L,"North Indian monoembryonic cultivar whose variant Dudhia Malda is grown in Bihar and Nepal.",[v("Banaras Langda Aam GI","","","Old-data GI")]),
 x("Banganapalli","","",L,"Andhra Pradesh's most produced mango.",[v("Banaganapalle Mangoes GI","","","Old-data GI"),v("Banganapalli","","","Old-data name")]),
 x("Himsagar","","",L,"Fibreless mango from West Bengal and Bangladesh, also called Khirsapati.",[v("Malda Khirsapati (Himsagar) mango GI","","","Old-data GI"),v("Himsagar","","","Old-data name")],a="Khirsapati"),
 x("Kensington Pride","","",L,"Australian mango cultivar.",[v("Kensington Pride (Bowen)","","","Old-data name")],a="Bowen"),
 x("R2E2","","",L,"Australian mango cultivar.",[v("R2E2","","","Old-data name")])]
kinds=[K("Mango","Fresh or frozen mango, organised by cultivar from Indian, Florida, Mexican and Southeast Asian lines with protected origins.","https://plu.pro/commodity/mango",MX,["Totapuri","Amrapali","Badami","Langra","Neelam","Raspuri","Malda Fazli mango GI","Khirsapat GI","Guimaras mango GI","Hoà Lộc GI","Yên Châu GI","Manilita","Honey Manila","Brooks","Palmer","Zill","Young","Sensation","Julie","Lippens","Jakarta","Turpentine","Saigon","Chok Anan"],["ripe eating","green/raw for pickling"])]
kinds[0]["m"]=[m for m in kinds[0]["m"] if m[0]!="Langra"]
trad=[{"n":"Indian mango culture","g":"Food & drink","r":"India","p":"Ancient to present","d":"Mango cultivation and ritual in South Asia, with groves valued by Ashoka, the Mughals and in worship.",
 "tech":"grafting of monoembryonic cultivars such as Alphonso and Langra","mat":"mango","forms":["Alphonso","Langra","Dasheri","Himsagar"],"ctr":["Maharashtra (Ratnagiri, Raigad)","Lucknow area","Darbhanga orchard of Akbar"],"auth":"Named grafted cultivars; GI marks for several","s":W+"Mango"}]
notes="Cut the 173-entry list to sourced cultivars (nearly all from Wikipedia's mango cultivar list page) plus 23 flat models. All other Indian GIs merged as versions of their cultivar where the old data names the cultivar; the rest are dropped (Fajri Kalan, Kari Ishad, Rewa Sunderja, Kuttiattoor, Goa Mankurad GIs etc.). Dropped hobbyist Florida and Australian seedlings unless in a fetched list. Taiyo no Tamago facts from fruitnet via firecrawl after WebFetch gave 405."
urls=[L,W+"Haden_(mango)",W+"Ataulfo_(mango)",W+"Keitt_(mango)",W+"Kent_(mango)",FN,W+"Mango"]
write("00_09",kinds,[],trad,notes,urls)
