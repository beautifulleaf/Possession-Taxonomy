from lib import *
kinds=[
{"n":"Dried mushrooms","a":"","d":"Dried edible fungi: porcini, shiitake, morels and wood ear, rehydrated before cooking.","t":["whole","sliced","powder"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/dried-shiitake-mushrooms","m":[["Tangxiu Dried Shiitake","Tangxiu"]],
 "x":[
 X("Dried porcini","cep · Boletus edulis","Dried king bolete, flavour intensifies on drying; soak in hot water for about 20 minutes and keep the liquor. Fungo di Borgotaro has PGI for four Boletus species.",W+"Boletus_edulis",[V("Fungo di Borgotaro IGP","","","PGI covering B. edulis, aereus, aestivalis and pinophilus; much 'Italian' porcini is imported")],"whole slices · soaking liquor",y="PGI"),
 X("Dried shiitake","donko · huagu","Japanese and Chinese dried shiitake; donko (winter mushroom) is a high grade and huagu (flower mushroom) the most prized, grown in cooler temperatures.",W+"Shiitake",[V("Donko"),V("Huagu (flower mushroom)")],"cap cracking pattern · grade"),
 X("Dried morels","","Morels dried by hanging threaded caps in the sun; blanching is advised before cooking.",W+"Morchella_esculenta",[],"sun-dried caps"),
 X("Wood ear","black fungus · cloud ear","Chinese dried fungi sold shredded or whole, valued for texture; main species Auricularia heimuer and A. cornea.",W+"Wood_ear",[V("Auricularia heimuer"),V("Auricularia cornea","","","Hairy wood ear, coarser")],"rehydrates for texture"),
 ]},
{"n":"Dried seaweed","a":"","d":"Dried edible seaweed; fresh seaweed is in Fruit & Vegetables.","t":["sheets","flakes","strips"],"s":"https://www.joybuy.de/blog/buy-dried-seaweed-tips/1pnQVizL","m":[["Yutaka Dried Wakame","Yutaka"]],
 "x":[
 X("Nori","laver","Dried red alga (Pyropia) pressed into sheets of about 18 × 20 cm; the top grade is first-harvest shin-nori from the Ariake Sea.",W+"Nori",[V("Shin-nori (Ariake)","","","First harvest, the priciest"),V("Iwanori","","","Wild rock-harvested, rougher")],"sheets · grade by harvest"),
 X("Wakame","","Brown kelp Undaria pinnatifida used in Japan and Korea, sold as dried leaves.",W+"Edible_seaweed",[],"dried leaves"),
 X("Hijiki","","Brown alga Sargassum fusiforme sold dried.",W+"Edible_seaweed",[],"dried"),
 X("Dulse","","Red alga Palmaria palmata eaten dried as flakes or leaves, a source of iodine and protein.",W+"Edible_seaweed",[],"flakes · leaves"),
 X("Kombu","kelp","Kelp Saccharina japonica; dried kombu for stock is covered with its varieties under Dashi and dashi ingredients.",W+"Edible_seaweed",[],"cross-link: dashi"),
 ]},
{"n":"Sun-dried tomatoes","a":"","d":"Tomatoes dried in the sun or by machine, sold dry or packed in sunflower or olive oil.","t":["dry","oil-packed","paste or purée"],"s":W+"Sun-dried_tomato"},
]
notes="Koshin grade, morel and hijiki grades not on retrieved pages (koshin omitted; hijiki and Wakame (Naruto) origin not confirmed so no origin claim). Kombu is cross-linked to the dashi kind on shelf 05_02. No brands in register (Tangxiu, Yutaka are old-data models only). Dried mushroom and seaweed old sources kept."
write("07_01",kinds,[],[],notes)
