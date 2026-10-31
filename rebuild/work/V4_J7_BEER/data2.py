# Entry definitions. B(...) = one named entry; many(...) = a list from a fetched brand page.
from data1 import U
ENT = []
GR, NT, CF = 'Global group', 'National champion', 'Craft & indie'
IN, OLB = 'Independent', 'Own label'

def B(kind, n, own='', cty='', tier='', g='', src='', d='', old=(), v=(), y='', own_y='', role='', a='', style='', alc=''):
    ENT.append(dict(kind=kind, n=n, own=own, cty=cty, tier=tier, g=g, src=src, d=d, old=list(old), v=list(v), y=y,
                    own_y=own_y, role=role, a=a, style=style, alc=alc))

def many(kind, own, tier, src, items, what='beer brand'):
    for it in items:
        n, cty = it[0], it[1]
        oy = it[2] if len(it) > 2 else ''
        d = it[3] if len(it) > 3 else f'{what.capitalize()} from {cty}, listed on the source page under {own}.'
        B(kind, n, own, cty, tier, cty, src, d, own_y=oy)

# ---------------- AB InBev ----------------
A = 'Anheuser-Busch InBev'
B('AB', 'Budweiser', A, 'United States', GR, 'United States', U['AB'], old=['Budweiser'],
  d='American pale lager from St. Louis, the reference for the American lager style; named a global brand by the owner.',
  v=[('Budweiser 66', 'UK, 4% ABV', ''), ('Budweiser Zero', 'Alcohol-free version, 0.00 % ABV as stated by the product page', 'alcohol-free')])
B('AB', 'Bud Light', A, 'United States', GR, 'United States', U['AB'], old=['Bud Light'])
B('AB', 'Michelob Ultra', A, 'United States', GR, 'United States', U['AB'], d='American light lager brand of AB InBev, listed on the portfolio page.')
B('AB', 'Busch', A, 'United States', GR, 'United States', U['AB'])
B('AB', 'Natural Light', A, 'United States', GR, 'United States', U['AB'])
B('AB', 'LandShark', A, 'United States', GR, 'United States', U['AB'])
B('AB', 'Shock Top', A, 'United States', GR, 'United States', U['AB'], d='Belgian-style wheat beer brand of Anheuser-Busch, listed as a global brand.')
B('AB', 'Rolling Rock', A, 'United States', GR, 'United States', U['AB'])
B('AB', 'Goose Island', A, 'United States', GR, 'United States', U['AB'], old=['Bourbon County Brand Stout'],
  d='Chicago craft brewery in the Anheuser-Busch craft-partner group; Bourbon County Brand Stout is its imperial stout.')
B('AB', 'Stella Artois', A, 'Belgium', GR, 'Belgium', U['AB'], own_y='2008', d='Belgian pilsner from Leuven, named a global brand by AB InBev.',
  v=[('Stella Artois 0.0', 'Alcohol-free version, 0.0 % ABV', 'alcohol-free')])
B('AB', "Beck's", A, 'Germany', GR, 'Germany', U['AB'], d='Bremen pilsner in the AB InBev European list.',
  v=[("Beck's Blue", 'Alcohol-free version, 0.05 % ABV', 'alcohol-free')])
B('AB', 'Hoegaarden', A, 'Belgium', GR, 'Belgium', U['AB'], own_y='2008', old=['Hoegaarden'])
B('AB', 'Leffe', A, 'Belgium', GR, 'Belgium', U['AB'], old=['Leffe Blond'])
B('AB', 'Corona', A, 'Mexico', GR, 'Mexico', U['MEX'], old=['Corona Extra'],
  d='Mexican pale lager in a clear bottle from Grupo Modelo, now AB InBev; Constellation Brands holds the US rights.',
  v=[('Corona Cero', 'Alcohol-free version, 0.0 % ABV', 'alcohol-free')])
B('AB', 'Modelo', A, 'Mexico', GR, 'Mexico', U['MEX'], old=['Modelo Especial'],
  d='Pilsner-style Mexican lager from Grupo Modelo; Constellation Brands holds the US rights since 2013.')
