# Possession Taxonomy — category rebuild brief (schema v2)

You are rebuilding ONE category file of a published taxonomy of everything a person can own. Read first:
- Binding rules: /home/user/Possession-Taxonomy/rebuild/RULES.md (owner-approved; they override anything in the old data).
- This file (schema and method).
- Your category's audit findings in the prompt.
- The current data: /home/user/Possession-Taxonomy/rebuild/reader/<CODE>.json (schema v1: kinds with flat `m` model lists).

## Output (write only into /home/user/Possession-Taxonomy/rebuild/out/; create /home/user/Possession-Taxonomy/rebuild/work/<CODE>/ for scratch)
1. `out/<CODE>.json` — the rebuilt category (schema below). Must pass `python3 /home/user/Possession-Taxonomy/rebuild/validate.py out/<CODE>.json`.
2. `out/<CODE>_brands.json` — `{"b":[brand,…]}` brand-register entries for this category (may be empty).
3. `out/<CODE>_traditions.json` — `{"t":[tradition,…]}` (may be empty).
4. `out/<CODE>_moves.json` — `{"out":[{"to":"<target code>","dept":"<suggested dept>","kind":{…full kind…}}]}` for kinds that the rules move to another category (the receiving category is rebuilt by someone else; just hand the kind over). Use `[]` if none.
5. `out/<CODE>_report.md` — ≤ 300 words: what changed (counts before/after), sources used, anything left undone.
Never edit files outside out/ and work/<CODE>/. Never publish.

## Category JSON (schema v2)
```
{"c":"A5","rev":true,"lead":"One sentence: what this category holds and how it is organised.",
 "b":[{"m":"criterion","v":"scale or ladder (optional)","w":"why/where it comes from"}],
 "depts":[{"n":"Dept name","mode":"variety|tier|mixed","note":"optional one line","b":[…],
   "s":[{"n":"Shelf name","k":[KIND,…]}]}]}
KIND = {"n":"Kind name","a":"aliases · separated","d":"one-sentence definition",
        "t":["type",…] (optional, attribute-level variants that are NOT separate kinds),
        "tg":["baby"] (optional tags; "baby" puts it in the Baby & child view),
        "s":"source URL for the kind",
        "x":[ARCHETYPE,…]  (hobbyist kinds),
        "m":[["model","maker"],…], "r":[["range","maker"],…]  (tier kinds or leftovers; may be omitted)}
ARCHETYPE = {"n":"Name","a":"aliases","d":"one sentence: what defines it",
        "mk":"originating maker/brand/designer (exact brand-register name) or empty for maker-free patterns",
        "y":"year or era","s":"source URL (required)",
        "v":[{"n":"version name or reference","mk":"maker","y":"year","d":"short note"}],
        "dt":"detail axes in words, e.g. 'case 36–41 mm · steel, gold · dial colours'"}
BRAND = {"n":"Name","c":"Country","f":"founding year","seg":"segment label","d":"one sentence",
        "lines":["…"],"eras":["Creative director or period, years"],"sig":["signature archetypes"],
        "sc":["scenes"],"rel":["related brands"],"s":"source URL"}
TRADITION = {"n":"Name","g":"group label (e.g. Woodwork & furniture, Textiles & rugs, Metal & blades, Ceramics & glass, Faith traditions, Food & drink)",
        "r":"region","p":"period","d":"one sentence","tech":"technique","mat":"materials",
        "forms":["signature forms"],"ctr":["centres, workshops, masters"],"auth":"how to tell authentic pieces","s":"source URL"}
```

## Method
1. **Restraint first (tier areas).** Apply the scope rule (drop trade/institutional models; keep the kind with no models only if a person plausibly owns one), dissolve "Other …" catch-alls and attribute-only kinds into `t` types, merge near-duplicates, collapse spare parts to one entry per appliance (except parts hobbies), cut SKU lists to market-covering brands plus independent test winners (≈5–12 per kind). Drop wholesale/SKU noise.
2. **Coverage (variety areas).** Add the missing icons and kinds named in the findings and any others a knowledgeable enthusiast would expect. Organise as kind → archetype → version → detail, ordered by significance (originator, reference versions, then the rest), never alphabetical. Existing models that belong to an archetype become its versions; good existing models with no archetype may stay in `m`.
3. **Brands and traditions.** Put brand facts in the brand register, not in every kind. Archetype `mk` must equal a register name where the brand is in the register. Add tradition entries where artisan traditions matter.
4. **Moves.** Kinds the rules send elsewhere go to `_moves.json`, not into your file.
5. **Sourcing (attestation rule).** Every archetype and every NEW kind needs `s`: a page or dataset record you actually retrieved this session (Wikipedia article, Wikidata entity, maker page, reference database). Prefer bulk/API lookups to cut effort:
   - Wikipedia search API: `curl -s -A "possession-taxonomy/1.0 (noreply@anthropic.com)" "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=<q>&format=json&srlimit=5"`; page check: `…action=query&titles=<T>&format=json&prop=info&inprop=url`; page text: `…action=query&prop=extracts&explaintext=1&titles=<T>&format=json`.
   - Wikidata search: `https://www.wikidata.org/w/api.php?action=wbsearchentities&search=<q>&language=en&format=json&limit=5`; SPARQL: `https://query.wikidata.org/sparql?format=json&query=<urlencoded>`.
   - Other pages: WebFetch, or the Parallel web_fetch/web_search tools if present. Never guess URLs; never record a URL you did not retrieve. If a fetch is blocked, do not work around it.
   Batch lookups in scripts (python3 -I, a polite 0.2 s delay) and keep a work/<CODE>/sources.tsv log (item, url, retrieved date, status).
   Versions and details may come from the archetype's own source page or another retrieved page; if you cannot confirm a version, leave it out.
6. **Validate** with validate.py; fix until it passes. Keep the file under ~400 KB.

## Style
Plain, short definitions (< 25 words). British spelling as in the existing data. Department and shelf names readers would guess. No marketing language.
