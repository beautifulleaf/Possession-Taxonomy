import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E4/agent')
from h import v,x,B,W
w=lambda t:'https://en.wikipedia.org/wiki/'+t
DA=w('Dane_axe'); BE=w('Bearded_axe'); BA=w('Battle_axe'); TO=w('Tomahawk'); SM='https://collection.sciencemuseumgroup.org.uk/objects/co103630/tobacco-pipe-tomahawk'
PE='https://peachstatearchaeologicalsociety.org/artifact-identification/pipes/tomahawk-trade-pipes'; MA=w('Mace_(bludgeon)'); MS=w('Morning_star_(weapon)')
KB=w('Kanab%C5%8D'); WH=w('War_hammer'); HP=w('Horseman%27s_pick'); FL=w('Flail_(weapon)')
CS='Cold Steel'; BKS='Baltimore Knife & Sword'
kinds=[
{"n":"Battle axe","a":"war axe","d":"Axe made for fighting, not for cutting wood.","t":["one-handed","two-handed","throwing"],"s":"https://www.reliks.com/axes/viking-battle-axe/",
 "x":[x("Dane axe","","Viking Age–12th century","Two-handed axe with a broad, very thin blade on a long haft, carried by huscarls and the Varangian Guard.",DA,dt="edge 20–30 cm · haft 0.9–1.7 m",a="Danish axe · broadaxe"),
  x("Bearded axe","","6th century on","Axe whose lower blade extends below the butt into a 'beard' that can hook a shield.",BE,dt="beard length · haft",a="skeggøx"),
  x("Francisca","","early Middle Ages","Early medieval throwing axe.",BA,dt="head profile · haft"),
  x("Tabarzin","","","Traditional Persian battle axe with one or two crescent blades on a thin metal haft.",BA,dt="single or double blade · length",a="tabar")],
 "m":[["Viking Battle Axe",CS]]},
{"n":"Tomahawk","a":"","d":"Light one-handed axe of North American origin, made for fighting, throwing or trade.","t":["trade","pipe","spike","tactical","throwing"],"s":"https://www.buyingasword.com/hudson-bay-tomahawk-by-cold-steel/",
 "x":[x("Pipe tomahawk","","mid-1700s","Tomahawk with a pipe bowl on the poll and a hollow haft, made for trade and diplomacy; 'war and peace' in one object.",SM,
   [v("Trade pipe tomahawk blade (British)","","1780–1850","Science Museum Group example, of the type sold by the Hudson's Bay Company")],"bowl form · haft · inlay"),
  x("Hudson Bay tomahawk","","1750–1850","Trade axe sold by the Hudson's Bay Company to Native peoples, also called a frontiersman's axe.",PE,[v("Hudson Bay Tomahawk",CS)],"head profile · haft length",a="Hudson Bay axe"),
  x("Spontoon tomahawk","","c. 1875","Trade tomahawk with a spear-like spontoon blade, found mainly at western plains sites.",PE,dt="blade · haft"),
  x("Vietnam tomahawk","","1960s","Non-traditional tomahawk used by some US units in the Vietnam War, revived as a 'tactical tomahawk'.",TO,
   [v("Revival","American Tomahawk Company","2001","with knife-maker Ernest Emerson"),v("Vietnam Tomahawk",CS,"","wood handle")],"head · handle · spike")]},
{"n":"Mace","a":"","d":"Club with a heavy head, often flanged or spiked.","t":["flanged","knobbed","spiked"],"s":"https://copsplus.com/knives-tools/swords/medieval-swords/cold-steel-90mflm-maa-gothic-mace-28-overall-1055-carbon-steel/",
 "x":[x("Flanged mace","","12th century","Mace whose head carries radiating flanges that focus a blow enough to dent or pierce armour.",MA,
   [v("Pernach","","12th century on","Kievan Rus' origin"),v("Shestopyor","","","six-flanged, used in Poland-Lithuania")],"flange count · haft",a="pernach"),
  x("Morning star","","14th century","Club topped by a spiked ball, often with a long top spike; widely used in Germany.",MS,[v("Holy water sprinkler","","16th century","English army variant")],"head · spikes · haft length",a="Morgenstern"),
  x("Gada","","ancient","Indian mace with a spherical head, known since ancient times.",MA,dt="head · haft"),
  x("Kanabō","","feudal Japan","Spiked or studded Japanese war club of wood or iron, about 140 cm long.",KB,
   [v("Tetsubō","","","usually one-handed"),v("Ararebō","","","smaller one-handed, iron studs")],"wood or iron · studs · length")],
 "m":[["Bronze Skull Mace",BKS],["Man at Arms Gothic Mace",CS]],"r":[["Man at Arms",CS]]},
{"n":"War hammer","a":"","d":"Hafted weapon with a hammer head, often backed by a spike.","t":["long (polearm)","short (horseman's)"],"s":"https://www.kultofathena.com/product-category/weapons/",
 "x":[x("Long war hammer","","mid-14th century on","Two-handed foot war hammer about 1.5–1.8 m long, usually with a rear spike.",WH,dt="head · spike · haft"),
  x("Horseman's pick","","late Middle Ages–18th century","Short cavalry war hammer with a long, usually down-curved rear spike.",HP,[v("Nadziak","","","Polish form of the winged hussars")],"spike length · haft",a="nadziak")],
 "m":[["Gothic Warhammer 1",BKS],["Gothic Warhammer 2",BKS],["Norse Fenris Hammer",BKS],["Twin Ravens Hammer",BKS],["Viking Longship Warhammer",BKS],["Italian 14th to 15th Century War Hammer","Tod Cutler"]]},
{"n":"Flail","a":"","d":"Striking head joined to a handle by a chain, strap or hinge.","t":["short ball-and-chain","long two-handed"],"s":"https://www.kultofathena.com/product-category/weapons/",
 "x":[x("Peasant flail","","Late Middle Ages","Long two-handed flail adapted from the threshing flail, fielded in numbers by the Hussites.",FL,dt="striker · studs · length"),
  x("Military flail","","10th century on","Short weapon with a ball or striker on a chain, such as the kisten.",FL,dt="striker · chain length",a="kisten · Kettenmorgenstern"),
  x("Mangual","","15th–17th century","Spanish and Portuguese long two-handed military flail with very long chains.",FL,dt="chains · haft")]},
]
brands=[B("Baltimore Knife & Sword","United States","","Artisan & independent","forged replica weapons","US smithy making forged replica weapons.")]
W('07_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"All five old kinds kept. Mace placeholder 'Kanabo' became the Kanabō archetype; Cold Steel Hudson Bay Tomahawk became a version. Baltimore Knife & Sword war-hammer models kept in m (no archetype page). Cold Steel brand is registered on shelf 07_00. Ceremonial maces left out (institutional)."})
