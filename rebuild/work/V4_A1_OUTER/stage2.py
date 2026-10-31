import json,re
R='/home/user/Possession-Taxonomy/'
S=json.load(open(R+'rebuild/work/V4_A1_OUTER/stage1.json'))
REG={x['n'].lower() for x in json.load(open(R+'rebuild/out/A1_brands.json'))['b']}
W='https://en.wikipedia.org/wiki/'
ART={'Fur coat':('Fur clothing',0),'Leather & suede jacket':('Leather jacket',0),'Cut-off vest':('Leather jacket',0),'Overcoat':('Overcoat; Trench coat',0),'Pea coat':('Pea coat',0),'Duffle coat':('Duffel coat',0),'Trench coat':('Trench coat',0),
'Raincoat':('Raincoat',0),'Parka':('Parka',0),'Puffer coat':('Down jacket',0),'Puffer jacket':('Down jacket',0),'Puffer vest':('Gilet',0),
'Cape':('Cape',0),'Flight jacket':('Flight jacket; Bomber jacket',0),'Field jacket':('Trench coat; Safari jacket',0),'Biker jacket':('Perfecto motorcycle jacket',0),
'Waxed cotton jacket':('Waxed jacket',0),'Mackinaw':('Mackinaw coat',0),'Norfolk jacket':('Norfolk jacket',0),'Trucker jacket':('Jean jacket',0),
'Harrington jacket':('Harrington jacket',0),'Varsity jacket':('Letterman (sports)',0),'Track jacket':('Tracksuit',0),'Tracksuit':('Tracksuit',0),
'Bolero':('Bolero jacket',0),'Shell jacket':('Parka',0),'Anorak':('Parka',0),'Fleece jacket & pullover':('Polar fleece',0),
'Business suit':('Suit',168380),'Blazer':('Blazer',0),'Waistcoat':('Waistcoat',110474),'Tuxedo':('Tuxedo',190725),'Morning dress':('Morning dress; Tuxedo',142835),
'Tailcoat':('Tailcoat',0),'Smoking jacket':('Smoking jacket',0),'Tie':('Necktie',157287),'Bow tie':('Bow tie',0),'Ascot & cravat':('Bow tie; Necktie',157287),
'Cummerbund & collar stay':('Cummerbund',0),'Pocket square':('Handkerchief',0),'Braces':('Suspenders',0),'Work trousers':('Overalls',0),
'Overalls':('Overalls',0),'Boiler suit':('Boilersuit',0),'Chore coat':('Chore jacket',0),'Work jacket':('Chore jacket',0),'Donkey jacket':('Donkey jacket',0),
"Chef's jacket":("Chef's uniform",0),'Scrub top':('Scrubs (clothing)',0),'Lab coat':('Lab coat',0)}
TRUNC0={'Mackinaw':'6,937 of 106,937','Business suit':'68,380 of 168,380','Waistcoat':'10,474 of 110,474','Tuxedo':'90,725 of 190,725','Morning dress':'42,835 of 142,835','Tie':'57,287 of 157,287','Ascot & cravat':'57,287 of 157,287'}

