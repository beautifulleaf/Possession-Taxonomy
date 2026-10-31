from dsl import *
S=lambda *a:[["A1",x,y] for x,y in a]
DEPTS_A=[
DP("Tops","Garments that cover the upper body and are worn as a main layer, from tees to knitwear; a coat or jacket → Coats & jackets, an undershirt → Underwear, nightwear & swim.",
 "Is the top cut from knitted jersey, woven cloth, knitted yarn or brushed fleece, or is it a club or team shirt?",[
 SH("Jersey tops","Tops cut and sewn from knitted jersey, from the round-neck tee to collared polos and sleeveless or one-piece tops; a woven shirt → Shirts & blouses.",
  "kinds by neckline and sleeve: round neck, collared, striped boat neck, sleeveless, closed at the crotch",[
  K("T-shirt","Neckline: Crew neck | V-neck | Henley (buttoned placket) | Scoop ;; Sleeve: Short | Long | Three-quarter raglan (baseball tee) ;; Fit: Regular | Tall | Oversized | Cropped ;; Fabric weight: Lightweight | Heavyweight loopwheeled ;; Print: Plain | Pocket | Ringer | Graphic or band",see=S(("Tank top","sleeveless cousin"),("Undershirt","worn underneath"))),
  K("Polo shirt","Collar: Plain knitted | Button-down | Tipped | Zip neck ;; Fabric: Piqué | Jersey or interlock | Fine-gauge knit ;; Sleeve: Short | Long ;; Use: Casual | Golf or performance"),
  K("Breton shirt","Neck and sleeve: Long-sleeve boat neck | Short-sleeve ;; Fabric: Heavyweight carded cotton | Lightweight jersey ;; Stripes: Regulation 21-stripe | Wider fashion stripe ;; Cut: Men's | Women's | Children's"),
  K("Tank top","Cut: Athletic singlet (A-shirt) | Muscle tank | Racerback | Camisole | Cropped ;; Extras: Shelf-bra | Nursing or maternity ;; Fabric: Cotton | Ribbed | Technical"),
  K("Bodysuit","Sleeve: Long | Short | Sleeveless ;; Neckline: Crew | Turtleneck | Scoop ;; Back: Thong-back | Full-back ;; Closure: Snap crotch | Seamless pull-on ;; Function: Plain | Shaping",see=S(("Baby bodysuit","baby size"),("Shapewear","shaping bodysuits"))),
  K("Baby bodysuit","Sleeve: Short | Long | Sleeveless ;; Neck: Envelope (lap-shoulder) | Kimono wrap ;; Cuffs: Plain | Mitten ;; Pack: Single | Multipack",see=S(("Bodysuit","adult size"))),
 ]),
 SH("Team & sports shirts","Shirts in a team's colours, worn by players and fans and collected by club and season; cycling and running tops → Sports.",
  "kinds by sport: football, rugby, American football, basketball, ice hockey, baseball, cricket, then other sports",[
  K("Football shirt","Version: Home | Away | Third | Goalkeeper ;; Grade: Authentic (player issue) | Replica ;; Era: Current | Retro or throwback ;; Sleeve: Short | Long ;; Print: Plain | Name and number"),
  K("Rugby shirt","Style: Hooped stripe | Solid with contrast collar ;; Sleeve: Long | Short ;; Fabric: Heavyweight cotton | Modern technical jersey ;; Fit: Casual | Tight playing fit"),
  N("American football jersey","gridiron jersey · NFL jersey","Numbered pullover jersey with shoulder-width sleeves worn over pads by American football players and bought by fans.",WP+"Jersey_(clothing)",
    "Grade: Elite (game) | Limited | Game replica ;; Era: Current | Throwback ;; Print: Name and number | Plain"),
  K("Basketball jersey","Cut: Sleeveless | Sleeved ;; Grade: Authentic | Replica ;; Era: Current | Throwback ;; Edition: Association | Icon | Statement | City"),
  K("Ice-hockey jersey","Grade: Authentic | Fan replica ;; Version: Home | Away | Alternate ;; Era: Current | Throwback"),
  K("Baseball jersey","Version: Home | Road | Alternate ;; Fastening: Button-front | Pullover ;; Pattern: Plain | Pinstripe ;; Era: Current | Throwback"),
  N("Cricket shirt","cricket whites · one-day shirt","Collared shirt in white for Test cricket or in team colours for limited-overs matches, worn by players and fans.",WP+"Cricket_clothing",
    "Format: Test whites | Limited-overs colours ;; Sleeve: Long | Short ;; Print: Plain | Name and number"),
  K("Team jersey","Version: Home | Away | Third ;; Grade: Authentic (player issue) | Replica ;; Era: Current | Retro or throwback ;; Sleeve: Short | Long ;; Print: Plain | Name and number",d="Pullover top in a team's colours for a sport without its own kind here; cycling jerseys are in Sports."),
 ]),
 SH("Shirts & blouses","Woven shirts with a collar and front opening, from dress shirts to regional styles, and women's blouses; a knitted tee or polo → Jersey tops.",
  "kinds by use: dress, casual, worn as a jacket, regional, then women's blouse",[
  K("Dress shirt","Collar: Spread | Cutaway | Point | Button-down | Club | Pin or tab | Wing ;; Cuff: Barrel | French (double) | Cocktail ;; Cloth: Poplin | Twill | Oxford | End-on-end ;; Making: Ready-to-wear | Made to measure | Bespoke ;; Care: Non-iron | Standard"),
  K("Button-up shirt","Cloth: Oxford | Flannel | Chambray | Denim | Linen | Poplin | Corduroy ;; Collar: Button-down | Camp or revere | Point ;; Placket: Full | Popover (half) ;; Sleeve: Long | Short"),
  K("Overshirt","Cloth: Wool flannel | Corduroy | Canvas | Waxed cotton | Ripstop ;; Lining: Unlined | Quilted | Brushed fleece ;; Closure: Buttoned | Zip-through",see=S(("Chore coat","heavier workwear jacket"))),
  K("Western shirt","Fastening: Pearl snaps | Buttons ;; Detail: Pointed yoke | Sawtooth pocket flaps | Smile pockets | Piping | Embroidery | Shield front ;; Cloth: Denim | Chambray | Plaid | Satin"),
  K("Aloha shirt","Cloth: Rayon | Cotton | Silk ;; Print: Border print | Reverse print | All-over ;; Cut: Open collar | Pullover ;; Origin: Hawaiian | Kariyushi (Okinawa)"),
  K("Blouse","Neckline: Pussy-bow (lavallière) | Peter Pan collar | Sailor collar | Wrap ;; Cut: Peasant | Smock | Tunic ;; Trim: Ruffled or jabot | Lace ;; Cloth: Denim | Rayon | Silk | Chiffon"),
 ]),
 SH("Knitwear","Tops knitted from yarn: plain jumpers and cardigans, then named regional knits; a hooded or brushed sweatshirt → Hoodies & sweatshirts.",
  "kinds by garment shape, then by named regional knitting tradition",[
  K("Sweater","Neckline: Crew | V-neck | Polo or roll neck | Mock neck | Shawl collar ;; Knit: Cable | Fine-gauge | Chunky | Brushed Shetland ;; Yarn: Wool | Merino | Cashmere | Cotton | Lambswool ;; Style: Cricket (tennis) | Quarter-zip | Christmas"),
  K("Cardigan","Front: Button | Zip-through | Open or duster ;; Neckline: V-neck | Shawl collar ;; Length: Cropped | Hip | Long ;; Gauge: Fine | Chunky"),
  K("Sweater vest","Style: V-neck slipover | Buttoned waistcoat ;; Knit: Plain | Cable | Fair Isle pattern ;; Use: Casual | Golf or performance | Cricket"),
  K("Aran jumper","Neckline: Crew | Shawl collar | Polo neck ;; Form: Pullover | Cardigan ;; Stitch: Cable | Honeycomb | Diamond | Trellis | Moss ;; Making: Hand-knit | Machine-knit ;; Wool: Undyed báinín | Coloured",d="Cream cabled wool jumper from the Aran Islands, off the west coast of Ireland, knitted in rope-like stitches."),
  K("Guernsey (gansey)","Form: Traditional navy with gusset and split welt | Striped | Zip or cardigan ;; Neckline: Crew ;; Regional pattern: Guernsey | Filey | Flamborough | Staithes | Polperro",d="Tight-knit worsted fisherman's jumper from the Channel Islands and the English coast, with a gusseted underarm and a split hem."),
  K("Fair Isle jumper","Pattern: All-over | Yoke ;; Motif: OXO | Star ;; Form: Jumper | Slipover ;; Making: Hand-knit | Machine-knit",d="Jumper knitted in bands of coloured geometric motifs, named for Fair Isle in Shetland and popular since the 1920s."),
  K("Lopapeysa","Form: Pullover | Zip cardigan ;; Colour: Natural undyed | Dyed ;; Making: Hand-knit | Machine-knit",d="Icelandic yoke jumper knitted in unspun lopi wool, with a round colourwork pattern at the neck and shoulders."),
  K("Norwegian sweater","Form: Pullover | Cardigan with pewter clasps ;; Motif: Selburose star | Lice (lus) pattern | Snowflake ;; Use: Everyday | Ski or Olympic",d="Colourwork wool jumper or cardigan from Norway, including the Setesdal lusekofte and the Marius ski sweater."),
  K("Cowichan sweater","Form: Cardigan (zip or button) | Pullover ;; Motif: Eagle | Deer | Thunderbird | Snowflake | Geometric ;; Wool: Natural white | Grey | Brown",d="Heavy hand-knitted wool sweater made by Coast Salish knitters of the Cowichan Valley, Vancouver Island, with bold pictorial bands.",
    ),
 ]),
 SH("Hoodies & sweatshirts","Loopback cotton or fleece pullovers, with or without a hood; a knitted yarn jumper → Knitwear, a zip fleece jacket → Coats & jackets.",
  "kinds by whether the top has a hood",[
  K("Hoodie","Front: Pullover (kangaroo pocket) | Full-zip | Half-zip ;; Fit: Regular | Cropped | Oversized ;; Weight: Light (250-300 gsm) | Mid (300-400 gsm) | Heavy (400 gsm+) ;; Fabric: French terry | Brushed fleece | Loopwheel knit | Tech fleece",see=S(("Fleece jacket & pullover","brushed technical cousin"))),
  K("Sweatshirt","Sleeve: Set-in | Raglan | Freedom ;; Neck: Crewneck | Quarter-zip | V-insert gusset ;; Fit: Regular | Cropped ;; Fabric: French terry | Brushed fleece | Loopwheel knit | Heavy 12-14 oz"),
 ]),
],mode="mixed",note="Tier for basics, variety for named icons (polos, knitwear, sweats)."),

DP("Trousers, jeans & shorts","Garments that cover the legs separately, from jeans to tailored trousers, shorts and stretch legwear; a skirt → Skirts, jumpsuits & sets, riding or sports breeches → Sports.",
 "Is the leg cloth denim, woven trouser cloth, a short cut, or knitted and stretch fabric?",[
 SH("Jeans","Five-pocket denim trousers, sorted by who made the pattern: the original American makers, faithful reproductions, then modern fashion cuts.",
  "kinds by provenance: original American patterns, faithful reproductions, modern fashion cuts",[
  "JEANS_A","JEANS_B","JEANS_C"]),
 SH("Trousers","Trousers in woven cloth, from tailored to casual, work and wide cuts; denim → Jeans, knitted legwear → Knitted & stretch legwear.",
  "kinds by cloth and use: tailored, chino, utility, wide-cut, then period and subculture styles",[
  K("Trousers","Front: Flat | Pleated ;; Leg: Straight | Tapered | Wide | Cropped ;; Rise: Low | Mid | High ;; Use: Tailored | Casual",see=S(("Chinos","casual cotton twill"))),
  K("Chinos","Front: Flat | Pleated ;; Leg: Slim | Straight | Cropped ;; Fabric: Cotton twill | Stretch twill"),
  K("Cargo trousers","Cut: Baggy streetwear | Slim | Double-front ;; Cloth: Ripstop | Cotton twill ;; Use: Military surplus | Workwear | Walking or travel | Tactical"),
  N("Harem pants","harem trousers · hammer pants","Baggy trousers gathered at the ankle with a low, loose crotch, worn from Ottoman dress to 1980s fashion.",WP+"Trousers",
    "Fabric: Cotton | Silk or satin | Jersey ;; Hem: Gathered at ankle | Loose ;; Crotch: Low drop | Standard"),
  N("Capri pants","capris · pedal pushers · crop trousers","Slim trousers ending mid-calf, named for the island of Capri and popular in the 1950s.",WP+"Trousers",
    "Length: Mid-calf | Pedal pusher below the knee ;; Fit: Slim | Straight ;; Fabric: Cotton | Stretch"),
  K("Plus fours & breeks","Length: Plus fours (four inches below the knee) | Plus twos, sixes and eights ;; Style: Knickerbockers | Shooting breeks"),
  K("Bondage trousers","Pattern: Tartan | Black cotton ;; Fit: Slim | Baggy"),
 ]),
 SH("Shorts","Legwear cut above the knee, by length and cloth; swim shorts → Swimwear, cycling shorts → Sports.",
  "kinds by length and cut, from knee-length to the shortest",[
  K("Shorts","Cloth: Chino | Cargo | Work | Technical or running ;; Length: Above knee | Knee ;; Fastening: Zip-off legs | Plain",see=S(("Swim trunks","for the water"))),
  N("Bermuda shorts","Bermudas","Tailored shorts ending just above the knee, named for the island of Bermuda.",WP+"Trousers",
    "Cloth: Wool | Cotton twill | Madras plaid | Linen ;; Length: Just above knee ;; Front: Flat | Pleated",take={"Shorts":["Bermuda shorts"]}),
  N("Denim shorts & cut-offs","cut-offs · jorts · denim shorts","Jeans shortened to above the knee, either cut and frayed by hand or sold hemmed.",WP+"Trousers",
    "Hem: Frayed cut-off | Turned-up | Hemmed ;; Rise: Low | High ;; Length: Mid-thigh | Knee (jorts)",take={"Shorts":["Jorts"]}),
  N("Hot pants","hotpants · short shorts","Very short, tight shorts that came into fashion around 1970.",WP+"Trousers",
    "Cloth: Satin | Denim | Velvet | Stretch ;; Rise: High | Low",take={"Shorts":["Hotpants"]}),
 ]),
 SH("Knitted & stretch legwear","Trousers in jersey, fleece or stretch cloth that fit close or loose for comfort; tights worn as hosiery → Underwear, nightwear & swim.",
  "kinds by fit: loose at the ankle or close to the leg",[
  K("Joggers","Hem: Cuffed | Open | Tearaway ;; Fabric: Jersey | Fleece | Tech fleece ;; Leg: Slim | Wide",d=None),
  K("Leggings","Fabric: Matt cotton | Technical stretch | Shiny disco | Thermal ;; Rise: Mid | High ;; Leg: Full-length | Flared | Cropped ;; Use: Yoga or athletic | Fashion | Compression"),
 ]),
],mode="mixed",note="Jeans are a full hobbyist kind; the rest tier."),

DP("Dresses","One-piece garments for the body and legs hanging from the shoulders or waist; a skirt or two-piece set → Skirts, jumpsuits & sets, a robe or kaftan from a tradition → Traditional dress.",
 "What silhouette does the dress make: close to the body, straight and loose, or flared and long?",[
 SH("Close-fitting dresses","Dresses that follow the body line, by how they are held in place.",
  "kinds by how the dress closes on the body: wrapped, slipped on, or cut tight",[
  K("Wrap dress","Front: True wrap | Faux wrap ;; Fabric: Knit jersey | Woven ;; Length: Mini | Midi | Maxi ;; Collar: Plain | Shirt collar",d="Dress whose front panels cross and tie at the waist, made famous by Diane von Furstenberg in 1974."),
  K("Slip dress","Cut: Bias-cut satin | Lace-trimmed ;; Neckline: Straight | Cowl ;; Length: Midi | Maxi ;; Layering: Single | Layered chiffon"),
  K("Sheath & bodycon dress","Cut: Darted sheath | Pencil or wiggle | Bandage | Stretch bodycon ;; Fabric: Wool crepe | Stretch jersey | Latex ;; Detail: Cut-out | Plain"),
 ]),
 SH("Straight & loose dresses","Dresses that hang from the shoulders or yoke without defining the waist.",
  "kinds by how loose the dress hangs, from straight shift to gathered smock",[
  K("Shift & A-line dress","Cut: Shift (straight) | A-line | Trapeze or tent | Drop-waist flapper ;; Length: Mini | Knee ;; Style: Plain | Colour-block"),
  K("Shirt dress","Cut: Shirtwaist (full skirt) | Straight | T-shirt dress | Trench ;; Fit: Belted midi | Oversized"),
  K("Babydoll & smock dress","Cut: Babydoll (empire) | Smocked yoke | Tiered ;; Trim: Peter Pan collar | Puff sleeve ;; Fabric: Cotton | Tulle"),
  K("Pinafore dress","Cut: Dungaree or overall dress | Gymslip (pleated school) | Bib front ;; Closure: Button-through | Pull-on ;; Style: School | Fashion | Lolita jumperskirt"),
 ]),
 SH("Flared & full-length dresses","Dresses that widen from the waist or fall to the ankle.",
  "kinds by skirt volume and length, from swing skirts to gowns",[
  K("Fit-and-flare & swing dress","Skirt: Swing or circle | Skater (short) | Pleated ;; Neckline: Halter | Shirt collar ;; Underskirt: Petticoat | None"),
  K("Sundress & tea dress","Strap: Halter | Strappy ;; Bodice: Shirred | Fitted ;; Sleeve: Puff | Short ;; Cloth: Linen | Cotton | Rayon ;; Era: 1940s tea dress | Modern"),
  K("Maxi dress","Cut: Prairie (ruffled high neck) | Gipsy or bohemian | Kaftan dress | Tiered | Knit column ;; Neckline: Halter | High",see=S(("Kaftan","Middle Eastern origin"))),
  K("Evening gown & cocktail dress","Silhouette: Ball gown | Mermaid | Trumpet | Column | A-line | Fit and flare ;; Length: Cocktail (knee) | Floor ;; Neckline: Halter | Strapless | Sleeved"),
  N("Wedding dress","bridal gown · wedding gown","Dress worn by a bride, usually white or ivory, from ball gown to column cut.",WP+"Dress",
    "Silhouette: Ball gown | A-line | Mermaid | Column | Fit and flare ;; Neckline: Strapless | Sweetheart | Sleeved ;; Train: Chapel | Sweep | None ;; Making: Off the peg | Made to measure | Bespoke",take={"Evening gown & cocktail dress":["Bridal gown"]}),
 ]),
],mode="variety",note="Dresses organised by silhouette, each with its originating icon."),

DP("Skirts, jumpsuits & sets","Garments for the lower body or whole body that are not dresses or trousers: skirts, one-piece suits with legs, matching sets and costumes.",
 "Does it cover the lower body only (skirt), the whole body in one piece with legs, or come as a set or costume?",[
 SH("Skirts","Garments hanging from the waist, by silhouette; a kilt → Traditional dress, a tutu worn for dance → Sports.",
  "kinds by silhouette: close, straight, flared, pleated, wrapped, tiered, then very short and split",[
  "SK_PENCIL","SK_ALINE","SK_CIRCLE","SK_PLEAT","SK_WRAP","SK_TIER","SK_MINI","SK_TUTU","SK_CULOTTE"]),
 SH("Jumpsuits & playsuits","One-piece garments covering torso and legs, worn as everyday or fashion clothes; workwear coveralls → Workwear & uniform clothing.",
  "kinds by leg length and fit",[
  K("Jumpsuit","Leg: Full-length | Wide | Shorts (playsuit or romper) ;; Cut: Utility or boiler-style | Tailored | Catsuit ;; Top: Strapless | Halter | Sleeved ;; Cloth: Denim | Crepe | Jersey",see=S(("Boiler suit","workwear original")))),
 ]),
 SH("Sets & costumes","Garments sold together as a matching set, or dressed in as a character.",
  "kinds by purpose: a matching outfit for wear, or a costume for play",[
  K("Co-ord set","Pieces: Top and skirt | Top and trousers | Top and shorts ;; Cloth: Knit | Woven | Loungewear jersey"),
  K("Costume","Theme: Licensed character | Historical | Animal | Cosplay ;; Form: Inflatable | Full-body suit ;; Wearer: Adult | Child | Group"),
 ]),
],mode="variety",note="Skirts by silhouette; jumpsuits and sets kind-level."),
]

