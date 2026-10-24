# DPW1_B7 report: B7 Climate, Water & Energy (offline)

## Task 1: missing kinds (49 rows, verify/out/DPW1_B7_kinds.tsv)
The inputs were 26 single items from the two harvest reports, plus 23 generic types taken from the fetched.tsv "gave" columns. There was no DPMK_1_B7 file to check against.
- **Counts:** covered 16, attribute 16, other_category 9, new_kind 8.
- **New kinds** (next free number per R-58, checked against data/kinds.tsv and TREE_B7_map.tsv; all go to HV_NK for attestation):
  - B7.1.3.10 Box fan
  - B7.1.3.11 Window fan
  - B7.2.3.12 Swim spa (no source_url) †
  - B7.3.2.03 Power optimizer
  - B7.3.2.04 Battery-bank charger
  - B7.4.3.02 PV combiner box
  - B7.4.3.03 Rapid shutdown device
  - B7.4.4.01 Battery enclosure, in a new parts leaf **B7.4.4 Home-battery equipment**
- **Other categories:**
  - C8: shower valve, shower enclosure, surge protection
  - C1: shower pump, solar water pump
  - B5: pitcher filter, instant hot-water dispenser, solar refrigerator
  - G1: DC-DC vehicle charger
- **Covered or attribute, main calls:**
  - Space heaters are filed by mechanism (tree precedence). Tube heater goes to the convector heater, torpedo and kerosene stoves to the flueless room heater, and electric flame-effect fires to the fan heater. In-wall and plinth fitting is an installation attribute.
  - Thermal-fluid and oil-free radiators are a fill attribute of the oil-filled radiator, because the body is the same (rule T). Its definition should say "fluid or solid core".
  - Shower head is covered by the shower (C8 memo: "the unit or head" stays B7).
  - Portable power station goes to the home battery (K-157).

## Task 2: named forms (25 rows, verify/out/DPW1_B7_moves.tsv)
- **to_line (15):**
  - Kirigamine and the Waterdrop X Series already have line rows.
  - New lines: Baxi Combi 2, Sengoku KeroHeat and HeatMate, Hitachi Shirokuma-kun, Panasonic Eolia, Corona ReLaLa, Toshiba Daiseikai, Iris Ohyama WOOZOO, and DampRid moisture absorbers. DampRid takes 5 rows; it is a consumable line under C2(e) and R-35, and its formats are variants.
- **move_kind (2):**
  - Dyson Purifier Hot+Cool goes to the air purifier (tree precedence).
  - Vornado Transom goes to the window fan. This move waits until the new kind is attested.
- **drop (8):** names that only restate the kind or an attribute: Downflow Fan Heater, Halogen Heater, Quartz Tube Heater, Infrarot-Bildheizkörper, Pedestal Air Circulator Fan, Mini Portable Dehumidifier, the Megahome stainless steel distiller, and Side of Pole Mount.
- No named form is a maker or a shop. The owner role holds: every form is a model owned by a maker, and there are 99 makers.

## Task 3: navigation
**I confirm R-116:** the way in is the job (heat, cool, fans and ventilation, treat air, hot water, water treatment, bathroom, solar and power), then the device type.
- Every harvested catalogue divides by job and then type: Screwfix (central heating > boilers, heat pumps, underfloor), Kakaku (heaters, fans, aircon by form), the Solar Store (panels, inverters, charge controllers, storage, kits, metering), Wickes, City Plumbing and Navien.
- Makers enter only through models: 265 forms across 99 makers, concentrated in a few kinds (Washlet seats 23, circulators 15, inverters 13).
- Brand pages turn up only in solar and water treatment (Victron, Waterdrop, Sun-Mar collections). That supports the brand filter in solar, not a brand entry point.

View:
1. **Level 1, the 11 groups:** Heating; Heat pumps and air conditioning; Fans and ventilation; Air purifiers, humidifiers and dehumidifiers; Thermostats and controls; Water heating; Water treatment; Baths, showers, toilets and basins; Hot tubs and saunas; Solar panels, inverters and batteries; Filters, salt and spare parts.
2. **Level 2, the kinds by form or heat source.** For example, Fans and ventilation has desk, stationary, tower, wall or clip, handheld, box, window, circulator, ceiling, extractor and ventilation unit.
3. **Level 3, size, then efficiency:** BTU or kW, tatami, litres, pints per day, kWh. Named forms come next, with the brand filter in solar and the OEM view for mini-splits.

## Rules applied
R-58, C2(b), (d) and (e), C3, C10, C11, C12, S3 and S3b, CV-17, K-157, K-175, K-186, B-24, B-26, B-33, B7-O1, R-35, R-70a and R-116. Memo section 14 was left as decided.

## Resting on † claims
- The swim spa, soft-sided and in-ground hot tubs rest on a guide page only. The C2 pool boundary for the swim spa still needs checking.
- The ReLaLa and Daiseikai lines rest on product knowledge beyond the row notes.
- The ozone generator was seen only in a search excerpt.
- The four new solar and battery kinds cite collection-list pages, where the harvester did not say which page showed which type.
