import json, os
W='https://en.wikipedia.org/wiki/'
kayak={"n":"Kayak","a":"qajaq · canoe (UK, decked)","d":"Narrow paddle craft, usually decked, driven by a double-bladed paddle; rigid, folding or inflatable.",
 "t":["sea kayak","whitewater kayak (playboat, creekboat, river-runner)","recreational kayak","sit-on-top","fishing kayak","tandem","inflatable (incl. drop-stitch)","folding","skin-on-frame","polyethylene","fibreglass","carbon-Kevlar","wooden (plywood, strip)"],
 "s":"https://buyersguide.paddlingmag.com/brand/wilderness-systems/product/61-14-pungo-120",
 "x":[
  {"n":"Baidarka","a":"Aleutian kayak · iqyax̂","d":"Aleut skin-on-frame kayak with a forked bow and flexible driftwood frame, built with one, two or three cockpits.","mk":"","y":"pre-contact; three-hole form 18th–19th c.","s":W+"Baidarka",
   "v":[{"n":"one-hole","mk":"","y":"pre-Russian","d":"single paddler, the common early form"},{"n":"two-hole","mk":"","y":"pre-Russian","d":"less common early form"},{"n":"three-hole","mk":"","y":"Russian period","d":"developed under Russian fur-hunting influence"},{"n":"modern revival","mk":"","y":"20th c.","d":"aluminium frame and PVC skin; revival credited to George Dyson"}],
   "dt":"cockpits 1–3 · frame driftwood/bone or aluminium · skin sea-lion hide or PVC"},
  {"n":"Greenland kayak","a":"Greenland qajaq","d":"Inuit hunting kayak with few chines, angular hull and gunwales rising to points at bow and stern, sized to its paddler.","mk":"","y":"traditional","s":W+"Kayak",
   "v":[{"n":"West Greenland","mk":"","y":"","d":"angular hull, raised pointed ends"},{"n":"East Greenland","mk":"","y":"","d":"snugger fit, steeper gunwale-to-stem angle for manoeuvrability"}],
   "dt":"about 5.2 m long · 51–56 cm wide · skin-on-frame or modern replica in fibreglass"},
  {"n":"Rob Roy","a":"Rob Roy canoe","d":"John MacGregor's decked canoe inspired by North American kayaks, whose published voyages launched recreational touring.","mk":"","y":"1866","s":W+"Sea_kayak","v":[],"dt":"decked · wooden"},
  {"n":"Klepper folding kayak","a":"Klepper Faltboot · Aerius","d":"German wooden-framed, fabric-skinned folding kayak that made the foldboat a commercial success.","mk":"Klepper","y":"1906","s":W+"Folding_kayak",
   "v":[{"n":"Delphin (precursor)","mk":"","y":"1905","d":"Alfred Heurich's bamboo-framed prototype, patented 1906"},{"n":"Faltboot","mk":"Klepper","y":"1906","d":"first Klepper folding boat, Rosenheim"},{"n":"Aerius I","mk":"Klepper","y":"","d":"single-seater used in early whitewater kayaking"},{"n":"Aerius II","mk":"Klepper","y":"1951","d":"double; Hannes Lindemann crossed the Atlantic in one in 1956"},{"n":"Quattro","mk":"Klepper","y":"","d":"up to four air sponsons"}],
   "dt":"frame wood or aluminium · hull Hypalon or PVC · deck cotton/hemp · single or double"},
  {"n":"Cockle","a":"Cockle Mk II","d":"British Second World War commando folding kayak series, used in the 1942 Bordeaux raid; collected as militaria-linked boats.","mk":"","y":"1942","s":W+"Folding_kayak",
   "v":[{"n":"Mk 1","mk":"","y":"","d":"used in Operation Jaywick"},{"n":"Mk II","mk":"","y":"1942","d":"used in Operation Frankton"}],"dt":"folding · two-seat"},
  {"n":"Perception rotomoulded kayak","a":"Perception","d":"Polyethylene kayak made by rotational moulding, which cut the cost and upkeep of kayaks and reshaped the market.","mk":"Perception","y":"1970s","s":W+"Perception_Kayaks","v":[],"dt":"polyethylene · whitewater, recreational, sit-on-top"},
  {"n":"Oru origami kayak","a":"Oru","d":"Folding kayak made from a single creased sheet of corrugated plastic, 9 to 16 feet long.","mk":"Oru Kayak","y":"","s":W+"Folding_kayak","v":[],"dt":"length 9–16 ft · corrugated polypropylene"}],
 "m":[["Pungo","Wilderness Systems"],["Recon","Wilderness Systems"],["Targa","Wilderness Systems"],["Puffin","Pakboats"]]}
