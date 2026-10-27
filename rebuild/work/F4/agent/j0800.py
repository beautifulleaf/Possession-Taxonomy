import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/F4/agent')
from w import save
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Coffin","a":"casket","d":"Box that holds a body for burial or cremation; coffin plate, handles and lining are fittings. Rental caskets are included.",
 "t":["coffin (tapered)","casket (rectangular)","steel","wood","cardboard or X-Board","bamboo, willow or banana leaf","mycelium","rental casket","coffin plate","coffin pillow and lining"],"s":W+"Coffin",
 "r":[["Caskets and urns","Batesville Casket Company"],["Wooden and metal caskets","Matthews Aurora Funeral Solutions"],["Coffin range","Co-op Funeralcare"]],"m":[]},
{"n":"Burial shroud","a":"winding sheet","d":"Cloth or set of cloths that wrap the body, in natural fibre.","t":["white cotton","linen","wool","hemp","tachrichim","kaffan"],"s":W+"Shroud",
 "r":[["Shroud","Loop Biotech"]],"m":[]},
{"n":"Cremation urn","a":"","d":"Container for cremated remains, of any capacity from a keepsake portion to a companion pair; scattering urns and urn plaques are types.",
 "t":["keepsake (1-50 cubic inches)","companion (about 400+ cubic inches)","pet","scattering","biodegradable","military","urn plaque or medallion"],"s":"https://www.memorials.com/catalog/cremation-urns",
 "r":[["Cremation urns","Memorials.com"],["Cremation urns","Batesville Casket Company"],["Urns for cremated remains","Matthews Aurora Funeral Solutions"]],"m":[]},
{"n":"Urn vault","a":"grave liner · burial vault","d":"Outer box or liner made to hold an urn or coffin in the ground and stop the grave collapsing.","t":["concrete","grave liner","urn vault"],"s":W+"Burial","m":[]},
{"n":"Grave marker","a":"tombstone · gravestone · headstone · tomb slab","d":"Stone or plaque set on or at a grave (tombstone, tomb slab named forms).","t":["headstone","footstone","ledger slab","plaque","granite","bronze","wood"],"s":W+"Gravestone","m":[["Headstone",""]]}
]
brands=[
{"n":"Batesville Casket Company","c":"United States","f":"1884","seg":"Professional & flagship","kf":"steel caskets","d":"Batesville, Indiana casket and urn maker, owned by LongRange Capital since 2023.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Batesville_Casket_Company"},
{"n":"Matthews Aurora Funeral Solutions","c":"United States","f":"1890","seg":"Professional & flagship","kf":"wood and metal caskets","d":"Former Aurora Casket Company of Aurora, Indiana; part of Matthews International since 2015.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Matthews_Aurora_Funeral_Solutions"},
{"n":"Co-op Funeralcare","c":"United Kingdom","f":"","seg":"Own-label & retailer","kf":"funeral director","d":"UK's largest funeral director, subsidiary of The Co-operative Group, running the UK's largest coffin factory.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Co-op_Funeralcare"},
{"n":"Loop Biotech","c":"Netherlands","f":"","seg":"Artisan & independent","kf":"mycelium coffins","d":"Delft company selling biodegradable shrouds and the Living Cocoon coffin.","lines":["Living Cocoon","ForestBed","Shroud"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://loop-biotech.com/product/shroud/"},
{"n":"Memorials.com","c":"United States","f":"","seg":"Own-label & retailer","kf":"online urns","d":"Online funeral and memorial retailer of urns, caskets and headstones.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://www.memorials.com/catalog/cremation-urns"}]
save('08_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Co-op Funeralcare coffin SKUs (Adora, Asta, Beata, Dulcinea, Sancia, Valentino) and 8 Memorials.com urn SKUs dropped as SKU lists; maker/retailer ranges kept in r. Coffin plate/pillow and scattering urn/plaque folded in as types. No retrieved page for Australian or other regional urn retailers; Loop founding year not on page; Co-op founding not stated. Market-share claim for Matthews (38%, 2005) not used."})
