import json, copy, os, re
R='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open(R+'work/STR_A4/bak/A4.json'))
K={}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=copy.deepcopy(k)
HB='https://en.wikipedia.org/wiki/Handbag'; WL='https://en.wikipedia.org/wiki/Wallet'
GL='https://en.wikipedia.org/wiki/Glasses'; BP='https://en.wikipedia.org/wiki/Backpack'
BS='https://en.wikipedia.org/wiki/Baby_sling'; HF='https://en.wikipedia.org/wiki/Hand_fan'
LG='https://en.wikipedia.org/wiki/Luggage'
def new(n,a,d,s,x=None):
    k={'n':n,'a':a,'d':d,'s':s}
    if x: k['x']=x
    K[n]=k
# ---- new kinds
new('Barrel bag','duffle-shaped purse · cylinder bag','Cylindrical bag larger than a baguette, with two short handles, no flap and usually no shoulder strap.',HB)
new('Wristlet bag','wristlet · wrist pouch','Small rectangular bag with a short wrist strap, close to a clutch in size.',HB)
new('Gladstone & doctor\'s bag','Gladstone bag · doctor\'s bag','Victorian-style leather bag with two sturdy handles and no flap or strap, traditionally black; used for travel and by doctors.',HB)
K["Gladstone & doctor's bag"]['x']=[x for x in K['Top-handle bag']['x'] if x['n']=='Gladstone bag']
K['Top-handle bag']['x']=[x for x in K['Top-handle bag']['x'] if x['n']!='Gladstone bag']
new('Fashion backpack','mini backpack · designer backpack','Small purse-sized backpack carried as a fashion accessory rather than for loads.',BP,
 [{'n':'Prada nylon backpack','a':'','d':'Black military-spec nylon backpack from Miuccia Prada\'s first backpacks and totes.','mk':'Prada','y':'1979','s':'https://en.wikipedia.org/wiki/Prada','v':[]}])
new('Rolling backpack','wheeled backpack','Backpack with wheels and an extendable handle, used mostly for air or rail travel.',BP)
new('Travel wallet','document wallet · travel organiser','Wallet that holds passport, tickets, boarding passes, currency and itinerary together.',WL)
new('Oversized & bug-eye frames','bug-eye glasses · oversized sunglasses','Frame with very large, rounded lenses, in fashion in the 1970s.',GL)
new('Rivet spectacles','','Earliest wearable glasses: two magnifying lenses riveted together at the handles and balanced on the nose.',GL)
new('Scissors glasses','','Glasses with a handle on each side, held up to the face rather than worn.',GL)
new('Lens cloth & cleaning kit','microfibre cloth','Soft cloth or kit that cleans lenses without scratching them.',GL)
new('Pouch sling','tube sling','Wide piece of fabric sewn into a tube and worn sash-style, with no rings or hardware.',BS)
new('Onbuhimo','','Japanese carrier with long top straps and a small rectangular body, usually worn on the back.',BS)
# merges
tote=K['Tote bag']; ct=K.pop('Canvas tote'); tote['x']+=ct['x']; tote['a']+=' · canvas tote · boat tote · cotton tote'
duf=K['Duffel bag']; wd=K.pop('Wheeled duffel'); duf['x']+=wd['x']; duf['m']=(duf.get('m') or [])+wd['m']; duf['a']+=' · wheeled duffel · rolling duffel'
pg=K['Prescription glasses']; K.pop('Prescription sunglasses'); K.pop('Spectacle frame')
pg['d']="Glasses with lenses made to the wearer's prescription, including prescription sunglasses; bought complete or as a frame for glazing."
K['Long wallet']['a']+=' · breast wallet'
K['Folding fan']['a']+=''
# demote generic archetypes
def drop(k,names):
    K[k]['x']=[x for x in K[k]['x'] if x['n'] not in names]
drop('Stick umbrella',['Solid-stick umbrella']); drop('Satchel',['School satchel'])
drop('Travel trunk',['Steamer trunk','Wardrobe trunk','Dome-top trunk']); drop('Vanity case',['Train case'])
drop('Saddle & half-moon bag',['Half-moon bag']); drop('Rigid fan',['Palm-leaf fan','Feather fan'])
K['Vanity case']['a']+=' · train case'
# new archetypes
def ax(k,n,d,mk,y,s,a='',v=None):
    K[k].setdefault('x',[]).append({'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':v or []})
