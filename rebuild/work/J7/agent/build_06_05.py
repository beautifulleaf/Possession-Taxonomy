import json, os
W='https://en.wikipedia.org/wiki/'
BJ=W+'Baijiu'; SH=W+'Shōchū'; AW=W+'Awamori'; SO=W+'Soju'
def X(n,a,d,mk,y,s,v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Baijiu","a":"Chinese white spirit · shaojiu · 白酒","d":"Chinese spirit distilled from fermented grain, usually sorghum, made with a qu starter and graded by aroma type.",
 "t":["Sauce aroma (jiangxiang)","Strong aroma (nongxiang)","Light aroma (qingxiang)","Rice aroma (mixiang)","Fuyu / mixed aroma (jianxiang)","Sesame aroma (zhima)","Feng aroma (Xifeng)","Daqu (wheat qu)","Xiaoqu (rice qu)"],
 "s":"https://www.masterofmalt.com/baijiu/",
 "x":[
  X("Kweichow Moutai","Maotai · Moutai · 茅台","The reference sauce-aroma (jiangxiang) baijiu from Maotai town, Renhuai, Guizhou; gold medal at the 1915 Panama-Pacific Exposition.","Kweichow Moutai","1951",W+"Kweichow_Moutai",
    [("Flying Fairy Brand Kweichow Moutai Chiew","Kweichow Moutai","","flagship bottling"),("Kweichow Moutai Dufu","Kweichow Moutai","",""),("Kweichow Moutai Libai","Kweichow Moutai","","")],"bottling · age statement · vintage year · bottle size"),
  X("Wuliangye","五粮液 · Five Grain Liquor","Strong-aroma (nongxiang) baijiu from Yibin, Sichuan, distilled from sorghum, rice, glutinous rice, wheat and corn.","Wuliangye","1909",W+"Wuliangye",
    [("Wuliangye (eighth generation)","Wuliangye","","signature flagship"),("501 Wuliangye","Wuliangye","","ultra-premium"),("Classic Wuliangye","Wuliangye","",""),("Wuliangye 1618","Wuliangye","",""),("Wuliangchun","Wuliangye","","baijiu series"),("Wuliang Tequ","Wuliangye","","baijiu series"),("Jianzhuang","Wuliangye","","baijiu series")],"grade · ABV · bottle size"),
  X("Luzhou Laojiao","泸州老窖 · luxiang","Originator of the strong-aroma style, made in Luzhou, Sichuan, in fermentation cellars in use since 1573.","Luzhou Laojiao","1573",W+"Luzhou_Laojiao",
    [("National Cellar 1573 (Guojiao 1573) Jingdian Zhuang","Luzhou Laojiao","","38% or 52%; aged at least five years"),("National Cellar 1573 Zhongguo Pinwei","Luzhou Laojiao","","52%; aged at least ten years"),("Luzhou Laojiao Tequ","Luzhou Laojiao","",""),("Luzhou Laojiao Erqu","Luzhou Laojiao","",""),("Dah Chu Chiew","Luzhou Laojiao","",""),("Luzhou Laojiao 1952","Luzhou Laojiao","","")],"grade · ABV · age · bottle size"),
  X("Fenjiu","Fen Chiew · 汾酒 · Xinghuacun Fenjiu","The reference light-aroma (qingxiang) baijiu from Xinghua village, Fenyang, Shanxi; one of the Four Famous Spirits of 1952.","Xinghuacun Fenjiu","1949","https://en.wikipedia.org/wiki/Xinghuacun_Fenjiu",
    [("Fen Chiew 10 Year Old","Xinghuacun Fenjiu","","age-stated bottling")],"age statement · ABV · bottle size"),
  X("Erguotou","二锅头 · head of the second pot","Light-aroma baijiu of Beijing, named for the second pot of cooling water on the still; Red Star and Niulanshan are the best-known makers.","","1680s",W+"Erguotou",
    [("Red Star Erguotou","Beijing Hongxing","",""),("Niulanshan Erguotou","Niulanshan","","")],"maker · ABV · bottle size"),
  X("Kinmen Kaoliang","Kaoliang liquor · kaoliang wine · 金门高粱酒","Sorghum (kaoliang) baijiu from the government-owned Kinmen distillery in Kinmen County, Taiwan.","Kinmen Kaoliang Liquor","1952",W+"Kinmen_Kaoliang_Liquor",[],"ABV · age · bottle size"),
  X("Jiugui","酒鬼酒 · Jiu Gui Jiu","Fuyu-aroma (mixed-aroma) baijiu from Jishou, Hunan; brand created in 1985 by the former Jishou Distillery.","Jiugui Liquor","1985","https://zh.wikipedia.org/wiki/酒鬼酒",
    [("Neican","Jiugui Liquor","","high-end series"),("Jiugui","Jiugui Liquor","","mid-range"),("Xiangquan","Jiugui Liquor","1977","entry brand")],"series · ABV · bottle size"),
 ],
 "m":[["National Cellar 1573","National Cellar 1573"],["Shui Jing Fang Red Fortune","Shui Jing Fang"],["Shui Jing Fang Wellbay Phoenix","Shui Jing Fang"],["Yanghe M6 Plus","Yanghe"],["Yanghe M9","Yanghe"],["Kweichow Maotaizhen 5 Year Old Baijiu","Kweichow Maotaizhen"],["Kweichow Maotaizhen 9 Year Old Baijiu","Kweichow Maotaizhen"],["Binhe 12 YO Baijiu","Gansu Binhe Nine-Grain Liquor Co."],["Guizhou Century Shi Zhanggui Winery Shizhanggui Zhenkunsha Baijiu","Guizhou Century Shi Zhanggui Winery"],["Shi Rongxiao Liquor Secret Recipe 6 Baijiu","Guizhou Rongtaihe Shaofang Shirongxiao Winery Co."]]},
{"n":"Shochu","a":"Shōchū · 焼酎 · honkaku shochu","d":"Japanese spirit distilled from sweet potato, barley, rice, brown sugar, buckwheat or other starch, usually with koji.",
 "t":["Imo (sweet potato)","Mugi (barley)","Kome (rice)","Kokuto (brown sugar)","Soba (buckwheat)","Honkaku (single pot distillation, ≤45%)","Kōrui (multiple column distillation, <36%)","Black / white / yellow koji","Aged or cask-aged"],
 "s":"https://www.masterofmalt.com/Shochu/",
 "x":[
  X("Satsuma shochu","Satsuma imo shochu · Kagoshima shochu","Sweet-potato shochu from Kagoshima under the Satsuma geographical indication.","","",SH,[("Kuroma Sweet Potato Shochu","Iwagawa Distillery","",""),("Kuro Isanishiki","Okuchi Distillery","","")],"potato variety · koji colour · ABV"),
  X("Kuro Kirishima","黒霧島 · Kuro Kiri","Black-koji imo shochu from Kogane Sengan sweet potatoes, flagship of Japan's largest shochu maker in Miyakonojo, Miyazaki.","Kirishima Shuzo","1998","https://en.www.kirishima.co.jp/brand/kuro-kirishima/",
    [("Kuro Kirishima","Kirishima Shuzo","1998","original black-koji bottling"),("Kuro Kirishima EX","Kirishima Shuzo","2018",""),("Kuro Kirishima MELT","Kirishima Shuzo","2017",""),("Shibitakojo Kuro Kirishima Genshu","Kirishima Shuzo","2022","undiluted"),("Kin Kirishima","Kirishima Shuzo","2007",""),("Kokuho Kirishima","Kirishima Shuzo","2009",""),("Shiro Kirishima","Kirishima Shuzo","","white koji"),("Aka Kirishima","Kirishima Shuzo","","purple Murasaki Masari potato")],"koji colour · ABV · pack size"),
  X("Iki shochu","Iki mugi shochu","Barley shochu from Iki island, Nagasaki, under the Iki geographical indication.","","",SH,[],"ABV · ageing"),
  X("iichiko","Iichiko","Honkaku barley shochu distilled once from 100% barley, launched in 1979 by Sanwa Shurui of Usa, Oita.","Sanwa Shurui","1979","https://www.jetro.go.jp/en/discovershochu/distillery/sanwa_shurui.html",
    [("iichiko Silhouette","Sanwa Shurui","","core bottling"),("iichiko Special","Sanwa Shurui","",""),("iichiko Saiten","Sanwa Shurui","","")],"ABV · bottle size"),
  X("Kuma shochu","Kuma rice shochu · Kumamoto kome shochu","Rice shochu from the Hitoyoshi basin, Kumamoto, under the Kuma geographical indication.","","",SH,[],"ABV · ageing"),
  X("Amami kokuto shochu","Kokuto shochu · brown-sugar shochu","Brown-sugar shochu made with rice koji, permitted only in the Amami Islands of Kagoshima since 1953.","","1953",SH,[],"island · ABV · ageing"),
 ],
 "m":[["Chuko Awamori Distillery 18 YO Pot Aged Koshu Shochu","Chuko Awamori Distillery"],["Hikimi Kuro-moji Shochu Usho Morinoka","Hikimi"],["Misora Shochu","Kitaya Co."],["St. George California Shochu","St. George Spirits"]]},
{"n":"Awamori","a":"泡盛 · Ryukyu Awamori","d":"Okinawan spirit distilled from long-grain rice with indigenous black koji in a single fermentation.",
 "t":["Ippanshu (unaged)","Kusu (aged 3+ years)","Hanazake (60%)","Clay-pot aged","Thai rice / Okinawan rice"],
 "s":"https://www.lcbo.com/en/shimauta-awamori-okinawa-shochu-51996",
 "x":[
  X("Kusu","Kūsu · 古酒 · aged awamori","Awamori aged at least three years, traditionally in clay pots kept cool underground.","","",AW,
    [("Chuko Awamori Distillery 15 YO Awamori Koshu","Chuko Awamori Distillery","","15-year kusu"),("Awamori 7 Year","Seishin Distillery","","7-year kusu")],"age · vessel (clay pot, tank, cask) · ABV"),
  X("Hanazake","Yonaguni hanazake","60% awamori made only by the Donan, Yonaguni and Maifuna distilleries on Yonaguni island.","","",AW,[],"distillery · age"),
 ],
 "m":[["Shimauta Awamori",""]]},
{"n":"Soju","a":"소주 · Korean soju","d":"Korean spirit, either diluted ethanol-based soju or traditional soju distilled from rice or other grain.",
 "t":["Diluted (green-bottle) soju","Distilled (traditional) soju","Flavoured / fruit soju","Sparkling soju","Low-alcohol (under 17%)"],
 "s":"https://www.danmurphys.com.au/shop/buy-soju-online",
 "x":[
  X("Andong soju","안동소주","Traditional distilled soju from Andong, North Gyeongsang, kept by two Korean food grandmasters (Park Jae-seo, Jo Ok-hwa).","","",W+"Andong_soju",[],"maker · ABV"),
  X("Chamisul","참이슬 · Jinro Chamisul","Filtered diluted soju from HiteJinro, launched in 1998; the best-selling soju brand.","HiteJinro","1998",W+"Jinro",
    [("Chamisul Soju","HiteJinro","1998",""),("Chamisul Fresh","HiteJinro","","17.2%"),("Chamisul Classic","HiteJinro","",""),("Green Grape Soju","HiteJinro","","flavoured"),("Plum Soju","HiteJinro","","flavoured"),("Chamisul Grapefruit","HiteJinro","","flavoured")],"strength · flavour · bottle size"),
  X("Chum Churum","처음처럼","Diluted soju brand from Lotte Chilsung, the main challenger to Chamisul.","Lotte Chilsung","",SO,
    [("Chum Churum Apple Soju","Lotte Chilsung","","flavoured"),("Chum Churum Peach Soju","Lotte Chilsung","","flavoured"),("Chum Churum Blueberry Soonhari","Lotte Chilsung","","flavoured")],"strength · flavour"),
  X("Good Day","좋은데이","Diluted soju from Muhak of Changwon, popular in South Gyeongsang and Ulsan.","Muhak","",SO,[],"strength · flavour"),
 ],
 "m":[["Strawberry Soju","HiteJinro"],["Hoju Soju","Hoju"],["Hwasimjujo Miraon Still Young Single Rice Soju","Hwasimjujo"]]},
]
def B(n,c,f,seg,d,lines,sig,s,rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Kweichow Moutai","China","1951","Baijiu distillery","State-owned maker of sauce-aroma Maotai baijiu in Maotai, Renhuai, Guizhou.",["Moutai"],["Kweichow Moutai"],W+"Kweichow_Moutai"),
 B("Wuliangye","China","1952","Baijiu distillery","Yibin, Sichuan maker of five-grain strong-aroma baijiu.",["Wuliangye","501 Wuliangye","Wuliangchun","Jianzhuang"],["Wuliangye"],W+"Wuliangye"),
 B("Luzhou Laojiao","China","1950","Baijiu distillery","Luzhou, Sichuan distillery whose cellars date from 1573; originator of strong aroma.",["National Cellar 1573","Tequ","Erqu"],["Luzhou Laojiao"],W+"Luzhou_Laojiao"),
 B("Xinghuacun Fenjiu","China","1949","Baijiu distillery","State-owned light-aroma baijiu distillery in Xinghua village, Fenyang, Shanxi.",["Fenjiu","Zhuyeqing"],["Fenjiu"],"https://en.wikipedia.org/wiki/Xinghuacun_Fenjiu"),
 B("Jiugui Liquor","China","1956","Baijiu distillery","Jishou, Hunan maker of fuyu-aroma baijiu; part of COFCO since 2016.",["Neican","Jiugui","Xiangquan"],["Jiugui"],"https://zh.wikipedia.org/wiki/酒鬼酒"),
 B("Beijing Hongxing","China","","Baijiu distillery","Beijing Red Star, formed by merging twelve Beijing distilleries; best-known erguotou maker.",["Red Star Erguotou"],["Erguotou"],W+"Erguotou",["Niulanshan"]),
 B("Kinmen Kaoliang Liquor","Taiwan","1952","Baijiu distillery","Government-owned sorghum-liquor distillery in Kinmen County.",["Kinmen Kaoliang"],["Kinmen Kaoliang"],W+"Kinmen_Kaoliang_Liquor"),
 B("Kirishima Shuzo","Japan","1916","Shochu distillery","Miyakonojo, Miyazaki maker of imo shochu; largest shochu producer by sales.",["Kuro Kirishima","Shiro Kirishima","Aka Kirishima"],["Kuro Kirishima"],"https://www.jetro.go.jp/en/discovershochu/distillery/kirishima_shuzo.html",["Sanwa Shurui"]),
 B("Sanwa Shurui","Japan","1958","Shochu distillery","Usa, Oita maker of iichiko barley shochu.",["iichiko"],["iichiko"],"https://www.jetro.go.jp/en/discovershochu/distillery/sanwa_shurui.html",["Kirishima Shuzo"]),
 B("HiteJinro","South Korea","1924","Soju and beer maker","Seoul drinks company, largest soju maker; controlled by Hite Holdings since 2006.",["Chamisul","Jinro"],["Chamisul"],W+"Jinro",["Lotte Chilsung"]),
 B("Lotte Chilsung","South Korea","","Drinks company","Lotte group drinks maker, producer of Chum Churum soju.",["Chum Churum"],["Chum Churum"],SO,["HiteJinro"]),
 B("Muhak","South Korea","","Soju maker","Changwon soju producer of Good Day.",["Good Day"],["Good Day"],SO),
]
out={"kinds":kinds,"brands":brands,"traditions":[{"n":"Awamori distilling","g":"Food & drink","r":"Okinawa (Ryukyu), Japan","p":"15th century–present","d":"Okinawan rice spirit distilled with indigenous black koji and aged as kusu in clay pots; UNESCO-listed in 2024 among Japan's traditional koji knowledge.","tech":"Single fermentation of steamed long-grain rice fully converted with black koji, single pot distillation, long ageing in clay pots","mat":"Thai indica or Okinawan rice, black koji (Aspergillus luchuensis), clay pots","forms":["Awamori","Kusu","Hanazake"],"ctr":["Shuri","Shikina Distillery","Taragawa (Miyako-jima)","Yonaguni"],"auth":"'Ryukyu Awamori' GI label (since 2004); age claim for kusu means at least the stated years","s":AW},
 {"n":"Andong soju","g":"Food & drink","r":"Andong, North Gyeongsang, South Korea","p":"13th century–present","d":"Traditional distilled rice soju of Andong, tied to the Yuan-era supply base and recorded in the 17th-century Ŭmsik timibang.","tech":"Brewing a grain mash and distilling it in a soju gori still","mat":"Rice and nuruk","forms":["Andong soju"],"ctr":["Park Jae-seo (food grandmaster No. 6)","Jo Ok-hwa (food grandmaster No. 20)"],"auth":"","s":W+"Andong_soju"}],
"notes":"All four planned kinds kept. Baijiu: aroma types as t (ladder from the Baijiu article); 7 archetypes (Moutai, Wuliangye, Luzhou Laojiao, Fenjiu, Erguotou, Kinmen Kaoliang, Jiugui). Old Moutai, Fen Chiew and 1573 models moved into versions where the maker matched; old 'National Cellar 1573' row kept in m as given (its maker field names the brand, not Luzhou Laojiao). Yanghe, Shui Jing Fang, Maotaizhen and small makers stay in m (no archetype source retrieved). Shochu: base and honkaku/kōrui as t; GI archetypes (Satsuma, Iki, Kuma) plus Amami kokuto, Kuro Kirishima and iichiko; duplicate Iichiko Saiten removed. Awamori: Kusu and Hanazake archetypes; old aged bottlings became kusu versions. Soju: Andong soju, Chamisul, Chum Churum, Good Day; old 'Jinro' maker renamed HiteJinro, 'Lotte Liquor' to Lotte Chilsung (as on the Soju article). Left out for lack of a retrieved page: Gujing Gongjiu, Xifeng, Jiannanchun, Hwayo, Ryukyu 1429 archetypes; founding years for Lotte Chilsung, Muhak, Beijing Hongxing. Jishou Distillery founding (1956) is the Jiugui brand founding year."}
p='work/J7/shelves/06_05.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
