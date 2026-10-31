import json, os
W='https://en.wikipedia.org/wiki/'
SW='https://www.sweetwater.com/shop/by-category'
def A(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+s,"v":[dict(zip(("n","mk","y","d"),x)) for x in v],"dt":dt}
solid=[
A("Telecaster","Tele · Broadcaster · Esquire","Single-cutaway slab body, bolt-on maple neck, two single coils and a three-saddle fixed bridge; the first mass-produced solid-body Spanish electric.","Fender","1950","Fender_Telecaster",[
 ("Esquire","Fender","1950","single-pickup original, reintroduced 1951"),("Broadcaster","Fender","1950","two-pickup original; renamed after Gretsch 'Broadkaster' conflict"),("Nocaster","Fender","1951","Broadcaster with decal snipped off; unofficial name"),
 ("Telecaster Custom","Fender","1959","bound body; redesigned 1972"),("Telecaster Thinline","Fender","1968","semi-hollow ash body; 1972 version with Wide Range humbuckers"),("Telecaster Deluxe","Fender","1972","produced 1972–1981, later reissued"),
 ("'52 Telecaster reissue","Fender","1982","made 1982–1984 and 1986–2018"),("'50 Broadcaster reissue","Fender","2020",""),("Squier Telecaster","Squier","","Fender-owned import brand")],
 "alder or ash body · 25.5 in scale · single-coil or humbucker configurations · finishes"),
A("Stratocaster","Strat","Contoured double-cutaway body with extended upper horn, three single coils and a six-screw vibrato bridge.","Fender","1954","Fender_Stratocaster",[
 ("Pre-CBS Stratocaster","Fender","1954–1965","before Fender's sale to CBS; hardtail option from March 1955"),("CBS-era Stratocaster","Fender","1965–1985","period of perceived quality decline, notably the 1970s"),
 ("American Vintage reissues ('57, '62)","Fender","1985","vintage reissues from 1985; '57 AVRI discontinued 2012"),("American Standard Stratocaster","Fender","1987","renamed American Series 2000, restored 2008, ended 2016"),
 ("American Professional Stratocaster","Fender","2017","replaced American Standard"),("Eric Clapton Stratocaster","Fender","1988","first Stratocaster signature model"),("Vintera Stratocaster","Fender","2019","50s/60s/70s models; Vintera II 2023"),
 ("Player Stratocaster (Mexico)","Fender","","Mexican-made; Player Plus 2021"),("Custom Classic Strat","Fender","","Custom Shop; discontinued 2008"),("Squier Stratocaster","Squier","","Fender-owned budget brand")],
 "alder or ash body · SSS, HSS or HSH pickups · tremolo or hardtail · maple or rosewood fingerboard · finishes"),
A("Les Paul","LP","Single-cutaway mahogany body with carved maple cap, set mahogany neck, two pickups with separate controls.","Gibson","1952","Gibson_Les_Paul",[
 ("Les Paul Goldtop","Gibson","1952","gold finish, two P-90s; PAF humbuckers from 1957"),("Les Paul Custom","Gibson","1954","black, gold hardware, ebony board; two-pickup reissue 1968"),("Les Paul Junior","Gibson","1954","slab body, one P-90"),("Les Paul Special","Gibson","1955","slab body, two P-90s"),
 ("Les Paul Standard 1958–60 sunburst","Gibson","1958","PAF humbuckers, maple top; c. 1,200–1,700 made; reissued from 1976"),("Les Paul Deluxe","Gibson","1970","mini-humbuckers; to 1985"),("Les Paul Studio","Gibson","1983","lower-priced, carved maple top"),
 ("Custom Shop Historic reissues","Gibson","1986","replicate 1958–60 specs"),("Epiphone Les Paul","Epiphone","","lower-cost copies made outside the US")],
 "P-90 or humbucker · plain or flame maple top · sunburst, goldtop, black · weight and neck profile"),
A("SG","Solid Guitar · Les Paul SG","Thin, bevelled double-cutaway mahogany body with the neck joining three frets further out for upper-fret access.","Gibson","1961","Gibson_SG",[
 ("Les Paul SG","Gibson","1961–1963","early SGs sold under the Les Paul name"),("SG Standard","Gibson","1961","trapezoid inlays, binding"),("SG Special","Gibson","1961","dot inlays"),("SG Junior","Gibson","1961","entry model"),("SG Custom","Gibson","1961","three pickups"),
 ("SG '61 Reissue","Gibson","2007",""),("SG Custom '63 Reissue","Gibson","",""),("Epiphone G-400","Epiphone","","lower-cost SG")],
 "two or three pickups · P-90 or humbucker · Vibrola or stopbar · cherry, walnut, white"),
A("Jazzmaster","","Offset-waist body with separate lead and rhythm circuits, wide soapbar single coils and floating vibrato with lock.","Fender","1958","Fender_Jazzmaster",[
 ("Original Jazzmaster","Fender","1958–1980","unveiled at NAMM 1958; first Fender with rosewood board"),("'62 reissue (Japan)","Fender","1986","with a '66 model"),("American Vintage Reissue '62","Fender","1999–2012",""),("American Vintage '65","Fender","2012",""),
 ("Classic Player Jazzmaster (Mexico)","Fender","2008","Tune-o-matic-style bridge"),("American Professional Jazzmaster","Fender","2017","V-Mod pickups"),("J Mascis Jazzmaster","Fender","2007","Squier version 2011"),("Squier Jagmaster","Squier","1996","budget hybrid")],
 "25.5 in scale · vibrato or hardtail · single coils or humbuckers · finishes"),
A("Jaguar","Jag","Short-scale offset with smaller notched single coils, lead/rhythm circuits, floating vibrato and spring-loaded string mute.","Fender","1962","Fender_Jaguar",[
 ("Original Jaguar","Fender","1962–1975","24 in scale, 22 frets"),("Japanese Jaguar","Fender","1984–2015",""),("American Vintage Reissue '62","Fender","1999",""),("Kurt Cobain Jaguar","Fender","2011","signature"),
 ("American Vintage '65","Fender","2012","replaced AVRI"),("American Original Jaguar","Fender","2018",""),("Squier Classic Vibe '70s Jaguar","Squier","2019","")],
 "24 in scale · vibrato · single coils or humbuckers · finishes"),
A("Flying V","V","V-shaped solid body, originally korina, with set neck, two humbuckers and Tune-o-matic bridge.","Gibson","1958","Gibson_Flying_V",[
 ("1958–59 Korina Flying V","Gibson","1958","98 made"),("1967 Flying V","Gibson","1967","mahogany, large pickguard, Vibrola; now the standard design"),("Flying V2","Gibson","1979–1982","walnut/maple, boomerang pickups"),
 ("Reverse Flying V","Gibson","2007","body rotated 180°"),("Flying V Pro","Gibson","2016",""),("Murphy Lab '58 Korina","Gibson","2021","81 aged reissues")],
 "korina or mahogany · Vibrola or stopbar · finishes"),
A("Explorer","Futura","Angular, futuristic solid body (originally korina) with two or three humbuckers and a long drooping headstock.","Gibson","1958","Gibson_Explorer",[
 ("Futura prototype","Gibson","1957","shown at NAMM"),("Korina Explorer","Gibson","1958–1963","19 made in 1958"),("Limited Edition reissue","Gibson","1976","mahogany, gold hardware"),("Explorer II (E2)","Gibson","1979–1983",""),
 ("Explorer III","Gibson","1984–1985","P-90s"),("Explorer Pro","Gibson","2007",""),("Explorerbird (Lzzy Hale)","Gibson","2022","signature")],
 "korina, mahogany, alder or maple · two or three humbuckers · finishes"),
A("Firebird","","Neck-through 'reverse' body with stepped centre, reversed six-in-line headstock and covered mini-humbuckers; styled by car designer Ray Dietrich.","Gibson","1963","Gibson_Firebird",[
 ("Firebird V","Gibson","1963",""),("Non-reverse Firebird (Custom Shop)","Gibson","2002",""),("Johnny Winter Firebird","Gibson","","signature")],
 "reverse or non-reverse body · finishes incl. custom colours"),
A("Custom 24","PRS Custom","Double-cutaway carved-top guitar blending Strat and Les Paul ideas, 25 in scale, PRS tremolo and coil-split humbuckers.","PRS","1985","PRS_Guitars",[
 ("Custom 24 (rotary selector)","PRS","1985","first PRS production model"),("Custom 22","PRS","1993","22-fret version"),("Custom 24 five-way blade","PRS","2011","rotary replaced by blade switch"),("McCarty","PRS","1994","deeper body, three-way toggle"),
 ("SE Custom 24","PRS","2000","lower-priced SE line, Korea then Indonesia/China")],
 "flame or quilt maple top · 10-top grades · tremolo or stoptail · finishes"),
A("Singlecut (PRS)","","PRS's Les Paul-like single-cutaway carved-top model.","PRS","2000","PRS_Guitars",[],"maple top · humbuckers"),
A("Silver Sky","","PRS's Stratocaster-style single-coil model co-designed with John Mayer.","PRS","2018","PRS_Guitars",[],"three single coils · vintage tremolo · finishes"),
A("Superstrat","Shred guitar · S-type with humbuckers","Strat-derived body with pointed horns, deep cutaways, 24 frets, humbuckers and a locking vibrato (usually Floyd Rose).","","1980s","Superstrat",[
 ("Kramer Baretta","Kramer","1983–1991",""),("Dean Bel Aire","","1983–1984",""),("Fender Contemporary Stratocaster (Japan)","Fender","1984–1987",""),("Gibson US-1","Gibson","1986–1991",""),("Fender HM Strat","Fender","1988–1992","")],
 "HSS/HSH/HH · Floyd Rose or fixed · neck-through or bolt-on"),
A("Soloist","Jackson Soloist · SL","Neck-through superstrat with deeper lower horn, sharp edges, Floyd Rose and sharkfin inlays; often called the first definitive mass-produced superstrat.","Jackson","1984","Jackson_Soloist",[
 ("Custom and Student Soloist","Jackson","1984","made to order"),("SL1","Jackson","","USA flagship; Custom Shop only from 2021"),("SL2H","Jackson","","USA, two Seymour Duncans; ended 2021"),("SL3 (Pro Series)","Jackson","","Japanese-made"),("American Series SL3","Jackson","2022","Corona, California")],
 "Floyd Rose, Kahler or fixed · inlays · finishes"),
A("JEM","Ibanez JEM · JEM777","Steve Vai superstrat with monkey grip, scalloped top frets, 'lion's claw' rout behind the Edge tremolo and DiMarzio HSH pickups.","Ibanez","1987","Ibanez_JEM",[
 ("JEM777","Ibanez","1987","original, incl. Loch Ness Green"),("JEM77","Ibanez","1988","77FP, 77VBK, 77WDP 'Woody'"),("JEM7V","Ibanez","1993","JEM7VWH 1993–2019"),("JEM555 (JEM Jr)","Ibanez","1994","Korean-made"),("30th Anniversary JEM777 reissue","Ibanez","","")],
 "HSH DiMarzio · Edge tremolo · vine inlay · finishes"),
A("RG","Roadstar Guitar · RG550","Thin, flat, wide 24-fret neck on a pointed offset double-cutaway body, usually with Edge tremolo; a staple of shred and metal.","Ibanez","1987","Ibanez_RG",[
 ("RG550","Ibanez","1987","first model, sold as Roadstar"),("RG Prestige","Ibanez","1996","Japanese-made by FujiGen"),("RG7620/RG7621","Ibanez","1998","seven-string")],
 "six or seven strings · Edge or fixed bridge · HSH/HH")]
