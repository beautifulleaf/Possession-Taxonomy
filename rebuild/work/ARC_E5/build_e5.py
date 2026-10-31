import json,sys,copy,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from data_new import *
SRC='/home/user/Possession-Taxonomy/rebuild/work/ARC_E5/bak/E5.json'
OUT='/home/user/Possession-Taxonomy/rebuild/out/E5.json'
d=json.load(open(SRC))
dp=[x for x in d['depts'] if x['n']=='Consoles & handhelds'][0]
K={k['n']:k for s in dp['s'] for k in s['k']}
OLD={n:{x['n']:x for x in k.get('x',[])} for n,k in K.items()}
def new(n,mk,y,g,a,desc,s,v=None,role=None,dt=None):
    x={"n":n,"mk":mk,"y":y,"g":g}
    if role:x["role"]=role
    if a:x["a"]=a
    x["d"]=desc; x["s"]=s
    x["v"]=v or []
    if dt:x["dt"]=dt
    return x
def keep(kind,name,g,role=None,**ch):
    x=copy.deepcopy(OLD[kind][name]); x["g"]=g
    if role:x["role"]=role
    for k,v in ch.items(): x[k]=v
    # order keys
    return x
def vv(*items): return [{"n":n,"y":y,"d":dsc} for n,y,dsc in items]
def finish(kind,xs,nl,sel,xg,order):
    k=K[kind]
    xs.sort(key=order)
    k['x']=xs; k['nl']=nl; k['sel']=sel; k['xg']=xg
    k.pop('m',None); k.pop('r',None)
report={}
# ---------- Home console
H=[]
roles={"Fairchild Channel F":"origin","Atari 2600":"landmark","Nintendo Entertainment System":"landmark","Super Nintendo Entertainment System":"landmark","PlayStation":"landmark","PlayStation 2":"landmark","Wii":"landmark"}
ren={"APF-M1000":("APF-MP1000","1978"),"Master System":("Master System",None)}
for n,x in OLD["Home console"].items():
    if n=="APF-M1000":
        x=copy.deepcopy(x); x["n"]="APF-MP1000"; x["y"]="1978"; x["a"]=(x.get("a","")+" · APF-M1000").strip(" ·")
        y=1978
    else:
        x=copy.deepcopy(x)
    if n=="Master System": x["a"]=(x.get("a","")+" · Sega Mark III").strip(" ·")
    y=int(x["y"]); g=gen(y); x["g"]=GEN[g]
    if x["n"] in roles: x["role"]=roles[x["n"]]
    H.append((g,x))
for n,mk,y,go,a,desc in HOME_NEW:
    g=go or gen(y)
    H.append((g,new(n,mk,y,GEN[g],a,desc,LH)))
Hx=[]
for g,x in H: Hx.append(x)
def gkey(x):
    gi=[i for i,v in GEN.items() if v==x['g']][0]
    return (gi,int(x['y']) if x.get('y') else 9999,x['n'])
finish("Home console",Hx,
 "One entry is a distinct home video game console platform sold under its own name; regional names are aliases and slim or redesigned models are versions.",
 "Every released home console from the second generation onward in Wikipedia's List of home video game consoles, grouped by the generation ranges in Home video game console generations (placed by release year); add-ons such as the Sega CD and 32X are under Console add-ons, hybrids under Hybrid console, first-generation dedicated consoles under Plug-and-play.",
 "by console generation",gkey)
# ---------- Microconsole
M=[]
A="Android-based";O="Other systems"
for n,mk,y,g,a,desc in [
("OnLive MicroConsole","OnLive","2010",O,"","Small box for streaming cloud games from the OnLive service."),
("Ouya","Ouya Inc.","2013",A,"","Crowdfunded Android-based microconsole sold with a gamepad."),
("GameStick","PlayJam","2013",A,"","Stick-sized Android microconsole with a bundled controller."),
("GamePop","BlueStacks","2013",A,"","Subscription Android microconsole from BlueStacks."),
("Mad Catz MOJO","Mad Catz","2013",A,"","Android microconsole from Mad Catz."),
("PlayStation TV","Sony","2013",O,"Vita TV","Sony set-top unit that plays PlayStation Vita games on a TV."),
("Fire TV","Amazon","2014",A,"Amazon Fire TV","Amazon's streaming box with a gaming controller option."),
("Nexus Player","Google","2014",A,"","Google's Android TV streaming box with game support."),
("Apple TV (tvOS)","Apple","2015",O,"","Apple's set-top box running tvOS games."),
("Razer ForgeTV","Razer","2015",A,"","Razer's Android TV microconsole."),
("Nvidia Shield TV","Nvidia","2015",A,"","Nvidia's Android TV box aimed at games."),
("Chromecast Ultra","Google","2020",O,"","Google's streaming dongle listed on the microconsole page.")]:
    if n in OLD["Microconsole"]:
        x=keep("Microconsole",n,g); x["s"]=MC
        if not x.get("mk"):x["mk"]=mk
        M.append(x)
    else: M.append(new(n,mk,y,g,a,desc,MC))
