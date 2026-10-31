import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
DA="Davis Instruments"; EW="Ecowitt"; AW="Ambient Weather"; WF="WeatherFlow"; NK="Nielsen-Kellerman"; TF="TFA Dostmann"; BR="Bresser"; GQ="GQ Electronics"
WSE="https://theweatherstationexperts.com/davis-instruments-vantage-pro2-review/"
ws={"n":"Weather station","a":"home weather station · personal weather station","d":"Set of instruments that measures several weather quantities together and shows or uploads the readings.",
 "t":["all-in-one sensor array","separate sensors","cabled","wireless","Wi-Fi / app-only (no console)","fan-aspirated radiation shield","ultrasonic anemometer","indoor-outdoor thermo-hygrometer type"],
 "s":"https://www.astroshop.eu/miscellaneous/weather-stations/44",
 "x":[
  X("Davis Vantage Pro2","Davis's reference home weather station, on the market for about two decades and long rated the most accurate consumer station.",DA,"",WSE,
    [("Vantage Pro",DA,"","first generation, mid-2000s"),("Vantage Pro2",DA,"","from old data"),("Vantage Pro2 Plus",DA,"","from old data"),("fan-aspirated shield option",DA,"","daytime or 24-hour fan"),("sonic anemometer option",DA,"",""),("WeatherLink Live",DA,"","internet base unit")],
    "cabled or wireless · standard or fan-aspirated shield · cup or sonic anemometer"),
  X("Davis Vantage Vue","Smaller, cheaper Davis all-in-one station with compact shielding and lesser sensors than the Pro2.",DA,"",WSE,[("Vantage Vue",DA,"","from old data")],"integrated sensor suite"),
  X("Fine Offset all-in-one station","Low-cost Chinese design licensed to many brands, sold by Fine Offset's own Ecowitt brand and rebadged by Ambient Weather, Sainlogic and Froggit.","Fine Offset","","https://theweatherstationexperts.com/ecowitt-weather-station/",
    [("HP2551",EW,"","from old data"),("HP2553H",EW,"","from old data"),("WS2910",EW,"","from old data"),("Wittboy Pro",EW,"","from old data"),("GW1202 gateway",EW,"","from old data")],"display console or Wi-Fi gateway · add-on sensors"),
  X("WeatherFlow Tempest","Solar-powered, console-free all-in-one station (2020) with a haptic rain sensor and lightning detection, read through an app.",WF,"2020","https://theweatherstationexperts.com/weatherflow-tempest-weather-system-review/",
    [("Tempest",WF,"2020","sensor plus Wi-Fi hub")],"no console · solar")],
 "m":[["WS-2902",AW],["WS-5000",AW],["WS-2000",AW],["HP1000SE Ultra","Froggit"],["WiFi Professional","Sainlogic"],["Weather Station","Netatmo"],["5-en-1 WiFi",BR],["MeteoChamp",BR],["View 35.1142.01",TF],["Spring Breeze 35.1140.01",TF],["Wezzer PRO","Levenhuk"],["HomeCast","Celestron"],["Kestrel 5500",NK]]}
th={"n":"Air thermometer","a":"indoor-outdoor thermometer · max-min thermometer","d":"Instrument that reads the air temperature indoors or outdoors.",
 "t":["liquid-in-glass","dial","digital","wireless indoor-outdoor","maximum-minimum (Six's)"],
 "s":"https://www.astroshop.eu/miscellaneous/weather-stations/44",
 "m":[["DOUBLE-CHECK",TF],["PALMA",TF]]}
hy={"n":"Hygrometer","a":"thermo-hygrometer","d":"Instrument that reads the humidity of the air, usually with temperature too.",
 "t":["hair (dial)","digital","data-logging","for terrarium or cigars"],
 "s":"https://www.astroshop.eu/miscellaneous/weather-stations/44",
 "m":[["Klima-Guard",TF],["KlimaLogg Pro",TF],["TERRACHECK",TF],["ClimaTemp",BR],["Hygrometer POLAR","Fischer"]]}
an={"n":"Anemometer","a":"wind meter","d":"Instrument that measures wind speed.",
 "t":["handheld vane (impeller)","cup","hot-wire","thermo-anemometer","pocket weather meter"],
 "s":"https://datatec.eu/de/en/extech-45168cp",
 "x":[X("Kestrel pocket wind meter","Waterproof handheld impeller wind meter designed in 1995 by Nielsen-Kellerman's co-founder for gliding; the reference pocket anemometer.",NK,"1995","https://www.alphacontrols.com/products/1000-pocket-wind-meter",
    [("Kestrel 1000",NK,"1995","wind speed only"),("Kestrel 3000",NK,"","from old data")],"impeller · IP67 · floats")],
 "m":[["testo 405i","Testo"],["testo 410-1","Testo"],["testo 410i","Testo"],["AN100","Extech"],["AN200","Extech"],["45158","Extech"],["BT-100","BTMETER"],["866B","HoldPeak"]]}
