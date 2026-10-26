import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, s, y='', a='', mk='', v=(), dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": W + s,
            "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
WC = 'https://www.wine.com/list/wine/white-wine/7155-125'
kinds = []

kinds.append({"n": "Chardonnay", "a": "", "d": "Still white wine made mainly from the Chardonnay grape.", "s": WC,
 "t": ["unoaked", "barrel-fermented"],
 "x": [
  X("Chablis", "Dry, mineral, high-acid Chardonnay from around Chablis in northern Burgundy.", "Chablis_wine", "1938",
    v=[("Chablis Grand Cru", "", "", "seven climats on one hill: Bougros, Les Preuses, Vaudésir, Grenouilles, Valmur, Les Clos, Blanchot"),
       ("Chablis Premier Cru", "", "", "about 40 climats"),
       ("Petit Chablis", "", "1944", "lowest level, outlying land"),
       ("La Chablisienne", "La Chablisienne", "", "co-operative making nearly a third of all Chablis"),
       ("Domaine Pinson Frères Mont de Milieu Chablis 1er Cru", "Domaine Pinson Frères", "", ""),
       ("Jean-Marc Brocard Vau de Vey Chablis 1er Cru", "Jean-Marc Brocard", "", "")],
    dt="Petit Chablis → Chablis → Premier Cru → Grand Cru · climat · vintage"),
  X("Montrachet", "Grand cru white Burgundy from the Montrachet vineyard and its neighbours in Puligny- and Chassagne-Montrachet.", "Montrachet", "1937",
    v=[("Montrachet", "", "1937", "about 8 ha split between Puligny- and Chassagne-Montrachet"),
       ("Chevalier-Montrachet", "", "", "grand cru above Montrachet, in Puligny"),
       ("Bâtard-Montrachet", "", "", "grand cru below Montrachet"),
       ("Bienvenues-Bâtard-Montrachet", "", "", "grand cru, in Puligny"),
       ("Criots-Bâtard-Montrachet", "", "", "grand cru, in Chassagne"),
       ("Domaine de la Romanée-Conti Montrachet", "Domaine de la Romanée-Conti", "", "0.67 ha, about 3,000 bottles a year"),
       ("Montrachet (de Laguiche parcel)", "Joseph Drouhin", "", "largest holding, leased to Drouhin"),
       ("Ramonet-Prudhon Bâtard-Montrachet 1973", "Ramonet-Prudhon", "1973", "in the 1976 Judgment of Paris"),
       ("Domaine Louis Lequin et Fils Bâtard-Montrachet", "Domaine Louis Lequin et Fils", "", "")],
    dt="grand cru vineyard · producer · vintage"),
  X("Corton-Charlemagne", "Grand cru white Burgundy from the Corton hill in the Côte de Beaune.", "Corton-Charlemagne", "1937",
    v=[("Charlemagne", "", "1937", "separate tiny grand cru, usually sold as Corton-Charlemagne"),
       ("Bonneau du Martray Corton-Charlemagne", "Bonneau du Martray", "", "largest single owner, 9.5 ha"),
       ("Louis Latour Corton-Charlemagne", "Louis Latour", "", ""),
       ("Hospices de Beaune Corton-Charlemagne", "Hospices de Beaune", "", ""),
       ("Domaine Comte Senard Corton-Charlemagne", "Domaine Comte Senard", "", ""),
       ("Albert Bichot Corton-Charlemagne Grand Cru Domaine du Pavillon", "Albert Bichot", "", "")],
    dt="communes Aloxe-Corton, Pernand-Vergelesses, Ladoix-Serrigny · producer · vintage"),
  X("Meursault", "White Burgundy from the commune of Meursault in the Côte de Beaune, typically rich in style.", "Meursault_wine",
    v=[("Roulot Meursault Charmes 1973", "Roulot", "1973", "in the 1976 Judgment of Paris")],
    dt="village or premier cru (Perrières, Genevrières, Charmes, Gouttes d'Or …) · producer · vintage"),
  X("Pouilly-Fuissé", "Chardonnay from four communes in the Mâconnais, southern Burgundy.", "Pouilly-Fuiss%C3%A9", "1936",
    v=[("Louis Latour Pouilly-Fuissé", "Louis Latour", "", "")],
    dt="village or premier cru (22 climats since 2020) · producer"),
  X("California Chardonnay", "Ripe, often oaked Chardonnay from California, put on the map by the 1976 Judgment of Paris.", "Judgment_of_Paris_(wine)", "1970s",
    v=[("Chateau Montelena Chardonnay 1973", "Chateau Montelena", "1973", "top white at the 1976 Judgment of Paris"),
       ("Chalone Vineyard Chardonnay 1974", "Chalone Vineyard", "1974", "third at the Judgment of Paris"),
       ("Kendall-Jackson Vintner's Reserve Chardonnay", "Kendall-Jackson", "", ""),
       ("Far Niente Chardonnay", "Far Niente", "", ""),
       ("Chalk Hill Sonoma Coast Chardonnay", "Chalk Hill", "", "")],
    dt="Napa, Sonoma, Central Coast · oak and malolactic level · vintage")],
 "m": [["Tyrrell's Vat 47 Chardonnay", "Tyrrell's"], ["Brokenwood Indigo Vineyard Chardonnay", "Brokenwood"],
       ["Xanadu Wines Reserve Chardonnay", "Xanadu"], ["Tolpuddle Chardonnay", "Tolpuddle"],
       ["Church Road 1 Chardonnay", "Church Road"], ["Girlan Curlan Chardonnay Riserva", "Girlan"],
       ["Wirra Wirra The 12th Man Chardonnay", "Wirra Wirra"], ["Sidewood Owen's Chardonnay", "Sidewood"],
       ["Soumah Hexham Vineyard Chardonnay", "Soumah"], ["Greystone Wines Erin's Chardonnay", "Greystone Wines"],
       ["Lothian of Elgin Chardonnay", "Lothian of Elgin"], ["Tidebrook Staddle Stone Chardonnay", "Tidebrook"],
       ["1276 Wines Chardonnay", "1276 Wines"], ["Deurić La Rem Chardonnay", "Deurić"]]})

