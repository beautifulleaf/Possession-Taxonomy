import json, os
W='https://en.wikipedia.org/wiki/'
MAR=W+'Marimba'; VIB=W+'Vibraphone'; XYL=W+'Xylophone'; GLO=W+'Glockenspiel'; TIM=W+'Timpani'
M1='https://www.marimbaone.com/'; KD='https://www.kettledrummer.com/?p=561'
M55='https://connselmer.com/instruments/mallet-instruments/musser-pro-vibe-vibraphone-m55b'
def v(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Marimba","a":"concert marimba","d":"Tuned mallet percussion instrument with wooden bars and resonators.",
 "t":["4.3 octave (A2–C7)","4.5 octave (F2–C7)","5 octave (C2–C7)","rosewood bars","padauk bars","synthetic bars (Kelon, Klyperon, Acoustalon)","tube resonators","box or oval-bottom resonators"],
 "s":"https://www.shopnemc.com/category/500",
 "x":[
  {"n":"Central American chromatic double-keyboard marimba","a":"marimba doble · marimba de tecomates (gourd forerunner)","d":"Chromatic marimba with two keyboard rows, developed in Mexico and Guatemala from African-derived gourd marimbas.","mk":"","y":"1892–1894","s":MAR,
   "v":[v("Double-keyboard marimba (Chiapas)","Corazón de Jesús Borras Moreno","1892","first played publicly 1897"),v("Chromatic double-keyboard marimba (Quetzaltenango)","Sebastián Hurtado","1894","Guatemala's national instrument")],
   "dt":"gourd, carved wood or tube resonators · played by several players"},
  {"n":"Deagan concert marimba","a":"Century of Progress Model","d":"American concert marimba with metal tube resonators adapting the Latin American instrument for Western music.","mk":"J. C. Deagan","y":"1930s","s":W+"Clair_Omar_Musser",
   "v":[v("Century of Progress Model","J. C. Deagan","","designed by Clair Omar Musser")],
   "dt":"metal tube resonators · rosewood bars"},
  {"n":"Marimba One concert marimba","a":"","d":"Hand-built Californian concert marimbas with box-shaped resonators, the best-known modern professional line.","mk":"Marimba One","y":"","s":M1,
   "v":[v("3100","Marimba One","","Basso Bravo resonator option"),v("Izzy","Marimba One"),v("Wave","Marimba One","","4.6 octave (low E) and 5.0 octave; rosewood or Horizon synthetic keyboard"),v("Motif","Marimba One","","4.3 octave; rosewood or Horizon synthetic"),v("Educational Series","Marimba One","","3.0, 4.3 and 5.0 octave, padauk")],
   "dt":"3.0–5.5 octave · rosewood, padauk or synthetic keyboard · resonator options"}],
 "m":[["Musser concert marimba","Musser"],["Yamaha concert marimba","Yamaha"],["Adams concert marimba","Adams"]]},
{"n":"Vibraphone","a":"vibes · vibraharp","d":"Tuned mallet percussion with metal bars, resonators and motor-driven vibrato fans, with a damper pedal.",
 "t":["3 octave (F3–F6)","3.5 octave","4 octave","silver bars","gold bars","black bars","variable-speed motor","portable frame"],
 "s":"https://www.shopnemc.com/category/500",
 "x":[
  {"n":"Leedy vibraphone","a":"","d":"The first vibraphone: steel bars with motor-driven rotating discs under the bars, no damper pedal.","mk":"Leedy","y":"1921","s":VIB,
   "v":[v("Three-octave steel marimba experiments","Leedy","1916","Herman E. Winterhoff"),v("Vibraphone as marketed","Leedy","1924","steel bars, no pedal; name by George H. Way")],
   "dt":"steel bars · motor-driven discs"},
  {"n":"Deagan Vibraharp","a":"vibraharp","d":"Aluminium-bar vibraphone with a foot damper, the template for later vibraphones.","mk":"J. C. Deagan","y":"1927","s":VIB,
   "v":[v("Vibraharp","J. C. Deagan","1927","designed by Henry Schluter")],
   "dt":"aluminium bars · damper pedal · motor"},
  {"n":"Musser Pro-Vibe","a":"M55","d":"Three-octave professional vibraphone with hand-tuned bars, arched mitred resonators and a quiet variable-speed motor.","mk":"Musser","y":"","s":M55,
   "v":[v("M55","Musser","","silver powder-coat bars"),v("M55G","Musser","","gold satin bars"),v("M55B","Musser","","black bars")],
   "dt":"3 octave · A=442 · bar finish silver, gold or black · swivelling sustain pedal"}],
 "m":[["Musser M58/M58M Piper Vibe","Musser"]]},
{"n":"Xylophone","a":"concert xylophone","d":"Tuned mallet percussion with hard wooden or synthetic bars, brighter and higher than the marimba.",
 "t":["3.5 octave","4 octave","rosewood bars","padauk bars","synthetic (fibreglass) bars","classroom (Orff) xylophone, about 1.5 octaves"],
 "tg":["baby"],"s":"https://www.shopnemc.com/category/500",
 "x":[
  {"n":"Orchestral xylophone","a":"concert xylophone","d":"Chromatic keyboard xylophone with a high, dry tone, used in orchestras since the 1870s.","mk":"","y":"1874","s":XYL,
   "v":[v("Concert xylophone, 3.5 octave","Marimba One"),v("Concert xylophone, 4.0 octave","Marimba One")],
   "dt":"3.5–4 octave · rosewood, padauk, cocobolo or synthetic bars"},
  {"n":"Balafon","a":"","d":"West African frame xylophone whose wooden bars sit on gourd resonators.","mk":"","y":"","s":XYL,"v":[],"dt":"gourd resonators · number of keys"},
  {"n":"Gyil","a":"","d":"Pentatonic 14-key xylophone of the Gur-speaking peoples of Ghana, Burkina Faso and Ivory Coast.","mk":"","y":"","s":XYL,"v":[],"dt":"14 keys · gourd resonators"},
  {"n":"Amadinda","a":"","d":"Ugandan log xylophone of twelve pentatonically tuned logs played by three players.","mk":"","y":"","s":XYL,"v":[],"dt":"12 logs"}]},
{"n":"Glockenspiel","a":"orchestra bells · bell lyre · lyra","d":"Metallophone of tuned steel or aluminium bars in a keyboard layout, sounding two octaves above written pitch.",
 "t":["2.5 octave","3 octave","3.5 octave","steel bars","aluminium bars","with sustain pedal","toy glockenspiel"],
 "tg":["baby"],"s":GLO,
 "x":[
  {"n":"Orchestral glockenspiel","a":"orchestra bells","d":"Horizontally mounted bar glockenspiel played with mallets; larger sets have a sustain pedal.","mk":"","y":"19th century","s":GLO,
   "v":[v("Parsifal bells (with resonator)","J. C. Deagan","1918–1932","pattern for later professional models"),v("Professional glockenspiel on the Deagan pattern","Adams"),v("Professional glockenspiel on the Deagan pattern","Yamaha")],
   "dt":"2.5–3.5 octave · steel or aluminium bars · case or frame"},
  {"n":"Bell lyre","a":"lyra-glockenspiel · Stahlspiel · Militär-Glockenspiel","d":"Marching-band glockenspiel in a lyre-shaped frame, carried on a strap and played vertically.","mk":"","y":"mid-19th century","s":GLO,"v":[],"dt":"vertical or horizontal · strap or frame"}],
 "m":[["Malletech glockenspiel","Malletech"]]},
{"n":"Timpani","a":"kettledrums","d":"Tuned kettle drum with a bowl-shaped shell, played with mallets.",
 "t":["32, 29, 26, 23 in standard set","piccolo timpano (about 20 in)","copper bowl","fibreglass bowl","aluminium bowl","calfskin head","plastic head","ratchet clutch","friction clutch","chain or cable tuning","German or American set-up"],
 "s":"https://www.shopnemc.com/category/500",
 "x":[
  {"n":"Dresden pedal timpani","a":"Dresden timpani","d":"Pedal timpani with the pedal on the player's side, worked by ankle motion; the first pedal timpani.","mk":"","y":"1870s","s":TIM,
   "v":[v("Ludwig Dresden model","Ludwig","","top of the Ludwig line; suspended bowls after about 1973")],
   "dt":"copper bowl · calfskin or plastic head · clutch type"},
  {"n":"Balanced-action pedal timpani","a":"floating pedal","d":"Pedal timpani whose head tension is balanced by a spring, so no clutch is needed.","mk":"Ludwig","y":"","s":KD,
   "v":[v("Balanced action timpani","Ludwig","ca. 1935"),v("Universal","Ludwig","late 1930s"),v("Standard Symphony","Ludwig","early 1950s"),v("Professional Symphonic","Ludwig","1970","suspended kettles and extended collar heads after about 1973"),v("Grand Symphonic","Ludwig"),v("Professional","Ludwig")],
   "dt":"copper or fibreglass bowl · 20–32 in"},
  {"n":"Berlin-style (Ringer) pedal timpani","a":"Ringer timpani","d":"Pedal on the far side worked by a long arm and the whole leg.","mk":"","y":"","s":TIM,
   "v":[v("Ringer-type timpani","Ludwig","ca. 1973","made from Günter Ringer's plans")],"dt":"copper bowl · calfskin head"},
  {"n":"Viennese timpani","a":"Schnellar system","d":"Handle-tuned timpani in which the bowl moves against a fixed head.","mk":"","y":"","s":TIM,
   "v":[v("Pedal-operated Viennese timpani","Adams")],"dt":"calfskin head · copper bowl"},
  {"n":"Machine timpani","a":"handle or spider timpani","d":"Timpani tuned by a single handle that tightens all tension rods at once.","mk":"","y":"1812","s":TIM,"v":[],"dt":"handle or chain"}],
 "m":[["Yamaha 4200 series timpani","Yamaha"],["Yamaha 6200 series timpani","Yamaha"],["Yamaha 7200 series timpani","Yamaha"]],
 "r":[["Big Sound","Adams"]]}]
