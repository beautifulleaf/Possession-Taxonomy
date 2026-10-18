# J3 Dairy, Eggs & Alternatives: decided tree

Category: J3 Dairy, Eggs & Alternatives (domain J, Groceries & Cellar). Membership test: milk, cream, butter and ghee, yoghurt and kefir, cheese and eggs, milk powders and infant formula, and plant-based alternatives to them (plant drinks, plant yoghurts, plant cheeses, plant creams and creamers, plant egg alternatives), as the product is bought. Structure (Candidate A, J-6): sub-family by the dairy or egg product family the object is or replaces, then leaf by one axis per sub-family (only where a sub-family has more than about 12 kinds: Cream and butter, Cheese, Plant-based alternatives), then kind at product-type level (the variety for cheese). Each object gets one kind. Sub-families without a leaf (Milk, Yoghurt and fermented milks, Eggs, Milk powders and infant formula) have kind ids without a leaf part. Cheese also holds the final kind Mixed cheeses with leaf = null, which takes leaf 0. A kind marked † is named only by a navigation box, the framework key, a review or a decision and needs a fetched page before it enters the data; kinds with regional-word labels keep their level as provisional until attested (R-19). Fat level, salt, treatment, lactose-free, A2, organic, farming code, class, size, grade, stage, protein base, plant base, flavour, age, format and milk species (except where the species names the kind, in Milk and Eggs) are attributes and never kinds. Protected names and maker lines are named forms, not kinds.

Ids (R-58): J3.n is a sub-family and J3.n.m a leaf; a kind is J3.n.m.kk, or J3.n.kk where a sub-family has no leaf.

## J3.1 Milk (no leaf)

Axis: the product kinds buttermilk, evaporated and condensed milk and dulce de leche are tested first; otherwise the animal source of the drinking milk (the species names the kind here). Fat level, treatment, A2, lactose-free and organic are attributes.
- J3.1.01 Cow's milk [牛乳]: liquid milk of the cow, whatever its fat level or treatment, including lactose-free cow's milk.
- J3.1.02 Buffalo milk: liquid milk of the buffalo. †
- J3.1.03 Goat's milk: liquid milk of the goat.
- J3.1.04 Sheep's milk: liquid milk of the sheep. †
- J3.1.05 Buttermilk: plain fermented or cultured liquid left from or made to resemble the churning of butter, sold as a drink or cooking liquid. †
- J3.1.06 Evaporated and condensed milk: milk with part of its water removed, unsweetened (evaporated) or sweetened (condensed), sold tinned or tubed. †
- J3.1.07 Dulce de leche: sweetened milk cooked down to a thick caramel-like milk spread. †

## J3.2 Cream and butter

Leaf axis: the milk-fat product (cream, or butter and ghee).

### J3.2.1 Cream
Cream types named by fat tier and culture; the fat percentage is a measured attribute with its standard, which differs by jurisdiction.
- J3.2.1.01 Single (light) cream: pouring cream of lower fat content that does not whip.
- J3.2.1.02 Whipping cream: cream of a fat content that whips.
- J3.2.1.03 Thickened cream: cream with a thickener added to a whipping fat tier so that it holds its shape when whipped.
- J3.2.1.04 Double cream: cream of the highest pouring and whipping fat tier.
- J3.2.1.05 Soured cream: cream cultured to a sour, thick finish. †
- J3.2.1.06 Crème fraîche: thick cultured cream with a mild sour taste. †

### J3.2.2 Butter and ghee
Butter made from milk fat, its blends that contain butter, and its clarified forms.
- J3.2.2.01 Butter: churned milk fat and water, salted or unsalted.
- J3.2.2.02 Spreadable butter blend: spread of butter blended with vegetable oil; a spread that contains butter.
- J3.2.2.03 Clarified butter: butter with its water and milk solids removed.
- J3.2.2.04 Ghee: clarified butter cooked until its milk solids brown, with a nutty flavour and long shelf life.

## J3.3 Yoghurt and fermented milks (no leaf)

