from data2 import B, many, ENT, GR, NT, CF, IN, OLB
from data1 import U

# ---------------- National & regional brands ----------------
# Europe
B('EU', 'Obolon', 'Obolon CJSC', 'Ukraine', '', 'Ukraine', U['REG'], d='Ukrainian brewer with a production site in Kyiv, named on the regional page.')
many('EU', '', '', U['REG'], [('Birra Tirana', 'Albania'), ('Birra Korça', 'Albania'), ('Birra Kaon', 'Albania'), ('Birra Puka', 'Albania'), ('Birra Stela', 'Albania'),
 ('Kalnapilis', 'Lithuania'), ('Ragutis', 'Lithuania'), ('Tauras', 'Lithuania'), ('Smädný mních', 'Slovakia'), ('Corgoň', 'Slovakia'), ('Steiger', 'Slovakia'),
 ('Kilikia', 'Armenia'), ('Kotayk', 'Armenia'), ('Gyumri', 'Armenia'), ('Dilijan', 'Armenia'), ('Estrella Levante', 'Spain'), ('Reina', 'Spain'),
 ('Dorada', 'Spain'), ('Ambar', 'Spain', '', 'Beer of La Zaragozana, named on the regional page for Spain.'), ('Alhambra (Granada)', 'Spain')])
B('EU', 'Sinebrychoff', '', 'Finland', '', 'Finland', 'https://en.wikipedia.org/wiki/Sinebrychoff_Brewery', old=['Sinebrychoff Porter'], d='Finnish brewery making a Baltic porter since the 1860s.')

# North America
B('NA', "Gablinger's Diet Beer", 'Rheingold Breweries', 'United States', '', 'United States', 'https://en.wikipedia.org/wiki/Pale_lager', old=["Gablinger's Diet Beer"], role='origin')
B('NA', 'Genesee', 'Genesee Brewing Company', 'United States', '', 'United States', 'https://en.wikipedia.org/wiki/Genesee_Brewing_Company', old=['Genesee Cream Ale'])
B('NA', 'Little Kings', 'Schoenling Brewing Company', 'United States', '', 'United States', 'https://en.wikipedia.org/wiki/Little_Kings', old=['Little Kings'])
B('NA', 'Yuengling Lager', "D.G. Yuengling & Son", 'United States', IN, 'United States', U['BA'], d='Amber lager of the Pottsville brewery that tops the Brewers Association craft list for 2024.')

# Latin America
B('LA', 'Nova Schin', 'Brasil Kirin', 'Brazil', '', 'Brazil', U['BRZ'], d='Brazilian lager of Grupo Schincariol with 10.2% of the market in 2005; the maker later became Brasil Kirin.')
B('LA', 'Franca', 'Ajeper', 'Peru', '', 'Peru', U['REG'], d='Peruvian beer of Ajeper, named on the regional page.')

# Africa & Middle East
B('AF', 'Tusker', 'East African Breweries Limited', 'Kenya', '', 'Kenya', U['KEN'], d='Kenyan lager first brewed by Kenya Breweries, founded in 1922; now a product of EABL.')
B('AF', 'White Cap', 'East African Breweries Limited', 'Kenya', '', 'Kenya', U['KEN'], d='Kenyan pale lager of EABL.')
B('AF', 'Summit Malt', 'Keroche Breweries', 'Kenya', '', 'Kenya', U['KEN'], d='Kenyan malt beer from Keroche Breweries of Naivasha, founded in 1997.')
B('AF', "Jo'burg Beer", '', 'South Africa', '', 'South Africa', U['ZAF'], d='Low-priced independent South African brand popular with lower-income drinkers.')
B('AF', 'Almaza', 'Almaza', 'Lebanon', '', 'Lebanon', U['HE'], own_y='2021', d='Lebanese pilsner brewery; the page says Philippe Jabre took majority ownership in December 2021.')

