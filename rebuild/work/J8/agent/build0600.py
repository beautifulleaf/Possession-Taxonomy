import json, os
U = {}
for l in open('work/J8/agent/u0600.tsv'):
    t, u = l.rstrip('\n').split('\t'); U[t] = u
def u(t): return U[t]
GG = "https://www.staradvertiser.com/?p=805144"
def X(n, d, s, mk="", y="", a="", v=None, dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}
def V(n, mk="", y="", d=""): return {"n": n, "mk": mk, "y": y, "d": d}
K = []
K.append({"n": "Ice cream tub", "a": "ice cream pint · carton · take-home ice cream · scoop ice cream",
 "d": "Take-home container of scoopable ice cream bought for the freezer, from pint to multi-litre.",
 "t": ["pint (473 ml / 500 ml)", "litre and 2-litre tub", "mini tub", "super-premium (dense, low air)", "light / low-calorie", "frozen dairy dessert (reduced butterfat)", "dairy ice cream vs ice cream (non-milk fat)"],
 "s": u("Ice cream"),
 "x": [
  X("Vanilla ice cream", "Plain ice cream flavoured with vanilla bean, extract or vanillin; the default flavour.", u("Vanilla ice cream"), y="18th century (France)", a="vanilla", dt="vanilla source (bean, extract, vanillin) · French-style egg custard or Philadelphia style"),
  X("Chocolate ice cream", "Ice cream flavoured with cocoa or chocolate; one of the oldest and most popular flavours.", u("Chocolate ice cream"), dt="cocoa intensity · inclusions"),
  X("Strawberry ice cream", "Ice cream made with strawberries or strawberry flavouring, usually pink.", u("Strawberry ice cream"), v=[V("Strawberry ripple", d="vanilla with a strawberry jam or syrup ribbon"), V("Strawberry cheesecake", d="variation")], dt="fresh fruit vs flavouring · ripple"),
  X("Neapolitan ice cream", "Three flavours, typically vanilla, chocolate and strawberry, side by side in one block.", u("Neapolitan ice cream"), y="1839 (first recorded, Prussia)", a="Harlequin ice cream · Fürst-Pückler-Eis", v=[V("Fürst-Pückler-Eis", y="1839", d="German three-flavour version credited to the cook of Prince Pückler-Muskau")], dt="brick or tub · flavour order"),
  X("Mint chocolate chip", "Mint ice cream, often coloured green, with small chocolate chips.", u("Mint chocolate chip"), a="mint choc chip", dt="peppermint or spearmint · green or white base"),
  X("Cookies and cream", "Vanilla ice cream with crumbled chocolate sandwich cookies, most often Oreo under licence.", u("Cookies and cream"), a="cookies 'n cream", v=[V("Oreo-licensed versions", d="Nabisco's Oreo crumbs under licence"), V("Chocolate, coffee or mint base", d="variations")], dt="cookie brand · base flavour"),
  X("Cookie dough", "Ice cream with chunks of edible (egg-free, heat-treated) cookie dough.", u("Cookie dough"), v=[V("Chocolate Chip Cookie Dough", "Ben & Jerry's", d="won a 2013 public survey of Ben & Jerry's flavours")], dt="dough type · base flavour"),
  X("Rocky road", "Chocolate ice cream with nuts and whole or diced marshmallows.", u("Rocky road (ice cream)"), dt="nut type · marshmallow size"),
  X("Cherry ice cream", "Ice cream made with cherries; mass-produced in the US since at least 1917.", u("Cherry ice cream"), v=[V("Cherry Garcia", "Ben & Jerry's", "1987", "cherries and chocolate; named for Jerry Garcia")], dt="cherry type · chocolate pieces"),
  X("Butter pecan", "Buttery vanilla ice cream with roasted pecans, prominent in the southern US.", u("Butter pecan"), v=[V("Butter almond", d="almonds instead of pecans")], dt="nut roast · base"),
  X("Pistachio ice cream", "Pistachio-flavoured ice cream, often distinctively green.", u("Pistachio ice cream"), dt="nut paste vs flavouring · colour"),
  X("Rum raisin", "Vanilla ice cream with rum-soaked raisins.", u("Rum raisin"), a="rum and raisin", dt="rum content · raisin size"),
  X("Tutti frutti", "Ice cream with chopped candied fruits or a mixed-fruit flavour.", u("Tutti frutti"), dt="candied fruit mix · nuts"),
  X("Moose Tracks", "Licensed flavour: vanilla ice cream with peanut-butter cups and Moose Tracks fudge.", u("Moose Tracks"), mk="Denali Flavors", y="1988", v=[V("Chocolate, mint and brownie Moose Tracks", "Denali Flavors"), V("Light and frozen yogurt versions", "Denali Flavors")], dt="licensee brand · base"),
  X("Hokey pokey", "New Zealand vanilla ice cream with small lumps of honeycomb toffee.", u("Hokey pokey (ice cream)"), v=[V("Honeycomb-ball recipe", "Tip Top", "c. 1980", "replaced the original solid toffee")], dt="toffee type"),
  X("Booza", "Arabic ice cream pounded and stretched with mastic and sahlab for a dense, elastic texture.", u("Booza"), a="Arabic ice cream", v=[V("Pistachio-coated booza", "Bakdash", d="Damascus")], dt="mastic · rose or orange-flower water · pistachio coating"),
  X("Maraş dondurma", "Turkish mastic ice cream thickened with salep, chewy and slow to melt.", u("Dondurma"), a="Turkish ice cream · dondurma", y="", dt="salep · mastic"),
 ],
 "m": [["Pints and Core range", "Ben & Jerry's"], ["Pints", "Häagen-Dazs"], ["Carte d'Or", "The Magnum Ice Cream Company"], ["Breyers", "Breyers"], ["Pints", "Jeni's Splendid Ice Creams"], ["Halo Top", "Halo Top Creamery"], ["Blue Bell", "Blue Bell Creameries"], ["Tillamook", "Tillamook County Creamery Association"], ["Dreyer's / Edy's Grand", "Dreyer's"], ["Mövenpick", "Mövenpick Ice Cream"], ["Graeter's", "Graeter's"], ["Salt & Straw", "Salt & Straw"]]})