ax('Suitcase','Rollaboard','Two-wheeled case pulled upright by a long handle, first made for carry-on use.','',"",LG)
ax('Folding fan','Tessen','Iron fan, a folding fan used as a weapon in Japan.','','',HF)
ax('Folding fan','Mai ogi','Japanese dancing fan with ten sticks and a thick paper mount showing a family crest.','','',HF)
ax('Folding fan','Kawahori-ogi','Japanese paper folding fan with fewer blades; two were given to the Chinese emperor by the monk Chōnen.','','988',HF)
# ---- type groups (tt), written by hand
LF='Lens fitted'; FM='Frame material'
TT={
'Top-handle bag':[['Handles',['Single handle','Double handle']],['Strap',['Handles only','Detachable shoulder strap']],['Size',['Mini','Medium','Large']]],
'Bowling & Boston bag':[['Shape',['Domed zip-top (bowling)','Barrel-shaped (Boston)']],['Material',['Leather','Coated canvas','Nylon']],['Size',['Mini','Medium','Large']]],
'Barrel bag':[['Shape',['Cylinder','Rounded barrel']],['Strap',['Handles only','Detachable shoulder strap']],['Size',['Mini','Medium','Large']]],
'Tote bag':[['Structure',['Unstructured','Structured']],['Top',['Open top','Zip top']],['Orientation',['North–south','East–west']],['Material',['Leather','Cotton canvas','Jute','Nylon','Coated canvas']],['Fitted extras',['Reversible','Removable pouch','Contrast trim']]],
'Satchel':[['Structure',['Structured','Soft']],['Closure',['Buckle','Lock']],['Strap',['Handle only','Crossbody strap']]],
'Basket & woven bag':[['Construction',['Woven basket','Looped string','Crocheted']],['Fibre',['Straw','Raffia','Rattan','Cotton cord']]],
'Flap bag':[['Strap',['Chain','Leather','Chain woven with leather']],['Closure',['Turn-lock','Magnetic closure','Snap']]],
'Shoulder bag':[['Strap',['Chain','Leather','Webbing']],['Closure',['Zip top','Open top','Magnetic closure']],['Size',['Mini','Medium','Large']]],
'Baguette bag':[['Strap',['Short strap','Chain strap']],['Material',['Leather','Fabric','Beaded','Embossed']]],
'Hobo bag':[['Closure',['Top zip','Magnetic snap','Open top']],['Strap',['Single shoulder strap','Crossbody strap']],['Size',['Small','Medium','Large']]],
'Saddle & half-moon bag':[['Shape',['Saddle','Half-moon','Crescent']],['Closure',['Flap','Zip']],['Strap',['Short shoulder strap','Crossbody strap']]],
'Bucket bag':[['Closure',['Drawstring','Open top']],['Strap',['Shoulder strap','Crossbody strap']],['Size',['Mini','Medium','Large']]],
'Crossbody bag':[['Strap',['Adjustable strap','Chain strap','Detachable strap']],['Closure',['Zip','Flap','Magnetic closure']],['Size',['Phone-size mini','Standard']]],
'Messenger bag':[['Material',['Canvas','Nylon','Leather']],['Closure',['Full flap with buckles','Flap with hook-and-loop']],['Strap',['Padded wide strap','Cross-body stabiliser strap']]],
'Clutch bag':[['Shape',['Envelope','Box','Frame (kiss-lock)','Oversized']],['Strap',['None','Detachable wrist or chain strap']],['Material',['Leather','Satin','Beaded','Metal']]],
'Pochette':[['Strap',['Chain','Fabric or leather strap']],['Pouches',['Single pouch','Multi-pouch set']]],
'Wristlet bag':[['Strap',['Wrist strap','Detachable chain']],['Closure',['Zip','Flap']],['Size',['Phone-size','Standard']]],
'Minaudière':[['Material',['Metal','Crystal-covered','Enamel','Resin']],['Shape',['Rectangular case','Figural (novelty shape)']]],
'Bifold wallet':[['Size',['Slim','Standard','Tall']],['Extras',['Coin pocket','ID window']],['Material',['Leather','Exotic skin','Fabric']]],
'Trifold wallet':[['Extras',['ID window','Coin pocket']],['Material',['Leather','Fabric']]],
'Long wallet':[['Closure',['Snap or flap','Zip','Open']],['Build',['Flat','Gusseted']],['Material',['Leather','Exotic skin','Fabric']]],
'Zip-around wallet':[['Size',['Compact','Continental']],['Sections',['Single section','Multi-section']],['Material',['Leather','Coated canvas']]],
'Wristlet wallet':[['Strap',['Fixed wrist strap','Detachable wrist strap']],['Size',['Compact','Phone-size']]],
'Biker chain wallet':[['Length',['Long','Short']],['Fastening',['Belt-loop chain','Clip']]],
'Wallet on chain (bag)':[['Strap',['Chain','Leather strap','Detachable strap']],['Closure',['Flap','Zip']],['Material',['Leather','Coated canvas']]],
'Cardholder':[['Closure',['Open slip','Snap','Pull-tab sleeve','Zip']],['Material',['Leather','Aluminium','Metal','Fabric']]],
'Money clip':[['Material',['Solid metal','Carbon fibre','Leather with magnet']],['Card slots',['Clip only','With card slots']]],
'Coin purse':[['Closure',['Zip','Snap','Frame (kiss-lock)']],['Material',['Leather','Fabric']]],
'Key pouch':[['Closure',['Zip','Fold-over']],['Holder',['Inner ring','Hooks']]],
'Keyring':[['Fastening',['Split ring','Carabiner clip','Fob']],['Material',['Metal','Leather','Fabric']]],
'Passport cover':[['Build',['Slip cover','Wallet with card slots']],['Material',['Leather','Fabric']]],
'Travel wallet':[['Size',['Passport-size','Family document size']],['Extras',['RFID blocking','Pen loop']]],
'Aviator frames':[['Bridge',['Double bridge','Triple bridge']],[FM,['Metal','Titanium','Acetate']],[LF,['Sun','Polarised','Prescription','Photochromic']]],
'Round & panto frames':[['Rim shape',['Fully round','Panto (flatter top)']],[FM,['Metal','Acetate','Titanium']],[LF,['Sun','Prescription','Clear plano']]],
'Square & rectangular frames':[['Rim shape',['Square','Rectangular']],[FM,['Acetate','Metal']],[LF,['Sun','Prescription','Clear plano']]],
'Wayfarer-style frames':[[FM,['Acetate','Plastic']],['Size',['Standard','Large','Small']],[LF,['Sun','Polarised','Prescription','Clear plano']]],
'Cat-eye frames':[[FM,['Acetate','Metal']],['Rim shape',['Softly upswept','Sharply winged']],[LF,['Sun','Prescription','Clear plano']]],
'Browline frames':[['Lower rim',['Metal wire','Nylon thread','Rimless']],[FM,['Acetate and metal','Titanium']],[LF,['Sun','Prescription','Clear plano']]],
'Geometric frames':[['Rim shape',['Hexagonal','Octagonal','Angular']],[FM,['Metal','Acetate']],[LF,['Sun','Prescription']]],
'Oversized & bug-eye frames':[['Rim shape',['Round oversized','Square oversized','Butterfly']],[FM,['Acetate','Metal']],[LF,['Sun','Prescription']]],
'Rimless & semi-rimless frames':[['Rim build',['Rimless (drilled)','Half-rim with nylon thread']],[FM,['Metal','Titanium']],[LF,['Sun','Prescription','Clear plano']]],
'Shield & wrap sunglasses':[['Lens shape',['Single shield lens','Two wrap lenses']],['Fit',['Close to the face','Over spectacles']],[LF,['Polarised','Photochromic','Prescription']]],
'Folding sunglasses':[[FM,['Metal','Acetate']],[LF,['Sun','Polarised']]],
'Clip-on sunglasses':[['Attachment',['Clip','Flip-up hinge','Magnet']],[LF,['Tinted','Polarised']]],
'Prescription glasses':[['Lens power',['Single vision','Bifocal','Trifocal','Varifocal (progressive)']],['Lens treatment',['Clear','Photochromic','Tinted (prescription sunglasses)','Blue-light filter']],['Supply',['Complete pair','Frame only for glazing']]],
'Reading glasses':[['Frame build',['Full frame','Half-eye','Folding']],['Lens treatment',['Clear','Blue-light filter','Tinted (sun readers)']]],
'Rivet spectacles':[['Lens power',['Convex (reading)','Concave (distance)']],[FM,['Wood','Bone','Horn','Leather']]],
'Lorgnette':[['Form',['Standard','Fan lorgnette','Double lorgnette']],[FM,['Tortoiseshell','Metal','Gold']]],
'Scissors glasses':[[FM,['Tortoiseshell','Metal','Gold']],['Handle',['Single side handle','Handles on both sides']]],
'Monocle':[['Rim',['Slotted loop (1830s)','Gallery frame (1890s)','Frameless cut glass']],['Hold',['Worn in the eye socket','On a cord']]],
'Pince-nez':[['Bridge',['C-bridge','Bar-spring (astig)','Spring with spectacle-style lens mount']],['Rim',['Rimless','Full rim','Half rim']]],
'Glasses case':[['Shell',['Hard shell','Semi-hard shell','Soft pouch']],['Form',['Single pair','Folding','Multi-pair']]],
'Glasses chain & cord':[['Build',['Neoprene retainer','Cord','Chain','Beaded chain']],['Use',['Everyday','Sports strap']]],
'Lens cloth & cleaning kit':[['Form',['Microfibre cloth','Cloth with spray']],['Size',['Pocket','Case-size']]],
'Daypack':[['Opening',['Top-loading','Panel-loading','Flap-top']],['Fabric',['Canvas','Nylon']]],
'Laptop backpack':[['Laptop size',['13–14 inch','15–16 inch','17 inch']],['Extras',['USB pass-through','Trolley sleeve']]],
'Carry-on travel backpack':[['Opening',['Clamshell','Top-loading']],['Harness',['Stowable harness','Hip belt']],['Capacity',['Under 30 L','30–45 L']]],
'Hiking backpack':[['Frame',['Internal frame','External frame','Frameless']],['Closure',['Lid-top','Roll-top']],['Capacity',['Under 30 L','30–50 L','Over 50 L']]],
'School backpack':[['Safety features',['Reflective panels','Chest and hip straps']],['Supply',['Bag only','School set with pencil case']]],
'Fashion backpack':[['Material',['Nylon','Leather','Coated canvas']],['Size',['Mini','Small']]],
'Rolling backpack':[['Wheels',['Two wheels','Four wheels']],['Straps',['Stowable backpack straps','Fixed backpack straps']]],
'Drawstring bag':[['Material',['Cotton','Polyester','Mesh']],['Size',['Small','Large']]],
'Belt bag':[['Worn',['At the waist','Crossbody']],['Fabric',['Nylon or polyester','Coated canvas','Leather']],['Size',['Mini','Standard']]],
'Sling bag':[['Worn',['On the back','On the chest','On the hip']],['Size',['Mini (under 2 L)','Standard']],['Use',['Everyday','Camera']]],
'Suitcase':[['Size',['Cabin (carry-on)','Medium check-in','Large check-in']],['Wheels',['Four-wheel spinner','Two-wheel upright']],['Shell',['Hardside aluminium','Hardside polycarbonate or composite','Softside nylon','Vulcanised fibreboard','Leather']],['Capacity',['Fixed','Expandable']],['Electronics',['None','Battery and tracking (smart)']]],
'Travel trunk':[['Lid',['Flat-top','Dome-top (camel-back)']],['Size',['Standard','Cabin']],['Fitted for',['Flat-packed clothes','Hanging clothes','Hats','Barracks kit (footlocker)']],['Covering',['Canvas','Leather','Wicker']]],
'Vanity case':[['Shell',['Hard shell','Soft shell']],['Fittings',['Removable tray','Lid mirror']],['Security',['Lockable','Plain clasp']]],
"Gladstone & doctor's bag":[['Material',['Leather','Canvas']],['Size',['Small','Large']]],
'Weekender':[['Material',['Leather','Canvas','Coated canvas','Nylon']],['Strap',['Handles only','Shoulder strap']]],
'Duffel bag':[['Material',['Canvas','Nylon','Coated (TPU or PVC)']],['Wheels',['None','Two wheels with handle']],['Straps',['Carry handles','Backpack straps']],['Capacity',['Under 40 L','40–100 L']]],
'Gym bag':[['Compartments',['Shoe compartment','Wet pocket','Ventilated pocket']],['Straps',['Shoulder strap','Backpack straps']]],
'Garment bag':[['Fold',['Fold-over carry-on','Full-length']],['Wheels',['None','Wheeled']],['Material',['Fabric','Leather','Plastic dust cover']]],
'Dry bag':[['Weight',['Lightweight','Heavy-duty']],['Closure',['Roll-top','Roll-top with purge valve']],['Carry',['Hand','Backpack straps']]],
'Shopping trolley':[['Wheels',['Two wheels','Four wheels']],['Frame',['Fixed','Foldable']]],
'Toiletry bag':[['Material',['Leather','Fabric','Clear plastic']],['Form',['Zipped pouch','Hanging roll-up']]],
'Packing cube':[['Build',['Standard','Compression','Ultralight']],['Sorting',['Mixed-size set','Clean/dirty split']]],
'Luggage tag':[['Material',['Leather','Plastic']],['Option',['Personalised','With privacy flap']]],
'Luggage lock':[['Opening',['Combination','Keyed']],['Shackle',['Rigid','Cable']],['Standard',['TSA-accepted','Not TSA-accepted']]],
'Luggage strap':[['Fastening',['Plain buckle','With combination lock']],['Layout',['Single strap','Cross strap']]],
'Luggage scale':[['Reading',['Digital','Mechanical dial']]],
'Briefcase':[['Build',['Soft-sided','Structured']],['Capacity',['Standard','Expandable']],['Strap',['Handles only','Detachable shoulder strap']],['Material',['Leather','Nylon','Canvas']]],
'Attaché case':[['Material',['Aluminium','Leather']],['Lock',['Combination locks','Key locks']]],
'Pilot case':[['Carry',['Hand-carried','Wheeled']],['Material',['Leather','Hard shell']]],
'Document folio':[['Closure',['Zip-around','Flap']],['Fitted extras',['None','Writing pad']],['Paper size',['A4','A5','B5']]],
'Stick umbrella':[['Handle',['Crook','Straight']],['Canopy',['Standard dome','Bubble (deep dome)']],['Opening',['Manual','Auto-open']],['Closing',['Standard','Reverse-closing (inverted)']],['Wind rating',['Standard','Storm-rated']]],
'Folding umbrella':[['Opening',['Manual','Auto-open','Auto open-close']],['Folds',['Two-fold','Three-fold','Five-fold']],['Size',['Standard','Flat or mini']]],
'Golf umbrella':[['Canopy',['Single canopy','Vented double canopy']],['Frame',['Fibreglass','Steel']],['Opening',['Manual','Auto-open']]],
'Parasol':[['Canopy',['Lace','Paper','Silk','UV-blocking']],['Weather',['Sun only','Sun and rain (en-tout-cas)']]],
'Folding fan':[['Leaf',['Paper','Silk','Lace','Feather']],['Sticks',['Wooden slats','Bamboo','Bone or horn']],['Decoration',['Hand-painted','Printed or lithographed']]],
'Rigid fan':[['Leaf',['Paper','Silk','Woven palm leaf','Feathers']],['Frame',['Bamboo frame','Wooden handle','Papier-mâché']]],
'Fashion cane':[['Handle',['Crook','Knob','Derby','T-handle']],['Shaft',['Wood','Bamboo','Metal']]],
'Bag strap':[['Material',['Chain','Webbing','Leather']],['Width',['Standard','Wide guitar-style']]],
'Bag charm':[['Material',['Leather','Fur or plush','Metal','Resin']],['Form',['Figure','Pendant']]],
'Twilly':[['Fabric',['Printed silk twill']],['Worn',['Single','In pairs']]],
'Bag organiser':[['Material',['Felt','Nylon']],['Form',['Insert with pockets','Base shaper']]],
'Woven wrap':[['Fibre',['Cotton','Linen','Hemp','Silk','Wool blend']],['Length',['Short','Standard','Long']]],
'Stretchy wrap':[['Fabric',['Jersey','Interlock']],['Tying',['Long tie','Pre-sewn (pre-tied)']]],
'Ring sling':[['Fabric',['Linen','Silk','Cotton']],['Rings',['Aluminium','Nylon']],['Shoulder',['Pleated','Gathered']]],
'Pouch sling':[['Fabric',['Cotton','Stretch jersey']],['Sizing',['Fixed sizes','Adjustable']]],
'Mei tai':[['Waist strap',['Tied','Buckled (half-buckle)']]],
'Onbuhimo':[['Fastening',['Tied','Buckled']],['Fabric',['Cotton','Linen']]],
'Soft structured baby carrier':[['Age fit',['Newborn-only','Infant to toddler','Toddler size']],['Position',['Front-facing in','Forward-facing','Back carry']],['Fabric',['Standard','Mesh (all-season)']]],
'Hip seat':[['Build',['Seat only','With detachable carrier panel']]],
'Child carrier backpack':[['Frame',['Aluminium frame','Lightweight travel frame']],['Extras',['Sunshade','Daypack storage']]],
'Changing bag':[['Style',['Backpack','Tote','Shoulder','Crossbody','Convertible']],['Extras',['Insulated bottle holder','Stroller clip','Wipe-clean lining']]],
}
# see links: kind -> [[code,name,why]]
SEE={
'Wristlet wallet':[['A4','Wristlet bag','a bag, not a wallet']],
'Wristlet bag':[['A4','Wristlet wallet','card slots only']],
'Wallet on chain (bag)':[['A4','Crossbody bag','same carry, larger bag']],
'Messenger bag':[['A4','Briefcase','for work papers']],
'Briefcase':[['A4','Messenger bag','soft, crossbody']],
'Laptop backpack':[['D4','Camera backpack','padded for cameras'],['A4','Briefcase','carried by hand']],
'Hiking backpack':[['E2','Hydration pack','drink-carrying pack']],
'Drawstring bag':[['E2','Hydration pack','drink-carrying pack']],
'Toiletry bag':[['H1','Toiletry & make-up bag','bathroom storage']],
'Fashion cane':[['H2','Walking stick','mobility aid'],['H2','Collector cane','collected canes']],
'Folding fan':[['B7','Handheld fan','powered']],
'Rigid fan':[['B7','Handheld fan','powered']],
'Prescription glasses':[['D2','Smart glasses','electronic'],['H2','Low-vision glasses','for low vision']],
'Reading glasses':[['H2','Low-vision glasses','for low vision']],
'Lorgnette':[['E6','Opera glasses','magnifying']],
'Monocle':[['E6','Handheld magnifier','magnifier']],
'Rivet spectacles':[['E6','Handheld magnifier','magnifier']],
'Scissors glasses':[['E6','Opera glasses','magnifying']],
'Shield & wrap sunglasses':[['C1','Safety glasses','impact-rated']],
'Luggage tag':[['F5','Luggage label','collectable paper labels']],
'Travel trunk':[['B1','Trunk','furniture trunk']],
'Soft structured baby carrier':[['G1','Stroller','wheeled']],
'Child carrier backpack':[['G1','Stroller','wheeled']],
'Changing bag':[['G1','Stroller','wheeled']],
'Weekender':[['A4','Duffel bag','cylindrical, softer']],
'Duffel bag':[['A4','Weekender','leather or canvas, shaped']],
"Gladstone & doctor's bag":[['A4','Top-handle bag','structured handbag']],
'Sling bag':[['A4','Crossbody bag','larger, fashion']],
'Pochette':[['A4','Clutch bag','handle-less evening bag']],
'Rolling backpack':[['A4','Suitcase','upright wheeled case']],
'Dry bag':[['E2','Hydration pack','outdoor pack']],
}
# fix dry bag see (avoid weak link)
SEE.pop('Dry bag'); SEE.pop('Drawstring bag')
def fin(n):
    k=K[n]
    if n in TT: k['tt']=TT[n]; k.pop('t',None)
    elif 't' in k: raise SystemExit('no tt for '+n)
    if n in SEE: k['see']=SEE[n]
    return k
