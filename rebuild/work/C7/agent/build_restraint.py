import json, os, sys
OUT = '/home/user/Possession-Taxonomy/rebuild/work/C7/shelves'
def K(n, d, s=None, a='', t=None, m=None, r=None):
    k = {'n': n, 'a': a, 'd': d}
    if t: k['t'] = t
    if s: k['s'] = s
    if m: k['m'] = m
    if r: k['r'] = r
    return k
J = {}
J['00_01'] = ([
 K('Row-crop tractor', 'Wheeled tractor with adjustable track and clearance for working between crop rows.',
   'https://koenigequipment.com/john-deere/agricultural-solutions/tractors/row-crop-tractors',
   t=['two-wheel drive', 'mechanical front-wheel drive'], r=[['8 Series (8R, 8RT, 8RX)', 'John Deere']]),
 K('Articulated 4WD tractor', 'Large tractor with four equal driven wheels that steers by bending at a central pivot.',
   'https://koenigequipment.com/john-deere/agricultural-solutions/tractors/4wd-track-tractors', a='articulated four-wheel-drive tractor',
   r=[['9 Series (9R, 9RT, 9RX)', 'John Deere'], ['STX Steiger', 'Case IH']]),
 K('Crawler tractor', 'Tractor running on two full-length tracks, steel or rubber, instead of wheels.',
   'https://kellytractor.com/eng/products/agriculture/rubberbelted_tractors.aspx', a='full-track tractor',
   t=['rubber-belted', 'steel-tracked'], m=[['MT700C', 'Challenger'], ['MT800C', 'Challenger'], ['8RT', 'John Deere'], ['9RT', 'John Deere']]),
 K('Four-track tractor', 'Tractor running on four separate track units, one at each corner, on an articulated or rigid frame.',
   'https://koenigequipment.com/john-deere/agricultural-solutions/tractors/4wd-track-tractors',
   t=['articulated frame', 'rigid frame'], m=[['Quadtrac', 'Case IH'], ['Xerion 4500 TRAC TS', 'Claas'], ['8RX', 'John Deere'], ['9RX', 'John Deere']]),
 K('Half-track tractor', 'Tractor with front tyres and rear crawler tracks.',
   'https://www.yanmar.com/jp/agri/products/tractor/series_lineup/', a='delta tractor'),
], 'Restraint only. Dropped the duplicate John Deere 8R model in Row-crop (range kept) and the second Xerion size; the 8 and 9 Series ranges are kept once each (on Row-crop and Articulated) rather than repeated on every kind. Drive and track layouts moved to types.')

J['00_02'] = ([
 K('Orchard and vineyard tractor', 'Wheeled tractor with a narrow track and low profile for working between vines and fruit trees.',
   'https://www.fendt.com/us/products/tractors/fendt-200-vfp-vario', a='narrow tractor · tracteur fruitier · tracteur vigneron · Schmalspurtraktor',
   t=['vineyard (V)', 'orchard (F)', 'plantation (P)'], m=[['200 F Vario', 'Fendt'], ['200 P Vario', 'Fendt'], ['200 V Vario', 'Fendt']]),
 K('High-clearance tractor', 'Tractor with high ground clearance that straddles rows of vines or crops.',
   'https://www.pellenc.com/en-gb/our-products/from-the-vineyard-to-the-winery/vine-growing/straddle-and-multifunction-tractor/straddle-tractor-345',
   a='straddle tractor · enjambeur', r=[['OPTIMUM', 'Pellenc']]),
 K('Slope tractor', 'Low, wide tractor with a low centre of gravity that carries mowers and implements on steep ground.',
   'https://www.landwirt.com/traktoren/maeh-und-bergtraks/sonstige', a='mower-carrier tractor · Mähtrak · Bergtrak',
   r=[['Terratrac', 'Aebi Schmidt'], ['Metrac', 'Reform']]),
 K('Forestry tractor', 'Wheeled tractor built and guarded for forest work such as winching and skidding; also shown under Forestry.',
   'https://www.landwirt.com/en/tractors/forestry-tractors/country-austria', a='tracteur forestier · Forsttraktor'),
 K('Implement carrier', 'Self-propelled carrier that carries and drives implements, with no load body; a Unimog with a load bed is in Vehicles.',
   'https://aebi-schmidt.com/en/products/aebi/slope-tractors/tt-small', a='tool-carrier tractor'),
], 'Restraint only. Pellenc OPTIMUM numbers cut to the OPTIMUM range; Aebi Schmidt Terratrac sizes and Reform Metrac models cut to their ranges (names taken from the old model list). Fendt 200 V/F/P kept as the three narrow-tractor forms and mirrored as types.')

