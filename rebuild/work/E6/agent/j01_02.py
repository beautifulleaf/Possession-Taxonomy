import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
Z="ZWO"; AB="https://astrobackyard.com/optolong-l-extreme-filter-review/"
cam={"n":"Astronomy camera","a":"astronomy imaging camera · CMOS camera · CCD camera","d":"Camera with no lens or screen made to fit a telescope, run from a computer or controller.",
 "t":["cooled deep-sky (TEC)","uncooled planetary","guide camera","colour (one-shot colour)","monochrome","CCD (historic)"],
 "s":"https://www.astroshop.eu/astrophotography/cameras/15_35_10/m,ZWO",
 "x":[
  X("SBIG ST series","Santa Barbara Instrument Group's CCD cameras that brought cooled CCD imaging to amateurs; later models added a built-in guide chip.","SBIG","","https://company7.com/sbig/index.html",
    [("ST-4","SBIG","","autoguider that could also image"),("ST-6","SBIG","",""),("ST-7","SBIG","","integral autoguide chip"),("ST-8","SBIG","","integral autoguide chip")],"CCD · cooled · built-in guide chip (ST-7/ST-8)"),
  X("ZWO ASI Pro cooled camera","Mass-market cooled CMOS deep-sky camera with a regulated two-stage thermoelectric cooler, sold in colour (MC) and mono (MM).",Z,"",
    "https://starizona.com/products/zwo-asi2600mc-pro-usb3-cooled-color-camera-2025",
    [("ASI2600MC Pro",Z,"","APS-C Sony IMX571, 26 MP; 2025 revision"),("ASI2600",Z,"","from old data"),("ASI6200",Z,"","from old data"),("ASI294",Z,"","from old data"),("ASI533",Z,"","from old data")],"sensor size · colour or mono · cooling ΔT 30–35 °C"),
  X("ZWO ASI planetary camera","Small uncooled high-frame-rate camera for lucky imaging of the Moon and planets; doubles as a guide camera.",Z,"","https://astrobackyard.com/zwo-asi462mc-review",
    [("ASI290MC",Z,"","predecessor of the 462MC"),("ASI462MC",Z,"","Sony IMX462, 2.9 µm pixels"),("ASI585",Z,"","successor"),("ASI662MC",Z,"",""),("ASI678MC",Z,"",""),("ASI715MC",Z,"","")],"1/3 to 1/1.2-inch sensors · USB 3.0")],
 "m":[["Ceres-462M","Player One Astronomy"],["Uranus-C","Player One Astronomy"],["Xena-585M","Player One Astronomy"],["QHY5III585C","QHY"],["QHY5III568","QHY"],["QHY5III178M","QHY"],["ASI174MM",Z],["ASI432MM",Z],["ASI676MM",Z],["G3M2210M","ToupTek"],["SV905C","Svbony"],["SC311 WiFi camera","Svbony"]]}
fil={"n":"Astronomical filter","a":"","d":"Filter for a telescope eyepiece barrel, filter wheel or camera that passes chosen wavelengths (colour, moon, light-pollution, nebula, narrowband); solar filters are listed separately.",
 "t":["broadband light-pollution","dual-band (Ha + OIII)","tri/quad-band","narrowband (Ha, OIII, SII, H-beta)","LRGB imaging","visual colour and moon","1.25-inch, 2-inch, 31/36/50 mm unmounted"],
 "s":"https://www.adorama.com/l/optics-and-binoculars/telescopes-and-astronomy/telescope-filters",
 "x":[X("Optolong L-eXtreme","Dual-band filter passing only 7 nm bands of H-alpha and OIII, for nebula imaging with colour cameras under light pollution.","Optolong","",AB,
    [("L-eNhance","Optolong","","tri-band: 24 nm OIII/H-beta, 10 nm Ha"),("L-eXtreme","Optolong","","7 nm Ha and OIII; new in 2020")],"7 nm · 1.25 and 2-inch")],
 "m":[["L-Pro","Optolong"],["Nebula Booster","IDAS"],["IDAS NB1","IDAS"],["IDAS NB3","IDAS"],["Triad Ultra","Radian"],["Duo-Narrowband","STC"],["Edge narrowband filters","Antlia"],["CCD MaxFR","Astronomik"],["f/2 Highspeed filters","Baader Planetarium"],["Baader Contrast Booster filter","Baader Planetarium"],["Haida NanoPro Magnetic Clear Night filter","Haida"]]}
efw={"n":"Filter wheel","a":"electronic filter wheel · EFW","d":"Motorised wheel between telescope and camera that swaps filters under computer control.",
 "t":["5, 7 or 8 positions","1.25-inch/31 mm","36 mm","2-inch/50 mm"],"s":"https://www.zwoastro.com/product/efw/",
 "x":[X("ZWO EFW","Low-cost USB filter wheel widely paired with ZWO cameras; now with a USB-C port.",Z,"","https://www.zwoastro.com/product/efw/",
    [("EFW Mini (5×1.25″)",Z,"","300 g"),("EFW 8×1.25″",Z,"",""),("EFW 7×36 mm",Z,"",""),("EFW 7×2″",Z,"",""),("EFW 7×50 mm square",Z,"","")],"positions · filter size")]}
