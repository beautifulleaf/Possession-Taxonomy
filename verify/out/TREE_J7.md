# J7 Wine, Beer & Spirits: decided tree

Category: J7 Wine, Beer & Spirits (domain J, Groceries). Membership test: wine, beer, cider, sake, spirits and other alcoholic drinks in sealed containers (bottle, can, keg, cask, box), as the product is bought. Not here: wines, spirits and bitters made for cooking or flavouring (mirin, cooking wine, bitters sold by the dash, extracts: J5), home-brewing and winemaking ingredients (J5) and equipment (B5), alcohol-free versions of beer, wine and spirits and other prepared drinks (Culinary), drinks bought but not yet delivered (en primeur, casks held in bond: OUT), cannabis-, kratom- or areca-bearing drinks (B9), glassware, decanters, barware and wine fridges (B5), and cellar racks (B1). Structure (Candidate A, memo section 10): sub-family by the drink's base material and how it is made (fermented, distilled, or compounded from a distillate), then leaf by one axis per sub-family (wine class by a first-yes key; beer style family; base fruit, honey or sap; legal class or base spirit), with no leaf in Sake and other rice wines, Liqueurs and flavoured spirits, and Mixed alcoholic drinks; then kind at grape or blend type (wine), BJCP style (beer, cider, mead), composition class (sake) and legal or production type (spirits, liqueurs). Each object gets one kind. Seventeen wine and spirit designations are kinds under the written exception of CV-40 and JC1 (Champagne, Cava, Prosecco, Crémant, Sauternes, Tokaj, Port, Sherry, Madeira, Bordeaux red blend, which is also a blend type, Cognac, Armagnac, Calvados, Pisco, Cachaça, Tequila, Mezcal); every other appellation (Barolo, Burgundy grands and premiers crus, Alsace grands crus) is a non-maker named form carrying `designation_id`, or a tag, and a multi-kind designation (Scotch) is a tag. Kinds with a place word in a BJCP style name (Czech and Munich lagers, English, French and Spanish cider) are not designations and keep their level as provisional until attested (CV-27, R-19). Country, region and appellation, vintage (a variant), bottler edition (a variant), age statement, ABV, sake designation and polishing ratio, dosage, sweetness, carbonation, bottle size, container, closure, organic certification, `cru_class`, `chill_filtered`, `added_colour`, `single_cask`, `cask_strength`, `cask_type` and the spirits `flavour_profile` are attributes, tags or variants, never kinds. A kind marked † is named by the memo without a fetched page and needs one before it enters the data; the Aromatised wine leaf (J7.1.8) and the leaves holding only † kinds are provisional with them. A final "mixed <class>" kind (K-46) is stored with leaf = null as leaf 0 and enters when one fetched page attests a mixed pack. Display groups (navigation proposal, display only): G-J7-1 Wine (J7.1); G-J7-2 Beer (J7.2); G-J7-3 Cider, perry and mead (J7.3); G-J7-4 Spirits and liqueurs (J7.5 and J7.6); G-J7-5 Sake and rice wines (J7.4); G-J7-6 Premix and ready-to-drink (J7.7); level 2 groups G-J7-10 to G-J7-26 follow the leaves (aromatised wine shown with fortified, J7.5.7 to J7.5.9 under Other spirits).

Ids (R-58): J7.n is a sub-family and J7.n.m a leaf; a kind is J7.n.m.kk, or J7.n.kk where a sub-family has no leaf.

## J7.1 Wine (grape)

Leaf axis: wine class, by the first-yes key (aromatised; fortified; sweet; sparkling; orange; rosé; otherwise still red or still white by colour). Inside still red and still white the kind is the grape or blend type; display order is single grapes first, then blends, each light to full body (memo section 8).

### J7.1.1 Still red wine
- J7.1.1.01 Pinot Noir: still red wine made mainly from the Pinot Noir grape.
- J7.1.1.02 Cabernet Sauvignon: still red wine made mainly from the Cabernet Sauvignon grape.
- J7.1.1.03 Bordeaux red blend: still red wine of the Bordeaux blend of grapes (Cabernet Sauvignon, Merlot, Cabernet Franc and their partners), a blend type and a CV-40 designation kind.
- J7.1.1.04 Sangiovese: still red wine made mainly from the Sangiovese grape.
- J7.1.1.05 Nebbiolo: still red wine made mainly from the Nebbiolo grape.
- J7.1.1.06 Syrah/Shiraz: still red wine made mainly from the Syrah grape, under either name.

