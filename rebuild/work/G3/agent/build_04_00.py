import json, os
W='https://en.wikipedia.org/wiki/'
LS='https://support.lutron.com/us/en/product/radiora3/article/system-design-setup/Which-Lutron-Residential-System-is-Best-for-Me'
SIV='https://www.lutron.com/us/en/window-treatments/sivoia-shades'
PAL='https://www.lutron.com/us/en/window-treatments/palladiom'
KP='https://www.lutron.com/us/en/controls/keypads-remotes'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Home automation system","a":"Smart home system · domotics · whole-home control",
 "d":"Central controller and software that runs a home's lighting, climate, shading, media and security from keypads, touch panels and apps.",
 "t":["wired bus","wireless","hybrid","professionally installed","DIY hub","Zigbee","Z-Wave","Matter / Thread"],
 "s":W+"Home_automation",
 "x":[
  X("KNX","Open, royalty-free building-automation standard for lighting, blinds, HVAC and security, run by the KNX Association.","", "1999 (KNX Association)",W+"KNX",
    [("European Installation Bus (EIB / Instabus)","","","predecessor standard"),("BatiBUS","","","predecessor standard"),("European Home Systems (EHS)","","","predecessor standard")],
    "medium: twisted pair (TP1), powerline, KNX-RF 868 MHz, KNXnet/IP · ISO/IEC 14543-3, EN 50090"),
  X("X10","Early home-automation protocol sending control signals over household wiring.","","1975",W+"Home_automation",dt="powerline · plug-in and wall modules"),
  X("Crestron Home","Crestron's residential control platform and operating system (Crestron Home OS) for whole-home automation.","Crestron","",W+"Crestron_Electronics",
    dt="touch panels, keypads, remotes · voice: Alexa, Siri, Google Home"),
  X("Control4 Smart Home OS","Control4's controller-based whole-home platform for dealer-installed systems.","Control4","2005 (first products)",W+"Control4",
    [("Media Controller","Control4","2005","first product line"),("Smart Home OS 3","Control4","2019","current OS generation"),("CA-1 controller","Control4","",""),("EA-series controllers","Control4","","")],
    "controllers · touch screens · Neeo remote (acquired 2019)"),
  X("Savant","Luxury home-automation platform with host controller, touchscreen remote and app.","Savant","2005",'https://smarthomeworks.com.au/2020/05/06/everything-you-need-to-know-about-savant-home-automation/',
    [("Savant Remote","Savant","2016","more affordable remote and hub version")],"host · touchscreen remote · lamp control · app"),
  X("Loxone Miniserver","Central PLC-style controller running lighting, shading, climate, access and energy in a Loxone home.","Loxone","",'https://www.loxone.com/enus/products/miniserver/',
    [("Miniserver","Loxone","",""),("Miniserver Compact","Loxone","",""),("Miniserver Go","Loxone","","wireless-oriented")],"runs locally without cloud · extensions"),
 ]},
{"n":"Lighting control system","a":"Whole-home dimming · scene control",
 "d":"Network of dimmers, keypads and a processor that sets lighting scenes across rooms, often with shades.",
 "t":["wired","RF wireless","DIY","pro-installed","keypad finishes"],
 "s":LS,
 "x":[
  X("HomeWorks","Lutron's top residential system: wired and wireless, up to 10,000 zones, pro-installed and programmed.","Lutron","",LS,
    [("HomeWorks QSX","Lutron","","current generation")],"keypads: Palladiom, Alisse, Signature Series, Architrave, Sunnata, seeTouch · 50+ finishes"),
  X("RadioRA 3","Lutron's professional wireless whole-home lighting system, up to 400 devices.","Lutron","",LS,
    dt="keypads and dimmers: Sunnata RF, Maestro RF, seeTouch · 20+ colours"),
  X("Caséta","Lutron's DIY smart dimmer and switch system with hub and Pico remotes, up to 75 devices.","Lutron","",LS,
    [("Caséta Original","Lutron","","push-button"),("Smart Diva","Lutron","","paddle"),("Smart Claro","Lutron","","paddle")],"Pico remote · fan control · 6 colours"),
  X("Palladiom keypad","Lutron's architectural keypad in metal, glass or polymer for HomeWorks.","Lutron","",PAL,
    dt="stainless steel, glass, polymer · Signature Metals finishes (Matte Graphite, Champagne)"),
 ]},
{"n":"Motorised blinds and shading","a":"Motorised shades · automated blinds",
 "d":"Blinds, shades or curtains moved by a motor, run from switches, remotes or a home-control system.",
 "t":["roller shade","roman shade","drapery","wood blind","tensioned shade","wired","battery / wire-free"],
 "s":SIV,
 "x":[
  X("Sivoia QS","Lutron's customisable motorised shade, blind and drapery line for homes and commercial use.","Lutron","",SIV,
    dt="widths 20 in–20 ft · roller, roman, drapery, wood blinds, tensioned · QS wired or Clear Connect wireless; sister lines Serena, Triathlon"),
  X("Palladiom shades","Lutron's premium roller shades and drapery with milled aluminium or brass brackets.","Lutron","",PAL,
    [("Palladiom Wired Roller Shade","Lutron","","new construction"),("Palladiom Wire-Free Roller Shade","Lutron","",""),("Palladiom Drapery","Lutron","","")],
    "brackets and hembars: aluminium, brass · finishes incl. Aged Bronze"),
  X("Somfy drives","French motors and controls for blinds, awnings, shutters, gates and garage doors.","Somfy","",W+"Somfy",dt="blinds, awnings, gates, garage doors"),
 ]},
{"n":"Thermostat","a":"Room thermostat · smart thermostat",
 "d":"Device that switches heating or cooling on and off to hold a set temperature; smart or plain, and smart radiator heads are included.",
 "t":["mechanical","programmable","smart / learning","smart radiator thermostat","wired","wireless"],
 "s":"https://shop.tado.com/en",
 "x":[
  X("Honeywell T87","Round dial wall thermostat designed by Henry Dreyfuss from a concept by Carl Kronmiller.","Honeywell","1953",W+"Honeywell_T87"),
  X("Nest Learning Thermostat","Learning smart thermostat with rotating ring, designed by Tony Fadell, Ben Filson and Fred Bould.","Google Nest","2011",W+"Nest_Learning_Thermostat",
    [("1st generation","Nest Labs","2011",""),("2nd generation","Nest Labs","2012",""),("3rd generation","Nest Labs","2015",""),("Nest Thermostat E","Google Nest","2017","lower-cost version"),("Nest Thermostat","Google Nest","2020","touch strip instead of ring; model G4CVZ"),("4th generation","Google Nest","2024","")],
    "ring finishes · wired"),
  X("ecobee Smart Thermostat","Canadian Wi-Fi smart thermostat family, the first released in 2008.","ecobee","2008",W+"Ecobee",
    [("Smart","ecobee","2008","first model"),("Smart Si","ecobee","",""),("ecobee3","ecobee","","1st and 2nd generation"),("ecobee3 lite","ecobee","",""),("ecobee4","ecobee","",""),("Smart Thermostat with Voice Control","ecobee","",""),("Smart Thermostat Enhanced","ecobee","",""),("Smart Thermostat Premium","ecobee","",""),("Smart Thermostat Essential","ecobee","2025","")],
    "room sensors · voice assistant"),
  X("tado Smart Thermostat X","tado's DIY smart heating control, with matching smart radiator thermostats.","tado","",'https://www.tado.com/',
    [("Wired Smart Thermostat X","tado","",""),("Wireless Smart Thermostat X","tado","",""),("Smart Radiator Thermostat X","tado","","radiator head")],
    "boilers, underfloor heating, heat pumps, air conditioning"),
 ],
 "m":[["Thermostatkopf H","Herz"]]},
{"n":"Energy monitor","a":"Energy meter · home energy monitor",
 "d":"Device that measures and shows a home's electricity use or generation.",
 "t":["clamp-on sensor","meter-reading sensor","smart-meter in-home display","plug-in monitor","solar / battery (DC) monitor"],
 "s":W+"Home_energy_monitor",
 "m":[["e2","Efergy"],["PowerCost Monitor",""],["FLEXnet DC","OutBack Power"],["TriMetric 2030",""]]},
{"n":"Intruder alarm system","a":"burglar alarm system · security alarm",
 "d":"Control panel, sensors, keypad and siren that detect break-ins; also listed under Home Safety & Security.",
 "t":["wired","wireless","local (bells only)","remote monitored","self-monitored app"],
 "s":W+"Security_alarm",
 "x":[
  X("SimpliSafe","Self-installed wireless alarm system with base station and keypad, launched as a DIY system.","SimpliSafe","2009",W+"SimpliSafe",
    [("Third generation","SimpliSafe","2018","cellular and Wi-Fi, lithium batteries")],"base station · keypad · sensors · cameras"),
  X("Ring Alarm","Ring's DIY wireless alarm system linked to its app and doorbells.","Ring","2018",W+"Ring_(company)",
    [("Ring Alarm Pro","Ring","2021","")]),
 ],
 "m":[["Wireless Alarm Kit 2","Swann"]]},
{"n":"Door phone and video intercom","a":"Door phone · video door entry · video doorbell",
 "d":"An entry panel with speaker (and screen) linked to an indoor unit or phone for speaking to a caller.",
 "t":["audio door phone","two-wire video","IP video intercom","smart video doorbell","multi-apartment panel"],
 "s":W+"Video_door-phone",
 "x":[
  X("Ring Video Doorbell","Wi-Fi video doorbell that alerts a phone and lets the owner see and talk to callers; one of the first smart doorbells.","Ring","2013",W+"Smart_doorbell",
    [("Ring Video Doorbell","Ring","2013","original"),("Ring Doorbell 2","Ring","2017","1080p camera"),("Ring Doorbell Pro","Ring","","")],a="Doorbot"),
  X("2N IP Force","2N's rugged IP video intercom door station.","2N","",'https://www.2n.com/en-GB/',
    [("2N IP Force 2.0","2N","","5 MP camera, noise cancellation, QR access")]),
 ],
 "m":[["Nest Hello","Google Nest"],["DS-KIS702 Two-Wire Video Intercom Kit","Hikvision"]]},
]
def B(n,c,f,seg,d,s,lines=(),sig=(),rel=(),eras=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Crestron","United States","1972","Luxury home automation","Control and automation maker founded by George Feldstein in New Jersey.",W+"Crestron_Electronics",["Crestron Home"],["Crestron Home"],["Control4","Savant"]),
 B("Control4","United States","2003","Home automation","Utah home-automation company, now part of Resideo after the 2024 Snap One acquisition.",W+"Control4",["Smart Home OS"],["Control4 Smart Home OS"],["Crestron","Savant"],["Snap One, 2019–2024","Resideo, 2024–"]),
 B("Savant","United States","2005","Luxury home automation","Home-automation firm founded by Robert Madonna, first at the luxury end.",'https://smarthomeworks.com.au/2020/05/06/everything-you-need-to-know-about-savant-home-automation/',["Savant Remote"],["Savant"],["Crestron","Control4"]),
 B("Loxone","","","Home and building automation","Maker of the Miniserver controller and its extensions for homes and buildings.",'https://www.loxone.com/enus/products/miniserver/',["Miniserver","Miniserver Compact","Miniserver Go"],["Loxone Miniserver"]),
 B("Lutron","United States","1961","Lighting and shading control","Coopersburg, Pennsylvania firm founded by Joel Spira, maker of the first successful solid-state dimmer.",W+"Lutron_Electronics_Company",["HomeWorks","RadioRA 3","Caséta","Sivoia","Palladiom","Serena","Triathlon"],["HomeWorks","RadioRA 3","Caséta","Palladiom keypad","Sivoia QS"],["Somfy"]),
 B("Somfy","France","1969","Motorised shading and access","French group making drives and controls for blinds, awnings, gates and garage doors.",W+"Somfy",sig=["Somfy drives"],rel=["Lutron"]),
 B("ecobee","Canada","2007","Smart thermostats","Toronto smart-thermostat maker, owned by Generac since 2021.",W+"Ecobee",["Smart Thermostat"],["ecobee Smart Thermostat"],["Google Nest","tado"]),
 B("tado","","2011","Smart heating","Smart heating-control company selling DIY thermostats and radiator heads in Europe.",'https://www.tado.com/',["Smart Thermostat X","Smart Radiator Thermostat X"],["tado Smart Thermostat X"],["ecobee","Google Nest"]),
 B("Ring","United States","2013","Smart doorbells and DIY security","Santa Monica company founded by Jamie Siminoff as Doorbot, owned by Amazon since 2018.",W+"Ring_(company)",["Video Doorbell","Ring Alarm"],["Ring Video Doorbell","Ring Alarm"],["SimpliSafe"]),
 B("SimpliSafe","United States","2006","DIY home security","Boston company that launched a self-installed home security system in 2009.",W+"SimpliSafe",sig=["SimpliSafe"],rel=["Ring"]),
 B("Yale","United States","1868","Locks and home security","Lock maker owned by Assa Abloy, selling smart locks, cameras and burglar alarms.",W+"Yale_(company)",rel=["Ring","SimpliSafe"]),
 B("2N","Czech Republic","","IP intercoms and access control","Prague maker of IP door intercoms, indoor stations and access control.",'https://www.2n.com/en-GB/',["IP Force"],["2N IP Force"]),
 B("Resideo","United States","2018","Home comfort and security","Honeywell spin-off that sells Honeywell Home thermostats under licence and owns Control4.",W+"Resideo",["Honeywell Home","First Alert"],rel=["Control4"]),
]
notes=("Kinds: 7 (3 new: Home automation system, Lighting control system, Motorised blinds and shading; 4 old kept). Old kinds' sources switched to retrieved reference pages except Thermostat. "
 "Intruder alarm system and Door phone/video intercom cross-link to Home Safety & Security (B8). 2N country from Wikidata label (Prague). "
 "Left out (no retrieved page confirming models): Philips Dynalite, Hive thermostat models (Hive home page names none), Honeywell T-series/Lyric Round, Yale alarm models, Somfy RTS/io/TaHoma lines, Loxone founding year/country (blog page 403), 2N founding year, other energy monitors (Sense, Emporia). "
 "Loxone/tado country left blank because the retrieved pages do not state it.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/G3/shelves/04_00.json'
open(p+'.tmp','w').write(json.dumps(out,ensure_ascii=False,indent=1)); os.replace(p+'.tmp',p)
print('ok')
