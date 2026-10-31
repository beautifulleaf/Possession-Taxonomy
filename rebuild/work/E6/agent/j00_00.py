import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
T="Takahashi Seisakusho"; TV="Tele Vue Optics"; SW="Sky-Watcher"; WP="https://en.wikipedia.org/wiki/"
refr={"n":"Refractor telescope","a":"refracting telescope · apo · achromat","d":"Telescope that gathers light with a lens objective.",
 "t":["achromat","apochromat (ED or fluorite)","Petzval astrograph","doublet","triplet","quadruplet"],
 "s":"https://www.highpointscientific.com/telescopes/refracting-telescopes",
 "x":[
  X("Takahashi FC fluorite doublet","Air-spaced Steinheil doublet with a fluorite crown at the back; the refractor that made Takahashi's name.",T,"1981","https://www.scopeviews.co.uk/TakFC-100Classic.htm",
    [("FC-100",T,"1981","original F8 fluorite doublet"),("FC-50, FC-60, FC-76, FC-125",T,"1980s","F8 sister sizes"),("FS-102",T,"early 1990s","FS series successor, F8.1"),("FS-60",T,"early 1990s","F6, replaced the FC-60"),("FC-76D",T,"","modern Steinheil revival"),("FC-100DC / FC-100DF",T,"","F7.4"),("FC-100DZ",T,"2020","800 mm, F8"),("FC-100DL",T,"","limited F9 planetary version")],
    "aperture 50–125 mm · F7.4–F9 · fluorite"),
  X("Takahashi FSQ-106","Four-element Petzval astrograph; reference wide-field imaging refractor.",T,"","https://skyandtelescope.org/astronomy-equipment/the-new-q/",
    [("FSQ-106",T,"","original, from old data"),("FSQ-106ED",T,"2007","successor with ED glass")],"106 mm · F5 · reducers and extenders",a="the Q"),
  X("Tele Vue Genesis / NP101","Al Nagler's fast flat-field four-inch Petzval refractor, from fluorite Genesis to the ED NP101.",TV,"mid-1980s","https://scopeviews.co.uk/TVGenesis.htm",
    [("Genesis",TV,"","100 mm f/5, achromat front with fluorite Petzval lens"),("Genesis SDF",TV,"","f/5.4, special-dispersion front doublet"),("Renaissance",TV,"","brass-cell sibling"),("NP101",TV,"","101 mm f/5.4, ED doublet + Petzval"),("NP101is",TV,"","imaging-system version, larger focuser and Petzval lens")],
    "100–101 mm · f/5–5.4 · white tube"),
  X("Astro-Physics StarFire","Hand-built American triplet apochromats, long the benchmark for premium refractors.","Astro-Physics","","https://en.wikipedia.org/wiki/Astro-Physics",
    [("StarFire","Astro-Physics","","triplet apos 102–178 mm"),("StarFire EDT","Astro-Physics","","ED triplets 130–180 mm"),("StarFire EDF","Astro-Physics","","flat-field 130–206 mm"),("StarFire GTX","Astro-Physics","","110 and 130 mm"),("Traveler","Astro-Physics","","105 mm f/6"),("Stowaway","Astro-Physics","","90–92 mm")],
    "aperture 90–206 mm · triplet ED"),
  X("William Optics RedCat 51","Small 250 mm Petzval apochromat that popularised compact wide-field imaging.","William Optics","2019","https://astrobackyard.com/william-optics-redcat-51/",
    [("RedCat 51","William Optics","2019","helical focuser"),("RedCat 51 Gen 3 WIFD","William Optics","","internal rack-and-pinion focuser")],"51 mm · f/4.9 · FPL-53 · red tube"),
  X("Sky-Watcher Evostar / Equinox ED","Affordable Chinese ED doublet apochromat that brought FPL-53 colour correction to the mass market.",SW,"2004","https://www.scopeviews.co.uk/SW120ED.htm",
    [("Equinox 120ED",SW,"","120 mm f/7.5, FPL53 doublet"),("EvoStar ED APO",SW,"","current doublet range")],"80–150 mm · ED doublet"),
  X("Sky-Watcher Esprit","Sky-Watcher's triplet apochromat for imaging, with matched flattener.",SW,"","https://skywatcher.com/post/review/esprit-120ed-review-in-skynews/",
    [("Esprit 120ED",SW,"2012","reviewed in SkyNews 2012"),("Esprit 150ED",SW,"",""),("Esprit PRO",SW,"","from old data")],"triplet apo · flattener"),
  X("Unitron achromat","Japanese-made achromatic refractors sold in the US from the 1950s, the classic first serious scope.","Unitron","1950s","https://unitronhistory.com/?p=77",
    [("Model 114","Unitron","1950s–1960s","60 mm, 900 mm focal length, alt-az, about $125")],"60–152 mm · long-focus achromat · white tube"),
  X("Galileoscope","Low-cost 50 mm achromatic refractor kit made for the International Year of Astronomy.","","2009","https://astronomy2009.org/globalprojects/cornerstones/galileoscope/index.html",[],"50 mm · 25–50×")],
 "m":[["TOA-130",T],["130PHQ","Askar"],["SQA106","Askar"],["Askar V","Askar"],["Petzval 75","Radian"],["Z4","Sharpstar"],["FLT","William Optics"],["Fluorostar 132","William Optics"],["ZenithStar","William Optics"],["StarTravel",SW],["Inspire 100AZ","Celestron"],["StarSense Explorer DX 102AZ","Celestron"]],
 "r":[["ETX","Meade Instruments"],["Megrez","William Optics"],["StarSense Explorer","Celestron"]]}
