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
N='Nintendo'; G='Sega'; S='Sony'; M='Microsoft'; K='Konami'; NA='Namco'
LG=W+'Light_gun'; RH='https://retrohandhelds.gg/a-brief-look-at-the-gun4ir-light-gun/'
gun={"n":"Light gun","a":"lightgun · gun controller","d":"Gun-shaped pointing controller aimed at the screen to shoot.",
 "t":["CRT light-sensing gun","infrared-sensor gun","camera-based gun","gun shell for a motion controller"],"s":LG,"x":[
 X("Nintendo Zapper","Kōsenjū · Video Shooting Series light gun","Nintendo's revolver-style light gun with a light sensor in the barrel, first for the Famicom.",N,"1984",W+"NES_Zapper",
   [("Famicom Video Shooting Series light gun",N,"1984","Japan; designed by Gunpei Yokoi and Satoru Okada"),("NES Zapper (grey)",N,"1985","North America; Lance Barr redesign"),("NES Zapper (orange)",N,"1989","recoloured after the 1988 US toy-gun law")],"grey or orange"),
 X("Sega Light Phaser","","Sega's light gun for the Master System; the Menacer succeeded it.",G,"1986",LG,[("Sega Light Phaser",G,"1986","")]),
 X("Super Scope","Nintendo Scope","Wireless bazooka-style light gun for the Super NES with an infrared receiver on top of the TV; CRT only.",N,"1992",W+"Super_Scope",
   [("Super Scope",N,"1992","North America; Japan 1993"),("Nintendo Scope",N,"1993","Europe; orange fire button")],"six AA batteries"),
 X("Menacer","","Sega's infrared light gun for the Genesis and Sega CD, built from a pistol, binocular sight and shoulder stock.",G,"1992",W+"Menacer",
   [("Menacer",G,"1992","Genesis / Mega Drive and Sega CD")],"three detachable modules"),
 X("Konami Justifier","The Justifier · Hyper Blaster","Konami's revolver-shaped light gun modelled on its arcade cabinets; a pink second gun daisy-chains to the blue one.",K,"1993",W+"Konami_Justifier",
   [("The Justifier (Genesis / Mega Drive)",K,"1993","blue; pink second gun"),("Justifier (Super NES)",K,"1993","blue; pink second gun"),("Justifier Model 510 (Super Famicom)",K,"",""),("Hyper Blaster (PlayStation)",K,"","green; black in Japan")],"blue or pink"),
 X("GunCon","G-Con","Namco's light gun line for PlayStation consoles, from video-synced CRT guns to an infrared gun for flat screens.",NA,"1997",W+"GunCon",
   [("GunCon (NPC-103)",NA,"1997","PlayStation; G-Con 45 in Europe; CRT only"),("GunCon 2 (NPC-106)",NA,"2001","PlayStation 2; USB; G-Con 2 in Europe; CRT only"),("GunCon 3 (NC-109)",NA,"2007","PlayStation 3; infrared LED markers; works with flat screens")]),
 X("Sinden Lightgun","Sinden Light Gun","Camera-based light gun that finds the screen outline, needing a white border, so it works on flat screens.","Sinden","2019",RH,
   [("Sinden Lightgun","Sinden","2019","crowdfunded on Indiegogo")]),
 X("GUN4IR","GUN4IR Lightguns","Infrared light-gun system using four IR LED clusters around the screen; sold as a kit, a licence or pre-built guns.","GUN4IR","2019",RH,
   [("GUN4IR pre-built gun","GUN4IR","","official pre-build sellers")],"recoil solenoid · rumble · pedal")],
 "m":[["Wii Zapper",N],["Sega Stunner",G],["Saturn Virtua Gun",G],["Sega Dreamcast Gun",G],["Odyssey Shooting Gallery","Magnavox"],["Atari XG-1","Atari"],["3DO Game Gun","The 3DO Company"],["Peacekeeper Revolver","Philips"],["Action Max light gun","Worlds of Wonder"],["Konami LaserScope",K],["PlayStation VR Aim Controller",S],["EMS Topgun","EMS"],["EMS Topgun II","EMS"],["Nintendo Beam Gun",N],["Nintendo Laser Clay Shooting System",N],["Atari Qwak!","Atari"],["ASCII Plus-X Terminator Laser","ASCII Corporation"],["MoProUsa Integrated Pistol","MoProUsa"],["PDP MARS LightGun","PDP"],["Pelican Pulse Cannon","Pelican (game accessories)"]]}
