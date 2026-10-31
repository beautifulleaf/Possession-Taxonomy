import json, os
W='https://en.wikipedia.org/wiki/'
S1855=W+'Bordeaux_Wine_Official_Classification_of_1855'; SSE=W+'Classification_of_Saint-%C3%89milion_wine'
SBX=W+'Bordeaux_wine'
def X(n,d,mk,y,s,v,dt='',a=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
bdx={"n":"Bordeaux red blend","a":"Claret · Bordeaux blend · Bordeaux-style red",
 "d":"Red wine blended from Cabernet Sauvignon, Merlot, Cabernet Franc and their Bordeaux partners, in Bordeaux or in its style elsewhere.",
 "t":["Cabernet-led (Left Bank)","Merlot-led (Right Bank)","Grand vin","Second wine"],
 "s":"https://www.wine.com/list/wine/red-wine/7155-124",
 "x":[
  X("Médoc and Graves classed growth","Left Bank red ranked in the 1855 classification, from first to fifth growth; Cabernet Sauvignon-led.","","1855",S1855,
    [("Château Lynch-Bages","Château Lynch-Bages","","Pauillac fifth growth; second wine Echo de Lynch-Bages")],
    "growth 1st–5th · commune (Pauillac, Margaux, Pessac-Léognan…) · grand vin / second wine · vintage",a="Grand cru classé en 1855 · Left Bank blend"),
  X("Château Lafite Rothschild","Pauillac first growth of 1855; typically 80–95% Cabernet Sauvignon with Merlot.","Château Lafite Rothschild","1855",W+'Ch%C3%A2teau_Lafite_Rothschild',
    [("Château Lafite Rothschild (grand vin)","Château Lafite Rothschild","","first growth"),("Carruades de Lafite","Château Lafite Rothschild","","second wine")],"vintage · bottle size"),
  X("Château Latour","Pauillac first growth of 1855 on the border with Saint-Julien.","Château Latour","1855",W+'Ch%C3%A2teau_Latour',
    [("Château Latour (grand vin)","Château Latour","","first growth"),("Les Forts de Latour","Château Latour","1966","second wine"),("Pauillac de Latour","Château Latour","1989","third wine")],"vintage · bottle size"),
  X("Château Margaux","Margaux first growth of 1855.","Château Margaux","1855",W+'Ch%C3%A2teau_Margaux',
    [("Château Margaux (grand vin)","Château Margaux","","first growth"),("Pavillon Rouge du Château Margaux","Château Margaux","","second wine")],"vintage · bottle size"),
  X("Château Haut-Brion","Pessac first growth of 1855, the only Graves estate among the first growths.","Château Haut-Brion","1855",W+'Ch%C3%A2teau_Haut-Brion',
    [("Château Haut-Brion (grand vin)","Château Haut-Brion","","first growth"),("Le Clarence de Haut-Brion","Château Haut-Brion","2007","second wine, formerly Château Bahans Haut-Brion")],"vintage · bottle size"),
  X("Château Mouton Rothschild","Pauillac estate promoted from second to first growth in 1973; artist-designed labels each vintage.","Château Mouton Rothschild","1973",W+'Ch%C3%A2teau_Mouton_Rothschild',
    [("Château Mouton Rothschild (grand vin)","Château Mouton Rothschild","1973","first growth since 1973")],"vintage · artist label (permanent from 1946) · bottle size"),
  X("Right Bank Merlot-led blend","Saint-Émilion and Pomerol red led by Merlot with Cabernet Franc, softer in tannin than the Left Bank.","","",SBX,
    [("Chateau L'Enclos Pomerol","Chateau L'Enclos","","Pomerol"),("Chateau La Croix Younan Saint-Emilion Grand Cru","Chateau La Croix Younan","","Saint-Émilion Grand Cru"),("Maison Ginestet Grand Vin Saint-Emilion Grand Cru","Maison Ginestet","","Saint-Émilion Grand Cru")],
    "appellation (Saint-Émilion, Pomerol, satellites) · Merlot share · vintage",a="Libournais blend"),
  X("Saint-Émilion classed growth","Saint-Émilion red ranked Premier Grand Cru Classé A or B or Grand Cru Classé, first published 1955 and revised.","","1955",SSE,
    [("Château Pavie","","2022","Premier Grand Cru Classé A"),("Château Figeac","","2022","Premier Grand Cru Classé A"),("Château Angélus","","2021","withdrew from the classification"),("Château Ausone","","2022","withdrew from the classification")],
    "rank A / B / Grand Cru Classé · classification edition · vintage"),
  X("Château Cheval Blanc","Saint-Émilion estate with a Cabernet Franc-led blend (about 57% with Merlot); ranked Premier Grand Cru Classé A from 1955 until it withdrew in 2021.","Château Cheval Blanc","1955",W+'Ch%C3%A2teau_Cheval_Blanc',
    [("Château Cheval Blanc (grand vin)","Château Cheval Blanc","",""),("Le Petit Cheval","Château Cheval Blanc","","second wine")],"vintage · bottle size"),
  X("Cru Bourgeois du Médoc","Médoc red from estates outside the 1855 classification, ranked Cru Bourgeois, Supérieur or Exceptionnel.","","2020",W+'Cru_Bourgeois',
    [("Château de Malleret Cru Bourgeois Exceptionnel Haut-Médoc","Chateau de Malleret","","Exceptionnel"),("Château Braude Fellonneau Haut-Médoc","Château Braude Fellonneau","","Haut-Médoc")],
    "tier Cru Bourgeois / Supérieur / Exceptionnel · appellation · vintage"),
  X("Sassicaia","Bolgheri Cabernet Sauvignon–Cabernet Franc wine, the first Super Tuscan; only single-estate wine in Italy with its own DOC (1994).","Tenuta San Guido","1968",W+'Sassicaia',
    [("Sassicaia","Tenuta San Guido","1968","first commercial vintage, released 1971"),("Guidalberto","Tenuta San Guido","2000","second wine"),("Le Difese","Tenuta San Guido","","third wine, Cabernet Sauvignon with Sangiovese")],"vintage · bottle size"),
  X("Ornellaia","Bolgheri blend of Cabernet Sauvignon, Merlot, Cabernet Franc and Petit Verdot.","Tenuta dell'Ornellaia","1985",W+'Tenuta_dell%27Ornellaia',
    [("Ornellaia","Tenuta dell'Ornellaia","1985","first vintage"),("Le Serre Nuove dell'Ornellaia","Tenuta dell'Ornellaia","1997","second wine")],"vintage · bottle size"),
  X("Opus One","Napa Valley Bordeaux-style blend from a Mondavi–Rothschild joint venture in Oakville.","Opus One","1979",W+'Opus_One_Winery',
    [("Opus One","Opus One","1979","first vintage, To Kalon grapes"),("Opus One Overture","Opus One","1993","second wine")],"vintage · bottle size"),
  X("Meritage","Trademarked name for a Bordeaux-variety blend made outside Bordeaux, no variety above 90%.","","1988",W+'Meritage',
    [("The Poet","Cosentino Winery","1986","first wine labelled Meritage"),("Dry Creek Vineyard Meritage","Dry Creek Vineyard","1985","oldest vintage released as Meritage")],
    "region (California, Canada…) · blend share · vintage",a="Bordeaux-style blend (US)"),
  X("Ridge Monte Bello","Santa Cruz Mountains Cabernet Sauvignon field blend with Merlot and Petit Verdot; 1971 vintage placed fifth at the 1976 Judgment of Paris.","Ridge Vineyards","1962",W+'Ridge_Vineyards',
    [("Monte Bello","Ridge Vineyards","1962","first commercial release")],"vintage"),
 ]}
red={"n":"Red blend","a":"Red cuvée · Field blend · Assemblage",
 "d":"Still red wine blended from several grapes outside the Bordeaux pattern, such as Rhône, Tuscan, Iberian and New World blends.",
 "t":["Grenache–Syrah–Mourvèdre (GSM)","Sangiovese–Cabernet","Tempranillo-led","Field blend","Cabernet–Carmenère"],
 "s":"https://www.wine.com/list/wine/red-wine/7155-124",
 "x":[
  X("Southern Rhône blend","Grenache-led blend with Syrah and Mourvèdre; Châteauneuf-du-Pape allows 18 varieties.","","1936",W+'Ch%C3%A2teauneuf-du-Pape_AOC',
    [("Château de Beaucastel","Château de Beaucastel","","uses all the originally permitted varieties"),("Domaine du Vieux Télégraphe","Domaine du Vieux Télégraphe","","La Crau"),("Château Fortia","Château Fortia","","estate of Baron Pierre le Roy"),("Perdeberg Cellar The Dry Land Collection Joseph's Legacy Shiraz-Grenache-Mourvèdre","Perdeberg Cellar","","South African GSM")],
    "appellation (Châteauneuf-du-Pape, Côtes du Rhône…) · Grenache share · vintage",a="GSM · Châteauneuf-du-Pape"),
  X("Super Tuscan","Tuscan red made outside DOC rules, often Sangiovese with Cabernet or Merlot; many became cult wines.","","1970s",W+'Super_Tuscan',
    [("Le Volte dell'Ornellaia","Tenuta dell'Ornellaia","1991","Sangiovese, Cabernet Sauvignon and Merlot")],"grapes · IGT / DOC · vintage"),
  X("Tignanello","Antinori's Sangiovese–Cabernet blend, a pioneer Super Tuscan; 80% Sangiovese, 15% Cabernet Sauvignon, 5% Cabernet Franc since 1995.","Marchesi Antinori","1971",W+'Tignanello',
    [("Tignanello","Marchesi Antinori","1971","first vintage, released 1978; IGT from 1994")],"vintage · bottle size"),
  X("Rioja red","Blend of Tempranillo, Garnacha, Mazuelo and Graciano, sold by ageing grade; Spain's first DOCa (1991).","","1991",W+'Rioja_(wine)',
    [("Marqués de Murrieta Gran Reserva","Marqués de Murrieta","1942","released 1983 after 41 years")],
    "grade Crianza / Reserva / Gran Reserva · vintage"),
  X("Douro red","Unfortified Douro wine from Touriga Nacional, Tinta Roriz, Touriga Franca and other Port grapes.","","1952",W+'Douro_DOC',
    [("Barca Velha","","1952","first produced; grapes from Quinta do Vale de Meão")],"grapes · vintage"),
 ],
 "m":[["A Corazón Abierto Gran Corte","A Corazón Abierto"],["Abadia Retuerta Cuvée Palomar","Abadia Retuerta"],["Arzuaga Reserva","Arzuaga"],["Bodegas Luzón Por Tí","Bodegas Luzón"],["Bodegas Olarra Nucerro Gran Reserva","Bodegas Olarra"],["Campillo 57 Selección Especial","Campillo"],["Château Lancyre Grande Cuvée Pic Saint Loup","Château Lancyre"],["El Coto Coto de Imaz Gran Reserva","El Coto"],["Finca Rodma Gran Rodma","Finca Rodma"],["Helanhong Winery Helan Hong Jiangnan Reserva Red","Helanhong Winery"],["Marqués de Cáceres Gaudium Reserva","Marqués de Cáceres"],["Monteabellón Finca Matambres","Monteabellón"],["Pago Finca Élez Las Teselas de Élez","Pago Finca Élez"],["Quinta da Vacaria Grande Reserva","Quinta da Vacaria"],["Ridge Lytton Springs Red Blend","Ridge Vineyards"],["Tobelos Tahon Reserva","Tobelos"],["Valduero 6 Años Reserva Premium","Valduero"],["Viña Indómita Duette Cabernet Sauvignon-Carménère","Viña Indómita"]]}
def B(n,c,f,seg,d,sig,s,lines=(),rel=()): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Château Lafite Rothschild","France","","Bordeaux first growth","Pauillac first growth owned by the Rothschild family since the 19th century.",["Château Lafite Rothschild"],W+'Ch%C3%A2teau_Lafite_Rothschild',["Carruades de Lafite"],["Château Mouton Rothschild"]),
 B("Château Latour","France","","Bordeaux first growth","Pauillac first growth bought by François Pinault's Groupe Artemis in 1993.",["Château Latour"],W+'Ch%C3%A2teau_Latour',["Les Forts de Latour","Pauillac de Latour"]),
 B("Château Margaux","France","","Bordeaux first growth","Margaux first growth owned by Corinne Mentzelopoulos.",["Château Margaux"],W+'Ch%C3%A2teau_Margaux',["Pavillon Rouge du Château Margaux","Pavillon Blanc du Château Margaux"]),
 B("Château Haut-Brion","France","","Bordeaux first growth","Pessac-Léognan first growth owned by Domaine Clarence Dillon since 1935.",["Château Haut-Brion"],W+'Ch%C3%A2teau_Haut-Brion',["Le Clarence de Haut-Brion","Château Haut-Brion Blanc"]),
 B("Château Mouton Rothschild","France","","Bordeaux first growth","Pauillac estate promoted to first growth in 1973, known for artist labels.",["Château Mouton Rothschild"],W+'Ch%C3%A2teau_Mouton_Rothschild',[],["Opus One","Château Lafite Rothschild"]),
 B("Château Cheval Blanc","France","","Saint-Émilion estate","Saint-Émilion estate owned by LVMH and the Frère family, known for a Cabernet Franc-led blend.",["Château Cheval Blanc"],W+'Ch%C3%A2teau_Cheval_Blanc',["Le Petit Cheval"]),
 B("Tenuta San Guido","Italy","","Bolgheri estate","Bolgheri estate that makes Sassicaia, the first Super Tuscan.",["Sassicaia"],W+'Sassicaia',["Sassicaia","Guidalberto","Le Difese"],["Tenuta dell'Ornellaia"]),
 B("Tenuta dell'Ornellaia","Italy","1981","Bolgheri estate","Bolgheri estate founded by Lodovico Antinori, owned by the Frescobaldi family since 2005.",["Ornellaia"],W+'Tenuta_dell%27Ornellaia',["Ornellaia","Le Serre Nuove","Le Volte","Masseto"],["Tenuta San Guido","Marchesi Antinori"]),
 B("Marchesi Antinori","Italy","","Tuscan wine house","Florentine wine family firm whose Tignanello pioneered the Super Tuscans.",["Tignanello"],W+'Tignanello',["Tignanello"],["Tenuta dell'Ornellaia"]),
 B("Opus One","United States","1980","Napa Valley estate","Oakville winery founded as a joint venture of Robert Mondavi and Baron Philippe de Rothschild.",["Opus One"],W+'Opus_One_Winery',["Opus One","Overture"],["Château Mouton Rothschild"]),
 B("Ridge Vineyards","United States","","California winery","Santa Cruz Mountains and Sonoma winery known for Monte Bello Cabernet and Zinfandel blends.",["Ridge Monte Bello"],W+'Ridge_Vineyards',["Monte Bello","Lytton Springs","Geyserville"]),
]
notes=("Bordeaux red blend: all 10 old models placed as archetype versions (Lynch-Bages under classed growths; Pomerol/Saint-Émilion Grand Cru wines under Right Bank; Cru Bourgeois wines under Cru Bourgeois). "
 "Red blend (was 'Other red blend'): 18 old models kept in m because no retrieved page tied them to an archetype (e.g. Rioja/Douro membership of El Coto, Cáceres, Quinta da Vacaria unconfirmed); Perdeberg GSM moved into the Southern Rhône archetype. "
 "Left out: Pétrus (100% Merlot, not a blend; belongs with Merlot), Masseto (varietal Merlot), Solaia and other Super Tuscans not on a retrieved page, Saint-Julien/Saint-Estèphe estates, Lytton Springs as field-blend archetype (page does not call it one). "
 "No traditions (not an artisan-craft shelf). Antinori founding year omitted (not on a retrieved page).")
out={"kinds":[bdx,red],"brands":brands,"traditions":[],"notes":notes}
p='work/J7/shelves/00_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p); print('ok')
