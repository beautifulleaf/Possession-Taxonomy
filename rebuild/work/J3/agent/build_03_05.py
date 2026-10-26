import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,mk='',y='',a='',v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
grana = {"n":"Parmigiano Reggiano & grana","a":"Parmesan · grana-type hard cheese · Grana Padano",
 "d":"Hard, granular, long-aged cow's-milk cheese of the grana type, split rather than sliced and often grated.",
 "t":["whole wedge","grated","shavings"],"s":"https://www.belgioioso.com/Products/",
 "x":[
  X("Parmigiano Reggiano","Grana from Parma, Reggio Emilia and nearby provinces, aged at least 12 months; the originator of the type.",W+"Parmesan",
    y="earliest record 1254",a="Parmesan (outside the EU) · Parmigiano",
    v=[("12–18 months","","","youngest, milky"),("20–24 months","","","typical maturity"),("30–36 months","","","crumblier, nutty"),("over 40 months","","","extra-aged"),
       ("Vacche Rosse","Consorzio Vacche Rosse","1990s","Reggiana red-cow milk, aged at least 24 months; sold at 24–72 months"),
       ("Vacca Bruna","Caseificio San Pier Damiani","","Bruna-cow milk, 40 months"),
       ("Prodotto di Montagna","","","mountain-area dairies, consortium quality project"),
       ("Organic 30 mesi (Borgo del Gazzano)","Consorzio Gourm.it","",""),
       ("30–39 months","Rastelli Fratelli (Nazionale Parmigiano Reggiano)","",""),
       ("min 36 months","Zanetti","",""),
       ("Parmigiano Reggiano PDO","Ferrari Giovanni Industria Casearia spa","",""),
       ("Parmigiano Reggiano","Cravero","","")],
    dt="age 12–18 · 20–24 · 30–36 · 40+ months · breed (Friesian, Reggiana, Bruna) · mountain product · first or medium grade"),
  X("Grana Padano","Po Valley grana from semi-skimmed raw milk, less strictly regulated than Parmigiano Reggiano.",W+"Grana_Padano",
    y="12th century (Chiaravalle Abbey monks)",
    v=[("Grana Padano","","","9–16 months"),("Grana Padano oltre 16 mesi","","","over 16 months"),("Grana Padano Riserva","","","over 20 months"),
       ("Grana Padano DOP Collezione","Consorzio Gourm.it","",""),("Selezione da Fieno 50 Mesi","Latteria Agricola S. Pietro","","hay-fed, 50 months"),
       ("Grana Padano","Zanetti","","")],
    dt="age class · wheel 24–40 kg · grated or wedge"),
  X("Trentingrana","Trentino mountain grana from raw milk of cows fed grass and hay, a territorial specificity within the Grana Padano PDO.","https://www.formaggideltrentino.it/en/trentingrana",
    y="1926",v=[("20 months","","",""),("30 months","","",""),("Trentingrana di alpeggio","","","summer alpine-pasture milk; Slow Food Presidium")],
    dt="age 20–30 months · valley or alpine-pasture milk"),
  X("Sbrinz","Very hard Swiss grating cheese from Central Switzerland, made in about 42 dairies.",W+"Sbrinz",a="Sbrinz AOP",dt="age · grated, broken or shaved"),
  X("Bagòss","Raw-milk hard cheese of Bagolino tinted with saffron, rind oiled with linseed oil; 'poor man's grana'.",W+"Bag%C3%B2ss",
    a="Bagòs · Bagoss di Bagolino",y="Slow Food Presidium 1999",dt="age 12 months to 3 years"),
  X("Reggianito","Argentinian small-wheel hard grating cheese created by Italian immigrants after Parmigiano Reggiano.",W+"Reggianito",
    v=[("Reggianito 18 meses","Lácteos Vaquero","",""),("Reggianito","Lácteos Vaquero","",""),("Man Reggianito","Man S.A.","",""),
       ("Santa Rosa Reggianito","Santa Rosa (quesería)","",""),("Queso Reggianito Rallado","Colun","","grated")],
    dt="wheel about 6.8 kg · age 5–6 months and longer · grated or wedge"),
  X("Džiugas","Lithuanian long-aged hard cheese with PGI status, made by Žemaitijos Pienas in Telšiai.","https://www.dairyreporter.com/Article/2019/08/12/Lithuanian-cheese-Dziugas-gets-PGI-status/",
    mk="Žemaitijos Pienas",y="PGI 2019",v=[("100 months","Žemaitijos Pienas","","extra-aged")],dt="age in months · grated or wedge"),
  X("American Grana","Wisconsin-made extra-aged Parmesan-style cheese.","https://www.belgioioso.com/Products/",mk="BelGioioso",
    v=[("American Grana","BelGioioso","",""),("Extra Aged American Grana","BelGioioso","","aged at least 24 months")],dt="age · wedge or grated")],
 "m":[["Parmesão Faixa Azul","Vigor"],["Queijo Parmesão Cilindro","Piracanjuba"],["Queijo Parmesão","Quatá"],["Treze Tílias Queijo Parmesão Preto","Laticínios Tirol"],
      ["Parmesão Cunha Barão Premiado","Queijo Barão da Canastra"],["Casarias Parmesano","Casarias S.A."],["Man Parmesano","Man S.A."],
      ["Queso Parmesano Rallado","Colun"],["Himalayan Parmesan","Darima Farms"],["Parmesan","BelGioioso"]]}
