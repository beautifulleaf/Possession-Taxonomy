step0 done: read briefs, old J7 depts surveyed (Whisky, Spirits, Liqueurs); plan 8 depts
step1 done: fetched lists (Scotland distilleries, bourbon brands, Irish distilleries, tequilas, Japanese whisky, vodkas, gins, liqueurs, rum producers, Cognac, Armagnac, Calvados, Baijiu, Canadian, Mezcal, Pisco, Shochu, Soju, Aquavit) logged in sources.tsv; next: write build script build_part.py in this dir
step2: scot.txt written (malt distilleries)
step3: lists.py part 1 written (bourbon, irish, japan, canada, grain, tequila, vodka, gin)
step4: lists2.py written (rum, liqueurs, baijiu)
step5: ownmap.txt written (own knowledge map; note unsourced by page except where lists state)
step6: build_part.py part A (whisky, brandy) written; part B (rum, agave, gin/vodka, anise, asian, liqueur, output) pending
step7: build_part.py run OK, SPIRITS.json written (1400 entries); next validate + report
step8 done: validated and report written
audit: started; plan: wikidata SPARQL for ownmap owners, set os, fix craft tier, restore dropped models as versions
audit: wikidata batch gave few clean hits (label collisions, one query Invalid URL); switched to owner groups' Wikipedia pages (Diageo, Pernod Ricard, Bacardi, Campari, Rémy Cointreau, Brown-Forman, Beam Suntory, LVMH) as fetched owner records; logged
audit: owners re-sourced (verified.txt -> os/own_y), tiers recomputed, dropped models restored where maker matches; next validate+report
audit: done; validated, report updated
