import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
k0=[K("Button mushroom","Fresh cultivated Agaricus bisporus; one species sold white, brown or mature.",x=[A("White button",W+"Agaricus_bisporus","Immature white form, from a 1925 Pennsylvania white mutant.",a="champignon de Paris"),A("Cremini",W+"Agaricus_bisporus","Immature brown form.",a="chestnut · baby bella · Swiss brown"),A("Portobello",W+"Agaricus_bisporus","Mature brown form with a 10-15 cm cap.",a="portabella")],t=["white","chestnut/cremini","portobello"],s="https://plu.pro/commodity/mushrooms"),
K("Shiitake","Fresh shiitake.",t=["donko","koshin"],s="https://plu.pro/commodity/mushrooms",m=["庆元香菇"],a="xianggu"),
K("Oyster mushroom","Fresh oyster mushroom (Pleurotus), including king oyster.",x=[A("Pearl oyster",W+"Oyster_mushroom","Pleurotus ostreatus, the type species and a major cultivated edible.",dt="grey"),A("King oyster",W+"Oyster_mushroom","Pleurotus eryngii, a weak parasite of herbaceous plants.",a="eryngii"),A("Pink oyster",W+"Oyster_mushroom","Pleurotus djamor, tropical.",dt="pink"),A("Golden oyster",W+"Oyster_mushroom","Pleurotus citrinopileatus, native to eastern Asia.",dt="golden")],t=["grey","king oyster","pink","golden"],s="https://plu.pro/commodity/mushrooms"),
K("Enoki","Fresh enoki mushroom (Flammulina), sold in clusters.",s="https://plu.pro/commodity/mushrooms",a="enokitake · golden needle"),
K("Shimeji","Fresh beech mushrooms (Hypsizygus), brown or white.",x=[A("Buna-shimeji",W+"Hypsizygus_tessellatus","Brown wild-type beech mushroom.",a="brown beech"),A("Bunapi-shimeji",W+"Hypsizygus_tessellatus","White variant from a UV mutation of the brown strain, strain registered by Hokto Corporation.",mk="Hokto",a="white beech")],s=W+"Hypsizygus_tessellatus"),
K("Maitake","Fresh hen-of-the-woods (Grifola frondosa).",s=W+"Grifola_frondosa",a="hen-of-the-woods"),
K("Lion's mane","Fresh Hericium erinaceus.",s=W+"Hericium_erinaceus",a="yamabushitake"),
K("Wood ear","Fresh wood ear fungus (Auricularia); dried wood ear is in Pantry Staples.",s="https://www.foraged.com/products/wood-ear-mushroom",a="jelly ear · Jew's ear")]
b3=[{"n":"Hokto","c":"Japan","f":"","seg":"Mainstream","kf":"cultivated mushrooms","d":"Japanese mushroom producer holding the registered bunapi-shimeji strain.","s":"https://en.wikipedia.org/wiki/Hypsizygus_tessellatus"}]
save("03_00",k0,b3,[],"Wikipedia pages used; 'koshin' not on the retrieved shiitake page, kept as a type name from the plan. Hokuto/Yukiguni/Monaghan: only Hokto sourced. Hokto name from Hypsizygus page; country from knowledge.")
T=W+"Truffle"
k1=[K("Truffle","Fresh truffle, species ordered by value.",x=[
A("Alba white truffle",T,"Tuber magnatum, from Langhe and Monferrato (Alba, Asti) and Molise; sells for thousands of dollars per pound.",a="Tartufo Bianco d'Alba · Tuber magnatum"),
A("Périgord black truffle",T,"Tuber melanosporum, second most valuable, harvested late autumn and winter.",a="Tuber melanosporum",v=[("Truffe noire du Tricastin AOC",)]),
A("Burgundy truffle",T,"Tuber uncinatum, autumn truffle with darker aromatic flesh, same species as T. aestivum.",a="Tuber uncinatum"),
A("Summer truffle",T,"Tuber aestivum, black summer truffle found across Europe.",a="Tuber aestivum"),
A("Bianchetto",T,"Tuber borchii, whitish truffle of Tuscany and Umbria, less aromatic.",a="Tuber borchii"),
A("Desert truffle",T,"Terfezia and Tirmania of Africa and the Middle East; used by Romans mainly as a flavour carrier.",a="terfez")],t=["grade by size and aroma"],s="https://www.truffe-plantin.com/en/7-fresh-truffles"),
K("Matsutake","Fresh Tricholoma matsutake, Japanese premium autumn mushroom.",x=[A("Japanese matsutake",W+"Matsutake","Tricholoma matsutake with Pinus densiflora in Japan; domestic harvest now under 1,000 tons and imports supply most of the market.",dt="Japan, Korea"),A("Jilin matsutake",W+"Matsutake","Matsutake of Longjing City, Jilin, 'Hometown of Matsutake'.",dt="China")],s=W+"Matsutake"),
K("Porcini","Fresh porcini or cep (Boletus edulis group); dried is in Pantry Staples.",x=[A("Fungo di Borgotaro",W+"Boletus_edulis","Porcini of the Borgotaro area near Parma, PGI, covering four Boletus species.",v=[("Fungo di Borgotaro PGI",)])],s="https://plu.pro/commodity/mushrooms",a="cep · penny bun"),
K("Chanterelle","Fresh chanterelle.",t=["golden","trumpet/yellowfoot"],s="https://plu.pro/commodity/mushrooms",a="girolle · Pfifferling"),
K("Morel","Fresh morel; dried morels are in Pantry Staples.",t=["black","yellow"],s="https://plu.pro/commodity/mushrooms")]
save("03_01",k1,[],[],"Tanba/Yangyang/Tibet matsutake origins not on retrieved page (replaced by Japanese and Jilin). Chinese winter truffle not found. Chanterelle/morel types from Wikipedia.")
k2=[K("Wakame","Fresh or frozen wakame seaweed; dried wakame is in Pantry Staples.",s="https://www.biovie.fr/en/146-organic-fresh-wakame-seaweed.html",a="Undaria pinnatifida",t=["fresh","salted"]),
K("Samphire","Fresh Salicornia shoots.",s=W+"Salicornia",a="marsh samphire · glasswort · sea asparagus · sea beans"),
K("Sea grapes","Fresh Caulerpa lentillifera, umibudo.",s=W+"Caulerpa_lentillifera",a="umibudo · kubiretsuta")]
save("03_02",k2,[],[],"Naruto and Sanriku wakame origins not found on retrieved page; left out.")