pec = {"n":"Pecorino","a":"Italian sheep's-milk cheese","d":"Firm to hard Italian sheep's-milk cheese, salted and aged; young for the table, old for grating.",
 "t":["fresco/dolce","semi-aged","aged/stagionato","peppered","rind-treated"],"s":"https://www.cheese.com/pecorino-romano/",
 "x":[
  X("Pecorino Romano","Hard, salty grating pecorino of Roman origin, now made mostly in Sardinia, also Lazio and Grosseto.",W+"Pecorino_romano",
    y="ancient (described by Varro and Pliny)",dt="age 5 months or more · wheel 20–35 kg"),
  X("Pecorino Toscano","Firm Tuscan sheep's-milk cheese, PDO since 1996.",W+"Pecorino_toscano",dt="age"),
  X("Pecorino Sardo","Uncooked Sardinian pecorino from Sarda-sheep milk.",W+"Pecorino_sardo",y="PDO 1996",
    v=[("Pecorino sardo dolce","","","20–60 days"),("Pecorino sardo maturo","","","over 2 months")],dt="dolce or maturo"),
  X("Pecorino Siciliano","Semi-hard Sicilian pecorino of about 12 kg, of classical Greek ancestry.",W+"Pecorino_siciliano",y="DOC 1955",dt="age"),
  X("Fiore Sardo","Raw Sarda-sheep's-milk hard uncooked cheese, briefly brined and lightly smoked.","https://www.sardegnaagricoltura.it/index.php?xsl=443&s=45051&v=2&c=3592",
    y="PDO 1996",v=[("Shepherds’ Fiore Sardo","","","shepherd-made")],dt="age · smoked rind treated with oil and vinegar"),
  X("Formaggio di fossa","Cheese matured for three months in tufa pits at Sogliano al Rubicone.",W+"Formaggio_di_fossa",a="Formaggio di Fossa di Sogliano PDO · fossa",
    y="14th century; PDO 2009",v=[("Ambra di Talamello","","","made in Talamello")],dt="sheep or mixed milk · pit-aged"),
  X("Pecorino di Filiano","Firm sheep's-milk cheese from the province of Potenza, Basilicata.",W+"Pecorino_di_Filiano",y="PDO 2007"),
  X("Pecorino di Picinisco","Italian PDO sheep's-milk cheese of Picinisco, Lazio.","https://www.wikidata.org/wiki/Q140642329"),
  X("Piacentinu Ennese","Sicilian pecorino from Enna with saffron and whole black peppercorns in the paste.","https://wikicibo.com/en/prodotti/latticini-e-formaggi/piacentinu-ennese",
    y="PDO 2011",dt="age · young for slicing, aged for grating"),
  X("Canestrato","Hard basket-moulded sheep's- and goat's-milk cheese of southern Italy.",W+"Canestrato",
    v=[("Canestrato Pugliese","","","PDO, province of Foggia"),("Canestrato di Moliterno","","","Basilicata, PGI, at least 60 days"),("Canestrato of Castel del Monte","","","Abruzzo")],
    dt="basket-marked rind · age")],
 "m":[["Pecorino Bislacco al Rum e Tabacco","F.lli Petrucci"],["The English Pecorino","White Lake Cheese"],["Pecorino a latte crudo della Maremma",""],
      ["Pecorino della montagna pistoiese",""],["Pecorino di Carmasciano",""],["Sibillini Mountains Pecorino",""],["Farindola Pecorino",""],
      ["Osilo Pecorino",""],["Alta Baronia Sheep Cheese",""],["Escalaplano Axridda Cheese",""]]}
