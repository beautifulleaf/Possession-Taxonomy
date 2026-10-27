import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
chard=[A("Green chard",W+"Chard","Green-stalked Swiss chard.",v=[("Lucullus",),("Fordhook Giant",)]),
A("Red-ribbed chard",W+"Chard","Red-stalked chard.",v=[("Ruby Chard",),("Rhubarb Chard",)]),
A("Rainbow chard",W+"Chard","Usually a mix of coloured chard varieties.")]
kinds=[K("Spinach","Fresh spinach (Spinacia oleracea).",t=["baby leaf","bunched","flat","savoy"],s=W+"Spinach"),
K("Chard","Fresh chard or silver beet.",x=chard,s="https://en.wikipedia.org/wiki/Chard",a="silver beet · Swiss chard · leaf beet"),
K("Amaranth greens","Fresh Amaranthus leaves cooked as a green: callaloo, chaulai.",s=W+"Amaranth",a="callaloo · chaulai · khada sag"),
K("Water spinach","Fresh Ipomoea aquatica shoots.",s=W+"Ipomoea_aquatica",a="kangkong · ong choy"),
K("Water dropwort","Fresh Oenanthe javanica, seri or minari.",x=[A("Sendai seri",W+"Oenanthe_javanica","Water dropwort from Miyagi Prefecture, Geographical Indication status in 2024.",a="仙台せり",dt="Japan GI")],s=W+"Oenanthe_javanica",a="seri · minari · komprek"),
]
save("01_10",kinds,[],[],"Spinach has no cultivars on retrieved page; Japanese and GI spinach not sourced. Hin choy alias not confirmed (omitted).")
