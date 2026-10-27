import json, os
W = 'https://en.wikipedia.org/wiki/'; K = 'knowledge'
def X(n, a, d, mk, y, s, v, dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [{"n": q[0], "mk": q[1], "y": q[2], "d": q[3]} for q in v], "dt": dt}
def B(n, c, f, seg, kf, d, s, sig=()):
    return {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "sig": list(sig), "s": s}
NI, SE = "Nintendo", "Sega"
disk = [
 X("Famicom Disk System", "FDS", "Famicom add-on that plays games on rewritable Disk Cards.", NI, "1986", W+"Famicom_Disk_System",
   [("Famicom Disk System", NI, "1986", "Japan"), ("Sharp Twin Famicom", "Sharp", "1986", "Famicom with built-in Disk System")], "Disk Card · Disk Writer kiosk"),
 X("CD-ROM²", "TurboGrafx-CD · Super CD-ROM²", "First CD-ROM add-on for a console, for the PC Engine.", "NEC", "1988", W+"TurboGrafx-16",
   [("CD-ROM²", "NEC", "1988", "Japan"), ("TurboGrafx-CD", "NEC", "1989", "North America"), ("Super CD-ROM²", "NEC", "1991", "more RAM")]),
 X("Mega-CD", "Sega CD", "CD-ROM add-on for the Mega Drive / Genesis.", SE, "1991", W+"Sega_CD",
   [("Mega-CD / Sega CD (Model 1)", SE, "1991", "front-loading tray, sits under the console"),
    ("Mega-CD 2 / Sega CD Model 2", SE, "1993", "top-loading, sits beside the console")], "model · region"),
 X("Jaguar CD", "", "CD-ROM add-on that sits on top of the Atari Jaguar.", "Atari", "1995", W+"Atari_Jaguar",
   [("Atari Jaguar CD", "Atari", "1995", "")]),
 X("64DD", "Nintendo 64DD", "Japan-only magnetic disk drive for the Nintendo 64, with the Randnet online service.", NI, "1999", W+"64DD",
   [("Nintendo 64DD", NI, "1999", "Japan only; built by Alps Electric")]),
]
upg = [
 X("Sega 32X", "Super 32X · Genesis 32X · Mega Drive 32X", "Cartridge-slot add-on that gives the Genesis 32-bit processors for 32X games.", SE, "1994", W+"32X",
   [("Genesis 32X", SE, "1994", "North America"), ("Super 32X", SE, "1994", "Japan"), ("Mega Drive 32X", SE, "1994", "Europe")], "region"),
 X("Expansion Pak", "NUS-007", "Nintendo 64 memory pak that adds 4 MB of RDRAM, replacing the Jumper Pak.", NI, "", "https://n64brew.dev/wiki/NUS-007",
   [("Expansion Pak version 1", NI, "", ""), ("Expansion Pak version 2", NI, "", "factory bodge"), ("Expansion Pak version 3", NI, "", "added resistor")]),
]
conv = [
 X("Power Base Converter", "Master System Converter · Mega Adapter", "Adapter that plugs into the Mega Drive / Genesis slot to play Master System cartridges and cards.", SE, "1990", "https://www.computinghistory.org.uk/det/6318/Sega-Master-System-Converter/",
   [("Power Base Converter", SE, "1990", "US"), ("Master System Converter", SE, "", "Europe"), ("Mega Adapter", SE, "", "Japan")], "region"),
 X("Super Game Boy", "", "SNES cartridge adapter that plays Game Boy games on a TV with colour palettes and borders.", NI, "1994", W+"Super_Game_Boy",
   [("Super Game Boy", NI, "1994", ""), ("Super Game Boy 2", NI, "1998", "Japan only, link port")]),
 X("Game Boy Player", "", "GameCube add-on that plays Game Boy, Game Boy Color and Game Boy Advance cartridges on a TV.", NI, "2003", W+"GameCube",
   [("Game Boy Player", NI, "2003", "")]),
]
conv_m = [["Hyperkin Hyperconvert 83", "Hyperkin"], ["Retro-Bit RetroGEN", "Retro-Bit"], ["HES Unidaptor", "Home Entertainment Suppliers"],
 ["Family Converter", "Honey Bee"], ["Game Key", "Horeleg"], ["Magic Key", "Magic Key"], ["Spica T89", "Spica"], ["Wu Ho Cassette Adaptor", "Wu Ho"],
 ["Mega Converter", ""], ["Mega Key 2", ""], ["Passport Plus III", ""], ["Programmable Universal Converter", ""], ["Super Key", ""], ["Tri-Star", ""], ["Universal Adaptor", ""]]
kinds = [
 {"n": "Disk or CD drive add-on", "a": "disk-drive add-on · CD add-on", "d": "Unit that adds a disk or CD drive to a console so it can play games on that medium.",
  "t": ["floppy/Disk Card", "CD-ROM", "magnetic disk"], "s": "https://en.wikipedia.org/wiki/Famicom_Disk_System", "x": disk},
 {"n": "Hardware upgrade add-on", "a": "32X type · memory pak", "d": "Unit that plugs into a console to add processor, graphics or memory hardware so it runs games made for the upgraded system.",
  "s": "https://en.wikipedia.org/wiki/32X", "x": upg, "m": [["High-Rez Pack", "Mad Catz"]]},
 {"n": "Cartridge converter", "a": "region converter · cartridge adapter", "d": "Unit that lets a console play cartridges of another system or region.",
  "t": ["other-system adapter", "region converter"], "s": "https://en.wikipedia.org/wiki/Super_Game_Boy", "x": conv, "m": conv_m},
]
brands = [
 B("Nintendo", "Japan", "1889", "Mainstream", "consoles", "Japanese console maker; made the Disk System, 64DD, Expansion Pak and Game Boy adapters.", K, ["Famicom Disk System", "Super Game Boy"]),
 B("Sega", "Japan", "1960", "Mainstream", "consoles", "Japanese game company; made the Mega-CD, 32X and Power Base Converter.", K, ["Mega-CD", "Sega 32X"]),
 B("NEC", "Japan", "1899", "Mainstream", "electronics", "Japanese electronics group that made the PC Engine CD-ROM².", K, ["CD-ROM²"]),
 B("Atari", "United States", "1972", "Mainstream", "consoles", "Video-game pioneer; made the Jaguar CD.", K, ["Jaguar CD"]),
]
notes = ("Disk add-ons: 6 old models became 5 archetypes (FDS, CD-ROM², Mega-CD, Jaguar CD, 64DD) with model revisions as versions. "
 "Hardware upgrade: 32X and Expansion Pak archetypes, Mad Catz High-Rez Pack kept as model; duplicate 'Sega Mega-CD' dropped here as the brief says (kept in Disk or CD drive add-on). "
 "Cartridge converter: Power Base Converter (Master System Converter), Super Game Boy (+SGB2) and Game Boy Player archetypes; 15 third-party and maker-less converters kept as models.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/E5/shelves/00_03.json'
t = p + '.tmp'; json.dump(out, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
