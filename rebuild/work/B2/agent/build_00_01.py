import json, os
W="https://en.wikipedia.org/wiki/"
AN="https://anewtribe.co.uk/blogs/journal/explorations-moroccan-rug-guide"
kinds=[
{"n":"Moroccan rug","a":"Berber rug · Amazigh rug","d":"Hand-woven wool rug made by Moroccan Berber (Amazigh) weavers, in thick pile or flatweave, often with geometric motifs.",
 "t":["pile","flatweave","rag-woven","antique","vintage","new"],"s":W+"Moroccan_rugs",
 "x":[
 {"n":"Beni Ourain","a":"Beni Ouarain","d":"Thick undyed cream-white pile rug with dark lozenge and zigzag motifs, from the Beni Ourain tribal confederation.","mk":"","y":"traditional; Western vogue from the 1920s–30s","s":"https://www.moroccancorridor.com/pages/beni-ourain","v":[],"dt":"Ghiordes knot · pile c. 3–5 cm · undyed Middle Atlas wool · black/brown motifs (walnut shell, oak gall)"},
 {"n":"Azilal","a":"","d":"Single-knotted wool rug from the High Atlas with a cream ground and bright, often story-telling motifs.","mk":"","y":"traditional","s":AN,"v":[],"dt":"cream or white ground · bright plant-dyed accents · asymmetric motifs"},
 {"n":"Boujad","a":"","d":"Tightly knotted wool rug from the central plains with fine geometric patterns in warm reds, pinks and oranges.","mk":"","y":"traditional","s":AN,"v":[],"dt":"natural dyes incl. henna · red, pink, orange"},
 {"n":"Beni M'Guild","a":"Beni Mguild","d":"Plush-pile rug from the western Middle Atlas in deep blue, purple, brown and red, usable either side up.","mk":"","y":"traditional","s":AN,"v":[],"dt":"vertical loom · reversible pile/flat face"},
 {"n":"Boucherouite","a":"Boucharouette · rag rug","d":"Brightly coloured rag-woven rug made from scraps of fabric and old clothing where wool is scarce.","mk":"","y":"traditional","s":AN,"v":[],"dt":"cotton and synthetic rags · shaggy or flat"},
 {"n":"Moroccan kilim","a":"hanbel","d":"Thin pileless flatwoven Berber rug, light and portable for desert tents.","mk":"","y":"traditional","s":AN,"v":[],"dt":"flatwoven · lightweight"},
 {"n":"Rabat carpet","a":"","d":"Urban knotted carpet from Rabat with floral and diamond elements, Turkish-derived motifs and a fairly bare field.","mk":"","y":"traditional","s":W+"Moroccan_rugs","v":[],"dt":"medallion/diamond layouts · floral borders"}]},
{"n":"Aubusson & Savonnerie carpet","a":"French court carpet · Savonnerie · Aubusson","d":"French carpet in the court tradition: knotted-pile Savonnerie or flat-woven Aubusson tapestry carpet, with reproductions.",
 "t":["knotted pile","tapestry-woven (flatweave)","antique","reproduction"],"s":W+"Savonnerie_manufactory",
 "x":[
 {"n":"Savonnerie carpet","a":"Savonnerie","d":"Knotted-pile wool carpet with silk details from the royal Paris workshop, with framed medallions, bouquets and rinceaux on dark grounds.","mk":"Savonnerie manufactory","y":"1615","s":W+"Savonnerie_manufactory",
  "v":[{"n":"Louvre Grande Galerie carpets","mk":"Savonnerie manufactory","y":"1668–1683","d":"93 carpets for the Grande Galerie (and 13 for the Galerie d'Apollon) after Charles Le Brun"},
       {"n":"Napoleonic revival","mk":"Savonnerie manufactory","y":"after 1805","d":"production revived before merger into the Gobelins in 1825"}],
  "dt":"Ghiordes knot c. 90 per sq in · wool with silk · dark grounds · medallion and floral designs"},
 {"n":"Aubusson tapestry carpet","a":"Aubusson rug","d":"Flat-woven floral tapestry carpet from the Aubusson and Felletin workshops in central France.","mk":"","y":"19th century","s":W+"Aubusson_tapestry","v":[],"dt":"tapestry weave · floral designs · pastel and rose palettes"}]},
{"n":"Rya rug","a":"rya · rye · ryijy","d":"Scandinavian long-pile wool rug knotted with a Ghiordes-type knot, once a bed cover, later a floor rug or wall hanging.",
 "t":["vintage","new","wall hanging"],"s":W+"Rya_(rug)",
 "x":[
 {"n":"Swedish rya","a":"rya","d":"Long-piled (c. 1–3 in) knotted cover of three-strand wool, first used by seafarers instead of furs.","mk":"","y":"early 15th century","s":W+"Rya_(rug)",
  "v":[{"n":"Baroque floral rya","mk":"","y":"c. 1690","d":"shorter, closer pile with floral patterns, from Stockholm; became a daytime spread"}],"dt":"pile 1–3 in · three-strand wool knots · double-sided pile"},
 {"n":"Finnish ryijy","a":"ryijy","d":"Finnish long-tufted textile, used as bedcover and wedding rug, now mostly a wall hanging, often with Tree of Life motifs.","mk":"","y":"9th century onwards","s":W+"Ryijy",
  "v":[{"n":"Wedding ryijy","mk":"","y":"18th century","d":"wedding rug; e.g. late 18th-century Keuruu ryijy with couple, plants and birds"},
       {"n":"Liekki ('Flame')","mk":"","y":"","d":"designed by Akseli Gallen-Kallela"},
       {"n":"Modern artist ryijy","mk":"","y":"20th century","d":"by textile artists such as Laila Karttunen, Greta Skogster and Kirsti Ilvessalo"}],
  "dt":"natural white, grey, black; vegetable-dyed yellow, red, green, blue · geometric, floral, figurative motifs"},
 {"n":"Ege Rya","a":"","d":"Danish factory-made pure-wool rya rug of the 1960s–70s with abstract, geometric and op-art designs.","mk":"Ege","y":"1960s–1970s","s":"https://www.classic-modern.co.uk/ege-rya",
  "v":[{"n":"Gallery","mk":"Ege","y":"","d":"abstract art rugs"},{"n":"Galaxy Collection","mk":"Ege","y":"","d":"export range"}],
  "dt":"wool backing early 1960s, jute/polyester from mid-1960s · mothproofed · 25-year guarantee"}]},
{"n":"European workshop rug","a":"European hand-knotted carpet","d":"Hand-made pile carpet from a European workshop tradition, such as Spanish, Irish or Arts & Crafts English carpets.",
 "t":["antique","new","reproduction"],"s":W+"Donegal_Carpets",
 "x":[
 {"n":"Alcaraz carpet","a":"Spanish carpet","d":"Spanish knotted carpet from southern Castile in Renaissance style, dominated by acanthus vinescrolls.","mk":"","y":"16th century","s":W+"Alcaraz_rug","v":[],"dt":"muted palettes, e.g. dark green on green, dark yellow on yellow · animal figures"},
 {"n":"Alpujarra rug","a":"Alpujarra","d":"Spanish rug from the Alpujarras of woollen or silken loops worked on canvas.","mk":"","y":"","s":"https://www.merriam-webster.com/dictionary/alpujarra rugs","v":[],"dt":"looped pile · linen or canvas foundation"},
 {"n":"Hammersmith carpet","a":"Morris carpet · Hammersmith","d":"Morris & Co. hand-knotted carpet, named after Morris's Hammersmith home where they were first woven.","mk":"Morris & Co.","y":"","s":"https://collections.vam.ac.uk/item/O78824",
  "v":[{"n":"Bullerswood carpet","mk":"Morris & Co.","y":"1889","d":"by William Morris and J. H. Dearle, woven at Merton Abbey; V&A T.31-1923"}],
  "dt":"Turkish (Ghiordes) knot · 25 knots per sq in · wool pile on cotton warp"},
 {"n":"Donegal carpet","a":"Donegal","d":"Hand-made wool carpet from Killybegs, County Donegal, often with Celtic designs.","mk":"Donegal Carpets","y":"1898","s":W+"Donegal_Carpets",
  "v":[{"n":"St Eunan's Cathedral altar carpet","mk":"Donegal Carpets","y":"c. 1901","d":"designed by Oreste Amici, Letterkenny"},
       {"n":"Cork Exhibition carpet","mk":"Donegal Carpets","y":"1902","d":"first Donegal carpet with Celtic designs"}],
  "dt":"hand-knotted wool · Celtic and Arts & Crafts designs"}]},
{"n":"Designer rug","a":"art rug · studio rug","d":"Rug made to a named designer's or studio's design, from 20th-century studio weaving to contemporary collaborations.",
 "t":["hand-knotted","hand-tufted","flatweave","vintage","new"],"s":W+"M%C3%A4rta_M%C3%A5%C3%A5s-Fjetterstr%C3%B6m",
 "x":[
 {"n":"Märta Måås-Fjetterström rugs","a":"MMF rugs","d":"Swedish studio pile and flatwoven rugs blending Nordic folk tradition with modernism, signed MMF.","mk":"Märta Måås-Fjetterström AB","y":"1919","s":W+"M%C3%A4rta_M%C3%A5%C3%A5s-Fjetterstr%C3%B6m",
  "v":[{"n":"Hjorthagen","mk":"Märta Måås-Fjetterström AB","y":"1914","d":"knotted pile rug shown at the Baltic Exhibition (before the studio)"},
       {"n":"Röda trädgårdsmattan","mk":"Märta Måås-Fjetterström AB","y":"1930s","d":"classic rug"},
       {"n":"Bruna heden","mk":"Märta Måås-Fjetterström AB","y":"1930s","d":"classic rug"},
       {"n":"Hästhagen","mk":"Märta Måås-Fjetterström AB","y":"1930s","d":"classic rug"},
       {"n":"Ängarna","mk":"Märta Måås-Fjetterström AB","y":"1930s","d":"classic rug"},
       {"n":"Blå heden","mk":"Märta Måås-Fjetterström AB","y":"","d":"rug"}],
  "dt":"signed MMF; AB MMF from 1942 · later designs by Barbro Nilsson, Marianne Richter, Ann-Mari Forsberg"},
 {"n":"Kasthall rugs","a":"","d":"Swedish woven and tufted wool rugs made at the Kinna mill since 1889.","mk":"Kasthall","y":"1889","s":"https://kasthall.com/about",
  "v":[{"n":"Atlas","mk":"Kasthall","y":"","d":""},{"n":"Ori Honeycomb","mk":"Kasthall","y":"","d":""},{"n":"Chique 701 Rye","mk":"Kasthall","y":"","d":""}],"dt":"woven or hand-tufted · bespoke sizes and colours"},
 {"n":"nanimarquina rugs","a":"Nani Marquina","d":"Barcelona design-led rugs and kilims by Nani Marquina and invited designers, handmade in India, Pakistan and Nepal.","mk":"Nanimarquina","y":"1987","s":"https://www.salonemilano.it/en/articles/interview-nani-marquina-ceo-eponymous-cult-rugs-brand",
  "v":[{"n":"Gravitación","mk":"Nanimarquina","y":"1994","d":"designed by Eduardo Chillida"},
       {"n":"Cuadros","mk":"Nanimarquina","y":"1996","d":""},
       {"n":"Losanges","mk":"Nanimarquina","y":"","d":"kilim by Ronan and Erwan Bouroullec"},
       {"n":"Medina","mk":"Nanimarquina","y":"","d":"kilim by Nani Marquina"},
       {"n":"Luna","mk":"Nanimarquina","y":"","d":"designed by Oscar Tusquets"},
       {"n":"Digit","mk":"Nanimarquina","y":"","d":"designed by Cristian Zuzunaga"}],"dt":"hand-knotted, hand-tufted or kilim · wool, felt, recycled fibres"},
 {"n":"The Rug Company rugs","a":"","d":"London designer rugs, mostly hand-knotted with Tibetan knots, often in collaboration with international designers.","mk":"The Rug Company","y":"1997","s":W+"The_Rug_Company","v":[],"dt":"Tibetan knot · wool and silk · designer collaborations"}]}
]
brands=[
 {"n":"Savonnerie manufactory","c":"France","f":"1615","seg":"Royal carpet manufactory","d":"Paris royal knotted-carpet workshop founded by Pierre Dupont; merged into the Gobelins in 1825.","lines":[],"eras":["Peak c. 1650–1685","Manufacture Royale from 1712","Gobelins from 1825"],"sig":["Savonnerie carpet"],"sc":[],"rel":["Gobelins Manufactory"],"s":W+"Savonnerie_manufactory"},
 {"n":"Morris & Co.","c":"United Kingdom","f":"1875","seg":"Arts & Crafts furnishings","d":"William Morris's decorative-arts firm, maker of textiles, wallpapers and hand-knotted 'Hammersmith' carpets.","lines":[],"eras":["William Morris","John Henry Dearle"],"sig":["Hammersmith carpet"],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"Donegal Carpets","c":"Ireland","f":"1898","seg":"Hand-made carpets","d":"Killybegs hand-made wool carpet maker founded by Alexander Morton.","lines":[],"eras":["Morton family 1898–1957","Donegal Carpets Ltd from 1957"],"sig":["Donegal carpet"],"sc":[],"rel":[],"s":W+"Donegal_Carpets"},
 {"n":"Ege","c":"Denmark","f":"1938","seg":"Carpets and rugs","d":"Herning carpet maker, known for 1960s–70s Ege Rya rugs.","lines":["Ege Rya"],"eras":[],"sig":["Ege Rya"],"sc":[],"rel":[],"s":"https://egecarpets.com/about-ege-carpets/facts"},
 {"n":"Märta Måås-Fjetterström AB","c":"Sweden","f":"1919","seg":"Studio hand-woven rugs","d":"Båstad weaving studio founded by Märta Måås-Fjetterström, still weaving her and later artists' designs.","lines":[],"eras":["Märta Måås-Fjetterström 1919–1941","Barbro Nilsson, artistic director from 1942"],"sig":["Märta Måås-Fjetterström rugs"],"sc":[],"rel":[],"s":"https://mmf.se/pages/marta-maas-fjetterstrom"},
 {"n":"Kasthall","c":"Sweden","f":"1889","seg":"Premium woven and tufted rugs","d":"Swedish rug maker with its mill in Kinna.","lines":[],"eras":[],"sig":["Kasthall rugs"],"sc":[],"rel":[],"s":"https://kasthall.com/about"},
 {"n":"Nanimarquina","c":"Spain","f":"1987","seg":"Design rugs","d":"Barcelona rug brand founded by Nani Marquina, working with invited designers.","lines":[],"eras":["Nani Marquina"],"sig":["nanimarquina rugs"],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"The Rug Company","c":"United Kingdom","f":"1997","seg":"Designer hand-knotted rugs","d":"London rug company founded by Christopher and Suzanne Sharp.","lines":[],"eras":[],"sig":["The Rug Company rugs"],"sc":[],"rel":[],"s":W+"The_Rug_Company"}]
