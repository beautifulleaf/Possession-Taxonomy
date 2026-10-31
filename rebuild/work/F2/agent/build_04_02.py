import json
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
AUTH="field-collected and used vs made for trade or tourists · provenance before 1970 · export and cultural-property law (UNESCO 1970 Convention)"
kinds=[
 {"n":"African mask","a":"tribal mask · dance mask · ritual mask","d":"A carved face or headdress made to be worn in masquerade or displayed, from West, Central or Southern Africa.",
  "t":["face mask","helmet mask","headdress or crest","plank mask","miniature or passport mask","dance mask worn in use","made-for-trade mask"],
  "s":W+"Traditional_African_masks",
  "x":[
   {"n":"Dan mask","a":"gle · ge","d":"Mask of the Dan of Liberia and Côte d'Ivoire, embodying a spirit; types include gentle, war and small personal masks.","mk":"","y":"","s":W+"Dan_masks",
    "v":[V("Dean gle","","","gentle, feminine-associated mask"),V("Bu gle","","","war mask, masculine-associated"),V("Ma go","","","small personal protective mask")],
    "dt":"face form · wood · patina · pigment · fibre or cloth attachments · used or made-for-trade"},
   {"n":"Punu mask","a":"white-face mask · mukudj","d":"White-faced mask of the Punu of south Gabon, with nine forehead dots for the nine clans.","mk":"","y":"","s":W+"Punu_people",
    "v":[V("White life-size mask","","","nine forehead dots, secret-society dance"),V("Mukudj female ancestor mask","","","diamond scarification"),V("Black training mask","","","danced at night")],
    "dt":"kaolin whitening · coiffure · scarification marks · wood"},
   {"n":"Chokwe mask","a":"mwana pwo · cikunza","d":"Masks of the Chokwe of Angola, DR Congo and Zambia, such as the female mwana pwo and the circumcision-rite cikunza.","mk":"","y":"","s":W+"Chokwe_people",
    "v":[V("Mwana pwo","","","mature woman or girl, fertility; danced by a man"),V("Cikunza","","","antelope-horn headdress, circumcision rites")],
    "dt":"facial scarification · fibre wig · wood or bark cloth"},
   {"n":"Gelede mask","a":"Gẹlẹdẹ headdress","d":"Yoruba headdress worn by men in the Gẹlẹdẹ masquerade honouring the 'Mothers'.","mk":"","y":"","s":W+"G%E1%BA%B9l%E1%BA%B9d%E1%BA%B9",
    "v":[V("Gelede headdress","","","rests on the head, veil hides the wearer's face")],
    "dt":"superstructure scene · painted wood · region (Ketu, Oyo)"},
   {"n":"Baule mask","a":"goli · kple kple","d":"Dance masks of the Baule of Côte d'Ivoire tied to named dances.","mk":"","y":"","s":W+"Baoul%C3%A9_people",
    "v":[V("Goli glin"),V("Kple kple"),V("Gbagba"),V("Bo nu amuin")],
    "dt":"dance · colour (red female, black male) · wood"}]},
 {"n":"African carved figure","a":"tribal figure · power figure · ancestor figure","d":"A freestanding carved figure from Africa made for ritual, ancestor or protective use.",
  "t":["reliquary guardian","power figure","twin figure","spirit-spouse figure","hunting statuette","ancestor figure","made-for-trade figure"],
  "s":W+"Traditional_African_masks",
  "x":[
   {"n":"Fang byeri figure","a":"bieri · mwan bian · reliquary guardian","d":"Guardian figure set on a box of ancestral bones among the Fang of Gabon, Equatorial Guinea and Cameroon.","mk":"","y":"","s":W+"Fang_people",
    "v":[V("Byeri figure on reliquary box","","","large head, prominent forehead, concave face; oiled with palm oil")],
    "dt":"style region · height · oil patina · wood · early cavities"},
   {"n":"Kongo nkisi nkondi","a":"nail figure · power figure","d":"Nail-studded power figure of the Kongo, driven with nails to seal oaths and settle disputes.","mk":"","y":"","s":W+"Nkondi",
    "v":[V("Nailed nkondi","","","nailed examples recorded from at least 1864"),V("Mirror-eyed nkondi","","","medicine pack behind a mirror")],
    "dt":"nails and blades · medicine pack · mirror · museum or field history"},
   {"n":"Yoruba ere ibeji","a":"ibeji · twin figure","d":"Wooden figure carved for a dead twin and cared for as a living child by the Yoruba.","mk":"","y":"","s":W+"Ibeji",
    "v":[V("Ere ibeji figure","","","dressed with cowries, beads, coins and paint")],
    "dt":"sex · coiffure · beads and camwood patina · carver's hand"},
   {"n":"Baule spirit-spouse figure","a":"blolo bla · blolo bian","d":"Figure of a person's spirit husband or wife among the Baule of Côte d'Ivoire.","mk":"","y":"","s":W+"Baoul%C3%A9_people",
    "v":[V("Blolo bla","","","spirit wife"),V("Blolo bian","","","spirit husband"),V("Bo usu","","","hunter's statuette")],
    "dt":"coiffure · scarification · polished surface · wood"},
   {"n":"Chokwe figure","a":"Chibinda Ilunga · ngombo figure","d":"Chokwe carved figures including the hero Chibinda Ilunga and ngombo divining figurines.","mk":"","y":"","s":W+"Chokwe_people",
    "v":[V("Chibinda Ilunga figure","","","hunter hero"),V("Ngombo divining figurine","","","used for illness and misfortune")],
    "dt":"headdress · wood · divination use"}]},
 {"n":"Oceanic carving","a":"Pacific carving · Oceanic art","d":"A carved ceremonial or personal object from the Pacific islands, Māori New Zealand or New Guinea.",
  "t":["pendant","memorial pole","ancestor figure","mask","canoe or house element","made-for-trade carving"],
  "s":W+"Hei-tiki",
  "x":[
   {"n":"Hei-tiki","a":"Māori greenstone pendant","d":"Māori neck pendant in pounamu, a family treasure (taonga).","mk":"","y":"","s":W+"Hei-tiki",
    "v":[V("Nephrite and shell hei-tiki","","18th century"),V("Pāua-eyed pendant","","1500–1850"),V("Tourist hei-tiki","","","jade, other stone or plastic")],
    "dt":"nephrite vs bowenite (tangiwai) · eyes (pāua, red wax) · age · taonga status"},
   {"n":"Asmat bisj pole","a":"mbis · bis pole","d":"Ancestor memorial pole carved from one mangrove tree by the Asmat of south-west New Guinea.","mk":"","y":"","s":W+"Bisj_Pole",
    "v":[V("Bisj pole","","","up to about 7.6 m (25 ft)")],
    "dt":"height · stacked figures · wing-like projection · mangrove wood"}]},
 {"n":"Pre-Columbian figure","a":"pre-Columbian ceramic figure · ancient American figurine","d":"A figure or effigy vessel made by an ancient Mesoamerican or Andean culture before European contact.",
  "t":["ceramic figurine","effigy vessel","jade or stone figure","tomb figure","portrait vessel","restored vs intact"],
  "s":W+"Pre-Columbian_art",
  "x":[
   {"n":"Olmec figurine","a":"Olmec baby-face figure","d":"Small ceramic or jade figure of the Olmec of the Mexican Gulf coast, c. 1200–400 BCE.","mk":"","y":"c. 1200–400 BCE","s":W+"Olmecs",
    "v":[V("Seated ceramic figure","","12th–9th century BC"),V("Jade face mask","","c. 900–300 BC")],
    "dt":"clay vs jade · size · fakes common · looting history"},
   {"n":"Colima dog","a":"Colima effigy · fattened dog","d":"Red-slipped hollow ceramic dog or human figure from the Colima shaft-tomb tradition of west Mexico.","mk":"","y":"c. 300 BCE–400 CE","s":W+"Western_Mexico_shaft_tomb_tradition",
    "v":[V("Plump dog figure","","","some wear human masks"),V("Human figure","","","mannered, less exuberant")],
    "dt":"burnished slip · restoration · thermoluminescence test"},
   {"n":"Moche portrait vessel","a":"huaco retrato","d":"Realistic stirrup-spout portrait vessel of the Moche of north Peru.","mk":"","y":"c. 100–800 CE","s":W+"Huaco_(pottery)",
    "v":[V("Moche portrait pot","","","Moche pottery c. 200 BC–600 AD per huaco article")],
    "dt":"portrait vs animal form · slip painting · restoration · museum parallels (Larco Museum)"}]}
]
T=lambda n,g,r,p,d,tech,mat,forms,ctr,auth,s:{"n":n,"g":g,"r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
trad=[
 T("Dan masks","African sculpture","Liberia, Côte d'Ivoire","","Masks embodying spirits tied to men's societies.","carved wood","wood, pigment, fibre",["Dan mask"],["Dan villages"],AUTH,W+"Dan_masks"),
 T("Gelede","African sculpture","Yorubaland, Nigeria and Benin","","Masked spectacle honouring women's spiritual power; on UNESCO's intangible heritage list.","carved painted headdress","wood, paint",["Gelede mask"],["Ketu","Oyo"],AUTH,W+"G%E1%BA%B9l%E1%BA%B9d%E1%BA%B9"),
 T("Fang reliquary tradition","African sculpture","Gabon, Equatorial Guinea, Cameroon","","Guardian figures over ancestral bone boxes.","carved wood, palm-oil patina","wood",["Fang byeri figure"],[],AUTH,W+"Fang_people"),
 T("Kongo nkisi","African sculpture","Congo region","19th–early 20th century","Ritual power figures charged by a nganga.","carved figure with medicine pack","wood, nails, mirror, medicines",["Kongo nkisi nkondi"],["Northern Kongo"],AUTH,W+"Nkondi"),
 T("Yoruba twin figures","African sculpture","Yorubaland","","Figures commemorating dead twins.","carved wood, dressed","wood, beads, cowries",["Yoruba ere ibeji"],[],AUTH,W+"Ibeji"),
 T("Māori pounamu carving","Oceanic carving","New Zealand","pre-contact to present","Carving of greenstone as taonga.","slow grinding and carving","nephrite, bowenite",["Hei-tiki"],[],"Age and provenance; tourist copies in other stone or plastic; claims of improperly obtained taonga",W+"Hei-tiki"),
 T("Asmat carving","Oceanic carving","South-west New Guinea, Indonesia","","Ancestor memorial poles and carved figures.","carved from one mangrove tree","mangrove wood",["Asmat bisj pole"],["Asmat villages"],AUTH,W+"Bisj_Pole"),
 T("Olmec","Pre-Columbian","Mexican Gulf coast","c. 1200–400 BCE","Earliest Mesoamerican civilisation; jade and ceramic figurines.","modelled clay, carved jade","clay, jade",["Olmec figurine"],[],"Fakes common; thermoluminescence; export law of Mexico",W+"Olmecs"),
 T("West Mexico shaft-tomb ceramics","Pre-Columbian","Colima, Jalisco, Nayarit","c. 300 BCE–400 CE","Tomb figures, notably Colima dogs.","hollow modelled, burnished red slip","clay",["Colima dog"],["Colima"],"Restoration and thermoluminescence; Mexican patrimony law",W+"Western_Mexico_shaft_tomb_tradition"),
 T("Moche pottery","Pre-Columbian","North coast of Peru","c. 100–800 CE","Portrait vessels and painted scenes.","mould-made and painted","clay slip",["Moche portrait vessel"],["Larco Museum, Lima"],"Restoration; Peruvian export law",W+"Huaco_(pottery)")]
notes="Old data empty. Four planned kinds built from retrieved Wikipedia pages. Left out: Dogon figures (page text not confirmed), Sepik carving (only dealer pages found), Māori and Asmat only as Oceanic examples. Authenticity/law notes use the UNESCO 1970 Convention page. No brands (makers anonymous)."
json.dump({"kinds":kinds,"brands":[],"traditions":trad,"notes":notes},open('work/F2/shelves/04_02.tmp','w'),ensure_ascii=False,indent=1)
import os;os.rename('work/F2/shelves/04_02.tmp','work/F2/shelves/04_02.json')
