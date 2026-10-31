import json, os, sys
sys.path.insert(0,"/home/user/Possession-Taxonomy/rebuild/work/J9/agent"); from segfix import fix
W='https://en.wikipedia.org/wiki/'
K=[]
def k(n,a,d,s,t=None,m=None,x=None):
    o={"n":n,"a":a,"d":d}
    if t: o["t"]=t
    o["s"]=s
    if x: o["x"]=x
    if m: o["m"]=m
    K.append(o)
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
k("Canned coffee","canned coffee · can coffee · kan kōhī","Pre-brewed coffee sold ready to drink in cans, sold hot or cold from vending machines across East Asia.",W+"Canned_coffee",
  t=["with milk","black","low sugar","café au lait","hot-vending can","bottle-can"],
  x=[X("UCC Coffee with Milk","UCC Milk Coffee","Sweet milk coffee in a slim can, launched in April 1969 as the first mass canned coffee.","UCC Ueshima Coffee","1969",W+"UCC_Ueshima_Coffee_Co.",[("UCC Coffee with Milk","UCC Ueshima Coffee","1969","Original, April 1969")],"slim can · original or reduced sugar"),
     X("Georgia","Georgia Coffee","Coca-Cola's Japanese canned coffee range, the top-grossing canned coffee in Japan.","Coca-Cola (Japan)","1975","https://en.wikipedia.org/wiki/Georgia_(coffee)",[("Emerald Mountain Blend","Coca-Cola (Japan)","","Signature blend"),("US release","Coca-Cola (Japan)","2009","Sold mainly in Asian grocery stores")],"can or bottle-can · blend · with milk or black"),
     X("Boss","Suntory Boss","Suntory canned coffee range with a pipe-smoking 'boss' logo, known for Tommy Lee Jones adverts since 2006.","Suntory","1992",W+"Boss_Coffee",[("Super Blend","Suntory","1992","Original"),("Boss Rainbow","Suntory","","Rainbow-coloured can"),("Craft Boss","Suntory","","Bottled sub-brand: Cafe Latte, Black Coffee"),("All-Star blend","Suntory","2022","30th-anniversary limited edition")],"can or PET bottle · blend · with milk or black")],
  m=[["Fire","Kirin Beverage"],["Dydo Blend","Dydo"],["Wonda","Asahi Soft Drinks"],["Nescafé canned coffee","Nestlé"],["Roots","Suntory"],["Mr Brown","King Car Group"],["Lotte canned coffee","Lotte"]])
k("Cold brew & iced coffee","cold brew · nitro cold brew · Dutch coffee · Kyoto-style","Coffee steeped cold for 12–24 hours, sold as concentrate, bottles or nitrogen-charged cans.",W+"Cold_brew_coffee",
  t=["ready-to-drink black","concentrate","nitro can","slow-drip (Kyoto-style)","sweetened / with milk"],
  m=[["Stumptown nitro cold brew","Stumptown"],["Cuvee nitro cold brew","Cuvee Coffee"],["RISE nitro cold brew","RISE Brewing Co."]])
k("Bottled latte & coffee drink","bottled latte · coffee drink · draft latte","Ready-to-drink milk-coffee drinks in bottles or cans, from sweet blended coffees to nitro-textured lattes.",W+"Frappuccino",
  t=["blended / Frappuccino-style","latte","mocha","protein coffee","nitro-textured can"],
  x=[X("Starbucks bottled Frappuccino","Frappuccino bottled coffee drink","Sweet bottled coffee-and-milk drink, the first product of Starbucks and PepsiCo's North American Coffee Partnership.","Starbucks","1996",W+"Frappuccino",[("Bottled Frappuccino","North American Coffee Partnership","1996","First bottled version")],"glass bottle · flavour"),
     X("La Colombe Draft Latte","","Cold-pressed espresso and milk in a can that froths on opening via a nitrous-oxide valve.","La Colombe","2016",W+"La_Colombe_Coffee_Roasters",[("Canned Draft Latte","La Colombe","2016","Launched in four flavours")],"can · flavour")],
  m=[["Craft Boss Cafe Latte","Suntory"]])