canoe={"n":"Canoe","a":"open canoe · Canadian canoe","d":"Open paddle craft driven by a single-bladed paddle, kneeling or seated.",
 "t":["tripping","solo","tandem","whitewater","freight/square-stern","birch-bark","dugout","wood-canvas","cedar-strip","aluminium","Royalex","polyethylene","fibreglass/Kevlar"],
 "s":"https://buyersguide.paddlingmag.com/product/11-9-discovery-158",
 "x":[
  {"n":"Birch-bark canoe","a":"birchbark canoe","d":"Indigenous canoe of eastern Canada and the north-eastern US: paper-birch bark over a cedar frame, sewn with roots and sealed with resin.","mk":"","y":"pre-contact–","s":W+"Canoe",
   "v":[{"n":"Algonquin style","mk":"","y":"1918 example","d":"light enough to carry around rapids; Minnesota Historical Society example"},{"n":"canot du maître (rabaska, Montreal canoe)","mk":"","y":"fur trade","d":"about 11 m, crews of eight to ten"},{"n":"canot du nord","mk":"","y":"fur trade","d":"about half the size, portaged upright by two men"},{"n":"canot léger (express canoe)","mk":"","y":"fur trade","d":"about 4.6 m, for people and news"}],
   "dt":"bark · cedar ribs and planking · spruce-root lashing · resin seams"},
  {"n":"Dugout canoe","a":"dugout · logboat","d":"Canoe carved from a single tree trunk; the oldest known boat type.","mk":"","y":"c. 8500 BC–","s":W+"Canoe",
   "v":[{"n":"Pesse canoe","mk":"","y":"c. 8200–7600 BC","d":"Netherlands find"},{"n":"Pacific Northwest cedar dugout","mk":"","y":"","d":"red or yellow cedar; incl. Quinault shovel-nose river canoe"}],"dt":"species of tree · length · carved or burnt out"},
  {"n":"Chestnut Prospector","a":"Prospector","d":"Deep, beamy wood-canvas tripping canoe with arched hull and marked rocker; its name is now generic for derivatives.","mk":"Chestnut Canoe Company","y":"","s":W+"Chestnut_Canoe_Company",
   "v":[{"n":"Prospector","mk":"Chestnut Canoe Company","y":"","d":"original wood-canvas model"},{"n":"modern Prospector derivatives","mk":"","y":"","d":"generic name for canoes based on the Chestnut model"}],"dt":"length · wood-canvas or modern composites"},
  {"n":"Chestnut Pal","a":"Pal","d":"16-foot wood-canvas pleasure canoe, often cited as Chestnut's most famous model.","mk":"Chestnut Canoe Company","y":"","s":W+"Chestnut_Canoe_Company",
   "v":[{"n":"Chum (Twozer, Gooseberry)","mk":"Chestnut Canoe Company","y":"","d":"15-foot sister model popular with solo paddlers"},{"n":"Cruiser","mk":"Chestnut Canoe Company","y":"","d":"narrower, faster lines"}],"dt":"15–16 ft · wood-canvas"},
  {"n":"Old Town wood-canvas canoe","a":"Old Town","d":"Canvas-covered wooden canoe built at Old Town, Maine, since 1898, never out of production.","mk":"Old Town","y":"1898–","s":W+"Old_Town_Canoe",
   "v":[{"n":"wood-canvas","mk":"Old Town","y":"1898–","d":"original construction"},{"n":"Oltonar (Royalex)","mk":"Old Town","y":"early 1970s","d":"ABS composite hulls"},{"n":"Discovery 158","mk":"Old Town","y":"","d":"plastic tripping canoe"}],"dt":"length · wood-canvas, Royalex, polyethylene"},
  {"n":"Peterborough canoe","a":"Peterborough cedar-strip","d":"Ontario canoe of wide-board, cedar-strip and cedar-rib construction, mostly canvas-covered.","mk":"Peterborough Canoe Company","y":"1892–1961","s":W+"Peterborough_Canoe_Company","v":[],"dt":"board, strip or rib construction · varnished cedar"}],
 "m":[]}
