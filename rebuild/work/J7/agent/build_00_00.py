import json, os
WP = 'https://en.wikipedia.org/wiki/'
WD = 'https://www.wikidata.org/wiki/'
OLD = 'https://www.wine.com/list/wine/red-wine/7155-124'
def X(n, d, s, mk='', y='', a='', v=None, dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s}
    if v: x["v"] = [dict(zip(("n","mk","y","d"), t)) for t in v]
    if dt: x["dt"] = dt
    return x
def gc(n, s, commune, extra=''):
    return X(n, f"Grand cru vineyard and appellation in {commune}, Côte de Nuits, for Pinot Noir.{extra}", s)
CDN = "Côte de Nuits"
kinds = []

kinds.append({"n": "Cabernet Sauvignon", "a": "Cab · Cabernet", "d": "Still red wine made mainly from the Cabernet Sauvignon grape.", "s": OLD,
 "x": [
  X("Napa Valley Cabernet Sauvignon", "Cabernet-led red from the Napa Valley AVA in California, established 1981, with 17 sub-AVAs such as Oakville and Rutherford.", WP+"Napa_Valley_AVA", y="1981",
    v=[("Stag's Leap Wine Cellars Cabernet Sauvignon 1973", "Stag's Leap Wine Cellars", "1973", "won the red wine section of the 1976 Judgment of Paris tasting"),
       ("Stag's Leap Wine Cellars Artemis Cabernet Sauvignon", "Stag's Leap Wine Cellars", "", ""),
       ("Heitz Martha's Vineyard Cabernet Sauvignon 1970", "Heitz Wine Cellars", "1970", "one of the Californian reds in the 1976 Paris tasting"),
       ("Caymus Napa Valley Cabernet Sauvignon", "Caymus", "", "")],
    dt="sub-AVA (Oakville, Rutherford, Stags Leap District, Howell Mountain…) · vintage · single vineyard vs blend"),
  X("Screaming Eagle", "Small-production Oakville cult wine based on Cabernet Sauvignon; estate founded 1986, first vintage 1992.", WP+"Screaming_Eagle_Winery_and_Vineyards", mk="Screaming Eagle", y="1992",
    v=[("Screaming Eagle 1992", "Screaming Eagle", "1992", "first vintage, released 1995")]),
  X("Opus One", "Napa Valley winery and its eponymous red wine.", WD+"Q448588", mk="Opus One"),
  X("Coonawarra Cabernet Sauvignon", "Cabernet from the terra rossa soils over limestone of Coonawarra, South Australia, first planted by John Riddoch in 1890.", WP+"Coonawarra_wine_region", y="1890",
    v=[("Wynns Wynvale Cabernet Sauvignon", "Wynns", "", "")], dt="terra rossa strip · vintage"),
  X("Sassicaia", "Bolgheri Super Tuscan of about 85% Cabernet Sauvignon and 15% Cabernet Franc, first made in 1948; first commercial vintage 1968.", WP+"Sassicaia", mk="Tenuta San Guido", y="1968",
    v=[("Sassicaia 1968", "Tenuta San Guido", "1968", "first commercial vintage, unveiled 1971"), ("Bolgheri Sassicaia DOC", "Tenuta San Guido", "1994", "own DOC granted")]),
 ],
 "m": [["Penfolds Bin 407 Cabernet Sauvignon", "Penfolds"], ["Silver Oak Alexander Valley Cabernet Sauvignon", "Silver Oak"],
       ["Nickel & Nickel John C. Sullenger Vineyard Cabernet Sauvignon", "Nickel & Nickel"], ["Kenwood Vineyards Six Ridges Cabernet Sauvignon", "Kenwood Vineyards"],
       ["Baron Philippe de Rothschild Escudo Rojo Origine Cabernet Sauvignon", "Baron Philippe de Rothschild"], ["Trapiche Terroir Series Laborde Cabernet Sauvignon", "Trapiche"],
       ["Kleine Zalze Family Reserve Cabernet Sauvignon", "Kleine Zalze"], ["Spier Wines 21 Gables Cabernet Sauvignon", "Spier Wines"],
       ["Stella Bella Wines Suckfizzle Cabernet Sauvignon", "Stella Bella Wines"], ["Xanadu Reserve Cabernet Sauvignon", "Xanadu"], ["Lenton Brae Cabernet Sauvignon", "Lenton Brae"]]})

