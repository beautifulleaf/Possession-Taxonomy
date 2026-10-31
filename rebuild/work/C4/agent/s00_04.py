import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
CO='https://en.wikipedia.org/wiki/Copic'; FL='https://www.wellappointeddesk.com/2015/06/pigment-pen-comparison-aka-archival-waterproof-felt-tip-pens/'
BR='https://www.parkablogs.com/node/11382'; NIB='https://splendith.nl/en/blogs/nieuws/massive-nib-review'
DPM='https://www.parkablogs.com/content/review-dr-ph-martins-coloured-bombay-india-inks-set-2'; WN='https://www.parkablogs.com/comment/29841'
OH='https://parkablogs.com/content/review-ohuhu-alcohol-markers'; PO='https://hlstore.com/en/brands/uni-posca-markers/'
TB='https://www.cowlingandwilcox.com/artist-pens/30537-tombow-abt-dual-brush-pen-box-of-12-primary-colours'
kinds=[
{"n":"Drawing ink","a":"India ink · Indian ink · art ink","d":"Liquid ink made for drawing and painting with pen or brush.","s":"https://www.dickblick.com/categories/drawing/inks/",
 "t":["waterproof pigment ink","dye ink","shellac-based","acrylic ink","coloured ink","white ink"],
 "x":[X("Bombay India Ink","Dr. Ph. Martin's",DPM,"Pigmented waterproof ink in 24 colours; most are transparent, black and white opaque.",dt="24 colours · 15 ml plastic or 30 ml glass bottles"),
      X("Black India Ink","Winsor & Newton",WN,"Waterproof, lightfast black that flows well; sold in 14 ml square glass bottles.",dt="14 ml bottle")],
 "m":[["Black Cat Waterproof India Ink","Blick Art Materials"],["Bleedproof White","Dr. Ph. Martin's"],["Abstract Acrylic Inks","Sennelier"]]},
{"n":"Alcohol markers","a":"art markers · Copic-type markers","d":"Alcohol-ink blending markers for illustration, manga and colouring.","s":"https://www.deserres.ca/collections/art-graphic-markers",
 "t":["double-ended","refillable","chisel and brush nib","student set"],
 "x":[X("Copic","Too Corporation",CO,"Refillable Japanese alcohol markers with 358 colours and varied nibs; the professional reference.","1987",dt="358 colours · refill ink in 12 ml and 32 ml bottles · Sketch, Ciao and Classic bodies"),
      X("Ohuhu Alcohol Markers","Ohuhu",OH,"Budget dye-based alternative with 481 colours at review time and replaceable tips.",dt="sets of 24 to 320 · six nib series")],
 "m":[["Ad Markers","Chartpak"],["Premier Dual-Ended Chisel Tip Markers","Prismacolor"],["Promarker","Winsor & Newton"],["Studio Double-Ended Alcohol Art Markers","Blick Art Materials"]]},
{"n":"Fineliner and technical drawing pen","a":"drawing pen · pigment liner","d":"Fine-tipped archival pen for line work, comics and technical drawing.","s":"https://www.dickblick.com/categories/drawing/markers/",
 "t":["archival pigment ink","refillable technical pen","coloured fineliner"],
 "x":[X("Pigma Micron","Sakura",FL,"Archival waterproof pen with seven tip sizes; reviewer rated its black the darkest tested.",dt="seven tip sizes · sizing non-standard (03 is 0.35 mm)"),
      X("Multiliner SP","Copic",FL,"Refillable aluminium pen with replaceable nib; eight black tip sizes 0.03 to 0.7 mm plus brush.",dt="0.03 to 0.7 mm · refillable"),
      X("Pigment Liner","Staedtler",FL,"Archival waterproof fineliner in five tip sizes; black only.",dt="five tip sizes"),
      X("PITT Artist Pen","Faber-Castell",FL,"Acid-free archival pigment pens.",dt="felt tip and brush")],
 "m":[["OHTO Graphic Liner","OHTO"],["Zig Millennium","Kuretake"]]},
{"n":"Brush pens","a":"brush markers","d":"Pens with a flexible brush nib for lettering and brush-line work.","s":"https://arttoart.net/art-markers-alcohol-markers",
 "t":["felt tip","synthetic bristle","sable bristle","cartridge-refillable","water-based dual tip"],
 "x":[X("ABT Dual Brush Pen","Tombow",TB,"Water-based twin-tip pen with brush and fine ends; over 100 shades; blends with water.",dt="over 100 colours · water-based"),
      X("Pocket Brush Pen","Pentel",BR,"Synthetic-bristle brush pen with waterproof ink, refilled with Pentel cartridges.",dt="synthetic bristle · waterproof"),
      X("Zig Brushables","Kuretake",BR,"Dual felt-tip pen with black and warm grey, waterproof pigment ink; disposable.",dt="dual felt tip"),
      X("No. 40 Brush Pen","Kuretake",BR,"Sable-hair brush pen taking Kuretake cartridges or a converter.",dt="sable hair")],
 "m":[["Fibralo Brush Markers","Caran d'Ache"],["Pitt Artist Brush Pens","Faber-Castell"],["Brushmarker Pro","Karin"],["Studio Brush Markers","Blick Art Materials"]]},
{"n":"Paint markers","a":"paint pens","d":"Opaque paint markers for canvas, wood, glass and metal.","s":"https://www.deserres.ca/collections/art-graphic-markers",
 "t":["water-based","oil-based","extra-fine to broad tip"],
 "x":[X("Posca","Uni Mitsubishi Pencil",PO,"Water-based opaque paint marker released in 1983; popular with graffiti artists; tips PC-1M to PC-5M.","1983",dt="PC-1M 0.7 mm · PC-3M 0.9-1.3 mm · PC-5M 1.8-2.5 mm")],
 "m":[["Posca Brush Tip Paint Markers","Posca"]]},
{"n":"Dip pen and nib","a":"nib pen · pointed pen","d":"Pen holder and metal nib dipped in ink for calligraphy, comics and drawing.","s":NIB,
 "t":["pointed nib","mapping (round) nib","oblique holder","straight holder"],
 "x":[X("Zebra G","Zebra",NIB,"Japanese semi-flexible nib giving thin upstrokes; a standard for comics and calligraphy; Titanium version lasts longer.",dt="semi-flexible · G Titanium"),
      X("Nikko G","Nikko",NIB,"Semi-flexible nib with a sharp point, recommended for learning.",dt="semi-flexible"),
      X("Hunt nibs","Hunt",NIB,"Hunt nibs range from flexible (99, 101) to inflexible mapping nibs (107, 108).",dt="mapping nibs 107, 108")]},
]
brands=[
B("Too Corporation","Japan","1969","Professional & flagship","Copic markers","Japanese maker of Copic; formerly Izumiya, renamed Too in 1992.",s=CO,sig=["Copic"]),
B("Sakura","Japan","1921","Mainstream","Pigma Micron","Japanese maker of the Pigma Micron fineliner and Cray-Pas.",sig=["Pigma Micron"],s="knowledge"),
B("Uni Mitsubishi Pencil","Japan","1886","Mainstream","Posca","Japanese pencil and pen maker; made the Posca paint marker from 1983.",s=PO,sig=["Posca"]),
B("Tombow","Japan","1913","Mainstream","brush pens","Japanese stationery maker of the ABT Dual Brush Pen.",sig=["ABT Dual Brush Pen"]),
B("Dr. Ph. Martin's","United States","","Specialist","Bombay inks","Maker of Bombay India Ink and coloured art inks.",sig=["Bombay India Ink"],s=DPM),
B("Winsor & Newton","United Kingdom","1832","Professional & flagship","artists' colours","London colourman with a black India ink.",s="https://en.wikipedia.org/wiki/Winsor_%26_Newton",sig=["Black India Ink"]),
B("Staedtler","Germany","1835","Professional & flagship","pencils","German pencil and pen maker with the Pigment Liner.",sig=["Pigment Liner"]),
B("Copic","Japan","1987","Professional & flagship","alcohol markers","Marker brand of Too Corporation.",s=CO,sig=["Copic","Multiliner SP"]),
B("Ohuhu","China","","Value","budget markers","Budget alcohol-marker brand sold mainly online.",s=OH,sig=["Ohuhu Alcohol Markers"]),
B("Pentel","Japan","1945","Mainstream","brush pens","Japanese pen maker of the Pocket Brush Pen.",sig=["Pocket Brush Pen"]),
B("Kuretake","Japan","1902","Heritage manufactory","brush pens, sumi","Japanese maker of Zig brush pens and calligraphy inks.",sig=["Zig Brushables","No. 40 Brush Pen"]),
B("Zebra","Japan","1897","Mainstream","G nib","Japanese pen maker whose G nib is a comic-art standard.",sig=["Zebra G"]),
B("Nikko","Japan","","Specialist","G nib","Japanese nib maker of the Nikko G.",sig=["Nikko G"],s=NIB),
B("Hunt","United States","","Specialist","dip pen nibs","Maker of the Hunt range of drawing and mapping nibs.",sig=["Hunt nibs"],s=NIB),
B("Faber-Castell","Germany","1761","Professional & flagship","pencils, pens","German writing and art maker with PITT Artist Pens.",sig=["PITT Artist Pen"]),
]
write('00_04',kinds,brands,[],"Uni Posca moved from Other drawing pens to Paint markers; Higgins and Sennelier ink archetypes, Hunt 102 specifics and Copic Sketch/Ciao years left out (no retrieved page confirmed them). Pentel/Zebra/Kuretake brand facts from knowledge; Hunt 102 itself not in the retrieved page, so the archetype is the Hunt nib family.")
