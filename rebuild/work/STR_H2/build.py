import json, copy, os
BASE = '/home/user/Possession-Taxonomy/rebuild/'
src = json.load(open(BASE + 'work/STR_H2/bak/H2.json'))
old = {}
for dp in src['depts']:
    for s in dp['s']:
        for k in s['k']:
            old[k['n']] = k

def G(label, *m):
    return [label, list(m)]

W = lambda u: 'https://en.wikipedia.org/wiki/' + u

# ---------- type groups (tt) for existing kinds ----------
TT = {
 'Cold & flu remedy': [G('Time of day', 'Day (non-drowsy)', 'Night (with a sedating antihistamine)'),
    G('Main ingredients', 'Paracetamol with phenylephrine', 'Paracetamol with pseudoephedrine', 'With dextromethorphan'),
    G('Format', 'Hot-drink powder', 'Capsule or tablet', 'Liquid')],
 'Nasal decongestant': [G('Format', 'Spray', 'Tablet or capsule'), G('Active ingredient', 'Xylometazoline', 'Oxymetazoline', 'Pseudoephedrine', 'Phenylephrine')],
 'Cough medicine': [G('Cough treated', 'Dry (suppressant)', 'Chesty (expectorant)', 'Combined'), G('Active ingredient', 'Dextromethorphan', 'Guaifenesin'), G('Format', 'Syrup', 'Tablet')],
 'Sore-throat lozenge & spray': [G('Action', 'Antiseptic', 'Local anaesthetic', 'Anti-inflammatory', 'Menthol and eucalyptus soothing'),
    G('Active ingredient', 'Amylmetacresol with dichlorobenzyl alcohol', 'Benzocaine', 'Lidocaine', 'Hexylresorcinol', 'Flurbiprofen', 'Benzydamine', 'Phenol'),
    G('Format', 'Lozenge', 'Spray', 'Cough drop')],
 'Antihistamine tablets': [G('Active ingredient', 'Cetirizine', 'Loratadine', 'Fexofenadine', 'Chlorphenamine', 'Diphenhydramine', 'Acrivastine'),
    G('Generation', 'Second-generation (little drowsiness)', 'First-generation (drowsiness listed)'), G('Format', 'Tablet', 'Capsule', 'Liquid or syrup for children')],
 'Allergy nasal spray': [G('Class', 'Steroid', 'Antihistamine'), G('Active ingredient', 'Fluticasone', 'Mometasone', 'Triamcinolone', 'Beclometasone', 'Azelastine')],
 'Painkillers': [G('Active ingredient', 'Paracetamol (acetaminophen)', 'Ibuprofen', 'Aspirin', 'Naproxen', 'Aspirin, paracetamol and caffeine'),
    G('Labelled for', 'General pain', 'Migraine', 'Night-time (with a sleep aid)'), G('Format', 'Tablet', 'Caplet', 'Liquid capsule', 'Soluble')],
 "Children's pain & fever medicine": [G('Active ingredient', 'Paracetamol', 'Ibuprofen'), G('Age', 'Infant (from 2–3 months)', 'Older child (6+ years)'),
    G('Format', 'Oral suspension', 'Sachet', 'Chewable', 'Melt'), G('Free from', 'Sugar', 'Dye')],
 'Topical pain relief': [G('Format', 'Gel', 'Cream or rub', 'Adhesive patch'), G('Action', 'NSAID', 'Cooling (menthol)', 'Warming', 'Counterirritant', 'Local anaesthetic (lidocaine)')],
 'Sleep aid': [G('Active ingredient', 'Diphenhydramine', 'Doxylamine', 'Melatonin (where sold without prescription)'), G('Format', 'Tablet', 'Liquid', 'Capsule')],
 'Indigestion & heartburn remedy': [G('Action', 'Antacid (calcium carbonate, magnesium or aluminium salts, sodium bicarbonate)', 'Alginate (raft-forming)', 'H2 blocker (famotidine)', 'Proton-pump inhibitor (omeprazole)'),
    G('Format', 'Chewable tablet', 'Liquid', 'Effervescent tablet')],
 'Laxative': [G('Action', 'Bulk-forming (psyllium, methylcellulose)', 'Osmotic (macrogol, lactulose)', 'Stimulant (senna, bisacodyl)', 'Stool softener (docusate)', 'Saline (magnesium hydroxide)'),
    G('Format', 'Tablet or liquid', 'Powder sachet', 'Suppository', 'Medicinal enema')],
 'Anti-diarrhoeal': [G('Active ingredient', 'Loperamide', 'Bismuth subsalicylate', 'Kaolin', 'Charcoal'), G('Format', 'Capsule', 'Tablet', 'Melt', 'Liquid', 'Chewable')],
 'Oral rehydration salts': [G('Format', 'Powder sachet', 'Ready-to-drink liquid', 'Freezer pop'), G('Formula', 'WHO low-osmolarity', "Children's flavoured")],
 'Travel-sickness remedy': [G('Active ingredient', 'Dimenhydrinate', 'Meclizine', 'Cinnarizine', 'Promethazine', 'Hyoscine (scopolamine)', 'Ginger'), G('Format', 'Tablet', 'Chewable', 'Skin patch (prescription in many countries)')],
 'Antiseptic': [G('Active ingredient', 'Chlorhexidine or cetrimide', 'Chloroxylenol', 'Povidone-iodine', 'Hydrogen peroxide', 'Benzalkonium chloride'), G('Format', 'Cream', 'Liquid', 'Spray', 'Wipe')],
 'Anti-itch & hydrocortisone cream': [G('Active ingredient', 'Hydrocortisone (low strength)', 'Antihistamine', 'Calamine', 'Menthol'), G('Format', 'Cream', 'Ointment', 'Lotion', 'Cooling gel')],
 'Antifungal treatment': [G('Condition', "Athlete's foot", 'Nail fungus', 'Thrush'), G('Active ingredient', 'Clotrimazole', 'Miconazole', 'Terbinafine', 'Amorolfine'), G('Format', 'Cream', 'Spray', 'Powder', 'Nail lacquer', 'Pessary')],
 'Cold-sore treatment': [G('Treatment', 'Aciclovir cream', 'Docosanol cream', 'Hydrocolloid patch', 'Anaesthetic gel')],
 'Corn, wart & verruca treatment': [G('Condition', 'Corn', 'Callus', 'Wart', 'Verruca'), G('Method', 'Salicylic-acid plaster or pad', 'Salicylic-acid gel or liquid', 'Freeze spray', 'Hydrocolloid corn plaster')],
 'Head-lice treatment': [G('Treatment', 'Dimeticone lotion or spray', 'Permethrin', 'Malathion', 'Fine-toothed detection comb')],
 'Eye drops': [G('Purpose', 'Lubricating (artificial tears)', 'Allergy', 'Redness relief'), G('Formulation', 'With preservative', 'Preservative-free', 'Gel')],
 'Ear drops': [G('Purpose', 'Earwax softening', "Swimmer's ear drying", 'Outer-ear soreness'), G('Active ingredient', 'Carbamide peroxide', 'Olive oil', 'Sodium bicarbonate'), G('Format', 'Drops', 'Spray')],
 'Teething gel': [G('Active ingredient', 'Lidocaine', 'Benzocaine (not for under-2s in the US)', 'Choline salicylate (not for under-16s in the UK)', 'None (massage gel)', 'Homeopathic or herbal')],
 'Nicotine replacement': [G('Form', 'Patch', 'Chewing gum', 'Lozenge or pastille', 'Mouth spray', 'Inhalator', 'Nasal spray', 'Sublingual tablet')],
 'Homeopathic single remedy': [G('Format', 'Pillules', 'Liquid dilution'), G('Potency scale', 'Centesimal (C)', 'Decimal (D or X)', 'Quintamillesimal (Q or LM)')],
 'Traditional medicine preparation': [G('System', 'Chinese', 'Kampo', 'Ayurvedic', 'Unani', 'Western herbal'),
    G('Format', 'Teapills', 'Honey pills', 'Powders', 'Granules', 'Herbal tablets', 'Plasters', 'Liniments', 'Medicated oils')],
 # monitors
 'Blood-pressure monitor': [G('Where the cuff sits', 'Upper arm', 'Wrist', 'Wearable (watch or band)'), G('Features', 'Irregular-heartbeat (AFib) detection', 'Bluetooth or app connection')],
 'Manual blood-pressure kit': [G('Supplied with', 'Stethoscope', 'Cuff only'), G('Cuff size', 'Child', 'Adult', 'Large adult')],
 'Digital thermometer': [G('Where it reads', 'Mouth or armpit (stick)', 'Ear', 'Forehead')],
 'Pulse oximeter': [G('Where it is worn', 'Fingertip clip', 'Wrist with finger sensor')],
 'Personal ECG monitor': [G('Leads', 'Single-lead', 'Six-lead')],
 'Peak flow meter': [G('Display', 'Mechanical', 'Digital'), G('Range', 'Standard (adult)', 'Low range (child)')],
 'Continuous glucose monitor': [G('Readings', 'Real-time', 'Flash (scan on demand)'), G('Supply', 'Prescription', 'Over the counter'), G('Placement', 'Skin-worn', 'Implantable')],
 'Blood glucose meter': [G('Features', 'Standard', 'Bluetooth or app connection', 'Glucose and ketone', 'Pump-linked'), G('Supplies', 'Test strips', 'Lancets and lancing device')],
 'Insulin pump': [G('Design', 'Tubed', 'Patch (tubeless)'), G('Control', 'Manual dosing', 'Automated insulin delivery (hybrid closed loop)'), G('Supplies', 'Infusion sets', 'Reservoirs')],
 'Insulin pen': [G('Design', 'Reusable (cartridge)', 'Disposable prefilled', 'Smart (connected)'), G('Add-on', 'Smart pen cap', 'Pen needles')],
 'Adrenaline auto-injector': [G('Dose', '0.1 mg (infant)', '0.15 mg (child)', '0.3 mg (adult)', '0.5 mg'), G('Feature', 'Voice-guided')],
 'Pill organiser & dispenser': [G('Design', 'Weekly pill box', 'Day-and-time organiser', 'Travel or pen-shaped case', 'Locking or Braille-marked organiser'),
    G('Dispenser', 'Automatic carousel with alarm', 'Connected smart dispenser with app alerts')],
 'Infection test kit': [G('Infection', 'COVID-19 antigen', 'Combined COVID-19 and flu A/B', 'Combined COVID-19, flu and RSV')],
 'Urine test strips': [G('Looks for', 'Urinary infection (nitrite and leukocyte)', 'Ketones', 'Up to 10 parameters'), G('Reading', 'Colour chart', 'Smartphone')],
 'HIV self-test': [G('Sample', 'Oral fluid', 'Fingerstick blood')],
 'Bowel screening test': [G('Method', 'Faecal immunochemical test (FIT)', 'Guaiac faecal occult blood test', 'Multi-target stool DNA test')],
 'Cholesterol test': [G('Result', 'Total cholesterol only', 'Full lipid panel'), G('Reader', 'Meter with test strips', 'Single-use cassette')],
 'Breathalyser': [G('Sensor', 'Fuel cell', 'Semiconductor'), G('Use', 'Personal reusable', 'Single-use disposable', 'Smartphone-connected')],
 # first aid
 'First-aid kit': [G('Setting', 'Home and leisure', 'Car', 'Workplace', 'Travel', 'Outdoor and wilderness', 'Trauma (IFAK)'),
    G('Standard met', 'BS 8599-1 workplace (small, medium, large)', 'BS 8599-2 vehicle', 'DIN 13157 or 13169 workplace', 'DIN 13164 vehicle', 'ANSI/ISEA Z308.1')],
 'Plaster': [G('Material', 'Fabric (flexible)', 'Waterproof film', 'Hydrogel or transparent', 'Hydrocolloid (blister)'), G('Made for', 'Sensitive skin', "Children's printed designs"), G('Supply', 'Individual', 'Strip roll to cut')],
 'Bandage': [G('Form', 'Roller (gauze, conforming)', 'Triangular (sling, cravat)', 'Tubular', 'Cohesive (self-adhering)', 'Elastic compression (short-stretch, long-stretch)')],
 'Wound-closure strip': [G('Shape', 'Straight strip', 'Butterfly')],
 'Liquid bandage': [G('Applied as', 'Brush-on liquid', 'Spray')],
 'Home defibrillator': [G('Operation', 'Semi-automatic (rescuer presses shock)', 'Fully automatic'), G('Guidance', 'Voice prompts only', 'With CPR feedback')],
 'Medical face mask': [G('Standard', 'EN 14683 Type I', 'EN 14683 Type II', 'EN 14683 Type IIR'), G('Fastening', 'Ear loops', 'Head ties')],
 'Joint support / brace': [G('Joint', 'Knee', 'Ankle', 'Back', 'Wrist and hand', 'Elbow', 'Neck'), G('Construction', 'Sleeve', 'Strapped', 'Hinged', 'Lace-up', 'Rigid-stay', 'Walker boot', 'Soft or rigid collar')],
 'Orthotic insole': [G('Make', 'Prefabricated', 'Custom-made from a cast or scan', 'Heat-mouldable'), G('Length', 'Full', 'Three-quarter'), G('Arch', 'Low', 'Medium', 'High'), G('Made for', 'Everyday', 'Running', 'Court sport')],
 'Compression stocking': [G('Pressure', 'Support (about 8–20 mmHg)', 'Firm medical (20–30, 30–40 mmHg)', 'Anti-embolism'), G('Length', 'Knee-high', 'Thigh-high', 'Tights'), G('Knit', 'Circular', 'Flat'), G('Fit', 'Off the shelf', 'Made to measure'), G('Wearer', 'Maternity')],
 'Leg prosthesis': [G('Amputation level', 'Transtibial (below knee)', 'Transfemoral (above knee)'), G('Knee', 'Mechanical or hydraulic', 'Microprocessor', 'Powered'), G('Foot', 'Carbon-fibre energy-storing', 'Running blade', 'Waterproof')],
 'Arm prosthesis': [G('Power source', 'Cosmetic (passive)', 'Body-powered', 'Myoelectric', 'Multi-articulating bionic'), G('Extent', 'Partial hand or finger', 'Hand', 'Below elbow', 'Above elbow'), G('Terminal device', 'Hook', 'Hand', 'Activity attachment')],
 'Breast prosthesis': [G('Material', 'Full silicone', 'Lightweight silicone', 'Foam or fibre (non-silicone)'), G('Shape', 'Full form', 'Partial form or shell'), G('Wear', 'In a bra', 'Adhesive (attachable)', 'Swim form')],
 'Eye prosthesis': [G('Extent', 'Full ocular prosthesis', 'Scleral shell')],
 'Facial prosthesis': [G('Part replaced', 'Ear', 'Nose', 'Orbital', 'Finger or partial hand'), G('Retention', 'Adhesive', 'Implant-retained')],
 # supplements
 'Multivitamin': [G('Wearer', 'Adult', "Men's", "Women's", '50+', 'Prenatal', "Children's", 'Teen'), G('Format', 'Tablet', 'Chewable', 'Gummy')],
 'Vitamin supplement': [G('Vitamin', 'D (D3, D3 with K2)', 'C', 'B12', 'B complex', 'Folic acid', 'Biotin', 'E', 'K', 'A'), G('Format', 'Tablet', 'Capsule', 'Gummy', 'Spray', 'Liquid')],
 'Mineral supplement': [G('Mineral', 'Magnesium', 'Iron', 'Zinc', 'Calcium (with vitamin D)', 'Selenium', 'Iodine', 'Potassium', 'Chromium'),
    G('Salt form', 'Magnesium glycinate', 'Magnesium citrate', 'Magnesium oxide', 'Ferrous sulphate', 'Gentle (chelated) iron')],
 'Omega-3 oil': [G('Source', 'Fish oil', 'Cod liver oil', 'Krill oil', 'Algal (vegan) oil'), G('Strength', 'Standard', 'High-strength concentrate'), G('Format', 'Softgel', 'Liquid', 'Gummy')],
 'Probiotic': [G('Content', 'Single-strain', 'Multi-strain', 'Yeast (Saccharomyces boulardii)'), G('Format', 'Capsule', 'Powder or sachet', 'Gummy'), G('Wearer', "Children's")],
 'Herbal supplement': [G('Plant', 'Ashwagandha', 'Turmeric', 'Echinacea', 'Ginseng', "St John's wort", 'Valerian'), G('Format', 'Capsule or tablet', 'Powder', 'Tincture')],
 'Collagen': [G('Source', 'Bovine', 'Marine'), G('Format', 'Peptide powder', 'Ready-to-drink', 'Gummy', 'Capsule')],
 'Combination supplement': [G('Aimed at', 'Joints', 'Hair, skin and nails', 'Sleep and stress (magnesium with ashwagandha)')],
 'Tonic & essence': [G('Base', 'Chicken essence', 'Herbal-infused essence')],
 'Protein powder': [G('Protein source', 'Whey concentrate', 'Whey isolate', 'Hydrolysed whey', 'Clear whey', 'Casein', 'Plant (pea, rice, soy blends)', 'Egg white'), G('Aim', 'Standard', 'Diet or low-calorie blend')],
 'Mass gainer': [G('Calorie level', 'Standard', 'High-calorie', 'Lean'), G('Diet', 'Dairy-based', 'Vegan'), G('Added', 'Creatine')],
 'Creatine': [G('Form', 'Monohydrate powder', 'Micronised', 'Hydrochloride (HCl)', 'Capsules', 'Gummies'), G('Blend', 'With HMB')],
 'Pre-workout': [G('Stimulant level', 'Stimulant', 'High-stim', 'Stim-free'), G('Format', 'Powder', 'Ready-to-drink', 'Capsules')],
 'Amino acids': [G('Amino acid', 'BCAA', 'EAA', 'Glutamine', 'Citrulline', 'Beta-alanine'), G('Format', 'Powder', 'Capsules')],
 'Fat burner': [G('Type', 'Thermogenic (stimulant)', 'Stim-free', 'L-carnitine'), G('Format', 'Capsules', 'Powder')],
 'Energy gel & chew': [G('Form', 'Gel', 'Chew or blok'), G('Concentration', 'Standard concentrated', 'Isotonic (pre-diluted)', 'Hydrogel', 'Liquid'), G('Added', 'Caffeine', 'Electrolytes')],
 'Electrolyte drink mix': [G('Format', 'Powder tub', 'Stick or sachet', 'Effervescent tablet'), G('Content', 'Carbohydrate-electrolyte (energy) mix', 'Low or zero sugar', 'High sodium', 'Caffeinated')],
 'Meal-replacement shake': [G('Format', 'Powder', 'Ready-to-drink bottle', 'Bar or hot meal'), G('Diet', 'Vegan', 'High-protein, lower-carb', 'Weight-control')],
 'Oral nutritional supplement': [G('Energy density', 'Standard (about 1–1.5 kcal/ml)', 'Compact high-energy'), G('Focus', 'High-protein', 'Diabetes-specific'), G('Format', 'Ready-to-drink', 'Powder to mix with milk', 'Juice style')],
 'Medical-condition formula': [G('Condition', 'Milk allergy (extensively hydrolysed)', 'Severe allergy (amino-acid based)', 'Metabolic (for example phenylalanine-free for PKU)'), G('Age', 'Infant', 'Child'), G('Completeness', 'Nutritionally complete', 'Nutritionally incomplete')],
 # breathing, sleep, pain
 'CPAP machine': [G('Pressure', 'Fixed', 'Auto-adjusting (APAP)'), G('Size', 'Standard', 'Travel'), G('Humidifier', 'Heated', 'None'), G('Mask style', 'Nasal pillows', 'Nasal', 'Full-face', 'Hybrid')],
 'Oxygen concentrator': [G('Use', 'Home (stationary)', 'Portable'), G('Flow', 'Continuous', 'Pulse dose')],
 'Nebuliser': [G('Mechanism', 'Jet (compressor)', 'Vibrating mesh', 'Ultrasonic'), G('Wearer', "Children's with mask")],
 'Inhaler spacer': [G('Design', 'Valved holding chamber', 'Anti-static chamber', 'Collapsible bag'), G('Interface', 'Mouthpiece', 'Child mask', 'Infant mask')],
 'Steam inhaler': [G('Design', 'Electric personal inhaler with mask', 'Bowl or cup inhaler')],
 'Anti-snoring device': [G('Mechanism', 'Mandibular advancement mouthpiece (boil-and-bite)', 'Custom dentist-made splint', 'Tongue-retaining device', 'Nasal dilator', 'Chin strap')],
 'Light-therapy lamp': [G('Design', '10,000-lux light box', 'Blue-light energy light', 'Wake-up light (dawn simulator)'), G('Size', 'Desk', 'Portable')],
 'Weighted blanket': [G('Filling', 'Glass beads', 'Poly pellets'), G('Construction', 'Quilted', 'Knitted chunky weave'), G('Size', 'Adult', 'Child'), G('Weight', 'Fixed', 'Adjustable')],
 'TENS/EMS unit': [G('Function', 'TENS (pain)', 'EMS (muscle stimulation)', 'Combined TENS/EMS'), G('Made for', 'Labour (maternity)'), G('Pads', 'Wired', 'Wireless, app-controlled')],
 'Heat & cold pack': [G('Temperature', 'Heat', 'Cold'), G('Construction', 'Self-heating patch', 'Electric heat pad', 'Gel pack', 'Instant cold pack', 'Hot-water bottle', 'Microwavable wheat bag')],
 'Orthopaedic pillow': [G('Supports', 'Neck (cervical contour)', 'Back or reflux (wedge)', 'Knee and leg'), G('Filling', 'Foam', 'Water-based')],
 # mobility
 'Walking stick': [G('Base', 'Single-point', 'Quad', 'Tripod'), G('Handle', 'Crook', 'Derby', 'Fischer (anatomic)'), G('Design', 'Fixed length', 'Folding', 'Seat stick')],
 'Crutches': [G('How it supports', 'Forearm (elbow)', 'Underarm (axillary)', 'Platform (trough)'), G('Design', 'Fixed', 'Folding travel')],
 'Walking frame': [G('Wheels', 'None (pick-up)', 'Two front wheels'), G('Design', 'Fixed', 'Folding')],
 'Rollator': [G('Wheels', 'Three (delta)', 'Four'), G('Use', 'Indoor', 'Outdoor and all-terrain'), G('Build', 'Standard', 'Lightweight carbon', 'Bariatric')],
 'Knee walker': [G('Steering', 'Steerable', 'Non-steerable'), G('Terrain', 'Indoor', 'All-terrain')],
 'Collector cane': [G('Handle', 'Silver-topped', 'Carved or ivory-style'), G('Shaft', 'Malacca (rattan)', 'Ash', 'Blackthorn', 'Bamboo'), G('Fitting', 'Folding', 'Hidden compartment', 'Tippling flask', 'Gadget (compass or tool)', 'Seat (shooting stick)')],
 'Manual wheelchair': [G('Pushed by', 'Attendant (transit)', 'User (self-propelled)'), G('Frame', 'Folding', 'Rigid ultralight'), G('Use', 'Everyday', 'Active', 'Sports', 'Beach and all-terrain'), G('Capacity', 'Standard', 'Bariatric')],
 'Powered wheelchair': [G('Drive wheels', 'Front-wheel', 'Mid-wheel', 'Rear-wheel'), G('Use', 'Folding travel', 'Indoor and outdoor', 'Complex rehab'), G('Seating', 'Tilt', 'Recline', 'Elevate')],
 'Mobility scooter': [G('Size', 'Boot or travel (dismantling or folding)', 'Mid-size', 'Full-size'), G('Class', 'Pavement (UK Class 2)', 'Road (UK Class 3)'), G('Wheels', 'Three', 'Four'), G('Terrain', 'Pavement', 'All-terrain')],
 'Wheelchair power add-on': [G('Where the motor sits', 'Push-rim assist wheels', 'Rear power-assist drive', 'Front handbike attachment', 'Attendant power pack')],
 'Wheelchair parts & accessories': [G('Part', 'Seat cushion', 'Backrest', 'Wheels and push-rims', 'Tyres and castors', 'Armrests and side guards', 'Footplates and legrests', 'Batteries and chargers', 'Joysticks and controls', 'Bags, trays and weather covers')],
 'Portable ramp': [G('Design', 'Threshold ramp', 'Singlefold suitcase ramp', 'Multifold ramp', 'Telescopic channel ramps', 'Rollable ramp', 'Semi-permanent modular ramp')],
 'Patient lift': [G('Design', 'Mobile floor hoist', 'Folding portable hoist', 'Powered sit-to-stand lift'), G('Power', 'Electric', 'Hydraulic (manual pump)'), G('Accessory', 'Sling')],
 'Transfer aid': [G('Aid', 'Transfer (sliding) board', 'Pivot disc', 'Non-powered sit-to-stand aid', 'Car transfer plate')],
 'Mobility vehicle lift': [G('Design', 'Hitch-mounted platform', 'Inside platform', 'Boot crane hoist', 'Rotating seat or person-transfer lift')],
 # daily living
 'Shower chair': [G('Design', 'Stool', 'Chair with back', 'Chair with arms', 'Swivel bath seat', 'Bath board'), G('Mounting', 'Free-standing', 'Wall-mounted fold-down')],
 'Raised toilet seat': [G('Fixing', 'Clamp-on', 'Loose-fitting'), G('Extras', 'Armrests', 'Lid', 'Bidet'), G('Height', 'Fixed', 'Adjustable')],
 'Toilet safety frame': [G('Mounting', 'Free-standing', 'Fixed to toilet', 'Floor-fixed'), G('Height', 'Fixed', 'Adjustable')],
 'Commode chair': [G('Mobility', 'Static', 'Wheeled shower commode', 'Self-propelled'), G('Use', '3-in-1 over-toilet'), G('Capacity', 'Standard', 'Bariatric')],
 'Bath lift': [G('Design', 'Battery reclining seat', 'Inflatable cushion', 'Fixed seat')],
 'Tub transfer bench': [G('Seat', 'Standard', 'Sliding'), G('Extras', 'Padded', 'With commode opening')],
 'Incontinence pads & pants': [G('Product', 'Liner', 'Pad', 'Pull-up pants', 'All-in-one brief', "Men's guard", 'Washable underwear'), G('Absorbency', 'Light', 'Moderate', 'Heavy', 'Overnight')],
 'Bed & chair protector': [G('Reuse', 'Disposable', 'Washable'), G('Purpose', 'Leak protection', 'Positioning (turning a person)')],
 'Stoma appliance': [G('Pieces', 'One-piece', 'Two-piece (baseplate and pouch)'), G('Output', 'Closed', 'Drainable', 'Urostomy'), G('Barrier', 'Flat', 'Convex'), G('Accessory', 'Barrier seal')],
 'Intermittent catheter': [G('Coating', 'Hydrophilic (ready to use)', 'Gel pre-lubricated', 'Uncoated'), G('Format', 'Standard', 'Compact', 'No-touch sleeve'), G('Tip', 'Straight', 'Coudé')],
 'Care bed': [G('Adjustment', 'Semi-electric', 'Full-electric'), G('Height', 'Standard', 'Low or floor bed'), G('Capacity', 'Standard', 'Bariatric')],
 'Pressure-relief mattress': [G('Mechanism', 'Static foam', 'Hybrid foam and air', 'Alternating-pressure air', 'Low-air-loss'), G('Format', 'Mattress', 'Overlay')],
 'Pressure-relief cushion': [G('Filling', 'Foam', 'Gel', 'Air-cell', 'Hybrid')],
 'Bed rail': [G('Design', 'Full-length side rail', 'Half rail', 'Bed assist handle', 'Bumper or rail cover')],
 'Personal alarm': [G('Worn as', 'Pendant', 'Wrist'), G('Trigger', 'Button press', 'Automatic fall detector'), G('Range', 'Home only', 'GPS')],
 'Medical ID': [G('Form', 'Bracelet', 'Tag', 'Card', 'Keyring')],
 'Wandering detector': [G('Sensor', 'Door alarm', 'Motion sensor')],
 'Reacher': [G('Length', 'Standard', 'Long (wheelchair-user)'), G('Design', 'Folding', 'Rotating jaw', 'Magnetic tip', 'Forearm support or power grip')],
 'Dressing aid': [G('Helps with', 'Socks (sock aid)', 'Compression stockings', 'Buttons (button hook)', 'Zips (zip puller)', 'Shoes (long-handled shoehorn, elastic laces)', 'Clothes (dressing stick)')],
 'Adapted cutlery & cups': [G('Item', 'Cutlery', 'Plate or dish', 'Cup or mug'),
    G('Adaptation', 'Built-up handle', 'Angled or bendable', 'Weighted', 'Electronic stabilising', 'Plate guard or lipped dish', 'Suction or non-slip base', 'Two-handled', 'No-spill lid')],
 # hearing
 'Hearing aid': [G('Style', 'Receiver-in-canal (RIC)', 'Behind-the-ear (BTE, miniBTE, power BTE)', 'In-the-ear (full or half shell)', 'In-the-canal (ITC)', 'Completely-in-canal (CIC)', 'Invisible-in-canal (IIC)', 'Extended-wear'),
    G('Power', 'Rechargeable', 'Disposable battery (sizes 10, 312, 13, 675)'), G('Special fitting', 'CROS or BiCROS', 'Paediatric')],
 'Over-the-counter hearing aid': [G('Style', 'Receiver-in-ear', 'Earbud style', 'Completely-in-canal', 'Behind-the-ear')],
 'Implant sound processor': [G('Implant', 'Cochlear', 'Bone-anchored (abutment)', 'Transcutaneous bone-conduction', 'Non-surgical bone-conduction'), G('Worn', 'Behind the ear', 'Off the ear (single unit)')],
 'Hearing-aid spare parts': [G('Part', 'Batteries', 'Domes and ear tips', 'Wax guards and filters', 'Thin tubes', 'Receivers'), G('Battery size', '10', '312', '13', '675')],
 'Hearing-aid streamer & remote mic': [G('Function', 'TV streamer', 'Remote microphone', 'Remote control')],
 'Alerting system': [G('Signal', 'Vibrating alarm clock', 'Bed shaker', 'Doorbell and phone flasher', 'Smoke-alarm transmitter and shaker'), G('Receiver', 'Pager', 'Wrist receiver')],
 # vision
 'Spectacle lens': [G('Design', 'Single vision', 'Aspheric or freeform single vision', 'Bifocal', 'Progressive (varifocal)', 'Personalised progressive', 'Office or occupational', 'Myopia control (children)'),
    G('Material', 'CR-39 (1.5)', 'Polycarbonate', '1.6 high-index', '1.67 high-index', '1.74 high-index', 'Glass'),
    G('Coating or tint', 'Hard coat', 'Anti-reflective', 'Blue-light filter', 'Photochromic', 'Polarised', 'Tint', 'Mirror')],
 'Soft contact lens': [G('Replacement', 'Daily disposable', 'Two-weekly', 'Monthly'), G('Correction', 'Spherical', 'Toric (astigmatism)', 'Multifocal (presbyopia)'), G('Material', 'Silicone hydrogel', 'Hydrogel'), G('Look', 'Clear', 'Coloured or cosmetic')],
 'Rigid contact lens': [G('Type', 'Corneal gas-permeable', 'Orthokeratology (overnight reshaping)', 'Scleral'), G('Correction', 'Spherical', 'Toric', 'Multifocal')],
 'Contact-lens solution & drops': [G('Product', 'Multipurpose solution', 'Hydrogen peroxide system', 'Saline rinse', 'Rigid-lens cleaner and conditioner', 'Rewetting drops')],
 'Handheld magnifier': [G('Light', 'Plain lens', 'LED-illuminated'), G('Form', 'Pocket or folding', 'Sheet (Fresnel) page magnifier')],
 'Stand magnifier': [G('Light', 'Plain lens', 'LED-illuminated'), G('Lens', 'Dome', 'Bar (bright-field)')],
 'Electronic magnifier': [G('Form', 'Handheld', 'Portable with stand', 'Desktop', 'Wearable or head-mounted')],
 'Low-vision glasses': [G('Optics', 'Spectacle magnifier (near)', 'Galilean telescope glasses (distance, TV)', 'Bioptic telescope'), G('Fitting', 'Worn as glasses', 'Clip-on or flip-down')],
 'White cane': [G('Role', 'Long cane', 'Guide cane', 'Identification (symbol) cane', 'Support cane', 'Children\'s cane'), G('Construction', 'Folding', 'Rigid', 'Telescopic'), G('Material', 'Aluminium', 'Graphite', 'Fibreglass'), G('Tip', 'Pencil', 'Marshmallow', 'Roller', 'Rolling ball')],
 'Braille device': [G('Form', 'Mechanical braille writer', 'Refreshable braille display (14–80 cells, usually 40)', 'Braille note-taker (18–40 cells)')],
 'Communication aid': [G('Form', 'Dedicated speech-generating device', 'Tablet with communication app', 'Handheld communicator', 'Picture or letter board', 'Communication book')],
 'Eye-gaze device': [G('Form', 'Add-on eye tracker', 'Integrated eye-gaze tablet')],
 # sexual health & family
 'Condom': [G('Worn', 'External', 'Internal (female)'), G('Material', 'Latex', 'Non-latex'), G('Fit', 'Standard', 'Thin', 'Large'), G('Surface', 'Smooth', 'Textured')],
 'Emergency contraceptive pill': [G('Active ingredient', 'Levonorgestrel', 'Ulipristal acetate')],
 'Dental dam': [G('Material', 'Latex', 'Non-latex'), G('Flavour', 'Unflavoured', 'Flavoured')],
 'Pregnancy test': [G('Format', 'Test strip', 'Midstream stick', 'Cup-dip cassette'), G('Result display', 'Lines', 'Digital read-out', 'Digital with weeks estimate'), G('Timing', 'Standard', 'Early detection (before a missed period)')],
 'Ovulation test': [G('Hormone measured', 'LH', 'LH and oestrogen', 'Progesterone (PdG) confirmation', 'FSH (ovarian reserve)'), G('Format', 'Strip', 'Midstream stick', 'Digital reader', 'App-connected reader')],
 'Fertility monitor': [G('Method', 'Urine hormone reader (LH and oestrogen)', 'Multi-hormone app reader', 'Temperature-based cycle computer')],
 'Basal-body thermometer': [G('Style', 'Oral digital (two decimal places)', 'Bluetooth app-linked', 'Wearable overnight sensor')],
 'Sperm test kit': [G('Test', 'Concentration threshold (male fertility)', 'Post-vasectomy', 'Smartphone video motility')],
 'Breast pump': [G('Power', 'Manual', 'Single electric', 'Double electric'), G('Style', 'Handheld or portable', 'Wearable (in-bra)')],
 'Nursing pad': [G('Reuse', 'Disposable', 'Reusable washable', 'Reusable silicone')],
 'Nipple cream': [G('Base', 'Lanolin', 'Lanolin-free balm')],
 'Pelvic-floor trainer': [G('Method', 'App-connected biofeedback', 'Electrical muscle stimulation')],
 'Vaginal dilator': [G('Supply', 'Graduated set', 'Single dilator'), G('Material', 'Silicone', 'Rigid plastic')],
 'Vacuum erection device': [G('Pump', 'Manual', 'Battery')],
 'Erection ring': [G('Material', 'Elastic band', 'Silicone')],
}

