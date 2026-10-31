import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E5/agent')
from write import w
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":q[0],"mk":q[1],"y":q[2],"d":q[3]} for q in v],"dt":dt}
def B(n,c,f,seg,kf,d,s,sig=(),rel=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d}
    if sig: b["sig"]=list(sig)
    if rel: b["rel"]=list(rel)
    b["s"]=s; return b
L='Logitech'; T='Thrustmaster'; F='Fanatec'; MZ='Moza Racing'; HE='Heusinkveld Engineering'
TM=W+'Thrustmaster'; SN='https://speednation.co.nz/blogs/simulator-guides-articles/the-ultimate-guide-to-moza-racing-products'; HK='https://heusinkveld.com/about-us/'
wheel={"n":"Racing wheel","a":"wheel-and-pedal set","d":"Steering-wheel controller for driving games, usually sold with pedals as a set.","t":["gear-driven","belt-driven","direct-drive","toy or motion wheel"],
 "s":"https://secure.logitech.com/en-ph/shop/p/driving-force-racing-wheel","x":[
 X("Logitech Driving Force and G-series wheels","G29 · G920 · G923","Logitech's gear-driven wheel-and-pedal sets, the mainstream console and PC choice.",L,"",W+"Logitech_G29",
   [("Logitech G25",L,"","shifter with buttons"),("Logitech G27",L,"","replaced by the G29 in 2015"),("Logitech Driving Force GT",L,"",""),
    ("Logitech G29 Driving Force",L,"2015","dual-motor force feedback; PlayStation"),("Logitech G920 Driving Force",L,"2015","Xbox version of the G29"),("Logitech G923 TRUEFORCE",L,"2020","G29 successor")]),
 X("Thrustmaster T-series wheels","T300 · T150 · T248","Thrustmaster's console and PC wheel-and-pedal sets.",T,"2013",TM,
   [("Thrustmaster TX Racing Wheel",T,"2013","Xbox; launched as the 458 Italia Edition"),("Thrustmaster T300 RS",T,"2014","PlayStation; brake and accelerator pedals"),
    ("Thrustmaster T300 RS GT Edition",T,"","three-pedal set"),("Thrustmaster T150 RS",T,"2015","entry model"),("Thrustmaster T248",T,"2021","with T3PM pedals"),("Thrustmaster T818",T,"2023","direct-drive")])],
 "m":[["Thrustmaster T-GT",T],["Thrustmaster T128",T],["Thrustmaster T598",T],["Fanatec Porsche 911 Turbo S Racing Wheel",F],["Moza R3 Racing Wheel and Pedals",MZ],["Moza R5 Bundle",MZ],
      ["Thermaltake G6 Direct Drive Racing Wheel","Thermaltake"],["Xbox 360 Wireless Racing Wheel","Microsoft"],["neGcon","Namco"],["JogCon","Namco"],["Wii Wheel","Nintendo"],["Joy-Con Wheel","Nintendo"],
      ["Saturn Racing Controller","Sega"],["Dreamcast Race Controller","Sega"]]}
base={"n":"Racing wheelbase","a":"wheel base · DD base","d":"Force-feedback motor base sold without a rim; interchangeable rims mount on it by quick release.","t":["direct-drive","belt-driven","gear-driven"],"s":"https://simucube.com/about","x":[
 X("Fanatec direct-drive bases","CSL DD · Podium","Fanatec's direct-drive bases from the entry CSL DD to the Podium range.",F,"",'https://traxion.gg/fanatec-csl-dd-wheel-base-and-csl-pedals-review/',
   [("Fanatec CSL DD",F,"2021","5 Nm, 8 Nm with Boost Kit"),("Fanatec Podium DD1",F,"","20 Nm"),("Fanatec Podium DD2",F,"","25 Nm")],"torque · platform licence"),
 X("Moza R-series","","Moza's direct-drive bases graded by peak torque.",MZ,"",SN,
   [("Moza R3",MZ,"","3.9 Nm"),("Moza R5 Pro",MZ,"","6 Nm"),("Moza R9",MZ,"","9 Nm"),("Moza R12",MZ,"","12 Nm; V1 15-bit, V2 21-bit encoder"),("Moza R16",MZ,"","16 Nm"),("Moza R21",MZ,"","21 Nm")],"torque · version"),
 X("Simucube","","Finnish high-end direct-drive bases from Granite Devices, built with sim-racing community input.","Simucube","2017","https://simucube.com/about",
   [("Simucube 1","Simucube","2017","first model"),("Simucube 2 Pro","Simucube","2019–2020",""),("Simucube 3 Pro","Simucube","",""),("Simucube 3 Ultimate","Simucube","","")])],
 "m":[["Fanatec ClubSport DD",F],["Fanatec ClubSport DD+",F],["Fanatec Gran Turismo DD Pro",F],["Asetek Initium","Asetek SimSports"],["Simagic Alpha","Simagic"],["Simagic Alpha Mini","Simagic"],
      ["Simagic Alpha EVO","Simagic"],["Simagic Alpha EVO Pro","Simagic"],["Moza Racing R16 Ultra",MZ],["Moza Racing R25 Ultra",MZ],["Simucube 3 Sport","Simucube"],["Thrustmaster TS-XW Servo Base",T]]}
