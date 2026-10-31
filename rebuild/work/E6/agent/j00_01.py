import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
C="Celestron"; M="Meade Instruments"; Q="Questar"; SW="Sky-Watcher"; U="Unistellar"; V="Vaonis"; Z="ZWO"; D="DwarfLab"
AS="https://www.astroshop.eu/telescopes/10/a,Teleskope.Optik.Bauart=Cassegrain/a,Teleskope.Optik.Bauart=Maksutov-Newton/a,Teleskope.Optik.Bauart=Newton/a,Teleskope.Optik.Bauart=Schmidt-Cassegrain/a,Teleskope.Optik.Bauart=Schmidt-Newton"
SS="https://skiesandscopes.com/best-smart-telescopes/"
sct={"n":"Schmidt-Cassegrain telescope","a":"SCT","d":"Catadioptric telescope with a thin Schmidt corrector plate and a folded mirror light path in a short tube.",
 "t":["optical tube only","computerised fork package","GoTo equatorial package","aplanatic (EdgeHD, ACF)"],"s":AS,
 "x":[
  X("Celestron C8","The orange-tube 8-inch f/10 SCT that brought mass-produced Schmidt-Cassegrains to amateurs.",C,"1970","https://en.wikipedia.org/wiki/Celestron",
    [("C8",C,"1970","8-inch f/10, first of the mass-produced line"),("C11 / C14",C,"","11- and 14-inch sizes"),("NexStar SE",C,"","single-arm GoTo package, from old data"),("NexStar Evolution",C,"","app-controlled package"),("CPC",C,"","computerised fork line")],
    "aperture 5–14 in · f/10 · OTA or GoTo package · orange or black tube"),
  X("Celestron EdgeHD","Celestron's aplanatic SCT with a built-in field corrector for a flat imaging field.",C,"","https://en.wikipedia.org/wiki/Celestron",
    [("EdgeHD 8 / 9.25 / 11 / 14",C,"","four apertures")],"8–14 in · f/10"),
  X("Meade LX200 / ACF","Meade's fork-mounted GoTo SCTs, from 2008 with Advanced Coma-Free optics.",M,"","https://en.wikipedia.org/wiki/Meade_Instruments",
    [("LX200-ACF",M,"2008","8–16 in, ACF optics"),("LX90-ACF",M,"","8–12 in")],"8–16 in · fork GoTo")],
 "m":[["NexStar SLT",C],["StarSense Explorer DX 6 AZ",C],["Advanced VX",C],["CGX",C]]}
mak={"n":"Maksutov-Cassegrain telescope","a":"Mak · Maksutov","d":"Catadioptric telescope with a deep meniscus corrector and a folded mirror light path.",
 "t":["spot (Gregory) Maksutov","Rutten Maksutov (Rumak)"],"s":"https://www.highpointscientific.com/telescopes/catadioptric-telescopes/maksutov-cassegrain-telescopes",
 "x":[
  X("Questar 3.5","The 90 mm spot-Maksutov in a fork mount with built-in control box, the icon of the luxury small telescope.",Q,"1954","https://en.wikipedia.org/wiki/Questar_Corporation",
    [("Standard",Q,"1954","tube and fork with RA drive"),("Field Model",Q,"1956","optical tube only"),("Duplex",Q,"","detachable tube"),("Birder",Q,"","terrestrial, faster focusing"),("Questar Seven",Q,"1967","7-inch scaled-up version")],
    "90 mm · f/14 · Pyrex, Zerodur or quartz mirror · broadband coatings · PowerGuide drive",a="Q3.5"),
  X("Meade ETX","Mass-produced small Maksutov on a fork GoTo mount.",M,"1996","https://en.wikipedia.org/wiki/Meade_Instruments",
    [("ETX-90",M,"1996",""),("ETX-105",M,"",""),("ETX-125",M,"","127 mm")],"90–127 mm"),
  X("Sky-Watcher Skymax","Synta-made spot Maksutov sold as a grab-and-go planetary scope.",SW,"","https://www.scopeviews.co.uk/SW127Mak.htm",
    [("Skymax 127",SW,"","127 mm, 1500 mm, F12")],"90–180 mm · OTA or on AZ-GTi / EQ mount"),
  X("Rutten Maksutov (Rumak)","Maksutov with a separate aspheric secondary mirror for a flatter, wider field.","","","https://en.wikipedia.org/wiki/Maksutov_telescope",
    [("Rumak","iOptron","","from old data")],"")],
 "m":[["C90 Mak",C],["NexStar 127 SLT",C],["OMC Maksutov-Cassegrain","Orion Optics UK"],["MAKSYGO-60","Acuter"],["MightyMak","Omegon"]],
 "r":[["NexStar SE",C]]}