asi = {"n":"Asiago","d":"Pressed cow's-milk cheese of the Asiago plateau type, fresh (pressato) or aged (d'allevo).",
 "s":"https://stopandshop.com/groceries/product/belgioioso-aged-asiago-cheese-wedge-8-oz-pkg/328650",
 "x":[X("Asiago","Cow's-milk cheese first made at Asiago, smooth when fresh and crumbly when aged.",W+"Asiago_cheese",a="Asiago PDO",
    v=[("Asiago pressato","","","fresh, pressed"),("Asiago d'allevo","","","aged"),("Asiago","BelGioioso","","US-made, aged"),("Fresh Asiago","BelGioioso","","US-made, young")],
    dt="pressato or d'allevo · age"),
  X("Monte Veronese","Lessini Mountains cow's-milk cheese which, like Asiago, comes fresh or matured.",W+"Monte_Veronese",y="PDO 1996",dt="fresh or matured")]}
mon = {"n":"Montasio & Piave","a":"north-east Italian mountain cheese","d":"Firm cooked cow's-milk cheeses of Friuli and the Veneto Dolomites, sold by age.",
 "s":W+"Montasio",
 "x":[X("Montasio","Cow's-milk mountain cheese of Friuli-Venezia Giulia and the Veneto.",W+"Montasio",y="PDO 1986",dt="age"),
  X("Piave","Hard cooked cow's-milk cheese of the province of Belluno, named after the Piave river.",W+"Piave_cheese",a="Piave DOP",
    v=[("Piave Fresco","","","20–60 days, blue label"),("Piave Mezzano","","","61–180 days, blue label"),("Piave Vecchio","","","over 6 months, blue label"),
       ("Piave Vecchio Selezione Oro","","","over 12 months, red label"),("Piave Vecchio Riserva","","","over 18 months, black label")],
    dt="age and label colour")]}
