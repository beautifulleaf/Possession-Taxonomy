import json, os
W='https://en.wikipedia.org/wiki/'
CF=W+'Ceiling_fan'
fan={"n":"Ceiling fan","a":"Paddle fan · fandelight (fan with integral light)",
 "d":"Fan hung from the ceiling, with or without a light.",
 "t":["with light kit","without light","flush-mount (hugger)","downrod-mount","indoor","damp-rated","wet-rated outdoor","AC motor","brushless DC motor","smart/app-controlled","belt-driven","orbit fan","bladeless","pendulum (punkah) fan","residential HVLS"],
 "s":"https://www.delmarfans.com/ceiling-fans/with-lights",
 "x":[
  {"n":"Punkah","a":"Pendulum fan · flap fan","d":"Swinging blade, originally cut from palm leaf and pulled by cord, that moves air to and fro rather than rotating.","mk":"","y":"c. 500 BC (India); belt-driven electric versions later","s":CF,"v":[],"dt":"blade material · manual cord or belt drive"},
  {"n":"Hunter Original","a":"The Original","d":"Cast-iron body ceiling fan with oil-bath lubrication, made continuously since the early 1900s.","mk":"Hunter Fan Company","y":"1906","s":CF,
   "v":[{"n":"36-inch Original (shaded-pole motor)","mk":"Hunter Fan Company","y":"to 1984","d":"91.44 cm span"},
        {"n":"42-inch Original","mk":"Hunter Fan Company","y":"1985","d":"106.68 cm span replaced the 36-inch"},
        {"n":"Motor change","mk":"Hunter Fan Company","y":"2002","d":""},
        {"n":"Revised Original","mk":"Hunter Fan Company","y":"2015","d":""}],
   "dt":"cast-iron housing · oil-bath motor · wood blades · finishes"},
  {"n":"Emerson Heat Fan","a":"","d":"Long-running Emerson ceiling fan model from a maker that pioneered electrically reversible fan motors.","mk":"Emerson Electric","y":"1962–2005","s":CF,"v":[],"dt":"blade span · finish"},
  {"n":"Encon Deco","a":"","d":"Indian-made fan with the Crompton Greaves 20-pole 'pancake' induction motor, imported to the US under the Encon brand.","mk":"Encon Industries","y":"mid-1970s","s":CF,"v":[],"dt":"pancake induction motor · 4 or 5 blades"},
  {"n":"Casablanca Delta","a":"","d":"Premium Casablanca ceiling fan of the early 1980s, from the maker that sold fans as furniture.","mk":"Casablanca Fan Company","y":"early 1980s","s":"https://en.wikipedia.org/wiki/Casablanca_Fan_Company",
   "v":[{"n":"Delta II","mk":"Casablanca Fan Company","y":"1993","d":""}],"dt":"finish · blade set · light kit"},
  {"n":"Big Ass Fans Haiku","a":"Haiku","d":"Residential fan with a concealed brushless DC motor and aerofoil blades of Moso bamboo or composite, drawing about 2–30 W.","mk":"Big Ass Fans","y":"2012","s":"https://www.greenbuildingadvisor.com/article/high-tech-ceiling-fans-for-low-tech-cooling",
   "v":[],"dt":"60 in span · bamboo (natural, cocoa) or composite (black, white) blades · stem lengths · flat or sloped ceiling · optional LED"},
  {"n":"Minka-Aire Light Wave","a":"","d":"Three-blade fan with an integrated LED downlight behind an etched lens.","mk":"Minka-Aire","y":"","s":"https://www.2modern.com/products/light-wave-ceiling-fan",
   "v":[{"n":"F844","mk":"Minka-Aire","y":"","d":"52 in, 3-speed remote; white, distressed koa, silver, coal"}],"dt":"span · finish"}],
 "m":[["Punkah","Fanimation"],["Palmetto","Fanimation"],["Bourbon Street","Fanimation"],["Palisade","Fanimation"],["Islander","Fanimation"],
      ["Katana","Craftmade"],["Presley","Craftmade"],["Ariella","Matthews"],["Alessandra Tropical","Matthews"],["Darling Fandelight","Maxim Lighting"],["Serene","Maxim Lighting"],["Skylark","Modern Forms"]]}