sch={"n":"Schmidt astrograph","a":"Schmidt camera · RASA","d":"Catadioptric imaging telescope with a full-aperture Schmidt corrector and a camera at prime focus inside the tube, with no eyepiece position.",
 "s":"https://www.celestron.com/pages/rowe-ackermann-schmidt-astrograph-technology",
 "x":[
  X("Celestron RASA","Rowe-Ackermann Schmidt Astrograph: f/2 imaging-only telescope with a four-element corrector.",C,"2014","https://rothervalleyoptics.co.uk/celestron-8-rowe-ackermann-schmidt-astrograph-rasa-ota.html",
    [("RASA 11",C,"2014","279 mm, 620 mm, f/2.22"),("RASA 11 V2",C,"",""),("RASA 8",C,"","203 mm f/2, 7.7 kg"),("RASA 6",C,"",""),("RASA 36 V2",C,"","36 cm")],"6–14 in · f/2–2.2 · camera at front"),
  X("Schmidt camera","Bernhard Schmidt's wide-field photographic telescope with a corrector plate and spherical mirror.","","1930","https://en.wikipedia.org/wiki/Schmidt_camera",
    [("8-inch Schmidt camera",C,"early 1970s","factory-focused film camera, about 300 made")],"")]}
smart={"n":"Smart telescope","a":"imaging telescope · all-in-one telescope","d":"Self-aligning telescope with a camera and no eyepiece that shows the sky in an app.",
 "t":["refractor type","reflector type","with eyepiece-style viewer"],"s":AS,
 "x":[
  X("Vaonis Stellina","The first app-driven all-in-one smart telescope.",V,"2018","https://scopetrader.com/ultimate-smart-telescope-showdown/",
    [("Stellina",V,"2018","80 mm")],"80 mm · white body"),
  X("Unistellar eVscope","Reflector smart telescope with an electronic eyepiece showing live stacked images.",U,"2017","https://en.wikipedia.org/wiki/Unistellar",
    [("eVscope",U,"2017","114 mm; prototype shown at CES 2017"),("eVscope 2",U,"2022","114 mm"),("eQuinox",U,"",""),("eQuinox 2",U,"2023","114 mm"),("Odyssey",U,"2024","85 mm"),("Odyssey Pro",U,"","")],"85–114 mm"),
  X("Vaonis Vespera","Compact smaller sibling of the Stellina; CES 2021 Innovation Award.",V,"","https://www.space.com/vaonis-vespera-smart-telescope",
    [("Vespera",V,"",""),("Vespera II",V,"",""),("Vespera III",V,"",""),("Vespera Pro",V,"",""),("Vespera Pro 2",V,"2026","50 mm")],"50 mm"),
  X("ZWO Seestar","Low-cost compact smart telescope that made the category mass-market.",Z,"","https://skiesandscopes.com/best-smart-telescopes/",
    [("Seestar S50",Z,"","50 mm"),("Seestar S30",Z,"","30 mm"),("Seestar S30 Pro",Z,"2026","30 mm"),("Seestar S50 Pro",Z,"2026","50 mm, successor to S50")],"30–50 mm"),
  X("DWARF","Palm-sized dual-camera smart telescope.",D,"","https://skiesandscopes.com/best-smart-telescopes/",
    [("DWARF 3",D,"2024","35 mm"),("DWARF Mini",D,"2025","30 mm"),("Draco",D,"","from old data")],"30–35 mm"),
  X("Celestron Origin","Celestron's app-controlled smart telescope.",C,"","https://en.wikipedia.org/wiki/Celestron",
    [("Origin",C,"",""),("Origin Mark II",C,"","")],"")],
 "m":[["Hestia",V],["Atlas",V]]}
