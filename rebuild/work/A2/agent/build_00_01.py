import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a='',dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
heritage = {"n":"Heritage running sneaker","a":"retro runner · heritage runner · classic running shoe",
 "d":"Running shoe from the 1960s–2000s worn or reissued as an everyday lifestyle sneaker.",
 "t":["OG reissue","retro (updated)","made in USA/UK","collaboration"],
 "s":W+"Air_Max",
 "x":[
  X("Cortez","Nike","1972",W+"Nike_Cortez","Bill Bowerman's cushioned training shoe; Nike's first running shoe, launched around the 1972 Olympics.",
    [("Onitsuka Tiger Cortez / Tiger Corsair","Onitsuka Tiger","1969","Onitsuka version; renamed Corsair after the Cortez name went to Blue Ribbon Sports"),
     ("Cortez (leather original)","Nike","1972",""),("Cortez nylon and suede","Nike","","lighter uppers"),("Cortez Fly Motion","Nike","2009","Flywire upper")],
    a="Mexico · Aztec",dt="upper leather, nylon, suede · colourway"),
  X("Waffle Trainer","Nike","1975","https://about.nike.com/stories/nike-moon-shoe-waffle-iron-true-history","Running shoe with Bowerman's waffle-iron-moulded studded sole.",
    [("Moon Shoe","Nike","1972","hand-made prototype for the US Olympic Trials"),("Oregon Waffle","Nike","1973","first released waffle-soled shoe"),("Waffle Trainer","Nike","1975","Bowerman and Geoff Hollister")],dt="colourway · upper nylon, suede"),
  X("Air Max 1","Nike","1986",W+"Air_Max","First shoe of the Air Max line, with a visible Air unit in the heel; the line was conceived by Tinker Hatfield.",dt="colourway · upper mesh, suede, leather"),
  X("Air Max 90","Nike","1990",W+"Air_Max","Air Max model of 1990 with a larger visible heel Air unit.",dt="colourway · upper mesh, suede, leather"),
  X("Air Max 95","Nike","1995",W+"Air_Max","Air Max with a layered upper and visible forefoot Air; visual design by Sergio Lozano.",dt="colourway · gradient side panels"),
  X("Air Max 97","Nike","1997",W+"Air_Max","Air Max with a full-length visible Air unit, designed by Christian Tresser.",dt="colourway · metallic or tonal upper"),
  X("Air Max Plus","Nike","1998",W+"Air_Max","Air Max with Tuned Air and a caged upper, designed by Sean McDowell.",a="TN · Tuned Air",dt="colourway · gradient upper"),
  X("Air Max family (other models)","Nike","1989–2024",W+"Air_Max","Further Air Max generations, from the Light and BW to the 270 and DN.",
    [("Air Max Light","Nike","1989",""),("Air Max BW","Nike","1991",""),("Air Max 180","Nike","1991",""),("Air Max 93","Nike","1993",""),("Air Max2 CB 94","Nike","1994","Tracy Teague"),
     ("Air Max 360","Nike","2006",""),("Air VaporMax","Nike","2017",""),("Air Max 270","Nike","2018",""),("Air Max 720","Nike","2019",""),("Air Max 2090","Nike","2020",""),("Air Max DN","Nike","2024","")]),
  X("990","New Balance","1982",W+"New_Balance_99X_Series","New Balance's grey-suede premium runner, made in the USA and updated in numbered generations.",
    [("990 (v1)","New Balance","1982",""),("990v2","New Balance","1998",""),("990v3","New Balance","2012","led by Andrew Nyssen"),("990v4","New Balance","2016",""),("990v5","New Balance","2019",""),("990v6","New Balance","2022","")],
    dt="grey suede/mesh or colourways · made in USA · width fittings"),
  X("99X numbered models","New Balance","1986–2023",W+"New_Balance_99X_Series","Other models of the 99X premium line, several since reissued.",
    [("995","New Balance","1986",""),("996","New Balance","1988",""),("997","New Balance","1990",""),("998","New Balance","1993",""),("999","New Balance","1996",""),("991","New Balance","2001",""),("992","New Balance","2006",""),("993","New Balance","2008",""),("991v2","New Balance","2023","")],
    dt="made in USA or UK · colourway"),
  X("574","New Balance","1988",W+"New_Balance_574","Affordable hybrid road/trail runner with ENCAP heel, designed by Steven Smith from the 576 and 577.",
    [("574","New Balance","1988","original"),("574 Greens","New Balance","2021","golf version"),("574+","New Balance","2022","platform, stacked EVA"),("Numeric 574","New Balance","2023","skate version")],dt="suede/mesh · colourway"),
  X("Gel-Lyte III","ASICS","1990","https://www.complex.com/sneakers/a/gary-warnett/asics-gel-lyte-iii-shigeyuki-mitsui","Shigeyuki Mitsui's runner with split tongue, Gel cushioning and triple-density sole.",
    [("Gel-Lyte III (OG)","ASICS","1990","original citrus and green colourway"),("Gel-Lyte III retro","ASICS","mid-2000s","reissue; collaborations with Patta, Solebox, Ronnie Fieg")],dt="colourway · suede/mesh"),
  X("Mexico 66","Onitsuka Tiger","1966 (stripes); 2002 (reissue)",W+"Onitsuka_Tiger","Slim low runner carrying the crossed 'Mexico line' stripes introduced in 1966.",
    [("Mexico 66 reissue","Onitsuka Tiger","2002","launched with the brand's fashion revival")],dt="leather or suede · colourway"),
  X("ZX series","adidas","1984","https://highsnobiety.com/p/adidas-archive-zx-history","Numbered adidas running line led by Jacques Chassaing and Markus Thaler, with Torsion and Soft Cell technology.",
    [("ZX 500","adidas","1984","first model"),("ZX 8000","adidas","","Torsion runner; Undefeated collaboration 2008"),("ZX 9000","adidas","",""),("ZX Flux","adidas","2014","pared-down runner based on the ZX 8000")],dt="model number · colourway"),
  X("Jazz","Saucony","1981","https://www.80scasualclassics.co.uk/blog/saucony-jazz-trainer-history/","Saucony's suede-and-nylon runner with double foam midsole, its first global running success.",dt="suede/nylon · colourway"),
  X("SL 72","adidas","1972",W+"Adidas_SL_72","Super-light nylon-and-suede runner released at the 1972 Olympics; first shoe with the trefoil logo.",
    [("SL 72 OG","adidas","1972",""),("SL Loop Runner","adidas","2014","modern reinterpretation"),("SL 72 RS","adidas","2024","reshaped, chunkier sole"),("SL 72 RTN","adidas","2024","rugged outdoor sole")],dt="nylon upper, suede overlays · colourway"),
 ]}
