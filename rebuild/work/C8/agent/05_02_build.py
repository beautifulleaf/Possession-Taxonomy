import json, os
W='https://en.wikipedia.org/wiki/'
MW=W+'William_Morris_wallpaper_designs'
COLE='https://cole-and-son.com/our-heritage/'
ZW=W+'Zuber_%26_Cie'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":list(v),"dt":dt}
x=[
 X("Strawberry Thief","Morris design of thrushes stealing strawberries among flowers and leaves, first a printed cotton, now a wallpaper classic.","Morris & Co.","1883",
   "https://johnlewis.com/morris-co-strawberry-thief-wallpaper-miami-strip/p111882116",
   [{"n":"Original printed cotton","mk":"Morris & Co.","y":"1883","d":"indigo discharge print at Merton Abbey with red and yellow added","s":""},
    {"n":"Miami Strip colourway wallpaper","mk":"Morris & Co.","y":"","d":"dark ground with pink and teal; 32 cm straight-match repeat"}],
   "colourway · ground colour · paper finish"),
 X("Trellis","Morris's first wallpaper design: roses climbing a trellis with birds drawn by Philip Webb, inspired by the Red House garden.","Morris & Co.","1862",
   "https://collections.vam.ac.uk/item/O248458/trellis-wallpaper-morris-william",
   [{"n":"Original block print","mk":"Morris & Co.","y":"1864","d":"block-printed in distemper by Jeffrey & Co. for Morris, Marshall, Faulkner & Co."},
    {"n":"Grey-green colourway (V&A E.451-1919)","mk":"Morris & Co.","y":"1864","d":"from the Volume 1 pattern book"}],
   "colourway · light or dark ground"),
 X("Willow Bough","Morris pattern of willow leaves on curving branches, later also used for fabric.","Morris & Co.","1887",MW,dt="colourway"),
 X("Daisy","Early Morris wallpaper of simple flowering plants in a folk-like grid.","Morris & Co.","1864",MW,dt="colourway"),
 X("Acanthus","Morris wallpaper of large overlapping acanthus leaves.","Morris & Co.","1875",MW,dt="colourway"),
 X("Pimpernel","Morris wallpaper of symmetrical tulips and pimpernel flowers.","Morris & Co.","1876",MW,dt="colourway"),
 X("Woods","Cole & Son pattern of slender tree trunks and foliage from its mid-century Contemporary Collection.","Cole & Son","1950s–1960s",COLE,
   [{"n":"EDIDA Wallcovering of the Year","mk":"Cole & Son","y":"2005","d":"award to the reissued design"}],"colourway"),
 X("Palm Leaves","Large-scale palm-frond pattern from Cole & Son's 1950s–60s Contemporary Collection.","Cole & Son","1950s–1960s",COLE,dt="colourway"),
 X("Hummingbirds","Cole & Son classic of hummingbirds among flowering branches.","Cole & Son","",COLE,dt="colourway"),
 X("Zebras","Leaping zebras and arrows, first drawn for the Gino of Capri restaurant in Manhattan.","Scalamandré","1945","https://scalamandre.com/zebras",
   [{"n":"Original restaurant design","mk":"","y":"1945","d":"drawn by Valentino Crescenzi on a red ground"},
    {"n":"Scalamandré recreation","mk":"Scalamandré","y":"1973","d":"redrawn by Flora Scalamandré after a fire; baby zebra lacks a stripe"},
    {"n":"Masai Red","mk":"Scalamandré","y":"","d":"wallpaper colourway"},
    {"n":"Limelight","mk":"Scalamandré","y":"","d":"wallpaper colourway"}],
   "printed paper · grasscloth · paperweave · vinyl · colourway"),
 X("Vues de l'Amérique du Nord","Zuber woodblock-printed panoramic wallpaper of North American scenes.","Zuber & Cie","1843",ZW,dt="panoramic set · colour or grisaille"),
 X("Eldorado","Zuber woodblock-printed panoramic wallpaper.","Zuber & Cie","",ZW,dt="panoramic set"),
 X("Chinese wallpaper","Hand-painted chinoiserie panels of trees, flowers and birds, first made by Chinese artists for European houses.","","1740–1790",W+"Chinoiserie",
   [{"n":"Hand-painted modern panels","mk":"de Gournay","y":"1986–","d":"hand-painted wallpapers made mainly at its Shanghai studio"}],
   "silk or paper ground · panel set · colourway",a="chinoiserie wallpaper"),
 X("Toile de Jouy","Repeated pastoral scene in one colour on a white or off-white ground, after the cloths of Jouy-en-Josas.","","late 18th century",W+"Toile_de_Jouy",
   dt="print colour (black, red, blue) · scene"),
 X("Glasgow Toile","Timorous Beasties toile that swaps pastoral scenes for modern Glasgow street life.","Timorous Beasties","",
   "https://collections.vam.ac.uk/item/O1427908/glasgow-glasgow-toile-de/",
   [{"n":"Glasgow toile de Jouy (V&A)","mk":"Timorous Beasties","y":"2017","d":"given by the company to the V&A"}],"colourway"),
 X("Lincrusta","Deep-embossed wallcovering of gelled linseed oil on a paper base, painted after hanging.","Lincrusta","1877",W+"Lincrusta",
   [{"n":"Lincrusta (Morecambe)","mk":"Lincrusta","y":"2014–","d":"made in Morecambe by Heritage Wallcoverings"}],"pattern · dado, frieze or full-height"),
 X("Anaglypta","Lighter embossed relief wallpaper, originally of wood pulp and cotton, made to be painted.","Anaglypta","1887",W+"Anaglypta",
   [{"n":"Anaglypta Original","mk":"Anaglypta","y":"","d":"all-wood-pulp duplex paper introduced under Reed"}],"paper or vinyl · pattern"),
]
x[0]["v"][0].pop("s")
wall={"n":"Wallpaper","a":"wallcovering","d":"Paper, vinyl or textile wall covering sold in rolls or panels for hanging.",
 "t":["paper","vinyl","non-woven","paste-the-wall","embossed relief","flock","grasscloth","hand-painted silk","panoramic mural"],
 "s":"https://www.wickes.co.uk/Products/Painting+Decorating/Wallpaper/Decorative-Wallpaper/c/1001129","x":x,
 "m":[["Heritage Trail","Arthouse"],["Linen Texture","Arthouse"],["Magical Garden","Arthouse"],["Everbloom","Holden Decor"],["Osterley","Holden Decor"],["Regal Beasts","Holden Decor"],["Safari Fusion","Holden Decor"],["Amelie","Rasch"],["Dimension Panel","Rasch"],["Innocence","Superfresco"],["Natural Branches","Superfresco"],["Organics","Superfresco"]],
 "r":[["Superfresco Easy","Superfresco"],["Fornasetti","Cole & Son"]]}
