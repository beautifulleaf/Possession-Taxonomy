import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
L=W+"List_of_strawberry_cultivars"
FP="https://www.freshplaza.com/north-america/article/9100642/sweet-fragrant-and-crazy-expensive/"
X=[x("Royal Sovereign","","1892",W+"Royal_Sovereign_strawberry","Thomas Laxton's English strawberry (Noble x King of the Earliest per the cultivar list), served at the 1953 coronation banquet and still prized by enthusiasts.",[v("Royal Sovereign","","","Old-data name")]),
 x("Senga Sengana","","1954",L,"German strawberry from Markee x Sieger; a freezer and processing standard in central and eastern Europe."),
 x("Honeoye","","1979",L,"Early midseason Cornell strawberry from Vibrant x Holiday.",[v("Honeoye","","","Old-data name")]),
 x("Elsanta","","1975",L,"Dutch midseason strawberry from Gorella x Holiday, bred at the Institute for Horticultural Plant Breeding; the European supermarket standard.",[v("Elsanta","","","Old-data name")]),
 x("Camarosa","University of California","1994",L,"Early short-day California strawberry from Douglas x Cal 85.218-605; a Mediterranean and Californian staple.",[v("Camarosa","","","Old-data name")]),
 x("Albion","University of California","2006",L,"Day-neutral University of California strawberry from Diamante x Cal 94.16-1.",
   [v("Monterey","University of California","2009","Albion x Cal 97.85-6, day-neutral"),v("San Andreas","University of California","2009","Albion x Cal 97.86-1, day-neutral (listed as San Andrés)")]),
 x("Chandler","University of California","1983",L,"University of California strawberry from Douglas x Cal 72.361-105."),
 x("Seascape","University of California","1991",L,"Day-neutral University of California strawberry from Selva x Douglas."),
 x("Amaou","","",FP,"Very large Fukuoka strawberry, four to five times average size, whose name stands for red, round, sweet, big, delicious.",[]),
 x("Tochiotome","","",FP,"Small, sweet, fragrant Tochigi strawberry, widely eaten in eastern Japan.",[],a="Tochi Otome"),
 x("Bijin-hime","","",FP,"Gifu luxury strawberry, some berries over 100 g, selling up to 50,000 yen each.",[],a="Beautiful Princess"),
 x("Hatsukoi no Kaori","","2006",FP,"Yamanashi white (albino) strawberry brought to market in 2006 after about ten years of development.",[],a="Scent of First Love"),
 x("Alpine strawberry","","",W+"Fraise_des_bois","Fragaria vesca fraises des bois, small runnerless everbearing berries sold to gourmets.",
   [v("Rügen","","1920","First modern runnerless alpine cultivar"),v("Alexandria","","1964","Seed-raised alpine"),v("Weisse Solemacher","","","White-fruited alpine"),v("Baron Solemacher","","1935","Seed-raised alpine")],a="Fraise des bois · Wild strawberry"),
 x("Pineberry","","",W+"Pineberry","Small white pineapple-flavoured strawberry with red seeds, a Fragaria chiloensis x virginiana hybrid grown in Belgium and exported from the Netherlands.",[v("Pineberry","","","Old-data name")])]
brands=[B("Driscoll's","United States","Specialist","berry breeder and marketer","California family-owned berry company founded 1904, breeding proprietary varieties licensed to approved growers.",W+"Driscoll%27s")]
brands[0]["f"]="1904"
M=["AC-Yamaska","Alinta","Allstar","Darselect","Earliglow","Evie 2","Favori","Flamenco","Florence","Fraise de Nîmes PGI","Fraise du Périgord PGI","Frel (Pink Panda)","Gaviota","Hapil","Jewel strawberry","Kent strawberry","Malling Opal","Malling Pearl","Nyoho","Portola","Redgauntlet","Rhapsody","Sable strawberry","Sky Berry","Sonata","Symphony","Tristar","Truskawka kaszubska PGI","Mahabaleshwar Strawberry GI","Camino Real","Cambridge Favourite","Cavendish strawberry","Hokowase","Beni Hoppe","Rainier strawberry","Strawberry Festival","Pegasus","Sussette","Wendy"]
kinds=[K("Strawberry","Fresh strawberry, organised by cultivar from classic reference berries to Japanese premium and club berries.","https://plu.pro/commodity/berries",X,M,["June-bearing","everbearing","day-neutral","alpine/wild","white"])]
notes="Trimmed from 164 to 40 flat models plus archetypes. Gariguette, Mara des Bois, Malling Centenary, Sonata details, Skyberry, Sagahonoka, Beni Hoppe, Shiroi Hoseki and Seolhyang had no fetched page, so not archetypes (Beni Hoppe, Sky Berry, Sonata kept flat from old data). Bijin-hime may or may not be white; not stated. Dropped older and regional cultivars such as the Puget, Ozark and Canadian lines."
urls=[L,FP,W+"Royal_Sovereign_strawberry",W+"Fraise_des_bois",W+"Pineberry",W+"Driscoll%27s"]
write("00_05",kinds,brands,[],notes,urls)