def shelf(n,t,ax_,names):
    s={'n':n,'t':t,'k':[fin(x) for x in names]}
    if ax_: s['ax']=ax_
    return s
D=[]
def dept(n,mode,t,ax_,shelves,note=None,b=None):
    d={'n':n,'mode':mode,'t':t,'ax':ax_}
    if note: d['note']=note
    d['b']=b if b is not None else []
    d['s']=shelves; D.append(d)
od={d['n']:d for d in old['depts']}
dept('Handbags','variety','Bags for daily and evening use, named by shape and by icon; a bag for work papers → Work bags, a bag worn on both shoulders → Backpacks & belt bags.',
 'How is the bag carried: by handles, on one shoulder, across the body, or in the hand with no handle?',[
 shelf('Top-handle & tote bags','Bags carried by handles in the hand or crook of the arm; a bag with only a shoulder strap → Shoulder bags.','kinds by body shape: structured box, domed zip-top, cylinder, open tote, soft flapped satchel, woven',['Top-handle bag','Bowling & Boston bag','Barrel bag','Tote bag','Satchel','Basket & woven bag']),
 shelf('Shoulder bags','Bags hung on one strap from the shoulder, from the flapped classic to the drawstring bucket; a strap worn across the body → Crossbody bags.','kinds by body shape and closure: flapped, plain, narrow, slouchy crescent, curved saddle, drawstring cylinder',['Flap bag','Shoulder bag','Baguette bag','Hobo bag','Saddle & half-moon bag','Bucket bag']),
 shelf('Crossbody bags','Bags on a strap worn from one shoulder to the opposite hip, such as the crossbody and messenger; a work bag with a strap → Work bags.',None,['Crossbody bag','Messenger bag']),
 shelf('Clutches & evening bags','Small bags held in the hand or on the wrist with no carrying handle, such as clutch, pochette and minaudière; a coin-and-card holder → Wallets & small leather goods.','kinds by size and rigidity: flat clutch, small strapped pochette, wrist-strapped bag, rigid jewelled case',['Clutch bag','Pochette','Wristlet bag','Minaudière'])],
 note=od['Handbags']['note'])
