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
('OTB Group',G,W+'OTB_Group','Designer',[('Diesel',None),('Maison Margiela',2002),('Viktor & Rolf',2008),('Marni',2012),('Amiri',2019),('Jil Sander',2021)]),
('Nike, Inc.',G,W+'Nike,_Inc.','Athletic & sportswear',[('Nike',None),('Converse',2003)]),
('Adidas AG',G,W+'Adidas','Athletic & sportswear',[('Adidas',None),('Five Ten',2011)]),
('Puma SE',G,W+'Puma_(brand)','Athletic & sportswear',[('Puma',None),('Cobra Golf',2010)]),
('Under Armour, Inc.',G,W+'Under_Armour','Athletic & sportswear',[('Under Armour',None)]),
('Anta Sports',G,W+'Anta_Sports','Athletic & sportswear',[('Anta',None),('Fila',2009),('Descente',None),('Kolon Sport',2017),('Jack Wolfskin',None)]),
('Li-Ning Company',N,W+'Li-Ning','Athletic & sportswear',[('Li-Ning',None)]),
('Amer Sports',G,W+'Amer_Sports','Outdoor & technical',[("Arc'teryx",None),('Salomon',2005),('Atomic',1994),('Wilson',1989),('Peak Performance',2018),('Armada',None),('Louisville Slugger',None)]),
('Gildan Activewear',G,W+'Gildan_Activewear','Value & basics',[('Gildan',None),('American Apparel',2017),('Comfort Colors',2015),('Anvil',2012)]),
('Hanesbrands',G,W+'Hanesbrands','Value & basics',[('Hanes',None),('Playtex',None),('Bali',None),("L'eggs",None),('Just My Size',None),('Barely There',None),('Wonderbra',None),('Maidenform',None),('Berlei',None),('Bonds',None)]),
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
('Punto Fa (Mango)',I,W+'Mango_(retailer)','High street',[('Mango',None),('Violeta by Mango',None)]),
('Trent',I,W+'Trent_Limited','Value & basics',[('Westside',None),('Zudio',None),('Utsa',None),('Samoh',None)]),
('Lojas Renner',N,W+'Lojas_Renner','High street',[('Renner',None),('Youcom',None),('Ashua',None)]),
('Arvind Limited',I,W+'Arvind_(company)','Heritage & workwear',[('Flying Machine',None),('Newport',None),('Ruf & Tuf',None),('Ruggers',None),('True Blue',None)]),
('Benetton Group',I,W+'Benetton_Group','High street',[('United Colors of Benetton',None),('Sisley',None)]),
('Oniverse',I,W+'Oniverse','High street',[('Calzedonia',None),('Intimissimi',None),('Tezenis',None),('Falconeri',None),('Atelier Emé',None),('Antonio Marras',None)]),
('Max Mara Fashion Group',I,W+'Max_Mara','Designer',[('Max Mara',None),('Sportmax',None),('Weekend Max Mara',None),('Marella',None),('Pennyblack',None),('iBlues',None),('MAX&Co.',None),('Marina Rinaldi',None)]),
('Esprit Holdings',I,W+'Esprit_Holdings','High street',[('Esprit',None)]),
('s.Oliver Group',I,W+'S.Oliver','High street',[('s.Oliver',None),('Knockout',None),('comma',2001),('QS by s.Oliver',None)]),
('Cofra Holding (Brenninkmeijer family)',I,W+'C&A','High street',[('C&A',None),('Clockhouse',None),('Palomino',None),('Yessica',None),('Angelo Litrico',None),('Westbury',None)]),
('Zalando',I,'https://www.fairwear.org/brands/zalando-se','High street',[('Anna Field',None),('Even&Odd',None),('Zign',None),('Pier One',None),('Yourturn',None),('Friboo',None)]),
('Ryohin Keikaku',I,W+'Muji','Value & basics',[('Muji',None)]),
('Canada Goose Holdings',I,W+'Canada_Goose_Inc.','Outdoor & technical',[('Canada Goose',None),('Baffin',2018)]),
('Columbia Sportswear',G,W+'Columbia_Sportswear','Outdoor & technical',[('Columbia',None),('Sorel',2000),('Mountain Hardwear',2003),('Prana',2014),('Montrail',2006),('Pacific Trail',2006)]),
('Patagonia Purpose Trust',I,W+'Patagonia,_Inc.','Outdoor & technical',[('Patagonia',2022)]),
('HLA Group',I,W+'HLA_Group','High street',[('Heilan Home',None),('HLA',None),('EICHITOO',None),('BETTSALE',None),('SANCANAL',None)]),
('Samsung C&T',I,W+'Samsung_C%26T_Corporation','Contemporary & premium',[('Beanpole',None),('Galaxy',None),('Rogatis',None),('Juun.J',None),('Kuho',None),('8 Seconds',None)]),
('Gloria Jeans',N,W+'Gloria_Jeans','High street',[('Gloria Jeans',None),('Gee Jay',None)]),
('Koton',I,W+'Koton_(company)','High street',[('Koton',None)]),
('Mavi',I,W+'Mavi_Jeans','Japanese & denim',[('Mavi',None)]),
('Woolworths Holdings',I,W+'Country_Road_Group','High street',[('Country Road',2014),('Witchery',2012),('Mimco',2012),('Trenery',None),('Politix',2016)]),
('Pepkor',N,W+'Pepkor','Value & basics',[('PEP',None),('Ackermans',None),('Legit',2025),('Style',2025),('Best & Less',None)]),
('Lindex Group',I,W+'Lindex','High street',[('Lindex',None)]),
('Association Familiale Mulliez',I,W+'Association_Familiale_Mulliez','High street',[('Kiabi',None),('Brice',None),('Jules',None)]),
('El Puerto de Liverpool',I,W+'El_Puerto_de_Liverpool','High street',[('Suburbia',2016)]),
('Soma (Azzas 2154)',N,W+'Cia._Hering','High street',[('Hering',None),('Dzarm',None),('Reserva',None)]),
('Shimamura',N,'https://cdn.gltjp.com/en/article/item/21284/','High street',[('Fashion Center Shimamura',None),('Avail',None),('Birthday',None)]),
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
RD={"'47":("New Era",2024),"A Bathing Ape":("I.T Group",None),"Aquascutum":("Shandong Ruyi",None),"Arena":("Descente",1990),"Carhartt":("Carhartt (family-owned)",None),"Chantelle":("Chantelle (family-owned)",None),"DAKS":("Sankyo Seiko",1991),"Dale of Norway":("Rossignol",2018),"Falke":("Falke Group (family-owned)",None),"Fjällräven":("Fenix Outdoor",None),"J. Press":("Onward Holdings",1986),"Johnstons of Elgin":("Johnstons of Elgin (family-owned)",None),"Lacoste":("Maus Frères",None),"Mackintosh":("Yagi Tsusho",None),"Nelson Knitting Company":("Fox River Mills",1992),"Original Penguin":("Perry Ellis",None),"Orlebar Brown":("Chanel",2018),"OshKosh B'gosh":("Carter's",None),"Rab":("Equip",None),"Rothco":("Rothco (family-owned)",None),"Schott NYC":("Schott NYC (family-owned)",None),"Shanghai Tang":("Richemont (1998-2017, former)",None),"Spanx":("Blackstone",2021),"Stubbies":("Workwear Group",None),"Thinx":("Kimberly-Clark",2022),"Valley Apparel":("Valley Apparel (independent)",2000),"Wolford":("Fosun",2018)}
bymap={x['n']:x for x in R}
regsrc={}
for k,(o,y) in RD.items():
    if k in bu or k not in bymap: continue
    if k=="Shanghai Tang": continue
    e={'own':o,'tier':I}
    if y and k not in ("Valley Apparel",): e['own_y']=y
    bu[k]=e; regsrc[k]=bymap[k].get('s','')
