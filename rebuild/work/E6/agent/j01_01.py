import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
TV="Tele Vue Optics"; BA="Baader Planetarium"; C="Celestron"; ES="Explore Scientific"; SW="Sky-Watcher"
WE="https://en.wikipedia.org/wiki/Eyepiece"; WT="https://en.wikipedia.org/wiki/Televue"
ep={"n":"Telescope eyepiece","a":"ocular","d":"Lens unit that slides into a telescope's focuser to magnify the image; its focal length sets the power.",
 "t":["0.965-inch barrel","1.25-inch barrel","2-inch barrel","dual 1.25/2-inch skirt"],
 "s":"https://www.highpointscientific.com/brands/celestron/celestron-telescope-accessories/celestron-eyepieces",
 "x":[
  X("Plössl","Two matched achromatic doublets; the standard all-round eyepiece since makers revived it in the 1980s.","","1860",WE,
    [("Simon Plössl's design","","1860","original two-doublet form"),("Tele Vue Plössl",TV,"","Tele Vue's first eyepiece line"),("Super Plossl",SW,"",""),("Plossl","Omegon","","")],
    "apparent field about 50° · eye relief 70–80% of focal length",a="symmetrical"),
  X("Orthoscopic","Four-element eyepiece (triplet field lens and single eye lens) prized for sharp, contrasty planetary views.","","1880",WE,
    [("Abbe orthoscopic","","1880","Ernst Abbe's original"),("Classic Ortho",BA,"","4 elements, 52°, 6/10/18 mm")],
    "apparent field 40–52° · short eye relief",a="Abbe ortho"),
  X("Tele Vue Nagler","First eyepiece to give a sharp 82° apparent field to the edge; started the ultra-wide era.",TV,"1982",WT,
    [("Nagler 13 mm Type 1",TV,"1982","the original")],"82° field · several Types (generations) · 1.25 and 2-inch"),
  X("Tele Vue Panoptic","Six-element 68° eyepiece giving Nagler-like edge correction in a smaller, lighter body.",TV,"","https://www.bhphotovideo.com/c/product/1891082-REG/tele_vue_epn_24_0_panoptic_24mm_eyepiece.html",
    [("Panoptic 24 mm",TV,"","1.25-inch, 15 mm eye relief")],"68° field · 6 elements in 4 groups"),
  X("Tele Vue Ethos","Ultra-wide 100° eyepiece by David Nagler and Paul Dellechiaie.",TV,"2006","https://en.wikipedia.org/wiki/Al_Nagler",
    [("Ethos 13 mm",TV,"2006","first of the line"),("Ethos SX 3.7 mm",TV,"2010","110° field")],"100–110° field"),
  X("Tele Vue Delos","Ethos-derived 72° eyepiece with 20 mm eye relief for spectacle wearers.",TV,"2011",WT,[],"72° field · 20 mm eye relief"),
  X("Explore Scientific wide-field series","Sealed, argon-purged waterproof eyepiece families named by their apparent field, led by the 82° line.",ES,"",
    "https://astronomics.com/collections/eyepieces/products/explore-scientific-6-7mm-82-field-argon-purged-waterproof-1-25-eyepiece",
    [("82 Degree Series",ES,"","7 elements in 4 groups (6.7 mm)"),("100 Degree Series",ES,"",""),("120 Degree 9mm",ES,"",""),("68 Degree Series",ES,"",""),("62 Degree Series LER",ES,"","long eye relief"),("52 Degree Series",ES,"","")],
    "52°–120° fields · argon-purged, O-ring sealed"),
  X("Pentax XW","Japanese 70° eyepiece with 20 mm eye relief across the range.","Pentax","","https://www.adorama.com/PX7XW.html",
    [("SMC XW","Pentax","","1.25-inch focal lengths include 5, 7, 10, 14, 20 mm")],"70° field · 20 mm eye relief"),
  X("Baader Morpheus","Sealed 8-element 76° eyepiece with a dual 1.25/2-inch skirt.",BA,"","https://agenaastro.com/articles/baader-planetarium-morpheus",
    [("Morpheus 76",BA,"","")],"76° field · dual skirt"),
  X("Baader Hyperion Zoom","8–24 mm zoom eyepiece, now in its fourth generation.",BA,"","https://agenaastro.com/articles/baader-hyperion-mark-iv-zoom-eyepiece-performance-review",
    [("Mark III",BA,"","predecessor"),("Mark IV",BA,"2017","48–68° field")],"8–24 mm zoom · click stops"),
  X("Leica ASPH zoom","Leica's aspheric zoom eyepiece, widening from 60° to 80° as it zooms in.","Leica","","https://singastro.org/forum2/viewtopic.php?p=79185",
    [("ASPH 9-18mm zoom","Leica","","60° at 18 mm to 80° at 9 mm")],"9–18 mm zoom")],
 "m":[["Hyperion eyepiece",BA],["Ultima Edge",C],["X-Cel LX",C],["Luminos",C],["E-Lux",C],["Omni",C],["Emerald 82",SW],["Planetary UWA",SW],["UWAN 82","TS Optics"],["LE Planetary","Omegon"],["Super ED","Artesky"],["Kellner",""]]}
