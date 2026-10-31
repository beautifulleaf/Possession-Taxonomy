import json, os
p='/home/user/Possession-Taxonomy/rebuild/work/D3/shelves/00_01.json'
WP='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a="",dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),vv)) for vv in v]}
    if dt: x["dt"]=dt
    return x
SONY='https://experience.sony-asia.com/sg/home/exploredetail/1328'
kinds=[
{"n":"In-ear monitors","a":"universal in-ear monitor · IEM","d":"Sealing in-ear earphone with standard tips, sold for listening.",
 "t":["dynamic","balanced armature","hybrid","planar magnetic","electrostatic"],"s":"https://www.64audio.com/collections/all-iems?page=2",
 "x":[
  X("Etymotic ER4","Etymotic Research","1991","https://stereophile.com/content/25-years-making-good-thing-better-etymotic-er4sr-and-er4xr","Single balanced-armature, deep-insertion earphone; the first hi-fi noise-isolating in-ear.",
    [("ER4S","Etymotic Research","1991","original"),("ER4B","Etymotic Research","1991","binaural recording version"),("ER4PT","Etymotic Research","","portable version"),("ER4SR","Etymotic Research","2016","studio reference"),("ER4XR","Etymotic Research","2016","extended response")]),
  X("Shure SE series","Shure","","https://canford.co.uk/SHURE-IN-EAR-MONITORS-Earphones","Sound-isolating stage and listening earphones with detachable cables, from single dynamic to quad armature.",
    [("SE215 Pro","Shure","","single dynamic driver"),("SE425 Pro","Shure","","two drivers"),("SE535 Pro","Shure","","three drivers"),("SE846 Gen 2","Shure","","four drivers"),("SE112","Shure","","entry"),("Aonic 3","Shure","","")]),
  X("Shure KSE electrostatic earphones","Shure","",WP+"In-ear_monitor","Electrostatic in-ear system with its own energiser.",[("KSE1200","Shure","",""),("KSE1500","Shure","","")]),
  X("Sennheiser IE 300 / IE 600 / IE 900","Sennheiser","2021","https://sg.sennheiser-hearing.com/blogs/stories/sennheiser-ie-600-review-a-short-simple-comparison-with-ie-300-and-ie-900","Single 7 mm driver audiophile in-ears in plastic, zirconium and aluminium housings.",
    [("IE 300","Sennheiser","2021","entry, plastic"),("IE 900","Sennheiser","2021","flagship, aluminium"),("IE 600","Sennheiser","2022","zirconium alloy")]),
  X("Campfire Audio Andromeda","Campfire Audio","2016","https://www.campfireaudio.com/pages/andromeda-history-page","Five-armature IEM in a green aluminium shell, revised many times.",
    [("Andromeda","Campfire Audio","2016","five balanced armatures"),("Andromeda S","Campfire Audio","","stainless steel"),("Andromeda Gold","Campfire Audio","","seven armatures"),("Andromeda 2020","Campfire Audio","2020",""),("Andromeda Emerald Sea","Campfire Audio","2023",""),("Andromeda 10","Campfire Audio","2025","ten armatures")],dt="limited colourways 2017–2018"),
  X("64 Audio tia flagships","64 Audio","","https://headphones.com/blogs/reviews/64-audio-flagship-shootout-nio-u12t-tia-trio-u18t-tia-fourte","Multi-driver universal IEMs with tubeless tia armatures and APEX pressure vents.",
    [("U12t","64 Audio","","12 BA"),("U18t","64 Audio","","18 BA"),("Tia Trio","64 Audio","","2BA + 1DD"),("Nio","64 Audio","","8BA + 1DD"),("Volür","64 Audio","",""),("Solo","64 Audio","","")],dt="APEX module mX · m15 · m20"),
  X("Moondrop Blessing","Moondrop Audio","","https://nextrift.com/202224422/","Hybrid IEM regarded as the benchmark at its price, much imitated in Chi-Fi.",
    [("Blessing","Moondrop Audio","",""),("Blessing 2","Moondrop Audio","","benchmark around US$300"),("Aria Snow Edition","Moondrop Audio","","single dynamic sibling")]),
  X("Truthear Hexa","Truthear","2022","https://nextrift.com/202224422/","Budget 1DD + 3BA hybrid tuned close to the Blessing 2.",
    [("Zero","Truthear","","dual dynamic, with Crinacle"),("Hexa","Truthear","2022","1DD + 3BA")]),
 ],
 "m":[["Solaris","Campfire Audio"],["Kima","DUNU"],["Odin","Empire Ears"],["Heaven II","Final Audio"],["HA-FW10000","JVC"],["Orchestra","Kiwi Ears"],["Variations","Moondrop Audio"],["Katana","Noble Audio"],["Traillii","Oriolus"],["IER-M9","Sony"],["IER-Z1R","Sony"],["Helios","Symphonium Audio"],["T2","TIN HiFi"],["Monarch Mk2","ThieAudio"],["Elysium","Vision Ears"],["Anole V14","qdc"],["Timeless","7Hz"],["ASTRU","Meze Audio"],["Hana","Tanchjim"],["Zetian Wu","Tangzu"]]},
{"n":"Custom in-ear monitors","a":"custom IEM","d":"In-ear earphones with shells moulded to one listener's ear, sold for listening.","t":["acrylic shell","silicone shell"],"s":"https://www.64audio.com/collections/all-iems?page=2",
 "x":[
  X("Ultimate Ears custom monitors","Ultimate Ears","1995",WP+"Ultimate_Ears","Custom-moulded multi-armature monitors that began with Jerry Harvey's 1995 design for Van Halen.",
    [("UE-5","Ultimate Ears","1998",""),("UE5 Pro","Ultimate Ears","","dual armature"),("UE11 Pro","Ultimate Ears","","four armatures"),("UE18 Pro","Ultimate Ears","","six armatures"),("UE Live","Ultimate Ears","","7BA + 1DD hybrid")]),
  X("JH Audio JH13 / JH16","JH Audio","2009","https://en.wikipedia.org/wiki/Jerry_Harvey_(inventor)","Jerry Harvey's later multi-driver custom monitors with integrated crossovers.",
    [("JH13 Pro","JH Audio","2009","dual lows, mids and highs"),("JH16 Pro","JH Audio","",""),("Layla","JH Audio","","12 armatures")]),
  X("64 Audio A-series","64 Audio","",WP+"In-ear_monitor","Custom-shell versions of 64 Audio's tia monitors.",
    [("A18t","64 Audio","","18 armatures"),("A12t","64 Audio","",""),("A18s","64 Audio","",""),("A3e","64 Audio","","")]),
 ],
 "m":[["Viento","Hidition"],["KL-Sirius","Kumitate"]]},
{"n":"True wireless earbuds","a":"TWS earbuds · wireless earbuds","d":"Two separate wireless buds sold with a charging case.","t":["with active noise cancellation","without ANC"],"s":"https://www.apple.com/airpods/compare/?modelList=airpods-pro-3,airpods-4,airpods-max",
 "x":[
  X("Apple AirPods","Apple","2016",WP+"AirPods","Apple's wireless earbuds, the best-selling true wireless line.",
    [("AirPods","Apple","2016","first generation"),("AirPods (2nd generation)","Apple","2019",""),("AirPods (3rd generation)","Apple","2021",""),("AirPods 4","Apple","2024",""),("AirPods 4 with Active Noise Cancellation","Apple","2024","")]),
  X("Apple AirPods Pro","Apple","2019",WP+"AirPods","Sealing AirPods with active noise cancellation.",
    [("AirPods Pro","Apple","2019",""),("AirPods Pro 2","Apple","2022",""),("AirPods Pro 3","Apple","2025","")]),
  X("Sony WF-1000X","Sony","2017",SONY,"Sony's flagship noise-cancelling true wireless earbuds.",
    [("WF-1000X","Sony","2017","Sony's first true wireless"),("WF-1000XM3","Sony","2019",""),("WF-1000XM4","Sony","2021",""),("WF-1000XM5","Sony","2023",""),("WF-1000XM6","Sony","2026","")]),
  X("Samsung Galaxy Buds","Samsung","2019",WP+"Samsung_Galaxy_Buds_series","Samsung's true wireless earbud series, successor to the Gear IconX.",
    [("Galaxy Buds","Samsung","2019",""),("Galaxy Buds Live","Samsung","2020",""),("Galaxy Buds Pro","Samsung","2021",""),("Galaxy Buds 2 Pro","Samsung","2022",""),("Galaxy Buds FE","Samsung","2023",""),("Galaxy Buds 3 Pro","Samsung","2024",""),("Galaxy Buds 4 Pro","Samsung","2026","")]),
  X("Bose QuietComfort Earbuds","Bose","2022",WP+"List_of_Bose_headphones","Bose's noise-cancelling true wireless earbuds.",
    [("QuietComfort Earbuds II","Bose","2022",""),("QuietComfort Ultra Earbuds","Bose","2023",""),("QuietComfort Earbuds (2nd gen)","Bose","2024","")]),
 ]},
{"n":"Earbuds","a":"non-sealing earbud · wired earbuds","d":"Earphone that rests in the outer ear without sealing the canal.","s":"https://audiot.co.uk/p-33473-sennheiser-accentum-open-earbuds-audio-t.aspx",
 "x":[
  X("Apple iPod earbuds / EarPods","Apple","2001",WP+"Apple_headphones","Apple's bundled white wired earbuds, round from 2001 and contoured EarPods from 2012.",
    [("iPod earbuds","Apple","2001","round, foam covers"),("EarPods","Apple","2012","contoured, remote and mic"),("EarPods (3.5mm Headphone Plug)","Apple","",""),("EarPods (Lightning)","Apple","",""),("EarPods (USB-C)","Apple","","")]),
 ]},
{"n":"Open-ear earphones","a":"bone-conduction earphones · open-fit earbuds","d":"Earphones that leave the ear canal open, by bone conduction or an open-ear driver.","t":["bone conduction","air conduction (open-ear driver)","ear-clip"],"s":"https://shokz.com/collections/all",
 "x":[
  X("Shokz OpenRun (Aeropex)","Shokz","2019","https://shokz.ae/pages/our-story","Wrap-around bone-conduction sports headphone, Shokz's flagship line.",
    [("Bluez","Shokz","2012","first AfterShokz product"),("Titanium","Shokz","",""),("Air","Shokz","2017",""),("Aeropex","Shokz","2019",""),("OpenRun","Shokz","2021","renamed Aeropex"),("OpenRun Pro","Shokz","2022",""),("OpenRun Pro 2","Shokz","",""),("OpenRun Air 2","Shokz","","")]),
  X("Shokz OpenMove","Shokz","2020","https://shokz.ae/pages/our-story","Entry-level bone-conduction headphone of Shokz's Open series."),
  X("Shokz OpenSwim","Shokz","2019","https://shokz.ae/pages/our-story","Waterproof bone-conduction headphone with built-in MP3 player, first sold as Xtrainerz.",
    [("Xtrainerz","Shokz","2019",""),("OpenSwim","Shokz","2021","renamed"),("OpenSwim Pro","Shokz","","")]),
 ],
 "m":[["OpenFit 2","Shokz"],["OpenFit Air 2","Shokz"],["OpenFit Pro","Shokz"],["OpenDots 2","Shokz"],["OpenDots Air","Shokz"],["Pill","Moondrop Audio"],["ACCENTUM Open","Sennheiser"]],
 "r":[["OpenFit","Shokz"],["OpenDots","Shokz"]]},
]
def B(n,c,f,seg,kf,d,s,sig=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=list(sig)
    return b
brands=[
 B("Etymotic Research","United States","1983","Specialist","insert earphones","Hearing-research firm whose ER4 was the first hi-fi noise-isolating in-ear.","https://stereophile.com/content/25-years-making-good-thing-better-etymotic-er4sr-and-er4xr",["ER4"]),
 B("Shure","United States","1925","Professional & flagship","microphones, in-ears","Chicago-area microphone and earphone maker.","knowledge",["SE215","SE846"]),
 B("Sennheiser","Germany","1945","Professional & flagship","headphones, microphones","Wedemark audio company.","knowledge",["IE 900"]),
 B("Campfire Audio","United States","","Artisan & independent","IEMs","In-ear maker known for the Andromeda.","https://www.campfireaudio.com/pages/andromeda-history-page",["Andromeda"]),
 B("64 Audio","United States","","Specialist","multi-driver IEMs","In-ear maker with tia armatures and APEX venting.","https://headphones.com/blogs/reviews/64-audio-flagship-shootout-nio-u12t-tia-trio-u18t-tia-fourte",["U12t","A18t"]),
 B("Moondrop Audio","China","","Value","Chi-Fi IEMs","Chinese in-ear maker whose Blessing 2 became a price-class benchmark.","https://nextrift.com/202224422/",["Blessing 2","Aria"]),
 B("Truthear","","","Value","budget IEMs","Chinese in-ear brand (Zero, Hexa).","https://nextrift.com/202224422/",["Hexa"]),
 B("Ultimate Ears","United States","1995","Professional & flagship","custom IEMs","Custom in-ear pioneer founded by Jerry and Mindy Harvey; owned by Logitech since 2008.",WP+"Ultimate_Ears",["UE18 Pro"]),
 B("JH Audio","United States","2007","Artisan & independent","custom IEMs","Jerry Harvey's custom in-ear company, founded as Jerry Harvey Audio LLC.","https://en.wikipedia.org/wiki/Jerry_Harvey_(inventor)",["JH13 Pro","JH16 Pro"]),
 B("Apple","United States","1976","Premium","consumer electronics","American technology company; AirPods and EarPods.","knowledge",["AirPods","EarPods"]),
 B("Sony","Japan","1946","Mainstream","consumer electronics","Japanese electronics group.","knowledge",["WF-1000X"]),
 B("Samsung","South Korea","1938","Mainstream","consumer electronics","Korean electronics group; Galaxy Buds.","knowledge",["Galaxy Buds"]),
 B("Bose","United States","1964","Premium","noise cancelling","American audio company.","knowledge",["QuietComfort Earbuds"]),
 B("Shokz","China","2004","Specialist","bone conduction","Bone-conduction headphone maker, sold as AfterShokz from 2011 until the 2021 rebrand.","https://shokz.ae/pages/our-story",["OpenRun","OpenSwim"]),
]
notes=("82 flat IEM models cut to 8 archetypes (with old models as versions) and 20 leftovers; dropped SKU duplicates (Elysian Annihilator (2021), ThieAudio Monarch Mk2 prefixed copy) and long-tail Chi-Fi models (TIN HiFi P2/T2 Plus/T3, Softears, Acoustune, etc.) to stay under the mixed-mode cap. "
 "Custom IEMs organised by UE / JH Audio / 64 Audio lineages. Earbud icons Sennheiser MX500 and Sony Fontopia/MDR-E888 left out: only forum snippets, no retrievable page. Sennheiser ACCENTUM Open kept in Open-ear earphones (old data listed it under true wireless and earbuds). founding years left blank where no page gave them.")
t=p+'.tmp'; json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
