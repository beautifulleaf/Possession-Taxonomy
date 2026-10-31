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
CMP=W+'Comparison_of_virtual_reality_headsets'
XP='https://xpert.digital/en/xr-glasses-comparison-test/'
MX='https://mixed-news.com/en/xreal-introduces-new-ar-glasses-with-native-3dof-tracking-larger-field-of-view-and-in-house-x1-chip/'
PA='https://www.phonearena.com/reviews/viture-pro-review_id6881'
AC='https://www.androidcentral.com/gaming/virtual-reality/rokid-max-2-review'

sa={"n":"Standalone VR headset","a":"mixed-reality headset · all-in-one headset","d":"Headset that encloses the eyes and has its own computer and battery, often with camera passthrough for mixed reality.",
 "t":["VR only","colour-passthrough mixed reality"],"s":"https://www.reality-atlas.com/hardware","x":[
 X("Meta Quest","Oculus Quest","Meta's (formerly Oculus) line of standalone headsets with inside-out tracking and Touch controllers.","Meta","2019",W+"Meta_Quest",
   [("Oculus Quest","Oculus","2019","first generation"),("Quest 2","Meta","2020","launched as Oculus Quest 2, renamed 2022"),("Quest Pro","Meta","2022","premium model, colour passthrough, Touch Pro controllers"),("Quest 3","Meta","2023","pancake lenses, Snapdragon XR2 Gen 2"),("Quest 3S","Meta","2024","lower-priced model, same chip as Quest 3")],"storage 64–512 GB"),
 X("Apple Vision Pro","","Apple's standalone mixed-reality 'spatial computer' controlled by eyes, hands and voice, running visionOS.","Apple","2024",W+"Apple_Vision_Pro",
   [("Apple Vision Pro (M2)","Apple","2024","M2 with R1 co-processor"),("Apple Vision Pro (M5)","Apple","2025","M5 update")]),
 X("Samsung Galaxy XR","","Samsung's standalone mixed-reality headset, the first to run Android XR, with a tethered battery pack.","Samsung","2025",W+"Samsung_Galaxy_XR",
   [("Samsung Galaxy XR","Samsung","2025","Snapdragon XR2+ Gen 2, 16 GB RAM")]),
 X("HTC Vive Focus","Vive Focus","HTC's standalone Vive line.","HTC","2018",W+"HTC_Vive",
   [("HTC Vive Focus","HTC","2018",""),("Vive Focus Plus","HTC","2019",""),("HTC Vive Focus 3","HTC","2021",""),("HTC Vive Focus Vision","HTC","2024","also works tethered to a PC")]),
 X("Pico 4","Pico Neo","Standalone headset line from Pico, a ByteDance division.","Pico","2022",W+"PICO_4",
   [("Pico Neo 3","Pico","","predecessor"),("Pico Neo 3 Pro","Pico","2021",""),("Pico 4","Pico","2022",""),("Pico 4 Ultra","Pico","2024","successor")])],
 "m":[["Oculus Go","Oculus"],["HTC Vive XR Elite","HTC"],["HTC Vive Flow","HTC"],["Lenovo Mirage Solo","Lenovo"],["Valve Steam Frame","Valve"],["Pimax Portal View","Pimax"],["Lynx R1","Lynx"],["Lynx R2","Lynx"],["Play For Dream MR","Play For Dream"],["Pico G2 4K","Pico"],["DPVR P2","DPVR"],["iQIYI Qiyu MIX","iQIYI"],["SimulaVR Simula One","SimulaVR"]]}

