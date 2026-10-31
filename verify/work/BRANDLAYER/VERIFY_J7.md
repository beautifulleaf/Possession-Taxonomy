# VERIFY J7 Wine, Beer & Spirits (lean, Opus fused audit+verify)

**Result:** 1638 brands: quality 121, cultural 877, listed 640; shown false 0. 59 sub-brands moved to alias_merges, 48 generic/heading rows dropped, 29 homonyms renamed with a qualifier (e.g. Pendleton (whisky), Malibu (rum), DeLeón (tequila), Montana (wine)), 92 rows are the same company as a register J7 brand (merge adds aliases).

**Sample (random.seed(7), 15 rows + 3 extra WBC):** all 18 names are on their source page. All 6 WBC rows (Hop Nation, Cervecería Hondureña, Fresh Beer 30 Kilometres, Lovibonds, Hirsch-Brauerei Honer, Tsingtao) match the PDF medal rows. Wikipedia rows had noise: Distillery unidentified (a heading) and Damiana (a generic herb liqueur) were dropped; Oxford Rye and Kryshtal Etalon were moved to aliases of their parent.

**Tiers by script:** a Wikipedia list row counts as cultural only when it links to the brand's own article. A plain row or red link is listed. A link to a parent company makes the row an alias. IWSC trophies and WBC medals are quality. The 6 IWSC/WBC pages behind the other 115 award rows were not re-fetched.

**Retry research (14 fetches, wine gap):** 1855 Bordeaux classification (87 châteaux), list of Champagne houses (49), list of vineyards and wineries (90), Port wine (6 houses), Baijiu (21 brands), South Africa wineries (148), Western Australia wineries (134), South Australia (2), Barossa Valley (15), Georgian wine (region only).

**Regions:** 26 total; 7 renowned: Bordeaux, Champagne, Douro/Porto, Guizhou+Sichuan, Georgia (UNESCO qvevri), Barossa (GI), Mexico/tequila (Consejo Regulador). 19 without renown: most harvest regions cite IWSC/WBC pages, which make no renown statement.

**Next:** sake kura, Rioja/Barolo/Burgundy, Napa/Chile/Argentina lists, Decanter/IWSC wine awards; IWSC spirits pages not re-fetched.