SEE = {
 'Plaster': [['C8', 'Plaster', 'builder\'s wall plaster, a different object with the same name']],
 'Handheld magnifier': [['E6', 'Handheld magnifier', 'the same tool sold for hobby use']],
 'Stand magnifier': [['E6', 'Stand magnifier', 'the same tool sold for hobby use']],
 'Walking stick': [['A4', 'Fashion cane', 'dress cane worn as an accessory'], ['E2', 'Trekking pole', 'pole for hiking, not a medical aid']],
 'Collector cane': [['A4', 'Fashion cane', 'dress cane worn as an accessory'], ['E4', 'Sword cane', 'cane with a hidden blade']],
 'Orthotic insole': [['A2', 'Insole & heel grip', 'comfort insole sold with shoe care']],
 'Compression stocking': [['A1', 'Tights & stockings', 'fashion hosiery']],
 'Spectacle lens': [['A4', 'Prescription glasses', 'the frames the lenses are glazed into']],
 'Heat & cold pack': [['H1', 'Hot-water bottle', 'comfort item'], ['H1', 'Heat pack & hand warmer', 'comfort item']],
 'Light-therapy lamp': [['B3', 'Wake-up light', 'bedside lamp sold for the home']],
 'Orthopaedic pillow': [['B2', 'Bed pillow', 'ordinary bedding pillow']],
 'Personal alarm': [['B8', 'Personal attack alarm', 'alarm for personal safety, not medical']],
 'Nicotine replacement': [['J10', 'Nicotine pouch', 'nicotine product that is not a quit aid']],
 'Electrolyte drink mix': [['J9', 'Electrolyte drink & tablets', 'ready-made and tablet drinks']],
 'Protein powder': [['J9', 'Protein & recovery drink', 'ready-to-drink protein']],
 'Probiotic': [['J3', 'Probiotic cultured drink', 'probiotic as a food']],
 'Multivitamin': [['J9', 'Functional & vitamin drink', 'vitamins in a drink']],
 'Erection ring': [['H3', 'Penis ring', 'sold as a sex toy']],
 'Vacuum erection device': [['H3', 'Penis pump', 'sold as a sex toy']],
 'Vaginal dilator': [['H3', 'Dilator', 'sold as a sex toy']],
 'Digital thermometer': [['C1', 'Infrared thermometer', 'workshop tool, not for the body'], ['H2', 'Basal-body thermometer', 'fertility tracking']],
 'Basal-body thermometer': [['H2', 'Digital thermometer', 'general body temperature']],
 'TENS/EMS unit': [['H1', 'Handheld massager', 'massage for comfort']],
 'Alerting system': [['B8', 'Smoke alarm', 'ordinary alarm the transmitter listens to']],
 'Toilet safety frame': [['G3', 'Grab bar', 'fixed rail built into a bathroom']],
 'Mobility scooter': [['G1', 'Scooter', 'motor scooter, a different vehicle']],
 'Medical face mask': [['C1', 'Respirator', 'protective mask for dust and fumes']],
 'Portable ramp': [['G3', 'Stairlift', 'built-in way past stairs']],
 'Walking frame': [['H2', 'Rollator', 'walking frame on wheels with brakes']],
 'Bath lift': [['H2', 'Tub transfer bench', 'bench that slides a person into the bath']],
 'Pelvic-floor trainer': [['H2', 'Incontinence pads & pants', 'leakage products']],
}

