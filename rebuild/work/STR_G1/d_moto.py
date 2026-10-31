import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_G1')
from edit import *
S='https://en.wikipedia.org/wiki/Types_of_motorcycles'
spec=dict(
t="Powered two- and three-wheelers ridden astride or standing, from road bikes to personal electric machines; a pedal bicycle → Bicycles; riding clothing → Motorcycle riding gear.",
ax="Where and how is the machine ridden: on the road, in the dirt, as a small step-through, or on a personal electric board?",
add=[dict(n="Dual-sport motorcycle",a="dual-purpose · trail-legal enduro",d="Road-legal motorcycle with long-travel suspension and a tall seat, lighter than an adventure bike and equally at home on dirt tracks.",s=S,tt=[["Bias",["Road-biased","Dirt-biased"]],["Engine size",["Under 400 cc","400–650 cc"]],["Start",["Kick start","Electric start"]]])],
dem=[("Chopper and bobber","Bob-job","type"),("Leather race suit","One-piece racing leathers","type")] if False else [("Chopper and bobber","Bob-job","type")],
tt={
"Standard motorcycle":"Style:Naked|Retro (modern classic)|Streetfighter;Licence:Learner-legal (A2)",
"Sport motorcycle":"Class:Lightweight sport|Supersport (600–750 cc)|Superbike (1000 cc class)|Hypersport|Sport-touring",
"Cruiser motorcycle":"Style:Classic cruiser|Power cruiser|Bagger|Factory custom",
"Touring motorcycle":"Equipment:Full dresser|Bagger;Style:Sport-tourer|Luxury tourer",
"Adventure motorcycle":"Size:Middleweight adventure|Large adventure;Style:Adventure-touring|Rally replica",
"Café racer":"Origin:Factory café racer|Custom café racer",
"Scrambler":"Era:Classic scrambler|Modern-classic scrambler",
"Chopper and bobber":"Style:Chopper|Bobber;Origin:Factory custom|Home-built",
"Trike":"Layout:Conventional (two rear wheels)|Reverse (two front wheels);Origin:Factory built|Trike conversion",
"Motorcycle with sidecar":"Drive:Single-wheel drive|Sidecar-wheel drive (2WD);Origin:Factory outfit|Sidecar conversion",
"Motocross bike":"Engine:Two-stroke|Four-stroke|Electric;Class:Youth and minicross (50–85 cc)|125 cc / 250F class|250 cc two-stroke|450 cc four-stroke",
"Enduro bike":"Engine:Two-stroke|Four-stroke;Registration:Road-registered|Competition only;Style:Cross-country (XC)|Wide-ratio gearbox",
"Trials bike":"Engine:Two-stroke|Four-stroke|Electric;Era:Classic twin-shock|Modern;Rider:Youth|Adult",
"Trail bike":"Clutch:Automatic|Semi-automatic|Manual clutch;Start:Kick start|Electric start;Rider:Children's|Adult",
"Supermoto":"Use:Road-legal|Competition",
"Pit bike":"Engine size:50 cc|110–190 cc;Engine:Honda-clone engine",
"Scooter":"Style:Classic scooter|Maxi-scooter|Three-wheel tilting scooter;Power:Petrol|Electric",
"Moped":"Style:Pedal moped|Step-through moped|Sports moped;Power:Petrol|Electric",
"Underbone motorcycle":"Style:Step-through cub|Sports underbone",
"Electric kick scooter":"Class:Folding commuter|Dual-motor performance;Rider:Adult|Children's",
"Electric unicycle":"Suspension:Suspension|Non-suspension;Seating:Standing|Seated",
"Powered skateboard":"Board:Mini board|Street (flexy) board|All-terrain (2-in-1) board|Off-road mountainboard|Racing board|Folding board|One-wheel board;Drive:Hub drive|Direct drive|Belt drive|Gear drive",
},
see={
"Electric kick scooter":[["E2","Kick scooter","pushed by foot, no motor"]],
"Electric unicycle":[["E2","Unicycle","pedalled one-wheeler"]],
"Powered skateboard":[["E2","Skateboard","pushed by foot, no motor"]],
"Pit bike":[["G1","Mini bike","small fun bikes"]],
"Mini bike":[["G1","Pit bike","small off-road bikes"]],
"Adventure motorcycle":[["G1","Dual-sport motorcycle","lighter, dirt-biased cousin"]],
"Dual-sport motorcycle":[["G1","Adventure motorcycle","larger touring cousin"]],
"Trike":[["G1","Three-wheeled car","car-style three-wheeler"]],
"Scooter":[["H2","Mobility scooter","for reduced mobility, not a motorcycle"]],
},
shelves=[
dict(n="Road motorcycles",t="Motorcycles built mainly for the road, named by riding position and what the engine is tuned for; a retro-look bike → Retro & custom styles.",ax="kinds by riding position and purpose: upright all-rounder, lean-forward speed, laid-back cruising, distance, mixed surfaces",k=["Standard motorcycle","Sport motorcycle","Cruiser motorcycle","Touring motorcycle","Adventure motorcycle"]),
dict(n="Retro & custom styles",t="Bikes styled on an older scene, whether made by a factory or built at home; a plain modern bike → Road motorcycles.",ax="kinds by the scene whose look they copy: 1960s road racing, 1950s dirt riding, post-war custom",k=["Café racer","Scrambler","Chopper and bobber"]),
dict(n="Three-wheelers & sidecars",t="Motorcycles that carry extra weight on a third wheel or a sidecar; a three-wheeled car → Cars.",ax="kinds by what carries the extra weight: a rear axle or a sidecar",k=["Trike","Motorcycle with sidecar"]),
dict(n="Off-road motorcycles",t="Lightweight motorcycles for dirt, from competition machines to trail and fun bikes; a bike for tarmac and gravel touring → Adventure motorcycle.",ax="kinds by what the rider does: race a short track, race a long course, climb obstacles, mix tarmac and dirt, ride trails",k=["Motocross bike","Enduro bike","Trials bike","Supermoto","Dual-sport motorcycle","Trail bike","Pit bike"]),
dict(n="Scooters, mopeds & cubs",t="Small-engined step-through machines for short trips; a pedal-assisted bicycle → Electric bike.",ax="kinds by frame and engine layout: scooter platform, pedal frame, cub underbone, mini frame",k=["Scooter","Moped","Underbone motorcycle","Mini bike"]),
dict(n="Electric rides",t="Personal electric machines ridden standing or balancing; a motorised bicycle → Electric bike.",ax="kinds by how the rider stands and balances: deck with handlebar, board, one wheel, two wheels side by side",k=["Electric kick scooter","Powered skateboard","Electric unicycle","Hoverboard","Self-balancing personal transporter"]),
])
if __name__=='__main__': apply("Motorcycles & scooters",spec)

