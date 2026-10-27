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
T='Thrustmaster'; TM=W+'Thrustmaster'; V='VKB'; H='Honeycomb Aeronautical'; TB='Turtle Beach'
HC='https://techcrunch.com/2023/03/06/honeycomb-alpha-flight-control-xpc-yoke-and-bravo-throttle-take-flight-sim-review-pc-xbox'
NXT='https://stormbirds.blog/2020/08/11/vkb-announces-gladiator-nxt/'; GF='https://stormbirds.blog/2017/01/09/our-first-look-at-the-vkb-gunfighter-series/'
RF='https://forums.flightsimulator.com/t/honeycomb-charlie-or-mfg-crosswinds-rudder-pedals/592274'
stick={"n":"Flight stick","a":"joystick · HOTAS · HOSAS","d":"Joystick controller for flight and space games, sold alone or as a stick-and-throttle (HOTAS) set.","t":["stick only","HOTAS set","HOSAS dual-stick set","sidestick"],"s":"https://en.wikipedia.org/wiki/Saitek_X52","x":[
 X("Thrustmaster HOTAS Cougar and Warthog","HOTAS Warthog","Thrustmaster's metal replica-style HOTAS line; the Warthog replaced the Cougar in 2010.",T,"",TM,
   [("Thrustmaster HOTAS Cougar",T,"","replaced in 2010"),("Thrustmaster HOTAS Warthog",T,"2010",""),("HOTAS Warthog MKII",T,"","")]),
 X("Thrustmaster T.16000M","T.16000M FCS","Thrustmaster's ambidextrous stick sold alone or in HOTAS, flight-pack and dual-stick sets.",T,"2009",TM,
   [("Thrustmaster T.16000M",T,"2009","stick"),("T.16000M FCS HOTAS",T,"","with TWCS throttle"),("T.16000M FCS Flight Pack",T,"","with throttle and rudder pedals"),("T.16000M FCS Space Sim Duo",T,"","two sticks")]),
 X("Thrustmaster T.Flight","T.Flight HOTAS","Thrustmaster's entry HOTAS line for PC and consoles.",T,"2008",TM,
   [("Thrustmaster T-Flight HOTAS-X",T,"2008",""),("T.Flight HOTAS 4",T,"","PlayStation"),("T.Flight HOTAS One",T,"","Xbox"),("T.Flight Hotas 5",T,"",""),("Thrustmaster T.Flight Hotas Neo",T,"",""),("T.Flight Stick X",T,"",""),("T.Flight Full Kit X",T,"","")]),
 X("Thrustmaster TCA Sidestick Airbus Edition","TCA Sidestick","Airliner-style sidestick in the Thrustmaster Civil Aviation range.",T,"2020",TM,
   [("Thrustmaster TCA Sidestick Airbus Edition",T,"2020",""),("TCA Sidestick X Airbus Edition",T,"","Xbox"),("TCA Officer Pack Airbus Edition",T,"","with throttle quadrant"),("TCA Captain Pack X Airbus Edition",T,"","")]),
 X("Saitek X52","X52 Pro · X56","Saitek's HOTAS with a backlit throttle display, now supported by Logitech.","Saitek","2004",W+"Saitek_X52",
   [("Saitek X52","Saitek","2004","blue LCD, single centring spring"),("Saitek X52 Pro","Saitek","","green LCD, dual springs"),("Saitek Pro Flight X-56 H.O.T.A.S.","Saitek","","")]),
 X("VKB Gunfighter","","VKB's all-metal modular stick base with metal gimbals and adjustable dry clutches.",V,"2017",GF,
   [("VKB Gunfighter",V,"2017","base, gimbal, KG-12 grip"),("VKB Gunfighter Pro",V,"2017","20 cm extension, cockpit base plate"),("VKB Gunfighter Mk.III",V,"",""),("VKB Gunfighter Mk.IV",V,"","")],"grip · extension"),
 X("VKB Gladiator NXT","","VKB's plastic complete stick, successor to the Gladiator Mk.II; grips also fit the Gunfighter.",V,"2020",NXT,
   [("VKB Gladiator NXT",V,"2020","Standard and Premium, left or right hand"),("VKB Gladiator NXT EVO",V,"","")])],
 "m":[["Logitech G Extreme 3D Pro","Logitech"],["Turtle Beach VelocityOne Flightstick",TB],["Turtle Beach VelocityOne Flightdeck",TB],["SOL-R 1 Flightstick",T],["SOL-R 2 HOSAS Space Sim Duo",T],["SOL-R 4 HOTAS",T],["AVA F/A-18 Super Hornet Flightstick",T]]}
yoke={"n":"Flight yoke","a":"yoke","d":"Controller with a yoke handle on a column that pushes, pulls and turns, made for flying aircraft in games and simulators.","s":TM,"x":[
 X("Honeycomb Alpha","Alpha Flight Controls","Self-centring yoke with built-in light, electrical and five-position ignition switches.",H,"",HC,
   [("Honeycomb Alpha Flight Controls Yoke",H,"",""),("Honeycomb Alpha Flight Controls XPC",H,"","PC, Xbox via separate hub")]),
 X("Thrustmaster TCA Yoke Boeing Edition","TCA Yoke","Airliner-style yoke in the Thrustmaster Civil Aviation range.",T,"2021",TM,
   [("Thrustmaster TCA Yoke Pack Boeing Edition",T,"2021","with throttle quadrant"),("TCA Yoke Boeing Edition",T,"","yoke only")])],
 "m":[["Saitek Pro Flight Yoke System","Saitek"],["TCA Sky Yoke",T]]}