# ---------- new kinds ----------
def N(n, a, d, s, tt=None):
    k = {'n': n, 'a': a, 'd': d, 's': s}
    if tt: k['tt'] = tt
    return k
NEW = {
 'Vapour rub & inhalant': N('Vapour rub & inhalant', 'chest rub · menthol rub', 'Menthol, camphor and eucalyptus ointment rubbed on the chest or inhaled to ease a blocked nose and cough.', W('Vicks'),
    [G('Format', 'Chest rub', 'Inhalant stick', 'Steam capsule or oil')]),
 'Nasal rinse & saline spray': N('Nasal rinse & saline spray', 'sinus rinse · neti pot', 'Salt-water spray or rinse kit that flushes mucus and allergens from the nose.', W('Nasal_irrigation'),
    [G('Device', 'Saline spray', 'Squeeze bottle', 'Neti pot', 'Bulb syringe'), G('Supply', 'Pre-mixed solution', 'Sachets to mix')]),
 'Wind & bloating remedy': N('Wind & bloating remedy', 'simethicone · anti-gas', 'Anti-foaming medicine, usually simeticone, taken for trapped wind and bloating.', W('Simethicone'),
    [G('Format', 'Chewable tablet', 'Capsule', 'Drops for infants')]),
 'Haemorrhoid treatment': N('Haemorrhoid treatment', 'piles cream · piles treatment', 'Cream, ointment or suppository applied to soothe haemorrhoids, often with a local anaesthetic or barrier base.', W('Hemorrhoid'),
    [G('Format', 'Cream or ointment', 'Suppository', 'Medicated wipe')]),
 'Oral syringe & dosing spoon': N('Oral syringe & dosing spoon', 'medicine measure · dosing cup', 'Needleless syringe, spoon or cup that measures a dose of liquid medicine.', W('Oral_syringe'),
    [G('Device', 'Oral syringe', 'Dosing spoon', 'Dosing cup', 'Dropper'), G('Wearer', 'Infant', 'Child', 'Adult')]),
 'Pill cutter': N('Pill cutter', 'pill splitter · pill crusher', 'Small blade holder that cuts a tablet in two; some models also crush it.', W('Pill_splitting'),
    [G('Function', 'Splitter', 'Crusher', 'Splitter and crusher')]),
 'Wound dressing': N('Wound dressing', 'gauze pad · non-stick pad', 'Sterile pad laid over a wound and held with tape or a bandage; larger than a plaster.', W('Dressing_(medical)'),
    [G('Material', 'Gauze', 'Non-adherent pad', 'Foam', 'Hydrocolloid', 'Film'), G('Form', 'Pad', 'Island dressing', 'Roll')]),
 'Medical tape': N('Medical tape', 'surgical tape · micropore tape', 'Roll of adhesive tape that holds a dressing or bandage in place.', W('Dressing_(medical)'),
    [G('Material', 'Paper (microporous)', 'Cloth', 'Plastic film'), G('Skin', 'Standard', 'Sensitive')]),
 'Burn dressing': N('Burn dressing', 'burn gel pad · hydrogel dressing', 'Cooling gel dressing that covers a minor burn or scald.', W('Dressing_(medical)'),
    [G('Format', 'Gel-soaked pad', 'Gel sachet', 'Spray')]),
 'Splint & sling': N('Splint & sling', 'arm sling · finger splint', 'Support that keeps an injured arm, hand or finger still while it heals.', W('Sling_(medicine)'),
    [G('Part held', 'Arm (sling)', 'Wrist', 'Finger', 'Thumb'), G('Material', 'Cotton or fabric', 'Foam', 'Aluminium and foam')]),
 'Disposable medical gloves': N('Disposable medical gloves', 'examination gloves · nitrile gloves', 'One-use gloves worn when treating wounds or cleaning up, to limit cross-contamination.', W('Medical_glove'),
    [G('Material', 'Nitrile', 'Latex', 'Vinyl'), G('Powder', 'Powder-free', 'Powdered')]),
 'Emergency foil blanket': N('Emergency foil blanket', 'space blanket · rescue blanket', 'Thin heat-reflecting sheet that stops body heat loss after an accident or exposure.', W('Space_blanket'),
    [G('Size', 'Adult', 'Child'), G('Finish', 'Silver and gold', 'Silver only')]),
 'Sterile eyewash': N('Sterile eyewash', 'eye wash · eye bath', 'Sterile saline in a bottle, pod or wall station that rinses the eye after dust or a splash.', W('Eyewash'),
    [G('Format', 'Bottle', 'Single-use pod', 'Wall-mounted station')]),
 'Gait trainer': N('Gait trainer', 'posterior walker · supportive walker', 'Wheeled frame with body support, harness or seat that helps a child or adult practise walking.', W('Mobility_aid'),
    [G('Support', 'Posterior (behind the user)', 'Anterior (in front)'), G('Wearer', 'Child', 'Adult')]),
 'Lift chair': N('Lift chair', 'riser recliner · rise and recline chair', 'Powered armchair that tilts the whole seat forward to help the user stand, often with a recline.', W('Lift_chair'),
    [G('Motors', 'Single motor', 'Dual motor', 'Triple or quad motor'), G('Position', 'Two-position', 'Three-position', 'Infinite')]),
 'Bedpan & urinal': N('Bedpan & urinal', 'commode pan · urine bottle', 'Bed-side receptacle for passing urine or stools without leaving bed.', W('Bedpan'),
    [G('Item', 'Bedpan', 'Male urinal', 'Female urinal', 'Fracture pan'), G('Material', 'Plastic', 'Stainless steel', 'Disposable pulp')]),
 'Urine drainage bag': N('Urine drainage bag', 'leg bag · catheter bag', 'Bag strapped to the leg or hung from the bed that collects urine from a catheter.', W('Urinary_catheterization'),
    [G('Worn', 'Leg bag', 'Night (bed) bag'), G('Outlet', 'Tap', 'Drainable')]),
 'External catheter': N('External catheter', 'condom catheter · male external catheter', 'Sheath worn on the penis that carries urine to a drainage bag, with no tube inside the body.', W('Urinary_catheterization'),
    [G('Fixing', 'Self-adhesive', 'Strapped')]),
 'Bathing & washing aid': N('Bathing & washing aid', 'long-handled sponge · bottom wiper', 'Long-handled sponge, brush or wiper that lets a person with limited reach wash and toilet alone.', 'https://www.completecareshop.co.uk/bathing-aids',
    [G('Aid', 'Long-handled sponge', 'Bath brush', 'Bottom wiper', 'Bath step', 'Non-slip bath mat')]),
 'Jar opener & grip aid': N('Jar opener & grip aid', 'tap turner · jar opener', 'Tool that gives grip or leverage to open jars, bottles and taps for people with weak hands.', 'https://en.wikipedia.org/wiki/Jar_opener',
    [G('Opens', 'Jar lid', 'Bottle top', 'Can ring-pull'), G('Mechanism', 'Wall-mounted', 'Handheld', 'Electric')]),
 'Amplified telephone': N('Amplified telephone', 'big-button phone · hearing phone', 'Telephone with extra volume and tone control for people with hearing loss.', 'https://en.wikipedia.org/wiki/Assistive_technology',
    [G('Type', 'Corded', 'Cordless', 'Mobile'), G('Feature', 'Large buttons', 'Flashing ringer', 'Hearing-aid compatible')]),
 'Assistive listening system': N('Assistive listening system', 'hearing loop · TV listener', 'Transmitter and receiver that carry sound from a TV, speaker or room straight to a listener or their hearing aid.', W('Hearing_loop'),
    [G('Technology', 'Induction loop', 'FM', 'Infrared'), G('Use', 'TV listening', 'Room or counter loop', 'Portable')]),
 'Electrolarynx': N('Electrolarynx', 'artificial larynx · speech aid', 'Battery device held to the throat that makes a voice for people who have lost their voice box.', W('Electrolarynx'),
    [G('Held', 'Against the neck', 'In the mouth')]),
 'Spermicide': N('Spermicide', 'contraceptive gel · contraceptive film', 'Gel, film or foam placed in the vagina before sex to kill sperm.', W('Spermicide'),
    [G('Format', 'Gel', 'Film', 'Foam')]),
 'Diaphragm & cervical cap': N('Diaphragm & cervical cap', 'cervical barrier', 'Reusable cup fitted over the cervix with spermicide as a barrier contraceptive.', W('Diaphragm_(birth_control)'),
    [G('Shape', 'Diaphragm', 'Cervical cap'), G('Material', 'Silicone', 'Latex')]),
 'Nipple shield': N('Nipple shield', 'breastfeeding shield', 'Thin silicone cover worn over the nipple during a feed.', W('Nipple_shield'),
    [G('Size', 'Small', 'Medium', 'Large')]),
 'Breast-milk storage bag': N('Breast-milk storage bag', 'milk bag · freezer bag', 'Sterile freezable bag for storing expressed milk.', W('Breast_pump'),
    [G('Fill', 'Standard', 'Pump-connecting')]),
}

