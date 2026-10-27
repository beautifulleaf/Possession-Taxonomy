exec(open('/home/user/Possession-Taxonomy/rebuild/work/E2/agent/w00_00.py').read().split('NT="NordicTrack"')[0])
MA="Manduka"; BB="Balanced Body"
kinds=[
 K("Yoga mat","exercise mat","Thin, non-slip mat made for yoga and floor exercise.","https://www.outdoorgearlab.com/catalog/yoga-mat",
   [("PRO",MA),("GRP Adapt",MA),("Liforme Original","Liforme"),("The Mat","Lululemon Athletica"),("Harmony","Jade Yoga"),("Fusion","Jade Yoga"),("Premium Sticky","Gaiam"),("Performance Cork","Gaiam"),("Earth Elements","Hugger Mugger"),("B Mat Everyday","B Yoga"),("Unity Cork","Yoloha"),("E.C.O.","prAna")],
   None,["PVC","natural rubber","TPE","cork","travel/foldable","hot-yoga"]),
 K("Yoga block","yoga brick · yoga props","Firm block used in yoga to support or extend reach; sold with straps and bolsters as props.","https://outdoorgearlab.com/topics/fitness/best-yoga-blocks",
   [("Cork",MA),("unBLOK",MA),("Cork","Jade Yoga"),("Yoga Essentials Block","Gaiam"),("Inner Flow","Lululemon Athletica"),("Bamboo","Hugger Mugger"),("StrongBlocks","BaseBlocks")],
   None,["foam","cork","bamboo/wood","wedge","yoga strap","bolster"]),
 K("Foam roller","massage roller","Cylinder of firm foam rolled under the body for self-massage.","https://en.wikipedia.org/wiki/Foam_roller",
   [("GRID","TriggerPoint"),("High-Density Round Foam Roller","Amazon Basics"),("Pro-Roller Soft-Density","OPTP"),("Textured Foam Roller","RumbleRoller"),("Wave Roller","Therabody")],
   None,["smooth","textured","vibrating","soft","firm"]),
 K("Exercise ball","Swiss ball · stability ball · gym ball · birth ball","Large inflatable ball, 35 to 95 cm across, used for balance, core and rehab exercise.","https://en.wikipedia.org/wiki/Exercise_ball",
   None,None,["35–95 cm sizes","anti-burst"]),
 K("Pilates reformer","reformer · Universal Reformer","Sliding carriage on a frame with springs, footbar and straps, devised by Joseph Pilates; home models fold or stack.","https://en.wikipedia.org/wiki/Pilates",
   [("Allegro 2",BB),("CenterLine",BB),("Allegro Stretch",BB),("At Home SPX","Merrithew"),("AeroPilates Premier","Stamina"),("Smart Reformer","Flexia")],
   None,["studio","home/foldable","cord-resistance"]),
 K("Skipping rope","jump rope","Rope with handles turned and jumped over in training.","https://shop.app/products/8619220173038/aero-speed-2-0",
   [("Aero Speed 2.0","Buddy Lee Jump Ropes")],None,["speed","weighted","beaded","PVC"]),
 K("Fitness trampoline","rebounder · mini trampoline","Small trampoline (rebounder) with a frame of about 1.2 m or less, sold for exercise. A garden or play trampoline is in Toys & Games.","https://www.bestbuy.ca/en-ca/product/jumpsport-220-fitness-rebounder-mini-trampoline-handle-bar-accessory-black/18193032",
   [("220 Fitness Rebounder","JumpSport"),("350","JumpSport"),("Bungee Rebounder","bellicon"),("Soft-Bounce","Needak"),("Exercise Trampoline 40in","Forza (Decathlon)")],
   None,["bungee","steel spring","folding","with handlebar"]),
 K("Balance board","wobble board · rocker board · rola bola","Board on a pivot, roller or ball that the user balances on for training or rehab.","https://en.wikipedia.org/wiki/Balance_board",
   None,None,["rocker","rocker-roller (rola bola)","wobble","sphere-and-ring"]),
]
brands=[
 B(MA,"United States","1997","Premium","yoga mats","Yoga mat and prop maker best known for the dense PRO mat.","knowledge",["PRO","GRP"]),
 B("Liforme","United Kingdom","","Premium","alignment yoga mats","Maker of grippy yoga mats printed with alignment markers.","knowledge"),
 B("Lululemon Athletica","Canada","1998","Premium","yoga wear","Vancouver athletic-wear brand that also sells mats and props.","knowledge"),
 B("Jade Yoga","United States","","Specialist","natural rubber mats","Maker of natural-rubber yoga mats.","knowledge",["Harmony","Fusion"]),
 B("TriggerPoint","United States","","Specialist","foam rollers","Maker of the GRID foam roller and other self-massage tools.","knowledge",["GRID"]),
 B(BB,"United States","","Professional & flagship","Pilates reformers","Sacramento maker of studio and home Pilates apparatus.","knowledge",["Allegro","CenterLine"]),
 B("Merrithew","Canada","","Professional & flagship","Pilates equipment","Toronto Pilates equipment and training company behind STOTT Pilates.","knowledge",["SPX"]),
 B("JumpSport","United States","","Specialist","rebounders","Maker of bungee-suspended fitness rebounders.","knowledge"),
 B("bellicon","Germany","","Premium","bungee rebounders","German maker of bungee-cord mini trampolines.","knowledge"),
]
w('00_02',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Tier/QoL shelf. Kept Yoga mat, Skipping rope, Fitness trampoline with old sources; yoga mats cut from 16 to 12 (dropped Gaiam Foldable, GuruGrid, Kulae, prAna Revolution). Added Yoga block (OutdoorGearLab test), Foam roller, Exercise ball, Pilates reformer, Balance board (Wikipedia). Models from OutdoorGearLab blocks, CNN Underscored foam rollers, NBC Select reformers, a rebounder comparison page. Exercise ball and balance board left without models: no fetched page named makers."})
