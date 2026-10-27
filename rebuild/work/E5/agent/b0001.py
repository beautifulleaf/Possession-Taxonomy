import json, os
W = 'https://en.wikipedia.org/wiki/'
K = 'knowledge'

def X(n, a, d, mk, y, s, v, dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [{"n": q[0], "mk": q[1], "y": q[2], "d": q[3]} for q in v], "dt": dt}

def B(n, c, f, seg, kf, d, s, sig=(), rel=()):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d}
    if sig: b["sig"] = list(sig)
    if rel: b["rel"] = list(rel)
    b["s"] = s
    return b

NI, SO, SE = "Nintendo", "Sony", "Sega"
handheld = [
 X("Microvision", "", "First handheld with interchangeable cartridges, each carrying its own processor.", "Milton Bradley", "1979", W+"Microvision",
   [("Microvision", "Milton Bradley", "1979", "designed by Jay Smith")]),
 X("Game Boy", "DMG-01", "Nintendo's monochrome cartridge handheld that set the template for handheld gaming.", NI, "1989", W+"Game_Boy",
   [("Game Boy (DMG-01)", NI, "1989", "original grey"),
    ("Game Boy Play It Loud!", NI, "1995", "coloured cases"),
    ("Game Boy Pocket", NI, "1996", "slimmer, better screen"),
    ("Game Boy Light", NI, "1998", "Japan only, backlit")], "case colour · edition"),
 X("Atari Lynx", "Handy", "First handheld with a colour backlit screen, designed by Epyx.", "Atari", "1989", W+"Atari_Lynx",
   [("Atari Lynx", "Atari", "1989", ""),
    ("Lynx II", "Atari", "1991", "smaller, stereo headphone jack")]),
 X("Game Gear", "", "Sega's colour handheld, based on Master System hardware.", SE, "1990", W+"Game_Gear",
   [("Game Gear", SE, "1990", ""),
    ("Game Gear (Majesco)", "Majesco", "2000", "budget re-release"),
    ("Coca-Cola Game Gear", SE, "", "red promotional edition")], "colour · edition"),
 X("TurboExpress", "PC Engine GT", "Handheld that plays the same HuCards as the PC Engine.", "NEC", "1990", W+"TurboExpress",
   [("PC Engine GT", "NEC", "1990", "Japan"),
    ("TurboExpress", "NEC", "1990", "North America")]),
 X("Sega Nomad", "Genesis Nomad", "Handheld Genesis that plays standard Genesis cartridges, developed from the Mega Jet.", SE, "", W+"Sega_Genesis",
   [("Genesis Nomad", SE, "", "3.25-inch LCD")]),
 X("Game Boy Color", "GBC", "Colour successor to the Game Boy that also plays Game Boy cartridges.", NI, "1998", W+"Game_Boy_Color",
   [("Game Boy Color", NI, "1998", "Berry, Grape, Kiwi, Dandelion, Teal, Atomic Purple"),
    ("Game Boy Color Pikachu edition", NI, "", "special edition")], "case colour · special edition"),
 X("Neo Geo Pocket", "Neo Geo Pocket Color", "SNK's handheld with a clicky microswitch joystick.", "SNK", "1998", W+"Neo_Geo_Pocket",
   [("Neo Geo Pocket", "SNK", "1998", "monochrome"),
    ("Neo Geo Pocket Color", "SNK", "1999", "colour")]),
 X("WonderSwan", "", "Bandai's Japanese handheld developed with Gunpei Yokoi's Koto Laboratory.", "Bandai", "1999", W+"WonderSwan",
   [("WonderSwan", "Bandai", "1999", "monochrome"),
    ("WonderSwan Color", "Bandai", "2000", ""),
    ("SwanCrystal", "Bandai", "2002", "improved screen")]),
 X("Game Boy Advance", "GBA", "Nintendo's 32-bit cartridge handheld, backward-compatible with Game Boy games.", NI, "2001", W+"Game_Boy_Advance",
   [("Game Boy Advance", NI, "2001", "original"),
    ("Game Boy Advance SP (AGS-001)", NI, "2003", "clamshell, front-lit"),
    ("Game Boy Micro", NI, "2005", "smallest model"),
    ("Game Boy Advance SP (AGS-101)", NI, "2005", "backlit screen")], "model · colour"),
 X("Nintendo DS", "DS", "Nintendo's dual-screen handheld with a touch screen.", NI, "2004", W+"Nintendo_DS",
   [("Nintendo DS", NI, "2004", ""),
    ("Nintendo DS Lite", NI, "2006", "slimmer, brighter"),
    ("Nintendo DSi", NI, "2008", "cameras, SD slot"),
    ("Nintendo DSi XL", NI, "2009", "larger screens")], "model · colour"),
 X("PlayStation Portable", "PSP", "Sony's first handheld, using UMD optical discs.", SO, "2004", W+"PlayStation_Portable",
   [("PSP-1000", SO, "2004", "original"),
    ("PSP-2000", SO, "2007", "slimmer, lighter"),
    ("PSP-3000", SO, "2008", "better screen, microphone"),
    ("PSP Go (PSP-N1000)", SO, "2009", "no UMD drive"),
    ("PSP Street (PSP-E1000)", SO, "2011", "budget, Europe")], "model · colour"),
 X("Nintendo 3DS", "3DS", "Nintendo's handheld with glasses-free stereoscopic 3D.", NI, "2011", W+"Nintendo_3DS",
   [("Nintendo 3DS", NI, "2011", ""),
    ("Nintendo 3DS XL", NI, "2012", "larger screens"),
    ("Nintendo 2DS", NI, "2013", "slate, no 3D"),
    ("New Nintendo 3DS", NI, "2014", "faster, C-stick"),
    ("New Nintendo 3DS XL", NI, "2014", ""),
    ("New Nintendo 2DS XL", NI, "2017", "clamshell, no 3D")], "model · colour · edition"),
 X("PlayStation Vita", "PS Vita", "Sony's second handheld, with an OLED screen and rear touch pad.", SO, "2011", W+"PlayStation_Vita",
   [("PCH-1000", SO, "2011", "OLED screen"),
    ("PCH-2000 (PS Vita Slim)", SO, "2013", "thinner, LCD"),
    ("PlayStation TV (Vita TV)", SO, "2013", "TV micro-console that plays Vita games")]),
 X("Evercade", "Evercade EXP", "Blaze's handheld for multi-game Evercade cartridges of licensed retro games.", "Blaze Entertainment", "2020", W+"Evercade",
   [("Evercade", "Blaze Entertainment", "2020", ""),
    ("Evercade EXP", "Blaze Entertainment", "2022", "upgraded handheld"),
    ("Evercade EXP-R", "Blaze Entertainment", "", "")]),
 X("Analogue Pocket", "", "FPGA handheld that plays original Game Boy, Game Boy Color and Game Boy Advance cartridges.", "Analogue", "2021", W+"Analogue_Pocket",
   [("Analogue Pocket (black, white)", "Analogue", "2021", ""),
    ("Analogue Pocket Glow", "Analogue", "2023", "glow-in-the-dark"),
    ("Analogue Pocket Transparent", "Analogue", "2023", ""),
    ("Analogue Pocket Classic", "Analogue", "2023", "Game Boy colours"),
    ("Analogue Pocket Aluminium", "Analogue", "2024", "white, black, grey, indigo")], "edition · colour"),
 X("Playdate", "", "Small 1-bit handheld with a crank, designed with Teenage Engineering.", "Panic", "2022", W+"Playdate_(console)",
   [("Playdate", "Panic", "2022", "")], "cover colour"),
]
handheld_m = [["Select-A-Game", "Entex"], ["Adventure Vision", "Entex"], ["Epoch Game Pocket Computer", "Epoch Co."],
 ["Palmtex Portable Videogame System", "Palmtex"], ["Gamate", "Bit Corporation"], ["Watara Supervision", "Watara"],
 ["Game Master", "Hartung"], ["Mega Duck", "Welback Holdings"], ["Design Master Senshi Mangajukuu", "Bandai"],
 ["Digi Casse", "Bandai"], ["Game.com", "Tiger Electronics"], ["GameKing", "Timetop"], ["Cybiko", "Cybiko"],
 ["P/ECE", "Aquaplus"], ["Pokemon mini", "Nintendo"], ["N-Gage", "Nokia"], ["N-Gage QD", "Nokia"],
 ["Tapwave Zodiac", "Tapwave"], ["Gizmondo", "Tiger Telematics"], ["Neo Geo X", "Tommo"],
 ["Nvidia Shield Portable", "Nvidia"], ["Hyperkin Supaboy S", "Hyperkin"], ["Hyperkin Supaboy SFC", "Hyperkin"],
 ["SupaBoy Portable", "Hyperkin"], ["Retro Duo Portable", "Retro-Bit"], ["ZX Spectrum Vega+", "Basic Fun"],
 ["Arduboy", ""], ["Thumby", "TinyCircuits"], ["Game Gadget", ""]]

