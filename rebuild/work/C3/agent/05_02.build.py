import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='pot size · height',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
A=lambda n,d="",y="":(n,"",y,d)
CR="https://www.crocus.co.uk/plants/_/"
HO,PE,PL,PS=W+"Hosta",W+"Peony",W+"Paeonia_lactiflora",W+"Paeonia_suffruticosa"
IG,IE,IS=W+"Iris_germanica",W+"Iris_ensata",W+"Iris_sibirica"
DY="https://www.waltersgardens.com/article.php?ID=98"; AIS="https://wiki.irises.org/Main/InfoAwards2025"
HE,DE,GE,SN,HU=W+"Hemerocallis",W+"Delphinium",W+"Geranium",W+"Salvia_nemorosa",W+"Heuchera"
MS,CA,CE=W+"Miscanthus_sinensis",W+"Calamagrostis_×_acutiflora",W+"Cenchrus_alopecuroides"
PN,FA,BA=W+"Phyllostachys_nigra",W+"Fargesia",W+"Bamboo"
kinds=[
 {"n":"Hosta","a":"plantain lily · giboshi","d":"Living herbaceous perennial of the genus Hosta, a shade plant grown for its leaves; the American Hosta Society registers over 7,200 names.",
  "t":["giant","large","medium","small","miniature","blue","gold","variegated"],"s":CR,"x":[
  X("'Sum and Substance'","","Huge hosta with chartreuse-yellow leaves; "+AGM+".",HO,dt="leaf colour · clump size · pot size"),
  X("'Frances Williams'","H. sieboldiana 'Frances Williams'","Large blue-green hosta with a gold margin; "+AGM+".",HO),
  X("'Blue Angel'","H. sieboldiana 'Blue Angel'","Large blue-leaved sieboldiana hosta; "+AGM+".",HO),
  X("Hosta sieboldiana","","Japanese species whose glaucous coating makes the leaves look blue.",HO,v=[A("var. elegans",AGM)]),
  X("Hosta plantaginea","August lily","The only strongly fragrant species, with white evening-opening flowers up to 10 cm long.",HO,v=[A("var. japonica",AGM)]),
  X("Tardiana Group","H. × tardiana","Blue-leaved hybrids.",HO,v=[A("'Halcyon'",AGM),A("'June'","blue-green with creamy centre; "+AGM),A("'El Niño'",AGM)]),
  X("Variegated cultivars","","Widely grown edged and centred variegated hostas.",HO,v=[A("'Francee'","green with white edge; "+AGM),A("'Gold Standard'","yellow with green edge; discovered by Pauline Banyai"),A("'Patriot'",AGM),A("'Wide Brim'",AGM),A("'Undulata'","green with white centre"),A("'Guacamole'","fragrant")]),
  X("Miniature hostas","","Small cultivars for pots and troughs.",HO,v=[A("'Blue Mouse Ears'",AGM),A("'Cracker Crumbs'",AGM),A("'Shining Tot'",AGM)]),
  X("Other AGM hostas","","Further cultivars holding the "+AGM+".",HO,v=[A("'Krossa Regal'"),A("'Royal Standard'"),A("'Sagae'"),A("'Golden Tiara'"),A("'Fire Island'"),A("'Orange Marmalade'"),A("'Stained Glass'"),A("'Praying Hands'")]),
  ]},
 {"n":"Peony","a":"Paeonia · paeony · moutan","d":"Living peony plant (Paeonia), herbaceous or tree peony; the American Peony Society registers over 7,000 cultivars.",
  "t":["herbaceous","tree (moutan)","intersectional (Itoh)","single","semi-double","Japanese","anemone","bomb","double"],"s":CR,"x":[
  X("'Sarah Bernhardt'","P. lactiflora 'Sarah Bernhardt'","Double pink lactiflora peony that dominates Dutch cut-flower sales; "+AGM+".",PE,dt="root grade (eyes) · pot size"),
  X("'Bowl of Beauty'","P. lactiflora 'Bowl of Beauty'","Anemone-flowered pink and cream lactiflora peony; "+AGM+".",PE),
  X("Paeonia lactiflora","Chinese peony · common garden peony","Herbaceous species behind most cut-flower and garden cultivars.",PL,
    v=[A("'Duchesse de Nemours'","double white; "+AGM),A("'Festiva Maxima'","double white; "+AGM),A("'Monsieur Jules Elie'","double pink; "+AGM),A("'Felix Crousse'","double deep pink; "+AGM),A("'Laura Dessert'",AGM),A("'Whitleyi Major'","single white; "+AGM),A("'Miss America'",AGM),A("'James Kelway'","semi-double")]),
  X("'Coral Charm'","","Semi-double salmon-pink herbaceous peony; "+AGM+".",PE),
  X("Paeonia officinalis","common peony · European peony","European species grown since the fifteenth century, first for medicine.",PE,v=[A("P. × festiva 'Rubra Plena'","bomb red; "+AGM)]),
  X("Itoh peonies","intersectional peony","Herbaceous peonies with tree-peony leaves, first bred by Toichi Itoh of Tokyo from 'Alice Harding' pollen on 'Katoden'.",PS,y="1948",
    v=[A("'Bartzella'","double yellow; "+AGM),A("'Yellow Crown'","early Itoh"),A("'Yellow Dream'","early Itoh"),A("'Yellow Emperor'","early Itoh"),A("'Yellow Heaven'","early Itoh")]),
  X("Paeonia suffruticosa","moutan · mudan · tree peony","Chinese woody peony, ornamental since the Northern and Southern Dynasties; Heze alone grows over 1,300 varieties.",PS,dt="grafted or own-root · age · flower form"),
  X("Lemoine tree peonies","P. × lemoinei","French yellow-flowered tree peony hybrids from P. delavayi crosses.",PS,
    v=[A("'Chromatella'","double yellow","1928"),A("'Alice Harding'","double; parent of the Itoh peonies","1935"),A("'Sang Lorraine'","semi-double","1939"),A("'High Noon'","semi-double lemon-yellow; "+AGM)]),
  ]},
 {"n":"Iris","a":"flag · fleur-de-lis","d":"Living rhizomatous garden iris, mainly bearded, Siberian and Japanese irises; the American Iris Society is the registrar.",
  "t":["tall bearded","border bearded","intermediate bearded","standard dwarf bearded","miniature dwarf bearded","reblooming","Siberian","Japanese (hanashōbu)","Louisiana","spuria","Pacific Coast"],"s":IG,"x":[
  X("Iris × germanica","bearded iris · German iris","Hybrid rhizomatous perennial up to 120 cm, in colours from near-black to white and red; some rebloom in autumn.",IG,
    v=[A("'Amas'","key parent of modern tetraploid tall bearded irises"),A("'Black Prince'"),A("'Gypsy Queen'"),A("'Dominion'")],dt="class (TB, BB, IB, SDB, MDB) · colour pattern · rhizome"),
  X("Dykes Medal tall bearded irises","American Dykes Medal","Irises winning the American Iris Society's highest annual award, mostly tall bearded.",DY,
    v=[A("'Royston Rubies'","2025 American Dykes Medal; tall bearded","2025"),A("'Montmartre'","","2017"),A("'Paul Black'","","2010"),A("'Golden Panther'","","2009"),A("'Splashacata'","","2005"),A("'Stairway to Heaven'","","2000"),A("'Before The Storm'","","1996"),A("'Edith Wolford'","","1993"),A("'Jesse's Song'","","1990")]),
  X("Iris sibirica","Siberian iris · Siberian flag","Clump-forming beardless iris; several hundred cultivars are registered with the American Iris Society.",IS,
    v=[A("'Butter and Sugar'","white standards, yellow falls; "+AGM),A("'Cambridge'",AGM,"1964"),A("'Silver Edge'",AGM),A("'Ruffled Velvet'",AGM),A("'Caesar's Brother'"),A("'Sultan's Ruby'","deep magenta")] if False else
      [A("'Butter and Sugar'","white standards, yellow falls; "+AGM),A("'Cambridge'",AGM,"1964"),A("'Silver Edge'",AGM),A("'Ruffled Velvet'",AGM),A("'Sultan's Ruby'","deep magenta"),A("'Ego'","rich blue"),A("'Dreaming Spires'","","1964")]),
  X("Iris ensata","Japanese iris · hanashōbu · I. kaempferi","Japanese water iris grown in Edo, Higo and Ise strains.",IE,
    v=[A("Edo strain","Tokyo"),A("Higo strain","Kumamoto"),A("Ise strain","Mie"),A("'Rose Queen'",AGM),A("'Variegata'",AGM),A("'The Great Mogul'",AGM),A("'Narihira'")]),
  ]},
 {"n":"Daylily","a":"Hemerocallis · day lily","d":"Living Hemerocallis plant, each flower lasting a day; over 100,000 cultivars are registered by the American Daylily Society.",
  "t":["diploid","tetraploid","spider","double (polymerous)","evergreen","dormant","rebloomer"],"s":HE,"x":[
  X("'Hyperion'","","Large bright yellow cultivar of the 1920s that revived interest in daylilies.",HE,y="1920s"),
  X("Stout Silver Medal daylilies","Stout Medal","Cultivars winning the highest US daylily award, named after breeder Arlow Burdette Stout.",HE,v=[A("'Webster's Pink Wonder'","Stout Silver Medal","2014")]),
  X("'Kwanzo'","H. fulva 'Kwanzo'","Triple-flowered triploid daylily.",HE),
  X("Spider daylilies","","Narrow-petalled daylilies.",HE,v=[A("'Ruby Spider'"),A("'Spider Man'",AGM)]),
  X("Other AGM daylilies","","Cultivars holding the "+AGM+".",HE,v=[A("'Stafford'"),A("'Tuxedo Junction'")]),
  ]},
 {"n":"Delphinium","a":"larkspur","d":"Living perennial delphinium grown for tall spikes of blue, white, mauve or pink flowers; most garden hybrids derive from D. elatum.",
  "t":["Elatum","Pacific hybrid","New Millennium","single","double"],"s":DE,"x":[
  X("Elatum hybrids","D. elatum","Tall perennial hybrids bred since the 19th century, led by Victor Lemoine in France.",DE,y="19th century",
    v=[A("'Faust'","blue, black eye; 1.8 m; "+AGM),A("'Galileo'","blue; "+AGM),A("'Langdon's Blue Lagoon'",AGM),A("'Blue Dawn'","violet; 2.2 m; "+AGM),A("'Atholl'","white; "+AGM),A("'Kennington Classic'","white, yellow eye; "+AGM),A("'Rosemary Brock'","pink; "+AGM),A("'Can-can'","double; "+AGM)],dt="height · flower colour · eye"),
  X("Pacific Giant hybrids","Pacific hybrids","Delphiniums developed by Reinelt in the United States, 1.2–1.8 m tall.",DE),
  X("New Millennium hybrids","Millennium series","Delphiniums bred by Dowdeswell's in New Zealand, better in warmer climates.",DE,v=[A("'Sweethearts'","pink; 2.5 m; "+AGM)]),
  ]},
 {"n":"Hardy geranium","a":"cranesbill · Geranium","d":"Living perennial of the genus Geranium, long-lived and mounding, distinct from tender pelargoniums.",
  "t":["mounding","trailing","rock garden","evergreen"],"s":GE,"x":[
  X("Rozanne","'Gerwat'","Violet-blue cranesbill protected by plant breeders' rights; "+AGM+".",GE,dt="pot size"),
  X("'Johnson's Blue'","","Hybrid of G. himalayense and G. pratense.",GE),
  X("Geranium × oxonianum","","Hybrid cranesbill group.",GE,v=[A("'Wargrave Pink'",AGM),A("'A. T. Johnson'",AGM)]),
  X("Other AGM cranesbills","","Further hybrid cranesbills holding the "+AGM+".",GE,v=[A("'Ann Folkard'"),A("'Ballerina'"),A("'Brookside'"),A("Patricia = 'Brempat'"),A("'Orion'"),A("Blue Sunrise = 'Blogold'"),A("'Mavis Simpson'")]),
  ]},
 {"n":"Salvia","a":"sage · woodland sage","d":"Living perennial ornamental sage, chiefly Salvia nemorosa and its hybrids, grown for upright violet-blue spikes.",
  "t":["perennial","shrubby","tender"],"s":SN,"x":[
  X("'Caradonna'","S. nemorosa 'Caradonna'","Woodland sage cultivar; "+AGM+".",SN),
  X("'Mainacht'","May Night · S. × sylvestris 'Mainacht'","Sage cultivar classed by the RHS under Salvia × sylvestris; "+AGM+".",SN),
  X("Salvia nemorosa","woodland sage · Balkan clary","Perennial sage described by Linnaeus in 1762.",SN,y="1762",
    v=[A("'Ostfriesland'","East Friesland; "+AGM),A("'Amethyst'",AGM),A("'Blauhügel'","Blue Hill; "+AGM),A("'Lubecca'",AGM),A("'Porzellan'",AGM),A("'Tänzerin'",AGM),A("'Viola Klose'",AGM)]),
  ]},
 {"n":"Heuchera","a":"coral bells · alumroot · × Heucherella","d":"Living heuchera, an evergreen North American perennial grown for coloured leaves; × Heucherella crosses it with Tiarella.",
  "t":["purple-leaved","lime","amber","silver","Heucherella"],"s":HU,"x":[
  X("'Palace Purple'","H. micrantha 'Palace Purple'","Purple-leaved heuchera found at a palace in England, believed to be H. micrantha × H. villosa.",HU),
  X("AGM heucheras","","Leaf-colour cultivars holding the "+AGM+".",HU,v=[A("'Obsidian'"),A("'Blackberry Jam'"),A("'Can-Can'"),A("'Walnut'","Fox series")]),
  X("'Green Spice'","","Heuchera americana hybrid.",HU),
  ]},
 {"n":"Ornamental grass","a":"grass · sedge","d":"Living perennial grass grown for foliage and flower plumes in borders and prairie planting.",
  "t":["clump-forming","spreading","evergreen","deciduous","sedge"],"s":MS,"x":[
  X("'Karl Foerster'","Calamagrostis × acutiflora 'Karl Foerster' · feather reed-grass","Upright feather reed-grass cultivar; "+AGM+".",CA,v=[A("'Overdam'"),A("'Eldorado'")]),
  X("Miscanthus sinensis","Chinese silver grass · eulalia · susuki","East Asian clump-forming grass with silky autumn plumes.",MS,
    v=[A("'Zebrinus'","horizontal yellow bands; "+AGM),A("'Morning Light'",AGM),A("'Gracillimus'","narrow leaves"),A("'Malepartus'"),A("'Strictus'","narrow upright; "+AGM),A("'Kleine Fontäne'",AGM),A("'Silberfeder'",AGM),A("'Ferner Osten'",AGM)]),
  X("Cenchrus alopecuroides","fountain grass · Pennisetum alopecuroides","Fountain grass with bottlebrush flower heads.",CE,v=[A("'Hameln'","purplish heads; "+AGM),A("'Cassian's Choice'",AGM),A("'Red Head'","dark red heads; "+AGM)]),
  ]},
 {"n":"Bamboo","a":"","d":"Living bamboo plant, any genus; running types need a root barrier, clumping types spread slowly.",
  "t":["clumping","running"],"s":CR,"x":[
  X("Phyllostachys nigra","black bamboo · purple bamboo","Bamboo with slender arching canes that turn black; "+AGM+".",PN,v=[A("f. henonis","Henon bamboo; "+AGM)],dt="cane height · pot size"),
  X("Fargesia","umbrella bamboo · fountain bamboo","Hardy clumping mountain bamboos of East Asia, not aggressive spreaders.",FA,v=[A("F. murielae"),A("F. nitida"),A("F. rufa")]),
  X("Phyllostachys aurea","golden bamboo","Running bamboo spreading by rhizomes; invasive in the United States.",BA),
  ]},
]
trads=[{"n":"Hanashōbu (Japanese iris)","g":"Plants & gardens","r":"Japan","p":"Edo period onward","d":"Japanese cultivation of Iris ensata in three regional strains.","tech":"selection of cultivars for pond and pot display","mat":"Iris ensata","forms":["Edo strain","Higo strain","Ise strain"],"ctr":["Tokyo (Edo)","Kumamoto (Higo)","Mie (Ise)"],"auth":"Named cultivar of Iris ensata, assigned to a regional strain.","s":IE},
 {"n":"Mudan tree peony","g":"Plants & gardens","r":"China","p":"Northern and Southern Dynasties onward","d":"Chinese cultivation of the moutan tree peony, national flower from 1903 to 1929.","tech":"selection and grafting of tree peony cultivars","mat":"Paeonia suffruticosa","forms":["tree peony"],"ctr":["Heze (Caozhou)"],"auth":"Named Chinese cultivar; Heze lists over 1,300 varieties.","s":PS}]
w('C3','05_02',{"kinds":kinds,"brands":[],"traditions":trads,"notes":"Three old kinds (Hosta, Peony, Bamboo) kept with old s; seven new kinds sourced to Wikipedia. Iris 'Iris' with bearded/Siberian/Japanese as archetypes; Dykes Medal winners from Walters Gardens list plus AIS wiki 2025 (2006 duplicate of 'Jesse's Song' left out). No brand entries: no breeder confirmed as originator on retrieved pages (Rozanne breeder, Terra Nova/Dan Heims, Ernst Pagels not on pages). 'Palace Purple' spelt as on old usage; page names it 'Purple Palace' in places. Fargesia cultivars 'Simba'/'Jumbo' and Delphinium Belladonna group left out (not on retrieved pages)."})
