import json
W='https://en.wikipedia.org/wiki/'
LE="https://www.leafly.com/brands/cheech-and-chong-glass"
TC="https://techcrunch.com/2022/06/15/puffco-unveils-the-299-proxy-an-innovative-modular-cannabis-vaporizer"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
kinds=[
{"n":"Bong","a":"water pipe","d":"Water pipe with a bowl and a tube, drawn through water, for dry material.","t":["Beaker","Straight tube","Bubbler","Percolator"],"s":LE,
 "x":[x("RooR","RooR","",W+"Bong","Glass bong brand; the one maker named on Wikipedia's bong article, which says it has sued sellers of counterfeits.")],
 "m":[["Hey Margaret Flower Bubbler","Cheech and Chong Glass"],["Roots Beaker Tube Bong","Cheech and Chong Glass"]]},
{"n":"Dab rig","a":"","d":"Water pipe made to vaporise concentrates on a heated nail or banger, usually with a torch.","t":["Recycler","Mini rig","Concentrate bubbler"],"s":LE,"m":[["Mr. Neatnik Concentrate Bubbler","Cheech and Chong Glass"]]},
{"n":"Electronic dab rig","a":"e-rig","d":"Battery-heated device that vaporises concentrate without a torch, often through a water-filtered glass piece.","t":["Ceramic heater","Quartz heater"],"s":TC,
 "x":[x("Puffco Peak","Puffco","",TC,"Electronic dab rig from Puffco, founded 2013 by Roger Volodarsky; the Peak Pro is among the best e-rigs and its heating element is reused in the 2022 Proxy.",[("Peak Pro","Puffco","",""),("Proxy","Puffco","2022","Modular unit, $299 at launch")])]},
{"n":"Hand pipe & chillum","a":"","d":"Small dry pipe, or straight conical pipe, made for cannabis.","t":["Spoon","Sherlock","Steamroller","One-hitter","Dugout","Chillum"],"s":LE,
 "x":[x("Chillum","","",W+"Chillum","Straight conical pipe of clay or soft stone, used in Nepal and India; a water-filtered version is called a chalice."),
      x("One-hitter and dugout","","",W+"Dugout_(smoking)","Slender pipe for a single inhalation of about 0.1-0.3 g, carried in a two-compartment dugout case.")],
 "m":[["Ajax Lady Hand Pipe","Cheech and Chong Glass"]]},
{"n":"Water-pipe bowls & bangers","a":"bowl slide · banger · nail","d":"Parts of a water pipe: removable bowl slides, downstems, ash catchers, and heated quartz bangers with carb caps for dab rigs.","t":["Bowl slide","Downstem","Ash catcher","Quartz banger","Carb cap"],"s":LE},
{"n":"Portable vaporiser","a":"handheld vaporiser","d":"Battery-powered handheld vaporiser for dry herb or concentrate.","t":["Conduction","Convection","Butane-heated"],"s":"https://www.storz-bickel.com/en-us/devices/portable",
 "x":[x("PAX","Pax Labs","2012",W+"Pax_Labs","Dry-herb vaporiser line from Pax Labs (formerly Ploom): PAX 1 (2012), PAX 3 (2016) with concentrate insert, Era pods, Mini and Plus (2022).",[("PAX 1","Pax Labs","2012","First dry-herb model"),("PAX 3","Pax Labs","2016","Herb and concentrates"),("PAX Era","Pax Labs","2016","Prefilled oil pods"),("PAX Flow","Pax Labs","2025","")])],
 "m":[["Crafty+","Storz and Bickel"],["Mighty+","Storz and Bickel"],["Veazy","Storz and Bickel"],["Venty","Storz and Bickel"]]},
{"n":"Desktop vaporiser","a":"tabletop vaporiser","d":"Mains-powered stationary vaporiser for dry herb or concentrate, including the bag-filling Volcano type.","t":["Bag-fed","Whip-fed"],"s":"https://www.grasscity.com/collections/desktop-vaporizers",
 "m":[["Volcano Classic","Storz and Bickel"],["Volcano Hybrid","Storz and Bickel"],["Plenty","Storz and Bickel"]],"r":[["Volcano","Storz and Bickel"]]},
{"n":"Grinder","a":"herb grinder","d":"Device with teeth for grinding herb or tobacco; 4-piece types hold a screen that collects kief.","t":["2-piece","3-piece","4-piece with kief catcher"],"s":W+"Herb_grinder","m":[["Twisty Grinder","7pipe"]]},
]
brands=[
{"n":"Pax Labs","c":"United States","f":"2007","seg":"Premium","kf":"vaporisers","d":"San Francisco vaporiser company founded 2007 as Ploom by James Monsees and Adam Bowen; spun out Juul in 2017.","lines":["PAX","PAX Era"],"s":W+"Pax_Labs"},
{"n":"Puffco","c":"United States","f":"2013","seg":"Premium","kf":"e-rigs","d":"Maker of the Peak electronic dab rig, founded by Roger Volodarsky.","lines":["Peak","Proxy"],"s":TC},
{"n":"RooR","c":"","f":"","seg":"Specialist","kf":"glass bongs","d":"Glass bong brand named in Wikipedia's bong article.","s":W+"Bong"},
]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Illadelph, Mobius, Santa Cruz Shredder, Space Case, DynaVap, Arizer, Storz & Bickel company facts not on retrieved pages; omitted. Cheech and Chong Glass SKU list trimmed to a few models. Bong bowl and dab nail merged; 'Other vaporizers' merged into desktop. Storz & Bickel models kept as old models. Grasscity page cited from old data."},open('s07_02.json','w'),ensure_ascii=False)