bar={"n":"Barlow lens","a":"image amplifier · focal extender","d":"Negative lens unit fitted in a telescope's eyepiece barrel that multiplies the effective focal length, and so the magnification, by a stated factor.",
 "t":["2x","2.5x","3x","adjustable (extension tube)","telecentric focal extender"],
 "s":"https://www.celestron.com/products/x-cel-lx-125in-2x-barlow-lens",
 "x":[X("Tele Vue Powermate","Four-element telecentric amplifier that keeps eye relief and avoids vignetting, unlike a simple Barlow.",TV,"","https://milehighastro.com/products/televue-2-5x-1-1-4-powermate",
    [("Powermate 2.5x",TV,"","1.25-inch"),("Powermate 5x",TV,"","1.25-inch"),("Powermate 2x",TV,"","2-inch"),("Powermate 4x",TV,"","2-inch")],"1.25 or 2-inch · 2x–5x")],
 "m":[["Tele Vue 3x Barlow",TV],["X-Cel LX Barlow",C],["Luminos 2.5x Barlow",C],["Omni 2x Barlow",C]]}
dia={"n":"Star diagonal","a":"diagonal · zenith mirror · zenith prism","d":"Mirror or prism unit between focuser and eyepiece that turns the light 90° for comfortable viewing.",
 "t":["aluminium mirror","dielectric mirror","90° prism","pentaprism (correct image)","Amici erecting prism","0.965, 1.25 or 2-inch"],
 "s":"https://en.wikipedia.org/wiki/Star_diagonal","m":[["T2 Prism Diagonal 1.25\"",BA]]}
bino={"n":"Binoviewer","a":"binocular viewer","d":"Beam-splitter that divides a telescope's light between two eyepieces so you observe with both eyes.",
 "t":["with glass-path corrector","1.25-inch nosepiece","2-inch nosepiece"],
 "s":"https://agenaastro.com/articles/field-test-of-the-baader-maxbright-ii-binoviewer",
 "x":[X("Baader MaxBright","Mid-priced binoviewer with prism coatings tuned for green light and glass-path correctors from 1.25x to 2.6x.",BA,"",
    "https://agenaastro.com/articles/field-test-of-the-baader-maxbright-ii-binoviewer",
    [("MaxBright",BA,"","discontinued"),("MaxBright II",BA,"","26 mm clear aperture")],"26 mm aperture · T2 system")],
 "m":[["Mark V Giant Binoviewer",BA],["Binotron 27","Denkmeier"],["Binoviewer","William Optics"]]}
fin={"n":"Telescope finder","a":"finderscope · finder","d":"Small sighting device fitted on a telescope tube to aim it: finderscope, right-angle finder, red-dot or ring sight. The polar scope is listed separately.",
 "t":["straight-through finderscope","right-angle correct-image (RACI) finderscope","red-dot finder","reflex ring sight"],
 "s":"https://astronomics.com/collections/finderscopes/products/celestron-9x50-right-angle-correct-image-illuminated-finder-scope",
 "x":[X("Telrad","Reflex sight that projects red rings onto the sky with no magnification; the classic finder for Dobsonians.","Telrad","late 1970s","https://en.wikipedia.org/wiki/Telrad",[],"unmagnified reflex rings")],
 "m":[["9x50 Right Angle Correct Image finder",C],["Star Pointer",C],["QuikFinder","Rigel Systems"],["Starbeam",TV]]}
foc={"n":"Telescope focuser","a":"","d":"Draw-tube unit fitted to a telescope that moves the eyepiece or camera to focus.",
 "t":["Crayford","rack and pinion","helical","dual-speed (fine focus)","motorised"],
 "s":"https://astroshop.eu/telescope-accessories/15/m,Astrozap",
 "x":[X("Feather Touch","Precision-machined Crayford-type friction-drive focuser with 10:1 fine focus and an internal brake.","Starlight Instruments","",
    "https://astronomics.com/collections/focusers/products/feather-touch-2-manual-crayford-focuser-for-reflectors-and-scts",
    [("FT-1.5BC","Starlight Instruments","","2-inch, 1.5-inch travel, for reflectors and SCTs")],"1.5–3.5 inch drawtube · dual speed · brake"),
  X("Moonlite Crayford","Low-profile Crayford focuser, single or dual rate, often fitted as an upgrade.","Moonlite Telescopes","",
    "https://astromart.com/reviews/accessories/other/show/moonlite-telescopes-cr2",
    [("CR1","Moonlite Telescopes","","single rate"),("CR2","Moonlite Telescopes","","dual rate, 1.45-inch racked height")],"dual rate · drawtube options")],
 "m":[["Diamond Steeltrack",BA],["Dual-Speed Low Profile Crayford Focuser",SW],["Monorail R96","TS Optics"],["Alpha Crayford Focuser","Omegon"],["2 inch Hybrid Crayford Focuser","Omegon"],["Automatic Focuser iAFS3","iOptron"]]}
