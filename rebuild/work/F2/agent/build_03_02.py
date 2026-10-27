import json, os
W='https://en.wikipedia.org/wiki/'
PT=W+'Platinum_print'; HM='https://www.harvardmagazine.com/2017/09/a-tale-of-two-cameras'; IF=W+'Instant_film'
TA='https://www.tate.org.uk/tate-etc/issue-33-spring-2015/out-light-shadows'; AA=W+'Anna_Atkins'
YE='https://yalealumnimagazine.org/articles/2271-object-lesson'; AC='https://ackland.org/?p=384'
CD='https://www.metmuseum.org/en/essays/the-last-print-man-ray-champs-delicieux'
def V(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Instant print","a":"Polaroid · instant photograph","d":"A self-developing print from an instant camera or film pack.",
  "t":["integral (self-contained)","peel-apart (pack or roll)","Polaroid SX-70 / 600 square","Spectra / Image (91 × 74 mm)","Instax Mini","Instax Wide","Instax SQUARE","large format (4 × 5, 8 × 10, 20 × 24)","black-and-white or colour","signed unique print"],
  "s":"https://www.1stdibs.com/art/photography/black-white-photography/material/polaroid/?page=17",
  "x":[
   {"n":"Polaroid peel-apart print","a":"Polaroid-Land print · Polacolor","d":"The original instant print, peeled from its negative after development.","mk":"Polaroid","y":"1948","s":IF,
    "v":[V("Polaroid-Land roll film (sepia)","Polaroid","1948"),V("Black-and-white roll film","Polaroid","1950"),V("4 × 5 sheet film","Polaroid","1958"),V("8 × 10 film","Polaroid","1973"),V("FP-100C pack film","Fujifilm","to 2016","discontinued 2016")],
    "dt":"film type · size · coater marks · fading"},
   {"n":"Polaroid SX-70 integral print","a":"","d":"The first integral instant print, developing by itself with no peeling, introduced with the SX-70 system.","mk":"Polaroid","y":"1972","s":IF,
    "v":[V("SX-70 film","Polaroid","1972"),V("600 film (79 mm square image)","Polaroid",""),V("Spectra film (91 × 74 mm)","Polaroid",""),
         V("PX100 and PX600","Impossible Project","2010","after Polaroid stopped film in 2008"),V("Polaroid Originals film","Polaroid","2017","Impossible Project renamed")],
    "dt":"film generation · frame · colour shift · unique or signed"},
   {"n":"Walker Evans SX-70 Polaroid","a":"","d":"Walker Evans's small colour SX-70 prints of signs, buildings and people, his last photographs.","mk":"Walker Evans","y":"1973–1975","s":YE,
    "v":[V("'Dead End' sign, five Polaroids","Walker Evans","c. 1974","one signed for John Benson")],
    "dt":"subject · signed or estate · provenance"},
   {"n":"Warhol Polacolor portrait","a":"Warhol Polaroid","d":"Andy Warhol's close-up Polaroid portraits of sitters, often studies for painted portraits.","mk":"Andy Warhol","y":"1970–1987","s":AC,
    "v":[V("Bianca Jagger","Andy Warhol","1979","Polacolor Type 108, 4¼ × 3⅜ in")],
    "dt":"sitter · film type · Warhol Foundation stamp · provenance"},
   {"n":"Polaroid 20 × 24 print","a":"","d":"A unique large instant print from Polaroid's room-sized 20 × 24 camera, lent to artists from the late 1970s.","mk":"Polaroid","y":"1976 onward","s":HM,
    "v":[V("1979 Polaroid exhibition of 20 × 24 works","Polaroid","1979","18 artists including Andy Warhol and Chuck Close")],
    "dt":"artist · subject · colour or black-and-white"},
   {"n":"Fujifilm Instax print","a":"Instax","d":"Fujifilm's integral instant print, the main instant format after 2008.","mk":"Fujifilm","y":"1998","s":IF,
    "v":[V("Instax Mini","Fujifilm","US 2009"),V("Instax Wide","Fujifilm","US 2008"),V("Instax SQUARE","Fujifilm","2017")],
    "dt":"format · frame design · monochrome or colour"}]},
 {"n":"Platinum or palladium print","a":"platinotype · palladiotype · platinum-palladium print","d":"An image in platinum or palladium metal on paper, matte and very permanent.",
  "t":["platinum","palladium","platinum-palladium","pigment over platinum","hot bath","cold bath","period print","modern print"],
  "s":"https://www.1stdibs.com/art/photography/black-white-photography/ian-sanderson-franci-sales-platinum-palladium-print-over-pure-gold-leaf-limited-edition/id-a_14269852",
  "x":[
   {"n":"Platinotype","a":"","d":"The commercial platinum paper patented by William Willis and sold across Europe and the United States until 1916.","mk":"Platinotype Company","y":"1873–1916","s":PT,
    "v":[V("Willis patent","Platinotype Company","1873","British Patent No. 2011"),V("Palladiotype paper","Platinotype Company",""),V("Satista (silver-platinum)","Platinotype Company","")],
    "dt":"paper · tone · period"},
   {"n":"Pictorialist platinum print","a":"","d":"A soft, matte platinum print favoured by pictorialist photographers around 1890–1915.","mk":"","y":"1880s–1910s","s":PT,
    "v":[V("Coming Home from the Marshes","Peter Henry Emerson","1886"),V("Georgia O'Keeffe","Alfred Stieglitz",""),V("The Flatiron","Edward Steichen","","pigment over platinum"),
         V("Dance Study","Adolph de Meyer","1912"),V("Blind Woman, New York","Paul Strand","")],
    "dt":"photographer · period print or later · tone · mount"},
   {"n":"Modern platinum print","a":"","d":"A platinum or platinum-palladium print made by a later photographer for its tonal range and permanence.","mk":"","y":"20th century onward","s":PT,
    "v":[V("Cigarette No. 98, New York","Irving Penn",""),V("Platinum prints","Robert Mapplethorpe","")],
    "dt":"photographer · edition · paper"}]},
 {"n":"Cyanotype","a":"blueprint","d":"An iron-salt print giving a blue image, invented by Sir John Herschel in 1842.",
  "t":["photogram (contact)","from negative","toned","on fabric","album or book"],
  "s":"https://www.1stdibs.com/art/paintings/landscape-paintings/kind-cyan-serene-cloudy-sky-triptych-blue-relaxing-skyscape-multi-panel-blueprint/id-a_13844502",
  "x":[
   {"n":"Atkins – Photographs of British Algae","a":"Cyanotype Impressions","d":"Anna Atkins's self-published cyanotype contact prints of seaweed, the first book illustrated with photographic images.","mk":"Anna Atkins","y":"1843–1853","s":AA,
    "v":[V("Photographs of British Algae: Cyanotype Impressions","Anna Atkins","1843–1853","three volumes; about 17 copies known; one sold for £229,250 in 2004"),
         V("Cyanotypes of British and Foreign Ferns","Anna Atkins","1853","with Anne Dixon")],
    "dt":"part and plate · species · completeness · fading"}]},
 {"n":"Photogram","a":"rayograph · schadograph · photogenic drawing","d":"An image made without a camera by placing objects on light-sensitive material.",
  "t":["gelatin silver","salted paper","cyanotype","colour","unique","editioned"],
  "s":"https://www.1stdibs.com/art/prints-works-on-paper/figurative-prints-works-on-paper/material/photogram",
  "x":[
   {"n":"Talbot photogenic drawing","a":"","d":"Talbot's early images of leaves or lace laid on sensitised paper, precursors of the photogram.","mk":"Henry Fox Talbot","y":"1835","s":TA,"dt":"subject · fading · paper"},
   {"n":"Schadograph","a":"","d":"Christian Schad's Dada photograms of torn tickets and scraps, named by Tristan Tzara.","mk":"Christian Schad","y":"1918–1919","s":TA,"dt":"subject · print date"},
   {"n":"Rayograph","a":"","d":"Man Ray's photogram, made by laying objects on photographic paper.","mk":"Man Ray","y":"1922","s":CD,
    "v":[V("Champs délicieux","Man Ray","1922","album of 12 rayographs, edition of 40, preface by Tristan Tzara"),V("Copy no. 41 with cancelled images","Man Ray","","post-edition copy")],
    "dt":"unique or album print · copy number · condition"},
   {"n":"Moholy-Nagy photogram","a":"","d":"László Moholy-Nagy's abstract light photograms, taught at the Bauhaus and the New Bauhaus in Chicago.","mk":"László Moholy-Nagy","y":"1920s–1940s","s":TA,"dt":"print date · unique"},
   {"n":"Contemporary cameraless photograph","a":"","d":"A recent cameraless work extending the photogram.","mk":"","y":"21st century","s":TA,
    "v":[V("Cameraless works","Liz Deschenes",""),V("Cameraless works","Walead Beshty",""),V("Cameraless works","Sam Falls","")],
    "dt":"artist · medium · edition"}]}]
