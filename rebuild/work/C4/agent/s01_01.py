import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
FT=W+'Four_Treasures_of_the_Study'; HB=W+'Huzhou_ink_brush'; IS=W+'Inkstone'; IK=W+'Inkstick'; WA=W+'Washi'; SE=W+'Seals_in_the_Sinosphere'
KG='https://artshedonline.com.au/kuretake-gansai-tambi-watercolour-set-sumi-colours'; MW=W+'Mino_washi'; UN='https://ich.unesco.org/en/decisions/9.COM/10.22'
IB=W+'Ink_brush'; XP=W+'Xuan_paper'; KB='https://nihonmono.jp/en/?p=9754'; JC=W+'Japanese_calligraphy'
kinds=[
{"n":"Calligraphy and ink-painting brush","a":"fude · maobi · sumi-e brush","d":"Soft-haired brush for calligraphy and ink painting, graded by hair type and size.","s":IB,
 "t":["soft hair (goat)","hard hair (wolf, weasel)","mixed hair","big, medium and small sizes","brush pen (fudepen)"],
 "x":[X("Hu brush (Huzhou ink brush)","",HB,"Chinese brush from Shanlian, Huzhou, Zhejiang, the best-known of the Four Treasures brushes; brushmaking traced to the Qin dynasty.",dt="hair: goat, rabbit, wolf, mixed · size · hair length"),
      X("Japanese fude","",JC,"Japanese brush used in shodō, the brush of the Four Treasures of the Study.",dt="hair, size and length")]},
{"n":"Inkstick and liquid sumi ink","a":"ink cake · sumi · bokujū","d":"Solid soot-and-glue inkstick ground on an inkstone, or bottled liquid sumi for beginners.","s":IK,
 "t":["pine-soot ink (blue-black)","oil-soot ink (warm black)","liquid ink (bokujū)","coloured inkstick (cinnabar)"],
 "x":[X("Hui ink (Huīmò)","",FT,"Chinese inkstick tradition of Shexian, Anhui, regarded as the finest for calligraphy.",dt="pine or oil soot · glue · aromatics"),
      X("Nara sumi","Kobaien",KB,"Japanese oil-soot sumi by the Nara shop opened in 1577, using soot from burning rapeseed and sesame oil (yuen-zumi).","1577",dt="yuen-zumi oil soot · older pine-soot shoen-zumi")]},
{"n":"Inkstone","a":"suzuri · yan","d":"Stone slab with a grinding hill and ink well for grinding inksticks with water.","s":IS,
 "t":["Duan stone","She stone","Tao stone","Chengni (ceramic)","Japanese suzuri"],
 "x":[X("Duan inkstone","",IS,"Purple to purple-red volcanic tuff from Zhaoqing, Guangdong, with distinctive stone eyes; first of the Four Famous Inkstones.",dt="graded by quarry"),
      X("She inkstone","",IS,"Black slate with gold-like markings from Anhui and Jiangxi, used since the Tang dynasty.",dt=""),
      X("Tao (Taohe) inkstone","",IS,"Jade-like crystalline stone from the Tao River, Gansu; rare today.",dt=""),
      X("Chengni inkstone","",IS,"Ceramic inkstone of Tang origin, traditionally associated with Luoyang.",dt="")]},
{"n":"Xuan (rice) paper","a":"xuanzhi · Chinese rice paper","d":"Strong, smooth Chinese paper from Jing County, Anhui, made of blue sandalwood bark, sold raw, half-ripe or ripe.","s":XP,
 "t":["raw (shengxuan)","half-ripe (banshuxuan)","ripe (shuxuan)","sandalwood-bark content grades"],
 "x":[X("Xuan paper (Jing County)","",XP,"Paper first made in Tang-dynasty Jing County; UNESCO-listed in 2009; raw type blurs ink, ripe type is alum-sized.","Tang dynasty",v=[("Shengxuan","raw, unsized, absorbent"),("Banshuxuan","half-ripe"),("Shuxuan","ripe, alum-sized, suits gongbi")],dt="blue sandalwood bark · rice straw · raw/ripe")]},
{"n":"Washi paper","a":"Japanese paper","d":"Handmade Japanese paper from kozo, gampi or mitsumata fibre, used for calligraphy, printing and conservation.","s":WA,
 "t":["kozo (paper mulberry)","gampi","mitsumata","nagashi-zuki (thin)","tame-zuki (thick)"],
 "x":[X("Mino washi (Hon-minoshi)","",MW,"Paper-mulberry paper of Gifu Prefecture dating to the Nara period; one of three UNESCO-listed washi types.","Nara period",dt="kozo"),
      X("Sekishu-banshi","",UN,"Washi of Misumi-cho, Hamada City, Shimane; one of the three types in the UNESCO inscription.","",dt=""),
      X("Hosokawa-shi","",UN,"Washi of Ogawa Town/Higashi-chichibu Village, Saitama; one of the three types in the UNESCO inscription.","",dt=""),
      X("Echizen washi","",WA,"Washi of Fukui Prefecture, named in the washi article alongside Mino.","",dt="")]},
{"n":"Seal paste and seal stone","a":"yinni · inkan · hanko · chop","d":"Cinnabar-red paste and carved stone seal used to sign East Asian paintings and calligraphy.","s":SE,
 "t":["silk-based paste","plant-based (moxa) paste","soapstone seal","hard-stone seal","hanko"],
 "x":[X("Cinnabar seal paste","",SE,"Vermilion paste of powdered cinnabar and castor oil; thick silk-based and looser plant-based types.",dt="silk or moxa base"),
      X("Japanese hanko","",SE,"Personal seals in four types: jitsuin, ginkō-in, mitome-in and gagō-in (artists' seals).",dt="jitsuin · ginkō-in · mitome-in · gagō-in")]},
{"n":"Gansai and East Asian watercolour","a":"gansai tambi · Japanese solid watercolour","d":"Solid pan watercolour from Japan with a gouache-like binder, used for sumi-e, manga and illustration.","s":KG,
 "t":["standard pans","pearl colours","gem colours","sumi colours"],
 "x":[X("Gansai Tambi","Kuretake",KG,"Traditional Japanese solid watercolours that can be used thickly like gouache; lightfast but not waterproof.",dt="pan sets · sumi, pearl and gem colour sets")]},
]
brands=[
B("Kuretake","Japan","1902","Heritage manufactory","sumi, Gansai Tambi","Nara ink maker founded by Narakichi Watatani; makes Gansai Tambi and Zig pens.",s=KG,sig=["Gansai Tambi"]),
B("Kobaien","Japan","1577","Heritage manufactory","Nara sumi","Nara maker of sumi inksticks, reported as Japan's oldest.",s=KB,sig=["Nara sumi"]),
]
trad=[
{"n":"Four Treasures of the Study","g":"Printmaking & ink painting","r":"China, spreading to Japan and Korea","p":"Song dynasty onward","d":"The brush, ink, paper and inkstone of Chinese calligraphy, each with a famed production place.","tech":"Ink ground from a soot-and-glue stick on an inkstone and applied with a brush to paper.","mat":"Animal-hair brush, soot-and-glue inkstick, bark paper, stone inkstone","forms":["Hu brush","Hui ink","Xuan paper","Duan and She inkstones"],"ctr":["Shanlian, Huzhou (brush)","Shexian, Anhui (ink, She stone)","Jingxian, Anhui (paper)","Zhaoqing, Guangdong (Duan stone)"],"auth":"Provenance by production place and, for inkstones, by quarry.","s":FT},
{"n":"Washi","g":"Paper & Japanese crafts","r":"Japan","p":"7th century onward","d":"Handmade Japanese paper of kozo, gampi or mitsumata bark, UNESCO-listed in 2014.","tech":"Fibres boiled with lye, beaten and formed on a screen with mucilage (nagashi-zuki or tame-zuki).","mat":"Kozo, gampi, mitsumata","forms":["Kozogami","Ganpishi","Mitsumatagami"],"ctr":["Mino (Gifu)","Echizen (Fukui)","Misumi-cho (Shimane)","Ogawa Town (Saitama)"],"auth":"Hand-made washi of the three UNESCO types: Sekishu-banshi, Hon-minoshi, Hosokawa-shi.","s":WA},
{"n":"Japanese calligraphy (shodō)","g":"Printmaking & ink painting","r":"Japan","p":"c. AD 600 onward","d":"Artistic writing in Japanese, from Chinese models to the wayō style and Zen ink traces.","tech":"Single-stroke brush writing in kaisho, gyōsho, sōsho and kana.","mat":"Fude, sumi, washi, suzuri","forms":["Kaisho","Gyōsho","Sōsho","Kana","Bokuseki"],"ctr":["Hōryū-ji","Shōren-in (Oie style)","Hon'ami Kōetsu"],"auth":"Style and school lineage (wayō or karayō).","s":JC},
]
write('01_01',kinds,brands,trad,"Fully new shelf. Kobaien's Nara sumi used for 'Nara inksticks'. Left out: Kuretake sumi sticks, Hu brush hair details, Duan quarries, Echizen specifics (no page), Awagami etc already on printmaking shelf. Traditions: three entries; Four Treasures group label is ours.")