B('AB', 'Victoria', A, 'Mexico', GR, 'Mexico', U['MEX'], old=['Victoria'])
many('AB', A, GR, U['MEX'], [('Negra Modelo', 'Mexico'), ('Pacífico', 'Mexico'), ('León', 'Mexico'), ('Montejo', 'Mexico')])
many('AB', A, GR, U['AB'], [
 ('Estrella Jalisco', 'Mexico', '2013'), ('Presidente', 'Dominican Republic', '2012'), ('Bohemia', 'Brazil'), ('Brahma', 'Brazil'),
 ('Skol', 'Brazil'), ('Antarctica', 'Brazil'), ('Quilmes', 'Argentina'), ('Aguila', 'Colombia'), ('Poker', 'Colombia'),
 ('Cusqueña', 'Peru'), ('Pilsener', 'Ecuador'), ('Labatt', 'Canada'), ("Alexander Keith's", 'Canada'), ('Kokanee', 'Canada'),
 ('Franziskaner', 'Germany'), ('Löwenbräu', 'Germany'), ('Hasseröder', 'Germany'), ('Diebels', 'Germany'),
 ('St. Pauli Girl', 'Germany'), ('Haake-Beck', 'Germany'), ('Jupiler', 'Belgium'), ('Belle-Vue', 'Belgium'), ('Bosteels', 'Belgium'),
 ('Boddingtons', 'United Kingdom'), ('Camden Town Brewery', 'United Kingdom'), ('Dommelsch', 'Netherlands'), ('Hertog Jan', 'Netherlands'),
 ('Oranjeboom', 'Netherlands'), ('Diekirch', 'Luxembourg'), ('Mousel', 'Luxembourg'), ('Chernigivske', 'Ukraine'), ('Klinskoye', 'Russia'),
 ('Cass', 'South Korea'), ('OB', 'South Korea'), ('Harbin', 'China'), ('Double Deer', 'China'), ('Sedrin', 'China'),
 ('Haywards 5000', 'India'), ('Elysian', 'United States'), ('Golden Road', 'United States'), ('Karbach', 'United States'),
 ('Devils Backbone', 'United States'), ('Wicked Weed', 'United States'), ('Four Peaks', 'United States'), ('10 Barrel Brewing Co.', 'United States'),
 ('Blue Point Brewing Company', 'United States'), ('Breckenridge Brewery', 'United States')])
B('AB', 'Spaten', A, 'Germany', GR, 'Germany', U['AB'], old=['Spaten Münchner Hell', 'Spaten Ur-Märzen'],
  d='Munich brewery in the AB InBev regional list; Ur-Märzen is its Märzen of 1841 and Münchner Hell its Helles.')
B('AB', 'Foster\'s', A, 'Australia', GR, 'Australia', U['AUS'], own_y='2011', d='Australian lager of the Foster\'s Group, owned by AB InBev since 2011 according to the page.')
B('AB', 'Castle', A, 'South Africa', GR, 'South Africa', U['ZAF'], d='South African Breweries lager, with Castle Lite and Castle Milk Stout in the range; SAB is listed under AB InBev in Africa.',
  v=[('Castle Lager', 'Pale lager, owned by SAB', ''), ('Castle Lite', 'Lighter lager', ''), ('Castle Milk Stout', 'Sweet stout', '')], style='International pale lager')
many('AB', 'South African Breweries', GR, U['ZAF'], [('Carling Black Label', 'South Africa', '', 'SAB\'s most popular and valuable brand according to the page; 20 international awards.'), ('Hansa Pilsner', 'South Africa')])

# ---------------- Heineken ----------------
H = 'Heineken'
B('HE', 'Heineken', H, 'Netherlands', GR, 'Netherlands', U['HE'], old=['Heineken'],
  v=[('Heineken 0.0', 'Alcohol-free version, 0.0 % ABV, launched 2017', 'alcohol-free')], d='Dutch pale lager of 5% ABV, the company flagship, first brewed with the Heineken yeast in 1873.')
