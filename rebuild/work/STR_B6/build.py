import json, copy, os, re
BASE = '/home/user/Possession-Taxonomy/rebuild/'
d = json.load(open(BASE + 'work/STR_B6/bak/B6.json'))
K = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k
before = (len(d['depts']), sum(len(dp['s']) for dp in d['depts']), len(K),
          sum(len(k.get('x', [])) for k in K.values()))

WIKI = 'https://en.wikipedia.org/wiki/'
def new(n, a, dd, s, tt, **kw):
    k = {'n': n, 'a': a, 'd': dd, 's': s, 'tt': tt}
    k.update(kw)
    K[n] = k

# ---- new kinds (each with fetched source) ----
new('Hand brush', 'whisk broom · hearth brush · crumb brush', 'A short-handled brush swept into a dustpan for stairs, upholstery, hearths and car seats.', WIKI + 'Broom',
    [['Bristle', ['Horsehair', 'Synthetic', 'Natural fibre']], ['Use', ['Stairs and upholstery', 'Hearth']]])
new('Metal polish', 'brass polish · silver polish · chrome cleaner', 'Paste, liquid or impregnated cloth that cleans and shines metal such as brass, silver and stainless steel.', WIKI + 'Cleaning_agent',
    [['Metal', ['Brass and copper', 'Silver', 'Stainless steel', 'Chrome']], ['Form', ['Paste', 'Liquid', 'Cloth']]])
new('Dishwasher rinse aid and salt', 'rinse aid · rinsing agent · dishwasher salt · water-softener salt', 'Separate liquid or salt added to a dishwasher to dry dishes without spots and to soften hard water.', WIKI + 'Dishwasher_detergent',
    [['Product', ['Rinse aid', 'Dishwasher salt (water softener)']]])
new('Laundry bleach and whitener', 'oxygen bleach · colour-safe bleach · whitener', 'Additive that whitens and brightens washing and lifts stains the detergent leaves; unlike a household bleach cleaner.', WIKI + 'Laundry_detergent',
    [['Active', ['Oxygen bleach', 'Chlorine bleach']], ['Form', ['Powder', 'Liquid']]])
new('Laundry starch', 'spray starch · fabric stiffener', 'Product that stiffens cotton and linen so they press crisp; unlike a crease-releasing ironing spray.', WIKI + 'Laundry_detergent',
    [['Form', ['Spray', 'Liquid', 'Powder']]])
new('Technical fabric wash', 'technical wash · down wash · merino wash · shell wash', 'Specialist wash that cleans waterproof shells, down and merino without stripping their finish.', K['Fabric waterproofing and technical wash']['s'],
    [['Fabric', ['Waterproof shell', 'Down', 'Merino and base layer']]],
    m=[m for m in K['Fabric waterproofing and technical wash']['m'] if re.search(r'Tech Wash|Down Wash|Performance Wash', m[0])],
    r=[r for r in K['Fabric waterproofing and technical wash']['r'] if r[1] in ('Nikwax', 'Grangers')])
new('Fabric waterproofer', 'wash-in proofer · spray-on proofer · DWR reproofer · fabric protector', 'Treatment that restores water repellency to outdoor clothing, upholstery and shoe fabric.', K['Fabric waterproofing and technical wash']['s'],
    [['Application', ['Wash-in', 'Spray-on']], ['Fabric', ['Outdoor clothing', 'Upholstery and shoe fabric']]],
    m=[m for m in K['Fabric waterproofing and technical wash']['m'] if re.search(r'Proofer|Repel|Shield', m[0])],
    r=[r for r in K['Fabric waterproofing and technical wash']['r'] if r[1] == 'Scotchgard'])
new('Drying cabinet', 'clothes drying cupboard · airing cabinet', 'A cupboard that dries or airs hung clothes with warm air, without tumbling; unlike a tumble dryer.', WIKI + 'Clothes_dryer',
    [['Heat source', ['Warm air', 'Heat pump']]])
new('Flatiron (sad iron)', 'sad iron · smoothing iron · box iron · charcoal iron · goffering iron · tailor\'s goose', 'Solid or hollow iron heated on a stove or with charcoal, from before electric irons; now collected or used for display.', WIKI + 'Clothes_iron',
    [['Heating', ['Stove-heated solid iron', 'Charcoal box iron', 'Heated slug iron']], ['Shape', ['Flat', 'Goffering', "Tailor's goose"]]])
