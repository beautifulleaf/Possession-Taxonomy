import json, os
W='https://en.wikipedia.org/wiki/'
FR='https://fr.wikipedia.org/wiki/Secrétaire_(meuble)'
kinds=[
{"n":"Desk","a":"writing desk · writing table · computer desk · study desk","d":"A table made to work, write or study at, usually with drawers.",
 "t":["pedestal desk","kneehole desk","single-pedestal (student) desk","partners desk","roll-top desk","writing table","computer desk","L-shaped desk","typewriter desk","armoire desk","loft-bed desk"],
 "s":"https://www.google.com/basepages/producttype/taxonomy.en-US.txt",
 "x":[
  {"n":"Pedestal desk","a":"panel desk · tanker desk (steel)","d":"A rectangular top resting on two drawer pedestals, usually with a central drawer over the knees.","mk":"","y":"18th century, England","s":W+"Pedestal_desk",
   "v":[{"n":"Kneehole desk","mk":"","y":"","d":"older, smaller type with a panel, set against a wall; also called bureau table"},
        {"n":"Single-pedestal desk","mk":"","y":"","d":"about two-thirds width, one pedestal replaced by legs; common as a student desk"},
        {"n":"Steel tanker desk","mk":"","y":"1946","d":"steel version, popular in America until the 1970s"}],
   "dt":"leather or baize writing surface · pull-out writing slide · modesty panel · wood or steel"},
  {"n":"Partners desk","a":"double desk","d":"A large pedestal desk for two people facing each other, with drawers on both sides.","mk":"","y":"18th century (from library writing tables)","s":W+"Partners_desk","dt":"deep writing top · drawers both sides · leather inset"},
  {"n":"Rolltop desk","a":"roll-top desk · tambour desk","d":"A pedestal desk with tiers of pigeonholes and drawers closed by a sliding tambour of linked slats.","mk":"","y":"19th century","s":W+"Rolltop_desk",
   "v":[{"n":"Bureau du Roi (cylinder desk)","mk":"","y":"c. 1760","d":"Jean-François Oeben's cylinder desk for Louis XV, completed by Jean Henri Riesener; the rolltop's ancestor"},
        {"n":"Cutler patent rolltop","mk":"","y":"1882","d":"first American-made rolltop patent, Abner Cutler (A. Cutler & Son), Buffalo NY"}],
   "dt":"tambour slats on cloth or leather · pigeonhole tiers · oak, walnut · lock"},
  {"n":"Wooton desk","a":"Wooton patent desk","d":"A lockable cabinet desk on casters whose two hinged wings are filled with pigeonholes and drawers.","mk":"","y":"1874–1890","s":W+"Wooton_desk",
   "v":[{"n":"Wooton patent desk","mk":"","y":"1874","d":"patented by William S. Wooton of Indianapolis; made 1874–1890"}],
   "dt":"hinged wings · fold-up writing flap · casters · single lock"},
  {"n":"Carlton House desk","a":"","d":"A writing table with small drawers and slopes curving in a U around the user's back edge.","mk":"","y":"18th century","s":W+"Carlton_House_desk",
   "v":[{"n":"Hepplewhite design","mk":"","y":"18th century","d":"attributed to George Hepplewhite for the Prince of Wales; popularised by Sheraton's design book"}],
   "dt":"U-shaped drawer gallery · end slopes · mahogany"},
  {"n":"Bonheur du jour","a":"lady's writing desk","d":"A light lady's writing desk with a raised back cabinet or shelves and a drawer under the writing surface.","mk":"","y":"c. 1760, Paris","s":W+"Bonheur_du_jour",
   "v":[{"n":"Sèvres-plaque bonheur du jour","mk":"","y":"1766–67","d":"Sèvres porcelain plaques supplied through marchand-mercier Simon-Philippe Poirier; makers incl. Martin Carlin"},
        {"n":"Neoclassical bonheur du jour","mk":"","y":"after c. 1775","d":"straight tapering legs replace slender cabriole legs"},
        {"n":"Lady's writing-desk (English)","mk":"","y":"mid-1770s","d":"London-made version"}],
   "dt":"cabriole or tapered legs · marquetry, lacquer, gilt-bronze mounts · porcelain plaques"},
  {"n":"Bureau Mazarin","a":"","d":"A 17th-century French kneehole desk on eight braced legs with tiers of small drawers; ancestor of the pedestal desk.","mk":"","y":"17th century, France","s":W+"Bureau_Mazarin","dt":"eight legs · X or H stretchers · two or three drawer tiers"}
 ],
 "m":[["ALEX","IKEA"],["MICKE","IKEA"]][:1]+[["TONSTAD","IKEA"],["ROSENTORP","IKEA"]]},
{"n":"Writing bureau","a":"bureau · slant-top desk · slant-front desk · bureau à pente","d":"A chest of drawers topped by a sloping hinged lid that opens onto lopers to form a writing surface.",
 "t":["slant-front","bureau bookcase","lopers or pull-out supports","fitted interior (pigeonholes, small drawers)"],
 "s":W+"Slant-top_desk",
 "x":[
  {"n":"English slant-front bureau","a":"bureau · slope-front bureau","d":"A chest of drawers with a sloping fall flap resting on lopers, opening to pigeonholes and small drawers.","mk":"","y":"18th century","s":W+"Slant-top_desk","dt":"oak, walnut, mahogany · loper supports · fitted interior · bracket feet"},
  {"n":"Bureau bookcase","a":"bureau-cabinet · secretary and bookcase · desk and bookcase","d":"A slant-front bureau with a bookcase or cabinet above, often glazed, forming one tall unit.","mk":"","y":"18th century","s":W+"Secretary_desk",
   "v":[{"n":"Escritoire (glazed)","mk":"","y":"","d":"name used when the bookcase has glazed panels"},{"n":"Side-by-side secretary","mk":"","y":"","d":"half-width desk beside a glazed cabinet"}],
   "dt":"glazed or panelled doors · broken pediment · drawer base"},
  {"n":"Block-front bureau","a":"Chippendale block-front desk","d":"A Colonial American slant-front desk with a blocked drawer front, often with carved shells.","mk":"","y":"18th century","s":W+"Slant-top_desk","dt":"mahogany · block front · shell carving"},
  {"n":"Governor Winthrop desk","a":"","d":"An American colonial-revival slant-front desk; the name was a 1924 trade name with no link to John Winthrop.","mk":"","y":"1924","s":W+"Slant-top_desk",
   "v":[{"n":"Winthrop Furniture Co. naming","mk":"","y":"1924","d":"Boston firm applied the name"}],"dt":"mahogany or veneer · serpentine or straight front · brass hardware"},
  {"n":"Bureau brisé","a":"","d":"A French desk inspired by the bureau Mazarin, whose top lifts to reveal a writing space.","mk":"","y":"17th century","s":W+"Slant-top_desk","dt":"hinged folding top · marquetry"}
 ]},
{"n":"Secretaire","a":"secretary · secrétaire à abattant · fall-front desk · drop-front desk · escritoire","d":"An upright cabinet whose vertical front falls forward to form a writing surface over drawers or doors.",
 "t":["fall-front (à abattant)","cylinder (secrétaire à cylindre)","mechanical (spring-out slides)","with bookcase above"],
 "s":FR,
 "x":[
  {"n":"Secrétaire à abattant","a":"fall-front secretary · billet-doux (small)","d":"A French upright secretary: top drawer, fall-front writing flap, and two doors or drawers below.","mk":"","y":"18th century","s":FR,
   "v":[{"n":"Billet-doux","mk":"","y":"","d":"small version"}],"dt":"marquetry or veneer · marble top · gilt-bronze mounts · fitted interior"},
  {"n":"Cylinder secretary","a":"secrétaire à cylindre · bureau à cylindre","d":"A desk whose fitted writing area is closed by a solid quarter-cylinder lid.","mk":"","y":"18th century","s":FR,
   "v":[{"n":"Bureau du Roi","mk":"","y":"c. 1760","d":"Louis XV's cylinder desk by Oeben and Riesener, Versailles"}],"dt":"solid quarter-round lid · fitted interior"},
  {"n":"Mission drop-front desk","a":"Arts and Crafts drop-front desk","d":"A plain quartersawn-oak drop-front desk in the American Mission style.","mk":"Gustav Stickley","y":"c. 1903","s":W+"Mission_style_furniture",
   "v":[{"n":"Gustav Stickley drop-front desk","mk":"Gustav Stickley","y":"c. 1903","d":"example in the Brooklyn Museum"}],"dt":"quartersawn white oak · flat panels · exposed joinery"}
 ]},
{"n":"Davenport desk","a":"davenport","d":"A small English desk with a sloping lift-up top over a box, carried on side drawers and front legs or pillars.",
 "t":["side drawers (true or false)","pop-up stationery box","cabriole or pillar front supports"],
 "s":W+"Davenport_desk",
 "x":[{"n":"Gillows Davenport","a":"","d":"The original design made for a Captain Davenport by Gillows of Lancaster.","mk":"Gillows","y":"late 18th century","s":W+"Davenport_desk",
   "v":[{"n":"Victorian davenport","mk":"","y":"19th century","d":"peak popularity; varied, often carved leg designs"},{"n":"Reproduction davenport","mk":"","y":"20th century","d":"many reproductions made"}],
   "dt":"walnut, rosewood, mahogany · leather-lined slope · carved cabriole or pillar supports"}]},
{"n":"Sit-stand desk","a":"standing desk · height-adjustable desk · electric desk","d":"A desk whose height adjusts between sitting and standing, by motor, crank or counterbalance.",
 "t":["electric single-motor","electric dual-motor","crank","counterbalance/gas spring","desk converter (riser on an existing desk)","L-shaped"],
 "s":"https://www.ikea.com/us/en/cat/standing-desks-55008",
 "m":[["UPLIFT V3","UPLIFT Desk"],["EN1","FlexiSpot"],["Comhar","FlexiSpot"],["Duo Standing Desk","Branch"],["Standing Desk","VIVO"],["Copilot Standing Desk","Burrow"],["IDÅSEN","IKEA"],["MITTZON","IKEA"],["TROTTEN","IKEA"]][:6]+[["IDÅSEN","IKEA"],["MITTZON","IKEA"],["RELATERA","IKEA"]]},
{"n":"Dressing table","a":"vanity · vanity table · duchess · toilet table · poudreuse · lowboy","d":"A table with drawers and often a mirror, made to sit at while dressing or applying make-up.",
 "t":["with fixed mirror","with folding or triple mirror","lift-top (poudreuse)","lowboy","bureau dressing table","wall-mounted","with stool"],
 "s":"https://www.ikea.com/nl/en/cat/dressing-tables-20657",
 "m":[["MALM","IKEA"],["HEMNES","IKEA"],["BRIMNES","IKEA"],["NORDKISA","IKEA"],["GRÅFJÄLLET","IKEA"]]},
{"n":"Drafting table","a":"drawing table · drawing board · architect's table","d":"A work table whose top tilts and often rises, made for drawing, drafting or art work.",
 "t":["mechanical (counterweighted)","steel-frame","motorised","convertible to flat desk","tabletop drawing board","antique (wood and brass)"],
 "s":"https://www.google.com/basepages/producttype/taxonomy.en-US.txt"},
{"n":"Lap desk","a":"bed desk · lap tray · laptop lap desk","d":"A small portable surface made to rest on the lap, often cushioned underneath.",
 "t":["cushioned","folding legs (bed tray)","laptop with fan","antique writing slope"],
 "s":"https://www.officedepot.com/b/laptop-stands-and-lap-desks/Product_Type--Lap_Desk/N-1461903",
 "m":[["Home Office Lap Desk","LapGear"],["Sidekick Lap Desk","LapGear"],["Lap Tray with Removable Cushion","LapGear"],["Atlas Lap Desk","LapGear"]]}
]
# fix m lists (avoid non-old models)
kinds[0]["m"]=[["ALEX","IKEA"],["TONSTAD","IKEA"],["ROSENTORP","IKEA"]]
kinds[5]["m"]=[["UPLIFT V3","UPLIFT Desk"],["EN1","FlexiSpot"],["Comhar","FlexiSpot"],["Duo Standing Desk","Branch"],["Standing Desk","VIVO"],["IDÅSEN","IKEA"],["MITTZON","IKEA"],["RELATERA","IKEA"]]
brands=[
 {"n":"IKEA","c":"Sweden","f":"1943","seg":"Mass-market flat-pack furniture","d":"Swedish-founded flat-pack furniture and homeware retailer.","s":"knowledge"},
 {"n":"Gillows","c":"United Kingdom","seg":"Georgian and Victorian cabinetmakers","d":"Gillows of Lancaster, cabinetmakers credited with the original Davenport desk.","sig":["Gillows Davenport"],"s":W+"Davenport_desk"},
 {"n":"Gustav Stickley","c":"United States","seg":"Arts and Crafts / Mission furniture","d":"American Arts and Crafts furniture maker in plain quartersawn oak, often called Mission style.","sig":["Mission drop-front desk"],"rel":["L. & J.G. Stickley","Stickley Brothers","Charles Limbert"],"s":W+"Mission_style_furniture"},
 {"n":"FlexiSpot","c":"China","seg":"Mid-price height-adjustable desks","d":"Maker of electric sit-stand desks and desk risers.","s":"knowledge"},
 {"n":"UPLIFT Desk","c":"United States","seg":"Premium-mid height-adjustable desks","d":"Austin, Texas maker of customisable sit-stand desks.","s":"knowledge"}
]
notes=("Desk: old KALLAX model dropped (it is a shelving unit, not a desk); pedestal/partners/roll-top/etc kept as t types and also given archetypes for named period forms (Pedestal, Partners, Rolltop with Bureau du Roi and Cutler 1882 versions, Wooton 1874, Carlton House, Bonheur du jour, Bureau Mazarin), all from Wikipedia. "
 "New kinds Writing bureau (5 archetypes incl. bureau bookcase, block-front, Governor Winthrop 1924, bureau brisé), Secretaire (abattant, cylinder, Stickley Mission drop-front c.1903; sourced to fr.wikipedia Secrétaire (meuble) and Mission style page) and Davenport desk (Gillows archetype). "
 "Shaker desk left out: Shaker furniture page shows only an undated 'student desk' caption. Sit-stand desk: Wirecutter blocked and Which?/RTINGS URLs 404, so no independent test winner confirmed; added market brands named on a retrieved roundup (drewandjonathan.com page not cited as kind s; UPLIFT V3, FlexiSpot EN1 and Comhar, Branch Duo, VIVO) plus IKEA IDÅSEN, MITTZON, RELATERA; BOLLSIDAN, SEGRARE, TRAVSPORT trimmed. "
 "Dressing table trimmed to 5 IKEA ranges (SYVDE dropped); vanity/poudreuse/lowboy as aliases and t. Drafting table and lap desk kept at restraint level (types only; LapGear models kept). FlexiSpot and UPLIFT Desk register entries from knowledge (country only, no founding year).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B1/shelves/02_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