kinds.append({"n": "Sauvignon Blanc", "a": "", "d": "Still white wine made mainly from the Sauvignon Blanc grape.", "s": WC,
 "x": [
  X("Sancerre", "Crisp Sauvignon Blanc from the Sancerre hills in the eastern Loire.", "Sancerre_(wine)", "1936",
    v=[("Jean-Max Roger Sancerre Cuvée GC", "Jean-Max Roger", "", "from Le Grand Chemarin"),
       ("Chateau de Sancerre Cuvée du Connétable Sancerre", "Chateau de Sancerre", "", ""),
       ("Henri Bourgeois Sancerre Blanc", "Henri Bourgeois", "", "")],
    dt="soil: chalk, flint, clay-limestone · lieu-dit (Clos de la Poussie, Chêne Marchand, Le Grand Chemarin) · vintage"),
  X("Pouilly-Fumé", "Dry Sauvignon Blanc from around Pouilly-sur-Loire, across the river from Sancerre.", "Pouilly-Fum%C3%A9", "1937",
    dt="producer · vintage"),
  X("Marlborough Sauvignon Blanc", "Pungent, tropical Sauvignon Blanc from New Zealand's largest wine region.", "Marlborough_wine_region", "1973",
    v=[("Montana (now Brancott Estate)", "Brancott Estate", "1973", "first large-scale Marlborough vineyards"),
       ("Cloudy Bay Sauvignon Blanc", "Cloudy Bay", "1985", "brought international attention")],
    dt="Wairau or Awatere valley · producer · vintage"),
  X("White Pessac-Léognan", "Barrel-fermented Sauvignon Blanc–Sémillon blend from the northern Graves of Bordeaux.", "Pessac-L%C3%A9ognan", "1987",
    a="white Graves",
    v=[("Château Carbonnieux blanc", "Château Carbonnieux", "", "")],
    dt="Sauvignon/Sémillon share · classed growth · vintage")],
 "m": [["Kim Crawford Sauvignon Blanc", "Kim Crawford"], ["Villa Maria Private Bin Sauvignon Blanc", "Villa Maria"],
       ["Clos Henri Otira Sauvignon Blanc", "Clos Henri"], ["Rapaura Springs Rohe Sauvignon Blanc", "Rapaura Springs"],
       ["Craggy Range Te Muna Sauvignon Blanc", "Craggy Range"], ["Merry Edwards Sauvignon Blanc", "Merry Edwards"],
       ["Clos du Val Estate Sauvignon Blanc", "Clos du Val"], ["Terlano Quarz Sauvignon", "Terlano"],
       ["Skoff Original Walter Skoff Royal Sauvignon Blanc", "Skoff Original"],
       ["Weingut Johann Schneeberger Kittenberg Sauvignon Blanc", "Weingut Johann Schneeberger"],
       ["Chateau de Sours Montesours", "Chateau de Sours"]]})

