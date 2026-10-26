import json, os
W = 'https://en.wikipedia.org/wiki/'
VA = W + 'Vernacular_architecture'


def X(n, a, d, y, s, dt, v=None):
    return {"n": n, "a": a, "d": d, "mk": "", "y": y, "s": s, "v": v or [], "dt": dt}


def V(n, y, d):
    return {"n": n, "mk": "", "y": y, "d": d}


def T(n, r, p, d, tech, mat, forms, ctr, auth, s):
    return {"n": n, "g": "Vernacular architecture", "r": r, "p": p, "d": d, "tech": tech, "mat": mat,
            "forms": forms, "ctr": ctr, "auth": auth, "s": s}


brit = {"n": "British & Irish vernacular houses", "a": "British vernacular · Irish vernacular · traditional British houses",
        "d": "Traditional regional house forms of Britain and Ireland, built by local custom from local timber, stone, cob and thatch.",
        "t": ["listed", "unlisted", "restored", "converted"], "s": VA, "x": [
    X("Wealden hall house", "Wealden house · hall house", "Timber-framed medieval hall house with an open central hall between jettied end bays under one roof.",
      "medieval", W + "Wealden_hall_house", "timber frame · wattle and daub or brick infill · thatch, later tile · hall floored over",
      [V("Wealden hall house", "medieval", "Full form with both end bays jettied, mainly Kent and east Sussex."),
       V("Half-Wealden", "", "Only one jettied end, built where town space was limited."),
       V("Floored-over hall", "16th–17th century", "Open hall later floored over to add an upper room.")]),
    X("Cruck house", "cruck-framed house · cruck cottage", "House framed on pairs of curved timbers (crucks) rising from near the ground to meet at the ridge.",
      "from c. mid-13th century", W + "Cruck", "oak crucks · true, base, raised, middle, upper or jointed cruck",
      [V("Full (true) cruck", "", "Blades run from ground to ridge."),
       V("Base cruck", "", "Blades stop at a collar or tie beam."),
       V("Raised cruck", "", "Blades rise from solid walls.")]),
    X("Longhouse", "Devon longhouse · Dartmoor longhouse · Tŷ hir", "Long, narrow, one-room-deep house in which people and animals share one roof, entered by a single passage.",
      "pre-1600 survivors, some before 1400", W + "Longhouse", "cruck frame · rough stone, cob · thatch · Devon, Cornwall, Wales",
      [V("Devon and Exmoor longhouse", "before 1400–1600", "Dozens of early examples survive on Exmoor."),
       V("Welsh Tŷ hir", "", "Welsh form of the longhouse."),
       V("Cumbrian longhouse", "", "Northern English relative.")]),
    X("Blackhouse", "taigh-dubh · teach dubh", "Low house of double dry-stone walls packed with earth, turf thatch and a central hearth with no chimney.",
      "surviving examples under 150 years old; type far older", W + "Blackhouse",
      "double dry-stone walls · turf and straw thatch · flagstone or earth floor · Hebrides, Highlands, Ireland",
      [V("Blackhouse", "", "Smoke-blackened interior from the open central hearth."),
       V("Whitehouse (teach bán)", "", "Later form with harled, rendered stone walls.")]),
    X("Thatched cob cottage", "cob house · clay lump", "Cottage with thick walls of cob, a mix of subsoil, water and straw, typical of the English West Country.",
      "term c. 1600; material prehistoric", W + "Cob_(material)", "cob walls · Devon, Cornwall · clay lump in East Anglia",
      [V("Devon and Cornwall cob", "", "Main traditional area."),
       V("East Anglian clay lump", "", "Regional variant made with clay blocks."),
       V("Modern cob house", "1994", "First new cob home in England in 70 years, built by Kevin McCabe.")]),
    X("Bastle house", "bastle · bastel", "Fortified farmhouse of the Anglo-Scottish border with metre-thick walls and living quarters above a byre.",
      "16th–early 17th century", W + "Bastle_house", "stone walls c. 1 m · vaulted or timber floor · ladder access",
      [V("Classic bastle", "", "Upper living floor reached by a ladder, sometimes with a quenching hole.")]),
    X("Back-to-back house", "back-to-back · back-to-back terrace", "Terraced house sharing walls on two or three sides, with door and windows only at the front.",
      "late 1700s–early 1900s", W + "Back-to-back_house", "brick · northern England, Midlands · Leeds, Bradford",
      [V("Birmingham Back to Backs", "", "Preserved court of back-to-backs (National Trust).")]),
]}

