import json,os
W='https://en.wikipedia.org/wiki/'
L=W+'List_of_pasta'
R='https://ronzoni.com/products'
def A(n,d,s=L,dt="",a=""):return {"n":n,"a":a,"d":d,"mk":"","y":"","s":s,"dt":dt}
k=[
{"n":"Long-strand pasta","a":"","d":"Long cut strands of durum pasta, solid or hollow.","s":R,"t":["Dried","Fresh","Wholemeal","Bronze-die"],
 "x":[A("Spaghetti","'Little strings' from spago, twine; the standard long pasta."),
 A("Linguine","'Little tongues'; flattened spaghetti."),
 A("Bucatini","Thick spaghetti with a hole through the centre, typical of Lazio and Rome.",W+"Bucatini",a="perciatelli"),
 A("Vermicelli","'Little worms'; thin strands from Campania."),
 A("Capellini","'Thin hair'; very fine strands from Liguria.")],
 "m":[["Whole grain thin spaghetti",""]]},
{"n":"Tube pasta","a":"","d":"Short hollow cuts of durum pasta.","s":R,"t":["Smooth (lisce)","Ridged (rigate)"],
 "x":[A("Penne","Short tubes cut on the diagonal; patented as a cutting machine in 1865 in Liguria.",W+"Penne","lisce, rigate, pennoni; mostaccioli in English-language packs"),
 A("Rigatoni","Wide grooved tubes from Lazio."),
 A("Paccheri","Large smooth tubes from Naples."),
 A("Macaroni","Tube pasta whose name comes from Greek for a barley food; linked to Naples."),
 A("Ziti","Tubes from Sicily and southern Italy; name means bride and bridegroom in Sicilian.")],
 "m":[["Elbows",""],["Macarrones",""]]},
{"n":"Short and twisted pasta","a":"","d":"Short solid shapes of durum pasta, twisted, shell or bow.","s":R,
 "x":[A("Fusilli","Spindle-shaped spiral."),A("Farfalle","'Butterflies', bow-tie shapes from northern Italy."),A("Orecchiette","'Little ears' from Apulia."),A("Conchiglie","Shell shapes."),A("Cavatappi","Corkscrew shapes.")],
 "m":[["Medium shells",""]]},
{"n":"Egg pasta, ribbons and nests","a":"","d":"Pasta or noodles made with egg in the dough, cut into ribbons or coiled nests.","s":R,"t":["Fresh","Dried nests"],
 "x":[A("Tagliatelle","Ribbons cut from egg pasta, from Emilia-Romagna and Bologna.",dt="Italian egg pasta needs at least four eggs per kg of semolina"),
 A("Pappardelle","Wide ribbons from Tuscany and northern Italy."),A("Fettuccine","'Little ribbons', Roman.")],
 "m":[["Tagliatelle nests",""]]},
{"n":"Filled pasta","a":"stuffed pasta","d":"Pasta wrapped around a filling, sold fresh, chilled or dried.",
 "s":W+"Filled_pasta","t":["Fresh (chilled)","Dried","Frozen"],
 "x":[A("Ravioli","Filled squares; 'raviolo' is a generic term for almost any filled pasta."),
 A("Tortellini","Filled pasta named with ravioli as a leading Italian example.",W+"Filled_pasta"),
 A("Agnolotti","Piedmontese stuffed pasta, usually roasted meat; the Montferrat variant uses donkey meat.",W+"Agnolotti")]},
{"n":"Soup pasta","a":"pastina","d":"Very small shapes of durum pasta for cooking in broth.","s":R,
 "x":[A("Orzo","Rice-shaped pasta, also risoni and kritharaki.",W+"Orzo"),A("Stelline","'Stars'."),A("Fregola","'Little fragments' from Sardinia, toasted pasta grains."),A("Acini di pepe","'Grains of pepper'.")],
 "m":[["Acini di pepe",""]]},
{"n":"Potato gnocchi","a":"","d":"Small unfilled dumplings of potato dough.","s":"https://www.coles.com.au/product/coles-kitchen-potato-gnocchi-500g-3167363","t":["Fresh (chilled)","Shelf-stable","Frozen"],
 "x":[A("Potato gnocchi","Potato, wheat flour, egg and salt; common in Lombardy, Abruzzo, Friuli, Veneto and Lazio since the late 19th century.",W+"Gnocchi")]},
{"n":"Couscous","a":"","d":"Steamed and dried semolina granules, plus Israeli (pearl) couscous and fregola.","s":L,"t":["Fine","Medium","Israeli (ptitim, pearl)","Fregola"],
 "x":[A("Israeli couscous (ptitim)","Larger toasted wheat pasta pearls from Israel."),A("Fregola","Sardinian toasted semolina pasta grains.")]}]
G='https://www.scattidigusto.it/pasta-di-gragnano-8-marche-migliori'
def B(n,c,seg,kf,d,s=G):return {"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s}
br=[B("Pastificio dei Campi","Italy","Artisan & independent","Gragnano IGP","Gragnano pasta maker rated top quality in a tasting."),
B("Pastificio Faella","Italy","Artisan & independent","Gragnano pasta","Gragnano pasta maker rated top quality in a tasting."),
B("Pastificio Afeltra","Italy","Artisan & independent","Gragnano IGP","Member of the Gragnano consortium."),
B("Di Martino","Italy","Premium","Gragnano IGP","Member of the Gragnano consortium; bronze-die pasta."),
B("Garofalo","Italy","Premium","Gragnano IGP","Member of the Gragnano consortium."),
B("Barilla","Italy","Mainstream","market leader","World's largest pasta maker.","knowledge"),
B("De Cecco","Italy","Mainstream","bronze-die dry pasta","Italian dry pasta maker.","knowledge")]
tr=[{"n":"Pasta di Gragnano","g":"Food & drink","r":"Gragnano, Campania","p":"IGP recognised 30 July 2010","d":"Dry pasta made in Gragnano from durum semolina and Lattari mountain water.","tech":"bronze-die extrusion, slow drying at 40-80 C","mat":"durum semolina, limestone water","forms":["Spaghetti","Paccheri"],"ctr":["Pastificio dei Campi","Afeltra","Di Martino","Garofalo"],"auth":"IGP mark; produced and packed in Gragnano","s":G}]
out={"kinds":k,"brands":br,"traditions":tr,"notes":"Rummo, Setaro, Martelli, Cavalieri, Felicetti not on retrieved pages so omitted. Cavatelli etc. omitted. Shape families used as archetypes, no per-shape producers."}
json.dump(out,open('work/J5/shelves/01_01.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/01_01.tmp','work/J5/shelves/01_01.json')
