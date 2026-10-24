# J1 Meat & Poultry: decided tree

Category: J1 Meat & Poultry (domain J, Groceries). Membership test: meat, poultry, game and other land animals eaten (frogs, insects) as bought, fresh, frozen, cured, smoked or cooked, including whole cuts, mince, offal, sausages, charcuterie, hams, jerky, and cooked, tinned and potted meats (CATEGORIES_v0_7; K-47, K-52). Not here: meat coated (breaded or battered), filled (in pastry, as a dumpling or a stuffed dish), sauced or sold as a ready-to-heat dish (Culinary); spreads and pastes of meat in a jar or tub (rillettes, liver pâté, potted meat), stocks, broths, rendered fats and meat alternatives (J5); fish and seafood, and snails (J2); eggs (J3); meat, bones and offal sold as food for animals (B10); meat protein bars, powders and shakes (H2); living animals (OUT). Structure (Candidate B, decided J-2; memo sections 3 and 10): sub-family by how the meat is prepared for sale (fresh and frozen; cured, smoked and dried whole-muscle; sausages; cooked, tinned and potted), then leaf by one axis per sub-family (the animal in J1.1, with Veal its own leaf and offal under each animal, J-3; cure class in J1.2; process class in J1.3; no leaf in J1.4), then kind: the named retail cut in J1.1 (J-1), with primals and sides sold as such after the retail cuts (J-3) and the placeholder "<species>, whole or jointed" (cut as the attribute `cut`) for a species whose cuts are not yet harvested; the type of cured piece in J1.2; the sausage type in J1.3; the product type in J1.4. Each object gets one kind. Carcass and yield grade (USDA, JMGA, Hanwoo, China), marbling score (BMS), the Ibérico sale name and seal colour, EU poultry farming term, breed (a row of the varieties table, never a kind), feeding, ageing, fat percentage, fresh or frozen, bone and skin, portion, sliced or whole, pack (tin or jar when the same product is also sold unpacked), halal or kosher, organic and farming claims, wild or farmed, and `cut` are attributes, never kinds; origin is a tag; a one-kind designation (Prosciutto di Parma, the ham PDOs) is a non-maker named form, a multi-kind one (Kobe Beef) a tag. Maker role: none (maker_roles.tsv, provisional; grocery rule: breed, cut, grade and origin replace the maker; a ranch or ham house enters only when a quality source names it, R-115 b). Pending kinds: the memo marks 24 kinds † (named without a fetched page); their ids are allocated here in the tree (wave-2 convention, coordinator decision), placed in memo order and numbered after the attested kinds of their parent as the next free numbers (R-58), each line ending in †; a † kind enters the data only when a fetched page attests it (memo section 14, R-96 c). The four final "mixed <class>" kinds (K-46) are all †, at leaf 0 (J1.1.0.01, J1.2.0.01, J1.3.0.01) or, in J1.4 which has no leaf, at J1.4.10; leaves that hold only † kinds are provisional with them. Display groups (navigation proposal, display only, no leaf): P-J1-1 Beef & veal (J1.1.1, J1.1.2); P-J1-2 Pork (J1.1.3); P-J1-3 Lamb & goat (J1.1.4, J1.1.5); P-J1-4 Chicken (J1.1.6); P-J1-5 Turkey, duck & other poultry (J1.1.7, J1.1.8, J1.1.9); P-J1-6 Game (J1.1.10 to J1.1.14); P-J1-7 Ham, bacon & cured meats (J1.2; level-2 display groups ibérico, other dry-cured ham, cooked ham, bacon); P-J1-8 Sausages & salami (J1.3); P-J1-9 Deli, cooked & tinned meats (J1.4). Level-2 display groups for fresh meat (steaks, roasting joints, mince & burgers, slow-cook cuts, offal) are display only; no use class is a leaf. Quality markers (display): beef by marbling and grade (USDA, JMGA/BMS), animal age, breed, feeding, ageing; pork by breed then farming; poultry by farming method and claims; ham by breed × feeding label, cure time and protected origin; sausages by named type and organic.

Ids (R-58): J1.n is a sub-family and J1.n.m a leaf; a kind is J1.n.m.kk, or J1.n.kk where a sub-family has no leaf.

## J1.1 Fresh & frozen meat

