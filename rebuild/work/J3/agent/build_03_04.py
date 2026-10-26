import json, os
W = 'https://en.wikipedia.org/wiki/'
NYD = 'https://www.nealsyarddairy.co.uk/products/'
SF = 'https://www.slowfood.org.uk/ark-producer/james-montgomery-montgomerys-cheddar-artisan-somerset-cheddar/'
CP = 'https://www.cheeseprofessor.com/blog/somerset-cheddar-cheesemakers'
MART = 'https://www.charlesmartell.com/farm/history/'
VELLA = 'https://www.vellacheese.com/dry-jack.php'
STAFF = 'https://assets.publishing.service.gov.uk/media/604b66eae90e07153e493fde/product_specification_Staffordshire_Cheese..pdf'


def A(n, d, s, mk="", y="", a="", v=None, dt=""):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or []}
    if dt: x["dt"] = dt
    return x


def V(n, mk="", y="", d=""):
    o = {"n": n}
    if mk: o["mk"] = mk
    if y: o["y"] = y
    if d: o["d"] = d
    return o


cheddar = {"n": "Cheddar", "a": "farmhouse cheddar · clothbound cheddar · block cheddar",
 "d": "Hard pressed cow's-milk cheese made by cheddaring the curd, from Cheddar in Somerset and now made worldwide, mild to vintage by age.",
 "t": ["mild", "medium", "mature", "extra mature", "vintage", "clothbound (larded cloth)", "block / rindless", "white or coloured (annatto)", "smoked", "raw or pasteurised milk"],
 "s": "https://kerrygold.com/products/",
 "x": [
  A("West Country Farmhouse Cheddar PDO", "Cheddar made from local milk in Somerset, Dorset, Devon and Cornwall by traditional methods; the protected reference cheddar.",
    W + "Cheddar_cheese", y="PDO 2007", a="West Country Farmhouse Cheddar Cheese",
    v=[V("West Country Farmhouse Cheddar Cheese UK PDO", d="Protected name (old data).")],
    dt="Somerset, Dorset, Devon, Cornwall milk · traditional methods · mild to vintage · clothbound or block"),
  A("Artisan Somerset Cheddar", "Raw-milk, cloth-bound Somerset cheddar aged at least a year, made by three farms under a Slow Food presidium.",
    SF, y="presidium 2004", a="Slow Food Somerset Cheddar presidium",
    v=[V("Montgomery's Cheddar", "Montgomery's", "farm bought 1911", "North Cadbury; unpasteurised organic milk from about 200 Friesians; 12-month and 18-month extra-matured, plus smoked."),
       V("Keen's Cheddar", "Keen's", "1899", "Moorhayes Farm, Wincanton; unpasteurised mature and extra mature, plus a pasteurised Somerset cheddar."),
       V("Westcombe Cheddar", "Westcombe Dairy", "1999", "Evercreech; clothbound with lard, about 12–14 months; clothbound making restored by Richard Calver.")],
    dt="raw milk · cloth-bound · at least 12 months · selected and sold by Neal's Yard Dairy among others"),
  A("Clothbound farmhouse cheddar", "Traditional cheddar bound in larded cloth so it breathes as it matures, made by farms outside the presidium in Britain and America.",
    W + "Cheddar_cheese",
    v=[V("Quicke's Clothbound Cheddar", "Quicke's", d="Home Farm, Newton St Cyres, Devon; Buttery, Mature and Vintage (two years)."),
       V("Pitchfork Cheddar", "Trethowan's Dairy", "2019", "Organic Somerset cheddar from the Trethowan brothers' own herd."),
       V("Cabot Clothbound", "Cabot Creamery", d="Bandaged natural-rind cheddar matured by the Cellars at Jasper Hill, Vermont."),
       V("Stockinghall", "Murray's Cheese", d="Old data.")],
    dt="cloth and lard binding · natural rind · 12–24 months"),
  A("Isle of Mull Cheddar", "Very sharp white unpasteurised cheddar from the Isle of Mull, sometimes with blue veining.",
    W + "Isle_of_Mull_Cheddar", a="Isle of Mull",
    dt="raw milk · white · sharp · occasional blue vein"),
  A("Orkney Scottish Island Cheddar PGI", "Protected Orkney cheddar made by traditional methods passed down since 1946.",
    W + "Cheddar_cheese", y="PGI 2013",
    v=[V("Orkney Scottish Island Cheddar PGI", d="Protected name (old data).")],
    dt="Orkney milk · block · mild to mature"),
  A("Creamery block cheddar", "Large-scale cheddar matured in vacuum-packed blocks and sold by strength under national brands.",
    W + "Cheddar_cheese",
    v=[V("Cathedral City", "Cathedral City", d="Made by Saputo Dairy UK at Davidstow, Cornwall."),
       V("Davidstow Cheddar", "Saputo Dairy UK", d="Made at Davidstow Creamery, Cornwall."),
       V("Kerrygold Aged Cheddar", "Kerrygold", d="Irish grass-fed pasteurised cheddar aged about a year; also Sharp, Extra Sharp White and Reserve."),
       V("Cabot Private Stock Cheddar", "Cabot Creamery", d="Vermont cheddar aged 16 months."),
       V("Seriously Strong Cheddar", d="Old data."),
       V("Pilgrims Choice", d="Brand of Ornua."),
       V("Anchor cheddar", d="New Zealand blocks matured a further year in the UK.")],
    dt="block or pre-pack · mild, medium, mature, extra mature, vintage · white or coloured"),
  A("Applewood", "Smoke-flavoured round cheddar made in Somerset.", W + "Applewood_cheese",
    mk="", a="Applewood smoked cheddar",
    v=[V("Applewood", "Norseland", d="Formerly Ilchester Cheese Company.")],
    dt="round · smoke flavour"),
  A("Dunlop", "Mild 'sweet-milk' cheese from Dunlop, Ayrshire, resembling a soft cheddar.", W + "Dunlop_cheese",
    dt="mild · softer than cheddar · Ayrshire"),
 ],
 "m": [["Béal Handmade Mature Organic Cheddar", "Béal Organic Cheese"], ["Coolattin Mature Cheddar", "Coolattin Cheddar"],
       ["Cahill's Vintage Cheddar", "Cahill's Farm Cheese"], ["Ballinwood Smoked Cheddar", "Cahill's Farm Cheese"],
       ["Hegarty's Cheddar", "Hegarty Cheese"], ["Bay Lough Cheddar", "Bay Lough Cheese"], ["Fivemiletown Cheddar", "Fivemiletown Creamery"],
       ["Dale End Cheddar", "Botton Village Creamery"], ["Leonard Stanley Cheddar", "Godsells Cheese"],
       ["Wookey Hole Cave Aged Cheddar", ""], ["Street Ched Aged Cheddar", "Urban Stead Cheese"],
       ["Akshayakalpa Organic Cheddar Cheese", "Akshayakalpa Organic"], ["Kodai Red Chilli Cheddar", "Kodai Cheese"],
       ["Ode to Chennai Cheddar", "Käse Fromagerie"], ["Kotmale Cheddar Cheese", "Cargills Quality Dairies (Kotmale)"],
       ["Sangha Cheddar", "Maeil Dairies"], ["KCC Rindless Cheddar Cheese", "New Kenya Co-operative Creameries (New KCC)"],
       ["Bonnita Cheddar Loaves", "Lactalis South Africa (formerly Parmalat SA)"], ["Pınar Cheddar Cheese Slices", "Pınar Süt Ürünleri"]]}

