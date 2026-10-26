import json, os
P='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/02_02.json'
ROSE='https://en.wikipedia.org/wiki/Ros%C3%A9'; PROV='https://en.wikipedia.org/wiki/Provence_wine'
ESC='https://en.wikipedia.org/wiki/Ch%C3%A2teau_d%27Esclans'
GRAV='https://www.winespectator.com/articles/the-wizard-of-oslavia-winemaker-josko-gravner'
RAD='https://www.winespectator.com/articles/robert-camuto-radikon-friuli-wine'
UN='https://ich.unesco.org/en/RL/ancient-georgian-traditional-qvevri-wine-making-method-00870'
def v(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
rose={"n":"Rosé","a":"Rosado · Rosato · Blush · Pink wine",
 "d":"Still pink wine of any grape, made with brief skin contact, by saignée or by the methods the rosé class allows.",
 "t":["Dry","Off-dry and sweet (blush)","Direct-press","Saignée","Blended (where allowed)"],
 "s":"https://www.wine.com/list/wine/rose-wine/7155-126",
 "x":[
  {"n":"Côtes de Provence rosé","a":"Provence rosé · Cru Classé de Provence","d":"Pale dry rosé of Grenache, Cinsault, Mourvèdre, Tibouren and Carignan; about 80% of the appellation's output.","mk":"","y":"1955 (Cru Classé list)","s":PROV,
   "v":[v("Château Minuty","Château Minuty","","Gassin; one of the 18 Crus Classés"),
        v("Château de l'Aumérade Marie-Christine Cru Classé","Château de l'Aumérade","","Cru Classé estate"),
        v("Domaine de la Croix Irrésistible Cru Classé","Domaine de la Croix","","Cru Classé estate"),
        v("Queen Côtes de Provence Rosé","Les Caves du Commandeur","","")],
   "dt":"estate or négociant · Cru Classé or not · grape blend · vintage · bottle size"},
  {"n":"Château d'Esclans rosé","a":"Whispering Angel","d":"Côtes de Provence estate whose ladder from Whispering Angel to Garrus made premium pale rosé a global category.","mk":"Château d'Esclans","y":"2005","s":ESC,
   "v":[v("Whispering Angel","Château d'Esclans","","entry cuvée"),v("Rock Angel","Château d'Esclans","","premium cuvée"),
        v("Les Clans","Château d'Esclans","","estate-grown"),v("Garrus","Château d'Esclans","","estate-grown; among the most expensive rosés"),
        v("The Pale","Château d'Esclans","","lesser wine")],
   "dt":"cuvée tier · vintage · bottle size (to magnum and larger)"},
  {"n":"Tavel","a":"Tavel AOC","d":"Rhône appellation that makes only rosé, fuller and darker than Provence, from Grenache and Cinsault.","mk":"","y":"1936","s":"https://en.wikipedia.org/wiki/Tavel_AOC",
   "v":[],"dt":"producer · Grenache share · vintage"},
  {"n":"Bandol rosé","a":"","d":"Spicy, earthy Provence rosé in which Mourvèdre must make up at least half the blend.","mk":"","y":"","s":PROV,
   "v":[],"dt":"producer · Mourvèdre share · vintage"},
  {"n":"Spanish rosado","a":"Navarra rosado","d":"Spanish rosé, most noted from Navarra, where it is mostly made from Garnacha.","mk":"","y":"","s":ROSE,
   "v":[],"dt":"region (Navarra, Rioja…) · Garnacha or Tempranillo · vintage"},
  {"n":"White Zinfandel","a":"Blush · White Zin","d":"Sweet pale-pink Californian Zinfandel created at Sutter Home from a stuck fermentation of drawn-off juice.","mk":"Sutter Home","y":"1975","s":"https://en.wikipedia.org/wiki/White_Zinfandel",
   "v":[v("Sutter Home White Zinfandel","Sutter Home","1975","originator; category leader")],"dt":"bottle size (187 ml to 1.5 l) · sweetness"},
  {"n":"Mateus Rosé","a":"Mateus","d":"Portuguese medium-sweet, lightly sparkling rosé in a flask-shaped bottle; reformulated as still and dry in the 2010s.","mk":"Sogrape","y":"1942","s":"https://en.wikipedia.org/wiki/Mateus_Rose",
   "v":[],"dt":"style (original frizzante, dry still) · closure"},
  {"n":"Lancers","a":"","d":"Portuguese rosé first sold in a stone crock, now made by the continuous method in steel tanks.","mk":"José Maria da Fonseca","y":"1944","s":ROSE,
   "v":[],"dt":"bottle (crock or glass)"}],
 "m":[["Hampton Water Rosé","Hampton Water"],["Artesans Les Secrets Rosé","Artesans"],["Lunae Mea Rosa","Lunae"],["Pierre-Yves Colin-Morey Rosé de Pinot Noir","Pierre-Yves Colin-Morey"]]}
orange={"n":"Orange wine","a":"Amber wine · Skin-contact white · Skin-fermented white",
 "d":"Still white-grape wine fermented on its skins for days to months, as a red wine is.",
 "t":["Clay vessel (qvevri, amphora)","Wood or steel","Short maceration (days)","Long maceration (months)"],
 "s":"https://www.wine.com/list/wine/7155",
 "x":[
  {"n":"Georgian qvevri amber wine","a":"Kvevri wine · Amber wine","d":"White grapes fermented with skins, stalks and pips in buried egg-shaped clay qvevri for about five to six months.","mk":"","y":"ancient; UNESCO 2013","s":UN,
   "v":[v("Kakhetian method","","","whole pomace with stems; about six months on skins"),v("Imeretian method","","","about a third of the pomace; 15–30 days")],
   "dt":"region (Kakheti, Imereti) · grape · maceration length · producer"},
  {"n":"Gravner amphora Ribolla","a":"Gravner Ribolla","d":"Oslavia (Collio) Ribolla Gialla fermented on its skins in Georgian qvevri buried in the cellar since the 2001 vintage.","mk":"Gravner","y":"2001","s":GRAV,
   "v":[v("Ribolla","Gravner","2001","whites in qvevri from 2001")],"dt":"vintage · long cellar ageing before release"},
  {"n":"Radikon skin-contact whites","a":"Radikon","d":"Oslavia whites macerated on their skins from 1995, later for up to four months, mostly without added sulphur.","mk":"Radikon","y":"1995","s":RAD,
   "v":[v("Ribolla Gialla","Radikon","1995","first skin-macerated vintage"),v("Jakot","Radikon","","Friulano"),v("Oslavje","Radikon","","blend incl. Chardonnay and Sauvignon Blanc")],
   "dt":"variety or blend · vintage · maceration length"}],
 "m":[["Vinakoper Capris Orange Rumeni Muškat","Vinakoper"]]}
brands=[
 {"n":"Château d'Esclans","c":"France","f":"","seg":"Provence rosé estate","d":"Côtes de Provence estate bought by Sacha Lichine in 2005; LVMH took a majority stake in 2019.","lines":["Whispering Angel","Rock Angel","Les Clans","Garrus","The Pale"],"eras":["Sacha Lichine, from 2005","LVMH majority, from 2019"],"sig":["Château d'Esclans rosé"],"sc":[],"rel":[],"s":ESC},
 {"n":"Sutter Home","c":"United States","f":"","seg":"Mass-market California wine","d":"Napa Valley winery whose winemaker Bob Trinchero created White Zinfandel; leads the category.","lines":[],"eras":[],"sig":["White Zinfandel"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/White_Zinfandel"},
 {"n":"Sogrape","c":"Portugal","f":"","seg":"Wine group","d":"Portugal's largest winemaker, owner of the Mateus brand.","lines":["Mateus"],"eras":[],"sig":["Mateus Rosé"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Mateus_Rose"},
 {"n":"José Maria da Fonseca","c":"Portugal","f":"","seg":"Wine producer","d":"Portuguese wine house that released Lancers rosé in 1944.","lines":["Lancers"],"eras":[],"sig":["Lancers"],"sc":[],"rel":[],"s":ROSE},
 {"n":"Gravner","c":"Italy","f":"","seg":"Natural / orange wine producer","d":"Josko Gravner's Oslavia estate, fermenting whites in buried qvevri since 2001.","lines":["Ribolla"],"eras":["Josko Gravner"],"sig":["Gravner amphora Ribolla"],"sc":[],"rel":["Radikon"],"s":GRAV},
 {"n":"Radikon","c":"Italy","f":"","seg":"Natural / orange wine producer","d":"Oslavia family estate where Stanko Radikon pioneered skin-contact whites; run by his son Saša since 2016.","lines":["Ribolla Gialla","Jakot","Oslavje"],"eras":["Stanko Radikon, to 2016","Saša Radikon, from 2016"],"sig":["Radikon skin-contact whites"],"sc":[],"rel":["Gravner"],"s":RAD}]
trad=[{"n":"Georgian qvevri winemaking","g":"Food & drink","r":"Georgia (Kakheti, Imereti, Guria)","p":"Ancient to present; UNESCO ICH 2013",
 "d":"Fermenting and ageing wine with skins, stalks and pips in egg-shaped clay qvevri sealed and buried in the ground.",
 "tech":"Pressed grapes and pomace sealed in a buried qvevri for five to six months; vessels lime-washed and re-lined with beeswax",
 "mat":"Clay, beeswax, lime, grapes with skins, stalks and pips",
 "forms":["Orange wine","Georgian qvevri amber wine"],
 "ctr":["Vardisubani (Kakheti)","Makatubani, Shrosha, Tq'emlovana, Chkhiroula (Imereti)","Atsana (Guria)"],
 "auth":"Fermented and aged in qvevri (not steel or barrel), with whole-pomace contact; listed by Georgian region and grape.","s":UN}]
out={"kinds":[rose,orange],"brands":brands,"traditions":trad,
 "notes":"Kept both old kinds (k50 Rosé, k56 Orange wine). Old models re-homed: Les Clans and Cru Classé wines became versions; four others kept in m. Not added: Domaine Tempier and Bandol producers, Tavel producers and Navarra producers (no retrieved page named them); Whispering Angel launch year (not on fetched page). Bandol_AOC Wikipedia URL served the Provence page, so Bandol is cited to Provence_wine. Sutter Home and José Maria da Fonseca founding years left blank (not confirmed)."}
tmp=P+'.tmp'; json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
