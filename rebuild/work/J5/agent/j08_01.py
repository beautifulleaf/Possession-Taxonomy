from lib import *
def B(n,c,f,kf,d,s,seg="Mainstream",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
kinds=[
{"n":"Jam and fruit spreads","a":"preserves · conserve","d":"Fruit cooked with sugar to a spread.","t":["jam","conserve (whole fruit)","jelly (strained)","reduced sugar"],"s":W+"Fruit_preserves","m":[["Bonne Maman Strawberry Conserve","Bonne Maman"]]},
{"n":"Marmalade","a":"","d":"Citrus preserve of juice and peel boiled with sugar; British marmalade is usually Seville orange.","t":["thick cut","shred","Seville orange","lemon","three-fruit"],"s":W+"Marmalade","m":[["Robertson's Golden Shred","Robertson's"],["Frank Cooper's Oxford Marmalade","Frank Cooper's"],["Keiller Dundee Marmalade","Keiller"]]},
{"n":"Maple syrup","a":"","d":"Syrup boiled from maple sap, graded by colour and taste into Golden, Amber, Dark and Very Dark.","t":["Golden (delicate)","Amber (rich)","Dark (robust)","Very Dark (strong)"],"s":W+"Maple_syrup","m":[],
 "x":[X("Québec maple syrup","","Quebec makes about 90% of Canada's syrup and some 72% of the world's, under a supply-management system.",W+"Maple_syrup",[V("Golden","","","Over 75% light transmittance"),V("Amber","","","50-74.9%"),V("Dark","","","25-49.9%"),V("Very Dark","","","Under 25%")],"harmonised Canada-US grade",y="2025 share"),
      X("Vermont maple syrup","","Vermont, the largest US producer, adopted the harmonised grading early on 1 January 2014.",W+"Maple_syrup",[],"Grade A colour classes",y="2014")]},
{"n":"Golden syrup","a":"","d":"Pale invert sugar syrup, first canned by Lyle's in 1885.","t":["tin","squeezy bottle"],"s":W+"Golden_syrup","m":[["Lyle's Golden Syrup","Lyle's"]]},
{"n":"Molasses and treacle","a":"black treacle · blackstrap","d":"Thick dark syrup left from sugar refining, sold as molasses or black treacle.","t":["first molasses","second molasses","blackstrap","black treacle"],"s":W+"Molasses","m":[]},
{"n":"Date syrup and fruit molasses","a":"debes · silan · pekmez · petimezi","d":"Date syrup (date honey) and grape or pomegranate molasses reduced to a dark syrup.","t":["date syrup","grape molasses (pekmez, petimezi)","pomegranate molasses","carob pekmez"],"s":W+"Date_honey",
 "x":[X("Date syrup","date honey · debes · silan","Thick dark sweet syrup extracted from dates, with names debes, rub, silan and shireh khorma.",W+"Date_honey",[],"date molasses"),
      X("Pekmez and petimezi","grape molasses","Grape syrup reduced until dark and thick; pekmez in Turkey, petimezi or epsima in Greece, and pekmez can also be carob, fig or mulberry.",W+"Grape_syrup",[V("Carob pekmez"),V("Petimezi")],"grape must reduced")]},
{"n":"Agave and plant syrups","a":"","d":"Sweet syrups from agave, brown rice and other plants.","t":["agave","brown rice syrup","coconut","sorghum"],"s":W+"List_of_syrups","m":[]},
{"n":"Flavoured syrup","a":"","d":"Sugar syrup flavoured with caramel, nuts, vanilla or the like, for coffee and desserts.","t":["coffee syrup","cocktail syrup","sugar-free"],"s":W+"List_of_syrups","m":[["Monin Flavoured Syrups","Monin"],["Torani Flavoured Syrups","Torani"]]},
{"n":"Peanut butter","a":"","d":"Ground roasted peanuts as a spread.","t":["smooth","crunchy","natural (oil separates)"],"s":W+"Peanut_butter","m":[["Meridian Natural Smooth Peanut Butter","Meridian (peanut butter)"],["Skippy Creamy Peanut Butter","Skippy"],["Jif Peanut Butter","Jif"],["Peter Pan Peanut Butter","Peter Pan"]]},
{"n":"Nut and seed butters","a":"","d":"Spreads ground from almonds, cashews, hazelnuts, sesame (tahini), sunflower and other nuts and seeds.","t":["almond","cashew","tahini (sesame)","sunflower","pistachio"],"s":W+"Nut_butter","m":[]},
{"n":"Hazelnut-chocolate spread","a":"","d":"A sweet spread of hazelnuts with chocolate or cocoa.","t":["with cocoa","palm-oil free"],"s":W+"Nutella","m":[["Nutella","Nutella"]],
 "x":[X("Nutella","","Ferrero's hazelnut cocoa spread, first jar from Alba on 20 April 1964; mostly sugar and palm oil with about 13% hazelnuts.",W+"Nutella",[V("Nutella","Ferrero","1964")],"hazelnut · cocoa",mk="Ferrero",y="1964")]},
{"n":"Yeast extract spread","a":"","d":"Salty savoury spread of yeast extract: Marmite, Vegemite and their relatives.","t":["Marmite (UK)","Vegemite (Australia)","Marmite (New Zealand)"],"s":W+"Marmite",
 "x":[X("Marmite","","British yeast extract spread invented by the Marmite Food Company in 1902; owned by Unilever.",W+"Marmite",[],"yeast extract",mk="Marmite",y="1902"),
      X("Vegemite","","Australian brewers' yeast extract spread first sold in 1923; owned by Bega Group since 2017.",W+"Vegemite",[],"yeast extract",mk="Vegemite",y="1923")]},
]
brands=[
B("Bonne Maman","France","1971","preserves","French Andros brand known for fruit preserves in gingham-lidded jars.",W+"Bonne_Maman",sig=["Strawberry Conserve"]),
B("Robertson's","United Kingdom","1864","marmalade","Paisley marmalade brand known for Golden Shred, now owned by Premier Foods.",W+"Marmalade",seg="Heritage manufactory"),
B("Lyle's","United Kingdom","1885","golden syrup","Golden syrup first canned in 1885 at Abram Lyle's Plaistow refinery; now made by American Sugar Refining under the Tate & Lyle licence.",W+"Golden_syrup",seg="Heritage manufactory",sig=["Lyle's Golden Syrup"]),
B("Monin","France","1912","flavoured syrups","Bourges beverage company founded by Georges Monin in 1912; syrups from the 1920s.",W+"Monin_(company)"),
B("Torani","United States","1925","flavoured syrups","Syrup maker founded by Rinaldo and Ezilda Torre in 1925; based in San Leandro, California.","https://en.wikipedia.org/wiki/R._Torre_&_Company,_Inc."),
B("Skippy","United States","1932","peanut butter","Peanut butter introduced by Joseph Rosefield in 1932; owned by Hormel since 2013.",W+"Skippy_(peanut_butter)",sig=["Skippy Creamy Peanut Butter"]),
B("Ferrero","Italy","","hazelnut spread","Italian maker of Nutella, which it launched in 1964 in Alba.",W+"Nutella",seg="Premium",sig=["Nutella"]),
B("Marmite","United Kingdom","1902","yeast extract","British yeast extract spread, owned by Unilever since 2000.",W+"Marmite"),
B("Vegemite","Australia","1923","yeast extract","Australian yeast extract spread, owned by Bega Group since 2017.",W+"Vegemite"),
]
brands[1]["f"]="1864"
notes="Tate & Lyle black treacle, Monin/Torani products, Jif and Peter Pan models taken from retrieved brand pages, not SKUs. Meridian kept from old data. Pomegranate molasses and fruit pekmez detail limited to what the Molasses/Grape syrup pages state. Ferrero founding year left blank (not retrieved). Seville orange marmalade cited on the Marmalade page."
write("08_01",kinds,brands,[],notes)
