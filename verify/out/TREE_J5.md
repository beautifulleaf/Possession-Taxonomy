# J5 Pantry Staples: decided tree

Category: J5 Pantry Staples (domain J, Groceries). Membership test: pantry staples as bought: rice, grains, flours, oats and breakfast cereals, dried and fresh unfilled pasta and noodles, gnocchi, pulses, nuts and seeds, dried fruit, dried vegetables, dried mushrooms and dried seaweed, oils, cooking fats and vinegars, spices, dried herbs and salt, sugar, honey (including honeycomb) and syrups, sweet and savoury spreads, sauces, condiments, stocks and pastes from any source, coconut milk and cream, pickles and preserves, tinned and jarred fruit, vegetables, pulses and tomatoes, baking ingredients (raising agents and dried yeast, baking chocolate, unbaked doughs and pastry, cake and baking mixes), home-brewing and winemaking ingredients, wines, sake and bitters made for cooking or flavouring, tofu, tempeh, seitan and other plant proteins and meat alternatives (CATEGORIES_v0_7, step 3 branch 5; K-24, K-44 to K-46, K-48, K-50, K-53, K-54, K-58, K-59, K-75). Not here: butter, ghee, cheese, spreads and fresh cheeses made from milk, a fat spread containing butter, and plant substitutes for milk, cream, cheese or yoghurt (J3); fresh and frozen fruit, vegetables, herbs, mushrooms and seaweed, and fresh olives (J4); dried, cured and tinned meat and fish, sliceable pâtés and terrines, and whole salted-fermented seafood (J1, J2); coffee, tea, cocoa powder, cocoa butter and cocoa paste, roasted grains and roots sold to brew, and dry drink mixes led by coffee, tea or cocoa (J6); wines, sake, spirits and bitter liqueurs sold to drink (J7); prepared foods: bakery, confectionery, snacks, ready meals, soups, filled pasta and dumplings, noodle cups and pots, rice or pulses cooked in a seasoned sauce, nuts coated in chocolate, sugar or batter, sprinkles, and coated, filled or sauced plant-protein products (OUT); plants and seed sold to grow (C3); vitamins, supplements and sports nutrition (H2); CBD products and the step-27 products (B9); food for animals (B10); pasta machines, grinders, spice racks and brewing equipment (B5). Structure (Candidate A, decided J-11; memo sections 3 and 10): sub-family by what the product is made from or what it is (the ingredient or product family), then leaf by one axis stated per sub-family, with no sub-family skipping the leaf level, then kind at the level of memo section 4b: grain type and cultivar group (rice), grain and use class (flour), shape family (durum pasta, J-1), base and style (noodles), species (pulses, nuts), source plant (oils; olive oil one kind, J-13), raw material (vinegars; balsamic its own kind), single spice or named blend, crystal class (salt), floral source (honey), the five JAS types (soy sauce, J-13), product type (sauces, condiments, spreads, baking aids, plant proteins) and the crop as preserved (J5.10). Each object gets one kind. Milling, age in months, cooked pouch, fresh or dried (`storage_state`), pack (dried, tinned, jarred, carton, pouch), whole or split, form (in shell, shelled, ground, flaked), roast and salt, legal or measured grade (olive-oil category, JAS grade, ISO 3632 category and cut, UMF, MGO, USDA nut grade, flour type number, balsamic age class), firmness, instant, origin, organic and the DPH attributes `harvest_date`, `broken_pct`, `grain_length_mm`, `moisture_pct`, `additive_free` and `certification` (organic, non-GMO, regenerative organic, fair trade) are attributes, never kinds; cultivars, pasta cuts, protected names binding one kind (Aceto Balsamico Tradizionale di Modena DOP, Aceto Balsamico di Modena IGP, San Marzano DOP) and maker lines are named forms. The level of the regional-word kinds (udon, somen, ramen, soba, glass noodles, atta, besan, sooji, poha, sabudana, whole cane sugar blocks) is provisional until attested (CV-27). A kind marked † is named by the memo without a fetched page; its id is fixed (memo section 13, R-58), but by memo section 14 (DPH, R-96 c) it waits for attestation before it enters data/kinds.tsv. Leaves marked "no kinds decided" hold no kind yet; the possible kinds the memo names for them get no id (R-96 c) and are listed as kinds to look for. Maker role: none (maker_roles.tsv, provisional; grocery rule, makers come through branded products), with the R-115 b exception: a producer enters when a quality source names it (Great Taste winner, Slow Food Presidium, NYIOOC or Olive Oil Times ranking, consortium list of acetaie, JAS-certified brewery, specialist shop selection), never by regional harvest. Display groups (navigation proposal, display only, no id changes): G-J5-1 Oils, fats & vinegars (J5.5); G-J5-2 Rice, pasta, grains & pulses (J5.1.1 to J5.1.3, J5.2, J5.3); G-J5-3 Flour, sugar & baking (J5.1.4, J5.7.1, J5.11); G-J5-4 Spices, salt & stocks (J5.6, J5.9.5); G-J5-5 Sauces & condiments (J5.9.1 to J5.9.4, J5.9.6); G-J5-6 Tins, jars & preserves (J5.10.2 to J5.10.5, with cross-links only to tinned fish J2.4 and tinned meat in J1); G-J5-7 Nuts, seeds & dried fruit (J5.4, J5.10.1); G-J5-8 Honey, syrups & spreads (J5.7.2, J5.7.3, J5.8); G-J5-9 Tofu & meat alternatives (J5.12); level-2 groups G-J5-10 to G-J5-34 follow the leaves (olive oil apart from the other plant oils). Flour shown with baking and stocks shown with spices and salt are display only (DPH, display_only); the tree placement stands. Dried seaweed J5.10.1.02 is cross-linked from J4 group G-J4-26. Quality markers (display): olive oil by legal grade, harvest date and freshness, flavour and cultivar, dark glass or tin; balsamic by designation (Tradizionale DOP, Modena IGP, condiment), age class, clean label; basmati by variety, grain length, broken grains, age, moisture, chalky grains; Japanese rice by area-by-cultivar rank; soy sauce by JAS type, JAS grade, brewing method; saffron by ISO 3632 category, then cut; honey by floral source, then measured grade (manuka UMF, MGO); spices by traceable single origin and freshness (provisional); nuts by USDA grade by nut and form (provisional); pasta, sauces, tins, spreads and baking by product type, clean label and awards (provisional); every product by blind-tasting awards (Great Taste 3, 2, 1 stars).