cont = {"n": "Continental European vernacular houses", "a": "European farmhouses · regional European houses",
        "d": "Traditional farmhouse, town-house and tower forms of continental Europe, from north German hall houses to Balkan towers.",
        "t": ["restored", "converted", "listed"], "s": VA, "x": [
    X("Low German house", "Niederdeutsches Hallenhaus · Fachhallenhaus · hall house", "Timber-framed farmhouse with people, livestock and storage under one long hall-like roof.",
      "13th–19th century", W + "Low_German_house", "oak, later pine frame · wattle and daub or brick infill · reed thatch · north Germany, eastern Netherlands"),
    X("Fachwerkhaus", "half-timbered house · timber-framed house", "House with an exposed timber frame infilled with wattle and daub, brick or stone.",
      "from 14th century", W + "Timber_framing", "timber frame on stone or brick base · Germany, Alsace",
      [V("Franconian", "", "Ornate southern regional form."),
       V("Lower Saxon", "", "Northern form close to Dutch and English work."),
       V("Earliest dated example", "1318", "Biberach building.")]),
    X("Black Forest house", "Schwarzwaldhaus", "Farmhouse combining living quarters, workspace and cattle stalls under one long sloping roof.",
      "survivors over 400 years old", W + "Black_Forest_house", "timber on stone base · shingle or thatch, now tile · seven variants (Schilli)",
      [V("Heath house", "", "One of Hermann Schilli's seven variants."),
       V("Gutach house", "", "One of Hermann Schilli's seven variants.")]),
    X("Geestharden house", "Geestharden", "North German longhouse with living and working areas under one roof, one root of Schleswig-Holstein farmhouses.",
      "Bronze Age roots", W + "Geestharden_house", "turf, clay or wood walls, later brick · thatch · Schleswig"),
    X("Uthland-Frisian house", "Frisian house · Uthlandfriesisches Haus", "Frisian variant of the Geestharden house with livestock stall and living area under one roof.",
      "dominant for centuries", W + "Uthland-Frisian_house", "red brick · thatch · ship-timber frame · North Frisian Islands, Halligen"),
    X("Upper Lusatian house", "Umgebindehaus", "Hybrid of log, timber-frame and stone construction with the roof carried separately from the living area.",
      "frame from 13th century; arch late 18th century", W + "Upper_Lusatian_house", "logs or boards · timber frame · rubble stone · Upper Lusatia, Silesia, North Bohemia"),
    X("Frutighaus", "Frutigländer Haus", "Traditional farmhouse type of the Frutigland and Kander valley in the Bernese Oberland.",
      "from 15th century", "https://de.wikipedia.org/wiki/Frutighaus", "timber block construction · masonry plinth and hearth · Canton of Bern"),
    X("Longère", "longhouse (France)", "Long, narrow longhouse of Brittany and Normandy, home of farmers and artisans.",
      "", W + "Long%C3%A8re", "Brittany, Normandy"),
    X("Dutch canal house", "grachtenpand · canal house", "Slim, tall, deep town house on a canal plot, typical of Amsterdam.",
      "plot widths 17th century", W + "Canal_house", "Amsterdam, Haarlem · neck gable · stoop"),
    X("Nordic log house", "Scandinavian log house · stabbur", "House or farm building of solid fitted logs, as in Norway and Sweden.",
      "", W + "Log_building", "solid logs · Norway, Sweden"),
    X("Dacha", "dacha", "Seasonal or year-round second home in the exurbs of Russia and other post-Soviet countries.",
      "from 17th century; Soviet peak 1980s", W + "Dacha", "wood (middle-class) · brick and concrete (elite)"),
    X("Kulla", "Albanian tower house · kullë", "Fortified stone tower house of Kosovo and Albania, usually three storeys with livestock on the ground floor.",
      "17th–19th century", W + "Architecture_of_Kosovo", "stone, early wood and stone · three storeys · Dukagjin",
      [V("Divanhane floor", "", "Top-floor men's gathering room.")]),
    X("Vainakh residential tower", "ghala · Vainakh tower · Chechen tower · Ingush tower", "Stone family tower of the North Caucasus, two to four storeys, livestock below and living above.",
      "11th–18th century", W + "Chechen_tower_architecture", "local stone · lime mortar · central stone pillar · Chechnya, Ingushetia",
      [V("Chechen ghala", "from 12th century", "Usually 3–4 storeys with a central pillar."),
       V("Ingush ghala", "13th–17th century", "Two or three floors, flat earthen roof.")]),
]}
cont["x"][12]["v"][1]  # sanity

