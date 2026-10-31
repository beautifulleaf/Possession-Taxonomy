import json, os
W='https://en.wikipedia.org/wiki/'
def A(n,d,s,mk='',y='',a='',v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=x[0],mk=x[1],y=x[2],d=x[3]) for x in v],"dt":dt}
K=[]
K.append({"n":"Kente cloth","a":"kente · nwentoma · kete (Ewe)","d":"Ghanaian cloth of narrow hand-woven silk or cotton strips sewn edge to edge, each pattern carrying a name.",
 "t":["Full cloth (men's toga-style wrap)","Stole or sash","Silk, rayon or cotton"],"s":W+"Kente_cloth",
 "x":[A("Asante kente","Strip-woven Akan kente from the Ashanti Region, traditionally traced to Bonwire and woven with unravelled imported silk.",W+"Kente_cloth",y="18th century",a="Ashanti kente · Bonwire kente",
   v=[("Ahwepan","","","Simple warp-stripe design in plain weave on a single pair of heddles"),("Adweneasa","","","'I've exhausted my skills': weft patterns in every block, needs three heddles")],
   dt="strip width · warp-stripe pattern name · silk or cotton · weft-block density"),
  A("Ewe kente","Kente of the Ewe people of south-eastern Ghana and Togo, made of double-woven bands.",W+"Kente_cloth",y="16th century (oral tradition)",
   v=[("Keta weaving","","18th century","Keta became the centre of Ewe weaving")],dt="double-woven bands"),
  A("Kente print","Factory-printed cloth imitating kente patterns, made by wax-print firms and mass-produced in China.",W+"Kente_cloth",
   v=[("Vlisco kente print","Vlisco","",""),("ATL kente print","Akosombo Textile Limited","","")],dt="printed cotton · not strip-woven")]})
K.append({"n":"Wax print (Ankara)","a":"African wax print · Dutch wax · Ankara · Hollandais","d":"Industrially printed cotton with batik-style resin-resist designs, clear on both faces, sold for West and Central African dress.",
 "t":["Full piece (12 yards)","Half piece (6 yards)","Real wax (resin resist both sides)","Fancy / imitation wax (roller printed)","Digital print"],"s":W+"African_wax_prints",
 "x":[A("Real wax print","Resin-resist cloth printed with wooden stamp blocks per colour, the design and registration number printed on the selvedge.",W+"African_wax_prints",mk="Vlisco",y="19th century",a="Dutch wax · wax Hollandais",
   v=[("Vlisco","Vlisco","1846","Helmond, Netherlands; the reference maker"),("GTP","Vlisco","","Ghana Textiles Printing, Vlisco Group"),("Uniwax","Vlisco","","Côte d'Ivoire, Vlisco Group"),("Woodin","Vlisco","","Vlisco Group brand"),("ATL","Akosombo Textile Limited","","Ghana; real wax and fancy prints"),("ABC Wax","","","African wax maker named in sources")],
   dt="selvedge maker name and design number · colourway · 6- or 12-yard piece"),
  A("Fancy print","Cheaper roller-printed cloth that mimics wax-print designs, often experimenting with new patterns.",W+"African_wax_prints",
   v=[("Printex","Printex","","Accra, Ghana"),("ATL fancy print","Akosombo Textile Limited","","")],dt="one-sided print · lighter colour on reverse")],
 "m":[["Wax Hollandais","Vlisco"],["GTP wax","Vlisco"],["Uniwax","Vlisco"],["ATL real wax","Akosombo Textile Limited"]]})
