import json,os
W="https://en.wikipedia.org/wiki/"
ST=W+"Stout"; PO=W+"Porter_(beer)"; GU=W+"Guinness"; GI=W+"Goose_Island_Brewery"; FO=W+"Founders_Brewing_Company"
B13="https://www.bjcp.org/style/2021/13"; B15="https://www.bjcp.org/style/2021/15"; B16="https://www.bjcp.org/style/2021/16"; B20="https://www.bjcp.org/style/2021/20"; BB="https://www.bjcp.org/style/2021/beer"
def A(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=x[0],mk=x[1],y=x[2],d=x[3]) for x in v],"dt":dt}
kinds=[
{"n":"Irish stout","a":"Dry stout · Irish dry stout","d":"Black, dry, roasty ale of moderate strength, often served on nitrogen.","t":["Draught (nitrogen keg)","Widget can or bottle","Irish extra stout (stronger bottled)"],"s":BB,
 "x":[A("Guinness Draught","Dublin's draught stout, the best-selling stout worldwide; 4.1–4.3% on keg, also in widget cans and bottles.","Guinness","",GU,
   [("Guinness Original / Extra Stout","Guinness","","bottled; 4.2–6% by market; BJCP Irish extra stout example"),("Guinness 0.0","Guinness","2021","alcohol-free; announced 2020, relaunched 2021")],"keg · widget can · bottle · ABV by market"),
  A("Murphy's Irish Stout","Cork dry stout, now Heineken-owned; BJCP Irish stout example.","Murphy's","",ST),
  A("Beamish Irish Stout","Cork dry stout from Beamish and Crawford, now Heineken-owned.","Beamish and Crawford","",ST)],
 "m":[["O'Hara's Irish Stout","O'Hara's"],["Porterhouse Irish Stout","Porterhouse Brewery"],["Belhaven Black Stout","Belhaven"],["O'Hara's Leann Folláin","O'Hara's"],["Porterhouse XXXX","Porterhouse Brewery"],["Sheaf Stout",""]]},
{"n":"Sweet stout","a":"Milk stout · cream stout","d":"Dark, sweet, full stout, often made with lactose, the milk-stout type.","t":["Milk stout (lactose)","Nitro","Oyster stout"],"s":BB,
 "x":[A("Mackeson's XXX Stout","Archetypal surviving English milk stout.","Mackeson","",ST),
  A("Left Hand Milk Stout","Well-known American milk stout from Colorado.","Left Hand Brewing","",ST,[("Left Hand Milk Stout Nitro","Left Hand Brewing","","nitrogen version")] if False else []),
  A("Oyster stout","Stout brewed with or for oysters; first sold by Dunedin Brewery Company, New Zealand, in 1938.","","1938",ST,
   [("Hammerton Oyster Stout","Hammerton Brewery","1939","London, same formula"),("Marston's Oyster Stout","Marston's","","BJCP sweet stout example"),("Porterhouse Oyster Stout","Porterhouse Brewery","","Dublin")])],
 "m":[["Bristol Beer Factory Milk Stout","Bristol Beer Factory"],["Lancaster Milk Stout","Lancaster Brewery"],["Castle Milk Stout","South African Breweries"],["Firestone Nitro Merlin Milk Stout","Firestone Walker"],["Sweetheart Stout",""]]},
{"n":"Oatmeal stout","a":"","d":"Smooth, silky stout brewed with a share of oats.","s":B16,
 "x":[A("Samuel Smith Oatmeal Stout","Tadcaster stout commissioned by importer Charles Finkel after Michael Jackson's 1977 book; reference for the revival.","Samuel Smith","",ST),
  A("Maclay Original Oatmalt Stout","Early Scottish oat-malt stout from Maclay of Alloa.","Maclay","1895",ST,[("63/- Oatmeal Stout","Maclay","1909","")])],
 "m":[["Young's London Stout","Young's"],["Anderson Valley Barney Flats Oatmeal Stout","Anderson Valley"],["St-Ambroise Oatmeal Stout","St-Ambroise"],["Broughton Stout Jock","Broughton"],["Summit Oatmeal Stout","Summit"]]},
{"n":"Foreign extra stout","a":"Export stout · tropical stout","d":"Stronger stout brewed for export and tropical markets, either dry and bitter or sweet and fruity.","t":["Export (dry, bitter)","Tropical (sweet, fruity)"],"s":B16,
 "x":[A("Guinness Foreign Extra Stout","Strong export Guinness, formerly West Indies Porter then Extra Stout; about 7.5% ABV, varying by market.","Guinness","",GU,
   [("Guinness Special Export Stout","Guinness","1912","8%; commissioned by John Martin of Belgium")],"ABV 5–8% by market")],
 "m":[["Coopers Best Extra Stout","Coopers"],["The Kernel Export Stout London 1890","The Kernel"],["Lion Stout","Lion Brewery"],["Dragon Stout",""],["ABC Extra Stout",""],["Royal Extra Stout",""]]},
{"n":"Imperial stout","a":"Russian imperial stout · imperial Russian stout","d":"Very strong, intensely roasty and malty stout.","t":["Bourbon barrel-aged","Pastry / adjunct","English type","American type"],"s":BB,
 "x":[A("Courage Imperial Russian Stout","London export stout descended from Thrale's Anchor Brewery stout for Catherine II; Barclay Perkins Imperial Brown Stout, renamed 1955 under Courage.","Courage","18th century",ST,
   [("Barclay Perkins Imperial Brown Stout","Barclay Perkins","1781","name after the brewery changed hands"),("Courage Imperial Russian Stout","Courage","1955","brewed sporadically until 1993")]),
  A("Samuel Smith Imperial Stout","English imperial stout first brewed for US export.","Samuel Smith","early 1980s",ST),
  A("Bourbon County Brand Stout","Imperial stout aged in used bourbon barrels, the pioneer of barrel-aged stout; first brewed 1992 (perhaps 1995) by Greg Hall.","Goose Island","1992",GI,[],"annual release · variant series"),
  A("Kentucky Breakfast Stout","Imperial stout with coffee and chocolate aged in bourbon barrels in former gypsum mines.","Founders","",FO,[("Canadian Breakfast Stout","Founders","","11.7%; irregular, December release since 2023")]),
  A("Old Rasputin","Californian Russian imperial stout.","North Coast Brewing","",ST),
  A("Yeti Imperial Stout","Denver imperial stout.","Great Divide","",ST,[("Oak Aged Yeti","Great Divide","","oak-aged")]),
  A("Wiibroe Imperial Stout","Danish imperial stout launched at 8.2%.","Wiibroe","1930",ST)],
 "m":[["Bell's Expedition Stout","Bell's"],["Oskar Blues Ten Fidy","Oskar Blues"],["Sierra Nevada Narwhal","Sierra Nevada"],["Three Floyds Dark Lord","Three Floyds"],["Thornbridge Saint Petersburg","Thornbridge"],["Le Coq Imperial Extra Double Stout","Le Coq"]]},
{"n":"English porter","a":"London porter · brown porter","d":"Brown to dark British ale with chocolate and caramel malt.","s":BB,
 "x":[A("Fuller's London Porter","Chiswick porter, multiple International Beer and Cider Competition medal winner.","Fuller's","",PO),
  A("Samuel Smith Taddy Porter","Tadcaster porter; BJCP English porter example.","Samuel Smith","",B13),
  A("Guinness West Indies Porter","Revival of an 1801 Guinness porter recipe at 6%.","Guinness","2014",GU)],
 "m":[["Bateman's Salem Porter","Bateman's"],["Burton Bridge Burton Porter","Burton Bridge"],["Nethergate Old Growler Porter","Nethergate"],["RCH Old Slug Porter","RCH"],["Wickwar Station Porter","Wickwar Brewery"],["Timothy Taylor Porter","Timothy Taylor"]]},
{"n":"American porter","a":"Robust porter","d":"Dark, roasty, hoppier American ale of the porter type.","s":BB,
 "x":[A("Anchor Porter","San Francisco porter that led the American revival; brewed from 1972, bottled 1974.","Anchor Brewing","1972",PO),
  A("Black Butte Porter","Oregon porter; BJCP American porter example.","Deschutes","",B20),
  A("Edmund Fitzgerald Porter","Cleveland robust porter; BJCP American porter example.","Great Lakes Brewing","",B20),
  A("Founders Porter","Year-round Michigan porter, 6.5% ABV.","Founders","",FO)],
 "m":[["Bell's Porter","Bell's"],["Sierra Nevada Porter","Sierra Nevada"],["Smuttynose Robust Porter","Smuttynose"]]},
{"n":"American stout","a":"","d":"Roasty, hop-forward American take on stout, stronger than Irish stout.","s":B20,
 "m":[["Deschutes Obsidian Stout","Deschutes"],["Sierra Nevada Stout","Sierra Nevada"],["Bell's Kalamazoo Stout","Bell's"],["Avery Out of Bounds Stout","Avery"],["Trillium Secret Stairs","Trillium"]]},
]
K="knowledge"
def Br(n,c,f,seg,d,sig,s=K,rel=()):
    o={"n":n,"c":c,"seg":seg,"d":d,"sig":sig,"s":s}
    if f:o["f"]=f
    if rel:o["rel"]=list(rel)
    return o