# South Asia
B('SA', 'Kingfisher', 'United Breweries', 'India', NT, 'India', U['IND'], role='landmark', d='Best-selling Indian beer brand, with 41.2% of the Indian market in 2014.')
B('SA', 'Kalyani Black Label', 'United Breweries', 'India', NT, 'India', U['IND'], d='United Breweries brand with 2.7% of the Indian market in 2014.')
B('SA', 'Golden Eagle', 'Mohan Meakin', 'India', IN, 'India', U['IND'], d='Mohan Meakin brand with 1.7% of the Indian market in 2014.')
B('SA', 'Black Knight', 'Mohan Meakin', 'India', IN, 'India', U['IND'], d='Mohan Meakin brand with 1.1% of the Indian market in 2014.')

# East Asia
B('EA', 'Yanjing', 'Beijing Yanjing Brewery', 'China', IN, 'China', U['CHN'], d='Beijing brewery named a major Chinese group; its group output was 40 million hl in 2024.')
B('EA', 'Zhujiang', 'Guangzhou Zhujiang Brewery Group', 'China', IN, 'China', U['CHN'], d='Guangzhou beer named a major Chinese brewing group.')
B('EA', 'Kingway', 'Kingway Brewery', 'China', IN, 'China', U['CHN'])
B('EA', 'China Pabst Blue Ribbon', 'Joint venture', 'China', IN, 'China', U['CHN'])
B('EA', 'Taedonggang', '', 'North Korea', NT, 'North Korea', U['REG'], d='Named the top brand of North Korea on the regional page.')

# Southeast Asia
B('SE', 'Leo', 'Boon Rawd Brewery', 'Thailand', NT, 'Thailand', U['THA'], d='Standard Thai lager; 53% of the Thai market in 2018.')
B('SE', 'Chang', 'Thai Beverages', 'Thailand', IN, 'Thailand', U['THA'], d='Thai lager of ThaiBev and Singha\'s largest competitor; 38% of the Thai market in 2018.')
B('SE', 'Singha', 'Boon Rawd Brewery', 'Thailand', IN, 'Thailand', U['THA'], y='1933', d='Thailand\'s best-known lager, first brewed under a licence granted in 1933; 5% of the market in 2018.')
B('SE', 'Archa', 'Thai Beverages', 'Thailand', IN, 'Thailand', U['THA'], d='Mass-market non-premium Thai lager.')
B('SE', 'Phuket Beer', 'San Miguel Brewery', 'Thailand', '', 'Thailand', U['THA'], d='Thai beer brewed to the German purity law under San Miguel supervision.')
B('SE', 'San Miguel Pale Pilsen', 'San Miguel Brewery', 'Philippines', NT, 'Philippines', U['SMB'], d='Philippine pale lager of the country\'s largest brewery, which held over 95% of the market in 2008.',
  v=[('San Miguel Premium All-Malt', '', ''), ('San Miguel Super Dry', '', ''), ('San Mig Light', '', ''), ('San Mig Extra Light', '', ''), ('Red Horse', 'Strong lager', ''), ('Gold Eagle Beer', '', ''), ('San Mig Zero', 'Zero', 'alcohol-free')])
B('SE', 'Bia Saigon', 'Saigon Beverage Corporation (Sabeco)', 'Vietnam', '', 'Vietnam', U['VNM'], d='Sabeco range with 333 Beer; Sabeco held 33.9% of the Vietnamese market in 2023.', v=[('333 Beer', '', '')])
B('SE', 'Bia Hanoi', 'Habeco', 'Vietnam', '', 'Vietnam', U['VNM'], d='Northern Vietnam brand; Habeco held 7.5% of the market in 2023.')
B('SE', 'Myanmar Beer', 'Myanmar Brewery', 'Myanmar', '', 'Myanmar', U['REG'], d='Myanmar Brewery range with Double Strong and Andaman Gold.')

# Oceania
B('OC', 'Coopers', "Coopers Brewery", 'Australia', IN, 'Australia', U['AUS'], d='Largest Australian-owned brewery and the only major one not owned by a multinational since 2011; over 5% of the market (2016).',
  old=['Coopers Best Extra Stout'])

