# FIX_J1 report
Counts before -> after: kinds 157 -> 150 (+1 empty dept "Meat alternatives" for J3's incoming kinds); archetypes 326 -> 326 (+1 Hinai-jidori, -1 label-class archetype); brands 51 -> 62; traditions 0 -> 9; moves out 0.

- J1-1 done: 9 traditions (Italian salumi, Parma and San Daniele prosciutto, Iberian dehesa curing, Spanish embutidos, French charcuterie, German Wurst, Polish kiełbasa, Cantonese preserved meats, Japanese jidori). Sourced only from fetched Wikipedia pages. Authenticity marks left blank where no fetched page gave them (embutidos, French charcuterie, Wurst, Cantonese, jidori); period left blank throughout.
- J1-2 done: added Tyson Foods, Perdue Farms, Applegate, Niman Ranch, Campofrío, ElPozo, Fleury Michon, Herta, Rovagnati, Citterio, La Quercia. Founding year blank for Herta (uncertain) and La Quercia (no fetched date). Citterio was not in any other register under that name, so none was reused.
- J1-3 done: Hinai-jidori archetype (Whole chicken), Lap yuk, Saucisson à l'ail, Poultry offal kinds. "Saucisson à l'ail" source is French Wikipedia; it names no region or label.
- J1-4 done: five beef offal kinds -> "Beef & veal offal"; rump, tri-tip, flat iron, flank, skirt, hanger -> "Minor grilling steaks" (named so because validate.py rejects names starting "Other"). Ribeye, sirloin, fillet, T-bone and picanha kept. Oxtail and the other empty kinds left, as the finding did not ask to merge them.
- J1-5 done: Dry-aged beef kind removed, "dry-aged" added as a type on ribeye, sirloin, T-bone and rib roast. Meat box and Charcuterie selection now on a "Boxes & selections" shelf in Other meats.
- J1-6 done: kind renamed "Spreadable raw sausage"; Ibérico label-class archetype removed and added as a criterion in the Pork department's `b`.
- Coordinator note: empty "Meat alternatives" dept and shelf created for J3's kinds.
