import json, os
W="https://en.wikipedia.org/wiki/"
STR=W+"Stradivarius"; GDG=W+"Giuseppe_Guarneri_del_Ges%C3%B9"; AM=W+"Amati"; VU=W+"Jean-Baptiste_Vuillaume"
SW="https://www.sweetwater.com/shop/by-category"
strad_v = {"n":"Stradivari pattern","a":"Strad model · Stradivarius copy","d":"Antonio Stradivari's Cremonese violin outline, the model most modern violins copy.","mk":"Antonio Stradivari","y":"c. 1700–1725 (golden period)","s":STR,
 "v":[{"n":"Long Pattern","mk":"Antonio Stradivari","y":"1690–1700","d":"elongated outline of the 1690s"},
      {"n":"'Tuscan'","mk":"Antonio Stradivari","y":"1690","d":""},
      {"n":"Golden-period violins (e.g. 'Le Maurien' 1714, 'Lady Blunt' 1721)","mk":"Antonio Stradivari","y":"c. 1700–1725","d":"the reference period for copies"},
      {"n":"'Messiah' (Le Messie) copies","mk":"Jean-Baptiste Vuillaume","y":"c. 1853–1873","d":"Vuillaume's main model; about six notable copies"},
      {"n":"Modern workshop and factory copies","mk":"","y":"","d":"'Stradivarius' labels on copies do not mean a genuine instrument"}],
 "dt":"maker and school · varnish colour · antiqued or clean finish · fractional sizes 1/16–4/4"}
gdg_v = {"n":"Guarneri del Gesù pattern","a":"del Gesù model · Guarneri copy","d":"Bartolomeo Giuseppe Guarneri's bolder Cremonese violin model, prized for a darker, more robust tone; the second most copied pattern.","mk":"Giuseppe Guarneri del Gesù","y":"1730s–1744","s":GDG,
 "v":[{"n":"'Il Cannone'","mk":"Giuseppe Guarneri del Gesù","y":"1743","d":"Paganini's violin"},
      {"n":"'Lord Wilton'","mk":"Giuseppe Guarneri del Gesù","y":"1742","d":"once Yehudi Menuhin's"},
      {"n":"'Vieuxtemps'","mk":"Giuseppe Guarneri del Gesù","y":"1741","d":""},
      {"n":"'Kochański'","mk":"Giuseppe Guarneri del Gesù","y":"1741","d":""},
      {"n":"'Il Cannone' copy","mk":"Jean-Baptiste Vuillaume","y":"","d":"made for Paganini, later owned by Camillo Sivori"}],
 "dt":"maker and school · varnish colour · antiqued or clean finish"}
amati_v = {"n":"Amati pattern","a":"Andrea Amati · Nicolò Amati · Grand Amati","d":"The Amati family's Cremonese model that gave the violin family its definitive form; Nicolò's wider 'Grand Amati' is the best-known variant.","mk":"Amati","y":"c. 1560–1684","s":AM,
 "v":[{"n":"Charles IX violin","mk":"Amati","y":"1564","d":"from the royal set ordered by Catherine de Médicis"},
      {"n":"Brothers Amati (Antonio and Girolamo)","mk":"Amati","y":"c. 1580–1630","d":"refined f-hole shape"},
      {"n":"Grand Amati","mk":"Amati","y":"17th century","d":"Nicolò Amati's wider model"}],
 "dt":"size · decoration (painted royal sets) · maker generation"}
