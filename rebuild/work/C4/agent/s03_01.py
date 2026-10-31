import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
H='https://www.hobbycraft.co.uk/knitting-crochet'
NE='https://bromefields.com/comparing-interchangeable-knitting-needles'; CH='https://justbcrafty.com/my-favorite-crochet-hooks-html/'; SW='https://woolery.com/yarn-ball-winder-and-swift-combo.html'
CC='https://www.woolandcompany.com/products/clover-universal-knitting-counter'; BL='https://www.dover.nh.gov/Assets/government/city-operations/library/borrow/library-of-things/Blocking%20Mats%20for%20Knit%20and%20Crochet.pdf'
o={k['n']:k for k in old('03_01')}
kinds=[
{"n":"Knitting needles","a":"","d":"Straight, circular and double-pointed knitting needles differ by form and number of points, sold as one needle listing.","s":NE,
 "t":["Straight knitting needle","Circular knitting needle","Double-pointed knitting needle","Interchangeable set","Fixed circular","Bamboo","Metal","Wood"],
 "x":[X("HiyaHiya interchangeable","HiyaHiya",NE,"Stainless steel tips with 6 mm screw join and lifeline holes; ranked first in a four-brand comparison.","",dt="screw join · hard pliable plastic cable"),
      X("ChiaoGoo interchangeable","ChiaoGoo",NE,"Surgical-grade stainless steel with 4 mm fine thread and nylon-coated steel cable; lifeline holes.","",dt="screw join · stiff steel cable"),
      X("Click-lock interchangeable","addi",NE,"German aluminium tips that slide into the cable and twist to lock; no lifeline holes.","",dt="click-lock join"),
      X("KnitPro interchangeable","KnitPro",NE,"Nova Platina metal, wood and birch tips with 5 mm fine screw join.","",dt="metal or wood tips")],
 "m":o['Knitting needles']['m'],"r":o['Knitting needles']['r']},
{"n":"Crochet hook","a":"","d":"Hooked tool made for crochet.","s":o['Crochet hook']['s'],
 "t":["aluminium","steel (thread)","bamboo","ergonomic handle","Tunisian","tapered head","inline head"],
 "x":[X("Amour","Clover",CH,"Brushed-metal hook with rubber handle; ranked top in one decade-long review.","",dt="aluminium head · rubber handle"),
      X("Bamboo hooks","Susan Bates",CH,"Lightweight, budget bamboo hooks sold singly.","",dt="bamboo"),
      X("Odyssey","Furls",CH,"Luxury resin hooks; heavy and since discontinued per the review.","",dt="resin"),
      X("Ergonomic hooks","Boye",CH,"Budget ergonomic set with comfortable handles; visible seams.","",dt="")],
 "m":o['Crochet hook']['m'],"r":o['Crochet hook']['r']},
{"n":"Yarn swift and ball winder","a":"umbrella swift · skein winder","d":"Frame that holds a skein open and winder that turns it into a centre-pull ball.","s":SW,
 "t":["umbrella swift","Swedish wooden swift","centre-pull ball winder","table clamp"],
 "x":[X("Swedish wooden swift and ball winder","The Woolery",SW,"Solid-wood swift with 100 in maximum circumference and 1 lb capacity, paired with a winder making centre-pull balls of up to 4 oz.","",dt="100 in circumference · 4 oz ball")]},
{"n":"Blocking mats and wires","a":"blocking board · T-pins","d":"Foam mats, T-pins and stainless wires used to pin out damp knitting to shape and size.","s":BL,
 "t":["interlocking foam mat","blocking board","T-pins","blocking wires","sock blockers"],
 "x":[X("Wet blocking kit","",BL,"Basin, towels, T-pins and measuring tape; mats and stainless steel wires give straight edges.","",dt="mats · T-pins · wires · spray bottle")]},
{"n":"Stitch markers and knitting notions","a":"row counter · stitch holders","d":"Small markers, counters and holders that keep track of stitches and rows.","s":CC,
 "t":["ring marker","locking marker","progress keeper","row counter","stitch holder","cable needle"],
 "x":[X("Universal Knitting Counter","Clover",CC,"Two-digit row counter whose loop slides on needles US 0-15 and doubles as a stitch marker.","",dt="US 0 to 15 needles")]},
{"n":"Pom-pom maker","a":"","d":"Hand tool made for winding and cutting yarn pom-poms.","s":o['Pom-pom maker']['s'],"t":["plastic ring","fork","clip-on"],"m":[]},
{"n":"Yarn bowl","a":"","d":"Bowl with a slot that holds a ball of yarn while knitting or crocheting.","s":o['Yarn bowl']['s'],"t":["ceramic","wooden"],"m":[]},
]
brands=[
B("HiyaHiya","","","Specialist","stainless needles","Maker of stainless steel interchangeable needles.",s=NE,sig=["HiyaHiya interchangeable"]),
B("ChiaoGoo","","","Specialist","steel needles","Maker of surgical-steel needles with coated cables.",s=NE,sig=["ChiaoGoo interchangeable"]),
B("addi","Germany","","Premium","click-lock needles","German needle brand with the click-lock join.",s=NE,sig=["Click-lock interchangeable"]),
B("KnitPro","India","","Mainstream","needles","Needle brand with metal and wood interchangeable sets.",s=NE,sig=["KnitPro interchangeable"]),
B("Knit Picks","United States","","Own-label & retailer","own-label needles","US yarn retailer with its own needle and hook lines.",sig=["Obsidian","Radiant"],s="knowledge"),
B("Clover","Japan","","Premium","Amour hooks","Japanese notions maker of Amour hooks and knitting counters.",s=CC,sig=["Amour","Universal Knitting Counter"]),
B("Furls","United States","","Premium","luxury hooks","Maker of resin and wood Odyssey and Streamline hooks.",s=CH,sig=["Odyssey"]),
B("Boye","United States","","Mainstream","budget hooks","Hook brand with an ergonomic set.",s=CH,sig=["Ergonomic hooks"]),
B("Susan Bates","United States","","Mainstream","bamboo hooks","Hook brand with lightweight bamboo hooks.",s=CH,sig=["Bamboo hooks"]),
]
write('03_01',kinds,brands,[],"Tulip Etimo, Lantern Moon, Hiya Hiya wire and Knit Picks needle archetypes left out (no retrieved page). Old Knit Picks lists kept as flat models. HiyaHiya Japan, addi Germany: addi per page; HiyaHiya country from knowledge. Pom-pom maker and yarn bowl kept as old kinds, no models.")
