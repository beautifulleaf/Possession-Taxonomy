import json
W='https://en.wikipedia.org/wiki/'
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":mk,"y":b,"d":c} for a,b,c in v]
    return r
C=W+"Cigarillo"
kinds=[
{"n":"Cigarillo","a":"small cigar","d":"Small, thin cigar about 7-10 cm long and 6-9 mm wide, usually unfiltered; premium and mass-market versions exist.","t":["Tipped cigarillo","Flavoured cigarillo"],"s":"https://www.famous-smoke.com/cigars",
 "x":[x("Café Crème","","",C,"British cigarillo brand, now sold as Henri Wintermans Signature."),
      x("Cohiba Mini","Cohiba","",C,"Premium cigarillo from Cohiba."),
      x("Davidoff Club Cigarillos","Davidoff","",C,"Premium cigarillo from Davidoff."),
      x("Dannemann Moods","Dannemann","1994",W+"Dannemann_Cigars","Flavoured cigarillo brand launched in 1994."),
      x("Swisher Sweets","Swisher","1958",W+"Swisher_Sweets","US flavoured cigarillo line introduced about 1958-59.",[("Classics","",""),("Minis","",""),("BLK","","")])],
 "m":[["Hamlets",""],["Agio Panters",""],["Garcia y Vega",""],["Game",""],["Optimo",""]]},
{"n":"Little cigar","a":"filtered cigar","d":"Cigarette-sized cigar wrapped in tobacco leaf or tobacco-pulp paper, usually filtered.","t":["Filtered little cigar","Flavoured little cigar"],"s":"https://en.wikipedia.org/wiki/List_of_tobacco_products"},
{"n":"Machine-made cigar","a":"mass-market cigar","d":"Cigar made by machine from short-filler or reconstituted tobacco, cheaper than a handmade cigar and sold in many shapes and flavours.","t":["Pipe-tobacco cigar","Blunt"],"s":C,
 "x":[x("Swisher Sweets","Swisher","1958",W+"Swisher_Sweets","Best-known US machine-made cigar line; Swisher also sells Minis and BLK.",[("Classics","",""),("Encore Edition","",""),("Limited Edition","","")]),
      x("Black & Mild","John Middleton","",W+"Black_and_Mild","Machine-made cigar with an outer layer of processed pipe tobacco, sold with plastic or wood tip; Altria bought the maker in 2007.",[("Tipped","",""),("Shorts","","about half size")]),
      x("Phillies","Phillies","1910",W+"Phillies_(cigar)","Cigar brand started by the Bayuk brothers in 1910, source of the blunt name; now made by ITG Brands.",[("Blunt","",""),("Cheroot","",""),("Cigarillo","",""),("Panatella","",""),("Titan","","")])],
 "m":[["Backwoods",""],["Dutch Masters",""]]},
{"n":"Toscano (Italian fire-cured cigar)","a":"Toscano · Sigaro Toscano","d":"Italian cigar made from Kentucky tobacco, fermented and flame-cured, 13-16.5 mm thick and about 155-163 mm long.","t":["Hand-rolled Toscano"],"s":W+"Toscano_(cigar)",
 "x":[x("Toscano Originale","Manifatture Sigaro Toscano","1818",W+"Toscano_(cigar)","Hand-rolled Toscano, the higher-quality range."),
      x("Toscano Antico","Manifatture Sigaro Toscano","",W+"Toscano_(cigar)","Variety of Toscano; Toscanello Speciale is half of one.")]},
{"n":"Cheroot","a":"seboleik","d":"Cylindrical, untapered, filterless cigar with both ends clipped, cheap to roll mechanically; traditional in India and Myanmar.","t":["Burmese cheroot","Indian cheroot"],"s":W+"Cheroot",
 "x":[x("Burmese cheroot","","",W+"Cheroot","Myanmar cheroot (seboleik, 'light-tasting rolled tobacco'), made mainly around Myin Gyan; home-rolled ones may be conical."),
      x("Indian cheroot","","",W+"Cheroot","Cheroot form said to originate from Tiruchirappalli in Tamil Nadu.")]},
]
brands=[
{"n":"Swisher","c":"United States","f":"","seg":"Mainstream","kf":"cigarillos","d":"US cigar maker behind Swisher Sweets, headquartered in Jacksonville, Florida.","lines":["Swisher Sweets"],"s":W+"Swisher_Sweets"},
{"n":"John Middleton","c":"United States","f":"","seg":"Mainstream","kf":"pipe-tobacco cigars","d":"Maker of Black & Mild, bought by Altria in 2007.","lines":["Black & Mild"],"s":W+"Black_and_Mild"},
{"n":"Phillies","c":"United States","f":"1910","seg":"Mainstream","kf":"blunts","d":"Cigar brand introduced by the Bayuk brothers in 1910, now made by ITG Brands.","s":W+"Phillies_(cigar)"},
{"n":"Manifatture Sigaro Toscano","c":"Italy","f":"","seg":"Heritage manufactory","kf":"Toscano","d":"Maker of the Toscano fire-cured cigar, in Lucca and Cava de' Tirreni.","s":W+"Toscano_(cigar)"},
{"n":"Cohiba","c":"Cuba","f":"1966","seg":"Heritage manufactory","kf":"flagship","d":"Cuban brand launched 1966.","s":W+"Cohiba_(cigar)"},
{"n":"Davidoff","c":"Switzerland","f":"1906","seg":"Premium","kf":"Swiss luxury","d":"Swiss house making premium cigars and cigarillos.","s":W+"Davidoff"},
{"n":"Dannemann","c":"Brazil","f":"1873","seg":"Heritage manufactory","kf":"Brazilian origin","d":"Founded by Geraldo Dannemann in São Félix, Brazil; now Germany-based and Swiss-owned.","s":W+"Dannemann_Cigars"},
]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Villiger, Agio, Partagás Mini, Cohiba Club and Swiss stumpen not found on retrieved pages and left out. Backwoods, Dutch Masters and others kept as flat models without sources. Little cigar has no archetypes (no sourced named brand). Cohiba, Davidoff and Dannemann also appear in shelves 00_00/00_01."},open('s00_02.json','w'),ensure_ascii=False)