Axis: the culture-defined or concentration-defined type. Test order: kefir or kumys culture; plain drinking yoghurt; skyr; strained yoghurt; other concentrated fermented milk; then yoghurt. Flavour, fat, milk species and probiotic or high-protein claims are attributes.
- J3.3.01 Yoghurt [ヨーグルト]: milk fermented with yoghurt culture, set or stirred, plain or fruited, spoon-eaten.
- J3.3.02 Drinking yoghurt, plain: plain unsweetened drinkable fermented milk (ayran and plain lassi are named forms); sweetened or flavoured drinks are not in J3. †
- J3.3.03 Kefir: milk fermented with kefir culture (grains), a tart drinkable fermented milk.
- J3.3.04 Kumys: fermented mare's or other milk of the Central Asian type, defined by its culture.
- J3.3.05 Strained (Greek-style) yoghurt: yoghurt with whey strained off to a thick, concentrated texture.
- J3.3.06 Skyr: strained cultured milk product of Nordic origin, sold as a yoghurt.
- J3.3.07 Other concentrated fermented milk: concentrated fermented milk that is neither strained yoghurt nor skyr (labneh, ymer, ylette).

## J3.4 Cheese

Leaf axis: family of the curd and its maturing, tested by the first-yes key in the order below (leaf numbers follow the order of the leaves, wet to dry, then blue and processed). The final kind Mixed cheeses has leaf = null and sits at leaf 0.
1. Processed (melted, emulsified): J3.4.10.
2. Dried or dehydrated to a shelf-stable solid, not ripened: J3.4.8.
3. Blue-veined: J3.4.9.
4. White-mould rind: J3.4.4.
5. Matured in brine: J3.4.2.
6. Stretched curd (pasta filata): J3.4.3.
7. Unripened, or a whey cheese: J3.4.1.
8. Soft or semi-soft with a washed or smear rind (pungent orange rind): J3.4.5.
9. Otherwise by Codex firmness: firm or semi-hard to J3.4.6, hard or extra-hard to J3.4.7.

### J3.4.1 Fresh and whey cheeses
Unripened cheeses and whey cheeses.
- J3.4.1.01 Cottage cheese: fresh curd cheese in loose curds with a cream dressing.
- J3.4.1.02 Cream cheese: soft, spreadable fresh cheese of milk and cream.
- J3.4.1.03 Paneer: fresh, unsalted, non-melting acid-set curd cheese of South Asia.
- J3.4.1.04 Quark [Speisequark]: fresh, soft, strained sour-milk cheese, spoonable.
- J3.4.1.05 Spreadable soft cheese: fresh soft cheese sold to spread, seasoned or plain, other than cream cheese.

### J3.4.2 Brined cheeses
Cheeses matured and kept in brine.
- J3.4.2.01 Feta: white cheese matured in brine, crumbly and salty.

### J3.4.3 Stretched-curd cheeses
Pasta filata cheeses, whose curd is heated and stretched.
- J3.4.3.01 Burrata: stretched-curd pouch filled with strands of curd and cream.
- J3.4.3.02 Mozzarella: stretched-curd cheese, moist and mild, fresh or low-moisture.

### J3.4.4 Bloomy-rind soft cheeses
Soft cheeses ripened from the outside under a white-mould rind.
- J3.4.4.01 Brie: large, flat white-mould soft cheese.
- J3.4.4.02 Camembert: small, round white-mould soft cheese.

### J3.4.5 Washed-rind cheeses
Soft or semi-soft cheeses with a washed or smear rind, pungent and orange.
- J3.4.5.01 Limburger: soft cheese with a washed rind and a strong smell.

### J3.4.6 Semi-hard pressed cheeses
Firm or semi-hard pressed cheeses by Codex firmness, not blue, brined, stretched or smear-rind soft.
- J3.4.6.01 Cheddar: semi-hard pressed cheese made by cheddaring the curd, mild to vintage by age.
- J3.4.6.02 Emmental: semi-hard Alpine cooked-pressed cheese with large holes.
- J3.4.6.03 Gouda: semi-hard pressed round cheese of Dutch type, young to aged.
- J3.4.6.04 Havarti: semi-hard, smooth, buttery pressed cheese with small irregular holes.