Ids (R-58): J5.n is a sub-family and J5.n.m a leaf; a kind is J5.n.m.kk, or J5.n.kk where a sub-family has no leaf.

## J5.1 Rice, grains & flours

Leaf axis: the grain and its form as sold, an ordered key, first yes: (1) milled to flour or meal: Flours & meals; (2) a rice grain, whole or flattened: Rice; (3) oats, or a cereal made to eat at breakfast: Oats & breakfast cereals; (4) otherwise: Other grains, pseudo-cereals & starch pearls.

### J5.1.1 Rice
Kinds are grain types and cultivar groups as sold. Kind key, first yes: flattened; glutinous; red or black bran; basmati group; jasmine group; sold as risotto rice; sold as paella rice; long-grain; otherwise medium- and short-grain. Milling (white, brown, parboiled), the "boiled" process, age in months and cooked state in a pouch are attributes.
- J5.1.1.01 Long-grain rice: slender non-aromatic rice grains that stay separate when cooked.
- J5.1.1.02 Basmati rice: the long, aromatic, aged grain of the basmati group.
- J5.1.1.03 Jasmine rice: the long, soft, fragrant grain of the jasmine group. †
- J5.1.1.04 Medium- and short-grain rice: rounder rice that cooks tender and clings, including sushi and pudding rice and the Indian table rices.
- J5.1.1.05 Risotto rice: rice sold for risotto because it gives up starch as it cooks.
- J5.1.1.06 Paella rice: rice sold for paella because it absorbs a lot of stock and stays whole.
- J5.1.1.07 Glutinous (sticky) rice: rice that turns sticky and translucent when cooked, of any bran colour. †
- J5.1.1.08 Red and black rice: non-glutinous rice with a red or black bran layer left on. †
- J5.1.1.09 Flattened rice (poha): rice grains steamed or parboiled and rolled flat.