J['02_00'] = ([
 K('Mouldboard plough', 'Plough whose curved mouldboards cut and turn the soil over.',
   'https://www.landwirt.com/en/soil-tillage-equipment/ploughs', t=['mounted', 'semi-mounted', 'reversible', 'conventional'],
   m=[['Juwel', 'Lemken'], ['Vari-Diamant', 'Lemken'], ['2300S Variomat', 'Kverneland'], ['Multi-Master', 'Kuhn'], ['Varimaster', 'Kuhn'], ['Cayros', 'Amazone'], ['Teres', 'Amazone'], ['Servo', 'Poettinger']]),
 K('Chisel and tine cultivator', 'Implement with rigid or sprung tines that loosens the soil without turning it.',
   'https://www.landwirt.com/en/soil-tillage-equipment/cultivators', t=['rigid tine', 'spring tine'],
   m=[['Kristall', 'Lemken'], ['Cenius', 'Amazone'], ['Cenio', 'Amazone'], ['Terrano', 'Horsch'], ['Vibrostar', 'Einbock']]),
 K('Subsoiler', 'Implement with heavy legs that break compacted layers below plough depth.',
   'https://www.landwirt.com/en/soil-tillage-equipment/subsoilers', a='deep ripper', m=[['Culter', 'Imants'], ['Attila', 'Maschio Gaspardo']]),
 K('Spading machine', 'PTO-driven implement whose spades dig and turn the soil.',
   'https://www.agriexpo.online/prod/imants-b-v/product-169346-6346.html', r=[['SX', 'Imants']]),
], 'Restraint only. Kept one or two lines per market-covering maker; dropped Einbock Hurricane and Taifun (third and fourth Einbock lines). Imants 38SX/48SX/58SX sizes cut to the SX range.')

J['02_01'] = ([
 K('Disc harrow', 'Implement with gangs of concave discs that cut and mix the surface soil.',
   'https://www.landwirt.com/en/soil-tillage-equipment/harrows', t=['compact disc', 'tandem disc'], m=[['Catros', 'Amazone']]),
 K('Power harrow', 'PTO-driven harrow whose rotating vertical tines break clods into a seedbed.',
   'https://www.landwirt.com/en/soil-tillage-equipment/harrows', m=[['HRB', 'Kuhn'], ['Zirkon', 'Lemken']]),
 K('Rotary tiller', 'PTO-driven implement whose blades on a horizontal rotor churn the soil.',
   'https://www.landwirt.com/en/soil-tillage-equipment/rotary-cultivators', a='rotavator', m=[['FPG', 'Vigolo']]),
 K('Land roller', 'Roller or packer that firms and levels the soil surface.',
   'https://www.landwirt.com/en/soil-tillage-equipment/rollers', a='packer', t=['flat roller', 'ring roller', 'packer']),
 K('Seedbed combination', 'Implement that combines tines, levelling bars and rollers to make a seedbed in one pass.',
   'https://lemken.com/en-en/agricultural-machines/soil-cultivation/seedbed-preparation/seedbed-combinations',
   m=[['Korund 8', 'Lemken'], ['System-Kompaktor', 'Lemken']]),
 K('Puddling harrow', 'Implement that churns flooded paddy soil into a puddle before transplanting.',
   'https://tractorkarvan.com/index.php/implement/shaktiman-rice-puddler-srt-8', a='rice paddy harrow',
   m=[['GreenSystem Puddler Leveler', 'John Deere'], ['Oryza 300', 'Maschio Gaspardo'], ['Paddy 165', 'Maschio Gaspardo'], ['Rice Puddler SRT-8', 'Shaktiman']]),
], 'Restraint only. Catros+ folded into Catros (same line). Puddling harrow kept for paddy users. Roller forms as types.')

