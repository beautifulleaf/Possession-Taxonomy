import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
PS=W+"Agneau_de_pr%C3%A9-sal%C3%A9"; SM=W+"Salt_marsh_lamb"
HW="https://assets.publishing.service.gov.uk/media/5fd3647de90e076634d0177f/pfn-lakeland-herdwick-pdo.pdf"
kinds=[
{"n":"Salt-marsh lamb","a":"saltmarsh lamb · agneau de pré-salé","d":"Lamb from sheep grazed on tidal salt marshes of salt-tolerant grasses and herbs such as samphire and sea lavender.",
 "s":SM,
 "x":[X("Prés-salés de la baie de Somme AOP","Salt-marsh lamb from the Somme bay in Picardy; AOC in 2006, EU PDO in 2013.","","2006",PS,[],"cut · whole or half"),
      X("Prés-salés du Mont-Saint-Michel AOP","Salt-marsh lamb raised near Mont-Saint-Michel in Normandy, registered as a PDO in 2013.","","2013",PS,[],"cut · whole or half"),
      X("Gower salt marsh lamb","Lamb grazed on the salt marshes of the Gower Peninsula in Wales.","","",SM,[],"cut"),
      X("Morecambe Bay salt marsh lamb","Lamb grazed on the salt marshes of Morecambe Bay in north-west England.","","",SM,[],"cut")],
 "dt":"marsh · cut · season"},
{"n":"Protected-origin & breed lamb","a":"PDO lamb · PGI lamb · breed lamb","d":"Lamb sold under a protected regional name or a named sheep breed.",
 "t":["PDO","PGI","Label Rouge"],
 "s":"https://www.gov.uk/protected-food-drink-names/welsh-lamb",
 "x":[X("Welsh Lamb PGI","Lamb from Wales protected as a geographical indication since 2003, guarded by Hybu Cig Cymru.","Hybu Cig Cymru","2003","https://www.gov.uk/protected-food-drink-names/welsh-lamb",[],"cut"),
      X("Lakeland Herdwick PDO","Meat of pure-bred Herdwick sheep born, raised and slaughtered in Cumbria; lambs are 8–12 months at slaughter.","Herdwick Sheep Breeders Association","",HW,
        [{"n":"Lakeland Herdwick lamb","mk":"","y":"","d":"8–12 months, 14–22 kg deadweight"},{"n":"Lakeland Herdwick shearling and mutton","mk":"","y":"","d":"shearling 15 months–2 years; mutton usually over 2 years"}],"age · cut"),
      X("Shetland Lamb PDO","Fresh lamb from Shetland, registered as a PDO with the EU in 1996.","","1996","https://www.gov.uk/protected-food-drink-names/shetland-lamb",[],"cut"),
      X("Orkney Lamb PDO","Fresh lamb from Orkney, registered as a PDO with the EU in 1996.","","1996","https://www.gov.uk/protected-food-drink-names/orkney-lamb",[],"cut"),
      X("Agneau de Sisteron IGP","Young, light Provençal lamb of 13–19 kg from hardy breeds such as Mérinos, also sold as Label Rouge.","","","https://www.reussir.fr/patre/lagneau-de-sisteron-un-label-toujours-en-progression",[],"label (IGP, Label Rouge) · cut")],
 "dt":"designation · breed · cut"},
{"n":"Suckling lamb","a":"milk-fed lamb · lechazo · cordero lechal · abbacchio","d":"A whole milk-fed young lamb, sold whole or in halves and legs.",
 "t":["whole","half","leg"],
 "s":"https://www.tienda.com/products/suckling-leg-of-lamb-moralejo-me-09",
 "x":[X("Lechazo de Castilla y León IGP","Churra, Castellana or Ojalada suckling lamb fed only on its mother's milk and slaughtered by 35 days at 9–12 kg live.","","","https://www.foodswinesfromspain.com/en/food/products/fresh-meat/lechazo-de-castilla-y-leon-pgi",[],"carcass 4.5–8 kg · with or without head and pluck"),
      X("Abbacchio Romano IGP","Lazio lamb raised semi-wild from Sarda, Sopravissana and other native breeds, with pale pink, lean meat.","","","https://www.arsial.it/wp-content/uploads/2025/06/AbbacchioRomanoIGP.pdf",[],"cut")]},
{"n":"Mutton & hogget","a":"mutton · hogget · hogg · whole lamb","d":"Meat of older sheep (hogget up to about two years, mutton older), and whole or half lamb carcasses.",
 "t":["hogget","mutton","whole lamb","half lamb"],
 "s":"https://www.realfoodhub.co.uk/category/meat-poultry/lamb"},
]
brands=[{"n":"Herdwick Sheep Breeders Association","c":"United Kingdom","f":"","seg":"Institution & issuer","kf":"Lakeland Herdwick PDO","d":"Breed society named as the applicant group for the Lakeland Herdwick PDO.","lines":[],"eras":[],"sig":["Lakeland Herdwick PDO"],"sc":[],"rel":[],"s":HW}]
notes=("Old 'Lamb' catch-all (k51) dissolved into 'Mutton & hogget' with types; old 'Suckling lamb' (k52) kept. Cabrito goes to Goat. Hybu Cig Cymru brand entry is in shelf 00_00. "
"Left out (no page retrieved): Agneau de Pauillac IGP (INAO PDF 503, Firecrawl timed out), Cordero Manchego, New Zealand lamb, Texel/Suffolk crosses, Mutton Renaissance (named on the Mutton article but no details). Hogget/mutton definitions from https://en.wikipedia.org/wiki/Mutton.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/02_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
