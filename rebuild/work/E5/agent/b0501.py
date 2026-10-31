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
VIVE=W+'HTC_Vive'; WF='https://winfuture.de/news,108698.html'; RV='https://roadtovr.com/best-quest-3-accessories/'
BH='https://bhaptics.com/news/bhaptics-to-showcase-tactsuit-x-series-next-generation-haptic-suit-at-ces-2021'; BG='https://bhaptics.com/tactsuit/tactglove'
KAT='https://knoxlabs.com/products/kat-walk-c2'; OM=W+'Virtuix_Omni'

ctl={"n":"VR controller","a":"tracked controller · motion controller","d":"Hand-held controller tracked in 3D space by a VR headset or base stations; also see Motion controller.","t":["ring-tracked","self-tracked","finger tracking"],"s":W+"Oculus_Touch","x":[
 X("Oculus Touch","Touch · Touch Plus · Touch Pro","Pair of handheld units with a stick, buttons and triggers, the controller of the Rift and Quest lines.","Oculus","2016",W+"Oculus_Touch",
   [("Oculus Touch (1st gen)","Oculus","2016","Rift CV1, external sensors"),("Touch (2nd gen)","Oculus","2019","Rift S and Quest, rings face the user"),("Touch (3rd gen)","Meta","","Quest 2, thumbrest back"),("Touch Pro","Meta","2022","Quest Pro, onboard tracking"),("Touch Plus","Meta","","Quest 3 and 3S")]),
 X("Valve Index controller","Knuckles","Valve's controller strapped to the hand that senses each finger's position.","Valve","2019",WF,[("Valve Index controllers","Valve","2019","sold with the Index or as a pair")]),
 X("HTC Vive controller","Vive wand","Wand controller with a trackpad and sensor ring, tracked by Lighthouse base stations.","HTC","2016",VIVE,
   [("Vive controller","HTC","2016","original wand"),("Vive controller (SteamVR 2.0)","HTC","","blue, matches the Vive Pro")]),
 X("PlayStation VR2 Sense controller","Sense controller","Sony's PS VR2 controller pair, tracked by the headset's cameras.","Sony","2023",W+"PlayStation_VR2",[])]}

trk={"n":"VR tracker or base station","a":"Lighthouse · puck tracker","d":"Base station that lets a headset track its position, or a puck strapped to the body or an object so it shows up in VR.","t":["base station","body tracker","facial tracker"],"s":VIVE,"x":[
 X("SteamVR Base Station","Lighthouse","Box that sweeps a room with infrared lasers so Lighthouse headsets, controllers and trackers find their position.","Valve","2016",VIVE,
   [("SteamVR Base Station 1.0","HTC","2016","with the original Vive"),("SteamVR Base Station 2.0","Valve","2019","larger tracking volume; with the Vive Pro full kit and Valve Index")]),
 X("Vive Tracker","Vive puck","HTC's puck that adds a tracked body part or object to SteamVR.","HTC","",VIVE,
   [("Vive Tracker","HTC","","three iterations by 2021"),("Vive Ultimate Tracker","HTC","","inside-out, no base stations")])],
 "m":[["Vive Facial Tracker","HTC"]]}

strap={"n":"VR head strap or facial interface","a":"battery strap · elite strap · face cushion","d":"Replacement strap, battery strap, face cushion or cover that makes a headset fit or last longer.","t":["rigid strap","battery strap","audio strap","facial interface","silicone cover"],"s":RV,"x":[
 X("Meta Elite Strap","Elite Strap","Meta's rigid replacement strap for Quest headsets, with or without a rear battery.","Meta","",RV,
   [("Meta Elite Strap","Meta","",""),("Meta Elite Strap with Battery","Meta","","rear battery")]),
 X("Vive Deluxe Audio Strap","Deluxe Audio Strap","Rigid replacement strap for the first Vive with built-in over-ear speakers.","HTC","2017",VIVE,[]),
 X("BOBOVR M3","","BOBOVR's battery head strap for Quest 3 with hot-swappable batteries.","BOBOVR","",RV,[("BOBOVR M3 Pro","BOBOVR","","with battery; dock sold separately")]),
 X("KIWI Design head strap","K4","KIWI Design's padded replacement straps for Quest headsets.","KIWI Design","",RV,[("KIWI Design K4 Headstrap","KIWI Design","","")])],
 "m":[["KIWI Design V3 Facial Interface","KIWI Design"],["KIWI Design V4 Silicone Cover","KIWI Design"],["VR Cover for Quest 3 & 3S","VR Cover"]]}