cnt['register-d (owner stated in the register entry\'s cited page)']=len(regsrc)

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

ms_tops+=[M('Global apparel market',a,b,2024,'https://www.globaldata.com/shein-emerges-biggest-winner-global-apparel-market-2024-says-globaldata/','GlobalData forecast, share of global apparel sales') for a,b in [('Nike','2.85 %'),('Adidas','1.79 %'),('Shein','1.53 %'),('Zara','1.24 %'),('H&M','1.06 %'),('Uniqlo','0.92 %'),('Chanel','0.59 %'),('Hermès','0.55 %'),('Gucci','0.38 %')]]
ms_tops+=[M('US apparel','Nike','4.9 %',2021,'https://www.globaldata.com/store/report/usa-apparel-market-trend-analysis/','GlobalData; followed by Old Navy 1.7 % and Adidas 1.5 %'),M('US apparel','Nike','4.3 %',2022,'https://www.globaldata.com/store/report/usa-apparel-market-trend-analysis/','GlobalData; followed by Adidas 1.6 % and Old Navy 1.4 %'),
 M('US clothing spending','Amazon','17.8 %',2026,'https://www.pymnts.com/?p=4118866','Share of US clothing spending; 15.7 % in 2024, 17.0 % in 2025'),M('US clothing spending','Walmart','6.0 %',2026,'https://www.pymnts.com/?p=4118866','Share of US clothing spending; 6.5 % in 2024, 6.2 % in 2025'),M('US clothing spending',"Macy's",'3.1 %',2026,'https://www.pymnts.com/?p=4118866','Latest estimate, Q1 2026 data; 3.4 % in 2024')]