terrace = {"n":"Terrace sneaker","a":"terrace trainer · casuals trainer · T-toe sneaker",
 "d":"Low suede indoor-sport or training shoe adopted by British football casuals, usually with gum sole.",
 "t":["OG reissue","gum sole","made in Germany/Italy","collaboration"],
 "s":W+"Adidas_Handball_Spezial",
 "x":[
  X("Samba","adidas","1949",W+"Adidas_Samba","Adolf Dassler's gum-soled football trainer for icy, hard ground.",
    [("Samba '85","adidas","1985",""),("Samba OG","adidas","","suede and leather, gum sole"),("Samba Classic","adidas","","indoor/five-a-side"),("Samba ADV","adidas","2017","skate version"),("Samba Rose","adidas","2018","women's platform")],dt="leather/suede · gum sole · colourway"),
  X("Gazelle","adidas","1966",W+"Adidas_Gazelle","Suede training shoe continuing the Olympiade, reworked as a handball shoe in 1979.",
    [("Gazelle (training)","adidas","1966",""),("Gazelle handball rework","adidas","1979","transparent sole"),("Gazelle Bold","adidas","1996","triple-stacked platform"),("Gazelle Indoor","adidas","","thin translucent gum sole"),("Gazelle ADV","adidas","","skate version")],dt="suede · colourway · sole gum or rubber"),
  X("Handball Spezial","adidas","1979",W+"Adidas_Handball_Spezial","Suede handball shoe taken up by 1980s UK football fans in club colours.",
    [("Handball Spezial","adidas","1979","original"),("Sporty & Rich collaboration","adidas","2023","vintage-inspired colours")],a="Spezial",dt="suede · gum sole · colourway"),
  X("Campus","adidas","1980","https://blog.laced.com/from-hip-hop-to-hardflips-the-history-of-the-adidas-campus/","Suede basketball shoe following the Tournament, later a hip-hop and skate staple.",
    [("Campus 80s","adidas","","reissue"),("Campus 00s","adidas","2023","padded tongue, chunky laces")],dt="suede · colourway"),
  X("Suede","Puma","1968",W+"Puma_Suede","Heiko Desens's suede basketball shoe, an early sneaker in suede, later a b-boy favourite.",
    [("Suede Classic","Puma","1968",""),("Clyde","Puma","1973","narrower Suede for Walt Frazier"),("Suede XL","Puma","2024","bulkier skate-inspired")],a="Clyde",dt="suede · colourway"),
  X("Palermo","Puma","1980s","https://about.puma.com/en/newsroom/news/80s-terrace-legend-classic-puma-palermo-og-back","T-toe terrace shoe with gum sole from Puma's European-cities series.",
    [("Palermo OG","Puma","2023","reissue in original blue and white")],dt="suede/nylon · gum sole · colourway"),
  X("Borg Elite","Diadora","1978","https://www.soccerbible.com/lifestyle/sneakers/2016/02/diadora-borg-elite-made-in-italy/","Leather tennis shoe for Björn Borg adopted by 1980s football casuals.",
    [("Borg Elite 'Made in Italy'","Diadora","2016","reissue"),("B-Elite","Diadora","2021","white and gold")],a="B.Elite",dt="leather · branding gold or silver"),
 ]}