J['02_02'] = ([
 K('Box blade', 'Tractor-mounted open box with a blade and scarifier teeth for grading and moving soil.',
   'https://masontractor.com/new-products/land-pride/Dirtworking/BB12-Series-Box-Scrapers/BB1260', a='box scraper',
   r=[['BB12 Series box scraper', 'Land Pride']]),
 K('Rear grader blade', 'Rear-mounted blade or levelling frame for grading, levelling and ditching.',
   'https://www.tractorsupply.com/tsc/catalog/blades-scrapers', a='land leveller'),
 K('Post-hole auger', 'Tractor-driven auger that bores holes for posts and planting.',
   'https://kubota.com.au/product/post-hole-digger-pd10-25-35-series', a='post-hole digger', r=[['PD10, PD25 and PD35 series', 'Land Pride']]),
 K('Trencher', 'Tractor-driven implement that cuts narrow trenches.',
   'https://www.evergladesfarmequipment.com/paladin-attachments/construction/implements/trenchers-model-612', m=[['612 Trencher', 'Bradco']]),
 K('Stone picker', 'Tractor implement that lifts stones from a field and collects them in a hopper or windrows them for removal.',
   'https://www.landwirt.com/en/soil-tillage-equipment?page=88', a='stone picker and collector', t=['stone picker', 'stone windrower']),
 K('Tractor snow blade and blower', 'Snow blade or blower mounted on or driven from a tractor.',
   'https://deere.com/en/attachments-accessories-and-implements/utility-tractors-attachments-accessories/snow-removal-equipment',
   a='tractor snow blade · tractor snow blower', t=['snow blade', 'snow blower'], m=[['SB1164P', 'Frontier'], ['SB1174', 'Frontier']]),
 K('Bund plasterer', 'Implement that forms and smooths the earth bunds round paddy fields.',
   'https://jmty.jp/miyazaki/sale-oth/article-1qjsx3', a='rice paddy bund plasterer', m=[['AR750S', 'Kobashi']]),
], 'Restraint only. Kinds kept at kind level; Land Pride post-hole digger sizes grouped as one range; old names "Stone picker and collector" and "Snow blade and blower" renamed to the planned names (old names kept as aliases).')

J['03_00'] = ([
 K('Seed drill', 'Implement that sows seed in rows at a set rate and depth.',
   'https://www.truckscout24.com/agricultural-machines/used/seeders', t=['tine coulter', 'disc coulter', 'no-till'],
   m=[['Pronto', 'Horsch'], ['Venta', 'Kuhn'], ['Solitair', 'Lemken'], ['Rapid', 'Vaderstad']]),
 K('Single-seed planter', 'Planter that places single seeds at a set spacing in the row.',
   'https://www.profi.co.uk/test-centre/four-precision-planters-with-front-hoppers-part-2-pressure-is-on/', a='precision planter',
   m=[['Precea', 'Amazone'], ['Maestro', 'Horsch'], ['Optima', 'Kverneland'], ['Tempo', 'Vaderstad']]),
 K('Transplanter', 'Implement that sets seedlings or young plants into the field.',
   'https://www.duijndam-machines.com/en/machines/309267/checchi-magli-tex-carousel-planting-machine-2-rows', m=[['TEX', 'Checchi & Magli']]),
 K('Rice transplanter', 'Machine that plants rice seedlings into a flooded paddy, usually four to eight rows at a time.',
   'https://yanmar.com/global/agri/rice_transplanter', t=['walk-behind', 'ride-on']),
 K('Potato planter', 'Implement that plants seed potatoes in ridges.',
   'https://products.grimme.com/en/p/gl-420', r=[['GL', 'Grimme']], m=[['PRIOS 440', 'Grimme'], ['Next Structural', 'Dewulf']]),
 K('Seed potato cutter', 'Machine that cuts seed potatoes into planting pieces before planting.',
   'https://www.dewulfgroup.com/en/used-machines/'),
], 'Restraint only. Grimme GL 32 B / GL 410 / GL 420 cut to the GL range. Coulter forms as types; rice transplanter types walk-behind and ride-on.')

J['03_01'] = ([
 K('Fertiliser spreader', 'Implement that broadcasts or places granular fertiliser.',
   'https://www.fwi.co.uk/machinery/fertiliser-spreader-test-kuhn-axis', t=['twin-disc', 'pneumatic boom'],
   m=[['Axis', 'Rauch'], ['ZA-M', 'Amazone'], ['ZA-V', 'Amazone']]),
 K('Manure spreader', 'Wagon that shreds and spreads solid manure.',
   'https://agdealer.com/listings/manufacturer/kuhn-knight/category/applicators/subcategory/manure-spreaders',
   t=['vertical beater', 'horizontal beater', 'side discharge'], m=[['PS-270', 'Kuhn'], ['SLC150', 'Kuhn']]),
 K('Slurry tanker', 'Tank that carries and spreads liquid slurry.',
   'https://swedish-agro-machinery.mynewsdesk.com/pressreleases/samson-introduces-new-slurry-tanker-series-2940955',
   m=[['PG II', 'Samson Agro'], ['TG', 'Samson Agro']]),
 K('Slurry injector', 'Implement that places slurry into the soil.',
   'https://www.agriexpo.online/product-manufacturer/filesan-mounted-slurry-incorporator-1208-5028.html', t=['disc injector', 'tine injector'],
   m=[['Terradisc2', 'Joskin'], ['Solodisc', 'Joskin'], ['Terraflex/2', 'Joskin']]),
 K('Crop sprayer', 'Sprayer that applies crop-protection liquids through a boom.',
   'https://www.tractorhouse.com/listing/for-sale/257444019/2023-amazone-ux-5201-super-pull-type-sprayers',
   t=['mounted', 'trailed', 'self-propelled'], m=[['UX 5201 Super', 'Amazone']]),
 K('Inter-row hoe and tine weeder', 'Implement that weeds mechanically between and within crop rows.',
   'https://www.einboeck.at/en/tined-weeders-and-row-crop-cultivators/', a='inter-row hoe · tine weeder',
   t=['tine weeder', 'inter-row hoe'], r=[['AEROSTAR', 'Einbock'], ['CHOPSTAR', 'Einbock']]),
], 'Restraint only. Dropped the bare Kuhn "8132" number and Joskin Multi-Action; old "Inter-row hoe" renamed to the planned name.')

