import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
SW="Sky-Watcher"; C="Celestron"; IO="iOptron"; Z="ZWO"; LO="Losmandy"; SB="Software Bisque"; AP="Astro-Physics"
AS="https://www.astroshop.eu/mounts-accessories/15_55"; BP="https://agenaastro.com/berlebach-planet-tripod-with-tray-for-telescope-mounts-14020.html"
mount={"n":"Telescope mount","a":"GoTo mount · equatorial mount · alt-az mount","d":"Head that carries a telescope and turns it to follow the sky, by hand or motor; differs by axis arrangement.",
 "t":["German equatorial","centre-balanced equatorial","strain-wave (harmonic) equatorial","alt-azimuth","fork","alt-az/equatorial dual-mode"],
 "s":"https://en.wikipedia.org/wiki/Equatorial_mount",
 "x":[
  X("German equatorial mount","T-shaped mount with the telescope on one end of the declination axis and a counterweight on the other.","","1824","https://en.wikipedia.org/wiki/Equatorial_mount",
    [("Great Dorpat Refractor mount","","1824","Joseph von Fraunhofer's original")],"payload · GoTo or manual · polar scope or camera",a="GEM"),
  X("Losmandy G11","American machined GEM first built for the Celestron C11; spread the D-style dovetail standard.",LO,"1990s","https://telescopicwatch.com/losmandy-g-11-mount-review/",
    [("G11",LO,"1990s","for the C11 tube"),("G11 Gemini 2",LO,"","GoTo version"),("G11 PMC-Eight","Explore Scientific","","app GoTo version"),("G11T",LO,"","Titan-parts hybrid, more payload"),("GM8",LO,"","smaller sibling")],"payload about 27 kg visual · D-style saddle"),
  X("Sky-Watcher EQ6-R Pro","Mass-market GoTo German equatorial mount widely used for mid-weight imaging.",SW,"","https://astrobackyard.com/sky-watcher-eq6r-review/",
    [("EQ6-R Pro",SW,"","20 kg payload, SynScan"),("HEQ5 Pro",SW,"","smaller sibling"),("EQ5",SW,"","lighter manual/GoTo GEM, from old data")],"SynScan handset · 20 kg class"),
  X("Celestron CGX","Celestron's heavy GoTo GEM, successor to the CGEM II and CGE.",C,"","https://telescopicwatch.com/celestron-cgx-equatorial-mount-review/",
    [("CGEM II",C,"","predecessor"),("CGX",C,"","25 kg payload"),("CGX-L",C,"","larger gears and shaft")],"payload 25 kg and up"),
  X("iOptron CEM","Centre-balanced equatorial mount that sits the payload over the mount's centre for stability.",IO,"","https://www.astronomy.com/observing/navigate-the-stars-with-the-ioptron-cem70-mount/",
    [("ZEQ25",IO,"","first centre-balanced design"),("CEM40",IO,"",""),("CEM60",IO,"",""),("CEM70",IO,"","31.8 kg payload, iPolar camera"),("CEM120",IO,"","")],"payload up to 31.8 kg (CEM70)"),
  X("Software Bisque Paramount","Observatory-grade American mounts for serious imaging, sold as heads to put on a pier or tripod.",SB,"","https://www.skyatnightmagazine.com/reviews/mounts/software-bisque-paramount-myt-mount/",
    [("Paramount MyT",SB,"","23 kg portable model"),("Paramount MX",SB,"",""),("Paramount MX+",SB,"","")],"payload 23 kg and up"),
  X("ZWO AM5","Light strain-wave (harmonic drive) mount needing no counterweight for most loads; among the best-known harmonic mounts.",Z,"","https://www.skyatnightmagazine.com/reviews/zwo-am5n-harmonic-drive-mount-tc40-tripod",
    [("AM5",Z,"","12 kg without counterweight"),("AM5N Harmonic Equatorial",Z,"2024","15 kg, improved tracking"),("AM3",Z,"","smaller"),("AM3N",Z,"","from old data"),("AM7",Z,"","larger, from old data")],"payload 12–20 kg · EQ or alt-az mode"),
  X("Sky-Watcher AZ-GTi","Small Wi-Fi GoTo alt-az mount controlled from a phone app.",SW,"","https://telescopicwatch.com/sky-watcher-az-gti-mount-review/",
    [("AZ-GTi",SW,"","SynScan app")],"payload about 5 kg · alt-az, EQ with wedge")],
 "m":[["Mach2",AP],["1100 GTO",AP],["GM 1000 HPS","10Micron"],["GM 2000 HPS","10Micron"],["Porta II","Vixen"],["AZ5",SW],["Gibraltar HD4","Tele Vue Optics"],["WarpDrive WD-20","WarpAstron"],["WarpDrive WD-20EP","WarpAstron"],["EQ-AL55i Pro",SW],["CG-4 (Omni)",C],["EM31 Pro","EmCan"],["AZ-Bellavista","Omegon"],["EQ570DX","Omegon"]]}
