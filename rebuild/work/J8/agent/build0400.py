import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, a='', v=None, dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s if s.startswith('http') else W + s, "v": v or [], "dt": dt}
def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}
def K(n, a, d, s, t=None, x=None, m=None):
    k = {"n": n, "a": a, "d": d}
    if t: k["t"] = t
    k["s"] = W + s; k["x"] = x or []
    if m: k["m"] = m
    return k

kinds = [
 K("Potato crisps", "crisps · potato chips · chips",
   "Thin potato slices fried, baked or air-fried until crunchy, then salted or seasoned.", "Potato_chips",
   t=["ready salted", "flavoured", "crinkle-cut / ridged", "baked", "shaped", "vegetable (beetroot, parsnip, sweet potato)", "unsalted with salt sachet"],
   x=[
    X("Smiths crisps", "Original British bagged crisp, first sold with a twist of salt in a greaseproof bag.", "Smiths", "1920", "Smiths_(snack_foods)",
      v=[V("Salt 'n' Shake", "", "", "unseasoned crisps with a salt sachet, heir to the salt twist"), V("Salt and vinegar", "Smiths", "1967", "launched nationally, starting the UK flavour rivalry")],
      dt="salt twist · flavours · UK and Australian lines differ"),
    X("Tayto cheese and onion", "First seasoned crisp, made by Joe 'Spud' Murphy's Irish company.", "Tayto", "1954", "Tayto_(Republic_of_Ireland)",
      a="Tayto",
      v=[V("Tayto (Northern Ireland)", "Tayto Group", "", "separate Tandragee company, largest-selling crisp in Northern Ireland")],
      dt="cheese and onion · salt and vinegar · Mr Tayto packs"),
    X("Walkers crisps", "Britain's best-selling crisp, made in Leicester since 1948.", "Walkers", "1948", "Walkers_(snack_foods)",
      v=[V("Cheese & Onion", "Walkers", "1954", "blue bag"), V("Salt & Vinegar", "Walkers", "1967", "green bag"),
         V("Max", "Walkers", "1999", "ridged crisps"), V("Sensations", "Walkers", "2002", "black bags, 'adult' flavours"), V("Baked", "Walkers", "2006", "oven-baked, lower fat")],
      dt="flavour colour code (blue cheese & onion, green salt & vinegar) · pack size"),
    X("Lay's", "PepsiCo's global potato-chip brand, sold under other names in some markets.", "Lay's", "1938", "Lay%27s",
      dt="regional flavours · classic, wavy, kettle-cooked lines"),
    X("Golden Wonder", "British crisp that led the market in the 1960s, overtaking Smiths.", "Golden Wonder", "1947", "Golden_Wonder",
      v=[V("Ringos", "Golden Wonder", "", "ring-shaped snack")], dt="flavours · pack colours"),
    X("Ruffles", "Crinkle-cut (ridged) potato chip, sold as Walkers Max and Lay's Maxx in some markets.", "", "1948", "Ruffles_(potato_chips)",
      v=[V("Ruffles trademark", "Bernhardt Stahmer", "1948", "original owner"), V("Ruffles", "Frito Company", "1958", "rights acquired"), V("Walkers Max", "Walkers", "1999", "UK version")],
      dt="ridge depth · flavours"),
    X("McCoy's", "Thick crinkle-cut British crisp.", "KP Snacks", "1985", "McCoy%27s_(crisp)", dt="ridged cut · strong flavours"),
    X("Calbee Potato Chips", "Japan's leading potato chip, holding most of the domestic market.", "Calbee", "1975", "Calbee",
      dt="Japanese flavours: norishio, consommé, soy sauce and butter, wasabi"),
    X("Torres", "Spanish handcrafted crisps, with a premium Selecta range.", "Patatas Torres", "1969", "https://www.potatopro.com/node/170804",
      v=[V("Selecta", "Patatas Torres", "", "extra virgin olive oil, black truffle, Iberian ham, Mediterranean herbs")], dt="olive oil · truffle · ham flavours · unsalted"),
    X("Pom-Bear", "Teddy-bear-shaped potato crisp.", "Intersnack", "1987", "Pom-Bear", a="Pom-Bär",
      v=[V("Pom-Bär", "Intersnack", "1987", "launched in Germany"), V("Pom-Bear", "Intersnack", "1990", "UK launch")], dt="original · cheese and onion · salt and vinegar"),
    X("Terra Chips", "American root-vegetable chips.", "", "1990", "Terra_Chips", v=[V("Terra", "Hain Celestial Group", "", "current owner")], dt="root vegetable mix · sweet potato"),
   ],
   m=[["Herr's potato chips", "Herr's"], ["Utz potato chips", "Utz Brands"], ["Jays potato chips", "Jays Foods"], ["Old Dutch potato chips", "Old Dutch Foods"],
      ["Wise potato chips", "Wise Foods"], ["Seabrook Crisps", "Seabrook Crisps"], ["Balaji wafers", "Balaji Wafers"], ["Funny-frisch", "Intersnack"]]),

 K("Kettle crisps", "kettle chips · kettle-cooked · hand-cooked · batch-cooked crisps",
   "Thicker potato crisps cooked in batches (kettle-style), sold as a premium crisp.", "Potato_chips",
   t=["sea salt", "salt and vinegar", "skin-on", "hand-cooked"],
   x=[
    X("Cape Cod Potato Chips", "Batch-cooked kettle-style chip that helped make the style a premium product.", "Cape Cod Potato Chips", "1980", "Cape_Cod_Potato_Chips", dt="thick cut · sea salt · owned by Campbell's"),
    X("Kettle Brand", "Kettle-cooked chips from Salem, Oregon, with a UK base in Norwich.", "Kettle Foods", "1977", "Kettle_Foods", a="Kettle Chips", dt="sea salt · balsamic · US and UK ranges"),
    X("Tyrrells", "British hand-cooked crisps.", "Tyrrells", "", "Tyrrells_(crisps)", dt="hand-cooked · vegetable crisps · owned by KP Snacks"),
    X("Zapp's", "Louisiana kettle chips cooked in peanut oil.", "", "", "Zapp%27s", v=[V("Spicy Cajun Crawtator", "", "", "Cajun flavour"), V("Voodoo", "", "", "signature flavour")], dt="peanut oil · Cajun flavours"),
   ]),

 K("Stackable crisps", "stacked chips · fabricated crisps · tube crisps",
   "Uniform saddle-shaped crisps made from dried-potato dough and sold stacked in a tube.", "Pringles",
   t=["original", "flavoured", "rice-based", "multigrain"],
   x=[
    X("Pringles", "Originator of the stacked crisp in a tube, made from dried-potato dough.", "Pringles", "1968", "Pringles",
      v=[V("Pringle's Newfangled Potato Chips", "Procter & Gamble", "1968", "original name"), V("Rice-based Pringles", "Pringles", "2010", "rice version")],
      dt="saddle shape · tube size · flavour"),
    X("Lay's Stax", "Frito-Lay's stacked crisp made to compete with Pringles.", "Lay's", "2003", "Lay%27s_Stax", dt="tube · flavours"),
   ]),

 K("Tortilla chips", "nachos · corn chips · totopos",
   "Triangles of nixtamalised-corn tortilla, fried or baked, for eating plain or with dips.", "Tortilla_chips",
   t=["lightly salted", "flavoured", "blue corn", "rolled", "scoop shape", "restaurant style"],
   x=[
    X("Totopo", "Mexican fried or baked tortilla pieces from which tortilla chips grew.", "", "", "Tortilla_chips", dt="yellow, white, blue or red corn"),
    X("Doritos", "First tortilla chip sold nationally in the US, known for strong seasonings.", "Frito-Lay", "1966", "Doritos",
      v=[V("Toasted Corn", "Frito-Lay", "1966", "first flavour"), V("Taco", "Frito-Lay", "1967", ""), V("Nacho Cheese", "Frito-Lay", "1972", ""), V("Doritos 3D", "Frito-Lay", "", "puffed variant")],
      dt="flavour · regional ranges"),
    X("Tostitos", "Lightly salted tortilla chip sold with salsa and queso dips.", "Frito-Lay", "1977", "Tostitos",
      v=[V("Tostitos", "Frito-Lay", "1981", "national roll-out"), V("Scoops", "Frito-Lay", "2001", "bowl shape")], dt="shape · dips"),
    X("Takis", "Rolled, taquito-shaped tortilla chip with intense chilli flavour.", "Barcel", "1999", "Takis",
      v=[V("Taquis", "Barcel", "1999", "original name in Mexico"), V("Fuego", "Barcel", "2006", "chilli-lime, purple bag")], dt="rolled shape · heat level"),
   ],
   m=[["Mission tortilla chips", "Mission Foods"], ["Old Dutch Restaurante Style", "Old Dutch Foods"]]),

 K("Extruded corn snack", "corn puffs · cheese puffs · cheese curls · corn curls",
   "Corn (or potato and corn) dough pushed through a die, puffed by heat and seasoned.", "Cheese_puffs",
   t=["puffed (crunchy)", "baked", "fried", "cheese-coated", "ring-shaped", "shaped", "peanut-flavoured"],
   x=[
    X("Fritos", "Corn chip of fried extruded whole cornmeal, made without nixtamalisation.", "Frito-Lay", "1932", "Fritos", v=[V("Fritos", "Frito Corporation", "1932", "Charles Elmer Doolin")], dt="corn chip · scoops"),
    X("Cheetos", "Best-selling cheese puff, invented by Fritos creator Charles Elmer Doolin.", "Frito-Lay", "1948", "Cheetos", a="Chee-tos", dt="crunchy or puffed · cheese flavours"),
    X("Cheez Doodles", "East Coast US cheese puff first made in the Bronx.", "Wise Foods", "", "Cheez_Doodles", v=[V("Cheez Doodles", "King Kone Corp.", "", "original maker")], dt="crunchy or puffed"),
    X("Twisties", "Australian cheese curl, sold as Fonzies in Europe.", "Smiths", "1950", "Twisties", v=[V("Twisties", "General Foods", "1950", "launch"), V("Fonzies", "", "", "European name")], dt="cheese · chicken"),
    X("Wotsits", "British cheese-flavoured baked corn puff.", "Walkers", "1971", "Wotsits", v=[V("Wotsits", "Golden Wonder", "1971", "launch"), V("Wotsits", "Walkers", "2002", "brand bought by Walkers")], dt="'Really Cheesy' · flavours"),
    X("Quavers", "Curly, deep-fried potato-based puff named after the musical note.", "Smiths", "1968", "Quavers", v=[V("Quavers", "Walkers", "", "current maker")], dt="cheese"),
    X("Hula Hoops", "Short hollow cylinders of potato and corn.", "KP Snacks", "1973", "Hula_Hoops", v=[V("Chio Hula Hoops", "Intersnack", "", "Belgium"), V("Vico", "Intersnack", "2016", "France")], dt="original · flavours"),
    X("Monster Munch", "British baked corn snack shaped like monsters' feet.", "Smiths", "1977", "Monster_Munch", v=[V("Monster Munch", "Walkers", "", "current maker")], dt="roast beef · pickled onion · Flamin' Hot"),
    X("Funyuns", "Onion-flavoured extruded corn rings shaped like onion rings.", "Frito-Lay", "1969", "Funyuns", a="Cebolitos", dt="onion and salt"),
    X("Bugles", "Corn snack from General Mills.", "General Mills", "", "Bugles_(snack)", v=[V("Bugles", "Tom's Snacks", "", "made under licence")], dt="original · flavours"),
    X("Bamba", "Israeli peanut-butter-flavoured puffed maize snack.", "Osem", "1964", "Bamba_(snack)", v=[V("Erdnussflips", "", "1963", "similar German peanut puff")], dt="peanut · nougat-filled"),
    X("Kurkure", "Indian spiced crunchy puffcorn of rice, lentil and corn.", "Frito-Lay", "1999", "Kurkure", dt="masala flavours · India and Pakistan"),
   ]),

 K("Popcorn", "popped corn · pop-corn",
   "Corn kernels heated until they burst and puff, sold popped and seasoned or as kernels for popping.", "Popcorn",
   t=["salted", "sweet", "sweet and salty", "butter", "toffee / caramel", "microwave bag", "kernels", "ready to eat"],
   x=[
    X("Cracker Jack", "Molasses-caramel popcorn and peanuts packed with a prize; called the first junk food.", "Frito-Lay", "1896", "Cracker_Jack", v=[V("Cracker Jack", "Frito-Lay", "1997", "owner since"), V("QR-code prize", "Frito-Lay", "2016", "replaced the toy")], dt="prize · baseball link"),
    X("Caramel corn", "Popcorn coated with a thin caramel shell.", "", "", "Caramel_corn", a="toffee popcorn", dt="caramel · molasses · baked crisp"),
    X("Kettle corn", "Sweet-and-salty popcorn, traditionally made in cast-iron kettles.", "", "", "Kettle_corn", dt="sugar · salt · oil"),
    X("Microwave popcorn", "Unpopped kernels with fat and seasoning in a sealed bag for the microwave.", "", "", "Microwave_popcorn",
      v=[V("Pop Secret", "General Mills", "1985", "now owned by Our Home"), V("Orville Redenbacher's", "Conagra Brands", "", "brand launched 1969")], dt="butter level · flavour"),
    X("Orville Redenbacher's", "American popping-corn brand fronted by its founder.", "", "1969", "Orville_Redenbacher%27s", v=[V("Orville Redenbacher's", "Chester Inc.", "1969", "launch"), V("Orville Redenbacher's", "Conagra Brands", "1990", "owner since")], dt="kernels · microwave bags"),
    X("Smartfood", "Pre-popped white cheddar popcorn from Massachusetts.", "", "1984", "Smartfood", v=[V("Smartfood", "Frito-Lay", "1989", "bought by Frito-Lay")], dt="white cheddar · flavours"),
    X("Butterkist", "Britain's best-selling popcorn brand.", "KP Snacks", "", "Butterkist", dt="toffee · sweet · salted"),
    X("Jolly Time", "Brand of the oldest US popcorn producer.", "American Pop Corn Company", "1914", "American_Pop_Corn_Company", dt="kernels · microwave"),
   ]),

 K("Pretzel", "Brezel · Breze · Brezn · bretzel",
   "Knotted or stick-shaped bread, dipped in lye or soda before baking; soft to eat fresh or hard-baked to keep.", "Pretzel",
   t=["soft", "hard", "sticks", "rods", "twists", "salted", "chocolate-coated"],
   x=[
    X("Laugenbrezel", "Soft German lye pretzel with the classic knotted loop and coarse salt.", "", "", "Pretzel", a="lye pretzel · Brezn",
      v=[V("Bavarian pretzel", "", "", "thick arms, little fat"), V("Swabian pretzel", "", "", "very thin arms, fat split belly, more fat"), V("Alsatian bretzel", "", "", "sold at street stands and bakeries")],
      dt="arm thickness · belly split · salt"),
    X("Hard pretzel", "Long-keeping hard-baked pretzel, an industry born in south-eastern Pennsylvania.", "", "1861", "Pretzel", a="Pennsylvania Dutch pretzel",
      v=[V("Sturgis bakery", "", "1861", "Lititz, Pennsylvania, first commercial hard-pretzel bakery (article also gives 1850)"), V("Pretzel sticks", "", "", "about 3 mm thick"), V("Pretzel rods", "", "", "thicker sticks, also called Bavarian pretzels in the US")],
      dt="loops, braids, letters, sticks, rods"),
    X("Rold Gold", "American hard-pretzel brand.", "Frito-Lay", "1917", "Rold_Gold", v=[V("American Cone and Pretzel Company", "", "1917", "original company, Lorraine Schumaker")], dt="twists · sticks · rods"),
    X("Snyder's of Hanover", "Pennsylvania pretzel snacks sold internationally.", "Snyder's of Hanover", "", "Snyder%27s_of_Hanover", dt=""),
    X("Pretz", "Japanese pretzel sticks.", "Glico", "", "Pretzel", dt="flavoured sticks"),
    X("Chocolate-covered pretzel", "Pretzels coated in chocolate, a US Christmas gift.", "", "", "Pretzel", dt="milk, dark, white chocolate"),
   ]),

 K("Pork scratchings & chicharrón", "pork scratchings · pork rinds · crackling · cracklins · chicharrón · chicharon",
   "Pork skin rendered and fried, roasted or baked until crisp, eaten as a snack.", "Pork_rind",
   t=["scratchings (hard, with fat)", "puffed rinds", "crackling", "seasoned"],
   x=[
    X("Pork scratchings", "British deep-fried salted pork rind with fat, eaten cold as a pub snack.", "", "", "Pork_rind", dt="hair-free · fat layer · salt"),
    X("Pork rinds", "North American bagged skins, rendered, dried, then fried and puffed.", "", "", "Pork_rind", v=[V("Cajun cracklins", "", "", "fried fat with skin, seasoned after frying")], dt="puffed · seasonings"),
    X("Chicharrón", "Fried pork belly or rinds of Spain, Mexico and the Philippines.", "", "", "Chicharr%C3%B3n", a="chicharrones · chicharon",
      v=[V("Chicharon", "", "", "Philippines, eaten with vinegar"), V("Chicharrones", "", "", "Spain")], dt="pork, chicken, mutton or beef"),
    X("Khaep mu", "Chiang Mai pork rind, salt-cured, slow-cooked in fat and baked crisp.", "", "", "Pork_rind", dt="with nam phrik num"),
    X("Flæskesvær", "Dried pork-rind snack of Denmark, Norway and Sweden, served cold.", "", "", "Pork_rind", dt=""),
   ],
   m=[["Mr. Porky", "Tayto Group"]]),

 K("Prawn cracker", "prawn crackers · krupuk · keropok · kropek · shrimp chips",
   "Cracker of starch and ground prawn, dried and then fried so it puffs up light and crisp.", "Prawn_cracker",
   t=["ready to eat", "uncooked (to fry)", "fish", "cassava"],
   x=[
    X("Krupuk udang", "Indonesian prawn cracker, part of the maritime Southeast Asian krupuk family.", "", "", "Krupuk",
      v=[V("Keropok udang", "", "", "Malaysia, Singapore, Brunei"), V("Kropek", "", "", "Philippines"), V("Bánh phồng tôm", "", "", "Vietnam")], dt="tapioca starch · prawn content"),
    X("Kappa Ebisen", "Japanese wheat-and-shrimp snack stick.", "Calbee", "1964", "Kappa_Ebisen", dt="shrimp · wheat flour"),
    X("Saeukkang", "South Korean shrimp cracker.", "Nongshim", "1971", "Saeukkang", a="Shrimp Cracker", dt=""),
    X("Skips", "Small British prawn-cocktail snack that melts on the tongue.", "KP Snacks", "1974", "Skips_(snack)", dt="prawn cocktail · tapioca (UK) or maize (Ireland)"),
   ]),

 K("Rice cracker & senbei", "rice crackers · senbei · sembei · arare",
   "East Asian cracker of cooked rice or rice flour, baked or fried, often brushed with soy sauce.", "Rice_cracker",
   t=["baked", "fried", "soy-glazed", "sweet", "nori-wrapped", "glutinous (Kansai)", "uruchi rice (Kantō)"],
   x=[
    X("Senbei", "Japanese rice cracker; salty soy senbei spread from a Sōka teahouse in the Edo period.", "", "Edo period (soy); 737 (first record)", "Senbei",
      v=[V("Katayaki senbei", "", "", "hard-baked"), V("Nure senbei", "", "", "wet, soy sauce"), V("Ebi senbei", "", "", "shrimp"), V("Nori senbei", "", "", "seaweed"), V("Nanbu senbei", "", "", "wheat flour")],
      dt="thickness (usuyaki, atsuyaki) · glaze · shape"),
    X("Arare", "Bite-sized glutinous-rice crackers flavoured with soy sauce, named after hailstones.", "", "", "Arare_(food)", dt="size · shape · flavour"),
    X("Kaki no tane", "Crescent soy rice crackers, often mixed with peanuts (kaki-pi).", "", "", "Kaki_no_tane", a="kaki-pi",
      v=[V("KAMEDA Kaki-no-Tane with peanuts", "Kameda Seika", "1966", "JAXA space food, 2017")], dt="wasabi · pepper flavours"),
    X("Happy Turn", "Kameda Seika rice cracker.", "Kameda Seika", "", "https://kamedaseika.co.jp/en/company/rice-cracker-business", dt=""),
    X("Want Want rice crackers", "Taiwanese rice crackers from the country's largest rice-cake maker.", "Want Want", "", "Want_Want", dt="senbei · rice crisps"),
   ]),

 K("Seaweed snack", "seaweed snack · gim · kim · nori snack",
   "Thin sheets of dried laver, roasted or fried with oil and salt and eaten as a crisp snack.", "Gim_(food)",
   t=["roasted", "fried", "sesame oil", "tempura", "sandwich"],
   x=[
    X("Seasoned gim", "Korean laver roasted with sesame oil and salt, cut into snack sheets.", "", "", "Gim_(food)", dt="sesame oil · salt"),
    X("Tao Kae Noi", "Thai crispy seaweed snack.", "Tao Kae Noi", "2004", "Tao_Kae_Noi", dt="fried, grilled, baked, tempura"),
   ]),

 K("Namkeen & Bombay mix", "namkeen · farsan · Bombay mix · chevda · bhujia",
   "South Asian savoury fried snacks of gram flour, lentils, nuts and puffed rice, spiced and sold loose or packed.", "Bombay_mix",
   t=["mix", "sev / bhujia", "spiral (chakli)", "mild", "spicy"],
   x=[
    X("Bombay mix", "Spicy mix of sev, fried lentils, peanuts, chickpeas and puffed rice.", "", "", "Bombay_mix", dt="ingredients · heat"),
    X("Bikaneri bhujia", "Crisp moth-bean and gram-flour noodles from Bikaner.", "", "", "Bikaneri_bhujia", a="bhujia", dt="spice level"),
    X("Sev", "Small crunchy fried chickpea-flour noodles.", "", "", "Sev_(food)", a="oma podi", dt="thickness · flavour"),
    X("Chakli", "Spiral, spiked snack of rice and gram flours.", "", "", "Chakli", a="chakali · chakri",
      v=[V("Murukku", "", "", "South Indian rice and black-gram version")], dt="flour mix"),
   ],
   m=[["Haldiram's namkeen", "Haldiram's"], ["Bikanervala namkeen", "Bikanervala"]]),
]

