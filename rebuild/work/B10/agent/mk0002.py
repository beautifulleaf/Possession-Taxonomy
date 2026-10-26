import json, os
W='https://en.wikipedia.org/wiki/'
OLD='https://www.petsathome.com/category/dog'
KU='https://kuranda.com/about/'; BB='https://bigbarker.com/blogs/news/big-barker-upenn-clinical-study'
OH='https://outwardhound.com/donut-shag-dog-bed-taupe-36x36/'
GU='https://www.gunner.com/blogs/pack/crash-tested-dog-crates-5-star-certified'
PM='https://brandwiki.lazada.com.ph/petmate/'
MW='https://www.midwesthomes4pets.com/about-us/'; MW2='https://globalpetindustry.com/article/midwest-homes-pets-united-states/'
EQ='https://www.tavistock-today.co.uk/news/dog-therapy-jumpers-set-to-spark-a-business-boom-363468'
BA='https://www.ahume.co.uk/blogs/editorial/its-a-dogs-life-introducing-the-new-barbour-dog-accessory-range'
HU='https://hurtta.com/en/pages/about-us'
RB='https://ruffwear.ca/blogs/explored/the-history-of-the-first-ruffwear-dog-boots'
CH='https://www.cleverhiker.com/more-gear/ruffwear-grip-trex-dog-boot-review/'
RF='https://ruffwear.ca/blogs/explored/the-float-coat-life-jacket'
SP='https://petsplusmag.com/sleepypod-achieves-first-safety-harness-certification-for-giant-dog-breeds/amp/'
kinds=[
{"n":"Dog bed","a":"dog basket · dog cushion","d":"A bed, cushion or basket made for a dog to sleep on.",
 "t":["donut / calming bed","bolster bed","orthopaedic memory-foam mattress","cushion / pillow bed","elevated cot bed","cave / hooded bed","sofa-style bed","cooling mat","heated or self-warming bed","chew-resistant bed","crate mat","basket"],
 "s":OLD,
 "x":[
  {"n":"Orthopaedic memory-foam bed","a":"orthopedic dog bed","d":"Thick foam mattress, often with bolsters, meant to support older or arthritic dogs' joints.","mk":"","y":"","s":BB,
   "v":[{"n":"Big Barker","mk":"Barker Beds","y":"2012","d":"large-dog bed tested in a University of Pennsylvania pilot study on arthritic dogs"},
        {"n":"Casper Plush Memory Foam Dog Bed","mk":"Casper","y":"","d":""},
        {"n":"Bully Beds Orthopedic Dog Bed","mk":"Bully Beds","y":"","d":""},
        {"n":"The Dog's Bed Orthopedic Dog Bed","mk":"The Dog's Bed","y":"","d":""},
        {"n":"PetFusion Ultimate Dog Bed","mk":"PetFusion","y":"","d":""}],
   "dt":"foam depth · bolster or flat · removable washable cover · sizes"},
  {"n":"Calming donut bed","a":"donut shag bed · cuddler","d":"Round bed with a high stuffed rim and shaggy faux-fur top that a dog curls and burrows into.","mk":"Best Friends by Sheri","y":"","s":OH,
   "v":[{"n":"The Original Calming Donut Shag Bed","mk":"Best Friends by Sheri","y":"","d":"AirLoft fibre fill; sizes 23–54 in"},
        {"n":"Furhaven Calming Donut Dog Bed","mk":"Furhaven","y":"","d":""}],
   "dt":"diameter · faux shag or lux fur · colours"},
  {"n":"Kuranda chew-proof bed","a":"Kuranda bed","d":"Elevated cot bed whose fabric sits in a channel inside the frame, leaving no edge for a dog to chew.","mk":"Kuranda","y":"1995","s":KU,
   "v":[{"n":"Rectangular dog bed (RDB)","mk":"Kuranda","y":"1995","d":"original rectangular design, replacing a round trampoline-style bed"},
        {"n":"Standard PVC Bed","mk":"Kuranda","y":"1998","d":"PVC frame"},
        {"n":"Standard Bed, aluminium","mk":"Kuranda","y":"2003","d":"aluminium frame for heavy chewers"}],
   "dt":"PVC or aluminium frame · vinyl, Cordura or mesh fabric · sizes"}],
 "m":[["Orvis ToughChew Dog Bed","Orvis"],["K9 Ballistics Chew Proof Elevated Cooling Dog Bed","K9 Ballistics"],["Bully Beds Chew Resistant Bed","Bully Beds"],["K&H Pet Products Self-Warming Dog Crate Bed","K&H Pet Products"],["K&H Pet Products Lectro-Soft Outdoor Heated Dog Bed","K&H Pet Products"],["Green Pet Shop Dog Cooling Mat","Green Pet Shop"],["Snoozer Luxury Cozy Cave Pet Bed","Snoozer"],["Kurgo Loft Wander Outdoor Dog Bed","Kurgo"],["P.L.A.Y. Eco-Friendly Dog Bed","P.L.A.Y."],["Trixie Vital Bed Noah","TRIXIE Heimtierbedarf"],["Ferplast Siesta Deluxe Dog Bed","Ferplast"]]},
{"n":"Dog crate","a":"dog cage · travel crate","d":"A box or cage in which a dog is kept at home or carried in a car or plane.",
 "t":["folding wire crate","plastic airline kennel","fabric / soft crate","furniture crate","heavy-duty aluminium crate","crash-tested rotomoulded kennel","car transport box","collapsible car crate"],
 "s":OLD,
 "x":[
  {"n":"Folding wire crate","a":"wire cage · fold-and-carry crate","d":"Wire-mesh crate with a plastic floor tray that folds flat, the standard indoor and house-training crate.","mk":"MidWest Homes for Pets","y":"","s":MW2,
   "v":[{"n":"iCrate","mk":"MidWest Homes for Pets","y":"","d":"double-door fold-and-carry crate with divider"},
        {"n":"iCrate Single Door","mk":"MidWest Homes for Pets","y":"","d":""},
        {"n":"LifeStages fold and carry crate","mk":"MidWest Homes for Pets","y":"","d":""},
        {"n":"Contour crate","mk":"MidWest Homes for Pets","y":"","d":"LapLock door with multiple lock points"}],
   "dt":"length 18–54 in · single or double door · divider panel"},
  {"n":"Plastic airline kennel","a":"Sky Kennel · Vari Kennel","d":"Moulded plastic shell with a wire door and vents, built to airline pet-travel standards.","mk":"Petmate","y":"","s":PM,
   "v":[{"n":"Sky Kennel","mk":"Petmate","y":"","d":"grew out of Doskocil's early plastic kennel; helped set airline standards"},
        {"n":"Ultra Vari Kennel","mk":"Petmate","y":"","d":""}],
   "dt":"sizes by dog weight · IATA compliance · wire or plastic door"},
  {"n":"Gunner G1 Kennel","a":"Gunner kennel","d":"Double-walled rotomoulded travel kennel, the first pet crate to earn a Center for Pet Safety 5-star crash-test rating.","mk":"Gunner Kennels","y":"","s":GU,
   "v":[{"n":"G1 Intermediate","mk":"Gunner Kennels","y":"","d":"CPS 5-star"},
        {"n":"G1 Medium","mk":"Gunner Kennels","y":"2018","d":"CPS 5-star with strength-rated anchor straps"},
        {"n":"G1 Small","mk":"Gunner Kennels","y":"","d":"CPS 5-star"}],
   "dt":"sizes Small–XL · colours · anchor straps · door options"}],
 "m":[["Diggs Revol Dog Crate","Diggs"],["Fable Dog Crate","Fable"],["Impact High Anxiety Dog Crate","Impact"],["EliteField 3-Door Folding Soft Dog Crate","EliteField"],["PetSafe Happy Ride Collapsible Dog Car Crate","PetSafe"],["Trixie Gulliver Transport Crate","TRIXIE Heimtierbedarf"],["Savic Dog Residence","SAVIC"],["Ferplast Atlas Scenic Car Transport Box","Ferplast"],["Carlson Secure and Compact Double Door Metal Dog Crate","Carlson"]]},
{"n":"Dog kennel","a":"doghouse · kennel and run","d":"An outdoor house that shelters a dog from the weather, sometimes with a fenced run.",
 "t":["wooden","plastic","insulated","heated","raised floor","kennel and run","steel shelter"],
 "s":W+"Doghouse",
 "m":[["Petmate Indigo dog house","Petmate"],["Petmate Husky Outdoor Plastic Dog House","Petmate"],["Trixie Natura Classic Flat Roof Dog Kennel","TRIXIE Heimtierbedarf"],["Lifetime Deluxe Dog House","Lifetime"],["Dog Palace Insulated Outdoor Plastic Dog House with Central Heater","Dog Palace"],["Aspen Pet Petbarn 3","Aspen Pet"],["ShelterLogic Steel Pet Shelter","ShelterLogic"],["Pawhut Plastic Dog House","Pawhut"]]},
{"n":"Dog coat","a":"dog jacket · dog jumper","d":"A garment made to be worn by a dog.",
 "t":["raincoat","padded winter coat / parka","fleece jumper or suit","knitted jumper","waxed cotton coat","quilted coat","drying coat","cooling coat","snowsuit","reflective / hi-vis"],
 "s":OLD,
 "x":[
  {"n":"Barbour wax dog coat","a":"Barbour dog coat","d":"Country dog coat in waxed or waterproof cotton with tartan or fleece lining and a cord collar, after Barbour's jackets.","mk":"Barbour","y":"","s":BA,
   "v":[{"n":"Classic Utility Waxed Dog Coat","mk":"Barbour","y":"","d":"Berber fleece lining, buckled under-strap"},
        {"n":"Waterproof Dog Coat","mk":"Barbour","y":"","d":"tartan lining, reflective trim"},
        {"n":"Waterproof Tartan Dog Coat","mk":"Barbour","y":"","d":"fleece lining"},
        {"n":"Wool Touch Tartan Dog Coat","mk":"Barbour","y":"","d":"Berber fleece lining"}],
   "dt":"wax, quilted or waterproof · olive, navy, tartan · XS–XXL by back length · harness keyhole"},
  {"n":"Equafleece dog suit","a":"Equafleece jumper","d":"Close-fitting polar-fleece jumper or suit for dogs, made as a cottage industry in Devon.","mk":"Equafleece","y":"2000s","s":EQ,
   "v":[{"n":"Dog jumper","mk":"Equafleece","y":"2000s","d":"first product, followed by T-shirts and coats"}],
   "dt":"jumper, suit or coat · colours · breed-specific sizes"}],
 "m":[["Hurtta Expedition Parka","Hurtta"],["Ruffwear Vert Dog Winter Jacket","Ruffwear"],["Canada Pooch Snowsuit Thermal Dog Snow Jacket","Canada Pooch"],["Carhartt Firm Duck Insulated Dog Chore Coat","Carhartt"],["Danish Design 2 in 1 Ultimate Lightweight Dog Coat","Danish Design"],["Wilderdog Waterproof Raincoat","Wilderdog"],["Puppia Bylur Mock Neck Full Zip Winter Jumpsuit","Puppia"],["HUNTER Uppsala Trend Dog Coat","HUNTER International"]]},
{"n":"Dog boots","a":"dog booties · paw boots","d":"Boots or socks that protect a dog's paws from rough ground, heat, ice or salt.",
 "t":["rubber-soled boots","fabric booties","socks","disposable rubber booties","winter boots"],
 "s":RB,
 "x":[
  {"n":"Ruffwear Grip Trex","a":"Grip Trex","d":"Hiking boot for dogs with a Vibram lugged sole, mesh upper and hook-and-loop closure, sold in pairs.","mk":"Ruffwear","y":"","s":RB,
   "v":[{"n":"Grip Trex","mk":"Ruffwear","y":"","d":"first Ruffwear boot with chevron lugs, mesh, toe guard and polyester strap"}],
   "dt":"sizes by paw width · colours · with Bark'n Boot liners or socks"}]},
{"n":"Dog life jacket","a":"dog buoyancy aid · flotation vest","d":"A buoyant vest with a lifting handle that keeps a dog afloat in water.",
 "t":["foam buoyancy jacket with handle","neoprene flotation vest"],
 "s":RF,
 "x":[
  {"n":"Ruffwear Float Coat","a":"Float Coat","d":"Dog life jacket with foam panels set for a natural swimming position, a strong lifting handle and reflective trim.","mk":"Ruffwear","y":"","s":RF,
   "v":[{"n":"Float Coat","mk":"Ruffwear","y":"","d":"later versions use softer PVC-free foam"}],
   "dt":"sizes XXS–XL · colours · leash D-ring"}]},
{"n":"Dog car restraint","a":"car harness · dog guard · seat cover","d":"A harness, guard, seat or cover that keeps a dog secure in a car.",
 "t":["crash-tested car harness","seat-belt tether","boot dog guard","seat cover / hammock","car booster seat"],
 "s":SP,
 "x":[
  {"n":"Sleepypod Clickit","a":"Clickit harness","d":"Car safety harness certified in Center for Pet Safety crash tests.","mk":"Sleepypod","y":"","s":SP,
   "v":[{"n":"Clickit Terrain (XL)","mk":"Sleepypod","y":"","d":"CPS five-star certification to 110 lb"}],
   "dt":"sizes · seat-belt loop · padded vest"}],
 "m":[["CarSafe travel harness","Company of Animals"]]}]
