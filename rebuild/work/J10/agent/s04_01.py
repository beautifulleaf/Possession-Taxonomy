import json
W='https://en.wikipedia.org/wiki/'
SN=W+"Snuff_(tobacco)"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
kinds=[
{"n":"Nasal snuff","a":"dry snuff","d":"Finely ground dry tobacco taken through the nose, plain or scented with spice, fruit, floral or menthol.","t":["Fine snuff","Scented snuff","Medicated snuff","Tobacco-free snuff"],"s":"https://en.wikipedia.org/wiki/List_of_tobacco_products",
 "x":[x("German snuff","","",SN,"Pungent traditional German blends such as Schmalzler and Brasil.",[("Schmalzler","","",""),("Brasil","","","")]),
      x("Pöschl Weiss","Pöschl","",SN,"Tobacco-free snuff alternative from Pöschl.")],
 "m":[["Carhart's CC",""],["Peach Sweet",""],["Tube Rose",""]]},
{"n":"Moist snuff","a":"dip","d":"Moist ground tobacco placed between lip and gum.","t":["Fine cut","Long cut","Pouch"],"s":"https://en.wikipedia.org/wiki/List_of_tobacco_products",
 "x":[x("Copenhagen","U.S. Smokeless Tobacco Company","1822",W+"Dipping_tobacco","American moist snuff brand; dipping tobacco evolved from dry snuff."),
      x("Skoal","U.S. Smokeless Tobacco Company","1934",W+"Dipping_tobacco","Moist snuff brand in production from 1934; ReadyCut is a pouch form.",[("Skoal Bandits","","","Pouched snuff")]),
      x("Grizzly","American Snuff Company","",W+"Dipping_tobacco","American dip brand, also in a wide cut.")]},
{"n":"Chewing tobacco","a":"","d":"Loose leaf, plug or twist tobacco made for chewing.","t":["Loose leaf","Plug","Twist","Kautabak stick"],"s":W+"Chewing_tobacco",
 "x":[x("Red Man","","",W+"Chewing_tobacco","Loose-leaf brand now sold as America's Best Chew."),
      x("Beech-Nut","","",W+"Chewing_tobacco","Chewing brand linked to Lorillard."),
      x("Levi Garrett","","",W+"Chewing_tobacco","Loose-leaf chewing brand."),
      x("Stoker's","","",W+"Chewing_tobacco","Chewing and dipping brand.")],
 "m":[["Grimm und Triepel stick","Grimm und Triepel"],["La Corona stick","La Corona"],["Jackson's Apple Jack","Swisher International"]]},
{"n":"Snuff box","a":"","d":"Small airtight box for carrying snuff, from horn to gold and enamel; mostly 18th and 19th century.","t":["Gold","Silver","Enamel","Tortoiseshell","Papier-mâché","Porcelain"],"s":"https://www.1stdibs.com/buy/antique-snuff-boxes/"},
{"n":"Snuff bottle","a":"Chinese snuff bottle","d":"Small stoppered Chinese bottle with an attached spoon for powdered snuff, in glass, porcelain, hardstone and other materials.","t":["Glass","Porcelain","Jade and hardstone","Inside-painted","Enamel"],"s":W+"Snuff_bottle",
 "x":[x("Imperial glass snuff bottle","","1696",W+"Snuff_bottle","Glass bottles from the imperial workshop opened in Beijing in 1696 after the Kangxi Emperor's 1693 order; includes glass-overlay and hardstone imitations."),
      x("Porcelain snuff bottle","","",W+"Snuff_bottle","Traditionally blue and white, later with coloured glazes."),
      x("Inside-painted snuff bottle","","late 1800s",W+"Snuff_bottle","Bottle decorated from inside through the neck with special pens, generally not meant for snuff.")]},
]
trad=[{"n":"Chinese snuff bottles","g":"Glass & ceramics","r":"China (Beijing, Guangzhou)","p":"1690s to early 1900s","d":"Status objects of the Qing court and elite, made in glass, porcelain, hardstone and enamel.","tech":"Glass blowing and overlay, porcelain, hardstone carving, inside painting","mat":"Glass, porcelain, jade, agate, amber, coral, ivory","forms":["Snuff bottle"],"ctr":["Beijing palace glassworks","Guangzhou court workshops","Boshan"],"auth":"Original stopper and spoon rarely survive; imperial pieces are most prized.","s":W+"Snuff_bottle"}]
json.dump({"kinds":kinds,"brands":[],"traditions":trad,"notes":"Wilsons of Sharrow, Fribourg & Treyer, Gawith Apricot, Bernard not on retrieved pages; omitted. Chewing list trimmed to Red Man, Beech-Nut, Levi Garrett, Stoker's (old list of 12) plus German sticks and Apple Jack kept in m; Brown's Mule, Cannon Ball, Days Work, Piccanell, Oliver Twist, America's Best Chew dropped as duplicates or low coverage. Moist snuff old ranges kept via archetypes."},open('s04_01.json','w'),ensure_ascii=False)