K.append({"n":"Batik cloth","a":"batik · kain batik · batik tulis · batik cap","d":"Cloth patterned by drawing or stamping hot wax as a dye resist, then dyeing in repeated cycles.",
 "t":["Batik tulis (hand-drawn with canting)","Batik cap (copper stamp)","Combination tulis and cap","Printed batik-pattern cloth (not true batik)","Cotton or silk","Kain panjang, sarong or length"],"s":W+"Batik",
 "x":[A("Parang","One of the oldest Javanese batik motifs: unbroken interlocking S-shapes running diagonally.",W+"Parang_(batik)",a="batik parang · lereng",dt="diagonal width · colour · tulis or cap"),
  A("Kawung","Native Indonesian geometric batik motif, linked with Flower of Life geometry.",W+"Batik",dt="repeat size · colour"),
  A("Truntum","Native Indonesian batik motif listed among the traditional patterns.",W+"Batik"),
  A("Sidomukti","Javanese motif from the Hindu-Buddhist strand, one of the 'sida' patterns.",W+"Batik",a="sidha mukti · sidha asih · sidha luhur"),
  A("Megamendung","Chinese-style cloud motif of the north coast, associated with Cirebon, Lasem and Pekalongan.",W+"Batik",a="mega mendung",v=[("Cirebon Trusmi","","","Trusmi Batik Village, West Java")],dt="cloud motif"),
  A("Malaysian batik","East-coast Malay batik with larger, simpler floral motifs, brush-painted in lighter, brighter colours.",W+"Batik",y="1920s (block batik introduced)",dt="leaf and flower motifs · brush-painted · block-stamped")]})
K.append({"n":"Shweshwe","a":"seshoeshoe · seshweshwe · ishweshwe · German print · blaudruck","d":"Southern African discharge-printed cotton with fine geometric patterns, worn for Basotho and Xhosa dress.",
 "t":["Indigo","Chocolate brown","Red","Other colourways"],"s":W+"Seshoeshoe",
 "x":[A("Three Cats","The best-known shweshwe brand, roller-printed by acid discharge and starched stiff.",W+"Seshoeshoe",mk="Da Gama Textiles",y="sole rights 1992",a="3 Cats · Three Cats Original",
   v=[("Three Cats Original backstamp","Da Gama Textiles","","3 Cats logo stamped on the back of genuine cloth")],dt="design · colourway · starched handle that softens after washing")]})
K.append({"n":"Bogolan","a":"bògòlanfini · mud cloth · mud-dyed cloth","d":"Handmade Malian cotton cloth patterned with fermented mud, now a symbol of Malian identity.",
 "t":["Traditional hand-dyed","Commercial stencilled or printed","Strip-woven cotton panels"],"s":W+"B%C3%B2g%C3%B2lanfini"})
K.append({"n":"Adire & aso-oke","a":"Yoruba cloth · àdìrẹ · aṣọ òkè · òfì","d":"The two named Yoruba cloths: resist-dyed indigo adire and strip-woven aso-oke for festive dress.",
 "t":["Wrapper (ìró)","Head tie (gele)","Shawl (ìborùn)","Matched set (aso ebi)"],"s":W+"Adire_(textile_art)",
 "x":[A("Adire","Indigo cloth dyed by Yoruba women using tie, stitch, stencil or hand-painted starch resists.",W+"Adire_(textile_art)",dt="resist method: tied, stitched, hand-painted, stencilled · indigo depth"),
  A("Aso oke","Hand-woven Yoruba strip cloth, usually woven by men, for agbada, fila, gele, ìró and bùbá.",W+"Aso_oke",a="òfì",dt="strip pattern · cotton, silk or lurex · set of pieces")]})
