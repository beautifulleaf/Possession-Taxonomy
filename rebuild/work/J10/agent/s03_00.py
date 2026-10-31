import json
W='https://en.wikipedia.org/wiki/'
CE=W+"Construction_of_electronic_cigarettes"
V="https://www.vapesuperstore.co.uk/"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
kinds=[
{"n":"Disposable vape","a":"big puff","d":"Sealed vape sold prefilled and charged, used up and discarded.","t":["Nicotine-salt disposable","Rechargeable disposable"],"s":V,
 "x":[x("Elf Bar","Elf Bar","2018",W+"Elf_Bar","Disposable brand by Shenzhen iMiracle; Elf Bar 600 with a pre-filled 20 mg nicotine-salt tank was the world's best-selling disposable by 2023; sold as EB Create in the US.",[("Elf Bar 600","iMiracle","2018","Best-known model")])],
 "m":[["SKE Crystal Bar","SKE"],["Dojo Blast","Vaporesso"]],"r":[["Crystal","SKE Crystal"]]},
{"n":"Refillable pod kit","a":"pod mod","d":"Device with a battery body and refillable or replaceable pods.","t":["Closed pod","Open pod"],"s":V,
 "x":[x("JUUL","Juul Labs","2015",W+"Juul","USB-stick-shaped pod device introduced by Pax Labs in June 2015, using nicotine-salt pods; Juul Labs spun off in 2017.",[("JUUL","Juul Labs","2015","Original device")])],
 "m":[["Xlim","OXVA"],["Novo Axis EZ","SMOK"],["XROS 6","Vaporesso"],["Argus Z3","VooPoo"]]},
{"n":"Vape pen kit","a":"","d":"Pen-shaped battery with a tank or cartridge, sold together as a kit.","t":["Cartridge pen","Tank pen"],"s":V},
{"n":"Box mod kit","a":"box mod","d":"Box-shaped regulated battery device with a separate tank, adjustable power and sometimes temperature control.","t":["Single battery","Dual battery","Regulated","Temperature control"],"s":V,
 "x":[x("Evolv DNA mod","Evolv","","https://vaping360.com/best-vape-mods/dna-mods/","Box mod built on an Evolv DNA chipset, configured through EScribe software; DNA40 is also cited as a temperature-control board.",
        [("Therion 2 DNA250C","LVE (Lost Vape)","","Dual-battery DNA250C box"),("Harrier DNA60C","Early Bird","","Single 21700 or 18650"),("Sidera DNA60C","Innokin","","Single 18650"),("Paramour DNA80C","Mechvape x Evolv","","Single 21700 or 18650")])]},
{"n":"Mechanical mod","a":"mech mod","d":"Switch-fired tube or box battery body with no circuitry or power regulation, using 18350 to 18650 cells.","t":["Tube mech","Box mech"],"s":CE},
{"n":"Squonk mod","a":"bottom-feeder · BF mod","d":"Mod with an in-body bottle of e-liquid squeezed to feed the atomiser through a 510 connection.","t":["Mechanical squonker","Regulated squonker"],"s":CE},
]
brands=[
{"n":"Elf Bar","c":"China","f":"2018","seg":"Mainstream","kf":"disposables","d":"Disposable brand of Shenzhen iMiracle Technology.","s":W+"Elf_Bar"},
{"n":"Juul Labs","c":"United States","f":"2015","seg":"Mainstream","kf":"pod device","d":"San Francisco company founded 22 May 2015; its JUUL pod device launched June 2015.","s":W+"Juul"},
]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Dropped from brief for lack of a retrieved page: Dicodes, SX Mini, Lost Vape Centaurus, Geekvape Aegis, Kennedy, Avid Lyfe, Uwell Caliburn. Vaping360 DNA page fetched via Firecrawl after WebFetch 403. Old models kept in m (SKE, Vaporesso, OXVA, SMOK, VooPoo)."},open('s03_00.json','w'),ensure_ascii=False)
