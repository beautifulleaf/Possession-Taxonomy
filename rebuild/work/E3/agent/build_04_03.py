import json, os
S='https://saxophone.org/museum/saxophones/'
WP='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),x)) for x in v],"dt":dt}
FIN="lacquer · silver plate · unlacquered · special finishes"
# shared archetypes, voice-specific versions
def mark6(voice, extra):
    return A("Selmer Mark VI","Mark 6 · MK VI","Paris-made professional saxophone, the benchmark against which later saxophones are compared.","Selmer","1954",S+"model/1",
      extra,"serial range · Paris or US-finished (Elkhart engraving) · bow length · lacquer or plate")
def ba(voice, extra):
    return A("Selmer Balanced Action","BA","Larger-bore Selmer that first grouped the bell keys on the right side, the layout most modern saxophones use.","Selmer","1935",S+"model/34",extra,"serial range · Dorsey model · lacquer or plate")
def sba(extra):
    return A("Selmer Super Balanced Action","SBA · Super Action","First Selmer with offset tone holes in both stacks; often said to have set the tone for the modern saxophone.","Selmer","1947",S+"model/35",extra,"serial range · short or long bow (tenor) · special-order keys")
def sa80(extra):
    return A("Selmer Super Action 80 Series II","SA80 II · Serie II","Selmer's longest-running professional model, an update of the Super Action 80 with a darker sound.","Selmer","1986",S+"model/38",extra,"finish · engraving (Jubilee from 2010) · neck")
def s3(extra):
    return A("Selmer Series III","Serie III · SA80 Serie III","Later Selmer professional line, announced 1993, with redesigned keywork.","Selmer","1993",S+"model/54",extra,"finish · Jubilee engraving from 2010 · necks")
def ref(extra):
    return A("Selmer Reference 54","Reference · Ref 54","Modern Selmer modelled on the 1954 Mark VI, with modern keywork and a darker, more open sound.","Selmer","2000",S+"model/112",extra,"dark gold lacquer · vintage matte · clear lacquer")
def conn(extra,mm="6M · 10M · 12M"):
    return A("Conn M series 'Naked Lady'","Conn "+mm+" · Naked Lady","Elkhart-made Conn professional line named after the engraved female figure on the bell.","Conn","1934",S+"model/20",extra,"silver plate · lacquer · nickel · gold plate")
def super20(extra):
    return A("King Super 20","Super 20","H. N. White's professional saxophone, developed from the Zephyr Special; Charlie Parker played a Super 20 alto.","King","1945",WP+"King_Musical_Instruments",extra,"series I–VI · pearl keys · Silver Sonic (sterling neck/bell)")
def y62(extra):
    return A("Yamaha 62 series","YAS-62 · YTS-62 · YSS-62 · 'purple logo'","Yamaha's long-running professional saxophone; early horns are called 'purple logo' after their fading bell printing.","Yamaha","",S+"model/170",extra,"generation (original, II, III) · lacquer or silver plate")
def ycz(extra):
    return A("Yamaha Custom Z","82Z · Custom Z","Yamaha's jazz-oriented Custom saxophone, successor to the original Custom horns, with the Custom G1 neck.","Yamaha","",S+"model/175",extra,"series I or II · lacquer, black lacquer · neck")
def yana(extra,n="Yanagisawa 901 / 902 series",a="A-901 · T-901 · SC-901 · A-902 · T-902"):
    return A(n,a,"Yanagisawa's professional line; 901 in brass, 902 in bronze, with 991/992 the higher-grade equivalents.","Yanagisawa","1998",S+"model/143",extra,"brass (90x/99x) or bronze (902/992) · solid silver (9930/9937)")
def kw(extra):
    return A("Keilwerth SX90R","SX-90R · SX90","German professional saxophone line introduced in the late 1980s, known in black nickel finishes.","Keilwerth","late 1980s",WP+"Julius_Keilwerth",extra,"black nickel · lacquer · straight alto/tenor versions")