K.append({"n": "Gelato", "a": "Italian ice cream · gelati",
 "d": "Italian-style ice cream with less butterfat (6–9%) and less air (20–35%) than other ice creams, for intense flavour.",
 "t": ["artisanal (gelateria)", "packaged pint", "crema (custard) base", "fruit base"],
 "s": u("Gelato"),
 "x": [
  X("Fior di latte", "Plain base gelato with no flavourings and no eggs; the original gelato.", u("Gelato"), y="16th century (Florence)", dt="milk quality"),
  X("Stracciatella", "Fior di latte gelato with fine strands of drizzled chocolate.", u("Stracciatella (ice cream)"), mk="Ristorante La Marianna", y="1961 (Bergamo)", dt="chocolate type"),
  X("Spumoni", "Moulded gelato in layers, usually pistachio, cherry and chocolate, with candied fruit and nuts.", u("Spumoni"), y="late 19th century (Naples)", dt="layer flavours · candied fruit · whipped-cream lightened"),
  X("Tartufo", "Ball of two or more gelato flavours, often with a melted-chocolate centre, from Pizzo.", u("Tartufo"), a="tartufo di Pizzo", dt="flavours · cocoa or nut coating"),
 ],
 "m": [["Grom", "Grom"], ["Talenti", "Talenti"]]})
K.append({"n": "Sorbet", "a": "sorbetto · water ice · sherbet (US, with dairy)",
 "d": "Frozen dessert of ice with fruit juice or purée, or wine, liqueur or honey, without dairy.",
 "t": ["fruit sorbet", "wine or liqueur sorbet", "palate-cleanser", "sherbet (North American, with dairy)"],
 "s": u("Sorbet"),
 "x": [
  X("Granita", "Sicilian sorbet stirred while freezing into many tiny ice crystals; lemon, coffee or fruit.", u("Granita"), a="granita siciliana", v=[V("Messina style", d="creamy, served with brioche"), V("Palermo / west-coast style", d="chunkiest")], dt="texture (chunky to smooth) · flavour"),
  X("Italian ice", "Semi-frozen ice whipped with fruit concentrates, derived from granita; no dairy or egg.", u("Italian ice"), dt="consistency · flavour"),
  X("Givré", "Sorbet served in a frozen coconut shell or hollowed-out fruit such as a lemon.", u("Sorbet"), a="frosted fruit · citron givré", dt="fruit shell"),
 ]})
