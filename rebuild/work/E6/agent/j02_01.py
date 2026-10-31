import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
SO="Swarovski Optik"; CZ="Carl Zeiss"; LC="Leica Camera"; KW="Kowa"; PU="Pulsar"; HM="HIKMICRO"; GS="Guide Sensmart (Wuhan Guide Sensmart Tech)"
OT="https://www.optics-trade.eu/blog/pulsar-thermal-monoculars-axion-and-helion/"
spot={"n":"Spotting scope","a":"birding scope · field scope","d":"Compact single-tube telescope for daytime viewing of distant things, used on a tripod or rest.",
 "t":["angled (45°) eyepiece","straight-through","zoom eyepiece","fixed eyepiece","ED or fluorite objective","modular (swap objective)","digiscoping adapter"],
 "s":"https://www.adorama.com/l/Binoculars-and-Telescopes/Spotting-Scopes",
 "x":[
  X("Swarovski ATX modular scope","Modular scope: an angled, straight or binocular eyepiece module fitted to a choice of objective modules.",SO,"","https://Birdguides.Com/reviews/optics/swarovski-115-mm-atx-stx-btx-objective-module/",
    [("ATX",SO,"","angled eyepiece module"),("STX",SO,"","straight eyepiece module"),("BTX",SO,"","binocular eyepiece module"),("115 mm objective module",SO,"","30–70×, 2,100 g")],
    "objective modules 65, 85, 95, 115 mm · 25–60× or 30–70×"),
  X("Kowa Prominar TSN","Kowa's flagship scopes with a pure-fluorite-crystal element, in angled and straight bodies.",KW,"","https://www.bhphotovideo.com/c/product/1724920-REG/kowa_tsn_88a_88mm_prominar_pure.html",
    [("TSN-88A",KW,"","88 mm, angled, magnesium body"),("TSN-88S",KW,"","88 mm, straight"),("TSN-99 Prominar",KW,"","from old data"),("TSN-66S Prominar",KW,"","from old data")],"66–99 mm · eyepiece sold separately (TE-11WZ II zoom)"),
  X("Zeiss Harpia","Zeiss's top scope with the zoom built into the body behind the objective and a fixed eyepiece.",CZ,"","https://www.scopeviews.co.uk/ZeissHarpia95.htm",
    [("Harpia 85",CZ,"",""),("Harpia 95",CZ,"","")],"23–70× body zoom"),
  X("Leica APO-Televid","Leica's apochromatic spotting scope with zoom eyepiece.",LC,"","https://digitalcameraworld.com/reviews/leica-apo-televid-82",
    [("APO-Televid 82",LC,"","")],"82 mm · zoom eyepiece")],
 "m":[["Conquest Gavia 85",CZ],["Televid HD 82",LC],["ATS HD",SO],["STS HD",SO],["STR",SO],["TSN-82SV",KW],["PF-80EDA","Pentax"],["PF-100ED","Pentax"],["Viper HD","Vortex Optics"],["Crossfire HD","Vortex Optics"],
     ["Prostaff 5 spotting scope","Nikon"],["Mark 4 spotting scope","Leupold & Stevens"],["Nature-Trek","Hawke Sport Optics"],["Ultima 80","Celestron"],["REGAL M2","Celestron"],["Ares G2 UHD","Athlon Optics"],["Forge spotting scope","Bushnell"],["Geoma III ED","Vixen"]]}
nv={"n":"Night-vision viewer","a":"night vision · NVD","d":"Handheld or head-worn viewer that amplifies faint light to show a scene in the dark; weapon sights are under Weapons.",
 "t":["Gen 1","Gen 2 (microchannel plate)","Gen 3 (gallium arsenide)","autogated Gen 3 ('Gen 4')","digital","monocular","binocular (BNVD)","head-mount"],
 "s":"https://shop.armasight.com/night-vision/shop-by-series/?page=2",
 "x":[X("AN/PVS-14","US military Gen 3 night-vision monocular, hand-held or head-mounted; the reference civilian NV monocular pattern.","","2000","https://en.wikipedia.org/wiki/AN/PVS-14",
    [("PVS14","ATN Corp (American Technologies Network)","",""),("PVS-14","Armasight","","")],"Gen 3 tube · head mount or hand-held")],
 "m":[["BNVD-51","Armasight"],["Opsin","SiOnyx"]]}
