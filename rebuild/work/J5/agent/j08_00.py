from lib import *
MH=W+"Monofloral_honey"
kinds=[
{"n":"Honey","a":"","d":"Honey sold as blended, wildflower or single-flower (varietal) honey, liquid, set, creamed or in the comb.","t":["raw","set/creamed","comb","chunk","wildflower"],"s":W+"Honey",
 "m":[["Billy Bee Pure Canadian Clover Honey","Billy Bee"],["Mieli Thun Acacia Honey","Mieli Thun"],["Jacobsen Raw Buckwheat Honey","Jacobsen Salt Co."]],
 "x":[
 X("Acacia honey","Miere de salcâm","Light, clear, mildly floral and very sweet honey that stays liquid; main producers Bulgaria, Hungary, Ukraine and Romania.",MH,[V("Mieli Thun Acacia Honey","Mieli Thun")],"high fructose · stays liquid"),
 X("Clover honey","","Water-white to amber honey from Canada, the US, Sweden and New Zealand that crystallises readily.",MH,[V("Billy Bee Pure Canadian Clover Honey","Billy Bee")],"mild"),
 X("Orange blossom honey","","Thick, very sweet, strongly aromatic honey from citrus nectars.",MH,[],"citrus blend"),
 X("Lavender honey","Miel de Provence lavender","Light yellow honey with a woody, floral profile; Miel de Provence has an IGP (2005) and Label Rouge for all-flower and lavender/lavandin honey.",W+"Provence_Honey",[],"Banon · Valensole",y="IGP 2005"),
 X("Heather honey","ling","Honey mainly from UK moorland; thixotropic, gel-like when still and liquid when stirred.",W+"Honey",[],"thixotropic"),
 X("Chestnut honey","","Dark yellowish-brown honey from France, Italy and Greece with one of the highest mineral contents; barely crystallises.",MH,[],"dark · mineral"),
 X("Buckwheat honey","","Mahogany honey with a hay-like aroma and an intense, slightly bitter taste.",MH,[V("Jacobsen Raw Buckwheat Honey","Jacobsen Salt Co.")],"dark"),
 X("Tupelo honey","","Southeastern US honey from Nyssa trees, northern Florida a major source; very slow to granulate.",MH,[],"slow to crystallise"),
 X("Sourwood honey","","Thin, complex straw-coloured honey from Appalachia and the southeastern US with a faint sour finish.",MH,[],"Appalachia"),
 X("Sidr honey","jujube honey","Yellowish-brown traditional honey from Yemen and Pakistan with reputed health benefits.",MH,[],"Yemen · Pakistan"),
 X("Thyme honey","wild thyme honey","Dark amber honey from New Zealand, Greece and Italy; the most popular honey in Greece.",MH,[],"dark amber"),
 ]},
{"n":"Manuka honey","a":"mānuka honey","d":"Honey from mānuka flowers, graded by UMF or MGO (methylglyoxal), mainly from New Zealand.","t":["UMF graded","MGO graded","monofloral","multifloral (MGS)"],"s":W+"M%C4%81nuka_honey","m":[["Comvita Certified UMF Manuka Honey","Comvita"]],
 "x":[X("Certified UMF mānuka honey","UMF","New Zealand honey certified by the UMF Honey Association for honey harvested, packed and sealed in New Zealand; UMF 5 matches about 83 mg/kg MGO and UMF 10 about 263.",W+"M%C4%81nuka_honey",[V("UMF 10","","","About 263 mg/kg MGO"),V("UMF 15","","","About 514 mg/kg MGO"),V("UMF 20","","","About 829 mg/kg MGO"),V("UMF 24","","","About 1122 mg/kg MGO")],"UMF · MGO · NPA in UK")]},
{"n":"Honeydew honey","a":"forest honey","d":"Dark, strong, less sweet honey made by bees from sap-sucking insect secretions rather than nectar.","t":["forest","pine","fir","oak"],"s":W+"Honeydew_honey",
 "x":[X("Pine honey","","Honeydew honey from Marchalina hellenica scale insects on pine; Turkey makes about 92% of the world's, Muğla province about 80% of that.",W+"Pine_honey",[],"dark amber · resinous"),
      X("Fir honeydew honey","","Honeydew honey from conifer secretions; fir is named among the source trees.",W+"Honeydew_honey",[],"fir")]},
]
brands=[{"n":"Comvita","c":"New Zealand","f":"","seg":"Premium","kf":"mānuka honey","d":"New Zealand beekeeping and mānuka honey company with UMF-certified honey.","lines":["Certified UMF Manuka Honey"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"knowledge"}]
notes="Miel de Galicia IGP and Corsican AOP not found on retrieved pages; Manuka Health, Mieli Thun/Billy Bee brand entries and heather detail omitted or minimal. Beekeeping tradition entry not sourced so none. Honeydew sub-types limited to pine (own page) and fir (named in honeydew article)."
write("08_00",kinds,brands,[],notes)