med = {"n": "Mediterranean & Iberian houses", "a": "Mediterranean houses · Spanish farmhouses · Italian vernacular",
       "d": "Traditional houses of Iberia, Italy, Greece and North Africa, from farmhouses and manors to stone huts and courtyard houses.",
       "t": ["restored", "converted", "listed"], "s": VA, "x": [
    X("Masía", "masia · mas · masover", "Large, free-standing rural farmhouse of Catalan-speaking lands tied to family farming, with its estate (mas).",
      "medieval onwards", W + "Masia", "rough stone or adobe · lime mortar · arched (pre-16th c.) or lintel door · Catalonia, Valencia, Provence"),
    X("Cortijo", "cortijo andaluz", "Southern Spanish farmstead: large main house with workers' quarters, sheds, granaries and often an oil mill.",
      "possibly Roman villa roots", W + "Cortijo", "stone, adobe, later brick · red clay tile roof · Andalusia, Extremadura"),
    X("Finca", "finca rústica", "Rural estate with a farmhouse or cottage, now also a rural holiday home in Spain and Latin America.",
      "many over 300 years old", W + "Finca", "mainland Spain, Balearics, Canaries, Latin America"),
    X("Pazo", "pazo gallego", "Galician manor house in the countryside, once the seat of local nobility.",
      "17th–19th century", W + "Pazo", "Galicia",
      [V("Pazo de Meirás", "", "Sada; Franco's former summer home."),
       V("Pazo de Cadro", "", "Marín.")]),
    X("Casona", "casona montañesa · casa montañesa", "Stone manor-type house of La Montaña in northern Spain, a grander form of the casa montañesa.",
      "16th–18th century", W + "Casa_monta%C3%B1esa", "rough masonry · ashlar corners · wooden balconies · south façade · Cantabria"),
    X("Casa torre", "Basque tower house · torre", "Medieval stone tower house of northern Spain, Navarre and the Basque Country.",
      "from 8th century; many cut down 1379–1456", W + "Tower_house", "stone · Basque Country, Navarre"),
    X("Trullo", "trulli", "Apulian dry-stone hut with a conical corbelled roof.",
      "golden age 19th century", W + "Trullo", "limestone or tufa without mortar · Itria Valley · UNESCO World Heritage"),
    X("Dammuso", "dammusi", "Stone dwelling of Pantelleria with thick double walls and a domed lime roof that feeds a cistern.",
      "c. 10th century onwards", W + "Dammuso", "volcanic stone · dry-laid double walls · lime dome · Pantelleria, Lampedusa"),
    X("Cycladic house", "Cycladic architecture", "Whitewashed island house of the Cyclades.",
      "", W + "Modern_Greek_architecture", "whitewash · Cyclades"),
    X("Riad", "riyad", "House or palace built round an interior garden courtyard split into four parts with a central fountain.",
      "from early 12th century", W + "Riad_(architecture)", "earthen walls · tadelakt, stucco, zellij · Marrakesh, Maghreb"),
]}