th={"n":"Thermal-imaging viewer","a":"thermal viewer · thermal monocular","d":"Viewer that shows a scene by the heat it gives off, used by hunters, naturalists and walkers; weapon sights are under Weapons.",
 "t":["monocular","binocular","with laser rangefinder","sensor resolution (160×120 to 1024×768)"],
 "s":"https://pulsarvision.com/products/thermal-imaging-monoculars/",
 "x":[
  X("Pulsar Helion","Pulsar's higher-end thermal monocular line, in top XP and more affordable XQ ranges.",PU,"",OT,
    [("Helion XP50",PU,"",""),("Helion XP38",PU,"",""),("Helion XQ50F",PU,"",""),("Helion XQ38F",PU,"","")],"38 or 50 mm lens"),
  X("Pulsar Axion","Pulsar's compact entry-level thermal monocular line, launched 2019.",PU,"2019",OT,
    [("Axion XM30",PU,"2019",""),("Axion XM38",PU,"2019","discontinued 2019"),("Axion Key XM30",PU,"",""),("Axion Compact",PU,"","from old data")],"compact · 30–38 mm lens"),
  X("HIKMICRO Lynx","Compact handheld thermal monoculars from Hikvision's outdoor brand.",HM,"","https://www.optics-trade.eu/blog/hikmicro-lynx-l15-thermal-imaging-monocular-review-optics-trade-reviews/",
    [("LYNX-L15",HM,"","384×288 sensor, 15 mm lens, IP67")],"IP67 · built-in battery"),
  X("FLIR Scout TK","Low-priced pocket thermal monocular that brought thermal viewing to a consumer price.","FLIR","2016","https://www.pcworld.com/article/418967/flirs-scout-tk-is-an-affordable-thermal-monocular.html",
    [("Scout TK","FLIR","2016","160×120, $599 at launch")],"")],
 "m":[["TrackIR 35",GS],["TrackIR Pro 25",GS],["TD410",GS],["Eye C2W","InfiRay"],["Telos",PU],["Krypton 2",PU],["Oryx LRF",PU]]}
brands=[
 {"n":SO,"c":"Austria","f":"1949","seg":"Premium","kf":"binoculars, scopes","d":"Absam, Tyrol maker of premium binoculars, spotting scopes and riflescopes.","sig":["Swarovski ATX modular scope"],"s":"https://en.wikipedia.org/wiki/Swarovski_Optik"},
 {"n":KW,"c":"Japan","seg":"Specialist","kf":"spotting scopes","d":"Japanese company whose optics division makes Prominar fluorite spotting scopes.","sig":["Kowa Prominar TSN"],"s":"knowledge"},
 {"n":CZ,"c":"Germany","f":"1846","seg":"Premium","kf":"optics","d":"German optics maker of Victory and Conquest binoculars and Harpia scopes.","sig":["Zeiss Harpia"],"s":"knowledge"},
 {"n":LC,"c":"Germany","seg":"Premium","kf":"cameras, sport optics","d":"Wetzlar optics maker, formerly Leitz.","sig":["Leica APO-Televid"],"s":"https://en.wikipedia.org/wiki/Trinovid"},
 {"n":PU,"seg":"Specialist","kf":"thermal, night vision","d":"Maker of affordable night-vision and thermal optics for hunters and naturalists.","sig":["Pulsar Helion","Pulsar Axion"],"s":OT},
 {"n":HM,"c":"China","seg":"Specialist","kf":"thermal imaging","d":"Hikvision's outdoor thermal-imaging brand.","sig":["HIKMICRO Lynx"],"s":"knowledge"},
 {"n":"FLIR","c":"United States","seg":"Professional & flagship","kf":"thermal imaging","d":"American thermal-imaging maker whose Scout line serves consumers.","sig":["FLIR Scout TK"],"s":"knowledge"}]
w('02_01',{"kinds":[spot,nv,th],"brands":brands,"traditions":[],
 "notes":"Spotting scope: 36 flat models -> 4 archetypes (Swarovski ATX, Kowa Prominar TSN, Zeiss Harpia, Leica APO-Televid) + 18 m; dropped Acuter Nature Close, Athlon Talos, Bushnell Nitro and Prime, Celestron TrailSeeker, Hawke Vantage, Levenhuk Blaze Base, Pentax PF-85EDA and PF-65EDA II, Sun Optics Range Pro, Vortex Recon RT155, Swarovski AT Endura (minor or duplicative); old range 'Televid' replaced by the archetype. Vortex Razor HD and Swarovski ATS archetypes not built (no fetched page; ATS HD stays in m). Night vision: PVS-14 archetype (ATN and Armasight versions); generations and digital as types; SiOnyx Opsin added from the Wikipedia page; ATN/Pulsar NV lines not added (no page). Thermal: TrackIR cut from 6 to 2 plus Guide TD410; old range TrackIR dropped; InfiRay Eye C2W added (named in fetched review). Weapon sights left to Weapons. No traditions."})
