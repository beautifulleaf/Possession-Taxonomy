import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
pea=[A("Garden pea",W+"Pea","The green, immature pea eaten fresh, frozen or canned.",v=[("Kelvedon Wonder","","","65 days, RHS AGM 1997, popular in the UK"),("Little Marvel","","1934","63 days, All-America Selections winner")]),
A("Mangetout",W+"Pea","Flat-podded edible-pod pea eaten very young; snow pea.",a="snow pea"),
A("Sugar snap pea",W+"Pea","Round thick-walled edible-pod pea eaten before maturity.",a="snap pea")]
gb=[A("French bean",W+"Green_bean","Stringless Phaseolus vulgaris pods, thin round fillet types.",a="haricot vert · fine bean"),
A("Runner bean",W+"Green_bean","Phaseolus coccineus, a separate species usually grown as pole type.",v=[("Scarlet Runner",)]),
A("Yardlong bean",W+"Green_bean","Vigna unguiculata subsp. sesquipedalis, immature pods used like green beans.",a="asparagus bean"),
A("Romano bean",W+"Green_bean","Wide flat-podded green bean.",a="Italian flat bean")]
sh=[A("Borlotti",W+"Cranberry_bean","Cranberry bean variety bred in Italy with thicker skin, tan with red streaks that fade when cooked.",a="cranberry bean · Roman bean",v=[("Saluggia bean","","","regional borlotti from Saluggia")])]
sw=[A("Golden Bantam",W+"Sweet_corn","Open-pollinated heirloom sweet corn favoured by home gardeners, tender and flavourful.",dt="su class",v=[("Early Golden Bantam",),("Golden Cross Bantam",)]),
A("Kandy Korn",W+"Sweet_corn","Example of sugary-enhanced (se) sweet corn that stores longer, 12-20% sugar.",dt="se class"),]
kinds=[K("Pea","Fresh or frozen green pea, in or out of the pod.",x=pea,t=["garden pea","mangetout","sugar snap"],s="https://plu.pro/commodity/peas",m=["Salento Traditional Peas","Little Marvel","Wando","Tom Thumb (Half Pint)","Thomas Laxton (Laxton's Progress)","Tall Telephone (Alderman)"]),
K("Green bean","Fresh or frozen immature bean pods eaten whole (French, runner, yardlong beans); dried beans are in Pantry Staples.",x=gb,t=["French","runner","yardlong","flat"],s="https://plufinder.com/plu/4066"),
K("Broad bean","Fresh or frozen broad beans (Vicia faba), in or out of the pod; dried beans are in Pantry Staples.",s="https://www.ocado.com/products/natoora-fresh-broad-beans/86468011",a="fava bean"),
K("Shelling bean","Fresh Phaseolus beans sold in or out of the pod to shell; green beans are the pod eaten whole, dried beans are in Pantry Staples.",x=sh,s="https://fr.wikipedia.org/wiki/Liste_des_appellations_europ%C3%A9ennes_de_fruits,_l%C3%A9gumes_et_c%C3%A9r%C3%A9ales",m=["Coco de Paimpol AOP","Flageolet"]),
K("Edamame","Fresh or frozen green soya beans in the pod.",s="https://www.ardo.com/en/stories/european-edamame-pod",m=["くろさき茶豆 GI"]),
K("Sweetcorn","Fresh or frozen sweetcorn, on the cob or as kernels; genetic class su, se or sh2 is the organising detail.",x=sw,t=["su","se","sh2 supersweet","yellow","white","bicolour","baby corn"],s="https://plu.pro/commodity/corn",m=["Silver Queen","Peaches and Cream","Incredible","Honey and Cream","Butter and Sugar","Jubilee SuperSweet","How Sweet It Is","Illini Xtra Sweet","Country Gentleman","Luther Hill"]),
]
save("01_11",kinds,[],[],"Sweetcorn list trimmed from 95 to attested classes plus a few flat models. Aquadulce, The Sutton, Hurst Green Shaft, dadachamame, Kurosaki, Silver Queen, Peaches and Cream not found on retrieved pages. Flageolet page was the instrument; kept Flageolet only as a name.")
