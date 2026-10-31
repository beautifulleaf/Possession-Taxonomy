# brand data from fetched pages. tuples: (name, dept, own, own_y, cty, desc, srckey)
U={
'PG':'https://en.wikipedia.org/wiki/List_of_Procter_%26_Gamble_brands',
'UNI':'https://en.wikipedia.org/wiki/List_of_Unilever_brands',
'LOR':'https://en.wikipedia.org/wiki/L%27Or%C3%A9al',
'CP':'https://en.wikipedia.org/wiki/Colgate-Palmolive',
'HAL':'https://en.wikipedia.org/wiki/Haleon',
'KEN':'https://en.wikipedia.org/wiki/Kenvue',
'BEI':'https://en.wikipedia.org/wiki/Beiersdorf',
'HEN':'https://en.wikipedia.org/wiki/Henkel',
'EDG':'https://en.wikipedia.org/wiki/Edgewell_Personal_Care',
'KAO':'https://en.wikipedia.org/wiki/Kao_Corporation',
'LION':'https://lion.co.jp/en/products/category/oral/11',
'CD':'https://en.wikipedia.org/wiki/Church_%26_Dwight',
'TP':'https://en.wikipedia.org/wiki/List_of_toothpaste_brands',
'CSH':'https://en.wikipedia.org/wiki/Category:Shampoo_brands',
'CSO':'https://en.wikipedia.org/wiki/Category:Soap_brands',
'HUL':'https://en.wikipedia.org/wiki/Hindustan_Unilever',
'MAR':'https://en.wikipedia.org/wiki/Marico',
'DAB':'https://en.wikipedia.org/wiki/Dabur',
'MAN':'https://en.wikipedia.org/wiki/Mandom',
'NAT':'https://en.wikipedia.org/wiki/Natura_%26Co',
'YB':'https://en.wikipedia.org/wiki/Yunnan_Baiyao',
'BM':'https://www.beautymatter.com/articles/mens-grooming-disruption-and-consolidation-snapshot',
'SEC':'https://www.sec.gov/Archives/edgar/data/21665/000115752324000119/a53887925ex99.htm',
'SON':'https://en.wikipedia.org/wiki/Sonicare',
}
PGn='Procter & Gamble'; UNn='Unilever'; LOn='L\'Oréal'; CPn='Colgate-Palmolive'; HAn='Haleon'; KEn='Kenvue'; BEn='Beiersdorf'; HEn='Henkel'; EDn='Edgewell Personal Care'; KAn='Kao Corporation'; LIn='Lion Corporation'; CDn='Church & Dwight'; HULn='Hindustan Unilever'
GROUPS=[PGn,UNn,LOn,CPn,HAn,KEn,BEn,HEn,EDn,KAn,LIn,CDn]
B=[]
def a(dept,own,src,names,y=None,cty='',d=None):
    for n in names:
        if isinstance(n,tuple): nm,yy,dd=(n+(None,None))[:3]
        else: nm,yy,dd=n,None,None
        B.append(dict(n=nm,dept=dept,own=own,own_y=yy or '',cty=cty,d=dd,src=src))