hybrid = [
 X("Nintendo Switch", "Switch", "Nintendo's console that docks to a TV or runs as a handheld with detachable Joy-Con.", NI, "2017", W+"Nintendo_Switch",
   [("Nintendo Switch (HAC-001)", NI, "2017", "original"),
    ("Nintendo Switch (HAC-001(-01))", NI, "2019", "Tegra X1+, longer battery life"),
    ("Nintendo Switch Lite", NI, "2019", "handheld-only"),
    ("Nintendo Switch OLED Model", NI, "2021", "OLED screen")], "model · colour · edition"),
 X("Nintendo Switch 2", "", "Nintendo's successor hybrid console with larger screen and magnetic Joy-Con 2.", NI, "2025", W+"Nintendo_Switch_2",
   [("Nintendo Switch 2", NI, "2025", "international model"),
    ("Nintendo Switch 2 (Japan-only model)", NI, "2025", "region-locked, Japanese language only")], "region · bundle"),
]

pc = [
 X("Steam Deck", "", "Valve's handheld gaming PC running SteamOS.", "Valve", "2022", W+"Steam_Deck",
   [("Steam Deck LCD 64 GB", "Valve", "2022", ""),
    ("Steam Deck LCD 256 GB", "Valve", "2022", ""),
    ("Steam Deck LCD 512 GB", "Valve", "2022", ""),
    ("Steam Deck OLED 512 GB", "Valve", "2023", ""),
    ("Steam Deck OLED 1 TB", "Valve", "2023", "")], "screen · storage"),
 X("ROG Ally", "ROG Xbox Ally", "ASUS's Windows handheld gaming PC line, later co-branded with Xbox.", "ASUS", "", "https://rog.asus.com/gaming-handhelds/rog-ally/rog-xbox-ally-2025/",
   [("ROG Ally (RC71L)", "ASUS", "", "Ryzen Z1"),
    ("ROG Ally X", "ASUS", "", ""),
    ("ROG Xbox Ally (RC73YA)", "ASUS", "2025", "Ryzen Z2 A"),
    ("ROG Xbox Ally X (RC73XA)", "ASUS", "2025", "Ryzen Z2 Extreme")], "chip · memory"),
 X("Legion Go", "", "Lenovo's Windows handheld gaming PC with detachable controllers.", "Lenovo", "2023", "https://liliputing.com/lenovo-legion-go-handheld-gaming-pc-coming-in-september-for-700-and-up/",
   [("Legion Go", "Lenovo", "2023", "Ryzen Z1 Extreme")]),
 X("GPD Win", "", "GamePad Digital's Windows palmtop with keyboard and game controls.", "GPD", "2016", W+"GPD_Win",
   [("GPD Win", "GPD", "2016", ""),
    ("GPD Win 2", "GPD", "", ""),
    ("GPD Win 3", "GPD", "", ""),
    ("GPD Win 4", "GPD", "", ""),
    ("GPD Win Max", "GPD", "", "larger clamshell"),
    ("GPD Win Mini", "GPD", "", "")], "chip · screen"),
]
pc_m = [["MSI Claw A1M", "MSI"], ["Ayaneo", "Ayaneo"], ["Ayaneo 2", "Ayaneo"], ["Ayaneo Air", "Ayaneo"],
        ["Ayaneo Kun", "Ayaneo"], ["Ayaneo Next", "Ayaneo"], ["Anbernic WIN600", "Anbernic"]]