amer = {"n": "Houses of the Americas", "a": "American vernacular houses · folk houses · Caribbean houses",
        "d": "Traditional house types of North America and the Caribbean, from colonial New England forms to Southern and Pueblo houses.",
        "t": ["original", "restored", "revival-built"], "s": VA, "x": [
    X("Cape Cod", "Cape Cod house · Cape", "Low, broad one- or two-storey frame house with a steep gable roof and large central chimney.",
      "from 1600s; revival 1930s–1950s", W + "Cape_Cod_(house)", "timber frame · wood siding · cedar shingles",
      [V("Half Cape", "", "Door at one side with windows to one side."),
       V("Three-quarter Cape", "", "Off-centre door."),
       V("Full Cape", "", "Centred door with two windows each side."),
       V("Colonial Revival Cape", "1930s–1950s", "Mass-built revival form.")]),
    X("Saltbox", "saltbox house", "New England gable house of two storeys in front and one behind under a long low rear roof.",
      "colonial era to c. 1820", W + "Saltbox", "timber frame · mortise-and-tenon · wood siding · Massachusetts, Connecticut"),
    X("Connected farm", "big house, little house, back house, barn", "Farm where house, kitchen, barn and outbuildings are joined into one structure.",
      "17th–19th century", W + "Connected_farm", "wood frame · New England, Maritimes, Delmarva"),
    X("I-house", "I house", "Two-storey, one-room-deep house with side gables.",
      "colonial era to mid-1800s", W + "I-house", "log, frame, brick or stone · Mid-Atlantic, South"),
    X("Upright and wing", "temple and wing · gable and wing", "Folk house with a two-storey gabled upright and a perpendicular one-storey wing.",
      "c. 1830–1890", W + "Upright_and_Wing", "New England, Upper Midwest"),
    X("Charleston single house", "single house", "Charleston house with its narrow end to the street and the door halfway along the long side.",
      "from mid-1700s", W + "Charleston_single_house", "Federal, Greek Revival, Victorian dress · Charleston SC",
      [V("Thomas Legare House", "c. 1759", "Early example.")]),
    X("Creole cottage", "Creole house", "Gulf Coast house with a full front gallery and high gabled roof.",
      "c. 1790–1840", W + "Creole_cottage", "heavy timber frame · brick or bousillage infill · Louisiana, Alabama, Mississippi"),
    X("Shotgun house", "shotgun", "Narrow house about 12 feet wide with rooms in a line and doors at each end.",
      "Civil War to 1920s", W + "Shotgun_house", "wood frame and siding · New Orleans, US South",
      [V("Single shotgun", "", "One unit."),
       V("Double shotgun", "", "Two units sharing a central wall."),
       V("Camelback", "", "Partial second floor at the rear.")]),
    X("Brownstone", "brownstone rowhouse", "Urban row house faced in brown sandstone.",
      "19th century", W + "Brownstone", "brown sandstone · New York, Boston Back Bay, Philadelphia"),
    X("Adobe pueblo-style house", "Pueblo Revival · Santa Fe style", "Flat-roofed, earth-toned stuccoed house modelled on adobe Pueblo buildings.",
      "early 1900s onwards, peak 1920s–30s", W + "Pueblo_Revival_architecture", "adobe, brick or concrete · stucco · flat roof · New Mexico"),
    X("Chattel house", "chattel", "Small movable wooden house of Barbados, built without nails so it can be taken apart.",
      "plantation era to present", W + "Chattel_house", "timber · no nails · on blocks · corrugated iron roof · Barbados"),
]}

