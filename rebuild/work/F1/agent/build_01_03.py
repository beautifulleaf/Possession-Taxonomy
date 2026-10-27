import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
CAS = W + 'Cassette_tape'
EIGHT = W + '8-track_cartridge'
DAT = W + 'Digital_Audio_Tape'
DCC = W + 'Digital_Compact_Cassette'
ELC = W + 'Elcaset'
REEL = W + 'Reel-to-reel_audio_tape_recording'
MIC = W + 'Microcassette'
TP = 'https://positive-feedback.com/Issue46/tape_project.htm'
PLAY = W + 'Playaway'
SMM = 'https://hifilab.cz/en/detail-clanku/sony-super-metal-master-231'
MAX = 'https://www.soundandvision.com/content/maxell-audio-amp-video-tape'
MAR = 'https://3docean.net/item/cassette-tdk-mar-metal-1979-collection-29/29951787'
SA = 'https://www.duplication.com/tdk-sa-60-high-bias-cassette-tape.html'
ZX = 'https://www.ebay.de/itm/136457002161'
REV = 'https://www.theabsolutesound.com/articles/new-blank-cassettes-now-available-from-revox/'

kinds = [
 {"n": "Compact cassette", "a": "cassette · cassette tape · musicassette · MC", "d": "Audio tape in the standard two-hub compact cassette shell, pre-recorded or blank.",
  "t": ["Type I (ferric, normal)", "Type II (chrome or cobalt, high bias)", "Type III (ferrichrome)", "Type IV (metal)", "C60", "C90", "C120", "Dolby B", "Dolby C", "Dolby S", "dbx", "sealed new old stock", "J-card insert", "cassingle"],
  "s": CAS,
  "x": [
   X("Philips Compact Cassette", "The original two-hub cassette format, launched by Philips and licensed to other makers from 1966.", "Philips", "1963", CAS,
     [("Norelco cassette", "Philips", "1964", "US launch under the Norelco brand")], dt="shell type · tape type"),
   X("Pre-recorded musicassette", "Commercially duplicated music cassette, launched in Europe in 1965 and in the US by Mercury in 1966.", "", "1965", CAS,
     [("US musicassette launch", "Mercury Records", "1966", "49 titles")], dt="J-card · Dolby B · shell colour · chrome or ferric duplication"),
   X("TDK SA", "TDK's Type II blank cassette using its Super Avilyn formulation.", "TDK", "", SA, a="Super Avilyn", dt="C46–C100 · generation · shell design"),
   X("Maxell UD-XL II", "Maxell's Type II blank cassette using Epitaxial particles, later the XLII line.", "Maxell", "", MAX, a="UDXL-II · XLII", dt="length · generation"),
   X("TDK MA-R", "Metal blank cassette with a high-precision die-cast frame, the Reference Standard mechanism.", "TDK", "1979", MAR,
     [("1979 MA-R", "TDK", "1979", "first generation"), ("Later MA-R", "TDK", "", "revised many times after 1979")], dt="Type IV · C46–C90 · generation"),
   X("Metafine", "3M's pure metal-particle Type IV cassette tape.", "3M", "1979", CAS, dt="Type IV · length"),
   X("Sony Super Metal Master", "Sony's ceramic-shell Type IV metal cassette, made in limited numbers mainly for Japan.", "Sony", "1992", SMM, a="C-90SMMST", dt="ceramic shell · Type IV"),
   X("Nakamichi ZX", "Nakamichi-branded Type IV metal blank cassette.", "Nakamichi", "", ZX, dt="C-90 · sealed new old stock"),
   X("Revox Grandmaster", "Modern Type I blank cassette in a Revox-exclusive screwed shell made in Villingen.", "Revox", "2025", REV, a="Grandmaster Audio Cassette", dt="Type I · five-screw shell"),
  ]},
 {"n": "Reel-to-reel tape", "a": "open-reel tape · reel tape · R2R", "d": "Magnetic tape wound on an open reel, pre-recorded or blank, for a reel-to-reel recorder.",
  "t": ["¼-inch tape", "7-inch reel", "10.5-inch reel", "3¾ ips", "7½ ips", "15 ips", "two-track (half-track)", "four-track (quarter-track)", "Dolby or dbx encoded", "blank", "metal or plastic reel"],
  "s": REEL,
  "x": [
   X("The Tape Project tape", "Subscription audiophile releases copied from running masters at 15 ips on two-track reels.", "The Tape Project", "", TP, dt="15 ips · two-track · two-reel sets · series"),
   X("Barclay-Crocker tape", "Licensed audiophile reel tapes, mostly classical, Dolby encoded and duplicated at only four times speed.", "Barclay-Crocker", "1977–1986", REEL, dt="Dolby or dbx · label licensor"),
   X("Ampex pre-recorded tape", "Pre-recorded reel tapes of popular and classical music from Ampex.", "Ampex", "mid-1950s–mid-1970s", REEL, dt="speed · track format · box"),
  ]},
 {"n": "8-track cartridge", "a": "8-track · Stereo 8 · eight-track tape", "d": "Endless-loop tape cartridge with eight tracks (four stereo programmes), made for car and home players.",
  "t": ["stereo", "Quad-8 (quadraphonic)", "blank", "pre-recorded", "sealed"],
  "s": EIGHT,
  "x": [
   X("Stereo 8", "Bill Lear's eight-track endless-loop cartridge, offered in Ford cars from the 1966 models.", "Lear Jet", "1965", EIGHT,
     [("RCA Victor Stereo-8 cartridge", "RCA Victor", "1965", "175 launch cartridges from RCA Victor and RCA Camden"), ("Quad-8", "", "1970", "discrete quadraphonic, notched corner")],
     a="Lear Jet Stereo 8", dt="label · shell colour · stereo or quad"),
   X("Stereo-Pak", "Earlier four-track cartridge that Lear's eight-track format replaced.", "Muntz", "", EIGHT, a="4-track cartridge", dt="four-track"),
  ]},
 {"n": "Microcassette", "a": "minicassette · picocassette", "d": "Audio tape in a cassette smaller than the compact cassette, mostly for dictation and answering machines.",
  "t": ["MC60", "MC30", "MC90", "2.4 cm/s", "1.2 cm/s"],
  "s": MIC,
  "x": [
   X("Microcassette", "Olympus's small cassette for voice recording, 30 minutes a side at 2.4 cm/s.", "Olympus", "1969", MIC, dt="length · speed"),
   X("Mini-Cassette", "Philips's look-alike small cassette, not compatible with the Microcassette.", "Philips", "1967", MIC, dt="length"),
   X("Picocassette", "Cassette about half the size of a Microcassette.", "Dictaphone", "1985", MIC, [("Picocassette", "JVC", "1985", "co-introduced")]),
  ]},
 {"n": "DAT cassette", "a": "Digital Audio Tape · R-DAT", "d": "Small digital tape cassette recording 16-bit stereo audio at 32, 44.1 or 48 kHz, for 15 to 180 minutes.",
  "t": ["blank", "pre-recorded", "length 15–180 minutes", "DDS (computer data)"],
  "s": DAT},
 {"n": "Digital Compact Cassette", "a": "DCC", "d": "Philips and Matsushita's digital cassette using PASC compression, playable alongside analogue cassettes in DCC decks.",
  "t": ["blank", "pre-recorded (with track text)"],
  "s": DCC},
 {"n": "Elcaset", "a": "", "d": "Large cassette with ¼-inch tape at 3¾ ips, made by Sony, Panasonic and Teac from 1976 to 1980.",
  "t": ["blank", "tape type"],
  "s": ELC},
 {"n": "Audiobook player", "a": "Playaway · pre-recorded digital audio player", "d": "Self-contained device sold with one work, usually an audiobook, fixed on it; it plays only that work.",
  "s": PLAY,
  "x": [
   X("Playaway", "Card-deck-sized solid-state player preloaded with one audiobook, sold mainly to libraries.", "Playaway Products", "2005", PLAY,
     [("Playaway", "Playaway Products", "2005", ""), ("Redesigned Playaway", "Playaway Products", "2016", "backlit LCD, simpler buttons"), ("Wonderbook", "Playaway Products", "", "print book with player in the inside cover")],
     dt="title · library case"),
  ]},
]

