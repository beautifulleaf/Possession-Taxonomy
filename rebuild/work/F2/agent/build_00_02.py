import json, os
W='https://en.wikipedia.org/wiki/'
IW=W+'Ink_wash_painting'; LP=W+'Lacquer_painting'; MH=W+'Minhwa'; RP=W+'Rinpa_school'; CT=W+'Cypress_Trees'
KA='https://aisf.or.jp/%7Ejaanus/deta/k/kanouha.htm'; NH='https://www.nippon.com/en/people/e00170/nihonga-rediscovering-the-classic-japanese-painting-style.html'
BP=W+'Byeongpung'; FS=W+'Folding_screen'; MFA='https://www.mfa.org/node/23331'; BR='https://www.britannica.com/art/wenrenhua'
def v(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Ink wash painting","a":"guohua · shan shui · sumi-e · suibokuga · sumukhwa","d":"Black or coloured ink brushed in graded washes on paper or silk, in the East Asian manner.",
  "t":["hanging scroll (kakejiku)","handscroll","album leaf","fan","on paper","on silk","monochrome ink","ink and colour"],
  "s":"https://www.artsy.net/categories","m":[["sumi-sai (墨彩画)",""]],
  "x":[
   {"n":"Shan shui landscape","a":"mountain-and-water painting","d":"An ink landscape of mountains, rivers and waterfalls, usually imagined rather than drawn from one place.","mk":"","y":"Tang dynasty onward (618–907)","s":IW,
    "v":[v("Monumental landscape","Fan Kuan","c. 960–1030"),v("Landscape","Guo Xi","c. 1020–1090"),v("Yuan literati landscape","Huang Gongwang","1269–1354"),v("Spare river landscape","Ni Zan","1301–1374"),v("Ming orthodox landscape","Dong Qichang","1555–1636"),v("Individualist landscape","Shitao","1642–1707")],
    "dt":"format (hanging scroll, handscroll, album leaf) · paper or silk · seals, colophons and inscriptions"},
   {"n":"Late Qing and modern Chinese ink painting","a":"guohua","d":"Bold brush-and-ink flowers, creatures and figures by late Qing and 20th-century masters, a large modern market.","mk":"","y":"19th–20th century","s":IW,
    "v":[v("Flower painting","Wu Changshuo","1844–1927"),v("Shrimps, birds and flowers","Qi Baishi","1864–1957")],
    "dt":"subject · seals and inscription · mounting · provenance (very frequently forged)"},
   {"n":"Japanese suibokuga","a":"sumi-e · Zen ink painting","d":"Japanese monochrome ink painting brought by Zen monks in the 14th century from Song and Yuan models.","mk":"","y":"14th century onward","s":IW,
    "v":[v("Ink landscapes after Xia Gui","Sesshū",""),v("Pine Trees (screen)","Hasegawa Tōhaku","16th century"),v("Chan models","Muqi","c. 1210–1269")],
    "dt":"hanging scroll or screen · inscription · temple or daimyō provenance"},
   {"n":"Korean sumukhwa","a":"","d":"Korean ink painting, often mixing colour with monochrome ink.","mk":"","y":"Joseon period","s":IW,
    "v":[v("Dream Journey to the Peach Blossom Land","An Kyŏn","1447")],"dt":"scroll or album · ink or ink and colour"}]},
 {"n":"Nihonga","a":"mineral-pigment painting","d":"Painting in ground mineral pigments fixed with animal glue, on paper or silk, in the Japanese tradition.",
  "t":["on silk","on washi paper","hanging scroll","framed panel","screen"],
  "s":"https://www.motokawa.com/technique-painting/",
  "x":[
   {"n":"Modern Nihonga","a":"","d":"Meiji-era and later Japanese painting in mineral pigments, sumi ink and gofun shell white, bound with nikawa glue.","mk":"","y":"1868 onward","s":NH,
    "v":[v("Morotai (hazy) style","Yokoyama Taikan",""),v("Morotai style","Hishida Shunsō",""),v("Enbu (Dancing in the Flames)","Hayami Gyoshū","1925"),v("Bijin-ga","Uemura Shōen",""),v("Toshi kuru (End of the Year)","Higashiyama Kaii","1968","blue-toned landscapes"),v("Oirase: Aki","Okuda Gensō","1983")],
    "dt":"silk or washi · framed, scroll or screen · artist seal and box (tomobako)"}]},
 {"n":"Painted folding screen","a":"byōbu · byeongpung · folding screen painting","d":"A painting on several hinged panels of paper or silk, made to stand free and divide or decorate a room.",
  "t":["two-panel","four-panel","six-panel","eight-panel and more","pair of screens","gold ground","ink on paper"],
  "s":FS,
  "x":[
   {"n":"Kanō gold-ground screen","a":"Kanō school byōbu","d":"A bold colour-and-gold screen of trees, tigers, dragons or birds, made by the shogunal Kanō painting workshop.","mk":"Kanō Eitoku","y":"late 16th century","s":CT,
    "v":[v("Cypress Trees","Kanō Eitoku","c. 1590","attributed; National Treasure, Tokyo National Museum"),v("Tiger and dragon pair","Kanō Sanraku","17th century","each about 1.78 × 3.56 m")],
    "dt":"panels and pairing · gold leaf · school attribution vs. named master"},
   {"n":"Rinpa screen","a":"Sōtatsu–Kōrin school screen","d":"A decorative screen of plants, flowers or gods set boldly against gold or silver ground, in the Kyoto Rinpa style.","mk":"Tawaraya Sōtatsu","y":"17th century","s":RP,
    "v":[v("Wind and Thunder Gods","Tawaraya Sōtatsu","","Kennin-ji, Kyoto"),v("Irises","Ogata Kōrin","early 18th century","Nezu Museum"),v("Red and White Plum Blossoms","Ogata Kōrin","c. 1714–15","MOA Museum of Art"),v("Summer and Autumn Grasses","Sakai Hōitsu","","Edo revival")],
    "dt":"gold or silver ground · pair or single · original, school work or later copy"},
   {"n":"Korean byeongpung","a":"","d":"A Korean folding screen of 2 to 12 panels bearing painting or calligraphy, used in homes, palaces and rites.","mk":"","y":"Goryeo period onward","s":BP,
    "v":[v("Irworobongdo screen","","Joseon","sun, moon and five peaks, behind the throne"),v("Chaekgeori screen","","Joseon","scholar's bookshelves"),v("Geumgangsan screen","","","8-panel mountain landscape")],
    "dt":"panel count (six or eight common) · subject · paper and mount"},
   {"n":"Coromandel lacquer screen","a":"kuancai screen","d":"A dark lacquer screen, incised, painted and inlaid, with a detailed scene in front and flowers behind.","mk":"","y":"late Ming dynasty onward","s":FS,
    "v":[],"dt":"panel count · inlay (mother-of-pearl, ivory) · export history"}]},
 {"n":"Lacquer painting","a":"sơn mài","d":"An image built in layers of natural or synthetic lacquer on a rigid panel, sanded and polished, often with inlaid shell or metal leaf.",
  "t":["on board","eggshell inlay","silver leaf","gold leaf"],
  "s":"https://www.singulart.com/en/painting",
  "x":[
   {"n":"Vietnamese sơn mài panel","a":"","d":"A fine-art lacquer painting on black board, built up and polished layer by layer with eggshell and silver leaf.","mk":"","y":"1930s onward","s":LP,
    "v":[v("Indochina school teaching","Joseph Inguimberty","1930s","French teacher at the École Supérieure des Beaux-Arts de l'Indochine"),v("Lacquer paintings","Nguyễn Gia Trí","1930s"),v("Contemporary lacquer","Cong Quoc Ha","")],
    "dt":"panel size · eggshell, shell and metal leaf · single panel or screen"},
   {"n":"Russian lacquer miniature","a":"Fedoskino miniature","d":"A small painting on papier-mâché under many varnish layers, from Russian folk-craft centres.","mk":"","y":"late 18th century onward","s":LP,
    "v":[v("Fedoskino","","late 18th century","papier-mâché")],"dt":"box or plaque · centre · signature"}]},
 {"n":"Korean folk painting","a":"minhwa · sokhwa","d":"Decorative Korean paintings by mostly anonymous, untrained painters, made for homes and carrying lucky or protective meaning.",
  "t":["hanging scroll","folding screen","on hanji paper","on canvas"],
  "s":MH,
  "x":[
   {"n":"Kkachi horangi","a":"tiger and magpie · hojakdo","d":"A foolish-looking tiger with a magpie in a pine, satirising the Joseon elite.","mk":"","y":"Joseon period","s":MH,"v":[],"dt":"single scroll or screen panel · natural pigments"},
   {"n":"Chaekgeori","a":"chaekgado · books and scholar's things","d":"A still life of books and scholar's objects on shelves, which spread from court to commoners in the 19th century.","mk":"","y":"18th–19th century","s":MH,"v":[],"dt":"screen (usually) · bookcase or stacked-book composition"},
   {"n":"Munjado","a":"flower writing","d":"Large Chinese characters for Confucian virtues with stories painted into the strokes.","mk":"","y":"18th–19th century","s":MH,"v":[],"dt":"eight-character set, often as a screen"},
   {"n":"Hwajodo","a":"flowers and birds","d":"Paired birds among flowers, symbols of happy marriage and advancement.","mk":"","y":"Joseon period","s":MH,"v":[],"dt":"screen or scroll · bird and plant"}]}]
