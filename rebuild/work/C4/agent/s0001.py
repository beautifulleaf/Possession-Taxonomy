import sys; sys.path.insert(0,'work/C4/agent'); from w import w
WN="https://en.wikipedia.org/wiki/Winsor_%26_Newton"; PK="https://www.parkablogs.com/content/review-winsor-newton-series-7-kolinsky-sable-brush"
LC="https://linesandcolors.com/2018/05/10/french-box-easels-field-easels-and-other-plein-air-painting-systems/"; ET="https://finearttutorials.com/guide/types-of-easels/"
ST="https://www.virtualartacademy.com/strada-pochade-box/"; GB="https://www.judsonsart.com/products/guerrilla-painter-9x12-guerrilla-box-v4-0"
OB="https://uk.winsornewton.com/blogs/guides/oil-paint-brush-guide"; CA="https://www.cassart.co.uk/blog/choose-paintbrush.htm"
MB="https://opusartsupplies.com/products/masters-brush-cleaner-and-preservers"; PL="https://drawpaintacademy.com/artist-palettes/"; RG="https://artsavingsclub.co.za/product/idea-line-palette-knives-sets-rgm"
def X(n,mk,d,s,v=(),y="",a="",dt=""):
    o={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
    return {k:val for k,val in o.items() if val or k in("mk","s")}
BD="size (000–24) · shape (round, flat, mop, rigger) · handle length"
ED="material (beech, oak, aluminium) · maximum canvas height · tilt range"
kinds=[
{"n":"Watercolour and soft-hair brush","a":"artist brush · sable brush · watercolour brush","d":"Soft-haired brush for watercolour, gouache and ink, made of sable, squirrel or synthetic fibre.",
 "t":["Kolinsky sable","red sable","squirrel","synthetic sable","sable-synthetic mix","round","flat","filbert","rigger","mop","dagger","water brush (reservoir handle)","travel (pocket) brush"],
 "x":[X("Series 7","Winsor & Newton","Kolinsky sable round made in England, developed for Queen Victoria in 1866; the reference sable brush.",WN,
        [("Series 7 Finest Kolinsky Sable","Winsor & Newton","","current short-handled line")],y="1866",dt=BD),
      X("Escoda Reserva","Escoda","Kolinsky sable watercolour brush line, linked to Tajmyr sable.",PK,[("Reserva Series 1212","Escoda","","round")],dt=BD),
      X("Da Vinci Maestro","da Vinci Brushes","Kolinsky sable watercolour brush line, also made as a travel pocket brush.",PK,[("Series 10","da Vinci Brushes","",""),("Series 35","da Vinci Brushes","","")],dt=BD),
      X("Rosemary & Co Series 33","Rosemary & Co","Kolinsky sable round from the British brushmaker.",PK,[("Series 441","Rosemary & Co","","")],dt=BD),
      X("Nevskaya Palitra Kolinsky","Nevskaya Palitra","Kolinsky watercolour brush from the St Petersburg colour maker.",PK,dt=BD)],
 "m":[["Aquash Water Brush","Pentel"],["Ultra Round","Loew-Cornell"],["Series 6228","Isabey"],["8404","Raphaël"],["Artists' Synthetic Sable Mix","Cass Art"]],
 "s":"https://www.dickblick.com/categories/brushes/"},
{"n":"Oil and acrylic brush","a":"hog brush · bristle brush · long-handled brush","d":"Stiff long-handled brush of hog bristle or firm synthetic fibre for oil and heavy acrylic paint.",
 "t":["hog bristle","synthetic (flagged)","synthetic grey","mongoose","round","flat","bright","filbert","fan","long handle"],
 "x":[X("Winsor & Newton Artists' Hog","Winsor & Newton","Natural hog-bristle oil brush line graded for stiffness, flags and shape retention.",OB,
        [("Professional Oil Synthetic Hog","Winsor & Newton","","synthetic fibres replicating hog flags")],dt="hog grade (best, better, good) · shape · size")],
 "m":[["Artists' Hog Bristle","Cass Art"],["Artists' Synthetic Grey","Cass Art"]],
 "s":OB},
{"n":"Palette knife","a":"painting knife · spatula","d":"Thin flexible steel blade on a handle, used to mix paint on the palette or lay it on the canvas.",
 "t":["palette knife (mixing)","painting knife (cranked, for applying)","trowel","diamond","teardrop","wooden handle","one-piece stainless steel"],
 "x":[X("RGM painting knives","RGM","Italian hand-finished painting and palette knives made since 1961.",RG,
        [("Idea Line","RGM","","one-piece non-welded stainless steel, no separate handle")],y="1961",dt="blade number and shape · flex · handle")],
 "s":RG},
{"n":"Palette","a":"mixing palette · paint palette","d":"Flat surface or tray on which paint is laid out and mixed.",
 "t":["hand-held wooden (thumb-hole)","tabletop wood","glass","disposable paper pad","stay-wet (acrylic)","plastic","porcelain or ceramic well","enamel tin (watercolour box)"],
 "m":[["Palette, Maple Wood","New Wave"],["Grey Pad","New Wave"],["POSH Glass Artist Palette","New Wave"]],
 "s":PL},
{"n":"Easel","a":"painting easel · artist's easel","d":"Stand that holds a canvas or board while it is painted.",
 "t":["studio","field","tabletop","wall-mounted","radial (tilts flat)","wood","aluminium"],
 "x":[X("H-frame easel","","Four-legged studio easel, the most stable support for large canvases.",ET,
        [("M-07","Mabef","","Italian beech H-frame, canvases to 84½ in"),("Santa Fe II","Richeson","","double-mast oak H-frame, canvases to 106 in"),("Medium-Duty H-Frame Easel","Blick Art Materials","","")],dt=ED),
      X("A-frame (lyre) easel","","Three-legged folding studio easel with a sliding canvas holder.",ET,[("A-Frame Studio Easel","Mabef","","canvases to 47 in")],dt=ED),
      X("French box easel","Jullian","Folding field easel combined with a paint box; Jullian credits its founder with the design.",LC,
        [("Full French easel","Jullian","",""),("Half French easel","Jullian","",""),("Rexy Watercolor Easel","Jullian","","more horizontal surface, removable paint box"),("Blick French Easel by Jullian","Jullian","","retailer-labelled"),("French Sketch Box Easel M22","Mabef","",""),("Weston Half French Easel","Richeson","","")],dt="full or half box · wood or metal"),
      X("Gloucester (Anderson) easel","","Tripod field easel used in early-19th-century northern Europe and revived in the US by Emile Gruppe.",LC,
        [("Take It Easel","Take It Easel","",""),("Beauport Easel","","","variation")]),
      X("Tabletop easel","","Small easel that stands on a table for small works.",ET,[("Table Easel","Mabef","","beech"),("Tabletop Easel","Richeson","","hardwood, tilts 0–85°")],dt=ED)],
 "m":[["#500 Aluminum Easel","Testrite"],["Versatile H-Frame Easel","Meeden"],["3-in-1 Floor Easel","artPOP!"]],
 "s":"https://www.dickblick.com/categories/easels/"},
{"n":"Pochade and plein-air box","a":"pochade box · paint box easel · field box","d":"Portable box combining palette, paint storage and a panel holder for painting outdoors.",
 "t":["lap or tripod-mounted","wood","aluminium","wet-panel carrier","oil","watercolour","pastel"],
 "x":[X("Guerrilla Box","Guerrilla Painter","Basswood pochade box with a sliding palette and wet-panel storage in the lid.",GB,
        [("9x12 Guerrilla Box V4.0","Guerrilla Painter","","holds two wet 9×12 in panels; 3 lb 13 oz"),("Campaign Box","Guerrilla Painter","","clamps to tripod with Flex Easel")],dt="panel size · tripod mount"),
      X("Strada pochade box","Strada","Aluminium pochade box with a single hand screw.",ST,[("Strada Mid","Strada","","3 lb 4 oz; panels to 16 in"),("Strada Mini","Strada","","")],dt="size · palette depth"),
      X("Coulter Easel","Art Box and Panel","Panel holder and fold-out palette on a metal tripod, designed by James Coulter.",LC)],
 "m":[["Open Box M","Open Box M"],["Pochade Box","Mabef"],["Pochade Box Easel","Richeson"],["EasyL Lite","EasyL"],["Soltek Easel","Soltek"]],
 "s":ET},
{"n":"Brush cleaner","a":"brush soap · brush washer","d":"Soap, solvent or washer made for cleaning artists' brushes.",
 "t":["solid brush soap","liquid cleaner","solvent","brush washer tank"],
 "m":[["\"The Masters\" Brush Cleaner and Preserver","General Pencil"]],
 "s":"https://www.dickblick.com/categories/brushes/"}]
K="knowledge"
def B(n,c,f,seg,kf,d,s,sig=(),lines=()):
    o={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":list(sig),"lines":list(lines)}
    return {k:v for k,v in o.items() if v}
brands=[
 B("Winsor & Newton","United Kingdom","1832","Professional & flagship","artists' colours, Series 7","London colourman founded by William Winsor and Henry Newton.",WN,["Series 7"]),
 B("Escoda","Spain","","Specialist","sable brushes","Spanish artists' brushmaker.",K,["Escoda Reserva"]),
 B("da Vinci Brushes","Germany","","Specialist","artists' brushes","German artists' brushmaker from Nuremberg.",K,["Da Vinci Maestro"]),
 B("Rosemary & Co","United Kingdom","","Artisan & independent","handmade brushes","British maker of handmade artists' brushes sold direct.",K,["Rosemary & Co Series 33"]),
 B("Nevskaya Palitra","Russia","","Mainstream","watercolour","St Petersburg artists' colour and brush maker, known for White Nights watercolour.",K,["Nevskaya Palitra Kolinsky"]),
 B("Jullian","France","","Heritage manufactory","French box easel","French easel maker credited with the French box easel.",LC,["French box easel"]),
 B("Mabef","Italy","","Mainstream","beech easels","Italian maker of beech-wood easels.",ET),
 B("Richeson","United States","","Mainstream","easels","American art-materials maker of easels and pochade boxes.",ET),
 B("RGM","Italy","1961","Specialist","painting knives","Italian maker of painting and palette knives.",RG,["RGM painting knives"]),
 B("Guerrilla Painter","United States","","Specialist","pochade boxes","Plein-air box and easel line sold by Judson's Art Outfitters.",GB,["Guerrilla Box"]),
 B("Strada","","","Specialist","aluminium pochade boxes","Maker of aluminium pochade boxes and palettes.",ST,["Strada pochade box"]),
 B("Art Box and Panel","","","Artisan & independent","Coulter Easel","Maker of the Coulter Easel plein-air system.",LC,["Coulter Easel"]),
 B("General Pencil","United States","","Mainstream","pencils, brush soap","American pencil maker that also makes The Masters brush cleaner.",MB),
]
notes=("Blick Studio and Meeden easel SKUs trimmed (kept one Blick H-frame as a version, one Meeden in m); Blick Studio activity/convertible/tabletop easels, Meeden Deluxe and XL and Blick Studio Table Easel by Jullian dropped as SKU noise. "
 "Pentel Aquash kept in m: no retrieved page to source a 'water brush' archetype. Open Box M kept as a model only (named in a comment; maker not confirmed). "
 "Synthetic sable kept as a type; no synthetic-sable line archetype sourced. Escoda, da Vinci, Rosemary & Co and Nevskaya Palitra brand facts from knowledge, founding years left out. Rosemary Series 441, da Vinci Series 10/35 and Escoda Series 1212 appear only as reader comments on the review page.")
w('C4','00_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
