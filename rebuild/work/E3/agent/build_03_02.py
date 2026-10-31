import json, os
W='https://en.wikipedia.org/wiki/'
K=[]
K.append({"n":"Djembe","a":"jembe · goblet drum","d":"Rope-tuned goblet drum carved from one log with a goatskin head, played with bare hands; from Mandinka West Africa.",
 "t":["carved hardwood shell (lenke, djalla, iroko…)","goatskin head","cowhide head","synthetic head (FiberSkyn)","rope tuning (Mali weave)","lug tuning","fibreglass shell","14 in head","12 in head"],
 "s":W+"Djembe","m":[]})
K.append({"n":"Conga","a":"tumbadora · conga drum","d":"Tall barrel-shaped Afro-Cuban hand drum with a single head, usually played in sets of two or three.",
 "t":["requinto","quinto (about 11 in)","conga / tres dos (about 11.75 in)","tumba (about 12.5 in)","supertumba (up to 14 in)","staved wood shell","fibreglass shell","rawhide head","synthetic head"],
 "s":W+"Conga",
 "x":[{"n":"LP fibreglass conga","a":"","d":"Martin Cohen's louder, road-durable fibreglass-shell conga; adopted by Carlos \"Patato\" Valdés, which established it.","mk":"Latin Percussion","y":"","s":"https://pas.org/martin-cohen/","v":[],"dt":"quinto · conga · tumba · shell colours"}]})
K.append({"n":"Bongos","a":"bongo drums · bongó","d":"Pair of small open-bottomed drums joined by a bridge, the smaller macho and larger hembra, from eastern Cuba.",
 "t":["wood shells","fibreglass shells","calfskin heads","synthetic heads","lug tuning","tacked heads (flame-tuned)"],
 "s":W+"Bongo_drum",
 "x":[{"n":"LP original bongos","a":"","d":"Hand-made mahogany bongos that were Martin Cohen's first instrument and the start of Latin Percussion.","mk":"Latin Percussion","y":"1964","s":"https://pas.org/martin-cohen/","v":[],"dt":"mahogany shells · rawhide heads"}]})
K.append({"n":"Cajon","a":"cajón · box drum","d":"Box-shaped wooden drum played by hand while the player sits on it; from Afro-Peruvian music, later adopted in flamenco.",
 "t":["Peruvian (no snares)","snare / flamenco cajon (wires or strings)","adjustable snare","bass port","kids' size","stave or round-back body","pedal-played cajon"],
 "s":W+"Cajón",
 "x":[
  {"n":"Peruvian cajón","a":"cajón peruano","d":"Plain resonant box with a sound hole and no snares, the original Afro-Peruvian form; declared Peruvian National Heritage in 2001.","mk":"","y":"19th century","s":W+"Cajón","v":[],"dt":"plywood or hardwood · tapa thickness"},
  {"n":"Flamenco cajón","a":"snare cajón","d":"Cajón with guitar strings or wires behind the playing face; entered flamenco after Paco de Lucía brought one from Lima in 1977.","mk":"","y":"1977","s":W+"Cajón","v":[],"dt":"string or wire snares · fixed or adjustable"},
  {"n":"Schlagwerk Cajon la Peru","a":"","d":"Schlagwerk's Peruvian-style cajón line.","mk":"Schlagwerk","y":"","s":"https://boullard.ch/en/brand/schlagwerk-percussion","v":[{"n":"CP4005","mk":"Schlagwerk","y":"","d":""},{"n":"CP4007","mk":"Schlagwerk","y":"","d":""}],"dt":"front-plate woods"},
  {"n":"Schlagwerk 2inOne","a":"","d":"Schlagwerk's snare cajón with switchable snare sound.","mk":"Schlagwerk","y":"","s":"https://boullard.ch/en/brand/schlagwerk-percussion","v":[{"n":"CP404BLK, large, black edition","mk":"Schlagwerk","y":"","d":""},{"n":"2inOne Deluxe Makassar (CP432)","mk":"Schlagwerk","y":"","d":""}],"dt":"size · front-plate finish"},
  {"n":"De Gregorio DrumBox","a":"","d":"De Gregorio cajón designed for use with a pedal.","mk":"De Gregorio","y":"2013","s":"https://drummerszone.com/brands/profile/1389/dg-de-gregorio","v":[],"dt":""}],
 "m":[["Latin Percussion Aspire Accent cajon","Latin Percussion"],["Latin Percussion Gio Stave cajon","Latin Percussion"],["Latin Percussion Round Back Bass cajon","Latin Percussion"],["Meinl Headliner snare cajon","Meinl"],["Meinl Snarecraft Professional 100 cajon","Meinl"],["Schlagwerk Super Agile cajon","Schlagwerk"],["Schlagwerk High Five kids cajon","Schlagwerk"],["De Gregorio Compass cajon","De Gregorio"]]})
