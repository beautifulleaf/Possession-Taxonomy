import json
TU='https://wp.tobacconistuniversity.org/?p=19643'
def x(n,mk,s,d): return {"n":n,"a":"","d":d,"mk":mk,"y":"","s":s}
kinds=[
{"n":"Pipe tamper & tool","a":"pipe tool","d":"Small tool for pressing down burning tobacco in the bowl, often combined with a pick and reamer.","t":["Pipe nail","Three-in-one (Czech) tool","Decorative tamper"],"s":"https://www.flyingtigerantiques.com/1950s-dunhill-pipe-tamper-tool-in-brass-stainless-steel-brindle-vulcanite.html"},
{"n":"Pipe cleaner","a":"","d":"Disposable wire-and-cotton cleaner that wicks moisture and char from the pipe's airhole.","t":["Bristle","Fluffy","Tapered"],"s":"https://www.ebay.com/p/1394277360"},
{"n":"Pipe filter","a":"","d":"Charcoal, balsa or paper filter insert for a filter pipe.","t":["9 mm charcoal","6 mm balsa","Paper"],"s":"https://www.ebay.de/itm/255531431311"},
{"n":"Pipe reamer","a":"cake cutter","d":"Tool that scrapes carbon cake from the inside of a pipe bowl with turned blades.","t":["Four-head fixed reamer","Adjustable reamer"],"s":"https://rebornpipes.com/tag/castleford-pipe-reamers/",
 "x":[x("Castleford reamer","Castleford","https://rebornpipes.com/tag/castleford-pipe-reamers/","Plastic T-handle reamer with four fixed-blade heads."),
      x("Senior reamer","Senior","https://rebornpipes.com/tag/castleford-pipe-reamers/","Lighter reamer with a flatter central cone, compared with the Kleen Reem.")]},
{"n":"Pipe stand & rack","a":"pipe rack","d":"Stand or rack that holds tobacco pipes when not in use, from single holders to multi-pipe racks.","t":["Single stand","Multi-pipe rack"],"s":"https://www.ebay.com/itm/405490839841"},
{"n":"Pipe case & bag","a":"","d":"Case or bag for carrying one or more pipes and sometimes tools.","t":["Pipe bag","Hard case"],"s":TU},
{"n":"Tobacco pouch","a":"","d":"Pouch with a non-hygroscopic liner for carrying pipe or roll-your-own tobacco.","t":["Roll-up","Zipper","Pipe-combo","Leather"],"s":"https://www.haddockslightershop.com/en/smoking-supplies/roll-your-own-pouch/","m":[["Kamasu",""]]},
{"n":"Tobacco jar","a":"cellaring jar","d":"Airtight jar or container for storing and ageing pipe tobacco; gasketed glass mason-style jars are recommended.","t":["Glass jar","Tupperdor","Humidor"],"s":"https://bespokeunit.com/pipes/tobacco/cellaring/"},
]
json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":"Restraint shelf. Czech tool, charcoal/balsa filter sizes and roll-up/combo pouch types follow the brief; not separately sourced. New kinds Pipe reamer, Pipe case & bag, Tobacco jar sourced from retrieved pages. Castleford and Senior kept as the two named reamers. No brands registered."},open('s01_02.json','w'),ensure_ascii=False)