k("Iced tea","iced tea · ice tea · sweet tea","Chilled tea sold sweetened or unsweetened, often lemon or peach flavoured, in bottles, cans and cartons.",W+"Iced_tea",
  t=["lemon","peach","sweet tea","unsweetened","half-and-half (with lemonade)","sparkling"],
  x=[X("Lipton Ice Tea","Lipton Iced Tea","Ready-to-drink iced tea from the PepsiCo–Unilever joint ventures, in lemon, peach and other flavours.","Lipton","1991",W+"Lipton",[("Pepsi Lipton Tea Partnership","Lipton","1991","North American joint venture"),("Pepsi Lipton International","Lipton","2003","Joint venture outside North America"),("Pure Leaf","Lipton","","Brewed real-leaf iced tea"),("Brisk","Lipton","","Sharp North American iced tea")],"lemon, peach, mango, raspberry · PET, can or carton"),
     X("AriZona Iced Tea","Arizona","Brooklyn-founded iced tea in large painted cans with a printed 99-cent price.","Arizona Beverage Company","1992",W+"Arizona_Beverage_Company",[("First AriZona teas","Arizona Beverage Company","1992","First four teas by 1993, including green tea"),("Arnold Palmer","Arizona Beverage Company","1990s","Iced tea and lemonade blend under licence")],"22 oz Big Can · flavour"),
     X("Snapple iced tea","Snapple","Bottled iced tea from a New York juice company, starting with lemon tea in 1987.","Snapple","1987",W+"Snapple",[("Lemon tea","Snapple","1987","First tea"),("Raspberry and peach teas","Snapple","","Original and diet")],"glass bottle or can · flavour")],
  m=[["Fuze Tea","Coca-Cola"],["Nestea","Nestea"]])
k("Bottled green & oolong tea","bottled green tea · ocha · canned oolong · RTD tea","Unsweetened Japanese-style green or oolong tea in cans and PET bottles, sold chilled or heated.","https://en.wikipedia.org/wiki/Canned_tea",
  t=["sencha","genmaicha","matcha-blend","oolong","black oolong","hot PET bottle"],
  x=[X("Oi Ocha","Ito En green tea","ITO EN's unsweetened green tea, the first canned sencha and first PET-bottled green tea.","ITO EN","1985","https://www.itoen-global.com/about_us/history.html",[("Canned sencha","ITO EN","1985","World's first canned green tea"),("Oi Ocha","ITO EN","1989","Renamed Oi Ocha"),("PET bottle","ITO EN","1990","First green tea in a PET bottle"),("Heatable PET bottle","ITO EN","2000","For hot vending")],"can or PET · sencha, koicha, genmaicha"),
     X("Canned oolong tea","Ito En oolong","Unsweetened oolong in a can, the first canned tea product in Japan.","ITO EN","1980","https://www.itoen-global.com/about_us/history.html",[],"can or PET"),
     X("Iyemon","Iyemon Cha","Suntory bottled green tea developed with the Kyoto tea merchant Fukujuen, named after its founder.","Suntory","2004","https://global.fukujuen.com/pages/history",[("Iyemon","Suntory","2004","Collaboration brand with Fukujuen")],"PET bottle · size")],
  m=[["Teas' Tea","ITO EN"]])
k("Barley & grain tea","barley tea · mugicha · boricha · damai cha","Caffeine-free infusion of roasted barley or other grains, sold bottled and drunk cold in Japan and hot or cold in Korea.",W+"Barley_tea",
  t=["barley","corn tea","mixed grain","hot PET bottle"],
  m=[["AGV barley tea","AGV"],["Haneul Bori","Woongjin Food"]])
k("Milk tea & bubble tea","milk tea · royal milk tea · bubble tea · boba · pearl milk tea","Ready-to-drink sweet tea with milk, including Japanese bottled milk teas, Hong Kong-style canned milk tea and bubble tea in sealed cups or kits.",W+"Bubble_tea",
  t=["bottled milk tea","Hong Kong-style canned milk tea","sealed-cup bubble tea","bubble tea kit (tea and tapioca pearls)","no sugar"],
  x=[X("Kirin Gogo no Kocha","Kirin Afternoon Tea","Kirin's bottled black tea range named after British afternoon tea, said to be Japan's first bottled tea.","Kirin","1986","https://www.kirin.co.jp/experience/factory/en/gogo/sukkiricafe/",[("Straight Tea","Kirin","1986","Original lightly sweet tea"),("Milk Tea","Kirin","","Milk tea"),("Lemon Tea","Kirin","","Lemon tea")],"PET bottle · straight, milk or lemon")])
k("Yerba mate & guayusa drink","yerba mate drink · mate tea · guayusa · tereré","Bottled or canned brewed yerba mate or guayusa, still or sparkling, as a caffeinated alternative to coffee.",W+"Yerba_mate",
  t=["still brewed","sparkling","sweetened iced mate","guayusa"],
  x=[X("Guayakí yerba mate","Guayaki","Californian yerba mate brand founded by Cal Poly friends, sold in bottles and cans.","Guayakí","1996","https://magazine.calpoly.edu/spring-summer-2018/cultivating-change-guayaki-21-years-later/",[("Glass bottles","Guayakí","2005","First bottled drinks")],"bottle or can · flavour")],
  m=[["Matte Leão iced mate","Matte Leão"],["Runa","Vita Coco"]])