K = "knowledge"
brands = [
 {"n": "Philips", "c": "Netherlands", "f": "1891", "seg": "Mainstream", "kf": "electronics", "d": "Dutch electronics company that launched the Compact Cassette in 1963 and co-developed the Digital Compact Cassette.", "sig": ["Philips Compact Cassette", "Mini-Cassette"], "s": K},
 {"n": "TDK", "c": "Japan", "f": "1935", "seg": "Mainstream", "kf": "blank tape", "d": "Japanese electronics maker known for SA and MA-R blank cassettes.", "sig": ["TDK SA", "TDK MA-R"], "s": K},
 {"n": "Maxell", "c": "Japan", "f": "1961", "seg": "Mainstream", "kf": "blank tape", "d": "Osaka tape maker known for Epitaxial UD-XL II cassettes and its Blown Away Guy advertising.", "sig": ["Maxell UD-XL II"], "s": MAX},
 {"n": "3M", "c": "United States", "f": "1902", "seg": "Mainstream", "kf": "materials", "d": "American materials company whose Scotch tapes included the Metafine metal cassette.", "sig": ["Metafine"], "s": K},
 {"n": "Sony", "c": "Japan", "f": "1946", "seg": "Mainstream", "kf": "electronics", "d": "Japanese electronics maker of the Walkman, DAT and premium metal cassettes.", "sig": ["Sony Super Metal Master"], "s": K},
 {"n": "Nakamichi", "c": "Japan", "f": "1948", "seg": "Premium", "kf": "cassette decks", "d": "Japanese maker of high-end cassette decks that also sold own-brand blank tapes.", "sig": ["Nakamichi ZX"], "s": K},
 {"n": "Revox", "c": "Switzerland", "f": "", "seg": "Premium", "kf": "tape recorders", "d": "Swiss audio brand known for reel-to-reel recorders, now selling Grandmaster blank cassettes.", "sig": ["Revox Grandmaster"], "s": REV},
 {"n": "The Tape Project", "c": "United States", "f": "", "seg": "Specialist", "kf": "reel-to-reel releases", "d": "Audiophile reel-tape label of Dan Schmalle, Michael Romanowski and Paul Stubblebine.", "sig": ["The Tape Project tape"], "s": TP},
 {"n": "Barclay-Crocker", "c": "United States", "f": "", "seg": "Specialist", "kf": "reel-to-reel releases", "d": "Maker of licensed audiophile pre-recorded reel tapes from 1977 to 1986.", "sig": ["Barclay-Crocker tape"], "s": REEL},
 {"n": "Ampex", "c": "United States", "f": "1944", "seg": "Professional & flagship", "kf": "tape recorders", "d": "American tape-recorder maker that also issued pre-recorded reel tapes.", "sig": ["Ampex pre-recorded tape"], "s": K},
 {"n": "Lear Jet", "c": "United States", "f": "", "seg": "Specialist", "kf": "8-track", "d": "Bill Lear's company, which led the consortium that created the Stereo 8 cartridge.", "sig": ["Stereo 8"], "s": EIGHT},
 {"n": "Muntz", "c": "United States", "f": "", "seg": "Specialist", "kf": "4-track cartridges", "d": "Maker of the four-track Stereo-Pak cartridge that preceded the 8-track.", "sig": ["Stereo-Pak"], "s": EIGHT},
 {"n": "Olympus", "c": "Japan", "f": "1919", "seg": "Mainstream", "kf": "optics", "d": "Japanese optics and electronics maker that introduced the Microcassette in 1969.", "sig": ["Microcassette"], "s": K},
 {"n": "Dictaphone", "c": "United States", "f": "", "seg": "Specialist", "kf": "dictation machines", "d": "Dictation-machine maker that introduced the Picocassette with JVC in 1985.", "sig": ["Picocassette"], "s": MIC},
 {"n": "Playaway Products", "c": "United States", "f": "", "seg": "Specialist", "kf": "preloaded players", "d": "Solon, Ohio maker of Playaway preloaded audiobook players, owned by Penguin Random House since 2023.", "sig": ["Playaway"], "s": PLAY},
]

notes = ("All three old kinds kept (old Metafine/3M, Grandmaster/Revox, Microcassette/Olympus, Mini-Cassette/Philips, Picocassette and Playaway models became archetypes); "
         "reel-to-reel, 8-track, DAT, DCC and Elcaset added. Tape types, lengths and Dolby are 't'. Left out: TDK SA and Maxell UD-XL II launch years and The Tape Project start year "
         "(only in search snippets), Sony 'Metal Master' (only the 1992 Super Metal Master was attested), Playaway View (a video player, not audiobook). DAT/DCC/Elcaset carry no archetypes; pre-recorded issues were rare.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/F1/shelves/01_03.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written', len(kinds), 'kinds')