te={"n":"Tethered VR headset","a":"PC VR headset · console VR headset","d":"Headset that encloses the eyes and needs a console or PC to run it.",
 "t":["outside-in (base stations or camera)","inside-out tracking","eye tracking"],"s":"https://www.reality-atlas.com/hardware","x":[
 X("Oculus Rift","Rift","The headset that started the 2010s VR revival, from development kits to the consumer Rift and Rift S.","Oculus","2013",W+"Oculus_Rift",
   [("Oculus Rift DK1","Oculus","2013","development kit, 7-inch LCD"),("Oculus Rift DK2","Oculus","2014","OLED, positional tracking"),("Oculus Rift CV1","Oculus","2016","first consumer version"),("Oculus Rift S","Oculus","2019","inside-out tracking; discontinued 2021")]),
 X("HTC Vive","Vive","HTC's PC headset line built with Valve, tracked by Lighthouse base stations.","HTC","2016",W+"HTC_Vive",
   [("HTC Vive","HTC","2016","first generation"),("HTC Vive Pro","HTC","2018",""),("Vive Pro Eye","HTC","2019","eye tracking"),("HTC Vive Pro 2","HTC","2021","2448×2448 per eye, 120 Hz")]),
 X("HTC Vive Cosmos","Cosmos","HTC's PC headset with inside-out camera tracking and swappable faceplates.","HTC","2019",W+"HTC_Vive",
   [("HTC Vive Cosmos","HTC","2019",""),("Vive Cosmos Elite","HTC","2020","Lighthouse faceplate")]),
 X("Valve Index","Index","Valve's PC headset with Lighthouse 2.0 tracking, finger-tracking Knuckles controllers and up to 144 Hz.","Valve","2019",W+"Valve_Index",
   [("Valve Index","Valve","2019","full kit with base stations and controllers")]),
 X("PlayStation VR","PS VR · PSVR2","Sony's console headsets for PlayStation 4 and 5.","Sony","2016",W+"Sony_PlayStation_Virtual_Reality",
   [("PlayStation VR (CUH-ZVR1)","Sony","2016","PlayStation 4, needs PlayStation Camera"),("PlayStation VR (CUH-ZVR2)","Sony","2017","slimmer cable, built-in headphones"),("PlayStation VR2","Sony","2023","PlayStation 5, OLED, eye tracking, inside-out tracking; PC adapter 2024")]),
 X("Pimax wide-FOV headsets","Pimax","Pimax's high-resolution, wide-field-of-view PC headsets.","Pimax","2016",W+"Pimax",
   [("Pimax 4K","Pimax","2016","first product"),("Pimax 5K Plus","Pimax","2018",""),("Pimax 5K XR","Pimax","2018",""),("Pimax 8K","Pimax","2019",""),("Pimax Vision 8K X","Pimax","2019",""),("Pimax Vision 8K Plus","Pimax","2019",""),("Pimax 5K Super","Pimax","2020",""),("Pimax Artisan","Pimax","2020",""),("Pimax Crystal","Pimax","2023",""),("Pimax Crystal Light","Pimax","2024",""),("Pimax Crystal Super","Pimax","2024",""),("Pimax Dream Air","Pimax","2025",""),("Pimax Dream Air SE","Pimax","2025","")]),
 X("Bigscreen Beyond","Beyond","Ultra-light PC headset with a facial interface 3D-printed from a scan of the owner's face.","Bigscreen","2023",W+"Bigscreen_Beyond",
   [("Bigscreen Beyond","Bigscreen","2023","127 g, fixed IPD"),("Bigscreen Beyond 2","Bigscreen","","announced 2025; wider field of view, manual IPD"),("Bigscreen Beyond 2e","Bigscreen","","adds eye tracking")]),
 X("Windows Mixed Reality headset","WMR","PC headsets built by several makers to Microsoft's Windows Mixed Reality platform, with inside-out tracking.","","2017",CMP,
   [("Lenovo Explorer","Lenovo","2017",""),("Acer AH101","Acer","2017",""),("Dell Visor","Dell","2017",""),("Samsung HMD Odyssey","Samsung","2017",""),("Asus HC102","ASUS","2018",""),("Samsung Odyssey+","Samsung","2018",""),("HP Reverb G1","HP","2019",""),("HP Reverb G2","HP","2020","")])],
 "m":[["Varjo Aero","Varjo"],["Shiftall MeganeX","Shiftall"],["Somnium Space VR1","Somnium Space"],["Immersed Visor","Immersed"],["Razer OSVR HDK 1.4","Razer"],["Razer OSVR HDK 2","Razer"],["Fove 0","Fove"],["DPVR E4","DPVR"],["Deepoon VR E3","Deepoon"]]}

ph={"n":"Phone VR viewer","a":"Cardboard · Gear VR","d":"Headset that encloses the eyes and holds a phone as its screen and computer.","t":["cardboard","plastic","fabric"],"s":"https://www.reality-atlas.com/hardware","x":[
 X("Google Cardboard","Cardboard","Google's fold-out cardboard viewer with open specifications that anyone could make.","Google","2014",W+"Google_Cardboard",
   [("Google Cardboard","Google","2014","official viewer sold until 2021"),("View-Master Virtual Reality Starter Pack","Mattel","2015","made with Google")]),
 X("Samsung Gear VR","Gear VR","Samsung's plastic phone headset for Galaxy phones, made with Oculus.","Samsung","2015",CMP,[("Samsung Gear VR","Samsung","2015","")]),
 X("Google Daydream View","Daydream View","Fabric-covered phone headset with a handheld controller for Google's Daydream platform.","Google","2016",W+"Google_Daydream",
   [("Daydream View (1st gen)","Google","2016",""),("Daydream View (2nd gen)","Google","2017","wider field of view")])],
 "m":[["Zeiss VR One","Carl Zeiss"],["Homido","Homido"],["Merge VR","Merge VR"],["Destek VONE","Destek"],["DSCVR Cardboard","DSCVR"]]}