newt={"n":"Newtonian & Dobsonian telescope","a":"Newtonian reflector · Dobsonian · Dob","d":"Telescope that gathers light with a primary mirror and a flat secondary mirror at the side of the tube; the Dobsonian is its commonest form.",
 "t":["solid-tube Dobsonian","collapsible Dobsonian","truss-tube Dobsonian","tabletop Dobsonian","equatorial Newtonian","imaging Newtonian astrograph","Schmidt–Newtonian","Maksutov–Newtonian"],
 "s":"https://www.astroshop.eu/telescopes/10/a,Teleskope.Optik.Bauart=Cassegrain/a,Teleskope.Optik.Bauart=Maksutov-Newton/a,Teleskope.Optik.Bauart=Newton/a,Teleskope.Optik.Bauart=Schmidt-Cassegrain/a,Teleskope.Optik.Bauart=Schmidt-Newton",
 "x":[
  X("Dobsonian","Newtonian on a simple rocker-box alt-az base, devised to put large apertures in amateur hands.","","1965","https://en.wikipedia.org/wiki/Dobsonian_telescope",
    [("John Dobson's design","","1965","original rocker-box design"),("Odyssey","Coulter Optical","1980s","cheap large-aperture Dobs with Sonotube tubes"),("Odyssey Compact 10.1","Coulter Optical","1980s","10.1-inch f/4.5"),("Obsession truss Dobsonian","Obsession Telescopes","1989","first commercial truss Dob, 12.5–25 in"),("Obsession Ultra Compact","Obsession Telescopes","2007","more portable truss line"),("SkyQuest XT8 Plus","Orion Telescopes & Binoculars","","8-inch f/5.9 solid tube"),("SkyQuest XT6 Plus / XT10i IntelliScope","Orion Telescopes & Binoculars","","from old data"),("Flextube",SW,"2008","collapsible tube"),("Heritage 130P",SW,"","130 mm f/5 tabletop collapsible"),("Stargate",SW,"2017","truss-tube line"),("Library Telescope","Apertura","","tabletop, from old data")],
    "aperture 4.5–36 in · f/3–6 · solid, collapsible or truss tube · push-to or GoTo"),
  X("Newton's reflector","The original reflecting telescope: concave primary and flat diagonal sending the image out of the side of the tube.","","1668","https://en.wikipedia.org/wiki/Newtonian_telescope",[],"tube or truss · on equatorial or alt-az mount")],
 "m":[["Explorer P",SW],["Skyliner Classic",SW],["Heritage FlexTube Virtuoso GTi",SW],["SpaceProbe 130ST EQ","Orion Telescopes & Binoculars"],["AD6","Apertura"],["AstroMaster 114 EQ","Celestron"],["StarSense Explorer DX 130AZ","Celestron"],["ProDob","Omegon"],["Pro Truss","Omegon"],["VX Newtonian","Orion Optics UK"],["Z10 Deluxe","Zhumell"]],
 "r":[["SkyQuest","Orion Telescopes & Binoculars"],["StarSense Explorer","Celestron"]]}
cass={"n":"Cassegrain telescope","a":"","d":"Telescope whose concave primary and convex secondary mirror fold the light back through a hole in the primary, with no full-aperture corrector plate.",
 "t":["classical Cassegrain","Ritchey–Chrétien","Dall–Kirkham","Klevtsov"],
 "s":"https://www.astroshop.eu/telescopes/omegon-cassegrain-telescope-pro-cc-154-1848-eq370dx-goto/p,93041",
 "x":[
  X("Ritchey–Chrétien","Cassegrain with two hyperbolic mirrors, free of coma; the standard of observatories and of amateur imaging RCs.","","1910s","https://en.wikipedia.org/wiki/Ritchey%E2%80%93Chr%C3%A9tien_telescope",
    [("AT8RC","Astro-Tech","2010","8-inch f/8 carbon-fibre tube, S&T Hot Product 2010"),("AT6RC / AT10RC","Astro-Tech","","6- and 10-inch sizes")],"6–16 in · f/8 · steel or carbon tube",a="RC"),
  X("Takahashi Mewlon","Takahashi's Dall–Kirkham Cassegrains, prized for refractor-like planetary views.",T,"","https://www.scopeviews.co.uk/TakMewlon180C.htm",
    [("Mewlon 180",T,"","1.25-inch back"),("Mewlon 180C",T,"","2-inch back, HR multi-coatings"),("Mewlon 210",T,"",""),("Mewlon 250 / 300",T,"","with corrector for imaging")],"180–300 mm · F12 · white tube"),
  X("Classical Cassegrain","Parabolic primary and hyperbolic secondary, the 1672 design.","","1672","https://en.wikipedia.org/wiki/Cassegrain_reflector",[],"")],
 "m":[["Pro CC 154/1848","Omegon"],["VMC200L","Vixen"]]}
