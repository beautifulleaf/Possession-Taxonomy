import sys; sys.path.insert(0,'work/C4/agent')
from rb_lib import *
PC='https://www.potterycreative.com/types-of-clay-for-pottery/'
PCR='https://potterycrafts.co.uk/collections/modelling-clays'
BM='https://www.portcitymakerspace.com/product/laguna-clay-bmix5/'
SC='https://theclaystudio.org/clay'
TT='https://www.potclays.co.uk/tools-accessories-throwing-tools/'
DC='https://diamondcoretools.com/blogs/resources/diamondcore%c2%ae-tools-meet-our-new-wood-rib-series-of-tools'
PM='https://en.wikipedia.org/wiki/Polymer_clay';SP='https://en.wikipedia.org/wiki/Sculpey';FI='https://en.wikipedia.org/wiki/Fimo';KA='https://en.wikipedia.org/wiki/Kato_polyclay'
FA='https://www.fredaldous.co.uk/collections/clay'
kinds=[
{'n':'Stoneware clay','a':'','d':'Mid-to-high-fired dense clay body.','t':['cone 5-6 mid-range','cone 10 high-fire','white','buff','speckled','grogged'],'m':[],'s':'https://seattlepotterysupply.com/pages/search-by-type',
 'x':[X('Stoneware clay body','Clay that vitrifies at about 1150 to 1275 degrees C (cone 3 to 11) and absorbs 2 to 5 percent water.','',PC,dt='firing cone · colour fired · grog · maker'),
      X('Laguna B-Mix','Laguna Clay smooth, porcelain-like stoneware body, sold as a cone 5 and a cone 10 version, cream when fired in oxidation.','Laguna Clay',BM,v=[('B-Mix 5','Laguna Clay','cone 5, light grey wet'),('B-Mix 10','Laguna Clay','cone 10')],dt='cone · fired colour'),
      X('Standard Clay stoneware','Studio-supplied stoneware, terra cotta and porcelain bodies from Standard Clay.','Standard Clay',SC,dt='cone · body type')]},
{'n':'Earthenware clay','a':'terracotta','d':'Low-fired clay body.','t':['terracotta red','white earthenware','low-fire cone 06-04'],'m':[],'s':FA,
 'x':[X('Earthenware clay body','Porous, plastic body fired from about 705 to 1160 degrees C (cone 018 to 3) that absorbs 10 to 15 percent water.','',PC,dt='firing cone · colour · grog')]},
{'n':'Porcelain clay','a':'','d':'High-fired white translucent clay body.','t':['cone 6','cone 10','casting slip','translucent'],'m':[],'s':'https://seattlepotterysupply.com/pages/search-by-type',
 'x':[X('Porcelain clay body','White, translucent body made mainly from kaolin that vitrifies near 1260 degrees C (cone 9).','',PC,dt='firing cone · translucency')]},
{'n':'Paper clay','a':'','d':'Clay body mixed with paper fibre.','t':['porcelain paper clay','grogged paper clay'],'m':[['Potterycrafts Porcelain Paper Clay','Potterycrafts']],'s':'https://potterycrafts.co.uk/products/potterycrafts-grogged-body-paper-clay'},
{'n':'Polymer clay','a':'','d':'PVC-based modelling clay hardened in a home oven.','t':['block','liquid','translucent','metallic','glitter','stone effect'],
 'm':[['Cernit Number One','Cernit'],['Liquid Sculpey','Sculpey'],['Original Sculpey','Sculpey'],['Premo Sculpey','Sculpey'],['Sculpey III','Sculpey'],['Sculpey Souffle','Sculpey'],['Super Sculpey','Sculpey'],['Fimo Effect','Staedtler'],['Fimo Professional','Staedtler'],['Fimo Soft','Staedtler']],'r':[['Fimo','Staedtler']],'s':FA,
 'x':[X('Fimo','German polymer clay first offered to dollmaker Kathe Kruse in 1939 and marketed by Eberhard Faber, now Staedtler.','Staedtler',FI,'1939',v=[('Fimo Classic','Staedtler','original formula'),('Fimo Soft','Staedtler','easier to condition')],dt='line (Classic, Soft, Effect, Professional) · colour'),
      X('Sculpey','Polyform Products polymer clay, first made in the early 1960s and sold to crafters from the late 1960s.','Polyform Products',SP,'1960s',v=[('Original Sculpey','Polyform Products'),('Super Sculpey','Polyform Products'),('Premo','Polyform Products'),('Sculpey III','Polyform Products'),('Sculpey Souffle','Polyform Products'),('Sculpey BakeShop','Polyform Products')],dt='line · firmness · colour'),
      X('Kato Polyclay','Polymer clay developed by artist Donna Kato with Van Aken International, known for strength after curing.','Van Aken International',KA,dt='cure up to 149 C · 18 colours')]},
{'n':'Air-dry clay','a':'','d':'Clay that hardens in air without firing.','t':['paper-based','stone-effect','self-hardening terracotta'],'m':[['DAS Modelling Clay','DAS'],['Darwi ROC','Darwi'],['Scola Air Drying Clay','Scola'],['Model Air','Sculpey'],['Fimo Air','Staedtler'],['Potterycrafts Earthstone Air-Drying Clay','Potterycrafts']],'r':[['Fimo','Staedtler']],'s':FA},
{'n':'Modelling clay','a':'plasticine · oil-based clay','d':'Non-hardening oil- or wax-based clay for modelling and sculpting.','t':['sulphur-free (silicone-safe)','soft','medium','hard grades'],'m':[],'s':FA,
 'x':[X('Chavant NSP','Sulphur-free oil-based sculpting clay that stays non-drying and suits silicone moulding; sold in soft, medium and hard grades.','Chavant',PCR,v=[('Soft Non Sulphurated','Chavant'),('Medium Non Sulphurated','Chavant'),('Hard Non Sulphurated','Chavant'),('Le Beau Touche','Chavant')],dt='hardness · colour')]},
{'n':'Pottery and sculpting hand tools','a':'ribs · loop tools · wire cutter · banding wheel','d':'Hand tools for shaping, trimming and finishing clay.','t':['ribs (wood, metal, silicone)','loop and ribbon tools','wire cutters','needle tools','sponges','banding wheel'],'m':[],'s':TT,
 'x':[X('Wood rib','Oiled-hardwood throwing and shaping ribs with engraved grip patterns, sold in 50, 75 and 100 mm sizes.','DiamondCore Tools',DC,dt='size · edge shape · wood'),
      X('Kemper and Mudtools throwing tools','Ribs, sponges, wire cutters and trimming tools from brands stocked as throwing tools by UK retailers.','Kemper Tools',TT,dt='tool type · material')]},
]
brands=[
B('Staedtler','Germany','1835','Mainstream','Fimo, pencils','German stationery maker of Fimo polymer clay.',s=FI,sig=['Fimo']),
B('Polyform Products','United States','','Mainstream','Sculpey','US maker of Sculpey polymer clay.',s=SP,sig=['Sculpey']),
B('Van Aken International','United States','','Specialist','Kato Polyclay','Maker of modelling compounds that developed Kato Polyclay with Donna Kato.',s=KA,sig=['Kato Polyclay']),
B('Laguna Clay','United States','','Mainstream','B-Mix','Clay maker of the B-Mix stoneware bodies.',s=BM,sig=['Laguna B-Mix']),
B('Standard Clay','United States','','Mainstream','studio clays','Maker of terra cotta, stoneware and porcelain bodies.',s=SC,sig=['Standard Clay stoneware']),
B('Chavant','United States','','Specialist','sculpting clay','Maker of oil-based modelling clays including NSP.',s=PCR,sig=['Chavant NSP']),
B('DiamondCore Tools','United States','','Specialist','ribs, tools','Pottery tool maker with a wood rib series.',s=DC,sig=['Wood rib']),
B('Kemper Tools','United States','','Specialist','pottery tools','Pottery hand-tool brand stocked in UK throwing-tool ranges.',s=TT,sig=['Kemper and Mudtools throwing tools']),
]
save('06_00',kinds,brands,[],'Kept all 8 kinds. Valentine, Potclays, Standard 266, Limoges porcelain, Newplast, Monster Clay not confirmed on fetched pages so left out; Sculpey Souffle etc. kept from old data. Founding years of Staedtler from knowledge only where given.')