AN = "Anbernic"
emu = [
 X("GP2X", "GP32 · GP2X Wiz · Caanoo", "GamePark's open Linux handheld line, the root of the homebrew emulation handheld.", "GamePark Holdings", "2005", W+"GP2X",
   [("GP32", "Game Park", "2001", "predecessor"),
    ("GP2X", "GamePark Holdings", "2005", "Linux"),
    ("GP2X Wiz", "GamePark Holdings", "", "successor"),
    ("Caanoo", "GamePark Holdings", "", "successor")]),
 X("Anbernic RG351", "", "Anbernic's early Linux emulation handheld series.", AN, "2020", W+"Anbernic",
   [("RG351P", AN, "2020", "Linux"), ("RG351M", AN, "2021", ""), ("RG351V", AN, "2021", "vertical")]),
 X("Anbernic RG353", "", "Anbernic's Android-and-Linux handheld series.", AN, "2022", W+"Anbernic",
   [("RG353P", AN, "2022", "Android 11 and Linux"), ("RG353M", AN, "2022", "Android 11 and Linux"), ("RG353V", AN, "2022", "vertical, Linux")]),
 X("Anbernic RG35XX", "", "Anbernic's low-cost Game Boy-styled Linux handheld series.", AN, "", W+"Anbernic",
   [("RG35XX", AN, "", "original"), ("RG35XX Plus", AN, "2023", "Linux"), ("RG35XX H", AN, "2024", "horizontal"),
    ("RG35XXSP", AN, "2024", "clamshell"), ("RG35XX Pro", AN, "2025", "")], "form factor"),
 X("Anbernic RG40XX", "", "Anbernic's 4-inch-screen Linux handheld series.", AN, "2024", W+"Anbernic",
   [("RG40XX H", AN, "2024", "horizontal"), ("RG40XX V", AN, "2024", "vertical")]),
 X("Anbernic RG Cube", "", "Anbernic's square-screen handheld series.", AN, "2024", W+"Anbernic",
   [("RG Cube", AN, "2024", ""), ("RG CubeXX", AN, "2024", "")]),
 X("Miyoo Mini", "Miyoo Mini Plus", "Pocket-sized Linux emulation handheld with a 4:3 screen, popular with custom firmware.", "Miyoo", "", "https://reviewed.com/gaming/content/miyoo-mini-plus-review",
   [("Miyoo Mini", "Miyoo", "", "2.8-inch screen"), ("Miyoo Mini Plus", "Miyoo", "", "3.5-inch 640×480 IPS")]),
 X("Retroid Pocket", "", "Retroid's Android emulation handheld line.", "Retroid", "", "https://thesixthaxis.com/2025/03/20/retroid-pocket-5-review-one-of-the-best-gaming-handhelds-you-can-buy",
   [("Retroid Pocket 4 Pro", "Retroid", "", ""), ("Retroid Pocket 5", "Retroid", "", "Snapdragon 865, Android 13"),
    ("Retroid Pocket 6", "Retroid", "", ""), ("Retroid Pocket Classic", "Retroid", "", ""),
    ("Retroid Pocket Flip 2", "Retroid", "", "clamshell"), ("Retroid Pocket G2", "Retroid", "", "")]),
]
emu_m = [["RG505", AN], ["RG556", AN], ["RG552", AN], ["RG503", AN], ["RG405M", AN], ["RG28XX", AN], ["RG34XX", AN],
 ["RG34XXSP", AN], ["RG Slide", AN], ["RG DS", AN], ["RG Vita", AN], ["Miyoo Flip", "Miyoo"], ["Miyoo A30", "Miyoo"],
 ["Odin 2 Portal", "AYN"], ["Thor", "AYN"], ["Trimui Smart Pro", "TrimUI"], ["TrimUI Smart Pro S", "TrimUI"],
 ["RGB30", "Powkiddy"], ["Dingoo A320", "Dingo Digital Technology"], ["GCW Zero", "Game Consoles Worldwide"],
 ["Pandora", "OpenPandora"], ["DragonBox Pyra", "DragonBox"], ["GPD XD", "GamePad Digital"],
 ["Pocket Air Mini", "Ayaneo"], ["Pocket S", "Ayaneo"], ["Pimax Portal", "Pimax"], ["Air X", "Mangmi"],
 ["TECNO Pocket Go", "Tecno Mobile"]]

