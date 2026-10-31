# TRAD_RUBRIC notes
- 553 records in 30 files (verify/work/TRAD_RUBRIC/<CAT>.json, "done": true). Helpers in tmp/ (decision tables <CAT>.txt, gen.py, check.py).
- Classes: product 12, both 422, technique 116, use 3 (extra class: kōdō, suiseki, gongshi are use traditions that stay here per rubric question 3, with a product where one exists).
- "exists" was set by hand, then checked against names, aliases and version names in rebuild/out/<CAT>.json (check.py); only identity matches count, not matches to a generic parent kind.
- "as": "version of X" means X is the existing parent kind and the record is an origin or tradition version of it. When exists is true the record is already a kind or version and "as" is informational.
- "src" is the tradition record's own source URL (field "s") for every product record. No separate fetch was done to confirm the page names the product; the Wikipedia or craft-site pages are the tradition's own pages and the product names are those pages' topics or forms.
- Cross-category duplicates: Murano, Bohemian glass, Delftware, Talavera, Wajima, Nambu, Kantha, Aubusson, Gee's Bend, Kumano fude, Yixing, Tokoname, Miki, Sanjo and the Japanese blade towns appear in several categories; each record's "where" is placed in the record's own category (or the cross-category home is named in the note).
- F2 and G2 rule applied: schools, movements, periods, painting and carving traditions and architectural styles are technique; a record is "both" only when the tradition name is itself an object (Netsuke, Ukiyo-e print, Tingatinga, ware names, ibeji, mola) or a house type you can buy (trullo, riad, machiya, hanok).
- Ambiguous cases are flagged "ambiguous": true in the JSON.
