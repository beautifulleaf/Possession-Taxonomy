import json, os
W="https://en.wikipedia.org/wiki/"
EL="EssilorLuxottica"
kinds=[
{"n":"Prescription glasses","a":"prescription spectacles · eyeglasses · prescription sunglasses · spectacle frame",
 "d":"Glasses with lenses made to the wearer's prescription, including tinted prescription sunglasses and frames bought for glazing.",
 "t":["single vision","varifocal (progressive)","bifocal","trifocal","prescription sunglasses","blue-light filter","frame only for glazing"],
 "s":"https://www.warbyparker.com/eyeglasses",
 "m":[["Warby Parker Percey","Warby Parker"],["Warby Parker Durand","Warby Parker"],["Warby Parker Winston","Warby Parker"]],
 "r":[["Ray-Ban",EL],["Oakley",EL],["Persol",EL],["Oliver Peoples",EL],["Vogue Eyewear",EL],["Own frame designs","Specsavers"],["In-house frames","Zenni Optical"]]},
{"n":"Reading glasses","a":"ready-made reading glasses · readers",
 "d":"Glasses with fixed, equal magnifying power in both lenses, sold without a prescription.",
 "t":["full frame","half-eye","folding","blue-light filter","sun readers"],
 "s":"https://www.zennioptical.com/readers",
 "m":[["Foster Grant Camden","Foster Grant"],["Foster Grant Conan","Foster Grant"],["Foster Grant Sawyer","Foster Grant"],["Foster Grant Troy","Foster Grant"]]},
{"n":"Clip-on sunglasses","a":"sunglass clips · clip-ons · flip-ups",
 "d":"Tinted lenses that clip or magnet onto a spectacle frame to turn it into sunglasses.",
 "t":["clip-on","flip-up","magnetic","polarised"],"s":W+"Glasses"},
{"n":"Glasses case","a":"spectacle case · eyeglass case · sunglasses case",
 "d":"Container that stores and protects glasses when not worn.",
 "t":["hard shell","semi-hard shell","soft pouch","folding","multi-pair"],
 "s":"https://www.wikidata.org/wiki/Q2658561",
 "m":[["Leather Sunglasses Case","Smythson"]]},
{"n":"Glasses chain & cord","a":"eyewear retainer · glasses strap · spectacle chain · glasses lanyard",
 "d":"Cord, strap or chain that holds glasses round the neck when not worn.",
 "t":["neoprene retainer","cord","chain","beaded chain","sports strap"],"s":W+"Glasses",
 "x":[{"n":"Croakies","a":"Croakies retainer","d":"Neoprene eyewear retainer loop first cut from an old wetsuit by a Jackson Hole ski patrolman.",
   "mk":"Croakies","y":"1977","s":"https://www.swimoutlet.com/croakies/","v":[],"dt":"neoprene · colours and prints · sizes for temple width"}]}]
brands=[
{"n":"Warby Parker","c":"United States","f":"2010","seg":"Direct-to-consumer optical","d":"New York eyewear brand that designs frames in-house and sells online and through its own stores, with a buy-a-pair, give-a-pair programme.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Warby_Parker"},
{"n":"Specsavers","c":"Guernsey","f":"1984","seg":"Optical and audiology retail chain","d":"Optician chain founded by Doug and Mary Perkins, with about 2,500 stores across the UK, Ireland, Australasia, the Nordics and elsewhere.","lines":["Own frame designs","Licensed collections (Hackett London, Tommy Hilfiger, Converse…)"],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Specsavers"},
{"n":"Zenni Optical","c":"United States","f":"2003","seg":"Online budget optical","d":"Online-only seller of low-priced prescription glasses and sunglasses in its own in-house frames.","lines":["ReMakes by Zenni"],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Zenni_Optical"},
{"n":"Foster Grant","c":"United States","f":"1919","seg":"Mass-market sunglasses and readers","d":"American sunglasses and reading-glasses brand founded by Sam Foster, now part of FGX International under EssilorLuxottica.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["EssilorLuxottica"],"s":W+"Foster_Grant"},
{"n":EL,"c":"France / Italy","f":"2018","seg":"Eyewear group","d":"Franco-Italian group formed by the Essilor–Luxottica merger, owning Ray-Ban, Oakley, Persol, Oliver Peoples and retail chains such as LensCrafters and Sunglass Hut.","lines":["Ray-Ban","Oakley","Persol","Oliver Peoples","Vogue Eyewear","Arnette","Alain Mikli","Foster Grant","Costa Del Mar","Licensed: Prada, Chanel, Armani, Burberry…"],"eras":[],"sig":[],"sc":[],"rel":["Foster Grant"],"s":W+"EssilorLuxottica"},
{"n":"Croakies","c":"United States","f":"1977","seg":"Eyewear retainers","d":"Jackson Hole, Wyoming maker of neoprene eyewear retainers, produced mainly in Bozeman, Montana.","lines":[],"eras":[],"sig":["Croakies"],"sc":[],"rel":[],"s":"https://www.swimoutlet.com/croakies/"},
{"n":"Smythson","c":"","f":"","seg":"Luxury leather goods","d":"Leather-goods maker whose cross-grain leather sunglasses case is a luxury pick in a FashionBeans case round-up.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://www.fashionbeans.com/article/best-glasses-cases"}]
notes=("Merged Prescription sunglasses and Spectacle frame into Prescription glasses as types; Warby Parker trimmed from 8 to 3 models, "
 "market coverage given as ranges (EssilorLuxottica house brands, Specsavers own frames, Zenni in-house frames). Foster Grant readers trimmed 5->4 (dropped The McKay). "
 "No independent test winner could be named: Which? opticians/glasses scores are paywalled. Croakies archetype sourced from a retailer brand page (GearJunkie and Jackson Hole News&Guide were blocked). "
 "Glasses case sourced to Wikidata Q2658561; no named case archetypes added. Smythson brand entry is thin (country/founding not retrieved).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/A4/shelves/02_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