J['03_02'] = ([
 K('Centre-pivot and linear irrigator', 'Self-moving span of sprinkler pipe that irrigates a field in a circle or a strip.',
   'https://www.valleyirrigation.com/8000', a='centre-pivot irrigator · linear-move irrigation machine', t=['centre pivot', 'linear move'],
   m=[['8000 Series', 'Valley Irrigation'], ['7000 Series', 'Valley Irrigation'], ['Rainger Linear', 'Valley Irrigation']]),
 K('Irrigation reel', 'Hose reel and field sprinkler gun for irrigating field crops.',
   'https://portal.bauer-at.com/cn/products/irrigation/rainstar', a='hose reel irrigator · sprinkler set', r=[['Rainstar', 'Bauer']]),
 K('Irrigation pump', 'Pump that moves water for field irrigation.',
   'https://vandenbussche.com/ag/product/p-t-o-rovatti-pumps', a='field irrigation pump', t=['PTO-driven', 'engine-driven', 'electric'],
   m=[['MEC D2/80', 'Caprari'], ['T3-110E', 'Rovatti']]),
], 'Restraint only. Valley Two Wheel Linear folded into Rainger Linear entry; Rovatti T1-50E dropped (second size).')

J['04_00'] = ([
 K('Combine harvester', 'Self-propelled machine that reaps, threshes and cleans grain.',
   'https://www.landwirt.com/en/harvesting-equipment-crop-fields/combine-harvesters', a='moissonneuse-batteuse · Mähdrescher · colheitadeira',
   t=['conventional (straw walker)', 'axial rotor', 'hybrid', 'head-feeding'],
   r=[['Lexion', 'Claas']], m=[['S780', 'John Deere'], ['Axial-Flow 6150', 'Case IH'], ['CR9090', 'New Holland']]),
 K('Combine header', 'Interchangeable front cutting or pick-up unit for a combine harvester.',
   'https://www.allmachines.com/combine-headers/view-all?q=CONVIO', a='plataforma colheitadeira',
   t=['grain header', 'draper header', 'corn header', 'pick-up header'],
   m=[['Convio', 'Claas'], ['FD230', 'MacDon'], ['Patriot NorthStar', 'Geringhoff']]),
 K('Forage harvester', 'Machine that cuts and chops forage crops for silage.',
   'https://www.allmachines.com/directory/forage-harvesters/C', a='ensileuse', t=['self-propelled', 'trailed'],
   r=[['Jaguar', 'Claas'], ['9000 Series forage harvesters', 'John Deere'], ['BiG X', 'Krone']]),
], 'Restraint only. Krone BiG X moved from models to ranges. Threshing systems and header forms as types.')

J['04_01'] = ([
 K('Potato harvester', 'Machine that lifts potatoes and separates them from soil and haulm.',
   'https://www.landwirt.com/en/potato-technology/potato-harvesters?page=2', t=['trailed', 'self-propelled'],
   m=[['EVO 280', 'Grimme'], ['SE 150-60', 'Grimme'], ['Enduro', 'Dewulf'], ['Kwatro', 'Dewulf'], ['Keiler 2', 'ROPA Fahrzeug- und Maschinenbau']]),
 K('Sugar-beet harvester', 'Machine that tops, lifts and cleans sugar or fodder beet.',
   'https://www.agriexpo.online/agricultural-manufacturer/beet-harvester-1946.html', t=['self-propelled', 'trailed'],
   m=[['Euro-Tiger V8-4', 'ROPA Fahrzeug- und Maschinenbau'], ['Terra Dos T4-40', 'Holmer Maschinenbau'], ['Maxtron 620', 'Grimme'], ['BM 300', 'Grimme']]),
 K('Carrot harvester', 'Machine that lifts carrots by their tops.',
   'https://www.truckscout24.com/agricultural-machines/used/harvesting-beet'),
 K('Grape harvester', 'Machine that straddles vine rows and shakes off the grapes.',
   'https://agriculture.newholland.com/en-nz/oceania/products/grape-harvesters/braud-grape-harvester',
   t=['self-propelled', 'trailed'], r=[['Braud', 'New Holland'], ['OPTIMUM', 'Pellenc']]),
], 'Restraint only. New Holland Braud 9000L / 9090X cut to the Braud range.')

