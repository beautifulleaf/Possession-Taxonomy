import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":q[0],"mk":(q[3] if len(q)>3 else mk),"y":q[1],"d":q[2]} for q in v],"dt":dt}
SW=["regular","diet / zero sugar","glass bottle","can","PET bottle"]
kinds=[
{"n":"Guaraná soda","a":"guaraná · refrigerante de guaraná","d":"Brazilian-style soda flavoured with the caffeine-bearing guaraná fruit.","t":SW,"s":W+"Guaraná_Antarctica","x":[
 X("Guaraná Antarctica","Brazil's leading guaraná soda, created by Pedro Baptista de Andrade for Companhia Antarctica Paulista; made by Ambev.","Guaraná Antarctica","1921",W+"Guaraná_Antarctica",
   [("Guaraná Antarctica Zero","","Brazil"),("Guaraná Antarctica Açaí","","")],"made in Brazil, Portugal, Argentina, Bolivia, Japan"),
 X("Fanta Guaraná","Brazilian regional Fanta flavour.","Fanta","",W+"Fanta",[],""),
 ],"m":[["Kuat","Coca-Cola"]]},
{"n":"Bubblegum & tutti-frutti soda","a":"champagne cola · kola champagne · cream-soda-flavoured","d":"Bright sweet sodas with bubblegum, tutti-frutti or cream-soda notes, often national icons.","t":SW+["golden / yellow","orange","red"],"s":W+"Irn-Bru","x":[
 X("Irn-Bru","Scotland's orange 'other national drink' from A.G. Barr, with a tutti-frutti, bubblegum and cream-soda flavour.","A.G. Barr","1901",W+"Irn-Bru",
   [("Diet Irn-Bru","1980","Sugar Free 2011–2025, then Diet again"),("Irn-Bru Xtra","2016","renamed Irn-Bru Zero 2025"),("Reduced-sugar reformulation","2018","UK sugar tax"),("Irn-Bru 1901","2019","original recipe; permanent 2021"),("Irn-Bru Energy","2019","")],"orange colour · glass, can, PET"),
 X("Inca Kola","Peru's golden lemon-verbena 'champagne cola', created by the Lindley family in Lima.","Inca Kola","1935",W+"Inca_Kola",
   [("Diet Inca Kola","",""),("Golden Kola","","international advertising name")],"golden yellow"),
 X("Colombiana","Postobón's cola champagne, its most popular product.","Postobón","",W+"Postobón",[],""),
 X("Big Red","Red, citrus-and-vanilla soda from Waco, Texas, first sold as Sun Tang Red Cream Soda; often taken for bubblegum.","Big Red","1937",W+"Big_Red_(drink)",[("Sun Tang Red Cream Soda","1937","original name")],"red"),
 ],"m":[["Kola Román","Kola Román"]]},
{"n":"Chinotto & bitter soda","a":"chinotto · chinò · bitter aperitivo soda · analcolico","d":"Dark bittersweet soda from myrtle-leaved orange (chinotto) or bitter herbs, including non-alcoholic red bitter aperitivo sodas.","t":["glass bottle","can","diet"],"s":W+"Chinotto_(soft_drink)","x":[
 X("Chinotto","Italian dark, bittersweet soda from Citrus myrtifolia juice, industrially produced from the 1950s.","","1950s",W+"Chinotto_(soft_drink)",
   [("Chinò","","Sanpellegrino",'Sanpellegrino'),("Brio","","Canada, sweeter",'Brio'),("Fanta Amara","","Malta",'Fanta')],"dark, cola-like colour · less sweet"),
 X("Kinnie","Maltese bittersweet soda brewed from bitter oranges and wormwood by Simonds Farsons Cisk.","Kinnie","1952",W+"Kinnie",
   [("Diet Kinnie","1984",""),("Kinnie Zest","2007","stronger orange"),("Kinnie Vita","2014","stevia")],""),
 X("Sanbittèr","Sanpellegrino's non-alcoholic red bitter aperitivo soda.","Sanpellegrino","",W+"Sanpellegrino",[],"small glass bottles"),
 ]},
{"n":"Herbal & sarsaparilla soda","a":"sarsi · sarsaparilla · herbal lemonade","d":"Sodas flavoured with sarsaparilla, gentian or Alpine herbs, distinct from cola and root beer.","t":SW,"s":W+"Sarsaparilla_(soft_drink)","x":[
 X("Sarsaparilla","Root-beer-like soda originally from Smilax vine, popular as 'sarsi' in Southeast Asia and in Australia.","","19th century",W+"Sarsaparilla_(soft_drink)",
   [("Badak","1916","Indonesia",'Badak'),("Sarsi","","Philippines, Cosmos Bottling",'Sarsi'),("HeySong Sarsaparilla","","Taiwan",'HeySong'),("F&N Sarsi","","Singapore",'F&N'),("Bundaberg Sarsaparilla","","Australia",'Bundaberg')],"",a="sarsi · sarsae"),
 X("Moxie","Bitter gentian-root soda from Lowell, Massachusetts, begun as 'Moxie Nerve Food'; Maine's official soft drink since 2005.","Moxie","1876",W+"Moxie",[("Moxie Nerve Food","1876","patent medicine")],""),
 X("Almdudler","Austrian herbal-extract lemonade, the 'national drink of Austria', launched by Erwin Klein.","Almdudler","1957",W+"Almdudler",
   [("Almdudler Light","","sugar-free"),("Almdudler Still","","uncarbonated"),("G'spritzt","","with mineral water")],""),
 X("Dandelion & Burdock","British botanical soda; botanically brewed version by Fentimans.","Fentimans","",W+"Fentimans",[],""),
 ]},
{"n":"Ramune & marble soda","a":"ramune · marble soda · Codd-neck soda","d":"Japanese lemonade-style soda sold in a Codd-neck glass bottle sealed by a marble.","t":["original (lemon-lime)","fruit flavours","glass Codd-neck bottle","plastic Codd-style bottle"],"s":W+"Ramune","x":[
 X("Ramune","Carbonated lemonade introduced in Kobe by Scottish pharmacist Alexander Cameron Sim; made by many small Japanese firms.","","1884",W+"Ramune",
   [("Original","","lemon-lime"),("Melon","",""),("Lychee","",""),("Strawberry","",""),("Yuzu","",""),("Matcha","","")],"Codd-neck bottle · 17+ flavours"),
 ]},
{"n":"Mexican & Latin American soda","a":"refresco · gaseosa · Mexican soda","d":"Fruit sodas from Mexico and Latin America, often cane-sugar sweetened in glass bottles.","t":["cane sugar","glass bottle","PET bottle","apple, tamarind, mandarin, guava, lime"],"s":W+"Jarritos","x":[
 X("Jarritos","Mexican fruit sodas in tall glass bottles, cane-sugar sweetened and lightly carbonated.","Jarritos","1950",W+"Jarritos",
   [("Tamarind","",""),("Mandarin","",""),("Lime","",""),("Guava","",""),("Mexican cola","","")],"370 and 600 mL glass · 16 flavours"),
 X("Sidral Mundet","Mexican apple soda first bottled by Arturo Mundet; made by Coca-Cola FEMSA.","Sidral Mundet","1902",W+"Sidral_Mundet",[("US introduction","1988","")],"red, green and golden apple"),
 X("Manzana Postobón","Colombian apple soda from Postobón of Medellín.","Postobón","",W+"Postobón",[],""),
 X("Mirinda","Spanish fruit soda brand, PepsiCo-owned since 1970, mostly orange.","Mirinda","1959",W+"Mirinda",[("Orange","",""),("Lemon","",""),("Apple","","")],""),
 ]},
{"n":"Cordial-based soda","a":"heritage fruit soda · British pop","d":"Heritage fruit sodas built on cordial or fruit-juice bases, such as Vimto, Tango and Ting.","t":SW,"s":W+"Vimto","x":[
 X("Vimto","Mixed-fruit drink created by John Noel Nichols as 'Vim Tonic'; sold as cordial and fizzy; an iftar favourite in Arabia.","Vimto","1908",W+"Vimto",
   [("Vim Tonic","1908","original"),("Cordial","1913",""),("Fizzy Vimto","",""),("Vimto Energy","2023","")],"cordial, can, bottle"),
 X("Tango","British orangeade launched by Corona of Porth, Wales; owned by Britvic since 1986.","Tango","1958",W+"Tango_(drink)",
   [("Orange","1958",""),("Apple","1986",""),("Cherry","1998","discontinued 2019"),("Tango Ice Blast","2004","slush")],""),
 X("Ting","Jamaican grapefruit soda made with grapefruit juice, first produced by Desnoes & Geddes.","Ting","1976",W+"Ting_(drink)",[("Pink Ting","",""),("Diet Ting","","")],""),
 X("Sinalco","German soft drink brand from Detmold, claimed as the oldest European soft-drink brand.","Sinalco","1902",W+"Sinalco",[("Orange","",""),("Cola","",""),("Zitron","","")],""),
 X("Cheerwine","Black-cherry soda from Salisbury, North Carolina.","Cheerwine","1917",W+"Cheerwine",[("Cheerwine Zero Sugar","",""),("Retro Cheerwine","","")],""),
 ]},
{"n":"Craft & prebiotic soda","a":"craft soda · gut-health soda · prebiotic pop","d":"Small-batch brewed sodas and modern low-sugar sodas marketed with prebiotic fibre or vinegar.","t":["botanically brewed","prebiotic fibre","apple cider vinegar","low sugar"],"s":W+"Olipop","x":[
 X("Bundaberg brewed soft drinks","Australian brewed soft drinks from Bundaberg, Queensland.","Bundaberg","1960",W+"Bundaberg_Brewed_Drinks",
   [("Lemon, Lime & Bitters","",""),("Pink Grapefruit","",""),("Blood Orange","",""),("Spiced Ginger Beer","2014","festive limited")],"375 ml glass, 200 ml mini cans"),
 X("Olipop","Prebiotic soda with added fibre, founded by Ben Goodwin and David Lester in Oakland.","Olipop","2018",W+"Olipop",[],"cans"),
 X("Poppi","Prebiotic soda with apple cider vinegar, founded as Mother Beverage by Allison and Stephen Ellsworth; PepsiCo-owned since 2025.","Poppi","2018",W+"Poppi_(drink)",[("Mother Beverage","2018","original name; Poppi 2020")],"cans"),
 ]},
]
def br(n,c,f,seg,d,sig,s,rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 br("Guaraná Antarctica","Brazil","1921","guaraná soda","Ambev's guaraná soda.",["Guaraná Antarctica"],W+"Guaraná_Antarctica"),
 br("A.G. Barr","United Kingdom","","soft drinks","Glasgow soft-drinks maker of Irn-Bru and cream soda.",["Irn-Bru"],W+"Irn-Bru"),
 br("Inca Kola","Peru","1935","champagne cola","Peruvian golden soda, co-owned by Coca-Cola and the Lindley family.",["Inca Kola"],W+"Inca_Kola"),
 br("Postobón","Colombia","1904","soft drinks","Medellín soft-drinks maker owned by Grupo Mariposa.",["Colombiana","Manzana Postobón"],W+"Postobón"),
 br("Big Red","United States","1937","regional soda","Austin, Texas soda company.",["Big Red"],W+"Big_Red_(drink)"),
 br("Kinnie","Malta","1952","bitter soda","Maltese bitter-orange soda by Simonds Farsons Cisk.",["Kinnie"],W+"Kinnie"),
 br("Moxie","United States","1876","heritage soda","New England gentian soda, owned by Coca-Cola since 2018.",["Moxie"],W+"Moxie"),
 br("Almdudler","Austria","1957","herbal lemonade","Austrian herbal soft drink founded by Erwin Klein.",["Almdudler"],W+"Almdudler"),
 br("Jarritos","Mexico","1950","fruit soda","Mexican fruit sodas founded by Francisco Hill, owned by Novamex.",["Jarritos"],W+"Jarritos"),
 br("Sidral Mundet","Mexico","1902","apple soda","Mexican apple soda made by Coca-Cola FEMSA.",["Sidral Mundet"],W+"Sidral_Mundet"),
 br("Mirinda","Spain","1959","fruit soda","PepsiCo fruit-soda brand.",["Mirinda"],W+"Mirinda"),
 br("Vimto","United Kingdom","1908","cordial and soda","Nichols plc mixed-fruit drink brand.",["Vimto"],W+"Vimto"),
 br("Tango","United Kingdom","1958","fruit soda","Britvic fruit soda known for 'You know when you've been Tango'd'.",["Tango"],W+"Tango_(drink)"),
 br("Ting","Jamaica","1976","grapefruit soda","Jamaican grapefruit soda owned by Pepsi-Cola Jamaica.",["Ting"],W+"Ting_(drink)"),
 br("Sinalco","Germany","1902","soft drinks","Detmold soft-drinks brand born from Bilz Brause.",["Sinalco"],W+"Sinalco"),
 br("Cheerwine","United States","1917","cherry soda","Carolina Beverage Corporation's black-cherry soda.",["Cheerwine"],W+"Cheerwine"),
 br("Bundaberg","Australia","1960","brewed soft drinks","Bundaberg Brewed Drinks, family firm of Bundaberg, Queensland.",["Bundaberg brewed soft drinks"],W+"Bundaberg_Brewed_Drinks"),
 br("Olipop","United States","2018","prebiotic soda","Oakland prebiotic soda maker.",["Olipop"],W+"Olipop",["Poppi"]),
 br("Poppi","United States","2018","prebiotic soda","Texas prebiotic soda brand, owned by PepsiCo since 2025.",["Poppi"],W+"Poppi_(drink)",["Olipop"]),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"All eight planned kinds are new. Thums Up and Afri-Cola already sit on the Cola kind (shelf 01_00), so not duplicated. Kola champagne page 404; covered via Inca Kola and Postobón's Colombiana, with Kola Román as a flat model. Kuat kept as a flat model (named on the Guaraná Antarctica page). Bundaberg ginger beer left to the Mixers/Fermented shelves. Sarsaparilla versions point to brands without register entries (Badak, Sarsi, HeySong, F&N) as stubs for the register later."}
p='/home/user/Possession-Taxonomy/rebuild/work/J9/shelves/01_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