K.append({"n":"Tabla","a":"tabla pair · dayan and bayan","d":"Hindustani pair of hand drums: a wooden treble dayan and a metal or clay bass bayan, each with black syahi paste.",
 "t":["dayan in teak or rosewood","bayan in brass","bayan in copper","bayan in aluminium or steel","bayan in clay","bayan in wood (Punjab)"],
 "s":W+"Tabla"})
K.append({"n":"Darbuka","a":"darabuka · doumbek · tarabuka · goblet drum","d":"Single-headed goblet drum of North Africa, the Middle East and the Balkans, held under the arm.",
 "t":["clay / pottery body","wooden body","metal body","goatskin or fish-skin head","synthetic head"],
 "s":W+"Goblet_drum",
 "x":[{"n":"Egyptian-style darbuka","a":"tabla (Egypt)","d":"Darbuka with rounded edges around the head, suited to rapid rolls.","mk":"","y":"","s":W+"Goblet_drum","v":[],"dt":"size · body material · finish"},
      {"n":"Turkish-style darbuka","a":"","d":"Darbuka with an exposed head edge, allowing finger-snapping techniques.","mk":"","y":"","s":W+"Goblet_drum","v":[],"dt":"size · body material"}]})
K.append({"n":"Frame drum","a":"hand frame drum","d":"Drum whose head is wider than its shallow round frame is deep, with or without jingles.",
 "t":["bodhrán (Ireland)","riq (Arab world, with jingles)","tar (Middle East, North Africa)","daf (Iran, Kurdistan)","bendir (North Africa, with snares)","tambourine","pandeiro (Brazil)","kanjira (India)","tamborim (Brazil)","Sámi drum"],
 "s":W+"Frame_drum",
 "x":[{"n":"Tunable bodhrán","a":"","d":"Bodhrán with an internal tone ring tightened by screws, invented by Seamus O'Kane, making it resistant to humidity.","mk":"","y":"1975","s":W+"Bodhrán","v":[{"n":"Hex-key mechanical tuning","mk":"","y":"","d":"drum-kit-style tuning on modern professional drums"}],"dt":"35–45 cm head · 9–20 cm depth · goatskin or synthetic"}]})
K.append({"n":"Handpan","a":"hang drum · pantam","d":"Steel instrument of two glued half-shells with a central note ringed by seven or more tuned fields, played with the hands.",
 "t":["scale (number of notes)","nitrided or stainless steel","bottom notes"],
 "s":W+"Handpan",
 "x":[{"n":"Hang","a":"","d":"The original handpan by Felix Rohner and Sabina Schärer, shown at Frankfurt in 2001; production ended in 2013.","mk":"PANArt","y":"2001","s":W+"Hang_(instrument)",
   "v":[{"n":"First generation","mk":"PANArt","y":"2001–2005","d":"many scales, up to 45 sound models; Low Hang 2005"},{"n":"Second generation","mk":"PANArt","y":"2006–2007","d":"brass coating and brass ring"},{"n":"Integral Hang","mk":"PANArt","y":"2008","d":"single scale, seven tone fields"},{"n":"Free Integral Hang","mk":"PANArt","y":"2010","d":"no brass ring, tuned without electronic tuners"}],
   "dt":"scale · generation"}]})
K.append({"n":"Tongue drum","a":"steel tongue drum · hank drum · tank drum · slit drum","d":"Steel or wooden drum with cut tuned tongues struck by hand or mallet.",
 "t":["steel","wood (slit drum)","number of tongues","scale"],
 "s":W+"Steel_tongue_drum",
 "x":[{"n":"Hank drum","a":"tank drum","d":"Steel tongue drum cut from a propane tank, first made by Dennis Havlena after the Hang's note layout.","mk":"","y":"2007","s":W+"Steel_tongue_drum","v":[],"dt":"tank size · tongue count"}]})