K.append({"n": "Frozen yogurt", "a": "froyo · frogurt",
 "d": "Frozen dessert like ice cream but made with yogurt, often with live cultures, tarter and lower in fat.",
 "t": ["soft-serve", "packaged tub", "live cultures", "fat-free / sugar-free"],
 "s": u("Frozen yogurt"),
 "x": [
  X("Tart frozen yogurt with toppings", "Tangy soft-serve yogurt customised with toppings.", u("Pinkberry"), mk="Pinkberry", y="2005"),
  X("Self-serve frozen yogurt", "Customers pull their own flavours and add toppings, paying by weight.", u("Yogurtland"), mk="Yogurtland", dt="flavours · toppings"),
 ],
 "m": [["TCBY", "TCBY"], ["llaollao", "Llaollao"]]})
K.append({"n": "Kulfi", "a": "qulfi · Indian ice cream",
 "d": "Dense frozen dairy dessert of slow-cooked, thickened milk, frozen unchurned in moulds.",
 "t": ["malai", "kesar pista (saffron-pistachio)", "mango", "badam (almond)", "elaichi (cardamom)", "stick", "cone mould"],
 "s": u("Kulfi"),
 "x": [
  X("Matka kulfi", "Kulfi frozen in sealed moulds sunk in a matka pot of ice and salt; the traditional method.", u("Kulfi"), y="16th century (Mughal Delhi)", v=[V("Kuremal Mohan Lal Kulfi Wale", y="1906", d="Old Delhi kulfi shop"), V("Prakash Kulfi", y="1956", d="Lucknow kulfi shop")], dt="flavour · mould (kulhar, cone)"),
  X("Kulfi falooda", "Kulfi served with falooda: vermicelli, rose syrup and sweet basil seeds.", u("Falooda"), dt="rose syrup · basil seeds"),
 ],
 "m": [["Kulfi", "Vadilal"], ["Kulfi", "Amul"], ["Kulfi", "Bombay Kulfi"]]})
K.append({"n": "Mochi ice cream", "a": "ice cream mochi · mochi balls",
 "d": "Small balls of ice cream wrapped in soft pounded-rice mochi.",
 "t": ["vanilla, chocolate, strawberry", "green tea", "mango", "multipack"],
 "s": u("Mochi ice cream"),
 "x": [
  X("Yukimi Daifuku", "Lotte's original mochi ice cream: rice-starch mochi around an ice-milk centre, sold in pairs.", u("Yukimi Daifuku"), mk="Lotte Wellfood", y="1981", a="snow-viewing daifuku"),
  X("Mikawaya mochi ice cream", "US mochi ice cream developed by Frances Hashimoto of Mikawaya.", u("Mikawaya"), mk="Mikawaya", y="1993", v=[V("Hawaii debut", "Mikawaya", "1994"), V("My/Mo Mochi Ice Cream", "My/Mochi Ice Cream", "2017", "brand relaunch")], dt="flavours"),
 ],
 "m": [["Little Moons", "Little Moons"]]})
