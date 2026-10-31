import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/D3/agent')
from lib import *
VT='https://vintagetechnics.co.uk/'; CD=WP+'Cassette_deck'; NK=WP+'Nakamichi'; RV=WP+'Revox'; AK=WP+'Akai'
kinds=[
K("Cassette deck","tape deck · cassette recorder","Hi-fi component that plays and records compact cassettes.",VT,
  ["two-head","three-head","auto-reverse","dual-cassette","Dolby B / C / S","dbx"],
  [X("Advent Model 200","Advent","1970",CD,"The first high-fidelity cassette deck, pairing Dolby B with chromium dioxide tape.",[("Model 200","Advent","1970",""),("Model 201","Advent","","Wollensak transport")]),
   X("Nakamichi 1000 / 700","Nakamichi","1973",NK,"Three-head, dual-capstan decks that set the standard for cassette fidelity.",
     [("1000","Nakamichi","c. 1973",""),("700","Nakamichi","c. 1973",""),("580M","Nakamichi","c. 1978","early metal-tape deck"),("1000ZXL","Nakamichi","c. 1980","built-in calibration computer"),("700ZXL","Nakamichi","c. 1980","")],dt="head count · Dolby B/C · metal-tape capability"),
   X("Nakamichi Dragon","Nakamichi","1983",NK,"Top Nakamichi deck with motor-driven automatic azimuth correction (NAAC), made 1983–1995."),
   X("Nakamichi RX series","Nakamichi","",NK,"Auto-reverse decks that mechanically eject and flip the cassette (UDAR).",[("RX-202","Nakamichi","",""),("RX-303","Nakamichi","",""),("RX-505","Nakamichi","","")]),
   X("Revox B215","Revox","1985",RV,"Four-motor, beltless direct-drive cassette deck made 1985–1992.",[("B710","Revox","","earlier, shares Studer A710 transport"),("B215","Revox","1985","")]),
   X("Tandberg TCD","Tandberg","",CD,"High-end Tandberg decks with automatic bias and head azimuth adjustment.",[("TCD-330","Tandberg","",""),("TCD-340A","Tandberg","",""),("TCD 3014 A","Tandberg","1988","")]),
   X("Akai GX three-head decks","Akai","",AK,"Akai closed-loop three-head decks with glass-and-crystal ferrite heads.",[("GX-F95","Akai","",""),("GX-R99","Akai","",""),("GX-90","Akai","",""),("GX-F91","Akai","","")]),
  ],
  [("Nakamichi 480","Nakamichi"),("Nakamichi 582","Nakamichi"),("Nakamichi 680 ZX","Nakamichi"),("Sony TC-K71","Sony"),("Sony TC-K81","Sony"),("Technics RS-B33W","Technics"),("Technics RS-TR575","Technics"),("Aiwa AD-WX717","Aiwa"),("Bang & Olufsen Beocord 9000","Bang & Olufsen"),("Pioneer CT-959","Pioneer"),("Trio KX-780","Trio"),("Denon DRM-600","Denon"),("Marantz SD4050","Marantz"),("TASCAM 122mkIII","TASCAM")]),
K("Reel-to-reel tape deck","open-reel tape recorder","Hi-fi component that plays and records open-reel magnetic tape.",VT,
  ["quarter-track","half-track","7-inch reels","10.5-inch reels","3¾ / 7½ / 15 ips","valve","solid-state"],
  [X("Revox A77 / B77","Revox","1967",RV,"Swiss transistor open-reel recorders with servo direct-drive capstan; over 460,000 A77s were built.",
     [("A77","Revox","1967","made to 1977"),("A700","Revox","1970s","three-speed quartz PLL capstan"),("B77","Revox","1979","logic control"),("PR99 Mk II","Revox","c. 1985","professional B77, balanced I/O")]),
   X("Revox 36 series","Revox","1954",RV,"Willi Studer's first Revox valve recorders.",[("A36","Revox","1954",""),("G36","Revox","","last of the series, ended 1967")]),
   X("TEAC A-3340","TEAC","1972",WP+"TEAC_Corporation","Four-track home recorder with Simul-Sync overdubbing, popular with musicians.",[("A3340","TEAC","",""),("A2340","TEAC","","")]),
   X("Akai GX open-reel","Akai","",AK,"Popular Akai open-reel decks with GX glass-ferrite heads.",[("GX-630D","Akai","",""),("GX-635D","Akai","",""),("GX-747","Akai","","also GX-747DBX"),("GX-77","Akai","","auto-loading")]),
   X("Tandberg tape recorders","Tandberg","1956",WP+"Tandberg","Norwegian domestic tape recorders.",[("Model 2 Hi-Fi","Tandberg","1956","three speeds"),("Model 6","Tandberg","1960","first full stereo"),("Model 12","Tandberg","1966","first transistorised consumer model")]),
   X("Pioneer RT-707","Pioneer","1977",WP+"Reel-to-reel_audio_tape_recording","Pioneer open-reel deck reviewed in 1977–78."),
   X("Sony TC-630","Sony","1970s",WP+"Reel-to-reel_audio_tape_recording","Sony open-reel deck typical of a 1970s audiophile machine."),
  ]),
K("MiniDisc deck","MD deck","Hi-fi component that plays and records MiniDiscs.",VT,["ATRAC","MDLP","Hi-MD"],
  [X("Sony MDS-JE780","Sony","2002",WP+"MiniDisc","Sony home MiniDisc deck made 2002–2005.")]),
K("DAT deck","digital audio tape deck","Hi-fi component that plays and records digital audio tape (DAT) cassettes.",VT,None,None,[("Sony DTC-60ES","Sony")]),
K("8-track player","Stereo 8 player","Home component that plays (and may record) 8-track tape cartridges; an 8-track player fitted in a car is in Vehicles.",VT,["player","recorder"]),
]
brands=[
 B("Nakamichi","Japan","1948","Professional & flagship","cassette decks","Tokyo maker founded by Etsuro Nakamichi; Nakamichi brand from 1972.",NK,["1000","Dragon","RX-505"]),
 B("Revox","Switzerland","1951","Heritage manufactory","tape recorders","Willi Studer's consumer brand.",RV,["A77","B77","B215"]),
 B("Akai","Japan","1929","Mainstream","tape recorders","Tokyo electronics maker known for open-reel and cassette decks.",AK,["GX-635D","GX-747"]),
 B("Tandberg","Norway","1933","Heritage manufactory","tape recorders","Oslo radio and tape-recorder maker founded by Vebjørn Tandberg.",WP+"Tandberg",["TCD 3014 A"]),
 B("TEAC","Japan","1953","Specialist","tape recorders","Tokyo maker; its TASCAM division serves musicians.",WP+"TEAC_Corporation",["A3340"]),
 B("Advent","United States","1967","Heritage manufactory","early hi-fi cassette","Henry Kloss's Cambridge, Massachusetts company.",WP+"Advent_Corporation",["Model 200"]),
 B("Pioneer","Japan","1938","Mainstream","receivers","Japanese electronics maker.","knowledge",["RT-707"]),
 B("Sony","Japan","1946","Premium","consumer electronics","Tokyo electronics maker that introduced DAT and MiniDisc.","knowledge",["TC-K81","MDS-JE780"]),
]
notes=("All five kinds kept. Cassette deck: 21 models cut to 14 plus 7 archetypes (dropped Akai HX-A3, B&O Beocord 3500, Pioneer CT-939, Rotel RD-15F, Technics RS-263US/RS-288, Nakamichi 670 ZX as near-duplicates); head count, NR and auto-reverse as types. Reel-to-reel gains archetypes (old kind had no models). "
 "Left out (no retrieved page naming them): Nakamichi CR-7/ZX-7 years, Aiwa and Sony TC-K archetypes, Technics RS-B, Studer A810, TEAC X-2000, Technics RS-1500/1700, Tandberg 9000X, Otari, Sony MDS-JA555ES/JB980, Sony DTC-ZA5ES, Pioneer D-07, Akai/Panasonic 8-track players (8-track article names no home players).")
write('04_00',kinds,brands,notes)