row={"n":"Rowing boat","a":"rowboat · skiff · dinghy (rowing)","d":"Small boat driven by oars, usually from a fixed seat.",
 "t":["fixed seat","sliding seat","clinker (lapstrake)","carvel","glued plywood","fibreglass","sailing rig option"],
 "s":"https://tsca.net/gig-harbor-whitehall-for-sale/",
 "x":[
  {"n":"Whitehall","a":"Whitehall rowboat · Whitehall gig","d":"Fast lapstrake rowboat from New York Harbor with near-straight stem, full keel and wine-glass transom.","mk":"","y":"19th c.","s":W+"Whitehall_rowboat",
   "v":[{"n":"Whitehall","mk":"","y":"19th c.","d":"14–22 ft, one or two rowers"},{"n":"Whitehall gig","mk":"","y":"","d":"25 ft, four rowers and a coxswain"},{"n":"modern Whitehall","mk":"","y":"","d":"fibreglass or thermoformed plastic, fixed or sliding seat"}],"dt":"14–25 ft · wood, fibreglass, plastic · fixed or sliding seat"},
  {"n":"Thames skiff","a":"skiff · camping skiff","d":"Clinker-built wooden river rowing boat of the Thames, with thole pins and fixed thwarts.","mk":"","y":"Victorian","s":W+"Thames_skiff",
   "v":[{"n":"double skiff","mk":"","y":"","d":"24 ft lines by W.A.B. Hobbs of Henley"},{"n":"racing skiff","mk":"","y":"","d":"to Skiff Racing Association rules"},{"n":"camping skiff","mk":"","y":"","d":"canvas cover turns it into a floating tent"}],"dt":"single or double sculling · coxed multi-rower · optional sail"},
  {"n":"Dory","a":"banks dory · Swampscott dory · drift boat","d":"Flat-bottomed, double-ended small boat of North Atlantic fisheries, adapted for beaches and rivers.","mk":"","y":"18th c.–","s":W+"Dory_(boat)",
   "v":[{"n":"Banks dory","mk":"","y":"1850s","d":"stackable Grand Banks fishing dory"},{"n":"Swampscott dory","mk":"","y":"","d":"beach-launched inshore variant"},{"n":"McKenzie River drift boat","mk":"","y":"","d":"river and rapids adaptation"}],"dt":"length · wooden or modern construction"},
  {"n":"Punt","a":"Thames punt · Cambridge punt","d":"Flat-bottomed, square-ended river boat pushed with a pole; a leisure boat of the Thames, Cam and Cherwell.","mk":"","y":"c. 1860–","s":W+"Punt_(boat)",
   "v":[{"n":"pleasure punt","mk":"","y":"c. 1860–1880","d":"about 24 ft by 3 ft"},{"n":"racing punt","mk":"","y":"","d":"narrower, incl. single-seater"}],"dt":"hardwood sides · teak treads · 12–16 ft pole"}],
 "m":[]}
raft={"n":"River raft","a":"whitewater raft · inflatable raft","d":"Inflatable open boat of large tubes, paddled or rowed by a group, made for whitewater rivers.",
 "t":["paddle raft","oar rig","self-bailing","catamaran","PVC","urethane","rubber"],
 "s":"https://coloradokayak.com/collections/rafts",
 "x":[{"n":"Packraft","a":"trail boat","d":"Small, portable inflatable boat, usually under 4 kg, carried on foot for river and coastal trips.","mk":"","y":"1952–","s":W+"Packraft",
   "v":[{"n":"Scout","mk":"Alpacka","y":"","d":"1.6 kg"},{"n":"Canyon","mk":"Supai","y":"","d":"0.68 kg"},{"n":"Recon Self-Bailing","mk":"Kokopelli","y":"","d":"7.2 kg"}],"dt":"weight · self-bailing or closed deck · spray deck"}],
 "m":[["Cub","AIRE"],["Puma","AIRE"],["Tributary HD","AIRE"],["ARK","Badfish"],["MAX","Hyside"],["Otter","NRS"],["PAC","Outcast"]]}
