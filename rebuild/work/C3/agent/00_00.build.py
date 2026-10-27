import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,s,y='',v=(),dt='variegation · leaf form · plant size (node, cutting, established)',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
kinds=[
 {"n":"Monstera","a":"Swiss cheese plant · Monstera deliciosa · M. adansonii","d":"Living climbing aroid of the genus Monstera, grown for large leaves with splits and holes.",
  "t":["green","variegated"],"s":"https://botachoku.com/foliage","x":[
  X("Monstera deliciosa","Swiss cheese plant · split-leaf philodendron · delicious monster","Large climbing aroid from southern Mexico to Panama with glossy leaves that develop splits and holes.",W+"Monstera_deliciosa",
    v=[("'Variegata'","","","RHS Award of Garden Merit"),("Thai Constellation","","",""),("Albo Variegata","","","")]),
  X("Monstera adansonii","Adanson's monstera · Swiss cheese vine · five holes plant · monkey mask plant","Tropical American vine with heart-shaped waxy leaves pierced by large oval holes.",W+"Monstera_adansonii",y="1830",
    v=[("'Archipelago'","","","variegated leaves")]),
  X("Monstera obliqua","","Rarely cultivated Central and South American species with highly perforated leaves; the name is often misapplied to M. adansonii.",W+"Monstera_obliqua"),
 ]},
 {"n":"Philodendron","a":"heartleaf philodendron · Pink Princess · Birkin","d":"Living climbing or creeping aroid of the genus Philodendron, grown for heart-shaped or velvety leaves.",
  "t":["climbing","creeping","self-heading","velvet-leaf","variegated"],"s":"https://botachoku.com/foliage","x":[
  X("Philodendron hederaceum","heartleaf philodendron · P. scandens · velvet-leaf philodendron · P. micans","Evergreen climbing philodendron from Central America and the Caribbean, the classic trailing houseplant.",W+"Philodendron_hederaceum",
    v=[("Brasil","","",""),("Micans","","","velvet-leaf form sold as P. micans")]),
  X("Philodendron erubescens","blushing philodendron · red-leaf philodendron","Colombian climbing philodendron with red stems; parent of many self-heading cultivars.",W+"Philodendron_erubescens",
    v=[("'Pink Princess'","","",""),("'Prince of Orange'","","",""),("'Imperial Red'","","",""),("'Red Emerald'","","",""),("'Burgundy'","","",""),("'White Princess'","","",""),("'Green Princess'","","",""),("'Black Cardinal'","","",""),("'Moonlight'","","",""),("'McColley's Finale'","","","")]),
  X("Philodendron gloriosum","","Creeping Colombian philodendron with large velvety heart-shaped leaves, pink margins and pale veins.",W+"Philodendron_gloriosum",dt="leaf size · vein colour · plant size (node, cutting, established)"),
  X("Philodendron melanochrysum","black gold philodendron","Colombian climber whose velvety leaves open copper-gold and mature blackish green with pale veins.",W+"Philodendron_melanochrysum"),
  X("Philodendron verrucosum","","Climbing Andean and Central American species with wavy, white-veined leaves and bristly petioles.",W+"Philodendron_verrucosum"),
  X("Philodendron billietiae","","Hemi-epiphyte from Brazil and the Guianas with orange-yellow petioles and long wavy-edged leaves.",W+"Philodendron_billietiae",y="1995"),
  X("Philodendron 'Birkin'","Birkin","Self-heading cultivar with white-striped leaves, a sport found among 'Rojo Congo' plants.","https://getplanta.com/article/trivia/birkin",dt="stripe density · reversion · plant size"),
 ]},
 {"n":"Pothos","a":"Epipremnum · devil's ivy · golden pothos · E. aureum","d":"Living climbing aroid of the genus Epipremnum, mainly pothos (E. aureum).",
  "t":["green","variegated"],"s":"https://botachoku.com/foliage","x":[
  X("Epipremnum aureum","golden pothos · devil's ivy · money plant","Evergreen climbing vine from Mo'orea, the most widely grown trailing houseplant.",W+"Epipremnum_aureum",
    v=[("Golden","","",""),("Marble Queen","","","white marbling"),("Neon","","","bright chartreuse leaves"),("N'Joy","","","small variegated leaves, slow"),("Global Green","","","green-on-green variegation"),("Manjula","","","cream centres, dark green margins"),("Pearls and Jade","","","small green dots"),("Jade","","","solid green"),("Jessenia","","",""),("Shangri-La","","","crinkled curled leaves")]),
  X("Epipremnum pinnatum","centipede tongavine · dragon-tail plant","Old World tropical climber, from northern Australia to southern China and Japan, that becomes epiphytic as it climbs.",W+"Epipremnum_pinnatum",
    v=[("Cebu Blue","","","")]),
 ]},
 {"n":"Satin pothos","a":"Scindapsus · S. pictus · silver pothos","d":"Living climbing aroid of the genus Scindapsus, including satin pothos (S. pictus).",
  "t":["silver-spotted","silver-splashed"],"s":"https://botachoku.com/foliage","x":[
  X("Scindapsus pictus","satin pothos · silver pothos · silver vine","Evergreen climber from South and Southeast Asia with matt leaves flecked silver.",W+"Scindapsus_pictus",
    v=[("'Argyraeus'","","",""),("'Exotica'","","",""),("'Silvery Ann'","","",""),("'Silver Lady'","","",""),("'Silver Satin'","","",""),("'Silver Splash'","","",""),("'Jade Satin'","","","")]),
 ]},
 {"n":"Arrowhead vine","a":"Syngonium · arrowhead plant · nephthytis","d":"Living arrowhead vine, genus Syngonium (Araceae).",
  "t":["green","pink","variegated"],"s":"https://mountaincrestgardens.com/","x":[
  X("Syngonium podophyllum","arrowhead plant · goosefoot · nephthytis","Climbing aroid from Mexico to Bolivia with arrow-shaped juvenile leaves; RHS Award of Garden Merit.",W+"Syngonium_podophyllum",
    v=[("'White Butterfly'","","","")]),
 ]},
 {"n":"Thaumatophyllum","a":"tree philodendron · Philodendron Xanadu · selloum","d":"Living self-heading aroid of the genus Thaumatophyllum, the former tree philodendrons.",
  "s":"https://botachoku.com/foliage","x":[
  X("Thaumatophyllum bipinnatifidum","lacy tree philodendron · selloum · horsehead philodendron · Philodendron selloum","Large South American aroid with deeply lobed drooping leaves on a thick trunk-like stem.",W+"Thaumatophyllum_bipinnatifidum",
    v=[("'Hope'","","","")],dt="leaf lobing · plant size"),
  X("Thaumatophyllum xanadu","Philodendron Xanadu · 'Winterbourn' · 'Showboat'","Compact clump-forming species with glossy lobed leaves, found as a chance seedling in a Western Australian nursery in 1983.",W+"Thaumatophyllum_xanadu",y="1983",
    v=[("'Xanadu'","House Plants of Australia","1988","released as plant of the year")],dt="plant size"),
 ]},
 {"n":"Rhaphidophora","a":"mini monstera · R. tetrasperma","d":"Living climbing aroid of the genus Rhaphidophora, from tropical Africa to the Western Pacific.",
  "t":["juvenile","mature fenestrated"],"s":W+"Rhaphidophora","x":[
  X("Rhaphidophora tetrasperma","mini monstera","Climber from southern Thailand and Malaysia whose leaves split into lobes as it matures.",W+"Rhaphidophora_tetrasperma"),
  X("Rhaphidophora decursiva","","Climbing aroid from China, the Indian subcontinent and Indochina.",W+"Rhaphidophora_decursiva"),
 ]},
]
notes=("Merged old Philodendron species kinds and the hybrid kind (Birkin) into one Philodendron kind; old flat models became versions (Thai Constellation, Albo, Brasil, Micans, Cebu Blue, pothos cultivars). "
 "Cultivar lists taken from the Wikipedia species pages fetched this session; Birkin from getplanta.com. No brand register entries: archetypes are species/cultivars without makers. "
 "Left out: P. 'Rojo Congo' and Thai Constellation origin details (not confirmed on a retrieved page); Wikidata was rate-limited (HTTP 429), so Wikipedia used throughout.")
out={"kinds":kinds,"brands":[],"traditions":[],"notes":notes}
p='work/C3/shelves/00_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
