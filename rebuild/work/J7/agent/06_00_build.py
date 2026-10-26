import json, os
W='https://en.wikipedia.org/wiki/'
def A(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":x[0],"mk":x[1],"y":x[2],"d":x[3]} for x in v],"dt":dt}
gin={"n":"Gin","a":"","d":"Spirit flavoured predominantly with juniper, either redistilled with botanicals or compounded with flavourings.",
 "t":["London dry gin","Distilled gin","Compound gin","Plymouth gin","Old Tom gin","Navy strength gin","Contemporary (New Western) gin","Pot-distilled gin"],
 "s":W+"Gin","x":[
 A("Gordon's London Dry Gin","London dry gin made to Alexander Gordon's recipe since 1769; reportedly unchanged.","Gordon's","1769",W+"Gordon%27s_Gin",
   [("Gordon's Gin","Gordon's","",""),("Gordon's Special Old Tom Gin","Gordon's","1921","Old Tom style; discontinued 1987"),("Gordon's Distiller's Cut","Gordon's","2004","lemongrass and ginger; discontinued"),("Gordon's Pink","Gordon's","2017","red berry flavours"),("Gordon's alcohol-free","Gordon's","2020","")],
   "strength by market · flavoured editions"),
 A("Plymouth Gin","Earthier, softer-juniper, more citrus derivative of London dry, distilled at the Black Friars Distillery, Plymouth, since 1793.","Plymouth","1793",W+"Plymouth_Gin",
   [("Plymouth Original Strength","Plymouth","1998","41.2%, restored in 1998 relaunch"),("Plymouth Navy Strength","Plymouth","1998","57% ABV (100° English proof)")],
   "strength 41.2 · 47 · 57%"),
 A("Tanqueray London Dry Gin","London dry gin first distilled by Charles Tanqueray in Bloomsbury in 1830.","Tanqueray","1830",W+"Tanqueray",
   [("Tanqueray No. Ten","Tanqueray","2000","47.3%, aimed at the martini"),("Tanqueray Malacca","Tanqueray","1997","discontinued 2001, limited relaunch 2013"),("Tanqueray Rangpur","Tanqueray","2006","41.3%"),("Tanqueray 0.0","Tanqueray","2021","non-alcoholic")],
   "strength 40 · 41.3 · 43.1 · 47.3% by market"),
 A("Beefeater London Dry Gin","London dry gin of James Burrough's Chelsea distillery, introduced in 1876.","Beefeater","1876",W+"Beefeater_Gin",
   [("Beefeater 24","Beefeater","2009","45%"),("Beefeater Crown Jewel","Beefeater","",""),("Beefeater 0.0%","Beefeater","2024","")],
   "strength · flavoured editions at 37.5%"),
 A("Bombay Sapphire","Vapour-infused London dry gin with ten botanicals in a blue bottle, launched in 1986.","Bombay Sapphire","1986",W+"Bombay_Sapphire",
   [("Bombay Original Dry","Bombay Sapphire","","eight botanicals"),("Bombay Sapphire East","Bombay Sapphire","2011","adds lemongrass and black pepper, 42%"),("Star of Bombay","Bombay Sapphire","2015","47.5%"),("Bombay Bramble","Bombay Sapphire","","blackberry and raspberry, 37.5%")],
   "botanical count · strength"),
 A("Hendrick's Gin","Scottish gin from Girvan with rose and cucumber, launched in 1999; a model for contemporary gin.","Hendrick's","1999",W+"Hendrick%27s_Gin",
   [("Hendrick's Orbium","Hendrick's","2017","blue lotus, cinchona, wormwood"),("Hendrick's Midsummer Solstice","Hendrick's","2019","floral"),("Hendrick's Lunar","Hendrick's","2021","baked spices and citrus"),("Hendrick's Neptunia","Hendrick's","2022","kelp, thyme, lime")],
   "annual limited editions"),
 A("Monkey 47 Schwarzwald Dry Gin","Black Forest gin of 47 botanicals, a third picked locally, revived by Alexander Stein from Montgomery Collins's recipe.","Monkey 47","",
   "https://www.diffordsguide.com/producer/1194/monkey-47",
   [("Monkey 47 Sloe Gin","Monkey 47","",""),("Monkey 47 Barrel Cut","Monkey 47","","aged in mulberry-wood casks"),("Monkey 47 Experimentum 2y06","Monkey 47","2022","sixth Experimentum edition")],
   "50 cl apothecary bottle · editions"),
 A("New Western dry gin","Contemporary style where juniper shares the lead with other botanicals; Aviation from Oregon was an early example.","","",W+"Gin",
   [("Aviation American Gin","","","Oregon, US")],"botanical lead · country"),
 ],"m":[["The Belfry 1960 London Dry Gin","Hawkridge Distillery"]]}
gen={"n":"Genever","a":"Jenever · Genièvre · Dutch gin","d":"Juniper-flavoured spirit of the Low Countries made with malt wine.",
 "t":["Grain genever","Hasselt genever","Peket","Barrel-aged"],"s":"https://en.wikipedia.org/wiki/Jenever","x":[
 A("Oude genever","Old-style genever with at least 15% malt wine and up to 20 g/l sugar; 'old' refers to method, not age.","","",W+"Jenever",
   [("Bols Genever","Bols","",""),("Zuidam 1 Year Old Rogge (Rye) Genever","Zuidam","","rye")],"malt-wine share · cask ageing",a="Old genever"),
 A("Jonge genever","Young-style genever with up to 15% malt wine and 10 g/l sugar, close to neutral in taste.","","",W+"Jenever",
   [("Zuidam Jonge (Young Grain) Genever","Zuidam","",""),("Claeryn","Bols","","jonge genever")],"grain base · strength",a="Young genever"),
 A("Korenwijn","Genever with 51–70% malt wine and up to 20 g/l sugar, often matured in oak.","","",W+"Jenever",
   [("Zuidam 1 Year Old Korenwijn Jenever","Zuidam","","")],"malt-wine share · years in oak",a="Corenwyn · grain wine"),
 ]}
vod={"n":"Vodka","a":"Wódka · Vodka","d":"Neutral spirit distilled and filtered to minimal character, made from grain, potatoes or other farm produce.",
 "t":["Grain vodka (wheat, rye, barley, corn)","Potato vodka","Grape vodka","Molasses or other base"],"s":"https://www.masterofmalt.com/vodka/","x":[
 A("Wyborowa","Polish rye-tradition vodka first made in Poznań by Hartwig Kantorowicz in 1823.","Wyborowa","1823",W+"Vodka",[],"strength"),
 A("Smirnoff No. 21","Smirnoff's core red-label vodka, created by Vladimir Smirnov after the family left Russia; brand from Pyotr Smirnov's 1864 Moscow distillery.","Smirnoff","1864",W+"Smirnoff",
   [("Smirnoff","Smirnoff","",""),("Smirnoff Black (No. 55)","Smirnoff","","small batch, copper stills, 40%")],"37.5 or 40% by market",a="Smirnoff Red Label"),
 A("Stolichnaya","Soviet-era wheat and rye vodka, now split between Russian and Latvian producers after long trademark disputes.","Stolichnaya","1938",W+"Stolichnaya",
   [("Stolichnaya","Stolichnaya","",""),("Stolichnaya Elit","Stolichnaya","","")],"producer (Russia / Latvia) · 40%",a="Stoli"),
 A("Finlandia","Finnish six-row barley vodka cut with Rajamäki glacial spring water, created by Alko in 1970.","Finlandia","1970",W+"Finlandia_(vodka)",[("Finlandia","Finlandia","","")],"strength"),
 A("Absolut Vodka","Swedish winter-wheat vodka from Åhus, launched by Vin & Sprit in 1979 in its apothecary bottle.","Absolut","1979",W+"Absolut_Vodka",[("Absolut","Absolut","","")],"bottle size · limited-edition bottles",a="Absolut"),
 A("Ketel One","Wheat vodka from the Nolet distillery in Schiedam (founded 1691), launched in 1983.","Ketel One","1983",W+"Ketel_One",[("Ketel One","Ketel One","","")],"strength"),
 A("Chopin","Polish vodka from Siedlce made in separate potato, rye and wheat versions, introduced in 1992.","Chopin","1992",W+"Chopin_(vodka)",[],"base: potato · rye · wheat"),
 A("Belvedere","Polish Dankowskie rye vodka from Żyrardów, produced since 1993.","Belvedere","1993",W+"Belvedere_(vodka)",
   [("Belvedere","Belvedere","",""),("Belvedere Single Estate Rye","Belvedere","2017","replaced Unfiltered")],"estate · strength"),
 A("Grey Goose","French soft-winter-wheat vodka blended in Cognac, created by Sidney Frank in 1997.","Grey Goose","1997",W+"Grey_Goose_(vodka)",[("Grey Goose","Grey Goose","","")],"bottle size"),
 A("Tito's Handmade Vodka","Corn vodka from Austin, Texas, made in pot stills since 1997.","Tito's","1997","https://en.wikipedia.org/wiki/Tito%27s_Vodka",[("Tito's Vodka","Tito's","","")],"bottle size"),
 ],"m":[["Crystal Head Vodka",""],["Reyka",""],["62Nordic Spirits Premium Vodka","62Nordic Spirits"],["Alexander Vodka","Alexandrion Saber Distilleries"],["Doa Distilleria Orobica Autonoma Premium Vodka","Doa Distilleria Orobica Autonoma"]]}
fv={"n":"Flavoured vodka","a":"","d":"Vodka infused or compounded with fruit, herbs, spices or other flavourings.",
 "t":["Citrus","Berry & fruit","Pepper & spice","Herb & grass","Dessert & sweet"],"s":"https://www.masterofmalt.com/vodka/","x":[
 A("Żubrówka Bison Grass","Polish vodka flavoured with bison grass, a blade in every bottle; commercial since 1928.","Żubrówka","1928",W+"%C5%BBubr%C3%B3wka",
   [("Żubrówka (US rye-based version)","Żubrówka","2011","coumarin-free recipe"),("Żubrówka Czarna","Żubrówka","","charcoal- and oak-filtered, unflavoured")],"blade of grass · US / EU recipe",a="Bison grass vodka · Zubrowka"),
 A("Absolut Peppar","Pepper-flavoured Absolut, the brand's first flavour, launched in 1986.","Absolut","1986",W+"Absolut_Vodka",[],""),
 A("Absolut Citron","Lemon-flavoured Absolut launched in 1988, a template for citrus vodkas.","Absolut","1988",W+"Absolut_Vodka",
   [("Absolut Kurant","Absolut","1992","blackcurrant")],"fruit flavour"),
 ],"m":[["Grey Goose L'Orange","Grey Goose"],["Grey Goose Le Citron","Grey Goose"],["Ketel One Citroen","Ketel One"],["Ketel One Botanical","Ketel One"],["Stolichnaya Razberi","Stolichnaya"],["Belvedere Maceration","Belvedere"],["Smirnoff Twist","Smirnoff"]]}
aq={"n":"Aquavit","a":"Akvavit · Snaps","d":"Scandinavian grain or potato spirit flavoured mainly with caraway or dill.",
 "t":["Taffel (clear, unaged)","Cask-aged","Norwegian","Danish","Swedish (with fennel)"],"s":"https://www.masterofmalt.com/aquavit/","x":[
 A("Linie Aquavit","Norwegian aquavit aged in oloroso casks then shipped as deck cargo across the equator and back; recipe since 1821.","Linie","1821","https://matadornetwork.com/read/norwegian-liquor-travels-world/",
   [("Linie Aquavit","Linie","","")],"voyage (ship, dates on label)"),
 A("Aalborg Taffel Akvavit","Clear Danish caraway akvavit from Isidor Henius's Aalborg factory, opened in 1846.","Aalborg","1846","https://www.systembolaget.se/produkt/sprit/aalborg-16501/",
   [("Aalborg Jubilæums Akvavit","Aalborg","1946","dill and coriander; centenary tribute to Taffel")],"clear · aged"),
 A("O.P. Anderson Aquavit","Sweden's oldest and best-selling akvavit, with caraway, anise and fennel, oak-aged; first shown in Gothenburg in 1891.","O.P. Anderson","1891",W+"O.P._Anderson",
   [("Gammaldags Norrlands Akvavit","O.P. Anderson","1929","same spices plus sherry"),("Skåne Akvavit","O.P. Anderson","1931","milder")],"oak ageing"),
 ],"m":[["Bivrost Cask Aquavit","Bivrost"],["Svol Danish-Style Aquavit","Svol"]]}
def B(n,c,f,seg,d,s,lines=(),sig=(),rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Gordon's","England","1769","Gin","London dry gin founded by Alexander Gordon; owned by Diageo.",W+"Gordon%27s_Gin",["Special London Dry","Pink"],["Gordon's London Dry Gin"],["Tanqueray"]),
 B("Plymouth","England","1793","Gin","Gin from the Black Friars Distillery, Plymouth; owned by Pernod Ricard.",W+"Plymouth_Gin",["Original Strength","Navy Strength"],["Plymouth Gin"],["Beefeater"]),
 B("Tanqueray","England","1830","Gin","London gin first distilled by Charles Tanqueray; owned by Diageo.",W+"Tanqueray",["London Dry","No. Ten","Rangpur"],["Tanqueray London Dry Gin"],["Gordon's"]),
 B("Beefeater","England","1876","Gin","London dry gin of James Burrough; owned by Pernod Ricard.",W+"Beefeater_Gin",["London Dry","24"],["Beefeater London Dry Gin"],["Plymouth"]),
 B("Bombay Sapphire","England","1986","Gin","Gin launched by International Distillers & Vintners, distilled at Laverstoke Mill; owned by Bacardi.",W+"Bombay_Sapphire",["Sapphire","Original Dry","East"],["Bombay Sapphire"],["Grey Goose"]),
 B("Hendrick's","Scotland","1999","Gin","Rose-and-cucumber gin made at Girvan by William Grant & Sons.",W+"Hendrick%27s_Gin",["Original","Orbium","limited editions"],["Hendrick's Gin"],[]),
 B("Monkey 47","Germany","","Gin","Black Forest gin of Black Forest Distillers, founded by Alexander Stein; majority owned by Pernod Ricard.","https://www.diffordsguide.com/producer/1194/monkey-47",["Schwarzwald Dry Gin","Sloe Gin","Barrel Cut","Experimentum"],["Monkey 47 Schwarzwald Dry Gin"],[]),
 B("Bols","Netherlands","1575","Genever & liqueurs","Amsterdam distiller dating from the Bols family's 't Lootsje of 1575; dominant genever producer after buying Henkes in 1986.",W+"Lucas_Bols",["Bols Genever","Claeryn","Bokma","Hartevelt"],[],[]),
 B("Wyborowa","Poland","1823","Vodka","Polish vodka first made in Poznań by Hartwig Kantorowicz.",W+"Vodka",[],["Wyborowa"],["Chopin","Belvedere"]),
 B("Smirnoff","Russia / United Kingdom","1864","Vodka","Vodka brand from Pyotr Smirnov's Moscow distillery, rebuilt abroad via Heublein; owned by Diageo.",W+"Smirnoff",["No. 21","Black","Ice"],["Smirnoff No. 21"],[]),
 B("Stolichnaya","Russia / Latvia","1938","Vodka","Soviet vodka brand whose rights are contested by FKP Sojuzplodoimport and SPI Group (sold as Stoli).",W+"Stolichnaya",["Stolichnaya","Elit"],["Stolichnaya"],[]),
 B("Finlandia","Finland","1970","Vodka","Barley vodka created by Alko; owned by Coca-Cola HBC since 2023.",W+"Finlandia_(vodka)",[],["Finlandia"],[]),
 B("Absolut","Sweden","1979","Vodka","Winter-wheat vodka from Åhus by The Absolut Company, owned by Pernod Ricard.",W+"Absolut_Vodka",["Absolut","Peppar","Citron","Kurant"],["Absolut Vodka","Absolut Citron"],[]),
 B("Ketel One","Netherlands","1983","Vodka","Wheat vodka of the Nolet distillery, Schiedam, owned jointly by the Nolet family and Diageo.",W+"Ketel_One",["Citroen","Oranje","Botanical"],["Ketel One"],[]),
 B("Chopin","Poland","1992","Vodka","Vodka made by Polmos Siedlce from potato, rye or wheat.",W+"Chopin_(vodka)",[],["Chopin"],["Belvedere"]),
 B("Belvedere","Poland","1993","Vodka","Rye vodka from Polmos Żyrardów, owned by LVMH.",W+"Belvedere_(vodka)",["Single Estate Rye","Maceration"],["Belvedere"],["Chopin"]),
 B("Grey Goose","France","1997","Vodka","French wheat vodka created by Sidney Frank; owned by Bacardi.",W+"Grey_Goose_(vodka)",["L'Orange","Le Citron","La Poire"],["Grey Goose"],["Bombay Sapphire"]),
 B("Tito's","United States","1997","Vodka","Corn vodka from Austin, Texas, made by Tito Beveridge's Fifth Generation, Inc.","https://en.wikipedia.org/wiki/Tito%27s_Vodka",[],["Tito's Handmade Vodka"],[]),
 B("Żubrówka","Poland","1928","Flavoured vodka","Bison grass vodka from Polmos Białystok; owned by Maspex since 2022.",W+"%C5%BBubr%C3%B3wka",["Bison Grass","Biała","Czarna"],["Żubrówka Bison Grass"],[]),
 B("Linie","Norway","1821","Aquavit","Lysholm's equator-crossing aquavit, produced by Arcus.","https://matadornetwork.com/read/norwegian-liquor-travels-world/",[],["Linie Aquavit"],["Aalborg"]),
 B("Aalborg","Denmark","1846","Aquavit","Akvavit from Isidor Henius's Aalborg factory, now produced by Arcus.","https://www.systembolaget.se/produkt/sprit/aalborg-16501/",["Taffel","Jubilæums"],["Aalborg Taffel Akvavit"],["Linie"]),
 B("O.P. Anderson","Sweden","1891","Aquavit","Swedish akvavit of O.P. Anderson & Son, Gothenburg; owned by Anora Group.",W+"O.P._Anderson",["Aquavit","Gammaldags Norrlands","Skåne"],["O.P. Anderson Aquavit"],[]),
]
notes=("All five planned kinds kept (Gin, Genever, Vodka, Flavoured vodka, Aquavit); gin and vodka styles/bases moved into 't'. "
 "Old vodka duplicates 'Alexander Vodka' / 'Alexandrion Saber Distilleries 1789 Alexander Vodka' merged. Old makerless models became versions of archetypes. "
 "Monkey 47: no Wikipedia page exists and the Pernod (theabsolutcompany.com) page returned 403; sourced from Difford's Guide, launch year left blank (not on that page). "
 "Gordon's year 1769 per its article (Gin article says 1763). Sloe gin left to the Liqueurs shelf. "
 "Genever archetypes are the legal styles (oude, jonge, korenwijn) with Bols and Zuidam bottlings as versions; no Bols Genever launch year found. "
 "Left out: Sipsmith, Nicholson's, Russian Standard, Beluga, Løiten, Lysholm, Bommerlunder (named on retrieved pages but no detail worth an archetype); Elyx and Burrough's Reserve not confirmed by retrieved pages. No traditions added (industrial spirits; genever GI noted as types).")
out={"kinds":[gin,gen,vod,fv,aq],"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/06_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