shell={"n":"Rowing shell","a":"racing shell · scull · sweep boat","d":"Long narrow racing boat rowed with oars on sliding seats.",
 "t":["single scull (1x)","double (2x)","quad (4x)","octuple (8x+)","pair (2- / 2+)","four (4- / 4+)","eight (8+)","coastal/touring shell","carbon-honeycomb","wooden"],
 "s":"https://www.nauticexpo.com/prod/filippi/product-22350-230212.html",
 "x":[
  {"n":"Empacher racing shell","a":"Empacher","d":"German racing shell built at Eberbach in every international class; pioneer of the plastic shell.","mk":"Empacher","y":"1952–","s":W+"Empacher",
   "v":[{"n":"first plastic shell","mk":"Empacher","y":"1956","d":"developed with BASF"},{"n":"Munich gold boat","mk":"Empacher","y":"1972","d":"plastic boat won Olympic gold"}],"dt":"class · rigger · carbon-honeycomb"},
  {"n":"Filippi racing shell","a":"Filippi","d":"Italian blue-and-white carbon-honeycomb racing shell from Donoratico, with hundreds of championship medals.","mk":"Filippi","y":"1980–","s":W+"Filippi_Boats",
   "v":[{"n":"F14","mk":"Filippi","y":"","d":"model from old data"}],"dt":"class · carbon-honeycomb sandwich"}],
 "m":[]}
pedal={"n":"Pedal boat","a":"pedalo · paddle boat","d":"Small boat driven by pedals turning a paddle wheel or propeller.",
 "t":["two-seat","four-seat","paddle wheel","propeller","with slide","themed (swan, car, animal)"],
 "s":"https://www.nauticexpo.com/product-manufacturer/la-noria-pedal-boat-17097-11885.html",
 "x":[{"n":"Swan pedalo","a":"swan boat","d":"Pedalo with a swan-shaped body, a fixture of park lakes.","mk":"","y":"","s":W+"Pedalo",
   "v":[{"n":"Gran Cisne","mk":"Aventuras Acuaticas La Noria","y":"","d":"swan model"}],"dt":"seats · paddle wheel"}],
 "m":[["Hidrobeetle","Aventuras Acuaticas La Noria"],["Gran Caballito de Mar","Aventuras Acuaticas La Noria"]]}
