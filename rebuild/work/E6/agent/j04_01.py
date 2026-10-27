import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
NZ="Negretti & Zambra"; SM="Short & Mason"; PA="P Adie"; RF="Richard Frères"; TF="TFA Dostmann"
WB="https://en.wikipedia.org/wiki/Barometer"; WG="https://en.wikipedia.org/wiki/Barograph"
baro={"n":"Barometer","a":"weather glass","d":"Instrument that shows air pressure, and so the likely weather, with a mercury column or a sealed aneroid capsule.",
 "t":["mercury cistern (stick)","angle (diagonal)","wheel (banjo)","aneroid","marine (gimballed)","digital"],
 "s":WB,
 "x":[
  X("Stick barometer","Upright mercury-tube barometer in a narrow case, the original form after Torricelli's 1643 experiment.","","1643",WB,
    [("Fortin barometer","","","adjustable mercury cistern for exact readings, named after Jean Nicolas Fortin")],"mahogany or oak case · cistern or siphon tube · vernier scale"),
  X("Wheel barometer","Mercury barometer whose float turns a pointer round a dial, in a banjo-shaped case; popular in Britain from about 1810.","","c. 1810",WB,
    [("Aiano wheel barometers","Natalo Aiano","c. 1785–1805","Holborn, London maker")],"banjo case · dial with weather words · often with thermometer and hygrometer","banjo barometer"),
  X("Admiral FitzRoy barometer","Mercury barometer with thermometers and printed rules for forecasting, after Admiral Robert FitzRoy; made for homes after his death in 1865.","","",
    "https://collection.sciencemuseumgroup.org.uk/objects/co54595",
    [("domestic FitzRoy storm barometer",NZ,"1876–1884","oak case, dry and wet thermometers")],"oak case · inscribed weather rules"),
  X("Kew pattern marine barometer","Gimballed mercury barometer with an iron cistern that became the standard on Royal Navy and other ships in the late 19th and early 20th centuries.",PA,"","https://www.rmg.co.uk/collections/objects/rmgc-object-384485",
    [("Kew pattern Mark 1",PA,"c. 1885","Meteorological Office numbered"),("Kew pattern",PA,"","from old data")],"brass tube · iron cistern · gimbals · attached thermometer"),
  X("Marine barometer","Mercury barometer built to be read at sea, from Robert Hooke's 1668 design onward.","","1668",WB,
    [("marine gun barometer",NZ,"1863","from the BADA maker history")],"gimballed or bracket-mounted"),
  X("Aneroid barometer","Barometer using a sealed metal capsule instead of liquid, invented by Lucien Vidi in 1844; the common household form.","","1844",WB,
    [("Stormoguide",SM,"","from old data"),("Tycos aneroid",SM,"c. 1907 on","Short & Mason with Taylor Instrument Companies"),("Sputnik barometer",TF,"","from old data")],"brass or wood case · dial · ship's-wheel and porthole styles")]}
bg={"n":"Barograph","a":"recording barometer","d":"Barometer that records air pressure over time as a line on a paper chart turned by clockwork.",
 "t":["aneroid drum (weekly chart)","marine","precision (microbarograph)","electronic"],
 "s":WG,
 "x":[
  X("Aneroid drum barograph","Stacked aneroid capsules move a pen across a chart on a clockwork drum turning once a day, week or month; heyday late Victorian to early 20th century.","","1760s",WG,
    [("first effective recording barograph","Alexander Cumming","1760s",""),("stacked-aneroid design","Lucien Vidi","1844",""),("drum barograph",NZ,"",""),("drum barograph",SM,"","")],"glazed wooden case · ink pen · weekly chart"),
  X("Richard Frères barograph","Recording barometer from the Paris firm of Jules and Max Richard, whose 1880s recorders set the pattern; marked with the RF monogram.",RF,"1880s","https://collection.sciencemuseumgroup.org.uk/people/cp53015/jules-richard",
    [("aviation barograph","Jules Richard","","")],"RF monogram · aneroid stack · drum")]}
sg={"n":"Storm glass","a":"chemical weather glass · FitzRoy's storm barometer","d":"Sealed glass of camphor solution whose crystals were believed to foretell the weather; really a crude thermoscope.",
 "s":"https://en.wikipedia.org/wiki/Storm_glass",
 "x":[X("FitzRoy storm glass","Storm glass popularised in the 1860s by Admiral Robert FitzRoy, after the Crown gave them to fishing communities following the 1859 storms.","","1860s","https://en.wikipedia.org/wiki/Storm_glass",[],"camphor, potassium nitrate, ammonium chloride in ethanol and water")]}