### J3.4.7 Hard and long-aged cheeses
Hard or extra-hard pressed cheeses, aged for long periods.
- J3.4.7.01 Grana-type hard cheese (parmesan): hard, granular, long-aged cheese of the grana kind. †
- J3.4.7.02 Pecorino: hard sheep's-milk cheese, salted and aged.

### J3.4.8 Dried and preserved dairy (provisional until attested, K-55)
Dairy dried or dehydrated to a shelf-stable solid as its main preservation, not ripened; the kind or named-form level of each entry is set at the harvest (R-19).
- J3.4.8.01 Aaruul: sun-dried hard curd of Mongolia. †
- J3.4.8.02 Chhurpi: hard dried cheese of the Himalaya. †
- J3.4.8.03 Jameed: hard dried salted yoghurt of the Levant. †
- J3.4.8.04 Kashk: dried whey or strained yoghurt product of Iran and the Middle East. †
- J3.4.8.05 Qurut: dried salted yoghurt balls of Central Asia. †

### J3.4.9 Blue cheeses
Blue-veined cheeses. The two protected cheeses below are kinds because no generic sibling is sold under their names; their kind level is provisional until attested (fallback: named forms under a generic "blue cheese").
- J3.4.9.01 Blue cheese (Gorgonzola): blue-veined cheese of the Gorgonzola type, creamy to firm.
- J3.4.9.02 Blue cheese (Stilton): blue-veined, crumbly, firm cheese of the Stilton type.

### J3.4.10 Processed cheese
Melted and emulsified cheese.
- J3.4.10.01 Processed cheese: cheese melted with emulsifiers and re-formed as slices, blocks or spread.

### J3.4.0 Mixed cheeses (leaf = null)
A mix of cheeses none of which is half or more of the weight (K-46).
- J3.4.0.01 Mixed cheeses: selection of cheeses (for example a selection box) none of which is half or more of the weight. †

## J3.5 Eggs (no leaf)

Axis: tested in this order: preserved or plain-cooked form (any species), then species. Class, grade, size, farming code, organic and breed line are attributes.
- J3.5.01 Hen's egg [たまご]: egg of the domestic hen in the shell, raw.
- J3.5.02 Duck egg: egg of the duck in the shell, raw. †
- J3.5.03 Quail egg: egg of the quail in the shell, raw. †
- J3.5.04 Preserved or plain-cooked egg: egg of any species salted, pickled, cured (century) or plainly boiled in the shell. †

## J3.6 Milk powders and infant formula (no leaf)

Axis: the product type. Stage number, protein base, casein or whey ratio and liquid or powder form are attributes.
- J3.6.01 Skimmed milk powder: dried milk with the fat removed.
- J3.6.02 Whole milk powder: dried whole milk. †
- J3.6.03 Infant formula: breast-milk substitute for babies in the first months, a normal food (first or stage 1 formula).
- J3.6.04 Follow-on formula: milk formula for babies from about six months.
- J3.6.05 Growing-up milk: milk drink for toddlers and young children, outside the infant formula categories.

## J3.7 Plant-based alternatives

Leaf axis: the animal-derived product replaced (drink, yoghurt, cheese, cream or creamer, egg).

### J3.7.1 Plant drinks
Drinks sold as an alternative to milk, divided by plant base.
- J3.7.1.01 Almond drink: drink made from almonds.
- J3.7.1.02 Coconut drink: coconut drink sold as a milk alternative (coconut milk and cream for cooking are J5).
- J3.7.1.03 Oat drink: drink made from oats.
- J3.7.1.04 Soy drink: drink made from soya beans.

### J3.7.2 Plant yoghurts
- J3.7.2.01 Plant yoghurt: fermented or cultured plant product sold as a yoghurt alternative, whatever its base.

### J3.7.3 Plant cheeses
Plant products sold as an alternative to cheese, divided by texture family; format is an attribute.
- J3.7.3.01 Plant cheese, firm style: block, sliced or grated plant cheese alternative.
- J3.7.3.02 Plant cheese, soft style: spreadable, soft, camembert- or blue-style plant cheese alternative.

