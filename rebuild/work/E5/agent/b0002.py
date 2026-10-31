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

NI, SE, AT, AG = "Nintendo", "Sega", "Atari", "AtGames"
pnp = [
 X("Magnavox Odyssey", "Odisea", "First home video game console, with plug-in game cards that switch built-in circuits and TV overlays.", "Magnavox", "1972", W+"Magnavox_Odyssey",
   [("Magnavox Odyssey", "Magnavox", "1972", "US; 12 bundled games"),
    ("Magnavox Odyssey (UK)", "Magnavox", "1973", "different games")]),
 X("Home Pong", "Sears Tele-Games Pong", "Atari's dedicated home version of its Pong arcade game.", AT, "1975", W+"Pong",
   [("Tele-Games Pong", "Sears", "1975", "Sears exclusive"),
    ("Pong (home version)", AT, "1976", "Atari-branded"),
    ("Super Pong", AT, "", "follow-up"),
    ("Pong Doubles / Pong IV", AT, "", "four-player follow-up")]),
 X("Color TV-Game", "", "Nintendo's first home consoles, each with its games built in.", NI, "1977", W+"Color_TV-Game",
   [("Color TV-Game 6", NI, "1977", ""), ("Color TV-Game 15", NI, "1977", ""),
    ("Color TV-Game Racing 112", NI, "1978", ""), ("Color TV-Game Block Kuzushi", NI, "1979", ""),
    ("Computer TV-Game", NI, "1980", "")]),
 X("Activision 10-in-1", "Activision TV Games", "One of the first licensed plug-and-play TV game controllers.", "Toymax", "2001", W+"Handheld_TV_game",
   [("Activision 10-in-1 TV Game", "Toymax", "2001", "joystick"), ("Activision TV Games gamepad", "Toymax", "", "")]),
 X("Plug It In & Play TV Games", "Jakks TV Games", "Jakks Pacific's line of joystick-shaped TV games with licensed arcade and console ports.", "Jakks Pacific", "2002", W+"Plug-%26-Play_TV_Games",
   [("Atari Classic 10-in-1 TV", "Jakks Pacific", "2002", "first big hit"),
    ("Atari 10 in 1 TV Games", "Jakks Pacific", "", ""),
    ("Atari Joystick Controller TV Video Game System", "Jakks Pacific", "", "CX40 joystick shape"),
    ("Atari Paddle Controller", "Jakks Pacific", "", ""),
    ("Namco Plug and Play (Pac-Man)", "Jakks Pacific", "", ""),
    ("Namco Ms. Pac-Man and Friends", "Jakks Pacific", "", ""),
    ("Namco Ms. Pac-Man Super Gamekey Mega Pack", "Jakks Pacific", "", "GameKey expansion"),
    ("Super Pac-Man Collection", "Jakks Pacific", "", ""),
    ("Activision TV Games joystick controller", "Jakks Pacific", "", ""),
    ("Capcom 3-in-1", "Jakks Pacific", "", ""),
    ("Retro Arcade featuring Pac-Man", "Jakks Pacific", "", ""),
    ("Retro Arcade featuring Space Invaders", "Jakks Pacific", "", ""),
    ("Arcade Gold featuring Pac-Man", "Jakks Pacific", "", "")], "licence · controller shape"),
 X("Radica Play TV", "Play TV", "Radica's plug-and-play TV games, including motion games and Sega collections.", "Radica Games", "2003", W+"Handheld_TV_game",
   [("Play TV", "Radica Games", "2003", "motion-control titles"),
    ("Sega Mega Drive/Genesis PlayTV Legends", "Radica Games", "2004", "Sega collection"),
    ("Sega Mega Drive/Genesis PlayTV Legends Volume II", "Radica Games", "", "")]),
 X("Atari Flashback", "", "Licensed Atari 2600-style console with built-in games.", AT, "2004", W+"Atari_Flashback",
   [("Atari Flashback", "Legacy Engineering Group", "2004", ""),
    ("Atari Flashback 2", "Legacy Engineering Group", "2005", ""),
    ("Atari Flashback 2+", AT, "2010", ""),
    ("Atari Flashback 3", AG, "2011", ""), ("Atari Flashback 4", AG, "2012", ""),
    ("Atari Flashback 5", AG, "2014", ""), ("Atari Flashback 6", AG, "2015", ""),
    ("Atari Flashback 7", AG, "2016", ""), ("Atari Flashback 8", AG, "2017", "Gold editions"),
    ("Atari Flashback 9", AG, "2018", "Gold edition"), ("Atari Flashback X", AG, "2019", ""),
    ("Atari Flashback 50th Anniversary Edition", AG, "2022", "limited"),
    ("Atari Flashback 12 Gold", AG, "2023", "limited")], "game count · Gold edition"),
 X("Nintendo Classic Mini", "NES Classic Edition · Famicom Mini · SNES Classic", "Nintendo's official miniature replicas of the NES and SNES with built-in games and HDMI.", NI, "2016", W+"NES_Classic_Edition",
   [("NES Classic Edition", NI, "2016", "North America; relaunched 2018"),
    ("Nintendo Classic Mini: Family Computer", NI, "2016", "Japan"),
    ("Super NES Classic Edition", NI, "2017", ""),
    ("Nintendo Classic Mini: Super Famicom", NI, "", "Japan")], "region"),
 X("PlayStation Classic", "", "Sony's miniature PlayStation with 20 built-in games.", "Sony", "2018", W+"PlayStation_Classic",
   [("PlayStation Classic", "Sony", "2018", "20 games")]),
 X("Neo Geo Mini", "NEOGEO mini", "SNK's small arcade-cabinet-shaped Neo Geo with built-in screen and games.", "SNK", "2018", W+"Neo_Geo_(system)",
   [("NEOGEO mini", "SNK", "2018", "Japan"), ("NEOGEO mini International", "SNK", "2018", "")]),
 X("Mega Drive Mini", "Sega Genesis Mini", "Sega's official miniature Mega Drive with built-in games.", SE, "2019", W+"Sega_Genesis",
   [("Sega Mega Drive Mini / Genesis Mini", SE, "2019", "40 games"),
    ("Sega Mega Drive Mini 2 / Genesis Mini 2", SE, "", "successor")], "region"),
 X("PC Engine Mini", "TurboGrafx-16 Mini · PC Engine CoreGrafx Mini", "Konami's miniature PC Engine with built-in games, co-developed with M2.", "Konami", "2020", W+"TurboGrafx-16_Mini",
   [("PC Engine Mini", "Konami", "2020", "Japan"), ("TurboGrafx-16 Mini", "Konami", "2020", "North America"),
    ("PC Engine CoreGrafx Mini", "Konami", "2020", "Europe")], "region"),
 X("Astro City Mini", "", "Sega's miniature Astro City arcade cabinet with built-in screen and 37 games.", SE, "2020", "https://sega.fandom.com/wiki/Astro_City_Mini",
   [("Astro City Mini", SE, "2020", "Japan, 60th anniversary"), ("Astro City Mini V", SE, "", "vertical-screen follow-up announced 2021")]),
 X("THEC64", "THEC64 Mini · THEA500 Mini · THE400 Mini", "Retro Games Ltd.'s licensed replicas of classic home computers that run built-in and loaded games.", "Retro Games Ltd.", "2018", "https://www.c64-wiki.com/wiki/Retro_Games_Ltd.",
   [("THEC64 Mini", "Retro Games Ltd.", "2018", "miniature keyboard"),
    ("THEC64 (full-size)", "Retro Games Ltd.", "2019", "working keyboard"),
    ("THEA500 Mini", "Retro Games Ltd.", "", "Amiga 500 replica"),
    ("THE400 Mini", "Retro Games Ltd.", "", "Atari 400 replica")]),
]
pnp_m = [["Pac-Man Collection", "Arcade1Up"], ["Legends Flashback", AG], ["Mega Drive Twin Pads", AG],
 ["ColecoVision Flashback", AG], ["Intellivision Flashback", ""], ["Atari Flashback 64", AT], ["Atari Gamestation Pro", AT],
 ["Arcade Motion Dual", AT], ["Atari 2600 Plug & Play joystick", AT], ["Pac-Man Connect and Play", "Bandai Namco Entertainment"],
 ["Capcom Home Arcade", "Capcom"], ["Mega Man Collection", "Capcom"], ["Konami Collector's Series: Arcade Advanced", "Konami"],
 ["Midway Arcade Classics Vol. 1", "MSI Entertainment"], ["Arcade Legends: Space Invaders", "Majesco Entertainment"],
 ["TV Arcade", "Majesco Entertainment"], ["Intellivision 10 TV Play Power", "Techno Source"],
 ["Intellivision 10 2nd Edition TV Play Power", "Techno Source"], ["Intellivision 25 TV Play Power", "Techno Source"],
 ["Intellivision X2 15", "Techno Source"], ["Master System Evolution", "Tectoy"], ["Retro-Bit Generations", "Retro-Bit"],
 ["Super Retro-Cade", "Retro-Bit"], ["NEOGEO Arcade Stick Pro", "SNK"], ["Taito Egret II Mini", "Taito"],
 ["Zemmix Mini", "Team-Neo"], ["Zemmix Super Mini", "Team-Neo"], ["DanceDanceRevolution Classic Mini", "Zuiki"],
 ["X68000 Z", "Zuiki"], ["X68000 Z 2", "Zuiki"], ["PasocomMini PC-8001", "HAL Laboratory"], ["PasocomMini MZ-80C", "HAL Laboratory"],
 ["PasocomMini PC-8801mkIISR", "Dempa Micomsoft"], ["C64 Direct-to-TV", "Toy:Lobster"], ["ZX Spectrum Vega", ""],
 ["Vectrex Mini", ""], ["Flynn's Generation", ""], ["Sport Vii", "JungleTac"], ["Xavix PORT", "SSD Company"]]