# HAIR
a('H',PGn,'PG',['Aussie','Frederic Fekkai','Head & Shoulders','Herbal Essences','Mielle','Nicky Clarke',('Pantene','1985'),('Vidal Sassoon','1984'),'Ascend'])
a('H',UNn,'UNI',['AHC','Clear','Clinic','Cream Silk','Indulekha','Linic','Living Proof','Love Beauty & Planet','Organics','Pinuk','Shea Moisture','Sunsilk','Thermasilk','TRESemmé','VO5','Vibrance','Vitakeratin','K18','Suave'])
a('H',HULn,'HUL',['TIGI','Brylcreem'])
a('H',LOn,'LOR',['Dark and Lovely','Garnier','L\'Oréal Paris','Niely','Biolage','Carol\'s Daughter','Kérastase','L\'Oréal Professionnel','Matrix','Mizani','PulpRiot','Pureology','Redken','Shu Uemura Art of Hair','Color Wow'])
a('H',HEn,'HEN',[('Schwarzkopf','1995'),'Syoss','Alterna','Authentic Beauty Concept',('Joico','2017'),'Kenra','Pravana','Sexy Hair',('DevaCurl','2019'),('Zotos','2017'),'Breck'],cty='')
a('H',KAn,'KAO',[('John Frieda','2002'),('Goldwell','1989'),'Guhl','KMS','Oribe','Liese','Merit','Segreta','Success'])
a('H',KEn,'KEN',['Rogaine'])
a('H',CDn,'CD',['Batiste',('Toppik','2016')])
a('H','Marico','MAR',[('Parachute','1974'),('Hair & Care','1991'),'Livon',('Set Wet','2012')],cty='India')
a('H','Mandom','MAN',[('Gatsby','1976'),'Lucido'],cty='Japan')
# SHAVING
a('S',PGn,'PG',['Gillette','Braun','Old Spice'])
a('S',EDn,'EDG',['Schick','Wilkinson Sword','Personna','Edge','Skintimate',('Billie','2021'),('Cremo','2020'),('Jack Black','2018'),'Bull Dog'])
a('S',UNn,'UNI',['Williams'])
a('S',CPn,'CP',['Mennen','Skin Bracer','Afta Lotion'])
a('S',CDn,'CD',[('Nair','2001')])
a('S','Harry\'s','EDG',['Harry\'s'])
# ORAL
a('O',CPn,'CP',['Colgate','Colodent','Darlie','Dentagard','Duraphat',('Elmex','2003'),'Meridol','Kolynos','Profidén','Ultra Brite','Cibaca',('Tom\'s of Maine','2006'),('Hello Products','2020'),'Peak'])
a('O',HAn,'HAL',['Aquafresh','Astring-o-Sol','Biotene','Chlorhexamed','Corega','Corsodyl','Dr. Best','Macleans','Odol','Odol-med3','Parodontax','Polident','Poligrip Ultra','Sensodyne','Shumitect','Super Poligrip','Super Wernet\'s','Synthol'])
a('O',PGn,'PG',['Crest','Oral-B','Scope','Fixodent','Gleem'])
a('O',UNn,'UNI',['Close-Up','Fluocaril','Mentadent','Pepsodent','Prodent','Regenerate','Signal','SR','Zendium','Zhonghua'])
a('O',CDn,'CD',[('Aim','2003'),('Spinbrush','2005'),('Orajel','2008'),('Waterpik','2017'),('TheraBreath','2021')])
a('O',KEn,'KEN',['Listerine'])
a('O',LIn,'LION',['Lion','Clinica','Systema','Nonio','Lion Kodomo','Och-Tune','Dent Health','Migacot','Between','Magic Toothbrush'],cty='Japan')
# BATH
a('B',PGn,'PG',['Always','Tampax','Whisper','Fresco','Ivory','Native','Secret','Olay','Pampers','Luvs'])
a('B',UNn,'UNI',['Badedas','Baby Dove','Camay','Gessy','Good Morning','Lever 2000','Lifebuoy','Liril','Lux','Mist','Pears','Radox','St Ives','Vinólia','Axe','Rexona','Schmidt\'s Naturals','Wild','Dove','Dove Men+Care','Dove Spa','Citra','Zwitsal'])
a('B',HULn,'HUL',['Hamam'])
a('B',CPn,'CP',['Palmolive','Protex','Irish Spring','Softsoap','Sanex','Speed Stick','Soft As Soap','Pousse Mousse'])
a('B',KEn,'KEN',['Johnson\'s Baby','Le Petit Marseillais','Carefree'])
a('B',BEn,'BEI',['Nivea','8x4','Florena'],cty='Germany')
a('B',HEn,'HEN',[('Dial','2004'),'Fa'])
a('B',KAn,'KAO',[('Jergens','1988'),('Molton Brown','2005'),'Ban','Laurier','Merries'])
a('B',CDn,'CD',[('Arrid','2001'),('Touchland','2025')])
a('B',EDn,'EDG',['Wet Ones'])
a('B','Natura &Co','NAT',['Natura'],cty='Brazil')
# independents / owner stated by toothpaste list
TPI=[('Babool','Dabur','India','2005'),('Meswak','Dabur','India','2005'),('Promise','Dabur','India','2005'),('Binaca','Dabur','India',''),('Bentodent','Indian Dental Organization','India',''),
('Dant Kanti','Patanjali Ayurved','India',''),('Formula','PT Ultra Prima Abadi','Indonesia',''),('Hapee','Lamoiyan Corporation','Philippines',''),('KIN','Laboratorios KIN','Spain',''),
('Maxam','Shanghai MAXAM Company Limited','China',''),('Oxygenol','Berner Oy','Finland',''),('Pomorin','Rubella','Bulgaria',''),('BlueM','','Netherlands',''),('BioRepair','','Italy',''),
('Cedel','Heritage Brands','Australia',''),('Grants of Australia','','Australia',''),('White Glo','','Australia',''),('Cleure','Cleure','United States',''),('Jāsön','Hain Celestial','',''),
('Euthymol','Johnson & Johnson','',''),('Ipana','Maxill Inc.','',''),('Stomatol','','Sweden',''),('TartarEnd','','',''),('White Birch','Total Clean LLC','',''),('Rembrandt','','',''),('R.O.C.S.','','',''),('GUM','Sunstar','',''),('P/S','','Vietnam',''),('Davids Natural Toothpaste','','','')]
for n,o,c,y in TPI:
    B.append(dict(n=n,dept='O',own=o,own_y=y,cty=c,d=None,src='TP',indep=True))
