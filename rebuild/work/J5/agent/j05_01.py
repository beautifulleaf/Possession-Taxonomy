from lib import *
def B(n,c,f,kf,d,s,seg="Mainstream",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
H=W+"Hot_sauce"
kinds=[
{"n":"Hot sauce","a":"chilli sauce","d":"Pourable table sauce of chillies with vinegar or salt, fermented or not, in regional styles.","t":["fermented","vinegar-based","fruit-based","extract/superhot"],"s":H,"m":[],
 "x":[
 X("Tabasco","Tabasco brand pepper sauce","The McIlhenny Company's Louisiana sauce of aged tabasco peppers and vinegar, created in 1868 on Avery Island.",W+"Tabasco_sauce",[V("Original red","Tabasco","1868"),V("Habanero","Tabasco"),V("Jalapeño","Tabasco"),V("Chipotle","Tabasco"),V("Sriracha","Tabasco"),V("Scorpion","Tabasco","","Hottest in the range")],"red pepper · vinegar · aged",mk="Tabasco",y="1868"),
 X("Frank's RedHot","Frank's","Louisiana-style cayenne sauce from 1920, the classic base for Buffalo wing sauce; owned by McCormick since 2017.",W+"Frank's_RedHot",[V("Original","Frank's RedHot","1920","About 450 SHU"),V("XTRA Hot","Frank's RedHot","","About 2,000 SHU")],"cayenne · vinegar",mk="Frank's RedHot",y="1920"),
 X("Crystal Hot Sauce","Crystal","Louisiana sauce of aged cayenne, vinegar and salt, made by family-owned Baumer Foods since 1923.",W+"Crystal_Hot_Sauce",[],"cayenne · medium heat",mk="Crystal",y="1923"),
 X("Louisiana Hot Sauce","The Original Louisiana Brand","Louisiana-style sauce first marketed in 1928 and made in New Iberia, Louisiana.",W+"Louisiana_Hot_Sauce",[],"aged peppers",y="1928"),
 X("Cholula","","Mexican sauce of piquín and árbol chillies from Chapala, Jalisco, sold in the US since 1989; owned by McCormick.",W+"Cholula_Hot_Sauce",[V("Original","Cholula"),V("Chipotle","Cholula"),V("Chili Garlic","Cholula"),V("Chili Lime","Cholula"),V("Green Pepper","Cholula"),V("Sweet Habanero","Cholula")],"piquín · árbol",mk="Cholula",y="1989 US launch"),
 X("Valentina","Salsa Valentina","Thick, less vinegary Mexican sauce from Salsa Tamazula, Guadalajara, introduced in 1954.",W+"Valentina_(hot_sauce)",[V("Hot","Valentina","","About 900 SHU"),V("Extra Hot","Valentina","","About 2,100 SHU")],"thick · chilli flavour",mk="Valentina",y="1954"),
 X("Tapatío","","Californian hot sauce founded in 1971 by Jose-Luis Saavedra Sr. and popular with Mexican-American communities.",W+"Tapat%C3%ADo_hot_sauce",[],"Vernon, California",mk="Tapatío",y="1971"),
 X("El Yucateco","","Habanero sauce range from Mérida, Yucatán, founded 1968.",W+"El_Yucateco",[V("Black Label Reserve","El Yucateco","","4,500-5,500 SHU, the mildest habanero"),V("Ghost Habanero","El Yucateco","","About 14,165 SHU, the hottest")],"habanero",mk="El Yucateco",y="1968"),
 X("Sriracha","","Chilli-garlic sauce named after Si Racha, Thailand: Sriraja Panich from 1935 and the Californian Huy Fong 'rooster sauce' from 1980.",W+"Sriracha",[V("Sriraja Panich","","1935","Thai original, owned by Thai Theparos since 1984"),V("Huy Fong sriracha","Huy Fong Foods","1980","Jalapeño-based rooster sauce")],"red chilli · garlic · sugar"),
 X("Marie Sharp's","Belizean habanero sauces","Fruit and vegetable based habanero sauces from Stann Creek District, Belize; selling since 1981.",W+"Marie_Sharp's",[],"habanero · carrot · fruit",mk="Marie Sharp's",y="1981"),
 X("Peri-peri sauce","piri piri","Portuguese-world sauce of African bird's eye chilli, garlic and oil or acid, made known in the UK by Nando's (founded 1987).",W+"Piri_piri",[],"piri piri chilli"),
 X("The Last Dab","Hot Ones sauce","Superhot sauce made with Hot Ones as the show's final wing sauce, rated above 2,000,000 SHU; renamed over the seasons.",W+"Hot_Ones",[V("The Last Dab Reduxx","","","Season 6"),V("The Last Dab XXX","","","Season 10"),V("The Last Dab Apollo","","","Season 13"),V("The Last Dab Xperience","","","Season 22")],"extract-level heat",y="2015 show")]},
{"n":"Chilli oil and chilli crisp","a":"chili crunch · lajiao","d":"Oil infused with chilli, with or without crunchy solids such as fried garlic, onion or soybeans.","t":["clear chilli oil","chilli crisp","rāyu","salsa macha","olio di peperoncino"],"s":W+"Chili_crisp","m":[["Fly By Jing Sichuan Chili Crisp","Fly By Jing"],["Lao Gan Ma Spicy Chilli Crisp","Lao Gan Ma"]],
 "x":[X("Lao Gan Ma chilli crisp","Laoganma","Guizhou-style chilli crisp made commercially since 1997 by Tao Huabi; the largest chilli crisp company.",W+"Lao_Gan_Ma",[V("Spicy Chili Crisp","Lao Gan Ma"),V("Chili Oil with Black Bean","Lao Gan Ma"),V("Fried Chili in Oil","Lao Gan Ma"),V("Hot Chili Sauce","Lao Gan Ma"),V("Spicy Bean Paste","Lao Gan Ma")],"Guizhou crisps",mk="Lao Gan Ma",y="1997"),
      X("Fly By Jing chilli crisp","","American-founded Sichuan chilli crisp by Jing Gao, launched via Kickstarter in 2018.",W+"Fly_By_Jing",[V("Sichuan Chili Crisp","Fly By Jing")],"Sichuan",mk="Fly By Jing",y="2018")]},
{"n":"Chilli paste","a":"nam prik pao · sambal · harissa","d":"Unfermented paste of chillies, roasted or raw, with oil, garlic or spices. Fermented gochujang has its own entry.","t":["raw","roasted","sweet"],"s":W+"Sambal","m":[],
 "x":[X("Harissa","Tunisian harissa","Tunisian paste of roasted red and Baklouti peppers with garlic, caraway, coriander, cumin and olive oil; listed by UNESCO in 2022.",W+"Harissa",[],"Baklouti pepper · olive oil",y="UNESCO 2022"),
      X("Sambal oelek","sambal ulek","Plain raw chilli paste that is the base of other sambals; the most popular jarred sambal in the Netherlands.",W+"Sambal",[],"raw chilli"),
      X("Nam phrik phao","Thai roasted chilli paste","Sweet Thai paste of roasted chillies and tamarind with sugar, used in tom yum and as a spread.",W+"Nam_phrik",[],"roasted chilli · tamarind"),
      X("Zhug","sahawiq · skhug","Yemeni hot sauce of fresh chillies, coriander, garlic and olive oil; red, green and brown (with tomato) forms in Israel.",W+"Zhug",[V("Red zhug (skhug adom)"),V("Green zhug (skhug yarok)"),V("Brown zhug (skhug khum)")],"fresh chilli · herbs")]},
{"n":"Sweet chilli sauce","a":"nam chim kai","d":"Thick sweet sauce of chilli, sugar, garlic and vinegar in the Thai style.","t":["dipping","with fish sauce"],"s":W+"Sweet_chili_sauce","m":[]},
{"n":"Salsa","a":"","d":"Mexican table sauces, raw or cooked, sold jarred as red (roja), green (verde) and chunky salsas.","t":["salsa roja","salsa verde","pico de gallo","chunky","fruit"],"s":W+"Salsa_(food)","m":[["Pace Picante Sauce","Pace"]]},
]
brands=[
B("Tabasco","United States","1868","Louisiana pepper sauce","Edmund McIlhenny's sauce made by the McIlhenny Company on Avery Island, Louisiana.",W+"Tabasco_sauce",seg="Heritage manufactory",sig=["Tabasco"]),
B("Frank's RedHot","United States","1920","Buffalo wing base","Louisiana-style cayenne sauce first sold in 1920; owned by McCormick since 2017.",W+"Frank's_RedHot",sig=["Frank's RedHot"]),
B("Crystal","United States","1923","Louisiana sauce","Hot sauce made by family-owned Baumer Foods.",W+"Crystal_Hot_Sauce",sig=["Crystal Hot Sauce"]),
B("Cholula","Mexico","","Mexican hot sauce","Sauce from Chapala, Jalisco, owned by McCormick since 2020.",W+"Cholula_Hot_Sauce",sig=["Cholula"]),
B("Valentina","Mexico","1954","Mexican hot sauce","Sauce from Salsa Tamazula of Guadalajara.",W+"Valentina_(hot_sauce)",sig=["Valentina"]),
B("Tapatío","United States","1971","Californian hot sauce","Vernon, California sauce founded by Jose-Luis Saavedra Sr.",W+"Tapat%C3%ADo_hot_sauce",sig=["Tapatío"]),
B("El Yucateco","Mexico","1968","habanero sauce","Mérida, Yucatán maker of habanero sauces.",W+"El_Yucateco",sig=["El Yucateco"]),
B("Huy Fong Foods","United States","1980","sriracha","Los Angeles company founded by David Tran; maker of the rooster-label sriracha.",W+"Huy_Fong_Foods",sig=["Huy Fong sriracha"]),
B("Marie Sharp's","Belize","1981","habanero sauce","Belizean maker of habanero hot sauces and preserves from Stann Creek District.",W+"Marie_Sharp's",seg="Artisan & independent"),
B("Lao Gan Ma","China","1997","chilli crisp","Guizhou brand of Tao Huabi, the largest chilli crisp company.",W+"Lao_Gan_Ma",sig=["Spicy Chili Crisp"]),
B("Fly By Jing","United States","2018","Sichuan chilli crisp","Brand founded by Jing Gao; started via Kickstarter in 2018.",W+"Fly_By_Jing",seg="Artisan & independent"),
B("Pace","United States","1947","picante sauce","San Antonio brand founded by David Pace; owned by Campbell's since 1995.",W+"Pace_Foods"),
]
notes="Encona, Yellowbird, Secret Aardvark not found on retrieved pages so omitted; Sriraja Panich is a version (no brand register entry as no maker page). Nando's not given a register entry. Sweet chilli sauce has no maker models (Mae Ploy not confirmed). Harissa gets UNESCO year from the Harissa page; no tradition entry."
write("05_01",kinds,brands,[],notes)