new('Washing line', 'clothes line · rotary dryer · whirligig · retractable line', 'Line or frame fixed outdoors to dry washing in the air; an indoor rack → Clothes airer.', WIKI + 'Clothes_line',
    [['Form', ['Rotary', 'Fixed line and prop', 'Retractable', 'T-post line']]])
new('Waste-paper basket', 'wastebasket · office bin', 'Small open bin for paper and light rubbish in a room; a kitchen bin has a lid or pedal.', WIKI + 'Waste_container',
    [['Material', ['Wire mesh', 'Plastic', 'Metal', 'Wicker']], ['Shape', ['Round', 'Rectangular']]])

# ---- edits to existing kinds: tt (hand written), see ----
TT = {
'Cylinder vacuum cleaner': [['Dust collection', ['Bagged', 'Bagless (cyclonic)']], ['Floor head', ['Plain suction head', 'Powered brush head']]],
'Upright vacuum cleaner': [['Dust collection', ['Bagged', 'Bagless']], ['Body', ['Fixed body', 'Lift-away (detachable canister)']], ['Power', ['Corded', 'Cordless']]],
'Stick vacuum cleaner': [['Power', ['Corded', 'Cordless']], ['Body', ['Fixed body', 'With detachable handheld']], ['Emptying', ['Manual bin', 'Self-emptying dock']], ['Floor', ['Dry only', 'Wet-and-dry']]],
'Robot vacuum cleaner': [['Cleaning', ['Vacuum only', 'Vacuum-and-mop', 'Mop only (no suction)']], ['Navigation', ['Random bounce', 'Camera', 'Lidar']], ['Dock', ['Charge only', 'Self-emptying', 'Wash-and-dry']]],
'Handheld vacuum cleaner': [['Power', ['Corded', 'Cordless']], ['Use', ['Car', 'Mattress', 'Crumbs and pet hair']]],
'Wet and dry vacuum cleaner': [['Power', ['Corded', 'Cordless (battery)']], ['Function', ['Dry and liquid pick-up', 'With blower', 'With power-tool socket (dust extraction)']]],
'Ash vacuum cleaner': [['Form', ['Self-powered', 'Drum attachment for a shop vacuum']]],
'Floor washer': [['Power', ['Corded', 'Cordless']], ['Cleaning', ['Wet-dry with suction', 'With steam', 'Electric mop without suction (pads or rollers)']], ['Dock', ['Manual rinse', 'Self-cleaning dock']]],
'Carpet cleaning machine': [['Form', ['Upright carpet washer', 'Portable spot cleaner', 'Spray-extraction attachment for a wet-dry vacuum']]],
'Steam cleaner': [['Form', ['Steam mop (upright)', 'Cylinder steam cleaner with hose', 'Handheld steam cleaner', 'Steam vacuum']]],
'Window vacuum': [['Power', ['Cordless rechargeable', 'Corded']]],
'Wet mop': [['Head', ['String', 'Flat', 'Sponge', 'Cloth (Cuban)', 'Spin-mop head']], ['Use', ['Wet', 'Dry (dust mop)']]],
'Spray mop': [['Refill', ['Refillable tank', 'Disposable pad and cartridge']]],
'Mop bucket': [['Design', ['Wringer bucket', 'Double bucket', 'Bucket on wheels']]],
'Broom': [['Bristle', ['Soft indoor', 'Stiff outdoor', 'Rubber']], ['Head', ['Angle', 'Push (wide)']]],
'Dustpan and brush': [['Handle', ['Hand-held', 'Long-handled lobby pan']]],
'Carpet sweeper': [['Drive', ['Roller turned by the wheels']]],
'Scrub brush': [['Use', ['General scrubbing', 'Grout', 'Deck']], ['Drive', ['By hand', 'Powered spin scrubber']]],
'Toilet brush': [['Head', ['Bristle', 'Silicone', 'Disposable']]],
'Carpet beater': [['Material', ['Rattan', 'Wire']]],
'Microfibre cloth': [['Use', ['General-purpose', 'Glass and polishing']], ['Weave', ['Flat', 'Waffle']]],
'Dishcloth': [['Material', ['Cotton knit', 'Cellulose and cotton (Swedish)', 'Disposable']]],
'Sponges and scourers': [['Material', ['Cellulose sponge', 'Polyurethane foam', 'Natural sea sponge', 'Steel wool', 'Melamine foam', 'Non-scratch nylon pad']]],
'Cleaning wipes': [['Use', ['Antibacterial surface', 'Floor pads', 'Glass']], ['Material', ['Standard', 'Biodegradable']]],
'Duster': [['Material', ['Feather (ostrich)', 'Microfibre', 'Lambswool']], ['Reach', ['Hand-held', 'Extendable cobweb duster']]],
'Chamois': [['Material', ['Natural leather', 'Synthetic (PVA)']]],
'Squeegee': [['Form', ['Hand squeegee', 'Washer-squeegee combination', 'Telescopic pole kit', 'Shower squeegee']]],
'Multi-purpose cleaner': [['Form', ['Trigger spray', 'Cream cleaner', 'Concentrate', 'Scouring powder']], ['Action', ['Standard', 'Antibacterial']], ['Room', ['Kitchen', 'Bathroom']]],
'Bleach and disinfectant': [['Active', ['Chlorine bleach', 'Non-chlorine disinfectant']], ['Thickness', ['Thin', 'Thick']], ['Form', ['Liquid', 'Spray', 'Wipes']]],
'Glass cleaner': [['Form', ['Spray', 'Wipes', 'Concentrate']]],
'Toilet cleaner': [['Form', ['Gel', 'Rim block', 'In-cistern block', 'Tablet', 'Wipes']]],
'Limescale remover': [['Form', ['Spray', 'Foam', 'Concentrate']]],
'Degreaser and oven cleaner': [['Surface', ['Oven', 'Grill', 'Hob', 'Worktops']], ['Form', ['Spray', 'Gel', 'Bag-and-gel kit']]],
'Mould remover': [['Form', ['Spray', 'Foam', 'Gel']], ['Base', ['Bleach', 'Bleach-free']]],
'Drain unblocker': [['Form', ['Gel', 'Granules or crystals', 'Foaming', 'Liquid']], ['Action', ['Chemical', 'Enzyme (biological)']]],
'Appliance cleaner and descaler': [['Appliance', ['Kettle and coffee machine', 'Dishwasher', 'Washing machine', 'Iron soleplate']], ['Job', ['Descale', 'Clean', 'Freshen']]],
'Floor and carpet cleaner': [['Surface', ['Hard floor', 'Wood and laminate', 'Carpet']], ['Form', ['Liquid', 'Shampoo', 'Powder', 'Machine solution']]],
'Furniture and upholstery cleaner': [['Surface', ['Wood', 'Leather', 'Fabric upholstery']], ['Form', ['Spray polish', 'Wax polish', 'Foam']]],
'Pet-stain and odour remover': [['Form', ['Spray', 'Concentrate', 'Powder']]],
'Washing-up liquid': [['Form', ['Liquid', 'Concentrated liquid', 'Spray or foam', 'Powder', 'Bar']], ['Formula', ['Standard', 'Antibacterial', 'Plant-based']]],
'Dishwasher detergent': [['Form', ['Tablet', 'All-in-one tablet', 'Pod or capsule', 'Powder', 'Gel', 'Sheet']]],
'Front-load washing machine': [['Fitting', ['Freestanding', 'Integrated (built-in)']], ['Depth', ['Standard', 'Slim-depth']], ['Capacity', ['Up to 8 kg', '9 kg', '10 kg and over']], ['Dosing', ['Manual', 'Auto-dosing']], ['Connectivity', ['No app', 'Wi-Fi app']]],
'Top-load washing machine': [['Agitation', ['Agitator', 'Impeller (pulsator)']], ['Water use', ['Standard', 'High-efficiency low-water']], ['Lid', ['Lid lock', 'No lid lock']], ['Control', ['Dial', 'Smart app']]],
'Washer-dryer': [['Drying', ['Condenser', 'Heat-pump (ventless)']], ['Size', ['Compact 24-inch', 'Full-size']]],
'Laundry centre': [['Washer', ['Top-load base', 'Front-load base']], ['Dryer fuel', ['Electric', 'Gas']], ['Size', ['Full-size', 'Compact 24-inch']]],
'Compact washing machine': [['Form', ['24-inch front-loader (stackable)', 'Portable top-loader with sink hook-up', 'Pedestal washer', 'Countertop or manual washer']]],
'Twin-tub washing machine': [['Drain', ['Semi-automatic with drain pump', 'Gravity drain']], ['Size', ['Full-size', 'Portable mini']]],
'Tumble dryer': [['Moisture removal', ['Vented', 'Condenser', 'Heat-pump']], ['Fuel', ['Electric', 'Gas']], ['Fitting', ['Freestanding', 'Integrated or built-under']], ['Size', ['Full-size', 'Compact tabletop']]],
'Spin dryer': [['Size', ['Full-size', 'Compact']]],
'Bedding dryer': [['Method', ['Mat', 'Hose and nozzle (mat-free)']], ['Extras', ['Shoe-drying attachment']]],
'Laundry detergent': [['Form', ['Powder', 'Liquid or gel', 'Capsule or pod', 'Sheet or tile']], ['Enzymes', ['Bio', 'Non-bio']], ['Fabric', ['Colour-care', 'Delicates and wool', 'Sports and activewear']], ['Skin', ['Standard', 'Baby and sensitive (fragrance-free)']], ['Conditioning', ['Detergent only', '2-in-1 with conditioner']]],
'Fabric conditioner': [['Form', ['Liquid softener', 'Dryer sheets', 'Wool dryer balls']]],
'Stain remover': [['Form', ['Pre-wash spray', 'Oxygen bleach powder', 'Stain bar or soap']], ['Job', ['Stain removal', 'Colour-run removal', 'Colour catching']]],
'Scent booster and fabric freshener': [['Form', ['In-wash scent beads', 'Fabric refresher spray']]],
'Ironing spray': [['Form', ['Crease releaser', 'Ironing water']]],
'Lint remover': [['Form', ['Lint roller', 'Electric fabric shaver', 'Lint brush', 'Clothes brush']]],
'Steam iron': [['Heating', ['Dry iron', 'Steam iron']], ['Power', ['Corded', 'Cordless (heats on a base)']], ['Size', ['Full-size', 'Travel (dual-voltage, folding handle)']], ['Soleplate', ['Stainless steel', 'Ceramic', 'Non-stick']]],
'Steam generator iron': [['Boiler', ['Pressurised', 'Non-pressurised flow-through']], ['Size', ['Full-size station', 'Compact station']]],
'Garment steamer': [['Form', ['Handheld or travel', 'Upright with pole and hanger', 'Hybrid iron-steamer']]],
'Ironing board': [['Form', ['Full-size freestanding', 'Tabletop', 'Wall-mounted or pull-out', 'Extra-wide', 'Sleeve board', 'Folding ironing mat']], ['Cover', ['Cotton', 'Metallised reflective', 'Felt or foam underlay']]],
'Trouser press': [['Power', ['Electric heated', 'Non-electric valet']], ['Garments', ['Trousers only', 'Shirt and trousers']], ['Finish', ['Oak', 'Walnut', 'Mahogany', 'Beech', 'White']]],
'Clothes airer': [['Form', ['Folding or concertina', 'Wall-mounted', 'Over-bath or over-door', 'Ceiling pulley']], ['Heat', ['Unheated', 'Heated']]],
'Clothes pegs': [['Material', ['Wood', 'Plastic', 'Stainless steel']], ['Grip', ['Standard', 'Soft-grip']], ['Carrier', ['Peg bag', 'Peg basket']]],
'Laundry basket': [['Form', ['Hamper', 'Bag', 'Sorter', 'Collapsible basket', 'Mesh wash bag']]],
'Washboard and hand-wash tools': [['Tool', ['Washboard', 'Washing dolly or posser', 'Mangle or wringer', 'Wash copper']]],
'Kitchen bin': [['Opening', ['Pedal', 'Sensor', 'Touch-top', 'Swing', 'Open']], ['Fitting', ['Freestanding', 'Under-counter']]],
'Recycling and food-waste bin': [['Waste', ['Mixed recycling', 'Food waste', 'Compost']], ['Form', ['Multi-compartment bin', 'Caddy']]],
'Outdoor bin': [['Form', ['Wheelie bin', 'Dustbin', 'Sack holder or bin-bag frame']], ['Accessory', ['Wheelie-bin store']]],
'Bin bags': [['Use', ['Drawstring liner', 'Refuse sack', 'Compostable caddy liner', 'Recycling sack']]],
'Trash compactor': [['Fitting', ['Freestanding', 'Under-counter']]],
'Vacuum cleaner spare parts': [['Part', ['Dust bag', 'Filter', 'Drive belt', 'Brush roll', 'Floor head and tools', 'Hose', 'Wand', 'Battery pack', 'Motor', 'Wheel or castor', 'Robot mop pad and side brush']]],
'Washing machine spare parts': [['Part', ['Inlet or drain hose', 'Door seal', 'Drain pump', 'Drum paddle (lifter)', 'Carbon brushes', 'Heater element', 'Door lock (interlock)', 'Filter', 'Pedestal and stacking kit']]],
'Tumble dryer spare parts': [['Part', ['Lint filter', 'Drum belt', 'Condenser water container', 'Vent hose', 'Heater', 'Sensor']]],
'Iron and steam generator spare parts': [['Part', ['Anti-scale cartridge', 'Water tank', 'Soleplate', 'Steam hose']]],
}
for n, tt in TT.items():
    k = K[n]; k['tt'] = tt; k.pop('t', None)