ad={"n":"Telescope camera adapter","a":"T-ring · T-adapter","d":"T-ring or adapter that fits a camera to a telescope.",
 "t":["T-ring (camera bayonet to T2)","T-adapter / nosepiece","off-axis guider","field flattener / reducer"],
 "s":"https://www.adorama.com/lists/astrophotography-camera-adapters","m":[["Baader Clickstop MicroStage II","Baader Planetarium"]]}
fm={"n":"Focus motor","a":"electronic focuser · autofocuser","d":"Motor unit fitted to the knob shaft of an existing telescope focuser and driven from a computer or hand box to focus.",
 "s":"https://www.astroshop.eu/telescope-accessories/focusers/15_57/m,Explore-Scientific",
 "m":[["Electronic Automatic Focuser EAF",Z],["FocusCube v3","Pegasus Astro"],["SESTO SENSO 3","PrimaLuceLab"]]}
ctl={"n":"Astrophotography controller","a":"imaging computer · astro computer","d":"Small computer on the telescope that runs camera, mount, guiding and filter wheel from a phone or tablet app.",
 "s":"https://www.zwoastro.com/2018/12/13/zwo-asiair-review",
 "x":[X("ZWO ASIAIR","Raspberry Pi in a ZWO case that runs ZWO cameras and filter wheels, guiding and the mount from an app.",Z,"2018","https://www.zwoastro.com/2018/12/13/zwo-asiair-review",[],"")],
 "m":[["StellarMate",""],["EAGLE","PrimaLuceLab"]]}
cs={"n":"Cloud sensor","a":"cloud watcher","d":"Instrument that detects cloud cover by measuring the infrared temperature of the sky.","s":"https://www.lunaticoastro.com/the-company",
 "m":[["Boltwood Cloud Sensor III","Diffraction Limited"],["Boltwood Portable Cloud Sensor","Diffraction Limited"],["AAG CloudWatcher","Lunático Astronomía"],["Cloud Watcher Solo","Lunático Astronomía"]]}
sqm={"n":"Sky-quality meter","a":"SQM","d":"Instrument that measures the brightness of the night sky in magnitudes per square arcsecond.","s":"https://www.lunaticoastro.com/the-company",
 "x":[X("Unihedron SQM","Pocket meter that reads zenith sky brightness; the standard for measuring light pollution.","Unihedron","","https://en.wikipedia.org/wiki/Sky_quality_meter",
    [("SQM","Unihedron","","84° field"),("SQM-L","Unihedron","","lens, 20° field"),("SQM-LU","Unihedron","","USB"),("SQM-LE","Unihedron","","Ethernet"),("SQM-LR","Unihedron","",""),("SQM-LU-DL","Unihedron","","USB data logger")],"mag/arcsec² · field width · connection")]}
brands=[
 {"n":Z,"c":"China","seg":"Specialist","kf":"astronomy cameras","d":"Chinese maker of astronomy cameras, filter wheels, ASIAIR controllers and mounts.","sig":["ZWO ASI Pro cooled camera","ZWO ASI planetary camera","ZWO EFW","ZWO ASIAIR"],"s":"knowledge"},
 {"n":"SBIG","c":"United States","seg":"Specialist","kf":"CCD cameras","d":"Santa Barbara Instrument Group, California pioneer of cooled CCD cameras for amateurs and universities.","eras":["Richard Schwartz, president and co-founder"],"sig":["SBIG ST series"],"s":"https://company7.com/sbig/index.html"},
 {"n":"Optolong","c":"China","seg":"Specialist","kf":"astronomy filters","d":"Chinese maker of light-pollution, dual-band and narrowband filters.","sig":["Optolong L-eXtreme"],"s":"knowledge"},
 {"n":"Unihedron","c":"Canada","seg":"Specialist","kf":"sky-quality meters","d":"Grimsby, Ontario maker of the Sky Quality Meter.","sig":["Unihedron SQM"],"s":"https://en.wikipedia.org/wiki/Sky_quality_meter"}]
w('01_02',{"kinds":[cam,fil,efw,ad,fm,ctl,cs,sqm],"brands":brands,"traditions":[],
 "notes":"Astronomy camera: 23 flat models -> 3 archetypes (SBIG ST CCD, ZWO ASI Pro cooled, ZWO planetary) + 12 m; dropped old range 'ASI cameras' and ZWO ASI664MC/676MC (near-duplicates of listed planetary cameras); guide camera is a type. Filter: L-eNhance became a version of the Optolong L-eXtreme archetype; added L-Pro, IDAS Nebula Booster, Radian Triad Ultra, STC Duo-Narrowband (named on the fetched review). Astrodon/Chroma not added (no fetched page); Antlia page blocked (403). New kinds Filter wheel (ZWO EFW; Starlight Xpress not added, no page) and Astrophotography controller (ASIAIR; StellarMate and EAGLE named on the same page). Camera adapter: generic maker-less 'T-ring'/'T-adapter' models became types, with off-axis guider and field flattener. Focus motor, cloud sensor kept as is (QoL, few models). SQM models became versions of the Unihedron SQM archetype. No traditions."})