K.append({"n":"Kalimba and mbira","a":"thumb piano · lamellophone · sansa","d":"Plucked instrument with metal tongues fixed over a board or box, played with the thumbs.",
 "t":["board","box resonator","gourd resonator (deze)","number of keys","diatonic or chromatic"],
 "s":W+"Mbira",
 "x":[{"n":"Mbira dzavadzimu","a":"","d":"Shona mbira of Zimbabwe with 22–28 keys in three registers on a hardwood board, often played in a calabash deze.","mk":"","y":"","s":W+"Mbira","v":[],"dt":"22–28 keys · deze resonator"},
      {"n":"Mbira nyunga nyunga","a":"","d":"Fifteen-key mbira from Manicaland in two rows, without a soundboard hole.","mk":"","y":"","s":W+"Mbira","v":[],"dt":"15 keys"},
      {"n":"Matepe","a":"","d":"Twenty-six-key mbira of the Zimbabwe–Mozambique border region.","mk":"","y":"","s":W+"Mbira","v":[],"dt":"26 keys"},
      {"n":"Hugh Tracey kalimba","a":"","d":"Diatonic kalimba tuned in G, based on the nyunga nyunga; it made 'kalimba' the Western name for the instrument.","mk":"Hugh Tracey","y":"mid-1950s","s":W+"Mbira","v":[],"dt":"key count · box or board"}]})
K.append({"n":"Singing bowl","a":"standing bell · Himalayan bowl · Tibetan singing bowl","d":"Standing bowl bell sounded by striking or rubbing the rim; one made for a rite is in Religious & Ceremonial Objects.",
 "t":["bell bronze","crystal (quartz) bowl","hand-hammered","cast","diameter"],
 "s":W+"Singing_bowl",
 "x":[{"n":"Himalayan singing bowl","a":"Tibetan singing bowl","d":"Bell-metal bowl from Nepal or northern India played by rotating a mallet round the rim; reached the West in the early 1970s.","mk":"","y":"1970s (in the West)","s":W+"Singing_bowl","v":[],"dt":"diameter · hammered or cast"},
      {"n":"Rin","a":"kin","d":"Japanese standing bell for Buddhist temples and home altars.","mk":"","y":"","s":W+"Singing_bowl","v":[],"dt":"temple or home-altar size"},
      {"n":"Crystal singing bowl","a":"","d":"Bowl formed from crushed synthetic crystal, a modern form.","mk":"","y":"","s":W+"Singing_bowl","v":[],"dt":"diameter · note"}]})
K.append({"n":"Bar chimes","a":"mark tree · chime tree","d":"Row of hanging metal bars or tubes swept or struck for a shimmering effect.",
 "t":["number of bars","single or double row","aluminium or brass bars"],
 "s":"https://meinlpercussion.com/en/products/ch27-m8532.html",
 "x":[{"n":"Mark tree","a":"nail tree","d":"Graded small chimes hung from a bar for glissandos, devised by studio percussionist Mark Stevens and named by Emil Richards.","mk":"","y":"1967","s":W+"Mark_tree","v":[],"dt":"bar count · length"}],
 "m":[["Meinl bar chimes","Meinl"]]})
B=[
 {"n":"Latin Percussion","c":"United States","f":"1964","seg":"Hand percussion","d":"Martin Cohen's New York firm, maker of congas, bongos, cajons and inventor of the Vibraslap; owned by Drum Workshop since 2014.","lines":[],"sig":["LP original bongos","LP fibreglass conga"],"rel":["Meinl"],"s":W+"Latin_Percussion"},
 {"n":"Schlagwerk","c":"Germany","f":"1982","seg":"Cajons and wooden percussion","d":"Founded by Gerhard Priel and Bengt Schumacher, first making slit drums, now a major cajón maker.","lines":[],"sig":["Schlagwerk Cajon la Peru","Schlagwerk 2inOne"],"rel":[],"s":"https://boullard.ch/en/brand/schlagwerk-percussion"},
 {"n":"De Gregorio","c":"Spain","f":"2002","seg":"Cajons","d":"DG Percussion, founded by percussionist Paolo De Gregorio, maker of flamenco cajons.","lines":[],"sig":["De Gregorio DrumBox"],"rel":[],"s":"https://drummerszone.com/brands/profile/1389/dg-de-gregorio"},
 {"n":"Meinl","c":"Germany","f":"1951","seg":"Cymbals and hand percussion","d":"German family maker of cymbals and a wide range of hand percussion, cajons and sound effects.","lines":[],"sig":[],"rel":["Latin Percussion"],"s":"knowledge"},
 {"n":"PANArt","c":"Switzerland","f":"","seg":"Handpans","d":"Bern firm of Felix Rohner and Sabina Schärer (PANArt Hangbau AG) that created the Hang.","lines":[],"sig":["Hang"],"rel":[],"s":W+"Hang_(instrument)"},
 {"n":"Hugh Tracey","c":"South Africa","f":"","seg":"Kalimbas","d":"Kalimbas named after ethnomusicologist Hugh Tracey, hand-made in a family-run workshop in Grahamstown.","lines":[],"sig":["Hugh Tracey kalimba"],"rel":[],"s":W+"Hugh_Tracey"}]
