import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
kinds=[
K("Ginger","Fresh ginger root, sold young (juicy, mild) or mature (fibrous, pungent).",t=["young","mature"],s="https://plu.pro/commodity/ginger-root",m=["Assam Karbi Anglong Ginger GI","Mizo Ginger GI","八代生姜 GI"]),
K("Fresh wasabi","Fresh Eutrema japonicum rhizome grated at the table.",x=[
 A("Daruma",W+"Wasabi","One of the two main market cultivars of fresh wasabi.",dt="Eutrema japonicum"),
 A("Mazuma",W+"Wasabi","Main market cultivar and one of three traditional parents of modern wasabi cultivars.",dt="Eutrema japonicum"),
 A("Shizuoka wasabi",W+"Wasabi","Izu Peninsula terraced (tatamiishi) wasabi growing, recognised as a Globally Important Agricultural Heritage System.",dt="Izu Peninsula"),
 A("Azumino wasabi",W+"Wasabi","Wasabi from Azumino, Nagano, the largest producing prefecture in 2016.",dt="Nagano")],
 s=W+"Wasabi",a="wasabi rhizome"),
K("Horseradish","Fresh horseradish root; grated horseradish in jars is in Pantry Staples.",s="https://de.wikipedia.org/wiki/Herkunftsbezeichnung",m=["Bayerischer Meerrettich PGI","Hajdúsági torma PDO","Spreewälder Meerrettich PGI","Steirischer Kren PGI"]),
K("Fresh turmeric","Fresh Curcuma longa rhizome.",s=W+"Turmeric",a="fresh haldi"),
K("Galangal","Fresh Alpinia galanga rhizome.",t=["greater galangal","lesser galangal"],s=W+"Galangal",a="laos · kha"),
]
save("01_03",kinds,[],[],"Wasabi cultivars and regions from Wikipedia Wasabi. No cultivars found for ginger, turmeric, galangal, horseradish (GIs kept as models from old data).")
