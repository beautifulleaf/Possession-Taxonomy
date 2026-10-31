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
SL=W+'List_of_Sega_arcade_system_boards'; NL=W+'List_of_Namco_arcade_system_boards'
S='Sega'; N='Namco'; T='Taito'; C='Capcom'; K='Konami'; SN='SNK'; NI='Nintendo'
OLD="https://www.arcade-game-sales.com/products/arcade-game-boards-kits/genre-motherboards.html"
sb={"n":"Arcade system board","a":"JAMMA board · PCB · motherboard","d":"Circuit board, with its game ROMs or cartridge or disc slot, that runs games inside a coin-operated video cabinet.",
 "t":["dedicated board","cartridge or cassette system","disc or PC-based system","multi-game board (bootleg)"],"s":OLD,"x":[
 X("Neo Geo MVS","MVS","SNK's cartridge arcade system that let one cabinet hold up to six swappable games.",SN,"1990",W+"Neo_Geo",
   [("1-slot MVS",SN,"",""),("2-slot MVS",SN,"",""),("4-slot MVS",SN,"",""),("6-slot MVS",SN,"","")],"slots 1/2/4/6 · cartridges"),
 X("Capcom CP System","CPS-1 · CPS-2 · CPS-3","Capcom's own board family; CPS-2 splits into a common A board and a game B board, CPS-3 runs from CD-ROM.",C,"",W+"CP_System_II",
   [("Capcom CP System",C,"",""),("CP System II",C,"1993","A/B boards, regional case colours"),("CP System III",C,"1996","CD-ROM with security cartridge")],"region case colour"),
 X("Sega System 16","System 18","Sega's 16-bit sprite boards that served as the basis for the Mega Drive.",S,"1985",SL,
   [("Sega System 16",S,"1985",""),("Sega System 18",S,"","")]),
 X("Sega Super Scaler","X Board · Y Board","Sega's sprite-scaling boards for driving and flying games.",S,"1985",SL,
   [("Sega Super Scaler",S,"1985",""),("Sega OutRun board",S,"1986",""),("Sega X Board",S,"1987","256 sprites"),("Sega Y Board",S,"1988","sprite rotation"),("Sega System 32",S,"1990","first 32-bit, last major sprite board")]),
 X("Sega Model 1, 2 and 3","Model 2","Sega's 3D polygon boards of the 1990s.",S,"1992",SL,
   [("Sega Model 1",S,"1992","first 3D board"),("Sega Model 2",S,"1994","texture mapping, with GE Aerospace"),("Sega Model 3",S,"1996","PowerPC")]),
 X("Sega NAOMI","NAOMI 2","Sega's Dreamcast-based cartridge and GD-ROM board.",S,"1998",SL,
   [("Sega NAOMI",S,"1998",""),("Sega Hikaru",S,"1999","modified NAOMI"),("Sega NAOMI 2",S,"2000","")]),
 X("Sega Mega-Tech","Mega Play","Sega's Mega Drive-based multi-game arcade units.",S,"1989",SL,
   [("Sega Mega-Tech",S,"1989","up to eight games"),("Sega Mega Play",S,"","up to four games")]),
 X("Sega Chihiro, Triforce and PC boards","Lindbergh · RingEdge · ALLS","Sega's console-derived and PC-based boards of the 2000s onward.",S,"2002",SL,
   [("Sega Chihiro",S,"2002","Xbox-based"),("Sega Triforce",S,"2003","GameCube-based, with Namco and Nintendo"),("Sega Lindbergh",S,"2005","Pentium 4"),("Sega Europa-R",S,"2008",""),("Sega RingEdge",S,"2009",""),("Sega RingWide",S,"2011",""),("Sega RingEdge 2",S,"2012",""),("Sega Nu",S,"2013",""),("Sega ALLS",S,"2018","")]),
 X("Namco System 11 and 12","System 10","Namco's PlayStation-based boards, co-developed with Sony.",N,"1994",NL,
   [("Namco System 11",N,"1994",""),("Namco System 12",N,"1996","1.5× CPU clock"),("Namco System 10",N,"2000","")]),
 X("Namco System 22","System 21 · Super System 22","Namco's 3D polygon boards.",N,"1992",NL,
   [("Namco System 21",N,"1988","first board designed for 3D polygons"),("Namco System 22",N,"1992",""),("Namco Super System 22",N,"1995",""),("Namco System 23",N,"1997","")]),
 X("Namco System 246","System 256","Namco's PlayStation 2-based boards.",N,"2000",NL,[("Namco System 246",N,"2000",""),("Namco System 256",N,"2004","")]),
 X("Taito Type X","Type X2 · Type X3","Taito's PC-based arcade platform.",T,"2004",W+"Taito_Type_X",
   [("Taito Type X",T,"2004",""),("Taito Type X2",T,"","PCI Express"),("Taito Type X Zero",T,"","Intel Atom"),("Taito Type X3",T,"",""),("Taito Type X4",T,"","")]),
 X("Konami System 573","System 573","Konami's PlayStation-based board used mainly for Bemani music games.",K,"",W+"System_573",
   [("System 573 Bemani Analog",K,"","CD audio"),("System 573 Bemani Digital",K,"","MP3 decoder")]),
 X("Nintendo VS. System","PlayChoice-10","Nintendo's Famicom-based arcade systems.",NI,"1984",W+"PlayChoice-10",
   [("VS. DualSystem",NI,"1984","two screens"),("VS. UniSystem",NI,"1985","one screen"),("Nintendo PlayChoice-10",NI,"1986","up to ten NES games")])],
 "m":[["Sega Dual",S],["Sega G80",S],["Sega VCO Object",S],["Sega System 1",S],["Sega System 2",S],["Sega System E",S],["Sega System 24",S],["Sega System C",S],["Sega Titan-Video (ST-V)",S],["Sega SystemSP",S],
  ["Namco System 357",N],["Nintendo Super System",NI],["Sony ZN-1","Sony"],["Sony ZN-2","Sony"],
  ["Konami Bubble System",K],["Konami GX",K],["Konami GQ System",K],["Konami GV System",K],
  ["Taito B System",T],["Taito F2 System",T],["Taito F3 System",T],["Taito L System",T],["Taito X System",T],["Taito Z System",T],["Taito SJ System",T],["Taito G-NET",T],["Taito Wolf System",T],
  ["Midway T-Unit","Midway Manufacturing"],["Midway Wolf Unit","Midway Manufacturing"],["Midway X-Unit","Midway Manufacturing"],["Midway Y-Unit","Midway Manufacturing"],
  ["DECO Cassette System","Data East"],["Data East MEC-M1","Data East"],["Cave 68000","Cave"],["Cave CV1000","Cave"],["Psikyo SH2","Psikyo"],["Atomiswave","Sammy"],["PolyGame Master (PGM)",""],["Aleck 64",""]]}
