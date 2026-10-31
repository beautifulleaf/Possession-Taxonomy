import json, os
KW="https://en.wikipedia.org/wiki/Kong_(dog_toy)"; AG="https://en.wikipedia.org/wiki/Dog_agility"
FB="https://en.wikipedia.org/wiki/Flyball"; FR="https://en.wikipedia.org/wiki/Frisbee"
NY="https://nylabone.com/about-us/our-story"; WP="https://westpaw.com/products/hurley-dog-bone"
HY="https://hyperflite.com/the-hyperflite-story/"; CH="https://madegooddesigns.com/?p=92499"
NO="https://outwardhound.com/furtropolis/product/the-ultimate-guide-to-nina-ottosson-dog-puzzles"
LM="https://www.vetnpetdirect.com.au/collections/lickimat-range-for-dogs"
DK="https://www.gundogmag.com/editorial/dokken-puppy-dead-fowl-trainer/471602"
SU="https://www.shootinguk.co.uk/?p=10411"
SS="https://www.sportingsaint.co.uk/choosing-the-right-canvas-dummy-for-gundog-training-sizes-options-and-benefits/"
AK="https://www.akc.org/expert-advice/sports/akc-scent-work-supplies-for-beginners/"
ER="https://globalpetindustry.com/article/earth-rated-canada"
def v(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def ag(n,a,d,vs,dt=""): return {"n":n,"a":a,"d":d,"mk":"","y":"late 1970s","s":AG,"v":vs,"dt":dt}
kinds=[
{"n":"Dog chew toys","a":"chew toys · chews","d":"A durable toy made for a dog to chew on rather than eat.",
 "t":["natural rubber","nylon","thermoplastic (TPE)","antler and wood"],"s":"https://www.petsathome.com/category/dog",
 "x":[{"n":"KONG Classic","a":"Kong","d":"Hollow, snowman-shaped rubber toy that bounces erratically and can be stuffed with food or frozen.","mk":"Kong Company","y":"1970s","s":KW,
   "v":[v("KONG Classic","Kong Company","","red rubber, standard strength"),v("KONG Extreme","Kong Company","","black rubber for strong chewers"),v("KONG Puppy KONG","Kong Company","","softer rubber for puppies")],
   "dt":"sizes XS–XXL · rubber compounds by chewing strength"},
  {"n":"Nylabone nylon chew bone","a":"Nylabone","d":"Hard nylon bone-shaped chew; the first nylon dog chew.","mk":"Nylabone","y":"1955","s":NY,
   "v":[v("Nylabone Power Chew Classic Bone","Nylabone","","for strong chewers"),v("Nylabone Comfort Hold X-Bone Puppy Power Chew","Nylabone","","puppy line")],
   "dt":"strength lines Puppy, Flexi, Strong, Power Chew · flavours · sizes"},
  {"n":"West Paw Hurley","a":"Hurley bone","d":"Bone-shaped chew moulded from recyclable Zogoflex that floats and does not splinter.","mk":"West Paw","y":"","s":WP,
   "v":[],"dt":"sizes XS 11 cm, S 15 cm, L 21 cm · colours"}],
 "m":[["Benebone Wishbone","Benebone"],["Arm & Hammer Super Treadz Gorilla Dental Chew","ARM & HAMMER"],["KONG Extreme Goodie Bone","Kong Company"],["WoofBite Indestructible Chew Stick","WoofBite"],["PeaksNPaws Large Whole Elk Antlers","PeaksNPaws"]]},
{"n":"Dog fetch toys","a":"balls · ball launchers · flying discs","d":"Balls, launchers and flyers made to be thrown for a dog to retrieve.",
 "t":["ball","ball launcher","flying disc","floating water toy"],"s":"https://www.petsmart.com/dog/toys/fetch-toys",
 "x":[{"n":"Chuckit! ball launcher","a":"Chuckit","d":"Long plastic arm with a cupped end that picks up and throws a tennis ball further without bending.","mk":"Chuckit!","y":"","s":CH,
   "v":[v("Chuckit! Ultra launcher","Chuckit!","by 2008"),v("Chuckit! Jr.","Chuckit!","by 2008","shorter launcher"),v("Chuckit! Pocket","Chuckit!","by 2008","folding"),v("Chuckit! Mini","Chuckit!","by 2008"),v("Chuckit! Ultra Ball","Chuckit!","","rubber ball sized for the launchers")],
   "dt":"arm length about 26–27 in · ball sizes"},
  {"n":"Frisbee flying disc","a":"Pluto Platter · flying disc","d":"Plastic flying disc that set the pattern for all modern discs, thrown for dogs in disc-dog sport.","mk":"Wham-O","y":"1957","s":FR,
   "v":[v("Pluto Platter","","1955","Fred Morrison's design, bought by Wham-O"),v("KONG Flyer","Kong Company","","soft rubber dog flyer")],"dt":"diameter · rigid or pliable plastic"},
  {"n":"Hyperflite competition dog disc","a":"K-10","d":"Flying disc designed for canine disc competition, with grip surfaces that spare a dog's teeth.","mk":"Hyperflite","y":"2000s","s":HY,
   "v":[v("K-10","Hyperflite","","first Hyperflite disc"),v("Jawz","Hyperflite","","puncture-resistant polymer"),v("FrostBite","Hyperflite"),v("SofFlite","Hyperflite","","soft disc"),v("Pup","Hyperflite","","about one-third smaller K-10")],
   "dt":"polymer · diameter · colours"}],
 "m":[["KONG AirDog Squeakair Ball","Kong Company"],["KONG Jumbler Ball","Kong Company"],["KONG Aqua","Kong Company"],["Goughnuts Virtually Indestructible Ball","Goughnuts"],["Monster K9 Indestructible Dog Ball","Monster K9"],["K9 Ops Dog Ball on a Rope","K9 Ops"],["TIAKI Spiky Ball Dog Toy","TIAKI"]]},
{"n":"Dog puzzle and treat-dispensing toys","a":"puzzle toys · enrichment toys · lick mats","d":"Toys a dog works at with nose, paws or tongue to get food out.",
 "t":["puzzle board","treat-dispensing ball or toy","lick mat","snuffle mat"],"s":"https://www.petsmart.com/dog/toys/interactive-toys",
 "x":[{"n":"Nina Ottosson puzzle","a":"Dog Brick · Dog Tornado","d":"Board puzzle with sliders, lids and spinning layers that hide treats, graded by difficulty.","mk":"Nina Ottosson","y":"","s":NO,
   "v":[v("Dog Smart","Nina Ottosson","","level 1"),v("Dog Brick","Nina Ottosson","","level 2"),v("Dog Tornado","Nina Ottosson","","level 2, stacked rotating layers"),v("Dog Casino","Nina Ottosson","","level 3"),v("Dog Twister","Nina Ottosson","","level 3"),v("MultiPuzzle","Nina Ottosson","","level 4")],
   "dt":"difficulty levels 1–4 · wood or plastic"},
  {"n":"LickiMat","a":"lick mat","d":"Flat rubber mat with a textured surface that is spread with soft food for a dog to lick off.","mk":"LickiMat","y":"","s":LM,
   "v":[v("LickiMat Classic Soother","LickiMat","","brush-nub surface for liquid foods"),v("LickiMat Buddy","LickiMat","","cross-maze surface for thick foods"),v("LickiMat Playdate","LickiMat","","box surface for chunky foods")],
   "dt":"about 20 × 20 cm · food-grade TPR · colours"}],
 "m":[["KONG Wobbler","Kong Company"],["Trixie Activity Sniffer Carpet","TRIXIE Heimtierbedarf"],["WOOF Pupsicle","WOOF"]],
 "r":[["KONG Squeezz","Kong Company"]]},
{"n":"Plush dog toys","a":"soft toys · squeaky toys","d":"Soft stuffed toys for dogs, often with squeakers.","s":"https://www.petsmart.com/dog/toys/plush-toys",
 "m":[["KONG Comfort Jumbo","Kong Company"],["KONG CuteSeas","Kong Company"],["KONG Wild Knots Bears","Kong Company"],["KONG Scrunch Knots Fox","Kong Company"],["TIAKI Squeaky Fox Dog Toy","TIAKI"]]},
{"n":"Dog rope and tug toys","a":"tug toys","d":"Rope, ring and woven toys for tugging games and chewing.","s":"https://www.petsmart.com/dog/toys/rope-and-tug-toys",
 "m":[["KONG Wubba","Kong Company"],["Goughnuts Tug Toy","Goughnuts"],["TIAKI Rope Ball Dog Toy","TIAKI"]]},
{"n":"Dog agility equipment","a":"agility obstacles · flyball","d":"Obstacles and gear for dog agility, flyball and home training courses.",
 "t":["competition grade","garden or indoor kit"],"s":"https://www.zooplus.co.uk/shop/dogs/agility_training/agility",
 "x":[ag("Agility jump","hurdle · bar jump","Bar between two uprights, height adjustable; also spread, panel, long and tyre jumps.",
        [v("Trixie Dog Agility Hurdle","TRIXIE Heimtierbedarf"),v("Trixie Dog Agility Hurdle Cone Set","TRIXIE Heimtierbedarf")],"single, spread, panel, long, tyre"),
      ag("A-frame","","Two ramps meeting in an inverted V, with painted contact zones.",[v("Galican A-frame","Galican")]),
      ag("Dog walk","","Raised plank with a ramp at each end and contact zones.",[v("Clip & Go Agility Dogwalk","Clip & Go Agility")]),
      ag("Agility seesaw","teeter","Pivoting plank that tips as the dog crosses it.",[v("Max 200 Adjustable See-saw","Max 200"),v("M.A.D. Agility Teeter Tote","M.A.D. Agility"),v("Clip & Go Agility Teeter","Clip & Go Agility"),v("Trixie Dog Agility Seesaw","TRIXIE Heimtierbedarf")]),
      ag("Weave poles","","Line of upright poles the dog zigzags through without missing one.",[v("Max 200 Weave Poles","Max 200"),v("M.A.D. Agility 12-colored Channel Weave Poles","M.A.D. Agility"),v("Mark's Agility Equipment 2x2 Weaves","Mark's Agility Equipment"),v("Cool Runners Agility Weave Poles","Cool Runners")],"6 or 12 poles · channel or 2x2 training sets"),
      ag("Agility tunnel","pipe tunnel","Flexible open tube the dog runs through; the closed chute is now rarely used.",[v("Max 200 Tunnels","Max 200"),v("Clip & Go Agility Tunnels","Clip & Go Agility"),v("HDP Dog Agility Training Tunnel","HDP")],"length · diameter"),
      ag("Pause table","","Raised platform where the dog holds a sit or down for a count.",[v("Max 200 Pause Table","Max 200"),v("M.A.D. Agility Pause Table","M.A.D. Agility")]),
      {"n":"Flyball box","a":"","d":"Spring-loaded box that launches a tennis ball when the dog presses its pad, used in flyball relay racing.","mk":"","y":"1970s","s":FB,
       "v":[v("first flyball box","","","credited to Herbert Wagner")],"dt":"pad angle · single or double ball hole"}],
 "m":[["Outward Hound Zip & Zoom Indoor Dog Agility Training Kit","Outward Hound"],["Outward Hound Zip & Zoom Outdoor Dog Agility Training Kit","Outward Hound"],["Better Sporting Dogs Deluxe Agility Equipment Set","Better Sporting Dogs"],["XiaZ Dog Agility Equipment","XiaZ"]]},
{"n":"Dog scent work kit","a":"nosework kit","d":"Set of target odours, cotton swabs, jars and vented tins for training a dog in scent-work sport.",
 "t":["birch","anise","clove","cypress"],"s":AK},
{"n":"Gundog training dummy","a":"retrieving dummy · canvas dummy · bumper","d":"A throwable object carrying the handler's scent, used to train gundogs to retrieve game.",
 "t":["canvas","foam bird-shaped","feather- or fur-wrapped"],"s":SU,
 "x":[{"n":"Canvas dummy","a":"","d":"Weighted canvas-covered tube with a throwing toggle, sized to match game.","mk":"","y":"1970s","s":SU,
   "v":[v("FLIGHT series","Sporting Saint","","bird-pattern 1 lb dummies")],"dt":"puppy, ½ lb, 1 lb, 2 lb, 3 lb, 6 lb · colours · long-throw toggle"},
  {"n":"Dokken Dead Fowl Trainer","a":"DeadFowl","d":"Life-size foam bird dummy with a free-swinging hard head and feet that discourage hard mouthing.","mk":"Dokken","y":"1995","s":DK,
   "v":[v("Dead Fowl Trainer, full size","Dokken","","waterfowl and upland species, dove the smallest"),v("Puppy Dead Fowl Trainer","Dokken","","about 8 in; mallard, dove, bobwhite quail")],"dt":"species · scentable foam"}]},
{"n":"Dog waste bags","a":"poop bags · poo bags","d":"A bag made for picking up and disposing of a dog's droppings.",
 "t":["bag","dispenser","poop scooper","compostable or plastic"],"s":"https://www.petsathome.com/category/dog",
 "m":[["Earth Rated dog waste bags","EARTH RATED"],["BioBag standard pet waste bags","BioBag"],["beyondGREEN compostable dog waste bags","beyondGREEN"],["Mutt Mitt dog waste pick up bag","Mutt Mitt"],["Pogi's poop bags with easy-tie handles","Pogi's"],["Greener Walker dog poop bags","Greener Walker"],["AmazonBasics dog waste bags","AmazonBasics"],["Downtown Pet Supply dog poop bags","Downtown Pet Supply"]]},
]
brands=[
{"n":"Kong Company","c":"United States","f":"1976","seg":"Dog and cat toys","d":"Maker of the KONG rubber toy, founded in Golden, Colorado by Joe Markham.","lines":["KONG Classic","Wubba"],"sig":["KONG Classic"],"rel":[],"s":KW},
{"n":"Nylabone","c":"United States","f":"","seg":"Dog chews","d":"Chew-toy brand that introduced the first nylon dog chew in 1955; part of Central Garden & Pet.","lines":["Puppy Chew","Flexi Chew","Strong Chew","Power Chew","Nutri Dent"],"sig":["Nylabone nylon chew bone"],"s":NY},
{"n":"West Paw","c":"United States","f":"","seg":"Dog toys","d":"Family-owned maker of recyclable Zogoflex toys in Bozeman, Montana.","lines":["Zogoflex"],"sig":["West Paw Hurley"],"s":WP},
{"n":"Chuckit!","c":"United States","f":"1998","seg":"Fetch toys","d":"Ball-launcher brand created by Canine Hardware of the Seattle area; owned by Petmate since 2012.","lines":["Ultra Ball","launchers"],"sig":["Chuckit! ball launcher"],"rel":["Petmate"],"s":CH},
{"n":"Wham-O","c":"United States","f":"","seg":"Toys","d":"Toy company that bought Fred Morrison's flying disc in 1957 and named it Frisbee.","sig":["Frisbee flying disc"],"s":FR},
{"n":"Hyperflite","c":"","f":"2000","seg":"Dog sport discs","d":"Dog-disc maker founded by canine disc world champions Peter Bloeme and Jeff Perry.","lines":["K-10","Jawz","SofFlite"],"sig":["Hyperflite competition dog disc"],"s":HY},
{"n":"Nina Ottosson","c":"Sweden","f":"","seg":"Pet puzzle toys","d":"Puzzle-toy line of designer Nina Ottosson, sold by Outward Hound.","sig":["Nina Ottosson puzzle"],"rel":["Outward Hound"],"s":NO},
{"n":"LickiMat","c":"Australia","f":"","seg":"Pet enrichment","d":"Lick-mat brand of Innovative Pet Products.","lines":["Classic","Tuff"],"sig":["LickiMat"],"s":"knowledge"},
{"n":"Dokken","c":"United States","f":"","seg":"Gundog training","d":"Training-dummy brand of trainer Tom Dokken of Dokken's Oakridge Kennels.","sig":["Dokken Dead Fowl Trainer"],"s":DK},
{"n":"Sporting Saint","c":"United Kingdom","f":"","seg":"Gundog training","d":"Herefordshire maker of canvas training dummies.","sig":["Canvas dummy"],"s":SS},
{"n":"EARTH RATED","c":"Canada","f":"2010","seg":"Pet waste bags","d":"Montreal maker of dog waste bags, known for lavender-scented bags in purple packaging.","s":ER},
]
notes=("Old 'Dog chew toys and other toys' dissolved: balls/flyers to fetch, plush, tug and puzzle items to their kinds. Agility generic entries (Agility bridge, hurdle, seesaw, tunnel, Balance trainer, Jump hoop, Weave poles) became obstacle archetypes. "
 "NEW kinds: Gundog training dummy, Dog scent work kit (AKC page). Waste bags trimmed from 11 to 8 (dropped Gorilla Supply, PET N PET, Pet Faves); dispenser and scooper are types. "
 "Left out: Lotus ball (no retrievable source page: AKC shop 404, desertcart 403); chew-toy years for KONG variants and the Chuckit! launch year are unconfirmed so left blank; LickiMat brand facts recorded from knowledge. Wikipedia gives agility's Crufts origin only as 'late 1970s'.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/B10/shelves/00_03.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