B('HE', 'Amstel', H, 'Netherlands', GR, 'Netherlands', U['HE'], own_y='1968', d='Dutch lager brand taken over by Heineken in 1968.', v=[('Amstel Light', 'Light lager', ''), ('Amstel 1870', 'Premium lager', '')])
B('HE', 'Tecate', H, 'Mexico', GR, 'Mexico', U['HE'], own_y='2010', role='landmark', d='Mexican lager named on the page as the group\'s largest brand by volume; Heineken took the FEMSA brewery in 2010.')
many('HE', H, GR, U['MEX'], [('Sol', 'Mexico', '2010'), ('Dos Equis', 'Mexico', '2010'), ('Carta Blanca', 'Mexico', '2010'), ('Superior', 'Mexico', '2010'),
 ('Indio', 'Mexico', '2010'), ('Bohemia (Cuauhtémoc-Moctezuma)', 'Mexico', '2010')])
many('HE', H, GR, U['BRZ'], [('Kaiser', 'Brazil', '2010'), ('Eisenbahn', 'Brazil')])
B('HE', 'Tiger', H, 'Singapore', GR, 'Singapore', U['HE'], y='1932', d='Singaporean lager launched in 1932 by Malayan Breweries, brewed by Asia Pacific Breweries.')
B('HE', 'Żywiec', H, 'Poland', GR, 'Poland', U['HE'], own_y='1995', old=['Żywiec Porter'], d='Polish brewery acquired in the mid-1990s; Żywiec Porter is a Baltic porter.')
B('HE', "Murphy's", H, 'Ireland', GR, 'Ireland', U['HE'], own_y='1983', old=["Murphy's Irish Stout"], d='Cork stout brewery bought by Heineken in 1983; Irish stout and Irish red.')
B('HE', 'Beamish', H, 'Ireland', GR, 'Ireland', U['HE'], own_y='2009', old=['Beamish Irish Stout'], d='Cork stout brewery, part of Heineken since 2009.')
B('HE', 'Birra Moretti', H, 'Italy', GR, 'Italy', U['HE'], own_y='1996', d='Italian lager from Udine, acquired in 1996; includes La Rossa and Doppio Malto.')
B('HE', 'Birra Dreher (Italy)', H, 'Italy', GR, 'Italy', U['HE'], own_y='1974', d='Italian brewery founded in Trieste, acquired in 1974.')
many('HE', H, GR, U['HE'], [
 ('Birra Ichnusa', 'Italy'), ('Affligem', 'Belgium'), ('Athenian Brewery', 'Greece'), ('Alfa Hellenic', 'Greece'), ('Fischer (Greece)', 'Greece'),
 ('Brand', 'Netherlands'), ('Wieckse Witte', 'Netherlands'), ('Botchkarev', 'Russia', '2002'), ('Sagres', 'Portugal', '2008'),
 ('Cruzcampo', 'Spain'), ('Fürstenberg', 'Germany', '2004'), ('Karlovačko', 'Croatia', '2003'), ('Krušovice', 'Czech Republic', '2007'),
 ('Starobrno', 'Czech Republic'), ('Laško', ''), ('Pelforth', 'France', '1988'), ('Fischer Tradition', 'France'), ('Adelscott', 'France'),
 ('Skopsko', 'North Macedonia'), ('Zagorka', 'Bulgaria'), ('Zlatý Bažant', 'Slovakia', '1995'), ('Desperados', 'France'),
 ('Sakara', 'Egypt', '2002'), ('Stella (Egypt)', 'Egypt', '2002'), ('Birell', 'Egypt', '2002'), ('Windhoek Lager (Sedibeng)', 'South Africa'),
 ('DB Draught', 'New Zealand', '2004'), ('Tui', 'New Zealand'), ("Monteith's", 'New Zealand'), ('Reeb', 'China')])
B('HE', 'Buckler', H, 'Netherlands', GR, 'Netherlands', U['HE'], y='1988', d='Low-alcohol lager launched by Heineken in 1988.', alc='low')

# ---------------- China Resources Snow ----------------
B('SN', 'Snow', 'China Resources Snow Breweries', 'China', GR, 'China', U['SN'], role='landmark',
  d='Principal brand of CR Snow; the page says it was the biggest-selling beer in the world by volume in 2010.')
many('SN', 'China Resources Snow Breweries', GR, U['SN'], [(n, 'China') for n in
 ['Blue Sword', 'Green Leaves', 'Huadan', 'Huadan Yate', 'Largo', 'Löwen', 'New Three Star', 'Shengquan', 'Shenyang', 'Singo', 'Sip', 'Tianjin', 'Yatai', 'Yingshi', 'Zero Clock']])

