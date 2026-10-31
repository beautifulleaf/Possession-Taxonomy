import json, os
GD="https://www.glassesdirect.co.uk/buying-guides/help-me-choose/types-of-sunglasses/"
W="https://en.wikipedia.org/wiki/"
T=["sun","polarised","prescription","photochromic","plano"]
def X(n,d,mk,y,s,v=(),a="",dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
kinds=[
{"n":"Aviator frames","a":"aviators · pilot glasses · teardrop frames","d":"Teardrop-shaped metal or acetate frame with a double or triple bridge, worn as sunglasses or with optical lenses.","t":T,"s":W+"Aviator_sunglasses",
 "x":[X("Ray-Ban Aviator","Bausch & Lomb's teardrop pilot sunglass, the originator of the shape, sold under the Ray-Ban name.","Ray-Ban","1937",W+"Aviator_sunglasses",
   [("Anti-Glare prototype","Bausch & Lomb","1936","plastic frame, green lenses"),("Metal-frame redesign","Ray-Ban","1938–39","sources give 1938 and 1939"),("Shooter","Ray-Ban","1938","aviator-family model"),("Outdoorsman","Ray-Ban","1939","aviator-family model"),("Aviator Classic","Ray-Ban","",""),("Aviator Max","Ray-Ban","","")],
   a="Anti-Glare",dt="metal frame · G-15 tempered glass lenses (1953) · lens colours"),
  X("AN6531 Comfort Cable","US Army/Navy standard flying sunglasses with cable temples, made by several contractors.","American Optical","1941",W+"Aviator_sunglasses",
   [("D-1","American Optical","1935","US Army Air Corps predecessor, standardised 13 August 1935"),("MIL-G-6250","","post-war","later issue with F-2 and G-2 lenses")],dt="cable temples · military lens types"),
  X("Original Pilot","American Optical's Flight Goggle 58, made to the US Air Force HGU-4/P standard and sold as the Original Pilot Sunglass.","American Optical","1958",W+"American_Optical",
   [("Flight Goggle 58 (HGU-4/P)","American Optical","1958","issued to pilots from 1959"),("Original Pilot re-release","American Optical","","")],a="Flight Goggle 58 · HGU-4/P"),
  X("Randolph Aviator","Randolph Engineering's MIL-SPEC HGU-4/P-style aviator, made in Massachusetts as US military prime contractor.","Randolph Engineering","1982",W+"Randolph_Engineering",[],dt="bayonet or skull temples · lens tints"),
  X("Persol 649","Large-lens acetate pilot frame designed for Turin tram drivers, made famous by Marcello Mastroianni.","Persol","1957",W.replace("en.wikipedia.org/wiki/","www.gearpatrol.com/style/a724428/persol-sunglasses-brand-breakdown/") if False else "https://www.gearpatrol.com/style/a724428/persol-sunglasses-brand-breakdown/",
   [("649 Original","Persol","1957","wider profile, thicker temples"),("PO9649S","Persol","","slimmer, less prominent bridge")],dt="acetate colours · Silver Arrow hinge · Meflecto temples")]},
{"n":"Trapezoid frames","a":"Wayfarer-style · trapezoidal frames","d":"Frame wider at the top than the bottom, usually in thick acetate or plastic.","t":T,"s":GD,
 "x":[X("Wayfarer","Raymond Stegeman's trapezoidal acetate frame for Bausch & Lomb, the defining plastic sunglass shape.","Ray-Ban","1952",W+"Ray-Ban_Wayfarer",
   [("Original Wayfarer B&L5022","Bausch & Lomb","1952","original"),("B&L5024","Bausch & Lomb","","about 2 mm wider at the bridge"),("New Wayfarer RB2132","Ray-Ban","2001","smaller, injected plastic"),("Original Wayfarer RB2140","Ray-Ban","2007","reintroduction with Ray-Ban logo studs"),("Classic Wayfarer RB5121","Ray-Ban","",""),("Original Wayfarer Classic","Ray-Ban","",""),("New Wayfarer Classic","Ray-Ban","",""),("Mega Wayfarer","Ray-Ban","",""),("Wayfarer Puffer","Ray-Ban","",""),("Dealan","Jacques Marie Mage","2015","Wayfarer-style interpretation in plant-based acetate")],
   dt="sizes · acetate colours · lens type")]},
{"n":"Round & panto frames","a":"round glasses · panto · Windsor","d":"Frame with circular or near-circular lenses, or panto lenses rounded below a flatter top.","t":T,"s":GD,
 "x":[X("Windsor glasses","Thin metal frame with circular eyerims, a saddle bridge and centre-mounted temples.","","1840s",W+"Windsor_glasses",[("Teashades","","","tinted version")],a="Gandhi glasses · John Lennon glasses · granny glasses",dt="wire metal · gold, silver · tint"),
  X("Lemtosh","Moscot's rounded acetate frame from the Lower East Side optician.","Moscot","",W+"Moscot",[],dt="acetate colours · sizes"),
  X("O'Malley","Oliver Peoples acetate frame seen in The Jackal and American Psycho.","Oliver Peoples","by 1997",W+"Oliver_Peoples",[("O'Malley Sun","Oliver Peoples","1997","worn in The Jackal"),("O'Malley","Oliver Peoples","2000","worn in American Psycho")]),
  X("Gregory Peck","Oliver Peoples eponymous line based on the frames Gregory Peck wore in To Kill a Mockingbird.","Oliver Peoples","2012",W+"Oliver_Peoples",[])]},
{"n":"Square & rectangular frames","a":"square glasses · rectangular frames","d":"Frame with square or rectangular lenses.","t":T,"s":GD,
 "x":[X("Caravan","Ray-Ban metal pilot frame with squarer lenses than the Aviator.","Ray-Ban","1950s",W+"Ray-Ban",[],a="Echelon")]},
{"n":"Cat-eye frames","a":"cat-eye glasses · Harlequin frames","d":"Frame that sweeps upward at the outer top corners.","t":T,"s":W+"Cat_eye_glasses",
 "x":[X("Harlequin frame","Altina Schinasi's upswept frame named after the Harlequin mask, the origin of the cat-eye.","Altina Schinasi","",W+"Cat_eye_glasses",
   [("Ful-Vue","American Optical","1931","precursor with hinges on the upper frame"),("Lugene production","Lugene","","first commercial frames"),("Claire McCardell line","American Optical","1952","first eyewear line by a fashion designer")])]},
{"n":"Browline frames","a":"browlines · combination frames · Clubmaster-style","d":"Frame with a bold upper brow and a thin metal or rimless lower part.","t":T,"s":W+"Browline_glasses",
 "x":[X("Ronsir","Shuron's acetate-brow, metal-rim frame with interchangeable parts, the originator of the browline.","Shuron","1947",W+"Browline_glasses",
   [("Supra","Neville Chappell","pre-1939","British precursor, licensed by Shuron"),("Ronsir","Shuron","","current US-made version")],dt="ebony, tortoise, clear brow · metal and acetate"),
  X("Clubmaster","Ray-Ban browline sunglass revived for 1980s demand.","Ray-Ban","mid-1980s",W+"Browline_glasses",[("Clubmaster Classic","Ray-Ban","",""),("New Clubmaster","Ray-Ban","","")]),
  X("Clubman","Art-Craft Optical's men's browline in its Art-Rim range.","Art-Craft Optical","",W+"Browline_glasses",[("Leading Lady","Art-Craft Optical","","women's counterpart")]),
  X("Wayfarer Max","Ray-Ban monobrowline of the 1980s.","Ray-Ban","1980s",W+"Browline_glasses",[])]},
{"n":"Geometric frames","a":"hexagonal · octagonal · angular frames","d":"Frame with hexagonal, octagonal or other many-sided lenses.","t":T,"s":GD,
 "m":[["Hexagonal Flat Lenses","Ray-Ban"],["Jim","Ray-Ban"],["Marshal II","Ray-Ban"]]},
{"n":"Rimless & semi-rimless frames","a":"rimless glasses · drilled frames · half-rims","d":"Frame with drilled lenses fixed directly to bridge and temples, or a half-rim holding lenses with nylon thread.","t":T,"s":W+"Silhouette_(eyewear)",
 "x":[X("Titan Minimal Art","Silhouette's screwless, hingeless rimless titanium frame, certified for space travel.","Silhouette","",W+"Silhouette_(eyewear)",[],dt="titanium · lens shapes · colours"),
  X("Santos de Cartier","Cartier eyewear with temple screws taken from the Santos watch bezel.","Cartier","1983","https://www.eye-oo.com/en-us/blogs/highlights/spotlight-on-cartier-the-timeless-appeal-of-the-santos-de-cartier-eyewear",[],dt="titanium, 22-carat gold, buffalo horn"),
  X("Décor C de Cartier","Cartier frames carrying the house's C initial on the temples.","Cartier","","https://www.cartier.com/en-us/bags-and-accessories/sunglasses/decor-c-de-cartier/",[("Décor precious","Cartier","","white gold and diamonds")],a="C Décor",dt="gold, rose gold, platinum tones · lens tints incl. photochromic")]},
{"n":"Shield & wrap sunglasses","a":"shields · wraparounds · sport sunglasses","d":"Sunglasses with a single shield lens or lenses curved round the face, mostly for sport.","t":T,"s":"https://en.wikipedia.org/wiki/Oakley,_Inc.",
 "x":[X("Factory Pilot Eyeshades","Oakley's first sunglasses, a goggle-like sport shade.","Oakley","1984","https://en.wikipedia.org/wiki/Oakley,_Inc.",[]),
  X("Frogskins","Oakley's first lifestyle frame and first dual-lens design.","Oakley","1985","https://www.sportrx.com/blog/oakley-frogskins-collection/",
   [("Frogskins re-release","Oakley","2007","O Matter frame, molded hinges"),("Frogskins Mix","Oakley","","steel temples"),("Frogskins Lite","Oakley","","semi-rimless"),("Frogskins XS","Oakley","","smaller fit"),("Frogskins Rx","Oakley","","for prescription lenses")]),
  X("M Frame","Oakley's interchangeable-lens sport shield, launched as the Mumbo.","Oakley","1989","https://www.revantoptics.com/blogs/the-lens/history-of-oakley-m-frame",
   [("Mumbo","Oakley","1989","V, 67 and Hybrid lenses"),("M Frame Strip, Sweep, Heater","Oakley","1991","new lens shapes"),("M2 Frame","Oakley","2014","")],a="Mumbo",dt="lens shape · lens tint"),
  X("Eye Jacket","Oakley's dual-lens wraparound, its first design done fully in CAD.","Oakley","1994","https://www.dazeddigital.com/fashion/article/43908/1/oakley-eye-jacket-jim-jannard-90s-sunglasses",[("Eye Jacket Redux","Oakley","","reissue")]),
  X("Radar","Oakley's single-shield sport sunglass built on the M Frame idea.","Oakley","2006","https://www.revantoptics.com/blogs/the-lens/history-and-differences-of-oakley-radar",
   [("Radar XL","Oakley","2006",""),("Radarlock","Oakley","2012","new lens lock"),("Radar EV","Oakley","2015","taller lens")],dt="lens shape (Path, Pitch) · Prizm lenses")]},
{"n":"Folding sunglasses","a":"foldable sunglasses","d":"Sunglasses that fold at the bridge as well as the temples to pack small.","t":T,"s":"https://www.gearpatrol.com/style/a724428/persol-sunglasses-brand-breakdown/",
 "x":[X("Persol 714","Persol's first folding sunglass, a slimmer 649 hinged at bridge and temples, worn by Steve McQueen.","Persol","","https://www.gearpatrol.com/style/a724428/persol-sunglasses-brand-breakdown/",
   [("714 Steve McQueen","Persol","","polarised lenses, Supreme Arrow hinges")],dt="acetate colours · polarised or not"),
  X("Wayfarer Folding","Folding version of the Ray-Ban Wayfarer.","Ray-Ban","by 2007",W+"Ray-Ban_Wayfarer",[])]},
]
def B(n,c,f,seg,d,s,lines=(),sig=(),rel=(),eras=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
B("Ray-Ban","United States","1936","Mainstream sunglasses","Bausch & Lomb's sunglass brand, now owned by EssilorLuxottica and based in Milan.",W+"Ray-Ban",["Ray-Ban Stories"],["Ray-Ban Aviator","Wayfarer","Clubmaster","Caravan","Olympian"],["Persol","Oliver Peoples","Oakley"],["Bausch & Lomb, from 1936","Luxottica (EssilorLuxottica), later"]),
B("American Optical","United States","1833","Heritage optical maker","Optical maker that supplied US military aviator sunglasses from 1935.",W+"American_Optical",[],["Original Pilot","AN6531 Comfort Cable"],["Randolph Engineering"]),
B("Randolph Engineering","United States","1973","Heritage aviator maker","Randolph, Massachusetts maker of military-specification aviators and shooting glasses.",W+"Randolph_Engineering",["Ranger shooting glasses"],["Randolph Aviator"],["American Optical"]),
B("Persol","Italy","1917","Heritage luxury sunglasses","Turin sunglass house founded by Giuseppe Ratti, known for the Silver Arrow and folding frames.",W+"Persol",[],["Persol 649","Persol 714"],["Ray-Ban"]),
B("Moscot","United States","1915","Heritage optician","Lower East Side New York optician and frame maker founded by Hyman Moscot.",W+"Moscot",[],["Lemtosh"],[]),
B("Oliver Peoples","United States","1986","Luxury optical","Los Angeles frame maker, now part of EssilorLuxottica.",W+"Oliver_Peoples",[],["O'Malley","Gregory Peck"],["Ray-Ban","Persol"]),
B("Shuron","United States","1865","Heritage optical maker","American frame maker that launched the Ronsir browline in 1947.","https://theallamericanshades.com/en/shuron/",["Freeway","MacArthur","Sportivo"],["Ronsir"],["American Optical"]),
B("Cartier","France","1847","Luxury house","Paris jeweller that added eyewear in the 1980s in gold, platinum and buffalo horn.","https://en.wikipedia.org/wiki/Cartier_(jeweler)",[],["Santos de Cartier","Décor C de Cartier"],[]),
B("Silhouette","Austria","1964","Lightweight optical","Linz maker of rimless titanium frames founded by Anneliese and Arnold Schmied.",W+"Silhouette_(eyewear)",[],["Titan Minimal Art"],[]),
B("Jacques Marie Mage","United States","2014","Independent luxury eyewear","Los Angeles brand of limited-run frames made in Japan and Italy, founded by Jérôme Mage.",W+"Jacques_Marie_Mage",[],["Dealan"],[]),
B("Gentle Monster","South Korea","2011","Fashion eyewear","Seoul brand of oversized, often avant-garde sunglasses and optical frames.",W+"Gentle_Monster",[],[],[]),
B("Oakley","United States","1975","Sport eyewear","Californian sport-eyewear maker founded by Jim Jannard, known for shields and wraparounds.","https://en.wikipedia.org/wiki/Oakley,_Inc.",[],["Frogskins","M Frame","Eye Jacket","Radar"],["Ray-Ban"]),
]
notes=("All 7 old kinds kept (renamed to frame-shape kinds that cover sun and optical); 3 new kinds added (rimless, shield & wrap, folding). "
"Ray-Ban SKUs folded into Aviator, Wayfarer and Clubmaster versions; Ray-Ban hexagonal models stay in m (no sourced geometric archetype). "
"Left out: Gentle Monster and Jacques Marie Mage geometric archetypes (no retrieved page names a signature geometric model; JMM Dealan added as a Wayfarer interpretation, Gentle Monster brand only); "
"Persol 714 and Lemtosh launch years (not on retrieved pages); Titan Minimal Art 1999 date (snippet only); Frogskins placed in Shield & wrap per plan though it is a dual-lens lifestyle frame; "
"Ray-Ban Olympian (shape not confirmed). Cartier rimless status of Santos/Décor C not stated on fetched pages; placed per plan.")
os.makedirs("work/A4/shelves",exist_ok=True)
p="work/A4/shelves/02_00.json"; tmp=p+".tmp"
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open(tmp,"w"),ensure_ascii=False,indent=1); os.replace(tmp,p)
print("archetypes",sum(len(k.get("x",[])) for k in kinds))
