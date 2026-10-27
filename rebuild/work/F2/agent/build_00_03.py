import json, os
W='https://en.wikipedia.org/wiki/'
PM=W+'Portrait_miniature'; EY='https://nelson-atkins.org/starr/contents/volume-1/Eye-Miniatures/'
PER=W+'Persian_miniature'; ST=W+'Shahnameh_of_Shah_Tahmasp'; RA=W+'Reza_Abbasi'; MU=W+'Mughal_painting'
RJ='https://www.gktoday.in/rajput-paintings/'; KG=W+'Kangra_painting'; DC=W+'Deccan_painting'
RG=W+'Reverse_glass_painting'; SW='https://www.piasa.fr/en/news/suwer-senegal-2023'; TH=W+'Thangka'; RB=W+'Andrei_Rublev'
def v(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Portrait miniature","a":"miniature · limning · painting in little","d":"A small painted portrait made as a work of its own, often on vellum, ivory, card or metal.",
  "t":["watercolour on vellum or card","watercolour on ivory","enamel on copper","oil on copper","in locket or case","in frame","jewellery-mounted"],
  "s":"https://www.1stdibs.com/buy/ivory-miniature-painting",
  "x":[
   {"n":"Elizabethan limning","a":"Tudor miniature","d":"An opaque watercolour miniature on vellum or card heightened with gold, often signed and with a Latin motto.","mk":"Nicholas Hilliard","y":"16th – early 17th century","s":PM,
    "v":[v("Margaret Roper","Hans Holbein the Younger","c. 1535–36","court miniature before Hilliard"),v("Treatise on the Art of Limning","Nicholas Hilliard","c. 1600"),v("Rounded modelling of faces","Isaac Oliver","c. 1560–1617","Hilliard's pupil"),v("Miniatures","Peter Oliver","1594–1647")],
    "dt":"vellum on playing card · oval or round · original case or locket"},
   {"n":"Enamel portrait miniature","a":"","d":"A miniature painted in vitreous enamel on copper and fired, popular especially in France.","mk":"Jean Petitot","y":"mid-17th century onward","s":PM,
    "v":[v("Enamels for Louis XIV","Jean Petitot","1607–1691"),v("Enamel copies","Henry Bone","1755–1834","leading British enamel painter")],
    "dt":"copper plate · counter-enamel · mount"},
   {"n":"Watercolour-on-ivory miniature","a":"Georgian miniature","d":"A translucent watercolour portrait on a thin ivory leaf, the standard miniature from about 1700 until photography.","mk":"","y":"c. 1700 – mid-19th century","s":PM,
    "v":[v("Miniatures","Richard Cosway","1742–1821","best work about 1799"),v("Miniatures","George Engleheart","1750–1829","about 4,900 miniatures"),v("Miniatures","John Smart","1741–1811"),v("Miniatures","Andrew Plimer","1763–1837"),v("Miniatures","Rosalba Carriera","1675–1757")],
    "dt":"ivory leaf (sale and export may be legally restricted) · case, locket or frame · hair work on reverse"},
   {"n":"Eye miniature","a":"lover's eye","d":"A miniature showing only one eye of a loved one, set in a ring, brooch, pin or clasp.","mk":"","y":"1785","s":EY,
    "v":[v("Prince of Wales's eye for Maria Fitzherbert","","1785","origin of the fashion"),v("Victorian revival","William Charles Ross","19th century")],
    "dt":"jewellery mount (ring, brooch, pin, clasp) · surrounding stones or pearls · mourning or love token"}]},
 {"n":"Persian and Indian miniature painting","a":"Persian miniature · Mughal miniature · Rajput painting · Pahari painting · Deccani painting","d":"A small, finely detailed painting on paper, made as a manuscript illustration or an album page, in Persian and Indian court traditions.",
  "t":["manuscript folio","album page (muraqqa)","with borders and calligraphy","single leaf","set or series"],
  "s":PER,
  "x":[
   {"n":"Safavid manuscript miniature","a":"Tabriz school","d":"A court book illustration, often for the Shahnameh, painted in the royal workshop at Tabriz.","mk":"","y":"1520s–1530s","s":ST,
    "v":[v("Shahnameh of Shah Tahmasp","Sultan Muhammad","1520s – mid-1530s","258 miniatures; dispersed in the 1970s; with Mir Musavvir and Aqa Mirak")],
    "dt":"folio with text · detached leaf · provenance from a dispersed manuscript"},
   {"n":"Isfahan album miniature","a":"Isfahan school","d":"A single-page figure study of one or two figures for a collector's album, often signed and dated.","mk":"Reza Abbasi","y":"c. 1590 – 1635","s":RA,
    "v":[v("Reclining Woman","Reza Abbasi","1595"),v("Youth Reading","Reza Abbasi","1625–26"),v("Two Lovers","Reza Abbasi","1630")],
    "dt":"drawing or full colour · album borders · signature"},
   {"n":"Mughal miniature","a":"Mughal painting","d":"Indian court painting of the Mughal emperors, grown from Persian models, for manuscripts and albums.","mk":"","y":"16th–19th century","s":MU,
    "v":[v("Hamzanama","","1562–1577","about 1,400 large cotton folios for Akbar"),v("Baburnama","","1589"),v("Akbar-period painting","Basawan","c. 1580–1600"),v("Animals and plants","Ustad Mansur","c. 1590–1624"),v("Portraits","Bichitr","c. 1610–1660"),v("Company style","","later","for British clients")],
    "dt":"reign (Akbar, Jahangir, Shah Jahan) · manuscript folio or album page · borders"},
   {"n":"Rajasthani miniature","a":"Rajput painting (Rajasthan)","d":"Miniature painting of the Hindu Rajput courts of Rajasthan, each court with its own style.","mk":"","y":"17th–19th century","s":RJ,
    "v":[v("Mewar (Udaipur)","","peak 1628–1652","under Jagat Singh"),v("Bani Thani","Nihal Chand","","Kishangarh"),v("Bundi and Kota","","",""),v("Jodhpur (Marwar)","","",""),v("Bikaner","","","strongest Mughal influence")],
    "dt":"school and court · subject (Ragamala, Krishna, court scenes) · single leaf or series"},
   {"n":"Pahari miniature","a":"Pahari painting · Kangra painting","d":"Miniature painting of the Himalayan hill kingdoms, known for Radha–Krishna themes in naturalistic landscape.","mk":"","y":"17th–19th century","s":KG,
    "v":[v("Basohli","","to mid-18th century","earlier style"),v("Guler","Nainsukh","1710–1778","with his brother Manaku"),v("Kangra","","peak 1776–1824","under Sansar Chand")],
    "dt":"school · series (Gita Govinda, Bhagavata Purana, Baramasa) · leaf condition"},
   {"n":"Deccani miniature","a":"Deccan painting","d":"Miniature painting of the Deccan sultanates, with rich colour and suave figures.","mk":"","y":"late 16th – mid-17th century; revival mid-18th century","s":DC,
    "v":[v("Tarif-i Husain Shahi","","c. 1565–69","Ahmadnagar"),v("Nujum al-Ulum","","1570–71","Bijapur"),v("Hindola Raga","","c. 1585","Ragamala set"),v("Portrait of Ibrahim Adil Shah II","","c. 1590","Bijapur")],
    "dt":"court (Bijapur, Golconda, Ahmadnagar, Hyderabad) · subject"}]},
 {"n":"Reverse glass painting","a":"Hinterglasmalerei · verre églomisé · souwère · suwer","d":"A picture painted on the back of a glass sheet in reverse order and viewed through the glass.",
  "t":["religious","portrait","genre scene","with metal leaf","framed panel","clock face"],
  "s":RG,
  "x":[
   {"n":"Central European Hinterglasmalerei","a":"glass icon","d":"Folk and devotional pictures painted behind glass in Austria, Bavaria, Bohemia, Moravia and Slovakia.","mk":"","y":"mid-18th – 19th century","s":RG,
    "v":[v("Folk glass pictures","","19th century",""),v("Modern reverse glass paintings","Wassily Kandinsky","","more than 70 works"),v("Modern reverse glass paintings","Gabriele Münter","","")],
    "dt":"region · religious or secular · frame"},
   {"n":"Verre églomisé","a":"","d":"Glass reverse-decorated with paint and metal leaf, named after the French framer Jean-Baptiste Glomy.","mk":"","y":"18th century","s":RG,"v":[],"dt":"gilding · use (frame, mirror, panel)"},
   {"n":"Chinese reverse glass painting","a":"Chinese export reverse glass painting","d":"Reverse painting on glass taken up in China after Jesuit missionaries brought the technique, made for export and home use.","mk":"","y":"18th–19th century","s":RG,"v":[],"dt":"subject (figures, landscapes) · mirror or plain glass · frame"},
   {"n":"Senegalese souwère","a":"suwer · fixé sous verre","d":"Senegalese popular painting under glass of religious figures, portraits and street life.","mk":"","y":"late 19th century onward","s":SW,
    "v":[v("Souwère","Meïssa Gaye","1892–1982"),v("Souwère","Gora M'Bengue","1931–1988"),v("Souwère","Babacar Lô",""),v("Souwère","Mor Gueye","")],
    "dt":"subject (religious, Drianké, musicians) · glass size · signature"},
   {"n":"Iranian reverse glass painting","a":"","d":"Persian painting behind glass, flourishing in the Qajar period.","mk":"","y":"c. 1797 onward","s":RG,
    "v":[v("Early surviving examples","","c. 1797–1834","reign of Fath Ali Shah")],"dt":"subject · frame"}]}]
