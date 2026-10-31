from dsl import *
S=lambda *a:[["A1",x,y] for x,y in a]
A=["Levi's 501","Levi's 505","Levi's 517 Bootcut","Levi's 511 Slim","Levi's 550 Relaxed","Lee 101 Riders","Wrangler 13MWZ Cowboy Cut"]
B=["Warehouse Lot 1001XX","Sugar Cane 1947","Full Count 1101","TCB 50s","Studio D'Artisan SD-101","Iron Heart IH-634","Samurai S710XX","The Flat Head 3000 series","Pure Blue Japan XX-013","Momotaro Standard Collection","Japan Blue J301","Evisu Lot 2000 No. 2"]
C=["A.P.C. Petit Standard","Nudie Jeans named fits","JNCO wide-leg"]
JEANS={
"JEANS_A":N("Heritage American jeans","501s · Levi's · Lee Riders · Wrangler jeans","Five-pocket denim jeans in the patterns the American makers still sell: Levi's, Lee and Wrangler.",WP+"Jeans",
 "Leg shape: Straight | Slim | Tapered | Bootcut | Relaxed ;; Rise: Low | Mid | High ;; Fly: Button | Zip ;; Finish: Raw or rinse | Stonewash | Distressed",take={"Jeans":A},see=S(("Trucker jacket","matching denim jacket"))),
"JEANS_B":N("Selvedge reproduction jeans","selvedge jeans · raw denim · Japanese repro jeans","Jeans that copy 1930s to 1960s American patterns in selvedge denim, led by Japanese makers.",WP+"Jeans",
 "Denim: Selvedge | Unsanforized shrink-to-fit | Sanforized ;; Finish: Raw or dry | One-wash | Distressed ;; Leg shape: Straight | Slim tapered | Wide straight ;; Fly: Button | Zip",take={"Jeans":B}),
"JEANS_C":N("Fashion & designer jeans","designer denim · premium jeans","Jeans cut and washed by fashion labels rather than copying a heritage pattern.",WP+"Jeans",
 "Leg shape: Skinny | Slim | Wide-leg or baggy | Flare | Boyfriend | Mom ;; Rise: Low | Mid | High ;; Wash: Raw | Stone-wash | Acid-wash ;; Fabric: Rigid | Stretch",take={"Jeans":C}),
}
DEPTS_B=[
DP("Coats & jackets","Outer layers worn over other clothes, by origin and use; a tailored suit jacket → Suits & formalwear, trade jackets sold as workwear → Workwear & uniform clothing.",
 "What is the outer layer for: town and weather coats, military issue, riding and country, casual sportswear, or technical outdoor use?",[
 SH("Town & weather coats","Long coats worn over clothes against cold and rain, from tailored overcoats to parkas and capes.",
  "kinds by weather: tailored wool, rain, deep cold, then the loose cape",[
  K("Overcoat","Breast: Single | Double ;; Collar: Notch | Velvet | Fur ;; Sleeve: Set-in | Raglan ;; Length: Topcoat | Full ;; Lining: Fixed | Zip-in or button-in",see=S(("Pea coat","shorter naval coat"))),
  K("Pea coat","Cut: Classic hip length | Bridge coat (thigh) ;; Style: Reefer (officer's) | Plain ;; Cloth: Melton wool | Leather"),
  K("Duffle coat","Fastening: Wooden toggles with jute loops | Horn toggles with leather loops ;; Hood: Pancake | Classic ;; Length: Short | Mid-length"),
  K("Trench coat","Breast: Double (classic) | Single ;; Length: Short | Knee | Long ;; Lining: Check | Detachable wool | Plain ;; Colour: Honey | Stone | Navy | Black"),
  K("Raincoat","Coating: Rubberised cotton | PU or PVC | Waxed | Breathable laminate ;; Cut: Balmoral | Hooded | Long ;; Form: Mac | Poncho"),
  K("Parka","Type: Fishtail military | Snorkel (N-3B) | Down expedition | Wool ;; Hood: Fur-trim | Plain ;; Lining: Detachable | Fixed",see=S(("Puffer coat","filled long coat"),("Anorak","pullover shell"))),
  K("Puffer coat","Fill: Down | Synthetic ;; Fill power: 550 | 650 | 800+ ;; Quilting: Baffle | Seamless ;; Length: Hip | Knee | Floor ;; Extras: Hooded | Belted",see=S(("Puffer jacket","shorter outdoor cut"))),
  K("Fur coat","Pelt: Mink | Fox | Sable | Rabbit | Shearling | Faux ;; Length: Stroller | Full ;; Source: New | Vintage or remodelled"),
  K("Cape","Form: Shoulder cape | Full cloak | Inverness | Blanket wrap ;; Hood: Hooded | None ;; Use: Everyday | Ceremonial"),
 ]),
 SH("Flight, field & military jackets","Jackets copied from military issue, by service: air force, army field wear and navy deck wear, with the souvenir jackets they inspired.",
  "kinds by origin: air force, army, navy, then souvenir jackets made for service members",[
  K("Flight jacket","Material: Horsehide | Goatskin | Cowhide | Shearling | Nylon flight satin | Nomex ;; Style: Fashion bomber (wool, satin, suede) | Reversible orange lining ;; Finish: Plain | Patched or painted"),
  K("Field jacket","Colour: Olive drab | Woodland camouflage | Desert camouflage ;; Lining: Button-in | None ;; Hood: Detachable | None ;; Cut: Safari | Greenland",see=S(("Chore coat","civilian workwear cousin"))),
  K("Deck jacket","Colour: Khaki | Navy blue | Olive drab ;; Shell: Cotton | Waxed or coated ;; Collar: Stand | Fur"),
  K("Souvenir jacket","Fabric: Silk | Rayon | Acetate | Nylon ;; Make: Reversible | Velvet panels | Quilted ;; Origin: Yokosuka (sukajan) | Vietnam-era commissions"),
 ]),
 SH("Leather, waxed & country jackets","Jackets in leather, waxed cotton, quilting or wool for riding, shooting and country wear.",
  "kinds by cloth: leather, waxed cotton, quilting, then wool",[
  K("Biker jacket","Cut: Double rider (asymmetric) | Café racer (straight zip) | Split collar ;; Hide: Horsehide | Steerhide | Cowhide | Goatskin ;; Extras: Belted | Padded",see=S(("Leather & suede jacket","non-riding leather"))),
  K("Waxed cotton jacket","Wax: Sylkoil (unshorn) | Thornproof (shorn) ;; Weight: Lightweight 4 oz | Medium 6 oz ;; Length: Three-quarter | Hip ;; Extras: Motorcycle belted | Hooded"),
  K("Quilted jacket","Quilting: Diamond | Onion (wave) | Box ;; Collar: Corduroy | Plain ;; Shell: Polyamide | Wool or tweed ;; Form: Jacket | Gilet"),
  K("Mackinaw","Cloth: Mackinaw wool ;; Pattern: Red-and-black plaid | Solid ;; Breast: Single | Double"),
  N("Norfolk jacket","Norfolk coat","Belted tweed jacket with box pleats on the back and front, made for shooting and country wear.",WP+"Jacket",
    "Cloth: Tweed | Wool ;; Pleats: Box | Knife ;; Belt: Cloth | Leather"),
 ]),
 SH("Casual & sportswear jackets","Short jackets worn every day, named for the cloth or trim that defines them.",
  "kinds by main cloth: leather and suede, denim, cotton blouson, nylon, wool and leather, jersey, then sleeveless",[
  K("Leather & suede jacket","Hide: Leather | Suede ;; Cut: Blouson | Cropped ;; Closure: Zip | Button",ren="Leather & suede jacket",d="Hip-length leather or suede jacket in a cut not made for riding: blousons and cropped styles.",a="blouson · leather jacket · suede jacket · casual jacket"),
  K("Trucker jacket","Cloth: Denim | Corduroy ;; Lining: Sherpa | Blanket | Unlined ;; Type: Selvedge reproduction | Standard",see=S(("Heritage American jeans","matching denim"))),
  K("Harrington jacket","Cloth: Cotton | Suede | Wool | Leather ;; Lining: Tartan | Plain"),
  K("Coach jacket","Shell: Nylon ;; Lining: Jersey | Quilted | None ;; Collar: Snap | Zip"),
  K("Varsity jacket","Body: Wool | Satin ;; Sleeves: Leather | Wool ;; Trim: Chenille letter | Embroidered",d="Wool-bodied jacket with leather sleeves and a school letter, also called a letterman jacket and first worn in US colleges in the 1860s."),
  K("Track jacket","Cloth: Tricot | Velour | Denim ;; Detail: Taped sleeves | Plain",see=S(("Joggers","matching bottoms"))),
  N("Bolero","bolero jacket · shrug","Short open jacket ending above the waist, worn over a dress or blouse.",WP+"Jacket",
    "Cloth: Satin | Knit | Lace | Velvet ;; Sleeve: Long | Short | Sleeveless ;; Origin: Spanish matador | Fashion"),
  K("Tracksuit","Set: Full tracksuit | Top only | Bottoms only ;; Cloth: Velour | Tricot | Shell ;; Tearaway: Popper pants | Plain ;; Style: Football club | Tennis | Shell suit",see=S(("Joggers","bottoms alone"))),
  K("Cut-off vest","Material: Denim | Leather ;; Form: Sleeveless | Sleeved battle jacket",d="Sleeveless denim or leather vest with sewn-on patches, also called a battle jacket or kutte.",a="battle vest · battle jacket · kutte · patch jacket"),
 ]),
 SH("Outdoor & technical jackets","Jackets made for weather on the hill, by the layer they form: shell, insulation or mid layer.",
  "kinds by layer: outer shell, insulation, mid layer",[
  K("Shell jacket","Layers: 2-layer | 2.5-layer | 3-layer hardshell ;; Membrane: Gore-Tex | H2No | DryVent | Pertex Shield ;; Type: Hardshell | Softshell | Windshell ;; Pack: Packable | Standard"),
  K("Anorak","Form: Pullover with kangaroo pocket | Half-zip | Smock ;; Cloth: Waxed or G-1000 cotton | Packable nylon | Insulated",see=S(("Parka","longer hooded coat"))),
  K("Puffer jacket","Fill: Down (fill power 600-900) | Synthetic (PrimaLoft, Thermoball) ;; Baffles: Box | Sewn-through ;; Shell: Ultralight packable | Lacquered | Crinkle ;; Hood: Hooded | Collar",see=S(("Puffer coat","longer city cut"))),
  K("Puffer vest","Fill: Down | Synthetic ;; Shell: Nylon | Lacquered nylon | Leather ;; Pack: Ultralight packable | Standard"),
  K("Fleece jacket & pullover","Weight: Microfleece 100 | 200-300 | High pile or sherpa ;; Zip: Full-zip | Half-zip | Snap-neck ;; Pile: Retro pile | Grid fleece | Windproof ;; Hood: Hooded | None",see=S(("Hoodie","cotton fleece cousin"))),
 ]),
],mode="variety",note="Archetype-led; the richest icon area in Clothing."),
]
# donkey jacket added to workwear later