K.append({"n":"Ikat cloth","a":"ikat · abrband · kasuri · jaspe","d":"Cloth woven from yarns resist-dyed before weaving, giving a characteristic blurred pattern on both faces.",
 "t":["Warp ikat","Weft ikat","Double ikat","Silk, cotton or silk–cotton"],"s":W+"Ikat",
 "x":[A("Patola","Fine silk double ikat of Patan, Gujarat, prized in the spice trade and copied in Bali.",W+"Ikat",dt="double ikat · repeat or pictorial · six-metre sari length"),
  A("Pochampally ikat","Geometric ikat saris and dress fabric from Bhoodan Pochampally, Telangana.",W+"Pochampally_sari",a="Pochampalli ikat",dt="silk or cotton · geometric paagadu bandhu patterns"),
  A("Sambalpuri bandha","Odisha tie-dyed ikat with motifs such as the shankha.",W+"Sambalpuri_sari",a="Sambalpuri ikat",v=[("Khandua","","","Odisha ikat with Gita Govinda texts, worn at weddings")],dt="weft or double ikat · motif · cotton or silk"),
  A("Geringsing","Double-ikat tenun of the Bali Aga village of Tenganan Pegeringsingan, believed to carry protective power.",W+"Geringsing",dt="double ikat"),
  A("Kasuri","Japanese ikat with brushed-looking patterns from resist-dyed warp and weft.",W+"Kasuri",v=[("Tate-yoko gasuri","","","Okinawan double ikat")],dt="warp, weft or double ikat"),
  A("Atlas (etles)","Uyghur and Uzbek silk ikat with bold patterns.",W+"Etles_silk",a="khan-atlas · etles · abrbandi",
   v=[("Qara-atlas","","","black, for older women"),("Khoja'e-atlas","","","yellow, blue or purple, for married women"),("Qizil-atlas","","","red, for girls"),("Yarkent-atlas","","","khan or royal atlas")],dt="silk satin · colour group · pattern"),
  A("Adras","Uzbek and Tajik ikat of half silk, half cotton, called 'royal' for its costly making.",W+"Adras_(fabric)",a="pādshāhī · shāhī",dt="half silk, half cotton"),
  A("Jaspe","Maya back-strap-woven ikat of Guatemala, used for the corte wrap skirt.",W+"Ikat",dt="pre-dyed warp · blurred figures")]})
K.append({"n":"Songket & tenun","a":"songket · sungkit · tenun · kain tenun","d":"Maritime Southeast Asian hand-woven cloth, songket being brocade with gold or silver supplementary weft.",
 "t":["Kain (lower wrap)","Sampin","Tengkolok head cloth","Gold, silver or nylon metallic thread"],"s":W+"Tenun",
 "x":[A("Palembang songket","Songket of South Sumatra, linked to Srivijaya and recognised as Indonesian heritage in 2013.",W+"Songket",y="8th century (depicted)",dt="silk · gold weft · motifs such as lepus, tretes, limar"),
  A("Pandai Sikek songket","Minangkabau songket of West Sumatra, recognised in 2014.",W+"Songket"),
  A("Silungkang songket","West Sumatran songket tradition recognised in 2019.",W+"Songket"),
  A("Terengganu songket","Malaysian east-coast songket; Malaysian songket was inscribed by UNESCO in 2021.",W+"Songket",v=[("Kelantan songket","","","")]),
  A("Ulos","Hand-woven tenun cloth of the Batak of North Sumatra, worn over the shoulder and given at weddings.",W+"Ulos",dt="ulos pargomgom given by the bride's parents at weddings")]})
K.append({"n":"Tartan cloth","a":"tartan · plaid · breacan","d":"Woollen cloth woven in setts of crossing coloured bands, most associated with Scotland.",
 "t":["Clan","District","Hunting","Dress","Mourning","Corporate","Kilt-weight wool or lighter poly-viscose"],"s":W+"Tartan",
 "x":[A("Government (Black Watch)","Sett of the Highland regiment raised in 1739, base of many later tartans.",W+"42nd_Regiment_of_Foot",y="1739",a="Black Watch · Government No. 1 · old Campbell",dt="modern, ancient or weathered colours"),
  A("Royal Stewart","Best-known Stewart sett and the British monarch's personal tartan, first published 1831.",W+"Royal_Stewart_tartan",y="1831",a="Royal Stuart",dt="red ground · modern or ancient colours"),
  A("Balmoral","Two-grey tartan created by Prince Albert and reserved for the royal family.",W+"Tartan",y="c. 1852"),
  A("Burberry check","Check introduced for the lining of Burberry trench coats.",W+"Tartan",mk="Burberry",y="1920s"),
  A("Prince Charles Edward Stuart","One of the oldest setts in continuous production, known from 18th-century samples.",W+"Tartan",y="mid-18th century"),
  A("Maple Leaf tartan","Canadian tartan designed in 1964 and an official national symbol since 2011.",W+"Tartan",y="1964")],
 "m":[["Kilt cloth","Lochcarron of Scotland"],["Tartan cloth","Kinloch Anderson"],["Tartan cloth","Johnstons of Elgin"]]})
