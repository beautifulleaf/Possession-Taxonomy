import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
SC='https://schachtspindle.com/collections/spinning-wheels-and-accessories'; MA='https://revolutionfibers.com/products/schacht-matchless-spinning-wheel'; SW=W+'Spinning_wheel'; DS=W+'Drop_spindle'
DC='https://woolery.com/ashford-drum-carder.html'; FB='https://woolery.com/collections/top-roving-batts'; FN='https://flippityfelts.wordpress.com/needle-felting-for-beginners/felting-needles'
o={k['n']:k for k in old('03_03')}
kinds=[
{"n":"Spinning wheel","a":"","d":"Wheel-driven device made for spinning fibre into yarn.","s":SC,
 "t":["Saxony","upright (castle)","great (walking) wheel","charkha","folding","single treadle","double treadle","Scotch tension","double drive"],
 "x":[X("Matchless","Schacht Spindle Company",MA,"Double-treadle maple wheel with a 19.5 in drive wheel, double drive, Scotch tension and bobbin-lead modes; six whorls give about 4:1 to 21:1.","",dt="19.5 in wheel · double treadle · 4:1-21:1"),
      X("S10 Concept","Schacht Spindle Company",SC,"Available in Irish or Scotch tension, single or double treadle, with 3- or 5-spoke or classic wheel options.","",dt="Irish or Scotch tension"),
      X("Sidekick","Schacht Spindle Company",SC,"Folding wheel made for transport.","",dt="folding"),
      X("Charkha","",SW,"Small hand-cranked wheel native to Asia, symbol of the Indian independence movement.","",dt="hand-cranked")],
 "m":[["Flatiron","Schacht Spindle Company"],["Jenn-E","Schacht Spindle Company"],["Ladybug","Schacht Spindle Company"],["S17","Schacht Spindle Company"],["S95 Victoria","Schacht Spindle Company"]]},
{"n":"Drop spindle","a":"","d":"Weighted hand spindle made for spinning yarn.","s":SC,
 "t":["top-whorl","bottom-whorl","Turkish (cross-arm)","supported spindle","takli","Navajo","Orenburg"],
 "x":[X("Top-whorl drop spindle","",DS,"Whorl near the top beneath a hook, with yarn forming a cop below; suspended while spinning.","",dt=""),
      X("Bottom-whorl spindle","",DS,"Whorl at the bottom with yarn above; more stable and preferred for plying.","",dt=""),
      X("Turkish spindle","",DS,"Low-whorl suspended spindle with crossed arms; yarn winds over and under the arms into a centre-pull ball.","",dt="crossed arms")],
 "m":o['Drop spindle']['m']},
{"n":"Hand and drum carder","a":"drum carder · hand cards · blending board","d":"Tool with teeth that cards fibre into batts, rolags or blended colours before spinning.","s":DC,
 "t":["drum carder","hand cards (pair)","blending board","fine (72 tpi)","superfine (120 tpi)"],
 "x":[X("Ashford Drum Carder","Ashford",DC,"8 x 24 in drum carder in Fine (72 tpi) and Superfine (120 tpi) card cloth, 6:1 for fleece or 4:1 for blending.","",dt="8 in drum · 2 oz capacity")]},
{"n":"Unspun fibre","a":"fleece · roving · top · batt","d":"Fleece, roving or top sold for spinning or felting.","s":"https://www.dickblick.com/categories/crafts/textile-arts/",
 "t":["fleece","combed top","roving","sliver","batt","rolag","Merino","Blue-faced Leicester (BFL)","Corriedale","Shetland"],
 "x":[X("Combed top","",FB,"Fibre combed so all fibres are parallel, best for worsted or semi-worsted spinning.","",dt=""),
      X("Roving","",FB,"Carded fibre in a continuous cord 2-3 in thick, best for woollen spinning.","",dt=""),
      X("Batt","",FB,"Fibre drum-carded into a blanket-like sheet.","",dt="")],"m":[]},
{"n":"Felting needle","a":"","d":"Barbed needle made for felting unspun fibre by hand.","s":"https://www.dickblick.com/categories/crafts/textile-arts/",
 "t":["triangle","star","spiral","reverse barb","gauge 32-42"],
 "x":[X("Gauge ladder","",FN,"Coarse 32-36 for shaping a core, 38 all-rounder, 40-42 for detail and finishing; star needles felt faster than triangle.","",dt="36 triangle · 38 star · 40 star starter set")],"m":[]},
]
brands=[
B("Schacht Spindle Company","United States","","Premium","spinning wheels and looms","Maker of Matchless, Ladybug, Sidekick and S10 Concept wheels, also looms.",s=SC,sig=["Matchless","S10 Concept"]),
B("Ashford","New Zealand","","Mainstream","wheels and carders","New Zealand maker of spinning wheels, looms and drum carders.",s=DC,sig=["Ashford Drum Carder"]),
B("Louët","Netherlands","","Premium","wheels and spindles","Dutch maker of wheels and spindles.",s="knowledge"),
]
write('03_03',kinds,brands,[],"Ashford Traditional/Kiwi, Louët S10 specs (Louët page blocked), Lendrum, Majacraft left out: no retrieved page confirmed them. Old Schacht models kept as flat models. Fibre breed names are types only.")