K.append({"n": "Ice lolly", "a": "ice pop · popsicle · icy pole · ice block · paleta · freezie",
 "d": "Flavoured liquid, water- or cream-based, frozen at rest on a stick.",
 "t": ["water ice", "fruit-juice", "cream-based", "multipack", "freeze pop (tube, no stick)"],
 "s": u("Ice pop"),
 "x": [
  X("Popsicle", "The original fruit-flavoured ice on a stick, patented by Frank Epperson.", u("Popsicle (brand)"), mk="Popsicle", y="1905 (claimed); patented 1923–24", a="Epsicle", dt="flavours · twin stick"),
  X("Paleta", "Mexican ice pop of fresh fruit, milk- or water-based, sold by paleteros.", u("Ice pop"), a="paleta de agua · paleta de leche", v=[V("Paletería La Michoacana", y="1940s", d="franchise from Tocumbo, Michoacán")], dt="milk or water base · fruit · chili and chamoy"),
  X("Freeze pop", "Flavoured liquid sealed in a plastic tube, frozen without a stick.", u("Freezie"), a="freezie · ice pop (UK)", v=[V("Otter Pops", d="one of the earliest US brands")], dt="tube width · flavour"),
  X("Bomb Pop", "Rocket-shaped cherry, lime and blue-raspberry ice pop.", u("Bomb Pop"), mk="Wells Enterprises", v=[V("Original", "Wells Enterprises"), V("Extremes Super Sour", "Wells Enterprises")], dt="flavour layers"),
  X("Fab", "Strawberry and vanilla lolly dipped in chocolate with sprinkles, after the Thunderbirds era.", u("Fab (brand)"), mk="J. Lyons and Co.", y="1960s", v=[V("Zoom", "J. Lyons and Co.", "1960s", "precursor")], dt="sprinkles"),
  X("Twister", "Spiral lolly of pineapple ice cream and lime ice around strawberry ice.", u("Twister (ice cream)"), mk="The Magnum Ice Cream Company", y="1982", a="Tangle Twister"),
  X("Calippo", "Water ice pushed up from a cardboard tube.", u("Calippo"), mk="The Magnum Ice Cream Company", y="1984"),
  X("Solero", "Fruit-ice-coated ice cream on a stick.", u("Solero (ice cream)"), mk="The Magnum Ice Cream Company", y="1994", a="Salar"),
  X("Garigari-kun", "Japanese soda-flavoured ice pop with an ice shell and shaved-ice centre.", GG, mk="Akagi Nyugyo", y="1981", v=[V("Soda", "Akagi Nyugyo", "1981", "best seller"), V("Cola and grapefruit", "Akagi Nyugyo", "1981"), V("Corn potage", "Akagi Nyugyo", "2012", "novelty flavour")], dt="flavour"),
  X("Paddle Pop", "Australian ice confection on a wooden stick with a lion mascot.", u("Paddle Pop"), mk="Streets"),
  X("Bubble O' Bill", "Cowboy-face ice cream lolly with a bubblegum nose.", u("Bubble O' Bill"), mk="Streets"),
 ]})
K.append({"n": "Stick bar & choc ice", "a": "choc ice · ice cream bar · stick bar · novelty",
 "d": "Block or stick of ice cream thinly coated in chocolate or compound coating.",
 "t": ["on a stick", "stickless block", "milk, dark or white coating", "nut-coated", "multipack"],
 "s": u("Choc ice"),
 "x": [
  X("Good Humor bar", "Chocolate-coated ice cream bar on a stick sold from ice cream trucks.", u("Good Humor"), mk="Good Humor", y="1920 (patent 1923)"),
  X("Eskimo Pie", "Foil-wrapped chocolate-covered vanilla ice cream bar; the first such US dessert.", u("Edy's Pie"), mk="Christian Kent Nelson", y="1921 (patent 1922)", a="Edy's Pie · I-Scream Bar", v=[V("Edy's Pie", "Dreyer's", d="renamed version")], dt="foil wrap · coating"),
  X("Klondike bar", "Square, stickless chocolate-coated ice cream bar.", u("Klondike bar"), mk="Isaly Dairy Company", y="1922", v=[V("Klondike", "Good Humor-Breyers", d="current brand owner")], dt="flavour · coating"),
  X("Magnum", "Thick vanilla ice cream bar on a stick with a cracking real-chocolate coating.", u("Magnum (ice cream)"), mk="Frisko", y="1988", v=[V("Magnum Classic", "Frisko", "1988", "86 g, 120 ml"), V("Almond, Double Chocolate, White", "The Magnum Ice Cream Company", "1992"), V("Magnum Intense", "The Magnum Ice Cream Company", "2002"), V("7 Deadly Sins", "The Magnum Ice Cream Company", "2002", "limited edition"), V("Magnum Moments / mini", "The Magnum Ice Cream Company", "2002")], dt="coating (milk, dark, white, almond) · size (mini, classic) · limited editions"),
  X("Dove Bar", "Vanilla ice cream bar in milk or dark chocolate.", u("Dove Bar"), mk="Dove Candies & Ice Cream", y="1956 (national 1984)", v=[V("Dove Bar", "Mars", "1986", "Mars ownership")], dt="coating · nut"),
  X("Nogger", "Vanilla ice cream bar with hard chocolate and nuts.", u("Nogger"), mk="The Magnum Ice Cream Company", y="1964 (West Germany)"),
  X("Golden Gaytime", "Toffee and vanilla ice cream dipped in chocolate and rolled in biscuit crumbs.", u("Golden Gaytime"), mk="Streets", y="1970", a="Cookie Crumble (NZ)"),
 ]})
