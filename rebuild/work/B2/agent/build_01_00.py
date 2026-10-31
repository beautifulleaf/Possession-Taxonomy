import json, os
NBC="https://www.nbcnews.com/select/shopping/best-sheets-rcna262463"
lux=[("Frette bed linen","Frette"),("Sferra bed linen","Sferra"),("Pratesi bed linen","Pratesi"),("Libeco Home linen bedding","Libeco"),("Matouk bed linen","Matouk"),("Yves Delorme bed linen","Yves Delorme"),("D. Porthault bed linen","D. Porthault"),("Anichini bed linen","Anichini"),("Garnier-Thiebaut bed linen","Garnier-Thiebaut"),("Hästens bed linen","Hästens")]
kinds=[
 {"n":"Sheet","a":"bed sheet · flat sheet · fitted sheet · top sheet · bottom sheet",
  "d":"A flat or fitted sheet of woven or knitted fabric laid over the mattress or under the top cover.",
  "t":["flat (top) sheet","fitted (bottom) sheet","sheet set","percale","sateen","linen","flannel","jersey knit","silk charmeuse","bamboo / lyocell","microfibre","cotton–polyester blend","thread count","deep-pocket fitted"],
  "s":"https://en.wikipedia.org/wiki/Bed_sheet",
  "m":[["Classic Percale Sheet Set","Brooklinen"],["Percale Sheet Set","Parachute"],["Percale Sheet Set","Coop Sleep Goods"],["Cotton Sheets (sateen)","California Design Den"],["Signature Hemmed Sheet Set","Boll & Branch"],["Heritage Chamois Flannel Sheet Collection","L.L.Bean"],["Cotton Jersey Sheet Set","Amazon Basics"],["Washed European Linen Core Sheet Set","Brooklinen"],["Stonewashed Linen Sheet Set","The Citizenry"],["Bamboo Sheet Set","Quince"],["AiryWeight Eucalyptus Sheet Set","Sijo"],["Sheet Set (silk)","Mulberry Park Silks"]],
  "r":[list(x) for x in lux]},
 {"n":"Pillowcase","a":"pillow slip · pillowslip · pillow sham",
  "d":"A removable fabric case that covers a bed pillow.",
  "t":["housewife (flap closure)","Oxford (flanged border)","bag / plain (open end)","sham (decorative, back opening)","zip or button closure","silk","percale","sateen","linen"],
  "s":"https://en.wikipedia.org/wiki/Pillowcase"},
 {"n":"Duvet cover","a":"comforter cover · quilt cover",
  "d":"A removable fabric bag, closed by buttons, ties or a zip, that encloses a duvet or comforter.",
  "t":["button closure","popper closure","zip closure","tie closure","reversible","percale","sateen","linen","flannel","jersey","waffle"],
  "s":"https://www.sleepfoundation.org/best-bedding/quilt-vs-comforter-vs-duvet"},
 {"n":"Valance","a":"dust ruffle · bed skirt · valance sheet",
  "d":"A fabric skirt fitted between mattress and bed base that hides the base and legs.",
  "t":["platform valance (sheet with skirt)","fitted valance sheet","box-pleated","gathered / ruffled","tailored"],
  "s":"https://www.pbteen.com/shop/bedding/bed-skirt-basics"},
 {"n":"Headboard cover","a":"bed frame cover",
  "d":"A removable fabric cover for an upholstered bed frame or headboard, including covers made to fit one model.",
  "s":"https://www.ikea.com/qa/en/cat/bedding-tl004"}]
K="knowledge"
def B(n,c,f,seg,d,lines=None,sig=None,rel=None,s=K):
    b={"n":n,"c":c,"seg":seg,"d":d,"s":s}
    if f: b["f"]=f
    if lines: b["lines"]=lines
    if rel: b["rel"]=rel
    return b
brands=[
 B("Frette","Italy","1860","luxury linen house","Founded in Grenoble and based in Italy since 1865; luxury bed and bath linen supplied to grand hotels, royal households and the Orient Express.",rel=["Pratesi","Sferra"],s="https://en.wikipedia.org/wiki/Frette"),
 B("Sferra","United States","1891","luxury linen house","Linen house founded in Venice and now based in New Jersey; luxury bed, bath and table linen.",rel=["Frette","Matouk"]),
 B("Pratesi","Italy","1906","luxury linen house","Tuscan family linen maker known for embroidered bed linen.",rel=["Frette"]),
 B("Libeco","Belgium","1858","linen weaver","Belgian flax-linen weaver headquartered in Meulebeke, West Flanders; household linen sold as Libeco Home.",lines=["Libeco Home"],s="https://en.wikipedia.org/wiki/Libeco"),
 B("Matouk","United States","1929","luxury linen house","Fall River, Massachusetts maker of luxury bed and bath linen.",rel=["Sferra"]),
 B("Yves Delorme","France","","luxury linen house","French maker of printed and plain luxury bed and bath linen.",rel=["D. Porthault","Garnier-Thiebaut"]),
 B("D. Porthault","France","","luxury linen house","Paris linen house known for printed cotton bed linen.",rel=["Yves Delorme"]),
 B("Anichini","United States","","luxury linen house","Vermont-based maker of luxury bed and table linen."),
 B("Garnier-Thiebaut","France","1833","linen weaver","Weaver from Gérardmer in the Vosges; jacquard table, bath and bed linen.",rel=["Yves Delorme"]),
 B("Hästens","Sweden","1852","luxury bed maker","Köping bed maker founded by Pehr Adolf Janson; its stores also sell bedding and bed linen (the beds are in Furniture).",s="https://en.wikipedia.org/wiki/Hästens"),
 B("Brooklinen","United States","2014","direct-to-consumer bedding","Brooklyn direct-to-consumer bedding brand; percale, sateen and linen sets.",rel=["Parachute","Boll & Branch"]),
 B("Parachute","United States","2014","direct-to-consumer bedding","Los Angeles direct-to-consumer bed and bath brand.",rel=["Brooklinen"]),
 B("Boll & Branch","United States","2014","direct-to-consumer bedding","Direct-to-consumer brand selling organic cotton bedding.",rel=["Brooklinen"]),
]
notes=("Bedding / Bed linen. Five planned kinds kept (Sheet, Pillowcase, Duvet cover, Valance, Headboard cover); weave, fibre, flat/fitted and pillowcase styles moved into t. "
 "Cut the single Solace SKU (retail noise). Sheet models = test winners from NBC Select's 2026 tested roundup (Brooklinen, Parachute, Coop, California Design Den, Boll & Branch, L.L.Bean, Amazon Basics, The Citizenry, Quince, Sijo, Mulberry Park Silks); "
 "Wirecutter (nytimes.com) and HGTV duvet-cover page were blocked, Which?/CHOICE not reached, so no UK/AU test winners and no models for duvet covers/pillowcases. "
 "Luxury houses listed once as ranges on Sheet (not repeated across kinds) and in the brand register; Frette, Libeco and Hästens cite fetched Wikipedia pages, the rest are knowledge entries; founding years left out for Yves Delorme, D. Porthault and Anichini (unsure). "
 "Sferra and Pratesi have no Wikipedia article. No archetypes or traditions (tier shelf). Kept old sources for carried-over kinds except Sheet and Pillowcase, now on fetched Wikipedia pages.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/B2/shelves/01_00.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
