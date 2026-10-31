from lib import *
GMS=WP+'General_Mills'; KEL=WP+'Kellanova'
gmb=[
 E('Nature Valley','US granola bar brand; the bar was introduced in 1973.',WP+'Nature_Valley',own='General Mills',tier='Global group',cty='United States',y='1973',g='United States',
   v=[V('Oats and Honey'),V('Fruit and Nut'),V('Peanut'),V('Protein bar')]),
 E('Fiber One','Fibre bar brand of General Mills.',GMS,own='General Mills',tier='Global group',cty='United States',g='United States'),
 E('Lärabar','Fruit and nut bar listed among General Mills\' North American brands.',GMS,own='General Mills',tier='Global group',cty='United States',g='United States'),
 E('Cascadian Farms','Organic brand whose grain snacks are listed under General Mills snacks.',GMS,own='General Mills',tier='Global group',cty='United States',g='United States'),
]
marsb=[
 E('KIND','New York snack bar company founded 2004 by Daniel Lubetzky; Mars bought a minority stake in 2017 and took full ownership in 2020.',WP+'Kind_(company)',own='Mars',tier='Global group',cty='United States',y='2004',own_y='2020',g='United States',
   v=[V('Kind Fruit & Nut'),V('Kind Plus'),V('Strong & Kind'),V('Kind Breakfast')]),
 E('RXBAR','Protein bar listed among Kellanova brands.',KEL,own='Mars',tier='Global group',cty='United States',own_y='2025',g='United States'),
 E('Rice Krispies Treats','Marshmallow cereal bar listed among Kellanova brands.',KEL,own='Mars',tier='Global group',cty='United States',own_y='2025',g='United States'),
 E('Nutri-Grain','Breakfast bar listed among Kellanova brands.',KEL,own='Mars',tier='Global group',cty='United States',own_y='2025',g='United States'),
 E('Special K','Snack bars listed among Kellanova brands.',KEL,own='Mars',tier='Global group',cty='United States',own_y='2025',g='United States'),
 E('Bear Naked','Granola and bar brand listed among Kellanova brands.',KEL,own='Mars',tier='Global group',cty='United States',own_y='2025',g='United States'),
 E('Pure Organic','Fruit bar brand listed among Kellanova brands.',KEL,own='Mars',tier='Global group',cty='United States',own_y='2025',g='United States'),
]
mond=[
 E('Clif Bar','Energy bar from Emeryville, California, founded 1992; Mondelez agreed to buy the company for $2.9bn in 2022.',WP+'Clif_Bar_%26_Company',own='Mondelez International',tier='Global group',cty='United States',y='1992',own_y='2022',g='United States',v=[V('Luna Bar','','bar marketed to women')]),
]
pepb=[
 E('Quaker Chewy','Chewy granola bars, under Frito-Lay North America after the 2001 Quaker merger.',WP+'Frito-Lay',own='PepsiCo',tier='Global group',cty='United States',own_y='2001',g='United States'),
 E('Quaker rice cakes','Rice cakes under Frito-Lay North America after the 2001 Quaker merger.',WP+'Frito-Lay',own='PepsiCo',tier='Global group',cty='United States',own_y='2001',g='United States'),
]
inter=[
 E('ültje','German nut brand that came with Intersnack\'s 2008 merger with the Nut Company.',WP+'Intersnack',own='Intersnack',tier='Global group',cty='Germany',own_y='2008',g='Germany'),
 E('KP Nuts','British nut brand of KP Snacks, bought by Intersnack in 2012.',WP+'KP_Snacks',own='Intersnack',tier='Global group',cty='United Kingdom',own_y='2012',g='United Kingdom'),
]
abfn=[E('Jordans','Cereal and bar brand owned by ABF.',WP+'Associated_British_Foods',own='Associated British Foods',tier='Global group',cty='United Kingdom',g='United Kingdom')]
EB=WP+'Energy_bar'
ind=[
 E('Planters','Peanut and mixed-nut brand founded 1906 in Wilkes-Barre; Hormel bought it from Kraft Heinz for $3.35bn in 2021.',WP+'Planters',own='Hormel Foods',tier='National champion',cty='United States',y='1906',own_y='2021',g='United States',
   v=[V('Dry roasted peanuts'),V('Honey roasted peanuts'),V('Deluxe mixed nuts'),V('CornNuts','','acquired in the late 1990s')]),
 E('Blue Diamond','Californian almond cooperative founded 1910 as the California Almond Growers\' Exchange, serving about 3,500 growers.',WP+'Blue_Diamond_Growers',own='Blue Diamond Growers',tier='National champion',cty='United States',y='1910',g='United States',
   v=[V('Almond Breeze'),V('Nut-Thins')]),
 E('Graze','London snack company founded 2007; Unilever bought it in 2019 and Candy Kittens was named buyer in December 2025.',WP+'Graze_(company)',own='Candy Kittens',tier='Independent',cty='United Kingdom',y='2007',own_y='2025',g='United Kingdom'),
 E('Quest Nutrition','Protein bar, chip and cookie brand.','https://www.questnutrition.com/collections/protein-bars',own='owner not stated',tier='Independent',cty='United States',g='United States'),
 E('PowerBar','Energy bar named on the energy bar page.',EB,own='owner not stated',tier='Independent',cty='',g='Energy bars'),
 E('Balance Bar','Bar named on the energy bar page.',EB,own='owner not stated',tier='Independent',cty='',g='Energy bars'),
 E('CalorieMate','Bar named on the energy bar page.',EB,own='owner not stated',tier='Independent',cty='',g='Energy bars'),
 E('Odwalla Bar','Bar named on the energy bar page.',EB,own='owner not stated',tier='Independent',cty='',g='Energy bars'),
 E('Soldier Fuel','Bar named on the energy bar page.',EB,own='owner not stated',tier='Independent',cty='',g='Energy bars'),
 E("Tiger's Milk",'Bar named on the energy bar page.',EB,own='owner not stated',tier='Independent',cty='',g='Energy bars'),
 E('ZonePerfect','Bar named on the energy bar page.',EB,own='owner not stated',tier='Independent',cty='',g='Energy bars'),
]
nocc=E('Nocciola Piemonte IGP','Hazelnut of Piedmont with PGI status.','https://www.wikidata.org/wiki/Q3993016',y='PGI',g='Italy')