### J7.1.2 Still white wine
- J7.1.2.01 Chardonnay: still white wine made mainly from the Chardonnay grape.
- J7.1.2.02 Sauvignon Blanc: still white wine made mainly from the Sauvignon Blanc grape.
- J7.1.2.03 Pinot Gris/Grigio: still white wine made mainly from the Pinot Gris grape, under either name.

### J7.1.3 Rosé wine
- J7.1.3.01 Rosé wine: still pink wine of any grape, made with brief skin contact or by the methods the rosé class allows.

### J7.1.4 Orange wine
- J7.1.4.01 Orange wine: still white-grape wine made with long skin contact, as a red wine is.

### J7.1.5 Sparkling wine
- J7.1.5.01 Champagne: sparkling wine of the Champagne designation, a CV-40 designation kind.
- J7.1.5.02 Cava: sparkling wine of the Cava designation, made by the traditional method, a CV-40 designation kind.
- J7.1.5.03 Prosecco: sparkling wine of the Prosecco designation, a CV-40 designation kind.
- J7.1.5.04 Crémant: traditional-method sparkling wine of a French Crémant designation, a CV-40 designation kind.

### J7.1.6 Sweet wine
- J7.1.6.01 Late-harvest wine: sweet wine made from grapes left on the vine past normal ripeness.
- J7.1.6.02 Sauternes: sweet white wine of the Sauternes designation, a CV-40 designation kind.
- J7.1.6.03 Tokaj: sweet wine of the Tokaj designation, a CV-40 designation kind.

### J7.1.7 Fortified wine
- J7.1.7.01 Port: wine of the Port designation, fortified with grape spirit, a CV-40 designation kind.
- J7.1.7.02 Sherry: wine of the Sherry designation, fortified, a CV-40 designation kind.
- J7.1.7.03 Madeira: wine of the Madeira designation, fortified, a CV-40 designation kind.

### J7.1.8 Aromatised wine
Leaf provisional until its kinds are attested (memo section 3, 10).
- J7.1.8.01 Vermouth: wine flavoured with wormwood and other botanicals and fortified, sold to drink. †
- J7.1.8.02 Retsina: wine flavoured with pine resin. †
- J7.1.8.03 Quinquina: wine aromatised with cinchona bark. †

### Mixed (leaf 0)
- J7.1.0.01 Mixed wine: mixed case or pack of wines of several kinds, none of which makes up half or more of its volume or weight. †

## J7.2 Beer

Leaf axis: style family (BJCP style family tags). Kinds are BJCP styles, shown in BJCP category and letter order; further BJCP 2021 styles enter as kinds on a fetched page (DPH, section 14).

### J7.2.1 Pale lager family
- J7.2.1.01 American Light Lager: very pale, highly carbonated, light-bodied lager of low strength (BJCP 1A).
- J7.2.1.02 International Pale Lager: pale, clean, well-attenuated lager of standard strength (BJCP 2A).
- J7.2.1.03 Czech Premium Pale Lager: golden Czech lager of ležák strength with a soft malt and Saaz hop character (BJCP 3B).
- J7.2.1.04 Munich Helles: pale, malt-forward Bavarian lager (BJCP 4A).

### J7.2.2 Dark lager family
- J7.2.2.01 Czech Dark Lager: dark Czech lager with roasted malt character (BJCP 3D).

### J7.2.3 Wheat beer family
- J7.2.3.01 American Wheat Beer: pale beer brewed with a large share of wheat and a clean American yeast (BJCP 1D).