kinds = [
 {"n":"Violin","a":"fiddle","d":"Four-string bowed instrument held under the chin, the treble of the violin family; sold in fractional sizes.",
  "t":["fractional sizes 1/16–4/4","carved solid wood","laminated (student)","electric violin","baroque set-up"],"tg":["baby"],"s":SW,
  "x":[strad_v,gdg_v,amati_v]},
 {"n":"Viola","a":"","d":"Four-string bowed instrument held under the chin, larger and lower than the violin; sized by body length.",
  "t":["body length 14–17 in","carved solid wood","laminated (student)","electric viola"],"s":SW,
  "x":[{"n":"Amati viola","a":"","d":"Early Cremonese violas by the Amati family, including large tenor violas.","mk":"Amati","y":"c. 1570–1677","s":AM,
        "v":[{"n":"'Violetta'","mk":"Amati","y":"c. 1570","d":"painted decoration"},{"n":"'Henry IV'","mk":"Amati","y":"c. 1590","d":"heraldic decoration"},{"n":"Royal Academy of Music tenor viola","mk":"Amati","y":"c. 1620","d":"tenor size not cut down"},{"n":"'Romanov'","mk":"Amati","y":"1677","d":"by Nicolò Amati"}],"dt":"body length · tenor or contralto size · decoration"},
       {"n":"Stradivari viola","a":"","d":"Violas from Antonio Stradivari's Cremona workshop, a reference model for copies.","mk":"Antonio Stradivari","y":"","s":STR,
        "v":[{"n":"'Macdonald'","mk":"Antonio Stradivari","y":"","d":""}],"dt":"body length · varnish"},
       {"n":"Tertis model","a":"","d":"Lionel Tertis's 16¾-inch viola design, keeping the tone of his large Montagnana in a more manageable body.","mk":"Lionel Tertis","y":"20th century","s":W+"Lionel_Tertis","v":[],"dt":"16¾ in body"}]},
 {"n":"Cello","a":"violoncello","d":"Four-string bowed instrument played seated with an endpin, the tenor-bass of the violin family.",
  "t":["fractional sizes 1/10–4/4","carved solid wood","laminated (student)","carbon fibre","electric cello"],"tg":["baby"],"s":SW,
  "x":[{"n":"Stradivari cello","a":"forma B · Strad cello","d":"Stradivari's reduced cello pattern, which many older large bass violins were cut down to match.","mk":"Antonio Stradivari","y":"c. 1700s","s":W+"Cello",
        "v":[{"n":"'General Kyd'","mk":"Antonio Stradivari","y":"1684","d":"early cello"},{"n":"'Servais'","mk":"Antonio Stradivari","y":"","d":"old large pattern"},{"n":"'Davidov'","mk":"Antonio Stradivari","y":"1712","d":"played by du Pré and Yo-Yo Ma"}],"dt":"body length · varnish · baroque or modern set-up"},
       {"n":"Montagnana cello","a":"Venetian cello","d":"Domenico Montagnana's Venetian cello, about 1 cm shorter and 2 cm wider across the C bouts than a Stradivari forma B.","mk":"Domenico Montagnana","y":"1712–1750","s":W+"Domenico_Montagnana",
        "v":[{"n":"'Petunia'","mk":"Domenico Montagnana","y":"1733","d":"Yo-Yo Ma"},{"n":"'Mighty Venetian'","mk":"Domenico Montagnana","y":"1738","d":""}],"dt":"width · varnish"},
       {"n":"Amati cello","a":"","d":"The earliest surviving cellos, made by Andrea Amati.","mk":"Amati","y":"c. 1538–1545","s":AM,
        "v":[{"n":"'The King'","mk":"Amati","y":"c. 1538–1545","d":"oldest extant cello"}],"dt":""}],
  "m":[["Carbon-fibre cello","Luis & Clark"]]},
 {"n":"Double bass","a":"upright bass · contrabass","d":"Largest and lowest bowed string instrument, played standing or on a high stool.",
  "t":["3/4 (most common)","4/4","1/2 and smaller","five-string (low B)","C extension","carved","laminated (plywood)","hybrid (laminated back, carved top)","electric upright"],"s":SW,
  "x":[{"n":"Violin-form bass","a":"","d":"Double bass with the rounded shoulders and outline of the violin family.","mk":"","y":"","s":W+"Double_bass","v":[],"dt":"carved or laminated · size · four or five strings"},
       {"n":"Gamba-form bass","a":"viol-form bass","d":"Double bass with sloping shoulders and flat back, following the viola da gamba outline.","mk":"","y":"","s":W+"Double_bass","v":[],"dt":"carved or laminated · size"},
       {"n":"Busetto-form bass","a":"","d":"Less common double bass outline without the usual corners.","mk":"","y":"","s":W+"Double_bass","v":[],"dt":""}]},
 {"n":"Bow","a":"violin bow · cello bow · bass bow","d":"Stick strung with horsehair, drawn across the strings of a violin-family instrument.",
  "t":["violin","viola","cello","double bass","pernambuco","ipê or brazilwood","carbon fibre","fibreglass","horsehair (white or black)","synthetic hair","ebony frog"],"s":W+"Bow_(music)",
  "x":[{"n":"Tourte model","a":"modern bow · French bow","d":"François Tourte's heat-bent pernambuco bow with screw-adjusted frog and spreader, the basis of virtually all modern bows.","mk":"François Tourte","y":"1785–1790","s":W+"Fran%C3%A7ois_Tourte",
        "v":[{"n":"Tourte bows with Viotti","mk":"François Tourte","y":"1785–1790","d":"original heavier model"},{"n":"Self-rehairing bow","mk":"Jean-Baptiste Vuillaume","y":"","d":"hair replaced via frog mechanism"},{"n":"Hollow steel bow","mk":"Jean-Baptiste Vuillaume","y":"c. 1834","d":""}],"dt":"wood · mounts (silver, gold) · frog material · weight and balance"},
       {"n":"Baroque bow","a":"Corelli-Tartini bow · sonata bow","d":"Pre-Tourte Italian bow, straight or slightly convex, lighter, with a narrower ribbon of hair.","mk":"","y":"c. 1725","s":W+"Bow_(music)","v":[],"dt":"61–71 cm · straight or convex stick"},
       {"n":"German bass bow","a":"Butler bow","d":"Broad double bass bow with a large frog, held underhand; the older design.","mk":"","y":"","s":W+"Bow_(music)","v":[],"dt":""},
       {"n":"French bass bow","a":"","d":"Double bass bow held overhand like other string bows, popularised by Giovanni Bottesini.","mk":"","y":"19th century","s":W+"Bow_(music)","v":[],"dt":""},
       {"n":"Carbon-fibre bow","a":"composite bow","d":"Bow with an engineered carbon-fibre stick that holds its camber through humidity and temperature changes.","mk":"CodaBow","y":"","s":"https://codabow.com/pages/innovation-technology-and-design",
        "v":[{"n":"Master","mk":"CodaBow","y":"","d":"top tier"},{"n":"Performance","mk":"CodaBow","y":"","d":""},{"n":"Student","mk":"CodaBow","y":"","d":"violin, viola, cello only"}],"dt":"instrument · tier · frog material"}]}]