chunky = {"n":"Chunky sneaker","a":"dad sneaker · dad shoe · ugly sneaker",
 "d":"Sneaker with an oversized, sculpted midsole as the main design feature.",
 "s":"https://www.littleburgundyshoes.com/blog/dadshoes",
 "x":[
  X("Triple S","Balenciaga","2017","https://www.sneakerfreaker.com/features/real-talk/did-the-triple-s-break-the-sneaker-industry","Demna Gvasalia's panel-heavy designer sneaker on a stacked triple sole; see also Designer sneaker.",dt="colourway"),
  X("Ozweego","adidas","1996","https://highsnobiety.com/p/adidas-ozweego-history","adiPRENE running shoe revived by Raf Simons as a chunky icon.",
    [("Ozweego","adidas","1996","original runner"),("Ozweego 2","adidas","1997",""),("Ozweego 3","adidas","1998","Torsion midsole"),("Ozweego 4","adidas","1999",""),("Raf Simons Ozweego 1","adidas","2013","collaboration"),("Ozweego (in-line)","adidas","2019","based on Ozweego 3")],dt="colourway"),
  X("Disruptor","Fila","1996","https://www.dazeddigital.com/fashion/article/45892/1/fila-disruptor-ii-ugly-sneaker-trend-memes-gen-z-dad-shoes","Chunky trainer with zig-zag platform sole and F logo tongue.",
    [("Disruptor","Fila","1996",""),("Disruptor II","Fila","2014","revival with upgraded materials")],dt="colourway · also sandal and platform forms"),
 ],
 "m":[["Falcon","adidas"]]}
K=lambda n,c,f,seg,d,sig: {"n":n,"c":c,"f":f,"seg":seg,"d":d,"sig":sig,"s":"knowledge"}
brands=[K("Nike","United States","1964","sportswear","American sportswear company, founded as Blue Ribbon Sports.",["Cortez","Waffle Trainer","Air Max 1","Air Max 90"]),
 K("adidas","Germany","1949","sportswear","German sportswear company founded by Adolf Dassler.",["Samba","Gazelle","SL 72","ZX series"]),
 K("New Balance","United States","1906","sportswear","American athletic footwear maker with US and UK factories.",["990","574"]),
 K("ASICS","Japan","1977","sportswear","Japanese sportswear company formed from Onitsuka and others.",["Gel-Lyte III"]),
 K("Onitsuka Tiger","Japan","1949","heritage sportswear","Japanese heritage sneaker brand owned by ASICS.",["Mexico 66"]),
 K("Saucony","United States","1898","running","American running shoe brand.",["Jazz"]),
 K("Puma","Germany","1948","sportswear","German sportswear company founded by Rudolf Dassler.",["Suede","Palermo"]),
 K("Diadora","Italy","1948","sportswear","Italian sportswear company.",["Borg Elite"]),
 K("Fila","Italy","1911","sportswear","Italian-founded sportswear brand.",["Disruptor"]),
 K("Balenciaga","France","1917","luxury fashion","Luxury fashion house founded by Cristóbal Balenciaga.",["Triple S"])]
notes=("Kinds: Heritage running sneaker (new), Terrace sneaker (new), Chunky sneaker (old k4). Dropped from Chunky: Nike Axis and Puma Defy "
 "(not sourced as icons, per plan); adidas Falcon kept as a flat model from old data. Left out: Nike P-6000 (no source retrieved), NB 550 "
 "(basketball, belongs in Basketball sneaker), Saucony Jazz versions (not confirmed), ZX 8000/9000 years (sources disagree), Diadora other models. "
 "Wikidata helper returned HTTP 429 so all sources are WebFetch pages. Brand entries are from knowledge.")
out={"kinds":[heritage,terrace,chunky],"brands":brands,"traditions":[],"notes":notes}
p='work/A2/shelves/00_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
