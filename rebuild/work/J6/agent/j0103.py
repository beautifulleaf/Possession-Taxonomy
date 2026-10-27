import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
ch=[
 A("West Lake Longjing","Xihu Longjing · Dragon Well","Pan-roasted green tea from around Longjing Village near West Lake, Hangzhou; name protected as an EU/UK PDO since 1998.","","Qing dynasty tribute tea",W+'Longjing_tea',[V("Shi Feng (Lion Peak) Longjing","","","Sharp, long-lasting fragrance, yellowish-green leaf"),V("Qiantang Longjing","","","Grown just outside the Xihu district; cheaper"),V("Pre-Qingming (Ming Qian)","","","Premium early-spring harvest"),V("Bai Longjing","","","Look-alike from Anji, not true Longjing")],"grades: Superior, 1-5 · peaks: Lion, Dragon, Cloud, Tiger, Plum Flower"),
 A("Biluochun","Bi Luo Chun · Pi Lo Chun · Green Snail Spring","Jiangsu green tea from the Dongting Mountains near Lake Tai, rolled into tight spirals; seven grades from Supreme to Chao Qing II.","","Ming era roots",W+'Biluochun',[V("Dong Shan / Xi Shan Dongting","","","Considered the best versions"),V("Kangxi naming","","","Qing chronicle says he named it Green Snail Spring")],"grades: Supreme, Supreme I, I, II, III, Chao Qing I, II"),
 A("Huangshan Maofeng","Yellow Mountain Fur Peak","Anhui needle-like green tea with white hairs, picked before Qingming from bud and one leaf.","","",W+'Huangshan_Maofeng',[],"province Anhui · pick: bud + 1 leaf"),
 A("Lu'an Guapian","Lu'an Melon Seed · Liu An Gua Pian","Lu'an, Anhui tea of flat melon-seed leaves, made from the second leaf with the vein removed and pan-fired.","","Qing tribute tea",W+"Lu'an_Melon_Seed_tea",[],"leaf: second leaf · no bud"),
 A("Taiping Houkui","Monkey Tea · Tai Ping Hou Kui","Anhui tea with leaves up to about 15 cm from the Shi Da Cha cultivar; best from Houkeng, Hougang and Yanjiachun.","","Ming era; commercial early 20th century",W+'Taiping_houkui',[V("King of Tea award","","2004","Won at the China Tea Exhibition")],"cultivar Shi Da Cha · counterfeits common"),
 A("Xinyang Maojian","Xinyang Mao Jian · Yu Maofeng","Henan green tea with white downy hairs, graded by harvest timing from Mingqian to autumn.","","1913 named; 1958 top ten",W+'Xinyang_Maojian_tea',[V("Mingqian","","","Before Qingming, highest level"),V("Yuqian","","","Before Guyu"),V("Spring tail tea"),V("Summer tea"),V("Autumn (Bailu) tea")],"gold medal Panama-Pacific 1914/15"),
 A("Anji Bai Cha","Anji white tea","Zhejiang green tea from a cultivar identified in 1982 whose leaves turn jade-white in cold weather; rare and costly.","","1982",W+'Anji_bai_cha',[],"cultivar Anji Baicha · also Changxing"),
 A("Duyun Maojian","Fishhook tea","Guizhou green tea with the 'three yellows'; its processing was added to UNESCO's intangible heritage list in 2022.","","2022 UNESCO",W+'Duyun_Maojian',[],"province Guizhou"),
]
ko=[
 A("Boseong green tea","Boseong nokcha · Banya-cha","Korea's largest tea area, about 40% of national output, centre of green tea.","","",W+'Korean_tea',[V("Ujeon","","","Pre-rain first flush, plucked before gogu"),V("Sejak","","","Thin sparrow grade"),V("Jungjak","","","Medium sparrow grade"),V("Daejak","","","Big sparrow grade")],"grades: ujeon, sejak, jungjak, daejak"),
 A("Jeju green tea (O'Sulloc)","Jeju nokcha","Jeju volcanic-soil tea, led by O'Sulloc, founded 1979 by Suh Sung-hwan and now owned by Amorepacific.","O'Sulloc","1979","https://en.wikipedia.org/wiki/O'Sulloc_Tea",[V("Seogwang field","O'Sulloc","","Largest tea field in South Korea")],"island Jeju"),
 A("Hadong green tea","Hadong nokcha","Southern Gyeongsang tea county named with Boseong and Jeju as famous Korean tea areas.","","",W+'Korean_tea',[],"region South Gyeongsang"),
]
ye=[
 A("Junshan Yinzhen","Silver Needle of Jun Mountain","Hunan yellow tea from Junshan Island, one of China's Ten Famous Teas and called its rarest.","","",W+'Junshan_Yinzhen',[],"island Junshan, Dongting Lake"),
 A("Huoshan Huangya","Huo Mountain Yellow Sprout","Anhui yellow tea, once an imperial tribute tea since the Ming dynasty, picked early April from single buds.","","Ming dynasty",W+'Huoshan_Huangya_tea',[],"pick: bud + leaf"),
 A("Meng Ding Huangya","Mengding yellow bud","Yellow tea from Mt Meng, Ya'an, Sichuan.","","",W+'Yellow_tea',[],"province Sichuan"),
 A("Korean hwangcha","hwangcha","Korean 'yellow tea', partly oxidised, made like oolong or lightly oxidised black tea by maker.","","",W+'Korean_tea',[],"partly oxidised"),
]
sm="https://www.smithtea.com/products/dragonwell"; tt="https://www.taotealeaf.com/"
kinds=[
 {"n":"Chinese green tea","a":"pan-fired green tea · Ten Famous Teas","d":"Unoxidised tea fixed by heating in a pan or drum, sold by named appellation.","s":sm,"x":ch},
 {"n":"Korean green tea","a":"nokcha · hwangcha","d":"Korean tea named by harvest time (ujeon to daejak), from Boseong, Hadong and Jeju.","s":W+'Korean_tea',"x":ko},
 {"n":"Yellow tea","a":"huangcha","d":"Green-processed tea given a slow sealed yellowing step before drying.","s":tt,"x":ye},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[B("O'Sulloc","South Korea","1979","Premium","Jeju tea","Jeju tea company founded by Suh Sung-hwan; subsidiary of Amorepacific since 2020.","https://en.wikipedia.org/wiki/O'Sulloc_Tea")]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Left out unsourced: Lushan Yunwu, Enshi Yulu (no retrieved page). Old Pan-fired green tea models kept as archetypes (Longjing, Bi Luo Chun, Maofeng, Gua Pian, Houkui, Maojian, Anji). Tradition entry for Duyun Maojian processing not added (no detail page)."}
json.dump(out,open('01_03.src.json','w'),ensure_ascii=False)