alto={"n":"Alto saxophone","a":"alto sax","d":"Single-reed saxophone in E♭, the most common voice for beginners and jazz.",
 "t":["student · intermediate · professional","with or without high F♯ key","low A (some vintage altos)",FIN,"mouthpiece (hard rubber or metal; ebonite student/classical)"],
 "s":"https://www.thomannmusic.com/saxophones.html",
 "x":[
  mark6("alto",[("Mark VI alto","Selmer","1954–1975","bow length changed over the run; some keyed to low A"),("Mark VII alto","Selmer","1975","successor; first Selmer with high F♯ standard")]),
  ba("alto",[("Balanced Action alto","Selmer","1935–1948",""),("Balanced Action 'Dorsey' model","Selmer","1937–1939","Jimmy Dorsey model")]),
  sba([("Super Balanced Action alto","Selmer","1947–1954","")]),
  conn([("Conn 6M","Conn","1934",""),("Conn New Wonder 'Chu Berry'","Conn","1925–1931","predecessor"),("Conn Transitional","Conn","1931–1934","predecessor")],"6M"),
  super20([("Super 20 series I","King","1945–1950",""),("Super 20 series II–V","King","1950–1976",""),("Super 20 series VI","King","1973–1998",""),("Zephyr","King","1935","predecessor")]),
  sa80([("Super Action 80","Selmer","1980","predecessor, said to be closer to the Mark VI than the VII"),("Super Action 80 Series II alto","Selmer","1986","")]),
  s3([("Series III alto","Selmer","2000","regular production by 2000; discontinued 2021"),("Millennium Edition A.III.2000","Selmer","2000","matte brushed silver body")]),
  ref([("Reference 54 alto","Selmer","","followed the tenor a couple of years after 2000; ended 2021"),("Supreme","Selmer","2021","successor")]),
  y62([("YAS-62 (original)","Yamaha","","long wrap-around keyguard"),("YAS-62II","Yamaha","2003","keywork changes, G1 neck"),("YAS-62 (III)","Yamaha","","new neck stamped '62'")]),
  ycz([("YAS-82Z","Yamaha","","Custom G1 neck"),("YAS-82Z II","Yamaha","","minor changes, new neck options")]),
  yana([("A-901","Yanagisawa","1998","brass"),("A-902","Yanagisawa","2002","bronze"),("A-9937","Yanagisawa","1999","solid silver"),("AWO series","Yanagisawa","2014","successor WO series")]),
 ],
 "m":[["Selmer Axos alto","Selmer"],["Yamaha YAS-480","Yamaha"],["Yamaha YAS-280","Yamaha"],["Thomann TAS-180","Thomann"],["Startone SAS-75","Startone"]]}

tenor={"n":"Tenor saxophone","a":"tenor sax","d":"Single-reed saxophone in B♭, pitched below the alto; the main jazz and rock solo voice.",
 "t":["student · intermediate · professional",FIN,"mouthpiece (hard rubber or metal)"],
 "s":"https://www.thomannmusic.com/saxophones.html",
 "x":[
  mark6("tenor",[("Mark VI tenor","Selmer","1954–1975",""),("Mark VII tenor","Selmer","1975","successor; designed by Michel Nouaux and Frederick Hemke")]),
  conn([("Conn 10M","Conn","1934","first-year horns 1934–35"),("Conn New Wonder 'Chu Berry'","Conn","1925–1931","predecessor"),("Conn Transitional","Conn","1931–1934","predecessor")],"10M"),
  ba("tenor",[("Balanced Action tenor","Selmer","1935–1948",""),("Reference 36","Selmer","2000","modern tenor modelled on the Balanced Action")]),
  sba([("Super Balanced Action tenor","Selmer","1947–1954","early short-bow tenors sharp below low C")]),
  super20([("Super 20 tenor series I","King","1945–1950","")]),
  ref([("Reference 54 tenor","Selmer","2000","inspired by a 1958 Mark VI"),("Supreme tenor","Selmer","2021","successor")]),
  sa80([("Super Action 80 Series II tenor","Selmer","1986","first serial 380423")]),
  s3([("Series III tenor","Selmer","1995","first serial 529312")]),
  kw([("SX-90R tenor","Keilwerth","","black nickel"),("Straight SX-90R tenor","Keilwerth","","")]),
  yana([("T-901","Yanagisawa","1998","brass"),("T-902","Yanagisawa","2003","bronze"),("T-9937","Yanagisawa","2000","solid silver"),("TWO series","Yanagisawa","2015","successor WO series")]),
  y62([("YTS-62","Yamaha","","")]),
  ycz([("YTS-82Z","Yamaha","","")]),
 ],
 "m":[["Selmer Axos tenor","Selmer"],["Yamaha YTS-280","Yamaha"]]}

