import json, os
W='https://en.wikipedia.org/wiki/'
MK=W+'Makgeolli'; CJ=W+'Cheongju_(beverage)'; HJ=W+'Huangjiu'; SX=W+'Shaoxing_wine'; KS=W+'Kooksoondang'; KAD=W+'Korean_alcoholic_drinks'; BJ=W+'Beopju'
AS='https://www.asiae.co.kr/en/article/2020041711095107081'
def v(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Makgeolli","a":"takju · nongju · makkoli","d":"Korean milky, lightly sparkling, unfiltered rice wine fermented with nuruk, usually 6–9% ABV.",
 "t":["Fresh unpasteurised (saeng)","Pasteurised / shelf-stable","Fruit-flavoured (chestnut, peach, strawberry, banana, grape)","Honey (kkul-makgeolli)","Nuruk-brewed vs manufactured-starter","Dansul (sweet, partly fermented)"],
 "s":"https://waso.uk/items/Kooksoondang-Makgeolli-6-750ml",
 "x":[
  {"n":"Dongdong-ju","a":"float-float wine","d":"Creamier makgeolli-type wine with unfiltered rice grains floating in it, associated with Gyeonggi Province.","mk":"","y":"","s":MK,"v":[],"dt":"rice grains floating · creamy body"},
  {"n":"Ihwa-ju","a":"pear-blossom wine","d":"Very thick makgeolli brewed with rice malt in pear-blossom season, sometimes eaten with a spoon.","mk":"","y":"Goryeo","s":MK,"v":[],"dt":"thickness · rice malt"},
  {"n":"Geumjeongsanseong Makgeolli","a":"","d":"Busan nuruk-brewed makgeolli whose brewer is the country's only officially recognised makgeolli master (2023).","mk":"","y":"","s":MK,"v":[],"dt":"traditional nuruk · Busan"},
  {"n":"Jangsu Saeng Makgeolli","a":"Seoul Jangsoo","d":"Seoul's best-selling fresh makgeolli, sold within a 10-day window; top domestic seller since launch.","mk":"Seoul Jangsu","y":"1996","s":AS,
   "v":[v("Jangsu Saeng Makgeolli 6%","Seoul Jangsu","1996","fresh, unpasteurised"),v("Insaeng Makgeolli 5%","Seoul Jangsu","2018","lower-alcohol line")],"dt":"6% · 5% · clear PET bottle"},
  {"n":"Kooksoondang Makgeolli","a":"Kooksoondang rice makkoli","d":"Kooksoondang's export-wide makgeolli range, canned and bottled, plain and fruit-flavoured.","mk":"Kooksoondang","y":"","s":KS,
   "v":[v("Kooksoondang Makgeolli 6%","Kooksoondang"),v("Kooksoondang Makgeolli Chestnut 4%","Kooksoondang"),v("Kooksoondang Makgeolli Peach 3%","Kooksoondang"),v("Kooksoondang Makgeolli Strawberry 3%","Kooksoondang"),v("Kooksoondang Makgeolli Green Grape 3%","Kooksoondang")],"dt":"plain 6% · fruit 3–4% · can, bottle, draught"}]},
{"n":"Cheongju","a":"yakju · malgeun-sul · chungju","d":"Korean clear refined rice wine, drawn off the settled ferment of steamed rice and nuruk.",
 "t":["Flavoured: chrysanthemum (gukhwa-ju)","Flavoured: azalea (dugyeon-ju)","Flavoured: pine sprout (songsun-ju)","Flavoured: lotus leaf (yeonyeop-ju)","Flavoured: ginseng (insam-ju)","Glutinous-rice or black-rice base"],
 "s":"https://www.danmurphys.com.au/product/DM_ER_1000003185_YC-YANGCHON500ML/yangchon-premium-korean-cheongju-500ml",
 "x":[
  {"n":"Gyodong Beopju","a":"Gyeongju beopju · hundred-days liquor","d":"Gyeongju cheongju of glutinous rice, wheat nuruk and water, fermented about 100 days; Intangible Cultural Property No. 86-3 (1986).","mk":"","y":"Joseon","s":BJ,
   "v":[v("Gyodong-beopju (Gyerim Choe clan head-house)","","1986","designated recipe, 16–18% ABV")],"dt":"16–18% ABV · brewed September–April"},
  {"n":"Hansan Sogok-ju","a":"sogok-ju","d":"Cheongju from Hansan with a claimed history of about 1,500 years, among Korea's oldest sul.","mk":"","y":"","s":KAD,"v":[],"dt":""},
  {"n":"Myeoncheon Dugyeon-ju","a":"azalea wine","d":"Azalea-petal rice wine from Chungcheong, about 21% ABV; Important Intangible Cultural Property No. 86-2.","mk":"","y":"","s":KAD,"v":[],"dt":"about 21% ABV · azalea petals"},
  {"n":"Baekseju","a":"Bekseju · Bek Se Ju","d":"Yakju infused with ginseng and eleven other herbs, about 13% ABV; Kooksoondang's best-known product.","mk":"Kooksoondang","y":"","s":KAD,
   "v":[v("Bekseju","Kooksoondang"),v("Bekseju Dry","Kooksoondang"),v("Kangjang Bekseju","Kooksoondang"),v("50seju","Kooksoondang","","")],"dt":"about 13% ABV · herbal"}],
 "m":[["Sulseam Seosul","Sulseam"],["Yangchon Premium Korean Cheongju","Yangchon Brewery"]]},
{"n":"Huangjiu","a":"yellow wine · amber rice wine · Chinese rice wine","d":"Chinese grain wine of rice, glutinous rice or millet fermented with qu, typically 8–20% ABV and jar-aged.",
 "t":["Dry (gan, ≤1% sugar)","Semi-dry (ban gan, 1–3%)","Semi-sweet (ban tian, 3–10%)","Sweet (tian, 10–20%)","Extra-sweet (nong tian, ≥20%)","Aged / vintage-dated (chen nian)","Red-qu (hongqu) wine","Cooking wine (liaojiu)"],
 "s":"https://www.thewhiskyexchange.com/p/83551/gu-yue-long-shan-10-year-old-shaoxing-rice-wine",
 "x":[
  {"n":"Shaoxing wine","a":"Shaoxing jiu · Shao Hsing","d":"Originating huangjiu of Shaoxing, Zhejiang, from glutinous rice, water and wheat qu; drunk and used in cooking.","mk":"","y":"","s":SX,
   "v":[v("Yuanhong jiu","","","dry"),v("Jiafan jiu","","","semi-dry, extra rice"),v("Shanniang jiu","","","sweet; brewed with aged yuanhong in place of water"),v("Xiangxue jiu","","","very sweet"),v("Huadiao jiu / Nü'er hong","","","glutinous rice and wheat, about 16%")],"dt":"sugar class · years aged · jar or bottle"},
  {"n":"Gu Yue Long Shan","a":"Guyue Longshan","d":"Shaoxing wine from Zhejiang Gu Yue Long Shan Shaoxing Wine Co., the leading Shaoxing house.","mk":"Gu Yue Long Shan","y":"","s":HJ,
   "v":[v("Gu Yue Long Shan 10 Year Old Shaoxing Rice Wine","Gu Yue Long Shan")],"dt":"age statements"},
  {"n":"Kuaijishan","a":"Kuai Ji Shan · Huijishan","d":"Shaoxing wine named after the local Kuaiji mountain.","mk":"Kuaijishan","y":"","s":SX,"v":[],"dt":""},
  {"n":"Huiquan jiu","a":"Su-shi laojiu","d":"Wuxi wine, the iconic Jiangsu-style aged huangjiu.","mk":"","y":"","s":HJ,"v":[],"dt":""},
  {"n":"Fujian nuomijiu","a":"Fujian glutinous rice wine","d":"Glutinous-rice wine with added medicinal herbs, about 18% ABV.","mk":"","y":"","s":HJ,"v":[],"dt":"about 18% ABV · herbs"},
  {"n":"Honglu jiu","a":"","d":"Taiwanese red-qu rice wine whose brands trace to the 1910s.","mk":"","y":"1910s","s":HJ,"v":[],"dt":""}]}]