### J5.1.2 Other grains, pseudo-cereals & starch pearls
- J5.1.2.01 Millet: small whole millet grains (finger, foxtail, kodo and others).
- J5.1.2.02 Quinoa: the seed of the quinoa plant sold as a grain.
- J5.1.2.03 Wild rice: the long dark grain of the aquatic grass Zizania, not a rice plant.
- J5.1.2.04 Tapioca pearls (sabudana): dried pearls of cassava starch.

### J5.1.3 Oats & breakfast cereals
No kinds decided (the shelf is attested; its kinds are †). Kinds to look for (no id, R-96 c): oats and breakfast cereal types.

### J5.1.4 Flours & meals
Kinds are by grain, and for wheat by use class. Type numbers (405, 550, 1050, 1150; Tipo 00) are attributes with the standard named. Ground nuts (almond flour) are nuts in J5.4, not flour.
- J5.1.4.01 Plain / all-purpose wheat flour: refined soft-wheat flour for general baking and cooking.
- J5.1.4.02 Bread and pizza wheat flour: stronger wheat flour for yeast doughs.
- J5.1.4.03 Wholemeal wheat flour: wheat flour milled from the whole grain.
- J5.1.4.04 Rye flour: flour milled from rye.
- J5.1.4.05 Spelt flour: flour milled from spelt.
- J5.1.4.06 Whole-wheat atta: finely ground whole-wheat flour for South Asian flatbreads.
- J5.1.4.07 Semolina (sooji, rava): coarse granular milled wheat endosperm.
- J5.1.4.08 Chickpea flour (besan): flour milled from chickpeas.
- J5.1.4.09 Rice flour: flour milled from rice.

## J5.2 Pasta & noodles

Leaf axis: the dough base, an ordered key, first yes: (1) potato dough: Gnocchi; (2) buckwheat in the dough: Buckwheat noodles; (3) egg dough: Egg pasta & egg noodles; (4) rice flour or a pure starch (mung bean, potato): Rice & starch noodles; (5) durum wheat semolina, including whole-wheat durum: Durum wheat pasta; (6) soft wheat flour: Soft-wheat noodles; (7) any other flour: Other-flour pasta & noodles. Fresh or dried is the attribute `storage_state`. Cuts within a shape family (spaghetti, penne, fusilli) are named forms of the family kind; a maker line is a maker-bound named form with its cut recorded (J-1).

### J5.2.1 Durum wheat pasta
- J5.2.1.01 Long-strand pasta: long cut strands of durum pasta, solid or hollow.
- J5.2.1.02 Tube pasta: short hollow cuts of durum pasta.
- J5.2.1.03 Short and twisted pasta: short solid shapes of durum pasta, twisted, shell or bow.
- J5.2.1.04 Soup pasta (pastina): very small shapes of durum pasta for cooking in broth.

### J5.2.2 Egg pasta & egg noodles
- J5.2.2.01 Egg pasta, ribbons and nests: pasta or noodles made with egg in the dough, cut into ribbons or coiled nests.

### J5.2.3 Soft-wheat noodles
A dry instant noodle brick, with or without a flavour sachet, is a noodle of its kind (attribute `instant`, K-24); a cup or pot of noodles is a ready meal and is not in J5.
- J5.2.3.01 Udon: thick Japanese wheat noodles.
- J5.2.3.02 Somen: very thin Japanese wheat noodles.
- J5.2.3.03 Ramen noodles: alkaline wheat noodles, fresh, dried or in an instant brick.

### J5.2.4 Buckwheat noodles
- J5.2.4.01 Soba: Japanese noodles made with buckwheat flour; the buckwheat share is an attribute.

### J5.2.5 Rice & starch noodles
- J5.2.5.01 Glass noodles (harusame): transparent noodles made from mung bean, potato or a similar pure starch.

