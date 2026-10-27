import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
carrot=[A("Nantes",W+"Carrot","Cylindrical, blunt-tipped Western carrot type, the classic fresh-market carrot.",dt="cylindrical · blunt tip"),
A("Imperator",W+"Carrot","Long, slender, pointed Western carrot type, the most widely grown by commercial growers.",dt="long · pointed"),
A("Chantenay",W+"Carrot","Short, broad-shouldered Western carrot type with vigorous foliage.",dt="short · wide"),
A("Danvers",W+"Carrot","Conical Western carrot type with a defined shoulder, developed in Danvers, Massachusetts.",y="1871"),
A("Kintoki",W+"Carrot","Red Japanese carrot cultivar from Kyoto Prefecture.",a="Kyoto red carrot",dt="Kyo-yasai"),
A("Purple carrot",W+"Carrot","Eastern-group carrots coloured by anthocyanin, domesticated in Persia.",dt="purple · yellow Eastern types")]
beet=[A("Detroit Dark Red",W+"Beetroot","Heirloom globe beetroot, listed as Detroit Dark Red Medium Top.",a="Perfected Detroit",dt="round · deep red"),
A("Chioggia",W+"Beetroot","Heirloom beetroot with red and white concentric rings.",dt="striped flesh"),
A("Boltardy",W+"Beetroot","Bolt-resistant round beetroot with the RHS Award of Garden Merit (1993).",dt="round · red"),
A("Cylindra",W+"Beetroot","Heirloom elongated beetroot, also sold as Formanova.",a="Formanova",dt="cylindrical"),
A("Golden beetroot",W+"Beetroot","Yellow-rooted beetroots.",v=[("Burpee's Golden",),("Touchstone Gold",)],dt="yellow"),
A("Albino beetroot",W+"Beetroot","White-rooted heirloom beetroot.")]
rad=[A("Cherry Belle",W+"Radish","Round red-skinned salad radish with white interior, common in North American shops.",dt="small red salad radish"),
A("French Breakfast",W+"Radish","Elongated red radish with a white tip, mild but quick to turn pithy.",dt="small red salad radish"),
A("White Icicle",W+"Radish","White carrot-shaped salad radish dating to the 16th century.",dt="small white salad radish"),
A("Black Spanish",W+"Radish","Rough black-skinned, hot, round or pear-shaped winter radish known in Europe since 1548.",y="1548",a="black radish",dt="winter radish"),
A("Daikon",W+"Daikon","Large Asian winter radish, usually a long white root; mooli in South Asia.",a="mooli · Japanese radish",v=[("Sakurajima",),("Nerima daikon",),("Watermelon radish",)],dt="winter radish"),
A("Korean mu",W+"Radish","Shorter, stouter radish with denser flesh and stronger flavour than daikon.",a="Joseon radish"),
A("Shogoin daikon",W+"Kyoyasai","Kyoto heritage radish among the Kyo-yasai brand vegetables.",a="Shōgoin",dt="Kyo-yasai")]
turnip=[A("Hakurei",W+"Turnip","Small white salad turnip, sold in bundles.",a="Tokyo turnip")]
pars=[A("Student",W+"Parsnip","Parsnip bred by James Buckman at the Royal Agricultural College, dominant in the late 19th century.",y="1859")]
cel=[A("Giant Prague",W+"Celeriac","Named celeriac cultivar."),A("Monarch",W+"Celeriac","Named celeriac cultivar."),A("Diamant",W+"Celeriac","Named celeriac cultivar.")]
burd=[A("Horikawa gobo",W+"Kyoyasai","Thick Kyoto burdock among the Kyo-yasai brand vegetables.",a="Horikawa burdock",dt="Kyo-yasai")]
kinds=[
K("Carrot","Fresh or frozen carrot.",x=carrot,s="https://plu.pro/commodity/carrots",m=["Carotte des sables de Créances AOC","Lammefjordsgulerod PGI","Carota Novella di Ispica PGI","Carota dell'Altopiano del Fucino PGI","津南の雪下にんじん GI","Polignano Carrots"]),
K("Beetroot","Fresh or frozen beetroot.",x=beet,s="https://plu.pro/commodity/beets"),
K("Radish","Fresh radish of any type: small salad radish or large winter radish (daikon).",x=rad,t=["small salad radish","daikon/winter radish"],s="https://plufinder.com/plu/4598",m=["松館しぼり大根 GI"]),
K("Parsnip","Fresh or frozen parsnip root (Pastinaca sativa).",x=pars,s="https://www.ocado.com/categories/fresh-chilled-food/vegetables/carrots-root-vegetables/ff6eaafb-28ef-4e55-8abd-f48f75b484d7"),
K("Turnip","Fresh turnip, round or long (hinona, kabu).",x=turnip,s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["山内かぶら GI"]),
K("Swede","Fresh swede (Brassica napus var. napobrassica); turnip is separate.",s="https://www.ocado.com/categories/fresh-chilled-food/vegetables/carrots-root-vegetables/ff6eaafb-28ef-4e55-8abd-f48f75b484d7",a="rutabaga · neep"),
K("Celeriac","Fresh celeriac root (Apium graveolens var. rapaceum).",x=cel,s="https://www.ocado.com/categories/fresh-chilled-food/vegetables/carrots-root-vegetables/ff6eaafb-28ef-4e55-8abd-f48f75b484d7"),
K("Parsley root","Fresh root of Petroselinum crispum var. tuberosum.",s="https://www.penzcentrum.hu/gazdasag/20210807/ismet-bovult-a-lista-ujabb-igazi-magyar-termek-kerult-unios-oltalom-ala-1116811",m=["Hegykői petrezselyemgyökér","Makói petrezselyemgyökér"]),
K("Salsify","Fresh salsify or black salsify roots (Tragopogon, Scorzonera).",t=["salsify","black salsify"],s="https://www.fineandwild.com/products/salsify"),
K("Burdock","Fresh burdock root, gobo in Japan.",x=burd,s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["連島ごぼう GI"]),
K("Maca","Fresh maca root; dried maca and maca flour are in Pantry Staples, capsules in Health, Medical & Mobility.",t=["cream-yellow","purple","black"],s="https://api.comunidadandina.org/uploads/LISTADO_DENOMINACIONES_DE_ORIGEN_CAN_07025d1e91.pdf",m=["Maca Junín - Pasco DO"]),
]
t=[{"n":"Kyō-yasai (Kyoto heritage vegetables)","g":"Food & drink","r":"Kyoto Prefecture, Japan","p":"pre-Meiji (before 1868); name adopted 1960; brand certification from 1989","d":"Heirloom vegetables of Kyoto, certified as brand products and tied to kaiseki and temple cooking.","tech":"local seed selection, small-lot farming","mat":"vegetables","forms":["Kintoki carrot","Shogoin daikon","Horikawa gobo","Kamo eggplant","Kujo negi"],"ctr":["Kyoto Prefecture","JA Kyoto"],"auth":"Kyoto Prefecture brand-product certification","s":"https://en.wikipedia.org/wiki/Kyoyasai"}]
save("01_02",kinds,[],t,"Cut flat cultivar lists (beetroot 25, carrot) to archetypes attested by retrieved pages. Shogoin kabu (turnip) not attested; Shogoin daikon used. Salsify, swede, parsley root, maca kept kind-level.")
