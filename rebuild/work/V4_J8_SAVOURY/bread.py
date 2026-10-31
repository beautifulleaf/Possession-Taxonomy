from lib import *
GB='Grupo Bimbo'
S_BIMBO=WP+'Grupo_Bimbo'
def bim(n,cty,d,y='',own_y='',g='',**kw):
    return E(n,d,S_BIMBO,own=GB,tier='Global group',cty=cty,y=y,own_y=own_y,g=g,**kw)
bimbo=[
 bim('Bimbo','Mexico','Mexican bread and bakery brand that gave the group its name, founded 1945.',y='1945',g='Mexico',role='origin'),
 bim('Tía Rosa','Mexico','Mexican packaged bread and cake brand, inaugurated 1974.',y='1974',g='Mexico'),
 bim('Marinela','Mexico','Mexican snack-cake brand of the group.',g='Mexico'),
 bim('Gansito','Mexico','Mexican filled snack cake launched 1958.',y='1958',g='Mexico'),
 bim('Sunbeam','Mexico','Bread brand held under licence in Mexico, acquired 1964.',own_y='1964',g='Mexico'),
 bim('El Globo','Mexico','Mexican pastry chain and brand, acquired 2005.',own_y='2005',g='Mexico'),
 bim('Mrs Baird\'s','United States','Texas bread brand, acquired 1998.',own_y='1998',g='United States'),
 bim('Oroweat','United States','US bread brand from the George Weston bakery business, acquired 2009.',own_y='2009',g='United States'),
 bim('Thomas\'','United States','US English muffin and bagel brand from the George Weston bakery business, acquired 2009.',own_y='2009',g='United States'),
 bim('Arnold','United States','US bread brand from the George Weston bakery business, acquired 2009.',own_y='2009',g='United States'),
 bim('Boboli','United States','US pizza crust brand from the George Weston bakery business, acquired 2009.',own_y='2009',g='United States'),
 bim('Stroehmann','United States','US bread brand from the George Weston bakery business, acquired 2009.',own_y='2009',g='United States'),
 bim('Freihofer\'s','United States','US bread and baked-goods brand from the George Weston bakery business, acquired 2009.',own_y='2009',g='United States'),
 bim('Sara Lee (North American fresh bakery)','United States','Sara Lee fresh bread and bakery business in North America, acquired 2011.',own_y='2011',g='United States'),
 bim('Bays English Muffins','United States','US English muffin brand, added 2017.',own_y='2017',g='United States'),
 bim('Canada Bread','Canada','Canadian bread company and brand, acquired 2014.',own_y='2014',g='Canada'),
 bim('Vachon','Canada','Canadian snack-cake brand, acquired 2015.',own_y='2015',g='Canada'),
 bim('Stonemill Bakehouse','Canada','Canadian bakery brand, added 2017.',own_y='2017',g='Canada'),
 bim('Pullman','Brazil','Brazilian bread brand, acquired 2001.',own_y='2001',g='Brazil'),
 bim('Plus Vita','Brazil','Brazilian bread and cake brand, acquired 2001.',own_y='2001',g='Brazil'),
 bim('Nutrella','Brazil','Brazilian bread brand, acquired 2008.',own_y='2008',g='Brazil'),
 bim('Fargo','Argentina','Argentine bread brand, acquired 2011.',own_y='2011',g='Argentina'),
 bim('Ideal','Chile','Chilean bakery brand (Grupo Ideal), acquired 1995.',own_y='1995',g='Chile'),
 bim('Nutra Bien','Chile','Chilean bakery brand, acquired 2018.',own_y='2018',g='Chile'),
 bim('Supán','Ecuador','Ecuadorian bakery brand, acquired 2014.',own_y='2014',g='Ecuador'),
 bim('Panettiere','Colombia','Colombian bakery brand, acquired 2016.',own_y='2016',g='Colombia'),
 bim('El Paisa','Colombia','Colombian bakery brand, acquired 2018.',own_y='2018',g='Colombia'),
 bim('Bimbo Iberia','Spain and Portugal','Spanish and Portuguese bread business acquired in 2011.',own_y='2011',g='Europe'),
 bim('Panrico','Spain and Portugal','Spanish and Portuguese bakery company and brand, acquired 2016.',own_y='2016',g='Europe'),
 bim('St Pierre','United Kingdom','British bakery brand, acquired 2022.',own_y='2022',g='Europe'),
 bim('Vel Pitar','Romania','Romanian bread brand, acquired 2023.',own_y='2023',g='Europe'),
 bim('Ready Roti','India','Indian flatbread maker; the group bought a 65% stake in 2017.',own_y='2017',g='Asia'),
 bim('Modern','India','Indian bread brand (Modern Group), acquired 2021.',own_y='2021',g='Asia'),
 bim('Kitty Bread','India','Indian bread brand, acquired 2021.',own_y='2021',g='Asia'),
 bim('Mankattan','China','Chinese bakery chain and brand (Mankattan Group), acquired 2018.',own_y='2018',g='Asia'),
]
S_ABF=WP+'Associated_British_Foods'
def abf(n,d,**kw):
    return E(n,d,S_ABF,own='Associated British Foods',**kw)
