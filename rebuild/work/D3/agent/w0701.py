import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D3/agent')
from w0500lib import w, X, B
WP = "https://en.wikipedia.org/wiki/"
K = "knowledge"
CAR = WP + "Carousel_slide_projector"
SP = WP + "Slide_projector"
kinds = [
 {"n": "CRT television and video monitor", "a": "tube TV · CRT TV · PVM · BVM", "d": "Television or video monitor with a cathode-ray tube, now collected for design and for retro gaming.",
  "t": ["colour", "black-and-white", "portable", "professional monitor", "flat-screen CRT"], "s": WP + "Trinitron",
  "x": [
   X("Braun HF 1", "Low wooden table television by Herbert Hirche, a German design classic.", "Braun", "1959", "https://www.radiomuseum.org/r/braun_hf1hf.html",
     [("HF 1", "Braun", "1959", "Telefunken Visiomat 2 chassis")]),
   X("Brionvega Algol 11", "Portable 11-inch television by Marco Zanuso and Richard Sapper, its screen tilted up like a face.", "Brionvega", "1964", "https://collection.designmuseum.brussels/en/algol-11",
     [], dt="colour of ABS case"),
   X("Sony Trinitron", "Sony's aperture-grille colour tube, sold for four decades; PVM/BVM monitors are prized for retro gaming.", "Sony", "1968", WP + "Trinitron",
     [("KV-1210", "Sony", "1968", "original 12-inch Trinitron"), ("PVM (Professional Video Monitor)", "Sony", "", "studio monitor"),
      ("BVM (Broadcast Video Monitor)", "Sony", "", "broadcast monitor"), ("FD Trinitron / WEGA", "Sony", "1998", "flat-screen, 27–36 inch")],
     dt="screen size · consumer or PVM/BVM · inputs (RGB, component, SDI)"),
   X("JVC Videosphere", "Space-helmet black-and-white portable TV that can hang from a chain.", "JVC", "1970", WP + "Videosphere",
     [], dt="white, red, black, orange, grey · plain or alarm-clock base"),
   X("Bang & Olufsen Beovision 600 / 601", "Low-profile Danish black-and-white portable televisions.", "Bang & Olufsen", "", "https://beocentral.com/beovision601",
     [("Beovision 600", "Bang & Olufsen", "", ""), ("Beovision 601", "Bang & Olufsen", "1972", "last B&O-made portable, to 1974")]),
  ]},
 {"n": "Rear-projection television", "a": "RPTV · projection TV", "d": "Television whose picture is projected onto the screen from inside its cabinet.",
  "t": ["CRT", "DLP", "LCD or LCoS"], "s": "https://www.crutchfield.com/p_690WD60737/Mitsubishi-WD-60737.html",
  "m": [["Mitsubishi WD-60737", "Mitsubishi"], ["Mitsubishi WD-65734", "Mitsubishi"], ["Samsung HL-P4663W", "Samsung"], ["Sony Grand WEGA KDF-E42A10", "Sony"], ["Sony KDF-60WF655 Grand WEGA", "Sony"]]},
 {"n": "Slide projector", "a": "carousel projector", "d": "Projector that shows 35 mm photographic slides from a tray or magazine.",
  "t": ["rotary tray", "straight tray", "dissolve (twin-lens)"], "s": "https://www.ebay.ca/b/Kodak-Slide-Projectors/15256/bn_158411",
  "x": [
   X("Kodak Carousel", "Slide projector with a round gravity-fed tray, dominant in the US from 1961 to 2004.", "Kodak", "1961", CAR,
     [("Model 550", "Kodak", "1961", "first Carousel"), ("Carousel 800", "Kodak", "1964", ""), ("Carousel 750H / 760H / 850H", "Kodak", "1972", "600H–850H series to 1981"),
      ("Carousel 4200 / 4400 / 5200", "Kodak", "1981", "4000–5600 series to 2004"), ("Ektapro 3020", "Kodak", "", "")]),
   X("Leitz Pradovit", "German straight-tray projectors, made by Leica until 2006.", "Leica", "1958", SP,
     [("Prado", "Leica", "1958", "Leitz"), ("Pradovit RC", "Leica", "", "24 V 150 W quartz lamp"), ("Pradovit 153", "Leica", "", "")]),
   X("Braun Paximat", "German straight-magazine slide projectors from Braun Foto Technik, later Reflecta.", "Braun Foto Technik", "", SP, []),
   X("Rolleivision", "Rollei projectors including twin-lens dissolve models.", "Rollei", "", SP,
     [("P3800", "Rollei", "1976", "two lenses for dissolve"), ("Rolleivision 35 Twin Digital", "Rollei", "1990", "PC interface")]),
  ],
  "r": [["Carousel", "Kodak"]]},
 {"n": "Cine film projector", "a": "film projector · home movie projector", "d": "Projector that shows motion-picture film at home.",
  "t": ["Super 8", "8 mm", "Single 8", "16 mm", "9.5 mm", "sound"], "s": "https://www.1stdibs.com/buy/8mm-projector",
  "x": [
   X("Elmo projectors", "Japanese projectors from 1927; the Super 8 GS-1200 is the collectors' high point.", "Elmo", "1927", WP + "Elmo_(company)",
     [("Model A", "Elmo", "1927", "16 mm, first made in Japan"), ("Hayabusa", "Elmo", "1936", "first Elmo 8 mm"), ("16-CL", "Elmo", "", "16 mm"), ("ST-600M", "Elmo", "", ""),
      ("ST-1200HD", "Elmo", "", "Super 8, 1970s"), ("GS-1200", "Elmo", "", "Super 8 stereo, 1970s"), ("GS-1200 P Xenon", "Elmo", "1983", "final model")]),
   X("Eumig Super 8 projectors", "Austrian home-movie projectors, among the most common Super 8 machines.", "Eumig", "1965", "https://collection.sciencemuseumgroup.org.uk/objects/co8461117/eumig-super-610d-super-8-cine-projector",
     [("Super 610D", "Eumig", "1965", "Super 8; made 1965–1970")]),
   X("Bolex SP 80", "Swiss Super 8 and Single 8 projector.", "Bolex", "1973", "https://www.super8wiki.com/index.php/Bolex_SP_80_projector",
     [("SP 8", "Bolex", "", "predecessor"), ("SP 80", "Bolex", "1973", ""), ("SP 80 Special", "Bolex", "", "successor")]),
  ],
  "m": [["Heurtier Mono 42 Integral Automatic", "Heurtier"], ["Keystone R-8", "Keystone"], ["Revere Eight Model 85", "Revere"]],
  "r": [["Kodascope", "Kodak"]]},
]
brands = [
 B("Sony", "Japan", "1946", "Mainstream", "Trinitron, Walkman", "Japanese electronics maker.", K, ["Sony Trinitron"]),
 B("Braun", "Germany", "1921", "Premium", "Rams design", "German maker whose 1950s–60s audio and TV defined functional design.", K, ["Braun HF 1"]),
 B("Brionvega", "Italy", "", "Premium", "design radios and TVs", "Milan maker of design radios, radiograms and televisions.", "https://collection.designmuseum.brussels/en/algol-11", ["Brionvega Algol 11"]),
 B("JVC", "Japan", "1927", "Mainstream", "audio, video", "Japanese audio and video maker.", K, ["JVC Videosphere"]),
 B("Bang & Olufsen", "Denmark", "1925", "Premium", "design audio", "Danish maker of design-led audio and TV.", K, ["Bang & Olufsen Beovision 600 / 601"]),
 B("Kodak", "United States", "1888", "Mainstream", "film, Carousel", "American photography company.", K, ["Kodak Carousel"]),
 B("Leica", "Germany", "", "Premium", "cameras, Pradovit", "German camera and optics maker, formerly Leitz.", K, ["Leitz Pradovit"]),
 B("Braun Foto Technik", "Germany", "", "Mainstream", "slide projectors", "German slide-projector maker, later Reflecta; not the Braun appliance company.", SP, ["Braun Paximat"]),
 B("Rollei", "Germany", "", "Premium", "cameras, projectors", "German camera maker that also made slide projectors.", SP, ["Rolleivision"]),
 B("Elmo", "Japan", "1921", "Specialist", "cine projectors", "Tokyo maker of cine cameras and projectors until 1983.", WP + "Elmo_(company)", ["Elmo projectors"]),
 B("Eumig", "Austria", "1919", "Mainstream", "home-movie gear", "Viennese maker of cine projectors and cameras, active 1919–1982.", "https://collection.sciencemuseumgroup.org.uk/objects/co8461117/eumig-super-610d-super-8-cine-projector", ["Eumig Super 8 projectors"]),
 B("Bolex", "Switzerland", "", "Specialist", "cine cameras", "Swiss maker of cine cameras and projectors.", "https://www.super8wiki.com/index.php/Bolex_SP_80_projector", ["Bolex SP 80"]),
 B("Mitsubishi", "Japan", "", "Mainstream", "rear-projection TVs", "Japanese electronics group, a leading rear-projection TV maker.", K),
]
notes = ("Added CRT television and video monitor; kept the three old kinds. Rear-projection models kept as flat list (5). Kodak and Leica slide projectors and Elmo cine projectors became versions of archetypes; Revere model name tidied ('Revere Revere Eight' to 'Revere Eight'). "
 "Brief said Trinitron KV-1310 (1968); the Trinitron article names the KV-1210 as the original, so that is used. Left out as not attested on a fetched page: Brionvega Doney (Domus page blocked, retry redirected), Sony KV-HR, Philips CRT sets, Braun Paxiscope (Slide projector article names Paximat instead), Bell & Howell projectors, Mitsubishi model history.")
w('D3', '07_01', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