J['04_02'] = ([
 K('Grain auger and conveyor', 'Auger, belt, chain or bucket elevator that moves grain into bins, dryers or trailers.',
   'https://grainsupply.com/product-category/grain-handling', a='grain leg',
   t=['tube auger', 'belt conveyor', 'chain conveyor', 'bucket elevator (grain leg)'],
   m=[['Batco 1590SA', 'Batco'], ['Brandt 1535', 'Brandt'], ['Convey-All 1650TL', 'Convey-All'], ['Hutchinson HCX2 1515LP', 'Hutchinson'], ['Kwik-Belt 1838', 'Norwood Kwik-Belt'], ['USC FL7540', 'USC'], ['KSI 161237', 'KSI']]),
 K('Grain dryer', 'Installation that dries harvested grain.',
   'https://www.grainsystems.com/na/en/products/conditioning/continuous-flow-dryers/', t=['tower', 'mixed-flow', 'batch'],
   r=[['T-Series tower dryers', 'GSI'], ['Modular tower dryers', 'GSI'], ['SUPERB SQ Series dryers', 'Brock Grain Systems']],
   m=[['Brock VECTOR Mixed Flow Dryer', 'Brock Grain Systems']]),
 K('Grain cleaner', 'Machine that separates grain from chaff, weed seed and dirt.',
   'https://www.feedandgrain.com/directory/grain-cleaning-testing-analysis/product/15391133/grain-cleaning-llc-scalper',
   m=[['Grain Cleaning LLC Scalper', 'Grain Cleaning LLC']]),
 K('Rice huller', 'Machine that removes the husk from paddy rice.',
   'https://directindustry.com/prod/satake/product-211643-2195061.html', m=[['Satake HR10FH', 'Satake'], ['Satake HR10DDF-T', 'Satake']]),
], 'Restraint only. Merged Grain auger, Belt and chain grain conveyor and Grain bucket elevator into one kind with types; the 13-SKU conveyor list cut to one model per maker (7 makers). Dropped GSI Quiet Dryer and Zimmerman (kept GSI tower ranges).')

J['05_00'] = ([
 K('Disc mower', 'Mower whose rotating discs or drums cut grass for hay or silage.',
   'https://www.kuhn.com/en/hay-forage/mowers/disc-mowers', a='drum mower', t=['disc', 'drum', 'with conditioner', 'front-mounted', 'rear-mounted', 'trailed'],
   r=[['GMD disc mowers', 'Kuhn'], ['PZ drum mowers', 'Kuhn'], ['EasyCut disc mowers', 'Krone']]),
 K('Rotary cutter', 'Implement whose blades on a vertical shaft cut grass, weeds and brush under a deck.',
   'https://www.goodworkstractors.com/product-category/attachments/mowers/', a='brush hog', t=['single-spindle', 'flex-wing'],
   r=[['Flex-wing rotary cutters', 'Bush Hog']], m=[['Bush Hog 2215', 'Bush Hog']]),
 K('Flail mower', 'Implement that cuts and shreds standing vegetation on grassland, verges, vineyards and scrub.',
   'https://bushhog.com/?p=9052', a='mulcher', r=[['BRC row crop flails', 'Bush Hog']]),
], 'Restraint only. The 23 Kuhn/Krone disc-mower models cut to three ranges; the nine Bush Hog rotary-cutter models cut to one example plus the flex-wing range (moved here from Flail mower, where it was misfiled). Dropped the "rotary cutter" alias from Flail mower; FW2110/FW4120 flex-wing models dropped with it.')

