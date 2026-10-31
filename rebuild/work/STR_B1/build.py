import json,sys,copy,os
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_B1')
from tt import TT
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/STR_B1/bak/B1.json'))
K={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
OLDB={dp['n']:dp.get('b') for dp in d['depts']}
OLDN={dp['n']:dp.get('note') for dp in d['depts']}
LIST='https://en.wikipedia.org/wiki/List_of_furniture_types'
GAR='https://en.wikipedia.org/wiki/Garden_furniture'
CH='https://en.wikipedia.org/wiki/List_of_chairs'
def new(n,a,dd,s,**kw):
    k={"n":n,"a":a,"d":dd,"s":s}; k.update(kw); return k
NEW=[
 new("Headboard","bedhead","A board or panel fixed behind the head of a bed, sold with or apart from the frame.",LIST),
 new("Toddler bed","junior bed","A low child's bed, often with side rails, for a child moving out of a cot.",LIST),
 new("Drop-leaf table","flap table","A table whose top has hinged leaves that fold down to save space.",LIST),
 new("Chabudai","Japanese low dining table","A low Japanese dining table used on a tatami floor, often with folding legs.",LIST),
 new("Sewing table","","A table made for machine sewing, with a well or extension for the machine.",LIST),
 new("Washstand","wash stand · basin stand","A small cabinet or stand that carries a wash basin and jug.",LIST),
 new("Monks bench","monk's bench · settle table","A bench whose hinged back swings over to form a table top.",LIST),
 new("Plan chest","map chest · flat file","A chest of wide shallow drawers for storing large flat sheets.",LIST),
 new("Hoosier cabinet","kitchen cabinet (freestanding)","A freestanding American kitchen cupboard with flour bin, sifter and work top.",LIST),
 new("Pie safe","pie cupboard","A cupboard with pierced tin or mesh doors for keeping food ventilated.",LIST),
 new("Hutch","dresser top · Welsh dresser","A cupboard with shelves or glazed doors that stands on a sideboard or base.",LIST),
 new("Baker's rack","bakers rack","An open freestanding metal or wood rack of shelves, often with a work surface.",LIST),
 new("Umbrella stand","","A stand or tub that holds wet umbrellas upright by the door.",LIST),
 new("Clothes valet","valet stand · suit stand","A stand or frame that holds a suit, shirt and trousers overnight.",LIST),
 new("Garden bench","park bench","A bench for outdoor use, made to stand weather.",GAR),
 new("Picnic table","","An outdoor table with attached or separate benches.",GAR),
 new("Patio set","garden set · bistro set","A table sold with matching chairs or sofas for a patio or garden.",GAR),
]
for k in NEW: K[k['n']]=k
# demotions: archetype names dropped (become types / aliases)
DEM={"Gaming chair":["Racing-seat PC gaming chair"],"Bed frame":["Sleigh bed"],"Four-poster bed":["Medieval–Tudor curtained tester bed"],
"Trunk":["Dome-top trunk","Steamer trunk","Wardrobe trunk"],"Display cabinet":["China cabinet","Curio cabinet","Chinese hardwood display cabinet"],
"Desk":["Pedestal desk","Partners desk","Rolltop desk"],"Dining table":["Refectory table","Trestle table"],"Chest of drawers":["Highboy","Commode","Mule chest"],
"Bar cabinet":["Art Deco cocktail cabinet"],"Sideboard":["Danish modern sideboard"],"Storage cabinet":["Round-corner cabinet","Boulle marquetry cabinet"],
"Writing bureau":["Bureau bookcase"],"Secretaire":["Secrétaire à abattant","Cylinder secretary","Mission drop-front desk"],"Stool":["Milking stool"],
"Folding screen":["Byōbu","Byeongpung"],"Ottoman":["Moroccan leather pouf"],"Rocking chair":["Iron rocker"],"Adirondack chair":["Fan-back Adirondack chair"],
"Dining chair":["Ladder-back chair"]}
DEMOTED=[]
for kn,names in DEM.items():
    K[kn]['x']=[x for x in K[kn]['x'] if x['n'] not in names]
    DEMOTED+=names
    if not K[kn]['x']: del K[kn]['x']
# gaming chair named range
K["Gaming chair"]['r']=[["Titan / Omega","Secretlab"]]
# aliases additions
K["Folding screen"]['a']="screen · paravent · pingfeng"
K["Sofa bed"]['a']=K["Sofa bed"]['a']
# new archetypes
def arch(n,dd,y,mk=''):
    return {"n":n,"a":"","d":dd,"mk":mk,"y":y,"s":CH,"v":[]}
K["Dining chair"]['x']+= [arch("Peacock chair","Wegner armchair with a spindle fan back, a Windsor-type design.","1947"),
 arch("The Round Chair","Wegner's round-back armchair with a continuous curved top rail.","1949"),
 arch("Grand Prix chair","Arne Jacobsen's moulded plywood stacking chair.","1957")]
K["Tubular & wire-frame lounge chair"]['x'].append(arch("Brno chair","Cantilevered tubular-steel chair by Mies van der Rohe and Lilly Reich.","1929–30"))
K["Upholstered lounge chair"]['x'].append(arch("Djinn chair","Low foam lounge chair on a steel base, designed by Olivier Mourgue.","1960s"))
# move Elements
def tt(k):
    n=k['n']
    if n in TT:
        k.pop('t',None); k['tt']=TT[n]
    else:
        raise SystemExit('no tt for '+n)
SEE={
"Camp bed":[["E2","Camp bed","same object sold for camping"]],
"Folding chair":[["E2","Camp chair","camping version"]],
"Folding table":[["E2","Camp table","camping version"]],
"Hammock":[["E2","Camping hammock","hung between trees"]],
"Wardrobe":[["G3","Fitted wardrobe","built into the room"]],
"Game table":[["E1","Poker table","casino-style card table"]],
"Trunk":[["A4","Travel trunk","luggage rather than furniture"]],
"Bed guard rail":[["H2","Bed rail","adult care bed rail"]],
"Mattress":[["H2","Pressure-relief mattress","for pressure care"],["B2","Mattress topper","a layer on top"]],
"Bed frame":[["H2","Care bed","adjustable care bed"]],
"Recliner":[["H1","Massage chair","reclining chair with massage"]],
"Folding screen":[["F2","Painted folding screen","screen valued as a painting"]],
"Bar cabinet":[["G3","Built-in wine cabinet","fitted into the kitchen"]],
"Heated low table":[["B2","Kotatsu futon","the quilt that covers it"]],
"Sofa":[["B2","Sofa cover","loose cover for a sofa"]],
"Dining chair":[["B2","Chair pad","seat cushion"]],
"Headboard":[["B2","Headboard cover","fabric cover"]],
"Changing table":[["H1","Changing mat","the mat used on it"],["A4","Changing bag","carried bag"]],
"TV unit":[["D3","TV and speaker stands and mounts","stand for the set only"]],
"Display stand":[["F2","Sculpture stand","stand for artwork"]],
"Desk screen":[["C5","Desk organiser","tidies the desk top"]],
"Sit-stand desk":[["D1","Monitor arm or stand","raises the screen only"]],
"Display cabinet":[["F3","Coin cabinet","collector's cabinet for coins"]],
"Chaise longue":[["Sofas & armchairs_","",""]],
}
SEE.pop("Chaise longue")
SEE["Bunk bed"]=[["B1","Loft bed","one bed raised over open space"]]
SEE["Loft bed"]=[["B1","Bunk bed","two beds stacked"]]
SEE["Gateleg table"]=[["B1","Drop-leaf table","leaves on hinges without a swinging leg"]]
SEE["Drop-leaf table"]=[["B1","Gateleg table","leaves held by swinging legs"]]
SEE["Platform bed"]=[["B1","Divan base","base with a solid top and drawers"]]
SEE["Divan base"]=[["B1","Platform bed","frame without an upholstered base"]]
SEE["Writing bureau"]=[["B1","Secretaire","fall-front rather than slant-front"]]
SEE["Secretaire"]=[["B1","Writing bureau","slant-front rather than fall-front"]]
SEE["Booster seat"]=[["B1","High chair","full chair with legs"]]
SEE["High chair"]=[["B1","Booster seat","seat that straps to a chair"]]
SEE["Sofa bed"]=[["B1","Daybed","a bed that doubles as a seat"]]
SEE["Daybed"]=[["B1","Sofa bed","a sofa that opens to a bed"]]
SEE["Hanging chair"]=[["B1","Hammock","hung without a frame"]]
SEE["Hammock"]=SEE["Hammock"]+[["B1","Hanging chair","hung seat with a rigid frame"]]
SEE["Coat rack"]=[["B1","Umbrella stand","for umbrellas"]]
SEE["Bar stool"]=[["B1","Stool","low stool"]]
for kn,v in SEE.items():
    K[kn]['see']=v
# layout
def S(n,t,ax,kinds): return {"n":n,"t":t,"ax":ax,"k":kinds} if ax else {"n":n,"t":t,"k":kinds}
L=[
("Sofas & armchairs","mixed",
 "Soft upholstered seats for relaxing: sofas for several people and easy chairs, loungers, recliners and rockers for one; an upright chair for a table → Chairs, stools & benches; a garden seat → Garden furniture.",
 "How many people sit and how: several side by side, one in an upright easy chair, or one reclined, stretched out, rocking or hung?",
 [S("Sofas & sofa beds","Seats for two or more with a back and arms, in fixed, sectional or bed-converting form; a seat for one → Armchairs & design lounge chairs.","kinds by build: fixed sofa, buttoned Chesterfield, sections, converting to a bed, floor seating",["Sofa","Chesterfield sofa","Sectional sofa","Sofa bed","Majlis seating"]),
  S("Armchairs & design lounge chairs","Single upholstered seats with arms, from the plain armchair and wingback to the named design lounge chairs; a seat that tilts or moves → Reclining, rocking & hanging seats.","kinds by how the seat is made: upholstered frame, wing back, upholstered design chair, tubular steel, moulded shell or bentwood",["Armchair","Wingback chair","Upholstered lounge chair","Tubular & wire-frame lounge chair","Moulded, shell & bentwood lounge chair"]),
  S("Reclining, rocking & hanging seats","Single seats that hold the body tilted, stretched, rocked, hung or sunk, such as a recliner, chaise longue, rocking chair, hanging chair or bean bag.","kinds by how the body is held: tilted back, stretched out, rocked, hung, sunk into filling",["Recliner","Chaise longue","Rocking chair","Hanging chair","Bean bag chair"])]),
("Chairs, stools & benches","mixed",
 "Upright seats for a table, desk, bar or hall: chairs with backs, work chairs and seats without backs; a soft relaxing seat → Sofas & armchairs; a nursery seat → Nursery & children's furniture.",
 "Is it a chair with a back for eating, a chair for work at a desk, or a seat without a back for one or several people?",
 [S("Dining & side chairs","Upright chairs with backs for eating or occasional seating: dining chairs, Windsor chairs and folding chairs; a desk chair → Desk & gaming chairs.","kinds by build: general dining chair, spindle-back Windsor, folding",["Dining chair","Windsor chair","Folding chair"]),
  S("Desk & gaming chairs","Swivel chairs on a base for long hours at a desk or screen; an upright dining chair → Dining & side chairs.",None,["Office chair","Gaming chair"]),
  S("Stools, benches & footrests","Seats without a back, from a bar stool to a shared bench, a floor chair or a footrest.","kinds by height and posture: tall perch, low seat, shared bench, table-bench, floor level, footrest",["Bar stool","Stool","Bench","Monks bench","Floor chair","Ottoman"])]),
("Tables & desks","mixed",
 "Surfaces at table or desk height for eating, writing, working or putting things down; a surface for storage with doors or drawers → Storage furniture; a garden table → Garden furniture.",
 "What is the surface for: eating, resting things beside seating, writing, or a particular task?",
 [S("Dining & kitchen tables","Tables to eat or prepare food at, fixed or with leaves, high or low; a table for the garden → Garden furniture.","kinds by how the top is held or extended: fixed, hinged leaves, swinging legs, high, island, floor-level",["Dining table","Drop-leaf table","Gateleg table","Bar table","Kitchen island","Chabudai"]),
  S("Living-room & occasional tables","Tables that stand before, beside or behind seating, or carry a tray or drinks, such as a coffee table, side table, console and bar cart.","kinds by where it stands: in front of seating, beside it, against a wall, on a lap or bed, folded away, wheeled, low and heated",["Coffee table","Side table","Console table","Tray table","Folding table","Heated low table","Bar cart","Rolling cart"]),
  S("Desks & writing furniture","Furniture to write or work at, with the writing surface open, sloped, enclosed or adjustable; a table for a single task → Specialist tables.","kinds by how the writing surface is housed: open top, slant front, fall front, side drawers, height-adjustable, on the lap",["Desk","Writing bureau","Secretaire","Davenport desk","Sit-stand desk","Lap desk"]),
  S("Specialist tables","Tables made for one task: dressing, drawing, card games, sewing or washing; a general desk → Desks & writing furniture.","kinds by the task the top is made for: dressing, drawing, games, sewing, washing",["Dressing table","Drafting table","Game table","Sewing table","Washstand"])]),
("Beds & mattresses","mixed",
 "Frames, bases and mattresses to sleep on; a cot or bassinet for a baby → Nursery & children's furniture; bedding and pillows → B2.",
 "Does it hold the sleeper up (frame or base), save space or travel (folding, stacked, raised), or is it the sleeping surface?",
 [S("Bed frames & bases","Frames, bases and headboards that carry a mattress in a fixed place; a bed that folds, stacks or doubles as a seat → Space-saving & portable beds.","kinds by how the sleeper is supported: framed bed, platform, divan, slats, headboard, posts and canopy, woven rope",["Bed frame","Platform bed","Divan base","Slatted bed base","Headboard","Four-poster bed","Charpai"]),
  S("Space-saving & portable beds","Beds that double as a seat, fold away, stack, rise on legs or pack for travel.","kinds by how the bed saves space: doubles as a seat, folds into a wall, stacks, is raised, folds for travel",["Daybed","Wall bed","Bunk bed","Loft bed","Camp bed"]),
  S("Mattresses","The sleeping surface itself, from sprung and foam mattresses to airbeds and floor futons.","kinds by whether the bed is permanent: fixed mattress, inflatable, rolled-out futon",["Mattress","Airbed","Futon mattress"])]),
("Nursery & children's furniture","mixed",
 "Furniture made for babies and small children to sleep, be changed, eat or play in; an older child's bed or desk is ordinary furniture → Beds & mattresses or Tables & desks.",
 "What does the baby or child do on it: sleep, be changed, eat, or play safely?",
 [S("Cots & sleepers","Beds for a baby or toddler, from a bassinet to a toddler bed, with the rails that keep a child in.","kinds by the child's age: newborn, infant, toddler, bed-guard",["Bassinet","Baby cot","Toddler bed","Bed guard rail"]),
  S("Changing, feeding & play","Furniture for caring for a baby: changing, feeding in a raised seat, or playing in an enclosed space.","kinds by what the carer does: change, feed in a chair, feed at the table, contain play",["Changing table","High chair","Booster seat","Playpen"])]),
("Storage furniture","mixed",
 "Cupboards, chests, drawer units and shelving that hold belongings; a box or hook for tidying → Racks, boxes & organisers; a built-in cupboard or fitted kitchen → G3.",
 "How does it hold things: hung behind doors, laid in drawers or a chest, shut or shown in a cabinet, or open on shelves?",
 [S("Wardrobes, chests & drawers","Furniture that shuts clothes and papers away: hanging space behind doors, drawer units and lidded chests.","kinds by how things are kept: hung, laid in drawers, laid in a lidded chest",["Wardrobe","Chest of drawers","Nightstand","Filing cabinet","Plan chest","Blanket chest","Trunk"]),
  S("Regional traditional chests","Chests and cabinets whose form and joinery belong to a Japanese or Korean furniture tradition; a European chest → Wardrobes, chests & drawers.",None,["Tansu","Bandaji"]),
  S("Sideboards, cabinets & vitrines","Cabinets for tableware, drink, display, media, shoes or kitchen food, from sideboards to glass vitrines.","kinds by what it holds: tableware, display, drink, media, general goods, shoes, kitchen food",["Sideboard","Hutch","Display cabinet","Bar cabinet","TV unit","Storage cabinet","Shoe cabinet","Hoosier cabinet","Pie safe"]),
  S("Shelving & bookcases","Open shelves for books and objects, free-standing, modular or fixed to the wall.","kinds by how it stands: case, system, wall-fixed, open rack",["Bookcase","Modular shelving system","Wall shelf","Baker's rack"])]),
("Racks, boxes & organisers","tier",
 "Plain tidying pieces that hold things in a box or basket, or hang or prop them on a rack, hook or hanger; a cupboard or drawer unit → Storage furniture.",
 "Does it hold things in a container, or hang and prop them on a rack, hook or hanger?",
 [S("Boxes, baskets & hanging organisers","Containers for loose items, from lidded boxes to baskets and fabric organisers hung in a wardrobe or on a door.",None,["Storage box","Storage basket","Hanging organiser"]),
  S("Racks, hooks & hangers","Rails, hooks and stands that carry coats, umbrellas, shoes, clothes and bottles.","kinds by what hangs or rests on it: coats, umbrellas, hooks, shoes, garment rail, hanger, suit, bottles",["Coat rack","Umbrella stand","Wall hook","Shoe rack","Clothes rail","Clothes hanger","Clothes valet","Wine rack"])]),
("Screens & stands","mixed",
 "Pieces that divide a space or lift an object for show: screens and dividers, display and plant stands; a cabinet that encloses objects → Storage furniture.",
 "Does it divide a space or raise something for show?",
 [S("Screens & dividers","Free-standing panels that divide or screen a space, folding, rolling or on a desk.",None,["Folding screen","Room divider","Desk screen"]),
  S("Display & plant stands","Stands that lift an object or pot to be seen.",None,["Display stand","Plant stand"])]),
("Garden furniture","mixed",
 "Seats and tables made to stay outdoors; indoor seating → Sofas & armchairs or Chairs, stools & benches; barbecues and fire pits → C2.",
 "Is it a seat or a table, and is it sold singly or as a set?",
 [S("Garden seating","Outdoor seats from loungers and Adirondack chairs to hammocks and garden benches.","kinds by posture: lying, sitting back, hung, sitting upright on a shared bench",["Sun lounger","Adirondack chair","Hammock","Garden bench"]),
  S("Garden tables & sets","Tables for outdoor meals and the matched sets of table and seats sold for a patio.",None,["Picnic table","Patio set"])]),
("Spare parts","tier",
 "Replacement parts for furniture, kept as one entry rather than listed per piece; a part for an appliance → its own category.",
 "Is it a replacement part for a piece of furniture?",
 [S("Spare parts","One entry for the replacement parts owners buy for furniture.",None,["Furniture spare parts"])]),
]
depts=[]
placed=set()
for n,mode,t,ax,shelves in L:
    dp={"n":n,"mode":mode,"t":t,"ax":ax}
    if OLDB.get(n): dp['b']=OLDB[n]
    if OLDN.get(n): dp['note']=OLDN[n]
    dp['s']=[]
    for sh in shelves:
        ks=[]
        for kn in sh['k']:
            k=copy.deepcopy(K[kn]); tt(k); placed.add(kn); ks.append(k)
        sh=dict(sh); sh['k']=ks; dp['s'].append(sh)
    depts.append(dp)
missing=set(K)-placed
assert not missing,missing
out={"c":"B1","rev":True,"lead":d['lead'],"b":d.get('b',[]),
 "ax":"What does the piece do for the household: seat someone, give a surface, hold a sleeper, hold belongings, divide a space, or furnish the garden?",
 "key":[
 "1. Is it made to stay outdoors in a garden or on a patio (lounger, garden bench, picnic table, patio set)? → Garden furniture",
 "2. Is it a soft upholstered seat for relaxing (sofa, armchair, recliner, chaise longue, bean bag)? → Sofas & armchairs",
 "3. Is it an upright chair, stool or bench for a table, desk or bar? → Chairs, stools & benches",
 "4. Is it a surface to eat, write, work or put things on (table, desk, cart)? → Tables & desks",
 "5. Is it a frame, base or mattress to sleep on, or a bed that folds or stacks? → Beds & mattresses",
 "6. Is it made for a baby or small child (cot, high chair, changing table)? → Nursery & children's furniture",
 "7. Is it a wardrobe, chest, drawer unit, cabinet or shelving that holds belongings? → Storage furniture",
 "8. Is it a plain box, basket, rack, hook or hanger for tidying? → Racks, boxes & organisers",
 "9. Does it divide a space or lift an object for show (screen, divider, display or plant stand)? → Screens & stands",
 "10. Is it a replacement part for furniture? → Spare parts",
 "<i>Precedence: outdoor use (step 1) comes before the indoor seat or table steps; a nursery piece (step 6) comes before the general bed, chair or table; a desk chair is a chair (step 3), not a sofa; a built-in or fitted piece → G3.</i>"],
 "depts":depts}
json.dump(out,open(R+'work/STR_B1/B1.new.json','w'),ensure_ascii=False,indent=1)
print('built',len(K),'demoted',DEMOTED)
