import json, os
W='https://en.wikipedia.org/wiki/'
FP='https://www.fashionphile.com/blogs/academy/louis-vuitton-pochette-accessories'
FN='https://bd.fashionnetwork.com/news/Bottega-Veneta-celebrates-its-Knot-clutch-bag,667050.html'
RB='https://www.rebag.com/thevault/?p=10304'
MET='https://thefemin.com/2022/04/louis-vuitton-pochette-metis-bags/'
kinds=[
 {"n":"Clutch bag","a":"clutch · evening clutch","d":"Small firm handle-less bag carried in the hand or under the arm, often with an optional strap.",
  "t":["envelope clutch","frame clutch","oversized clutch","box clutch"],"s":W+"Handbag",
  "x":[
   {"n":"Knot","a":"Knot clutch · Knot minaudière","d":"Curvy small Bottega Veneta clutch closed by a clasp shaped like a leather knot.",
    "mk":"Bottega Veneta","y":"2001","s":FN,
    "v":[{"n":"Pre-Knot clutches","mk":"Bottega Veneta","y":"1980s–1990s","d":"archive forerunners shown in the 2016 retrospective"},
         {"n":"Knot (Tomas Maier clasp)","mk":"Bottega Veneta","y":"2001","d":"knot-shaped clasp that named the bag"},
         {"n":"Knot Origami","mk":"Bottega Veneta","y":"","d":"pleated varnished leather"},
         {"n":"Knot Jardin","mk":"Bottega Veneta","y":"","d":"decorated with leather flowers"},
         {"n":"Knot Vintage Jewel","mk":"Bottega Veneta","y":"","d":"antique crystal embroidery"},
         {"n":"Knot Memory","mk":"Bottega Veneta","y":"","d":"plaited nappa leather"},
         {"n":"Knot Metallic Lace","mk":"Bottega Veneta","y":"","d":"two metallic lace frames"}],
    "dt":"intrecciato or plain leather · metallic, crystal, embroidered and limited editions · knot clasp"},
   {"n":"The Pouch","a":"Pouch clutch","d":"Oversized soft gathered leather clutch, one of Daniel Lee's first Bottega Veneta designs.",
    "mk":"Bottega Veneta","y":"c. 2019","s":RB,
    "v":[{"n":"The Pouch (large)","mk":"Bottega Veneta","y":"","d":"classic oversized size"},
         {"n":"Mini Pouch","mk":"Bottega Veneta","y":"","d":"smaller size"}],
    "dt":"size large · mini · leather colours"},
   {"n":"Lauren 1980","a":"","d":"Intrecciato clutch named after the bag carried by Lauren Hutton in American Gigolo (1980).",
    "mk":"Bottega Veneta","y":"1980; revived 2016","s":W+"Bottega_Veneta",
    "v":[{"n":"Lauren 1980 revival","mk":"Bottega Veneta","y":"2016","d":"reissued for the house's 50th-anniversary show"}],
    "dt":"intrecciato leather · colours"}],
  "m":[["Curve","Jimmy Choo"],["T-Lock","Toteme"]]},
 {"n":"Pochette","a":"pochette accessoires · accessory pouch","d":"Small flat bag with a short strap or chain, carried alone or clipped inside a larger bag.",
  "t":["chain pochette","strap pochette","multi-pouch set"],"s":FP,
  "x":[
   {"n":"Pochette Accessoires","a":"LV Pochette","d":"Small zip-top Louis Vuitton pouch with a short strap, first an insert for the Monogram bucket bag.",
    "mk":"Louis Vuitton","y":"1992","s":FP,
    "v":[{"n":"Pochette Accessoires (original)","mk":"Louis Vuitton","y":"1992","d":"insert in the Monogram bucket bag, later sold alone"},
         {"n":"Pochette Accessoires NM","mk":"Louis Vuitton","y":"2012","d":"longer strap, interior pocket, stiffer base"},
         {"n":"Mini Pochette Accessoires","mk":"Louis Vuitton","y":"","d":"compact version"},
         {"n":"Multi Pochette Accessoires","mk":"Louis Vuitton","y":"","d":"several pouches with interchangeable straps"},
         {"n":"Maxi Multi Pochette Accessoires","mk":"Louis Vuitton","y":"","d":"slightly larger multi-pouch set"}],
    "dt":"canvas Monogram, Damier Ebène, Damier Azur, Monogram Multicolor · Epi leather · artist editions (Stephen Sprouse, Takashi Murakami)"},
   {"n":"Pochette Métis","a":"Metis","d":"Compact Louis Vuitton flap bag with a trunk-style lock, derived from the 1986 Monceau.",
    "mk":"Louis Vuitton","y":"2012","s":MET,
    "v":[{"n":"Monceau (forerunner)","mk":"Louis Vuitton","y":"1986","d":"source silhouette"},
         {"n":"Pochette Métis","mk":"Louis Vuitton","y":"2012","d":"front pocket merged into the body"},
         {"n":"Pochette Métis 10th-anniversary model","mk":"Louis Vuitton","y":"2022","d":"19 × 25 × 7 cm, top handle and shoulder strap"}],
    "dt":"Monogram · Monogram Reverse · full leather · personalised lining and trim"}]},
 {"n":"Minaudière","a":"vanity case · minaudiere","d":"Small rigid, often jewelled evening case, hinged at the base, carried in the hand.",
  "t":["metal","crystal-covered","enamel","figural (novelty shape)"],"s":W+"Handbag",
  "x":[
   {"n":"Minaudière (Van Cleef & Arpels)","a":"vanity case","d":"Jewelled metal evening case with compartments for make-up, watch and keys; the originating design.",
    "mk":"Van Cleef & Arpels","y":"1934","s":W+"Minaudi%C3%A8re",
    "v":[{"n":"Original minaudière","mk":"Van Cleef & Arpels","y":"1934","d":"credited to Charles Arpels"}],
    "dt":"precious metal · gems · fitted compartments"},
   {"n":"Judith Leiber crystal minaudière","a":"Leiber minaudière","d":"Metal-shell evening bag covered in crystals, often in figural shapes such as animals and food.",
    "mk":"Judith Leiber","y":"1963 onwards","s":W+"Judith_Leiber",
    "v":[{"n":"Cupcake","mk":"Judith Leiber","y":"","d":"figural minaudière"},
         {"n":"Socks","mk":"Judith Leiber","y":"","d":"figural minaudière"}],
    "dt":"shape (animal, fruit, food, geometric) · silver or gold plating · crystal colours"}]},
 {"n":"Wristlet bag","a":"wristlet","d":"Small bag with a short wrist strap and its own inner compartment, unlike a wristlet wallet.","s":W+"Handbag"}
]
brands=[
 {"n":"Louis Vuitton","c":"France","f":"1854","seg":"Luxury fashion house","d":"Paris trunk-maker turned leather-goods and fashion house, part of LVMH.",
  "lines":["Monogram canvas","Damier canvas"],"eras":["Marc Jacobs, 1997–2013","Nicolas Ghesquière (women's), 2013–","Virgil Abloh (men's), 2018–2021","Pharrell Williams (men's), 2023–"],
  "sig":["Pochette Accessoires","Pochette Métis"],"sc":[],"rel":[],"s":W+"Louis_Vuitton"},
 {"n":"Bottega Veneta","c":"Italy","f":"1966","seg":"Luxury leather goods","d":"Vicenza-founded house known for intrecciato woven leather.",
  "lines":["Intrecciato"],"eras":["Renzo Zengiaro, 1966–1970s","Laura Braggion, 1980s–2001","Tomas Maier, 2001–2018","Daniel Lee, 2018–2021","Matthieu Blazy, 2021–2024","Louise Trotter, 2024–"],
  "sig":["Knot","The Pouch","Lauren 1980"],"sc":[],"rel":[],"s":W+"Bottega_Veneta"},
 {"n":"Van Cleef & Arpels","c":"France","f":"1896","seg":"High jewellery","d":"Paris jeweller credited with inventing the minaudière.",
  "lines":[],"eras":[],"sig":["Minaudière (Van Cleef & Arpels)"],"sc":[],"rel":[],"s":W+"Van_Cleef_%26_Arpels"},
 {"n":"Judith Leiber","c":"United States","f":"1963","seg":"Luxury evening bags","d":"Label founded by Hungarian-American designer Judith Leiber, famed for crystal minaudières.",
  "lines":[],"eras":["Judith Leiber, 1963–1998"],"sig":["Judith Leiber crystal minaudière"],"sc":[],"rel":[],"s":W+"Judith_Leiber"},
 {"n":"Jimmy Choo","c":"United Kingdom","f":"1996","seg":"Luxury shoes and accessories","d":"London house making shoes, handbags and accessories, owned by Capri Holdings.",
  "lines":[],"eras":["Sandra Choi (creative director), 2013–"],"sig":[],"sc":[],"rel":[],"s":W+"Jimmy_Choo_Ltd"}
]
notes=("Kept all three old kinds (Clutch bag, Minaudière, Wristlet bag) and added Pochette. Toteme T-Lock and Jimmy Choo Curve stay as models: "
 "no attestation page retrievable without stealth proxies (hypebae, mytheresa, purseblog blocked/empty), so no archetypes or Toteme brand entry. "
 "Jimmy Choo Bon Bon left out (only search snippets). Pouch 20 size name left out (source page not retrievable); Pouch year given as c. 2019 from the rebag guide (Lyst 2019, Daniel Lee's first designs). "
 "Mini Pochette launch year unconfirmed so blank. No craft traditions apply to this shelf. Wristlet bag has no archetypes (no named icons found).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/A4/shelves/00_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
