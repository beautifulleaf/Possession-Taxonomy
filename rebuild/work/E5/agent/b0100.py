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
RC=W+'ROM_cartridge'; N='Nintendo'; S='Sony'; G='Sega'
ED=["standard edition","budget reprint label (Player's Choice, Greatest Hits, Platinum, The Best, Essentials, Nintendo Selects)","limited print run","collector's edition"]
cart={"n":"Game cartridge","a":"Game Pak · cassette · ROM cartridge","d":"Game supplied on a plug-in cartridge holding memory chips.",
 "t":ED+["loose cartridge","complete in box","unlicensed cartridge"],"s":W+"Video_game_cartridge","x":[
 X("Channel F cartridge","Videocart","Fairchild's ROM cartridge, the first interchangeable game cartridge for a home console.","Fairchild","1976",RC,[],"label · box"),
 X("Odyssey game card","jumper card","Plug-in circuit card of the Magnavox Odyssey that rewired the console; a precursor rather than a true ROM cartridge.","Magnavox","1972",RC,[]),
 X("Atari 2600 cartridge","VCS cartridge","ROM cartridge of the Atari 2600, which made swappable cartridges the norm.","Atari","1977",RC,[],"label style · region · handle shape"),
 X("NES Game Pak and Famicom cassette","Game Pak · Famicom cartridge","Nintendo's 8-bit cartridge: short top-loading Famicom cassette in Japan, larger front-loading Game Pak with lockout chip elsewhere.",N,"1983",W+"Nintendo_Entertainment_System",
   [("Famicom cassette",N,"1983","top-loading, 60 connection lines, no lockout chip; Japan"),
    ("NES Game Pak",N,"1985","front-loading, 10NES lockout chip; name coined by Gail Tilden"),
    ("PAL-A and PAL-B Game Paks",N,"","regional lockout variants for the British Isles, Italy and Australasia (A) and continental Europe (B)"),
    ("Unlicensed Famicom cartridge","","","common in Japan and East Asia because the Famicom has no lockout")],"region · lockout chip · label · box"),
 X("Super NES and Super Famicom Game Pak","SNES cartridge","Nintendo's 16-bit cartridge, with region-shaped shells and optional enhancement chips and battery saves.",N,"1990",W+"Super_Nintendo_Entertainment_System",
   [("Super Famicom / PAL Game Pak",N,"","narrow shell with a smooth curved front"),
    ("North American SNES Game Pak",N,"","rectangular shell with grooves matching the console slot"),
    ("Super FX cartridge",N,"","on-cartridge RISC chip for 3D polygon graphics"),
    ("SA-1 cartridge",N,"","on-cartridge 10.7 MHz 65C816 coprocessor"),
    ("DSP cartridge",N,"","fixed-point DSP-1 to DSP-4 maths chips")],"region shell · enhancement chip · battery save"),
 X("Mega Drive and Genesis cartridge","Sega cartridge","Sega's 16-bit top-loading ROM cartridge.",G,"1988",W+"Sega_Genesis",
   [("J-Cart","Codemasters","","two extra controller ports on the cartridge"),
    ("SVP cartridge",G,"1994","Samsung DSP-based polygon chip; the only Genesis cartridge with an enhancement chip"),
    ("EA yellow-tab cartridge","Electronic Arts","","EA shell with a yellow moulded tab")],"region · label · shell"),
 X("Game Boy Game Pak","DMG cartridge · GBC cartridge · GBA Game Pak","Nintendo's handheld cartridge family, from grey Game Boy carts to the half-size Game Boy Advance Game Pak.",N,"1989",W+"Game_Boy_Game_Pak",
   [("Game Boy Game Pak (grey, class A)",N,"1989","works in all Game Boy models except Micro"),
    ("Dual-mode Game Pak (black, class B)",N,"","colour on Game Boy Color, still plays on original Game Boy"),
    ("Game Boy Color Game Pak (clear, class C)",N,"1998","colour-only, no notch"),
    ("Game Boy Advance Game Pak (class D)",N,"2001","about half the size; rumble, tilt and light-sensor variants")],"shell colour · rumble, tilt or sensor"),
 X("Nintendo 64 Game Pak","N64 cartridge","Nintendo 64 ROM cartridge of 4 to 64 MB, some with built-in EEPROM, flash or battery save.",N,"1996",W+"Nintendo_64_Game_Pak",
   [("4–12 MB Game Pak",N,"1996","launch-era size"),("32 MB Game Pak",N,"1998",""),("64 MB Game Pak",N,"1999","largest size")],"size · save type · region")],
 "m":[["Genesis / Mega Drive cartridge",G]]}