### J5.2.6 Other-flour pasta & noodles
No kinds decided. Kinds to look for (no id, R-96 c): legume pasta †, and gluten-free versions of the cuts.

### J5.2.7 Gnocchi
- J5.2.7.01 Potato gnocchi: small unfilled dumplings of potato dough.

## J5.3 Pulses

Leaf axis: the species group. Whole or split (dal), dried or tinned, and cooked plain in water or brine are attributes: a dried and a tinned pulse of one species are one kind. Heirloom varieties are named forms.

### J5.3.1 Beans
- J5.3.1.01 Red kidney beans (rajma): the dark red, kidney-shaped Phaseolus bean.
- J5.3.1.02 Small red beans: small red Phaseolus beans.
- J5.3.1.03 Lima beans: flat, pale lima (butter) beans.
- J5.3.1.04 Mung beans: small green mung beans, whole or split.
- J5.3.1.05 Black gram (urad): black gram beans, whole or split.

### J5.3.2 Lentils
- J5.3.2.01 Lentils (masoor): lentils of any colour, whole or split.

### J5.3.3 Peas
No kinds decided.

### J5.3.4 Chickpeas & other pulses
- J5.3.4.01 Chickpeas: kabuli or desi chickpeas, dried or tinned.
- J5.3.4.02 Pigeon peas (toor, arhar): pigeon peas, whole or split as dal.

## J5.4 Nuts & seeds

Leaf axis: the plant group of the nut or seed. Form (in shell, shelled, blanched, flaked, ground), roasting and salting are attributes, so ground almonds are almonds. Every nut, chestnut and coconut is here (K-54).

### J5.4.1 Tree nuts
- J5.4.1.01 Almonds: almonds in any form.
- J5.4.1.02 Walnuts: walnuts in any form.
- J5.4.1.03 Pecans: pecans in any form.
- J5.4.1.04 Hazelnuts (filberts): hazelnuts in any form.
- J5.4.1.05 Cashews: cashew nuts in any form.
- J5.4.1.06 Chestnuts: chestnuts, fresh, dried, roasted or peeled. †

### J5.4.2 Coconut
- J5.4.2.01 Desiccated coconut: dried shredded or grated coconut flesh. †
- J5.4.2.02 Coconut milk and cream: the pressed milk or cream of coconut flesh sold in a tin or carton for cooking; a coconut drink is J3. †

### J5.4.3 Peanuts
- J5.4.3.01 Peanuts: peanuts in any form; the Virginia, Runner or Spanish type is an attribute.

### J5.4.4 Seeds
Kinds to look for (no id, R-96 c): sesame, sunflower, pumpkin and chia seeds †.
- J5.4.4.01 Hemp seeds: shelled or whole hemp seeds sold as food. †

### Mixed (leaf 0)
- J5.4.0.01 Mixed nuts: a mix of several nuts in which no one nut makes up half or more of the weight (K-46).

## J5.5 Oils, fats & vinegars

Leaf axis: the kind of product: plant oil, solid fat, vinegar or cooking liquid.

### J5.5.1 Plant oils
The legal category (extra virgin, virgin, refined, pomace; EU 2022/2104 and IOC) is an attribute.
- J5.5.1.01 Olive oil: oil pressed from olives, all legal categories together.
- J5.5.1.02 Sesame (gingelly) oil: oil pressed from sesame seed.
- J5.5.1.03 Mustard oil: oil pressed from mustard seed.
- J5.5.1.04 Rapeseed oil: oil pressed from rapeseed.
- J5.5.1.05 Sunflower oil: oil pressed from sunflower seed.

### J5.5.2 Animal & solid cooking fats
- J5.5.2.01 Lard and dripping: rendered pork or beef fat. †
- J5.5.2.02 Margarine and plant-only fat spreads: spreadable fat made from plant oils and water, with no butter (K-53).