Leaf axis: the animal (raw muscle, bone, offal, mince and shaped raw mince, chilled or frozen). Offal sits under each animal (J-3). Kind: the animal and its named retail cut (J-1); a cut enters as a kind on one fetched page showing it sold. Order inside a leaf (memo section 8): whole-muscle steak and roast cuts front to back along the carcass, then kinds sold whole, then primals or sides, then mince, then shaped raw mince, then offal.

### J1.1.1 Beef
- J1.1.1.01 Chuck roast: beef roasting or braising joint from the chuck (shoulder).
- J1.1.1.02 Flat iron steak: beef steak cut from the top blade muscle of the chuck.
- J1.1.1.03 Ribeye steak: beef steak cut from the rib section, bone-in or boneless.
- J1.1.1.04 Striploin steak: beef steak cut from the short loin (strip loin).
- J1.1.1.05 Tenderloin: the beef tenderloin (fillet), whole or cut into steaks.
- J1.1.1.06 T-bone / porterhouse steak: bone-in beef steak from the short loin holding both striploin and tenderloin across a T-shaped bone.
- J1.1.1.07 Top sirloin steak: beef steak cut from the top sirloin (rump side of the loin).
- J1.1.1.08 Rump cap (picanha): the beef rump cap muscle with its fat cap, whole or sliced.
- J1.1.1.09 Skirt steak: beef steak cut from the diaphragm muscles (outer or inner skirt).
- J1.1.1.10 Short rib: beef rib section cut short across or along the bones.
- J1.1.1.11 Brisket: beef joint from the breast, whole or as point or flat.
- J1.1.1.12 Shin / shank: beef cut from the lower leg, on or off the bone.
- J1.1.1.13 Beef primal or side: beef sold as a primal (chuck, rib, loin, round, flank, plate, brisket, shank), side or carcass.
- J1.1.1.14 Ground beef: raw minced beef sold loose or packed.
- J1.1.1.15 Shaped raw mince, beef (burgers, meatballs): raw minced beef shaped into burgers, meatballs or similar, plain or only seasoned.
- J1.1.1.16 Beef tongue: the tongue of cattle, sold raw.

### J1.1.2 Veal
Leaf provisional until its kinds are attested (its only kind is †).
- J1.1.2.01 Sweetbreads: the thymus or pancreas glands of a calf, sold raw (the animal is not stated on the fetched page; veal assumed). †

### J1.1.3 Pork
- J1.1.3.01 Pork jowl: the cheek and jowl of a pig, sold raw.
- J1.1.3.02 Pork collar: pork cut from the neck and upper shoulder (collar, Boston butt).
- J1.1.3.03 Pork loin chop: pork chop cut across the loin, bone-in or boneless.
- J1.1.3.04 Pork tenderloin: the pork tenderloin (fillet), whole or in medallions.
- J1.1.3.05 Pork ribs: pork rib sections (spare ribs, baby back ribs), sold raw.
- J1.1.3.06 Pork belly: raw, uncured pork belly, skin-on or skinless.
- J1.1.3.07 Pork hock: the lower leg joint of a pig above the trotter, sold raw.
- J1.1.3.08 Pork trotter: the foot of a pig, sold raw.
- J1.1.3.09 Suckling pig: a whole milk-fed young pig, sold whole.
- J1.1.3.10 Ground pork: raw minced pork sold loose or packed.
- J1.1.3.11 Shaped raw mince, pork (burgers, meatballs): raw minced pork shaped into burgers, meatballs or similar, plain or only seasoned.

### J1.1.4 Lamb & mutton
- J1.1.4.01 Lamb rack: the rib section of a lamb with its chops joined, sold raw.
- J1.1.4.02 Lamb leg: the hind leg of a lamb, whole or part, on or off the bone.
- J1.1.4.03 Lamb, whole or jointed: lamb or mutton sold whole or as any cut not yet a kind (the cut is the attribute `cut`).
- J1.1.4.04 Suckling lamb: a whole milk-fed young lamb, sold whole.

### J1.1.5 Goat
- J1.1.5.01 Goat, whole or jointed: goat meat sold whole or as any cut (the cut is the attribute `cut`).

### J1.1.6 Chicken
- J1.1.6.01 Whole chicken: a whole dressed chicken carcass, including poussin and capon.
- J1.1.6.02 Chicken breast: the breast meat of a chicken, on or off the bone, skin-on or skinless.
- J1.1.6.03 Chicken leg: the leg of a chicken (thigh and drumstick together or apart).

### J1.1.7 Turkey
- J1.1.7.01 Turkey, whole or jointed: turkey sold whole or as any cut (the cut is the attribute `cut`).

