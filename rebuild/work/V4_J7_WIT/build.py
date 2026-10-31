import json
U={'DOCG':'https://en.wikipedia.org/wiki/List_of_Italian_DOCG_wines','DOC':'https://en.wikipedia.org/wiki/List_of_Italian_DOC_wines','IGT':'https://en.wikipedia.org/wiki/List_of_Italian_IGT_wines'}
# (name, alias, desc-from-page, [versions])
DOCG={
'Piedmont':[
 ('Alta Langa','','sparkling, traditional method',[]),
 ('Asti','','white',[('Asti','the sparkling style'),('Moscato d\'Asti','the lightly sparkling style')]),
 ('Barbaresco','','red',[('Barbaresco Riserva','')]),
 ('Barbera d\'Asti','','red',[('Barbera d\'Asti Superiore',''),('Tinella','sub-zone'),('Colli Astiani','sub-zone')]),
 ('Nizza','','',[]),
 ('Barbera del Monferrato Superiore','','red',[]),
 ('Barolo','','red',[('Barolo Riserva',''),('Barolo Chinato','')]),
 ('Brachetto d\'Acqui','Acqui','red, still and sparkling',[]),
 ('Dogliani','Dolcetto di Dogliani Superiore','red',[]),
 ('Ovada','Dolcetto di Ovada Superiore','red',[]),
 ('Gattinara','','red',[('Gattinara Riserva','')]),
 ('Gavi','Cortese di Gavi','white; still, frizzante and spumante',[]),
 ('Ghemme','','red',[('Ghemme Riserva','')]),
 ('Roero','','white (Roero Arneis, also spumante) and red',[('Roero Arneis',''),('Roero Riserva','')]),
 ('Caluso','Erbaluce di Caluso','white',[]),
 ('Diano d\'Alba','Dolcetto di Diano d\'Alba','red',[]),
 ('Ruché di Castagnole Monferrato','','red',[])],
'Lombardy':[
 ('Franciacorta','','sparkling: spumante, rosé spumante and crémant',[]),
 ('Oltrepò Pavese Metodo Classico','','sparkling: rosé, crémant, Pinot Noir and Pinot Noir rosé',[]),
 ('Scanzo','Moscato di Scanzo','',[]),
 ('Sforzato di Valtellina','Sfurzat di Valtellina','red',[]),
 ('Valtellina Superiore','','red',[(x,'sub-zone') for x in ['Inferno','Grumello','Maroggia','Sassella','Valgella','Stagaflassi']]+[('Valtellina Superiore Riserva','')])],
'Veneto':[
 ('Amarone della Valpolicella','','',[]),
 ('Bagnoli Friularo','Friularo di Bagnoli','',[]),
 ('Bardolino Superiore','','red',[]),
 ('Colli di Conegliano','','',[]),
 ('Colli Euganei Fior d\'Arancio','Fior d\'Arancio Colli Euganei','',[]),
 ('Asolo Prosecco','','',[]),
 ('Conegliano Valdobbiadene Prosecco','','',[]),
 ('Lison','','',[]),
 ('Montello Rosso','','',[]),
 ('Piave Malanotte','Malanotte del Piave','',[]),
 ('Recioto di Soave','','white; normale, classico and spumante',[]),
 ('Soave Superiore','','white',[('Soave Superiore Classico',''),('Soave Superiore Riserva','')]),
 ('Recioto di Gambellara','','white',[]),
 ('Recioto della Valpolicella','','',[])],
'Friuli-Venezia Giulia':[
 ('Ramandolo','','white',[]),
 ('Colli Orientali del Friuli Picolit','','passito',[]),
 ('Rosazzo','','',[])],
'Emilia-Romagna':[
 ('Albana di Romagna','','white; dry, medium-sweet, sweet, passito and passito reserve',[]),
 ('Colli Bolognesi Pignoletto','','',[])],
'Tuscany':[
 ('Brunello di Montalcino','','red',[('Brunello di Montalcino Riserva','')]),
 ('Carmignano','','red',[('Carmignano Riserva','')]),
 ('Chianti','','red',[(x,'sub-zone') for x in ['Colli Aretini','Colli Senesi','Colli Fiorentini','Colline Pisane','Montalbano','Montespertoli','Rufina']]+[('Chianti Superiore',''),('Chianti Riserva','')]),
 ('Chianti Classico','','',[]),
 ('Elba Aleatico Passito','','passito',[]),
 ('Montecucco','','',[]),
 ('Morellino di Scansano','','red',[('Morellino di Scansano Riserva','')]),
 ('Suvereto','','',[]),
 ('Val di Cornia','','',[]),
 ('Vernaccia di San Gimignano','','white',[('Vernaccia di San Gimignano Riserva','')]),
 ('Vino Nobile di Montepulciano','','red',[('Vino Nobile di Montepulciano Riserva','')])],
'Abruzzo':[
 ('Colline Teramane Montepulciano d\'Abruzzo','','',[]),
 ('Terre Tollesi','','',[]),
 ('Terre di Casauria','','',[])],
'Lazio':[
 ('Cannellino di Frascati','','sweet dessert wine',[]),
 ('Cesanese del Piglio','Piglio','red, some sparkling',[]),
 ('Frascati Superiore','','',[])],
'Marche':[
 ('Castelli di Jesi Verdicchio Riserva','','',[]),
 ('Conero','','red, riserva only',[]),
 ('Offida','','',[]),
 ('Vernaccia di Serrapetrona','','red; dolce and secco',[]),
 ('Verdicchio di Matelica Riserva','','',[])],
'Umbria':[
 ('Sagrantino di Montefalco','','red; secco and passito',[]),
 ('Torgiano Rosso Riserva','','red, riserva only',[])],
'Basilicata':[('Aglianico del Vulture Superiore','','',[])],
'Campania':[
 ('Aglianico del Taburno','','',[]),
 ('Fiano di Avellino','','white',[]),
 ('Greco di Tufo','','white, also spumante',[]),
 ('Taurasi','','red',[('Taurasi Riserva','')])],
'Apulia':[
 ('Castel del Monte Bombino Nero','','',[]),
 ('Castel del Monte Nero di Troia Riserva','','',[]),
 ('Castel del Monte Rosso Riserva','','',[]),
 ('Primitivo di Manduria Dolce Naturale','','',[])],
'Sardinia':[('Vermentino di Gallura','','white',[('Vermentino di Gallura Superiore','')])],
'Sicily':[('Cerasuolo di Vittoria','','red',[('Cerasuolo di Vittoria Classico','')])],
}
DOC={
'Abruzzo':"Abruzzo|Cerasuolo d'Abruzzo|Controguerra|Montepulciano d'Abruzzo|Trebbiano d'Abruzzo|Villamagna",
'Basilicata':"Aglianico del Vulture|Matera|Terre dell'Alta Val d'Agri",
'Calabria':"Bivongi|Cirò|Donnici|Greco di Bianco|Lamezia|Melissa|Pollino|Sant'Anna di Isola Capo Rizzuto|San Vito di Luzzi|Savuto|Scavigna|Verbicaro",
'Campania':"Aversa Asprinio|Campi Flegrei|Capri|Castel San Lorenzo|Cilento|Costa d'Amalfi|Falerno del Massico|Falanghina del Sannio|Galluccio|Guardiolo|Irpinia|Ischia|Penisola Sorrentina|Sannio|Sant'Agata dei Goti|Solopaca|Taburno|Vesuvio",
'Emilia-Romagna':"Bosco Eliceo|Cagnina di Romagna|Colli Bolognesi|Colli Bolognesi Classico Pignoletto|Colli di Faenza|Colli di Imola|Colli di Parma|Colli di Rimini|Colli di Scandiano e di Canossa|Colli Piacentini|Colli Romagna Centrale|Gutturnio|Lambrusco di Sorbara|Lambrusco Grasparossa di Castelvetro|Lambrusco Salamino di Santa Croce|Modena|Ortrugo|Pagadebit di Romagna|Reggiano|Reno|Romagna Albana Spumante|Sangiovese di Romagna|Trebbiano di Romagna",
'Friuli-Venezia Giulia':"Carso|Colli Orientali del Friuli|Colli Orientali del Friuli Cialla|Colli Orientali del Friuli Rosazzo|Collio Goriziano|Friuli Annia|Friuli Aquileia|Friuli Grave|Friuli Isonzo|Friuli Latisana|Lison Pramaggiore",
'Lazio':"Aleatico di Gradoli|Aprilia|Atina|Bianco Capena|Castelli Romani|Cerveteri|Cesanese del Piglio|Cesanese di Affile|Cesanese di Olevano Romano|Circeo|Colli Albani|Colli della Sabina|Colli Etruschi Viterbesi|Colli Lanuvini|Cori|Est! Est!! Est!!! di Montefiascone|Frascati|Genazzano|Marino|Montecompatri Colonna|Nettuno|Roma|Tarquinia|Terracina|Velletri|Vignanello|Zagarolo",
'Liguria':"Cinque Terre|Cinque Terre Sciacchetrà|Colli di Luni|Colline di Levanto|Golfo del Tigullio|Riviera Ligure di Ponente|Rossese di Dolceacqua|Val Polcevera|Pornassio",
'Lombardy':"Botticino|Bonarda dell'Oltrepò Pavese|Buttafuoco dell'Oltrepò Pavese|Casteggio|Capriano del Colle|Cellatica|Garda|Garda Colli Mantovani|Lambrusco Mantovano|Lugana|Oltrepò Pavese|Riviera del Garda Bresciano|San Colombano al Lambro|San Martino della Battaglia|Terre di Franciacorta|Valcalepio|Valtellina Rosso|Valtenesi",
'Marche':"Bianchello del Metauro|Colli Maceratesi|Colli Pesaresi|Esino|Falerio dei Colli Ascolani|Lacrima di Morro d'Alba|Pergola|Rosso Conero|Rosso Piceno|Verdicchio dei Castelli di Jesi|Verdicchio di Matelica",
'Molise':"Biferno|Molise|Pentro di Isernia|Tintilia",
'Piedmont':"Albugnano|Barbera d'Alba|Barbera del Monferrato|Boca|Bramaterra|Calosso|Canavese|Carema|Cisterna d'Asti|Colli Tortonesi|Collina Torinese|Colline Novaresi|Colline Saluzzesi|Cortese dell'Alto Monferrato|Coste della Sesia|Dolcetto d'Acqui|Dolcetto d'Alba|Dolcetto d'Asti|Dolcetto delle Langhe Monregalesi|Dolcetto di Diano d'Alba|Dolcetto di Dogliani|Dolcetto di Ovada|Fara|Freisa d'Asti|Freisa di Chieri|Gabiano|Grignolino d'Asti|Grignolino del Monferrato Casalese|Langhe|Lessona|Loazzolo|Malvasia di Casorzo d'Asti|Malvasia di Castelnuovo Don Bosco|Monferrato|Nebbiolo d'Alba|Piemonte|Pinerolese|Rubino di Cantavenna|Sizzano|Valsusa|Verduno Pelaverga",
'Apulia':"Aleatico di Puglia|Alezio|Barletta|Brindisi|Cacc'e mmitte di Lucera|Castel del Monte|Colline Joniche Tarantine|Copertino|Galatina|Gioia del Colle|Gravina|Leverano|Lizzano|Locorotondo|Martina|Matino|Moscato di Trani|Nardò|Negroamaro di Terra d'Otranto|Orta Nova|Ostuni|Primitivo di Manduria|Rosso Barletta|Rosso Canosa|Rosso di Cerignola|Salice Salentino|San Severo|Squinzano|Tavoliere delle Puglie|Terra d'Otranto",
'Sardinia':"Alghero|Arborea|Campidano di Terralba|Cannonau di Sardegna|Carignano del Sulcis|Girò di Cagliari|Malvasia di Bosa|Malvasia di Cagliari|Mandrolisai|Monica di Cagliari|Monica di Sardegna|Moscato di Cagliari|Moscato di Sardegna|Moscato di Sorso Sennori|Nasco di Cagliari|Nuragus di Cagliari|Sardegna Semidano|Vermentino di Sardegna|Vernaccia di Oristano",
'Sicily':"Alcamo|Contea di Sclafani|Contessa Entellina|Delia Nivolelli|Eloro|Erice|Etna|Faro|Malvasia delle Lipari|Mamertino di Milazzo|Marsala|Menfi|Monreale|Noto|Moscato di Pantelleria|Moscato di Siracusa|Riesi|Salaparuta|Sambuca di Sicilia|Santa Margherita di Belice|Sciacca|Siracusa|Vittoria",
'Tuscany':"Ansonica Costa dell'Argentario|Barco Reale di Carmignano|Bianco della Valdinievole|Bianco dell'Empolese|Bianco di Pitigliano|Bianco Pisano di San Torpè|Bianco Vergine della Valdichiana|Bolgheri|Candia dei Colli Apuani|Capalbio|Colli dell'Etruria Centrale|Colline Lucchesi|Cortona|Elba|Maremma Toscana|Montecarlo|Monteregio di Massa Marittima|Montescudaio|Moscadello di Montalcino|Orcia|Parrina|Pomino|Rosso di Montalcino|Rosso di Montepulciano|San Gimignano|Sant'Antimo|Sovana|Val d'Arbia|Vin Santo del Chianti|Vin Santo del Chianti Classico|Vin Santo di Montepulciano",
'Trentino-Alto Adige':"Südtirol|Kalterersee|Valdadige|Santa Maddalena|Casteller|Teroldego Rotaliano|Trentino|Trento",
'Umbria':"Amelia|Assisi|Colli Altotiberini|Colli Amerini|Colli del Trasimeno|Colli Martani|Colli Perugini|Lago di Corbara|Montefalco|Orvieto|Rosso Orvietano|Spoleto|Todi|Torgiano",
'Aosta Valley':"Valle d'Aosta",
'Veneto':"Arcole|Bagnoli di Sopra|Bardolino|Bianco di Custoza|Breganze|Colli Berici|Colli di Conegliano|Colli Euganei|Corti Benedettine del Padovano|delle Venezie|Fiol Prosecco|Gambellara|Merlara|Montello e Colli Asolani|Monti Lessini|Piave|Prosecco|Riviera del Brenta|Soave|Valpolicella|Valpolicella Ripasso|Venezia|Vicenza|Vin Santo di Gambellara",
}
DOC={k:v.split('|') for k,v in DOC.items()}
# region alias notes
DOCNOTE={'Südtirol':'also called Alto Adige and Südtiroler','Kalterersee':'also called Lago di Caldaro, Caldaro and Kalterer','Valdadige':'zone straddling Trentino-Alto Adige and Veneto','delle Venezie':'zone covering Veneto, Friuli-Venezia Giulia and Trentino','Lison Pramaggiore':'zone straddling Veneto and Friuli-Venezia Giulia','Garda':'zone straddling Lombardy and Veneto','Lugana':'zone straddling Lombardy and Veneto','San Martino della Battaglia':'zone straddling Lombardy and Veneto','Orvieto':'zone straddling Umbria and Lazio','Colli di Luni':'zone straddling Liguria and Tuscany','Terre Tollesi':'also a DOCG','Modena':'','Lugana':'zone straddling Lombardy and Veneto'}
DOC['Abruzzo']=[x for x in DOC['Abruzzo']]  # Terre Tollesi is DOCG
IGT={
'Abruzzo':"Alto Tirino|Colli Aprutini|Colli del Sangro|Colline Frentane|Colline Pescaresi|Colline Teatine|del Vastese|Terre di Chieti|Valle Peligna",
'Apulia':"Daunia|Murgia|Puglia|Salento|Tarantino|Valle d'Itria",
'Basilicata':"Basilicata",
'Calabria':"Arghillà|Calabria|Condoleo|Costa Viola|Esaro|Lipuda|Locride|Palizzi|Pellaro|Scilla|Val di Neto|Valdamato|Valle del Crati",
'Campania':"Falanghina del Beneventano|Campania|Catalanesca del Monte Somma|Colli di Salerno|Dugenta|Epomeo|Paestum|Pompeiano|Roccamonfina|Terre del Volturno",
'Emilia-Romagna':"Bianco di Castelfranco Emilia|Emilia|Fortana del Taro|Forlì|Modena|Ravenna",
'Friuli-Venezia Giulia':"Venezia Giulia",
'Lazio':"Civitella d'Agliano|Colli Cimini|Frusinate|Lazio",
'Liguria':"Colline del Genovesato|Colline Savonesi|Golfo dei Poeti",
'Lombardy':"Alto Mincio|Benaco Bresciano|Bergamasca|Collina del Milanese|Montenetto di Brescia|Provincia di Mantova|Provincia di Pavia|Quistello|Ronchi di Brescia|Sabbioneta|Sebino|Terrazze Retiche di Sondrio|Valcamonica",
'Marche':"Marche",
'Molise':"Rotae|Osco",
'Sardinia':"Barbagia|Colli del Limbara|Isola dei Nuraghi|Marmilla|Nurra|Ogliastra|Parteolla|Planargia|Provincia di Nuoro|Romangia|Sibiola|Tharros|Trexenta|Valle del Tirso|Valli di Porto Pino",
'Sicily':"Camarro|Colli Ericini|Fontanarossa di Cerda|Salemi|Salina|Sicilia|Valle Belice",
'Tuscany':"Alta Valle della Greve|Colli della Toscana Centrale|Maremma Toscana|Toscano|Val di Magra",
'Trentino-Alto Adige':"Atesino|Mitterberg|Vallagarina|Vigneti delle Dolomiti",
'Umbria':"Allerona|Bettona|Cannara|Narni|Spello|Umbria",
'Veneto':"Alto Livenza|Colli Trevigiani|Conselvano|delle Venezie|Marca Trevigiana|Provincia di Verona|Veneto",
}
IGT={k:v.split('|') for k,v in IGT.items()}
IGTNOTE={'del Vastese':'also called Histonium','Osco':'also called Terre degli Osci','Frusinate':'also called del Frusinate','Toscano':'also called Toscana','Mitterberg':'also called Mitterberg zwischen Gfrill und Toll','Vigneti delle Dolomiti':'also called Weinberg Dolomiten','Atesino':'Atesino delle Venezie','Alto Livenza':'zone straddling Veneto and Friuli-Venezia Giulia','delle Venezie':'zone covering Veneto, Friuli-Venezia Giulia and Trentino','Vallagarina':'zone straddling Trentino-Alto Adige and Veneto','Golfo dei Poeti':'also called Golfo dei Poeti La Spezia','Modena':'also called Provincia di Modena'}
BAROLO={'Barolo':['Bricco Viole','Brunate','Cannubi','Cannubi Boschis','Rue','San Lorenzo','Sarmassa','Via Nuova'],'Castiglione Falletto':['Bricco Rocche','Fiasc','Mariondino','Monprivato','Parussi','Pira','Rivera','Villero'],'La Morra':['Arborina','Brunate','Cerequio','Gattera','Giachini','Marcenasco','Rocche dell\'Annunziata'],'Monforte d\'Alba':['Bussia','Cicala','Colonnello','Dardi','Ginestra','Mosconi','Munie','Romirasco','Santo Stefano'],'Serralunga d\'Alba':['Falletto','Francia','La Serra','Marenca','Marenca-Rivette','Margheria','Ornato','Parafada','Vigna Rionda']}
order=['Piedmont','Aosta Valley','Lombardy','Trentino-Alto Adige','Veneto','Friuli-Venezia Giulia','Liguria','Emilia-Romagna','Tuscany','Umbria','Marche','Lazio','Abruzzo','Molise','Campania','Apulia','Basilicata','Calabria','Sicily','Sardinia']
AREA={'Piedmont':'North-west','Aosta Valley':'North-west','Lombardy':'North-west','Liguria':'North-west','Trentino-Alto Adige':'North-east','Veneto':'North-east','Friuli-Venezia Giulia':'North-east','Emilia-Romagna':'North-east'}
TT={'DOCG':[["Colour and style",["Red","White","Rosé","Sparkling","Sweet or passito"]],["Quality step",["Normale","Superiore","Riserva","Classico"]]],
    'DOC':[["Colour and style",["Red","White","Rosé","Sparkling","Sweet or passito"]],["Quality step",["Normale","Superiore","Riserva","Classico"]]],
    'IGT':[["Colour and style",["Red","White","Rosé","Sparkling","Sweet"]]]}