rim={"n":"Steering wheel rim","a":"wheel rim · button box","d":"Interchangeable steering wheel or button box that fits a wheelbase's quick release.","t":["formula","GT","round","button box"],"s":SN,
 "m":[["Moza KS",MZ],["Moza GS V2P",MZ],["Moza CS",MZ],["Moza FSR Formula",MZ],["Moza ES Lite",MZ],["Moza ESX",MZ]]}
ped={"n":"Pedal set","a":"sim pedals","d":"Set of foot pedals for driving games, sold as a controller.","t":["potentiometer","hall sensor","load cell","hydraulic","active pedal"],"s":"https://www.coolblue.nl/en/product/858301/thrustmaster-t-lcm-pedals-set.html","x":[
 X("Heusinkveld pedals","Sprint · Ultimate","Dutch load-cell pedal sets that grew from sim racers' home-built pedals.",HE,"2013",HK,
   [("Heusinkveld Sprint",HE,"2018","custom output curves via SmartControl"),("Heusinkveld Ultimate",HE,"2021","brake force up to 140 kg; later Ultimate+")])],
 "m":[["Fanatec ClubSport Pedals V3",F],["Fanatec CSL Pedals",F],["Logitech G PRO Racing Pedals",L],["Logitech RS Pedals",L],["Moza CRP2 Load Cell Pedals",MZ],["Moza SR-P Pedals",MZ],
      ["Moza mBooster Active Pedal",MZ],["Simagic P1000","Simagic"],["Thrustmaster T-LCM Pedals",T],["Thrustmaster T3PM",T],["Thrustmaster Raceline Pedals III LC",T],["PXN Vector X Pedals","PXN"]]}
shift={"n":"Gear shifter","a":"H-pattern shifter · sequential shifter","d":"Lever controller sold apart from a wheel that changes gear in driving games.","t":["H-pattern","sequential"],"s":HK,"x":[
 X("Heusinkveld shifters","MagShift","Heusinkveld's sequential and adjustable shifters.",HE,"2014",HK,
   [("Heusinkveld Sim Shifter Sequential",HE,"2014–2017","compact sequential"),("Heusinkveld MagShift Mini",HE,"2023","adjustable 2-way and 3-way"),("Heusinkveld MagShift",HE,"2023","")])],
 "m":[["Thrustmaster TH8A",T],["Logitech Driving Force Shifter",L],["Fanatec ClubSport Shifter SQ V1.5",F],["Moza SGP",MZ],["Aiologs Sim Sequential Shifter","Aiologs"]]}
hb={"n":"Handbrake controller","a":"sim handbrake","d":"Lever controller sold apart from a wheel that works the handbrake in driving games.","t":["load cell","hall sensor"],"s":HK,
 "m":[["Heusinkveld HE Sim Handbrake",HE],["MOZA HBP Handbrake",MZ],["Thrustmaster TSS Handbrake",T],["Thrustmaster TSS Handbrake Sparco Mod",T]]}
