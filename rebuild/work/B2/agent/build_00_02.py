import json, os
W='https://en.wikipedia.org/wiki/'
K=W+'Kilim'; NV=W+'Navajo_weaving'; HK=W+'Hooked_rug'; RR=W+'Rag_rug'
kinds=[
{"n":"Flatweave rug","a":"kilim · soumak · dhurrie · flatwoven rug","d":"A rug woven without pile, the pattern made by the weft (kilim, soumak, dhurrie and related constructions).",
 "t":["slit-tapestry","interlocked tapestry","weft-wrapped (soumak)","supplementary weft (zili)","strip-woven (jajim)","antique","new","reproduction"],
 "s":"https://www.kilim.com/kilim-wiki/kilim-flatweave-handwoven-hand-knotted",
 "x":[
  {"n":"Kilim","a":"gelim · ćilim · kelim","d":"Slit-tapestry flatweave of Anatolia, Persia, the Caucasus and the Balkans, named by town or tribe of origin.","mk":"","y":"","s":K,
   "v":[{"n":"Hotamis kilim","mk":"","y":"early 19th century","d":"central Anatolia"},
        {"n":"Konya kilim","mk":"","y":"","d":"Anatolian place style"},
        {"n":"Malatya kilim","mk":"","y":"","d":"Anatolian place style"},
        {"n":"Karapınar kilim","mk":"","y":"","d":"Anatolian place style"},
        {"n":"Awar kilim","mk":"","y":"late 19th century","d":"Caucasus"}],
   "dt":"region and town · slit or interlocked joins · natural or aniline dyes · antique, new or reproduction"},
  {"n":"Pirot kilim","a":"Pirot carpet · Pirotski ćilim · Şarköy · sarkoy","d":"Woollen tapestry-woven kilim from Pirot, south-eastern Serbia, with geometric, plant and figural ornaments.","mk":"","y":"Middle Ages; mentioned 1565","s":W+'Pirot_carpet',
   "v":[{"n":"Rašičeva šara (Model of Rašić)","mk":"","y":"","d":"design based on General Mihailo Rašić's kilim"},
        {"n":"Bombe u pregradama","mk":"","y":"","d":"border ornament called kornjača (turtle)"}],
   "dt":"about 122 ornaments in 96 types · vertical loom · geographical indication since 2002"},
  {"n":"Chiprovtsi kilim","a":"Chiprovtsi carpet","d":"Double-sided Bulgarian woollen kilim from Chiprovtsi, woven by hand since the 17th century.","mk":"","y":"17th century","s":W+'Chiprovtsi_carpet',
   "v":[{"n":"Early red-and-black kilim","mk":"","y":"","d":"red and black only"},{"n":"Later polychrome kilim","mk":"","y":"","d":"adds yellow, brown, blue and green"}],
   "dt":"3–5 mm thick · plant or mineral dyes · UNESCO ICH 2014"},
  {"n":"Soumak","a":"sumak · soumak mafrash","d":"Thick weft-wrapped flatweave with a smooth front, ragged back and no slits, used for rugs and bedding bags.","mk":"","y":"","s":W+'Soumak',
   "dt":"Caucasus (Shirvan), Persia (Luristan), Anatolia, Shahsavan, Kurdish, Baloch · rug or mafrash bag"},
  {"n":"Dhurrie","a":"durrie · dhurri · durry · dari","d":"Handwoven flat cotton or wool rug of the Indian subcontinent, used as floor covering or bedding.","mk":"","y":"","s":W+'Dhurrie',
   "v":[{"n":"Panja dhurrie","mk":"","y":"","d":"Salawas, Rajasthan"},{"n":"Punja dhurrie","mk":"","y":"","d":"Haryana"},
        {"n":"Navalgund dhurrie","mk":"","y":"","d":"Karnataka; geographical tag"},{"n":"Sitapur (Citapore) rug","mk":"","y":"","d":"Uttar Pradesh"}],
   "dt":"cotton, wool, jute or silk · centre of origin"},
  {"n":"Jajim","a":"jijim · cicim · jajim-bafi","d":"Blanket-like flatweave made of several narrow strips sewn together, from Iranian villages, Azerbaijan and Turkey.","mk":"","y":"","s":W+'Jajim',
   "dt":"number of strips · wool, cotton or blend · rug, cover or bedding use"},
  {"n":"Zili","a":"","d":"Coarse supplementary-weft flatweave used for mats, sacks, cushions and tent pieces.","mk":"","y":"","s":K,"dt":"region · use"},
  {"n":"Rölakan","a":"röllakan · Scanian interlocked tapestry","d":"Swedish double-interlocked tapestry weave, wool on linen warp, with geometric stars, rosettes and lightning zigzags.","mk":"","y":"mid-18th to mid-19th century (Scania)","s":W+'Swedish_carpets_and_rugs',
   "dt":"folk or 20th-century studio · pattern · size"}]},
{"n":"Navajo rug","a":"Navajo weaving · Navajo blanket · Diné textile","d":"A tapestry-woven wool rug or blanket made by Navajo (Diné) weavers, classed by regional trading-post style.",
 "t":["antique","contemporary","vegetal dye","aniline dye"],"s":NV,
 "x":[
  {"n":"Chief's blanket","a":"","d":"Banded wearing blanket woven in successive phases, the earliest Navajo textiles prized by collectors.","mk":"","y":"c. 1840 onward","s":NV,
   "v":[{"n":"First phase","mk":"","y":"c. 1840","d":""},{"n":"Third phase","mk":"","y":"c. 1870–1880","d":""},{"n":"Fourth phase","mk":"","y":"","d":""}],
   "dt":"phase · wool and dye · condition"},
  {"n":"Germantown","a":"","d":"Weaving in four-ply aniline-dyed yarn from Pennsylvania, brought in by the railroad.","mk":"","y":"early 1880s","s":NV,"dt":"yarn · design"},
  {"n":"Eye Dazzler","a":"","d":"Bright, busy late-19th-century weaving made possible by aniline dyes.","mk":"","y":"late 19th century","s":NV,"dt":"colour scheme · yarn"},
  {"n":"Two Grey Hills","a":"","d":"Mainly black, white and natural-grey regional style associated with traders George Bloomfield and Ed Davies.","mk":"","y":"","s":NV,"dt":"size · fineness"},
  {"n":"Ganado","a":"Ganado Red","d":"Red-dominated regional style with black and white, from John Lorenzo Hubbell's trading post.","mk":"","y":"","s":NV,"dt":"size · pattern"},
  {"n":"Teec Nos Pos","a":"","d":"Colourful regional style with very extensive patterning.","mk":"","y":"","s":NV,"dt":"size · palette"},
  {"n":"Crystal","a":"","d":"Regional style with 'Oriental' elements, from J. B. Moore's post in the Chuska Mountains.","mk":"","y":"from 1897","s":NV,"dt":"size · palette"},
  {"n":"Wide Ruins","a":"","d":"Warm gold, orange, beige and yellow style influenced by the Lippincotts' trading post.","mk":"","y":"","s":NV,
   "v":[{"n":"Pine Springs","mk":"","y":"","d":"similar, adds soft greens"}],"dt":"size · vegetal dyes"},
  {"n":"Storm Pattern","a":"","d":"Central rectangle with four outer rectangles linked by zigzag lightning forms.","mk":"","y":"","s":NV,"dt":"size · palette"},
  {"n":"Yei","a":"Yei be Chei · Yeibichai","d":"Pictorial weaving showing Yei figures.","mk":"","y":"","s":NV,"dt":"figures · size"},
  {"n":"Chinle","a":"","d":"Simpler regional style in yellow, natural wool and a few other colours.","mk":"","y":"","s":NV,"dt":"size"},
  {"n":"Raised Outline","a":"","d":"Regional technique with raised outlines, as at Newlands and Coal Mine Mesa.","mk":"","y":"","s":NV,"dt":"place · size"}]},
{"n":"Hooked rug","a":"hooked mat · latch-hook rug","d":"A rug made by pulling loops of yarn or fabric strips through a woven backing with a hook.",
 "t":["yarn","fabric strip","latch-hook","antique","kit"],"s":"https://harcourtcollection.com/pages/construction-and-weave-types",
 "x":[
  {"n":"Waldoboro rug","a":"sculpted hooked rug","d":"Maine hooked rug with motifs hooked high and sheared into a sculpted pile on linen backing.","mk":"","y":"mid-1860s–early 1900s (finest 1870–1885)","s":"https://welikerughooking.com/Rug-Hooking-Articles/The-Waldoboro-Museum-Rug","dt":"pile height · scroll border · natural dyes"},
  {"n":"Grenfell mat","a":"silk-stocking mat","d":"Kit-standardised hooked mat of the Grenfell Mission, Newfoundland and Labrador, often of recycled silk stockings.","mk":"","y":"early 20th century; standards by 1916","s":"https://www.canadashistory.ca/explore/museums-galleries-archives/hooked-mat","dt":"material · motif"},
  {"n":"Chéticamp rug","a":"Cheticamp hooked rug","d":"Cape Breton hooked rug in dyed homespun yarn, made to Lillian Burke's designs for New York decorators.","mk":"","y":"1927–1940","s":W+'Lillian_Burke',"dt":"size · design · muted palette"},
  {"n":"Stamped-pattern rug","a":"Frost pattern","d":"Hooked rug worked on a commercially stamped design, as sold by Edward Sands Frost in Maine.","mk":"","y":"c. 1868–1871","s":HK,"dt":"pattern · material"},
  {"n":"Latch-hook rug","a":"Readicut · Shillcraft","d":"Kit rug knotted with a latch hook from pre-cut yarn on canvas.","mk":"","y":"heyday after WWII","s":HK,
   "v":[{"n":"Readicut kit","mk":"Readicut","y":"","d":"Britain"},{"n":"Shillcraft kit","mk":"Shillcraft","y":"","d":"North America"}],"dt":"kit · design · size"}]},
{"n":"Felt rug","a":"felt carpet · felt ball rug","d":"A rug or carpet of matted fibre, made by felting rather than weaving.",
 "t":["felt ball","pressed felt","stitched felt"],"s":"https://www.woollyfelt.com/products/handmade-purple-felt-ball-wool-round-area-rug",
 "x":[
  {"n":"Shyrdak","a":"syrmak","d":"Kyrgyz and Kazakh stitched felt carpet of cut-out contrasting felt layers in mirrored pairs.","mk":"","y":"","s":W+'Shyrdak',"dt":"motif (water, horns, yurt) · colours · size"},
  {"n":"Ala kiyiz","a":"tekemet","d":"Kyrgyz and Kazakh felt carpet with coloured wool pressed into the base by rolling, no stitching.","mk":"","y":"","s":W+'Ala_kiyiz',"dt":"ground colour · motifs · size"}]},
{"n":"Rag rug","a":"rag mat · thrift rug","d":"A rug braided, woven or hooked from strips of reused cloth.",
 "t":["woven","braided","hooked","proddy / clippy"],"s":"https://www.trc-leiden.nl/trc-needles/individual-textiles-and-textile-types/accessories/rag-rugs",
 "x":[
  {"n":"Trasmatta","a":"Swedish rag rug · ripsmatta","d":"Swedish loom-woven rug with cloth-strip weft on cotton or linen warp.","mk":"","y":"word from 1824; common after the 1860s","s":"https://sv.wikipedia.org/wiki/Trasmatta","dt":"weave (tuskaft, kypert, rosengång) · warp colours · length"},
  {"n":"Braided rug","a":"","d":"Rug of braided fabric strips or yarn coiled and sewn, common in colonial America.","mk":"","y":"","s":W+'Braided_rug',"dt":"banded, cloth, flat or yarn braid · hand or machine"},
  {"n":"Proggy mat","a":"proddy · clippy · clootie · poke · peg mat","d":"British shaggy mat of cloth clippings poked through hessian.","mk":"","y":"19th century; revived WWII","s":RR,"dt":"material · shag length"}]},
{"n":"Hide rug","a":"cowhide · sheepskin","d":"A rug that is a tanned animal hide with its hair, or a patchwork of hides (cowhide, sheepskin).",
 "t":["natural","dyed","printed","patchwork"],"s":"https://www.ikea.com/sg/en/cat/rugs-carpets-textiles-10653",
 "x":[
  {"n":"Cowhide rug","a":"","d":"Whole tanned cowhide with hair, coloured by breed; damaged hides go into patchwork rugs.","mk":"","y":"","s":W+'Cowhide',"dt":"natural or dyed · whole or patchwork · size"},
  {"n":"Sheepskin rug","a":"lambskin","d":"Tanned sheep hide with the fleece left on, used as a rug or baby rug.","mk":"","y":"","s":W+'Sheepskin',"dt":"fleece length · seed grade"}]}]
