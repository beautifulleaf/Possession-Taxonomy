import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,y,s,v=(),dt='',a='',mk=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(('n','mk','y','d'),t)) for t in v],"dt":dt}
kinds=[
 {"n":"Verdejo","a":"","d":"Still white wine made mainly from the Verdejo grape, Rueda's signature variety.","t":["young and fresh","barrel-fermented","oxidative (historic)"],"s":W+"Verdejo",
  "x":[X("Rueda","DO in Castilla y León; 'Rueda Verdejo' needs at least 85% Verdejo.","1980",W+"Rueda_(DO)",
     [("Rueda (white)","","","at least half Verdejo or Sauvignon Blanc"),("Rueda Verdejo","","","at least 85% Verdejo, often 100%"),("Vino de Pueblo","","","village-labelled tier"),("Gran Vino de Rueda","","","old vines, low yields; top tier"),("Fresh-style Rueda","Marqués de Riscal","1972","investment that began modern quality production")],
     "tier: Rueda · Vino de Pueblo · Gran Vino de Rueda · steel or oak",a="Rueda DO")]},
 {"n":"Godello","a":"Gouveio · Verdello","d":"White wine made mainly from the Godello grape of north-west Spain.","s":W+"Godello",
  "x":[X("Valdeorras","Galician DO where Godello, reintroduced in the 1970s, gives its best results.","1945",W+"Valdeorras_(DO)",dt="steel or oak · single vineyard"),
       X("Monterrei","Galician DO with Godello, Treixadura and Doña Blanca as recommended whites.","1994","https://en.wikipedia.org/wiki/Monterrei_(DO)")]},
 {"n":"Vermentino","a":"Rolle · Pigato · Favorita · Vermentinu","d":"White wine made mainly from the Vermentino grape of Sardinia, Liguria and Corsica.","s":W+"Vermentino",
  "x":[X("Vermentino di Gallura","Sardinia's only DOCG, from Gallura in the north; the best-known Vermentino.","",W+"Sardinian_wine",dt="Superiore · still or sparkling"),
       X("Vermentino di Sardegna","DOC covering the whole island of Sardinia.","",W+"Sardinian_wine"),
       X("Colli di Luni Vermentino","DOC Vermentino from Liguria and neighbouring Tuscany.","",W+"Vermentino"),
       X("Patrimonio blanc","Northern Corsican AOC white made from 100% Vermentino.","1968",W+"Vermentino",a="Vermentinu")]},
 {"n":"Garganega","a":"Grecanico","d":"White wine made mainly from the Garganega grape of the Veneto.","t":["dry","recioto (sweet, dried grapes)"],"s":W+"Garganega",
  "x":[X("Soave","Veneto DOC of at least 70% Garganega, with up to 30% Trebbiano di Soave.","1968","https://en.wikipedia.org/wiki/Soave_(wine)",
     [("Soave Classico","","1927","hillside zone around Soave and Monteforte d'Alpone"),("Soave Superiore DOCG","","2001","lower yields, 11.5% minimum"),("Recioto di Soave DOCG","","1998","sweet passito style, 14% minimum")],
     "zone: Soave · Classico · Superiore · dry or recioto"),
       X("Gambellara","Veneto zone next to Soave where Garganega is the main grape.","",W+"Gambellara",[("Gambellara Classico","","","DOC dry white"),("Recioto di Gambellara DOCG","","2009","sweet; upgraded from DOC")]),
       X("Bianco di Custoza","Veneto DOC blend in which Garganega is widely grown.","",W+"Garganega")]},
 {"n":"Fiano","a":"Apiano · Minutolo","d":"White wine made mainly from the Fiano grape of Campania.","s":"https://en.wikipedia.org/wiki/Fiano_(grape)",
  "x":[X("Fiano di Avellino","Campanian DOCG of at least 85% Fiano; may be labelled Apianum.","2003",W+"Fiano_di_Avellino",[("Fiano di Avellino","Mastroberardino","","producer that led the variety's revival")],"85–100% Fiano · Greco, Coda di Volpe or Trebbiano for the rest",a="Apianum")]},
 {"n":"Verdicchio","a":"Trebbiano di Lugana · Turbiana","d":"White wine made mainly from the Verdicchio grape of the Marche.","t":["still","sparkling","passito"],"s":W+"Verdicchio",
  "x":[X("Verdicchio dei Castelli di Jesi","Marche DOC of at least 85% Verdicchio, classically sold in the amphora-shaped Anfora bottle.","",W+"Verdicchio",dt="still, sparkling or passito · Anfora bottle"),
       X("Verdicchio di Matelica","Inland Marche DOC of at least 85% Verdicchio with tighter yield limits.","",W+"Verdicchio_dei_Castelli_di_Jesi",dt="still, spumante or passito")]},
 {"n":"Trebbiano","a":"Ugni blanc","d":"White wine made mainly from Trebbiano grapes, Italy's most widely named white variety.","s":W+"Trebbiano",
  "x":[X("Trebbiano d'Abruzzo","Abruzzo DOC white, thought to be from Bombino bianco rather than Trebbiano Toscano.","1972",W+"Trebbiano_d%27Abruzzo",
     [("Trebbiano d'Abruzzo","Edoardo Valentini","","called possibly Italy's greatest dry white"),("Trebbiano d'Abruzzo","Emidio Pepe","","foot-crushed, aged in glass")]),
       X("Orvieto","Umbrian DOC white of Trebbiano Toscano with Grechetto and Verdello.","",W+"Orvieto_DOC",[("Orvieto Classico","","","historic core zone"),("Orvieto Abboccato","","","semi-sweet; small production")],"secco · abboccato · dolce"),
       X("Trebbiano di Romagna","One of the seven DOCs named after Trebbiano.","",W+"Trebbiano")]},
 {"n":"Friulano","a":"Tocai Friulano · Sauvignonasse · Sauvignon Vert","d":"White wine made mainly from the Friulano grape of Friuli and western Slovenia.","s":W+"Sauvignonasse",
  "x":[X("Collio Friulano","Friulano from the Collio Goriziano DOC, a mostly white hill zone on the Slovenian border.","",W+"Collio_Goriziano",dt="labelled Tocai Friulano until 2007"),
       X("Friuli Colli Orientali Friulano","Friulano from the Colli Orientali del Friuli DOC, one of its four main zones.","",W+"Sauvignonasse"),
       X("Friuli Isonzo Friulano","Friulano from the Friuli Isonzo DOC.","",W+"Sauvignonasse")]},
 {"n":"Falanghina","a":"Falanghina Greco · Uva Falerna","d":"White wine made mainly from the Falanghina grape of Campania.","t":["still","sparkling","late-harvest","passito"],"s":W+"Falanghina",
  "x":[X("Falanghina del Sannio","Campanian DOC of at least 85% Falanghina.","2011","https://italianwinecentral.com/denomination/falanghina-del-sannio-doc/",
     [("Guardia Sanframondi (Guardiolo)","","","subzone"),("Sant'Agata dei Goti","","","subzone"),("Solopaca","","","subzone"),("Taburno","","","subzone")],"bianco · spumante · metodo classico · vendemmia tardiva · passito")]},
 {"n":"Pecorino","a":"","d":"White wine made mainly from the Pecorino grape of the Marche and Abruzzo.","s":"https://en.wikipedia.org/wiki/Pecorino_(grape)",
  "x":[X("Offida Pecorino","Marche DOCG varietal white of at least 85% Pecorino and 12% alcohol.","",W+"Offida",[("Offida Pecorino","Cocci Grifoni","1980s","first producer to use the grape widely")])],
  "m":[["Pecorino","Cataldi Madonna"]]},
 {"n":"Loureiro","a":"Loureira","d":"White wine made mainly from the aromatic Loureiro grape of Minho and Galicia.","s":"https://en.wikipedia.org/wiki/Loureiro_(grape)",
  "x":[X("Vinho Verde Loureiro","Varietal Loureiro from the Vinho Verde DOC, notably the Lima subregion.","1984",W+"Vinho_Verde",[("Lima","","","subregion along the Lima river")],"light, fresh, often lightly spritzy")]},
 {"n":"Albillo Mayor","a":"","d":"White wine made mainly from the Albillo Mayor grape of Castilla y León.","s":W+"Albillo",
  "x":[X("Ribera del Duero blanco","White from the Ribera del Duero DO, where Albillo is the only authorised white grape.","1982","https://en.wikipedia.org/wiki/Ribera_del_Duero_(DO)")]},
]
brands=[
 {"n":"Marqués de Riscal","c":"Spain","f":"1858","seg":"Wine producer","d":"Rioja winery whose 1972 investment in Rueda began modern fresh Verdejo.","lines":[],"eras":[],"sig":["Rueda"],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"Mastroberardino","c":"Italy","seg":"Wine producer","d":"Campanian producer that led the revival of Fiano around Avellino.","lines":[],"eras":[],"sig":["Fiano di Avellino"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Fiano_di_Avellino"},
 {"n":"Edoardo Valentini","c":"Italy","seg":"Wine producer","d":"Abruzzo estate in Pescara province famed for its Trebbiano d'Abruzzo.","lines":[],"eras":[],"sig":["Trebbiano d'Abruzzo"],"sc":[],"rel":["Emidio Pepe"],"s":"https://en.wikipedia.org/wiki/Trebbiano_d%27Abruzzo"},
 {"n":"Emidio Pepe","c":"Italy","seg":"Wine producer","d":"Teramo estate and early artisanal pioneer that foot-crushes organic grapes.","lines":[],"eras":[],"sig":["Trebbiano d'Abruzzo"],"sc":[],"rel":["Edoardo Valentini"],"s":"https://en.wikipedia.org/wiki/Trebbiano_d%27Abruzzo"},
 {"n":"Cocci Grifoni","c":"Italy","seg":"Wine producer","d":"Offida producer whose founder Guido Cocci Grifoni first used Pecorino widely in the 1980s.","lines":[],"eras":[],"sig":["Offida Pecorino"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Pecorino_(grape)"},
 {"n":"Cataldi Madonna","c":"Italy","seg":"Wine producer","d":"Abruzzo producer; Luigi Cataldi Madonna first put Pecorino on a label in 1997.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Pecorino_(grape)"},
]
notes=("Archetypes are DOC/DOCG/DO/AOC appellations, all maker-free (mk empty); producer-specific bottlings appear only as versions or m where a retrieved page names them. "
 "Dropped the old single-SKU retailer models (Bodega Diez Siglos 1985, Montepedroso Enoteca, Villa de Randis/Muzic, Passo alle Tremiti/Tenimenti Grieco, Aimè/Cascina del Colle, Eminência/Quinta da Pedra, Bodegas Virtus Gran Reserva) per the brief; replaced retailer kind sources with grape pages. "
 "Left out: Verdicchio Riserva DOCGs and Lugana (no retrieved page confirmed them), appellation years not stated on retrieved pages, Rías Baixas for Loureiro, Bierzo for Godello. "
 "Albillo Mayor: Wikipedia's Albillo page treats Albillo Real as 'Albillo' and lists Albillo Mayor separately; the Ribera del Duero page says 'Albillo' is the DO's only white — flagged for checking. No traditions added (not an artisan-craft shelf).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/J7/shelves/01_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