### J1.1.8 Duck & goose
- J1.1.8.01 Duck breast: the breast of a duck, skin-on, sold raw.
- J1.1.8.02 Whole duck: a whole dressed duck carcass.
- J1.1.8.03 Fatty liver (foie gras): the enlarged liver of a duck or goose, sold raw.

### J1.1.9 Game birds
- J1.1.9.01 Pheasant, whole or jointed: pheasant sold whole or as any cut (the cut is the attribute `cut`).
- J1.1.9.02 Partridge, whole or jointed: partridge sold whole or as any cut (the cut is the attribute `cut`).

### J1.1.10 Deer
- J1.1.10.01 Venison saddle: the saddle (loin section) of a deer, on or off the bone.
- J1.1.10.02 Venison medallions: round slices cut from the venison loin.
- J1.1.10.03 Venison, whole or jointed: venison sold whole or as any cut not yet a kind (the cut is the attribute `cut`).

### J1.1.11 Rabbit & hare
- J1.1.11.01 Rabbit, whole or jointed: rabbit sold whole or as any cut (the cut is the attribute `cut`).
- J1.1.11.02 Hare, whole or jointed: hare sold whole or as any cut (the cut is the attribute `cut`).

### J1.1.12 Wild boar
- J1.1.12.01 Wild boar, whole or jointed: wild boar sold whole or as any cut (the cut is the attribute `cut`; wild or farmed is an attribute).

### J1.1.13 Horse
- J1.1.13.01 Horse meat, whole or jointed: horse meat sold whole or as any cut, including raw slices for eating raw (the cut is the attribute `cut`).

### J1.1.14 Other land animals
- J1.1.14.01 Bison, whole or jointed: bison sold whole or as any cut (the cut is the attribute `cut`).
- J1.1.14.02 Frogs' legs: the hind legs of edible frogs, sold raw or frozen. †
- J1.1.14.03 Turtle meat: the meat of turtles sold to eat. †
- J1.1.14.04 Edible insects: crickets, mealworms and other insects sold to eat, fresh, frozen, dried or roasted (attribute `storage_state`; K-47). †

### J1.1.0 Mixed (leaf = null, K-46)
- J1.1.0.01 Mixed fresh meats: a pack of raw meats of several J1.1 kinds, none of which makes up half or more of its weight. †

## J1.2 Cured, smoked & dried whole-muscle meats

Leaf axis: cure class (raw-cured; cooked-cured; dried and jerked; cured fat; pickled and fermented). A whole muscle or piece cured, smoked, dried or pickled, raw or cured then cooked, sold as a piece or sliced. The sale name, seal colour and size of piece are attributes. Order inside a leaf: the canonical dry-cured ham first, then the other pieces front to back (jowl, neck, shoulder, loin, belly, then cured beef).

### J1.2.1 Raw-cured (dry-cured)
- J1.2.1.01 Dry-cured ham, bone-in leg: the hind leg of a pig, salted and air-dried raw, sold whole or sliced.
- J1.2.1.06 Cured pork jowl (guanciale): pork jowl salted and air-dried raw. †
- J1.2.1.02 Cured pork neck: the pork neck (collar) salted and air-dried raw, sold whole or sliced (coppa).
- J1.2.1.03 Cured pork shoulder: the front leg of a pig salted and air-dried raw (paleta).
- J1.2.1.04 Cured pork loin: the pork loin salted, seasoned and air-dried raw in a casing or net (lomo).
- J1.2.1.05 Bacon: cured pork belly, back or loin sold in rashers or a piece to be cooked, smoked or unsmoked.
- J1.2.1.07 Cured pork belly (pancetta): pork belly salted and air-dried raw, eaten without cooking or used in cooking (not the fresh Spanish panceta). †
- J1.2.1.08 Cured beef (bresaola, cecina): a beef whole muscle salted and air-dried raw. †

### J1.2.2 Cooked-cured
- J1.2.2.01 Cooked ham: pork leg cured then cooked, sold whole or sliced, bone-in or boneless, glazed or plain.
- J1.2.2.02 Pastrami: beef cured, seasoned, smoked and cooked, sold as a piece or sliced. †
- J1.2.2.03 Corned beef brisket: beef brisket brine-cured and cooked, sold as a piece or sliced. †

### J1.2.3 Dried & jerked
Leaf provisional until its kinds are attested (its only kind is †).
- J1.2.3.01 Dried meat strips (jerky, biltong): strips or slabs of meat seasoned and dried, sold to eat as they are. †