K.append({"n":"Tweed cloth","a":"tweed · clò","d":"Rough, durable woollen cloth in plain, twill or herringbone weave, often with mixed-colour yarns.",
 "t":["Herringbone","Barleycorn","Check or overcheck","Plain twill","Jacket or coat weight"],"s":W+"Tweed",
 "x":[A("Harris tweed","Tweed handwoven at home in the Outer Hebrides from virgin wool dyed and spun there, protected by the Harris Tweed Act 1993.",W+"Harris_tweed",y="Act 1993",a="clò mór · clò hearach",dt="Orb certification stamp · pattern · weight"),
  A("Donegal tweed","Tweed from County Donegal with flecked yarns, hand-woven until mechanised looms arrived in the 1950s–60s.",W+"Donegal_tweed",v=[("Magee Donegal tweed","Magee of Donegal","","Donegal Town maker")],dt="nep flecks · hand or power loom"),
  A("Glen plaid","Woollen twill of small and large checks, also called Glen Urquhart or Prince of Wales check.",W+"Glen_plaid",a="Glenurquhart check · Prince of Wales check",dt="black/grey and white or muted colours · overcheck"),
  A("Houndstooth","Duotone broken-check pattern of light and dark tessellated checks.",W+"Houndstooth",a="dogstooth · dog's tooth",dt="scale: puppytooth to large · colour pair")],
 "m":[["Estate tweed","Johnstons of Elgin"],["Donegal tweed","Magee of Donegal"]]})
K.append({"n":"Khadi & handloom cloth","a":"khadi · khaddar · handloom","d":"Hand-spun and hand-woven natural-fibre cloth of the Indian subcontinent, promoted by Gandhi as swadeshi.",
 "t":["Cotton khadi","Silk khadi","Wool khadi","Muslin weight"],"s":W+"Khadi",
 "x":[A("Khadi","Hand-spun, hand-woven cloth first made at Gandhi's Sabarmati Ashram in 1917–18.",W+"Khadi",y="1917–18",v=[("KVIC khadi","","1957","Khadi and Village Industries Commission, statutory body")],dt="cotton, silk or wool · coarse to fine"),
  A("Jamdani","Figured fine muslin woven on the Shitalakshya river near Narayanganj, Bangladesh.",W+"Jamdani",dt="figured patterns · fineness"),
  A("Dhaka muslin","Extraordinarily fine Bengal handwoven cotton, 'woven air', made until the 18th century.",W+"Dhaka_muslin",y="medieval–18th century",a="Dhakai malmal",dt="thread count · transparency"),
  A("Chanderi","Traditional silk handloom sari cloth of Chanderi, Madhya Pradesh.",W+"Chanderi_sari",dt="silk")]})
K.append({"n":"Faso Dan Fani","a":"Faso Danfani · pagne tissé","d":"Burkinabè hand-spun cotton cloth woven in narrow strips and sewn into wrappers; name means 'woven cloth of the homeland'.",
 "t":["Wrapper (pagne)","Tailored garment cloth","Labelled authentic (since 2021)"],"s":"https://fr.wikipedia.org/wiki/Faso_Dan_Fani"})
K.append({"n":"Tapa & masi","a":"tapa · barkcloth · ngatu · siapo · masi · kapa","d":"Pacific barkcloth beaten from paper-mulberry inner bark and decorated by rubbing, stencilling or freehand painting.",
 "t":["Rubbed (kupesi board)","Stencilled","Freehand painted","Plain white"],"s":W+"Tapa_cloth",
 "x":[A("Ngatu","Tongan tapa, measured in named lengths for ceremonies.",W+"Tapa_cloth",v=[("Launima","","","15 m, five-sheet piece"),("Lautefuhi","","","30 m piece"),("Fātuua","","","8-piece")],dt="length · kupesi design"),
  A("Siapo","Samoan tapa, either rubbed or painted freehand.",W+"Tapa_cloth",v=[("Siapo 'elei","","","rubbing method"),("Siapo mamanu","","","freehand"),("Siapo vala","","","large ceremonial piece")],dt="Palauli village reputation"),
  A("Masi","Fijian tapa, made regularly mainly on Moce and Vatulele.",W+"Tapa_cloth",v=[("Masi kesa","","","stencilled"),("Masi kuvui","","","smoked brown"),("Masi vulavula","","","plain white"),("Masi vakarerega","","","yellow")]),
  A("Kapa","Hawaiian tapa.",W+"Tapa_cloth")]})
