import json, os
W = 'https://en.wikipedia.org/wiki/'
PORT, SHER, MAD, MARS, VDN = W+'Port_wine', W+'Sherry', W+'Madeira_wine', W+'Marsala_wine', W+'Vin_doux_naturel'
FORT = W+'Mistela'
OLD = 'https://www.wine.com/list/wine/dessert-sherry-and-port/7155-128'
OLDM = 'https://bgwm.co.uk/collections/marsala-wine'


def X(n, d, s, mk='', y='', a='', v=None, dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}


def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}


port = {"n": "Port", "a": "Porto · Port wine", "d": "Sweet red or white wine from the Douro Valley, fortified with grape spirit during fermentation.",
  "t": ["Bottle-aged (ruby family)", "Wood-aged (tawny family)", "Filtered / unfiltered", "Age indication 10 · 20 · 30 · 40 · 50 years"],
  "s": OLD,
  "x": [
    X("Vintage Port", "Single declared year, at most about 2.5 years in cask, then aged in bottle for decades; about 2% of production.", PORT,
      v=[V("Quinta do Crasto Vintage Port", "Quinta do Crasto"), V("Vallegre Vista Alegre Vintage Port", "Vallegre"),
         V("Ferreira 1815 vintage", "Ferreira", "1815", "oldest vintage port still sold by a shipper")],
      dt="declared year · house blend or single quinta · bottle size"),
    X("Quinta do Noval Nacional", "Vintage port from Noval's Nacional vineyard of ungrafted vines planted in 1925; among the most expensive ports.", PORT,
      mk="Quinta do Noval", y="1925", dt="declared year only"),
    X("Single quinta vintage Port", "Vintage port from one estate, usually released in years the house does not declare its main vintage.", PORT,
      v=[V("Graham's Quinta dos Malvedos Single Quinta Vintage Port", "Graham's"), V("Taylor's Quinta de Vargellas", "Taylor's"),
         V("Dow's Quinta do Bomfim", "Dow's"), V("Cockburn's Quinta dos Canais Single Quinta Vintage Port", "Cockburn's")],
      dt="estate · year"),
    X("Late bottled vintage (LBV)", "Single-year port aged 4–6 years in wood before bottling; filtered or unfiltered.", W+'Taylor,_Fladgate,_&_Yeatman',
      mk="Taylor's", a="LBV", v=[V("Fonseca Quinta Milieu 1958", "Fonseca", "1958", "early LBV reference")],
      dt="filtered (ready) / unfiltered (decant) · year"),
    X("Colheita Port", "Single-vintage tawny aged at least seven years in wood, harvest year on the label.", PORT, a="Single harvest tawny",
      v=[V("Kopke Colheita 1957", "Kopke", "1957"), V("Kopke Colheita 1967", "Kopke", "1967"), V("Kopke Colheita 1987 Port", "Kopke", "1987"),
         V("Kopke Colheita Port", "Kopke"), V("Taylor's Single Harvest", "Taylor's"),
         V("Graham's 1882 Ne Oublie Tawny", "Graham's", "1882", "released 2014 in 656 decanters")],
      dt="harvest year · bottling date"),
    X("Aged tawny with indication of age", "Blend of vintages aged in wood, labelled 10, 20, 30, 40 or 50 years (target average age).", PORT,
      v=[V("Burmester 20 Year Old Tawny Port", "Burmester", "", "20 years"), V("Menin Douro Estates 50 Year Old Tawny Port", "Menin Douro Estates", "", "50 years"),
         V("Menin Porto Tawny 80 Anos", "Menin", "", "80 years")],
      dt="10 · 20 · 30 · 40 · 50 years · bottling date"),
    X("Reserve ruby", "Premium ruby approved by the IVDP tasting panel; the term 'vintage character' was banned in 2002.", PORT, a="Reserve port",
      v=[V("Graham's Six Grapes", "Graham's", "", "the house reserve port")], dt="house blend"),
    X("Ruby Port", "Youngest and most common style, 2–3 years in tank, fined and cold-filtered before bottling.", PORT, dt="house blend"),
    X("Tawny Port", "Wood-aged 3–7 years and blended to a house style; golden-brown with nutty flavours. Reserve tawny about seven years.", PORT,
      dt="basic · reserve"),
    X("Crusted Port", "Blend of several vintages bottled unfiltered, throwing a crust; decanted before drinking.", PORT, dt="bottling year"),
    X("White Port", "Port from white grapes, dry to very sweet ('lagrima').", PORT,
      v=[V("Taylor's Chip Dry", "Taylor's", "1934", "dry white port"), V("Dalva Porto Colheita White", "Dalva", "", "white colheita"),
         V("Jáfoste 80 Year Old White Port", "Jáfoste", "", "aged white")],
      dt="dry · sweet · lagrima · age indication"),
    X("Rosé Port", "Ruby port made with limited skin contact, like rosé wine; first released in 2008.", PORT, y="2008",
      v=[V("Croft rosé", "Croft", "2008"), V("Poças rosé", "Poças", "2008")]),
    X("Garrafeira Port", "Vintage-dated port aged 3–6 years in wood, then at least eight years in glass demijohns.", PORT, mk="Niepoort"),
  ],
  "m": [["Ferreira Porto Dona Antonia", "Ferreira"]]}