mot={"n":"Motion controller","a":"motion wand","d":"Controller that senses its own movement in the player's hand.","t":["wand","glove","clip-on attachment","fitness accessory"],
 "s":"https://en.wikipedia.org/wiki/List_of_game_controllers","x":[
 X("Power Glove","","Glove controller for the NES with finger-flex sensors and forearm keypad, a simplified VPL DataGlove.","Mattel","1989",W+"Power_Glove",
   [("Power Glove","Mattel","1989","United States"),("Power Glove","PAX","","Japan")]),
 X("Wii Remote","Wiimote","Nintendo's one-handed motion controller with accelerometer and infrared pointer, extended by the Nunchuk and MotionPlus.",N,"2006",W+"Wii_Remote",
   [("Wii Remote (RVL-003)",N,"2006","white at launch; black, blue, pink later"),("Nunchuk (RVL-004)",N,"2006","analog stick and accelerometer"),("Wii MotionPlus",N,"2009","gyroscope add-on"),("Wii Remote Plus (RVL-036)",N,"2010","MotionPlus built in; reissued for Wii U 2012")],"colours · Wii Remote Jacket sleeve"),
 X("PlayStation Move","Move motion controller","Sony wand with a glowing ball tracked by camera plus inertial sensors, later used with PlayStation VR.",S,"2010",W+"PlayStation_Move",
   [("PlayStation Move motion controller",S,"2010","Mini USB"),("PlayStation Move navigation controller",S,"2010","one-handed, no motion sensing"),("PlayStation Move Sharp Shooter (CECHYA-ZRA1E)",S,"","rifle-style holder"),("PlayStation Move CECH-ZCM2",S,"2017","Micro USB, larger battery; not for PS3")]),
 X("Ring-Con","Ring Fit Ring-Con","Bendable resistance ring holding a Joy-Con, sold with a Joy-Con Leg Strap for fitness play.",N,"2019","https://www.imore.com/nintendo-announces-new-ring-con-fitness-accessory-nintendo-switch",
   [("Ring-Con",N,"2019",""),("Leg Strap",N,"2019","holds the second Joy-Con")])],
 "m":[["Poke Ball Plus",N],["Sega Activator",G],["Nyko Wii Wand+","Nyko"],["PlayStation VR2 Sense Controller",S]]}
cam={"n":"Console camera","a":"","d":"Camera made to track the player as game input.","t":["colour camera","depth camera"],"s":W+"Kinect","x":[
 X("EyeToy and PlayStation Eye","PlayStation Camera","Sony's line of player-tracking cameras from the PlayStation 2 EyeToy onward.",S,"2003",W+"EyeToy",
   [("EyeToy",S,"2003","PlayStation 2; made by Logitech, later Namtai"),("PlayStation Eye",S,"","PlayStation 3"),("PlayStation Camera",S,"","PlayStation 4")]),
 X("Kinect","","Microsoft's depth camera for full-body tracking without a controller.",M,"2010",W+"Kinect",
   [("Kinect for Xbox 360",M,"2010","structured light (PrimeSense)"),("Kinect for Windows",M,"2012",""),("Kinect for Xbox One",M,"2013","time-of-flight"),("Kinect 2 for Windows",M,"2014",""),("Azure Kinect",M,"2019","developer kit")])],
 "m":[["Xbox Live Vision",M],["Dreameye",G],["Nintendo Switch 2 Camera",N]]}
mouse={"n":"Console mouse","a":"","d":"Mouse or trackball made to plug into one console as pointing input. A mouse with a standard connector sold for computers is in Computers & Components.",
 "s":"https://en.wikipedia.org/wiki/List_of_Super_Nintendo_Entertainment_System_accessories","m":[["Super NES Mouse",N],["Nintendo 64 Mouse","Mitsumi"],["Dreamcast Mouse",G]]}