cheshire = {"n": "Cheshire", "a": "Cheshire cheese",
 "d": "Dense, crumbly, slightly salty pressed cow's-milk cheese from Cheshire and neighbouring counties, white, red or blue.",
 "t": ["white", "red (annatto)", "blue", "clothbound or waxed"],
 "s": "https://www.trolley.co.uk/product/waitrose-crumbly-cheshire-cheese-s2/HSK730",
 "x": [A("Appleby's Cheshire", "Raw-milk, clothbound farmhouse Cheshire from Hawkstone Abbey Farm; one of the last of its kind.",
         NYD + "applebys-cheshire", mk="Appleby's", y="1952",
         dt="raw cow's milk · clothbound · about 3 months")]}

lancashire = {"n": "Lancashire", "a": "Lancashire cheese",
 "d": "Crumbly or creamy pressed cow's-milk cheese from Lancashire, traditionally made by mixing curds of more than one day.",
 "t": ["Creamy (4–12 weeks)", "Tasty (12 weeks–24 months)", "Crumbly (single-day curd)"],
 "s": "https://www.mousetrapcheese.co.uk/products/lancashire-cheese-kirkhams-traditional-tasty-lancashire-cheese",
 "x": [A("Beacon Fell Traditional Lancashire PDO", "Traditional mixed-curd Lancashire made north of the River Ribble by the designated method.",
         W + "Lancashire_cheese", y="Gornall method 1890s", a="Traditional Lancashire",
         v=[V("Creamy Lancashire", d="Young, 4–12 weeks; fluffy, for toasting."),
            V("Tasty Lancashire", d="Matured 12 weeks to 24 months; nutty."),
            V("Beacon Fell Traditional Lancashire Cheese UK PDO", d="Protected name (old data).")],
         dt="two or three days' curds · 1–24 months"),
       A("Kirkham's Lancashire", "Raw-milk farmhouse Lancashire from Beesley Farm, Goosnargh, made by the third generation of the Kirkham family.",
         NYD + "kirkhams-lancashire", mk="Kirkham's",
         v=[V("Kirkham's Tasty Lancashire", "Kirkham's", d="Old data."),
            V("Mature Kirkham's Lancashire", "Kirkham's", d="Selected cheeses matured about 9–12 months.")],
         dt="raw milk · several days' curds · lard-bound · 3–4 months"),
       A("Crumbly Lancashire", "Faster single-day-curd Lancashire created in the 1950s for mass production.",
         W + "Lancashire_cheese", y="1950s", a="Lancashire Crumbly", dt="6–8 weeks · block")]}

