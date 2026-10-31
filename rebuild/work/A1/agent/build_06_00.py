import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, v=(), dt='', a=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}

kinds = []
kinds.append({"n": "Cowboy hat", "a": "western hat · Stetson · ten-gallon hat",
 "d": "High-crowned, wide-brimmed felt or straw hat developed for ranch work in the American West.",
 "t": ["crease: cattleman", "crease: pinch front / Carlsbad", "crease: Gus", "crease: brick", "crease: Cool Hand Luke", "crease: Minick",
       "fur felt (beaver, rabbit) · straw · leather", "felt quality grade (X rating)"],
 "s": W + "Cowboy_hat",
 "x": [
  X("Boss of the Plains", "Flat-brimmed, straight-sided open-crowned hat with four-inch crown and brim; the first western model.", "Stetson", "1865", W + "Cowboy_hat",
    [("Boss of the Plains", "Stetson", "1865", "Original, natural colour; still in production.")], "felt grade · colour · open or creased crown"),
  X("Carlsbad", "Front-creased western crown that became the most prominent cowboy style.", "", "late 19th century", W + "Cowboy_hat", [],
    "crease depth · brim width · felt or straw", a="cattleman crease"),
  X("Open Road", "Western hat with a cattleman crown, narrow grosgrain band and shorter town-friendly brim turned up at the edges.", "Stetson", "1948", "https://blog.stetson.com/story-of-the-stetson-open-road/",
    [("1937 precursor", "Stetson", "1937", "Lightweight western-style fedora."), ("Open Road", "Stetson", "1948", "Worn by Truman, Eisenhower and Lyndon B. Johnson ('The L.B.J. Look').")],
    "colour (silverbelly etc.) · felt grade"),
  X("Akubra Cattleman", "Australian rabbit-fur felt bush hat with pinched telescope crown and 3¼-inch brim, made for the Australian Stockman's Hall of Fame.", "Akubra", "", "https://davidmorgan.com/products/cattleman-hat",
    [], "crown 4 in · brim 3¼ in · colours (fawn, bran …)", a="Cattleman"),
  X("Ten-gallon hat", "Unusually large, tall-crowned cowboy hat; the term has been in use since about 1925.", "", "c. 1925", W + "Cowboy_hat", [], "crown height · brim width"),
  X("Calgary White Hat", "White felt cowboy hat symbol of Calgary, first worn at the 1946 Calgary Stampede.", "Smithbilt Hat Company", "1946", W + "Cowboy_hat",
    [("Calgary White Hat", "Smithbilt Hat Company", "1946", "Created by Morris Shumiatcher.")], "white felt · ceremonial gift hat"),
 ]})

kinds.append({"n": "Fedora & trilby", "a": "fedora · trilby · snap-brim · soft felt hat",
 "d": "Soft felt or straw hat with an indented crown pinched at the front and a flexible brim; the trilby has a shorter, downturned brim.",
 "t": ["crown: teardrop", "crown: centre dent", "crown: diamond", "brim width (stingy to wide)", "snap brim", "rabbit or beaver fur felt · wool felt · straw · tweed"],
 "s": W + "Fedora",
 "x": [
  X("Fedora", "Felt hat with soft brim and lengthwise-creased crown pinched at the front, named after Sardou's 1882 play Fédora.", "", "1882 (name in use by 1891)", W + "Fedora",
    [("Prince of Wales adoption", "", "1924", "Start of the 1920s–50s peak.")], "crown about 11 cm · brim about 6.4 cm · felt colours"),
  X("Borsalino felt fedora", "Italian fur-felt fedora tied to the Borsalino trademark and Hollywood films such as Casablanca.", "Borsalino", "1857 (firm)", W + "Borsalino",
    [("Bogart by Borsalino", "Borsalino", "2018", "Collection made with the Humphrey Bogart Estate.")], "felt quality · brim width · colour"),
  X("Stratoliner", "Lightweight, packable 2½-ounce fur-felt fedora with a lower, raked crown, named after Boeing's pressurised airliner.", "Stetson", "1940", "https://blog.stetson.com/high-life-story-of-the-stetson-stratoliner/",
    [("Stratoliner", "Stetson", "1940", "Silver Boeing pin on band; retired post-war."), ("Stratoliner revival", "Stetson", "2009", "Style reissued.")], "colour · felt weight"),
  X("Trilby", "Narrow-brimmed hat, brim angled down at the front and turned up at the back, crown shorter than a fedora; named from the 1895 stage play Trilby.", "", "1895", W + "Trilby",
    [("Christys' trilby", "Christys'", "1894", "Christys dates the trilby's mass popularity to 1894."),
     ("Inspector Clouseau trilby", "Herbert Johnson", "", "Worn by Peter Sellers."),
     ("Harrison", "Lock & Co. Hatters", "", "Crochet trilby (old data).")], "rabbit felt · tweed · straw · cotton"),
 ]})