pn = [
  X("Romanée-Conti", "1.8-hectare grand cru monopole in Vosne-Romanée, named after the Prince of Conti who bought it in 1760.", WP+"Domaine_de_la_Roman%C3%A9e-Conti", mk="Domaine de la Romanée-Conti", y="1760"),
  X("La Tâche", "Grand cru monopole in Vosne-Romanée, Côte de Nuits.", WD+"Q923449", mk="Domaine de la Romanée-Conti"),
  X("Chambertin", "Grand cru of about 15 ha in Gevrey-Chambertin; AOC since 1937; head of the Chambertin family of grands crus.", WP+"Chambertin", y="1937",
    dt="satellites: Charmes-, Mazoyères-, Chapelle-, Griotte-, Latricières-, Mazis-, Ruchottes-Chambertin"),
  X("Chambertin-Clos de Bèze", "Grand cru bordering Chambertin to the north in Gevrey-Chambertin; may also be sold as Chambertin.", WD+"Q2948095"),
  X("Musigny", "Grand cru in Chambolle-Musigny, Côte de Nuits.", WD+"Q641077"),
  X("Richebourg", "Grand cru in Vosne-Romanée, AOC since 1936; about 7.4 ha in production, half held by Domaine de la Romanée-Conti.", WP+"Richebourg_AOC", y="1936"),
  X("Romanée-Saint-Vivant", "Grand cru vineyard in Vosne-Romanée, Côte de Nuits.", WD+"Q2165002"),
  X("La Romanée", "Grand cru in Vosne-Romanée, Côte de Nuits.", WD+"Q753438"),
  X("La Grande Rue", "Grand cru in Vosne-Romanée, Côte de Nuits.", WD+"Q1555244"),
  X("Grands Échezeaux", "Grand cru in Flagey-Échezeaux, Côte de Nuits.", WD+"Q1542916"),
  X("Échezeaux", "Grand cru in Flagey-Échezeaux, Côte de Nuits.", WD+"Q273390"),
  X("Clos de Vougeot", "Walled 50.6-ha grand cru created by Cistercian monks of Cîteaux, the largest in the Côte de Nuits, now split among more than 80 owners.", WP+"Clos_de_Vougeot", y="12th–14th century"),
  X("Bonnes-Mares", "Grand cru vineyard in the Côte de Nuits.", WD+"Q892772"),
  X("Clos de Tart", "Grand cru in Morey-Saint-Denis, Côte de Nuits.", WD+"Q1102353"),
  X("Clos de la Roche", "Grand cru in Morey-Saint-Denis, Côte de Nuits.", WD+"Q1102361"),
  X("Clos Saint-Denis", "Grand cru in Morey-Saint-Denis, Côte de Nuits.", WD+"Q1102349"),
  X("Clos des Lambrays", "Grand cru in Morey-Saint-Denis, Côte de Nuits.", WD+"Q596588"),
  X("Mazis-Chambertin", "Chambertin satellite grand cru in Gevrey-Chambertin.", WD+"Q646011"),
  X("Charmes-Chambertin", "Chambertin satellite grand cru in Gevrey-Chambertin.", WD+"Q2961100"),
  X("Mazoyères-Chambertin", "Chambertin satellite grand cru in Gevrey-Chambertin.", WD+"Q3303152"),
  X("Griotte-Chambertin", "Chambertin satellite grand cru in Gevrey-Chambertin.", WD+"Q3116771"),
  X("Chapelle-Chambertin", "Chambertin satellite grand cru in Gevrey-Chambertin.", WD+"Q2956528"),
  X("Latricières-Chambertin", "Chambertin satellite grand cru in Gevrey-Chambertin.", WD+"Q283167"),
  X("Ruchottes-Chambertin", "Chambertin satellite grand cru in Gevrey-Chambertin.", WD+"Q3446619"),
  X("Central Otago Pinot Noir", "Pinot Noir from New Zealand's Central Otago, where it fills over 80% of plantings; subregions include Bannockburn, Gibbston and Bendigo.", WP+"Central_Otago_wine_region",
    dt="subregion (Bannockburn, Bendigo, Gibbston, Wānaka, Alexandra, Cromwell) · vintage"),
  X("Willamette Valley Pinot Noir", "Pinot Noir from Oregon's Willamette Valley AVA (1983), pioneered by Eyrie Vineyard; sub-AVAs include Dundee Hills and Eola-Amity Hills.", WP+"Willamette_Valley_AVA", y="1983",
    v=[("Alexana Estate Vineyard Pinot Noir", "Alexana", "", "")], dt="sub-AVA (Dundee Hills, Eola-Amity Hills, Ribbon Ridge…) · vintage"),
]
# Alexana is in Dundee Hills? not confirmed -> remove version
pn[-1].pop("v")
kinds.append({"n": "Pinot Noir", "a": "Pinot Nero · Spätburgunder · red Burgundy", "d": "Still red wine made mainly from the Pinot Noir grape; red Burgundy is its classic home.", "s": OLD,
 "t": ["Grand cru", "Premier cru", "Village", "Regional (Bourgogne)"], "x": pn,
 "m": [["Corton", ""], ["Craggy Range Pinot Noir", "Craggy Range"], ["Te Kairanga Pinot Noir", "Te Kairanga"], ["Palliser Estate Hua Nui Vineyard Pinot Noir", "Palliser Estate"],
       ["Rockburn Crimson Peak Pinot Noir", "Rockburn"], ["Nevis Bluff The Holdsworth Pinot Noir", "Nevis Bluff"], ["Belle Glos Clark and Telephone Vineyard Pinot Noir", "Belle Glos"],
       ["Alexana Estate Vineyard Pinot Noir", "Alexana"], ["Leyda Origin Pinot Noir", "Leyda"], ["Dalrymple Vineyards Single Site Pinot Noir", "Dalrymple Vineyards"]]})