sop={"n":"Soprano saxophone","a":"soprano sax","d":"Single-reed saxophone in B♭ an octave above the tenor, usually straight but also curved.",
 "t":["straight · curved · semi-curved","one-piece or detachable neck(s)",FIN],
 "s":"https://www.thomannmusic.com/saxophones.html",
 "x":[
  mark6("soprano",[("Mark VI soprano","Selmer","1954–1980","continued until the Super Action 80")]),
  s3([("Series III soprano","Selmer","1993","first Selmer soprano with straight and curved detachable necks, keyed to high G")]),
  A("Yanagisawa 99x soprano","S-991 · S-992 · SC-991 · SC-992","Yanagisawa's professional straight and curved sopranos in brass or bronze.","Yanagisawa","1998",S+"model/146",
    [("S-992","Yanagisawa","1998","bronze"),("SC-991 / SC-992","Yanagisawa","2004","curved sopranos"),("S-880","Yanagisawa","","first straight soprano with a detachable neck"),("SWO series","Yanagisawa","2017","successor WO series")],"brass or bronze · straight or curved"),
  ycz([("YSS-82Z","Yamaha","","fixed neck, straight or semi-curved"),("YSS-82ZRB","Yamaha","","black lacquer")]),
  y62([("YSS-62 / YSS-62R","Yamaha","","")]),
  kw([("Liebman Signature SX90R","Keilwerth","","David Liebman signature"),("SX-90 series II soprano","Keilwerth","","")]),
  conn([("Conn 4M curved soprano","Conn","","")],"4M"),
 ],
 "m":[["Selmer Signature soprano","Selmer"],["Yamaha YSS-475 II","Yamaha"],["Startone SCS-75 curved soprano","Startone"]]}

bari={"n":"Baritone saxophone","a":"bari sax","d":"Large single-reed saxophone in E♭ an octave below the alto, with a looped neck.",
 "t":["low A or low B♭",FIN,"student · professional"],
 "s":"https://www.thomannmusic.com/baritone_saxophones.html",
 "x":[
  mark6("bari",[("Mark VI baritone","Selmer","1954–1980","continued until the Super Action 80")]),
  conn([("Conn 12M","Conn","1934","designs developed from 1930")],"12M"),
  sba([("Super Balanced Action baritone","Selmer","1947–1954","low A offered as a special order")]),
  s3([("Series III baritone (SE-B3L)","Selmer","2008",""),("Super Action 80 Series II baritone (SE-B2L)","Selmer","1986","")]),
  A("Yanagisawa WO baritone","B-WO1 · B-WO2 · B-WO10 · B-WO20","Yanagisawa's professional baritone series with revised tone-hole layout, keyed to low A.","Yanagisawa","2018",WP+"Yanagisawa_Wind_Instruments",
    [("B-WO10","Yanagisawa","","brass Elite model, low A to high F♯"),("B-WO1","Yanagisawa","",""),("B-WO2","Yanagisawa","",""),("B-WO20","Yanagisawa","","")],"brass or bronze · lacquer"),
  kw([("SX-90 baritone","Keilwerth","",""),("SX90R baritone","Keilwerth","","")]),
 ],
 "m":[["Yamaha YBS-62II","Yamaha"],["Yamaha YBS-82","Yamaha"],["Yamaha YBS-480","Yamaha"],["Jupiter JBS1000","Jupiter"],["Rampone & Cazzani R1 Jazz baritone","Rampone & Cazzani"],["Schagerl 66","Schagerl"],["Startone SBS-75","Startone"]]}