### J5.5.3 Vinegars & cooking liquids
Age class is an attribute; a protected name binding one kind is a named form.
- J5.5.3.01 Wine vinegar: vinegar made from wine.
- J5.5.3.02 Balsamic vinegar: vinegar of cooked grape must, alone or with wine vinegar, including the protected Modena types.
- J5.5.3.03 Rice vinegar: vinegar made from rice.
- J5.5.3.04 Malt vinegar: vinegar made from malted barley.
- J5.5.3.05 Cider vinegar: vinegar made from apple cider.
- J5.5.3.06 Mirin: sweet rice seasoning sold for cooking, hon-mirin and mirin-style seasoning. †
- J5.5.3.07 Cooking wine: wine made or sold for cooking. †
- J5.5.3.08 Cooking sake: sake made or sold for cooking. †

## J5.6 Spices, herbs & salt

Leaf axis: the form of the seasoning: single spice, dried herb, blend, salt.

### J5.6.1 Single spices
A dried chilli, whole, flaked or ground, sold to season food is here. Origin and species variants are named forms; ISO category and cut are attributes.
- J5.6.1.01 Saffron: dried stigmas of the saffron crocus.
- J5.6.1.02 Cinnamon: dried cinnamon or cassia bark, whole or ground.
- J5.6.1.03 Dried chilli and paprika: dried chillies and paprika, whole, flaked or ground.
- J5.6.1.04 Cumin (jeera): cumin seed, whole or ground.

### J5.6.2 Dried herbs
No kinds decided.

### J5.6.3 Spice blends & seasoning mixes
A blend sold under a blend name is a kind of its own.
- J5.6.3.01 Garam masala: the North Indian ground spice blend.

### J5.6.4 Salt
Brands are maker-bound named forms.
- J5.6.4.01 Table salt: fine, free-flowing salt, iodised or not.
- J5.6.4.02 Kosher salt: coarse, light-crystal cooking salt.
- J5.6.4.03 Flake salt: thin hollow or pyramid flakes used to finish dishes.
- J5.6.4.04 Fleur de sel: the fine crust of sea salt skimmed by hand from the pans.

## J5.7 Sugars, honey & syrups

Leaf axis: the sweetener type.

### J5.7.1 Sugars
- J5.7.1.01 Demerara sugar: large-crystal pale-brown cane sugar.
- J5.7.1.02 Muscovado sugar: moist dark unrefined cane sugar.
- J5.7.1.03 Whole cane sugar blocks (jaggery, piloncillo): unrefined cane juice boiled down and set in blocks or cones.

### J5.7.2 Honey
Origin, creamed or comb form and the manuka grades (UMF, MGO, NPA) are attributes.
- J5.7.2.01 Manuka honey: honey from manuka flowers.
- J5.7.2.02 Acacia honey: honey from acacia flowers.
- J5.7.2.03 Clover honey: honey from clover flowers.
- J5.7.2.04 Buckwheat honey: honey from buckwheat flowers.

### J5.7.3 Syrups & molasses
No kinds decided.

## J5.8 Spreads, pastes & dips

Leaf axis: the kind of spread. A spread, paste or dip eaten with other food is here whatever it is made from, except spreads and fresh cheeses made from milk (J3) (K-44).

### J5.8.1 Sweet spreads
- J5.8.1.01 Jam and fruit spreads: fruit cooked with sugar to a spread.
- J5.8.1.02 Hazelnut-chocolate spread: a sweet spread of hazelnuts with chocolate or cocoa.

### J5.8.2 Nut & seed butters
Kinds to look for (no id, R-96 c): tahini.
- J5.8.2.01 Peanut butter: ground roasted peanuts as a spread.

### J5.8.3 Savoury spreads, pastes & dips
Kinds to look for (no id, R-96 c): hummus, taramasalata, tzatziki, rillettes in a jar †, yeast-extract spread.
- J5.8.3.01 Pesto: a paste of basil or other herbs with oil and nuts or cheese, jarred or chilled.

## J5.9 Sauces, condiments & stocks

Leaf axis: the product type as standards and shelves class it, an ordered key, first yes: (1) a soy sauce: Soy sauces; (2) another seasoning made by fermenting beans, grain or fish: Other fermented seasonings; (3) a stock or bouillon in any form: Stocks & bouillon; (4) a paste used as a cooking ingredient: Cooking & seasoning pastes; (5) a sauce to cook with or pour over pasta: Cooking & pasta sauces; (6) otherwise: Table sauces, condiments & dressings.