# ---------- structure ----------
def K(*names):
    out = []
    for n in names:
        if n in old: out.append(old[n])
        elif n in NEW: out.append(NEW[n])
        else: raise SystemExit('missing kind ' + n)
    return out

def S(n, t, ax, *names):
    sh = {'n': n, 't': t}
    if ax: sh['ax'] = ax
    sh['k'] = K(*names)
    return sh

DEPTS = [
 {'n': 'Medicines & remedies', 'mode': 'tier', 'note': 'Grouped by use class only; definitions name the class and active ingredient, never a health claim.',
  't': 'Non-prescription products swallowed, applied, sprayed or dropped to treat a complaint, plus traditional remedies; vitamins and sports products → Supplements & nutrition; devices that read or dose → Monitors, tests & dosing.',
  'ax': 'What complaint is the medicine taken for: colds and allergy, pain and sleep, the gut, skin, eyes, ears and mouth, quitting smoking, or general ills treated by a healing system?',
  's': [
   S('Cold, flu & allergy', 'Remedies for a cold, cough, blocked nose, sore throat or hay fever; a steam device → Breathing, sleep & therapy.', 'kinds by symptom, from a whole cold to the nose, chest and throat, then allergy',
     'Cold & flu remedy', 'Nasal decongestant', 'Nasal rinse & saline spray', 'Vapour rub & inhalant', 'Cough medicine', 'Sore-throat lozenge & spray', 'Antihistamine tablets', 'Allergy nasal spray'),
   S('Pain, fever & sleep', 'Medicines taken or rubbed on for pain, fever or poor sleep; a heat pack or TENS unit → Breathing, sleep & therapy.', 'kinds by what is eased and who takes it: general pain, children, local pain, sleep',
     'Painkillers', "Children's pain & fever medicine", 'Topical pain relief', 'Sleep aid'),
   S('Stomach & bowel', 'Medicines for indigestion, wind, constipation, diarrhoea, dehydration and travel sickness; a probiotic → Supplements & nutrition.', 'kinds from the top of the gut to the bottom: acid, wind, bowel, fluid loss, nausea',
     'Indigestion & heartburn remedy', 'Wind & bloating remedy', 'Laxative', 'Anti-diarrhoeal', 'Haemorrhoid treatment', 'Oral rehydration salts', 'Travel-sickness remedy'),
   S('Skin, eyes, ears & mouth', 'Creams, drops and treatments put on the skin or into the eyes, ears and mouth; contact-lens drops → Vision & communication.', 'kinds by body part: skin, feet, hair, eyes, ears, gums',
     'Antiseptic', 'Anti-itch & hydrocortisone cream', 'Antifungal treatment', 'Cold-sore treatment', 'Corn, wart & verruca treatment', 'Head-lice treatment', 'Eye drops', 'Ear drops', 'Teething gel'),
   S('Quit smoking', 'Products that supply nicotine without tobacco smoke to help a person stop; an ordinary vape → J10.', None, 'Nicotine replacement'),
   S('Traditional remedies', 'Preparations sold under a healing system rather than for one complaint; a herb sold as a supplement → Supplements & nutrition.', 'kinds by healing system: homeopathy, then other traditional systems',
     'Homeopathic single remedy', 'Traditional medicine preparation'),
  ]},
 {'n': 'Monitors, tests & dosing', 'mode': 'tier', 'note': 'Validated accuracy is the first test for every monitor.',
  't': 'Devices that read a body measure, test a sample at home or measure out a dose; pregnancy and ovulation tests → Sexual health & family; a fitness watch → D2.',
  'ax': 'What does the device do: read a body measure again and again, track glucose, test a sample once, or measure out a dose?',
  's': [
   S('Vital signs', 'Home monitors for blood pressure, temperature, blood oxygen, heart rhythm and breathing; a stethoscope-only kit is a manual kit here.', 'kinds by what is measured: blood pressure, temperature, oxygen, heart rhythm, breath flow',
     'Blood-pressure monitor', 'Manual blood-pressure kit', 'Digital thermometer', 'Pulse oximeter', 'Personal ECG monitor', 'Peak flow meter'),
   S('Glucose monitoring', 'Meters and sensors that follow blood sugar; an insulin pen or pump → Dosing devices.', 'kinds from continuous sensor to single reading to long-term average',
     'Continuous glucose monitor', 'Blood glucose meter', 'HbA1c test kit'),
   S('Home tests', 'One-use kits that test a sample at home for infection, markers or alcohol; a pregnancy test → Sexual health & family.', 'kinds by what is tested: infection, urine, blood, stool, breath',
     'Infection test kit', 'Urine test strips', 'HIV self-test', 'Cholesterol test', 'Bowel screening test', 'Breathalyser'),
   S('Dosing devices', 'Devices that deliver or measure out a dose of medicine; the medicine itself → Medicines & remedies.', 'kinds from injected doses to oral doses to organising tablets',
     'Insulin pen', 'Insulin pump', 'Adrenaline auto-injector', 'Oral syringe & dosing spoon', 'Pill organiser & dispenser', 'Pill cutter'),
  ]},
 {'n': 'First aid & supports', 'mode': 'tier', 'note': 'Medical face masks arrive here from clothing.',
  't': 'Items that treat an injury, hold a joint or replace a missing body part; a medicine for the wound → Medicines & remedies; sports kit that is not medical → E2.',
  'ax': 'What does the item do for the body: cover a wound, deal with an emergency, support a joint or limb, or replace a missing part?',
  's': [
   S('Wound care', 'Kits, plasters, dressings and bandages for cuts, grazes and burns; a medicated antiseptic → Medicines & remedies.', 'kinds from the whole kit to single dressings, then what holds them',
     'First-aid kit', 'Plaster', 'Wound dressing', 'Burn dressing', 'Bandage', 'Medical tape', 'Wound-closure strip', 'Liquid bandage'),
   S('Emergency & protective supplies', 'Kept for an emergency or to protect the helper; a worker\'s respirator → C1.', 'kinds by emergency: heart stop, exposure, eye splash, infection risk',
     'Home defibrillator', 'Emergency foil blanket', 'Sterile eyewash', 'Disposable medical gloves', 'Medical face mask'),
   S('Braces, supports & insoles', 'Worn supports that steady a joint or limb, shape the foot or squeeze the leg; a sports-brand brace is the same kind.', 'kinds by what the support does: hold a joint, hold a limb, shape the foot, squeeze the leg',
     'Joint support / brace', 'Splint & sling', 'Orthotic insole', 'Compression stocking'),
   S('Prostheses', 'Artificial limbs and body parts fitted by a specialist; an implant is surgery, not a possession.', 'kinds by body part replaced: leg, arm, breast, eye, face',
     'Leg prosthesis', 'Arm prosthesis', 'Breast prosthesis', 'Eye prosthesis', 'Facial prosthesis'),
  ]},
 {'n': 'Supplements & nutrition', 'mode': 'tier',
  't': 'Capsules, powders, drinks and formulas taken to add nutrients or fuel training or diet; a medicine → Medicines & remedies; a food or ready drink → J.',
  'ax': 'What does it supply: vitamins and minerals, oils, herbs and specialty ingredients, training protein, endurance fuel, or whole-diet nutrition?',
  's': [
   S('Vitamins & minerals', 'Supplements built on vitamins, minerals or both together.', None, 'Multivitamin', 'Vitamin supplement', 'Mineral supplement'),
   S('Oils, herbs & specialty supplements', 'Supplements built on an oil, microbe, plant or protein rather than a vitamin or mineral.', 'kinds from oils and microbes to herbs, collagen and blends',
     'Omega-3 oil', 'Probiotic', 'Herbal supplement', 'Collagen', 'Combination supplement', 'Tonic & essence'),
   S('Protein & training supplements', 'Powders and capsules taken around training for muscle, energy or weight; a protein bar → J8.', 'kinds from bulk protein to focused ingredients, then stimulants and fat loss',
     'Protein powder', 'Mass gainer', 'Creatine', 'Amino acids', 'Pre-workout', 'Fat burner'),
   S('Endurance fuel & hydration', 'Carbohydrate and salt products taken during long exercise; a ready-made sports drink → J9.', None, 'Energy gel & chew', 'Electrolyte drink mix'),
   S('Meal replacement & medical nutrition', 'Products that stand in for a meal or feed a medical condition, from diet shakes to clinical formulas.', 'kinds from diet shake to nutrition drink to condition-specific formula',
     'Meal-replacement shake', 'Oral nutritional supplement', 'Medical-condition formula'),
  ]},
 {'n': 'Breathing, sleep & therapy', 'mode': 'tier',
  't': 'Machines, packs, lamps and bedding that ease breathing, sleep, mood or pain; a medicine for the same complaint → Medicines & remedies; a massager → H1.',
  'ax': 'What does the device ease: breathing, sleep and mood, or pain and comfort?',
  's': [
   S('Breathing aids', 'Machines and holders that help air or inhaled medicine reach the lungs, by day or in sleep.', 'kinds from machines that supply air to those that deliver medicine or steam',
     'CPAP machine', 'Oxygen concentrator', 'Nebuliser', 'Inhaler spacer', 'Steam inhaler'),
   S('Sleep & mood', 'Devices and bedding that improve sleep or lift winter mood; a sleeping tablet → Medicines & remedies.', None,
     'Anti-snoring device', 'Weighted blanket', 'Light-therapy lamp'),
   S('Pain & comfort', 'Devices that ease sore muscles, joints and the neck through current, heat, cold or support.', None,
     'TENS/EMS unit', 'Heat & cold pack', 'Orthopaedic pillow'),
  ]},
 {'n': 'Mobility aids', 'mode': 'mixed', 'note': 'Archetypes only for active wheelchairs and collector canes; the rest is tier.',
  't': 'Aids for walking, rolling, crossing a step or being lifted; a bathroom or bed aid → Daily living & care; a hiking pole → E2.',
  'ax': 'How does the person move: on foot with support, seated on wheels, or lifted and carried over a step or into a vehicle?',
  's': [
   S('Walking aids', 'Sticks, crutches and frames that take weight on foot; a cane owned as a collectable → Collector canes.', 'kinds by how much weight they take, from a stick to a wheeled frame',
     'Walking stick', 'Crutches', 'Walking frame', 'Rollator', 'Gait trainer', 'Knee walker'),
   S('Collector canes', 'Canes owned as accessories or curiosities rather than as aids; a stick used for support → Walking aids.', 'named forms of collectable cane',
     'Collector cane'),
   S('Wheelchairs & scooters', 'Chairs and scooters on wheels, pushed, self-driven or powered, with the add-ons and parts owners swap.', 'kinds by what moves it: user or helper, motor, add-on drive, then parts',
     'Manual wheelchair', 'Powered wheelchair', 'Mobility scooter', 'Wheelchair power add-on', 'Wheelchair parts & accessories'),
   S('Ramps, lifts & transfers', 'Aids that change a person\'s height or position: over a step, between seats, or into a vehicle.', 'kinds by the move they make: roll over a step, lift, slide or pivot, load into a vehicle',
     'Portable ramp', 'Patient lift', 'Transfer aid', 'Mobility vehicle lift'),
  ]},
 {'n': 'Daily living & care', 'mode': 'tier',
  't': 'Aids that help a person wash, use the toilet, stay continent, rest in bed, call for help or manage meals and dressing; built-in grab bars and stairlifts → G3.',
  'ax': 'Which part of daily life does the aid help with: washing and toileting, continence, rest in bed, calling for help, or reaching, dressing and eating?',
  's': [
   S('Bathroom & toilet aids', 'Seats, frames and tools for washing and using the toilet safely.', 'kinds from bathing to toileting: bath, shower, toilet, commode',
     'Shower chair', 'Tub transfer bench', 'Bath lift', 'Bathing & washing aid', 'Raised toilet seat', 'Toilet safety frame', 'Commode chair', 'Bedpan & urinal'),
   S('Continence & stoma', 'Products that contain or collect urine and stool.', 'kinds from absorbent products to collecting devices to catheters',
     'Incontinence pads & pants', 'Bed & chair protector', 'Stoma appliance', 'Intermittent catheter', 'External catheter', 'Urine drainage bag'),
   S('Beds & pressure care', 'Beds, mattresses, cushions and rails for someone who spends long hours lying or sitting.', 'kinds from the bed to what lies on it, sits on it or guards its edge',
     'Care bed', 'Pressure-relief mattress', 'Pressure-relief cushion', 'Bed rail', 'Lift chair'),
   S('Alarms & medical ID', 'Worn or fitted items that call help or tell others about a condition.', None, 'Personal alarm', 'Medical ID', 'Wandering detector'),
   S('Everyday aids', 'Hand tools and adapted tableware for reaching, dressing, eating and gripping.', 'kinds by task: reach, dress, eat, grip',
     'Reacher', 'Dressing aid', 'Adapted cutlery & cups', 'Jar opener & grip aid'),
  ]},
 {'n': 'Hearing', 'mode': 'tier',
  't': 'Devices for people with hearing loss: aids worn in or on the ear, their care and parts, and tools that bring sound and alerts to the listener; earplugs and headphones → C1, D3.',
  'ax': 'Where does the device work: worn at the ear, caring for the ear device, or carrying sound and alerts to the listener?',
  's': [
   S('Ear-worn hearing devices', 'Devices worn in or on the ear to amplify sound or drive an implant.', 'kinds from prescribed aids to over-the-counter aids to amplifiers and implant processors',
     'Hearing aid', 'Over-the-counter hearing aid', 'Personal sound amplifier', 'Implant sound processor'),
   S('Hearing-aid parts', 'Batteries and small parts that keep a hearing aid running.', None, 'Hearing-aid spare parts'),
   S('Listening & alerting aids', 'Tools that carry speech, TV sound and alarms to a person with hearing loss.', 'kinds by what they carry: remote voice, TV or room sound, phone calls, alarms',
     'Hearing-aid streamer & remote mic', 'Assistive listening system', 'Amplified telephone', 'Alerting system'),
  ]},
 {'n': 'Vision & communication', 'mode': 'tier', 'note': 'Frames, ready readers and all glasses move to A4 Eyewear; lenses, contacts and low-vision aids stay here.',
  't': 'Lenses and aids for people who see poorly or cannot see, and aids for people who cannot rely on speech; frames and sunglasses → A4; a hobby loupe → E6.',
  'ax': 'What does the person need help with: seeing through corrected lenses, using limited sight, getting around and reading without sight, or speaking?',
  's': [
   S('Spectacle & contact lenses', 'Prescription lenses worn in glasses or on the eye, and their care.', 'kinds from lenses in glasses to lenses on the eye to their care',
     'Spectacle lens', 'Soft contact lens', 'Rigid contact lens', 'Contact-lens solution & drops'),
   S('Low-vision aids', 'Magnifiers and optical aids that make the most of remaining sight.', 'kinds from simple magnifiers to electronic and worn aids',
     'Handheld magnifier', 'Stand magnifier', 'Electronic magnifier', 'Low-vision glasses', 'Low-vision monocular'),
   S('Aids for blind people', 'Canes and braille tools used without sight.', None, 'White cane', 'Braille device'),
   S('Communication aids', 'Devices and boards that let a person speak or be understood without ordinary speech.', None, 'Communication aid', 'Eye-gaze device', 'Electrolarynx'),
  ]},
 {'n': 'Sexual health & family', 'mode': 'tier',
  't': 'Products for preventing or planning pregnancy, feeding a baby and intimate function; sex toys → H3; period products → H1.',
  'ax': 'What stage or need is it for: contraception and barriers, conceiving and confirming pregnancy, breastfeeding, or intimate function?',
  's': [
   S('Contraception & barriers', 'Products that prevent pregnancy or infection during sex.', 'kinds from the worn barrier to fitted barriers to chemical and emergency methods',
     'Condom', 'Dental dam', 'Diaphragm & cervical cap', 'Spermicide', 'Emergency contraceptive pill'),
   S('Fertility & pregnancy', 'Tests and trackers for trying to conceive and for confirming pregnancy.', 'kinds from tracking the cycle to testing to confirming pregnancy',
     'Basal-body thermometer', 'Fertility monitor', 'Ovulation test', 'Sperm test kit', 'Pregnancy test'),
   S('Breastfeeding', 'Pumps and care items for breastfeeding and expressing milk.', 'kinds from expressing and storing milk to feeding and skin care',
     'Breast pump', 'Milk collector', 'Breast-milk storage bag', 'Nipple shield', 'Nursing pad', 'Nipple cream'),
   S('Intimate health devices', 'Medical devices for pelvic and sexual function; a pleasure toy → H3.', 'kinds by body part: pelvic floor, vagina, penis',
     'Pelvic-floor trainer', 'Vaginal dilator', 'Vacuum erection device', 'Erection ring', 'Penile traction device', 'Delay spray'),
  ]},
]