# ---------------- Carlsberg ----------------
C = 'Carlsberg Group'
B('CA', 'Carlsberg', C, 'Denmark', GR, 'Denmark', U['CA'], d='Danish lager and flagship of the group, named after Carl Jacobsen.',
  v=[('Carlsberg 0.0', 'Alcohol-free lager, 0.0 % ABV', 'alcohol-free')])
B('CA', 'Tuborg', C, 'Denmark', GR, 'Denmark', U['CA'], own_y='1970', d='Danish brewery merged with Carlsberg in 1970.')
B('CA', 'Kronenbourg 1664', C, 'France', GR, 'France', U['CA'], own_y='2008', d='French lager from Kronenbourg, acquired through the 2008 Scottish & Newcastle deal.')
B('CA', 'Grimbergen', C, 'Belgium', GR, 'Belgium', U['CA'], d='Belgian abbey beer brand taken over by Carlsberg; Alken-Maes brews it for Belgium.')
B('CA', 'Baltika', 'Baltika Breweries', 'Russia', IN, 'Russia', U['CA'], d='Russian brewery, formerly majority held through Baltic Beverages Holding; Russian authorities seized the shares in July 2023.')
B('CA', 'Okocim', C, 'Poland', GR, 'Poland', U['CA'], own_y='2004', d='Polish brewery under full Carlsberg control since 2004.')
B('CA', 'Aldaris', C, 'Latvia', GR, 'Latvia', U['CA'], own_y='2008', d='Latvian brewery acquired in 2008.')
B('CA', 'Žatecký Pivovar', C, 'Czech Republic', GR, 'Czech Republic', U['CA'], own_y='2014', d='Czech brewery owned since 2014.')
B('CA', 'Marston\'s', 'Carlsberg Marston\'s Brewing Company', 'United Kingdom', GR, 'United Kingdom', U['CA'], own_y='2020',
  d='British brewery whose brands sit in the Carlsberg Marston\'s joint venture, 60% Carlsberg from 2020; Carlsberg bought the other 40% in 2024.',
  old=["Marston's Pedigree"])
B('CA', 'Waterloo Brewing Company', C, 'Canada', GR, 'Canada', U['CA'], own_y='2022', d='Canadian brewery whose acquisition was announced in December 2022.')
B('CA', 'Huda', C, 'Vietnam', GR, 'Vietnam', U['VNM'], d='Vietnamese beer of Carlsberg, which held 9.2% of the Vietnamese market in 2023.')
many('CA', C, GR, U['CA'], [
 ('Holsten', 'Germany'), ('Feldschlösschen', 'Switzerland'), ('Jacobsen', 'Denmark'), ('Karhu', 'Finland'), ('Super Bock', 'Portugal'),
 ('Birrificio Angelo Poretti', 'Italy'), ('Mythos', 'Greece', '2014'), ('Lav', 'Serbia'), ('Pan', 'Croatia'), ('Lvivske', 'Ukraine'),
 ('Slavutych', 'Ukraine'), ('Lao', 'Laos'), ('Švyturys', 'Lithuania'), ('Utenos Alus', 'Lithuania'), ('Saku', 'Estonia'), ('Falcon', 'Sweden'),
 ('Ringnes', 'Norway'), ('Dahls', 'Norway'), ('Frydenlund', 'Norway'), ('Arendals', 'Norway'), ('Nordlands', 'Norway'), ('Tou', 'Norway'),
 ('Wusu', 'China'), ('Lhasa Beer', 'China'), ('Huizhou Brewery', 'China', '1995'), ('Carlsberg Malaysia', 'Malaysia')])

# ---------------- Molson Coors ----------------
M = 'Molson Coors Beverage Company'
B('MC', 'Miller Lite', M, 'United States', GR, 'United States', U['MC'], old=['Miller Lite'], own_y='2016', role='landmark',
  d='Pilsner-style light lager of 4.2% ABV that made light beer a mass category; Molson Coors took full ownership of the Miller portfolio in 2016.')