kinds.append({"n": "Panama hat", "a": "toquilla straw hat · Montecristi · jipijapa",
 "d": "Brimmed hat hand-woven in Ecuador from toquilla palm straw, graded by weave fineness.",
 "t": ["weave: cuenca (herringbone)", "weave: brisa (diamond)", "weave: crochet · torcido", "grade (weaves per inch)", "shape: fedora · boater · optimo", "rollable / foldable"],
 "s": W + "Panama_hat",
 "x": [
  X("Montecristi Panama", "Finest grade of Panama hat woven around Montecristi on the Ecuadorian coast; superfino hats can take months to weave.", "", "19th century", W + "Panama_hat",
    [("Superfino Montecristi", "Lock & Co. Hatters", "", "Lock's highest grade; up to nine months to weave."),
     ("Rollable Superfino Montecristi", "Lock & Co. Hatters", "", ""),
     ("Ventnor Cuenca Ultra-fino", "Lock & Co. Hatters", "", "Cuenca-weave grade.")],
    "carreras per inch · natural or bleached · brim width"),
  X("Rollable Panama", "Panama hat woven fine enough to be rolled and stowed in a tube for travel.", "Lock & Co. Hatters", "", "https://www.lockhatters.com/products/mens-rollable-palm-straw-panama-hat",
    [("Rollable Panama Hat", "Lock & Co. Hatters", "", "Brim 7.5 cm, crown 10 cm, black ribbon.")], "brim · band colour · grade"),
  X("Fedora-shaped Panama", "Panama woven and blocked in fedora shape, the summer hat of choice in the 1920s–30s after the boater.", "", "1920s", W + "Panama_hat",
    [("Classic Panama", "Lock & Co. Hatters", "", "")], "band colour · grade"),
 ]})

kinds.append({"n": "Bowler hat", "a": "Coke hat · derby · billycock · bombín",
 "d": "Hard felt hat with a rounded dome crown and short curled brim, created in 1849 for gamekeepers.",
 "t": ["black · navy · brown · grey", "extra-firm · soft", "square-top"],
 "s": W + "Bowler_hat",
 "x": [
  X("Coke hat", "Original bowler made by Thomas and William Bowler for Lock & Co. for Edward Coke's gamekeepers at Holkham Hall.", "Lock & Co. Hatters", "1849", "https://www.lockhatters.com/blogs/news/why-is-it-called-a-bowler-hat",
    [("Town Coke", "Lock & Co. Hatters", "", ""), ("Extra-Firm Coke", "Lock & Co. Hatters", "", ""), ("Soft Town Coke", "Lock & Co. Hatters", "", ""),
     ("Cambridge", "Lock & Co. Hatters", "", "Rabbit fur felt bowler."), ("The Oddjob", "Lock & Co. Hatters", "", "Limited-edition square-top bowler.")],
    "shellacked linen under rabbit fur felt · colour", a="bowler"),
  X("Christys' bowler", "Bowler from Christys', one of the largest bowler makers from 1849.", "Christys'", "1849", "https://christys-hats.com/pages/since-1773", [], "felt · colour"),
  X("Bombín", "Bowler worn by Quechua and Aymara pollera women in South America from the 1920s.", "", "1920s", W + "Bowler_hat", [], "colour · size worn high on the head"),
 ]})

