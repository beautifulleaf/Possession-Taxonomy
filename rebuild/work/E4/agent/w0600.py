import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E4/agent')
from h import v,x,B,W
EL='https://en.wikipedia.org/wiki/English_longbow'; FB='https://en.wikipedia.org/wiki/Flatbow'; MB='https://en.wikipedia.org/wiki/Mongol_bow'
TA='https://en.wikipedia.org/wiki/Turkish_archery'; GG='https://en.wikipedia.org/wiki/Gakgung'; KA='https://en.wikipedia.org/wiki/Lajos_Kassai'
KY='https://en.wikipedia.org/wiki/Ky%C5%ABd%C5%8D'; MY='https://www.fun-japan.jp/en/articles/14031'; HG='https://en.wikipedia.org/wiki/Holmegaard_bow'
CB='https://en.wikipedia.org/wiki/Compound_bow'; HA='https://en.wikipedia.org/wiki/Holless_Wilbur_Allen'; BK='https://www.beararchery.com/blogs/base-camp-archery-blog/bear-archery-kodiak'
HO='https://en.wikipedia.org/wiki/Hoyt_Archery'; GH='https://www.gohunt.com/browse/hunting-101/archery/compound-crossbow-versus-recurve-crossbow'
FS='https://fieldandstream.com/outdoor-gear/hunting-gear/bow-hunting/crossbows/ravin-r10x-pro-crossbow-review'; TP='https://www.tenpointcrossbows.com/our-story'
EX='https://www.bowhunter.com/editorial/excalibur-micro-335-crossbow-review/309494'
kinds=[
{"n":"Longbow","a":"warbow · self longbow","d":"Tall hand-drawn bow, about the archer's height, with long straight limbs and no recurve.",
 "t":["self bow (one stave)","laminated","D-section (English)","rectangular-section (American)"],"s":"https://lancasterarchery.com/pages/bows",
 "x":[x("English longbow","","c. 1250–1450","Tall yew self bow of medieval English and Welsh archers, about 6 ft long, used for war and hunting.",EL,
   [v("Mary Rose bows","","1545","about 137 bows recovered from the wreck; 6 ft 2 in–6 ft 11 in, est. 150–160 lbf"),v("Modern replica warbow","","","heavy yew reproductions after the Mary Rose finds")],"wood (yew, ash, elm) · length · draw weight",a="warbow"),
  x("American longbow","","1930s","Longbow with narrow limbs of rectangular section and a handle of similar width, developed from 1930s limb research.",FB,
   [v("Hill-style longbow","","","popularised by Howard Hill; later built with fibreglass")],"wood or fibreglass lamination · length · draw weight",a="Hill-style bow · American semi-longbow")],
 "m":[["Bear Montana Longbow","Bear Archery"]]},
{"n":"Horse bow","a":"composite bow · Asiatic bow · horsebow","d":"Short reflex composite bow of horn, wood or bamboo and sinew, made to shoot from horseback.",
 "t":["traditional horn-and-sinew","modern laminated or fibreglass","thumb draw"],"s":MB,
 "x":[x("Mongol bow","","13th century","Recurved composite bow of bamboo, horn and sinew used by the Mongol Empire's horse archers.",MB,
   [v("Medieval Mongol bow","","13th century","smaller siyahs, low string bridges"),v("Manchu-derived Mongolian bow","","17th century on","larger siyahs and leather string bridges; used at Naadam")],"siyah size · string bridges · draw weight"),
  x("Turkish bow","","Ottoman period","Short, strongly reflexed composite bow with a maple core, horn belly and sinew back, refined for flight archery.",TA,
   [v("Ottoman flight bow","","after 1571","built for distance shooting after Lepanto")],"limb reflex · draw weight · decoration",a="Ottoman bow"),
  x("Gakgung","","Joseon period","Korean reflex bow with a bamboo core, water-buffalo horn belly and sinew back, shot with a thumb draw.",GG,
   [v("Horn gakgung","","","traditional; Yecheon makes most of them"),v("Laminated fibreglass gakgung","","","modern version")],"horn or fibreglass · draw weight",a="Korean bow · guk gung"),
  x("Hungarian bow","Kassai","Hungarian Conquest period; reconstructed mid-1980s","Composite reflex bow of the Hungarian Conquest period, reconstructed and put into series production by Lajos Kassai.",KA,
   [v("Kassai reconstruction","Kassai","mid-1980s","modern materials; Kassai also makes Scythian, Hun, Avar and Mongol styles")],"style · draw weight",a="Magyar bow")]},
{"n":"Yumi","a":"Japanese bow · daikyū · wakyū","d":"Asymmetric Japanese longbow over 2 m long, gripped below the middle, used in kyūdō.",
 "t":["bamboo","synthetic (laminated wood with fibreglass or carbon)","daikyū (full length)","hankyū (short)"],"s":KY,
 "x":[x("Miyakonojō bamboo yumi","","Edo period","Bamboo and haze-wood bow from Miyakonojō, Japan's main centre for bamboo bows, each made by one bowyer in 200-plus steps.",MY,
   dt="length · draw weight · bowyer",a="Miyakonojō daikyū")]},
{"n":"Flatbow","a":"flat bow","d":"Non-recurved bow with wide, flat limbs of roughly rectangular section and a narrower, deeper handle.",
 "t":["wooden self bow","laminated","fibreglass"],"s":FB,
 "x":[x("Holmegaard bow","","c. 7000 BC","Mesolithic elm bow from Danish bogs with wide parallel limbs; the oldest bow type found, now copied by bowyers.",HG,
   [v("Replica Holmegaard bow","","","modern reconstructions, used in flight archery")],"wood · length 170–180 cm · draw weight"),
  x("Native American flatbow","","","Wooden flatbow of tribes such as the Hupa, Karok and Wampanoag, used for hunting and war.",FB,dt="wood · backing · length")]},
{"n":"Recurve bow","a":"","d":"Hand-drawn bow whose limb tips curve away from the archer.",
 "t":["one-piece","take-down","Olympic (ILF fitting)","barebow","hunting"],"s":"https://lancasterarchery.com/collections/recurve-bows",
 "x":[x("Bear Kodiak","Bear Archery","1959","Fibreglass-and-maple hunting recurve made famous by Fred Bear.",BK,[v("'59 Kodiak reproduction","Bear Archery","","maple laminate core with black fibreglass")],"length · draw weight · riser wood")],
 "m":[["Fred Bear Super Grizzly","Bear Archery"],["Buffalo","Hoyt"],["Gamemaster II","Hoyt"]]},
{"n":"Compound bow","a":"","d":"Hand-drawn bow whose limbs are bent by a system of cams and cables that gives let-off at full draw.",
 "t":["single cam","hybrid cam","dual cam","binary cam","youth"],"s":"https://lancasterarchery.com/collections/compound-bows",
 "x":[x("Allen compound bow","","1966","The first compound bow: Holless Wilbur Allen's recurve with pulleys at the limb tips.",HA,[v("US patent 3,486,495","","1969","granted December 1969")],"",a="Allen pulley bow")],
 "m":[["Hoyt RX-10","Hoyt"],["Hoyt AX-3","Hoyt"],["Hoyt Ruckus","Hoyt"],["Mathews Title","Mathews"],["Mathews ARC","Mathews"],["Bowtech Carbon One","Bowtech"],["Bowtech Reckoning","Bowtech"],
      ["PSE Dominator Duo X","PSE Archery"],["Elite Victra","Elite Archery"],["Bear Adapt 2","Bear Archery"],["Darton Consequence 2","Darton Archery"],["Prime Divide","Prime Archery"]]},
{"n":"Recurve crossbow","a":"","d":"Crossbow with recurved limbs and no cams or cables, mounted across a stock and released by a trigger.","s":"https://lancasterarchery.com/collections/barnett",
 "x":[x("Excalibur Micro","Excalibur","","Compact recurve crossbow line built on Excalibur's Compact Recurve Technology limbs.",EX,[v("Micro 335","Excalibur","2015","Gen II CRT limbs, 270 lb draw")],"draw weight · length · speed")]},
{"n":"Compound crossbow","a":"","d":"Crossbow whose limbs work through cams and cables.","t":["standard limbs","reverse-draw","HeliCoil (cams turn on the rail)"],"s":"https://lancasterarchery.com/collections/barnett",
 "x":[x("Ravin R10","Ravin","","Compact compound crossbow with Ravin's HeliCoil cam system and a light cocking system.",FS,[v("R10X Pro","Ravin","","fully supported optics rail")],"speed · cocking system · finish")],
 "m":[["TX Ultra 29.5","TenPoint"],["Nitro XRT","TenPoint"],["Vapor RS470","TenPoint"]]},
]
brands=[
 B("Bear Archery","United States","","Mainstream","hunting bows · recurves","Bow maker founded by Fred Bear, known for hunting recurves and compound bows.",BK,sig=["Bear Kodiak"]),
 B("Hoyt","United States","1931","Professional & flagship","target & hunting bows","Bow maker founded in St. Louis; owned by Jas. D. Easton since 1983; its recurves won every individual gold at London 2012.",HO,rel=["Easton Archery"]),
 B("Mathews","United States","1992","Premium","compound bows","Compound-bow maker from Wisconsin founded by Matt McPherson."),
 B("Bowtech","United States","","Premium","compound bows","US compound-bow maker."),
 B("PSE Archery","United States","1970","Mainstream","compound bows","Precision Shooting Equipment, founded by Pete Shepley; the surviving licensee of Allen's compound patent and parent of Browning Archery.",HA),
 B("Elite Archery","United States","","Premium","compound bows","US compound-bow maker."),
 B("Darton Archery","United States","","Specialist","compound bows","US compound-bow maker from Michigan."),
 B("Prime Archery","United States","","Premium","compound bows","US compound-bow brand."),
 B("Excalibur","","1983","Specialist","recurve crossbows","Crossbow maker known for recurve crossbows.",EX,sig=["Excalibur Micro"]),
 B("TenPoint","United States","1994","Premium","crossbows","Crossbow maker of Mogadore, Ohio, founded by Rick and Bill Bednar; owns Wicked Ridge and Horton.",TP,lines=["Ultra Series","Wicked Ridge","Horton"]),
 B("Ravin","United States","","Premium","compound crossbows","Crossbow maker whose bows use its patented HeliCoil cam system.",FS,sig=["Ravin R10"]),
 B("Barnett","","","Mainstream","crossbows","Crossbow maker."),
 B("Kassai","Hungary","mid-1980s","Artisan & independent","horse bows","Bow workshop of Lajos Kassai, first to series-produce the reconstructed Hungarian bow.",KA,sig=["Hungarian bow"]),
]
trads=[
 {"n":"Miyakonojō bamboo bow-making","g":"Weapons & arms","r":"Miyakonojō, Miyazaki, Japan","p":"Edo period to present","d":"Making of bamboo yumi for kyūdō by single bowyers (yumi-shi); the city makes about 90% of Japan's bamboo bows.",
  "tech":"laminating bamboo and wood strips, over 200 hand steps","mat":"madake bamboo · haze wood","forms":["Yumi"],"ctr":["Miyakonojō"],"auth":"bamboo construction by a named yumi-shi","s":MY},
 {"n":"Korean gakgung bow-making","g":"Weapons & arms","r":"Korea","p":"Joseon period to present","d":"Making of the horn composite Korean bow; designated an Important Intangible Cultural Property in 1971.",
  "tech":"horn, bamboo and sinew composite glued with isinglass, birch-bark covering","mat":"water-buffalo horn · bamboo · oak · sinew · mulberry or black locust","forms":["Horse bow"],"ctr":["Yecheon"],"auth":"horn belly and sinew back rather than fibreglass","s":GG},
 {"n":"Turkish traditional archery and bow-making","g":"Weapons & arms","r":"Anatolia, Ottoman lands","p":"Ottoman period; revived after the 1930s","d":"Ottoman composite bows and flight archery, inscribed on UNESCO's intangible heritage list in 2019.",
  "tech":"reflexed horn-wood-sinew composite bonded with animal glue","mat":"maple · horn · sinew","forms":["Horse bow"],"ctr":["Neçmeddin Okyay (last traditional bowyer, d. 1930s)"],"auth":"horn and sinew construction; strongly reflexed C-shape unstrung","s":TA},
]
W('06_00',{"kinds":kinds,"brands":brands,"traditions":trads,"notes":"All five old kinds kept; Horse bow, Yumi and Flatbow added. Compound bow cut from 20 to 12 models (one or two per market brand plus Hoyt Ruckus youth bow from Wikipedia); dropped Bowtech Ascend, Darton Tritech, Elite Emerse/Terrain/Varos, Hoyt Concept X/Enduro, PSE Lazer X/Sicario as older or duplicate lines. Field & Stream 2026 crossbow test winner TenPoint TX Ultra 29.5 added. Japanese traditional-craft site (kougeihin.jp) was down (503, also via Firecrawl), so the Miyakonojō entry uses fun-japan.jp. No Howard Hill Archery or Bear founding year added (not confirmed on a fetched page)."})