asia = {"n": "Asian & Middle Eastern houses", "a": "Asian vernacular houses · courtyard houses",
        "d": "Traditional house forms of East, South and Southeast Asia and the Middle East, from courtyard houses to stilt and earth houses.",
        "t": ["original", "restored", "converted"], "s": VA, "x": [
    X("Siheyuan", "courtyard house · quadrangle", "Chinese house with a courtyard enclosed by buildings on all four sides.",
      "popular Ming–Qing", W + "Siheyuan", "grey brick · lacquered wood · Beijing, Shanxi",
      [V("Beijing siheyuan", "", "Classic northern form."),
       V("Neo-siheyuan villa", "", "Modern concrete version with faux brick.")]),
    X("Fujian tulou", "tulou · earth building", "Large fortified communal house of the Hakka and Minnan with thick rammed-earth walls.",
      "c. 1100s–1900s", W + "Fujian_tulou", "rammed earth · stone · wood · round, square, oval · UNESCO 2008"),
    X("Yaodong", "cave dwelling · loess cave house", "Earth-sheltered dwelling cut into a hillside, dug round a sunken court or built as a vault.",
      "2nd millennium BC; peak Ming–Qing", W + "Yaodong", "loess · brick · stone · Loess Plateau",
      [V("Cliffside yaodong", "", "Cut into a hillside."),
       V("Sunken yaodong", "", "Dug down round a courtyard."),
       V("Hoop yaodong", "", "Freestanding arched form.")]),
    X("Machiya", "kyōmachiya · townhouse", "Japanese wooden townhouse with narrow frontage, deep plot and lattice front.",
      "Heian to Meiji", W + "Machiya", "wood · earthen walls · tile roof · Kyoto",
      [V("Kyōmachiya", "", "Kyoto form.")]),
    X("Minka", "nōka · Japanese farmhouse", "Vernacular Japanese house of farmers, artisans and merchants.",
      "styles matured in Edo period", W + "Minka", "thatch · bamboo · shingle · clay",
      [V("Gasshō-zukuri", "", "Steep thatched roof, Shirakawa."),
       V("Honmune-zukuri", "", "Gabled board-covered roof.")]),
    X("Hanok", "chosŏnjip · Korean house", "Traditional Korean house of timber, earth and stone, with ondol floor heating.",
      "form completed late Joseon", W + "Hanok", "timber · soil · stone · giwa tile or straw · hanji windows",
      [V("Giwa-jip", "", "Tile-roofed."), V("Choga-jip", "", "Straw-roofed."), V("Gulpijip", "", "Bark-shingled.")]),
    X("Shophouse", "tong lau · qilou · ruko", "Building with a shop on the pavement and the owner's home above.",
      "from 1822 Singapore plan", W + "Shophouse", "masonry party walls, later concrete · five-foot way",
      [V("Singapore shophouse", "", "Covered five-foot way."), V("Tong lau", "", "Hong Kong and Macau."),
       V("Qilou", "", "Southern China and Taiwan."), V("Ruko", "", "Modern Indonesian form.")]),
    X("Malay house", "rumah Melayu · kampung house", "Timber and bamboo house raised on stilts, joined without nails.",
      "", W + "Malay_houses", "timber · bamboo · stilts · Malay Peninsula, Sumatra, Borneo",
      [V("Rumah Limas", "", "Regional style."), V("Rumah Bumbung Panjang", "", "Regional style.")]),
    X("Assam-type house", "Assam-type architecture", "Light timber-framed house with steep roof, raised plinth and wide veranda for monsoon and earthquakes.",
      "late 19th–20th century", W + "Assam-type_architecture", "timber · bamboo · ikra reed · mud plaster · corrugated roof"),
    X("Haveli", "havelī", "Traditional townhouse or mansion of the Indian subcontinent built round courtyards.",
      "many 1830–1930", W + "Haveli", "brick · sandstone · marble · wood · Shekhawati, Jaisalmer, Lahore",
      [V("Patwon Ki Haveli", "1805", "Jaisalmer, yellow sandstone.")]),
    X("Wind-tower house", "badgir house · windcatcher house", "Iranian and Gulf house cooled by a windcatcher tower.",
      "ancient; Achaemenid links", W + "Windcatcher", "adobe, stone or brick · Yazd, Kerman, Kashan"),
]}

kinds = [brit, cont, med, amer, asia]
for k in kinds:
    for x in k['x']:
        if not x['v']: del x['v']