semi=[
A("ES-335","335 · dot neck","Thinline double-cutaway with maple centre block, f-holes, two humbuckers and Tune-o-matic bridge.","Gibson","1958","Gibson_ES-335",[
 ("Dot-neck ES-335","Gibson","1958","dot inlays until mid-1962, then blocks"),("ES-345","Gibson","1958","Varitone, stereo; returned c. 2020"),("ES-355","Gibson","1958–1982","ebony board, split-diamond inlay"),("Trini Lopez Standard","Gibson","1964–1971","diamond soundholes"),
 ("B.B. King Lucille","Gibson","1981","ES-355-based, no f-holes"),("CS-336 / ES-339","Gibson","2007","smaller bodies"),("Epiphone Dot, Sheraton, Riviera","Epiphone","","lower-cost versions")],
 "dot or block inlays · stopbar or Bigsby · sunburst, cherry, natural"),
A("Rickenbacker 330","330 · Capri","Double-cutaway semi-hollow with slash soundhole, two single coils, dual truss rods and R tailpiece.","Rickenbacker","1958","Rickenbacker_330",[
 ("330","Rickenbacker","1958","designed by Roger Rossmeisl; blend knob added 1961"),("331 Light Show","Rickenbacker","1970–1974","built-in light organ"),("340 and 340/12","Rickenbacker","","three pickups; 12-string"),("330/12","Rickenbacker","","12-string")],
 "Mapleglo, Fireglo, Jetglo · six or twelve strings"),
A("Rickenbacker 360","360 · 360/12","Bound deluxe semi-hollow with 'crescent moon' cutaway, triangle inlays and stereo Rick-O-Sound option.","Rickenbacker","1958","Rickenbacker_360",[
 ("360/12 (early style)","Rickenbacker","","George Harrison's until August 1965"),("360/12 (new style)","Rickenbacker","1965","rounded cutaways and top edge"),("370","Rickenbacker","","three pickups")],
 "six or twelve strings · mono or stereo · Mapleglo, Fireglo, Jetglo, Midnight Blue")]
