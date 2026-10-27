import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D3/agent')
from w0500lib import w, X, B
WP = "https://en.wikipedia.org/wiki/"
K = "knowledge"
CORE = "https://www.core77.com/posts/24768/A-History-of-Braun-Design-Part-3-Audio-Products"
R = "Roberts Radio"
kinds = [
 {"n": "Radio", "a": "table radio · portable radio · DAB radio", "d": "Broadcast receiver with a built-in speaker, for the table or to carry.",
  "t": ["table", "portable", "DAB/DAB+", "FM", "AM", "Bluetooth", "solar or wind-up"], "s": "https://www.philips.co.uk/c-m-so/home-audio/radios-and-alarm-clocks/all",
  "x": [
   X("Ekco AD-65", "Round Bakelite table radio by architect Wells Coates, an Art Deco design classic.", "Ekco", "1934", "https://collections.vam.ac.uk/item/O22790/ekco-ad-65-radio-coates-wells",
     [("AD-65", "Ekco", "1934", "designed 1932; Bakelite, walnut-effect or black")]),
   X("Philips Bi-Ampli", "Philips valve table radios with separate bass and treble output stages and two speakers.", "Philips", "1954", "https://radiomuseum.org/r/philips_bx740a.html",
     [("BX740A", "Philips", "1954", "12 valves, AM and FM")]),
   X("Regency TR-1", "First commercially made transistor radio, a pocket set with Texas Instruments transistors.", "Regency", "1954", WP + "Regency_TR-1",
     [("TR-1", "Regency", "1954", "black, bone white, mandarin red, cloud grey; rarer colours later")], dt="case colour"),
   X("Sony TR-55", "First transistor radio from the company that renamed itself Sony.", "Sony", "1955", WP + "Regency_TR-1", []),
   X("Roberts R200 / Revival", "Leatherette-covered British portable whose 1950s look returned as the Roberts Revival.", R, "1956", WP + "Roberts_Radio",
     [("R66", R, "1956", "portable valve radio"), ("R200", R, "1960", "six-transistor portable, made to 1964"), ("Revival (250 series)", R, "1993", "reissue in original red"),
      ("Revival Petite", R, "", "UK best-selling radio 2022"), ("Revival Petite 2", R, "2024", ""), ("Revival Uno BT", R, "", ""), ("Revival Uno Solar", R, "", "")],
     dt="colour · DAB/FM · Bluetooth"),
   X("Braun T 3", "Minimal pocket transistor radio by Dieter Rams with the Ulm school.", "Braun", "1958", CORE,
     [("SK 1", "Braun", "1955", "table radio"), ("exporter 2", "Braun", "1956", "portable"), ("T 3", "Braun", "1958", "pocket transistor radio"),
      ("T 52", "Braun", "1961", "portable with handle"), ("RT 20", "Braun", "1961", "last Braun table radio")]),
   X("Tivoli Audio Model One", "Simple table radio with a large tuning knob, designed by Henry Kloss.", "Tivoli Audio", "", "https://www.remodelista.com/products/henry-kloss-model-one-radio/", [], dt="cabinet: walnut, black and silver, beige"),
  ],
  "m": [["TAV2000DB", "Philips"], ["Blutune 300L", R], ["Rambler Max", R], ["Revere 100", R], ["Revere 500", R], ["SolarDAB 99", R], ["SportsDAB 65", R]],
  "r": [["Revere", R], ["Revival", R]]},
 {"n": "Shortwave and world-band receiver", "a": "world receiver · world-band radio · SW receiver", "d": "Receiver covering the shortwave bands to hear international and distant broadcasts, often with SSB and synchronous detection.",
  "t": ["portable", "tabletop", "SSB", "synchronous detection", "airband"], "s": WP + "Trans-Oceanic",
  "x": [
   X("Zenith Trans-Oceanic", "American portable multiband radio made 1941–1981, the first popular world-band portable.", "Zenith", "1942", WP + "Trans-Oceanic",
     [("7G605 \"Clipper\"", "Zenith", "1942", "first model"), ("8G005Y", "Zenith", "1946", "first post-war model"), ("H500", "Zenith", "1951", "'Super Trans-Oceanic'"),
      ("600 series", "Zenith", "1954", "last valve sets, to 1962"), ("Royal 1000", "Zenith", "1957", "first transistor model"), ("Royal 3000", "Zenith", "", "added FM"),
      ("Royal 7000", "Zenith", "1968", "BFO for SSB/CW"), ("R7000", "Zenith", "1979", "last model")]),
   X("Braun T 1000", "Portable shortwave receiver by Dieter Rams.", "Braun", "1963", CORE, []),
   X("Grundig Satellit", "German world-band portables; the Satellit 650 is often called the best shortwave radio ever built.", "Grundig", "", "https://spectrum.ieee.org/the-consumer-electronics-hall-of-fame-grundig-satellit-650-radio",
     [("Satellit 650", "Grundig", "1986", "nearly 9 kg"), ("Satellit 700", "Grundig", "", ""), ("Satellit 800", "Grundig", "2000", "")]),
   X("Sony ICF-2001D / ICF-2010", "Portable with synchronous detection, SSB and airband, among the best shortwave portables.", "Sony", "1985", "https://mwcircle.org/legacy-receiver-reviews/receiver-review-sony-icf-2001d-icf-2010/",
     [("ICF-2001", "Sony", "1980", "earlier, different set"), ("ICF-2001D / ICF-2010", "Sony", "1985", "ICF-2010 in North America; made to 2003")]),
   X("Tecsun PL series", "Low-priced Chinese DSP and PLL shortwave portables with SSB.", "Tecsun", "", "https://swling.com/blog/2025/01/jeffs-short-review-of-the-tecsun-pl-880",
     [("PL-310ET", "Tecsun", "", ""), ("PL-660", "Tecsun", "", "airband, synchronous"), ("PL-680", "Tecsun", "", ""), ("PL-880", "Tecsun", "", "reviewed 2013"), ("PL-990", "Tecsun", "", "")]),
  ]},
 {"n": "Clock radio", "a": "alarm clock radio · bedside radio", "d": "Radio combined with a clock and alarm, for the bedside.",
  "t": ["FM", "DAB", "projection clock", "Bluetooth"], "s": "https://www.philips.co.uk/c-m-so/home-audio/radios-and-alarm-clocks/all",
  "m": [["TAR5100", "Philips"], ["Ortus 5", R]]},
 {"n": "Radio scanner", "a": "police scanner · scanner", "d": "Receiver that scans and listens to public-service, air and marine radio frequencies.",
  "t": ["handheld", "base or mobile", "analogue", "digital trunking"], "s": "https://uniden.com/collections/radio-scanners",
  "m": [["BC125AT", "Uniden"], ["BC365CRS", "Uniden"], ["BC355N", "Uniden"], ["BCD436HP", "Uniden"], ["SDS100", "Uniden"], ["SDS150", "Uniden"], ["SDS200", "Uniden"], ["HomePatrol-2", "Uniden"], ["WS1010", "Whistler"]],
  "r": [["Bearcat", "Uniden"]]},
]
brands = [
 B("Ekco", "United Kingdom", "", "Heritage manufactory", "Bakelite radios", "E.K. Cole Ltd of Southend-on-Sea, maker of Bakelite radios.", "https://collections.vam.ac.uk/item/O22790/ekco-ad-65-radio-coates-wells", ["Ekco AD-65"]),
 B("Philips", "Netherlands", "1891", "Mainstream", "compact cassette", "Dutch electronics maker.", K, ["Philips Bi-Ampli"]),
 B("Regency", "United States", "", "Heritage manufactory", "first transistor radio", "Radio division of I.D.E.A. of Indianapolis.", WP + "Regency_TR-1", ["Regency TR-1"]),
 B("Sony", "Japan", "1946", "Mainstream", "Walkman", "Japanese electronics maker.", K, ["Sony TR-55", "Sony ICF-2001D / ICF-2010"]),
 B("Roberts Radio", "United Kingdom", "1932", "Premium", "Revival radios", "British radio maker founded in London by Harry Roberts and Leslie Bidmead; owned by Glen Dimplex since 1994.", WP + "Roberts_Radio", ["Roberts R200 / Revival"]),
 B("Braun", "Germany", "1921", "Premium", "Rams design", "German maker whose 1950s–60s radios defined functional design.", K, ["Braun T 3", "Braun T 1000"]),
 B("Tivoli Audio", "United States", "2000", "Premium", "table radios", "Boston radio maker founded by Tom DeVesto and Henry Kloss.", "https://www.remodelista.com/products/henry-kloss-model-one-radio/", ["Tivoli Audio Model One"]),
 B("Zenith", "United States", "1918", "Heritage manufactory", "Trans-Oceanic", "American radio and TV maker, now owned by LG.", K, ["Zenith Trans-Oceanic"]),
 B("Grundig", "Germany", "", "Mainstream", "world-band radios", "German radio maker founded by Max Grundig; owned by Arçelik since 2007.", "https://spectrum.ieee.org/the-consumer-electronics-hall-of-fame-grundig-satellit-650-radio", ["Grundig Satellit"]),
 B("Tecsun", "China", "", "Value", "shortwave portables", "Chinese maker of shortwave portables.", "https://swling.com/blog/2025/01/jeffs-short-review-of-the-tecsun-pl-880", ["Tecsun PL series"]),
 B("Uniden", "Japan", "1966", "Specialist", "Bearcat scanners", "Maker of Bearcat radio scanners.", K),
 B("Whistler", "United States", "", "Specialist", "scanners", "Maker of radio scanners.", "https://reviewed.com/home-outdoors/best-right-now/best-police-scanners"),
]
notes = ("Kept Radio, Clock radio and Radio scanner; added Shortwave and world-band receiver. Radio: Philips/Roberts models kept (Revival Uno models became versions of the Roberts Revival archetype). Radio scanner trimmed from 11 Uniden models to 8 plus Whistler WS1010 (Reviewed pick); dropped BCD536HP, BCD996P2, SR30C as near-duplicates. "
 "Braun SK 4 is a radio-phonograph and belongs on the radiogram shelf, not here. Not attested on a retrieved page and left out: Eton models, AOR scanners, Whistler beyond WS1010, Grundig Satellit 2000/3400 (only listings), Tecsun model years. Regency TR-1 and Sony TR-55 both sourced from the TR-1 article.")
w('D3', '06_00', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
