import json, os
W='https://en.wikipedia.org/wiki/Plug_(jewellery)'
GG='https://getgorilla.com/categoria-producto/plugs/'
K=[
{"n":"Ear plug","a":"plug · earspool · gauge (colloquial)","d":"Solid cylinder worn in a stretched piercing, with double, single or no flare.",
 "t":["double flare","single flare with O-ring","no flare (straight)","glass","stone","wood","horn and bone","amber","titanium","steel","silicone","acrylic"],
 "s":"https://bm25.com/pages/size-conversion-chart",
 "x":[
  {"n":"Double-flare plug","a":"saddle plug","d":"Plug flared at both ends so it sits in the lobe without O-rings.","mk":"","y":"","s":W,
   "dt":"gauge 8g upwards · glass, stone, wood, metal, silicone · solid or patterned front"},
  {"n":"Gorilla Glass plug","a":"","d":"Hand-carved soda-lime glass plug made in solid, coloured-front and dichroic lines.","mk":"Gorilla Glass","y":"","s":GG,
   "v":[{"n":"Solid Plugs","mk":"Gorilla Glass","y":"","d":"plain coloured glass"},
        {"n":"Color Front Plugs","mk":"Gorilla Glass","y":"","d":"coloured front face"},
        {"n":"Simple Plugs","mk":"Gorilla Glass","y":"","d":"clear basic plug"},
        {"n":"Martele Color Front Plugs","mk":"Gorilla Glass","y":"","d":"Martele variant of the coloured-front plug"},
        {"n":"Dichroic Plugs","mk":"Gorilla Glass","y":"","d":"dichroic glass inlay"}],
   "dt":"double or single flare · glass colours · matte or polished"},
  {"n":"Mayan flare plug","a":"Mayan plug","d":"Double-flared stone plug with a wide front flare after ancient Mesoamerican ear flares.","mk":"","y":"","s":"https://bodyartforms.com/productdetails.asp?productid=41062",
   "dt":"8g–1 in · amazonite, bloodstone, lapis and other stones"},
  {"n":"Single-flare plug","a":"O-ring plug","d":"Plug flared at one end and held at the back with a rubber O-ring.","mk":"","y":"","s":W,
   "dt":"glass, steel, titanium, acrylic · O-ring colour"},
  {"n":"Silicone plug","a":"hider plug · hollow plug","d":"Soft flexible plug in implant-grade silicone, often worn to hide or rest a stretch.","mk":"Kaos Softwear","y":"","s":"https://kaossoftwear.com/",
   "dt":"10g–3 in · solid or hollow · colours"}]},
{"n":"Ear tunnel","a":"flesh tunnel · eyelet","d":"Hollow cylinder worn in a stretched piercing.",
 "t":["double flare","single flare with O-ring","threaded (screw-back)","steel","titanium","glass","silicone","wood","stone"],
 "s":"https://bm25.com/pages/size-conversion-chart",
 "x":[
  {"n":"Flesh tunnel","a":"metal tunnel","d":"Tube-shaped tunnel in steel, titanium or glass, held by flares or grooves.","mk":"","y":"","s":W,
   "dt":"wall thickness · flared, threaded or O-ring · finish"},
  {"n":"Skin Eyelets","a":"silicone eyelet · earskin","d":"Thin-walled flexible silicone eyelet with subtle flares, folded to insert.","mk":"Kaos Softwear","y":"","s":"https://kaossoftwear.com/skin-eyelets/",
   "dt":"10g–3 in · colours, glow and UV"},
  {"n":"Gorilla Glass eyelet","a":"glass tunnel","d":"Hollow soda-lime glass eyelet from Gorilla Glass.","mk":"Gorilla Glass","y":"","s":GG,
   "dt":"double flare · glass colours"}]},
{"n":"Ear weight","a":"ear hanger","d":"Heavy hanging piece hooked through a stretched lobe, worn instead of a plug or tunnel.",
 "t":["brass","silver","bronze","copper","stone","horn","wood"],
 "s":"https://maedusabodyjewelry.com/shop/stretched-ears/helios-hangers/",
 "x":[
  {"n":"Helios Hangers","a":"","d":"Wide brass hoop hanger with spring-loaded clasp for stretched lobes of 6 mm and above.","mk":"Maedusa Body Jewelry","y":"","s":"https://maedusabodyjewelry.com/shop/stretched-ears/helios-hangers/",
   "dt":"brass, gold or silver tone · 43 mm inner diameter · 20 g each"},
  {"n":"Diablo Organics ear weights","a":"","d":"Cast brass and silver ear weights hung from coils or hooks in stretched lobes.","mk":"Diablo Organics","y":"","s":"https://diabloorganics.com/products/35184",
   "v":[{"n":"Vintage Ear Weights","mk":"Diablo Organics","y":"","d":"silver and solid brass, 74 × 48 mm, 180 g per pair"}],
   "dt":"brass, silver, stone inlay · weight per pair"}]},
{"n":"Ear taper","a":"stretching taper","d":"Tapered spike or crescent used to stretch a piercing or worn as ornament.",
 "t":["straight taper","crescent taper","spiral","pincher","steel","acrylic","glass","horn"],
 "s":"https://bm25.com/pages/size-conversion-chart",
 "x":[
  {"n":"Crescent taper","a":"pincher · horseshoe taper","d":"Curved C-shaped taper worn as jewellery and used for gradual stretching.","mk":"","y":"","s":"https://dustyjewelz.com/collections/tapers-pinchers-spirals",
   "dt":"gauge · acrylic, glass, horn · O-rings"},
  {"n":"Spiral","a":"stretching twist","d":"Coiled taper worn through a stretched lobe.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Stretching_(body_piercing)",
   "dt":"gauge · acrylic, glass, horn, wood"}]}]