### J7.2.4 Traditional grain, root and fruit beers
Leaf provisional until its kinds are attested (memo section 3, 10; Culinary DR-E2).
- J7.2.4.01 Sorghum beer: traditional beer brewed from sorghum. †
- J7.2.4.02 Millet beer: traditional beer brewed from millet. †
- J7.2.4.03 Maize beer: traditional beer brewed from maize. †
- J7.2.4.04 Root beer (fermented): alcoholic beer fermented from roots and their extracts; an alcohol-free root beer is not in J7. †
- J7.2.4.05 Banana beer: traditional beer fermented from bananas, often with grain. †

### Mixed (leaf 0)
- J7.2.0.01 Mixed beer: mixed case or pack of beers of several kinds, none of which makes up half or more of its volume or weight. †

## J7.3 Cider, perry, mead and other fruit and honey ferments

Leaf axis: base fruit, honey or sap. Kinds are BJCP styles where BJCP has them, in BJCP order.

### J7.3.1 Apple cider
- J7.3.1.01 Common cider: cider of culinary or table apples, of moderate strength (BJCP C1A).
- J7.3.1.02 English cider: cider in the English style, from bittersweet and bittersharp apples (BJCP C1C).
- J7.3.1.03 French cider [cidre]: cider in the French style, often keeved, sweet and low in alcohol (BJCP C1D).
- J7.3.1.04 Spanish cider [sidra]: cider in the Spanish and Basque style, tart and still or lightly sparkling (BJCP C1E).
- J7.3.1.05 Strong cider: apple cider of higher strength than the traditional styles (BJCP C2).

### J7.3.2 Perry
- J7.3.2.01 Perry: fermented drink of pear juice (BJCP C4).

### J7.3.3 Mead
- J7.3.3.01 Traditional mead: mead fermented from honey and water with no added fruit or spice (BJCP M1).

### J7.3.4 Fruit wine
Leaf provisional until its kind is attested.
- J7.3.4.01 Fruit wine: wine fermented from a fruit other than the grape, apple or pear (plum, berry and others; the fruit is an attribute). †

### J7.3.5 Palm and sap wine
Leaf provisional until its kind is attested.
- J7.3.5.01 Palm or sap wine: wine fermented from palm or tree sap. †

## J7.4 Sake and other rice wines (no leaf)

Kinds by composition (J-16, CV-42); the eight NTA names (ginjo, daiginjo, junmai and the rest) are values of the attribute `designation`, and polishing ratio, nama, genshu and taru are attributes. Canonical form first: junmai sake, then sake with brewer's alcohol.
- J7.4.01 Junmai sake: sake made only from rice, koji and water, with no brewer's alcohol added.
- J7.4.02 Sake with brewer's alcohol: sake to which brewer's alcohol is added within the legal limit (the ginjo, daiginjo and honjozo types).
- J7.4.03 Cloudy sake [nigori]: sake coarsely filtered so that rice solids stay in it. †
- J7.4.04 Non-designated sake [futsūshu]: ordinary sake outside the eight special designations. †
- J7.4.05 Makgeolli: Korean milky, lightly sparkling rice wine. †
- J7.4.06 Cheongju: Korean clear refined rice wine. †
- J7.4.07 Huangjiu and other amber rice wines: Chinese amber or yellow grain wine and its relatives. †
- J7.4.08 Infused rice wine: rice wine infused with fruit, herbs or other flavourings. †

## J7.5 Spirits

Leaf axis: legal class or base spirit. Kinds are production or legal types; country is a tag, the distillery and the bottler are makers, and age is an attribute. Display order inside Whisky follows the Scotch categories (single malt, single grain, blended malt, blended grain, blended), then pot still, bourbon and rye; inside Brandy the US type list (memo section 8).

### J7.5.1 Whisky
- J7.5.1.01 Single malt whisky: malt whisky distilled at one distillery.
- J7.5.1.02 Single grain whisky: grain whisky distilled at one distillery.
- J7.5.1.03 Blended malt whisky: blend of single malt whiskies from more than one distillery.
- J7.5.1.04 Blended whisky: blend of one or more malt whiskies with one or more grain whiskies.
- J7.5.1.05 Pot still whisky: whiskey of malted and unmalted barley distilled in pot stills.
- J7.5.1.06 Bourbon: American whiskey of mainly corn, aged in new charred oak containers.
- J7.5.1.07 Rye whiskey: whiskey distilled mainly from rye.
- J7.5.1.08 Blended grain whisky: blend of single grain whiskies from more than one distillery.
- J7.5.1.09 Corn whisky: whiskey distilled mainly from corn, with no new charred oak ageing required.

