import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Bra","a":"brassiere","d":"Supportive undergarment for the breasts with cups, straps and a band.",
 "t":["underwired","wire-free / soft cup","T-shirt (moulded)","push-up","plunge","balconette","full cup","demi-cup","strapless","convertible / multiway","racerback","sports","nursing / maternity","minimiser","bralette"],
 "s":W+"Brassiere",
 "x":[
  {"n":"Wonderbra plunge push-up","a":"Wonderbra 1300","d":"Plunging push-up bra with diagonally cut padded cups that lift and push the bust together.","mk":"Wonderbra","y":"1961","s":W+"Wonderbra",
   "v":[{"n":"1300 plunge push-up","mk":"Wonderbra","y":"1961","d":"Developed by Louise Poirier at Canadian Lady, Montreal; virtually identical to today's Wonderbra"},
        {"n":"One and Only Wonderbra","mk":"Wonderbra","y":"1994","d":"US launch with Eva Herzigová, alongside the UK 'Hello Boys' campaign"}],
   "dt":"padding level · plunge depth · cup and band sizes · lace or smooth"},
  {"n":"Playtex Cross Your Heart","a":"Cross Your Heart bra","d":"Mass-market bra with crossed front panels sold on the claim that it 'lifts and separates'.","mk":"Playtex","y":"1954","s":W+"Playtex",
   "v":[],"dt":"wired or soft cup · full coverage · cup and band sizes"}
 ],
 "m":[["Sculpture bra","La Perla"],["Comfort Chic","Chantelle"],["Rive Gauche","Chantelle"],["Eglantine","Wacoal"],["BraVissima","Mey"],["Air Bra","Leonisa"],["Magicup","Leonisa"],["Cassiopée","Empreinte"],["Melody","Empreinte"],["18 Hour Bra","Playtex"],["Mousse","Cake Maternity"]],
 "r":[["Comète","Simone Pérèle"],["Saga","Simone Pérèle"],["Wish","Simone Pérèle"],["Revolution","Empreinte"],["Joy","Felina"],["Avero","Van de Velde"],["Deauville","Van de Velde"],["Triumph","Triumph International"]]},
{"n":"Panties","a":"briefs · knickers","d":"Women's underpants covering the hips and crotch, sold apart from bras.",
 "t":["full brief","midi brief","high-leg","bikini","hipster","French cut","boyshort","thong","seamless / laser-cut"],
 "s":"https://media.adoreme.com/bras",
 "m":[["Petite culotte","Petit Bateau"]],
 "r":[["sloggi","Triumph International"],["Jockey For Her","Jockey International"]]},
{"n":"Men's underwear","a":"briefs · boxers · trunks · Y-fronts · jockey shorts","d":"Men's underpants, from close-fitting briefs to loose woven boxer shorts.",
 "t":["brief (full-rise, mid-rise, low-rise)","bikini brief","slip (no fly)","trunk","boxer brief","long-leg boxer brief","woven boxer shorts","jockstrap"],
 "s":W+"Briefs",
 "x":[
  {"n":"Jockey Y-front brief","a":"Y-fronts · jockey shorts · tighty-whities","d":"Close-fitting knitted brief with an inverted-Y overlapping fly; the first men's brief.","mk":"Jockey International","y":"1934","s":W+"Jockey_International",
   "v":[{"n":"Y-Front brief","mk":"Jockey International","y":"1935","d":"First sold 19 January 1935 at Marshall Field's, Chicago, by Coopers (later Jockey)"},
        {"n":"Skants","mk":"Jockey International","y":"1958","d":"Mass-market men's bikini brief"}],
   "dt":"rise (full, mid, low) · cotton, cotton-stretch · white, colours"},
  {"n":"Sunspel boxer shorts","a":"woven boxers","d":"Loose woven cotton boxer short brought to Britain by Sunspel, with an added back panel and flat seams.","mk":"Sunspel","y":"1947","s":W+"Sunspel",
   "v":[],"dt":"cotton poplin, Oxford, Sea Island · button or elastic waist · solids, stripes, checks"},
  {"n":"Calvin Klein boxer brief","a":"CK boxer brief","d":"Stretch-cotton boxer brief with a branded elastic waistband, made famous by the 1992 Mark Wahlberg adverts.","mk":"Calvin Klein","y":"1990s","s":W+"Calvin_Klein_(fashion_house)",
   "v":[],"dt":"cotton stretch, microfibre · leg length · logo waistband"},
  {"n":"Uniqlo AIRism underwear","a":"AIRism","d":"Quick-drying, cooling synthetic underwear fabric developed by Uniqlo with Toray.","mk":"Uniqlo","y":"2012","s":W+"Uniqlo",
   "v":[{"n":"AIRism Boxer Briefs","mk":"Uniqlo","y":"","d":"core boxer brief"},{"n":"AIRism Seamless Boxer Briefs","mk":"Uniqlo","y":"","d":"bonded, seam-free version"}],
   "dt":"boxer brief, trunk · colours"}
 ],
 "m":[["Classic Shorts","Björn Borg"],["Cotton Boxer Briefs","Uniqlo"],["Woven Trunks","Uniqlo"],["Low Rise brief","Jockey International"],["Midway Brief","Jockey International"],["Kangaroo brief","Munsingwear"],["Wonderjock","aussieBum"]],
 "r":[["Royal Classic","Zimmerli of Switzerland"]]},
{"n":"Undershirt","a":"vest · singlet · A-shirt · baniyan","d":"Thin shirt worn under a shirt for warmth or to keep sweat off it.",
 "t":["A-shirt / athletic singlet","crew neck","V-neck","deep V","long-sleeved","string vest","camisole (women's)"],
 "s":W+"Undershirt",
 "x":[
  {"n":"Bonds Athletic singlet","a":"Chesty Bond singlet","d":"Australian sleeveless cotton singlet promoted from 1940 by the Chesty Bond comic-strip hero.","mk":"Bonds","y":"1940","s":W+"Chesty_Bond",
   "v":[],"dt":"rib-knit cotton · white, black, colours"}
 ],
 "m":[["The Undershirt","Mey"],["Singleton","Jockey International"],["Undershirt","Hanes"]],
 "r":[["Royal Classic","Zimmerli of Switzerland"]]},
{"n":"Period underwear","a":"menstrual underwear · period pants","d":"Washable underwear with a highly absorbent, leak-resistant gusset worn during menstruation.",
 "t":["absorbency: light, moderate, heavy / super, overnight","cut: bikini, hipster, boyshort, French cut, full brief, high-waist, thong","teen ranges","swim and sleep versions"],
 "s":"https://www.thinx.com/collections/period-shop-all",
 "m":[],
 "r":[["Basic","Modibodi"],["Classic","Modibodi"],["Seamfree","Modibodi"],["Period underwear","Thinx"],["Period underwear","Knix"]]},
{"n":"Thermal base layer","a":"long johns · long underwear · thermals · base layer","d":"Close-fitting long-sleeved top or long-legged bottoms worn next to the skin for warmth.",
 "t":["merino wool","synthetic (polyester, polypropylene)","cotton waffle","wool-synthetic blend","weight: light, mid, heavy","top, bottoms, one-piece"],
 "s":W+"Long_underwear",
 "x":[
  {"n":"Union suit","a":"combinations · long handles","d":"One-piece long underwear with long arms and legs, a buttoned front and a drop seat.","mk":"","y":"1868","s":W+"Union_suit",
   "v":[],"dt":"red flannel (winter), white (summer), wool 'woolly combinations' · button count · drop seat"},
  {"n":"Stanfield's Unshrinkable Underwear","a":"Stanfield's long johns","d":"Canadian wool long underwear treated not to shrink, later made as an adjustable two-piece.","mk":"Stanfield's","y":"1898","s":W+"Stanfield%27s",
   "v":[{"n":"Two-piece design","mk":"Stanfield's","y":"1915","d":"Adjustable two-piece patented 7 December 1915"}],
   "dt":"wool, cotton blends · one or two-piece"},
  {"n":"Uniqlo HEATTECH","a":"Heattech","d":"Thin synthetic heat-retaining base layer developed by Uniqlo with Toray and sold in huge volume.","mk":"Uniqlo","y":"2003","s":W+"Uniqlo",
   "v":[],"dt":"standard, Extra Warm, Ultra Warm · tops, leggings, socks"}
 ],
 "m":[["Classic Thermal Merino","Smartwool"],["Classic All-Season Merino","Smartwool"],["Thermolactyl","Damart"],["Active Warm","ODLO"],["Performance Warm","ODLO"],["Norse Merino Meshwool","Janusfabrikken"],["Airwool Zip Polo Merino","Janusfabrikken"],["Lux Inferno","Lux Industries"],["Strategic","Cimalp"]],
 "r":[["Merino base layers","Icebreaker"]]},
{"n":"Shapewear","a":"foundation garment · control underwear · girdle","d":"Elastic, unboned garment worn under clothing to smooth or shape the figure.",
 "t":["bodysuit / body shaper","high-waist control brief","control panties","thigh shaper / shaping shorts","girdle","waist cincher","shaping slip","firmness: light, medium, firm"],
 "s":W+"Shapewear",
 "m":[["SPANXsculpt Seamless Power","Spanx"],["SPANXshape Invisible","Spanx"],["SPANXsupersculpt Transform","Spanx"],["Bodytoners","Aristoc"],["Tummy Girdle","Wacoal"],["Petit Scandale","Scandale"],["Foundettes","Munsingwear"],["Two-Way-One-Way","Warnaco Group"]],
 "r":[["Shapewear","Skims"]]},
{"n":"Corset","a":"stays · waspie · waist cincher","d":"Boned, laced garment that shapes the torso, worn under or over clothing.",
 "t":["overbust","underbust","waspie / waist cincher","longline","standard length","corset belt","waist trainer (elastic, not a true corset)","steel-boned","plastic-boned (fashion)","satin, cotton, mesh, leather, PVC, latex"],
 "s":"https://www.orchardcorset.com/collections/underbust-corsets",
 "x":[
  {"n":"Orchard Corset CS series","a":"CS-411 · CS-426","d":"Ready-to-wear steel-boned corsets sold by curve (Modern, Romantic, Hourglass, Extreme) and length.","mk":"Orchard Corset","y":"","s":"https://www.orchardcorset.com/collections/underbust-corsets",
   "v":[{"n":"CS-411","mk":"Orchard Corset","y":"","d":"standard underbust, Romantic curve"},{"n":"CS-426","mk":"Orchard Corset","y":"","d":"standard, longline and hip-tie, Hourglass curve"},{"n":"CS-305","mk":"Orchard Corset","y":"","d":"standard underbust, Modern curve"},{"n":"CS-345","mk":"Orchard Corset","y":"","d":"longline, Romantic curve"},{"n":"CS-201","mk":"Orchard Corset","y":"","d":"waspie, Hourglass curve"},{"n":"CS-479","mk":"Orchard Corset","y":"","d":"standard underbust, Extreme curve"}],
   "dt":"curve · length · satin, cotton, mesh, lace, PVC"}
 ],
 "m":[["Dr. Warner's Health Corset","Warnaco Group"],["Eezee","Berlei"],["Princess Youth","Berlei"],["Fashonese","Twilfit"]]},
{"n":"Socks","a":"","d":"Knitted covering for the foot and ankle or lower leg.",
 "t":["no-show","ankle / quarter","crew","mid-calf","over-the-calf","knee-high","toe socks","compression","hiking / cushioned","dress","merino, cotton, synthetic, cashmere"],
 "s":"https://www.rei.com/c/socks/f/fbt-wool-wool-blend",
 "x":[
  {"n":"Argyle socks","a":"argyle hose","d":"Socks knitted with a diamond (lozenge) pattern descended from Scottish Highland tartan hose.","mk":"","y":"1920s","s":W+"Argyle_(pattern)",
   "v":[],"dt":"two to four colours · overplaid lines · wool, cotton · mid-calf, over-the-calf"},
  {"n":"Rockford Red Heel sock","a":"monkey sock · red heel sock","d":"Brown-grey work sock with a red heel, the raw material of the sock monkey.","mk":"Nelson Knitting Company","y":"1932","s":W+"Sock_monkey",
   "v":[{"n":"Original Rockford Red Heel Monkey Sock","mk":"Fox River Mills","y":"1992","d":"Made by Fox River Mills after it acquired Nelson Knitting in 1992"}],
   "dt":"cotton-wool blend · brown heather with red heel and white toe"},
  {"n":"Wigwam 622 slouch sock","a":"Wigwam 622","d":"Thick ribbed slouch sock popular from the mid-1980s to the late 1990s.","mk":"Wigwam Mills","y":"mid-1980s","s":W+"Wigwam_Mills",
   "v":[],"dt":"ribbed · white · slouched at the ankle"}
 ],
 "m":[["Hiker Micro Crew Cushion","Darn Tough"],["Light Hiker Micro Crew","Darn Tough"],["Performance Hike Targeted Cushion Ankle","Smartwool"],["Hike Medium Crew","Icebreaker"],["Outdoor Midweight Crew","Injinji"],["Trailsmith Merino Wool Crew","REI Co-op"],["Airport","Falke"],["Family","Falke"],["Tiago","Falke"],["Héritage Henry","Broussaud"],["Sportsman","Wolsey"],["Circulator Compression","Sockwell"]]},
{"n":"Tights & stockings","a":"pantyhose · nylons · hold-ups · stay-ups · thigh-highs","d":"Sheer or opaque knitted leg coverings: tights in one piece to the waist, stockings to the thigh.",
 "t":["denier: ultra-sheer (under 15), sheer (15–20), semi-opaque (30), opaque (40+)","control top","sheer-to-waist","fishnet","patterned / lace","mock suspender","footless","open-toe","crotchless","hold-ups (stay-ups)","suspender stockings","fully fashioned (seamed)","plus size","maternity"],
 "s":W+"Pantyhose",
 "x":[
  {"n":"Panti-Legs","a":"first pantyhose","d":"The first pantyhose sold to the public, combining stockings and briefs in one garment.","mk":"Glen Raven Knitting Mills","y":"1959","s":W+"Pantyhose",
   "v":[],"dt":"nylon · sheer"},
  {"n":"Fully fashioned stocking","a":"seamed stocking · FF stocking","d":"Stocking knitted flat and joined with a seam up the back; the dominant style until the 1960s.","mk":"","y":"before 1960s","s":W+"Stocking",
   "v":[],"dt":"nylon, silk · back seam · Cuban or French heel · worn with suspenders"}
 ],
 "m":[["Neon","Wolford"],["Ultimate","Aristoc"],["Magie","Oroblu"],["Federica Luxe Shine Opaque","Trasparenze"],["Sheer Look Opaque","Charnos"],["Eterno Super Lucido","Cecilia de Rafael"],["Talia Mock Stocking","Gatta"],["Elite","Kunert"],["Mink Royal","Wolsey"],["Supersize Plus Size","Glamory"],["Positive Look Plus Size","Giulia"]],
 "r":[["Fatal","Wolford"],["Hold-ups","Pretty Polly"]]},
{"n":"Leg warmers","a":"ankle warmers","d":"Footless knitted tubes worn over the lower leg for warmth, from dance practice.",
 "t":["cable knit","scrunch / slouch","ankle warmers (short)","thigh-length","wool, cotton, acrylic, chenille"],
 "s":W+"Leg_warmer","m":[]}
]
def B(n,c,f,seg,d,s,lines=[],eras=[],sig=[],rel=[]):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":eras,"sig":sig,"sc":[],"rel":rel,"s":s}
brands=[
B("Maidenform","United States","1922","mass-market lingerie","Bra maker founded in Bayonne, New Jersey, by Ida and William Rosenthal and Enid Bissett; owned by Hanesbrands since 2013.",W+"Maidenform",rel=["Wonderbra","Playtex"]),
B("Wonderbra","Canada","1939","push-up bras","Push-up bra brand from Canadian Lady, Montreal, built on Israel Pilot's 1935 'Wonder-Bra' name; with Hanesbrands from 2006.",W+"Wonderbra",lines=["Dici by Wonderbra (1974)"],eras=["Canadian Lady / Canadelle, 1939–","Gossard UK licence, to 1994","Sara Lee","HanesBrands, 2006–","Gildan, 2025–"],sig=["Wonderbra plunge push-up"],rel=["Playtex","Maidenform"]),
B("Playtex","United States","1947","mass-market bras","Bra brand begun as a division of International Latex Corporation, known for Cross Your Heart and the 18 Hour Bra.",W+"Playtex",lines=["Cross Your Heart","18 Hour"],sig=["Playtex Cross Your Heart"],rel=["Wonderbra","Maidenform"]),
B("Jockey International","United States","1876","mass-market underwear","Kenosha, Wisconsin, maker (formerly Coopers) that introduced the Y-front brief.",W+"Jockey_International",lines=["Y-Front","Skants","Jockey For Her"],eras=["Coopers, Inc., 1876–","Y-front brief, 1934–35"],sig=["Jockey Y-front brief"]),
B("Sunspel","United Kingdom","1860","heritage basics","Long Eaton maker of fine cotton underwear and T-shirts that introduced boxer shorts to Britain.",W+"Sunspel",lines=["Riviera polo"],sig=["Sunspel boxer shorts"]),
B("Calvin Klein","United States","","designer underwear and fashion","American fashion house whose branded-waistband underwear drove the 1980s–90s designer underwear boom; owned by PVH.",W+"Calvin_Klein_(fashion_house)",eras=["John Varvatos, menswear, 1990–1995"],sig=["Calvin Klein boxer brief"]),
B("Uniqlo","Japan","1984","mass-market basics","Japanese casual-wear chain whose fabric technologies with Toray include HEATTECH and AIRism.",W+"Uniqlo",lines=["HEATTECH","AIRism"],sig=["Uniqlo HEATTECH","Uniqlo AIRism underwear"]),
B("Stanfield's","Canada","1856","heritage underwear","Truro, Nova Scotia, woollen maker known for Unshrinkable Underwear and long johns.",W+"Stanfield%27s",sig=["Stanfield's Unshrinkable Underwear"]),
B("Icebreaker","New Zealand","1995","outdoor merino","Merino clothing brand that began with base layers; owned by VF Corporation.",W+"Icebreaker_(clothing)",rel=["Smartwool"]),
B("Smartwool","United States","1994","outdoor merino","Steamboat Springs merino sock and apparel maker; owned by VF Corporation.",W+"Smartwool",rel=["Icebreaker","Darn Tough"]),
B("Damart","France","1953","thermal clothing","French maker of thermal underwear in its Thermolactyl fibre.",W+"Damart",lines=["Thermolactyl"]),
B("Spanx","United States","2000","shapewear","Atlanta shapewear company founded by Sara Blakely; majority-owned by Blackstone since 2021.",W+"Spanx",rel=["Skims"]),
B("Skims","United States","2019","shapewear and basics","Los Angeles shapewear and loungewear brand founded by Kim Kardashian and Jens Grede.",W+"Skims",rel=["Spanx"]),
B("Wacoal","Japan","1949","lingerie","Kyoto lingerie maker founded by Koichi Tsukamoto.",W+"Wacoal"),
B("Triumph International","Switzerland","1886","mass-market lingerie","Underwear maker founded in Heubach, Germany, now based in Bad Zurzach; owns sloggi.",W+"Triumph_International",lines=["Triumph","sloggi"]),
B("Chantelle","France","1876","lingerie","Family-owned French lingerie maker of bras, briefs and hosiery, based in Cachan.",W+"Chantelle_(lingerie)"),
B("Hanes","United States","1900","mass-market basics","Winston-Salem maker of undershirts, T-shirts and underwear; part of Hanesbrands.",W+"Hanes"),
B("Zimmerli of Switzerland","Switzerland","1871","luxury underwear","Swiss luxury underwear brand founded in Aarburg by Pauline Zimmerli-Bäurlin.",W+"Zimmerli_of_Switzerland"),
B("Thinx","United States","2014","period underwear","New York period-underwear brand; majority-owned by Kimberly-Clark since 2022.",W+"Thinx",rel=["Modibodi"]),
B("Modibodi","Australia","","period underwear","Australian absorbent-underwear brand founded by Kristy Chong, with four absorbency levels.","https://eu.modibodi.com/blogs/womens/the-face-and-brains-behind-australian-brand-modibodi",rel=["Thinx"]),
B("Darn Tough","United States","2004","outdoor socks","Sock label of Cabot Hosiery Mills (1978), Northfield, Vermont.",W+"Darn_Tough",rel=["Smartwool"]),
B("Falke","Germany","1895","premium hosiery","Family-owned Schmallenberg maker of socks, tights and knitwear; holds Burlington trademarks since 2008.",W+"FALKE_Group",rel=["Burlington"]),
B("Wolford","Austria","1949","luxury hosiery","Bregenz maker of seamless tights and bodysuits; majority-owned by Fosun since 2018.",W+"Wolford"),
B("Pretty Polly","United Kingdom","1919","mass-market hosiery","Nottinghamshire hosiery brand that introduced hold-ups in 1967; went into liquidation in May 2026.",W+"Pretty_Polly_(hosiery)",rel=["Aristoc"]),
B("Aristoc","United Kingdom","1919","hosiery and shapers","Derbyshire hosiery brand best known for body shapers; a Pretty Polly brand, liquidated in May 2026.",W+"Aristoc",rel=["Pretty Polly"]),
B("Wigwam Mills","United States","1905","socks","Family-run Sheboygan, Wisconsin, sock maker, first for lumbermen, later athletic socks.",W+"Wigwam_Mills",sig=["Wigwam 622 slouch sock"]),
B("Bombas","United States","2013","direct-to-consumer socks","New York sock brand that donates an item for each one sold.",W+"Bombas"),
B("Nelson Knitting Company","United States","1880","work socks","Rockford, Illinois, sock maker that added the red heel in 1932; acquired by Fox River Mills in 1992.",W+"Sock_monkey",sig=["Rockford Red Heel sock"],rel=["Fox River Mills"]),
]
notes=("Dissolved 'Other underwear' (k73): bras to Bra, Jockey/Munsingwear/aussieBum to Men's underwear, Mey/Jockey Singleton/Zimmerli to Undershirt, "
 "Stanfield's to Thermal base layer. Merged Tights + Stockings. Dropped: duplicate Cabot Hosiery Mills socks (same models as Darn Tough), Jockey 'Kenosha Klosed Krotch' (historic), "
 "Empreinte model dump trimmed to two plus one range, Cake Maternity cut to one nursing bra, generic cut names moved to t. "
 "Not added (no retrieved page confirming): Maidenform bra archetype (page names no model), Spanx/Skims archetypes, Wolford Neon 40/Falke Pure Matt specifics, Burlington argyle link, "
 "Devold, Knix/Björn Borg brand entries (no page retrieved), Orchard Corset/What Katie Did/Dark Garden brand entries. Bonds singlet dated 1940 per the Chesty Bond page (brief said 1938). "
 "Pretty Polly and Aristoc ceased trading May 2026. No traditions on this shelf.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/A1/shelves/05_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