kinds.append({"n": "Merlot", "a": "", "d": "Still red wine made mainly from the Merlot grape.", "s": OLD,
 "x": [
  X("Pomerol", "Small Bordeaux right-bank appellation of about 800 ha, Merlot-dominant with Cabernet Franc; it has no official classification.", WP+"Pomerol",
    dt="château · vintage · Lalande-de-Pomerol as lighter neighbour"),
  X("Pétrus", "Pomerol estate regarded as the appellation's finest producer.", WD+"Q1090667", mk="Château Pétrus"),
  X("Le Pin", "Small Pomerol estate whose wine is priced alongside first growths.", WD+"Q305074", mk="Château Le Pin"),
  X("Masseto", "Bolgheri red from the Ornellaia estate; first vintage 1985.", WP+"Masseto", mk="Tenuta dell'Ornellaia", y="1985"),
 ],
 "m": [["Steenberg Merlot", "Steenberg"]]})

kinds.append({"n": "Syrah", "a": "Shiraz", "d": "Still red wine made mainly from the Syrah grape, under either name.", "s": OLD,
 "x": [
  X("Hermitage", "Northern Rhône hill appellation (1937) for Syrah, with up to 15% Marsanne or Roussanne allowed.", WP+"Hermitage_AOC", y="1937",
    v=[("Domaine Jean-Louis Chave Hermitage", "Domaine Jean-Louis Chave", "", "family estate traced to 1481"), ("Chapoutier Hermitage", "Chapoutier", "", ""),
       ("Paul Jaboulet Aîné Hermitage", "Paul Jaboulet Aîné", "", ""), ("Delas Hermitage", "Maison Delas Frères", "", "")],
    dt="lieu-dit (Les Bessards, L'Hermite, Le Méal, Les Greffieux, La Chapelle) · vintage"),
  X("Côte-Rôtie", "Northern Rhône appellation (1940) for Syrah co-fermented with up to 20% Viognier, split into Côte Brune and Côte Blonde.", WP+"C%C3%B4te-R%C3%B4tie_AOC", y="1940",
    v=[("Guigal La Mouline", "E. Guigal", "", "single-vineyard bottling"), ("Guigal La Landonne", "E. Guigal", "", "single-vineyard bottling"),
       ("Maison Delas Frères La Landonne Côte Rôtie", "Maison Delas Frères", "", "")], dt="Côte Brune vs Côte Blonde · Viognier share · vintage"),
  X("Penfolds Grange", "Australia's icon Shiraz, created by Max Schubert; sold as Grange Hermitage until the 1990 vintage.", WP+"Penfolds_Grange", mk="Penfolds", y="1951", a="Grange Hermitage",
    v=[("Grange 1951", "Penfolds", "1951", "experimental first vintage"), ("Grange 1952", "Penfolds", "1952", "first commercial release"),
       ("Grange 1990", "Penfolds", "1990", "first labelled without 'Hermitage'; Wine Spectator Wine of the Year 1995")], dt="vintage · Shiraz with a little Cabernet Sauvignon"),
  X("Barossa Valley Shiraz", "Shiraz from the Barossa Valley wine region of South Australia.", WD+"Q4863063",
    v=[("Barossa Old Vine Company Shiraz", "Barossa Old Vine Company", "", "")]),
 ],
 "m": [["Château Tanunda 100 Year Old Vines Shiraz", "Château Tanunda"], ["Shaw and Smith Shiraz", "Shaw and Smith"], ["Katnook Estate Prodigy Shiraz", "Katnook Estate"],
       ["Dandelion Vineyards Lioness of McLaren Vale Shiraz", "Dandelion Vineyards"], ["Hare's Chase Vigilance Marananga Shiraz", "Hare's Chase"],
       ["Mission Estate Reserve Syrah", "Mission Estate"], ["Babylonstoren Shiraz", "Babylonstoren"], ["Trentham Estate Reserve Shiraz", "Trentham Estate"]]})

