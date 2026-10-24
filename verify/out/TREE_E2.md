# E2 Sports, Fitness & Recreation: decided tree

Category: E2 Sports, Fitness & Recreation (domain E, Play, Sport & Music). Membership test (CATEGORIES_v0_7, step 26): made for a sport, dance, physical exercise, or an outdoor activity such as hiking, climbing, caving, angling, metal detecting or snow sports: balls, rackets, bats, cues, pool and snooker tables, darts and dartboards, table-tennis tables, bowling balls, fitness machines and fitness trampolines, boards, skates, kick scooters and skis, hang gliders and paragliders, tents and shelters, sleeping bags and sleeping mats, climbing, caving and navigation gear, fishing tackle and spearguns, metal detectors for treasure hunting, winter and water sports gear, combat-sport implements and their protective gear, airsoft and paintball markers, and garments, footwear and protective gear made for the demands of one sport and not suited to everyday wear (step 17). Structure (E-2, Candidate A): sub-family (the kind of activity, an editorial grouping fixed by E-2: E2.1 to E2.15 are the activity families in alphabetical order; E2.16 is the multi-use sub-family, C14(c), leaf axis function, and E2.17 the closing parts sub-family, CV-17, C5(d), leaf axis the object served, both exempt from the level-1 axis), then leaf (the sport or activity the object is made for, with the axis stated per sub-family: exercise mode in E2.9; a general leaf, where one exists, is listed first, C14(b); E2.5 Cycling gear and E2.6 Equestrian have no leaf, C5(b)), then kind (the generic equipment type used in that sport, sport-specific garments, footwear and protective gear included, at the level where buyers compare quality or makers: club type for golf, weapon for fencing, machine for fitness), then named form (design, model or series inside one kind, uncapped, `maker_bound` flagged; not listed here). Region, era, tier, price band, maker, scene, user (child, teen, gender, size, ability), setting, market, power source, material and condition are attributes, tags or views, never kinds or leaves. Measured or conventional specs stay attributes with their scale named: racket head size, weight, balance and U-weight; ski use class, width and radius; ski-boot flex; football-boot ground code; golf iron category; cricket willow grade; rod power and action; wetsuit thickness; ball size and pressure; treadmill drive (C10); mounting and setting (C12); certification as `standard_met` (UIAA, FIE, EN); section 14 adds `resistance_type` (magnetic, friction, fan, water) for exercise bikes. Tier is never on a kind: maker ladders are `line_rank` and tier entries on lines and named forms, `player_level` a skill scheme. Quality markers (proposals.tsv E2, display only): safety gear by certification present and genuine, then fit and compatibility, then activity and skill match; fitness machines by flywheel weight and frame stability, then resistance type, then weight capacity and adjustability; sport boots and shoes by comfort, support, traction, water resistance, durability and weight; rackets and implements by head size, weight and balance against player level. Makers (maker_roles.tsv E2, owner, provisional): sports equipment models carry the maker; shoppers choose the sport and the kind first, makers enter through models and lines, a brand tab sits inside each sport leaf, and artisan cue makers, rod builders, bat makers and board shapers stay in the ledger as owners of their named forms. Display only (section 14, proposals.tsv E2): each sub-family has one display group, shown on its heading with its display position (shopper prominence: fitness first, then hiking and camping, then the rest; provisional, E2-5); the stored alphabetical order and the ids are unchanged, and a group never moves a home or an id. Each sport page also lists the sport's A1, A2 and A4 objects as a generated cross-category view, and the generated view "Running" (E2-3) gathers A2 running shoes, A1 running clothing, A4 running bags and vests, D2 GPS sports watches, H2 sports nutrition and the E2.2.2 Track and field kinds; no Running leaf exists. Kinds are numbered in the order the memo's worked tree prints them; the stored display order is the role-in-play key of memo section 8 and is a separate column (R-58). Kinds and leaves added by section 14 take the next number under their parent. A kind marked † is named only by the key, a decision, the domain review or section 14, and needs a fetched page in the stage-3 harvest before it enters the data; a † kind that cannot be attested leaves the tree. Kinds named with a regional word (judo uniform, shinai, bokken, wushu practice weapon) keep their level as provisional until attested (R-19). Kinds to look for at harvest (no id, R-96 c): the air (fan) bike (E2-1); sport shoes other than football boot, tennis shoe, cycling shoe and track spike (basketball, badminton, golf, padel, pickleball), each only as a performance model under K-127; padel and pickleball nets and posts, only if a page sells them for the one sport (E2-2); caving gear (E2.3.1); gymnastics apparatus (E2.2.3); further parts hosts for E2.17.

