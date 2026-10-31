import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
P=W+'Pu%27er_tea'; C=W+'Compressed_tea'; F=W+'Fermented_tea'
raw=[
 A("Menghai factory recipes","Dayi · Menghai Tea Factory","Four-digit recipe numbers from the Menghai factory; 7542 is a 1975 grade-4 recipe (factory digit 2).","Menghai Tea Factory","1975 (7542)",P,[V("7542","Menghai Tea Factory","1975","Grade-4 recipe, factory digit 2")],"recipe digits: year, grade, factory · form: bing 357 g"),
 A("Xiaguan tea factory","Xiaguan tuocha","State-owned Yunnan factory dating from the 1940s, known for tuocha.","Xiaguan Tea Factory","1940s",P,[],"form: tuocha 100 g"),
 A("Six Great Tea Mountains","Xishuangbanna mountains","Best-known pu'er source area in Mengla, Xishuangbanna; the list has changed over time.","","1962 government list",P,[],"mountains · village · tree age"),
 A("Jingmai old tea forests","Jingmai","Lancang mountain where Bulang and Dai peoples have made pu'er since at least the 10th century; UNESCO World Heritage in 2023.","","2023 UNESCO",P,[],"old tree forests"),
 A("Haiwan","Haiwan Tea Factory","Private pu'er factory founded in 1999.","Haiwan Tea Factory","1999",P,[],"factory"),
 A("Pu'er cake (bing)","bingcha · 357 g cake","Disc-shaped compressed pu'er, most commonly 357 g.","","",C,[V("Tuocha","","","100 g dome-shaped nugget"),V("Zhuancha brick","","","Brick form"),V("Jinguan / Longzhu / Jingcha","","","Other forms named on the pu'er page")],"form: bing, tuocha, brick, loose"),
]
ripe=[
 A("Wet-piled ripe pu'er","shou · wòduī","Accelerated fermentation of 45-60 days developed in 1973 by the Kunming and Menghai factories to imitate aged raw tea; mass production from 1975.","Kunming and Menghai tea factories","1973 / 1975",P,[V("Mass production start","","1975","First ripe pu'er in volume")],"wet piling 45-60 days"),
]
dark=[
 A("Liu Bao","Liubao · Guangxi dark tea","Guangxi post-fermented dark tea, often sold loose and aged.","","",F,[V("Aged Liu Bao","","","Old-vintage dark tea sold as aged leaf")],"aged in baskets"),
 A("Fu brick tea","fu zhuan cha · Fu Cha","Hunan and Shaanxi brick dark tea, aged with golden-flower fungi.","","16th century Anhua fermentation mastery",F,[V("Anhua Hunan dark tea","","","Tea-makers of Anhua mastered fermentation in the early 16th century")],"form: brick · jin hua fungus"),
 A("Liu'an basket tea","Liu an lan cha","Anhui post-fermented dark tea aged in bamboo baskets.","","",F,[],"form: basket"),
 A("Tibetan brick tea","Zang cha · Ya'an brick","Sichuan brick tea from Ya'an traded to Tibet, five qualities; the third grade was 'eighth' (brgyad pa), worth eight tangkas in Lhasa.","","late 19th-early 20th century currency",C,[],"form: brick · Ya'an, Sichuan"),
]
kinds=[
 {"n":"Raw pu-erh (sheng)","a":"sheng · green pu-erh · raw pu'er","d":"Traditional pu'er aged for years or decades, sold as cakes, tuocha, bricks or loose; ripe pu'er has its own kind.","t":["bing cake 357 g","tuocha","brick","loose"],"s":P,"m":[["Banzhang",""]],"x":raw},
 {"n":"Ripe pu-erh (shou)","a":"shou · cooked pu-erh · shu","d":"Pu'er fermented by wet piling to imitate age.","t":["bing cake","tuocha","brick","loose"],"s":P,"x":ripe},
 {"n":"Dark tea (hei cha)","a":"Liu Bao · Liu'an · post-fermented tea","d":"Post-fermented tea other than pu-erh (Liu Bao, Fu brick, Liu'an, Tibetan brick).","s":"https://www.meimeitea.com/collections/aged-teas/products/2007-vintage-lao-liu-bao-dark-tea-hei-cha-shu","m":[["Chaling Hunan Hei Cha",""]],"x":dark},
]
trad=[{"n":"Pu'er tea craft","g":"Food & drink","r":"Yunnan, China","p":"10th century onward","d":"Yunnan large-leaf tea compressed and aged, in raw (sheng) and wet-piled ripe (shou) styles.","tech":"sun-drying, compression, natural ageing or wet piling (since 1973)","mat":"Camellia sinensis var. assamica","forms":["bing cake 357 g","tuocha","brick"],"ctr":["Menghai","Xiaguan","Kunming","Jingmai"],"auth":"Four-digit factory recipe numbers; 2008 standard limits the name to Yunnan tea","s":P}]
out={"kinds":kinds,"brands":[],"traditions":trad,"notes":"Left out unsourced: Lao Banzhang, Yiwu, Bingdao, Nannuo, Bulang, Xigui archetypes (only snippet-level), 8582/7572/7262 recipes, Lancang Gu Cha, Changtai, Zhongcha Red/Green/Yellow Mark, Yunnan Sourcing/White2Tea/Bitterleaf vendors, mushroom/jincha detail, Qianliang. Old Other pu-erh type dissolved."}
json.dump(out,open('01_05.src.json','w'),ensure_ascii=False)
