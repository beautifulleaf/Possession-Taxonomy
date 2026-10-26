import json, os
W = 'https://en.wikipedia.org/wiki/'
KIM, YUK, HAO, HAK, OBI, HAN = W+'Kimono', W+'Yukata', W+'Haori', W+'Hakama', W+'Obi_(sash)', W+'Hanbok'
QIP, RUQ, BEI, MAM, ZHS, TAN = W+'Cheongsam', W+'Ruqun', W+'Beizi', W+'Mamianqun', W+'Zhongshan_suit', W+'Tangzhuang'
TATLER = 'https://www.tatlerasia.com/style/fashion/best-cheongsams-qipaos-in-hong-kong'
CS = 'https://costumesociety.org.uk/blog/post/an-interview-with-designer-kim-young-jin'
NH = 'https://www.newhanfu.com/85304.html'
HONGDU = 'https://english.www.gov.cn/news/video/2014/09/30/content_281474990850846.htm'
RFX = 'https://english.www.gov.cn/news/video/2014/09/30/content_281474990850806.htm'

def X(n, d, s, a='', mk='', y='', v=None, dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}
def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}

kinds = [
 {"n": "Kimono", "a": "着物 · kimono robe", "d": "Japanese T-shaped wrapped robe worn left over right with an obi, graded by type from formal crested to everyday wear.",
  "t": ["awase (lined, autumn to spring)", "hitoe (unlined, early summer and autumn)", "silk", "wool", "cotton or synthetic", "number of crests (one, three or five)", "yūzen-dyed", "woven (ori) or dyed (some)"],
  "s": "https://www.kimonoya-japan.net/page/41",
  "x": [
   X("Furisode", "Long-sleeved formal kimono for young, usually unmarried women; the longest-sleeved ō-furisode is for brides, dancers and singers.", KIM, a="振袖 · ō-furisode · ko-furisode",
     v=[V("Kyō-yūzen furisode", "Chiso", "", "Kyoto yūzen house that lists furisode as a main line.")], dt="sleeve length · yūzen or woven pattern · coming-of-age or bridal use"),
   X("Kurotomesode", "Most formal black kimono for married women, short-sleeved, with pattern below the waist.", KIM, a="黒留袖 · kuro-tomesode",
     v=[V("Kurotomesode", "Chiso", "", "Listed among Chiso tomesode.")], dt="five crests · hem pattern · silk"),
   X("Irotomesode", "Formal coloured short-sleeved kimono with hem pattern; with crests also called iro-montsuki.", KIM, a="色留袖 · iro-tomesode",
     v=[V("Irotomesode", "Chiso", "", "Listed among Chiso tomesode.")], dt="ground colour · one to five crests"),
   X("Hōmongi", "Semi-formal visiting kimono whose pattern flows across the seams, developed in the Taishō period from the tomesode category.", KIM, a="訪問着 · houmongi", y="Taishō period (1912–26)",
     v=[V("Hōmongi", "Chiso", "", "Kyoto yūzen hōmongi line."), V("Hōmongi", "Ginza Motoji", "", "Formal women's range.")], dt="seam-crossing pattern · yūzen or embroidery"),
   X("Tsukesage", "Low-ranking formalwear one step below hōmongi; motifs usually do not cross the seams; suits parties rather than ceremonies.", KIM, a="付け下げ",
     v=[V("Tsukesage", "Chiso")], dt="one to three crests · placed motifs"),
   X("Iromuji", "Plain single-colour silk kimono with at most one crest, worn mainly to tea ceremonies.", KIM, a="色無地",
     v=[V("Iromuji", "Chiso")], dt="ground colour · woven self-pattern (rinzu) · crest or none"),
   X("Komon", "Informal kimono with an all-over repeating pattern, once the most common everyday womenswear.", KIM, a="小紋",
     v=[V("Edo komon", "", "", "Extremely small repeat, usually white on colour; always silk, about as formal as iromuji."), V("Komon and Edo komon", "Ginza Motoji")], dt="repeat size · silk, cotton, linen or synthetic"),
   X("Tsumugi", "Casual plain-weave silk kimono woven from silk noil or floss, often patterned with kasuri.", KIM, a="紬",
     v=[V("Ōshima tsumugi", "", "", "Mud-dyed kasuri silk from Amami Ōshima; see tradition."), V("Yūki tsumugi", "", "", "Hand-spun floss silk from Yūki; see tradition."), V("Oitama tsumugi", "", "", "Named in the source's illustrations."), V("Ginza Motoji Ōshima tsumugi", "Ginza Motoji", "", "Own-label Ōshima tsumugi for women and men.")],
     dt="region of weave · kasuri pattern · mud, indigo or plant dye"),
   X("Meisen", "Cheap ready-to-wear silk daywear with bright ikat-dyed designs, popular after the 1923 Kantō earthquake.", KIM, a="銘仙", y="1920s–1950s", dt="bold ikat pattern · vintage condition"),
   X("Uchikake", "Heavily decorated over-kimono worn unbelted, once upper-class formal dress, now bridal.", KIM, a="打掛", dt="brocade or embroidery · padded hem · bridal colours"),
   X("Shiromuku", "Pure-white bridal kimono for the Shinto wedding ceremony, often rented.", KIM, a="白無垢", dt="white woven pattern · with wataboshi or tsunokakushi"),
   X("Mofuku", "Mourning kimono of plain black silk with five crests, worn with white undergarments and tabi.", KIM, a="喪服"),
   X("Kuro-montsuki", "Black five-crested men's kimono, the most formal men's dress, worn with haori and hakama.", KIM, a="黒紋付 · montsuki",
     v=[V("Montsuki", "Ginza Motoji", "", "Men's formal crested range.")], dt="five crests · habutae silk · with sendaihira hakama"),
   X("Hikizuri", "Trailing-length kimono worn on stage, in period drama and by geisha and maiko.", KIM, a="引きずり · susohiki")]},
 {"n": "Yukata", "a": "浴衣 · summer kimono", "d": "Unlined cotton or linen summer kimono worn to festivals and at hot-spring inns.",
  "t": ["cotton", "linen", "synthetic", "indigo and white", "multicoloured modern prints", "inn (ryokan) bathrobe yukata", "men's · women's · children's"],
  "s": "https://www.ohiokimono.com/japanesekimono",
  "x": [
   X("Chūsen yukata", "Yukata cloth dyed by pouring dye through layered fabric, a late-Edo method that reproduces double-sided dyeing cheaply.", YUK, a="注染 · Tokyo Honzome Chusen", y="late Edo period; designated traditional craft 2023", dt="double-sided colour · soft gradations · cotton"),
   X("Nagaita chūgata yukata", "Traditional yukata stencil-dyed on both sides on long boards, an expensive indigo method.", YUK, a="長板中形", dt="indigo and white · stencil pattern both faces")],
  "m": [["Yukata", "SOU·SOU"], ["Yukata and hanhaba obi", "Ginza Motoji"]]},
 {"n": "Haori", "a": "羽織 · kimono jacket", "d": "Hip- or thigh-length jacket worn over a kimono, without overlapping front panels, tied with short cords.",
  "t": ["haori himo (front cords)", "decorated lining", "men's", "women's", "silk", "crested or plain"],
  "s": "https://eiyokimono.com/collections/haori",
  "x": [
   X("Kuro-montsuki haori", "Formal black haori bearing family crests, worn by men over kuro-montsuki kimono.", HAO, a="黒紋付羽織", dt="crests · black silk · white himo"),
   X("Merchant's lined haori", "Plain-faced men's haori with a lavishly decorated lining, a taste born of Edo sumptuary laws.", HAO, a="haura (lining)", y="Edo period", dt="lining picture · plain outer"),
   X("Women's haori", "Haori worn over women's kimono, adopted by Fukagawa geisha in the early 1800s and common by the 1930s.", HAO, y="early 1800s; general by 1930s", dt="length · pattern"),
   X("Hanten", "Informal, often padded jacket related to the haori.", HAO, a="半纏", dt="padding · cotton"),
   X("Happi", "Lightweight jacket of shopkeepers and festivals, related to the haori.", HAO, a="法被", dt="crest or shop name on back")],
  "m": [["Haori", "SOU·SOU"], ["Haori and coats", "Ginza Motoji"]]},
 {"n": "Hakama", "a": "袴", "d": "Pleated wide trousers or skirt tied over a kimono, worn formally, at graduations and in martial arts.",
  "t": ["seven pleats (five front, two back)", "tetron or polyester", "indigo cotton (aizome)", "silk", "black · navy · white · striped", "made to order"],
  "s": "https://japan-clothing.com/collections/hakama",
  "x": [
   X("Umanori", "Divided-leg 'horse-riding' hakama, the commoner cut and the one worn in martial arts.", HAK, a="馬乗袴",
     v=[V("Aikido and iaido hakama", "Tozando", "", "Made to order in Kyoto; in-store hakama tailor at the Nishijin store."), V("Tetron aikido and iaido/kendo hakama", "SeidoShop"), V("Memory Pleats Tetron iaido hakama", "Mitsuboshi")],
     dt="martial art (aikido, kendo, iaido, kyūdō) · fabric · colour"),
   X("Andon-bakama", "Undivided skirt-like 'lantern' hakama, as worn by women at school and graduation since Meiji.", HAK, a="行灯袴", y="Meiji–Taishō", dt="colour · with furisode at graduation"),
   X("Sendaihira", "Most formal men's hakama in stiff glossy striped silk, usually black and white.", HAK, a="仙台平", dt="stripe width · silk"),
   X("Naga-bakama", "Very long trailing court hakama, now used in Noh, kabuki and Shinto ritual.", HAK, a="長袴"),
   X("Ōguchi and ue-no-bakama", "Red closed ōguchi worn under white ue-no-bakama with sokutai court dress.", HAK, a="大口袴 · 表袴"),
   X("Sashinuki", "Heian-period hakama bloused over the leg and drawn in at the hem with a cord.", HAK, a="指貫 · nu-bakama", y="Heian period"),
   X("Karusan-bakama", "Sengoku-period hakama with tapered, banded hems, inspired by Portuguese trousers.", HAK, a="軽衫", y="Sengoku period"),
   X("Field hakama", "Umanori looser at the waist and narrow in the leg, worn by field and forest workers.", HAK, a="yama-bakama · nobakama")]},
 {"n": "Obi", "a": "帯 · kimono sash", "d": "Sash tied round a kimono or yukata, made in widths and lengths matched to formality.",
  "t": ["tied knot (musubi) style", "woven (ori) or dyed (some)", "silk · cotton · synthetic", "obiage, obijime and obi-ita accessories"],
  "s": OBI,
  "x": [
   X("Maru obi", "Most formal women's obi, patterned throughout; now worn mainly by maiko and brides.", OBI, a="丸帯", y="popular Meiji–Taishō"),
   X("Fukuro obi", "Formal women's obi about 30 cm wide and 360–450 cm long, almost indistinguishable from maru obi when tied.", OBI, a="袋帯",
     v=[V("Nishijin fukuro obi", "", "", "Kyoto brocade; Tatsumura Textile is a major Nishijin obi maker."), V("Fukuro obi", "Ginza Motoji")], dt="Nishijin or other weave · gold thread · pattern placement"),
   X("Nagoya obi", "Most common women's obi today, shorter (about 315–345 cm), developed by a Nagoya seamstress in the late 1920s.", OBI, a="名古屋帯", y="late 1920s",
     v=[V("Nagoya obi", "Ginza Motoji")], dt="woven or dyed · otaiko pattern"),
   X("Hanhaba obi", "Informal half-width obi (about 15 cm), the usual partner of yukata.", OBI, a="半幅帯"),
   X("Kaku obi", "Stiff men's obi about 10 cm wide, usually of Hakata-ori, worn from casual to formal.", OBI, a="角帯", v=[V("Hakata-ori kaku obi", "", "", "Tight weave of thick weft and fine warp from Fukuoka.")]),
   X("Heko obi", "Very soft, informal sash, traditionally for children and men.", OBI, a="兵児帯", dt="width · shibori"),
   X("Darari obi", "Maru-style obi about 6 m long worn only by maiko, bearing the crest of the geisha house.", OBI, a="だらり帯"),
   X("Tsuke obi", "Pre-tied obi that looks like a tied one when worn.", OBI, a="付け帯 · tsukuri obi")]},
 {"n": "Hanbok", "a": "한복 · chosŏn-ot", "d": "Korean traditional dress of a short jacket (jeogori) over a full high-waisted skirt (chima) or wide trousers (baji), with outer robes.",
  "t": ["jeogori (jacket)", "chima (skirt)", "baji (trousers)", "po and durumagi (outer robe)", "magoja (outer jacket)", "jokki (vest)", "sokgot (undergarments)", "silk · ramie · hemp · cotton", "custom-made · ready-to-wear"],
  "s": "https://thekoreaninme.com/",
  "x": [
   X("Jeogori and chima", "Women's ensemble of short tied jacket and full wrap skirt.", HAN, dt="jeogori length · goreum ribbon · chima colour"),
   X("Jeogori and baji", "Men's ensemble of jacket and wide trousers, worn with po or durumagi outside.", HAN),
   X("Durumagi", "Long outer coat worn over hanbok.", HAN, a="두루마기", v=[V("Kkachi durumagi", "", "", "Children's durumagi.")]),
   X("Dangui", "Royal and court women's ceremonial jacket.", HAN, a="당의"),
   X("Wonsam", "Ceremonial women's robe adapted from Ming styles.", HAN, a="원삼"),
   X("Hwarot", "Bridal robe of hanbok.", HAN, a="활옷"),
   X("Fashion hanbok", "Ready-to-wear hanbok-inspired clothing for daily wear, made from patterns and easy-care fabrics.", CS, a="modern hanbok · daily hanbok · saenghwal hanbok", y="2010s–",
     v=[V("Tchai Kim (ready-to-wear)", "Tchai Kim", "2012", "Factory-made from pre-made patterns; flat patterning with draping."), V("Tchai Kim Young Jin (couture)", "Tchai Kim", "2004", "Custom hanbok sewn by one dressmaker."), V("Daily jeogori range", "Leesle", "", "Everyday jeogori and hanbok dresses."), V("Maison Danha couture", "Danha", "", "Haute couture and upcycled custom hanbok by designer Kim Danha.")],
     dt="jeogori cut · fabric (traditional silks or modern) · daily or ceremonial")]},
 {"n": "Qipao", "a": "旗袍 · cheongsam · Chinese dress", "d": "Figure-fitting Chinese one-piece dress with mandarin collar, right-side opening and frog fastenings, developed in 1920s Shanghai.",
  "t": ["mandarin collar", "pankou frog fastenings", "side-slit height", "piping (gun)", "sleeve length", "silk brocade · cotton · lace", "bespoke · ready-to-wear"],
  "s": QIP,
  "x": [
   X("Shanghai qipao", "Dominant style using Western darts and curved cuts for a close fit, with high slits and collars and narrow piping.", QIP, a="海派旗袍", y="1920s",
     v=[V("Shanghai Tang qipao", "Shanghai Tang", "1994–", "Signature qipao inspired by 1920s cheongsam; ready-to-wear and tailoring."), V("Ruifuxiang bespoke qipao", "Ruifuxiang", "", "Beijing silk house tailoring over 100 mostly hand steps; one fitting.")],
     dt="slit height · collar height · fabric"),
   X("Beijing qipao", "Conservative, often handmade straight or A-line style with embroidery and wide piping.", QIP, a="京派旗袍", dt="embroidery · wide piping"),
   X("Hong Kong cheongsam", "Understated Cantonese style mixing Lingnan and Western taste, the 'qipao that looks least like a qipao'.", QIP, a="港派旗袍 · Cantonese cheongsam",
     v=[V("Bespoke cheongsam", "Mee Wah Qipao", "1920s–", "Hand-made by the Kan family; the oldest bespoke cheongsam shop in Hong Kong."), V("In the Mood for Love cheongsams", "Linva Tailor", "2000", "Made by master Leung Ching-wah for Maggie Cheung."), V("Bespoke cheongsam", "Shanghai Bo Sing Qipao", "", "Master Yan Ka-man.")],
     dt="hand-sewn · fitting count · fabric")]},
 {"n": "Ruqun", "a": "襦裙 · hanfu two-piece", "d": "Han Chinese two-piece dress of a short upper garment (ru) over a wrapped skirt (qun).",
  "t": ["jiaoling (crossed collar)", "duijin (parallel collar)", "tanling (U-shaped collar)", "skirt waist height", "silk · cotton · chiffon"],
  "s": "https://hanfuway.com/women-hanfu/qixiong-ruqun",
  "x": [
   X("Qixiong ruqun", "Skirt tied above the breasts under a short upper garment, from the Sui and Tang, revived by the modern Hanfu movement.", RUQ, a="齐胸襦裙", y="Sui–Tang; revived 2000s",
     v=[V("Dunhuang, Huazhao and Shanhaijing series", "Shisanyu", "", "Themed collections."), V("Tuyuexian, Tianxiangyin, Fenglaiyi and Yudie series", "Zhonglingji", "", "Poetically named collections.")], dt="skirt length · upper garment · colour"),
   X("Qiyao ruqun", "Skirt worn at the natural waist with a crossed-collar upper garment.", RUQ, a="齐腰襦裙"),
   X("Gaoyao ruqun", "High-rise skirt worn above the natural waist, late Sui and early Tang.", RUQ, a="高腰襦裙", y="late 6th–7th century"),
   X("Aoqun", "Thick ao jacket over a skirt, the main Han women's dress under the Qing and a national dress of the Republic.", RUQ, a="袄裙 · wenming xinzhuang", y="Qing; 1910s–1920s",
     v=[V("Wenming xinzhuang", "", "1910s–1920s", "Republican 'civilised new dress' aoqun.")]),
   X("Shanqun", "Unlined shan upper garment over a skirt, of the Wei, Jin and Northern and Southern dynasties.", RUQ, a="衫裙"),
   X("Qungua", "Gua jacket and qun skirt worn as a wedding dress.", RUQ, a="裙褂", y="Qing–present", dt="gold and silver embroidery"),
   X("Xiuhefu", "Modern bridal attire inspired by the aoqun and Qing wedding dress.", RUQ, a="秀禾服")],
  "r": [["Dunhuang series", "Shisanyu"], ["Huazhao series", "Shisanyu"], ["Shanhaijing series", "Shisanyu"], ["Fenglaiyi series", "Zhonglingji"], ["Tianxiangyin series", "Zhonglingji"], ["Tuyuexian series", "Zhonglingji"], ["Yudie series", "Zhonglingji"]],
  "m": [["Historically researched hanfu ensembles", "Minghuatang"], ["Han-element daily wear", "Chixia"]]},
 {"n": "Beizi", "a": "褙子 · 背子 · chuozi · pifeng", "d": "Loose Chinese outer robe with long sleeves, open or lightly fastened at the front, worn over other layers.",
  "t": ["long (chang beizi)", "short (duan beizi)", "narrow sleeves (casual)", "wide sleeves (formal)", "silk · gauze"],
  "s": "https://www.fashionhanfu.com/product-category/women-hanfu/womens-hanfu/beizi-hanfu",
  "x": [
   X("Song beizi", "Straight open-fronted robe with edge bands to the hem, worn by all classes in the Song dynasty.", BEI, y="Song dynasty (960–1279)"),
   X("Ming pifeng", "Ming form, long enough to cover the skirt, with tubular sleeves, short neckband and a clasp fastening.", BEI, a="披风", y="Ming, esp. 16th century", dt="zimu kou clasp · sleeve width"),
   X("Half-sleeve beizi", "Short-sleeved beizi, originally military, later worn by scholars and commoners.", BEI, a="半袖背子"),
   X("Sleeveless beizi", "Vest-like casual beizi sold in markets.", BEI),
   X("Hechang", "Crane cloak, a casual form worn by recluses and retired officials.", BEI, a="鹤氅")]},
 {"n": "Mamianqun", "a": "马面裙 · horse-face skirt · mamianzhequn", "d": "Han Chinese wrap skirt of two pleated panels on one waistband, with flat front and back aprons (mamian).",
  "t": ["knife pleats", "box pleats", "fish-scale pleats (yulinqun)", "gored", "woven gold lan bands", "Qing variants: yuehuaqun, fengweiqun, langanqun"],
  "s": MAM,
  "x": [
   X("Ming mamianqun", "Deeply pleated two-fabric skirt of the Ming, the form named in the History of the Ming Palace and copied by today's makers.", MAM, y="Ming (1368–1644)",
     v=[V("Song and Liao prototypes", "", "960–1279", "Unpleated wrap skirts from the Huang Sheng tomb, Fujian."), V("Qing mamianqun", "", "1644–1912", "More structured and luxurious; variants yuehuaqun, fengweiqun, yulinqun, langanqun."), V("Fall 2022 pleated skirt", "Dior", "2022", "Accused of copying the mamianqun; protests outside the Paris flagship on 23 July 2022; withdrawn from mainland China online stores.")],
     dt="pleat type · panel decoration · waistband fastening")]},
 {"n": "Zhongshan suit", "a": "中山装 · Sun Yat-sen suit · Mao suit · Chinese tunic suit", "d": "Men's buttoned tunic and trousers with turn-down collar and four patch pockets, promoted by Sun Yat-sen as national dress.",
  "t": ["five buttons", "four pockets", "wool · cotton drill", "grey · blue · olive · black"],
  "s": ZHS,
  "x": [
   X("Zhongshan suit", "Five-button, four-pocket tunic suit, regulation dress for Nationalist officials from 1929; pockets and buttons carry political symbolism.", ZHS, a="Sun Yat-sen suit", y="1912; regulation 1929",
     v=[V("Yokohama coat", "", "1905", "Coat made for Sun by a Yokohama tailor after a Japanese uniform."), V("Seven-button version", "", "1914", "Photographed on Sun Yat-sen."), V("Mao suit", "", "PRC era", "Same cut worn as a symbol of proletarian unity."), V("Bespoke Zhongshan suit", "Hongdu", "1956–", "Beijing tailor for state leaders; 100-suit centenary edition 2011.")],
     dt="button count · pocket flaps · cloth")]},
 {"n": "Tang jacket", "a": "唐装 · tangzhuang · Tang suit", "d": "Chinese jacket with straight mandarin collar and frog or knot fastenings, descended from the Manchu magua.",
  "t": ["brocade", "embroidered characters (fu, shou)", "red · blue", "knotwork buttons"],
  "s": TAN,
  "x": [
   X("Magua", "Waist- or three-quarter-length front-opening Manchu riding jacket, mandatory for Han officials under the Qing.", TAN, a="马褂", y="Qing dynasty"),
   X("APEC tangzhuang", "Fitted 'solid-cut' brocade jacket by Shanghai clothiers worn by leaders at the 2001 APEC summit, starting a tangzhuang craze.", TAN, y="2001", dt="brocade colour · knot buttons")],
  "m": [["Ready-to-wear Tang suit", "Ruifuxiang"]]},
]

