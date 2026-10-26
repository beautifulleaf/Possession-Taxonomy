import json, os
W='https://en.wikipedia.org/wiki/'
CF=W+'Western_concert_flute'; REC=W+'Recorder_(musical_instrument)'
HAY=W+'William_S._Haynes_Flute_Company'; POW=W+'Powell_Flutes'; MUR=W+'Muramatsu_Flutes'
MIY='https://johnpacker.co.uk/pages/miyazawa'; PRL=W+'Pearl_Flutes'; BRN=W+'Brannen_Brothers'
MOE=W+'Moeck_Musikinstrumente_%2B_Verlag'; MOL=W+'Conrad_Mollenhauer_GmbH'; KUNG=W+'K%C3%BCng_Blockfl%C3%B6ten_GmbH'
AUL='https://johnpacker.co.uk/pages/aulos'
def v(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Flute","a":"concert flute · Boehm flute · transverse flute · C flute","d":"Concert flute in C: transverse flute sounded by blowing across an embouchure hole.",
 "t":["open-hole (French model)","closed-hole (plateau)","C footjoint","B footjoint (down to B3)","split E mechanism","student body: silver-plated nickel silver","solid silver (sterling, French, coin, Britannia)","gold, platinum or gold/silver","wooden (grenadilla)"],
 "s":"https://www.thomannmusic.com/cat.html",
 "x":[
  {"n":"Boehm system flute","a":"Boehm flute","d":"Theobald Boehm's patented key system and design; the basis of the modern concert flute, its fingering also used on saxophones.","mk":"Theobald Boehm","y":"1847","s":CF,
   "v":[v("Boehm flute shown at the London Exhibition","Theobald Boehm","1851","")],"dt":"open or closed holes · C or B foot · body alloy or wood"},
  {"n":"Cooper scale","a":"Albert Cooper flute","d":"Boehm flute rescaled by Albert Cooper to A440 tuning with a recut embouchure hole.","mk":"Albert Cooper","y":"1950s","s":CF,"v":[],"dt":"pitch · headjoint cut"},
  {"n":"Brögger system","a":"Brögger Flute","d":"Johan Brögger's modification fixing key-alignment problems, with a pinless mechanism to set each key's spring tension.","mk":"Johan Brögger","y":"1980s","s":CF,
   "v":[v("Brögger Flute","Brannen Brothers","","Brannen's classic handmade model; most customisable"),v("Brögger 15/85","Brannen Brothers","","Body of 15% gold, 85% silver"),v("Brögger System","Miyazawa","2005","Pinless spring-tension mechanism")],
   "dt":"body tubing · key style · pitch · footjoint"},
  {"n":"Kingma System flute","a":"quarter-tone flute","d":"Flute with six extra keys, developed with Eva Kingma, allowing quarter-tone scales and multiphonics.","mk":"Eva Kingma","y":"","s":BRN,
   "v":[v("Kingma System flute","Brannen Brothers","","")],"dt":"open holes · extra keys"},
  {"n":"Haynes flute","a":"Wm. S. Haynes · Haynes Boston","d":"Handmade flutes from America's oldest flute maker, founded in Boston in 1888.","mk":"Wm. S. Haynes","y":"1888","s":HAY,
   "v":[v("First American gold flute","Wm. S. Haynes","1896","Made for Henry Jaeger, US Marine Band"),v("Drawn tone holes","Wm. S. Haynes","1898","George Haynes' patented design, refined by 1913"),v("Q series","Wm. S. Haynes","2010","Concert flute"),v("Sir James Galway Model Q Series","Wm. S. Haynes","",""),v("Amadeus","Wm. S. Haynes","","Concert flute"),v("Bravo","Wm. S. Haynes","","For advancing students")],
   "dt":"silver or gold body · drawn or soldered tone holes"},
  {"n":"Powell flute","a":"Verne Q. Powell","d":"Handmade Boston flutes from Verne Q. Powell's firm (1927), now part of Buffet Crampon.","mk":"Powell","y":"1927","s":POW,
   "v":[v("Platinum flute","Powell","1939","Made for the New York World's Fair; owned by William Kincaid; sold at Christie's 1986"),v("Sonaré","Powell","2002","Handmade Powell headjoint on a lower-cost body")],"dt":"silver, gold or platinum · headjoint"},
  {"n":"Muramatsu flute","a":"Muramatsu","d":"Handmade professional flutes made in Tokorozawa, Japan, since 1923.","mk":"Muramatsu","y":"1923","s":MUR,"v":[],"dt":"sterling silver · 9K, 14K, 18K or 24K gold · platinum"},
  {"n":"Miyazawa flute","a":"Miyazawa","d":"Japanese flutes known for new alloys, a wide range of headjoints and the Miyazawa Improved Scale.","mk":"Miyazawa","y":"1969","s":MIY,
   "v":[v("Miyazawa Improved Scale","Miyazawa","mid-1970s","Developed with US flutemaker P.L. West")],"dt":"alloy · headjoint"},
  {"n":"Pearl flute","a":"Pearl","d":"Japanese flutes with French pointed keywork and a pinless mechanism using socket-headed screws.","mk":"Pearl","y":"1968","s":PRL,"v":[],"dt":"pinless mechanism · body metal"}]},
{"n":"Piccolo","a":"","d":"Small transverse flute sounding an octave above the concert flute.",
 "t":["grenadilla or other hardwood","silver or nickel silver","plastic or resin","conical body, cylindrical head","in C","in D♭ (early 20th-century band)","low C key"],
 "s":"https://www.thomannmusic.com/cat.html","m":[["Amadeus piccolo","Wm. S. Haynes"]]},
{"n":"Alto flute","a":"alto flute in G","d":"Transverse flute pitched in G, a fourth below the concert flute.",
 "t":["straight headjoint","curved headjoint","open-hole (Kingma System)"],"s":"https://www.thomannmusic.com/cat.html",
 "x":[{"n":"Boehm alto flute","a":"alto flute in G","d":"Boehm's alto flute in G with levers and a reworked bore; the first widely produced version came from Rudall Carte.","mk":"Theobald Boehm","y":"c. 1854–1855","s":W+'Alto_flute',
   "v":[v("Rudall Carte alto flute","Rudall Carte & Co.","1891","First widely produced alto flute, London"),v("YFL-A421U","Yamaha","","Curved headjoint"),v("YFL-A421S","Yamaha","","Straight headjoint"),v("Amadeus alto flute","Wm. S. Haynes","","")],
   "dt":"straight or curved head · open or closed holes"}]},
{"n":"Bass flute","a":"","d":"Transverse flute pitched an octave below the concert flute, with a J-shaped head joint.",
 "t":["J-shaped head joint","vertical design","B footjoint","support rod"],"s":"https://www.thomannmusic.com/cat.html",
 "x":[{"n":"Vertical bass flute","a":"Kingma vertical bass","d":"Bass flute held upright so the floor supports its weight.","mk":"Eva Kingma","y":"","s":W+'Bass_flute',"v":[],"dt":"floor support · footjoint"}]},
{"n":"Recorder","a":"blockflöte · fipple flute","d":"Duct flute blown at the end through a fipple, with a thumb hole; sold in several voice sizes.",
 "t":["garklein","sopranino","soprano (descant)","alto (treble)","tenor","bass","great bass","contrabass","baroque (English) fingering","German fingering","wood","plastic (ABS)"],
 "s":"https://www.thomann.co.uk/moeck_4303.htm",
 "x":[
  {"n":"Bressan","a":"after Bressan","d":"Recorders after Pierre Bressan of London; his Bate Collection alto is the basis of many modern copies.","mk":"Peter Bressan","y":"1688–1732","s":W+'Peter_Bressan',
   "v":[v("Bressan alto, plastic (A=440)","Zen-On","",""),v("Bressan alto, plastic (A=415)","Zen-On","","")],"dt":"pitch 440 or 415 · wood or plastic · voice"},
  {"n":"Denner","a":"after Denner","d":"Recorders after Jacob Denner of Nuremberg (1681–1735), whose instruments became the model for many modern recorders.","mk":"Jacob Denner","y":"early 18th century","s":W+'Jacob_Denner',
   "v":[v("Moeck 5333 Denner alto","Moeck","","Boxwood, a′ = 442 Hz; after a Denner alto in the Musikhistorisk Museum, Copenhagen")],"dt":"wood · pitch · voice"},
  {"n":"Rottenburgh","a":"after Rottenburgh","d":"Recorders after Jean-Hyacinth Rottenburgh of Brussels; Moeck's line was developed with Friedrich von Huene.","mk":"Jean-Hyacinth Rottenburgh","y":"1672–1756","s":W+'Rottenburgh_family',
   "v":[v("Rottenburgh line","Moeck","1966","Developed with Friedrich von Huene; still in production"),v("Rottenburgh Alto","Moeck","","")],"dt":"wood · voice"},
  {"n":"Ganassi-type recorder","a":"Ganassi","d":"Renaissance-style design by Fred Morgan, loosely based on a recorder in the Vienna Kunsthistorisches Museum; much copied.","mk":"Fred Morgan","y":"","s":REC,"v":[],"dt":"voice · pitch"},
  {"n":"German-fingering recorder","a":"Harlan fingering","d":"Recorder with simplified fingering for F, introduced by Peter Harlan in the 1920s; other chromatic notes go out of tune.","mk":"Peter Harlan","y":"1920s","s":REC,"v":[],"dt":"voice · material"},
  {"n":"Plastic school recorder","a":"ABS recorder","d":"Injection-moulded plastic recorder, cheap enough to be sold to schools from the 1940s and 1950s.","mk":"","y":"1940s–1950s","s":REC,
   "v":[v("Aulos","Aulos","1954","Toyama Musical Instruments trademark"),v("Plastic recorder","Yamaha","","")],"dt":"voice · fingering system · colour"},
  {"n":"Adri's Dream","a":"Dream Edition","d":"Renaissance-style recorder for beginners designed by Adriana Breukink with Mollenhauer.","mk":"Mollenhauer","y":"1999","s":MOL,
   "v":[v("Adri's Dream","Mollenhauer","1999",""),v("Dream Edition","Mollenhauer","","Expanded line for more advanced players")],"dt":"voice"},
  {"n":"Eagle recorder","a":"Eagle","d":"Loud modern recorder for professional players designed with Adriana Breukink.","mk":"Küng","y":"2007","s":KUNG,"v":[],"dt":"voice"}]}]
