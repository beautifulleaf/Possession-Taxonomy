import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_G1')
from edit import *
spec=dict(
t="Vans, minibuses, taxis, lorries and coaches that a person owns or converts, kept at kind level; a family car → Cars; a van converted for living in → Caravans, motorhomes & trailers.",
ax="Does the vehicle carry a load, passengers or a special job, and on what chassis?",
tt={
"Panel van":"Size:Small (car-derived)|Medium|Large;Wheelbase:Short|Long;Roof:Low roof|High roof;Body:Crew van|Luton / box van;Power:Petrol|Diesel|Battery electric",
"Window van":"Seating:Kombi (seats plus load space)|Passenger (all seats)|Day van",
"Minibus":"Seats:9-seat|12–17 seat;Roof:Standard|High roof;Use:Wheelchair-accessible|School or community",
"Taxi":"Build:London-style purpose-built cab|Saloon-based cab;Access:Wheelchair-accessible",
"Rigid truck":"Body:Box truck (cube truck)|Tipper (dump truck)|Flatbed / dropside|Chassis-cab",
"Special-purpose truck":"Role:Fire engine|Recovery truck|Horsebox lorry|Ambulance|Hearse",
},
see={"Panel van":[["G1","Campervan","a panel van converted for living"]],"Window van":[["G1","Minibus","more seats, same body"]],"Special-purpose truck":[["G1","Horsebox","towed instead of driven"]]},
shelves=[
dict(n="Vans, minibuses & taxis",t="Van-bodied vehicles for people or goods: load vans, seated vans, minibuses and taxis; a lorry → Trucks & buses.",ax="kinds by what fills the body: load only, load and seats, a full set of seats, seats for hire",k=["Panel van","Window van","Minibus","Taxi"]),
dict(n="Trucks & buses",t="Heavy vehicles kept at kind level: lorries, tractor units, buses and special-purpose trucks; a pickup → Cars.",ax="kinds by job: carry a load, pull a trailer, carry passengers, do a special task",k=["Rigid truck","Tractor unit","Bus or coach","Special-purpose truck"]),
])
if __name__=='__main__': apply("Vans, trucks & buses",spec)

spec=dict(
t="Vehicles and trailers for sleeping and living on the road, plus plain load trailers; a house on a fixed site → G2; a tent → E2.",
ax="Is it towed behind a vehicle, driven as a vehicle with living quarters, or a trailer that only carries loads?",
ren={"Sport utility RV":"Toy hauler"},
merge={"Expandable-end trailer":"Folding camper"},
tt={
"Touring caravan":"Axles:Single-axle|Twin-axle;Build:Lightweight fibreglass|Aluminium-bodied;Roof:Fixed roof|Lifting roof",
"Folding camper":"Walls:Hard-top folding camper|Soft-side tent trailer|Expandable-end trailer",
"Fifth-wheel caravan":"Finish:Standard|Luxury",
"Teardrop trailer":"Skin:Classic plywood|Aluminium-skinned;Terrain:Road|Off-road teardrop",
"Toy hauler":"Hitch:Travel-trailer toy hauler|Fifth-wheel toy hauler",
"Off-road camper trailer":"Floor:Hard-floor camper|Soft-floor camper;Form:Camper trailer|Off-road hybrid caravan",
"Campervan":"Roof:Fixed roof (day van)|Pop-top (rising roof)|High top;Fit-out:With washroom|Without washroom",
"Low-profile motorhome":"Bed:Fixed rear bed|Island bed|Twin single beds|Drop-down bed",
"Overcab motorhome":"Chassis:Class C on cutaway van chassis|Super C on truck chassis",
"A-class motorhome":"Engine position:Front-engine|Rear-engine diesel pusher;Base:Bus-based",
"Truck camper":"Roof:Pop-up|Hard-side|Clamshell;Fitting:With slide-out|Flatbed-mounted",
"Expedition vehicle":"Drive:4×4|6×6;Cabin:Demountable cabin|Fixed habitation box",
"Utility trailer":"Type:Box trailer|Boat trailer|Car transporter|Tipper trailer|Motorcycle trailer;Cover:Open|Enclosed;Brakes:Braked|Unbraked",
},
see={"Campervan":[["G1","Panel van","the van it is converted from"]],"Folding camper":[["E2","Tent","tent living without a trailer"]],"Utility trailer":[["C7","Livestock trailer","trailer for animals"]],"Horsebox":[["C7","Livestock trailer","trailer for animals"],["G1","Special-purpose truck","driven horsebox lorry"]],"Teardrop trailer":[["G1","Touring caravan","full-size hard-shell caravan"]],"Toy hauler":[["G1","Fifth-wheel caravan","fifth-wheel layout"]]},
shelves=[
dict(n="Towed caravans & campers",t="Living trailers pulled behind a car or truck; a motorhome with its own engine → Motorhomes & campervans.",ax="kinds by shell: full hard shell, truck-bed hitch, small sleeper, folding or expanding, gear-carrying, rough-ground",k=["Touring caravan","Fifth-wheel caravan","Teardrop trailer","Folding camper","Toy hauler","Off-road camper trailer"]),
dict(n="Motorhomes & campervans",t="Self-propelled living vehicles, from converted vans to coach-sized motorhomes; a trailer to tow → Towed caravans & campers.",ax="kinds by body, from small conversions to coach-sized and off-road builds",k=["Campervan","Truck camper","Low-profile motorhome","Overcab motorhome","A-class motorhome","Expedition vehicle"]),
dict(n="Utility trailers",t="Trailers that carry loads or animals rather than people; a living trailer → Towed caravans & campers.",k=["Utility trailer","Horsebox"]),
])
if __name__=='__main__': apply("Caravans, motorhomes & trailers",spec)
