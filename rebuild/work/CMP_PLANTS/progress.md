step0 backups done
step1 wikidata name lookup: chunks.json v0 done (apple/pear start); results in wd_results.tsv; query template mk.py, URLs v*.txt (<2000 chars), 9 chunks
step1 chunk v1 done
step2 enumerated: wd_Apple.tsv (245 apple cultivars w/ enwiki, via en.py class-label query). Next classes: pear cultivar, mango cultivar, potato variety, banana cultivar, Orange cultivar, sweet cherry/sour cherry, tomato, citrus, strawberry, plum, peach, avocado, blackberry, olive, fruit cultivar, Capsicum, garlic, Allium; C3: rose, dahlia etc.
step2b wd_other.tsv done (kind|Q|label|year|country, fruit/veg classes). Still to do: rose/dahlia etc for C3, grape variety (table grapes), apple done in wd_Apple.tsv. Then step3 apply script
step2c wd_it.tsv (Italian PDO/PGI confirmed from Wikipedia list), wd_fp.tsv (freshplaza). Next: apply_j4.py
step3 J4 applied via apply_j4.py (idempotent from bak), validate OK; unconfirmed.json holds confirmed/unconfirmed removed names. Next: C3
