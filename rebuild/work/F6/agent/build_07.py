import json,os
W='https://en.wikipedia.org/wiki/'
L='https://luciteria.com/'
def x(n,d,s,y='',v=None,dt='',a='',mk=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def v(n,d,y='',mk=''): return {"n":n,"mk":mk,"y":y,"d":d}
SAFE="safety: radioactive, toxic, reactive and air-sensitive elements are restricted; check shipping and legal rules"
kinds=[
{"n":"Element cube","a":"density cube","d":"Sample of a chemical element machined or cast as a cube of standard size.","s":"https://luciteria.com/products/bismuth-metal-cube-99-99",
 "x":[x("Bismuth density cube","Metal cube sold in 10 mm, 25.4 mm and 50 mm sizes at 99.99% purity.",L+"products/bismuth-metal-cube-99-99","",[v("10 mm cube","9.8 g"),v("25.4 mm (1 inch) cube","160 g"),v("50 mm (2 inch) cube","over 1,200 g")],"purity 99.99% (4N) · 10 mm / 25.4 mm / 50 mm · mass",mk="Luciteria"),
      x("Rhenium density cube","10 mm metal cube at 99.95% purity.",L+"blog/2020/11/24/how-to-start-a-periodic-table-with-real-elements-collection","",[],"purity 99.95% · 10 mm",mk="Luciteria")]},
{"n":"Element ampoule","a":"element ampule","d":"Sample of a chemical element sealed in a glass ampoule.","s":"https://www.smart-elements.com/shop/1-5-grams-lithium-metal-sealed-in-ampoule-under-argon/",
 "x":[x("Noble gas glow ampoule","Sealed noble-gas tube lit by high voltage: neon glows orange-red, a Geissler-tube effect known since the 1850s.",W+"Neon_lighting","Geissler tubes 1857",[v("Neon discovery tube","Ramsay and Travers studied neon in a gas-discharge tube","1898")],"gas · glow colour · pressure · needs high-voltage source"),
      x("Uranium ampoule","2 g uranium ampoule sold for element collections; radioactive, so handling and shipping rules apply.",L+"blog/2020/11/24/how-to-start-a-periodic-table-with-real-elements-collection","",[],SAFE,mk="Luciteria")],"m":[]},
{"n":"Encased element sample","a":"Lucite block","d":"Sample of a chemical element embedded in a clear acrylic (Lucite) block.","s":"https://www.smart-elements.com/product/acrylic-element-cube-cesium133-cs-50mm/",
 "x":[x("Lucite element cube","Acrylic cube holding a sample so gases and unstable metals can be displayed safely.",L+"blog/2020/7/21/interested-in-element-collecting","",[],"cube size · element · "+SAFE,mk="Luciteria")]},
{"n":"Element crystal","d":"Sample of a refined chemical element sold as a grown crystal or crystal fragment for its identity.","s":"https://luciteria.com/products/bismuth-crystal-99-99",
 "x":[x("Bismuth hopper crystal","Stair-stepped rainbow-oxide crystal grown from molten bismuth; sold at 99.99% in small to very large sizes.",W+"Bismuth","",[v("Medium","15–40 g"),v("Large","40–75 g"),v("Very large","75 g and more")],"purity 99.99% · mass · crystal size · rainbow oxide colours",mk="Luciteria"),
      x("Gallium","Silvery blue metal that melts at 29.76 °C and can melt in the hand; embrittles aluminium and cannot be shipped by air.",W+"Gallium","",[],"melts in hand · plastic packet · no air shipping")]},
{"n":"Periodic table element collection","a":"periodic table display · element set","d":"Complete or partial set of element samples arranged as a periodic table in a display, table or case.","s":W+"Element_collecting",
 "x":[x("Theodore Gray's Periodic Table Table","Wooden table with a compartment under each element's label holding a sample; won an Ig Nobel Prize in Chemistry in 2002.","https://techcrunch.com/?p=507164","2002",[v("The Elements (book)","photographs by Nick Mann of Gray's collection"),v("Theodore Gray's Elements Vault","book with collectible samples")],"compartments per element · stable elements up to bismuth, plus thorium and uranium"),
      x("Luciteria display set","Element sample sets and display cases for 10 mm cubes, ampules and 25.4 mm cubes.",L+"blog/2020/7/21/interested-in-element-collecting","",[v("One of Each set","$25 listing"),v("10 mm cube and ampule display case",""),v("25.4 mm cube display case","")],"cube sizes 10 / 14 / 25.4 mm · cases",mk="Luciteria")]}]
brands=[{"n":"Luciteria","c":"United States","f":"","seg":"Specialist","kf":"element samples","d":"Seattle seller of element density cubes, ampules, Lucite cubes and display cases for collectors.","s":L+"blog/2020/7/21/interested-in-element-collecting","lines":["density cubes (10, 25.4, 50 mm)","Lucite cubes","ampules","bullion","displays"]}]
p='work/F6/shelves/07_00'
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Noble-gas colours beyond neon, osmium bead and Smart Elements products not confirmed on retrieved pages so left out (Smart Elements kept as old kind sources). Safety notes from Element collecting and Gallium pages. Radioactive element handling kept generic."},open(p+'.tmp','w'),ensure_ascii=False,indent=1)
os.rename(p+'.tmp',p+'.json')