K.append({"n": "Cone", "a": "ice cream cone · cornet · poke",
 "d": "Edible wafer cone, sold empty for home scooping or pre-filled and frozen as a wrapped cone.",
 "t": ["wafer (cake) cone", "sugar cone", "waffle cone", "chocolate-lined", "empty cones (box)", "pre-filled frozen cone"],
 "s": u("Ice cream cone"),
 "x": [
  X("Cornetto", "Pre-filled frozen cone whose wafer is sealed with oil, sugar and chocolate against sogginess.", u("Cornetto (frozen dessert)"), mk="Spica", y="1959 (Naples)", v=[V("Cornetto (Algida, Wall's, Streets, HB, Frigo)", "The Magnum Ice Cream Company", "1962–", "Unilever-era brands"), V("Cornetto Enigma", "The Magnum Ice Cream Company"), V("Cornetto Soft", "The Magnum Ice Cream Company", d="made on the spot"), V("Cornetto Max", "The Magnum Ice Cream Company")], dt="size 28–260 ml · flavour (strawberry, mint, nut)"),
  X("Drumstick", "Sugar cone with chocolate-and-nut coating and a chocolate tip; generic name in the US.", u("Drumstick (frozen dairy dessert)"), mk="Drumstick Company", y="1928", v=[V("Drumstick", "Froneri", "2016–", "current owner"), V("Vegan Drumstick", "Froneri", "2020", "Canada")], dt="flavour · coating"),
  X("99 Flake", "Soft-serve or scooped cone with a half-length Cadbury Flake, sold from ice cream vans.", u("99 Flake"), mk="Cadbury", y="by 1930", a="ninety-nine · 99", dt="soft-serve or scoop · sauce"),
  X("Choco Taco", "Folded waffle-cone 'taco' of vanilla ice cream, fudge, peanuts and chocolate (discontinued 2022).", u("Choco Taco"), mk="Klondike", dt="discontinued 2022"),
 ]})
K.append({"n": "Ice cream sandwich", "a": "cream-between · wafer ice cream · hokey pokey",
 "d": "Ice cream held between two wafers, biscuits or cookies, bought wrapped or as a vendor snack.",
 "t": ["wafer", "cookie", "chocolate-dipped", "Neapolitan filling", "multipack"],
 "s": u("Ice cream sandwich"),
 "x": [
  X("Wafer ice cream sandwich", "Block of ice cream between two flat wafers; the street-vendor classic.", u("Ice cream sandwich"), y="1890s", v=[V("Fürst-Pückler wafer", d="German, Neapolitan block"), V("Singapore wafer / potong", d="block sliced from a bar"), V("Bastani nooni", d="Iranian traditional ice cream between wafers")], dt="wafer · filling"),
  X("Chipwich", "Vanilla ice cream between two thick chocolate-chip cookies.", u("Chipwich"), mk="Crave Better Foods"),
  X("It's-It", "Ice cream between two oatmeal cookies, dipped in dark chocolate.", u("It's-It Ice Cream"), mk="It's-It Ice Cream", dt="flavours since 1980s"),
  X("Maxibon", "Chocolate-chip ice cream block half sandwiched in biscuits, half coated in chocolate.", u("Maxibon"), mk="Froneri"),
 ]})