# tidy aliases of split kinds
K['Dishwasher detergent']['a'] = 'dishwasher tablets · dishwasher pods · dishwasher powder · automatic dishwashing detergent'
K['Dishwasher detergent']['d'] = 'Detergent made for automatic dishwashers, sold as tablets, pods, powder, gel or sheets; rinse aid and salt → Dishwasher rinse aid and salt.'
K['Fabric waterproofing and technical wash']['_drop'] = True
K['Ironing spray']['d'] = 'Spray that relaxes creases or adds steam water for pressing; stiffening → Laundry starch.'
K['Kitchen bin']['d'] = K['Kitchen bin']['d'].replace('  ', ' ')
K['Clothes airer']['a'] = (K['Clothes airer'].get('a') or '') + (' · ' if K['Clothes airer'].get('a') else '') + 'clothes horse'
K['Clothes airer']['d'] = 'Indoor rack, heated or unheated, for drying washing; an outdoor line → Washing line.'

SEE = {
'Cylinder vacuum cleaner': [['G3', 'Central vacuum system', 'built-in system instead of a portable machine']],
'Handheld vacuum cleaner': [['G1', 'Car vacuum cleaner', 'made for car interiors']],
'Steam cleaner': [['C2', 'Pressure washer', 'cold water at high pressure, outdoors']],
'Glass cleaner': [['G1', 'Glass cleaner', 'same product sold for cars']],
'Multi-purpose cleaner': [['A2', 'Shoe cleaner', 'for footwear'], ['G1', 'Car-wash shampoo', 'for car paint']],
'Bleach and disinfectant': [['H3', 'Toy cleaner', 'gentler cleaner for adult toys']],
'Appliance cleaner and descaler': [['B5', 'Dishwasher', 'the appliance it cleans']],
'Dishwasher detergent': [['B5', 'Dishwasher', 'the appliance it serves']],
'Furniture and upholstery cleaner': [['G1', 'Leather cleaner and conditioner', 'for car leather']],
'Floor and carpet cleaner': [['G1', 'Upholstery and carpet cleaner', 'for car interiors']],
'Fabric waterproofer': [['A2', 'Shoe polish and waterproofing', 'for leather footwear']],
'Tumble dryer': [['G3', 'Bathroom clothes dryer', 'built-in bathroom unit'], ['B6', 'Drying cabinet', 'warm-air cupboard without tumbling']],
'Clothes airer': [['G3', 'Bathroom clothes dryer', 'built-in drying unit'], ['B1', 'Clothes hanger', 'the hanger itself'], ['B6', 'Washing line', 'outdoor drying']],
'Washing line': [['B6', 'Clothes airer', 'indoor drying']],
'Washer-dryer': [['B6', 'Tumble dryer', 'drying only']],
'Kitchen bin': [['G3', 'Waste disposal unit', 'sink-fitted grinder instead of a bin']],
'Trash compactor': [['G3', 'Waste disposal unit', 'grinds food waste down the drain']],
'Wet mop': [['B6', 'Spray mop', 'tank and trigger instead of a bucket']],
'Steam iron': [['B6', 'Flatiron (sad iron)', 'the historic form']],
'Garment steamer': [['B6', 'Steam generator iron', 'iron with a separate boiler']],
'Squeegee': [['B6', 'Window vacuum', 'powered alternative']],
'Dishwasher rinse aid and salt': [['B5', 'Dishwasher', 'the appliance it serves']],
'Waste-paper basket': [['B6', 'Kitchen bin', 'lidded bin for kitchen waste']],
'Laundry bleach and whitener': [['B6', 'Bleach and disinfectant', 'household bleach for surfaces']],
'Laundry starch': [['B6', 'Ironing spray', 'releases creases rather than stiffening']],
}
for n, v in SEE.items():
    K[n]['see'] = v