### J5.9.1 Soy sauces
The five JAS types are kinds (J-13); the JAS grade (Tokkyu, Jokyu, Hyojun; Tokusen, Cho-tokusen) is an attribute with JAS 1703; the brewery is a maker.
- J5.9.1.01 Koikuchi soy sauce: the common dark Japanese soy sauce of soybeans and wheat.
- J5.9.1.02 Usukuchi soy sauce: light-coloured, saltier Japanese soy sauce.
- J5.9.1.03 Tamari soy sauce: soy sauce brewed mainly from soybeans, with little or no wheat.
- J5.9.1.04 Saishikomi soy sauce: twice-brewed soy sauce, made with soy sauce in place of brine.
- J5.9.1.05 Shiro soy sauce: very pale soy sauce made mostly from wheat.

### J5.9.2 Other fermented seasonings
- J5.9.2.01 Fermented soybean paste: a fermented paste of soybeans, with or without grain, used to season. †
- J5.9.2.02 Fermented chilli paste (gochujang): a fermented paste of chilli, glutinous rice and soybeans used to season. †
- J5.9.2.03 Broad-bean chilli paste (doubanjiang): a fermented paste of broad beans and chilli used to season. †
- J5.9.2.04 Fish sauce: the liquid drawn from salted, fermented fish. †

### J5.9.3 Cooking & pasta sauces
- J5.9.3.01 Tomato pasta sauces: tomato-based sauces for pasta, in jars, with or without meat.
- J5.9.3.02 Oyster sauce and hoisin sauce: thick dark Chinese cooking sauces of oyster extract or of fermented soybeans.

### J5.9.4 Table sauces, condiments & dressings
A cooked relish or chutney of several ingredients is here.
- J5.9.4.01 Ketchup: thick sweet-sour tomato table sauce.
- J5.9.4.02 Mayonnaise: an emulsion of egg yolk and oil.
- J5.9.4.03 Mustard: prepared mustard, a paste of mustard seed.
- J5.9.4.04 Horseradish: prepared grated horseradish.
- J5.9.4.05 Salad dressing: pourable dressings for salad.
- J5.9.4.06 Chilli oil: oil infused with chilli, with or without solids.
- J5.9.4.07 Bitters sold as a flavouring by the dash: concentrated bitter flavouring used a few drops at a time; a bitter liqueur or drinking bitters sold by the glass is J7. †

### J5.9.5 Stocks & bouillon
- J5.9.5.01 Stock cubes and bouillon: cubes, powders, pastes and liquids for making stock, from any source.

### J5.9.6 Cooking & seasoning pastes
No kinds decided. Kinds to look for (no id, R-96 c): curry paste †.

## J5.10 Preserved fruit & vegetables

Fruit, vegetables, edible fungi and seaweed (as J4 defines produce) kept by a process. Leaf axis: the preserving process; the kind is the crop or product as preserved. A cultivar or a designation binding one kind is a named form; the pack medium is an attribute.

### J5.10.1 Dried
A dried vegetable is one sold to rehydrate and cook as a vegetable. Kinds to look for (no id, R-96 c): dried fruit kinds such as raisins and dried apricots †.
- J5.10.1.01 Dried mushrooms: dried edible fungi. †
- J5.10.1.02 Dried seaweed: dried edible seaweed (cross-linked from J4 G-J4-26). †

### J5.10.2 Tinned & jarred
Heat-processed in the pack, in water, brine, juice or syrup, or concentrated; tomato kinds first. Kinds to look for (no id, R-96 c): fruit in syrup †.
- J5.10.2.01 Whole peeled tomatoes: whole peeled tomatoes, heat-processed in the pack.
- J5.10.2.02 Chopped tomatoes: chopped tomatoes, heat-processed in the pack. †
- J5.10.2.03 Passata: sieved raw tomato pulp, heat-processed in the pack. †
- J5.10.2.04 Tomato purée and paste: concentrated tomato purée or paste. †
- J5.10.2.05 Tinned sweetcorn: sweetcorn kernels, heat-processed in the pack.