brands = [
 {"n": "Chiso", "c": "Japan", "f": "1555", "seg": "kimono house", "d": "Kyoto kimono maker known for Kyō-yūzen dyeing, with a gallery of about 20,000 historic fabrics.", "lines": ["Kimono (furisode, hōmongi, tomesode, tsukesage, iromuji, komon)", "KIMONO GOWN", "Scarves, bags, jewellery"], "eras": [], "sig": ["Furisode", "Hōmongi", "Kurotomesode"], "sc": [], "rel": [], "s": "https://en.wikipedia.org/wiki/Chiso"},
 {"n": "Ginza Motoji", "c": "Japan", "f": "", "seg": "kimono specialty store", "d": "Ginza, Tokyo kimono retailer with women's and men's kimono, own-label Ōshima tsumugi and Platinum Boy silk.", "lines": ["Ginza Motoji Ōshima tsumugi", "Platinum Boy", "Men's kimono"], "eras": [], "sig": ["Tsumugi", "Kuro-montsuki"], "sc": [], "rel": [], "s": "https://www.motoji.co.jp/"},
 {"n": "SOU·SOU", "c": "Japan", "f": "", "seg": "Kyoto textile and clothing label", "d": "Kyoto brand selling jika-tabi, kimono, yukata and haori in its own textiles.", "lines": ["Jika-tabi", "Kimono and yukata", "Haori"], "eras": [], "sig": [], "sc": [], "rel": [], "s": "https://www.sousou.co.jp/"},
 {"n": "Tozando", "c": "Japan", "f": "", "seg": "martial arts outfitter", "d": "Kyoto martial arts supplier with an in-store hakama tailor and bogu workshop at its Nishijin store.", "lines": ["Aikido hakama", "Iaido hakama", "Kendo bogu"], "eras": [], "sig": ["Umanori"], "sc": [], "rel": [], "s": "https://tozando.com/en/store-en/"},
 {"n": "Leesle", "c": "South Korea", "f": "", "seg": "modern hanbok", "d": "Korean label making everyday hanbok-inspired jeogori, dresses and menswear.", "lines": ["Daily jeogori", "Hanbok dresses", "Wedding"], "eras": ["Hwang Lee-seul, CEO"], "sig": ["Fashion hanbok"], "sc": [], "rel": ["Tchai Kim", "Danha"], "s": "https://www.leesle.com/"},
 {"n": "Tchai Kim", "c": "South Korea", "f": "2004", "seg": "couture and ready-to-wear hanbok", "d": "Designer Kim Young Jin's labels: couture hanbok Tchai Kim Young Jin (2004) and ready-to-wear Tchai Kim (2012).", "lines": ["Tchai Kim Young Jin (couture)", "Tchai Kim (ready-to-wear)"], "eras": ["Kim Young Jin, 2004–"], "sig": ["Fashion hanbok"], "sc": [], "rel": ["Leesle", "Danha"], "s": CS},
 {"n": "Danha", "c": "South Korea", "f": "", "seg": "sustainable couture hanbok", "d": "Seoul label of designer Kim Danha making haute couture and upcycled custom hanbok.", "lines": ["Maison Danha couture", "Upcycling custom made", "Danha Beauty"], "eras": ["Kim Danha"], "sig": ["Fashion hanbok"], "sc": [], "rel": ["Tchai Kim", "Leesle"], "s": "https://en.danhaseoul.com/maison"},
 {"n": "Shanghai Tang", "c": "Hong Kong", "f": "1994", "seg": "luxury fashion house", "d": "Hong Kong house founded by David Tang whose signature is the modern qipao; owned by Richemont 1998–2017.", "lines": ["Qipao", "Homeware and bone china"], "eras": ["David Tang, 1994–98", "Richemont, 1998–2017", "Lunar Capital, 2018–", "UTAN Group, 2020–"], "sig": ["Shanghai qipao"], "sc": [], "rel": [], "s": "https://en.wikipedia.org/wiki/Shanghai_Tang"},
 {"n": "Linva Tailor", "c": "Hong Kong", "f": "1965", "seg": "bespoke cheongsam tailor", "d": "Central, Hong Kong tailor run by master Leung Ching-wah, maker of Maggie Cheung's In the Mood for Love qipaos.", "lines": ["Bespoke cheongsam"], "eras": ["Leung Ching-wah, 1965–"], "sig": ["Hong Kong cheongsam"], "sc": [], "rel": ["Mee Wah Qipao"], "s": TATLER},
 {"n": "Mee Wah Qipao", "c": "Hong Kong", "f": "1920s", "seg": "bespoke cheongsam tailor", "d": "Sheung Wan shop founded by the Kan family, called the oldest bespoke cheongsam shop in Hong Kong.", "lines": ["Hand-made bespoke cheongsam"], "eras": ["Kan family, two generations"], "sig": ["Hong Kong cheongsam"], "sc": [], "rel": ["Linva Tailor"], "s": TATLER},
 {"n": "Shanghai Bo Sing Qipao", "c": "Hong Kong", "f": "", "seg": "bespoke cheongsam tailor", "d": "Jordan, Hong Kong qipao tailor of master Yan Ka-man, who also teaches young tailors.", "lines": ["Bespoke qipao"], "eras": ["Yan Ka-man"], "sig": ["Hong Kong cheongsam"], "sc": [], "rel": ["Linva Tailor", "Mee Wah Qipao"], "s": TATLER},
 {"n": "Ruifuxiang", "c": "China", "f": "1862", "seg": "silk house and tailor", "d": "Meng family silk house from Jinan with a Beijing store, supplier of the first PRC flag silk and bespoke qipao tailoring.", "lines": ["Silk and satin", "Bespoke qipao", "Ready-to-wear qipao and Tang suits"], "eras": ["Meng Hongsheng, founder", "Meng Luochuan, 1920s–30s peak"], "sig": ["Shanghai qipao"], "sc": [], "rel": ["Hongdu"], "s": "https://en.wikipedia.org/wiki/Rui_Fu_Xiang"},
 {"n": "Hongdu", "c": "China", "f": "", "seg": "bespoke tailor", "d": "Beijing time-honoured tailor, moved from Shanghai in 1956, regarded as the leading Zhongshan suit maker.", "lines": ["Bespoke Zhongshan suits"], "eras": ["Shanghai origin; Beijing from 1956"], "sig": ["Zhongshan suit"], "sc": [], "rel": ["Ruifuxiang"], "s": HONGDU},
 {"n": "Minghuatang", "c": "China", "f": "2007", "seg": "premium historical hanfu", "d": "Guangzhou hanfu house known for researched, hand-made historical garments and wedding sets.", "lines": ["Historical hanfu", "Hanfu wedding dress"], "eras": [], "sig": [], "sc": ["Hanfu movement"], "rel": ["Shisanyu", "Zhonglingji"], "s": NH},
 {"n": "Shisanyu", "c": "China", "f": "", "seg": "new-style hanfu", "d": "Hangzhou Dazai Culture hanfu label with themed youth collections.", "lines": ["Dunhuang series", "Huazhao series", "Shanhaijing series"], "eras": [], "sig": ["Qixiong ruqun"], "sc": ["Hanfu movement"], "rel": ["Zhonglingji", "Minghuatang"], "s": NH},
 {"n": "Zhonglingji", "c": "China", "f": "2016", "seg": "new-style hanfu", "d": "Chengdu hanfu brand with poetically named collections.", "lines": ["Tuyuexian", "Tianxiangyin", "Fenglaiyi", "Yudie"], "eras": [], "sig": ["Qixiong ruqun"], "sc": ["Hanfu movement"], "rel": ["Shisanyu"], "s": NH},
 {"n": "Chixia", "c": "China", "f": "", "seg": "Han-element daily wear", "d": "Hefei brand making hanfu-inspired garments for modern daily life.", "lines": ["Han-element fusion clothing"], "eras": [], "sig": [], "sc": ["Hanfu movement"], "rel": ["Shisanyu"], "s": NH},
]

