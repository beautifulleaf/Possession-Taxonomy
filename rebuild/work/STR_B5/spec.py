# -*- coding: utf-8 -*-
CAT={'ax':'What does the object do in the kitchen: cook food in a vessel, cut it, prepare it by hand, cook or process it by machine, brew coffee, make tea or hot water, serve it at the table, hold or mix a drink, brew or preserve at home, or store and carry food and drink?',
'key':[
'1. Is it a pan, pot or oven tin that food is cooked in? → Cookware & bakeware',
'2. Is it a knife, a board to cut on, or something that sharpens or stores knives? → Knives & cutting',
'3. Is it a hand tool, measure, timer or cook\'s wear used to prepare food? → Kitchen tools & measuring',
'4. Is it a plug-in or freestanding machine that cooks, mixes, chills or washes? → Kitchen appliances',
'5. Does it brew, grind, roast or serve coffee? → Coffee',
'6. Does it brew or serve tea, or heat, filter or carbonate water? → Tea & kettles',
'7. Is it a plate, bowl, cup, cutlery or table piece used to serve and eat? → Tableware',
'8. Is it a drinking glass, decanter or bar tool? → Glassware & bar',
'9. Does it make beer, wine or cider at home, or ferment or preserve food? → Brewing, fermenting & preserving',
'10. Does it keep food in the cupboard or fridge, or carry food and drink out of the house? → Food storage & on-the-go',
'11. Is it a replacement part for one appliance? → Spare parts',
'<i>Precedence: a kettle is Tea & kettles even for coffee; a coffee grinder is Coffee but a pepper mill is a kitchen tool; built-in ovens and hobs belong to Home Fixtures, barbecues to Garden.</i>']}
D=[]
def dept(n,mode,t,ax,shelves,note=None):
    d={'n':n,'mode':mode,'t':t,'ax':ax,'s':shelves}
    if note: d['note']=note
    D.append(d)
dept('Cookware & bakeware','mixed',
 'Vessels that food is cooked in on the hob or in the oven: pans, pots, pressure and steam cookers, and oven tins; electric cookers → Kitchen appliances, barbecue grills → Garden.',
 'How is the food cooked in it: fried in an open pan, simmered or braised in a pot, pressured or steamed, or baked in an oven tin?',[
 ('Pans','Shallow open vessels set on a hob to fry, sear, stir-fry or griddle; deep lidded pots → Pots & casseroles.','kinds by the work the pan does: everyday frying, searing, thin batters, stir-frying, then pans for one regional dish',
  ['Frying pan','Sauté pan','Grill pan','Griddle & tawa','Crêpe pan','Wok','Karahi','Paella pan','Tamagoyaki pan']),
 ('Pots & casseroles','Deep pots that simmer or braise food in liquid on the hob or in the oven, such as saucepans, stockpots, Dutch ovens and tagines; pressure cookers → Pressure, steam & table cookers.','kinds by how the pot cooks: boiling and sauces, gentle heating over water, then slow braising in a closed pot, then sets',
  ['Saucepan','Stockpot','Double boiler','Dutch oven','Donabe','Tagine','Cookware set']),
 ('Pressure, steam & table cookers','Vessels that cook by steam or at the table: pressure cookers, steamers and fondue pots; electric versions → Kitchen appliances.',None,
  ['Pressure cooker','Food steamer','Fondue set']),
 ('Trays, dishes & baking surfaces','Open oven vessels and surfaces for roasting and baking: sheet trays, roasting pans, baking dishes, ramekins, pizza stones and cooling racks; tins that shape a batter → Tins & moulds.','kinds from open sheets and roasters to dishes, then baking surfaces and racks',
  ['Baking tray','Roasting pan','Baking dish','Ramekin','Pizza stone','Cooling rack']),
 ('Tins & moulds','Tins and dishes that shape a batter, dough or pastry as it bakes: cake, loaf, muffin, tart and pie tins.','kinds by what is baked: cakes, bread, small cakes, then pastry cases and pies',
  ['Cake tin','Loaf tin','Muffin tin','Tart tin','Pie dish'])],
 'Form is the kind; material (cast iron, carbon steel, clad, copper, enamel, clay) is a type; icons become archetypes.')