traditions=[
 {"n":"Moroccan Berber rug weaving","g":"Textiles & rugs","r":"Morocco (Middle and High Atlas, central plains)","p":"traditional to present","d":"Amazigh women's weaving of pile and flatwoven wool rugs for floors, bedding, tent dividers and dowry.","tech":"Ghiordes-knotted pile on horizontal ground looms; flatweave; rag weaving","mat":"hand-spun undyed and plant-dyed sheep's wool; fabric scraps","forms":["Beni Ourain","Azilal","Boujad","Beni M'Guild","Boucherouite","Moroccan kilim"],"ctr":["Beni Ourain confederation","High Atlas","Middle Atlas"],"auth":"hand-spun undyed wool, natural dyes, irregular hand-drawn motifs and no drawn pattern","s":"https://www.moroccancorridor.com/pages/beni-ourain"},
 {"n":"French court carpet (Savonnerie)","g":"Textiles & rugs","r":"Paris, France","p":"1615–1825 (then Gobelins)","d":"Royal knotted-pile carpet weaving in the Turkish manner, developed into a French style under Crown monopoly.","tech":"Ghiordes knot, c. 90 knots per sq in","mat":"wool with silk details","forms":["Savonnerie carpet"],"ctr":["Savonnerie manufactory, Chaillot","Gobelins Manufactory","Mobilier National collection"],"auth":"Crown property until 1768; dark grounds with medallions, bouquets and rinceaux","s":W+"Savonnerie_manufactory"},
 {"n":"Aubusson tapestry","g":"Textiles & rugs","r":"Aubusson and Felletin, Creuse, France","p":"c. 1300 to present","d":"Tapestry weaving in family workshops, also producing floral tapestry carpets; UNESCO intangible heritage since 2009.","tech":"tapestry weaving","mat":"wool","forms":["Aubusson tapestry carpet"],"ctr":["Aubusson","Felletin","Jean Lurçat (from 1939)"],"auth":"","s":W+"Aubusson_tapestry"},
 {"n":"Scandinavian rya","g":"Textiles & rugs","r":"Sweden, Norway, Finland","p":"15th century to present","d":"Long-pile knotted wool covers, later floor rugs, wedding rugs and wall hangings (Finnish ryijy).","tech":"Ghiordes-type knot of three wool strands, long pile","mat":"wool","forms":["Swedish rya","Finnish ryijy","Ege Rya"],"ctr":["Stockholm","Keuruu"],"auth":"mixed-shade three-strand knots; long pile; dated or initialled folk pieces","s":W+"Rya_(rug)"}]
notes=("All five planned kinds are new (no old data). Left out: Marimekko rugs (marimekko.com returned 429, no other source fetched); "
 "Cuenca carpets (no fetched source); röllakan/rölakan flatweave and MMF Dukater (belong to Flatweave rug on another shelf; only a snippet source); "
 "Kasthall designer credits and Rug Company named collaborations (not on fetched pages); nanimarquina Bicicleta (not on fetched page). "
 "Britannica, MFAH, Nazmiyal and Finnish Design Shop blocked (403). Morris & Co. and Nanimarquina brand facts from knowledge.")
out={"kinds":kinds,"brands":brands,"traditions":traditions,"notes":notes}
p="/home/user/Possession-Taxonomy/rebuild/work/B2/shelves/00_01.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
