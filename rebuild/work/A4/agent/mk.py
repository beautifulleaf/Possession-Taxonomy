import json,os
W="https://en.wikipedia.org/wiki/"
kinds=[
{"n":"Belt bag","a":"bum bag · fanny pack · waist bag · hip pack · moon bag · belly bag","d":"Small pouch worn on a strap round the waist, usually buckled, now often worn across the chest.",
 "t":["worn at the waist","worn crossbody","nylon or polyester","coated canvas","leather","outdoor hip pack","designer belt bag"],
 "s":W+"Fanny_pack",
 "x":[
 {"n":"Black Hole Waist Pack","a":"Patagonia Black Hole hip pack","d":"5-litre outdoor waist pack in recycled ripstop polyester with TPU laminate, mesh back panel, stretch bottle pockets and compression straps.","mk":"Patagonia","y":"","s":"https://bikeradar.com/reviews/accessories/bags/waist-bag/patagonia-black-hole-waist-pack-5l-review",
  "v":[{"n":"Black Hole Waist Pack 5L","mk":"Patagonia","y":"2020","d":"reviewed 2020; 300-denier recycled polyester, 38 mm waistbelt"}],
  "dt":"capacity 5 L · Black Hole fabric colours"},
 {"n":"Everywhere Belt Bag","a":"Lululemon belt bag","d":"Compact 1-litre recycled-nylon belt bag sold as a waist bag but mostly worn crossbody; a social-media hit.","mk":"Lululemon","y":"","s":"https://gulfnews.com/best-buys/lululemon-everywhere-belt-bag-review-why-this-viral-favourite-still-earns-its-place-1.500621385",
  "v":[],"dt":"capacity 1 L · about 19 × 13 × 5 cm · colours"},
 {"n":"Bumbag","a":"LV Bumbag · Louis Vuitton bum bag","d":"Louis Vuitton belt bag in Monogram coated canvas with leather trim, part of the designer fanny-pack revival.","mk":"Louis Vuitton","y":"c. 2018","s":"https://www.1stdibs.com/buy/louis-vuitton-monogram-bumbag/",
  "v":[{"n":"Monogram Canvas Bumbag","mk":"Louis Vuitton","y":"","d":"about 37 × 14 × 13 cm, vachetta trim"},
       {"n":"Mini Bumbag","mk":"Louis Vuitton","y":"","d":"smaller size"},
       {"n":"High Rise Bumbag","mk":"Louis Vuitton","y":"","d":""},
       {"n":"Discovery Bumbag","mk":"Louis Vuitton","y":"","d":"menswear version, incl. Monogram Shadow"},
       {"n":"Dauphine Bumbag BB","mk":"Louis Vuitton","y":"","d":""}],
  "dt":"Monogram, Monogram Eclipse, Monogram Shadow · size BB, PM, Maxi · artist editions"},
 {"n":"Ophidia belt bag","a":"Gucci Ophidia","d":"Gucci belt bag in GG Supreme canvas or leather with the green-red web stripe and Double G detail.","mk":"Gucci","y":"","s":"https://www.1stdibs.com/buy/gucci-gg-canvas-belt-bag",
  "v":[{"n":"Ophidia small belt bag","mk":"Gucci","y":"","d":""},{"n":"Ophidia mini belt bag","mk":"Gucci","y":"","d":""}],
  "dt":"GG Supreme canvas, suede, leather · size mini, small · gold-tone hardware"}],
 "m":[["Jumbo GG belt bag","Gucci"],["Eden waist bag","Gucci"]]},
{"n":"Sling bag","a":"sling · sling pack","d":"Single-strap pack worn across the body on the back, chest or hip.",
 "t":["camera sling","everyday sling","mini sling under 2 L","convertible to waist pack"],
 "s":"https://www.dickssportinggoods.com/a/crossbody-sling-bag.html",
 "x":[
 {"n":"Everyday Sling","a":"Peak Design sling","d":"Structured camera-and-everyday sling with swivel quick-adjust strap, origami-style dividers and magnetic sleeve.","mk":"Peak Design","y":"2016","s":W+"Peak_Design",
  "v":[{"n":"Everyday Sling (V1)","mk":"Peak Design","y":"2016","d":"launched in the Everyday Backpack, Tote and Sling Kickstarter"},
       {"n":"Everyday Sling 3L / 6L V2","mk":"Peak Design","y":"","d":"camera-first sizes, can be worn as a waist pack"},
       {"n":"Everyday Sling 10L V2","mk":"Peak Design","y":"","d":"400D recycled nylon, 13-inch laptop sleeve"}],
  "dt":"capacity 3 · 6 · 10 L · Black, Ash and seasonal colours"},
 {"n":"Sling","a":"Bellroy Sling","d":"Slim 7-litre self-compressing sling in woven polyester with leather pulls and a padded back.","mk":"Bellroy","y":"","s":"https://packhacker.com/travel-gear/bellroy/sling/",
  "v":[{"n":"Sling","mk":"Bellroy","y":"","d":"Venture Weave polyester"},{"n":"Sling Premium Edition","mk":"Bellroy","y":"","d":"certified leather and sustainably sourced fabrics"}],
  "dt":"capacity 7 L · colours"},
 {"n":"Featherlight Sling Bag","a":"Away Featherlight Sling","d":"Tiny 1.1-litre polyester-twill sling from Away's Featherlight collection, worn crossbody or at the waist.","mk":"Away","y":"","s":"https://www.packhacker.com/travel-gear/away/featherlight-sling-bag/",
  "v":[],"dt":"capacity 1.1 L · Jet Black, Amaro Brown and other colours"}],
 "m":[["The Everywhere Sling","Away"],["Atom Sling","Patagonia"],["Commute Sling","Nike"],["Base Camp Voyager Sling","The North Face"],["Sapling Sling Pack","Thule"]]}]