kinds.append({"n": "Riesling", "a": "", "d": "Still white wine made mainly from the Riesling grape.", "s": WC,
 "t": ["trocken (dry)", "off-dry", "sweet"],
 "x": [
  X("Mosel Riesling", "Light, racy Riesling from the steep slate slopes of the Mosel, Saar and Ruwer.", "Mosel_(wine_region)",
    v=[("Wehlener Sonnenuhr", "", "", "vineyard"), ("Bernkastel Doctorberg", "", "", "vineyard"),
       ("Maximin Grünhaus", "Maximin Grünhaus", "", "Ruwer estate"), ("Bremm Calmont", "", "", "steepest recorded vineyard")],
    dt="Prädikat: Kabinett, Spätlese, Auslese, Beerenauslese, Trockenbeerenauslese, Eiswein · Mosel, Saar or Ruwer · vineyard"),
  X("Rheingau Riesling", "Firm, often dry Riesling from the south-facing Rhine bank in Hesse.", "Rheingau_(wine_region)",
    v=[("Schloss Johannisberg", "Schloss Johannisberg", "", "early Riesling estate; noble rot discovered here"),
       ("Kloster Eberbach", "Kloster Eberbach", "1135", "Cistercian abbey, now Hessian state winery"),
       ("Schloss Vollrads", "Schloss Vollrads", "", "estate in Winkel")],
    dt="Prädikat or dry · estate · vineyard"),
  X("Alsace Riesling", "Dry, full Riesling from Alsace, sold by grape name in the tall flûte bottle.", "Alsace_wine",
    v=[("Trimbach Riesling", "Trimbach", "", ""), ("Zind-Humbrecht Riesling", "Domaine Zind-Humbrecht", "", ""),
       ("Hugel Riesling", "Hugel", "", ""), ("Weinbach Riesling", "Domaine Weinbach", "", "")],
    dt="Alsace or Grand Cru · Vendange Tardive, Sélection de Grains Nobles (since 1983) · producer"),
  X("Alsace Grand Cru", "Wines of the 51 classified Alsace vineyards, mostly Riesling, Gewurztraminer, Pinot Gris or Muscat.", "Alsace_Grand_Cru_AOC", "1975",
    v=[("Schlossberg", "", "1975", "Kientzheim; first grand cru"), ("Rangen", "", "1983", "Thann"),
       ("Brand", "", "1983", "Turckheim"), ("Hengst", "", "1983", "Wintzenheim"),
       ("Schoenenbourg", "", "1992", "Riquewihr"), ("Kaefferkopf", "", "", "Ammerschwihr; latest grand cru, blends allowed")],
    dt="grand cru · grape · producer · vintage"),
  X("Clare Valley Riesling", "Dry, lime-scented Riesling from South Australia's Clare Valley.", "Clare_Valley", "1840s",
    v=[("Grosset Riesling", "Grosset Wines", "", ""), ("Jim Barry Riesling", "Jim Barry Wines", "", ""),
       ("Taylors Riesling", "Taylors Wines", "", ""), ("Kilikanoon Riesling", "Kilikanoon", "", "")],
    dt="producer · vineyard · vintage"),
  X("Wachau Riesling", "Dry Riesling from the Danube terraces of the Wachau, graded by the Vinea Wachau ladder.", "Wachau", "1983",
    dt="Steinfeder → Federspiel → Smaragd · village (Dürnstein, Loiben) · producer")],
 "m": [["Birgit Eichinger Ried Heiligenstein 1ötw Riesling", "Birgit Eichinger"],
       ["Peter Lehmann Masters Wigan Riesling", "Peter Lehmann"], ["Vinarstvi Volarik Ryzlink Rýnský", "Vinarstvi Volarik"]]})