for x in M:
    if x["n"]=="Fire TV": x["mk"]="Amazon"
def mkey(x): return (0 if x['g']==A else 1,int(x['y']),x['n'])
finish("Microconsole",M,
 "One entry is a distinct microconsole product, a small low-cost set-top unit sold under its own name; hardware revisions are versions.",
 "Every microconsole named on Wikipedia's Microconsole page except the iQue Player (a plug-and-play N64 controller, left under Plug-and-play); grouped by the page's own split between Android-based units and the exceptions.",
 "by operating system",mkey)
# ---------- FPGA & clone
F=[]
Fp="FPGA";Fc="Clone chip or emulation"
F.append(keep("FPGA & clone console","MiSTer",Fp,d="Open-source FPGA platform that re-creates many consoles and computers in hardware."))
F.append(new("Analogue FPGA consoles","Analogue","2009",Fp,"Analogue CMVS · Gencore","Analogue's line of FPGA consoles that play original cartridges and discs.",LR,
 vv(("Analogue CMVS / Genesis Gencore","2009","first Analogue console, per the retro-style list"),("Analogue Neo","2012","Neo Geo cartridge console"),("Analogue Nt","2014","NES cartridge console"),("Super Nt","2017","SNES cartridge console"),("Mega Sg","2018","Mega Drive cartridge console"),("Analogue Duo","","PC Engine console"),("Analogue 3D","","N64 cartridge console"),("Legends Core","2019","AtGames-listed core")),
 dt="platform emulated"))
F[-1]["v"]=[v for v in F[-1]["v"] if v["n"]!="Legends Core"]
F.append(keep("FPGA & clone console","Polymega",Fc))
F.append(keep("FPGA & clone console","Super Retro Trio",Fc,v=vv(("Super Retro Trio","2014","three-system clone console"),("Super Retro Trio Plus","","updated model"),("Retro Duo","2008","two-system clone console, per the retro-style list"))))
F[-1]["n"]="Retro-Bit Retro Duo and Super Retro Trio"; F[-1]["a"]="Retro Duo · Super Retro Trio"; F[-1]["s"]=LR; F[-1]["y"]="2008"
F.append(new("Hyperkin RetroN line","Hyperkin","2011",Fc,"RetroN 2 · RetroN 5","Hyperkin's HD retro consoles that play original cartridges of older systems.",LR,
 vv(("RetroN 2","2011","two-system console"),("RetroN 5","2014","five-system HD console"),("RetroN 77","2017","Atari 2600 cartridge console"),("SupaRetroN HD","2018","SNES cartridge console"),("MegaRetroN HD","2018","Mega Drive cartridge console"),("RetroN 3 HD","2020","three-system console"),("RetroN Sq","2021","Game Boy-family HD console"))))
F.append(new("AtGames retro consoles","AtGames","2008",Fc,"Arcade Motion Classic · Genesis Flashback","AtGames' retro-style non-dedicated consoles for older cartridge systems.",LR,
 vv(("Arcade Motion Classic","2008","motion-controlled retro unit"),("Sega Genesis Classic Game Console","2015","licensed Genesis unit"),("Sega Genesis Flashback","2016","Genesis re-creation"),("Legends Core","2019","retro cartridge unit"))))
F.append(new("Atari VCS","Atari","2020",Fc,"","Atari's modern PC-based console with retro Atari games.",LR))
F.append(keep("FPGA & clone console","Atari 2600+",Fc,v=vv(("Atari 2600+","2023","plays original 2600 cartridges"),("Atari 7800+","2023","plays original 7800 cartridges"))))
F[-1]["s"]=OLD["FPGA & clone console"]["Atari 2600+"]["s"]
F.append(keep("FPGA & clone console","ModRetro M64",Fc))
F.append(new("Hyperkin SupaBoy","Hyperkin","2011",Fc,"SupaBoy Portable Pocket Console","Handheld clone that plays SNES cartridges.",LR,vv(("SupaBoy Portable Pocket Console","2011","original portable"),("SupaBoy S","",""),("SupaBoy SFC",""," Super Famicom version"))))
F[-1]["v"]=[v for v in F[-1]["v"] if v["d"]]
def fkey(x): return (0 if x['g']==Fp else 1,int(x['y']) if x.get('y') else 9999,x['n'])
finish("FPGA & clone console",F,
 "One entry is a product family or model line of retro-style non-dedicated hardware that plays original cartridges or discs of older systems; its individual models are versions.",
 "Every non-dedicated retro-style console family on Wikipedia's List of retro style video game consoles (Retro-Bit, Hyperkin, AtGames, Analogue, Polymega, Atari 2600+ and others) plus MiSTer from its own page; dedicated units are under Plug-and-play. Implementation per entry is from the entry's own page and should be verified.",
 "by implementation",fkey)
for x in F:
    if x["n"]=="Atari VCS": x["g"]=Fc
# ---------- Handheld console
def hg(y):
    y=int(y)
    for lim,g in((1982,2),(1986,3),(1992,4),(1997,5),(2003,6),(2010,7),(2019,8)):
        if y<=lim:return g
    return 9
