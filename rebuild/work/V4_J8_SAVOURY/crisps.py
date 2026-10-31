from lib import *
FL=WP+'Frito-Lay'
def pep(n,d,cty,g,s=FL,own_y='',tier='Global group',**kw):
    return E(n,d,s,own='PepsiCo',tier=tier,cty=cty,own_y=own_y,g=g,**kw)
UKI='United Kingdom and Ireland'; LA='Mexico and Latin America'; WPW=WP+'Walkers_(snack_foods)'; SM=WP+'Smith%27s_Snackfood_Company'
pepsico=[
 pep("Lay's","First potato chip brand sold in all 50 US states, in 1965; Lay's Stax is its stacked version.",'United States','United States',y='1965',role='landmark',v=[V("Lay's Stax",'2003','stacked crisp made to compete with Pringles','PepsiCo')]),
 pep('Ruffles',"Ridged potato chip; Frito-Lay took the rights in 1958 and the UK version is Walkers Max.",'United States','United States',own_y='1958',reuse='Ruffles'),
 pep('Doritos',"First tortilla chip sold nationally in the US, launched 1966.",'United States','United States',reuse='Doritos',role='origin'),
 pep('Tostitos',"Tortilla chip developed 1978 and sold nationally by 1980.",'United States','United States',reuse='Tostitos'),
 pep('Fritos',"Corn chip, the original product of The Frito Company, 1932.",'United States','United States',reuse='Fritos'),
 pep('Cheetos',"Cheese-flavoured corn snack invented by Fritos creator Charles Elmer Doolin.",'United States','United States',reuse='Cheetos'),
 pep('Funyuns',"Onion-flavoured corn rings launched 1969.",'United States','United States',reuse='Funyuns'),
 pep('Munchos',"Potato-based crisp launched 1971.",'United States','United States',y='1971'),
 pep('Sun Chips',"Multigrain chip first sold 1991.",'United States','United States',y='1991'),
 pep('Smartfood',"Pre-popped cheese popcorn, acquired in the late 1980s.",'United States','United States',reuse='Smartfood'),
 pep('Cracker Jack',"Caramel popcorn and peanuts with a prize, acquired 1997.",'United States','United States',own_y='1997',reuse='Cracker Jack'),
 pep('Rold Gold',"Pretzel brand sold in North America.",'United States','United States',reuse='Rold Gold'),
 pep("Stacy's Pita Chips","Pita chip brand acquired by Frito-Lay.",'United States','United States'),
 pep("Miss Vickie's","Kettle-style chip brand listed among Frito-Lay brands.",'','United States'),
 pep('TrueNorth',"Nut clusters and nut crisps listed among Frito-Lay brands.",'','United States'),
 pep('Hostess (Canada)',"Canadian snack brand: Frito-Lay partnered with Hostess in 1987, merged in 1988 and took full ownership in 1992.",'Canada','Canada',own_y='1992'),
 pep('Sabritas',"Mexican snack brand, acquired 1966.",'Mexico',LA,own_y='1966'),
 pep('Poffets',"Local Sabritas snack brand in Mexico.",'Mexico',LA),
 pep('Rancheritos',"Local Sabritas snack brand in Mexico.",'Mexico',LA),
 pep('Crujitos',"Local Sabritas snack brand in Mexico.",'Mexico',LA),
 pep('Sabritones',"Local Sabritas snack brand in Mexico.",'Mexico',LA),
 pep('Elma Chips',"Brazilian snack company and brand within PepsiCo.",'Brazil',LA,tier='National champion'),
 pep('Fandangos',"Brazilian local snack brand.",'Brazil',LA),
 pep('Lucky',"Brazilian local snack brand.",'Brazil',LA),
 pep('Stiksy',"Brazilian local snack brand.",'Brazil',LA),
 pep("Pingo d'Ouro","Brazilian local snack brand.",'Brazil',LA),
 pep('Baconzitos',"Brazilian local snack brand.",'Brazil',LA),
 pep('Torcida',"Brazilian local snack brand.",'Brazil',LA),
 pep('ManiMoto',"Colombian local snack brand.",'Colombia',LA),
 pep('Pepito',"Venezuelan local snack brand.",'Venezuela',LA),
 pep('Savoy Brands',"Latin American snack group acquired 1998.",'',LA,own_y='1998'),
 pep('Walkers',"Leicester crisp maker founded 1948, owned by PepsiCo since 1989; 17.3% of Britain's savoury snacks in 2024.",'United Kingdom',UKI,s=WPW,own_y='1989',tier='National champion',role='landmark',y='1948',
     v=[V('Walkers Baked'),V('Walkers Max'),V('Walkers Sensations'),V('Walkers Sunbites')]),
 pep('Monster Munch',"British baked corn snack shaped like monsters' feet, a Walkers brand; Intersnack's Vico makes it in France.",'United Kingdom',UKI,s=WPW,reuse='Monster Munch',tier='National champion',v=[V('Monster Munch (France)','1998','sold by Vico','Intersnack')]),
 pep('Quavers',"Curly potato-based puff, a Walkers brand.",'United Kingdom',UKI,s=WPW,reuse='Quavers',tier='National champion'),
 pep('Wotsits',"British cheese-flavoured baked corn puff, a Walkers brand.",'United Kingdom',UKI,s=WPW,reuse='Wotsits',tier='National champion'),
 pep('Squares',"Walkers brand listed among its snacks.",'United Kingdom',UKI,s=WPW),
 pep('Frazzles',"Bacon-flavoured snack listed under Walkers and Smith's.",'United Kingdom',UKI,s=SM),
 pep('Smiths',"Crisp maker founded in Cricklewood in 1920; PepsiCo bought the UK business in 1989.",'United Kingdom',UKI,s=SM,y='1920',own_y='1989',tier='National champion',
     v=[V("Smith's Crisps"),V("Salt 'n' Shake"),V('Smiths (Netherlands)','1992',"phased out and replaced by Lay's in 2001",'PepsiCo')]),
 pep('Chipsticks',"UK Smiths snack.",'United Kingdom',UKI,s=SM),
 pep('Bacon Fries',"UK Smiths snack.",'United Kingdom',UKI,s=SM),
 pep('Scampi Fries',"UK Smiths snack.",'United Kingdom',UKI,s=SM),
 pep('Snaps',"UK Smiths snack.",'United Kingdom',UKI,s=SM),
 pep('Matutano',"Spanish and Portuguese snack subsidiary.",'Spain','Continental Europe'),
 pep('Duyvis',"European snack brand.",'','Continental Europe'),
 pep('Snack-a-Jacks',"European snack brand.",'','Continental Europe'),
 pep('Twistos',"European snack brand.",'','Continental Europe'),
 pep('Solinki',"European snack brand.",'','Continental Europe'),
 pep('Paw Ridge',"European snack brand.",'','Continental Europe'),
 pep('Star Chips',"Polish subsidiary snack brand.",'Poland','Continental Europe'),
 pep("Smith's (Australia)","Australian snack company; PepsiCo bought it in 1998. Its range includes Crinkle Cut, Thinly Cut and Red Rock Deli.",'Australia','Australia and India',s=SM,own_y='1998',tier='National champion',y='1932',
     v=[V("Smith's Crinkle Cut"),V("Smith's Thinly Cut"),V("Smith's Popped"),V('Red Rock Deli'),V('Burger Rings'),V("Nobby's"),V("Parker's"),V('Sakata'),V('Maxx'),V('Grain Waves'),V('Cool Pak Popcorn')]),
 pep('Twisties',"Australian cheese curl.",'Australia','Australia and India',s=SM,reuse='Twisties'),
 pep('Kurkure',"Indian spiced puffcorn launched 1999.",'India','Australia and India',reuse='Kurkure'),
 pep('Uncle Chipps',"Indian snack brand, bought out 2000.",'India','Australia and India',own_y='2000'),
]
mars=[E('Pringles',"Stacked crisps in a tube made from dried-potato dough, launched 1968 as Pringle's Newfangled Potato Chips.",WP+'Kellanova',reuse='Pringles',own='Mars',tier='Global group',cty='United States',own_y='2025',g='United States',role='origin')]
IS=WP+'Intersnack'; KPS=WP+'KP_Snacks'
def isn(n,d,cty,g,tier='Global group',s=IS,**kw): return E(n,d,s,own='Intersnack',tier=tier,cty=cty,g=g,**kw)
DA='Germany and Austria'
intersnack=[
 isn('funny-frisch',"Leading German crisp brand, created 1972 when Chipsfrisch merged with Pfanni's snack division.",'Germany',DA,tier='National champion',y='1972'),
 isn('Chio','German crisp brand begun in 1962 under the von Opel family.','Germany',DA,y='1962'),
 isn('Pom-Bär','Bear-shaped potato crisp created about 1987 in Germany; sold as Pom-Bear in the UK.','Germany',DA,reuse='Pom-Bear'),
 isn('Kelly','Austrian market leader in crisps, acquired 2007.','Austria',DA,tier='National champion',own_y='2007'),
 isn('Vico','French crisp and snack brand, acquired 1998.','France','France',own_y='1998',tier='National champion'),
 isn('Tayto',"First seasoned crisp, from Joe 'Spud' Murphy's Irish company; Intersnack reached 100% in 2015.",'Ireland',UKI,reuse='Tayto cheese and onion',tier='National champion',own_y='2015'),
 isn('KP Snacks','British snack maker bought from United Biscuits in December 2012 for about £500m.','United Kingdom',UKI,s=KPS,own_y='2012',tier='National champion',y='1853'),
 isn('Hula Hoops','Short hollow potato and corn rings, a KP Snacks brand.','United Kingdom',UKI,reuse='Hula Hoops',s=KPS),
 isn("McCoy's",'Crinkle-cut crisps, a KP Snacks brand.','United Kingdom',UKI,s=KPS),
 isn('Nik Naks','Corn snack, a KP Snacks brand.','United Kingdom',UKI,s=KPS),
 isn('Skips','Prawn-cocktail snack that melts on the tongue, a KP Snacks brand.','United Kingdom',UKI,reuse='Skips',s=KPS),
 isn('Space Raiders','Corn snack, a KP Snacks brand.','United Kingdom',UKI,s=KPS),
 isn('Discos','Crisp, a KP Snacks brand.','United Kingdom',UKI,s=KPS),
 isn('Frisps','Crisp, a KP Snacks brand.','United Kingdom',UKI,s=KPS),
 isn('Wheat Crunchies','Wheat snack, a KP Snacks brand.','United Kingdom',UKI,s=KPS),
 isn('Butterkist','Popcorn brand of KP Snacks.','United Kingdom',UKI,reuse='Butterkist',s=KPS),
 isn('Penn State','Intersnack snack brand named on its page.','',UKI),
 isn('Bohemia','Intersnack brand named on its page.','',DA),
 isn('Tyrrells','Hand-cooked crisps from Herefordshire, bought by Intersnack in 2018.','United Kingdom',UKI,own_y='2018'),
 isn('Popchips','Popped-chip brand listed on the Intersnack page.','',UKI),
 isn('Estrella','Nordic snack brand, from the 2014 Estrella Maarud deal.','','Nordic',own_y='2014'),
 isn('Maarud','Scandinavian snack brand, from the 2014 Estrella Maarud deal.','','Nordic',own_y='2014'),
 isn("Griffin's Foods",'Snack maker of Australia and New Zealand via Unisnack ANZ; Intersnack took full control in August 2021.','Australia and New Zealand','Australia and New Zealand',own_y='2021'),
 isn('Snack Brands Australia','Australian snack maker via Unisnack ANZ; Intersnack took full control in August 2021.','Australia','Australia and New Zealand',own_y='2021'),
]
CB=WP+'Calbee'
def cal(n,d,cty,g,tier='Global group',s=CB,**kw): return E(n,d,s,own='Calbee',tier=tier,cty=cty,g=g,**kw)
calbee=[
 cal('Calbee Potato Chips',"Calbee's potato chips, on sale from 1975; about 70% of Japan's potato chip market.",'Japan','Japan',tier='National champion',y='1975',role='landmark'),
 cal('Calbee Caramel',"Calbee's first product, from 1949.",'Japan','Japan',y='1949',role='origin'),
 cal('Kappa Ebisen','Japanese shrimp cracker stick, launched 1964; first exported to Hawaii and Southeast Asia in 1966.','Japan','Japan',reuse='Kappa Ebisen'),
 cal('Jagariko','Potato stick snack, launched 1995.','Japan','Japan',y='1995'),
 cal('Jagabee','Whole unhusked potato snack.','Japan','Japan'),
 cal('Jaga Pokkuru','Potato snack sold as a souvenir in Hakodate, Hokkaido.','Japan','Japan'),
 cal('Sapporo Potato','Wheat-based snack.','Japan','Japan'),
 cal('Seabrook','British crisps bought by Calbee in 2018.','United Kingdom','Overseas',own_y='2018'),
 cal('Warnock Food Products','Snack maker bought by Calbee in 2019 from BGL.','','Overseas',own_y='2019'),
 cal('Frito-Lay Japan','Japanese Frito-Lay company, a Calbee subsidiary since 2009 through the PepsiCo alliance.','Japan','Japan',own_y='2009'),
 E('Potabee','Indonesian potato chip brand from the 2014 Calbee and Wings Food joint venture.',WP+'List_of_potato_chip_brands',own='PT Calbee-Wings Food',tier='Global group',cty='Indonesia',y='2014',g='Overseas'),
]
CP=WP+'Campbell_Soup_Company'
def cam(n,d,s=CP,**kw): return E(n,d,s,own="Campbell's Company",tier='Global group',cty='United States',own_y='2018',g='United States',**kw)
campbell=[
 cam("Snyder's of Hanover","Pennsylvania pretzel snacks; part of Snyder's-Lance, bought by Campbell's in early 2018 for US$4.87bn.",reuse="Snyder's of Hanover"),
 cam('Lance',"Snack brand of Snyder's-Lance, bought by Campbell's in early 2018."),
 cam('Kettle Brand',"Oregon kettle chips founded 1977 in Salem; Campbell's took it with Snyder's-Lance in March 2018.",s=WP+'Kettle_Foods',role='origin',v=[V('Kettle Chips (Europe)','2019','European business','Valeo Foods')]),
 cam('Cape Cod',"Cape Cod Potato Chips, part of Snyder's-Lance."),
 cam('Snack Factory',"Pretzel Crisps brand of Snyder's-Lance."),
 cam('Late July',"Organic snack brand; Snyder's-Lance raised its stake to 80% in 2014 and Campbell's took it in 2018."),
]
GM=WP+'General_Mills'
gmc=[E(n,d,GM,own='General Mills',tier='Global group',cty='United States',g='United States',**kw) for n,d,kw in [
 ('Bugles','Cone-shaped corn snack of General Mills.',dict(reuse='Bugles')),
 ('Chex Mix','Seasoned cereal, pretzel and bagel-chip snack mix of General Mills.',{}),
 ("Gardetto's",'Snack mix and bagel chips of General Mills.',{})]]