sherry = {"n": "Sherry", "a": "Jerez · Xérès", "d": "Fortified wine from the Jerez area of Andalusia, aged in soleras either under flor or oxidatively.",
  "t": ["En rama (lightly filtered)", "VOS (20+ years average)", "VORS (30+ years average)", "Dry · pale cream · medium · cream"],
  "s": OLD,
  "x": [
    X("Tío Pepe", "Palomino fino of González Byass from soleras laid down in 1844; named after a founder's uncle.", W+'T%C3%ADo_Pepe',
      mk="González Byass", y="1844", v=[V("Tío Pepe sombrero-and-guitar bottle", "González Byass", "1935", "classic brand image")]),
    X("Fino", "Driest and palest sherry, aged under a layer of flor yeast.", SHER,
      v=[V("Valdespino Inocente Fino", "Valdespino")], dt="en rama · bottling date"),
    X("Manzanilla", "Especially light fino matured in Sanlúcar de Barrameda; manzanilla pasada is older and nuttier.", SHER,
      v=[V("Manzanilla pasada", "", "", "longer aged, partly oxidised")], dt="fresca · pasada · en rama"),
    X("Amontillado", "Aged first under flor, then oxidatively; amber and naturally dry.", SHER,
      v=[V("Gonzalez Byass Del Duque V.O.R.S. Amontillado", "González Byass", "", "VORS"),
         V("Gonzalez Byass Tio Pepe Cuatro Palmas Amontillado", "González Byass"),
         V("Bodegas Tradicion VORS 30 Years Amontillado", "Bodegas Tradicion", "", "VORS"),
         V("Lustau Almacenista Antonio Caballero y Sobrinos Amontillado", "Emilio Lustau", "", "almacenista"),
         V("Lustau Amontillado del Castillo Almacenista Antonio Caballero y Sobrinos", "Emilio Lustau", "", "almacenista")],
      dt="age (VOS/VORS) · almacenista · en rama"),
    X("Palo Cortado", "Starts like amontillado, then takes on oloroso character after the flor dies.", SHER,
      v=[V("Lustau VORS 30 Years Old Palo Cortado En Rama", "Emilio Lustau", "", "VORS, en rama"), V("Tabajete VORS Palo Cortado", "Tabajete", "", "VORS")],
      dt="age (VOS/VORS)"),
    X("Oloroso", "Oxidatively aged, dark and rich; 18–20% ABV.", SHER,
      v=[V("Tabajete VORS Oloroso", "Tabajete", "", "VORS")], dt="dry · sweetened · age"),
    X("Cream sherry", "Sweetened style first made in the 1860s, usually oloroso blended with Pedro Ximénez.", SHER, y="1860s",
      v=[V("Lustau Cream 30 YO VORS", "Emilio Lustau", "", "VORS")], dt="cream · pale cream"),
    X("Pedro Ximénez", "Intensely sweet, dark sherry from sun-dried PX grapes (212+ g/L sugar).", SHER, a="PX",
      v=[V("Lustau VORS 30 Years Old Pedro Ximénez", "Emilio Lustau", "", "VORS; also listed as Lustau Pedro Ximenez VORS 30 YO")],
      dt="age (VOS/VORS)"),
    X("Moscatel", "Sweet sherry from dried Moscatel grapes (160+ g/L sugar).", SHER,
      v=[V("Lustau VORS 30 Years Old Moscatel", "Emilio Lustau", "", "VORS")]),
  ],
  "m": [["Lustau East India Solera", "Emilio Lustau"]]}

