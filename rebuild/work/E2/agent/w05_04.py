import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
from write import w, K
def A(n,a,d,mk,y,s,v=None,dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: x["v"]=[dict((k,val) for k,val in zip(("n","mk","y","d"),vv) if val) for vv in v]
    if dt: x["dt"]=dt
    return x
TM="Tokyo Marui"; TMW="https://en.wikipedia.org/wiki/Tokyo_Marui"; LST="https://en.wikipedia.org/wiki/List_of_paintball_markers"
PE="Planet Eclipse"; TP="Tippmann"; TPW="https://en.wikipedia.org/wiki/Tippmann"; HOP="https://paintballer.co/best-paintball-hoppers/"
ag=K("Airsoft gun","airsoft marker","Replica gun that fires plastic BB pellets by spring, gas or electric power, made for airsoft play.","https://www.redwolfairsoft.com/guns/airsoft-rifles/electric-rifles",
  [("Nemesis LS12","Classic Army"),("FAR 9","G&G"),("TR80 DMR","G&G"),("Trident MK3","Krytac"),("SSR74","Novritsch"),("SSR77 A2","Novritsch"),("MDR-X","Silverback"),("Evolt",TM),("Avalon Samurai Edge","VFC")],None,
  ["spring","AEG (automatic electric gun)","AEP (electric pistol)","GBB (gas blowback)","NBB (gas non-blowback)","HPA"])
ag["x"]=[
 A("Tokyo Marui AEG","automatic electric gun","Battery-powered motor-and-gearbox replica; Tokyo Marui is credited with the original AEG gearbox.",TM,"1992",TMW,
   [("FA-MAS 5.56-F1",TM,"1992","first AEG"),("Glock 18C AEP",TM,"2005","first automatic electric pistol")],"gearbox version · battery · licensed or unlicensed markings"),
 A("Next Generation Recoil Shock","NGRS · Next Gen","Tokyo Marui AEG with a reciprocating weight that simulates recoil and bolt-lock on an empty magazine.",TM,"",
   "https://www.evike.com/products/86980/Tokyo-Marui-Next-Generation-Recoil-Shock-System-AK102-AEG-Rifle-Color-Black/",
   [("AK102 Next Generation",TM,"","metal receiver, folding stock")],"platform: M4, AK, HK416, SCAR · metal receiver"),
 A("Hi-Capa","","Tokyo Marui's gas-blowback high-capacity pistol family, the base of many race and custom guns.",TM,"",TMW,
   [("Hi-Capa 4.3",TM,"",""),("Hi-Capa 5.1",TM,"",""),("Hi-Capa D.O.R",TM,"",""),("Hi-Capa Xtreme .45",TM,"","")],"slide length · gas · upgrade parts"),
 A("VSR-10","","Tokyo Marui's spring bolt-action sniper rifle, the standard base for upgraded airsoft snipers.",TM,"",TMW,
   [("VSR-10 Pro-sniper",TM,"",""),("VSR-10 Real Shock",TM,"","imitation recoil"),("VSR-10 G-Spec",TM,"","suppressor-ready")],"stock colour · barrel · upgrade parts"),
 A("M92F Samurai Edge","Samurai Edge","Tokyo Marui gas pistol made in character editions from the Biohazard (Resident Evil) games.",TM,"1999",TMW,
   [("Samurai Edge Jill Model",TM,"1999–2000",""),("Samurai Edge Chris Model",TM,"2000",""),("Samurai Edge Barry Model",TM,"2001","")])]
pg=K("Paintball gun","paintball marker","Compressed-gas gun that fires paint-filled balls, made for paintball play.","https://en.wikipedia.org/wiki/Paintball_marker",
  [("Emek MG100",PE),("Etha",PE),("Etek",PE),("CS3",PE),("DSR+","Dye"),("Mini","Empire"),("Intimidator","Bob Long Technologies"),("Ion","Smart Parts")],None,
  ["pump","mechanical semi-auto","electropneumatic","spool valve","poppet valve","magazine-fed"])
pg["x"]=[
 A("Nelspot 007","","Nelson's inline pump marker, among the earliest markers; the PMI Tracer and CCI Phantom followed its design.","Nelson","",LST),
 A("Automag","","Airgun Designs' semi-automatic marker that set the pace in its era.","Airgun Designs","",LST),
 A("Spyder","","Kingman's low-cost mechanical blowback marker series.","Kingman","",LST,
   [("Spyder Classic","Kingman","",""),("Spyder MR","Kingman","",""),("Spyder VS2","Kingman","","mechanical"),("Spyder MRX","Kingman","2012","magazine-fed")]),
 A("98 Custom","Model 98","Tippmann's rugged, upgradeable mechanical marker with a split receiver, unchanged in essentials since launch; the classic rental and starter gun.",TP,"1998",TPW,None,"stock · barrel · electronic trigger kit"),
 A("A-5","","Tippmann mechanical marker fed by the gas-driven Cyclone feed system.",TP,"",TPW,
   [("A-5",TP,"",""),("X7",TP,"2006","enhanced Cyclone"),("X7 Phenom",TP,"","blow-forward"),("TMC",TP,"2016","M4-style")]),
 A("Angel","WDP Angel","Angel Paintball Sports' marker that pioneered electronic firing.","Angel","",LST,[("Angel LCD","Angel","","")]),
 A("Shocker","","Smart Parts' electropneumatic tournament marker.","Smart Parts","",LST,[("NXT Shocker","Smart Parts","",""),("SFT Shocker","Smart Parts","","")]),
 A("Ego","","Planet Eclipse's electropneumatic poppet-valve, stacked-tube tournament marker.",PE,"",LST),
 A("Geo","","Planet Eclipse's spool-valve electronic tournament marker series.",PE,"",LST,[("Geo r5",PE,"","")]),
 A("Matrix","DM","Dye's electronic tournament marker series.","Dye","",LST,[("Proto Matrix","Dye","",""),("DM","Dye","","")]),
 A("Axe","","Empire's electronic tournament marker.","Empire","",LST)]
hop=K("Paintball hopper","loader","Feed container mounted on a paintball marker that holds the paintballs and feeds them to it.","https://badlandspaintball.com/paintball-hoppers.html/",
  [("Halo Pro","Empire"),("Halo Too","Empire"),("VMAX+","Empire"),("GFX","HK Army"),("TFX 3.0","HK Army"),("Triad","JT"),("Revolution","JT"),("PAL FS.68",PE),("Speedster",PE),("V-Max Plus","Valken"),("Proto Primo","Dye")],None,
  ["gravity","agitating","force-fed (electronic)","gas-driven (Cyclone)"])
hop["x"]=[
 A("Rotor","Dye Rotor","Dye's electronic force-fed loader using Rotor Force Fed Technology.","Dye","",HOP,
   [("Rotor R2","Dye","","first adjustable-capacity loader"),("LT-R","Dye","",""),("Box Rotor","Dye","","")],"capacity · colourway"),
 A("Spire","Virtue Spire","Virtue's motorised electronic loader.","Virtue","",HOP,[("Spire IR2","Virtue","",""),("Spire IV","Virtue","",""),("Spire V","Virtue","","")]),
 A("Cyclone Feed System","Cyclone","Tippmann's non-electronic agitated feed that uses exhaust gas from each shot; standard on the A-5.",TP,"",TPW)]
mask=K("Paintball mask","paintball goggles","Full-face mask with a goggle lens made to protect the eyes and face from paintballs or airsoft pellets.","https://us.novritsch.com/product/dye-i5-mask/",
  [("i5","Dye"),("VIO Ascend","Virtue"),("EVS","Empire"),("Spectra Flex 8","JT"),("KLR","HK Army")],None,["thermal (dual-pane) lens","single lens","full-head","glasses-friendly"])
tank=K("Paintball air tank","HPA tank · CO2 tank","Refillable cylinder of CO2 or compressed air, with regulator, that powers a paintball or HPA airsoft gun.","https://propaintball.com/compressed-air-paintball-tanks/",
  [("Carbon Fiber HPA Tank","Ninja"),("Basics Carbon Fiber HPA Tank","Empire"),("Hero 2.0 Carbon Fiber","First Strike"),("Myth G3 Nitrogen Tank","Guerrilla Air"),("20oz CO2 Tank","JT"),("24oz CO2 Tank","Empire"),("Aluminum CO2 Tank",TP)],None,
  ["CO2 (20 oz, 24 oz)","HPA aluminium 3000 psi","HPA carbon fibre 4500 psi","nitrogen"])
w('E2','05_04',{"kinds":[ag,pg,hop,mask,tank],
 "brands":[
  {"n":"Tokyo Marui","c":"Japan","f":"1965","seg":"Professional & flagship","kf":"airsoft guns","d":"Tokyo airsoft maker credited with the first AEG (1992) and the standard AEG gearbox.","lines":["Next Generation Recoil Shock","Hi-Capa","VSR-10"],"sig":["Tokyo Marui AEG","Hi-Capa","VSR-10"],"s":TMW},
  {"n":"Tippmann","c":"United States","f":"1986","seg":"Mainstream","kf":"paintball markers","d":"Fort Wayne, Indiana paintball maker; owned by G.I. Sportz from 2013.","lines":["98 Custom","A-5","X7"],"sig":["98 Custom","A-5","Cyclone Feed System"],"rel":["Kingman"],"s":TPW},
  {"n":"Planet Eclipse","c":"United Kingdom","seg":"Professional & flagship","kf":"tournament markers","d":"British maker of high-end electronic paintball markers.","sig":["Ego","Geo"],"rel":["Dye","Empire"],"s":"knowledge"},
  {"n":"Dye","c":"United States","seg":"Professional & flagship","kf":"markers, masks, loaders","d":"American paintball brand (Dye Precision) known for the i5 mask and Rotor loader.","sig":["Matrix","Rotor"],"rel":["Planet Eclipse","Virtue"],"s":"knowledge"},
  {"n":"Kingman","c":"United States","seg":"Value","kf":"Spyder markers","d":"American maker of the low-cost Spyder marker series.","sig":["Spyder"],"rel":["Tippmann"],"s":"knowledge"}],
 "traditions":[],
 "notes":"All four old kinds kept; Paintball air tank added (CO2, HPA, nitrogen; models from Pro Paintball's tank guide). Airsoft: archetypes Tokyo Marui AEG, NGRS, Hi-Capa, VSR-10, Samurai Edge; old models kept in m (Avalon Samurai Edge is VFC's rifle, not the Marui pistol). Markers: Nelspot 007, Automag, Spyder, 98 Custom, A-5, Angel, Shocker, Ego, Geo, Matrix, Axe; Emek MG100 kept in m. Hopper: Rotor, Spire and Cyclone archetypes; Box Rotor, Rotor R2, LT-R, Spire IR2/V and Cyclone moved from m into them; Splitter dropped (no description). Mask: four makers added from Pro Paintball's guide. Not sourced, so left out: release years for Ego/Geo/CS/Axe/Spyder, which loader first used force-feed, Dye M3+, Empire Vents, JT Proflex, G&G/Krytac/VFC archetypes."})
