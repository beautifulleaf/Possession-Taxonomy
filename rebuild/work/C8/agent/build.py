import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Reclaimed brick","a":"second-hand brick · salvaged brick","d":"Used bricks cleaned of old lime mortar and resold by reclamation yards for repair, matching and character work.",
 "t":["London stock","handmade","imperial-size","reclaimed paviors","red stock","blue engineering"],"s":"https://www.salvoweb.com",
 "x":[
  {"n":"London stock brick","a":"London stock · yellow stock","d":"Handmade yellow-brown brick of London brickearth and chalk, moulded on a stock and used across London and the South East.","mk":"","y":"19th century","s":W+"London_stock_brick",
   "v":[{"n":"Red stock","mk":"","y":"19th century","d":"red-firing variant, also common"},{"n":"New handmade stock","mk":"","y":"today","d":"small batches from traditional works in Kent and Sussex for heritage work"}],
   "dt":"colour yellow, brown, red; soot-darkened grey or black faces · soft lime mortar cleans off; painted 'second-hand' fakes unfit for face work"},
  {"n":"Staffordshire blue brick","a":"Staffordshire blue · blue engineering brick","d":"Very hard deep-blue brick of Etruria marl fired hot in low oxygen, used for bridges, copings and steps.","mk":"","y":"17th century; boom 19th century","s":W+"Staffordshire_blue_brick",
   "v":[{"n":"Joseph Hamblet works, West Bromwich","mk":"Joseph Hamblet","y":"1851","d":"notable Black Country producer"}],
   "dt":"high crushing strength, low water absorption · copings, paviors, facings"},
  {"n":"Fletton brick","a":"Fletton","d":"Machine-made common brick of lower Oxford clay whose carbon content cut firing costs; displaced the stock brick in the 20th century.","mk":"London Brick Company","y":"1889","s":W+"Fletton_brick",
   "v":[],"dt":"made at Fletton (Peterborough) and Stewartby"}]},
{"n":"Reclaimed oak beam","a":"reclaimed timber beam · barn beam · reclaimed lumber","d":"Structural timbers and boards salvaged from barns, mills and warehouses, resold for beams, mantels, cladding and furniture.",
 "t":["oak beam","heart pine","barn wood boards","chestnut","reclaimed timber boards","air-dried vs reclaimed"],"s":W+"Reclaimed_lumber",
 "x":[
  {"n":"Heart pine","a":"antique longleaf pine","d":"Longleaf pine heartwood recovered from 19th-century factories and warehouses.","mk":"","y":"19th century","s":W+"Reclaimed_lumber","v":[],"dt":"beams resawn into wide planks · flooring, beams"},
  {"n":"Barn wood","a":"barnwood · reclaimed barn timber","d":"Mixed boards and timbers from dismantled barns, typically oak, chestnut, poplar, hickory and pine.","mk":"","y":"","s":W+"Reclaimed_lumber","v":[],"dt":"species mix · weathered or resawn faces · siding, beams, furniture"}]},
{"n":"Reclaimed flooring","a":"salvaged flooring · reclaimed parquet","d":"Floor blocks and boards lifted from old buildings and sold loose for relaying.",
 "t":["parquet blocks","pine floorboards","oak boards","Baltic pine","chevron"],"s":"https://www.salvoweb.com",
 "x":[
  {"n":"Herringbone parquet","a":"herringbone block floor","d":"Rectangular blocks laid in a zigzag, usually 2:1 or 3:1 in proportion; the most popular parquet pattern.","mk":"","y":"","s":W+"Herringbone_pattern","v":[],"dt":"wood, brick or tile · block ratio 2:1 or 3:1 · species, finish"},
  {"n":"Versailles panel","a":"parquet de Versailles · parquet de menuiserie","d":"Large diagonal-square panels of interlaced strips, introduced at Versailles to replace marble floors.","mk":"","y":"1684","s":W+"Parquetry","v":[],"dt":"panel size · oak · diagonal lattice"}]},
{"n":"Reclaimed roof slate and tile","a":"second-hand slates · reclaimed roof tiles","d":"Roofing slates and clay tiles stripped from old roofs and resold for repairs and period-matching.",
 "t":["Welsh slate","clay plain tile","pantile","interlocking tile","ridge and hip tiles"],"s":W+"Welsh_slate",
 "x":[
  {"n":"Welsh slate","a":"Penrhyn slate · Bangor slate","d":"Roofing slate from north-west Wales, sold in standard named sizes set by Penrhyn.","mk":"","y":"Roman period; named sizes 1730–1740","s":W+"Welsh_slate",
   "v":[{"n":"Duchess","mk":"Penrhyn Quarry","y":"1730–1740","d":"24 × 12 in, the largest"},{"n":"Countess","mk":"Penrhyn Quarry","y":"1730–1740","d":""},{"n":"Lady","mk":"Penrhyn Quarry","y":"1730–1740","d":""},{"n":"Double","mk":"Penrhyn Quarry","y":"1730–1740","d":""},{"n":"Single","mk":"Penrhyn Quarry","y":"1730–1740","d":"the smallest"}],
   "dt":"named size · quarry (Penrhyn, Dinorwic, Blaenau Ffestiniog, Nantlle) · colour"},
  {"n":"Plain clay tile","a":"English squared tile · flat tile","d":"Flat overlapping clay tile hung from battens, common in medieval Northern Europe.","mk":"","y":"medieval","s":W+"Roof_tiles","v":[{"n":"Beaver-tail","mk":"","y":"","d":"pointed southern German form"}],"dt":"handmade or machine-made · camber · colour"},
  {"n":"Pantile","a":"S tile","d":"One-piece S-profile clay tile combining pan and cover.","mk":"","y":"1500s (Dutch roofs)","s":W+"Roof_tiles","v":[{"n":"Scandia pantile","mk":"","y":"","d":"Scandinavian variant"}],"dt":"profile · colour"},
  {"n":"Marseilles tile","a":"French tile · interlocking tile","d":"Interlocking clay tile from Marseille.","mk":"","y":"1860s","s":W+"Roof_tiles","v":[{"n":"Martin Brothers, Marseille","mk":"Martin Brothers","y":"1860s","d":"originators"}],"dt":"interlock pattern · colour"}]},
{"n":"Reclaimed flagstone","a":"reclaimed flags · reclaimed paving","d":"Weathered stone flags, setts and kerbs lifted from old floors and streets for reuse.",
 "t":["York stone flags","setts","cobbles","kerb stones","slate flags","riven","sawn"],"s":W+"Flagstone",
 "x":[
  {"n":"York stone flag","a":"Yorkstone · York stone paving","d":"Carboniferous sandstone flag from Yorkshire quarries, the traditional London paving stone.","mk":"","y":"Middle Ages","s":W+"Yorkstone","v":[],"dt":"riven or sawn · weathered surface · buff, grey, rust banding"},
  {"n":"Granite sett","a":"sett · Belgian block","d":"Roughly rectangular quarried paving stone, usually granite, cut to a regular shape unlike a cobble.","mk":"","y":"Roman origin","s":W+"Sett_(paving)","v":[],"dt":"stone · size · sawn or split faces"}]},
{"n":"Chimney pot","a":"chimney terminal","d":"Pot or terminal set on top of a chimney stack; old terracotta pots are a salvage staple.",
 "t":["cannon head","roll top","beehive","crown","bishop","glazed","unglazed"],"s":"https://www.jewson.co.uk/building-materials/roofing/chimney-pots-cowls",
 "x":[
  {"n":"Leeds Roll Top","a":"roll top pot","d":"Rounded-shaft Yorkshire pot with a rolled rim, among the tallest of the Leeds range.","mk":"","y":"antique","s":"https://www.thisoldhouse.com/masonry/add-exterior-style-with-chimney-pots","v":[],"dt":"about 58 in tall · terracotta, glazed or unglazed"},
  {"n":"Leeds Beehive","a":"beehive pot","d":"Small bulbous pot of the Leeds range.","mk":"","y":"antique","s":"https://www.thisoldhouse.com/masonry/add-exterior-style-with-chimney-pots","v":[],"dt":"about 18 in · terracotta"},
  {"n":"Cannon Barrel","a":"cannon head pot","d":"Straight cylindrical pot with a plain or thickened rim.","mk":"","y":"","s":"https://www.thisoldhouse.com/masonry/add-exterior-style-with-chimney-pots","v":[],"dt":"height · finish"}]},
{"n":"Architectural salvage","a":"architectural antiques · reclamation","d":"Period fittings removed from demolished buildings and sold by reclamation yards: chimneypieces, doors, railings, columns and garden ornament.",
 "t":["fireplace surround","chimneypiece","fire grate","period door","cast-iron railings","cast-iron column","corbel","garden urn","church fittings","sanitaryware"],"s":"https://www.homesandantiques.com/antiques/history-reclamation-and-salvage-yards",
 "x":[
  {"n":"Adam chimneypiece","a":"Adam-style mantelpiece","d":"Neoclassical fireplace surround after the Adam brothers, dominant in late 18th-century Britain and revived a century later.","mk":"","y":"late 18th century","s":W+"Mantelpiece","v":[],"dt":"marble, stone or wood · overmantel · carving quality"},
  {"n":"Adam balcony railing","a":"Adelphi railing","d":"Cast-iron balcony railing pattern imitating wrought iron, made for Robert Adam's Adelphi in London.","mk":"Carron Company","y":"1775","s":W+"Cast-iron_architecture","v":[],"dt":"produced into the 1830s · panel pattern"}]}]
