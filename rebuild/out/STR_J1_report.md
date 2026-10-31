# STR_J1 report (Meat & Poultry)

**Counts before to after:** departments 10 to 10; shelves 27 to 32; kinds 153 to 164; archetypes 341 to 275. validate.py --v3: OK.

**Category:** added `ax` and a 10-step `key` with a precedence note. Lead unchanged (no conflict with RULES).

**Departments:** every one has `t` and `ax`. Every shelf has `t`, and `ax` where it holds more than three kinds.

**Regrouped shelves:**
- Beef: steaks, roasting joints, braising and slow-cook cuts, veal, and mince/offal/bulk are now separate shelves.
- Pork: breed, chops and joints, belly and extremities, and mince/offal/bulk.
- Poultry: chicken, turkey/duck/goose, and mince/offal/liver (foie gras moved here).
- Game: venison and boar, birds, small game.
- Other meats: mammals, birds/reptiles/insects, and boxes.

**Types:** every flat type list became hand-written `tt` groups, each answering one question (Cut, Bone, Breed, Cure, Smoking and so on).

**Split or renamed:** "Minor grilling steaks" was a catch-all. It became Rump steak (recorded in J1_renames.json), Tri-tip, Skirt & flank steak, and Flat iron & hanger steak.

**Added kinds:**
- Steaks, source Cut of beef: Tri-tip, Skirt & flank steak, Flat iron & hanger steak.
- Sausages, source List of sausages: Cotechino, Thai & Southeast Asian sausage, Saveloy, Linguiça & Portuguese smoked sausage, Chả lụa, Balkan & Baltic dry sausage.
- Tinned meats, sources Vienna sausage and Canned meat: Tinned sausages, Potted meat & devilled ham.
- Five hams added as archetypes of Regional dry-cured hams, source List of hams: Xuanwei, Njeguški pršut, Lacón gallego, Anfu, Elenski but.

**Demoted archetypes:**
- Species and breed archetypes, such as the game species, Iberian pig, the turkey breeds, American Pekin duck and Embden goose, became `tt` types.
- Plant-based sausage, mince and chicken, and macrobiotic Seitan, were demoted; their sourced versions went to `m` as models.
- Archetypes with the same name as their kind (Merguez, Boerewors, Biltong and similar) were dropped, since the kind itself carries the source. Their versions went to `m`.
- Foie gras and confit preparation names became `tt`.
- The new kinds Cotechino, Saveloy, Chả lụa, Tri-tip and so on carry no archetypes.

**Coverage references fetched (Wikipedia):** Offal, Cut of beef, Cut of pork, List of sausages, List of hams, Game (food), Tripe, Charcuterie, Vienna sausage, Canned meat.

**Cross-links:** 41 `see` entries, targets checked. They are mostly within J1 (fresh and cured cuts, foie gras, confit, corned beef). Others point to J2 Fish pâté & rillettes, J3 Tofu and J8 Pork scratchings & chicharrón, Protein snack.

**Moved:** nothing (J1_moves.json unchanged).

**Not done or weak:**
- Flat iron and hanger are sourced only from a navigation box on Cut of beef.
- Tripe is an offal type with no separate kind.
- Water buffalo, yak and emu were not added (no fetched source).
- The Cut of lamb and poultry reference pages were not fetched; lamb and poultry shelves were checked only against general reference pages.
- Firecrawl and Parallel are out of credit, so WebFetch only.