J['05_01'] = ([
 K('Hay tedder', 'Implement with rotating tines that spreads and turns cut grass to dry.',
   'https://www.kuhn.com/en/hay-forage/tedders', t=['mounted', 'trailed'], r=[['GF tedders', 'Kuhn'], ['Vendro tedders', 'Krone']]),
 K('Hay rake', 'Implement that gathers cut grass into windrows.',
   'https://www.kuhn.com/en/hay-forage/rakes-mergers', a='windrower', t=['rotary rake', 'wheel rake', 'belt merger'],
   r=[['GA rakes', 'Kuhn'], ['SR wheel rakes', 'Kuhn'], ['Merge Maxx belt mergers', 'Kuhn'], ['Swadro rakes', 'Krone']]),
 K('Baler', 'Machine that compresses hay or straw into round, large square or small square bales.',
   t=['round baler', 'large square baler', 'small square baler'],
   r=[['Comprima, Fortima and VariPack round balers', 'Krone'], ['BiG Pack large square balers', 'Krone']],
   m=[['VB 3200', 'Kuhn'], ['FB 3130-3135', 'Kuhn'], ['SB 1290', 'Kuhn'], ['i-BIO+', 'Kuhn'], ['Krone Bellima', 'Krone']]),
 K('Bale wrapper', 'Machine that wraps bales in stretch film for silage.',
   'https://www.kuhn.com/en/hay-forage/wrappers', t=['round-bale wrapper', 'square-bale wrapper', 'in-line wrapper'],
   r=[['RW and SW bale wrappers', 'Kuhn']], m=[['Tanco A100', 'Tanco'], ['Tanco A200', 'Tanco']]),
 K('Forage wagon', 'Wagon that picks up, cuts and carries grass or silage.',
   'https://www.poettinger.at/en_ca/Newsroom/Artikel/5805/pottinger-and-loader-wagons', a='loader wagon',
   r=[['Jumbo silage wagons', 'Pöttinger'], ['Boss loader wagons', 'Pöttinger'], ['Torro loader wagons', 'Pöttinger']],
   m=[['Krone AX 250 GD', 'Krone'], ['Krone RX 400 GD', 'Krone']]),
], 'Restraint only. Tedder and rake SKU lists cut to the existing ranges; baler type "Other balers" dropped and the misleading "big square baler" alias removed; Kuhn baler list cut to one model per baler form plus the i-BIO+ baler-wrapper. Old Baler had no source; none added (no web research on this shelf). Pöttinger Primo and Profi ranges dropped (smaller duplicates of Boss/Torro).')

J['06_00'] = ([
 K('Milking robot', 'Automatic milking system that attaches the cups and milks without a milker.',
   'https://www.gea.com/en/campaigns/dairyrobot-r9500-edition-2021/', a='automatic milking system',
   m=[['Astronaut A3 Next', 'Lely'], ['DeLaval VMS', 'DeLaval'], ['DairyRobot R9500', 'GEA']]),
 K('Milking parlour', 'Milking installation where cows stand in stalls while the milk runs through a pipeline to the dairy.',
   'https://www.truck1.co.za/agricultural-machinery/livestock-equipment/complete-delaval-pipeline-milking-system-for-2x7-milking-parlor-a10264258.html',
   a='pipeline milking installation', t=['static (herringbone, parallel)', 'rotary', 'trigon', 'polygon', 'pipeline in stalls', 'milk meter (fitting)'],
   m=[['DeLaval HB50', 'DeLaval'], ['SwingOver EuroClass 800', 'GEA'], ['DairyProQ', 'GEA'], ['Tru-Test Electronic Milk Meter', 'Tru-Test']]),
 K('Bucket milking machine', 'Portable milking unit that milks into a bucket.',
   'https://www.faie.at/en/products/dairy-farming/milking-machines-milking-buckets/bucket-milking-systems/bucket-milking-systems-for-cattle/'),
 K('Bulk milk cooling tank', 'Refrigerated tank that cools and holds the milk on the farm.',
   'https://en.paulmueller.com/milk-cooling-and-storage/milk-cooling-tanks/mueller-model-p', t=['open', 'closed'],
   r=[['Model P milk cooling tanks', 'Paul Mueller Company']], m=[['DeLaval DXCE', 'DeLaval']]),
], 'Restraint only. Pipeline milking installation and Milk meter merged into Milking parlour (types; meter kept as a fitting model). The 13 Mueller Model P/PC tank sizes cut to the Model P range; DeLaval DXCEM and older robot generations (Astronaut A3, R9000) dropped.')

