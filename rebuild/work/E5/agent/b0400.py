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
def KD(n,a,d,s,x=None,m=None,t=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    k["s"]=s
    if x: k["x"]=x
    if m: k["m"]=[list(q) for q in m]
    return k
KZ='Krikzz'; DB='https://dragonbox.de/en/everdrives'; DC='https://retrorgb.com/dreamcastode.html'; CM='https://consolemods.org/wiki/Saturn:Phoebe/Rhea'
UP='https://www.retrorgb.com/upscalers.html'; TE='https://www.timeextension.com/news/2025/03/this-mod-brings-crisp-and-clear-hdmi-to-gamecube'
HK='https://handheldlegend.com/en-no/products/game-boy-advance-3-0-inch-ips-lcd-backlight-kit-with-laminated-lens-and-osd-funnyplaying-copy'
HS='https://handheldlegend.com/products/agb-ips-max-laminated-shell'; GBC='https://handheldlegend.com/collections/gbc/products/game-boy-color-shell'
XS='https://dragonbox.de/en/everdrives-flashcarts/xstation-optical-discdrive-emulator-ode-mod-kit-psx-pu-18'
D='Datel'; FP='FunnyPlaying'; PX='PixelFX'; TX='Team Xecuter'; IF='iFixit'
flash=KD("Flash cartridge","flash cart · flashcart","Cartridge that loads game images from a memory card so they run on original console hardware.",W+"Mig_Flash",[
 X("EverDrive","Everdrive","Krikzz's family of SD-card flash cartridges, one model per classic console or handheld.",KZ,"",DB,
   [("Everdrive-N8 Pro",KZ,"","NES"),("Everdrive-N8 Pro Famicom",KZ,"","Famicom"),("Super Everdrive X6",KZ,"","SNES"),("Mega Everdrive Pro",KZ,"","Mega Drive / Genesis"),("Mega Everdrive Core",KZ,"","Mega Drive / Genesis"),("Everdrive64 X7",KZ,"","Nintendo 64"),("Everdrive GB X7",KZ,"","Game Boy and Game Boy Color"),("Everdrive GBA X5 Mini",KZ,"","Game Boy Advance"),("Master Everdrive X7",KZ,"","Master System"),("Everdrive GG X7",KZ,"","Game Gear"),("Turbo Everdrive Pro",KZ,"","PC Engine / TurboGrafx-16")],"Pro, X7, X5 and Core tiers"),
 X("FXPak Pro","","Krikzz-sold SNES flash cartridge from an SD card.",KZ,"",DB,[("FXPak Pro",KZ,"","SNES; grey shell")]),
 X("R4 cartridge","Revolution for DS · R4DS","Nintendo DS flash card booting games and homebrew from microSD; its name was reused by many unrelated clones.","R4 Team","2007",W+"R4_cartridge",
   [("R4 (Revolution for DS)","R4 Team","2007","microSD up to 2 GB, no SDHC")]),
 X("Mig Flash","Mig Switch","Flash cartridge shaped like a Nintendo Switch game card, holding a microSD card.","","",W+"Mig_Flash",
   [("Mig Switch","","","former name"),("Mig Flash","","","Switch and Switch 2")])])
ode=KD("Optical drive emulator","ODE","Board that replaces a console's disc drive so games load from an SD card, USB or hard drive.",DC,[
 X("GDEMU","GDEmu","SD-card board that replaces the Dreamcast's GD-ROM drive.","","",DC,[("GDEMU","","","Dreamcast")]),
 X("Rhea and Phoebe","","SD-card ODEs that physically replace the Sega Saturn disc drive.","Deunan","",CM,
   [("Rhea","Deunan","","Saturn with 20-pin drive"),("Phoebe","Deunan","","Saturn with 21-pin drive")]),
 X("MODE","Terraonion MODE","Multi-console ODE for Saturn, Dreamcast and PlayStation with SATA, USB and microSD storage.","Terraonion","",DC,
   [("MODE","Terraonion","","Saturn or Dreamcast; PlayStation with an extra kit")]),
 X("xStation","","PlayStation ODE loading from microSD, with region-free play built in.","","",XS,
   [("xStation PU-18 kit","","","SCPH-5001 to 5552 and some 700x"),("xStation PU-8 kit","","","sold separately")])],
 [("USB-GDROM","3DO Renovation")],["SD card","USB","SATA drive"])
mod=KD("Modchip","mod chip","Chip or board fitted inside a console to bypass region locking or copy protection, or to run homebrew.",W+"Modchip",[
 X("Xecuter","Team Xecuter chips","Team Xecuter's console modchips, from Xbox multi-BIOS chips to Xbox 360 glitch chips.",TX,"",W+"Modchip",
   [("Xecuter 3 (X3)",TX,"","original Xbox; LCD interface, multi-BIOS"),("CoolRunner",TX,"","Xbox 360 Reset Glitch Hack")])],
 [("MM3 (Multi-Mode 3)",""),("Aladdin",""),("Modbo",""),("X360ACE",""),("WiiKey",""),("Wasabi DX",""),("Picofly",""),("BadHTAB","")],["region and copy-protection chip","drive-emulating chip","voltage-glitch chip"])
sca=KD("Video scaler or upscaler","upscaler · line doubler","External box that converts retro console video for modern displays.",UP,[
 X("RetroTINK","","Plug-and-play line from 480p line doublers to full 4K scalers with CRT mask emulation.","RetroTINK","",UP,
   [("RetroTINK 2X","RetroTINK","",""),("RetroTINK 5X","RetroTINK","",""),("RetroTINK 6X","RetroTINK","",""),("RetroTINK 4K","RetroTINK","","")]),
 X("OSSC","Open Source Scan Converter","Open-source, low-lag line multiplier for RGB and component sources.","","",UP,
   [("OSSC","","",""),("OSSC Pro","","","")]),
 X("XRGB Mini Framemeister","Framemeister","Discontinued Japanese-market scaler, still used for streaming from consoles.","","",UP,[("XRGB Mini Framemeister","","","discontinued")])],
 [("PixelFX Morph",PX),("GBS-Control",""),("RAD2x HDMI cable","")],["line doubler","line multiplier","full scaler"])
hdmi=KD("Internal HDMI or RGB mod kit","HDMI mod · RGB mod","Board installed in a console, or adapter on its digital port, that gives HDMI or RGB output.",TE,[
 X("UltraHDMI","","Internal N64 board capturing digital RGB from the RCP for HDMI up to 1080p.","","","https://consolemods.org/wiki/N64:UltraHDMI_(HDMI)",[("UltraHDMI","","","Nintendo 64; No Cut version")]),
 X("Retro GEM","","PixelFX internal HDMI board for several disc consoles.",PX,"",TE,
   [("Retro GEM (PS1)",PX,"",""),("Retro GEM (PS2)",PX,"",""),("Retro GEM (Dreamcast)",PX,"",""),("Retro GEM (GameCube)",PX,"2025","")])],
 [("Carby","Insurrection Industries")],["internal HDMI board","RGB amplifier board","digital-port adapter"])
scr=KD("Screen upgrade kit","IPS kit · backlight kit","IPS or backlit replacement screen kit for a handheld.",HK,[
 X("FunnyPlaying IPS kit","","FunnyPlaying's IPS screen kits for Game Boy handhelds, with brightness and on-screen menus.",FP,"",HK,
   [("Game Boy Advance 3.0 Inch IPS LCD Backlight Kit M2",FP,"","laminated lens, OSD, 15 brightness levels"),("AGB IPS MAX Laminated Display Kit",FP,"","needs its own shell")])],
 None,["IPS","laminated","backlight"])
shell=KD("Replacement shell","housing","Aftermarket housing for a handheld or controller, often trimmed for screen and battery mods.",GBC,None,
 [("Game Boy Color Replacement Shell","Hand Held Legend"),("AGB IPS MAX Laminated Shell",FP)],["standard","IPS-ready","clear or coloured"])
rep=KD("Reproduction cartridge","repro cart","Aftermarket-made cartridge of a game; genuine-looking fakes are spotted by screws, labels and boards.","https://www.epilogue.co/support/cartridges/spotting-fakes",None,None,["sold as reproduction","counterfeit"])
AR=[("Pro Action Replay",D,"",""),("Pro Action Replay MK2","","",""),("Pro Action Replay MK3",D,"",""),("Pro Action Replay 4M",D,"",""),("Action Replay 4M Plus (Saturn)","","",""),("Action Replay CDX",D,"",""),("Action Replay Professional (Nintendo 64)",D,"",""),("Action Replay MAX",D,"",""),("Action Replay DS",D,"",""),("Action Replay Wii",D,"",""),("Action Replay PSP",D,"",""),("Action Replay Power Saves for 3DS",D,"","")]
cheat=KD("Cheat device","Game Genie · Action Replay · GameShark","Cartridge or unit that alters a game's code to give cheats.",W+"Game_Genie",[
 X("Game Genie","","Codemasters' pass-through cheat cartridge; a court ruled it did not infringe Nintendo's copyrights.","Codemasters","1990",W+"Game_Genie",
   [("Game Genie (NES)","Codemasters","1990","distributed by Galoob in the US"),("Game Genie (Super NES)","Codemasters","",""),("Game Genie (Genesis)","Codemasters","",""),("Game Genie (Game Boy)","Codemasters","",""),("Game Genie (Game Gear)","Codemasters","","")]),
 X("Action Replay","Pro Action Replay","Datel's cheat cartridge line, first for the Commodore 64 and Amiga, then for most consoles.",D,"",W+"Datel",[(a,b,c,d) for a,b,c,d in AR]),
 X("GameShark","","US name for Datel cheat devices through InterAct; Mad Catz bought the brand in 2003.",D,"",W+"Datel",
   [("GameShark",D,"","InterAct distribution"),("GameShark Duo","Mad Catz","","")])],
 [("Code Breaker",""),("Xploder",""),("Game Wizard",""),("X-Terminator","")])
part=KD("Replacement part","spare part","Spare part for repairing a game machine or controller.","https://chromagi.com/nintendo/n64/",None,
 [("iFixit Nintendo Switch Console Battery",IF),("iFixit Nintendo Switch Fan",IF),("iFixit Nintendo Switch Screen",IF),("iFixit Nintendo Switch Game Card Reader",IF),("iFixit Nintendo Switch Joy-Con/Switch Lite Joystick",IF),("iFixit PS5 DualSense Controller Gulikit TMR Joystick",IF),("iFixit PlayStation DualSense Controller Battery",IF),("iFixit Xbox 360 Red Ring of Death Fix Kit",IF),("iFixit PlayStation 3 Yellow Light of Death Fix Kit",IF)],
 ["battery","joystick module (incl. Hall-effect or TMR)","cooling fan","screen","game-card reader","buttons and trim","fix kit"])
tool=KD("Repair toolkit","console screwdriver set","Screwdriver and pry-tool set for opening and repairing game consoles and controllers.","https://www.amazon.com/EasyTime-Compatible-Nintendo-Screwdriver-Gamecube/dp/B087M85WMF",None,
 [("iFixit Nintendo Switch Toolkit",IF),("iFixit PlayStation Toolkit",IF),("iFixit Xbox Toolkit",IF),("iFixit Steam Deck Toolkit",IF),("Jumper Pak Ejector Tool","Nintendo")],["screwdriver set","security bits (tri-wing, 3.8 mm, 4.5 mm)","pry tools"])
br=[B(KZ,"","","Specialist","flash cartridges","Maker of EverDrive flash cartridges for classic consoles.",DB,["EverDrive","FXPak Pro"]),
 B("R4 Team","","2007","Artisan & independent","DS flash cards","Group behind the original R4 (Revolution for DS) flash card.",W+"R4_cartridge",["R4 cartridge"]),
 B("Deunan","","","Artisan & independent","Saturn ODEs","Developer of the Rhea and Phoebe Saturn optical drive emulators.",CM,["Rhea and Phoebe"]),
 B("Terraonion","","","Specialist","ODEs","Maker of the MODE multi-console optical drive emulator.",DC,["MODE"]),
 B(TX,"","","Specialist","modchips","Modchip maker named for Xbox and Xbox 360 chips.",W+"Modchip",["Xecuter"]),
 B("RetroTINK","","","Specialist","video scalers","Maker of the RetroTINK line doublers and scalers.",UP,["RetroTINK"]),
 B(PX,"","","Specialist","HDMI mods","Maker of Retro GEM internal HDMI boards and Morph scalers.",TE,["Retro GEM"]),
 B(FP,"","","Specialist","IPS screen kits","Maker of IPS screen kits and matching shells for Game Boy handhelds.",HK,["FunnyPlaying IPS kit"]),
 B("Codemasters","United Kingdom","1986","Mainstream","games","British game developer that created the Game Genie.","knowledge",["Game Genie"]),
 B(D,"United Kingdom","1980","Specialist","cheat devices","Staffordshire accessory maker of Action Replay and GameShark cheat devices.",W+"Datel",["Action Replay","GameShark"]),
 B(IF,"United States","2003","Specialist","repair parts & tools","Repair-guide site selling console parts and toolkits.","knowledge")]
w('E5','04_00',{"kinds":[flash,ode,mod,sca,hdmi,scr,shell,rep,cheat,part,tool],"brands":br,"traditions":[],
 "notes":"Old kinds kept: Flash cartridge (now EverDrive, FXPak Pro, R4, Mig Flash archetypes), Cheat device (34 models into Game Genie, Action Replay and GameShark archetypes; kept 12 Action Replay versions, dropped the long tail of DS/PSP/online/Max variants and GBX/Ultimate Codes), Replacement part (16 iFixit SKUs cut to 9 with part types), Repair toolkit. New kinds: Optical drive emulator, Modchip, Video scaler, Internal HDMI or RGB mod kit, Screen upgrade kit, Replacement shell, Reproduction cartridge, each sourced from a fetched page. Not found on retrieved pages: EZ-Flash, SD2SNES name history, makers of GDEMU, xStation, OSSC, UltraHDMI and Framemeister (left blank); Action Replay and GameShark years. Carby is a plug-in GameCube digital-port adapter, kept as a model in the HDMI kind."})