kinds.append({"n": "Grenache", "a": "Garnacha · Cannonau", "d": "Still red wine made mainly from the Grenache grape, under either name.", "s": OLD,
 "x": [
  X("Châteauneuf-du-Pape", "Southern Rhône appellation (1936) where Grenache fills about 72% of vines among up to 18 permitted varieties.", WP+"Ch%C3%A2teauneuf-du-Pape_AOC", y="1936",
    v=[("Château Rayas", "Château Rayas", "", ""), ("Château de Beaucastel", "Château de Beaucastel", "", ""), ("Domaine du Vieux Télégraphe", "Domaine du Vieux Télégraphe", "", "")],
    dt="estate · blend share · vintage"),
  X("Priorat", "Catalan DOQ of Garnacha and Cariñena on black slate llicorella soil; DO since 1954.", WP+"Priorat_(DOQ)",
    v=[("Álvaro Palacios L'Ermita", "Álvaro Palacios", "1993", "old-vine wine that revived interest in the region"), ("Clos Mogador", "René Barbier", "", "")],
    dt="village · old vines · Garnacha/Cariñena share"),
 ]})

kinds.append({"n": "Tempranillo", "a": "Tinto Fino · Tinta de Toro · Aragonez · Tinta Roriz", "d": "Still red wine made mainly from the Tempranillo grape.", "s": OLD,
 "t": ["Joven", "Crianza", "Reserva", "Gran Reserva"],
 "x": [
  X("Rioja", "Spain's first DOCa (1991): Tempranillo with Garnacha, Graciano and Mazuelo, graded Crianza, Reserva and Gran Reserva by ageing.", WP+"Rioja_(wine)", y="1991",
    v=[("Marqués de Murrieta Gran Reserva 1942", "Marqués de Murrieta", "1942", "released in 1983")],
    dt="subzone (Rioja Alta, Rioja Alavesa, Rioja Oriental) · ageing grade · vintage"),
  X("Ribera del Duero", "Castilian DO (1982) for Tinto Fino (Tempranillo) reds.", WP+"Ribera_del_Duero_(DO)", y="1982",
    v=[("Dominio de Pingus", "Dominio de Pingus", "", ""), ("Tinto Pesquera", "Alejandro Fernández", "", "")]),
  X("Vega Sicilia", "Ribera del Duero estate founded 1864, owned by the Álvarez family since 1982.", WP+"Vega_Sicilia", mk="Vega Sicilia", y="1864",
    v=[("Único", "Vega Sicilia", "", "Gran Reserva of about 80% Tempranillo, released about 10 years after vintage"),
       ("Valbuena 5°", "Vega Sicilia", "", "aged five years before release"),
       ("Único Reserva Especial", "Vega Sicilia", "", "non-vintage blend of Único vintages")]),
  X("Toro", "Denominación de origen in Castile and León for reds of Tinta de Toro.", WD+"Q765567",
    v=[("Bodegas Vatan Tinta de Toro", "Bodegas Vatan", "", "")]),
 ]})