sg={"n":"Supergun","a":"super gun · consolized arcade board","d":"Box that runs a JAMMA arcade board at home on a TV, with controller ports, RGB video and audio outputs.","t":["SCART RGB","composite or S-video","component or VGA","kick harness for extra buttons"],"s":W+"SuperGun"}
lv={"n":"Arcade lever and buttons","a":"arcade joystick · arcade pushbutton","d":"Replacement joystick lever and pushbuttons for an arcade cabinet, control panel or fight stick.",
 "t":["Japanese ball-top lever","American bat-top lever","snap-in button","screw-in button","4-way or 8-way gate"],"s":"https://thepihut.com/collections/sanwa","x":[
 X("Sanwa JLF","JLF-TP-8YT","Sanwa's ball-top Japanese arcade lever.","Sanwa Denshi","","https://thepihut.com/collections/latest-raspberry-pi-products/products/official-sanwa-8-way-arcade-joystick-jlf-tp-8yt",
   [("Sanwa JLF-TP-8YT","Sanwa Denshi","","8-way, square gate, LB-35 ball top")],"ball top colour · gate"),
 X("Sanwa OBSF","OBSF-30","Sanwa's snap-in Japanese arcade buttons.","Sanwa Denshi","","https://thepihut.com/collections/sanwa",
   [("Sanwa OBSF-30","Sanwa Denshi","","30 mm"),("Sanwa OBSF-30RG","Sanwa Denshi","","long-life"),("Sanwa OBSF-24","Sanwa Denshi","","24 mm, square and triangle caps"),("Sanwa SDM-20","Sanwa Denshi","","20 mm")],"colour · clear"),
 X("Seimitsu PS-14","PS-14-G","Seimitsu's flat-faced Japanese snap-in buttons, firmer than Sanwa's.","Seimitsu","","https://www.arcadexpress.com/en/buttons/385-1205-seimitsu-ps-14-g-boton-pulsador-arcade-japones-30mm.html",
   [("Seimitsu PS-14-G","Seimitsu","","30 mm"),("Seimitsu PS-14-D","Seimitsu","","24 mm")]),
 X("Suzo-Happ Competition","Happ","American-style concave pushbuttons and levers with microswitches.","Suzo-Happ","","https://www.arcadexpress.com/en/buttons-arcade-pushbuttons/618-suzo-happ-competition-concave-arcade-button.html",
   [("Suzo Happ Competition Concave Arcade Button","Suzo-Happ","","28 mm, E-Switch microswitch")])],
 "m":[["Seimitsu LS-32 SE","Seimitsu"]]}
