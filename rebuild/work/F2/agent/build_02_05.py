import json, os
W='https://en.wikipedia.org/wiki/'
PO=W+'Poster'; GI=W+'Gismonda'; CA=W+'Cassandre'; KA=W+'Edward_McKnight_Kauffer'; FAP=W+'Federal_Art_Project'
GC=W+'Gicl%C3%A9e'; MB=W+'Josef_M%C3%BCller-Brockmann'; KM=W+'King_and_McGaw'; DE='https://verdane.com/?p=2930'
S6='https://madegooddesigns.com/society6-brand-guidelines/'; IK='https://www.ikea.com/de/en/cat/posters-10787/'
MS=W+'Mourlot_Studios'; MR=W+'Moulin_Rouge:_La_Goulue'
def v(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Vintage poster","a":"original poster · antique poster · affiche",
  "d":"An original printed poster from its period of issue, usually a lithograph or screenprint made for the street, collected as an object.",
  "t":["stone lithograph","offset lithograph","screenprint","linen-backed","paper-backed","folded","original issue","later reprint"],"s":PO,
  "x":[
   {"n":"Belle Époque poster","a":"Art Nouveau poster","d":"Large colour lithographs of the 1880s–1900s Paris street, led by Chéret, Mucha and Toulouse-Lautrec.","mk":"Jules Chéret","y":"1880s–1900","s":PO,
    "v":[v("Chéret posters and chérettes","Jules Chéret","","more than 1,000 advertisements"),v("Maîtres de l'Affiche","Jules Chéret","1895–1900","poster series"),
         v("Gismonda","Alphonse Mucha","1894","for Sarah Bernhardt"),v("Moulin Rouge: La Goulue","Henri de Toulouse-Lautrec","1891","about 3,000 copies")],
    "dt":"original vs Maîtres de l'Affiche plate vs reprint · linen backing · margins · restoration"},
   {"n":"Art Deco travel poster","a":"","d":"Bold, simplified travel and transport posters of the 1920s–30s for railways, liners and city transport.","mk":"Cassandre","y":"1920s–1930s","s":CA,
    "v":[v("Nord Express","Cassandre","1927"),v("Étoile du Nord","Cassandre","1927"),v("Dubonnet","Cassandre","1932"),v("Normandie","Cassandre","1935")],
    "dt":"original vs later reprint · size · linen backing · condition"},
   {"n":"London Underground poster","a":"London Transport poster","d":"Posters commissioned from artists in many styles for the Underground and London Transport.","mk":"Edward McKnight Kauffer","y":"1910s onward","s":KA,
    "v":[v("The North Downs","Edward McKnight Kauffer","1915"),v("Godstone","Edward McKnight Kauffer","1915"),v("Victoria and Albert Museum","Edward McKnight Kauffer","1921"),v("Winter Sales","Edward McKnight Kauffer","1922")],
    "dt":"original vs reprint · condition"},
   {"n":"WPA poster","a":"Federal Art Project poster","d":"Hand-made and silkscreened public-information posters of the US Federal Art Project poster division; about 2,000 survive in collections.","mk":"WPA Federal Art Project","y":"1935–1943","s":FAP,
    "v":[v("Poster Division (New York and 18 states)","WPA Federal Art Project","1935–1943","headed by Richard Floethe; about 35,000 designs")],"dt":"silkscreen vs hand-painted · state unit · condition"},
   {"n":"Swiss International Style poster","a":"Swiss Style poster","d":"Grid-based posters with sans-serif type and photography, from Zürich and Basel designers.","mk":"Josef Müller-Brockmann","y":"1950s–1960s","s":MB,
    "v":[v("Tonhalle (Musica Viva) concert posters","Josef Müller-Brockmann","1950 onward"),v("Juni-Festwochen Zürich","Josef Müller-Brockmann","1957"),v("Der Film","Josef Müller-Brockmann","1960")],
    "dt":"screenprint or offset · condition"},
   {"n":"Vintage film poster","a":"movie poster","d":"An original cinema poster issued for display, collected by format and issue rather than as a title.","mk":"","y":"1910s onward","s":PO,
    "v":[],"dt":"one-sheet, three-sheet, six-sheet · country of issue · original vs re-release · folded or rolled · linen backing"}
  ]},
 {"n":"Exhibition and art poster","a":"museum poster · art exhibition poster",
  "d":"A poster made for an art exhibition or museum, often designed or drawn by the exhibiting artist and sometimes printed as a lithograph.",
  "t":["lithographic poster","offset poster","signed","with text","before letters"],"s":MS,
  "x":[
   {"n":"Mourlot exhibition poster","a":"","d":"Exhibition posters printed in lithography by Mourlot, including artist-drawn posters for the masters it printed.","mk":"Mourlot Studios","y":"1930 onward","s":MS,
    "v":[v("Delacroix exhibition poster","Mourlot Studios","1930"),v("Maîtres de l'Art indépendant","Henri Matisse","1937","with Bonnard")],"dt":"lithograph vs offset · original vs reissue · size"},
   {"n":"Museum-shop exhibition poster","a":"","d":"Posters and prints from museum collections and exhibitions, made for museum shops.","mk":"King & McGaw","y":"1982 onward","s":KM,
    "v":[v("Mourlot archive posters","King & McGaw","2015","pop-up showing Mourlot lithographic posters")],"dt":"size · paper · framed or unframed"}
  ]},
 {"n":"Giclée and fine-art reproduction","a":"giclée · inkjet print · fine-art print",
  "d":"A reproduction (not an original print) of a painting, photograph or digital artwork made on a large-format inkjet printer on paper or canvas.",
  "t":["pigment ink","dye ink","on paper","on canvas","signed limited edition","open edition"],"s":GC,
  "x":[{"n":"Iris giclée","a":"digigraph","d":"The first fine-art inkjet prints, made on a modified Iris printer at Nash Editions and named giclée about 1990.","mk":"Nash Editions","y":"c. 1990","s":GC,
    "v":[v("Term coined","Jack Duganne","c. 1990–91","at Nash Editions")],"dt":"inks · paper · edition"}]},
 {"n":"Canvas and framed art print","a":"wall art · art print · poster print · canvas print",
  "d":"An inexpensive printed picture, poster or canvas sold ready to hang for decorating a home.",
  "t":["poster (unframed)","framed print","canvas print","multi-pack","metal print"],"s":IK,
  "m":[["BILD poster","IKEA"],["Posters and prints","Desenio"],["Art prints and framed prints","King & McGaw"],["Art prints, canvas prints and framed posters","Society6"]]}
]
def a(n,c,kf,d,s,sig,seg="Artisan & independent",f=""): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 a("Jules Chéret","France","posters","'Father' of the advertising placard; more than 1,000 posters.",PO,["Belle Époque poster"]),
 a("Alphonse Mucha","Czech Republic","Art Nouveau posters","Art Nouveau designer of stylised women; Gismonda poster for Sarah Bernhardt.",PO,["Belle Époque poster"]),
 a("Henri de Toulouse-Lautrec","France","posters","French painter-printmaker of Montmartre posters.",MR,["Belle Époque poster"]),
 a("Cassandre","France","travel posters","Poster artist and type designer (1901–1968), born Adolphe Jean-Marie Mouron.",CA,["Art Deco travel poster"]),
 a("Edward McKnight Kauffer","United States","Underground posters","American-born designer (1890–1954) of 140 London Underground posters.",KA,["London Underground poster"]),
 a("WPA Federal Art Project","United States","public posters","New Deal art programme (1935–1943) with a poster division.",FAP,["WPA poster"],"Institution & issuer","1935"),
 a("Josef Müller-Brockmann","Switzerland","Swiss Style","Swiss designer (1914–1996) of the Tonhalle concert posters.",MB,["Swiss International Style poster"]),
 a("Mourlot Studios","France","lithography","Paris printing house known for lithographs and exhibition posters.",MS,["Mourlot exhibition poster"],"Heritage manufactory","1852"),
 a("King & McGaw","United Kingdom","art prints","Newhaven art-print publisher and framer supplying museum shops.",KM,["Museum-shop exhibition poster"],"Specialist","1982"),
 a("Nash Editions","United States","giclée","Print studio where the giclée name was coined.",GC,["Iris giclée"],"Specialist"),
 a("Desenio","Sweden","posters","Online seller of affordable wall art; bought Poster Store in 2020.",DE,[],"Value"),
 a("Society6","United States","print on demand","Los Angeles print-on-demand marketplace for artists, founded 2009.",S6,[],"Mainstream","2009"),
 {"n":"IKEA","c":"Sweden","f":"1943","seg":"Value","kf":"flat-pack furniture","d":"Swedish home-furnishing retailer; sells BILD posters and frames.","s":"knowledge","sig":[]},
]
notes="Inkjet print renamed Giclée and fine-art reproduction (marked as reproduction). Canvas and framed art print is a tier kind with four market-covering sellers; no test-winner data found. Film posters kept as an object archetype with formats only, no titles. Mucha country given as Czech Republic (modern state)."
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/02_05.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