def kd(n, **kw):
    return n

LAYOUT = [
 ('Vacuums & floor machines',
  'Powered machines that lift dirt from floors, carpets and glass by suction, water or steam; hand tools → Mops, brooms & cloths, a built-in central system → G3.',
  'What does the machine do with the dirt: suck up dry dust, take up wet mess, wash with water or steam, or clean glass?',
  [('Vacuum cleaners', 'Household machines that suck up dry dust and crumbs from floors and furniture: cylinder, upright, stick, robot and handheld; heavy debris and liquids → Shop & ash vacuums.',
    'kinds by the shape of the body and how it is moved: pulled, pushed, held in one hand or driving itself',
    ['Cylinder vacuum cleaner', 'Upright vacuum cleaner', 'Stick vacuum cleaner', 'Robot vacuum cleaner', 'Handheld vacuum cleaner']),
   ('Shop & ash vacuums', 'Tough machines for builders\' dust, liquids and cold ash; an everyday floor vacuum → Vacuum cleaners shelf.', '',
    ['Wet and dry vacuum cleaner', 'Ash vacuum cleaner']),
   ('Floor washers, carpet & steam cleaners', 'Machines that clean with water or steam rather than dry suction: floor washers, carpet cleaners and steam mops; a bucket mop → Mops & buckets shelf.', '',
    ['Floor washer', 'Carpet cleaning machine', 'Steam cleaner']),
   ('Window machines', 'Powered tools that clean glass: handheld window vacuums and window-cleaning robots; a hand squeegee → Cloths, dusters & squeegees shelf.', '',
    ['Window vacuum', 'Window-cleaning robot'])]),
 ('Mops, brooms & cloths',
  'Hand tools and cloths for sweeping, mopping, scrubbing and wiping; powered machines → Vacuums & floor machines, sprays and liquids → Cleaning products.',
  'What does the tool do to the dirt: wash a floor wet, sweep it up dry, scrub it off or wipe it away?',
  [('Mops & buckets', 'Tools for washing floors wet: string, flat and sponge mops, spray mops and the buckets that go with them; a steam mop → Steam cleaner.',
    '', ['Wet mop', 'Spray mop', 'Mop bucket']),
   ('Brooms & dustpans', 'Tools for sweeping dry dirt into a pile or pan: brooms, hand brushes, dustpans, carpet sweepers; a powered sweeper → Vacuum cleaners shelf.',
    'kinds from the largest floor tool to the smallest: broom, carpet sweeper, dustpan, hand brush, carpet beater',
    ['Broom', 'Carpet sweeper', 'Dustpan and brush', 'Hand brush', 'Carpet beater']),
   ('Brushes & scourers', 'Tools that scrub dirt off a surface: scrub brushes, toilet brushes and sponges and scourers; a cloth that only wipes → Cloths shelf.', '',
    ['Scrub brush', 'Toilet brush', 'Sponges and scourers']),
   ('Cloths, dusters & squeegees', 'Cloths and wipers that take dust, smears or water off surfaces: microfibre cloths, dishcloths, dusters, chamois leathers, wipes and squeegees.',
    'kinds by what is wiped off: general mess, dust, smears, standing water',
    ['Microfibre cloth', 'Dishcloth', 'Cleaning wipes', 'Duster', 'Chamois', 'Squeegee'])]),
 ('Cleaning products',
  'Liquids, gels, powders and blocks that clean, descale or disinfect surfaces, drains, floors and dishes; laundry products → Laundry products.',
  'What is the product for: any surface, a bathroom problem, the kitchen and its appliances, floors and furniture, or dishes?',
  [('General surface cleaners', 'Products for most hard surfaces: all-purpose sprays, bleach and disinfectant, glass and metal cleaners.',
    'kinds from the widest job to the narrowest: any surface, germs, glass, metal',
    ['Multi-purpose cleaner', 'Bleach and disinfectant', 'Glass cleaner', 'Metal polish']),
   ('Bathroom & drain cleaners', 'Products for toilets, limescale, mould and blocked drains; a kitchen grease cleaner → Kitchen & appliance cleaners.',
    'kinds by the bathroom problem: toilet bowl, limescale, mould, blocked drain',
    ['Toilet cleaner', 'Limescale remover', 'Mould remover', 'Drain unblocker']),
   ('Kitchen & appliance cleaners', 'Products for baked-on grease and for the insides of kettles, coffee machines and dishwashers.', '',
    ['Degreaser and oven cleaner', 'Appliance cleaner and descaler']),
   ('Floor, carpet & furniture care', 'Products for floors, carpets, upholstery, wood and pet accidents; hard-surface sprays → General surface cleaners.', '',
    ['Floor and carpet cleaner', 'Furniture and upholstery cleaner', 'Pet-stain and odour remover']),
   ('Dishwashing', 'Products for washing dishes by hand or in a dishwasher; the machine itself → B5.', '',
    ['Washing-up liquid', 'Dishwasher detergent', 'Dishwasher rinse aid and salt'])]),
 ('Washing machines & dryers',
  'Household appliances that wash or dry a load of clothes; irons and airers → Ironing & drying, a built-in bathroom dryer → G3.',
  'Does the appliance wash, dry, or do both?',
  [('Washing machines', 'Machines that wash a load: front-load, top-load, compact and twin-tub models; one that also dries → Washer-dryers & laundry centres.',
    'kinds by how clothes go in and how many tubs there are: front door, top lid, small size, two tubs',
    ['Front-load washing machine', 'Top-load washing machine', 'Compact washing machine', 'Twin-tub washing machine']),
   ('Dryers', 'Appliances that dry washing after the wash: tumble dryers, spin dryers, drying cabinets and bedding dryers; a washing line or rack → Ironing & drying.',
    'kinds by how the water is removed: hot air in a drum, spinning, warm air in a cabinet, air blown into bedding',
    ['Tumble dryer', 'Spin dryer', 'Drying cabinet', 'Bedding dryer']),
   ('Washer-dryers & laundry centres', 'Appliances that wash and dry in one: a single-drum washer-dryer or a washer and dryer stacked as a laundry centre.', '',
    ['Washer-dryer', 'Laundry centre'])]),
 ('Laundry products',
  'Detergents and additives used in or after the wash; machine and tool → Washing machines & dryers, Ironing & drying.',
  'At which stage is the product used: in the wash, or after it on clean fabric?',
  [('Washing & stain care', 'Products added to the wash or used on stains: detergent, bleach, stain remover and specialist fabric washes and proofers.',
    'kinds from the main wash to the specialist: detergent, bleach, stain remover, technical wash, waterproofer',
    ['Laundry detergent', 'Laundry bleach and whitener', 'Stain remover', 'Technical fabric wash', 'Fabric waterproofer']),
   ('After the wash', 'Products that soften, scent, stiffen or tidy fabric once washed: conditioner, scent boosters, starch, ironing spray and lint removers.',
    'kinds by what they do to dry fabric: soften, scent, stiffen, release creases, lift fluff',
    ['Fabric conditioner', 'Scent booster and fabric freshener', 'Laundry starch', 'Ironing spray', 'Lint remover'])]),
 ('Ironing & drying',
  'Equipment for pressing clothes, hanging washing to dry and carrying or hand-washing it; powered washers and dryers → Washing machines & dryers.',
  'Which step of caring for clothes does it serve: pressing, drying on a line or rack, or carrying and hand-washing?',
  [('Pressing', 'Irons, steamers, presses and boards that remove creases: steam irons, steam generators, garment steamers, trouser presses and ironing boards.',
    'kinds from the main tool to the support: iron, boiler iron, steamer, press, historic iron, board',
    ['Steam iron', 'Steam generator iron', 'Garment steamer', 'Trouser press', 'Flatiron (sad iron)', 'Ironing board']),
   ('Drying', 'Racks, lines and pegs for air-drying washing indoors or out; a machine → Dryers shelf.', '',
    ['Clothes airer', 'Washing line', 'Clothes pegs']),
   ('Carrying & hand washing', 'Baskets and tools for carrying laundry and for washing it by hand.', '',
    ['Laundry basket', 'Washboard and hand-wash tools'])]),
 ('Bins & waste',
  'Containers and bags that hold household waste, recycling and food scraps; a sink grinder or built-in unit → G3, a compost heap → C2.',
  'Where does the waste go: a room bin, a sorted-waste bin, an outdoor collection bin, or a bag or compactor?',
  [('Indoor bins', 'Lidded or open bins kept in a kitchen, bathroom or room for everyday rubbish.', '',
    ['Kitchen bin', 'Waste-paper basket']),
   ('Sorted-waste bins', 'Bins and caddies that keep recycling, food waste and compost apart from general rubbish.', '',
    ['Recycling and food-waste bin']),
   ('Outdoor bins', 'Large bins and holders kept outside for collection day.', '',
    ['Outdoor bin']),
   ('Liners & compactors', 'Bags that line bins and machines that squash waste to make more room.', '',
    ['Bin bags', 'Trash compactor'])]),
 ('Spare parts & consumables',
  'Replacement bags, filters, belts and seals for the household appliances above, one entry per appliance; parts for other machines → their own category.',
  'Which appliance does the part fit: vacuum cleaner, washing machine, tumble dryer or iron?',
  [('Spare parts', 'One entry per appliance listing the parts owners replace: vacuum, washing machine, dryer and iron.', 'kinds by appliance, in the order of the shelves above',
    ['Vacuum cleaner spare parts', 'Washing machine spare parts', 'Tumble dryer spare parts', 'Iron and steam generator spare parts'])]),
]

