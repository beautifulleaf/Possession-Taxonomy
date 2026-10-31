import json
W='https://en.wikipedia.org/wiki/'
G='Global group';I='Independent';N='National champion'
# (owner, tier, source, default seg, country, [(brand, year or None)])
D=[
('LVMH',G,W+'LVMH','Luxury house',[('Louis Vuitton',None),('Christian Dior Couture',2017),('Celine',None),('Loewe',None),('Kenzo',None),('Givenchy',None),('Fendi',None),('Emilio Pucci',None),('Berluti',None),('Loro Piana',None),('Rimowa',None),('Patou',None),('Barton Perreira',None),('Vuarnet',None),('JW Anderson',None),('Moynat',None),('Bulgari',2011),('Chaumet',None),('Fred',None),('Hublot',None),('TAG Heuer',None),('Zenith',None),('Tiffany & Co.',2021)]),
('Kering',G,W+'Kering','Luxury house',[('Gucci',1999),('Yves Saint Laurent',1999),('Saint Laurent',1999),('Boucheron',2000),('Bottega Veneta',2001),('Balenciaga',2001),('Alexander McQueen',2001),('Brioni',2011),('Qeelin',2012),('Pomellato',2012),('Dodo',2012)]),
('Richemont',G,W+'Richemont','Luxury house',[('Alaïa',None),('AZ Factory',None),('Chloé',None),('Delvaux',None),('Dunhill',None),('Gianvito Rossi',2023),('Montblanc',None),('Peter Millar',None),('Purdey',None),('Serapian',None),('Buccellati',None),('Cartier',None),('Van Cleef & Arpels',None),('Vhernier',2024)]),
('Inditex',G,'https://www.inditex.com/itxcomweb/en/brands','High street',[('Zara',None),('Pull&Bear',None),('Massimo Dutti',None),('Bershka',None),('Stradivarius',None),('Oysho',None),('Zara Home',None),('Lefties',None)]),
('H&M Group',G,W+'H%26M','High street',[('H&M',None),('COS',None),('& Other Stories',None),('Weekday',None),('Monki',None),('Cheap Monday',None),('ARKET',2017),('Afound',None),('Sellpy',None)]),
('Fast Retailing',G,W+'Fast_Retailing','High street',[('Uniqlo',None),('Theory',2004),('Helmut Lang',None),('J Brand',2012),('Comptoir des Cotonniers',None),('GU',None),('Princesse Tam-Tam',None)]),
('Gap Inc.',G,W+'Gap_Inc.','High street',[('Gap',None),('Banana Republic',None),('Old Navy',None),('Athleta',2008),('Intermix',None),('Janie and Jack',None)]),
('PVH Corp.',G,W+'PVH_(company)','Contemporary & premium',[('Tommy Hilfiger',2010),('Calvin Klein',2002)]),
('Tapestry, Inc.',G,W+'Tapestry,_Inc.','Contemporary & premium',[('Coach',None),('Kate Spade New York',2017)]),
('Capri Holdings',G,W+'Capri_Holdings','Contemporary & premium',[('Michael Kors',None),('Jimmy Choo',2017)]),
('Prada Group',G,W+'Prada','Luxury house',[('Prada',None),('Miu Miu',None),('Versace',2025),("Church's",1999)]),
('VF Corporation',G,W+'VF_Corporation','Outdoor & technical',[('The North Face',2000),('Timberland',2011),('Vans',2004),('Napapijri',2004),('Smartwool',2011),('Icebreaker',2018),('Altra Running',2018),('Eastpak',2000),('JanSport',1986),('Kipling',2004)]),
('Kontoor Brands',I,W+'VF_Corporation','Heritage & workwear',[('Lee',None),('Wrangler',None)]),
('Levi Strauss & Co.',G,W+'Levi_Strauss_%26_Co.','Heritage & workwear',[("Levi's",None),('Denizen',None),('Beyond Yoga',2021)]),
('Moncler Group',G,W+'Moncler','Luxury house',[('Moncler',None),('Stone Island',2020)]),
('OTB',G,W+'OTB_(company)','Designer',[]),
('Nike, Inc.',G,W+'Nike,_Inc.','Athletic & sportswear',[('Nike',None),('Converse',2003)]),
('Adidas AG',G,W+'Adidas','Athletic & sportswear',[('Adidas',None),('Five Ten',2011)]),
('Puma SE',G,W+'Puma_(brand)','Athletic & sportswear',[('Puma',None),('Cobra Golf',2010)]),
('Under Armour, Inc.',G,W+'Under_Armour','Athletic & sportswear',[('Under Armour',None)]),
('Anta Sports',G,W+'Anta_Sports','Athletic & sportswear',[('Anta',None),('Fila',2009),('Descente',None),('Kolon Sport',2017),('Jack Wolfskin',None)]),
('Li-Ning Company',N,W+'Li-Ning','Athletic & sportswear',[('Li-Ning',None)]),
('Amer Sports',G,W+'Amer_Sports','Outdoor & technical',[("Arc'teryx",None),('Salomon',2005),('Atomic',1994),('Wilson',1989),('Peak Performance',2018),('Armada',None),('Louisville Slugger',None)]),
('Gildan Activewear',G,W+'Gildan_Activewear','Value & basics',[('Gildan',None),('American Apparel',2017),('Comfort Colors',2015),('Anvil',2012),('Hanes',2025),('Playtex',2025),('Bali',2025),("L'eggs",2025),('Just My Size',2025),('Barely There',2025),('Wonderbra',2025),('Maidenform',2025),('Berlei',2025),('Bonds',2025)]),
('Authentic Brands Group',G,W+'Authentic_Brands_Group','Heritage & workwear',[('Aéropostale',2016),('Airwalk',2014),('Arrow',2021),('Billabong',2023),('Brooks Brothers',2020),('Champion',2024),('Dockers',None),('Eddie Bauer',2021),('Forever 21',2020),('Frederick\'s of Hollywood',2015),('Izod',2021),('Juicy Couture',2013),('Lucky Brand',2020),('Nautica',2018),('Nine West',2018),('Quiksilver',2023),('Reebok',2022),('Roxy',2023),('RVCA',2023),('Spyder',2013),('Ted Baker',2022),('Tretorn',2015),('Van Heusen',2021),('Volcom',2019),('Vince Camuto',2018),('Hervé Léger',2017),('Hickey Freeman',2012),('Hart Schaffner Marx',2012),('Greg Norman',2017),('Tapout',2010),('Jones New York',2015),('Frye',2017),('Guess',2026),('Sperry',2024),('DC Shoes',2023)]),
('WHP Global',G,W+'WHP_Global','High street',[('Joseph Abboud',2020),('Bonobos',2023),('Rag & Bone',2024),('Vera Wang',2024),('Lotto',None),('G-Star RAW',None),("Joe's Jeans",None),('Marc Jacobs',None),('Express',None),('Anne Klein',None),('Isaac Mizrahi',None),('Warner\'s',None)]),
('Marquee Brands',G,W+'Marquee_Brands','High street',[('Bruno Magli',2015),('Ben Sherman',2015),('BCBGMAXAZRIA',2017)]),
('Aditya Birla Fashion and Retail',I,W+'Aditya_Birla_Fashion_and_Retail','High street',[('Louis Philippe',None),('Allen Solly',None),('Peter England',None),('Pantaloons',2015),('Sabyasachi',2021),('Jaypore',2019),('Shantanu & Nikhil',2019),('House of Masaba',2022),('Tarun Tahiliani',2021)]),
('Reliance Retail',I,W+'Reliance_Retail','High street',[('Trends',None),('AJIO',None),('Yousta',None),('Azorte',None),('Zivame',2021)]),
('Shein',G,W+'Shein','Value & basics',[('Shein',None),('Romwe',2014),('Missguided',None),('SHEGLAM',None)]),
('Associated British Foods',N,W+'Primark','Value & basics',[('Primark',None),('Penneys',None)]),
('Next plc',N,W+'Next_plc','High street',[('Next',None),('Lipsy',2008),('Joules',2022),('Cath Kidston',2023),('FatFace',None),('Reiss',None),('Seraphine',None)]),
('Marks & Spencer',N,W+'Marks_%26_Spencer','High street',[('Marks & Spencer',None),('Per Una',2004),('Jaeger',2021),('Autograph',None),('Blue Harbour',None)]),
('Tendam',I,W+'Tendam','High street',[("Women'secret",None),('Springfield',None),('Cortefiel',None),('Pedro del Hierro',None),('Hoss Intropia',None),('Milano',None)]),
('LPP',I,W+'LPP_(company)','High street',[('Reserved',None),('Cropp',None),('House',2009),('Mohito',2009),('Sinsay',None)]),
('Bestseller',I,W+'Bestseller_(company)','High street',[('Jack & Jones',None),('Vero Moda',None),('Only',None),('Selected',None),('Name It',None),('Pieces',None),('Vila',None),('Y.A.S',None),('Object',None)]),
('Boohoo Group',I,W+'Boohoo_Group','Value & basics',[('Boohoo',None),('PrettyLittleThing',None),('Nasty Gal',None),('Karen Millen',2019),('Coast',2019),('Oasis',2020),('Warehouse',2020),('Debenhams',2021),('Burton',2021),('Wallis',2021),('Dorothy Perkins',2021)]),
('ASOS',I,W+'ASOS_plc','High street',[('Topshop',2021),('Topman',2021),('Miss Selfridge',2021),('HIIT',2021)]),
('Aritzia',I,W+'Aritzia','Contemporary & premium',[('Aritzia',None),('Wilfred',None),('Babaton',None),('TNA',None),('Reigning Champ',2021)]),
('lululemon athletica',I,W+'Lululemon_Athletica','Athletic & sportswear',[('Lululemon',None)]),
('American Eagle Outfitters',I,W+'American_Eagle_Outfitters','High street',[('American Eagle',None),('Aerie',None),('Todd Snyder',2015)]),
('Abercrombie & Fitch Co.',I,W+'Abercrombie_%26_Fitch','High street',[('Abercrombie & Fitch',None),('Hollister',None),('Gilly Hicks',None)]),
('Urban Outfitters, Inc.',I,W+'Urban_Outfitters','High street',[('Urban Outfitters',None),('Anthropologie',None),('Free People',None),('BHLDN',None)]),
('Pentland Group',I,W+'Pentland_Group','Athletic & sportswear',[('Speedo',2020),('Endura',2018),('Berghaus',None),('Mitre',None),('Canterbury of New Zealand',None),('Ellesse',None),('Boxfresh',None),('Red or Dead',None),('KangaRoos',None)]),
('Sanyo Shokai',I,W+'Sanyo_Shokai','Contemporary & premium',[('Mackintosh Philosophy',None),('Paul Stuart',None),('Epoca',None),('Mackintosh London',2015)]),
('Itochu',I,W+'Itochu','Japanese & denim',[('Edwin',None)]),
('Mr Price Group',N,W+'Mr_Price_Group','Value & basics',[('Mr Price',None),('Miladys',None),('Power Fashion',2021)]),
('Cotton On Group',I,W+'Cotton_On_Group','High street',[('Cotton On',None),('Typo',None),('Rubi',None),('Factorie',None),('Supré',2013)]),
('LC Waikiki',I,W+'LC_Waikiki','Value & basics',[('LC Waikiki',None)]),
('Landmark Group',I,W+'Max_Fashion','Value & basics',[('Max Fashion',None)]),
('Bosideng International',N,W+'Bosideng','Outdoor & technical',[('Bosideng',None),('Snow Flying',None),('Kangbo',None),('Bengen',None)]),
('Ralph Lauren Corporation',I,W+'Ralph_Lauren_Corporation','Contemporary & premium',[('Ralph Lauren',None),('Polo Ralph Lauren',None),('Double RL',None),('Chaps',None),('Lauren Ralph Lauren',None)]),
('Hugo Boss',I,W+'Hugo_Boss','Contemporary & premium',[('Hugo Boss',None),('Boss',None),('Hugo',None)]),
('Burberry Group',I,W+'Burberry','Luxury house',[('Burberry',None)]),
]
R=json.load(open('../../out/A1_brands.json'))['b']
idx={x['n'].lower():x['n'] for x in R}
bu={};new=[];nm=[];cnt={}
for own,tier,src,seg,bl in D:
    c=0
    for b,y in bl:
        e={'own':own,'tier':tier}
        if y: e['own_y']=y
        k=idx.get(b.lower())
        if k:
            if k in bu: continue
            bu[k]=e;c+=1
        else:
            if any(n['n'].lower()==b.lower() for n in new): continue
            ne={'n':b,'seg':seg,'rel':[],'kf':'','s':src}; ne.update(e); new.append(ne);c+=1
    cnt[own]=c