rg={"n":"Rain gauge","a":"pluviometer","d":"Instrument that collects and measures rainfall.",
 "t":["manual (read by eye)","tipping-bucket","wireless","haptic"],
 "s":"https://www.astroshop.eu/miscellaneous/weather-stations/44",
 "x":[X("CoCoRaHS 4-inch gauge","High-capacity 4-inch manual gauge required for CoCoRaHS volunteer reports; catches within a few per cent of the US NWS 8-inch standard gauge.","CoCoRaHS","","https://media.cocorahs.org/docs/WhyManualGauge.pdf",
    [],"4-inch diameter · manual · read daily")],
 "m":[["Waterfall","La Crosse Technology"],["Netatmo Rain Gauge","Netatmo"],["Drop",TF]]}
wv={"n":"Wind vane","a":"weathervane · weathercock","d":"Pivoting vane that turns to show the wind direction, from a sensor vane to a decorative roof weathervane.",
 "t":["decorative roof weathervane","weathercock","sensor vane for a weather station"],
 "s":"https://tools.woot.com/offers/rooster-weathervane-pure-copper-w-garden-pole"}
sock={"n":"Windsock","a":"wind cone","d":"Tapered fabric sleeve that shows wind direction and strength.",
 "t":["garden","airfield-pattern"],
 "s":"https://www.aviationpros.com/directory/airport-facilities-buildings/product/55403700/the-custom-windsock-company-airport-windsock-faa-compliant-orange"}
sol={"n":"Solar radiation sensor","a":"pyranometer · UV sensor","d":"Sensor that measures sunlight (solar radiation), often added to a home weather station.",
 "t":["silicon-cell pyranometer","UV sensor"],
 "s":"https://campbellsci.com.au/sp-110",
 "m":[["SP-110","Apogee Instruments"]]}
gc={"n":"Geiger counter","a":"radiation detector · dosimeter","d":"Handheld detector that counts ionising radiation and shows a dose rate, used by hobbyists, collectors and preppers.",
 "t":["Geiger–Müller tube","scintillator","dosimeter","data-logging","GPS mapping","alpha-sensitive"],
 "s":"https://trueprepper.com/?p=3494",
 "x":[
  X("GQ GMC","Budget Geiger counter family from GQ Electronics, the common hobby entry point.",GQ,"","https://trueprepper.com/?p=3494",
    [("GMC-300S",GQ,"","budget pick"),("GMC-320+",GQ,"","data logging"),("GMC-500+",GQ,"","dual Geiger tubes"),("GMC-800",GQ,"","")],"G-M tube · USB logging"),
  X("Safecast bGeigie Nano","Open-source, GPS-logging radiation kit for mapping from a car or bike, the workhorse of the Safecast citizen network.","Safecast","","https://safecast.org/devices",
    [("bGeigie Nano","Safecast","","reading every 5 s with GPS"),("bGeigie Zen","Safecast","","")],"kit · GPS · open source")],
 "m":[["Radiacode 103","Radiacode"],["Radiacode Zero","Radiacode"],["S-2","Better Geiger"],["Geiger-2","Mira Safety"],["NukAlert","NukAlert"]]}
seis={"n":"Home seismometer","a":"home seismograph","d":"Small seismograph run at home that records earthquakes and local ground motion and can share data with a citizen network.",
 "t":["vertical geophone","three-component","with infrasound"],
 "s":"https://raspberryshake.org/home-bf/",
 "x":[X("Raspberry Shake","Raspberry Pi-based home seismograph whose owners form a live citizen seismic network.","Raspberry Shake","","https://raspberryshake.org/home-bf/",[],"Raspberry Pi · data sharing")]}