ms_tops+=[M('Japan apparel','Uniqlo','6.5 %',None,'https://fashionunited.com/news/fashion-statistics-japan/2016082312615','Page states no year (FashionUnited, 2016 article); described as the nation\'s largest apparel retail chain')]
ms_tops+=[M('Japan apparel group revenue',a,'n/a',2016,'https://fashionunited.com/news/fashion-statistics-japan/2016082312615','Annual revenue, not share: '+b) for a,b in [('Fast Retailing','USD 14.4 billion'),('Shimamura Group','USD 4.64 billion'),('Asics','USD 3.90 billion'),('Onward Holdings','USD 2.3 billion'),('United Arrows','USD 1.17 billion')]]
ms_tops+=[M('Brazil apparel','Lojas Renner','7.2 %',2021,'https://www.globaldata.com/store/?p=3341435','GlobalData; 4.7 % in 2016')]
ms_tops+=[M('Germany fashion retail',a,'n/a',2023,'https://fashionunited.de/nachrichten/business/grosste-modehandler-otto-spitzenreiter-h-m-uberholt-zalando/2024121059376','Sales ranking by Textilwirtschaft, not share: '+b) for a,b in [('Otto Group','about EUR 4.5 billion'),('H&M','EUR 3.07 billion'),('Zalando','EUR 3 billion'),('Shein','about EUR 2 billion')]]
ms_tops+=[M('South Africa apparel and footwear',  'Mr Price Group','9 %',2014,'https://fashionunited.com/news/fashion/looking-beyond-the-obvious-in-sub-saharan-africa-part-i/201505297101','Described as South Africa\'s leading apparel and footwear retailer'),
 M('South Africa clothing, top six retailers combined','Six largest retailers','47 %',2012,'https://oxfordbusinessgroup.com/reports/nigeria/2013-report/economy/trend-setters-changes-in-consumer-culture-herald-opportunities-for-local-and-international-fashion-retailers','McKinsey figure quoted by Oxford Business Group'),
 M('Nigeria clothing, top six retailers combined','Six largest retailers','under 2 %',2012,'https://oxfordbusinessgroup.com/reports/nigeria/2013-report/economy/trend-setters-changes-in-consumer-culture-herald-opportunities-for-local-and-international-fashion-retailers','McKinsey figure quoted by Oxford Business Group'),
 M('Egypt clothing, top six retailers combined','Six largest retailers','4 %',2012,'https://oxfordbusinessgroup.com/reports/nigeria/2013-report/economy/trend-setters-changes-in-consumer-culture-herald-opportunities-for-local-and-international-fashion-retailers','McKinsey figure quoted by Oxford Business Group; year taken from the same comparison'),
 M('India apparel group revenue','Trent','n/a',2026,W+'Trent_Limited','Revenue, not share: INR 20,074 crore'),
 M('Global apparel group revenue','Mango (Punto Fa)','n/a',2025,W+'Mango_(retailer)','Revenue, not share: EUR 3.767 billion; EUR 3.339 billion in 2024'),
 M('Global apparel group revenue','Oniverse','n/a',2024,W+'Oniverse','Revenue, not share: EUR 3.527 billion'),
 M('Global apparel group revenue','OTB Group','n/a',2023,W+'OTB_Group','Revenue, not share: EUR 1.9 billion'),
 M('Global apparel group revenue','Canada Goose','n/a',2025,W+'Canada_Goose_Inc.','Revenue, not share: CAD 1.35 billion'),
 M('Global apparel group revenue','Columbia Sportswear','n/a',2025,W+'Columbia_Sportswear','Revenue, not share: USD 3.4 billion'),
 M('Global apparel group revenue','Pepkor','n/a',2025,W+'Pepkor','Revenue, not share: ZAR 95.3 billion; clothing retail about 72 % of it'),
 M('Global apparel group revenue','Gloria Jeans','n/a',2023,W+'Gloria_Jeans','Revenue, not share: RUB 78 billion'),
 M('Global apparel group revenue','Koton','n/a',2023,W+'Koton_(company)','Revenue, not share: USD 660 million'),
 M('Global apparel group revenue','Mavi','n/a',2024,W+'Mavi_Jeans','Revenue, not share: USD 1.11 billion'),
 M('Global apparel group revenue','El Puerto de Liverpool','n/a',2022,W+'El_Puerto_de_Liverpool','Revenue, not share: MXN 176.0 billion (whole group)'),
 M('Global apparel group revenue','Max Mara Fashion Group','n/a',None,W+'Max_Mara','Revenue, not share: EUR 1.2 billion; page gives no year'),
 M('Global apparel group revenue','Lindex','n/a',2023,W+'Lindex','Revenue, not share: EUR 633.1 million'),
 M('Global apparel group revenue','Arvind Limited','n/a',2025,W+'Arvind_(company)','Revenue, not share: INR 8,329 crore'),
 M('Global apparel group revenue','HLA Group','n/a',2015,W+'HLA_Group','Revenue, not share: CNY 12.338 billion')]
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