disc={"n":"Game disc","a":"optical game disc","d":"Game supplied on an optical disc.","t":ED+["CD-ROM","DVD","Blu-ray","black-label first print"],"s":W+"PlayStation_5","x":[
 X("GD-ROM","Gigabyte Disc","Sega's 1 GB proprietary optical disc developed with Yamaha.",G,"1998",W+"GD-ROM",
   [("Dreamcast GD-ROM",G,"","home console discs"),("NAOMI and Chihiro GD-ROM",G,"","arcade-system discs")]),
 X("GameCube Game Disc","mini-DVD game disc","8 cm, 1.46 GB proprietary disc made with Panasonic.",N,"2001",W+"Nintendo_optical_discs",[]),
 X("Wii Optical Disc","Wii disc","12 cm Nintendo disc of 4.7 or 8.54 GB, followed by the 25 GB Wii U disc.",N,"2006",W+"Nintendo_optical_discs",
   [("Wii Optical Disc",N,"","single or dual layer"),("Wii U Optical Disc",N,"","25 GB")]),
 X("Universal Media Disc","UMD","Sony's 64 mm cased optical disc for the PSP, also used for UMD Video.",S,"2004",W+"Universal_Media_Disc",
   [("Single-layer UMD",S,"2004","900 MB"),("Dual-layer UMD",S,"","1.8 GB"),("UMD Video",S,"","film releases until 2011")]),
 X("Blu-ray game disc","BD-ROM game disc","Blu-ray disc of 25 to 100 GB used for PlayStation and Xbox games.","","2006",W+"Blu-ray",
   [("PlayStation 3 disc",S,"",""),("PlayStation 4 disc",S,"",""),("PlayStation 5 game disc",S,"",""),("Xbox One disc","Microsoft","",""),("Xbox Series X disc","Microsoft","","")],"layers · console")]}
card={"n":"Game card","a":"","d":"Game supplied on a small flash or ROM card.","t":ED+["loose card","complete in box"],"s":W+"Nintendo_Game_Card","x":[
 X("HuCard","TurboChip","Hudson Soft's credit-card-sized ROM card for the PC Engine.","Hudson Soft","1987",W+"HuCard",
   [("HuCard","Hudson Soft","1987","PC Engine and SuperGrafx"),("TurboChip","NEC","","name used where the console was the TurboGrafx-16")]),
 X("Nintendo Game Card","DS card · 3DS card · Switch cartridge","Nintendo's flash game card for DS, 3DS, Switch and Switch 2.",N,"2004",W+"Nintendo_Game_Card",
   [("Nintendo DS Game Card",N,"2004","8–512 MB; DSi-exclusive cards in white"),("Nintendo 3DS Game Card",N,"","side tab blocks use in a DS; region-locked"),
    ("Nintendo Switch Game Card",N,"2017","1–32 GB, region-free, bitter coating"),("Nintendo Switch 2 Game Card",N,"2025","red, 16–64 GB")],"capacity · colour"),
 X("PlayStation Vita Game Card","Vita card","Sony's SD-card-sized flash game card with space for saves and patches.",S,"2011",W+"PlayStation_Vita",[])],
 "m":[["Sega Card (My Card)",G]]}
tape={"n":"Cassette or floppy game","a":"magnetic game media","d":"Game on a cassette tape, floppy disk or disk-system card.","t":["cassette tape","floppy disk","Quick Disk"],"s":"https://en.wikipedia.org/wiki/Famicom_Disk_System","x":[
 X("Home-computer cassette game","tape game","Game sold on compact cassette and loaded through a computer's tape deck, common on 1980s 8-bit home computers.","","1980s","https://collections.vam.ac.uk/item/O1172817",
   [("Amstrad CPC cassette","Amstrad","c. 1985","loaded through the CPC 464's built-in tape deck")],"platform · case and inlay"),
 X("Famicom Disk Card","Disk Card","Nintendo's rewritable 112 KB double-sided disk, a modified Mitsumi Quick Disk.",N,"1986",W+"Famicom_Disk_System",
   [("Disk Card",N,"1986","most without shutters"),("Blue Disk Card",N,"","for Disk Fax high-score games"),("Disk Writer rewrite",N,"","new game written onto an owned card at a shop kiosk")])]}
