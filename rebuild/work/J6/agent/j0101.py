import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
dj=W+'Darjeeling_tea'
darj=[
 A("Darjeeling first flush","spring flush","March-May plucking after winter dormancy; light, floral, mildly astringent.","","",dj,[V("Castleton"),V("Jungpana"),V("Thurbo"),V("Margaret's Hope"),V("Glenburn"),V("Giddapahar","","","Noted for its first flush on its Wikipedia page")],"flush: March-May · grade: FTGFOP etc. · estate"),
 A("Darjeeling second flush","summer flush · muscatel","May-June harvest whose leaves, bitten by leafhoppers, give the prized muscatel aroma.","","",dj,[V("Rishihat","","","Noted for its second flush on its Wikipedia page")],"flush: May-June"),
 A("Darjeeling autumnal flush","autumn flush","October-November harvest with softer muscatel, fuller body and darker colour.","","",dj,[],"flush: Oct-Nov"),
 A("Makaibari","Makaibari Tea Estate","Darjeeling estate that built the region's first processing factory and was India's first organic-certified estate in 1988.","","1988 organic",W+'Darjeeling_tea',[V("Biodynamic certification","","1993","First biodynamic certification in the region")],"estate · organic, biodynamic"),
]
dar2=A("Darjeeling GI","Tea Board licence","Registered in 2004 as India's first GI product, with EU protected status from 2011 and a ban on blending since 2000.","Tea Board of India","2004",dj,[],"GI 2004 · EU PGI 2011")
darj.append(dar2)
asm=[
 A("Assam second-flush tippy tea","Assam tippy","Malty, brisk, bright black tea from Assam var. assamica, with a prized second flush.","","1838-39 first London auction",W+'Assam_tea',[V("First shipment to London","","1838","Auctioned in January 1839"),V("Robert Bruce encounter","","1823","Discovered the plant on a trade expedition")],"region: Brahmaputra Valley · flush: first (March), second (tippy)"),
 A("Nilgiri tea","frost tea","Black tea of the Nilgiris district, brisk and fragrant, a registered GI since 2008; January-March frost tea is prized.","","2008 GI",W+'Nilgiri_tea',[V("Frost tea","","","First leaves after winter, plucked January-March"),V("Thiashola estate","","1859","One of the first estates"),V("Coonoor auction","","1963","Tea auction established")],"types: orthodox, CTC · use: blending"),
 A("Kangra tea","","Himachal Pradesh tea, about 90% black, GI since 2005; pale liquor from the Chinese hybrid, no CTC.","","2005 GI",W+'Kangra_tea',[V("Kangra earthquake decline","","1905","Output fell after the earthquake")],"black 90%, green"),
]
cey=[
 A("Ceylon orthodox black tea","Ceylon tea · Lion logo","Sri Lanka's mainly orthodox black teas, with the Lion logo permitted only on pure Ceylon tea packed in Sri Lanka to Tea Board standards.","Sri Lanka Tea Board","1867 planting (James Taylor)",W+'Tea_production_in_Sri_Lanka',[V("Nuwara Eliya","","","Highest-grown district, town at about 1,868 m"),V("Dimbula","","","Largest tea-growing district, centre Talawakelle"),V("Uva","","","Badulla district; Haputale and Bandarawela"),V("Low-grown Matara, Galle, Ratnapura","","","High astringency")],"elevation: high, mid, low · type: orthodox, CTC")]