kinds.append({"n": "Sangiovese", "a": "Brunello · Prugnolo Gentile · Morellino", "d": "Still red wine made mainly from the Sangiovese grape.", "s": OLD,
 "x": [
  X("Brunello di Montalcino", "100% Sangiovese from Montalcino, Italy's first DOCG (1980); first modern version released by Ferruccio Biondi-Santi in 1888.", WP+"Brunello_di_Montalcino", mk="", y="1888",
    v=[("Rosso di Montalcino", "", "1984", "younger DOC from the same area"),
       ("Padelletti Brunello di Montalcino Riserva", "Padelletti", "", ""), ("Poggio Il Castellare Brunello di Montalcino", "Poggio Il Castellare", "", ""),
       ("Bottega Il Vino dei Poeti Brunello di Montalcino", "Bottega", "", "")], dt="normale vs Riserva · vintage"),
  X("Chianti Classico", "Sangiovese-led red from the historic Chianti heartland, marked by the black rooster seal; tiers Riserva and Gran Selezione (2014).", WP+"Chianti_Classico", a="Gallo Nero",
    v=[("Castello di Cacchiano Millennio Gaiole Chianti Classico Gran Selezione", "Castello di Cacchiano", "", "")],
    dt="commune (Castellina, Gaiole, Greve, Radda…) · annata/Riserva/Gran Selezione"),
  X("Chianti", "Wider Tuscan Sangiovese appellation with sub-zones such as Rufina; Superiore since 1996.", WP+"Chianti_Classico",
    v=[("Castello del Trebbio Vigneto Lastricato Terraelectae Chianti Rùfina Riserva", "Castello del Trebbio", "", "")]),
  X("Vino Nobile di Montepulciano", "DOCG (1980) of at least 70% Sangiovese (Prugnolo gentile) from Montepulciano, aged two years.", WP+"Vino_Nobile_di_Montepulciano", y="1980",
    v=[("Canneto Vino Nobile di Montepulciano", "Canneto", "", "")]),
 ]})

kinds.append({"n": "Nebbiolo", "a": "Spanna · Chiavennasca", "d": "Still red wine made mainly from the Nebbiolo grape.", "s": OLD,
 "x": [
  X("Barolo", "100% Nebbiolo from the Langhe around Barolo, DOCG 1980, aged at least 38 months (Riserva 62).", WP+"Barolo", y="1980",
    v=[("Aldo Conterno Barolo Bussia Romirasco", "Poderi Aldo Conterno", "", "Bussia cru"), ("Gaja Barolo Sperss", "Angelo Gaja", "", ""),
       ("Gaja Barolo Conteisa", "Angelo Gaja", "", ""), ("Ceretto Barolo Bricco Rocche", "Ceretto", "", ""), ("Ceretto Barolo Bussia", "Ceretto", "", "Bussia cru"),
       ("Ceretto Barolo Rocche di Castiglione", "Ceretto", "", ""), ("Fratelli Serio & Battista Borgogno Cannubi Barolo Riserva", "Fratelli Serio & Battista Borgogno", "", "Cannubi cru"),
       ("G.D. Vajra Barolo Ravera", "G.D. Vajra", "", ""), ("Chiara Boschis Barolo Via Nuova", "Chiara Boschis", "", ""),
       ("Giovanni Rosso Barolo Serra", "Giovanni Rosso", "", ""), ("Fontanafredda Barolo La Rosa", "Fontanafredda", "", ""), ("Prunotto Barolo", "Prunotto", "", "")],
    dt="commune (Barolo, La Morra, Castiglione Falletto, Serralunga, Monforte) · MGA cru (Cannubi, Brunate, Bussia, Monprivato…) · normale/Riserva"),
  X("Barbaresco", "Nebbiolo from Barbaresco, Neive and Treiso; DOCG 1980, aged at least 2 years (Riserva 4).", WP+"Barbaresco", y="1980",
    v=[("Produttori del Barbaresco", "Produttori del Barbaresco", "", "cooperative"), ("Gaja Barbaresco", "Angelo Gaja", "", ""),
       ("Vinory Serragrilli Barbaresco Riserva", "Vinory", "", "")], dt="commune · cru · normale/Riserva"),
 ]})

