import json, os
W='https://en.wikipedia.org/wiki/'
PI_L='https://perfumeintelligence.co.uk/library/perfume/bottlers/data/Lalique.htm'
PI_G='https://perfumeintelligence.co.uk/library/perfume/bottlers/data/GuerlainFlacons.htm'
LA='https://www.loveantiques.com/antique-glass/scent-bottles'
JOA='https://journalofantiques.com/features/czech-art-deco-vanity/'
CW='https://collectorsweekly.com/stories/98665-devilbiss-atomizer-perfume-bottle'
EI='https://egyptianimports.com/blogs/news/the-timeless-beauty-of-hand-blown-egyptian-glass-perfume-bottles'
def X(n,a,d,mk,y,s,v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Collectible perfume bottle","a":"designer flacon · art-glass perfume bottle · perfume flacon",
 "d":"Named bottle design made for a perfume house, often by a glass designer or crystal works, collected for the bottle itself.",
 "t":["full with perfume","empty","boxed","limited edition","extrait / parfum size","signed (e.g. etched maker's mark)"],
 "s":W+"Perfume_bottle",
 "x":[
  X("Lalique for Coty","L'Effleurt · Coty flacons by René Lalique","René Lalique's moulded-glass bottles for François Coty, which began his move into industrial glassmaking.","Lalique","1908",
    "https://www.musee-lalique.com/en/exhibit-month/leffleurt-perfume-bottle/",
    [("L'Effleurt label","Lalique","1908","glass label applied to a Baccarat crystal bottle"),
     ("L'Effleurt bottle","Lalique","1912","Lalique's own bottle, patinated, stopper with two cicadas"),
     ("Cyclamen","Lalique","1909",""),("Ambré Antique","Lalique","1911",""),("Styx de Coty","Lalique","1911",""),
     ("Au Cœur des Calices","Lalique","1912",""),("Lezards","Lalique","1912","")],
    "moulded glass · patina · stopper motif · label · with or without box"),
  X("Lalique for D'Orsay","Parfums d'Orsay flacons","Series of René Lalique bottles for Parfums d'Orsay in the 1910s.","Lalique","1910s",PI_L,
    [("Chevalier d'Orsay","Lalique","1911",""),("Leurs Ames","Lalique","1912",""),("Mystère","Lalique","1912",""),("Gavotte Bleue","Lalique","1919","")],
    "moulded glass · stopper design · size"),
  X("Quelques Fleurs (Lalique for Houbigant)","","René Lalique bottle for Houbigant's Quelques Fleurs.","Lalique","1912",PI_L,[],"moulded glass · size"),
  X("Dans la Nuit (Lalique for Worth)","","Cobalt-blue René Lalique bottle for Worth's Dans la Nuit.","Lalique","1924",LA,[],"cobalt blue glass · size"),
  X("Shalimar bottle","Shalimar flacon","Raymond Guerlain's design with a blue fan-shaped stopper, modelled on eastern garden basins; made by Baccarat.","Guerlain","1925",
    W+"Shalimar_(perfume)",[("Baccarat crystal flacon","Baccarat","1925","won the Decorative Arts Exhibition Award"),("60th-anniversary Lucite box","Guerlain","1985","repackaging")],
    "crystal · blue stopper · extrait size"),
  X("Bee bottle","Flacon Abeilles","Guerlain bottle decorated with bees, made by Pochet du Courval and still in use.","Guerlain","",PI_G,[],"gilt bees · size · eau de cologne / extrait"),
  X("Quadrilobe bottle","Bouchon Quadrilobe · quatrefoil stopper","Guerlain's house bottle with a four-lobed stopper, Baccarat design #24.","Guerlain","c1908",PI_G,
    [("Baccarat design #24","Baccarat","c1908",""),("Pochet du Courval and Cristalleries de Nancy production","","","")],"stopper · size · perfume inside"),
  X("Tortue bottle","Flacon Tortue · turtle","Guerlain flacon made by Baccarat and Pochet du Courval.","Guerlain","c1914",PI_G,[("production run","Baccarat","c1914–1995","")],"crystal · size"),
  X("Djedi bottle","","Guerlain flacon designed by George Chevalier, Baccarat design #598.","Guerlain","c1926",PI_G,[],"crystal"),
  X("Chanel No. 5 bottle","No. 5 flacon","Plain rectangular bottle with an octagonal stopper, conceived as an alternative to ornate Lalique and Baccarat crystal.","Chanel","1922",W+"Chanel_No._5",
    [("Original bottle","Chanel","1922","thin glass, rounded shoulders, small glass plug"),("Faceted bottle and octagonal stopper","Chanel","1924","only significant redesign"),
     ("Pocket flacon","Chanel","1934","purse size"),("Bevel-cut stopper","Chanel","1950s","larger, thicker"),("Re-proportioned stopper","Chanel","1986",""),
     ("Red crystal limited edition","Chanel","2018","Christmas edition")],"size · concentration · stopper generation"),
  X("Shocking torso","Shocking bottle","Female-torso bottle by Leonor Fini based on Mae West's figure, with a measuring tape at the shoulders.","Schiaparelli","1937",
    "https://dazeddigital.com/fashion/article/69984/1/schiaparelli-fashion-becomes-art-exhibition-london-most-shocking-designs",[],"size · glass dome · flowers"),
  X("Le Roy Soleil","Le Roi Soleil","Salvador Dalí's sun-stopper bottle on a wave-beaten rock, in a gilt shell-shaped case.","Schiaparelli","1946",
    "https://www.boijmans.nl/en/collection/artworks/146003/le-roy-soleil",[("Baccarat limited edition","Baccarat","1947","two thousand made")],"gilded pressed glass · gilt metal case"),
  X("L'Air du Temps doves","twin-dove bottle","Nina Ricci bottle with a stopper of two crystal doves, designed by Marc Lalique.","Nina Ricci","1948",W+"Nina_Ricci_(brand)",
    [("Original bottle by René Lalique","Lalique","1948",""),("Twin-dove crystal bottle by Marc Lalique","Lalique","","")],"crystal · size · factice versions"),
  X("Classique torso","Jean Paul Gaultier (original name) · corset bottle","Corset-shaped bust bottle, a modern version of Schiaparelli's Shocking torso, often re-dressed.","Jean Paul Gaultier","1993",
    "https://www.jeanpaulgaultier.com/uk/en/gaultier-universe/classique-30-years/the-secrets-of-an-haute-couture-perfume",
    [("Dressed editions","Jean Paul Gaultier","","sequins, lace, tattoo mesh, rainbow sailor top and others")],"corset 'dress' · size · tin can"),
  X("Le Male torso","","Male torso in a striped marinière, sold in an aluminium can; counterpart to Classique.","Jean Paul Gaultier","1995",W+"Le_Male",[],"marinière stripes · size · can"),
 ]},
{"n":"Antique scent bottle","a":"scent bottle · smelling bottle · scent flask",
 "d":"Hand-made scent bottle from before about 1920, collected for its glass, silver mounts and form; period is an attribute.",
 "t":["Georgian (1714–1837)","Victorian","Art Nouveau","cut glass","Bristol blue","silver overlay","silver-gilt mount","opaline"],
 "s":LA,
 "x":[
  X("Double-ended scent bottle","double scent bottle · scent and vinaigrette","Cylindrical bottle holding scent at one end and smelling salts or a vinaigrette at the other.","","c1860–1880s",
    "https://proantic.com/en/702701-an-victorian-gold-double-ended-crystal-scent-bottle.html",
    [("Gold-mounted crystal","","c1860–1870","guilloché gold caps, pierced vinaigrette grille"),("Cranberry glass, silver mounts","Sampson Mordan","Victorian","")],"glass colour · silver or gold caps · length"),
  X("Cameo glass scent bottle","Webb cameo scent bottle","Layered glass bottle with the opaque outer layer carved away to leave a raised design.","Thomas Webb & Sons","19th century",W+"Thomas_Webb_%26_Sons",
    [("Swan","Thomas Webb & Sons","",""),("Albatross","Thomas Webb & Sons","","")],"two or three colours · silver mount · form"),
  X("Silver-mounted scent bottle","Mordan scent bottle","Glass bottle with a hinged silver or silver-gilt top, a staple of Victorian silversmiths.","Sampson Mordan","Victorian",LA,
    [("Amethyst glass","Sampson Mordan","Victorian","")],"glass colour · silver hallmark · cap form"),
  X("Chatelaine scent bottle","","Small bottle of scent or smelling salts hung from a chatelaine at the waist.","","19th century",W+"Chatelaine_(chain)",[],"glass or silver · chain fitting"),
 ]},
{"n":"Factice (display dummy)","a":"factice · dummy bottle · display bottle · giant bottle",
 "d":"Store display bottle, often oversized, filled with coloured liquid or empty and not for sale as perfume.",
 "t":["oversized (giant)","standard-size dummy","sealed with coloured liquid","empty"],
 "s":"https://www.guinnessworldrecords.com/world-records/375466-largest-collection-of-giant-dummy-perfume-bottles-factices",
 "m":[["L'Air du Temps giant factice","Nina Ricci"]]},
{"n":"Czech crystal perfume bottle","a":"Bohemian perfume bottle · Czechoslovakian perfume bottle · Czech vanity bottle",
 "d":"Interwar Czechoslovak glass perfume bottle with a large moulded or intaglio stopper, often enamelled or jewelled.",
 "t":["intaglio stopper","double intaglio","jewelled metalwork","enamelled","coloured glass","dauber"],
 "s":JOA,
 "x":[
  X("Ingrid","Schlevogt Ingrid","Henry Schlevogt's line named after his daughter; won a Grand Prix at the 1937 Paris exhibition.","Schlevogt","1934",JOA,[],"glass colour · moulded design"),
  X("Hoffmann hanging nude bottle","Hoffmann dauber bottle","Bottle whose stopper carries a hanging nude figure, a known Heinrich Hoffmann design.","Heinrich Hoffmann","1924–1926",JOA,[],"glass colour · stopper figure · original vs reproduction base"),
  X("Vogel & Zappe intaglio bottle","","Bottle with a large intaglio or double-intaglio stopper.","","1935",JOA,[],"stopper size · intaglio scene"),
  X("Josef Schmidt bottle","","Workshop credited with registering the first Czech design of this style.","","1924",JOA,[],""),
  X("Jewelled Czech bottle","Neiger jewelled bottle","Bottle dressed with gilt filigree and glass jewels by specialist firms such as Neiger Brothers or Turriet & Bardach.","","1928–1938",JOA,[],"metal stamp (Czechoslovakia or Austria) · jewel colours"),
 ]},
{"n":"Attar bottle","a":"oil bottle · itr bottle · attardan · Egyptian perfume bottle",
 "d":"Small decorative bottle for perfume oils, such as Egyptian hand-blown glass or Indian perfume boxes.",
 "t":["hand-blown glass","gilt decoration","with dipper stopper","miniature","silver box set"],
 "s":EI,
 "x":[
  X("Egyptian hand-blown perfume bottle","Cairo perfume bottle · genie bottle","Mouth-blown glass bottle with a hand-formed neck and stopper, sold for perfume oils.","","",EI,
    [("Pyrex blown-glass bottles","","","sold in Khan el-Khalili perfumeries, Cairo")],"height · colour · stopper shape"),
  X("Attardan","perfume box","Silver box holding several scent bottles whose stoppers end in small scooping spoons.","","18th century",
    "https://michaelbackmanltd.com/object/mughal-deccan-perfume-set-attardan",[("Mughal or Deccan six-bottle box","","18th century","high-grade silver, lockable")],"metal · number of bottles"),
 ]},
{"n":"Refillable travel atomiser","a":"travel spray · perfume atomiser · purse spray",
 "d":"Small refillable spray filled from a full-size bottle, for carrying perfume in a pocket or bag.",
 "t":["pump-fill (bottom-fill)","funnel-fill","glass","aluminium case","5 ml"],
 "s":"https://www.johnlewis.com/travalo-milano-refillable-perfume-atomiser/p114514145",
 "x":[X("Travalo","","Pump-to-fill atomiser that refills from most standard perfume bottles without spills or air exposure.","Travalo","",
    "https://www.johnlewis.com/travalo-milano-refillable-perfume-atomiser/p114514145",[("Milano","Travalo","","5 ml, Genie-S pump, up to 65 sprays")],"case finish · capacity")]},
{"n":"Bulb atomiser","a":"perfumizer · puffer bottle · squeeze-bulb atomiser",
 "d":"Vanity perfume bottle with a squeeze bulb, often netted or tasselled, that blows scent out as a mist.",
 "t":["netted bulb","tasselled bulb","art glass","cut glass","bulb only (replacement)"],
 "s":CW,
 "x":[X("DeVilbiss perfumizer","DeVilbiss atomizer","American bulb atomiser with crocheted bulb netting; glass made to DeVilbiss designs by other glassworks.","DeVilbiss","1905",CW,
    [("Aurene glass atomisers","DeVilbiss","","Steuben blue and gold Aurene, signed DeVilbiss"),("Draped ladies","DeVilbiss","","glass by Cambridge")],"glass maker · bulb netting · metal fittings")]},
]
brands=[
 {"n":"Lalique","c":"France","f":"1888","seg":"Art glass & crystal","d":"Glassmaker founded by René Lalique, whose moulded perfume bottles for Coty from 1907 helped create the designer flacon.","lines":["Lalique perfumes (from 1992)"],"eras":["René Lalique, 1888–1945","Marc Lalique, 1945–1977","Marie-Claude Lalique, 1977–1994"],"sig":["Lalique for Coty","Dans la Nuit (Lalique for Worth)","L'Air du Temps doves"],"sc":[],"rel":["Coty","Baccarat","Nina Ricci"],"s":W+"Lalique"},
 {"n":"Baccarat","c":"France","f":"1764","seg":"Crystal","d":"Lorraine crystal works that made perfume bottles for many houses, over 4,000 a day by 1907.","lines":["Baccarat Rouge 540"],"eras":[],"sig":["Shalimar bottle","Le Roy Soleil","Quadrilobe bottle"],"sc":[],"rel":["Guerlain","Schiaparelli","Lalique"],"s":W+"Baccarat_(company)"},
 {"n":"Guerlain","c":"France","f":"1828","seg":"Perfume house","d":"Paris perfume house founded by Pierre-François Pascal Guerlain, owned by LVMH since 1994.","lines":["Shalimar","Mitsouko","L'Heure Bleue"],"eras":[],"sig":["Shalimar bottle","Bee bottle","Quadrilobe bottle"],"sc":[],"rel":["Baccarat"],"s":W+"Guerlain"},
 {"n":"Schiaparelli","c":"France","f":"1927","seg":"Couture house","d":"Elsa Schiaparelli's Paris house, known for surrealist collaborations; revived under Tod's Group.","lines":["Shocking"],"eras":["Elsa Schiaparelli, 1927–","Daniel Roseberry, 2019–"],"sig":["Shocking torso","Le Roy Soleil"],"sc":[],"rel":["Baccarat","Jean Paul Gaultier"],"s":W+"Schiaparelli_(fashion_house)"},
 {"n":"Chanel","c":"France","f":"1910","seg":"Couture house","d":"Paris house founded by Gabrielle 'Coco' Chanel; No. 5 (1921) is its signature perfume.","lines":["No. 5","Coco Mademoiselle","Bleu de Chanel"],"eras":["Karl Lagerfeld, 1983–2019","Virginie Viard, 2019–2024","Matthieu Blazy, 2024–"],"sig":["Chanel No. 5 bottle"],"sc":[],"rel":[],"s":W+"Chanel"},
 {"n":"Nina Ricci","c":"France","f":"1932","seg":"Couture house","d":"Paris house founded by Nina Ricci and her son Robert, owned by Puig since 1998.","lines":["L'Air du Temps","Nina"],"eras":[],"sig":["L'Air du Temps doves"],"sc":[],"rel":["Lalique"],"s":W+"Nina_Ricci_(brand)"},
 {"n":"Jean Paul Gaultier","c":"France","f":"1982","seg":"Fashion house","d":"Paris fashion label whose torso bottles are among the best-known modern flacons; fragrances by Puig since 2016.","lines":["Classique","Le Male","Scandal"],"eras":["Jean Paul Gaultier, 1982–2020"],"sig":["Classique torso","Le Male torso"],"sc":[],"rel":["Schiaparelli"],"s":W+"Jean_Paul_Gaultier"},
 {"n":"Coty","c":"France","f":"1904","seg":"Beauty group","d":"Beauty company founded in Paris by François Coty, early patron of Lalique bottles.","lines":[],"eras":[],"sig":["Lalique for Coty"],"sc":[],"rel":["Lalique","Baccarat"],"s":W+"Coty"},
 {"n":"Thomas Webb & Sons","c":"United Kingdom","f":"1837","seg":"Art glass","d":"Stourbridge glassworks known for cameo glass, including scent bottles.","lines":[],"eras":[],"sig":["Cameo glass scent bottle"],"sc":[],"rel":["Sampson Mordan"],"s":W+"Thomas_Webb_%26_Sons"},
 {"n":"Sampson Mordan","c":"United Kingdom","f":"1822","seg":"Silversmith","d":"London silver firm best known for mechanical pencils, also silver-mounted scent bottles; factory destroyed in 1941.","lines":[],"eras":[],"sig":["Silver-mounted scent bottle"],"sc":[],"rel":["Thomas Webb & Sons"],"s":W+"Sampson_Mordan"},
 {"n":"Schlevogt","c":"Czechoslovakia","f":"","seg":"Glass export firm","d":"Jablonec firm of Curt and Henry Schlevogt; Henry's Ingrid bottles date from 1934.","lines":["Ingrid"],"eras":[],"sig":["Ingrid"],"sc":[],"rel":["Heinrich Hoffmann"],"s":JOA},
 {"n":"Heinrich Hoffmann","c":"Czechoslovakia","f":"","seg":"Glass maker","d":"Costume-jewellery stone exporter who turned to artistic glass in 1926 and is known for figural perfume bottles.","lines":[],"eras":[],"sig":["Hoffmann hanging nude bottle"],"sc":[],"rel":["Schlevogt"],"s":JOA},
 {"n":"DeVilbiss","c":"United States","f":"1887","seg":"Atomiser maker","d":"Medical-atomiser firm that added perfume atomisers from 1905 and sold up to a million a year in the mid-1920s.","lines":["Perfumizer"],"eras":["Dr Allen DeVilbiss, from 1887","Tom DeVilbiss, from 1905"],"sig":["DeVilbiss perfumizer"],"sc":[],"rel":[],"s":CW},
]
trads=[
 {"n":"Czech (Bohemian) perfume-bottle glass","g":"Ceramics & glass","r":"Bohemia, Czechoslovakia (Jablonec nad Nisou)","p":"c1924–1938",
  "d":"Interwar export trade in figural and cut perfume bottles drawing on centuries of Bohemian glassmaking.",
  "tech":"press-moulded stoppers, mould-blown bases, selective polishing, intaglio, enamelling, jewelled metal mounts",
  "mat":"glass; gilt metal; glass jewels","forms":["Czech crystal perfume bottle"],
  "ctr":["Jablonec nad Nisou","Heinrich Hoffmann","Schlevogt (Ingrid)","Josef Schmidt","Vogel & Zappe","Johann Umann","Neiger Brothers (jewelling)"],
  "auth":"'Made in Czechoslovakia' acid stamp on the base; Turriet & Bardach metal stamped Austria; post-war Glassexport bottles usually lack the stamp; Hoffmann reproductions often have a different base shape.","s":JOA},
 {"n":"Egyptian hand-blown perfume glass","g":"Ceramics & glass","r":"Egypt (Cairo)","p":"present day",
  "d":"Mouth-blown decorative bottles sold for perfume oils, notably in the perfume shops of Khan el-Khalili.",
  "tech":"free blowing with a blowpipe; neck and stopper formed by hand","mat":"glass","forms":["Attar bottle"],
  "ctr":["Khan el-Khalili perfumeries, Cairo"],"auth":"Hand-made pieces vary in height and shape from bottle to bottle.","s":EI},
]
notes=("No old data for this shelf; all seven planned kinds are new and sourced. Art-glass bottles (Lalique, Webb cameo, Czech) should cross-link to F2. "
 "Left out: lay-down bottles (no retrieved source defines the form); Georgian cut-glass archetype (only a category label found); Mordan mounts on Webb cameo bottles (Corning page blocked, 403); "
 "Shalimar 'Chauve Souris' link (not on fetched page); Guerlain Bee bottle date (source gives c1818, before the house's 1828 founding, so left blank); "
 "Indian itardan and Mughal jewelled flasks beyond the attardan (search snippets only); Travalo brand entry (only a retailer product page retrieved); Marcel Franck atomisers (unsourced). "
 "Factice has no archetypes; one example from the Guinness record page.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/H4/shelves/02_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p); print('written')
