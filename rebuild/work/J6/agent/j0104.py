import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
wu=W+'Wuyi_tea'; rs="https://www.rishi-tea.com/collections/loose-leaf-teas?page=1"; tt="https://www.taotealeaf.com/"
wuyi=[
 A("Da Hong Pao","Big Red Robe","Wuyi rock tea with orchid fragrance and a long sweet aftertaste; only six mother trees remain at Jiulongyu and most market tea is bred from cuttings.","","Qing dynasty; mother trees banned from collection 2006",W+'Da_Hong_Pao',[V("Mother-tree sample","","2005","20 g sold for 208,000 yuan"),V("Nixon gift","","1972","Mao gave Nixon 200 g")],"harvest May-June · brewed in Yixing pot"),
 A("Rou Gui","Cinnamon Scent","Wuyi rock tea named for its cinnamon scent.","","",wu,[],"Wuyi Mountains"),
 A("Shui Xian","Water fairy","Wuyi rock tea cultivar.","","",wu,[],"Wuyi Mountains"),
 A("Tie Luo Han","Iron Arhat","Wuyi rock tea cultivar.","","",wu,[],"Wuyi Mountains"),
 A("Bai Jiguan","White Cockscomb","Wuyi rock tea cultivar.","","",wu,[],"Wuyi Mountains"),
]
anxi=[
 A("Tieguanyin","Iron Goddess of Mercy","Anxi, Fujian oolong from the 19th century, now usually lightly oxidised and floral; the older style was heavily roasted.","","19th century",W+'Tieguanyin',[V("Anxi light style","","","Close to green tea, golden-yellow liquor"),V("Traditional roast","","","Heavier roast, stronger body"),V("Muzha Tieguanyin","","","Taiwanese roasted style with reddish-brown liquor")],"harvest: spring (Jade), autumn · brew 90-95 C"),
 A("Huangjin Gui","Golden Osmanthus","Premium Anxi oolong similar to Tieguanyin, popularised by merchant Lin Jintai in the 1900s.","","1900s",W+'Huangjin_Gui',[V("Wang legend","","1860","Bride Wang Dan's seedling"),V("Wei legend","","1850","Farmer Wei Zhen's golden plant")],"fruity · Anxi"),
]
phx=[A("Phoenix Dancong","Fenghuang Dancong · single-bush oolong","Premium oolong from Phoenix Mountain, Chaozhou, picked and processed bush by bush; over 3,000 ancient trees, many 200-400 years old.","","900+ year history",W+'Phoenix_Mountain_(Chaozhou)',[V("Honey-Orchid Fragrance","","","Famous aroma type"),V("Duck-Shit Fragrance","","","Famous aroma type")],"single-bush picking · aroma-type naming")]
tw=[
 A("Dongfang Meiren (Oriental Beauty)","Bai Hao · white-tip oolong","Heavily oxidised, unroasted Hsinchu oolong from leaves bitten by tea jassids; harvested mid-summer.","","late 19th century",W+'Dongfang_meiren',[V("John Dodd export","","","Shipped west from Tamsui")],"oxidation about 70% · Beipu, Emei"),
 A("Dong Ding","Tung-ting · Frozen Summit","Tightly rolled oolong named for a mountain in Nantou County, from Qingxin plants brought from the Wuyi Mountains.","","",W+'Dong_Ding_tea',[],"cultivar Qingxin"),
 A("Alishan","Ali Shan high-mountain","Chiayi County oolong grown at 1,000-1,400 m, sweet and less astringent.","","",W+'Oolong',[V("Lishan","","","Above 1,600 m; resembles Alishan")],"altitude 1,000-1,400 m"),
 A("Baozhong","Pouchong","Least oxidised Taiwanese oolong, with unrolled leaves.","","",W+'Oolong',[],"unrolled leaf"),
 A("Muzha Tieguanyin","Muzha","Taiwanese roasted Tieguanyin with nutty roast and reddish-brown liquor.","","",W+'Tieguanyin',[],"roast: traditional"),
]
wt=[
 A("Silver Needle (Baihao Yinzhen)","Bai Hao Yinzhen","Fujian white tea of unopened buds only, the highest and costliest grade; cultivated from vegetable tea in Fuding in 1796.","","1796; export 1891",W+'Baihao_Yinzhen',[V("Fuding","","","Production area"),V("Zhenghe","","","Production area"),V("Lüxueya","","","Former name, 'green snow shoots'")],"harvest: late March-early April"),
 A("Bai Mudan (White Peony)","Pai Mu Tan","One bud and two young leaves from Da Bai cultivars, fuller and more floral than Silver Needle.","","",W+'Baimudan_tea',[V("Fuding Da Bai","","","Eastern Fujian style"),V("Zhenghe Da Bai","","","Northern Fujian style"),V("Gushan Baiyun","","","Drum Mountain White Cloud, first grown by monks")],"1 bud + 2 leaves"),
 A("Gong Mei","","Similar to White Peony but with three to four leaves.","","",W+'White_Tea',[],"3-4 leaves"),
 A("Shou Mei","Longevity Eyebrow","Lowest white-tea grade, many leaves and few buds.","","",W+'White_Tea',[],"leaf heavy"),
]
kinds=[
 {"n":"Wuyi rock oolong","a":"yancha · Bohea","d":"Partly oxidised rock tea from the Wuyi Mountains, Fujian, sold by cultivar.","s":rs,"x":wuyi},
 {"n":"Tieguanyin & Anxi oolong","a":"Anxi oolong","d":"Oolongs from Anxi County, southern Fujian, led by Tieguanyin.","s":W+'Tieguanyin',"x":anxi},
 {"n":"Phoenix Dancong oolong","a":"Fenghuang Dancong","d":"Single-bush oolongs from Phoenix Mountain, Chaozhou, named by aroma type.","s":W+'Phoenix_Mountain_(Chaozhou)',"x":phx},
 {"n":"Taiwanese oolong","a":"Formosa oolong","d":"Oolongs from Taiwan, from rolled high-mountain teas to Oriental Beauty and Baozhong.","s":W+'Oolong',"x":tw},
 {"n":"White tea","a":"","d":"Camellia sinensis buds or young leaves withered and dried with little processing.","s":tt,"x":wt},
]
trad=[{"n":"Wuyi rock tea (yancha)","g":"Food & drink","r":"Wuyi Mountains, Fujian, China","p":"16th century onward","d":"Partly oxidised cliff-grown tea from the Wuyi Mountains, made by withering, shaking, rolling, firing and baking.","tech":"withering, making (shaking and rolling), stir-frying, kneading, baking","mat":"Wuyi cultivars (Da Hong Pao, Rou Gui, Shui Xian, Tie Luo Han, Bai Jiguan)","forms":["Da Hong Pao","Rou Gui","Shui Xian"],"ctr":["Jiulongyu mother trees"],"auth":"Mother-tree Da Hong Pao is rare; most market tea is from cuttings","s":wu}]
out={"kinds":kinds,"brands":[],"traditions":trad,"notes":"Old Oolong models moved: Bai Hao to Taiwanese, Tieguanyin to Anxi. Left out unsourced: Mi Lan Xiang/Ya Shi Xiang pinyin names, Huang Zhi Xiang, zhengyan vs banyan, UNESCO 2022 craft claim, GABA oolong, aged white cakes, Darjeeling/Ceylon silver tips, Lishan separately, Fuding White Tea as separate item (merged into Silver Needle/Bai Mudan)."}
json.dump(out,open('01_04.src.json','w'),ensure_ascii=False)
