import json, os
W='https://en.wikipedia.org/wiki/'
PT=W+'Papunya_Tula'; BK=W+'Bark_painting'; MB=W+'Madhubani_art'; WR=W+'Warli_painting'; KG=W+'Kalighat_painting'
JS=W+'Jangarh_Singh_Shyam'; TT=W+'Tingatinga_(painting)'; HH=W+'Hector_Hyppolite'; NA=W+'Na%C3%AFve_art'
OA=W+'Outsider_art'; VP=W+'Votive_paintings_of_Mexico'; HD=W+'Henry_Darger'; AW=W+'Adolf_W%C3%B6lfli'
HR=W+'Henri_Rousseau'; IAC='https://www.indigenousartcode.org/news-article/purchasing-art-ethically'
PC=W+'Pattachitra'; WL=W+'Warlugulong'; CI=W+'Contemporary_Indigenous_Australian_art'; HA=W+'Haitian_art'
def v(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def b(n,c,kf,d,s,sig): return {"n":n,"c":c,"f":"","seg":"Artisan & independent","kf":kf,"d":d,"s":s,"sig":sig}
kinds=[
 {"n":"Aboriginal Australian painting","a":"Aboriginal art · Indigenous Australian painting · dot painting · bark painting",
  "d":"A painting by an Aboriginal Australian artist, usually telling a Dreaming story, in acrylic on canvas or ochre on bark.",
  "t":["acrylic on canvas","acrylic on board","ochre on bark","watercolour","art-centre certificate","unstretched canvas"],
  "s":CI,
  "x":[
   {"n":"Western Desert dot painting","a":"Papunya painting · Western Desert Art Movement","d":"Acrylic painting of ancestral stories in fields of dots and roundels, begun at Papunya in 1971.","mk":"Papunya Tula","y":"1971 onward","s":PT,
    "v":[v("Early Papunya boards","Papunya Tula","1971–73","Bardon years; masonite, car bonnets and other hard surfaces"),
         v("Gulgardi","Kaapa Tjampitjinpa","","won a regional award"),
         v("Warlugulong","Clifford Possum Tjapaltjarri","1977","acrylic on canvas, 202 × 337.5 cm; NGA bought it for A$2.4m in 2007"),
         v("Earth's Creation","Emily Kame Kngwarreye","","Utopia; sold for $1.056m in 2007")],
    "dt":"early board vs canvas · size · art-centre catalogue number and certificate · provenance"},
   {"n":"Arnhem Land bark painting","a":"Yolŋu bark painting","d":"Earth ochres on the flattened inner bark of stringybark, with rarrk cross-hatching identifying clan designs.","mk":"","y":"modern form from 1912","s":BK,
    "v":[v("Commissioned barks at Gunbalanya (Oenpelli)","Baldwin Spencer","1912","start of the modern form"),
         v("Yirrkala bark petitions","Yolŋu artists","1963"),
         v("Buku-Larrnggay Mulka Centre barks","Buku-Larrnggay Mulka Centre","","Yirrkala"),
         v("Injalak Arts barks","Injalak Arts","","Gunbalanya; includes x-ray style")],
    "dt":"stringybark · ochre and pipeclay · rarrk · splinted ends · art-centre provenance"},
   {"n":"Hermannsburg watercolour","a":"Arrernte watercolour","d":"Western-style watercolour landscapes of Central Australia begun by Albert Namatjira.","mk":"Albert Namatjira","y":"1930s onward","s":CI,
    "v":[v("First exhibition","Albert Namatjira","1938")],"dt":"watercolour on paper · size · signature"}
  ]},
 {"n":"Indian folk painting","a":"Indian tribal painting · folk and tribal art of India",
  "d":"A painting in one of India's regional folk or tribal traditions, made on walls, cloth or paper with natural or bright colours.",
  "t":["on paper","on cloth","on canvas","on palm leaf","natural pigments","acrylic"],"s":MB,
  "x":[
   {"n":"Madhubani painting","a":"Mithila painting","d":"Painting by women of the Mithila region of Bihar, with black outlines, flat colour and densely filled space.","mk":"","y":"traditional; on paper from the 1960s","s":MB,
    "v":[v("Bharni","","","style"),v("Kachni","","","line style"),v("Tantrik","","","style"),v("Godna","","","style"),v("Kohbar","","","wedding-chamber style"),
         v("Works","Sita Devi","","Padma Shri 1981"),v("Works","Ganga Devi","","Padma Shri 1984"),v("Works","Baua Devi","")],
    "dt":"paper or canvas · natural pigment vs synthetic · size · GI-registered origin"},
   {"n":"Pattachitra","a":"patachitra · patta painting · Bengal patachitra scroll","d":"Painting on gum-and-chalk-coated cloth from Odisha and Bengal, often of Jagannath or epic scenes.","mk":"","y":"traditional","s":PC,
    "v":[v("Odisha pattachitra","","","Raghurajpur near Puri; GI 2008"),v("Tala pattachitra","","","incised palm-leaf panels"),v("Bengal patachitra scroll","","","sung narrative scroll by Patuas; GI 2018")],
    "dt":"cloth or palm leaf · single panel vs scroll · pigments"},
   {"n":"Gond painting","a":"Jangarh Kalam · Pardhan Gond painting","d":"Bright figures of animals and deities filled with dots and lines, moved from house walls to paper and canvas.","mk":"Jangarh Singh Shyam","y":"from 1981","s":JS,
    "v":[v("Works on paper and canvas","Jangarh Singh Shyam","1981–2001","Bharat Bhavan, Bhopal")],"dt":"paper or canvas · acrylic or ink · size"},
   {"n":"Warli painting","a":"","d":"White rice-paste stick figures in circles and triangles on a red-ochre or mud ground, from Maharashtra.","mk":"Jivya Soma Mashe","y":"on paper and canvas from the 1970s","s":WR,
    "v":[v("Works","Jivya Soma Mashe","1970s onward"),v("Works","Balu Mashe","1970s onward")],"dt":"paper, cloth or canvas · white on ochre · size"},
   {"n":"Kalighat painting","a":"Kalighat pat","d":"Bold-outlined watercolours on paper sold near Kolkata's Kalighat temple, of gods and satirical town scenes.","mk":"","y":"c. 1800–1930","s":KG,
    "v":[v("Mythological subjects","","","Kali, Durga, Krishna"),v("Babu and bibi satires","","")],"dt":"paper · watercolour, tin highlights · antique vs revival"}
  ]},
 {"n":"Tingatinga painting","a":"Tinga Tinga",
  "d":"A Tanzanian naïve painting in glossy enamel paint on board, of animals and village or city scenes filling the whole surface.",
  "t":["enamel on masonite","enamel on canvas","small tourist format","large panel"],"s":TT,
  "x":[{"n":"Tingatinga school painting","a":"","d":"Bicycle-enamel animals and flowers in repeated designs, begun by Edward Tingatinga in Dar es Salaam.","mk":"Edward Tingatinga","y":"1968 onward","s":TT,
    "v":[v("Original works","Edward Tingatinga","1968–1972"),v("Tingatinga Arts Cooperative Society","Tingatinga Arts Cooperative Society","1990","Oyster Bay, Dar es Salaam"),
         v("Second generation","January Linda",""),v("Second generation","Simon Mpata",""),v("Second generation","Adeusi Mandu","")],
    "dt":"masonite or canvas · size · signature · city scenes from the 1990s"}]},
 {"n":"Naive painting","a":"naïve art · primitive painting · self-taught painting",
  "d":"A painting by a self-taught artist with flat, bright colour, careful detail and little conventional perspective.",
  "t":["oil on canvas","oil on board","acrylic","glass painting"],"s":NA,
  "x":[
   {"n":"Rousseau-style jungle and dream painting","a":"Le Douanier","d":"The reference naïve painting: dense jungles and dreamlike scenes by Henri Rousseau.","mk":"Henri Rousseau","y":"1891–1910","s":HR,
    "v":[v("Tiger in a Tropical Storm (Surprised!)","Henri Rousseau","1891"),v("The Sleeping Gypsy","Henri Rousseau","1897"),v("The Snake Charmer","Henri Rousseau","1907"),v("The Dream","Henri Rousseau","1910")],
    "dt":"oil on canvas · size"},
   {"n":"Sacred Heart painters","a":"Painters of the Sacred Heart","d":"French self-taught painters shown together by Wilhelm Uhde in 1928.","mk":"","y":"1928","s":NA,
    "v":[v("Works","André Bauchant",""),v("Works","Camille Bombois",""),v("Works","Séraphine Louis",""),v("Works","Louis Vivin","")],"dt":"oil on canvas"},
   {"n":"Haitian painting","a":"Haitian naïve painting · Centre d'Art school","d":"Bright, often Vodou-inspired painting from the Port-au-Prince Centre d'Art and later schools.","mk":"Hector Hyppolite","y":"1944 onward","s":HA,
    "v":[v("Maitresse Erzulie","Hector Hyppolite","c. 1945–48"),v("Damballah La Flambeau","Hector Hyppolite","c. 1945–48"),
         v("Centre d'Art painters","Rigaud Benoit",""),v("Centre d'Art painters","Wilson Bigaud",""),v("Centre d'Art painters","Castera Bazile",""),
         v("Saint Soleil","Louisiane Saint Fleurant","1973 onward","Soisson-la-Montagne group")],
    "dt":"oil or enamel on board or canvas · Cap-Haïtien and Jacmel schools"},
   {"n":"Hlebine painting","a":"Hlebine school · Croatian naïve","d":"Croatian peasant painting from the village of Hlebine, founded as a school in 1930.","mk":"Ivan Generalić","y":"1930 onward","s":NA,
    "v":[v("Works","Ivan Generalić","","first master"),v("Works","Ivan Lacković-Croata",""),v("Works","Mijo Kovačić",""),v("Works","Ivan Večenaj","")],"dt":"oil on canvas or glass · size"}
  ]},
 {"n":"Outsider art","a":"art brut · raw art · self-taught art · visionary art",
  "d":"Art by self-taught makers outside the art world, often psychiatric patients or recluses, in any medium.",
  "t":["drawing","painting","collage","mixed media","sculpture"],"s":OA,
  "x":[
   {"n":"Art brut","a":"raw art","d":"The work Jean Dubuffet collected from the 1940s, now the Collection de l'Art Brut in Lausanne.","mk":"Jean Dubuffet","y":"1940s onward","s":OA,
    "v":[v("Compagnie de l'Art Brut","Jean Dubuffet","1948"),v("Bildnerei der Geisteskranken","Hans Prinzhorn","1922","founding study"),v("Outsider Art","Roger Cardinal","1972","coined the English term")],
    "dt":"medium · documented provenance"},
   {"n":"Wölfli illustrated epic","a":"","d":"Dense pencil and coloured-pencil pages from Adolf Wölfli's 45-volume epic, drawn at the Waldau clinic.","mk":"Adolf Wölfli","y":"1904–1930","s":AW,
    "v":[v("Irren-Anstalt Band-Hain","Adolf Wölfli","1910"),v("45-volume epic","Adolf Wölfli","1908 onward")],"dt":"pencil and coloured pencil · newsprint · single sheet vs volume"},
   {"n":"Darger Vivian Girls painting","a":"","d":"Watercolour, collage and traced panoramas illustrating Henry Darger's In the Realms of the Unreal.","mk":"Henry Darger","y":"c. 1910–1960s","s":HD,
    "v":[v("Collages","Henry Darger","c. 1912–25"),v("Watercolour panoramas","Henry Darger","","up to 10–12 ft long")],"dt":"watercolour, graphite, collage · double-sided · length"}
  ]},
 {"n":"Retablo and ex-voto painting","a":"ex-voto · retablo · lámina · votive painting",
  "d":"A small Mexican devotional painting, usually oil on tin: a saint image (retablo) or a thanks-offering scene with written testimony (ex-voto).",
  "t":["oil on tin","oil on canvas","on paper","saint image","narrative ex-voto"],"s":VP,
  "x":[
   {"n":"Narrative ex-voto","a":"exvoto · milagro painting","d":"A scene of rescue or cure with a holy figure above and a dated written testimony below.","mk":"","y":"late 18th century onward","s":VP,
    "v":[v("Works","Hermenegildo Bustos","19th century"),v("Works","Vicente Barajas",""),v("Contemporary ex-votos","Alfredo Vilchis","","Mexico City")],
    "dt":"tin sheet · inscription and date · size · condition of paint"},
   {"n":"Saint retablo","a":"lámina","d":"A static devotional image of a saint or Virgin for a home shrine, painted on tin.","mk":"","y":"18th – 19th century","s":VP,
    "v":[],"dt":"tin · saint depicted · workshop"}
  ]}
]
brands=[
 {"n":"Papunya Tula","c":"Australia","f":"1972","seg":"Artisan & independent","kf":"dot painting","d":"Aboriginal-owned artist cooperative from Papunya, now in Alice Springs.","s":PT,"sig":["Western Desert dot painting"]},
 b("Kaapa Tjampitjinpa","Australia","dot painting","Papunya painter; Gulgardi won a regional award.",CI,["Western Desert dot painting"]),
 b("Clifford Possum Tjapaltjarri","Australia","dot painting","Leading Papunya Tula painter, author of Warlugulong (1977).",WL,["Western Desert dot painting"]),
 b("Emily Kame Kngwarreye","Australia","Utopia painting","Utopia painter of the late 1980s–1990s.",CI,["Western Desert dot painting"]),
 b("Albert Namatjira","Australia","watercolour","Arrernte watercolourist first exhibited 1938.",CI,["Hermannsburg watercolour"]),
 {"n":"Buku-Larrnggay Mulka Centre","c":"Australia","f":"","seg":"Artisan & independent","kf":"bark painting","d":"Art centre at Yirrkala, Arnhem Land.","s":BK,"sig":["Arnhem Land bark painting"]},
 {"n":"Injalak Arts","c":"Australia","f":"","seg":"Artisan & independent","kf":"bark painting","d":"Art centre at Gunbalanya, Arnhem Land.","s":BK,"sig":["Arnhem Land bark painting"]},
 b("Jangarh Singh Shyam","India","Gond painting","Pardhan Gond painter (1962–2001), founder of Jangarh Kalam.",JS,["Gond painting"]),
 b("Jivya Soma Mashe","India","Warli painting","Modern father of Warli painting on paper and canvas.",WR,["Warli painting"]),
 b("Sita Devi","India","Madhubani","Madhubani painter, Padma Shri 1981.",MB,["Madhubani painting"]),
 b("Edward Tingatinga","Tanzania","Tingatinga","Founder of the Tingatinga style (died 1972).",TT,["Tingatinga school painting"]),
 {"n":"Tingatinga Arts Cooperative Society","c":"Tanzania","f":"1990","seg":"Artisan & independent","kf":"Tingatinga","d":"Painters' cooperative at Oyster Bay, Dar es Salaam.","s":TT,"sig":["Tingatinga school painting"]},
 b("Henri Rousseau","France","naïve painting","Self-taught French painter (1844–1910), 'Le Douanier'.",HR,["Rousseau-style jungle and dream painting"]),
 b("Hector Hyppolite","Haiti","Vodou painting","Self-taught Haitian painter and oungan (1894–1948).",HH,["Haitian painting"]),
 b("Ivan Generalić","Croatia","naïve painting","First master of the Hlebine school.",NA,["Hlebine painting"]),
 b("Jean Dubuffet","France","art brut","French artist who named and collected art brut.",OA,["Art brut"]),
 b("Adolf Wölfli","Switzerland","outsider art","Swiss psychiatric patient-artist (1864–1930) at Waldau.",AW,["Wölfli illustrated epic"]),
 b("Henry Darger","United States","outsider art","Chicago janitor-artist (1892–1973) of In the Realms of the Unreal.",HD,["Darger Vivian Girls painting"]),
]
trads=[
 {"n":"Western Desert painting","g":"Painting","r":"Central and Western Desert, Australia","p":"1971 onward","d":"Acrylic painting of Dreaming stories begun at Papunya.","tech":"dotting, roundels, ground designs","mat":"acrylic on canvas or board","forms":["Western Desert dot painting"],"ctr":["Papunya Tula","Yuendumu","Utopia","Balgo","Kintore"],"auth":"Buy through art centres or Indigenous Art Code signatories; works over A$250 should carry a certificate on art-centre or gallery letterhead matching the work; a photo of the artist is not a certificate.","s":IAC},
 {"n":"Arnhem Land bark painting","g":"Painting","r":"Arnhem Land and Top End, Australia","p":"ceremonial origin; market form from 1912","d":"Ochre painting on stringybark with clan rarrk designs.","tech":"rarrk cross-hatching, x-ray style","mat":"stringybark, ochres, pipeclay","forms":["Arnhem Land bark painting"],"ctr":["Yirrkala (Buku-Larrnggay Mulka)","Gunbalanya (Injalak Arts)","Maningrida","Ramingining"],"auth":"Art-centre documentation and catalogue number.","s":BK},
 {"n":"Mithila painting","g":"Painting","r":"Mithila, Bihar (India) and Nepal","p":"traditional; on paper from the 1960s","d":"Women's wall and floor painting moved onto paper and canvas.","tech":"Bharni, Kachni, Tantrik, Godna, Kohbar styles","mat":"natural pigments, paper, cloth","forms":["Madhubani painting"],"ctr":["Madhubani district","Sita Devi","Ganga Devi"],"auth":"GI-registered; natural pigments and named artist.","s":MB},
 {"n":"Pattachitra","g":"Painting","r":"Odisha and West Bengal, India","p":"traditional","d":"Cloth and palm-leaf painting for Jagannath worship and sung scrolls.","tech":"gum-chalk primed cloth, Mota Kala and Saru Kala lines","mat":"cotton cloth, palm leaf, mineral pigments","forms":["Pattachitra"],"ctr":["Raghurajpur","Puri","Naya (Medinipur)"],"auth":"GI registered 2008 (Odisha) and 2018 (Bengal).","s":PC},
 {"n":"Warli painting","g":"Painting","r":"Northern Sahyadri, Maharashtra","p":"traditional; on paper from the 1970s","d":"White geometric figures on ochre or mud walls.","tech":"rice-paste with chewed bamboo stick","mat":"rice paste, mud, ochre, paper","forms":["Warli painting"],"ctr":["Dahanu","Talasari","Jawhar","Jivya Soma Mashe"],"auth":"GI registered.","s":WR},
 {"n":"Kalighat painting","g":"Painting","r":"Kolkata, West Bengal","p":"c. 1800–1930","d":"Temple-market watercolours by Patua painters.","tech":"bold outline, wash, tin lustre","mat":"paper, natural pigments, colloidal tin","forms":["Kalighat painting"],"ctr":["Kalighat temple","V&A collection (645 works)"],"auth":"Antique paper and pigments; later revivals common.","s":KG},
 {"n":"Tingatinga","g":"Painting","r":"Dar es Salaam, Tanzania","p":"1968 onward","d":"Enamel painting of animals and scenes for the tourist market.","tech":"layered bicycle enamel, horror vacui","mat":"masonite, enamel paint","forms":["Tingatinga school painting"],"ctr":["Oyster Bay, Dar es Salaam","Tingatinga Arts Cooperative Society"],"auth":"Signature; cooperative provenance.","s":TT},
 {"n":"Mexican votive painting","g":"Painting","r":"Mexico","p":"late 18th century onward","d":"Saint retablos and narrative ex-votos on tin.","tech":"oil on tin with written testimony","mat":"tin sheet, oil paint","forms":["Narrative ex-voto","Saint retablo"],"ctr":["Basilica of Our Lady of Guadalupe","Sanctuary of Chalma","Hermenegildo Bustos"],"auth":"Dated inscription, aged tin; modern works often on paper.","s":VP},
]
notes="New shelf; no old kinds. Six kinds as planned. Pattachitra, Kalighat etc. are archetypes of Indian folk painting. Hermannsburg watercolour added under Aboriginal painting. Artist register entries use seg Artisan & independent. ULAN ids not retrieved. Retablo and ex-voto: modern fakes not covered by source."
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/00_04.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
