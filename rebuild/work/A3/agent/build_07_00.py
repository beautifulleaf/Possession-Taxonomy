import json,os
NM="https://neometal.com/blogs/information/neometal-setting-the-standard-since-1997"
NG="https://NEOMETAL.COM/blogs/information/guide-to-threadless-jewelry"
BV="https://coolhunting.com/design/bvlas-body-of-work/"
IS="https://laughingbuddhabodypiercing.com/collections/industrial-strength"
AN="https://anatometal.com/pages/about-us"
JU="https://junipurrjewelry.com/blogs/newsroom/junipurr-journal-august-2022"
BJ="https://thepointjournal.org/2020/04/24/point-80-technical-innovator-award/"
BM="https://bm25.com/pages/size-conversion-chart"
K=[
{"n":"Threadless end","a":"press-fit end · push-pin end · threadless top","d":"Decorative top on a bent pin held by tension inside a threadless labret post or barbell.",
 "t":["prong-set gem","bezel-set gem","cabochon","cluster","plain gold shape"],"s":NG,
 "x":[
  {"n":"Threadless push-pin end","a":"threadless","d":"End whose pin is bent slightly and pushed into the post, held by tension with no threads.","mk":"NeoMetal","y":"1997","s":NM,
   "v":[{"n":"Original threadless system","mk":"NeoMetal","y":"1997","d":"patented 1997, on the US market 1998"},
        {"n":"Universal Threadless System","mk":"NeoMetal","y":"2015","d":"one end fits any post gauge"}],
   "dt":"top: gem, cabochon or metal shape · ASTM F-136 titanium or solid 18k gold · fits 18–12 gauge posts"},
  {"n":"Gold-pin threadless end","a":"unicorn pin","d":"Solid-gold threadless end on a patented gold pin engineered to hold securely, keeping the piece fully gold.","mk":"BVLA","y":"","s":BV,
   "dt":"14k gold · hand-matched gemstones · cast settings"},
  {"n":"Odyssey Luna end","d":"Threadless end with a prong-set faceted gem.","mk":"Industrial Strength","y":"","s":IS,
   "dt":"gem colour and size · titanium"}],
 "m":[["Crown End","Industrial Strength"],["Flower End","Industrial Strength"],["Star End","Industrial Strength"],["Heart End","Industrial Strength"]]},
{"n":"Labret stud","a":"labret · flatback","d":"Post with a flat disc back inside and a decorative end outside, for lip, ear cartilage and nostril piercings.",
 "t":["internally threaded","threadless","flat disc back","post length"],"s":BM,
 "x":[{"n":"Threadless labret post","d":"One-piece post with a flat back and a smooth open end that takes a press-fit threadless top.","mk":"NeoMetal","y":"","s":NG,
   "dt":"gauge 18–12 · post length · ASTM F-136 titanium or 18k gold · inserted with a taper pin"}]},
{"n":"Nose stud","a":"nose pin · nosepin","d":"Small stud worn in a nostril piercing on an L-shape, screw, pin or bone post.",
 "t":["L-shape","nose screw","straight pin","nose bone","flat-back labret"],"s":BM},
{"n":"Nose ring","a":"nose hoop · septum ring","d":"Ring or hoop worn through a nostril or septum piercing.",
 "t":["seamless hoop","captive bead","hinged clicker","septum retainer"],"s":BM,
 "x":[{"n":"Nathori","a":"bulaki","d":"South Asian septum ring, traditionally gold, with a teardrop pendant that moves along the ring.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Nose_piercing",
   "dt":"gold · drop size · plain or gem-set"}]},
{"n":"Clicker ring","a":"hinged segment ring · clicker","d":"Piercing ring closed by a hinged segment that clicks into place.",
 "t":["plain","gem-set front","septum clicker","daith clicker"],"s":"https://www.bodyjewellery.co.uk/products/steel-hinged-smooth-segment-ring",
 "x":[{"n":"Titanium septum clicker","d":"Hinged titanium clicker shaped for the septum, sold as a numbered design series.","mk":"Industrial Strength","y":"","s":IS,
   "v":[{"n":"Titanium Septum Clickers 21–26","mk":"Industrial Strength","d":"numbered designs"}],"dt":"gauge · inner diameter · titanium, anodised colours"}]},
{"n":"Seamless ring","a":"seamless hoop · continuous ring","d":"Plain ring whose ends meet with no bead, opened by twisting the ends sideways.",
 "t":["plain","twisted"],"s":"https://bodyjewelry.com/blog/whats-the-difference-between-a-captive-bead-ring-and-a-seamless-ring/"},
{"n":"Captive bead ring","a":"CBR · ball closure ring · BCR · captive hoop","d":"Ring held closed by a bead or ball captured between its ends by tension.",
 "t":["steel","titanium","niobium","glass, acrylic, ceramic or gem bead"],"s":"https://en.wikipedia.org/wiki/Captive_bead_ring"},
{"n":"Circular barbell","a":"horseshoe","d":"Open ring-shaped bar with a threaded or pressed ball or end at each tip.",
 "t":["externally threaded","internally threaded","threadless"],"s":"https://bodyjewelry.com/steel-horseshoe-circular-barbells-16g/",
 "x":[{"n":"Threadless circular barbell","d":"Horseshoe bar taking press-fit threadless ends at both tips.","mk":"NeoMetal","y":"2022","s":NM,
   "dt":"gauge · diameter · titanium · end styles"}],
 "m":[["Threaded Titanium Circular Barbell Post","Industrial Strength"]]},
{"n":"Straight barbell","a":"barbell · industrial bar","d":"Straight bar with an end at each side, for tongue, cartilage, nipple and similar piercings.",
 "t":["internally threaded","threadless","nipple bar","industrial bar","large gauge"],"s":BM,
 "m":[["Large Gauge Threaded Straight Barbell","Industrial Strength"]]},
{"n":"Curved barbell","a":"bent barbell","d":"Bent bar with an end at each side, for brow, rook, daith and similar piercings.",
 "t":["internally threaded","threadless"],"s":BM,
 "m":[["Threaded Titanium Curved Barbell Post","Industrial Strength"]]},
{"n":"Navel curve","a":"belly button ring · banana bell · bananabell","d":"Curved barbell made for a navel piercing, usually with a larger or dangling lower end.",
 "t":["plain gem","double gem","dangle","navel clicker","PTFE"],"s":"https://en.wikipedia.org/wiki/Navel_piercing",
 "x":[{"n":"Double bezel-set gem navel curve","d":"Navel curve with a bezel-set gem at both ends.","mk":"Industrial Strength","y":"","s":IS,
   "v":[{"n":"Double Bezel-Set Gem Curved Barbell 14g","mk":"Industrial Strength"},{"n":"Double Bezel-Set Gem Curved Barbell 12g","mk":"Industrial Strength"}],
   "dt":"gauge 14 or 12 · length · gem colour · titanium"}]},
{"n":"Surface bar","a":"surface barbell · staple bar","d":"Staple-shaped bar with two upturned ends, made for a surface piercing.",
 "t":["90-degree","internally threaded","threadless","PTFE"],"s":"https://www.painfulpleasures.com/products/14g-titanium-surface-barbells-90-degree-for-surface-piercings-nape-internally-threaded"},
]
B=[
{"n":"NeoMetal","c":"United States","f":"1997","seg":"High-end body jewellery","d":"Californian maker that invented and patented threadless body jewellery.","lines":["Threadless","Universal Threadless System","Threadless Circular Barbells","Illusion Rings"],"eras":["Ted and Sue Siekierski, founders, 1997–"],"sig":["Threadless push-pin end","Threadless circular barbell"],"sc":["Professional piercing"],"rel":["Anatometal","BVLA","Industrial Strength"],"s":NM},
{"n":"Anatometal","c":"United States","f":"1991","seg":"High-end body jewellery","d":"Santa Cruz maker of implant-grade titanium, steel, niobium and in-house cast gold body jewellery.","lines":[],"eras":[],"sig":[],"sc":["Professional piercing"],"rel":["Industrial Strength","NeoMetal"],"s":AN},
{"n":"BVLA","c":"United States","f":"","seg":"Fine body jewellery","d":"Body Vision Los Angeles, founded by Nick Martin; makes cast solid-gold body jewellery and threadless ends.","lines":[],"eras":["Nick and Kerry Martin"],"sig":["Gold-pin threadless end"],"sc":["Professional piercing"],"rel":["NeoMetal","Anatometal"],"s":BV},
{"n":"Industrial Strength","c":"United States","f":"1991","seg":"High-end body jewellery","d":"Founded by JD Lorenz in San Diego, now made in Carlsbad, California; titanium ends, barbells, clickers and navel curves.","lines":["Odyssey"],"eras":["JD Lorenz, founder, c. 1991–"],"sig":["Odyssey Luna end","Titanium septum clicker","Double bezel-set gem navel curve"],"sc":["Professional piercing"],"rel":["Anatometal","NeoMetal"],"s":IS},
{"n":"Junipurr","c":"","f":"","seg":"Gold and titanium body jewellery","d":"Maker of gold ends, gold gem ends, threaded gold ends and implant-grade titanium posts for piercers.","lines":["Gold Ends","Threaded Gold Ends"],"eras":[],"sig":[],"sc":["Professional piercing"],"rel":["BVLA"],"s":JU},
{"n":"Maria Tash","c":"United States","f":"","seg":"Luxury piercing jewellery","d":"New York fine-jewellery brand for piercings, known for the curated-ear style and invisible-set diamonds.","lines":[],"eras":[],"sig":[],"sc":["Curated ear"],"rel":["BVLA"],"s":"knowledge"},
{"n":"Buddha Jewelry Organics","c":"United States","f":"2002","seg":"Organic and stretched-ear jewellery","d":"Seattle-area maker founded by Rion and Katrina Wickersham, making stone, wood and metal plugs, weights and hoops.","lines":["Halo","Idol","Luxe","Deco","Osiris","Muse"],"eras":["Rion and Katrina Wickersham"],"sig":[],"sc":["Stretched ears"],"rel":[],"s":BJ},
]
notes=("All 10 old kinds kept; Threadless end and Seamless ring added. Maria Tash: its own product pages rendered without content and Harrods returned 403, so no Maria Tash archetypes (eternity/invisible-set clickers) were attested; brand entry from knowledge with no founding year. "
"Anatometal and Junipurr have register entries but no archetypes (no product page retrieved). Buddha Jewelry Organics lines are mainly plugs/weights for the stretched-ear shelf. "
"BVLA founding year left out (article implies c. 1996 only). Septum retainer and nathori placed under Nose ring. Gauge and diameter recorded as detail axes.")
out={"kinds":K,"brands":B,"traditions":[],"notes":notes}
p="work/A3/shelves/07_00.json";json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1);os.replace(p+".tmp",p)