kinds=[wall,
 {"n":"Wall tile","a":"","d":"Tile made and rated for walls.","t":["ceramic","porcelain","metro","mosaic","glass"],"s":"https://www.wickes.co.uk/Products/Tiles/Wall-Tiles/c/1047001"},
 {"n":"Floor tile","a":"","d":"Tile made and rated for floors, with its wear and slip rating.","t":["porcelain","ceramic","natural stone","wood-effect"],"s":"https://www2.wickes.co.uk/Products/Tiles/Floor-Tiles/c/1000803"},
 {"n":"Plaster","a":"skim · finishing plaster · bonding plaster","d":"Powdered plaster mixed with water to undercoat or skim walls and ceilings.","t":["finish (skim)","bonding undercoat","one-coat"],
  "s":"https://www.british-gypsum.com/products/plaster-products/thistle-multifinish",
  "m":[["Thistle MultiFinish","British Gypsum"],["Carlite Bonding Plaster","Gyproc"],["Carlite Finish Plaster","Gyproc"],["Carlite Ultra Finish Plaster","Gyproc"]]},
 {"n":"Flooring underlay","a":"","d":"Foam, fibre or cork layer laid under laminate, wood or vinyl flooring.","t":["polyethylene foam","fibreboard","cork","rubber","with damp-proof membrane"],
  "s":"https://www.screwfix.com/p/2mm-polyethylene-foam-underlay-roll-20m-/793fw"}]