kinds.append({"n": "Malbec", "a": "Côt · Auxerrois", "d": "Still red wine made mainly from the Malbec grape.", "s": OLD,
 "x": [
  X("Mendoza Malbec", "Malbec from Argentina's Mendoza, grown at 600–1,100 m in Luján de Cuyo, Maipú and the Uco Valley.", WP+"Mendoza_wine",
    v=[("Catena Zapata Malbec", "Bodega Catena Zapata", "", "")], dt="subregion (Luján de Cuyo, Uco Valley, Maipú) · altitude · vintage"),
  X("Cahors", "South-west French AOC (1971), at least 70% Malbec, historically the 'black wine'.", WP+"Cahors_AOC", y="1971"),
 ],
 "m": [["Luigi Bosca De Sangre Malbec", "Luigi Bosca"], ["El Enemigo As Bravas Malbec", "El Enemigo"], ["Alta-Yarí Gran Malbec", "Alta-Yarí"],
       ["La Luz Gran Callejón Del Crimen Ánfora Malbec", "La Luz"]]})
# Catena Zapata Malbec as a named bottling is not on the page -> drop version
kinds[-1]["x"][0].pop("v")

kinds.append({"n": "Zinfandel", "a": "Primitivo · Crljenak Kaštelanski", "d": "Still red wine made mainly from the Zinfandel grape, under either name.", "s": OLD,
 "x": [
  X("Lodi Zinfandel", "Old-vine Zinfandel from California's Lodi AVA (1986), with seven sub-AVAs since 2006.", WP+"Lodi_AVA", y="1986", dt="sub-AVA (Mokelumne River, Clements Hills…) · old vines"),
  X("Primitivo di Manduria", "Primitivo from Manduria in Apulia, southern Italy.", WP+"Primitivo_di_Manduria"),
 ]})

kinds.append({"n": "Cabernet Franc", "a": "Breton · Bouchet", "d": "Still red wine made mainly from the Cabernet Franc grape.", "s": "https://www.wine-republic.co.uk/collections/cabernet-franc",
 "x": [
  X("Chinon", "Touraine appellation on the Vienne for Cabernet Franc reds, with up to 25% Cabernet Sauvignon.", WP+"Chinon_AOC"),
  X("Saumur-Champigny", "Loire appellation for Cabernet Franc reds near Saumur.", WP+"Saumur-Champigny"),
  X("Bourgueil", "Touraine appellation for Cabernet Franc reds.", WD+"Q2922370"),
  X("Château Cheval Blanc", "Saint-Émilion Premier Grand Cru Classé (A) of about 57% Cabernet Franc and 40% Merlot.", WP+"Ch%C3%A2teau_Cheval_Blanc", mk="Château Cheval Blanc", y="1955",
    v=[("Cheval Blanc 1947", "Château Cheval Blanc", "1947", "vintage cited in Ratatouille and Bottle Shock")]),
 ],
 "m": [["Gran Enemigo Single Vineyard Cabernet Franc Gualtallary", "Gran Enemigo"], ["Gran Enemigo Single Vineyard Cabernet Franc El Cepillo", "Gran Enemigo"],
       ["Gran Enemigo Single Vineyard Cabernet Franc Los Chacayes", "Gran Enemigo"], ["Backsberg Patriarch Cabernet Franc", "Backsberg"],
       ["Echolands Blue Mountain Vineyard Cabernet Franc", "Echolands"]]})

kinds.append({"n": "Gamay", "a": "Gamay noir à jus blanc · Beaujolais", "d": "Light, fruity red wine made from the Gamay grape, above all Beaujolais.", "s": WP+"Beaujolais",
 "x": [
  X("Beaujolais cru", "Wine from one of the ten named Beaujolais crus, fuller and longer-lived than basic Beaujolais.", WP+"Beaujolais",
    v=[("Moulin-à-Vent", "", "", "parts of Chénas and Romanèche-Thorins; among the fullest"), ("Morgon", "", "", "full-bodied, ageworthy"),
       ("Fleurie", "", "", ""), ("Juliénas", "", "", ""), ("Chénas", "", "", ""), ("Saint-Amour", "", "", ""),
       ("Brouilly", "", "", "lighter style"), ("Côte de Brouilly", "", "", "lighter style"), ("Chiroubles", "", "", "lighter style"), ("Régnié", "", "", "lighter style")],
    dt="cru · producer · vintage"),
  X("Beaujolais-Villages", "Intermediate appellation from 39 communes in Haut Beaujolais, for drinking within two years.", WP+"Beaujolais"),
  X("Beaujolais nouveau", "Very young Beaujolais, often by carbonic maceration, released on the third Thursday of November.", WP+"Beaujolais"),
 ]})

