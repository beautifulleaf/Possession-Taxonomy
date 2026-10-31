import json, os
W = 'https://en.wikipedia.org/wiki/'
B25 = 'https://www.bjcp.org/style/2021/25'
B26 = 'https://www.bjcp.org/style/2021/26'
TB = W + 'Trappist_beer'

def X(n, d, mk, y, s, v=(), a='', dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [{"n": a_, "mk": b_, "y": c_, "d": d_} for a_, b_, c_, d_ in v], "dt": dt}

kinds = [
 {"n": "Dubbel", "a": "Double · Belgian dubbel · Abbey brown", "d": "Moderately strong, deep reddish-brown Belgian ale with rich malt and dark-fruit esters, finishing fairly dry; about 6–7.6% ABV.",
  "t": ["Trappist", "Abbey (licensed)", "Secular"], "s": W + "Dubbel",
  "x": [
   X("Westmalle Dubbel", "The Trappist brown beer from which the style takes its name; 7% ABV, purple label.", "Westmalle", "1926 (strong brown by 1856)", W + "Westmalle_Brewery",
     [("Strong brown beer", "Westmalle", "1856", "first strong brown, on public sale by 1861"),
      ("Dubbel Bruin", "Westmalle", "1926", "Henrik Verlinden's recipe, still the current one")], dt="bottle 33 cl or 75 cl · draught · vintage"),
   X("Chimay Red", "Chimay's 7% ABV dubbel.", "Chimay", "", W + "Chimay_Brewery", a="Chimay Première · Chimay Rouge", dt="bottle size · vintage"),
   X("Rochefort 6", "Oldest Rochefort Trappist beer; brown, 7.5% ABV, red cap.", "Rochefort", "", W + "Rochefort_Brewery", dt="bottle 33 cl"),
   X("Westvleteren 8", "Westvleteren's 8% ABV dubbel, blue cap; sold only at the abbey.", "Westvleteren", "", W + "Westvleteren_Brewery", dt="unlabelled bottle · cap colour"),
  ],
  "m": [["La Trappe Dubbel", "La Trappe"], ["Achel 8 Bruin", "Achel"], ["St. Bernardus Pater 6", "St. Bernardus"], ["Maredsous Brune", "Duvel Moortgat"],
        ["Corsendonk Bruin", "Corsendonk"], ["Ommegang Dubbel", "Brewery Ommegang"], ["Abbey Ale", "New Belgium"], ["Maudite Dubbel", "Unibroue"]]},
 {"n": "Tripel", "a": "Triple · Belgian tripel", "d": "Strong, pale, somewhat spicy Belgian ale with firm bitterness and a dry finish; about 7.5–9.5% ABV.",
  "t": ["Trappist", "Abbey (licensed)", "Secular"], "s": W + "Tripel",
  "x": [
   X("Westmalle Tripel", "The model for the style: a 9.5% ABV strong pale Trappist ale, yellow label.", "Westmalle", "1930s", W + "Westmalle_Brewery",
     [("Superbier", "Westmalle", "1933", "original name"), ("Tripel", "Westmalle", "1956", "renamed, with more hops, by Brother Thomas")], dt="bottle 33 cl or 75 cl · draught"),
   X("Witkap Tripel", "Hendrik Verlinden's golden strong ale, credited by Michael Jackson as the first beer linked to the tripel name.", "Slaghmuylder", "early 1930s", W + "Tripel",
     [("Witkap Pater", "Drie Linden", "early 1930s", "original name")]),
   X("La Trappe Tripel", "Dutch Trappist tripel from De Koningshoeven.", "La Trappe", "1987", W + "Tripel"),
   X("Chimay Triple", "Chimay's 8% ABV tripel, white label.", "Chimay", "", W + "Chimay_Brewery", a="Chimay White · Cinq Cents"),
  ],
  "m": [["St. Bernardus Tripel", "St. Bernardus"], ["Maredsous Triple", "Duvel Moortgat"], ["Val-Dieu Triple", "Val-Dieu"], ["La Rulles Tripel", "La Rulles"]]},
 {"n": "Belgian dark strong ale", "a": "Quadrupel · Quad · Abt · Grand cru", "d": "Dark, very strong Belgian ale of rich malt, dried dark fruit and spice; about 8–12% ABV.",
  "t": ["Trappist", "Abbey (licensed)", "Secular"], "s": B26,
  "x": [
   X("Westvleteren 12", "10.2% ABV quadrupel, yellow cap; RateBeer's best beer in the world in 2005 and 2014; sold only by reservation at the abbey.", "Westvleteren", "1940", W + "Westvleteren_Brewery", dt="unlabelled bottle · vintage"),
   X("Chimay Blue", "Chimay's 9% ABV classic ale.", "Chimay", "", W + "Chimay_Brewery", a="Chimay Grande Réserve", dt="bottle 33 cl or 75 cl · vintage"),
   X("Rochefort 10", "Dark 11.3% ABV Trappist ale, blue cap.", "Rochefort", "", W + "Rochefort_Brewery",
     [("Rochefort 8", "Rochefort", "1955", "9.2% ABV, green cap; regular from about 1960")], dt="bottle 33 cl · vintage"),
   X("St. Bernardus Abt 12", "10% ABV abt from the Watou brewery that brewed under licence for Westvleteren until 1992.", "St. Bernardus", "", W + "St._Bernardus_Brewery"),
   X("La Trappe Quadrupel", "The beer that named the quadrupel: stronger and darker than Koningshoeven's tripel.", "La Trappe", "", TB),
  ],
  "m": [["Achel Extra Bruin", "Achel"], ["Zundert 10", "Zundert"], ["Gouden Carolus Grand Cru of the Emperor", "Gouden Carolus"], ["The Sixth Glass", "Boulevard"]]},
 {"n": "Belgian golden strong ale", "a": "Golden strong ale · Duvel-type ale", "d": "Very pale, highly attenuated, strong Belgian ale, fruity and hoppy, dry and lively; about 7.5–10.5% ABV.",
  "s": "https://styles.bjcp.org/bjcp-2021-beer/25/25c-belgian-golden-strong-ale",
  "x": [
   X("Duvel", "The originator: Moortgat's 8.5% ABV golden strong ale, first sold as Victory Ale after the First World War.", "Duvel Moortgat", "1920s (name)", W + "Duvel_Moortgat_Brewery",
     [("Victory Ale", "Duvel Moortgat", "", "original name"), ("Duvel Tripel Hop", "Duvel Moortgat", "2007", "9.5% ABV; new hop each edition 2010–2016"),
      ("Duvel Tripel Hop Citra", "Duvel Moortgat", "2016", "permanent after a public vote"), ("Duvel Single Fermented Belgian Golden Ale", "Duvel Moortgat", "2018", "6.8% ABV")],
     dt="bottle 33 cl or 75 cl · draught · tulip glass"),
  ],
  "m": [["Delirium Tremens", ""], ["Brigand", ""], ["Lucifer", ""], ["Judas", ""], ["Damnation", "Russian River"]]},
 {"n": "Belgian blond ale", "a": "Abbey blond · Blonde", "d": "Moderately strong golden Belgian ale with subtle citrus-spice yeast character and a soft, dry finish; about 6–7.5% ABV.",
  "t": ["Trappist", "Abbey (licensed)", "Secular"], "s": B25,
  "x": [
   X("Leffe Blond", "The beer that popularised the post-war abbey blond, from the Leffe brand launched in 1952 and now brewed at Leuven.", "Leffe", "post-1952", B25, a="Leffe Blonde"),
  ],
  "m": [["Affligem Blond", "Affligem"], ["Grimbergen Blond", "Grimbergen"], ["La Trappe Blond", "La Trappe"], ["Corsendonk Blond", "Corsendonk"],
        ["Val-Dieu Blond", "Val-Dieu"], ["Maredsous Blonde", "Duvel Moortgat"], ["Achel 8 Blond", "Achel"]]},
 {"n": "Belgian single", "a": "Patersbier · Trappist single · Enkel · Table beer", "d": "Pale, bitter, very dry monastic table beer with forward Belgian yeast character; about 4.8–6% ABV.",
  "s": B26,
  "x": [
   X("Westvleteren Blond", "Pale 5.8% ABV ale, green cap, that set the modern bitter single style.", "Westvleteren", "1999", W + "Westvleteren_Brewery"),
   X("Westmalle Extra", "5% ABV beer, blue label, with limited availability.", "Westmalle", "", W + "Westmalle_Brewery", a="Westmalle Enkel"),
   X("Chimay Dorée", "4.8% ABV patersbier meant mainly for the abbey; sold at the Auberge de Poteaupré from 2007.", "Chimay", "", W + "Chimay_Brewery", a="Chimay Gold"),
  ],
  "m": [["La Trappe Puur", "La Trappe"], ["St. Bernardus Extra 4", "St. Bernardus"], ["Achel 5", "Achel"], ["Redemption", "Russian River"]]},
 {"n": "Saison", "a": "Farmhouse ale · Wallonian provision ale", "d": "Highly attenuated, dry, highly carbonated Walloon farmhouse ale, fruity, spicy and fairly bitter.",
  "t": ["Table (3.5–5%)", "Standard (5–7%)", "Super (7–9.5%)", "Spiced", "Grisette"], "s": W + "Saison",
  "x": [
   X("Saison Dupont", "The archetype of the modern saison; 6.5% ABV, from a Tourpes farm brewery; its yeast is widely used by US brewers.", "Brasserie Dupont", "1920s", W + "Brasserie_Dupont",
     [("Saison Vieille Provision", "Brasserie Dupont", "", "original title"), ("Foret Saison", "Brasserie Dupont", "", "5.5% ABV, organic ingredients")], a="Saison Vieille Provision", dt="bottle 33 cl or 75 cl, corked"),
  ],
  "m": [["Saison 1900", "Lefebvre"], ["Saison 2000", "Ellezelloise"], ["Saison de Pipaix", ""], ["Saison Voisin", ""], ["Tank 7 Farmhouse Ale", "Boulevard"]]},
 {"n": "Bière de garde", "a": "Keeping beer · French farmhouse ale", "d": "Strong golden or copper 'keeping beer' of French Flanders, matured before drinking; usually top-fermented and unfiltered.",
  "t": ["Golden", "Amber", "Top-fermented, unfiltered", "Bottom-fermented, filtered"], "s": W + "Bi%C3%A8re_de_Garde",
  "x": [
   X("Jenlain Ambrée", "Amber bière de garde from Jenlain in the Nord, the brand that carried the style.", "Brasserie Duyck", "1922", W + "Jenlain_(beer)",
     [("Jenlain Blonde", "Brasserie Duyck", "", ""), ("Jenlain Fraîche", "Brasserie Duyck", "", ""), ("Jenlain bière de Printemps", "Brasserie Duyck", "", "spring beer")], dt="75 cl corked bottle · 25 cl"),
  ],
  "m": [["Trois Monts", "Brasserie de Saint-Sylvestre"], ["Ch'Ti", "Brasserie Castelain"], ["La Choulette Ambrée", "Brasserie La Choulette"]]},
]