B=[
 {"n":"Gorilla Glass","c":"","f":"","seg":"Glass body jewellery","d":"Maker of hand-carved soda-lime glass plugs, eyelets and other body jewellery.","lines":["Plugs","Eyelets","Retainers"],"eras":[],"sig":["Gorilla Glass plug","Gorilla Glass eyelet"],"sc":["stretched ears"],"rel":["Kaos Softwear"],"s":GG},
 {"n":"Kaos Softwear","c":"United States","f":"","seg":"Silicone body jewellery","d":"US maker of implant-grade silicone body jewellery for stretched piercings.","lines":["Skin Eyelets","Hider Plugs","Hollow Plugs","Retainers"],"eras":[],"sig":["Skin Eyelets","Silicone plug"],"sc":["stretched ears"],"rel":["Gorilla Glass"],"s":"https://kaossoftwear.com/"},
 {"n":"Maedusa Body Jewelry","c":"","f":"","seg":"Body jewellery","d":"Maker of handcrafted brass hangers and ear weights for stretched piercings.","lines":["Stretched ears"],"eras":[],"sig":["Helios Hangers"],"sc":["stretched ears"],"rel":[],"s":"https://maedusabodyjewelry.com/shop/stretched-ears/helios-hangers/"},
 {"n":"Diablo Organics","c":"","f":"","seg":"Organic and metal body jewellery","d":"Maker of brass, silver, stone and amber ear weights and plugs, sold through Jimmy Buddha Designs.","lines":["Ear weights","Plugs"],"eras":[],"sig":["Diablo Organics ear weights"],"sc":["stretched ears"],"rel":[],"s":"https://diabloorganics.com/products/35184"}]
notes=("Four planned kinds kept (old k64-k67); materials and flare styles moved to t. Ear weight keeps Maedusa Helios Hangers as an archetype. "
 "Left out: Maya Jewelry and other organic-plug makers (no retrieved maker page), founding years and countries for Gorilla Glass, Maedusa and Diablo Organics (not confirmed), "
 "version years (none on retrieved pages). Old kinds keep their bm25 source. Parallel search unavailable (402); Firecrawl used.")
out={"kinds":K,"brands":B,"traditions":[],"notes":notes}
p='work/A3/shelves/07_01.json'; os.makedirs('work/A3/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