lcd = [
 X("Game & Watch Silver", "", "First Game & Watch series, with silver faceplates.", NI, "1980", W+"Game_%26_Watch", []),
 X("Game & Watch Gold", "", "Second Game & Watch series with gold faceplates.", NI, "1981", W+"Game_%26_Watch", []),
 X("Game & Watch Wide Screen", "", "Game & Watch series with a wider screen.", NI, "1981", W+"Game_%26_Watch", []),
 X("Game & Watch Multi Screen", "", "Clamshell Game & Watch series with two screens, vertical and horizontal.", NI, "1982", W+"Game_%26_Watch",
   [("Vertical Multi Screen", NI, "1982", ""), ("Horizontal Multi Screen", NI, "1983", "")]),
 X("Game & Watch New Wide Screen", "", "Long-running wide-screen Game & Watch series.", NI, "1982", W+"Game_%26_Watch", []),
 X("Game & Watch Panorama", "", "Game & Watch series with a folding mirror that projects a colour image.", NI, "1983", W+"Game_%26_Watch", []),
 X("Game & Watch Super Color", "", "Game & Watch series with colour-printed screens.", NI, "1984", W+"Game_%26_Watch", []),
 X("Game & Watch Micro Vs. System", "", "Two-player Game & Watch with detachable controllers.", NI, "1984", W+"Game_%26_Watch", []),
 X("Game & Watch Crystal Screen", "", "Game & Watch series with a transparent screen.", NI, "1986", W+"Game_%26_Watch", []),
 X("Game & Watch (2020 revival)", "", "Modern colour-screen Game & Watch units with built-in Nintendo games.", NI, "2020", W+"Game_%26_Watch",
   [("Game & Watch: Super Mario Bros.", NI, "2020", ""), ("Game & Watch: The Legend of Zelda", NI, "2021", "")]),
 X("Tiger handheld LCD games", "Tiger LCD", "Tiger Electronics' cheap single-game LCD handhelds, often licensed from films and games.", "Tiger Electronics", "", W+"Tiger_Electronics",
   [("Electronic Bowling", "Tiger Electronics", "", "early hit"), ("Licensed LCD games", "Tiger Electronics", "", "1990s film and game licences"),
    ("Barcodzz", "Tiger Electronics", "1994", "barcode-scanning battles"), ("Super Data Blasters", "Tiger Electronics", "1995", "sports with stats")]),
 X("Atari Flashback Portable", "", "Handheld version of the Atari Flashback with built-in 2600 games.", AG, "2016", W+"Atari_Flashback",
   [("Atari Flashback Portable", AG, "2016", ""), ("Atari Flashback Portable 2.0", AT, "", ""),
    ("Atari Flashback Portable 3.0", AT, "", ""), ("Atari Flashback Portable 4.0", AT, "", "")]),
 X("Game Gear Micro", "", "Tiny Game Gear replica with four built-in games per colour version.", SE, "2020", W+"Game_Gear",
   [("Game Gear Micro", SE, "2020", "four colour versions")], "colour"),
 X("Super Pocket", "", "HyperMegaTech!'s Game Boy-styled handheld with built-in arcade games that also takes Evercade cartridges.", "Blaze Entertainment", "2023", W+"Super_Pocket",
   [("Super Pocket Capcom Edition", "HyperMegaTech!", "2023", ""), ("Super Pocket Taito Edition", "HyperMegaTech!", "2023", ""),
    ("Super Pocket Technos Edition", "HyperMegaTech!", "", ""), ("Super Pocket Data East Edition", "HyperMegaTech!", "", ""),
    ("Super Pocket Atari Edition", "HyperMegaTech!", "2024", ""), ("Super Pocket Neo Geo Edition", "HyperMegaTech!", "2025", ""),
    ("Super Pocket Rare Edition", "HyperMegaTech!", "2026", ""), ("Super Pocket Activision Edition", "HyperMegaTech!", "2026", "")], "licence edition"),
]
lcd_m = [["Game & Watch Ball", NI], ["Game & Watch Balloon Fight", NI], ["Game & Watch Chef", NI], ["Game & Watch Climber", NI],
 ["Game & Watch Oil Panic", NI], ["Mattel Handheld Games re-release series", "Mattel"], ["Sega Genesis Ultimate Portable Game Player", AG],
 ["Atari Pocket Player", "Chromatic"], ["Atari Gamestation Go", "My Arcade"], ["The Oregon Trail Handheld", "Retro-Bit"],
 ["Atari 2600 Tiny Arcade", "Super Impulse"], ["Atari Micro Player", ""], ["Go Retro! Portable", ""]]

