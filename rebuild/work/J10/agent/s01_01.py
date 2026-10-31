import json
W='https://en.wikipedia.org/wiki/'
OLD="https://www.smokingpipes.com/smokingpipesblog/single.cfm/post/smokingpipes-university-tobacco-families"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
cuts=["Ribbon","Flake","Plug","Rope","Coin","Cube cut"]
kinds=[
{"n":"Virginia blend","a":"Virginia","d":"Pipe tobacco blend led by Virginia leaf.","t":cuts,"s":OLD,"m":[["Bright Virginia Ribbon","Cornell & Diehl"]]},
{"n":"Virginia/Perique blend","a":"VaPer","d":"Virginia-led blend with Perique, a pressure-fermented Louisiana leaf from St. James Parish.","t":["Flake","Ribbon"],"s":OLD,
 "x":[x("Three Nuns","Mac Baren","19th century",
  "https://www.tobaccoreviews.com/blend/1259/mac-baren-three-nuns/","Coin-cut blend created by J & F Bell; once Virginia-Perique under Imperial Tobacco, now Virginia and Kentucky, made by Mac Baren.",
  [("Imperial Tobacco VaPer","Imperial Tobacco","","Classic version with Perique"),("Orlik formula","Orlik","","Kentucky replaced Perique"),("Mac Baren","Mac Baren","","Current formula")])],
 "m":[["Bayou Morning","Cornell & Diehl"]]},
{"n":"English & Balkan blend","a":"Latakia blend · English · Balkan","d":"Unflavoured blend of Virginia or Burley with Latakia and Oriental leaf; Balkan blends use more Oriental.","t":["Ribbon","Flake"],"s":OLD,
 "x":[x("My Mixture 965","Peterson","",
  "https://www.tobaccoreviews.com/blend/458/peterson-my-mixture-965","English blend of Cavendish, Latakia, Oriental and Virginia in ribbon cut; made by Dunhill until 1981, later Orlik, now sold as Peterson.",
  [("Dunhill My Mixture 965","Dunhill","","Made in London until 1981"),("Murrays","Murrays","1981","Belfast until late 2004"),("Orlik","Orlik","2004","Denmark, Scandinavian Tobacco Group")])],
 "m":[["Early Morning Pipe","Peterson of Dublin"],["Billy Budd","Cornell & Diehl"],["Super Balkan","Cornell & Diehl"]]},
{"n":"Burley blend","a":"American blend","d":"Pipe tobacco blend led by Burley leaf; also sold as American blend.","t":["Ribbon","Cube cut"],"s":OLD,
 "x":[x("Prince Albert","Prince Albert","1907",W+"Prince_Albert_(tobacco)","Burley-based blend introduced by R.J. Reynolds in 1907; owned by John Middleton since 1987.")],
 "m":[["Haunted Bookshop","Cornell & Diehl"]]},
{"n":"Oriental blend","a":"Turkish blend","d":"Pipe tobacco led by small-leafed sun-cured Oriental (Turkish) leaf, grown in Thrace, Macedonia and Turkey.","t":["Ribbon","Flake"],"s":W+"Turkish_tobacco"},
{"n":"Aromatic blend","a":"","d":"Pipe tobacco blend flavoured or cased for aroma.","t":["Ribbon","Cavendish"],"s":OLD,"m":[["Autumn Evening","Cornell & Diehl"]]},
{"n":"Kizami","a":"","d":"Japanese very fine-cut tobacco leaf, smoked in the kiseru pipe.","t":[],"s":"https://www.jti.co.jp/tobacco/index.html"},
{"n":"Dokha","a":"","d":"Dried, ground Iranian-origin tobacco flavoured with herbs and spices, with no molasses, smoked in a midwakh.","t":["Hot","Warm","Cold"],"s":W+"Dokha"},
]
brands=[
{"n":"Mac Baren","c":"Denmark","f":"","seg":"Mainstream","kf":"pipe tobacco","d":"Danish blender that now makes Three Nuns.","lines":["Three Nuns"],"s":"https://www.tobaccoreviews.com/blend/1259/mac-baren-three-nuns/"},
{"n":"Prince Albert","c":"United States","f":"1907","seg":"Mainstream","kf":"burley","d":"Burley-based tobacco introduced by R.J. Reynolds, owned by John Middleton since 1987.","s":W+"Prince_Albert_(tobacco)"},
{"n":"Peterson","c":"Ireland","f":"1865","seg":"Heritage manufactory","kf":"System pipe","d":"Dublin pipe maker; now also sells My Mixture 965, formerly Dunhill.","s":W+"Peterson_Pipes"},
]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Samuel Gawith Full Virginia Flake, Gawith Hoggarth, Orlik Golden Sliced, McClelland, Sutliff, Lane, Erinmore, Captain Black, Escudo, Presbyterian Mixture: no retrieved page (Gawith retailer page blocked, others only snippets), so omitted. Cornell & Diehl skew trimmed to one or two blends per kind. Early Morning Pipe stays an unsourced old model. Dokha and Oriental are new kinds sourced from Wikipedia."},open('s01_01.json','w'),ensure_ascii=False)