brands=[
 {"n":T,"c":"Japan","f":"1932","seg":"Premium","kf":"apochromats","d":"Tokyo maker of fluorite and ED refractors, reflectors and equatorial mounts.","sig":["Takahashi FC fluorite doublet","Takahashi FSQ-106","Takahashi Mewlon"],"s":"https://en.wikipedia.org/wiki/Takahashi_Seisakusho"},
 {"n":TV,"c":"United States","f":"1977","seg":"Premium","kf":"eyepieces, Petzval refractors","d":"Al Nagler's Chester, New York maker of eyepieces and fast apochromatic refractors.","eras":["Al Nagler, 1977–"],"sig":["Tele Vue Genesis / NP101"],"s":"https://en.wikipedia.org/wiki/Tele_Vue_Optics"},
 {"n":"Astro-Physics","c":"United States","f":"1975","seg":"Artisan & independent","kf":"apo refractors","d":"Roland Christen's Illinois maker of triplet apochromats and mounts.","sig":["Astro-Physics StarFire"],"s":"https://en.wikipedia.org/wiki/Astro-Physics"},
 {"n":SW,"c":"China","f":"1999","seg":"Mainstream","kf":"telescopes, mounts","d":"Synta's telescope brand, making refractors, Dobsonians, Maksutovs and mounts in Suzhou.","sig":["Sky-Watcher Evostar / Equinox ED","Sky-Watcher Esprit"],"s":"https://en.wikipedia.org/wiki/Sky-Watcher"},
 {"n":"William Optics","c":"Taiwan","seg":"Specialist","kf":"small apo refractors","d":"Taiwanese maker of compact apochromatic refractors for imaging.","sig":["William Optics RedCat 51"],"s":"knowledge"},
 {"n":"Unitron","c":"United States","seg":"Heritage manufactory","kf":"classic refractors","d":"Importer that sold Japanese-made achromatic refractors to American amateurs from the 1950s.","sig":["Unitron achromat"],"s":"https://unitronhistory.com/?p=77"},
 {"n":"Obsession Telescopes","c":"United States","f":"1989","seg":"Artisan & independent","kf":"truss Dobsonians","d":"David Kriege's Wisconsin maker of large truss-tube Dobsonians.","s":"https://en.wikipedia.org/wiki/Obsession_Telescopes"},
 {"n":"Coulter Optical","c":"United States","seg":"Specialist","kf":"Dobsonians","d":"Maker of the cheap large Odyssey Dobsonians of the 1980s.","s":"https://en.wikipedia.org/wiki/Dobsonian_telescope"},
 {"n":"Astro-Tech","c":"United States","seg":"Own-label & retailer","kf":"RC astrographs","d":"House brand of the retailer Astronomics, known for its Ritchey–Chrétien astrographs.","s":"https://astronomics.com/products/astro-tech-8-f-8-ritchey-chretien-astrograph-carbon-fiber-tube"}]
w('00_00',{"kinds":[refr,newt,cass],"brands":brands,"traditions":[],
 "notes":"Refractor: 24 flat models → 9 archetypes (Takahashi FC, FSQ-106, Tele Vue Genesis/NP101, Astro-Physics StarFire, RedCat 51, Sky-Watcher Evostar/Equinox ED, Esprit, Unitron, Galileoscope) + 12 m; FC-76, FS-60, FSQ-106, EvoStar ED APO, Esprit PRO, RedCat 51, StarFire, Galileoscope absorbed as versions; dropped starter SKUs StarSense Explorer LT 80AZ, Explore Scientific FirstLight, Orion Observer 90, StarBlast 102. Not done: Takahashi FOA, Vixen achromats, Tele Vue NP101 years (no page found). Newtonian: Dobsonian archetype with Coulter, Obsession, Orion XT, Flextube, Heritage tabletop, Stargate versions; dropped starter SKUs Omegon Advanced X and Horizon, Zhumell Z130, Zoomion Cassini, StarSense Explorer LT, SkyQuest Classic. Cassegrain: RC (Astro-Tech) and Mewlon archetypes; GSO not confirmed as maker so not named."})