gt={"n":"Galileo thermometer","a":"termometro lento","d":"Sealed column of liquid with weighted glass bulbs that rise or sink with temperature, each tagged with a reading.",
 "s":"https://en.wikipedia.org/wiki/Galileo_thermometer",
 "x":[X("Galileo thermometer","Floating-bulb thermometer devised by the Accademia del Cimento in Florence and described in 1666; revived as a decorative piece from the 1990s.","","1666","https://en.wikipedia.org/wiki/Galileo_thermometer",
    [("Accademia del Cimento original","","1666","ethanol-water, ground glass bulbs"),("modern revival","","1990s","sold by the Natural History Museum, London"),("Galileo thermometer","","","from old data")],"column height · number of bulbs · coloured liquids")]}
brands=[
 {"n":NZ,"c":"United Kingdom","f":"1850","seg":"Heritage manufactory","kf":"barometers, thermometers","d":"London meteorological instrument makers founded by Henry Negretti and Joseph Warren Zambra at Hatton Garden; medal winners at the 1851 Great Exhibition.","sig":["Admiral FitzRoy barometer","Marine barometer"],"s":"https://www.bada.org/features/makers-series-negretti-and-zambra"},
 {"n":SM,"c":"United Kingdom","f":"1875","seg":"Heritage manufactory","kf":"aneroids, barographs","d":"London makers of aneroid barometers and barographs, partnered with Taylor Instrument (Tycos) from about 1907; merged 1969.","sig":["Aneroid barometer","Aneroid drum barograph"],"s":"https://collection.sciencemuseumgroup.org.uk/people/cp6649/short-and-mason-limited"},
 {"n":PA,"c":"United Kingdom","seg":"Heritage manufactory","kf":"marine barometers","d":"Patrick Adie's London firm, a principal maker of Kew pattern marine barometers.","sig":["Kew pattern marine barometer"],"s":"https://www.rmg.co.uk/collections/objects/rmgc-object-384485"},
 {"n":RF,"c":"France","f":"1882","seg":"Heritage manufactory","kf":"recording instruments","d":"Paris instrument firm of Jules and Max Richard, known for recording barometers; RF monogram kept after 1891.","sig":["Richard Frères barograph"],"s":"https://collection.sciencemuseumgroup.org.uk/people/cp53015/jules-richard"},
 {"n":TF,"c":"Germany","seg":"Mainstream","kf":"thermometers, hygrometers","d":"German maker of thermometers, hygrometers and weather stations.","s":"knowledge"}]
trad=[{"n":"English barometer making","g":"Scientific instruments","r":"England (London)","p":"late 18th–19th century",
 "d":"London trade in domestic and marine barometers, with Italian immigrant makers dominant by 1840 and Hatton Garden firms leading the Victorian era.",
 "tech":"mercury tube filling, carved and veneered cases, silvered engraved dials, aneroid movements","mat":"mahogany, oak, brass, glass, mercury",
 "forms":["Stick barometer","Wheel barometer","Admiral FitzRoy barometer","Kew pattern marine barometer","Aneroid barometer","Barograph"],
 "ctr":["Holborn and Hatton Garden, London","Natalo Aiano",NZ,SM,PA],
 "auth":"maker's name and address engraved on the dial or register plate; dates from address directories","s":WB}]
w('04_01',{"kinds":[baro,bg,sg,gt],"brands":brands,"traditions":trad,
 "notes":"Barometer: old kind had no source and 4 models; now 6 archetypes (stick, wheel, Admiral FitzRoy, Kew pattern marine, marine, aneroid) with old models as versions (Kew pattern -> P Adie; Stormoguide and Sputnik -> aneroid; 'Banjo barometer' -> wheel barometer alias). Kind s set to the Wikipedia Barometer article (old kind had none). 'Diagonal barometer' alias became the angle type. Barigo, Fischer and Lufft not added: no fetched page (Barigo trade-fair page 404). New kinds Barograph, Storm glass and Galileo thermometer sourced from Wikipedia and Science Museum Group; Galileo thermometer model moved here from Air thermometer (shelf 04_00). Wikipedia names Alexander Cumming (1760s) as first effective recording barograph, so Richard Frères is listed as the 1880s reference maker rather than originator. Tradition: English barometer making."})