dept('Knives & cutting','mixed',
 'Kitchen knives, the boards and slicers used with them, and the tools that keep an edge; pocket and outdoor knives → C1, fighting and hunting knives → E4.',
 'Is it a knife of the Western pattern, a knife of the Japanese pattern, something to cut on or with, or something that sharpens or stores knives?',[
 ('Western kitchen knives','Knives of the European pattern, each for one job: chef\'s, paring, bread, boning and carving knives and cleavers; steak knives for the table → Tableware.','kinds by the job: all-purpose, small work, serrated, slicing and boning, chopping, then sets',
  ["Chef's knife",'Paring knife','Kitchen utility knife','Bread knife','Carving knife','Boning knife','Cleaver','Knife set']),
 ('Japanese knives','Knives of the Japanese pattern, double-bevel or single-bevel, such as gyuto, santoku, nakiri and yanagiba; the Western chef\'s knife → Western kitchen knives.','kinds by job and bevel: double-bevel all-rounders, vegetable knives, slicers, then butchery knives',
  ['Gyuto','Santoku','Bunka','Petty knife','Sujihiki','Nakiri','Usuba','Kiritsuke','Yanagiba','Honesuki','Deba']),
 ('Boards & slicing aids','Surfaces and tools that help cut food: cutting boards, mandolines and kitchen shears; knives themselves → the knife shelves.','kinds by how the cut is made: on a board, with a fixed blade, with scissors',
  ['Cutting board','Mandoline','Kitchen shears']),
 ('Edge care & storage','Stones, sharpeners, rods and holders that keep knives sharp and safe; woodworking stones → C1.','kinds in the order of use: grind a new edge, set it quickly, realign it, then store the knife',
  ['Whetstone','Knife sharpener','Honing rod','Knife storage'])],
 'Western everyday knives are tier; Japanese and forged knives are variety, browsed by tradition, smith, steel and construction.')
dept('Kitchen tools & measuring','tier',
 'Hand tools, measures and cook\'s wear used to prepare food, such as spatulas, graters, scales and aprons; knives → Knives & cutting, machines → Kitchen appliances.',
 'What job does the tool do: stir or turn, peel or grind, mix or shape, strain or open, measure, or protect the cook and wash up?',[
 ('Stirring, turning & whisking','Hand tools that move, lift or beat food in the pan or bowl: spatulas, spoons, ladles, tongs, whisks and brushes.','kinds by action: turning, stirring, serving, gripping, whisking, brushing',
  ['Spatula','Cooking spoon','Ladle','Tongs','Whisk','Pastry brush']),
 ('Peeling, grating & grinding','Hand tools that strip, shred, press or crush food: peelers, graters, presses, mashers, mortars and mills.','kinds from removing skin to shredding, pressing and grinding',
  ['Peeler','Grater','Garlic press','Citrus squeezer','Potato masher','Mortar and pestle','Pepper mill']),
 ('Mixing & shaping','Bowls and tools for combining and shaping dough and batter.',None,['Mixing bowl','Rolling pin','Tortilla press']),
 ('Straining & opening','Tools that drain, dry or open: colanders, salad spinners and can openers.',None,['Colander','Salad spinner','Can opener']),
 ('Measuring','Instruments that measure an ingredient or a dish: volume, weight, temperature and time.','kinds by what is measured: volume, weight, temperature, time',
  ['Measuring cups and spoons','Kitchen scale','Kitchen thermometer','Kitchen timer']),
 ('Aprons, gloves & dish racks','Wear and fittings that protect the cook and the washing up.',None,['Apron','Oven glove','Dish rack'])])
