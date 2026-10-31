import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,a='',mk='',y='',v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+s,"v":v or [],"dt":dt}
def V(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
K=[]
K.append({"n":"Croissant & viennoiserie","a":"viennoiseries · breakfast pastries","d":"Yeast-leavened, butter-enriched pastries between bread and pastry, laminated or not, bought fresh or packaged.",
 "t":["laminated","non-laminated (brioche dough)"],"s":W+"Viennoiserie","x":[
 X("Croissant","Crescent of yeast-leavened laminated dough; buttery and flaky.","Croissant",y="early 20th century",
   v=[V("Kipferl (ancestor)","","13th century","Austrian crescent that inspired the croissant"),V("Boulangerie Viennoise, Paris","August Zang","1838–39","Viennese bakery that brought the kipferl to Paris")],dt="butter or margarine · plain or filled · fresh, frozen or packaged"),
 X("Pain au chocolat","Rectangle of laminated viennoiserie dough wrapped round one or two sticks of dark chocolate.","Pain_au_chocolat",a="chocolatine · couque au chocolat · chocolate croissant",dt="one or two chocolate batons · butter content"),
 X("Kouign-amann","Round Breton laminated cake with butter and sugar baked until caramelised.","Kouign-amann",mk="",y="c. 1860",
   v=[V("Original, Douarnenez","Yves-René Scordia","c. 1860",""),V("Kouignette","","","small muffin-shaped version")],dt="size · whole cake or individual"),
 X("Pain aux raisins","Spiral of laminated dough with raisins and crème pâtissière.","Pain_aux_raisins",a="escargot · pain russe"),
 X("Brioche","Non-laminated viennoiserie rich in eggs and butter, with a tender crumb.","Brioche",dt="loaf, tête or rolls · butter proportion"),
 X("Kipferl","Crescent-shaped yeast roll of central Europe, thought to have inspired the croissant.","Kifli",a="kifli · kiflice · cornuri")]})
K.append({"n":"Danish pastry","a":"Danish · wienerbrød","d":"Multilayered, laminated sweet yeast pastry with fillings such as custard, fruit or cinnamon.",
 "t":["custard","fruit","almond","cinnamon"],"s":W+"Danish_pastry","x":[
 X("Spandauer","Round Danish with a filling in the middle, often vanilla custard.","Danish_pastry",dt="custard, jam or fruit centre · icing"),
 X("Cinnamon roll","Spiral sweet roll with cinnamon filling; the Danish 'snail'.","Cinnamon_roll",a="cinnamon bun · cinnamon swirl · cinnamon Danish · snail",dt="yeast or puff-pastry dough · glaze or icing"),
 X("Kringle","Pretzel-shaped Nordic pastry, sweet, salty or filled.","Kringle",a="kringla",dt="size · filling")]})
K.append({"n":"Panettone & pandoro","a":"Italian festive breads","d":"Tall Italian sweet breads sold for Christmas and New Year (and Easter as colomba), by industrial makers and artisans.",
 "t":["classic","chocolate","filled or iced","artisan","industrial"],"s":W+"Panettone","x":[
 X("Panettone","Tall domed Milanese sweet bread with candied fruit and raisins, eaten at Christmas.","Panettone",y="first printed recipe 1853",
   v=[V("Motta panettone","Angelo Motta","1919","gave the tall domed shape with long triple rise"),V("Alemagna panettone","Gioacchino Alemagna","c. 1925",""),V("Bauli panettone","Bauli","","market leader after acquiring Motta and Alemagna")],dt="supermarket vs artisan · plain, chocolate or filled · size"),
 X("Pandoro","Eight-pointed star-shaped sweet bread from Verona, dusted with vanilla icing sugar.","Pandoro",mk="Melegatti",y="1894",
   v=[V("Melegatti pandoro","Melegatti","1894","patented industrial process by Domenico Melegatti"),V("Bauli pandoro","Bauli","","")],dt="plain or filled · size"),
 X("Colomba pasquale","Dove-shaped Easter bread of panettone dough with candied peel, pearl sugar and almonds.","Colomba_pasquale",a="colomba di Pasqua",
   v=[V("Bauli colomba","Bauli","","")],dt="classic or chocolate-topped")]})
K.append({"n":"Stollen & Christmas breads","a":"Christstollen · Weihnachtsstollen · festive fruit breads","d":"Fruit-and-nut yeast breads and cakes made for Christmas and Epiphany, often sugared or with marzipan.",
 "t":["marzipan","butter","almond","poppy seed"],"s":W+"Stollen","x":[
 X("Dresdner Stollen","Moist fruit stollen from Dresden, sold with a seal showing Augustus the Strong.","Stollen",a="Dresden stollen · Striezel",y="1474",
   v=[V("Official Dresden stollen","","","made in about 110 Dresden bakeries under the seal")],dt="weight · marzipan or plain"),
 X("Stollenkranz","Ring-shaped stollen baked in a Bundt or Gugelhupf pan.","Stollen"),
 X("Kerststol","Dutch Christmas stollen, usually with almond paste.","Stollen",a="stol"),
 X("King cake","Epiphany cake, traditionally of brioche dough, with a hidden fève.","King_cake",a="three kings cake · galette des rois · rosca de reyes",dt="brioche or puff pastry · fève figurine")]})
K.append({"n":"Gingerbread & Lebkuchen","a":"honey cake · Pfefferkuchen · piernik · pryanik","d":"Spiced honey or molasses cakes and biscuits, many sold for Christmas and protected by origin.",
 "t":["glazed","chocolate-coated","on wafer (Oblaten)","plain"],"s":W+"Gingerbread","x":[
 X("Nürnberger Lebkuchen","Nuremberg Lebkuchen, a protected designation since 1996; the Elisen grade has at least 25% nuts and under 10% flour.","Lebkuchen",a="Elisenlebkuchen · Nuremberg Lebkuchen",y="1395",
   v=[V("Elisenlebkuchen","","1808","flourless top grade")],dt="nut content · glaze or chocolate · tins"),
 X("Aachener Printen","Hard Lebkuchen from Aachen, a protected geographical indication.","Aachener_Printen",dt="hard or soft · chocolate or nut-topped"),
 X("Toruń gingerbread","Polish gingerbread made in Toruń since the Middle Ages.","Toru%C5%84_gingerbread",a="pierniki toruńskie · Thorner Lebkuchen"),
 X("Pryanik","Eastern European honey-spice cake, often stamped or filled.","Pryanik",a="piernik · perník · medenjak"),
 X("Pfeffernüsse","Small round spice biscuits for the holidays in Germany, the Netherlands and Denmark.","Pfeffern%C3%BCsse",a="pepernoten · pebernødder · peppernuts")]})
K.append({"n":"Fruitcake","a":"fruit cake · Christmas cake","d":"Dense cake of candied or dried fruit, nuts and spices, sometimes soaked in spirits, for Christmas and weddings.",
 "t":["iced","un-iced","spirit-soaked"],"s":W+"Fruitcake","x":[
 X("British Christmas cake","Round rich fruitcake covered with marzipan and royal or fondant icing.","Christmas_cake",dt="iced or plain · spirit used"),
 X("Dundee cake","Scottish fruitcake from Dundee, mass-produced by Keiller's.","Dundee_cake",mk="Keiller's",y="late 18th century"),
 X("Panforte","Chewy, dense Sienese fruit-and-nut Christmas cake.","Panforte"),
 X("American mail-order fruitcake","Nut-rich Southern fruitcake sold by mail-order bakeries.","Fruitcake",
   v=[V("Collin Street Bakery fruitcake","Collin Street Bakery","","Corsicana, Texas"),V("Claxton fruitcake","The Claxton Bakery","","Claxton, Georgia")])]})
K.append({"n":"Doughnut","a":"donut","d":"Fried or baked sweet dough, ring-shaped or filled, from bakeries, chains and supermarkets.",
 "t":["yeast-raised","cake","ring","filled","old-fashioned","Long John","twist / cruller"],"s":W+"Doughnut","x":[
 X("Ring doughnut","Ring-shaped doughnut of yeast dough or cake batter, glazed or sugared.","Doughnut",y="1847 (claimed)",
   v=[V("Krispy Kreme yeast-raised","Krispy Kreme","1937",""),V("Dunkin' doughnuts","Dunkin'","1950","")],dt="yeast or cake · glaze, sugar, chocolate"),
 X("Berliner","German jam doughnut with no hole, sugared or glazed.","Berliner_(doughnut)",a="Krapfen · Pfannkuchen · jam doughnut",v=[V("Kameruner","","","ring-shaped variant, Berlin and eastern Germany")]),
 X("Mochi doughnut","Pull-apart ring of balls made with tapioca flour.","Doughnut",a="pon de ring",mk="Mister Donut"),
 X("Doughnut holes","Small balls of doughnut dough sold by chains under their own names.","Doughnut",v=[V("Munchkins","Dunkin'"),V("Timbits","Tim Hortons","1964")])],
 "r":[["Doughnuts","Krispy Kreme"],["Doughnuts","Dunkin'"],["Doughnuts","Tim Hortons"],["Doughnuts","Mister Donut"]]})
K.append({"n":"Celebration cake","a":"party cake · occasion cake","d":"Decorated cakes bought for birthdays, weddings and festivals.",
 "t":["layer cake","sheet cake","cupcakes","personalised"],"tg":["baby"],"s":W+"Birthday_cake","x":[
 X("Birthday cake","Decorated layer cake with frosting, a message and candles.","Birthday_cake",dt="size · sponge and frosting · decoration"),
 X("Wedding cake","Tiered display cake served at wedding receptions.","Wedding_cake",dt="tiers · fruitcake or sponge · icing"),
 X("Yule log","Christmas sponge roll decorated to look like a log.","Yule_log_(cake)",a="bûche de Noël · chocolate log"),
 X("Japanese Christmas cake","Strawberry-and-cream sponge eaten on Christmas Eve in Japan.","Christmas_cake",mk="Fujiya"),
 X("Colin the Caterpillar","Chocolate roll cake shaped as a caterpillar, sold since 1990.","Colin_the_Caterpillar",mk="Marks & Spencer",y="1990")]})
K.append({"n":"Baumkuchen & layer cake","a":"tree cake · spit cake · layered cake","d":"Cakes built from many thin layers, baked on a spit or layer by layer.",
 "t":["iced","chocolate-coated","plain"],"s":W+"Baumkuchen","x":[
 X("Baumkuchen","German spit cake whose rings look like tree rings; popular in Japan.","Baumkuchen",
   v=[V("Juchheim Baumkuchen","Karl Juchheim","1919","introduced to Japan at Hiroshima")],dt="whole ring or slices · glaze"),
 X("Šakotis","Lithuanian and Polish spit cake with spiky branches.","%C5%A0akotis",a="sękacz · bankukha"),
 X("Lapis legit","Dutch-Indonesian spiced layer cake rich in butter and yolks.","Lapis_legit",a="spekkoek · kueh lapis"),
 X("Kue lapis","Southeast Asian steamed, colourful multi-layered rice cake.","Kue_lapis",a="kuih lapis"),
 X("Dobos torte","Hungarian sponge layered with chocolate buttercream under a caramel top.","Dobos_torte",mk="",y="late 19th century",v=[V("Original","József C. Dobos","late 19th century","")])]})
K.append({"n":"Mooncake","a":"yuebing","d":"Filled Chinese pastries given and eaten at the Mid-Autumn Festival, often boxed as gifts.",
 "t":["lotus seed paste","red bean","five kernel","salted egg yolk","baked","snow skin"],"s":W+"Mooncake","x":[
 X("Cantonese mooncake","Round chewy-crust mooncake, usually lotus seed paste, often with egg yolk; the best-known style.","Mooncake",
   v=[V("Wing Wah mooncakes","Wing Wah","","Hong Kong")],dt="filling · number of yolks · gift box"),
 X("Suzhou-style mooncake","Flaky lard-pastry mooncake, sweet or savoury with pork.","Mooncake"),
 X("Teochew-style mooncake","Large thin flaky mooncake, often with yam filling.","Mooncake",a="la bia"),
 X("Beijing-style mooncake","Northern style in two variations, one influenced by Suzhou.","Mooncake"),
 X("Snow skin mooncake","Unbaked chilled mooncake with a white glutinous-rice crust, from Hong Kong.","Mooncake",a="snowskin"),
 X("Bánh pía","Vietnamese Suzhou-style flaky mooncake adapted from Teochew cuisine.","B%C3%A1nh_p%C3%ADa")],
 "r":[["Mooncakes","Wing Wah"]]})
K.append({"n":"Castella & sponge cake","a":"kasutera · sponge · snack cake","d":"Light egg-foam cakes and bought sponge-based snack cakes.",
 "t":["plain","filled","rolled"],"s":W+"Sponge_cake","x":[
 X("Castella","Moist Nagasaki sponge cake of Portuguese origin, sold in long boxed bars.","Castella",a="kasutera",y="16th century",
   v=[V("Castella Honke Fukusaya","Fukusaya","1624","Nagasaki"),V("Shooken","Shooken","1681","Nagasaki"),V("Bunmeidō","Bunmeidō","1900","Nagasaki"),V("Siberia","","Meiji era","castella filled with yōkan")],dt="honey or matcha · zarame sugar base"),
 X("Victoria sponge","Butter sponge sandwich made possible by baking powder.","Sponge_cake",dt="jam and cream filling"),
 X("Swiss roll","Rolled sponge with jam, cream or icing.","Swiss_roll",a="jelly roll · roulade · mini rolls"),
 X("Lamington","Australian sponge squares coated in chocolate and desiccated coconut.","Lamington"),
 X("Twinkie","Golden sponge snack cake with creamy filling.","Twinkie",mk="Hostess Brands",y="1930")],
 "r":[["Cakes","Mr Kipling"],["Snack cakes","Hostess Brands"]]})
def B(n,c,f,seg,d,s,sig=None,lines=None,rel=None):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines or [],"eras":[],"sig":sig or [],"sc":[],"rel":rel or [],"s":W+s}
BR=[B("Bauli","Italy","1922","Industrial festive bakery","Verona bakery company making pandoro, panettone, colomba and cornetti; owns Motta and Alemagna.","Bauli",["Pandoro","Panettone","Colomba pasquale"],["Motta","Alemagna"]),
 B("Krispy Kreme","United States","1937","Doughnut chain","American doughnut company and coffeehouse chain founded by Vernon Rudolph in Winston-Salem.","Krispy_Kreme",["Ring doughnut"]),
 B("Dunkin'","United States","1950","Doughnut and coffee chain","Coffee and doughnut chain founded by Bill Rosenberg in Quincy, Massachusetts.","Dunkin%27_Donuts",["Ring doughnut","Doughnut holes"],["Munchkins"],["Mister Donut"]),
 B("Tim Hortons","Canada","1964","Coffee and doughnut chain","Canada's largest quick-service chain, serving coffee and doughnuts.","Tim_Hortons",["Doughnut holes"],["Timbits"]),
 B("Mister Donut","United States","1956","Doughnut chain","Doughnut chain founded by Harry Winokur, now mainly in Asia.","Mister_Donut",["Mochi doughnut"],[],["Dunkin'"]),
 B("Wing Wah","Hong Kong","","Bakery and mooncake maker","Hong Kong food manufacturer best known for mooncakes.","Wing_Wah",["Cantonese mooncake"]),
 B("Collin Street Bakery","United States","","Fruitcake bakery","Corsicana, Texas bakery best known for fruitcake.","Collin_Street_Bakery",["American mail-order fruitcake"]),
 B("The Claxton Bakery","United States","","Fruitcake bakery","Claxton, Georgia confectionery company known for fruitcake.","The_Claxton_Bakery",["American mail-order fruitcake"]),
 B("Keiller's","United Kingdom","","Marmalade and cake maker","Dundee marmalade brand credited with the Dundee cake.","Keiller%27s_marmalade",["Dundee cake"]),
 B("Mr Kipling","United Kingdom","1967","Packaged cakes","Brand of cakes and pies; the UK's largest cake maker by 1976.","Mr_Kipling"),
 B("Hostess Brands","United States","2013","Snack cakes","American bakery company making Hostess snack cakes, owned by J.M. Smucker.","Hostess_Brands",["Twinkie"])]