WP='https://en.wikipedia.org/wiki/'
def F(mkt,who,share,yr,s,note): return {"mkt":mkt,"who":who,"share":share,"yr":yr,"s":s,"note":note}
MS={
'Coats & jackets':([
 F('Outdoor and outerwear group revenue','VF Corporation (The North Face since 2000, Napapijri since 2004, Smartwool 2011, Icebreaker 2018)','US$10.45 billion',2024,WP+'VF_Corporation','group revenue as the page states; VF is the owner of The North Face'),
 F('Luxury down outerwear','Moncler','EUR 3.13 billion',2025,WP+'Moncler','group revenue; Moncler bought Stone Island in December 2020 for EUR 1.15 billion'),
 F('Parka maker','Canada Goose (Bain Capital and others)','CA$1.35 billion',2025,WP+'Canada_Goose_Inc.','revenue for the year to 30 March 2025; Bain bought a 70 percent stake in December 2013'),
 F('British waxed and quilted jackets','Barbour (J. Barbour & Sons, family-led)','GBP 225 million',2019,WP+'Barbour_(company)','revenue for the year ending 30 April 2019'),
 F('Trench coat house','Burberry Group plc','GBP 2,420 million',2026,WP+'Burberry','revenue in the infobox, marked as a decrease; floated on the London Stock Exchange in July 2002'),
 F('Heritage workwear and jackets','Carhartt (family owned)','US$1.8 billion',2024,WP+'Carhartt','revenue in the infobox'),
 ],'Outerwear revenue is given for the owner groups and houses that publish it: VF Corporation US$10.45 billion (2024), Moncler EUR 3.13 billion (2025), Canada Goose CA$1.35 billion (year to March 2025), Barbour GBP 225 million (2019). No category-wide market share was found on a fetched page.'),
'Suits & formalwear':([
 F('Tailoring and menswear group','HUGO BOSS, BOSS Menswear','EUR 3,329 million (77 % of Group sales)',2024,'https://annualreport.hugoboss.com/2024/management-report/report-on-economic-position/earnings-development/sales-performance.html','brand sales in the 2024 annual report; Group sales EUR 4,307 million'),
 F('Tailoring and menswear group','HUGO BOSS, HUGO','EUR 682 million (16 %)',2024,'https://annualreport.hugoboss.com/2024/management-report/report-on-economic-position/earnings-development/sales-performance.html','brand sales in the 2024 annual report'),
 F('Tailoring and menswear group','HUGO BOSS, BOSS Womenswear','EUR 297 million (7 %)',2024,'https://annualreport.hugoboss.com/2024/management-report/report-on-economic-position/earnings-development/sales-performance.html','brand sales in the 2024 annual report'),
 F('Ready-to-wear trench and tailoring house','Burberry Group plc','GBP 2,420 million',2026,WP+'Burberry','revenue in the infobox'),
 ],'HUGO BOSS reported Group sales of EUR 4,307 million in 2024, of which BOSS Menswear was EUR 3,329 million. The annual report gives no tailoring-only figure and no category-wide share was found.'),
'Workwear & uniform clothing':([
 F('Heritage workwear','Carhartt (family owned)','US$1.8 billion',2024,WP+'Carhartt','revenue in the infobox; about US$600 million a year in 2013'),
 F('Workwear brand sale','Dickies, sold by VF Corporation to Bluestar Alliance','about US$600 million',2025,WP+'Dickies','cash price; VF had bought Williamson-Dickie for US$820 million in 2017'),
 F('Jeans and workwear group','Kontoor Brands (Lee, Wrangler; spun off from VF in May 2019)','US$3.15 billion',2025,WP+'Kontoor_Brands','revenue as the page states'),
 ],'Carhartt reported US$1.8 billion revenue in 2024. Dickies changed hands from VF Corporation (bought 2017, US$820 million) to Bluestar Alliance (2025, about US$600 million). No category-wide workwear share was found.'),
}
cnt=0
for dp in S['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            x=k.get('x',[])
            b=sum(1 for e in x if e['g']!='Named forms without a brand'); f=len(x)-b
            art=ART.get(k['n'])
            if x:
                a=art[0] if art else 'the garment article named in s'
                line=f"Follows two references: the register's signature pieces and lines for this garment (each on the brand page named in s) and the brands and named types in Wikipedia: {a}."
                cov=f" Complete: {b} of {b} brand pieces from the register and from pages recorded in the earlier harvest for this garment, {f} named forms from the fetched article (long articles read in two windows to their end)."
                if k['n']=='Fur coat': cov=f" Covers {len(x)} entries; the article was read except its last 1,160 characters."
                k['sel']=line+cov+" Brands outside the 2,531-brand register are not listed."
            else:
                k['sel']=("No entries. "+(f"The fetched Wikipedia article ({art[0]}) names no brand or list of named types for this garment. " if art else "No Wikipedia article on this garment was fetched. ")+"No signature piece in the brand register matches it. Complete: 0 of 0.")
            cnt+=1
    dp['ms'],dp['msum']=MS[dp['n']]
# brands
new=[
 ('Eddie Bauer','United States','Outdoor brand named in the Down jacket article for the 1936 Skyliner.',W+'Down_jacket','Outdoor & technical'),
 ('Peter Storm','United Kingdom','Maker of the cagoule, credited to Noel Bibby in the early 1960s.',W+'Parka','Outdoor & technical'),
 ('Castell & Son','United Kingdom','Oxford firm opened in 1846, credited with the first modern-style necktie in 1870.',W+'Necktie','Heritage & workwear'),
 ('Gannex','United Kingdom','Raincoat style named in the Raincoat article.',W+'Raincoat','Heritage & workwear'),
 ('Driza-Bone','Australia','Oilskin coat style named in the Raincoat article.',W+'Raincoat','Heritage & workwear'),
 ("Hudson's Bay Company",'Canada','Supplier of point blankets and later of the point blanket coat.',W+'Mackinaw_coat','Heritage & workwear'),
 ('Blue Bell','United States','North Carolina overall maker begun in 1904, popular with railroad workers.',W+'Overalls','Heritage & workwear'),
 ('Grenfell','United Kingdom','Formerly Haythornthwaite and Sons; claims an identical golf jacket to Baracuta\'s.',W+'Harrington_jacket','Heritage & workwear'),
 ('Le Coq Sportif','France','French sportswear maker said to have first made sweatpants in 1920.',W+'Tracksuit','Athletic & sportswear'),
 ('One-In-Hand Tie Company','United States','Clinton, Iowa, maker of pre-tied and clip-on neckties.',W+'Necktie','Heritage & workwear'),
 ('Jesse Langsdorf','United States','New York tie maker who introduced bias-cut ties in 1922.',W+'Necktie','Heritage & workwear'),
 ('Outdoor Research','United States','Down parka maker; the Coze Down Parka has 240 grams of 700-fill down.','https://www.outdoorgearlab.com/reviews/clothing-womens/winter-jacket-womens/outdoor-research-coze-down-parka','Outdoor & technical'),
 ('Stio','United States','Maker of the Hometown Down Hooded Jacket, insulated with 800-fill down.','https://elevationoutdoors.com/?p=44444','Outdoor & technical'),
 ('Decathlon','France','Maker of the Simond MT100 hooded down puffer.','https://www.outdoorgearlab.com/reviews/clothing-mens/down-jacket-men/decathlon-simond-mt100-hooded-puffer','Value & basics'),
 ('Nobis','Canada','Maker of the Nord Men\'s Tailored Trench Coat.','https://us.nobis.com/products/nord-mens-tailored-trench-coat','Outdoor & technical'),
 ('Ossie Clark','United Kingdom','Designer of the 1969 Lamborghini trouser suit held by the V&A.','https://collections.vam.ac.uk/item/O86592/lamborghini-trouser-suit-clark-ossie/','Designer'),
 ('George Key','United Kingdom','Rugeley draper who developed the donkey jacket in 1888.',W+'Donkey_jacket','Heritage & workwear'),
]
brands=[{'n':n,'c':c,'f':'1846' if n=='Castell & Son' else ('1904' if n=='Blue Bell' else ''),'seg':seg,'d':d,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,'kf':''} for n,c,d,s,seg in new if n.lower() not in REG]
segs=set(json.load(open(R+'rebuild/out/A1_brands.json'))['b'][i]['seg'] for i in range(2531))
print('segs',sorted(segs))
OWN={'Aquascutum':('Shandong Ruyi','Independent',''),"Arc'teryx":('Amer Sports','Global group',''),'Mackintosh':('Yagi Tsusho','Independent',''),'Napapijri':('VF Corporation','Global group','2004'),'Rab':('Equip','Independent',''),'Stone Island':('Moncler','Global group','2020'),'The North Face':('VF Corporation','Global group','2000'),'DAKS':('Sankyo Seiko','Independent','1991'),"OshKosh B'gosh":("Carter's",'Global group',''),'Stubbies':('Workwear Group','Independent',''),'Fjällräven':('Fenix Outdoor','Independent',''),'Lacoste':('Maus Frères','Independent','')}
bu={n:{'own':o[0],'tier':o[1],'c':{x['n']:x.get('c','') for x in json.load(open(R+'rebuild/out/A1_brands.json'))['b']}[n]} for n,o in OWN.items()}
for n,o in OWN.items():
    if o[2]: bu[n]['own_y']=o[2]
import os
os.makedirs(R+'rebuild/out/A1_parts',exist_ok=True)
for dp in S['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x',[]):
                if e.get('mk')=='DuPont': e['g']='United States';e['cty']='United States'
part={'replaces':['Coats & jackets','Suits & formalwear','Workwear & uniform clothing'],'depts':S['depts'],'brands':brands,'brand_updates':bu,'renames':{},'moves':[]}
json.dump(part,open(R+'rebuild/out/A1_parts/OUTER.json','w'),ensure_ascii=False,indent=0)
print(len(brands),'new brands',os.path.getsize(R+'rebuild/out/A1_parts/OUTER.json'))
