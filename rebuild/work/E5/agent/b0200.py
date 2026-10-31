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
N='Nintendo'; S='Sony'; M='Microsoft'; G='Sega'; GP=W+'Gamepad'; AC=W+'Arcade_controller'; DS=W+'DualShock'
pad={"n":"Gamepad","a":"joypad · controller","d":"Hand-held controller with a directional pad, buttons and sticks or triggers, held in both hands.",
 "t":["wired","wireless","pro controller with back paddles","accessible controller"],"s":"https://en.wikipedia.org/wiki/List_of_game_controllers","x":[
 X("NES controller","Famicom controller","Nintendo's rectangular pad that brought the D-pad from Game & Watch to home consoles.",N,"",GP,
   [("NES / Famicom controller",N,"","original pad")]),
 X("Super NES controller","Super Famicom controller","Nintendo pad with four face buttons in a diamond and two shoulder buttons, the layout most modern pads follow.",N,"",GP,
   [("Super NES controller",N,"","original"),("Super Nintendo Classic Mini controller",N,"","mini-console reissue")]),
 X("Mega Drive and Genesis control pad","Genesis controller","Sega's pad with three face buttons, later a six-button version.",G,"",GP,
   [("Genesis controller",G,"","three-button"),("Genesis 6-Button Arcade Pad",G,"","six-button")]),
 X("Nintendo 64 controller","N64 pad","M-shaped pad with a control stick and a rear slot for Controller, Rumble and Transfer Paks.",N,"1996",W+"Nintendo_64_controller",
   [("Nintendo 64 controller",N,"1996","original"),("Nintendo 64 controller for Nintendo Switch",N,"2021","wireless replica with built-in rumble")]),
 X("PlayStation controller to DualSense","DualShock · DualSense","Sony's pad lineage, from the 1994 PlayStation pad through twin sticks and rumble to the DualSense.",S,"1994",DS,
   [("PlayStation controller",S,"1994","digital, no sticks"),("Dual Analog Controller",S,"","twin sticks, Japan first"),("DualShock",S,"1997","sticks and rumble"),
    ("DualShock 2",S,"2000","PlayStation 2"),("Sixaxis",S,"","motion sensing, no rumble"),("DualShock 3",S,"2007","rumble restored"),
    ("DualShock 4",S,"2013","touchpad and light bar; CUH-ZCT2 revision 2016"),("DualSense",S,"2020","haptics and adaptive triggers"),("DualSense Edge",S,"2023","pro controller with swappable sticks")],"colourway · special edition"),
 X("GameCube controller","WaveBird","Nintendo's GameCube pad, still sold and adapted for later consoles.",N,"2001",W+"GameCube_controller",
   [("GameCube controller",N,"2001","wired"),("WaveBird Wireless Controller",N,"2002","wireless"),("Wii U GameCube adapter",N,"2014","lets the pad work on Wii U"),("Switch 2 wireless GameCube controller",N,"2025","for Nintendo Switch Online")],"colour"),
 X("Xbox controller","The Duke · Controller S","Microsoft's first Xbox pad: the large Duke, then the smaller Japan-designed Controller S.",M,"2001",W+"Xbox_controller",
   [("Xbox controller (The Duke)",M,"2001","original"),("Xbox Controller S",M,"2002","smaller redesign; replaced the Duke by 2003"),("Duke re-release","Hyperkin","2018","for Xbox One and PC")]),
 X("Xbox 360 controller","","Microsoft's Xbox 360 pad in wired and wireless forms.",M,"2005",W+"Xbox_360_controller",
   [("Xbox 360 wired controller",M,"2005","USB"),("Xbox 360 wireless controller",M,"2005","2.4 GHz, AA or Play & Charge pack"),("Transforming D-pad controller",M,"2010","rotating plus/disc D-pad")]),
 X("Xbox Wireless Controller","Xbox One controller · Elite","Microsoft's pad for Xbox One and Series X|S, with Elite pro versions.",M,"2013",W+"Xbox_Wireless_Controller",
   [("Model 1537",M,"2013","Xbox One launch"),("Model 1697",M,"2015","3.5 mm headset jack"),("Model 1708",M,"2016","Bluetooth"),("Model 1914 (Series X|S)",M,"2020","share button"),
    ("Elite (model 1698)",M,"2015","paddles, swappable parts"),("Elite Series 2 (model 1797)",M,"2019","")],"colourway · special edition"),
 X("Xbox Adaptive Controller","","Microsoft controller for players with disabilities, with large buttons and 19 jacks for assistive switches.",M,"2018",W+"Xbox_Adaptive_Controller",[]),
 X("Access Controller","Project Leonardo","Sony's accessible PS5 controller with interchangeable buttons and jacks for extra devices.",S,"2023",W+"Xbox_Adaptive_Controller",[]),
 X("Steam Controller","","Valve's PC pad with two clickable haptic trackpads.","Valve","2015",W+"Steam_Controller_(1st_generation)",
   [("Steam Controller (1st generation)","Valve","2015","discontinued 2019"),("Steam Controller (2026)","Valve","2026","second generation, announced 2025")])],
 "m":[["Nintendo Switch Pro Controller",N],["Nintendo Switch 2 Pro Controller",N],["Wii U Pro Controller",N],["Wii Classic Controller Pro",N],["Wii U GamePad",N],
      ["Master System controller",G],["Saturn controller",G],["Saturn 3D Pad",G],["Dreamcast controller",G],
      ["8BitDo Pro 2","8BitDo"],["8BitDo Ultimate 2 Bluetooth","8BitDo"],["8BitDo SN30 Pro","8BitDo"],["8BitDo M30 Bluetooth","8BitDo"],
      ["GameSir G7 Pro","GameSir"],["Hori Split Pad Pro","Hori"],["Logitech Cordless Precision Controller","Logitech"],["Hyperkin Ranger GamePad with Paddle","Hyperkin"],
      ["Google Stadia Controller","Google"],["Amazon Luna Controller","Amazon"],["NES Max","Bullet-Proof Software"]]}