def B(n,c,kf,d,s,sig): return {"n":n,"c":c,"f":"","seg":"Artisan & independent","kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 B("Kanō Eitoku","Japan","gold screens","Kanō-school master (1543–1590) who created the bold colour-and-gold style for Nobunaga and Hideyoshi.",KA,["Kanō gold-ground screen"]),
 B("Kanō Sanraku","Japan","screens","Kanō-school painter of a 17th-century tiger-and-dragon screen pair.",FS,["Kanō gold-ground screen"]),
 B("Tawaraya Sōtatsu","Japan","Rinpa","Kyoto painter (d. c. 1643) whose atelier made fans and folding screens; co-founder of Rinpa.",RP,["Rinpa screen"]),
 B("Ogata Kōrin","Japan","Rinpa","Rinpa painter (1658–1716) of Irises and Red and White Plum Blossoms.",RP,["Rinpa screen"]),
 B("Sakai Hōitsu","Japan","Rinpa","Edo painter (1761–1828) who revived the Rinpa style.",RP,["Rinpa screen"]),
 B("Hasegawa Tōhaku","Japan","ink screens","Japanese ink painter (1539–1610) of the Pine Trees screens.",IW,["Japanese suibokuga"]),
 B("Yokoyama Taikan","Japan","Nihonga","Leading modern Nihonga painter.",NH,["Modern Nihonga"]),
 B("Higashiyama Kaii","Japan","Nihonga","Nihonga painter of blue-toned landscapes and murals.",NH,["Modern Nihonga"]),
 B("Hayami Gyoshū","Japan","Nihonga","Nihonga painter (1894–1935) of Enbu.",NH,["Modern Nihonga"]),
 B("Qi Baishi","China","ink painting","Chinese ink painter (1864–1957).",IW,["Late Qing and modern Chinese ink painting"]),
 B("Wu Changshuo","China","ink painting","Chinese painter and calligrapher (1844–1927).",IW,["Late Qing and modern Chinese ink painting"]),
]
def T(n,r,p,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":"Painting","r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
trads=[
 T("Chinese literati painting","China","Northern Song (960–1127) onward; leading style from the Yuan","Wenrenhua: the scholar-painter's ink painting, valuing personal expression over likeness.","brush and ink, minimal colour, with poetry and calligraphy","ink, paper, silk",["Ink wash painting","Shan shui landscape"],["Su Dongpo (Su Shi)","Dong Qichang"],"Forgery is common: Zhang Daqian (1899–1983) made fakes bought by nearly every major US art museum; check seals, colophons, paper and provenance.",BR),
 T("Kanō school","Japan","late Muromachi to early Meiji","Hereditary workshop of professional painters serving the shogunates, from Kanō Masanobu (1434–1530).","ink painting and colour-and-gold on paper","ink, mineral colours, gold leaf",["Painted folding screen","Kanō gold-ground screen"],["Kanō Masanobu","Kanō Motonobu","Kanō Eitoku","Kanō Tan'yū"],"Many screens are school works; a named master needs strong provenance.",KA),
 T("Rinpa","Japan","17th century onward, Kyoto then Edo","Decorative painting style of plants and gods on gold or silver ground, founded by Kōetsu and Sōtatsu.","bold flat design, gold and silver ground","mineral colours, ink, gold and silver leaf on paper",["Rinpa screen","Painted folding screen"],["Hon'ami Kōetsu","Tawaraya Sōtatsu","Ogata Kōrin","Ogata Kenzan","Sakai Hōitsu"],"Not a hereditary school; later copies and followers' works are common.",RP),
 T("Minhwa","Korea","Joseon (17th century form); revived 1980s","Korean folk painting by mostly anonymous itinerant painters, with lucky and protective meanings.","natural pigments on hanji","hanji paper, natural pigments",["Korean folk painting","Kkachi horangi","Chaekgeori","Munjado"],[],"Modern revival works and decorative reproductions are common.",MH),
 T("Sơn mài","Vietnam","1930s onward","Vietnamese fine-art lacquer painting developed at the École Supérieure des Beaux-Arts de l'Indochine in Hanoi.","layered lacquer, sanded and polished; eggshell for white; silver leaf","sơn tree lacquer, eggshell, seashell, silver leaf, board",["Lacquer painting","Vietnamese sơn mài panel"],["Joseph Inguimberty","Nguyễn Gia Trí"],"A work can take months of layering; check layer depth and signature.",LP),
]
out={"kinds":kinds,"brands":brands,"traditions":trads,
 "notes":"All three old kinds kept; two new kinds added (Painted folding screen, Korean folk painting). Mounting formats moved to t. FORGERY RISK: Chinese and Japanese ink and Nihonga works are among the most forged in the market (Zhang Daqian's fakes reached nearly every major US museum, MFA Boston page); tradition 'auth' fields say so. No Getty ULAN pages retrieved, so artist entries cite fetched Wikipedia/JAANUS/nippon.com pages; founding year blank. Korean byeongpung type names (irworobongdo, chaekgeori) taken from the Folding screen page. Some work dates not given on fetched pages, left blank. Fedoskino lacquer miniature kept here as a lacquer painting archetype; may cross-link to Miniatures."}
p='work/F2/shelves/00_02.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
