# DPW1_B7 report: B7 Climate, Water & Energy (offline)

## Task 1: missing kinds (49 rows, DPW1_B7_kinds.tsv)
Inputs: 26 harvest-report items, 23 types from fetched.tsv "gave" columns; no DPMK_1_B7 file.

**Counts:** covered 16, attribute 16, other_category 9, new_kind 8.

**New kinds** (next free id per R-58; all go to HV_NK):
- B7.1.3.10 Box fan
- B7.1.3.11 Window fan
- B7.2.3.12 Swim spa (no URL) †
- B7.3.2.03 Power optimizer
- B7.3.2.04 Battery-bank charger
- B7.4.3.02 PV combiner box
- B7.4.3.03 Rapid shutdown device
- B7.4.4.01 Battery enclosure, in a new leaf B7.4.4 Home-battery equipment

**Other categories:**
- C8: shower valve, shower enclosure, surge protection
- C1: shower pump, solar water pump
- B5: jug filter, hot-water dispenser, solar fridge
- G1: DC-DC vehicle charger

**Main calls:**
- Heaters are filed by how they heat. Tube heater goes to the convector heater, torpedo heater and kerosene stove to the flueless heater, electric flame-effect fire to the fan heater.
- In-wall and plinth fitting is an attribute.
- Thermal-fluid and oil-free radiators are a fill attribute of the oil-filled radiator, because the body is the same. Its definition should say "fluid or solid core".
- Shower head goes to the shower (C8 memo: "the unit or head" stays B7).

## Task 2: named forms (25 rows, DPW1_B7_moves.tsv)
**to_line (15):**
- Kirigamine and Waterdrop X Series join their existing lines.
- New lines: Baxi Combi 2, Sengoku KeroHeat, Sengoku HeatMate, Hitachi Shirokuma-kun, Panasonic Eolia, Corona ReLaLa, Toshiba Daiseikai, Iris Ohyama WOOZOO.
- DampRid: 5 rows go to one line, because it is a consumable brand line (C2(e)).

**move_kind (2):**
- Dyson Purifier Hot+Cool goes to the air purifier (tree precedence).
- Vornado Transom goes to the window fan, once that kind is attested.

**drop (8):** names that only restate the kind or an attribute, such as "Halogen Heater", "Mini Portable Dehumidifier" and "Side of Pole Mount".

No named form is a maker or a shop.

## Task 3: navigation
I confirm R-116: shoppers start from the job, then pick the device type.
- Every harvested catalogue (Screwfix, Kakaku, Solar Store, Wickes, City Plumbing, Navien) divides by job, then type.
- Makers come in only through models: 265 forms from 99 makers.
- Brand collections appear only in solar and water treatment (Victron, Waterdrop, Sun-Mar). That supports a brand filter in solar, not a brand way in.

**View:**
1. The 11 proposal groups, from Heating to "Filters, salt and spare parts".
2. Kinds by form or heat source. Fans: desk, stationary, tower, wall, handheld, box, window, circulator, ceiling, extractor, ventilation unit.
3. Size first (BTU, kW, litres, pints per day, kWh), then efficiency, then named forms.

## Rules applied
R-58, C2, C3, C10–C12, S3, CV-17, K-157, K-186, B-26, B-33, R-35, R-70a, R-116.

## Resting on † claims
- Swim spa and the soft-sided and in-ground hot tubs rest on a guide page only. The swim spa's boundary with C2 (pools) is unchecked.
- ReLaLa and Daiseikai as lines rest on product knowledge.
- The ozone generator was seen only in a search excerpt.
- The four solar and battery kinds cite collection-list pages that the harvester did not tell apart.
