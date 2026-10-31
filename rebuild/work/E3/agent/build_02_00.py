import json, os
W='https://en.wikipedia.org/wiki/'
ST=W+'Steinway_%26_Sons'; BO=W+'B%C3%B6sendorfer'; FA=W+'Fazioli'; BE=W+'C._Bechstein'; BL=W+'Bl%C3%BCthner'
KA=W+'Kawai_Musical_Instruments'; SK=W+'Shigeru_Kawai'; SG=W+'Steingraeber_%26_S%C3%B6hne'; PL=W+'Pleyel_et_Cie'
ER=W+'S%C3%A9bastien_%C3%89rard'; RH=W+'Rhodes_piano'; WU=W+'Wurlitzer_electronic_piano'; CL=W+'Clavinet'
CP=W+'Yamaha_CP-70'; HA=W+'Harpsichord'; RU=W+'Ruckers'; CH=W+'Clavichord'; PP=W+'Player_piano'
DP=W+'Digital_piano'; PI=W+'Piano'; DK=W+'Yamaha_Disklavier'; CV=W+'Clavinova'; YC=W+'Yamaha_Corporation'
U1='https://www.merriammusic.com/product/used-yamaha-u1-silent-upright-piano/'
def X(n,d,mk,y,s,v=(),a='',dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
grand={"n":"Grand piano","a":"concert grand · baby grand · parlour grand · boudoir grand",
 "d":"Acoustic piano with a horizontal frame and strings, from about 1.5 m baby grands to 3 m concert grands.",
 "t":["Baby grand (about 1.5 m)","Parlour or boudoir grand (1.7–2.2 m)","Concert grand (2.2–3 m)","Silent / hybrid grand"],
 "s":PI,"x":[
 X("Steinway Model D","Steinway's full concert grand, the standard instrument of concert halls; about 480 kg.","Steinway & Sons","",ST,
   [("D-274","Steinway & Sons","","Hamburg build, 274 cm"),("Model D (New York)","Steinway & Sons","","New York build, 8 ft 11¾ in")],dt="New York or Hamburg build · ebony or veneer case · Spirio player option"),
 X("Steinway Model B","Steinway's 211 cm semi-concert grand, widely used in studios and teaching rooms.","Steinway & Sons","",ST,
   [("B-211","Steinway & Sons","","Hamburg, 211 cm"),("Model B (New York)","Steinway & Sons","","New York, 6 ft 11 in")]),
 X("Steinway Model C","Steinway's 227 cm grand, built in Hamburg.","Steinway & Sons","",ST,[("C-227","Steinway & Sons","","Hamburg, 227 cm")]),
 X("Steinway Model A","Steinway's 188 cm grand, in the range since the 19th century with duplex scaling.","Steinway & Sons","1883 (example shown)",ST,
   [("A-188","Steinway & Sons","","Hamburg, 188 cm"),("Model A (New York)","Steinway & Sons","","New York, 6 ft 2 in")]),
 X("Steinway Model O","Steinway's 180 cm living-room grand.","Steinway & Sons","",ST,
   [("O-180","Steinway & Sons","","Hamburg, 180 cm"),("Model O (New York)","Steinway & Sons","","New York, 5 ft 10¾ in"),("Model L","Steinway & Sons","1922–2006","5 ft 10½ in replacement for the Model O")]),
 X("Steinway Model M","Steinway's 170 cm medium grand.","Steinway & Sons","",ST,
   [("M-170","Steinway & Sons","","Hamburg, 170 cm"),("Model M (New York)","Steinway & Sons","","New York, 5 ft 7 in")]),
 X("Steinway Model S","Steinway's smallest grand, 155 cm.","Steinway & Sons","",ST,
   [("S-155","Steinway & Sons","","Hamburg, 155 cm"),("Model S (New York)","Steinway & Sons","","New York, 5 ft 1 in")]),
 X("Bösendorfer Imperial 290","290 cm Viennese concert grand with nine extra bass keys (97 in all), commissioned by Ferruccio Busoni.","Bösendorfer","1909",BO,
   [("290 Imperial","Bösendorfer","1909","97 keys"),("290SE reproducing","Bösendorfer","1984–1987","SE reproducing system; 32 SE pianos built in all")],a="Model 290"),
 X("Bösendorfer VC grands","Bösendorfer's 'VC' grand range, model number equal to length in cm.","Bösendorfer","",BO,
   [("280 VC","Bösendorfer","","280 cm concert grand"),("230 VC","Bösendorfer","","230 cm"),("214 VC","Bösendorfer","","214 cm"),("185 VC","Bösendorfer","","185 cm"),("170 VC","Bösendorfer","","170 cm"),("225","Bösendorfer","","225 cm, 92 keys")]),
 X("Fazioli F278","Fazioli's 278 cm concert grand, among the first prototypes of the Sacile workshop.","Fazioli","1980 (prototype)",FA),
 X("Fazioli F308","Fazioli's 308 cm concert grand, the largest piano on the general market (about 570 kg).","Fazioli","1987 (first public performance); 1995 (NAMM)",FA),
 X("Fazioli smaller grands","Fazioli's salon to chamber grands, named by length in cm.","Fazioli","1980 onwards",FA,
   [("F228","Fazioli","1980","228 cm"),("F212","Fazioli","","212 cm"),("F198","Fazioli","","198 cm"),("F183","Fazioli","1980","183 cm"),("F156","Fazioli","1980","156 cm")]),
 X("C. Bechstein Concert grands","Bechstein's top grand line, from the D 282 concert grand down.","C. Bechstein","",BE,
   [("D 282","C. Bechstein","","282 cm concert grand"),("C 234","C. Bechstein","",""),("B 212","C. Bechstein","",""),("A 192","C. Bechstein","",""),("L 167","C. Bechstein","",""),("Model B-208 (interwar)","C. Bechstein","1920s–1930s","among the most successful models"),("Academy A 228–A 160","C. Bechstein","","mid-range Academy line")]),
 X("Blüthner aliquot grand","Leipzig grand with Blüthner's aliquot stringing: an extra sympathetic string on treble notes.","Blüthner","19th century",BL,
   [("Hindenburg piano","Blüthner","1936","lightweight aluminium-frame grand for the airship")]),
 X("Shigeru Kawai SK-EX","Kawai's hand-built 278 cm concert grand, top of the Shigeru Kawai series.","Kawai","2001",SK,
   [("SK-7","Kawai","","229 cm"),("SK-6","Kawai","","214 cm"),("SK-5","Kawai","","200 cm"),("SK-3","Kawai","","188 cm"),("SK-2","Kawai","","180 cm")],a="Shigeru Kawai series (1999)"),
 X("Kawai GX BLAK","Kawai's mainstream performance grand series with carbon-composite action parts.","Kawai","2013",KA,
   [("GX-7 to GX-1","Kawai","2013",""),("RX series","Kawai","1996","predecessor"),("GL series","Kawai","2015","entry grands GL-10 to GL-50"),("EX Concert Grand","Kawai","","")]),
 X("Steingraeber concert grand","Bayreuth-built 276 cm concert grand from a small family workshop.","Steingraeber & Söhne","",SG,
   [("232 cm semi-concert","Steingraeber & Söhne","2008","shown at Musikmesse Frankfurt"),("212 cm chamber concert","Steingraeber & Söhne","",""),("Transducer grand","Steingraeber & Söhne","2017","")]),
 X("Pleyel grand (historical)","Paris grand of the firm Chopin preferred and played at the Salle Pleyel.","Pleyel","19th century",PL,
   [("Duo-Clave double piano","Pleyel","1890s–1920s","two keyboards facing each other, after Emánuel Moór")]),
 X("Érard double-escapement grand","Paris grand with Sébastien Érard's double escapement action, the basis of modern grand actions.","Érard","1823",ER,
   [("Piano-pédalier","Érard","","pedal-board piano, Alkan's example in the Musée de la musique")]),
 ]}
upright={"n":"Upright piano","a":"vertical piano · spinet · console · studio upright",
 "d":"Acoustic piano with a vertical frame and strings, made for homes and practice rooms.",
 "t":["Spinet","Console","Studio (about 107–114 cm)","Full-size upright","Silent / hybrid upright"],"s":PI,"x":[
 X("Yamaha U1","Yamaha's 121 cm professional upright, built since the 1960s and the most widely sold upright model.","Yamaha","1960s",U1,
   [("U1 Silent","Yamaha","","with silent practice system")]),
 X("Steinway Vertegrand","Steinway's tall upright line.","Steinway & Sons","",ST,
   [("K-132","Steinway & Sons","","Hamburg, 132 cm"),("K-52","Steinway & Sons","","New York")]),
 X("Steinway Model 1098","Steinway's 'Professional Upright' for schools and studios.","Steinway & Sons","by 1953",ST),
 X("C. Bechstein Concert 8","Bechstein's tall concert upright, descendant of the interwar Model 8.","C. Bechstein","1920s–1930s (Model 8)",BE,
   [("Model 8 / Model 9","C. Bechstein","interwar",""),("Concert 6","C. Bechstein","",""),("Academy A6, A2","C. Bechstein","","")]),
 X("Bösendorfer uprights","Bösendorfer's two upright models, named by height in cm.","Bösendorfer","",BO,
   [("130","Bösendorfer","","130 cm"),("120","Bösendorfer","","120 cm")]),
 X("Steingraeber 138 concert upright","Steingraeber's largest upright, 138 cm.","Steingraeber & Söhne","",SG,
   [("130","Steingraeber & Söhne","",""),("122","Steingraeber & Söhne","","")]),
 ],"m":[["Yamaha b1","Yamaha"],["Kawai K 15","Kawai"]]}
digital={"n":"Digital piano","a":"home digital piano · stage piano · hybrid piano",
 "d":"Electronic piano with weighted keys and sampled or modelled piano sound, with or without built-in speakers.",
 "t":["Console (home) digital piano","Portable digital piano","Stage piano (no speakers)","Hybrid piano"],
 "s":"https://www.thomannmusic.com/keys.html","x":[
 X("Yamaha Clavinova","Yamaha's home digital piano line, widely seen as the first digital piano.","Yamaha","1983",CV,
   [("YP-10 / YP-20 / YP-30 / YP-40","Yamaha","1983","first models"),("CLP series","Yamaha","","piano-focused; CLP-800 series 2024"),("CVP series","Yamaha","","ensemble models; CVP-900 series 2023"),("CSP series","Yamaha","2017","")]),
 ],"m":[["FP-90X","Roland"],["V-Piano","Roland"],["CA series","Kawai"],["ES series","Kawai"],["MP series","Kawai"],["Privia PX-S3100","Casio"],["Celviano Grand Hybrid","Casio"],["Nord Piano 3","Clavia"],["U1 SH2 hybrid","Yamaha"]]}
electric={"n":"Electric piano","a":"electromechanical piano · Rhodes · Wurly · Clavinet",
 "d":"Electromechanical piano whose hammers or pads set tines, reeds or strings vibrating, read by pickups.",
 "t":["Tine (Rhodes type)","Reed (Wurlitzer type)","Plucked string (Clavinet type)","Electric grand (string type)"],
 "s":"https://keyboardexchange.com/inventory.html","x":[
 X("Rhodes piano","Tine-and-tonebar electric piano by Harold Rhodes, made with Fender from 1965.","Rhodes","1965",RH,
   [("Pre-Piano","Rhodes","1948","38 keys, Harold Rhodes's first marketed model"),("Piano Bass","Rhodes","1962","32-key keyboard bass for Fender"),("Fender Rhodes Silvertop","Rhodes","1965","73 keys, first Fender Rhodes"),("Mk I Suitcase","Rhodes","1970","73 keys, built-in amp cabinet"),("Mk I Stage","Rhodes","1970","73 keys"),("Mk I Stage 88","Rhodes","1971","88 keys"),("Mk II","Rhodes","1979","cosmetic update; 54-key model added"),("Mk V","Rhodes","1984","last of the original company"),("Mark 7","Rhodes","2007","reissue"),("Mark 8","Rhodes","2021","")],
   a="Fender Rhodes",dt="73 / 88 / 54 keys · Stage or Suitcase · Silvertop, Mk I–V"),
 X("Wurlitzer 200A","64-key portable reed electric piano, the most commercially successful Wurlitzer.","Wurlitzer","1974",WU,
   [("200","Wurlitzer","1968","plastic lid, two speakers"),("200A","Wurlitzer","1974–1983","improved hum shielding"),("200B","Wurlitzer","1978","battery model, no amp"),("206 / 206A","Wurlitzer","","classroom console"),("270 Butterfly Baby Grand","Wurlitzer","","domestic sister of the 200A")]),
 X("Wurlitzer early portables","Wurlitzer's first reed electric pianos, from the pilot 100 to the solid-state 140.","Wurlitzer","1954",WU,
   [("100","Wurlitzer","1954","pilot model"),("112","Wurlitzer","1955–1956","first mass-produced"),("120","Wurlitzer","1956–1962","first with tremolo"),("140","Wurlitzer","1962–1968","solid-state amp")]),
 X("Hohner Clavinet D6","Ernst Zacharias's plucked-string electric clavichord in its most popular form.","Hohner","1971",CL,
   [("Clavinet I","Hohner","1964","first model, built-in amp"),("Clavinet II","Hohner","1960s",""),("Clavinet C","Hohner","1968",""),("Clavinet L","Hohner","1968","trapezoid domestic model"),("D6","Hohner","1971",""),("Clavinet Duo","Hohner","1978","with Pianet T"),("E7","Hohner","1979","stage model")]),
 X("Yamaha CP-70","Electric grand with real strings and hammers, no soundboard, and piezo pickups.","Yamaha","1976",CP,
   [("CP-70B","Yamaha","1978",""),("CP-80","Yamaha","1978","88 keys"),("CP-70M / CP-80M","Yamaha","1985","MIDI")],a="CP-80 electric grand"),
 ]}
harps={"n":"Harpsichord","a":"cembalo · clavecin",
 "d":"Keyboard instrument whose strings are plucked by quills or plectra.",
 "t":["Single-manual","Double-manual","Virginal","Spinet","Muselar"],
 "s":"https://www.henrylebedinsky.com/for-sale","x":[
 X("Flemish harpsichord","Heavier Antwerp design with steel treble strings and the first two-manual instruments; model for later schools.","","late 16th century",RU,
   [("Ruckers single-manual","","16th–17th century","Hans, Joannes and Andreas Ruckers"),("Ruckers two-manual transposing","","17th century","manuals a fourth apart"),("Couchet","","17th century","successor workshop"),("Ravalement","","18th century","Paris rebuilds extending range (Blanchet, Taskin, Goermans)")],
   a="Ruckers type"),
 X("Italian harpsichord","Light, thin-cased single-manual harpsichord with low-tension brass strings.","","16th century",HA,
   [("Ottavino","","to 19th century","small four-foot instrument")]),
 X("French double-manual harpsichord","18th-century 'expressive double' with manuals controlling different choirs and a shove coupler.","","18th century",HA,
   [("Blanchet","","18th century",""),("Taskin","","18th century","Pascal Taskin")]),
 X("English harpsichord","Powerful veneered harpsichord with dogleg jacks.","","18th century",HA,
   [("Kirkman","","18th century",""),("Shudi","","18th century","")]),
 X("German harpsichord","Harpsichord with extended registers including 16-foot and 2-foot choirs.","","18th century",HA,
   [("Hass","","18th century","Hieronymus Albrecht Hass; one three-manual instrument"),("Mietke","","18th century","Michael Mietke")]),
 X("Historical-copy harpsichord","Modern instrument built by Baroque methods after surviving originals.","","mid-20th century",HA,
   [("Frank Hubbard","","20th century",""),("William Dowd","","20th century",""),("Martin Skowroneck","","20th century","")]),
 X("Revival harpsichord","Early 20th-century harpsichord built with piano-style construction.","","early 20th century",HA),
 ]}
clavi={"n":"Clavichord","a":"",
 "d":"Small rectangular keyboard whose strings are struck by brass tangents that stay on the string while the key is held.",
 "t":["Fretted (gebunden)","Unfretted (bundfrei)"],"s":CH,"x":[
 X("Fretted clavichord","Clavichord where several keys share a string pair (gebunden).","","Late Middle Ages",CH),
 X("Unfretted clavichord","Clavichord with its own string pair for every note (bundfrei).","","1693 (first reference)",CH,
   [("Heinitz","","1716","earliest signed and dated example"),("Hass","","1763","Johann Adolph Hass"),("Kintzing","","1763","Christian Kintzing, Neuwied"),("Stein","","18th century","Johann Andreas Stein, Augsburg")])]}
player={"n":"Player piano","a":"pianola · reproducing piano · self-playing piano",
 "d":"Piano that plays itself from perforated rolls or, in modern systems, MIDI data.",
 "t":["Pedal-operated (pneumatic)","Reproducing","Digital player system","Retrofit kit"],"s":PP,"x":[
 X("Pianola","All-pneumatic pedal-operated player invented by Edwin S. Votey.","Aeolian","1896",PP),
 X("Welte-Mignon","Reproducing piano that plays back a recorded performance with dynamics.","Welte","1904",PP),
 X("Duo-Art","Aeolian's reproducing system, rival of the Welte-Mignon.","Aeolian","1914",PP),
 X("Ampico","American reproducing piano system.","","1911",PP),
 X("Yamaha Disklavier","Acoustic piano with sensors and solenoids that records and plays MIDI.","Yamaha","1987",DK,
   [("Mark II","Yamaha","1992",""),("Mark IIXG","Yamaha","about 1994",""),("Disklavier PRO","Yamaha","1998–1999","high-resolution recording"),("Mark III","Yamaha","2000",""),("Mark IV","Yamaha","2004","grands only"),("E3","Yamaha","2009",""),("ENSPIRE","Yamaha","2016","seventh generation")]),
 X("Steinway Spirio","Steinway's high-resolution player piano system.","Steinway & Sons","2015",ST,
   [("Spirio r","Steinway & Sons","2018","adds recording")]),
 X("PianoDisc / PNOmation retrofit","Conversion kit adding computer playback to an existing piano.","","",PP),
 ]}
kinds=[grand,upright,digital,electric,harps,clavi,player]
def B(n,c,f,seg,d,s,lines=(),sig=(),rel=(),eras=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
    return b
brands=[
 B("Steinway & Sons","United States / Germany","1853","Premium pianos","Piano maker founded in Manhattan by Henry E. Steinway, with factories in New York and Hamburg.",ST,["New York grands","Hamburg grands","Vertegrand uprights","Spirio"],["Steinway Model D","Steinway Model B","Steinway Spirio"]),
 B("Bösendorfer","Austria","1828","Premium pianos","Viennese piano maker founded by Ignaz Bösendorfer; owned by Yamaha since 2008.",BO,["VC grands","Imperial"],["Bösendorfer Imperial 290"],["Yamaha"]),
 B("Fazioli","Italy","1981","Premium pianos","Grand piano maker founded by Paolo Fazioli in Sacile.",FA,[],["Fazioli F278","Fazioli F308"]),
 B("C. Bechstein","Germany","1853","Premium pianos","Berlin piano maker founded by Carl Bechstein.",BE,["Concert","Academy","W. Hoffmann"],["C. Bechstein Concert grands","C. Bechstein Concert 8"]),
 B("Blüthner","Germany","1853","Premium pianos","Leipzig piano maker founded by Julius Blüthner, known for aliquot stringing.",BL,["Blüthner","Haessler"],["Blüthner aliquot grand"]),
 B("Kawai","Japan","1927","Pianos and digital pianos","Hamamatsu piano maker founded by Koichi Kawai.",KA,["Shigeru Kawai","GX BLAK","GL","CA","ES","MP"],["Shigeru Kawai SK-EX","Kawai GX BLAK"]),
 B("Yamaha","Japan","1887","Pianos and electronic instruments","Hamamatsu maker founded by Torakusu Yamaha as a reed-organ builder; first Japanese piano 1900.",YC,["U series","Clavinova","Disklavier","CP"],["Yamaha U1","Yamaha Clavinova","Yamaha Disklavier","Yamaha CP-70"],["Bösendorfer"]),
 B("Steingraeber & Söhne","Germany","1852","Premium pianos","Bayreuth family piano maker founded by Eduard Steingraeber.",SG,[],["Steingraeber concert grand"]),
 B("Pleyel","France","1807","Historical and premium pianos","Paris piano maker founded by Ignace Pleyel; production stopped in 2013 and resumed under Algam in 2017.",PL,[],["Pleyel grand (historical)"],["Érard"]),
 B("Érard","France","","Historical pianos and harps","Paris maker founded by Sébastien Érard, inventor of the double escapement action (1823).",ER,[],["Érard double-escapement grand"],["Pleyel"]),
 B("Rhodes","United States","","Electric pianos","Electric piano brand of Harold Rhodes, made with Fender from 1965.",RH,["Fender Rhodes","Mark 7","Mark 8"],["Rhodes piano"]),
 B("Wurlitzer","United States","","Electric pianos","Maker of reed electric pianos from 1954 to 1983; bought by Baldwin in 1987.",WU,[],["Wurlitzer 200A"]),
 B("Hohner","Germany","1857","Harmonicas, accordions and keyboards","Trossingen instrument maker; built the Clavinet and Pianet.","knowledge",["Clavinet","Pianet"],["Hohner Clavinet D6"]),
 B("Roland","Japan","1972","Electronic instruments","Electronic musical instrument maker.","knowledge",["FP","RD","V-Piano"],[]),
 B("Casio","Japan","1946","Electronics and digital pianos","Electronics maker with Privia and Celviano digital pianos.","knowledge",["Privia","Celviano"],[]),
 B("Clavia","Sweden","","Stage keyboards","Maker of Nord stage pianos and keyboards.","knowledge",["Nord"],[]),
 B("Aeolian","United States","","Player pianos","Maker of the Pianola (1896) and the Duo-Art reproducing piano (1914).",PP,["Pianola","Duo-Art"],["Pianola","Duo-Art"]),
 B("Welte","Germany","","Player pianos","Maker of the Welte-Mignon reproducing piano (1904).",PP,["Welte-Mignon"],["Welte-Mignon"]),
]
notes=("Old 'Acoustic piano' split into Grand piano and Upright piano; its models Yamaha b1, Yamaha U1 (now archetype) and Kawai K 15 moved to Upright piano. "
 "Left out (no retrievable source this session; yamaha.com returned 403): Yamaha CFX, CF4/CF6, C3 and U3 archetypes; Kawai K series as archetype (K 15 kept as model). "
 "Steinway model years not given by the source, so left blank. Harpsichord national schools are maker-free archetypes; no tradition entries added (schools covered as archetypes). "
 "Hohner, Roland, Casio, Clavia brand facts from knowledge.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/E3/shelves/02_00.json'; os.makedirs('work/E3/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
