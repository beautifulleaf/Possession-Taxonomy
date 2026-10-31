import json, os
FP="https://www.fashionphile.com/products/"
LVOLD="https://us.louisvuitton.com/eng-us/women/small-leather-goods/all-wallets-and-small-leather-goods/_/N-t164iz3b"
TIF="https://www.tiffany.com/accessories/shop/key-rings/"
def X(n,d,mk,s,y="",v=None,dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk,y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Cardholder","a":"card case · card wallet · card sleeve","d":"Slim holder with card slots and no full note section.",
  "t":["slip cardholder","snap-closure cardholder","pull-tab card sleeve","metal or aluminium card wallet"],"s":LVOLD,
  "x":[
   X("Saint-Sulpice","Flat Goyardine card holder with leather card slots on each side and a middle compartment.","Goyard",FP+"goyard-goyardine-saint-sulpice-card-holder-black-1324093",
     v=[V("Saint-Sulpice, black Goyardine","Goyard","2023","chevron-painted coated canvas, about 4.25 × 2.75 in")],dt="Goyardine colours · leather slot trim · hand-painted personalisation"),
   X("Calvi","Small leather card holder with two card slots.","Hermès","https://www.1stdibs.com/buy/hermes-calvi/",
     v=[V("Calvi Duo","Hermès","","adds a pocket; limited Moulin à Vent edition in Swift"),V("Calvi Verso","Hermès","","contrasting interior colour")],
     dt="Epsom calf · Chèvre Mysore goat · alligator · colourway"),
   X("Pocket Organizer","Coated-canvas card case with card slots and patch pockets inside.","Louis Vuitton",FP+"louis-vuitton-damier-graphite-pocket-organizer-nm-1807992",
     v=[V("Pocket Organizer NM, Damier Graphite","Louis Vuitton","2017","black crossgrain leather interior")],dt="canvas (Damier Graphite, Monogram Eclipse, Monogram Macassar) · interior colour"),
   X("Cardprotector","Aluminium card case that fans cards out with a slide mechanism and blocks skimming; core of Secrid's wallets.","Secrid","https://secrid.com/en-us/collections/the-original/","2010",
     v=[V("Miniwallet","Secrid","2010","first Secrid model built round the Cardprotector"),V("Slimwallet","Secrid"),V("Twinwallet","Secrid")],dt="leather wrap (Original, Crisple, Matte, Vintage) · colour",a="Secrid Miniwallet"),
   X("Ridge Wallet","Front-pocket metal card wallet with a money clip or cash strap, holding up to 12 cards.","Ridge","https://luxe.digital/style/ridge-wallet-review.md","2013",
     v=[V("Aluminium","Ridge","","6061-T6 aluminium, widest colour range"),V("Titanium","Ridge","","grade 5 titanium"),V("Carbon fibre","Ridge","","lightest, 3K weave")],dt="money clip or cash strap · finish"),
   X("Card Sleeve","Slim leather sleeve with two outer slots and a pull-tab main pocket.","Bellroy","https://www.carryology.com/product/bellroy-card-sleeve/",dt="leather colour · 10.3 × 7.1 cm"),
  ],
  "m":[["LV Charms Card Holder","Louis Vuitton"],["Nano Alma Card Holder","Louis Vuitton"],["Recto Verso","Louis Vuitton"],["Romy Card Holder","Louis Vuitton"]]},
 {"n":"Money clip","a":"","d":"Clip that holds folded notes, sometimes with card slots.","t":["solid metal clip","carbon fibre clip","magnetic leather clip","money-clip wallet"],
  "s":"https://www.leatherology.com/blogs/stories/every-wallet-style-explained-bifold-trifold-slim-money-clip-more",
  "x":[X("Bean Money Clip","Sterling silver money clip in Elsa Peretti's bean form.","Tiffany & Co.","https://www.tiffany.ca/jewelry/mens-jewelry/elsa-peretti-bean-money-clip-21450413",
        v=[V("Product 60019776","Tiffany & Co.","","sterling silver, 2 in long")],dt="sterling silver",a="Elsa Peretti Bean money clip")],
  "m":[["Money clip wallet","Ridge"]]},
 {"n":"Coin purse","a":"change purse · porte-monnaie","d":"Small pouch or purse for coins.","t":["zip coin purse","snap coin purse","frame (kiss-lock) purse"],"s":LVOLD,
  "x":[X("Bastia","Change purse cut from one piece of leather, folded origami-style, with a snap.","Hermès","https://www.hermes.cn/cn/en/product/bastia-change-purse-H041054CK89/",
        v=[V("Bastia, Epsom calf","Hermès","","8.5 × 8 cm")],dt="Epsom calf · goatskin · colourway")],
  "m":[["Rosalie Coin Purse","Louis Vuitton"]]},
 {"n":"Key pouch","a":"key case · key holder · key wallet","d":"Small pouch or fold-over case holding keys on an inner ring or hooks.","t":["zip key pouch","fold-over key case"],"s":LVOLD,
  "x":[X("Pochette Clés","Small zipped pouch with a key ring or hook, also used for coins and notes.","Louis Vuitton","https://www.1stdibs.com/buy/louis-vuitton-cles-key-pouch",
        v=[V("Monogram canvas","Louis Vuitton"),V("Epi leather","Louis Vuitton"),V("Monogram Vernis","Louis Vuitton","","e.g. Amarante"),V("Monogram Denim","Louis Vuitton"),V("Monogram Mini Lin","Louis Vuitton")],
        dt="canvas or leather · hardware colour · date code",a="Cles key pouch"),
       X("Multiclés 6","Fold-over key case with six key rings inside.","Louis Vuitton",FP+"louis-vuitton-monogram-6-key-multicles-holder-1892455",
        v=[V("Monogram, 6 key","Louis Vuitton","2017","terra cotta cross-grain leather interior, six brass rings")],dt="canvas · number of rings",a="6 Key Holder")]},
 {"n":"Keyring","a":"key ring · keychain · key fob","d":"Ring or clip that holds keys and is carried on the person.","t":["split ring","key fob","carabiner"],"s":TIF,
  "x":[X("Return to Tiffany tag key ring","Sterling silver key ring with a 'Return to Tiffany' engraved tag.","Tiffany & Co.",TIF,
        v=[V("Heart Tag","Tiffany & Co."),V("Oval Tag Screwball","Tiffany & Co."),V("Round Tag Screwball","Tiffany & Co."),V("Rectangular Tag Screwball","Tiffany & Co."),V("Oval Tag Dangle","Tiffany & Co."),V("Double Heart Tag","Tiffany & Co.","","silver with Tiffany Blue")],
        dt="tag shape · screwball or dangle ring · engraving"),
       X("Elsa Peretti key rings","Sterling silver key rings carrying Elsa Peretti's motifs.","Tiffany & Co.",TIF,
        v=[V("Bean","Tiffany & Co."),V("Open Heart","Tiffany & Co."),V("Teardrop","Tiffany & Co."),V("Eternal Circle","Tiffany & Co.")],dt="motif · sterling silver"),
       X("Tiffany 1837 key rings","Key rings from the Tiffany 1837 line.","Tiffany & Co.",TIF,
        v=[V("Whistle","Tiffany & Co."),V("Makers Valet","Tiffany & Co.","","sterling silver and stainless steel")],dt="sterling silver · steel")]},
 {"n":"Passport cover","a":"passport holder · passport wallet","d":"Cover or wallet made to hold a passport.","t":["slip cover","travel wallet with card slots"],"s":LVOLD,
  "x":[X("Panama passport cover","Cross-grain calf cover with two slip pockets for passport and boarding pass.","Smythson","https://theprojectgarments.com/products/smythson-panama-cross-grain-leather-passport-cover",
        dt="Panama leather (from the 1908 Panama diary) · colour · 10 × 14.5 cm"),
       X("Monogram Passport Cover","Monogram canvas cover with leather interior, card slots and passport pocket.","Louis Vuitton",FP+"louis-vuitton-monogram-passport-cover-1349490",
        v=[V("Monogram, terra cotta interior","Louis Vuitton","2005")],dt="canvas · interior colour · year"),
       X("Passport Cover","Leather passport wallet with card slots, note flap, magnetic closure and RFID shielding.","Bellroy","https://milligram.com/products/bellroy-passport-cover",dt="145 × 100 mm · colour")],
  "m":[["Family Passport Holder","Leatherology"]]},
]
B=lambda **k:{**{"n":"","c":"","f":"","seg":"","d":"","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":""},**k}
brands=[
 B(n="Goyard",c="France",f="1853",seg="Luxury trunks & leather goods",d="Paris trunk maker known for its chevron Goyardine coated canvas.",sig=["Saint-Sulpice"],rel=["Louis Vuitton"],s="https://en.wikipedia.org/wiki/Goyard"),
 B(n="Hermès",c="France",f="1837",seg="Luxury leather goods & fashion",d="Paris house founded by Thierry Hermès, known for leather goods and saddlery.",lines=["Kelly","Birkin","Calvi","Bastia"],eras=["Jean-Louis Dumas, 1978–2005","Pierre-Alexis Dumas, 2005–"],sig=["Calvi","Bastia"],s="https://en.wikipedia.org/wiki/Herm%C3%A8s"),
 B(n="Louis Vuitton",c="France",f="1854",seg="Luxury trunks, leather goods & fashion",d="Paris trunk and leather-goods house; Damier (1888) and Monogram (1896) canvases.",eras=["Marc Jacobs, 1997–2013","Nicolas Ghesquière (women), 2013–","Virgil Abloh (men), 2018–2021","Pharrell Williams (men), 2023–"],sig=["Pocket Organizer","Pochette Clés","Multiclés 6","Monogram Passport Cover"],rel=["Goyard"],s="https://en.wikipedia.org/wiki/Louis_Vuitton"),
 B(n="Tiffany & Co.",c="United States",f="1837",seg="Luxury jewellery & silver",d="New York jeweller and silversmith founded by Charles Lewis Tiffany and John B. Young; owned by LVMH.",lines=["Return to Tiffany","Elsa Peretti","Tiffany 1837"],sig=["Return to Tiffany tag key ring","Bean Money Clip"],s="https://en.wikipedia.org/wiki/Tiffany_%26_Co."),
 B(n="Smythson",c="United Kingdom",f="1887",seg="Luxury stationery & leather goods",d="London stationer founded by Frank Smythson on New Bond Street; royal warrant holder.",sig=["Panama passport cover"],s="https://en.wikipedia.org/wiki/Smythson"),
 B(n="Bellroy",c="Australia",f="2009",seg="Slim wallets & carry",d="Melbourne maker that started with slim wallets; certified B Corporation.",sig=["Card Sleeve","Passport Cover"],s="https://en.wikipedia.org/wiki/Bellroy"),
 B(n="Secrid",c="Netherlands",f="2009",seg="Card protector wallets",d="Dutch wallet maker founded by designers Marianne and René, built round its aluminium Cardprotector.",lines=["Cardprotector","Miniwallet","Slimwallet","Twinwallet"],sig=["Cardprotector"],s="https://www.wipo.int/en/web/ip-advantage/w/stories/secrid-wallets-designing-a-better-world-from-your-pocket"),
 B(n="Ridge",f="2013",seg="Metal minimalist wallets",d="Metal front-pocket wallet maker launched on Kickstarter by Daniel and Paul Kane.",sig=["Ridge Wallet"],s="https://luxe.digital/style/ridge-wallet-review.md"),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"All six planned kinds kept. Tiffany keyrings: eight SKUs regrouped into three archetypes (Return to Tiffany tags, Elsa Peretti motifs, Tiffany 1837). LV Rosalie, LV cardholders and Leatherology passport holder stay as flat models (no retrievable page; louisvuitton.com product pages returned 403 and were not worked around). Left out: Hermès key ring (Carmen) — no page with usable detail retrieved; Ridge money clip as separate archetype (covered as Ridge Wallet option and flat model). No traditions: shelf is brand-led, no artisan tradition specific to it."}
p="/home/user/Possession-Taxonomy/rebuild/work/A4/shelves/01_01.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
