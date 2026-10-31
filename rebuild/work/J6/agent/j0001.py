import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
esp=[
 A("Mocha-Java","Mocha Java · Java-Mocha","Traditional blend pairing Yemeni Mocha beans with Javanese beans; the oldest named coffee blend.","","",W+'Mocha_coffee_bean',[V("Yemen Mocha","","","Small, hard olive-to-yellow beans from Jabal Haraz, Al Udayn and Taiz"),V("Java estate coffee","","","Heavy-bodied, sweet; see Coffee production in Indonesia")],"components: Mocha + Java · body heavy, sweet"),
 A("Classic Italian espresso blend","Italian espresso","Dark-ish arabica (often with robusta) blend sold by Italian houses for moka pot and espresso machine.","","",W+'Lavazza',[V("Lavazza Qualità Oro","Lavazza","","Named product in the Lavazza range"),V("Lavazza Super Crema","Lavazza","","Named product in the Lavazza range"),V("Lavazza Qualità Rossa","Lavazza","","Named product in the Lavazza range")],"roast: medium to dark · beans: arabica with robusta · pack: beans, ground, cans"),
 A("illy blend","illy classic","Single house arabica blend from many origins, sold in pressurised steel cans in medium, dark and decaf roasts.","illy","1933",W+'Illycaff%C3%A8',[],"roasts: medium, dark, decaf · pack: pressurised tin"),
]
reg=[
 A("Turkish coffee","Türk kahvesi · Greek coffee","Very fine coffee boiled in a cezve and served unfiltered; on UNESCO's intangible heritage list.","","c.1554 (first Istanbul coffeehouse)",W+'Turkish_coffee',[],"vessel: cezve · grind: powder-fine · sweetness: unsweetened to very sweet"),
 A("Arabic coffee (qahwa)","qahwa · Gulf coffee · Levantine coffee","Lightly to heavily roasted arabica boiled and often flavoured with cardamom, served unsweetened in small cups.","","mid-15th century",W+'Arabic_coffee',[V("Gulf style","","","Very light roast with saffron and cardamom, yellow colour"),V("Northern Arabia qahwah shamāliyya","","","Darker roast"),V("Qahwa murra","","","Coarse grounds with whole cardamom, brewed for hours"),V("Yemeni hawaij coffee","","","Brewed with hawaij spice blend")],"vessel: dallah · roast 165-210 C · spice: cardamom, saffron"),
 A("Vietnamese phin coffee","cà phê phin · Vietnamese iced coffee","Dark-roast Vietnamese robusta dripped through a metal phin, usually over condensed milk.","Trung Nguyên","",W+'Vietnamese_iced_coffee',[V("Trung Nguyên G7","Trung Nguyên","2003","Most successful product of the group"),V("Trung Nguyên Legendee","Trung Nguyên","","Simulated kopi luwak made with enzymes")],"species: robusta · filter: phin · milk: condensed"),
 A("New Orleans coffee and chicory","café au lait blend","Dark roast blended with chicory root, a tradition dating to the Civil War blockade.","Café du Monde","1862",W+'Caf%C3%A9_du_Monde',[V("Café du Monde tin","Café du Monde","","Orange-yellow tin sold across US grocery markets since the early 1990s")],"blend: coffee + chicory · served au lait"),
 A("Spanish torrefacto","torrefacto · cafe torrefacto","Beans roasted with added sugar, blended with ordinary roast; used in Spain and parts of Latin America.","","1920s",W+'Torrefacto',[],"sugar-coated roast · countries: Spain, Portugal, Mexico, Costa Rica, others"),
]
dec=W+'Decaffeination'
kinds=[
 {"n":"Espresso blends","a":"espresso roast · house espresso","d":"Blends roasted for espresso, as named patterns from Mocha-Java to Italian house blends.","s":W+'Mocha_coffee_bean',"x":esp},
 {"n":"Everyday ground & filter coffee","a":"supermarket coffee · roast and ground","d":"Ground or bagged coffee for filter and drip machines, bought on brand and price.","t":["roast and ground","whole bean","pods compatible"],"s":W+'Folgers',
  "m":[["Folgers","J.M. Smucker"],["Maxwell House","Kraft Heinz"],["Maxwell House (outside North America)","JDE Peet's"],["Douwe Egberts","JDE Peet's"],["Jacobs","JDE Peet's"],["Kenco","JDE Peet's"],["Lavazza Qualità Rossa","Lavazza"]]},
 {"n":"Decaffeinated coffee","a":"decaf","d":"Coffee with caffeine removed by water, solvent or supercritical CO2.","t":["Swiss Water process","supercritical CO2","ethyl acetate","dichloromethane (methylene chloride)","triglyceride process"],"s":dec,"x":[
   A("Café HAG","Kaffee HAG · HAG","First commercial decaf brand, founded in Bremen by Ludwig Roselius; Sanka split from it in 1910.","Café HAG","1906",W+'Caf%C3%A9_HAG',[V("Sanka","","1910","US/French spin-off from HAG"),V("HAG under JDE Peet's","JDE Peet's","2015","Current owner")],"process: solvent decaf (Roselius patent 1906)"),
   A("Swiss Water decaf","Swiss Water Process","Solvent-free decaf using green coffee extract and charcoal filters; commercialised by Coffex in 1980.","Swiss Water Company","1933 developed; 1980 commercial",dec,[V("Swiss Water Company, Burnaby","Swiss Water Company","1988","Commercial plant in British Columbia")],"process: water + activated carbon, 8-10 hours")]},
 {"n":"Traditional regional coffee","a":"regional coffee styles","d":"Coffee styles tied to a place and method, such as Turkish, Arabic, Vietnamese phin or New Orleans chicory blends.","s":W+'Turkish_coffee',"x":reg},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Lavazza","Italy","1895","Mainstream","Italian espresso","Turin family-owned roaster, founded by Luigi Lavazza.",W+'Lavazza'),
 B("illy","Italy","1933","Premium","single blend","Trieste roaster founded by Francesco Illy, known for pressurised tins.",W+'Illycaff%C3%A8'),
 B("Folgers","United States","1850","Mainstream","American canned coffee","San Francisco origin; owned by J.M. Smucker since 2008.",W+'Folgers'),
 B("Maxwell House","United States","1892","Mainstream","Nashville blend","Founded by Joel Owsley Cheek; Kraft Heinz in North America, JDE Peet's elsewhere.",W+'Maxwell_House'),
 B("Douwe Egberts","Netherlands","1753","Mainstream","Dutch coffee","Dutch brand from a 1752 Joure grocery; part of JDE Peet's.",W+'Douwe_Egberts'),
 B("Café HAG","Germany","1906","Specialist","decaf","Bremen decaf pioneer founded by Ludwig Roselius.",W+'Caf%C3%A9_HAG'),
 B("Trung Nguyên","Vietnam","1996","Mainstream","Vietnamese robusta","Buôn Ma Thuột group behind G7 instant and Legendee.",W+'Trung_Nguy%C3%AAn'),
 B("Café du Monde","United States","1862","Heritage manufactory","chicory coffee","New Orleans coffee stand selling chicory coffee in tins.",W+'Caf%C3%A9_du_Monde'),
 B("Jacobs","Germany","","Mainstream","German filter coffee","JDE Peet's brand.","knowledge"),
 B("Kenco","United Kingdom","","Mainstream","British coffee","JDE Peet's brand.","knowledge"),
 B("Tchibo","Germany","1949","Mainstream","coffee retailer","Hamburg coffee retailer and roaster.","knowledge"),
 B("Melitta","Germany","1908","Mainstream","paper filters and coffee","Melitta Bentz invented the paper coffee filter in 1908.","knowledge"),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"No test-winner data (Which?, Warentest, CHOICE, CR) retrieved, so everyday coffee lists brands only at brand level (no invented SKUs). Left out unsourced: Kimbo, Starbucks Espresso Roast, Square Mile Red Brick, Black Cat, Kurukahveci Mehmet Efendi facts (not on page; mentioned as a note), Cuban-style, Nanyang kopi, cafe de olla, Dallmayr Prodomo, Paulig, Lofbergs, Peet's, Cafe Bustelo, Segafredo (page is a disambiguation). Decaf Mountain Water not on retrieved page."}
json.dump(out,open('00_01.src.json','w'),ensure_ascii=False)
