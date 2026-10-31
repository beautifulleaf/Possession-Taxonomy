import sys; sys.path.insert(0,'work/C4/agent'); from w import w
w('C4','00_05',{"kinds":[
 {"n":"Paint-by-numbers kit","a":"paint by number","d":"Kit with a numbered printed outline, matching numbered paints and a brush, sold as one set.",
  "t":["acrylic","watercolour","canvas","board","theme: landscape, animal, portrait, museum reproduction","small, medium, large size"],
  "m":[["iHeartArt Paint By Number Kits","Bright Stripes"],["Creative Studio Watercolor Paint By Numbers","Faber-Castell"],["Paint By Number Museum Series","Faber-Castell"],["Paintology Paint-By-Number Canvas Kits","Ooly"],["Posca Paint By Number Kits","Posca"],["Canvas Art Painting Kits","Royal & Langnickel"]],
  "s":"https://www.dickblick.com/categories/painting/sets/paint-by-number/"},
 {"n":"Diamond-painting kit","a":"diamond art · 5D diamond painting","d":"Kit with a coded adhesive canvas, resin drills and an applicator, sold as one set.",
  "t":["round drills","square drills","full drill","partial drill","small, medium, large size"],
  "m":[["Diamond Painting Canvas Art Kits","Craft Medley"]],"s":"https://www.dickblick.com/categories/crafts/kits/"}],
 "brands":[],"traditions":[],"notes":"Restraint-only: both kit kinds kept with all old models (already within limit); medium, theme, drill shape and size as t types. No new brands added because none could be sourced from old data."})
FM="https://www.firemountaingems.com/beads/"
MET=["sterling silver","gold-filled","gold-plated","base metal","stainless steel","niobium","titanium"]
w('C4','05_01',{"kinds":[
 {"n":"Clasp","d":"Fastening finding that closes a necklace or bracelet.","t":["lobster claw","toggle","spring ring","box","magnetic","hook and eye"]+MET,"s":FM},
 {"n":"Jump ring","a":"split ring","d":"Open or closed wire ring that links jewellery parts.","t":["open","closed (soldered)","split ring"]+MET,"s":FM},
 {"n":"Earring finding","a":"ear wire · earring post","d":"Ear wire, post, hoop or clip used to build earrings.","t":["French hook ear wire","lever-back","post and back","hoop","clip-on"]+MET,"s":FM},
 {"n":"Pins, crimps and connectors","a":"head pin · eye pin · crimp bead · crimp tube · connector · link","d":"Small findings that hang beads on pins, join parts or secure stringing wire.","t":["head pin","eye pin","crimp bead","crimp tube","crimp cover","connector","link"]+MET,"s":FM},
 {"n":"Bail and bead cap","a":"bail · bead cap · pinch bail","d":"Findings that hang a pendant from a chain or cord, or cap a bead.","t":["pinch bail","glue-on bail","bail with loop","bead cap"]+MET,"s":FM},
 {"n":"Beading wire","a":"stringing wire · tiger tail","d":"Flexible nylon-coated steel wire made for stringing beads.","t":["strand count (7, 19, 49)","diameter","finish colour"],"m":[["Accu-Flex","Accu-Flex"]],"s":FM},
 {"n":"Beading thread and cord","a":"stretch cord · beading thread","d":"Thread, stretch cord or cord made for stringing beads.","t":["nylon thread","silk thread","stretch cord","leather cord","waxed cotton cord","braided cord"],"s":FM},
 {"n":"Jewellery wire and sheet","a":"jewellery wire · metal sheet · craft wire","d":"Solid metal wire or sheet sold for wire-wrapping, fabrication and jewellery making.","t":["wire","sheet","round, square, half-round profile","gauge","dead-soft, half-hard, hard temper","sterling silver","fine silver","gold-filled","copper","brass","coloured craft wire"],"s":FM},
 {"n":"Jewellery solder","d":"Solder wire, sheet or paste made for joining jewellery metal.","t":["wire","sheet","chip","paste","easy, medium, hard grade","silver solder","gold solder"],"s":"https://www.dickblick.com/categories/crafts/jewelry-making/"}],
 "brands":[],"traditions":[],"notes":"Restraint-only: merged head/eye pins, connectors and crimps into one kind and bails with bead caps, per plan; finding styles, metals, gauge, temper and solder grade as t types. Only old model kept (Accu-Flex). No brands added."})
