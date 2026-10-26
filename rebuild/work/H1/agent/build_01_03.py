import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Nail polish","a":"nail varnish · nail lacquer · nail enamel","d":"Coloured or clear lacquer brushed onto the nails and left to air-dry.",
 "t":["crème","sheer","jelly","shimmer","glitter","flake","holographic","multichrome","metallic","magnetic","thermal (heat colour-changing)","matte","base coat","top coat","ridge filler","peel-off base"],
 "s":W+"Nail_polish",
 "x":[
  {"n":"Revlon nail enamel","a":"Revlon nail colour","d":"Pigment-based nail enamel that founded Revlon and opened up a wide range of opaque shades.","mk":"Revlon","y":"1932","s":W+"Revlon",
   "v":[{"n":"Where's the Fire?","mk":"Revlon","y":"1950","d":"red nail enamel"},{"n":"Fire and Ice","mk":"Revlon","y":"1953","d":"lip and nail red from the Avedon campaign; reissued 2010"}],
   "dt":"bottle size · cream and frosted finishes · matching lip shades"},
  {"n":"Chanel Le Vernis","a":"Chanel nail colour","d":"Chanel's couture nail polish line, renamed Le Vernis after a 1995 reformulation.","mk":"Chanel","y":"1974","s":"https://client.cosmeticobs.com/en/articles/products-38/la-saga-du-rouge-noir-de-chanel-2144",
   "v":[{"n":"Rouge Noir","mk":"Chanel","y":"1994","d":"near-black red by Dominique Moncourtois; sold in the US as Vamp"},{"n":"Particulière 505","mk":"Chanel","y":"","d":"atypical greige shade"}],
   "dt":"numbered shades · seasonal limited editions"},
  {"n":"OPI Nail Lacquer","a":"OPI polish","d":"Salon-brand nail lacquer known for punning shade names and a large permanent classics range.","mk":"OPI","y":"","s":"https://www.opi.com/products/nail-lacquer-lincoln-park-after-dark",
   "v":[{"n":"Lincoln Park After Dark (NL W42)","mk":"OPI","y":"2005","d":"near-black aubergine; also in Infinite Shine, GelColor and Powder Perfection"}],
   "dt":"15 ml bottle · shade codes · same shades across lacquer, gel and dip"},
  {"n":"Essie nail polish","a":"essie enamel","d":"Salon nail polish line begun with twelve shades in 1981 and owned by L'Oréal since 2010.","mk":"Essie","y":"1981","s":"https://www.essie.co.uk/nail-polish/enamel/sheers/ballet-slippers",
   "v":[{"n":"Ballet Slippers","mk":"Essie","y":"","d":"best-selling sheer pale pink"}],
   "dt":"sheer, crème and shimmer shades · gloss finish"},
  {"n":"Dior Vernis","a":"Dior nail polish","d":"Dior's couture nail polish with a glossy gel-effect finish.","mk":"Dior","y":"","s":"https://dior.com/en_int/beauty/products/dior-vernis-Y0381009.html",
   "v":[],"dt":"reds, pinks, nudes, white, black · gel-effect gloss"},
  {"n":"CND Vinylux","a":"Vinylux weekly polish","d":"Two-step long-wear air-dry polish with a matching top coat, claimed to last about a week.","mk":"CND","y":"2013","s":"https://www.creativenails.co.nz/pages/cnd-nail-colour-coatings",
   "v":[],"dt":"100+ shades · base-and-colour in one plus top coat"},
  {"n":"Holo Taco","a":"Simply Nailogical polish","d":"Indie brand from YouTuber Cristine Rotenberg built around holographic top coats and special-effect polishes.","mk":"Holo Taco","y":"2019","s":W+"Cristine_Rotenberg",
   "v":[{"n":"Holo Taco top coat","mk":"Holo Taco","y":"2019","d":"silver holographic top coats in the launch set"},{"n":"One Coat Black","mk":"Holo Taco","y":"2019","d":"opaque black from the launch"},{"n":"Royal-Tea Blue","mk":"Holo Taco","y":"2019","d":"opaque blue from the launch"}],
   "dt":"holographic, multichrome, iridescent effects · collaboration collections"},
  {"n":"ILNP","a":"I Love Nail Polish","d":"Las Vegas boutique polish maker known for holographic, chrome, jelly and magnetic finishes.","mk":"ILNP","y":"2012","s":"https://www.ilnp.com/about/our-story/",
   "v":[],"dt":"holographic · metallic · chrome · shimmer · jelly · magnetic · speckled · toppers"}
 ]},
{"n":"Gel nail kit","a":"gel polish · soak-off gel · UV/LED nail lamp","d":"Gel polish cured under a UV or LED lamp for long wear, sold as kits or separately.",
 "t":["soak-off gel polish","builder gel","polygel","UV lamp","LED lamp","gel remover"],
 "s":W+"Gel_nails",
 "x":[
  {"n":"CND Shellac","a":"Shellac","d":"Lamp-cured gel-polish hybrid that applies like polish and wears for two weeks.","mk":"CND","y":"2010","s":"https://www.creativenails.co.nz/pages/cnd-nail-colour-coatings",
   "v":[],"dt":"base, colour and top coat system · 100+ shades · lamp cure"},
  {"n":"Gelish","a":"Harmony Gelish","d":"Brush-on, LED-cured soak-off gel polish sold in a polish bottle.","mk":"Gelish","y":"2010","s":"https://c8nailsupply.com/blogs/brand-spotlight/gelish-brand-spotlight",
   "v":[{"n":"Foundation base gel","mk":"Gelish","y":"","d":"base coat in the system"},{"n":"Top It Off","mk":"Gelish","y":"","d":"sealing top coat"}],
   "dt":"LED or UV cure · 200+ shades"}
 ]},
{"n":"Artificial nails","a":"false nails · fake nails · nail extensions","d":"Press-on, glued or salon-built covers and extensions worn over the natural nail.",
 "t":["press-on nails","nail tips","acrylic kit","soft gel tips","nail wraps","dip powder","nail glue"],
 "s":W+"Artificial_nails",
 "x":[
  {"n":"Acrylic sculpted nail","a":"acrylic nails","d":"Extension built from liquid monomer and powder polymer, first made from dental acrylic.","mk":"","y":"1954","s":W+"Artificial_nails",
   "v":[{"n":"Patti Nails","mk":"","y":"1954","d":"Fred and Tom Slack's patented dental-acrylic nail"}],"dt":"EMA monomer · tips or forms · up to about 3 weeks"},
  {"n":"imPRESS Press-On Manicure","a":"Kiss imPRESS","d":"Glue-free press-on nails with pre-applied adhesive.","mk":"Kiss","y":"2012","s":"https://chaindrugreview.com/kiss-unveils-impress-press-on-falsies/",
   "v":[],"dt":"length and shape · colour and art designs · manicure and pedicure sets"},
  {"n":"Gel-X soft gel tips","a":"soft gel extensions","d":"Full-cover soft gel tips cured on and removed by acetone soak.","mk":"","y":"2017","s":W+"Artificial_nails",
   "v":[],"dt":"shape and length · lamp cure"}
 ]},
{"n":"Nail clippers & manicure tools","a":"nail clippers · nail nippers · manicure set","d":"Hand tools for cutting nails and tidying cuticles, sold singly or as a set.",
 "t":["lever clipper","plier/nipper clipper","toenail clipper","nail scissors","cuticle nipper","cuticle pusher","orangewood stick","manicure set"],
 "s":"https://www.zwilling.com/us/zwilling-twinox-toenail-clippers-stainless-steel-white-42410-000-0/42410-000-0.html",
 "x":[
  {"n":"Trim lever clipper","a":"Trim nail clipper","d":"Classic compound-lever pocket clipper with jaw design, popularised by W. E. Bassett's Trim brand.","mk":"Trim","y":"1947","s":W+"Nail_clipper",
   "v":[{"n":"Gem","mk":"H. C. Cook Company","y":"1896","d":"earlier lever clipper claimed by Carter"}],"dt":"fingernail or toenail head · built-in file · catcher"},
  {"n":"Seki Edge clipper","a":"Green Bell clipper","d":"Japanese stainless lever clippers made in the blade town of Seki.","mk":"Seki Edge","y":"","s":"https://notes.nicolasdeville.com/interests/seki-edge/",
   "v":[{"n":"SS-106","mk":"Seki Edge","y":"","d":"fingernail clipper, best seller"},{"n":"SS-107","mk":"Seki Edge","y":"","d":"larger toenail version"},{"n":"SS-112","mk":"Seki Edge","y":"","d":"top of the range"},{"n":"SS-109 Satin Slim","mk":"Seki Edge","y":"","d":"slim travel clipper"},{"n":"SS-204","mk":"Seki Edge","y":"","d":"nipper for thick or ingrown toenails"}],
   "dt":"stainless steel · lever or nipper · with or without catcher"}
 ],
 "m":[["TWINOX Toenail Clippers","Zwilling"],["Cuticle nipper","Tweezerman"]]},
{"n":"Nail file","a":"emery board · nail buffer","d":"Abrasive tool for shaping and smoothing nail edges.",
 "t":["emery board","glass/crystal file","metal file","buffer","electric nail drill"],
 "s":"https://kbshimmer.com/nail-files/",
 "x":[
  {"n":"Emery board","a":"","d":"Flat flexible stick coated with emery, cheap and disposable.","mk":"","y":"1883","s":W+"Nail_file","v":[{"n":"J. Parker Pray patent","mk":"","y":"1883","d":"patented emery board"}],"dt":"grit · length"},
  {"n":"Glass nail file","a":"crystal file","d":"Glass file with an etched or coated surface that smooths without splintering the nail.","mk":"","y":"","s":W+"Nail_file","v":[],"dt":"solid or coated glass · length"}
 ]}
]
brands=[
 {"n":"Revlon","c":"United States","f":"1932","seg":"Mass cosmetics","d":"New York cosmetics company founded on a single pigment-based nail enamel.","lines":["Revlon nail enamel","Cutex","Sinful Colors"],"eras":["Charles Revson, 1932–1975"],"sig":["Revlon nail enamel"],"sc":[],"rel":[],"s":W+"Revlon"},
 {"n":"Chanel","c":"France","f":"1910","seg":"Luxury fashion and beauty","d":"Paris couture house founded by Gabrielle Chanel; makes Le Vernis nail colour.","lines":["Le Vernis"],"eras":[],"sig":["Chanel Le Vernis"],"sc":[],"rel":[],"s":W+"Chanel"},
 {"n":"Dior","c":"France","f":"1946","seg":"Luxury fashion and beauty","d":"Paris couture house in LVMH with a cosmetics business since 1969.","lines":["Dior Vernis"],"eras":[],"sig":["Dior Vernis"],"sc":[],"rel":[],"s":W+"Dior"},
 {"n":"OPI","c":"United States","f":"1981","seg":"Professional nail care","d":"California salon nail brand, now part of Wella Company.","lines":["Nail Lacquer","Infinite Shine","GelColor"],"eras":["George Schaeffer and Suzi Weiss-Fischmann, from 1981"],"sig":["OPI Nail Lacquer"],"sc":[],"rel":["Essie"],"s":W+"OPI_Products"},
 {"n":"Essie","c":"United States","f":"1981","seg":"Professional nail care","d":"Nail polish brand founded by Essie Weingarten, sold to L'Oréal in 2010.","lines":["essie enamel"],"eras":["Essie Weingarten, 1981–2010"],"sig":["Essie nail polish"],"sc":[],"rel":["OPI"],"s":W+"Essie_Weingarten"},
 {"n":"CND","c":"United States","f":"1979","seg":"Professional nail care","d":"Creative Nail Design, maker of Shellac gel polish and Vinylux.","lines":["Shellac","Vinylux"],"eras":[],"sig":["CND Shellac"],"sc":[],"rel":["Gelish"],"s":"https://www.creativenails.co.nz/pages/cnd-nail-colour-coatings"},
 {"n":"Gelish","c":"United States","f":"2010","seg":"Professional nail care","d":"Soak-off gel polish line from Hand & Nail Harmony, founded by Danny Haile in 2009.","lines":["Gelish soak-off gel"],"eras":[],"sig":["Gelish"],"sc":[],"rel":["CND"],"s":"https://c8nailsupply.com/blogs/brand-spotlight/gelish-brand-spotlight"},
 {"n":"Holo Taco","c":"Canada","f":"2019","seg":"Indie nail polish","d":"Special-effect polish brand founded by YouTuber Cristine Rotenberg (Simply Nailogical).","lines":[],"eras":[],"sig":["Holo Taco"],"sc":[],"rel":["ILNP"],"s":W+"Cristine_Rotenberg"},
 {"n":"ILNP","c":"United States","f":"2012","seg":"Indie nail polish","d":"Las Vegas boutique polish maker founded by Barbra Salet.","lines":["Boutique Effect"],"eras":[],"sig":["ILNP"],"sc":[],"rel":["Holo Taco"],"s":"https://www.ilnp.com/about/our-story/"},
 {"n":"Kiss","c":"United States","f":"","seg":"Mass nail and lash","d":"KISS Products, large maker of press-on nails and lashes, including imPRESS.","lines":["imPRESS"],"eras":[],"sig":["imPRESS Press-On Manicure"],"sc":[],"rel":[],"s":"https://chaindrugreview.com/kiss-unveils-impress-press-on-falsies/"},
 {"n":"Seki Edge","c":"Japan","f":"","seg":"Grooming tools","d":"Green Bell's clipper brand, made in Seki, Gifu.","lines":["SS series"],"eras":[],"sig":["Seki Edge clipper"],"sc":[],"rel":[],"s":"https://notes.nicolasdeville.com/interests/seki-edge/"},
 {"n":"Tweezerman","c":"United States","f":"","seg":"Grooming tools","d":"Tweezer and manicure-tool maker founded by Dal LaMagna, sold to Zwilling.","lines":["tweezers","cuticle nippers"],"eras":["Dal LaMagna, founder"],"sig":[],"sc":[],"rel":["Zwilling"],"s":"https://fortune.com/2013/12/19/dal-lamagna-the-rise-of-the-tweezerman/"},
 {"n":"Zwilling","c":"Germany","f":"1731","seg":"Cutlery and grooming","d":"Solingen knife-maker that owns Tweezerman (since 2004) and makes manicure tools.","lines":["TWINOX"],"eras":[],"sig":[],"sc":[],"rel":["Tweezerman"],"s":W+"Zwilling_J._A._Henckels"}
]
trad=[{"n":"Seki cutlery","g":"Metal & blades","r":"Seki, Gifu, Japan","p":"14th century to present","d":"Mino sword-making centre that became Japan's main cutlery town, now also making clippers and grooming blades.","tech":"forged and ground steel blades","mat":"carbon and stainless steel","forms":["Nail clippers & manicure tools"],"ctr":["Seki Cutlery Association","Seki Swordsmith Museum","Kinju (Kaneshige)"],"auth":"made-in-Seki marking from a named Seki maker","s":W+"Seki,_Gifu"}]
notes=("All five old kinds kept: Nail clippers and Manicure set merged; Gel nail kit added. Zwilling TWINOX kept as a model, Tweezerman cuticle nipper as a model "
 "(no retrieved page for a specific Tweezerman clipper). Left out for lack of a retrieved source: Dior 999 shade, Chanel Rouge Noir shade number, OPI GelColor as its own archetype, "
 "Cutex, ORLY, Zwilling/Tweezerman clipper archetypes. Gelish and CND 'first gel polish' claims are brand claims and not stated.")
out={"kinds":kinds,"brands":brands,"traditions":trad,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/H1/shelves/01_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