### J3.7.4 Plant creams and creamers
- J3.7.4.01 Plant cream: plant product sold as a replacement for cream.
- J3.7.4.02 Plant creamer: plant product sold as a replacement for cream or milk in coffee or tea.

### J3.7.5 Plant egg alternatives
- J3.7.5.01 Plant egg alternative: plant product sold as a replacement for egg (for example aquafaba).

## Precedence inside J3

- Species names the kind only in Milk (J3.1.01 to J3.1.04) and Eggs (J3.5.01 to J3.5.03); in every other sub-family milk species is an attribute (a sheep's-milk yoghurt is J3.3.01, a goat's-milk cheese goes by its variety, goat formula is J3.6.03 or J3.6.04).
- In Milk, buttermilk (J3.1.05), evaporated and condensed milk (J3.1.06) and dulce de leche (J3.1.07) are tested first; any other drinking milk goes by its animal source. Lactose-free, filtered, long-life, A2 and organic cow's milk is J3.1.01, though retailers file it with plant drinks.
- In Yoghurt and fermented milks the kinds are tested in this order: kefir or kumys culture (J3.3.03, J3.3.04); plain drinking yoghurt (J3.3.02); skyr (J3.3.06); strained yoghurt (J3.3.05); other concentrated fermented milk (J3.3.07); then yoghurt (J3.3.01). Skyr is J3.3.06 and quark is J3.4.1.04; labneh is J3.3.07. A sweetened or flavoured drinking yoghurt is not in J3.
- In Cheese the leaf is given by the first-yes key under J3.4: processed (J3.4.10), then dried and preserved dairy (J3.4.8), blue (J3.4.9), white-mould rind (J3.4.4), brine (J3.4.2), stretched curd (J3.4.3), unripened or whey (J3.4.1), washed or smear rind when soft or semi-soft (J3.4.5), and otherwise Codex firmness (J3.4.6 or J3.4.7). A hard smear-rind cheese (Appenzeller, Comté) therefore goes by firmness; a soft blue (Cambozola, Gorgonzola dolce) is J3.4.9; smoked scamorza is J3.4.3.
- A cheese variety is filed once, by its ordinary retail form; age and the band it falls in as it matures are attributes, so a young and a vintage Cheddar are both J3.4.6.01.
- A cheese kind is a variety made under that name by unrelated makers and labelled generically (Cheddar, Gouda, Emmental, brie, camembert, feta, mozzarella, Pecorino, grana-type hard cheese). A protected name that binds one kind is a non-maker named form of that kind (Parmigiano Reggiano and Grana Padano under J3.4.7.01; Mozzarella di Bufala Campana under J3.4.3.02; Feta PDO under J3.4.2.01; West Country farmhouse Cheddar under J3.4.6.01). A protected cheese with no generic sibling sold under its name is a kind (J3.4.9.01 Gorgonzola, J3.4.9.02 Stilton), provisional until attested.
- A mix of cheeses goes under the cheese kind that makes up half or more of its weight; if none does, it is J3.4.0.01 Mixed cheeses. A mix across J3 sub-families with no kind at half the weight (cheese and butter) is filed by its item of greatest value.
- In Eggs, a preserved or plain-cooked egg of any species (J3.5.04) is tested first; otherwise the species decides (J3.5.01 to J3.5.03).
- Butter and ghee: a spread that contains butter (butter and rapeseed oil blend) is J3.2.2.02; butter is J3.2.2.01; margarine and plant-only fat spreads are not in J3. Soured cream and crème fraîche are J3.2.1.05 and J3.2.1.06, not yoghurt.
- A plant product made to replace milk, yoghurt, cheese, cream, creamer or egg is in J3.7 and not under the dairy sub-family it imitates (an oat drink is J3.7.1.03, not J3.1; a plant soft cheese is J3.7.3.02, not J3.4.1). A soy-based infant formula is an infant formula (J3.6.03), not a plant alternative.
- Milk powders and infant formula: milk powders (J3.6.01, J3.6.02) first, then formula by the age of the infant (J3.6.03, J3.6.04, J3.6.05). A formula made for a named medical condition is not in J3; a partially hydrolysed range sold without a medical claim stays in J3.6.