chi=[
 A("Keemun (Qimen)","Qimen Red Tea","Anhui black tea, one of China's Ten Famous Teas, listed on Wikipedia's Chinese tea list.","","",W+'List_of_Chinese_teas',[],"province: Anhui"),
 A("Dianhong (Yunnan black)","Yunnan black tea","Yunnan black tea rich in golden buds, produced since the early 20th century and graded by orange pekoe.","","early 20th century",W+'Dianhong',[V("Broken Yunnan","","","BOP blending grade"),V("Yunnan Gold","","","OP to TGFOP"),V("Yunnan Pure Gold","","","TGFOP to SFTGFOP; only golden tips"),V("Golden Needle"),V("Pine Needle"),V("Yunnan Golden Snail")],"grade: BOP to SFTGFOP"),
 A("Lapsang Souchong (Zhengshan Xiaozhong)","Zhengshan Xiaozhong · smoked black tea","Wuyi Mountains black tea smoke-dried over pinewood; the unsmoked Tongmu style grew popular from the early 2000s.","","Qing dynasty",W+'Lapsang_souchong',[V("Tongmu unsmoked","","","Unsmoked variant from Tong Mu Guan village"),V("Jin Jun Mei","","2005","Bud-only descendant developed by Jiang Yuanxun's team")],"smoke: pine · region: Wuyi, Fujian"),
 A("Jin Jun Mei","","Fully oxidised, roasted black tea made only from early-spring buds in the Wuyi Mountains; among China's costliest black teas.","Wuyi Mountains Zhengshan Tea Industry","2005",W+'Jin_Jun_Mei_tea',[V("Master tea maker Liang Junde","","","Led the team of makers")],"buds only · Tongmu, Fujian"),
 A("Yingde Hong","Yingdehong","Chinese black tea listed on Wikipedia's list of Chinese teas.","","",W+'List_of_Chinese_teas',[],""),
 A("Ruby 18 (Taicha 18) / Sun Moon Lake","Hongyu · Sun Moon Lake black tea","Taiwanese cultivar hybrid of assamica and a native variety, bred in the 1990s; honey, cinnamon and mint notes.","Tea Research and Extension Station","1990s",W+'Taiwanese_tea',[V("Yuchi Black Tea Research Institute","","1926","Founded to study black tea")],"cultivar TTES 18 · region Nantou"),
]
afr=[
 A("Kenyan CTC black tea","Kenya tea","Crush-tear-curl tea from the Kenyan Highlands, sold at the Mombasa auction; KTDA smallholders run 66 factories.","Kenya Tea Development Agency","1903 introduced",W+'Tea_production_in_Kenya',[V("Limuru","","1903","First planting")],"type: CTC · auction: Mombasa"),
 A("Rize black tea","Turkish tea · çay","Black Sea black tea from Rize Province, mahogany in the glass, served in small tulip glasses strong (demli) or weak (açık).","","1912 experimental planting",W+'Rize_tea',[V("First local tea factory","","1947","")],"region: Rize"),
 A("Ilam tea (Nepal)","Nepali orthodox","Orthodox Nepalese tea from Ilam, where Nepal's first plantation was set up around 1863.","","c.1863",W+'Nepali_tea',[V("Ilam Tea Estate","","1863","First plantation"),V("Soktim Tea Estate","","c.1865","Also in Ilam"),V("Ilam factory","","1978","First Nepalese tea factory")],"flush: spring, summer, monsoon, autumn"),
]
rs="https://www.rishi-tea.com/collections/loose-leaf-teas?page=1"
kinds=[
 {"n":"Darjeeling tea","a":"Darjeeling","d":"Black tea of the Darjeeling hills, sold by flush and estate under a registered GI.","t":["first flush","second flush","autumnal","monsoon"],"s":dj,"x":darj},
 {"n":"Assam & Indian black tea","a":"Assam · Nilgiri · Kangra","d":"Black tea from Assam, Nilgiri, Kangra and other Indian regions; orthodox or CTC.","t":["orthodox","CTC"],"s":rs,"x":asm},
 {"n":"Ceylon tea","a":"Sri Lanka tea","d":"Black tea from Sri Lanka, sold by elevation region with the Lion logo marking pure Ceylon.","t":["orthodox","CTC","high-grown","low-grown"],"s":W+'Tea_production_in_Sri_Lanka',"x":cey},
 {"n":"Chinese & Taiwanese black tea","a":"hong cha · red tea","d":"Black teas from China and Taiwan, from Keemun and Yunnan to smoked Lapsang and bud-only Jin Jun Mei.","s":W+'List_of_Chinese_teas',"x":chi},
 {"n":"Kenyan, African & Black Sea tea","a":"African, Turkish and Himalayan black tea","d":"Black teas from Kenya, Turkey's Rize coast and Nepal's Ilam, plus other non-Indian, non-Chinese origins.","s":W+'Tea_production_in_Kenya',"x":afr},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Mariage Frères","France","1854","Premium","Paris tea house","Paris tea house founded by Henri and Edouard Mariage.","knowledge"),
 B("Fortnum & Mason","United Kingdom","1707","Premium","Piccadilly department store","London store with a long tea tradition.","knowledge"),
 B("Harney & Sons","United States","1983","Premium","loose and herbal tea","Connecticut-founded tea company, now in Millerton, New York.","knowledge"),
 B("Dammann Frères","France","","Premium","French tea house","French tea house.","knowledge"),
 B("Kusmi Tea","France","","Premium","Russian-style blends","French tea house founded by a Russian.","knowledge"),
 B("TWG Tea","Singapore","","Premium","luxury tea","Singapore luxury tea company.","knowledge"),
 B("Rishi Tea & Botanicals","United States","","Specialist","loose-leaf tea","US loose-leaf and botanical tea company.","knowledge"),
 B("Sri Lanka Tea Board","Sri Lanka","","Institution & issuer","Lion logo","Owner of the Lion logo for pure Ceylon tea.",W+'Tea_production_in_Sri_Lanka'),
 B("Tea Board of India","India","1953","Institution & issuer","GI licensing","Regulator of Darjeeling, Assam and Nilgiri tea since the Tea Act of 1953.",dj),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Old Assam, Ceylon Nuwara Eliya, Darjeeling, Dianhong, Keemun and Lapsang models became archetypes in the matching kinds. Left out unsourced: Halmari, Mangalam, Harmutty, Satemwa/Malawi, Rwanda, Georgian tea, Cay kur facts (not on page), Yingde Hong province details, CTC/orthodox definitions, Teekampagne. Yingde Hong archetype is thin (list entry only)."}
json.dump(out,open('01_01.src.json','w'),ensure_ascii=False)