traditions = [
 {"n": "Nishijin-ori", "g": "Textiles & rugs", "r": "Nishijin, Kamigyō-ku, Kyoto, Japan", "p": "794–present", "d": "Kyoto silk weaving for the court and aristocracy, today chiefly luxury obi and kimono cloth.", "tech": "Brocade, damask, tsumugi, kasuri and velvet weaving; Jacquard looms adopted in the Meiji era", "mat": "Raw and scoured silk, gold thread and gilded paper", "forms": ["Fukuro obi", "Maru obi", "Kimono"], "ctr": ["Nishijin, Kyoto", "Tatsumura Textile"], "auth": "Woven-in three-dimensional patterning and metallic threads; top obi can reach about 1 million yen.", "s": "https://en.wikipedia.org/wiki/Nishijin-ori"},
 {"n": "Kyō-yūzen", "g": "Textiles & rugs", "r": "Kyoto Prefecture, Japan", "p": "Edo period–present; designated traditional craft 1976", "d": "Kyoto paste-resist dyeing of pictorial designs on kimono silk, credited to fan painter Miyazaki Yūzensai.", "tech": "Hand-painting within itome-nori rice-paste outlines; stencil (kata) yūzen from the Meiji era; gold leaf and embroidery finishing", "mat": "Silk, rice-paste resist, gojiru soybean base, dyes, gold and platinum leaf", "forms": ["Furisode", "Hōmongi", "Kurotomesode", "Komon"], "ctr": ["Kyoto", "Chiso", "Moriguchi Kakō", "SAIRIN Co."], "auth": "Fine white or coloured outlines left by the paste, brushwork gradations and metallic finishing; hand-painted (itome) work versus stencil imitation.", "s": "https://kogeijapan.com/locale/en_US/kyoyuzen/"},
 {"n": "Kaga-yūzen", "g": "Textiles & rugs", "r": "Kanazawa, Ishikawa Prefecture, Japan", "p": "Edo period–present", "d": "Kanazawa yūzen dyeing with lifelike natural scenes in gentle gradients, more naturalistic than Kyō-yūzen.", "tech": "Paste-resist yūzen dyeing with realistic motifs such as insect-nibbled leaves", "mat": "Silk and dyes", "forms": ["Hōmongi", "Furisode"], "ctr": ["Kanazawa", "Asanogawa River (yūzen nagashi)"], "auth": "Realistic flora with worm-eaten leaf details and soft shading rather than Kyoto's framed, gilded pictures.", "s": "https://www.japan.travel/en/japans-local-treasures/kaga-yuzen-traditional-art-kimono/"},
 {"n": "Ōshima tsumugi", "g": "Textiles & rugs", "r": "Amami Ōshima and Kagoshima Prefecture, Japan", "p": "Late Edo period specialty (older roots)–present", "d": "Hand-woven kasuri silk dyed black with tannin bark and iron-rich mud.", "tech": "Techigi bark and mud dyeing; shimebata tie-weaving to resist-bind kasuri threads; plain weave by hand", "mat": "Silk, Techigi bark, iron-rich mud, igisu seaweed paste", "forms": ["Tsumugi"], "ctr": ["Amami Ōshima", "Kagoshima", "Miyakonojō"], "auth": "'Honba Amami-Oshima Tsumugi' certificate at the foot of the bolt; Amami union globe seal or Kagoshima union two-flag seal.", "s": "https://en.wikipedia.org/wiki/Ōshima_tsumugi"},
 {"n": "Yūki tsumugi", "g": "Textiles & rugs", "r": "Yūki (Ibaraki) and Oyama (Tochigi), Japan", "p": "Muromachi period or earlier–present; name from 1602", "d": "Soft plain-weave silk of hand-spun floss on a backstrap loom, on UNESCO's intangible heritage list since 2010.", "tech": "Hand-spinning silk floss; tying thousands of kasuri resists; weaving on the jibata backstrap loom", "mat": "Silk floss from cocoons, plant and synthetic dyes", "forms": ["Tsumugi"], "ctr": ["Yūki", "Oyama", "Association for the Preservation of Honba Yūki-tsumugi"], "auth": "Hand-spun yarn slubs and kasuri precision; Important Intangible Cultural Property production (1956).", "s": "https://en.wikipedia.org/wiki/Yūki-tsumugi"},
 {"n": "Hong Kong and Shanghai qipao tailoring", "g": "Textiles & rugs", "r": "Shanghai, Beijing and Hong Kong", "p": "1920s–present", "d": "Bespoke cheongsam making that fused Chinese robes with Western darts and fitting, now kept by a few master tailors.", "tech": "Hand-sewing, curved cuts and darts, hand-knotted pankou fastenings and piping", "mat": "Silk brocade, satin, cotton, lace", "forms": ["Qipao"], "ctr": ["Linva Tailor", "Mee Wah Qipao", "Shanghai Bo Sing Qipao", "Ruifuxiang"], "auth": "Hand-finished seams and frog fastenings, multiple fittings, several days to weeks of work.", "s": TATLER},
]

notes = ("Old 'Sash' (k112) became Obi (Japanese kimono sash; old s replaced by the Obi Wikipedia page). Hakama SKU flood (26 Tozando/SeidoShop/Mitsuboshi SKUs) cut to "
         "four maker-level versions under the Umanori archetype; old type names became archetypes. Kimono 'Hitoe' became a t type (unlined). Old Ruqun models Qixiong/Qiyao became archetypes; "
         "old Beizi chang/duan became t types. New kinds Qipao, Mamianqun, Zhongshan suit, Tang jacket sourced from Wikipedia. Left out (no page retrieved or facts unconfirmed): Y. & Sons, "
         "Kyoto Kimono Yuzen, Hanbok Lynn (no retrievable page); Longqingxiang (no source); Tatsumura Textile has no register entry (named only in Nishijin-ori tradition). "
         "Ruifuxiang founding: Wikipedia gives 1862 (Jinan), gov.cn gives 1893 (Meng Luochuan) for the Beijing house; register uses 1862. Dior referenced by register name 'Dior' (entry assumed from another shelf).")
out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = 'work/A1/shelves/07_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('kinds', len(kinds), 'archetypes', sum(len(k.get('x', [])) for k in kinds), 'brands', len(brands), 'traditions', len(traditions))
