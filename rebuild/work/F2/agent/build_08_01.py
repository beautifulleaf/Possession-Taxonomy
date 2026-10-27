import json,os
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def T(n,g,r,p,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":g,"r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
PC=W+"Papercutting"; MM=W+"Micromosaic"
kinds=[
 {"n":"Collage","a":"papier collé · photomontage","d":"A picture built from pasted or bonded elements (paper, cloth, photographs, found flat material).",
  "t":["papier collé (paper only)","cut-paper","photomontage","mixed-material collage","Merz collage"],
  "s":"https://www.singulart.com/en/painting",
  "x":[
   {"n":"Cubist papier collé","a":"Braque and Picasso collage","d":"Pasted-paper works begun in 1912 by Georges Braque and Pablo Picasso; the term applies to paper only.","mk":"","y":"1912","s":W+"Papier_coll%C3%A9",
    "v":[V("Fruit Dish and Glass","Georges Braque","1912","papier collé and charcoal; imitation wood-grain paper")],
    "dt":"paper types · charcoal · museum-held vs market"},
   {"n":"Matisse cut-out","a":"drawing with scissors","d":"Henri Matisse's coloured-paper cut-outs, his main medium after 1941, reproduced by pochoir in Jazz.","mk":"","y":"1941–1954","s":W+"Jazz_(Henri_Matisse)",
    "v":[V("Jazz (20 pochoir prints, Tériade)","Henri Matisse","1947","limited-edition artist's book"),V("Blue Nude II","Henri Matisse","","cited on the Collage page")],
    "dt":"gouache-painted paper · pochoir print vs original cut-out"},
   {"n":"Schwitters Merz collage","a":"Merz","d":"Kurt Schwitters's collages and assemblages of found refuse, named from a fragment of 'Kommerz'.","mk":"","y":"1920s","s":W+"Merz_(art_style)",
    "v":[V("Merzbau","Kurt Schwitters","1927–1943","tower-sized assemblage destroyed in a 1943 air raid")],
    "dt":"found fragments · small-scale collages · provenance"}]},
 {"n":"Mosaic picture","a":"micromosaic · mosaic panel","d":"A picture set in small pieces (tesserae) of stone, glass or ceramic.",
  "t":["Roman tessellated panel","Byzantine icon","micromosaic","modern mosaic panel","fragment"],
  "s":"https://www.1stdibs.com/furniture/wall-decorations/contemporary-art/stylish-artistic-mosaic-handmade-customizable/id-f_21118402",
  "x":[
   {"n":"Roman mosaic fragment","a":"opus tessellatum","d":"Pieces from Roman floor and wall mosaics, made from the Republic through the Empire.","mk":"","y":"3rd century BC onward","s":W+"Roman_mosaic",
    "v":[V("Earliest floor mosaics at Delos","","2nd century BC"),V("Floor mosaics of Tunisia","",""),V("Gold-ground wall mosaics","","late antiquity")],
    "dt":"tesserae material · subject · find site · export law"},
   {"n":"Micromosaic","a":"Vatican micromosaic · Grand Tour souvenir","d":"Pictures of very small glass tesserae, produced in Italy from the Renaissance and bought on the Grand Tour.","mk":"","y":"1576 onward","s":MM,
    "v":[V("Surviving Byzantine micromosaic icons","","c. 1300–1453","Constantinople"),V("Vatican Mosaic Studio founded","Vatican Mosaic Studio","1576","copies of St Peter's altarpieces"),V("Archaeological-style subjects","Fortunato Pio Castellani","19th century","1794–1865")],
    "dt":"tesserae per square inch (best work 3,000–5,000) · setting (jewellery, box) · signed"}]},
 {"n":"Paper cut","a":"jianzhi · Scherenschnitte · kirie · wycinanki · papel picado","d":"A picture made by cutting one or more sheets of paper so the image is formed by the cuts, mounted for display.",
  "t":["jianzhi","Scherenschnitte","kirie","wycinanki","papel picado","framed","banner"],
  "s":"https://www.artsy.net/categories",
  "x":[
   {"n":"Jianzhi","a":"Chinese paper cutting","d":"Chinese folk paper cutting, usually red, for windows, doors and festivals; UNESCO-listed in 2009.","mk":"","y":"earliest examples c. 4th–6th century","s":W+"Chinese_paper_cutting",
    "v":[V("Southern school","","","Foshan, Putian"),V("Jiangzhe school","","","Yangzhou, Yueqing"),V("Northern school","","","Hebei, Shaanxi")],
    "dt":"motif (福, carp, zodiac, peony) · region · red paper"},
   {"n":"Scherenschnitte","a":"scissor cuts","d":"European paper cutting from Switzerland and Germany, carried to Pennsylvania in the 18th century.","mk":"","y":"16th century onward","s":W+"Scherenschnitte",
    "v":[V("Pennsylvania Dutch Scherenschnitte","","18th century")],
    "dt":"symmetry · silhouette · valentine"},
   {"n":"Kirie","a":"Japanese paper picture","d":"Japanese paper-picture cutting, tied to papermaking reaching Japan around 610.","mk":"","y":"from c. 610","s":PC,
    "v":[V("Sekishu washi cutting paper","","c. 800")],
    "dt":"paper type · artist"},
   {"n":"Wycinanki","a":"Polish paper cutting","d":"Polish layered, bright paper cuts of roosters, flowers and holiday motifs; kin to Ukrainian vytynanky and Belarusian vycinanki.","mk":"","y":"","s":PC,
    "v":[V("Belarusian version UNESCO-recognised","","2024")],
    "dt":"layers · colour · motif"},
   {"n":"Papel picado","a":"perforated paper","d":"Mexican tissue-paper banners cut with chisels from stacks, prominent at Day of the Dead.","mk":"","y":"19th century tissue paper","s":W+"Papel_picado",
    "v":[V("San Salvador Huixcolotla, Puebla, birthplace","","")],
    "dt":"stack cutting · size · skull motif"}]},
 {"n":"Silhouette portrait","a":"cut silhouette · profile portrait","d":"A profile portrait cut from black paper or painted in solid outline, popular from the mid-18th century.",
  "t":["cut paper","painted on ivory","painted on glass","hollow-cut","cut and paste","full-length","bust"],
  "s":W+"Silhouette",
  "x":[
   {"n":"Auguste Edouart silhouette","a":"Edouart full-length silhouette","d":"Full-length profile likenesses cut from black paper by Auguste Edouart (1789–1861), who worked in Britain and the United States.","mk":"","y":"1825–1849","s":W+"Auguste_Edouart",
    "v":[V("Edinburgh period, about 5,000 likenesses","Auguste Edouart","1829–1832"),V("American tour","Auguste Edouart","c. 1839–1849")],
    "dt":"sitter · full length · cutting in duplicate · collections: NPG London, National Galleries of Scotland, MFA Boston"},
   {"n":"John Miers silhouette","a":"three-minute sittings","d":"Painted silhouette likenesses by John Miers, who advertised 'three minute sittings'.","mk":"","y":"c. 1790 onward","s":W+"Silhouette",
    "v":[V("Painted outline portrait","John Miers")],
    "dt":"outline painted on plaster, glass or ivory · frame"}]}
]
trad=[
 T("Jianzhi","Paper cutting","China","c. 4th–6th century onward","Chinese folk paper cutting with Southern, Jiangzhe and Northern schools; UNESCO 2009.","scissor or knife cutting","red paper",["Jianzhi"],["Foshan","Yangzhou","Hebei","Shaanxi"],"Region style; hand vs laser cut",W+"Chinese_paper_cutting"),
 T("Scherenschnitte","Paper cutting","Switzerland, Germany, Pennsylvania","16th century onward","German-speaking scissor-cut tradition, carried to Colonial America in the 18th century.","scissors","paper",["Scherenschnitte"],[],"Provenance",W+"Scherenschnitte"),
 T("Kirie","Paper cutting","Japan","papermaking from c. 610","Japanese paper-picture cutting.","cutting","washi",["Kirie"],[],"Artist",PC),
 T("Wycinanki","Paper cutting","Poland, Ukraine, Belarus","","Layered bright folk paper cuts.","scissors","coloured paper",["Wycinanki"],[],"Region and colour style",PC),
 T("Papel picado","Paper cutting","Mexico","19th century tissue paper","Tissue-paper banners cut with chisels, for Day of the Dead and festivals.","chisel cutting of stacks","tissue paper",["Papel picado"],["San Salvador Huixcolotla, Puebla"],"Hand-cut vs machine-cut",W+"Papel_picado"),
 T("Vatican micromosaic","Mosaic","Rome, Italy","1576 onward","Tiny-tessera glass mosaics from the Vatican Mosaic Studio, sold on the Grand Tour.","glass tesserae","glass, smalti",["Micromosaic"],["Vatican Mosaic Studio"],"Tesserae count; studio and maker signature",MM)]
notes="Kept old Collage, Mosaic picture and Paper cut with their old sources. Left out for lack of retrieved support: Byzantine large mosaics (only micromosaic icons), Picasso-specific works (Braque's Fruit Dish and Glass is the sourced example). Matisse and Schwitters under Collage. Silhouette is a new kind; John Miers from the Silhouette page. Artists belong to the artist register."
json.dump({"kinds":kinds,"brands":[],"traditions":trad,"notes":notes},open('work/F2/shelves/08_01.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F2/shelves/08_01.tmp','work/F2/shelves/08_01.json')
