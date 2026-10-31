import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
from write import w, K
CAL="Caldwell Shooting Supplies"; DA="Do-All Outdoors"; CH="Champion Traps & Targets"; PM="Promatic"; AT="Atlas Trap Co"
CB="https://www.thecountryman.com/browning-oryx-grey-cartridge-bag"
w('E2','05_01',{"kinds":[
 K("Clay thrower","clay trap · trap thrower","Hand or machine trap that launches clay targets.",
   "https://www.shootinguk.co.uk/shooting/shotgun/best-clay-pigeon-traps/",
   [("Pigeon",PM),("AT1",AT),("AT2",AT),("Workhorse Electronic Auto-Feed Trap",CH),("Skybird",CH),("Flyway 180x",DA),("Clayhawk",DA),("Clay Hand Cannon",DA),("Claymore Connect",CAL),("ClayCopter Hand-Held Thrower",CAL),("EZ Aim Xcelerator Claymaster","Allen Company")],
   [("Kestrel",PM),("Hobby",PM),("Pigeon",PM),("Peregrine",PM),("Flyway",DA),("Claymore",CAL),("ClayCopter",CAL)],
   ["hand thrower","manual trap","automatic trap"]),
 K("Clay target","clay pigeon · clay","Frangible disc of pitch and limestone thrown as a flying target for clay shooting.",
   "https://en.wikipedia.org/wiki/Clay_pigeon_shooting",
   [("Blackout","White Flyer"),("Western","White Flyer"),("Orange Dome",CH),("ClayCopter UFO Glow",CAL)],None,
   ["standard (110 mm)","midi (90 mm)","super mini (70 mm)","mini (60 mm)","battue","rabbit"]),
 K("Shooting vest","skeet vest","Sleeveless vest with cartridge pockets and a shoulder pad, worn for clay shooting.",
   "https://broncos.co.nz/clothing/shooting-vests-and-jackets",
   [("Olympic 3.0","Beretta"),("GT671 Full Mesh","Beretta"),("Sporting EVO","Beretta"),("Gold Shooting Vest","Beretta"),("Olimpic","Castellani"),("Rio Mesh","Castellani"),("Ambidextrous","Castellani")],None,
   ["full mesh","half mesh","ambidextrous","women's cut"]),
 K("Cartridge bag","shell bag","Shoulder bag sized to carry shotgun cartridges, often by count of 50 to 250.",CB,
   [("Uniform Pro EVO Field Bag","Beretta"),("Uniform Pro EVO 100","Beretta"),("Gamekeeper Evo 100","Beretta"),("Terrain Evo Leather 100","Beretta"),("Challenge 150","Beretta"),("Challenge Shooting Bag","Browning"),("Byland 100","Croots"),("Rosedale 100","Croots"),("Stockbridge Leather 100","GMK")],
   [("Uniform Pro","Beretta"),("Gamekeeper Evo","Beretta")],
   ["cartridge pouch","50 / 100 / 150 / 250 capacity","leather","canvas"])],
 "brands":[
  {"n":"Promatic","c":"United Kingdom","seg":"Specialist","kf":"clay traps","d":"Hooton, Wirral maker of clay target traps serving the sport since 1985; over 100 models, mostly named after birds.","lines":["Kestrel","Hobby","Pigeon","Peregrine"],"s":"https://www.themanufacturer.com/articles/shooting-stars-how-promatic-went-from-specialist-engineering-to-global-leader/"},
  {"n":"Atlas Trap Co","c":"United States","seg":"Specialist","kf":"clay traps","d":"American maker of electronic clay target throwers from 50-target personal units upward.","lines":["AT1","AT2"],"s":"https://www.brownells.com/brands/atlas-trap-co-inc/gear/targets/clay-target-throwers"},
  {"n":"Beretta","c":"Italy","f":"1526","seg":"Heritage manufactory","kf":"shotguns, shooting wear","d":"Italian gunmaker that also sells shooting vests and cartridge bags.","lines":["Uniform Pro","Gamekeeper Evo"],"rel":["Browning","Castellani"],"s":"knowledge"},
  {"n":"Browning","c":"United States","seg":"Mainstream","kf":"shotguns","d":"American firearms brand that also sells shooting bags and clothing.","rel":["Beretta"],"s":"knowledge"},
  {"n":"Castellani","c":"Italy","seg":"Specialist","kf":"clay shooting vests","d":"Clay-shooting apparel and accessory brand: vests, glasses, cases, bags.","rel":["Beretta"],"s":"https://latest.vikingshoot.com/news/discovering-castellani-uk-the-one-stop-shop-for-premium-shotgun-shooting-accessories"}],
 "traditions":[],
 "notes":"Both old kinds kept. Clay thrower trimmed from 16 models to 11 (dropped ClayCopter Rip/Surface-to-Air launchers, Claymore and Claymore Solo, Flightmaster Jr, High Fly Trap, Flyway 80/180, kept as ranges); added Promatic Pigeon and Atlas AT1/AT2 from retrieved pages; types hand/manual/automatic. Beomat not found on any page, so omitted. Clay target: sizes from Wikipedia and Shooting UK as types; source now Wikipedia instead of a thrower page. New kinds Shooting vest and Cartridge bag with Beretta, Castellani, Browning, Croots and GMK models from retailer pages. No archetypes: these are tier/QoL items without named icon patterns."})