brands = [
 {"n":"Antonio Stradivari","c":"Italy","f":"","seg":"Historic Cremonese luthier","d":"Cremona maker (1644–1737) of over 1,100 instruments, about 650 surviving; his model is the most copied.","lines":[],"eras":["Long Pattern, 1690–1700","Golden period, c. 1700–1725"],"sig":["Stradivari pattern","Stradivari cello","Stradivari viola"],"sc":[],"rel":["Amati","Giuseppe Guarneri del Gesù"],"s":STR},
 {"n":"Giuseppe Guarneri del Gesù","c":"Italy","f":"","seg":"Historic Cremonese luthier","d":"Cremona violin maker (1698–1744) whose labels carried the IHS monogram; his violins rival Stradivari's.","lines":[],"eras":[],"sig":["Guarneri del Gesù pattern"],"sc":[],"rel":["Antonio Stradivari"],"s":GDG},
 {"n":"Amati","c":"Italy","f":"c. 1538","seg":"Historic Cremonese luthier family","d":"Cremona family (c. 1538–1740) whose founder Andrea Amati fixed the form of violin, viola and cello; Nicolò taught Stradivari.","lines":[],"eras":["Andrea Amati, c. 1505–1577","Antonio and Girolamo Amati","Nicolò Amati, 1596–1684","Girolamo II, 1649–1740"],"sig":["Amati pattern","Amati viola","Amati cello"],"sc":[],"rel":["Antonio Stradivari"],"s":AM},
 {"n":"Domenico Montagnana","c":"Italy","f":"1712","seg":"Historic Venetian luthier","d":"Venetian maker (1686–1750) of violins, violas, cellos and basses, best known for wide cellos.","lines":[],"eras":[],"sig":["Montagnana cello"],"sc":[],"rel":[],"s":W+"Domenico_Montagnana"},
 {"n":"Jean-Baptiste Vuillaume","c":"France","f":"1828","seg":"Historic Paris workshop","d":"Mirecourt-born Paris maker (1798–1875) whose workshop made over 3,000 instruments, famed for Stradivari and Guarneri copies and bows.","lines":[],"eras":[],"sig":["'Messiah' copies","'Il Cannone' copy"],"sc":[],"rel":["Antonio Stradivari","Giuseppe Guarneri del Gesù"],"s":VU},
 {"n":"François Tourte","c":"France","f":"","seg":"Historic bow maker","d":"French bow maker (1747–1835) whose 1785–1790 changes shaped the modern bow.","lines":[],"eras":[],"sig":["Tourte model"],"sc":[],"rel":[],"s":W+"Fran%C3%A7ois_Tourte"},
 {"n":"Lionel Tertis","c":"United Kingdom","f":"","seg":"Violist and viola designer","d":"Violist who designed the 16¾-inch Tertis model viola.","lines":[],"eras":[],"sig":["Tertis model"],"sc":[],"rel":["Domenico Montagnana"],"s":W+"Lionel_Tertis"},
 {"n":"CodaBow","c":"United States","f":"","seg":"Carbon-fibre bows","d":"US maker that claims the original carbon-fibre bow, in Master, Performance and Student tiers.","lines":["Master","Performance","Student"],"eras":[],"sig":["Carbon-fibre bow"],"sc":[],"rel":[],"s":"https://codabow.com/pages/innovation-technology-and-design"},
 {"n":"Yamaha","c":"Japan","f":"1887","seg":"Mass-market instruments","d":"Japanese instrument maker with student and electric string instruments.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"knowledge"}]
trads = [
 {"n":"Cremonese violin making","g":"Woodwork & furniture","r":"Cremona, Italy","p":"16th century–present","d":"The violin-making tradition of the Amati, Stradivari and Guarneri, inscribed by UNESCO in 2012.","tech":"Hand-built from more than 70 wooden parts around an inner mould; three to six instruments a year per maker.","mat":"Naturally seasoned woods; no industrial materials","forms":["Violin","Viola","Cello"],"ctr":["Amati","Antonio Stradivari","Giuseppe Guarneri del Gesù","Consorzio Liutai Antonio Stradivari","Associazione Liutaria Italiana"],"auth":"Provenance and expert certification; a 'Stradivarius' label alone proves nothing.","s":"https://ich.unesco.org/en/RL/traditional-violin-craftsmanship-in-cremona-00719"},
 {"n":"Mittenwald violin making","g":"Woodwork & furniture","r":"Mittenwald, Bavaria, Germany","p":"mid-17th century–present","d":"Bavarian school of violin, viola and cello making founded by Matthias Klotz.","tech":"","mat":"","forms":["Violin","Viola","Cello"],"ctr":["Matthias Klotz (1640–1696)","Aegidius Klotz","Museum of violin manufacturing"],"auth":"","s":W+"Mittenwald"},
 {"n":"Mirecourt lutherie","g":"Woodwork & furniture","r":"Mirecourt, Lorraine, France","p":"c. 1602–present","d":"French centre of violin and bow making, from family workshops to factories, revived by a national school.","tech":"Workshop and factory production of violins and bows","mat":"","forms":["Violin","Bow"],"ctr":["Jean-Baptiste Vuillaume","Didier Nicolas (D. Nicolas Aîné)","Jérôme Thibouville-Lamy (JTL)","Collin-Mezin","École nationale de lutherie","Musée de la Lutherie et de l'Archèterie françaises"],"auth":"","s":W+"Mirecourt"},
 {"n":"Markneukirchen / Musikwinkel instrument making","g":"Woodwork & furniture","r":"Vogtland, Saxony, Germany","p":"17th century–present","d":"Saxon instrument-making region founded by Bohemian Protestant exiles, once a mass supplier of string, brass and woodwind instruments.","tech":"","mat":"","forms":["Violin","Bow"],"ctr":["Ernst Heinrich Roth","Musical Instrument Museum Markneukirchen (1883)"],"auth":"","s":W+"Markneukirchen"}]
notes=("All 4 old kinds kept; Bow added as new kind. Student-tier models (Yamaha, Eastman, Gliga) not listed: no retrieved page confirmed models, so only Yamaha has a knowledge register entry; Eastman and Gliga left out (founding facts unsure). "
 "Not added: famous instruments without retrieved years beyond those shown; double-bass maker archetypes (Gasparo da Salò, Maggini, Testore, Goffriller named on the Double bass page without years); Peccatte and other bow makers; Luis & Clark kept as a flat model only (cello page).")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p="work/E3/shelves/04_00.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
