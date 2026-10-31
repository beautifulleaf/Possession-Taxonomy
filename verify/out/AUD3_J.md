# AUD3_J — cold audit of J1–J10 (2026-10-28)

All counts come from rebuild/reader/<CODE>.json and its brand and tradition registers, read on 2026-10-28. Facts from my own knowledge are marked "to verify". I checked every claimed absence with a grep across all rebuild/reader/*.json, including brands/ and traditions/. As the J note asks, food is judged on grade schemes, protected designations and brand coverage, not on archetype counts alone.

---

## J1 Meat & Poultry

**Brand mode:** mixed (beef, pork, lamb, poultry, deli, other meats); variety (game, ham and cured meats, sausages and salami).

Size: 9 departments, 157 kinds, 326 archetypes, 140 versions; 51 brands; **0 traditions** (no traditions file).

### Gaps for hobbyists
- **J1-1 No charcuterie traditions register.** The cured-meat and sausage departments (49 kinds, 195 archetypes) are tradition-shaped: Italian salumi, Spanish embutidos and ibérico, French charcuterie, German Wurst, Polish kiełbasa, Cantonese laowei. There are no tradition entries at all. **Fix:** add about 8–10 entries (group "Food & drink"), each with its centres and authenticity marks: consortium brand, PDO seal, Ibérico colour label.
- **J1-2 Thin producer register.** The brand register has 51 brands and is skewed to the US (18). These are all absent: Tyson, Perdue, Applegate, Niman Ranch, Campofrío, ElPozo, Fleury Michon, Herta, Rovagnati and La Quercia. Citterio appears only in other categories' brand registers. **Fix:** use tier coverage for fresh meat (market leaders per country) and variety coverage for cured meat (ham houses and salumifici).
- **J1-3 Missing named products:** Japanese jidori chicken (Hinai-jidori, to verify), saucisson à l'ail, Cantonese lap yuk (cured pork belly) and chicken offal (livers, gizzards as a kind). A grep found none of these as J1 items.

### Too much detail
- **J1-4 Cut lists are split into many kinds.** The beef department holds 27 cut and offal kinds with 0 archetypes. 12 of them are completely empty (no types, no models), and J1 has 18 empty kinds in total. Examples: Rump steak, Tri-tip, Flat iron, Oxtail, Beef heart and Beef kidney. Pork, by contrast, puts all its offal in one kind ("Pork stomach & offal", 5 types). **Fix:** merge the five beef offal kinds into one "Beef & veal offal" kind with types. Merge the minor steaks into "Other grilling steaks" with types. Keep ribeye, sirloin, fillet, T-bone and picanha as separate kinds.
- **J1-5 Attribute-only kinds.** "Dry-aged beef" is a kind with 4 types and nothing else, although Ageing is already a department criterion. "Meat box" and "Charcuterie & deli selection" are purchase formats. **Fix:** turn dry-ageing into a type or criterion. Group the formats on one "Boxes & selections" shelf.

### Confusing organisation
- **J1-6** "'Nduja & sobrasada" also holds Rügenwalder Teewurst, so the label hides a German spread. "Ibérico label classes (Real Decreto 4/2014)" is an archetype, but it is a grading scheme, not an object. **Fix:** rename the kind "Spreadable raw sausage". Move the label classes into the department `b` criteria.

### What it would look like (Ham, bacon & cured meats › Dry-cured hams)
```
Jamón ibérico [tradition: Iberian dehesa curing]
  Jamón de Jabugo PDO → bellota (black label) · cebo de campo
    v: Joselito Gran Reserva · Cinco Jotas · Sánchez Romero Carvajal
  Jamón de Guijuelo PDO → bellota · cebo
Prosciutto crudo [tradition: Italian salumi]
  Prosciutto di Parma PDO → 24-month · 30-month
  Prosciutto di San Daniele PDO
Smoked raw ham → Speck Alto Adige PGI · Schwarzwälder Schinken PGI
```
Priority: medium
Fix size: medium

---

## J2 Fish & Seafood

**Brand mode:** mixed in every department, except Fish cakes, fingers & surimi (tier). Tinned fish and caviar are variety at the enthusiast end.

Size: 7 departments, 169 kinds, 155 archetypes, 47 versions; 60 brands; 10 traditions.

### Gaps for hobbyists
- **J2-1 Tinned fish (conservas) is under-branded.** Tinned fish is a real collecting scene: vintage sardines, conservas tastings, tin-art collecting. The register has 60 brands, but Fishwife, José Gourmet, Minerva, Cocagne, La Brújula, Güeyu Mar, Patagonia Provisions, Comur and Briosa are all absent across J (to verify each). Also, 4 archetype `mk` values have no register entry: Herpac, Olasagasti, Carmelo, Angelachu. **Fix:** harvest Portuguese, Spanish and French conservas houses from retailer brand directories and give the tinned kinds producer archetypes.
- **J2-2 No Japanese brand fish.** Japan's branded fish are absent: Ōma tuna, Seki-aji and Seki-saba (to verify GI status). These are the fish equivalent of brand wagyu in J1. **Fix:** add them as archetypes under Tuna and Mackerel.

### Too much detail
- **J2-3 Near-empty caviar kinds.** There are 12 sturgeon-caviar kinds. White sturgeon, Amur, Hybrid, Sterlet, Hackleback, Paddlefish and Pressed caviar each have 0 archetypes and 1–2 types. **Fix:** make one "Sturgeon caviar" kind with species as archetypes and caviar houses (Petrossian, Kaviari, Calvisius, Sturia) as versions. Make one "American roe" kind for hackleback, paddlefish and bowfin.
- **J2-4 Snail and gastropod kinds.** Periwinkle, Top shell, Mud snail, Apple snail and Conch are five separate kinds with 0 archetypes and 1–2 types each. **Fix:** merge them into "Sea & freshwater snails" with types. Keep Land snail separate (escargot grades).

### Confusing organisation
- **J2-5 Species axis is inconsistent.** Prawns get one kind per species (9 kinds, all with 0 archetypes). Fish are lumped: "Flatfish & skate" holds Dover sole, turbot, halibut and plaice as types. "Tuna" mixes species, cuts and sashimi grades (akami, chutoro, otoro) in 16 types. "Regional white fish", "Deep-sea fish" and "Pomfret, croaker & Asian market fish" are catch-alls. **Fix:** use one rule. Species become kinds only where buyers shop by species: tuna, salmon, cod, sole and turbot. Elsewhere use family kinds. Move the tuna cut grades into a `b` criterion.
- **J2-6 Untranslated labels.** The archetype names "みやぎサーモン" and "若狭小浜小鯛ささ漬" are in Japanese script. **Fix:** give English names with romaji aliases.
- **J2-7 Cross-category duplicates.** Katsuobushi is a J2 kind and also a J5 archetype (dashi ingredients). "Fermented bean curd" is a kind in J5 and an archetype in J3. **Fix:** keep each in one place and cross-link.

### What it would look like (Caviar & roe › Sturgeon caviar)
```
Sturgeon caviar
  Beluga (Huso huso) → grade 000 / 00 / 0
    v: Petrossian Beluga Royal · Sturia Beluga
  Osetra (A. gueldenstaedtii) → Imperial · Royal
  Kaluga (H. dauricus) · Kaluga hybrid
  Baerii (A. baerii) → Caviar d'Aquitaine
  White sturgeon (A. transmontanus) → California farmed
  Sevruga · Sterlet · Amur
American roe → hackleback · paddlefish · bowfin
```
Priority: medium
Fix size: medium

---

## J3 Dairy, Eggs & Alternatives

**Brand mode:** variety for cheese; mixed for butter, yoghurt, and tofu and meat alternatives; tier for milk, eggs, baby milks and plant drinks.

Size: 8 departments, 157 kinds, 441 archetypes, 552 versions; 107 brands; 22 traditions.

### Gaps for hobbyists
- **J3-1 Missing cheeses.** Cheese is strong (102 kinds, 365 archetypes). These are absent across all files: Oscypek (PDO, Poland), Paški sir, Garrotxa, Zamorano (PDO), Mothais-sur-feuille, Brin d'Amour, Harbison, Mt Tam, Casu marzu and Babybel. Mimolette appears only inside the brand register, with no archetype. **Fix:** add them to the matching make-family kinds.
- **J3-2 Affineurs and mass brands.** The criterion "Maker and affineur" is set, but the major affineurs (Hervé Mons, Androuët) and mass brands (Sargento, Babybel, Ehrmann) are absent. **Fix:** add affineurs as brands with `kf` "affineur" and as versions on the cheeses they age.

### Too much detail
- **J3-3** "Duck egg" and "Quail egg" are separate kinds with 0 types and 0 models. **Fix:** make one "Eggs from other birds" kind with types for duck, quail and goose. Keep breed eggs (Burford Brown) as hen's-egg archetypes.

### Confusing organisation
- **J3-4 Mixed shelf axes in Cheese.** Make-family shelves (Fresh, White-rind, Washed-rind, Alpine, Blue, Stretched-curd) sit beside country shelves (Cheddar & British; Dutch & Nordic; Spanish, Portuguese & Latin American; Italian grana & pecorino) and a "Regional pressed cheese" shelf. Pressed sheep cheeses end up in three places: Manchego, Ossau-Iraty and Pecorino. **Fix:** make family the shelf axis, e.g. "Pressed uncooked (sheep)" and "Cheddared". Make country a view.
- **J3-5 Misplaced department.** Meat alternatives (Plant-based meat with 8 archetypes, Mycoprotein, Seitan) are in a dairy category. Dulce de leche is a kind here and an archetype in J8. **Fix:** move "Tofu, tempeh & meat alternatives" to a J1 "Meat alternatives" department or to its own dept, cross-linked. Keep Dulce de leche in J8.
- **J3-6 Register hygiene.** "Cypress Grove" and "Cypress Grove Chevre" are two entries for one brand. 4 brands have no country. 2 archetype `mk` values have no register entry: Fromagerie Lincet and Žemaitijos Pienas.

### What it would look like (Cheese › Pressed uncooked sheep cheese)
```
Pressed uncooked sheep cheese
  Queso Manchego PDO → fresco · semicurado · curado · viejo
    v: artesano (raw milk) · industrial (pasteurised)
  Ossau-Iraty PDO → fermier · estive
  Pecorino Romano PDO · Pecorino Sardo PDO · Pecorino Toscano PDO
  Idiazábal PDO → smoked · unsmoked
  Zamorano PDO (new) · Oscypek PDO (new, smoked)
```
Priority: medium
Fix size: small

---

## J4 Fruit, Vegetables & Fresh Produce

**Brand mode:** variety for fruit, vegetables, mushrooms and sea vegetables; mixed for salad and herbs; tier for mixed packs. Club brands (Pink Lady, Envy, Sumo, Zespri) make the fruit end mixed.

Size: 5 departments, 208 kinds, 1,078 archetypes, 328 versions; 33 brands; 4 traditions.

### Too much detail
- **J4-1 Garden seed catalogue inside a food category.** 485 of the 1,078 archetypes are sourced from www.rhs.org.uk (RHS garden varieties). Wikipedia supplies 513, and no other site more than 13. These are grower cultivars that shoppers never see on a label. Examples: Cabbage has 31 archetypes (Winterjewel, TZ 7022, Cabbice), Cauliflower 25 (Moby Dick, Skywalker), Green bean 29, Broad bean 15, Brussels sprout 11, Celeriac 6 and Parsnip 6, all seed varieties. This is retail-harvest skew, and it is the wrong axis for a food category. **Fix:** move seed cultivars to the living-plants register (Garden). In J4, keep only cultivars sold by name at retail or under PDO/PGI: Jersey Royal, Rossa di Tropea, Vidalia, Charlotte, Hass, Alphonso, Shine Muscat. Target about 400 archetypes.
- **J4-2 Echo archetypes and empty kinds.** Clementine, Yuzu, Sudachi and Kabosu each hold one archetype with the same name as the kind. 24 kinds are completely empty, e.g. Cloudberry, Mangosteen, Kiwano, Enoki, Maitake, Sage and Chives. "Mixed fruit & vegetables" is a catch-all. **Fix:** delete the echo archetypes. Merge the Japanese aromatic citrus into one "Kōji citrus (yuzu, sudachi, kabosu)" kind. Merge the minor mushrooms into "Speciality cultivated mushrooms" with types. Dissolve the Mixed packs department into types.

### Gaps for hobbyists
- **J4-3 Premium and gift fruit is under-covered.** Japanese gift fruit is a real scene, but Shizuoka Crown melon is absent. The register has only 33 brands and lacks the European apple consortia: Marlene, Melinda and VOG/Val Venosta (to verify). Sea vegetables have 3 kinds; there is no fresh nori, dulse or sea lettuce in J4 (dulse and kombu appear only dried, in J5). **Fix:** add the Japanese premium grades (Yubari King and Densuke are present; add Crown melon), the consortium brands, and fresh sea vegetables.

### Confusing organisation
- **J4-4 One-kind shelves.** Apples, Strawberries, Mangoes and Potatoes are each a shelf holding one kind, next to 14-kind shelves. **Fix:** group them as "Pome fruit" and "Soft fruit", with apples and strawberries as their lead kinds.

### What it would look like (Fruit › Apples, retail axis)
```
Apple
  Club varieties → Pink Lady (Cripps Pink) · Jazz · Envy · Kanzi · Cosmic Crisp · SweeTango
  Heritage dessert → Cox's Orange Pippin · Ashmead's Kernel · Belle de Boskoop
  Global staples → Gala · Fuji · Granny Smith · Honeycrisp · Golden Delicious
  Cooking → Bramley's Seedling
  PGI origins → Mela Alto Adige / South Tyrol apples · Annurca Campana
  (seed-catalogue cultivars → Garden plant register)
```
Priority: high
Fix size: medium

---

## J5 Store Cupboard

**Brand mode:** mixed in every department; variety for home brewing.

Size: 10 departments, 237 kinds, 311 archetypes, 168 versions; 108 brands; 5 traditions.

### Gaps for hobbyists
- **J5-1 Olive oil has no producers.** "Olive oil" holds 15 archetypes, all PDOs, with 4 models. Enthusiasts compare estates that win competitions (Flos Olei, NYIOOC). Castillo de Canena, Oro Bailén, Laudemio, Frantoio Muraglia, Gaea, Cobram Estate and California Olive Ranch are all absent. **Fix:** add producers as versions under their PDO or as an estate shelf. Treat it as variety at the top end.
- **J5-2 Pasta shapes are thin.** There are 7 pasta kinds with 3–5 shape archetypes each. Trofie, strozzapreti, garganelli, cavatelli, calamarata, mafaldine, lasagne and cannelloni are absent (no sheet pasta at all). The artisan makers Rustichella d'Abruzzo, Setaro, Felicetti and Benedetto Cavalieri are absent, although Faella, Afeltra and dei Campi are present. **Fix:** add the missing shapes and a "Sheet pasta" kind. Put the bronze-die Gragnano makers in the register.
- **J5-3 Heirloom beans.** Rancho Gordo is in the register, but the 12 dried-bean kinds have 5 archetypes between them (none US heirloom). **Fix:** use one "Dried beans" kind with heirloom and PDO archetypes (Royal Corona, Eye of the Goat, Tarbais, Judión, to verify).
- **J5-4 Hot-sauce long tail.** Hot sauce has 12 archetypes. Secret Aardvark, Melinda's and Yellowbird are absent (to verify). **Fix:** add the craft hot-sauce makers as stubs.

### Too much detail
- **J5-5 Empty single-pulse and single-flour kinds.** There are 14 empty kinds, e.g. Black beans, Pinto beans, Small red beans, Black-eyed peas, Dried soybeans, Horse gram, Chickpea flour, Maize flour, Buckwheat flour, Millet flour, Icing sugar, Distilled vinegar and Konjac noodles. **Fix:** merge them into "Dried beans", "Other flours" and "Vinegar" kinds with types.

### Confusing organisation
- **J5-6 Missing product family across J.** Bought prepared and frozen foods have no home in any J category: ready meals, frozen pizza, oven chips, chilled dips and hummus, dumplings, and baby food (weaning purées and pouches, needed by the Baby & child view). A grep found none of them. Only fish fingers (J2) and deli meats (J1) cover any of this. **Fix (OWNER QUEUE):** decide whether bought prepared foods are "products" (in scope) or "dishes" (Culinary). If in scope, add a "Chilled, frozen & prepared foods" department here or a new J category.
- **J5-7 Duplicates.** "Flavoured syrup" (J5) overlaps "Café & flavouring syrup" (J9); Monin and Torani are in both registers. Medjool, Kashmiri chilli and Piment d'Espelette are archetypes in both J4 and J5. **Fix:** keep syrups in J9. Keep the dried forms here, cross-linked.

### What it would look like (Oils › Olive oil)
```
Olive oil  [b: grade · harvest date · Flos Olei / NYIOOC]
  Baena PDO · Priego de Córdoba PDO
    v: Castillo de Canena Reserva Familiar · Oro Bailén (to verify PDO)
  Terra di Bari PDO → v: Frantoio Muraglia
  Toscano PGI → v: Laudemio estates
  Kalamata PDO · Sitia Lasithi PDO → v: Gaea
  New World estates → Cobram Estate · California Olive Ranch
```
Priority: medium
Fix size: medium

---

## J6 Coffee, Tea & Infusions

**Brand mode:** mixed for coffee, tea and cocoa (tier for everyday packs, variety for speciality); tier for herbal infusions.

Size: 4 departments, 68 kinds, 225 archetypes, 245 versions; 94 brands; **2 traditions**.

### Gaps for hobbyists
- **J6-1 Traditions are thin for a tradition-led field.** There are only 2 entries (Pu'er craft, Wuyi yancha). Expected: Uji tea, Darjeeling, Kenyan smallholder, Taiwanese high-mountain oolong, Turkish coffee (UNESCO ICH), Arabic coffee (UNESCO ICH), Ethiopian coffee ceremony, gongfu cha, Moroccan mint tea. **Fix:** add about 10 entries (Food & drink) and link their signature forms.
- **J6-2 Missing teas and coffees.** Gunpowder tea is absent from J6 (found only in C3). Sobacha is absent. Ninety Plus, and the Italian espresso houses Kimbo and Segafredo, are absent. **Fix:** add gunpowder under Chinese green tea, and add the coffee houses as brands.
- **J6-3 Pu-erh factory axis.** Collectors buy by factory, recipe number and year (e.g. Menghai 7542, Xiaguan tuocha). These appear inside archetypes, but Menghai, Xiaguan and Haiwan are archetype `mk` values with no register entry. In total 16 `mk` values in J6 lack an entry. **Fix:** register the factories, and make recipes versions under each factory archetype.

### Too much detail
- None of substance. The herbal infusions are already restrained: 15 kinds, mostly types.

### Confusing organisation
- **J6-4 Concept archetypes.** "Motamayor ten genetic groups", "Fine or flavour cocoa", "Koicha vs usucha", "Fruit and floral blends", "Pu'er cake (bing)" and "Historic Mukashi blends" are classifications or forms, not objects. **Fix:** move them into `b` criteria or `t` types.
- **J6-5 Mixed archetype levels in coffee.** "Single-origin coffee" mixes countries (Colombia), regions (Yirgacheffe) and a grade (Kenya AA). Varieties sit in a separate kind ("Geisha & rare-variety coffee"), so a Panama Geisha could go in either kind. **Fix:** country → region archetypes with estates (Hacienda La Esmeralda) as versions. Make variety and process `b` axes.

### What it would look like (Tea › Pu-erh)
```
Raw pu-erh (sheng)
  Menghai Tea Factory (Dayi) → v: 7542 · 8582 · 7532 · by year
  Xiaguan Tea Factory → v: Jia Ji tuocha · FT series
  Mountain origins → Yiwu · Bulang · Lao Ban Zhang · Bingdao · Nannuo
  form t: bing 357 g · tuocha · brick · loose
Ripe pu-erh (shou) → Menghai 7572 · Haiwan
```
Priority: medium
Fix size: small

---

## J7 Wine, Beer & Spirits

**Brand mode:** variety for wine, beer, whisky, spirits, liqueurs, sake, and cider and mead; tier for ready-to-drink; mixed for no and low alcohol.

Size: 12 departments, 255 kinds, 991 archetypes, 1,698 versions; 445 brands; 33 traditions.

### Gaps for hobbyists
- **J7-1 Scotch is under-built against Whiskybase.** "Single malt Scotch whisky" has 15 archetypes, which are expressions (Glenfiddich 12, Lagavulin 16). Bruichladdich, Caol Ila, Kilchoman, Glenfarclas, Dalmore, Clynelish and Mortlach are absent. The independent bottlers Gordon & MacPhail and Cadenhead are absent, and Signatory appears only in a tradition. Region is a `b` criterion but not a shelf. **Fix:** copy the Whiskybase axis: region shelf → distillery archetype → core expressions and indie bottlings as versions. Cover the ~150 active distilleries, with stubs for the minor ones.
- **J7-2 Spirit enthusiast brands are missing.** Rum: Foursquare, Worthy Park, Zacapa and Smith & Cross are absent; Caroni appears only in J5. Tequila: Siete Leguas and Fuenteseca are absent. Amaro: Cynar, Ramazzotti, Braulio, Lucano and Suze are absent. Sake breweries: Jikon and Masumi are absent; Junmai sake has 4 archetypes. **Fix:** add these as archetypes or brands.
- **J7-3 Wine grape gaps.** These are absent across all files: Sylvaner, Müller-Thurgau, Arneis, Cortese, Greco, Carricante, Agiorgitiko, Moschofilero, Sagrantino, Lagrein, Petite Sirah, Txakoli, Arinto, Encruzado, Mavrud and Kadarka. Chasselas (Swiss wine) appears only as a table grape in J4. Icons are thin outside Burgundy: Cabernet Sauvignon has 3 archetypes against 26 for Pinot Noir. Egon Müller, Henschke Hill of Grace, Monfortino, Coche-Dury and Leflaive are absent.

### Too much detail
- **J7-4** "Mixed case & gift set" is a catch-all of 6 types. **Fix:** make it a format type on each department.

### Confusing organisation
- **J7-5 Inconsistent archetype level in wine.** Archetypes mix appellations (Barolo, Rioja), single vineyards (La Tâche), producer wines (Screaming Eagle, Tignanello) and classifications ("Médoc and Graves classed growth"). **Fix:** apply grape/region kind → appellation archetype → producer and cuvée versions everywhere. Make classifications `b` ladders.
- **J7-6 Sake grade split.** "Junmai sake" carries junmai ginjo and daiginjo types, while "Honjozo, ginjo & daiginjo sake" holds the non-junmai grades. A reader looking for "daiginjo" finds two homes. **Fix:** use one Sake kind with the JAS grade ladder as `b`, and brewery archetypes.
- **J7-7** "English cider" holds Magners Irish cider. **Fix:** rename the kind "British & Irish cider".

### What it would look like (Whisky › Scotch single malt)
```
Islay
  Lagavulin → v: 16 · 8 · Distillers Edition · 12 Cask Strength
  Laphroaig → 10 · Quarter Cask · 25
  Bruichladdich → Classic Laddie · Port Charlotte · Octomore (new)
Speyside
  The Macallan → Sherry Oak 12/18 · Double Cask
  Mortlach (new) · Glenfarclas (new) → 105 · Family Casks
Campbeltown → Springbank 10 · 15 · Longrow · Hazelburn
Independent bottlers [brand] → Gordon & MacPhail · Cadenhead · Signatory
```
Priority: high
Fix size: large

---

## J8 Bakery, Sweets & Snacks

**Brand mode:** mixed for bread, biscuits, crisps and ice cream; variety for chocolate and confectionery; tier for snack nuts and bars.

Size: 7 departments, 123 kinds, 532 archetypes, 547 versions; 247 brands; 39 traditions.

### Gaps for hobbyists
- **J8-1 Bean-to-bar chocolate is under-branded.** "Single-origin dark chocolate" has 9 archetypes, and some are concepts ("Vintage plantation chocolate", "Two-ingredient origin", "Criollo varietal bars"). Askinosie, Fruition, Pacari, Friis-Holm, Åkesson's, Raaka, Castronovo and Menakao are absent. **Fix:** use the bean-to-bar makers as the archetype axis (maker → origin bar as version), drawing on the Academy of Chocolate and International Chocolate Awards lists. Move the concepts into `b`.
- **J8-2 Nuts have no protected archetypes.** The 12 single-nut kinds hold Marcona almond and Nocciola del Piemonte IGP only as `m` models, and Pistacchio Verde di Bronte DOP is absent. **Fix:** see J8-4.

### Too much detail
- **J8-3 Ice-cream flavours as archetypes.** "Ice cream tub" has 17 archetypes that are flavours (Vanilla, Chocolate, Cookie dough, Rocky road). **Fix:** make flavours `t` types, and make makers (Ben & Jerry's, Häagen-Dazs, Jeni's, Salt & Straw) the archetype or brand axis.
- **J8-4 Twelve empty nut kinds.** The "Snack nuts & bars" shelf holds 22 kinds. Almonds, Walnuts, Cashews, Peanuts, Pistachios, Pecans, Macadamias, Brazil nuts, Pine nuts, Chestnuts and Mixed nuts are each defined as "X in any form", with almost nothing in them. They duplicate the types of "Roasted & salted nuts". **Fix:** use one "Nuts" kind (or a J5 "Nuts & seeds for baking" kind) with types, plus PDO archetypes (Bronte, Piemonte, Marcona).

### Confusing organisation
- **J8-5 Duplicates.** Brioche is an archetype under both "Enriched bread" and "Croissant & viennoiserie". Toblerone is under both "Flavoured & inclusion bar" and "Countline". Dulce de leche is also in J3. "Hot chocolate bomb & drinking flakes" overlaps J6 "Drinking chocolate".
- **J8-6 Label mismatch.** The department "Confectionery traditions" holds the generic "Sugar confectionery" shelf (gummies, chewing gum, mints). **Fix:** rename it "Sweets & confectionery" and keep "World confectionery traditions" as the second shelf.
- **J8-7 Register hygiene.** These pairs are split entries: Arnott's / Arnott's Group, Callebaut / Barry Callebaut, Kellogg's / Kellanova, Lotte / Lotte Wellfood, Meiji / Meiji Seika, Frito Company / Frito-Lay. 21 archetype `mk` values lack an entry, e.g. Streets, Klondike, Popsicle. **Fix:** treat parent groups as `rel` and keep one entry per consumer brand.

### What it would look like (Chocolate › Bean-to-bar)
```
Bean-to-bar dark chocolate  [b: cocoa % · origin · award]
  Pralus → v: Tanzanie · Madagascar · Pyramide des Tropiques
  Michel Cluizel → plantation bars: Mangaro · Los Ancones
  Amedei → Chuao · Porcelana
  Marou → Ben Tre · Tien Giang · Dong Nai
  Friis-Holm (new) · Fruition (new) · Pacari (new) → origin bars
  Domori → Criollo range
```
Priority: medium
Fix size: medium

---

## J9 Soft Drinks & Water

**Brand mode:** mixed for water, syrups, energy drinks and RTD coffee and tea; variety for sodas, tonics and fermented drinks; tier for juices.

Size: 8 departments, 81 kinds, 171 archetypes, 336 versions; 146 brands; 7 traditions.

### Gaps for hobbyists
- **J9-1 Regional soda long tail.** Regional sodas are a collecting and import scene. These are absent across all files: Calpis/Calpico, Milkis, Limca, Faygo, Ale-8-One, Bionade, Fassbrause, Mezzo Mix (cola-orange mix), Apfelschorle and Appletiser. **Fix:** add a "Cola-orange mix (Spezi)" kind and a "Juice spritzer (Schorle)" kind. Add Calpis under the fermented drinks.
- **J9-2 Mineral-water connoisseur end.** There are 12 sparkling and 7 still mineral-water archetypes. Acqua Panna, Ty Nant and Svalbarði are absent (to verify). The reference database FineWaters classifies waters by TDS and source type (to verify), and the dept `b` already uses those axes. **Fix:** add about 15 more source archetypes as variety.

### Too much detail
- **J9-3 The same types repeat on every soda kind.** The 8 types "regular, cane-sugar, diet / zero sugar, caffeine-free, glass bottle, can, PET bottle, fountain syrup" appear on Cola, Pepper, Lemon-lime, Citrus, Orange, Fruit, Root beer and Cream soda. **Fix:** move them into the department `b` (Sweetener and Format are already listed there) and keep only the flavour-specific types.

### Confusing organisation
- **J9-4 Register duplicates.** "Coca-Cola", "Coca-Cola (Japan)" and "The Coca-Cola Company" are three entries; also "Pepsi" / "PepsiCo" and "Bundaberg" / "Bundaberg Brewed Drinks". Fanta, Sprite and Schweppes appear as brands, while Schweppes is also in the J8 register. **Fix:** one entry per consumer brand, with the parent as `rel`.
- **J9-5 Cross-category overlap.** "Café & flavouring syrup" duplicates J5 "Flavoured syrup". The water-kefir and kombucha cultures overlap J3 kefir. **Fix:** keep syrups here and cross-link the cultures.

### What it would look like (Sodas › Regional & heritage)
```
Cola-orange mix (new) → Spezi · Mezzo Mix
Lactic soft drink (new) → Calpis / Calpico · Milkis
Tutti-frutti soda → Irn-Bru · Inca Kola · Big Red
Herbal soda → Almdudler · Moxie · Dandelion & Burdock
Lemon-lime regional → Limca (new) · Faygo Rock & Rye (new)
Marble soda → Ramune
```
Priority: low
Fix size: small

---

## J10 Tobacco, Smoking & Vaping

**Brand mode:** variety for cigars, pipes and pipe tobacco, and hookah; mixed for cigarettes, vaping, snus and lighters; tier for cannabis and herbal.

Size: 10 departments, 127 kinds, 192 archetypes, 271 versions; 93 brands; 12 traditions.

### Gaps for hobbyists
- **J10-1 Pipe tobacco blends are nearly empty.** There are 8 blend kinds with 9 archetypes in total. The Oriental blend, Kizami and Dokha kinds have none. The community database (TobaccoReviews) is organised by blender → blend. These are absent: Erinmore, Penzance, Frog Morton, Nightcap, Squadron Leader, Plum Pudding and the G. L. Pease and McClelland lines. Samuel Gawith, Gawith Hoggarth, Orlik and Lane are `mk` values with no register entry. **Fix:** add a blender register and 40–60 blend archetypes under the blend families.
- **J10-2 Cannabis has no strains.** The 21 cannabis kinds have 0 archetypes, apart from glass and vaporiser makers. The department is tier, but enthusiasts buy by named strain: OG Kush, Blue Dream, Sour Diesel and Northern Lights are all absent. The reference databases are Leafly and Seedfinder (to verify). **Fix:** make Cannabis flower variety, with strain archetypes and lineage as versions. Keep the legal-status `b`.
- **J10-3 Pipe makers and vape hardware.** Kaywoodie, Butz-Choquin, Vauen, Ascorti, Radice and Bo Nordh are absent. Uwell, GeekVape and dotMod are absent. Habanos marques such as Vegas Robaina, Juan López, Diplomáticos and Por Larrañaga are absent (to verify current list).

### Too much detail
- **J10-4 Duplicate department.** A tenth department, "Lighters & accessories", holds a single kind ("Lighter flint", 1 model). It duplicates "Lighter fuel, flints & wicks" in "Lighters & smoking accessories". **Fix:** delete it.
- **J10-5** "Molasses catcher", "Herbal smoking blend", "Tincture", "Distillate" and "Kief" are empty kinds. **Fix:** fold them into their sibling kinds as types.

### Confusing organisation
- **J10-6 Briar pipe mixes axes.** Its 18 archetypes mix shapes (Billiard, Bulldog, Dublin) with makers (Savinelli, Dunhill, Comoy's) and lines (Peterson System). **Fix:** make shapes the archetypes, makers the brand register, and maker lines versions. Swisher Sweets is an archetype under both Cigarillo and Machine-made cigar.
- **J10-7 Register gaps.** 33 archetype `mk` values have no register entry, the highest in J. Philip Morris vs Philip Morris International, R.J. Reynolds and Nat Sherman are examples.

### What it would look like (Pipes & pipe tobacco › Pipe tobacco)
```
Virginia / Perique
  Escudo Navy De Luxe → v: Cope (orig.) · Gawith Hoggarth / STG (current)
  Three Nuns → original · Orlik reissue
  Orlik Golden Sliced
English & Balkan
  Dunhill My Mixture 965 → Dunhill era · Peterson era
  Early Morning Pipe · Nightcap (new) · Penzance (new)
Aromatic → Erinmore (new) · Captain Black · Ennerdale Flake
Blender register → Samuel Gawith · Gawith Hoggarth · McClelland · G. L. Pease · Cornell & Diehl
```
Priority: medium
Fix size: medium