B=[
 {"n":"Vlisco","c":"Netherlands","f":"1846","seg":"wax-print textile house","d":"Helmond-based designer and maker of African wax-print fashion fabrics.","lines":["Vlisco","Woodin","Uniwax","GTP"],"eras":[],"sig":["Real wax print","Kente print"],"sc":[],"rel":["Akosombo Textile Limited","Printex"],"s":W+"Vlisco"},
 {"n":"Akosombo Textile Limited","c":"Ghana","f":"","seg":"wax-print mill","d":"Ghanaian mill beside the Akosombo Dam making real wax and fancy prints in 100% cotton.","lines":["ATL","ABC","Treasure"],"eras":[],"sig":["Real wax print","Fancy print","Kente print"],"sc":[],"rel":["Vlisco","Printex"],"s":W+"Akosombo_Textile_Limited"},
 {"n":"Printex","c":"Ghana","f":"1958","seg":"textile printer","d":"Accra textile printer, founded as Millet Textile Corporation, making African prints.","lines":[],"eras":[],"sig":["Fancy print"],"sc":[],"rel":["Akosombo Textile Limited","Vlisco"],"s":W+"Printex"},
 {"n":"Da Gama Textiles","c":"South Africa","f":"","seg":"shweshwe mill","d":"Eastern Cape mill making shweshwe since 1982 and owner of the Three Cats brand.","lines":["Three Cats"],"eras":[],"sig":["Three Cats"],"sc":[],"rel":[],"s":"https://www.dagama.co.za/three-cats-original-shweshwe-the-original-still-the-best/"},
 {"n":"Lochcarron of Scotland","c":"United Kingdom (Scotland)","f":"","seg":"tartan mill","d":"Scottish Borders weaver describing itself as the world's leading tartan manufacturer.","lines":["Strome kilt cloth","Knitwear","Scarves"],"eras":[],"sig":["Tartan cloth"],"sc":[],"rel":["Kinloch Anderson","Johnstons of Elgin"],"s":"https://www.lochcarron.co.uk/"},
 {"n":"Kinloch Anderson","c":"United Kingdom (Scotland)","f":"1868","seg":"kiltmaker and tartan house","d":"Edinburgh family firm of kiltmakers and tailors holding royal warrants.","lines":["Highland dress","1868 tweed collection"],"eras":["Six generations of the Kinloch Anderson family, 1868–"],"sig":["Tartan cloth"],"sc":[],"rel":["Lochcarron of Scotland"],"s":"https://www.kinlochanderson.com/discover/heritage/kinloch-anderson-timeline"},
 {"n":"Johnstons of Elgin","c":"United Kingdom (Scotland)","f":"1797","seg":"woollen and cashmere mill","d":"Family-owned Scottish mill weaving at Elgin and knitting at Hawick.","lines":[],"eras":[],"sig":["Tartan cloth","Tweed cloth"],"sc":[],"rel":["Lochcarron of Scotland"],"s":W+"Johnstons_of_Elgin"},
 {"n":"Magee of Donegal","c":"Ireland","f":"","seg":"tweed maker","d":"Donegal Town maker and retailer known for woollen Donegal tweed.","lines":[],"eras":[],"sig":["Donegal tweed"],"sc":[],"rel":[],"s":W+"Magee_of_Donegal"},
 {"n":"Burberry","c":"United Kingdom","f":"1856","seg":"luxury house","d":"London luxury house founded by Thomas Burberry, known for trench coats and its check.","lines":[],"eras":[],"sig":["Burberry check"],"sc":[],"rel":[],"s":W+"Burberry"}]