# ---------- apply kind edits ----------
used = set()
for dp in DEPTS:
    for sh in dp['s']:
        newk = []
        for k in sh['k']:
            k = copy.deepcopy(k)
            n = k['n']; used.add(n)
            if n in TT:
                k.pop('t', None); k['tt'] = TT[n]
            if n in SEE: k['see'] = SEE[n]
            newk.append(k)
        sh['k'] = newk
missing = [n for n in old if n not in used]
if missing: raise SystemExit('kinds dropped: %s' % missing)
nott = [k['n'] for dp in DEPTS for sh in dp['s'] for k in sh['k'] if 'tt' not in k]
print('kinds without tt:', nott)

# ---------- archetype demotions ----------
def find(n):
    for dp in DEPTS:
        for sh in dp['s']:
            for k in sh['k']:
                if k['n'] == n: return k
cc = find('Collector cane')
demote = {'Malacca cane', 'Gadget cane', 'Tippling cane', 'Shooting stick'}
cc['x'] = [x for x in cc['x'] if x['n'] not in demote]
for x in cc['x']:
    x['y'] = x.get('y', '')
cc['x'] += [
 {'n': 'Shillelagh', 'a': 'blackthorn stick', 'd': 'Irish stick of blackthorn or oak, used as a walking stick and cudgel; the name means thonged willow.', 'mk': '', 'y': '', 's': W('Shillelagh_(club)'), 'dt': 'blackthorn or oak · knobbed head · wrist thong'},
 {'n': 'Whangee cane', 'a': 'whanghee', 'd': 'Asian bamboo cane with a curved handle, carried by the Tramp character and sold as a riding crop.', 'mk': '', 'y': '', 's': W('Walking_stick'), 'dt': 'bamboo shaft · natural root handle'},
 {'n': 'Ziegenhainer', 'a': '', 'd': 'Knotty German stick of European cornel, also used by duellists\' seconds as a melee weapon.', 'mk': '', 'y': '', 's': W('Walking_stick'), 'dt': 'cornel wood · knotted shaft'},
]
wc = find('White cane')
hoover = [x for x in wc['x'] if x['n'].startswith('Long cane')]
wc['x'] = [x for x in wc['x'] if not x['n'].startswith('Long cane')]
for x in hoover:
    for v in x.get('v', []):
        wc.setdefault('m', []).append([v['n'], v['mk']])