wensleydale = {"n": "Wensleydale", "a": "",
 "d": "Crumbly, moist, mild pressed cow's-milk cheese of the Wensleydale type; Wensleydale Blue is under blue cheese.",
 "t": ["plain", "with cranberries"],
 "s": "https://www.trolley.co.uk/product/wensleydale-creamery-wensleydale-cheese/AGV431",
 "x": [A("Yorkshire Wensleydale PGI", "Wensleydale made in the dale itself, chiefly by the creamery at Hawes; protected since 2013.",
         W + "Wensleydale_cheese", mk="Wensleydale Creamery", y="PGI 2013",
         v=[V("Yorkshire Wensleydale", "Wensleydale Creamery", d="Old data."),
            V("Yorkshire Wensleydale UK PGI", d="Protected name (old data)."),
            V("Wensleydale with cranberries", d="Widely sold fruited version.")],
         dt="supple, crumbly · slight honey aroma · plain or fruited")]}

redl = {"n": "Red Leicester", "a": "Leicester · Leicestershire cheese",
 "d": "Cheddar-like but more crumbly cow's-milk cheese coloured orange with annatto, typically aged 6 to 12 months.",
 "t": ["cloth-matured wheel", "block", "mild", "mature"],
 "s": W + "Red_Leicester",
 "x": [A("Sparkenhoe Red Leicester", "England's only unpasteurised Red Leicester, bound in muslin and matured on beech shelves.",
         "https://www.leicestershirecheese.co.uk/product-page/sparkenhoe-red-leicester", mk="Leicestershire Handmade Cheese Co",
         dt="raw milk · muslin cloth · about 6 months")]}

