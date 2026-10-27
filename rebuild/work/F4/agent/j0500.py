import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/F4/agent')
from w import save
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Kamidana","a":"household Shinto altar","d":"Miniature wall-mounted household altar enshrining a kami, usually with a mirror and ofuda.","t":["ichisha (one-door)","sansha (three-door)","wall shelf"],"s":W+"Kamidana",
 "x":[{"n":"Wall-mounted kamidana","a":"","d":"Small shrine mounted high on a wall; the shintai is most often a small round mirror, with ofuda and offerings of water, sake or food.","mk":"","y":"","s":W+"Kamidana","dt":"wood · mirror · ofuda · mizutama water vessel"}],"m":[]},
{"n":"Ofuda","a":"shrine talisman · jingu taima","d":"Talisman of paper, wood, cloth or metal issued by a shrine or temple and kept on a household altar.","t":["kamifuda (paper)","kifuda (wood)","shinsatsu","purpose-specific (doorway, kitchen)"],"s":W+"Ofuda",
 "x":[{"n":"Jingu Taima","a":"Ise talisman","d":"Talisman issued by the Ise Grand Shrines, a wooden tablet with a cedar sliver wrapped in paper; often the first placed on a household altar.","mk":"","y":"spread Edo period","s":W+"Ofuda","dt":"wooden tablet · cedar sliver (gyoshin) · paper wrapper"}],"m":[]},
{"n":"Protective charm","a":"omamori · evil-eye charm","d":"Small charm carried, not worn as jewellery, for luck, protection or a named blessing. A worn one is in Jewellery; one issued for money is in Coins, Stamps, Medals & Trading Cards.",
 "t":["traffic safety","avoiding evil","open luck","education","business prosperity","love and marriage","pregnancy","family safety","evil-eye bead","hamsa"],"s":"https://www.ebay.de/itm/405433204553",
 "x":[{"n":"Omamori","a":"","d":"Amulet sold at Shinto shrines and Buddhist temples, usually a brocade silk bag enclosing a paper or wood prayer; replaced yearly.","mk":"","y":"","s":W+"Omamori","dt":"brocade bag · paper or wood inside"},
 {"n":"Nazar","a":"evil-eye bead · nazar boncugu","d":"Eye-shaped handmade glass amulet, blue and white, against the evil eye.","mk":"","y":"records from 16th century BCE","s":W+"Nazar_(amulet)","dt":"glass · concentric circles"},
 {"n":"Hamsa","a":"Hand of Fatima","d":"Palm-shaped amulet against the evil eye, often with an eye motif, worn or hung on walls.","mk":"","y":"","s":W+"Hamsa","dt":"silver, jet, tile, painted"}],"m":[["Omamori",""]]},
{"n":"Ema","a":"votive plaque","d":"Wooden plaque on which a wish is written, left at a shrine; the other side bears a picture.","t":["standard plaque","zodiac-year ema","large votive ema"],"s":W+"Omamori","m":[]},
{"n":"Omikuji","a":"fortune slip","d":"Paper fortune slip drawn at a shrine or temple for a small offering.","t":["dai-kichi to kyo grades","with charm"],"s":W+"O-mikuji","m":[]},
{"n":"Paper-streamer wand","a":"gohei · kinpei","d":"Wand of zigzag paper or metal-foil streamers set at a shrine or household altar as the sign of the kami's presence (gohei, kinpei named forms).","t":["gohei (two shide)","onusa (many shide)","kinpei"],"s":W+"Gohei","m":[]},
{"n":"Shrine rope","a":"shimenawa","d":"Rope hung to mark a sacred space or object in a rite. A seasonal festival decoration such as the kadomatsu is in Decor.","t":["hemp","rice straw","with shide","household kamidana size"],"s":W+"Shimenawa","m":[]},
{"n":"Ritual lantern","a":"bon lantern · votive stone toro","d":"Lantern made to be hung or set out in a rite or as a shrine offering. A garden stone lantern or decorative lantern is in Decor; a lantern made to be carried as a light is in Lighting.","t":["stone toro","bronze toro","hanging tsuri-doro","floating Obon lantern"],"s":W+"Stone_lantern","m":[]}
]
save('05_00',{"kinds":kinds,"brands":[],"traditions":[],"notes":"Ema sourced to Omamori page only as a search snippet described it, but the Omamori page itself does not describe ema - REVIEW. Chochin not covered. Ichisha/sansha not on the Kamidana page (listed as types only)."})