brands=[
 {"n":C,"c":"United States","f":"1964","seg":"Mainstream","kf":"Schmidt-Cassegrains","d":"Torrance, California telescope maker founded by Tom Johnson, owned by Synta since 2005.","sig":["Celestron C8","Celestron EdgeHD","Celestron RASA"],"rel":["Sky-Watcher"],"s":"https://en.wikipedia.org/wiki/Celestron"},
 {"n":M,"c":"United States","f":"1972","seg":"Mainstream","kf":"GoTo telescopes","d":"Watsonville, California maker of SCTs and the ETX; ceased operating in 2024.","sig":["Meade LX200 / ACF","Meade ETX"],"s":"https://en.wikipedia.org/wiki/Meade_Instruments"},
 {"n":Q,"c":"United States","f":"1950","seg":"Heritage manufactory","kf":"Maksutov telescopes","d":"New Hope, Pennsylvania maker of the Questar 3.5 Maksutov, founded by Lawrence Braymer.","sig":["Questar 3.5"],"s":"https://en.wikipedia.org/wiki/Questar_Corporation"},
 {"n":SW,"c":"China","f":"1999","seg":"Mainstream","kf":"telescopes, mounts","d":"Synta's telescope brand, made in Suzhou.","sig":["Sky-Watcher Skymax"],"s":"https://en.wikipedia.org/wiki/Sky-Watcher"},
 {"n":U,"c":"France","f":"2015","seg":"Specialist","kf":"smart telescopes","d":"Marseille maker of the eVscope smart telescopes.","sig":["Unistellar eVscope"],"s":"https://en.wikipedia.org/wiki/Unistellar"},
 {"n":V,"c":"France","seg":"Specialist","kf":"smart telescopes","d":"French maker of the Stellina and Vespera smart telescopes.","sig":["Vaonis Stellina","Vaonis Vespera"],"s":"knowledge"},
 {"n":Z,"c":"China","seg":"Specialist","kf":"astronomy cameras","d":"Chinese maker of astronomy cameras, mounts and the Seestar smart telescopes.","sig":["ZWO Seestar"],"s":"knowledge"},
 {"n":D,"c":"China","seg":"Specialist","kf":"smart telescopes","d":"Chinese maker of the DWARF palm-sized smart telescopes.","sig":["DWARF"],"s":"knowledge"}]
w('00_01',{"kinds":[sct,mak,sch,smart],"brands":brands,"traditions":[],
 "notes":"SCT: 9 models → C8, EdgeHD, Meade LX200/ACF archetypes + 4 m (mount bundles kept as m). Maksutov: Questar 3.5, Meade ETX, Skymax, Rumak archetypes; dropped starter SKUs Explore Scientific FirstLight Mak, Sky-Watcher Starquest DX EQ, Acuter Voyager MAK127 traverse bundle; ETX range became an archetype. Intes/Intes-Micro not added (no retrieved page naming models). Schmidt astrograph: RASA (all four old models as versions) and Schmidt camera. Smart telescope: 23 models → 6 archetypes (Stellina, eVscope, Vespera, Seestar, DWARF, Origin) + Hestia, Atlas in m; Seestar S50 and S30 years not confirmed on a fetched page so left blank."})
