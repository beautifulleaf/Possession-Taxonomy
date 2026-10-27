import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
WO="https://en.wikipedia.org/wiki/Orrery"; WA="https://en.wikipedia.org/wiki/Astrolabe"; WS="https://en.wikipedia.org/wiki/Sextant"
TP="Trippensee Planetarium Company"; ST="Sega Toys (Sega Fave Corporation)"; CP="Cassens & Plath"; DA="Davis Instruments"; GP="George Philip & Son"
SAN="https://www.skyatnightmagazine.com/advice/skills/how-to-use-a-planisphere/"
orr={"n":"Orrery","a":"planetarium (mechanical) · tellurion · tellurian","d":"Mechanical model of the Sun, planets and moons, turned by hand, clockwork or motor.",
 "t":["grand orrery (all known planets)","tellurion (Sun, Earth, Moon)","hand-cranked","clockwork or electric","brass","kit or desk model"],
 "s":"https://collection.sciencemuseumgroup.org.uk/search/objects/object_type/orreries",
 "x":[
  X("Graham–Rowley orrery","The first orreries: George Graham's planetary machine, copied and improved by John Rowley for the Earl of Orrery, who gave the device its name.","John Rowley","c. 1712",WO,
    [("Graham & Tompion orrery","George Graham and Thomas Tompion","c. 1710","History of Science Museum, Oxford"),("Earl of Orrery's orrery","John Rowley","c. 1712","made for Charles Boyle, 4th Earl of Orrery")],"geared · brass and wood"),
  X("Benjamin Martin orrery","Popular 18th-century English orrery after Benjamin Martin's 1764 planetary model; a 1766 example was used at Harvard.","Benjamin Martin","1764",WO,
    [("Harvard orrery","Benjamin Martin","1766","")],"brass · hand-cranked"),
  X("Trippensee planetarium","American classroom tellurion showing Sun, Earth, Moon and Venus with seasons, phases and eclipses, made in Michigan since the early 20th century.",TP,"1908","https://oshermaps.org/blog/understanding-the-trippensee-planetarium/",
    [("Laing planetarium","Alexander Laing","1896","string-and-pulley drive"),("chain-and-gear model, maple",TP,"1908","Frank J. Trippensee patent"),("black-painted model",TP,"1925",""),("electric model",TP,"by 1929","also hand-cranked"),("Bakelite / plastic model",TP,"after WWII",""),("Science First plastic model","Science First","from 1999","hand-cranked or electric"),("Trippensee orrery",TP,"","from old data")],
    "maple, ebonised, Bakelite or plastic arm · hand-cranked or electric")],
 "m":[["Orbit Orrery","Cochranes of Oxford"],["Grand Orrery",""]]}
ast={"n":"Astrolabe","a":"","d":"Hand-held instrument that models the sky, used to find star and Sun positions, the time and latitude.",
 "t":["planispheric","mariner's","universal","spherical","reproduction"],
 "s":"https://www.1stdibs.com/buy/brass-astrolabe",
 "x":[
  X("Planispheric astrolabe","Classic astrolabe: a mater holding latitude plates (tympans) under a rotating star map (rete), with a sighting alidade on the back; Greek in origin, refined in the Islamic world.","","c. 550 (earliest treatise)",WA,
    [("earliest surviving astrolabe","","927–928","Islamic"),("Jean Fusoris astrolabe","Jean Fusoris","c. 1400","Paris"),("Antonius de Pacento astrolabe","Antonius de Pacento","1420",""),("Gujarati astrolabe","","1644","calibrated for Jodhpur"),("Planispheric astrolabe","","","from old data")],
    "mater · tympans for latitudes · rete · alidade · brass"),
  X("Universal astrolabe","Astrolabe usable at any latitude without changing plates, perfected by Ibn al-Sarraj of Aleppo.","Ibn al-Sarraj","fl. 1328",WA,[],"single universal plate"),
  X("Mariner's astrolabe","Heavy, open-wheel astrolabe for measuring the Sun's or a star's altitude on a moving ship.","","15th century",WA,[],"open cast ring · weighted")]}
arm={"n":"Armillary sphere","a":"armilla · spherical astrolabe","d":"Model of the sky made of rings for the celestial equator, ecliptic and other circles around a central Earth or Sun.",
 "t":["Ptolemaic (Earth-centred)","Copernican (Sun-centred)","desk model","garden"],
 "s":"https://en.wikipedia.org/wiki/Armillary_sphere"}
