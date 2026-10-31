import sys; sys.path.insert(0,'work/C3/agent'); from w import w
def X(n,a,d,s,y='',v=(),dt='',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if dt: x["dt"]=dt
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
HMF_F="https://www.helpmefind.com/rose/l.php?l=2.43514"; HMF_A="https://www.helpmefind.com/rose/l.php?l=2.39107"
PN1="https://perishablenews.com/?p=149052"; PN2="https://perishablenews.com/?p=159348"
SG="https://en.wikipedia.org/wiki/Lilium_%27Stargazer%27"; CB="http://www.harvesting-history.com/?p=27972"
HOL="https://shop.holex.com/en_US/chrysanthemums"; TT="https://thursd.com/articles/the-top-5-most-sold-tulips"
RHS="https://www.rhs.org.uk/plants/155532/tulipa-strong-gold-3/details"; DC="https://en.wikipedia.org/wiki/Dianthus_caryophyllus"
KW="https://www.kelways.co.uk/paeonia-lactiflora-sarah-bernhardt/p49248"
LC="https://lynchcreekwreaths.com/blogs/the-farm/the-art-of-holiday-wreaths-lynch-creek-farm-s-signature-seasonal-statement"
NIP="https://www.nippon.com/en/japan-glances/jg00086/"
kinds=[
 {"n":"Cut rose","a":"florist's rose","d":"Fresh-cut rose stems, singly or as a bunch, mostly florist's hybrid teas grown for the trade.",
  "t":["standard (single-headed)","spray","garden rose","long-stemmed"],"s":"https://bloomingmore.com/products/24-farm-fresh-red-roses-40-cm","x":[
  X("'Freedom'","TAN97544","Medium red, very double florist's hybrid tea; a standard red cut rose.",HMF_F,y="2004",mk="Rosen Tantau",
    v=[("'Freedom'","Rosen Tantau","2004","bred by Hans Jürgen Evers 1997, introduced in Germany 2004")],dt="stem length · head size"),
  X("'Explorer'","","Intense velvet-red hybrid tea cut rose with a large head, grown mainly in Ecuador and Colombia.",PN1,y="2011",mk="Interplant Roses",
    v=[("'Explorer'","Interplant Roses","2011","intense velvet red"),("'Hot Explorer'","Interplant Roses","","deep pink"),("'Royal Explorer'","Interplant Roses","","blood red")],dt="stem length · head size"),
  X("'Avalanche+'","'Lexani'","White florist's hybrid tea with a vanilla centre and lime edge, bred by Lex Voorn in the Netherlands.",HMF_A,dt="stem length · head size"),
 ]},
 {"n":"Cut lily","a":"","d":"Fresh-cut lily stems.","t":["Oriental","Asiatic","LA hybrid","longiflorum (Easter lily)"],
  "s":"https://fiftyflowers.com/products/white-oriental-lilies","x":[
  X("'Casa Blanca'","Casablanca","Strongly fragrant crystalline-white Oriental lily, introduced 1984.",CB,y="1984",dt="buds per stem · stem length"),
  X("'Stargazer'","","Oriental hybrid lily with upward-facing flowers, created by California breeder Leslie Woodriff.",SG,y="1974",dt="buds per stem · stem length"),
 ]},
 {"n":"Cut chrysanthemum","a":"florist's mum · chrysanth","d":"Fresh-cut chrysanthemum stems, single-headed (disbud), spray or santini.",
  "t":["single-headed","spray","santini (mini)","daisy","cushion","spider","pompom"],"s":"https://freshdi.com/product/Fresh-Cut-Chrysanthemum-Flowers-XSQuNP",
  "m":[["Chrysanth Spray Baltica",""],["Chrysanth Spray Chic",""],["Chrysanth Santini Lassie",""]]},
 {"n":"Cut tulip","a":"","d":"Fresh-cut tulip stems sold in bunches.","t":["single early","Triumph","double","parrot","fringed"],"s":TT,"x":[
  X("'Strong Gold'","","Buttery-yellow long-stemmed tulip, among the most sold tulips; RHS Award of Garden Merit.",RHS,dt="stem length · bunch size"),
  X("'Leen van der Mark'","","Cardinal-red tulip with a golden edge fading to white, from Konijnenburg & Mark.",TT),
  X("'Purple Prince'","","Royal-purple single early tulip used in bouquets.",TT),
  X("'Jan Seignette'","","Cardinal-red tulip edged buttercup yellow, with tall robust stems.",TT),
 ]},
 {"n":"Cut carnation","a":"Dianthus caryophyllus · clove pink","d":"Fresh-cut carnation stems, one of the main cut flowers of the world.","t":["standard","spray","micro"],"s":DC,"x":[
  X("'Moondust'","","Blue-mauve carnation made by genetic engineering by Florigene and commercialised.",DC,y="c. 1996",
    v=[("'Moondust'","","c. 1996","blue-mauve"),("'Moonshade'","","1998","violet")]),
 ]},
 {"n":"Cut peony","a":"","d":"Fresh-cut herbaceous peony stems.","t":["single","semi-double","double","bomb"],"s":KW,"x":[
  X("'Sarah Bernhardt'","Paeonia lactiflora 'Sarah Bernhardt'","Large double apple-blossom-pink scented peony; the most widely grown cut-flower peony.",KW,y="1906",mk="Lemoine",dt="bud size · stem length"),
 ]},
 {"n":"Mixed bouquet","a":"mixed fresh bouquet or arrangement","d":"Made-up bouquet or arrangement of fresh-cut flowers of several kinds; single-kind bunches go with their own cut flower.",
  "t":["hand-tied","vase arrangement","posy","bridal bouquet","letterbox flowers","flower subscription","ikebana arrangement"],"s":"https://www.interflora.co.uk/category/next-day-flowers?page=8"},
 {"n":"Fresh wreath","a":"","d":"Wreath made of fresh-cut living foliage.","t":["Christmas wreath","door wreath","table wreath with candles","funeral wreath"],
  "s":"https://lynchcreekwreaths.com/blogs/the-farm/fresh-christmas-wreaths","m":[["Lynch Creek The Traditional","Lynch Creek Farm"],["Lynch Creek Country Christmas","Lynch Creek Farm"]]},
]
brands=[
 {"n":"Rosen Tantau","c":"Germany","f":"1906","seg":"Specialist","kf":"rose breeding","d":"Rose breeder at Uetersen, breeder of garden and cut roses such as 'Freedom'.","sig":["'Freedom'"],"s":"knowledge"},
 {"n":"Interplant Roses","c":"Netherlands","seg":"Specialist","kf":"cut-rose breeding","d":"Dutch cut-rose breeder whose 'Explorer' family is grown mainly in Ecuador and Colombia.","sig":["'Explorer'"],"s":PN1},
 {"n":"Lemoine","c":"France","seg":"Heritage manufactory","kf":"peonies, lilacs","d":"Nancy nursery of Victor Lemoine and family that bred peonies and lilacs, including 'Sarah Bernhardt'.","sig":["'Sarah Bernhardt'"],"s":KW},
 {"n":"Lynch Creek Farm","c":"United States","seg":"Artisan & independent","kf":"fresh wreaths","d":"Pacific Northwest maker of fresh noble-fir Christmas wreaths sold by mail.","s":LC},
]
trads=[{"n":"Ikebana","g":"Flowers & plants","r":"Japan","p":"late 15th century–present","d":"Japanese art of flower arrangement (kadō, 'way of the flower') rooted in Buddhist flower offerings.",
 "tech":"asymmetric arrangement of seasonal flowers, branches, stones and moss; stems held on a kenzan, cut with hanabasami",
 "mat":"seasonal flowers and branches; ceramic, glass, wood, bamboo or metal containers",
 "forms":["rikka","shōka","moribana","heika"],"ctr":["Ikenobō (Ikenobō Senkei, Muromachi period)","Ohara (Ohara Unshin, late 19th century)","Sōgetsu (Teshigahara Sōfū, 1927)"],
 "auth":"school certificates and teaching ranks; arrangements follow a school's named styles","s":NIP}]
w('C3','09_00',{"kinds":kinds,"brands":brands,"traditions":trads,"notes":"All five old kinds kept with old s; cut tulip, carnation and peony added. Rose archetypes Freedom, Explorer, Avalanche+ sourced; Avalanche+ and Stargazer/Casa Blanca breeders are individuals (Lex Voorn, Leslie Woodriff) so mk left empty; Casa Blanca breeder unconfirmed. Chrysanthemum has no single reference cultivar page: types spray/single-headed/santini plus three Holex-listed varieties as m (maker unknown). Wreath models trimmed from four to two Lynch Creek wreaths named on the retrieved page and in old data. No Royal FloraHolland page retrieved."})
