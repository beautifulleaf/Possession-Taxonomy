import json, os
W='https://en.wikipedia.org/wiki/Grip_(sport_fencing)'
FM='https://fencing.net/guides/fencing-safety-the-maraging-blade/'
BG='https://www.leonpaul.com/leon-paul-buyers-guide-new'
GL='https://fencing.net/15333/guide-fie-sabre-gloves/'
SH='https://fencing.net/4197/the-comprehensive-guide-to-fencing-shoes/'
SUB='https://ecsfencer.substack.com/p/fencing-kit-buying-guide'
AP='https://allstar.de/en/CLOTHING-FOOTWEAR/PROTECTIVE-EQUIPMENT/Underplastrons/'
def X(n,d,mk,y,s,v=(),dt='',a=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=a1,mk=b,y=c,d=e) for a1,b,c,e in v],"dt":dt}
grips=[
 X("Visconti grip","Named pistol (orthopaedic) grip pattern that fixes the hand in one position.","", "",W,[("Negrini Visconti","","","named variant")],"sizes · leather or rubber wrap · left/right hand"),
 X("Belgian grip","Named pistol (orthopaedic) grip pattern; the Schermasport is a loose variant.","", "",W,[("Schermasport","","","loose variant of the Belgian")],"sizes · left/right hand"),
 X("Russian grip","Named pistol (orthopaedic) grip pattern.","", "",W,[],"sizes · left/right hand"),
 X("Hungarian grip","Named pistol (orthopaedic) grip pattern.","", "",W,[],"sizes · left/right hand"),
]
kinds=[
{"n":"Fencing foil","a":"","d":"Light thrusting fencing weapon with a flexible rectangular blade, made to FIE rules for the foil.",
 "t":["electric","non-electric (dry)","FIE maraging blade","non-FIE carbon-steel blade","pistol grip","French grip","blade size 0–5 (children's to adult)"],
 "s":"https://leonpaulusa.com/mag-tec-fie-foil-with-pistol-grip.html",
 "x":[X("Maraging FIE blade","Maraging-steel blade carrying the FIE stamp, the standard for international foil, épée and (since 2020) sabre; recognised by the BF mark of Blaise Frères.","Blaise Frères","1980s",FM,[],"foil, épée, sabre · blade length · stiffness"),
      X("Mag-Tec FIE Foil","Leon Paul's lightweight competition foil with every part refined for low weight.","Leon Paul","",'https://leonpaulusa.com/mag-tec-fie-foil-with-pistol-grip.html',[("Mag-Tec FIE Foil (Apex FIE Blade)","Leon Paul","","current version fitted with the Apex FIE blade")],"pistol or French grip · left/right hand"),
      X("Golubitsky-Pro blade","Foil blade designed to Sergei Golubitsky's requirements, with weight shifted towards the hand.","Leon Paul","",FM,[],"")]+grips,
 "r":[["Mag-Tec","Leon Paul"]]},
{"n":"Fencing epee","a":"épée","d":"Thrusting fencing weapon with a stiff triangular blade and a large bell guard, made to FIE rules for the epee.",
 "t":["electric","non-electric (dry)","FIE maraging blade","non-FIE carbon-steel blade","French grip","pistol grip","guard: duralumin (lightweight), steel, titanium","offset guard (French épée)"],
 "s":"https://www.leonpaulusa.com/fencing-weapons/fencing-weapons/complete-electric-and-non-electric-epees.html",
 "x":[X("French grip","Straight or slightly curved grip held towards the pommel ('posting') for extra reach; favoured by épéeists.","","late 19th century",W,[],"length · straight or canted · leather wrap"),
      X("Italian grip","Rapier-derived grip with a crossbar, essentially unchanged since the 18th century; legal but rarely used.","","18th century",W,[],"")],
 "m":[["Mag-Tec FIE Epee","Leon Paul"],["Advanced Lightweight","Leon Paul"],["Extra Reach","Leon Paul"],["Project Zer0","Leon Paul"],["Sub Zer0","Leon Paul"],["Slimline Carbon French Grip FIE","Leon Paul"],["Standard","Leon Paul"]],
 "r":[["Mag-Tec","Leon Paul"]]},
{"n":"Fencing sabre","a":"","d":"Cutting and thrusting fencing weapon with a knuckle guard, made to FIE rules. The sabre sword is in Weapons & Armour.",
 "t":["electric","non-electric (dry)","FIE maraging blade (required at FIE events after Tokyo 2020)","non-FIE blade"],
 "s":"https://www.leonpaulusa.com/fencing-weapons/fencing-weapons/electric-and-non-electric-sabres.html",
 "m":[["Apex FIE Sabre","Leon Paul"],["Standard Sabre","Leon Paul"]],"r":[["Apex","Leon Paul"]]},
{"n":"Fencing mask","a":"","d":"Mesh mask with a bib that protects a fencer's face, head and neck; the FIE 1600 N bib is noted where it is met.",
 "t":["350 N bib (club)","1600 N FIE bib","foil (conductive bib)","épée","sabre (conductive mesh)","removable washable padding"],
 "s":"https://www.leonpaulusa.com/colored-x-change-fie-contour-foil-mask.html",
 "x":[X("X-Change FIE mask","Leon Paul's top mask range with a 1600 N bib and changeable padding, required level for international competition.","Leon Paul","",BG,[("X-Change FIE Contour Foil Mask","Leon Paul","","foil version"),("X-Change Contour Coaching Mask","Leon Paul","","coaching mask, silver mesh")],"foil, épée, sabre · coloured or plain bib"),
      X("FIE 1600N Comfort Plus mask","Heavily padded FIE mask with a removable washable inlay, sold under both Allstar and Uhlmann.","Allstar","",SUB,[("Uhlmann FIE 1600N Comfort Plus","Uhlmann","","same product line")],"foil, épée, sabre")],
 "m":[["Horizon","Leon Paul"],["Arena","Leon Paul"],["Club","Leon Paul"]],"r":[["X-Change","Leon Paul"]]},
{"n":"Fencing jacket","a":"fencing lamé · electric jacket","d":"Protective jacket made for fencing, rated to a puncture resistance such as FIE 800 N.",
 "t":["350 N (club)","800 N FIE","front-zip (handed)","back-zip","electric lamé overjacket (foil, sabre)"],
 "s":"https://www.leonpaulusa.com/clothing/mens-fencing-uniforms.html",
 "x":[X("Apex FIE Jacket","Leon Paul's FIE-level jacket, sold as a range with matching breeches.","Leon Paul","",BG,[],"men's, women's · left/right hand")],
 "m":[["Phoenix 350N Jacket","Leon Paul"],["Team FIE Jacket","Leon Paul"],["Lightweight Foil Lamé","Leon Paul"]],
 "r":[["Apex","Leon Paul"],["Phoenix 350N","Leon Paul"],["Team FIE","Leon Paul"]]},
{"n":"Fencing underarm protector","a":"fencing plastron · underplastron","d":"Half-jacket worn under the fencing jacket on the weapon-arm side, rated to FIE 800 N where certified.",
 "t":["350 N","800 N FIE","left- or right-handed","men's, women's, children's"],
 "s":"https://www.leonpaulusa.com/fencing-clothing-uniforms.html",
 "x":[X("ExtraLight FIE Underplastron","Lightweight 800 N FIE underplastron made of Dyneema fibre.","Allstar","",AP,[("Ecoline FIE Underplastron","Allstar","","thicker, cheaper 800 N fabric"),("Ecoline 350N Underplastron","Allstar","","non-FIE 350 N")],"men's, women's, kids' · 3/4 cut")],
 "m":[["Lightweight FIE Plastron","Leon Paul"]]},
{"n":"Fencing chest protector","a":"","d":"Rigid plastic chest guard worn under the fencing jacket.",
 "t":["women's","men's","children's"],
 "s":"https://www.leonpaulusa.com/fencing-clothing-uniforms.html",
 "m":[["Econoguard","Leon Paul"],["Masterguard","Leon Paul"]]},
{"n":"Fencing glove","a":"","d":"Padded glove with a cuff worn on the weapon hand in fencing.",
 "t":["foil/épée glove","sabre glove with conductive cuff (manchette)","800 N FIE","non-FIE"],
 "s":"https://www.leonpaulusa.com/fencing-clothing-uniforms.html",
 "x":[X("ExoSkin glove","Leon Paul's FIE glove range with a lightweight, durable lamé.","Leon Paul","",BG,[("ExoSkin 800N Sabre Glove","Leon Paul","",""),("FIE ExoSkin II Foil/Épée Glove","Leon Paul","",""),("FIE ExoSkin II Sabre Glove","Leon Paul","","")],"foil/épée or sabre · sizes")],
 "m":[["FIE Electric Sabre Glove","Allstar"],["FIE Sabre Glove","Uhlmann"],["FIE Sabre Glove","PBT"],["FIE Sabre Glove","Absolute Fencing"],["Gant 800N","Prieur"],["800N Sabre Glove","Planète Escrime"],["Safety Gel FIE Sabre Glove","FWF"],["Unibody FIE Sabre Glove","Negrini"],["Advanced fencing glove","Leon Paul"]]},
{"n":"Fencing breeches","a":"","d":"Knee-length protective breeches made for fencing, rated to FIE 800 N where certified.",
 "t":["350 N","800 N FIE","left- or right-handed (zip panel)"],
 "s":"https://www.leonpaulusa.com/clothing/mens-fencing-uniforms.html",
 "m":[["Apex FIE Breeches","Leon Paul"]]},
{"n":"Fencing shoe","a":"","d":"Flat, reinforced shoe made for fencing footwork.",
 "t":["fencing-specific","court shoe used for fencing (handball, tennis)"],
 "s":"https://www.leonpaulusa.com/fencing-clothing-uniforms.html",
 "x":[X("Nike Ballestra","Nike's dedicated fencing shoe, long the premium standard.","Nike","2008",SH,[("Ballestra","Nike","2008–2020","original; briefly sold as Nike Air Zoom"),("Ballestra 2","Nike","2020","successor")],"colourways"),
      X("Kempa Attack Pro","Fencing shoe made with Allstar/Uhlmann on a handball-shoe base, wider than Nike or Adidas.","Kempa","2019",SH,[("Attack Junior","Kempa","","youth sizes, hook-and-loop")],""),
      X("Hi-Tec x Leon Paul Razor","Mid-range fencing shoe with offset lacing and an extra heel cup, sold by Leon Paul.","Hi-Tec","",SH,[],"")],
 "m":[["AF Elite","Absolute Fencing"],["Lightning","Leon Paul"],["Coral","Leon Paul"]]},
]
K='knowledge'
brands=[
 {"n":"Leon Paul","c":"United Kingdom","f":"1921","seg":"Professional & flagship","kf":"fencing equipment","d":"London fencing maker founded by fencing master Leon Paul in Covent Garden; makes its own blades and invented the sectional piste.","lines":["Apex","Mag-Tec","X-Change","ExoSkin","Phoenix","Team"],"eras":[],"sig":["Mag-Tec FIE Foil","X-Change FIE mask","Apex FIE Jacket"],"sc":["Olympic fencing"],"rel":["Hi-Tec"],"s":"https://www.leonpaul.com/explore/heritage"},
 {"n":"Allstar","c":"Germany","f":"","seg":"Professional & flagship","kf":"fencing equipment","d":"Family-run German fencing manufacturer in its fourth generation, selling masks, clothing, weapons and pistes in over 160 countries.","lines":["ExtraLight","Ecoline"],"eras":[],"sig":["FIE 1600N Comfort Plus mask","ExtraLight FIE Underplastron"],"sc":["Olympic fencing"],"rel":["Uhlmann","Kempa"],"s":"https://allstar.de/en/"},
 {"n":"Uhlmann","c":"Germany","f":"","seg":"Professional & flagship","kf":"fencing equipment","d":"Fencing equipment maker from Laupheim, Germany, whose lines are often sold alongside Allstar.","lines":[],"eras":[],"sig":[],"sc":["Olympic fencing"],"rel":["Allstar"],"s":K},
 {"n":"PBT","c":"Hungary","f":"1991","seg":"Specialist","kf":"fencing equipment","d":"Hungarian fencing equipment maker whose sabres and jackets were used at Tokyo 2020 and Paris 2024.","lines":[],"eras":[],"sig":[],"sc":["Olympic fencing","HEMA"],"rel":[],"s":"http://olympic-museum-artefacts.zetcom.net/en/artists/artist/47018/"},
 {"n":"Prieur","c":"France","f":"1788","seg":"Heritage manufactory","kf":"fencing masks and weapons","d":"French fencing maker at Genlis near Dijon, credited with the first full-face mask; supplier to the French team again from 2023.","lines":[],"eras":["Didier Contrepois ownership, from 2014"],"sig":[],"sc":["Olympic fencing"],"rel":["Planète Escrime"],"s":"https://www.lagazettefrance.fr/article/la-renaissance-de-l-historique-equipementier-d-escrime-prieur-sport"},
 {"n":"Absolute Fencing","c":"United States","f":"","seg":"Specialist","kf":"fencing equipment","d":"Bridgewater, New Jersey supplier of fencing gear, strips and scoring machines, partner of USA Fencing.","lines":["AF Elite"],"eras":[],"sig":[],"sc":["Olympic fencing"],"rel":[],"s":"https://www.usafencing.org/news/2023/may/10/usa-fencing-and-absolute-fencing-renew-partnership-through-2028-olympics-and-paralympics-in-los-angeles"},
 {"n":"Blaise Frères","c":"France","f":"1885","seg":"Heritage manufactory","kf":"fencing blades","d":"Forge near Saint-Étienne whose BF-stamped maraging blades are the standard FIE competition blade.","lines":[],"eras":[],"sig":["Maraging FIE blade"],"sc":["Olympic fencing"],"rel":[],"s":FM},
 {"n":"Nike","c":"United States","f":"1964","seg":"Mainstream","kf":"athletic footwear","d":"American sportswear company; makes the Ballestra fencing shoe.","lines":[],"eras":[],"sig":["Nike Ballestra"],"sc":[],"rel":[],"s":K},
 {"n":"Kempa","c":"Germany","f":"","seg":"Specialist","kf":"handball","d":"German handball brand that makes the Attack Pro fencing shoe with Allstar/Uhlmann.","lines":[],"eras":[],"sig":["Kempa Attack Pro"],"sc":[],"rel":["Allstar"],"s":K},
 {"n":"Hi-Tec","c":"United Kingdom","f":"","seg":"Mainstream","kf":"sports footwear","d":"British sports-footwear brand that makes the Razor fencing shoe with Leon Paul.","lines":[],"eras":[],"sig":["Hi-Tec x Leon Paul Razor"],"sc":[],"rel":["Leon Paul"],"s":K},
]
notes=("Fencing lame merged into Fencing jacket (alias + t 'electric lamé'). All 10 planned kinds kept. Grip patterns (French, Italian, Visconti, Belgian, Russian, Hungarian) "
 "sourced from Wikipedia 'Grip (sport fencing)'; pistol grips placed under foil, French/Italian under épée. No brand-specific blade versions for épée/sabre could be confirmed beyond Leon Paul old data; "
 "PBT and Absolute Fencing kept as brands with glove models only. Founding years for Allstar, Uhlmann and Absolute Fencing left blank (sources conflict). Uhlmann/Nike/Kempa/Hi-Tec brand entries from knowledge.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/13_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
