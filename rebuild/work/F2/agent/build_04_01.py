import json, os
W='https://en.wikipedia.org/wiki/'
VT='https://visittuscany.com/en/crafts/volterra-alabaster'; NK='https://collections.vam.ac.uk/item/O17121/netsuke-okatori/'
BF='https://www.bada.org/features/makers-series-black-forest-carvings'; BI=W+'Bi_(jade)'; SC=W+'Scrimshaw'; OK=W+'Okimono'
QX='https://largeprint.khm.at/en/art-and-aesthetics-from-chinas-forbidden-city/celadon-jade-qixia-mountain-boulder-sculpture'
IP='https://www.inuitartfoundation.org/inuit-art-quarterly/iaq-online/how-osuitok-ipeelee-captured-life-in-stone'
IG='https://www.inuitartfoundation.org/iaq-online/what-the-igloo-tag-means-for-inuit-artists'
FC='https://www.finch-and-co.co.uk/artwork-detail/858480/0/an-after-the-antique-marble-portrait'
def V(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Stone carving","a":"marble sculpture · alabaster · soapstone carving","d":"Marble, limestone, alabaster or other stone carved to form.",
  "t":["marble","alabaster","soapstone or serpentinite","limestone","hardstone","after the antique","signed","bust","figure","relief"],
  "s":"https://www.singulart.com/en/sculpture",
  "x":[
   {"n":"Grand Tour marble after the antique","a":"","d":"A marble copy of a famous ancient bust or statue, bought by Grand Tour collectors who often preferred perfect replicas to damaged originals.","mk":"","y":"late 18th–19th century","s":FC,
    "v":[V("Bust of Cicero, signed 'Franco Franchi Copió in Carrara'","","early 19th century","62 cm")],
    "dt":"subject · marble quality · size · signature · weathering"},
   {"n":"Volterra alabaster carving","a":"","d":"Carved alabaster from Volterra in Tuscany, a craft dating back to the Etruscans and revived as an industry in 1792.","mk":"","y":"1792 onward (Volterrana School)","s":VT,
    "v":[V("Volterrana School work","","from 1792","from Marcello Inghirami Fei's factory workshop of 120 carvers")],
    "dt":"subject · translucency · detail · workshop"},
   {"n":"Inuit stone carving","a":"Kinngait (Cape Dorset) sculpture","d":"A sculpture in serpentinite or other stone by an Inuit artist, sold through northern co-operatives since the mid-20th century.","mk":"","y":"1950s onward","s":IP,
    "v":[V("Caribou","Osuitok Ipeelee",""),V("Queen Elizabeth II","Osuitok Ipeelee","")],
    "dt":"community · artist and disc or syllabic signature · stone · Igloo Tag"}]},
 {"n":"Wood carving","a":"carved wooden figure","d":"A figure or sculpture carved from wood.",
  "t":["limewood","walnut","boxwood","painted or natural","figure","relief","functional carving (stand, clock, box)"],
  "s":"https://www.1stdibs.com/furniture/decorative-objects/sculptures/figurative-sculptures/technique/hand-carved/?page=22",
  "x":[
   {"n":"Brienz 'Black Forest' carving","a":"Black Forest bear","d":"A carved figure or household piece from Brienz, Switzerland, named for its dark wood: bears, goats, birds of prey and chalets.","mk":"","y":"after 1816","s":BF,
    "v":[V("Bear figure","","19th century"),V("Hat stand, umbrella stand or clock","","19th century"),V("Carved bowls, cups and boxes","Christian Fischer","after 1816","founder of the industry")],
    "dt":"subject · size · quality of carving · glass eyes · function"}]},
 {"n":"Jade carving","a":"carved jade","d":"A figure or object carved from jade.",
  "t":["nephrite","jadeite","celadon","white","archaistic","imperial inscription","boulder (shanzi)"],
  "s":"https://www.1stdibs.com/buy/carved-jade-figure",
  "x":[
   {"n":"Bi disc","a":"jade bi","d":"A flat jade disc with a central hole, made from the Neolithic onward; its exact use is unknown.","mk":"","y":"Neolithic (Liangzhu, c. 3400–2250 BCE) onward","s":BI,
    "v":[V("Plain Liangzhu disc (nephrite)","","Neolithic"),V("Zhou carved bi","","Zhou","hexagonal pattern"),V("Western Han dragon bi","","Western Han"),
         V("Bi inscribed by the Qianlong Emperor","","1790","British Museum")],
    "dt":"period · stone colour · decoration · burial alteration · later copy"},
   {"n":"Qing jade boulder carving","a":"jade mountain · shanzi","d":"A jade boulder carved as a miniature landscape following the stone's natural shape, a Qianlong-period form.","mk":"","y":"Qianlong reign (1736–1795)","s":QX,
    "v":[V("Qixia Mountain boulder","","Qianlong","celadon jade, 23.5 cm; Palace Museum")],
    "dt":"jade colour · skin and inclusions · inscription · stand"}]},
 {"n":"Ivory and bone carving","a":"ivory carving · scrimshaw","d":"A figure or sculpture carved from ivory, bone, horn or antler; ivory trade is restricted under CITES and national laws.",
  "t":["elephant ivory","walrus ivory","sperm-whale tooth","bone","antler","horn","stained","pre-ban documentation"],
  "s":"https://www.1stdibs.com/buy/japanese-ivory-carvings",
  "x":[
   {"n":"Okimono","a":"","d":"A Japanese decorative carving for display in an alcove, larger than a netsuke; many ivory ones were made for Western buyers in the Meiji period.","mk":"","y":"Meiji period (1868–1912) and later","s":OK,
    "v":[V("Ivory Rakan","","c. 1860–1900","about 8.7 cm"),V("Jizai okimono","Yamada Sōbi","","articulated metal animal (cross-link to metal)")],
    "dt":"subject · material · signature · size · stand"},
   {"n":"Scrimshaw","a":"","d":"Engraving on whale teeth, bone, baleen or walrus tusk by whalers, its lines filled with soot or ink.","mk":"","y":"late 18th–19th century","s":SC,
    "v":[V("Engraved sperm-whale tooth","","after 1815"),V("Walrus tusk","",""),V("Modern scrimshaw on alternative materials","","","micarta, fossil ivory, camel bone")],
    "dt":"material · subject (whaling scenes) · legal status (pre-1973 marine ivory) · fakes"}]},
 {"n":"Netsuke","a":"根付","d":"A small Japanese toggle carving used to hang pouches from a sash on a cord; usually ivory or wood.",
  "t":["katabori (figure)","manjū (disc)","ivory","boxwood","stained","signed","Kyoto school","Edo or Meiji"],
  "s":NK,
  "x":[
   {"n":"Katabori netsuke","a":"shape-carved netsuke","d":"A three-dimensional figure netsuke, the most widely appreciated type; increasingly signed from the 18th century.","mk":"","y":"18th–19th century","s":NK,
    "v":[V("Quails on millet","Okatori","c. 1775–1825","stained ivory, Kyoto; V&A")],
    "dt":"subject · material · signature · cord holes (himotōshi) · wear"}]}]
