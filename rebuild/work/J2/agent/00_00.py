import json,os
K=[
{"n":"Atlantic salmon","a":"Salmo salar · farmed salmon · Lachs","d":"Whole fish or cuts of the salmon Salmo salar sold raw, mostly farmed, occasionally wild.",
 "t":["farmed","wild","whole","fillet","portion","fresh","frozen"],
 "s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/frozen-fish",
 "x":[
 {"n":"Scottish salmon PGI","a":"Scottish Farmed Salmon PGI","d":"Farmed salmon from the coast of mainland Scotland, Western Isles, Orkney and Shetland; the EU dropped 'farmed' from the name in 2025.","mk":"","y":"","s":"https://www.salmonbusiness.com/scottish-salmon-gains-updated-pgi-as-bloc-drops-farmed-from-label/?amp=1",
  "v":[{"n":"Scottish Farmed Salmon PGI","mk":"","y":"","d":"earlier registered name, replaced by 'Scottish salmon'"}],"dt":"farmed, packaging must say farm-raised"},
 {"n":"Label Rouge Scottish salmon","a":"","d":"Scottish salmon carrying the French Label Rouge quality mark, about a third of Scottish exports to France.","mk":"","y":"","s":"https://www.fishfarmingexpert.com/european-commission-label-rouge-protected-geographical-indication/eu-drops-farmed-from-protected-label-for-scottish-salmon/2028543","dt":"farmed · sold mainly in France"},
 {"n":"Loch Duart salmon","a":"","d":"Low-density, fallowed farmed salmon from Sutherland and the Outer Hebrides, exported mainly to France.","mk":"Loch Duart","y":"1999","s":"https://en.wikipedia.org/wiki/Loch_Duart","dt":"farmed · eight sea sites · fallow 5 to 12 months"},
 {"n":"Clare Island Salmon PGI","a":"","d":"Atlantic salmon associated with Clare Island, County Mayo, Ireland; EU PGI since 1999.","mk":"","y":"1999","s":"https://en.wikipedia.org/wiki/Clare_Island_Salmon","dt":"farmed, exposed Atlantic site"},
 {"n":"Faroe Islands salmon","a":"","d":"Farmed salmon from Faroese fjords; Bakkafrost is the largest Faroese farmer.","mk":"Bakkafrost","y":"1979","s":"https://en.wikipedia.org/wiki/Bakkafrost","dt":"farmed · Bakkafrost began salmon in 1979"},
 {"n":"West Wales Coracle Caught Salmon PGI","a":"","d":"Salmon taken by coracle netsmen on the Teifi, Taf and Towy; PGI awarded February 2017.","mk":"","y":"2017","s":"https://www.coraclesociety.org.uk/news/21-02-2017/west-wales-coracle-caught-salmon-awarded-eu-protected-status","dt":"wild · hand-made coracle nets"}
 ]},
{"n":"Pacific salmon","a":"Oncorhynchus · sockeye · king · chinook · coho · silver · keta · chum · pink · humpback","d":"Raw wild or farmed Pacific salmon: sockeye, king (chinook), coho, keta (chum) and pink.",
 "t":["sockeye (red)","king (chinook)","coho (silver)","keta (chum)","pink (humpback)","wild","farmed coho","whole","fillet","portion","fresh","frozen"],
 "s":"https://www.vitalchoice.com/v/wild-salmon",
 "x":[
 {"n":"Copper River salmon","a":"","d":"Wild king, sockeye and coho from the Copper River, Alaska, landed from mid-May and flown fresh from Cordova.","mk":"","y":"","s":"https://news.alaskaair.com/alaska-airlines/cordova-copper-river-salmon/","dt":"wild · king, sockeye, coho · gillnet, bled and iced"},
 {"n":"みやぎサーモン","a":"Miyagi Salmon","d":"Farmed coho salmon from Miyagi Prefecture, ikejime-killed for freshness and eaten raw; Japanese GI no. 31, registered 26 May 2017.","mk":"","y":"2017","s":"https://www.maff.go.jp/j/shokusan/gi_act/register/0031/index.html","dt":"farmed coho · ikejime · sashimi grade"}
 ]},
{"n":"Trout & char","a":"rainbow trout · brown trout · sea trout · sewin · steelhead · Arctic char · Saibling · Forelle","d":"Raw rainbow, brown and sea trout and Arctic char, sold whole or as fillets.",
 "t":["rainbow trout","brown trout","sea trout (sewin)","steelhead","Arctic char (Saibling)","wild","farmed","whole","fillet"],
 "s":"https://www.thefishsociety.co.uk/",
 "x":[
 {"n":"Trote del Trentino PGI","a":"Trentino trout · Salmerino del Trentino","d":"Rainbow trout (Oncorhynchus mykiss) bred in the Autonomous Province of Trento and Bagolino; registered by the EU in 2013, Trentino char marketed alongside.","mk":"","y":"2013","s":"https://www.legislation.gov.uk/eur/2013/910/data.xht","dt":"rainbow trout · about two years' rearing · Trentino char sold under the same IGP marking"},
 {"n":"West Wales Coracle Caught Sewin PGI","a":"","d":"Sea trout (sewin) caught by coracle netsmen on the Tywi, Taf and Teifi; PGI granted March 2017.","mk":"","y":"2017","s":"https://www.coraclesociety.org.uk/news/01-04-2017/west-wales-coracle-caught-sewin-awarded-protected-status","dt":"wild · five-month season from 1 March or 1 April · no weekend fishing"}
 ],
 "m":[["Szilvásváradi pisztráng PGI",""]]}
]
B=[
{"n":"Loch Duart","c":"United Kingdom","f":"1999","seg":"Artisan & independent","kf":"low-density salmon","d":"Independent salmon farmer at Scourie, Sutherland, with sites in Sutherland and the Outer Hebrides.","lines":["Loch Duart salmon"],"eras":[],"sig":["Loch Duart salmon"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Loch_Duart"},
{"n":"Bakkafrost","c":"Faroe Islands","f":"1968","seg":"Mainstream","kf":"Faroese salmon","d":"Faroese salmon farmer at Glyvrar, Eysturoy; moved from herring to salmon in 1979.","lines":["Faroe Islands salmon"],"eras":[],"sig":["Faroe Islands salmon"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Bakkafrost"}]
out={"kinds":K,"brands":B,"traditions":[],"notes":"Merged 9 old kinds into 3 planned kinds; the four PGI/GI names for Atlantic salmon and the Miyagi and Coracle Sewin names became archetypes (no longer flat models). Szilvasvaradi trout kept as flat model (no retrievable page). Salmerino del Trentino: the EU regulation names only Trote del Trentino, so char is noted inside that archetype. Scottish Wild Salmon PGI left out: wild Scottish salmon is no longer commercially sold (per Fish Farming Expert) and no readable register page was retrieved. Species defined by types, not new kinds."}
p='work/J2/shelves/00_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