dept('Wallets & small leather goods','variety','Flat goods for money, cards, keys and travel papers that fit a pocket or bag; a bag with a strap → Handbags.',
 'What does it hold: notes and cards together, a single kind of small content, or keys and travel papers?',[
 shelf('Wallets','Holders for notes and cards together, such as bifold, long and zip-around wallets; a holder for cards only → Cards, notes & coins.','kinds by how the wallet folds, closes or is carried: folded once, twice, long and flat, zipped, on the wrist, on a chain',['Bifold wallet','Trifold wallet','Long wallet','Zip-around wallet','Wristlet wallet','Biker chain wallet','Wallet on chain (bag)']),
 shelf('Cards, notes & coins','Small holders for one kind of content, such as a cardholder, money clip or coin purse; one holding notes and cards → Wallets.',None,['Cardholder','Money clip','Coin purse']),
 shelf('Keys & travel papers','Cases for keys or for passport and tickets, such as key pouches, keyrings, passport covers and travel wallets.','kinds by what is held: loose keys, keys in a case, a passport, a full set of travel papers',['Keyring','Key pouch','Passport cover','Travel wallet'])])
dept('Eyewear','mixed','Frames and glasses worn on the face or held to it, with their cases and cords; magnifiers and binoculars → Observing & measuring, goggles for sport → Sports.',
 'What is the eyewear for: a styled frame, shading the sun, correcting sight, an earlier era, or looking after glasses?',[
 shelf('Frames by shape','Sunglasses and optical frames named by the outline of the lens and rim; sport wraps → Sunglasses for a purpose.','kinds by the outline of the lens, then by how the rim is built',['Aviator frames','Round & panto frames','Square & rectangular frames','Wayfarer-style frames','Cat-eye frames','Browline frames','Geometric frames','Oversized & bug-eye frames','Rimless & semi-rimless frames']),
 shelf('Sunglasses for a purpose','Sunglasses whose design adds something for use, such as a wrap for sport, a fold for travel or a clip for spectacles.',None,['Shield & wrap sunglasses','Folding sunglasses','Clip-on sunglasses']),
 shelf('Prescription & reading glasses','Glasses bought for sight rather than style, either made to a prescription or ready-made for close reading.',None,['Prescription glasses','Reading glasses']),
 shelf('Antique eyewear','Early and historic ways of holding lenses to the eyes; modern frames → Frames by shape.','kinds by how the lens is held: riveted at the nose, on a handle, in the eye socket, clipped on the nose',['Rivet spectacles','Lorgnette','Scissors glasses','Monocle','Pince-nez']),
 shelf('Glasses accessories','Things that store, hold or clean glasses.',None,['Glasses case','Glasses chain & cord','Lens cloth & cleaning kit'])],
 note=od['Eyewear']['note'])