# Eagle 'loud' not sourced -> fix
kinds[4]["x"][-1]["d"]="Recorder for professional players introduced by Küng with Adriana Breukink."
brands=[
 {"n":"Wm. S. Haynes","c":"United States","f":"1888","seg":"Handmade flutes and piccolos","d":"America's oldest flute maker, founded in Boston by William S. and George W. Haynes; owned by Eastman since 2004.","lines":["Q series","Amadeus","Bravo"],"eras":["Haynes brothers, 1888–","Eastman Music Company, 2004–"],"sig":["Haynes flute"],"sc":["orchestral flute"],"rel":["Powell"],"s":HAY},
 {"n":"Powell","c":"United States","f":"1927","seg":"Handmade flutes","d":"Flute maker founded in Boston by Verne Q. Powell, now in Maynard, Massachusetts; owned by Buffet Crampon since 2016.","lines":["Sonaré"],"eras":["Verne Q. Powell, 1927–1961","Steven Wasser, 1986–2016","Buffet Crampon, 2016–"],"sig":["Powell flute"],"sc":["orchestral flute"],"rel":["Wm. S. Haynes"],"s":POW},
 {"n":"Muramatsu","c":"Japan","f":"1923","seg":"Handmade flutes","d":"Flute maker founded by Koichi Muramatsu; factory in Tokorozawa.","lines":[],"eras":[],"sig":["Muramatsu flute"],"sc":["orchestral flute"],"rel":[],"s":MUR},
 {"n":"Miyazawa","c":"Japan","f":"1969","seg":"Flutes","d":"Flute maker founded by Masashi Miyazawa; known for the Improved Scale and Brögger System.","lines":["Brögger System"],"eras":[],"sig":["Miyazawa flute","Brögger system"],"sc":["orchestral flute"],"rel":["Brannen Brothers"],"s":MIY},
 {"n":"Pearl","c":"Japan","f":"1946","seg":"Flutes, alto flutes and piccolos (Pearl Flutes, 1968)","d":"Pearl Musical Instrument Company's flute division, based in Chiba, with a pinless mechanism.","lines":[],"eras":[],"sig":["Pearl flute"],"sc":["orchestral flute"],"rel":[],"s":PRL},
 {"n":"Brannen Brothers","c":"United States","f":"1978","seg":"Handmade flutes","d":"Woburn, Massachusetts maker of handmade flutes including the Brögger and Kingma System models.","lines":["Brögger Flute","Kingma System"],"eras":[],"sig":["Brögger system","Kingma System flute"],"sc":["orchestral flute"],"rel":["Miyazawa"],"s":BRN},
 {"n":"Moeck","c":"Germany","f":"1925","seg":"Recorders and early-music publishing","d":"Celle recorder maker and publisher founded by Hermann Moeck.","lines":["Rottenburgh"],"eras":["Hermann Moeck, 1925–1960","Hermann Alexander Moeck, 1960–"],"sig":["Rottenburgh","Denner"],"sc":["early music","recorder"],"rel":["Mollenhauer","Küng"],"s":MOE},
 {"n":"Mollenhauer","c":"Germany","f":"1822","seg":"Recorders","d":"Fulda woodwind family firm founded by Johann Andreas Mollenhauer; recorders include Adri's Dream.","lines":["Adri's Dream","Dream Edition"],"eras":["Bernhard Mollenhauer, 1961–"],"sig":["Adri's Dream"],"sc":["early music","recorder"],"rel":["Moeck","Küng"],"s":MOL},
 {"n":"Küng","c":"Switzerland","f":"1933","seg":"Recorders","d":"Schaffhausen recorder maker founded by Franz Küng.","lines":["Eagle"],"eras":[],"sig":["Eagle recorder"],"sc":["recorder"],"rel":["Moeck","Mollenhauer"],"s":KUNG},
 {"n":"Aulos","c":"Japan","f":"1954","seg":"Plastic recorders","d":"Recorder trademark of Toyama Musical Instruments, used since 1954.","lines":[],"eras":[],"sig":["Plastic school recorder"],"sc":["school music"],"rel":["Yamaha"],"s":AUL},
 {"n":"Yamaha","c":"Japan","f":"1887","seg":"Musical instruments, all segments","d":"Japanese instrument maker covering student to professional flutes and plastic recorders.","lines":[],"eras":[],"sig":[],"sc":["school music","orchestral flute"],"rel":[],"s":"knowledge"}]
notes=("All 5 planned kinds kept (k48–k52). Flute archetypes are key systems (Boehm, Cooper, Brögger, Kingma) and maker house styles; no flute model lines for Muramatsu, Pearl or Yamaha "
 "because no retrieved page named them (Yamaha site returned 403). Piccolo has only one confirmed model (Haynes Amadeus). Recorder archetypes follow historical originals (Bressan, Denner, Rottenburgh) "
 "plus modern designs; Mollenhauer Denner/Canta, Küng Superio/Studio and Aulos/Yamaha model numbers left out (unconfirmed). Historical makers (Boehm, Cooper, Brögger, Kingma, Bressan, Denner, Rottenburgh, "
 "Morgan, Harlan) are archetype mk without brand entries; Zen-On and Rudall Carte appear only as version makers. Gemeinhardt, Jupiter, Sankyo, Altus, Louis Lot, Dolmetsch not added (no retrieved detail). No traditions.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/E3/shelves/04_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
