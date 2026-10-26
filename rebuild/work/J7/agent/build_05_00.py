import json, os
P='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/05_00.json'
WP='https://en.wikipedia.org/wiki/'
def v(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
def x(n,a,d,mk,y,s,vs,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":vs,"dt":dt}
DT="age statement · cask type and finish · ABV (standard or cask strength) · bottle size"
def ages(mk,base,lst): return [v(f"{base} {a}",mk,"",d) for a,d in lst]

sm={"n":"Single malt Scotch whisky","a":"Single malt · Malt whisky",
 "d":"Scotch distilled at one distillery from malted barley only in pot stills, aged at least three years in oak.",
 "t":["Speyside","Highland","Islands (Highland subregion)","Islay","Lowland","Campbeltown","Peated","Unpeated","Sherry cask","Bourbon cask","Cask strength","Independent bottling"],
 "s":"https://www.thewinereserve.co.uk/spirits/whiskies",
 "x":[
  x("Glenfiddich 12","Glenfiddich Original Twelve","Speyside single malt from William Grant's Dufftown distillery; the best-known entry single malt.","Glenfiddich","1886 (distillery)",WP+"Glenfiddich_distillery",
    [v("Glenfiddich 12 Year Old","Glenfiddich","","Original Twelve"),v("Glenfiddich 14 Year Old Bourbon Barrel Reserve","Glenfiddich"),
     v("Glenfiddich 15 Year Old Solera","Glenfiddich","","solera vat"),v("Glenfiddich 18 Year Old Small Batch","Glenfiddich"),
     v("Glenfiddich 21 Year Old","Glenfiddich","","Caribbean rum cask finish")],DT),
  x("The Macallan Sherry Oak","Macallan 12 Sherry Oak · Macallan 18","Speyside malt matured only in sherry-seasoned oak; the reference sherried single malt.","The Macallan","1824 (distillery)",WP+"The_Macallan_distillery",
    [v("The Macallan 12 Years Old Sherry Oak","The Macallan"),v("The Macallan 18 Years Old Sherry Oak","The Macallan"),
     v("The Macallan 25 Years Old Sherry Oak","The Macallan"),v("The Macallan Double Cask 12","The Macallan","","sherry and American oak; also Gold, 15, 18, 30"),
     v("The Macallan Triple Cask Matured 12","The Macallan","2018","formerly Fine Oak"),v("The Macallan Rare Cask","The Macallan")],DT),
  x("The Glenlivet 12","Glenlivet 12","Speyside single malt from the first licensed distillery in the glen; a soft, fruity benchmark.","The Glenlivet","1824 (distillery)",WP+"The_Glenlivet_distillery",
    [v("The Glenlivet 12 Year Old","The Glenlivet"),v("The Glenlivet 15 Year Old French Oak Reserve","The Glenlivet"),
     v("The Glenlivet Nàdurra 16 Year Old","The Glenlivet","","cask strength"),v("The Glenlivet 18 Year Old","The Glenlivet"),
     v("The Glenlivet Batch Reserve 18 YO","The Glenlivet"),v("The Glenlivet Archive 21 Year Old","The Glenlivet"),v("The Glenlivet XXV 25 Year Old","The Glenlivet")],DT),
  x("Lagavulin 16","","Heavily peated Islay malt aged 16 years; Diageo Classic Malt and a reference smoky whisky.","Lagavulin","1816 (distillery)",WP+"Lagavulin_distillery",
    [v("Lagavulin 16 Year Old","Lagavulin","","43% ABV standard bottling"),v("Lagavulin 8 Year Old","Lagavulin"),
     v("Lagavulin 12 Year Old","Lagavulin","","cask strength"),v("Lagavulin Distillers Edition","Lagavulin","","sherry finish"),
     v("Lagavulin Offerman Edition","Lagavulin","","11 years old")],DT),
  x("Laphroaig 10","","Medicinal, heavily peated Islay malt; the distillery's standard ten-year-old.","Laphroaig","1815 (distillery)",WP+"Laphroaig_distillery",
    [v("Laphroaig 10 Year Old","Laphroaig","","40% or 43% ABV"),v("Laphroaig 10 Year Old Cask Strength","Laphroaig"),
     v("Laphroaig Quarter Cask","Laphroaig","","small-cask finish, 48% ABV"),v("Laphroaig Triple Wood","Laphroaig"),
     v("Laphroaig Lore","Laphroaig"),v("Laphroaig Càirdeas","Laphroaig","","annual release"),v("Laphroaig 25 Year Old","Laphroaig")],DT),
  x("Ardbeg Ten","Ardbeg 10 · Ardbeg Uigeadail","Peaty Islay malt; the Ten is the core bottling, Uigeadail its sherried cask-strength partner.","Ardbeg","1815 (distillery)",WP+"Ardbeg_distillery",
    [v("Ardbeg TEN","Ardbeg"),v("Ardbeg Uigeadail","Ardbeg"),v("Ardbeg Corryvreckan","Ardbeg"),v("Ardbeg An Oa","Ardbeg"),
     v("Ardbeg Wee Beastie","Ardbeg"),v("Ardbeg 25 YO","Ardbeg")],DT),
  x("Talisker 10","","Peppery, maritime Isle of Skye malt; the island's long-standing distillery bottling.","Talisker","1830 (distillery)",WP+"Talisker_distillery",
    [v("Talisker 10 Year Old","Talisker"),v("Talisker 8 Year Old Cask Strength","Talisker","","periodic release"),
     v("Talisker 18 Year Old","Talisker"),v("Talisker 25 Year Old","Talisker")],DT),
  x("Highland Park 12","Highland Park 12 · Highland Park 18","Orkney malt from Kirkwall with heather-peat smoke and sherry-cask sweetness.","Highland Park","1798 (distillery)",WP+"Highland_Park_distillery",
    [v("Highland Park 12 Year Old","Highland Park"),v("Highland Park 10","Highland Park"),v("Highland Park 15","Highland Park"),
     v("Highland Park 18","Highland Park"),v("Highland Park 21 YO","Highland Park"),v("Highland Park 25","Highland Park")],DT),
  x("Springbank 10","","Campbeltown malt made entirely on site, from floor maltings to bottling, by a family firm.","Springbank","1828 (distillery)",WP+"Springbank_distillery",
    [v("Springbank 10 Year Old","Springbank"),v("Springbank 12 Year Old Cask Strength","Springbank"),v("Springbank 15 Year Old","Springbank"),
     v("Springbank 18 Year Old","Springbank"),v("Springbank 21 Year Old","Springbank"),
     v("Longrow","Springbank","","heavily peated"),v("Longrow 18 Year Old","Springbank"),
     v("Hazelburn 10 Year Old","Springbank","","triple distilled, unpeated")],DT),
  x("The Balvenie DoubleWood","Balvenie 12 DoubleWood","Speyside malt aged in bourbon casks then finished in sherry casks; pioneer of cask finishing.","The Balvenie","1892 (distillery)",WP+"Balvenie_distillery",
    [v("The Balvenie DoubleWood 12 Year Old","The Balvenie"),v("The Balvenie Caribbean Cask 14 Year Old","The Balvenie"),
     v("The Balvenie French Oak 16 Year Old","The Balvenie"),v("The Balvenie PortWood 21 Year Old","The Balvenie"),
     v("The Balvenie Single Barrel 12","The Balvenie"),v("The Balvenie Thirty","The Balvenie")],DT),
  x("Glenmorangie Original","Glenmorangie 10","Light, floral Highland malt from Tain's tall stills, matured in bourbon casks; base of a finishing range.","Glenmorangie","1843 (distillery)",WP+"Glenmorangie_distillery",
    [v("Glenmorangie The Original","Glenmorangie","","ex-bourbon casks"),v("Glenmorangie Lasanta 12","Glenmorangie","","sherry finish"),
     v("Glenmorangie The Quinta Ruban 14 YO","Glenmorangie","","port finish"),v("Glenmorangie Nectar 16","Glenmorangie","","formerly Nectar d'Or, Sauternes finish"),
     v("Glenmorangie Signet","Glenmorangie"),v("Glenmorangie 18","Glenmorangie")],DT),
  x("Oban 14","","West Highland malt from the port of Oban; Diageo Classic Malt.","Oban","1794 (distillery)",WP+"Oban_distillery",
    [v("Oban 14 Year Old","Oban"),v("Oban Distillers Edition","Oban","","Montilla Fino finish"),v("Oban Little Bay","Oban","2014","no age statement"),
     v("Oban 18 Year Old","Oban","","limited")],DT),
  x("Bowmore 12","","Medium-peated Islay malt from the island's oldest working distillery.","Bowmore","1779 (distillery)",WP+"Bowmore_distillery",
    [v("Bowmore 12 Year Old","Bowmore"),v("Bowmore 9 YO","Bowmore"),v("Bowmore 15 Year Old","Bowmore"),v("Bowmore 18 Year Old","Bowmore"),
     v("Bowmore 21 Years Old Sherry Oak Cask","Bowmore"),v("Bowmore 25 Year Old","Bowmore")],DT),
  x("The GlenDronach 12 Original","GlenDronach 12","Richly sherried Highland malt from Aberdeenshire.","The GlenDronach","1826 (distillery)",WP+"Glendronach_distillery",
    [v("The GlenDronach 12 Original","The GlenDronach"),v("The GlenDronach 15 Revival","The GlenDronach"),
     v("The GlenDronach 18 Allardice","The GlenDronach"),v("The GlenDronach 21 Parliament","The GlenDronach")],DT),
  x("Aberlour A'bunadh","Aberlour","Speyside malt; A'bunadh is its cask-strength, sherry-cask, no-age-statement bottling beside aged 10–18.","Aberlour","1879 (distillery)",WP+"Aberlour_distillery",
    [v("Aberlour A'bunadh","Aberlour","","cask strength"),v("Aberlour 12 YO Double Cask","Aberlour"),v("Aberlour 16","Aberlour"),v("Aberlour 18","Aberlour")],DT)],
 "m":[["Deanston Orange Wine Cask 17 YO Single Malt Scotch Whisky","Deanston"],["Glen Moray Forbidden Fruit Single Malt Scotch Whisky","Glen Moray"],
  ["The GlenAllachie 18 YO Single Malt Scotch Whisky","Glenallachie"],["Glengoyne 17 YO Scottish Oak Single Malt Scotch Whisky","Ian Macleod Distillers"],
  ["Loch Lomond Inchmurrin 12 YO Single Malt Scotch Whisky","Loch Lomond"],["Rosebank 31 Year Old Lowland Single Malt Scotch","Rosebank"],
  ["Royal Brackla PALO CORTADO 18 Years Old Highland Single Malt Scotch","Royal Brackla"],["Scapa 16 Year Old","Scapa"],
  ["Tormore 12 YO Single Malt Scotch Whisky","Tormore"],["Torabhaig Allt Glean","Torabhaig"],["Nc'nean Cask Strength","Nc'nean"],
  ["1933 Macleod's PX Highland Single Malt Sherry Cask Finish Scotch Whisky","Macleod's"],
  ["East Asia Whisky Company Manta Ray Genesis Bunnahabhain 35 YO Single Malt Scotch Whisky","East Asia Whisky Company"],
  ["Spiritfilled Mythical Beasts Aberlour 13 YO Single Malt Scotch Whisky","Spiritfilled"],["Wormtub 10yo Speyside Single Malt",""]]}

bl={"n":"Blended Scotch whisky","a":"Blended whisky · Blend",
 "d":"Scotch that blends one or more single malts with one or more single grain whiskies.",
 "t":["Standard (no age statement)","Deluxe (12 years)","Premium aged (15–21 years)","Prestige and very old","Peated blend"],
 "s":"https://en.wikipedia.org/wiki/List_of_whisky_brands",
 "x":[
  x("Johnnie Walker Black Label","Black Label · JW Black","Twelve-year-old Kilmarnock blend; the benchmark deluxe Scotch.","Johnnie Walker","1909 (name)",WP+"Johnnie_Walker",
    [v("Johnnie Walker Double Black","Johnnie Walker","2011","smokier"),v("Johnnie Walker 18 Year Old","Johnnie Walker","2011","launched as Platinum Label, renamed 2017"),
     v("Johnnie Walker Gold Label Reserve","Johnnie Walker","2013","Gold Label from 1995")],"label · age statement · bottle size · gift pack"),
  x("Johnnie Walker Red Label","Red Label","Standard no-age-statement Johnnie Walker blend, built for mixing.","Johnnie Walker","1909 (name)",WP+"Johnnie_Walker",[],"bottle size"),
  x("Johnnie Walker Blue Label","Blue Label","Johnnie Walker's no-age-statement prestige blend, first sold as Johnnie Walker Oldest.","Johnnie Walker","1992",WP+"Johnnie_Walker",
    [v("Johnnie Walker Oldest","Johnnie Walker","1992","renamed Blue Label 1994")],"limited editions · bottle size · presentation box"),
  x("Chivas Regal 12","Chivas 12","Speyside-led deluxe blend by Chivas Brothers.","Chivas Regal","1909",WP+"Chivas_Regal",
    [v("Chivas Regal 12 Years Old","Chivas Regal"),v("Chivas Regal Extra 13","Chivas Regal","","sherry-led"),v("Chivas Regal XV","Chivas Regal","2018","Cognac cask finish"),
     v("Chivas Regal 18 Years Old","Chivas Regal"),v("Chivas Regal 25 YO","Chivas Regal","","limited"),v("Chivas Regal Mizunara","Chivas Regal","2014","part Mizunara oak")],"age statement · cask finish · bottle size"),
  x("Ballantine's Finest","Ballantine's","Light no-age-statement blend; one of the largest-selling Scotch brands, with an aged ladder above it.","Ballantine's","1827 (house)",WP+"Ballantine%27s",
    [v("Ballantine's 12 Year Old","Ballantine's"),v("Ballantine's 17 Year Old","Ballantine's"),v("Ballantine's 21 Year Old","Ballantine's"),
     v("Ballantine's 23 Year Old","Ballantine's"),v("Ballantine's 30 Year Old","Ballantine's")],"age statement · bottle size"),
  x("Dewar's White Label","Dewar's","Dewar's best-selling blend, with an aged ladder and 8-year cask-finish series.","Dewar's","1846 (house)",WP+"Dewar%27s",
    [v("Dewar's 12","Dewar's"),v("Dewar's 15","Dewar's"),v("Dewar's 18","Dewar's"),v("Dewar's 8 Year Caribbean Smooth","Dewar's","","rum cask finish")],"age statement · cask finish · bottle size"),
  x("The Famous Grouse","Famous Grouse","Perth blend by Matthew Gloag & Son, Scotland's long-time best-selling blend.","The Famous Grouse","1896",WP+"The_Famous_Grouse",
    [v("The Famous Grouse Smoky Black","The Famous Grouse","2015","formerly The Black Grouse, 2007"),v("The Famous Grouse Bourbon Cask","The Famous Grouse","2018"),
     v("The Famous Grouse Ruby Cask","The Famous Grouse","2018"),v("The Famous Grouse Sherry Cask Finish","The Famous Grouse","2022")],"cask finish · bottle size"),
  x("Royal Salute 21","Royal Salute 21 Year Old Signature Blend","Prestige 21-year-old blend in a ceramic flagon, created for Elizabeth II's coronation.","Royal Salute","1953",WP+"Royal_Salute_(whisky)",
    [v("Royal Salute 21 YO The Signature Blend","Royal Salute"),v("Royal Salute 38 Year Old Stone of Destiny","Royal Salute")],"age statement · flagon colour · limited editions"),
  x("Haig Dimple","Pinch · Dimple Pinch","Haig's deluxe blend in a pinched bottle.","Haig","",WP+"Haig_(whisky)",
    [v("Haig Dimple Pinch","Haig"),v("Haig Gold Label","Haig")],"bottle size")],
 "m":[["Teacher's Highland Cream","Teacher's Highland Cream"],["Isle of Skye 25 Year Old Blended Scotch","Isle of Skye"],["D'YAVOL VORTEX Blended Scotch","D'YAVOL"]],
 "r":[[f"{b} blended Scotch range",b] for b in ["Bell's","Grant's","J&B","William Lawson's","Label 5","Cutty Sark","Buchanan's","Black & White","White Horse","Black Bottle","Clan MacGregor","Grand Old Parr","Hankey Bannister","Logan","Old St Andrews","Passport Scotch","Something Special","Vat 69","Whyte & Mackay"]]}

bm={"n":"Blended malt Scotch whisky","a":"Vatted malt · Pure malt",
 "d":"Scotch blended only from single malts of two or more distilleries, with no grain whisky.",
 "t":["Speyside-led","Peated","Regional (one region's malts)","Aged statement"],
 "s":"https://www.thewinereserve.co.uk/spirits/whiskies",
 "x":[
  x("Monkey Shoulder","","Speyside blended malt made for mixing, first from Balvenie, Glenfiddich and Kininvie.","Monkey Shoulder","2003",WP+"Monkey_Shoulder",
    [v("Monkey Shoulder","Monkey Shoulder"),v("Smokey Monkey","Monkey Shoulder","","includes Islay whiskies")],"batch · bottle size"),
  x("Johnnie Walker Green Label","Pure Malt 15","Fifteen-year-old Johnnie Walker blended malt.","Johnnie Walker","1997",WP+"Johnnie_Walker",
    [v("Johnnie Walker Pure Malt 15 Year Old","Johnnie Walker","1997","renamed Green Label 2004")],"bottle size"),
  x("The Peat Monster","","Compass Box's peated blended malt.","Compass Box","",WP+"Compass_Box",[],"edition · bottle size"),
  x("Spice Tree","","Compass Box blended malt with extra oak character.","Compass Box","",WP+"Compass_Box",
    [v("Compass Box Crimson Casks Blended Malt Scotch Whisky","Compass Box","","limited release")],"edition · bottle size"),
  x("Naked Malt","The Naked Grouse","Sherry-cask Famous Grouse offshoot, a blended malt since 2017 and renamed Naked Malt in 2021.","The Famous Grouse","2011",WP+"The_Famous_Grouse",[],"bottle size")],
 "m":[["Noble Rebel Orchard Outburst Blended Malt Scotch Whisky","Loch Lomond"],["Mossburn Island Blended Malt",""],["Mossburn Speyside Blended Malt",""],
  ["Caisteal Chamuis Blended Malt 12yo",""],["Angels' Nectar",""]]}

sg={"n":"Single grain Scotch whisky","a":"Single grain · Grain whisky",
 "d":"Scotch from one distillery made from malted barley and other cereals, usually in column stills.",
 "t":["Wheat","Maize","No age statement","Aged statement"],
 "s":"https://www.amathusdrinks.com/haig-club",
 "x":[x("Haig Club","","No-age-statement single grain from Diageo's Cameronbridge distillery, launched with David Beckham and Simon Fuller.","Haig","2014",WP+"Haig_(whisky)",
    [v("Haig Club Single Grain","Haig")],"bottle size")]}

bg={"n":"Blended grain Scotch whisky","a":"Blended grain",
 "d":"Scotch that blends single grain whiskies from two or more distilleries.",
 "s":"https://www.thewhiskyexchange.com/p/83901/compass-box-hedonism-2025-release",
 "x":[x("Hedonism","Compass Box Hedonism","Compass Box's blended grain Scotch, the best-known bottling of the category.","Compass Box","",WP+"Compass_Box",
    [v("Compass Box Hedonism","Compass Box")],"release year · bottle size")]}

K="knowledge"
def B(n,c,f,seg,d,lines=(),sig=(),rel=(),s=K,sc=(),eras=()): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":list(sc),"rel":list(rel),"s":s}
D="Single malt distillery"
brands=[
 B("Glenfiddich","Scotland","1886",D,"Speyside distillery in Dufftown founded by William Grant; owned by William Grant & Sons.",["12","15 Solera","18","21"],["Glenfiddich 12"],["The Balvenie","Monkey Shoulder"],WP+"Glenfiddich_distillery"),
 B("The Macallan","Scotland","1824",D,"Speyside distillery at Easter Elchies, Craigellachie; owned by Edrington.",["Sherry Oak","Double Cask","Triple Cask Matured"],["The Macallan Sherry Oak"],["Highland Park"],WP+"The_Macallan_distillery"),
 B("The Glenlivet","Scotland","1824",D,"Speyside distillery founded by George Smith; owned by Chivas Brothers (Pernod Ricard).",["12","15 French Oak Reserve","Nàdurra","18"],["The Glenlivet 12"],["Chivas Regal","Aberlour"],WP+"The_Glenlivet_distillery"),
 B("Lagavulin","Scotland","1816",D,"Islay distillery owned by Diageo.",["8","16","Distillers Edition"],["Lagavulin 16"],["Talisker","Oban"],WP+"Lagavulin_distillery"),
 B("Laphroaig","Scotland","1815",D,"Islay distillery near Port Ellen; owned by Suntory Global Spirits.",["10","Quarter Cask","Càirdeas"],["Laphroaig 10"],["Bowmore"],WP+"Laphroaig_distillery"),
 B("Ardbeg","Scotland","1815",D,"Islay distillery owned by LVMH.",["Ten","Uigeadail","Corryvreckan","An Oa"],["Ardbeg Ten"],["Glenmorangie"],WP+"Ardbeg_distillery"),
 B("Talisker","Scotland","1830",D,"Isle of Skye distillery at Carbost; owned by Diageo.",["10","8 Cask Strength","18"],["Talisker 10"],["Lagavulin"],WP+"Talisker_distillery"),
 B("Highland Park","Scotland","1798",D,"Orkney distillery in Kirkwall; owned by Edrington.",["10","12","15","18"],["Highland Park 12"],["The Macallan"],WP+"Highland_Park_distillery"),
 B("Springbank","Scotland","1828",D,"Campbeltown distillery owned by the family firm J & A Mitchell; also makes Longrow and Hazelburn.",["Springbank","Longrow","Hazelburn"],["Springbank 10"],[],WP+"Springbank_distillery"),
 B("The Balvenie","Scotland","1892",D,"Speyside distillery in Dufftown; owned by William Grant & Sons.",["DoubleWood","Caribbean Cask","PortWood"],["The Balvenie DoubleWood"],["Glenfiddich","Monkey Shoulder"],WP+"Balvenie_distillery"),
 B("Glenmorangie","Scotland","1843",D,"Highland distillery at Tain; owned by LVMH.",["Original","Lasanta","Quinta Ruban","Nectar"],["Glenmorangie Original"],["Ardbeg"],WP+"Glenmorangie_distillery"),
 B("Oban","Scotland","1794",D,"West Highland distillery in Oban; owned by Diageo.",["14","Distillers Edition","Little Bay"],["Oban 14"],["Lagavulin","Talisker"],WP+"Oban_distillery"),
 B("Bowmore","Scotland","1779",D,"Islay's oldest working distillery; owned by Suntory Global Spirits via Morrison Bowmore.",["12","15","18","25"],["Bowmore 12"],["Laphroaig"],WP+"Bowmore_distillery"),
 B("The GlenDronach","Scotland","1826",D,"Highland distillery near Forgue, Aberdeenshire; owned by Brown–Forman.",["12 Original","15 Revival","18 Allardice","21 Parliament"],["The GlenDronach 12 Original"],[],WP+"Glendronach_distillery"),
 B("Aberlour","Scotland","1879",D,"Speyside distillery in Aberlour; owned by Chivas Brothers (Pernod Ricard).",["A'bunadh","12","16","18"],["Aberlour A'bunadh"],["The Glenlivet"],WP+"Aberlour_distillery"),
 B("Johnnie Walker","Scotland","1820","Blended Scotch","Kilmarnock-founded blended Scotch brand owned by Diageo.",["Red Label","Black Label","Double Black","Green Label","Gold Label Reserve","18","Blue Label"],["Johnnie Walker Black Label","Johnnie Walker Red Label","Johnnie Walker Blue Label","Johnnie Walker Green Label"],["Haig"],WP+"Johnnie_Walker"),
 B("Chivas Regal","Scotland","1909","Blended Scotch","Deluxe blend of Chivas Brothers (Pernod Ricard).",["12","Extra 13","XV","18","25","Mizunara"],["Chivas Regal 12"],["Royal Salute","Ballantine's","The Glenlivet"],WP+"Chivas_Regal"),
 B("Ballantine's","Scotland","1827","Blended Scotch","Edinburgh-origin blended Scotch owned by Pernod Ricard via Chivas Brothers.",["Finest","12","17","21","30"],["Ballantine's Finest"],["Chivas Regal"],WP+"Ballantine%27s"),
 B("Dewar's","Scotland","1846","Blended Scotch","Blend house founded by John Dewar; owned by Bacardi since 1998.",["White Label","12","15","18","8 Year cask finishes"],["Dewar's White Label"],[],WP+"Dewar%27s"),
 B("The Famous Grouse","Scotland","1896","Blended Scotch","Blend first made by Matthew Gloag & Son; sold by Edrington to William Grant & Sons (approved 2025).",["The Famous Grouse","Smoky Black","Naked Malt"],["The Famous Grouse","Naked Malt"],[],WP+"The_Famous_Grouse"),
 B("Royal Salute","Scotland","1953","Prestige blended Scotch","Chivas Brothers (Pernod Ricard) prestige blend launched for the 1953 coronation.",["21","38 Stone of Destiny"],["Royal Salute 21"],["Chivas Regal"],WP+"Royal_Salute_(whisky)"),
 B("Haig","Scotland","1824","Blended and single grain Scotch","John Haig & Co. whisky brand tied to the Cameronbridge grain distillery; owned by Diageo.",["Haig Club","Gold Label","Dimple"],["Haig Club","Haig Dimple"],["Johnnie Walker"],WP+"Haig_(whisky)"),
 B("Monkey Shoulder","Scotland","2003","Blended malt Scotch","William Grant & Sons blended malt for mixing.",["Monkey Shoulder","Smokey Monkey"],["Monkey Shoulder"],["Glenfiddich","The Balvenie"],WP+"Monkey_Shoulder"),
 B("Compass Box","Scotland","2000","Independent whisky blender","Blending house founded by John Glaser, headquartered in Richmond.",["Hedonism","Spice Tree","The Peat Monster","Great King Street"],["Hedonism","The Peat Monster","Spice Tree"],[],WP+"Compass_Box"),
]
notes=("Region (Speyside, Highland, Islands, Islay, Lowland, Campbeltown) is a type, per the Scotch Whisky Association regions on the Scotch_whisky page. "
 "Old models that belong to a distillery archetype became its versions; the rest of the Scotch models stay in m (duplicates removed: second Manta Ray and second Rosebank listing, 3 extra Nc'nean, second Torabhaig, Loch Lomond Remarkable Alchemy, Darkness 8yo (no maker)). "
 "MOVE to the World/Irish/Japanese/American whisky shelves (not Scotch): Amrut Fusion; Kavalan Solist Vinho Barrique; Nikka Yoichi 10yo; Sakurao Togouchi; Starward Tawny; Sullivans Cove French Oak; Callington Mill PX; St George Baller; Stranahan's Snowflake; KI ONE Signature; Thy Whisky Casks 1035+1036; The English Distillery Sherry Hogshead; Teeling (4 listings), The Donn (Craft Irish Whiskey), Titanic Distillers 8 YO; Ichiro's Malt & Grain; Jameson Triple Triple; Midleton Very Rare 2026; Tullamore D.E.W. 12; Longleaf Cask Strength Heirloom; Kwun Cheung blended malt; Fercullen 15; Frey Ranch 100% Barley; Waterloo The Duke Rum Cask. "
 "Blend ranges in r kept only for houses without an archetype (Johnnie Walker, Chivas Regal, Ballantine's, Dewar's, Famous Grouse, Royal Salute, Haig ranges are now archetypes). "
 "No tradition entries: Scotch is an industrial-regional category, not an artisan craft tradition in the register's sense. Not added for want of a retrieved source: Compass Box archetype years, Great King Street/Asyla/Oak Cross, other single grains (Cameron Brig, Girvan, North British).")
out={"kinds":[sm,bl,bm,sg,bg],"brands":brands,"traditions":[],"notes":notes}
tmp=P+'.tmp'; json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P); print('ok')
