import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_G1')
from edit import *
B='https://en.wikipedia.org/wiki/List_of_boat_types'
spec=dict(
t="Small motorised vehicles for rough ground, snow, water or a closed course; a road car → Cars; a boat for open water → Boats.",
ax="Where is the vehicle driven: on dirt and sand, over snow and water, or on a closed course?",
add=[dict(n="Airboat",a="swamp boat · fan boat",d="Flat-bottomed boat pushed by an aircraft-style propeller above the stern, used in shallow marsh and swamp.",s=B,tt=[["Seats",["One-seat","Multi-seat"]]]),
dict(n="Hovercraft",a="air-cushion vehicle",d="Craft that rides on a cushion of air, crossing water, mud, ice and land.",s=B,tt=[["Seats",["One-seat","Multi-seat"]],["Power",["Petrol","Electric"]]])],
dem=[("Dune buggy","Sandrail","type"),("Dune buggy","Funco sand cars","r"),("Snowmobile","Ski-Doo","r"),("Snowmobile","Arctic Cat snowmobiles","r"),("Snowmobile","Lynx","r"),("Go-kart","Tony Kart","r"),("Go-kart","CRG","r"),("Go-kart","Birel","r")],
tt={
"Quad bike":"Class:Sport (two-wheel drive, manual)|Utility (four-wheel drive, racks, towing)|Youth;Seats:Single|Two-up;Registration:Off-road only|Road-registered;Vintage:Three-wheeled ATC;Power:Petrol|Electric",
"Side-by-side":"Class:Sport|Utility|Recreational / crossover;Seats:Two-seat|Four- or six-seat (crew);Power:Petrol|Diesel|Electric",
"Dune buggy":"Build:Fibreglass-bodied (Beetle-based)|Tube-frame sand rail;Supply:Kit|Turnkey;Road use:Off-road only|Street-legal;Power:Petrol|Electric",
"Snowmobile":"Class:Trail|Mountain (deep snow)|Snocross / race|Crossover|Touring (two-up)|Utility / working|Youth;Engine:Two-stroke|Four-stroke|Electric",
"Amphibious vehicle":"Form:Amphibious car|Amphibious ATV (6x6, 8x8)|Amphibious quad;Drive on water:Tracks|Outboard",
"Golf cart":"Seats:Two-seat|Four- or six-seat;Fit:Standard|Lifted|Utility bed;Power:Electric|Petrol;Road use:Course only|Street-legal (LSV)",
"Go-kart":"Class:Sprint chassis|Cadet / mini chassis|Shifter|Rental / leisure|Off-road kart|Pedal (children's);Power:Petrol|Electric",
},
see={"Hovercraft":[["G1","Airboat","fan-driven shallow-water boat"]],"Airboat":[["G1","Hovercraft","air-cushion craft"]],"Amphibious vehicle":[["G1","Hovercraft","other land-and-water craft"]],"Go-kart":[["G1","Track and racing car","full-size racing car"]],"Golf cart":[["G1","Side-by-side","larger utility vehicle"]],"Side-by-side":[["G1","Off-roader","road-registered off-road car"]]},
shelves=[
dict(n="Dirt & sand vehicles",t="Open vehicles for rough ground, trails and dunes; a road-registered off-roader → Cars.",ax="kinds by how the rider sits and steers: straddled quad, side-by-side seats, tube-frame buggy",k=["Quad bike","Side-by-side","Dune buggy"]),
dict(n="Snow, ice & water vehicles",t="Machines that cross snow, marsh, ice or water on tracks, skis or air; a boat on open water → Boats.",ax="kinds by surface crossed: snow, land and water, marsh, any flat surface on an air cushion",k=["Snowmobile","Amphibious vehicle","Airboat","Hovercraft"]),
dict(n="Course & track vehicles",t="Small vehicles driven on a golf course or kart track; a full-size racing car → Cars.",k=["Golf cart","Go-kart"]),
])
if __name__=='__main__': apply("Off-road & leisure vehicles",spec)