trk={"n":"Star tracker","a":"camera tracking mount · sky tracker","d":"Small motorised equatorial head that turns a camera with the sky for long night exposures.",
 "t":["camera tracker","tracker with GoTo"],"s":"https://astrobackyard.com/sky-watcher-star-adventurer-pro-review/",
 "x":[
  X("Sky-Watcher Star Adventurer","Battery tracker with built-in polar scope and wedge, the common first imaging mount.",SW,"","https://astrobackyard.com/sky-watcher-star-adventurer-pro-review/",
    [("Star Adventurer",SW,"","original black-and-red"),("Star Adventurer Pro",SW,"","5 kg payload"),("Star Adventurer 2i",SW,"",""),("Star Adventurer Mini",SW,"","nightscape model"),("Star Adventurer GTi",SW,"","GoTo version")],"payload 3–5 kg · AA batteries"),
  X("iOptron SkyGuider Pro","Compact metal-bodied tracker with illuminated polar scope.",IO,"","https://www.digitalcameraworld.com/photography/astrophotography/ioptron-skyguider-pro-review",
    [("SkyGuider Pro",IO,"",""),("SkyTracker Pro",IO,"","from old data")],""),
  X("Move Shoot Move","Pocket tracker aligned with a laser pointer, for wide-angle Milky Way shots.","Move Shoot Move","","https://www.space.com/moveshootmove-star-tracker-review",[],"wide-angle lenses")]}
tri={"n":"Telescope tripod","a":"","d":"Tripod made to carry a telescope mount head, sold apart from the mount; a universal photo tripod is in Cameras & Photography.",
 "t":["wooden","steel","carbon fibre","pier"],"s":AS,
 "m":[["Planet","Berlebach"],["Graviton","Berlebach"],["Sky","Berlebach"],["Uni 18","Berlebach"],["Uni 28","Berlebach"],["TC40 tripod",Z]]}
wed={"n":"Equatorial wedge","a":"polar wedge","d":"Tilting plate that sets a fork or alt-az telescope mount at the latitude angle to track equatorially.","s":AS,
 "m":[["900WDGA Hi-Lo Latitude Wedge",AP],["HD Pro CPC polar wedge",C],["Wedge for NexStar Evolution and SE 6/8",C],["Equatorial Wedge for Star Adventurer",SW],["Deluxe Polar Wedge","Omegon"],["MH-100","Bresser"]]}
pol={"n":"Polar scope","a":"pole finder · polar finder","d":"Small sighting scope or camera fitted to an equatorial mount's polar axis to align it on the celestial pole.",
 "t":["optical polar scope","electronic polar camera"],"s":AS,
 "m":[["PoleMaster","QHY"],["iPolar",IO],["Polar Axis Finderscope 94224",C],["Polar Scope for HEQ5/EQ3",SW],["Polar HM5",SW],["AccuAlign",IO]]}
