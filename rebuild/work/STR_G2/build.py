import json, os, shutil, copy
R='/home/user/Possession-Taxonomy/rebuild/'
src=json.load(open(R+'work/STR_G2/bak/G2.json'))
K={}
for dp in src['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
def pop_x(kind,name):
    xs=K[kind]['x']
    for i,a in enumerate(xs):
        if a['n']==name: return xs.pop(i)
    raise KeyError((kind,name))
def drop_x(kind,names):
    for n in names: pop_x(kind,n)
# --- archetype moves / demotions
for n in ['Dacha','Adobe pueblo-style house','Malay house','Assam-type house']:
    a=pop_x('Detached house',n); K['Cottage']['x'].insert(0 if n=='Dacha' else len(K['Cottage']['x']),a)
drop_x('Farmhouse',[]) 
drop_x('Castle & tower house',['Fortified house'])
drop_x('Palazzo',['Piano nobile apartment'])
drop_x('Chalet',['Alpine chalet'])
drop_x('Multi-unit residential building',['Tenement block'])
drop_x('Fractional & timeshare',['Points-based vacation club','Fractional apartment share'])
drop_x('Private island',['Caribbean resort cay','Aegean private island','Whole populated island'])
drop_x('Sporting estate',['Highland sporting estate'])
drop_x('Equestrian property',['Kentucky bluegrass stud farm'])
drop_x('Vineyard & wine estate',['Bordeaux first-growth château estate','Tuscan coastal tenuta'])
drop_x('Ranch & station',['Texas cattle ranch','Outback cattle station'])
drop_x('Airpark home & private airstrip',['Residential fly-in airpark'])
drop_x('Oast house',['Converted oast'])
drop_x('Bunker',['Home fallout shelter','Missile silo conversion'])
drop_x('Beach hut',['Bournemouth beach hut','Mudeford Spit hut','Brighton bathing box'])
# promote brand-type generics to named residences
sk=K['Serviced & branded residence']
newx=[]
for a in sk['x']:
    if a['n'] in ('Hotel-brand residences','Fashion-house residences','Automotive-marque residences'):
        for v in a['v']:
            newx.append({'n':v['n'],'a':'','d':a['d'],'mk':v['mk'],'y':v.get('y',''),'s':a['s'],'v':[]})
    elif a['n']=='Designer-led branded residences':
        a['n']='YOO residences'; newx.append(a)
    else: newx.append(a)
sk['x']=newx
# --- farm building split
fb=K.pop('Farm building')
def nk(n,a,d,tt,s,**kw):
    k={'n':n,'a':a,'d':d,'tt':tt,'s':s}; k.update(kw); return k
FBS=fb['s']
K['Barn']=nk('Barn','Dutch barn · threshing barn · tithe barn','A large farm building for storing crops and machinery or housing stock, sold on its own or with a farm.',
 [["Use",["Dutch (hay) barn","Threshing barn","Tithe barn"]],["Frame",["Timber frame","Pole","Steel portal frame"]]],FBS)
K['Stable block']=nk('Stable block','stable yard · loose boxes','A range of stables, with or without a yard, held with a farm, estate or house.',
 [["Layout",["American barn (internal aisle)","Traditional yard","Timber loose-box range"]]],FBS)
K['Field shelter']=nk('Field shelter','','A simple open-fronted shed for stock or horses in a paddock.',[["Siting",["Fixed","Mobile on skids"]]],FBS)
K['Granary & cart shed']=nk('Granary & cart shed','granary · cart shed','Small farm buildings for grain or carts, often listed and sold with a house.',
 [["Form",["Granary raised on staddle stones","Loft granary over cart shed","Open cart shed"]]],FBS)
K['Dovecote']=nk('Dovecote','pigeon house · columbarium (bird)','A building for keeping doves or pigeons, often a listed garden or estate feature.',
 [["Plan",["Circular","Square or rectangular","Lectern"]]],FBS)
# --- new kinds
LH='https://en.wikipedia.org/wiki/List_of_house_types'
AR='https://en.wikipedia.org/wiki/Adaptive_reuse'
K['Split-level house']=nk('Split-level house','tri-level · bi-level · raised ranch','A house whose floors are staggered half a storey apart, common in mid-century US suburbs.',
 [["Levels",["Split-entry (bi-level)","Tri-level","Quad-level"]]],LH)
K['A-frame house']=nk('A-frame house','A-frame cabin','A house with steep roof planes reaching near the ground, popular for mid-century holiday homes.',
 [["Size",["Small cabin","Full-size house"]],["Build",["Kit","Architect-designed"]]],LH)
K['Log cabin']=nk('Log cabin','log house · log home','A house built of stacked logs, from a plain frontier cabin to a modern holiday or kit home.',
 [["Log work",["Round log","Hand-hewn","Milled (D-log)"]],["Use",["Main home","Holiday cabin"]]],LH,
 see=[["G3","Garden log cabin","same build as a garden building"]])
K['Barndominium']=nk('Barndominium','barndo · barn home','A home built within or beside a barn-style shell, with workshop, stable or storage under the same roof.',
 [["Frame",["Steel","Timber post-frame"]],["Layout",["Living quarters with attached workshop","Full-width living space"]]],LH)
K['Container home']=nk('Container home','shipping container home · cargotecture','A home made from one or more steel shipping containers, bought as a kit, module or finished unit.',
 [["Container length",["20 ft","40 ft","High-cube"]],["Build",["Single container","Stacked multi-container"]],["Finish",["Bare shell","Insulated and fitted"]]],LH,
 see=[["G3","Shipping container","same box used as a garden building"]])
K['Yurt & ger']=nk('Yurt & ger','yurt · ger · felt house','A round, lattice-walled tent home covered in felt or canvas, from the Mongolian ger to a permanent glamping yurt.',
 [["Cover",["Felt","Canvas","Insulated fabric"]],["Base",["Wood platform","Concrete base","Bare ground"]],["Use",["Full-time home","Glamping","Garden room"]]],'https://en.wikipedia.org/wiki/Yurt')
K['Allotment']=nk('Allotment','Schrebergarten · Kleingarten · community garden plot','A small plot for growing food, rented from a council or leased through an association rather than owned.',
 [["Holding",["Council-rented plot","Association-leased plot"]],["Fittings",["With shed or pavilion","Bare plot"]]],'https://en.wikipedia.org/wiki/Allotment_(gardening)')
K['Factory & warehouse conversion']=nk('Factory & warehouse conversion','mill conversion · silo conversion','A former factory, mill, warehouse or silo converted to homes, held whole or as flats; one flat inside → Loft.',
 [["Former use",["Factory or mill","Warehouse","Grain silo","Mine building"]],["Result",["Single residence","Apartments"]]],AR,
 see=[["G2","Loft","a single flat inside such a building"]])
K['Converted school & civic building']=nk('Converted school & civic building','school conversion · hospital conversion','A former school, hospital, hotel, office or military post converted to a home or flats.',
 [["Former use",["School","Hospital","Hotel","Office block","Military post"]],["Result",["Single residence","Apartments"]]],AR)
K['Treehouse']=nk('Treehouse','tree house · tree fort','A habitable platform or building raised in or around mature trees, built as a home, retreat or holiday let.',
 [["Support",["Built around one tree","Several trees","Freestanding on posts"]],["Use",["Home","Garden retreat","Holiday let"]]],'https://en.wikipedia.org/wiki/Treehouse')
# --- tt for existing kinds
TT={
'Detached house':[["Age",["New-build","Period"]],["Size",["Family","Executive (4–6 bedroom)"]],["Garage link",["Fully detached","Link-detached (joined only by garage)"]]],
'Semi-detached house':[["Pairing",["Mirror-image pair","Linked semi"]],["Age",["Period","Interwar","Post-war","New-build"]]],
'Terraced house':[["Position",["Mid-terrace","End-of-terrace"]],["Age",["Georgian","Victorian","Edwardian","Interwar"]]],
'Townhouse':[["Storeys",["Two-storey","Three-storey","Four-storey or more"]],["Age",["Georgian","Modern townhome (US)"]],["Setting",["Street frontage","Gated development"]]],
'Bungalow':[["Attachment",["Detached","Semi-detached","Terraced"]],["Roof",["Single-storey","Dormer or chalet (rooms in roof)"]],["Frontage",["Plain","Veranda"]]],
'Cottage':[["Material",["Thatched","Stone","Cob","Brick"]],["Tenure or use",["Owner-occupied","Estate cottage (tied)","Holiday cottage"]],["Style",["Vernacular","Cottage orné"]]],
'Farmhouse':[["Land",["With land","Without land"]],["Plan",["Separate house","Housebarn (house and byre under one roof)","Courtyard farmhouse"]]],
'Mews house':[["Origin",["Original converted mews","Modern mews-style new-build"]],["Setting",["Cobbled mews lane","Private courtyard"]]],
'Ranch house':[["Style",["California","Suburban","Storybook"]]],
'Villa':[["Setting",["Holiday villa with pool","Urban or suburban villa"]],["Region",["Mediterranean","Victorian (UK usage)"]]],
'Courtyard house':[["Plan",["Single walled courtyard","Multi-courtyard compound","Round or square communal earth building"]]],
'Mansion':[["Age",["Historic mansion","Modern mega-mansion"]],["Origin",["Architect-built","Developer-built executive home"]]],
'Country house':[["Scale",["Dower house","Hall house","Stately home or power house"]]],
'Château':[["Defence",["Château fort (fortified)","Château de plaisance (unfortified)","Maison forte"]],["Size",["Manoir (small manor)","Full château"]]],
'Castle & tower house':[["Region",["Peel tower","Italian castello or torre"]],["Origin",["Medieval original","Fortified house","Castle-style revival house"]]],
'Palazzo':[["Holding",["Whole palazzo","Piano nobile apartment","Upper-floor apartment"]],["Origin",["Historic","Palazzo-style revival house"]]],
'Chalet':[["Setting",["Alpine village","Ski-in/ski-out","Holiday chalet outside the Alps","Quebec (any holiday dwelling)"]],["Letting",["Private use","Catered (operated holiday let)"]]],
'Hacienda & estancia':[["Part",["Casco (main house)","Whole estate"]],["Origin",["Historic","Hacienda-style new build"]]],
'Hunting & fishing lodge':[["Use",["Shooting lodge","Fishing lodge or hut","Stalking lodge","Hunting cabin"]],["Role",["Principal lodge of a sporting estate","Ancillary estate lodge"]]],
'Flat':[["Size",["Bedsit (not self-contained)","Micro-flat","Studio","One-bed","Two-bed","Three-bed or more"]],["Building",["Mansion block","Purpose-built","Converted house","Tower block","Walk-up"]],["Floor",["Garden","Basement","Upper floor"]],["Tenure",["Leasehold","Commonhold","Strata title","Condominium","Co-op share"]]],
'Penthouse':[["Position",["Set-back rooftop","Full-floor","Flush top-floor unit"]],["Levels",["Single-level","Duplex"]]],
'Loft':[["Origin",["Hard loft (original conversion, exposed structure)","Soft loft (new-build loft style)"]],["Use",["Residential","Live/work","Commercial"]]],
'Maisonette & duplex':[["Levels",["Maisonette (two levels)","Duplex","Triplex"]],["Entrance",["Own front door","Shared entrance"]],["Layout",["Stacked","Scissor-section"]]],
'Serviced & branded residence':[["Operator",["Hotel-attached (in or beside a hotel)","Standalone branded","Non-hotel brand (fashion, car marques)"]],["Management",["Owner-occupied","Rental-pool or managed let","Aparthotel or serviced apartment unit"]]],
'Multi-unit residential building':[["Size",["Two-flat","Three-flat","Fourplex and small multiplex","Block of flats"]],["Tenure",["Freehold block","Housing co-operative building","House in multiple occupation (HMO)"]],["Form",["Converted house","Walk-up block","Garden-apartment block","Tenement block"]]],
'Fractional & timeshare':[["Right held",["Deeded week","Right-to-use contract","Points programme","Fractional title share (one-quarter, one-eighth)"]],["Timing",["Fixed week","Floating week","Rotating (flex) week"]]],
'Kit & prefab house':[["Method",["Modular (volumetric sections craned on)","Panelised (closed-panel timber frame)","Mail-order kit (historic, 1908–1942)"]],["Material",["Log","Cedar post-and-beam","Timber frame","Steel frame"]]],
'Manufactured home':[["Width",["Single-wide (one section, 18 ft or less)","Double-wide (two sections)","Triple-wide or multi-section"]],["Era",["Pre-1976 mobile home (pre-HUD Code)","HUD Code (from 1976)"]]],
'Park home':[["Use",["Residential park home (BS 3632, retirement parks)","Holiday lodge"]],["Units",["Twin-unit","Single-unit lodge"]]],
'Static caravan':[["Width",["10 ft","12 ft","13–14 ft"]],["Specification",["Summer-use (no double glazing or central heating)","Year-round","Residential-spec (BS 3632)"]],["Trim",["Entry","Mid","Flagship"]]],
'Park model':[["Layout",["Single-level","Loft cabin"]],["Roof",["Porch roof","Wedge roof"]],["Siting",["Destination park","Private land"]]],
'Tiny house on wheels':[["Hitch",["Bumper-pull trailer","Fifth-wheel or gooseneck"]],["Layout",["Sleeping loft","Single-level"]],["Build",["Builder-made","Plans or DIY"]]],
'Houseboat':[["Hull",["Converted inland-vessel hull (woonschip)","Steel ship hull with built superstructure (schark)","Concrete-encased hull","Beached hull","Raft house (rumah rakit)"]]],
'Floating home':[["Float",["Log float","Concrete and foam float","Concrete tub (ark)","Concrete barge chained to lake bed"]],["Behaviour",["Fixed","Amphibious (rises on floods)"]]],
'Country estate':[["Land held",["Tenanted farms","Parkland","Home farm","Walled grounds"]],["Region",["British landed estate","American recreational country estate"]]],
'Private island':[["Title",["Freehold","Leasehold (e.g. China, 50-year maximum)"]],["Water",["Sea island","Lake island","Tidal island"]],["Development",["Undeveloped","Resort island with villas"]],["Setting",["Caribbean cay","Aegean island","Whole populated island"]]],
'Sporting estate':[["Quarry",["Red-deer stalking (deer forest)","Driven grouse (grouse moor)","Driven pheasant","Salmon beat and river fishing"]],["Make-up",["Mixed Highland estate with forestry and farm","Sporting rights let separately"]]],
'Equestrian property':[["Use",["Stud farm (breeding)","Livery yard (full, DIY, working)","Racing yard with gallops","Polo estate","Private yard with arena and paddocks","Riding school or trekking yard"]]],
'Vineyard & wine estate':[["Extent",["Planted vineyard parcel","Vineyard with winery","Hobby or lifestyle vineyard"]],["Region",["Bordeaux château estate","Burgundy domaine","Tuscan tenuta","Napa or New World estate"]]],
'Waterfront property':[["Water",["Beachfront or oceanfront","Lakefront","Riverside","Canal-side"]],["Rights",["Littoral rights to low-water line","Riparian rights and fishing","Foreshore publicly owned (UK, Nordic access rules)"]],["Mooring",["Marina berth with home"]]],
'Ranch & station':[["Stock",["Cattle ranch","Sheep station"]],["Tenure",["Freehold","Crown pastoral lease"]],["Use",["Working","Hunting and recreational","Guest or dude ranch","Hobby ranchette"]],["Region",["Texas","Australian outback"]]],
'Airpark home & private airstrip':[["Setting",["Airpark lot with attached hangar","Taxiway-access home","Fly-in community","Estate with private strip"]],["Runway",["Grass","Paved"]]],
'Farm':[["Enterprise",["Arable","Livestock","Dairy","Mixed","Hobby farm"]],["Sale",["Whole farm with farmhouse","Bare arable land"]]],
'Smallholding':[["Enterprise",["Mixed holding","Equestrian smallholding"]],["Use",["Working","Hobby or lifestyle"]]],
'Croft':[["Tenure",["Owner-occupied","Tenanted"]],["Make-up",["Croft with house","Bare land"]]],
'Grazing land':[["Type",["Pasture","Paddock","Meadow","Rough grazing"]]],
'Woodland':[["Purpose",["Amenity","Commercial forestry","Conservation"]],["Status",["Ancient woodland","Plantation"]]],
'Orchard':[["Form",["Traditional standard","Bush"]],["Crop",["Fruit","Nut grove","Olive grove"]]],
'Lake & fishery':[["Water",["Stillwater lake or pond","River beat","Wetland"]]],
'Building plot':[["Permission",["With planning permission","Without planning permission"]],["Services",["Serviced","Unserviced"]],["Route",["Self-build plot","Developer plot"]]],
'Parking space':[["Form",["Open bay","Lock-up garage (separate title)","Underground space"]],["Fittings",["With EV charger","Without"]]],
'Barn conversion':[["Frame",["Timber-framed","Stone","Brick"]],["Extent",["Whole barn","Part of a barn group"]]],
'Converted church & chapel':[["Building",["Anglican church","Nonconformist chapel"]],["Result",["Single house","Flats"]]],
'Oast house':[["Kiln shape",["Roundel (round kiln)","Square kiln"]]],
'Windmill & watermill':[["Power",["Wind","Water"]],["Condition",["Working order","Shell"]]],
"Lighthouse & keeper's cottage":[["Part",["Lighthouse tower","Keeper's cottage"]]],
'Martello tower & fort':[["Condition",["Original shell","Extended with new wing"]]],
'Water tower conversion':[["Result",["Single house","Apartments"]]],
'Railway conversion':[["Building",["Station building","Signal box"]]],
'Earth-sheltered & cave house':[["Earth cover",["Bermed","In-hill","Underground (atrium)","Cave (carved into rock)"]]],
'Bunker':[["Origin",["Former military or civil-defence","Home fallout shelter","Prefab survival shelter"]],["Form",["Surface blockhouse","Underground bunker","Missile silo"]]],
'Folly & tower house conversion':[["Form",["Folly","Tower","Gatehouse","Lodge"]]],
'Beach hut':[["Ownership",["Council-owned and let","Privately owned freehold or leasehold"]],["Resort",["Bournemouth","Mudeford Spit","Brighton (bathing box)"]]],
'Burial plot':[["Occupancy",["Single plot","Companion plot","Family plot","Communal grave space"]],["Setting",["Lawn cemetery","Walled or hedged family estate","Green burial plot (Baumgrab, shared-tree plot)"]]],
'Crypt & mausoleum':[["Form",["Lawn crypt","Mausoleum crypt (indoor)","Private mausoleum"]]],
'Cremation plot & niche':[["Form",["In-ground cremation plot","Columbarium niche","Urn stele (Urnenstele)"]]],
}
for n,tt in TT.items():
    k=K[n]; k.pop('t',None); k['tt']=tt
# --- see links
SEE={
'Houseboat':[["G1","Houseboat","the self-propelled boat; this one stays moored as a home"]],
'Static caravan':[["G1","Touring caravan","the towed holiday caravan"]],
'Tiny house on wheels':[["G1","Fifth-wheel caravan","road-going towed living space"]],
'Park model':[["G1","Fifth-wheel caravan","same RV-chassis build"]],
'Kit & prefab house':[["G3","Garden log cabin","log kits sold as garden buildings"]],
'Parking space':[["G3","Garage","the garage as a building"]],
'Waterfront property':[["G3","Boathouse","a boathouse on the frontage"]],
'Cremation plot & niche':[["F4","Cremation urn","the urn placed in the niche"]],
'Crypt & mausoleum':[["F4","Coffin","what the vault holds"]],
'Burial plot':[["F4","Grave marker","the headstone over the plot"]],
'Farmhouse':[["G2","Barn conversion","a barn turned into a house"]],
'Barn':[["G2","Barn conversion","a barn turned into a house"]],
'Stable block':[["G2","Equestrian property","stables sold as part of a yard"]],
'Country house':[["G2","Country estate","the house with its land"]],
'Hunting & fishing lodge':[["G2","Sporting estate","the lodge with its sporting land"]],
}
for n,s in SEE.items():
    K[n].setdefault('see',[])
    for e in s:
        if e not in K[n]['see']: K[n]['see'].append(e)
# --- structure
def sh(n,t,ax,kinds):
    d={'n':n,'t':t,'k':[K[x] for x in kinds]}
    if ax: d['ax']=ax
    return d
old={d['n']:d for d in src['depts']}
def dp(n,t,ax,shelves):
    o=old[n]; d={'n':n,'mode':o.get('mode'),'t':t,'ax':ax}
    if o.get('note'): d['note']=o['note']
    if o.get('b'): d['b']=o['b']
    d['s']=shelves
    if d['mode'] is None: d.pop('mode')
    return d
houses=dp('Houses','Dwellings built as houses, whether attached or free-standing, small or grand; one dwelling inside a larger building → Flats & apartments, a house converted from another building → Unusual & converted properties.',
 'Where does the house stand and how grand is it: in a town row, on a suburban or detached plot, in the countryside, or as a grand seat?',[
 sh('Town houses','Houses built in towns and cities that share walls or sit tightly on a narrow plot; a free-standing house on its own plot → Suburban & detached houses.',
  'kinds by how the house meets its neighbours: one shared wall, a continuous row, a tall narrow city house, a former mews, a house round a yard',
  ['Semi-detached house','Terraced house','Townhouse','Mews house','Courtyard house']),
 sh('Suburban & detached houses','Houses standing on their own plot, in suburbs and small towns; a house in a row → Town houses, a large country seat → Grand houses.',
  'kinds by shape and storeys: free-standing house, single storey, mid-century spread, staggered levels, garden villa',
  ['Detached house','Bungalow','Ranch house','Split-level house','Villa']),
 sh('Country & farm houses','Houses in the countryside, from small cottages to working farmhouses and timber holiday homes; a farm with its land → Farm in Land & estates.',
  'kinds by use: small rural home, working farm dwelling, barn-style home, timber holiday homes, sporting lodges',
  ['Cottage','Farmhouse','Barndominium','Log cabin','Chalet','A-frame house','Hunting & fishing lodge']),
 sh('Grand houses','Large houses built as the seat of a wealthy or noble household; a house with its farms and parkland → Country estate.',
  'kinds by national tradition: the general mansion, English country house, French château, castle, Italian palazzo, Spanish-American estate house',
  ['Mansion','Country house','Château','Castle & tower house','Palazzo','Hacienda & estancia'])])
flats=dp('Flats & apartments','A dwelling held as part of a building with other homes, or a whole building of such homes; a house sharing walls → Houses, a whole converted factory → Unusual & converted properties.',
 'Is it one unit held outright, a unit with hotel services or a part share, or a whole building of units?',[
 sh('Single units','One self-contained unit held outright within a larger building; a whole building of flats → Whole buildings.',
  'kinds by position and layout in the building: ordinary flat, top floor, open industrial space, two-level unit',
  ['Flat','Penthouse','Loft','Maisonette & duplex']),
 sh('Managed & part-owned units','Units whose use is run by an operator or shared among owners; an ordinary flat held outright → Single units.',
  None,['Serviced & branded residence','Fractional & timeshare']),
 sh('Whole buildings','A building of two or more dwellings held as one object; one flat inside it → Single units.',None,['Multi-unit residential building'])])
fact=dp('Factory-built, mobile & floating homes','Homes made in a factory, carried on a chassis, portable or afloat; a site-built house → Houses, a touring caravan or motorhome → G1.',
 'How is the home made and moved: craned onto a foundation, built on a chassis in a park, small and portable, or afloat?',[
 sh('Modular, kit & container homes','Homes delivered as kits, panels, modules or steel containers and fixed to a foundation; a home on a chassis → Chassis-built homes.',None,['Kit & prefab house','Container home']),
 sh('Chassis-built homes','Factory-built homes on a steel chassis, sited in a park or on a plot; a home on a road trailer to tow → Small & portable homes.',
  'kinds by the standard they are built to and where they stand: US federal code, US recreational park, UK residential park, UK holiday park',
  ['Manufactured home','Park model','Park home','Static caravan']),
 sh('Small & portable homes','Small homes that can be moved or taken down; a full-size home on a chassis → Chassis-built homes.',None,['Tiny house on wheels','Yurt & ger']),
 sh('Floating homes','Dwellings that live on water; a self-propelled boat → G1.',None,['Houseboat','Floating home'])])
land=dp('Land & estates','Land and land-based holdings kept for a way of life, farming, building or parking, with the buildings of a farm or estate; a house on its own plot → Houses.',
 'What is the land or building held for: a way of life or sport, farming, a farm building, or building and parking?',[
 sh('Estates & lifestyle land','Land held for the way of life it gives rather than for crops; a working farm → Farms & rural land.',
  'kinds by what the land is held for: a landed seat, field sports, wine, horses, an island, a waterfront, flying',
  ['Country estate','Sporting estate','Vineyard & wine estate','Equestrian property','Private island','Waterfront property','Airpark home & private airstrip']),
 sh('Farms & rural land','Land held to grow crops, graze stock or keep trees; an estate kept for sport → Estates & lifestyle land.',
  'kinds by size and use: whole holdings, small holdings, then single land uses',
  ['Farm','Ranch & station','Smallholding','Croft','Allotment','Grazing land','Woodland','Orchard','Lake & fishery']),
 sh('Farm & estate buildings','Working buildings on a farm or estate, sold alone or with land; a barn made into a home → Barn conversion.',
  'kinds by what the building keeps: crops and machinery, horses, grain, field stock, birds',
  ['Barn','Stable block','Granary & cart shed','Field shelter','Dovecote']),
 sh('Plots & parking','Small parcels of land held to build on or to park on.',None,['Building plot','Parking space'])])
unus=dp('Unusual & converted properties','Buildings made for something other than a house, or built in an odd way, that people buy as homes; an ordinary house → Houses, a garden building → G3.',
 'What was the building first made for: farm or industry; worship, public service or defence; or pleasure and shelter?',[
 sh('Farm & industrial conversions','Former working buildings of farm, mill or railway made into homes; a flat inside one → Flats & apartments.',
  'kinds by the building\'s first trade: farming, hop-drying, milling, manufacture, water supply, rail',
  ['Barn conversion','Oast house','Windmill & watermill','Factory & warehouse conversion','Water tower conversion','Railway conversion']),
 sh('Worship, civic & defence conversions','Former churches, schools, lighthouses and fortifications made into homes.',
  'kinds by first public purpose: worship, schooling and civic use, navigation, coastal defence, wartime shelter',
  ['Converted church & chapel','Converted school & civic building',"Lighthouse & keeper's cottage",'Martello tower & fort','Bunker']),
 sh('Pleasure & shelter buildings','Buildings made for show, play or shelter that are also owned as homes or retreats.',
  'kinds by how it shelters: a folly tower, a tree, the ground, the beach',
  ['Folly & tower house conversion','Treehouse','Earth-sheltered & cave house','Beach hut'])])
buri=dp('Burial places','A space owned or leased to bury a body or keep ashes; a coffin, urn or headstone → F4.',
 'Where do the remains lie: in the ground, above ground in a building, or as ashes in a niche?',[
 sh('Graves, vaults & niches','Spaces held in a cemetery or on private land for a burial or for ashes.',None,['Burial plot','Crypt & mausoleum','Cremation plot & niche'])])
out=dict(src)
out['ax']='What is the property: a house, a unit in a larger building, a factory-built or floating home, land, a converted or odd building, or a burial space?'
out['key']=[
 '1. Is it a house, from cottage to castle, standing alone or in a row? → Houses',
 '2. Is it one dwelling, or a share of one, inside a larger building, or a whole building of flats? → Flats & apartments',
 '3. Was it made in a factory, carried on a chassis, portable, or afloat? → Factory-built, mobile & floating homes',
 '4. Is it land, a farm or estate building, a plot or a parking space? → Land & estates',
 '5. Was the building first made for something other than a house, or built in an odd way (barn, mill, church, fort, folly, cave, tree)? → Unusual & converted properties',
 '6. Is it a space to bury a body or keep ashes? → Burial places',
 '<i>Precedence: a mobile or floating home is step 3 before step 1; a whole converted building is step 5 but one converted flat is step 2; a farmhouse with its land is step 1, bare farmland step 4.</i>']
out['depts']=[houses,flats,fact,land,unus,buri]
# integrity: every original kind accounted
placed={k['n'] for d in out['depts'] for s in d['s'] for k in s['k']}
missing=[n for n in K if n not in placed]
print('unplaced',missing)
tmp=R+'work/STR_G2/G2.new.json'
json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1)
json.dump({"Farm building":"Barn"},open(R+'out/G2_renames.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(tmp,R+'out/G2.json'); os.replace(R+'out/G2_renames.json.tmp',R+'out/G2_renames.json')
print('ok')