brands=[
 {"n":"Kuranda","c":"United States","f":"1987","seg":"elevated chew-proof dog beds","d":"Maryland maker of cot-style dog beds, named after the Australian town where the business began.","sig":["Kuranda chew-proof bed"],"s":KU},
 {"n":"Barker Beds","c":"United States","f":"2012","seg":"orthopaedic dog beds","d":"Maker of the Big Barker foam bed for large dogs.","sig":["Orthopaedic memory-foam bed"],"s":BB},
 {"n":"Best Friends by Sheri","c":"United States","seg":"pet beds","d":"Brand claiming the original calming donut shag bed.","sig":["Calming donut bed"],"s":OH},
 {"n":"MidWest Homes for Pets","c":"United States","f":"1921","seg":"wire crates and pens","d":"Family firm in Muncie, Indiana, making wire dog crates, pens and pet homes.","sig":["Folding wire crate"],"s":MW},
 {"n":"Petmate","c":"United States","f":"1959","seg":"pet travel and housing","d":"Founded as Doskocil Manufacturing in Texas; maker of plastic airline kennels.","sig":["Plastic airline kennel"],"s":PM},
 {"n":"Gunner Kennels","c":"United States","seg":"crash-tested dog kennels","d":"Tennessee maker of double-walled rotomoulded travel kennels.","sig":["Gunner G1 Kennel"],"s":GU},
 {"n":"Hurtta","c":"Finland","seg":"dog outdoor clothing and gear","d":"Finnish maker of dog coats, overalls, harnesses and leads, founded by clothing-industry professionals.","s":HU},
 {"n":"Equafleece","c":"United Kingdom","seg":"fleece dog clothing","d":"Devon cottage-industry maker of polar-fleece dog jumpers, suits and coats.","sig":["Equafleece dog suit"],"s":EQ},
 {"n":"Ruffwear","c":"United States","seg":"outdoor dog gear","d":"Bend, Oregon maker of dog boots, life jackets, harnesses and coats.","sig":["Ruffwear Grip Trex","Ruffwear Float Coat"],"s":"https://ruffwear.co.uk/blogs/explored/the-craftsmanship-behind-the-front-range-harness"},
 {"n":"Sleepypod","seg":"pet travel safety","d":"Maker of crash-tested pet car harnesses and carriers.","sig":["Sleepypod Clickit"],"s":SP},
 {"n":"Barbour","c":"United Kingdom","f":"1894","seg":"country clothing","d":"South Shields maker of waxed-cotton jackets whose range includes dog coats and accessories.","sig":["Barbour wax dog coat"],"s":"knowledge"},
 {"n":"Orvis","c":"United States","f":"1856","seg":"fly fishing and country goods","d":"Vermont outfitter whose dog range includes ToughChew beds.","s":"knowledge"}]
notes=("Kept all four old kinds and added Dog boots, Dog life jacket and Dog car restraint. Trimmed SKU lists to market-covering brands and turned families into archetypes. "
 "Dropped as SKU noise: generic marketplace coats, beds and houses (FUAMEY, IECOii, JoyDaog, Kuoser, LelePet, Snuowu, Homey Pet, Aivituvin, Mirapet, Retriever, Rugged Ranch, TIAKI and Trixie repeats, etc.). "
 "Left out: Tuffies chew-proof bed (no page found); Hurtta Expedition Parka and Ruffwear Vert kept only as models (no product page retrieved); boot-guard, seat-cover and booster-seat brands (none retrieved); Kurgo car harness (2013 CPS study placed it low; no current certification found); years for iCrate, Vari/Sky Kennel, Grip Trex and Float Coat (not on retrieved pages). Blocked: businesswire.com (403), charleychau.com (503).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/B10/shelves/00_02.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