brands=[
 {"n":"Selmer","c":"France","f":"1885","seg":"professional woodwinds","d":"Paris maker (Henri Selmer Paris) whose saxophones set the professional standard.","lines":["Balanced Action","Super Balanced Action","Mark VI","Mark VII","Super Action 80 Series II","Series III","Reference","Axos","Supreme","Signature"],"eras":[],"sig":["Selmer Mark VI","Selmer Balanced Action","Selmer Super Balanced Action"],"sc":["jazz","classical"],"rel":["Conn","King"],"s":WP+"Henri_Selmer_Paris"},
 {"n":"Conn","c":"United States","f":"1876","seg":"band instruments","d":"C. G. Conn of Elkhart, Indiana, a leading American maker of brass and saxophones.","lines":["New Wonder","Transitional","M series","Connqueror 26M/30M"],"eras":[],"sig":["Conn M series 'Naked Lady'"],"sc":["jazz","big band"],"rel":["King","Selmer"],"s":WP+"C.G._Conn"},
 {"n":"King","c":"United States","f":"1893","seg":"band instruments","d":"Brand of the H. N. White Company of Cleveland, Ohio, known for the Zephyr and Super 20 saxophones.","lines":["Voll-True","Zephyr","Super 20"],"eras":[],"sig":["King Super 20"],"sc":["jazz","bebop"],"rel":["Conn"],"s":WP+"King_Musical_Instruments"},
 {"n":"Yanagisawa","c":"Japan","f":"1894","seg":"professional saxophones","d":"Japanese saxophone specialist, maker of Japan's first soprano and the 90x/99x and WO lines.","lines":["800 series","900/990 series","901/902/991/992","9930/9937 Silver Sonic","WO series"],"eras":[],"sig":["Yanagisawa 901 / 902 series","Yanagisawa 99x soprano","Yanagisawa WO baritone"],"sc":["jazz","classical"],"rel":["Yamaha"],"s":WP+"Yanagisawa_Wind_Instruments"},
 {"n":"Keilwerth","c":"Germany","f":"1925","seg":"professional saxophones","d":"Julius Keilwerth of Nauheim, German saxophone maker known for the SX90R.","lines":["New King","Toneking","SX90","SX90R","MKX"],"eras":[],"sig":["Keilwerth SX90R"],"sc":["jazz","rock"],"rel":["Selmer"],"s":WP+"Julius_Keilwerth"},
 {"n":"Yamaha","c":"Japan","f":"1887","seg":"musical instruments","d":"Japanese instrument maker covering student to professional saxophones.","lines":["62 series","Custom Z","Custom EX","280","480"],"eras":[],"sig":["Yamaha 62 series","Yamaha Custom Z"],"sc":["school band","jazz"],"rel":["Yanagisawa"],"s":"knowledge"},
]
notes=("Four old kinds kept. Archetypes from saxophone.org museum model pages and Wikipedia; shared lines (Mark VI, Series III, Conn M, Yamaha 62/Custom Z, Keilwerth SX90R) repeat per voice with voice-specific versions only. "
 "Dropped: Thomann BariPRO/lowJAZZ (retailer house SKUs, also in r) and the r list; Selmer Supreme tenor folded in as Reference 54 successor version. "
 "Left out: Yamaha YAS-62/82Z years (Yamaha, Reverb, Sweetwater blocked 403, so no launch years cited); King Super 20 no tenor detail beyond series I; Conn 'Naked Lady' end year (sources disagree 1962/1968); mouthpieces (Otto Link, Meyer) left to accessories, noted only as a type.")
out={"kinds":[alto,tenor,sop,bari],"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/E3/shelves/04_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