J['06_01'] = ([
 K('Cattle crush', 'Crate or gate that restrains one animal for treatment.',
   'https://www.teemoreengineering.com/product-range/crushes-handling/', a='headgate · squeeze chute',
   t=['headgate only', 'full crush', 'hoof-trimming crush'],
   m=[['Clipex HDX 1500 Crush', 'Teemore Engineering'], ['Nugent Pro 2000', 'Teemore Engineering'], ['Universal Hoof Tech Crush', 'Teemore Engineering']]),
 K('Cattle race and handling system', 'Race, forcing pen or circular tub that moves and lines up cattle toward a crush.',
   'https://www.teemoreengineering.com/product-range/crushes-handling/', t=['race', 'forcing pen', 'circular tub']),
 K('Sheep handler', 'Race unit that holds, turns or sorts sheep into pens.',
   'https://www.tepari.com/uk/blog/the-difference-between-a-sheep-handler-and-an-auto-drafter', a='sheep drafter',
   t=['manual handler', 'auto handler', 'auto drafter'], r=[['Racewell sheep handling', 'Te Pari']], m=[['Combi-Clamp Sheep Handler', 'Te Pari']]),
 K('Livestock scales', 'Load bars or platform with an electronic indicator that weighs and records animals.',
   'https://www.tepari.com/us/shop/collections/livestock-weigh-scales-and-data-collectors', a='weigh-scale indicator · load bars · weigh platform',
   t=['load bars', 'platform', 'indicator'],
   m=[['Tru-Test XR5000', 'Tru-Test'], ['Tru-Test ID5000', 'Tru-Test'], ['Tru-Test MP800 Load Bars', 'Tru-Test'], ['Gallagher TW3', 'Gallagher'], ['Gallagher W1', 'Gallagher'], ['Macrostock Scale System', 'Te Pari']]),
 K('Livestock EID reader', 'Electronic ear-tag reader for animals, either a handheld stick or a fixed panel antenna on a race or crush.',
   t=['stick reader', 'panel reader'], m=[['Tru-Test XRS2i Stick Reader', 'Tru-Test'], ['Tru-Test SRS2i Stick Reader', 'Tru-Test']]),
], 'Restraint only. Scale indicator and weigh platform merged into Livestock scales; SKU lists cut (Clipex/Nugent sizes, older Tru-Test and Gallagher indicators, extra Racewell models). EID reader had no old source; none added (no web research on this shelf).')

J['06_02'] = ([
 K('Feed mixer wagon', 'Wagon that mixes and dispenses a feed ration.',
   'https://kuhn-usa.com/livestock/mixers-feeders', a='TMR mixer', t=['vertical auger', 'horizontal auger', 'reel', 'trailed', 'self-propelled'],
   r=[['TMR mixers (vertical, horizontal, reel)', 'Kuhn']], m=[['Kuhn SPW', 'Kuhn']]),
 K('Silage block cutter', 'Tractor implement that cuts and carries blocks from a silage clamp.',
   'https://cih.com.au/tractor-implements/loader-attachments/silage-handling/silage-shear-grab/', a='silage shear grab',
   m=[['Challenge Silage Shear Grab 170SS', 'Challenge Implements']]),
 K('Bedding spreader', 'Machine that spreads straw or other bedding in housing.',
   'https://www.farmersjournal.ie/teagle-to-debut-new-tomahawk-6100h-compact-straw-blower-884438', a='straw blower',
   r=[['Tomahawk straw blowers', 'Teagle']]),
], 'Restraint only. The 13 Kuhn mixer models cut to the Kuhn TMR range plus the SPW self-propelled mixer; mixer forms as types. Tomahawk 6100H folded into the Tomahawk range.')

J['06_03'] = ([
 K('Shearing machine', 'Powered machine with motor, drive and handpiece for flock-scale shearing; handpieces and comb-and-cutter sets are its spare parts.',
   'https://www.premier1supplies.com/p/heiniger-one-shearing-machine',
   t=['overhead drive', 'portable', 'handpiece (spare part)', 'comb and cutter set (spare part)'],
   r=[['EVO and ONE shearing systems', 'Heiniger'], ['ICON handpieces', 'Heiniger']]),
 K('Captive-bolt stunner', 'Tool that stuns livestock by driving a bolt into the skull.',
   'https://waltons.com/cash-special-captive-bolt-stunner-gun/', t=['penetrating', 'non-penetrating'],
   m=[['CASH Special', 'Accles & Shelvoke'], ['Schermer KR Stunner', 'Schermer']]),
], 'Restraint only. Shearing handpiece and Shearing comb and cutter merged into Shearing machine as spare-part types; Heiniger comb-and-cutter SKUs dropped. CASH Special HD/HL variants folded into CASH Special.')