B.append(dict(n='Yunnan Baiyao toothpaste',dept='O',own='Yunnan Baiyao',own_y='',cty='China',d='Toothpaste from the Chinese herbal-medicine maker Yunnan Baiyao; fifth by sales revenue in China in 2008 per its Wikipedia page.',src='YB',indep=True))
# owner-not-stated lists
SH=['Alpecin','Bawang Shampoo','Cécred','Diva By Cindy','Gee, Your Hair Smells Terrific','Mane \'n Tail','Meril','Pert Plus','Prell','Psssssst','Salon Selectives','Timotei','Vosene','Wen Hair Care','White Rain','AG Hair']
for n in SH: B.append(dict(n=n,dept='H',own='',own_y='',cty='',d=None,src='CSH'))
SO=['Ach. Brito','Biechele Soap','Bradford Soap','Caswell-Massey','Champion Brothers','Coast','Cuticura','Defense Soap','Fels-Naptha','Fenjal','Heno de Pravia','Imperial Leather','Lano','Lava','Los Angeles Soap Co.','Rozalex','Safeguard','Sapolio','Savlon','Schwab\'s Nature','Sebamed','Shower Shock','Swan Soap','Swarfega','Tabac','Wright\'s Coal Tar Soap','Zest','Zote','Faso soap','L\'Amande','Kohinoor Chemical Company (Bangladesh)']
for n in SO: B.append(dict(n=n,dept='B',own='',own_y='',cty='Bangladesh' if 'Bangladesh' in n else '',d=None,src='CSO'))
B.append(dict(n='Proraso',dept='S',own='',own_y='',cty='',d=None,src='CSO'))
B.append(dict(n='Dollar Shave Club',dept='S',own='',own_y='',cty='United States',d='Direct-to-consumer razor club; 8.5% of the US razor-blade market in 2018 and 16% of cartridge share in 2016 per Beautymatter.',src='BM'))
TIER_GLOBAL=set(GROUPS+[HULn])

