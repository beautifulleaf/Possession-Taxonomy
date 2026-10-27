import sys; sys.path.insert(0,'work/C4/agent'); from w import w
WP="https://en.wikipedia.org/wiki/Watercolor_paper"; CN="https://en.wikipedia.org/wiki/Canson"; PP="https://finearttutorials.com/guide/best-pastel-paper/"
SB="https://www.stillmanandbirn.com/sketchbook_system.php"; CL="https://madegooddesigns.com/claessens-brand-guidelines/"; SM="https://www.parkablogs.com/picture/review-strathmore-400-series-mixed-media-paper-300gsm"; FA="https://www.deckleedge.co.za/product/fabriano-artistico-paper/"
def X(n,mk,d,s,v=(),y="",a="",dt=""):
    o={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
    return {k:val for k,val in o.items() if val or k in("mk","s")}
WD="surface (hot-pressed, cold-pressed, rough) · weight (gsm/lb) · white shade · sheet, pad, block or roll"
PD="surface (sanded, velour, laid, honeycomb) · weight · colour range"
kinds=[
{"n":"Watercolour paper","a":"aquarelle paper · watercolour block · watercolour pad","d":"Heavy sized paper made to take watercolour washes, sold as sheets, pads and blocks.",
 "t":["100% cotton","cellulose (wood pulp)","mould-made","handmade","machine-made","synthetic","hot-pressed (smooth)","cold-pressed (NOT)","rough","90 lb / 190 gsm","140 lb / 300 gsm","300 lb / 640 gsm","sheet","pad","block (glued on four sides)","roll"],
 "x":[X("Arches Aquarelle","Arches","French watercolour paper made at Arches since about 1620; the benchmark cotton sheet.",WP,
        [("Arches Watercolor Blocks","Arches","",""),("Arches Watercolor Pads","Arches","","")],y="c. 1620",dt=WD),
      X("Saunders Waterford","St Cuthberts Mill","British watercolour paper made by St Cuthberts Mill.",WP,[("Bockingford","St Cuthberts Mill","","the mill's lower-cost watercolour paper")],dt=WD),
      X("Fabriano Artistico","Fabriano","Italian 100% cotton mould-made watercolour paper in Traditional White and Extra White.",FA,
        [("Artistico Enhanced Watercolor Blocks","Fabriano","",""),("Traditional White","Fabriano","","no optical brighteners"),("Extra White","Fabriano","","no optical brighteners")],dt=WD),
      X("Canson Montval","Canson","Canson's range of watercolour papers.",CN,[("XL Watercolor Pads","Canson","","student range")],dt=WD),
      X("Yupo","Legion Paper","Ultra-smooth synthetic paper used for watercolour.",WP,[("Yupo Synthetic Paper Pads","Legion Paper","","")])],
 "m":[["1264 Watercolor Pad","Fabriano"],["Studio Watercolor Pads","Fabriano"],["Concept Watercolour Joy Pads","Hahnemühle"],["Watercolor Bookmark Pad","Hahnemühle"],["400 Series Watercolor Paper Pads","Strathmore"]],
 "s":"https://www.dickblick.com/categories/paper/watercolor-paper/"},
{"n":"Drawing and mixed-media paper","a":"cartridge paper · drawing paper · mixed-media paper · bristol","d":"Paper sized and weighted for pencil, ink, marker and light washes.",
 "t":["cartridge (drawing)","mixed media","bristol (smooth or vellum)","vellum finish","smooth","pad","sheet","roll"],
 "x":[X("Strathmore series papers","Strathmore","American paper range graded by series number from student to artist quality.",SM,
        [("300 Series","Strathmore","","student grade"),("400 Series Mixed Media","Strathmore","","300 gsm vellum finish, 15-sheet pads"),("500 Series","Strathmore","","artist grade, some 100% cotton")],dt="series · weight · surface"),
      X("Canson drawing papers","Canson","French drawing papers from Canson, including \"C\" à Grain and 1557.",CN,[("\"C\" à Grain","Canson","",""),("1557","Canson","","")])],
 "s":SM},
{"n":"Pastel paper","a":"pastel card · sanded paper · Ingres paper","d":"Toothed, often tinted paper or card that grips pastel and charcoal.",
 "t":["sanded","velour","laid (Ingres)","honeycomb","tinted","board","sheet","pad"],
 "x":[X("Canson Mi-Teintes","Canson","Coloured paper of about 60% cotton in 60 colours, with a honeycomb face and vellum back.",CN,
        [("Mi-Teintes Touch","Canson","","sanded, 350 gsm, takes a little water")],dt=PD),
      X("Clairefontaine Pastelmat","Clairefontaine","Coated, sanded 360 gsm pastel card in 14 colours.",PP,dt=PD),
      X("Sennelier La Carte","Sennelier","Sanded 360 gsm pastel card on a bristol base for dry media.",PP,dt=PD),
      X("Art Spectrum Colourfix","Art Spectrum","Silica-coated sanded paper in 20 colours for wet and dry media.",PP,dt=PD),
      X("UART Pastel Paper","UART","Sanded paper sold in grit grades 400 to 800.",PP,dt="grit grade · colour"),
      X("Hahnemühle Velour","Hahnemühle","Velvety coated pastel paper for dry media.",PP,dt=PD),
      X("Fabriano Tiziano","Fabriano","Ingres-surface pastel paper of about 40% cotton rag.",PP,dt=PD)],
 "m":[["Pastelbord","Ampersand"],["Murano","Daler-Rowney"],["Ingres","Hahnemühle"]],
 "s":PP},
{"n":"Sketchbook","a":"sketch book · art journal","d":"Bound book of blank drawing paper made for sketching.",
 "t":["hardbound","wire-bound","softcover","landscape","portrait","square","cartridge paper","watercolour paper","toned paper"],
 "x":[X("Stillman & Birn sketchbook system","Stillman & Birn","Sketchbook range named by Greek-letter series, each a fixed paper weight, surface and colour.",SB,
        [("Alpha","Stillman & Birn","","150 gsm medium grain, white"),("Beta","Stillman & Birn","","270 gsm cold press, white"),("Gamma","Stillman & Birn","","150 gsm medium grain, ivory"),("Delta","Stillman & Birn","","270 gsm cold press, ivory"),("Epsilon","Stillman & Birn","","150 gsm smooth, white"),("Zeta","Stillman & Birn","","270 gsm smooth, white"),("Nova","Stillman & Birn","","150 gsm medium grain, beige, grey or white")],dt="series · binding · size")],
 "s":"https://www.stillmanandbirn.com/sketchbook_system.php"},
{"n":"Stretched canvas","a":"","d":"Artists' canvas stretched on a frame, ready to paint.",
 "t":["cotton duck","linen","studio (standard) depth","gallery (deep) depth","acrylic-primed (universal)","oil-primed"],
 "m":[["Classic Cotton Stretched Canvas","Art Alternatives"],["Liquitex Basics Stretched Cotton Canvas","Liquitex"],["Blick Premier Oil Primed Belgian Linen Canvas","Blick Art Materials"],["artPOP! Stretched Canvas","artPOP!"]],
 "s":"https://www.dickblick.com/categories/canvas/stretched-canvas/"},
{"n":"Canvas board and painting panel","a":"canvas panel · gesso board · painting panel","d":"Canvas laid on board, or a rigid primed panel, made to paint on.",
 "t":["canvas board","wood panel","gessoed hardboard","aluminium composite panel","cradled panel"],
 "s":"https://www.dickblick.com/categories/canvas/"},
{"n":"Canvas roll","a":"canvas by the metre","d":"Unstretched artists' canvas sold by the roll or metre.",
 "t":["cotton duck","linen","jute","blend","unprimed","oil-primed","universal-primed","absorbent ground"],
 "x":[X("Claessens Belgian linen","Claessens","Belgian linen canvas on the roll, primed in Waregem since 1906.",CL,y="1906",dt="weave number and texture · priming (oil, universal, absorbent) · roll width")],
 "s":"https://www.dickblick.com/categories/canvas/"},
{"n":"Stretcher bar","a":"stretcher strip","d":"Wooden bar sold in pairs to build a frame for stretching canvas.",
 "t":["standard","heavy-duty","gallery depth","keyed (with wedges)","cross-brace"],
 "s":"https://www.dickblick.com/categories/canvas/"}]
K="knowledge"
def B(n,c,f,seg,kf,d,s,sig=()):
    o={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":list(sig)}
    return {k:v for k,v in o.items() if v}
brands=[
 B("Arches","France","c. 1620","Heritage manufactory","watercolour paper","French paper mill making watercolour paper since about 1620.",WP,["Arches Aquarelle"]),
 B("St Cuthberts Mill","United Kingdom","","Heritage manufactory","watercolour paper","British mill making Saunders Waterford and Bockingford.",WP,["Saunders Waterford"]),
 B("Fabriano","Italy","1264","Heritage manufactory","paper","Italian papermaker from the town where paper was made from the 13th century; part of Fedrigoni since 2011.",WP,["Fabriano Artistico"]),
 B("Canson","France","1557","Heritage manufactory","drawing and pastel paper","Annonay paper maker founded by the Montgolfier family; owned by F.I.L.A. since 2016.",CN,["Canson Mi-Teintes"]),
 B("Strathmore","United States","","Mainstream","drawing paper","American artists' paper brand organised by series number.",SM,["Strathmore series papers"]),
 B("Stillman & Birn","United States","","Specialist","sketchbooks","American sketchbook maker.",K,["Stillman & Birn sketchbook system"]),
 B("Clairefontaine","France","","Mainstream","paper, Pastelmat","French paper and stationery maker.",K,["Clairefontaine Pastelmat"]),
 B("Sennelier","France","1887","Heritage manufactory","pigments, pastel","Paris colourman founded by Gustave Sennelier.",K,["Sennelier La Carte"]),
 B("Art Spectrum","Australia","","Specialist","Colourfix","Australian art materials maker.",K,["Art Spectrum Colourfix"]),
 B("UART","United States","","Specialist","sanded pastel paper","American maker of sanded pastel paper.",K,["UART Pastel Paper"]),
 B("Hahnemühle","Germany","","Heritage manufactory","fine art paper","German fine-art paper mill.",K,["Hahnemühle Velour"]),
 B("Legion Paper","United States","","Specialist","Yupo, Stonehenge","American fine paper distributor of Yupo and Stonehenge.",K,["Yupo"]),
 B("Claessens","Belgium","1906","Heritage manufactory","linen canvas","Family firm founded by Victor Claessens in Waregem making artists' canvas.",CL,["Claessens Belgian linen"]),
]
notes=("Blick Academic, Blick Premier Heavyweight Cotton and Blick Studio Linen stretched canvases trimmed as house-brand SKU duplicates (one Blick Belgian-linen kept). "
 "Belle Arti canvas, Sennelier/Hahnemühle watercolour lines and Saunders Waterford colour variants left out: no retrieved page confirmed them (artsupplies.co.uk blocked). "
 "Hahnemühle and Strathmore watercolour pads kept as flat models. Brand facts for Stillman & Birn, Clairefontaine, Art Spectrum, UART, Hahnemühle and Legion Paper from knowledge with founding years omitted.")
w('C4','00_02',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
