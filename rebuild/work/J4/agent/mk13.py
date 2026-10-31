import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
kinds=[
K("Custard apple","Fresh Annona fruit of any species; species names overlap by region.","https://en.wikipedia.org/wiki/List_of_Andalusian_food_and_drink_products_with_protected_status",
 [x("Fino de Jete","","",W+"Cherimoya","Cherimoya cultivar behind the Granada-Málaga Costa Tropical fruit, balancing sweetness with slight acidity.",
    [v("Chirimoya de la Costa Tropical Designation of Origin","","","Spanish designation; fruit picked by hand and packed within 24 hours")]),
  x("Atemoya","","1908",W+"Atemoya","Hybrid of cherimoya and sugar apple first crossed by P. J. Wester at the USDA lab in Miami in 1908.",
    [v("Gefner","","","Israeli cultivar, fruit to 450 g, about 25 degrees Brix"),v("Thompson","","","Most cultivated atemoya in Brazil")]),
  x("Sugar apple","","",W+"Custard_Apple","Annona squamosa, also called sweetsop.",[]),
  x("Soursop","","",W+"Custard_Apple","Annona muricata, also called guanábana; a different species from sugar apple.",[],a="Guanábana")],
 ["Anona da Madeira PDO","Beed Custard Apple GI","Bà Đen GI"],["cherimoya","sugar apple","atemoya","soursop"]),
K("Feijoa","Fresh Acca sellowiana fruit, the pineapple guava.",W+"Feijoa_sellowiana",
 [x("Unique","","",W+"Feijoa_sellowiana","New Zealand feijoa tolerant of clay soils and self-pollinating."),
  x("Apollo","","",W+"Feijoa_sellowiana","Named feijoa cultivar.")],None,a="Pineapple guava"),
K("Physalis","Fresh Physalis peruviana, sold in its husk as Cape gooseberry or goldenberry.",W+"Physalis_peruviana",None,None,a="Cape gooseberry · Goldenberry · Uchuva · Aguaymanto"),
K("Tamarillo","Fresh tamarillo (Solanum betaceum), eaten as fruit.","https://en.wikipedia.org/wiki/Geographical_indications_in_India",
 [x("Red tamarillo","","",W+"Tamarillo","Tart red to purple tamarillo, preferred in European import markets.",[v("Naga Tree Tomato GI","","","Nagaland Indian GI, old data")]),
  x("Yellow tamarillo","","",W+"Tamarillo","Sweeter yellow to orange tamarillo, better suited to industrial use.")],None,a="Tree tomato"),
K("Pepino","Fresh Solanum muricatum fruit, tasting of honeydew and cucumber.","https://plufinder.com/plu/4333",None,["Pepino melon"],a="Pepino dulce · Melon pear"),
K("Kiwano","Fresh horned melon (Cucumis metuliferus), orange spiked skin and lime-green jelly flesh.",W+"Cucumis_metuliferus",None,None,a="Horned melon · Jelly melon"),
K("Jamun","Fresh fruit of Syzygium cumini.","https://en.wikipedia.org/wiki/Geographical_indications_in_India",None,["Bahadoli Jamun GI","Badlapur Jamun GI"],a="Java plum · Black plum"),
K("Amla","Fresh Phyllanthus emblica fruit.","https://en.wikipedia.org/wiki/Geographical_indications_in_India",None,["Pratapgarh Aonla GI"],a="Indian gooseberry · Emblic"),
K("Karonda","Fresh fruit of Carissa carandas.","https://en.wikipedia.org/wiki/Geographical_indications_in_India",None,["Chiraigaon Karonda of Varanasi GI"],a="Bengal currant · Carandas plum"),
]
notes="Feijoa, Physalis and Kiwano added as new kinds as planned. Physalis and Kiwano have no cultivars on retrieved pages, so kind level only. Campas, Bronceada, African Pride, Rothamer not confirmed. Custard apple is organised by type (cherimoya, atemoya, sugar apple, soursop); Annona species names from Wikipedia Custard apple page. Jamun, amla and karonda: cultivar pages not available, GIs kept flat."
sub=lambda p: W+p
urls=[W+p for p in ["Cherimoya","Atemoya","Custard_Apple","Feijoa_sellowiana","Physalis_peruviana","Tamarillo","Solanum_muricatum","Cucumis_metuliferus","Syzygium_cumini","Phyllanthus_emblica","Carissa_carandas"]]
write("00_13",kinds,[],[],notes,urls)