# ---- round 2 additions ----
U.update({
'PGUS':'https://us.pg.com/brands/','PGARS':'https://www.sec.gov/Archives/edgar/data/0000080424/000119312526372220/pg_ars_2026.pdf',
'CPOWN':'https://www.colgatepalmolive.com/en-us/brands','EDOWN':'https://edgewell.com/pages/our-brands','KENOWN':'https://www.kenvue.com/brands',
'HALOWN':'https://www.haleon.com/our-brands','HALF':'https://www.haleon.com/who-we-are/facts-and-figures','BEIOWN':'https://www.beiersdorf.com/brands','BEIOTH':'https://www.beiersdorf.com/brands/other-iconic-brands',
'LOROWN':'https://www.loreal.com/en/our-global-brands-portfolio/','UNICAT':'https://en.wikipedia.org/wiki/Category:Unilever_brands','PGCAT':'https://en.wikipedia.org/wiki/Category:Procter_%26_Gamble_brands',
'CPCAT':'https://en.wikipedia.org/wiki/Category:Colgate-Palmolive_brands','HALCAT':'https://en.wikipedia.org/wiki/Category:Haleon_brands','LG':'https://en.wikipedia.org/wiki/LG_Household_%26_Health_Care',
'GOL':'https://en.wikipedia.org/wiki/Golrang_Industrial_Group','BID':'https://en.wikipedia.org/wiki/Bidco_Africa','PZ':'https://en.wikipedia.org/wiki/PZ_Cussons','MGC':'https://mygreencloset.com/small-batch-beauty-brands/',
'GD':'https://www.globaldata.com/store/?p=2597555','RP':'https://www.reportprime.com/electric-toothbrush-r2919/company','PHIL':'https://en.wikipedia.org/wiki/Philishave','ELS':'https://en.wikipedia.org/wiki/Electric_shaver'})
SRC_OVR={}  # (dept,name)->src key
def ov(dept,src,names):
    for n in names: SRC_OVR[(dept,n.lower())]=src
ov('H','PGUS',['Aussie','Head & Shoulders','Herbal Essences','Pantene'])
ov('S','PGUS',['Gillette','Braun','Old Spice'])
ov('O','PGUS',['Crest','Oral-B','Scope','Fixodent'])
ov('B','PGUS',['Always','Tampax','Ivory','Native','Secret','Olay','Pampers','Luvs'])
ov('O','CPOWN',['Colgate','Tom\'s of Maine','Elmex','Meridol'])
ov('B','CPOWN',['Palmolive','Protex','Irish Spring','Softsoap','Sanex','Speed Stick'])
ov('S','EDOWN',['Schick','Wilkinson Sword','Edge','Skintimate','Billie','Cremo','Jack Black'])
ov('O','KENOWN',['Listerine']); ov('B','KENOWN',['Johnson\'s Baby'])
ov('O','HALOWN',['Sensodyne','Polident','Parodontax'])
ov('B','BEIOWN',['Nivea']); ov('B','BEIOTH',['8x4'])
ov('H','LOROWN',['Biolage','Color Wow','Kérastase','L\'Oréal Professionnel','Matrix','Mizani','PulpRiot','Pureology','Redken','Shu Uemura Art of Hair','Garnier','L\'Oréal Paris','Dark and Lovely'])
a('H',PGn,'PGUS',['My Black Is Beautiful'])
a('H',PGn,'PGARS',['Rejoice'])
a('S',PGn,'PGUS',['joy+glee','The Art of Shaving'])
a('S',PGn,'PGARS',['Venus'])
a('B',PGn,'PGUS',['Always Discreet','This is L','Safeguard','Ninjamas'])
a('B',PGn,'PGUS',[])
a('O',CPn,'CPOWN',['Sorriso'])
a('B',CPn,'CPOWN',['Lady Speed Stick','Tahiti'])
a('B',CPn,'CPCAT',['Baby Magic','Soaky','Teen Spirit','Vel Soap'])
a('S',EDn,'EDOWN',['Intuition','Hydro Silk'])
a('H',KEn,'KENOWN',['OGX']); a('B',KEn,'KENOWN',['Neutrogena','Aveeno'])
a('O',HAn,'HALOWN',['Aquafresh'])  # facts page lists Aquafresh
ov('O','HALF',['Aquafresh'])
a('H',BEn,'BEIOTH',['Beiersdorf Hair Care China (Maestro)'],cty='China'); a('B',BEn,'BEIOTH',['D\'Dusch Shower','Hidrofugal'])
a('H',UNn,'UNICAT',['Aqua Net','Salon Selectives','Timotei'])
a('B',UNn,'UNICAT',['Lady\'s Choice','Crisp \'n Dry'])
a('S',UNn,'UNICAT',['Brut'])
# national champions / independents
for n in ['Elastine','Reen']:
    B.append(dict(n=n,dept='H',own='LG Household & Health Care',own_y='',cty='South Korea',d=None,src='LG',tier_o='National champion',g_o='National champions and independents'))
