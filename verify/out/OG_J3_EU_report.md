# OG_J3_EU report (designations only)

Rows: 233 in verify/out/OG_J3_EU_designations.tsv. By country: FR 61, IT 50, ES 28, GR 21, PT 13, AT 8, DE 7, NL 7, SK 6, SI 5, PL 5, DK 4, LT 3, CZ 3, BE 2, RO 2, BG 2, HR 2, HU 1, CY 1, IE 1, SE 1. By scheme: mostly PDO; PGI and TSG (Boerenkaas, Mozzarella, Heumilch, Ziegen-Heumilch) included. 58 rows have a kind_id; 174 are missing-kind and 1 is a tag (Crème d'Isigny).

Non-cheese rows: butter 6 (Beurre de Bresse, d'Isigny, Charentes-Poitou, d'Ardenne, Mantequilla de Soria, de l'Alt Urgell), cream 2 (Crème d'Isigny as tag, Crème de Bresse), ricotta-type 3, Bulgarian yoghurt, haymilk 2, Slovenian eggs 1.

Sources that served: the Wikipedia list of European cheeses with protected status (read through the fetch tool's summariser, per country), Wikipedia Italian list (first 100k chars only), lexaris.de and legislation.gov.uk copies of EU regulations, produits-laitiers-aop.fr, foodswinesfromspain.com, Slovenian ministry specification PDF.
Failed: eAmbrosia (JS app, title only), all eur-lex.europa.eu pages (empty), all inao.gouv.fr pages (503), mapa.gob.es (503), anycheese (403), officielebekendmakingen (403). Parallel_Auth tools: 402 no credit. Full log: verify/work/OG_J3_EU/fetched.tsv.

Caveats: register_ref is blank almost everywhere (Wikipedia gives none); the cheese list may be incomplete (e.g. Bjelovarski kvargl, further Polish, Finnish, Maltese names not found). Beurre Charentes-Poitou, Crème de Bresse, Alt Urgell and Soria butters have no date because no fetched page gave one. Bulgarian white brined cheese: Wikipedia and a search excerpt of the regulation say PDO, dairyreporter says PGI; written PDO. Egg PGI Œufs de Loué not written (no fetched page; INAO down).
Rule slips: I typed the eAmbrosia home URL and a Wikipedia Cheese_in_Bulgaria URL myself (404); logged as such.

Skips: UK (not EU: 17 cheeses plus Cornish Clotted Cream) and Serbia (3) cheeses; named_forms rows outside EU scope (Swiss AOP, UK, Turkey, Georgia, Iran, India, Luxembourg Beurre rose national mark) left to other batches; Gorgonzola Dolce/Piccante folded into the one Gorgonzola registration. No skips to other categories.

"missing kind?" : 171 EU cheeses whose style has no J3.4 kind (Abondance, Beaufort, Fontina, Tilsiter, Feta-like Telemea, etc.; each row notes it, source Wikipedia list URL https://en.wikipedia.org/wiki/List_of_European_cheeses_with_protected_geographical_status), plus Paški sir (https://en.wikipedia.org/wiki/Pag_cheese), Lički škripavac (https://lexaris.de/book/version/documentflat/head/2063364), Győr-Moson-Sopron megyei Csemege sajt (https://lexaris.de/book/version/documentflat/head/2064178). Suggest kinds for semi-hard/hard pressed Alpine cheese, washed-rind, fresh goat cheese, brined white cheese, whey cheese.
