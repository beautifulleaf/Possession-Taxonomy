import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,s,y='',v=(),dt='variegation · leaf form · plant size (cutting, small pot, specimen)',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
AGM="RHS Award of Garden Merit"
kinds=[
 {"n":"Snake plant & dracaena","a":"Dracaena · snake plant · Sansevieria · mother-in-law's tongue · corn plant · dragon tree","d":"Living plant of the genus Dracaena, from upright snake plants (ex-Sansevieria) to cane-stemmed dracaenas.",
  "t":["snake plant (rosette, ex-Sansevieria)","cane dracaena","lucky bamboo"],"s":"https://mountaincrestgardens.com/","x":[
  X("Dracaena trifasciata","snake plant · mother-in-law's tongue · Saint George's sword · Sansevieria trifasciata","West African rhizomatous succulent with stiff upright leaves banded grey-green; Sansevieria until 2017.",W+"Dracaena_trifasciata",
    v=[("var. laurentii ('Laurentii')","","",AGM),("Moonshine","","","(old data)"),("'Hahnii'","","",""),("'Golden Hahni'","","",AGM),("'Silver Hahnii'","","",""),("'Bantel's Sensation'","","",AGM),("'Compacta'","","",""),("'Goldiana'","","",""),("'Silbersee'","","","")],dt="leaf banding · margin colour · rosette or tall"),
  X("Dracaena angolensis","Sansevieria cylindrica · African spear · spear sansevieria","Angolan succulent with striped cylindrical leaves up to about 2 m.",W+"Dracaena_angolensis",dt="leaf length · braided or loose"),
  X("Dracaena fragrans","corn plant · striped dracaena · fortune plant","Tropical African shrub with glossy strap leaves, grown as a cane houseplant.",W+"Dracaena_fragrans",
    v=[("'Massangeana'","","","corn plant"),("'Janet Craig'","","",""),("'Lemon Lime'","","",""),("'Warneckei'","","",""),("'Compacta'","","","")],dt="variegation · cane height · single or multi-cane"),
  X("Dracaena reflexa var. angustifolia","Dracaena marginata · Madagascar dragon tree · red edge dracaena","Slender-leaved variety from Madagascar with thin red-edged leaves, sold as D. marginata.",W+"Dracaena_marginata",
    v=[("'Tricolor'","","",AGM),("'Colorama'","","",""),("'Tarzan'","","",""),("'Magenta'","","","")],dt="leaf colour · stem form · height"),
  X("Dracaena reflexa","song of India · song of Jamaica","Indian Ocean island tree with glossy leaves, kept small as a houseplant.",W+"Dracaena_reflexa",
    v=[("'Variegata'","","","cream and yellow-green margins; "+AGM),("Song of India","","","(old data)")]),
  X("Dracaena sanderiana","lucky bamboo · ribbon dracaena · Sander's dracaena","African dracaena sold as lucky bamboo; not a true bamboo.",W+"Dracaena_sanderiana",
    v=[("Million Bamboo","","","(old data)")],dt="stalk count · straight or curly · water or soil"),
 ]},
 {"n":"Houseplant fig","a":"Ficus · rubber plant · fiddle-leaf fig · weeping fig","d":"Living fig (genus Ficus) grown as an indoor tree, chiefly rubber plant, fiddle-leaf fig and weeping fig.",
  "t":["green","variegated","dark-leaved"],"s":"https://botachoku.com/foliage","x":[
  X("Ficus elastica","rubber plant · rubber fig · Indian rubber tree","South and Southeast Asian banyan fig with large leathery leaves, the classic rubber plant.",W+"Ficus_elastica",
    v=[("'Robusta'","","","broader, stiffer, more upright leaves"),("'Decora'","","","pinkish hues; also sold as 'Ruby' in Australia"),("Tineke","","","(old data)"),("Ruby","","","(old data)"),("Burgundy","","","(old data)")],dt="variegation · leaf colour · bush or standard"),
  X("Ficus lyrata","fiddle-leaf fig · banjo fig","West African fig with large violin-shaped leaves; "+AGM+".",W+"Ficus_lyrata",dt="height · bush or standard"),
  X("Ficus benjamina","weeping fig · benjamin fig","Asian and Australian fig with glossy oval leaves on drooping branchlets.",W+"Ficus_benjamina",
    v=[("'Starlight'","","","variegated; "+AGM),("'Danielle'","","",""),("'Naomi'","","",""),("'Exotica'","","",""),("'Golden King'","","","")],dt="variegation · braided stem · height"),
 ]},
 {"n":"Prayer plant","a":"Marantaceae · Calathea · Goeppertia · Maranta · Ctenanthe · Stromanthe","d":"Living patterned-leaf plant of the arrowroot family (Maranta, Goeppertia, Ctenanthe, Stromanthe) whose leaves fold up at night.",
  "s":"https://mountaincrestgardens.com/","x":[
  X("Maranta leuconeura","prayer plant","Brazilian rhizomatous perennial whose marked oval leaves lie flat by day and fold upward at night.",W+"Maranta_leuconeura",
    v=[("var. erythroneura","","","herringbone plant; red veins; "+AGM),("var. kerchoveana","","","rabbit's foot; dark blotches; "+AGM),("Lemon-Lime","","","")],dt="vein colour · leaf pattern"),
  X("Goeppertia orbifolia","Calathea orbifolia","Brazilian Atlantic Forest species grown for its ornamental leaves, formerly Calathea.",W+"Goeppertia_orbifolia",dt="leaf size · plant size"),
  X("Goeppertia makoyana","Calathea makoyana","Patterned-leaf Goeppertia species, moved from Calathea in 2012.",W+"Goeppertia"),
  X("Goeppertia roseopicta","Calathea roseopicta","Patterned-leaf Goeppertia species, moved from Calathea in 2012.",W+"Goeppertia"),
  X("Goeppertia zebrina","Calathea zebrina","Type species of Goeppertia, resurrected as a genus from Calathea in 2012.",W+"Goeppertia",y="2012"),
  X("Ctenanthe oppenheimiana 'Tricolor'","never-never plant","Brazilian ctenanthe with narrow leaves patterned silver above and maroon below; "+AGM+".",W+"Ctenanthe"),
  X("Stromanthe thalia","Stromanthe sanguinea","Southeastern Brazilian Stromanthe species, also known by the synonym S. sanguinea.",W+"Stromanthe"),
 ]},
 {"n":"Peperomia","a":"radiator plant · baby rubber plant · watermelon peperomia","d":"Living herbaceous plant of the genus Peperomia (Piperaceae), sold as a houseplant.",
  "s":"https://mountaincrestgardens.com/","t":["upright","trailing","succulent-leaved"],"x":[
  X("Peperomia obtusifolia","baby rubber plant · American rubber plant · pepper face","Compact tropical American perennial with thick cupped leaves; many variegated cultivars.",W+"Peperomia_obtusifolia",dt="variegation · plant size"),
  X("Peperomia argyreia","watermelon peperomia","Small South American peperomia with silver-striped oval leaves on red stems.",W+"Peperomia_argyreia",dt="plant size"),
  X("Peperomia caperata","emerald ripple peperomia","Brazilian mound-forming peperomia with wrinkled heart-shaped leaves.",W+"Peperomia_caperata",
    v=[("'Luna Red'","","",AGM),("'Red Ripple'","","",""),("'Rosso'","","",""),("'Rubra'","","","")],dt="leaf colour · plant size"),
  X("Peperomia prostrata","string of turtles","Peperomia sold as string of turtles, one of about 40 houseplant species.",W+"Peperomia",dt="trail length"),
  X("Peperomia polybotrya","raindrop peperomia","Peperomia with large drop-shaped leaves.",W+"Peperomia"),
  X("Peperomia rotundifolia","","Peperomia species commonly sold as a houseplant.",W+"Peperomia",dt="trail length"),
 ]},
 {"n":"Pilea","a":"Chinese money plant · P. peperomioides · aluminium plant","d":"Living herbaceous plant of the genus Pilea, including the Chinese money plant (P. peperomioides).",
  "s":"https://mountaincrestgardens.com/","x":[
  X("Pilea peperomioides","Chinese money plant · UFO plant · pancake plant · missionary plant","Chinese perennial with round shield-shaped leaves, spread through Europe by cuttings after 1946.",W+"Pilea_peperomioides",y="1906",
    v=[("'Sugar'","","",""),("'White Splash'","","",""),("'Mojito'","","","")],dt="variegation · plant size (pup, small pot, mature)"),
  X("Pilea cadierei","aluminium plant","Aluminium plant, one of the genus's horticultural species.",W+"Pilea"),
  X("Pilea involucrata","friendship plant","Friendship plant, one of the genus's horticultural species.",W+"Pilea"),
  X("Pilea microphylla","artillery plant · gunpowder plant","Artillery plant, one of the genus's horticultural species.",W+"Pilea"),
 ]},
 {"n":"Begonia","a":"rex begonia · cane begonia · wax begonia","d":"Living plant of the genus Begonia, foliage (rex) and flowering, houseplant or bedding.",
  "t":["cane-like","shrub-like","semperflorens (wax)","rhizomatous","rex","tuberous","Elatior (× hiemalis)","thick-stemmed","trailing"],"s":"https://mountaincrestgardens.com/","x":[
  X("Rex begonia","Begonia Rex group","Foliage begonias of the American Begonia Society's Rex group, propagated from leaf cuttings.",W+"Begonia",dt="leaf colour · leaf pattern · spiral or flat"),
  X("Begonia maculata","polka dot begonia · trout begonia","Brazilian cane begonia with silver-spotted olive leaves and red-purple undersides.",W+"Begonia_maculata",
    v=[("pink variegated form","","","rare, pastel pink patches")],dt="spot density · height"),
  X("Angel wing begonia","B. aconitifolia × B. coccinea","Cane-like hybrid begonia from B. aconitifolia and B. coccinea.",W+"Begonia",dt="leaf spotting · flower colour"),
  X("Dragonwing begonia","","Semperflorens-derived hybrids with much larger leaves and flowers.",W+"Begonia",dt="flower colour"),
 ]},
 {"n":"Indoor fern","a":"Boston fern · maidenhair · bird's-nest fern · staghorn fern","d":"Living fern grown indoors for its fronds, such as Boston, maidenhair, bird's-nest and staghorn ferns.",
  "s":W+"Nephrolepis_exaltata","t":["potted","hanging basket","mounted"],"x":[
  X("Boston fern","Nephrolepis exaltata 'Bostoniensis' · sword fern","Arching-frond mutation of N. exaltata found in 1894 in a shipment sent to Boston; "+AGM+".",W+"Nephrolepis_exaltata",y="1894",
    v=[("'Bostoniensis'","","1894",AGM),("'Elegantissima'","","",AGM),("'Teddy Junior'","","",""),("'Rooseveltii'","","",""),("'Whitmanii Improved'","","",""),("'Green Lady'","","",""),("'Sonata'","","","")],dt="frond form · pot or basket"),
  X("Delta maidenhair fern","Adiantum raddianum","South American maidenhair with fine fronds on dark glossy stalks.",W+"Adiantum_raddianum",
    v=[("'Brilliantelse'","","",AGM),("'Kensington Gem'","","",AGM)],dt="frond density · pot size"),
  X("Bird's-nest fern","Asplenium nidus · nest fern","Epiphytic fern with simple banana-like fronds; many plants sold are A. australasicum; "+AGM+".",W+"Asplenium_nidus",dt="frond form · plant size"),
  X("Elkhorn fern","Platycerium bifurcatum · staghorn fern","Eastern Australian epiphyte with nest fronds and forked fertile fronds, often mounted on boards; "+AGM+".",W+"Platycerium_bifurcatum",dt="mounted or potted · size"),
 ]},
 {"n":"Indoor palm","a":"kentia · parlour palm · areca palm","d":"Living palm grown as a houseplant, such as kentia, parlour and areca palms.",
  "s":W+"Howea_forsteriana","t":["single stem","multi-stem"],"x":[
  X("Kentia palm","Howea forsteriana · thatch palm · palm court palm","Lord Howe Island palm, a nineteenth-century parlour palm and still a major houseplant.",W+"Howea_forsteriana",y="19th century",dt="height · stems per pot"),
  X("Parlour palm","Chamaedorea elegans · Neanthe bella palm","Small slow-growing palm from southern Mexico and Guatemala; "+AGM+".",W+"Chamaedorea_elegans",dt="height · stems per pot"),
  X("Areca palm","Dypsis lutescens · Chrysalidocarpus lutescens · golden cane palm · butterfly palm","Madagascan palm widely grown as an ornamental and houseplant.",W+"Dypsis_lutescens",dt="height · stems per pot"),
 ]},
 {"n":"Spider plant","a":"Chlorophytum comosum · airplane plant · ribbon plant","d":"Living spider plant (Chlorophytum comosum), an African perennial with arching leaves and plantlets on runners.",
  "s":W+"Chlorophytum_comosum","t":["green","variegated","curly"],"x":[
  X("Chlorophytum comosum","spider plant · spider ivy · airplane plant","Evergreen perennial from tropical and southern Africa with arching strap leaves.",W+"Chlorophytum_comosum",
    v=[("'Vittatum'","","2017","white central stripe; "+AGM),("'Variegatum'","","2017","white margins; "+AGM),("'Bonnie'","","",""),("'Green Bonnie'","","","")],dt="variegation · leaf curl · pot or hanging"),
 ]},
 {"n":"Tradescantia","a":"inch plant · spiderwort · purple heart · Moses-in-the-cradle","d":"Living trailing or clumping spiderwort of the genus Tradescantia grown as a houseplant.",
  "s":W+"Tradescantia_zebrina","t":["trailing","upright rosette"],"x":[
  X("Tradescantia zebrina","silver inch plant · wandering dude","Creeping perennial from Mexico to Colombia with silver-striped leaves and purple undersides; "+AGM+".",W+"Tradescantia_zebrina",
    v=[("'Purpusii'","","",AGM),("'Quadricolor'","","",AGM),("'Danny Lee'","","","variegated")],dt="stripe colour · trail length"),
  X("Tradescantia pallida","purple heart · purple queen","Trailing Mexican spiderwort; the commercial cultivar has purple-violet leaves and stems.",W+"Tradescantia_pallida",
    v=[("'Purpurea'","","","sold as 'Purple Heart'")],dt="trail length"),
  X("Tradescantia spathacea","Moses-in-the-cradle · oyster plant · boatlily","Rosette-forming Central American herb with waxy leaves, purple underneath.",W+"Tradescantia_spathacea",
    v=[("'Sitara'","","",AGM),("'Vittata'","","","yellow-striped leaves")],dt="leaf stripe · plant size"),
 ]},
]
notes=("Kept all six old kinds (Dracaena became 'Snake plant & dracaena'; Rubber plant broadened to 'Houseplant fig'; Calathea broadened to 'Prayer plant'); added Indoor fern, Indoor palm, Spider plant, Tradescantia. "
 "Old flat models became versions (Moonshine, Song of India, Million Bamboo, Tineke, Ruby, Burgundy); D. marginata became D. reflexa var. angustifolia per Wikipedia. "
 "Left out: Begonia rex and Tradescantia fluminensis pages (Wikipedia 503, not retried); Goeppertia lancifolia, Ficus 'Bambino', Stromanthe 'Triostar' (not on fetched pages). No brands: archetypes are species/cultivars without makers. Wikidata rate-limited.")
out={"kinds":kinds,"brands":[],"traditions":[],"notes":notes}
p='work/C3/shelves/01_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
