import json, os
p='/home/user/Possession-Taxonomy/rebuild/work/D3/shelves/02_00.json'
WP='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a="",dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),vv)) for vv in v]}
    if dt: x["dt"]=dt
    return x
kinds=[
{"n":"Turntable","a":"record player · record deck","d":"Record-playing deck with platter and tonearm.","t":["belt drive","direct drive","idler drive","suspended sub-chassis","tangential arm","with built-in phono stage"],"s":"https://vintagetechnics.co.uk/",
 "x":[
  X("Garrard 301 / 401","Garrard","1954",WP+"Garrard_Engineering_and_Manufacturing_Company","Idler-drive transcription turntables, now prized for restoration in heavy plinths.",
    [("301","Garrard","1954","first transcription deck for 33, 45 and 78 rpm"),("401","Garrard","1965","restyled, stronger motor; made to 1976")]),
  X("Thorens TD 124","Thorens","1957",WP+"Thorens","Swiss transcription turntable made 1957–1965, a collector classic."),
  X("Thorens TD 150 / TD 160","Thorens","1965",WP+"Thorens","Belt-driven suspended sub-chassis decks that set the pattern for later British designs.",
    [("TD 150","Thorens","1965",""),("TD 150 MkII","Thorens","1965",""),("TD 160","Thorens","1972","successor to TD 150"),("TD 125 Mk II","Thorens","1972",""),("TD 126 Mk III","Thorens","1979","")]),
  X("Acoustic Research XA","Acoustic Research","1963",WP+"Acoustic_Research","Low-cost belt-drive deck with suspended platter and sub-chassis, ancestor of the LP12."),
  X("Linn Sondek LP12","Linn","1972",WP+"Linn_Sondek_LP12","Suspended sub-chassis belt-drive deck, upgraded piece by piece for fifty years.",
    [("LP12","Linn","1972","original"),("Valhalla power supply","Linn","1982","standard from May 1982"),("Lingo power supply","Linn","1990",""),("Cirkus upgrade","Linn","1993","bearing and sub-chassis"),("Keel sub-chassis","Linn","2006",""),("Trampolin Mk2 baseboard","Linn","2006",""),("Radikal","Linn","2009","motor and power supply"),("Karousel bearing","Linn","2020","")],dt="arm (Ittok, Ekos, Akito, Basik) · plinth wood · power supply level"),
  X("Technics SL-1200","Technics","1972",WP+"Technics_SL-1200","Quartz-locked direct-drive turntable; the MK2 became the DJ standard.",
    [("SL-1200","Technics","1972","original"),("SL-1200MK2","Technics","1979","DJ standard"),("SL-1200G / GAE / GR","Technics","2016","Grand Class revival"),("SL-1200MK7","Technics","2019","DJ model"),("Technics SL-1200GR2","Technics","",""),("Technics SL-1200GME","Technics","",""),("Technics SL-1300G","Technics","",""),("Technics SL-1500C","Technics","","with phono stage"),("Technics SL-1000MK2","Technics","","flagship")],dt="finish silver/black · limited editions"),
  X("Bang & Olufsen Beogram 4000","Bang & Olufsen","1972","https://www.whathifi.com/news/bang-and-olufsen-to-restore-1972-beogram-4000-turntables-and-other-classics","Tangential-arm turntable, later restored by B&O as a recreated edition."),
  X("Michell GyroDec","Michell","1980s","https://hifigear.co.uk/blog/history-of-michell-engineering-founded-by-the-late-john-michell","Acrylic-plinth suspended deck with gold platter weights.",
    [("Reference Electronic","Michell","1977","predecessor"),("GyroDec","Michell","1980s",""),("Orbe","Michell","1995","flagship"),("Gyro SE","Michell","2005","")]),
  X("Rega Planar","Rega","",WP+"Rega_Research","Light, rigid British belt-drive decks with Rega arms; the Planar 3 is the best known.",
    [("Planar 2","Rega","",""),("Rega Planar 1","Rega","",""),("Rega Planar 1 Plus","Rega","",""),("Rega RP2","Rega","",""),("Rega Planar 6","Rega","",""),("Rega Planar 8","Rega","",""),("Rega Planar 10","Rega","",""),("Rega Naia","Rega","","flagship")]),
  X("Pro-Ject Debut","Pro-Ject","1999",WP+"Pro-Ject","Budget belt-drive deck credited with helping the vinyl revival.",
    [("Pro-Ject 1","Pro-Ject","1991","first Pro-Ject"),("Debut","Pro-Ject","1999",""),("Debut Carbon EVO","Pro-Ject","2020",""),("Debut PRO","Pro-Ject","2021","30th anniversary"),("Pro-Ject Debut RecordMaster II","Pro-Ject","","")]),
 ],
 "m":[["Audio-Technica AT-LP7","Audio-Technica"],["Audio-Technica AT-LPA2","Audio-Technica"],["Cambridge Audio ALVA ST","Cambridge Audio"],["Clearaudio Innovation Compact","Clearaudio"],["Dr. Feickert Analogue Firebird","Dr. Feickert Analogue"],["Dual CS 618Q","Dual"],["EAT C-Sharp","EAT"],["Marantz TT15S1","Marantz"],["McIntosh MT5","McIntosh"],["MoFi Electronics UltraDeck","MoFi Electronics"],["Pro-Ject RPM 3 Carbon","Pro-Ject"],["Pro-Ject RPM 9 Carbon","Pro-Ject"],["Pro-Ject Xtension 9 Evolution","Pro-Ject"],["Pro-Ject Signature 10","Pro-Ject"],["Pro-Ject T1 EVO","Pro-Ject"],["Pure Fidelity Encore Mk2","Pure Fidelity"],["TW Acustic Raven Two","TW Acustic"],["VPI Forever Model One","VPI"],["Technics SL-1100A","Technics"],["Technics SL-QD33","Technics"]],
 "r":[["Planar","Rega"],["RPM Line","Pro-Ject"],["T Line","Pro-Ject"]]},
{"n":"Phono cartridge","a":"pickup · cart","d":"Pickup cartridge made to fit a turntable tonearm.","t":["moving magnet (MM)","moving coil (MC)","moving iron","SPU headshell-integrated","P-mount","DJ"],"s":"https://ortofon.com/collections/2m-series",
 "x":[
  X("Ortofon SPU","Ortofon","1959",WP+"Ortofon","The first Stereo Pick-Up, a moving-coil cartridge still made in headshell form."),
  X("Denon DL-103","Denon","1962","https://stereophile.com/content/denon-dl-103-phono-cartridge","Low-output moving-coil cartridge developed with Japan's NHK for broadcast use.",
    [("DL-103","Denon","1962","spherical tip"),("DL-103S","Denon","","Shibata tip")]),
  X("Ortofon Concorde","Ortofon","1979",WP+"Ortofon","Integrated-headshell DJ pickup.",[("Concorde","Ortofon","1979",""),("Concorde (second generation)","Ortofon","2018","")]),
  X("Ortofon 2M","Ortofon","2007",WP+"Ortofon","Moving-magnet series with interchangeable styli, colour-coded by grade.",
    [("2M Red","Ortofon","",""),("2M Blue","Ortofon","",""),("2M Bronze","Ortofon","",""),("2M Black","Ortofon","","")]),
  X("Audio-Technica AT95E / VM95","Audio-Technica","","https://the-ear.net/news/end-at95e-era/","Entry moving-magnet cartridge made for 38 years, replaced in 2018 by the VM95 family sharing one body.",
    [("AT95E","Audio-Technica","","38 years in production"),("AT-VM95C","Audio-Technica","2018","entry"),("AT-VM95E","Audio-Technica","2018","direct successor"),("AT-VM95EN","Audio-Technica","2018",""),("AT-VM95ML","Audio-Technica","2018",""),("AT-VM95SH","Audio-Technica","2018",""),("AT-VM95SP","Audio-Technica","2018","78 rpm")]),
  X("Shure M44-7","Shure","","https://www.thestranger.com/music/rip-shure-dj-cartridges-26128554/","DJ moving-magnet cartridge; Shure left the phono market in 2018."),
  X("Grado Prestige cartridges","Grado Labs","",WP+"Grado_Labs","High-output cartridges in ½-inch and P-mount with user-replaceable styli."),
 ],
 "r":[["2M","Ortofon"],["VM95","Audio-Technica"],["OM","Ortofon"],["Cadenza","Ortofon"]]},
{"n":"Tonearm","a":"pickup arm","d":"Arm that carries the cartridge across the record, sold separately for a turntable.","t":["pivoted","unipivot","linear tracking","9-inch","12-inch"],"s":"https://www.rega.co.uk/products/tonearms",
 "x":[
  X("SME 3009 / 3012","SME","1960s",WP+"SME_Limited","SME's first arms, 9- and 12-inch, the standard of the 1960s and 1970s.",
    [("3009","SME","","9-inch"),("3012","SME","","12-inch"),("Series III","SME","1970s",""),("Series V","SME","1986",""),("Series IV","SME","1987","")]),
  X("Linn Ittok LVII","Linn","1979",WP+"Linn_Sondek_LP12","Linn's first own-badge arm (1979–1993), succeeded by the Ekos.",
    [("Ittok LVII","Linn","1979",""),("Basik LVX","Linn","1983","budget arm"),("Ekos","Linn","","successor")]),
  X("Rega RB arms","Rega","",WP+"Rega_Research","One-piece cast arms fitted to Rega decks and supplied to other makers.",
    [("RB250","Rega","","fitted to NAD 533"),("RB220","Rega","",""),("RB330","Rega","",""),("RB3000","Rega","",""),("RB880","Rega","",""),("RB Titanium","Rega","","")]),
 ],
 "m":[["9CC Evolution","Pro-Ject"],["10CC Evolution","Pro-Ject"],["12CC Evolution","Pro-Ject"],["Signature Tonearm","Pro-Ject"]]},
{"n":"Turntable stylus","a":"needle · replacement stylus","d":"Replacement stylus made for a phono cartridge.","t":["spherical","elliptical","Shibata","microline","78 rpm"],"s":"https://www.dutchvinyl.com.au/collections/turntable-cartridges-needles",
 "m":[["AT-VMN95C","Audio-Technica"],["AT-VMN95E","Audio-Technica"],["ATN3600L","Audio-Technica"],["2M Blue Replacement Stylus","Ortofon"],["2M Red Replacement Stylus","Ortofon"]],"r":[["2M","Ortofon"],["VM95","Audio-Technica"]]},
{"n":"Phono preamplifier","a":"phono stage","d":"Stage that raises and equalises a phono cartridge signal to line level.","t":["MM","MC","MM/MC","valve","solid-state"],"s":"https://www.hifi-regler.de/products/plattenspieler/",
 "m":[["Cambridge Audio ALVA Duo","Cambridge Audio"],["Cambridge Audio ALVA Solo","Cambridge Audio"],["NAD PP 2e","NAD"],["NAD PP 4","NAD"],["Phono Box RS2","Pro-Ject"],["Urika II","Linn"]]},
{"n":"Turntable plinth","a":"turntable base · chassis","d":"Base or chassis made to hold one turntable mechanism and its tonearm, sold separately.","t":["solid wood","slate","layered/composite","for idler decks (Garrard, Lenco)","baseboard upgrade"],"s":"https://vintagetechnics.co.uk/",
 "m":[["Trampolin Mk2","Linn"]]},
{"n":"Record cleaning machine","a":"RCM · record washer","d":"Machine that washes vinyl records and removes the fluid, by vacuum or ultrasonic bath.","t":["vacuum","ultrasonic","manual bath"],"s":"https://stereophile.com/content/entry-level-3-page-2",
 "m":[["HW-16.5","VPI"],["Okki Nokki","Audio Classics"],["Mark II","Degritter"],["Humminguru","Humminguru"]]},
]
def B(n,c,f,seg,kf,d,s,sig=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=list(sig)
    return b
brands=[
 B("Garrard","United Kingdom","1915","Heritage manufactory","idler turntables","Swindon turntable maker founded by the jewellers Garrard & Co; brand now owned by SME.",WP+"Garrard_Engineering_and_Manufacturing_Company",["301","401"]),
 B("Thorens","Switzerland","1883","Heritage manufactory","turntables","Founded by Hermann Thorens in Sainte-Croix; now based in Germany.",WP+"Thorens",["TD 124","TD 150"]),
 B("Acoustic Research","United States","1954","Heritage manufactory","acoustic suspension","Cambridge, Massachusetts maker of speakers and the AR XA turntable.",WP+"Acoustic_Research",["AR XA"]),
 B("Linn","United Kingdom","1972","Premium","LP12, streaming","Glasgow hi-fi maker founded by Ivor Tiefenbrun.",WP+"Linn_Products",["Sondek LP12","Ittok"]),
 B("Technics","Japan","","Premium","direct-drive turntables","Panasonic's hi-fi brand.",WP+"Technics_SL-1200",["SL-1200"]),
 B("Bang & Olufsen","Denmark","1925","Premium","design audio","Struer audio maker.","knowledge",["Beogram 4000"]),
 B("Michell","United Kingdom","","Artisan & independent","acrylic turntables","John Michell's engineering firm.","https://hifigear.co.uk/blog/history-of-michell-engineering-founded-by-the-late-john-michell",["GyroDec"]),
 B("Rega","United Kingdom","1973","Premium","turntables, tonearms","Essex maker of Planar turntables and RB arms.",WP+"Rega_Research",["Planar 3","RB300"]),
 B("Pro-Ject","Austria","1991","Mainstream","affordable turntables","Founded by Heinz Lichtenegger in Mistelbach.",WP+"Pro-Ject",["Debut"]),
 B("Ortofon","Denmark","1918","Professional & flagship","cartridges","Copenhagen cartridge maker.",WP+"Ortofon",["SPU","2M","Concorde"]),
 B("Denon","Japan","","Mainstream","hi-fi, DL-103","Japanese audio brand from Nippon Columbia's Denki Onkyo division.","https://stereophile.com/content/denon-dl-103-phono-cartridge",["DL-103"]),
 B("Audio-Technica","Japan","1962","Premium","cartridges, headphones","Tokyo maker of cartridges and headphones.","knowledge",["AT95E","VM95"]),
 B("Shure","United States","1925","Professional & flagship","microphones","Left the phono cartridge market in 2018.","knowledge",["M44-7"]),
 B("Grado Labs","United States","1953","Artisan & independent","cartridges, headphones","Brooklyn family maker.",WP+"Grado_Labs"),
 B("SME","United Kingdom","1946","Professional & flagship","tonearms","Steyning maker founded by Alastair Robertson-Aikman.",WP+"SME_Limited",["3009","Series V"]),
 B("Dual","Germany","1907","Heritage manufactory","turntables","Black Forest maker founded by the Steidinger brothers.",WP+"Dual_(brand)"),
 B("VPI","United States","","Specialist","turntables, record cleaners","American maker of turntables and the HW-16.5 cleaner.","https://stereophile.com/content/entry-level-3-page-2",["HW-16.5"]),
 B("Degritter","Estonia","","Specialist","ultrasonic cleaners","Estonian maker of ultrasonic record cleaners.","https://www.analogplanet.com/node/125900",["Mark II"]),
]
notes=("Turntable list (45 models) turned into 10 archetypes; Technics/Rega/Pro-Ject models became versions. Dropped as near-duplicates: Pro-Ject A1.2, E1 Phono, Juke Box E1, RPM 5 Carbon, T2 Super Phono, T2 W, X8 B; Technics SL-1015/1025/SL-50C; EAT Forte S. "
 "Brief items not attested on a retrieved page and left out: Lenco L75 (forum snippets only), Dual 1019/1219 (Dual article names no models), Braun PS, Clearaudio/VPI archetypes, Koetsu, Lyra, Goldring, Shure V15, AT-OC9, Ortofon RMG-309, Rega RB300 and Planar 3 years, Linn Karousel 2021 (page says March 2020), Keith Monks, Klaudio and Pro-Ject VC-S cleaners. AR XA year from AR article (1963); the LP12 article gives 1961. Plinth kept with types only plus Linn Trampolin baseboard.")
t=p+'.tmp'; json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
