start: read briefs, structure
step1 done: structure read, register extracted (sel.tsv), fetched wiki T-shirt, Polo, Breton, Jeans, Hoodie, Sweater, Cardigan, Chino. Result: Wikipedia names few originators (Lacoste, Brooks Bros, Ralph Lauren, Levi, Saint James, Armor Lux, Orcival, Champion, Chanel)
step2 done: fetched Wrap_dress LBD Slip_dress Pencil_skirt Poodle_skirt Miniskirt Hot_pants Jumpsuit Aloha_shirt (17 fetches so far)
step3 done: fetched Aran Guernsey FairIsle Lopapeysa Cowichan Sweatshirt Leggings Bodysuit Cargo_pants (26 fetches)
step4 done: fetched Capri Bermuda Tutu Culottes Wedding_dress Western_wear Dress_shirt Shorts Tank_top Football_kit (35 fetches). Next: write build script build_part.py
step5: fetched tails of Miniskirt Jeans Shorts Football_kit Western_wear at offset 100000 (40 fetches). Decisions made per kind in head; next write build_part.py
step6: wrote rebuild/out/A1_parts/TOPS.json from build_part.py+assemble.py+brands_new.py; next validate, fix, report
step7: coordinator correction: restore removed m via data/named_forms.tsv; country rule; tier; empty kinds
step8: fetched McCoys Lot001XX, Edwin wiki(503 1997 Itochu Tokyo), orSlow meadow (105,107), Barbour Radial, ReigningChamp (47 fetches total). named_forms.tsv hits found for 104 of 178 removed m (removed_m.json). Next: searches/fetches for unrecorded pieces, empty kinds wiki fetches, then rebuild with country rule + tier
step9: fetched uniqlo super non-iron, fila heritage page, freddy wrup, wiki Infant_bodysuit, gymshark arrival, N&F Elephant X; empty-kind wiki checks: Blouse(KdW only), Pleat(Fortuny, Havelova-Vanek), Sweater_vest none, Harem(Poiret,Margaine-Lacroix,Bourniche,Hammer), Plus fours(Benjamin Bixby 2008), A-line(Dior 1955, YSL 1958), Skort(Montgomery Ward 1959, Poiret 1911), Cricket none, wrap skirt/cutoffs/tiered none. ~70 fetches total. Next: extend build_part with restored entries + country rule + tier