def B(n,c,kf,d,s,sig): return {"n":n,"c":c,"f":"","seg":"Artisan & independent","kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 B("Nicholas Hilliard","United Kingdom","limning","English miniaturist (c. 1537–1619), author of a treatise on limning.",PM,["Elizabethan limning"]),
 B("Jean Petitot","France","enamel miniatures","Enamel miniaturist (1607–1691) to Louis XIV.",PM,["Enamel portrait miniature"]),
 B("Richard Cosway","United Kingdom","miniatures","Most famous British miniaturist of the 18th century (1742–1821).",PM,["Watercolour-on-ivory miniature"]),
 B("George Engleheart","United Kingdom","miniatures","British miniaturist (1750–1829) of about 4,900 miniatures.",PM,["Watercolour-on-ivory miniature"]),
 B("Reza Abbasi","Iran","album miniatures","Leading Isfahan miniaturist (c. 1565–1635) for Shah Abbas I.",RA,["Isfahan album miniature"]),
 B("Sultan Muhammad","Iran","Safavid miniatures","Tabriz painter of the Shahnameh of Shah Tahmasp.",ST,["Safavid manuscript miniature"]),
 B("Nainsukh","India","Pahari painting","Pahari painter (1710–1778) of the Guler family workshop.",KG,["Pahari miniature"]),
 B("Nihal Chand","India","Kishangarh painting","Kishangarh court painter of Bani Thani.",RJ,["Rajasthani miniature"]),
 B("Gora M'Bengue","Senegal","souwère","Senegalese glass painter (1931–1988).",SW,["Senegalese souwère"]),
]
def T(n,g,r,p,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":g,"r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
P="Painting"
trads=[
 T("Persian miniature painting",P,"Iran and Persianate courts","13th century onward; peak 15th–16th century","Small paintings on paper for manuscripts and albums.","fine brushwork in opaque colour, gold","paper, mineral pigments, gold",["Persian and Indian miniature painting","Safavid manuscript miniature","Isfahan album miniature"],["Tabriz","Herat","Shiraz","Isfahan","Kamāl ud-Dīn Behzād","Sultan Muhammad","Reza Abbasi"],"Leaves from dispersed manuscripts circulate; check text, borders and provenance; later and modern work continues the style.",PER),
 T("Mughal painting",P,"North India","16th–19th century","Court painting of the Mughal emperors, fusing Persian and Indian traditions.","opaque watercolour, fine detail, portraiture","paper, cotton (Hamzanama), mineral pigments, gold",["Mughal miniature"],["Akbar's imperial atelier","Basawan","Ustad Mansur","Bichitr","Abu'l Hasan"],"Later provincial and Company-style works and copies are common; reign style helps dating.",MU),
 T("Rajasthani painting",P,"Rajasthan, India","17th–19th century","Rajput court painting of Rajasthan, classified by Coomaraswamy in 1916.","opaque watercolour on paper","paper, mineral pigments",["Rajasthani miniature"],["Mewar","Bundi","Kota","Kishangarh","Jaipur","Jodhpur","Bikaner","Nathdwara"],"School style and court inscriptions guide attribution.",RJ),
 T("Pahari painting",P,"Himalayan hill states, India","17th–19th century","Hill-state miniature painting, chiefly Basohli, Guler and Kangra.","fine line, cool colour, naturalistic landscape","paper, mineral pigments",["Pahari miniature"],["Basohli","Guler","Kangra","Nainsukh","Manaku"],"Kangra became a name for the whole school; attribution by family workshop.",KG),
 T("Deccani painting",P,"Deccan, India","late 16th – mid-17th century; 18th-century revival","Miniature painting of the Deccan sultanates.","rich colour, tropical setting","paper, pigments, gold",["Deccani miniature"],["Bijapur","Golconda","Ahmadnagar","Hyderabad"],"Few painters' names are known; court style guides attribution.",DC),
 T("Senegalese souwère",P,"Senegal","late 19th century onward","Popular painting under glass, from religious images to scenes of daily life.","reverse painting on glass","glass, paint",["Reverse glass painting","Senegalese souwère"],["Dakar","Saint-Louis","Gorée","Gora M'Bengue","Meïssa Gaye"],"Signed works by named painters are sought after.",SW),
 T("Orthodox icon painting","Faith traditions","Byzantium, Russia and the Orthodox world","from Byzantium; Russia from 988","Devotional panel painting of the Orthodox Church; icons themselves sit in F4 as devotional panel paintings.","painting on panel in a fixed iconographic canon","wood panel, pigments",["F4: Devotional panel painting"],["Theophanes the Greek","Andrei Rublev"],"Rublev's Trinity (c. 1410) is the only work fully authenticated as his; most icons are unsigned.",RB),
 T("Thangka painting","Faith traditions","Tibet, Nepal, Bhutan, Mongolia, Himalaya","about the 11th century onward","Tibetan Buddhist painted or textile scroll images for teaching and meditation; thangkas themselves sit in F4 as devotional scroll paintings.","distemper (pigment in animal glue) on cotton; appliqué and embroidery","cotton, silk, mineral and organic pigments, gold",["F4: Devotional scroll painting"],["Nepal (paubha)","monastic orders' styles"],"Rarely signed; old pieces often have a mantra or inscription on the back; poster reproductions are common.",TH),
]
out={"kinds":kinds,"brands":brands,"traditions":trads,
 "notes":"Old kind Portrait miniature kept; new kinds Persian and Indian miniature painting and Reverse glass painting added. Icons and thangka are not kinds here (they stay in F4); tradition entries link to F4. Ivory: watercolour-on-ivory miniatures may be subject to sale and export restrictions; the record flags this in dt only (no legal source retrieved). No Getty ULAN pages retrieved; artist entries cite fetched Wikipedia/museum pages; founding year blank. Sahibdin and Behzad dates not given on fetched pages, so left out. Chinese export reverse glass has no versions (OAPEN book page timed out; Art UK eye-miniature page 403). Qajar painting appears only as a reverse-glass archetype."}
p='work/F2/shelves/00_03.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