kinds.append({"n": "Top hat", "a": "topper · silk hat · stovepipe · opera hat",
 "d": "Tall, flat-crowned formal hat with a narrow brim, in silk plush or fur felt.",
 "t": ["silk plush (vintage)", "fur plush / melusine", "grey flat fur felt", "collapsible (opera hat)"],
 "s": W + "Top_hat",
 "x": [
  X("Silk top hat", "Top hat in silk hatter's plush, which replaced beaver felt; first English silk top hat credited to George Dunnage.", "", "1793", W + "Top_hat",
    [("Christys' top hat", "Christys'", "1850", "Prince Albert wore one in 1850.")], "crown height · colour (black, grey)"),
  X("Stovepipe", "Extreme tall top hat with mostly straight sides, popular in the 1840s–50s and with Abraham Lincoln.", "", "1840s", W + "Top_hat", [], "crown height · straight or convex (chimney pot)"),
  X("Opera hat", "Collapsible spring-framed top hat, called a gibus or chapeau claque.", "", "c. 1840", W + "Top_hat",
    [("Dollman elastic round hat", "", "1812", "Early London patent."), ("Gibus", "", "c. 1840", "Antoine Gibus's spring design, France.")], "silk or merino · black", a="gibus · chapeau claque"),
 ]})

kinds.append({"n": "Boater", "a": "straw boater · canotier · skimmer",
 "d": "Semi-formal summer hat of stiff sennit straw with a flat crown, flat brim and ribbon band.",
 "t": ["sennit straw", "ribbon band (plain, club or school colours)", "brim width"],
 "s": W + "Boater_(hat)",
 "x": [
  X("Straw boater", "Stiff sennit straw hat with flat crown and brim, from the Venetian gondolier's canotier; worn at regattas and in school uniform.", "", "late 19th century", W + "Boater_(hat)",
    [("Kreissäge", "", "post-1918", "Narrower German style ('circular saw').")], "brim width · band colours"),
 ],
 "m": [["Classic Boater", "Lock & Co. Hatters"]]})

kinds.append({"n": "Pork pie hat", "a": "porkpie",
 "d": "Short-brimmed hat with a flat crown and circular dent like a pork pie.",
 "t": ["felt · straw", "telescope crown", "snap or upturned brim"],
 "s": W + "Pork_pie_hat",
 "x": [
  X("Keaton flat pork pie", "Flat-topped felt pork pie that Buster Keaton made by stiffening fedora brims.", "", "1920s", W + "Pork_pie_hat", [], "felt · flat brim"),
  X("Telescope pork pie", "1930s–40s men's pork pie with snap brim and dished 'telescopic' crown, worn by jazz musicians such as Lester Young.", "", "1930s", W + "Pork_pie_hat",
    [("Rude boy / ska pork pie", "", "1960s", "Jamaican rude boys, then UK mod and ska scenes.")], "crown height · brim width · colour"),
 ]})

kinds.append({"n": "Homburg", "a": "Anthony Eden hat",
 "d": "Semi-formal fur felt hat with a single gutter crease, stiff curled brim with bound edge and wide grosgrain band.",
 "t": ["black · grey", "pencil-curl brim", "bound edge"],
 "s": W + "Homburg_(hat)",
 "x": [
  X("Homburg", "Hunting hat from Bad Homburg, popularised by the future Edward VII in the 1890s as an alternative to the top hat.", "", "1890s", W + "Homburg_(hat)",
    [("Anthony Eden hat", "", "1930s", "Black homburg made fashionable by Anthony Eden."),
     ("International homburg", "", "1957", "Eisenhower's second-inaugural hat."),
     ("Lock & Co. Homburg", "Lock & Co. Hatters", "", "Favoured by Winston Churchill.")], "colour · brim curl"),
 ]})

kinds.append({"n": "Beret", "a": "Basque beret · béret",
 "d": "Soft, round, flat-crowned cap of felted wool, from Pyrenean shepherds.",
 "t": ["Basque (with cabillou tail)", "military", "merino · felted wool · cotton · leather", "diameter (e.g. 28 cm)"],
 "s": W + "Beret",
 "x": [
  X("Basque beret", "Felted wool beret made commercially around Oloron-Sainte-Marie in Béarn since the 17th century.", "Laulhère", "1840 (Laulhère)", W + "Beret",
    [("Authentique", "Laulhère", "", "French merino wool, one-size 53–59 cm, 28 cm diameter."),
     ("Basque", "Laulhère", "", ""), ("Véritable", "Laulhère", "", ""), ("Bulle", "Laulhère", "", ""), ("Campan", "Laulhère", "", ""), ("Che", "Laulhère", "", "")],
    "diameter · wool · colour"),
  X("Military beret", "Beret as army uniform, from the Chasseurs Alpins and the Royal Tank Regiment's black beret.", "", "1889", W + "Beret",
    [("Chasseurs Alpins beret", "", "1889", ""), ("Royal Tank Regiment black beret", "", "1924", "Made famous by Montgomery.")], "colour by unit · badge"),
  X("Kangol beret", "Wool beret by Kangol, adopted by hip-hop artists such as Run-DMC and LL Cool J in the 1980s.", "Kangol", "1938 (firm)", W + "Kangol",
    [("Spitfire", "Kangol", "1990s", "Furgora (angora mix) style.")], "fabric · colour"),
 ]})

