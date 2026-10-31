import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
kinds=[
{"n":"Flip-flop","a":"thong sandal · thongs · jandals","d":"Flat sandal held only by a toe post between the first two toes and a strap from it to the sides of the sole.",
 "t":["rubber","EVA foam","leather"],"s":W+"Flip-flops",
 "x":[X("Havaianas","Havaianas flip-flop","Brazilian rubber flip-flop inspired by the Japanese zōri, launched by Alpargatas in 1962.","Havaianas","1962",W+"Havaianas",
     [("Top","Havaianas","","plain single-colour model"),("Havaianas Brazil","Havaianas","1998","made for the 1998 FIFA World Cup"),("Brasil Logo","Havaianas","","flag on strap"),
      ("Slim","Havaianas","","narrow straps"),("Square","Havaianas","","square-toe sole"),("Luna","Havaianas","",""),("Urban","Havaianas","","")],
     "rubber sole and straps · colours · prints"),
    X("Gizeh","Birkenstock Gizeh","Birkenstock thong sandal on the cork-latex footbed with a single buckled strap.","Birkenstock","1983",W+"Birkenstock",[],"leather, Birko-Flor, EVA · regular or narrow fit")],
 "m":[["'Ohana","OluKai"],["Ulele","OluKai"]]},
{"n":"Slide","a":"slider · pool slide · slide sandal","d":"Backless sandal with one or more bands or straps over the front of the foot.",
 "t":["single band","two-strap","recovery foam"],"s":"https://www.famousfootwear.com/browse/shoes/mens/sandals/athletic-slides",
 "x":[X("Adilette","adidas slides","Moulded one-band shower slide developed by Adi Dassler, introduced in 1972 for the West German football team.","adidas","1972",
     "https://www.80scasualclassics.co.uk/blogs/blog/slide-away-everything-you-need-to-know-about-the-adidas-adilette",
     [("Adilette Aqua","adidas","","all-moulded water slide"),("Adilette CF+","adidas","","")],"three-stripe band · colourways"),
    X("Madrid","Birkenstock Madrid","Birkenstock's first footbed sandal: a single-strap slide, launched as a gymnastics sandal in 1963 and named Madrid in 1979.","Birkenstock","1963",W+"Birkenstock",
     [],"one strap with pin buckle · leather, Birko-Flor"),
    X("Arizona","Birkenstock Arizona","Two-strap buckled slide on the cork-latex footbed; Birkenstock's most popular sandal.","Birkenstock","1973",W+"Birkenstock",
     [("Furkenstock","Céline","2012","Phoebe Philo runway recreation with mink-lined footbed"),("Valentino collaboration","Birkenstock","2019",""),("Birkenstock EVA","Birkenstock","2015","lightweight waterproof EVA versions")],
     "regular or narrow fit · leather, suede, Birko-Flor, EVA · soft footbed"),
    X("Oran","Hermès Oran","Flat leather slide with an H-shaped cut-out upper, designed by Pierre Hardy for Hermès.","Hermès","1997",W+"Pierre_Hardy_(fashion_designer)",[],"calfskin, suede, exotic leathers · colours")],
 "m":[["OOahh Slide","Oofos"],["ORA Recovery Slide","Hoka"],["Fluff Yeah Slide","UGG"],["Ultra Comfort","Nike"],["PureAlign Recharge","New Balance"],["Fraisier","Lacoste"],["Darwyn Cross Band","Rockport"]]},
{"n":"Flat strap sandal","a":"T-strap sandal · T-bar sandal","d":"Flat sandal held by straps across or round the foot, including one with a toe loop or T-strap.",
 "t":["T-bar","ankle strap","back strap"],"s":W+"Sandal",
 "x":[X("Fisherman sandal","T-bar sandal","Closed-toe T-bar sandal with leather bands over the toes, originally for men and boys; appears to have originated in France.","","",W+"Sandal",[],"leather bands · buckle"),
    X("Salt-Water sandal","Saltwater sandal","Waterproof leather fisherman-style sandal developed in the 1940s and still made on 1940s machinery in St Louis, Missouri.","","1940s",
      "https://www.salt-watersandals.co.uk/blogs/journal/tap-into-the-fisherman-sandals-trend-with-salt-water-shark-originals",[("Shark Original","","","hand-finished, waterproof leather")],"leather · colours"),
    X("Jelly sandal","jellies · jelly shoe","PVC version of the fisherman sandal, invented by Jean Dauphant in 1946 during a post-war leather shortage.","","1946",W+"Sandal",
      [("Jelly Shoes fashion jellies","","1980","Paris company that made jellies a colourful fashion item"),("Melissa","Grendene","1982","Brazilian licensed production"),("Grendha","Grendene","1983","")],"translucent or glitter PVC · colours"),
    X("Ho Chi Minh sandal","dép lốp · tyre sandal · Ho Chis","Sandal cut from discarded tyres, worn by Viet Cong soldiers in the Vietnam War.","","Vietnam War era",W+"Ho_Chi_Minh_sandals",[],"tyre sole · rubber straps")],
 "m":[["Milano","Birkenstock"],["Mayari","Birkenstock"]]},
{"n":"Sports and outdoor sandal","a":"sport sandal · hiking sandal · river sandal","d":"Sandal with adjustable straps on a treaded sole, made for walking, hiking and water.",
 "t":["open toe","closed toe (toe bumper)","webbing straps"],"s":"https://rei.com/c/womens-sport-sandals",
 "x":[X("Teva Original Sandal","Teva Original Universal","Webbing-strap sport sandal created by river guide Mark Thatcher in 1984, the first sport sandal with an ankle strap.","Teva","1984",
     "https://ir.deckers.com/news-events/press-releases/detail/572/teva-invigorates-timeless-sandal-silhouettes-with-limited-edition-offering",
     [("Original Sandal","Teva","1984","first Teva design"),("Original Universal","Teva","","Universal strapping, contoured EVA topsole"),("Mush Universal","Teva","","Universal straps on Mush flip-flop platform"),("Hurricane XLT","Teva","","sport-hiking family; Hurricane XLT3 later")],
     "nylon webbing · colours and prints"),
    X("Chaco Z/1","Z/1 Classic","Sport sandal with one adjustable strap looped through the sole, created by guide Mark Paigen.","Chaco","1989",W+"Chaco_(footwear)",
     [("Z/1 Classic","Chaco","",""),("Z/2 Classic","Chaco","","adds toe loop"),("ZX/2 Classic","Chaco","",""),("Mega Z/Cloud","Chaco","","thicker cushioned straps")],"webbing patterns · footbed"),
    X("Keen Newport","Newport","Closed-toe sport sandal with a rubber toe bumper, Keen's first design, shown in autumn 2003.","Keen","2003",
     "https://keenfootwear.ca/blogs/keen-blog/20-wild-years-of-the-newport-sandal",
     [("Newport H2","Keen","","water version"),("Newport Retro","Keen","",""),("Newport Slide","Keen","",""),("Newport Boundless","Keen","","children's")],"toe bumper · bungee lace · colours")],
 "m":[["Tirra","Teva"],["Terra Fi 5 Universal","Teva"],["UNEEK","Keen"],["Whisper","Keen"],["Atacama","Birkenstock"],["Hopara","Hoka"],["Cairn Evo","Bedrock Sandals"],["PFD Sandals","Astral"]]},
{"n":"Gladiator sandal","a":"Roman sandal · Grecian sandal","d":"Flat or low sandal with multiple straps up the foot or leg.",
 "t":["ankle height","calf height","knee height"],"s":W+"Sandal",
 "x":[X("Grecian sandal","Greek sandal","Flat sandal from Greece and Salento with interlaced straps over the toes and instep.","","",W+"Sandal",[],"leather straps · lacing height"),
    X("Roman sandal","solea · caliga","Strapped Roman sandal, from the indoor solea to the heavy-soled military caliga sandal-boot.","","",W+"Sandal",[],"leather · hobnailed sole (caliga)")]},
{"n":"Huarache","a":"woven leather sandal · guarache","d":"Mexican sandal with a hand-woven leather upper.",
 "s":W+"Huarache_(shoe)",
 "x":[X("Mexican huarache","traditional huarache","Handmade all-leather sandal of pre-Columbian origin from Jalisco, Michoacán, Guanajuato and Yucatán; tyre-rubber soles from the 1930s.","","pre-Columbian; modern form 1930s",W+"Huarache_(shoe)",[],"woven leather upper · leather or tyre sole")]},
{"n":"Heeled sandal","a":"high-heeled sandal","d":"Sandal on a separate raised heel, not a wedge.",
 "t":["block heel","stiletto","kitten heel","platform"],"s":"https://www.vagabond.com/tr/women/footwear/sandals/heeled-sandals"},
{"n":"Wedge sandal","a":"wedge · wedgie","d":"Sandal whose heel and sole form one continuous raised wedge.",
 "t":["cork wedge","espadrille wedge","platform wedge","low wedge"],"s":W+"Wedge_(footwear)",
 "x":[X("Ferragamo cork wedge","cork wedge","Women's wedge with a solid cork sole introduced by Salvatore Ferragamo in the late 1930s when sanctions cut steel supplies.","Salvatore Ferragamo","late 1930s",W+"Wedge_(footwear)",
     [("The Rainbow","Salvatore Ferragamo","1938","multicoloured platform shoe")],"cork sole · uppers"),
    X("Wörishofer","Woerishofer","Ladies' sandal with a cork wedge heel.","","",W+"Sandal",[],"cork wedge · straps")]}
]
brands=[
{"n":"Havaianas","c":"Brazil","f":"1962","seg":"Flip-flops","d":"Brazilian rubber flip-flop brand created by Alpargatas.","sig":["Havaianas"],"s":W+"Havaianas"},
{"n":"Birkenstock","c":"Germany","f":"1774","seg":"Footbed sandals","d":"German maker of cork-latex footbed sandals and clogs.","sig":["Madrid","Arizona","Gizeh","Boston"],"s":W+"Birkenstock"},
{"n":"adidas","c":"Germany","f":"1949","seg":"Sportswear","d":"German sportswear company founded by Adolf Dassler.","lines":["Originals"],"sig":["Adilette"],"rel":["Puma"],"s":"knowledge"},
{"n":"Hermès","c":"France","f":"1837","seg":"Luxury","d":"French luxury house, originally a harness maker.","sig":["Oran"],"s":"knowledge"},
{"n":"Teva","c":"United States","f":"1984","seg":"Sport sandals","d":"Sport-sandal brand started by river guide Mark Thatcher; owned by Deckers since 2002.","sig":["Teva Original Sandal"],"s":"https://www.kveller.com/your-favorite-sandals-are-named-after-a-hebrew-word/"},
{"n":"Chaco","c":"United States","f":"1989","seg":"Sport sandals","d":"Sport-sandal brand started by guide Mark Paigen; owned by Wolverine World Wide since 2009.","sig":["Chaco Z/1"],"s":W+"Chaco_(footwear)"},
{"n":"Keen","c":"United States","f":"2003","seg":"Outdoor footwear","d":"Portland-based outdoor footwear brand known for wide toe boxes and closed-toe sandals.","sig":["Keen Newport"],"s":"https://keenfootwear.ca/blogs/keen-blog/20-wild-years-of-the-newport-sandal"},
{"n":"Salvatore Ferragamo","c":"Italy","f":"1927","seg":"Luxury shoes","d":"Florence shoemaker whose workshop became Salvatore Ferragamo S.p.A.","sig":["Ferragamo cork wedge"],"s":W+"Salvatore_Ferragamo"},
]
trad=[{"n":"Mexican huarache making","g":"Leather & footwear","r":"Mexico (Jalisco, Michoacán, Guanajuato, Yucatán)","p":"Pre-Columbian to present",
 "d":"Handmade sandals with hand-woven braided leather uppers.","tech":"hand-woven braided leather straps on a flat sole","mat":"leather; tyre rubber soles from the 1930s",
 "forms":["Mexican huarache"],"ctr":["Jalisco","Michoacán","Guanajuato","Yucatán"],"auth":"handmade with a woven-leather upper","s":W+"Huarache_(shoe)"}]
notes=("Dropped/moved: Kolhapuri and Peshawari chappals (old Flat strap sandal models) live in Traditional footwear (shelf 06_00, own kinds); Birkenstock Boston is a clog (Clog kind, other shelf). "
 "Arizona and Madrid moved from Flat strap sandal to Slide (backless); Gizeh placed under Flip-flop. 'Other heeled sandals' dissolved into Heeled sandal types; its Wörishofer moved to Wedge sandal as an archetype. "
 "Trimmed SKU lists: dropped Teva Hydratrek, Grandview Max; Chaco Rapid Pro; Keen Hyperport H2; Hoka Infini Hike TC; Pikolinos Tarifa. "
 "Left out for lack of a retrievable source: Ancient Greek Sandals brand/archetype (pages 403), Havaianas Top date (sources conflict 1969/1994), Teva 1984 model name beyond Deckers' 'Original Sandal'. "
 "Wedge kind source changed from Old Navy to Wikipedia. Parallel fetch unavailable (402), wiki tool rate-limited (429).")
out={"kinds":kinds,"brands":brands,"traditions":trad,"notes":notes}
p='work/A2/shelves/05_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
