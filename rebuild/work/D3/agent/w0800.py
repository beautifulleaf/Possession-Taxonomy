import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D3/agent')
from w0500lib import w, X, B
WP = "https://en.wikipedia.org/wiki/"
K = "knowledge"
DT = "https://www.digitaltrends.com/wearables/best-streaming-devices/"
HCC = "https://homecinemachoice.com/node/121639"
KS = "https://www.audioadvice.com/content/kaleidescape-strato-movie-player-review/"
LD = WP + "LaserDisc_player"
P = "Panasonic"
kinds = [
 {"n": "Streaming stick or box", "a": "streaming media player", "d": "Stick or box that plays streamed video and audio on a television.",
  "t": ["stick", "box", "4K HDR", "Dolby Vision"], "s": "https://www.staples.com/Streaming-Media-Players/cat_CL160115",
  "m": [["Roku Ultra (2024)", "Roku"], ["Apple TV 4K (2022)", "Apple"], ["Google TV Streamer", "Google"], ["Shield TV Pro", "Nvidia"],
        ["Fire TV Stick 4K Max", "Amazon"], ["Fire TV Stick 4K", "Amazon"], ["Fire TV Stick HD", "Amazon"], ["Onn 4K Pro (2026)", "ONN"], ["onn 4K Streaming Device", "ONN"]]},
 {"n": "Blu-ray and DVD player", "a": "Blu-ray player · 4K Blu-ray player · DVD player · DVD recorder", "d": "Player or recorder for DVD, Blu-ray and 4K Ultra HD Blu-ray discs.",
  "t": ["DVD", "Blu-ray", "4K Ultra HD Blu-ray", "DVD recorder", "universal (SACD, DVD-Audio)"], "s": "https://vintagetechnics.co.uk/",
  "x": [
   X("Oppo UDP-203 / UDP-205", "Reference 4K Blu-ray universal players, still sought after since Oppo stopped making them in 2018.", "Oppo Digital", "2016", WP + "Oppo_UDP-203",
     [("UDP-203", "Oppo Digital", "2016", ""), ("UDP-205", "Oppo Digital", "", "ESS ES9038PRO DACs, 7.1 analogue outputs")]),
   X("Magnetar UDP800", "4K Blu-ray universal player seen as the Oppo successor; Home Cinema Choice Best Buy.", "Magnetar", "", HCC, []),
  ],
  "m": [["DP-UB9000", P], ["DP-UB820", P], ["DP-UB450", P], ["DP-UB420", P], ["DP-UB154", P], ["DMP-BD90", P], ["DMP-BD84", P], ["UBR-X200", "Reavon"], ["DVD-A10", "Technics"]]},
 {"n": "Set-top box", "a": "terrestrial receiver · satellite receiver · cable box · PVR", "d": "Box that receives broadcast television for a screen, often with a recorder.",
  "t": ["terrestrial (Freeview, ATSC)", "satellite", "cable", "with recorder (PVR)"], "s": "https://www.walmart.com/c/kp/set-top-box-digital-receiver",
  "m": [["CTCB105", "Core Innovations"], ["AT103B", "Ematic"], ["V8X", "GTMEDIA"]]},
 {"n": "Movie server", "a": "Kaleidescape type · movie player", "d": "Box that stores a library of films and plays them on a television or projector.",
  "t": ["player with storage", "player with separate server"], "s": "https://www.audiovenue.uk/product-tag/dap/",
  "x": [
   X("Kaleidescape Strato", "Players that download bit-perfect 4K films with lossless audio for disc-free playback.", "Kaleidescape", "", KS,
     [("Strato M", "Kaleidescape", "", "480 GB, 2K output"), ("Strato E", "Kaleidescape", "", "480 GB, 4K"), ("Strato C", "Kaleidescape", "", "no storage, needs Terra server"),
      ("Strato V", "Kaleidescape", "", "960 GB, Dolby Vision"), ("Terra server", "Kaleidescape", "", "8–123 TB")]),
  ]},
 {"n": "Video cassette recorder", "a": "VCR · video recorder · VHS player", "d": "Machine that records and plays television on videotape cassettes.",
  "t": ["VHS", "S-VHS", "VHS-C", "Betamax", "Philips VCR", "Video 2000"], "s": WP + "JVC_HR-3300",
  "x": [
   X("Philips N1500", "First home video cassette recorder, which gave the VCR format its name.", "Philips", "1972", WP + "Video_Cassette_Recording",
     [("N1500", "Philips", "1972", "VCR format"), ("N1700", "Philips", "1977", "VCR-LP"), ("SVR4004", "Grundig", "", "Super Video")]),
   X("Sony Betamax SL-7200", "Sony's first stand-alone Betamax deck in the US.", "Sony", "1976", "https://blog.cedmagic.com/history/betamax-sl-7200-1976.html",
     [("LV-1901", "Sony", "", "earlier TV and Betamax console"), ("SL-7200", "Sony", "1976", "$1,295; clock as external accessory")]),
   X("JVC HR-3300", "First VHS recorder, whose two-hour cassette helped VHS win the format war.", "JVC", "1976", WP + "JVC_HR-3300",
     [("Victor HR-3300", "JVC", "1976", "Japan"), ("HR-3300U VIDSTAR", "JVC", "1977", "US")]),
  ]},
 {"n": "LaserDisc player", "a": "LD player · LD/DVD combi player", "d": "Player for LaserDisc, the 30 cm analogue video disc sold from 1978, often combined with CD or DVD.",
  "t": ["LD only", "LD/CD combi", "LD/DVD combi", "MUSE Hi-Vision", "VCD", "CED videodisc"], "s": LD,
  "x": [
   X("Pioneer LaserDisc players", "Pioneer made most consumer LaserDisc players, from the DiscoVision era to the last DVL-919.", "Pioneer", "", LD,
     [("PR-7820", "Pioneer", "", "first mass-produced industrial player, from MCA DiscoVision"), ("LD-700", "Pioneer", "1984", "first with laser diode"),
      ("LD-W1", "Pioneer", "", "two-disc"), ("DVL-9", "Pioneer", "1996", "early LD/DVD combi"), ("HLD-X0", "Pioneer", "", "regarded as best LD player"),
      ("CLD-R5", "Pioneer", "", "LD/CD, one of the last"), ("DVL-919", "Pioneer", "", "LD/DVD, last models until 2009")]),
  ]},
]
brands = [
 B("Apple", "United States", "1976", "Premium", "iPhone, Apple TV", "American computer and phone maker.", K),
 B("Roku", "United States", "2002", "Mainstream", "streaming players", "American maker of streaming players and TV software.", K),
 B("Amazon", "United States", "1994", "Mainstream", "Fire TV", "American retailer that makes Fire TV streaming devices.", K),
 B("Google", "United States", "1998", "Mainstream", "Chromecast, Google TV", "American internet company that makes Google TV streamers.", K),
 B("Nvidia", "United States", "1993", "Premium", "GPUs, Shield", "American chip maker; its Shield TV is a power-user streamer.", K),
 B("ONN", "United States", "", "Own-label & retailer", "budget electronics", "Walmart's own electronics label.", DT),
 B("Oppo Digital", "United States", "", "Professional & flagship", "universal disc players", "Maker of reference Blu-ray players until 2018.", WP + "Oppo_UDP-203", ["Oppo UDP-203 / UDP-205"]),
 B("Magnetar", "China", "", "Specialist", "4K Blu-ray players", "Chinese brand of high-end disc players, distributed in Europe by Archisoft.", HCC, ["Magnetar UDP800"]),
 B("Panasonic", "Japan", "1918", "Mainstream", "Blu-ray players", "Japanese electronics maker.", K),
 B("Kaleidescape", "United States", "", "Professional & flagship", "movie servers", "American maker of home-cinema movie players and servers.", KS, ["Kaleidescape Strato"]),
 B("Philips", "Netherlands", "1891", "Mainstream", "compact cassette", "Dutch electronics maker.", K, ["Philips N1500"]),
 B("Sony", "Japan", "1946", "Mainstream", "Betamax, Walkman", "Japanese electronics maker.", K, ["Sony Betamax SL-7200"]),
 B("JVC", "Japan", "1927", "Mainstream", "VHS", "Japanese audio and video maker that created VHS.", K, ["JVC HR-3300"]),
 B("Pioneer", "Japan", "1938", "Mainstream", "LaserDisc, hi-fi", "Japanese audio and video maker.", K, ["Pioneer LaserDisc players"]),
]
notes = ("Kept the four old kinds; added Video cassette recorder and LaserDisc player. Streaming: added the Digital Trends picks (Roku Ultra, Apple TV 4K, Google TV Streamer, Shield TV Pro, Fire TV Stick 4K Max, Onn 4K Pro); dropped Fire TV Stick 4K Plus and 4K Select as near-duplicates; cleaned 'Apple Apple TV 4K'. Blu-ray: Panasonic models kept flat, Oppo and Magnetar archetypes added, Reavon UBR-X200 from the HCC review. Set-top box left with its three old models and types (no independent test winners fetched). "
 "Left out, not attested on a fetched page: Sky Q, TiVo, Freeview Play boxes, Panasonic AG-1970 S-VHS, Video 2000 VR2020 model, Sony SL-8200, Pioneer LD-S1 and CLD-D704 (forum only), Sony UHD players.")
w('D3', '08_00', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