HH=[]
HN=[("Entex Select-A-Game","Entex","1981","","Entex's cartridge handheld."),
("Entex Adventure Vision","Entex","1982","","Entex's LED cartridge handheld."),
("Palmtex Portable Videogame System","Palmtex","1984","","Early cartridge handheld listed on the Wikipedia handheld list."),
("Digi Casse","Bandai","1984","Bandai Digi Casse","Bandai's cassette-style handheld."),
("Epoch Game Pocket Computer","Epoch Co.","1984","","Epoch's cartridge handheld computer-game unit."),
("Etch A Sketch Animator 2000","Ohio Art","1988","","Handheld animation toy listed as a handheld console."),
("Gamate","Bit Corporation","1990","","Taiwanese cartridge handheld."),
("Game Master","Hartung","1990","","Cartridge handheld sold in Europe by Hartung."),
("Watara Supervision","Watara","1992","","Low-cost cartridge handheld."),
("Mega Duck","Welback Holdings","1993","","Cartridge handheld sold in Europe and Brazil."),
("Design Master Senshi Mangajukuu","Bandai","1995","Design Master Denshi Mangajuku","Bandai's manga-drawing handheld."),
("Cybiko","Cybiko","2000","","Handheld with wireless messaging and games."),
("GP32","Game Park","2001","","Korean open-style handheld with memory cards."),
("P/ECE","Aquaplus","2001","","Japanese hobbyist handheld."),
("GameKing","Timetop","2003","","Low-cost cartridge handheld."),
("Tapwave Zodiac","Tapwave","2003","","Palm OS handheld built for games."),
("Neo Geo X","Tommo","2012","","Retro-style handheld that connects to a TV."),
("Game Gadget","","2012","","Handheld listed on the Wikipedia handheld list."),
("Nvidia Shield Portable","Nvidia","2012","","Android handheld with built-in controls."),
("Arduboy","","2016","","Credit-card-sized open handheld for homemade games."),
("Thumby","TinyCircuits","2022","","Keychain-sized handheld that runs homemade games.")]
skip={"GP32"}
for n,mk,y,a,desc in HN:
    if n=="GP32": continue
    HH.append(new(n,mk,y,GEN[hg(y)],a,desc,LHH))
roleH={"Microvision":"origin","Game Boy":"landmark","Nintendo DS":"landmark"}
for n,x in OLD["Handheld console"].items():
    x=copy.deepcopy(x)
    if n=="Sega Nomad": x["y"]="1995"; x["a"]="Genesis Nomad"
    x["g"]=GEN[hg(x["y"])]
    if n in roleH: x["role"]=roleH[n]
    HH.append(x)
HH.append(new("GP32","Game Park","2001",GEN[6],"","Korean handheld with memory cards, listed on the handheld list.",LHH))
HH=[h for h in HH if h["n"]!="GP32"]  # GP32 stays a version of GP2X family (emulation handheld)
HH.append(new("Game Boy Advance","Nintendo","2001",GEN[6],"","","") ) if False else None
def hkey(x):
    gi=[i for i,v in GEN.items() if v==x['g']][0]
    return (gi,int(x['y']),x['n'])
finish("Handheld console",HH,
 "One entry is a distinct handheld console platform sold under its own name; colour, lighter or redesigned models are versions.",
 "Every handheld console in Wikipedia's List of handheld game consoles except handheld gaming PCs, hybrids and the Android or Linux homebrew devices (under their own kinds); placed in the generations of Home video game console generations by release year.",
 "by console generation",hkey)
# ---------- Hybrid
Y=[]
for n,x in OLD["Hybrid console"].items():
    x=copy.deepcopy(x); x["g"]=GEN[gen(x["y"])]; Y.append(x)
finish("Hybrid console",Y,
 "One entry is a distinct hybrid console platform that works docked to a TV and as a handheld; models like the Lite or OLED are versions.",
 "Both hybrids in Wikipedia's List of home video game consoles and List of handheld game consoles: the Nintendo Switch and Switch 2 (Steam Deck and ROG Ally are handheld PCs).",
 "by console generation",hkey)
# ---------- Handheld gaming PC
P=[]
mk_g=lambda m:m
P.append(keep("Handheld gaming PC","Steam Deck","Valve",s=LHH) if False else keep("Handheld gaming PC","Steam Deck","Valve"))
x=keep("Handheld gaming PC","ROG Ally","ASUS"); x["y"]="2023"; x["s"]=LHH; P.append(x)
P.append(keep("Handheld gaming PC","Legion Go","Lenovo"))
P.append(keep("Handheld gaming PC","GPD Win","GPD"))
P.append(new("Ayaneo handhelds","Ayaneo","2021","Ayaneo","Ayaneo 3","Ayaneo's line of Windows handheld PCs.",LHH,vv(("Ayaneo","2021","first model"),("Ayaneo 2","2022","second model"),("Ayaneo 3","","named by Liliputing"))))
P[-1]["n"]="Ayaneo"; P[-1].pop("a")
P.append(new("ONEXPLAYER","ONEXPLAYER","",  "ONEXPLAYER","","Handheld gaming PC family from ONEXPLAYER.",LL,vv(("X1 Mini","","named by Liliputing"))))
P.append(new("MSI Claw","MSI","","MSI","","MSI's Windows handheld gaming PC.",LL))
P.append(new("Anbernic WIN600","Anbernic","","Anbernic","","Anbernic's Windows handheld.",LL)) if False else None
P=[p for p in P if p]
def pkey(x): return (x['g'].lower(),int(x['y']) if x.get('y') else 9999,x['n'])
finish("Handheld gaming PC",P,
 "One entry is a handheld gaming PC family or model line sold under its own name; individual models and storage or screen variants are versions.",
 "Every handheld gaming PC family named in Wikipedia's List of handheld game consoles and in Liliputing's handheld gaming PC comparison (Steam Deck, ROG Ally, Legion Go, GPD Win, Ayaneo, ONEXPLAYER, MSI Claw); sections are by maker.",
 "by maker",pkey)
