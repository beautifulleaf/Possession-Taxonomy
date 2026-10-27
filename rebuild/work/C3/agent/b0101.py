import json, os
W='https://en.wikipedia.org/wiki/'; D='https://www.wikidata.org/wiki/'
def X(n,d,s,a='',mk='',y='',v=None,dt=''):
    o={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: o["v"]=[dict(zip(("n","mk","y","d"),vv)) for vv in v]
    if dt: o["dt"]=dt
    return o
kinds=[
 {"n":"African violet","a":"Saintpaulia · Streptocarpus sect. Saintpaulia","d":"Small rosette-forming gesneriad from Tanzania and Kenya grown indoors for year-round violet-like flowers.",
  "t":["micro and super-mini","mini and semi-mini","standard","large","trailing"],"s":W+"Saintpaulia",
  "x":[X("Saintpaulia ionantha","Original species described by Wendland in 1893; the parent of most houseplant cultivars.",D+"Q165406",a="Streptocarpus ionanthus · S. kewensis",y="1893",
         v=[("'Pink Amiss'","","","cultivar"),("'Red Velvet'","","","cultivar")],dt="rosette diameter class · single, double or frilled flowers · flower colour · variegated foliage"),
       X("Saintpaulia shumensis","Small species from the Usambara Mountains, grown by collectors of the species.",D+"Q17708576",a="Streptocarpus shumensis")]},
 {"n":"Cape primrose","a":"Streptocarpus · nodding violet (Streptocarpella)","d":"South African gesneriad with trumpet flowers on stalks above long strap leaves, grown as a houseplant.",
  "t":["rosulate hybrid","unifoliate","Streptocarpella (trailing)"],"s":W+"Streptocarpus",
  "x":[X("Streptocarpus rexii","First species described, reaching Kew in 1824; a parent of the early Victorian hybrids.",D+"Q7623337",y="1824",
         v=[("× Kewensis","","1886","early Kew hybrid"),("× Watsoni","","1887","early hybrid"),("Veitch's Original Hybrids","","","Veitch selections")]),
       X("Harlequin","Dibleys bicoloured hybrids; 'Harlequin Blue' was RHS Plant of the Year 2010.",W+"Dibleys_Nurseries",mk="Dibleys Nurseries",y="2010",
         v=[("'Harlequin Blue'","Dibleys Nurseries","2010","RHS Plant of the Year"),("'Harlequin Lace'","Dibleys Nurseries","","")]),
       X("Award of Garden Merit hybrids","Modern named hybrids holding the RHS Award of Garden Merit.",W+"Streptocarpus",
         v=[("'Crystal Ice'","","",""),("'Falling Stars'","","",""),("'Polka-Dot Purple'","","",""),("'Snow White'","","",""),("'Burgundy Ice'","","",""),("'White Butterfly'","","","")],
         dt="flower colour and veining · ruffled petals · leaf size"),
       X("Streptocarpus wendlandii","Unifoliate species with a single huge leaf; introduced in 1887.",D+"Q17708874",y="1887"),
       X("Streptocarpus dunnii","Red-flowered unifoliate species important to early hybrids.",D+"Q15445220"),
       X("Streptocarpus saxorum","Trailing Streptocarpella species with small lilac flowers, grown in hanging baskets.",D+"Q17708902",a="false African violet · nodding violet")]},
 {"n":"Bromeliad","a":"Bromeliaceae · Guzmania · Vriesea · Aechmea · Neoregelia","d":"Rosette-forming tropical American plant, often with a water-holding tank and long-lasting coloured bracts; air plants are listed separately.",
  "t":["tank epiphyte","terrestrial"],"s":W+"Bromeliaceae",
  "x":[X("Guzmania lingulata","Tank bromeliad with a star of red or orange bracts; in Europe since 1776.",D+"Q2710056",y="1776"),
       X("Aechmea fasciata","Silvery banded rosette with a pink bract head; introduced 1828.",D+"Q974721",a="urn plant",y="1828"),
       X("Vriesea splendens","Banded-leaf bromeliad with a flat red sword-shaped spike; introduced 1840.",D+"Q5220923",a="flaming sword",y="1840"),
       X("Neoregelia carolinae","Flat rosette whose centre turns red at flowering.",D+"Q3338220",a="blushing bromeliad"),
       X("Cryptanthus bivittatus","Small terrestrial star-shaped bromeliad with striped leaves.",D+"Q5190674",a="earth star"),
       X("Billbergia nutans","Clumping bromeliad with nodding pink-and-green flower spikes.",D+"Q1021163",a="queen's tears")]},
 {"n":"Poinsettia","a":"Euphorbia pulcherrima · Christmas star","d":"Mexican euphorbia sold at Christmas for its coloured bracts, usually red but also white, pink, cream and marbled.",
  "t":["red","white","pink","cream","marbled","novelty bract form"],"s":W+"Poinsettia",
  "x":[X("Euphorbia pulcherrima","Wild Mexican species, introduced to the US by Joel Poinsett in the 1820s; described 1834.",D+"Q208253",y="1834"),
       X("Freedom","Ecke Ranch series combining Hegg genetics with V-14 bract colour; dark foliage, early flowering.",'https://www.greenhousegrower.com/?p=10014',mk="Paul Ecke Ranch"),
       X("Prestige","Ecke Ranch series improving Freedom for shipping, with less branch breakage.",'https://www.greenhousegrower.com/?p=10014',mk="Paul Ecke Ranch"),
       X("Winter Rose","Ecke Ranch novelty with curled, rose-like bracts.",'https://www.greenhousegrower.com/?p=10014',mk="Paul Ecke Ranch")]},
 {"n":"Cyclamen","a":"florist's cyclamen · Cyclamen persicum · Persian cyclamen","d":"Tuberous Mediterranean plant with swept-back flowers and marbled leaves, sold in pots for winter colour.",
  "t":["standard","midi","mini"],"s":W+"Cyclamen_persicum",
  "x":[X("Cyclamen persicum","Wild species from Turkey to the Levant and North Africa, parent of all florist's cyclamen.",D+"Q150055"),
       X("Sierra","Seed series of florist's cyclamen.",W+"Cyclamen_persicum",v=[("Fuchsia","","",""),("Light Purple","","",""),("Pink with Eye","","",""),("Scarlet","","",""),("White with Eye","","","")]),
       X("Halios","Seed series of florist's cyclamen.",W+"Cyclamen_persicum",v=[("Bright Fuchsia","","",""),("Violet","","",""),("White","","","")]),
       X("Laser","Seed series of florist's cyclamen.",W+"Cyclamen_persicum",v=[("Rose","","",""),("Salmon with Eye","","",""),("Scarlet","","",""),("White","","","")]),
       X("Miracle","Seed series of florist's cyclamen.",W+"Cyclamen_persicum",v=[("Deep Rose","","",""),("Scarlet","","",""),("White","","","")]),
       X("Concerto","Seed series of florist's cyclamen.",W+"Cyclamen_persicum",v=[("'Concerto Apollo'","","","")])]},
 {"n":"Gardenia","a":"Gardenia jasminoides · cape jasmine","d":"Evergreen Asian shrub with glossy leaves and strongly scented white flowers, grown indoors in cool climates.",
  "t":["single","double"],"s":W+"Gardenia_jasminoides",
  "x":[X("Gardenia jasminoides","Wild species of southern East Asia; holds the RHS Award of Garden Merit.",D+"Q1072101"),
       X("'Fortuniana'","Large double-flowered sterile form, widely cultivated.",W+"Gardenia_jasminoides"),
       X("'Mystery'","Double-flowered upright cultivar to about 2 m, used for hedging.",W+"Gardenia_jasminoides"),
       X("'Kleim's Hardy'","Dwarf, star-flowered, cold-tolerant cultivar about 1 m high.",W+"Gardenia_jasminoides",
         v=[("'Crown Jewel'","","","hybrid of 'Kleim's Hardy' and 'Chuck Hayes'")]),
       X("'Radicans'","Low ground-cover form, 15–45 cm tall.",W+"Gardenia_jasminoides"),
       X("'Golden Magic'","Flowers open white and turn golden yellow.",W+"Gardenia_jasminoides"),
       X("'Summer Snow'","Cold-tolerant cultivar with flowers up to 11 cm across.",W+"Gardenia_jasminoides")]}]
brands=[{"n":"Dibleys Nurseries","c":"United Kingdom (Wales)","f":"1976","seg":"Streptocarpus breeder and nursery","d":"Family nursery at Llanelidan, Denbighshire, founded by Rex Dibley, best known for Streptocarpus and many RHS gold medals.","sig":["Harlequin"],"s":W+"Dibleys_Nurseries"},
 {"n":"Paul Ecke Ranch","c":"United States","seg":"Poinsettia breeder","d":"Ecke family poinsettia business in Encinitas, California, which developed grafting for bushy plants and long dominated the market.","sig":["Freedom","Prestige","Winter Rose"],"s":W+"Poinsettia"}]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"New shelf, six kinds. Archetypes are species (Wikidata) and named cultivars/series from Wikipedia and Greenhouse Grower. African violet size classes as t; AVSA is the cultivar registration authority (noted, no entry). Cyclamen series makers not given by the source, so mk left empty. Dümmen Orange and Optimara not added: no retrieved page linking them to named lines. No traditions."}
p='work/C3/shelves/01_01.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
