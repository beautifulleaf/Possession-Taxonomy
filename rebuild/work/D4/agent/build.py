import json,os
K=[
{"n":"Action camera","a":"sports camera · helmet camera","d":"Small rugged camera made to be mounted on a person, helmet, bike or vehicle for video.",
 "t":["waterproof body","modular","entry-level"],
 "s":"https://gopro.com/en/us/shop/cameras/learn/hero13black/CHDHX-131-master.html",
 "m":[["HERO13 Black","GoPro"],["HERO12 Black","GoPro"],["HERO (2024)","GoPro"],["Osmo Action 6","DJI"],["Osmo Action 5 Pro","DJI"],["Ace Pro","Insta360"]],
 "r":[["HERO","GoPro"],["Osmo Action","DJI"],["Ace","Insta360"]]},
{"n":"360-degree camera","a":"360 camera · spherical camera","d":"Camera with two or more lenses that records a full spherical view.",
 "s":"https://store.insta360.com/product/x4",
 "m":[["X5","Insta360"],["X6","Insta360"],["X4","Insta360"],["X4 Air","Insta360"],["X3","Insta360"],["ONE RS 1-Inch 360","Insta360"],["MAX 2","GoPro"],["Theta X","Ricoh"],["Theta Z1","Ricoh"]],
 "r":[["X series","Insta360"],["MAX","GoPro"],["Theta","Ricoh"]]},
{"n":"Pocket gimbal camera","a":"gimbal camera","d":"Small handheld device with a camera fixed to a built-in motorised stabilising gimbal.",
 "s":"https://store.dji.com/product/osmo-pocket-3",
 "m":[["Osmo Pocket 3","DJI"],["Pocket 4","DJI"],["Pocket 2","DJI"]],"r":[["Osmo Pocket","DJI"]]},
{"n":"Camcorder","a":"video camera · handycam","d":"Handheld camera built mainly to record video for long takes, with a fixed built-in zoom lens.",
 "t":["4K","Full HD","built-in projector","tape (vintage: Video8, Hi8, MiniDV)","DVD or hard disk (vintage)"],
 "s":"https://www.cameraworld.co.uk/sony-ax43-4k-handycam-4548.html",
 "m":[["HDR-CX405","Sony"],["FDR-AX43A","Sony"],["FDR-AX53","Sony"],["HC-V770","Panasonic"],["HC-V180K","Panasonic"],["Vixia HF R800","Canon"],["VIXIA HF G70","Canon"]],
 "r":[["Handycam","Sony"]]},
{"n":"Camera drone","a":"drone · quadcopter","d":"Unmanned aircraft made for filming, carrying a stabilised camera.",
 "t":["sub-250 g","folding","FPV"],
 "s":"https://store.dji.com/product/dji-mini-4-pro",
 "m":[["Mini 4 Pro","DJI"],["Air 3","DJI"],["Mavic 4 Pro","DJI"],["Mavic 3 Pro","DJI"],["Air 2S","DJI"]],
 "r":[["Mini","DJI"],["Air","DJI"],["Mavic","DJI"],["Phantom","DJI"]]},
{"n":"Trail camera","a":"camera trap · game camera","d":"Weatherproof camera left outdoors and triggered by motion, mainly to film wildlife.",
 "t":["cellular","standard (SD card)","solar panel","no-glow infrared flash"],
 "s":"https://www.nhbs.com/1/trail-cameras",
 "m":[["REVEAL Pro 4.0 Solar","Tactacam"],["Reveal Pro 4.0","Tactacam"],["Reveal X 4.0","Tactacam"],["Fusion Max 3","Stealth Cam"],["Spectre 4K Pro","Stealth Cam"],["Hyperfire 2 Cellular","Reconyx"],["HyperFire 4k Surveillance LPC","Reconyx"],["Spec Ops Elite HP5","Browning"],["Dark Ops Pro X 1080","Browning"],["GoLive 2","Spartan Camera"],["Terra Cell XT 3.0","Wildgame Innovations"],["Trifecta 180","Muddy"]],
 "r":[["Reveal","Tactacam"],["Trail Cameras (Dark Ops, Spec Ops, Defender)","Browning"]]},
]
B=[
{"n":"GoPro","c":"United States","f":"2002","seg":"Action cameras","d":"American maker of the HERO action cameras and MAX 360-degree cameras, founded by Nick Woodman.","lines":["HERO","MAX"],"rel":["DJI","Insta360"],"s":"https://en.wikipedia.org/wiki/GoPro"},
{"n":"DJI","c":"China","f":"2006","seg":"Drones, gimbals and action cameras","d":"Shenzhen maker of consumer camera drones, Osmo Action cameras and Osmo Pocket gimbal cameras.","lines":["Mavic","Mini","Air","Phantom","Osmo Action","Osmo Pocket"],"rel":["GoPro","Insta360"],"s":"https://en.wikipedia.org/wiki/DJI"},
{"n":"Insta360","c":"China","f":"2015","seg":"360-degree and action cameras","d":"Shenzhen maker of X-series 360-degree cameras, Ace action cameras and GO small cameras.","lines":["X series","ONE","Ace","GO"],"rel":["GoPro","DJI"],"s":"https://en.wikipedia.org/wiki/Insta360"},
{"n":"Sony","c":"Japan","seg":"Consumer electronics","d":"Japanese electronics maker whose Handycam camcorder line dates from 1985.","lines":["Handycam"],"s":"https://en.wikipedia.org/wiki/Handycam"},
{"n":"Panasonic","c":"Japan","f":"1918","seg":"Consumer electronics","d":"Japanese electronics maker of camcorders and Lumix cameras, based in Kadoma, Osaka.","lines":["Lumix"],"s":"https://en.wikipedia.org/wiki/Panasonic"},
{"n":"Canon","c":"Japan","seg":"Cameras and imaging","d":"Japanese camera and imaging maker; its consumer camcorders are sold as Vixia (Legria in Europe).","lines":["Vixia"],"s":"knowledge"},
{"n":"Ricoh","c":"Japan","seg":"Cameras and imaging","d":"Japanese imaging maker whose Theta 360-degree cameras date from 2013.","lines":["Theta"],"s":"https://en.wikipedia.org/wiki/Ricoh_Theta"},
{"n":"Tactacam","seg":"Hunting cameras","d":"American maker of Reveal cellular trail cameras, top pick in Outdoor Life's tests.","lines":["Reveal"],"s":"https://www.outdoorlife.com/gear/best-trail-cameras-2026/"},
{"n":"Reconyx","c":"United States","seg":"Trail and research cameras","d":"American maker of HyperFire trail cameras, made in the USA.","lines":["HyperFire"],"s":"https://www.outdoorlife.com/gear/best-trail-cameras-2026/"},
{"n":"Stealth Cam","seg":"Trail cameras","d":"Trail camera maker; its Fusion Max 3 was Outdoor Life's best-value cellular camera.","lines":["Fusion","Spectre"],"s":"https://www.outdoorlife.com/gear/best-trail-cameras-2026/"},
]
notes=("Tier shelf, no archetypes. Trimmed old SKU lists to current market-covering models plus test winners (Outdoor Life trail-camera tests; ReviewFinder camcorder meta-ranking). "
 "Dropped discontinued Sony DCR-SR50/SR90, HDR-SR10E, HDR-CX625, HDR-PJ410 (projector kept as a type); Insta360 X2; GoPro HERO12 kept as previous generation; trail models Defender Pro Scout Max, GoCam 2 M, GoLive 3 M (replaced by tested GoLive 2), Orbit 360, Yellowstone.ai Y2 (no test or reference evidence). "
 "Bushnell named in brief but no Bushnell model found on a retrieved page, so left out; Browning, Spartan, Wildgame Innovations, Muddy have no brand entries (facts not retrieved). Pro VR cameras (Insta360 Titan/Pro), Phantom 4 RTK survey drone and cinema cameras out of scope. Tactacam and Stealth Cam entries carry no country or founding year (not confirmed on a retrieved page).")
out={"kinds":K,"brands":B,"traditions":[],"notes":notes}
p='work/D4/shelves/00_02.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