kinds.append({"n": "Bucket hat", "a": "fisherman hat · Irish walking hat · Reni hat",
 "d": "Soft hat with an unshaped crown and a downward-sloping all-round brim, of cotton, canvas, tweed or terry.",
 "t": ["cotton · canvas · tweed · terry / Bermuda", "reversible", "luxury (Gucci, Prada, Loewe)"],
 "s": W + "Bucket_hat",
 "x": [
  X("Irish walking hat", "Tweed or wool-felt hat worn by Irish farmers and fishermen, foldable into a pocket.", "", "c. 1900", W + "Bucket_hat", [], "tweed · lining"),
  X("Bermuda Casual", "Kangol's round-crowned bucket in textured Bermuda pile with 2¼-inch brim, popular in 1980s hip hop.", "Kangol", "", "https://kangol.com/products/bermuda-casual",
    [("Bermuda Casual 0397BC", "Kangol", "", "Current style ID.")], "colours"),
  X("Reni hat", "British bucket hat of the 1990s associated with the Stone Roses and Liam Gallagher.", "", "1990s", W + "Bucket_hat", [], "fabric · colour"),
 ]})

kinds.append({"n": "Sun hat", "a": "floppy hat · harvest hat · field hat · wide-brim hat",
 "d": "Wide-brimmed hat (about 10–18 cm brim) shading face, neck and shoulders from the sun.",
 "t": ["wide-brim straw", "floppy hat", "visor", "UPF-rated fabric", "chin strap"],
 "s": W + "Sun_hat",
 "x": [
  X("Tilley hat", "Cotton-duck brimmed hat with snap-up brim and two straps that floats, designed for sailing by Alex Tilley.", "Tilley", "1980", "https://www.tilley.com/pages/about-us",
    [("T1 Iconic Bucket Hat", "Tilley", "1980", "The original cotton-duck hat."), ("LTM5", "Tilley", "", "Lightweight Nylamtium hat."), ("LTM6 Airflo", "Tilley", "", "Mesh-crown sun hat.")],
    "cotton duck · nylon · brim width"),
  X("Boonie hat", "Wide-brimmed soft military sun hat with branch loops, issued to US forces in Vietnam.", "", "1967", W + "Boonie_hat",
    [("Hat, Jungle, with Insect Net", "", "1967", "First US Army issue."), ("Giggle hat", "", "", "Australian shorter-brim variant.")], "camouflage pattern · ripstop"),
  X("Pith helmet", "Light cloth-covered sun helmet of sola pith or cork, from the Filipino salakot.", "", "18th–19th century", W + "Pith_helmet", [], "pith or cork · cover colour", a="sola topee · safari helmet"),
 ]})

kinds.append({"n": "Fur hat", "a": "winter fur hat · trapper hat",
 "d": "Warm hat of fur, sheepskin or fur imitation, worn in cold climates or as traditional and religious dress.",
 "t": ["real fur (mink, rabbit, muskrat, sable, fox)", "sheepskin / karakul", "faux fur ('fish fur')", "trapper hat"],
 "s": W + "Ushanka",
 "x": [
  X("Ushanka", "Russian round-crowned fur hat with ear-flaps that tie up, under the chin or behind the head.", "", "17th century", W + "Ushanka",
    [("Red Army ushanka", "", "1940", "Adopted after the Winter War."), ("Lei Feng hat", "", "", "Chinese PLA version.")], "fur · earflap tie"),
  X("Papakha", "Tall karakul or sheepskin hat of the Caucasus, adopted by Cossack uniform in 1855.", "", "", W + "Papakha",
    [("Kubanka", "", "", "Shorter version without ear-flaps.")], "karakul · height"),
  X("Shtreimel", "Fur hat of sable, marten or fox tails worn by married Hasidic men on Shabbat and holidays (faith item).", "", "", W + "Shtreimel",
    [("Spodik", "", "", "Taller version of Congress Poland Hasidim."), ("Rain shtreimel", "", "", "Cheaper backup, often synthetic.")], "tail count · fur"),
 ]})

