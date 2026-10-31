import json, os
p='/home/user/Possession-Taxonomy/rebuild/work/D3/shelves/00_00.json'
WP='https://en.wikipedia.org/wiki/'
SH=('https://www.sennheiser.com/en-ie/about-us/our-history')
BY='https://blog-en.beyerdynamic.com/spotlight-on-our-headphones-87-years-of-headphones-expertise/'
def X(n,mk,y,s,d,v=(),a="",dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),vv)) for vv in v]}
    if dt: x["dt"]=dt
    return x
kinds=[
{"n":"Open-back headphones","a":"over-ear open-back headphone · semi-open headphone","d":"Headphone whose cups enclose the ear and are open at the back; semi-open files here.",
 "t":["dynamic","planar magnetic","semi-open"],"s":"https://mezeaudio.com/pages/headphones",
 "x":[
  X("Sennheiser HD 580 / HD 600 / HD 650 lineage","Sennheiser","1990s","https://stereophile.com/content/very-important-sennheiser-hd-580-hd-600-and-hd-650",
    "Sennheiser's open dynamic reference family that founded the enthusiast headphone hobby.",
    [("HD 580","Sennheiser","","founding model"),("HD 580 Jubilee","Sennheiser","","50th-anniversary edition"),("HD 600","Sennheiser","",""),("HD 650","Sennheiser","",""),("HD 660S","Sennheiser","","later version"),("HD 560S","Sennheiser","","entry relative")],dt="cable · pads · grille finish"),
  X("Sennheiser HD 800","Sennheiser","",SH,"Large open dynamic flagship with angled drivers, Sennheiser's audiophile reference.",
    [("HD 800","Sennheiser","",""),("HD 800 S","Sennheiser","","current flagship open-back")]),
  X("Beyerdynamic DT 880 / DT 990","Beyerdynamic","1980s",BY,"Beyerdynamic's first hi-fi headphones; semi-open DT 880 and open DT 990, in hi-fi, PRO and Edition forms.",
    [("DT 880","Beyerdynamic","1980s","semi-open; first dynamic headphone with electrostatic-like playback"),("DT 990","Beyerdynamic","1980s","open"),("DT 880 Pro","Beyerdynamic","","spring-steel PRO version"),("DT 990 Pro","Beyerdynamic","",""),("DT 990 Pro X","Beyerdynamic","",""),("DT 900 Pro X","Beyerdynamic","2021","STELLAR.45 driver")],dt="impedance 32/250/600 ohm · PRO or Edition"),
  X("Beyerdynamic T1 (Tesla)","Beyerdynamic","2009",BY,"High-end open headphone built on the Tesla driver system.",
    [("T1","Beyerdynamic","2009","presented at IFA Berlin"),("T1 Tesla (third generation)","Beyerdynamic","2020",""),("DT 1990 Pro MKII","Beyerdynamic","","studio Tesla model")]),
  X("AKG K240","AKG","","https://en.wikipedia.org/wiki/AKG_(company)","Semi-open studio headphone used by many recording studios for monitoring and playback."),
  X("AKG K701 / K702","AKG","","https://en.wikipedia.org/wiki/AKG_(company)","Open reference headphone family widely used in studios; white K701, black K702 with removable cord.",
    [("K701","AKG","","white"),("K702","AKG","","black, removable cord"),("Q701","AKG","","detachable cable, colours"),("K712 Pro","AKG","",""),("K612 Pro","AKG","","")]),
  X("AKG K1000","AKG","","https://en.wikipedia.org/wiki/AKG_(company)","Fully open former AKG flagship with drivers held away from the ear; no longer produced."),
  X("Audeze LCD series","Audeze","2010","https://www.headfonia.com/audeze-lcd2-classic-review/","Large planar-magnetic open headphones that revived the planar type.",
    [("LCD-2","Audeze","2010",""),("LCD-X","Audeze","",""),("LCD-4","Audeze","",""),("LCD-24","Audeze","",""),("LCD-GX","Audeze","","gaming-oriented"),("LCD-MX4","Audeze","","")]),
  X("HiFiMAN HE-6 / HE1000 / Susvara","HiFiMAN","","https://www.theabsolutesound.com/articles/hifiman-susvara-planar-magnetic-headphone/","HiFiMAN's planar-magnetic flagships, from the hard-to-drive HE-6 to the Susvara (first shown as Edition 6, CES 2017).",
    [("HE6","HiFiMAN","","circular drivers, gold voice-coil traces"),("HE1000 V2","HiFiMAN","","window-shade grilles"),("Susvara","HiFiMAN","2017","flagship"),("HE500","HiFiMAN","",""),("HE400i","HiFiMAN","",""),("Sundara","HiFiMAN","",""),("Ananda","HiFiMAN","",""),("Arya","HiFiMAN","",""),("Deva","HiFiMAN","","")]),
  X("Focal Utopia","Focal","2016","https://www.theabsolutesound.com/articles/focal-utopia-2022-headphones/","Open dynamic flagship with 40 mm pure beryllium M-shaped dome drivers.",
    [("Utopia","Focal","2016","original, launched with the Elear"),("Utopia 2022","Focal","2022","copper-aluminium voice coil"),("Elear","Focal","2016","sibling"),("Clear","Focal","",""),("Clear MG","Focal","","")]),
 ],
 "m":[["ATH-ADX5000","Audio-Technica"],["ATH-R70x","Audio-Technica"],["Diana Phi","Abyss"],["D8000","Final Audio"],["TH909","Fostex"],["105 AER","Meze Audio"],["109 PRO","Meze Audio"],["ELITE","Meze Audio"],["EMPYREAN II","Meze Audio"],["Para","Moondrop Audio"],["Phoenix","Sivga"],["MDR-SA5000","Sony"],["Auteur","ZMF Headphones"],["Verite","ZMF Headphones"],["AH-D5000","Denon"]]},
{"n":"Closed-back headphones","a":"over-ear closed-back headphone · studio monitor headphone","d":"Headphone whose sealed cups enclose the ear.","t":["dynamic","planar magnetic"],"s":"https://mezeaudio.com/pages/headphones",
 "x":[
  X("Koss SP/3 and Pro4","Koss Corporation","1958","https://en.wikipedia.org/wiki/Koss_Corporation","Koss's sealed stereo headphones that started hi-fi stereo headphone listening.",
    [("SP/3","Koss Corporation","1958","first"),("Pro4 Stereophones","Koss Corporation","1962",""),("Pro4AA","Koss Corporation","1970",""),("Pro4S","Koss Corporation","2014","")]),
  X("Beyerdynamic DT 100","Beyerdynamic","1965",BY,"Closed monitoring headphone for recording studios, still widely used."),
  X("Beyerdynamic DT 770","Beyerdynamic","1980s",BY,"Closed member of Beyerdynamic's first hi-fi trio, standard studio and home closed-back.",
    [("DT 770","Beyerdynamic","1980s","hi-fi original"),("DT 770 Pro","Beyerdynamic","","PRO version with metal brackets; 80/250 ohm"),("DT 770 M","Beyerdynamic","","isolating monitor version"),("DT 770 Pro X","Beyerdynamic","2024","anniversary model, STELLAR.45 driver"),("DT 700 Pro X","Beyerdynamic","2021",""),("DT 1770 Pro MKII","Beyerdynamic","","Tesla studio model"),("T5p","Beyerdynamic","","closed counterpart of the T1")],dt="impedance 32/80/250 ohm"),
  X("Sony MDR-V6 / MDR-7506","Sony","1985","https://en.wikipedia.org/wiki/Sony_MDR-V6","Folding closed studio headphone that became an industry standard for engineers and broadcasting.",
    [("MDR-V6","Sony","1985","discontinued 2020"),("MDR-7506","Sony","1991","professional version, same driver"),("MDR-V600","Sony","1993","DJ version"),("MDR-7509HD","Sony","","larger driver"),("MDR-CD900ST","Sony","","Japanese studio relative")]),
  X("Audio-Technica ATH-M50","Audio-Technica","2007","https://audio-technica.com/en-gb/press/the-story-behind-the-legendary-m50x","Closed professional monitor headphone with 45 mm drivers, Audio-Technica's best seller.",
    [("ATH-M50","Audio-Technica","2007","launched at NAMM"),("ATH-M50x","Audio-Technica","2014","detachable cable"),("ATH-M50xBT","Audio-Technica","2018","Bluetooth"),("ATH-M40x","Audio-Technica","","sibling"),("ATH-M70x","Audio-Technica","","sibling")],dt="limited colourways since 2012"),
 ],
 "m":[["K371","AKG"],["LCD-XC","Audeze"],["DT 150","Beyerdynamic"],["DT 250","Beyerdynamic"],["AH-D5200","Denon"],["Stellia","Focal"],["Radiance","Focal"],["TH900","Fostex"],["TH610","Fostex"],["99 CLASSICS","Meze Audio"],["LIRIC","Meze Audio"],["NDH 20","Neumann"],["SRH840","Shure"],["SRH1540","Shure"],["SRH440","Shure"],["MDR-Z1R","Sony"],["MDR-1AM2","Sony"],["Verite Closed","ZMF Headphones"],["MK801","1MORE"]]},
{"n":"Wireless noise-cancelling headphones","a":"ANC headphones · Bluetooth noise-cancelling headphones","d":"Wireless over-ear headphone with active noise cancellation, chosen for travel and commuting.",
 "t":["over-ear","on-ear"],"s":"https://www.rtings.com/headphones/reviews/best/by-feature/noise-cancelling",
 "x":[
  X("Bose QuietComfort","Bose","","https://en.wikipedia.org/wiki/List_of_Bose_headphones","Bose's noise-cancelling headphone line, the long-running travel reference.",
    [("QuietComfort 35 II","Bose","2017",""),("Noise Cancelling Headphones 700","Bose","2019",""),("QuietComfort 45","Bose","2021",""),("QuietComfort","Bose","2023",""),("QuietComfort Ultra","Bose","2023",""),("QuietComfort Ultra (2nd Gen)","Bose","2025","")]),
  X("Sony 1000X","Sony","2016","https://experience.sony-asia.com/sg/home/exploredetail/1328","Sony's flagship wireless noise-cancelling headphone line, repeatedly top of independent tests.",
    [("MDR-1000X","Sony","2016","first generation"),("WH-1000XM2","Sony","2017","adaptive noise cancelling"),("WH-1000XM3","Sony","2018",""),("WH-1000XM4","Sony","2020",""),("WH-1000XM5","Sony","2022","redesign, eight microphones"),("WH-1000XM6","Sony","2025","12 microphones, folding; RTINGS top pick"),("1000X The Collexion","Sony","2026","premium design")]),
  X("Apple AirPods Max","Apple","2020","https://en.wikipedia.org/wiki/AirPods_Max","Apple's over-ear wireless headphone with active noise cancellation and transparency mode.",
    [("AirPods Max (Lightning)","Apple","2020",""),("AirPods Max (USB-C)","Apple","2024",""),("AirPods Max 2","Apple","2026","H2 chip")]),
  X("Sennheiser Momentum","Sennheiser","2012",SH,"Sennheiser's consumer headphone series, later wireless with noise cancelling.",
    [("Momentum","Sennheiser","2012","first series"),("Momentum 3 Wireless","Sennheiser","","")]),
 ],
 "m":[["Soundcore Space Q45","Anker"],["Live 780NC","JBL"],["HDB 630","Sennheiser"]]},
{"n":"Electrostatic headphones","a":"electrostat · earspeaker","d":"Headphone with a thin charged diaphragm between stators, driven by a dedicated high-voltage energiser.",
 "t":["normal-bias","pro-bias","with energiser (system)"],"s":"https://en.wikipedia.org/wiki/List_of_Stax_products",
 "x":[
  X("Stax SR-1","Stax Ltd","1960","https://en.wikipedia.org/wiki/List_of_Stax_products","Stax's first electrostatic earspeaker, the start of the type."),
  X("Stax Lambda","Stax Ltd","1979","https://en.wikipedia.org/wiki/List_of_Stax_products","Rectangular-driver electrostatic earspeaker series, Stax's long-running core range.",
    [("SR-Lambda","Stax Ltd","1979",""),("SR-Lambda Pro","Stax Ltd","1982",""),("SR-Lambda Signature","Stax Ltd","1987",""),("SR-404 Signature","Stax Ltd","1999",""),("SR-507","Stax Ltd","2010",""),("SR-L700","Stax Ltd","2015",""),("SR-L300","Stax Ltd","2016",""),("SR-L700MK2","Stax Ltd","2019","")]),
  X("Stax Omega","Stax Ltd","1993","https://en.wikipedia.org/wiki/List_of_Stax_products","Round-driver flagship electrostatic series.",
    [("SR-Omega","Stax Ltd","1993","original"),("SR-007","Stax Ltd","1998",""),("SR-007Mk2","Stax Ltd","2007",""),("SR-009","Stax Ltd","2011",""),("SR-009S","Stax Ltd","2018",""),("SR-X9000","Stax Ltd","2021","current flagship")]),
  X("Sennheiser Orpheus","Sennheiser","1991",SH,"Limited-edition electrostatic headphone system with its own amplifier; succeeded by the HE 1.",
    [("Orpheus (HE 90)","Sennheiser","1991","limited edition"),("HE 1","Sennheiser","2015","successor")]),
  X("HiFiMAN Shangri-La","HiFiMAN","","https://www.theabsolutesound.com/articles/hifiman-susvara-planar-magnetic-headphone/","Cost-no-object electrostatic headphone system."),
 ],
 "m":[["SR-4070","Stax Ltd"]]},
{"n":"On-ear headphones","a":"supra-aural headphone","d":"Headphone whose pads rest on the ear.","t":["open","closed"],"s":"https://www.sweetwater.com/brand/beyerdynamic/headphones",
 "x":[
  X("Sennheiser HD 414","Sennheiser","1968",SH,"Lightweight on-ear headphone, called the world's first open-back headphone."),
  X("Koss Porta Pro","Koss Corporation","1984","https://en.wikipedia.org/wiki/Koss_Corporation","Portable high-end on-ear headphone in continuous production since 1984.",
    [("Porta Pro","Koss Corporation","1984",""),("Sporta Pro","Koss Corporation","1999","tilting headband"),("PortaPro Wireless","Koss Corporation","2018",""),("PortaPro Wireless 2.0","Koss Corporation","2024",""),("KSC75","Koss Corporation","2004","ear-clip relative")]),
  X("Grado SR / Prestige","Grado Labs","","https://en.wikipedia.org/wiki/Grado_Labs","Grado's open on-ear headphones from the entry SR60 to the wooden RS1 and GS models.",
    [("SR60","Grado Labs","",""),("SR60e","Grado Labs","2014","e series"),("SR80","Grado Labs","",""),("SR80e","Grado Labs","2014","e series"),("SR325","Grado Labs","",""),("RS1","Grado Labs","","wood"),("GS1000","Grado Labs","",""),("PS1000","Grado Labs","",""),("HP1000","Grado Labs","","Joseph Grado's first headphone"),("GW100","Grado Labs","","wireless")]),
  X("Sennheiser HD 25","Sennheiser","1988",SH,"Closed on-ear monitor headphone, a DJ-booth favourite.",
    [("HD 25 Plus","Sennheiser","",""),("Amperior","Sennheiser","","")]),
  X("Beats Solo","Beats","","https://www.soundstagesolo.com/index.php/equipment/headphones/427-beats-solo-4-on-ear-headphones","Beats' best-selling fashion on-ear headphone line.",
    [("Solo 4","Beats","2024","40 mm drivers, 50-hour battery")]),
 ],
 "m":[["Sine DX","Audeze"],["Aventho 100","Beyerdynamic"],["DT 275 Pro","Beyerdynamic"],["PRO DJ100","Koss Corporation"],["MDR-7510","Sony"]]},
{"n":"Headset","a":"gaming headset · office headset · headphones with microphone","d":"Headphones with an attached microphone, whatever they are used for.","t":["gaming","office/UC","wired","wireless"],"s":"https://www.sweetwater.com/brand/beyerdynamic/headphones",
 "m":[["Maxwell 2","Audeze"],["BlackShark V3 Pro","Razer"],["Arctis Nova 7 Wireless","SteelSeries"],["Stealth 600 (Gen 3)","Turtle Beach"],["QuietComfort 35 II Gaming","Bose"],["MMX 100 Wireless","Beyerdynamic"]]},
]
def B(n,c,f,seg,kf,d,s,sig=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=list(sig)
    return b
brands=[
 B("Sennheiser","Germany","1945","Professional & flagship","headphones, microphones","Wedemark audio company founded as Labor W by Fritz Sennheiser; consumer division sold to Sonova in 2021.",WP+"Sennheiser",["HD 600","HD 800","Orpheus","HD 414","HD 25"]),
 B("Beyerdynamic","Germany","1924","Professional & flagship","studio headphones","Heilbronn headphone and microphone maker founded by Eugen Beyer in Berlin.",WP+"Beyerdynamic",["DT 770","DT 880","DT 990","T1"]),
 B("AKG","Austria","1947","Professional & flagship","studio headphones","Vienna headphone and microphone maker founded by Rudolf Görike and Ernst Pless.","https://en.wikipedia.org/wiki/AKG_(company)",["K240","K701","K1000"]),
 B("Koss Corporation","United States","1953","Mainstream","stereo headphones","Milwaukee maker credited with the first hi-fi stereo headphones (SP/3, 1958).",WP+"Koss_Corporation",["Pro4AA","Porta Pro"]),
 B("Grado Labs","United States","1953","Artisan & independent","open on-ear headphones","Brooklyn family maker of headphones and phono cartridges.",WP+"Grado_Labs",["SR60","RS1"]),
 B("Stax Ltd","Japan","","Specialist","electrostatic headphones","Japanese maker of electrostatic earspeakers and energisers since 1960; owned by Edifier since 2011.",WP+"List_of_Stax_products",["Lambda","SR-009"]),
 B("Sony","Japan","1946","Mainstream","consumer electronics","Japanese electronics group; studio MDR headphones and the 1000X noise-cancelling line.","knowledge",["MDR-7506","WH-1000X"]),
 B("Audio-Technica","Japan","1962","Premium","monitor headphones, cartridges","Tokyo maker of headphones, microphones and phono cartridges.","knowledge",["ATH-M50"]),
 B("HiFiMAN","China","","Specialist","planar headphones","Planar-magnetic headphone maker, from the HE-5/HE-6 to the Susvara and Shangri-La.","https://www.theabsolutesound.com/articles/hifiman-susvara-planar-magnetic-headphone/",["HE6","Susvara"]),
 B("Audeze","United States","2008","Specialist","planar headphones","Californian planar-magnetic headphone maker; acquired by Sony Interactive Entertainment in 2023.","https://www.headfonia.com/audeze-lcd2-classic-review/",["LCD-2"]),
 B("Focal","France","","Premium","loudspeakers, headphones","French loudspeaker maker that entered high-end headphones in 2016 with Utopia and Elear.","https://www.theabsolutesound.com/articles/focal-utopia-2022-headphones/",["Utopia"]),
 B("Bose","United States","1964","Premium","noise cancelling","American audio company known for QuietComfort noise-cancelling headphones.","knowledge",["QuietComfort"]),
 B("Apple","United States","1976","Premium","consumer electronics","American technology company; AirPods range.","knowledge",["AirPods Max"]),
 B("Beats","United States","2006","Mainstream","fashion headphones","Headphone brand co-founded by Dr. Dre and Jimmy Iovine, owned by Apple since 2014.","knowledge",["Solo"]),
]
notes=("Old flat lists turned into archetypes with versions; leftovers kept in m (≤20). AirPods range moved out of Closed-back (earbuds belong in True wireless earbuds, shelf 00_01); AirPods Max now in Wireless noise-cancelling. "
 "MDR-CD900ST moved from On-ear to Closed-back as a relative of MDR-7506 (it is circumaural). Stax SR-007/009/404/507/4070 moved from Open-back to Electrostatic headphones; Sennheiser HE-1 likewise. Dropped duplicate entries only (ThieAudio-style repeats none here). "
 "Years left blank where no retrieved page gave them (HD 580/600/650 years conflict across sources). Gaming headset picks from RTINGS gaming page; office headsets not sourced, so only types. Wikidata helper returned HTTP 429 throughout.")
t=p+'.tmp'; json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