brands=[
 {"n":"Kooksoondang","c":"South Korea","f":"1952","seg":"Traditional liquor brewer","d":"Seoul-based brewer of Bekseju, makgeolli and fruit wines.","lines":["Bekseju","Rice makkoli","Myungjak"],"eras":[],"sig":["Baekseju","Kooksoondang Makgeolli"],"sc":[],"rel":[],"s":KS},
 {"n":"Seoul Jangsu","c":"South Korea","f":"2009","seg":"Makgeolli brewer","d":"Subsidiary of the Seoul Takju Manufacturing Association making Jangsu Saeng Makgeolli.","lines":["Jangsu Saeng Makgeolli","Insaeng Makgeolli"],"eras":[],"sig":["Jangsu Saeng Makgeolli"],"sc":[],"rel":[],"s":AS},
 {"n":"Gu Yue Long Shan","c":"China","f":"","seg":"Shaoxing wine producer","d":"Zhejiang Gu Yue Long Shan Shaoxing Wine Co., Ltd., Shaoxing huangjiu maker.","lines":[],"eras":[],"sig":["Gu Yue Long Shan"],"sc":[],"rel":["Kuaijishan"],"s":HJ},
 {"n":"Kuaijishan","c":"China","f":"","seg":"Shaoxing wine producer","d":"Shaoxing wine house named after the local Kuaiji mountain.","lines":[],"eras":[],"sig":["Kuaijishan"],"sc":[],"rel":["Gu Yue Long Shan"],"s":SX}]