for x in P:
    if x["n"]=="Steam Deck": x["s"]=OLD["Handheld gaming PC"]["Steam Deck"]["s"]
# ---------- Emulation handheld
E=[]
def ke(n,g): return keep("Emulation handheld",n,g)
E.append(ke("GP2X","GamePark Holdings"))
E[-1]["y"]="2005"; E[-1]["s"]=LHH
E[-1]["v"]=vv(("GP32","2001","Game Park's predecessor"),("GP2X","2005","original model"),("GP2X Wiz","2009","pocket model"),("CAANOO","2010","gamepad model"))
for n in ["Anbernic RG351","Anbernic RG353","Anbernic RG35XX","Anbernic RG40XX","Anbernic RG Cube"]: E.append(ke(n,"Anbernic"))
E.append(new("Anbernic Android line","Anbernic","","Anbernic","RG405M · RG505 · RG556","Anbernic's Android handhelds for emulation.",RH,vv(("RG405M","",""),("RG505","",""),("RG556","",""))))
E[-1]["v"]=[{"n":v["n"],"y":"","d":"Android model"} for v in E[-1]["v"]]
E.append(ke("Miyoo Mini","Miyoo")); E[-1]["s"]=RH
E.append(new("Miyoo Flip","Miyoo","","Miyoo","","Miyoo's clamshell emulation handheld.",RH))
E.append(new("TrimUI Smart Pro","TrimUI","","TrimUI","","TrimUI's large-screen emulation handheld.",RH))
E.append(new("Ayaneo Pocket","Ayaneo","","Ayaneo","Pocket S","Ayaneo's pocket Android handhelds.",RH,vv(("Pocket S","",""),)))
E[-1]["v"][0]["d"]="Android model"
E.append(ke("Retroid Pocket","Retroid")); E[-1]["s"]=RH
E.append(new("Dingoo A320","Dingo Digital Technology","2009","Dingoo","","Chinese handheld popular for homebrew and emulators.",LHH))
E.append(new("Pandora","OpenPandora","2010","OpenPandora","","Open-source Linux handheld with keyboard.",LHH))
E.append(new("GCW Zero","Game Consoles Worldwide","2013","Game Consoles Worldwide","","Open-source Linux handheld for homebrew games.",LHH))
E.append(new("GPD XD","GamePad Digital","2015","GPD","","Android gaming handheld from GamePad Digital.",LHH))
E.append(new("TECNO Pocket Go","Tecno Mobile","2024","Tecno","","Windows-based handheld from Tecno Mobile.",LHH))
for x in E:
    if x["g"]=="Anbernic": pass
GM={"GamePark Holdings":"GamePark","Anbernic":"Anbernic"}
def ekey(x): return (x['g'].lower(),int(x['y']) if x.get('y') else 9999,x['n'])
for x in E:
    if x["n"]=="GP2X": x["g"]="GamePark"
    if x["n"]=="Dingoo A320": x["g"]="Dingoo"
finish("Emulation handheld",E,
 "One entry is an emulation-handheld product family or model line sold under its own name; individual models are versions.",
 "Every family named by Retro Handheld HQ's emulator-handheld guide (Anbernic, Miyoo, Retroid, TrimUI, Ayaneo) and every open or Android emulation handheld on Wikipedia's List of handheld game consoles; no whole-space list exists. Sections are by maker.",
 "by maker",ekey)