TIERD={'DOCG':'Denominazione di Origine Controllata e Garantita, the top tier of Italian wine appellations',
 'DOC':'Denominazione di Origine Controllata, the middle tier of Italian wine appellations',
 'IGT':'Indicazione Geografica Tipica, the geographical-indication tier of Italian wine'}
docg_names={e[0].lower() for v in DOCG.values() for e in v}|{e[1].lower() for v in DOCG.values() for e in v if e[1]}
def ent(n,a,d,v,tier,reg,g=None):
    e={'n':n,'a':a,'d':d,'mk':'','y':'','s':U[tier],'v':[{'n':x[0],'mk':'','y':'','d':x[1]} for x in v]}
    return e
shelves=[];kinds_all=[]
for r in order:
    ks=[]
    # DOCG
    if r in DOCG:
        xs=[]
        for n,a,d,v in DOCG[r]:
            dd=f"DOCG appellation of {r}"+(f": {d}." if d else ".")
            e=ent(n,a,dd,v,'DOCG',r)
            if d: e['dt']=d
            xs.append(e)
        xs.sort(key=lambda e:e['n'])
        ks.append({'n':f"{r}: DOCG appellations",'d':f"{TIERD['DOCG']}, in {r}.",'nl':f"One entry is a DOCG wine appellation of {r}; its normale, riserva, superiore and sub-zone forms are versions.",'sel':f"Every {r} appellation in Wikipedia's List of Italian DOCG wines, which gives 77 DOCG appellations nationally; appellations also in the DOC list appear once, under DOCG.",'xg':'alphabetical','tt':TT['DOCG'],'x':xs,'s':U['DOCG']})
    xs=[]
    for n in DOC.get(r,[]):
        if n.lower() in docg_names: continue
        note=DOCNOTE.get(n,'')
        d=f"DOC appellation of {r}"+(f"; {note}." if note else ".")
        e=ent(n,'',d,[],'DOC',r)
        if r=='Piedmont' and False: pass
        xs.append(e)
    if r=='Piedmont':
        for e in xs:
            pass
    if xs:
        xs.sort(key=lambda e:e['n'])
        ks.append({'n':f"{r}: DOC appellations",'d':f"{TIERD['DOC']}, in {r}.",'nl':f"One entry is a DOC wine appellation of {r}; riserva, superiore and classico forms are versions.",'sel':f"Every {r} appellation in Wikipedia's List of Italian DOC wines (a partial copy of the official register); appellations that are DOCG appear under DOCG.",'xg':'alphabetical','tt':TT['DOC'],'x':xs,'s':U['DOC']})
    xs=[]
    for n in IGT.get(r,[]):
        note=IGTNOTE.get(n,'')
        d=f"IGT appellation of {r}"+(f"; {note}." if note else ".")
        xs.append(ent(n,'',d,[],'IGT',r))
    if xs:
        xs.sort(key=lambda e:e['n'])
        ks.append({'n':f"{r}: IGT appellations",'d':f"{TIERD['IGT']}, in {r}.",'nl':f"One entry is an IGT wine indication of {r}.",'sel':f"Every {r} indication in Wikipedia's List of Italian IGT wines.",'xg':'alphabetical','tt':TT['IGT'],'x':xs,'s':U['IGT']})
    shelves.append({'n':r,'t':f"Italian wine appellations of {r}, by tier: DOCG, DOC and IGT.",'k':ks})