abfk=[
 abf('Kingsmill','Allied Bakeries sliced bread brand, owned by ABF.',tier='National champion',cty='United Kingdom',g='United Kingdom'),
 abf('Sunblest','Allied Bakeries bread brand, owned by ABF.',tier='National champion',cty='United Kingdom',g='United Kingdom'),
 abf('Allinson','Allied Bakeries wholemeal bread brand, owned by ABF.',tier='National champion',cty='United Kingdom',g='United Kingdom'),
 abf('Burgen','Allied Bakeries bread brand, owned by ABF.',tier='National champion',cty='United Kingdom',g='United Kingdom'),
 abf('Hovis','British bread brand; ABF\'s Allied Bakeries took it over from Endless for £75m, completed July 2026.',tier='National champion',cty='United Kingdom',own_y='2026',g='United Kingdom',role='landmark'),
 abf('Tip Top','Australian bakery brand founded 1949, owned through ABF\'s George Weston Foods.',tier='National champion',cty='Australia',y='1949',g='Australia'),
]
S_LAN=WP+'Lantm%C3%A4nnen'
lan=[E(n,d,S_LAN,own='Lantmännen',tier='Global group',cty='',g='Nordic and Baltic') for n,d in [
 ('Vaasan','Bakery brand listed among Lantmännen\'s food brands.'),
 ('Hatting','Bakery brand listed among Lantmännen\'s food brands.'),
 ('Bonjour','Bakery brand listed among Lantmännen\'s food brands.'),
 ('Korvbrödsbagarn','Hot-dog bread brand listed among Lantmännen\'s food brands.')]]
bar=[
 E('Mulino Bianco','Italian bakery brand of Barilla.',WP+'Barilla_Group',own='Barilla Group',tier='National champion',cty='Italy',g='Italy'),
 E('Harrys','French sliced-bread brand that Barilla kept when it sold Kamps to Agrofert in 2013.',WP+'Barilla_Group',own='Barilla Group',tier='National champion',cty='France',g='France'),
]
camp=[E('Pepperidge Farm','American bread and bakery brand, acquired by Campbell\'s in 1961.',WP+'Campbell_Soup_Company',own='Campbell\'s Company',tier='Global group',cty='United States',own_y='1961',g='United States')]
mars=[E('Pop-Tarts','Toaster pastry listed among Kellanova\'s brands; Kellanova was bought by Mars, completed 11 December 2025.',WP+'Kellanova',own='Mars',tier='Global group',cty='United States',own_y='2025',g='United States')]
# national champions
S_FL=WP+'Flowers_Foods'
fl=[E(n,d,S_FL,own='Flowers Foods',tier='National champion',cty='United States',own_y=oy,g='United States') for n,d,oy in [
 ('Wonder','US sliced-bread brand bought with the Hostess bread brands in 2013.','2013'),
 ('Dave\'s Killer Bread','US organic seeded bread brand, bought for $275m cash in 2015.','2015'),
 ('Nature\'s Own','US bread brand listed among Flowers Foods brands.',''),
 ('Tastykake','US snack-cake brand, bought in 2011.','2011'),
 ('Canyon Bakehouse','US gluten-free bread brand, bought in late 2018.','2018')]]
