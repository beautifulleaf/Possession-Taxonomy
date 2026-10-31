import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
onion=[
A("Vidalia",W+"Vidalia_onion","Sweet onion of Georgia, USA, grown under a USDA federal marketing order in a limited area; Granex-type.",y="1930s",dt="sweet · Yellow Granex type",v=[("Vidalia Onions",)]),
A("Walla Walla",W+"Onion","Sweet yellow onion cultivar.",dt="sweet"),
A("Rossa di Tropea",W+"Onion","Italian red onion sold as Cipolla Rossa di Tropea Calabria PGI.",dt="red · mild",v=[("Cipolla Rossa di Tropea Calabria PGI",)]),
A("Cévennes sweet onion",W+"Onion","Sweet yellow onion cultivar named in the onion article as Cévennes.",a="Oignon doux des Cévennes",v=[("Oignon doux des Cévennes AOP",)]),
]
garlic=[
A("Ail rose de Lautrec",W+"Garlic","Pink garlic of Lautrec, France, protected geographical indication.",dt="rose · PGI"),
A("Ail violet de Cadours",W+"Garlic","Purple garlic of Cadours, France, protected designation of origin.",dt="violet · PDO"),
A("Ajo Morado de Las Pedroñeras",W+"Garlic","Pink-purple garlic of Las Pedroñeras, Spain, protected geographical indication.",a="Ajo Morado de Las Pedronieras",dt="PGI"),
A("Aglio di Voghiera",W+"Garlic","Garlic of Voghiera, Ferrara, Italy, protected designation of origin.",dt="PDO"),
A("Elephant garlic",W+"Elephant_garlic","Mild, large-cloved bulb that is a leek relative (Allium ampeloprasum), not a true garlic."),
]
shallot=[A("French red shallot",W+"Shallot","The usual shallot, Allium cepa var. aggregatum, with golden brown, grey or rose red skin.",v=[("Pikant",),("Atlas",),("Ed's Red",)]),
A("French grey shallot",W+"Shallot","Allium oschaninii, the 'true shallot' or griselle.",a="Griselle"),
A("Persian shallot",W+"Shallot","Allium stipitatum, musir, from the Zagros mountains.",a="Musir")]
kinds=[
K("Bulb onion","Fresh bulb onion; colour and sweetness as types.",x=onion,t=["yellow","red","white","sweet"],s="https://plu.pro/commodity/onions",m=["Cebolla Fuentes de Ebro PDO","Bangalore Rose Onion GI","Oignon de Roscoff AOP","Makói vöröshagyma PDO","Všestarská cibule PDO","Ptujski lük PGI","Höri Bülle PGI","Cipolla bianca di Margherita PGI","Lasalgaon Onion GI","Alibag White Onion GI","Maui","Texas Sweet","Sunions","Sweetheart (Tearless Red)","Pearl onion"]),
K("Garlic","Fresh garlic bulb; hardneck or softneck, and fresh green garlic.",x=garlic,t=["hardneck","softneck","green (wet) garlic"],s="https://plu.pro/commodity/garlic",m=["Kodaikona Malai Poondu GI".replace("Kodaikona","Kodaikanal"),"Kanthalloor Vattavada Veluthulli GI","Ratlam Riyawan Lahsun GI","Ail blanc de Lomagne","Taşköprü Sarımsağı","Aglio Rosso di Nubia","Vrbički beli luk","ところピンクにんにく GI"]),
K("Shallot","Fresh shallot.",x=shallot,s="https://plu.pro/commodity/onions",m=["Scalogno di Romagna PGI","Échalote d'Anjou PGI"]),
K("Leek","Fresh or frozen leek.",t=["summer","overwintering"],s="https://plufinder.com/plu/4629",m=["Poireaux de Créances PGI","Welsh Leeks UK PGI"]),
K("Spring onion","Fresh young onion eaten with its green stems.",x=[A("Calçot",W+"Calçot","Blanched Catalan green onion eaten at calçotadas; the Valls variety is PGI.",a="Calçot de Valls",v=[("Calçot de Valls PGI",)])],s="https://plu.pro/commodity/onions",m=["Cipollotto Nocerino PGI","新里ねぎ GI"]),
K("Welsh onion","Fresh Allium fistulosum sold as long white-shanked negi; young salad onions are spring onions.",x=[A("Kujo negi",W+"Kyoyasai","Kyoto Kujo Welsh onion, a Kyo-yasai brand vegetable.",a="九条ねぎ",dt="Kyo-yasai")],s="https://www.melissas.com/products/tokyo-negi",a="negi · naganegi"),
K("Garlic chive","Fresh Allium tuberosum leaves and flower stems.",s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["しりうちにら北の華 GI"]),
K("Wild garlic","Fresh leaves and bulbs of wild Allium species gathered or grown (ramsons, dallae).",s="https://www.mafra.go.kr/bbs/home/792/576894/download.do",m=["태안달래 GI (지리적표시)"],a="ramsons · bear's garlic"),
K("Rakkyo","Fresh Allium chinense bulbs sold to pickle.",s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["鳥取砂丘らっきょう GI"]),
]
save("01_04",kinds,[],[],"Merged four onion kinds into Bulb onion. Walla Walla/Rossa di Tropea attested only by the onion article. Maui, Bangalore Rose and Shimonita negi not found on retrieved pages (Maui, Bangalore Rose kept as flat old-data models). Dropped ~25 minor regional onion/garlic models.")
