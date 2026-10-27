import json
V="https://www.vapesuperstore.co.uk/"
K="https://planetofthevapes.co.uk/reviews/rba/kayfun-prime-by-svoemesto.html"
G="https://planetofthevapes.co.uk/reviews/rda/the-goon-rda-by-528-custom-vapes.html"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
kinds=[
{"n":"Rebuildable tank atomiser (RTA)","a":"RTA","d":"Rebuildable atomiser with a built-in tank, where the user builds the coil and wick; filled from above or below.","t":["Mouth-to-lung RTA","Direct-lung RTA","Single coil","Dual coil"],"s":K,
 "x":[x("Kayfun","SvoeMesto","",K,"RTA line designed by SvoeMesto and refined through many models, widely cloned.",[("Kayfun Lite Plus","SvoeMesto","","Simplified version; widely cloned"),("Kayfun 5","SvoeMesto","","Broad-market model"),("Kayfun Prime","SvoeMesto","","Designed for mouth-to-lung vaping")])]},
{"n":"Rebuildable dripping atomiser (RDA)","a":"RDA · dripper","d":"Tankless rebuildable atomiser with a build deck, wetted by dripping e-liquid onto the coils.","t":["Single post","Two-post clamp","Squonk (BF) RDA"],"s":G,
 "x":[x("Goon RDA","528 Custom Vapes","2016",G,"24 mm RDA designed by coil builder Blue Eyed Goon with 528 Custom Vapes, with a bridge-clamp deck; released 15 May 2016.")]},
{"n":"Vape tank","a":"clearomiser","d":"Refillable tank or clearomiser for a vape device, with replaceable coils.","t":["MTL clearomiser","Sub-ohm tank"],"s":V},
{"n":"Refillable pod","a":"","d":"Empty pod for a pod device, filled by the user.","t":["Open pod"],"s":V},
{"n":"Vape coil","a":"replacement coil","d":"Replaceable heating coil for a vape tank or pod.","t":["Mesh","Ceramic","Wire-wound","Mouth-to-lung","Sub-ohm"],"s":V},
{"n":"Coil-building wire & cotton","a":"build supplies","d":"Resistance wire (Kanthal FeCrAl, nichrome, stainless steel), Clapton and other builds, wicking cotton and coil jigs for rebuildable atomisers.","t":["Kanthal","Nichrome","Stainless steel","Clapton","Wicking cotton","Coil jig"],"s":"https://en.wikipedia.org/wiki/Kanthal_(alloy)"},
{"n":"Vape battery cell","a":"18650 · 21700","d":"Rechargeable lithium-ion cell for regulated and mechanical mods, bought with a separate external charger; the number gives only size.","t":["18650","20700","21700"],"s":"https://en.wikipedia.org/wiki/18650_battery"},
{"n":"Vape pen battery","a":"510 battery","d":"Battery made for one vape pen or cartridge.","t":["510 thread"],"s":V},
]
brands=[{"n":"SvoeMesto","c":"Russia","f":"","seg":"Artisan & independent","kf":"Kayfun RTA","d":"Designer of the Kayfun series of rebuildable tank atomisers.","s":K},
 {"n":"528 Custom Vapes","c":"United States","f":"","seg":"Artisan & independent","kf":"Goon RDA","d":"Maker of the Goon RDA with designer Blue Eyed Goon.","s":G}]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Taifun, Dvarw, Zeus, Drop Dead and RDTA could not be sourced (vape sites mostly blocked; fetched only via Firecrawl for Goon and Kayfun Prime), so RDTA kind and those archetypes are omitted. SvoeMesto country (Russia) from memory and not on a retrieved page; kept off-line? kept in c field. Wire kind sourced from Wikipedia Kanthal (alloy); Clapton/nichrome types follow the brief."},open('s03_01.json','w'),ensure_ascii=False)