Ids (R-58): E2.n is a sub-family and E2.n.m a leaf; a kind is E2.n.m.kk, or E2.n.kk where a sub-family has no leaf.

## E2.1 Air sports
Leaf axis: flying discipline. Display group: Air sports (display position 15).

### E2.1.1 Free flight
- E2.1.1.01 Hang glider: unpowered, foot-launched glider with a rigid frame under a fabric wing, steered by the pilot's weight shift.
- E2.1.1.02 Paraglider: unpowered, foot-launched glider with a flexible ram-air fabric wing hung on suspension lines; a powered paraglider is G1. †
- E2.1.1.03 Free-flight harness: harness that suspends and carries the pilot under a hang glider or paraglider. †

### E2.1.2 Land kiting
- E2.1.2.01 Traction kite: steerable kite made to pull a rider on land (on a buggy, board or skis) or to train for kite sports. †

### E2.1.3 Skydiving
- E2.1.3.01 Parachute: canopy, container and harness system for descending from an aircraft, skydiving rigs included (K-96).

## E2.2 Athletics, gymnastics and dance
Leaf axis: discipline. Display group: Athletics, gymnastics & dance (display position 12).

### E2.2.1 Dance
- E2.2.1.01 Ballet shoe: soft, flexible slipper made for ballet practice and performance. †
- E2.2.1.02 Pointe shoe: ballet shoe with a stiffened box and shank for dancing on the tips of the toes. †
- E2.2.1.03 Tap shoe: dance shoe with metal plates at toe and heel that sound the steps. †
- E2.2.1.04 Dance practice wear: garment made for the demands of dance practice and not suited to everyday wear; E2 only if the P1 test holds, otherwise A1. †

### E2.2.2 Track and field
- E2.2.2.01 Hurdle: barrier on a base that athletes clear in hurdle races, height-adjustable to the race standard. †
- E2.2.2.02 Starting block: pair of angled foot plates fixed to the track that sprinters push off at the start. †
- E2.2.2.03 Starting pistol: blank-firing pistol made to start races; one made for self-defence or deterrence is E4 (P15). †
- E2.2.2.04 Track spike: lightweight running shoe with a spike plate made for track competition. †

### E2.2.3 Gymnastics
Leaf named in memo section 3 (only HS 950691 "gymnastic apparatus" attested); no kind is decided, kinds are found at harvest.

## E2.3 Climbing, caving and navigation
Leaf axis: discipline. Display group: Climbing, caving & navigation (display position 3).

### E2.3.1 Caving
Leaf from the key; no kind is decided, caving gear is found at harvest.

### E2.3.2 Climbing
- E2.3.2.01 Climbing harness: sit harness with leg loops and belay loop that ties the climber into the rope; the UIAA or EN standard is `standard_met`.
- E2.3.2.02 Climbing helmet: helmet made for climbing and mountaineering against falling objects and falls, certified to the UIAA or EN climbing-helmet standard.
- E2.3.2.03 Climbing rope: dynamic or static kernmantle rope made for climbing, rated to UIAA 101 or its EN equivalent.
- E2.3.2.04 Climbing shoe: tight-fitting shoe with a sticky rubber sole and rand made for climbing rock or walls.

### E2.3.3 Orienteering and navigation
- E2.3.3.01 Compass: magnetic compass made for navigation on foot (baseplate, thumb or sighting compass); a drawing compass is C5 (C6-O2). †
- E2.3.3.02 Map case: waterproof transparent case that holds a map for use outdoors. †

## E2.4 Combat and marker sports
Leaf axis: discipline. Display group: Combat & marker sports (display position 11).

### E2.4.1 Airsoft and paintball
- E2.4.1.01 Airsoft marker: replica gun that fires plastic BB pellets by spring, gas or electric power, made for airsoft play; energy limits go to the jurisdiction ledger (C17). †
- E2.4.1.02 Paintball hopper: feed container mounted on a paintball marker that holds the paintballs and feeds them to it. †
- E2.4.1.03 Paintball marker: compressed-gas gun that fires paint-filled balls, made for paintball play. †
- E2.4.1.04 Paintball mask: full-face mask with a goggle lens made to protect the eyes and face from paintballs or airsoft pellets. †

### E2.4.2 Boxing
- E2.4.2.01 Boxing glove: padded glove worn for boxing sparring, bagwork or competition.