### J5.10.3 Pickled in vinegar
- J5.10.3.01 Gherkins (cornichons): small cucumbers pickled in vinegar.
- J5.10.3.02 Pickled peppers: peppers pickled in vinegar.

### J5.10.4 Salted, brined & fermented
- J5.10.4.01 Table olives: olives cured in brine, salt or by another cure.
- J5.10.4.02 Sauerkraut: salt-fermented shredded cabbage. †
- J5.10.4.03 Kimchi: salt- and chilli-fermented vegetables, usually napa cabbage. †

### J5.10.5 Preserved in oil & spices
No kinds decided. Kinds to look for (no id, R-96 c): Indian oil pickles (achar) †.

## J5.11 Baking ingredients

Leaf axis: the function in the bake or the brew. Holds only products no other family holds; flour, sugar and nuts stay in their own families.

### J5.11.1 Baking & fermenting aids
Home-brewing and winemaking equipment is B5 (K-58).
- J5.11.1.01 Baking powder: chemical raising agent.
- J5.11.1.02 Dried yeast: dried baker's yeast.
- J5.11.1.03 Malt extract: concentrated malt wort, liquid or dry, for brewing or baking. †
- J5.11.1.04 Hops: hops sold for brewing. †
- J5.11.1.05 Brewing yeast: yeast for home brewing and winemaking. †

### J5.11.2 Flavourings, extracts & colourings
- J5.11.2.01 Vanilla and baking flavourings: vanilla extract, paste and essences and other flavourings for baking.

### J5.11.3 Setting agents, starches & thickeners
- J5.11.3.01 Gelatine and setting agents: gelatine, agar and similar agents that set a liquid.

### J5.11.4 Baking chocolate, doughs & mixes
Cocoa powder, cocoa butter and cocoa paste are J6 (K-50); sprinkles are OUT (K-59).
- J5.11.4.01 Baking chocolate and couverture: chocolate, chips included, sold to melt, temper or bake with. †
- J5.11.4.02 Unbaked pastry: unbaked dough or pastry sheets and blocks. †
- J5.11.4.03 Cake and baking mixes: dry mixes to which only liquid, egg or fat is added before baking. †

## J5.12 Tofu, tempeh & meat alternatives

Leaf axis: how the protein food is made, an ordered key, first yes: (1) texturised or formed to imitate a meat product: Plant-based meat analogues; (2) washed from wheat dough: Seitan & wheat gluten; (3) a whole bean fermented: Tempeh & fermented beans; (4) set as a curd: Tofu & bean-curd products. Firmness and format are attributes.

### J5.12.1 Tofu & bean-curd products
- J5.12.1.01 Tofu: soybean curd set from soy milk.
- J5.12.1.02 Fermented bean curd: tofu cubes fermented in brine.

### J5.12.2 Tempeh & fermented beans
- J5.12.2.01 Tempeh: whole beans cultured into a firm cake.
- J5.12.2.02 Natto: whole soybeans fermented to a sticky mass. †

### J5.12.3 Seitan & wheat gluten
- J5.12.3.01 Seitan: wheat gluten prepared as a meat-like protein food.

### J5.12.4 Plant-based meat analogues
- J5.12.4.01 Plant-based burgers and sausages: formed plant-protein patties, sausages and similar shapes imitating meat, seasoned but not coated, filled or sauced.

## Precedence inside J5