tm={"n":"VR treadmill","a":"omnidirectional treadmill · locomotion platform","d":"Low-friction platform with a harness that lets a player walk or run on the spot in any direction in VR.","s":OM,"x":[
 X("Virtuix Omni","Omni One","Kickstarter-funded omnidirectional treadmill used with special shoes and a support ring.","Virtuix","2016",OM,
   [("Virtuix Omni","Virtuix","2016","first units shipped"),("Omni Pro","Virtuix","","commercial only from 2017"),("Omni One","Virtuix","2023","home model, first units to investors")]),
 X("KAT Walk C","KAT Walk C2","KatVR's compact personal VR treadmill.","KatVR","",KAT,[("KAT Walk C2","KatVR","",""),("KAT Walk C2+","KatVR","","adds haptics and sitting module")])],
 "m":[["Cyberith Virtualizer","Cyberith"],["Wizdish ROVR","Wizdish"]]}

hap={"n":"Haptic vest or glove","a":"haptic suit · haptic glove","d":"Vest, sleeve or glove with vibration motors that let a player feel hits and touches in VR.","t":["vest","arm and hand","face cushion","glove"],"s":BH,"x":[
 X("bHaptics TactSuit","Tactot","bHaptics' haptic vest line.","bHaptics","",BH,
   [("Tactot","bHaptics","","predecessor"),("TactSuit X16","bHaptics","2021","16 motors"),("TactSuit X40","bHaptics","2021","40 motors"),("TactSuit Pro","bHaptics","",""),("TactSuit Air","bHaptics","","")]),
 X("bHaptics TactGlove","","Fabric glove with fingertip and wrist actuators that relies on the headset's hand tracking.","bHaptics","",BG,
   [("TactGlove DK2","bHaptics","","6 haptic points"),("TactGlove DK3","bHaptics","","tested with Quest 3")])],
 "m":[["Tactosy","bHaptics"],["Tactal","bHaptics"]]}

K="knowledge"
br=[B("Meta","United States","2004","Mainstream","Quest headsets","Owner of Oculus; sells the Quest line through its Reality Labs division.",K,["Meta Quest","Meta Elite Strap"],["Oculus"]),
 B("Oculus","United States","2012","Mainstream","Rift headsets","Palmer Luckey's VR company behind the Rift and Touch controllers; later part of Meta.",W+"Oculus_Touch",["Oculus Rift","Oculus Touch"],["Meta"]),
 B("HTC","Taiwan","1997","Mainstream","Vive headsets","Taiwanese electronics maker whose Vive line covers PC and standalone headsets and trackers.",K,["HTC Vive","Vive Tracker"],["Valve"]),
 B("Valve","United States","1996","Premium","Index, Steam","Game company and Steam store owner that makes the Index headset and Lighthouse tracking.",K,["Valve Index","SteamVR Base Station"],["HTC"]),
 B("Sony","Japan","1946","Mainstream","PlayStation","Japanese electronics group behind PlayStation and its VR headsets.",K,["PlayStation VR"]),
 B("BOBOVR","","","Value","Quest straps","Maker of battery head straps for Quest headsets.",RV,["BOBOVR M3"]),
 B("KIWI Design","","","Value","Quest accessories","Maker of straps, facial interfaces and covers for Quest headsets.",RV,["KIWI Design head strap"]),
 B("Virtuix","","","Specialist","VR treadmills","Jan Goetgeluk's company behind the Omni treadmill.",OM,["Virtuix Omni"]),
 B("KatVR","","","Specialist","VR treadmills","Maker of the KAT Walk treadmills.",KAT,["KAT Walk C"]),
 B("bHaptics","","2015","Specialist","haptic vests","Maker of TactSuit vests, Tactosy sleeves and TactGlove.",BH,["bHaptics TactSuit","bHaptics TactGlove"])]

w('E5','05_01',{"kinds":[ctl,trk,strap,tm,hap],"brands":br,"traditions":[],
 "notes":"All five kinds new (no old data). Controllers: Touch, Index, Vive wand, PS VR2 Sense (no version list attested for Sense). Trackers: base stations 1.0/2.0, Vive Tracker and Ultimate Tracker; no tracker-generation years attested. Straps: Meta Elite, Vive Deluxe Audio Strap, BOBOVR, KIWI; no Yoges/ZyberVR (search snippets only). Treadmills: Omni, KAT Walk C; Infinadeck not attested. Haptics: bHaptics only; other glove makers (HaptX, SenseGlove) not researched (mostly enterprise)."})