dept('Kitchen appliances','tier',
 'Movable electric and freestanding machines that cook, mix, chill or wash; built-in ovens, hobs and hoods → Home Fixtures, coffee machines → Coffee, electric kettles → Tea & kettles.',
 'How does the machine work on food: heated on plates or a ring, heated in a chamber, heated in a pot or bath, mixed or cut, chilled, or used to wash up?',[
 ('Plate & ring cookers','Appliances that heat food by contact or a ring: toasters, sandwich and waffle makers, table grills and portable induction hobs.','kinds from toasting to pressing, grilling and ring heating',
  ['Toaster','Sandwich and waffle maker','Electric grill and hotplate','Portable induction hob']),
 ('Oven & fryer cookers','Appliances that heat food in a chamber or hot air: microwave and countertop ovens, air fryers, deep fryers, bread makers and popcorn makers.','kinds by the heat in the chamber: microwaves, hot air and oil, then bread and popcorn',
  ['Microwave oven','Countertop oven','Air fryer','Deep fryer','Bread maker','Popcorn maker']),
 ('Pot & steam cookers','Electric pots and baths that cook food slowly or under pressure: multicookers, slow cookers, rice cookers, sous-vide circulators and steamers.','kinds from pressure and slow cooking to rice, water baths and steam',
  ['Multicooker','Slow cooker','Rice cooker','Sous-vide circulator','Electric steamer and egg cooker']),
 ('Mixers, blenders & processors','Machines that mix, blend, chop, extract or shape food, from stand mixers to single-food machines like pasta makers.','kinds by job: mixing dough and batter, blending liquids, chopping and slicing, extracting juice, then machines for one food',
  ['Stand mixer','Hand mixer','Blender','Immersion blender','Food processor','Juicer','Pasta machine','Ice cream maker','Meat grinder']),
 ('Chilling appliances','Freestanding cabinets that keep food and drink cold or frozen, and machines that make ice.','kinds by what is kept cold: everyday food, frozen food, wine, then ice',['Refrigerator','Freezer','Wine fridge','Ice maker']),
 ('Full-size cookers & dishwashers','Freestanding appliances that cook or wash at full household size; built-in versions → Home Fixtures.',None,['Freestanding cooker','Dishwasher'])],
 'Movable appliances only; built-in ovens, hobs, hoods and integrated units are in Home Fixtures & Features.')
dept('Coffee','variety',
 'Everything used to brew, grind, roast and serve coffee at home; tea and kettles → Tea & kettles, cups and mugs → Tableware.',
 'What part of coffee-making does it do: brew by hand, brew by machine, grind or roast, prepare the shot and milk, or weigh, serve and store?',[
 ('Manual brewers','Brewers worked by hand without a motor: drippers, presses, pots and siphons, each a different brewing principle.','kinds by brewing principle: drip, immersion, pressure, steam, vacuum, boiling and cycling',
  ['Pour-over dripper','Vietnamese phin','French press','Cold brew maker','AeroPress','Moka pot','Siphon brewer','Percolator','Cezve']),
 ('Coffee machines','Powered machines that brew coffee, by how much the machine does for the user.','kinds by who does the work: lever and semi-automatic, then super-automatic, capsule and drip machines',
  ['Manual lever espresso machine','Semi-automatic espresso machine','Super-automatic espresso machine','Capsule coffee machine','Drip coffee maker']),
 ('Grinders & roasters','Machines that turn green or roasted beans into the ground coffee a brewer needs.','kinds by step: roasting, then grinding by hand or motor',
  ['Home coffee roaster','Hand coffee grinder','Electric coffee grinder']),
 ('Espresso tools','Tools used around an espresso machine to dose, tamp, froth and clear the portafilter.','kinds in the order of making a shot: portafilter, distribution and tamping, milk, then knocking out',
  ['Portafilter and baskets','Tamper and distribution tool','Milk pitcher','Milk frother','Knock box']),
 ('Scales, servers & storage','Aids that weigh, serve and keep coffee whatever the brewer.',None,['Coffee scale','Coffee server','Coffee canister'])],
 'Organised by brew method; espresso and grinders are enthusiast territory with archetypes and parts.')
