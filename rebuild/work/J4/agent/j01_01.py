import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
N="https://potatoes.cals.ncsu.edu/sweetpotato/sweetpotato-varieties"
W="https://en.wikipedia.org/wiki/"
sp=[
A("Beauregard",W+"Sweet_potato","Orange-fleshed Louisiana cultivar that dominates US and Australian production.",mk="Louisiana Agricultural Experiment Station",y="1981",v=[("B94-14 Beauregard","NC State","","NC State selection with less twining vine")],dt="orange flesh · light rose skin"),
A("Jewel",N,"Orange-skinned, orange-fleshed North Carolina cultivar, long the state's main variety.",mk="NC State",y="1970",dt="orange flesh"),
A("Covington",N,"North Carolina table cultivar with high yield and uniform roots.",mk="NC State",y="2005",dt="orange flesh · light rose skin"),
A("Carolina Ruby",N,"Red-skinned, dark orange moist-baking cultivar.",mk="NC State",y="1998"),
A("Okinawan sweet potato",W+"Sweet_potato","Purple-fleshed sweet potato from Okinawa, called beni-imo.",a="beni imo",dt="purple flesh"),
A("Purple Majesty",N,"Dark-purple-skinned and fleshed North Carolina cultivar.",mk="NC State",y="2021",dt="purple flesh"),
A("Purple Splendor",N,"Dark purple skinned, purple fleshed, uniform and good storing.",mk="NC State",y="2021",dt="purple flesh"),
]
m=["Beni Azuma","Beni Haruka","Naruto Kintoki","Ayamurasaki","Stokes Purple","Garnet","O'Henry","Hannah Sweet","Batata doce de Aljezur PGI","Batata-Doce da Madeira PDO","ヤマダイかんしょ GI"]
kinds=[
K("Sweet potato","Fresh sweet potato, sold as orange, white or purple flesh.",x=sp,t=["orange flesh","white flesh","purple flesh"],s="https://plu.pro/commodity/sweet-potatoyamkumara",m=m),
K("Cassava","Fresh Manihot esculenta roots, sweet or bitter.",t=["sweet","bitter"],s=W+"Cassava",a="manioc · yuca"),
K("Yam","Fresh Dioscorea tubers; sweet potato sold as yam stays sweet potato.",x=[A("Greater yam",W+"Dioscorea","Dioscorea alata, the purple-fleshed water yam widely grown in the tropics.",a="ube · purple yam"),A("White Guinea yam",W+"Dioscorea","Dioscorea rotundata (D. cayennensis subsp. rotundata), the main West African food yam.",a="Dioscorea rotundata"),A("Chinese yam",W+"Dioscorea","Dioscorea japonica and relatives, eaten as shan yao in China.",a="nagaimo · shan yao")],s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["加賀丸いも GI"]),
K("Taro","Fresh Colocasia corms.",x=[A("Dasheen",W+"Taro","Large-cormed taro, also called dasheen.",a="dasheen"),A("Satoimo",W+"Taro","Japanese taro, simmered in dashi, with child corm (koimo) and grandchild corm (magoimo) offshoots.",a="village potato")],s="https://www.gov.uk/protected-food-drink-names/kolokasi-sotiras-slash-kolokasi-poulles-sotiras-slash-kolokasi-sotiras-slash-kolokasi-poulles-sotiras",m=["Κολοκάσι Σωτήρας / Κολοκάσι-Πούλλες Σωτήρας / Kolokasi Sotiras / Kolokasi-Poulles Sotiras PDO","上庄さといも GI"],t=["eddoe"]),
K("Jicama","Fresh yam-bean root (Pachyrhizus erosus).",s=W+"Jicama",a="Mexican turnip · singkamas"),
K("Jerusalem artichoke","Fresh tubers of Helianthus tuberosus.",s="https://www.ocado.com/categories/fresh-chilled-food/vegetables/carrots-root-vegetables/ff6eaafb-28ef-4e55-8abd-f48f75b484d7"),
K("Lotus root","Fresh Nelumbo rhizome.",x=[A("Tenno",W+"Lotus_root","Fresh-market lotus rhizome cultivar from Japan.",dt="rhizome lotus"),A("Bitchu",W+"Lotus_root","Fresh-market lotus rhizome cultivar from Japan.",dt="rhizome lotus")],s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["大口れんこん GI"]),
K("Arrowhead","Fresh Sagittaria corms.",s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",a="kuwai",m=["福山のくわい GI"]),
]
save("01_01",kinds,[],[],"Only cultivars attested by retrieved pages are archetypes; other old names kept as flat models up to the limit (about 120 old names cut). ube alias for Dioscorea alata is from knowledge. Cassava/jicama sourced to Wikipedia.")