glob={"n":"Celestial globe","a":"star globe","d":"Globe showing the stars and constellations on the celestial sphere, usually mounted with meridian and horizon rings.",
 "t":["antique printed gores","table or floor stand","illuminated","pair with terrestrial globe"],
 "s":"https://collections.whipplemuseum.cam.ac.uk/objects/9274",
 "x":[
  X("Blaeu celestial globe","Willem Jansz Blaeu's engraved celestial globes from Amsterdam, first based on Tycho Brahe's star catalogue; among the finest of 17th-century Europe.","Willem Jansz Blaeu","1598","https://www.metmuseum.org/art/collection/search/207816",
    [("first celestial globe","Willem Jansz Blaeu","1598",""),("corrected edition","Willem Jansz Blaeu","1603",""),("13 3/8 in globe","Willem Jansz Blaeu","after 1621","Met Museum")],"engraved gores · brass meridian · wooden stand"),
  X("Cary celestial globe","Georgian library globe from J. & W. Cary of the Strand, the leading British globe makers of the 19th century.","J. & W. Cary","1816","https://collections.whipplemuseum.cam.ac.uk/objects/9274",
    [("18-inch celestial globe","J. & W. Cary","1816","stars to 9th magnitude after Wollaston")],"12–21 in · tripod stand · hand-coloured gores"),
  X("Replogle celestial globe","Modern celestial globes from Replogle, the Chicago globe maker founded in 1930.","Replogle Globes","",
    "https://en.wikipedia.org/wiki/Replogle_Globes",[],"desk size · often illuminated")]}
plan={"n":"Planisphere","a":"star wheel · star finder","d":"Pair of rotating discs that show which stars are above the horizon at any date and time for one latitude.",
 "t":["single-sided","two-sided (north and south views)","latitude bands","card or plastic"],
 "s":SAN,
 "x":[
  X("Philip's Planisphere","The best-known British planisphere, set for latitude 51.5° N.",GP,"",SAN,
    [("Philip's planisphere for 51.5° N",GP,"","stars to magnitude 5")],"latitude editions"),
  X("David Chandler Night Sky","Two-sided planisphere with separate north- and south-facing maps that removes most distortion; first printed in 1976.","David Chandler","1976","https://www.denverastro.org/meet-fellow-das-member-david-chandler/",
    [("The Night Sky","David Chandler","1976","first 1,000 copies")],"two sizes · latitude zones"),
  X("Collins Planisphere","Planisphere by Storm Dunlop and Wil Tirion, approved by the Royal Observatory Greenwich.","Collins","",SAN,[],"northern latitudes")]}
proj={"n":"Home planetarium projector","a":"star projector · home planetarium","d":"Small projector that shows the night sky on the ceiling and walls of a room.",
 "t":["optical (star disc)","LED nebula / galaxy projector","with rotation and shooting stars"],
 "s":"https://www.astroshop.eu/planetaria-sundials/planetaria/42_20",
 "x":[X("Sega Toys Homestar","The first home optical planetarium, developed by Takayuki Ohira with Sega Toys in 2005; about 1.7 million sold by 2021.",ST,"2005","https://www.megastar.jp/en/products/homestar/",
    [("Homestar Pro Original",ST,"","from old data"),("Homestar Classic",ST,"","from old data"),("Homestar Flux",ST,"","from old data"),("Homestar Matataki",ST,"","from old data; twinkling stars")],"replaceable star discs · rotation · timer")],
 "m":[["Planetarium NV 110/220","Baader Planetarium"],["Astro Planetarium","National Geographic (licensed optics)"],["Planetarium HD","Buki"],["Pococo Galaxy Projector","Pococo"]]}
sex={"n":"Sextant","a":"octant · quadrant","d":"Double-reflecting hand instrument that measures the angle between a celestial body and the horizon for navigation.",
 "t":["octant (Hadley's quadrant)","sextant","micrometer drum","vernier","metal","plastic"],
 "s":WS,
 "x":[
  X("Hadley octant","John Hadley's double-reflecting instrument of about 1731 (also found by Thomas Godfrey), the ancestor of the sextant.","","c. 1731",WS,[],"wooden or brass frame · 45° arc"),
  X("Cassens & Plath sextant","German micrometer-drum sextant with a bronze frame, made by Cassens & Plath of Bremen from 1962, often sold through Weems & Plath.",CP,"1962","https://landandseacollection.com/id486.html",
    [("Weems & Plath branded sextant",CP,"","−5° to 125°, 4×40 scope, reads to 10″")],"bronze frame · black enamel · micrometer drum"),
  X("Davis Mark 15","Plastic micrometer-drum sextant sold as a low-cost learner and backup instrument.",DA,"","https://casualnavigation.com/davis-mk15-sextant-review/",
    [("Mark 15",DA,"","3× telescope, seven shades")],"plastic frame · 7 in radius")]}