glos = {"n": "Gloucester", "a": "Double Gloucester · Single Gloucester",
 "d": "Smooth, firm pressed cow's-milk cheese of Gloucestershire, Double (full milk, longer aged, often coloured) or Single (part-skimmed, crumbly).",
 "t": ["Single", "Double", "coloured or natural"],
 "s": "https://www.trolley.co.uk/product/tesco-double-gloucester-cheese/RQH563",
 "x": [A("Single Gloucester PDO", "Lighter, crumbly, lower-fat Gloucester made only on Gloucestershire farms with Gloucester cows.",
         W + "Gloucester_cheese", mk="Charles Martell & Son", y="revived 1978; PDO 1997",
         v=[V("Single Gloucester", "Charles Martell & Son", "1978", "Revived at Hunts Court, Dymock, from Old Gloucester milk."),
            V("Single Gloucester UK PDO", d="Protected name (old data).")],
         dt="Gloucester cattle · natural rind · young"),
       A("Double Gloucester", "Larger, longer-aged Gloucester with a stronger savoury flavour, coloured yellow; used for Cooper's Hill cheese-rolling.",
         W + "Gloucester_cheese",
         v=[V("Double Gloucester", "Charles Martell & Son", d="From Old Gloucester cows' milk.")],
         dt="natural rind or block · coloured · firmer")]}

caer = {"n": "Caerphilly", "a": "Caerffili",
 "d": "Moist, crumbly, lightly pressed cow's-milk cheese of Welsh origin, young and mild or ripened with a soft rim.",
 "t": ["young (2 weeks)", "ripened with rind (2–4 months)"],
 "s": "https://thecheeselady.co.uk/product/gorwydd-caerphilly/",
 "x": [A("Traditional Welsh Caerphilly PGI", "Caerphilly made in Wales by the pre-war farmhouse method.", W + "Caerphilly_cheese",
         a="Traditional Welsh Caerffili",
         v=[V("Traditional Welsh Caerphilly UK PGI", d="Protected name (old data)."),
            V("Cenarth Caerphilly", "Cenarth Cheese", "1980s", "Farmhouse revival by Thelma Adams."),
            V("Castle Dairies Caerphilly", "Castle Dairies", "late 1990s", "Made in Caerphilly town by hand.")],
         dt="up to ten weeks · moist, crumbly"),
       A("Gorwydd Caerphilly", "Ripened farmhouse Caerphilly with an edible rind and creamy, mushroomy breakdown, first made at Gorwydd Farm, Tregaron.",
         NYD + "gorwydd-caerphilly", mk="Trethowan's Dairy",
         v=[V("Gorwydd Caerphilly", "Trethowan's Dairy", "2014", "Made at Puxton Farm, Somerset, since 2014.")],
         dt="pasteurised cow's milk · natural rind · 2–4 months")]}

derby = {"n": "Derby & Sage Derby", "a": "Derby cheese · Sage Derby",
 "d": "Mild, semi-firm Derbyshire cow's-milk cheese, softer than cheddar, often marbled green with sage.",
 "t": ["plain", "sage", "port wine"],
 "s": W + "Derby_cheese",
 "x": [A("Sage Derby", "Derby marbled green with sage, or with green curd and sage extract, aged one to three months.",
         W + "Sage_Derby", dt="sage leaves or green curd · 1–3 months")]}

colby = {"n": "Colby", "a": "",
 "d": "Mild, moist, washed-curd semi-hard cheese of the American type, often orange.",
 "t": ["longhorn", "block", "Colby-Jack marble"],
 "s": "https://cheesegrotto.com/products/widmers-cheese-cellars-natural-colby-cheese",
 "x": [A("Washed-curd longhorn Colby", "Traditional Colby from Colby, Wisconsin, whose curd is washed with cold water and pressed into a longhorn cylinder.",
         W + "Colby_cheese", y="1885", a="Colby longhorn",
         v=[V("Colby", d="Developed by Joseph Steinwand at his family's factory near Colby, Wisconsin.")],
         dt="longhorn · open texture with irregular holes"),
       A("Colby-Jack", "Marbled cheese of mixed Colby and Monterey Jack curds.", W + "Colby_cheese",
         dt="orange and white marble")]}