col={"n":"Collimator","a":"collimation tool · Cheshire eyepiece · laser collimator","d":"Tool that fits in the focuser to line up a reflecting telescope's mirrors.",
 "t":["sight tube","Cheshire eyepiece","laser collimator"],"s":"https://skyandtelescope.org/astronomy-resources/collimation-tools/"}
dew={"n":"Dew shield & heater","a":"dew shield · dew heater strip · dew controller","d":"Tube or heated band fitted to a telescope to keep dew off the front optics, with the controller that powers the heaters.",
 "t":["rigid dew shield","flexible dew shield","heater strip","heated dew shield","dew controller"],
 "s":"https://astroshop.eu/telescope-accessories/15/m,Astrozap",
 "m":[["Flexi-Shield","Astrozap"],["Flexi-Heat","Astrozap"],["Digital Dew Heater Strip HB-30","Thousand Oaks"],["Soft dew shield cap DX",C],["Soft dew shield cap","Omegon"],["Flexible Dew Shield","TS Optics"]]}
brands=[
 {"n":TV,"c":"United States","f":"1977","seg":"Premium","kf":"eyepieces","d":"Al Nagler's Chester, New York maker of premium eyepieces, Powermates and refractors.","eras":["Al Nagler, 1977–"],
  "sig":["Tele Vue Nagler","Tele Vue Panoptic","Tele Vue Ethos","Tele Vue Delos","Tele Vue Powermate"],"s":WT},
 {"n":BA,"c":"Germany","seg":"Specialist","kf":"eyepieces, filters","d":"German maker of astronomy accessories: eyepieces, binoviewers, diagonals and filters.","sig":["Baader Morpheus","Baader Hyperion Zoom","Baader MaxBright"],"s":"knowledge"},
 {"n":ES,"c":"United States","seg":"Specialist","kf":"wide-field eyepieces","d":"American telescope and eyepiece brand known for argon-purged wide-field eyepieces.","sig":["Explore Scientific wide-field series"],"s":"knowledge"},
 {"n":"Pentax","c":"Japan","seg":"Mainstream","kf":"cameras, optics","d":"Japanese camera and optics brand whose XW eyepieces are an observing reference.","sig":["Pentax XW"],"s":"knowledge"},
 {"n":"Leica","c":"Germany","seg":"Premium","kf":"cameras, sport optics","d":"German camera and optics maker; its ASPH zoom is used as a premium astronomy eyepiece.","sig":["Leica ASPH zoom"],"s":"knowledge"},
 {"n":"Telrad","c":"United States","seg":"Specialist","kf":"reflex finders","d":"Maker of the Telrad reflex sight invented by amateur astronomer Steve Kufeld.","sig":["Telrad"],"s":"https://en.wikipedia.org/wiki/Telrad"},
 {"n":"Starlight Instruments","c":"United States","seg":"Specialist","kf":"focusers","d":"Maker of Feather Touch precision focusers.","sig":["Feather Touch"],"s":"https://astronomics.com/collections/focusers/products/feather-touch-2-manual-crayford-focuser-for-reflectors-and-scts"},
 {"n":"Moonlite Telescopes","seg":"Specialist","kf":"Crayford focusers","d":"Maker of Crayford focusers sold as upgrades for amateur telescopes.","sig":["Moonlite Crayford"],"s":"https://astromart.com/reviews/accessories/other/show/moonlite-telescopes-cr2"}]
w('01_01',{"kinds":[ep,bar,dia,bino,fin,foc,col,dew],"brands":brands,"traditions":[],
 "notes":"Eyepiece: 28 flat models -> 11 archetypes (Plössl, orthoscopic, Nagler, Panoptic, Ethos, Delos, ES series, Pentax XW, Morpheus, Hyperion Zoom, Leica ASPH zoom) + 12 m; dropped old range 'Celestron eyepiece lines' (duplicates m) and duplicate maker-less Plossl. Nagler Types 2-6 not listed as versions (only search snippets, no fetched page). Barlow: maker 'TeleVue' normalised to Tele Vue Optics; Powermates became an archetype. New kinds Star diagonal, Binoviewer, Collimator added; autocollimator left out of Collimator types (no page). Telrad circle sizes and RACI/red-dot archetypes not built (no fetched page). Dew shield renamed Dew shield & heater with heater strip and dew controller types. No traditions (no artisan craft on this shelf)."})