kinds.append({"n": "Cloche & women's millinery", "a": "cloche · pillbox · fascinator · picture hat",
 "d": "Fashion hats for women, from close-fitting cloches to decorative pillboxes, fascinators and wide picture hats.",
 "t": ["pillbox hat", "fascinator", "picture hat", "cartwheel hat", "halo hat", "half hat", "peach basket hat", "boudoir cap"],
 "s": W + "Cloche_hat",
 "x": [
  X("Cloche", "Close-fitting bell-shaped women's hat, usually felt, peaking 1922–33.", "", "1908", W + "Cloche_hat",
    [("Reboux cloche", "Caroline Reboux", "1908", "Credited invention.")], "felt · straw · beads/lace (evening)"),
 ]})

trad_t = [
 "Faith: kippah / yarmulke (Judaism)", "Faith: kolpik (Hasidic)", "Faith: taqiyah (Islam)", "Faith: songkok / kopiah (Islam, Maritime SE Asia)",
 "Faith: zucchetto (Catholic clergy)", "Faith: mitre (bishops)", "Faith: biretta", "Faith: cappello romano", "Faith: capirote (Holy Week)", "Faith: shovel hat (Anglican)",
 "Faith/region: turban (draped)",
 "Uniform: bearskin", "Uniform: busby", "Uniform: shako", "Uniform: kepi", "Uniform: bicorne", "Uniform: tricorne", "Uniform: Hardee hat", "Uniform: campaign hat",
 "Uniform: garrison / forage cap", "Uniform: Glengarry", "Uniform: sailor cap & sailor hat", "Uniform: budenovka",
 "Academic & ceremonial: mortarboard", "Academic & ceremonial: Tudor bonnet", "Scottish: Balmoral bonnet", "Scottish: Tam o' Shanter",
 "East Asia: gat, jeongjagwan, ayam (Korea)", "East Asia: kasa (Japan)", "East Asia: wushamao, guapi mao, damao, weimao (China)", "Asia: conical hat (nón lá, salakot)",
 "Southeast Asia: salakot, buntal hat (Philippines)", "Southeast Asia: blangkon (Java)", "Southeast Asia: tengkolok (Malay)", "Southeast Asia: gaung paung (Myanmar)",
 "South Asia: Gandhi cap", "South Asia: Dhaka topi / Bhadgaunle topi (Nepal)", "South Asia: pakul (Afghanistan, Pakistan)",
 "Middle East & Central Asia: fez", "Middle East & Central Asia: tubeteika", "Middle East & Central Asia: kalpak", "Middle East & Central Asia: telpek", "Middle East & Central Asia: kolah namadi",
 "Africa: kufi", "Africa: kofia (East Africa)", "Africa: mokorotlo (Lesotho)",
 "Europe: barretina (Catalonia)", "Europe: caubeen (Ireland)", "Europe: šajkača (Serbia)", "Europe: qeleshe (Albania)", "Europe: Montenegrin cap", "Europe: Lika cap", "Europe: Tyrolean hat", "Europe: Sami hat / gákti cap", "Europe: montera (bullfighting)", "Europe: sombrero cordobés",
 "Americas: sombrero (charro)", "Americas: sombrero vueltiao (Colombia)", "Americas: chupalla (Chile)", "Americas: coonskin cap",
 "Country & weather: deerstalker", "Country & weather: sou'wester", "Historical: cavalier hat, capotain, pilgrim's hat, wideawake, bycocket, hennin",
 "Historical women's: mobcap, poke bonnet, coal scuttle bonnet, widow's cap",
 "Novelty & costume: party hat, Santa hat, wizard/witch hat, dunce cap, umbrella hat",
]
kinds.append({"n": "Traditional, ceremonial & uniform headwear", "a": "religious headwear · national hats · military headdress",
 "d": "Hats defined by region, faith, rank or ceremony rather than fashion; see the Traditional dress shelves and religious objects (F4).",
 "t": trad_t, "s": W + "List_of_hat_styles"})

