import json, os
W='https://en.wikipedia.org/wiki/'
STUVH='https://www.stuv.com/en/entreprise/history'
STUVP='https://www.v2com-newswire.com/en/newsroom/categories/product-design/press-kits/1564-04/stuv-america-inaugurates-canada-s-largest-stuv-studio'
FOCUS='https://focus-creation.com/en/histoire.php'
kinds=[
{"n":"Wood-burning stove","a":"Log burner · wood burner · multi-fuel stove · flued stove",
 "d":"Closed metal firebox burning wood or other solid fuel, vented through a flue and set on a hearth.",
 "t":["wood only","multi-fuel","catalytic","non-catalytic","boiler stove (back boiler)","with cooking plate","soapstone heat storage","cast iron","steel"],
 "s":"https://www.stovax.com/products/stoves/traditional/wood-stoves-multi-fuel-stoves",
 "x":[
  {"n":"Franklin stove","a":"Pennsylvania fireplace · circulating stove","d":"Metal-lined fireplace with a hollow rear baffle that passes heat into the room; the name stuck to later open-fronted stoves.","mk":"","y":"1742","s":W+"Franklin_stove",
   "v":[{"n":"Pennsylvania fireplace","mk":"Benjamin Franklin","y":"1742","d":"original design"},{"n":"Rittenhouse improved version","mk":"David Rittenhouse","y":"","d":"fixed the weak draught; became the popular form"}],"dt":"cast iron · open or doored front"},
  {"n":"Potbelly stove","a":"","d":"Cylindrical cast-iron stove bulging in the middle, burning coal or wood, with a flat top for cooking.","mk":"","y":"by 1906","s":W+"Potbelly_stove","v":[],"dt":"cast iron · coal or wood"},
  {"n":"Jøtul F 602","a":"Jøtul 602","d":"Small cast-iron box stove with a cooking plate and relief decoration; over two million sold.","mk":"Jøtul","y":"1940","s":"https://www.jotul.com/guides-and-inspiration/jotul-f-602-eco-small-wood-burning-stove-great-personality",
   "v":[{"n":"F 602 (original)","mk":"Jøtul","y":"1940","d":"designed by architects Blakstad and Munthe-Kaas, relief by sculptor Ørnulf Bast"},{"n":"F 602 ECO","mk":"Jøtul","y":"","d":"current cleaner-burning version"}],"dt":"cast iron · black paint or enamel · one or two cooking plates"},
  {"n":"Morsø squirrel stove","a":"Morsø 1400 series · Squirrel","d":"Small radiant cast-iron stove with Morsø's squirrel relief cast on both sides.","mk":"Morsø","y":"","s":"https://morsoe.com/en/product/indoor/multifuel/p1410_uk",
   "v":[{"n":"Morsø 1410","mk":"Morsø","y":"1984–1990","d":"multi-fuel version, 70 kg, since discontinued in this form"}],"dt":"cast iron · wood, briquettes, smokeless fuel"},
  {"n":"Stûv 30","a":"","d":"Wood stove that can be run closed, open or as a grill: three operating modes.","mk":"Stûv","y":"2000–2006","s":STUVH,
   "v":[{"n":"30-compact","mk":"Stûv","y":"","d":"smaller model"},{"n":"30-compact H","mk":"Stûv","y":"","d":"compact on a high base"}],"dt":"steel · pedestal or wall-mounted"},
  {"n":"Stûv 16","a":"","d":"Minimal steel stove family with a large frameless glass door and outside-air option.","mk":"Stûv","y":"","s":STUVP,
   "v":[{"n":"16-H","mk":"Stûv","y":"","d":"on a high base"},{"n":"16-cube","mk":"Stûv","y":"","d":"cubic stove"}],"dt":"steel · log length by model"},
  {"n":"RAIS 1","a":"The Original","d":"RAIS's first stove, drawn by architect Bent Falk during the 1970s oil crisis.","mk":"RAIS","y":"early 1970s","s":"https://madegooddesigns.com/rais-brand-guidelines/","v":[],"dt":"steel"}],
 "m":[["Athos","Stovax"],["County","Stovax"],["Huntingdon","Stovax"],["Olympus","Stovax"],["Viva L","RAIS"],["Q-Tee","RAIS"],["Juno L","RAIS"],["Scan 85","Scan"],["Scan 83","Scan"],["Scan 68","Scan"],["Scan 66","Scan"],["3110","HWAM"],["5580","HWAM"],["5440C","HWAM"],["Skye E700","Charnwood"]]},
{"n":"Inset and wall-hung fire","a":"Fireplace insert · inset fire · hole-in-the-wall fire · suspended fire · flued fire",
 "d":"Fire built into a fireplace opening, wall or ceiling and vented through a flue; any fuel.",
 "t":["wood insert","gas inset (conventional flue)","balanced-flue gas","electric inset","wall-hung","suspended","retractable door","double-sided"],
 "s":"https://www.valor.co.uk/valor-inset-gas-fires",
 "x":[
  {"n":"Gyrofocus","a":"","d":"Steel fireplace hung from the ceiling, detached from the wall, with a hearth that turns 360°.","mk":"Focus","y":"1968","s":FOCUS,
   "v":[{"n":"Gyrofocus (open wood)","mk":"Focus","y":"1968","d":"original by Dominique Imbert"},{"n":"Gas Gyrofocus","mk":"Focus","y":"2020","d":"gas version keeping the pivoting hearth"},{"n":"Wood Gyrofocus (closed)","mk":"Focus","y":"2021","d":"closed version meeting Ecodesign"}],"dt":"black steel · suspended · wood, gas"},
  {"n":"Slimfocus","a":"","d":"Slim streamlined Focus fire; the maker's first balanced-flue fireplace.","mk":"Focus","y":"2014","s":FOCUS,"v":[],"dt":"steel · balanced flue"},
  {"n":"Stûv 21","a":"","d":"Built-in wood fire whose glass door retracts out of sight so it can burn closed or open.","mk":"Stûv","y":"2000–2006","s":STUVH,
   "v":[{"n":"Stûv 20","mk":"Stûv","y":"1990s","d":"predecessor, first fire with a retractable door"},{"n":"Stûv 21-clad","mk":"Stûv","y":"","d":"double-sided free-standing version with rusted cladding"}],"dt":"steel · single or double-sided · retractable door"},
  {"n":"Stûv 6","a":"","d":"Built-in wood fire for small masonry hearths, giving a large view of the fire.","mk":"Stûv","y":"","s":STUVP,"v":[],"dt":"steel · built-in"}],
 "m":[["Dream SL","Valor"],["Seattle Slimline","Valor"],["Trueflame","Valor"],["Homeflame","Valor"],["Valorflame","Valor"],["DSA 4-5","Scan"],["DSA 12","Scan"]]},
{"n":"Pellet stove","a":"Pellet burner","d":"Stove that feeds wood or biomass pellets from a hopper into a burn pot for a steady, controllable flame.",
 "t":["free-standing","fireplace insert","pellet boiler stove (central heating)"],"s":W+"Pellet_stove",
 "m":[["P-10","Stûv"]]},
{"n":"Masonry heater","a":"Masonry stove · cocklestove · tiled stove · tile stove · Kachelofen · kakelugn",
 "d":"Massive brick, tile or stone heater that stores heat from short hot fires in smoke channels and radiates it for hours.",
 "t":["tile-clad","stone or soapstone-clad","rendered (stucco)","metal-clad","with cooking oven","with sleeping bench or berth"],"s":W+"Masonry_heater",
 "x":[
  {"n":"Kachelofen","a":"Tile oven · Steinofen (stone version)","d":"German and Austrian tiled masonry stove built by master potters (Hafnermeister).","mk":"","y":"Renaissance onwards","s":W+"Masonry_heater",
   "v":[{"n":"Schleissheim Palace stove","mk":"Joseph Effner","y":"c. 1720","d":"palace example"}],"dt":"firebrick core · ceramic tile skin"},
  {"n":"Kakelugn","a":"Swedish tile stove","d":"Swedish tall tiled stove associated with the efficiency work of Cronstedt and Wrede.","mk":"","y":"18th century onwards","s":W+"Masonry_heater",
   "v":[{"n":"Rörstrand Art Nouveau stove","mk":"Rörstrand","y":"c. 1900","d":"factory-made tiled stove"}],"dt":"ceramic tile · round or square · glaze and decoration"},
  {"n":"Russian stove","a":"Russian oven","d":"Large brick stove that heats, cooks, bakes and dries, often with a sleeping berth on top.","mk":"","y":"15th century or earlier","s":W+"Russian_oven","v":[],"dt":"brick · about two tonnes · one or two hearths"},
  {"n":"Pönttöuuni","a":"Drum oven · plåtugn","d":"Finnish metal-clad masonry stove: a brick core inside a galvanised sheet-metal drum.","mk":"","y":"1878","s":W+"Masonry_heater",
   "v":[{"n":"Wiman patent","mk":"E. A. Wiman","y":"1878","d":"earliest record, Swedish patent"}],"dt":"brick core · sheet metal · painted or bare"}]},
{"n":"Flueless fire","a":"Ventless fire · bioethanol fire · electric fire",
 "d":"Fire that needs no chimney or flue: bioethanol burners, flueless gas fires and built-in electric fires.",
 "t":["bioethanol – table-top","bioethanol – wall-mounted","bioethanol – free-standing","bioethanol – automatic burner","flueless gas","electric – inset or wall-mounted","electric – mist flame effect"],
 "s":W+"Ethanol_fireplace",
 "x":[
  {"n":"Optiflame","a":"","d":"Electric fire flame effect from Dimplex that simulates a moving flame.","mk":"Dimplex","y":"1988","s":W+"Electric_fireplace",
   "v":[{"n":"Opti-myst","mk":"Dimplex","y":"2008","d":"simulated flames and smoke"},{"n":"Opti-V","mk":"Dimplex","y":"2013","d":"flames with LED logs and crackle sound"}],"dt":"inset, wall-mounted or stove-style casing"}]},
{"n":"Fireplace surround and mantel","a":"Mantelpiece · chimneypiece · fire surround · overmantel",
 "d":"Decorative frame of jambs and shelf around a fireplace opening, sometimes rising to the ceiling.",
 "t":["Georgian","Adam style","Victorian","Gothic revival","Art Deco","French (Louis XIV, Louis XV)","Empire","marble","limestone","granite","carved wood","cast iron","with overmantel"],
 "s":W+"Fireplace_mantel",
 "x":[
  {"n":"Adam-style mantel","a":"Adam chimneypiece","d":"Neoclassical surround after the Adam brothers' late-18th-century designs, in wood with cast ornament; revived a century later.","mk":"","y":"late 18th century","s":W+"Fireplace_mantel","v":[],"dt":"wood with cast ornament · marble"}]}
]
brands=[
{"n":"Jøtul","c":"Norway","f":"1853","seg":"Cast-iron stoves and fireplaces","d":"Norwegian maker of wood heating appliances, from the Kværner foundry; name used since 1920, company name since 1935.","lines":[],"eras":[],"sig":["Jøtul F 602"],"sc":[],"rel":["Scan"],"s":"https://en.wikipedia.org/wiki/J%C3%B8tul"},
{"n":"Morsø","c":"Denmark","f":"1853","seg":"Cast-iron stoves","d":"Morsø Jernstøberi, a Danish foundry founded by N. A. Christensen; stoves since about 1900, royal warrant 1915.","lines":[],"eras":[],"sig":["Morsø squirrel stove"],"sc":[],"rel":[],"s":"https://morsoe.com/en/about-morso/history"},
{"n":"Stûv","c":"Belgium","f":"1983","seg":"Design wood stoves and fires","d":"Belgian maker begun by industrial designer Gérard Pitance and Benoît Lafontaine; known for retractable-door fires.","lines":["Stûv 6","Stûv 16","Stûv 21","Stûv 30","Tulp (gas)"],"eras":["Gérard Pitance, founder-designer, 1983–"],"sig":["Stûv 21","Stûv 30","Stûv 16"],"sc":[],"rel":[],"s":STUVH},
{"n":"Focus","c":"France","f":"1968","seg":"Design fireplaces","d":"French maker of sculptural steel fireplaces founded around Dominique Imbert's Gyrofocus.","lines":[],"eras":["Dominique Imbert, to 2015","Jean-Marc Chalier and Laurent Gaborit, 2015–"],"sig":["Gyrofocus","Slimfocus"],"sc":[],"rel":[],"s":FOCUS},
{"n":"Contura","c":"Sweden","f":"","seg":"Wood stoves","d":"Swedish stove brand of the NIBE group, made in Markaryd, Småland.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Stovax"],"s":"https://www.contura.eu/en-gb/about/contura-from-sweden"},
{"n":"Scan","c":"Denmark","f":"1978","seg":"Wood stoves and inserts","d":"Danish stove maker founded in Odense.","lines":["Scan 66","Scan 68","Scan 83","Scan 85","DSA inserts"],"eras":[],"sig":[],"sc":[],"rel":["Jøtul"],"s":"https://archiup.com/brand/scan-a-s"},
{"n":"RAIS","c":"Denmark","f":"c. 1970","seg":"Design wood stoves","d":"Frederikshavn stove maker whose first model was drawn by architect Bent Falk; owned by Swiss Attika.","lines":["Viva","Q-Tee","Juno"],"eras":[],"sig":["RAIS 1"],"sc":[],"rel":[],"s":"https://madegooddesigns.com/rais-brand-guidelines/"},
{"n":"Charnwood","c":"United Kingdom","f":"1972","seg":"Wood stoves","d":"Isle of Wight stove maker (A. J. Wells & Sons) started by Alfred Wells and sons Alastair and John.","lines":["Skye","Haven"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://www.countrylife.co.uk/promoted/charnwood-homegrown-heroes-244987"},
{"n":"HWAM","c":"Denmark","f":"1973","seg":"Wood stoves","d":"Danish stove maker in Hørning known for its mechanical Autopilot air control; part of the SEGUIN group since 2019.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://www.cheminees-seguin.com/en/brands/hwam/page/2/"},
{"n":"Stovax","c":"United Kingdom","f":"1981","seg":"Wood stoves and fires","d":"Exeter stove maker with sister gas brand Gazco (1988); part of NIBE Stoves.","lines":["Gazco","Yeoman","Onyx"],"eras":[],"sig":[],"sc":[],"rel":["Contura"],"s":"https://www.stovax.com/information/about-us/"},
{"n":"Valor","c":"United Kingdom","f":"1890","seg":"Gas fires","d":"Birmingham heater maker that moved from oil to gas fires in 1966 (Valorflame 1979, Homeflame).","lines":["Homeflame"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://www.gracesguide.co.uk/Valor_Co"}]
trads=[
{"n":"Kachelofen (German and Austrian tiled stove)","g":"Ceramics & glass","r":"Germany, Austria","p":"Renaissance to present","d":"Tiled masonry stoves built by the Hafnermeister trade, heating rooms for hours from short fires.","tech":"Firebrick core with smoke channels, clad in glazed ceramic tiles","mat":"Firebrick, ceramic tile, stone","forms":["Masonry heater"],"ctr":["Hafnermeister (master potters)","Schleissheim Palace stove by Joseph Effner, c. 1720"],"auth":"","s":W+"Masonry_heater"},
{"n":"Swedish kakelugn","g":"Ceramics & glass","r":"Sweden, Finland","p":"18th century to present","d":"Tall tiled stoves made more efficient by Cronstedt and Wrede; factory tiles from makers such as Rörstrand.","tech":"Internal flue channels in a tiled masonry body","mat":"Ceramic tile, brick","forms":["Masonry heater"],"ctr":["Carl Johan Cronstedt","Fabian Casimir Wrede","Rörstrand, Stockholm"],"auth":"","s":W+"Masonry_heater"},
{"n":"Russian stove","g":"Masonry & stove-building","r":"Russia, Ukraine, Belarus, Poland, Slovakia, Romania","p":"15th century to present","d":"Brick stove at the centre of the izba used for heating, cooking, baking, drying and sleeping.","tech":"Labyrinth of brick smoke passages; sand layer between flue and shell","mat":"Brick","forms":["Masonry heater"],"ctr":[],"auth":"","s":W+"Russian_oven"}]
notes=("Kept both old kinds (Flued stove -> Wood-burning stove; Flued fire -> Inset and wall-hung fire, old Stovax/Valor models kept) and added four planned new kinds. "
"Left out: Contura and Jøtul model lists beyond F 602 (no retrieved model page), "
"Stûv 16/6 launch years, squirrel-relief start date (only in a search snippet), RAIS Viva L Red Dot year, Georgian/Art Deco dates, Dimplex brand entry (no brand page retrieved), "
"Morsø 1440/7900 and Charnwood Island/Cove ranges (not retrieved). No moves.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/G3/shelves/02_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