def T(n,g,r,p,d,tech,mat,forms,ctr,auth,s): return dict(n=n,g=g,r=r,p=p,d=d,tech=tech,mat=mat,forms=forms,ctr=ctr,auth=auth,s=s)
G="Textiles & rugs"
TR=[
 T("Asante kente weaving",G,"Ashanti Region, Ghana","18th century onwards","Akan strip weaving of named-pattern kente, traced by oral tradition to Bonwire.","Narrow-strip loom weaving with multiple heddles; strips sewn together","Silk, cotton, rayon",["Asante kente","Kente cloth"],["Bonwire","Kente Festival, Bonwire"],"Hand-woven strips sewn edge to edge (not printed); kente is a Ghanaian geographical indication",W+"Kente_cloth"),
 T("Ewe kente weaving",G,"South-eastern Ghana and Togo","16th century onwards (oral tradition)","Ewe strip weaving with double-woven bands.","Double-woven strip weaving","Cotton, rayon",["Ewe kente"],["Keta"],"Hand-woven double bands",W+"Kente_cloth"),
 T("African wax printing",G,"Netherlands and West Africa","19th century onwards","Industrial resin-resist printing of batik-inspired cloth for African markets.","Resin resist with wooden stamp blocks per colour","Cotton",["Real wax print","Fancy print"],["Helmond","Akosombo","Accra"],"Maker name, product and design number printed on the selvedge; design equally clear on both faces",W+"African_wax_prints"),
 T("Indonesian batik",G,"Java and other Indonesian islands","centuries old; UNESCO 2009","Wax-resist dyeing with symbolic motifs that mark life events from birth to burial.","Hot wax drawn with canting (tulis) or stamped with copper cap, repeated dyeing","Cotton, silk, wax, vegetable and synthetic dyes",["Parang","Kawung","Truntum","Sidomukti","Megamendung"],["Yogyakarta","Surakarta","Pekalongan","Cirebon (Trusmi)","Lasem"],"Batik tulis allows very fine hand-drawn detail; batik cap repeats stamped units with less detail","https://ich.unesco.org/en/RL/indonesian-batik-00170"),
 T("Shweshwe printing",G,"South Africa and Lesotho","1840s onwards","Indigo-based discharge-printed cotton adopted into Basotho and Xhosa dress.","Acid discharge roller printing","Cotton calico",["Three Cats"],["Da Gama mill, Eastern Cape"],"Three Cats backstamp, stiff starched handle and distinctive starch smell","https://www.dagama.co.za/three-cats-original-shweshwe-the-original-still-the-best/"),
 T("Bogolan mud-dyeing",G,"Mali","traditional","Malian cotton cloth patterned with fermented mud.","Mud-dye painting on strip-woven cotton","Cotton, fermented mud",["Bogolan"],[],"",W+"B%C3%B2g%C3%B2lanfini"),
 T("Yoruba adire",G,"South-western Nigeria","traditional","Indigo resist-dyed cloth made by Yoruba women.","Tie-dye, stitching, stencilling, hand-painted resist","Cotton, indigo",["Adire"],[],"",W+"Adire_(textile_art)"),
 T("Yoruba aso-oke weaving",G,"Yorubaland (Nigeria, Benin, Togo)","traditional","Hand-woven Yoruba strip cloth for ceremonial dress.","Strip weaving, usually by men","Cotton, silk",["Aso oke"],[],"",W+"Aso_oke"),
 T("Central Asian ikat",G,"Uzbekistan, Tajikistan, Xinjiang","19th century flowering","Silk and half-silk ikat with bold patterns from the Silk Road oases.","Warp ikat (abrband)","Silk, cotton",["Atlas (etles)","Adras"],["Margilan","Bukhara","Samarkand","Hotan","Kashgar"],"",W+"Etles_silk"),
 T("Indian ikat",G,"Gujarat, Telangana, Odisha","traditional","Single and double ikat saris and cloth of India.","Warp, weft and double ikat","Silk, cotton",["Patola","Pochampally ikat","Sambalpuri bandha"],["Patan","Bhoodan Pochampally","Sambalpur","Bargarh"],"Pattern visible equally on both faces with slight blurring at motif edges",W+"Ikat"),
 T("Songket weaving",G,"Sumatra, Malay Peninsula, Brunei, Bali, Lombok","8th century onwards","Brocade with gold or silver supplementary weft for ceremonial dress.","Supplementary weft weaving","Silk, cotton, gold and silver thread",["Palembang songket","Pandai Sikek songket","Terengganu songket"],["Palembang","Pandai Sikek","Silungkang","Terengganu","Kelantan","Sambas"],"Hand-woven metallic weft floats; nylon metallic thread in cheaper pieces",W+"Songket"),
 T("Scottish tartan weaving",G,"Scotland","16th century onwards","Woollen sett weaving of clan, district, dress and corporate tartans.","Twill weaving of colour setts","Wool, poly-viscose",["Government (Black Watch)","Royal Stewart","Balmoral"],["Lochcarron, Selkirk","Elgin","Edinburgh"],"Sett recorded in the Scottish Register of Tartans (since 2009)",W+"Scottish_Register_of_Tartans"),
 T("Harris tweed weaving",G,"Outer Hebrides, Scotland","19th century onwards","Home-woven island tweed protected by statute.","Hand weaving at weavers' homes; dyeing, spinning and finishing on the islands","Pure virgin wool",["Harris tweed"],[],"Orb certification mark stamped on the cloth; definition under the Harris Tweed Act 1993",W+"Harris_tweed"),
 T("Donegal tweed weaving",G,"County Donegal, Ireland","centuries","Flecked Irish tweed, hand-woven until the 1950s–60s.","Hand and power-loom weaving","Wool",["Donegal tweed"],["Donegal Town"],"",W+"Donegal_tweed"),
 T("Khadi and Bengal handloom",G,"India and Bangladesh","medieval to present","Hand-spun and hand-woven cloth from fine Bengal muslins to Gandhian khadi.","Hand spinning and handloom weaving","Cotton, silk, wool",["Khadi","Jamdani","Dhaka muslin"],["Sabarmati Ashram","Narayanganj","Dhaka"],"",W+"Khadi"),
 T("Faso Dan Fani weaving",G,"Burkina Faso","traditional; promoted 1983–87","Hand-spun cotton strip cloth, revived as a national symbol.","Women spin and dye; narrow strips woven on horizontal looms and sewn together","Cotton",["Faso Dan Fani"],["Ouagadougou","Bobo-Dioulasso","Koudougou"],"Official authenticity label since 2021","https://fr.wikipedia.org/wiki/Faso_Dan_Fani"),
 T("Pacific tapa making",G,"Tonga, Samoa, Fiji, Hawaii and wider Pacific","traditional","Barkcloth beaten from inner bark and decorated for ceremony and exchange.","Beating with ike mallets on tutua anvils; rubbing over kupesi boards, stencilling, painting","Paper mulberry, breadfruit and fig bark",["Ngatu","Siapo","Masi","Kapa"],["Moce","Vatulele","Palauli"],"",W+"Tapa_cloth")]
notes=("New shelf, no old kinds. 13 kinds, all sourced. Left out (not attested this session): Hitarget and other Chinese wax-print copiers; ABC Wax brand page (Wikipedia article missing; kept only as a version name); Uniwax, GTP and Woodin as separate brand entries (covered as Vlisco lines); Danar Hadi, Batik Keris, Iwan Tirta (no page retrieved); Yodgorlik (Margilan) factory; Harris Tweed mills and Harris Tweed Authority (authority page came via a stealth proxy so not used); Donegal makers other than Magee; named aso-oke types (sanyan, alaari, etu) and adire eleko/oniko not confirmed on retrieved pages; shweshwe brands other than Three Cats; Kawung/Truntum/Sidomukti have only the Batik article as source. "
 "Bogolan and Faso Dan Fani have no archetypes (no named forms confirmed). Patola, Pochampally, Sambalpuri and Chanderi also appear as saris in South Asian dress; here they are the cloth.")
out={"kinds":K,"brands":B,"traditions":TR,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/A1/shelves/07_07.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(len(K),sum(len(k.get('x',[])) for k in K),len(B),len(TR))