B('MC', 'Coors Light', M, 'United States', GR, 'United States', U['MC'], old=['Coors Light'], d='Pilsner-style light lager of 4.2% ABV; Coors Light holds 12% of the Canadian market (2008).')
B('MC', 'Blue Moon', M, 'United States', GR, 'United States', U['MC'], old=['Blue Moon Belgian White'], v=[('Blue Moon Light', 'Light version', '')])
many('MC', M, GR, U['MC'], [
 ('Coors Banquet', 'United States'), ('Miller High Life', 'United States', '2016'), ('Miller Genuine Draft', 'United States', '2016'),
 ('Miller64', 'United States', '2016'), ("Milwaukee's Best", 'United States', '2016'), ('Icehouse', 'United States'), ('Keystone', 'United States'),
 ("Leinenkugel's", 'United States'), ('Steel Reserve', 'United States'), ('Old Style Pilsner', 'United States'), ("Hamm's", 'United States'),
 ("Henry Weinhard's", 'United States'), ('Olde English 800', 'United States'), ("George Killian's Irish Red", 'United States'),
 ('Mickey\'s', 'United States'), ('Red Dog', 'United States'), ('Saint Archer', 'United States'), ('Sol Cerveza', ''),
 ('Molson Canadian', 'Canada'), ('Molson Export', 'Canada'), ('Molson Dry', 'Canada'), ('Molson Golden', 'Canada'), ('Creemore Springs', 'Canada'),
 ('Granville Island Brewing', 'Canada'), ('Laurentide', 'Canada'), ('Carling', 'United Kingdom'), ('Cobra Beer', 'United Kingdom'),
 ("Worthington's", 'United Kingdom'), ("Sharp's Brewery", 'United Kingdom'), ('Staropramen', 'Czech Republic'), ('Ostravar', 'Czech Republic'),
 ('Pardubice', 'Czech Republic'), ('Borsodi', 'Hungary'), ('Jelen', 'Serbia'), ('Ožujsko', 'Croatia'), ('Tomislav', 'Croatia'),
 ('Niksicko', 'Montenegro'), ('Apatinsko', 'Serbia'), ('Kamenitza', 'Bulgaria'), ('AstikA', 'Bulgaria'), ('Bergenbier', 'Romania'),
 ('Madrí', 'Spain'), ('Franciscan Well', 'Ireland'), ('Caffreys', 'Ireland')])
B('MC', 'Worthington White Shield', M, 'United Kingdom', GR, 'United Kingdom', U['MC'], old=['Worthington White Shield'],
  d='Bottle-conditioned English IPA from Worthington\'s, a brand in the Molson Coors Europe list.')

# ---------------- Asahi ----------------
S = 'Asahi Group Holdings'
B('AS', 'Asahi Super Dry', S, 'Japan', GR, 'Japan', U['AS'], old=['Asahi Super Dry'], role='origin',
  v=[('Asahi Super Dry 0.0%', 'Alcohol-free version, 0.0 % ABV', 'alcohol-free'), ('Asahi Dry Zero', 'Japanese beer-taste drink, 0.00 % alcohol', 'alcohol-free'), ('Asahi Draft', 'In-house brand', ''), ('Asahi Gold', 'In-house brand', ''), ('Asahi Z', 'In-house brand', ''), ('Asahi Black', 'In-house brand', ''), ('Asahi Prime Time', 'In-house brand', '')])
B('AS', 'Pilsner Urquell', S, 'Czech Republic', GR, 'Czech Republic', U['AS'], old=['Pilsner Urquell'], own_y='2016', role='origin')
B('AS', 'Peroni', S, 'Italy', GR, 'Italy', U['AS'], own_y='2016', d='Italian lager bought by Asahi with Grolsch and Meantime in a deal closed on 12 October 2016.',
  v=[('Peroni Libera 0.0%', 'Alcohol-free version launched in January 2019, 0.0 % ABV', 'alcohol-free'), ('Peroni Nastro Azzurro 0.0%', 'Alcohol-free successor to Libera, 0.0 % ABV', 'alcohol-free')])
