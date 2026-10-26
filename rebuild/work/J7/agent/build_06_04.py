import json, os
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":x[0],"mk":x[1],"y":x[2],"d":x[3]} for x in v],"dt":dt}
kinds=[
 {"n":"Pastis","a":"pastis de Marseille","d":"French anise and liquorice apéritif spirit, at least 40% ABV (pastis de Marseille 45%), drunk diluted with water.",
  "t":["Pastis de Marseille (45%)","Standard pastis (40%)","Artisanal / multi-herb pastis","Organic"],
  "s":"https://farehamwinecellar.co.uk/product-category/spirit/pastis-anise/",
  "x":[A("Ricard","Ricard Pastis · le vrai pastis de Marseille","The original commercial pastis, launched in Marseille by Paul Ricard; the reference pastis de Marseille.","Ricard","1932",W+"Ricard_(liqueur)",
         [["Ricard Pastis 45%","Ricard","1932","pastis de Marseille"],["Ricard Bio Amande","Ricard","",""]],"strength 45% · bottle size"),
       A("Pernod","Pernod Anise · liqueur d'anis","Anise spirit made by Pernod after the First World War as the successor to its absinthe; 45% ABV.","Pernod","after 1918",W+"Pernod_(brand)",
         [["Pernod Anise 45%","Pernod","",""]],"strength · bottle size"),
       A("Pastis 51","51","Mass-market pastis de Marseille launched by Pernod in 1951, now a Pernod Ricard brand.","Pernod Ricard","1951",W+"Pernod_Ricard",[],"strength · bottle size"),
       A("Henri Bardouin","Pastis Henri Bardouin","High-end Provençal pastis from Forcalquier with more than 65 herbs and spices; 45% ABV.","Distilleries et Domaines de Provence","",W+"Pastis_Henri_Bardouin",[],"strength 45% · bottle size")],
  "m":[["Brana Pastis Basque","Brana"],["Distillerie de la Seine 777 Pastis Artisanal",""],["Genestine Pastis Sauvage",""],["Le Vadrouilleur Anista Pastis",""],["Manguin Pastis",""],["Vermeil Pastis",""],["Pacific","Pernod Ricard"]]},
 {"n":"Ouzo","a":"","d":"Greek and Cypriot anise spirit, protected as a geographical indication since 2006.",
  "t":["Double-distilled","100% distilled","Lesvos ouzo","Cyprus ouzo"],
  "s":"https://www.danmurphys.com.au/spirits/ouzo",
  "x":[A("Ouzo Tyrnavou","Tyrnavos ouzo","Ouzo from the first ouzo distillery, founded in Tyrnavos in 1856 by Nikolaos Katsaros.","Ouzo Tyrnavou","1856",W+"Ouzo",[],"strength · bottle size"),
       A("Ouzo 12","","Named after the house blend in cask number twelve; first made by the Kaloyannis brothers in Constantinople and the best-known export ouzo.","Ouzo 12","1880","https://www.diffordsguide.com/beer-wine-spirits/40/ouzo-12",
         [["Ouzo 12 38%","Ouzo 12","","owned by Gruppo Campari since 1999"]],"strength 38% · bottle size"),
       A("Ouzo of Plomari","Ouzo Plomari · Isidoros Arvanitis","Lesvos ouzo from the island's best-known distilling town, founded by Isidoros Arvanitis.","Ouzo Plomari","1894",W+"Ouzo_Plomari",[],"strength · bottle size")]},
 {"n":"Arak & rakı","a":"arak · araq · rakı · raki","d":"Grape-based anise spirits of Turkey and the Levant, distilled twice or three times and drunk with water and food; absinthe, ouzo and pastis have their own entries.",
  "t":["Fresh-grape rakı (yaş üzüm)","Raisin rakı","Gum rakı (sakız)","Fig rakı (incir)","Lebanese arak","Syrian arak","Israeli arak","Palestinian arak","Amphora-aged"],
  "s":"https://www.whisky.fr/en/selections/anises.html",
  "x":[A("Yeni Rakı","","The largest rakı brand, made from raisins at 45% ABV; created by the state monopoly Tekel, now made by Diageo's Mey İçki.","Mey İçki","",W+"Rak%C4%B1",[["Yeni Rakı 45%","Mey İçki","","raisin suma"]],"strength 45% · bottle size"),
       A("Tekirdağ Rakısı","","Grape rakı from the Tekirdağ region at 45% ABV, its flavour credited to artesian water at Çorlu.","Mey İçki","",W+"Rak%C4%B1",[["Tekirdağ Altın Seri","Mey İçki","",""]],"strength · bottle size"),
       A("Efe Yaş Üzüm Rakısı","Efe fresh-grape rakı","The first rakı made exclusively from fresh-grape suma.","Efe","",W+"Rak%C4%B1",[],"strength · bottle size"),
       A("Lebanese arak","arak baladi · Zahlé arak","Bekaa Valley arak from grapes and aniseed, triple distilled and aged in clay amphorae, typically about 53% ABV.","", "",W+"Arak_(drink)",
         [["Ksarak","Château Ksara","",""],["Arak Massaya","Massaya","","triple distilled, aged 18 months"],["Domaine des Tourelles Arak Brun","Domaine des Tourelles","",""],["Zoumot Arak Al-Bustan","Zoumot","",""],["Arak Zahlawi","","","Zahlé"]],"strength 50–53% · ageing in amphorae · bottle size")],
  "m":[["Altınbaş","Mey İçki"],["Kulüp Rakısı","Mey İçki"],["Elite Arak","Joseph Gold & Sons"],["Arak Kawar","Kawar Distillery"],["Arak Muaddi",""]]},
 {"n":"Absinthe","a":"verte · blanche · la bleue · absinthe supérieure","d":"Spirit flavoured with grand wormwood, green anise and fennel, sold as absinthe (verte or blanche).",
  "t":["Verte (green, coloured by a second maceration)","Blanche / la bleue (clear)","Swiss (Val-de-Travers)","French (Pontarlier style)","Reproduction of a pre-ban recipe"],
  "s":"https://www.masterofmalt.com/absinthe/",
  "x":[A("Pernod Fils absinthe","Pernod absinthe","The Belle Époque reference verte from Pernod's Pontarlier distillery; the most popular absinthe until the French ban.","Pernod","1805",W+"Pernod_(brand)",
         [["Pernod Fils 68%","Pernod","19th century","pre-ban original"],["Pernod Absinthe","Pernod","2005","modern release"],["Pernod Absinthe (reformulated)","Pernod","2013","made in Thuir, closer to the original"]],"strength 68% · verte · bottle size"),
       A("Kübler La Bleue","Kübler Absinthe","Clear Swiss absinthe from Môtiers in the Val-de-Travers; first brand sold legally in Switzerland after the ban was lifted.","Kübler","1863",W+"K%C3%BCbler_Absinthe",
         [["Kübler Absinthe 53%","Kübler","2007","approved for US sale"]],"strength 53% · blanche · bottle size"),
       A("La Clandestine","","Swiss blanche said to follow a 1935 recipe by distiller Charlotte Vaucher; made by the Artemisia-Bugnon distillery.","Artemisia-Bugnon","1935 (recipe)",W+"La_Clandestine",
         [["La Clandestine Blanche","Artemisia-Bugnon","","53%"],["La Recette Marianne","Artemisia-Bugnon","2005","for French fenchone rules"],["La Clandestine Absinthe Supérieure","Artemisia-Bugnon","2008","US approval"]],"strength · blanche · bottle size"),
       A("Jade absinthes","Jade Liqueurs","Reproductions of pre-ban absinthes reconstructed by T. A. Breaux from sealed antique bottles and distilled at the Combier distillery.","Jade Liqueurs","2000","https://www.absinthe.de/en/Jade-Liqueurs",
         [["Jade Nouvelle-Orléans","Jade Liqueurs","","first of the series"],["Jade V.S. 1898","Jade Liqueurs","","second of the series"],["Jade 1901","Jade Liqueurs","",""],["Jade Esprit Edouard","Jade Liqueurs","",""],["Jade Terminus Oxygénée","Jade Liqueurs","","last of the series"]],"strength · verte · bottle size"),
       A("Lucid","Lucid Absinthe Supérieure","French absinthe that in 2007 became the first genuine absinthe approved for US import since 1912.","Lucid","2007",W+"Absinthe",[],"strength · verte · bottle size")],
  "m":[["St. George Absinthe Verte","St. George Spirits"],["La Fée Absinthe",""],["Hill's Absinth",""],["Taboo Absinthe","Okanagan Spirits"]]}]
