import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":q[0],"mk":(q[3] if len(q)>3 else mk),"y":q[1],"d":q[2]} for q in v],"dt":dt}
SW=["regular (sugar or HFCS)","cane-sugar","diet / zero sugar","caffeine-free","glass bottle","can","PET bottle","fountain syrup"]
kinds=[
{"n":"Cola","a":"coke · pop · soda","d":"Dark caramel-coloured soda flavoured with vanilla, cinnamon and citrus oils, named after the caffeine-bearing kola nut.","t":SW+["clear cola","flavoured (cherry, vanilla, lime)"],"s":W+"Cola","x":[
 X("Coca-Cola","The original cola, created by pharmacist John Stith Pemberton and first sold at Jacob's Pharmacy, Atlanta.","Coca-Cola","1886",W+"Coca-Cola",
   [("Contour bottle","1915","Earl R. Dean and Harold Hirsch, Root Glass Co."),("Diet Coke","1982",""),("Caffeine-Free Coca-Cola","1983",""),("New Coke","1985","withdrawn; original returned as Coca-Cola Classic"),("Cherry Coke","1985",""),("Vanilla Coke","2002",""),("Coca-Cola Zero (Zero Sugar)","2005",""),("Coca-Cola Life","2014","stevia blend; discontinued"),("Mexican Coke","","cane sugar, glass bottle"),("Kosher for Passover","","yellow cap")],"contour glass, can, PET · regular, diet, zero, flavours",a="Coke"),
 X("Pepsi","Cola created by Caleb Bradham at his New Bern, North Carolina drugstore as 'Brad's Drink', renamed Pepsi-Cola in 1898.","Pepsi","1893",W+"Pepsi",
   [("Diet Pepsi","1964",""),("Pepsi Wild Cherry","1970s",""),("Caffeine-Free Pepsi","1982",""),("Pepsi Max","1993",""),("Crystal Pepsi","","clear cola"),("Pepsi Zero Sugar","",""),("Pepsi Made with Real Sugar","",""),("Nitro Pepsi","",""),("Pepsi Perfect","2015","limited edition")],"can, PET, glass · regular, diet, max, flavours",a="Pepsi-Cola"),
 X("RC Cola","Royal Crown cola from Columbus, Georgia; first soft drinks in tin cans (1954) and maker of Diet Rite, the first diet cola.","Royal Crown","1934",W+"RC_Cola",
   [("Diet Rite","1954","first diet cola")],"",a="Royal Crown Cola"),
 X("Thums Up","Indian cola, fizzier and spicier than Coca-Cola, created by the Chauhan brothers of Parle.","Thums Up","1977",W+"Thums_Up",
   [("250 ml bottle","1977","original"),("MahaCola 300 ml bottle","","after the 1991 market opening")],""),
 X("Kofola","Czechoslovak herbal cola made from Kofo syrup of 14 herbal and fruit ingredients, created in Prague.","Kofola","1960",W+"Kofola",
   [("Original","",""),("Citrus","",""),("Vanilla","","")],"glass, PET, can, draught"),
 X("Fritz-kola","Hamburg craft cola with high caffeine (about 25 mg/100 ml), sold in glass bottles.","Fritz-kola","2003",W+"Fritz-kola",
   [("Fritz-kola sugar-free","",""),("mischmasch","","kola-orange")],"glass bottles"),
 X("Curiosity Cola","Botanically brewed craft cola from Fentimans of Hexham.","Fentimans","",W+"Fentimans",[],"glass bottles"),
 ],"m":[["Inca Kola","Inca Kola"],["Afri-Cola","Afri-Cola"],["Breizh Cola","Breizh Cola"],["Bec Cola","Bec Cola"],["Zevia","Zevia"],["Kola Román","Kola Román"]]},
{"n":"Pepper & spiced soda","a":"pepper-type soda · Dr Pepper-style","d":"Dark, spiced, fruity soda in the Dr Pepper style, distinct from cola.","t":SW+["cherry","cherry vanilla"],"s":W+"Dr_Pepper","x":[
 X("Dr Pepper","Spiced soda created by pharmacist Charles Alderton at Morrison's Old Corner Drug Store, Waco, Texas.","Dr Pepper","1885",W+"Dr_Pepper",
   [("Diet Dr Pepper","1962",""),("Caffeine Free Dr Pepper","1983",""),("Dr Pepper Cherry Vanilla","2004",""),("Dr Pepper Cherry","2009",""),("Heritage Dr Pepper","2009","sugar-sweetened"),("Dr Pepper Made with Real Sugar","2010",""),("Dr Pepper Ten","2011","discontinued 2018"),("Dr Pepper Zero Sugar","2021",""),("Dublin Dr Pepper","","discontinued")],""),
 X("Mr. Pibb","Coca-Cola's pepper-type soda, launched as Peppo in Memphis and renamed Pibb Xtra in 2001; name restored 2025.","Coca-Cola","1972",W+"Pibb_Xtra",
   [("Peppo","1972","original name"),("Pibb Xtra","2001","spicy cherry"),("Mr. Pibb relaunch","2025","more caffeine")],"",a="Pibb Xtra · Peppo"),
 ]},
{"n":"Lemon-lime soda","a":"lemonade (UK usage) · clear soda","d":"Clear, caffeine-free carbonated soft drink flavoured with lemon and lime.","t":SW+["cherry","cranberry"],"s":W+"7_Up","x":[
 X("7 Up","Lemon-lime soda developed by Charles Leiper Grigg of the Howdy Corporation, St. Louis.","7 Up","1928",W+"7_Up",
   [("SEVEN-UP","1928","original name"),("7up Lithiated Lemon Soda","1930","renamed 7 Up 1937"),("Like (Diet 7 Up)","1963","relaunched as Diet 7 Up 1970, 7 Up Zero Sugar 2020"),("Cherry 7 Up","1987",""),("7 Up Free","2005","UK, ex-7 Up Light")],"",a="7UP · Seven Up"),
 X("Sprite","Coca-Cola's lemon-lime soda, developed in West Germany as Fanta Klare Zitrone and launched in the US in 1961.","Coca-Cola","1959",W+"Sprite_(drink)",
   [("Fanta Klare Zitrone","1959","West Germany"),("Sprite (US)","1961",""),("Sugar Free Sprite / Sprite Zero Sugar","1974","renamed 1983, 2004, 2006, 2019"),("Sprite Remix","2003","Tropical; BerryClear 2004; Aruba Jam 2005"),("Sprite Cranberry","2013","seasonal"),("Clear bottle","2022","green bottle dropped")],""),
 ]},
{"n":"Citrus soda","a":"citrus pop · yellow soda","d":"Caffeinated, sharply sweet citrus-flavoured soda, often neon yellow-green.","t":SW+["cherry","tropical lime"],"s":W+"Mountain_Dew","x":[
 X("Mountain Dew","Citrus soda created by Knoxville bottlers Barney and Ally Hartman; reformulated in 1958, owned by PepsiCo since 1964.","Mountain Dew","1940s",W+"Mountain_Dew",
   [("Bill Bridgforth formula","1958","Johnson City, Tennessee"),("Diet Mountain Dew","1988",""),("Code Red","2001","cherry"),("Voltage","2008","DEWmocracy winner"),("Throwback","2009","sugar-sweetened"),("Baja Blast","2014","retail; originally Taco Bell exclusive"),("Kickstart","","")],"",a="Mtn Dew"),
 ],"m":[["Mello Yello","Coca-Cola"],["Surge","Coca-Cola"],["Sun Drop","Keurig Dr Pepper"]]},
{"n":"Orange soda","a":"orangeade · aranciata · orange pop","d":"Carbonated orange-flavoured soft drink, with or without real orange juice or pulp.","t":SW+["with juice","with pulp","blood orange"],"s":W+"Fanta","x":[
 X("Orange Crush","Orange soda created by chemist Neil C. Ward, originally sold with added orange pulp.","Crush","1911",W+"Crush_(soft_drink)",
   [("Ward's Orange-Crush","1911","with pulp"),("Diet Orange","","")],"",a="Crush"),
 X("Orangina","Lightly sparkling orange and citrus drink with pulp, in a round textured bottle; invented in Spain as Naranjina.","Orangina","1935",W+"Orangina",
   [("Round textured 250 ml bottle","1951","Jean-Claude Beton"),("Orelia","1978","US name until 1985"),("Orangina Rouge","",""),("Orangina Sanguine","","blood orange"),("Miss O","2010s","sugar-free")],"25 cl glass bottle · shake before opening"),
 X("Fanta Orange","Coca-Cola's orange soda, developed in Naples in 1955; Fanta itself began in wartime Germany under Max Keith.","Fanta","1955",W+"Fanta",
   [("Wartime German Fanta","1941","whey and apple pomace; ended 1949"),("Fanta Klassik","2015","Germany, wartime-style recipe"),("Fanta Orange No Sugar","","South Africa")],"real orange juice outside US"),
 X("Aranciata","Italian orangeade from Sanpellegrino.","Sanpellegrino","1932",W+"Sanpellegrino",[("Aranciata Rossa","","blood orange")],"cans, glass"),
 ]},
{"n":"Fruit soda","a":"fruit pop · flavoured soda","d":"Sweet carbonated soft drink flavoured with grape, strawberry, pineapple, tropical or other fruit.","t":SW+["grape","strawberry","pineapple","peach","tropical","apple"],"s":W+"Grape_soda","x":[
 X("Grape soda","Deep purple, Concord-grape-flavoured soda, sold at US soda fountains as grapeade from the late 1800s.","","late 1800s",W+"Grape_soda",
   [("Fanta Grape","","",'Fanta'),("Crush Grape","","",'Crush'),("Grapette","","",'Grapette'),("NuGrape","","",'NuGrape'),("Grapico","","",'Grapico')],"methyl anthranilate flavour · purple",a="grapeade · purple drink"),
 X("Crush fruit flavours","Crush's fruit soda range beyond orange.","Crush","",W+"Crush_(soft_drink)",
   [("Grape","",""),("Strawberry","",""),("Peach","",""),("Pineapple","","originally Newfoundland only"),("Cherry","2009","")],""),
 X("Fanta flavours","Fanta's range of over 200 fruit flavours worldwide, many regional.","Fanta","",W+"Fanta",
   [("Fanta Calamansi","1994","Philippines"),("Fanta Exotic","","Scandinavia"),("Fanta Shokata","","elderflower"),("Fanta Pineapple and Grapefruit","2023","UK, ex-Lilt"),("Brazilian regional flavours","2010","guaraná, passion fruit, cashew")],""),
 ]},
{"n":"Root beer & birch beer","a":"root beer · birch beer · sarsaparilla","d":"Sweet, foamy North American soda flavoured with sassafras, sarsaparilla or birch bark extract, usually caffeine-free.","t":SW+["red, brown or clear (white) birch beer"],"s":W+"Root_beer","x":[
 X("Hires Root Beer","The first commercial root beer, by Philadelphia pharmacist Charles Elmer Hires; now largely phased out.","Hires","1876",W+"Hires_Root_Beer",
   [("Powdered concentrate","1876",""),("Liquid extract and fountain syrup","1884",""),("Bottled root beer","1890",""),("Home brewing kits","1900s","to 1980s")],""),
 X("A&W Root Beer","Root beer from Roy W. Allen's roadside stand in Lodi, California.","A&W","1919",W+"A&W_Root_Beer",
   [("Sugar-Free","1974","Diet A&W 1987; A&W Zero Sugar 2020")],""),
 X("Barq's Root Beer","Sarsaparilla-based, caffeinated root beer from Edward Barq's Biloxi Artesian Bottling Works.","Barq's","1898",W+"Barq's",
   [("Diet / Zero Sugar","2022","renamed Zero Sugar")],"22.5 mg caffeine per 12 oz"),
 X("Birch beer","Root-beer-like soda flavoured with birch bark extract, typical of Pennsylvania, the Northeast US and Newfoundland.","","",W+"Birch_beer",
   [("White (clear) birch beer","",""),("Red birch beer","","Mid-Atlantic")],"brown, red, blue, clear"),
 ],"m":[["Mug Root Beer","Mug"],["IBC Root Beer","IBC"],["Dad's Root Beer","Dad's"],["Sprecher Root Beer","Sprecher"]]},
{"n":"Cream soda","a":"creme soda · creaming soda","d":"Sweet soda flavoured with vanilla or cream, clear, golden, pink, red or green by region.","t":SW+["vanilla (clear/golden)","red or pink","creaming soda (Australia, NZ)"],"s":W+"Cream_soda","x":[
 X("Vanilla cream soda","American clear or golden vanilla-flavoured soda; 'cream soda-water' was patented in 1865.","","1865",W+"Cream_soda",
   [("A&W Cream Soda","1986","",'A&W'),("Barq's French Vanilla Crème","","",'Barq\'s')],""),
 X("Red / pink cream soda","Red or pink cream soda, grenadine-like in Canada and raspberry-flavoured in Australia.","","",W+"Cream_soda",
   [("Barq's Red Crème Soda","","",'Barq\'s'),("Crush Cream Soda","","pink in Canada, clear in Québec",'Crush')],""),
 ]},
{"n":"Sparkling lemonade","a":"lemonade (UK) · clear lemonade · limonata · limonade","d":"Clear or cloudy carbonated lemon-flavoured drink, the usual meaning of 'lemonade' in Britain, Ireland and Australasia.","t":["clear","cloudy","red, brown or white (Ireland)","glass bottle","can","PET bottle"],"s":W+"Lemonade","x":[
 X("R. White's Lemonade","British clear lemonade, sold since 1845.","R. White's","1845",W+"Lemonade",[],""),
 X("Schweppes Lemonade","Clear lemonade from a blend of lemon and lime oils.","Schweppes","",W+"Lemonade",[],""),
 X("Limonata","Italian sparkling lemon drink from Sanpellegrino.","Sanpellegrino","",W+"Sanpellegrino",[],"cans, glass"),
 X("Victorian Lemonade","Botanically brewed cloudy lemonade from Fentimans; sister Rose Lemonade.","Fentimans","",W+"Fentimans",[("Rose Lemonade","","")],"glass bottles"),
 ],"m":[["Kirks Lemonade","Kirks"],["C&C Lemonade","C&C"],["Kelluke","Kelluke"]]},
]
def br(n,c,f,seg,d,sig,s='knowledge',rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 br("Coca-Cola","United States","1886","global soft drinks","The Coca-Cola Company, Atlanta, maker of Coca-Cola, Sprite, Fanta and Mr. Pibb.",["Coca-Cola","Sprite","Mr. Pibb"],W+"Coca-Cola",["Pepsi"]),
 br("Pepsi","United States","1893","global soft drinks","PepsiCo's flagship cola, also owner of Mountain Dew.",["Pepsi"],W+"Pepsi",["Coca-Cola"]),
 br("Royal Crown","United States","1905","cola","Columbus, Georgia maker of RC Cola and Diet Rite.",["RC Cola"],W+"RC_Cola"),
 br("Thums Up","India","1977","cola","Indian cola brand owned by Coca-Cola since 1993.",["Thums Up"],W+"Thums_Up"),
 br("Kofola","Czech Republic","1960","herbal cola","Czech-Slovak herbal cola, owned by the Samaras family's Kofola group.",["Kofola"],W+"Kofola"),
 br("Fritz-kola","Germany","2003","craft cola","Hamburg craft cola and lemonade maker.",["Fritz-kola"],W+"Fritz-kola"),
 br("Fentimans","United Kingdom","1905","botanically brewed soft drinks","Hexham maker of botanically brewed drinks, re-established 1988.",["Curiosity Cola","Victorian Lemonade"],W+"Fentimans"),
 br("Dr Pepper","United States","1885","pepper soda","Waco, Texas spiced soda, owned by Keurig Dr Pepper in North America.",["Dr Pepper"],W+"Dr_Pepper"),
 br("7 Up","United States","1928","lemon-lime soda","Lemon-lime soda owned by Keurig Dr Pepper in the US and PepsiCo elsewhere.",["7 Up"],W+"7_Up"),
 br("Mountain Dew","United States","1940s","citrus soda","PepsiCo citrus soda brand from Tennessee.",["Mountain Dew"],W+"Mountain_Dew"),
 br("Crush","United States","1911","fruit soda","Orange and fruit soda brand owned by Keurig Dr Pepper.",["Orange Crush"],W+"Crush_(soft_drink)"),
 br("Orangina","France","1935","orange soda","Pulpy orange soda invented in Spain, made in France, owned by Suntory since 2009.",["Orangina"],W+"Orangina"),
 br("Fanta","Germany","1940","fruit soda","Coca-Cola's fruit-soda brand with over 200 flavours worldwide.",["Fanta Orange"],W+"Fanta"),
 br("Sanpellegrino","Italy","1899","mineral water and sodas","Nestlé-owned maker of S.Pellegrino water and Italian sodas.",["Aranciata","Limonata"],W+"Sanpellegrino"),
 br("Hires","United States","1876","root beer","The first commercial root beer brand, from Philadelphia.",["Hires Root Beer"],W+"Hires_Root_Beer",["A&W"]),
 br("A&W","United States","1919","root beer","Root beer brand from Lodi, California, owned by Keurig Dr Pepper outside Canada.",["A&W Root Beer"],W+"A&W_Root_Beer"),
 br("Barq's","United States","1898","root beer","Biloxi root beer and crème sodas, owned by Coca-Cola.",["Barq's Root Beer"],W+"Barq's"),
 br("R. White's","United Kingdom","1845","lemonade","British clear lemonade brand.",["R. White's Lemonade"],W+"Lemonade"),
 br("Schweppes","Switzerland","1783","mixers and soft drinks","Soda-water firm founded by Johann Jacob Schweppe in 1783.",["Schweppes Lemonade"],W+"Carbonated_water"),
]
import sys; sys.path.insert(0,"/home/user/Possession-Taxonomy/rebuild/work/J9/agent"); from segfix import fix; brands=fix(brands)
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"All nine planned kinds are new (no old data). Diet/zero, caffeine-free and cane-sugar handled as types, with dated variants as archetype versions. Regional colas without fetched pages kept as flat m entries (named on the Cola page). Lemon & Paeroa left out (only a disambiguation page retrieved). Welch's/Nehi grape soda not on retrieved pages, left out. Dr Pepper-style store brands (Dr. Thunder etc.) not confirmed. Fanta founding year 1940 per infobox."}
p='/home/user/Possession-Taxonomy/rebuild/work/J9/shelves/01_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