madeira = {"n": "Madeira", "a": "Madeira wine", "d": "Fortified wine from Madeira, heated during ageing (estufagem or canteiro) to give a long-lived oxidised style.",
  "t": ["Finest (3 years)", "Reserve (5 years)", "Special Reserve (10 years)", "Extra Reserve (15+ years)", "Colheita (single harvest, 5+ years)",
        "Frasqueira (vintage, 20+ years)", "Estufagem / canteiro", "Tinta Negra"],
  "s": OLD,
  "x": [
    X("Sercial", "Driest Madeira (9–27 g/L), high acidity and almond notes.", MAD,
      v=[V("D'Oliveiras Sercial 1990 Madeira", "D'Oliveiras", "1990")], dt="age category · harvest year"),
    X("Verdelho", "Medium-dry Madeira (27–45 g/L) with smoky notes and high acidity.", MAD,
      v=[V("D'Oliveiras Colheita Verdelho 2005 Madeira", "D'Oliveiras", "2005", "colheita"), V("D'Oliveiras Verdelho 1981", "D'Oliveiras", "1981")],
      dt="age category · harvest year"),
    X("Terrantez", "Rare variety between Verdelho and Bual in sweetness, revived after near extinction.", MAD,
      v=[V("Barbeito 1795 Terrantez", "Barbeito", "1795")]),
    X("Bual", "Medium-rich Madeira (45–63 g/L) with raisin flavours.", MAD, a="Boal",
      v=[V("Henriques & Henriques Boal 30 Year Old Madeira", "Henriques & Henriques", "", "30 years")], dt="age category · harvest year"),
    X("Malmsey", "Sweetest Madeira (63–117 g/L), coffee and caramel flavours.", MAD, a="Malvasia · Malvazia",
      v=[V("Blandy's Malmsey Madeira", "Blandy's"), V("D'Oliveiras Malvazia 1991 Madeira", "D'Oliveiras", "1991")],
      dt="age category · harvest year"),
    X("Rainwater", "Dry to medium-dry aperitif style, today usually Tinta Negra aged about three years.", MAD,
      v=[V("Barbeito Rainwater", "Barbeito")]),
  ]}

marsala = {"n": "Marsala", "a": "Marsala DOC", "d": "Fortified wine from the Marsala area of western Sicily, graded by colour, sweetness and age.",
  "t": ["Oro (golden)", "Ambra (amber, with mosto cotto)", "Rubino (ruby, red grapes)", "Secco (≤40 g/L)", "Semisecco (41–100 g/L)", "Dolce (>100 g/L)"],
  "s": OLDM,
  "x": [
    X("Marsala Vergine Stravecchio / Riserva", "Top grade of Marsala Vergine, aged at least ten years.", MARS),
    X("Marsala Vergine / Soleras", "Dry Marsala aged at least five years.", MARS),
    X("Marsala Superiore Riserva", "Superiore aged at least four years.", MARS),
    X("Marsala Superiore", "Marsala aged at least two years.", MARS,
      v=[V("Cantina Florio Marsala Superiore Dolce", "Florio", "", "dolce"), V("Carlo Pellegrino Marsala Superiore Secco", "Pellegrino", "", "secco")],
      dt="oro · ambra · rubino · secco to dolce"),
    X("Marsala Fine", "Entry grade aged at least one year; much used in cooking.", MARS, dt="oro · ambra · rubino · secco to dolce"),
  ]}

vdn = {"n": "Vin doux naturel", "a": "VDN", "d": "Lightly fortified French wine, usually Muscat or Grenache, whose fermentation is stopped by grape spirit (mutage).",
  "t": ["Blanc · rosé · ambré · grenat · tuilé", "Hors d'âge", "Rancio", "Oxidised / unoxidised"],
  "s": VDN,
  "x": [
    X("Banyuls", "Grenache-based Roussillon VDN from four Côte Vermeille communes; AOC 1936, at least ten months' maturation.", W+'Banyuls_AOC', y="1936",
      v=[V("Banyuls Grand Cru", "", "1962", "75% Grenache noir, 30 months' maturation")], dt="colour · age · rancio"),
    X("Maury", "Roussillon VDN of at least 75% Grenache noir; AOC 1936, often aged in glass bonbonnes in the sun.", W+'Maury_AOC', y="1936",
      v=[V("Vintage-dated Maury", "", "1975", "bottled early, mainly since 1975"), V("Maury rancio", "", "", "aged in demijohns in the sun")],
      dt="grenat · tuilé · rancio · vintage"),
    X("Muscat de Beaumes-de-Venise", "Rhône Muscat VDN, AOC 1943, minimum 15% alcohol.", W+'Beaumes_de_Venise_AOC', y="1943"),
    X("Rivesaltes", "Roussillon VDN, red or white.", VDN, dt="ambré · grenat · tuilé · hors d'âge"),
    X("Muscat de Rivesaltes", "Roussillon VDN from white Muscat.", VDN),
    X("Muscat de Frontignan", "Languedoc VDN from white Muscat.", VDN),
    X("Rasteau", "Grenache-based Rhône VDN.", VDN),
    X("Muscat du Cap Corse", "Corsican Muscat VDN.", VDN),
  ]}