def T(n,r,p,d,tech,mat,forms,ctr,auth,s):
    return {"n":n,"g":"Food & drink","r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":W+s}
TR=[T("Dresden Christstollen","Dresden, Saxony, Germany","since 1474","Christmas fruit stollen baked by Dresden bakers.","yeast dough with macerated fruit, sugared","butter, dried and candied fruit, almonds",["Dresdner Stollen"],["about 110 Dresden bakeries","Striezelmarkt"],"seal showing Augustus the Strong","Stollen"),
 T("Nuremberg Lebkuchen","Nuremberg, Germany","since 1395","Guild-baked honey-spice cakes, protected since 1996.","nut-rich dough baked on wafer","honey, nuts, spices",["Nürnberger Lebkuchen","Elisenlebkuchen"],["Nuremberg bakeries"],"made within the city; Elisen grade ≥25% nuts, <10% flour","Lebkuchen"),
 T("Aachener Printen","Aachen, Germany","","Hard Lebkuchen from Aachen with protected origin.","baked spiced dough","sugar-beet syrup, spices",["Aachener Printen"],["Aachen"],"maker located in or near Aachen (PGI)","Aachener_Printen"),
 T("Toruń gingerbread","Toruń, Poland","Middle Ages to present","Traditional Polish gingerbread of Toruń.","moulded spiced honey dough","honey, spices",["Toruń gingerbread"],["Toruń"],"","Toru%C5%84_gingerbread"),
 T("Nagasaki castella","Nagasaki, Japan","16th century to present","Portuguese-derived sponge cake regarded as wagashi.","baked in square moulds with mizuame and zarame","eggs, flour, sugar, mizuame",["Castella"],["Fukusaya (1624)","Shooken (1681)","Bunmeidō (1900)"],"","Castella")]
out={"kinds":K,"brands":BR,"traditions":TR,"notes":"All 11 planned kinds built (shelf had no old data). Festive use noted in definitions. Left out: Motta, Alemagna, Melegatti, Juchheim, Fukusaya, Fujiya, Marks & Spencer brand entries (no page retrieved; Wikipedia API rate-limited, Parallel out of credit) - they appear only as version/archetype makers. Not added: pastel de nata (custard tart, not a planned kind), Gugelhupf/Bundt cake (no planned kind fits), Tunnock's (no product facts retrieved). Doughnut and mooncake chains kept as ranges; no SKU names confirmed."}
p='work/J8/shelves/00_01.json'; os.makedirs('work/J8/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(len(K),sum(len(k['x']) for k in K),len(BR),len(TR))