xg={"n":"XR display glasses","a":"AR glasses · video glasses · wearable display","d":"Sunglasses-style glasses with built-in screens that show a large virtual screen from a phone, console or PC over USB-C.",
 "t":["display only","3DoF screen anchoring","electrochromic dimming"],"s":XP,"x":[
 X("Xreal Air and One","Nreal · Xreal Air","Xreal's display glasses; the One adds an in-house X1 chip that anchors the screen in place.","Xreal","",MX,
   [("Xreal Air 2","Xreal","","46° field of view"),("Xreal One","Xreal","2024","X1 chip, 3DoF, 50°"),("Xreal One Pro","Xreal","2025","57° field of view")]),
 X("Viture Pro XR","Viture One","Viture's display glasses with micro-OLED screens, myopia sliders and electrochromic dimming.","Viture","",PA,
   [("Viture One Lite XR","Viture","",""),("Viture Pro XR","Viture","","1080p, 120 Hz")]),
 X("Rokid Max","","Rokid's display glasses for phones, handheld PCs and consoles.","Rokid","",AC,[("Rokid Max 2","Rokid","2025","")])],
 "m":[["RayNeo Air 2S","RayNeo"]]}

K="knowledge"
br=[B("Meta","United States","2004","Mainstream","Quest headsets","Owner of Oculus; sells the Quest line through its Reality Labs division.",K,["Meta Quest"],["Oculus"]),
 B("Oculus","United States","2012","Mainstream","Rift headsets","Palmer Luckey's VR company behind the Rift; bought by Facebook (now Meta) in 2014.",W+"Oculus_Rift",["Oculus Rift"],["Meta"]),
 B("HTC","Taiwan","1997","Mainstream","Vive headsets","Taiwanese electronics maker whose Vive line covers PC and standalone headsets.",K,["HTC Vive","HTC Vive Cosmos","HTC Vive Focus"],["Valve"]),
 B("Valve","United States","1996","Premium","Index, Steam","Game company and Steam store owner that makes the Index headset and Lighthouse tracking.",K,["Valve Index"],["HTC"]),
 B("Sony","Japan","1946","Mainstream","PlayStation","Japanese electronics group behind PlayStation and its VR headsets.",K,["PlayStation VR"]),
 B("Apple","United States","1976","Premium","Vision Pro","Maker of the Vision Pro spatial computer.",K,["Apple Vision Pro"]),
 B("Samsung","South Korea","1938","Mainstream","Galaxy, Gear VR","Korean electronics group behind Gear VR, Odyssey and Galaxy XR headsets.",K,["Samsung Gear VR","Samsung Galaxy XR"]),
 B("Google","United States","1998","Mainstream","Cardboard, Daydream","Maker of the Cardboard and Daydream phone VR platforms.",K,["Google Cardboard","Google Daydream View"]),
 B("Pico","China","","Mainstream","standalone headsets","Pico Immersive, ByteDance's VR division.",W+"PICO_4",["Pico 4"]),
 B("Pimax","China","2015","Specialist","wide-FOV headsets","Shanghai maker of high-resolution wide-field-of-view headsets.",W+"Pimax",["Pimax wide-FOV headsets"]),
 B("Bigscreen","United States","","Specialist","ultralight headsets","Bigscreen VR, maker of the custom-fitted Beyond headset.",W+"Bigscreen_Beyond",["Bigscreen Beyond"]),
 B("Xreal","China","","Specialist","display glasses","Maker of the Air and One display glasses, formerly Nreal.",MX,["Xreal Air and One"]),
 B("Viture","","","Specialist","display glasses","Maker of the One and Pro XR display glasses.",PA,["Viture Pro XR"]),
 B("Rokid","China","","Specialist","display glasses","Maker of the Max display glasses.",AC,["Rokid Max"])]

w('E5','05_00',{"kinds":[sa,te,ph,xg],"brands":br,"traditions":[],
 "notes":"Standalone: 29 models -> 5 archetypes (Quest, Vision Pro, Galaxy XR, Vive Focus, Pico 4) + 13 models; dropped Lenovo ThinkReality VRX (enterprise) and maker-less Woxter Neo VR100. Tethered: 53 models -> 8 archetypes (Rift, Vive, Vive Cosmos, Index, PlayStation VR, Pimax, Bigscreen Beyond, Windows Mixed Reality) + 9 models; enterprise-only Varjo VR-1/VR-2/VR-3/XR-1/XR-3/XR-4, StarVR One, VRgineers VRHero 5K and XTAL 3 dropped to kind level by the scope rule (Varjo Aero kept as the consumer model); XEO BIG dropped (no page). Phone viewer: 3 archetypes + 5 models; Pasonomi dropped as no-name. New kind XR display glasses (Xreal, Viture, Rokid, RayNeo). Rokid Max original not separately attested (only Max 2)."})