regional = {"n": "Regional fortified wine", "a": "Other fortified wine · vin de liqueur · mistelle",
  "d": "Fortified wines and vins de liqueur from outside Port, Sherry, Madeira, Marsala and the French VDNs.",
  "s": FORT,
  "x": [
    X("Rutherglen Muscat", "Victorian fortified wine from Muscat à Petits Grains Rouge (Rutherglen Brown Muscat), graded by average age.",
      'https://www.explorerutherglen.com.au/rutherglenmuscat/',
      v=[V("Rutherglen Muscat", "", "", "3–5 years"), V("Classic Rutherglen Muscat", "", "", "6–10 years"),
         V("Grand Rutherglen Muscat", "", "", "11–19 years"), V("Rare Rutherglen Muscat", "", "", "20+ years"),
         V("Morris Wines Old Premium Rare Muscat", "Morris Wines")],
      dt="classification Rutherglen · Classic · Grand · Rare"),
    X("Rutherglen Topaque", "Sweet fortified wine of the Rutherglen region, formerly called Tokay.", W+'Rutherglen,_Victoria', a="Tokay (former name)"),
    X("Moscatel de Setúbal", "Portuguese fortified Muscat (Muscat of Alexandria or Moscatel Roxo) matured in wood.", W+'Moscatel_de_Set%C3%BAbal',
      mk="José Maria da Fonseca", dt="vintage or blend · Moscatel Roxo"),
    X("Commandaria", "Cypriot sweet wine from sun-dried Mavro and Xynisteri grapes, aged in oak.", FORT),
    X("Pineau des Charentes", "Cognac-zone aperitif of grape must fortified with Cognac (vin de liqueur).", FORT),
    X("Floc de Gascogne", "Vin de liqueur of Armagnac and grape juice from the same vineyard.", FORT),
    X("Macvin du Jura", "Jura vin de liqueur.", FORT, a="Macvin"),
    X("Montilla-Moriles", "Sherry-like wines from Córdoba, mostly Pedro Ximénez and usually not fortified; DO since 1932.", W+'Montilla-Moriles', y="1932",
      dt="fino · amontillado · oloroso · palo cortado · Pedro Ximénez"),
  ],
  "m": [["Bodegas de Alberto Dorado", "Bodegas de Alberto"]]}

K = 'knowledge'


