# V4_F6 report — F6 Natural History & Specimens (light pass)

**Result:** validate.py --v3 OK (0 errors, 345 kinds, 1098 archetypes). Backups in rebuild/work/V4_F6/bak/. Fetches: 4.

**Four minerals checked** against the Wikipedia infobox (Strunz code): neptunite 9.EH.05 (phyllosilicate), petalite 9.EF.05 (phyllosilicate), astrophyllite 9.DC.05 (inosilicate), grandidierite 9.AJ.05 (nesosilicate). All four already sit in the right class (Sheet, Sheet, Chain, Single-unit silicates); no move.

**Loose models removed:** 207 `m` entries removed from 87 kinds in every department (examples: Native gold 21, Magnetite 6, Lunar meteorite 8, Trace fossil 8, Element cube 5). They were localities, forms or generic items, not models; the same localities and forms are covered where relevant by the kind's named entries. No ranges (`r`) existed. Their only makers (Luciteria, Van Ingen & Van Ingen) were already in F6_brands.json; no new brands added and no country or year invented.

**Named-entry standard:** all 276 kinds with entries now carry `nl` (one plain sentence per department: a collector occurrence for minerals, a gem variety, a taxon, a named fall or find, and so on) and `sel`. `sel` names the references actually cited by that kind's entries (Handbook of Mineralogy, Wikipedia, minerals.net, GIA, Fossilera, vendor catalogues) and states the scope cut.

**Not achieved:** no single fetched reference lists every occurrence, so the entries are those the cited pages name, not a complete list; `sel` says so. I did not add `xg`/`g` sections (kept the Strunz class, taxon and family structure at section level). Kinds with no entries (e.g. Bornite, Gabbro, Display dome) stay as kinds with no named entries, as commodity or end kinds.

**Market panels:** none, as instructed. `t`, `ax`, `tt`, `see` untouched. F6_brands.json, F6_renames.json, F6_moves.json unchanged.