mon={"n":"Arcade monitor","a":"arcade CRT · monitor chassis","d":"CRT or LCD monitor, with its chassis, made to fit and run in an arcade cabinet.","t":["15 kHz CRT","multi-sync CRT","LCD"],"s":"https://bitvint.com/pages/arcade-crt",
 "m":[["Electrohome G07-CBO","Electrohome"],["Nanao MS9-29T","Nanao"]],"r":[["Wells-Gardner arcade monitors","Wells-Gardner"],["Hantarex arcade monitors","Hantarex"]]}
KN="knowledge"
br=[B(SN,"Japan","1978","Professional & flagship","Neo Geo","Japanese maker of the Neo Geo MVS and its cabinets.",KN,["Neo Geo MVS"]),
 B(C,"Japan","1979","Professional & flagship","CP System","Japanese game maker of the CP System boards.",KN,["Capcom CP System"]),
 B(S,"Japan","1960","Professional & flagship","arcade boards","Japanese arcade and console maker with some twenty arcade board families.",KN,["Sega System 16","Sega Super Scaler","Sega Model 1, 2 and 3","Sega NAOMI"]),
 B(N,"Japan","1955","Professional & flagship","arcade boards","Japanese arcade maker, now Bandai Namco, of the System boards.",KN,["Namco System 11 and 12","Namco System 22","Namco System 246"]),
 B(T,"Japan","1953","Professional & flagship","arcade boards","Japanese arcade maker of the Type X platform.",KN,["Taito Type X"]),
 B(K,"Japan","1969","Professional & flagship","arcade games","Japanese game maker of the System 573 board.",KN,["Konami System 573"]),
 B(NI,"Japan","1889","Professional & flagship","consoles","Japanese game company that made the VS. System and PlayChoice-10 arcade machines.",KN,["Nintendo VS. System"]),
 B("Sanwa Denshi","Japan","","Specialist","arcade levers & buttons","Japanese maker of the JLF lever and OBSF buttons.","https://thepihut.com/collections/sanwa",["Sanwa JLF","Sanwa OBSF"],["Seimitsu"]),
 B("Seimitsu","Japan","","Specialist","arcade levers & buttons","Japanese maker of LS levers and PS buttons.","https://www.arcadexpress.com/en/buttons/385-1205-seimitsu-ps-14-g-boton-pulsador-arcade-japones-30mm.html",["Seimitsu PS-14"],["Sanwa Denshi"]),
 B("Suzo-Happ","","","Specialist","arcade controls","Maker of American-style Competition levers and pushbuttons.","https://www.arcadexpress.com/en/buttons-arcade-pushbuttons/618-suzo-happ-competition-concave-arcade-button.html",["Suzo-Happ Competition"])]
w('E5','06_01',{"kinds":[sb,sg,lv,mon],"brands":br,"traditions":[],
 "notes":"System board: 80 models -> 14 archetypes (MVS, CPS, Sega System 16, Super Scaler, Model 1-3, NAOMI, Mega-Tech, Chihiro/PC boards, Namco System 11/12, 22, 246, Taito Type X, Konami 573, Nintendo VS.) + 39 models. Dropped boards named after one game (Data East BurgerTime and Caveman Ninja hardware, Taito Qix hardware). Taito Type X+, X7 and NESiCAxLive left out; Pandora's Box-style multi-game boards only as a type (trade/bootleg). Supergun kind-level only (fan-built, no maker products attested). Levers/buttons: Sanwa, Seimitsu, Suzo-Happ; Seimitsu LS-32 attested only as a product mention. Monitors: Electrohome G07 and Nanao MS9-29T models; Wells-Gardner and Hantarex as ranges because no specific chassis page was retrieved (K7000 only in search snippets)."})