dept('Backpacks & belt bags','mixed','Bags worn on the back, waist or chest on straps; a pack with a frame for mountaineering → Sports, a bag carried by handle → Handbags.',
 'How is the bag worn on the body: on both shoulders, round the waist, or on one strap?',[
 shelf('Backpacks','Bags worn on both shoulders, from slim commuting packs to trail rucksacks; a technical climbing or ski pack → Sports.','kinds by what the pack is built for: errands, work, travel, trail, school, fashion, a light sack',['Daypack','Laptop backpack','Carry-on travel backpack','Rolling backpack','Hiking backpack','School backpack','Fashion backpack','Drawstring bag']),
 shelf('Belt bags & slings','Small bags on a waist belt or a single strap round the body.',None,['Belt bag','Sling bag'])],
 note=od['Backpacks & belt bags']['note'])
dept('Luggage & travel','mixed','Cases and bags made to carry a trip\'s clothes, and the small items that pack, label and secure them; a work case → Work bags.',
 'Is it a rigid case, a soft bag, or a small item used with them?',[
 shelf('Cases & trunks','Rigid or semi-rigid cases with a lid, from wheeled suitcases to steamer trunks; a soft bag → Soft travel bags.',None,['Suitcase','Travel trunk','Vanity case']),
 shelf('Soft travel bags','Soft-sided bags for clothes and kit, carried by hand, strap or wheels; a hard case → Cases & trunks.','kinds by use: a trip away, a trip with wheels, kit for a gym, clothes on hangers, wet gear, shopping',['Weekender',"Gladstone & doctor's bag",'Duffel bag','Gym bag','Garment bag','Dry bag','Shopping trolley']),
 shelf('Packing & luggage accessories','Items that organise, mark, lock or weigh luggage.','kinds by job: wash and organise, label, lock, strap, weigh',['Toiletry bag','Packing cube','Luggage tag','Luggage lock','Luggage strap','Luggage scale'])],
 note=od['Luggage & travel']['note'])