K.append({"n": "Ice cream cake", "a": "frozen cake · ice cream gateau · ice cream log",
 "d": "Cake or moulded dessert made with ice cream, bought frozen for parties and celebrations.",
 "t": ["round party cake", "roll / log", "moulded bombe", "layered slice dessert"],
 "s": u("Ice cream cake"),
 "x": [
  X("Viennetta", "Rippled layers of ice cream separated by thin sprayed sheets of compound chocolate.", u("Viennetta"), mk="Wall's", y="by 1983", v=[V("Mint and other flavours", "Wall's"), V("Viennetta (US)", "Good Humor", "2021", "reintroduction")], dt="flavour · slice size"),
  X("Arctic roll", "Vanilla ice cream wrapped in thin sponge with raspberry sauce.", u("Arctic roll"), mk="Birds Eye", y="1958 (Eastbourne)", v=[V("Chocolate Arctic roll", "Birds Eye")]),
  X("Carvel ice cream cake", "Soft-serve ice cream cake with a layer of chocolate 'crunchies'.", u("Carvel (franchise)"), mk="Carvel", y="by 1950s", v=[V("Fudgie the Whale", "Carvel"), V("Cookie Puss", "Carvel")], dt="themed shapes"),
  X("Baked Alaska", "Ice cream on cake under browned meringue.", u("Baked Alaska"), a="Bombe Alaska"),
  X("Bombe glacée", "French ice cream dessert frozen in a spherical mould.", u("Bombe glacée"), y="by 1882"),
  X("Semifreddo", "Half-frozen moulded dessert of egg whites, sugar and cream, lighter than ice cream.", u("Semifreddo"), dt="core (nougat, fruit, cake)"),
  X("Cassata (ice cream)", "Neapolitan-style moulded ice cream with candied or dried fruit and nuts; popular in India.", u("Cassata"), dt="layers · fruit"),
 ],
 "m": [["Ice cream cakes", "Dairy Queen"], ["Ice cream cakes", "Baskin-Robbins"]]})
K.append({"n": "Dairy-free ice cream", "a": "vegan ice cream · non-dairy frozen dessert · plant-based ice cream",
 "d": "Ice cream substitute made without milk, from soy, oat, almond, coconut or similar bases.",
 "t": ["soy", "oat", "almond", "coconut", "kosher parve"],
 "s": u("Tofutti"),
 "x": [
  X("Tofutti", "Soy-based non-dairy ice cream first made for kosher customers.", u("Tofutti"), mk="Tofutti", y="1981", v=[V("Tofutti Cuties", "Tofutti", d="ice cream sandwich")]),
  X("Ben & Jerry's Non-Dairy", "Vegan pints of Ben & Jerry's flavours made without dairy.", u("Ben & Jerry's"), mk="Ben & Jerry's", y="2016", v=[V("Chunky Monkey", "Ben & Jerry's", "2016"), V("Chocolate Fudge Brownie", "Ben & Jerry's", "2016"), V("Cherry Garcia", "Ben & Jerry's", "2017")], dt="flavour"),
 ],
 "m": [["So Delicious", "Danone North America"], ["Dairy-free range", "Breyers"]]})