P="Artisan & independent"
def B(n,c,f,seg,kf,d,s,sig): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 B("Polaroid","United States","1937","Specialist","instant film","American maker of instant cameras and film, founded by Edwin Land.","knowledge",["Polaroid peel-apart print","Polaroid SX-70 integral print","Polaroid 20 × 24 print"]),
 B("Fujifilm","Japan","1934","Professional & flagship","film, Instax","Japanese photographic company, maker of Instax instant film.","knowledge",["Fujifilm Instax print"]),
 B("Impossible Project","Netherlands","2008","Specialist","instant film revival","Company that took over Polaroid's Enschede factory and revived integral film, later renamed Polaroid Originals.",IF,[]),
 B("Walker Evans","United States","",P,"documentary photographs","American photographer who used the SX-70 in his last years.",YE,["Walker Evans SX-70 Polaroid"]),
 B("Andy Warhol","United States","",P,"pop art, Polaroids","American pop artist whose Polaroid portraits were given to museums by his foundation in 2008.",AC,["Warhol Polacolor portrait"]),
 B("Platinotype Company","United Kingdom","1880","Specialist","platinum paper","William Willis's company selling platinotype paper.",PT,["Platinotype"]),
 B("Anna Atkins","United Kingdom","",P,"cyanotypes","English botanist and photographer (1799–1871).",AA,["Atkins – Photographs of British Algae"]),
 B("Henry Fox Talbot","United Kingdom","",P,"calotype, salt prints","English photographic inventor, maker of photogenic drawings from 1835.",TA,["Talbot photogenic drawing"]),
 B("Christian Schad","Germany","",P,"schadographs","German artist who made Dada photograms in 1918–19.",TA,["Schadograph"]),
 B("Man Ray","United States","",P,"rayographs","American Dada and Surrealist artist in Paris, maker of rayographs.",CD,["Rayograph"]),
 B("László Moholy-Nagy","Hungary","",P,"photograms","Hungarian Bauhaus artist and teacher who explored the photogram.",TA,["Moholy-Nagy photogram"]),
]
out={"kinds":kinds,"brands":brands,"traditions":[],
 "notes":"Four old kinds kept with old sources. Mapplethorpe 20 × 24 and SX-70 works not found on a fetched page (only as platinum-print maker). Steichen/Stieglitz platinum prints are versions under a maker-free pictorialist archetype; their register entries come from the 03_01 shelf. Warhol's Big Shot camera not named on the fetched page, so omitted. Met collection records and Getty Atkins essay were rate-limited (429/503); Met Champs délicieux essay fetched via Firecrawl. Polaroid and Fujifilm register entries from knowledge."}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/03_02.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