# ---------- Plug-and-play
PL=[]
EA="Early dedicated home consoles (1972–1984)"
RE="Retro style dedicated consoles (2001–present)"
for n in ["Magnavox Odyssey","Home Pong","Color TV-Game"]: PL.append(keep("Plug-and-play & mini console",n,EA))
PL[0]["role"]="origin"; PL[0]["s"]=LD if False else PL[0]["s"]
PL.append(new("Coleco Telstar series","Coleco","",EA,"","Coleco's early dedicated home console series, named in the dedicated consoles list.",LD))
PL.append(new("APF TV Fun series","APF","",EA,"","APF's early dedicated home console series, named in the dedicated consoles list.",LD))
def ad(n): return OLD["Plug-and-play & mini console"][n]
PL.append(keep("Plug-and-play & mini console","Activision 10-in-1",RE,s=LR))
PL.append(new("Plug It In & Play TV Games","Jakks Pacific","2002",RE,"Plug & Play","Jakks Pacific's joystick TV units with built-in arcade or console games.",LR,
 vv(("Atari Joystick Controller","2002",""),("Namco Pac-Man","2003",""),("Namco Ms. Pac-Man and Friends!","2003",""),("Capcom 3-in-1","2005",""),("Namco Ms. Pac-Man Super Gamekey Mega Pack","2005",""),("Retro Arcade featuring Pac-Man","2008",""),("Retro Arcade featuring Space Invaders","2011",""),("Mega Drive Twin Pads","2007","Sega version"),("Master System Evolution","2008","Sega version"))))
for v in PL[-1]["v"]:
    if not v["d"]: v["d"]="TV game unit"
PL.append(new("Intellivision TV Play Power","Techno Source","2003",RE,"","Techno Source's Intellivision games in a joystick-style unit.",LR,vv(("Intellivision 10 TV Play Power","2003",""),("Intellivision 25 TV Play Power","2003",""),("Intellivision 10 2nd Edition","2005",""),("Intellivision X2 15","2005","")) ))
for v in PL[-1]["v"]: v["d"]=v["d"] or "game count in the name"
PL.append(new("C64 Direct-to-TV","","2004",RE,"","Commodore 64 games in a joystick-style TV unit.",LR))
PL.append(new("Konami Collector's Series: Arcade Advanced","Konami","2004",RE,"TV Arcade","Konami arcade games in a plug-in TV unit.",LR))
PL.append(new("Arcade Legends: Space Invaders","Majesco Entertainment","2004",RE,"","Majesco's plug-in Space Invaders TV unit.",LR))
PL.append(new("Atari Flashback series","Atari","2004",RE,"","Atari's plug-in consoles with built-in games, from Flashback onward.",LR,
 vv(("Atari Flashback","2004",""),("Atari Flashback 2","2005",""),("Atari Flashback 2+","2009","Tectoy"),("Atari Flashback 3","2010",""),("Atari Flashback 4","2011",""),("Atari Flashback 64","2012",""),("Atari Flashback 5","2013",""),("Atari Flashback 6","2014",""),("Atari Flashback 7","2015",""),("Atari Flashback 8","2017",""),("Atari Flashback 9","2017",""),("Atari Flashback X","2019",""),("Atari Flashback 50th Anniversary Edition","2022",""),("Atari Flashback 12 Gold","2022","")),
 role=None))
for v in PL[-1]["v"]: v["d"]=v["d"] or "numbered model"
PL.append(new("Radica Play TV Legends","Radica Games","2005",RE,"Sega Mega Drive/Genesis PlayTV Legends","Radica's plug-in Sega Mega Drive games unit.",LR,vv(("PlayTV Legends","2005","first unit"),("PlayTV Legends Volume II","2005","second unit"))))
PL.append(new("Arcade Motion Dual","Atari","2010",RE,"","Atari's motion-controlled plug-in unit.",LR))
PL.append(new("Pac-Man Connect and Play","Bandai Namco Entertainment","2012",RE,"","Plug-in Pac-Man joystick unit.",LR))
PL.append(new("ColecoVision Flashback","AtGames","2014",RE,"","Plug-in ColecoVision games unit.",LR))
PL.append(new("Intellivision Flashback","AtGames","2014",RE,"","Plug-in Intellivision games unit.",LR))
PL.append(keep("Plug-and-play & mini console","Nintendo Classic Mini",RE,role="landmark",s=OLD["Plug-and-play & mini console"]["Nintendo Classic Mini"]["s"]))
PL[-1].pop("role",None)
PL.append(new("Retro-Bit Generations","Retro-Bit","2016",RE,"","Retro-Bit's plug-in multi-system unit.",LR))
PL.append(new("Super Retro-Cade","Retro-Bit","2017",RE,"","Plug-in retro arcade unit.",LR))
PL.append(new("Atari 2600 Plug & Play joystick","Atari","2016",RE,"","Atari 2600 games in a plug-in joystick.",LR))
PL.append(new("PasocomMini","HAL Laboratory","2017",RE,"","HAL Laboratory's miniature re-creations of Japanese home computers.",LR,vv(("PasocomMini MZ-80C","2017",""),("PasocomMini PC-8001","2019",""),("PasocomMini PC-8801mkIISR","2024",""))))
for v in PL[-1]["v"]: v["d"]="computer mini"
for n in ["PlayStation Classic","Neo Geo Mini","Mega Drive Mini","PC Engine Mini","Astro City Mini","THEC64"]:
    x=keep("Plug-and-play & mini console",n,RE)
    PL.append(x)
for x in PL:
    if x["n"]=="THEC64": x["v"]=[v for v in x["v"] if v["n"] in("THEC64 Mini","THEC64 (full-size)")]; x["a"]="THEC64 Mini"
    if x["n"]=="Neo Geo Mini": x["v"]=x["v"]+[{"n":"NEOGEO Arcade Stick Pro","y":"2019","d":"arcade stick with built-in games"}]
    if x["n"]=="PC Engine Mini": x["mk"]="Konami"