def B(n, c, f, seg, d, s, lines=None, eras=None, sig=None, rel=None):
    return {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": lines or [], "eras": eras or [], "sig": sig or [], "sc": [], "rel": rel or [], "s": s if s.startswith('http') else W + s}

brands = [
 B("Walkers", "United Kingdom", "1948", "Crisps (mass market)", "Leicester crisp maker founded by Henry Walker, Britain's largest; owned by PepsiCo since 1989.", "Walkers_(snack_foods)",
   lines=["Walkers", "Sensations", "Max", "Baked", "Wotsits", "Quavers", "Monster Munch"], eras=["Walker family, 1948–1970", "Standard Brands, from 1970", "PepsiCo, from 1989"], sig=["Walkers crisps", "Wotsits", "Quavers", "Monster Munch"], rel=["Lay's", "Smiths"]),
 B("Lay's", "United States", "1938", "Crisps (mass market)", "PepsiCo's global potato-chip brand from the Frito-Lay division.", "Lay%27s",
   lines=["Lay's", "Lay's Stax"], eras=["H.W. Lay & Company, from 1938", "Frito-Lay, from 1961", "PepsiCo, from 1965"], sig=["Lay's", "Lay's Stax"], rel=["Walkers", "Smiths"]),
 B("Pringles", "United States", "1968", "Stackable crisps", "Stacked crisp in a tube invented by Procter & Gamble.", "Pringles",
   eras=["Procter & Gamble, 1968–2012", "Kellanova (Kellogg's), 2012–2024", "Mars, from 2024"], sig=["Pringles"]),
 B("Kettle Foods", "United States", "1977", "Kettle crisps", "Salem, Oregon maker of kettle-cooked chips, founded by Cameron Healy; owned by Campbell's since 2018.", "Kettle_Foods",
   lines=["Kettle Brand"], eras=["Cameron Healy, from 1977", "Lion Capital, 2006", "Diamond Foods, 2010–2016", "Snyder's-Lance, 2016", "Campbell's, from 2018"], sig=["Kettle Brand"], rel=["Cape Cod Potato Chips"]),
 B("Cape Cod Potato Chips", "United States", "", "Kettle crisps", "Hyannis, Massachusetts maker of kettle-cooked chips, owned by Campbell's since 2018.", "Cape_Cod_Potato_Chips", sig=["Cape Cod Potato Chips"], rel=["Kettle Foods"]),
 B("Tyrrells", "United Kingdom", "", "Hand-cooked crisps", "British hand-cooked crisp maker owned by KP Snacks.", "Tyrrells_(crisps)", sig=["Tyrrells"], rel=["KP Snacks"]),
 B("Patatas Torres", "Spain", "1969", "Premium crisps", "Montmeló (Barcelona) maker of handcrafted potato and vegetable crisps.", "https://www.potatopro.com/node/170804", lines=["Torres", "Selecta"], sig=["Torres"]),
 B("Tayto", "Ireland", "1954", "Crisps", "Irish crisp maker founded by Joe Murphy, inventor of seasoned crisps; owned by Intersnack.", "Tayto_(Republic_of_Ireland)", eras=["Joe Murphy, from 1954", "Intersnack"], sig=["Tayto cheese and onion"], rel=["Intersnack"]),
 B("Tayto Group", "United Kingdom", "", "Crisps", "Tandragee, Northern Ireland snack maker, owner of Golden Wonder, Ringos and Mr. Porky.", "Tayto_(Northern_Ireland)", lines=["Tayto", "Golden Wonder", "Ringos", "Mr. Porky", "Real Crisps", "Jonathan Crisp"], rel=["Golden Wonder"]),
 B("Smiths", "United Kingdom", "1920", "Crisps", "First British bagged-crisp brand, founded by Frank Smith and Jim Viney; now a PepsiCo brand.", "Smiths_(snack_foods)", sig=["Smiths crisps", "Quavers", "Monster Munch", "Twisties"], rel=["Walkers"]),
 B("Golden Wonder", "United Kingdom", "1947", "Crisps", "British crisp maker that led the market in the 1960s; owned by Tayto Group since 2006.", "Golden_Wonder", lines=["Golden Wonder", "Ringos", "Transform-A-Snack"], sig=["Golden Wonder", "Wotsits"], rel=["Tayto Group"]),
 B("KP Snacks", "United Kingdom", "1853", "Snacks and nuts", "Rotherham-born snack maker ('Kenyon Produce'), owned by Intersnack since 2012.", "KP_Snacks", lines=["KP Nuts", "Hula Hoops", "McCoy's", "Tyrrells", "Skips", "Butterkist"], sig=["Hula Hoops", "McCoy's", "Skips"], rel=["Intersnack", "Tyrrells"]),
 B("Intersnack", "Germany", "1968", "Savoury snacks", "Düsseldorf snack group, part of Pfeifer & Langen.", "Intersnack", lines=["funny-frisch", "Chio", "Pom-Bear", "Vico", "ültje", "Tayto"], sig=["Pom-Bear"], rel=["KP Snacks", "Tayto"]),
 B("Calbee", "Japan", "1949", "Snacks", "Hiroshima-founded snack maker with about 70% of Japan's potato chip market.", "Calbee", lines=["Calbee Potato Chips", "Kappa Ebisen", "Jagariko", "Jagabee", "Frugra"], sig=["Calbee Potato Chips", "Kappa Ebisen"]),
 B("Kameda Seika", "Japan", "", "Rice crackers", "Japan's leading rice-cracker maker, with about 30% of the domestic market.", "https://kamedaseika.co.jp/en/company/rice-cracker-business", lines=["Kaki-no-Tane", "Happy Turn", "Potapota Yaki", "Usuyaki"], sig=["Kaki no tane", "Happy Turn"]),
 B("Want Want", "Taiwan", "", "Rice crackers and snacks", "Taiwan's largest rice-cracker maker, with over 100 plants in China.", "Want_Want", sig=["Want Want rice crackers"]),
 B("Tao Kae Noi", "Thailand", "2004", "Seaweed snacks", "Thai crispy-seaweed snack maker founded by Itthipat Peeradechapan.", "Tao_Kae_Noi", sig=["Tao Kae Noi"]),
 B("Haldiram's", "India", "1937", "Namkeen and sweets", "Bikaner-founded maker of packaged Indian snacks and sweets, now based in Nagpur.", "Haldiram%27s", rel=["Bikanervala"]),
]

trads = [
 {"n": "Bikaneri bhujia", "g": "Food & drink", "r": "Bikaner, Rajasthan, India", "p": "", "d": "Crisp spiced noodle snack made as a cottage industry around Bikaner.",
  "tech": "dough of moth-bean and gram flour with spices pressed into fine strands and deep-fried", "mat": "Vigna aconitifolia (moth bean), gram flour, spices",
  "forms": ["Bikaneri bhujia"], "ctr": ["Bikaner"], "auth": "light yellow, crunchier and more strongly flavoured than sev; made in Bikaner", "s": W + "Bikaneri_bhujia"},
 {"n": "Sōka senbei", "g": "Food & drink", "r": "Sōka, Saitama, Japan", "p": "Edo period–present", "d": "Salty soy-glazed rice crackers popularised from a Sōka teahouse.",
  "tech": "rice crackers baked and brushed with soy sauce", "mat": "non-glutinous rice, soy sauce",
  "forms": ["Senbei"], "ctr": ["Sōka"], "auth": "", "s": W + "Senbei"},
 {"n": "Southern German lye pretzel", "g": "Food & drink", "r": "Bavaria and Swabia, Germany", "p": "", "d": "Knotted soft pretzels dipped in lye before baking.",
  "tech": "dough twisted into the pretzel loop, dipped in lye or washing soda, salted and baked", "mat": "wheat dough, lye, coarse salt",
  "forms": ["Laugenbrezel"], "ctr": ["Bavaria", "Swabia"], "auth": "Bavarian: thick arms, little fat; Swabian: thin arms, split fat belly", "s": W + "Pretzel"},
]

notes = ("No old data for this shelf; all 12 planned kinds are new and sourced. Vegetable crisps folded into Potato crisps (type + Terra Chips archetype). "
 "Quavers and Hula Hoops (potato-based shapes) placed under Extruded corn snack. Frito-Lay, Barcel, Osem, Nongshim, Glico, General Mills, Wise Foods and Frito-Lay-owned brands are archetype makers without register pages (no page fetched for the company). "
 "Left out: Propercorn, Jagariko as an archetype, Santitas, chivda, Kameda Seika founding year (pages missing or unconfirmed); Namkeen Wikipedia page is a film, so Bombay mix page used; no brand lists for pork scratchings beyond Mr. Porky (none on retrieved pages). "
 "Seaweed and namkeen brands kept minimal for lack of retrieved pages. Wikidata not used.")

out = {"kinds": kinds, "brands": brands, "traditions": trads, "notes": notes}
p = 'work/J8/shelves/04_00.json'; tmp = p + '.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1); os.replace(tmp, p)
print(len(kinds), sum(len(k['x']) for k in kinds), len(brands), len(trads))