brands=[
 {"n":TP,"c":"United States","f":"1920","seg":"Specialist","kf":"classroom orreries","d":"Michigan maker of the Trippensee planetarium tellurion, separated from Trippensee Manufacturing in 1920; bought by Science First in 1999.","sig":["Trippensee planetarium"],"s":"https://oshermaps.org/blog/understanding-the-trippensee-planetarium/"},
 {"n":"J. & W. Cary","c":"United Kingdom","seg":"Heritage manufactory","kf":"globes, maps","d":"London globe and map makers John and William Cary, the leading British globe producers of the 19th century.","sig":["Cary celestial globe"],"s":"https://collections.whipplemuseum.cam.ac.uk/objects/9274"},
 {"n":"Willem Jansz Blaeu","c":"Netherlands","f":"1598","seg":"Heritage manufactory","kf":"globes, atlases","d":"Amsterdam cartographer and globe maker, pupil of Tycho Brahe.","sig":["Blaeu celestial globe"],"s":"https://www.metmuseum.org/art/collection/search/207816"},
 {"n":"Replogle Globes","c":"United States","f":"1930","seg":"Mainstream","kf":"globes","d":"Chicago globe maker founded by Luther Replogle, making Earth, Moon, planet and celestial globes.","sig":["Replogle celestial globe"],"s":"https://en.wikipedia.org/wiki/Replogle_Globes"},
 {"n":GP,"c":"United Kingdom","seg":"Specialist","kf":"atlases, planispheres","d":"British map and atlas publisher whose Philip's planisphere is the best-known in Britain.","sig":["Philip's Planisphere"],"s":"knowledge"},
 {"n":ST,"c":"Japan","seg":"Mainstream","kf":"toys","d":"Japanese toy maker that developed the Homestar home planetarium with Takayuki Ohira.","sig":["Sega Toys Homestar"],"s":"https://www.megastar.jp/en/products/homestar/"},
 {"n":CP,"c":"Germany","f":"1902","seg":"Heritage manufactory","kf":"sextants, compasses","d":"Bremen nautical instrument firm founded by Captain Tanne Janssen Cassens, renamed with Theodore Plath in 1908; making its own sextants from 1962.","sig":["Cassens & Plath sextant"],"s":"https://landandseacollection.com/id486.html"},
 {"n":DA,"c":"United States","seg":"Premium","kf":"weather stations","d":"Californian maker of weather stations and marine instruments, including the plastic Mark 15 sextant.","sig":["Davis Mark 15"],"s":"knowledge"}]
trad=[
 {"n":"Islamic astrolabe making","g":"Scientific instruments","r":"Middle East, Persia, North Africa, Islamic Spain, India","p":"8th–17th century",
  "d":"Tradition of engraved brass astrolabes and astronomical treatises begun by al-Fazari and carried from Baghdad to Spain and India.",
  "tech":"cast and engraved brass, stereographic projection of plates, pierced rete","mat":"brass",
  "forms":["Planispheric astrolabe","Universal astrolabe"],"ctr":["Baghdad","Isfahan","Aleppo (Ibn al-Sarraj)","Gujarat"],
  "auth":"dated or signed inscriptions, latitudes of plates matching named cities, star names in Arabic","s":WA},
 {"n":"European astrolabe making","g":"Scientific instruments","r":"Western Europe","p":"c. 1000–17th century",
  "d":"Latin astrolabe tradition after Gerbert of Aurillac brought the instrument north of the Pyrenees, with treatises by Chaucer and Stöffler.",
  "tech":"engraved brass plates and rete, Latin scales","mat":"brass",
  "forms":["Planispheric astrolabe","Mariner's astrolabe"],"ctr":["Paris (Jean Fusoris)"],
  "auth":"Latin inscriptions and star names, maker's signature, plate latitudes","s":WA}]
w('05_00',{"kinds":[orr,ast,arm,glob,plan,proj,sex],"brands":brands,"traditions":trad,
 "notes":"Orrery: 3 archetypes (Graham–Rowley, Benjamin Martin, Trippensee) with the old Trippensee model as a version; Cochranes Orbit and generic Grand Orrery kept in m; modern geared kit orreries not added (no page). Astrolabe: planispheric, universal and mariner's archetypes; Islamic and European traditions from the Wikipedia article. New kinds Armillary sphere (types only, no owned-model page), Celestial globe (Blaeu, Cary, Replogle), Planisphere (Philip's, Chandler Night Sky, Collins; Miller not found), Sextant (Hadley octant, Cassens & Plath, Davis Mark 15; Heath and Tamaya not added, no page). Home planetarium projector: renamed from Planetarium projector; Carl Zeiss Mark V and Universarium IX dropped as professional dome projectors (Megastar likewise excluded); Orzorz dropped; Homestar models became versions of the Sega Toys Homestar archetype."})
