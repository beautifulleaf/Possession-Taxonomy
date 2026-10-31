import json, os
OLD="https://ergobaby.com/en-us/blogs/tiny-adventures/types-of-baby-carriers-and-how-to-wear-them"
BGL="https://www.babygearlab.com/topics/getting-around/best-baby-carrier"
kinds=[
 {"n":"Soft structured baby carrier","a":"SSC · buckle carrier · structured carrier","d":"Buckled carrier with a padded panel, shoulder straps and waistband.",
  "t":["newborn-only","toddler size","forward-facing","mesh / all-season","hybrid buckle wrap"],"tg":["baby"],"s":OLD,
  "m":[["Omni Deluxe","Ergobaby"],["Omni 360","Ergobaby"],["Embrace","Ergobaby"],["Baby Carrier One","BabyBjörn"],["Baby Carrier Harmony","BabyBjörn"],["Free-to-Grow","Tula"],["Explore","Tula"],["Boba X","Boba"],["Complete All Seasons","LILLEbaby"],["Flip 4-in-1","Infantino"],["Aerial","WildBird"],["Duet","Moby"]]},
 {"n":"Woven wrap","a":"woven baby wrap · tragetuch","d":"Long length of woven, non-stretch fabric tied round the wearer to hold a baby.",
  "t":["cotton","linen","hemp","silk","wool blend","sizes by length"],"tg":["baby"],"s":OLD,
  "m":[["Prima","Didymos"],["Lisca","Didymos"],["Doubleface","Didymos"]]},
 {"n":"Stretchy wrap","a":"jersey wrap · knit wrap","d":"Long length of stretch fabric tied round the wearer to hold a baby.",
  "t":["jersey","interlock","pre-sewn / pre-tied"],"tg":["baby"],"s":OLD,
  "m":[["Baby Wrap","Solly Baby"],["Boba Wrap","Boba"],["Classic Wrap","Moby"],["Original","Baby K'tan"],["Flex","Konny"],["Easy-Wrap Baby Carrier","Moby"]]},
 {"n":"Ring sling","a":"sling","d":"Length of fabric threaded through two rings and worn over one shoulder.",
  "t":["linen","silk","cotton","aluminium or nylon rings","pleated or gathered shoulder"],"tg":["baby"],"s":OLD,
  "m":[["Ring Sling","Sakura Bloom"],["Linen Ring Sling","WildBird"],["Ring Sling","Nalakai"],["DidySling","Didymos"],["Ring Sling","Tula"]]},
 {"n":"Mei tai","a":"bei dai · tie carrier","d":"Panel carrier with four straps that are tied rather than buckled.",
  "t":["tied waist","buckled waist (half-buckle)"],"tg":["baby"],"s":OLD,
  "m":[["Sash Mei Tai","Infantino"]]},
 {"n":"Hip seat","a":"hip seat carrier · hip carrier","d":"Waist belt with a seat on which a child sits on the wearer's hip.",
  "t":["seat only","with detachable carrier panel"],"tg":["baby"],"s":OLD,
  "m":[["Hip Seat Lite","Tushbaby"],["Alta Hip Seat","Ergobaby"],["Lift Hip Seat","Ergobaby"],["Hip Seat Baby Carrier","Momcozy"],["Hip Seat Carrier","Regalo"],["2-in-1 Carrier & Hip Seat","Moby"],["Hip Rider Plus 5-in-1","Infantino"],["Sidekick Plus 3-in-1","Chicco"],["DidyHip","Didymos"]]},
 {"n":"Child carrier backpack","a":"framed child carrier · hiking baby carrier · kid carrier","d":"Framed hiking backpack with a padded seat that carries a child on the wearer's back.",
  "t":["aluminium frame","with sunshade","with daypack storage","travel-light"],"tg":["baby"],"s":"https://www.babygearlab.com/topics/getting-around/best-baby-backpack",
  "m":[["Kid Comfort","Deuter"],["Kid Comfort Pro","Deuter"],["Kid Comfort Active SL","Deuter"],["Poco","Osprey"],["Poco LT","Osprey"],["Sapling","Thule"],["Journey PerfectFIT Elite","Kelty"],["Escape","Phil and Teds"],["Cross Country","Clevr"]]},
]
B=lambda n,c,f,seg,d,lines,s,sig=None:{"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":[],"sig":sig or [],"sc":[],"rel":[],"s":s}
brands=[
 B("Ergobaby","United States","2003","baby carriers","Baby-carrier maker founded on Maui, Hawaii, by Karin Frost after she sewed a carrier for her son.",["Omni","Embrace","Alta"],"https://archives.starbulletin.com/2007/07/29/business/engle.html",["Omni"]),
 B("BabyBjörn","Sweden","1961","baby products","Family-owned Swedish maker of minimalist baby products, best known for its carriers.",["Baby Carrier One","Baby Carrier Harmony","Baby Carrier Mini"],"https://en.wikipedia.org/wiki/BabyBjörn",["Baby Carrier Original"]),
 B("Tula","","2009","baby carriers","Baby-carrier brand making structured carriers, wraps and ring slings since 2009.",["Explore","Original","Kid","Free-to-Grow"],"https://babytula.com/pages/about-us"),
 B("Didymos","Germany","1972","babywearing","Babywearing firm founded by Erika Hoffmann, known for woven wraps, ring slings and buckle carriers.",["Prima","Lisca","Doubleface","DidySling","DidyKlick","DidySnap","DidyHip"],"https://www.didymos.de/en/"),
 B("Moby","","2003","baby wraps","Wrap brand whose name stands for 'MOther & baBY', launched with its classic stretchy wrap in 2003.",["Classic Wrap","Easy-Wrap","Duet"],"https://mobywrap.com/pages/moby-the-babywearing-experts",["Classic Wrap"]),
 B("Solly Baby","United States","2010","baby wraps","Californian maker of lightweight stretchy wraps, started when founder Elle sewed her first wrap in 2010.",["Baby Wrap","Soft Buckle Carrier"],"https://sollybaby.com/pages/our-story",["Baby Wrap"]),
 B("Sakura Bloom","United States","","ring slings","San Diego-based maker of small-batch linen and silk ring slings and carriers.",["Ring Sling"],"https://www.fashionmamas.com/blog/sakura-bloom-carries",["Ring Sling"]),
 B("Boba","United States","2007","baby carriers","Boulder, Colorado, maker of baby carriers and stretchy wraps.",["Boba Wrap","Boba X"],"https://discovery.patsnap.com/company/boba/"),
 B("Deuter","Germany","1898","outdoor packs","German maker of sport packs and bags founded by Hans Deuter in Augsburg, now owned by Schwan-Stabilo.",["Kid Comfort"],"https://en.wikipedia.org/wiki/Deuter_Sport"),
 B("Osprey","United States","1974","outdoor packs","American outdoor backpack maker founded in Santa Cruz by Mike Pfotenhauer, now in Cortez, Colorado.",["Poco"],"https://en.wikipedia.org/wiki/Osprey_Packs"),
 B("Thule","Sweden","1942","outdoor and transport","Swedish group making roof boxes, bike racks, strollers, bags and child carriers.",["Sapling"],"https://en.wikipedia.org/wiki/Thule_Group"),
]
notes=("Tier shelf. Models come from independent tests: BabyGearLab (carriers; backpack carriers), Babylist (carriers; hip seats), MountainIQ (hiking carriers). "
 "Old Ergobaby Omni Classic and Omni Lite dropped (not in any retrieved test; Omni Deluxe/360 kept). Mei tai has only the Infantino Sash Mei Tai: Hoppediz Hop-Tye and others were seen only in search snippets, so left out. "
 "No archetypes (tier kinds). No Ergobaby Wikipedia page exists; its register entry cites a 2007 Star-Bulletin article. Tula and Moby register entries leave country blank (not stated on retrieved pages). "
 "Hybrid buckle wraps and pre-sewn wraps folded into SSC / stretchy-wrap types, not separate kinds. Traditional carriers (onbuhimo, podaegi, cradleboard) not added as kinds. No traditions.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/A4/shelves/08_00.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
