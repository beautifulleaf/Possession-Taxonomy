import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
exec(open('/home/user/Possession-Taxonomy/rebuild/work/E2/agent/w00_00.py').read().split('NT="NordicTrack"')[0])
RG="Rogue Fitness"; REP="REP Fitness"; TI="Titan Fitness"; BOS="Bells of Steel"; FR="Fringe Sport"
SW="https://en.wikipedia.org/wiki/Suspension_training"
kinds=[
 K("Barbell","weight bar · Olympic bar","Long steel bar with sleeves that carry weight plates, lifted with both hands.","https://www.roguefitness.com/eu/weightlifting-bars-plates/barbells/stainless-steel-barbells",
   [("Ohio Bar",RG),("Colorado Bar",REP),("Ohio Power Bar",RG),("Olympic WL Bar",RG),("Pyrros Bar",RG),("IWF Weightlifting Competition Bar","Eleiko"),("Olympic Weightlifting Barbell 2.0",BOS),("Wonder Bar V2",FR),("Safety Squat Olympic Bar V2",TI),("Home Gym Barbell","Major Fitness")],
   None,["Olympic (multipurpose)","power bar","weightlifting bar","women's bar","EZ curl","trap/hex","safety squat bar"]),
 K("Weight plate","barbell plate · bumper plate","Disc weight with a centre hole loaded onto a barbell or dumbbell handle.","https://en.wikipedia.org/wiki/Weight_plate",
   [("Echo Bumper Plates",RG),("Competition Plates",RG),("Calibrated Steel Plates",RG),("Color Bumper Plates",FR),("Cast Iron Plates","Strength Co."),("Urethane Plates","American Barbell"),("Alpha Bumpers","Vulcan Strength"),("Urethane Equalizers",REP),("Olympic Grip Plates","CAP Barbell")],
   None,["bumper","cast iron","urethane","calibrated steel","change plates","standard (1 in)","Olympic (2 in)"]),
 K("Dumbbell","hand weight · adjustable dumbbell","Short bar with a weight at each end, lifted in one hand; fixed or adjustable.","https://en.wikipedia.org/wiki/Dumbbell",
   [("SelectTech 552","Bowflex"),("Pro EXP 50","PowerBlock"),("Adjustable Dumbbell Set","Core Home Fitness"),("Select-A-Weight 50 lb","Weider"),("Select-A-Weight 55 lb","NordicTrack"),("Quick-Lock","Ironmaster")],
   None,["fixed (hex, round)","adjustable dial","adjustable selector block","plate-loaded"]),
 K("Kettlebell","","Cast or steel weight shaped as a ball with a handle, swung and lifted in training.","https://www.roguefitness.com/be/en/rogue-competition-kettlebells",
   [("Competition Kettlebell",RG),("Competition Kettlebell","Kettlebell Kings"),("Adjustable Competition Kettlebell","Kettlebell Kings")],
   None,["cast iron","competition steel","adjustable"]),
 K("Power rack","power cage · squat rack · squat cage","Frame of steel uprights with adjustable bar catches that acts as a spotter for barbell lifts.","https://en.wikipedia.org/wiki/Power_rack",
   [("PR-5000",REP),("PR-1100",REP),("HR-2 Half Rack",RG),("T-3 Series Folding Power Rack",TI),("Hydra Rack",BOS),("Profile Pro Elite","PRx Performance"),("Garage Squat Cage",FR),("G20 Pro All-in-One Trainer","Force USA")],
   None,["full rack","half rack","squat stand","wall-mounted folding","all-in-one with cables"]),
 K("Weight bench","gym bench · FID bench","Padded bench for lying or sitting on during lifts, flat or adjustable.","https://fitnessvolt.com/weight-benches-reviewed/",
   [("AB-5200 2.0",REP),("Nighthawk Adjustable Bench",REP),("Adjustable Bench 3.0",RG),("Flat Utility Bench 2.0",RG),("Series Adjustable Bench",TI),("Super Bench Pro V2","Ironmaster"),("Pro Series FID Bench","Force USA"),("1000 Super Max","Fitness Reality")],
   None,["flat","adjustable (FID)","folding"]),
 K("Home multi-gym","home gym · cable machine · functional trainer","Home machine giving many exercises from cables, a weight stack or a motor; includes connected strength trainers.","https://barbend.com/best-cable-machines",
   [("Tonal 2","Tonal"),("Gym Monster","Speediance"),("Ares 2.0",REP),("Functional Trainer",TI),("G12 All-in-One Trainer","Force USA"),("F22","Major Fitness"),("Voltra I","Beyond Power"),("SmartConnect","MaxPRO")],
   None,["weight-stack","plate-loaded","functional trainer","connected/digital resistance","portable"]),
 K("Pull-up bar","chin-up bar","Bar fixed in a doorway, on a wall or on a stand for pull-ups and hanging.","https://www.garagegymreviews.com/best-pull-up-bar",
   [("Mounted Multi-Grip Pull-Up Bar",REP),("Jammer Pull-Up Bar",RG),("Wall-Mounted Pull-Up Bar",TI),("The Big Bar","BaseBlocks")],
   None,["doorway","wall-mounted","ceiling-mounted","freestanding"]),
 K("Gymnastic rings","","Pair of rings hung on straps for gymnastic and bodyweight training.","https://www.roguefitness.com/eu/rogue-wood-rings",
   [("Gymnastic Wood Rings",RG)],None,["wood","plastic"]),
 K("Resistance band","exercise band · loop band · therapy band","Elastic band or tube stretched against its own tension for strength and rehab exercises.","https://en.wikipedia.org/wiki/Resistance_band",
   None,None,["loop","tube with handles","therapy band (flat)","figure-8","mini band"]),
 K("Suspension trainer","TRX · suspension straps","Pair of adjustable straps with handles hung from an anchor, used for bodyweight exercises.",SW),
]
kinds[-1]["x"]=[{"n":"TRX Suspension Trainer","a":"TRX · Total Resistance eXercise","d":"Single-anchor strap system developed by former Navy SEAL Randy Hetrick; the original suspension trainer.","mk":"TRX","y":"2005","s":SW,"v":[],"dt":"strap length · anchor type"}]
brands=[
 B("Eleiko","Sweden","1957","Professional & flagship","competition barbells","Swedish maker of IWF and IPF competition barbells and plates.","knowledge",["IWF","XF"]),
 B(REP,"United States","","Mainstream","racks, benches","Colorado home-gym maker of racks, benches, barbells and cable machines.","knowledge",["PR","AB","Ares"],None,[RG,TI]),
 B(TI,"United States","","Value","budget racks","Low-price home-gym brand of racks, bars and conditioning machines.","knowledge",["T-3"],None,[RG]),
 B("PowerBlock","United States","","Specialist","adjustable dumbbells","Maker of selector-pin block adjustable dumbbells.","knowledge",["Pro EXP","Elite"]),
 B("Tonal","United States","2015","Premium","connected strength","Maker of wall-mounted digital-resistance cable trainers with streamed coaching.","knowledge"),
 B("Kettlebell Kings","United States","","Specialist","competition kettlebells","Kettlebell maker known for steel competition bells.","knowledge"),
 B("TRX","United States","2005","Specialist","suspension trainers","Brand of suspension straps developed by Randy Hetrick; holds the term suspension training as a trademark via Fitness Anywhere.",SW),
]
w('00_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Tier shelf. Renamed Weight bar to Barbell (bar types into t); kept Kettlebell and Gymnastic rings with their old Rogue sources. Added 8 new kinds sourced from Wikipedia (Weight plate, Dumbbell, Power rack, Resistance band, Suspension trainer) and test roundups (Fitness Volt benches, BarBend cable machines, Garage Gym Reviews pull-up bars). Models are test winners from GGR barbells, Garage Gym Lab plates, Reviewed dumbbells (Bowflex SelectTech 552 kept but recalled June 2025), BarBend racks, PowerliftingTechnique kettlebells, GGR smart gyms. Life Fitness multi-gyms and Eleiko plates not added: no fetched page named the models. Rogue Fitness and Bowflex register entries are in shelf 00_00."})
