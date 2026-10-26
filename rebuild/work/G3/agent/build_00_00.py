import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=(),a="",dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Fitted kitchen","a":"built-in kitchen · kitchen system · kitchen cabinetry","d":"Whole installed kitchen of matching base and wall cabinets, island and built-in appliance housings planned as one system.",
 "t":["Shaker (framed panel doors)","handleless (push-to-open or rail)","face-frame (framed)","frameless (European)","inset doors","overlay doors","painted timber","lacquer","stainless steel","modular system","bespoke joinery"],
 "s":W+"Kitchen_cabinet",
 "x":[
  X("Frankfurt kitchen","Compact galley kitchen installed complete with cabinets and appliances; regarded as the first fitted kitchen.","Margarete Schütte-Lihotzky","1926",W+"Frankfurt_kitchen",
    [("Original New Frankfurt installations","","late 1920s","about 10,000 built for Ernst May's social housing"),("Museum reconstructions and replicas","","","MAK Vienna reconstruction; homeowner replicas")],
    dt="about 1.9 × 3.4 m galley · blue fronts · labelled storage bins · sliding door to living room"),
  X("Poggenpohl unit kitchen","Early unit kitchen with a continuous countertop over base units and matching wall units.","Poggenpohl","1950",W+"Poggenpohl",
    [("The Ideal (freestanding cupboard)","Poggenpohl","1923","forerunner"),("Reform kitchen","Poggenpohl","1928","")]),
  X("Boffi Minikitchen","Compact kitchen-system block designed with Joe Colombo, an icon of kitchen-system design.","Boffi","1963","https://www.boffi.com/en/about/",[("Minikitchen","Boffi","1963","Joe Colombo")]),
  X("Bulthaup System b","Kitchen furniture programme based on Otl Aicher's studies of kitchen work.","Bulthaup","1982",W+"Bulthaup",
    [("Concept 12 (C12)","Bulthaup","1974","planning on a 12 cm grid"),("System b","Bulthaup","1982","Otl Aicher"),("System 25","Bulthaup","1992","25 mm grid modular system"),("System 20","Bulthaup","1997","mobile wheeled containers")]),
  X("Bulthaup Kitchen Workbench","Freestanding stainless-steel workbench combining cooking area, sink and work surface.","Bulthaup","1988",W+"Bulthaup",[("Kitchen Workbench (KWB)","Bulthaup","1988","influenced by Otl Aicher")],a="KWB",dt="stainless steel"),
  X("Bulthaup b3","Kitchen and room system of panels and units hung from a wall-mounted rail system.","Bulthaup","2004",W+"Bulthaup",
    [("b3","Bulthaup","2004","with Herbert H. Schultes"),("b.architecture","Bulthaup","2018","developed from b3, focus on water and food preparation")]),
  X("Bulthaup b2","Open, workshop-style kitchen of freestanding workbench and tool cabinets.","Bulthaup","2008",W+"Bulthaup"),
  X("Bulthaup b Solitaire","Freestanding minimalist kitchen elements that can be placed like furniture.","Bulthaup","2014",W+"Bulthaup",[("b Solitaire","Bulthaup","2014","presented in Milan"),("Bulthaup System","Bulthaup","2024","solid wood and stainless steel range")]),
  X("Boffi Xila","Handleless kitchen system developed under creative director Luigi Massoni.","Boffi","",  "https://www.boffi.com/en/about/",[("T12","Boffi","1967","Pier Ugo and Gian Casé"),("E15","Boffi","","first modular concept")]),
  X("Boffi Factory","Kitchen designed by Antonio Citterio and Paolo Nava.","Boffi","1980","https://www.boffi.com/en/about/",[("Case 5.0","Boffi","2002","Piero Lissoni"),("K-Series","Boffi","2003","Norbert Wangen"),("Code","Boffi","2016","custom-made collection")]),
  X("SieMatic S1","Handle-free kitchen with lighting and multimedia integrated into the cabinetry.","SieMatic","2008",W+"SieMatic",[("S1","SieMatic","2008",""),("S2","SieMatic","","lower price point"),("S3","SieMatic","","lower price point")],dt="style collections Classic · Pure · Urban"),
  X("Poggenpohl P'7340","Kitchen developed with Porsche Design.","Poggenpohl","2007",W+"Poggenpohl",a="Porsche Design Kitchen"),
  X("deVOL Real Shaker Kitchen","Economical painted kitchen of freestanding and fitted cupboards inspired by authentic Shaker carpentry.","deVOL","","https://www.devolkitchens.co.uk/kitchens",dt="base and wall cupboards · prep tables · canopies · paint colours"),
  X("deVOL Classic English Kitchen","Bespoke kitchen with Georgian-style furniture.","deVOL","","https://www.devolkitchens.co.uk/kitchens",[("Heirloom Collection","deVOL","","vintage-furniture-inspired designs"),("Haberdasher's Kitchen","deVOL","","oak cupboards, mid-century English inspiration"),("Sebastian Cox Kitchen","deVOL","","collaboration with Sebastian Cox")]),
  X("Plain English cupboard kitchen","Handmade bespoke kitchen blending traditional Georgian joinery with modern design, built in Suffolk.","Plain English","1992","http://plainenglishdesign.co.uk/",dt="fifty bespoke colours · painted cupboards"),
 ]},
{"n":"Worktop","a":"countertop · work surface · benchtop","d":"Installed work surface laid over kitchen base cabinets.",
 "t":["high-pressure laminate","engineered quartz","granite","marble","quartzite","soapstone","slate","solid surface (acrylic or polyester)","stainless steel","copper or zinc","wood or butcher block","bamboo","concrete","tile","terrazzo","glass","paper composite"],
 "s":W+"Countertop",
 "x":[
  X("Formica laminate","Heat-resistant, wipe-clean decorative paper-and-melamine laminate bonded to a board core.","Formica","1913","https://en.wikipedia.org/wiki/Formica_(plastic)",
    [("Decorative printed laminate","Formica","1927","wood-grain and marble looks"),("Melamine resin laminate","Formica","1938","wider colour range")],dt="post-formed or self-edged · colours and printed patterns"),
  X("Corian","Acrylic solid-surface material of alumina trihydrate and PMMA, seamlessly joined and repairable.","DuPont","1971",W+"Corian",dt="colours · integrated sinks · seamless joints"),
  X("Caesarstone","Engineered quartz surface of crushed quartz bound with resin, an early commercial quartz worktop.","Caesarstone","1987",W+"Caesarstone",[("ICON","Caesarstone","2024","crystalline-silica-free surface")],dt="slab colours · finishes"),
 ]},
{"n":"Kitchen sink","a":"sink · basin","d":"Basin fitted into or under a kitchen worktop for washing food and dishes.",
 "t":["stainless steel","fireclay","porcelain","granite or quartz","cast iron","copper","soapstone","inset","undermount","apron-front","single or double bowl"],
 "s":W+"Sink",
 "x":[
  X("Butler's sink","Deep rectangular ceramic sink with a rounded rim, set into or onto the worktop.","","",W+"Sink",
    [("Belfast sink","","","with overflow weir; deeper, about 38 cm in a 1921 guide"),("London sink","","","no overflow weir; originally shallower")],a="Belfast sink · London sink"),
  X("Franke stainless sink","Stainless-steel inset sink unit, the maker's core product since the 1930s.","Franke","1930s","https://en.wikipedia.org/wiki/Franke_(company)",
    [("Nickeline and Monel sinks","Franke","1930s","before stainless steel"),("Compact sink system","Franke","1979","")]),
 ]},
{"n":"Kitchen tap","a":"kitchen faucet · sink mixer","d":"Valve and spout over the kitchen sink delivering hot and cold water, sometimes boiling or filtered water.",
 "t":["two-handle mixer","single-lever mixer","pull-out spray","pull-down spray","touchless (sensor)","boiling-water","filter","thermostatic"],
 "s":"https://en.wikipedia.org/wiki/Tap_(valve)",
 "x":[
  X("Quooker boiling-water tap","Mixer tap fed by a vacuum-insulated under-sink tank that dispenses instant boiling water at the spout.","Quooker","1987",W+"Quooker",
    [("Fusion","Quooker","2012","combined mixer and boiling tap"),("Flex","Quooker","2016","pull-out hose"),("CUBE","Quooker","2019","adds chilled and sparkling water"),("Front","Quooker","2022","")],a="Quooker",dt="tank about 110 °C · finishes"),
  X("Moen single-lever mixer","Single-handle mixing tap controlling flow and temperature with one lever.","Moen","1956",W+"Moen_Incorporated",
    [("1225 cartridge","Moen","1960s","cartridge used in most single-handle Moen taps"),("Licensed production","Grohe","1962","exclusive rights to make the Moen single-lever mixer")]),
  X("Grohe Ladylux","Pull-out spray kitchen mixer.","Grohe","1983",W+"Grohe",[("Ladylux","Grohe","1983",""),("Europlus","Grohe","1989","pull-out spray")],dt="chrome or stainless finish"),
 ]},
{"n":"Waste disposal unit","a":"garbage disposer · food waste disposer · garbage disposal","d":"Electric unit fitted under a sink that grinds food waste into the drain.",
 "t":["continuous feed","batch feed","water-powered"],
 "s":"https://www.insinkerator.com/en-in/products/residential/residential-disposers",
 "x":[
  X("InSinkErator disposer","Under-sink food waste disposer from the company of its inventor, John W. Hammes.","InSinkErator","1938",W+"InSinkErator",
    [("Evolution 100","InSinkErator","",""),("Evolution 200","InSinkErator","",""),("Model 46","InSinkErator","",""),("Model 56","InSinkErator","",""),("Model 66","InSinkErator","","")],dt="motor size · batch or continuous feed"),
 ],
 "m":[["Disposall","General Electric"]]},
]
def B(n,c,f,seg,d,s,lines=(),eras=(),sig=(),rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Bulthaup","Germany","1949","Luxury fitted kitchens","Kitchen maker from Aich near Landshut, founded by Martin Bulthaup; kitchens since 1951.",W+"Bulthaup",["b3","b2","b Solitaire","b.architecture"],["Otl Aicher collaboration, from 1980"],["Bulthaup b3","Bulthaup b2","Bulthaup Kitchen Workbench"],["Boffi","Poggenpohl","SieMatic"]),
 B("Boffi","Italy","1934","Luxury kitchens and bathrooms","Lentate sul Seveso kitchen and bathroom maker founded by Piero Boffi; merged with De Padova in 2015.","https://www.boffi.com/en/about/",["Xila","Factory","Case 5.0","K-Series","Code"],["Luigi Massoni, creative director from 1967","Piero Lissoni, art director from 1990"],["Boffi Minikitchen","Boffi Xila"],["Bulthaup"]),
 B("Poggenpohl","Germany","1892","Luxury fitted kitchens","Herford kitchen maker founded by Freidemir Poggenpohl; early unit kitchen in 1950.",W+"Poggenpohl",["P'7340 Porsche Design Kitchen"],[],["Poggenpohl unit kitchen","Poggenpohl P'7340"],["Bulthaup","SieMatic"]),
 B("SieMatic","Germany","1929","Premium fitted kitchens","Löhne kitchen maker founded by August Siekmann; kitchens grouped as Classic, Pure and Urban.",W+"SieMatic",["S1","S2","S3","Classic","Pure","Urban"],[],["SieMatic S1"],["Poggenpohl"]),
 B("deVOL","United Kingdom","1989","Bespoke English kitchens","Leicestershire kitchen maker founded by Philip deVries and Paul O'Leary, based at Cotes Mill.","https://www.devolkitchens.co.uk/about-us",["Real Shaker Kitchen","Classic English Kitchen","Heirloom Collection","Sebastian Cox Kitchen","Haberdasher's Kitchen"],[],["deVOL Real Shaker Kitchen"],["Plain English"]),
 B("Plain English","United Kingdom","1992","Bespoke English kitchens","Kitchen maker with workshops at Stowupland Hall, Suffolk, and a flagship on Pimlico Road, London.","http://plainenglishdesign.co.uk/",[],[],["Plain English cupboard kitchen"],["deVOL"]),
 B("Formica","United States","1913","Decorative laminates","Laminate maker founded by Westinghouse engineers Daniel J. O'Conor and Herbert A. Faber; now Formica Group.","https://en.wikipedia.org/wiki/Formica_(plastic)",[],[],["Formica laminate"]),
 B("Caesarstone","Israel","1987","Engineered quartz surfaces","Quartz-surface maker based at Kibbutz Sdot Yam, one of the first to commercialise engineered quartz.",W+"Caesarstone",["ICON"],[],["Caesarstone"]),
 B("Franke","Switzerland","1911","Sinks and kitchen systems","Aarburg maker of kitchen sinks and systems, founded by Hermann Franke as a sheet-metal business.","https://en.wikipedia.org/wiki/Franke_(company)",[],[],["Franke stainless sink"]),
 B("Quooker","Netherlands","1987","Boiling-water taps","Ridderkerk maker of boiling-water taps founded by Henri and Niels Peteri.",W+"Quooker",["Fusion","Flex","CUBE","Front"],[],["Quooker boiling-water tap"]),
 B("Grohe","Germany","1936","Taps and fittings","Taps and sanitary fittings maker founded by Friedrich Grohe; owned by Lixil since 2014.",W+"Grohe",["Ladylux","Europlus","Grohmix"],[],["Grohe Ladylux"],["Moen"]),
 B("Moen","United States","1956","Taps and fittings","North Olmsted tap maker started by inventor Alfred M. Moen; part of Fortune Brands Innovations.",W+"Moen_Incorporated",[],[],["Moen single-lever mixer"],["Grohe"]),
 B("Dornbracht","Germany","1950","Luxury bathroom and kitchen fittings","Iserlohn maker of high-end bathroom, spa and kitchen fittings, founded by Aloys F. Dornbracht.",W+"Dornbracht",[],[],[],["Grohe"]),
 B("InSinkErator","United States","1938","Food waste disposers","Racine maker of food waste disposers and hot-water dispensers founded by inventor John W. Hammes; owned by Whirlpool since 2022.",W+"InSinkErator",["Evolution"],[],["InSinkErator disposer"]),
]
notes=("All five planned kinds kept; old k12 merged into Waste disposal unit (its five InSinkErator models became versions of the InSinkErator disposer archetype; GE Disposall added from the garbage disposal article). "
 "Left out: Corian maker DuPont has no register entry (no DuPont page retrieved); Cosentino/Silestone, Blanco/Silgranit, Dornbracht tap series and SieMatic 6006 not confirmed on any retrieved page; no years for deVOL ranges or Boffi Xila. "
 "Bath/basin taps belong to Bath & wellness. No traditions added (no artisan-tradition sources for this shelf).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/G3/shelves/00_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