mtn = {"n":"Italian mountain cheese","a":"formaggi d'alpeggio · Alpine Italian PDO cheese",
 "d":"Pressed cow's-milk cheeses of the Italian Alps and Piedmont, often from summer pasture milk.","s":W+"Castelmagno_cheese",
 "x":[X("Castelmagno","Piedmontese PDO cheese of the province of Cuneo.",W+"Castelmagno_cheese",dt="age · alpine-pasture or valley"),
  X("Bra","Cuneo cheese, soft after 45 days or hard after six months.",W+"Bra_cheese",v=[("Bra (soft)","","","at least 45 days"),("Bra (hard)","","","aged up to six months")],dt="age · milk mix"),
  X("Raschera","Semi-hard pressed cow's-milk cheese of Cuneo, sometimes with sheep's or goat's milk.",W+"Raschera",y="DOP 1996",
    v=[("Raschera di alpeggio","","","mountain pasture")],dt="round or square · age"),
  X("Bitto","Raw-milk alpine cheese of the Orobie valleys, optionally with up to 10% goat's milk.","https://it.wikipedia.org/wiki/Bitto_(formaggio)",y="DOP 1996",
    v=[("Bitto DOP","","","alpine pasture and barn, at least 70 days"),("Storico Ribelle","","2016","former Bitto Storico; summer pasture only, goat's milk required")],dt="age from 70 days to years"),
  X("Valtellina Casera","Semi-skimmed cow's-milk cheese of the province of Sondrio, used in pizzoccheri.",W+"Valtellina_Casera",y="16th century; PDO 1996",dt="age"),
  X("Formai de Mut","Raw-milk cheese of the high pastures of the Alta Valle Brembana, Bergamo.",W+"Formai_de_Mut_dell%27Alta_Valle_Brembana",y="PDO 1996"),
  X("Silter","Brined hard raw-milk cheese of the province of Brescia, aged at least six months.",W+"Silter",y="PDO 2015"),
  X("Puzzone di Moena","Washed-rind semi-hard raw-milk cheese of the Fassa and Fiemme valleys.",W+"Puzzone_di_Moena",a="Spretz tzaorì",y="PDO 2013"),
  X("Vezzena","Cow's-milk cheese of the Lavarone, Vezzena and Folgaria plateau, Trentino.",W+"Vezzena"),
  X("Spressa delle Giudicarie","Low-fat cow's-milk cheese of Trentino, eaten fresh or aged over six months.",W+"Spressa_delle_Giudicarie",dt="age")],
 "m":[["Nostrano Valtrompia PDO",""]]}
brands=[{"n":"BelGioioso","c":"United States","f":"1979","seg":"Italian-style cheese maker","d":"Wisconsin cheese maker founded by Errico Auricchio, of the Neapolitan Auricchio family.",
 "lines":["American Grana","Asiago","Romano","Parmesan","Provolone"],"eras":["Errico Auricchio, founder, 1979–"],"sig":["American Grana"],"sc":[],"rel":["Auricchio","Polly-O"],"s":W+"BelGioioso_Cheese"}]
notes=("Parmesan renamed 'Parmigiano Reggiano & grana'; 8 archetypes (PR originator with age/breed/mountain versions, Grana Padano age classes, Trentingrana, Sbrinz, Bagòss, Reggianito, Džiugas, American Grana). "
 "Brazilian/Chilean parmesão SKUs kept as flat m (no attested archetype); Lidl Deluxe 30M store SKU dropped. "
 "Pecorino: 10 archetypes; non-Italian old models moved out: Idiazábal, Roncal, Zamorano, Carranzana Cara Negra -> Spanish cheese shelf; Ossau-Iraty -> Pyrenean sheep cheese; Kefalograviera, Ladotyri Mytilinis -> Greek hard cheese; Paški sir, Bovški sir -> regional pressed/Balkan; Texel Sheep Cheese -> Dutch & Nordic. "
 "Asiago gains Monte Veronese. New kinds Montasio & Piave and Italian mountain cheese sourced. Nostrano Valtrompia kept as m (no page retrieved). "
 "Not attested so left out: Pecorino Crotonese, Granone Lodigiano, Džiugas age range beyond 100 months, PR 18-month Premium mark details. Toma, Fontina, Berner Alpkäse, Ragusano and Caciocavallo left to Alpine/stretched-curd shelves. No traditions (PDO consortia rather than craft traditions); Žemaitijos Pienas has no brand entry (only a news page retrieved).")
out={"kinds":[grana,pec,asi,mon,mtn],"brands":brands,"traditions":[],"notes":notes}
p='work/J3/shelves/03_05.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(sum(len(k.get('x',[])) for k in out['kinds']),'archetypes')