dept('Work bags','variety','Bags and cases for papers and a laptop, carried by hand; a soft bag across the body → Crossbody bags, a laptop pack on both shoulders → Backpacks.',
 'How does it carry papers: in a soft bag, a hard case, a deep case or a slim folder?',[
 shelf('Briefcases & work bags','Flat cases for papers, from soft briefcases and hard attaché cases to slim folios.','kinds by build: soft, hard-sided, deep hard, slim folder',['Briefcase','Attaché case','Pilot case','Document folio'])])
dept('Umbrellas, fans & canes','mixed','Hand-held items against rain, sun or heat, and canes carried for dress; a walking aid → Mobility aids, a powered fan → Cooling & fans.',
 'What does it do for the carrier: keep off rain or sun, cool the face, or accompany a walk?',[
 shelf('Umbrellas & parasols','Canopies on a frame held overhead against rain or sun.','kinds by build and size: fixed shaft, collapsing shaft, oversize, sun-only',['Stick umbrella','Folding umbrella','Golf umbrella','Parasol']),
 shelf('Hand fans','Fans waved by hand to cool the face, either folding or rigid.',None,['Folding fan','Rigid fan']),
 shelf('Dress canes','Canes carried as a dress accessory.',None,['Fashion cane'])],
 note=od['Umbrellas & fans']['note'])
