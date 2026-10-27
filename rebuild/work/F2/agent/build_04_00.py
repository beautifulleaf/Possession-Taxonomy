import json, os
W='https://en.wikipedia.org/wiki/'
TH=W+'The_Thinker'; LD=W+'Little_Dancer_of_Fourteen_Years'; CH=W+'Dem%C3%A9tre_Chiparus'
BA='https://collections.vam.ac.uk/item/O73229/senegalese-elephant-statuette-barbedienne-ferdinand/'
TG=W+'Tanagra_figurine'; PR='https://mus-col.com/en/the-authors/31967'
BE='https://www.smb.museum/en/museums-institutions/ethnologisches-museum/about-us/whats-new/detail/first-restitution-of-benin-bronzes-from-the-ethnologisches-museum-commemorative-head-and-relief-plaque/'
BC='https://collections.vam.ac.uk/context/organisation/A10476/brucciani-co.'
WX='https://collections.vam.ac.uk/item/O166643/isaac-gosset-junior-relief-unknown'
ME='https://www.langmann.com/artists/pierre-jules-mene'; BN='https://www.vam.ac.uk/articles/bernini-and-baroque'
def V(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Bronze sculpture","a":"bronze","d":"Cast copper-tin alloy, usually patinated.",
  "t":["lost-wax cast","sand cast","lifetime cast","posthumous cast","numbered edition","reduction","foundry mark","patina colour","cold-painted","gilt bronze","with ivory (chryselephantine)","marble or onyx base"],
  "s":"https://www.singulart.com/en/sculpture",
  "x":[
   {"n":"Rodin – The Thinker","a":"Le Penseur","d":"Rodin's seated figure conceived for The Gates of Hell, cast in many sizes and editions.","mk":"Auguste Rodin","y":"1880","s":TH,
    "v":[V("First bronze (small)","Auguste Rodin","1884","National Gallery of Victoria, Melbourne"),
         V("Monumental bronze (enlarged 1902)","Auguste Rodin","1904","about 181–185 cm; placed before the Panthéon, Musée Rodin since 1922"),
         V("Monumental cast","Rudier","c. 1928","offered at Christie's Paris 2022"),
         V("Numbered cast, edition of 12","Auguste Rodin","","No. 10, Cantor Center, Stanford"),
         V("Plaster and study-size versions","Auguste Rodin","from c. 1881","")],
    "dt":"size (study, 72 cm, monumental) · lifetime or posthumous · foundry · cast number · patina"},
   {"n":"Degas – Little Dancer Aged Fourteen","a":"Little Dancer of Fourteen Years","d":"Degas's wax dancer with real tutu and hair, cast in bronze by his heirs after his death.","mk":"Edgar Degas","y":"1878–1881 (wax)","s":LD,
    "v":[V("Hébrard bronze","Hébrard","1920–1936","at least 28 in museums; one sold £13.26m at Sotheby's 2009"),
         V("Later 'Hébrard' casts","Valsuani","to mid-1970s"),
         V("Edition from the pre-1903 plaster","Valsuani","from 1997","Airaindor-Valsuani; first-version pose")],
    "dt":"foundry · cast mark and letter · fabric tutu and ribbon · patina"},
   {"n":"Barye animalier bronze","a":"","d":"An animal bronze from the models of Barye, initiator of the French animalier school, often cast posthumously by Barbedienne.","mk":"Antoine-Louis Barye","y":"1830s–1875 (models)","s":BA,
    "v":[V("Senegalese Elephant","Barbedienne","c. 1882","modelled c. 1855–65; signature cast through, gilt 'FB' seal")],
    "dt":"lifetime or posthumous cast · Barbedienne 'FB' seal · crispness of detail · patina"},
   {"n":"Mêne animalier bronze","a":"","d":"A small naturalistic animal or hunting bronze by Mêne, issued in many editions from his own foundry.","mk":"Pierre-Jules Mêne","y":"1838 onward","s":ME,
    "v":[V("L'Accolade","Pierre-Jules Mêne","1852–1853","wax at the 1852 Salon, bronze 1853, shown 1855 Exposition Universelle")],
    "dt":"model · own-foundry or later Cain cast · size · patina"},
   {"n":"Chiparus chryselephantine figure","a":"bronze and ivory dancer","d":"An Art Deco dancer in cold-painted bronze with carved ivory face and hands, issued in small foundry editions.","mk":"Demétre Chiparus","y":"1914–1933","s":CH,
    "v":[V("Danseuse au cerceau (Ring Dancer)","Etling","1928"),V("The Russian Dancers","Demétre Chiparus","","Nijinsky and Ida Rubinstein in Schéhérazade"),
         V("Javelin Thrower","Demétre Chiparus","1923"),V("Ta-Keo","Goldscheider","1928")],
    "dt":"foundry (Etling, Les Neveux de J. Lehmann) · ivory or later resin · cold paint · marble base · reproductions"},
   {"n":"Preiss chryselephantine figure","a":"PK figure","d":"An Art Deco cabinet figure of carved ivory and painted bronze on an onyx or slate base, made by Preiss & Kassler in Berlin.","mk":"Ferdinand Preiss","y":"1906–1943","s":PR,
    "v":[V("Bat Girl","Ferdinand Preiss",""),V("Fencer","Ferdinand Preiss",""),V("Girl with a Fishing Rod","Ferdinand Preiss",""),
         V("Dancer with a Tambourine","Ferdinand Preiss",""),V("Peter Pan","Ferdinand Preiss",""),V("Early bronze moulds","Gladenbeck","","later cast in-house")],
    "dt":"model · 'F. Preiss' signature · onyx and slate base · ivory condition"},
   {"n":"Benin commemorative head","a":"Benin Bronzes","d":"A cast brass head made by the Benin brass-casters' guild for a royal ancestral altar; many were looted in 1897 and are subject to restitution.","mk":"","y":"16th–19th century","s":BE,
    "v":[V("Commemorative head of a king","","18th century","returned to Nigeria by Berlin, 2022"),V("Relief plaque, oba with four attendants","","16th century","lost-wax cast; palace pillar plaque")],
    "dt":"period · provenance (1897 looting; legal title) · later tourist casts"}]},
 {"n":"Terracotta sculpture","a":"terracotta · fired clay","d":"Modelled or moulded clay fired without a glaze.",
  "t":["bozzetto (sketch model)","modello (finished model)","mould-made","painted","glazed or unglazed","antique or later"],
  "s":"https://www.singulart.com/en/sculpture",
  "x":[
   {"n":"Bernini bozzetto","a":"terracotta sketch model","d":"A preliminary terracotta model for a marble, with the sculptor's tool marks and fingerprints, prized by collectors since the 16th century.","mk":"Gian Lorenzo Bernini","y":"17th century","s":BN,
    "v":[V("Pope Alexander VII (tomb model)","Gian Lorenzo Bernini","c. 1669–1670","V&A"),V("The Blessed Ludovica Albertoni","Gian Lorenzo Bernini","1672","V&A; back fully modelled")],
    "dt":"attribution (master or workshop) · tool marks · condition"},
   {"n":"Tanagra figurine","a":"","d":"A mould-cast Greek terracotta figure, usually a draped woman, slipped white and painted after firing.","mk":"","y":"later 4th century BC onward","s":TG,
    "v":[V("Tanagra (Boeotia) figurine","","Hellenistic","excavated 1870s"),V("Myrina, Alexandria, Tarentum or Centuripe figurine","","Hellenistic"),
         V("19th-century forgery","","late 19th century","about 20% of Berlin's holdings found fake")],
    "dt":"height 10–20 cm · paint remains · provenance and export · authenticity (thermoluminescence)"}]},
 {"n":"Plaster sculpture","a":"plaster cast","d":"Cast or modelled plaster.",
  "t":["cast after the antique","sculptor's working plaster","patinated plaster","painted plaster","relief","bust"],
  "s":"https://www.singulart.com/en/sculpture",
  "x":[
   {"n":"Brucciani plaster cast","a":"","d":"A plaster reproduction of a famous sculpture from the London cast-makers linked with the British Museum and South Kensington (V&A).","mk":"D. Brucciani & Co.","y":"19th–early 20th century","s":BC,
    "v":[V("Tobias and the Angel, after Della Robbia","D. Brucciani & Co.",""),V("Fig Leaf for David","D. Brucciani & Co.","c. 1857"),V("Pictish Cross","D. Brucciani & Co.","c. 1894"),V("Casts for schools (trade catalogue)","D. Brucciani & Co.","1906?")],
    "dt":"subject · stamp · size · paint or patina"}]},
 {"n":"Wax sculpture","a":"wax","d":"Modelled or cast wax.",
  "t":["portrait relief","coloured (polychrome) wax","sculptor's model","anatomical wax","under glass or in frame"],
  "s":"https://www.artsper.com/en-gb/contemporary-artworks/sculpture/wax",
  "x":[
   {"n":"Wax portrait relief","a":"","d":"A small low-relief portrait in coloured wax, popular in 18th- and 19th-century Britain and Germany as a portable likeness.","mk":"","y":"18th–19th century","s":WX,
    "v":[V("Isaac Gosset, Junior","","late 18th or early 19th century","English; V&A Schreiber Bequest")],
    "dt":"sitter · frame and glass · colour · condition"},
   {"n":"Sculptor's wax model","a":"","d":"An original sculpture in wax that later served as the model for bronze casts.","mk":"Edgar Degas","y":"1878–1881","s":LD,
    "v":[V("Little Dancer Aged Fourteen, wax","Edgar Degas","1878–1881","shown 1881; National Gallery of Art"),V("L'Accolade, wax","Pierre-Jules Mêne","1852","shown at the Salon")],
    "dt":"armature · added materials · condition"}]}]
