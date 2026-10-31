import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def X(n, d, mk, y, s, v=(), a="", dt=""):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [{"n": a_, "mk": b, "y": c, "d": e} for a_, b, c, e in v]}
    if dt: x["dt"] = dt
    return x
def B(n, c, f, seg, kf, d, s, sig=()):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    if sig: b["sig"] = list(sig)
    return b
WP = "https://en.wikipedia.org/wiki/"
LIST = WP + "List_of_Sony_Walkman_products"
S = "Sony"
kinds = [
 {"n": "Portable cassette player", "a": "Walkman · personal stereo", "d": "Battery-powered personal player for compact cassettes, listened to through headphones; hi-fi tape decks are a separate kind.",
  "t": ["playback only", "recorder", "with radio", "auto-reverse"], "s": "https://apos.audio/collections/brand-spotlight-fiio",
  "x": [
   X("Sony Walkman (cassette)", "The first low-cost personal stereo; its name became the generic word for the type.", S, "1979", WP + "Walkman",
     [("TPS-L2", S, "1979", "original, metal case"), ("WM-2", S, "1981", ""), ("WM-10", S, "1983", "smallest cassette Walkman"),
      ("WM-FX513", S, "1993", ""), ("WM-EX102", S, "1994", ""), ("WM-EX670", S, "1999", "")], a="Soundabout · Stowaway · Freestyle",
     dt="playback or record · radio · Dolby · auto-reverse · colour"),
   X("Sony Walkman Professional WM-D6 / WM-D6C", "Metal-cased portable cassette recorder with hi-fi deck performance, used for field and radio recording.", S, "1982", "https://www.stereonet.com/uk/features/past-masters-sony-wm-d6c",
     [("WM-D6", S, "1982", "first Walkman Professional"), ("WM-D6C", S, "1984", "line in/out, Dolby B and C; made to 2003")]),
  ]},
 {"n": "Portable CD player", "a": "Discman · CD Walkman", "d": "Battery-powered personal player for compact discs, listened to through headphones; hi-fi CD players are a separate kind.",
  "t": ["anti-skip", "with MP3/ATRAC playback", "video CD"], "s": "https://spencertified.com/collections/cassette-player-deck-systems/speakers",
  "x": [
   X("Sony Discman / CD Walkman", "First portable CD player, about half the price of Sony's first home CD player; renamed CD Walkman by 2000.", S, "1984", WP + "Discman",
     [("D-50 / D-5", S, "1984", "original, sold as 'CD Compact Player'"), ("D-145", S, "1995", ""), ("D-E330", S, "2002", "CD Walkman"),
      ("D-NE1", S, "2003", "early ATRAC CD Walkman"), ("D-NE301", S, "2004", ""), ("D-NE920", S, "2004", ""), ("D-NE830", S, "2005", "")]),
  ],
  "m": [["FiiO DM15 R2R CD Player", "FiiO"]]},
 {"n": "Portable MiniDisc player", "a": "MiniDisc Walkman · MD recorder", "d": "Battery-powered personal player or recorder for MiniDisc, a rewritable magneto-optical disc format sold 1992–2013.",
  "t": ["player", "recorder", "NetMD", "Hi-MD"], "s": WP + "MiniDisc",
  "x": [
   X("Sony MiniDisc Walkman (MZ series)", "Sony's MiniDisc players and recorders, from the first MZ-1 to the Hi-MD MZ-RH1.", S, "1992", LIST,
     [("MZ-1", S, "1992", "first MiniDisc recorder"), ("MZ-2P", S, "1992", "player"), ("MZ-R2", S, "1993", ""), ("MZ-R900", S, "2000", ""),
      ("MZ-R909", S, "2001", ""), ("MZ-NH1", S, "2004", "Hi-MD"), ("MZ-RH1", S, "2006", "Hi-MD; last MiniDisc Walkman, made to 2011")],
     dt="player or recorder · NetMD · Hi-MD · colour"),
  ]},
 {"n": "MP3 player", "a": "digital audio player · DAP · portable media player", "d": "Portable device sold mainly to play stored or streamed music, with no calling.",
  "t": ["flash memory", "hard drive", "hi-res DAP", "Android DAP"], "s": "https://apos.audio/collections/brand-spotlight-fiio",
  "x": [
   X("Rio PMP300", "First commercially successful portable MP3 player; survived an RIAA lawsuit.", "Diamond Multimedia", "1998", WP + "Rio_PMP300",
     [("PMP300", "Diamond Multimedia", "1998", "32 MB with SmartMedia slot"), ("PMP300 64 MB", "Diamond Multimedia", "", "translucent green")]),
   X("Creative Nomad Jukebox", "Hard-drive music player using laptop drives; the line became the Creative Zen.", "Creative", "2000", WP + "Creative_Nomad",
     [("Nomad", "Creative", "", "flash, rebadged Samsung Yepp YP-D40"), ("Nomad Jukebox", "Creative", "2000", ""), ("Nomad Jukebox 2", "Creative", "", "USB 2.0"),
      ("Nomad Jukebox 3", "Creative", "", "FireWire"), ("Nomad Jukebox Zen", "Creative", "", "first Zen")]),
   X("Apple iPod", "Apple's music player line, 2001–2022, from the hard-drive click-wheel original to the touchscreen iPod touch.", "Apple", "2001", WP + "IPod",
     [("iPod (classic)", "Apple", "2001", "hard drive; 6 generations, to 2014"), ("iPod mini", "Apple", "2004", "Microdrive; 2 generations"),
      ("iPod photo", "Apple", "2004", "colour screen"), ("iPod shuffle", "Apple", "2005", "no screen; 4 generations"),
      ("iPod nano", "Apple", "2005", "7 generations, to 2017"), ("iPod touch", "Apple", "2007", "7 generations, to 2022")],
     dt="generation · capacity · colour"),
   X("iRiver H100 series", "Hard-drive players with optical output and FM tuner, a favourite for Rockbox firmware.", "iRiver", "2003", WP + "IRiver_H100_series",
     [("iHP-100 / H110", "iRiver", "2003", "10 GB"), ("iHP-115 / H115", "iRiver", "2003", "15 GB"), ("iHP-120 / H120", "iRiver", "2003", "20 GB"), ("iHP-140 / H140", "iRiver", "2003", "40 GB")]),
   X("Microsoft Zune", "Microsoft's iPod rival with wireless sharing, sold 2006–2011.", "Microsoft", "2006", WP + "Zune",
     [("Zune 30", "Microsoft", "2006", "made with Toshiba"), ("Zune 80", "Microsoft", "2007", ""), ("Zune 4 / 8", "Microsoft", "2007", "flash"), ("Zune HD", "Microsoft", "2009", "touchscreen")]),
   X("Sony Walkman (digital, NW)", "Sony's flash-memory Walkman players, now high-resolution players in A, ZX and WM1 series.", S, "1999", LIST,
     [("NW-MS7", S, "1999", "first digital Walkman"), ("NW-A1000", S, "2005", "A series begins"), ("NW-WM1A / NW-WM1Z", S, "2016", "Signature series"),
      ("NW-ZX507", S, "2019", ""), ("NW-A100", S, "2019", ""), ("NW-WM1AM2 / NW-WM1ZM2", S, "2022", ""),
      ("NW-A306", S, "", ""), ("NW-ZX707", S, "", ""), ("NW-WM1AM3 / NW-WM1ZM3", S, "", ""), ("NW-ZX900", S, "", "")]),
   X("Astell&Kern players", "Korean high-resolution players that started the premium DAP market with the AK100.", "Astell&Kern", "2013", WP + "Astell_%26_Kern",
     [("AK100", "Astell&Kern", "2013", "first model"), ("AK120", "Astell&Kern", "2013", ""), ("AK240", "Astell&Kern", "2014", ""),
      ("A&ultima SP1000", "Astell&Kern", "2017", "flagship"), ("KANN", "Astell&Kern", "2017", ""), ("A&futura SE100", "Astell&Kern", "2018", ""),
      ("A&ultima SP2000", "Astell&Kern", "2019", ""), ("A&ultima SP3000", "Astell&Kern", "2022", ""), ("SP3000M", "Astell&Kern", "", ""),
      ("SE300", "Astell&Kern", "", ""), ("PD10", "Astell&Kern", "", ""), ("PD5", "Astell&Kern", "", "")]),
   X("FiiO X and M series", "Chinese hi-res players moving from the X series to Android-based M series.", "FiiO", "2013", WP + "Fiio",
     [("X3", "FiiO", "2013", ""), ("X5", "FiiO", "2014", ""), ("X7", "FiiO", "2015", "modular, Android"), ("M11", "FiiO", "2019", ""), ("M21", "FiiO", "", "")]),
   X("Shanling M series", "Portable hi-fi players from a Chinese hi-fi maker, from the M3 to the tiny M0.", "Shanling", "2014", "https://store.shanling.com/company-profile.html",
     [("M3", "Shanling", "2014", "first portable player"), ("M2", "Shanling", "2015", ""), ("M5", "Shanling", "2016", "flagship"), ("M0", "Shanling", "2018", "")]),
  ],
  "m": [["Shanling Q2", "Shanling"]]},
 {"n": "Boombox", "a": "ghetto blaster · radio-cassette", "d": "Portable radio-cassette or CD system with built-in speakers and a carry handle.",
  "t": ["radio-cassette", "double cassette", "CD", "Bluetooth/DAB"], "s": "https://www.sony.com/en-sa/electronics/boomboxes/cfd-s70/buy/cfd-s70-bc-ea6",
  "x": [
   X("Philips Radiorecorder", "Philips, inventor of the compact cassette, made the first boombox.", "Philips", "1966", WP + "Boombox",
     [("Norelco 22RL962", "Philips", "", "mid-1960s, Norelco brand")]),
   X("Sharp GF-777 \"Searcher\"", "Huge six-speaker radio-cassette called the king of the boomboxes, used in music battles.", "Sharp", "", "https://www.thehenryford.org/collections/explore/articles/boomboxes-at-the-henry-ford",
     [("GF-9494 \"Ghetto Blaster\"", "Sharp", "1980", ""), ("GF-777", "Sharp", "", "four woofers"), ("GF-7600", "Sharp", "", "carried in Say Anything...")]),
   X("JVC RC-M90", "One of the 'boombox kings' used in music battles.", "JVC", "", WP + "Boombox",
     [("RC-550 \"El Diablo\"", "JVC", "", "from The Henry Ford"), ("838 BiPhonic", "JVC", "", "from The Henry Ford")]),
   X("Panasonic RX-5350", "Upside-down-layout radio-cassette with two 8-inch speakers and 5-band equaliser.", "Panasonic", "1983", "https://classicboombox.com/panasonic-rx-5350",
     [("RX-5350", "Panasonic", "1983", "also sold as National")]),
   X("Conion C-100F", "Onkyo off-brand radio-cassette carried by Schoolly D.", "Conion", "", WP + "Boombox", []),
   X("Sony CD boombox", "Sony's CD radio-cassette and CD radio portables.", S, "", WP + "Boombox",
     [("CFD-S35CP", S, "2005", "CD and cassette"), ("ZS-PS50", S, "", "CD, FM, USB MP3"), ("CFD-S70", S, "", "")]),
  ],
  "m": [["GPO Brooklyn", "GPO"]]},
 {"n": "Audio figure", "a": "Toniebox · Tonies · Yoto card · audio card player", "d": "Figure or card that plays its stored content when placed in its children's player; the screen-free player belongs here too.",
  "tg": ["baby"], "t": ["figure", "card", "player"], "s": "https://us.tonies.com/pages/tonieboxes",
  "x": [
   X("Toniebox and Tonies", "Cube player for children that plays a story or songs when a rubber figure is set on top.", "Tonies", "2016", WP + "Tonies",
     [("Toniebox", "Tonies", "2016", "launched with 14 Tonies"), ("Creative Tonies", "Tonies", "", "blank, up to 90 minutes own content"), ("Tonie Clip", "Tonies", "2019", "links an existing toy")]),
   X("Yoto Player", "Screen-free children's speaker that plays audio cards.", "Yoto", "", "https://www.actoncapital.com/portfolio/yoto", []),
  ],
  "r": [["Classic Tonies", "Tonies"], ["Creative Tonies", "Tonies"], ["Cuddle Tonies", "Tonies"], ["My First Tonies", "Tonies"], ["Night Light Tonies", "Tonies"], ["Pocket Tonies", "Tonies"]]},
]
K = "knowledge"
brands = [
 B("Sony", "Japan", "1946", "Mainstream", "Walkman", "Japanese electronics maker whose Walkman created the personal-stereo market.", K, ["Sony Walkman (cassette)", "Sony Discman / CD Walkman", "Sony MiniDisc Walkman (MZ series)"]),
 B("Apple", "United States", "1976", "Premium", "iPod", "American computer and phone maker; its iPod led the MP3-player era.", K, ["Apple iPod"]),
 B("Diamond Multimedia", "United States", "", "Mainstream", "Rio players", "PC hardware maker that launched the Rio MP3 players.", WP + "Rio_PMP300", ["Rio PMP300"]),
 B("Creative", "Singapore", "1981", "Mainstream", "Sound Blaster, Zen", "Singapore audio maker of Nomad and Zen players.", K, ["Creative Nomad Jukebox"]),
 B("iRiver", "South Korea", "", "Mainstream", "MP3 players", "Korean maker of MP3 players and founder of Astell&Kern.", WP + "IRiver_H100_series", ["iRiver H100 series"]),
 B("Microsoft", "United States", "1975", "Mainstream", "software, Zune", "American software company that sold Zune players 2006–2011.", K, ["Microsoft Zune"]),
 B("Astell&Kern", "South Korea", "2013", "Professional & flagship", "hi-res players", "Korean premium portable-player brand founded by iRiver.", WP + "Astell_%26_Kern", ["Astell&Kern players"]),
 B("FiiO", "China", "2007", "Specialist", "DAPs, DACs", "Guangzhou maker of portable players, DACs and headphone amplifiers.", WP + "Fiio", ["FiiO X and M series"]),
 B("Shanling", "China", "1988", "Specialist", "DAPs", "Shenzhen hi-fi maker of portable players and CD players.", "https://store.shanling.com/company-profile.html", ["Shanling M series"]),
 B("Philips", "Netherlands", "1891", "Mainstream", "compact cassette", "Dutch electronics maker that invented the compact cassette and the boombox.", K, ["Philips Radiorecorder"]),
 B("Sharp", "Japan", "1912", "Mainstream", "electronics", "Japanese electronics maker of the GF series boomboxes.", K, ["Sharp GF-777 \"Searcher\""]),
 B("JVC", "Japan", "1927", "Mainstream", "audio, video", "Japanese audio and video maker.", K, ["JVC RC-M90"]),
 B("Panasonic", "Japan", "1918", "Mainstream", "electronics", "Japanese electronics maker, formerly also sold as National.", K, ["Panasonic RX-5350"]),
 B("Conion", "", "", "Value", "boomboxes", "Boombox brand described as an off-brand of Onkyo.", WP + "Boombox", ["Conion C-100F"]),
 B("Tonies", "Luxembourg", "2013", "Mainstream", "Toniebox", "Maker of the Toniebox children's audio player and Tonies figures, founded as Boxine in Germany.", WP + "Tonies", ["Toniebox and Tonies"]),
 B("Yoto", "United Kingdom", "2016", "Mainstream", "kids' audio cards", "London maker of the Yoto screen-free card player for children.", "https://www.actoncapital.com/portfolio/yoto", ["Yoto Player"]),
]
notes = ("All five old kinds kept; Portable MiniDisc player added. MP3 player keeps its name (aliases digital audio player / DAP); its 15 flat models became versions of Sony NW and Astell&Kern archetypes, FiiO M21 under FiiO, Shanling Q2 left in m. "
 "Toniebox content moved from MP3 player to Audio figure (tag baby), Tonies ranges kept. Brief items left out as not attested on a retrieved page: Aiwa HS-P02 (only a search snippet), Sony D-E01, Sony CFS boomboxes, HiBy, Creative Zen article, Sharp/Aiwa/Panasonic MiniDisc models, Yoto Mini; JVC RC-M90, Sharp GF-777 and Conion years unconfirmed so left blank. Old kind sources kept for carried-over kinds.")
w('D3', '05_00', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