spec2=dict(
t="Clothing and protection worn to ride a motorcycle; a leather jacket worn for fashion → A1; a bicycle or ski helmet → E2.",
ax="Which part of the rider does it protect or serve: the head, the body, or the hands and feet?",
tt={
"Full-face helmet":"Shell:Polycarbonate|Fibreglass composite|Carbon-fibre or Kevlar composite;Fit:Round|Intermediate-oval|Long-oval;Use:Race (FIM-homologated)|Sport-touring|Retro",
"Modular helmet":"Homologation:P/J double-homologated;Features:Internal sun visor|Intercom-ready",
"Open-face helmet":"Cover:Three-quarter (jet)|Half helmet (shorty);Visor:Snap-on visor|Bubble shield",
"Off-road helmet":"Shell:Fibreglass composite|Carbon-fibre;Liner:MIPS or rotational-impact liner",
"Dual-sport helmet":"Features:Removable peak|Goggle-compatible eye port",
"Motorcycle boot":"Use:Race|Sport|Touring|Adventure|Urban",
"Textile riding suit":"Use:Adventure|Touring|Urban;Make:One-piece|Two-piece;Waterproofing:Laminated|Drop-liner;Protection:CE class A|CE class AA|CE class AAA",
"Leather race suit":"Make:One-piece|Two-piece zip-together;Leather:Cowhide|Kangaroo leather;Fit:Off the peg|Made-to-measure;Airbag:Airbag-ready",
"Motorcycle gloves":"Use:Race gauntlet|Sport short-cuff|Summer mesh|Touring waterproof|Adventure;Heating:Heated;Protection:EN 13594 Level 1|EN 13594 Level 2",
"Motorcycle airbag vest":"Trigger:Tethered mechanical|Electronic standalone;Fitting:Integrated in jacket|Integrated in race suit|Over-jacket vest|Under-jacket vest",
"Back and body protector":"Coverage:Centre back|Full back|Chest protector|Limb insert armour;Fitting:Strap-on|Insert;Rating:CE Level 1|CE Level 2",
"Helmet communicator":"Link:Bluetooth intercom|Mesh intercom;Pack:Single pack|Duo pack;Fitting:Clip-on|Helmet-integrated",
},
see={"Leather race suit":[["A1","Biker jacket","street leather jacket"]],"Back and body protector":[["G1","Motorcycle airbag vest","inflating protection"]],"Motorcycle airbag vest":[["G1","Back and body protector","fixed-armour protection"]]},
shelves=[
dict(n="Head: helmets & communicators",t="Helmets in four cover levels and the intercoms that clip to them; a helmet for one other sport → E2.",ax="kinds by how much of the head is covered, most first, then the communicator fitted to any of them",k=["Full-face helmet","Modular helmet","Dual-sport helmet","Off-road helmet","Open-face helmet","Helmet communicator"]),
dict(n="Body: suits & protectors",t="Suits that cover the rider and the armour or airbags worn in or over them; a fashion biker jacket → A1.",ax="kinds by layer: the outer suit first, then protection worn in or over it",k=["Leather race suit","Textile riding suit","Motorcycle airbag vest","Back and body protector"]),
dict(n="Hands & feet: gloves & boots",t="Gloves and boots made for riding; walking boots and gloves → A2.",k=["Motorcycle gloves","Motorcycle boot"]),
])
if __name__=='__main__': apply("Motorcycle riding gear",spec2)