if not wc['x']: wc.pop('x')

# ---------- category ----------
out = {'c': 'H2', 'rev': True,
 'lead': src['lead'],
 'ax': 'What is the product for: treating a complaint, measuring or dosing, treating an injury or supporting the body, supplying nutrients, easing breathing, sleep or pain, moving about, daily care, hearing, seeing and speaking, or family planning?',
 'key': [
  '1. Is it a non-prescription medicine, or a traditional or homeopathic remedy, taken or applied for a complaint? → Medicines & remedies',
  '2. Does it read a body measure at home, test a sample, or measure out a dose (monitor, test kit, insulin pen, pill organiser)? → Monitors, tests & dosing',
  '3. Does it dress a wound, deal with an emergency, support a joint or replace a body part? → First aid & supports',
  '4. Is it a vitamin, herb, protein, sports fuel or medical formula? → Supplements & nutrition',
  '5. Is it a machine, pack, lamp or bedding that eases breathing, sleep, mood or pain? → Breathing, sleep & therapy',
  '6. Does it help someone walk, roll, cross a step or be lifted? → Mobility aids',
  '7. Does it help with washing, the toilet, continence, bed, calling for help, reaching, dressing or eating? → Daily living & care',
  '8. Is it a hearing aid, or a tool that brings sound and alerts to a person with hearing loss? → Hearing',
  '9. Is it a lens, magnifier, cane or braille tool for poor sight, or an aid for speaking? → Vision & communication',
  '10. Is it for contraception, conceiving, pregnancy, breastfeeding or intimate function? → Sexual health & family',
  '<i>Precedence: a tablet for sleep is a medicine (step 1) before a sleep device (step 5); a probiotic capsule is a supplement (step 4) but a probiotic yoghurt is food (J3); glasses frames and sunglasses → A4; sex toys → H3.</i>'],
 'b': src.get('b', []), 'depts': DEPTS}
tmp = BASE + 'out/H2.json.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, BASE + 'out/H2.json')
cnt = lambda d: (len(d), sum(len(x['s']) for x in d), sum(len(s['k']) for x in d for s in x['s']))
print('before', cnt(src['depts']), 'after', cnt(DEPTS))
print('new kinds', len(NEW), 'archetypes', sum(len(k.get('x', [])) for x in DEPTS for s in x['s'] for k in s['k']))