SKIRT_KINDS={
"SK_PENCIL":N("Pencil skirt","wiggle skirt","Close-fitting skirt that tapers to the knee, popularised by Dior in 1954.",WP+"Skirt","Length: Knee | Midi ;; Slit: Back | Side | None ;; Waist: High | Standard ;; Cloth: Wool | Stretch cotton | Leather",take={"Skirt":["Pencil skirt","Hobble skirt"]}),
"SK_ALINE":N("A-line skirt","","Skirt that widens evenly from the waist to the hem without gathers.",WP+"Skirt","Length: Mini | Knee | Midi | Maxi ;; Cloth: Denim | Wool | Cotton | Leather ;; Front: Plain | Buttoned"),
"SK_CIRCLE":N("Circle & poodle skirt","skater skirt · swing skirt","Full skirt cut as a circle, with a smooth flare at the hem, including the 1950s poodle skirt.",WP+"Skirt","Cut: Full circle | Half circle | Skater (short) ;; Era: 1950s poodle skirt | Modern ;; Cloth: Felt | Cotton | Jersey",take={"Skirt":["Poodle skirt"]}),
"SK_PLEAT":N("Pleated skirt","kilt-skirt · tennis skirt","Skirt folded into pleats that open as the wearer moves.",WP+"Skirt","Pleat: Knife | Box | Inverted | Accordion ;; Length: Mini | Midi | Maxi ;; Cloth: Wool | Chiffon | Tartan ;; Use: Fashion | School | Tennis"),
"SK_WRAP":N("Wrap skirt","wraparound skirt · sarong skirt","Skirt cut from a panel that wraps round the waist and ties or buttons.",WP+"Skirt","Closure: Tie | Button | Snap ;; Length: Mini | Midi | Maxi ;; Cloth: Cotton | Silk | Linen"),
"SK_TIER":N("Tiered & prairie skirt","gypsy skirt · broomstick skirt","Skirt built from gathered horizontal layers, as in the prairie and gypsy styles.",WP+"Skirt","Tiers: Two | Three or more ;; Hem: Midi | Maxi ;; Cloth: Cotton | Crinkle voile | Denim",take={"Skirt":["Prairie skirt"]}),
"SK_MINI":N("Miniskirt","mini skirt · micro skirt","Skirt ending well above the knee, popularised by Mary Quant in the 1960s.",WP+"Skirt","Length: Mini | Micro ;; Cut: A-line | Pleated | Straight ;; Cloth: Denim | Leather | Wool ;; Style: Rah-rah | Mini-crini",take={"Skirt":["Miniskirt","Rah-rah skirt","Mini-Crini"]}),
"SK_TUTU":N("Tutu & ballerina skirt","tutu · net skirt","Skirt of layered net or tulle, standing out stiffly or falling soft, worn on stage and for fashion.",WP+"Skirt","Shape: Classical (flat) | Romantic (bell) | Fashion tulle ;; Length: Short | Midi | Maxi"),
"SK_CULOTTE":N("Culottes & skort","split skirt · divided skirt","Wide shorts cut to look like a skirt, or a skirt with built-in shorts.",WP+"Skirt","Form: Culottes (wide leg) | Skort (shorts under a skirt) ;; Length: Knee | Midi ;; Use: Fashion | Tennis or golf"),
}