bimbo_snk=[
 E('Barcel','Mexican snack company of Grupo Bimbo, operating since 1971.',WP+'Grupo_Bimbo',own='Grupo Bimbo',tier='Global group',cty='Mexico',y='1971',g='Mexico'),
 E('Takis','Rolled tortilla chip with intense chilli flavour, made by Barcel; launched 1999.',WP+'Takis',reuse='Takis',own='Grupo Bimbo',tier='Global group',cty='Mexico',g='Mexico'),
 E('Popcornopolis','American popcorn brand, acquired by Bimbo in 2021.',WP+'Grupo_Bimbo',own='Grupo Bimbo',tier='Global group',cty='United States',own_y='2021',g='United States'),
]
FN='https://www.foodnavigator.com/Article/2026/01/29/worlds-biggest-snack-companies-in-2026-ranked/'
hersh=[E(n,d,FN,own='The Hershey Company',tier='Global group',cty='United States',g='United States') for n,d in [('SkinnyPop',"Popcorn brand named among Hershey's key brands (2026 FoodNavigator ranking)."),("Dot's Pretzels","Seasoned pretzel brand named among Hershey's key brands (2026 FoodNavigator ranking).")]]
PC=WP+'List_of_potato_chip_brands'
def pcb(n,d,cty,g,own='owner not stated',tier='National champion',s=PC,**kw): return E(n,d,s,own=own,tier=tier,cty=cty,g=g,**kw)
IR='Ireland, Russia and Israel'
europe=[
 pcb('Hunky Dorys','Irish crisp brand named on the potato chip brands page.','Ireland',IR),
 pcb('King','Irish crisp brand named on the potato chip brands page.','Ireland',IR),
 pcb('Russkaya Kartoshka','Russian crisp brand named on the potato chip brands page.','Russia',IR),
 pcb('Just Brutal','Russian crisp brand sold at Fix Price stores.','Russia',IR),
 E('Crunchips','German potato crisp range of Lorenz Snack-World, the Bahlsen company founded 1999 in Offenbach.',WP+'Lorenz_Snack-World',own='Lorenz Snack-World',tier='Independent',cty='Germany',g=IR),
 E('Bamba','Israeli peanut-butter-flavoured puffed maize snack, launched 1964.',WP+'Bamba_(snack)',reuse='Bamba',own='Osem',tier='National champion',cty='Israel',g=IR),
]
BS='https://www.bakeryandsnacks.com/Article/2017/02/24/Savory-snacks-in-China-expected-to-reach-16.6bn-by-2021-Euromonitor'
EA='East Asia'; SA='South and Southeast Asia'
asia=[
 E('Koikeya','Japanese snack maker founded 1958; second-largest potato chip maker in Japan as of 2019.',WP+'Koikeya',own='Koikeya',tier='National champion',cty='Japan',y='1958',g=EA),
 E('Pretz','Japanese pretzel sticks.',WP+'Pretzel',reuse='Pretz',own='Glico',tier='National champion',cty='Japan',g=EA),
 E('Happy Turn','Rice cracker from Kameda Seika.','https://kamedaseika.co.jp/en/company/rice-cracker-business',reuse='Happy Turn',own='Kameda Seika',tier='National champion',cty='Japan',g=EA),
 E('Want Want','Taiwanese food maker founded 1962 in Yilan County, best known for rice crackers; first in China savoury snacks with 9.9% in 2016.',WP+'Want_Want',own='Want Want',tier='National champion',cty='Taiwan',y='1962',g=EA,role='landmark'),
 E('Nongshim','South Korean food maker founded 1965; its snacks include Shrimp Crackers and Onion Rings.',WP+'Nongshim',own='Nongshim',tier='National champion',cty='South Korea',y='1965',g=EA),
 E('Saeukkang',"South Korea's first commercialised packaged snack, a shrimp cracker launched 1971.",WP+'Nongshim',reuse='Saeukkang',own='Nongshim',tier='National champion',cty='South Korea',g=EA,role='origin'),
 E('Orion',"Savoury snack maker with 4.2% of China's savoury snack value in 2016.",BS,own='Orion',tier='National champion',cty='',g=EA),
 E('Hefei Huatai Food',"Chinese savoury snack maker with 3.4% of China's savoury snack value in 2016.",BS,own='Hefei Huatai Food',tier='National champion',cty='China',g=EA),
 E('Shanghai Liwayway Food',"Savoury snack maker with 2.8% of China's savoury snack value in 2016.",BS,own='Shanghai Liwayway Food',tier='National champion',cty='China',g=EA),
 E('Fujian Dali Food',"Chinese food maker with 2.4% of China's savoury snack value in 2016.",BS,own='Fujian Dali Food',tier='National champion',cty='China',g=EA),
 E('Three Squirrels',"Chinese nut and snack brand with 2.3% of China's savoury snack value in 2016.",BS,own='Three Squirrels',tier='National champion',cty='China',g=EA),
 E("Jack 'n Jill",'Hong Kong barbecue-flavoured chip brand named on the potato chip brands page.',PC,own='owner not stated',tier='National champion',cty='Hong Kong',g=EA),
 E("Haldiram's","Indian snack and sweet maker founded 1937 in Bikaner; ranked India's largest snack company in 2017.",WP+'Haldiram%27s',own="Haldiram's India Pvt Ltd",tier='National champion',cty='India',y='1937',g=SA,role='landmark'),
 E('Balaji Wafers','Indian chips and namkeen maker from Rajkot, started 1974; 13.7% of local chips in 2012.',WP+'Balaji_Wafers',own='Balaji Wafers Private Limited',tier='National champion',cty='India',y='1974',g=SA),
 E('Chitato','Indonesian potato chip brand owned by Indofood.',PC,own='Indofood',tier='National champion',cty='Indonesia',g=SA),
 E('Chiki','Indonesian snack brand the Frito-Lay page lists as produced by Indofood.',FL,own='Indofood',tier='National champion',cty='Indonesia',g=SA),
 E('Qtela','Indonesian snack brand the Frito-Lay page lists as produced by Indofood.',FL,own='Indofood',tier='National champion',cty='Indonesia',g=SA),
 E('Maxicorn','Indonesian snack brand the Frito-Lay page lists as produced by Indofood.',FL,own='Indofood',tier='National champion',cty='Indonesia',g=SA),
 E('JetZ','Indonesian snack brand the Frito-Lay page lists as produced by Indofood.',FL,own='Indofood',tier='National champion',cty='Indonesia',g=SA),
]
UZ=WP+'Utz_Brands'
def utz(n,d,oy,**kw): return E(n,d,UZ,own='Utz Brands',tier='Independent',cty='United States',own_y=oy,g='United States',**kw)
usind=[
 E('Utz','Hanover, Pennsylvania chip maker founded 1921 as Hanover Home Brand Potato Chips; Intersnack agreed to buy Utz Brands in July 2026.',UZ,own='Utz Brands',tier='Independent',cty='United States',y='1921',g='United States'),
 E("Herr's",'Pennsylvania chip maker founded 1946 by Jim Herr, privately held; sold in all 50 states.',WP+'Herr%27s',own="Herr's",tier='Independent',cty='United States',y='1946',g='United States'),
 utz("Zapp's",'Louisiana kettle-chip brand, bought with Zappe Endeavors in 2011.','2011'),
 utz('Wachusett Potato Chip Company','Massachusetts chip maker, bought in 2011.','2011'),
 utz('Bachman','Pretzel and chip brand: Utz bought the intellectual property and Ephrata plant in 2012.','2012'),
 utz('Golden Flake','Alabama snack brand, bought in 2016.','2016'),
 utz('Boulder Canyon','Kettle-cooked chip brand, bought with Inventure Foods in December 2017.','2017'),
 utz('Snyder of Berlin','Pennsylvania snack maker, bought in October 2019.','2019'),
 utz('On the Border','Tortilla chip brand, bought with Truco Enterprises in 2020.','2020'),
 utz("Vitner's",'Snack brand, acquisition announced January 2021.','2021'),
 utz('R.W. Garcia','Tortilla chip maker, bought in December 2021.','2021'),
 pcb('Old Dutch','Minneapolis regional chip brand named on the potato chip brands page.','United States','United States',tier='Independent'),
 pcb('Jays','Chicago regional chip brand named on the potato chip brands page.','United States','United States',tier='Independent'),
 pcb('Better Made','Detroit regional chip brand named on the potato chip brands page.','United States','United States',tier='Independent'),
 pcb('Mikesells','Dayton regional chip brand named on the potato chip brands page.','United States','United States',tier='Independent'),
 pcb("Martin's Potato Chips",'Pennsylvania chip brand named on the potato chip brands page.','United States','United States',tier='Independent'),
 pcb('Charles Chips','Pennsylvania chip brand named on the potato chip brands page.','United States','United States',tier='Independent'),
 E('Wise Foods','US snack maker; Cheez Doodles are its East Coast cheese puff first made in the Bronx.',WP+'Cheez_Doodles',reuse='Cheez Doodles',own='Wise Foods',tier='Independent',cty='United States',g='United States'),
 E("Orville Redenbacher's",'American popping-corn brand fronted by its founder, 1969; listed earlier under Conagra Brands.',WP+'Orville_Redenbacher%27s',reuse="Orville Redenbacher's",own='Conagra Brands',tier='Independent',cty='United States',g='United States'),
 E('Jolly Time','Brand of the oldest US popcorn producer, the American Pop Corn Company, 1914.',WP+'American_Pop_Corn_Company',reuse='Jolly Time',own='American Pop Corn Company',tier='Independent',cty='United States',g='United States'),
 E('Pop Secret',"Microwave popcorn brand that Campbell's sold to Our Home in August 2024.",CP,own='Our Home',tier='Independent',cty='United States',own_y='2024',g='United States'),
 E("President's Choice","Loblaw's own-label brand, with crisps among its lines.",PC,own='Loblaw',tier='Own label',cty='Canada',g='Canada'),
]
LF='https://www.lovefood.com/news/57693/top-five-british-crisp-producers'
crafts=[
 E('Burts','Devon crisps cooked by hand in small batches.',LF,own='Burts',tier='Craft & indie',cty='United Kingdom',g='United Kingdom'),
 E('Fairfields Farm Crisps','Essex crisps grown, washed and cooked on one Colchester farm.',LF,own='Fairfields Farm Crisps',tier='Craft & indie',cty='United Kingdom',g='United Kingdom'),
 E('Corkers','Hand-cooked crisps from Fenland potatoes, run by Rod Garnham and Ross Taylor.',LF,own='Corkers',tier='Craft & indie',cty='United Kingdom',g='United Kingdom'),
 E('Yorkshire Crisps','Batch-fried Sheffield-area crisps, established 2005 by farmer Ashley Turner.',LF,own='Yorkshire Crisps',tier='Craft & indie',cty='United Kingdom',y='2005',g='United Kingdom'),
]
for e in pepsico:
    if e['n']=='Walkers': e['mk']='PepsiCo'
