import json, os
W='https://en.wikipedia.org/wiki/'
SG='https://www.sothebys.com/en/articles/the-complete-collectors-guide-to-prints'
ME=W+'Melencolia_I'; HG=W+'Hundred_Guilder_Print'; CA=W+'Carceri_d%27invenzione'; RP=W+'A_Rake%27s_Progress'
WH='https://collections.vam.ac.uk/item/O636207/chelsea-bridge-and-church-print-whistler/'
DW='https://www.metmuseum.org/art/collection/search/361851'
GC='https://www.gla.ac.uk/myglasgow/library/files/special/exhibns/hispanica/art.html'
TC='https://kemperartmuseum.wustl.edu/research/artwork-essays/van-rijn-rembrandt-the-three-crosses-166061'
VG='https://www.britishmuseum.org/collection/object/P_1902-1011-2384'
VR='https://www.metmuseum.org/ja/art/collection/search/360443'
kinds=[
 {"n":"Etching","a":"eau-forte · acquaforte","d":"A print from a metal plate whose lines were drawn through a wax ground and bitten with acid.",
  "t":["lifetime impression","posthumous impression","restrike","early state","late state","on laid paper","on Japan paper","with drypoint","with engraving"],
  "s":SG,
  "x":[
   {"n":"Rembrandt etching","a":"","d":"An etching by Rembrandt, often reworked with drypoint through several states and judged by impression quality.","mk":"Rembrandt","y":"17th century","s":HG,
    "v":[{"n":"Hundred Guilder Print, 1st state","mk":"Rembrandt","y":"c. 1647–49","d":"very rare; etching with drypoint, 278 × 388 mm"},
         {"n":"Hundred Guilder Print, 2nd state","mk":"Rembrandt","y":"c. 1647–49","d":"small additions of shading"},
         {"n":"Baillie reworked edition","mk":"William Baillie","y":"c. 1775","d":"100 impressions from the reworked plate, which was then cut into four"}],
    "dt":"state · lifetime or later impression · paper and watermark · plate tone and burr · margins"},
   {"n":"Piranesi Carceri","a":"Carceri d'invenzione · Imaginary Prisons","d":"Piranesi's series of etched fantasy prison interiors, issued in two editions.","mk":"Giovanni Battista Piranesi","y":"1750; reworked 1761","s":CA,
    "v":[{"n":"First edition","mk":"Giovanni Battista Piranesi","y":"1750","d":"14 untitled, unnumbered plates; title plate names publisher Giovanni Bouchard"},
         {"n":"Second edition","mk":"Giovanni Battista Piranesi","y":"1761","d":"16 plates reworked and numbered I–XVI; II and V new"},
         {"n":"Later impressions","mk":"Giovanni Battista Piranesi","y":"1770s","d":"individual plates printed with ink experiments"}],
    "dt":"edition and state · plate number · paper · margins"},
   {"n":"Piranesi Vedute di Roma","a":"Views of Rome","d":"Piranesi's 135 etched views of classical and Baroque Rome, issued plate by plate over three decades.","mk":"Giovanni Battista Piranesi","y":"to 1778","s":VR,
    "v":[{"n":"View along the Via del Corso of the Palazzo dell'Accademia","mk":"Giovanni Battista Piranesi","y":"1750–78","d":"Met"}],
    "dt":"plate subject · Roman or later Paris printing · state · paper and watermark"},
   {"n":"Goya Disasters of War","a":"Los Desastres de la Guerra","d":"Goya's 80 prints of the atrocities of the Peninsular War, published only after his death.","mk":"Francisco Goya","y":"from 1810; first published 1863","s":DW,
    "v":[{"n":"First edition","mk":"Real Academia de Bellas Artes de San Fernando","y":"1863","d":"first of the posthumous editions; 80 plates"},
         {"n":"Plate 26 'No se puede mirar'","mk":"Francisco Goya","y":"1810","d":"published 1863; Met"}],
    "dt":"edition · plate number · paper · trial proof or edition impression"},
   {"n":"Whistler Thames Set","a":"Sixteen Etchings of Scenes on the Thames","d":"Whistler's set of sixteen river etchings, published together in 1871.","mk":"James McNeill Whistler","y":"published 1871","s":WH,
    "v":[{"n":"Published set","mk":"Ellis and Green","y":"1871","d":"editions of one hundred; sixteen plates"},
         {"n":"Chelsea Bridge and Church","mk":"James McNeill Whistler","y":"c. 1865","d":"V&A"}],
    "dt":"plate · early proof or 1871 edition · paper"}]},
 {"n":"Line engraving","a":"engraving · burin engraving · copperplate engraving","d":"A print from a metal plate whose lines were cut with a burin.",
  "t":["copper","steel","proof before letters","lettered impression","early state","later restrike","hand-coloured"],
  "s":SG,
  "x":[
   {"n":"Dürer master engraving","a":"Meisterstiche","d":"Dürer's three large master engravings of 1513–14, the benchmark of Renaissance line engraving.","mk":"Albrecht Dürer","y":"1513–1514","s":ME,
    "v":[{"n":"Knight, Death and the Devil","mk":"Albrecht Dürer","y":"1513","d":""},
         {"n":"Melencolia I, 1st state","mk":"Albrecht Dürer","y":"1514","d":"nine in the magic square reversed; rare"},
         {"n":"Melencolia I, 2nd state","mk":"Albrecht Dürer","y":"1514","d":"corrected nine; more common; 24 × 18.8 cm"},
         {"n":"St. Jerome in His Study","mk":"Albrecht Dürer","y":"1514","d":""}],
    "dt":"state · impression quality · watermark · margins · provenance"},
   {"n":"Hogarth modern moral series","a":"Hogarth progress prints","d":"Hogarth's narrative print series of London life, engraved from his own paintings and sold by subscription.","mk":"William Hogarth","y":"1730s–1740s","s":RP,
    "v":[{"n":"A Rake's Progress","mk":"William Hogarth","y":"1735","d":"8 plates, published 25 June 1735 under the Engravers' Copyright Act"},
         {"n":"A Harlot's Progress","mk":"William Hogarth","y":"","d":"paintings 1731"},
         {"n":"Marriage A-la-Mode","mk":"William Hogarth","y":"1745","d":"six scenes"}],
    "dt":"plate · lifetime or later impression · state · paper"}]},
 {"n":"Drypoint","a":"","d":"A print from lines scratched straight into the plate with a needle, without acid; the raised burr gives a soft, velvety line.",
  "t":["rich burr","worn impression","early state","late state","with etching"],
  "s":SG,
  "x":[
   {"n":"Rembrandt drypoint","a":"","d":"A drypoint by Rembrandt, reworked through states, with the burr giving deep, rich blacks in early impressions.","mk":"Rembrandt","y":"1650s","s":TC,
    "v":[{"n":"The Three Crosses, early states","mk":"Rembrandt","y":"1653","d":""},
         {"n":"The Three Crosses, 4th state","mk":"Rembrandt","y":"c. 1660–61","d":"plate heavily reworked; Kemper Art Museum"}],
    "dt":"state · burr · paper (Japan, European) · impression quality"}]},
 {"n":"Aquatint","a":"","d":"A print whose tone comes from acid biting through a porous ground of resin dust.",
  "t":["with etching","sugar-lift","colour aquatint","first edition","later edition"],
  "s":SG,
  "x":[
   {"n":"Goya Los Caprichos","a":"Caprichos","d":"Goya's 80 satirical etchings with aquatint, published by the artist in Madrid in 1799.","mk":"Francisco Goya","y":"1799","s":GC,
    "v":[{"n":"First edition","mk":"Francisco Goya","y":"1799","d":"self-portrait plus 79 satires; plate 43 'El sueño de la razon produce monstruos'"},
         {"n":"Plates and unsold sets offered to Charles IV","mk":"Francisco Goya","y":"1803","d":"240 unsold first-edition sets"}],
    "dt":"edition · plate number · paper · aquatint wear"}]},
 {"n":"Mezzotint","a":"","d":"A print from a plate roughened all over with a rocker and then burnished from dark to light.",
  "t":["portrait","after a painting","proof before letters","lettered impression","colour mezzotint"],
  "s":SG,
  "x":[
   {"n":"British portrait mezzotint","a":"English mezzotint","d":"A mezzotint reproducing a society portrait, especially after Reynolds, valued most as proofs before letters.","mk":"Valentine Green","y":"18th century","s":VG,
    "v":[{"n":"Ann, Viscountess Townshend (after Reynolds)","mk":"Valentine Green","y":"1780","d":"proof before letters; British Museum 1902,1011.2384"}],
    "dt":"sitter · after which painter · state (proof before letters, lettered) · margins"}]}]