def B(n, c, f, seg, d, s=K, lines=None, sig=None, rel=None, eras=None):
    return {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": lines or [], "eras": eras or [], "sig": sig or [], "sc": [], "rel": rel or [], "s": s}


brands = [
  B("Taylor's", "Portugal", "1692", "Port house", "Port shipper founded by Job Bearsley in Vila Nova de Gaia; Taylor, Fladgate & Yeatman since 1838, part of The Fladgate Partnership.",
    W+'Taylor,_Fladgate,_&_Yeatman', lines=["Chip Dry", "Quinta de Vargellas"], sig=["Late bottled vintage (LBV)"], rel=["Fonseca", "Croft"]),
  B("Graham's", "Portugal", "1820", "Port house", "Port house of William and John Graham, owned by the Symington family since 1970.", W+"Graham's",
    lines=["Six Grapes", "Quinta dos Malvedos"], sig=["Single quinta vintage Port", "Reserve ruby"], rel=["Dow's", "Cockburn's"]),
  B("Dow's", "Portugal", "", "Port house", "Symington-owned port house.", W+'Symington_Family_Estates', lines=["Quinta do Bomfim"], rel=["Graham's"]),
  B("Cockburn's", "Portugal", "", "Port house", "Symington-owned port house.", W+'Symington_Family_Estates', lines=["Quinta dos Canais"], rel=["Graham's"]),
  B("Fonseca", "Portugal", "", "Port house", "Port house of The Fladgate Partnership, sister to Taylor's and Croft.", W+'Taylor,_Fladgate,_&_Yeatman', rel=["Taylor's"]),
  B("Croft", "Portugal", "", "Port house", "Port house of The Fladgate Partnership; an early maker of rosé port (2008).", W+'Taylor,_Fladgate,_&_Yeatman',
    sig=["Rosé Port"], rel=["Taylor's"]),
  B("Quinta do Noval", "Portugal", "", "Port house", "Douro port house known for the Nacional vineyard of ungrafted vines.", PORT, sig=["Quinta do Noval Nacional"]),
  B("Niepoort", "Portugal", "", "Port house", "Port house associated with the garrafeira style.", PORT, sig=["Garrafeira Port"]),
  B("Poças", "Portugal", "", "Port house", "Port house that, with Croft, first released rosé port in 2008.", PORT, sig=["Rosé Port"]),
  B("Ferreira", "Portugal", "", "Port house", "Port and Douro wine house, maker of Barca Velha since 1952.", PORT, lines=["Dona Antonia", "Barca Velha"]),
  B("Kopke", "Portugal", "", "Port house", "Port shipper noted for colheita tawnies.", PORT, sig=["Colheita Port"]),
  B("González Byass", "Spain", "1835", "Sherry bodega", "Jerez sherry house founded by Manuel María González Angel, later joined by Robert Blake Byass.",
    W+'Gonz%C3%A1lez_Byass', lines=["Del Duque", "Cuatro Palmas"], sig=["Tío Pepe"]),
  B("Emilio Lustau", "Spain", "1896", "Sherry bodega", "Jerez sherry house known for its Almacenista range; owned by Grupo Caballero from 1990.",
    W+'Emilio_Lustau', lines=["Almacenista", "VORS"]),
  B("Blandy's", "Portugal", "1811", "Madeira house", "Madeira shipper founded in 1811.", MAD, sig=["Malmsey"]),
  B("Cossart Gordon", "Portugal", "1745", "Madeira house", "Madeira shipper founded in 1745.", MAD),
  B("Barbeito", "Portugal", "", "Madeira house", "Madeira producer known for Rainwater and old Terrantez.", MAD, sig=["Rainwater", "Terrantez"]),
  B("D'Oliveiras", "Portugal", "", "Madeira house", "Funchal producer named among the top canteiro houses.", MAD),
  B("Florio", "Italy", "1833", "Marsala house", "Marsala house begun when Vincenzo Florio bought land at Marsala in 1833; later bought Woodhouse's firm.", MARS,
    rel=["Pellegrino"]),
  B("Pellegrino", "Italy", "", "Marsala house", "With Florio, one of the two leading Marsala producers.", MARS, rel=["Florio"]),
  B("José Maria da Fonseca", "Portugal", "1834", "Wine producer", "Setúbal producer believed to have invented Moscatel de Setúbal and holding a quasi-monopoly on it.",
    W+'Moscatel_de_Set%C3%BAbal', sig=["Moscatel de Setúbal"]),
  B("Morris Wines", "Australia", "", "Fortified wine producer", "Rutherglen producer of fortified Muscat (Morris of Rutherglen).",
    'https://www.explorerutherglen.com.au/rutherglenmuscat/', sig=["Rutherglen Muscat"]),
]

notes = ("Planned kind 'Other fortified wine' is kept as 'Regional fortified wine' (the checker bars 'Other …' names); its old models are kept "
  "(Morris under Rutherglen Muscat; Bodegas de Alberto Dorado stays in m because no page I retrieved describes Rueda dorado, and the Rueda DO page does not mention it). "
  "Marsala moved out of the catch-all into its own kind; the generic old model 'Marsala' (no maker) was dropped. Near-duplicate old entries were merged: "
  "Lustau PX VORS (two spellings) and D'Oliveiras Malvazia 1991 (two spellings). Ferreira Dona Antonia and Lustau East India Solera stay in m because no retrieved page gave their style. "
  "Montilla-Moriles is included as the plan asks, though its page says the wines are usually not fortified. Not added: Rutherglen producers other than Morris, "
  "Banyuls/Maury estates, Madeira 20–50 year categories, sherry 12/15-year labels, Málaga and Mavrodaphne (no retrieved page). Pages that failed: Wikipedia Taylor's_(port) and Quinta_do_Noval (404), "
  "wein.plus (401), Wikidata (429). Brands for Dow's, Cockburn's, Fonseca and Croft are cited to group pages that only list them; founding years left blank where not on a retrieved page.")

out = {"kinds": [port, sherry, madeira, marsala, vdn, regional], "brands": brands, "traditions": [], "notes": notes}
p = 'work/J7/shelves/03_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('ok', sum(len(k.get('x', [])) for k in out['kinds']), 'archetypes', len(brands), 'brands')