split={"n":"Detachable split controller","a":"Joy-Con","d":"Controller made as two detachable halves that can be used apart.","s":"https://en.wikipedia.org/wiki/List_of_game_controllers","x":[
 X("Joy-Con","","Nintendo's pair of detachable controllers that attach to the sides of the Switch.",N,"2017",W+"Joy-Con",
   [("Joy-Con",N,"2017","slide onto rails"),("Joy-Con 2",N,"2025","magnetic attachment, works as a mouse"),("Hori D-pad Joy-Con L","Hori","2018","licensed left unit with a D-pad, handheld mode only")],"colour pair")]}
stick={"n":"Arcade stick","a":"fight stick · levered arcade stick","d":"Arcade-style controller with a joystick lever and buttons.","t":["Japanese-style (Sanwa, Seimitsu parts)","American-style (Happ parts)","Vewlix layout","Noir layout"],"s":"https://www.hlj.com/nintendo-switch-real-arcade-pro-v-hayabusa-hrinsw-006","x":[
 X("NES Advantage","","Nintendo's desk-top stick, one of the earliest arcade imitations for a home console.",N,"",AC,[("NES Advantage",N,"","")]),
 X("Real Arcade Pro","RAP","Hori's long-running line of full-size arcade sticks.","Hori","",AC.replace(AC,"https://ubergizmo.com/2008/07/hori-real-arcade-pro-ex"),
   [("Real Arcade Pro EX","Hori","","Xbox 360, ball-top stick and eight buttons"),("Real Arcade Pro 3","Hori","",""),("Real Arcade Pro.V Hayabusa","Hori","","Switch, Hori Hayabusa parts")]),
 X("FightStick Tournament Edition","TE stick","Mad Catz stick line; the Street Fighter IV TE was the first North American console stick with genuine Sanwa parts.","Mad Catz","",AC,
   [("Street Fighter IV FightStick Tournament Edition","Mad Catz","","Sanwa parts")]),
 X("Qanba Obsidian","","Qanba's top stick line with Sanwa parts.","Qanba","",
   "https://thearcadestick.com/qanba-obsidian-2",[("Qanba Obsidian 2","Qanba","2023","Sony-licensed, Sanwa JLF and OBSF-30, Vewlix layout")]),
 X("Victrix Pro FS","","PDP's Victrix aluminium tournament stick with Sanwa parts and tool-free access.","PDP","",
   "https://www.thesixthaxis.com/2024/03/18/pdp-victrix-pro-fs-best-arcade-fight-stick-ps5-review/",[("Victrix Pro FS","PDP","","PS5, PS4 and PC; purple or white")])],
 "m":[["Hori Fighting Stick Alpha SF6 Edition","Hori"],["Qanba N3 Drone 2","Qanba"],["Saturn Virtua Stick",G],["Dreamcast Arcade Stick",G],["Arcade Power Stick II",G],
      ["Fighter Stick SN","ASCII Corporation"],["Super Advantage","ASCII Corporation"],["Mayflash F300","Mayflash"],["8BitDo 80FE Arcade Stick","8BitDo"],
      ["Speedking","Konix"],["Epyx 500XJ","Konix"],["Quickshot Arcade QS-128n","QuickShot"],["Zoomer","Beeshu, Inc."],["InterAct Alloy Arcade Stick","InterAct"]]}