def B(n,c,seg,kf,d,s,sig): return {"n":n,"c":c,"f":"","seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
A="Artisan & independent"
brands=[
 B("Albrecht Dürer","Germany",A,"engraving","German Renaissance painter and printmaker whose master engravings set the standard for the medium.",ME,["Dürer master engraving"]),
 B("Rembrandt","Netherlands",A,"etching, drypoint","Dutch painter and printmaker, the leading etcher of the 17th century.",HG,["Rembrandt etching","Rembrandt drypoint"]),
 B("Giovanni Battista Piranesi","Italy",A,"etched views","Venetian-born etcher and architect of Rome's views and imaginary prisons.",CA,["Piranesi Carceri","Piranesi Vedute di Roma"]),
 B("Francisco Goya","Spain",A,"etching and aquatint","Spanish painter and printmaker of Los Caprichos and the Disasters of War.",GC,["Goya Los Caprichos","Goya Disasters of War"]),
 B("James McNeill Whistler","United States",A,"etching","American-born painter and etcher working in London.",WH,["Whistler Thames Set"]),
 B("William Hogarth","United Kingdom",A,"satirical series","English painter and engraver of modern moral subjects.",RP,["Hogarth modern moral series"]),
 B("Valentine Green","United Kingdom",A,"mezzotint","English mezzotint engraver of portraits after Reynolds and his contemporaries.",VG,["British portrait mezzotint"]),
 B("Real Academia de Bellas Artes de San Fernando","Spain","Institution & issuer","print editions","Spanish Royal Academy that published the first edition of Goya's Disasters of War in 1863.",DW,[]),
 B("Ellis and Green","United Kingdom","Specialist","print publishing","Covent Garden publishers of Whistler's Thames Set in 1871.",WH,[]),
]
out={"kinds":kinds,"brands":brands,"traditions":[],
 "notes":"All five old kinds kept with their old Sotheby's source. Archetypes are landmark series with editions/states as versions. Disasters of War placed under Etching because the fetched Met record did not state the aquatint; Los Caprichos under Aquatint. Later Caprichos and Disasters editions (Calcografía reprints to 1937) not confirmed on a fetched page, so left out; Calcografía Nacional and Crown Point Press not added (unsourced). Valentine Green mezzotint after Reynolds as the mezzotint archetype. Artist founding year blank."}
p='work/F2/shelves/02_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