P="Artisan & independent"; H="Heritage manufactory"
def B(n,c,f,seg,kf,d,s,sig): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 B("Auguste Rodin","France","",P,"bronze sculpture","French sculptor of The Thinker and The Gates of Hell.",TH,["Rodin – The Thinker"]),
 B("Rudier","France","",H,"art foundry","Paris foundry founded by Alexis Rudier, maker of Rodin bronzes.",TH,[]),
 B("Edgar Degas","France","",P,"dancers","French Impressionist whose wax sculptures were cast in bronze after his death.",LD,["Degas – Little Dancer Aged Fourteen","Sculptor's wax model"]),
 B("Hébrard","France","",H,"art foundry","Paris foundry that cast Degas's bronzes from 1920 to 1936.",LD,[]),
 B("Valsuani","France","",H,"art foundry","Paris foundry that continued Degas casts and from 1997 issued the Little Dancer from the early plaster.",LD,[]),
 B("Antoine-Louis Barye","France","",P,"animalier bronzes","French animal sculptor (1796–1875), initiator of the animalier school.",BA,["Barye animalier bronze"]),
 B("Barbedienne","France","1838",H,"bronze editions","Paris foundry of Ferdinand Barbedienne, which bought Barye's models in 1875.",BA,[]),
 B("Pierre-Jules Mêne","France","1838",P,"animalier bronzes","French animalier sculptor who cast his own editions from 1838.",ME,["Mêne animalier bronze"]),
 B("Demétre Chiparus","France","",P,"chryselephantine dancers","Romanian-French Art Deco sculptor of bronze-and-ivory dancers.",CH,["Chiparus chryselephantine figure"]),
 B("Etling","France","",H,"Art Deco bronzes","Paris foundry Edmond Etling et Cie, Chiparus's main editor.",CH,[]),
 B("Les Neveux de J. Lehmann","France","",H,"Art Deco bronzes","Paris foundry, Chiparus's second editor.",CH,[]),
 B("Goldscheider","Austria","1885",H,"figures","Vienna manufactory that produced Chiparus's Ta-Keo.",CH,[]),
 B("Ferdinand Preiss","Germany","1906",P,"chryselephantine figures","Berlin ivory carver and co-founder of Preiss & Kassler (PK).",PR,["Preiss chryselephantine figure"]),
 B("Gladenbeck","Germany","",H,"art foundry","Berlin foundry that made Preiss's early bronze moulds.",PR,[]),
 B("Gian Lorenzo Bernini","Italy","",P,"Baroque sculpture","Roman Baroque sculptor whose terracotta bozzetti were collected early.",BN,["Bernini bozzetto"]),
 B("D. Brucciani & Co.","United Kingdom","",H,"plaster casts","London plaster-cast makers linked with the British Museum and the V&A.",BC,["Brucciani plaster cast"]),
]
trads=[
 {"n":"Benin brass casting","g":"Metal & blades","r":"Kingdom of Benin (Edo State, Nigeria)","p":"16th century to present",
  "d":"Lost-wax brass heads, plaques and figures made by a royal guild for the oba's palace and ancestral altars.",
  "tech":"lost-wax casting","mat":"brass, ivory",
  "forms":["Benin commemorative head","relief plaque"],
  "ctr":["Igun Eronmwon (brass founders' guild), Benin City"],
  "auth":"pieces looted in 1897 carry documented provenance and are subject to restitution claims; later casts for sale are common","s":BE},
 {"n":"French animalier bronze","g":"Metal & blades","r":"France (Paris)","p":"c. 1830–1900",
  "d":"Naturalistic small bronzes of animals and hunting scenes, issued in editions for middle-class interiors.",
  "tech":"sand and lost-wax casting, mechanical reduction, patination","mat":"bronze",
  "forms":["Barye animalier bronze","Mêne animalier bronze"],
  "ctr":["Antoine-Louis Barye","Pierre-Jules Mêne","Barbedienne foundry"],
  "auth":"cast-through signature and foundry seal; lifetime casts are crisper than later ones from worn moulds","s":BA}]
out={"kinds":kinds,"brands":brands,"traditions":trads,
 "notes":"Four old kinds kept with old sources. Giacometti not added (no page fetched this round). Coubertin foundry not named on any fetched page, so Rodin versions cite Rudier only. Benin head has a cultural-property note; maker-free (guild). Goldscheider register entry founding year from knowledge, source is Chiparus wiki."}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/04_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
