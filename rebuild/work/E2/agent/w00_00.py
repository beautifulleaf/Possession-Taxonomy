import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def K(n,a,d,s,m=None,r=None,t=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    k["s"]=s
    if m: k["m"]=[list(x) for x in m]
    if r: k["r"]=[list(x) for x in r]
    return k
def B(n,c,f,seg,kf,d,s,lines=None,sig=None,rel=None):
    b={"n":n,"c":c}
    if f: b["f"]=f
    b.update({"seg":seg,"kf":kf,"d":d})
    if lines: b["lines"]=lines
    if sig: b["sig"]=sig
    if rel: b["rel"]=rel
    b["s"]=s; return b
NT="NordicTrack"; LF="Life Fitness"; TG="Technogym"; TR="TRUE Fitness"; PE="Peloton"; C2="Concept2"; SF="Schwinn Fitness"
C2U="https://en.wikipedia.org/wiki/Concept2"; PU="https://en.wikipedia.org/wiki/Peloton_Interactive"; SMU="https://en.wikipedia.org/wiki/StairMaster"
kinds=[
 K("Treadmill","running machine · walking pad","Machine with a moving belt for walking or running in place; the belt is motorised or driven by the user.","https://www.fitshop.co.uk/nordictrack-treadmills",
   [("Commercial 1750",NT),("Commercial 2450",NT),("T Series 10",NT),("X24",NT),("Tread",PE),("Tread+",PE),("F63","Sole Fitness"),("Pro 2000","ProForm"),("Treadmill 10","Bowflex"),("T101","Horizon Fitness")],
   [("Commercial",NT),("T Series",NT)],["motorised","manual/curved","folding","walking pad","incline trainer"]),
 K("Spin bike","indoor cycling bike","Stationary bike with a heavy flywheel and a road-bike riding position that allows riding out of the saddle.","https://www.northernfitness.ca/collections/indoor-cycles",
   [("Bike+",PE),("Bike",PE),("M3i Indoor Bike","Keiser"),("IC4",SF),("S24 Bike",NT),("S22i",NT),("Ride Indoor Cycle",TG),("Group Cycle Connect",TG),("C6 Bike","Bowflex"),("EX-8s","Echelon"),("Myx II","MyxFitness"),("Bike Indoor Cycle","NOHrD")],
   [("M3i","Keiser")],["magnetic","friction","connected/streaming"]),
 K("Upright exercise bike","exercise bike","Stationary pedal machine with an upright seat and handlebar, the standard exercise bike.","https://www.marcypro.com/collections/cardio-upright-bikes",
   [("C1 LifeCycle",LF),("C3 LifeCycle",LF),("Bike Personal",TG),("Cycle Upright Bike",TG),("G LE Upright Bike",NT),("Performance Series Upright Bike",TR),("Magnetic Upright Exercise Bike NS-40504U","Marcy Pro")],
   [("LifeCycle",LF),("Performance Series",TR)],["magnetic","friction","folding"]),
 K("Recumbent exercise bike","","Stationary bike with a backrest seat and the pedals set forward.","https://www.northernfitness.ca/collections/recumbent-bikes",
   [("RS1 LifeCycle Recumbent",LF),("RS3 LifeCycle Recumbent",LF),("Recline Personal",TG),("10 Recumbent Bike",NT),("G LE Recumbent Bike",NT),("Performance Series Recumbent Bike",TR)],
   [("LifeCycle",LF),("Performance Series",TR)],["magnetic","folding"]),
 K("Air bike","fan bike · assault bike","Stationary bike whose fan gives the resistance, usually with handles that move with the pedals.","https://www.northernfitness.ca/collections/air-bikes",
   [("Echo Bike","Rogue Fitness"),("AirBike Classic","Assault Fitness"),("Airdyne AD7",SF),("BikeErg",C2),("Fan Bike","Titan Fitness"),("Blitz Air Bike 2.0","Bells of Steel"),("Raptor Air Bike","Fringe Sport")],
   None,["chain drive","belt drive","with moving arms","without arms"]),
 K("Rowing machine","rower · indoor rower · ergometer","Stationary machine that simulates rowing with a sliding seat and a resisted pull handle.","https://www.delta-fitness.com/products/concept-2-rowerg-with-standard-legs",
   [("RowErg",C2),("Dynamic RowErg",C2),("M1 HiRise","WaterRower"),("Wave","Hydrow"),("Rower","Hydrow"),("Row",PE),("Ergatta Rower","Ergatta"),("Echo Rower","Rogue Fitness"),("AssaultRower Pro","Assault Fitness"),("RW900",NT),("Pro R10","ProForm"),("Row-S","Echelon")],
   None,["air","water","magnetic","hydraulic","connected/streaming"]),
 K("Elliptical cross trainer","elliptical · cross trainer","Standing cardio machine with foot pedals on an elliptical path and moving arm handles.","https://fitshop.de/en/horizon-fitness",
   [("X16 Elliptical",NT),("E25","Sole Fitness"),("Max Trainer M6","Bowflex"),("Andes 7.1","Horizon Fitness")],
   None,["front drive","rear drive","centre drive","stepper hybrid"]),
 K("Recumbent cross trainer","recumbent stepper","Seated machine with a backrest whose pedals step back and forth, linked to moving arm handles.","https://www.northernfitness.ca/collections/recumbent-bikes",
   [("FreeStep LT1 Recumbent Step Bike","Teeter")]),
 K("Stair climber","stepmill · stair-mill · stepper · StairMaster","Machine for climbing in place, either on a revolving staircase or on two independent pedals.",SMU,
   [("StepMill 5 (SM5)","StairMaster"),("StepMill 3 (SM3)","StairMaster"),("StairClimber 5 (SC5)","StairMaster"),("Gauntlet","StairMaster")],
   None,["revolving staircase (stepmill)","independent pedals (stepper)"]),
 K("Ski ergometer","ski erg","Standing machine with two pull handles on a flywheel that simulates the double-pole action of cross-country skiing.",C2U,
   [("SkiErg",C2)]),
]
K_=lambda: None
brands=[
 B("Concept2","United States","1976","Specialist","rowing ergometers","Vermont maker of air-resistance rowing, ski and bike ergometers and racing oars; its RowErg is the standard indoor rower.",C2U,
   ["RowErg","SkiErg","BikeErg"],["RowErg (Model D, 2003)","SkiErg (2009)","BikeErg (2017)"]),
 B("Peloton","United States","2012","Premium","connected fitness","New York maker of streaming-connected exercise bikes, treadmills and rowers sold with class subscriptions.",PU,
   ["Bike","Bike+","Tread","Tread+","Row"],["Peloton Bike (2014)"],["Hydrow","Echelon"]),
 B("StairMaster","United States","1983","Professional & flagship","stair climbers","Tulsa-founded maker of stepmills and stair climbers whose name became a generic word for the machine; now part of Core Health & Fitness.",SMU,
   ["StepMill","StairClimber"],["StepMill"]),
 B(NT,"United States","1975","Mainstream","treadmills","Home cardio brand of iFIT, best known for treadmills, ellipticals and connected bikes.","knowledge",["Commercial","T Series","X Series"],None,["ProForm"]),
 B(LF,"United States","1977","Professional & flagship","gym cardio","Commercial and home gym equipment maker known for the Lifecycle exercise bike.","knowledge",["Lifecycle"]),
 B(TG,"Italy","1983","Professional & flagship","gym equipment","Italian maker of commercial and design-led home fitness equipment.","knowledge",["Personal","Skillrun"]),
 B("WaterRower","United States","1988","Specialist","water rowers","Maker of wooden-framed rowing machines that use a water flywheel.","knowledge"),
 B("Keiser","United States","1978","Specialist","magnetic spin bikes","Fresno maker of air-pneumatic strength machines and the M-series magnetic indoor bikes.","knowledge",["M3i"]),
 B(SF,"United States","","Mainstream","Airdyne","Fitness arm of the Schwinn name, known for the Airdyne fan bike and IC indoor bikes.","knowledge",["Airdyne","IC"]),
 B("Rogue Fitness","United States","2006","Premium","barbells, racks","Ohio maker of barbells, racks and conditioning equipment including the Echo bike and rower.","knowledge",["Echo"]),
 B("Assault Fitness","United States","","Specialist","air bikes","Maker of fan-resistance air bikes, rowers and curved manual treadmills.","knowledge",["AirBike","AssaultRunner"]),
 B("Hydrow","United States","2017","Premium","connected rowers","Maker of streaming-connected rowing machines with filmed on-water classes.","knowledge"),
 B("Bowflex","United States","1986","Mainstream","home gym","Home fitness brand known for its rod home gyms, adjustable dumbbells and Max Trainer.","knowledge",["Max Trainer"]),
]
w('00_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Tier shelf. Kept all 8 old kinds; added Stair climber (StairMaster wiki) and Ski ergometer (Concept2 wiki, for the SkiErg). Trimmed TRUE (Apex/Gravity/Launch) and Marcy Pro SKU runs, NordicTrack treadmill list from 13 to 4 plus test winners (reviewed.com: Commercial 1750 best, Sole F63 value), dropped Aviron Fit Bike, Yesoul S3, Keiser M3i Studio Plus, NordicTrack X24 Bike. Added test winners from reviewed.com (treadmills, bikes, rowers), Fortune (ellipticals), Garage Gym Reviews (air bikes: Rogue Echo best) and Frontdeskreview (Assault vs Airdyne). Drive/resistance types moved into t. Technogym and Life Fitness ellipticals and manual curved treadmills (Woodway, AssaultRunner) not added: no fetched page named the models."})