trads = [
    T("Wealden hall house", "South-east England (Kent, Sussex)", "Medieval", "Timber-framed open-hall house with jettied end bays.", "timber framing, jettying", "oak, wattle and daub, thatch", ["Wealden hall house"], ["Kent", "east Sussex"], "open hall with smoke-blackened roof timbers; jetties under one roof", W + "Wealden_hall_house"),
    T("Cruck framing", "England and Wales", "From c. 13th century", "Building with paired curved timbers rising to the ridge.", "cruck framing", "oak", ["Cruck house", "Longhouse"], [], "cruck blades visible inside", W + "Cruck"),
    T("Hebridean blackhouse", "Hebrides, Scottish Highlands, Ireland", "Traditional, mostly 19th–20th century survivors", "Low double-walled stone house with turf thatch and central hearth.", "dry-stone walling, turf thatching", "stone, earth, turf, straw", ["Blackhouse"], ["Lewis"], "double dry-stone wall with earth core; no chimney", W + "Blackhouse"),
    T("West Country cob", "Devon, Cornwall; East Anglia (clay lump)", "From c. 1600 (term)", "Mass earth walling of subsoil, water and straw.", "cob walling", "subsoil, straw, water, lime", ["Thatched cob cottage", "Longhouse"], ["Devon", "Cornwall"], "thick monolithic earth walls", W + "Cob_(material)"),
    T("Low German hall house", "North Germany, eastern Netherlands", "13th–19th century", "Timber-framed hall farmhouse for people, animals and crops.", "timber framing", "oak, pine, brick, reed thatch", ["Low German house"], [], "large central threshing door in the gable", W + "Low_German_house"),
    T("German Fachwerk", "Germany, Alsace", "From 14th century", "Exposed timber framing with infill.", "timber framing", "timber, wattle and daub, brick", ["Fachwerkhaus"], ["Biberach"], "pegged joints; regional bracing patterns", W + "Timber_framing"),
    T("Black Forest farmhouse", "Black Forest, south-west Germany", "Survivors over 400 years old", "Farmhouse with living, work and stall under one great roof.", "timber construction", "timber, stone, shingle, thatch", ["Black Forest house"], [], "deep hipped roof on stone base", W + "Black_Forest_house"),
    T("Umgebinde", "Upper Lusatia, Silesia, North Bohemia", "13th century onwards", "Log room carried inside a separate timber support frame.", "log and timber-frame hybrid", "logs, timber, rubble stone", ["Upper Lusatian house"], [], "arched support frame round the log room", W + "Upper_Lusatian_house"),
    T("Albanian kulla", "Kosovo (Dukagjin), Albania", "17th–19th century", "Fortified stone tower house.", "stone masonry", "stone, wood", ["Kulla"], ["Dukagjin"], "three storeys, small windows, firing holes", W + "Architecture_of_Kosovo"),
    T("Vainakh tower building", "Chechnya, Ingushetia", "11th–18th century", "Stone residential and battle towers.", "stone masonry", "stone, lime mortar", ["Vainakh residential tower"], [], "central stone pillar; livestock on ground floor", W + "Chechen_tower_architecture"),
    T("Catalan masia", "Catalonia, Valencia, Aragon, Provence", "Medieval onwards", "Free-standing farmhouse at the centre of a family estate.", "stone masonry", "stone, adobe, lime", ["Masía"], [], "arched doorway on early examples", W + "Masia"),
    T("Apulian trulli", "Apulia (Itria Valley)", "Peak 19th century", "Dry-stone huts with corbelled conical roofs.", "dry-stone corbelling", "limestone, tufa", ["Trullo"], ["Itria Valley"], "mortarless conical roof", W + "Trullo"),
    T("Pantelleria dammuso", "Pantelleria, Lampedusa", "From c. 10th century", "Volcanic-stone house with domed rain-catching roof.", "dry-stone walling, lime domes", "volcanic stone, lime", ["Dammuso"], ["Pantelleria"], "double dry walls; domed lime roof feeding a cistern", W + "Dammuso"),
    T("Moroccan riad", "Maghreb, al-Andalus", "From 12th century", "Inward-looking courtyard house with garden.", "earthen building, tadelakt plaster", "earth, stucco, zellij", ["Riad"], ["Marrakesh"], "four-part garden courtyard with central fountain", W + "Riad_(architecture)"),
    T("New England Cape and saltbox", "New England", "17th century onwards", "Timber-framed colonial house forms.", "timber framing", "timber, wood siding, cedar shingles", ["Cape Cod", "Saltbox"], [], "central chimney; pegged frame", W + "Cape_Cod_(house)"),
    T("Pueblo adobe", "US Southwest", "Traditional; revival from early 1900s", "Flat-roofed earthen houses and their revival.", "adobe building", "adobe, stucco", ["Adobe pueblo-style house"], ["New Mexico", "Santa Fe"], "true adobe walls versus stuccoed frame imitations", W + "Pueblo_Revival_architecture"),
    T("Shotgun house", "US South", "c. 1865–1920s", "Narrow linear-plan house.", "wood-frame building", "wood", ["Shotgun house"], ["New Orleans"], "rooms in a line, doors at each end", W + "Shotgun_house"),
    T("Beijing siheyuan", "Northern China", "Ming–Qing", "Four-sided courtyard house.", "timber frame, brick", "grey brick, lacquered wood", ["Siheyuan"], ["Beijing", "Shanxi"], "enclosed courtyard on all four sides", W + "Siheyuan"),
    T("Fujian tulou", "South-eastern Fujian", "c. 12th–20th century", "Fortified communal rammed-earth houses.", "rammed earth", "earth, stone, bamboo, wood", ["Fujian tulou"], ["Fujian"], "thick rammed-earth outer wall; UNESCO-listed sites", W + "Fujian_tulou"),
    T("Loess yaodong", "Loess Plateau, China", "2nd millennium BC onwards", "Earth-sheltered cave dwellings.", "excavation, vaulting", "loess, brick, stone", ["Yaodong"], ["Shaanxi", "Shanxi", "Gansu"], "cut into loess", W + "Yaodong"),
    T("Kyoto machiya", "Japan, chiefly Kyoto", "Heian–Meiji", "Wooden urban townhouses.", "timber carpentry", "wood, earth, tile", ["Machiya"], ["Kyoto"], "kōshi lattice front; eel-bed plan", W + "Machiya"),
    T("Japanese minka", "Japan", "Matured Edo period", "Folk houses of farmers and townspeople.", "timber carpentry, thatching", "wood, thatch, bamboo, clay", ["Minka"], ["Shirakawa", "Gifu", "Toyama"], "gasshō-zukuri steep thatch", W + "Minka"),
    T("Korean hanok", "Korean Peninsula", "Completed late Joseon", "Timber house with ondol heating.", "timber framing, ondol", "timber, soil, stone, giwa tile, hanji", ["Hanok"], [], "ondol floor; giwa or choga roof", W + "Hanok"),
    T("Malay timber house", "Malay Peninsula, Sumatra, Borneo", "Traditional", "Stilted timber house joined without nails.", "timber joinery", "timber, bamboo", ["Malay house"], [], "raised on stilts; nail-free joints", W + "Malay_houses"),
    T("Haveli building", "North India, Pakistan", "Many 1830–1930", "Courtyard townhouses and mansions.", "masonry, carving, wall painting", "brick, sandstone, marble, wood", ["Haveli"], ["Shekhawati", "Jaisalmer", "Lahore"], "", W + "Haveli"),
    T("Persian windcatcher", "Iranian plateau, Persian Gulf", "Ancient", "Passive cooling towers on houses.", "adobe and brick building", "adobe, brick, stone", ["Wind-tower house"], ["Yazd", "Kerman", "Kashan"], "", W + "Windcatcher"),
]

out = {"kinds": kinds, "brands": [], "traditions": trads,
       "notes": ("New shelf (no old kinds). Old k1 model list absorbed as archetypes: Wealden hall house, bastle house → British; "
                 "Longère, Frutighaus, Geestharden, Uthland-Frisian, Upper Lusatian, Kulla, Vainakh tower (as residential ghala) → Continental; "
                 "Masía (incl. Provençal mas), Cortijo, Finca, Casona, Trullo, Riad → Mediterranean; Charleston single house, chattel house, "
                 "connected farm, upright and wing → Americas; Siheyuan, Yaodong, Assam-type → Asia. 'Bauernhaus' covered by Low German house "
                 "and Black Forest house rather than a generic entry. Casona sourced via casa montañesa page; casa torre via Tower house; "
                 "Cycladic house thinly sourced (Modern Greek architecture). No brands (maker-free patterns). Not added: Irish thatched cottage, "
                 "Epirotic stone house, Scottish tower house (belongs in Castle & tower house). Link-detached house and mews from old k1 belong "
                 "to the House types shelf, not here.")}
p = 'work/G2/shelves/00_03.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print(sum(len(k['x']) for k in kinds), 'archetypes', len(trads), 'traditions')