# Barolo versions: unofficial crus
for s in shelves:
    for k in s['k']:
        for e in k['x']:
            if e['n']=='Barolo':
                e['v']+= [{'n':f"{c} ({com})",'mk':'','y':'','d':'traditional cru named by the Wikipedia Barolo page; not an official classification'} for com,cs in BAROLO.items() for c in cs]
                e['dt']='red · normale · riserva · commune and vineyard'
dept={'n':'Wine of Italy','mode':'tier','t':'Italian wine sold by its protected place name: DOCG, DOC and IGT appellations grouped by region; a wine of another country → its own department.',
 'ax':'Which region does the wine come from, and how strictly protected is its name: DOCG, DOC or IGT?',
 'note':'Organised region → tier → appellation; producers are not entries.',
 's':shelves,
 'ms':[{'mkt':'Italy wine production','who':'Italy','share':'19.3 % of world output (49.8 million hl)','yr':2022,'s':'https://en.wikipedia.org/wiki/Italian_wine','note':'volume, as the page states'}],
 'msum':'Italy produced 49.8 million hl of wine in 2022, over 19.3 % of world output, and was the largest wine exporter in 2024.'}
json.dump({'depts':[dept],'brands':[],'renames':RENAMES if False else {},'moves':[]},open('/tmp/x','w'))
nk=sum(len(s['k']) for s in shelves);ne=sum(len(k['x']) for s in shelves for k in s['k'])
print(nk,ne)
RENAMES={
'Sangiovese':'Tuscany: DOCG appellations','Nebbiolo':'Piedmont: DOCG appellations','Dolcetto':'Piedmont: DOC appellations','Barbera':'Piedmont: DOC appellations',
'Lagrein':'Trentino-Alto Adige: DOC appellations','Refosco':'Friuli-Venezia Giulia: DOC appellations','Sagrantino':'Umbria: DOCG appellations','Montepulciano':'Marche: DOCG appellations',
'Aglianico':'Campania: DOCG appellations',"Nero d'Avola":'Sicily: DOC appellations','Nerello Mascalese':'Sicily: DOC appellations','Arneis':'Piedmont: DOCG appellations','Cortese':'Piedmont: DOCG appellations',
'Garganega':'Veneto: DOC appellations','Friulano':'Friuli-Venezia Giulia: DOC appellations','Vermentino':'Sardinia: DOC appellations','Verdicchio':'Marche: DOC appellations','Trebbiano':'Abruzzo: DOC appellations',
'Pecorino':'Marche: DOCG appellations','Greco':'Campania: DOCG appellations','Fiano':'Campania: DOCG appellations','Falanghina':'Campania: DOC appellations','Carricante':'Sicily: DOC appellations','Malvasia':'Sicily: DOC appellations'}
json.dump({'depts':[dept],'brands':[],'renames':RENAMES,'moves':[]},open('/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WIT.json.tmp','w'),ensure_ascii=False,indent=1)