kinds.append({"n": "Pinot Grigio", "a": "Pinot Gris · Grauburgunder", "d": "Still white wine made mainly from the Pinot Gris grape, under either name.", "s": WC,
 "x": [
  X("Italian Pinot Grigio", "Light, crisp, early-picked Pinot Grigio from northern Italy.", "Pinot_gris", "1961",
    v=[("Santa Margherita Pinot Grigio", "Santa Margherita", "1961", "first to vinify Pinot Grigio as a white wine")],
    dt="Friuli, Alto Adige, Trentino, Oltrepò Pavese · producer"),
  X("Alsace Pinot Gris", "Full, spicy Pinot Gris from Alsace, formerly labelled Tokay d'Alsace.", "Pinot_gris",
    dt="Alsace or Grand Cru · Vendange Tardive, SGN · producer"),
  X("Oregon Pinot Gris", "Medium-bodied, pear-scented Pinot Gris from Oregon.", "Pinot_gris", "1965",
    v=[("Eyrie Vineyards Pinot Gris", "Eyrie Vineyards", "1965", "first American Pinot Gris vines, planted by David Lett"),
       ("King Estate Pinot Gris", "King Estate", "1991", "")],
    dt="producer · vintage"),
  X("Grauburgunder", "Fuller German Pinot Gris, chiefly from Baden, Rheinhessen and the Pfalz.", "Pinot_gris",
    dt="region · dry or off-dry · producer")]})

kinds.append({"n": "Chenin Blanc", "a": "Steen", "d": "Still white wine made mainly from the Chenin Blanc grape.", "s": WC,
 "x": [
  X("Vouvray", "Chenin Blanc from Vouvray in Touraine, made from bone dry to sweet and sparkling.", "Vouvray_AOC", "1936",
    v=[("Huet Vouvray", "Huet", "1947", "1947 ranked sixth in Decanter's 100 Greatest Wines (2005)"),
       ("François Pinon Vouvray", "François Pinon", "", "")],
    dt="sec, demi-sec, moelleux, doux · pétillant or mousseux · vintage"),
  X("Savennières", "Mostly dry, long-lived Chenin Blanc from the north bank of the Loire in Anjou.", "Savenni%C3%A8res_AOC", "1952",
    v=[("Savennières-Coulée-de-Serrant", "Nicolas Joly", "", "about 7 ha single estate"),
       ("Savennières-Roche-aux-Moines", "", "", "about 33 ha"),
       ("Closel", "Closel", "", ""), ("Baumard Savennières", "Baumard", "", ""),
       ("Thibaud Boudignon Savennières", "Thibaud Boudignon", "", "")],
    dt="sub-appellation · producer · vintage"),
  X("South African Chenin Blanc", "Riper, tropical Chenin Blanc, South Africa's most planted grape, long called Steen.", "Chenin_blanc",
    v=[("Nederburg Heritage Heroes The Anchor Man Old Vine Chenin Blanc", "Nederburg", "", "")],
    dt="Swartland, Paarl, Olifants River · old vines · oaked or unoaked")],
 "m": [["Domaine de Huillé Éternel Chenin Blanc", "Domaine de Huillé"],
       ["Domaine de la Clartière Terres de Paillé", "Domaine de la Clartière"]]})

kinds.append({"n": "Sémillon", "a": "Semillon", "d": "Still dry white wine made mainly from the Sémillon grape; sweet Sauternes is listed under sweet wine.", "s": "https://lifford.com/products/hunter-valley-semillon",
 "x": [
  X("Hunter Valley Semillon", "Unoaked, austere Semillon from New South Wales that turns rich and biscuity after ten years in bottle.", "Hunter_Valley_wine", "1830",
    v=[("Leo Buring Rhine Gold", "Leo Buring", "1960s", "first commercially successful Hunter Semillon"),
       ("Tyrrell's Semillon", "Tyrrell's", "", ""), ("Lindeman's Semillon", "Lindeman's", "", "")],
    dt="young or aged release · producer · vintage")]})

