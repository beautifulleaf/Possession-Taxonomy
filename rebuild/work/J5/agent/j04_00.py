from lib import *
S=W+"Saffron"
kinds=[
{"n":"Saffron","a":"","d":"Dried stigmas of the saffron crocus, graded by which part of the thread is kept and by lab-tested colour strength.","t":["threads","powder","ISO 3632 category I / II / III"],"s":S,"m":[["Pure Norfolk Saffron Threads","Norfolk Saffron"]],
 "x":[
 X("Iranian sargol","all-red saffron","Red stigma tips only, the strongest Iranian grade; typically ISO category I.",S,[V("Sargol"),V("Negin (stigma without yellow style, sold as premium)","","","Trade name; not described on the retrieved page")][:1],"red tips only · threads or powder"),
 X("Iranian pushal","pushali","Red stigmas with some yellow style attached; lower strength than sargol.",S,[V("Pushal"),V("Bunch","","","Red stigma with much yellow style, tied in a small bundle")],"stigma plus style"),
 X("Spanish coupé and mancha","Spanish grades","Spanish grading ladder: coupé (comparable to sargol), mancha (comparable to pushal), then rio, standard, sierra.",S,[V("Coupé"),V("Mancha"),V("Rio"),V("Standard"),V("Sierra")],"strength ladder"),
 X("Azafrán de La Mancha","La Mancha saffron","Spanish saffron from Castilla-La Mancha with protected designation of origin.",S,[],"whole stigmas · current-year harvest",y="PDO"),
 X("Krokos Kozanis","Greek saffron","Greek saffron from the Kozani region, protected designation of origin.","https://agriculture.ec.europa.eu/farming/geographical-indications-and-quality-schemes/geographical-indications-food-and-drink/krokos-kozanis-pdo_it",[],"Kozani region only",y="PDO"),
 X("Kashmir saffron","Kashmiri saffron","Saffron from the Kashmir Valley (Pampore area), given a Government of India geographical indication in 2020.",S,[V("Mongra","","","Stigma alone"),V("Lachha","","","Stigmas with parts of the style"),V("Guchhi")],"mongra · lachha",y="GI 2020"),
 X("Zafferano dell'Aquila","L'Aquila saffron","Premium saffron of the Navelli Valley, Abruzzo; the retrieved page does not state its protection status.",S,[],"Navelli Valley, Abruzzo"),
 ]},
{"n":"Vanilla","a":"vanilla beans · vanilla extract","d":"Cured pods of vanilla orchids, sold as beans, extract, paste or powder and named by growing region.","t":["whole beans","extract","bean paste","powder","seeds"],"s":W+"Vanilla","m":[["Madagascar Bourbon Pure Vanilla Bean Paste","Nielsen-Massey"]],
 "x":[
 X("Bourbon-Madagascar vanilla","Madagascar vanilla","V. planifolia beans from Madagascar, the Comoros, Mauritius and Réunion (formerly Île Bourbon); the standard vanilla taste.",W+"Vanilla",[V("Madagascar Bourbon"),V("Réunion"),V("Comoros")],"grade by length and moisture · gourmet vs extract beans"),
 X("Mexican vanilla","","V. planifolia from its native Mexico, produced in much smaller quantities.",W+"Vanilla",[],"beans · extract"),
 X("Tahitian vanilla","Vanilla tahitensis","Floral-fruity vanilla of French Polynesia from the hybrid Vanilla × tahitensis; under 1% of world production.",W+"Vanilla_%C3%97_tahitensis",[V("Tahitensis","","1848","Founding stock brought to Tahiti by Admiral Hamelin in 1848")],"beans · extract"),
 X("West Indian vanilla","Vanilla pompona","Vanilla from V. pompona grown in the Caribbean, Central and South America.",W+"Vanilla",[],"beans"),
 X("Indonesian vanilla","","V. planifolia from Indonesia, the second-largest producer after Madagascar (about 25% of 2023 output).",W+"Vanilla",[],"beans"),
 ]},
{"n":"Black pepper and peppercorns","a":"peppercorns · pepper","d":"Dried fruit of Piper nigrum, sold whole or ground by origin and by colour, which depends on processing.","t":["black (unripe fruit cooked and dried)","white (ripe seed, skin removed)","green (colour-preserved unripe)","red (ripe, brined or dried)","pink peppercorns are not true pepper (Schinus berries)"],"s":W+"Black_pepper",
 "x":[
 X("Malabar pepper","Malabar black pepper","Pepper from Kerala's Malabar coast, graded garbled or ungarbled; Geographical Indication 2007-08.",W+"Malabar_pepper",[V("Garbled","","","Nearly round, black, wrinkled"),V("Ungarbled","","","Dark brown to black")],"garbled · ungarbled"),
 X("Kampot pepper","Poivre de Kampot","Cambodian pepper from Kampot and Kep; GI in Cambodia 2010 and EU PGI 2016; black, white, red and green.",W+"Kampot_pepper",[V("Small-leaf kamchay"),V("Big-leaf lampong")],"black · white · red · green",y="PGI 2016"),
 X("Penja pepper","Poivre de Penja","Cameroon pepper from the Penja valley's volcanic soil; EU PGI; black, white, red, green.",W+"Penja_pepper",[],"black · white · red · green",y="PGI"),
 ]},
{"n":"Sichuan pepper","a":"huajiao · Szechuan pepper","d":"Dried husks of Zanthoxylum fruit with a tingling, numbing effect, red or green.","t":["red (Z. bungeanum)","green (Z. schinifolium / armatum)","whole husks","ground"],"s":W+"Sichuan_pepper","m":[]},
{"n":"Cinnamon","a":"cassia","d":"Dried cinnamon or cassia bark, whole or ground, in several species with different flavour and coumarin levels.","t":["quills","ground","chips"],"s":W+"Cinnamon","m":[],
 "x":[
 X("Ceylon cinnamon","true cinnamon · Cinnamomum verum","Thin, many-layered inner bark from Sri Lanka; subtle, with only trace coumarin.",W+"Cinnamon",[V("Alba","","","Quills under 6 mm"),V("Continental","","","Under 16 mm"),V("Mexican","","","Under 19 mm"),V("Hamburg","","","Under 32 mm")],"quill grade by diameter"),
 X("Cassia (Chinese cinnamon)","Cinnamomum cassia","Thick, hard, reddish-brown bark with a strong flavour; the commonest type in the USA.",W+"Cinnamon",[],"sticks · ground"),
 X("Korintje cinnamon","Indonesian cinnamon · Padang cassia","Cinnamomum burmanni, sold as neat single-layer quills, hard enough to harm a grinder.",W+"Cinnamon",[],"quills · ground"),
 X("Saigon cinnamon","Vietnamese cassia","Cinnamomum loureiroi from Vietnam; broken thick bark with a pronounced, complex aroma and high coumarin.",W+"Saigon_cinnamon",[],"broken bark · ground"),
 ]},
{"n":"Cardamom","a":"green cardamom · black cardamom","d":"Seed pods of Elettaria (green) or Amomum (black) used whole or ground.","t":["green","white (bleached)","black (smoky, larger)","pods","seeds"],"s":W+"Cardamom",
 "x":[X("Alleppey green cardamom","","Light-green capsules from southern Kerala and Tamil Nadu; Geographical Indication 2007-08.",W+"Alleppey_green_cardamom",[],"graded by size, weight, colour and aroma",y="GI 2007-08"),
      X("Black cardamom","brown cardamom · Nepal cardamom","Amomum subulatum pods from the eastern Himalayas; dark brown, smoky with cooling mint notes.",W+"Cardamom",[],"whole pods")]},
{"n":"Nutmeg and mace","a":"","d":"Seed (nutmeg) and red aril (mace) of Myristica fragrans, sold whole or ground.","t":["whole nutmeg","ground nutmeg","blade mace","ground mace"],"s":W+"Nutmeg",
 "x":[X("Banda nutmeg","Indonesian nutmeg","Nutmeg and mace from the Banda Islands, the tree's home and sole world source until the mid-19th century.",W+"Nutmeg",[],"whole · mace blades"),
      X("Grenada nutmeg","","Nutmeg grown on Grenada, where British traders transplanted trees; a leading export and a symbol on the national flag.",W+"Nutmeg",[],"whole · mace")]},
{"n":"Cloves","a":"","d":"Dried flower buds of Syzygium aromaticum, sold whole or ground.","t":["whole","ground"],"s":W+"Clove","m":[]},
{"n":"Star anise","a":"badian","d":"Star-shaped fruit of Illicium verum, from China and Vietnam, used whole in broths and blends.","t":["whole stars","ground"],"s":W+"Illicium_verum","m":[]},
{"n":"Paprika","a":"pimentón","d":"Ground dried paprika peppers, sweet, hot or smoked.","t":["sweet","hot","smoked","unsmoked"],"s":W+"Paprika","m":[["La Dalia Pimentón de la Vera Picante","La Dalia"]],
 "x":[X("Pimentón de la Vera","smoked Spanish paprika","Spanish paprika dried over oak smoke, with Denomination of Origin; sold dulce and picante.",W+"Paprika",[V("Dulce"),V("Agridulce"),V("Picante")][:1]+[V("Picante")],"sweet · hot · smoked",y="DOP"),
      X("Pimentón de Murcia","","Unsmoked Spanish paprika from bola/ñora peppers.",W+"Paprika",[],"sun or kiln dried"),
      X("Hungarian paprika","Kalocsa and Szeged paprika","Hungarian ground paprika from Kalocsa and Szeged, graded from különleges to erős.",W+"Paprika",[V("Különleges"),V("Édesnemes"),V("Félédes"),V("Rózsa"),V("Erős")],"five commercial grades")]},
{"n":"Dried chilli","a":"chili · chile","d":"Dried chillies, whole, flaked or ground, sold by named variety.","t":["whole","flakes","ground"],"s":W+"Kashmiri_red_chilli","m":[["Kashmiri chili powder",""]],
 "x":[
 X("Kashmiri chilli","Kashmiri mirch","Mild Capsicum annuum (1,000-2,000 SHU) prized in Indian cooking for its deep red colour.",W+"Kashmiri_red_chilli",[],"whole · powder"),
 X("Aleppo pepper","pul biber · Halep biberi","Moderately hot (about 10,000 SHU) Syrian and Turkish flakes, partly dried, deseeded and crushed.",W+"Aleppo_pepper",[],"flakes"),
 X("Piment d'Espelette","Espelette pepper","Gorria variety of Capsicum annuum from the Basque Country; AOC 2000, AOP 2002; mild to about 4,000 SHU.",W+"Espelette_pepper",[],"powder · festoons · purée",y="AOP 2002"),
 X("Ancho","chile ancho","Dried poblano, wide and mild.",W+"Poblano",[],"whole pods · ground"),
 X("Guajillo","","Dried form of the mirasol chilli.",W+"Chipotle",[],"whole pods · ground"),
 X("Chipotle","chipotle meco","Smoke-dried ripe jalapeño, 2,500-8,000 SHU; sold dried, ground or canned in adobo.",W+"Chipotle",[],"whole · ground · in adobo"),
 X("Gochugaru","Korean chili flakes","Seedless Korean red pepper flakes or powder, spicy, sweet and slightly smoky; Cheongyang types are finer and hotter.",W+"Korean_chili_pepper",[],"flakes · fine powder"),
 ]},
]
# clean up leftover hacks
for k in kinds:
    for x in k.get("x",[]):
        pass
kinds[0]["x"][0]["v"]=[V("Sargol")]
kinds[9]["x"][0]["v"]=[V("Dulce"),V("Picante")]
brands=[{"n":"Nielsen-Massey","c":"United States","f":"1907","seg":"Premium","kf":"vanilla","d":"Illinois maker of pure vanilla extracts, pastes and powders from Madagascar, Mexico and Tahiti.","lines":["Madagascar Bourbon","Tahitian","Mexican"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"knowledge"}]
notes="Dropped nothing. Negin grade omitted (not on retrieved pages). Zafferano dell'Aquila DOP status and Szegedi paprika PDO not confirmed on retrieved pages so stated without protection claim. Hanyuan, Lampong/Sarawak/Tellicherry, Heilala not confirmed. No traditions added."
write("04_00",kinds,brands,[],notes)
