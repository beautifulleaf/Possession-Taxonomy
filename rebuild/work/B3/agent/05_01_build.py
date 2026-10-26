import json, os
P='https://en.wikipedia.org/wiki/Petzl'
head = {
 "n":"Headlamp","a":"head torch · headtorch",
 "d":"Light worn on the head on a band or helmet mount, leaving both hands free.",
 "t":["AAA battery","rechargeable pack","hybrid (rechargeable or AAA)","18650/21700 cell","separate battery pack on cable","reactive (sensor) lighting","red night mode","caving lamp","running","ultralight","kids'"],
 "s":"https://zips.com/shop-by-brand/streamlight",
 "x":[
  {"n":"Petzl Tikka","a":"TIKKA","d":"Compact front-unit headlamp family; Petzl's first LED headlamps.","mk":"Petzl","y":"2000","s":P,
   "v":[{"n":"Tikka","mk":"Petzl","y":"","d":"current 350-lumen hiking and camping model"},{"n":"Tikka Core","mk":"Petzl","y":"","d":"rechargeable CORE battery version"},{"n":"Tikkina","mk":"Petzl","y":"","d":"entry model"},{"n":"Tikkid","mk":"Petzl","y":"","d":"children's headlamp"},{"n":"Tactikka","mk":"Petzl","y":"","d":"hunting and tactical version"},{"n":"Tactikka +RGB","mk":"Petzl","y":"","d":"coloured-light version"}],
   "dt":"output · AAA or CORE battery · red light · colour"},
  {"n":"Petzl Zoom","a":"","d":"Petzl's first brand-name headlamp, a historical model from the incandescent era.","mk":"Petzl","y":"1981","s":P,
   "v":[{"n":"Zoom","mk":"Petzl","y":"1981","d":"first brand-name headlamp"}],"dt":"historical; condition and completeness"},
  {"n":"Petzl Actik","a":"ACTIK","d":"Mixed flood-and-spot headlamp with red light; the Core version takes a CORE rechargeable pack or three AAAs.","mk":"Petzl","y":"","s":"https://www.cleverhiker.com/blog/petzl-actik-core-headlamp-review",
   "v":[{"n":"Actik","mk":"Petzl","y":"","d":"AAA-only version"},{"n":"Actik Core","mk":"Petzl","y":"","d":"hybrid; 625 lm current version, 600 lm previous"},{"n":"Reactik","mk":"Petzl","y":"","d":"reactive-lighting sibling"},{"n":"Reactik+","mk":"Petzl","y":"","d":"reactive-lighting sibling"}],
   "dt":"output · battery · beam pattern · colour"},
  {"n":"Petzl Swift RL","a":"SWIFT","d":"Compact rechargeable headlamp with Reactive Lighting, which adjusts brightness to the surroundings.","mk":"Petzl","y":"","s":"https://outsidebozeman.com/gear/product-reviews/misc/review-petzl-swift-rl-headlamp",
   "v":[{"n":"Swift RL","mk":"Petzl","y":"","d":"reactive lighting, USB-C rechargeable"},{"n":"Swift LT","mk":"Petzl","y":"","d":"non-reactive version"}],"dt":"output · reactive on/off"},
  {"n":"Petzl Nao","a":"NAO","d":"High-output running headlamp with Reactive Lighting and a rear battery pack.","mk":"Petzl","y":"","s":"https://www.petzl.com/INT/en/Sport/Headlamps/NAO-RL",
   "v":[{"n":"Nao RL","mk":"Petzl","y":"","d":"current model, code E105AA00"},{"n":"Nao+","mk":"Petzl","y":"","d":"earlier model"}],"dt":"output · battery · strap"},
  {"n":"Black Diamond Spot","a":"Spot","d":"Light AAA headlamp with a PowerTap touch spot for dimming; a long-running value classic.","mk":"Black Diamond Equipment","y":"","s":"https://www.outdoorgearlab.com/reviews/camping-and-hiking/headlamp/black-diamond-spot",
   "v":[{"n":"Spot 400","mk":"Black Diamond Equipment","y":"","d":"AAA version"},{"n":"Spot 400-R","mk":"Black Diamond Equipment","y":"","d":"rechargeable version"}],"dt":"output · AAA or rechargeable · colour"},
  {"n":"Zebralight H600","a":"H6xx · Zebralight H-series","d":"Aluminium 18650 tube light in a silicone headband holder that comes out for use as a handheld.","mk":"Zebralight","y":"","s":"https://justinsimoni.com/review-zebralight-h600w-mk-iv/",
   "v":[{"n":"H600w Mk IV","mk":"Zebralight","y":"","d":"neutral white, about 1,400 lumens"}],"dt":"emitter tint (w/c/d) · flood (F) or mixed beam · Mk generation"},
  {"n":"Fenix HM50R","a":"","d":"Small metal-bodied rechargeable headlamp whose housing detaches from the strap as a handheld.","mk":"Fenix","y":"","s":"https://www.greatwalks.com.au/gear/review-fenix-hm50r-v2-0-headtorch/",
   "v":[{"n":"HM50R V2.0","mk":"Fenix","y":"","d":"700 lm, 16340 cell, red light"},{"n":"HM53R","mk":"Fenix","y":"","d":""},{"n":"HM55R Renegade","mk":"Fenix","y":"","d":""},{"n":"HM61R V3","mk":"Fenix","y":"","d":""},{"n":"HM65R V2","mk":"Fenix","y":"","d":"spot plus flood"},{"n":"HM71R V2.0","mk":"Fenix","y":"","d":""},{"n":"HM75R Pro","mk":"Fenix","y":"","d":""}],"dt":"output · cell size · red light"},
  {"n":"Nitecore NU","a":"NU series","d":"Ultralight USB-rechargeable headlamp series; the NU25 UL weighs 47 g with band.","mk":"Nitecore","y":"","s":"https://www.nitecore.com/product/nu25ul",
   "v":[{"n":"NU25 MCT UL","mk":"Nitecore","y":"","d":"400 lm, three colour temperatures, 47 g"},{"n":"NU25","mk":"Nitecore","y":"","d":""},{"n":"NU25 MCT","mk":"Nitecore","y":"","d":""},{"n":"NU20 Classic","mk":"Nitecore","y":"","d":""},{"n":"NU27","mk":"Nitecore","y":"","d":""},{"n":"NU33","mk":"Nitecore","y":"","d":""},{"n":"NU43","mk":"Nitecore","y":"","d":""},{"n":"NU53","mk":"Nitecore","y":"","d":""}],"dt":"weight · output · colour temperature"},
  {"n":"Ledlenser H-series","a":"H7R · HF · MH","d":"Focusable headlamps using Ledlenser's Advanced Focus System to move from spot to flood.","mk":"Ledlenser","y":"","s":"https://ledlenser.co.uk/products/h7r-core",
   "v":[{"n":"H7R Core","mk":"Ledlenser","y":"2021","d":"1000 lm, 21700 cell, magnetic charging"},{"n":"H7R.2","mk":"Ledlenser","y":"","d":""},{"n":"H19R","mk":"Ledlenser","y":"","d":""},{"n":"HF8R Core","mk":"Ledlenser","y":"","d":""},{"n":"MH10","mk":"Ledlenser","y":"","d":"outdoor line"},{"n":"NEO5R","mk":"Ledlenser","y":"","d":"running line"},{"n":"KidLED2","mk":"Ledlenser","y":"","d":"children's line"}],"dt":"output · focus · battery · line (H, HF, MH, NEO, Kid)"}
 ],
 "m":[["Duo S","Petzl"],["Aria 2","Petzl"],["Zipka","Petzl"],["e+LITE","Petzl"],["Myo","Petzl"],["Storm R","Black Diamond"],["Sprinter 500","Black Diamond"],["Distance LT 1100","Black Diamond"],["Astro 300","Black Diamond"],["HL60R","Fenix"],["HP25R","Fenix"],["HC65 UHi","Nitecore"],["UT27","Nitecore"],["Perun 2","Olight"],["Perun 3","Olight"],["Range 400","BioLite"],["HeadLamp 800 Pro","BioLite"],["H50","AceBeam"],["H04 RC","Skilhunt"],["FL97R","Coast Products"],["Cross Trail 7R","Silva"],["Sledge","Streamlight"],["Septor","Streamlight"],["Minimus","SureFire"],["Indestructible H20 Pro","VARTA"],["HD800R","ANSMANN"]],
 "r":[["Aria","Petzl"],["HC Series","Nitecore"],["Array","Olight"],["ECO Series","Fenix"]]
}
clip = {"n":"Clip-on light","a":"clip light","d":"Small light with a clip made to attach to a cap, pocket, strap or bag.",
 "s":"https://zips.com/shop-by-brand/streamlight",
 "x":[
  {"n":"Olight Oclip","a":"Oclip","d":"USB-C rechargeable clip light with white and red LEDs and a magnetic body.","mk":"Olight","y":"","s":"https://eknives.com/olight-diy-bundle-oclip-clip-light-with-white-and-red-light-black-300-lumens/",
   "v":[{"n":"Oclip","mk":"Olight","y":"","d":"300 lm white, red LED"},{"n":"Oclip Pro","mk":"Olight","y":"","d":""},{"n":"Oclip Pro S","mk":"Olight","y":"","d":""},{"n":"Oclip 2 Pro","mk":"Olight","y":"","d":""},{"n":"Oclip 2 Ultra","mk":"Olight","y":"","d":""}],"dt":"output · colour LEDs · body colour/finish"},
  {"n":"Streamlight ClipMate","a":"ClipMate","d":"Clip light with an unbreakable clip and a flexible neck for aiming; white and red LEDs.","mk":"Streamlight","y":"","s":"https://www.officer.com/home/press-release/11389153/streamlight-inc-streamlight-debuts-clipmate-usb",
   "v":[{"n":"ClipMate","mk":"Streamlight","y":"","d":"original, non-rechargeable"},{"n":"ClipMate USB","mk":"Streamlight","y":"2014","d":"rechargeable, 70 lm, C4 white and red LEDs"}],"dt":"battery · LED colours"}
 ],
 "m":[["NU11","Nitecore"]]}
