import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
AG='https://www.austingallery.org/blog/best-weaving-looms-2026'; MW='https://www.yarn.com/products/schacht-mighty-wolf'; AM='https://rebeccamezoff.com/blog/2020/10/8/two-great-looms-the-schacht-arras-and-the-mirrix'
SH=W+'Shuttle_(weaving)'; RE=W+'Reed_(weaving)'; KM='https://yarn-store.com/machine-knitting/about-knitting-machines/knitting-machine-chart/'; BR='https://museum.global.brother/guide/zone/2/55?lang=en'
H='https://www.hobbycraft.co.uk/knitting-crochet'; WL='https://woolery.com/weaving-looms.html'
S='Schacht Spindle Company'
kinds=[
{"n":"Rigid heddle loom","a":"","d":"Portable two-shaft loom for plain weave and simple patterns.","s":WL,
 "t":["folding","10 to 32 in weaving width","7.5 dent reed","sample loom"],
 "x":[X("Cricket","Schacht Spindle Company",AG,"Entry-level rigid heddle loom, 15 in (also 10 in), sold as a complete starter.","",dt="10 or 15 in"),
      X("Flip","Schacht Spindle Company",AG,"Folding rigid heddle loom with ratchet tension.","",dt="folding"),
      X("Rigid Heddle Loom","Ashford",AG,"Ashford's 24 in (also 32 in) rigid heddle loom, the all-round pick in a 2026 guide.","",v=[("Knitters Loom","folding, 12, 20 or 28 in"),("SampleIt Loom","16 in")],dt="24 in · 7.5 dent reed"),
      X("Original Rigid Heddle Loom SG-20","Beka",AG,"20 in budget rigid heddle loom.","",dt="20 in")],
 "m":[]},
{"n":"Floor loom","a":"treadle loom · jack loom","d":"Large treadled multi-shaft loom for complex weaving.","s":WL,
 "t":["jack loom","countermarch","4 shaft","8 shaft","folding","height extender"],
 "x":[X("Mighty Wolf","Schacht Spindle Company",MW,"36 in floor loom on the Baby Wolf X-frame; 4 or 8 shafts or Four Now-Four Later.","",dt="36 in · folds to 18 in depth"),
      X("Baby Wolf","Schacht Spindle Company",MW,"26 in X-frame folding floor loom that the Mighty Wolf widens.","",dt="26 in")],
 "m":[["Cranbrook",S],["Megado",S],["Octado",S]]},
{"n":"Table loom","a":"","d":"Multi-shaft loom that sits on a table.","s":WL,
 "t":["4 shaft","8 shaft","folding"],
 "x":[X("Folding Table Loom","Ashford",AG,"8-shaft folding table loom, 24 in.","",dt="24 in · 8 shaft")],
 "m":[["David 3",S],["Erica",S],["Harmony",S],["Jane",S],["Lilli Loom",S],["Spring 2",S]]},
{"n":"Inkle loom","a":"","d":"Compact loom for weaving narrow bands.","s":WL,"t":["with belt shuttle","band width 4 to 4.5 in"],
 "x":[X("Inkle Loom","Schacht Spindle Company",AG,"Inkle loom with belt shuttle for bands up to 4.5 in.","",dt="up to 4.5 in"),
      X("Inkle Loom","Ashford",AG,"Inkle loom for bands up to 4 in.","",dt="up to 4 in")],"m":[]},
{"n":"Tapestry loom","a":"frame loom","d":"Frame loom for tapestry and wall hangings.","s":WL,"t":["frame","lap loom","table-top tapestry"],
 "x":[X("Arras Tapestry Loom","Schacht Spindle Company",AM,"Wooden loom weaving up to 20 in, tensioned by large screws raising the top beam.","",dt="20 in · wood"),
      X("Mirrix","Mirrix",AM,"Mostly metal tapestry looms in widths from 5 to 38 in with wing-nut tensioning; folds nearly flat.","",dt="5-38 in"),
      X("LapLoom A","Harrisville Designs",AG,"12 x 16 in frame loom for small tapestry.","",dt="12 x 16 in")],"m":[]},
{"n":"Shuttle, reed and weaving accessories","a":"shuttle · reed · heddle · lease sticks","d":"Shuttles, reeds, heddles and sticks used to set up and weave on a loom.","s":RE,
 "t":["stick shuttle","boat shuttle","belt shuttle","reed (dents per inch)","lease sticks","heddle hook"],
 "x":[X("Reed","",RE,"Comb of flattened steel wire between wooden ribs that spaces warp threads and beats in the weft; hand-weaving sizes 5 to 24 dents per inch.","",dt="6, 8, 10, 12, 15 dpi"),
      X("Stick shuttle","",SH,"Flat, narrow notched piece of wood holding the weft; 16 to 24 in typical.","",dt="")]},
{"n":"Knitting machine","a":"","d":"Machine that knits fabric with a bed of latch needles.","s":H,
 "t":["standard gauge (4.5 mm)","mid-gauge (6.5-7 mm)","bulky (9 mm)","punch-card","electronic"],
 "x":[X("SK280 / SK840","Silver Reed",KM,"Standard-gauge machines for lace to sport yarn: SK280 punch-card, SK840 electronic with DesignaKnit.","",v=[("LK150","mid-gauge manual, plastic bed"),("SK155","bulky metal bed, punch card")],dt="4.5 mm · lace to sport"),
      X("KH1-B3","Brother",BR,"Brother's 1955 home knitting machine from its entry into the field in 1954.","1955",dt="")]},
{"n":"Knitting loom","a":"","d":"Peg frame, round or long, made for knitting with yarn by hand.","s":H,"t":["round","long","adjustable"],"m":[]},
]
brands=[
B("Schacht Spindle Company","United States","","Premium","looms and wheels","Maker of Cricket, Flip, Baby Wolf and Mighty Wolf looms and spinning wheels.",s=MW,sig=["Cricket","Mighty Wolf","Arras Tapestry Loom"]),
B("Ashford","New Zealand","","Mainstream","looms and wheels","Maker of rigid heddle, table and inkle looms and spinning wheels.",s=AG,sig=["Rigid Heddle Loom","Folding Table Loom"]),
B("Mirrix","United States","","Specialist","tapestry looms","Maker of metal tapestry looms.",s=AM,sig=["Mirrix"]),
B("Harrisville Designs","United States","","Specialist","small looms","Maker of the LapLoom frame loom.",s=AG,sig=["LapLoom A"]),
B("Silver Reed","Japan","","Specialist","knitting machines","Maker of current domestic knitting machines SK280, SK840, LK150, SK155.",s=KM,sig=["SK280 / SK840"]),
B("Brother","Japan","","Mainstream","home machines","Entered home knitting machines in 1954.",s=BR,sig=["KH1-B3"]),
]
write('03_04',kinds,brands,[],"Other looms dissolved: Schacht Jane, Spring 2, Lilli Loom, David 3, Harmony, Erica placed under Table loom by my judgement (no retrieved page classified them); Cranbrook, Megado, Octado stay under Floor loom. Glimåkra, Louët, Passap, Addi Express left out (no retrieved page). Old generic models like 'Floor loom','Rigid heddle loom' dropped as non-items. Knitting loom and Knitting machine kept; machine archetypes from the Silver Reed page and Brother museum page.")