trads=[
 {"n":"Korean traditional liquor (sul)","g":"Food & drink","r":"Korea","p":"Three Kingdoms to present; revived after 1990s","d":"Home and regional brewing of rice wines and spirits with nuruk starters, suppressed under colonial rule and grain laws.","tech":"Multi-stage fermentation of steamed rice with nuruk; clear cheongju drawn off, cloudy takju kept unfiltered","mat":"Rice, glutinous rice, wheat nuruk, water, flowers and herbs","forms":["Makgeolli","Cheongju","Gyodong Beopju","Myeoncheon Dugyeon-ju","Hansan Sogok-ju"],"ctr":["Gyeongju (Gyerim Choe clan)","Hansan","Myeoncheon"],"auth":"Designated intangible-heritage recipes (e.g. No. 86-2, 86-3); traditional nuruk rather than manufactured starter","s":KAD},
 {"n":"Shaoxing wine brewing","g":"Food & drink","r":"Shaoxing, Zhejiang, China","p":"Ancient; spread nationally in the late Qing","d":"Glutinous-rice huangjiu brewing with wheat qu, aged in earthenware jars and dated by brewing year.","tech":"Fermentation with wheat-based qu; jar ageing for years or decades","mat":"Glutinous rice, wheat qu, local water","forms":["Shaoxing wine","Yuanhong jiu","Jiafan jiu","Shanniang jiu","Xiangxue jiu","Nü'er hong"],"ctr":["Gu Yue Long Shan","Kuaijishan"],"auth":"Wine from outside Shaoxing labelled as Shaoxing is a common fraud","s":SX}]
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":"Kept all 3 old kinds. Old models became archetype versions (Kooksoondang, Gu Yue Long Shan) or stay in m (Sulseam, Yangchon cheongju). Left out: Kuaijishan/Gu Yue Long Shan founding years and formal huangjiu age grades (no retrieved source gives them; age is a 't' attribute), a commercial 'Gyeongju Beopju' company line (no page retrieved; the Gyodong beopju heritage recipe is used instead), Tapai/Pagoda brand and Chungha (not confirmed on a retrieved page). Wikidata returned 429."}
p='work/J7/shelves/08_01.json'; t=p+'.tmp'; json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