eur=[
 E('Warburtons','English family bakery of Bolton, founded 1876; leads UK branded plant bread with 47.2% in 2026.',WP+'Warburtons',own='Warburtons Holdings Limited',tier='National champion',cty='United Kingdom',y='1876',g='United Kingdom',role='landmark'),
 E('Mestemacher','German packaged wholegrain and pumpernickel bread maker from Gütersloh, founded 1871.',WP+'Mestemacher',own='Mestemacher',tier='Independent',cty='Germany',y='1871',g='Germany'),
 E('Pågen','Swedish bakery of Malmö founded 1878, known for Krisprolls and bread.',WP+'P%C3%A5gen',own='Pågen',tier='National champion',cty='Sweden',y='1878',g='Sweden'),
 E('Oululainen','Bakery brand of Fazer, the Finnish company founded 1891.',WP+'Fazer',own='Fazer',tier='National champion',cty='Finland',g='Finland'),
 E('Skogaholm','Bakery brand of Fazer.',WP+'Fazer',own='Fazer',tier='National champion',cty='',g='Finland'),
 E('Druva','Bakery brand of Fazer.',WP+'Fazer',own='Fazer',tier='National champion',cty='',g='Finland'),
]
asia=[
 E('Yamazaki Baking','Japanese bread maker founded 1948 in Ichikawa, controlled by the Iijima family.',WP+'Yamazaki_Baking',own='Yamazaki Baking',tier='National champion',cty='Japan',y='1948',g='Japan'),
 E('Fleischer\'s Bagels','US bagel brand bought by Yamazaki through Bakewise Brands in 2016.',WP+'Yamazaki_Baking',own='Yamazaki Baking',tier='Independent',cty='United States',own_y='2016',g='Japan'),
 E('Tom Cat Bakery','US bakery bought by Yamazaki through Bakewise Brands in 2016.',WP+'Yamazaki_Baking',own='Yamazaki Baking',tier='Independent',cty='United States',own_y='2016',g='Japan'),
]
afr=[
 E('Albany','South African bread brand of Tiger Brands, the company founded in 1921 as Tiger Oats.',WP+'Tiger_Brands',own='Tiger Brands',tier='National champion',cty='South Africa',g='South Africa'),
 E('Tinkies','South African snack-cake brand listed with Albany under Tiger Brands bakery.',WP+'Tiger_Brands',own='Tiger Brands',tier='National champion',cty='South Africa',g='South Africa'),
 E('SASKO','South African bread brand of Pioneer Foods, which PepsiCo acquired in 2020.',WP+'Pioneer_Foods',own='PepsiCo',tier='National champion',cty='South Africa',own_y='2020',g='South Africa'),
]
cake=[
 E('Twinkie',reuse='Twinkie',own='Hostess Brands',tier='National champion',cty='United States',g='United States'),
 E('Colin the Caterpillar',reuse='Colin the Caterpillar',own='Marks & Spencer',tier='Own label',cty='United Kingdom',g='United Kingdom'),
]
# craft
craft=[E('Poilâne','Paris bakery whose two-kilogram sourdough miche dates from 1932.',WP+'Poil%C3%A2ne',own='Poilâne',tier='Craft & indie',cty='France',y='1932',g='France',role='origin')]
LM=WP.replace('en.wikipedia.org/wiki/','')+'www.sustainweb.org/news/sep26-where-to-find-real-bread-sourdough-september-2026/'
LM='https://www.sustainweb.org/news/sep26-where-to-find-real-bread-sourdough-september-2026/'
WALES={'Blaenau Gwent','Caerphilly','Cardiff','Carmarthenshire','Ceredigion','Flintshire','Powys','Vale of Glamorgan','Wrexham'}
SCOT={'Aberdeenshire','Argyll & Bute','East Lothian','Edinburgh','Fife','Glasgow','Helmsdale','Highlands','Inverness-shire','Midlothian','Moray','North Ayrshire','Orkney','Perthshire','Scottish Borders'}
NI={'County Antrim','Derry / Londonderry'}
seen={}
lines=[l.rstrip('\n').split('|') for l in open('/home/user/Possession-Taxonomy/rebuild/work/V4_J8_SAVOURY/loafmark.txt')]
cnt={}
for n,loc,sec in lines: cnt[n]=cnt.get(n,0)+1
loaf=[];dups=0
for n,loc,sec in lines:
    key=(n,loc)
    if key in seen: dups+=1; continue
    seen[key]=1
    if sec=='UK':
        if loc in WALES: c='Wales'
        elif loc in SCOT: c='Scotland'
        elif loc in NI: c='Northern Ireland'
        elif loc=='County Donegal': c='Ireland'
        else: c='England'
        g=c
    else:
        g='Outside the UK'; c=loc.split(',')[-1].strip().replace('USA','United States')
    nm=n if cnt[n]==1 else f'{n} ({loc})'
    loaf.append(E(nm,f'Bakery in {loc} on the Loaf Mark licensee list compiled 1 September 2026.',LM,own=n,tier='Craft & indie',cty=c,g=g))
