import json, os, sys
sys.path.insert(0,"/home/user/Possession-Taxonomy/rebuild/work/J9/agent"); from segfix import fix
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":q[0],"mk":(q[3] if len(q)>3 else mk),"y":q[1],"d":q[2]} for q in v],"dt":dt}
PK=["glass bottle (150–200 ml)","can","PET bottle","multipack"]
kinds=[
{"n":"Tonic water","a":"tonic · Indian tonic · quinine water","d":"Carbonated soft drink flavoured with bitter quinine, mainly drunk as a mixer with gin.","t":["Indian (classic)","light / slimline","aromatic","Mediterranean","floral (elderflower)","high-quinine"]+PK,"s":W+"Tonic_water","x":[
 X("Quinine Tonic Water (Pitt & Co.)","The first commercial tonic water, patented by Erasmus Bond of Pitt & Co., London.","","1858",W+"Tonic_water",[],"historic"),
 X("Schweppes Tonic Water","Schweppes' carbonated tonic, described as the first carbonated tonic.","Schweppes","1871",W+"Schweppes",[],"glass, can, PET · regular and diet"),
 X("Fever-Tree Indian Tonic Water","Premium tonic, Fever-Tree's first product, which spawned a family of flavoured tonics.","Fever-Tree","2005",W+"Fever-Tree",
   [("Mediterranean Tonic Water","2012","sofi award year"),("Elderflower Tonic Water","",""),("Aromatic Tonic Water","","")],"200 ml glass, cans"),
 X("Q Tonic","American tonic sweetened only with organic agave nectar, with cinchona-bark quinine.","Q Mixers","",W[:0]+"https://www.wholefoodsmarket.com/tips-and-ideas/archive/q-drinks",[],"",a="Q Drinks"),
 X("Thomas Henry Tonic Water","Premium mixer brand 'born in bars', making mixers, sodas and lemonades with bartenders.","Thomas Henry","",
   "https://www.thomas-henry.com/about-us/",[],""),
 X("Franklin & Sons Tonic","Premium tonic and mixer brand established by the Franklin family.","Franklin & Sons","1886","https://globalbrands.co.uk/our-brands/franklin-sons/",[],""),
 X("1724 Tonic Water","Premium tonic in 20 cl bottles, named after an Andean elevation of 1,724 m, with cinchona-bark quinine.","1724","","https://bottleofitaly.com/en/products/acqua-tonica-1724-confezione-20cl-x-24-bottiglie",[],"20 cl glass"),
 ]},
{"n":"Ginger beer","a":"ginger beer · brewed ginger beer","d":"Cloudy, strongly gingery sweet soda, traditionally brewed with ginger, yeast and sugar, now often just carbonated.","t":["brewed","carbonated","spiced","diet / zero"]+PK,"s":W+"Ginger_beer","x":[
 X("Fentimans Traditional Ginger Beer","Botanically brewed ginger beer from the 1905 Fentimans recipe, fermented before bottling.","Fentimans","1905",W+"Fentimans",[],"glass bottle"),
 X("Bundaberg Ginger Beer","Australian brewed ginger beer from Bundaberg, Queensland.","Bundaberg","",W+"Bundaberg_Brewed_Drinks",[("Spiced Ginger Beer","2014","festive limited")],"375 ml glass, mini cans"),
 X("Old Jamaica Ginger Beer","Jamaican ginger beer from Desnoes & Geddes.","Old Jamaica","",W+"Ginger_beer",[],""),
 X("Fever-Tree Ginger Beer","Premium mixer ginger beer.","Fever-Tree","",W+"Fever-Tree",[],""),
 ],"m":[["Reed's Ginger Beer","Reed's"],["Barritt's Ginger Beer","Barritt's"]]},
{"n":"Ginger ale","a":"ginger ale · dry ginger","d":"Clear ginger-flavoured soda, either sweet and spicy (golden) or pale and mild (dry).","t":["golden","dry / pale dry","diet / zero"]+PK,"s":W+"Ginger_ale","x":[
 X("Golden ginger ale","The older, darker, sweeter and spicier style, credited to Thomas Joseph Cantrell of Belfast.","","1850s",W+"Ginger_ale",[("Vernors","1866","Detroit; 'barrel aged'",'Vernors')],""),
 X("Vernors","Golden ginger ale from Detroit pharmacist James Vernor, sold as 'Barrel Aged 3 Years'.","Vernors","1866",W+"Vernors",[("Vernors 1-Calorie (Zero Sugar)","1962",""),("Black Cherry","2022","limited, Michigan")],""),
 X("Canada Dry Pale Dry Ginger Ale","The original dry ginger ale, created by John J. McLaughlin in Toronto.","Canada Dry","1904",W+"Canada_Dry",[("Canada Dry Pale Ginger Ale patent","1905",""),("Map-of-Canada label","1907","")],""),
 X("Schweppes Ginger Ale","Schweppes' dry ginger ale.","Schweppes","1870",W+"Schweppes",[],""),
 X("Fever-Tree Ginger Ale","Premium mixer ginger ale.","Fever-Tree","",W+"Fever-Tree",[("Refreshingly Light Ginger Ale","2019","")],""),
 ]},
{"n":"Soda water & club soda","a":"soda water · club soda · soda","d":"Carbonated water sold as a mixer; club soda has added mineral salts such as sodium bicarbonate.","t":["soda water","club soda (added minerals)"]+PK,"s":W+"Club_soda","x":[
 X("Schweppes Soda Water","Schweppes' original product, the first commercial carbonated water, made by Johann Jacob Schweppe in Geneva.","Schweppes","1783",W+"Schweppes",[],""),
 X("C&C Club Soda","The original trademarked club soda, made by Cantrell & Cochrane in Dublin.","C&C","1877",W+"Club_soda",[],""),
 X("Q Club","Club soda made with Himalayan salt.","Q Mixers","","https://www.wholefoodsmarket.com/tips-and-ideas/archive/q-drinks",[],""),
 ]},
{"n":"Bitter lemon & citrus mixer","a":"bitter lemon · bitter lime","d":"Quinine-bitter soda with lemon juice, pith and peel, drunk alone or as a mixer.","t":["bitter lemon","bitter lime"]+PK,"s":W+"Bitter_lemon","x":[
 X("Schweppes Bitter Lemon","Schweppes' bitter lemon, the best-known brand of the drink.","Schweppes","1957",W+"Bitter_lemon",[],""),
 ],"m":[["Fever-Tree Bitter Lemon","Fever-Tree"],["Canada Dry Bitter Lemon","Canada Dry"],["Krest Bitter Lemon","Krest"]]},
{"n":"Cocktail mix","a":"drink mixer · Bloody Mary mix · margarita mix · sweet and sour","d":"Ready-made non-alcoholic bases that supply the flavour, sweetness and sourness of a cocktail.","t":["Bloody Mary","margarita","sweet & sour","mojito","piña colada","daiquiri","liquid","powder"],"s":W+"Sour_mix",
 "x":[X("Sour mix","Lemon and/or lime juice with simple syrup, pre-blended for sours; also sold as powder.","","",W+"Sour_mix",[],"liquid or powder",a="sweet and sour mix")],
 "m":[["Mr & Mrs T Bloody Mary Mix","Mr & Mrs T"],["Mr & Mrs T Margarita Mix","Mr & Mrs T"],["Mr & Mrs T Sweet & Sour Mix","Mr & Mrs T"]]},
]
def br(n,c,f,seg,d,sig,s,rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 br("Schweppes","Switzerland","1783","mixers","Founded in Geneva by Johann Jacob Schweppe, moved to London in 1792; owned regionally by Coca-Cola, Suntory, Keurig Dr Pepper and Asahi.",["Schweppes Tonic Water","Schweppes Bitter Lemon"],W+"Schweppes",["Canada Dry"]),
 br("Fever-Tree","United Kingdom","2004","premium mixers","London premium mixer maker founded by Charles Rolls and Tim Warrillow.",["Fever-Tree Indian Tonic Water"],W+"Fever-Tree"),
 br("Q Mixers","United States","","premium mixers","Agave-sweetened mixers founded by Jordan Silbert.",["Q Tonic"],"https://www.wholefoodsmarket.com/tips-and-ideas/archive/q-drinks"),
 br("Thomas Henry","","","premium mixers","Mixer, soda and lemonade brand developed with bartenders.",["Thomas Henry Tonic Water"],"https://www.thomas-henry.com/about-us/"),
 br("Franklin & Sons","United Kingdom","1886","premium mixers","Premium tonic and mixer brand established by the Franklin family.",["Franklin & Sons Tonic"],"https://globalbrands.co.uk/our-brands/franklin-sons/"),
 br("1724","","","premium tonic","Premium tonic water named after an Andean elevation.",["1724 Tonic Water"],"https://bottleofitaly.com/en/products/acqua-tonica-1724-confezione-20cl-x-24-bottiglie"),
 br("Fentimans","United Kingdom","1905","botanically brewed soft drinks","Hexham maker of botanically brewed drinks.",["Fentimans Traditional Ginger Beer"],W+"Fentimans"),
 br("Bundaberg","Australia","1960","brewed soft drinks","Bundaberg Brewed Drinks of Queensland.",["Bundaberg Ginger Beer"],W+"Bundaberg_Brewed_Drinks"),
 br("Old Jamaica","Jamaica","","ginger beer","Ginger beer made by Desnoes & Geddes.",["Old Jamaica Ginger Beer"],W+"Ginger_beer"),
 br("Vernors","United States","1866","golden ginger ale","Detroit golden ginger ale owned by Keurig Dr Pepper.",["Vernors"],W+"Vernors"),
 br("Canada Dry","Canada","1904","ginger ale and mixers","Toronto-born dry ginger ale brand owned by Keurig Dr Pepper.",["Canada Dry Pale Dry Ginger Ale"],W+"Canada_Dry",["Schweppes"]),
 br("C&C","Ireland","","soft drinks","Cantrell & Cochrane of Dublin, maker of the original trademarked club soda.",["C&C Club Soda"],W+"Club_soda"),
 br("Mr & Mrs T","United States","1960","cocktail mixes","Bloody Mary and cocktail mix brand founded by Herb and June Taylor, owned by Keurig Dr Pepper.",[],W+"Mr_&_Mrs_T"),
]
SEGX={"Fever-Tree":"Premium","Q Mixers":"Premium","Thomas Henry":"Premium","Franklin & Sons":"Premium","1724":"Premium","Vernors":"Heritage manufactory","Old Jamaica":"Mainstream"}
brands=fix(brands)
for b in brands:
    if b['n'] in SEGX: b['seg']=SEGX[b['n']]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"All six planned kinds are new. Fentimans tonic and Fever-Tree Light Tonic not confirmed on retrieved pages, left out (only Refreshingly Light Ginger Ale). Thomas Henry, Q, Franklin & Sons and 1724 sourced from maker/retailer pages with sparse facts; founding years left blank where not on the page (Thomas Henry 2010 and Q 2007 only in search snippets). 1724 maker (Seventeen Mixers per snippets) not confirmed, so brand registered under '1724'. Cocktail mixes kept as a tier list (Mr & Mrs T) plus the sour-mix pattern; alcohol-free spirits stay in J7."}
p='/home/user/Possession-Taxonomy/rebuild/work/J9/shelves/02_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
