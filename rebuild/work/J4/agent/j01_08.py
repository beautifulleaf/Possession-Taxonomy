import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
WS=W+"Winter_squash"; Z=W+"Zucchini"
cuc=[A("Slicing cucumber",W+"Cucumber","The main fresh group, grown outdoors or under glass.",a="English cucumber · long seedless",dt="slicing"),
A("Pickling cucumber",W+"Cucumber","Short cucumber group grown for pickling and gherkins.",a="gherkin · Kirby",dt="pickling"),
A("Seedless cucumber",W+"Cucumber","Parthenocarpic burpless greenhouse cucumbers.",a="burpless · Beit Alpha · Persian",dt="seedless")]
cour=[A("Black Beauty courgette",Z,"Dark green courgette, listed with Cocozelle and Bianco di Trieste.",a="Black Beauty",v=[("Cocozelle",),("Bianco di Trieste",)],dt="summer squash")]
sq=[A("Butternut",WS,"Pale tan winter squash, a common type.",dt="Cucurbita moschata"),
A("Kabocha",WS,"Japanese-style winter squash.",a="Hokkaido · Red Kuri · Ebisu",dt="Cucurbita maxima"),
A("Acorn",WS,"Ribbed dark winter squash.",dt="Cucurbita pepo"),
A("Delicata",WS,"Thin-skinned oblong winter squash.",dt="Cucurbita pepo"),
A("Spaghetti squash",WS,"Winter squash whose flesh forms strands.",dt="Cucurbita pepo"),
A("Hubbard",WS,"Large thick-skinned winter squash.",dt="Cucurbita maxima")]
kinds=[K("Cucumber","Fresh cucumber: slicing, mini, pickling or Asian types.",x=cuc,t=["slicing","mini","pickling","Asian"],s="https://plu.pro/commodity/cucumber",m=["Persian","Armenian","Lebanese","Lemon cucumber","Japanese cucumber","Beit Alpha","Telegraph","Gurken von der Insel Reichenau PGI","Spreewälder Gurken PGI","Naga Cucumber GI","高山きゅうり GI","Kirby","Marketmore 76","Poinsett"]),
K("Courgette","Fresh courgette (zucchini), shelved with squash of the same culinary use.",x=cour,t=["green","yellow (Gold Bar)","round","flowers"],s="https://plu.pro/commodity/squash",m=["Gold Bar"]),
K("Pumpkin & winter squash","Fresh or frozen pumpkin or winter squash, hard-rinded and eaten mature (butternut, kabocha, acorn, spaghetti); soft-skinned summer squash is courgette.",x=sq,t=["Cucurbita maxima","Cucurbita moschata","Cucurbita pepo"],s="https://plu.pro/commodity/pumpkin",m=["Loche de Lambayeque DO","Pie Pumpkin","江戸崎かぼちゃ GI"]),
K("Bitter melon","Fresh Momordica charantia.",s=W+"Momordica_charantia",a="karela · goya · ampalaya",t=["Chinese","Indian","miniature"]),
K("Bottle gourd","Fresh young Lagenaria siceraria.",s=W+"Calabash",a="lauki · doodhi · calabash · cucuzza · upo"),
K("Chayote","Fresh Sechium edule.",s="https://www.cnipa.gov.cn/art/2026/8/4/art_1401_208262.html",m=["新丰佛手瓜 地理标志产品"]),
K("Wax gourd","Fresh Benincasa hispida.",s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["豊橋なんぶとうがん GI"]),
K("Luffa","Fresh young Luffa fruit eaten as a vegetable; the dried sponge is not food.",s="https://cn.chinadaily.com.cn/a/202106/16/WS60c96edda3101e7ce9755073.html",m=["白关丝瓜 农产品地理标志"]),
]
save("01_08",kinds,[],[],"Cucumber 150 cultivar names reduced to the three groups on the Wikipedia page; cultivars not attested were not made archetypes (a few kept as flat models). Costata Romanesco, Ronde de Nice, Musquée de Provence, Atlantic Giant not on retrieved pages.")
