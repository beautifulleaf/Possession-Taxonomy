import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,s,mk='',y='',v=(),dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
TL=W+'List_of_tomato_cultivars'; SEEDT=["packet","open-pollinated","F1 hybrid","heirloom","organic","pelleted"]
kinds=[
 {"n":"Tomato seed","a":"Solanum lycopersicum seed","d":"Packet of tomato seed sold for sowing, heirloom or F1 hybrid.",
  "t":SEEDT+["cherry","plum","beefsteak","bush (determinate)","cordon (indeterminate)"],"s":"https://www.rareseeds.com/store/plants-seeds","x":[
  X("'Brandywine'","Brandywine (Sudduth's)","Heirloom pink beefsteak on a tall potato-leaf vine, popularly rated among the best-tasting tomatoes.",W+"Brandywine_tomato",y="by 1886",
    v=[("Burpee catalogue listing","Burpee","1886","earliest seed-house listing named on the page"),("Brandywine (Sudduth's)","","","label used to separate the true strain from misnamed ones")],dt="fruit up to 1.5 lb · 80–100 days"),
  X("'Cherokee Purple'","","Heirloom dusky-rose beefsteak with green shoulders, one of the first 'black' tomatoes.",W+"Cherokee_Purple",y="1990",
    v=[("Named by Craig LeHoullier","","1990","from seed sent by John Green of Sevierville, Tennessee"),("Southern Exposure Seed Exchange catalogue","","1993",""),("'Cherokee Chocolate'","","1995","yellow-skinned offspring"),("'Cherokee Green'","","1997","green-fleshed offspring")]),
  X("'Sungold'","Sungold F1","Golden-orange F1 hybrid cherry tomato on an indeterminate vine; RHS Award of Garden Merit.","https://horticulture.co.uk/tomatoes/sungold/",mk="Tokita",y="early 1990s (UK)"),
  X("'Moneymaker'","","Red indeterminate heirloom with medium fruit, long a standard greenhouse tomato; blight prone.",TL),
  X("'Gardener's Delight'","","Red indeterminate heirloom with high yields of bite-sized fruit.",TL),
  X("'San Marzano'","","Red indeterminate heirloom plum tomato.",TL,dt="85 days"),
  X("'Black Krim'","","Purple-brown beefsteak heirloom from the Crimea, with a rich sweet flavour.",TL),
  X("'Green Zebra'","","Green-and-yellow striped open-pollinated tomato of about 3 oz.",TL,y="c. 1983",v=[("Bred by Tom Wagner","","c. 1983","Everett, Washington")]),
  X("'Mortgage Lifter'","","Large pink heirloom beefsteak popular in the Great Depression.",TL,y="1920s–30s",v=[("Estler strain","","","William Estler, West Virginia"),("Byles strain","","","M. C. Byles, West Virginia")]),
  X("'Better Boy' and 'Early Girl'","","Red indeterminate hybrids; 'Early Girl' was named to complement 'Better Boy'.",TL,v=[("'Better Boy'","","","70–80 days; disease codes F, V, N, T"),("'Early Girl'","","","63 days")]),
 ]},
 {"n":"Chilli & pepper seed","a":"Capsicum seed · hot pepper seed · sweet pepper seed","d":"Packet of chilli or sweet pepper seed sold for sowing.",
  "t":SEEDT+["sweet","mild","hot","superhot"],"s":W+"Jalapeño","x":[
  X("Jalapeño","","Medium-hot pepper named after Xalapa, Veracruz, typically 4,000–8,500 Scoville units.",W+"Jalapeño",
    v=[("'TAM Mild Jalapeño'","","","mild"),("'Early Jalapeño'","","",""),("'TAM Jaloro'","","","yellow"),("'NuMex Vaquero'","","","disease-resistant"),("'TAM Dulcito'","","","sweet, low heat")]),
  X("'Carolina Reaper'","HP22B","Superhot chilli bred by Ed Currie from a Naga and a habanero; Guinness hottest chilli from 2013 until 2023.",W+"Carolina_Reaper",y="2011",dt="average 1,641,183 SHU"),
 ]},
 {"n":"Squash & pumpkin seed","a":"Cucurbita seed · winter squash seed · courgette seed","d":"Packet of squash, pumpkin or courgette seed sold for sowing.",
  "t":SEEDT+["winter squash","summer squash","pumpkin","courgette"],"s":W+"Butternut_squash","x":[
  X("Butternut","butternut squash","Winter squash developed by Charles Leggett at Stow, Massachusetts, from a cross made in 1944.",W+"Butternut_squash",y="1944",v=[("'Waltham Butternut'","","","named in the same group on the page")]),
  X("'Crown Prince'","Crown Prince F1","Steel-grey-skinned winter squash with deep orange flesh, fruit 3–4 kg.","https://www.kingsseeds.com/products/Vegetable-Seeds/squash/squash-crown-prince-f1",v=[("Crown Prince F1","Kings Seeds","","seed-house listing with RHS award badge")]),
 ]},
 {"n":"Bean & pea seed","a":"legume seed · runner bean seed · French bean seed · pea seed","d":"Packet of bean or pea seed sold for sowing.",
  "t":SEEDT+["runner bean","French bean","broad bean","pole (climbing)","bush (dwarf)","pea","mangetout"],"s":W+"Runner_bean","x":[
  X("'Cherokee Trail of Tears'","Cherokee Black","Black-seeded pole bean used as snap or dry bean, carried by Cherokee families on the Trail of Tears (1838–39).","https://shop.seedsavers.org/cherokee-trail-of-tears-bean",y="1838–39",
    v=[("Seed Savers Exchange catalogue","Seed Savers Exchange","1995","shared by Dr John Wyche of Hugo, Oklahoma")],dt="85 days · 6-inch purple-tinged pods"),
  X("Runner bean cultivars","Phaseolus coccineus","Climbing runner beans grown for pods and seeds.",W+"Runner_bean",
    v=[("'Scarlet Emperor'","","",""),("'Painted Lady'","","",""),("'Japanese Runner'","","","sold as 'Akahana' or 'Shinshu runner'"),("'White Dutch Runner'","","",""),("'Judión de la Granja'","","","Spanish white bean from San Ildefonso")]),
 ]},
 {"n":"Root & brassica seed","a":"daikon radish seed · radish seed · carrot seed · cabbage seed","d":"Packet of root-crop or brassica seed, such as radish, daikon, carrot or cabbage, sold for sowing.",
  "t":SEEDT+["radish","daikon","carrot","beetroot","parsnip","cabbage","kale","broccoli"],"s":"https://shop.fifthseasongardening.com/products/radish-daikon-seeds","x":[
  X("Daikon","mooli · Japanese radish","Large white winter radish of East Asia.",W+"Daikon",
    v=[("'Sakurajima'","","","giant round Japanese daikon"),("Nerima daikon","","","specialty of Nerima, Tokyo"),("'Long White Icicle'","","","sold as seed in Britain"),("Watermelon radish","","","Chinese heirloom with rose-red centre"),("Korean radish (mu)","","","short, stout, green-shouldered")]),
 ]},
 {"n":"Salad & leaf seed","a":"lettuce seed · salad leaves seed","d":"Packet of lettuce or other salad-leaf seed sold for sowing.",
  "t":SEEDT+["butterhead","cos (romaine)","crisphead","loose-leaf","summercrisp (Batavian)","cut-and-come-again mix"],"s":W+"Lettuce","x":[
  X("'Little Gem'","","Dwarf compact romaine lettuce popular in the UK.",W+"Lettuce"),
  X("'Buttercrunch'","","Butterhead lettuce.",W+"Lettuce"),
  X("'Forellenschluss'","","Speckled romaine lettuce from Austria.",W+"Lettuce"),
 ]},
 {"n":"Herb seed","a":"culinary herb seed","d":"Packet of culinary herb seed, such as basil, parsley or coriander, sold for sowing.",
  "t":SEEDT+["basil","parsley","coriander","dill","chives"],"s":W+"Basil","x":[
  X("Basil","Ocimum basilicum","Sweet basil and its cultivars, the most sown culinary herb.",W+"Basil",
    v=[("'Genovese'","","","standard sweet basil for pesto"),("Thai basil","","","var. thyrsifolium"),("'Dark Opal'","","","dark-leaved"),("'Mrs. Burns' Lemon'","","","lemon-scented"),("'Napolitano'","","","very large leaves"),("Globe basil","","","small-leaved, 'Minimum'")]),
 ]},
 {"n":"Annual flower seed","a":"zinnia seed · cut-flower seed · bedding seed","d":"Packet of annual flower seed, such as zinnia or cosmos, sold for sowing.",
  "t":SEEDT+["cut-flower","bedding","dwarf","tall"],"s":"https://www.rareseeds.com/store/plants-seeds","x":[
  X("Benary's Giant zinnia","Zinnia elegans 'Benary's Giant'","Tall, large-flowered double Zinnia elegans strain, the Benary firm's first own variety and still sold.","https://laidbackgardener.blog/2018/09/22/benary-175-years-of-seeds/",mk="Benary",y="1859"),
  X("Profusion zinnia","Zinnia 'Profusion'","Hybrid group between Zinnia angustifolia and Z. elegans, in single and double forms.",W+"Zinnia"),
 ]},
 {"n":"Wildflower seed mix","a":"meadow seed mix · wildflower meadow mix","d":"Mixture of native wildflower and grass seed sold to sow a meadow or wildlife patch.",
  "t":["annual cornfield mix","perennial meadow mix","soil-specific mix (chalk, clay, wet)","flowering lawn mix","with grasses","flowers only"],
  "s":"https://www.habitataid.co.uk/collections/wildflower-seed-meadow-mixes-others/products/calcareous-meadow-seed-mix"},
 {"n":"Lawn seed","a":"grass seed","d":"Grass seed mixture sold to sow or repair a lawn.",
  "t":["ryegrass","fescue","bentgrass","Kentucky bluegrass","Bermuda grass","zoysia","shade mix","hard-wearing mix","fine ornamental mix","coated seed"],"s":W+"Lawn"},
 {"n":"Unrooted cutting","a":"succulent cutting · offset · node cutting · leaf cutting","d":"Unrooted cutting, offset or leaf of a plant sold for the buyer to root.",
  "t":["succulent offset","aroid node cutting","stem cutting","leaf cutting","root cutting"],"s":"https://mountaincrestgardens.com/succulent-cuttings-assorted-pack-10-50-plants-2-3/"},
]
K='knowledge'
brands=[
 {"n":"Burpee","c":"United States","f":"1876","seg":"Mainstream","kf":"vegetable seed","d":"W. Atlee Burpee & Co., Pennsylvania seed house; listed 'Brandywine' by 1886.","sig":["'Brandywine'"],"s":K},
 {"n":"Tokita","c":"Japan","seg":"Specialist","kf":"vegetable breeding","d":"Japanese vegetable seed breeder of the 'Sungold' cherry tomato.","sig":["'Sungold'"],"s":"https://horticulture.co.uk/tomatoes/sungold/"},
 {"n":"Benary","c":"Germany","f":"1843","seg":"Specialist","kf":"flower breeding","d":"Family-owned flower-seed breeder founded by Ernst Benary in Erfurt; bred the first F1 tomato 'Heterosis' (1927).","sig":["Benary's Giant zinnia"],"s":"https://laidbackgardener.blog/2018/09/22/benary-175-years-of-seeds/"},
 {"n":"Seed Savers Exchange","c":"United States","f":"1975","seg":"Institution & issuer","kf":"heirloom seed bank","d":"Iowa non-profit heirloom seed exchange and catalogue.","sig":["'Cherokee Trail of Tears'"],"s":K},
 {"n":"Kings Seeds","c":"United Kingdom","seg":"Mainstream","kf":"vegetable seed","d":"Essex seed house selling vegetable and flower seed by mail order.","s":"https://www.kingsseeds.com/products/Vegetable-Seeds/squash/squash-crown-prince-f1"},
 {"n":"Baker Creek","c":"United States","f":"1998","seg":"Specialist","kf":"heirloom seed","d":"Baker Creek Heirloom Seed Co. of Missouri, large catalogue of open-pollinated heirloom seed.","s":K},
 {"n":"Johnny's Selected Seeds","c":"United States","f":"1973","seg":"Professional & flagship","kf":"market-garden seed","d":"Maine employee-owned seed company serving market growers and gardeners.","s":K},
 {"n":"Thompson & Morgan","c":"United Kingdom","f":"1855","seg":"Mainstream","kf":"seed catalogue","d":"Ipswich seed and plant mail-order house.","s":K},
 {"n":"Suttons","c":"United Kingdom","f":"1806","seg":"Mainstream","kf":"seed","d":"Long-established English seed house, now based in Devon.","s":K},
 {"n":"Sakata","c":"Japan","f":"1913","seg":"Professional & flagship","kf":"vegetable & flower breeding","d":"Yokohama seed breeder supplying growers and garden seed houses worldwide.","s":K},
 {"n":"Takii","c":"Japan","f":"1835","seg":"Professional & flagship","kf":"vegetable & flower breeding","d":"Kyoto seed breeder supplying growers and garden seed houses worldwide.","s":K},
]
w('C3','07_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"All four old kinds kept: Tomato seed (Brandywine now an archetype), Daikon broadened to Root & brassica seed, Zinnia to Annual flower seed, Succulent cutting to Unrooted cutting; seven new kinds sourced from Wikipedia, a seed-house page and a meadow-mix product page. State Fair zinnia, Minowase daikon, Real Seeds and AAS winners not included: no retrieved page confirmed them (Daikon article lacks Minowase). Kings Seeds and Benary register entries cite retrieved pages; other seed houses from knowledge. Wildflower and lawn seed kept kind-level (QoL) with types only."})