table = [
 X("Coleco Mini-Arcade", "Coleco tabletop", "Coleco's tabletop cabinets of licensed arcade games with VFD screens, revived with LCDs in 2019.", "Coleco", "1981", "https://toytales.ca/mini-arcade-games-from-coleco",
   [("Coleco Pac-Man", "Coleco", "", ""), ("Coleco Ms. Pac-Man", "Coleco", "", ""), ("Coleco Zaxxon", "Coleco", "", "")]),
 X("Game & Watch Table Top", "", "Tabletop Game & Watch series with a colour image projected by a mirror.", NI, "1983", W+"Game_%26_Watch",
   [("Table Top Donkey Kong Jr.", NI, "", ""), ("Table Top Mario's Cement Factory", NI, "", ""),
    ("Table Top Popeye", NI, "", ""), ("Table Top Snoopy", NI, "", "")]),
]
table_m = [["Bandai Gunfighter", "Bandai"], ["Bandai Zaxxon (FL Zaxxon)", "Bandai"], ["Epoch Astro Wars", "Epoch Co."],
 ["Epoch Star Force", "Epoch Co."], ["Gakken Puck Monster", "Gakken"], ["Gakken Super Puck Monster", "Gakken"],
 ["Grandstand Firefox F-7", "Grandstand"], ["Grandstand Scramble", "Grandstand"], ["Tomy Demon Driver", "Tomy"], ["Tomy Tron", "Tomy"]]