M=lambda mkt,who,share,yr,s,note:{"mkt":mkt,"who":who,"share":share,"yr":yr,"s":s,"note":note}
UK=W
glob='https://www.globaldata.com/media/retail/shein-adidas-record-biggest-gains-in-uk-apparel-market-share-in-2025-estimates-globaldata/'
ms_tops=[M('UK apparel',a,b,2025,glob,'GlobalData estimate, share of UK apparel market') for a,b in [('Primark','6.0 %'),('Marks & Spencer','4.2 %'),('Next','3.8 %'),('Nike','3.6 %'),('Shein','3.5 %'),('Adidas','3.1 %'),('George (Asda)','2.8 %'),('Zara','2.6 %'),('F&F (Tesco)','2.3 %'),('TU (Sainsbury\'s)','1.6 %')]]
ms_tops+=[M('China sportswear',a,b,None,'https://epaper.chinadaily.com.cn/a/202504/02/WS67ec864fa3101d7a97b6b2c6.html','Euromonitor figure quoted by China Daily, April 2025; the article states no year') for a,b in [('Anta Sports','23 %'),('Nike','20.7 %'),('Li-Ning','9.4 %'),('Adidas','8.7 %')]]
ms_tops.append(M('US fast fashion','Shein','28 %',2022,W+'Shein','Share claimed by Shein, April 2022'))
rev=[('Inditex group brands (Zara etc.)',None)]
revs=[('Kering','EUR 14.67 billion',2025,'Kering'),('Fast Retailing','JPY 2,130 billion',2018,'Fast_Retailing'),('Gap Inc.','USD 15.4 billion',2025,'Gap_Inc.'),('PVH Corp.','USD 8.95 billion',2025,'PVH_(company)'),('Tapestry, Inc.','USD 7.01 billion',2025,'Tapestry,_Inc.'),('Capri Holdings','USD 5.17 billion',2024,'Capri_Holdings'),('VF Corporation','USD 10.45 billion',2024,'VF_Corporation'),('Levi Strauss & Co.','USD 6.28 billion',2025,'Levi_Strauss_%26_Co.'),('Prada Group','EUR 5.431 billion',2024,'Prada'),('Moncler Group','EUR 3.13 billion',2025,'Moncler'),('Hugo Boss','EUR 4,270 million',2025,'Hugo_Boss'),('Ralph Lauren Corporation','USD 8.1145 billion',2026,'Ralph_Lauren_Corporation'),('Burberry Group','GBP 2,420 million',2026,'Burberry'),('Nike, Inc.','USD 46.3 billion',2025,'Nike,_Inc.'),('Adidas AG','EUR 23.683 billion',2024,'Adidas'),('Puma SE','EUR 8.601 billion',2023,'Puma_(brand)'),('Under Armour, Inc.','USD 5.164 billion',2025,'Under_Armour'),('Anta Sports','USD 7.7 billion',2021,'Anta_Sports'),('Li-Ning Company','CNY 29,598 million',2025,'Li-Ning'),('Amer Sports','USD 5.18 billion',2024,'Amer_Sports'),('Gildan Activewear','USD 3.27 billion',2024,'Gildan_Activewear'),('Shein','USD 38 billion',2024,'Shein'),('Associated British Foods (Primark)','GBP 9,489 million',2025,'Primark'),('Next plc','GBP 6,901.3 million',2026,'Next_plc'),('Marks & Spencer','GBP 17,273.6 million (whole group)',2026,'Marks_%26_Spencer'),('LPP','USD 4.58 billion',2025,'LPP_(company)'),('Aritzia','CAD 2.20 billion',2022,'Aritzia'),('lululemon athletica','USD 11.1 billion',2025,'Lululemon_Athletica'),('American Eagle Outfitters','USD 5.261 billion',2023,'American_Eagle_Outfitters'),('Abercrombie & Fitch Co.','USD 5.27 billion',2025,'Abercrombie_%26_Fitch'),('Urban Outfitters, Inc.','USD 3.9 billion',2019,'Urban_Outfitters'),('Reliance Retail','INR 330,870 crore (all retail)',2025,'Reliance_Retail'),('Aditya Birla Fashion and Retail','INR 8,177 crore',2026,'Aditya_Birla_Fashion_and_Retail'),('Mr Price Group','ZAR 40.93 billion',2025,'Mr_Price_Group'),('Cotton On Group','AUD 4.2 billion',2023,'Cotton_On_Group'),('LC Waikiki','USD 4.92 billion',2024,'LC_Waikiki'),('E-Land Group','KRW 4.592 trillion',2023,'E-Land_Group'),('H&M Group','SEK 228 billion',2025,'H%26M')]
for who,v,y,p in revs: ms_tops.append(M('Global apparel group revenue',who,'',y,W+p,'Revenue, not share: '+v))
ms_tops.append(M('Global apparel group revenue','Hanesbrands','',2024,W+'Hanesbrands','Revenue, not share: USD 3.51 billion; Champion sold to Authentic Brands 2024'))
# swap Hanesbrands to intimates
hb=ms_tops.pop()
coats=[M('China down clothing','Bosideng, Snow Flying, Kangbo and Bengen combined','36.7 %',2010,W+'Bosideng','Sales share in the PRC per the China Industrial Information Issuing Center')]
for m in ms_tops+[hb]:
    if m['share']=='' : m['share']='n/a'
for m in coats: pass
ms={'Tops':ms_tops,'Coats & jackets':coats,'Underwear, nightwear & swim':[hb]}
json.dump({'replaces':[],'depts':[],'brand_updates':bu,'brands':new,'dept_ms':ms},open('../../out/A1_parts/BRANDS.json','w'),ensure_ascii=False,indent=1)
json.dump({'cnt':cnt,'bu':len(bu),'new':len(new)},open('stats.json','w'))
print(cnt,len(bu),len(new))
