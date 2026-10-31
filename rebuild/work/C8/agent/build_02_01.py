import json, os
W='https://en.wikipedia.org/wiki/'
ENC=W+'Encaustic_tile'; CEM=W+'Cement_tile'; ZEL=W+'Zellij'; DEL=W+'Delftware'; AZU=W+'Azulejo'; TAL=W+'Talavera_pottery'
TDR=W+'Talavera_de_la_Reina_pottery'; MIN=W+'Mintons'; MAW=W+'Maw_%26_Co'; CD=W+'Craven_Dunnill'; RD=W+'Royal_Delft'; RT=W+'Royal_Tichelaar_Makkum'
SAL=W+'Saltillo_tile'; QT=W+'Quarry_tile'; PAN=W+'Pantile'; ROOF=W+'Roof_tiles'; TOM=W+'Tomette'
def X(n,d,s,mk='',y='',a='',v=None,dt=''):
    o={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: o["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    if dt: o["dt"]=dt
    return o
kinds=[
{"n":"Encaustic tile","a":"inlaid tile · Victorian encaustic tile","d":"Fired clay tile whose pattern is inlaid in differently coloured clays rather than painted or glazed.",
 "t":["Victorian geometric floor tile","two-colour","multi-colour (up to six clays)","glazed","unglazed"],"s":ENC,
 "x":[X("Minton encaustic tile","Gothic Revival inlaid floor and wall tile developed by Herbert Minton, with designs by Augustus Pugin.",MIN,"Mintons","1845",a="Minton Hollins tile",
        v=[("Minton, Hollins & Company","Mintons","1845","partnership formed to make decorative floor and wall tiles"),("Pugin tiles, St George's Cathedral, Southwark","Mintons","1847–48",""),("United States Capitol floor","Mintons","1856","")],
        dt="inlaid coloured clays · churches, public buildings, homes"),
      X("Medieval inlaid tile","Original inlaid paving tile of medieval churches and abbeys, chiefly English, later copied by Victorian makers.",ENC,"","13th–16th century",
        v=[("Printed inlaid tile","","later medieval","shallow inlay of about 3 mm")],dt="inlay depth c. 3–6.4 mm · mostly two colours"),
      X("Maw & Co encaustic and geometric tile","Encaustic and plain geometric floor tiles from the Shropshire maker, made at Broseley and later Jackfield.",MAW,"Maw & Co","1850",
        v=[("Benthall Works, Jackfield","Maw & Co","1883","move from Broseley")],dt="encaustic and geometric floor styles · designs incl. Walter Crane, Lewis F. Day"),
      X("Craven Dunnill encaustic tile","Encaustic tiles modelled on medieval originals, made at Jackfield for churches such as Chester Cathedral.",CD,"Craven Dunnill","1872",
        v=[("Craven Dunnill Jackfield revival","Craven Dunnill","2000","traditional Victorian methods"),("House of Commons Central Lobby floor restoration","Craven Dunnill","2021","")],
        dt="inlaid clays · medieval-style patterns")]},
{"n":"Cement tile","a":"encaustic cement tile · hydraulic tile · mosaico hidráulico · cementine · gạch bông","d":"Unfired, pressed tile with a coloured white-cement face layer over a grey cement body.",
 "t":["Catalan/Spanish mosaico hidráulico","Italian cementine","Vietnamese gạch bông","hand-press","electric hydraulic press"],"s":CEM,
 "x":[X("Catalan hydraulic tile","Original pressed cement tile with profuse patterns, developed in Catalonia in the 1850s and spread across Europe and America.",CEM,"","1850s",a="paviment hidràulic",
        v=[("Garret & Rivet tiles, Paris International Exposition","Garret & Rivet","1867","")],dt="colour layer 2.5–4 mm · mineral pigments · white cement, marble powder")]},
{"n":"Zellige","a":"zellij · zillij · alicatado","d":"Mosaic of hand-cut glazed terracotta pieces fitted into geometric patterns, the classic tilework of Morocco and al-Andalus.",
 "t":["star pattern","rosette","sgraffito","panel","loose pieces"],"s":ZEL,
 "x":[X("Fez zellige","Glazed squares of grey Fez clay cut by hand after firing into shapes for tight-fitting star and rosette patterns.",ZEL,"","14th century–present",
        v=[("Marinid madrasa panels (al-Attarine, Bou Inania)","","14th century",""),("Bab Bou Jeloud, Fez","","1913","")],
        dt="c. 10 cm glazed squares cut by adze-hammer · 6-, 8-, 12-, 16-pointed stars · yellow, blue, brown, green, white"),
      X("Nasrid alicatado","Andalusi tile mosaic of the Alhambra, known for the curved three-pointed 'Nasrid bird' motif.",ZEL,"","14th century",a="pajarita nazarí",
        v=[("Torre de la Cautiva, Alhambra","","14th century","unique purple glaze"),("Court of the Myrtles, Alhambra","","14th century","")],dt="plaster backing with esparto and cane"),
      X("Tétouan zellige","Northern Moroccan zellige cut before firing, harder-glazed but duller and looser-fitting; noted for the 'four hammers' motif.",ZEL,"","19th century",a="arba'a matariq",
        dt="cut before baking · looser joints")]},
{"n":"Delft tile","a":"Dutch tile · Delft blue tile","d":"Dutch tin-glazed earthenware wall tile, usually painted in cobalt blue on white.",
 "t":["blue-and-white","single tile","reproduction"],"s":DEL,
 "x":[X("Makkum tile","Tin-glazed tiles and wares from the Friesland pottery founded in 1594, still made by the majolica technique.",RT,"Royal Tichelaar Makkum","1594",
        dt="white tin glaze after first firing · restoration of historic Delft blue"),
      X("Royal Delft tile","Delft Blue from the last of the 17th-century Delft factories, revived by Joost Thooft in 1876.",RD,"Royal Delft","1653",a="De Porceleyne Fles",
        v=[("Thooft revival","Royal Delft","1876","hand-painted pieces carry Thooft's trademark")],dt="underglaze cobalt blue on white body")]},
{"n":"Azulejo","a":"Portuguese tile · Spanish tile","d":"Iberian painted tin-glazed tile, used singly or in large panels on façades and interiors.",
 "t":["single pattern tile","figurative panel","façade tile","reproduction"],"s":AZU,
 "x":[X("Hispano-Moresque cuenca tile","Mould-pressed Seville tile with clay ridges separating the glazes, the cheaper successor to cut-tile alicatado.",AZU,"","late 15th–16th century",a="arista tile · cuerda seca tile",
        v=[("Cuerda seca","","","older technique with greasy lines between colours")],dt="pressed ridges · polychrome glazes"),
      X("Enxaquetado","Checkerboard azulejo pattern covering large church and monastery walls; polychrome form called enxaquetado rico.",AZU,"","late 16th century"),
      X("Azulejo de tapete","Carpet-like repeat compositions of pattern tiles covering whole walls.",AZU,"","",a="carpet azulejo"),
      X("Aves e ramagens","Birds-and-branches design popular in Portugal.",AZU,"","1650–1680"),
      X("Joanine blue-and-white panel","Large figurative blue-and-white panels of the Golden Age under João V.",AZU,"","1706–1750",a="Ciclo dos Mestres"),
      X("Pombaline tile","Austere pattern tiles of Lisbon's rebuilding after the 1755 earthquake.",AZU,"","after 1755"),
      X("Rato tile","Tiles of the Real Fábrica de Louça do Rato, with master-designer Sebastião Inácio de Almeida.",AZU,""),
      X("Art Nouveau and Art Deco façade tile","Industrial and transfer-printed façade tiles of the late 19th and 20th centuries.",AZU,"","late 19th–20th century",
        v=[("São Bento station panels (Jorge Colaço)","","","about 20,000 tiles"),("Lisbon Metro panels (Maria Keil)","","1957–1972","")])]},
{"n":"Talavera tile","a":"Talavera azulejo · Puebla tile","d":"Hand-painted tin-glazed tile in the Talavera tradition of Puebla, Mexico, or Talavera de la Reina, Spain.",
 "t":["certified (DO hologram)","uncertified majolica","blue-and-white","polychrome"],"s":TAL,
 "x":[X("Puebla Talavera tile","Mexican tin- and lead-glazed tile under the 1997 Denominación de Origen, in up to six natural colours.",TAL,"","1550 onward",
        v=[("Uriarte Talavera","Uriarte Talavera","1824","oldest continuously operating certified workshop"),("Casa de los Azulejos façade, Mexico City","","18th century","")],
        dt="blue, yellow, black, green, orange, mauve · milky crazed glaze · hologram, signature, workshop logo"),
      X("Talavera de la Reina tile","Spanish tin-glazed azulejos from Talavera de la Reina, the source of the Mexican tradition.",TDR,"","15th century onward",
        v=[("Golden Chapel tiles, New Cathedral of Salamanca","","1515",""),("Ruiz de Luna workshop","","","")],dt="Renaissance, Baroque, hunting and bird scenes")]},
{"n":"Terracotta floor tile","a":"cotto · terracotta tile · red floor tile","d":"Unglazed fired-clay floor tile, often handmade and sealed after laying.",
 "t":["cotto","Saltillo","tomette","quarry tile","handmade","machine-pressed"],"s":TOM,
 "x":[X("Saltillo tile","Porous handmade terracotta tile from Saltillo, Coahuila, pressed in a wooden frame or carved, in reds, oranges and yellows.",SAL,"","",
        v=[("Super","","","pressed in a wooden frame"),("Regular","","","carved shape"),("Manganese","","","light and dark brown")],dt="unglazed · needs sealing · bumps, chips, fingerprints"),
      X("Tomette","Hexagonal (sometimes octagonal) terracotta floor tile of southern France, made at Apt and Salernes.",TOM,"","1829",dt="six- or eight-sided · iron-rich red clay"),
      X("Quarry tile","Dense pressed or extruded clay or shale floor tile fired like brick, traditionally red, grey or near-black.",QT,"","",
        dt="6–12 in square (UK) · 1/2–3/4 in thick · unglazed")]},
{"n":"Handmade clay roof tile","a":"handmade plain tile · handmade pantile","d":"Roof tile formed by hand from fired clay, used for heritage roofs and repairs.",
 "t":["plain (flat) tile","pantile","ridge tile","reclaimed match"],"s":ROOF,
 "x":[X("Plain tile","Flat double-lap clay tile, the common hand-made roof tile of medieval northern Europe.",ROOF,"","medieval",a="flat tile · shingle tile"),
      X("Pantile","S-profile single-lap clay tile, lighter and laid at lower pitch; brought to eastern England and Scotland from the Netherlands.",PAN,"","early 17th century (Britain)",
        dt="S profile · single lap · Norfolk, East Yorkshire, Fife, Bridgwater"),
      X("Mission tile","Semi-cylindrical pan-and-cover tile, early examples bent over a worker's thigh.",ROOF,"","",a="monk and nun tile",
        v=[("Mission San Antonio de Padua, California","","1780","")]),
      X("Imbrex and tegula","Ancient Greek and Roman flat pan with curved cover tile.",ROOF,"","700–650 BC (Corinth)")]},
]
brands=[
{"n":"Mintons","c":"England","f":"1793","seg":"Heritage tile and pottery maker","d":"Stoke-upon-Trent pottery whose Minton Hollins tile arm led the Victorian encaustic revival.","lines":["Minton, Hollins & Company tiles","majolica"],"eras":["Herbert Minton, 1836–","Léon Arnoux art director, 1849–"],"sig":["Minton encaustic tile"],"sc":["Gothic Revival"],"rel":["Maw & Co","Craven Dunnill"],"s":MIN},
{"n":"Maw & Co","c":"England","f":"1850","seg":"Heritage tile maker","d":"Shropshire maker best known for encaustic and geometric floor tiles; closed 1970.","lines":["encaustic tiles","geometric tiles","art pottery"],"eras":["Worcester 1850","Broseley 1852","Benthall Works, Jackfield 1883–1970"],"sig":["Maw & Co encaustic and geometric tile"],"sc":["Victorian"],"rel":["Craven Dunnill","Mintons"],"s":MAW},
{"n":"Craven Dunnill","c":"England","f":"1872","seg":"Heritage tile maker","d":"Jackfield tile maker of medieval-style encaustic tiles, reviving traditional manufacture since 2000.","lines":["encaustic tiles","Craven Dunnill Jackfield"],"eras":["Jackfield Works 1874–1951","Craven Dunnill Jackfield 2000–"],"sig":["Craven Dunnill encaustic tile"],"sc":["Victorian","church restoration"],"rel":["Maw & Co","Mintons"],"s":CD},
{"n":"Royal Delft","c":"Netherlands","f":"1653","seg":"Heritage Delftware maker","d":"Koninklijke Porceleyne Fles, the only survivor of Delft's 17th-century earthenware factories.","lines":["Delft Blue"],"eras":["Joost Thooft revival, 1876–","Royal title 1919"],"sig":["Royal Delft tile"],"sc":["Dutch"],"rel":["Royal Tichelaar Makkum"],"s":RD},
{"n":"Royal Tichelaar Makkum","c":"Netherlands","f":"1594","seg":"Heritage tile and pottery maker","d":"Friesland pottery making tin-glazed earthenware and tiles, also restoring historic Delft blue.","lines":["majolica pottery","tiles"],"eras":["Royal title 1960"],"sig":["Makkum tile"],"sc":["Dutch"],"rel":["Royal Delft"],"s":RT},
{"n":"Uriarte Talavera","c":"Mexico","f":"1824","seg":"Certified Talavera workshop","d":"Puebla workshop founded by Dimas Uriarte, the oldest continuously operating certified Talavera maker.","lines":["Talavera tiles and pottery"],"eras":[],"sig":["Puebla Talavera tile"],"sc":["Mexican"],"rel":[],"s":TAL},
]
G="Ceramics & glass"
trads=[
{"n":"Victorian encaustic tile","g":G,"r":"England","p":"13th–16th century; revived c. 1840–1930s","d":"Inlaid-clay floor tiles of medieval England, mass-produced again in the Gothic Revival.","tech":"two-shot moulding of coloured clay inlay backfilled with body clay, then fired","mat":"coloured clays","forms":["Encaustic tile"],"ctr":["Mintons, Stoke-upon-Trent","Maw & Co, Jackfield","Craven Dunnill, Jackfield","Jackfield Tile Museum"],"auth":"pattern runs through the body (inlay 3–6.4 mm), not painted on the surface","s":ENC},
{"n":"Zellige","g":G,"r":"Morocco, Algeria, al-Andalus","p":"10th/11th century–present","d":"Hand-cut glazed tile mosaic in Islamic geometric patterns.","tech":"glazed squares cut by hand with an adze-hammer, assembled face down and backed with plaster","mat":"Fez grey kaolinitic clay, metal-oxide glazes","forms":["Zellige"],"ctr":["Fez","Meknes","Salé","Marrakesh","Tétouan","Tlemcen"],"auth":"Fez pieces cut after firing and fit tightly; Tétouan pieces cut before firing, looser fit","s":ZEL},
{"n":"Delftware","g":G,"r":"Netherlands","p":"1570s–present (main period 1640–1740)","d":"Dutch tin-glazed earthenware, including some eight hundred million tiles over two centuries.","tech":"underglaze cobalt painting on white-glazed earthenware","mat":"blend of local, Tournai and Rhineland clays; tin glaze; cobalt oxide","forms":["Delft tile"],"ctr":["Delft","Makkum","Gouda","Rotterdam","Haarlem","Amsterdam","Royal Delft","Royal Tichelaar Makkum"],"auth":"","s":DEL},
{"n":"Azulejo","g":G,"r":"Portugal and Spain","p":"13th century–present","d":"Iberian painted tin-glazed tilework for façades, churches and interiors.","tech":"alicatado, cuerda seca, cuenca/arista, maiolica painting, later transfer-printing","mat":"tin-glazed earthenware","forms":["Azulejo"],"ctr":["Seville","Lisbon","Porto","Caldas da Rainha","Viúva Lamego","Real Fábrica de Louça do Rato","National Museum of the Azulejo"],"auth":"","s":AZU},
{"n":"Talavera","g":G,"r":"Puebla and Tlaxcala, Mexico; Talavera de la Reina, Spain","p":"16th century–present","d":"Tin-glazed majolica tradition shared by Mexico and Spain, on UNESCO's list since 2019.","tech":"two firings, hand painting in natural pigments that blur into a milky crazed glaze","mat":"black Amozoc and white Tecali sands with natural clays; tin and lead glaze","forms":["Talavera tile"],"ctr":["Puebla","Atlixco","Cholula","Tecali","San Pablo del Monte","Talavera de la Reina","Uriarte Talavera","Ruiz de Luna"],"auth":"DO hologram, potter's signature, workshop logo, base inscription with artist's initials and Puebla","s":TAL},
]
notes=("New shelf, no old kinds. Archetypes sourced from retrieved Wikipedia pages. Left out: Delft tile motifs (ships, biblical, corner motifs) and English delftware - not confirmed on a retrieved page; "
 "American Encaustic Tiling Company (no brand page retrieved); machine-made interlocking roof tiles (Marseille, Ludowici) as not handmade; Viúva Lamego brand page (404) - kept as tradition centre only; "
 "Italian cotto/Impruneta archetype (no page retrieved) kept as a type.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/C8/shelves/02_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(len(kinds),sum(len(k['x']) for k in kinds),len(brands),len(trads))
