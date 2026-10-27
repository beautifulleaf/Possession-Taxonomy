import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,a='',mk='',y='',v=None,dt=''):
    o={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: o["v"]=[dict(zip(("n","mk","y","d"),vv)) for vv in v]
    if dt: o["dt"]=dt
    return o
H=W+"Hoya_(plant)"; T=W+"Tillandsia"; S=W+"Selaginella"
kinds=[
 {"n":"Wax plant","a":"Hoya · porcelain flower · waxflower","d":"Climbing or trailing Asian vine with thick leaves and clusters of waxy, scented star-shaped flowers.",
  "t":["trailing","climbing","variegated"],"s":"https://rewilddc.com/products/hoya-carnosa",
  "x":[X("Hoya carnosa","The most popular houseplant hoya, from southern China, Taiwan and Japan; holds the RHS Award of Garden Merit.",W+"Hoya_carnosa",
         v=[("'Compacta'","","1967","Hindu rope: folded, curled leaves on a rope-like stem; popularised by B. L. Cobia Nursery"),("'Krimson Queen'","","","variegated cultivar"),("'Tricolor'","","","variegated"),("'Rubra'","","","")],
         dt="leaf variegation (cream edge, pink centre) · leaf form (flat, curled) · flower colour"),
       X("Hoya pubicalyx","Commonly sold species, often mislabelled as H. carnosa.",H),
       X("Hoya kerrii","Heart-leaved hoya from South-East Asia, sold in Europe for Saint Valentine's Day.",W+"Hoya_kerrii",a="lucky-heart"),
       X("Hoya lanceolata subsp. bella","Small-leaved hoya often grown in hanging baskets.",H,a="Hoya bella")]},
 {"n":"Air plant","a":"Tillandsia","d":"Soil-free bromeliad of the genus Tillandsia that takes water through leaf scales and is grown mounted or loose.",
  "t":["silver (xeric)","green (mesic)","clump"],"s":"https://mountaincrestgardens.com/",
  "x":[X("Tillandsia ionantha","Small, popular species that blushes red when it flowers and forms pups.",T,dt="size · blush colour · clump or single"),
       X("Tillandsia xerographica","Large silver rosette, listed under CITES Appendix II.",T),
       X("Tillandsia usneoides","Hanging strands of grey stems that drape from trees.",T,a="Spanish moss"),
       X("Tillandsia cyanea","Pink-bracted species that, unusually, takes water through its roots; grown potted.",T),
       X("Tillandsia stricta","Common clump-forming species with soft leaves.",T),
       X("Tillandsia recurvata","Small ball-shaped species that grows even on wires.",T,a="ball moss")]},
 {"n":"Live moss","a":"terrarium moss · moss ball · marimo","d":"Living moss or moss-like alga sold to grow in terrariums, moss gardens or water, as sheets, cushions or balls.",
  "t":["sheet","cushion","moss ball"],"s":"https://www.thebiodude.com/collections/terrarium-mosses",
  "x":[X("Marimo","Velvety green ball of the alga Aegagropila linnaei, kept in water; famous from Lake Akan, Japan.",W+"Marimo",a="Aegagropila linnaei · moss ball · lake ball",
         dt="ball diameter · single or several per jar"),
       X("Pincushion moss","Pale green dome-forming moss of Northern Hemisphere forests.",W+"Leucobryum_glaucum",a="Leucobryum glaucum · cushion moss")],
  "m":[["Live Hand-Propagated Star Moss",""]]},
 {"n":"Spikemoss","a":"Selaginella · lesser clubmoss","d":"Living spikemoss of the genus Selaginella, a fern ally sold for terrariums and shade.",
  "t":["creeping","upright"],"s":"https://www.thebiodude.com/collections/terrarium-mosses",
  "x":[X("Selaginella kraussiana","Creeping African species, the most commonly sold spikemoss.",S,a="golden clubmoss"),
       X("Selaginella uncinata","Creeping species with iridescent blue-green leaves.",S,a="peacock moss · blue spikemoss"),
       X("Selaginella martensii","Upright species, often variegated.",S,a="frosty fern · variegated spikemoss"),
       X("Selaginella erythropus","Upright species with red stems.",S,a="ruby-red spikemoss"),
       X("Selaginella lepidophylla","Chihuahuan Desert species that curls into a brown ball when dry and greens again when wetted.",S,a="resurrection plant · dinosaur plant"),
       X("Selaginella willdenowii","South-East Asian climber known for iridescent colours.",S,a="peacock fern")]},
 {"n":"Nerve plant","a":"Fittonia · mosaic plant","d":"Low tropical American plant with leaves netted in white, pink or red veins, grown in pots and terrariums.",
  "t":["white-veined","red- or pink-veined","mini"],"s":W+"Fittonia",
  "x":[X("Fittonia albivenis","The commonly grown species, with many cultivars differing in vein colour and size.",W+"Fittonia",v=[("'Mini Red'","","","red-veined")],dt="vein colour · leaf size")]}]
trads=[{"n":"Marimo culture of Lake Akan","g":"Plants & gardens","r":"Hokkaido, Japan","p":"protected since the 1920s","d":"Lake Akan's large marimo balls are a protected natural monument celebrated by an Ainu festival each October; shop marimo are of European origin.","tech":"growing loose algal balls in cool water","mat":"Aegagropila linnaei","forms":["Marimo"],"ctr":["Lake Akan"],"auth":"collecting at Lake Akan is prohibited, so balls sold in Japan come from Europe","s":W+"Marimo"}]
out={"kinds":kinds,"brands":[],"traditions":trads,"notes":"All four old kinds kept (wax plant, air plant, live moss, spikemoss) plus new Nerve plant. Old kinds keep their old s. 'Krimson Queen' from the old definition. Hoya linearis and Tillandsia caput-medusae left out: no retrieved page confirmed them. Star moss species not confirmed, so the old model stays in m. No brands."}
p='work/C3/shelves/01_02.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