pad={"n":"Paddle or spinner controller","a":"paddle · spinner · Vaus type","d":"Controller with a rotary knob whose turn sets a position on screen.","t":["potentiometer paddle (absolute)","spinner or driving controller (relative)"],"s":W+"Paddle_(game_controller)","x":[
 X("Atari paddle","Atari paddles","Pair of potentiometer knob controllers sharing one Atari 2600 port; the driving controller is a free-spinning relative version.","Atari","",W+"Paddle_(game_controller)",
   [("Atari CX-30 Paddle","Atari","","pair"),("Atari driving controller","Atari","1977","relative-position spinner")]),
 X("Arkanoid Vaus controller","Arkanoid controller","Knob-and-button paddle controller sold with Arkanoid for the NES and Famicom.","","",'https://www.nesdev.org/wiki/Arkanoid_controller',
   [("Arkanoid controller (NES)","","",""),("Arkanoid controller (Famicom)","","",""),("Arkanoid II controller (Famicom)","","","expansion port for a second controller")])],
 "m":[["Magnavox Odyssey paddles","Magnavox"],["Sony PlayStation paddle controller",S],["Nintendo DS paddle controller",""]]}
br=[B(N,"Japan","1889","Mainstream","consoles","Japanese console maker; Zapper, Super Scope, Wii Remote and Ring-Con.","knowledge",["Nintendo Zapper","Super Scope","Wii Remote","Ring-Con"]),
 B(G,"Japan","1960","Mainstream","consoles","Japanese game company; Light Phaser and Menacer guns.","knowledge",["Sega Light Phaser","Menacer"]),
 B(S,"Japan","1946","Mainstream","consoles","Japanese electronics group; PlayStation Move and EyeToy cameras.","knowledge",["PlayStation Move","EyeToy and PlayStation Eye"]),
 B(M,"United States","1975","Mainstream","consoles","US software company; Xbox and the Kinect camera.","knowledge",["Kinect"]),
 B("Atari","United States","1972","Mainstream","consoles","Video-game pioneer; 2600 paddle and driving controllers.","knowledge",["Atari paddle"]),
 B("Mattel","United States","1945","Mainstream","toys","Toy company that sold the Power Glove in the US.","knowledge",["Power Glove"]),
 B(K,"Japan","1969","Mainstream","games","Japanese game publisher; made the Justifier light gun.","knowledge",["Konami Justifier"]),
 B(NA,"Japan","1955","Mainstream","arcade games","Japanese arcade and game company; made the GunCon light guns.","knowledge",["GunCon"],["Bandai Namco"]),
 B("Sinden","United Kingdom","2019","Artisan & independent","flat-screen light guns","UK developer of a camera-based light gun first crowdfunded on Indiegogo.",RH,["Sinden Lightgun"]),
 B("GUN4IR","France","","Artisan & independent","DIY IR light guns","Infrared light-gun system by French developer Jean-Baptiste Bongrand, sold as kits and pre-built guns.",RH,["GUN4IR"])]
w('E5','02_03',{"kinds":[gun,mot,cam,mouse,pad],"brands":br,"traditions":[],
 "notes":"All five old kinds kept. Light gun: 34 models grouped into 8 archetypes (Zapper, Light Phaser, Super Scope, Menacer, Justifier incl. Hyper Blaster, GunCon 1-3, Sinden, GUN4IR); duplicate 'Hyper Blaster / Justifier' merged; rest kept in m; dropped maker-less Magnum Light Phaser and Retro Shooter Lightguns and the minor third-party Dominator Pro Beam to stay within 20 flat models. Motion: Power Glove, Wii Remote (Nunchuk, MotionPlus, Plus), PlayStation Move, Ring-Con. Camera: EyeToy line and Kinect. Mouse unchanged (3 models). Paddle: Atari paddle and Arkanoid Vaus archetypes (Vaus maker not stated on retrieved page, left blank); old retailer source replaced by the Wikipedia paddle article. No Sega Light Phaser or Dreamcast-gun page fetched beyond the Light gun article; Virtua Gun/Stunner left as separate old entries."})
