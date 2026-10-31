# -*- coding: utf-8 -*-
W="https://en.wikipedia.org/wiki/"
NOODLES = """Acecook|Japan|Acecook|Founded 1948; large Southeast Asian subsidiaries; top brand in Vietnam
Ajinomen|Peru|Ajinomoto del Perú S.A.|Peruvian brand
Amino|Poland|Unilever|Noodles, ready meals and sauces; founded in the 1970s
Annie Chun's||CJ CheilJedang|American-market Asian food brand
Ansungtangmyun|South Korea|Nongshim|Ramyeon since 1983; third-highest seller in 2014
A-Sha Noodles|Taiwan|Asha Foods|Dry noodles; gained international attention in 2020
Bakmi Mewah|Indonesia|Mayora Indah|Asian-style noodles
Buitoni Instant Noodles|Italy|Buitoni (Nestlé)|Now sold as Maggi Noodles
Cham-ggae Ramyeon|South Korea|Ottogi|Dried noodle block with seasoning, oil, sesame and an egg-and-vegetable block
Chapagetti|South Korea|Nongshim|Since 1984; first instant jajangmyeon in Korea
Ching's Secret|India|Capital Foods|Indian Chinese cuisine ingredients and ready meals
Dosirac|South Korea|Korea Yakult (Paldo)|Since 1986; popular in Russia
Foodles|India|Haleon|Launched in India in 2010 under GSK
Hot Chicken Flavor Ramen|South Korea|Samyang Foods|Spicy chicken-flavoured ramen
Ho-Mi|Philippines|Uni-President Philippines Corporation|Filipino brand
Imperial Big Meal|Taiwan|Uni-President Enterprises|Beef noodle soup with real meat chunks
Intermi|Indonesia|Indofood Sukses Makmur|Indonesian brand
Jin Ramen|South Korea|Ottogi|Korean brand
KiKi Noodles|Taiwan|KiKi Fine Goods|Taiwanese brand
Knorr Instant Noodles|India|Unilever|Made in India, Pakistan and Poland
Koka Instant Noodles|Singapore|Tat Hui Foods|Sold domestically and internationally
La Choy Chow Mein Noodles|United States|La Choy|American brand
Lemonilo|Indonesia|Lemonilo|Health-focused brand founded in 2016
Maggi Cuppa Mania||Nestlé|Cup product
Mamee Chef|Malaysia||Malaysian brand
Migelas|Indonesia|Mayora Indah|Indonesian brand
Mie Oven|Indonesia|Mayora Indah|Indonesian brand
Mr. Noodles|Canada|Anderson Watts Limited|Imported by Anderson Watts and made in Guangdong
Neoguri|South Korea|Nongshim|Since 1982; exported to over 80 countries
Nissin Noodles (Kenya)|Kenya|Nissin Foods|Sold in Kenya
Paldo Bibim Men|South Korea|Korea Yakult (Paldo)|Brothless ramyeon since 1984
Patanjali Atta Noodles|India|Patanjali Ayurved|Wheat-based instant noodles
Payless|Philippines|Universal Robina|Filipino brand
Pop Mie|Indonesia|Indofood|Cup noodles
Prima Taste||Prima Food|Premium instant noodles
Prince Noodles|Taiwan|Ve Wong Corporation|Taiwanese brand
Quickchow|Philippines|Zest-O Corporation|Filipino brand
Saikebon|Italy|Star (GBfoods)|Popular in Italy
Sakura|Indonesia|Indofood Sukses Makmur|Indonesian brand
Samyang Ramen|South Korea|Samyang Foods|First ramyeon brand in South Korea
Sarimi|Indonesia|Indofood Sukses Makmur|Introduced 1982
Science Noodles|Taiwan|Uni-President Enterprises|Taiwanese brand
Shoop Instant Noodles|Pakistan|Shan Foods|Made in Pakistan since 2012
Smith & Jones instant noodles|India|Capital Foods Ltd|Made in India for domestic and export markets
Tekki Shomen|Philippines|Zest-O Corporation|Filipino brand
Tekki Yakiudon|Philippines|Zest-O Corporation|Filipino brand
Tong Yi (統一)|Taiwan|Uni-President Enterprises|Taiwanese brand
Top Ramen|United States|Nissin Foods|Sold in the US since 1972; Nissin's first overseas launch
TTL Hua Tiao Chicken Noodles|Taiwan|Taiwan Tobacco and Liquor Corporation|Taiwanese brand
Wei Lih Men|Taiwan|Wei Lih Food Industrial Co.|Made in Taiwan since 1973
Supermi|Indonesia|PT Lima Satu Sankyo|Early brand, introduced 1969
Charumera|Japan|Myōjō Foods|Japanese brand
Super Cup|Japan|Acecook|Japanese brand
Akai Kitsune|Japan|Tōyō Suisan|Product under the Maruchan brand
Midori no Tanuki|Japan|Tōyō Suisan|Product under the Maruchan brand
Mivina|Ukraine|Technocom|First Ukrainian brand, 1995
Big Bon|Ukraine|Mareven Food Europe|Ukrainian brand
Thai Chef|Hungary|Thai President Foods|Made in Hungary for the European market
Asia Gold|Hungary|Thai President Foods|Made in Hungary for the European market
De-Royal Instant Noodles|Nigeria|Royal Mills and Foods Limited|Launched 2013
Gaga|Indonesia|Jakarana Tama|Indonesian brand
Arirang|Indonesia|Jakarana Tama|Indonesian brand
Kkoburang guksu|North Korea||First local ramyeon brand, from 2000
Doll Noodles|Hong Kong|Winner Food Products|Generic term for instant noodles in Hong Kong; bought by Nissin in 1984
Good Good Eat Noodles|Taiwan|Wei Lih|Wei Lih product"""
SPLIT = """Toor dal|Split pigeon pea|Also called arhar dal; main ingredient of sambar
Chana dal|Split black chickpea|Made by removing the outer layer and splitting
Kabuli dal|Split kabuli chickpea|Made from the kabuli chickpea variety
Yellow split pea dal|Split yellow pea|Most popular dal in Indian diaspora communities
Mung dal|Split mung bean|Most popular in Bangladesh and West Bengal
Urad dal|Split black gram|Used in idli, dosa and bori, and in dal makhani
Masoor dal|Split red lentil|Called kempu togari bele in Karnataka
Rajma dal|Split kidney bean|Listed as a split form of kidney beans
Moth bean dal|Split moth bean|Ingredient in bikaneri bhujia, misal and usal
Panchratna dal|Mixture of five dals|The five-jewel blend
Navrangi dal|Multicoloured mix|Lesser-known variety from Himachal Pradesh
Mussyang|Mixed dals|Mixed-colour dal from the hilly regions of Nepal
Chilka dal|Split, unhulled pulse|Split but not hulled; chilka means skin
Dhuli dal|Hulled split pulse|Hulled and split; dhuli means washed"""
HOPS = """Admiral|England|bittering|
Ahtanum|United States|aroma|
Amarillo|United States||
Apollo|United States||
Bramling Cross|England|dual|1951
Brewer's Gold|England|bittering|1919
Bullion|England|bittering|1919
Crystal|United States|aroma|1993
Eroica|United States|bittering|1979
First Gold|England||1995
Feux-Coeur Francais|Australia||2010
Galena|United States||1968
Glacier|United States||
Green Bullet|New Zealand|bittering|1972
Greensburg|United States||
Herald|England|dual|
Herkules|Germany|bittering|2005
Hersbrucker|Germany|aroma|
Horizon|United States||1970
Liberty|United States|aroma|1983
Lublin|Poland|aroma|
Merkur|Germany|bittering|
Millennium|United States||
Mosaic|United States||
Mount Hood|United States|aroma|
Mount Rainier|United States||
Newport|United States|bittering|
Northdown|England|dual|1970s
Nugget|United States|bittering|
Opal|Germany|aroma|
Pacifica|New Zealand|bittering|1994
Pacific Gem|New Zealand|bittering|1987
Pacific Jade|New Zealand|bittering|
Palisade|United States|aroma|
Phoenix|England|dual|
Pilgrim|England|dual|2000
Pilot|England||2002
Pioneer|England||
Polnischer Lublin|Poland||
Pride of Ringwood|Australia|bittering|1953
Progress|England||1960s
Riwaka|New Zealand|aroma|1997
Saaz Late|Czech Republic||
Bor|Czech Republic|aroma|
Premiant|Czech Republic|aroma|
Rubin|Czech Republic||
Agnus|Czech Republic||
Vital|Czech Republic||
Sladek|Czech Republic||
Kazbek|Czech Republic||
Bohemie|Czech Republic||
Harmonie|Czech Republic||
San Juan Ruby Red|United States|aroma|
Santiam|United States|aroma|
Saphir|Germany|aroma|
Satus|United States|bittering|
Select|Germany||
Smaragd|Germany||
Sorachi Ace|Japan|dual|
Southern Cross|New Zealand|bittering|
Spalt|Germany|aroma|
Sterling|United States|aroma|1998
Strisselspalt|France|aroma|
Styrian Aurora|Slovenia||
Styrian Bobek|Slovenia|aroma|
Styrian Goldings|Slovenia||
Styrian Celeia|Slovenia|aroma|
Summit|United States||
Tardif de Bourgogne|France|aroma|
Taurus|Germany|bittering|
Tomahawk|United States|bittering|
Tomyski|Poland|aroma|
Tradition|Germany||1991
Ultra|United States|aroma|1995
Vanguard|United States|aroma|1982
Waimea|New Zealand|dual|2012
Warrior|United States|bittering|
Whitbread Golding Variety|England||1911
Willamette|United States|aroma|1976
Zeus|United States||
Cluster|United States||
Eroica|United States|bittering|1979
Galaxy|Australia|dual|1994
Pacific Gem|New Zealand|bittering|1987"""
HOT = """Blair's Death Sauce|United States|Blair's Sauces and Snacks
Búfalo Jalapeño Mexican Hot Sauce|Mexico|
Da'Bomb|United States|
Dave's Gourmet Insanity Sauce|Costa Rica|Dave's Gourmet
El Pato|Mexico|
Endorphin Rush Beyond Hot Sauce|United States|
Indofood Sambal|Indonesia|Indofood
Mad Dog 357|United States|Ashley Food Company
Maga|Mexico|
Mezzetta California Habanero Hot Sauce|United States|Mezzetta
Nali Sauce|Malawi|
Nerpy's Hot Sauce|Canada|Nerpy's
Pickapeppa Sauce|Jamaica|
San Diego Pepper Company sauces|United States|San Diego Pepper Company
Scorpion Bay Hot Sauce|United States|
Taco Bell sauces|United States|Taco Bell
Tamazula|Mexico|
Texas Pete|United States|
Toad Sweat dessert hot sauces|United Kingdom|
Trappey's|United States|Trappey's
Maria Avvacato's Apocalypse Scorpion Hot Sauce|United States|"""
OLIVES = """Aglandau|France, Australia, Azerbaijan, Ukraine|table
Aloreña|Spain|table
Amfissa|Greece|both
Arbequina|Spain|both
Arbosana|Spain|oil
Ascolano|Italy|both
Ayvalık|Turkey|oil
Azeradj|Algeria|oil
Barnea|Israel|both
Beldi|Morocco|table
Biancolilla|Italy|oil
Bidni|Malta|oil
Bosana|Italy|oil
Bouteillan|France|oil
Cailletier|France, Italy|table
Calabria|Italy|
Canino|Italy|
Carolea|Italy|oil
Casaliva|Italy|
Castelvetrano|Italy|both
Cayon|France|oil
Cellina di Nardo|Italy|
Cerasuola|Italy|oil
Cerignola|Italy|table
Chemlali|Tunisia|
Chetoui|Tunisia|
Cobrançosa|Portugal|
Conservolea|Greece|table
Coratina|Italy, Croatia|oil
Cornicabra|Spain|oil
Domat|Turkey|both
Dritta|Italy|oil
Empeltre|Spain|both
Frantoio|Italy|oil
Galega|Portugal|
Gemlik|Turkey|table
Gentile di Chieti|Italy|
Germaine|France, Italy|both
Gordal|Spain|table
Grossane|France|
Halkidiki|Greece|table
Hojiblanca|Spain|oil
Hondroelia|Greece|table
İzmir Sofralık|Turkey|oil
Kalamata|Greece|table
Koroneiki|Greece|oil
Kothreiki|Greece|both
Lechín de Sevilla|Spain|oil
Leccino|Italy|oil
Lugano|Italy|
Lucques|France|
Maalot|Israel|oil
Manzanilla|Spain|table
Mastoidis|Greece|table
Megaritiki|Greece|both
Memecik|Turkey|
Memeli|Turkey|both
Meslalla|Morocco|both
Mission|United States|table
Morrut|Spain|oil
Nabali|Israel|
Nafplion|Greece|table
Nocellara del Belice|Italy|both
Nocellara Etnea|Italy|oil
Nyons|France|
Oliana|Spain|
Olivière|France|
Patrinia|Greece|
Picholine|France|
Picual|Spain|both
Ravece|Italy|
Sabine|France|
Salkini|Syria, Lebanon, Jordan|
Salonenque|France|
Sevillano|Spain, United States|
Sevillenca|Spain|
Sikitita|Spain|
Souri|Lebanon, Israel|oil
Tanche|France|both
Thassos|Greece|table
Throumbolia|Greece|both
Verdale de l'Hérault|France|
Verdial|Spain|"""
DATES = """Abid Raḥim|Sudan|Called Dabino in Nigeria
Aṣeel|Pakistan|Pitted and diced before sale
Amir Hajj|Iraq|Soft, thin-skinned, thick-fleshed; served to guests
Barḥi|Bahrain, India, Iran, Iraq, Israel|Nearly spherical; amber to dark brown when ripe; good at the yellow khalal stage
Dayri|Iran, Iraq, Israel|The monastery date; long, slender, nearly black, soft
Empress|United States|Developed from a Thoory seedling; larger, softer and sweeter than Thoory
Farḍ|Oman, Bahrain, Somalia|Deep dark brown, tender skin, sweet, small seed; keeps well
Ḥalawi|India, Iran, Iraq, Israel, Palestine|Soft, extremely sweet, small to medium
Hayany|Egypt, Israel, Palestine|Dark red to nearly black, soft
Judean date palm|Israel|Ancient cultivar revived in 2005 from a 2,000-year-old seed
Kabkab|Iran, Syria|Listed Iranian and Syrian cultivar
Khaḍrawi|Djibouti, India, Iraq, Israel, Palestine, Syria|Name means green; very dark, soft
Khastawi|Iraq, Syria|Leading soft date in Iraq; syrupy, small, prized for dessert
Mabroom|Saudi Arabia|Large, elongated
Maktoom|Syria, Kuwait, Saudi Arabia|Large, red-brown, thick-skinned, soft, medium-sweet
Mishriq|Sudan|Name means east; includes Wad Khateeb and Wad Laggai varieties
Piarom|Iran|Large, thin-skinned, black-brown, semi-dry
Roṭab|Iran, Iraq|Dark and soft
Ṣafawi|Saudi Arabia|Grown mainly in Al-Madina; soft, semi-dried, deep black; similar to Ajwa
Ṣafrir|Israel|Red, sweet; can be eaten straight from the tree
Saidi|Libya|Soft, very sweet
Sayer|Iran, Iraq|Dark orange-brown, medium-sized, soft and syrupy
Thoory|Algeria|Popular dry date; brown-red when cured, wrinkled; sweet, nutty flavour
Um Al-Khashab|Saudi Arabia|Brilliant red skin; bittersweet, hard white flesh
Zaghloul|Egypt, India, Syria|Dark red, long, very crunchy when fresh; essentially exclusive to Egypt
Zahidi|Djibouti, Chile, Peru, India, Iran, Iraq, Israel, Palestine, Syria|Medium, cylindrical, light golden-brown semi-dry; very sugary
Bousthami|Morocco|Black (kahla) and white varieties
Tezerzayet|Tunisia|Includes Kahla and Safra varieties
Fṭimi|Tunisia|Grown in Tunisia's inland oases
Deglet Noor|Algeria, Tunisia, United States, Israel, Chile, Peru|Widely grown cultivar listed under many countries"""
CHILLI = """Cascabel|C. annuum|3,000 SHU
Chilhuacle|C. annuum|1,500–2,000 SHU
Chiltepin|C. annuum|50,000–100,000 SHU
De Árbol|C. annuum|15,000–30,000 SHU
Guntur chilli|C. annuum|30,000–350,000 SHU
Pequin|C. annuum|100,000–140,000 SHU
Puya|C. annuum|5,000 SHU
Bird's Eye|C. annuum|50,000–100,000 SHU
Cayenne|C. annuum|30,000–50,000 SHU
Mirasol|C. annuum|2,000–5,000 SHU
Prik Kee Nu|C. annuum|50,000–100,000 SHU
Cheongyang|C. annuum|10,000 SHU
Facing Heaven|C. annuum|30,000–50,000 SHU
Baklouti|C. annuum|1,000–5,000 SHU
Peperoncino|C. annuum|15,000–30,000 SHU
Chimayó|C. annuum|4,000–6,000 SHU
Habanero|C. chinense|100,000–350,000 SHU
Scotch Bonnet|C. chinense|150,000–325,000 SHU
Bhut Jolokia|C. chinense|up to 1,040,000 SHU
Carolina Reaper|C. chinense|1,569,300–2,200,000 SHU
Peri-peri|C. frutescens|50,000–175,000 SHU
Malagueta|C. frutescens|60,000–100,000 SHU
Tabasco pepper|C. frutescens|30,000–50,000 SHU
Aji Limon|C. baccatum|30,000–50,000 SHU
Rocoto|C. pubescens|30,000–100,000 SHU"""
FROZEN = """Amy's Kitchen
Aunt Bessie's
Banquet Foods
Bellisio Foods
Birds Eye
Bubba Foods
Dr. Praeger's
Earthbound Farm
Eggo
El Charrito
Elbtal
Felix
FarmRich
Findus
Freezer Queen
Frikom
FRoSTA
Fry Group Foods
Gorton's of Gloucester
Green Giant
Groupe Doux
Hilcona
Hortex
Hot Pockets
Hungry-Man
Iglo
Kangaroo Brands
Kart's
Kid Cuisine
Kidfresh
King of Pops
Lender's Bagels
M&M Meat Shops
Maxaroni
McCain Foods
Morton Frozen Foods
Mrs. Smith's
Ore-Ida
Pepperidge Farm
Perdue Farms
Ramly Group
Ross Group
Steak-umm
SuperFresh
Swanson
Tee Yih Jia
Tyson Foods"""
PIZZA = """Bagel Bites
Celeste
Ellio's Pizza
Fiestada
Freschetta
Grandiosa
Palermo's Pizza
Pizza Pops
Red Baron
Richelieu Foods
Totino's
Uno Chicago Grill"""
KIMCHI = """Baechu-geotjeori|napa cabbage|Unfermented, eaten fresh
Bossam-kimchi|napa cabbage|Wrapped kimchi
Baek-kimchi|napa cabbage|White kimchi made without chili pepper
Dongchimi|Korean radish|Non-spicy, watery winter kimchi
Nabak-kimchi|Korean radish|Mildly spicy, watery kimchi
Chonggak-kimchi|ponytail radish|Cubed, popular spicy kimchi
Pa-kimchi|green onion|Spicy green onion kimchi
Yeolmu-kimchi|young radish|Popular in spring and summer; not always fermented
Gat-kimchi|Indian mustard leaves|Made with gat mustard
Yangbaechu-kimchi|headed cabbage|Spicy, made with headed cabbage rather than napa
Morkovcha|carrot|Koryo-saram spicy marinated carrot dish
Gogumasoon kimchi|sweet potato stems|Seasonal variety
Seokryu kimchi||Named after its pomegranate-like shape
Jang kimchi||Pickled with soy sauce
Mugeun-ji||Aged kimchi
Hobakji|pumpkin|Typical of Hwanghae Province
Seokbak-ji||Named in a 1766 book; uses salted croaker
Gulgimchi|oyster|Kimchi with added oyster
Mul-kimchi||Watery kimchi
Dubu-kimchi||Tofu kimchi
Gimjang kimchi||Winter kimchi made in large batches, traditionally stored in the ground"""
