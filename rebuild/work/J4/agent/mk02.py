import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
ART="https://artsandculture.google.com/story/WAWRT-UbglE7KA"
PEACH=[x("Shimizu Hakuto","","1932",ART,"Okayama white peach, bagged on the tree and graded by sugar; a luxury summer gift fruit almost never exported.",
   [v("Hakuto","","1899","Parent variety bred by Jugoro Okubo from Shanghai honey peach seedlings"),
    v("Royal / King / Ace grades","","","Brix 12+ (Royal), over 11 (King), over 10 (Ace)")],dt="white skin and flesh · bagged on the tree · late July to early August"),
  x("Flat peach","","",W+"Flat_peach","Flattened white-fleshed peach of probable Chinese origin, also called Saturn, doughnut or paraguayo.",
   [v("Saturn (flat peach)","","","Old-data name")],a="Saturn · Doughnut · Pan tao")]
CH=[x("Bing","","1875",W+"Bing_cherry","Dark sweet cherry from Milwaukie, Oregon, raised by Seth Lewelling; the most popular sweet cherry in the US."),
 x("Rainier","","1952",W+"Rainier_cherry","Yellow-and-red premium sweet cherry bred by Harold Fogle at Washington State University from Bing x Van.",
   [v("Rainier","","1952","Old-data name")]),
 x("Lapins","","1983",W+"Lapins_cherry","Self-fertile late sweet cherry from Summerland, British Columbia, bred by Karlis Lapins; also sold as Cherokee.",a="Cherokee"),
 x("Sweetheart","","1994",W+"Sweetheart_cherry","Late self-fertile sweet cherry from Summerland, British Columbia, bred by David Lane."),
 x("Regina","","1998",W+"Regina_cherry","Rain-crack-resistant sweet cherry bred at the Jork Fruit Research Station, Germany."),
 x("Satonishiki","","1912","https://pd.jgic.jp/en/register/entry/30.html","Japanese premium sweet cherry from Higashine, Yamagata, over 80% of that area's output.",
   [v("東根さくらんぼ GI","","2017","Higashine Sakuranbo, Japanese GI covering Higashine City and parts of neighbouring towns")],a="Sato Nishiki")]
SC=[x("Montmorency","","",W+"Montmorency_cherry","Light-red Amarelle sour cherry from near Paris; the most popular sour cherry in the US and Canada."),
 x("Morello","","",W+"Prunus_cerasus","Dark-red sour cherry group, the main commercial sour cherry in Central Europe."),
 x("Oblačinska","","",W+"Obla%C4%8Dinska","Serbian landrace sour cherry, the predominant variety in Serbia and Montenegro, grown for processing.")]
PL=[x("Victoria","","1844",W+"Victoria_plum","English egg plum with yellow flesh and red mottled skin, self-fertile and a household favourite."),
 x("Santa Rosa","","",W+"Prunus_salicina","Luther Burbank's Japanese-type plum, large red-purple fruit, ripening midseason.",
   [v("Santa Rosa","","","Old-data name"),v("Late Santa Rosa","","","Old-data name")]),
 x("Pluot","","",W+"Pluot","Plum-dominant plum-apricot hybrid bred by Floyd Zaiger, mostly Japanese plum parentage with a smooth skin.",
   [v("Flavor King","","","Pluot cultivar named on Wikipedia")],dt="plumcot, aprium, pluot are different hybrid generations")]
UME=[x("Nankoume","","",W+"Prunus_mume","Very popular Japanese yabai-type ume, used mainly for umeboshi.",a="Nanko-ume")]
kinds=[
K("Peach","Fresh peach, white or yellow fleshed, clingstone or freestone, with Japanese premium and flat forms.","https://plu.pro/commodity/peaches",PEACH,["Amsden June","Avalon Pride","de Vigne (Sanguine)","Pesca di Verona PGI","Pesca di Leonforte PGI","Pescabivona PGI","Pêssego da Cova da Beira PGI","Ροδάκινα Νάουσας PDO","あら川の桃 GI","Ramgarh Nainital Aadu GI"],["yellow","white","flat","clingstone","freestone"]),
K("Nectarine","Fresh smooth-skinned nectarine, a fuzzless peach.","https://plu.pro/commodity/nectarine",None,["Nectavigne"],["yellow","white","clingstone","freestone"]),
K("Cherry","Fresh sweet cherry, organised by cultivar with its protected origin.","https://plu.pro/commodity/cherries",CH,["Skylar Rae (Tip Top)","Timberline (HR87)","Audra Rose (RL 100)","Ciliegia di Vignola PGI","Ciliegia dell'Etna PGI","Cereza del Jerte PDO","Cerise des coteaux de Vaucluse PGI","Cereja da Cova da Beira PGI","Ciliegia di Marostica PGI","Szomolyai rövidszárú fekete cseresznye"],["sweet"]),
K("Sour cherry","Fresh Prunus cerasus (Morello, Montmorency, amarena), bought to cook or process.",W+"Prunus_cerasus",SC,["Wiśnia nadwiślanka PDO","Újfehértói meggy"],a="Tart cherry · Morello"),
K("Plum","Fresh plum, European or Japanese type, with interspecific hybrids and protected regional plums.","https://plu.pro/commodity/plums",PL,["Angeleno","Black Amber (Blackamber)","President","Italian Prune (Sugar)","Mirabelle de Lorraine PGI","Stromberger Pflaume PDO","Ameixa d'Elvas PDO","Susina di Dro PGI","The Vale of Clwyd Denbigh Plum PGI","Śliwka szydłowska PDO","Wickson","김천자두"],["European","Japanese","greengage","damson","mirabelle","interspecific"]),
K("Apricot","Fresh apricot, including protected regional apricots.","https://plufinder.com/plu/3422",None,["Wachauer Marille PDO","Abricots rouges du Roussillon AOP","Abricot des Baronnies PGI","Gönci kajszibarack PGI","Albicocche del Vesuvio Crisommole","Ladakh Raktsey Karpo Apricot GI","Scillato Apricot","彭阳红梅杏"]),
K("Ume","Fresh Prunus mume fruit, sold to pickle or steep.","https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",UME,["氷見稲積梅 GI"]),
]
# fix names for plum m: use old exact names
old_plum={"Black Amber (Blackamber)":"Blackamber"}
for k in kinds:
    if k["n"]=="Plum": k["m"]=[[old_plum.get(m[0],m[0]),""] for m in k["m"]]
notes="Nectarine, apricot kept flat with old models: no cultivar pages retrieved (Prunus armeniaca page names no cultivars; Elberta, Redhaven, Bergeron, Hunza, Akatsuki, Kawanakajima Hakuto unconfirmed so left out). Benishuho and Cerise de Vignola cultivar link not retrieved, left as flat GI. Nanko-ume Wakayama link not confirmed by page, left out. Dropped long tails of Santa Rosa-series, Cherry and plum cultivar lists. Pluot trademark owner not confirmed."
urls=[W+p for p in ["Flat_peach","Bing_cherry","Rainier_cherry","Lapins_cherry","Sweetheart_cherry","Regina_cherry","Victoria_plum","Prunus_salicina","Prunus_mume","Montmorency_cherry","Obla%C4%8Dinska","Prunus_cerasus","Pluot","Prunus_armeniaca"]]+["https://pd.jgic.jp/en/register/entry/30.html",ART]
write("00_02",kinds,[],[],notes,urls)
