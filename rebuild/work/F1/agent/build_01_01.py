import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
PR = W + 'Phonograph_record'
CYL = W + 'Phonograph_cylinder'
BER = W + 'Berliner_Gramophone'
RS = W + 'Red_Seal_Records'
COL = W + 'Columbia_Records'
EDD = W + 'Edison_Disc_Record'
PAT = W + 'Pathé_Records'
FLX = W + 'Flexi_disc'
ET = W + 'Electrical_transcription'
ACE = W + 'Acetate_disc'
VOG = 'https://pinrepair.com/arcade/voice.htm'
REC = 'https://collection.ingenium.ca/item/1993.0159.001'

kinds = [
 {"n": "78 rpm record", "a": "coarse-groove record · shellac record · 78", "d": "Shellac or early disc with wide grooves, played at about 78 rpm with a coarse stylus.",
  "t": ["7-inch", "10-inch", "12-inch", "single-sided", "double-sided", "acoustic recording (before 1925)", "electrical recording (1925 on)", "vinylite 78", "album set of several discs"],
  "s": PR,
  "x": [
   X("Berliner gramophone disc", "Emile Berliner's early lateral-cut gramophone discs, the ancestor of all disc records.", "Berliner Gramophone", "1892", BER,
     [("Hard rubber 7-inch disc", "Berliner Gramophone", "1892", "United States Gramophone Company"), ("Shellac disc", "Berliner Gramophone", "1895", "shellac compound replaced hard rubber"),
      ("Canadian Berliner disc", "Berliner Gramophone", "1899", "Montreal company, bought by Victor in 1924")],
     dt="single-sided · 7-inch · speed about 70 rpm · label type"),
   X("Red Seal record", "Premium red-label celebrity and classical recordings, begun by the Gramophone Company and taken up by Victor.", "Victor Talking Machine Company", "1901", RS,
     [("Gramophone Record Red Seal", "The Gramophone Company", "1901", "first red-label discs"), ("Victor Red Seal", "Victor Talking Machine Company", "1903", "US issues from 1903")],
     a="Red Label", dt="10-inch or 12-inch · single- or double-sided · acoustic or electrical"),
   X("Columbia Double-Faced disc", "Columbia's mass-produced discs with grooves on both sides, which made double-sided records the norm.", "Columbia Records", "1908", COL,
     [("10-inch Double-Faced", "Columbia Records", "1908", "65 cents at launch")], dt="10-inch or 12-inch · acoustic or electrical (from 1925)"),
   X("Vinylite 78", "Late 78s pressed in quieter vinyl compounds instead of shellac.", "RCA Victor", "1945", PR,
     [("De Luxe vinylite 78", "RCA Victor", "1945", ""), ("Deccalite 78", "Decca", "", "")], dt="vinyl compound · label colour"),
  ]},
 {"n": "Cylinder record", "a": "phonograph cylinder · wax cylinder", "d": "Sound recorded in the groove of a cylinder (wax or celluloid) for a phonograph.",
  "t": ["brown wax", "black wax (moulded)", "celluloid", "two-minute", "four-minute", "standard 2¼-inch", "concert-size", "with original box and lid"],
  "s": CYL,
  "x": [
   X("Brown wax cylinder", "Early soft-wax cylinders cut at about 120 rpm, each worn out after a few dozen plays.", "", "c. 1888", CYL, dt="condition · mould · box"),
   X("Gold Moulded Record", "Edison's hard-wax cylinders moulded from a master, so hundreds of copies could be made.", "Edison Records", "1902", CYL, a="Edison Gold Moulded", dt="two-minute · box and slip"),
   X("Amberol", "Edison's four-minute wax cylinder with a finer groove.", "Edison Records", "1908", CYL, dt="four-minute · box"),
   X("Blue Amberol", "Edison's durable blue celluloid four-minute cylinder, made under the acquired Lambert patents.", "Edison Records", "1912", CYL, dt="four-minute · celluloid · box"),
   X("Lambert celluloid cylinder", "The first mass-produced celluloid cylinders, made in Chicago under Thomas B. Lambert's patent.", "Lambert Company", "1900", CYL, dt="celluloid colour · two-minute"),
   X("Indestructible cylinder", "Celluloid cylinders made under licence by the Indestructible Record Company, also sold by Columbia.", "Indestructible Record Company", "1906", CYL,
     [("Columbia-sold Indestructible cylinder", "Columbia Records", "1908", "Columbia's celluloid cylinders until it dropped the format in 1912")], dt="two- or four-minute"),
   X("Pathé cylinder", "French cylinders sold by Pathé alongside its phonographs, in a standard and several larger sizes.", "Pathé Records", "1894", PAT,
     [("Standard 2¼-inch", "Pathé Records", "1894", ""), ("Salon", "Pathé Records", "", "3.5-inch"), ("Stentor", "Pathé Records", "", "5-inch"), ("Le Céleste", "Pathé Records", "", "5 × 9 inches")],
     dt="size · production to about 1914"),
  ]},
 {"n": "Vertical-cut disc", "a": "hill-and-dale disc", "d": "Disc record cut with a vertical (hill-and-dale) groove, played with its own reproducer.",
  "t": ["centre-start", "rim-start", "sapphire ball stylus", "diamond stylus"],
  "s": W + 'Edison_Records',
  "x": [
   X("Edison Diamond Disc", "Thick vertical-cut Edison disc of phenolic resin over a wood-flour core, played at 80 rpm with a diamond stylus.", "Edison Records", "1912", EDD,
     [("Diamond Disc", "Edison Records", "1912–1929", "just under 1/4 inch thick"), ("Needle Type lateral disc", "Edison Records", "1929", "lateral-cut issues just before Edison left records")],
     a="Edison Disc Record", dt="10-inch · label type · surface condition"),
   X("Pathé vertical disc", "Pathé's vertical-cut shellac discs, played with a sapphire ball stylus and at first starting from the centre.", "Pathé Records", "1905", PAT,
     [("Centre-start disc", "Pathé Records", "1905–1916", ""), ("Rim-start disc", "Pathé Records", "1916", ""), ("20-inch disc", "Pathé Records", "", "played at 120 rpm; failed commercially")],
     dt="sizes 6.5 to 20 inches · speed 80–120 rpm · etched or paper label"),
  ]},
 {"n": "Flexi-disc", "a": "flexi · soundsheet · sonosheet · phonosheet", "d": "Thin flexible vinyl sheet record, often bound into magazines or given away as a promotion.",
  "t": ["magazine insert", "promotional giveaway", "one-sided", "square sheet", "round sheet", "software flexi (computer magazines)"],
  "s": FLX,
  "x": [
   X("Soundsheet", "The flexible record as first sold commercially, by the American maker Eva-Tone, which made them until 2000.", "Eva-Tone", "1962", FLX, a="Eva-Tone Soundsheet", dt="colour · insert or loose"),
   X("Sonosheet", "Japanese flexi-discs inserted in Asahi Sonorama's monthly magazine.", "Asahi Sonorama", "early 1960s", FLX, dt="with magazine or loose"),
  ]},
 {"n": "Acetate or lathe-cut disc", "a": "instantaneous disc · lacquer · dubplate · reference disc · lathe cut", "d": "Disc cut one at a time on a recording lathe, as an acetate or lacquer, not pressed.",
  "t": ["aluminium core", "glass core (wartime)", "paper or card base", "test or reference acetate", "home recording", "dubplate", "modern lathe-cut vinyl"],
  "s": ACE,
  "x": [
   X("Lacquer instantaneous disc", "Aluminium disc coated with nitrocellulose lacquer, cut on a lathe for broadcast, reference and home recording.", "", "1934", ACE,
     [("Bare aluminium disc", "", "1929", "earlier instantaneous discs"), ("Glass-core disc", "", "World War II", "used when aluminium was scarce")], a="acetate", dt="size 6–16 inches · core · label writing"),
   X("Recordio disc", "Blank home-recording disc for Wilcox-Gay's Recordio disc recorders, with a metal core and synthetic coating.", "Wilcox-Gay", "1940–1950", REC,
     dt="label fields for title, date and speed · storage album"),
   X("Voice-O-Graph record", "Coin-operated booth recording of the customer's voice, delivered as a 6-inch record with an envelope.", "International Mutoscope", "1940–1957", VOG,
     dt="6-inch · 45 or 78 rpm · envelope"),
   X("Dubplate", "One-off acetate cut for sound systems and DJs to play exclusive tracks.", "", "1960s", ACE, dt="10 or 12 inches · wear"),
  ]},
 {"n": "16-inch transcription disc", "a": "transcription disc · electrical transcription · ET", "d": "16-inch, 33⅓ rpm disc made for radio broadcast playback, not sold to the public.",
  "t": ["shellac", "vinylite", "lacquer instantaneous", "vertical-cut", "lateral-cut", "library service", "programme disc"],
  "s": ET,
  "x": [
   X("NBC Thesaurus", "NBC's transcription library service for stations, later the RCA/NBC Thesaurus Library.", "NBC", "1934", ET, dt="library numbering · vinylite"),
   X("World Broadcasting System transcription", "Transcription library discs from one of the major suppliers to US stations.", "World Broadcasting System", "", ET, dt="vertical-cut · library numbering"),
   X("AFRS transcription", "Armed Forces Radio Service programme discs made from World War II onward.", "Armed Forces Radio Service", "World War II", ET, dt="programme number · vinylite"),
  ]},
]