brands=[
 {"n":"Carron Company","c":"United Kingdom","f":"1759","seg":"Ironfounder","d":"Falkirk ironworks that cast stoves, fire grates, balustrades and carronades; now Carron Phoenix.","lines":["fire grates","balustrades","Carron bathtub"],"eras":["Receivership 1982; later Carron Phoenix under Franke"],"sig":["Adam balcony railing"],"sc":[],"rel":[],"s":W+"Carron_Company"},
 {"n":"London Brick Company","c":"United Kingdom","f":"1900","seg":"Brickmaker","d":"Maker of Fletton bricks from Oxford clay at Peterborough and Stewartby; now part of Forterra.","lines":["Fletton bricks"],"eras":["John Cathles Hill, from 1889","Hanson ownership from 1984"],"sig":["Fletton brick"],"sc":[],"rel":["Forterra"],"s":W+"Fletton_brick"}]
trads=[
 {"n":"Welsh slate quarrying","g":"Stone & masonry","r":"North-west Wales","p":"Roman period–present; peak 1898","d":"Quarrying and splitting of Welsh slate for roofs, floors and slabs.","tech":"quarrying, splitting and dressing slate to standard sizes","mat":"slate","forms":["Reclaimed roof slate and tile"],"ctr":["Penrhyn Quarry","Dinorwic Quarry","Blaenau Ffestiniog","Nantlle Valley","Corris"],"auth":"Penrhyn named sizes from Duchess (24 × 12 in) down to Single","s":W+"Welsh_slate"},
 {"n":"London stock brickmaking","g":"Stone & masonry","r":"London and South East England","p":"19th century; small revival today","d":"Hand-moulding of brickearth bricks on a stock, fired with 'Spanish' ash and cinders.","tech":"clay pressed into a mould on an iron-faced stock, struck off with a wire, dried and fired","mat":"brickearth, chalk, ash","forms":["Reclaimed brick"],"ctr":["west Middlesex","Kent","Essex","Sussex"],"auth":"original soft lime mortar cleans off; new bricks painted to pass as second-hand are unfit for face work","s":W+"London_stock_brick"}]
notes=("Chimney pot: old blank models (Cannon head, Roll top) turned into types; archetypes from This Old House. "
 "Left out: chevron parquet and cast-iron radiators (no retrieved salvage source); LASSCO/Salvo/Walcot are dealers, not makers, so no brand entries; "
 "Wikipedia 'Architectural salvage' page does not exist (404), so that kind is sourced to a Homes & Antiques article; Penrhyn Quarry is a version mk without a register entry.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/C8/shelves/02_02.json'; os.makedirs('work/C8/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