B.append(dict(n='Perioe',dept='O',own='LG Household & Health Care',own_y='',cty='South Korea',d=None,src='LG',tier_o='National champion'))
B.append(dict(n='ON: THE BODY',dept='B',own='LG Household & Health Care',own_y='',cty='South Korea',d=None,src='LG',tier_o='National champion'))
B.append(dict(n='Pakshoo',dept='B',own='Golrang Industrial Group',own_y='',cty='Iran',d='Iranian hygiene, cosmetics and detergent maker, described on Wikipedia as the biggest private-sector maker of its range in Iran.',src='GOL',tier_o='National champion'))
B.append(dict(n='Golrang',dept='B',own='Golrang Industrial Group',own_y='',cty='Iran',d=None,src='GOL'))
for n,y in [('Cowboy',None),('Pure and Natural',None),('Nuru',None),('Gaea',None),('Germonil',None)]:
    B.append(dict(n=n,dept='B',own='Bidco Africa',own_y='2002' if n=='Cowboy' else '',cty='Kenya',d=('Kenyan soap brand that came to Bidco with the 2002 purchase of Unilever\'s Kenyan edible-oil and soap business.' if n=='Cowboy' else None),src='BID'))
OVR={('B','imperial leather'):dict(own='PZ Cussons',src='PZ',d='Soap range that Wikipedia calls PZ Cussons\' main brand; Nigeria is the company\'s largest market.')}
CR=[('The Innate Life','H','Canada','Hair care: shampoo, conditioner, scalp treatment and hair oil.'),('Less is More','H','Austria','Hair care: Neem scalp-relief shampoo and herbal tonic.'),
('Oil + Water','B','United States','New York maker of soaps, face oil, face mist and clay mask.'),('Magic Organic Apothecary','B','United Kingdom','English maker of body oil and multi-purpose balm.'),
('Sḵwálwen Botanicals','B','Canada','Hand-made cleansing bar and facial serums, made in small batches.'),('Pure Skin Food','B','Austria','Body and face care products.'),('Meow Meow Tweet','B','','Baking-soda-free deodorant.')]
for n,dp,c,d in CR:
    B.append(dict(n=n,dept=dp,own=n,own_y='',cty=c,d=d,src='MGC',tier_o='Craft & indie',g_o='Craft and indie'))
# L'Oréal Carol's Daughter sold
OVR[('H',"carol's daughter")]=dict(own='',d='Hair-care brand L\'Oréal acquired in 2014 and sold in March 2025, per Wikipedia; no current owner on a fetched page.',src='LOR')
B.sort(key=lambda b: 0 if b['own'] else 1)
for b in B:
    k=(b['dept'],b['n'].lower())
    if k in SRC_OVR: b['src']=SRC_OVR[k]
    if k in OVR: b.update(OVR[k])
TIER_GLOBAL=set(GROUPS+[HULn])
DEV_OWN2={'braun':(PGn,''),'oral-b':(PGn,''),'waterpik':(CDn,'2017'),'philips sonicare':('Philips',''),'sonicare':('Philips',''),'philips':('Philips',''),'philishave':('Philips',''),'gillette':(PGn,''),
 'wahl':('Wahl',''),'remington':('Remington Products',''),'panasonic':('Panasonic',''),'dyson':('Dyson',''),'homedics':('HoMedics',''),'therabody':('Therabody',''),'schick':(EDn,''),'oster':('Oster',''),'andis':('Andis',''),'babyliss':('BaByliss',''),'conair':('Conair','')}