B=[
 {"n":"UCC Ueshima Coffee","c":"Japan","f":"1933","seg":"Mainstream","kf":"coffee","d":"Kobe coffee company founded by Tadao Ueshima, maker of the first canned coffee.","sig":["UCC Coffee with Milk"],"s":W+"UCC_Ueshima_Coffee_Co."},
 {"n":"Coca-Cola (Japan)","c":"Japan","seg":"Mainstream","kf":"soft drinks","d":"Japanese subsidiary of The Coca-Cola Company, maker of Georgia coffee.","sig":["Georgia"],"s":"https://en.wikipedia.org/wiki/Georgia_(coffee)"},
 {"n":"Suntory","c":"Japan","f":"1899","seg":"Mainstream","kf":"drinks","d":"Osaka drinks group behind Boss coffee and Iyemon green tea.","lines":["Boss","Iyemon","Craft Boss"],"sig":["Boss","Iyemon"],"s":"knowledge"},
 {"n":"Starbucks","c":"United States","f":"1971","seg":"Mainstream","kf":"coffee","d":"Seattle coffeehouse chain whose bottled drinks are made with PepsiCo.","sig":["Starbucks bottled Frappuccino"],"s":"knowledge"},
 {"n":"La Colombe","c":"United States","f":"1994","seg":"Premium","kf":"coffee","d":"Philadelphia roaster known for the canned Draft Latte, owned by Chobani since 2023.","sig":["La Colombe Draft Latte"],"s":W+"La_Colombe_Coffee_Roasters"},
 {"n":"Lipton","c":"United Kingdom","seg":"Mainstream","kf":"tea","d":"Tea brand whose ready-to-drink iced teas are made by PepsiCo–Unilever joint ventures.","lines":["Lipton Ice Tea","Pure Leaf","Brisk"],"sig":["Lipton Ice Tea"],"s":W+"Lipton"},
 {"n":"Arizona Beverage Company","c":"United States","f":"1992","seg":"Value","kf":"iced tea","d":"Brooklyn-founded iced tea company of Don Vultaggio and John Ferolito.","sig":["AriZona Iced Tea"],"s":W+"Arizona_Beverage_Company"},
 {"n":"Snapple","c":"United States","f":"1972","seg":"Mainstream","kf":"iced tea & juice drinks","d":"New York-founded tea and juice brand, owned by Keurig Dr Pepper.","sig":["Snapple iced tea"],"s":W+"Snapple"},
 {"n":"ITO EN","c":"Japan","f":"1966","seg":"Specialist","kf":"green tea","d":"Tokyo tea company that launched the first canned and PET-bottled green tea.","lines":["Oi Ocha","Teas' Tea"],"sig":["Oi Ocha","Canned oolong tea"],"s":"https://www.itoen-global.com/about_us/history.html"},
 {"n":"Fukujuen","c":"Japan","f":"1790","seg":"Heritage manufactory","kf":"Uji tea","d":"Kyoto tea merchant founded by Iyemon Fukui; partner in Suntory's Iyemon.","rel":["Suntory"],"s":"https://global.fukujuen.com/pages/history"},
 {"n":"Kirin","c":"Japan","seg":"Mainstream","kf":"beer & soft drinks","d":"Japanese drinks group whose Kirin Beverage makes Gogo no Kocha and Fire coffee.","sig":["Kirin Gogo no Kocha"],"s":"https://www.kirin.co.jp/experience/factory/en/gogo/sukkiricafe/"},
 {"n":"Guayakí","c":"United States","f":"1996","seg":"Specialist","kf":"yerba mate","d":"Sebastopol, California yerba mate company started by five Cal Poly friends.","sig":["Guayakí yerba mate"],"s":"https://magazine.calpoly.edu/spring-summer-2018/cultivating-change-guayaki-21-years-later/"},
]
T=[{"n":"Hong Kong-style milk tea","g":"Food & drink","r":"Hong Kong","p":"mid-20th century to present","d":"Strong 'silk-stocking' black tea with evaporated milk, sold fresh and as cold milk tea in cans and bottles.","tech":"Ceylon black tea blend mixed with evaporated or condensed milk","mat":"Ceylon black tea, evaporated milk","forms":["hot milk tea","iced milk tea","canned or bottled cold milk tea"],"ctr":["Hong Kong"],"auth":"smooth, strong tea with evaporated milk; technique listed as Hong Kong intangible cultural heritage (2017)","s":W+"Hong_Kong-style_milk_tea"}]
notes=("All 8 planned kinds kept (no old data). Suntory brand facts from knowledge (suntory.com blocked, 403); Starbucks from knowledge. Left out: Suntory Oolong Tea 1981 (only snippets; Suntory pages 403), Nescafé RTD specifics (Nescafé page has none), "
"Stumptown/La Colombe beyond retrieved facts, named bubble-tea kits and HK milk-tea can brands (none on retrieved pages), Toddy. Canned oolong first date: ITO EN history says 1980, Wikipedia 'Canned tea' says 1981; used maker's 1980.")
fix(B)
out={"kinds":K,"brands":B,"traditions":T,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J9/shelves/07_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