1. A fruit, vegetable, edible fungus or seaweed sold dried, tinned, jarred, pickled, fermented or in oil is J5.10, in the leaf of its preserving process, with the crop as the kind. Except: pulses are J5.3 in any state (dried or tinned is a pack attribute; a tinned chickpea is J5.3.4.01); nuts, seeds and coconut are J5.4 (a dried chestnut is J5.4.1.06, desiccated coconut J5.4.2.01); a dried chilli or dried herb sold to season is J5.6; fruit cooked with sugar to a spread is J5.8.1.01 Jam and fruit spreads; a concentrated purée of one crop is J5.10 (tomato purée J5.10.2.04), not a J5.9 paste. (P3)
2. A dried chilli, whole, flaked or ground, sold to season food is a spice (J5.6.1.03); a dried vegetable (J5.10.1) is one sold to rehydrate and cook as a vegetable. A fermented soy or grain paste used to season (miso, doenjang J5.9.2.01; gochujang J5.9.2.02; doubanjiang J5.9.2.03) is J5.9; a fermented bean eaten as a protein body (natto J5.12.2.02, tempeh J5.12.2.01) is J5.12; a vegetable kept by fermenting (kimchi J5.10.4.03, sauerkraut J5.10.4.02) is J5.10. Pickled peppers are J5.10.3.02, dried chillies J5.6.1.03. (P9)
3. A mix of kinds from one category is filed under the kind that makes up half or more of its weight. Otherwise it is a final kind "mixed <class>" at the end of the lowest level that holds all its parts (Mixed nuts J5.4.0.01). A spice blend sold under a blend name (garam masala J5.6.3.01) is a kind of its own. Trail mix follows this sentence; roasted and salted nuts are J5.4 with roast and salt as attributes; nuts coated in chocolate, sugar or batter are OUT. A mix across categories is filed by its item of greatest value. (P10, K-46, K-59)
4. A preserve of one main crop, pickled, brined, fermented or in oil, is J5.10; a cooked relish or chutney of several ingredients is J5.9.4 Table sauces, condiments & dressings. (P12)
5. A spread, paste or dip eaten with other food (rillettes, liver pâté in a jar or tub, potted shrimp, taramasalata, hummus, guacamole, tzatziki, pesto) is J5.8.3, whatever it is made from; pesto is J5.8.3.01, not a J5.9 sauce. Spreads and fresh cheeses made from milk are J3; a pâté or terrine sold as a loaf or slice to be cut is J1 or J2. (P8, K-44)
6. A stock cube, bouillon paste, fish sauce, shrimp paste, oyster sauce or XO-type sauce is J5.9 (stock J5.9.5.01, fish sauce J5.9.2.04, oyster sauce J5.9.3.02), whatever it is made from; fish or meat sold as itself is J2 or J1. (P1, P4)
7. Margarine and plant-only fat spreads sold for cooking or spreading are J5.5.2.02; a spread containing butter is J3. (P2, K-53)
8. Mirin, cooking wine, cooking sake and bitters sold as a flavouring are J5 even when they contain alcohol: J5.5.3.06, J5.5.3.07 and J5.5.3.08, and bitters by the dash J5.9.4.07; extracts are J5.11.2.01. A wine, sake, spirit or bitter liqueur sold to drink is J7. (P5, P5b, R-17)
9. Baking chocolate, couverture and chocolate chips are J5.11.4.01; cocoa powder, cocoa butter and cocoa paste are J6. (P6, K-50)
10. A grocery is filed in J5 once, by what it is when bought. A mix to which only liquid is added is J5.11.4.03 if the mix is for baking, and a prepared meal (OUT) if it is eaten as a meal. Malt extract, hops and brewing yeast are J5.11.1.03 to J5.11.1.05; their equipment is B5. (P7, K-58, K-59)
11. A sausage, patty, ball or other shaped product made mainly of a plant protein, seasoned but not coated, filled or sauced, is J5.12.4.01; coated (breaded or battered), filled (in pastry, as a dumpling or as a stuffed dish) or sauced products are prepared (OUT). (P11, K-45)
12. A dry noodle brick, with or without a flavour sachet, is J5.2 (ramen J5.2.3.03, attribute `instant`); a noodle cup or pot is a ready meal (OUT). Rice and pulses cooked plain in water or brine are J5, on their kinds with a pack attribute; cooked in a seasoned sauce (baked beans, seasoned microwave rice) they are OUT. (K-24, J5-O1)
13. Ground almonds and other nut flours are their nut kind in J5.4 with the form `ground`; J5.1.4 holds grain and pulse flours only.
