import json, os
W='https://en.wikipedia.org/wiki/'
SH=W+'Southworth_%26_Hawes'; AU=W+'Autochrome_Lumi%C3%A8re'; CW=W+'Camera_Work'; PN=W+'The_Pencil_of_Nature'
UC='https://dictionary.archivists.org/entry/union-case.html'; GA='https://www.getty.edu/art/collections/glossary/g319.html'
BR='https://www.battlefields.org/learn/biographies/mathew-brady'; PG=W+'Photogravure'; SP=W+'Salt_print'
TT=W+'Tintype'; AM=W+'Ambrotype'; MET='https://www.metmuseum.org/essays/photography-and-the-civil-war-1861-1865'
CA='https://cartermuseum.org/press-release/carter-museum-acquires-rare-20-volume-photography-book-and-portfolio-set'
def V(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Daguerreotype","a":"cased image","d":"A unique, mirror-like photographic image on a silvered copper plate, the first public photographic process (1839).",
  "t":["whole plate (8½ × 6½ in)","half plate","quarter plate","sixth plate","ninth plate","leather or wood folding case","Union case (moulded thermoplastic, 1854)","hand-tinted","stereo daguerreotype"],
  "s":"https://www.sothebys.com/en/articles/the-complete-collectors-guide-to-photographic-prints",
  "x":[
   {"n":"Southworth & Hawes whole-plate portrait","a":"","d":"A large-format daguerreotype portrait from the Boston studio that raised the process to fine art.","mk":"Southworth & Hawes","y":"1843–1863","s":SH,
    "v":[V("Longfellow family portrait","Southworth & Hawes","1849"),V("William Hickling Prescott","Southworth & Hawes","c. 1850"),
         V("Ralph Waldo Emerson","Southworth & Hawes","1857"),V("Ether operation, Massachusetts General Hospital","Southworth & Hawes","1847","early surgery series")],
    "dt":"plate size (whole plate 8½ × 6½ in) · sitter · case · plate condition and tarnish"},
   {"n":"Brady studio daguerreotype portrait","a":"","d":"A daguerreotype portrait of a public figure from Mathew Brady's Daguerrean Miniature Gallery on Broadway, opened 1844.","mk":"Mathew Brady","y":"1844–1850s","s":BR,
    "v":[V("Henry Clay","Mathew Brady",""),V("Daniel Webster","Mathew Brady",""),V("John C. Calhoun","Mathew Brady",""),V("Edgar Allan Poe","Mathew Brady","")],
    "dt":"sitter · plate size · studio stamp or case label · condition"}]},
 {"n":"Ambrotype","a":"collodion positive","d":"A collodion positive image on a glass plate, backed with a dark ground so the negative reads as a positive.",
  "t":["black varnish backing","ruby (dark red) glass","black velvet backing","hand-tinted","oval plate","folding case","Union case","balsam-sealed"],
  "s":"https://www.1stdibs.com/buy/antique-ambrotype",
  "x":[
   {"n":"Cutting patent ambrotype","a":"","d":"The cased glass positive patented in Boston and spread across the United States, overtaking the daguerreotype in the late 1850s.","mk":"James Ambrose Cutting","y":"1854–1860s","s":AM,
    "v":[V("Patent ambrotype, introduced with Isaac Rehn","James Ambrose Cutting","1854"),
         V("NYPD 'rogues' gallery' portraits","","1858","police use"),V("Charlotte Cushman portrait","","1859")],
    "dt":"backing method · case · tinting · sitter · condition of varnish"}]},
 {"n":"Tintype","a":"ferrotype · melainotype · melanotype","d":"A collodion positive image on a thin, black-lacquered iron plate; cheap, robust and popular from the 1850s to about 1910.",
  "t":["gem (¾ × 1 in)","Bon-ton size","up to 11 × 14 in","paper mat or sleeve","cased","album card","hand-tinted"],
  "s":"https://www.1stdibs.com/buy/antique-ambrotype",
  "x":[
   {"n":"Smith patent ferrotype","a":"melainotype","d":"The iron-plate collodion positive patented in the United States in 1856.","mk":"Hamilton L. Smith","y":"1856","s":TT,
    "v":[V("Martin process, Paris","","1853","introduced by Adolphe Alexandre Martin"),V("Ferrotype plates","V. M. Griswold","","rival plate maker who coined 'ferrotype'")],
    "dt":"plate size · maker's stamp · case or sleeve"},
   {"n":"Pocket portrait tintype","a":"Civil War tintype","d":"A small tintype portrait carried in a pocket, made in huge numbers for soldiers and on the American frontier.","mk":"","y":"1860s–1880s","s":TT,
    "v":[V("Civil War soldier portrait","","1861–1865"),V("Billy the Kid, Fort Sumner","","c. 1879–1880","his only surviving portrait")],
    "dt":"sitter and uniform · plate size · tinting · mat"},
   {"n":"Gem tintype","a":"gem portrait","d":"A tiny tintype portrait, a dozen made with one exposure of a twelve-lens camera.","mk":"","y":"from 1858","s":TT,
    "dt":"¾ × 1 in · album, locket or card mount"},
   {"n":"Contemporary tintype","a":"","d":"A modern tintype made in the revival of wet-plate collodion.","mk":"","y":"2010s","s":TT,
    "v":[V("Sundance portraits","Victoria Will","2014–2015"),V("Air Force pilots, Afghanistan","Ed Drew","2013")],
    "dt":"plate size · artist · varnish"}]},
 {"n":"Salted paper print","a":"salt print","d":"The first paper photographic print, with the image in the paper fibres, usually printed from a calotype paper negative (c. 1839–1860).",
  "t":["from calotype negative","from glass negative","gold-toned","untoned","mounted","in album or book"],
  "s":SP,
  "x":[
   {"n":"Talbot calotype print – The Pencil of Nature","a":"","d":"The first commercially published book illustrated with photographs, issued in six parts with 24 pasted-in prints.","mk":"Henry Fox Talbot","y":"1844–1846","s":PN,
    "v":[V("Plate VI, The Open Door","Henry Fox Talbot","1844"),V("Plate X, The Haystack","Henry Fox Talbot",""),V("Plate XIV, The Ladder","Henry Fox Talbot",""),
         V("Facsimile edition","Hans P. Kraus Jr.","1989"),V("Facsimile edition","Da Capo Press","1969")],
    "dt":"part (fascicle) · plate number · fading · original or facsimile"},
   {"n":"Hill & Adamson calotype","a":"","d":"A salt print from a calotype negative by the Edinburgh partnership of painter and photographer.","mk":"Hill & Adamson","y":"1840s","s":SP,
    "v":[V("Edinburgh Ale","Hill & Adamson","c. 1844")],
    "dt":"subject · print date (period or later) · toning"},
   {"n":"Nadar salt-print portrait","a":"","d":"A salted paper portrait from Nadar's Paris studio.","mk":"Nadar","y":"1850s","s":SP,
    "v":[V("Jean-François Millet","Nadar","")],
    "dt":"sitter · mount and studio stamp · fading"}]},
 {"n":"Albumen print","a":"albumen silver print","d":"A paper print with the image in an egg-white binder, the dominant photographic print from the 1850s to about 1890.",
  "t":["gold-toned","mounted on card","loose or in album","hand-coloured","book illustration (tipped-in)","travel view","stereoview, carte de visite and cabinet card (see F5)"],
  "s":GA,
  "x":[
   {"n":"Gardner's Photographic Sketch Book of the War","a":"","d":"Two volumes of 100 albumen prints of the American Civil War, crediting each of eleven photographers.","mk":"Alexander Gardner","y":"1865–1866","s":MET,
    "v":[V("Plates by Timothy O'Sullivan","Alexander Gardner","1865–1866","former Brady apprentice")],
    "dt":"volume · plate · photographer credit · fading and foxing of mount"},
   {"n":"Brady studio war view","a":"","d":"A Civil War view by the photographers Brady organised and paid to follow the troops.","mk":"Mathew Brady","y":"1861–1865","s":BR,
    "v":[V("The Dead of Antietam","Mathew Brady","1862","exhibited in Brady's New York studio; taken by Gardner and James F. Gibson")],
    "dt":"battle or site · credit line (often misattributed) · mount"}]},
 {"n":"Photogravure","a":"héliogravure · gravure","d":"A photomechanical intaglio print from an etched copper plate, giving continuous tone in ink; prized in fine photographic books and portfolios.",
  "t":["tipped-in book plate","large portfolio plate","hand-pulled","Japan tissue","later restrike","rotogravure (machine-printed, not true gravure)"],
  "s":PG,
  "x":[
   {"n":"Camera Work gravure","a":"","d":"A photogravure tipped by hand into Alfred Stieglitz's quarterly, the showcase of Photo-Secession photography.","mk":"Alfred Stieglitz","y":"1903–1917","s":CW,
    "v":[V("Issues 1–48","Alfred Stieglitz","1903–1916","1,000 copies each"),V("Final issue Nos. 49–50 (Paul Strand)","Alfred Stieglitz","1917","500 copies"),
         V("Complete set of 50 issues","Alfred Stieglitz","","sold at Sotheby's 2011 for $398,500")],
    "dt":"issue · photographer (Steichen, Stieglitz, Coburn, Käsebier, White, Hill & Adamson…) · loose or in issue · condition"},
   {"n":"Curtis – The North American Indian","a":"","d":"Edward S. Curtis's 20-volume study of Native American peoples, with small gravures in the books and large ones in the portfolios.","mk":"Edward S. Curtis","y":"1907–1930","s":CA,
    "v":[V("Text-volume gravure","Edward S. Curtis","1907–1930","over 1,500 across 20 volumes"),V("Portfolio gravure","Edward S. Curtis","1907–1930","about 36 per portfolio, 722 in all"),
         V("Complete subscriber set","Edward S. Curtis","","500 planned, 222 completed")],
    "dt":"volume and plate number · book or portfolio size · paper · original or later restrike"},
   {"n":"Strand – The Mexican Portfolio","a":"Photographs of Mexico","d":"Paul Strand's portfolio of twenty hand-pulled photogravures of Mexico.","mk":"Paul Strand","y":"1940","s":PG,
    "v":[V("Photographs of Mexico","Paul Strand","1940"),V("The Mexican Portfolio","Paul Strand","1967","edition of 1,000")],
    "dt":"edition · completeness · plate"}]},
 {"n":"Autochrome","a":"autochrome plate","d":"An early colour photograph on glass, made through a mosaic of dyed potato-starch grains (marketed 1907).",
  "t":["glass plate","stereo autochrome","diascope viewer","lantern slide","Filmcolor or Lumicolor film"],
  "s":AU,
  "x":[
   {"n":"Lumière Autochrome plate","a":"","d":"The Lumière brothers' additive screen-plate colour process, the main colour process until the mid-1930s.","mk":"Lumière","y":"1907","s":AU,
    "v":[V("Autochrome glass plate","Lumière","1907","patented 1903"),V("Filmcolor sheet film","Lumière","1931"),V("Lumicolor roll film","Lumière","1933"),V("Alticolor","Lumière","1952–1955","last version")],
    "dt":"plate size · stereo or single · photographer (Genthe, Kahn's Archives, Bufka…) · cracks and fading"}]}]
