import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='pot size · height',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
A=lambda n,d="":(n,"","",d)
HM,HP,HA=W+"Hydrangea_macrophylla",W+"Hydrangea_paniculata",W+"Hydrangea_arborescens"
CJ=W+"Camellia_japonica"; AP=W+"Acer_palmatum"; PS=W+"Prunus_serrulata"; CL=W+"Clematis"; RH=W+"Rhododendron"
kinds=[
 {"n":"Hydrangea","a":"hortensia · mophead · lacecap","d":"Living shrub of the genus Hydrangea, grown for large heads of flowers that in bigleaf types turn blue on acid soil and pink on alkaline.",
  "t":["mophead","lacecap","panicle","smooth","climbing"],"s":"https://www.starkbros.com/products/fruit-trees","x":[
  X("Hydrangea macrophylla","bigleaf hydrangea · hortensia","Japanese coastal shrub with over 500 mophead and over 20 lacecap cultivars; flower colour follows soil pH via aluminium.",HM,
    v=[A("'Nikko Blue'","cold-hardy mophead, pink to blue"),A("'Bailmer'","marketed as Endless Summer; perpetual-flowering mophead"),A("'Mariesii Lilacina'","lacecap; "+AGM),A("'Ayesha'","mophead with cupped lilac-like florets"),A("'Altona'",AGM),A("'Europa'",AGM),A("'Zorro'","blue lacecap; "+AGM),A("'Lanarth White'","white lacecap; "+AGM)],dt="mophead or lacecap · flower colour (pH) · pot size"),
  X("'Limelight'","Hydrangea paniculata 'Limelight'","Panicle hydrangea cultivar protected by plant breeders' rights; "+AGM+".",HP,dt="height · pot size"),
  X("Hydrangea paniculata","panicled hydrangea","East Asian shrub with conical flower panicles.",HP,
    v=[A("'Grandiflora'"),A("'Phantom'",AGM),A("Pinky-Winky = 'Dvppinky'",AGM),A("Pink Diamond = 'Interhydia'",AGM),A("'Big Ben'",AGM),A("'Silver Dollar'",AGM),A("'Praecox'","early flowering")]),
  X("'Annabelle'","Hydrangea arborescens 'Annabelle'","Smooth hydrangea with large rounded white heads; "+AGM+".",HA,
    v=[A("'Incrediball' ('Abetwo')","stronger stems"),A("Invincibelle","pink-flowered cultivars")],dt="height · pot size"),
  ]},
 {"n":"Rhododendron & azalea","a":"Rhododendron · azalea · rhodie","d":"Living rhododendron or azalea, an acid-soil shrub of the genus Rhododendron; azaleas have smaller, funnel-shaped flowers usually with five stamens.",
  "t":["evergreen rhododendron","deciduous azalea","evergreen azalea","dwarf"],"s":RH,"x":[
  X("Exbury azaleas","Exbury hybrids","Deciduous azaleas bred by Lionel de Rothschild at the Exbury Estate from the Knap Hill hybrids.",RH,v=[A("Knap Hill hybrids","raised by Anthony Waterer at Knap Hill Nursery")]),
  X("Kurume azaleas","","Japanese-raised evergreen azalea hybrids.",RH),
  X("Satsuki azaleas","","Japanese-raised evergreen azaleas, originally for bonsai.",RH),
  X("Ghent azaleas","Gandavense","Belgian-raised deciduous azalea hybrids.",RH),
  X("Loderi hybrids","","Fragrant rhododendrons from R. fortunei × R. griffithianum.",RH),
  X("PJM hybrids","","Hardy rhododendrons from R. carolinianum × R. dauricum, named after Peter J. Mezitt of Weston Nurseries.",RH),
  X("'Nova Zembla'","","Rhododendron hybrid shown in American nursery cultivation.",RH),
  X("Inkarho","","Lime-tolerant rootstock for rhododendrons, shown at Chelsea in 2011.",RH,y="2011"),
  ]},
 {"n":"Camellia","a":"tsubaki","d":"Living shrub of the genus Camellia, evergreen with glossy leaves and winter to spring flowers; thousands of cultivars, mostly of C. japonica.",
  "t":["single","semi-double","anemone (elegans) form","formal double","informal double"],"s":"https://www.paramountplants.co.uk/plants-to-buy-online.html/6/","x":[
  X("Camellia japonica","common camellia · Japanese camellia","Chinese and Japanese forest shrub with more than 2,000 cultivars.",CJ,
    v=[A("'Elegans'","large pink, anemone form"),A("'Alba Plena'","white formal double; brought to England in 1792"),A("'Adolphe Audusson'","red; "+AGM),A("'Bob Hope'","deep red irregular semi-double; "+AGM),A("'Kingyo-tsubaki'","fishtail camellia"),A("'Black Lace'","formal double"),A("'Debutante'",""),A("'Nuccio's Jewel'",AGM)],dt="flower form · colour · pot size"),
  ],"m":[["Camellia japonica 'Lady Campbell'",""],["Camellia japonica 'Kramer's Supreme'",""],["Camellia japonica 'Dr Burnside'",""],["Camellia japonica 'Comte de Gomer'",""],["Camellia japonica 'Bonomiana'",""],["Camellia japonica 'Blood of China'",""],["Camellia sasanqua 'Kanjiro'",""],["Camellia reticulata 'Mary Williams'",""]]},
 {"n":"Japanese maple","a":"Acer palmatum · momiji · laceleaf maple","d":"Living Japanese maple tree (Acer palmatum and allies), with over 1,000 cultivars grown for leaf shape and colour.",
  "t":["palmate","dissectum (laceleaf)","linearilobum","coral-bark"],"s":"https://www.arundelarboretum.co.uk/products/acer-palmatum-bloodgood-bloodgood-japanese-maple-100-150cm-5lt","x":[
  X("'Bloodgood'","","Vigorous large selection of 'Atropurpureum' with wine-red leaves; "+AGM+".",AP,dt="height · pot size"),
  X("'Osakazuki'","","Green-leaved tree-like maple of about 4 m with spectacular autumn colour; "+AGM+".",AP),
  X("'Sango-kaku'","'Senkaki' · coral-bark maple","Maple with pinkish-red bark; "+AGM+".",AP),
  X("'Atropurpureum'","","Wine-red maple; the original clone is lost and the name covers similar seedlings.",AP),
  X("Dissectum maples","laceleaf · filigree","Cultivars with finely dissected lace-like leaves.",AP,v=[A("'Seiryu'",AGM),A("'Garnet'",AGM),A("'Crimson Queen'",AGM)]),
  X("Other notable cultivars","","Further Japanese maple cultivars named on Wikipedia.",AP,v=[A("'Katsura'","yellow-green leaves tipped orange; "+AGM),A("'Butterfly'","variegated white"),A("'Beni-maiko'",AGM)]),
  ]},
 {"n":"Flowering cherry","a":"sakura · Japanese cherry · ornamental cherry","d":"Living ornamental cherry tree (Prunus) grown for its spring flowers, chiefly the Japanese Sato-zakura cultivars.",
  "t":["upright","weeping","columnar","single","double"],"s":"https://www.arundelarboretum.co.uk/products/prunus-serrulata-kanzan-100-120cm-7lt","x":[
  X("'Kanzan'","'Sekiyama' · 'Kwanzan'","Double pink Sato-zakura with bronze young leaves; the most popular blossom cherry in Europe and North America; "+AGM+".",PS,dt="height · standard or bush"),
  X("'Taihaku'","'Tai Haku' · great white cherry","Single white cherry with flowers up to 8 cm; lost in Japan and returned there by Collingwood Ingram in 1932; "+AGM+".",PS),
  X("'Shirotae'","Mt Fuji cherry","Semi-double pure white cherry with a low, broad, near-horizontal crown; "+AGM+".",PS),
  X("'Somei-yoshino'","Yoshino cherry","Cherry named after Somei village in Tokyo, developed in the mid to late 19th century.",W+"Cherry_blossom"),
  X("Other Sato-zakura","","Further Sato-zakura cultivars.",PS,v=[A("'Amanogawa'","columnar, pale pink; "+AGM),A("'Ukon'","cream-yellow; Edo period; "+AGM),A("'Fugenzo' ('Shiro-fugen')","double pink fading; "+AGM),A("'Kiku-shidare'","Cheal's weeping cherry")]),
  ]},
 {"n":"Magnolia","a":"saucer magnolia · star magnolia · tulip tree","d":"Living ornamental magnolia tree or shrub, grown for large spring flowers.",
  "t":["tree","shrub","deciduous","evergreen"],"s":W+"Magnolia_×_soulangeana","x":[
  X("Magnolia × soulangeana","saucer magnolia","Hybrid of M. denudata and M. liliiflora raised by Étienne Soulange-Bodin near Paris in 1820.",W+"Magnolia_×_soulangeana",y="1820",
    v=[A("'Brozzonii'",AGM),A("'Speciosa'"),A("'André Leroy'")]),
  X("Magnolia stellata","star magnolia","Japanese shrub from the Ise Bay area with star-shaped flowers.",W+"Magnolia_stellata",
    v=[A("'Royal Star'",AGM),A("'Jane Platt'",AGM),A("'Centennial'",AGM),A("f. rosea","pink form")]),
  ]},
 {"n":"Lilac","a":"Syringa · common lilac · French lilac","d":"Living lilac shrub of the genus Syringa, grown for scented spring flower panicles.",
  "t":["single","double"],"s":W+"Syringa_vulgaris","x":[
  X("Syringa vulgaris","common lilac","Balkan shrub widely cultivated for scented flowers.",W+"Syringa_vulgaris",
    v=[A("'Sensation'","single purple edged white; "+AGM),A("'Katherine Havemeyer'","double lilac; "+AGM),A("'Primrose'","double pale yellow; "+AGM),A("'Charles Joly'","")]),
  X("French lilacs","Lemoine hybrids","Over 153 cultivars introduced by Victor Lemoine of Nancy between 1876 and 1927, with deeper colours and many doubles.",W+"Syringa_vulgaris",y="1876",v=[A("'Madame Lemoine'","double white; "+AGM)]),
  ]},
 {"n":"Lavender","a":"Lavandula · English lavender · lavandin","d":"Living lavender plant (Lavandula), an aromatic shrub with spikes of purple, pink or white flowers.",
  "t":["dwarf","semi-dwarf","giant","lavandin"],"s":"https://www.crocus.co.uk/plants/_/","x":[
  X("'Hidcote'","Lavandula angustifolia 'Hidcote'","Semi-dwarf English lavender, 40–50 cm, deep violet-blue; named after Hidcote Manor; "+AGM+".",W+"Lavandula_angustifolia",v=[A("'Hidcote Superior'","dwarf")],dt="hedge or specimen · pot size"),
  X("'Munstead'","Lavandula angustifolia 'Munstead'","Dwarf English lavender about 30 cm, named after Gertrude Jekyll's Munstead Wood.",W+"Lavandula_angustifolia",dt="hedge or specimen · pot size"),
  X("Lavandula angustifolia","English lavender · true lavender","Mediterranean lavender species.",W+"Lavandula_angustifolia",
    v=[A("'Imperial Gem'",AGM),A("'Folgate'"),A("'Vera'","thought to be the original species lavender"),A("'Nana Alba'","dwarf white; "+AGM),A("'Jean Davis'","pale pink")]),
  X("Lavandin","Lavandula × intermedia","Hybrids of L. angustifolia and spike lavender, flowering later.",W+"Lavandula_angustifolia",v=[A("'Hidcote Giant'","90–100 cm; "+AGM)]),
  ]},
 {"n":"Clematis","a":"old man's beard · virgin's bower","d":"Living climber of the genus Clematis (about 380 species), grown in three pruning groups by flowering time.",
  "t":["group 1 (no pruning)","group 2 (early large-flowered)","group 3 (late-flowering)"],"s":"https://www.rootsplants.co.uk/collections/cottage-garden-plants?page=4","x":[
  X("'Nelly Moser'","","Early large-flowered clematis, white with pink stripes; best in light shade.",CL),
  X("'Jackmanii'","","Late large-flowered purple clematis, a garden staple since 1862.",CL,y="1862"),
  X("'The President'","","Early large-flowered blue clematis.",CL),
  X("Clematis montana","mountain clematis · Himalayan clematis","Vigorous spring climber of Asian mountains.",W+"Clematis_montana",v=[A("var. grandiflora",AGM),A("var. rubens"),A("'Elizabeth'","pale pink"),A("'Tetrarose'","deep pink; "+AGM),A("'Broughton Star'","double deep pink; "+AGM),A("'Mayleen'","pale pink")]),
  X("Clematis armandii","evergreen clematis","Chinese evergreen with fragrant white spring flowers.",W+"Clematis_armandii",v=[A("'Apple Blossom'",AGM),A("'Snowdrift'"),A("'Hendersonii Rubra'","pink")]),
  X("Clematis viticella","","Compact late-flowering species listed by Linnaeus in 1753.",CL,v=[A("'Alba Luxurians'"),A("'Purpurea Plena Elegans'")]),
  X("Clematis alpina","Atragene group","Spring climber with bell-shaped flowers.",CL),
  ]},
 {"n":"Wisteria","a":"fuji · wistaria","d":"Living wisteria, a long-lived twining climber with hanging racemes of spring flowers.",
  "t":["standard","trained on wall","pergola"],"s":W+"Wisteria_floribunda","x":[
  X("Wisteria sinensis","Chinese wisteria","Chinese climber twining anticlockwise, up to 30 m.",W+"Wisteria_sinensis",v=[A("'Prolific'",AGM),A("'Amethyst'",AGM),A("'Jako'","white; "+AGM),A("'Alba'","found by Robert Fortune, 1844")]),
  X("Wisteria floribunda","Japanese wisteria · fuji","Japanese climber twining clockwise, with long racemes.",W+"Wisteria_floribunda",
    v=[A("'Shiro-noda'","white; "+AGM),A("'Kokuryu'","violet; "+AGM),A("'Hon-beni'","pale rose; "+AGM),A("'Domino'",AGM),A("'Lawrence'",AGM),A("'Macrobotrys'","racemes 1 m or longer"),A("'Longissima Kyushaku'","from the Ushijima-no-fuji"),A("'Kuchibeni'","pink")]),
  X("Wisteria × valderi 'Burford'","","Hybrid with Japanese wisteria as a parent; "+AGM+".",W+"Wisteria_floribunda"),
  ]},
 {"n":"Honeysuckle","a":"Lonicera · woodbine","d":"Living honeysuckle of the genus Lonicera, mostly scented twining climbers with some shrubs.",
  "t":["climbing","shrubby","winter-flowering"],"s":W+"Lonicera","x":[
  X("Lonicera periclymenum","common honeysuckle · woodbine","European twining climber.",W+"Lonicera_periclymenum",v=[A("'Graham Thomas'",AGM),A("'Serotina'",AGM)]),
  X("Lonicera × heckrottii 'Gold Flame'","golden flame honeysuckle","Climbing honeysuckle; "+AGM+".",W+"Lonicera"),
  X("Lonicera sempervirens","trumpet honeysuckle · coral honeysuckle","North American climber attractive to hummingbirds.",W+"Lonicera"),
  X("Lonicera fragrantissima","winter honeysuckle","Winter-flowering shrubby honeysuckle.",W+"Lonicera",v=[A("L. × purpusii 'Winter Beauty'",AGM)]),
  X("Lonicera nitida","","Small-leaved shrub used for low hedges.",W+"Lonicera"),
  ]},
]
brands=[
 {"n":"Raymond Evison","c":"Guernsey","f":"1985","seg":"Specialist","kf":"clematis breeding","d":"Clematis breeder whose Guernsey Clematis Nursery is the world's leading producer of young clematis, breeding with Poulsen Roser.","rel":["Poulsen Roser"],"s":"https://clematisontheweb.org/raymond-j-evison/"},
 {"n":"Proven Winners","c":"United States","seg":"Mainstream","kf":"branded ornamental plants","d":"American brand of ornamental plants sold through garden centres.","s":"knowledge"},
]
trads=[{"n":"Sakura and hanami","g":"Plants & gardens","r":"Japan","p":"Heian period (794–1185) onward","d":"Japanese culture of flowering cherries and blossom viewing, with hundreds of Sato-zakura cultivars.","tech":"selection and grafting of cherry cultivars; blossom-viewing parties","mat":"Prunus speciosa-based hybrids, P. serrulata","forms":["Sato-zakura","Somei-yoshino","weeping cherry"],"ctr":["Somei village (Tokyo)","Jindai-zakura","Usuzumi-zakura","Miharu Takizakura","Collingwood Ingram"],"auth":"Cultivar names follow the Japanese Sato-zakura group; check grafted named cultivar rather than seedling.","s":W+"Cherry_blossom"}]
w('C3','05_01',{"kinds":kinds,"brands":brands,"traditions":trads,"notes":"All six old kinds kept with old s; five new kinds sourced to Wikipedia. Camellia: old 12-SKU list trimmed — cultivars on Wikipedia became versions; six unconfirmed old japonica names kept in m from old data. Proven Winners: Wikipedia page 404, knowledge stub, no cultivars attributed (not confirmed on retrieved pages). Evison Boulevard/Garland series left out (search snippet only). Rhododendron Yakushimanum hybrids and 'Belgica' honeysuckle left out (not on retrieved pages)."})
