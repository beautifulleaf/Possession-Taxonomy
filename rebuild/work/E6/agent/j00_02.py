import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
CO="Coronado"; L="Lunt Solar Systems"; B="Baader Planetarium"; DS="DayStar Filters"
sol={"n":"Solar telescope","a":"H-alpha telescope","d":"Telescope with a built-in etalon filter made to observe the Sun in hydrogen-alpha light.",
 "t":["single-stack","double-stack"],"s":"https://www.astroshop.eu/solar-observation/solar-telescopes/10_80/m,Coronado",
 "x":[
  X("Coronado PST","Personal Solar Telescope: the small 40 mm H-alpha refractor that made solar prominence viewing affordable.",CO,"","https://skyatnightmagazine.com/reviews/telescopes/coronado-personal-solar-telescope",
    [("PST",CO,"","40 mm, 400 mm, <1 Å etalon; sold under Meade"),("0.5PST",CO,"","narrower-band version, from old data")],"40 mm · <1 Å or 0.5 Å · gold body",a="Personal Solar Telescope"),
  X("Lunt LS THa","Lunt's dedicated H-alpha refractors with an internal tunable etalon and choice of blocking filter.",L,"","https://www.spacegazer.com/lunt-ls60tha/b1200",
    [("LS60THa",L,"","60 mm, internal etalon"),("LS40THa / LS50THa",L,"","smaller sizes, from old data"),("LS60MT / LS80MT / LS100MT / LS130MT",L,"","modular telescopes, from old data")],"35–130 mm · blocking filter B600, B1200, B1800 · single or double stack")],
 "m":[["SolarMax III","Meade Instruments"],["Solar Ranger","Meade Instruments"],["Sol 60",DS],["SolarScout",DS],["Heliostar","Sky-Watcher"]]}
filt={"n":"Solar filter","a":"sun filter","d":"Filter made to fit a telescope, camera or binocular for safe viewing of the Sun.",
 "t":["white-light film filter","white-light glass filter","binocular filter","Herschel wedge","H-alpha eyepiece filter","Ca-K filter"],
 "s":"https://www.highpointscientific.com/baader-astf-100-astrosolar-clearwhite-telescope-solar-filter-100-mm",
 "x":[
  X("Baader AstroSolar","Thin coated safety film, sold as sheets or in ready-made cells; the reference white-light filter material.",B,"","https://www.digitalcameraworld.com/cameras/baader-astrosolar-film-and-filters-review",
    [("AstroSolar film",B,"","OD 5.0 and OD 3.8 sheets"),("AstroSolar ASTF",B,"","telescope filter cell"),("AstroSolar ClearWhite ASSF",B,"",""),("AstroSolar ASBF",B,"","binocular filter")],"OD 5.0 or 3.8 · sheet or cell · aperture size"),
  X("DayStar Quark","H-alpha filter that fits at the eyepiece end of an ordinary refractor.",DS,"","https://www.skyatnightmagazine.com/reviews/eyepieces/daystar-quark-hydrogen-alpha-eyepiece-filters",
    [("Quark Chromosphere",DS,"","0.5–0.3 Å, surface detail"),("Quark Prominence",DS,"","0.8–0.6 Å, prominences")],"for f/4–f/9 refractors · energy-rejection filter above 3 in"),
  X("Herschel wedge","Prism diagonal that sends most sunlight and heat out of the back, for white-light views with a refractor.","","1830s","https://en.wikipedia.org/wiki/Herschel_wedge",[],"used with a neutral-density filter",a="Herschel prism")],
 "m":[["BDSF digital solar filter",B],["Glass Solar Filter 1200","Meade Instruments"],["Helios Solar Glass","Seymour Solar"],["AstroSolar solar filter","Astrozap"],["SF100","euro EMC"],["Solar Filters","Artesky"]]}
ecl={"n":"Eclipse glasses","a":"eclipse viewing glasses · solar viewer","d":"Card or plastic glasses with solar filter film for looking at the Sun; safe ones conform to ISO 12312-2, tested by an accredited lab.",
 "t":["card glasses","plastic-frame glasses","handheld viewer"],"s":"https://eclipse.aas.org/eye-safety/how-to-tell-if-viewers-are-safe"}
brands=[
 {"n":CO,"c":"United States","seg":"Specialist","kf":"H-alpha telescopes","d":"Maker of hydrogen-alpha solar telescopes and filters, owned by Meade from 2004.","sig":["Coronado PST"],"rel":["Meade Instruments","Lunt Solar Systems"],"s":"https://en.wikipedia.org/wiki/Meade_Instruments"},
 {"n":L,"c":"United States","seg":"Specialist","kf":"H-alpha telescopes","d":"Solar telescope maker owned by Andrew Lunt, a former Coronado employee.","sig":["Lunt LS THa"],"rel":["Coronado"],"s":"https://www.spacegazer.com/lunt-ls60tha/b1200"},
 {"n":B,"c":"Germany","seg":"Specialist","kf":"filters, solar film","d":"German maker of astronomy filters and accessories, known for AstroSolar film.","sig":["Baader AstroSolar"],"s":"knowledge"},
 {"n":DS,"c":"United States","seg":"Specialist","kf":"H-alpha filters","d":"American maker of hydrogen-alpha filters including the Quark.","sig":["DayStar Quark"],"s":"knowledge"}]
w('00_02',{"kinds":[sol,filt,ecl],"brands":brands,"traditions":[],
 "notes":"Solar telescope: 13 models → Coronado PST and Lunt LS THa archetypes (PST, 0.5PST and all Lunt models as versions) + 5 m; PST/0.5PST were listed under Meade in old data, now maker Coronado (Meade brand). SolarMax kept as m (no page fetched). Solar filter: Baader AstroSolar (4 old models as versions), DayStar Quark and Herschel wedge archetypes; Ca-K as type. Thousand Oaks glass filters not added (no page retrieved). Eclipse glasses: no models by design; source switched to the AAS safety page (ISO 12312-2)."})
