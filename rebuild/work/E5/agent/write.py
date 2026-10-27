import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def K(n,a,d,s,m=None,r=None,t=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    k["s"]=s
    if m: k["m"]=[list(x) for x in m]
    if r: k["r"]=[list(x) for x in r]
    return k
N="Nintendo"; S="Sony"; M="Microsoft"; G="Sega"; PA="PowerA"; CH="https://chromagi.com/nintendo/switch/"
w('E5','01_01',{"kinds":[
 K("Digital game","digital game licence","Full game downloaded from a console or PC store, held with no disc or cartridge.","https://en.wikipedia.org/wiki/Steam_(service)"),
 K("DLC","downloadable content · expansion · add-on","Extra game content bought and downloaded for a game already owned, from a large expansion to a small map, character or cosmetic pack.","",None,None,["Expansion","Add-on pack"]),
 K("Game mod","","Modification that adds to or changes one game.","https://en.wikipedia.org/wiki/Video_game_modding")],
 "brands":[],"traditions":[],"notes":"All three kinds kept kind-level with no models. DLC given a plain definition; Expansion and Add-on pack kept as types; it still has no source (old kind had none; no research on this shelf)."})
w('E5','03_00',{"kinds":[
 K("Case or pouch","carry case · storage case","Case or pouch made to hold or protect one game machine.",CH,
   [("Switch Carry Case & Screen Protector",N),("PowerA Protection Case for Nintendo Switch",PA),("PowerA PlayStation Portal Protection Case",PA),("PlayStation VR2 Storage Case",S),("Meta Quest 3 Carrying Case","Meta"),("KIWI Design Carrying Case for Quest 3","KIWI Design"),("PSP Pouch & Hand Strap",S),("Game Boy Advance Pouch",N)],None,["hard carry case","soft pouch","storage case"]),
 K("Screen protector","screen protector film · tempered glass","Film or glass sheet cut to cover the screen of one game machine.",CH,
   [("dbrand Gaming Glass for Nintendo Switch 2","dbrand"),("dbrand Gaming Glass for Steam Deck","dbrand"),("dbrand Gaming Glass for ROG Ally","dbrand"),("dbrand Gaming Glass for PlayStation Portal","dbrand"),("Spigen Glas.tR EZ Fit for Nintendo Switch 2","Spigen"),("PowerA PlayStation Portal Screen Protection Kit",PA),("Ringke Easy Slide for Nintendo Switch 2","Ringke"),("3MK FlexibleGlass for Steam Deck","3MK")],None,["tempered glass","film","matte"]),
 K("Faceplate, skin or decal","","Cover plate, skin or decal that changes the outside of one game machine or controller.","https://dbrand.com/shop/devices/nintendo-skins",
   [("dbrand Nintendo Switch 2 skin","dbrand"),("dbrand Nintendo Switch OLED skin","dbrand"),("dbrand Nintendo Switch Lite skin","dbrand"),("dbrand Nintendo Switch Pro Controller skin","dbrand")],None,["faceplate","skin","decal"])],
 "brands":[],"traditions":[],"notes":"Case or pouch cut from 16 to 8 (kept two Quest cases as the VR examples; dropped other Quest cases from Annapro, BOBOVR, Syntech, Meta Compact, PowerA Quest bag, PS VR storage case, Mobile Pouch DS; dropped the maker-less 'Nintendo 64 Game Storage Tower' as noise). Screen protector film renamed Screen protector; cut from 22 to 8 market-covering makers. Skins unchanged."})
w('E5','03_01',{"kinds":[
 K("Replacement battery pack","","Rechargeable battery pack made for one game machine or controller.","https://chromagi.com/class/battery/",
   [("Xbox Rechargeable Battery",M),("Xbox Play and Charge Kit (Series X|S)",M),("Xbox 360 Play & Charge Kit",M),("Joy-Con AA Battery Pack",N),("Nintendo 3DS Rechargeable Battery Pack",N),("Wii U GamePad Rechargeable Battery Pack",N),("PSP Battery Pack",S)]),
 K("AC adapter","power supply","Power adapter made for one game machine.","https://chromagi.com/class/power-supply/",
   [("Nintendo Switch 2 AC Adapter",N),("Nintendo Switch AC Adapter",N),("Nintendo 3DS AC Adapter",N),("Xbox 360 S AC Adapter",M),("PSP AC Adaptor",S),("Super NES AC Adapter",N),("Mega Drive AC Adaptor",G)]),
 K("Charging stand","charging dock","Stand or dock that only charges the machine or controller.","https://chromagi.com/sony/ps5/cfi-zds1/",
   [("DualSense Charging Station",S),("DUALSHOCK 4 Charging Station",S),("PowerA PlayStation Portal Charging Station",PA),("Meta Quest 3 Charging Dock","Meta"),("PowerA Charging Station for Quest 3/3S",PA),("KIWI Design RGB Vertical Charging Stand","KIWI Design"),("New Nintendo 3DS Charging Cradle",N),("Wii U GamePad Cradle",N)]),
 K("TV dock","","Dock that gives video output to a TV as well as charging.",CH,
   [("Nintendo Switch 2 Dock",N),("Nintendo Switch OLED Model Dock",N),("Nintendo Switch Dock",N),("GENKI Covert Dock 2 HDMI & Charger","Genki"),("Razer Handheld Dock Chroma","Razer")]),
 K("Console stand or mount","","Stand or mount made to hold one game machine.",CH,
   [("PlayStation 4 Vertical Stand",S),("PlayStation 2 Vertical Stand",S),("Xbox One S Vertical Stand",M),("Nintendo Switch Stand",N),("Wii Console Stand",N),("Nintendo Switch Attachment Bracket",N),("AMVR VR Stand","AMVR")],None,["vertical stand","horizontal stand","wall mount"]),
 K("Console cooling unit","","External fan, cooling stand or clip-on unit made to cool one console. A replacement internal fan is a replacement part.","https://en.wikipedia.org/wiki/Nyko",
   [("NexiGo PS5 Silent Cooling Stand","NexiGo"),("OIVO PS5 Stand","OIVO"),("G-STORY Cooling Fan","G-STORY")],None,["cooling stand","clip-on fan"])],
 "brands":[],"traditions":[],"notes":"Battery packs: removed 8 VR battery head straps (Annapro, BOBOVR, KIWI Design, Meta Elite, ZyberVR; the VR shelf handles head straps) and older duplicates (Xbox 360 Quick Charge Kit, Xbox 360 Rechargeable Battery Pack, Xbox Play & Charge Kit, Virtual Boy Battery Box): 20 to 7. AC adapter cut from 22 per-console models to 7 first-party examples (no aftermarket makers in old data). Charging stand 14 to 8, stands 9 to 7, cooling units 8 no-name brands to 3. TV dock unchanged."})
w('E5','03_02',{"kinds":[
 K("Console cable or adapter","proprietary cable · AV cable · link cable","Cable or adapter with a connector made for one console.","https://chromagi.com/microsoft/x360/",
   [("PlayStation 3 Component AV Cable",S),("Xbox 360 Component HD AV Cable",M),("Wii Component AV Cable",N),("GameCube Component Video Cable",N),("Mega Drive RF Unit",G),("Game Boy Game Link Cable",N),("Game Boy Advance Game Link Cable",N),("PlayStation Link Cable",S),("SNES and N64 RGB SCART 75 Ohm Coaxial Pro Cable with MultiSync Switch","Retro Access"),("PlayStation 2 RGB SCART 75 Ohm Coaxial Pro Cable","Retro Access"),("Sega Saturn RGB SCART PACKAPUNCH PRO cable","Retro Game Cables"),("Sega Mega Drive 2 Component YPbPr cable (RetroTink)","Retro Game Cables")],
   None,["RF","composite","S-Video","RGB SCART","component","VGA","HDMI","link cable"]),
 K("Console memory card","proprietary memory card · expansion","Memory card, drive or expansion in a format made only for one console.","https://chromagi.com/microsoft/x360/",
   [("PlayStation memory card",S),("PlayStation 2 8 MB Memory Card",S),("Dreamcast VMU",G),("Saturn Backup Memory",G),("Nintendo 64 Controller Pak",N),("Nintendo 64 Expansion Pak",N),("GameCube Memory Card 251",N),("Xbox 360 64MB Memory Unit",M),("Neo Geo memory card","SNK"),("Seagate Storage Expansion Card for Xbox Series X and S","Seagate")]),
 K("Multitap","","Unit that adds controller ports to a console.","https://chromagi.com/nintendo/sfc-snes/",
   [("NES Four Score",N),("NES Satellite",N),("Super Multitap","Hudson Soft"),("PC Engine Multitap","NEC Home Electronics"),("Sega Team Player",G),("EA 4 Way Play","Electronic Arts"),("Saturn 6 Player Adapter",G),("PlayStation Multitap",S),("PlayStation 2 Slimline Multitap (SCPH-70120)",S),("Famicom 4-Player Adaptor","Hori")]),
 K("Controller converter","Brook Wingman · Mayflash Magic","Dongle, adapter or board that translates a controller's signals so it works on a console or computer it was not made for. A plain cable is a console cable or adapter.","https://tools.prnewswire.com/en-us/live/20813/release/20251029EN05296",
   [("Brook Wingman XB2","Brook"),("Brook Wingman FGC2","Brook"),("Brook Wingman SD","Brook"),("Brook Ras1ution 2","Brook"),("Mayflash Magic NS","Mayflash"),("Mayflash Magic-S Pro 2","Mayflash"),("8BitDo Wireless USB Adapter 2","8BitDo"),("GameCube Controller Adapter for Wii U",N)]),
 K("Console network adapter","modem adapter","Adapter that adds a dial-up modem, broadband or wireless network connection to one console through its own port or bay. A standard USB network adapter is in Computers & Components.","https://chromagi.com/nintendo/ngc/",
   [("Sega NetLink",G),("Dreamcast Modem Adapter",G),("Dreamcast Broadband Adapter",G),("PlayStation 2 Network Adaptor",S),("XBAND Modem","Catapult Entertainment"),("Mega Modem",G),("Nintendo 64 Modem Cartridge (NUS-029)",N),("Xbox 360 Wireless Network Adapter",M),("SharkWire Online","Datel")])],
 "brands":[],"traditions":[],"notes":"Console cable: 44 per-console SKUs cut to 12 examples with signal types as types (first-party, Retro Access, Retro Game Cables; no Hyperkin models in old data). GameCube Controller Adapter for Wii U moved into Controller converter. Memory card: kept first-party formats plus Seagate (dropped third-party Turbo File/II and Dreamcast Nexus, Xbox 360 hard drive, duplicates). Multitap: 22 to 10, dropped maker-less entries and minor third-party units. Controller converter: 18 to 8. Network adapter: dropped maker-less GameCube adaptors, Dreamcast LAN Adapter and NTT Data modem."})
