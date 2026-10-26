import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,a='',mk='',y='',v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=a1,mk=b,y=c,d=e) for a1,b,c,e in v],"dt":dt}
OLD='https://www.smartpakequine.com/horse-tack-supplies-and-equipment-687pc'
kinds=[
 {"n":"Headcollar","a":"halter","d":"Headgear without a bit used to lead, tie up or hold a horse.",
  "t":["flat nylon webbing","leather","rope","padded","adjustable chin and crown","throat snap","foal / pony / cob / full / draft / miniature sizes","grooming halter (no jaw ring)"],"s":OLD,
  "x":[
   X("Working headcollar","Everyday flat headcollar in nylon webbing or leather with a jaw ring for the lead and two side rings.",W+"Halter",a="stable headcollar · nylon halter · leather halter",
     v=[("Original Nylon Halter","Weaver Leather","",""),("Poly Nylon Adjustable Halter with Throat Snap","Country Pride","",""),("British Style Leather Halter","Walsh","",""),("British Style Premium Leather Halter","Quiet Creek","",""),("Premium Leather Halter with Double Adjustable Crown","Quiet Creek","",""),("Fairfield Leather Halter","Country Pride","","")],
     dt="nylon or leather · brass, nickel or stainless fittings · plain or padded · colours"),
   X("Rope halter","Halter knotted from one piece of rope with no metal parts, tied with a knot instead of a buckle; associated with western and natural horsemanship.",W+"Halter",a="cowboy halter · knotted halter · natural-horsemanship halter",
     v=[("Silvertip Four Knot Rope Halter","Weaver Leather","","four knots on the noseband"),("Harmony Rope Halter","Woof Wear","",""),("Poly Rope Miniature Horse Halter","Tough 1","","miniature size")],
     dt="rope diameter and stiffness · number of noseband knots · integrated lead"),
   X("Show halter","Close-fitting decorative halter, flat or rolled leather, made to show off the head in in-hand classes.",W+"Halter",a="in-hand halter · Arabian show halter",
     v=[("Congress Silver Show Halter","Royal King","","silver-mounted"),("Rolled Nose Arabian Style Premium Leather Halter","Quiet Creek","","Arabian style"),("Original Nylon Arabian Halter","Weaver Leather","",""),("Thoroughbred Premium Leather Halter","Quiet Creek","","")],
     dt="flat or rolled leather · silver trim · matching show lead shank"),
   X("Breakaway headcollar","Safety headcollar that gives way under panic through a leather crown, breakaway buckle or detachable part.",W+"Halter",a="safety halter · field-safe headcollar",
     v=[("Padded Breakaway Nylon Halter","Weaver Leather","","")],dt="leather crown or breakaway tab · padding"),
  ],
  "m":[["Werano Therapeutic Halter","Back on Track"],["Grooming Halter","Tory Leather"],["Victory Standardbred Nylon Halter","Walsh"],["Kalley Krickeberg Horseman's Combination Halter","Weaver Leather"],["Two Tone Beta Halter","Country Pride"]]},
 {"n":"Lead rope","a":"lead · lead shank","d":"A rope or strap with a clip or snap that is fixed to a headcollar to lead or tie up a horse.",
  "t":["cotton","polypropylene","yacht braid","nylon webbing","leather","with chain (lead shank)","show lead shank","bull snap · trigger snap · panic snap","about 9–12 ft working length","longer natural-horsemanship training rope"],
  "s":"https://www.thevetshed.com.au/horses/saddlery/halters/?pgnum=1",
  "m":[["Cotton Lead Rope","Weaver Leather"],["Poly Lead Rope","Weaver Leather"],["Silvertip Yacht Braid Lead","Weaver Leather"],["1\" Single-Ply Horse Lead with Chain","Weaver Leather"],["Stacy Westfall Training Rope","Weaver Leather"],["EcoLuxe Bamboo Lead","Weaver Leather"],["Woven Poly Cord Lead Rope","Tough1"],["Riding Cotton Lead","Hilason"],["Western Nylon Lead Rope","Hilason"]]},
 {"n":"Lunge line","a":"lunge rein · longe line","d":"A long line fixed to a horse's headgear by which it is worked in a circle round the handler.",
  "t":["flat cotton or nylon webbing (about 25–30 ft)","round cotton rope (shorter, natural horsemanship)","with chain","snap end","padded or grip handle"],
  "s":"https://www.cheshirehorse.com/tack/training/lunge-lines",
  "m":[["Cushion Web Lunge Line","Centaur"],["Saga Lunge Line","Equinavia"],["Grip-Tek Lunge Line","LeMieux"],["Lunge Line","Professional's Choice"],["Arma Cotton Lunge Line","Shires"],["Soft Feel Lunge Line","Shires"],["German Cord Cotton Lunge Line","Tough1"],["Lunge Line with Chain","Walsh"],["Flat Cotton Lunge Line","Weaver Leather"],["Flat Nylon Lunge Line","Weaver Leather"],["Rounded Cotton Lunge Line","Weaver Leather"]]},
 {"n":"Lunge roller and side reins","a":"surcingle · roller · side reins · lungeing aids","d":"Padded girth band with rings, and the reins and training aids clipped to it, used when lungeing or long-lining a horse.",
  "s":W+"Longeing",
  "x":[
   X("Training surcingle","Padded roller with many rings up the sides for side reins or long reins when lungeing or long-lining.",W+"Surcingle",a="lunge roller · training roller",
     v=[("Vaulting surcingle","","","variation of the training surcingle for equestrian vaulting"),("Basic surcingle","","","unpadded strap without rings, worn over a racing saddle")],dt="number and height of rings · padding · leather or synthetic"),
   X("Side reins","Pair of reins from the bit to the roller or girth, set to encourage balance and steady head carriage on the lunge.",W+"Longeing",dt="plain leather or with elastic or rubber insert · length adjustment"),
   X("Lungeing cavesson","Headgear with one to three rings on a reinforced noseband for attaching the lunge line.",W+"Longeing",a="longeing cavesson",dt="leather with metal-topped noseband, or padded nylon"),
   X("Pessoa lungeing system","Rope-and-pulley training aid designed by showjumper Nelson Pessoa, fitted to a roller with a rear piece behind the quarters.","https://www.yourhorse.co.uk/gear-advice/pessoa-lungeing-system",a="Pessoa",dt="pony and horse sizes · sheepskin rear piece"),
  ]},
 {"n":"Driving harness","a":"carriage harness · harness","d":"The set of harness a horse, pony or donkey wears to draw a vehicle or implement: collar or breastplate, harness saddle, traces, breeching and reins.",
  "t":["single","pair","tandem","team / four-in-hand","leather","synthetic","miniature / pony / cob / full / draft sizes"],
  "s":"https://www.bbb.org/us/category/harness",
  "x":[
   X("Breast-collar harness","Harness whose pull comes through a padded strap across the chest; needs no individual fitting and suits lighter vehicles.",W+"Horse_collar",a="breastplate harness · Dutch collar harness",dt="collar padding · saddle width · leather or synthetic"),
   X("Full-collar harness","Harness built on a fitted, padded neck collar with hames that carry the traces; for heavier draught.",W+"Horse_collar",a="neck-collar harness · collar and hames",
     dt="collar shape (full face, half sweeney, full sweeney) · wooden or metal hames"),
   X("Hybrid-collar harness","Modern light collar that starts as a breast collar but encircles the neck without hames; popular in combined driving.",W+"Horse_collar"),
   X("Zilco Classic harness","Synthetic driving harness set with stainless fittings, sold as single, pair, tandem and team sets.","https://ivccarriage.com/products/zilco-classic-single-harness-horse-size",mk="Zilco",
     v=[("Classic Single Driving Harness","Zilco","","breast collar; convertible to pair with extra parts"),("Classic Pair Harness","Zilco","",""),("Classic Tandem Leader Harness","Zilco","",""),("Classic Team Harness","Zilco","","")],
     dt="pony, cob, full and horse sizes · breast collar · quick-release tugs"),
  ]},
]
brands=[{"n":"Zilco","c":"Australia","f":"","seg":"synthetic harness","d":"Maker of synthetic driving and racing harness, now also active in New Zealand and the UK.",
  "lines":["Classic"],"eras":[],"sig":["Zilco Classic harness"],"sc":["carriage driving"],"rel":[],"s":"knowledge"}]
notes=("Headcollar: old SKUs folded into four archetypes (working, rope, show, breakaway) sourced from the Halter article; a few unassigned models kept. "
 "No Parelli rope-halter archetype: the retrieved Parelli page confirms the 1981 founding but says nothing about its rope halter, so it was left out. "
 "Lead rope and lunge line stay tier kinds with types and trimmed models (Weaver lead list cut from 11 to 6). "
 "New kind 'Lunge roller and side reins' (sourced: Longeing, Surcingle, YourHorse Pessoa page); Chambon and de Gogue left out (no retrieved page). "
 "Driving harness: collar types as archetypes plus the Zilco Classic family; Zilco brand recorded from knowledge (the harnessstuff history page returned 503).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B10/shelves/04_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