PL.append(new("Capcom Home Arcade","Capcom","2019",RE,"","Capcom's arcade-stick console with built-in games.",LR,vv(("Mega Man Collection","2020","Capcom's Mega Man unit"))))
PL[-1]["v"][0]["d"]="separate Capcom unit"
PL.append(new("Zemmix Mini","Team-Neo","2018",RE,"","Re-creation of the Daewoo Zemmix.",LR,vv(("Zemmix Mini","2018","MSI Entertainment"),("Zemmix Super Mini","2021","Team-Neo"))))
PL.append(new("Midway Arcade Classics","MSI Entertainment","2018",RE,"Midway Classic Arcade Classics Vol. 1","Plug-in unit of Midway arcade games.",LR))
PL.append(new("Pac-Man Collection (Arcade1Up)","Arcade1Up","2020",RE,"","Arcade1Up's Pac-Man plug-in unit.",LR))
PL.append(new("Retro Station","","2020",RE,"","Retro-style plug-in unit listed on the retro-style list.",LR))
PL.append(new("Taito Egret II Mini","Taito","2021",RE,"Taito Arcade Selection: Egret II Mini","Taito's miniature arcade cabinet with built-in games.",LR))
PL.append(new("DanceDanceRevolution Classic Mini","Zuiki","2023",RE,"","Zuiki's mini DDR unit.",LR))
PL.append(new("Atari Gamestation Pro","Atari","2023",RE,"","Atari's handheld-sized TV unit with built-in games.",LR))
PL.append(new("Vectrex Mini","","2025",RE,"","Miniature Vectrex re-creation.",LR))
PL.append(new("Flynn's Generation","","2026",RE,"","Listed retro unit for 2026.",LR))
for x in PL:
    if x["n"]=="Capcom Home Arcade": pass
def plkey(x): return (0 if x['g']==EA else 1,int(x['y']) if x.get('y') else 9999,x['n'])
finish("Plug-and-play & mini console",PL,
 "One entry is a plug-and-play product line or unit with its games built in, sold under its own name; numbered or regional models are versions.",
 "The dedicated consoles named in Wikipedia's List of dedicated consoles and List of retro style video game consoles (dedicated section), grouped into the dedicated-consoles page's two eras; Sport Vii and Xavix PORT sit under Home console, computer re-creations in D1.",
 "by era",plkey)
# ---------- LCD
L=[]
GWs="Game & Watch series (1980–1991)"
OE="Other handheld electronic games (1976–1998)"
RR="Retro-style handhelds (2001–present)"
order=["Game & Watch Silver","Game & Watch Gold","Game & Watch Wide Screen","Game & Watch Multi Screen","Game & Watch New Wide Screen","Game & Watch Panorama","Game & Watch Super Color","Game & Watch Micro Vs. System","Game & Watch Crystal Screen"]
for n in order:
    x=keep("LCD handheld game",n,GWs)
    if n=="Game & Watch Silver": x["role"]="origin"
    L.append(x)
L.append(keep("LCD handheld game","Game & Watch (2020 revival)",RR))
for n in ["Atari Flashback Portable","Game Gear Micro","Super Pocket"]: L.append(keep("LCD handheld game",n,RR))
for x in L:
    if x["n"]=="Atari Flashback Portable": x["s"]=LR
    if x["n"]=="Game & Watch (2020 revival)": x["s"]=LR