hollow=[
A("L-5","","Carved archtop with f-holes designed by Lloyd Loar; the template for the jazz archtop, later electrified.","Gibson","1923","Gibson_L-5",[
 ("L-5 (acoustic)","Gibson","1923","16 in, 17 in from c. 1934–35"),("L-5 cutaway","Gibson","1939",""),("L-5 CES","Gibson","1951","P-90s, humbuckers from 1958"),("L-5CT","Gibson","1958–1963","thin body, about 45 made"),("L-5S","Gibson","1970s","solid-body version")],
 "acoustic or electric · cutaway or non-cutaway · sunburst or natural"),
A("Super 400","","Gibson's largest carved archtop, named after its $400 price; later a cutaway electric.","Gibson","1934","Gibson_Super_400",[
 ("Super 400 (1934)","Gibson","1934","engraved tailpiece"),("Super 400P / 400C","Gibson","1939","Premiere cutaway, enlarged upper bout"),("Super 400 CES","Gibson","1950s","two P-90s, humbuckers from 1957")],
 "acoustic or CES electric · sunburst or natural"),
A("ES-175","175","Laminated maple jazz box with pointed Florentine cutaway, floating bridge and trapeze tailpiece.","Gibson","1949","Gibson_ES-175",[
 ("ES-175 (one P-90)","Gibson","1949","single pickup to 1971"),("ES-175D","Gibson","1953","two P-90s"),("Humbucker ES-175","Gibson","1957","PAF humbuckers; discontinued 2019")],
 "one or two pickups · sunburst or natural"),
A("Gretsch 6120","Chet Atkins Hollow Body · 6120 Nashville","Orange maple-laminate hollow body with f-holes and Bigsby; the first Chet Atkins signature Gretsch.","Gretsch","1955","Gretsch_6120",[
 ("Chet Atkins Hollow Body 6120","Gretsch","1955","DeArmond Dynasonics; Filter'Trons from 1958"),("6120 Nashville","Gretsch","1960s",""),("Brian Setzer G6120-SSLVO / SSU","Gretsch","1993–2003","signature"),("Eddie Cochran","Gretsch","2011","signature"),("Duane Eddy","Gretsch","1997","signature; again from 2011")],
 "Dynasonic or Filter'Tron · Bigsby · orange and other finishes"),
A("White Falcon","6136 · 6137","Gretsch's showpiece 17 in hollow body with gold sparkle binding, engraved falcon pickguard and gold hardware.","Gretsch","1955","Gretsch_White_Falcon",[
 ("6136 single-cutaway","Gretsch","1955","designed by Jimmie Webster; Dynasonics to 1958"),("Filter'Tron White Falcon","Gretsch","1958","Space Control bridge"),("Double-cutaway White Falcon","Gretsch","1962","Bigsby standard"),("6137 stereo","Gretsch","",""),("Modern reissues","Gretsch","1996","incl. Stephen Stills, Billy Duffy signatures")],
 "single or double cutaway · mono or stereo · white, black, silver"),
A("ES-330","330","Thinline fully hollow Gibson with ES-335 dimensions, P-90 pickups and no centre block.","Gibson","1959","Gibson_ES-330",[
 ("ES-330T","Gibson","1959","one P-90"),("ES-330TD","Gibson","1959","two P-90s; neck at 19th fret from 1968; ended 1972")],
 "cherry, sunburst, natural, walnut"),
A("Casino","Epiphone Casino","Thinline fully hollow Epiphone with P-90s and trapeze or Bigsby; ES-330's lighter, louder cousin.","Epiphone","1961","Epiphone_Casino",[
 ("Pre-1970 Casino","Epiphone","1961","17° headstock"),("Korean/Chinese Casino","Epiphone","","Korea until 2007, then China"),("USA Casino","Epiphone","2021","Gibson USA-made"),("Original Collection Casino","Epiphone","2023","")],
 "one or two P-90s · trapeze or Bigsby · finishes"),
A("D'Angelico New Yorker","New Yorker · Excel","Hand-carved New York archtops by John D'Angelico: the 18 in New Yorker and 17 in Venetian-cutaway Excel.","D'Angelico","1936","D%27Angelico_Guitars",[
 ("New Yorker","D'Angelico","1936","18 in; about 300 made"),("Excel","D'Angelico","","17 in, Venetian cutaway"),("Revived D'Angelico","D'Angelico","2011","trademark brand relaunch")],
 "acoustic or with pickups · sunburst or natural"),
A("Benedetto archtop","","Hand-carved jazz archtops by luthier Robert Benedetto, built since 1968 and licensed to Fender 1999–2006.","Benedetto","1968","Robert_Benedetto",[
 ("La Cremona Azzurra","Benedetto","1996","blue archtop for Scott Chinery"),("Fender Custom Shop Benedetto","Fender","1999–2006","licensed models")],
 "17–18 in carved spruce/maple · floating pickup"),
A("Danelectro U2","U2 · '56 U2","Low-cost Masonite-and-poplar hollow guitar with lipstick-tube pickups and a single cutaway.","Danelectro","1956","Danelectro",[
 ("U2","Danelectro","1956–1958",""),("Shorthorn / 59-DC","Danelectro","1959","double cutaway"),("U2 reissue","Danelectro","late 1990s","Evets revival; '56 Pro 2006")],
 "lipstick pickups · finishes")]
