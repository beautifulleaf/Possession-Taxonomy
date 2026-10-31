import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=(),a='',dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Ukulele","a":"uke","d":"Small four-string plucked lute of the guitar family, developed in Hawaii from Portuguese instruments.",
 "t":["soprano (standard, 13 in scale)","concert (15 in scale, 1920s)","tenor (17 in scale)","baritone (19 in scale, 1940s)","pocket / sopranino","bass","contrabass","six- or eight-string (taropatch)","pineapple body","electro-acoustic"],
 "s":W+"Ukulele","x":[
  X("Madeiran Hawaiian ukulele","The first ukuleles, made in Honolulu by Madeiran cabinet makers from the machete, cavaquinho and rajão.","","1880s","Ukulele",
    [("Manuel Nunes","","1880s","Credited as one of the first makers"),("Augusto Dias","","1880s","Credited as one of the first makers"),("José do Espírito Santo","","1880s","Credited as one of the first makers")],
    dt="soprano size · koa · Madeiran pattern"),
  X("Martin Style 0 soprano","Plain mahogany soprano from Martin's 1920s ukulele boom; the reference American soprano.","Martin","1920s","C._F._Martin_%26_Company",
    [("Style 0 soprano","Martin","c. 1930","Played by Tiny Tim"),("Style 1 soprano","Martin","1950–1960",""),("Martin 3K","Martin","","Koa model shown on the Ukulele article")],
    dt="style number · mahogany or koa · binding and trim level"),
  X("Kamaka pineapple ukulele","Oval-bodied ukulele shape designed by Kamaka, giving a fuller tone than the figure-eight body.","Kamaka","1927","Kamaka_Ukulele",
    [("Pineapple design","Kamaka","1927","Patented 1928"),("Kamaka HF-48","Kamaka","","Eight-string baritone taropatch")],a="pineapple uke",
    dt="soprano to baritone · four, six or eight strings · koa"),
  X("Maccaferri plastic ukulele","Mass-produced moulded-plastic ukulele; about 9 million made.","Mario Maccaferri","late 1940s–late 1960s","Ukulele",dt="plastic body · soprano size"),
 ]},
{"n":"Banjo","a":"five-string banjo · tenor banjo","d":"Plucked lute with a drum-like membrane soundtable on a round frame.",
 "t":["five-string resonator (bluegrass)","five-string open-back (old-time)","tenor (17 or 19 frets)","plectrum (four-string, about 22 frets)","long-neck (Seeger, three extra frets)","six-string banjo guitar","banjo ukulele","banjo mandolin","cello and bass banjo","with or without tone ring"],
 "s":W+"Banjo","x":[
  X("Gibson Mastertone resonator banjo","Gibson's prewar resonator banjo with a heavy flathead tone ring inside the rim; the bluegrass reference.","Gibson","1920s–1930s","Prewar_Gibson_banjo",
    [("Granada RB Mastertone 9584-3","Gibson","1934","Earl Scruggs's banjo; now at the Country Music Hall of Fame"),("RB-4","Gibson","1929",""),("PB-3","Gibson","1929","Plectrum"),("RB-1","Gibson","1933",""),("RB-7","Gibson","1938",""),("RB-11","Gibson","1938",""),("RB-00","Gibson","1940",""),("RB-250","Gibson","1968",""),("Earl Scruggs Standard","Gibson","1984","Nickel-plated replica of Scruggs's Granada"),("RB-75","Gibson","1997","Modern reproduction")],
    a="Mastertone · prewar flathead",dt="RB five-string, TB tenor, PB plectrum · flathead tone ring · gold or nickel plating · original vs conversion neck"),
  X("Vega Tu-ba-Phone","Vega banjo with a perforated metal tone ring between the wooden rim and the head.","Vega","1909","Vega_Company",
    [("Tu-ba-Phone","Vega","1909",""),("Vegaphone Deluxe","Vega","1931","")],a="Tubaphone",dt="five-string or tenor · open-back"),
  X("Vega Pete Seeger long-neck","Long-neck five-string banjo designed for Pete Seeger, with three extra frets for lower keys.","Vega","1950s","Vega_Company",
    [("Pete Seeger model","Vega","1950s–1960s","Later used by the Kingston Trio and the Limeliters")],a="Seeger long neck",dt="open-back · long neck"),
 ]},
{"n":"Mandolin","a":"","d":"Small plucked lute with paired strings, usually tuned in fifths.",
 "t":["A-style (pear-shaped archtop)","F-style (scroll and points)","Neapolitan bowlback","flatback","mandola","octave mandolin","mandocello","electric mandolin"],
 "s":W+"Mandolin","x":[
  X("Gibson F-5","Carved archtop mandolin with f-holes, floating fingerboard and scroll body, designed by Lloyd Loar; the bluegrass reference.","Gibson","1922","Gibson_F-5",
    [("Loar-signed F-5","Gibson","1923–1924","About 326 made; 228 documented by 2010"),("Bill Monroe's F-5, serial 73987","Gibson","1923","Signed by Loar on 9 July 1923"),("'Fern' F-5","Gibson","1920s","Fern peghead inlay; about twenty known"),("F-4","Gibson","c. 1916","Predecessor with a single oval soundhole")],
    a="Lloyd Loar F-5 · Loar",dt="f-holes · scroll and points · Virzi Tone Producer (some) · sunburst"),
  X("Gibson A-style","Pear-shaped carved archtop mandolin without scroll or points.","Gibson","1900s","Mandolin",
    [("A-4","Gibson","1921",""),("A-5","Gibson","1920s","Loar design; one Loar-signed example known")],dt="oval or f-holes · finish"),
  X("Neapolitan bowlback mandolin","Almond-shaped bowl of curved wood strips with eight metal strings in four courses; the classical mandolin.","","18th–19th century","Mandolin",
    [("Vinaccia","","","Naples"),("Calace","","","Naples"),("Embergher","","","Rome (Roman style)")],a="round-back · tater bug",dt="number of ribs · maker · decoration"),
  X("Vega cylinder-back mandolin","Vega mandolin with a cylindrical back.","Vega","1913","Mandolin",[("Cylinder-back","Vega","1913–c. 1927","")]),
 ],
 "m":[["H-2 mandola","Gibson"],["K-4 mandocello","Gibson"],["K-5 mandocello","Gibson"],["Electric mandolin (1992)","Fender"]]},
{"n":"Bouzouki","a":"","d":"Long-necked plucked lute with paired metal strings, Greek or Irish.",
 "t":["three-course (trichordo)","four-course (tetrachordo)","five-course (pentachordo)","flat-back Irish","archtop Irish"],
 "s":W+"Bouzouki","x":[
  X("Greek trichordo bouzouki","Three-course, six-string bowl-backed bouzouki of rebetiko.","","c. 1900","Bouzouki",[("Tsakirian replica","Karolos Tsakirian","","Athens maker")],a="trichordo",dt="bowl back · three courses"),
  X("Greek tetrachordo bouzouki","Four-course, eight-string bouzouki popularised by Manolis Chiotis; the modern Greek standard.","","1956","Bouzouki",a="tetrachordo",dt="bowl back · four courses tuned C F A D"),
  X("Irish bouzouki","Four-course bouzouki with a flatter back, usually tuned GDAD, adapted for Irish music.","","c. 1972","Irish_bouzouki",
    [("Greek tetrachordo in Irish music","","mid-1960s","Introduced by Johnny Moynihan with Sweeney's Men"),("Abnett instrument for Dónal Lunny","Peter Abnett","c. 1972","First built for Irish music; staved back, straight sides")],dt="flat or staved back · archtop or flat top · GDAD"),
 ]},
{"n":"Balalaika","a":"","d":"Russian plucked lute with a triangular body and three strings.",
 "t":["piccolo","prima","secunda","alto","bass","contrabass"],
 "s":W+"Balalaika","x":[
  X("Andreyev orchestral balalaika","Standardised balalaika family built for the balalaika orchestra.","","1880s","Balalaika",
    [("Andreyev standard","","1880s","Developed by Vasily Andreyev with violin maker V. Ivanov"),("Paserbsky chromatic","Paserbsky","","St Petersburg maker; chromatic frets and orchestral sizes")],dt="size in the family · frets"),
 ]},
{"n":"Oud","a":"short-necked fretless lute","d":"Short-necked, fretless, pear-bodied plucked lute.",
 "t":["zenne oud (smaller)","oud arbi (North African, four courses)","oud kumethra","electro-acoustic"],
 "s":"https://salamuzik.com/collections/ouds","x":[
  X("Arabic oud","Larger oud with about 61–62 cm scale and a fuller, deeper sound; Iraqi, Egyptian and Syrian schools.","","","Oud",
    [("Iraqi school","","","Local differences; Munir Bashir its noted master"),("Syrian oud","","",""),("Egyptian oud","","","")],dt="scale 61–62 cm · tuning C F A D G C or F A D G C F"),
  X("Turkish oud","Lighter-built oud of about 58.5 cm scale, tuned about a whole step higher, with a brighter sound.","","","Oud",dt="scale 58.5 cm · unfinished soundboard · Bolahenk tuning"),
  X("Persian barbat","Iranian relative with a smaller body, longer neck and slightly raised fingerboard.","","","Oud",a="barbat"),
 ]},
{"n":"Sitar","a":"long-necked plucked lute","d":"Long-necked plucked lute from India with movable frets and sympathetic strings.",
 "t":["with or without upper tumba","electric sitar"],
 "s":"https://www.sitarmaker.com/","x":[
  X("Ravi Shankar style sitar","Instrumental-style sitar of toon wood, often with a second neck resonator, heavy carving and 13 sympathetic strings.","","","Sitar",a="instrumental style · Kharaj Pancham",dt="toon or teak · tumba · carving and inlay"),
  X("Vilayat Khan style sitar","Gayaki-style sitar built for Vilayat Khan's vocal-like meend technique.","","","Sitar",a="gayaki style"),
 ],
 "m":[["Hiren Roy sitar","Hiren Roy"],["Rikhi Ram sitar","Rikhi Ram"],["Zitar (Niladri Kumar style)",""],["Sitar guitar","Danelectro"]]},
{"n":"Tanpura","a":"tambura · long-necked drone lute","d":"Long-necked unfretted plucked lute from India that sounds a drone on open strings.",
 "t":["male (about 1 m string)","female (about three-quarters size)","electronic tanpura"],
 "s":"https://www.sitarmaker.com/","x":[
  X("Miraj tanpura","Hindustani tanpura with a bottle-gourd body and bone bridge.","","since 1850","Tanpura",dt="gourd · length three to five feet"),
  X("Tanjore tanpura","Carnatic tanpura with a solid jackwood body, no gourd, and rosewood bridge.","","17th century","Tanpura",dt="jackwood"),
 ]},
{"n":"Veena","a":"vina · South Indian long-necked lute","d":"Long-necked fretted plucked lute from India with one or two gourd resonators.",
 "t":["Saraswati veena","Chitra veena (gottuvadhyam)","Rudra veena","Vichitra veena"],
 "s":"https://mufemusicals.com/","x":[
  X("Saraswati veena","Carnatic veena with a jackwood resonator, 24 wax-set frets, four playing and three drone strings, and yali head.","","17th century","Saraswati_veena",
    [("Ekanda veena","","","Built from a single piece of wood"),("Thanjavur veena","","","Thanjavur makers considered the finest"),("Pithapuram and Bobbili veenas","","","Andhra Pradesh centres")],dt="jackwood · 24 frets · yali carving"),
 ]},
{"n":"Pipa","a":"Chinese lute","d":"Chinese pear-shaped four-string plucked lute with many frets.",
 "t":["24-fret modern","fewer-fret antique","steel-wound nylon or silk strings"],
 "s":W+"Pipa","x":[
  X("Modern 24-fret pipa","Pipa with 24 frets laid out for equal temperament, tuned A D E A, played with the fingers.","","1920s–1930s","Pipa",dt="frets 24 or more · strings"),
 ]},
{"n":"Shamisen","a":"three-string lute · samisen","d":"Long-necked, three-string plucked lute from Japan with a skin-covered body.",
 "t":["hosozao (thin neck)","chuzao (middle neck)","futozao (thick neck)","cat, dog or synthetic skin","electric"],
 "s":"https://wagakkistore.com/","x":[
  X("Tsugaru shamisen","Large futozao-based shamisen for the fast, improvised Tsugaru style.","","early 20th century","Shamisen",a="tsugaru-jamisen",dt="futozao · skin · acoustic or electric"),
  X("Nagauta hosozao","Smallest thin-necked shamisen, used for nagauta and kouta.","","","Shamisen"),
  X("Gidayu futozao","Thick-necked shamisen of bunraku puppet theatre.","","","Shamisen"),
  X("Heike shamisen","Short-necked shamisen built for the folk tune Heike Ondo.","","","Shamisen",dt="steel strings · plastic skin"),
 ]},
{"n":"Charango","a":"","d":"Small Andean lute with ten strings in five courses.",
 "t":["armadillo-shell back","wooden bowl back","ronroco (baritone)","walaycho (small)","charangón (tenor)"],
 "s":W+"Charango","x":[
  X("Andean charango","Ten-string, five-course charango tuned G C E A E, traditionally with an armadillo-shell back.","","early 18th century","Charango",dt="armadillo or wood · Bolivian or Peruvian"),
 ]},
]
brands=[
 {"n":"Gibson","c":"United States","f":"1902","seg":"guitars, mandolins, banjos","d":"Kalamazoo-founded maker of the F-5 mandolin and Mastertone banjo.","lines":[],"eras":[],"sig":["Gibson F-5","Gibson Mastertone resonator banjo"],"sc":["bluegrass"],"rel":[],"s":W+"Mandolin"},
 {"n":"Martin","c":"United States","f":"1833","seg":"acoustic guitars, ukuleles","d":"Nazareth, Pennsylvania guitar maker that added ukuleles in the 1920s.","lines":[],"eras":[],"sig":["Martin Style 0 soprano"],"sc":[],"rel":["Vega"],"s":W+"C._F._Martin_%26_Company"},
 {"n":"Kamaka","c":"United States","f":"1916","seg":"ukuleles","d":"Honolulu ukulele maker founded by Samuel Kamaka Sr.; inventor of the pineapple ukulele.","lines":[],"eras":[],"sig":["Kamaka pineapple ukulele"],"sc":["Hawaiian"],"rel":[],"s":W+"Kamaka_Ukulele"},
 {"n":"Vega","c":"United States","f":"1881","seg":"banjos, mandolins","d":"Boston maker founded by Julius and Carl Nelson; name owned by Deering since 1989.","lines":["Tu-ba-Phone","Vegaphone"],"eras":["Martin ownership, 1970s","Deering, from 1989"],"sig":["Vega Tu-ba-Phone","Vega Pete Seeger long-neck"],"sc":["folk revival"],"rel":["Martin"],"s":W+"Vega_Company"},
 {"n":"Mario Maccaferri","c":"","f":"","seg":"plastic instruments","d":"Maker of about 9 million inexpensive plastic ukuleles, late 1940s to late 1960s.","lines":[],"eras":[],"sig":["Maccaferri plastic ukulele"],"sc":[],"rel":[],"s":W+"Ukulele"},
 {"n":"Hiren Roy","c":"India","f":"","seg":"sitar maker","d":"Kolkata sitar maker whose older instruments are collectible.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Rikhi Ram"],"s":W+"Sitar"},
 {"n":"Rikhi Ram","c":"India","f":"","seg":"sitar maker","d":"Delhi sitar maker whose older instruments are collectible.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Hiren Roy"],"s":W+"Sitar"},
]
trads=[
 {"n":"Miraj instrument making","g":"Musical instruments","r":"Miraj, Maharashtra, India","p":"since 1850","d":"Family workshops making tanpuras and sitars for over seven generations, regarded as the finest tanpura makers.","tech":"gourd resonators dried for a year; about three weeks per tanpura","mat":"bottle gourd, wood, bone","forms":["Miraj tanpura","sitar"],"ctr":["Miraj sitar-maker family"],"auth":"","s":W+"Tanpura"},
 {"n":"Thanjavur veena making","g":"Musical instruments","r":"Thanjavur, Tamil Nadu, India","p":"17th century to present","d":"Making of the 24-fret Saraswati veena, linked to the court of Raghunatha Nayak.","tech":"resonator hollowed from a log; frets set in wax","mat":"jackfruit wood, brass or bell-metal frets, steel strings","forms":["Saraswati veena","ekanda veena"],"ctr":["Thanjavur","Pithapuram","Bobbili"],"auth":"","s":W+"Saraswati_veena"},
]
notes=("Oud: dropped the four retailer SKUs (Miras UNQ-2A, Sala AAO-108, AO-101M, OUDE EA5) per the brief; Arabic/Syrian/Turkish models became archetypes. "
 "Banjo/mandolin old models (plectrum, tenor, A-style, F-style) became types. Kinds whose old s was a concertina shop page now cite Wikipedia. "
 "Not done for lack of a confirming retrieved page: Vega Whyte Laydie, Gibson RB-3/Granada as a separate line, Kamaka HF model numbers, Martin Styles 2/3/5K, Kanailal sitars, Danelectro Coral electric sitar year, Greek/Turkish oud makers (Nahat, Manol), Naleykin balalaikas, pipa makers. Wikidata returned HTTP 429.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/E3/shelves/05_00.json'; tmp=p+'.tmp'
json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,p)
