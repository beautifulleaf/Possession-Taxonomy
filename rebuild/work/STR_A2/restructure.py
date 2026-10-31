import json,copy,shutil,os,re,sys
R='/home/user/Possession-Taxonomy/rebuild/'
W=R+'work/STR_A2/'
src=R+'out/A2.json'
if not os.path.exists(W+'bak/A2.json'): shutil.copy(src,W+'bak/A2.json')
old=json.load(open(W+'bak/A2.json'))
K={}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
LSS='https://en.wikipedia.org/wiki/List_of_shoe_styles'
BOOT='https://en.wikipedia.org/wiki/Boot'; SAND='https://en.wikipedia.org/wiki/Sandal'; SLIP='https://en.wikipedia.org/wiki/Slipper'
def T(*g): return [[a,b] for a,b in g]
TT={
"Basketball sneaker":T(("Cut",["High","Mid","Low"]),("Upper",["Leather","Canvas","Synthetic"])),
"Air Jordan":T(("Cut",["High","Mid","Low"]),("Release",["Original-year release","Retro reissue"])),
"Court sneaker":T(("Cut",["Low","Mid"]),("Upper",["Leather","Canvas","Suede"])),
"Canvas sneaker":T(("Cut",["Low","High"]),("Fastening",["Lace-up","Slip-on"]),("Sole",["Vulcanised rubber","Cupsole"])),
"Heritage running sneaker":T(("Release",["OG reissue","Retro (updated)","Collaboration"]),("Made in",["USA or UK","Imported"])),
"Terrace sneaker":T(("Release",["OG reissue","Collaboration"]),("Sole",["Gum","Cream rubber"]),("Made in",["Germany or Italy","Imported"])),
"Chunky sneaker":T(("Midsole",["Stacked foam","Sculpted air unit"]),("Upper",["Mesh and suede","Leather"])),
"Skate shoe":T(("Sole",["Vulcanised","Cupsole"]),("Cut",["Low","Mid","High"]),("Upper",["Suede","Canvas","Leather"]),("Fastening",["Lace-up","Slip-on"])),
"Designer sneaker":T(("Cut",["Low","High"]),("Silhouette",["Minimalist leather","Chunky","Distressed"])),
"Running shoe":T(("Support",["Neutral","Stability","Motion control"]),("Cushioning",["Standard","Max-cushion"]),("Purpose",["Daily trainer","Tempo","Carbon-plate racer"])),
"Trail running shoe":T(("Protection",["Rock plate","Waterproof membrane"]),("Outsole",["Mud and soft-ground lugs","Hard-pack lugs"])),
"Minimalist shoe":T(("Toe box",["Five-toe","Wide toe box"]),("Drop",["Zero-drop","Low-drop"])),
"Walking shoe":T(("Upper",["Leather","Mesh"]),("Fastening",["Lace-up","Slip-on"])),
"Hiking shoe":T(("Upper",["Leather","Synthetic","Vented mesh"]),("Lining",["Waterproof membrane","Unlined"]),("Fit",["Standard","Wide"])),
"Hiking boot":T(("Cut",["Mid","High"]),("Weight",["Lightweight hiking","Backpacking","Mountaineering (crampon-compatible)"]),("Upper",["Leather","Synthetic or fabric"]),("Lining",["Waterproof membrane","Unlined"])),
"Water shoe":T(("Build",["Sock-style","Laced river shoe","Closed-toe sandal-style"])),
"Oxford":T(("Toe",["Plain","Cap toe","Wholecut"]),("Brogueing",["None","Quarter","Semi","Full"]),("Finish",["Calf","Patent (evening)","Suede"])),
"Derby":T(("Toe",["Plain","Cap toe","Norwegian split-toe","Moc-toe"]),("Brogueing",["None","Full (longwing)"]),("Weight",["Dress","Country (storm welt)"])),
"Monk strap":T(("Straps",["Single","Double"]),("Toe",["Cap","Plain","Wholecut"])),
"Saddle shoe":T(("Saddle colour",["Black","Brown","Navy"]),("Upper",["White leather","Suede"])),
"Boat shoe":T(("Eyelets",["1-eye","2-eye","3-eye"]),("Upper",["Leather","Canvas"])),
"Dr. Martens lace-up":T(("Height",["Shoe","Boot"]),("Upper",["Smooth leather","Suede"])),
"Brothel creeper":T(("Upper",["Suede","Leather"]),("Sole",["Crepe","Platform crepe"])),
"Loafer":T(("Lining",["Unlined","Lined"]),("Leather",["Calf","Suede","Shell cordovan"]),("Construction",["Goodyear-welted","Blake-stitched","Hand-sewn moccasin"])),
"Moccasin & driving shoe":T(("Sole",["Soft","Rubber-nub driving","Lug or crepe"]),("Lining",["Unlined","Pile-lined"]),("Upper",["Suede","Leather"]),("Trim",["Plain","Fringed","Beaded"])),
"Evening slipper":T(("Upper",["Velvet","Patent leather","Silk"]),("Trim",["Embroidered crest or motif","Grosgrain bow"])),
"Court shoe":T(("Heel",["Stiletto","Kitten","Block","Flat"]),("Toe",["Pointed","Almond","Round"]),("Sides",["Closed","D'Orsay (open sides)"]),("Toe cover",["Closed toe","Peep-toe"])),
"Ballet flat":T(("Toe",["Round","Pointed","Cap toe"]),("Trim",["Plain","Bow"])),
"Platform shoe":T(("Heel",["Flat platform","Block","Stiletto","Wedge"]),("Upper",["Leather","Patent","Suede"])),
"Slingback":T(("Heel",["Kitten","Block","Flat"]),("Colour",["Single colour","Two-tone"])),
"Mary Jane":T(("Strap",["Single bar","T-bar","Buckle","Button"]),("Heel",["Flat","Block","Platform"])),
"Mule":T(("Heel",["Flat","Heeled","Wedge"]),("Toe",["Pointed","Round"])),
"Clog":T(("Back",["Backless","Heel strap","Closed back"]),("Sole",["Wood","Moulded foam"]),("Heel",["Flat","High"])),
"Espadrille":T(("Sole",["Flat rope","Wedge rope"]),("Fastening",["Slip-on","Ankle-tie lace-up"])),
"Chelsea boot":T(("Upper",["Smooth leather","Suede"]),("Construction",["Goodyear-welted","Direct-moulded rubber sole"]),("Heel",["Low","Cuban","Platform"])),
"Chukka & desert boot":T(("Eyelet pairs",["Two","Three"]),("Upper",["Suede","Leather"]),("Sole",["Crepe","Rubber","Leather"]),("Lining",["Unlined","Lined"])),
"Bootie":T(("Closure",["Zip","Lace-up","Pull-on"]),("Heel",["Block","Stiletto","Wedge"]),("Toe",["Closed","Peep-toe"])),
"Go-go boot":T(("Heel",["Low block","Platform"]),("Material",["Patent","Vinyl","Leather"])),
"Knee-high boot":T(("Closure",["Pull-on","Zip","Lace-up"]),("Heel",["Flat","Block","Stiletto","Platform"]),("Upper",["Leather","Suede"]),("Calf fit",["Standard","Wide calf"])),
"Over-the-knee boot":T(("Height",["Over-the-knee","Thigh-high","Crotch-high"]),("Closure",["Pull-on","Zip","Tie-back"]),("Upper",["Leather","Suede","Stretch","Vinyl or latex"])),
"Jodhpur boot":T(("Upper",["Calf","Suede"]),("Sole",["Leather","Rubber"])),
"Cowboy boot":T(("Toe",["Round","Square","Pointed or snip"]),("Heel",["Cowboy (angled)","Walking","Roper"]),("Skin",["Cowhide","Exotic (ostrich, caiman, snake, stingray, bison)"]),("Decoration",["Plain","Hand-tooled"])),
"Equestrian riding boot":T(("Colour",["Black","Brown"]),("Upper",["Calf leather","Synthetic"]),("Closure",["Pull-on","Back zip"]),("Fit",["Off-the-peg","Custom-made"])),
"Work boot":T(("Height",["6-inch","8-inch"]),("Toe",["Soft","Steel","Composite"]),("Lining",["Waterproof membrane","Unlined"])),
"Moc-toe boot":T(("Height",["6-inch","8-inch"]),("Sole",["Wedge","Lug"])),
"Logger boot":T(("Sole",["Calked (spiked)","Lug"]),("Toe",["Soft","Steel"])),
"Engineer boot":T(("Upper",["Cowhide","Horsehide","Suede"]),("Toe",["Soft","Steel"])),
"Rigger boot":T(("Toe",["Soft","Steel"]),("Closure",["Pull-on","Elastic-sided"])),
"Service boot":T(("Toe",["Plain","Cap","Double cap"]),("Sole",["Leather","Rubber"])),
"Combat & military boot":T(("Upper",["Smooth black","Rough-out tan","Canvas (jungle)"]),("Closure",["Lace-up","Side-zip"])),
"Rain boot":T(("Height",["Tall","Short","Ankle"]),("Lining",["Unlined","Neoprene-lined","Fleece-lined"]),("Material",["Rubber","PVC"])),
"Duck boot":T(("Height",["Short","Tall"]),("Lining",["Unlined","Lined","Shearling-lined"])),
"Snow boot":T(("Insulation",["Removable liner (pac)","Fixed liner","Shearling"]),("Rating",["Temperature-rated","Unrated"])),
"Sheepskin boot":T(("Height",["Ultra mini","Mini","Short","Tall"]),("Sole",["Moulded","Platform"])),
"Flip-flop":T(("Material",["Rubber","EVA foam","Leather"]),("Sole",["Flat","Wedge"])),
"Slide":T(("Straps",["Single band","Two-strap","Cross-band"]),("Footbed",["Flat","Contoured","Recovery foam"])),
"Flat strap sandal":T(("Strap layout",["T-bar","Ankle strap","Back strap","Toe loop"])),
"Sports and outdoor sandal":T(("Toe",["Open","Closed (toe bumper)"]),("Straps",["Adjustable webbing"])),
"Gladiator sandal":T(("Height",["Ankle","Calf","Knee"]),("Heel",["Flat","Low heel"])),
"Huarache":T(("Sole",["Leather","Tyre rubber"]),("Weave",["Basket weave","Open weave"])),
"Heeled sandal":T(("Heel",["Block","Stiletto","Kitten","Platform"]),("Straps",["Ankle strap","Slingback","Toe loop"])),
"Wedge sandal":T(("Wedge material",["Cork","Espadrille rope","Platform foam"]),("Height",["Low","High"])),
"Geta":T(("Teeth",["Two","Three","One","None"]),("Shape",["Oval (women's)","Rectangular (men's)"])),
"Zōri":T(("Material",["Rice straw","Rush (igusa)","Bamboo sheath","Rubber","Brocade","Vinyl"]),("Thong colour",["White (formal)","Black (informal)"])),
"Waraji":T(("Material",["Rice straw","Hemp cord","Cotton cord"])),
"Jika-tabi":T(("Height",["Ankle","Calf","Knee-high"]),("Toe",["Soft","Steel toe"])),
"Jipsin":T(("Material",["Rice straw","Hemp"])),
"Tiger-head shoe":T(("Wearer",["Toddler","Child"]),("Material",["Cotton cloth","Embroidered silk"])),
"Kolhapuri chappal":T(("Weight",["House (light)","Farm (heavy)"]),("Straps",["Single","Double","T-strap"])),
"Peshawari chappal":T(("Sole",["Tyre rubber","Leather-on-rubber"]),("Decoration",["Plain","Embroidered (zari)"])),
"Jutti":T(("Wearer",["Men's (pointed nokh)","Women's (backless)"]),("Sole",["Leather","Rubber"]),("Decoration",["Plain","Embroidered"])),
"Paduka":T(("Shape",["Footprint","Fish","Hourglass"]),("Material",["Wood","Silver","Brass","Ivory"])),
"Babouche":T(("Toe",["Pointed","Round"]),("Decoration",["Plain","Embroidered"])),
"Giveh":T(("Upper",["Woven cotton thread"]),("Sole",["Pressed cloth","Leather"])),
"Wooden clog (klomp)":T(("Decoration",["Plain","Painted"]),("Wood",["Willow","Poplar"])),
"Opanak":T(("Toe",["Horn","Curly","Flat","Sharp"])),
"Valenki":T(("Sole",["Unsoled","Leather-soled","Rubber-soled"]),("Colour",["Brown","Black","Grey","White","Dyed"])),
"Bast shoe (lapti)":T(("Fibre",["Lime bast","Birch bark","Willow bast"])),
"Abarka":T(("Material",["Leather","Recycled tyre rubber"])),
"Mukluk":T(("Season",["Summer","Winter"]),("Skin",["Sealskin","Caribou"])),
"Bakya":T(("Strap",["Fabric","Rubber"]),("Finish",["Plain wood","Painted"])),
"Veldskoen":T(("Cut",["Ankle","Low"]),("Sole",["Rubber","Leather"])),
"Scuff slipper":T(("Material",["Terry cloth","Wool felt","Shearling","Leather"]),("Sole",["Foam","Rubber"])),
"Moccasin slipper":T(("Lining",["Shearling","Fleece","Unlined"]),("Upper",["Suede","Leather"]),("Sole",["Hard rubber","Soft"])),
"Clog slipper":T(("Back",["Closed","Backless"]),("Upper",["Terry","Felt","Suede"])),
"Slipper boot":T(("Height",["Bootie","Ankle","Mid-calf"]),("Lining",["Fleece","Shearling","Faux fur"])),
"Novelty slipper":T(("Form",["Animal","Character","Food"]),("Material",["Plush","Fleece"])),
"Shoe cleaner":T(("Target",["Sneaker","Suede and nubuck","Smooth leather"]),("Form",["Liquid","Foam","Wipes","Saddle soap"])),
"Shoe polish and conditioner":T(("Form",["Wax (tin)","Cream","Liquid","Conditioner","Dubbin","Waterproofing spray"]),("Finish",["Feed and colour","Mirror gloss"])),
"Shoe brush":T(("Bristle",["Horsehair","Boar","Goat hair","Synthetic"]),("Job",["Shine","Applicator (dauber)","Scrub","Crêpe suede"])),
"Shoe-shine kit":T(("Case",["Wooden valet box","Travel pouch","Starter tin"])),
"Shoe tree":T(("Material",["Cedar","Beech or lacquered wood","Plastic or metal"]),("Construction",["Lasted","Split-toe","Twin-tube","Spring"]),("Fits",["Shoe","Boot"])),
"Shoe horn":T(("Material",["Horn","Metal","Wood","Plastic"]),("Length",["Short","Long-handled","Travel"])),
"Shoelace":T(("Shape",["Flat","Round","Oval"]),("Material",["Waxed cotton","Cotton","Polyester","Leather"])),
"Insole & heel grip":T(("Part",["Insole","Heel grip"]),("Material",["Leather","Foam","Gel"])),
"Overshoe":T(("Closure",["Buckle","Slip-on"]),("Material",["Rubber","Fabric","Silicone"])),
"Spat":T(("Material",["Cloth","Leather"]),("Wearer",["Dress","Highland piper"])),
}
# ---- new kinds
NEW={
"Platform shoe":dict(a="platform pump · flatform",d="Shoe raised on a thick sole under the whole foot or the front, with or without a heel.",s=LSS),
"Go-go boot":dict(a="mod boot",d="Calf-high fashion boot with a low heel and rounded toe, worn in the 1960s.",s=LSS),
"Rigger boot":dict(a="",d="Ankle-high pull-on work boot, often steel-capped, worn on building and industrial sites.",s=LSS),
"Waraji":dict(a="straw sandal",d="Japanese straw sandal tied on with cords round the ankle; the ancestor of the zōri.",s=LSS),
"Jipsin":dict(a="Korean straw shoe",d="Korean sandal woven from rice straw or hemp and tied to the foot.",s=LSS),
"Tiger-head shoe":dict(a="hu tou xie",d="Chinese cloth shoe for small children, embroidered with a tiger face on the toe.",s=LSS),
"Giveh":dict(a="galesh · klash",d="Persian shoe with a woven cotton upper and a soft pressed sole, from Iran and Kurdistan.",s=LSS),
"Bast shoe (lapti)":dict(a="lapti · bast sandal",d="Slavic shoe plaited from lime bark or other bast, worn by peasants.",s=LSS),
"Abarka":dict(a="abarkas · avarcas · albarcas",d="Iberian leather or rubber sandal-shoe tied over the foot, worn by farmers and shepherds.",s=LSS),
"Bakya":dict(a="wooden sandal",d="Philippine wooden sandal with a fabric or rubber strap, carved from light wood.",s=LSS),
"Veldskoen":dict(a="vellie",d="South African ankle-high leather shoe with a simple sole, made for the bush and farm.",s=LSS),
"Scuff slipper":dict(a="backless slipper · open-heel slipper",d="Slipper covering the toes and top of the foot, heel left open.",s=SLIP),
"Moccasin slipper":dict(a="closed slipper",d="Closed slipper in a moccasin cut, often suede with a soft lining and a hard-wearing sole.",s=SLIP),
"Clog slipper":dict(a="",d="Closed slipper shaped like a clog, in terry, felt or suede.",s=SLIP),
"Slipper boot":dict(a="bootie slipper",d="Boot-shaped slipper, usually fleece-lined, with a soft rubber sole.",s=SLIP),
"Novelty slipper":dict(a="bunny slipper",d="Slipper shaped like an animal, character or object.",s=SLIP),
}
RENAME={"Fit aids":"Insole & heel grip"}
DEMOTE={
"Oxford":["Cap-toe Oxford","Plain-toe Oxford","Quarter brogue","Semi-brogue","Full brogue"],
"Derby":["Plain derby","Longwing blucher","Country brogue derby"],
"Monk strap":["Single monk","Double monk"],
"Moccasin & driving shoe":["Soft-sole moccasin"],
"Espadrille":["Traditional espadrille"],
"Cowboy boot":["Classic western boot","Western dress boot"],
"Gladiator sandal":["Grecian sandal","Roman sandal"],
"Huarache":["Mexican huarache"],
"Geta":["Two-tooth geta"],
"Zōri":["Wara-zōri","Setta","Igusa zōri","Formal brocade or vinyl zōri","Gomu zōri","Shigure zōri"],
"Jika-tabi":[],
"Peshawari chappal":["Peshawari kheri"],
"Jutti":["Punjabi jutti","Mojari","Khussa"],
"Paduka":["Wooden paduka","Ceremonial paduka"],
"Babouche":["Pointed (Arab) babouche","Round-toe (Amazigh) babouche","Embroidered babouch"],
"Wooden clog (klomp)":["Dutch klomp"],
"Valenki":["Unsoled valenki","Soled valenki"],
"Mukluk":["Summer sealskin kamik","Winter caribou kamik"],
"Opanak":["Tsarvuli","Tsarouhi"],
"Shoe tree":["Lasted shoe tree","Split-toe shoe tree","Twin-tube shoe tree","Spring shoe tree"],
}
ALIAS={"Zōri":"waraji-style straw zori","Jutti":"punjabi jutti","Peshawari chappal":"","Opanak":"","Gladiator sandal":"","Oxford":"cap-toe · wholecut · brogue"}
# slipper model distribution
SLIPM={"Scuff slipper":["Daybreak Scuffs","Scuffette II","Sydney Scuff"],"Moccasin slipper":["Classic Moccasin Slipper","Wicked Good Moccasins","Chesney"],
"Clog slipper":["Forest Clog Slipper","Terry Clog Slippers"],"Slipper boot":["Camden Recycled Bootie","Beth Faux Fur Fold Down Bootie"]}
SEE={
"Slide":[["F5","Slide","a photographic slide, not a shoe"],["A2","Flip-flop","other open footwear without a heel"]],
"Flip-flop":[["A2","Slide","band over the foot instead of a toe post"]],
"Insole & heel grip":[["H2","Orthotic insole","prescribed or medical insole"]],
"Shoe tree":[["B1","Shoe rack","stores shoes, does not shape them"]],
"Court sneaker":[["E2","Tennis shoe","court shoe made for play"],["E2","Pickleball shoe","court shoe made for play"]],
"Terrace sneaker":[["E2","Football boot","the outdoor boot of the same sport"]],
"Snow boot":[["E2","Ski boot","clips to a ski binding"],["E2","Snowboard boot","clips to a snowboard binding"]],
"Rain boot":[["E2","Waders","chest or hip boot for fishing"],["A2","Valenki","felt boot worn with galoshes"]],
"Ballet flat":[["E2","Ballet shoe","made for dancing"]],
"Hiking boot":[["E2","Climbing shoe","made for rock, not trails"]],
"Equestrian riding boot":[["A2","Jodhpur boot","short boot of the same riding style"]],
"Jodhpur boot":[["A2","Equestrian riding boot","tall riding boot"]],
"Espadrille":[["A2","Wedge sandal","rope-soled wedge as a sandal"]],
"Wedge sandal":[["A2","Espadrille","rope-soled shoe"]],
"Clog":[["A2","Wooden clog (klomp)","whole-foot wooden clog"],["A2","Clog slipper","indoor clog"]],
"Wooden clog (klomp)":[["A2","Clog","fashion and work clog"]],
"Evening slipper":[["A2","Scuff slipper","home slipper"]],
"Scuff slipper":[["A2","Evening slipper","formal slip-on"]],
"Valenki":[["A2","Snow boot","modern insulated winter boot"]],
"Zōri":[["A2","Waraji","straw sandal it came from"]],
"Waraji":[["A2","Zōri","slip-on descendant"]],
"Opanak":[["A2","Abarka","similar tied peasant shoe"]],
"Jika-tabi":[["E2","Climbing shoe","tabi-style sole used in climbing"]] if False else [],
"Mary Jane":[["A2","Ballet flat","flat shoe without a strap"]],
"Combat & military boot":[["G1","Motorcycle boot","riding boot with shin armour"]],
"Work boot":[["A2","Rigger boot","pull-on work boot"]],
"Rigger boot":[["A2","Work boot","lace-up work boot"]],
"Chelsea boot":[["A2","Rigger boot","pull-on work version"]],
"Loafer":[["A2","Mule","backless loafer"]],
"Mule":[["A2","Loafer","closed-back loafer"]],
"Shoe polish and conditioner":[],
}
def mk_shelf(n,t,ax,names): return dict(n=n,t=t,ax=ax,names=names)
DEPTS=[
dict(n="Sneakers",t="Rubber-soled lace-up or slip-on shoes descended from sport and street styles and worn every day; a shoe built for running or hiking → Running, walking & outdoor shoes, a sport-specific shoe → E2.",
 ax="Which sport or street scene set the look of the shoe: basketball, court and canvas, running and football terraces, or skate and fashion?",
 shelves=[
 ("Basketball sneakers","High-cut and signature shoes from basketball courts; a low court or tennis shoe → Court & canvas sneakers.","kinds by origin: the general basketball shoe, then the signature line",["Basketball sneaker","Air Jordan"]),
 ("Court & canvas sneakers","Low shoes from tennis courts and canvas plimsolls, such as the Stan Smith and Chuck-style canvas; a basketball shoe → Basketball sneakers.","kinds by upper: leather court shoes, then canvas plimsolls",["Court sneaker","Canvas sneaker"]),
 ("Running heritage & terrace sneakers","Old running and indoor-sport shoes worn as lifestyle shoes, such as the Air Max and Samba; a shoe made for current running → Running shoes.","kinds by origin: track and road running, then indoor football and casuals",["Heritage running sneaker","Terrace sneaker"]),
 ("Skate, street & designer sneakers","Shoes whose look came from skaters, sculpted midsoles or fashion houses, such as the Old Skool and the Triple S.","kinds by who set the look: skaters, midsole trends, fashion houses",["Skate shoe","Chunky sneaker","Designer sneaker"]),
 ]),
dict(n="Running, walking & outdoor shoes",t="Shoes and low boots built for movement on road, trail, rough ground or in water, judged on cushioning and grip; a lifestyle sneaker → Sneakers, a dress boot → Boots.",
 ax="What ground is the shoe built for: road and trail running, walking and hiking, or water?",
 shelves=[
 ("Running shoes","Cushioned shoes for running on road, trail or in minimalist form, such as the Pegasus, Speedgoat and FiveFingers; a retro runner worn as everyday style → Sneakers.","kinds by ground and sole: road, trail, near-barefoot",["Running shoe","Trail running shoe","Minimalist shoe"]),
 ("Walking & hiking shoes","Flexible shoes and boots for walking on pavements and rough ground, such as the Moab and Skechers GO WALK; a boot for dress or work → Boots.","kinds by terrain: pavement, rough ground, mountain",["Walking shoe","Hiking shoe","Hiking boot"]),
 ("Water shoes","Drainable shoes for streams, beaches and boats; an open sandal → Sandals & slides.","single kind",["Water shoe"]),
 ]),
dict(n="Dress & casual shoes",t="Leather and suede shoes below the ankle, laced, buckled or slipped on, for work, town and evening; a boot → Boots, a heel or flat made for women's dress → Heels, flats & mules.",
 ax="How is the shoe fastened: laces, a buckle strap, or slipped on?",
 shelves=[
 ("Lace-ups","Shoes closed with laces, such as the cap-toe Oxford, the Derby and the saddle shoe; a lace-up boot → Boots.","kinds by lacing and sole: closed lacing, open lacing, contrast panel, deck sole, thick sole",["Oxford","Derby","Saddle shoe","Boat shoe","Dr. Martens lace-up","Brothel creeper"]),
 ("Strap shoes","Shoes closed by a buckled strap across the instep, such as the monk strap; a strapped heel or flat → Mary Jane.","single kind",["Monk strap"]),
 ("Loafers & slip-ons","Shoes with no fastening, slipped on, such as the penny loafer, the driving moccasin and the velvet Albert slipper; a backless shoe → Mule.","kinds by sole and formality: stitched apron, soft sole, evening",["Loafer","Moccasin & driving shoe","Evening slipper"]),
 ]),
dict(n="Heels, flats & mules",t="Shoes with a raised heel, a ballet-flat cut or an open back, mostly sold for women; a lace-up or loafer → Dress & casual shoes, a heeled boot → Boots.",
 ax="How is the foot held: closed with no fastening, by a strap, or with an open back and a distinctive sole?",
 shelves=[
 ("Closed shoes","Closed shoes with no strap, such as the pump, the ballet flat and the platform shoe; a strapped shoe → Strapped shoes.","kinds by sole height: raised heel, flat, platform",["Court shoe","Ballet flat","Platform shoe"]),
 ("Strapped shoes","Shoes held by a strap round the heel or across the instep, such as the slingback and the Mary Jane; a buckled men's shoe → Monk strap.","kinds by strap position: round the heel, across the instep",["Slingback","Mary Jane"]),
 ("Mules, clogs & espadrilles","Backless and rope-soled shoes, such as the Princetown mule, the Swedish clog and the espadrille; a house shoe → Slippers.","kinds by back and sole: open back, rigid clog sole, rope sole",["Mule","Clog","Espadrille"]),
 ]),
dict(n="Boots",t="Footwear that covers the ankle or more, worn for dress, work, riding or weather; a hiking or climbing boot → Running, walking & outdoor shoes, a sport boot → E2.",
 ax="What is the boot for: dress and fashion, work and service, riding, or bad weather?",
 shelves=[
 ("Dress & fashion boots","Boots worn for style, from ankle to thigh, such as the Chelsea, the chukka and the over-the-knee boot; a work boot → Work, service & military boots.","kinds by shaft height: ankle, calf, knee, thigh",["Chelsea boot","Chukka & desert boot","Bootie","Go-go boot","Knee-high boot","Over-the-knee boot"]),
 ("Work, service & military boots","Boots made for labour and service, such as the Red Wing Iron Ranger, the logger and the army boot; a fashion boot → Dress & fashion boots.","kinds by trade: general labour, timber, factory, building site, office service, army",["Work boot","Moc-toe boot","Logger boot","Engineer boot","Rigger boot","Service boot","Combat & military boot"]),
 ("Western & riding boots","Boots made for horse riding, such as the cowboy boot, the jodhpur boot and the field boot; a rain boot → Weather boots.","kinds by riding style: western, short English, tall English",["Cowboy boot","Jodhpur boot","Equestrian riding boot"]),
 ("Weather boots","Boots made to keep out rain, snow and cold, such as the Hunter wellington, the Bean boot and the Ugg; a fashion boot → Dress & fashion boots.","kinds by weather: rain, rain with cold, snow, dry cold",["Rain boot","Duck boot","Snow boot","Sheepskin boot"]),
 ]),
dict(n="Sandals & slides",t="Open footwear that holds the foot with a toe post, a band or straps and leaves the toes bare; a closed shoe → another department, an indoor shoe → Slippers.",
 ax="How is the foot held and raised: by a toe post or band, by straps on a flat sole, or on a heel?",
 shelves=[
 ("Beach & pool sandals","Flat, light sandals worn at the beach, pool and home, such as the Havaianas flip-flop and the Adilette slide; a strapped sandal → Strapped flat sandals.","kinds by the part that holds the foot: toe post, band",["Flip-flop","Slide"]),
 ("Strapped flat sandals","Flat sandals held by straps, such as the Teva Original, the Roman sandal and the huarache; a heel → Heeled sandals.","kinds by strap layout: simple T and ankle straps, adjustable sports straps, multiple straps, woven leather",["Flat strap sandal","Sports and outdoor sandal","Gladiator sandal","Huarache"]),
 ("Heeled sandals","Sandals on a raised heel or wedge, such as the stiletto sandal and the cork wedge; a closed heel → Heels, flats & mules.","kinds by heel build: separate heel, continuous wedge",["Heeled sandal","Wedge sandal"]),
 ]),
dict(n="Traditional & regional footwear",t="Shoes still made to a regional craft pattern, such as the geta, the jutti and the klomp; a modern sandal, boot or clog from a brand → its own department.",
 ax="Which region's craft tradition does the shoe belong to?",
 shelves=[
 ("East Asian footwear","Japanese, Korean and Chinese regional shoes, such as the geta, the zōri and the jipsin; a modern flip-flop → Sandals & slides.","kinds by build: wooden base, straw or rush sole, cloth boot, child's shoe",["Geta","Zōri","Waraji","Jika-tabi","Jipsin","Tiger-head shoe"]),
 ("South Asian & Middle Eastern footwear","Leather and woven regional shoes of India, Pakistan, Iran and North Africa, such as the Kolhapuri, the jutti and the babouche.","kinds by region: India, Pakistan, Iran, Morocco",["Paduka","Kolhapuri chappal","Peshawari chappal","Jutti","Giveh","Babouche"]),
 ("European footwear","Peasant and folk shoes of Europe, such as the klomp, the opanak and valenki; a fashion clog → Clog.","kinds by material: wood, leather, felt, bast",["Wooden clog (klomp)","Opanak","Abarka","Bast shoe (lapti)","Valenki"]),
 ("Arctic, Philippine & African footwear","Regional shoes of the Arctic, South-East Asia and southern Africa, such as the mukluk, the bakya and the veldskoen.","kinds by climate: Arctic cold, tropical wood, bush leather",["Mukluk","Bakya","Veldskoen"]),
 ]),
dict(n="Slippers",t="Soft shoes worn indoors at home; a formal evening slip-on → Evening slipper, an outdoor sandal → Sandals & slides.",
 ax="How much of the foot does the slipper cover: open heel, closed heel, ankle, or a novelty shape?",
 shelves=[
 ("House slippers","Soft shoes worn indoors, such as the L.L.Bean moccasin, the Dearfoams scuff and the UGG Scuffette II.","kinds by cover: open heel, closed heel, ankle, novelty shape",["Scuff slipper","Moccasin slipper","Clog slipper","Slipper boot","Novelty slipper"]),
 ]),
dict(n="Shoe care & accessories",t="Products and fittings that clean, polish, shape, fasten or cover shoes; a shoe rack → B1, an orthotic insole → H2.",
 ax="What do you do to the shoe: clean and polish it, shape and put it on, or replace and cover parts?",
 shelves=[
 ("Cleaning & polishing","Products and tools for cleaning and finishing shoe leather, such as Saphir polish and the Jason Markk kit.","kinds by step: clean, feed and polish, brush, bring together as a kit",["Shoe cleaner","Shoe polish and conditioner","Shoe brush","Shoe-shine kit"]),
 ("Shaping & putting on","Tools that hold a shoe's shape or help the foot in, such as the cedar shoe tree and the shoe horn; a pair of laces → Laces, insoles & covers.","kinds by moment: when the shoe is off, when it goes on",["Shoe tree","Shoe horn"]),
 ("Laces, insoles & covers","Parts that fasten, pad or cover a shoe, such as waxed laces, insoles, galoshes and spats; a medical insole → H2.","kinds by part: fastening, fit, outer cover",["Shoelace","Insole & heel grip","Overshoe","Spat"]),
 ]),
]
KEY=[
"1. Is it made to a regional craft pattern, such as a geta, jutti, klomp or mukluk? → Traditional & regional footwear",
"2. Is it polish, a brush, a tree, laces, an insole or a cover for shoes? → Shoe care & accessories",
"3. Is it worn only indoors at home? → Slippers",
"4. Is it built for running, walking, hiking or water, with a cushioned or lugged sole? → Running, walking & outdoor shoes",
"5. Does it cover the ankle or more? → Boots",
"6. Is the foot held by a toe post, a band or straps, with the toes bare? → Sandals & slides",
"7. Is it a rubber-soled trainer from a sport or street style? → Sneakers",
"8. Does it have a raised heel, a ballet-flat cut or an open back? → Heels, flats & mules",
"9. Is it a leather or suede shoe laced, buckled or slipped on? → Dress & casual shoes",
"<i>Precedence: a hiking boot is outdoor footwear (step 4) before a boot (step 5); a Chelsea or work boot is a boot even in a dress style; a backless loafer is a mule; a shoe made for one sport (tennis, football, climbing, cycling) → E2.</i>"]
def build():
    pool={n:copy.deepcopy(k) for n,k in K.items()}
    # merge polish dup
    a=pool.pop("Shoe polish and waterproofing"); p=pool["Shoe polish and conditioner"]
    for key in('m','r'):
        for e in a.get(key,[]):
            if e not in p.setdefault(key,[]): p[key].append(e)
    # rename
    for o,n in RENAME.items():
        k=pool.pop(o); k['n']=n; pool[n]=k
    # slippers
    sl=pool.pop("Slippers")
    allm=sl.get('m',[])
    for kn,names in SLIPM.items():
        k=dict(NEW[kn]); k['n']=kn
        k['m']=[e for e in allm if e[0] in names]; pool[kn]=k
    used=set(sum([v for v in SLIPM.values()],[]))
    left=[e for e in allm if e[0] not in used]; assert not left,left
    for kn,v in NEW.items():
        if kn in pool: continue
        k=dict(v); k['n']=kn; pool[kn]=k
    # demote
    log=[]
    for kn,names in DEMOTE.items():
        k=pool[kn]; keep=[]
        for x in k.get('x',[]):
            if x['n'] in names:
                for v in x.get('v',[]):
                    if v.get('mk'):
                        e=[v['n'],v['mk']]
                        if e not in k.setdefault('m',[]): k['m'].append(e)
                log.append((kn,x['n']))
            else: keep.append(x)
        k['x']=keep
    for kn,al in ALIAS.items():
        if al:
            k=pool[kn]; k['a']=(k.get('a','')+' · '+al).strip(' ·')
    # tt, see
    for n,k in pool.items():
        assert n in TT,'no tt for '+n
        k['tt']=TT[n]; k.pop('t',None)
        if SEE.get(n): k['see']=SEE[n]
    assert set(TT)==set(pool),(set(TT)-set(pool),set(pool)-set(TT))
    out=copy.deepcopy(old)
    out['ax']="What kind of footwear is it: a sneaker, a shoe for running, walking or the outdoors, a dress or casual shoe, a heel, flat or mule, a boot, a sandal, a regional traditional shoe, a slipper, or shoe care?"
    out['key']=KEY
    od={d['n']:d for d in old['depts']}
    depts=[]; placed=set()
    for D in DEPTS:
        dd=dict(n=D['n'],mode=od[D['n']]['mode']) if D['n'] in od else None
        o=od[D['n']]
        nd={k:v for k,v in o.items() if k!='s'}
        nd['t']=D['t']; nd['ax']=D['ax']
        if D['n']=="Slippers": nd['note']="Indoor slippers by how much of the foot they cover; tier brands only."
        if D['n']=="Boots": nd['note']="Organised by what the boot is for; heritage boots by archetype (service, engineer, logger, moc-toe, jodhpur, 1460)."
        if D['n']=="Sneakers": nd['note']="Organised by lineage, then silhouette and cut (high, mid, low), then release (OG or retro) and colourway, the StockX and GOAT axis."
        if D['n']=="Traditional & regional footwear": nd['note']="Organised by region and craft tradition; each kind links to a tradition-register entry."
        sh=[]
        for (sn,st,sax,names) in D['shelves']:
            s={'n':sn,'t':st,'k':[]}
            if len(names)>3: s['ax']=sax
            for nm in names:
                assert nm in pool and nm not in placed,nm
                s['k'].append(pool[nm]); placed.add(nm)
            sh.append(s)
        nd['s']=sh; depts.append(nd)
    assert placed==set(pool),set(pool)-placed
    out['depts']=depts
    return out,log
if __name__=='__main__':
    out,log=build()
    tmp=W+'A2.new.json'; json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); 
    json.dump(log,open(W+'demoted.json','w'),ensure_ascii=False)
    shutil.copy(tmp,src+'.tmp'); os.replace(src+'.tmp',src)
    print('written',len(json.dumps(out)),'bytes; demoted',len(log))