K = "knowledge"
brands = [
 {"n": "Berliner Gramophone", "c": "United States", "f": "1892", "seg": "Heritage manufactory", "kf": "gramophone discs", "d": "Emile Berliner's gramophone companies in the US and Canada, which made the first commercial disc records.",
  "eras": ["United States Gramophone Company, 1892–1900", "Montreal company, 1899–1924"], "sig": ["Berliner gramophone disc"], "rel": ["Victor Talking Machine Company", "The Gramophone Company"], "s": BER},
 {"n": "The Gramophone Company", "c": "United Kingdom", "f": "1898", "seg": "Heritage manufactory", "kf": "records", "d": "Berliner's English subsidiary, later Gramophone & Typewriter Ltd, which issued the first Red Seal records.",
  "sig": ["Red Seal record"], "rel": ["Berliner Gramophone", "Victor Talking Machine Company"], "s": BER},
 {"n": "Victor Talking Machine Company", "c": "United States", "f": "1901", "seg": "Heritage manufactory", "kf": "records", "d": "Eldridge Johnson's Camden, New Jersey, record and phonograph maker, known for Red Seal discs; later RCA Victor.",
  "lines": ["Red Seal"], "sig": ["Red Seal record"], "rel": ["RCA Victor", "Berliner Gramophone"], "s": RS},
 {"n": "Columbia Records", "c": "United States", "f": "1889", "seg": "Heritage manufactory", "kf": "records", "d": "Founded as the Columbia Phonograph Company in Washington, D.C.; made cylinders, then discs from 1901.",
  "sig": ["Columbia Double-Faced disc"], "s": COL},
 {"n": "RCA Victor", "c": "United States", "f": "", "seg": "Heritage manufactory", "kf": "records", "d": "Record label that introduced the 7-inch 45 rpm single in 1949 and vinylite 78s in 1945.",
  "sig": ["Vinylite 78"], "rel": ["Victor Talking Machine Company"], "s": PR},
 {"n": "Decca", "c": "United Kingdom", "f": "1929", "seg": "Heritage manufactory", "kf": "records", "d": "Record label that issued Deccalite vinyl 78s.", "s": K},
 {"n": "Edison Records", "c": "United States", "f": "", "seg": "Heritage manufactory", "kf": "cylinders", "d": "Thomas Edison's record maker: Gold Moulded and Amberol cylinders and Diamond Discs, until it left the business in 1929.",
  "sig": ["Gold Moulded Record", "Amberol", "Blue Amberol", "Edison Diamond Disc"], "rel": ["Lambert Company"], "s": CYL},
 {"n": "Lambert Company", "c": "United States", "f": "1900", "seg": "Specialist", "kf": "celluloid cylinders", "d": "Chicago maker of the first mass-produced celluloid cylinders under Thomas B. Lambert's patent; patents bought by Edison in 1912.",
  "sig": ["Lambert celluloid cylinder"], "s": CYL},
 {"n": "Indestructible Record Company", "c": "United States", "f": "", "seg": "Specialist", "kf": "celluloid cylinders", "d": "Licensed maker of celluloid cylinders from 1906, also supplying Columbia.",
  "sig": ["Indestructible cylinder"], "s": CYL},
 {"n": "Pathé Records", "c": "France", "f": "1894", "seg": "Heritage manufactory", "kf": "vertical-cut discs", "d": "French phonograph and record maker known for cylinders and vertical-cut discs played with a sapphire ball.",
  "lines": ["Pathé Actuelle"], "sig": ["Pathé cylinder", "Pathé vertical disc"], "s": PAT},
 {"n": "Eva-Tone", "c": "United States", "f": "", "seg": "Specialist", "kf": "flexi-discs", "d": "American maker of Soundsheet flexi-discs from 1962 until August 2000.", "sig": ["Soundsheet"], "s": FLX},
 {"n": "Asahi Sonorama", "c": "Japan", "f": "", "seg": "Specialist", "kf": "flexi-discs", "d": "Japanese publisher whose monthly magazine carried Sonosheet flexi-discs from the early 1960s.", "sig": ["Sonosheet"], "s": FLX},
 {"n": "Wilcox-Gay", "c": "United States", "f": "", "seg": "Specialist", "kf": "home disc recorders", "d": "Charlotte, Michigan maker of Recordio home disc recorders and blank Recordio discs.", "sig": ["Recordio disc"], "s": REC},
 {"n": "International Mutoscope", "c": "United States", "f": "", "seg": "Specialist", "kf": "arcade machines", "d": "Arcade-machine maker of the Voice-O-Graph recording booth, built from 1940 to 1957.", "sig": ["Voice-O-Graph record"], "s": VOG},
 {"n": "NBC", "c": "United States", "f": "1926", "seg": "Institution & issuer", "kf": "radio network", "d": "American broadcast network whose Thesaurus transcription service began in 1934.", "sig": ["NBC Thesaurus"], "s": ET},
 {"n": "World Broadcasting System", "c": "United States", "f": "", "seg": "Specialist", "kf": "transcriptions", "d": "Major supplier of transcription libraries to US radio stations.", "sig": ["World Broadcasting System transcription"], "s": ET},
 {"n": "Armed Forces Radio Service", "c": "United States", "f": "", "seg": "Institution & issuer", "kf": "military radio", "d": "US forces radio service that used transcription discs from World War II until 1998.", "sig": ["AFRS transcription"], "s": ET},
]

notes = ("All six old kinds kept. Old Edison cylinder models (Amberol, Blue Amberol, Gold Moulded) and flexi models (Soundsheet, Sonosheet) became archetypes. "
         "Old sources replaced by retrieved Wikipedia pages where better. Left out: Presto discs as an archetype (only the Presto 'K' recorder and 8N engraver were attested, not a disc line), "
         "HMV as a separate entry (no retrieved page tied it to a disc line; The Gramophone Company covers it), Pathé Actuelle as an archetype (a lateral 78 label; named only as a line). "
         "Recordio launch year left as 1940–1950 (museum record) since the 1939 date came only from a search snippet.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/F1/shelves/01_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written', len(kinds), 'kinds')