L.append(new("Mattel Auto Race","Mattel","1976",OE,"","Mattel's LED race game, an early handheld electronic game.",LD))
L.append(new("Mattel Electronics Battlestar Galactica Space Alert","Mattel","1976",OE,"","Mattel's licensed early handheld electronic game.",LD))
L.append(new("Blip","Tomy","1977",OE,"","Tomy's early handheld electronic game.",LD))
L.append(new("Coleco Electronic Quarterback","Coleco","1978",OE,"","Coleco's handheld electronic football game.",LD))
L.append(new("Merlin","Parker Brothers","1978",OE,"","Handheld the Handheld game console page calls the first commercially successful one.",LHH if False else "https://en.wikipedia.org/wiki/Handheld_game_console",role="origin"))
L.append(new("Alien Attack","Coleco","1979",OE,"","Coleco's handheld electronic game.",LD))
L.append(new("VTech electronic series","VTech","1979",OE,"","VTech's line of handheld electronic games, 1979 to 1991.",LD))
L.append(new("LCD Solarpower","Bandai","1982",OE,"","Bandai's solar-powered LCD handheld games.",LD))
L.append(new("Tiger Electronics Handheld Games series","Tiger Electronics","1987",OE,"Tiger handheld LCD games","Tiger's licensed LCD handheld games, 1987 to 2003.",LD,vv(("Electronic Bowling","",""),("Barcodzz","",""),("Super Data Blasters",'',''))))
L[-1]["v"]=[]
L.append(new("Acclaim Handheld Games series","Acclaim Entertainment","1988",OE,"","Acclaim's handheld games, 1988 to 1991.",LD))
L.append(new("Barcode Battler","Epoch","1991",OE,"","Epoch's barcode-scanning handheld battle game.",LD))
L.append(new("Nintendo Mini Classics","Nintendo","1998",OE,"","Smaller LCD versions of ten Game & Watch titles.",GW))
L.append(new("Pokémon Pikachu","Nintendo","1998",OE,"","Nintendo's pedometer pet handheld.",LD,vv(("Pokémon Pikachu 2","1999","second model"))))
L.append(new("Mattel Handheld Games re-release series","Mattel","2001",RR,"","Re-releases of Mattel's early handheld games.",LR))
L.append(new("Sega Genesis Ultimate Portable Game Player","AtGames","2016",RR,"","Portable Genesis games unit.",LR))
L.append(new("The Oregon Trail Handheld","Basic Fun","2018",RR,"","Retro handheld with a single classic game.",LR))
L.append(new("Go Retro! Portable","","2018",RR,"","Retro handheld listed on the retro-style list.",LR))
L.append(new("Atari 2600 Tiny Arcade","Super Impulse","2021",RR,"","Miniature Atari 2600 games handheld.",LR))
L.append(new("Atari Micro Player","My Arcade","2023",RR,"","Miniature Atari handheld.",LR))
L.append(new("Atari Pocket Player","","2023",RR,"","Atari handheld listed on the retro-style list.",LR))
L.append(new("Atari Gamestation Go","My Arcade","2025",RR,"","Atari handheld with built-in games.",LR))
L.append(new("Game & Watch: Ball (Club Nintendo)","Nintendo","2009",RR,"","Re-release of the original Ball.",LR)) if False else None
L=[l for l in L if l]
sec={GWs:0,OE:1,RR:2}
def lkey(x): return (sec[x['g']],int(x['y']) if x.get('y') else 9999,x['n'])
finish("LCD handheld game",L,
 "One entry is a series or product line of handheld games with the game built in, sold under its own name; the individual games or models in it are versions.",
 "The Game & Watch series from Wikipedia's Game & Watch page, the early handheld electronic games named in List of dedicated consoles, and the retro-style handhelds on List of retro style video game consoles; sections follow those pages' eras.",
 "by series era",lkey)
# ---------- Tabletop
T=[]
T.append(keep("Tabletop electronic game","Coleco Mini-Arcade","Coleco Mini-Arcade (1981– )"))
T.append(keep("Tabletop electronic game","Game & Watch Table Top","Game & Watch Table Top (1983)"))
T[-1]["s"]=GW
T.append(new("Grandstand Astro Wars","Grandstand","1981","Tabletop electronic games (1981– )","","Grandstand's tabletop vacuum-fluorescent shooting game.",LD))
for x in T:
    x["g"]=x["mk"]
def tkey(x): return (int(x['y']),x['n'])
finish("Tabletop electronic game",T,
 "One entry is a tabletop electronic game series or product line sold under its own name; individual games in it are versions.",
 "The tabletop lines named on the Game & Watch page and the dedicated consoles list plus Coleco's Mini-Arcade from its own page; no whole-space list exists.",
 "by maker",tkey)
# ---------- add-ons
AD={}
D1="Disk or CD drive add-on";HU="Hardware upgrade add-on";CC="Cartridge converter"
def addon(kind,name,g): return keep(kind,name,g)
dr=[addon(D1,n,"Drive add-ons") for n in OLD[D1]]
for x in dr:
    x["s"]=x["s"]
finish(D1,sorted(dr,key=lambda x:(int(x['y']),x['n'])),
 "One entry is a distinct disk, CD or card drive add-on sold under its own name for one console family; revisions are versions.",
 "Every drive add-on row of Wikipedia's List of home video game consoles (Famicom Disk System, CD-ROM², Sega CD, Jaguar CD, 64DD); the Satellaview broadcast add-on has no kind here.",
 "by host console",lambda x:(int(x['y']),x['n']))
ex=[keep(HU,"Sega 32X","Hardware upgrades"),keep(HU,"Expansion Pak","Hardware upgrades")]
ex[1]["y"]="1998"
finish(HU,ex,
 "One entry is a distinct hardware upgrade add-on sold under its own name for one console; memory or processor variants are versions.",
 "The upgrade add-ons on Wikipedia's List of home video game consoles (32X) and the Nintendo 64 Expansion Pak from its own page; no whole-space list exists.",
 "by host console",lambda x:(int(x['y']) if x.get('y') else 9999,x['n']))
cv=[keep(CC,n,"Converters") for n in OLD[CC]]
finish(CC,sorted(cv,key=lambda x:(int(x['y']),x['n'])),
 "One entry is a distinct converter or adapter sold under its own name that lets a console play another system's games; regional or revised models are versions.",
 "Official converters named on their own pages (Power Base Converter, Super Game Boy, Game Boy Player); third-party converters are not listed because no fetched reference covers them.",
 "by host console",lambda x:(int(x['y']),x['n']))