dept('Bag accessories','variety','Extras that attach to a bag or sit inside it, rather than carrying things themselves.',
 'Does it change how the bag is carried, decorate it, or arrange its contents?',[
 shelf('Bag accessories','Straps, charms, scarves and inserts that go on or in a bag.','kinds by job: carry, decorate, protect the handle, arrange',['Bag strap','Bag charm','Twilly','Bag organiser'])])
dept('Baby carriers & changing bags','tier','Carriers that hold a baby or child on the wearer\'s body, and the bag for a baby\'s things; a wheeled pram or buggy → Prams & strollers.',
 'What is carried: the child on the body, or the child\'s things?',[
 shelf('Baby carriers','Carriers that hold a child against the wearer, from wraps to framed backpacks.','kinds by how the child is held: wrapped in fabric, hung on rings, in a sewn tube, on a panel, on the hip, in a back frame',['Woven wrap','Stretchy wrap','Ring sling','Pouch sling','Mei tai','Onbuhimo','Soft structured baby carrier','Hip seat','Child carrier backpack']),
 shelf('Changing bags','Bags with pockets, mat and bottle holder for a baby\'s outing.',None,['Changing bag'])],
 note=od['Baby carriers & changing bags']['note'])
for dp in D:
    if dp['n']=='Baby carriers & changing bags':
        for s in dp['s']:
            for k in s['k']: k.setdefault('tg',['baby'])