### J7.5.2 Brandy
- J7.5.2.01 Cognac: grape brandy of the Cognac designation, a CV-40 designation kind.
- J7.5.2.02 Armagnac: grape brandy of the Armagnac designation, a CV-40 designation kind.
- J7.5.2.03 Calvados: apple and pear brandy of the Calvados designation, a CV-40 designation kind.
- J7.5.2.04 Pisco: grape brandy of the Pisco designation, a CV-40 designation kind.
- J7.5.2.05 Grappa: brandy distilled from grape pomace.
- J7.5.2.06 Fruit brandy [eau de vie]: clear brandy distilled from fermented fruit other than grape wine.

### J7.5.3 Rum
- J7.5.3.01 Rum from cane juice [rhum agricole]: rum distilled from fresh sugar-cane juice.
- J7.5.3.02 Cachaça: Brazilian sugar-cane spirit of the Cachaça designation, a CV-40 designation kind.

### J7.5.4 Gin
- J7.5.4.01 London dry gin: gin distilled with juniper and natural botanicals, with nothing but a little sweetening added after distillation.

### J7.5.5 Agave spirits
- J7.5.5.01 Tequila: agave spirit of the Tequila designation, a CV-40 designation kind.
- J7.5.5.02 Mezcal: agave spirit of the Mezcal designation, a CV-40 designation kind.

### J7.5.6 Vodka
- J7.5.6.01 Vodka: neutral spirit without distinctive character, aroma or taste.

### J7.5.7 East Asian grain and rice spirits
Leaf provisional until its kinds are attested.
- J7.5.7.01 Baijiu: Chinese spirit distilled from fermented grain, usually sorghum. †
- J7.5.7.02 Shochu: Japanese spirit distilled from rice, barley, sweet potato or other starch. †
- J7.5.7.03 Soju: Korean spirit distilled from rice or other starch. †
- J7.5.7.04 Awamori: Okinawan spirit distilled from long-grain rice with black koji. †

### J7.5.8 Palm spirits
Leaf provisional until its kind is attested.
- J7.5.8.01 Arrack and palm spirit: spirit distilled from palm sap and related bases. †

### J7.5.9 Anise and other botanical spirits
Leaf provisional until its kinds are attested.
- J7.5.9.01 Anise spirit: spirit flavoured mainly with anise (ouzo, pastis, absinthe and the like). †
- J7.5.9.02 Genever: juniper-flavoured spirit made with malt wine. †
- J7.5.9.03 Aquavit: spirit flavoured mainly with caraway or dill. †

### Mixed (leaf 0)
- J7.5.0.01 Mixed spirits: mixed pack of spirits of several kinds, none of which makes up half or more of its volume or weight. †

## J7.6 Liqueurs and flavoured spirits (no leaf)

A spirit compounded with a flavouring; if the sub-family grows past about 12 kinds its leaf axis is the flavouring. The brand is a named form.
- J7.6.01 Triple sec and curaçao: orange-peel liqueur.
- J7.6.02 Amaretto: almond-flavoured liqueur.
- J7.6.03 Sloe gin: liqueur of gin flavoured with sloes.
- J7.6.04 Cream liqueur: liqueur made with cream.
- J7.6.05 Fruit liqueur: liqueur flavoured with fruit.
- J7.6.06 Herb and spice liqueur: liqueur flavoured with herbs and spices.
- J7.6.07 Bitter liqueur and amaro: bitter liqueur or drinking bitters sold to drink by the glass (amaro, Fernet and similar). †

## J7.7 Mixed alcoholic drinks, ready-to-drink (no leaf)

Sealed ready-to-drink drinks of a spirit, wine or malt base mixed with a flavouring or mixer (K-24).
- J7.7.01 Ready-to-drink mixed alcoholic drink [blanddryck]: sealed mix of a spirit or wine with a flavouring that no other J7.7 kind covers.
- J7.7.02 Hard seltzer: sealed carbonated water with alcohol and flavouring. †
- J7.7.03 Ready-to-drink cocktail: sealed premixed cocktail, such as canned gin and tonic. †
- J7.7.04 Canned spritzer: sealed mix of wine with soda water or a mixer. †