HOSTG={"Famicom Disk System":"Nintendo","CD-ROM²":"NEC","Mega-CD":"Sega","Jaguar CD":"Atari","64DD":"Nintendo","Sega 32X":"Sega","Expansion Pak":"Nintendo","Power Base Converter":"Sega","Super Game Boy":"Nintendo","Game Boy Player":"Nintendo"}
for kn in (D1,HU,CC):
    for x in K[kn]['x']: x["g"]=HOSTG[x["n"]]
    K[kn]['xg']="by host console maker"
    K[kn]['x'].sort(key=lambda x:(x['g'],int(x['y']) if x.get('y') else 9999,x['n']))

# ---- gen-fix: explicit membership from per-generation articles
MEM={2:["Fairchild Channel F","Atari 2600","Atari 5200","Bally Astrocade","Magnavox Odyssey 2","Intellivision","ColecoVision","Vectrex","Arcadia 2001","RCA Studio II","1292 Advanced Programmable Video System","Interton VC 4000","APF-MP1000","Champion 2711","Bandai Super Vision 8000","Cassette Vision","VTech CreatiVision","Compact Vision TV Boy","Microvision","Entex Select-A-Game","Entex Adventure Vision","Palmtex Portable Videogame System","Epoch Game Pocket Computer"],
3:["SG-1000","Master System","Nintendo Entertainment System","Atari 7800","Atari XEGS","Super Cassette Vision","Videopac+ G7400","My Vision","PV-1000","Pyuuta Jr.","Bridge Companion","Action Max","View-Master Interactive Vision","VTech Socrates","Amstrad GX4000","Commodore 64 Games System"],
4:["PC Engine","Mega Drive","Super Nintendo Entertainment System","CD-i","Neo Geo AES","SuperGrafx","CDTV","Video Information System","Sega Pico","Pioneer LaserActive","Super A'Can","Game Boy","Atari Lynx","Game Gear","TurboExpress"],
5:["3DO Interactive Multiplayer","Sega Saturn","PlayStation","Nintendo 64","Atari Jaguar","PC-FX","Amiga CD32","FM Towns Marty","Playdia","Casio Loopy","Apple Pippin","CPS Changer","Neo Geo CD","Sega Nomad","Game Boy Color","Neo Geo Pocket","Virtual Boy"],
6:["Dreamcast","PlayStation 2","GameCube","Xbox","Nuon","Xavix PORT","V.Smile","WonderSwan","Game Boy Advance","N-Gage","Cybiko","GP32","Tapwave Zodiac","Pokémon mini"],
7:["Xbox 360","PlayStation 3","Wii","Game Wave Family Entertainment System","HyperScan","V.Flash","Zeebo","Nintendo DS","PlayStation Portable"],
8:["Wii U","PlayStation 4","Xbox One","Nintendo Switch","Nintendo 3DS","PlayStation Vita"],
9:["PlayStation 5","Xbox Series X|S","Nintendo Switch 2"]}
M2={n:g for g,l in MEM.items() for n in l}
placed=[]
for kn in("Home console","Handheld console","Hybrid console"):
    for x in K[kn]['x']:
        if x['n'] in M2: x['g']=GEN[M2[x['n']]]
        else: placed.append(x['n'])
    K[kn]['x'].sort(key=lambda x:([i for i,v in GEN.items() if v==x['g']][0],int(x['y']) if x.get('y') else 9999,x['n']))
    K[kn]['sel']=K[kn]['sel'].replace("placed by release year","placed by the membership lists of the per-generation articles (Second to Ninth generation of video game consoles), by release year where no article names the console").replace("by release year.","by the per-generation articles' membership lists, by release year where none names it.")
open('/home/user/Possession-Taxonomy/rebuild/work/ARC_E5/placed_by_year.txt','w').write('\n'.join(placed))
# drop single-entry sections
for kn in("Handheld gaming PC","Tabletop electronic game","Hardware upgrade add-on"):
    for x in K[kn]['x']: x.pop('g',None)
    K[kn].pop('xg',None)
K["Handheld gaming PC"]['sel']=K["Handheld gaming PC"]['sel'].replace("; sections are by maker","; ordered by release year")
K["Handheld gaming PC"]['x'].sort(key=lambda x:(int(x['y']) if x.get('y') else 9999,x['n']))
K["Tabletop electronic game"]['x'].sort(key=lambda x:(int(x['y']),x['n']))
K["Hardware upgrade add-on"]['x'].sort(key=lambda x:(int(x['y']) if x.get('y') else 9999,x['n']))
# validate fields
for n,k in K.items():
    assert 'm' not in k and 'r' not in k
for k in K.values():
    for x in k['x']:
        assert (x.get('g') or k['n'] in('Handheld gaming PC','Tabletop electronic game','Hardware upgrade add-on')) and x.get('s') and x.get('d') and x.get('mk') is not None, (k['n'],x['n'])
tmp=OUT+'.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=None,separators=(',',':'))
os.replace(tmp,OUT)
for n,k in K.items(): print(n,len(OLD[n]),len(k.get('m',[])) if 0 else '',len(k['x']), sorted({x['g'] for x in k['x']})[:12])
