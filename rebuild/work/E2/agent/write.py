import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def K(n,a,d,s,m=None,r=None,t=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    k["s"]=s
    if m: k["m"]=[list(x) for x in m]
    if r: k["r"]=[list(x) for x in r]
    return k
BH="Bauer Hockey"; CC="CCM Hockey"; WH="Warrior Hockey"; TH="TRUE Hockey"
w('E2','04_05',{"kinds":[
 K("Hockey helmet","","Hard-shell helmet with chin strap made for ice hockey; sold alone or as a combo with a cage.","https://www.hockeymonkey.com/ice-hockey/helmets.html",
   [("RE-AKT 155",BH),("RE-AKT 90",BH),("RE-AKT 55",BH),("Hyperlite 2",BH),("Super Tacks X",CC),("Tacks X Pro",CC),("Tacks 720",CC),("Tacks 310",CC),("CF 80",WH)],
   [("RE-AKT",BH),("Tacks",CC)],["helmet only","helmet and cage combo"]),
 K("Hockey cage or visor","","Face cage or clear shield that clips to a hockey helmet.","https://www.hockeymonkey.com/ice-hockey/helmets.html",[("FM580",CC),("Straight Small Visor","Oakley")],None,["cage","visor"]),
 K("Hockey gloves","","Padded glove with a segmented cuff made for skaters in ice hockey.","https://www.purehockey.com/c/hockey-protective-gloves",
   [("Jetspeed FT8 Pro",CC),("Jetspeed FTW",CC)],[("Vapor",BH),("Supreme",BH),("Nexus",BH),("Jetspeed",CC),("Covert",WH)]),
 K("Hockey shoulder pads","","Padded shoulder, chest and upper-arm protector worn under the jersey in ice hockey.","https://www.purehockey.com/c/hockey-protective-shoulder-pads",
   None,[("Vapor",BH),("Supreme",BH),("Jetspeed",CC),("Tacks",CC),("Alpha",WH)]),
 K("Hockey elbow pads","","Padded elbow and forearm guard worn in ice hockey.","https://www.purehockey.com/c/hockey-protective-elbow-pads"),
 K("Hockey pants","hockey girdle · pant shell","Padded pants or girdle with shell worn over the hips and thighs in ice hockey.","https://www.purehockey.com/c/hockey-protective-pants-senior",
   [("Bauer S21 Pant Shell",BH),("CCM JetSpeed Girdle Shell",CC),("CCM PP25 Pant Shell",CC)],
   [("Vapor",BH),("Supreme",BH),("Jetspeed",CC),("Tacks",CC),("Alpha",WH),("Covert",WH),("Catalyst",TH)],["hockey pants","girdle","removable pant shell"]),
 K("Hockey neck guard","","Cut-resistant collar or bib worn round the neck against skate blades in ice hockey.","https://www.icewarehouse.com/Sherwood_Neck_Guards/catpage-SWDNECKGRD.html",
   [("Sherwood Cut Protective Neck Guard Collar","Sherwood Hockey"),("Sherwood Cut Protective Neck Guard Bib","Sherwood Hockey"),("Sherwood Cut Protective Neck Guard Pro","Sherwood Hockey")],None,["collar","bib"])],
 "brands":[],"traditions":[],"notes":"Merged Hockey pant shell into Hockey pants (shell and girdle as types; shell models kept). Helmet cut from 13 to 9 (dropped RE-AKT 70, Super Tacks 210, Tacks 70, Tacks 920). Gloves dropped Jetspeed FT880 (covered by the Jetspeed range). Other kinds unchanged; no new models."})
w('E2','04_06',{"kinds":[
 K("Goalie mask","","Face mask or helmet-cage worn by the goalie in ice hockey.","https://goalie.purehockey.com/c/goalie-masks"),
 K("Goalie leg pads","","Pair of large rigid-faced pads strapped over the goalie shins and knees in ice hockey.","https://goalie.purehockey.com/c/goalie-leg-pads",
   [("S Series","Brian's"),("HZRDUS 9X4",TH)],[("HZRDUS",TH),("Catalyst",TH)]),
 K("Goalie blocker","","Rectangular pad on the goalie stick hand, used to deflect shots and hold the stick.","https://goalie.purehockey.com/c/goalie-blockers"),
 K("Goalie catcher","","Large pocketed glove on the goalie non-stick hand, made to catch the puck.","https://goalie.purehockey.com/c/goalie-catch-gloves"),
 K("Goalie chest and arm protector","","Padded chest, shoulder and arm protector worn by the goalie in ice hockey.","https://goaliemonkey.com/equipment/chest-arm.html",
   [("Bauer Supreme Fuse Goalie Chest & Arm Protector",BH),("Bauer Vapor FlyLite Goalie Chest & Arm Protector",BH),("CCM Pro Spec Chest & Arm Protector",CC),("Vaughn Velocity XP Pro Goalie Chest & Arm Protector","Vaughn"),("Vaughn Ion Pro Select Goalie Chest & Arm Protector","Vaughn"),("Warrior Ritual X5 Pro Goalie Chest & Arm Protector",WH)]),
 K("Goalie pants","","Padded pants with thigh and hip protection cut for the goalie in ice hockey.","https://goalie.purehockey.com/product/bauer-pro-goalie-pants-senior/itm/70032-41/",[("Bauer Pro Goalie Pants",BH)])],
 "brands":[],"traditions":[],"notes":"All six kinds kept. Chest and arm protector cut from 7 to 6 (dropped Warrior Ritual X4 Pro+, superseded by the X5 Pro). No mask makers added (none in old data)."})
w('E4','03_00',{"kinds":[
 K("Centrefire handgun cartridge","","Complete cartridge with a central primer made for handguns.","https://www.sportsmans.com/shooting-gear-gun-supplies/ammunition-ammo-for-hunting-shooting-sports/c/cat100112",
   [("9mm Luger",""),(".45 ACP",""),(".380 ACP",""),(".40 S&W",""),(".38 Special",""),(".357 Magnum",""),("10mm Auto",""),(".44 Magnum","")]),
 K("Centrefire rifle cartridge","","Complete cartridge with a central primer made for rifles.","https://www.sportsmans.com/shooting-gear-gun-supplies/ammunition-ammo-for-hunting-shooting-sports/c/cat100112",
   [(".223 Remington",""),("5.56x45mm NATO",""),(".308 Winchester",""),(".30-06 Springfield",""),("6.5 Creedmoor",""),(".270 Winchester",""),(".300 Winchester Magnum",""),(".300 AAC Blackout","")]),
 K("Rimfire cartridge","","Complete cartridge whose priming compound sits in the rim.","https://www.sportsmans.com/shooting-gear-gun-supplies/ammunition-ammo-for-hunting-shooting-sports/c/cat100112",
   [(".22 Long Rifle",""),(".22 WMR",""),(".17 HMR","")]),
 K("Shotshell","shotgun shell · birdshot · buckshot · slug shells","Cartridge for a shotgun loaded with shot or a single slug.","https://www.sportsmans.com/shooting-gear-gun-supplies/ammunition-ammo-for-hunting-shooting-sports/c/cat100112",
   [("12 gauge shotshell",""),("20 gauge shotshell",""),(".410 bore shotshell",""),("16 gauge shotshell",""),("28 gauge shotshell",""),("10 gauge shotshell","")],None,["birdshot","buckshot","slug"])],
 "brands":[],"traditions":[],"notes":"Merged Other shotshells, Birdshot shells, Buckshot shells and Shotgun slugs into Shotshell (load as types, gauges as the list; kept the Other shotshells source). Calibre lists kept as they were (short lists of common standard cartridges), reordered by commonness."})
w('E4','04_01',{"kinds":[
 K("Magazine","","Detachable or fixed container that feeds cartridges into a firearm.","https://www.eurooptic.com/Magpul-Magazines.aspx",
   [("PMAG Gen M3","Magpul"),("PMAG LR/SR Gen M3","Magpul"),("PMAG AK MOE","Magpul"),("PMAG GL9","Magpul"),("PMAG EV9","Magpul")],[("PMAG","Magpul")],["rifle","pistol","drum"]),
 K("Barrel","","Replacement or upgrade barrel made to fit a firearm model or platform.","https://www.basspro.com/l/guns"),
 K("Trigger","","Drop-in trigger or trigger group made to fit a firearm model or platform.","https://www.basspro.com/l/guns"),
 K("Iron sight","","Fixed or adjustable open or aperture sight fitted to a firearm, sold as front, rear or set.","https://www.basspro.com/l/guns",None,None,["front","rear","set"]),
 K("Suppressor","","Device fitted to a firearm muzzle that reduces the sound of a shot; its legal class varies by place.","https://www.basspro.com/l/guns")],
 "brands":[],"traditions":[],"notes":"All five kinds kept at platform level. Magazine cut from 7 Magpul models to 5 (dropped PMAG MOE, superseded by Gen M3, and PMAG D-60 drum). No OEM magazine models added (none in old data)."})
w('E4','08_00',{"kinds":[
 K("Pepper spray","pepper gel · OC spray","Defensive OC spray, in a liquid stream or a thicker gel.","",
   [("SABRE Pepper Spray with Quick Release Keychain","SABRE"),("SABRE Red MK-9 Gel","SABRE")],[("SABRE Red","SABRE")],["spray","gel"]),
 K("Taser-type stun gun","projectile electroshock weapon · TASER","Device that fires wired darts to deliver an incapacitating electric shock; Taser is the best-known brand.","https://taser.com/pages/pulse-series",
   [("TASER Pulse 2","TASER"),("TASER Bolt 2","TASER"),("TASER 7 CQ","TASER")]),
 K("Contact stun gun","","Hand-held device that delivers an electric shock through electrodes pressed against the body.","https://www.pyramydair.com/product/guard-dog-dual-led-grip-to-stun-gun-rechargeable-black?a=38393",
   [("TASER StrikeLight 2","TASER"),("Guard Dog Dual LED Grip-to-Stun","Guard Dog Security")]),
 K("Pepper-ball launcher","CO2 launcher","Launcher that fires frangible projectiles filled with an irritant powder.","https://www.blackovis.com/byrna-hd-xl-pepper-self-defense-weapon-kit-2020",
   [("Byrna SD","Byrna Technologies"),("Byrna HD XL","Byrna Technologies")]),
 K("Baton","","Rigid or telescoping club made for striking.","https://www.nafeco.com/products/asp-baton-26-expandable-foam-friction-locblack-chrome/52611",None,[("Friction Loc","ASP")],["telescoping","fixed"]),
 K("Kubotan","","Short rod held in the fist to strike or apply pressure.","https://www.bladehq.com/item--Cold-Steel-Delta-Dart-8-Kubaton--44304",[("Delta Dart","Cold Steel")]),
 K("Sword cane","shikomizue","Walking stick whose shaft hides a sword blade drawn from it. A cane without a blade is in Bags & Accessories or Health, Medical & Mobility.","https://www.kultofathena.com/product-category/swords/asian-swords/japanese-swords/")],
 "brands":[],"traditions":[],"notes":"All seven kinds kept. Pepper spray: formula (spray/gel) as types; old kind had no source and none was added (no web research on this shelf). Taser-type stun gun dropped TASER X1 (police model, scope rule). Sword cane's placeholder model 'Sword cane' removed. No new models."})
w('E4','09_01',{"kinds":[
 K("Soft ballistic vest","","Flexible body armour against handgun rounds.","https://pointblankenterprises.com/point-blank-body-armor/hi-lite-male.html",[("Hi-Lite","Point Blank Enterprises")],None,["NIJ Level IIA","NIJ Level II","NIJ Level IIIA"]),
 K("Hard ballistic plate","","Rigid armour plate against rifle rounds, worn alone or in a carrier.","https://www.police1.com/police-products/body-armor/press-releases/spartan-armor-systems-introduce-hercules-level-iv-ceramic-body-armor-Ehih1MxexnqeM1KM/",[("Hercules","Spartan Armor Systems")],None,["NIJ Level III","NIJ Level IV","steel","ceramic","polyethylene"]),
 K("Plate carrier","","Vest made to hold hard armour plates; it counts as armour in its own right.","https://www.atomicdefense.com/collections/bulletproof-plate-carriers/spo-default"),
 K("Stab-resistant vest","","Body armour made against knife and spike attacks (NIJ 0115.00 standard).","https://www.officer.com/on-the-street/body-armor-protection/product/10052826/chief-protech-corrections-persuader-stab-vest",[("Persuader Stab Vest","Protech Corrections")]),
 K("Ballistic helmet","","Helmet made against bullets and fragments; sold by protection level.","https://www.atomicdefense.com/collections/ops-core-helmets",
   [("Ops-Core FAST SF","Ops-Core"),("Ops-Core FAST XP","Ops-Core"),("Ops-Core FAST RF1","Ops-Core")],[("FAST","Ops-Core")],["NIJ Level IIIA","rifle-rated"])],
 "brands":[],"traditions":[],"notes":"All five kinds kept; NIJ protection levels and plate materials as types. Ballistic helmet cut from 5 to 3 Ops-Core models (dropped FAST XR and TBH). No new makers added."})
