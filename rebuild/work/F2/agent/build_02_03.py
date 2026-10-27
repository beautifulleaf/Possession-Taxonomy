import json, os
W='https://en.wikipedia.org/wiki/'
MS=W+'Mourlot_Studios'; LI=W+'Lithography'; MM=W+'Marilyn_Monroe_(Warhol)'; GG=W+'Gemini_G.E.L.'
PR='https://graphicarts.princeton.edu/2014/07/03/traite-denluminure-dart-au-pochoir-par-jean-saude'
BK='https://www.composition.gallery/journal/banksys-girl-with-balloon-2004-signed-vs-unsigned-prints/'
WO='https://pochoir.wolfsonian.org/Technique/Technique.htm'; TI=W+'Tamarind_Institute'; TG=W+'Tatyana_Grosman'
MR=W+'Moulin_Rouge:_La_Goulue'; CK=W+'Corita_Kent'; CS=W+"Campbell's_Soup_I"; SP=W+'Screen_printing'; LT=W+'Le_Taureau'
SOT='https://www.sothebys.com/en/articles/the-complete-collectors-guide-to-prints'
def v(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Lithograph","a":"litho · stone lithograph · colour lithograph",
  "d":"A print drawn in greasy crayon or ink on stone or a plate and printed by the repulsion of oil and water; offset reproductions are not original lithographs.",
  "t":["Stone lithograph","Offset lithograph","colour lithograph","transfer lithograph","signed in pencil","signed in the stone"],"s":LI,
  "x":[
   {"n":"Toulouse-Lautrec colour lithograph","a":"","d":"Flat-colour lithographic posters and prints of Montmartre nightlife, inspired by Chéret's posters.","mk":"Henri de Toulouse-Lautrec","y":"1891–1890s","s":MR,
    "v":[v("Moulin Rouge: La Goulue","Henri de Toulouse-Lautrec","1891","first lithograph; about 3,000 copies; 170 × 118.7 cm"),v("Ambassadeurs","Henri de Toulouse-Lautrec","1892"),v("Divan Japonais","Henri de Toulouse-Lautrec","1893–94"),v("Elles","Henri de Toulouse-Lautrec","1896","album")],
    "dt":"poster vs print · paper · linen-backed · margins and condition"},
   {"n":"Mourlot lithograph","a":"Mourlot-printed lithograph","d":"A fine-art lithograph drawn by a modern master directly on stone at Fernand Mourlot's Paris workshop.","mk":"Mourlot Studios","y":"1930s onward","s":MS,
    "v":[v("Le Taureau","Pablo Picasso","1945–46","11 states; edition 50 plus 18 artist's proofs"),v("Lithographs for Verve","Henri Matisse","from 1937"),v("Lithographs","Joan Miró",""),v("Lithographs","Georges Braque","")],
    "dt":"state · edition number · signature · paper and blindstamp"},
   {"n":"American workshop lithograph","a":"Tamarind lithograph · ULAE lithograph","d":"A collaborative artist–printer lithograph from the American revival workshops of the late 1950s–60s.","mk":"Tamarind Lithography Workshop","y":"1957 onward","s":TI,
    "v":[v("Tamarind edition","Tamarind Lithography Workshop","1960 onward","workshop and printer's chops; fully documented"),v("Stones","Universal Limited Art Editions","","Larry Rivers and Frank O'Hara; first ULAE project"),v("ULAE lithographs","Universal Limited Art Editions","","Jasper Johns, Robert Rauschenberg, Helen Frankenthaler"),v("Gemini editions","Gemini G.E.L.","1966 onward","Rauschenberg, Lichtenstein, Johns, Hockney")],
    "dt":"workshop chop · printer's chop · edition and proofs · documentation"}
  ]},
 {"n":"Screenprint","a":"silkscreen · serigraph · serigraphy",
  "d":"A print made by forcing ink through a mesh stencil, one screen per colour.",
  "t":["signed and numbered","unsigned edition","artist's proof","hand-cut stencil","photo stencil"],"s":SOT,
  "x":[
   {"n":"Warhol screenprint portfolio","a":"Factory Additions portfolio","d":"Portfolios of ten large screenprints in editions of 250, published by Warhol's Factory Additions from 1967.","mk":"Andy Warhol","y":"1967 onward","s":MM,
    "v":[v("Marilyn Monroe (Marilyn)","Factory Additions","1967","ten 91 × 91 cm prints; edition 250"),v("Campbell's Soup I","Factory Additions","1968","ten prints, 91.8 × 61.3 cm; printed by Salvatore Silkscreen"),v("Campbell's Soup II","Factory Additions","1969"),v("Sunday B. Morning edition","Sunday B. Morning","1970","Belgian reprint; black verso stamp; later blue stamp")],
    "dt":"original vs Sunday B. Morning stamp · signed or unsigned · colourway · edition number"},
   {"n":"Corita Kent serigraph","a":"","d":"Bright hand-pulled serigraphs combining text and colour, by the Immaculate Heart sister Corita Kent.","mk":"Corita Kent","y":"1950s–1980s","s":CK,
    "v":[v("The Lord Is with Thee","Corita Kent","1951"),v("love your brother","Corita Kent","1969")],"dt":"paper · edition · signature"},
   {"n":"Pictures on Walls screenprint","a":"POW print · Banksy print","d":"Street-art screenprints published by Pictures on Walls in signed and unsigned editions, authenticated by Pest Control.","mk":"Banksy","y":"2000s","s":BK,
    "v":[v("Girl with Balloon","Pictures on Walls","2004","150 signed and 600 unsigned; POW blindstamp")],
    "dt":"signed vs unsigned · Pest Control certificate · blindstamp · colour proof"},
   {"n":"Pop art screenprint edition","a":"","d":"Screenprints by Pop and neo-Dada artists who took up the process from 1962.","mk":"Robert Rauschenberg","y":"1962 onward","s":SP,
    "v":[v("Silkscreen works","Robert Rauschenberg","1962–64","about fifty screens"),v("Gemini G.E.L. screenprints","Gemini G.E.L.","1966 onward")],"dt":"edition · publisher · signature"}
  ]},
 {"n":"Pochoir","a":"stencil colouring · hand-stencilled print",
  "d":"A print or collotype coloured by hand through a series of cut stencils, prized for 1920s French fashion and design portfolios.",
  "t":["fashion plate","design portfolio","book illustration","single plate","bound portfolio"],"s":WO,
  "x":[{"n":"1920s French pochoir portfolio","a":"Art Deco pochoir","d":"Hand-stencilled portfolios and plates produced in Paris studios in the 1920s.","mk":"Jean Saudé","y":"1920s","s":WO,
    "v":[v("Traité d'enluminure d'art au pochoir","Jean Saudé","1925","Éditions de l'Ibis; 74 pages, 20 plates; 500 copies")],
    "dt":"complete portfolio vs loose plate · colour freshness · paper"}]}
]
def a(n,c,kf,d,s,sig,seg="Artisan & independent",f=""): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 a("Henri de Toulouse-Lautrec","France","posters","French painter-printmaker whose first lithograph was Moulin Rouge: La Goulue (1891).",MR,["Toulouse-Lautrec colour lithograph"]),
 a("Mourlot Studios","France","lithography","Paris printing house whose fine-art studio printed lithographs for Picasso, Matisse and Miró.",MS,["Mourlot lithograph"],"Heritage manufactory","1852"),
 a("Tamarind Lithography Workshop","United States","lithography","Los Angeles workshop founded by June Wayne in 1960; now Tamarind Institute, University of New Mexico.",TI,["American workshop lithograph"],"Specialist","1960"),
 a("Universal Limited Art Editions","United States","lithography","Print publisher founded by Tatyana Grosman at West Islip in 1957.",TG,["American workshop lithograph"],"Specialist","1957"),
 a("Gemini G.E.L.","United States","print editions","Los Angeles workshop and publisher of limited-edition prints and multiples.",GG,["American workshop lithograph"],"Specialist","1966"),
 a("Andy Warhol","United States","screenprints","Pop artist who popularised screenprinting and published portfolios through Factory Additions.",SP,["Warhol screenprint portfolio"]),
 a("Factory Additions","United States","print portfolios","Warhol's publishing company for screenprint editions, founded 1967.",CS,["Warhol screenprint portfolio"],"Specialist","1967"),
 a("Sunday B. Morning","Belgium","Warhol reprints","Publisher of reprints from Warhol's portfolios since 1970.",MM,["Warhol screenprint portfolio"],"Specialist"),
 a("Corita Kent","United States","serigraphs","Artist and educator (1918–1986) known for text-based serigraphs.",CK,["Corita Kent serigraph"]),
 a("Banksy","United Kingdom","street art","Anonymous street artist whose prints are authenticated by Pest Control.",BK,["Pictures on Walls screenprint"]),
 a("Pictures on Walls","","street-art prints","Publisher of Banksy screenprints, identified by its blindstamp.",BK,["Pictures on Walls screenprint"],"Specialist"),
 a("Robert Rauschenberg","United States","silkscreen","American artist who used silkscreen from 1962.",SP,["Pop art screenprint edition"]),
 a("Jean Saudé","France","pochoir","Paris pochoir colourist, author of a 1925 treatise on the technique.",PR,["1920s French pochoir portfolio"]),
]
notes="Lithograph kept with types Stone/Offset; new source Wikipedia Lithography. Screenprint keeps old Sotheby's source. Pochoir new. Lichtenstein named only as Gemini artist (no specific edition confirmed). Chagall at Mourlot not confirmed by source so left out. No traditions."
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/02_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