# ---------------- Independents ----------------
# Europe
B('IE', 'Guinness', 'Diageo', 'Ireland', IN, 'Ireland', U['VP'], old=['Guinness Draught', 'Guinness Foreign Extra Stout', 'Guinness West Indies Porter'], role='landmark',
  v=[('Guinness 0.0', 'Zero-alcohol stout; relaunched 2021', 'alcohol-free')])
B('IE', 'Oettinger', 'Oettinger Gruppe', 'Germany', IN, 'Germany', U['GER'], d='Germany\'s best-selling brand by output in 2012 (5.89 million hl); 5.39 million hl in 2015.')
B('IE', 'Krombacher', 'Krombacher Gruppe', 'Germany', IN, 'Germany', U['GER'], d='Kreuztal pilsner brewery; 5.49 million hl in 2015.')
B('IE', 'Bitburger', 'Bitburger Braugruppe', 'Germany', IN, 'Germany', U['GER'], old=['Bitburger Pilsner'], d='Bitburg pilsner; 3.84 million hl in 2015.')
B('IE', 'Warsteiner', '', 'Germany', IN, 'Germany', U['GER'], d='Warstein pilsner brewery; 2.34 million hl in 2015.')
B('IE', 'Veltins', '', 'Germany', IN, 'Germany', U['GER'], d='Meschede pilsner brewery; 2.79 million hl in 2015.')
B('IE', 'Radeberger', 'Radeberger Gruppe', 'Germany', IN, 'Germany', U['GER'], d='Radeberg pilsner; 1.90 million hl in 2015.')
B('IE', 'Paulaner', 'Paulaner Gruppe', 'Germany', IN, 'Germany', U['GER'], old=['Paulaner Salvator', 'Paulaner Hefe-Weissbier'], d='Munich brewery; 2.42 million hl in 2015. Salvator is its Doppelbock of 1751.')
B('IE', 'Erdinger', '', 'Germany', IN, 'Germany', U['GER'], old=['Erdinger Weissbier'], d='Erding wheat-beer brewery; 1.80 million hl in 2015.')
B('IE', 'Jever', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Jever_Pilsener', old=['Jever Pilsener'])
B('IE', 'Augustiner-Bräu', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Augustiner_Brewery', old=['Augustiner Lagerbier Hell', 'Munich Oktoberfestbier'])
B('IE', 'Ayinger', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Ayinger', old=['Ayinger Altbairisch Dunkel', 'Ayinger Celebrator'])
B('IE', 'Köstritzer', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/K%C3%B6stritzer', old=['Köstritzer Schwarzbier'])
B('IE', 'Kulmbacher', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Kulmbacher_Brauerei', old=['Kulmbach Schwarzbier', 'Kulmbacher Eisbock'])
B('IE', 'Schlenkerla', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Schlenkerla', old=['Aecht Schlenkerla Rauchbier'])
B('IE', 'Einbecker', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Einbecker_Brauhaus', old=['Einbecker Ur-Bock'])
B('IE', 'Schneider Weisse', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Schneider_Weisse', old=['Schneider Weisse Tap 7 Mein Original', 'Schneider Aventinus', 'Aventinus Eisbock'])
B('IE', 'Weihenstephan', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Weihenstephan_Brewery', old=['Weihenstephaner Hefeweissbier'])
B('IE', 'Reissdorf', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Reissdorf', old=['Reissdorf Kölsch'])
B('IE', 'Früh', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Fr%C3%BCh', old=['Früh Kölsch'])
B('IE', 'Gaffel', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Gaffel', old=['Gaffel Kölsch'])
B('IE', 'Uerige', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Uerige', old=['Uerige Alt'])
B('IE', 'Schumacher', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Schumacher_Alt', old=['Schumacher Alt'])
B('IE', 'Dortmunder Union', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Dortmunder_Union', old=['Dortmunder Union Export'])
B('IE', 'Berliner Kindl', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Berliner_Kindl', old=['Berliner Kindl Weisse'])
B('IE', 'Leipziger Gose', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Gose', old=['Leipziger Gose'])
B('IE', 'Zoigl', '', 'Germany', IN, 'Germany', 'https://en.wikipedia.org/wiki/Zoigl', old=['Zoigl'])
B('IE', 'Budějovický Budvar', 'Budějovický Budvar', 'Czech Republic', IN, 'Czech Republic', 'https://en.wikipedia.org/wiki/Budweiser_Budvar_Brewery', old=['Budějovický Budvar Original'],
  v=[('Budvar Free', 'Low-alcohol version', 'low')], y='1895')
B('IE', 'U Fleků', 'U Fleků', 'Czech Republic', IN, 'Czech Republic', 'https://en.wikipedia.org/wiki/U_Flek%C5%AF', old=['U Fleků Flekovský tmavý ležák 13°'])
B('IE', 'Duvel Moortgat', 'Duvel Moortgat', 'Belgium', IN, 'Belgium', 'https://en.wikipedia.org/wiki/Duvel_Moortgat_Brewery', old=['Duvel'])
B('IE', 'Swinkels (Bavaria, La Trappe, Rodenbach)', 'Swinkels Family Brewers', 'Netherlands', IN, 'Netherlands', U['SWI'],
  old=['La Trappe Tripel', 'La Trappe Quadrupel', 'Rodenbach Grand Cru'], d='Family-owned Dutch brewer for seven generations; its brands include Bavaria, Swinckels\', La Trappe and Rodenbach.')
B('IE', 'Brasserie Dupont', '', 'Belgium', IN, 'Belgium', 'https://en.wikipedia.org/wiki/Brasserie_Dupont', old=['Saison Dupont'])
B('IE', 'Jenlain', 'Brasserie Duyck', 'France', IN, 'France', 'https://en.wikipedia.org/wiki/Jenlain', old=['Jenlain Ambrée'])
B('IE', 'Mahou', 'Mahou San Miguel', 'Spain', IN, 'Spain', U['MAH'], y='1890', d='Madrid brewery founded in 1890; Mahou Clásica is the leading beer in Spain.',
  v=[('Mahou Cinco Estrellas', '1969', ''), ('Mahou Negra', '2003', ''), ('Mahou Sin', '1990, first called Laiker', '')])
B('IE', 'San Miguel (Spain)', 'Mahou San Miguel', 'Spain', IN, 'Spain', U['MAH'], own_y='2000', d='Spanish San Miguel; Mahou took 70% from Danone in 2000.',
  v=[('San Miguel Especial', '1957', ''), ('San Miguel 0,0', '2001', 'alcohol-free'), ('San Miguel 1516', '2003', ''), ('San Miguel ECO', '2003', '')])
B('IE', 'Alhambra', 'Mahou San Miguel', 'Spain', IN, 'Spain', U['MAH'], d='Granada beer in the Mahou San Miguel group.', v=[('Alhambra Reserva 1925', '', ''), ('Alhambra Negra', '', ''), ('Mezquita', '', ''), ('Alhambra Sin', '', '')])
B('IE', 'Estrella Damm', 'Damm', 'Spain', IN, 'Spain', U['REG'], d='Barcelona lager; the Damm group brewed 12.65 million hl in 2024.')
B('IE', 'Estrella Galicia', 'Estrella de Galicia', 'Spain', IN, 'Spain', U['REG'], d='Galician lager; the group brewed 5.3 million hl in 2024.')
B('IE', 'Efes Pilsen', 'Efes Group', 'Turkey', IN, 'Turkey', U['VP'], d='Turkish lager of the Efes Group, which brewed 38.7 million hl in 2024.')

# Americas
B('IA', 'Moosehead', 'Moosehead Breweries', 'Canada', IN, 'Canada', U['CAN'], d='Largest fully Canadian-owned brewer, with about 3.8% of the domestic market in 2016.')
B('IA', 'Polar', 'Empresas Polar', 'Venezuela', IN, 'Venezuela', U['VP'], d='Venezuelan beer; the brewer made 4.75 million hl in 2024.')
many('IA', 'Compañía de las Cervecerías Unidas', IN, U['REG'], [('Schneider', 'Argentina'), ('Imperial', 'Argentina'), ('Isenbeck', 'Argentina')])
B('IA', 'Pabst Blue Ribbon', 'Pabst Brewing Co', 'United States', IN, 'United States', U['BA'], d='Pabst ranks fifth among all US brewing companies on the Brewers Association 2024 list.')

# Asia, Africa, Oceania
B('IW', 'Sapporo', 'Sapporo Holdings', 'Japan', IN, 'Japan', U['SAP'], y='1876', d='Hokkaido brewery of 1876; Sapporo Draft is sold as Sapporo Premium in North America.',
  v=[('Yebisu', 'Luxury label, first brewed 1890', ''), ('Sapporo Black Label', 'Launched 1977', ''), ('Super Clear', 'Low-alcohol malt drink, 2002', 'low')])
B('IW', 'Sleeman', 'Sapporo Holdings', 'Canada', IN, 'Canada', U['SAP'], own_y='2006', old=['Sleeman Cream Ale'], d='Canadian brewer bought by Sapporo in 2006 for $400 million.')
B('IW', 'Stone Brewing', 'Sapporo Holdings', 'United States', IN, 'United States', U['SAP'], own_y='2022', d='California craft brewery bought by Sapporo in 2022.')
B('IW', 'Castel Beer', 'Groupe Castel', 'France', IN, 'Africa', U['CAS'], d='Beer of the family-owned Castel group, active in about twenty African countries (2023); Flag and 33 Export are its other African brands.',
  v=[('Flag', '', ''), ('33 Export', '', '')], own_y='1990')

# ---------------- Craft & indie ----------------
CU_TOP = [
 ('D.G. Yuengling and Son Inc','Pottsville','PA'),('Boston Beer Co','Boston','MA'),('Sierra Nevada Brewing Co','Chico','CA'),('Tilray Beer Brands','New York','NY'),
 ('Duvel Moortgat USA','Cooperstown','NY'),('Gambrinus','Shiner','TX'),('Matt Brewing Co','Utica','NY'),('Athletic Brewing Company','Milford','CT'),
 ('Brooklyn Brewery','Brooklyn','NY'),('Monster Brewing','Longmont','CO'),('Deschutes Brewery','Bend','OR'),('New Glarus Brewing Co','New Glarus','WI'),
 ('Barrel One Collective','Boston','MA'),('Georgetown Brewing Co','Seattle','WA'),('Gordon Biersch Brewing Co','San Jose','CA'),('Rhinegeist Brewery','Cincinnati','OH'),
 ("Craft 'Ohana (Maui/Modern Times)",'Kihei','HI'),('Great Lakes Brewing Company','Cleveland','OH'),('Narragansett Brewing Co','Pawtucket','RI'),('Tröegs Brewing Co','Hershey','PA'),
 ('Allagash Brewing Company','Portland','ME'),('August Schell Brewing Company','New Ulm','MN'),('Fiddlehead Brewing','Shelburne','VT'),('Stevens Point Brewery','Stevens Point','WI'),
 ('Pittsburgh Brewing Co','Pittsburgh','PA'),('Three Floyds Brewing','Munster','IN'),('Odell Brewing Co','Fort Collins','CO'),('Great Frontier Holdings','Eugene','OR'),
 ('Abita Brewing Co','Covington','LA'),('BrewDog Brewing Co','Canal Winchester','OH'),('Creature Comforts Brewing Co.','Athens','GA'),('Hendler Family Brewing Company','Framingham','MA'),
 ('Alaskan Brewing Co.','Juneau','AK'),('Summit Brewing Co','St. Paul','MN'),('Saint Arnold Brewing Co','Houston','TX'),('Revolution Brewing','Chicago','IL'),
 ('Kona Brewing Hawaii','Kailua-Kona','HI'),('Pizza Port','Carlsbad','CA'),('Surly Brewing Company','Minneapolis','MN'),('pFriem Family Brewers','Hood River','OR'),
 ('Fremont Brewing','Seattle','WA'),('The Florida Brewery','Auburndale','FL'),("BJ's Restaurants, Inc.",'Huntington Beach','CA'),('Russian River Brewing Co','Santa Rosa','CA'),
 ('Shipyard Brewing Co','Portland','ME'),('New Trail Brewing Company','Williamsport','PA'),('Zero Gravity Craft Brewery','Burlington','VT'),("Fat Head's Brewery",'Middleburg Heights','OH'),
 ("Drake's Brewing Co./Bear Republic",'San Leandro','CA'),('Rogue Ales Brewery','Newport','OR')]
CU_OLD = {  # top-50 name -> old entries absorbed
 'D.G. Yuengling and Son Inc': [], 'Sierra Nevada Brewing Co': ['Sierra Nevada Pale Ale', 'Sierra Nevada Bigfoot'],
 'Deschutes Brewery': ['Black Butte Porter'], 'Great Lakes Brewing Company': ['Edmund Fitzgerald Porter'], 'Allagash Brewing Company': ['Allagash White'],
 'Russian River Brewing Co': ['Pliny the Elder'], 'BrewDog Brewing Co': ['BrewDog Punk IPA'],
}
for i, (nm, city, st) in enumerate(CU_TOP, 1):
    grp = f'Ranks {((i-1)//10)*10+1}-{((i-1)//10)*10+10}'
    own, oy, role, d = nm, '', '', f'Craft brewing company of {city}, {st}, ranked {i} among US craft brewers by volume in 2024 (Brewers Association).'
    if i == 1: role = 'landmark'; d = f'Pottsville, PA brewer ranked first among US craft brewers by volume in 2024 (Brewers Association).'
    if nm == 'Kona Brewing Hawaii': own, oy = 'Anheuser-Busch', '2020'; d += ' Anheuser-Busch bought Kona Big Wave in 2020.'
    if nm == 'Brooklyn Brewery': d += ' Kirin holds a 24.5% stake.'
    if nm == 'Duvel Moortgat USA': d += ' US arm of the Belgian Duvel Moortgat group.'
    if nm == 'Athletic Brewing Company': d = f'Milford, CT brewery making only non-alcoholic beer, ranked {i} among US craft brewers in 2024 (Brewers Association).'
    B('CU', nm, own, 'United States', CF, grp, U['BA'], d=d, old=CU_OLD.get(nm, []), own_y=oy, role=role)
B('CU', 'Tilray Beer Brands (Molson Coors sale)', 'Tilray', 'United States', CF, 'Ranks 1-10', U['MC'], own_y='2024',
  d='Tilray bought Hop Valley, Terrapin, Revolver and Atwater from Molson Coors in August 2024.', v=[('Hop Valley', '', ''), ('Terrapin', '', ''), ('Revolver Brewing', '', ''), ('Atwater', '', '')])
OUT = 'Outside the 2024 top 50'
for nm, own, oy, olds, src in [
 ('Anchor Brewing', 'Sapporo Holdings', '2017', ['Anchor Liberty Ale', 'Anchor Porter', 'Anchor Old Foghorn', 'Anchor Steam Beer'], U['SAP']),
 ('Dogfish Head', '', '', ['Dogfish Head 60 Minute IPA', 'Dogfish Head 90 Minute IPA'], 'https://en.wikipedia.org/wiki/Dogfish_Head_Brewery'),
 ('Founders Brewing', 'Mahou San Miguel', '2019', ['Founders Porter', 'Kentucky Breakfast Stout'], U['MAH']),
 ('The Alchemist', '', '', ['Heady Topper'], 'https://en.wikipedia.org/wiki/The_Alchemist_(brewery)'),
 ('Tree House Brewing Company', '', '', ['Tree House Julius'], 'https://en.wikipedia.org/wiki/Tree_House_Brewing_Company'),
 ('Left Hand Brewing', '', '', ['Left Hand Milk Stout'], 'https://en.wikipedia.org/wiki/Left_Hand_Brewing_Company'),
 ('North Coast Brewing', '', '', ['Old Rasputin'], 'https://en.wikipedia.org/wiki/North_Coast_Brewing_Company'),
 ('Great Divide Brewing', '', '', ['Yeti Imperial Stout'], 'https://en.wikipedia.org/wiki/Great_Divide_Brewing_Company'),
 ('Widmer Brothers', '', '', ['Widmer Weizenbier'], 'https://en.wikipedia.org/wiki/Widmer_Brothers_Brewery'),
 ('Celis Brewery', '', '', ['Celis White'], 'https://en.wikipedia.org/wiki/Celis_Brewery'),
 ('Ballantine', 'P. Ballantine and Sons', '', ['Ballantine IPA'], 'https://en.wikipedia.org/wiki/Ballantine_Brewery')]:
    B('CU', nm, own, 'United States', CF, OUT, src, old=olds, own_y=oy)

# Belgium & Netherlands
BEL = 'https://en.wikipedia.org/wiki/Trappist_beer'
for nm, olds, src in [
 ('Westvleteren', ['Westvleteren Blond', 'Westvleteren 8', 'Westvleteren 12'], BEL), ('Westmalle', ['Westmalle Extra', 'Westmalle Dubbel', 'Westmalle Tripel'], BEL),
 ('Chimay', ['Chimay Dorée', 'Chimay Red', 'Chimay Triple', 'Chimay Blue'], BEL), ('Rochefort', ['Rochefort 6', 'Rochefort 10'], BEL),
 ('St. Bernardus', ['St. Bernardus Abt 12'], 'https://en.wikipedia.org/wiki/St._Bernardus_Brewery'), ('Witkap (Slaghmuylder)', ['Witkap Tripel'], 'https://en.wikipedia.org/wiki/Witkap'),
 ('Cantillon', ['Cantillon Grand Cru Bruocsella', 'Cantillon Gueuze 100% Lambic', 'Cantillon Rosé de Gambrinus'], 'https://en.wikipedia.org/wiki/Brasserie_Cantillon'),
 ('Oud Beersel', ['Oud Beersel Oude Lambiek', 'Oud Beersel Oude Geuze'], 'https://en.wikipedia.org/wiki/Oud_Beersel'),
 ('3 Fonteinen', ['3 Fonteinen Oude Geuze'], 'https://en.wikipedia.org/wiki/Drie_Fonteinen'), ('Boon', ['Oude Geuze Boon'], 'https://en.wikipedia.org/wiki/Brouwerij_Boon'),
 ('Girardin', ['Girardin Gueuze 1882'], 'https://en.wikipedia.org/wiki/Brouwerij_Girardin'), ('Hanssens Artisanaal', ['Hanssens Oude Geuze'], 'https://en.wikipedia.org/wiki/Hanssens_Artisanaal'),
 ('Tilquin', ['Oude Gueuze Tilquin'], 'https://en.wikipedia.org/wiki/Gueuzerie_Tilquin'), ('Lindemans', ['Lindemans Gueuze Cuvée René', 'Lindemans Framboise'], 'https://en.wikipedia.org/wiki/Lindemans_Brewery'),
 ('Liefmans', ['Liefmans Goudenband'], 'https://en.wikipedia.org/wiki/Liefmans_Brewery'), ('Verhaeghe (Duchesse de Bourgogne)', ['Duchesse de Bourgogne'], 'https://en.wikipedia.org/wiki/Brouwerij_Verhaeghe'),
 ('Omer Vander Ghinste', ['Cuvée des Jacobins'], 'https://en.wikipedia.org/wiki/Brouwerij_Vander_Ghinste'), ('De Brabandere (Petrus)', ['Petrus Oud Bruin'], 'https://en.wikipedia.org/wiki/Brouwerij_De_Brabandere')]:
    B('CB', nm, '', 'Belgium', CF, 'Belgium', src, old=olds)

# British & Irish
for nm, own, olds, src in [
 ('Samuel Smith', "Samuel Smith's", ['Samuel Smith Taddy Porter', 'Samuel Smith Oatmeal Stout', 'Samuel Smith Imperial Stout'], 'https://en.wikipedia.org/wiki/Samuel_Smith_Brewery'),
 ("Timothy Taylor's", '', ["Timothy Taylor's Landlord"], 'https://en.wikipedia.org/wiki/Timothy_Taylor_Brewery'),
 ('Bass', '', ['Draught Bass', 'Bass No. 1 Ale'], 'https://en.wikipedia.org/wiki/Bass_Brewery'),
 ('Hop Back Brewery', '', ['Hop Back Summer Lightning'], 'https://en.wikipedia.org/wiki/Hop_Back_Brewery'),
 ('Theakston', '', ['Theakston Old Peculier'], 'https://en.wikipedia.org/wiki/T._%26_R._Theakston'),
 ('Greene King', '', ['Greene King Strong Suffolk'], 'https://en.wikipedia.org/wiki/Greene_King'),
 ("Gale's", '', ["Gale's Prize Old Ale"], 'https://en.wikipedia.org/wiki/George_Gale_%26_Co'),
 ('Belhaven', '', ['Belhaven Scottish ales'], 'https://en.wikipedia.org/wiki/Belhaven_Brewery'),
 ("McEwan's", '', ["McEwan's Scotch Ale"], 'https://en.wikipedia.org/wiki/McEwan%27s'),
 ('Traquair House Brewery', '', ['Traquair House Ale'], 'https://en.wikipedia.org/wiki/Traquair_House'),
 ('Orkney Brewery', '', ['Orkney Skull Splitter'], 'https://en.wikipedia.org/wiki/Orkney_Brewery'),
 ('John Martin (Gordon\'s)', '', ["Gordon's Highland Scotch Ale"], 'https://en.wikipedia.org/wiki/Gordon%27s_Scotch_Ale'),
 ('Maclay', '', ['Maclay Original Oatmalt Stout'], 'https://en.wikipedia.org/wiki/Maclay_Brewery'),
 ("Mackeson", '', ["Mackeson's XXX Stout"], 'https://en.wikipedia.org/wiki/Mackeson_Stout'),
 ('Eldridge Pope', '', ["Thomas Hardy's Ale"], 'https://en.wikipedia.org/wiki/Eldridge_Pope'),
 ('Courage', '', ['Courage Imperial Russian Stout'], 'https://en.wikipedia.org/wiki/Courage_Brewery'),
 ('Export India ale', '', ['Export India ale'], 'https://en.wikipedia.org/wiki/India_pale_ale'),
 ('Tartan IPA', '', ['Tartan IPA'], 'https://en.wikipedia.org/wiki/India_pale_ale'),
 ('Wiibroe', '', ['Wiibroe Imperial Stout'], 'https://en.wikipedia.org/wiki/Wiibroe')]:
    B('CG', nm, own, 'United Kingdom' if nm != 'Wiibroe' else 'Denmark', '', 'United Kingdom' if nm != 'Wiibroe' else 'Denmark', src, old=olds)

# ---------------- Own label ----------------
B('OL', 'Aldi own-label beers', 'Aldi', 'United States', OLB, 'United States', U['PUN'], d='Aldi sells beers under its own names, brewed under contract by Octopi Brewing and Genesee Brewing Co.',
  v=[('Wild Range Brewing Company IPA', 'American IPA', ''), ('White Tide Wheat Beer', 'Wheat beer', ''), ('Wernesgruner Pilsner', 'Pilsner', ''), ("Locken's Ruby Grapefruit Kölsch", 'Kölsch, brewed by Genesee', '')])
B('OL', 'Josephsbrau (Trader Joe\'s)', "Trader Joe's", 'United States', OLB, 'United States', U['PUN'], d='In-house brewery name used on Trader Joe\'s beers.',
  v=[('Drive Thru Red Dry Hopped Red Ale', 'Red ale', ''), ('Stockyard Oatmeal Stout', 'Oatmeal stout', ''), ('Boatswain IPA', 'IPA', ''), ('Trader José', 'Mexican-style lager, discontinued', '')])
B('OL', 'Kirkland Signature Helles-Style Lager', 'Costco', 'United States', OLB, 'United States', U['PUN'], d='Costco own-label Helles repackaged from Deschutes\' Prinz Crispy.')
B('OL', 'Mountain Brew', "Stewart's Shops", 'United States', OLB, 'United States', U['PUN'], d='Convenience-store own label brewed by Paradox Brewery.')