### E2.4.3 Fencing
- E2.4.3.01 Foil: light thrusting fencing weapon with a flexible rectangular blade, made to FIE rules for the foil.
- E2.4.3.02 Epee: thrusting fencing weapon with a stiff triangular blade and a large bell guard, made to FIE rules for the epee.
- E2.4.3.03 Sabre (fencing): cutting and thrusting fencing weapon with a knuckle guard, made to FIE rules for the sabre; the sabre sword is E4 (homonym, C9).
- E2.4.3.04 Fencing mask: mesh mask with a bib that protects a fencer's face, head and neck; the FIE 1600 N bib is `standard_met`.
- E2.4.3.05 Fencing jacket: protective jacket made for fencing, rated to a puncture resistance such as FIE 800 N.

### E2.4.4 Judo
- E2.4.4.01 Judo uniform (judogi): heavy cotton jacket and trousers made for judo grips and throws; level provisional until attested in two regions (R-19).

### E2.4.5 Kendo
- E2.4.5.01 Bokken: solid wooden sword made for kendo and other Japanese sword-art practice. †
- E2.4.5.02 Kendo armour: protective armour set made for kendo (head guard, gloves, breastplate and waist guard). †
- E2.4.5.03 Shinai: practice sword of bamboo or carbon staves made for kendo sparring. †

### E2.4.6 Wushu
- E2.4.6.01 Wushu practice weapon: blunt or unsharpened wushu implement (sword, broadsword, staff, spear) made for practice or competition (K-87). †

### E2.4.7 Historical European martial arts (HEMA)
- E2.4.7.01 HEMA training sword: blunt steel or synthetic sword made for HEMA sparring and drills (section 14, provisional). †
- E2.4.7.02 HEMA fencing jacket: padded jacket made for HEMA, rated to a puncture resistance such as 350 N or 800 N, recorded as `standard_met` (section 14, provisional). †
- E2.4.7.03 HEMA protective gloves: padded or plated gloves that protect the hands from sword blows in HEMA sparring (section 14, provisional). †

## E2.5 Cycling gear (no leaf)
Kind axis: equipment type (`leaf = null`, C5(b)). Display group: Cycling gear (display position 4).
- E2.5.01 Cycling shoe: stiff-soled shoe made for cycling, usually with a cleat interface for clipless pedals (cleat systems are C13 rows).
- E2.5.02 Padded cycling shorts: close-fitting shorts with a sewn-in chamois pad made for riding a bicycle. †

## E2.6 Equestrian (no leaf)
Kind axis: equipment type (`leaf = null`, C5(b)); the rider's gear only. Display group: Equestrian (rider) (display position 14).
- E2.6.01 Riding hat: helmet made for horse riding, certified to an equestrian helmet standard (K-125). †

## E2.7 Fishing and hunting
Leaf axis: activity. Display group: Fishing & hunting (display position 13).

### E2.7.1 Angling
- E2.7.1.01 Fishing rod: flexible rod made to cast and play a fish on a line; power and action are attributes.

### E2.7.2 Hunting
- E2.7.2.01 Decoy: model or replica of a bird or animal set out to lure game within range (K-163). †
- E2.7.2.02 Game call: device blown, struck or played electronically that imitates an animal's sound to attract game (K-163). †
- E2.7.2.03 Game trap: snare, leg-hold or body-grip trap made for trapping game or fur animals; mouse, rat, insect and live-catch cage traps are B8.4 (R-6; level provisional, R-19). †
- E2.7.2.04 Hunting blind: portable hide or screen that conceals a hunter from game (K-163). †
- E2.7.2.05 Hunting rangefinder: handheld laser rangefinder made to measure the distance to game (K-148). †

### E2.7.3 Spearfishing
- E2.7.3.01 Speargun: underwater gun powered by rubber bands or compressed air that fires a spear at fish. †

## E2.8 Golf, cue and target sports
Leaf axis: sport. Display group: Golf, cue & target sports (display position 7).

### E2.8.1 Archery
- E2.8.1.01 Archery target: boss, butt or block made to stop arrows, with or without a target face (K-163). †
- E2.8.1.02 Arm guard: guard strapped to the bow arm that protects it from the bowstring (K-163). †
- E2.8.1.03 Finger tab: leather or synthetic pad worn on the drawing fingers to hold and release the string (K-163). †

### E2.8.2 Boomerang
- E2.8.2.01 Boomerang: curved throwing wing made to return to the thrower or fly for distance, in every form (K-84). †

