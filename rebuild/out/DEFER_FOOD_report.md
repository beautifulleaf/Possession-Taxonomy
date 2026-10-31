# DEFER_FOOD report (J1 J2 J4 J5 J6 J7 J8 J9 J10)

Tools: Parallel free tier, 24 calls, no rate-limit errors. Backups in rebuild/work/DEFER_FOOD/bak/. All edited files pass validate.py --v3.

**eAmbrosia (J2, J4, J5, J8, J1 meat)**: done. The JS register shell was useless, but the register's own public API (URL printed on the page) returned the whole register (4,022 records, saved as rebuild/work/DEFER_FOOD/gi_register.json). Six new kinds, registered food names only, each sectioned by country with a Complete line: J1 EU protected fresh meat names (189) and meat-product names (211); J2 fish and seafood names (77); J4 fruit, vegetable and cereal names (521); J5 oil names (152, butter excluded); J8 bakery and confectionery names (116). Not added: cheeses, other classes outside these departments, applied/published names.
**J1 online butchers**: done. Delicious and Good Web Guide read; 13 UK suppliers added to Meat box (19 -> 32). Delicious list read only in the excerpt Parallel returned, so not claimed complete.
**J1 halal bodies**: partly done. 8 Australian bodies added to J1_brands.json; the table came back truncated (rows after Halal Certification Authority missing), not claimed complete.
**J2 UK fishmongers**: done as a market-fact list (10 of 10, April 2023) in Fresh & frozen fish.
**J6 India tea regions**: done as market facts (Assam, Darjeeling, Kangra, Karnataka, Munnar; page undated).
**J7 cognac-expert**: done. The All Brands page gave 353 Cognac-tagged houses; Cognac kind 30 -> 353 entries (no owners stated), Complete line updated.
**J7 CRT tequila NOM**: partly. CRT itself is JS-only; Spirited Agave's reproduction of the CRT list (1 Oct 2026, 203 producers, 2,466 brand lines) gave six producer market facts and a coverage note; individual brands not added as entries.
**J7 IDAC cider pdf**: done; seven appellations confirmed, all already placed; coverage note added.
**J8 market pages**: Harry's about 36 % / Jacquet about 15 % (French sliced bread, 2011), Pladis 22.2 % UK biscuits (2023), Haribo 2 % US (2017), Saudi Snack Foods over 45 % (2001) added. Still blocked: kamcity (403, Grocer page gave the figure), Bahlsen 2015 PDF (302 redirect only).
**J10**: Habano vitolas done from the Cuban Cigar Website current-production list (versions added for 9 marques). Pipedia pages for Vauen, Stanwell, Kaywoodie (KB&B) and Dunhill fetched, but no pipe-maker kind exists to hold them, so nothing placed; facts remain in sources.tsv.
**J9**: no deferred lines.
