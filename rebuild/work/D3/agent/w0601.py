import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D3/agent')
from w0500lib import w, X, B
WP = "https://en.wikipedia.org/wiki/"
K = "knowledge"
CORE = "https://www.core77.com/posts/24768/A-History-of-Braun-Design-Part-3-Audio-Products"
SM = "The Singing Machine"
kinds = [
 {"n": "Jukebox", "a": "juke box · coin-op phonograph", "d": "Machine that plays a record or track chosen from a menu, coin-operated or for home use.",
  "t": ["78 rpm", "45 rpm", "CD", "digital", "wallbox"], "s": "https://www.gamesroomcompany.com/collections/jukeboxes?page=3",
  "x": [
   X("Wurlitzer 1015", "Paul Fuller's 'bubbler' with bubble tubes and 24 selections, the icon of the jukebox.", "Wurlitzer", "1946", WP + "Jukebox",
     [("950", "Wurlitzer", "1942", "75–90 known to exist"), ("1015", "Wurlitzer", "1946", "over 56,000 sold in under two years"),
      ("1050", "Wurlitzer", "1971", "about 1,600 sold"), ("1015 tribute", "Sound Leisure", "2024", "made with the Wurlitzer family; CD, 45 or LP")], a="bubbler"),
   X("Seeburg Select-O-Matic", "First 100-selection jukebox, playing both sides of 50 records.", "Seeburg", "1949", WP + "Seeburg_Corporation",
     [("Symphonola 148 'Trashcan'", "Seeburg", "1948", ""), ("M100A", "Seeburg", "1949", "78 rpm, 100 selections"), ("3W1 wallbox", "Seeburg", "1949", "remote selector"),
      ("45 rpm model", "Seeburg", "1950", "first Seeburg for 45s"), ("M100C", "Seeburg", "1952", "seen in Happy Days")]),
   X("Rock-Ola jukeboxes", "Chicago jukeboxes from 1935, still made in classic styles in California.", "Rock-Ola", "1935", WP + "Rock-Ola",
     [("Model A", "Rock-Ola", "1935", "12 selections"), ("IMP-20", "Rock-Ola", "1937", "20 selections"), ("President", "Rock-Ola", "1942", "one known"),
      ("Premier", "Rock-Ola", "1942", ""), ("1434", "Rock-Ola", "", "first Rock-Ola 45 rpm player, early 1950s"), ("1448", "Rock-Ola", "1955", ""),
      ("404 Capri II", "Rock-Ola", "1965", ""), ("434 Concerto", "Rock-Ola", "1967", ""), ("Bubbler 100 CD", "Rock-Ola", "", "modern CD"),
      ("Harley-Davidson American Beauties Digital Music Center", "Rock-Ola", "", "digital"), ("Harley-Davidson American Legend Digital Music Center", "Rock-Ola", "", "digital")]),
   X("Orphéau Sunflower", "Modern French jukebox playing up to twenty LPs on both sides.", "Orphéau", "2018", WP + "Jukebox", []),
  ],
  "m": [["Maestro", "Filben"]]},
 {"n": "Radiogram", "a": "radio-phonograph · music cabinet · console stereo", "d": "Furniture-style cabinet combining a radio and a record player with speakers.",
  "t": ["console", "table-top", "portable", "valve", "transistor"], "s": "https://www.dansette.com/product-page/dansette-rg31",
  "x": [
   X("Braun radio-phonographs", "Braun's 1950s radio and record-player combinations that set the functional German style.", "Braun", "1955", CORE,
     [("combi", "Braun", "1955", "portable, Wilhelm Wagenfeld"), ("SK 4", "Braun", "1956", "'Snow White's coffin', Gugelot, Rams, Lindinger"),
      ("atelier 1", "Braun", "1957", "Dieter Rams"), ("studio 1", "Braun", "1957", "Gugelot and Lindinger"), ("TP 1", "Braun", "1959", "transistor radio with 45 player")]),
   X("Brionvega RR126", "Castiglioni brothers' radiogram on castors, a 'musical pet' with speakers as ears.", "Brionvega", "1966", "https://collections.vam.ac.uk/item/O1325746/brionvega-rr126-radiofonografo-radiogram-castiglioni-achille/",
     [("RR126", "Brionvega", "1966", "designed 1965; white laminated plywood")]),
  ],
  "m": [["RG31", "Dansette"]]},
 {"n": "Compact hi-fi system", "a": "mini system · midi system · micro system · music centre", "d": "Music system with source, amplifier and speakers sold together as one unit.",
  "t": ["micro", "mini", "midi", "lifestyle", "music centre"], "s": "https://www.denon.com/en-gb/product/archive-mini-systems/rcd-m38-dab/RCDM38DAB.html",
  "x": [
   X("Bang & Olufsen Beocenter", "Slim B&O music centres combining tuner, amplifier and tape or record player in one deck.", "Bang & Olufsen", "1973", "https://beocentral.com/beocenter1400",
     [("Beocenter 1400", "Bang & Olufsen", "1973", "first Beocenter with cassette"), ("Beocenter 1500 / 1600", "Bang & Olufsen", "", "successors to the 1400"),
      ("Beocenter 2000", "Bang & Olufsen", "1979", "compact system, to 1981")]),
  ],
  "m": [["D-M41", "Denon"], ["RCD-M38 DAB", "Denon"], ["SC-PM700", "Panasonic"], ["BTB2465", "Philips"], ["FX10", "Philips"], ["FX25", "Philips"], ["FX55", "Philips"]]},
 {"n": "Karaoke machine", "a": "karaoke speaker · karaoke system", "d": "Machine that plays music for singing along, with microphone inputs.",
  "t": ["portable", "party speaker", "TV-connected"], "s": "https://singingmachine.com/collections/classic-karaoke",
  "m": [["SML385", SM], ["Groove DISCO", SM], ["Cube Studio", SM], ["Singcast Max", SM], ["Platinum Wi-Fi Karaoke Machine", SM]]},
]
brands = [
 B("Wurlitzer", "United States", "1853", "Heritage manufactory", "jukeboxes", "Cincinnati instrument maker whose 1940s jukeboxes became icons.", WP + "Wurlitzer", ["Wurlitzer 1015"]),
 B("Seeburg", "United States", "1902", "Heritage manufactory", "jukeboxes", "Chicago maker of the first 100-selection jukebox.", WP + "Seeburg_Corporation", ["Seeburg Select-O-Matic"]),
 B("Rock-Ola", "United States", "1927", "Heritage manufactory", "jukeboxes", "Jukebox maker founded by David Rockola; now made in Torrance, California.", WP + "Rock-Ola", ["Rock-Ola jukeboxes"]),
 B("Sound Leisure", "United Kingdom", "", "Specialist", "jukeboxes", "Leeds maker of classic-styled jukeboxes.", WP + "Wurlitzer"),
 B("Orphéau", "France", "", "Artisan & independent", "LP jukebox", "Breton maker of the Sunflower LP jukebox.", WP + "Jukebox", ["Orphéau Sunflower"]),
 B("Braun", "Germany", "1921", "Premium", "Rams design", "German maker whose 1950s–60s audio defined functional design.", K, ["Braun radio-phonographs"]),
 B("Brionvega", "Italy", "", "Premium", "design radios and TVs", "Milan maker of design radios, radiograms and televisions.", "https://collections.vam.ac.uk/item/O1325746/brionvega-rr126-radiofonografo-radiogram-castiglioni-achille/", ["Brionvega RR126"]),
 B("Bang & Olufsen", "Denmark", "1925", "Premium", "design audio", "Danish maker of design-led audio and TV.", K, ["Bang & Olufsen Beocenter"]),
 B("Denon", "Japan", "1910", "Mainstream", "hi-fi, AV receivers", "Japanese hi-fi and home-cinema maker.", K),
 B("The Singing Machine", "United States", "", "Value", "karaoke", "American maker of home karaoke machines.", K),
]
notes = ("All four kinds kept. Jukebox: Rock-Ola Harley-Davidson models became versions of the Rock-Ola archetype; Filben Maestro kept in m. Compact hi-fi: added Denon D-M41 (maker page); Beocenter as archetype. Karaoke trimmed from 7 Singing Machine models to 5 (dropped Singcast One and Ultimate WiFi Karaoke Party as near-duplicates). "
 "Left out, not attested on a fetched page: Grundig and Blaupunkt radiograms (museum record timed out), Beosystem, AMI jukeboxes (only named), Yamaha MusicCast and Marantz M-CR612 systems. SK 4 is listed under Braun radio-phonographs; the fetched Core77 page treats it mainly as a record player.")
w('D3', '06_01', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