K='knowledge'
brands=[
 {"n":"Old Town","c":"United States","f":"1898","seg":"canoes and kayaks","d":"Maine canoe maker begun by the Gray brothers; owned by Johnson Outdoors since 2004.","lines":[],"eras":["Gray family, 1898–1974","S.C. Johnson, 1974–2004","Johnson Outdoors, 2004–"],"sig":["Old Town wood-canvas canoe"],"sc":[],"rel":[],"s":W+"Old_Town_Canoe"},
 {"n":"Chestnut Canoe Company","c":"Canada","f":"late 19th century","seg":"wood-canvas canoes (defunct)","d":"Fredericton, New Brunswick, maker of wood-canvas canoes, closed 1978–79.","lines":[],"eras":[],"sig":["Chestnut Prospector","Chestnut Pal"],"sc":[],"rel":["Peterborough Canoe Company"],"s":W+"Chestnut_Canoe_Company"},
 {"n":"Peterborough Canoe Company","c":"Canada","f":"1892","seg":"wooden canoes (defunct)","d":"Peterborough, Ontario, maker of board, cedar-strip and rib canoes until 1961.","lines":[],"eras":[],"sig":["Peterborough canoe"],"sc":[],"rel":["Chestnut Canoe Company"],"s":W+"Peterborough_Canoe_Company"},
 {"n":"Klepper","c":"Germany","f":"1906","seg":"folding kayaks","d":"Rosenheim maker that made the folding kayak a commercial success.","lines":["Aerius"],"eras":[],"sig":["Klepper folding kayak"],"sc":[],"rel":[],"s":W+"Folding_kayak"},
 {"n":"Perception","c":"United States","f":"1970s","seg":"plastic kayaks","d":"Kayak brand founded by Bill Masters that developed rotomoulded plastic kayaks; part of Confluence, now Pelican.","lines":[],"eras":[],"sig":["Perception rotomoulded kayak"],"sc":[],"rel":["Wilderness Systems"],"s":W+"Perception_Kayaks"},
 {"n":"Wilderness Systems","c":"United States","f":"1986","seg":"recreational and touring kayaks","d":"Kayak brand founded by Andy Zimmerman and John Sheppard; merged into Confluence in 1998.","lines":["Pungo","Tarpon"],"eras":[],"sig":[],"sc":[],"rel":["Perception"],"s":W+"Perception_Kayaks"},
 {"n":"Oru Kayak","c":"United States","f":"","seg":"folding kayaks","d":"Maker of origami-style folding kayaks from corrugated plastic.","lines":[],"eras":[],"sig":["Oru origami kayak"],"sc":[],"rel":[],"s":W+"Folding_kayak"},
 {"n":"Empacher","c":"Germany","f":"1923","seg":"racing shells","d":"Eberbach boatbuilder, rowing shells since 1952; boats won 10 of 14 golds at London 2012.","lines":[],"eras":["Willy Empacher, 1923–","Hans Empacher, 1970–","Helmut Empacher, 2018–"],"sig":["Empacher racing shell"],"sc":[],"rel":["Filippi"],"s":W+"Empacher"},
 {"n":"Filippi","c":"Italy","f":"1980","seg":"racing shells","d":"Donoratico boatyard founded by Lido Filippi, run by his son David.","lines":[],"eras":[],"sig":["Filippi racing shell"],"sc":[],"rel":["Empacher"],"s":W+"Filippi_Boats"},
]
# fix: Tarpon not sourced -> drop
brands[5]["lines"]=["Pungo"]
trads=[
 {"n":"Birch-bark canoe building","g":"Woodwork & furniture","r":"Eastern Canada and north-eastern United States","p":"pre-contact to present","d":"Indigenous craft of building canoes from paper-birch bark over a cedar frame, later adopted for the fur trade.","tech":"bark sewn with split roots over cedar ribs and planking; seams sealed with resin","mat":"paper birch bark, cedar, spruce root, resin","forms":["Birch-bark canoe","canot du maître","canot du nord"],"ctr":["Algonquin and Ojibwe builders"],"auth":"","s":W+"Canoe"},
 {"n":"Greenland kayak","g":"Woodwork & furniture","r":"Greenland","p":"traditional; living sport","d":"Inuit skin-on-frame hunting kayak and its rolling skills, kept alive by the Greenland Kayaking Championships with 35 rolls and manoeuvres.","tech":"skin-on-frame hull sized to the paddler; rolling","mat":"wood frame, sealskin or fabric skin","forms":["Greenland kayak"],"ctr":["West Greenland","East Greenland"],"auth":"","s":W+"Kayak_roll"},
 {"n":"Aleut baidarka","g":"Woodwork & furniture","r":"Aleutian Islands","p":"pre-contact; 20th-century revival","d":"Aleut skin-on-frame kayak with forked bow, lashed driftwood frame and sea-lion skin sewn by women.","tech":"sinew-lashed flexible frame; waterproof-stitched skin","mat":"driftwood, bone, sinew, sea-lion skin","forms":["Baidarka"],"ctr":["George Dyson (revival)","David Zimmerly (documentation)"],"auth":"","s":W+"Baidarka"},
]
out={"kinds":[kayak,canoe,row,raft,shell,pedal],"brands":brands,"traditions":trads,
 "notes":"Kept all six planned kinds. Dropped from m: La Noria Gran Cisne folded into Swan pedalo; Gran Tucán and Gran Unicornio cut (rental-fleet SKUs). Old Town Discovery 158 moved to a version of the Old Town archetype. Wilderness Systems Pungo/Recon/Targa kept in m (paddlingmag page blocked, could not build an archetype). Not attested so left out: Swan Boats of Boston (rides, not owned), Mad River, Dagger, Hudson/Vespoli/Stämpfli shells (named on Racing shell page but no archetype facts), Grumman aluminium canoe (no page retrieved), Valley Nordkapp. AIRE/NRS rafts kept as old models; no raft brand entries."}
p='work/G1/shelves/06_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