spec=dict(
t="Aircraft owned privately, from light airplanes and gliders to balloons and ultralights, with warbirds kept; airliners and military fleets are out; a model aircraft → E1, a drone → D4.",
ax="How does the aircraft stay up and move: powered wings, soaring wings, lighter-than-air gas, a rotor, or a fabric wing?",
dem=[("Airship","Hot-air airship","type")],
tt={
"Single-engine piston airplane":"Wing:High wing|Low wing;Landing gear:Tailwheel|Tricycle gear;Undercarriage:Fixed gear|Retractable gear;Engine:Turbocharged|Diesel;Cockpit:Glass cockpit",
"Multi-engine piston airplane":"Cabin:Pressurised;Engine:Turbocharged|Diesel;Thrust:Centreline thrust",
"Turboprop airplane":"Engines:Single-engine|Twin-engine;Cabin:Pressurised",
"Jet":"Class:Very light jet|Light jet|Midsize|Super-midsize|Large-cabin|Ultra-long-range;Engines:Single-engine jet|Twin-engine jet",
"Light-sport and ultralight airplane":"Class:Light-sport (LSA)|Microlight|Ultralight;Wing:High wing|Low wing;Landing gear:Tailwheel;Float:Amphibious",
"Homebuilt aircraft":"Build:Plans-built|Kit-built|Quick-build kit;Material:Metal|Composite|Wood and fabric",
"Aerobatic airplane":"Seats:Single-seat|Two-seat;Wings:Biplane|Monoplane;Class:Unlimited class",
"Floatplane":"Alighting gear:Straight floats|Amphibious floats|Flying-boat hull|Amphibian",
"Warbird":"Role:Piston fighter|Trainer|Jet|Bomber;Form:Two-seat conversion|Replica",
"Glider":"Class:Standard Class|15-metre Class|18-metre Class|Open Class|Club Class;Seats:Single-seat|Two-seater;Era:Vintage wooden",
"Motor-glider":"Launch:Self-launching|Sustainer (turbo)|Touring motor glider;Power:Electric|Front electric sustainer",
"Hot-air balloon":"Class:Hopper (solo)|Sport|Passenger|Special shape;Sold as:Envelope, basket and burner",
"Gas balloon":"Gas:Hydrogen|Helium|Rozière hybrid",
"Airship":"Structure:Blimp|Helium semi-rigid;Lift gas:Helium|Hot air (thermal)",
"Helicopter":"Engine:Piston|Turbine;Seats:Two-seat|Four-seat;Build:Factory built|Kit-built;Landing gear:Skids|Float-equipped",
"Gyroplane":"Cockpit:Open cockpit|Enclosed cockpit;Seats:Single-seat|Tandem two-seat|Side-by-side;Build:Factory built|Homebuilt",
"Powered parachute":"Seats:Single-seat|Two-seat;Power:Petrol|Electric",
"Paramotor":"Launch:Foot-launched|Trike-mounted;Engine:Two-stroke|Four-stroke|Electric;Wing:Reflex paramotor wing",
"Weight-shift trike":"Cockpit:Open cockpit|Pod-faired;Wing:Kingpost wing|Topless strut-braced wing;Seats:Single-seat|Tandem two-seat",
},
see={"Jet":[["F6","Jet","same name, a black gemstone"]],"Paramotor":[["E2","Paraglider","unpowered fabric wing"]],"Weight-shift trike":[["E2","Hang glider","unpowered weight-shift wing"]],"Glider":[["E2","Hang glider","foot-launched glider"]],"Helicopter":[["D4","Camera drone","unmanned rotorcraft"]],"Warbird":[["E1","Model locomotive","scale models are in toys"]] if False else [["G1","Aerobatic airplane","agile piston airplane"]]},
shelves=[
dict(n="Airplanes",t="Powered fixed-wing aircraft named by engine type; a purpose-built airplane → Special-purpose airplanes.",ax="kinds by engine type and number, smallest first",k=["Single-engine piston airplane","Multi-engine piston airplane","Turboprop airplane","Jet"]),
dict(n="Special-purpose airplanes",t="Airplanes defined by how the owner builds or uses them: light-sport rules, home building, aerobatics, water landing or military history; a general touring airplane → Airplanes.",ax="kinds by use or origin: easy licence, home-built, aerobatic, water landing, military heritage",k=["Light-sport and ultralight airplane","Homebuilt aircraft","Aerobatic airplane","Floatplane","Warbird"]),
dict(n="Gliders",t="Aircraft that soar without a main engine, or with a small one for launching or sustaining; a hang glider → E2.",k=["Glider","Motor-glider"]),
dict(n="Balloons & airships",t="Aircraft that float on hot air or gas; a party balloon → B4.",ax="kinds by lift and control: hot air, gas, gas with an engine",k=["Hot-air balloon","Gas balloon","Airship"]),
dict(n="Rotorcraft",t="Aircraft lifted by rotating blades: powered rotor or free-spinning rotor; a drone → D4.",k=["Helicopter","Gyroplane"]),
dict(n="Parachute & weight-shift flyers",t="Light flyers hung beneath a fabric wing, with an engine for take-off and flight; an unpowered paraglider → E2.",ax="kinds by how the pilot is carried: seated under a canopy, carried on the back, hung in a trike under a wing",k=["Powered parachute","Paramotor","Weight-shift trike"]),
])
if __name__=='__main__': apply("Aircraft",spec)