J['07_01'] = ([
 K('Forest harvester', 'Self-propelled machine that fells, delimbs and cuts trees to length.',
   'https://www.mascus.com/forestry/forestry-harvesters', t=['wheeled harvester', 'tracked harvester', 'harvester head', 'harwarder', 'delimber'],
   m=[['Ponsse Ergo 8W', 'Ponsse'], ['John Deere 1270G', 'John Deere'], ['Komatsu 931.2', 'Komatsu Forest'], ['Rottne H14C', 'Rottne'], ['Eco Log 688F', 'Eco Log'], ['John Deere 3156G', 'John Deere']],
   r=[['600 Series 3 and 4 Roller', 'Waratah'], ['400 Series 4 Roller', 'Waratah'], ['200 Series 2 Roller', 'Waratah']]),
 K('Forwarder', 'Self-propelled machine that carries cut logs clear of the ground on its own load bed.',
   'https://www.mascus.com/forestry/forwarders',
   m=[['Ponsse Buffalo', 'Ponsse'], ['Ponsse Elephant King K100S', 'Ponsse'], ['John Deere 1210 G', 'John Deere'], ['John Deere 1510 G', 'John Deere'], ['Komatsu 895', 'Komatsu Forest'], ['Weiler F888', 'Weiler']]),
 K('Skidder', 'Machine that drags felled trees or logs to the roadside.',
   'https://www.mascus.com/forestry/skidders', t=['cable', 'grapple'],
   m=[['Tigercat 632H', 'Tigercat'], ['Tigercat 635H', 'Tigercat'], ['John Deere 748L-II', 'John Deere'], ['John Deere 948L', 'John Deere'], ['CAT 525C', 'Caterpillar']]),
 K('Feller buncher', 'Machine that fells trees and gathers them into bunches.',
   'https://www.tigercat.com/products/feller-bunchers', t=['drive-to-tree', 'swing-boom'],
   m=[['Tigercat 724H', 'Tigercat'], ['Tigercat 830C', 'Tigercat'], ['John Deere MH60D', 'John Deere'], ['CAT 552 Series 2', 'Caterpillar'], ['TimberPro TL775D', 'TimberPro']]),
 K('Forestry crane and grapple', 'Hydraulic jointed-boom crane or loader with grapple and rotator for lifting and loading logs.',
   'https://www.mascus.com/forestry/knuckleboom-loaders', a='knuckleboom loader · log grapple · rotator',
   t=['forwarder or trailer crane', 'knuckleboom loader', 'grapple and rotator'],
   m=[['Farmi Forest C25', 'Farmi Forest'], ['Joutsa TX900+140', 'Joutsa'], ['John Deere 2154D', 'John Deere'], ['Liebherr 580', 'Liebherr']]),
], 'Restraint only (contractor machines). Harvester head, Delimber and Harwarder merged into Forest harvester as types; the 28 Waratah head SKUs cut to the three Waratah series ranges; harwarder kept as one JD example. Forestry crane, knuckleboom loader and log grapple merged into one kind. Dropped discontinued or old-generation listings (Timberjack, Valmet, Kockums, older JD/Komatsu generations) and duplicate sizes. The old data has no family names for Ponsse/JD/Komatsu/Tigercat machines, so model examples stand in for ranges.')

J['08_00'] = ([
 K('Front-end loader', 'Loader arms and frame fitted to the front of a tractor.',
   'https://agriland.co.uk/farming-news/new-range-of-quicke-front-loaders-complemented-by-online-support-systems/', a='front loader',
   r=[['Q-series front loaders', 'Quicke']]),
 K('Loader attachment', "Tool fitted to a tractor's front loader.",
   'https://www.reviews.io/product-reviews/store/titan-attachments/132233', a='pallet forks · bucket · bale spike',
   t=['bucket', 'pallet forks', 'bale spike', 'grab'], r=[['Economy Series', 'Titan Attachments']]),
 K('Tractor tyre and wheel', 'Tyre, rim or complete tyred wheel made for a tractor.',
   'https://bigtyres.co.uk/tyres/brands/trelleborg/tm900-hp/600-70r30-trelleborg-tm900-hp-158d-155e', a='tractor tyre · tractor rim · complete wheel',
   t=['tyre', 'rim', 'complete wheel', 'dual wheel'], m=[['TM900 HP', 'Trelleborg']]),
 K('Rubber track unit', 'Rubber track system fitted to a tractor in place of wheels.',
   'https://camso.co/en/agriculture/conversion-tracks-systems', r=[['Conversion Track System', 'Camso']]),
 K('Tractor ballast weight', 'Cast-iron weights for added traction, hung on a front bracket or bolted to the wheels.',
   a='suitcase weight', t=['wheel weight', 'front ballast weight']),
 K('Guidance and auto-steer system', 'Guidance receiver, display or auto-steer kit for a tractor or farm machine.',
   'https://www.gpsworld.com/trimble-releases-display-system-for-agriculture-applications/', t=['receiver', 'display', 'auto-steer kit'],
   m=[['GFX-750', 'Trimble'], ['NAV-900', 'Trimble']]),
], 'Restraint only. Tractor tyre and Tractor rim and wheel merged into one kind; loader attachment forms as types. GFX-750 range entry dropped as duplicate of the model. Ballast weight had no old source; none added.')

only = sys.argv[1:] or list(J)
for job in only:
    kinds, notes = J[job]
    p = os.path.join(OUT, job + '.json'); tmp = p + '.tmp'
    json.dump({'kinds': kinds, 'brands': [], 'traditions': [], 'notes': notes}, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, p)
print('wrote', len(only))