cock={"n":"Sim cockpit or wheel stand","a":"sim rig","d":"Frame, stand or seat rig made to hold a racing wheel, pedals, shifter or flight controls for play. A gaming chair without controller mounts is in Furniture & Storage.",
 "t":["wheel stand","seat cockpit","aluminium-profile rig","motion platform"],"s":"https://computerlounge.co.nz/products/playseat-challenge-x-sim-racing-cockpit-logitech-g-edition","x":[
 X("Playseat","","Seat with wheel and pedal mounts in a race-car seating position; the brand's founder built the first in 1996.","Playseat","1996","https://www.d-box.com/en/blog/partner-spotlight-playseat",
   [("Playseat Challenge X","Playseat","","foldable"),("Playseat Pro Formula","Playseat","","formula position")]),
 X("Next Level Racing GTtrack and F-GT","","Steel cockpits with adjustable seat, pedal and wheel positions, convertible to flight.","Next Level Racing","","https://boxthislap.org/next-level-racing-gttrack/",
   [("Next Level Racing GT Track Cockpit","Next Level Racing","","carbon steel, motion-platform ready"),("Next Level Racing F-GT","Next Level Racing","","formula and GT positions"),("Next Level Racing F-GT Lite","Next Level Racing","",""),("Next Level Racing F-GT Elite","Next Level Racing","","")])],
 "m":[["Next Level Racing Wheel Stand Lite","Next Level Racing"],["GT Omega APEX","GT Omega"]]}
br=[B(L,"Switzerland","1981","Mainstream","PC peripherals","Swiss-American peripheral maker; its G-series wheels lead the mainstream market.","knowledge",["Logitech Driving Force and G-series wheels"]),
 B(T,"United States","1990","Mainstream","wheels & flight sticks","Hillsboro, Oregon maker of wheels and flight controls, owned by Guillemot.",TM,["Thrustmaster T-series wheels"],["Guillemot"]),
 B(F,"Germany","1997","Premium","sim racing","Landshut sim-racing maker founded by Thomas Jackermeier; acquired by Corsair in 2024.",W+"Fanatec",["Fanatec direct-drive bases"],["Corsair"]),
 B(MZ,"","","Mainstream","direct-drive bases","Maker of R-series direct-drive bases, rims, pedals and shifters.",SN,["Moza R-series"]),
 B("Simucube","Finland","2007","Professional & flagship","direct-drive bases","Consumer brand of Granite Devices of Tampere, maker of high-end direct-drive bases.","https://simucube.com/about",["Simucube"]),
 B(HE,"Netherlands","2013","Professional & flagship","load-cell pedals","Dutch maker of pedals, shifters and handbrakes, designed and assembled in-house.",HK,["Heusinkveld pedals","Heusinkveld shifters"]),
 B("Playseat","Netherlands","","Mainstream","racing seats","Dutch cockpit maker founded by Fernando Smit.","https://www.d-box.com/en/blog/partner-spotlight-playseat",["Playseat"]),
 B("Next Level Racing","Australia","2009","Mainstream","sim cockpits","Gold Coast maker of cockpits, stands and motion platforms.","https://boxthislap.org/next-level-racing-gttrack/",["Next Level Racing GTtrack and F-GT"])]
w('E5','02_01',{"kinds":[wheel,base,rim,ped,shift,hb,cock],"brands":br,"traditions":[],
 "notes":"Racing wheel 39 to 2 archetypes + 14 models; Fanatec CSL DD kept only under wheelbase; TS-XW Servo Base moved to wheelbase; dropped Agetec, Mad Catz, Moza R5 Pro duplicate and Trucking bundle, Thermaltake G15, T98 Ferrari variants, T248R, PlayStation Move wheel, Xbox 360 Speed Wheel, maker-less NeoRacer. Rudder pedals (Honeycomb Charlie, Thrustmaster TFRP, Turtle Beach VelocityOne Rudder) moved to the Flight sim shelf's Rudder pedals kind; Thrustmaster T2PM and maker-less N64/PlayStation pedals dropped. Simagic EVO Sport/Ultra/Alpha U, Moza R9 V3/R12 V2/R21 Ultra variants folded into the R-series archetype or dropped. Fanatec help page blocked (403/404); no Simagic or Asetek page fetched, so they stay as models. Steering wheel rim models are Moza only (only retrieved rim list)."})