thr={"n":"Flight throttle","a":"throttle quadrant","d":"Lever unit sold apart from a stick or yoke that sets engine power, often with flap or trim levers. A stick-and-throttle set (HOTAS) is a flight stick.","s":"https://thrustmaster.com/products/tca-quadrant-airbus-edition","x":[
 X("Honeycomb Bravo","Bravo Throttle Quadrant","Six-lever throttle quadrant with trim wheel, flap lever, autopilot keys and annunciator lights.",H,"",HC,[("Honeycomb Bravo Throttle Quadrant",H,"","")]),
 X("WinWing Orion 2 throttle","Orion2","Metal fighter-style throttle with detents and many buttons.","WinWing","2022","https://simulatorhardware.com/products/winwing-orion2-throttle-fa18-max/msfs",
   [("Orion 2 F/A-18 Throttle","WinWing","2022","two levers, 6 axes, 80 buttons")])],
 "m":[["HOTAS Warthog Dual Throttle",T],["TCA Quadrant Airbus Edition",T],["TCA Quadrant Add-On Airbus Edition",T],["TCA Quadrant Boeing Edition",T],["TWCS Throttle",T],["Viper TQS",T],["SOL-R 6 Throttle",T],["VKB Gladiator NXT EVO Omni Throttle",V],["VKB THQ",V]]}
rud={"n":"Rudder pedals","a":"flight pedals","d":"Foot pedals that control yaw and often toe brakes in flight simulators.","t":["sliding","pendular","toe brakes","dampers"],"s":RF,"x":[
 X("Honeycomb Charlie","Charlie Rudder Pedals","Aluminium rudder pedals with Hall-effect sensors on yaw and both toe brakes.",H,"2023","https://www.key.aero/article/honeycomb-charlie-rudder-pedals-review",[])],
 "m":[["Thrustmaster TPR Pendular Rudder",T],["Thrustmaster T-Flight Rudder Pedals (TFRP)",T],["MFG Crosswind V3","MFG"],["VKB T-Rudder MK IV",V],["Turtle Beach VelocityOne Rudder Pedals",TB],["CH Pedals","CH Products"]]}
pan={"n":"Flight-sim control panel","a":"cockpit panel · switch panel","d":"Panel of switches, knobs, displays or MFD bezels that sends cockpit inputs to a flight simulator.","t":["switch panel","radio panel","autopilot panel","instrument panel","MFD bezel","button box"],
 "s":"https://pilotmall.com/collections/flight-simulation-hardware",
 "m":[["Logitech G Pro Flight Switch Panel","Logitech"],["Logitech G Flight Radio Panel","Logitech"],["Logitech G Flight Multi Panel","Logitech"],["Logitech G Flight Instrument Panel","Logitech"],["VKB FSM front switchboard module",V],["VKB SEM side extension module",V]]}
br=[B(T,"United States","1990","Mainstream","wheels & flight sticks","Hillsboro, Oregon maker of flight controls and wheels, owned by Guillemot.",TM,["Thrustmaster HOTAS Cougar and Warthog","Thrustmaster T.16000M","Thrustmaster T.Flight"],["Guillemot"]),
 B("Saitek","","","Mainstream","flight sticks","Flight-control brand of the X52 and Pro Flight range; taken over by Logitech in 2016.",W+"Saitek_X52",["Saitek X52"],["Logitech"]),
 B(V,"","","Specialist","flight sticks","VKB-Sim, maker of Gunfighter metal bases and Gladiator sticks.",GF,["VKB Gunfighter","VKB Gladiator NXT"]),
 B(H,"","","Specialist","civil flight controls","Maker of the Alpha yoke, Bravo throttle and Charlie rudder pedals.",HC,["Honeycomb Alpha","Honeycomb Bravo","Honeycomb Charlie"]),
 B("WinWing","","","Specialist","military flight controls","Maker of fighter-style throttles, sticks and panels.","https://simulatorhardware.com/products/winwing-orion2-throttle-fa18-max/msfs",["WinWing Orion 2 throttle"])]
w('E5','02_02',{"kinds":[stick,yoke,thr,rud,pan],"brands":br,"traditions":[],
 "notes":"Flight stick 33 models grouped into 7 archetypes (Thrustmaster Cougar/Warthog, T.16000M, T.Flight, TCA Sidestick; Saitek X52; VKB Gunfighter, Gladiator NXT) plus 7 models; dropped Hori Ace Combat 6 Flight Stick (named after a game title) and duplicate Thrustmaster HOTAS Warthog/Flight Stick entries. Rudder pedals is a new kind taking the rudder sets moved from the Sim racing Pedal set kind (Honeycomb Charlie, Thrustmaster TFRP, Turtle Beach VelocityOne). Control panel models: Logitech G panels and VKB modules (no WinWing MFD page retrieved). Throttle adds VKB THQ and WinWing Orion 2."})