dept('Tea & kettles','variety',
 'Teaware by the tea tradition it serves, and the vessels that heat or treat water; cups and mugs → Tableware, coffee pots → Coffee.',
 'Which tea tradition is the piece made for, Western, Chinese or Japanese, or does it heat and treat water for any tea?',[
 ('Western tea','Teapots and fittings for the British and European way of making tea with bags or leaves.','kinds in the order of making tea: pot, keeping it warm, straining, storing leaves',
  ['Teapot','Tea cosy','Tea infuser and strainer','Tea caddy']),
 ('Chinese tea','Teaware for gongfu brewing in small pots and lidded bowls.',None,['Yixing teapot','Gaiwan','Gongfu tea tray and pitcher']),
 ('Japanese tea','Teaware for leaf tea and for the matcha ceremony, classed by kiln, maker and use.','kinds from leaf-tea ware to the matcha ceremony: pot, bowl, whisk, caddy, kettles, then water tools',
  ['Kyusu','Chawan','Matcha whisk and scoop','Japanese tea caddy','Tetsubin','Chagama','Mizusashi','Hishaku']),
 ('Water heating & treatment','Vessels and machines that heat, filter, carbonate or distil water for any drink.','kinds by job: heating, holding hot, filtering, carbonating, distilling',
  ['Kettle','Samovar','Hot water dispenser','Water filter jug','Soda maker','Water distiller'])],
 'Tea ware browsed by tradition (Yixing, Tokoname, Banko, Arita, Jingdezhen, chanoyu, British teapot); kettles are tier with a few design icons.')
dept('Tableware','variety',
 'Pieces used to serve and eat a meal, bought by house and pattern: plates, cutlery and serving pieces; glasses → Glassware & bar, table linen → Soft Furnishings.',
 'What is the piece for at the table: eating from, eating with, serving from, setting down, or buying as a set by pattern?',[
 ('Plates, bowls & cups','Pieces one diner eats and drinks from, sold singly or in a pattern.','kinds by what is held: food, soup and grain, hot drinks, then large cups',['Plate','Bowl','Cup and saucer','Mug']),
 ('Services & patterns','Matching sets, and the named patterns they are collected by house.',None,['Dinner service','China pattern']),
 ('Cutlery','Knives, forks, spoons and sticks for eating and serving; kitchen knives → Knives & cutting.','kinds from the matched set to its special pieces, then chopsticks and children\'s sets',
  ['Cutlery set','Steak knife','Serving cutlery','Chopsticks',"Children's cutlery"]),
 ('Serving dishes','Dishes that bring food to the table to be shared.','kinds from main-course dishes to trays, stands and bread',
  ['Serving platter','Serving bowl','Tureen','Gravy boat','Serving tray','Chafing dish','Cake stand','Bread basket','Cheese board']),
 ('Breakfast & condiment pieces','Small pieces for breakfast, tea and seasoning at the table.','kinds in the order of the meal: egg and toast, spread, sweetener, seasoning',['Egg cup','Toast rack','Butter dish','Sugar bowl and creamer','Cruet set']),
 ('Table accessories','Pieces that protect or set off the table.','kinds from protecting the surface to setting the place and sharing dishes',['Trivet','Hard placemat','Coaster','Napkin ring','Lazy Susan'])],
 'Organised house → pattern (archetype) → piece (type); traditions register carries kilns and silversmithing centres.')