### J1.2.4 Cured fat
Leaf provisional until its kinds are attested (its only kind is †).
- J1.2.4.01 Cured back fat (lardo, salo): pork back fat cured with salt and seasoning, not rendered. †

### J1.2.5 Pickled & fermented
Leaf provisional until its kinds are attested (its only kind is †; the leaf is † in the memo).
- J1.2.5.01 Pickled or fermented meat (pickled chicken feet, nem): meat preserved by pickling in vinegar or brine, or by lactic fermentation, outside a sausage casing. †

### J1.2.0 Mixed (leaf = null, K-46)
- J1.2.0.01 Mixed cured meats: a pack of cured meats of several J1.2 kinds, none of which makes up half or more of its weight. †

## J1.3 Sausages

Leaf axis: process class (fresh, to be cooked; dry-cured and fermented; scalded; cooked, liver and blood). Comminuted meat in a casing or formed as a sausage. Order: by process class, then the canonical form of the class first. Regional varieties (Cumberland, Milano, Toscana) are named forms.

### J1.3.1 Fresh, to be cooked
- J1.3.1.01 Fresh pork sausage: raw seasoned minced pork in a casing, sold to be cooked.

### J1.3.2 Dry-cured & fermented
- J1.3.2.01 Dry-cured salami: fermented, air-dried sausage of chopped meat and fat, eaten without cooking.
- J1.3.2.02 Paprika dry-cured sausage (chorizo): dry-cured sausage seasoned with paprika.
- J1.3.2.03 Spreadable dry-cured sausage ('nduja): soft, spreadable fermented pork sausage with chilli, sold in a casing (a jar of spread is J5). †

### J1.3.3 Scalded
- J1.3.3.01 Frankfurter / wiener: thin scalded sausage of finely emulsified meat, usually smoked, heated or eaten cold.
- J1.3.3.02 Large emulsified scalded sausage (mortadella): large-calibre scalded sausage of finely emulsified meat, often with cubes of fat, sold for slicing.

### J1.3.4 Cooked (liver, blood)
- J1.3.4.01 Liver sausage: cooked sausage made mainly of liver and meat, sliced or spread from the casing.

### J1.3.0 Mixed (leaf = null, K-46)
- J1.3.0.01 Mixed sausages: a pack of sausages of several J1.3 kinds, none of which makes up half or more of its weight. †

## J1.4 Cooked, tinned & potted meats

No leaf (memo: about 12 kinds at most, C5(b); if it passes about 12 kinds it takes three leaves, axis how the cooked meat is kept or sold: plain-cooked, tinned and potted, pâtés and terrines). Kind: the product type; the animal (duck, game, poultry) is an attribute. Order: plain-cooked, then tinned and potted, then pâtés and terrines. Only pâté and terrine are attested; the other kinds are †.
- J1.4.03 Plain-cooked whole bird (rotisserie chicken): a whole bird roasted or cooked plain or only seasoned, sold ready to eat. †
- J1.4.04 Plain-cooked sliced meat (roast beef, roast turkey): a cut roasted or cooked plain or only seasoned, sold whole or sliced to eat cold (porchetta a named form). †
- J1.4.05 Plain-cooked shaped mince (cooked meatball, patty, meat loaf): minced meat of one animal shaped and cooked, plain or only seasoned, not coated, filled or sauced. †
- J1.4.06 Corned beef in a tin: cured, cooked beef sealed and cooked in its tin. †
- J1.4.07 Luncheon meat: cured, seasoned minced meat formed into a block and cooked in a sealed tin. †
- J1.4.08 Confit: meat (duck, goose, pork) cooked slowly and preserved in its own fat, in a tin, jar or pot. †
- J1.4.09 Head cheese (brawn): pieces of head meat set in their own jelly, sold as a loaf or slice. †
- J1.4.01 Pâté (loaf or slice): a cooked, finely or coarsely ground meat mixture sold as a loaf or slice to be cut (a spread in a jar or tub is J5).
- J1.4.02 Terrine: a cooked meat preparation set in a terrine mould, sold whole or sliced (duck, game, poultry terrine).
- J1.4.10 Mixed cooked meats: a pack of cooked meats of several J1.4 kinds, none of which makes up half or more of its weight (final kind, K-46; J1.4 has no leaf, so it takes the sub-family's next number). †

## Precedence inside J1

- Level-1 tie-break (first yes; C5(c)): (1) comminuted meat sold as a sausage, in a casing or formed as a sausage, fresh, cured, scalded or cooked, is Sausages (J1.3); (2) meat that is cooked, tinned, potted or made into a pâté or terrine, as a product that exists in that form (corned beef in a tin, luncheon meat, confit or brawn set in fat or jelly, sliced roast meat, a rotisserie chicken, a pâté loaf), and a plain or only seasoned shaped product of one meat sold cooked (a cooked meatball or patty), or a herb-rolled or glazed uncured roast sold to slice (porchetta), is Cooked, tinned & potted (J1.4; K-45); (3) a whole muscle or piece cured, smoked, dried or pickled, raw or cured then cooked (dry-cured ham J1.2.1.01, bacon J1.2.1.05, cooked ham J1.2.2.01, pastrami J1.2.2.02), is Cured, smoked & dried (J1.2); (4) everything else raw, chilled or frozen is Fresh & frozen (J1.1).
- Pack (JC4): a tin, jar or pouch is a pack attribute when the same product is also sold unpacked (a cooked ham or a sausage in a tin keeps its home); it makes a J1.4 kind only when the product exists as tinned-cooked-in-the-pack or as a solid potted piece set in fat or jelly (JC4(b)). A cured piece that is cooked or glazed (glazed ham) stays in Cooked-cured as a named form of cooked ham (J1.2.2.01; K-45); pastrami and corned brisket sold as a piece stay in Cooked-cured, and the same meat sealed in a tin is corned beef in a tin (J1.4.06; K-52).
- Mince against sausage: loose or patted mince is J1.1 (ground beef J1.1.1.14, ground pork J1.1.3.10); a raw shaped burger or meatball, plain or only seasoned, is shaped raw mince (J1.1.1.15, J1.1.3.11); the same shaped mince sold cooked is plain-cooked shaped mince (J1.4.05; K-45); minced meat in a casing or formed as a sausage is J1.3.
- Kind rule in J1.1 (J-1, J-3): the kind is the animal and its named retail cut; national names, sub-cuts and bone or trim variants are named forms or attributes (entrecôte under ribeye steak J1.1.1.03, 五花肉 under pork belly J1.1.3.06). A cut of a species with no harvested cut kinds goes to "<species>, whole or jointed" with the cut as the attribute `cut` (wild boar haunch J1.1.12.01); the placeholder then keeps only the animal sold unjointed and cuts not yet kinds. An animal sold whole (suckling pig J1.1.3.09, suckling lamb J1.1.4.04) is a kind of its own; primals, sides and carcasses sold as such are kinds after the retail cuts (beef primal or side J1.1.1.13). Offal is filed under its animal (beef tongue J1.1.1.16, pork trotter J1.1.3.08, fatty liver J1.1.8.03).
- Homonym: Spanish panceta is fresh pork belly (J1.1.3.06); Italian pancetta is cured pork belly (J1.2.1.07).
- Ibérico and other dry-cured hams: the sale name (bellota, cebo de campo, cebo; 100 %, 75 %, 50 % Ibérico) and seal colour are attributes; a protected name binding one kind (Prosciutto di Parma, Jabugo) is a non-maker named form of dry-cured ham (J1.2.1.01).
- Mixed packs (P10, K-46): a mix of J1 kinds is filed under the kind that makes up half or more of its weight; otherwise under the final kind "mixed <class>" of the lowest level holding all its parts, stored with leaf = null (mixed fresh meats, mixed cured meats, mixed sausages, mixed cooked meats: J1.1.0.01, J1.2.0.01, J1.3.0.01, J1.4.10). A pack that spans sub-families with no kind at half weight is filed by its item of greatest value (P7, applied by default).
- 'nduja sold in a casing is a sausage (J1.3.2.03); in a jar it is a spread (J5). Liver sausage (J1.3.4.01) in a casing is J1; liver paste in a jar or tub is J5. A pâté or terrine sold as a loaf or slice is J1.4 (J1.4.01, J1.4.02); a cooked foie gras terrine is a terrine (J1.4.02), raw duck liver is fatty liver (J1.1.8.03).
- Frogs' legs, turtle meat and edible insects are Other land animals (J1.1.14.02 to J1.1.14.04; K-47); snails are J2.
- Unrendered fat and bones sold as a cut (fatback, marrow bones) are J1 under their animal; cured back fat is J1.2.4.01; rendered fat is J5.