kinds=[
 {"n":"Solid-body electric guitar","a":"solidbody electric","d":"Electric guitar with a solid wooden body and magnetic pickups.","t":["S-type (Stratocaster type)","T-type (Telecaster type)","Single-cut (Les Paul type)","Double-cut","Offset","V-type","Explorer-type","Seven- and eight-string","Headless","Baritone"],"s":SW,"x":solid},
 {"n":"Semi-hollow electric guitar","a":"thinline · semi-acoustic","d":"Electric guitar with hollow wings around a solid centre block.","s":SW,"x":semi},
 {"n":"Hollow-body electric guitar","a":"archtop electric · jazz box","d":"Electric guitar with a fully hollow, usually archtop body.","t":["Full-depth archtop","Thinline hollow body","Carved top","Laminated top"],"s":SW,"x":hollow}]
K="knowledge"
brands=[
 {"n":"Fender","c":"United States","f":"1946","seg":"Mainstream to Custom Shop","d":"Californian maker of the Telecaster and Stratocaster and the first mass-market solid-body electric.","lines":["American Professional","American Vintage","Player","Vintera","Custom Shop"],"eras":["Pre-CBS, to 1965","CBS, 1965–1985"],"sig":["Telecaster","Stratocaster","Jazzmaster","Jaguar"],"rel":["Squier","Jackson","Charvel","Gretsch"],"s":K},
 {"n":"Gibson","c":"United States","f":"1902","seg":"Mainstream to Custom Shop","d":"Michigan-born, Nashville-based maker of the Les Paul, SG, ES-335 and Gibson archtops.","lines":["Original","Modern","Custom Shop","Murphy Lab"],"sig":["Les Paul","SG","ES-335","Flying V","Explorer","Firebird","L-5","Super 400","ES-175"],"rel":["Epiphone","Kramer"],"s":K},
 {"n":"Epiphone","c":"United States","f":"1873","seg":"Budget to mid","d":"Former New York archtop rival bought by Gibson, now its lower-priced brand.","sig":["Casino","Les Paul","G-400","Dot"],"rel":["Gibson"],"s":K},
 {"n":"Squier","c":"United States","seg":"Budget","d":"Fender-owned budget brand making Fender designs in Asia.","lines":["Classic Vibe","Affinity","Bullet"],"sig":["Stratocaster","Telecaster"],"rel":["Fender"],"s":K},
 {"n":"Gretsch","c":"United States","f":"1883","seg":"Mid to premium","d":"New York firm known for flashy hollow bodies and rockabilly guitars.","lines":["Professional","Players Edition","Electromatic","Streamliner"],"sig":["Gretsch 6120","White Falcon"],"rel":["Fender"],"s":K},
 {"n":"Rickenbacker","c":"United States","f":"1931","seg":"Premium","d":"Californian maker of jangly 300-series semi-hollows and 12-strings.","sig":["Rickenbacker 330","Rickenbacker 360"],"s":K},
 {"n":"PRS","c":"United States","f":"1985","seg":"Premium to mid","d":"Paul Reed Smith's Maryland maker of carved-top double-cutaways.","lines":["Core","S2","CE","SE","Private Stock"],"sig":["Custom 24","McCarty","Silver Sky"],"s":W+"PRS_Guitars"},
 {"n":"Ibanez","c":"Japan","seg":"Budget to premium","d":"Hoshino Gakki's brand, central to superstrats and shred guitars.","lines":["Prestige","Premium","Standard","GIO"],"sig":["RG","JEM"],"s":K},
 {"n":"Jackson","c":"United States","f":"1980","seg":"Mid to Custom Shop","d":"Californian metal-guitar maker of the Soloist and Rhoads; Fender-owned since 2002.","sig":["Soloist"],"rel":["Charvel","Fender"],"s":K},
 {"n":"Charvel","c":"United States","seg":"Mid to Custom Shop","d":"Californian hot-rod superstrat maker linked to Jackson; Fender-owned since 2002.","rel":["Jackson","Fender"],"s":K},
 {"n":"Kramer","c":"United States","f":"1976","seg":"Budget to mid","d":"1980s superstrat leader, now a Gibson brand.","sig":["Baretta"],"rel":["Gibson"],"s":K},
 {"n":"ESP","c":"Japan","f":"1975","seg":"Budget to premium","d":"Tokyo maker of metal-oriented electrics, with LTD as its lower-priced line.","lines":["ESP Original","E-II","LTD"],"s":K},
 {"n":"Schecter","c":"United States","f":"1976","seg":"Mid","d":"Californian maker best known today for modern metal guitars.","s":K},
 {"n":"Yamaha","c":"Japan","f":"1887","seg":"Budget to premium","d":"Japanese instrument giant whose electric lines include the Pacifica and Revstar.","lines":["Pacifica","Revstar"],"s":K},
 {"n":"Danelectro","c":"United States","f":"1947","seg":"Budget","d":"Nathan Daniel's New Jersey maker of Masonite guitars with lipstick-tube pickups.","sig":["Danelectro U2"],"s":W+"Danelectro"},
 {"n":"D'Angelico","c":"United States","f":"1932","seg":"Luthier / premium","d":"John D'Angelico's Little Italy archtop workshop; brand revived in 2011.","sig":["D'Angelico New Yorker"],"s":W+"D%27Angelico_Guitars"},
 {"n":"Benedetto","c":"United States","f":"1968","seg":"Luthier","d":"Robert Benedetto's hand-carved jazz archtops; Savannah facility from 2006.","sig":["Benedetto archtop"],"rel":["Fender"],"s":W+"Robert_Benedetto"}]
notes=("Old flat models Fender Stratocaster/Telecaster, Gibson Les Paul/SG became archetypes; generic S-type, T-type, single-cut, double-cut, V-type, Explorer-type moved to 't'. "
 "Superstrat added as maker-free archetype. Left out: Gretsch Electromatic semis, Gibson Firebird I/III/VII, Ibanez Genesis reissues, Benedetto model names (La Venezia etc.), Epiphone Elitist/Revolution Casinos — not confirmed on retrieved pages. "
 "Wikipedia API rate-limited (429), so all sources are WebFetch'd Wikipedia articles; Benedetto_Guitars 404, used Robert_Benedetto. "
 "Brand facts for Fender, Gibson, Epiphone, Squier, Gretsch, Rickenbacker, Ibanez, Jackson, Charvel, Kramer, ESP, Schecter, Yamaha from knowledge (s=knowledge); Charvel founding year omitted (unsure).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/E3/shelves/00_00.json'; os.makedirs('work/E3/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(sum(len(k['x']) for k in kinds))
