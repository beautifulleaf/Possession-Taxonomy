import json, os
HM="https://heidelbergmaterials.co.uk/packed-products/decorative-aggregates"
HO="https://www.holcim.co.uk/products/aggregates/decorative-aggregates"
HW="https://www.howarth-timber.co.uk/gardening-landscaping/garden-maintenance/decorative-aggregates/"
LA="https://longacres.co.uk/gardening-products/fencing-and-landscaping/decorative-stone/kelkay-golden-gravel-18-22mm-1003"
kinds=[
{"n":"Garden gravel","a":"stone chippings · decorative aggregate · decorative stone","d":"Gravel and crushed stone chippings sold in bags or bulk bags for paths, drives and borders.",
 "t":["limestone chippings","granite chippings","flint gravel","black basalt","white spar","rounded river gravel","panda gravel (black and icy blue)","dark grey Clee Hill stone","standard bag","bulk bag"],
 "s":"https://www.homebase.co.uk/garden-outdoor/fencing-decking-landscaping/decorative-stone-gravel-chippings.list",
 "x":[
  {"n":"Pea gravel","a":"","d":"Clean rounded gravel about the size of garden peas, used for walkways, drives and concrete surfaces.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Gravel","v":[],"dt":"rounded · fine sizes · mixed natural colours"},
  {"n":"Cotswold chippings","a":"Cotswold buff · Cotswold stone chippings","d":"Buff-cream limestone chippings named after Cotswold stone, the honey-coloured oolitic limestone of the Cotswolds.","mk":"","y":"","s":HO,
   "v":[{"n":"Cotswold Buff Limestone","mk":"Holcim","y":"","d":"Carboniferous limestone, buff/cream, 20 mm"},
        {"n":"Cotswold Buff chippings","mk":"Heidelberg Materials","y":"","d":"20 mm"},
        {"n":"Cotswold Chippings Buff","mk":"Suburban Stone","y":"","d":"20 mm, 20 kg bag"}],
   "dt":"angular · 10–20 mm · buff to cream · standard or bulk bag"},
  {"n":"Golden gravel","a":"golden flint","d":"Angular flint gravel in shades of gold, sand and cream.","mk":"","y":"","s":HO,
   "v":[{"n":"Golden Gravel","mk":"Holcim","y":"","d":"angular flinted gravel, 10, 20 and 40 mm"},
        {"n":"Golden Gravel Chippings","mk":"Kelkay","y":"","d":"fish friendly, 25 kg bag; listed as 10–20 mm and 18–22 mm"},
        {"n":"Solent Gold","mk":"Heidelberg Materials","y":"","d":"10–20 mm"},
        {"n":"York Gold","mk":"Heidelberg Materials","y":"","d":"10 mm"}],
   "dt":"10–40 mm · gold, brown, white, grey"},
  {"n":"Leicestershire granite chippings","a":"Leicester Pink granite · Bardon Hill granite","d":"Hard quarried granite chippings from Leicestershire, used for paths, landscaping and drives.","mk":"","y":"","s":HO,
   "v":[{"n":"Leicester Pink Granite","mk":"Holcim","y":"","d":"grey with pink specks, 10, 14, 20 mm"},
        {"n":"Bardon Hill Granite","mk":"Holcim","y":"","d":"grey with blue/purple tint, 10, 14, 20 mm"}],
   "dt":"10–20 mm · grey, pink, blue-grey; other granites: Scottish red, Cornish silver, Shropshire green"},
  {"n":"Flamingo chippings","a":"Flamingo Pink","d":"Mixed white, pink, black and pale grey chippings from Eastern Europe.","mk":"","y":"","s":HO,
   "v":[{"n":"Flamingo Chippings","mk":"Holcim","y":"","d":"20 mm"},{"n":"Flamingo Pink","mk":"Heidelberg Materials","y":"","d":"new line"}],
   "dt":"20 mm · related mixes: Ice Blue, Polar White, Black Ice"},
  {"n":"Shirakawa-suna","a":"Shirakawa sand · Japanese garden gravel","d":"Black-speckled white granite gravel from Kyoto's upper Shirakawa river, prized for holding raked patterns in dry gardens.","mk":"","y":"extraction illegal since late 1950s","s":"https://en.wikipedia.org/wiki/Japanese_rock_garden",
   "v":[{"n":"Crushed and sieved granite substitute","mk":"","y":"","d":"modern replacement; rounded grains hold raked lines poorly"}],
   "dt":"feldspar, quartz, mica · c. 9 mm grain for small gardens · raked line, wave, scroll and check patterns"}],
 "r":[["Decorative aggregates","Heidelberg Materials"],["Decorative aggregates","Holcim"],["Suburban Stone","Suburban Stone"]]},
{"n":"Slate chippings","a":"slate chips · slate mulch","d":"Crushed flat slate in bags as decorative ground cover, darker and brighter when wet.",
 "t":["plum","blue","green","20 mm","40 mm"],
 "s":"https://www.homebase.co.uk/garden-outdoor/fencing-decking-landscaping/decorative-stone-gravel-chippings.list",
 "x":[{"n":"Welsh slate chippings","a":"plum slate · blue slate · green slate","d":"Crushed Welsh slate sold by colour; pastel when dry, vivid when wet.","mk":"","y":"","s":HO,
   "v":[{"n":"Plum Slate","mk":"Holcim","y":"","d":"Wales, 20 and 40 mm"},{"n":"Blue Slate","mk":"Holcim","y":"","d":"Wales, 20 and 40 mm"},{"n":"Green Slate","mk":"Holcim","y":"","d":"Wales, 40 mm"},
        {"n":"Plum Slate chippings","mk":"Heidelberg Materials","y":"","d":"15–30 mm and 40 mm"},{"n":"Blue Slate","mk":"Heidelberg Materials","y":"","d":"15–30 mm and 40 mm"}],
   "dt":"15–40 mm · plum, blue, green"}]},
{"n":"Decorative pebbles","a":"cobbles · beach pebbles","d":"Rounded water-worn stones (pebbles 4–64 mm, cobbles 64–256 mm) in bags for borders, ponds and containers.",
 "t":["pebbles","cobbles","mixed colours","white"],
 "s":"https://www.homebase.co.uk/garden-outdoor/fencing-decking-landscaping/decorative-stone-gravel-chippings.list",
 "x":[{"n":"Scottish pebbles and cobbles","a":"Highland pebbles · Scottish cobbles","d":"Rounded Scottish stones in mixed pink, grey, brown and white.","mk":"","y":"","s":HO,
   "v":[{"n":"Scottish Cobbles","mk":"Holcim","y":"","d":"50–75 mm"},{"n":"Highland Pebbles","mk":"Holcim","y":"","d":"30 mm"},
        {"n":"Scottish Pebbles","mk":"Heidelberg Materials","y":"","d":"20–40 mm"},{"n":"Scottish Cobbles","mk":"Heidelberg Materials","y":"","d":"50 mm"}],
   "dt":"20–75 mm · pink, grey, brown, white"},
  {"n":"Flamingo pebbles","a":"","d":"Rounded white, pink, black and pale grey pebbles from Eastern Europe.","mk":"","y":"","s":HO,
   "v":[{"n":"Flamingo Pebbles","mk":"Holcim","y":"","d":"40 mm"}],"dt":"40 mm"}]},
{"n":"Rockery stone and boulders","a":"rockery stone · feature boulders · rockwork","d":"Large natural or artificial stones for rock gardens, rockeries and garden features.",
 "t":["natural granite","limestone","artificial stone"],
 "s":"https://en.wikipedia.org/wiki/Rock_garden",
 "x":[{"n":"Pulhamite","a":"Pulham rockwork","d":"Patented Victorian artificial stone resembling gritty sandstone, used to build or join garden rock features.","mk":"James Pulham and Son","y":"Victorian (James Pulham, 1820–1898)","s":"https://en.wikipedia.org/wiki/Pulhamite",
   "v":[],"dt":"sand, Portland cement and clinker over rubble and crushed-brick core · recipe lost"}],
 "m":[["Rockery Granite","Holcim"]]},
{"n":"Stepping stone","a":"stepping stones · garden stepping stone","d":"Flat stones set apart to make a path across a garden, pond or stream.",
 "s":"https://en.wikipedia.org/wiki/Stepping_stones",
 "x":[{"n":"Iso-watari","a":"","d":"Japanese garden path of stepping stones across shallow parts of a pond.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Stepping_stones","v":[],"dt":"selected natural stone"}]}]
