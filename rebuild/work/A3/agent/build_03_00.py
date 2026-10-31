import json, os
W='https://en.wikipedia.org/wiki/'
LOVE=W+'Love_bracelet_(Cartier)'; CIP=W+'Aldo_Cipullo'; PER=W+'Elsa_Peretti'; AMF=W+'Francesca_Amfitheatrof'
BUL=W+'Bulgari'; HER=W+'Herm%C3%A8s'; DY=W+'David_Yurman'; VCA='https://www.sothebys.com/en/articles/the-history-of-the-iconic-van-cleef-alhambra'
HEARD='https://heard.org/southwest-silverwork-1850-1940/'; BR=W+'Bracelet'; TB=W+'Tennis_bracelet'; CB=W+'Charm_bracelet'
PAN=W+'Pandora_(jewelry)'; FB=W+'Friendship_bracelet'; KARA=W+'Kara_(Sikhism)'; SB=W+'Slave_bracelet'; MID=W+'Medical_identification_tag'
AR=W+'Arm_ring'; BAN=W+'Bangle'
OLD_B='https://www.bloomingdales.com/shop/jewelry-accessories/designer-bracelets/Bracelets_type/Cuff?id=8701'
def X(n,a,d,mk,y,s,v=(),dt=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(('n','mk','y','d'),t)) for t in v],"dt":dt}
kinds=[
 {"n":"Bangle","a":"","d":"Rigid bracelet, closed or hinged, worn round the wrist (whatever a maker calls it).",
  "t":["choor (chudi)","kada","kankan","glass","lac","shell (shakha)","metal","wood","plastic","hinged","stacked set"],
  "s":OLD_B,"x":[
  X("Love bracelet","Cartier Love","Flat oval gold bangle closed by screws and opened only with the supplied screwdriver.","Cartier","1969",LOVE,
    [("Classic Love bracelet","Cartier","1969","Aldo Cipullo design; early pieces gold-plated, later solid 18k gold"),
     ("Love bracelet, pavé diamonds","Cartier","2009","fully diamond-paved"),
     ("Love bracelet, thin","Cartier","","hinge and a single screw"),
     ("Love bracelet, medium","Cartier","","between classic and thin widths"),
     ("Charity Love bracelet","Cartier","2006","silk cord with a gold LOVE ring")],
    "yellow, rose, white gold (platinum discontinued) · screw motif or diamonds · ceramic and coloured-stone versions"),
  X("Juste un Clou","Nails collection","Bangle shaped as a nail bent round the wrist.","Cartier","1971",CIP,
    [("Juste un Clou (original)","Cartier","1971","Aldo Cipullo, Nails collection")],"gold colours · with or without diamonds"),
  X("Kara","kada","Plain steel or iron bangle worn by Sikhs as one of the Five Ks.","","1699",KARA,
    [("Khalsa kara","","1699","instituted by Guru Gobind Singh at the Baisakhi Amrit Sanchar")],"steel, iron · single bangle · also worn by non-Sikh Punjabi and Hindu families"),
  X("Chooda","chura","Set of red and white bridal bangles worn by Punjabi brides on the wedding day and after.","","",BAN,[],"red and white · stonework · set size"),
  ]},
 {"n":"Cuff bracelet","a":"cuff","d":"Rigid bracelet with an opening, slipped on over the side of the wrist.",
  "t":["open cuff","wrap (coil) cuff","wire cuff","wide cuff","hinged cuff"],"s":OLD_B,"x":[
  X("Navajo silver cuff","Navajo bracelet","Hand-made Navajo silver cuff, stamped, chiselled or cast, often set with turquoise.","","1880s",HEARD,
    [("Copper or brass bangle","","1860s","hammered from heavy copper wire around Bosque Redondo"),
     ("Stamped flat silver cuff","","late 1880s","stamp-work decoration on coin silver"),
     ("Cast (tufa) cuff","","","cast silver, multiple castings from one mould"),
     ("Turquoise-set cuff","","1880s–1890s","bezel-set turquoise; multi-stone settings by the 1920s")],
    "coin or ingot silver · stamped, chiselled, cast · single or multi-stone turquoise"),
  X("Bone cuff","Elsa Peretti Bone","Sculpted cuff shaped like a wrist bone.","Tiffany & Co.","1970",PER,
    [("Elsa Peretti Bone cuff","Tiffany & Co.","1970","inspired by bones seen in a Capuchin church near Rome")],"silver, 18k gold · left or right wrist · inlays"),
  X("Serpenti","Bulgari Serpenti","Snake-form bracelet coiled round the wrist, also made as a bracelet-watch.","Bulgari","late 1940s",BUL,
    [("Serpenti bracelet-watch","Bulgari","late 1940s","first Serpenti form")],"gold · enamel or gem-set scales · bracelet or watch"),
  X("Tiffany T","T cuff","Minimal cuff or wire bracelet ending in the T motif.","Tiffany & Co.","2015",AMF,
    [("Tiffany T","Tiffany & Co.","2015","first collection of design director Francesca Amfitheatrof")],"gold colours, silver · wire or wide cuff · diamonds"),
  X("Cable bracelet","Cable Classics","Twisted-cable cuff with capped ends, the signature David Yurman form.","David Yurman","",DY,
    [("Cable Classics Bracelet","David Yurman","","from old data")],"silver, gold · end caps with gemstones · widths"),
  ]},
 {"n":"Tennis bracelet","a":"diamond line bracelet","d":"Flexible line of evenly set stones round the wrist.",
  "t":["four-claw","bezel","channel","lab-grown diamond","coloured gemstone"],"s":"https://www.bluenile.com/diamond-jewelry/diamond-bracelets/diamond-tennis-bracelets","x":[
  X("Diamond line bracelet","tennis bracelet","Hinged line of round diamonds, renamed after Chris Evert lost hers mid-match at the US Open.","","1978 (often given as 1987)",TB,
    [("Chris Evert's bracelet","","1978","fell onto the court at the US Open: 'I dropped my tennis bracelet'")],"round diamonds in four-claw settings · carat weight · gold or platinum")]},
 {"n":"Chain bracelet","a":"link bracelet","d":"Bracelet of linked chain.","t":["curb","anchor","figaro","paperclip","rolo","box","snake","station"],"s":OLD_B,"x":[
  X("Chaîne d'ancre","anchor chain","Silver chain of oval anchor-style links, emblematic of Hermès.","Hermès","1938",HER,
    [("Chaîne d'ancre (original)","Hermès","1938","designed by Robert Dumas")],"silver · link size · toggle clasp"),
  X("Alhambra bracelet","Van Cleef clover","Chain set with four-leaf-clover motifs edged in beaded gold.","Van Cleef & Arpels","1968",VCA,
    [("Vintage Alhambra","Van Cleef & Arpels","1968","original medium clover with beaded edges"),
     ("Magic Alhambra","Van Cleef & Arpels","early 2000s","clovers of mixed sizes"),
     ("Sweet Alhambra","Van Cleef & Arpels","","small clovers"),
     ("Pure Alhambra","Van Cleef & Arpels","","plain polished gold clovers"),
     ("Lucky Alhambra","Van Cleef & Arpels","","hearts, butterflies, leaves with the clover"),
     ("Byzantine Alhambra","Van Cleef & Arpels","","openwork gold")],"mother-of-pearl, onyx, malachite, carnelian, gold · motif count"),
  X("HardWear","Tiffany HardWear","Bold gold or silver link bracelet from Tiffany's HardWear line.","Tiffany & Co.","2017",AMF,
    [("HardWear","Tiffany & Co.","2017","gold, silver and leather collection")],"gold, silver · link size"),
  ]},
 {"n":"Charm bracelet","a":"","d":"Bracelet made to carry hanging or threaded charms.","t":["dangle charm","threaded bead charm","Italian link charm"],
  "s":"https://us.pandora.net/en/bracelets/charm-bracelets","x":[
  X("Pandora charm bracelet","European bead bracelet","Snake-chain bracelet onto which threaded silver charms are collected.","Pandora","2000",PAN,
    [("Moments Snake Chain Bracelet","Pandora","","Pandora Moments line"),("Moments Studded Chain Bracelet","Pandora","","Pandora Moments line")],"sterling silver, gold-plated · clasp style · charm count"),
  X("Italian charm bracelet","Nomination bracelet, Composable","Stretch band of flat steel links, each with a soldered charm face.","Nomination","1987",CB,
    [("Composable","Nomination","1987","original modular steel line")],"stainless steel · usually 18 links · enamel or gold faces"),
  X("Tiffany heart charm bracelet","","Link bracelet with a single heart charm, Tiffany's first charm bracelet.","Tiffany & Co.","1889",CB,[],"silver or gold link · heart tag"),
  ]},
 {"n":"Beaded bracelet","a":"","d":"Bracelet of strung beads or stones, stretch or clasped (power-stone bracelets included).","t":["stretch","clasped","wood","glass","crystal","gemstone (power-stone)","plastic"],"s":OLD_B},
 {"n":"Identity bracelet","a":"ID bracelet · medical ID bracelet","d":"Bracelet with an engraved plate or tag naming the wearer or a medical condition.","t":["engraved plate on chain","medical alert tag","silicone ID band","hatch with folded paper"],"s":BR,"x":[
  X("Medical ID bracelet","medical alert bracelet","Bracelet carrying an engraved tag that lists a medical condition for emergency responders.","","",MID,[],"stainless steel, silver, gold, silicone · pre-engraved or custom engraving")]},
 {"n":"Friendship bracelet","a":"","d":"Knotted or woven cord bracelet, often handmade from embroidery floss and given as a token of friendship.","t":["alpha (letters)","candystripe","chevron","zig zag","hearts","diamonds","double chain knot","Chinese staircase","beaded letter bracelet"],"s":FB},
 {"n":"Armlet","a":"arm ring · upper-arm bracelet · bajuband · kelat bahu · vangi","d":"Band or ornament worn round the upper arm.","t":["bajuband","kelat bahu (Indonesia)","vangi (Sri Lanka)","snake arm ring","chainmail armlet"],"s":"https://www.chainmailandmore.com/store/c/29-Arm-Jewelry.aspx",
  "m":[["Hexmaile Armlet","Chainmail & More"]]},
 {"n":"Hand harness","a":"haath phool · hand chain · slave bracelet","d":"Ornament joining one or more finger rings by chains to a bracelet across the back of the hand.","t":["single ring","multi-ring","beaded"],"s":"https://amyojewelry.com/collections/bracelets-handchains",
  "m":[["Faceted Hand Chain","AMYO"],["Minimal Ring Handchain","AMYO"]]},
]
brands=[
 {"n":"Cartier","c":"France","f":"1847","seg":"Luxury jeweller","d":"Paris jewellery house, part of Richemont.","lines":["Love","Juste un Clou"],"eras":["Aldo Cipullo, designer, 1969–1970s"],"sig":["Love bracelet","Juste un Clou"],"sc":[],"rel":["Van Cleef & Arpels","Tiffany & Co."],"s":"knowledge"},
 {"n":"Tiffany & Co.","c":"United States","f":"1837","seg":"Luxury jeweller","d":"New York jeweller; Elsa Peretti designed for it from 1974.","lines":["Elsa Peretti","Tiffany T","HardWear"],"eras":["Elsa Peretti, 1974–2021","Francesca Amfitheatrof, design director, 2014–"],"sig":["Bone cuff","Tiffany T","HardWear"],"sc":[],"rel":["Cartier"],"s":"knowledge"},
 {"n":"Bulgari","c":"Italy","f":"1884","seg":"Luxury jeweller","d":"Roman jeweller founded by Sotirios Voulgaris, owned by LVMH since 2011.","lines":["Serpenti","B.zero1"],"eras":[],"sig":["Serpenti"],"sc":[],"rel":[],"s":BUL},
 {"n":"Hermès","c":"France","f":"1837","seg":"Luxury house","d":"Paris saddler turned luxury house whose jewellery grew from equestrian buckles.","lines":["Chaîne d'ancre"],"eras":["Robert Dumas, 1938"],"sig":["Chaîne d'ancre"],"sc":[],"rel":[],"s":HER},
 {"n":"Van Cleef & Arpels","c":"France","f":"1896","seg":"Luxury jeweller","d":"Paris jeweller owned by Richemont since 1999.","lines":["Alhambra"],"eras":[],"sig":["Alhambra bracelet"],"sc":[],"rel":["Cartier"],"s":W+'Van_Cleef_%26_Arpels'},
 {"n":"David Yurman","c":"United States","f":"1980","seg":"Designer jeweller","d":"American jeweller founded by David and Sybil Yurman, known for the cable motif.","lines":["Cable Classics"],"eras":[],"sig":["Cable bracelet"],"sc":[],"rel":[],"s":DY},
 {"n":"Pandora","c":"Denmark","f":"1982","seg":"Mass-market jeweller","d":"Copenhagen jeweller founded by Per and Winnie Enevoldsen; charm bracelets since 2000.","lines":["Pandora Moments"],"eras":[],"sig":["Pandora charm bracelet"],"sc":[],"rel":["Nomination"],"s":PAN},
 {"n":"Nomination","c":"Italy","f":"","seg":"Fashion jeweller","d":"Sesto Fiorentino maker of the modular Composable Italian charm bracelet (1987).","lines":["Composable"],"eras":[],"sig":["Italian charm bracelet"],"sc":[],"rel":["Pandora"],"s":CB},
]
trads=[{"n":"Navajo silversmithing","g":"Metal & blades","r":"Navajo Nation, south-western United States","p":"1850s–present","d":"Navajo silverwork begun by Atsidi Sani, known for stamped and cast cuffs set with turquoise.","tech":"hammering coin or ingot silver, stamp work, chiselling, tufa casting, bezel setting","mat":"silver (pesos, US coins, then refinery ingots), copper, brass, turquoise","forms":["Navajo silver cuff","Squash blossom necklace"],"ctr":["Atsidi Sani (Herrero)"],"auth":"coin-derived silver, hand stamp and chisel marks, filed ingot grooves, Native-cut or domed turquoise in bezels","s":HEARD}]
notes=("Old models kept as versions (Cartier none; David Yurman Cable Classics; Pandora Moments x2). Choor/kada/kankan moved from m to Bangle types; Kara archetype added. "
 "Dropped 'Diamond Harem Slave Armlet' (retail SKU noise; one Chainmail & More armlet kept). No sourced versions found for Hermès Clic H, Cartier Love SM/Unlimited or Serpenti Tubogas, so left out. "
 "Beaded and Friendship bracelets have no archetypes (no maker-defined icons found); patterns kept as types. Hand harness keeps old AMYO models. "
 "Tennis bracelet naming: Wikipedia gives 1978 US Open, many sources say 1987.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/A3/shelves/03_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