jack = {"n": "Monterey Jack", "a": "Jack",
 "d": "Mild, pale, semi-hard Californian cow's-milk cheese, aged to Dry Jack.",
 "t": ["young (about 1 month)", "pepper", "cheddar-Jack marble"],
 "s": "https://stopandshop.com/groceries/product/cabot-creamery-natural-monterey-jack-cheese-block-8-oz-pkg/35403",
 "x": [A("Monterey Jack", "White, mild, slightly sweet cheese from Monterey, sold commercially by David Jacks.", W + "Monterey_Jack",
         y="19th century", dt="about one month · melting cheese"),
       A("Dry Jack", "Hard, long-aged Jack rubbed with cocoa, pepper and oil; first found as forgotten aged wheels in 1915.",
         VELLA, mk="Vella Cheese Company", y="1915", a="Dry Monterey Jack",
         v=[V("Mezzo Secco", "Vella Cheese Company", d="Partially dry Jack, 5–7 months."),
            V("Dry Monterey Jack", "Vella Cheese Company", d="7–10 months."),
            V("Special Select Dry Jack", "Vella Cheese Company", d="1–2 years."),
            V("Golden Bear", "Vella Cheese Company", d="2–4 years."),
            V("Oro Secco", "Vella Cheese Company", d="Longer-aged Mezzo Secco, 2–4 years."),
            V("Habanero Dry Monterey Jack", "Vella Cheese Company", d="About a year, with habanero.")],
         dt="cocoa, pepper and canola-oil rind · quarter, half or whole wheel"),
       A("Pepper Jack", "Monterey Jack flavoured with chilli and bell peppers and herbs.", W + "Monterey_Jack",
         dt="chilli and bell peppers · herbs")]}

brit = {"n": "British farmhouse hard cheese", "a": "regional British hard cheese",
 "d": "Revived or new British pressed hard cheeses that are not one of the classic territorials.",
 "s": W + "Swaledale_cheese",
 "x": [A("Staffordshire Cheese PDO", "Cloth-bound cylindrical cheese from Staffordshire milk and cream, revived from a recipe linked to Leek's Cistercian monks.",
         STAFF, mk="", y="13th century origin; revived",
         v=[V("Staffordshire Cheese", "Staffordshire Cheese Company", d="Leek, Staffordshire.")],
         dt="8–10 kg cylinder · muslin cloth · 2–4 weeks up to 12 months"),
       A("Swaledale", "Full-fat hard cheese from Richmond in Swaledale, made from cow's, sheep's or goat's milk.", W + "Swaledale_cheese",
         dt="cow, ewe or goat"),
       A("Teviotdale", "Full-fat hard Jersey-milk cheese of the Scottish–English border; no known current producer.", W + "Teviotdale_cheese",
         dt="Jersey milk"),
       A("Cornish Kern", "Alpine-style Cornish cheese made with Alpine starters and scalded curd, often compared to Gruyère.",
         NYD + "cornish-kern", mk="Lynher Dairies",
         dt="pasteurised Ayrshire milk · Alpine cultures · 16–24 months")]}

kinds = [cheddar, cheshire, lancashire, wensleydale, redl, glos, caer, derby, colby, jack, brit]

