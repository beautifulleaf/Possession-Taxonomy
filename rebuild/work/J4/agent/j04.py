import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
M="https://metropolisjapan.com/japanese-luxury-fruits/"
H="https://en.wikipedia.org/wiki/Harry_%26_David"
kinds=[K("Mixed fruit","A mix of fruit from several crop groups in which no one kind makes up half or more of the weight, such as a smoothie mix.",s="https://bestberries.co.za/shop/frozen-mixes/summer-mix-mango-banana-rasp-straw/",t=["fresh","frozen"]),
K("Mixed berries","A mix of berries or small fruit in which no one kind makes up half or more of the weight, such as a forest-fruit mix.",s="https://podravkagrupa.com/en/products/forest-fruits/",t=["fresh punnet","frozen"]),
K("Mixed vegetables","A plain mix of vegetables from several crop groups, such as frozen mixed vegetables, in which no one kind makes up half or more of the weight.",s="https://www.huntsfoodgroup.co.uk/shop/mixed-vegetables-1kg",t=["fresh","frozen"]),
K("Mixed fruit & vegetables","A mix of fruit and vegetables, such as a party tray, in which no one kind makes up half or more of the weight.",s="https://www.instacart.com/categories/316-food/317-fresh-produce"),
K("Fruit gift box","Selected premium fruit packed as a gift: boxed melons, grapes, mangoes, baskets.",s=M,t=["Japanese gift fruit","Western fruit basket"],a="fruit basket · gift fruit")]
brands=[
{"n":"Sembikiya","c":"Japan","f":"","seg":"Specialist","kf":"luxury gift fruit","d":"Tokyo fruit shop and parlour, flagship in Nihonbashi, selling seasonal fruit from Japan and abroad.","lines":["Sembikiya Fruit Parlor"],"s":M},
{"n":"Takano","c":"Japan","f":"1885","seg":"Specialist","kf":"fruit parlour","d":"Shinjuku Takano Fruits Parlor, founded 1885 beside Shinjuku Station, known for fruit parfaits.","s":M},
{"n":"Harry & David","c":"United States","f":"1910","seg":"Specialist","kf":"fruit gift baskets","d":"Medford, Oregon firm that began as Bear Creek Orchards and sells fruit gift baskets; owned by 1-800-Flowers.com.","s":H},
{"n":"Birds Eye","c":"","f":"","seg":"Mainstream","kf":"frozen vegetables","d":"Frozen vegetable brand, market leader in frozen mixed vegetables.","s":"knowledge"},
{"n":"Green Giant","c":"United States","f":"","seg":"Mainstream","kf":"frozen vegetables","d":"Frozen and canned vegetable brand, market leader in mixed vegetables.","s":"knowledge"},
{"n":"Bonduelle","c":"France","f":"1853","seg":"Mainstream","kf":"vegetables","d":"French vegetable group selling frozen and canned mixed vegetables.","s":"knowledge"}]
save("04_00",kinds,brands,[],"Dropped old GI citrus models under Mixed fruit (single-crop GIs, not mixes). Market-leader brands (Birds Eye, Green Giant, Bonduelle) recorded in the register from knowledge. Japanese shipping grades not found on retrieved pages, left out. Takano founded 1885 per metropolisjapan; Sembikiya year given only as 19th century so omitted.")