spk={"n":"In-wall and in-ceiling speaker","a":"Architectural speaker · custom-install speaker",
 "d":"Loudspeaker built into a wall or ceiling, with only a flush grille showing; freestanding speakers are in Audio & Video.",
 "t":["in-wall","in-ceiling","LCR in-wall","angled baffle or pivoting tweeter","invisible (plaster-over)","in-wall subwoofer","weather-resistant outdoor/bathroom","fire-rated back box"],
 "s":"https://www.sonance.com/company",
 "x":[
  {"n":"Sonance in-wall loudspeaker","a":"","d":"The first in-wall loudspeaker, a 6½-inch two-way frame on which later in-wall designs were based.","mk":"Sonance","y":"1981–83","s":"https://widescreenreview.com/news_detail.php?id=3967",
   "v":[],"dt":"6½ in two-way frame · magnetic shielding · pivoting tweeter · angled baffle · 3-way 8×12 in"},
  {"n":"KEF Ci Series","a":"Ci","d":"KEF architectural range built around the Uni-Q driver, with the tweeter at the acoustic centre of the cone.","mk":"KEF","y":"","s":"https://www.cepro.com/news/kef_ci_series_architectural_speakers_cedia/3142/",
   "v":[{"n":"Ci160.2CS","mk":"KEF","y":"","d":"Ci-C entry series, 160 mm Uni-Q, shallow mount, IP64"},
        {"n":"Ci200RR","mk":"KEF","y":"2017","d":"in-ceiling, 8 in Uni-Q"},
        {"n":"Ci4100QL","mk":"KEF","y":"2017","d":"in-wall, 4 in Uni-Q array"},
        {"n":"Ci3160RL","mk":"KEF","y":"2017","d":"Reference in-wall"},
        {"n":"Ci5160REF THX Ultra 2","mk":"KEF","y":"2017","d":"THX-certified in-wall"}],
   "dt":"series (Ci-C, Ci-Q, Ci-R, Reference) · round or square · in-wall or in-ceiling"},
  {"n":"Bowers & Wilkins CCM in-ceiling","a":"CCM","d":"Flush in-ceiling speakers from Bowers & Wilkins for music and home cinema.","mk":"Bowers & Wilkins","y":"","s":"https://rapalloav.co.nz/product/bowers-wilkins-ccm7-5-s2-in-ceiling-speaker",
   "v":[{"n":"CCM7.5 S2","mk":"Bowers & Wilkins","y":"","d":"25 mm carbon dome tweeter, 180 mm Continuum cone"},
        {"n":"CCM8.5 D","mk":"Bowers & Wilkins","y":"","d":""}],"dt":"series · driver size"},
  {"n":"Origin Acoustics Director","a":"","d":"Premium in-ceiling collection from a maker founded by former SpeakerCraft leaders.","mk":"Origin Acoustics","y":"2014","s":"https://originacoustics.com/about-origin/",
   "v":[{"n":"Composer","mk":"Origin Acoustics","y":"","d":"in-wall collection"},{"n":"BLENDS","mk":"Origin Acoustics","y":"","d":"invisible speakers"}],"dt":"collection · mounting (minimal opening, ThinFit)"}]}
av={"n":"Motorised TV lift and projection screen","a":"TV lift · projector lift · electric screen",
 "d":"Built-in mechanism that raises, lowers or hides a TV, projector or screen in furniture, floor or ceiling.",
 "t":["cabinet or floor TV lift","ceiling drop-down TV mount","table pop-up lift","moving wall panel","projector lift","ceiling-recessed electric screen","wall or ceiling electric screen","fixed-frame screen","tensioned screen","acoustically transparent screen","ambient-light-rejecting (grey) screen"],
 "s":"https://www.residentialsystems.com/news/future-automation-enters-us-market",
 "x":[
  {"n":"Enlightor 4K","a":"","d":"Woven acoustically transparent screen fabric that lets speakers stand behind the picture.","mk":"Seymour Screen Excellence","y":"2014","s":"https://hometheaterhifi.com/reviews/video-accessory/screens/seymour-screen-excellence-enlightor-4k-acoustically-transparent-projection-screen",
   "v":[],"dt":"gain about 0.8 · optional black backing · frame type"}],
 "r":[["TV, projector and panel lifts","Future Automation"],["Projection screens","Dai Nippon Printing"],["Projection screens","Screen Innovations"],["Projection screens","Sony"]]}