### E2.8.3 Clay shooting
- E2.8.3.01 Clay target: frangible disc thrown as a flying target for clay shooting.
- E2.8.3.02 Clay thrower: hand or machine trap that launches clay targets.

### E2.8.4 Cue sports
- E2.8.4.01 Cue: tapered stick used to strike the balls in pool, snooker and billiards.
- E2.8.4.02 Pool table: cloth-covered slate or board table with cushions, with or without pockets, made for pool, snooker or billiards.

### E2.8.5 Darts
- E2.8.5.01 Dartboard: target board made for darts, of bristle, cork or electronic segments.

### E2.8.6 Golf
- E2.8.6.01 Driver: lowest-lofted wood with the largest head, made to hit the ball off the tee for maximum distance.
- E2.8.6.02 Fairway wood: wood with more loft and a smaller head than the driver, made to be hit from the fairway or tee.
- E2.8.6.03 Hybrid (utility): club with a compact wood-like head that replaces a long iron.
- E2.8.6.04 Iron set: matched set of irons of graded loft with flat-faced heads; iron category (game improvement, players distance, blade) is an attribute.
- E2.8.6.05 Wedge: high-lofted club made for short approach, pitch, chip and bunker shots.
- E2.8.6.06 Putter: low-lofted club made to roll the ball on the green.
- E2.8.6.07 Golf ball: dimpled ball made to the rules of golf.
- E2.8.6.08 Golf rangefinder: handheld laser rangefinder made to measure the distance to the flag; golf GPS units are D2 (K-148). †

## E2.9 Gym, fitness and exercise
Leaf axis: exercise mode. Display group: Gym, fitness & exercise (display position 1).