P="Artisan & independent"
brands=[{"n":"Osuitok Ipeelee","c":"Canada","f":"","seg":P,"kf":"stone carving","d":"Kinngait Inuit sculptor (1922–2005) known for caribou and a portrait of Queen Elizabeth II.","s":IP,"sig":["Inuit stone carving"]}]
trads=[
 {"n":"Inuit stone carving","g":"Stone & carving","r":"Canadian Arctic (Kinngait/Cape Dorset and other communities)","p":"mid-20th century onward",
  "d":"Stone (serpentinite) and ivory sculpture by Inuit artists, marketed through northern co-operatives.","tech":"hand carving and polishing","mat":"serpentinite, soapstone, ivory, whalebone",
  "forms":["Inuit stone carving"],"ctr":["Kinngait (Cape Dorset)","West Baffin Eskimo Co-operative","Osuitok Ipeelee"],
  "auth":"Igloo Tag trademark, created by the Canadian government and run by the Inuit Art Foundation since 2017, marks authentic Inuit work; resin imitations have circulated since the mid-20th century","s":IG},
 {"n":"Volterra alabaster","g":"Stone & carving","r":"Volterra, Tuscany, Italy","p":"Etruscan period; industry from 1792",
  "d":"Carving of local alabaster, a soft stone suited to fine ornament and faces.","tech":"carving, turning and polishing","mat":"alabaster (quarried at Castellina Marittima)",
  "forms":["Volterra alabaster carving"],"ctr":["Volterra workshops","Marcello Inghirami Fei (1792)","Ecomuseo dell'Alabastro"],"auth":"workshop provenance; alabaster is softer than marble and unsuited to outdoor display","s":VT},
 {"n":"Brienz woodcarving","g":"Woodwork & furniture","r":"Brienz, Bernese Oberland, Switzerland","p":"after 1816",
  "d":"Souvenir and fine carving, sold as 'Black Forest' carving, of bears and Alpine animals and household pieces.","tech":"woodcarving","mat":"dark-toned wood",
  "forms":["Brienz 'Black Forest' carving"],"ctr":["Christian Fischer","School of Woodcarving (1884)","Swiss Woodcarving Museum (2009)"],"auth":"quality of carving separates master workshops from cheap souvenirs","s":BF},
 {"n":"Netsuke carving","g":"Ivory, bone & carving","r":"Japan (Kyoto, Osaka, Edo and provinces)","p":"Edo period (18th–19th century) and Meiji",
  "d":"Miniature toggle carving for the cord of hanging pouches, a sculptural art in its own right.","tech":"carving and staining","mat":"ivory, boxwood and other woods",
  "forms":["Netsuke","Okimono"],"ctr":["Kyoto (Tomotada school, Okatori)"],"auth":"carver's signature (common from the 18th century), wear around cord holes; later copies and resin casts exist","s":NK}]
out={"kinds":kinds,"brands":brands,"traditions":trads,
 "notes":"Four old kinds kept with old sources; Netsuke added. Old 'okimono' model line becomes the Okimono archetype under Ivory and bone carving. Igloo Tag founding year (1958) seen only in search excerpts, so not stated. Met Qianlong rock (429) and RCT Ipeelee (403) not fetched. Named Brienz master carvers (Huggler, Mäder) only in search excerpts, left out. Jadeite kept only as a 't' type."}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/04_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