def B(n,c,f,seg,d,eras,sig,s,rel=[]): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":eras,"sig":sig,"sc":[],"rel":rel,"s":s}
brands=[
B("Patagonia","United States","1973","Outdoor apparel","Ventura, California outdoor clothing and gear company founded by Yvon Chouinard.",[],["Black Hole Waist Pack"],W+"Patagonia,_Inc."),
B("Lululemon","Canada","1998","Athletic apparel","Vancouver athletic-wear retailer that began with yoga clothing.",[],["Everywhere Belt Bag"],W+"Lululemon"),
B("Louis Vuitton","France","1854","Luxury fashion house","Paris trunk maker turned luxury house known for monogram canvas bags.",["Marc Jacobs, artistic director 1997–2013","Nicolas Ghesquière, women's from 2014","Virgil Abloh, men's 2018–2021","Pharrell Williams, men's from 2023"],["Speedy","Keepall","Noé","Neverfull","Bumbag"],W+"Louis_Vuitton",["Gucci"]),
B("Gucci","Italy","1921","Luxury fashion house","Florence luxury house founded by Guccio Gucci, known for the green-red web stripe.",["Tom Ford, 1995–2004","Frida Giannini, 2006–2015","Alessandro Michele, 2015–2022","Sabato De Sarno, 2023–2025","Demna, from 2025"],["Jackie","Bamboo","Ophidia belt bag"],W+"Gucci",["Louis Vuitton"]),
B("Peak Design","United States","2010","Camera and travel carry","San Francisco maker of camera clips and bags founded by Peter Dering, launched via Kickstarter.",[],["Everyday Sling","Everyday Backpack","Capture clip"],W+"Peak_Design"),
B("Bellroy","Australia","2009","Everyday carry accessories","Melbourne maker of slim wallets, bags and travel goods; a certified B Corporation.",[],["Sling"],W+"Bellroy"),
B("Away","United States","2015","Direct-to-consumer luggage","New York luggage brand founded by Steph Korey and Jen Rubio, sold mainly online.",[],["The Carry-On","Featherlight Sling Bag"],W+"Away_(company)")]
notes=("Kept both planned kinds. Belt bag: added Patagonia Black Hole, Lululemon Everywhere Belt Bag, LV Bumbag (old Mini Bumbag became a version), Gucci Ophidia; bum-bag origins covered by the kind source (Wikipedia Fanny pack). "
 "Sling bag: Peak Design Everyday Sling, Bellroy Sling, Away Featherlight Sling archetypes; the old Dick's retailer list trimmed to 5 flat models. "
 "Left out (no retrieved page): Patagonia Ultralight Black Hole Mini Hip Pack, Lululemon clear/velour/large versions, Gucci GG Marmont belt bag, launch years for Everywhere Belt Bag, Bumbag versions and Ophidia; LV and Gucci official/Purseblog pages returned 403. No traditions apply.")
p="work/A4/shelves/03_01.json"; json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