key={"n":"Game-key card","a":"","d":"Physical card that holds only a key to download a game, not the game itself.","s":"https://www.nintendo.com/au/support/articles/nintendo-switch-2-game-key-card-overview","m":[["Nintendo Switch 2 Game-Key Card",N]]}
dl={"n":"Download-code card","a":"download-code voucher","d":"Card or box that unlocks one game as a download.","s":"https://en-americas-support.nintendo.com/app/answers/detail/a_id/56959","m":[["Nintendo Switch download card (CHOOSE ONE)",N]]}
ce={"n":"Collector's edition","a":"limited edition · special edition","d":"Boxed special edition of a game with extras such as an art book, statue or steelbook.","t":["collector's edition","limited edition","steelbook edition","limited physical print run"],"s":W+"Collector's_edition","x":[
 X("Limited Run Games release","LRG","Small, limited physical print run of a game, sold mainly online, often with a collector's edition.","Limited Run Games","2015",W+"Limited_Run_Games",[])]}
gr={"n":"Graded game","a":"slabbed game","d":"Sealed or loose game sealed in a case and graded for condition by a grading service.","t":["sealed graded","loose cartridge graded","Wata 10-point scale","VGA grade"],"s":W+"Video_game_collecting"}
br=[B("Fairchild","United States","","Mainstream","semiconductors","Fairchild Camera and Instrument; made the Channel F and its cartridges.","knowledge",["Channel F cartridge"]),
 B("Magnavox","United States","","Mainstream","consumer electronics","Electronics brand that sold the first home console, the Odyssey.","knowledge",["Odyssey game card"],["Philips"]),
 B("Atari","United States","1972","Mainstream","consoles","Video-game pioneer behind the 2600 cartridge console.","knowledge",["Atari 2600 cartridge"]),
 B("Nintendo","Japan","1889","Mainstream","consoles","Japanese console maker; Game Paks, Game Cards and optical discs.","knowledge",["NES Game Pak and Famicom cassette","Nintendo Game Card","Game Boy Game Pak"]),
 B("Sega","Japan","1960","Mainstream","consoles","Japanese game company; Mega Drive cartridges and GD-ROM.","knowledge",["Mega Drive and Genesis cartridge","GD-ROM"]),
 B("Sony","Japan","1946","Mainstream","consoles","Japanese electronics group behind PlayStation; UMD and Vita cards.","knowledge",["Universal Media Disc","PlayStation Vita Game Card"]),
 B("Hudson Soft","Japan","","Specialist","games & HuCard","Japanese game company that developed the HuCard for the PC Engine.",W+"HuCard",["HuCard"],["NEC"]),
 B("Limited Run Games","United States","2015","Specialist","limited print runs","North Carolina distributor of small physical print runs and collector's editions; owned by Embracer since 2022.",W+"Limited_Run_Games",["Limited Run Games release"])]
w('E5','01_00',{"kinds":[cart,disc,card,tape,key,dl,ce,gr],"brands":br,"traditions":[],
 "notes":"Edition types (budget reprint labels, limited print run, collector's edition) are types, not titles; no game titles listed. Game cartridge r ['Game Pak', Nintendo] dissolved into Game Pak archetypes; old models became archetypes or versions (J-Cart as Mega Drive version; Channel F, Atari 2600, Odyssey card archetypes); Genesis cartridge kept in m. Game disc: GameCube/Wii/Wii U/GD-ROM/UMD archetypes; PS5 game disc as Blu-ray version. No sourced page found for PlayStation CD-ROM black discs (CD-ROM left as type). Graded game: grading services (Wata, VGA) named as types; belongs with cross-category Grading-services register. Floppy-disk games left as a type (no archetype sourced)."})
