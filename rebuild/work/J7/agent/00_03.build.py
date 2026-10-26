import json, os
W="https://en.wikipedia.org/wiki/"
def X(n,d,y,s,a="",v=None,dt=""):
    o={"n":n,"a":a,"d":d,"mk":"","y":y,"s":s}
    if v: o["v"]=v
    if dt: o["dt"]=dt
    return o
def V(n,y,d): return {"n":n,"mk":"","y":y,"d":d}
kinds=[
{"n":"Barbera","a":"Barbera Nera · Barberone","d":"Red wine made mainly from Barbera, a deep-coloured, high-acid, low-tannin grape from Piedmont.","t":["normale","Superiore","Riserva"],"s":W+"Barbera",
 "x":[X("Barbera d'Asti","Piedmont DOCG red of at least 90% Barbera from the Asti hills; the best-known Barbera appellation.","DOC 1970 · DOCG 2008",W+"Barbera_d'Asti",
        v=[V("Barbera d'Asti Superiore","2000","12.5% ABV, 14 months' ageing with 6 in oak or chestnut; may name subzones Tinella or Colli Astiani")],dt="normale · Superiore · subzone"),
      X("Nizza","100% Barbera DOCG from the former Nizza subzone of Barbera d'Asti; yields capped at 7 t/ha.","DOCG 2014",W+"Nizza_DOCG",a="Barbera d'Asti Superiore Nizza",
        v=[V("Nizza Riserva","2014","30 months' total ageing, 12 in barrel"),V("Nizza vigna","2014","single named vineyard, 13.5% ABV minimum")],dt="normale · Riserva · single vineyard"),
      X("Barbera d'Alba","Barbera DOC from the hills around Alba in Piedmont.","",W+"Barbera"),
      X("Barbera del Monferrato","Barbera DOC from Monferrato, often slightly sparkling and rarely exported.","",W+"Barbera",dt="still · frizzante")]},
{"n":"Montepulciano","a":"Montepulciano d'Abruzzo grape · Cordisco","d":"Red wine made mainly from Montepulciano, a deep-coloured grape of central and southern Italy.","t":["normale","Riserva","rosato (Cerasuolo d'Abruzzo)"],"s":W+"Montepulciano_(grape)",
 "x":[X("Montepulciano d'Abruzzo","Abruzzo DOC red of at least 85% Montepulciano, up to 15% Sangiovese.","DOC 1968",W+"Montepulciano_d'Abruzzo",
        v=[V("Montepulciano d'Abruzzo Riserva","","at least two years' ageing, 9 months in wood, 12.5% ABV"),V("Cerasuolo d'Abruzzo","2010","rosato style split into its own DOC")],dt="normale · Riserva · rosato"),
      X("Colline Teramane Montepulciano d'Abruzzo","DOCG of at least 90% Montepulciano from the Teramo hills of Abruzzo.","DOC 1995 · DOCG 2003",W+"Montepulciano_d'Abruzzo"),
      X("Conero","Marche DOCG of at least 85% Montepulciano from the slopes of Monte Conero near Ancona.","",W+"Montepulciano_(grape)",a="Rosso Conero",v=[V("Rosso Conero","","DOC version of the same zone")]),
      X("Offida Rosso","Marche DOCG red with at least 50% Montepulciano.","",W+"Montepulciano_(grape)"),
      X("Rosso Piceno","Marche DOC red blending Montepulciano with Sangiovese.","",W+"Montepulciano_(grape)",v=[V("Rosso Piceno Superiore","","")])]},
{"n":"Aglianico","a":"Aglianico del Vulture grape · Ellenico","d":"Red wine made mainly from Aglianico, a tannic, age-worthy grape of Campania and Basilicata.","t":["normale","Superiore","Riserva"],"s":W+"Aglianico",
 "x":[X("Taurasi","Campania DOCG red from Aglianico with up to 15% other grapes, aged three years including one in wood.","DOC 1970 · DOCG 1993",W+"Taurasi_DOCG",
        v=[V("Taurasi Riserva","","at least four years' ageing")],dt="normale · Riserva"),
      X("Aglianico del Vulture","Basilicata red from Aglianico grown on the volcanic slopes of Monte Vulture.","DOC 1971",W+"Aglianico_del_Vulture",
        v=[V("Aglianico del Vulture Superiore","2011","own DOCG; three years' ageing, 13.5% ABV"),V("Aglianico del Vulture Superiore Riserva","2011","five years' ageing, two in wood")],dt="DOC · Superiore DOCG · Riserva"),
      X("Aglianico del Taburno","Campania DOCG for Aglianico from Monte Taburno near Benevento.","DOCG 2011",W+"Aglianico")]},
{"n":"Nero d'Avola","a":"Calabrese","d":"Red wine made mainly from Nero d'Avola, Sicily's most important red grape.","s":W+"Nero_d'Avola",
 "x":[X("Cerasuolo di Vittoria","Sicilian DOCG blending 50–70% Nero d'Avola with Frappato; Sicily's first DOCG.","DOC 1973 · DOCG 2005",W+"Cerasuolo_di_Vittoria",
        v=[V("Cerasuolo di Vittoria Classico","","from the Classico sub-region"),V("Vittoria DOC","","looser rules over the same area")],dt="normale · Classico"),
      X("Noto and Pachino Nero d'Avola","Nero d'Avola from the districts around Noto and Pachino in south-eastern Sicily, reputed for the grape.","",W+"Nero_d'Avola")]},
{"n":"Nerello Mascalese","a":"Nerello","d":"Red wine made mainly from Nerello Mascalese, a Sicilian grape named after Mascali near Etna.","s":W+"Nerello_Mascalese",
 "x":[X("Etna Rosso","Sicilian DOC red of at least 80% Nerello Mascalese with up to 20% Nerello Cappuccio, from the slopes of Etna.","DOC 1968",W+"Etna_DOC",a="Etna DOC",
        v=[V("Etna Rosato","1968","same grape rules as the red"),V("Etna Spumante","","at least 60% Nerello Mascalese")],dt="rosso · rosato · spumante")]},
{"n":"Touriga Nacional","a":"Touriga · Mortágua","d":"Red wine made mainly or partly from Touriga Nacional, Portugal's leading red grape, also central to Port.","s":W+"Touriga_Nacional",
 "x":[X("Douro DOC red","Unfortified red from the Douro valley, blending Touriga Nacional, Touriga Franca, Tinta Roriz and others.","demarcated 1756",W+"Douro_DOC",a="Douro tinto",
        dt="subregion: Baixo Corgo · Cima Corgo · Douro Superior"),
      X("Dão DOC red","Red from the granite plateau of Dão, at least 20% Touriga Nacional with Tinta Roriz, Jaen and Alfrocheiro.","DOC 1908",W+"Dão_DOC",
        dt="subregions on label: Alva · Besteiros · Castendo · Serra da Estrela · Silgueiros · Terras de Azurara · Terras de Senhorim")]},
{"n":"Monastrell","a":"Mourvèdre · Mataro","d":"Red wine made mainly from Monastrell (Mourvèdre), a tannic, earthy grape of south-east Spain and Provence.","t":["joven","Crianza","Reserva","Gran Reserva","rosé"],"s":W+"Mourvèdre",
 "x":[X("Jumilla","Murcia DO where Monastrell makes up over 85% of plantings.","DO 1966",W+"Jumilla_(DO)",dt="joven · Crianza · Reserva · Gran Reserva"),
      X("Bandol","Provence AOC whose reds hold at least 50% Mourvèdre and age 18 months in oak.","",W+"Bandol_AOC",v=[V("Bandol rosé","","same 50% Mourvèdre minimum")],dt="rouge · rosé"),
      X("Yecla","Murcia DO known for heavy use of Monastrell.","DO 1975",W+"Yecla_(DO)")]},
{"n":"Dolcetto","a":"Ormeasco · Dolsin","d":"Dry, fruity red wine made from Dolcetto, a Piedmont grape usually drunk within a few years.","t":["normale","Superiore"],"s":W+"Dolcetto",
 "x":[X("Dogliani","Piedmont DOCG for Dolcetto from Dogliani, formerly Dolcetto di Dogliani DOC.","DOC 1974 · DOCG 2005",W+"Dolcetto",a="Dolcetto di Dogliani",
        v=[V("Dogliani Superiore","2005","at least one year's ageing, yield 7 t/ha")],dt="normale · Superiore"),
      X("Dolcetto d'Alba","100% Dolcetto DOC from around Alba; Superiore at 12.5% ABV.","",W+"Dolcetto",dt="normale · Superiore"),
      X("Dolcetto di Ovada","Dolcetto from the Ovada area, one of the two largest-volume zones.","",W+"Dolcetto",a="Ovada"),
      X("Diano d'Alba","Dolcetto appellation from Diano d'Alba in the Langhe.","",W+"Dolcetto")]},
{"n":"Refosco","a":"Refošk · Refosco dal Peduncolo Rosso · Teran · Terrano","d":"Powerful, tannic deep-violet red wine from the Refosco family of grapes of north-east Italy, Slovenia and Istria.","s":"https://www.singular.shop/en-si/products/refosk-berce",
 "x":[X("Refosco dal Peduncolo Rosso","Red-stalked Refosco, the best-known type, with leading examples from Friuli Colli Orientali.","",W+"Refosco"),
      X("Kraški teran","Karst Plateau red from the Terrano grape of the Refosco family, best drunk young; EU PDO as Teran.","PDO 2006",W+"Terrano_(grape)",a="Teran · Terrano del Carso · Carso Rosso",
        v=[V("Terrano del Carso","","Italian Carso DOC name")]),
      X("Refosco d'Istria","Green-stalked Refosco grown in Slovenian and Croatian Istria and around Trieste.","",W+"Refosco",a="Refošk · Refosco dal Peduncolo Verde")],
 "m":[["Refošk","Steras"]]},
{"n":"Mencía","a":"Jaen","d":"Still red wine made mainly from Mencía, a grape of north-west Spain and Portugal.","t":["joven","Crianza","Reserva"],"s":"https://www.licorea.com/merayo-mencia-2024-bierzo-en-p-6729.html",
 "x":[X("Bierzo","León DO whose young reds hold at least 70% Mencía.","DO 1989",W+"Bierzo_(DO)",dt="joven · Crianza · Reserva"),
      X("Ribeira Sacra","Galician DO of steep river-canyon vineyards where Mencía is the main red grape.","DO 1996",W+"Ribeira_Sacra_(DO)",dt="subzone: Amandi · Chantada · Quiroga-Bibei · Ribeiras do Miño · Ribeiras do Sil"),
      X("Valdeorras","Galician DO on the Sil river with Mencía as its first recommended red.","DO 1945",W+"Valdeorras_(DO)"),
      X("Jaen do Dão","Mencía under its Portuguese name, part of Dão red blends.","",W+"Mencía_(grape)")],
 "m":[["Cuatro Pasos Black Mencía","Cuatro Pasos"]]},
{"n":"Graciano","a":"Tintilla · Morrastel","d":"Still red wine made mainly from Graciano, a low-yielding, deep-coloured Rioja grape mostly used in blends.","s":"https://www.lcbo.com/en/graciano-vega-vella-rioja-2021-51934",
 "x":[X("Varietal Rioja Graciano","Single-variety Graciano bottled by some Rioja bodegas, though the grape is mainly a blending component.","",W+"Graciano")],
 "m":[["Altos R Pigeage Graciano","Altos R Pigeage"]]},
]
notes=("All 11 planned kinds kept; old k24/k16/k19 merged with their models kept in m. Archetypes are appellations (maker-free, so no brand entries). "
 "Left out: Port as a Touriga Nacional archetype (belongs to Fortified wine); Faro DOC and a separate Barbera d'Alba DOC year (no page retrieved); "
 "Istrian Teran (a different grape per Wikipedia); Navarra/Corsica Graciano (no named appellation). No traditions apply.")
out={"kinds":kinds,"brands":[],"traditions":[],"notes":notes}
p="work/J7/shelves/00_03.json"; t=p+".tmp"
json.dump(out,open(t,"w"),ensure_ascii=False,indent=1); os.replace(t,p)