brands=[
 {"n":"J. C. Deagan","c":"United States","f":"1880","seg":"Historic mallet percussion","d":"St Louis, later Chicago, maker of xylophones, marimbas, vibraharps, chimes and glockenspiels; mark sold to Yamaha in 1986.","lines":["Vibraharp","Century of Progress marimba","Parsifal bells"],"eras":["John Calhoun Deagan, founder, 1880","Clair Omar Musser, mallet division, from 1930","Slingerland, 1977–1984","Yamaha, from 1986"],"sig":["Deagan Vibraharp","Deagan concert marimba"],"sc":[],"rel":["Musser","Yamaha","Leedy"],"s":W+"J._C._Deagan,_Inc."},
 {"n":"Leedy","c":"United States","f":"1902","seg":"Historic drums and percussion","d":"Indianapolis drum maker that introduced the vibraphone; sold to Conn in 1929, rights now with Gretsch.","lines":["Vibraphone"],"eras":["Ulysses G. Leedy, 1897–1929","C. G. Conn, from 1929","Slingerland, from 1955","Gretsch, from 1986"],"sig":["Leedy vibraphone"],"sc":[],"rel":["J. C. Deagan","Ludwig"],"s":W+"Leedy_Manufacturing_Company"},
 {"n":"Musser","c":"United States","f":"","seg":"Professional mallet percussion","d":"Mallet-instrument maker founded by Clair Omar Musser after leaving Deagan; owned by Ludwig since 1965.","lines":["Pro-Vibe","marimbas","xylophones","glockenspiels","chimes"],"eras":["Clair Omar Musser, founder","Lyons, 1956","Ludwig, from 1965"],"sig":["Musser Pro-Vibe"],"sc":[],"rel":["Ludwig","J. C. Deagan"],"s":W+"Clair_Omar_Musser"},
 {"n":"Marimba One","c":"United States","f":"","seg":"Professional marimbas","d":"Arcata, California maker of concert marimbas and xylophones.","lines":["3100","Izzy","Wave","Motif","Educational Series"],"eras":[],"sig":["Marimba One concert marimba"],"sc":[],"rel":[],"s":M1},
 {"n":"Ludwig","c":"United States","f":"1910","seg":"Drums and orchestral percussion","d":"Drum maker founded by William F. Ludwig Sr. and his brother Theobald; known for balanced-action timpani.","lines":["Dresden","Grand Symphonic","Professional Symphonic","Universal","Standard Symphony"],"eras":["William F. Ludwig Sr., from 1910"],"sig":["Balanced-action pedal timpani"],"sc":[],"rel":["Musser","Leedy"],"s":"https://pas.org/?p=8094"},
 {"n":"Adams","c":"Netherlands","f":"1970","seg":"Professional percussion and brass","d":"Ittervoort maker of timpani, marimbas, xylophones, vibraphones and brass, founded by André Adams.","lines":["Big Sound timpani"],"eras":["André Adams, from 1970"],"sig":["Viennese timpani"],"sc":[],"rel":[],"s":W+"Adams_Musical_Instruments"},
 {"n":"Yamaha","c":"Japan","f":"1887","seg":"Budget to premium","d":"Japanese instrument maker with full lines of timpani and mallet percussion; owns the Deagan mark.","lines":["4200, 6200, 7200 timpani"],"s":"knowledge"}]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"All five planned kinds kept; Glockenspiel added (new, sourced). Old Marimba One models became versions; Ludwig Grand Symphonic/Professional became versions of the balanced-action archetype (the Grand Symphonic maker page returned 403, so no specs); Yamaha timpani series kept in m, duplicate r list dropped. Generic Musser/Yamaha/Adams marimba entries kept in m without model names because no model page was retrieved. No years given where pages lacked them (Musser founding, M55 introduction, balanced-action invention year). No traditions: Guatemalan marimba and African xylophones are covered as archetypes; a tradition entry could be added by the world-percussion shelf."}
p='work/E3/shelves/03_03.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