brands = [
 {"n": "Montgomery's", "c": "United Kingdom", "f": "1911", "seg": "farmhouse cheddar", "d": "Montgomery family farm at North and South Cadbury, Somerset, making raw-milk clothbound cheddar.",
  "lines": ["Montgomery's Cheddar 12 month", "18-month extra matured", "smoked"], "sig": ["Artisan Somerset Cheddar"], "rel": ["Keen's", "Westcombe Dairy", "Neal's Yard Dairy"], "s": SF},
 {"n": "Keen's", "c": "United Kingdom", "f": "1899", "seg": "farmhouse cheddar", "d": "Keen family cheddar made at Moorhayes Farm, Wincanton, for five generations.",
  "lines": ["Unpasteurised Mature", "Extra Mature", "Pasteurised Somerset Cheddar", "Wedding wheels"], "sig": ["Artisan Somerset Cheddar"], "rel": ["Montgomery's", "Westcombe Dairy"], "s": "https://www.keenscheddar.co.uk/"},
 {"n": "Westcombe Dairy", "c": "United Kingdom", "f": "", "seg": "farmhouse cheddar", "d": "Calver family dairy at Evercreech, Somerset, making clothbound cheddar since 1999 on a farm making cheddar since the late 19th century.",
  "sig": ["Artisan Somerset Cheddar"], "rel": ["Montgomery's", "Keen's"], "s": NYD + "westcombe-cheddar"},
 {"n": "Quicke's", "c": "United Kingdom", "f": "", "seg": "farmhouse cheddar", "d": "Devon farm at Home Farm, Newton St Cyres, making clothbound cheddars.",
  "lines": ["Buttery", "Mature Clothbound", "Vintage Clothbound"], "sig": ["Clothbound farmhouse cheddar"], "s": "https://www.quickes.co.uk/"},
 {"n": "Neal's Yard Dairy", "c": "United Kingdom", "f": "1979", "seg": "cheesemonger and affineur", "d": "London retailer, wholesaler and affineur of British and Irish farmhouse cheese founded by Nicholas Saunders and Randolph Hodgson.",
  "rel": ["Montgomery's", "Keen's", "Westcombe Dairy", "Appleby's", "Kirkham's"], "s": W + "Neal%27s_Yard_Dairy"},
 {"n": "Cabot Creamery", "c": "United States", "f": "", "seg": "dairy cooperative", "d": "Vermont dairy cooperative owned by Agri-Mark, known for cheddar.",
  "lines": ["Cabot Clothbound", "Private Stock Cheddar"], "sig": ["Clothbound farmhouse cheddar", "Creamery block cheddar"], "s": W + "Cabot_Creamery"},
 {"n": "Cathedral City", "c": "United Kingdom", "f": "", "seg": "mass-market cheddar", "d": "British cheddar brand made by Saputo Dairy UK in Cornwall, named after Wells Cathedral.",
  "sig": ["Creamery block cheddar"], "s": W + "Cathedral_City_Cheddar"},
 {"n": "Kerrygold", "c": "Ireland", "f": "", "seg": "dairy brand", "d": "Irish butter and cheese brand owned by the Ornua cooperative.",
  "lines": ["Aged Cheddar", "Sharp Cheddar", "Extra Sharp White Cheddar", "Reserve Cheddar", "Dubliner"], "sig": ["Creamery block cheddar"], "s": W + "Ornua"},
 {"n": "Wensleydale Creamery", "c": "United Kingdom", "f": "1897", "seg": "creamery", "d": "Creamery at Hawes, North Yorkshire, making Yorkshire Wensleydale; a Saputo subsidiary.",
  "sig": ["Yorkshire Wensleydale PGI"], "s": W + "Wensleydale_Creamery"},
 {"n": "Appleby's", "c": "United Kingdom", "f": "1952", "seg": "farmhouse cheese", "d": "Appleby family making raw-milk clothbound Cheshire at Hawkstone Abbey Farm.",
  "sig": ["Appleby's Cheshire"], "rel": ["Neal's Yard Dairy"], "s": NYD + "applebys-cheshire"},
 {"n": "Kirkham's", "c": "United Kingdom", "f": "", "seg": "farmhouse cheese", "d": "Kirkham family making raw-milk Lancashire at Beesley Farm, Goosnargh.",
  "sig": ["Kirkham's Lancashire"], "rel": ["Neal's Yard Dairy"], "s": NYD + "kirkhams-lancashire"},
 {"n": "Trethowan's Dairy", "c": "United Kingdom", "f": "", "seg": "farmhouse cheese", "d": "Brothers Todd and Maugan Trethowan, makers of Gorwydd Caerphilly and Pitchfork Cheddar, in Somerset since 2014.",
  "lines": ["Gorwydd Caerphilly", "Pitchfork Cheddar"], "sig": ["Gorwydd Caerphilly"], "s": NYD + "gorwydd-caerphilly"},
 {"n": "Leicestershire Handmade Cheese Co", "c": "United Kingdom", "f": "", "seg": "farmhouse cheese", "d": "Maker of Sparkenhoe raw-milk Red Leicester at Sparkenhoe Farm, Upton.",
  "sig": ["Sparkenhoe Red Leicester"], "s": "https://www.leicestershirecheese.co.uk/product-page/sparkenhoe-red-leicester"},
 {"n": "Charles Martell & Son", "c": "United Kingdom", "f": "1972", "seg": "farmhouse cheese", "d": "Hunts Court Farm, Dymock, cheesemakers who revived Single Gloucester and make Stinking Bishop from Old Gloucester milk.",
  "lines": ["Single Gloucester", "Double Gloucester", "Stinking Bishop", "Double Berkeley"], "sig": ["Single Gloucester PDO"], "s": MART},
 {"n": "Vella Cheese Company", "c": "United States", "f": "1931", "seg": "artisan cheese", "d": "Sonoma, California, maker of hand-made Dry Monterey Jack.",
  "lines": ["Mezzo Secco", "Dry Monterey Jack", "Special Select", "Golden Bear", "Oro Secco"], "sig": ["Dry Jack"], "s": VELLA},
 {"n": "Lynher Dairies", "c": "United Kingdom", "f": "", "seg": "farmhouse cheese", "d": "Cornish dairy at Ponsanooth led by Catherine Mead, maker of Cornish Kern.",
  "sig": ["Cornish Kern"], "s": NYD + "cornish-kern"},
]