hw={"n":"Mount hardware","a":"counterweight · tube rings · dovetail bar","d":"Counterweights, tube rings, dovetail bars and pier extensions that join a telescope to its mount and balance it.",
 "t":["counterweight","tube rings","dovetail bar (Vixen style)","dovetail bar (Losmandy D style)","pier extension"],"s":AS,
 "m":[["Counterweight 2.6kg","Omegon"],["2.5kg Counterweight CEM60/iEQ45",IO],["PLUS Tube Rings","PrimaLuceLab"],["Tube ring clamps for DuoScope One-T","Lunatico"]]}
brands=[
 {"n":LO,"c":"United States","seg":"Specialist","kf":"equatorial mounts","d":"American maker of machined German equatorial mounts and the D-style dovetail.","sig":["Losmandy G11"],"s":"https://telescopicwatch.com/losmandy-g-11-mount-review/"},
 {"n":SW,"c":"China","f":"1999","seg":"Mainstream","kf":"telescopes, mounts","d":"Synta's telescope brand, made in Suzhou.","sig":["Sky-Watcher EQ6-R Pro","Sky-Watcher AZ-GTi","Sky-Watcher Star Adventurer"],"s":"https://en.wikipedia.org/wiki/Sky-Watcher"},
 {"n":C,"c":"United States","f":"1964","seg":"Mainstream","kf":"Schmidt-Cassegrains","d":"Torrance, California telescope maker, owned by Synta since 2005.","sig":["Celestron CGX"],"s":"https://en.wikipedia.org/wiki/Celestron"},
 {"n":IO,"c":"United States","seg":"Specialist","kf":"GoTo mounts","d":"American maker of centre-balanced and strain-wave GoTo mounts and star trackers.","sig":["iOptron CEM","iOptron SkyGuider Pro"],"s":"knowledge"},
 {"n":SB,"c":"United States","seg":"Professional & flagship","kf":"observatory mounts","d":"American maker of Paramount mounts and TheSkyX software.","sig":["Software Bisque Paramount"],"s":"knowledge"},
 {"n":Z,"c":"China","seg":"Specialist","kf":"astronomy cameras","d":"Chinese maker of astronomy cameras, strain-wave mounts and smart telescopes.","sig":["ZWO AM5"],"s":"knowledge"},
 {"n":"Move Shoot Move","seg":"Specialist","kf":"star trackers","d":"Maker of pocket-sized star trackers for photographers.","sig":["Move Shoot Move"],"s":"https://www.space.com/moveshootmove-star-tracker-review"},
 {"n":"Berlebach","c":"Germany","seg":"Heritage manufactory","kf":"wooden tripods","d":"German maker of ash-wood tripods for cameras and telescope mounts.","s":"knowledge"}]
w('01_00',{"kinds":[mount,trk,tri,wed,pol,hw],"brands":brands,"traditions":[],
 "notes":"Telescope mount: 23 flat models → 8 archetypes (GEM pattern, Losmandy G11, EQ6-R Pro, CGX, iOptron CEM, Paramount, ZWO AM5, AZ-GTi) + 14 m; Astro-Physics Mach2/1100 and 10Micron added as m (named on a fetched tripod-compatibility page). Star Adventurer, SkyGuider Pro and SkyTracker Pro moved to the new Star tracker kind. Dropped EmCan AZ40 and Sky-Watcher Solarquest AZ (minor). Rainbow Astro, iOptron HEM and Vixen Porta archetypes not built (no page fetched; Porta II kept in m). Equatorial wedge cut 11→6 (dropped Fornax FMW-200, Robtics photo wedge, Omegon dovetail wedge, Fusion 120i wedge, WO SkyGuider wedge). Milburn tripods not added (no page). Counterweight and Tube rings merged into Mount hardware."})