brands=[
 {"n":DA,"c":"United States","seg":"Premium","kf":"weather stations","d":"Californian maker of the Vantage Pro2 and Vantage Vue home weather stations.","sig":["Davis Vantage Pro2","Davis Vantage Vue"],"s":"knowledge"},
 {"n":"Fine Offset","c":"China","f":"2005","seg":"Value","kf":"weather stations (OEM)","d":"Shenzhen Fine Offset Electronics, maker of weather stations licensed to many brands; sells under its own Ecowitt brand.","sig":["Fine Offset all-in-one station"],"rel":[EW,AW,"Froggit","Sainlogic"],"s":"https://theweatherstationexperts.com/ecowitt-weather-station/"},
 {"n":EW,"c":"China","seg":"Value","kf":"weather stations","d":"Fine Offset's own commercial brand of weather stations and sensors.","rel":["Fine Offset"],"s":"https://theweatherstationexperts.com/ecowitt-weather-station/"},
 {"n":AW,"c":"United States","seg":"Mainstream","kf":"weather stations","d":"US seller of home weather stations including Fine Offset designs.","rel":["Fine Offset"],"s":"https://theweatherstationexperts.com/ecowitt-weather-station/"},
 {"n":WF,"c":"United States","seg":"Specialist","kf":"weather stations","d":"Maker of the solar-powered Tempest weather system.","sig":["WeatherFlow Tempest"],"s":"https://theweatherstationexperts.com/weatherflow-tempest-weather-system-review/"},
 {"n":"Netatmo","c":"France","seg":"Mainstream","kf":"smart home","d":"French smart-home maker of app-based weather stations and add-on rain and wind gauges.","s":"knowledge"},
 {"n":NK,"c":"United States","seg":"Specialist","kf":"pocket weather meters","d":"Pennsylvania maker of Kestrel handheld wind and weather meters.","sig":["Kestrel pocket wind meter"],"s":"https://www.alphacontrols.com/products/1000-pocket-wind-meter"},
 {"n":TF,"c":"Germany","seg":"Mainstream","kf":"thermometers, hygrometers","d":"German maker of thermometers, hygrometers and weather stations.","s":"knowledge"},
 {"n":"CoCoRaHS","c":"United States","seg":"Institution & issuer","kf":"rain-gauge network","d":"Community Collaborative Rain, Hail and Snow Network, a volunteer precipitation network that sets a standard manual gauge.","sig":["CoCoRaHS 4-inch gauge"],"s":"https://media.cocorahs.org/docs/WhyManualGauge.pdf"},
 {"n":GQ,"seg":"Value","kf":"Geiger counters","d":"Maker of low-priced GMC Geiger counters.","sig":["GQ GMC"],"s":"https://trueprepper.com/?p=3494"},
 {"n":"Safecast","seg":"Institution & issuer","kf":"citizen radiation mapping","d":"Volunteer citizen-science project that designs open-source radiation and environmental sensors.","sig":["Safecast bGeigie Nano"],"s":"https://safecast.org/devices"},
 {"n":"Raspberry Shake","seg":"Specialist","kf":"home seismographs","d":"Maker of Raspberry Pi-based home seismographs and their citizen network.","sig":["Raspberry Shake"],"s":"https://raspberryshake.org/home-bf/"}]
w('04_00',{"kinds":[ws,th,hy,an,rg,wv,sock,sol,gc,seis],"brands":brands,"traditions":[],
 "notes":"Weather station: 41 flat models -> 4 archetypes (Davis Vantage Pro2 and Vue, Fine Offset all-in-one with Ecowitt versions, WeatherFlow Tempest) + 13 m; dropped Ambient WS-1553-IP and WS-5000-IP3 (duplicates), Bresser 4CAST/Beaufort/El Nino/Profi, Ecowitt GW1210/HP2561/WS3900, Fischer 801, JDC Skywatch, Kalawen, Levenhuk Wezzer PLUS, Metos uMetos (farm), Onset HOBO (professional), Safonovo M-49M (institutional), Kestrel 3550AG/5000/5200 (handheld meters kept to one). Ambient/Froggit/Sainlogic models left in m because no fetched page ties specific models to Fine Offset; La Crosse station models not added (none in data or pages). Air thermometer: Galileo thermometer removed from aliases and models (it is its own kind on the Barometers & weather glasses shelf). Anemometer: 21 -> Kestrel archetype + 8 m (dropped Brannan, Sky View, Velleman, older Testo/Extech duplicates). Hygrometer 7->5 (dropped Bresser Quadro NV and VentAir). Solar radiation sensor: renamed from Pyranometer; Kipp & Zonen CMP research pyranometers dropped as professional, Apogee kept. New kinds Geiger counter (GQ GMC and Safecast bGeigie archetypes; Radex and SOEKS not added, no fetched page) and Home seismometer (Raspberry Shake; model variants not on fetched page). No traditions."})