kinds.append({"n": "Gewürztraminer", "a": "Gewurztraminer · Traminer", "d": "Still white wine made mainly from the aromatic, lychee-scented Gewürztraminer grape.", "s": WC,
 "x": [
  X("Alsace Gewurztraminer", "Alsace's signature aromatic white, from dry to Vendange Tardive and SGN.", "Gew%C3%BCrztraminer",
    v=[("Domaine Kirrenbourg Gewurztraminer Grand Cru Schlossberg", "Domaine Kirrenbourg", "", "")],
    dt="Alsace or Grand Cru · dry to sweet · producer"),
  X("Alto Adige Gewürztraminer", "Gewürztraminer from South Tyrol, where Tramin (Termeno) gave the grape its name.", "Gew%C3%BCrztraminer",
    dt="producer · vintage")]})

kinds.append({"n": "Grüner Veltliner", "a": "Gruner Veltliner", "d": "Still white wine made mainly from Austria's peppery Grüner Veltliner grape.", "s": "https://www.rohlik.cz/en-CZ/1405968-ar-gruener-veltliner-austria-niederoesterreich",
 "x": [
  X("Wachau Grüner Veltliner", "Dry Grüner Veltliner from the Danube terraces of the Wachau.", "Wachau", "1983",
    dt="Steinfeder → Federspiel → Smaragd · village · producer"),
  X("Kamptal Grüner Veltliner", "Grüner Veltliner from the Kamp valley around Langenlois.", "Kamptal",
    v=[("Schloss Gobelsburg", "Schloss Gobelsburg", "", "")], dt="vineyard · producer"),
  X("Weinviertel Grüner Veltliner", "Everyday Grüner Veltliner from Austria's largest wine region.", "Weinviertel",
    dt="producer · vintage")],
 "m": [["Gritsch Ried Singerriedel Grüner Veltliner", "Gritsch"], ["Weingut Müller Ried Gottschelle Grüner Veltliner", "Weingut Müller"]]})

kinds.append({"n": "Pinot Blanc", "a": "Pinot Bianco · Weissburgunder", "d": "Still white wine made mainly from the Pinot Blanc grape, under either name.", "s": "https://differentdrop.com/products/2022-willm-pinot-blanc",
 "x": [
  X("Alsace Pinot Blanc", "Soft, dry Alsace white, often blended with Auxerrois.", "Pinot_blanc", dt="producer · vintage"),
  X("Alto Adige Pinot Bianco", "Pinot Bianco (Weissburgunder) from South Tyrol, one of its most common whites.", "South_Tyrol_wine",
    dt="cooperative or estate · vineyard"),
  X("Weissburgunder", "German and Austrian Pinot Blanc; the fullest come from Baden and the Pfalz.", "Pinot_blanc",
    v=[("Kranz Ilbesheim Kalmit Weisser Burgunder Grosses Gewächs", "Kranz", "", "")],
    dt="dry or sweet · region · producer")],
 "m": [["Cantina Terlano Vorberg Pinot Bianco", "Cantina Terlano"], ["Amandum Pinot Bianco", "Amandum"]]})

kinds.append({"n": "Albariño", "a": "Alvarinho", "d": "Still white wine made mainly from the Albariño grape, under either name.", "s": "https://www.bodeboca.fr/vino/arruxo-albarino-2023",
 "x": [
  X("Rías Baixas Albariño", "Fresh, saline Albariño from Galicia's Atlantic coast.", "R%C3%ADas_Baixas_DO", "1988",
    v=[("Bodegas Aquitania Albariño", "Bodegas Aquitania", "", "")],
    dt="subzone: Val do Salnés, O Rosal, Condado do Tea, Soutomaior, Ribera de Ulla · producer"),
  X("Vinho Verde Alvarinho", "Riper Alvarinho from Monção e Melgaço in Portugal's Vinho Verde.", "Vinho_Verde", "1984",
    dt="subregion · producer")]})