dept('Glassware & bar','mixed',
 'Glasses to drink from, vessels to pour from, and bar tools to mix, open and chill drinks; kitchen mugs → Tableware.',
 'Is it a glass to drink from, a vessel to pour from, a tool to mix with, or a tool to open, keep or chill?',[
 ('Drinking glasses','Glasses shaped for one kind of drink.','kinds by drink: wine, sparkling wine, beer, spirits, cocktails, then general tumblers',
  ['Wine glass','Champagne glass','Beer glass','Spirits glass','Cocktail glass','Tumbler']),
 ('Decanters & jugs','Vessels that wine, spirits or water are poured into to serve.',None,['Decanter','Jug and carafe']),
 ('Mixing tools','Bar tools that measure, stir, shake and strain a cocktail.','kinds in the order of making a drink: set, measure, muddle, shake or stir, strain',
  ['Bar set','Cocktail shaker','Jigger','Muddler','Bar spoon','Mixing glass','Cocktail strainer']),
 ('Opening, keeping & chilling','Tools that open a bottle, keep wine fresh or chill a drink.','kinds by job: open the bottle, keep the wine, chill it, ice for the glass',['Corkscrew','Wine preserver','Ice bucket','Ice mould'])],
 'Everyday glasses are tier; stemware and crystal are variety by house → pattern; bar tools follow the craft-cocktail standard.')
dept('Brewing, fermenting & preserving','mixed',
 'Equipment for making beer, cider or wine at home, culturing foods, and keeping food by heat, drying, vacuum or smoke; the drinks and foods themselves are in the food categories.',
 'What is made or kept: a home brew, a cultured food, or food preserved by jar, drying, vacuum or smoke?',[
 ('Home brewing','Equipment for brewing and packaging beer, cider and wine at home.','kinds in order of the brewing stages: starter kit, brewing, cooling, fermenting, measuring, packaging, serving, then juice pressing',
  ['Homebrew kit','All-in-one brewing system','Wort chiller','Fermenter','Hydrometer and refractometer','Bottling equipment','Keg and kegerator','Fruit press']),
 ('Culturing foods','Vessels and kits for fermented vegetables, drinks, yoghurt, bread and cheese.','kinds by what is cultured: vegetables, tea and milk drinks, yoghurt, bread, cheese',
  ['Fermentation crock','Kombucha and kefir vessel','Yoghurt maker','Sourdough tools','Cheese-making kit']),
 ('Preserving','Equipment that keeps food by sealed heating, drying, vacuum, freezing or smoke.','kinds by method: sealed jars, heat processing, drying, freeze-drying, vacuum, smoke and cure',
  ['Preserving jar','Canner','Food dehydrator','Freeze dryer','Vacuum sealer','Smoker box and curing equipment'])],
 'New department: equipment only; the drinks and foods made with it live in J categories.')
dept('Food storage & on-the-go','tier',
 'Containers that keep food at home and bottles, flasks and bags that carry food and drink out; wine racks → B1.',
 'Is it kept at home to store food, or carried out to hold a drink or a meal?',[
 ('Pantry & fridge storage','Containers and wraps that keep food in the cupboard, on the worktop or in the fridge.','kinds by what is kept: leftovers, dry goods, biscuits, spices, bread, wrapped food',
  ['Food storage container','Kitchen canister','Cookie jar','Spice jar and rack','Bread bin','Reusable food wrap']),
 ('Drink carriers','Bottles, mugs and flasks that carry a drink.','kinds by how the drink is kept: bottle, cup, insulated flask, pocket flask, back-pack reservoir',
  ['Drink bottle','Travel mug','Vacuum flask','Hip flask','Hydration bladder']),
 ('Meal carriers','Boxes, bags and baskets that carry a meal and keep it cool.','kinds from the packed lunch to the picnic and the day cooler',
  ['Lunch box','Lunch bag','Cool box','Picnic basket'])])
dept('Spare parts','tier',
 'Replacement parts bought for one kitchen appliance; the appliance itself is in its own department.',
 'Which appliance is the part for?',[
 ('Spare parts','One entry for the replacement and accessory parts of kitchen appliances.',None,['Appliance spare parts'])])
DEPTS=D