K="knowledge"
def B(n,c,f,seg,d,lines,sig,rel,s): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":[],"sig":sig,"sc":[],"rel":rel,"s":s}
brands=[
 B("Ricard","France","1932","Pastis","Marseille pastis house founded by Paul Ricard; merged with Pernod Fils in 1975 to form Pernod Ricard.",["Ricard"],["Ricard"],["Pernod","Pernod Ricard"],W+"Ricard_(liqueur)"),
 B("Pernod","France","1805","Absinthe and anise","Pernod Fils absinthe house of Pontarlier, later maker of Pernod Anise; part of Pernod Ricard.",["Pernod Anise","Pernod Absinthe"],["Pernod Fils absinthe","Pernod"],["Ricard","Pernod Ricard"],W+"Pernod_(brand)"),
 B("Pernod Ricard","France","1975","Drinks group","Paris-based group formed by the merger of Pernod Fils and Ricard; owns Ricard, Pernod and Pastis 51.",["Ricard","Pernod","Pastis 51","Pacific"],["Pastis 51"],["Ricard","Pernod"],W+"Pernod_Ricard"),
 B("Distilleries et Domaines de Provence","France","","Pastis and Provençal spirits","Forcalquier distillery that makes Pastis Henri Bardouin.",["Henri Bardouin"],["Henri Bardouin"],[],W+"Pastis_Henri_Bardouin"),
 B("Ouzo Tyrnavou","Greece","1856","Ouzo","Brand of the first ouzo distillery, founded in Tyrnavos by Nikolaos Katsaros.",[],["Ouzo Tyrnavou"],[],W+"Ouzo"),
 B("Ouzo 12","Greece","1880","Ouzo","Ouzo first made by the Kaloyannis brothers in Constantinople; owned by Gruppo Campari since 1999.",[],["Ouzo 12"],[],"https://www.diffordsguide.com/beer-wine-spirits/40/ouzo-12"),
 B("Ouzo Plomari","Greece","1894","Ouzo","Lesvos ouzo company founded in Plomari by Isidoros Arvanitis.",[],["Ouzo of Plomari"],[],W+"Ouzo_Plomari"),
 B("Mey İçki","Turkey","","Rakı","Diageo subsidiary (acquired 2011) that took over Tekel's rakı brands; maker of Yeni Rakı, Tekirdağ, Kulüp and Altınbaş.",["Yeni Rakı","Tekirdağ Rakısı","Kulüp Rakısı","Altınbaş"],["Yeni Rakı","Tekirdağ Rakısı"],["Efe"],W+"Rak%C4%B1"),
 B("Efe","Turkey","","Rakı","Rakı producer that first made rakı exclusively from fresh-grape suma.",["Efe Yaş Üzüm Rakısı"],["Efe Yaş Üzüm Rakısı"],["Mey İçki"],W+"Rak%C4%B1"),
 B("Château Ksara","Lebanon","1857","Winery and arak","Lebanon's oldest and largest winery, founded by Jesuits near Zahlé in the Bekaa Valley; makes Ksarak.",["Ksarak"],["Lebanese arak"],["Massaya"],W+"Ch%C3%A2teau_Ksara"),
 B("Massaya","Lebanon","1998","Winery and arak","Bekaa Valley winery of the Ghosn brothers, founded partly to revive traditional triple-distilled arak.",["Arak Massaya"],["Lebanese arak"],["Château Ksara"],W+"Massaya"),
 B("Kübler","Switzerland","1863","Absinthe","Môtiers absinthe distillery founded by J. Fritz Kübler; first legal Swiss absinthe after 2005.",["Kübler Absinthe"],["Kübler La Bleue"],["Artemisia-Bugnon"],W+"K%C3%BCbler_Absinthe"),
 B("Artemisia-Bugnon","Switzerland","","Absinthe","Swiss distillery making La Clandestine absinthes.",["La Clandestine"],["La Clandestine"],["Kübler"],W+"La_Clandestine"),
 B("Jade Liqueurs","United States","2000","Absinthe","Company of T. A. Breaux making reproductions of pre-ban absinthes at the Combier distillery in France.",["Nouvelle-Orléans","V.S. 1898","1901","Esprit Edouard","Terminus Oxygénée"],["Jade absinthes"],[],"https://www.absinthe.de/en/Jade-Liqueurs"),
 B("Lucid","France","2007","Absinthe","Absinthe that was the first genuine absinthe approved for US import after the ban.",["Lucid"],["Lucid"],["Kübler"],W+"Absinthe")]
