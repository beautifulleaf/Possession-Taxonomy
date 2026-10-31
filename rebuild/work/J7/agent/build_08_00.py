import json, os
P='https://palateproject.co/collections/'
def X(n,d,mk,s,v=(),dt='',a='',y=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a_,"mk":b,"y":c,"d":e} for a_,b,c,e in v],"dt":dt}
GR="Junmai · Tokubetsu junmai · Junmai ginjo (≤60% polish) · Junmai daiginjo (≤50% polish)"
common=["Polishing ratio (seimaibuai, % of grain remaining)","Starter: kimoto · yamahai · sokujō","Namazake (unpasteurised) · genshu (undiluted) · muroka (unfiltered)","Koshu (aged sake)","Taruzake (cedar-cask)"]
kinds=[
{"n":"Junmai sake","a":"junmai-shu · pure rice sake","d":"Sake made only from rice, koji and water, with no brewer's alcohol added.",
 "t":[GR]+common,"s":"https://www.masterofmalt.com/sake/",
 "x":[
  X("Dassai","Asahi Shuzo's junmai daiginjo from Yamada-nishiki rice, the label number giving the polishing ratio.","Asahi Shuzo (Yamaguchi)",
    "https://www.nippon.com/en/features/c00618/dassai-how-a-rural-sake-brewery-took-on-the-world.html",
    [("Dassai 23","Asahi Shuzo (Yamaguchi)","1992","rice milled to 23%; flagship"),
     ("Dassai 39","Asahi Shuzo (Yamaguchi)","","junmai daiginjo, 39% polish"),
     ("Dassai 45","Asahi Shuzo (Yamaguchi)","","junmai daiginjo, 45% polish"),
     ("Dassai Beyond","Asahi Shuzo (Yamaguchi)","","top junmai daiginjo; ratio not stated"),
     ("Dassai Blue 50 · 35 · 23","Asahi Shuzo (Yamaguchi)","2023","brewed at DASSAI Blue Sake Brewery, Hyde Park, New York")],
    "polishing ratio 23–50% · Japan vs. New York brewery · nigori variant","otter festival",y="1990"),
  X("Juyondai","Takagi Shuzo's 'fourteenth generation' label, among the most sought-after Yamagata sake.","Takagi Shuzo",
    "https://www.skurnik.com/producer/takagi-shuzo/",
    [("Juyondai Bessen Junmai Daiginjo","Takagi Shuzo","",""),("Juyondai Tokujo Omachi Junmai Daiginjo","Takagi Shuzo","","Omachi rice")],
    "grade · rice variety (Omachi and others) · Yamagata"),
  X("Gekkeikan","Kyoto house brand of one of the oldest sake brewers, made in Fushimi and in Folsom, California.","Gekkeikan",
    "https://en.wikipedia.org/wiki/Gekkeikan",
    [("Gekkeikan Black & Gold","Gekkeikan","","junmai, 70% polish; blend of Traditional and Haiku, made in Folsom, California"),
     ("Gekkeikan Horin Junmai Daiginjo","Gekkeikan","","50% polish; Kyoto Prefecture")],
    "Kyoto vs. California brewing · grade",y="1637"),
  X("Akashi-Tai","Family brewery's Hyōgo sake named after Akashi sea bream, widely exported.","Akashi-Tai",
    "https://www.diffordsguide.com/producers/287/akashi-sake-brewery-company-ltd",
    [("Akashi-Tai Junmai Daiginjo Genshu","Akashi-Tai","","undiluted"),("Akashi-Tai Junmai Tokubetsu","Akashi-Tai","",""),("Akashi-Tai Junmai Ginjo","Akashi-Tai","","")],
    "grade · genshu vs. diluted · Akashi, Hyōgo"),
 ],
 "m":[["Tenbi Junmai Ginjo Hotaten","Choshu Sake Brewery"],["Bijofu Junmai Ginjo Cel-24","Hamakawa Shoten"],["Hanamoyou 1988 Vintage Aged Junmai Sake","Hanayoisyuzo"],["Kid Junmai","Heiwa Shuzou"],["Junmai Kagura Unfiltered Undiluted Midnight Blue","Matsui Sake Brewery"],["Chiebijin Junmaishu","Nakano Shuzo Sake Breweries"],["Black Chosan","Niigata Meijo"],["Koshino Kanchubai Gold Label","Niigata Meijo"],["Junmai Daiginjo Zankyo Super7","Niizawa Sake Brewery"],["Raifuku Junmai Daiginjo Aiyama","Raifuku Sake Brewing"],["SAKE HUNDRED Byakko Bespoke","SAKE HUNDRED"],["SOTO Junmai","SOTO Sake"],["Sanran Junmai Ginjo Yumesasara","Tonoikeshuzouten"]]},
{"n":"Honjozo, ginjo & daiginjo sake","a":"honjōzō · ginjō · daiginjō · aruten (alcohol-added) sake","d":"Special-designation sake with a small legal amount of brewer's alcohol added, graded by polishing ratio.",
 "t":["Honjōzō (≤70% polish) · Tokubetsu honjōzō (≤60%) · Ginjō (≤60%) · Daiginjō (≤50%)"]+common,"s":"https://www.masterofmalt.com/sake/",
 "x":[
  X("Dewazakura Oka Ginjo","Ginjo sold at an everyday price from 1980, credited with starting Japan's ginjo boom.","Dewazakura",
    "https://www.dewazakura.co.jp/en/dewazakura/01.html",[],"pasteurised vs. nama · Tendo, Yamagata","Ouka · Cherry Bouquet",y="1980"),
  X("Kokuryu Daiginjo Ryu","Fukui daiginjo described as the first daiginjo sold nationwide.","Kokuryu",
    "https://openers.jp/en/lounge/9883",[("Kokuryu Crystal Dragon Daiginjo","Kokuryu","","Gohyakumangoku rice, 50% polish")],"soft Kuzuryu river water · Fukui"),
  X("Hakkaisan","Minami-Uonuma, Niigata range made in small batches with handmade koji, from honjozo to snow-aged daiginjo.","Hakkaisan",
    "https://en.imadeya.co.jp/blogs/brewery/hatsukaisan",
    [("Hakkaisan Tokubetsu Honjozo","Hakkaisan","",""),("Hakkaisan Daiginjo","Hakkaisan","","45% polish"),("Hakkaisan Junmai Ginjo 55%","Hakkaisan","",""),
     ("Hakkaisan Tokubetsu Junmai","Hakkaisan","",""),("Hakkaisan Junmai Daiginjo","Hakkaisan","",""),("Hakkaisan Yukimuro 3 Years Snow Aged","Hakkaisan","","aged in a snow store")],
    "grade · snow-aged · genshu · Niigata"),
  X("Kubota","Asahi-Shuzo's Niigata range sold in named tiers.","Asahi-Shuzo (Niigata)","https://palateproject.co/collections/niigata-prefecture",
    [("Kubota Senju","Asahi-Shuzo (Niigata)","",""),("Kubota Hekiju","Asahi-Shuzo (Niigata)","",""),("Kubota Manju","Asahi-Shuzo (Niigata)","","top tier"),
     ("Kubota Junmai Daiginjo","Asahi-Shuzo (Niigata)","",""),("Kubota Seppou White · Black","Asahi-Shuzo (Niigata)","","")],
    "tier (Senju · Hekiju · Manju) · Niigata"),
 ],
 "m":[["Akashi-Tai Daiginjo Genshu","Akashi-Tai"],["Kikusui Honjozo Shiroki Tenryu","Kikusui Brewery"],["Kisoji Honjozo Kinmonnishiki","Yukawa Sake Brewery"]]},
{"n":"Futsūshu","a":"everyday sake · non-designated sake · table sake","d":"Ordinary sake outside the eight special designations, where more added alcohol is allowed.",
 "t":["Cup sake · carton · bottle","Served warm (kan) or chilled"],"s":"https://shop.creewine.com/sake/Tozai-Typhoon-Futsushu-Premium-Sake-Tozai-Typhoon-Futsushu-Premium-Sake-w173210988",
 "m":[["Tozai Typhoon Futsushu","Tozai"]]},
{"n":"Nigori sake","a":"nigorizake · cloudy sake","d":"Sake strained through a coarse mesh so that rice sediment stays in it.",
 "t":["Usu-nigori (lightly cloudy) · thick nigori","Any grade (junmai, ginjo, daiginjo)","Sparkling (active) nigori"],"s":"https://shop.takarasake.com/products/nigori-silky-mild",
 "x":[
  X("Sho Chiku Bai Nigori","Takara's Berkeley-brewed cloudy sake, a common nigori in the US.","Takara Sake USA","https://shop.takarasake.com/products/nigori-silky-mild",
    [("Sho Chiku Bai Nigori Silky Mild","Takara Sake USA","","Calrose rice, 70% polish"),("Sho Chiku Bai Nigori Crème de Sake","Takara Sake USA","","sweeter, thicker")],"sweetness · bottle size 375 ml–1.5 l"),
  X("Hakutsuru Sayuri","Nada-brewed cloudy sake from Hakutsuru.","Hakutsuru",P+"hakutsuru-brewing-company",[],"Nada, Kobe"),
 ],
 "m":[["Dassai 45 Nigori","Asahi Shuzo (Yamaguchi)"]]},
{"n":"Sparkling sake","a":"awa sake · happōshu sake","d":"Sake carbonated by secondary fermentation in bottle or by added gas.",
 "t":["Bottle-fermented · tank or gas-carbonated","Clear · cloudy"],"s":"https://www.marketviewliquor.com/product/hakutsuru-awayuki-sparkling-sake-300ml",
 "x":[X("Awa Hakkaisan","Hakkaisan's bottle-fermented sparkling sake made with white koji.","Hakkaisan","https://en.imadeya.co.jp/blogs/brewery/hatsukaisan",[],"cork-finished bottle · white koji")],
 "m":[["Awayuki","Hakutsuru"]]},
{"n":"Infused sake","a":"yuzushu · sake-based umeshu · fruit sake","d":"Sake steeped or blended with fruit such as yuzu or ume plum.",
 "t":["Yuzu · ume · other fruit","Sake base grade"],"s":"https://www.slowood.hk/products/umeshu-classic-rice-wine-based-100ml",
 "m":[["Akashi-Tai Ginjo Yuzushu","Akashi-Tai"],["Akashi-Tai Shiraume Ginjo Umeshu","Akashi-Tai"],["Dassai Blue Yuzu","Asahi Shuzo (Yamaguchi)"],["Dassai 23 Umeshu","Asahi Shuzo (Yamaguchi)"]]},
]
def B(n,c,f,seg,d,lines,sig,s,rel=(),eras=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Asahi Shuzo (Yamaguchi)","Japan","","Sake brewery","Iwakuni, Yamaguchi brewery revived by Hiroshi Sakurai; also brews Dassai Blue in Hyde Park, New York.",["Dassai","Dassai Blue"],["Dassai"],"https://www.nippon.com/en/features/c00618/dassai-how-a-rural-sake-brewery-took-on-the-world.html",eras=["Hiroshi Sakurai, president, 1984–"]),
 B("Asahi-Shuzo (Niigata)","Japan","1830","Sake brewery","Nagaoka, Niigata brewery best known for its Kubota range.",["Kubota"],["Kubota"],"knowledge",rel=["Hakkaisan"]),
 B("Takagi Shuzo","Japan","1615","Sake brewery","Murayama, Yamagata family brewery; Juyondai named for the fourteenth generation.",["Juyondai"],["Juyondai"],"https://www.skurnik.com/producer/takagi-shuzo/",eras=["Akitsuna Takagi, fifteenth-generation owner, 1993–"]),
 B("Gekkeikan","Japan","1637","Sake brewery","Fushimi, Kyoto brewer founded by Jiemon Ōkura; US subsidiary in Folsom, California.",["Gekkeikan","Horin","Black & Gold"],["Gekkeikan"],"https://en.wikipedia.org/wiki/Gekkeikan",rel=["Hakutsuru","Takara Sake USA"]),
 B("Akashi-Tai","Japan","1886","Sake brewery","Yonezawa family's Akashi Sake Brewery in Akashi, Hyōgo, making sake and fruit liqueurs.",["Akashi-Tai"],["Akashi-Tai"],"https://www.diffordsguide.com/producers/287/akashi-sake-brewery-company-ltd"),
 B("Dewazakura","Japan","1892","Sake brewery","Tendo, Yamagata brewery founded by Seijiro Nakano; Oka Ginjo began the ginjo boom.",["Oka","Dewasansan"],["Dewazakura Oka Ginjo"],"https://www.dewazakura.co.jp/en/dewazakura/01.html"),
 B("Kokuryu","Japan","1804","Sake brewery","Eiheiji, Fukui ginjo brewery founded by Ishidaya Nizaemon.",["Kokuryu","Kuzuryu"],["Kokuryu Daiginjo Ryu"],"https://openers.jp/en/lounge/9883"),
 B("Hakkaisan","Japan","1925","Sake brewery","Hakkai Jozo of Minami-Uonuma, Niigata, at the foot of Mount Hakkai.",["Hakkaisan","Awa Hakkaisan"],["Hakkaisan","Awa Hakkaisan"],"https://en.imadeya.co.jp/blogs/brewery/hatsukaisan",rel=["Asahi-Shuzo (Niigata)"]),
 B("Hakutsuru","Japan","1743","Sake brewery","Large Nada-Gogō brewer in Kobe.",["Hakutsuru","Sayuri","Ukiyoe"],["Hakutsuru Sayuri"],P+"hakutsuru-brewing-company",rel=["Gekkeikan"]),
 B("Takara Sake USA","United States","","Sake brewery","Berkeley, California brewer of Sho Chiku Bai, subsidiary of Japan's Takara group.",["Sho Chiku Bai"],["Sho Chiku Bai Nigori"],"https://shop.takarasake.com/products/nigori-silky-mild",rel=["Gekkeikan"]),
]
trad=[{"n":"Nada-Gogō sake brewing","g":"Food & drink","r":"Kobe and Nishinomiya, Hyōgo, Japan","p":"from 1330; rise from the Kan'ei period (17th century)",
 "d":"Five brewing districts producing about a quarter of Japan's sake, known for strong, full sake.","tech":"Tanba tōji brewmasters; cold Rokkō oroshi winds slow fermentation",
 "mat":"Miyamizu hard water from Mount Rokkō; Yamada Nishiki rice","forms":["Junmai sake","Honjozo, ginjo & daiginjo sake"],"ctr":["Hakutsuru"],
 "auth":"Nada-Gogō geographical indication on the label","s":"https://en.wikipedia.org/wiki/Nada-Gog%C5%8D"}]
notes=("All 6 planned kinds kept (Sake with brewer's alcohol renamed Honjozo, ginjo & daiginjo; Everyday sake -> Futsūshu; Infused rice wine -> Infused sake). "
 "Grades, polishing ratio, kimoto/yamahai, namazake/genshu and koshu are types. Old Akashi-Tai junmai models became versions; 'Akashi-Tai sake range' r dropped (brand in register). "
 "Dropped old models SAKE HUNDRED Nikou/Shirin (SKU noise; one SAKE HUNDRED kept). Tozai Typhoon given maker 'Tozai' from its name. "
 "Left out: Sho Chiku Bai Classic Junmai, Kubota Manju grade/year, Hakutsuru Awayuki details, Kikusui Funaguchi - sources blocked (masterofmalt/tippsy 429, gltjp/takarasake 403, JETRO 503) or not retrieved. "
 "Asahi-Shuzo (Niigata) brand entry from knowledge. Prefecture given in archetype details.")
out={"kinds":kinds,"brands":brands,"traditions":trad,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/08_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