brands=[
{"n":"Heidelberg Materials","c":"Germany","f":"1874","seg":"Building materials group","d":"Cement, aggregates, ready-mix and asphalt group; owns Hanson in the UK (now Heidelberg Materials UK), which sells packed decorative aggregates.","lines":["Packed products: decorative aggregates"],"eras":["HeidelbergCement AG until 2022"],"sig":["Cotswold chippings","Golden gravel","Welsh slate chippings"],"sc":[],"rel":["Holcim"],"s":"https://en.wikipedia.org/wiki/Heidelberg_Materials"},
{"n":"Holcim","c":"Switzerland","f":"1912","seg":"Building materials group","d":"Cement, aggregates and concrete group; entered the UK by buying Aggregate Industries in 2005 and sells decorative aggregates as Holcim UK.","lines":["Decorative aggregates"],"eras":["Holderbank to 2001","LafargeHolcim 2015–2021"],"sig":["Golden gravel","Leicestershire granite chippings","Welsh slate chippings"],"sc":[],"rel":["Heidelberg Materials"],"s":"https://en.wikipedia.org/wiki/Holcim"}]
trads=[{"n":"Karesansui (Japanese dry garden)","g":"Garden & landscape","r":"Japan (Kyoto)","p":"mid-14th century onwards","d":"Zen dry landscape of raked gravel and set stones representing water.","tech":"raking gravel (samon) into line, wave, scroll and check patterns","mat":"granite gravel (Shirakawa-suna), stones, moss","forms":["Garden gravel","Rockery stone and boulders"],"ctr":["Ryōan-ji","Daisen-in (1509–1513)","Ginkaku-ji","Saihō-ji","Tōfuku-ji (Shigemori Mirei, 1940)"],"auth":"True Shirakawa-suna has jagged-and-smooth grains that hold raked lines for weeks; crushed quarried granite holds them poorly.","s":"https://en.wikipedia.org/wiki/Japanese_rock_garden"}]
notes=("'Other garden stone' dissolved into Garden gravel types; bark chippings it mentioned are not stone and are left to the garden mulch kinds. "
 "Marble chippings not added: no retrieved page confirmed a marble product (Polar White is not called marble on Holcim's page). "
 "Kelkay kept only as a version maker: kelkay.com says its owner The AMES Companies has ceased trading, so no brand entry. "
 "Pulhamite mk 'James Pulham and Son' has no register entry (only the Pulhamite page was retrieved). Homebase and B&M old pages returned 403/no listings; old s kept.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p="work/C8/shelves/03_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