kinds.append({"n": "Viognier", "a": "", "d": "Still white wine made mainly from the perfumed, full-bodied Viognier grape.", "s": W + "Viognier",
 "x": [
  X("Condrieu", "100% Viognier white from steep northern Rhône slopes near Vienne.", "Condrieu_AOC", "1940",
    v=[("Guigal Condrieu", "Guigal", "", "négociant who widened the market for Condrieu")],
    dt="producer · vintage"),
  X("Château-Grillet", "Tiny Viognier appellation enclosed within Condrieu.", "Condrieu_AOC", dt="vintage")]})

kinds.append({"n": "Muscat", "a": "Moscato · Muskateller · Moscatel", "d": "Dry or off-dry white wine from the floral Muscat grape family; sweet styles are under sweet wine.", "s": W + "Muscat_(grape_and_wine)",
 "t": ["Muscat Blanc à Petits Grains", "Muscat of Alexandria", "Muscat Ottonel"],
 "x": [
  X("Alsace Muscat", "Dry or off-dry Alsace Muscat, mainly from Muscat Ottonel.", "Muscat_(grape_and_wine)", dt="Alsace or Grand Cru · producer"),
  X("Austrian dry Muscat", "Dry, perfumed Muscat Blanc à Petits Grains from the Wachau and Südsteiermark.", "Muscat_(grape_and_wine)", dt="region · producer")]})

K = lambda n, c, f, seg, d: {"n": n, "c": c, "f": f, "seg": seg, "d": d, "s": "knowledge"}
brands = [
 K("Domaine de la Romanée-Conti", "France", "", "Burgundy domaine", "Vosne-Romanée domaine with a small holding in Montrachet."),
 K("Joseph Drouhin", "France", "1880", "Burgundy négociant-grower", "Beaune house making wines across Burgundy and Chablis."),
 K("Louis Latour", "France", "1797", "Burgundy négociant-grower", "Beaune house known for Corton-Charlemagne."),
 K("Cloudy Bay", "New Zealand", "1985", "wine producer", "Marlborough winery whose Sauvignon Blanc made the region famous; owned by LVMH."),
 K("Santa Margherita", "Italy", "1935", "wine producer", "Veneto producer best known for Pinot Grigio."),
 K("Trimbach", "France", "1626", "Alsace producer", "Ribeauvillé family house known for dry Riesling."),
 K("Hugel", "France", "1639", "Alsace producer", "Riquewihr family house."),
 K("Domaine Zind-Humbrecht", "France", "1959", "Alsace producer", "Turckheim domaine with grand cru holdings."),
 K("Chateau Montelena", "United States", "1882", "Napa Valley winery", "Calistoga winery whose 1973 Chardonnay topped the 1976 Judgment of Paris."),
 K("Kim Crawford", "New Zealand", "1996", "wine brand", "Large-volume New Zealand Sauvignon Blanc brand."),
 K("Kendall-Jackson", "United States", "1982", "wine producer", "Californian producer of Vintner's Reserve Chardonnay."),
]
out = {"kinds": kinds, "brands": brands, "traditions": [],
 "notes": ("All 10 planned old kinds kept; Viognier and Muscat added (Wikipedia-sourced). Archetypes are appellations/regional styles "
           "(maker-free, mk empty). Old models moved into archetype versions only where a retrieved page or the model's own name ties them to the archetype; "
           "the rest stay in m. Dropped: retailer own-label 'Villa Maria Tesco Finest Black Birch', and unknown-origin SKUs 'Delta Sauvignon Blanc', "
           "'Grand Napa Vineyards Sauvignon Blanc', 'Emma Marris Chardonnay', 'House of Cards Ace High Chardonnay', 'Sidewood Mappinga Chardonnay' (second Sidewood SKU). "
           "Old unattributed grand cru names (Montrachet family, Corton-Charlemagne, Charlemagne, Chablis Grand Cru) became archetypes/versions. "
           "Not added for lack of a retrieved source: Puligny-/Chassagne-Montrachet village archetypes, Margaret River Chardonnay, Pfalz/Nahe Riesling, "
           "Weinviertel DAC year, producer names for Pouilly-Fumé and Wachau. No traditions (appellations are not craft traditions).")}
p = '/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/01_00.json'
os.makedirs(os.path.dirname(p), exist_ok=True)
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('kinds', len(kinds), 'archetypes', sum(len(k.get('x', [])) for k in kinds), 'brands', len(brands))
