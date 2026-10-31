import json, os
W='https://en.wikipedia.org/wiki/'
def A(n,d,s,mk="",y="",a="",v=None,dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or []}
    if dt: x["dt"]=dt
    return x
def V(n,mk="",y="",d=""):
    o={"n":n}
    if mk:o["mk"]=mk
    if y:o["y"]=y
    if d:o["d"]=d
    return o
GRU=W+'Gruy%C3%A8re_cheese'; COM=W+'Comt%C3%A9_cheese'; EMM=W+'Emmental_cheese'; BERG=W+'Bergk%C3%A4se'
kinds=[
{"n":"Gruyère","a":"Greyerzer · groviera · gravyer",
 "d":"Hard Alpine cooked-pressed cow's-milk cheese from western Switzerland, nutty and sweet-salty, with few or no holes.",
 "t":["doux (mild, 6 months+)","réserve / surchoix (10 months+)","mi-salé, salé, vieux","cave-aged (Höhlengereift)","alpage (summer)","organic"],
 "s":"https://www.cheese.com/le-gruyere-aop/",
 "x":[
  A("Le Gruyère AOP","Swiss raw-milk Gruyère from Fribourg, Vaud, Neuchâtel, Jura and Bern, AOC 2001 and AOP 2013.",GRU,y="AOC 2001",a="Le Gruyère Switzerland AOP",
    v=[V("Le Gruyère AOP d'Alpage",d="Made only in summer on Swiss Alpine pastures."),
       V("Le Gruyère AOP Réserve",d="Aged at least 10 months."),
       V("Kaltbach Le Gruyère AOP","Emmi",d="Cave-aged (Höhlengereift) in the Kaltbach cave (old data)."),
       V("Gruyère AOP Vorderfultigen Spezial 18 months","Bergkäserei Vorderfultigen"),
       V("Le Gruyère AOP (Fromagerie de Develier Bio)","Fromagerie de Develier",d="Organic."),
       V("Le Gruyère AOP (Käserei Juchlishaus)","Käserei Juchlishaus"),
       V("Le Gruyère AOP (Käserei Mamishaus)","Käserei Mamishaus"),
       V("Gruyère AOP (14 months)","Elsa Group"),V("Gruyère AOP (18 months)","Elsa Group")],
    dt="raw cow's milk · doux 6 months+, réserve 10 months+, older profiles to 14 months+ · village dairy, alpage or cave-aged"),
  A("French Gruyère PGI","EU-protected French Gruyère from a wider area than the Swiss AOP, with holes from pea- to cherry-sized.",GRU,a="Gruyère IGP",dt="must state French origin · holes pea- to cherry-sized"),
  A("Kars gravyer","Turkish Gruyère-type cheese from Kars, made in copper cauldrons from high-pasture cow's milk and aged about 6–9 months; Turkish GI 2024.",
    "https://www.ntv.com.tr/turkiye/gravyer-peyniri-cografi-isaretle-tescillendi,vagsE4ae8U2nurz4zz448Q",y="GI 2024",a="Kars gravyeri · Kars gravyer peyniri",
    v=[V("Bernis Kars Gravyer Peyniri","Bernis"),V("Boğatepe Gravyer",d="Boğatepe village, Kars (old data).")],dt="cow's milk · 6–9 months"),
  A("Generic gruyere","Gruyère-style cheese made outside Europe; a US court ruled \"gruyere\" generic in 2021, upheld 2023.",GRU,y="2021 ruling",
    v=[V("Darima Gruyère","Darima Farms"),V("Quatá Queijo Gruyère","Quatá",d="Brazil."),V("Vigor Gruyère","Vigor",d="Brazil.")])]},
{"n":"Comté","a":"Gruyère de Comté",
 "d":"Hard cooked-pressed raw cow's-milk cheese of the French Jura in large wheels, made by village fruitières and aged by affineurs.",
 "t":["Comté Extra (green band)","Comté (brown band)","young (4–8 months)","mature (12–18 months)","long-aged (24 months+)","organic"],
 "s":COM,
 "x":[
  A("Comté AOP","France's largest PDO cheese, from Montbéliarde or French Simmental milk, made by about 150 co-operative fruitières; AOC 1958, PDO 1996.",COM,y="AOC 1958",a="Comté AOC · Comté PDO",
    v=[V("Comté Extra",d="Scores above 14/20 at grading; green casein band with bell logo."),
       V("Comté",d="Scores 12–14/20; brown band."),
       V("Marcel Petite Comté Elegance","Marcel Petite",d="Aged about 10 months at Fort Saint-Antoine."),
       V("Marcel Petite Comté Symphonie","Marcel Petite",d="Aged 16–24 months at Fort Saint-Antoine.")],
    dt="wheel 40–70 cm, up to 55 kg · raw milk · 4 months minimum, commonly to 36 months · fruitière and affineur · summer or winter milk")],
 "m":[["Templegall","Hegarty Cheese"],["L'Estival","Ici en Chartreuse"]]},
{"n":"Emmental","a":"Emmentaler · Swiss cheese",
 "d":"Medium-hard Alpine cooked-pressed cow's-milk cheese in very large wheels with big round holes, from the Emme valley.",
 "t":["classic (4 months+)","surchoix","Premier Cru (14 months+)","cave-aged","foil-ripened block"],
 "s":"https://kerrygold.com/products/",
 "x":[
  A("Emmentaler AOP","Swiss raw-milk Emmental from village dairies (42 in 2024), AOC 2000 and AOP 2013, ripened at least four months.",EMM,y="AOC 2000",a="Emmentaler Switzerland AOP",
    v=[V("Emmentaler Switzerland Premier Cru",d="Ripened at least 14 months in a humid cellar."),
       V("Emmentaler Surchoix",d="At least 4 months, grainier texture."),
       V("Kaltbach Emmentaler AOP","Kaltbach",d="Cave-aged (old data)."),
       V("Emmentaler AOP (Käserei Guntershausen)","Käserei Guntershausen"),
       V("Emmentaler AOP (Käserei Hüpfenboden)","Käserei Hüpfenboden"),
       V("Emmentaler AOP (Käserei Waldegg)","Käserei Waldegg")],
    dt="very large wheels · raw milk without silage · 4 months minimum · holes from hay-dust nuclei"),
  A("Allgäuer Emmentaler PDO","Bavarian raw-milk Emmental from the Allgäu, ripened at least three months and milder than the Swiss.","https://de.wikipedia.org/wiki/Allgäuer_Emmentaler",a="Allgäuer Emmentaler",
    v=[V("Allgäuer Emmentaler","Allgäuland-Käsereien")],dt="raw milk · 3 months minimum"),
  A("Emmental de Savoie PGI","French protected Emmental from Savoie.",EMM),
  A("Emmental français est-central PGI","French protected Emmental from Franche-Comté and east-central France.",EMM)],
 "m":[["Vigor Emmental","Vigor"]]},
{"n":"Beaufort & Abondance","a":"Beaufort · Abondance",
 "d":"Savoie Alpine raw cow's-milk cheeses of the gruyère family, from Tarine and Abondance cattle, in concave-heeled wheels.",
 "t":["summer (été)","alpage / chalet","winter (hiver)"],
 "s":W+"Beaufort_cheese",
 "x":[
  A("Beaufort PDO","Firm raw-milk gruyère-family cheese from Beaufortain, Tarentaise and Maurienne, in wheels with a concave heel; AOC 1968.",W+"Beaufort_cheese",y="AOC 1968",
    v=[V("Beaufort chalet d'alpage",d="Made in Alpine chalets on high pastures."),V("Beaufort d'été",d="Summer milk."),V("Beaufort d'hiver",d="Winter milk.")],
    dt="wheel 35–75 cm, 20–70 kg, concave heel 11–16 cm · beechwood hoops · Tarine or Abondance cows · aged 6–12 months or more"),
  A("Abondance PDO","Semi-hard fragrant raw-milk cheese of Haute-Savoie, named after the commune of Abondance; AOC 1990.",W+"Abondance_cheese",y="AOC 1990",
    dt="about 10 kg · Abondance, Montbéliarde and Tarine cows (Abondance 55%+) · 3 months minimum on spruce boards")]},
{"n":"Appenzeller","a":"Appenzeller Käse",
 "d":"Hard Swiss washed-rind cow's-milk cheese from Appenzellerland, rubbed during curing with a secret herbal brine.",
 "t":["Classic (silver, 3–4 months)","Surchoix (gold, 4–6 months)","Extra (black, 6 months+)","Purple Label"],
 "s":W+"Appenzeller_cheese",
 "x":[
  A("Appenzeller","Straw-coloured, small-eyed cheese made by about 75 dairies, each with its own herbal brine; first mentioned 1282.",W+"Appenzeller_cheese",mk="Appenzeller Käse GmbH",y="1282",
    v=[V("Appenzeller Classic","Appenzeller Käse GmbH",d="3–4 months, mild, silver label."),
       V("Appenzeller Surchoix","Appenzeller Käse GmbH",d="4–6 months, sharp, gold label."),
       V("Appenzeller Extra","Appenzeller Käse GmbH",d="6 months or more, extra sharp, black label."),
       V("Appenzeller Purple Label","Appenzeller Käse GmbH")],
    dt="label colour by age · herbal brine, sometimes with wine or cider · golden rind")]},
{"n":"Bergkäse & Alpkäse","a":"mountain cheese · alpine cheese · Almkäse · Hobelkäse",
 "d":"Hard or semi-hard Alpine cow's-milk cheeses made in mountain dairies (Bergkäse) or on summer pastures (Alpkäse), with few holes.",
 "t":["Alp (summer pasture) or village dairy","extra-hard planing cheese (Hobelkäse)","raw milk, no silage"],
 "s":W+"Alpk%C3%A4se",
 "x":[
  A("Berner Alpkäse & Hobelkäse AOP","Full-fat raw-milk Alpine cheese of the Bernese Oberland, made by hand over wood fire; Hobelkäse is aged two years or more.",W+"Berner_Alpk%C3%A4se",y="first mentioned 1548",a="Berner Alpkäse · Berner Hobelkäse",
    v=[V("Berner Hobelkäse AOP",d="Extra-hard, aged at least two years.")],dt="summer Alp season only · wood fire · no holes"),
  A("L'Etivaz AOP","Raw-milk summer Alp cheese from the Vaud Alps, made in copper cauldrons over open wood fires; first Swiss non-wine AOC, 2000.","https://en.wikipedia.org/wiki/L%27Etivaz",y="AOC 2000",
    dt="20–50 kg, 40–65 cm · summer only · aged 5–13 months"),
  A("Allgäuer Bergkäse PDO","Raw-milk mountain cheese of the Allgäu, smaller and flatter than Emmental, ripened at least four months; PDO 1997.","https://de.wikipedia.org/wiki/Allgäuer_Bergkäse",y="PDO 1997",
    dt="15–50 kg · raw milk · 4 months minimum",v=[V("Baldauf 1862 Meisterstück Alpkäse","Baldauf Käse")]),
  A("Vorarlberger Bergkäse PDO","Hand-made mountain cheese of Vorarlberg, Austria, from silage-free grassland milk processed daily.",W+"Vorarlberger_Bergk%C3%A4se"),
  A("Vorarlberger Alpkäse PDO","Austrian Alp cheese of Vorarlberg under EU designation of origin.",BERG),
  A("Tiroler Bergkäse PDO","Tyrolean mountain cheese under EU designation of origin.",BERG),
  A("Tiroler Alpkäse PDO","Tyrolean summer Alp cheese under EU designation of origin.",BERG,a="Tiroler Almkäse"),
  A("Bündner Bergkäse","Grisons mountain cheese made only in village dairies above 1,000 m, protected under Swiss mountain rules.",BERG)],
 "m":[["Gantrisch Bergkäse","Bergkäserei Vorderfultigen"],["Kärntnermilch Mölltaler Almkäse Selektion 50% FiT","Kärntnermilch"],["Glarner Alpkäse AOP",""],["Formaggio d'alpe ticinese AOP",""],["Gailtaler Almkäse PDO",""],["Formai de Mut dell'Alta Valle Brembana PDO",""]]},
{"n":"Raclette","a":"raclette cheese · Walliser Raclette",
 "d":"Semi-hard cow's-milk cheese with a washed or smear rind, made to melt and be scraped for the raclette dish.",
 "t":["raw or pasteurised milk","wheel, half-wheel or slices","smoked, pepper, garlic"],
 "s":W+"Raclette",
 "x":[
  A("Raclette du Valais AOP","Valais raw-milk raclette cheese in wheels of about 6 kg, aged 3–6 months; AOC 2003, AOP 2013.",W+"Raclette_du_Valais",y="AOC 2003",a="Walliser Raclette AOP",dt="about 6 kg · 3–6 months"),
  A("Raclette de Savoie PGI","Savoie raw-milk raclette cheese from Abondance, Montbéliarde or Tarentaise cows, aged 4–5 months; PGI 2017.","https://fr.wikipedia.org/wiki/Raclette_de_Savoie",y="PGI 2017",dt="raw milk · 4–5 months")],
 "m":[["Takara no Tokeru","Cheese Kobo Takara"],["Leelanau Raclette","Leelanau Cheese Company"],["十勝ラクレット GI",""]]},
{"n":"Fontina","a":"fontine · fontal · fontella",
 "d":"Semi-soft to hard washed-rind cow's-milk cheese of the Aosta Valley, earthy and melting; milder copies made widely.",
 "t":["young (fondue)","mature"],
 "s":"https://Cheese.com/stella-fontina/",
 "x":[
  A("Fontina Valle d'Aosta PDO","Aosta Valley fontina from raw milk of a single milking, made since the 12th century; PDO 1996.",W+"Fontina",y="PDO 1996",a="Fontina DOP",
    dt="about 45% fat · tan to orange-brown natural rind · earthy, mushroomy"),
  A("Danish, Swedish and US fontina","Milder, softer fontina with more holes made outside Italy; \"fontina\" ruled generic in the US in 1986.",W+"Fontina")]},
{"n":"Vacherin fribourgeois","a":"Vacherin Fribourgeois AOP",
 "d":"Semi-hard Swiss cheese of Fribourg from thermised cow's milk, slightly acidic and resiny, used in fondue.",
 "t":["Classic","Extra","Rustic","Alpage","Mountain","organic"],
 "s":W+"Vacherin_Fribourgeois",
 "x":[
  A("Vacherin Fribourgeois AOP","Fribourg cheese under Swiss AOP in six varieties by age and origin.",W+"Vacherin_Fribourgeois",
    v=[V("Classic",d="6–12 weeks."),V("Extra",d="12 weeks minimum."),V("Rustic",d="12–25 weeks."),V("Alpage",d="12–25 weeks."),V("Mountain",d="9–25 weeks."),V("Bio",d="Organic, 9 weeks minimum.")],
    dt="thermised milk · 6–25 weeks")]},
{"n":"Tête de Moine","a":"Fromage de Bellelay · monk's head",
 "d":"Small tall Swiss Jura cheese pared into rosettes with a girolle rather than cut.",
 "t":["whole wheel","pre-pared rosettes"],
 "s":W+"T%C3%AAte_de_Moine",
 "x":[
  A("Tête de Moine AOP","Cheese first made by the canons of Bellelay Abbey, now by fewer than ten Jura dairies; AOC 2001, matured 75 days+ on spruce.",W+"T%C3%AAte_de_Moine",y="AOC 2001",a="Tête de Moine, Fromage de Bellelay",
    dt="10–15 cm across, about 850 g (up to 2.5 kg) · 75 days minimum on spruce boards · served as rosettes shaved with a girolle (invented 1982 by Nicolas Crevoisier)")]},
{"n":"Morbier","a":"Morbier AOP",
 "d":"Semi-soft cow's-milk cheese of Franche-Comté with a thin black ash line through the middle and a sticky rind.",
 "t":["raw milk","pasteurised"],
 "s":W+"Morbier_cheese",
 "x":[
  A("Morbier PDO","Jura and Doubs cheese whose ash layer recalls evening curd protected overnight under ash by Comté makers; aged 45 days to 3 months.",W+"Morbier_cheese",
    v=[V("Morbier Marcel Petite","Marcel Petite")],dt="ivory paste, horizontal ash line · 45 days–3 months")]},
{"n":"Tomme","a":"tome · toma",
 "d":"Semi-hard pressed cheese of the Alpine or Pyrenean type, in small wheels with a natural grey rind, often from skimmed milk.",
 "t":["cow, ewe or goat milk","skimmed or whole milk","natural rind or waxed"],
 "s":"https://www.artisanalcheese.com/products/tomme-de-savoie",
 "x":[
  A("Tomme de Savoie PGI","Mild semi-firm Savoie tomme from skimmed cow's milk with a thick brownish-grey rind, 20–45% fat.",W+"Tomme_de_Savoie",dt="beige paste · winter-hay or summer-grass milk"),
  A("Tome des Bauges PDO","Raw whole-milk tomme of the Bauges mountains with a thick greyish-brown crust.",W+"Tome_des_Bauges",dt="about 17 cm, just over 1 kg · up to 3 months"),
  A("Toma Piemontese PDO","Piedmont cow's-milk toma in round wheels of 1.8–8 kg, PDO 1996.","https://it.wikipedia.org/wiki/Toma_piemontese",y="PDO 1996",dt="15–35 cm · 15–60 days by size"),
  A("Tomme des Pyrénées PGI","Mild rustic Pyrenean tomme, often in black or gold wax; PGI 2021.",W+"Tomme_des_Pyr%C3%A9n%C3%A9es",y="PGI 2021",
    v=[V("Black-rind tomme",d="21 days minimum."),V("Gold-rind tomme",d="45 days minimum.")],dt="raw or pasteurised cow's milk · waxed")],
 "m":[["Tomme Bejo","Maison Bejo"]]},
]
brands=[
 {"n":"Emmi","c":"Switzerland","f":"","seg":"Dairy group","d":"Swiss milk processor headquartered in Lucerne with plants in Europe and the Americas.","lines":["Kaltbach"],"eras":[],"sig":["Le Gruyère AOP"],"sc":[],"rel":[],"s":W+"Emmi_AG"},
 {"n":"Marcel Petite","c":"France","f":"","seg":"Comté affineur","d":"Franche-Comté affineur that has aged Comté at the 1870s Fort Saint-Antoine since 1965.","lines":["Comté Elegance","Comté Symphonie"],"eras":[],"sig":["Comté AOP","Morbier PDO"],"sc":[],"rel":[],"s":"https://sheridanscheesemongers.com/pages/producer/marcel-petite"},
 {"n":"Appenzeller Käse GmbH","c":"Switzerland","f":"","seg":"Cheese trade organisation","d":"Sortenorganisation of Appenzell that markets Appenzeller cheese under colour labels.","lines":["Silver Label","Gold Label","Black Label","Purple Label"],"eras":[],"sig":["Appenzeller"],"sc":[],"rel":[],"s":"https://www.appenzeller.ch/en/"},
]
trads=[{"n":"Swiss and Jura alpine cheesemaking","g":"Food & drink","r":"Swiss Alps, Jura massif, Savoie, Allgäu, Vorarlberg and Tyrol","p":"Medieval to present (Appenzeller 1282; Bernese Alpkäse 1548)",
 "d":"Large cooked-pressed cheeses from raw cow's milk made in village co-operatives and summer Alp huts, then aged for months.",
 "tech":"curd cooked in copper cauldrons, sometimes over wood fire, pressed into large wheels, brined and cellar-aged with turning and brushing",
 "mat":"raw cow's milk from pasture or hay, no silage",
 "forms":["Gruyère","Comté","Emmental","Beaufort","Bergkäse & Alpkäse","Appenzeller"],
 "ctr":["Comté fruitières (about 150 co-operatives)","Fort Saint-Antoine (Marcel Petite)","Kaltbach cave (Emmi)","L'Etivaz Alp huts","Bernese Oberland Alps"],
 "auth":"AOP/PDO marks, casein or rind marks, Comté green or brown band, Appenzeller colour labels",
 "s":W+"Alpk%C3%A4se"}]
notes=("Greek gravieras (Agrafon, Kritis, Naxou) and San Michali left out of this shelf: they go to Regional pressed cheese (Greek hard cheese). "
 "Montasio, Piave, Bitto and Tolminc left out: they go to the Italian shelf. Abondance and Beaufort moved to Beaufort & Abondance; Alpkäse/Bergkäse PDOs to Bergkäse & Alpkäse. "
 "Glarner Alpkäse, Formaggio d'alpe ticinese, Gailtaler Almkäse, Formai de Mut and Tokachi raclette kept as m (no page retrieved). "
 "Templegall and L'Estival kept in Comté m, Tomme Bejo in Tomme m (style not confirmed). Affineurs Arnaud (Juraflore, Fort des Rousses) and Seignemartin left out: no retrieved page (SIAL 403; no cheese hit for Seignemartin). "
 "Kaltbach versions taken from old data (cave pages 403). Raclette kind source replaced with Wikipedia Raclette (old source was an unrelated contest page). Girolle is a kitchen tool: noted in Tête de Moine detail only.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/J3/shelves/03_03.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print('kinds',len(kinds),'arch',sum(len(k.get('x',[])) for k in kinds))
