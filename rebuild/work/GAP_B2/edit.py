import json,os
p='rebuild/out/B2.json'
d=json.load(open(p))
W='https://en.wikipedia.org/wiki/'
def ent(n,y,dd,s,g=None):
    e={"n":n,"a":"","d":dd,"mk":"","y":y,"s":s,"v":[]}
    if g: e["g"]=g
    return e
K={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
def add(kn,es,cov):
    k=K[kn]; have={x['n'].lower() for x in k['x']}
    for e in es:
        if e['n'].lower() in have: continue
        if 'xg' in k and 'g' not in e and k['x'] and k['x'][0].get('g'): print('NOG',kn,e['n'])
        k['x'].append(e)
    k['sel']=k['sel'].split(' Covers ')[0].split(' Complete:')[0].rstrip()+' '+cov
add('Central Asian rug',[
 ent('Uzbek Julkhyr','','Long, coarsely woven sleeping rug made mainly in Uzbekistan and by Uzbeks in northern Afghanistan.',W+'Uzbek_Julkhyr','Uzbek rugs'),
 ent('Uzbek Napramach','late 19th century','Floor rug made largely in Uzbekistan.',W+'Uzbek_Napramach','Uzbek rugs')],
 'Complete: 7 of 7 rug pages in Category:Turkic_rugs_and_carpets and Category:Uzbekistani_rugs_and_carpets (Turkmen rug, Yomut, Asmalyk, Chul, Uzbek carpet, Uzbek Julkhyr, Uzbek Napramach); Shakhrisabz Suzani is held under Suzani.')
add('Chinese rug',[ent('Khotan','c. 1800–1930s','Hand-knotted wool carpet from Khotan (Hotan) in the Tarim Basin, Xinjiang, on the Silk Road.','https://rugsonnet.com/rug-types-styles/khotan-rugs/')],
 'No complete list exists; Wikipedia\'s Chinese carpet article names no rug types, so the five entries follow the dealer overviews of Ningxia, Baotou, Peking, Khotan and Chinese Art Deco (Tianjin rugs are the same Art Deco output).')
add('Tibetan rug',[ent('Potala rug','','Lhasa workshop design showing the Potala Palace, made for wall hanging.',W+'Tibetan_rug')],
 'Complete: 4 of 4 rug types named on the Tibetan rug page (Khaden, tiger rug, Wangden, Potala); its weaving centres and period styles are not entries.')
add('Moroccan rug',[ent('Fes carpet','Marinid period','Carpet of Fes, called the most important carpet-producing city in Morocco.',W+'Moroccan_rugs'),
 ent('Ait Bou Ichaouen','','Weaving of a nomadic Berber tribe, named in the Moroccan rugs page reading list.',W+'Moroccan_rugs')],
 'Complete: the Moroccan rugs page (Fes, Rabat, Beni Ourain, Ait Bou Ichaouen, Berber carpet) read in full; Berber carpet is the general name already held as alias, and the other entries come from the dealer overview.')
add('Rya rug',[],'Complete: 3 of 3 rug traditions in the Rya and Scandinavian rugs pages (Swedish rya, Finnish ryijy; Ege Rya from the earlier pass); Rölakan is held under Flatweave rug, and the Marby carpet is a single object.')
nv=[('Klagetoh',''),('Burntwater',''),('Yei be Chei',''),('Pine Springs',''),('Sand Painting',''),('Spider Rock',''),('Pictorial rug',''),('Burnham',''),('JB Moore plate rug',''),('Diamond Twill',''),('Two Faced',''),('Blue Canyon',''),('Saddle blanket','')]
add('Navajo rug',[ent(n,y,'Navajo weaving style or regional pattern named in the Navajo weaving article.',W+'Navajo_weaving') for n,y in nv],
 'Complete: 25 of 25 regional styles and patterns named in the Navajo weaving article (read to its end), with Coal Mine Mesa and Newlands outlines held under Raised Outline and the Oriental and Persian styles left out as imitations.')
add('Hooked rug',[ent('Yorkshire hooky mat','early 19th century','English floor mat of hooked rag strips, the earliest hooked-rug form the Hooked rug article names.',W+'Hooked_rug'),
 ent('Turkey rug','1930','Latch-hooked rug form described in Kent\'s 1930 book.',W+'Hooked_rug'),
 ent('Thunderbird latch-hooked rug','late 20th century','Latch-hooked rug design named in the Hooked rug article.',W+'Hooked_rug')],
 'Complete: the place and style traditions named in the Hooked rug article (Yorkshire, Grenfell, Chéticamp, Waldoboro from its own source, Turkey rug, Thunderbird); makers, methods and museums are not entries.')
add('Felt rug',[],'No complete list exists; the Wikipedia Felt article names only Shyrdak, and Ala kiyiz comes from its own page. Namda and other felt rugs had no fetched page with a date.')
add('Flatweave rug',[],'Complete: 11 of 11 flatweave pages in the categories (Khes, a cotton damask cloth, is held under Blanket); Zili and Rölakan are kept from the earlier pass.')
add('Quilt',[
 ent('Pictorial quilt','from 1795','Quilt with a scene or figures worked in appliqué or piecing.',W+'Quilt'),
 ent('Native American star quilt','late 19th century','Star-pattern quilt made by Native American makers.',W+'Quilt'),
 ent('New York Beauty quilt','name marketed in the 1930s','Pieced quilt pattern family.',W+'Quilt'),
 ent('Seminole patchwork','','Strip-pieced patchwork tradition of the Seminole.',W+'Quilt'),
 ent('Nine-patch quilt','','Pieced quilt pattern family built from nine squares.',W+'Quilt'),
 ent('Cathedral Windows quilt','','Folded-fabric quilt pattern family.',W+'Quilt'),
 ent('Provençal quilt','since the 17th century','Quilting of Provence, including boutis, matelassage and piqûre de Marseille.',W+'Quilt'),
 ent('Lancashire double-cloth quilt','late 18th to early 20th century','Quilt of the Lancashire tradition made from two cloths.',W+'Quilt'),
 ent('Kilis quilt','','Turkish quilt style of the city of Kilis, stitched on a glossy satin top backed with muslin.',W+'Kilis_quilts'),
 ent('Godadi','','Indian patchwork quilt, often embroidered, stitched from assorted fabric scraps.',W+'Godadi'),
 ent('Razai','','South Asian quilt filled with cotton wool, similar to a duvet; the Jaipuri razai is a named form.',W+'Razai'),
 ent('Tivaevae','','Quilt tradition of the Cook Islands.',W+'Quilt'),
 ent('Khayamiya','','Appliqué quilt tradition of Egypt.',W+'Quilt'),
 ent('Mola','','Appliqué panel tradition of the Kuna.',W+'Quilt'),
 ent('Kavudi','','Quilt tradition of India.',W+'Quilt'),
 ],'Complete: 28 of 28 quilt traditions and pattern families named in the Wikipedia Quilt article (read to its end); individual named works and memorial quilts, techniques (trapunto, appliqué, piecing) and non-quilt appliqué forms are left out as content or method, and Nakshi kantha is held under Kantha.')
add('Blanket',[
 ent('Basotho blanket','1876','Woollen garment of the Sotho in Lesotho and South Africa, traced to a gift to King Moshoeshoe I.',W+'Basotho_blanket'),
 ent('Lizhnyk','1920s','Woven wool covering of the Hutsul people of the Ukrainian Carpathians, also called a Hutsul blanket.',W+'Lizhnyk'),
 ent('Button blanket','mid-1800s','Woollen wrap decorated with shell buttons, made by Northwest Coast peoples for ceremonial wear.',W+'Button_blanket'),
 ent('Khes','','Thick hand-woven cotton damask cloth of northern India and Pakistan, used for blankets and wraps.',W+'Khes')],
 'Complete: the named blanket traditions in Category:Blankets (Basotho blanket, Hudson\'s Bay point blanket, Lizhnyk, Button blanket, Khes); Navajo blanket is held under Navajo rug, Godadi and Razai under Quilt, and the rest are modern products or general kinds.')
add('Printed & embroidered furnishing textile',[ent('Strawberry Thief','1883','Repeating textile pattern by William Morris showing thrushes raiding fruit at Kelmscott Manor.',W+'Strawberry_Thief')],
 'Complete: the furnishing-cloth pages in Category:Textile_patterns (Strawberry Thief, Toile, Ikat); the other pages are clothing cloths, motifs or brands, and Suzani and Josef Frank prints come from the earlier pass.')
add('Tablecloth',[ent('Perugia tablecloth','medieval','White table linen woven with blue stripes and patterns.',W+'Tablecloth'),
 ent('Hedebo embroidery','from the 1760s','Danish whitework and needle-lace technique from Zealand used on tablecloths and serviettes.',W+'Hedebo_embroidery'),
 ent('Maramureș tablecloth','','Traditional Romanian tablecloth from Maramureș.',W+'Tablecloth')],
 'Complete: the named traditions in the Tablecloth article (Perugia, Maramureș) with Hedebo from its own page and the earlier Basque and Provençal entries; Victorian, damask, crochet and runner are styles or types, not entries.')
tmp=p+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.rename(tmp,p)