trads=[
 {"n":"Val-de-Travers and Pontarlier absinthe","g":"Food & drink","r":"Neuchâtel (Switzerland) and Doubs (France)","p":"1797–present (banned 1910–2005 in Switzerland, 1915–2011 in France)","d":"Birthplace of commercial absinthe: Dubied and Pernod at Couvet, then Pernod Fils at Pontarlier; revived at Môtiers after legalisation.","tech":"Maceration of wormwood, anise and fennel in alcohol, redistilled; verte gets a second herbal maceration for colour","mat":"Grand wormwood, green anise, fennel, wine or neutral alcohol","forms":["Absinthe verte","Absinthe blanche (la bleue)"],"ctr":["Couvet","Môtiers","Pontarlier","Maison de l'Absinthe (Môtiers)"],"auth":"Swiss court ruled in 2014 that 'absinthe' is a product name, not a protected origin; look for named Val-de-Travers or Pontarlier distilleries.","s":W+"Absinthe"},
 {"n":"Levantine arak","g":"Food & drink","r":"Lebanon, Syria, Israel, Palestine","p":"Traditional, ongoing","d":"Grape-and-aniseed spirit of the Levant, centred on Zahlé and the Bekaa Valley.","tech":"Grapes fermented about three weeks, distilled, redistilled with aniseed, then a slow third distillation; aged in clay amphorae","mat":"Grapes or pomace, aniseed","forms":["Lebanese arak"],"ctr":["Zahlé","Bekaa Valley","Ramallah"],"auth":"Quality arak is triple distilled and amphora-aged, typically about 53% ABV.","s":W+"Arak_(drink)"}]
notes=("Merged all four old kinds as planned; 'Other anise spirits' renamed Arak & rakı (its ouzo/pastis aliases dropped since those have own kinds); its 'Ricard Bio Amande' moved under the Ricard archetype. "
 "Old-data unattributed pastis models kept in m. Left out: Ouzo Plomari variants, ABVs and launch years not on retrieved pages; Ouzo 12 Gold, Barbayannis, Mini, Tsantali (not on fetched pages); Duplais and other absinthe brands not confirmed; Val-de-Travers only via Absinthe article. "
 "Ouzo minimum ABV given as 37.5% per EU rule? -- see text") 
notes=notes.replace(" Ouzo minimum ABV given as 37.5% per EU rule? -- see text","")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/06_04.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