old = {dp['n']: dp for dp in d['depts']}
depts = []
used = set()
for n, t, ax, shelves in LAYOUT:
    dp = {'n': n, 'mode': old[n]['mode'], 't': t, 'ax': ax}
    for key in ('note', 'b'):
        if old[n].get(key): dp[key] = old[n][key]
    dp['s'] = []
    for sn, st, sax, kinds in shelves:
        sh = {'n': sn, 't': st}
        if len(kinds) > 3:
            sh['ax'] = sax
        ks = []
        for kn in kinds:
            k = copy.deepcopy(K[kn]); used.add(kn)
            ks.append(k)
        sh['k'] = ks
        dp['s'].append(sh)
    depts.append(dp)
# split-out and carry
left = [n for n in K if n not in used and not K[n].get('_drop')]
assert not left, left
# remove helper tokens
for dp in depts:
    for s in dp['s']:
        for k in s['k']:
            k.pop('_drop', None)

# Kind-level edits: dep trimming of types moved
d['ax'] = 'What job does the object do for the household: clean a floor or window, wipe or scrub a surface, clean with a product, wash or dry clothes, press and hang them, or hold waste?'
d['key'] = [
 '1. Is it a powered machine that sucks, scrubs or steams dirt off floors, carpets or glass? → Vacuums & floor machines',
 '2. Is it a hand tool or cloth for sweeping, mopping, scrubbing or wiping? → Mops, brooms & cloths',
 '3. Is it a liquid, powder, gel or block that cleans, descales or disinfects a surface, drain, floor or dish? → Cleaning products',
 '4. Is it an appliance that washes or dries a load of clothes? → Washing machines & dryers',
 '5. Is it a detergent or additive used in the wash or on clean fabric? → Laundry products',
 '6. Is it for pressing clothes, drying them on a line or rack, or carrying and hand-washing them? → Ironing & drying',
 '7. Does it hold or squash household waste, recycling or food scraps? → Bins & waste',
 '8. Is it a bag, filter, belt or seal that replaces a worn part of one of these appliances? → Spare parts & consumables',
 '<i>Precedence: a powered window or floor machine is a machine (step 1) before a hand tool (step 2); a dishwasher product is a cleaning product (step 3), the dishwasher itself → B5; a tumble dryer is an appliance (step 4) before a rack (step 6).</i>']
d['lead'] = 'Movable equipment, tools and consumables for keeping a home and its textiles clean, organised by the job the object does: floor machines, hand tools, cleaning products, laundry appliances and products, pressing and drying, bins, then spare parts.'
d['depts'] = depts

out = BASE + 'out/B6.json'
tmp = out + '.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, out)
after = (len(depts), sum(len(dp['s']) for dp in depts), sum(len(s['k']) for dp in depts for s in dp['s']),
         sum(len(k.get('x', [])) for dp in depts for s in dp['s'] for k in s['k']))
print('before', before, 'after', after)