P="Artisan & independent"
def B(n,c,f,seg,kf,d,s,sig): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 B("Southworth & Hawes","United States","1843",P,"daguerreotypes","Boston studio of Albert Sands Southworth and Josiah Johnson Hawes, 1843–1863.",SH,["Southworth & Hawes whole-plate portrait"]),
 B("Mathew Brady","United States","1844",P,"portraits, Civil War","New York and Washington portrait studio that organised photographers to cover the Civil War.",BR,["Brady studio daguerreotype portrait","Brady studio war view"]),
 B("James Ambrose Cutting","United States","",P,"ambrotype patent","Boston photographer who patented the ambrotype process in 1854.",AM,["Cutting patent ambrotype"]),
 B("Hamilton L. Smith","United States","",P,"tintype patent","American scientist who patented the tintype (ferrotype) in 1856.",TT,["Smith patent ferrotype"]),
 B("V. M. Griswold","United States","","Specialist","ferrotype plates","Ohio maker of iron plates who coined the name ferrotype.",TT,[]),
 B("Victoria Will","United States","",P,"modern tintypes","Photographer of tintype portraits at Sundance in 2014–2015.",TT,[]),
 B("Ed Drew","United States","",P,"modern tintypes","Photographer of tintypes of Air Force pilots in Afghanistan (2013).",TT,[]),
 B("Henry Fox Talbot","United Kingdom","",P,"calotype, salt prints","English inventor of the salted paper print and calotype, author of The Pencil of Nature.",SP,["Talbot calotype print – The Pencil of Nature"]),
 B("Hans P. Kraus Jr.","United States","","Specialist","photo books, facsimiles","Publisher of a 1989 facsimile of The Pencil of Nature.",PN,[]),
 B("Da Capo Press","United States","","Specialist","facsimiles","Publisher of a 1969 facsimile of The Pencil of Nature.",PN,[]),
 B("Hill & Adamson","United Kingdom","",P,"calotypes","Edinburgh partnership of David Octavius Hill and Robert Adamson, known for calotype portraits.",SP,["Hill & Adamson calotype"]),
 B("Nadar","France","",P,"portraits","Paris portrait photographer.",SP,["Nadar salt-print portrait"]),
 B("Alexander Gardner","United States","",P,"Civil War views","Civil War photographer and publisher of Gardner's Photographic Sketch Book of the War.",MET,["Gardner's Photographic Sketch Book of the War"]),
 B("Alfred Stieglitz","United States","",P,"Camera Work, pictorialism","American photographer and editor of Camera Work (1903–1917).",CW,["Camera Work gravure"]),
 B("Edward S. Curtis","United States","",P,"The North American Indian","American photographer of The North American Indian (1907–1930).",CA,["Curtis – The North American Indian"]),
 B("Paul Strand","United States","",P,"modernist photographs","American photographer; subject of the last Camera Work and maker of The Mexican Portfolio.",PG,["Strand – The Mexican Portfolio"]),
 B("Lumière","France","","Specialist","Autochrome plates","Company of Louis and Auguste Lumière that made Autochrome plates from 1907.",AU,["Lumière Autochrome plate"]),
]
out={"kinds":kinds,"brands":brands,"traditions":[],
 "notes":"Three old kinds kept with old sources; four new kinds sourced. Case types and plate sizes as 't'. Cartes de visite, cabinet cards and stereoviews left in F5 (cross-link noted in Albumen print types). Francis Frith's Egypt and Palestine (1858–59) albumen travel views left out: every catalogue page found (Toledo, Eastman, Ackland, HathiTrust) returned 403. Brady's Gallery of Illustrious Americans omitted (lithographs, not photographs). Albert Kahn's Archives of the Planet not an archetype (institutional collection). LOC daguerreotype size page 403: plate-size types rest on the Southworth & Hawes page (whole plate) and standard nomenclature."}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/03_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