D1="https://www.deserres.ca/collections/candles-making"
w('C4','07_03',{"kinds":[
 {"n":"Candle wax","d":"Wax sold for making candles.","t":["soy wax","paraffin wax","beeswax","coconut wax","rapeseed wax","gel wax","container blend","pillar blend"],"s":D1},
 {"n":"Candle wick","a":"wick · wick holder · wick sustainer","d":"Wick sold for making candles, with the tabs and holders that keep it centred.","t":["pre-tabbed cotton wick","braided cotton wick","wooden wick","wick sustainer tab","wick holder or centring bar"],"s":D1},
 {"n":"Candle mould","d":"Mould for casting pillar, taper or shaped candles.","t":["metal","silicone","plastic","pillar","taper","votive","shaped"],"s":D1},
 {"n":"Soap base","a":"melt-and-pour base","d":"Ready-made soap base sold for melting, scenting and moulding into soap.","t":["melt-and-pour","cold-process supplies","glycerin (clear)","goat's milk","shea butter","olive oil"],"s":"https://www.fredaldous.co.uk/products/shea-butter-soap-base"},
 {"n":"Soap mould","d":"Mould for casting bars or shaped soaps.","t":["silicone","plastic","wooden loaf","single bar","multi-cavity","loaf"],"s":"https://www.deserres.ca/collections/soap-making"}],
 "brands":[],"traditions":[],"notes":"Restraint-only: wick holder merged into Candle wick; wax types and melt-and-pour versus cold-process bases as t types. Old data had no models; none added."})
w('C4','08_04',{"kinds":[
 {"n":"Pyrography pen","a":"wood burner · woodburning tool","d":"Heated pen made for burning designs into wood, leather or gourds.","t":["solid-point (soldering-iron style)","wire-nib with control unit","single pen","dual pen","interchangeable tips"],
  "m":[["Razertip P80 Burner","Razertip Industries Ltd"],["Razertip SS-D10 Burner","Razertip Industries Ltd"],["Razertip SK Burner","Razertip Industries Ltd"],["TruArt Professional Dual-Pen Wood-Burning Tool","TruArt"],["TruArt Stage 1 Pyrography Pen Wood-Burning Tool Set","TruArt"],["Creative Versa-Tool","Walnut Hollow"],["Creative Woodburner","Walnut Hollow"]],
  "s":"https://razertip.com/collections/razertip-pyrographic-burners"},
 {"n":"Craft wood blank","a":"wooden plaque · wood shape","d":"Wooden plaque, shape or blank sold for decorating, burning or painting.","t":["plaque","round","slice with bark","shape","box","clock surface","basswood","birch plywood"],
  "m":[["Basswood Country Round Plaque","Walnut Hollow"],["Clock Surface","Walnut Hollow"]],"s":"https://www.walnuthollow.com/collections/wood-burning"},
 {"n":"Turning blank","a":"bowl blank · pen blank · spindle blank","d":"Wood blank sold for turning bowls, pens or spindles on a lathe.","t":["bowl blank","spindle blank","pen blank","seasoned","green","stabilised"],"s":"https://www.greenvill.co.uk/collections/bowl-blanks"}],
 "brands":[],"traditions":[],"notes":"Restraint-only: three kinds kept. Pyrography pen trimmed from 11 to 7 models (dropped Razertip P88, SL1, SL3 and Walnut Hollow Creative Woodburner Value Tool as near-duplicate variants). Colwood named in the brief was not added because it is not in the old data and no page was retrieved."})