def B(n,c,f,seg,d,s,lines=(),eras=(),sig=(),rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Morris & Co.","United Kingdom","1861","Heritage design house","Arts and Crafts firm of William Morris whose block-printed wallpapers were made by Jeffrey & Co.; the name now belongs to Walker Greenbank and is sold through Sanderson.",
   "https://en.wikipedia.org/wiki/Morris_%26_Co.",eras=["Morris, Marshall, Faulkner & Co., 1861–1875","Morris & Co., 1875–1940"],sig=["Strawberry Thief","Trellis","Willow Bough","Acanthus"]),
 B("Cole & Son","United Kingdom","1875","Heritage design house","London wallpaper maker holding a block archive of about 2,000 woodblocks and an early screen-print studio; Royal Warrant 1961.",
   COLE,lines=["Contemporary Collection","Fornasetti","Historic Royal Palaces","Ardmore","Pearwood"],eras=["A.P. Cole ownership from 1941"],sig=["Woods","Palm Leaves","Hummingbirds"]),
 B("Zuber & Cie","France","1797","Heritage design house","Rixheim maker of woodblock-printed wallpapers and panoramics, using more than 100,000 historic woodblocks.",ZW,sig=["Vues de l'Amérique du Nord","Eldorado"]),
 B("de Gournay","United Kingdom","1986","Luxury hand-painted","British maker of hand-painted wallpapers founded by Claud Cecil Gurney, made mainly in its Shanghai studio.","https://en.wikipedia.org/wiki/De_Gournay",sig=["Chinese wallpaper"]),
 B("Scalamandré","United States","1929","Luxury design house","American wallpaper and fabric house whose Zebras pattern became its emblem.","https://scalamandre.com/zebras",sig=["Zebras"]),
 B("Timorous Beasties","United Kingdom","1990","Independent design studio","Glasgow wallpaper and fabric studio founded by Alastair McCauley and Paul Simmons, known for subverted historical patterns.",
   "https://collections.vam.ac.uk/item/O1427908/glasgow-glasgow-toile-de/",sig=["Glasgow Toile"]),
 B("Lincrusta","United Kingdom","1877","Heritage relief wallcovering","Embossed linseed-oil wallcovering invented by Frederick Walton, now made in Morecambe.",W+"Lincrusta",sig=["Lincrusta"],rel=["Anaglypta"]),
 B("Anaglypta","United Kingdom","1887","Relief wallpaper","Embossed paintable wallpaper developed by Thomas John Palmer; now owned by Retford Wallcoverings.",W+"Anaglypta",sig=["Anaglypta"],rel=["Lincrusta"]),
]
notes=("Wallpaper became the enthusiast kind with 17 archetypes (Morris & Co., Cole & Son, Scalamandré, Zuber, Timorous Beasties, Lincrusta, Anaglypta, plus maker-free Chinese wallpaper and Toile de Jouy); mass-market Arthouse/Holden/Rasch/Superfresco models kept as m. "
 "Wickes own-label tile ranges (Cosmopolitan, Farmhouse, Metro; Central Park, Lava, Livingstone, Melia, Onyx, Petra, Ruben, Sigford) are blank-maker names: folded into types (metro etc.) and dropped as models; no tile brands added (no tier research done). "
 "Left out: Florence Broadhurst (no named design confirmed on a fetched page), Morris Golden Lily/Snakeshead (only retailer search snippets), de Gournay Earlham and Glasgow Toile original date (pages 403 or undated), Cole & Son Woods designer. Heritage tiles belong to Heritage & reclaimed.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/C8/shelves/05_02.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
