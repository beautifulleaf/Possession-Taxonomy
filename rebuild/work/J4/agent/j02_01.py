import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
B=W+"Basil"
bas=[A("Genovese",B,"The sweet basil that 'basil' usually means in Western cooking.",a="sweet basil · Ocimum basilicum",v=[("Basilico Genovese PDO",)]),
A("Thai basil",B,"Ocimum basilicum var. thyrsiflora.",a="Thyrsiflora"),
A("Holy basil",B,"Separate species Ocimum tenuiflorum, tulsi.",a="tulsi"),
A("Lemon basil",B,"Hybrid of O. basilicum and O. americanum with citral scent, kemangi in Indonesia.",a="kemangi"),
A("Purple basil",B,"Purple-leaved basils.",v=[("Dark Opal",),("Purple Ruffles",),("Purple Delight",),("Purpurescens",)]),
A("Greek bush basil",B,"Small-leaved Ocimum basilicum var. minimum.")]
kinds=[K("Basil","Fresh cut basil.",x=bas,s="https://plu.pro/commodity/basil"),
K("Coriander","Fresh or frozen coriander leaf, sold in bunches or packs to flavour food.",s="https://plu.pro/commodity/cilantro-chinese-parsleycoriander",a="cilantro"),
K("Parsley","Fresh or frozen parsley.",t=["flat-leaf (Italian)","curly (French)"],s="https://plu.pro/commodity/parsley"),
K("Mint","Fresh mint.",t=["spearmint","peppermint","other mints"],s="https://plu.pro/commodity/mint",m=["Peppermint","Spearmint","Apple mint","Moroccan mint"]),
K("Dill","Fresh or frozen dill leaf (Anethum graveolens), sold in bunches or packs; dill seed and dried dill are in Pantry Staples.",s="https://stopandshop.com/groceries/browse-aisles/3310-fresh-dill"),
K("Chives","Fresh chives (Allium schoenoprasum) sold in bunches or packs as a herb; garlic chives and wild chives are separate.",s="https://www.gurkerl.at/7909-chives-fresh-in-a-bunch-approx-85g"),
K("Thyme","Fresh thyme; dried thyme is in Pantry Staples.",s="https://fr.wikipedia.org/wiki/Liste_des_indications_g%C3%A9ographiques_prot%C3%A9g%C3%A9es_fran%C3%A7aises",m=["Thym de Provence PGI"]),
K("Rosemary","Fresh rosemary sprigs (Salvia rosmarinus); dried rosemary is in Pantry Staples.",s="https://www.superc.ca/en/aisles/fruits-vegetables/fresh-herbs/fresh-rosemary/p/068567120852"),
K("Sage","Fresh sage leaves (Salvia officinalis); dried sage is in Pantry Staples.",s="https://groceries.morrisons.com/products/morrisons-fresh-sage-20g/110419523"),
K("Oregano & marjoram","Fresh Origanum sprigs.",t=["Greek oregano","sweet marjoram","Turkish marjoram"],s=W+"Oregano",a="wild marjoram"),
K("Tarragon","Fresh Artemisia dracunculus.",t=["French tarragon","Russian tarragon","Mexican tarragon (Tagetes lucida)"],s=W+"Tarragon"),
K("Lemongrass","Fresh lemongrass stalks.",s="https://plu.pro/commodity/lemongrass",t=["West Indian (C. citratus)","East Indian (C. flexuosus)"]),
K("Perilla","Fresh Perilla frutescens leaves, green or red.",t=["green shiso","red shiso","kkaennip"],x=[A("Shiso",W+"Perilla_frutescens","Perilla frutescens var. crispa, milder aroma favoured in Japan; leaves green to red.",a="tía tô"),A("Kkaennip",W+"Perilla_frutescens","Korean perilla leaf eaten in ssam, namul and kimchi.",a="깻잎")],s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["川井赤しそ GI"]),
K("Mixed herbs","A fresh bundle of several herbs, none half or more of the weight (Frankfurter Grüne Soße).",s="https://de.wikipedia.org/wiki/Herkunftsbezeichnung",m=["Frankfurter Grüne Soße PGI"]),
]
save("02_01",kinds,[],[],"Basil cultivars trimmed from 35 to six attested archetypes. Coriander, dill, chives, rosemary, sage kept kind-level; no sourced cultivars. Cultivar names of mint not made archetypes.")