kinds = [
 {"n": "Handheld console", "a": "portable console", "d": "Battery-powered handheld that plays games from changeable cartridges, cards, discs or downloads.",
  "s": "https://en.wikipedia.org/wiki/List_of_handheld_game_consoles", "x": handheld, "m": handheld_m},
 {"n": "Hybrid console", "a": "", "d": "Console that works both docked to a TV and as a handheld.",
  "s": "https://en.wikipedia.org/wiki/Video_game_console", "x": hybrid},
 {"n": "Handheld gaming PC", "a": "gaming handheld PC · PC handheld", "d": "Handheld x86 computer with built-in controls that runs PC games under Windows or SteamOS.",
  "t": ["Windows", "SteamOS", "with keyboard"], "s": W+"Steam_Deck", "x": pc, "m": pc_m},
 {"n": "Emulation handheld", "a": "retro handheld · emulator handheld", "d": "Low-cost Linux or Android handheld built to run emulators of older consoles from memory cards.",
  "t": ["Linux", "Android", "clamshell", "vertical", "horizontal"], "s": W+"Anbernic", "x": emu, "m": emu_m},
]

brands = [
 B("Milton Bradley", "United States", "", "Mainstream", "games & toys", "Games company that made the Microvision and sold the Vectrex.", W+"Microvision", ["Microvision"]),
 B("Nintendo", "Japan", "1889", "Mainstream", "consoles", "Japanese console maker of the Game Boy, DS, 3DS and Switch lines.", K, ["Game Boy", "Nintendo DS", "Nintendo Switch"]),
 B("Atari", "United States", "1972", "Mainstream", "consoles", "Video-game pioneer; made the Lynx handheld.", K, ["Atari Lynx"]),
 B("Sega", "Japan", "1960", "Mainstream", "consoles", "Japanese game company; made the Game Gear and Nomad.", K, ["Game Gear", "Sega Nomad"]),
 B("NEC", "Japan", "1899", "Mainstream", "electronics", "Japanese electronics group; made the TurboExpress.", K, ["TurboExpress"]),
 B("SNK", "Japan", "1978", "Premium", "arcade & Neo Geo", "Japanese arcade company behind the Neo Geo Pocket.", K, ["Neo Geo Pocket"]),
 B("Bandai", "Japan", "1950", "Mainstream", "toys", "Japanese toy company that made the WonderSwan.", K, ["WonderSwan"]),
 B("Sony", "Japan", "1946", "Mainstream", "consoles", "Japanese electronics group behind PSP and PS Vita.", K, ["PlayStation Portable", "PlayStation Vita"]),
 B("Blaze Entertainment", "United Kingdom", "", "Value", "retro cartridges", "British maker of the Evercade cartridge systems.", W+"Evercade", ["Evercade"]),
 B("Analogue", "Hong Kong", "2011", "Premium", "FPGA consoles", "Maker of premium FPGA consoles including the Pocket.", W+"Analogue_Pocket", ["Analogue Pocket"]),
 B("Panic", "United States", "", "Artisan & independent", "software & Playdate", "Software company that made the Playdate handheld.", W+"Playdate_(console)", ["Playdate"]),
 B("Valve", "United States", "1996", "Premium", "PC gaming", "PC game company behind Steam and the Steam Deck.", K, ["Steam Deck"]),
 B("ASUS", "Taiwan", "1989", "Mainstream", "PC hardware", "Taiwanese PC maker; ROG Ally handhelds under its Republic of Gamers brand.", K, ["ROG Ally"], ["Microsoft"]),
 B("Lenovo", "China", "1984", "Mainstream", "PCs", "PC maker behind the Legion Go handhelds.", K, ["Legion Go"]),
 B("GPD", "China", "", "Specialist", "handheld PCs", "GamePad Digital, Shenzhen maker of Windows handheld PCs.", W+"GPD_Win", ["GPD Win"]),
 B("GamePark Holdings", "South Korea", "", "Specialist", "Linux handhelds", "South Korean maker of the GP2X open handhelds.", W+"GP2X", ["GP2X"]),
 B("Anbernic", "China", "2017", "Value", "emulation handhelds", "Shenzhen maker of low-cost Linux and Android emulation handhelds.", W+"Anbernic", ["Anbernic RG35XX", "Anbernic RG353"], ["Miyoo", "Retroid"]),
 B("Miyoo", "China", "", "Value", "emulation handhelds", "Maker of the Miyoo Mini pocket emulation handhelds.", "https://reviewed.com/gaming/content/miyoo-mini-plus-review", ["Miyoo Mini"], ["Anbernic"]),
 B("Retroid", "China", "", "Value", "Android handhelds", "Maker of the Retroid Pocket Android handhelds.", "https://thesixthaxis.com/2025/03/20/retroid-pocket-5-review-one-of-the-best-gaming-handhelds-you-can-buy", ["Retroid Pocket"], ["Anbernic"]),
]

notes = ("Handheld console: 141 flat models reorganised into 17 handheld-family archetypes (Microvision to Playdate) with revisions as versions; 29 minor handhelds kept as flat models. "
 "Switch Lite moved into the Switch archetype under Hybrid console. PlayStation TV (moved from Home consoles shelf) added as a Vita version. "
 "New kind Handheld gaming PC: Steam Deck, ROG Ally line, Legion Go, GPD Win archetypes; Ayaneo PCs, MSI Claw A1M, Anbernic WIN600 as models. "
 "New kind Emulation handheld: GP2X lineage, Anbernic series (RG351, RG353, RG35XX, RG40XX, RG Cube), Miyoo Mini, Retroid Pocket; other Anbernic, AYN, TrimUI, Powkiddy, Dingoo, GCW Zero, Pandora/Pyra, Android handhelds as models. "
 "Old maker 'GoRetroid' normalised to Retroid. N-Gage left as flat model (Wikipedia N-Gage page is a disambiguation). Nothing dropped. "
 "Founding years for Retroid, Miyoo, GPD not confirmed, left blank.")

out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/E5/shelves/00_01.json'
t = p + '.tmp'; json.dump(out, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
print('ok')