def B(n, c, f, seg, d, s, lines=None, sig=None, rel=None, eras=None):
    return {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": lines or [], "eras": eras or [], "sig": sig or [], "sc": [], "rel": rel or [], "s": s}
BR = [
 B("Ben & Jerry's", "United States", "1978", "Super-premium ice cream", "Vermont maker of chunky-flavour ice cream, sold to Unilever in 2000.", u("Ben & Jerry's"), ["Pints", "Non-Dairy"], ["Cherry Garcia", "Chocolate Chip Cookie Dough", "Ben & Jerry's Non-Dairy"], ["The Magnum Ice Cream Company"], ["Ben Cohen and Jerry Greenfield, 1978–2000", "Unilever, 2000–2025"]),
 B("Häagen-Dazs", "United States", "1960", "Super-premium ice cream", "Bronx-founded premium ice cream, now General Mills (Froneri in North America).", u("Häagen-Dazs"), ["Pints", "Bars"], [], ["Froneri"], ["Reuben and Rose Mattus, 1960–1983", "Pillsbury, 1983–2001", "General Mills, 2001–"]),
 B("Breyers", "United States", "1866", "Mainstream ice cream", "Oldest US ice cream maker, now part of The Magnum Ice Cream Company.", u("Breyers"), ["Ice cream", "Frozen dairy dessert", "Dairy-free"], [], ["Good Humor", "The Magnum Ice Cream Company"]),
 B("Jeni's Splendid Ice Creams", "United States", "2002", "Artisan ice cream", "Columbus, Ohio ice cream maker with scoop shops and retail pints.", u("Jeni's Splendid Ice Creams")),
 B("Grom", "Italy", "2003", "Gelato", "Turin gelato company, owned by Unilever from 2015.", u("Grom (company)")),
 B("The Magnum Ice Cream Company", "Netherlands", "2025", "Ice cream group", "World's largest ice cream maker, demerged from Unilever; owns the Heartbrand brands.", u("The Magnum Ice Cream Company"), ["Magnum", "Cornetto", "Wall's", "Ben & Jerry's", "Breyers", "Talenti", "Carte d'Or"], ["Magnum", "Cornetto", "Twister", "Calippo", "Solero", "Nogger"], ["Wall's", "Kwality Wall's", "Good Humor"]),
 B("Wall's", "United Kingdom", "1922", "Ice cream (Heartbrand)", "UK Heartbrand ice cream brand, market leader in hand-held ice creams.", u("Wall's (ice cream)"), ["Magnum", "Cornetto", "Viennetta", "Mr. Whippy mix"], ["Viennetta"], ["The Magnum Ice Cream Company"]),
 B("Froneri", "United Kingdom", "2016", "Ice cream group", "Nestlé–PAI Partners ice cream joint venture, second-largest ice cream producer.", u("Froneri"), ["Drumstick", "Maxibon", "Fab", "Mövenpick", "Häagen-Dazs (US)"], ["Drumstick", "Maxibon"], ["Dreyer's"]),
 B("Good Humor", "United States", "1920s", "Ice cream novelties", "Ice cream truck brand behind the Good Humor bar, now Good Humor-Breyers.", u("Good Humor"), [], ["Good Humor bar"], ["Breyers"]),
 B("Lotte Wellfood", "South Korea", "1967", "Confectionery and ice cream", "Korean confectionery group (formerly Lotte Confectionery).", u("Lotte Wellfood"), [], ["Yukimi Daifuku"]),
 B("Mikawaya", "United States", "", "Japanese confectionery", "Los Angeles wagashi maker that introduced mochi ice cream to the US.", u("Mikawaya"), [], ["Mikawaya mochi ice cream"], ["My/Mochi Ice Cream"]),
 B("Akagi Nyugyo", "Japan", "1931", "Ice confectionery", "Saitama ice cream maker of Garigari-kun.", GG, [], ["Garigari-kun"]),
 B("Tofutti", "United States", "1981", "Dairy-free", "New Jersey maker of soy-based dairy-free foods and ice cream substitutes.", u("Tofutti"), [], ["Tofutti"]),
 B("Halo Top Creamery", "United States", "2012", "Low-calorie ice cream", "Lower-calorie pint brand using stevia and erythritol.", u("Halo Top Creamery")),
 B("Talenti", "United States", "2003", "Gelato and sorbet", "Gelato and sorbet brand begun as a Dallas gelateria.", u("Talenti"), rel=["The Magnum Ice Cream Company"]),
 B("Dreyer's", "United States", "1928", "Mainstream ice cream", "Oakland ice cream maker selling as Dreyer's in the West and Edy's in the East.", u("Dreyer's"), ["Dreyer's Grand", "Edy's Grand", "Edy's Pie"], rel=["Froneri"]),
 B("Carvel", "United States", "", "Soft-serve and ice cream cakes", "Ice cream franchise known for soft serve and themed ice cream cakes.", u("Carvel (franchise)"), [], ["Carvel ice cream cake"]),
 B("Vadilal", "India", "1907", "Ice cream and kulfi", "Ahmedabad ice cream maker, world's top kulfi supplier.", u("Vadilal")),
 B("Kwality Wall's", "India", "", "Ice cream (Heartbrand)", "South Asian Heartbrand ice cream company.", u("Kwality Wall's"), rel=["The Magnum Ice Cream Company"]),
 B("Blue Bell Creameries", "United States", "1907", "Mainstream ice cream", "Texas ice cream maker from Brenham.", u("Blue Bell Creameries")),
 B("Mövenpick Ice Cream", "Switzerland", "", "Premium ice cream", "Swiss-origin premium ice cream made by Froneri.", u("Mövenpick Ice Cream"), rel=["Froneri"]),
]
TR = [
 {"n": "Italian gelato", "g": "Food & drink", "r": "Italy (Florence, Sicily, Naples)", "p": "16th century–present", "d": "Artisanal Italian ice cream tradition of low-fat, low-air gelato made daily in gelaterie.", "tech": "custard or milk base pasteurised, batch-frozen with little air", "mat": "milk, sugar, nuts, fruit", "forms": ["Fior di latte", "Stracciatella", "Spumoni", "Tartufo", "Granita"], "ctr": ["Café Procope (Procopio dei Coltelli, 1686)", "Carpigiani (Bologna, batch freezers)"], "auth": "6–9% butterfat, 20–35% air, served softer than ice cream", "s": u("Gelato")},
 {"n": "Kulfi", "g": "Food & drink", "r": "Indian subcontinent (Delhi)", "p": "16th century (Mughal)–present", "d": "Unchurned frozen dessert of slow-reduced milk, sold by kulfiwallahs.", "tech": "milk reduced and caramelised, frozen in sealed moulds in a matka of ice and salt", "mat": "milk, sugar, pistachio, saffron, cardamom", "forms": ["Matka kulfi", "Kulfi falooda"], "ctr": ["Kuremal Mohan Lal Kulfi Wale, Old Delhi (1906)", "Prakash Kulfi, Lucknow (1956)"], "auth": "dense, slow-melting, no ice crystals, cooked-milk taste", "s": u("Kulfi")},
 {"n": "Mexican paleta", "g": "Food & drink", "r": "Mexico (Tocumbo, Michoacán)", "p": "1940s–present", "d": "Fresh-fruit ice pops, milk- or water-based, made by paleterías and sold by paleteros.", "tech": "fresh fruit frozen on a stick", "mat": "fruit, milk, chili, chamoy", "forms": ["Paleta"], "ctr": ["Paletería La Michoacana"], "auth": "fresh-fruit base; local flavours such as tamarind, mamey, horchata", "s": u("Ice pop")},
 {"n": "Maraş dondurma", "g": "Food & drink", "r": "Turkey (Kahramanmaraş)", "p": "", "d": "Turkish mastic ice cream thickened with salep.", "tech": "pounded and stretched rather than churned", "mat": "cream, salep, mastic, sugar", "forms": ["Maraş dondurma", "Booza"], "ctr": ["Kahramanmaraş"], "auth": "chewy, elastic, slow to melt", "s": u("Dondurma")},
]
notes = ("All 12 planned kinds built new (shelf had no old data). Left out: Wall's Mini Milk, Feast and Zoom as own archetypes, Creamsicle/Fudgsicle "
         "(no page retrieved; Wikipedia titles missing or rate-limited); Carte d'Or kept only as a tub model (brand page 403, attested via Miko page); "
         "soft serve, sundaes, shaved ice/kakigori/bingsu/halo-halo omitted as served desserts rather than bought products; Streets, Frisko, Spica, "
         "Wells Enterprises etc. used as archetype makers without register entries (no brand page retrieved for some).")
out = {"kinds": K, "brands": BR, "traditions": TR, "notes": notes}
p = 'work/J8/shelves/06_00.json'; tmp = p + '.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1); os.replace(tmp, p)
print(len(K), sum(len(k.get('x', [])) for k in K), len(BR), len(TR))