out={'c':'A4','rev':True,
 'lead':'Bags, wallets, eyewear, umbrellas and other carried accessories, organised by what the object is and how it is carried, then by named icon and version for the collected kinds.',
 'ax':'What is the object for: carrying belongings (handbag, backpack, luggage, work bag), holding money and cards, seeing, keeping off rain or heat, or carrying a baby?',
 'key':[
 '1. Does it hold a baby on the body, or carry a baby\'s things? → Baby carriers & changing bags',
 '2. Is it worn on the face or held to it, or does it store or clean glasses? → Eyewear',
 '3. Is it held against rain, sun or heat, or a cane carried for dress? → Umbrellas, fans & canes',
 '4. Does it hold only money, cards, keys or travel papers, small enough for a pocket? → Wallets & small leather goods',
 '5. Does it attach to a bag or sit inside it instead of carrying things itself? → Bag accessories',
 '6. Is it made to carry a trip\'s clothes, or to pack, label or secure them? → Luggage & travel',
 '7. Is it worn on both shoulders, round the waist or on one strap on the back or chest? → Backpacks & belt bags',
 '8. Is it a case or bag for papers and a laptop, carried for work? → Work bags',
 '9. Is it a bag carried by handle, on a shoulder, across the body or in the hand? → Handbags',
 '<i>Precedence: a laptop pack on both shoulders is a backpack (step 7) before a work bag (step 8); a messenger bag across the body stays in Handbags unless sold as a briefcase; a technical climbing or ski pack goes to Sports.</i>'],
 'b':old.get('b',[]),'depts':D}
# integrity: every old kind accounted
used={k['n'] for d in D for s in d['s'] for k in s['k']}
gone=[n for n in K if n not in used]
print('unused',gone)
tmp=R+'out/A4.json.tmp'; json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'out/A4.json')
# see target check
names=used
for d in D:
    for s in d['s']:
        for k in s['k']:
            for sv in k.get('see',[]):
                if sv[0]=='A4' and sv[1] not in names: print('BAD see',k['n'],sv)
