import json, os
W='https://en.wikipedia.org/wiki/'
DS=W+'D%C3%BCsseldorf_school_of_photography'; RH=W+'Rhein_II'; DT=W+'Dye-transfer_process'; IL=W+'Ilfochrome'
MG='https://www.magnumphotos.com/theory-and-practice/stories-hidden-magnum-distribution-vintage-prints/'
WE=W+'William_Eggleston'; GS=W+'Gelatin_silver_process'; CP=W+'Chromogenic_print'; AP=W+'Art_photography_print_types'
YO='https://yosemite.org/press-releases/rare-collection-of-ansel-adams-photography-donated-to-the-yosemite-museum-in-yosemite-national-park/'
MO=W+'Moonrise,_Hernandez,_New_Mexico'; TS=W+'Thomas_Struth'
SOT='https://www.sothebys.com/en/articles/the-complete-collectors-guide-to-photographic-prints'
def v(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Gelatin silver print","a":"silver gelatin print · black-and-white print",
  "d":"A black-and-white photograph of fine silver particles in a gelatin layer on paper, made in a darkroom; the standard process since the 1890s.",
  "t":["fibre-based (baryta) paper","resin-coated paper","selenium-toned","gold-toned","vintage print (made near the negative date)","printed later","estate print","mural size"],"s":SOT,
  "x":[
   {"n":"Ansel Adams Museum Set","a":"Museum Set print","d":"Sets of 25, 45 or 75 prints chosen from 75 images, made by Adams from 1979 to place his work in public collections.","mk":"Ansel Adams","y":"from 1979","s":YO,
    "v":[v("Moonrise, Hernandez, New Mexico","Ansel Adams","negative 1941","over 1,300 prints made; pre-1970 prints very rare; 1948 print sold for $609,600 in 2006"),
         v("Clearing Winter Storm, Yosemite National Park","Ansel Adams","","core image of every set"),
         v("45-print set","Ansel Adams","","e.g. Yosemite Museum set")],
    "dt":"set size 25/45/75 · core ten images · print date vs negative date · mount and signature"},
   {"n":"Magnum distribution press print","a":"agency print · press print","d":"A vintage print circulated by Magnum Photos to newspapers and magazines, its back carrying agency stamps, captions and editors' notes.","mk":"Magnum Photos","y":"","s":MG,
    "v":[],"dt":"verso stamps and annotations · caption label · crop marks · condition"},
   {"n":"Becher typology","a":"","d":"Grids of frontal black-and-white photographs of industrial structures by Bernd and Hilla Becher.","mk":"Bernd and Hilla Becher","y":"","s":DS,
    "v":[v("New Topographics exhibition","Bernd and Hilla Becher","1975","George Eastman House")],"dt":"single print vs grid (typology) · print size"}
  ]},
 {"n":"Chromogenic print","a":"C-print · C-type · Type C · Lambda print · LightJet print",
  "d":"A colour photograph whose cyan, magenta and yellow dyes form in the paper's emulsion layers during development; also printed digitally by laser.",
  "t":["Type C (from negative)","Type R (from transparency)","digital C-print (Lambda, LightJet, Chromira)","face-mounted to acrylic","mural size"],"s":SOT,
  "x":[
   {"n":"Düsseldorf School large-format print","a":"Becher school print","d":"Very large colour photographs by former Becher students, often mounted to acrylic glass and issued in small editions.","mk":"Andreas Gursky","y":"from 1989","s":DS,
    "v":[v("Rhein II","Andreas Gursky","1999","C-print on acrylic glass, 190 × 360 cm; $4,338,500 at Christie's 2011"),
         v("Museum Photographs","Thomas Struth","1989 onward","editions usually of ten"),v("Interiors","Candida Höfer",""),v("Works","Thomas Ruff","")],
    "dt":"size · edition number · acrylic face mount · artist-approved print"},
   {"n":"New Color photograph","a":"","d":"Early fine-art colour prints by the photographers who brought colour into museums from the 1960s–70s.","mk":"","y":"1962 onward","s":CP,
    "v":[v("MoMA colour exhibition","Ernst Haas","1962"),v("Colour prints","William Eggleston",""),v("Colour prints","Stephen Shore","")],"dt":"vintage vs later print · size"}
  ]},
 {"n":"Archival pigment print","a":"pigment print · inkjet print · giclée (photography)",
  "d":"A photograph printed with pigment inks on a large-format inkjet printer, usually on fine-art paper.",
  "t":["matte fine-art paper","baryta-type inkjet paper","pigment ink","dye ink","signed and editioned"],"s":SOT},
 {"n":"Dye-transfer print","a":"dye imbibition print",
  "d":"A colour print built by transferring cyan, magenta and yellow dyes from three gelatin relief matrices onto paper; Kodak ended the materials in 1994.",
  "t":["vintage dye transfer","later dye transfer from new matrices"],"s":SOT,
  "x":[{"n":"Eggleston dye transfer","a":"","d":"Saturated dye-transfer prints by William Eggleston, who found the process in a Chicago lab price list in 1973–74.","mk":"William Eggleston","y":"1973 onward","s":WE,
    "v":[v("The Red Ceiling","William Eggleston","1973"),v("14 Pictures","William Eggleston","1974","first portfolio"),v("Election Eve","William Eggleston","1977","artist book, edition of five"),v("William Eggleston's Guide","William Eggleston","1976","MoMA exhibition")],
    "dt":"portfolio vs single print · print date · size"},
   {"n":"Dye-transfer colour photograph","a":"","d":"Prints by the colour photographers who used dye transfer for its saturation and stability.","mk":"","y":"1940s–1994","s":DT,
    "v":[v("Prints","Eliot Porter",""),v("Prints","Ernst Haas",""),v("Prints","Marie Cosindas",""),v("Road Song","Pete Turner",""),v("Maybe Babies","Sandy Skoglund","")],"dt":"matrices · paper · print date"}]},
 {"n":"Silver dye bleach print","a":"dye destruction print · Cibachrome · Ilfochrome",
  "d":"A colour print from a transparency in which azo dyes already in the paper are bleached away where not wanted, giving vivid, sharp colour on a polyester base.",
  "t":["glossy polyester base","in-camera direct positive"],"s":IL,
  "x":[{"n":"Cibachrome / Ilfochrome print","a":"Ilfochrome Classic","d":"The Ciba-Geigy silver dye bleach paper, renamed Ilfochrome in 1992 and made until 2012.","mk":"Ilford","y":"1960s–2012","s":IL,
    "v":[v("Cibachrome","Ciba-Geigy","1960s","based on Gasparcolor"),v("Ilfochrome print","Ilford","1992","renamed"),v("Ilfochrome Classic final run","Ilford","2012")],
    "dt":"size · print date"}],
  "m":[]}
]
def a(n,c,kf,d,s,sig,seg="Artisan & independent",f=""): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 a("Ansel Adams","United States","landscape photography","American photographer who made the Museum Set prints from 1979.",YO,["Ansel Adams Museum Set"]),
 a("Magnum Photos","","photo agency","Photographers' cooperative agency whose distribution prints carry its stamps.",MG,["Magnum distribution press print"],"Specialist"),
 a("Bernd and Hilla Becher","Germany","typologies","Photographer couple who founded the Düsseldorf photography class in 1976.",DS,["Becher typology"]),
 a("Andreas Gursky","Germany","large-format colour","Düsseldorf School photographer of large panoramic views.",RH,["Düsseldorf School large-format print"]),
 a("Thomas Struth","Germany","museum photographs","Düsseldorf School photographer (born 1954).",TS,["Düsseldorf School large-format print"]),
 a("William Eggleston","United States","colour photography","American colour photographer known for dye-transfer prints.",WE,["Eggleston dye transfer"]),
 {"n":"Ilford","c":"United Kingdom","f":"1879","seg":"Heritage manufactory","kf":"photographic paper","d":"British maker of photographic film and paper; produced Ilfochrome.","s":"knowledge","sig":["Cibachrome / Ilfochrome print"]},
]
notes="Five old kinds kept with old sources. Ilfochrome model moved to a version of the Cibachrome/Ilfochrome archetype. Archival pigment print has no archetype (no specific edition confirmed). ULAN ids not retrieved. Ansel Adams 'Special Edition' prints not confirmed by a fetched page, so left out; Life-magazine press prints left out (only a search snippet)."
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/03_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