MA='https://www.maycocolors.com/product-conversions/'
TN='https://en.wikipedia.org/wiki/Tenmoku';GM='https://garlandmag.com/article/eastern-glazes-the-provenance-of-celadon-tenmoku-and-shino/';KI='https://en.wikipedia.org/wiki/Kintsugi'
SG='https://seattlepotterysupply.com/pages/glaze'
kinds=[
{'n':'Glaze','a':'','d':'Glassy coating made to be fired onto ceramics.','t':['brush-on','dipping','spray','low-fire','mid-range','high-fire','food-safe'],'m':[['Stroke & Coat','Mayco']],'s':SG,
 'x':[X('Celadon','Green glaze coloured by a small amount of iron oxide in reduction firing, from China, named by seventeenth-century Europeans.','',GM,dt='iron content · firing atmosphere · body'),
      X('Tenmoku','Deep black iron glaze that breaks to ginger brown at edges, imitating Chinese Jian ware of the southern Song dynasty; oil-spot crystals form in oxidation.','',TN,v=[('Oil spot','','iron crystals at the surface')],dt='iron content · cooling rate · colour'),
      X('Shino','Japanese glaze from the sixteenth century with a satiny white to creamy surface and orange where it breaks, prized for tea wares.','',GM,dt='carbon trapping · thickness · body')]},
{'n':'Underglaze','a':'','d':'Coloured slip-based decoration applied under or without glaze.','t':['bottled','pencil','crayon','transfer'],'m':[],'s':SG},
{'n':'Wax resist','a':'','d':'Liquid wax painted on ceramics to keep glaze off.','t':['water-based','hot wax'],'m':[],'s':SG},
{'n':'Kintsugi repair kit','a':'kintsukuroi kit','d':'Kit for mending broken pottery with lacquer and gold powder in the Japanese manner.','t':['urushi (traditional lacquer)','epoxy (modern substitute)','gold, silver or platinum powder'],'m':[],'s':KI,
 'x':[X('Urushi kintsugi','Repair with urushi lacquer, including ki urushi, red bengara urushi, mugi urushi (lacquer and wheat flour) and sabi urushi (lacquer and clay), cured in a humid furo for 2 days to 2 weeks and dusted with gold, silver or platinum.','',KI,dt='lacquer type · metal powder · cure time')]},
]
trads=[{'n':'Kintsugi','g':'Ceramics & glass','r':'Japan','p':'late 15th century onward','d':'Japanese mending of broken pottery with urushi lacquer dusted with gold, silver or platinum.','tech':'urushi lacquer joins and fills, cured in a humid furo, then metal powder is applied','mat':'urushi, wheat flour, clay, gold, silver or platinum powder','forms':['Kintsugi repair kit','Glaze'],'ctr':[],'auth':'lacquer seams cured over days and dusted with metal powder rather than epoxy glue','s':KI}]
brands=[B('Mayco','United States','','Mainstream','brush-on glaze','Brush-on glaze maker whose Stroke & Coat line fires cone 06 to 10.',s=MA,sig=['Glaze'])]
save('06_01',kinds,brands,trads,'Kept 3 planned kinds, added Kintsugi repair kit. Amaco Potters Choice, Coyote, Botz, Spectrum not confirmed on fetched pages so left out; Mayco brand entry cites conversion page.')

