import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,dt,a='',v=None): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
kinds=[
{"n":"Natural mineral water","a":"mineral water · eau minérale · Mineralwasser","d":"Still groundwater bottled at a protected, recognised source with its natural minerals and only minimal permitted treatment.",
 "t":["very low to high mineral content (TDS)","calcium- or magnesium-rich","sulphate-rich","low sodium","PET bottle","glass bottle","can","multipack","sports cap"],
 "s":W+"Mineral_water","x":[
 X("Evian","Low-to-medium mineral still water from springs near Évian-les-Bains on Lake Geneva; TDS 300 mg/L, pH 7.2.","Evian","1826","https://en.wikipedia.org/wiki/Evian",
   "TDS 300 mg/L · Ca 80, Mg 26, Na 6.5 mg/L · glass, PET · yearly designer limited-edition bottles",v=[
   {"n":"Glass bottle","mk":"Evian","y":"1908","d":"first glass bottles sold"},{"n":"PVC bottle","mk":"Evian","y":"1969","d":"first plastic bottle"},
   {"n":"Collapsible PET bottle","mk":"Evian","y":"1995","d":""},{"n":"Designer limited edition (Diane von Fürstenberg)","mk":"Evian","y":"2013","d":""},
   {"n":"Designer limited edition (Balmain)","mk":"Evian","y":"2022","d":""}]),
 X("Vittel","Medium-high mineral still water from the Grande Source in the Vosges spa town of Vittel; TDS 841 mg/L.","Vittel","1854","https://en.wikipedia.org/wiki/Vittel_(water)",
   "TDS 841 mg/L · Ca 202, sulphate 306, bicarbonate 402 mg/L · pH 7.5"),
 X("Contrex","Highly mineralised still water from Contrexéville, Vosges, rich in sulphate and calcium; TDS 2078 mg/L.","Contrex","","https://en.wikipedia.org/wiki/Contrex",
   "TDS 2078 mg/L · sulphate 1121, Ca 468, Mg 74.5 mg/L · pH 7.4"),
 X("Volvic","Very low mineral, silica-bearing still water filtered through volcanic rock in the Auvergne, France; TDS 109 mg/L.","Volvic","1938","https://en.wikipedia.org/wiki/Volvic_(mineral_water)",
   "TDS 109 mg/L · silica 32 mg/L · pH 7 · PET bottles",v=[{"n":"First spring tapped","mk":"Volvic","y":"1922","d":"bottles on sale from 1938"}]),
 X("Gerolsteiner Still (Naturell)","Still bottling of the very hard, bicarbonate-rich Eifel source water at Gerolstein, Germany; TDS 2,488 mg/L.","Gerolsteiner","1888","https://en.wikipedia.org/wiki/Gerolsteiner_Brunnen",
   "TDS 2488 mg/L · bicarbonate 1816, Ca 348, Mg 108 mg/L · glass and PET crates"),
 X("Highland Spring","Scottish still water from protected organic land in the Ochil Hills, bottled at Blackford, Perthshire; TDS 170 mg/L.","Highland Spring","1980","https://en.wikipedia.org/wiki/Highland_Spring",
   "TDS 170 mg/L · pH 7.8 · still, sparkling, flavoured (2024)"),
 X("Hildon Still","English natural mineral water drawn from a chalk aquifer in the Test Valley at Broughton, Hampshire; a restaurant glass-bottle staple.","Hildon","","https://hampshirefare.co.uk/member/hildon-natural-mineral-water/",
   "chalk aquifer · glass bottles · still and gently sparkling")]},
{"n":"Spring water","a":"natural spring water · source water","d":"Water from an underground formation that flows naturally to the surface, bottled at or near the spring; mineral content not fixed.",
 "t":["PET bottle","gallon jug","3- and 5-gallon cooler jug","glass bottle","carton","can"],"s":W+"Spring_water","x":[
 X("Poland Spring","American spring water first sold from the spring at Poland, Maine; now drawn from several Maine springs.","Poland Spring","1845","https://en.wikipedia.org/wiki/Poland_Spring",
   "half-pint to 5-gallon jugs · Eco-Shape bottle (30% less plastic)"),
 X("Icelandic Glacial","Naturally alkaline, very low mineral water from the Ölfus Spring in south-west Iceland; pH 8.4, TDS 72 ppm.","Icelandic Glacial","2004","https://en.wikipedia.org/wiki/Icelandic_Glacial",
   "pH 8.4 · TDS 72 ppm · PET, glass, can · still and sparkling")]},
{"n":"Purified & table water","a":"purified water · table water · drinking water · remineralised water","d":"Water, often from a municipal supply, purified by reverse osmosis, distillation or similar and sometimes remineralised for taste.",
 "t":["reverse osmosis","distilled","remineralised","PET single-serve","multipack","gallon jug","can","refill station"],"s":W+"Bottled_water",
 "m":[["Dasani","The Coca-Cola Company"],["Aquafina","PepsiCo"],["Nestlé Pure Life","Nestlé"],["Bisleri","Bisleri"]],
 "x":[X("Dasani","Coca-Cola's purified municipal water, filtered by reverse osmosis and nanofiltration with trace minerals added.","The Coca-Cola Company","1999","https://en.wikipedia.org/wiki/Dasani",
   "355 mL–1.5 L PET · aluminium can (2019) · PlantBottle · flavoured in Latin America"),
  X("Aquafina","PepsiCo's purified water from public sources treated by reverse osmosis, UV and ozone; first sold in Wichita, Kansas.","PepsiCo","1994","https://en.wikipedia.org/wiki/Aquafina","PET bottles · FlavorSplash flavoured line"),
  X("Nestlé Pure Life","Nestlé's mass-market purified water brand, launched in Pakistan and sold in about 21 countries.","Nestlé","1998","https://en.wikipedia.org/wiki/Nestl%C3%A9_Pure_Life","purified; some Canadian packs spring water")]},
{"n":"Artesian & glacier water","a":"artesian water · glacial water · iceberg water","d":"Groundwater from a confined, pressurised aquifer that rises without pumping, or water marketed as from glacial or ice sources.",
 "t":["artesian","glacial / snowmelt","square or cylindrical PET","glass"],"s":W+"Artesian_aquifer","x":[
 X("Fiji Water","Artesian water from an aquifer at Yaqara on Viti Levu, Fiji, high in silica; sold in a square bottle.","Fiji Water","1996","https://en.wikipedia.org/wiki/Fiji_Water",
   "silica 93 mg/L · TDS 222 mg/L · pH 7.3–7.7 · square PET bottle"),
 X("Voss","Norwegian still and sparkling water from Vatnestrøm, Iveland, in a cylindrical glass bottle designed by Neil Kraft; marketed as artesian, a claim disputed by TV 2 in 2010.","Voss","","https://en.wikipedia.org/wiki/Voss_(water)",
   "cylindrical glass or PET bottle · still and sparkling")]},
{"n":"Alkaline & functional water","a":"alkaline water · electrolyte water · ionised water · hydrogen water · oxygenated water","d":"Bottled water with raised pH (often by electrolysis/ionisation) or with added electrolytes, hydrogen or oxygen for claimed benefits.",
 "t":["high-pH / ionised","electrolyte-added","vapour-distilled","hydrogen-infused","oxygenated","fluoridated (infant / nursery water)"],"s":W+"Alkaline_water","x":[
 X("Smartwater","Distilled water with potassium, calcium and magnesium electrolytes added back; first sold in the US as Glacier Mineral Water.","Glacéau","1990","https://en.wikipedia.org/wiki/Smartwater",
   "electrolytes added · PET bottles · 12 oz can (2024) · sparkling flavours (2017)")]},
{"n":"Flavoured still water","a":"flavoured water · enhanced water · fruit water","d":"Non-carbonated water with added flavouring and sometimes sweeteners, juice, vitamins or minerals.",
 "t":["unsweetened","sugar-free (sweetener)","with fruit juice","vitamin-enhanced"],"s":W+"Flavored_water",
 "m":[["Volvic Touch of Fruit","Volvic"],["Volvic Juiced","Volvic"],["Aquafina FlavorSplash","PepsiCo"],["Vitaminwater","Glacéau"],["Propel","PepsiCo"],["Hint","Hint"]]},
{"n":"Packaged ice","a":"bagged ice · ice cubes · block ice · cocktail ice","d":"Ice made and sold in bags or blocks for drinks and cool boxes, from cubed and crushed to clear cocktail ice.",
 "t":["cubed","crushed","block","clear cocktail ice","dry ice (separate use)"],"s":"https://en.wikipedia.org/wiki/Reddy_Ice","m":[["Packaged ice","Reddy Ice"]]}
]
# Propel maker not on fetched page -> remove maker attribution risk
kinds[5]["m"]=[["Volvic Touch of Fruit","Volvic"],["Volvic Juiced","Volvic"],["Aquafina FlavorSplash","PepsiCo"],["Vitaminwater","Glacéau"]]
def B(n,c,f,seg,d,s,sig=(),lines=(),rel=()): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
B("Evian","France","1826","premium mineral water","Danone-owned mineral water from springs at Évian-les-Bains on Lake Geneva.","https://en.wikipedia.org/wiki/Evian",["Evian"],rel=["Volvic","Danone"]),
B("Volvic","France","1938","mineral water","Danone-owned volcanic-filtered mineral water from the Auvergne.","https://en.wikipedia.org/wiki/Volvic_(mineral_water)",["Volvic"],["Touch of Fruit","Juiced","Sparkling"],["Evian"]),
B("Vittel","France","1854","mineral water","Nestlé-owned mineral water from the Vosges spa town of Vittel.","https://en.wikipedia.org/wiki/Vittel_(water)",["Vittel"],rel=["Contrex"]),
B("Contrex","France","","mineral water","Nestlé-owned highly mineralised water from Contrexéville, Vosges.","https://en.wikipedia.org/wiki/Contrex",["Contrex"],rel=["Vittel"]),
B("Gerolsteiner","Germany","1888","mineral water","Eifel mineral water company at Gerolstein, majority owned by Bitburger Holding.","https://en.wikipedia.org/wiki/Gerolsteiner_Brunnen",["Gerolsteiner Still (Naturell)"],["Sprudel","Medium","Naturell"]),
B("Highland Spring","United Kingdom","1979","mineral water","Scottish water bottler at Blackford, Perthshire, owned by Mahdi Al Tajir.","https://en.wikipedia.org/wiki/Highland_Spring",["Highland Spring"]),
B("Hildon","United Kingdom","","premium mineral water","Hampshire natural mineral water from a chalk aquifer at Broughton, Test Valley.","https://hampshirefare.co.uk/member/hildon-natural-mineral-water/",["Hildon Still"]),
B("Poland Spring","United States","1845","spring water","Maine spring water brand, now owned by Primo Brands (BlueTriton bought it from Nestlé in 2021).","https://en.wikipedia.org/wiki/Poland_Spring",["Poland Spring"]),
B("Icelandic Glacial","Iceland","2004","premium spring water","Icelandic Water Holdings brand bottling the Ölfus Spring, founded by Jón Ólafsson.","https://en.wikipedia.org/wiki/Icelandic_Glacial",["Icelandic Glacial"]),
B("Fiji Water","Fiji / United States","1996","premium artesian water","Artesian water from Viti Levu, owned by The Wonderful Company of Los Angeles.","https://en.wikipedia.org/wiki/Fiji_Water",["Fiji Water"]),
B("Voss","Norway","","premium water","Norwegian water in a Neil Kraft cylinder bottle; Reignwood Group took majority control in 2016.","https://en.wikipedia.org/wiki/Voss_(water)",["Voss"]),
B("Glacéau","United States","","functional water","Coca-Cola subsidiary (Energy Brands) behind Smartwater and Vitaminwater.","https://en.wikipedia.org/wiki/Smartwater",["Smartwater"],["Smartwater","Vitaminwater"],["The Coca-Cola Company"]),
B("The Coca-Cola Company","United States","1892","soft drinks","Atlanta drinks multinational; owner of Dasani, Smartwater and Vitaminwater.","knowledge",["Dasani"]),
B("PepsiCo","United States","1965","soft drinks and snacks","US food and drinks multinational; owner of Aquafina.","knowledge",["Aquafina"]),
B("Nestlé","Switzerland","1866","food and drinks","Swiss food multinational; Nestlé Waters owns Vittel, Contrex and Pure Life.","knowledge",["Nestlé Pure Life"],rel=["Vittel","Contrex"]),
B("Reddy Ice","United States","1972","packaged ice","Dallas-based packaged ice maker, described as the largest in the US; began as a Southland Corporation division.","https://en.wikipedia.org/wiki/Reddy_Ice"),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Planned kinds all kept. Essentia, hydrogen-water and oxygenated-water brands left out: no retrievable page (Essentia/Nestlé pages 403/404). Hildon founding year (1989 per search snippets) left blank: not on a retrieved page. Glacier-sourced brands beyond Icelandic Glacial not found on retrieved pages. Gerolsteiner and Highland Spring sparkling bottlings belong on the Sparkling water shelf. Packaged ice kept kind-level with one maker. Bisleri listed as Indian market leader per the Bottled water article (owner not stated there)."}
p='work/J9/shelves/00_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
