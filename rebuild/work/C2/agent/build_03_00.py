import json, os
BCI="https://www.bonsai-bci.com/knowledge/tools"
BE="https://www.bonsaiempire.com/basics/general/tools"
WIKI="https://en.wikipedia.org/wiki/Bonsai_cultivation_and_care"
KAN="https://www.bonsai.co.uk/browse/accessories/tools/kaneshin-carbon-steel-bonsai-tools/"
MIS="https://www.mistralbonsai.com/tienda/en/tools/1373-podadora-concava-recta-170-mm"
LAOS="https://www.laosgarden.com/gb/branch-cutters/24790-masakuni-stainless-xs-knob-cutter-ma8036-145-mm.html"
JT="https://www.japanesetools.com.au/collections/kikuwa"
JG="https://japanesegardens.jp/product-category/bonsai-tools/kikuwa/"
V16="https://valavanisbonsaiblog.com/2016/11/21/2016-autumn-japan-bonsai-exploration-part-7-final/"
V13="https://valavanisbonsaiblog.com/2013/11/25/japan-international-bonsai-tour-exploration-autumn-2013-part-6-final/"
EUP="https://bonsaiempire.com/locations/potters/bonsai-potters-europe"
HER="https://www.herons.co.uk/Bonsai-Pots/Ceramic-Pots/Shohin-Chinese-Ceramic-Bonsai-Pots"
TOK="https://en.wikipedia.org/wiki/Tokoname_ware"
YIX="https://en.wikipedia.org/wiki/Yixing_clay"
POD="https://bonsaimirai.podbean.com/e/joshua-roth-tools/"
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Bonsai pot","a":"bonsai container · bonsai tray · hachi","d":"Shallow glazed or unglazed pot with drainage and wire holes, made for growing bonsai.",
  "t":["unglazed","glazed","rectangle","oval","round","square","cascade","shohin size","accent pot"],
  "s":"https://www.bonsaidirect.co.uk/product/unglazed-rectangular-bonsai-pot/",
  "x":[
   {"n":"Tokoname bonsai pot","a":"Japanese bonsai pot","d":"Pot from the kilns of Tokoname, Japan, the best-known source of bonsai containers; hand-built or press-moulded, stamped with the kiln seal.",
    "mk":"","y":"19th century–present","s":V16,
    "v":[V("Gyozan Kiln","Gyozan","","hand-built without moulds; mostly unglazed, some glazed"),
         V("Reiho Kiln","Reiho","","famous for glazed pots, also unglazed; seal stamped on every base"),
         V("Yamaaki Kiln","Yamaaki","","mainly unglazed brown pots, plus light blue glaze"),
         V("Koyo Kiln","Koyo","","smaller glazed pots, unusual glaze decoration"),
         V("Shuho Kiln","Shuho","","glazed small and shohin pots"),
         V("Ikko Kiln","Ikko","","all sizes, glazed and unglazed, fine detail")],
    "dt":"hand-built or pressed · unglazed brown or glazed · seal on base · shohin to large"},
   {"n":"Antique-style Tokoname bonsai pot","a":"","d":"Antique-style bonsai pot from Tokoname, a collector's item still being made.",
    "mk":"","y":"","s":TOK,"v":[],"dt":"stoneware or redware · kiln and potter marks"},
   {"n":"Chinese bonsai pot","a":"Chinese ceramic bonsai pot","d":"Mass-produced or hand-made pot from China, the main source of affordable bonsai containers, glazed or unglazed.",
    "mk":"","y":"","s":HER,"v":[],"dt":"round, oval, square, rectangular, fan, lotus, cascade · turquoise, blue, green, cream, crackle glazes"},
   {"n":"European studio bonsai pot","a":"hand-made bonsai pot","d":"Hand-made pot from an independent European bonsai potter or small studio.",
    "mk":"","y":"1980s–present","s":EUP,
    "v":[V("Walsall Studio Ceramics","Walsall Studio Ceramics","1986","David Jones, West Midlands, UK"),
         V("Erin Pottery","Erin Pottery","1998","Glyn and Victor Harris, Bristol, UK"),
         V("Isabelia","Isabelia","2000","Staré Město, Czech Republic"),
         V("Bryan Albright","Bryan Albright","1985","UK"),
         V("Petra Hahn","Petra Hahn","2000","Germany"),
         V("Carles Vives","Carles Vives","1978","Canovelles, Spain"),
         V("Pravoslav Dorda","Pravoslav Dorda","1990s","Czech Republic"),
         V("Antonio Ziccarelli","Antonio Ziccarelli","2010","woodfired, Italy")],
    "dt":"hand-thrown or slab-built · woodfired or electric · individual glazes"}]},
 {"n":"Concave cutter","a":"concave branch cutter · branch cutter","d":"Cutter with curved jaws that removes branches flush, leaving a slightly hollow wound that heals without a bump.",
  "t":["straight blade","semi-round blade","carbon steel","stainless steel","170–285 mm"],"s":BCI,
  "x":[
   {"n":"Straight-blade concave cutter","a":"","d":"The original concave branch cutter, both blades cutting, for green branches of about 2–3 cm.",
    "mk":"Masakuni","y":"","s":MIS,
    "v":[V("No.3S large concave branch cutter, 205 mm","Kaneshin"),V("No.6C narrow concave cutter with spring, 180 mm","Kaneshin"),V("No.3B large branch cutter with spring, 205 mm","Kaneshin")],
    "dt":"170 mm (shohin) to 285 mm (large trees) · carbon or stainless steel"},
   {"n":"Semi-round concave cutter","a":"","d":"Concave cutter with a rounded blade profile.","mk":"","y":"","s":BE,"v":[],"dt":"sizes · carbon or stainless steel"}]},
 {"n":"Knob cutter","a":"wen cutter","d":"Cutter with spherical, bite-shaped jaws that carve a deep hollow where a branch or stub has been removed.",
  "t":["carbon steel","stainless steel"],"s":BCI,
  "x":[{"n":"Spherical-jaw knob cutter","a":"wen cutter","d":"Ball-shaped jaws nibble out stubs and callus after a concave cut.","mk":"","y":"","s":BCI,
    "v":[V("No.10 large knob cutter, 175 mm","Kaneshin"),V("No.11 large knob cutter, 210 mm","Kaneshin"),V("MA8036 stainless XS knob cutter, 145 mm","Masakuni","","for shohin")],
    "dt":"145–210 mm · carbon or stainless steel"}]},
 {"n":"Bonsai shears","a":"bonsai scissors · butterfly shears","d":"Long-handled scissors with short sharp blades for twigs, leaves and fine roots.",
  "t":["butterfly","long-handled","twig","shohin and azalea","root"],"s":BCI,
  "x":[{"n":"Butterfly shears","a":"standard bonsai shears","d":"Wide-handled shears with short blades for maintenance pruning and thicker twigs.","mk":"","y":"","s":BCI,
     "v":[V("No.35A carbon steel bonsai scissors, 180 mm","Kaneshin"),V("No.40b large carbon steel bonsai scissors, 180 mm","Kaneshin")],"dt":"carbon or stainless steel · length"},
   {"n":"Long slim twig shears","a":"twig shears","d":"Long, slim shears that reach into dense canopies.","mk":"","y":"","s":BE,
     "v":[V("No.34C trimming scissors, 160 mm","Kaneshin"),V("No.32 trimming bud scissors, 150 mm","Kaneshin")],"dt":"length · blade shape"},
   {"n":"Shohin and azalea shears","a":"satsuki shears","d":"Small shears for shohin trees, trimming azaleas and removing spent flowers.","mk":"","y":"","s":BE,"v":[],"dt":"size"},
   {"n":"Root shears","a":"strong standard shears","d":"Heavy-duty shears for root pruning at repotting.","mk":"","y":"","s":BE,"v":[],"dt":"thicker blades"}]},
 {"n":"Bonsai wire & wire cutter","a":"training wire · wire cutter","d":"Soft wire wrapped round branches to shape them, and the round-headed cutter that removes it flush against the bark.",
  "t":["anodised aluminium","annealed copper","wire gauge"],"s":BCI,
  "x":[{"n":"Anodised aluminium wire","a":"","d":"Soft wire, the standard for deciduous trees and beginners.","mk":"","y":"","s":BCI,"v":[],"dt":"gauge · colour"},
   {"n":"Annealed copper wire","a":"","d":"Traditional Japanese wire for conifers; work-hardens after application.","mk":"","y":"","s":BCI,"v":[],"dt":"gauge"},
   {"n":"Bonsai wire cutter","a":"","d":"Cutter with a rounded head that cuts wire flush without damaging the cambium.","mk":"","y":"","s":BCI,"v":[],"dt":"large or small · carbon or stainless steel"}]},
 {"n":"Jin pliers","a":"wire-bending pliers · deadwood pliers","d":"Heavy pliers with textured jaws for stripping bark to make jin and shari, and bending heavy wire.",
  "t":["straight","angled"],"s":BCI},
 {"n":"Root hook & rake","a":"root hook · root rake","d":"Hooks and rakes for opening the root ball and combing out old soil at repotting.",
  "t":["single prong","one, two or three teeth","with tweezer or spatula"],"s":BE,
  "x":[{"n":"Single-prong root hook","a":"","d":"Single prong for precise work near the trunk without tearing fine roots.","mk":"","y":"","s":BCI,"v":[],"dt":"handle length"},
   {"n":"Root rake","a":"","d":"Rake with one, two or three teeth that combs roots and removes old soil.","mk":"","y":"","s":BE,
    "v":[V("Bonsai root rake with tweezer","Kikuwa"),V("Bonsai rake","Kikuwa")],"dt":"number of teeth · tweezer end"}]},
 {"n":"Bonsai turntable","a":"bonsai lazy Susan · banshin","d":"Rotating stand that lets a tree be turned while pruning, wiring or repotting.",
  "t":["flat disc","tiltable","three-legged height-adjustable","lockable"],"s":BE,
  "x":[{"n":"Ball-bearing turntable","a":"","d":"Heavy ball-bearing turntable; Japanese models lock to stop movement while wiring.","mk":"","y":"","s":BCI,
     "v":[V("Turntable for bonsai care","Kikuwa"),V("Bonsai turntable set, 3 pcs","Kikuwa")],"dt":"diameter · lock"},
   {"n":"Tiltable wooden turntable","a":"","d":"Wooden turntable that tilts the tree as well as turning it.","mk":"","y":"","s":BE,"v":[],"dt":"size"},
   {"n":"Three-legged turntable","a":"","d":"Height-adjustable stand on three legs.","mk":"","y":"","s":BE,"v":[],"dt":"height range"}]},
]
brands=[
 {"n":"Masakuni","c":"Japan","f":"","seg":"Bonsai tools (premium)","d":"Leading Japanese maker of bonsai tools, credited with designing the concave cutter.","lines":["stainless steel tools"],"eras":[],"sig":["Straight-blade concave cutter"],"sc":["Bonsai"],"rel":["Kaneshin","Kikuwa"],"s":LAOS},
 {"n":"Kaneshin","c":"Japan","f":"1919","seg":"Bonsai tools","d":"Kaneshin Cutlery Mfg, maker of carbon and stainless steel bonsai tools in Yasuki-Hagane steel.","lines":["carbon steel","stainless steel"],"eras":[],"sig":["Straight-blade concave cutter","Spherical-jaw knob cutter"],"sc":["Bonsai"],"rel":["Masakuni"],"s":KAN},
 {"n":"Kikuwa","c":"Japan","f":"","seg":"Bonsai tools","d":"Japanese bonsai tool brand of shears, cutters, root rakes and turntables.","lines":[],"eras":[],"sig":["Root rake","Ball-bearing turntable"],"sc":["Bonsai"],"rel":["Masakuni"],"s":JT},
 {"n":"Joshua Roth","c":"","f":"","seg":"Bonsai tools","d":"Bonsai tool brand owned by Ken Carlson, known for durable professional-grade tools.","lines":[],"eras":["Ken Carlson, owner"],"sig":[],"sc":["Bonsai"],"rel":[],"s":POD},
 {"n":"Walsall Studio Ceramics","c":"United Kingdom","f":"1986","seg":"Bonsai pots (studio)","d":"Bonsai pottery formed by David Jones in the West Midlands.","lines":[],"eras":["David Jones, 1986–"],"sig":["European studio bonsai pot"],"sc":["Bonsai"],"rel":["Erin Pottery"],"s":EUP},
 {"n":"Erin Pottery","c":"United Kingdom","f":"1998","seg":"Bonsai pots (studio)","d":"Bristol pottery of Glyn and Victor Harris, selling hand-made bonsai pots since 1998.","lines":[],"eras":[],"sig":["European studio bonsai pot"],"sc":["Bonsai"],"rel":["Walsall Studio Ceramics"],"s":EUP},
 {"n":"Isabelia","c":"Czech Republic","f":"2000","seg":"Bonsai pots (studio)","d":"Czech bonsai pottery and supplier in Staré Město, specialised in bonsai since 2000.","lines":[],"eras":[],"sig":["European studio bonsai pot"],"sc":["Bonsai"],"rel":[],"s":EUP},
 {"n":"Gyozan","c":"Japan","f":"","seg":"Bonsai pots (Tokoname kiln)","d":"Tokoname kiln regarded as Japan's leading bonsai potter; hand-built pots without moulds.","lines":[],"eras":[],"sig":["Tokoname bonsai pot"],"sc":["Bonsai"],"rel":["Reiho","Yamaaki"],"s":V16},
 {"n":"Reiho","c":"Japan","f":"","seg":"Bonsai pots (Tokoname kiln)","d":"Tokoname kiln famous for glazed bonsai pots, its seal stamped on every base.","lines":[],"eras":[],"sig":["Tokoname bonsai pot"],"sc":["Bonsai"],"rel":["Gyozan","Koyo"],"s":V16},
 {"n":"Yamaaki","c":"Japan","f":"","seg":"Bonsai pots (Tokoname kiln)","d":"Tokoname kiln known for unglazed pots, later adding some glazed ones.","lines":[],"eras":[],"sig":["Tokoname bonsai pot"],"sc":["Bonsai"],"rel":["Gyozan"],"s":V13},
]
trads=[
 {"n":"Tokoname ware","g":"Ceramics & glass","r":"Tokoname, Aichi, Japan","p":"12th century–present","d":"One of Japan's Six Ancient Kilns; stoneware and redware including teapots and the best-known Japanese bonsai pots.",
  "tech":"coil-built and pressed stoneware; chambered climbing kilns (nobori-gama)","mat":"stoneware and red clay (redware)",
  "forms":["Bonsai pot","kyusu teapot","shochu server","incense burner"],"ctr":["Tōei kiln","Gyozan","Reiho","Yamaaki","Koyo","Shuho","Ikko","Yamada Jōzan III"],
  "auth":"kiln seal stamped on the base; Tokoname protected as a local brand since 2007","s":TOK},
 {"n":"Yixing zisha pottery","g":"Ceramics & glass","r":"Yixing, Jiangsu, China","p":"Song dynasty clay mining; teapots from Ming dynasty–present","d":"Unglazed stoneware of purple, red and beige Yixing clays, best known for teapots and other teaware.",
  "tech":"slab-built, coiled, thrown or slip-cast; usually unglazed, fired 1100–1200 °C","mat":"zisha (zi ni), zhu ni, duan ni clays",
  "forms":["Yixing clay teapot","tea pets","brush rest"],"ctr":["Yixing","Huanglongshan and Zhaozhuangshan clay mines","Ge Mingxiang"],
  "auth":"clay colour and texture; potter's seal on base (widely imitated since the 17th century)","s":YIX},
]
notes=("Kept the one old kind (Bonsai pot, old source) and added the seven planned tool kinds, all sourced from bonsai-bci.com and bonsaiempire.com tool guides. "
 "Concave cutter originator credited to Masakuni (with Murata) per retailer page; no Masakuni founding year found (official site returned 503), so left blank. "
 "Left out: Ryuga (no retrieved page about the brand), Bigei (no retrieved source), a Joshua Roth country/founding year and models (official site 503; only an owner podcast page fetched), "
 "Yixing as a named bonsai-pot archetype (no fetched page links Yixing clay to bonsai pots; Chinese pots covered by a generic archetype). No moves.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p="/home/user/Possession-Taxonomy/rebuild/work/C2/shelves/03_00.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
