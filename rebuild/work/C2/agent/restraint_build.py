import json, os, sys
B='/home/user/Possession-Taxonomy/rebuild/work/C2/shelves/'
HB='https://www.hornbach.de/c/garten/gartenbewaesserung/S883'
GM='https://www.greenhousemegastore.com/collections/plant-labels'
GE='https://www.gardeningexpress.co.uk/gardening-supplies/garden-furniture-outdoor-living/arches-and-obelisks'
DIY2='https://www.diy.com/outdoor-garden/lawn-plant-care/compost-soil-improvers.cat?page=2'
def K(n,d,s,a='',t=None,m=None,r=None):
    k={'n':n,'a':a,'d':d}
    if t: k['t']=t
    k['s']=s
    if m: k['m']=m
    if r: k['r']=r
    return k
J={}
J['04_01']=dict(kinds=[
 K('Garden hose','Flexible hose for carrying water round a garden.',HB,
   t=['reinforced','anti-kink','expandable','flat'],
   m=[['Ultimate Anti-Kink Hose','Hozelock'],['Ultraflex Anti-Kink Hose','Hozelock'],['Superhoze','Hozelock'],['Maxi Plus','Hozelock'],['Select','Hozelock']]),
 K('Hose reel','Reel or cart on which a garden hose is wound and stored.',HB,
   t=['wall reel','cart','auto-rewind'],
   m=[['RollUp','Gardena'],['Auto Reel','Hozelock'],['Auto Reel Mobile','Hozelock'],['2-in-1 Reel','Hozelock'],['Pico Reel','Hozelock']]),
 K('Hose connector','Click-on or screw fitting that joins a garden hose to a tap, a tool or another hose.','https://shop.ernestdoe.com/collections/hozelock',
   a='hose fitting',m=[['Aquastop Connector','Hozelock']]),
 K('Hose spray gun','Hand-held nozzle or gun on a hose end that shapes and stops the water jet.','https://shop.ernestdoe.com/collections/hozelock',
   a='hose nozzle',m=[['Multi Plus Spray Gun','Hozelock']]),
],notes='Restraint only. Garden hose: 7 Hozelock models cut to 5 (dropped Tuffhoze, Wonderhoze); reel/cart/auto-rewind and hose constructions as types. Hose reel: dropped two for_q SKU codes (wholesale noise) and the duplicate RollUp range entry. No Gardena or Flexi-Hose hose models added because the old data has none and this shelf has no web research. No new kinds, brands or archetypes.')
J['04_02']=dict(kinds=[
 K('Lawn sprinkler','Device that sprays water over an area of lawn or bed.',HB,
   t=['oscillating','rotary','pulsating','pop-up'],
   m=[['OS 140','Gardena'],['Pulsating Sprinkler','Hozelock'],['Rectangular Sprinkler Aquasave Pro','Hozelock'],['Rectangular Sprinkler Plus','Hozelock'],['Round Sprinkler Plus','Hozelock']]),
 K('Drip irrigation kit','Set of pipe, drippers and fittings that delivers water drop by drop to plants.',HB,
   m=[['AquaBloom','Gardena'],['AquaPrecise','Gardena'],['Micro 15 Pot Garden Watering System','Hozelock'],['Solar Drip Automatic Watering Kit','Hozelock'],['Strauch','RainBird']],
   r=[['Micro-Drip-System','Gardena'],['Easy Drip','Hozelock'],['Micro','Hozelock']]),
 K('Soaker hose','Porous hose that seeps water into the soil along its length.','https://www.mitre10.com.au/garden/hose-fittings-accessories/soaker-weeper-hoses',
   m=[['Porous Soaker Hose','Hozelock']]),
 K('Irrigation controller','Timer or controller that switches the water supply to a garden watering system.',HB,
   t=['tap timer','multi-zone controller','smart'],
   m=[['Master Unit 1000','Gardena'],['Master Unit 2000','Gardena'],['Sensor Controller Plus','Hozelock']]),
 K('Tree watering bag','Water-filled bag strapped round a tree trunk that releases water slowly into the root zone.',HB),
],notes='Restraint only. Sprinkler head styles and controller kinds kept as types. Dropped for_q FQ-BC 4 SKU, the Gardena MASTER 1197-20 article-number duplicate of the Master units, the Micro range on sprinklers (it is a drip system, kept under Drip irrigation kit) and the Micro-Drip-System range on controllers (duplicate of the drip kit range). Soaker hose model name stripped of its 6764 article number. No new kinds, brands or archetypes.')
J['04_03']=dict(kinds=[
 K('Pond liner','Flexible waterproof sheet laid to form a garden pond.','https://aquacadabra.com/collections/pond-liners',
   t=['EPDM','PVC','butyl'],m=[['Affinity Pond Liner','Blagdon'],['Alfafol PVC Pond Liner','Oase']]),
 K('Preformed pond','Rigid moulded pond shell set into the ground.','https://aquacadabra.com/collections/pond-liners',
   m=[['Pre-Formed Pond Dee','Bermuda']]),
 K('Pond pump','Pump that circulates water in a garden pond, fountain or water feature.',HB,
   a='fountain pump',t=['filter pump','fountain pump']),
],notes='Restraint only. Liner materials and pump uses as types. All old models kept (only three). Pond fish belong in the animal register and are not on this shelf. No new kinds, brands or archetypes.')
J['05_01']=dict(kinds=[
 K('Plant stake','Rod or cane pushed into the soil to hold up a plant.',GM,a='cane'),
 K('Plant tie','Tie, twine, clip or tape that fastens a plant to its support.',GM,a='tapener',
   t=['twine','wire','clip','tying tool (tapener)']),
 K('Plant support frame','Wire or plastic cage, ring or grow-through grid that holds up a whole plant or clump.',GM,a='plant cage · plant ring'),
 K('Trellis','Open lattice panel on which climbing plants are trained.',GM),
 K('Garden arch','Arched frame over a path on which climbing plants are grown.',GE),
 K('Obelisk','Free-standing tapering frame on which climbing plants are grown.',GE),
 K('Plant label','Tag or marker that names a plant in a pot or bed.',GM),
],notes='Restraint only. Plant tying tool (tapener) merged into Plant tie as a type, its alias carried over. No old models existed. No new kinds, brands or archetypes.')
J['05_02']=dict(kinds=[
 K('Horticultural fleece','Light non-woven fabric laid over plants against frost and pests.','https://www.palmcentre.co.uk/fleece-jackets',
   m=[['Plant Fleece Jackets','Haxnicks']]),
 K('Plant netting','Netting that supports climbing plants or keeps birds and pests off crops.',GM,
   m=[['Crop support trellis','Hortonova']]),
 K('Cloche','Small transparent cover placed over plants to shelter and warm them.','https://www.quickcrop.ie/product/easy-lantern-cloches-for-plant-protection',
   t=['glass bell','lantern','tunnel'],
   m=[['Original Victorian Bell Garden Cloche','Haxnicks'],['Easy Lantern Cloche','Tildenet'],['Access Glass Cloche','Two Wests & Elliott']]),
],notes='Restraint only. Cloche forms as types; dropped the maker-less "Victorian bell cloche (glass)" entry, which is the glass bell type rather than a model. No new kinds, brands or archetypes.')
J['06_00']=dict(kinds=[
 K('Potting compost','Prepared growing medium for pots and containers.','https://diy.com/departments/levington-compost-50l/919405_BQ.prd',
   t=['multi-purpose','peat-free','seed and cutting','ericaceous','John Innes']),
 K('Soil improver','Material dug into soil to improve its structure or fertility.',DIY2),
 K('Mulch','Material spread on the soil surface to hold moisture and suppress weeds, such as bark.','https://www.diy.com/departments/verve-natural-bark-chippings-50l-bag/5063022843166_BQ.prd'),
 K('Topsoil','Screened upper soil sold for beds, lawns and filling.',DIY2),
 K('Compost-filled grow bag','Plastic sack of growing medium laid flat and planted into directly.',DIY2,a='grow bag'),
 K('Compost bin','Container in which garden and kitchen waste is composted.','https://www.getcomposting.com/products/blackwall-220-litre-green-compost-converter',
   t=['bin','tumbler','wormery','hot composter'],m=[['Compost Converter','Blackwall']]),
],notes='Restraint only. Compost blends and composter styles as types. No decorative stone or gravel kinds were on this shelf (they belong in C8). No new kinds, brands or archetypes.')
for j,o in J.items():
    o.setdefault('brands',[]); o.setdefault('traditions',[])
    o={'kinds':o['kinds'],'brands':[],'traditions':[],'notes':o['notes']}
    tmp=B+j+'.json.tmp'; json.dump(o,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,B+j+'.json')
