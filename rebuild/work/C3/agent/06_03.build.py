import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
A=lambda n,d="",y="",mk="":(n,mk,y,d)
OLD="https://www.starkbros.com/products/fruit-trees"
HP='pot size · plug or established plant'
TP='grafted or own-root · pot size'
kinds=[
 {"n":"Basil plant","a":"Ocimum basilicum · living basil","d":"Living basil plant sold growing in a pot or tray, also when sold to eat.","t":["supermarket living herb","garden plant","purple-leaved"],"s":"https://www.goodeggs.com/rocketfarms/large-living-basil-plant/6827a0bc23b5ec001333fa70","x":[
  X("Genovese","sweet basil","The sweet basil type Western cooking means by basil.",W+"Basil",dt=HP),
  X("Thai basil","O. basilicum var. thyrsifolium","Basil variety grown and used in Thailand.",W+"Basil",dt=HP),
  X("Holy basil","tulsi · Ocimum tenuiflorum","Separate Ocimum species, formerly O. sanctum.",W+"Basil",dt=HP),
  X("Other basils","","Further basil cultivars and hybrids.",W+"Basil",v=[A("Lemon basil","O. basilicum × O. americanum"),A("Dark Opal","purple-leaved"),A("Greek basil","var. minimum, small-leaved"),A("African blue basil","O. basilicum × O. kilimandscharicum")]),
  ]},
 {"n":"Mint plant","a":"Mentha","d":"Living mint plant grown in a pot or bed for its leaves.","t":["spearmint","peppermint","apple mint","variegated"],"s":W+"Mentha","x":[
  X("Spearmint","Mentha spicata","The usual culinary mint, carvone-scented.",W+"Mentha",dt=HP,v=[A("Moroccan","var. crispa"),A("Mojito"),A("Curly")]),
  X("Peppermint","Mentha × piperita","Menthol-rich hybrid of water mint and spearmint.",W+"Mentha",dt=HP,v=[A("Chocolate"),A("Citrata","eau de Cologne mint"),A("Strawberry"),A("Swiss")]),
  X("Apple mint","Mentha suaveolens · round-leaf mint","Soft, round-leaved mint.",W+"Mentha",dt=HP,v=[A("Pineapple mint","variegated form 'Variegata'")]),
  X("Pennyroyal","Mentha pulegium","Low mint rich in pulegone.",W+"Mentha",dt=HP),
  ]},
 {"n":"Rosemary","a":"Salvia rosmarinus · Rosmarinus","d":"Living rosemary shrub grown for its aromatic leaves.","t":["upright","prostrate","hedging"],"s":W+"Rosemary","x":[
  X("Miss Jessopp's Upright","","Tall columnar rosemary with wider leaves; "+AGM+".",W+"Rosemary",dt=HP),
  X("Prostratus","","Low ground-cover rosemary.",W+"Rosemary",dt=HP,v=[A("Severn Sea","spreading, deep violet flowers; "+AGM)]),
  X("Tuscan Blue","","Robust, fast upright rosemary hardy to about −9 °C.",W+"Rosemary",dt=HP),
  X("Arp","","Upright, lemon-scented rosemary from Madalene Hill of Arp, Texas, hardy to about −12 °C.",W+"Rosemary",dt=HP),
  X("Benenden Blue","","Rosemary with narrow dark leaves; "+AGM+".",W+"Rosemary",dt=HP),
  ]},
 {"n":"Thyme","a":"Thymus vulgaris · common thyme","d":"Living thyme plant grown for its aromatic leaves.","t":["culinary","creeping","variegated","lemon-scented"],"s":W+"Thymus_vulgaris","x":[
  X("Common thyme","Thymus vulgaris","Culinary thyme in French, German and English forms.",W+"Thymus_vulgaris",dt=HP,v=[A("Silver Queen","white-margined; "+AGM),A("Argenteus","silver thyme")]),
  ]},
 {"n":"Bay tree","a":"Laurus nobilis · sweet bay · bay laurel","d":"Living bay laurel grown for its leaves, often trained as a clipped standard.","t":["standard (lollipop)","pyramid","twisted stem","bush"],"s":W+"Laurus_nobilis","x":[
  X("Laurus nobilis","sweet bay","Mediterranean evergreen grown for kitchen leaves and topiary.",W+"Laurus_nobilis",dt="stem height · head shape · pot size",
    v=[A("Aurea","gold-leaved; "+AGM),A("f. angustifolia","willow-leaved; "+AGM)]),
  ]},
 {"n":"Tomato plant","a":"tomato plug · grafted tomato","d":"Young tomato plant sold to grow on, own-root or grafted on a vigorous disease-resistant rootstock.","t":["grafted","own-root","cordon (indeterminate)","bush (determinate)","cherry","beefsteak","plum"],"s":W+"Grafting","x":[
  X("Brandywine","","Potato-leaved pink beefsteak heirloom listed by Burpee by 1886.",W+"Brandywine_tomato",y="1886",dt=TP),
  X("San Marzano","","Italian plum tomato from San Marzano sul Sarno, indeterminate; PDO for canned fruit.",W+"San_Marzano_tomato",dt=TP),
  X("Cherokee Purple","","Dusky purple heirloom from John Green of Tennessee, named by Craig LeHoullier, introduced by Southern Exposure Seed Exchange.",W+"Cherokee_Purple",y="1993",dt=TP),
  X("Mortgage Lifter","","West Virginia beefsteak heirloom; William Estler's version 1922, M. C. 'Radiator Charlie' Byles' in the 1930s.",W+"Mortgage_Lifter",y="1922",dt=TP),
  X("Other famous heirlooms","","Heirloom tomatoes widely sold as plants.",W+"Heirloom_tomato",v=[A("Black Krim"),A("Green Zebra")]),
  ]},
 {"n":"Chilli plant","a":"pepper plant · Capsicum","d":"Young or mature chilli pepper plant (Capsicum) sold to grow on for fruit.","t":["C. annuum","C. chinense","C. baccatum","C. frutescens","grafted","overwintered"],"s":W+"Capsicum_chinense","x":[
  X("Habanero","","Compact Capsicum chinense bush, named after Havana.",W+"Capsicum_chinense",dt=TP,v=[A("Scotch bonnet","Jamaica and Trinidad"),A("Datil","Florida")]),
  X("Carolina Reaper","","Habanero-type superhot from South Carolina.",W+"Capsicum_chinense",dt=TP,v=[A("Pepper X","South Carolina, 2.69 million SHU","2023")]),
  X("Bhut jolokia","ghost pepper","Superhot chilli from Assam.",W+"Capsicum_chinense",dt=TP,v=[A("Dorset Naga")]),
  X("Trinidad Scorpion","","Superhot chilli from Trinidad.",W+"Capsicum_chinense",dt=TP,v=[A("Butch T"),A("Moruga")]),
  X("Jalapeño","","Mexican Capsicum annuum chilli, usually 4,000–8,500 SHU.",W+"Jalapeño",dt=TP,v=[A("Early Jalapeño"),A("TAM Mild Jalapeño"),A("NuMex Primavera")]),
  ]},
 {"n":"Rhubarb plant","a":"Rheum × hybridum · rhubarb crown","d":"Living rhubarb crown or potted plant (Rheum) grown for its edible stalks.","t":["early (for forcing)","maincrop","perpetual"],"s":OLD,"x":[
  X("Timperley Early","","Old early rhubarb, rated the best for forcing, cut unforced from late February; "+AGM+".","https://www.ashridgetrees.co.uk/products/timperley-early-rhubarb-plants",dt="crown or pot"),
  X("Victoria","","Rhubarb favoured by Lawrence D. Hills for flavour.",W+"Rhubarb",dt="crown or pot",v=[A("Hawke's Champagne","Hills's favourite"),A("Stein's Champagne",AGM),A("Early Albert"),A("Gaskin's Perpetual","lowest oxalic acid")]),
  ]},
 {"n":"Asparagus plant","a":"asparagus crown · Asparagus officinalis","d":"Living asparagus crown or plant grown for its edible spears.","t":["all-male F1","open-pollinated","green","purple","white (blanched)"],"s":OLD,"x":[
  X("Connover's Colossal","Conover's Colossal","Nineteenth-century American asparagus developed by S. B. Conover and introduced by J. M. Thorburn & Co.; "+AGM+".",
    "https://www.motherearthnews.com/organic-gardening/heirloom-asparagus-varieties-zewz1304zsch/",y="1868",dt="1- or 2-year crowns"),
  X("Gijnlim","","All-male F1 asparagus with purple-tipped green spears; "+AGM+".","https://www.rhsplants.co.uk/plants/_/asparagus-gijnlim/classid.2000010490/",dt="1- or 2-year crowns"),
  X("Purple Passion","Passionate Purple","Sweet purple asparagus eaten raw, partly from Swiss heirloom stock.","https://www.motherearthnews.com/organic-gardening/heirloom-asparagus-varieties-zewz1304zsch/",dt="crowns",
    v=[A("Violetto d'Albenga","purple asparagus from Albenga, Italy")]),
  X("Jersey King","","Disease-resistant asparagus from Rutgers University.","https://www.motherearthnews.com/organic-gardening/heirloom-asparagus-varieties-zewz1304zsch/",dt="crowns"),
  ]},
 {"n":"Cannabis plant","a":"marijuana plant · hemp plant","d":"Living cannabis plant (Cannabis) sold to grow where legal, as seed-raised plant or clone.","t":["photoperiod","autoflowering","feminised","regular","clone","seed-raised"],"s":"https://sourcenursery.com/","x":[
  X("Autoflowering cannabis","autoflower","Cannabis that flowers by age, not day length, from Cannabis ruderalis genetics.",W+"Autoflowering_cannabis",dt="seed or plant · indoor or outdoor",v=[A("Lowryder","early autoflowering strain")]),
  ]},
]
trads=[{"n":"Yorkshire forced rhubarb","g":"Food & drink","r":"Rhubarb Triangle, West Yorkshire, England (Wakefield, Morley, Rothwell)","p":"early 1800s to today","d":"Rhubarb crowns grown two years in the field, then forced in heated dark sheds and picked by candlelight.","tech":"field-grown roots frosted, moved into heated windowless sheds in November, harvested by candlelight","mat":"rhubarb crowns","forms":["forced rhubarb stalks","forcing crowns"],"ctr":["E. Oldroyd & Sons","Asquith Growers"],"auth":"'Yorkshire Forced Rhubarb' carries EU Protected Designation of Origin (2010).","s":W+"Rhubarb_Triangle"}]
w('C3','06_03',{"kinds":kinds,"brands":[],"traditions":trads,"notes":"All 4 old kinds kept with old s; Mint plant, Rosemary, Thyme, Bay tree, Tomato plant and Chilli plant added from Wikipedia. Cannabis plant stays near kind-level: one autoflowering archetype from Wikipedia, no seed-bank SKUs. Asparagus Mary Washington and rhubarb Stockbridge Arrow not on retrieved pages; Timperley Early origin unconfirmed so no year. No brands needed."})