brands=[
 {"n":"Hunter Fan Company","c":"United States","f":"1886","seg":"Ceiling fans, mainstream to premium","d":"Ceiling-fan maker founded by John Hunter and his son James; owns Casablanca.","lines":["Original","HunterSMART (formerly SIMPLEconnect)","WeatherMax"],"eras":[],"sig":["Hunter Original"],"sc":[],"rel":["Casablanca Fan Company"],"s":"https://www.hunterfan.com/blogs/hunter-blog/hunter-the-history-of-the-largest-ceiling-fan-company"},
 {"n":"Casablanca Fan Company","c":"United States","f":"1974","seg":"Premium ceiling fans","d":"Founded by Burton A. Burton; marketed fans as furniture; Hunter's luxury division since 1996.","lines":[],"eras":["Casablanca Industries 1974–1991","General Electric 1991–1996","Hunter Fan 1996–"],"sig":["Casablanca Delta"],"sc":[],"rel":["Hunter Fan Company","Fanimation"],"s":"https://en.wikipedia.org/wiki/Casablanca_Fan_Company"},
 {"n":"Big Ass Fans","c":"United States","f":"1999","seg":"Industrial and premium residential fans","d":"Lexington, Kentucky maker founded by Carey Smith (as Delta T, 1994), known for large HVLS fans.","lines":["Haiku"],"eras":[],"sig":["Big Ass Fans Haiku"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Big_Ass_Fans"},
 {"n":"Fanimation","c":"United States","f":"1984","seg":"Decorative ceiling fans","d":"Founded by Tom Frampton in Pasadena, California; now based in Zionsville, Indiana.","lines":["Punkah","Palmetto","Palisade","Islander"],"eras":[],"sig":[],"sc":[],"rel":["Casablanca Fan Company"],"s":"https://fanimation.com/the-story-of-fanimation/"},
 {"n":"Minka-Aire","c":"","f":"","seg":"Decorative ceiling fans","d":"Ceiling-fan brand sold through lighting dealers.","lines":["Light Wave"],"eras":[],"sig":["Minka-Aire Light Wave"],"sc":[],"rel":[],"s":"https://www.2modern.com/products/light-wave-ceiling-fan"},
 {"n":"Sonance","c":"United States","f":"1983","seg":"Architectural audio","d":"San Clemente, California maker credited with the first in-wall loudspeaker; sister brands James, IPORT, TRUFIG.","lines":[],"eras":[],"sig":["Sonance in-wall loudspeaker"],"sc":[],"rel":[],"s":"https://www.sonance.com/company"},
 {"n":"KEF","c":"United Kingdom","f":"1961","seg":"Hi-fi and architectural speakers","d":"Maidstone loudspeaker maker founded by Raymond Cooke; owned by Gold Peak since 1992.","lines":["Ci Series"],"eras":[],"sig":["KEF Ci Series"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/KEF"},
 {"n":"Bowers & Wilkins","c":"United Kingdom","f":"1966","seg":"Hi-fi and architectural speakers","d":"Worthing loudspeaker maker founded by John Bowers and Roy Wilkins; part of Harman since 2025.","lines":["CCM"],"eras":[],"sig":["Bowers & Wilkins CCM in-ceiling"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Bowers_%26_Wilkins"},
 {"n":"Origin Acoustics","c":"United States","f":"2014","seg":"Architectural audio","d":"Riverside, California speaker maker launched by Jeremy Burkhardt, Ken Humphries and Ed Haase.","lines":["Director","Composer","Producer","BLENDS","ThinFit"],"eras":[],"sig":["Origin Acoustics Director"],"sc":[],"rel":[],"s":"https://originacoustics.com/about-origin/"},
 {"n":"Future Automation","c":"United Kingdom","f":"","seg":"AV lifts and mounts","d":"British maker of motorised TV lifts, projector lifts, moving panels and ceiling drops.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://www.residentialsystems.com/news/future-automation-enters-us-market"},
 {"n":"Seymour Screen Excellence","c":"","f":"","seg":"Projection screens","d":"Projection-screen maker known for acoustically transparent fabrics.","lines":["Enlightor 4K"],"eras":[],"sig":["Enlightor 4K"],"sc":[],"rel":[],"s":"https://hometheaterhifi.com/reviews/video-accessory/screens/seymour-screen-excellence-enlightor-4k-acoustically-transparent-projection-screen"}]
notes=("Ceiling fan: old 11 Delmar-sourced SKUs trimmed to 7 (dropped Craftmade Prost, Sea Scape; Maxim Jewel and Portcullis Fandelight as SKU noise); "
 "added 7 archetypes and 5 Fanimation historic models. Emerson Heat Fan and Encon Deco have no brand-register entries (no brand page retrieved). "
 "Big Ass Fans Haiku versions (Haiku L, Outdoor, Coastal) left out: not confirmed on a retrieved page. Casablanca Panama/Zephyr, Hunter models beyond the Original not confirmed. "
 "Speakers: KEF Ci and B&W CCM versions limited to models seen on retrieved pages; Sonance 1 name not on a retrieved page. "
 "TV lift/screen: no Future Automation model names found; Screen Excellence UK base not confirmed on a retrieved page, so named as on the review (Seymour Screen Excellence). "
 "Freestanding speakers, TVs and projectors stay in Audio & Video (D3). No traditions apply.")
out={"kinds":[fan,spk,av],"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/G3/shelves/02_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