brands=[
Br("Guinness","Ireland","1759","Stout brewer","Arthur Guinness's St. James's Gate brewery in Dublin, now owned by Diageo.",["Guinness Draught","Guinness Foreign Extra Stout"],GU),
Br("Murphy's","Ireland","1856","Stout brewer","Cork stout brand, now owned by Heineken.",["Murphy's Irish Stout"],K,["Beamish and Crawford"]),
Br("Beamish and Crawford","Ireland","1792","Stout brewer","Cork brewer of Beamish stout, brand now owned by Heineken.",["Beamish Irish Stout"]),
Br("Mackeson","United Kingdom","","Milk stout brand","English milk stout brand.",["Mackeson's XXX Stout"]),
Br("Left Hand Brewing","United States","1993","Craft brewery","Longmont, Colorado, brewery known for its milk stout.",["Left Hand Milk Stout"]),
Br("Samuel Smith","United Kingdom","1758","Independent brewery","Tadcaster, Yorkshire, brewery of the Old Brewery.",["Samuel Smith Oatmeal Stout","Samuel Smith Taddy Porter","Samuel Smith Imperial Stout"]),
Br("Maclay","United Kingdom","","Historic brewery","Brewery of Alloa, Scotland, early maker of oat-malt stout.",["Maclay Original Oatmalt Stout"],ST),
Br("Courage","United Kingdom","1787","Historic London brewer","London brewer that took over Barclay Perkins and its imperial stout.",["Courage Imperial Russian Stout"],K,["Barclay Perkins"]),
Br("Goose Island","United States","1988","Craft brewery (AB InBev)","Chicago brewpub founded by John Hall; bought by AB InBev in 2011.",["Bourbon County Brand Stout"],GI),
Br("Founders","United States","1996","Craft brewery","Grand Rapids, Michigan, brewery majority-owned by Mahou San Miguel.",["Kentucky Breakfast Stout","Founders Porter"],FO),
Br("North Coast Brewing","United States","1988","Craft brewery","Fort Bragg, California, brewery.",["Old Rasputin"]),
Br("Great Divide","United States","1994","Craft brewery","Denver, Colorado, brewery.",["Yeti Imperial Stout"]),
Br("Wiibroe","Denmark","","Brewery (Carlsberg)","Danish brewery whose imperial stout is now made by Carlsberg.",["Wiibroe Imperial Stout"],ST),
Br("Fuller's","United Kingdom","1845","Brewery (Asahi)","Griffin Brewery, Chiswick, London; brewing business owned by Asahi since 2019.",["Fuller's London Porter"]),
Br("Anchor Brewing","United States","1896","Craft brewery","San Francisco brewery that pioneered the US craft revival.",["Anchor Porter"]),
Br("Deschutes","United States","1988","Craft brewery","Bend, Oregon, brewery.",["Black Butte Porter"]),
Br("Great Lakes Brewing","United States","1988","Craft brewery","Cleveland, Ohio, brewery.",["Edmund Fitzgerald Porter"]),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Kept all 5 old kinds; added Oatmeal stout, Foreign extra stout (planned) and American stout (BJCP 20B, enthusiasts expect it). Irish extra stout and tropical stout folded in as types. Baltic porter left to the dark-lager shelf. Barrel-aged is a type of imperial stout. Bourbon County variant names (Coffee etc.) left out: not on any retrieved page. Beers named only in BJCP lists stay in m; no traditions apply (brewing styles, not artisan crafts)."}
p="/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/04_03.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
