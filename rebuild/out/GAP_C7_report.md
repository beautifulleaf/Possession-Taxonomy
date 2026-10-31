# GAP_C7 report (Farm & Forestry Equipment)

validate.py --v3 out/C7.json: OK. Fetches: 5 plus 3 searches (log: rebuild/work/GAP_C7/sources.tsv).

1. Loose models: none in out/C7.json.
2. Coverage lines: all eight kinds with entries now end with one. Seven vintage-tractor kinds: "No complete list exists; follows the maker pages named here", plus a sentence naming the maker pages not read this pass (Ford, Fendt, Hanomag, Eicher, SAME, Lamborghini, Caterpillar, Cletrac, Holt, Cub Cadet). Cream separator gained nl, xg, sel and role origin for De Laval (Wikipedia: de Laval manufactured the first cream separators; the page gives no year).
3. Partial coverage: no "Covers" kinds. The tractor kinds have no whole-space reference (Wikidata has no usable tractor-model class for this); nothing further to read.
4. Report gaps:
- CNH, Kubota, CLAAS, Mahindra: a ranking was fetched (reportprime.com, 2024: Deere 18.0 %, CNH 12.5 %, Kubota 6.9 %, AGCO 6.1 %, Mahindra 5.2 %, CLAAS 3.8 %). Method is not stated and a second vendor names Claas, not Mahindra, in the top five, so the note says "indicative". IndustryWeek 2025 page had no table.
- Fordson Dexta years: the Wikipedia page gives none (two attempts); left blank.
- IH vehicles list (paraphrase only earlier): not retried; searched nothing further, so IH entries stay as in V4.
- Brand register: country and year added for 21 makers from Wikidata items (Deere & Company, AGCO, Alamo Group, GEA, Hanomag, Eicher, Chelyabinsk Tractor Plant, Lely, DeLaval, Horsch, Joskin, Lemken, Landini, Ursus, Väderstad, Pellenc, Kesla, Maschio Gaspardo, Dewulf, Case IH, Reform). About 67 stay name-only: ambiguous labels (Kuhn, Krone, Zetor, Amazone and others returned wrong entities and were rejected).
5. Sections: every tractor entry carries g (maker).