trads = [
 {"n": "Somerset clothbound cheddar", "g": "Food & drink", "r": "Somerset, England", "p": "19th century to present",
  "d": "Farmhouse cheddar made from the farm's own raw milk, cheddared by hand, bound in cloth and aged at least a year.",
  "tech": "cheddaring by hand, cloth binding, long cellar ageing", "mat": "raw cow's milk, rennet, cloth, lard",
  "forms": ["Cheddar"], "ctr": ["Montgomery's, North Cadbury", "Keen's, Moorhayes Farm", "Westcombe Dairy, Evercreech"],
  "auth": "Raw milk, cloth-bound natural rind, maker's farm name; Slow Food presidium members.", "s": SF},
]

notes = ("Kept all 8 old kinds; added Red Leicester and Derby & Sage Derby, plus a NEW kind 'British farmhouse hard cheese' holding "
         "Staffordshire PDO, Swaledale, Teviotdale and Cornish Kern pulled from the old tomme catch-all (Tomme shelf should drop them). "
         "Cheddar flat list trimmed from 33 to 19 m (duplicates Coolattin Mature, Keens Cheddar, West Country PDO dupes, Béal Mild, Hegarty Smoked removed); "
         "PDO/PGI and brand models became archetype versions. Left out: Montgomery's ageing details beyond Slow Food page; Orkney maker name; "
         "Dunlop and Isle of Mull makers (not on retrieved pages); Cheshire white/red/blue only as types; Port wine Derby only as a type; "
         "Hartington/other Derby makers not confirmed; NYD Keen's and Montgomery's product pages returned 404.")

out = {"kinds": kinds, "brands": brands, "traditions": trads, "notes": notes}
p = 'work/J3/shelves/03_04.json'
open(p + '.tmp', 'w').write(json.dumps(out, ensure_ascii=False, indent=1))
os.replace(p + '.tmp', p)
print('written', os.path.getsize(p))