### E2.9.1 Cardio
- E2.9.1.01 Upright exercise bike: stationary pedal machine with an upright seat and handlebar, the canonical exercise bike; resistance type is the attribute `resistance_type` (section 14 E2-1; the memo's "exercise bike").
- E2.9.1.02 Spin bike (indoor cycling bike): stationary bike with a heavy front flywheel and a road-bike riding position that allows riding out of the saddle (section 14 E2-1, provisional). †
- E2.9.1.03 Recumbent exercise bike: stationary bike with a seat with a backrest and the pedals set forward (section 14 E2-1, provisional). †
- E2.9.1.04 Fitness trampoline: small trampoline (rebounder) with a frame of about 1.2 m or less, sold for exercise; a garden or play trampoline is E1 (K-159, cut provisional). †
- E2.9.1.05 Rowing machine: stationary machine that simulates rowing with a sliding seat and a resisted pull handle.
- E2.9.1.06 Treadmill: machine with a moving belt for walking or running in place; motorised or manual drive is an attribute (C10).

### E2.9.2 Strength training
- E2.9.2.01 Kettlebell: cast weight shaped as a ball with a handle, swung and lifted in training.
- E2.9.2.02 Weight bar: bar made to carry weight plates for lifting (barbell or dumbbell bar).

### E2.9.3 Yoga and Pilates
- E2.9.3.01 Yoga mat: thin, non-slip mat made for yoga and floor exercise.

## E2.10 Hiking, camping and trail
Leaf axis: activity. Display group: Hiking, camping & trail (display position 2).

### E2.10.1 Metal detecting
- E2.10.1.01 Metal detector: handheld search coil and control unit made to find buried metal objects for treasure hunting. †
- E2.10.1.02 Pinpointer: small handheld probe detector that locates a find inside a dug hole. †
- E2.10.1.03 Digging tool: trowel, spade or knife made to dig out finds in metal detecting. †

### E2.10.2 Shelter and sleep
- E2.10.2.01 Bivvy bag: waterproof, breathable sleeping-bag cover used as a minimal shelter. †
- E2.10.2.02 Sleeping bag: insulated bag to sleep in outdoors; season or temperature rating is an attribute.
- E2.10.2.03 Sleeping mat: foam, self-inflating or air pad that insulates and cushions a sleeper from the ground. †
- E2.10.2.04 Tarp shelter: waterproof sheet pitched with poles or lines as a roof shelter. †
- E2.10.2.05 Tent: portable fabric shelter pitched on poles or frames, yurts and tipis included (K-65); a platform built for it is G2.

### E2.10.3 Trekking
- E2.10.3.01 Trekking pole: adjustable walking pole used for support on trails; grip type (I-type, T-type, Nordic) is an attribute.

## E2.11 Racket and paddle sports
Leaf axis: sport. Display group: Racket & paddle sports (display position 5).

### E2.11.1 Badminton
- E2.11.1.01 Badminton racket: light, long-shafted racket strung for badminton; balance, U-weight and flex are attributes.
- E2.11.1.02 Shuttlecock: feathered or plastic-skirted projectile hit in badminton.

### E2.11.2 Table tennis
- E2.11.2.01 Table-tennis bat: wooden blade, with or without rubbers, used to hit the ball in table tennis; grip (shakehand, penholder) is an attribute.
- E2.11.2.02 Table-tennis table: regulation-surface table with a net made for table tennis; indoor or outdoor is an attribute (C12).

### E2.11.3 Tennis
- E2.11.3.01 Tennis ball: felt-covered rubber ball made for tennis; pressurised or pressureless is an attribute.
- E2.11.3.02 Tennis racket: strung racket made for tennis; head size, weight and balance are attributes.
- E2.11.3.03 Tennis shoe: court shoe sold as a performance model with a court-specific sole for tennis; an everyday tennis-lineage sneaker is A2 (K-127).

### E2.11.4 Padel
- E2.11.4.01 Padel racket: solid, stringless perforated racket made for padel (section 14 E2-2, provisional). †
- E2.11.4.02 Padel ball: pressurised felt ball made for padel, slightly less pressurised than a tennis ball (section 14 E2-2, provisional). †

### E2.11.5 Pickleball
- E2.11.5.01 Pickleball paddle: solid, flat-faced paddle made for pickleball (section 14 E2-2, provisional). †
- E2.11.5.02 Pickleball ball: perforated plastic ball made for pickleball (section 14 E2-2, provisional). †

## E2.12 Rolling and board sports
Leaf axis: sport. Display group: Rolling & board sports (display position 10).

### E2.12.1 Inline and roller skating
- E2.12.1.01 Inline skate: boot with a single line of wheels in a frame, made for skating.

### E2.12.2 Kick scootering
- E2.12.2.01 Kick scooter: unpowered scooter with a deck and handlebar, pushed along by foot; a powered kick scooter is G1. †

### E2.12.3 Skateboarding
- E2.12.3.01 Skateboard: unpowered board on two trucks and four wheels, ridden standing; a powered board is G1.

### E2.12.4 Unicycling
- E2.12.4.01 Unicycle: unpowered single-wheel cycle pedalled and balanced by the rider; an electric unicycle is G1 (K-90). †

## E2.13 Snow and ice sports
Leaf axis: sport, with the general leaf first (C14(b)). Display group: Snow & ice sports (display position 9).

### E2.13.1 Snow and ice, general
- E2.13.1.01 Ski goggles: goggles made for skiing and snowboarding against glare, wind and snow (K-125).
- E2.13.1.02 Ski helmet: helmet made for skiing and snowboarding (K-125).

### E2.13.2 Alpine skiing
- E2.13.2.01 Alpine ski: ski made for downhill skiing with a fixed-heel binding; use class, width and radius are attributes.
- E2.13.2.02 Ski boot: rigid plastic-shell boot made to drive an alpine or touring ski through the binding; flex index on the maker's scale is an attribute.

### E2.13.3 Cross-country skiing
- E2.13.3.01 Cross-country ski: long, narrow ski made for Nordic touring or racing with a free-heel binding.

### E2.13.4 Ice skating
- E2.13.4.01 Ice skate: boot with a steel blade made for skating on ice.

### E2.13.5 Ski touring
- E2.13.5.01 Touring ski: light ski made for climbing with skins and descending, used with a touring binding and boot interface (E-16).

### E2.13.6 Sledging
- E2.13.6.01 Sledge: unpowered sled or toboggan ridden downhill on snow or ice for play or sport; a horse-drawn or machine-drawn sleigh is G1 (G-10). †

### E2.13.7 Snowboarding
- E2.13.7.01 Snowboard: single wide board ridden sideways down snow with both feet bound to it.

## E2.14 Team and ball sports
Leaf axis: sport. Display group: Team & ball sports (display position 6).

### E2.14.1 Baseball and softball
- E2.14.1.01 Baseball bat: rounded bat made for baseball or softball; hard-ball or soft-ball and material are attributes.
- E2.14.1.02 Baseball glove: padded leather glove or mitt made for catching in baseball or softball.

### E2.14.2 Cricket
- E2.14.2.01 Cricket ball: hard, leather-covered cork-core ball with a raised seam, made for cricket.
- E2.14.2.02 Cricket bat: flat-faced willow bat made for cricket; willow grade 1 to 4 is an attribute (a retailer convention).

### E2.14.3 Football (soccer)
- E2.14.3.01 Football: inflated ball made for association football; size is an attribute.
- E2.14.3.02 Football boot: studded or bladed boot made for football; the ground code (FG, AG, SG, MG, TF, IC) is an attribute.

### E2.14.4 Rugby
- E2.14.4.01 Rugby ball: oval inflated ball made for rugby; official-ball class and size are attributes.

## E2.15 Water sports
Leaf axis: sport, with the general leaf first (C14(b)). Display group: Water sports (display position 8).

### E2.15.1 Water, general
- E2.15.1.01 Competition swimsuit: racing suit made for competitive swimming; bikinis, trunks and beachwear are A1 (K-126). †
- E2.15.1.02 Swim goggles: watertight goggles made for swimming (K-125). †
- E2.15.1.03 Wetsuit: neoprene suit that insulates the wearer in water, for surfing, diving, triathlon and paddling; thickness is an attribute.

### E2.15.2 Diving and snorkelling
- E2.15.2.01 Diving mask: mask with a glass lens and nose pocket made for diving and snorkelling.

### E2.15.3 Kite and wind sports
- E2.15.3.01 Kitesurf kite: large steerable kite made to pull a rider on a board across water. †
- E2.15.3.02 Wing-foil wing: hand-held inflatable wing that powers a rider on a foil board. †

### E2.15.4 Paddleboarding and bodyboarding
- E2.15.4.01 Bodyboard: short foam board ridden lying prone on waves. †
- E2.15.4.02 Stand-up paddleboard: large board ridden standing and propelled with a paddle, rigid or inflatable. †

### E2.15.5 Surfing
- E2.15.5.01 Surfboard: board ridden standing on breaking waves.

## E2.16 Multisport, fitness and protective gear
Leaf axis: function (C14(c): kinds used across sub-families). Display group: Protective gear & training aids (multisport) (display position 16).

### E2.16.1 Protective guards
- E2.16.1.01 Knee pad: padded guard worn over the knee to protect it in sport. †
- E2.16.1.02 Mouthguard: moulded guard worn over the teeth to protect them in contact sports. †
- E2.16.1.03 Shin guard: rigid or padded guard worn over the shin in sport.

### E2.16.2 Signalling and safety
- E2.16.2.01 Distress flare: pyrotechnic flare that signals distress by light or smoke (K-84). †
- E2.16.2.02 Flare pistol: pistol made to fire distress or signal flares (K-84). †

### E2.16.3 Training aids
- E2.16.3.01 Gymnastic rings: pair of rings hung on straps for gymnastic and bodyweight training. †
- E2.16.3.02 Punch bag: heavy hanging or free-standing bag struck in boxing and fitness training.
- E2.16.3.03 Skipping rope: rope with handles turned and jumped over in training. †

### E2.16.4 Traction and snow travel
- E2.16.4.01 Crampon: spiked frame fitted to a boot for grip on ice and hard snow. †
- E2.16.4.02 Ice axe: axe with a pick and adze made for climbing and travel on snow and ice. †
- E2.16.4.03 Snowshoe: wide frame strapped to a boot to walk on deep snow. †

## E2.17 Parts and accessories made for one object
Leaf axis: the object served (CV-17, C5(d)); further hosts open at harvest. Display group: Parts & accessories for one object (display position 17).

### E2.17.1 Golf clubs
- E2.17.1.01 Golf bag: bag that carries one set of golf clubs (K-137). †

### E2.17.2 Skis and snowboards
- E2.17.2.01 Ski bag: bag that carries one pair of skis; a bag for several pieces is A4 (K-137). †
- E2.17.2.02 Ski binding: binding that fixes a boot to a ski or snowboard and releases it in a fall.

### E2.17.3 Table-tennis bats
- E2.17.3.01 Table-tennis rubber: rubber sheet, with or without sponge, glued to a table-tennis blade; surface (inverted, pimples-out, long pimples) is an attribute.

### E2.17.4 Tennis rackets
- E2.17.4.01 Racket case: case or cover that holds one racket (K-137).
- E2.17.4.02 Tennis string: string sold to string a tennis racket, by the set or the reel.

## Precedence inside E2

- One home per object: a named form, lines row or variant is a ledger row under one kind and never a second home. A kind used in several sports is placed by C14: first the leaf of the sport whose rule or standard defines it (fencing mask E2.4.3.04 by FIE; climbing helmet E2.3.2.02 by UIAA), then the general leaf of the one sub-family that holds all its uses (wetsuit E2.15.1.03 and swim goggles E2.15.1.02 in E2.15.1; ski helmet E2.13.1.02 and ski goggles E2.13.1.01 in E2.13.1), otherwise E2.16 by function (mouthguard E2.16.1.02, knee pad E2.16.1.01, shin guard E2.16.1.03, skipping rope E2.16.3.03, punch bag E2.16.3.02, crampon E2.16.4.01). A generated view lists the kind under every sport that uses it. A Multisport and cross-training leaf opens in E2.16 only if the harvest finds kinds that C14 (a) to (c) cannot place.
- P1, P1b (K-126, A-6). A garment or shoe made for the demands of one sport and not suited to everyday wear (football boot E2.14.3.02, ski boot E2.13.2.02, climbing shoe E2.3.2.04, ballet shoe E2.2.1.01, wetsuit E2.15.1.03, padded cycling shorts E2.5.02) is E2; running shoes, hiking boots, general trainers, leggings, team jerseys and outdoor jackets are A1 or A2. An arm sleeve or arm warmer made for a sport is E2, otherwise A1. Only competition and sport swimwear (E2.15.1.01) and wetsuits are E2; bikinis, swim shorts, trunks and beachwear are A1.
- P2 (K-125, E-23). A helmet goes by the hazard it was made for: armour against weapons is E4 (ballistic and fragmentation helmets E4.8); a helmet made for one sport (ski helmet E2.13.1.02, climbing helmet E2.3.2.02, riding hat E2.6.01, and hockey, American football and swimming helmets found at harvest) is E2; a helmet against other hazards, general cycling and motorcycle helmets included, is A1; riding boots are A2.
- P3 (K-125). Goggles and masks made for one sport (ski goggles E2.13.1.01, swim goggles E2.15.1.02, diving mask E2.15.2.01, paintball mask E2.4.1.04) are E2; sunglasses are A4; safety glasses are A1.
- P4 (K-127). A court, field or gym shoe sold by sport is E2 only as a performance model with sport-specific soles, cleats or spikes, filed as a kind named for the sport (football boot E2.14.3.02, tennis shoe E2.11.3.03, cycling shoe E2.5.01, track spike E2.2.2.04); a basketball- or tennis-lineage sneaker worn every day and a general trainer are A2. Padel and pickleball shoes follow the same test (E2-2).
- P5 (K-137, K-161, CV-17). A bag or case made for one piece or one pair of sport equipment follows it into E2.17 (golf bag E2.17.1.01, ski bag E2.17.2.01, racket case E2.17.4.01, a boot bag for one pair); every other bag is A4 (gym bag, sports backpack, hydration pack sold with its bag, a bag for several rackets or for boots and a helmet, chalk bags, quivers). Drink bottles and bladders are B5.
- P6 (K-89, K-90, G-10). A bicycle, kayak, canoe or boat is G1; an unpowered skateboard (E2.12.3.01), surfboard (E2.15.5.01), stand-up paddleboard (E2.15.4.02), ski, snowboard (E2.13.7.01), sledge (E2.13.6.01), kick scooter (E2.12.2.01), unicycle (E2.12.4.01), hang glider (E2.1.1.01) or paraglider (E2.1.1.02) is E2; a powered board, electric kick scooter, electric unicycle, hoverboard or eFoil is G1; a horse-drawn or machine-drawn sleigh is G1.
- P7, P7b (K-13, K-96). A part, accessory or paddle made for one vehicle follows the vehicle to G1 (kayak paddles, bike pumps, racks, bottle cages); bicycle service tools are C1. A turbo or indoor trainer that holds a real bicycle is G1; an exercise bike that is a complete machine is E2 (E2.9.1.01 to E2.9.1.03), and resistance type (magnetic, friction, fan, water) is the attribute `resistance_type`, never a kind (E2-1). Parachutes and skydiving rigs are E2.1.3.01; a powered paraglider is an aircraft.
- P8 (K-87, section 14 HEMA). A bow or crossbow made for target shooting is E4; a blunted foil, epee or sabre (E2.4.3.01 to E2.4.3.03), shinai (E2.4.5.03), bokken (E2.4.5.01), blunt wushu implement (E2.4.6.01), HEMA training sword (E2.4.7.01), the protective gear for them, and airsoft and paintball markers (E2.4.1.01, E2.4.1.03) are E2; a sword made for fighting, a sharp sword and a sharpened wushu implement are E4; a decorative sword or wushu implement is B4. The HEMA mask is the fencing mask E2.4.3.04; a back-of-head overlay made for one mask is a part in E2.17.
- P9, P9b (K-163, K-137, R-6, K-148, E4-O1). Archery targets, arm guards and finger tabs (E2.8.1.01 to E2.8.1.03), clay throwers and clay targets (E2.8.3.01, E2.8.3.02), decoys, game calls and hunting blinds (E2.7.2.01, E2.7.2.02, E2.7.2.04) are E2; arrows, bolts, bipods and rests are E4 (arrows and bolts E4.9); a quiver is A4; snares, leg-hold and body-grip traps for game or fur are E2.7.2.03, while mouse, rat, insect and live-catch cage traps are B8.4; golf and hunting laser rangefinders are E2 (E2.8.6.08, E2.7.2.05). Ear defenders and safety glasses, shooting glasses included, are A1; a product sold as shooting goggles is placed at harvest.
- P15 (K-84). A blank-firing pistol made to start races is E2.2.2.03; one made for self-defence or deterrence is E4; distress flare pistols and flares are E2.16.2.02 and E2.16.2.01. Boomerangs are E2.8.2.01 in every form; slingshots, blowguns and shuriken are E4 unless made as toys (E1).
- P10, P16, P17 (K-159, K-160, C15). Equipment for a sport is E2 whoever uses it, and junior sizes stay in the sport leaf, size an attribute; play equipment made as a toy (play-set rackets, foam balls, play trampolines, table football) is E1. A trampoline with a frame of about 1.2 m or less sold for exercise is the fitness trampoline E2.9.1.04; a garden or play trampoline is E1. A kite, disc or ball made as a toy that cannot do the sport object's job to its own standard is E1; one made to the sport's standard (an official rugby ball E2.14.4.01, a traction kite E2.1.2.01) is E2. A toy torch is E1 (K-162).
- P11 (K-65, K-30, K-161, K-162). A tent, yurt or tipi (E2.10.2.05), shelter (E2.10.2.04, E2.10.2.01), sleeping bag (E2.10.2.02) or sleeping mat (E2.10.2.03) is E2, and a platform built for a tent is G2; a portable table, chair or camp bed is B1; a camping stove or cookset B5; a lantern, head torch or dive light B3; a cool box goes by its function; gas cylinders and canisters are C8; drink bottles and bladders are B5.
- P12 (E-15, K-125). Equipment fitted to or worn by an animal (saddle, bridle, halter, horse boots, dog harness), dog-sport and dog-agility equipment and riding gear for the horse are B10; the rider's riding hat is E2.6.01, riding boots are A2, and riders' clothing follows P1.
- P13 (E-18, K-41, K-32). A brace or support made to treat or support an injured joint is H2; padded guards worn to protect during a sport (knee pad E2.16.1.01, shin guard E2.16.1.03) are E2; a foam roller, resistance band or recovery tool used in training is E2; a comfort massager is H1; sports nutrition is H2. Sports nutrition and braces appear in generated sport views only.
- P14 (K-6, K-124, K-148, K-151, D-10). A device whose main function is computing, communication or sensing (dive computer, heart-rate strap, GPS sports watch, golf GPS unit) is D2, a GPS sports watch being a smartwatch with `multisport_gps`; a bike computer made to be fitted to a bicycle is G1; an action camera is D4; a stopwatch is A5; laser rangefinders made for golf or hunting stay E2 (E2.8.6.08, E2.7.2.05).
- Navigation and the compass (C6-O2): a compass made for navigation is E2.3.3.01; a drawing compass is C5.
- Parts (S3, CV-17). A part, case or accessory made to be fitted to, used up in or carried with one sport object (ski binding E2.17.2.02, table-tennis rubber E2.17.3.01, tennis string E2.17.4.02) is filed in E2.17 under the object served, never in the host's leaf; protective gear and anything worn on the body are never parts; boxes and storage holding several objects are B1, cleaning products B6.
- Legal classes (C17). Airsoft and paintball energy limits and any licence or registration class for markers go to the jurisdiction ledger, never to a level or a tag on the tree.
- Attributes that are not kinds (4b, E-16, section 14): ski use class, golf iron category, cricket willow grade, racket bands, boot flex, rod power and action, ground code, wetsuit thickness, mounting and setting, treadmill drive and exercise-bike resistance type are attributes; the touring ski E2.13.5.01 is a kind of its own, the alpine ski E2.13.2.01 another. Second-hand condition is a shop facet only and stores no data (C16, E2-4).