B('AS', 'Grolsch', S, 'Netherlands', GR, 'Netherlands', U['AS'], own_y='2016', d='Dutch lager brand bought in the October 2016 deal.')
B('AS', 'Meantime', S, 'United Kingdom', GR, 'United Kingdom', U['AS'], own_y='2016', d='London brewery bought in the October 2016 deal.')
B('AS', 'Dreher', S, 'Hungary', GR, 'Hungary', U['AS'], own_y='2016', old=['Dreher Vienna lager'])
B('AS', "Fuller's", S, 'United Kingdom', GR, 'United Kingdom', U['AS'], own_y='2019', old=["Fuller's London Pride", "Fuller's ESB", "Fuller's London Porter"],
  d='London brewery whose beer business Asahi bought in 2019; London Pride is its best bitter.')
B('AS', 'Carlton & United Breweries', S, 'Australia', GR, 'Australia', U['AUS'], d='Australian brewer owned by Asahi, with Carlton Draught, Victoria Bitter, Melbourne Bitter and Tooth\'s KB.',
  v=[('Carlton Draught', '', ''), ('Victoria Bitter', '', ''), ('Melbourne Bitter', '', ''), ("Tooth's KB Lager", '', '')])
many('AS', S, GR, U['AS'], [
 ('Velkopopovický Kozel', 'Czech Republic', '2016'), ('Tyskie', 'Poland', '2016'), ('Lech', 'Poland', '2016'), ('Ursus', 'Romania', '2016'),
 ('Radegast', 'Czech Republic', '2016'), ('Gambrinus', 'Czech Republic', '2016'), ('Šariš', 'Slovakia', '2016'), ('Topvar', 'Slovakia', '2016'),
 ('Mountain Goat Brewery', 'Australia', '2015'), ('Cricketers Arms', 'Australia', '2013')])
B('AS', 'Cascade', S, 'Australia', GR, 'Australia', U['AUS'], d='Australia\'s oldest operating brewery, owned by Asahi.')

# ---------------- Kirin ----------------
K = 'Kirin Holdings'
B('KI', 'Kirin Lager', K, 'Japan', GR, 'Japan', U['KI'], y='1888', d='Kirin\'s own lager, brewed since 1888.', v=[('Kirin Zero ICHI', 'Non-alcoholic beer-taste drink, 0.00 % alcohol, launched 11 April 2017', 'alcohol-free'), ('Ichiban Shibori', 'Kirin product', ''), ('Kirin Tanrei', 'Happoshu product', '')])
B('KI', "Bell's Brewery", K, 'United States', GR, 'United States', U['KI'], old=["Bell's Two Hearted Ale", "Bell's Hopslam", "Bell's Oberon"],
  d='Michigan craft brewery listed as owned by Kirin; Two Hearted Ale is its American IPA.')
B('KI', 'New Belgium Brewing', K, 'United States', GR, 'United States', U['KI'], d='Colorado craft brewery listed as owned by Kirin; BA lists Kirin-Lion at Fort Collins among the overall top 50.')
B('KI', 'Lion', K, 'Australia', GR, 'Australia', U['KI'], d='Lion Nathan, the Australian and New Zealand brewer in which Kirin holds 100%; it brews Kirin and licensed beers.')
B('KI', "Boag's", 'Lion Nathan', 'Australia', GR, 'Australia', U['AUS'], own_y='2007', d='Tasmanian beer bought by Lion Nathan in November 2007 for A$325 million.')
B('KI', 'Spring Valley Brewery', K, 'Japan', GR, 'Japan', U['KI'], own_y='2014', d='Japanese craft brewery revived as a wholly owned Kirin subsidiary in 2014.')
B('KI', 'Brasil Kirin', K, 'Brazil', GR, 'Brazil', U['KI'], own_y='2011', d='Former Schincariol, bought by Kirin in 2011; Nova Schin held 10.2% of Brazil in 2005.')

# ---------------- Tsingtao ----------------
B('TS', 'Tsingtao Beer', 'Tsingtao Brewery Group', 'China', GR, 'China', U['TS'], y='1903', role='landmark',
  d='Flagship 4.7% pale lager; the page says it was the second most consumed beer worldwide in 2016 with 2.8% of global beer.',
  v=[('Tsingtao Draft Beer', 'Unpasteurised version of the flagship', ''), ('Tsingtao Dark Beer', '5.2% ABV', ''), ('Tsingtao Spirulina Green Beer', '4.5% green pilsner', '')])