spec=dict(
t="Preserved and privately owned rail vehicles, and horse-drawn carriages, wagons and sleighs; working freight and trams are out; a model train → E1.",
ax="Is it moved along rails, or pulled by a horse on the road?",
dem=[("Handcar","Pump handcar","type"),("Horse-drawn carriage","Coach","type")],
tt={
"Locomotive":"Power:Steam tender engine|Steam tank engine|Vertical-boiler steam|Diesel shunter|Diesel main-line|Electric;Gauge:Standard gauge|Narrow-gauge industrial",
"Railway carriage":"Layout:Corridor|Open;Service:Brake|Sleeper|Dining or buffet|Observation;Goods stock:Goods wagon (heritage)|Brake van",
"Railcar":"Power:Steam railcar|Diesel multiple unit|Railbus;Formation:Single car|With trailer",
"Ride-on miniature locomotive":"Gauge:5 in gauge|7¼ in gauge|10¼ in gauge|15 in gauge;Power:Live steam|Petrol or diesel|Battery electric;Prototype:Scale model|Freelance",
"Handcar":"Drive:Pump handcar|Pedal railbike|Push trolley",
"Motor trolley":"Body:Open|Enclosed cab;Engine:One-cylinder;Use:Towing trailer",
"Horse-drawn carriage":"Wheels:Two-wheeled|Four-wheeled;Body:Open|Closed;Origin:Original antique|Modern reproduction;Use:Competition (marathon) vehicle",
"Horse-drawn wagon":"Wheels:Two-wheeled cart|Four-wheeled wagon;Cover:Covered|Open;Origin:Original antique|Reproduction",
"Romani vardo":"Origin:Original|Restored|New-built",
"Sleigh":"Seats:Single-seat|Double (four-passenger);Body:Open|Enclosed",
},
see={"Locomotive":[["E1","Model locomotive","scale model"]],"Ride-on miniature locomotive":[["E1","Model locomotive","scale model"]],"Horse-drawn wagon":[["C7","Horse-drawn implement","farm implement"]],"Romani vardo":[["G1","Touring caravan","modern towed caravan"]],"Motor trolley":[["G1","Handcar","muscle-powered track vehicle"]]},
shelves=[
dict(n="Heritage rail",t="Preserved rail vehicles owned by societies and individuals, from locomotives to track trolleys and ride-on miniatures; a model railway → E1.",ax="kinds by role on the line: haul trains, carry passengers, self-propelled, track work, small scale",k=["Locomotive","Railcar","Railway carriage","Motor trolley","Handcar","Ride-on miniature locomotive"]),
dict(n="Horse-drawn vehicles",t="Carriages, wagons, living wagons and sleighs pulled by horses; a motor car in carriage style → Cars.",ax="kinds by what it carries: people, goods, a family's home, people over snow",k=["Horse-drawn carriage","Horse-drawn wagon","Romani vardo","Sleigh"]),
])
if __name__=='__main__': apply("Heritage rail & horse-drawn",spec)

spec=dict(
t="Wheeled beds and seats for carrying a baby, young child or small pet; a baby carrier worn on the body → A4; a bicycle trailer → Bicycles.",
ax="How does the passenger travel and where is it pushed: lying or sitting, on pavements, running paths or in a wagon?",
tt={
"Stroller":"Format:Umbrella stroller|Compact travel stroller|Full-size modular stroller;System:Travel system;Seats:Single|Double side-by-side|Double tandem|Single-to-double",
"Pram":"Build:Coach-built pram|Carrycot pram (detachable body)",
"Jogging stroller":"Front wheel:Fixed front wheel|Swivel-and-lock front wheel;Seats:Single|Double",
"Stroller wagon":"Seats:2-seater|4-seater|6-seater",
},
see={"Pram":[["E1","Dolls' pram","toy version"]],"Stroller":[["A4","Soft structured baby carrier","worn on the body"]],"Jogging stroller":[["G1","Bicycle trailer","multisport trailers convert to joggers"]]},
shelves=[dict(n="Prams & strollers",t="Pushchairs for a baby, child or small pet; a baby carrier worn on the body → A4.",ax="kinds by how the passenger travels: lying flat, sitting up, sitting while the parent runs, in a wagon, a pet",k=["Pram","Stroller","Jogging stroller","Stroller wagon","Pet stroller"])])
if __name__=='__main__': apply("Prams & strollers",spec)