brands = [
 {"n": "Domaine de la Romanée-Conti", "c": "France", "f": "1869", "seg": "Burgundy grand-cru domaine", "d": "Vosne-Romanée estate owning the Romanée-Conti and La Tâche monopoles.",
  "lines": ["Romanée-Conti", "La Tâche", "Richebourg", "Romanée-Saint-Vivant", "Grands Échezeaux", "Échezeaux"], "sig": ["Romanée-Conti", "La Tâche"], "s": WP+"Domaine_de_la_Roman%C3%A9e-Conti"},
 {"n": "Penfolds", "c": "Australia", "seg": "Australian wine house", "d": "South Australian winery known for Grange and its Bin series.", "lines": ["Grange", "Bin 407"], "eras": ["Max Schubert, creator of Grange, 1951"], "sig": ["Penfolds Grange"], "s": WP+"Penfolds_Grange"},
 {"n": "Vega Sicilia", "c": "Spain", "f": "1864", "seg": "Ribera del Duero estate", "d": "Spain's most famous red-wine estate, owned by the Álvarez family since 1982.", "lines": ["Único", "Valbuena 5°", "Único Reserva Especial"], "sig": ["Vega Sicilia"], "s": WP+"Vega_Sicilia"},
 {"n": "Screaming Eagle", "c": "United States", "f": "1986", "seg": "Napa cult winery", "d": "Oakville estate founded by Jean Phillips, first vintage 1992.", "sig": ["Screaming Eagle"], "s": WP+"Screaming_Eagle_Winery_and_Vineyards"},
 {"n": "Opus One", "c": "United States", "seg": "Napa winery", "d": "Napa Valley winery and its eponymous red wine.", "sig": ["Opus One"], "s": WD+"Q448588"},
 {"n": "Tenuta San Guido", "c": "Italy", "seg": "Bolgheri estate", "d": "Tuscan estate of the Incisa della Rocchetta family that makes Sassicaia.", "sig": ["Sassicaia"], "s": WP+"Sassicaia"},
 {"n": "Tenuta dell'Ornellaia", "c": "Italy", "seg": "Bolgheri estate", "d": "Bolgheri estate founded by Lodovico Antinori, owned by the Frescobaldi family since 2005, maker of Masseto.", "sig": ["Masseto"], "s": WP+"Masseto"},
 {"n": "Château Pétrus", "c": "France", "seg": "Pomerol estate", "d": "Pomerol estate regarded as the appellation's finest producer.", "sig": ["Pétrus"], "s": WD+"Q1090667"},
 {"n": "Château Le Pin", "c": "France", "seg": "Pomerol estate", "d": "Small Pomerol estate.", "sig": ["Le Pin"], "s": WD+"Q305074"},
 {"n": "Château Cheval Blanc", "c": "France", "seg": "Saint-Émilion first growth", "d": "Saint-Émilion Premier Grand Cru Classé (A), owned by LVMH and the Frère family.", "sig": ["Château Cheval Blanc"], "s": WP+"Ch%C3%A2teau_Cheval_Blanc"},
]
notes = ("All 11 planned old kinds kept, Gamay added (Beaujolais crus as versions). Burgundy grand-cru names from old models became Pinot Noir archetypes (Wikidata/Wikipedia sourced); "
         "Corton kept in m (no retrieved source). Old retail-shop SKUs (wine.com skew) trimmed: kept as archetype versions where the source confirms the appellation, "
         "otherwise ≤11 per kind in m; dropped minor labels (Calculated Risk, Deep Woods, House of Cards, Knorhoek, Nocturne, Oakridge, Shangri-La, Suckfizzle duplicate, "
         "Brashley, Clos Ostler, Dawson James, Grand Napa Vineyards, Nga Waka, Purple Hands, Southern Light, Unsworth, Wayfarer, Beresford, Black Pig, Chateau La Borie, "
         "E.J. McDougall, Ferngrove, Greystone, Kimsey, Monteperle, Passage Rock, Diego Morra, Dosio, minor Barolo duplicates, M&S own-label Barolo). "
         "Bordeaux left-bank and red blends belong to the Red blends shelf. Not added (no time/source): Sonoma Zinfandel, Barossa details, Gaja Barbaresco crus, Mendoza named bottlings, Corton.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/00_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('kinds', len(kinds), 'archetypes', sum(len(k.get('x', [])) for k in kinds), 'brands', len(brands))