lev={"n":"Leverless controller","a":"all-button controller · hitbox","d":"Arcade-style controller with all-button directional input and no lever.","t":["SOCD cleaning modes","mechanical switches","optical switches"],"s":AC,"x":[
 X("Hit Box","","The first commercial leverless controller; its name became the generic term.","Hit Box","",AC,
   [("Hit Box","Hit Box","","original layout with Up at the bottom"),("Smash Box","Hit Box","","layout for platform fighters")]),
 X("Razer Kitsune","","Razer's slim leverless controller with optical switches in the original Hit Box layout.","Razer","2023","https://lowyat.net/2024/317774/razer-kitsune-lightning-review",[])],
 "m":[["Turtle Beach Victrix Pro KO","Turtle Beach"],["Mixbox","Mixbox"],["8BitDo All-Button Arcade Controller","8BitDo"],["Haute42 M16 Plus","Haute42"],["Haute42 T16 Pro V2","Haute42"],
      ["Haute42 C16 Magnetic","Haute42"],["Qanba Sapphire S1","Qanba"],["Brook Fighter Starburst","Brook"],["Mayflash F500 FLAT","Mayflash"],["DOIO KBHX-01 Pro","DOIO"],["Sunga G1","Sunga"]]}
br=[B("Nintendo","Japan","1889","Mainstream","consoles","Japanese console maker; pads from the NES controller to Joy-Con.","knowledge",["Super NES controller","Joy-Con","GameCube controller"]),
 B("Sony","Japan","1946","Mainstream","consoles","Japanese electronics group; DualShock and DualSense pads.","knowledge",["PlayStation controller to DualSense"]),
 B("Microsoft","United States","1975","Mainstream","consoles","US software company; Xbox pads including Elite and Adaptive.","knowledge",["Xbox Wireless Controller","Xbox Adaptive Controller"]),
 B("Sega","Japan","1960","Mainstream","consoles","Japanese game company; Mega Drive and Saturn pads.","knowledge",["Mega Drive and Genesis control pad"]),
 B("Valve","United States","1996","Premium","PC gaming","PC game company behind Steam and the Steam Controller.","knowledge",["Steam Controller"]),
 B("Hori","Japan","1970","Specialist","licensed controllers","Yokohama maker of licensed pads, sticks and wheels, founded as Hori Electric.",W+"Hori_(company)",["Real Arcade Pro"]),
 B("Mad Catz","","","Mainstream","fight sticks","Accessory maker of the FightStick Tournament Edition line.","knowledge",["FightStick Tournament Edition"]),
 B("Qanba","","","Specialist","fight sticks","Arcade-stick maker of the Obsidian and Drone lines.","https://thearcadestick.com/qanba-obsidian-2",["Qanba Obsidian"]),
 B("PDP","United States","","Mainstream","licensed controllers","Accessory maker whose Victrix brand makes premium fight sticks; part of Turtle Beach.","knowledge",["Victrix Pro FS"],["Turtle Beach"]),
 B("Hit Box","","","Artisan & independent","leverless controllers","Maker of the first commercial leverless controllers.",AC,["Hit Box"]),
 B("Razer","","","Premium","gaming peripherals","Gaming-peripheral brand; makes the Kitsune leverless controller.","knowledge",["Razer Kitsune"]),
 B("8BitDo","China","2013","Value","retro-style controllers","Shenzhen maker of retro-styled pads and sticks.",W+"8BitDo")]
w('E5','02_00',{"kinds":[pad,split,stick,lev],"brands":br,"traditions":[],
 "notes":"Gamepad: 69 flat models turned into 12 first-party archetypes (lineage versions) plus 20 market models; dropped minor/obscure third-party pads (Acclaim, Bandai Super Controller, Camerica, EasySMX, Gravis, Innovation, JAMJAKE, iPega, Triax, Ouya, Virtual Boy pad, Xbox Nano, maker-less Afterglow/Total Control 3/SNProPad, older 8BitDo and GameSir variants). Switch Pro Controllers kept in m (no page fetched). Arcade stick 32 to 5 archetypes + 14 models; dropped Beeshu duplicates, Agetec, Camerica, Multicorp, Toyo, Mad Catz Xbox 360 GameStick. Leverless 23 to 2 archetypes + 11 (Haute42 cut to 3, DOIO to 1, LBER dropped). Victrix Pro KO kept as old 'Turtle Beach' entry (PDP is Turtle Beach's brand); no Snack Box or Haute42 page fetched."})