kinds = [
 {"n": "Plug-and-play & mini console", "a": "dedicated console · mini console · TV game",
  "d": "Console with its games built in that plugs into a TV, from Pong-era machines to official mini replicas.",
  "t": ["Pong-era dedicated", "TV game joystick", "official mini", "computer mini"],
  "s": "https://en.wikipedia.org/wiki/Video_game_console", "x": pnp, "m": pnp_m},
 {"n": "LCD handheld game", "a": "LCD game · electronic handheld",
  "d": "Handheld with its game or games built in on its own screen.",
  "s": "https://en.wikipedia.org/wiki/Game_&_Watch", "x": lcd, "m": lcd_m},
 {"n": "Tabletop electronic game", "a": "tabletop mini-arcade",
  "d": "Game machine with its game built in and its own screen (VFD, LCD or LED), made to stand on a table, not held and not linked to a TV.",
  "t": ["VFD", "LCD", "LED"], "s": "https://en.wikipedia.org/wiki/Grandstand_(game_manufacturer)", "x": table, "m": table_m},
]

brands = [
 B("Magnavox", "United States", "", "Mainstream", "consumer electronics", "Electronics brand that sold the first home console, the Odyssey.", K, ["Magnavox Odyssey"], ["Philips"]),
 B("Atari", "United States", "1972", "Mainstream", "consoles", "Video-game pioneer behind home Pong and the Flashback licences.", K, ["Home Pong", "Atari Flashback"], ["AtGames"]),
 B("Nintendo", "Japan", "1889", "Mainstream", "consoles", "Japanese console maker of the Color TV-Game, Game & Watch and Classic Mini lines.", K, ["Color TV-Game", "Nintendo Classic Mini", "Game & Watch Silver"]),
 B("Toymax", "United States", "", "Mainstream", "toys", "Toy company that made the Activision 10-in-1 TV game.", W+"Handheld_TV_game", ["Activision 10-in-1"]),
 B("Jakks Pacific", "United States", "", "Mainstream", "toys & TV games", "Toy company behind the Plug It In & Play TV Games line.", W+"Plug-%26-Play_TV_Games", ["Plug It In & Play TV Games"]),
 B("Radica Games", "", "", "Mainstream", "electronic games", "Maker of the Play TV plug-and-play line.", W+"Handheld_TV_game", ["Radica Play TV"]),
 B("AtGames", "", "", "Value", "licensed retro consoles", "Maker of licensed Atari and Sega plug-and-play consoles.", W+"Atari_Flashback", ["Atari Flashback", "Atari Flashback Portable"], ["Atari"]),
 B("Sony", "Japan", "1946", "Mainstream", "consoles", "Japanese electronics group behind PlayStation.", K, ["PlayStation Classic"]),
 B("SNK", "Japan", "1978", "Premium", "arcade & Neo Geo", "Japanese arcade company behind the Neo Geo.", K, ["Neo Geo Mini"]),
 B("Sega", "Japan", "1960", "Mainstream", "consoles", "Japanese game company; makes the Mega Drive Mini and Astro City Mini.", K, ["Mega Drive Mini", "Astro City Mini", "Game Gear Micro"]),
 B("Konami", "Japan", "1969", "Mainstream", "games", "Japanese game publisher that owns Hudson's PC Engine properties.", K, ["PC Engine Mini"]),
 B("Retro Games Ltd.", "United Kingdom", "2015", "Specialist", "computer replicas", "Luton firm making licensed replicas of classic home computers.", "https://www.c64-wiki.com/wiki/Retro_Games_Ltd.", ["THEC64"]),
 B("Tiger Electronics", "United States", "1978", "Mainstream", "LCD games", "Toy maker known for handheld LCD games; part of Hasbro since 1998.", W+"Tiger_Electronics", ["Tiger handheld LCD games"]),
 B("Blaze Entertainment", "United Kingdom", "", "Value", "retro cartridges", "British maker of Evercade and the HyperMegaTech! Super Pocket.", W+"Super_Pocket", ["Super Pocket"]),
 B("Coleco", "United States", "", "Mainstream", "toys & consoles", "Toy maker of ColecoVision and the tabletop Mini-Arcades.", K, ["Coleco Mini-Arcade"]),
]

notes = ("Plug-and-play & mini console: 92 old models plus 6 moved in from Home consoles (THE400 Mini, THEA500 Mini, THEC64 Mini, X68000 Z, Sport Vii, Xavix PORT) organised into 14 archetypes "
 "(Pong-era Magnavox Odyssey, Home Pong, Color TV-Game; TV-game lines Toymax, Jakks, Radica, Atari Flashback; official minis from Nintendo, Sony, SNK, Sega, Konami, Retro Games) with 39 smaller lines as flat models. "
 "LCD handheld game: Game & Watch series as archetypes (Silver to Crystal Screen plus the 2020 revival; old ranges became archetypes), Tiger LCD, Atari Flashback Portable, Game Gear Micro, Super Pocket; individual old G&W titles kept as models without assigning series. "
 "Tabletop: Coleco Mini-Arcade and Game & Watch Table Top archetypes, others as models. Nothing dropped. "
 "Old maker 'Legacy Engineering Group' kept as version maker. Vectrex Mini, ZX Spectrum Vega, Flynn's Generation still have no maker in old data.")

out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/E5/shelves/00_02.json'
t = p + '.tmp'; json.dump(out, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
print(len(pnp_m), len(lcd_m), len(table_m))