G="Musical instruments"
T=[
 {"n":"Mandinka djembe","g":G,"r":"West Africa (Guinea, Mali, Burkina Faso, Ivory Coast, Senegal, Gambia)","p":"Mali Empire era to present","d":"Goblet drum linked to the Numu blacksmith caste of the Mandinka, spread worldwide by national ballets.","tech":"single-log carving with hand tools; rope tuning with Mali weave","mat":"lenke, djalla, iroko and other hardwoods; goatskin","forms":["Djembe"],"ctr":["Les Ballets Africains (Guinea)"],"auth":"one-piece hand-carved hardwood shell and rawhide head versus factory softwood or fibreglass with synthetic heads","s":W+"Djembe"},
 {"n":"Afro-Cuban drums","g":G,"r":"Cuba","p":"late 19th century to present","d":"Conga and bongo drums developed by Afro-Cuban musicians from Bantu and Yoruba ancestors.","tech":"staved shells; tacked flame-tuned heads, then screw-lug tuning from the 1940s–50s","mat":"wood, calfskin","forms":["Conga","Bongos"],"ctr":["Cándido Requena","Vergara brothers","Carlos \"Patato\" Valdés"],"auth":"","s":W+"Conga"},
 {"n":"Afro-Peruvian cajón","g":G,"r":"Coastal Peru","p":"colonial era, peak by 1850","d":"Box drum developed by enslaved Africans in coastal Peru; Peruvian National Heritage since 2001.","tech":"resonant box with a sound hole, played seated","mat":"wood","forms":["Cajon"],"ctr":["Caitro Soto"],"auth":"no snares; plain resonant box","s":W+"Cajón"},
 {"n":"Hindustani tabla","g":G,"r":"Indian subcontinent","p":"18th century to present","d":"Paired hand drums of Hindustani classical music, taught through gharanas.","tech":"layered syahi paste of starch and black powder on laced heads","mat":"teak or rosewood dayan; brass, copper or clay bayan; goatskin","forms":["Tabla"],"ctr":["Delhi","Lucknow","Ajrara","Farukhabad","Benares","Punjab gharanas"],"auth":"quality of the syahi is the main mark of a good instrument","s":W+"Tabla"},
 {"n":"Shona mbira","g":G,"r":"Zimbabwe and Malawi","p":"traditional to present","d":"Making and playing of mbira, on UNESCO's Representative List of Intangible Cultural Heritage since 2020.","tech":"forged metal keys on a hardwood soundboard, played in a calabash resonator","mat":"hardwood, metal, gourd","forms":["Kalimba and mbira"],"ctr":[],"auth":"","s":W+"Mbira"},
 {"n":"Irish bodhrán","g":G,"r":"Ireland","p":"1960s revival to present","d":"Goatskin frame drum popularised by Seán Ó Riada and the Chieftains in Irish traditional music.","tech":"skin tacked to a bent frame; played with a tipper","mat":"goatskin, ash, holly or hickory tippers","forms":["Frame drum"],"ctr":["Seamus O'Kane","Paraic McNeela","Caramel Tobin"],"auth":"","s":W+"Bodhrán"},
 {"n":"Himalayan singing bowls","g":G,"r":"Nepal, northern India, Himalaya","p":"modern trade since the 1970s","d":"Bell-metal standing bowls sold in the West as Tibetan bowls, played by rubbing or striking.","tech":"hammering or casting bell metal","mat":"copper–tin bell bronze","forms":["Singing bowl"],"ctr":[],"auth":"claims of seven metals are not supported by analysis","s":W+"Singing_bowl"}]
notes=("All 12 planned kinds kept. Old source pages replaced by retrieved Wikipedia pages where kinds were rewritten; Bar chimes keeps its old Meinl page. "
 "Cajon SKU list trimmed from 10 to 8 market models (LP, Meinl, Schlagwerk, De Gregorio); Schlagwerk La Peru and 2inOne models moved into archetypes. "
 "Left out (could not confirm from a retrieved page): LP conga line names and years (Classic, Galaxy, Patato model), Pantheon Steel Halo and other handpan makers, "
 "named tongue-drum makers, djembe and tabla maker brands, Schlagwerk model years, AMI founding year. Riq page redirected to Daf, so riq is a type sourced to Frame drum.")
out={"kinds":K,"brands":B,"traditions":T,"notes":notes}
p='work/E3/shelves/03_02.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
