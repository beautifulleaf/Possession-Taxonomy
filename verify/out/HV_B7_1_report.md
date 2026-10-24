# HV_B7_1 report (B7.1 Heating, cooling and air)

- Kinds: 41 of 41 attested (HV_B7_1_kinds.tsv). Three rest on partial pages: B7.1.1.11 Infrared heat lamp (Broan 163 infrared bulb heater fixture at Lowes, bulbs sold separately; Walmart heat-lamp page shows only bulbs, so a lamp sold as a heater is not shown cleanly), B7.1.4.06 Deodoriser (Panasonic ziaino air treatment unit, sold to sanitise and deodorise), B7.1.4.07 Ion generator (Kakaku air-cleaner guide lists the type, no product page). None unattested.
- Named forms: 142 (HV_B7_1_named_forms.tsv), all maker-bound; lines: 10 (HV_B7_1_lines.tsv). Makers: 58 (HV_B7_1_makers.tsv), recorded only as owners of a named form or line (owner-only role); 11 reuse existing ids, 47 are new. Country not recorded because no fetched page stated one.
- Catalogues used: Kakaku.com (aircon, heaters, fans, air-cleaner guide) served well for Japanese series; Screwfix category pages served well for UK boilers, heaters, radiators, extractors, heat pumps; Lennox, WaterFurnace, Mitsubishi Comfort, Stovax, Valor, BPC Ventilation, Vornado, Levoit, tado, AprilAire, DampRid as maker or specialist shop pages. The registries in source_catalogues (AHRI, EPREL, MCS, ENERGY STAR) were not fetched. Screwfix subcategory URLs are not exposed on its pages, so ventilation/air-quality sub-types came from other shops.
- Process flag: three Screwfix URLs (heaters cat7230009, oil-filled-radiators cat7230013, stoves cat7230021) were guessed by mistake, returned 404 or an unrelated page, are logged as failed in verify/work/HV_B7_1/fetched.tsv and feed no row. Real URLs were then taken from fetched pages.
- Series that cover several models are in lines (Lennox Elite, Merit, Signature; WaterFurnace 3, 5, 7 Series; Kirigamine; Sentinel; Dyson Purifier; Levoit purifiers). Model codes such as MSZ-GV2226 were not recorded as forms.
- missing kind? candidates (URL):
  - Tube heater (wall-mounted thermostatic tubular heater): https://www.screwfix.com/c/heating-plumbing/heaters/cat831056
  - Oil-free / thermal-fluid electric radiator (30 thermal fluid, 5 oil-free): https://www.screwfix.com/c/heating-plumbing/electric-radiators/cat4840006
  - In-wall / kick-space electric heater: https://www.heatstorm.com/collections/infrared-heaters
  - Window fan and box fan (Vornado Portal, Transom, Model 80): https://vornado.com/collections/circulators-fans
  - Forced-air kerosene or diesel torpedo / construction heater: https://www.walmart.com/c/kp/kerosene-heaters
  - Ozone generator / odour machine (Home Depot listing seen only in search): not fetched
  - Heat recovery extractor fan (12 products, between extractor fan and MVHR): https://www.screwfix.com/c/heating-plumbing/extractor-fans/cat840510
  - Cast iron radiator category: https://www.screwfix.com/c/heating-plumbing/radiators/cat830960
  - Gas stove and electric stove/fire categories: https://www.stovax.com/products/stoves/traditional/wood-stoves-multi-fuel-stoves