def BR(n, c, f, seg, d, lines, sig, s, eras=(), rel=()):
    return {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": list(lines), "eras": list(eras), "sig": list(sig), "sc": [], "rel": list(rel), "s": s}

T = ["Westmalle", "Westvleteren", "Chimay", "Rochefort", "Orval", "La Trappe", "Achel"]
brands = [
 BR("Westmalle", "Belgium", "1836", "Trappist brewery (ATP)", "Brewery of Westmalle Abbey, Malle, Antwerp; originator of the dubbel and tripel.", ["Dubbel", "Tripel", "Extra"], ["Westmalle Dubbel", "Westmalle Tripel", "Westmalle Extra"], W + "Westmalle_Brewery", rel=[t for t in T if t != "Westmalle"]),
 BR("Westvleteren", "Belgium", "1838", "Trappist brewery (ATP)", "Small brewery of St Sixtus Abbey, Vleteren; sells only by reservation at the abbey.", ["Blond", "8", "12"], ["Westvleteren 12", "Westvleteren 8", "Westvleteren Blond"], W + "Westvleteren_Brewery", rel=["St. Bernardus"]),
 BR("Chimay", "Belgium", "1862", "Trappist brewery (ATP)", "Brewery of Scourmont Abbey, Chimay, Hainaut; also makes cheese.", ["Red (Première)", "Blue (Grande Réserve)", "Triple (Cinq Cents)", "150", "Dorée"], ["Chimay Blue", "Chimay Red", "Chimay Triple", "Chimay Dorée"], W + "Chimay_Brewery"),
 BR("Rochefort", "Belgium", "1899", "Trappist brewery (ATP)", "Brewery of Rochefort Abbey, Namur; brewing recorded from 1595, re-established 1899.", ["6", "8", "10", "Triple Extra"], ["Rochefort 10", "Rochefort 6"], W + "Rochefort_Brewery"),
 BR("Orval", "Belgium", "1931", "Trappist brewery (ATP)", "Brewery inside Orval Abbey, Gaume; its single dry-hopped beer is fermented with Brettanomyces.", ["Orval", "Orval Vert (Petit Orval)"], [], W + "Orval_Brewery"),
 BR("La Trappe", "Netherlands", "1884", "Trappist brewery (ATP)", "Brewery of De Koningshoeven Abbey, which named the quadrupel.", ["Blond", "Dubbel", "Tripel", "Quadrupel", "Bockbier", "Puur"], ["La Trappe Quadrupel", "La Trappe Tripel"], TB, rel=["Westmalle"]),
 BR("Achel", "Belgium", "1850", "Former Trappist brewery", "Brewery of St Benedict's Abbey, Achel; lost Authentic Trappist Product recognition.", ["5", "8 Blond", "8 Bruin", "Extra Bruin"], [], TB),
 BR("Zundert", "Netherlands", "2013", "Former Trappist brewery", "Brewery of Abdij Maria Toevlucht; ATP-recognised, closed 2025.", ["10"], [], TB),
 BR("Tre Fontane", "Italy", "2015", "Trappist brewery (ATP)", "Brewery of Tre Fontane Abbey, Rome.", [], [], TB),
 BR("Tynt Meadow", "United Kingdom", "2018", "Trappist brewery (ATP)", "Brewery of Mount St Bernard Abbey, England; one 7.4% ABV beer.", ["Tynt Meadow"], [], TB),
 BR("Engelszell", "Austria", "2012", "Former Trappist brewery", "Brewery of Engelszell Abbey, first ATP addition outside the original abbeys; closed 2023.", [], [], TB),
 BR("Spencer", "United States", "2013", "Former Trappist brewery", "Brewery of St Joseph's Abbey, Spencer, Massachusetts; closed 2022.", [], [], TB),
 BR("St. Bernardus", "Belgium", "1946", "Abbey-style brewery", "Watou brewery that brewed Westvleteren's recipes under licence until 1992.", ["Abt 12", "Prior 8", "Pater 6", "Tripel", "Witbier"], ["St. Bernardus Abt 12"], W + "St._Bernardus_Brewery", rel=["Westvleteren"]),
 BR("Duvel Moortgat", "Belgium", "1871", "Family brewing group", "Breendonk brewery founded by Jan-Leonard Moortgat; maker of Duvel and owner of several breweries.", ["Duvel", "Maredsous", "Vedett", "Liefmans"], ["Duvel"], W + "Duvel_Moortgat_Brewery", rel=["Brasserie d'Achouffe", "De Koninck", "Boulevard", "Firestone Walker"]),
 BR("Leffe", "Belgium", "1952", "Abbey beer brand (AB InBev)", "Abbey beer brand of Notre-Dame de Leffe, brewed by AB InBev at the Stella Artois brewery in Leuven.", [], ["Leffe Blond"], W + "Leffe"),
 BR("Brasserie Dupont", "Belgium", "1950", "Farmhouse brewery", "Farm brewery at Tourpes, Hainaut, known for Saison Dupont.", ["Saison Dupont", "Moinette", "Avec Les Bons Vœux", "Foret"], ["Saison Dupont"], W + "Brasserie_Dupont"),
 BR("Brasserie Duyck", "France", "", "Family brewery", "Brewery at Jenlain, Nord, maker of the Jenlain range.", ["Jenlain"], ["Jenlain Ambrée"], W + "Jenlain_(beer)"),
 BR("Slaghmuylder", "Belgium", "", "Brewery", "Belgian brewery that makes Witkap Tripel, Hendrik Verlinden's early golden strong ale.", ["Witkap"], ["Witkap Tripel"], W + "Tripel"),
]

trads = [{"n": "Authentic Trappist Product", "g": "Food & drink", "r": "Belgium, Netherlands, Italy, England (formerly Austria, United States)", "p": "Monastic brewing since 1836 (Westmalle); ITA label from 1997",
  "d": "Label of the International Trappist Association for beers and goods made at Trappist abbeys under monastic supervision.",
  "tech": "Brewed within the immediate surroundings of the abbey under the supervision of monks or nuns; profits go to the community and charity",
  "mat": "Barley malt, hops, sugar, abbey yeast strains",
  "forms": ["Dubbel", "Tripel", "Belgian dark strong ale", "Belgian single"],
  "ctr": ["Westmalle", "Westvleteren", "Chimay", "Rochefort", "Orval", "La Trappe (Koningshoeven)", "Tre Fontane", "Tynt Meadow (Mount St Bernard)"],
  "auth": "Hexagonal 'Authentic Trappist Product' logo on the label; 'abbey beer' or licensed brands such as Leffe or St. Bernardus are not Trappist.",
  "s": TB}]

notes = ("All kinds new (no old data). Added one unplanned kind, Belgian single (BJCP 26A), since Westvleteren Blond, Westmalle Extra and Chimay Dorée had no other home. "
         "Orval is in the brand register but has no archetype: its Brett-fermented pale ale fits none of these styles. "
         "Left out: Grisette and Belgian pale ale (not planned; grisette kept as a Saison type); Delirium Tremens, Brigand, Lucifer, Judas, Saison de Pipaix and Saison Voisin kept in m without makers because no retrieved page named them; "
         "Leffe Brune/Tripel/Ruby not confirmed by the Leffe page, so omitted; Chimay 150 omitted (blonde 10%, style unclear); no ABVs or years beyond the cited pages. "
         "Westmalle Tripel year given as '1930s' because sources differ (1931 BJCP, 1933 Superbier, 1934 brewery page). Brasserie Duyck and Slaghmuylder founding years not retrieved, left blank.")

out = {"kinds": kinds, "brands": brands, "traditions": trads, "notes": notes}
p = 'work/J7/shelves/04_05.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('written', len(kinds), 'kinds', sum(len(k['x']) for k in kinds), 'archetypes', len(brands), 'brands')