trads=[
 {"n":"Anatolian & Caucasian kilim weaving","g":"Textiles & rugs","r":"Anatolia, Persia, Caucasus","p":"","d":"Village and nomad flatweaving of kilims, named by town or tribe.","tech":"slit tapestry, supplementary weft","mat":"wool, cotton","forms":["Kilim","Zili","Jajim"],"ctr":["Konya","Malatya","Karapınar"],"auth":"","s":K},
 {"n":"Balkan kilim (Pirot & Chiprovtsi)","g":"Textiles & rugs","r":"Serbia, Bulgaria","p":"Middle Ages / 17th century to present","d":"Double-sided wool kilims woven by hand on vertical looms.","tech":"tapestry flatweave","mat":"wool, plant and mineral dyes","forms":["Pirot kilim","Chiprovtsi kilim"],"ctr":["Pirot","Chiprovtsi"],"auth":"Pirot geographical indication (2002); UNESCO ICH for Chiprovtsi (2014)","s":W+'Chiprovtsi_carpet'},
 {"n":"Navajo weaving","g":"Textiles & rugs","r":"Navajo Nation, south-western United States","p":"c. 1840 to present","d":"Diné tapestry weaving of blankets and rugs, styled by trading post.","tech":"tapestry weave","mat":"wool; vegetal and aniline dyes","forms":["Chief's blanket","Two Grey Hills","Ganado","Teec Nos Pos","Yei"],"ctr":["Hubbell (Ganado)","Two Grey Hills","Crystal","Wide Ruins"],"auth":"","s":NV},
 {"n":"Kyrgyz felt carpets (ala kiyiz & shyrdak)","g":"Textiles & rugs","r":"Kyrgyzstan","p":"","d":"Felt carpets made by Kyrgyz women; on UNESCO's urgent-safeguarding list since 2012.","tech":"pressed felt (ala kiyiz), cut and stitched felt (shyrdak)","mat":"sheep's wool, natural dyes","forms":["Shyrdak","Ala kiyiz"],"ctr":[],"auth":"","s":"https://ich.unesco.org/en/USL/00693"}]
notes=("Kept all six planned kinds (k30,k31,k35,k36,k34 merged; Navajo rug new, sourced to Wikipedia). Old flat models Kilim/Soumak/Dhurrie/Jijim became archetypes; Felt ball rug became a type. "
 "Left out for lack of a retrievable source: verneh (Britannica 403), reindeer hide, Persian kilim as separate archetype, Anatolian kilim phases. Navajo styles have no dates in source beyond those given; trader names in definitions rather than mk. No brand entries needed (no archetype maker in register; Readicut/Shillcraft named only as versions).")
out={"kinds":kinds,"brands":[],"traditions":trads,"notes":notes}
p='work/B2/shelves/00_02.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