brands=[
 {"n":"Petzl","c":"France","f":"","seg":"climbing, caving and headlamps","d":"French maker of climbing and caving equipment and headlamps, based in Crolles near Grenoble; founded by caver Fernand Petzl.","lines":["Tikka","Actik","Swift","Nao","Aria","Duo"],"eras":[],"sig":["Petzl Tikka","Petzl Zoom","Petzl Actik","Petzl Swift RL","Petzl Nao"],"sc":["climbing","caving","trail running","hiking"],"rel":["Black Diamond Equipment"],"s":P},
 {"n":"Black Diamond Equipment","c":"United States","f":"1989","seg":"climbing and outdoor equipment","d":"American maker of climbing, skiing and outdoor gear including headlamps.","lines":["Spot","Storm","Sprinter","Distance","Astro"],"eras":[],"sig":["Black Diamond Spot"],"sc":["climbing","hiking"],"rel":["Petzl"],"s":"knowledge"},
 {"n":"Fenix","c":"China","f":"","seg":"enthusiast and outdoor lights","d":"Chinese maker of flashlights and headlamps.","lines":["HM","HL","HP"],"eras":[],"sig":["Fenix HM50R"],"sc":["hiking","EDC"],"rel":["Nitecore","Olight"],"s":"knowledge"},
 {"n":"Nitecore","c":"China","f":"","seg":"enthusiast and outdoor lights","d":"Chinese maker of flashlights, headlamps and battery chargers.","lines":["NU","HC","UT"],"eras":[],"sig":["Nitecore NU"],"sc":["ultralight hiking","EDC"],"rel":["Fenix","Olight"],"s":"knowledge"},
 {"n":"Ledlenser","c":"Germany","f":"","seg":"torches and headlamps","d":"German maker of focusable LED torches and headlamps.","lines":["H","HF","MH","NEO","KidLED"],"eras":[],"sig":["Ledlenser H-series"],"sc":["outdoor","work"],"rel":[],"s":"knowledge"},
 {"n":"Zebralight","c":"","f":"","seg":"enthusiast lights","d":"Small maker of enthusiast flashlights and headlamps known for its H-series 18650 headlamps.","lines":["H series","SC series"],"eras":[],"sig":["Zebralight H600"],"sc":["flashlight enthusiasts"],"rel":[],"s":"https://justinsimoni.com/review-zebralight-h600w-mk-iv/"},
 {"n":"Olight","c":"China","f":"","seg":"enthusiast and EDC lights","d":"Chinese maker of flashlights, clip lights and headlamps.","lines":["Oclip","Perun","Array"],"eras":[],"sig":["Olight Oclip"],"sc":["EDC"],"rel":["Fenix","Nitecore"],"s":"knowledge"},
 {"n":"Streamlight","c":"United States","f":"1973","seg":"professional and duty lights","d":"American maker of flashlights, headlamps and clip lights for duty and outdoor use.","lines":["ClipMate","Septor","Sledge","Bandit"],"eras":[],"sig":["Streamlight ClipMate"],"sc":["police and fire","work","EDC"],"rel":["SureFire"],"s":"knowledge"}
]
notes=("Headlamp: 116 flat models cut to 10 archetypes (Petzl Tikka, Zoom, Actik, Swift RL, Nao; BD Spot; Zebralight H600; Fenix HM50R; Nitecore NU; Ledlenser H-series) with old models as versions, plus 26 market-covering leftovers in m. "
 "Dropped as SKU noise: redundant colour/edition SKUs (Signature, RGB, Work, Core variants of Ledlenser HF/H, ANSMANN HD200B/HD700RS-DS, BioLite Range 300/500, Dash 450, Fenix HL12R/HL30/HL32R/HL40R/HP15UE/HP30R, Nitecore NU30/NU45/NU50/HC60 UHi/UT27 MCT Pro/NU25 UL, Ledlenser H3.2/H7 SE/H8R SE/H14R.2/H15R/HF4R/HF6R/MH3-MH8/NEO1R/NEO3/NEO9R/KidLED4R, Petzl Aria 1/Duo Z2/Nao RL dup, Olight Perun 3 Mini, Streamlight Bandit/QB/Trident, Coast RL35R, VARTA H30R/H10 Pro). "
 "Ranges Tikka/Actik/Swift/NU/Perun folded into archetypes. Caving lamps (e.g. Scurion) kept only as a type: no retrievable page. Zoom year 1981 per Wikipedia (1973 = first Petzl mountaineering headlamp); Petzl founding year omitted (Wikipedia gives 1970 and 1975). "
 "Zebralight right-angle form not confirmed on a fetched page, so not stated. Many retail pages blocked (REI, GPKnives, Trailspace, Scheels, MEC); Firecrawl out of credits.")
out={"kinds":[head,clip],"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B3/shelves/05_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