LOAF_N=len(lines); LOAF_D=len(loaf)
# protected
S_WD='https://www.wikidata.org/wiki/'
prot_bread=[
 E('Pane di Altamura',reuse='Pane di Altamura',g='Italy',role='origin'),
 E('Pane toscano',reuse='Pane toscano',g='Italy',s=S_WD+'Q62027701'),
 E('Pane casareccio di Genzano','Hearth bread of Genzano di Roma, Lazio, with PGI status.',S_WD+'Q3893172',y='PGI',g='Italy'),
 E('Pagnotta del Dittaino','Sicilian durum-wheat loaf with PDO status.',S_WD+'Q3360448',y='PDO',g='Italy'),
 E('Pane di Matera',reuse='Pane di Matera',g='Italy'),
 E('Coppia ferrarese',reuse='Coppia ferrarese',g='Italy',s=S_WD+'Q2996854'),
 E('Piadina romagnola',reuse='Piadina romagnola',g='Italy',s=S_WD+'Q926532'),
 E('Focaccia di Recco col formaggio','Two thin layers of dough with cheese from Recco, Liguria; PGI status.',S_WD+'Q3746935',y='PGI',g='Italy'),
]
prot_bake=[
 E('Aachener Printen',reuse='Aachener Printen',g='Germany',s=S_WD+'Q153254'),
 E('Nürnberger Lebkuchen',reuse='Nürnberger Lebkuchen',g='Germany'),
 E('Dresdner Stollen',reuse='Dresdner Stollen',g='Germany'),
 E('Toruń gingerbread',reuse='Toruń gingerbread',g='Poland'),
 E('Panforte di Siena','Dense fruit and nut cake of Siena; PGI status.',S_WD+'Q1278788',y='PGI',g='Italy'),
 E('Ricciarelli di Siena','Soft almond biscuit-cake of Siena; PGI status.',S_WD+'Q1059643',y='PGI',g='Italy'),
 E('Pastel de Tentúgal','Portuguese conventual pastry of very thin dough around egg-yolk filling, first made by Carmelite nuns in the 16th century; listed as IGP.',WP+'Pastel_de_Tent%C3%BAgal',g='Portugal'),
]
