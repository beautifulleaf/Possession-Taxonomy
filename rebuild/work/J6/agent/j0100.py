import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
bk=[
 A("English Breakfast","English breakfast tea","Full-bodied black blend, usually Assam, Ceylon and Kenyan, made to take milk and sugar; Keemun in dearer blends.","","1843-44 (New York merchant); 1892 (Victoria at Balmoral)",W+'English_breakfast_tea',[V("Richard Davies blend","","1843","New York blend of Congou, Pekoe and Pouchong, per one account"),V("Balmoral blend","","1892","Blend Queen Victoria tasted in Scotland")],"base: Assam, Ceylon, Kenya · cut: broken leaf · types: tea bag, loose"),
 A("Irish Breakfast","Irish blend","Strong, malty Assam-led blend, softened with Kenyan broken pekoe, drunk with milk through the day.","","",W+'Irish_breakfast_tea',[V("Barry's","Barry's Tea","1901","Cork brand named on the page"),V("Lyons","Lipton Teas and Infusions","","Irish brand named on the page"),V("Bewley's","","","Irish brand named on the page"),V("Robert Roberts","","","Republic of Ireland brand"),V("Nambarrie's","","","Northern Ireland brand"),V("Thompson's Punjana","","","Northern Ireland brand")],"base: Assam + Kenyan BP · cut: broken leaf"),
 A("Russian Caravan","","Blend of oolong, Keemun and lapsang souchong, malty and smoky; named for the 18th-century camel caravans on the Siberian Route.","","18th-century trade",W+'Russian_Caravan',[V("Yunnan variant","","","Yunnan black replaces part of the blend")],"typical: about 60% Keemun, 20% lapsang, rest roasted oolong"),
 A("East Frisian blend","Ostfriesentee · East-Frisian Blend","Strong Assam, Ceylon and Darjeeling blend served with rock candy (kluntje) and cream in East Frisia.","","",W+'Tea_culture',[],"served: kluntje + cream cloud, unstirred"),
]
kinds=[
 {"n":"Breakfast & everyday black tea","a":"builder's tea · black tea bags","d":"Blended black tea in bags or loose for daily cups with milk, bought mainly by brand.","t":["tea bag","pyramid bag","loose","decaf"],"s":W+'English_breakfast_tea',"x":bk,
  "m":[["PG Tips","Lipton Teas and Infusions"],["Yorkshire Tea","Bettys & Taylors"],["Tetley","Tata Consumer Products"],["Twinings","Associated British Foods"],["Typhoo","Supreme Imports"],["Lipton","Lipton Teas and Infusions"],["Barry's Tea","Barry's"],["Lyons","Lipton Teas and Infusions"],["Brooke Bond","Lipton Teas and Infusions"],["Red Rose","Lipton Teas and Infusions"]]},
 {"n":"Iced tea mixes & tea concentrates","a":"instant iced tea · instant tea powder","d":"Powdered instant tea, iced-tea mixes and tea concentrates to dilute; bottled ready-to-drink tea is in Soft Drinks.","t":["unsweetened instant tea","sweetened iced-tea mix","tea concentrate"],"s":W+'Instant_tea',"x":[A("Instant tea powder","soluble tea","Tea extract concentrated to about 40% solids then freeze-, spray- or vacuum-dried; first patented as a paste in 1885.","","1885 patent",W+'Instant_tea',[],"drying: freeze, spray, vacuum · additives: sugar, citric acid, flavour")]},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Twinings","United Kingdom","1706","Mainstream","Strand tea room","London tea house founded by Thomas Twining, owned by Associated British Foods since 1964.",W+'Twinings'),
 B("Tetley","United Kingdom","1837","Mainstream","tea bags","Founded by Joseph and Edward Tetley in Yorkshire; owned by Tata Consumer Products.",W+'Tetley'),
 B("PG Tips","United Kingdom","","Mainstream","pyramid bags","Brooke Bond brand from the 1930s, made by Lipton Teas and Infusions.",W+'PG_Tips'),
 B("Yorkshire Tea","United Kingdom","1977","Mainstream","hard-water blend","Brand launched in 1977 by Taylors, part of Bettys & Taylors.",W+'Yorkshire_Tea'),
 B("Typhoo","United Kingdom","1903","Mainstream","Birmingham tea","Launched by John Sumner Jr in 1903; Supreme Imports bought it in December 2024.",W+'Typhoo'),
 B("Barry's Tea","Ireland","1901","Mainstream","Irish tea","Cork company founded by James J. Barry.",W+"Barry's_Tea"),
 B("Brooke Bond","United Kingdom","1869","Mainstream","Manchester tea","Founded by Arthur Brooke; now Lipton Teas and Infusions outside India, Nepal and Indonesia.",W+'Brooke_Bond'),
 B("Red Rose Tea","Canada","1890","Mainstream","Canadian tea","Saint John, New Brunswick brand founded by Theodore Harding Estabrooks.",W+'Red_Rose_Tea'),
 B("Lipton Teas and Infusions","Netherlands","2021","Mainstream","tea group","Amsterdam company spun off from Unilever that owns Lipton, PG Tips and others.",W+'Lipton_Teas_and_Infusions'),
 B("Dilmah","Sri Lanka","","Premium","Ceylon tea","Sri Lankan tea company.","knowledge"),
 B("Bigelow","United States","","Mainstream","US tea bags","American family tea company.","knowledge"),
 B("Teekanne","Germany","","Mainstream","tea bags","German tea company; owns Red Rose in the US via Redco.","knowledge"),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"No test-winner pages retrieved (Which?, Warentest), so models are brand-level only. Left out unsourced: Scottish Breakfast, Clipper, Ahmad, Buenting, Thiele, Onno Behrends (not on retrieved pages), concentrates brands. Iced-tea mix brands not named on retrieved page."}
json.dump(out,open('01_00.src.json','w'),ensure_ascii=False)