brands = [
 {"n": "Stetson", "c": "United States", "f": "1865", "seg": "western & dress hat maker", "d": "Philadelphia hat brand founded by John B. Stetson, originator of the cowboy hat; licensing since the factory closed in 1971.",
  "lines": ["Boss of the Plains", "Open Road", "Stratoliner", "Stetson Royal (women's, 1930s–50s)"], "eras": ["John B. Stetson, 1865–", "Licensing era, 1971–"], "sig": ["Boss of the Plains", "Open Road", "Stratoliner"],
  "sc": ["Western", "cowboy"], "rel": ["Resistol", "Akubra"], "s": W + "Stetson"},
 {"n": "Akubra", "c": "Australia", "f": "1876", "seg": "bush hat maker", "d": "Australian maker of rabbit-fur felt bush hats, founded by Benjamin Dunkerley in Tasmania, now in Kempsey, NSW.",
  "lines": ["Cattleman", "fedoras, homburgs, pork pies"], "eras": [], "sig": ["Akubra Cattleman"], "sc": ["Australian bush"], "rel": ["Stetson"], "s": W + "Akubra"},
 {"n": "Resistol", "c": "United States", "f": "1927", "seg": "western hat maker", "d": "Texas cowboy and dress hat maker founded by E.R. Byer and Harry Rolnick; the name means hats that 'resist all' weather.",
  "lines": ["cowboy hats", "dress hats"], "eras": [], "sig": [], "sc": ["Western", "rodeo"], "rel": ["Stetson"], "s": W + "Resistol"},
 {"n": "Borsalino", "c": "Italy", "f": "1857", "seg": "luxury hat maker", "d": "Alessandria hat maker founded by Giuseppe Borsalino, synonymous with the felt fedora.",
  "lines": ["felt fedoras", "Bogart by Borsalino (2018)"], "eras": ["Borsalino family, 1857–1987", "Haeres Equita, 2016–"], "sig": ["Borsalino felt fedora"], "sc": ["film noir"], "rel": [], "s": W + "Borsalino"},
 {"n": "Lock & Co. Hatters", "c": "United Kingdom", "f": "1676", "seg": "heritage hatter", "d": "St James's Street, London hatter, among the oldest hat shops, which commissioned the first bowler (Coke) in 1849.",
  "lines": ["Coke bowlers", "Panamas", "Homburg", "trilbies"], "eras": ["Lock family"], "sig": ["Coke hat", "Rollable Panama"], "sc": ["English gentleman", "racing & formal"], "rel": ["Christys'"], "s": W + "James_Lock_%26_Co."},
 {"n": "Christys'", "c": "United Kingdom", "f": "1773", "seg": "heritage hatter", "d": "London hat maker founded by Miller Christy; major maker of top hats and bowlers.",
  "lines": ["top hats", "bowlers", "Panamas", "trilbies"], "eras": ["Christy family, 1773–", "Liberty, 2011–", "Laird Hatters, 2026–"], "sig": ["Christys' bowler", "Silk top hat"], "sc": [], "rel": ["Lock & Co. Hatters"], "s": "https://christys-hats.com/pages/since-1773"},
 {"n": "Kangol", "c": "United Kingdom", "f": "1938", "seg": "casual headwear", "d": "British hat maker founded in Cleator, Cumbria by Jacques Spreiregen; berets and buckets adopted by 1980s hip hop.",
  "lines": ["Bermuda", "Spitfire", "berets"], "eras": ["Frasers Group, 2006–"], "sig": ["Bermuda Casual", "Kangol beret"], "sc": ["hip hop"], "rel": [], "s": W + "Kangol"},
 {"n": "Laulhère", "c": "France", "f": "1840", "seg": "beret maker", "d": "Béarn beret maker making berets since 1840; acquired Blancq-Olibet in 2014.",
  "lines": ["Authentique", "Basque", "Véritable", "Che"], "eras": [], "sig": ["Basque beret"], "sc": [], "rel": [], "s": W + "Beret"},
 {"n": "Tilley", "c": "Canada", "f": "1980", "seg": "outdoor & travel hats", "d": "Toronto maker founded by Alex Tilley, whose floating cotton-duck sailing hat became a travel icon.",
  "lines": ["T1", "LTM5", "LTM6 Airflo"], "eras": ["Alex Tilley, 1980–2015", "Gibraltar & Company, 2018–"], "sig": ["Tilley hat"], "sc": ["travel", "outdoor"], "rel": [], "s": W + "Tilley_Endurables"},
]
traditions = [
 {"n": "Ecuadorian toquilla straw hat weaving", "g": "Textiles & rugs", "r": "Ecuador (coast and Azuay)", "p": "19th century to present",
  "d": "Hand-weaving of hats from toquilla palm fibre, inscribed by UNESCO in 2012.", "tech": "fibre boiled, sulphur-bleached and hand-woven from crown to brim; finished by washing, moulding and pressing",
  "mat": "toquilla palm fibre", "forms": ["Panama hat", "Montecristi Panama"], "ctr": ["Montecristi", "Pile", "Cuenca"],
  "auth": "weave count (carreras) and evenness; Montecristi and Pile superfinos are finest", "s": "https://ich.unesco.org/en/RL/traditional-weaving-of-the-ecuadorian-toquilla-straw-hat-00729"},
 {"n": "Béarnais beret making", "g": "Textiles & rugs", "r": "Béarn, south-west France", "p": "17th century to present",
  "d": "Felted wool beret making around Oloron-Sainte-Marie, industrialised in the 19th century.", "tech": "knitted then felted and shaped wool",
  "mat": "wool", "forms": ["Basque beret"], "ctr": ["Oloron-Sainte-Marie", "Laulhère", "Blancq-Olibet"], "auth": "", "s": W + "Beret"},
]
notes = ("'Other hats' (158 entries) dissolved: named makers' models became archetype versions (Stetson Boss of the Plains, Open Road, Stratoliner; Akubra Cattleman; Lock Coke, Rollable Panama, Classic Boater (kept in m), Harrison (crochet trilby, under Trilby); Kangol Bermuda Casual, Spitfire; Laulhère Authentique, Basque, Bulle, Campan, Che, Véritable). "
 "Duplicate 'Boss of the Plains'/'Stratoliner' under John B. Stetson Company vs Stetson merged into Stetson. Generic shapes became kinds (Bowler, Top hat, Boater, Pork pie, Homburg, Beret, Panama, Sun hat, Cowboy hat) or types. "
 "Women's fashion hats (cloche, pillbox, fascinator, picture, cartwheel, halo, half hat, peach basket, boudoir cap) went to a new kind 'Cloche & women's millinery'. Fur hats (ushanka, papakha, shtreimel) became archetypes of Fur hat; boonie and pith helmet archetypes of Sun hat. "
 "Remaining regional, religious, uniform, historical and novelty hats listed as types of 'Traditional, ceremonial & uniform headwear' grouped by faith/region (no models); cross-link to Traditional dress shelves and F4. Deerstalker kept there as a type but may belong in Caps & knit headwear. "
 "Left out (not confirmed on a retrieved page): Akubra Snowy River, Lock Monaco and St. Louis (shape unknown), Greeley and Atwood, Homero Ortega and Optimo, Elósegui, Stüssy bucket, Bailey/Brixton pork pies, Kangol Bermuda Casual launch year. "
 "Pre-Wikipedia 'Breton' (women's hat) and 'Slouch', 'Legionnaire', 'Mushroom hat', 'Printer's hat', 'Smoking cap', 'Whoopee cap', 'Gaitou', 'Humao', 'Liangmao', 'Baishamao', 'Jaapi', 'Mathal', 'Kova tembel', 'Upe', 'Icelandic tail-cap', 'Kłobuk', 'Kołpak', 'Börk', 'Labbadeh', 'Makapili', 'Chilote cap', 'Birke topi', 'Planter's hat', 'Yishan Guan', 'Zhanjiao Futou', 'Liuheyitong mao', 'Phrygian cap', 'Šubara', 'Tembel hat', 'Karakul' not listed individually (covered by group types or as fur-hat/sun-hat/bucket variants; tembel hat is a bucket-hat regional name). "
 "Wikidata helper returned empty results, so all sources are fetched Wikipedia, UNESCO and maker pages.")
out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = 'work/A1/shelves/06_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print(len(kinds), sum(len(k.get('x', [])) for k in kinds), len(brands))