TC='https://www.theceramicshop.com/store/department/15/Kilns/page2.html'
PW='https://en.wikipedia.org/wiki/Potter%27s_wheel';LE='https://makezine.com/article/craft/the-leach-treadle-wheel/'
kinds=[
{'n':"Potter's wheel",'a':'throwing wheel','d':'Powered or kick wheel made for throwing pots.','t':['electric','kick','treadle','tabletop','banding wheel'],'m':[['Pacifica Glyde Torc 400','Pacifica']],'s':'https://seattlepotterysupply.com/pages/search-wheels-by-brand',
 'x':[X('Leach treadle wheel','Human-powered treadle wheel with crank, reciprocating pedal and heavy flywheel, named after Bernard Leach but designed by his sons.','',LE,dt='flywheel weight · seat · wheel head size'),
      X('Kick wheel','Wheel with a heavy flywheel the potter kicks to build momentum, developed in the mid to late third millennium BC.','',PW,dt='flywheel material · head size'),
      X('Electric wheel','Motor-driven wheel with speed set by foot pedal, common among craft potters and schools.','',PW,dt='motor power · centring capacity · head size')]},
{'n':'Pottery kiln','a':'','d':'Kiln made for firing clay. Fuel, loading style and chamber size vary by model.','t':['electric top loader','electric front loader','gas','raku','test kiln'],'m':[['Olympic 1818HE','Olympic Kilns'],['Olympic 2318HE','Olympic Kilns'],['Olympic 2818HE','Olympic Kilns'],['Skutt KM-818','Skutt'],['L&L Easy-Fire e23S-JH','L&L'],['Nabertherm Top 60','Nabertherm'],['Paragon Caldera XL','Paragon']],'s':'https://seattlepotterysupply.com/collections/electric-kilns'},
{'n':'Slab roller','a':'','d':'Machine that rolls clay into even slabs.','t':['table-top','free-standing','manual crank'],'m':[['Shimpo Mini Slab Roller','Shimpo'],['Shimpo SR-3050','Shimpo']],'s':'https://seattlepotterysupply.com/collections/slab-rollers'},
{'n':'Pugmill','a':'','d':'Machine that mixes clay and removes air from it.','t':['de-airing','mixer only'],'m':[['Shimpo NRA-04S','Shimpo'],['Shimpo NVS-07','Shimpo']],'s':'https://seattlepotterysupply.com/collections/mixers-pug-mills'},
{'n':'Kiln furniture','a':'','d':'Shelves, posts and stilts made to load work in a kiln.','t':['shelf','post','stilt','cone pack'],'m':[],'s':'https://seattlepotterysupply.com/pages/about-us'},
{'n':'Kiln spare parts','a':'kiln element · thermocouple · controller','d':'Element, thermocouple, relay or controller made for a kiln.','t':['element','thermocouple','relay','controller'],'m':[],'s':'https://seattlepotterysupply.com/pages/about-us'},
]
brands=[B('Skutt','United States','1953','Premium','electric kilns','Portland, Oregon electric-kiln maker.',s='knowledge',sig=[]),B('Shimpo','Japan','','Premium','potter\'s wheels','Maker of VL-Whisper wheels, slab rollers and pugmills.',s='knowledge'),B('Brent','United States','','Premium','potter\'s wheels','American potter\'s wheel maker (CXC and C models).',s='knowledge')]
brands[0].pop('sig')
save('06_02',kinds,brands,[],'Kept all 6 planned kinds. Shimpo VL-Whisper and Brent CXC, Skutt/L&L/Paragon/Olympic/Nabertherm kiln lines appear only as flat models from the kiln retailer page and old data; no archetypes since no fetched page describes them. Skutt 1953 from search snippet only, so brand uses knowledge.')