A="https://shop.ilovetocreate.com/aleenes"
w('C4','09_01',{"kinds":[
 {"n":"Craft glue","a":"PVA glue · liquid craft glue · tacky glue","d":"Liquid glue made for paper, fabric and general crafts.","t":["tacky (PVA)","quick-dry","clear gel","fabric glue","multi-surface"],
  "m":[["Aleene's Original Tacky Glue","Aleene's"],["Aleene's Quick Dry Tacky Glue","Aleene's"],["Aleene's Fast Grab Tacky Glue","Aleene's"],["Aleene's Clear Gel Tacky Glue","Aleene's"],["Aleene's Super Fabric Adhesive","Aleene's"],["Aleene's The Ultimate Multi-Surface Adhesive","Aleene's"]],
  "r":[["Tacky Glue","Aleene's"]],"s":A},
 {"n":"Hot-glue gun","a":"glue gun · glue pen · hot-melt glue stick · glue skillet","d":"Electric tool that melts hot-melt glue sticks for quick craft bonding.","t":["mini","full size","glue pen","cordless","dual temperature","low-temperature","hot-melt glue stick","glue skillet"],
  "m":[["CL-195F Cordless/Corded Detail Tip Mini Hot Glue Gun","Surebonder"],["CL-800F Cordless/Corded Full Size Hot Glue Gun","Surebonder"],["GP-100F Mini Detail Tip Hot Glue Pen","Surebonder"],["PRO2-60 Cordless Professional Hot Glue Gun","Surebonder"],["Ultra Series DT-360F Dual Temperature Hot Glue Gun","Surebonder"]],
  "r":[["Ultra Series","Surebonder"]],"s":"https://surebonder.com/collections/glue-guns"},
 {"n":"Spray adhesive","d":"Aerosol adhesive made for mounting paper, fabric and foam.","t":["permanent","repositionable","heavy-duty"],
  "m":[["Aleene's DIY Craft Heavy-Duty Adhesive Spray","Aleene's"],["Aleene's Repositionable Tacky Spray","Aleene's"]],"s":A},
 {"n":"Decoupage medium","d":"Glue and sealer in one, made for decoupage.","t":["matte","gloss","satin","outdoor","dishwasher-safe"],"s":A},
 {"n":"Craft paint","a":"acrylic craft paint","d":"Paint made for decorating craft objects, chosen by the surface it goes on.","t":["matte acrylic","multi-surface","metallic","glitter","outdoor","glow-in-the-dark","texture","wax effect"],
  "m":[["DecoArt Americana Acrylic Paints","DecoArt"],["DecoArt Americana Decor Texture Paints","DecoArt"],["FolkArt Matte Acrylic Paints","Plaid"],["FolkArt Multi-Surface Acrylic Paints","Plaid"],["FolkArt Metallic Acrylic Paints","Plaid"],["FolkArt Outdoor Acrylic Paints","Plaid"],["Apple Barrel Acrylic Craft Paint","Plaid"]],
  "r":[["Americana","DecoArt"],["FolkArt","Plaid"]],"s":"http://dickblick.com/categories/crafts/paint/acrylic-craft-paint"},
 {"n":"Shrink plastic sheet","a":"shrink film","d":"Plastic sheet that shrinks and hardens when baked, sold for making charms.","t":["clear","frosted","white","printable"],"s":"https://www.dickblick.com/categories/crafts/jewelry-making/"}],
 "brands":[],"traditions":[],"notes":"Restraint-only: glue sticks and glue skillet merged into Hot-glue gun as t types. Craft glue trimmed from 9 to 6 Aleene's models (dropped temporary fabric glue, Insta-Fuse and Turbo as niche variants); craft paint trimmed from 14 to 7 (glitter, glow, colour-shift, neon, treasure-gold and wax-effect lines moved to t types); 'Ultra Series' moved from m to r; duplicate 'Apple Barrel' model dropped. UHU, Bostik and Mod Podge named in the brief were not added because they are not in the old data and no pages were retrieved."})