## Precedence inside J7

- Sub-family by base and process: a drink of grape wine is J7.1; a beer of malted or other grain or root is J7.2; a ferment of apple, pear, other fruit, honey or sap is J7.3; sake and other rice or grain wines are J7.4; an unsweetened distilled spirit is J7.5; a spirit compounded with a flavouring is J7.6; a sealed ready-to-drink mix is J7.7. A product that meets the standard of more than one spirit class goes by its legal class and type.
- Wine class by the first-yes key: (0) aromatised with botanicals and sold to drink (vermouth, retsina, quinquina) is J7.1.8; (1) fortified with spirit is J7.1.7; (2) sweet by botrytis, ice, dried grapes or late harvest is J7.1.6; (3) sparkling is J7.1.5; (4) a white made with long skin contact is J7.1.4; (5) pink is J7.1.3; (6) otherwise still red (J7.1.1) or still white (J7.1.2) by colour. A sparkling rosé is sparkling, a vin doux naturel is fortified, and Lambrusco is sparkling. Dosage, sweetness and body are attributes.
- Still wine kinds are grape or blend types; an appellation is a region tag or a non-maker named form carrying `designation_id` under its grape kind (Barolo under Nebbiolo J7.1.1.05; a Burgundy grand or premier cru under Pinot Noir J7.1.1.01 or Chardonnay J7.1.2.01, with `cru_class`). Only the seventeen CV-40 designations are kinds (J7.1.1.03, J7.1.5.01 to J7.1.5.04, J7.1.6.02, J7.1.6.03, J7.1.7.01 to J7.1.7.03, J7.5.2.01 to J7.5.2.04, J7.5.3.02, J7.5.5.01, J7.5.5.02). Blanc de Blancs, Blanc de Noirs and rosé are non-maker named forms of Champagne (J7.1.5.01). Bordeaux 1855 and Saint-Émilion classes are tier entries on the estate (maker), not kinds or named forms.
- A BJCP style name with a place word (J7.2.1.03, J7.2.1.04, J7.2.2.01, J7.3.1.02 to J7.3.1.04) is a style, not an appellation: a beer or cider brewed anywhere to that style takes the kind.
- Gin is a spirit (J7.5.4), not a liqueur, by its legal class, although some shops count it a "compound" spirit with liqueurs. Sloe gin is a liqueur (J7.6.03).
- Sake goes by composition: brewer's alcohol added is J7.4.02, otherwise J7.4.01; the NTA designation and the polishing ratio are attributes. Cloudy sake (J7.4.03) and non-designated sake (J7.4.04) are tested before the composition split.
- Whisky goes by production type; Scotch, Irish, Japanese, Canadian and American are origin tags or designation rows, never kinds. An independent bottling takes the bottler as maker and the distillery as `built_by_maker_id`.
- A bitter liqueur sold to drink by the glass, and drinking bitters, are J7.6.07; bitters sold as a flavouring by the dash are J5 (K-48, R-17).
- A sealed ready-to-drink cocktail, hard seltzer, canned gin and tonic or canned spritzer is J7.7 (K-24); the same drink mixed to order is Culinary. A mix of a spirit or wine with a flavouring that no other J7.7 kind covers is J7.7.01.
- A mixed case or pack of kinds from one sub-family is filed under the kind that makes up half or more of its weight; otherwise under the sub-family's final mixed kind (J7.1.0.01, J7.2.0.01, J7.5.0.01), stored last. A set that mixes categories is filed by its item of greatest value (a Champagne and chocolates gift set is J7.1.5.01); the box kept afterwards is B1.
- A wine, beer, cider, sake or spirit in a sealed bottle, can, keg or cask is J7 as the product bought; poured, cooked with or mixed to serve, it is Culinary. A cask or bottle bought but not yet delivered (en primeur, a warehouse receipt for a cask held in bond) is OUT; once delivered it is J7 under its kind.
