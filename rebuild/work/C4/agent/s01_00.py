import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
BA=W+'Baren_(printing_tool)'; WJ=W+'Woodblock_printing_in_Japan'; ET=W+'Etching'; CON='https://www.conradmachine.com/tabletop-etching-presses/'
LT='https://tinyworkshops.com/best-lino-cutting-tools'; PP='https://peopleofprint.com/?p=84832'; TK='https://shop.takachpress.com/takach-presses'
GR=W+'Ground_(etching)'; SP=W+'Screen_printing'; WC=W+'Woodcut'
kinds=[
{"n":"Printing ink","a":"relief ink · etching ink · block-printing ink","d":"Ink made for relief, intaglio and screen hand printmaking.","s":"https://www.dickblick.com/categories/drawing/inks/",
 "t":["oil-based","water-washable oil-based","water-based","etching ink","relief ink","screen-printing ink"],
 "m":[["Waterbased Acrylic Fabric Screen Printing Ink","Blick Art Materials"],["Etching Inks","Charbonnel"],["Artist's Colors Relief Inks","Gamblin"],["Etching Inks","Gamblin"]]},
{"n":"Lino and wood cutting tool","a":"gouge · lino cutter","d":"Hand cutter made for carving lino or wood blocks for printing.","s":"https://shop.takachpress.com/speedball-lino-cutter-assortment-no-2",
 "t":["V-gouge","U-gouge","palm handle","mallet handle","interchangeable-blade cutter"],
 "x":[X("Pfeil gouges","Pfeil",LT,"Swiss-made carving gouges favoured by serious printmakers; palm-handle tools for lino, mallet handles for wood.",dt="L 12/1 V · L 11/3 U · L 5/8 wide shallow · palm or mallet handle"),
      X("Linoleum Printmaking Carving Set","Flexcut",LT,"Four interchangeable heads with strop and compound; sharp and reliable intermediate set.",dt="four heads · wooden handle"),
      X("Lino cutter assortment","Speedball (printmaking)",LT,"Inexpensive starter cutter with blades stored in the handle; best on soft blocks.",dt="five cutter heads"),
      X("Lino Cutting & Printing Kit","Essdee",LT,"UK starter kit with a six-blade cutter.",dt="23-piece kit")],
 "m":[["Linoleum Tool Set L331-0 (6 pc)","E C Lyons"]]},
{"n":"Printing block and plate","a":"lino block · woodblock · etching plate","d":"Lino, wood, soft-cut or metal block or plate made to be cut or etched for printing.","s":"https://www.dickblick.com/categories/printmaking/",
 "t":["linoleum","soft-cut rubber","cherry woodblock","plywood","copper plate","zinc plate","steel plate","photopolymer"],"m":[]},
{"n":"Brayer","a":"ink roller","d":"Hand roller made for rolling ink onto a printing block.","s":"https://www.dickblick.com/categories/printmaking/block-printing/brayers/",
 "t":["soft rubber","hard rubber","pop-in handle","gel"],
 "m":[["Fabric Ink Rollers","Essdee"],["Pop-In Hard Rubber Brayer","Gelli Arts"],["Lino Inking Brayers","Pebeo"],["Pop-In Brayer","Speedball (printmaking)"],["Professional Brayers","Speedball (printmaking)"]]},
{"n":"Baren","a":"hon-baren · printing pad","d":"Hand pad made for burnishing paper onto an inked block in relief printing.","s":"https://www.dickblick.com/categories/printmaking/block-printing/brayers/",
 "t":["hon-baren (traditional)","daiyo-baren","plastic baren","ball-bearing baren"],
 "x":[X("Hon-baren","Kikuhide",BA,"Traditional baren with a braided cord core, lacquered paper disk and bamboo-sheath cover; the disk takes 40-50 days to make.",dt="hosokawa paper disk · bamboo sheath · fine or coarse core")]},
{"n":"Printing press","a":"etching press · tabletop press","d":"Hand press made for pulling relief or intaglio prints.","s":"https://shop.takachpress.com/takach-presses",
 "t":["tabletop etching press","floor-model press","combination etching and litho press","relief press"],
 "x":[X("Tabletop intaglio press","Conrad",CON,"American tabletop etching presses from E-9 to E-37 with composite, aluminium or steel beds.",dt="E-9 to E-37 · spring-balanced pressure · bed material"),
      X("Table Top Etching Press","Takach",TK,"Portable etching presses handmade in Albuquerque, New Mexico; combination etching-litho setups.",dt="table-top or floor model")],
 "m":[["Table-top etching press",""]]},
{"n":"Screen-printing screen","a":"silk screen · screen frame","d":"Mesh screen on a frame made for hand screen printing.","s":"https://www.dickblick.com/categories/printmaking/",
 "t":["polyester mesh","nylon mesh","silk mesh","stainless-steel mesh","photo-emulsion screen","squeegee","emulsion"],
 "x":[X("Photo-emulsion screen","",SP,"Mesh stretched on a frame, coated with photo emulsion and exposed to UV through film to open the image; one screen per colour.",dt="mesh count · frame size · squeegee blade")],"m":[]},
{"n":"Etching tools and grounds","a":"etching needle · hard ground · soft ground · aquatint","d":"Needles, grounds, resins and acids used to draw and bite intaglio plates.","s":ET,
 "t":["etching needle","échoppe","hard ground","soft ground","liquid ground","aquatint rosin","ferric chloride","nitric acid"],
 "x":[X("Hard ground etching","",ET,"Waxy acid-resistant coating scratched through with a needle, then bitten in acid on copper, zinc or steel.",dt="needle · échoppe · ferric chloride for copper and zinc"),
      X("Soft ground","",ET,"Ground that stays impressionable so leaves, fabrics or prints pressed into it mark the plate.",dt="")]},
{"n":"Printmaking paper","a":"etching paper · block-printing paper","d":"Sheet made for hand printing, from cotton intaglio papers to Japanese kozo.","s":PP,
 "t":["cotton mould-made","kozo (mulberry) washi","dampened for intaglio","dry for relief"],
 "x":[X("Rives BFK","Arjomari Prioux",PP,"French mould-made cotton paper for lithography, etching, monotype and letterpress.",dt="cotton · smooth, strong"),
      X("Arches Cover","Arches",PP,"French paper for lithography, etching and relief.",dt=""),
      X("Hahnemühle Copperplate","Hahnemühle",PP,"German acid-free paper for etching, drypoint and engraving.",dt=""),
      X("Somerset Satin","St Cuthberts Mill",PP,"UK paper for intaglio and relief that handles heavy printing.",dt=""),
      X("Fabriano Rosaspina","Fabriano",PP,"Italian cotton-cellulose paper for intaglio, screen and relief.",dt=""),
      X("Stonehenge","Legion Paper",PP,"US paper for screen, relief and lithography, popular in North America.",dt=""),
      X("Kozo","Awagami Factory",PP,"Japanese mulberry-bark washi for woodblock, relief and chine-collé.",dt=""),
      X("Kitakata","Awagami Factory",PP,"Japanese absorbent paper for woodblock, chine-collé and monotype.",dt="")]},
]
S="Professional & flagship"
brands=[
B("Pfeil","Switzerland","",S,"carving gouges","Swiss maker of carving gouges and chisels.",sig=["Pfeil gouges"],s="knowledge"),
B("Flexcut","United States","","Specialist","carving tools","US maker of carving tools including a linoleum printmaking set.",sig=["Linoleum Printmaking Carving Set"],s=LT),
B("Speedball (printmaking)","United States","","Mainstream","block-printing kits","US maker of lino cutters, inks and plastic barens.",sig=["Lino cutter assortment"],s=LT),
B("Essdee","United Kingdom","","Mainstream","lino kits","UK maker of lino cutting and printing kits.",sig=["Lino Cutting & Printing Kit"],s=LT),
B("Kikuhide","Japan","","Artisan & independent","hon-baren","Workshop of Hidehiko Goto, the last known commercial maker of traditional baren.",s=BA,sig=["Hon-baren"]),
B("Conrad","United States","","Specialist","etching presses","American maker of tabletop and floor intaglio presses.",s=CON,sig=["Tabletop intaglio press"]),
B("Takach","United States","","Specialist","etching presses","Albuquerque maker of handmade etching and litho presses.",s=TK,sig=["Table Top Etching Press"]),
B("Arjomari Prioux","France","","Specialist","Rives BFK","French paper company behind Rives BFK.",s=PP,sig=["Rives BFK"]),
B("Arches","France","","Specialist","artists' paper","French mill making Arches Cover.",s=PP,sig=["Arches Cover"]),
B("Hahnemühle","Germany","1584","Heritage manufactory","fine art paper","German paper maker with Copperplate and Bugra.",sig=["Hahnemühle Copperplate"],s=PP),
B("St Cuthberts Mill","United Kingdom","","Specialist","Somerset paper","UK paper mill making Somerset Satin and Bockingford.",s=PP,sig=["Somerset Satin"]),
B("Fabriano","Italy","1264","Heritage manufactory","paper","Italian paper maker with Rosaspina and Tiepolo.",sig=["Fabriano Rosaspina"],s=PP),
B("Legion Paper","United States","","Specialist","Stonehenge","US distributor and maker of Stonehenge paper.",s=PP,sig=["Stonehenge"]),
B("Awagami Factory","Japan","","Heritage manufactory","kozo washi","Japanese washi maker producing Kozo, Kitakata and Bamboo Select papers.",s=PP,sig=["Kozo","Kitakata"]),
]
trad=[
{"n":"Mokuhanga (Japanese woodblock printing)","g":"Printmaking & ink painting","r":"Japan","p":"Edo period (1603-1868) to present","d":"Water-based colour woodblock printing, best known for ukiyo-e.","tech":"Design glued to a block, cut away around the lines, inked with brush and printed with a baren; kentō marks register multiple blocks.","mat":"Cherry wood blocks, gampi/washi paper, water-based ink, bamboo-sheathed baren","forms":["Ukiyo-e","Nishiki-e","Shin-hanga","Sōsaku-hanga"],"ctr":["Edo (Tsutaya Jūzaburō publisher)","Adachi Institute of Woodblock Prints","Takezasado"],"auth":"Technique alone does not date a print, as workshops such as Adachi reproduce with the same methods; early impressions are the most valued.","s":WJ},
{"n":"Western etching","g":"Printmaking & ink painting","r":"Europe","p":"c. 1515 to present","d":"Intaglio method of biting lines into a metal plate with acid, from Dürer and Hopfer to Rembrandt.","tech":"Waxy ground scratched through with a needle, plate bitten in acid, inked, wiped and printed under pressure on damp paper.","mat":"Copper, zinc or steel plate, hard or soft ground, ferric chloride or nitric acid","forms":["Etching","Aquatint","Soft-ground etching"],"ctr":["Augsburg (Daniel Hopfer)","Société des Aquafortistes (1862)","Edinburgh Printmakers"],"auth":"Early impressions from a numbered edition are valued higher because plates wear; a plate may exist in several states.","s":ET},
]
write('01_00',kinds,brands,trad,"Pfeil, Flexcut, Speedball, Essdee, Conrad, Takach, Rives, Hahnemühle etc from retrieved pages. Xcut and Ternes-Burton/Blick presses left out (Blick blocked, no retrieved page). Etching 'Hunt' none. Screen printing has one process archetype only; Power Grip not confirmed. Brand facts for Pfeil, Hahnemühle, Fabriano from knowledge.")
