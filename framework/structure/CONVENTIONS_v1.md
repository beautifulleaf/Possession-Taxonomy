# Shared conventions v1

**Status.** Binding for every category from stage 2 on. Decided 2026-10-17 by Claude on the owner's delegation (BRIEF.md, "Owner decisions on stage 2"; decisions CV-1 to CV-46 in framework/structure/decisions/D1_shared_and_framework.md). The owner may overturn any of them; until then they bind like owner decisions. This file supersedes framework/structure/_conventions.md. The placement key is framework/CATEGORIES_v0_7.md.

**Two owner rules govern every convention below.**
- **Depth and breadth.** Maker ledgers, lines, named forms, variants and registers have no per-category cap. They are seeded from attested catalogues, databases, registries and community wikis and grow as far as the attested evidence goes. Makers, artisans, houses, workshops, perfumers and schools are recorded in ledgers off the tree, never as extra kinds. Scene and subculture tags are used wherever communities exist. No boundary decision may drop a maker community.
- **One source proves existence.** One fetched page showing that a thing is or was made or sold (a maker's or shop page, a catalogue, an auction or marketplace listing, a museum or trade record) admits a kind, named form, line, variant, maker or tier scheme. A second source or a second region is never a condition of inclusion; it may only help decide level (kind against named form) or the weight of a tier scheme. Individual objects stay out (C16).

Level names used throughout: category, sub-family, leaf, kind, named form (C5). Every table carries `sources` (one or more fetched URLs; see "Sources and attestation").

---

## C1. Maker ledger

**One ledger for the whole domain.** One row per maker across all categories; a maker's kinds may cross categories.

| Column | Content |
|---|---|
| `maker_id` | stable id |
| `name` | English or Latin-script name |
| `native_name` | name in native script |
| `aliases` | other names (full alias rows live in C9) |
| `maker_class` | one or more values from the class list below (multi-valued) |
| `country`, `place` | where the maker is based |
| `founded`, `ended` | years |
| `status` | active, defunct, revived |
| `parent_id` | group or parent maker |
| `licensor_id` | maker whose licence the row works under, if any |
| `authority_id` | external authority ids (ULAN, Numista, VIAF, ISNI) |
| `scene_tags` | via the C8 tag table (core or adjacent) |
| `price_band` | C4(d) band, computed |
| `sources` | at least one fetched URL |

- `known_for_kinds` is **not stored**: it is derived from the named-form ledger (C2).
- Never maker columns: segment, owned platforms or apps (`platform_ids`: platforms link to their owner through C13), legal class, declared conformity.
- Optional category extension columns: A2 `construction_policy`; A3 `marks` (maker's marks and hallmark notes); A5 `movement_policy`; any category `certifications`.

**`maker_class` values.**
- General: house or manufacture; independent; microbrand; retail own-label; licensee or diffusion; costume or fashion brand; artisan or atelier; supplier (such as a movement, fabric, chip or panel maker); perfumer or composer (a person, so that noses and composers are recorded).
- Vehicles and property: builder (built to order or in small series); converter (builds on another maker's base); kit supplier.
- Health: pharmaceutical company; medical-device manufacturer; supplement brand.
- Software, digital and subscriptions: software publisher; community or foundation project; platform holder; storefront or marketplace (with a `resale` flag); game publisher; type foundry; format steward or standards body; registry operator; network operator; MVNO or reseller; membership body; venue, club or attraction operator; transport operator or association; aggregator; producer; curated-box company.
- Culture and records: publisher; imprint; record label; cartographic publisher; globe maker; artist; print studio or atelier; print publisher; foundry; mint; refiner; banknote and security printer; medallist or engraver; card manufacturer; awards maker; certifier or grader; taxidermy studio.
- Making and growing: breeder or registrant; tannery or mill; smith or forge.
- "Manufacturer-retailer" is not a class (it is a sales channel). Groceries add `supply_role` (JC3).

**Lines table** (a maker's line or collection spanning several kinds; a line inside one kind is a maker-bound named form, C2).

| Column | Content |
|---|---|
| `line_id`, `maker_id`, `name` | |
| `kinds` | kind ids the line spans |
| `line_rank` | the maker's own order of its lines (used for generated ladder views, C7) |
| `built_by_maker_id` | licensed or contract builder of the line |
| `licensor_id` | licensor, if any |
| `years`, `sources` | |

Tier entries for lines are in C4. Brand product lines of everyday consumables (cleaning products, e-liquids, cigarette brands, feed recipes, insecticides) are lines rows, not named forms (C2).

**Maker-relations table.**

| Column | Content |
|---|---|
| `relation_id` | |
| `maker_id` | |
| `other_id` | a maker, line, named form or platform |
| `relation` | OEM (builds for); supplies chip or panel to; board partner of; licensed by; rebrand of; composed by (perfumer or composer of a named form) |
| `scope` | line, named form or range covered |
| `years`, `sources` | |

**School table** (standing, not optional): traditions of makers such as nihonto smiths, luthier schools, puzzle-box workshops or perfumery schools. Columns: `school_id`, `name`, `native_name`, `tradition`, `region`, `years`, `sources`; makers link to it by `school_id` (multi-valued).

**Issuer table** (shared by F3 and F5). Issuing authorities are not makers: `issuer_id`, `name`, `country`, `type` (state, central bank, postal administration, transit authority), `years`, `sources`.

**Admission and growth.**
- One fetched page admits a maker.
- Ledgers are seeded from attested pages, existing catalogues and registries first, and grow without a cap per category.
- Identity and platform makers come first only as an ordering rule for harvesting, never as a limit.
- Retailer own-labels are rows with class "retail own-label".

## C2. Kind, named form and register

**(a) Choice-level test.** A **kind** is the level at which buyers compare quality or makers. A **named form** is a specific design below it, either **maker-bound** (a model or line inside one kind: Levi's 501, Iron Ranger, Speedy, Submariner) or **not maker-bound** (a generic cut, iconic design or traditional variant that many makers make and that buyers ask for by name: penny loafer, Shetland sweater, klompen, furisode, uchiwa, Vienna regulator). The number of makers is not the test; comparison is.

**(b) Never named forms.** Specifications and certifications (attributes); link patterns, motifs and prints (attributes or variants); sizes (attributes, C6); colourways, reference numbers, collaborations and editions (variants, C3); measuring modes, load or size classes, fitting variants, active ingredients and materials (attributes).

**(c) Traditional and regional types** are kinds when a fetched source shows them sold or compared as their own category (sari, kurta, kimono, geta, maang tikka, mangalsutra, jhumka). Otherwise they are non-maker named forms under the nearest generic kind (borla under maang tikka, klompen under clog). Both carry a `region` or `culture` tag and appear in a generated "by tradition" view; neither gets a leaf of its own. C11 and JC1 refine this.

**(d) Lines against named forms.** A maker's line spanning several kinds is a lines row (C1); a line or design inside one kind is a maker-bound named form.

**(e) Consumable brand lines.** Brand product lines of everyday consumables (cleaning products, e-liquids, cigarette brands, feed recipes, insecticides) are ledger lines, not named forms. Fragrances, cigars, teas and wines keep named forms.

**(f) Admission.** Every named form has one attested row (one fetched source). Named forms are harvested in stage 3 and grow without a cap; there is no per-category cap and no "load on demand only" rule.

**(g) Registers.** Large named-form sets (flags, china patterns, cigar vitolas, feed lines and similar) live in registers linked to their kind, not as tree rows, and are uncapped. A register row has the named-form columns.

**Named-form table.**

| Column | Content |
|---|---|
| `named_form_id`, `kind_id`, `name`, `native_name` | |
| `maker_bound` | yes or no |
| `maker_id` | for maker-bound forms |
| `line_id` | if the form belongs to a line |
| `first_year` | first attested year |
| `base_named_form_id` | for converters: the base form built on |
| `licensor_id` | if licensed |
| `licence_class`, `spdx_id` | software and digital forms (a variant may override) |
| `region`, `culture` | tags where relevant |
| `scene_tags` | via C8 |
| `register_id` | when the form sits in a register |
| `sources` | |

## C3. Variant ledger

- One optional schema for the whole domain. A variant is never a level and never a kind.
- Filled wherever a community compares variants (sneakers, denim, watch references, fragrance concentrations and editions, vehicles, electronics configurations, plans), not only in owner-emphasis scenes, and grown without a cap.
- A model or revision is a named form only when shell, display, format, market identity or compatibility makes it a distinct target; otherwise it is a variant.

| Column | Content |
|---|---|
| `variant_id`, `named_form_id` | |
| `variant_code` | maker's style code, lot or reference number |
| `variant_type` | from the list below |
| `partner` | for collaborations and partner builds |
| `year` | |
| `sources` | |

**`variant_type` values:** colourway; material; print; size; reference; retro or re-issue; collaboration; limited edition; generation; trim; model_year; engine; edition; version; plan; licence scope; style; configuration; partner build; regional model; hardware revision; bundle; vintage; bottler edition. `concentration` is added only if the per-category decision H-4 makes fragrance concentration a variant.

**Plan and edition columns** (types plan, edition, version, licence scope): `seat_structure`, `seat_count`, `eligibility`, `term`, `price_model` (free, freemium, one-time, subscription, bundle), `list_price`, `currency`, `price_date`, `annual_price_usd`, allowances (`storage_gb`, `data_gb`, `speed_mbps`, `devices`, `cloud_hours`, `credits_per_period`), `components`, `addon_of`, `status`; a variant may override the named form's `licence_class` and `spdx_id`.

## C4. Tiers, scales and price bands

**(a) Tier entries.** A tier never sits on a kind. It sits on a maker, line, named form, or (under (b)) a variant or plan row, as tier entries:

| Column | Content |
|---|---|
| `tier_entry_id` | |
| `subject_id`, `subject_type` | maker, line, named form, variant or plan |
| `scheme_id` | the scheme (registry below) |
| `value`, `rank` | |
| `direction` | higher is better or lower is better |
| `scope` | the range of a series the entry covers |
| `test_version` | for measured scores |
| `stale_after` | date after which the entry is stale |
| `source_url`, `date` | |
| `disputed` | computed: entries from different sources disagree |

A subject may hold several entries from different sources. A named form does not inherit a maker's tier unless an entry says so.

**(b) Entries on variants and plans.** A tier entry may sit on a variant or plan row when (i) the scheme is the maker's own ladder for one named form (`scheme = maker ladder: <named_form_id>`, with value and `rank`, attested by the maker's page alone, never compared across named forms), or (ii) an external test or score rates that specific version, vintage scores included.

**(c) Scheme registry and the six scale classes.** Every scale is registered once (`scheme_id`, `name`, `owner`, `scale_class`, `steps`, `direction`, `test_version`, `stale_after`, `kinds_served`, `sources`) and typed as one of six classes:

| Class | Stored as |
|---|---|
| (i) spec or certification measured on the object | attribute with its standard named (COSC, EN ISO 20345 class, fill power, metal fineness, 80 PLUS, IP code); never a tier entry |
| (ii) third-party measured score or rank | tier entry, numeric value, `test_version` |
| (iii) editorial or community class (reviewer grades included) | tier entry |
| (iv) maker's own ladder | `line_rank` in the lines table and, optionally, tier entries with `scheme = <maker>` |
| (v) price-defined band | the C4(d) price band only; never a tier |
| (vi) a shop's or platform's own label | dated `platform_tag` (Grailed Core / Grails / Hype; StockX premium); never a tier |

- A maker's own technology or range level is a tier entry with `scheme` = the maker's name.
- Skill or level schemes (player level; "beginner") are allowed as tier entries.

**(d) Price band.** One domain-wide scheme in USD, derived from a dated, sourced list price; a band is never a tier.

| Band (USD) |
|---|
| 0 (free) |
| under 50 |
| 50–150 |
| 150–500 |
| 500–1,500 |
| 1,500–5,000 |
| 5,000–15,000 |
| 15,000–50,000 |
| 50,000–150,000 |
| 150,000–500,000 |
| 500,000–1,500,000 |
| 1,500,000–5,000,000 |
| over 5,000,000 |

- Categories that never reach the upper bands leave them unused. In G2, bands attach only to maker and line rows where objects are factory-built.
- **Recurring and free prices.** The band is computed per variant or plan row from the annualised list price of the plan as sold (all seats, `seat_count` recorded) at a dated USD rate. Promotional first-year prices are recorded but not used. One-time, perpetual, lifetime and multi-year terms count at full price, with the term recorded. Free plans take band "0 (free)". A domain name is banded at the TLD's standard renewal price. A named form's band is that of its cheapest paid plan, with `has_free_plan`.
- Groceries also carry a unit-price band (JC2).

**(e) Entry.** A tier scheme enters the data on one fetched source. A second source or a second region adds weight (it feeds `disputed` and the scheme's weight in views); it is never a condition of entry. A reviewer's grade enters on one source.

## C5. Levels and axes

- (a) Fixed level names: category, sub-family, leaf, kind, named form. At most four levels below the category, the named form counted as one of them.
- (b) A sub-family may skip the leaf level when it holds about 12 kinds or fewer; the kind is then stored with `leaf = null`, never under a dummy leaf.
- (c) One stated axis per level within each sub-family. Each sub-family states the axis of its leaf level in its definition.
- (d) **Parts sub-family.** Every category that receives S3 parts ends with the sub-family "Parts and accessories made for one <object>", leaf axis = object served. It is the only sub-family exempt from the level-1 axis. E2 files its parts there too (no host-leaf exception). J1–J7, G2, C3, C8 and I3 have none.

## C6. Size, fit and user

- Size (garment, shoe, ring and frame size, case diameter, luggage size class and the like) is always an attribute with its standard (ISO 8559-1, ISO 19407, ISO 8653, ISO 8624, airline bands). The luggage size class is the only case decided per category (question A-16, decision file D2).
- **Size against format.** A size class names a kind only when it changes what the object works with, so that one size cannot replace the other without different equipment (film gauge; 16-inch transcription disc; 3-inch Mini-CD), and a fetched source sells the sizes apart. Otherwise size is an attribute (record diameter, paperback trim, urn capacity).
- **User** is always a tag, with generated department views; no leaf name carries a user word. One user list: women, men, unisex, couples, baby, child, bariatric, adapted. "Beginner" is a level scheme (C4), not a user. (The kind of animal served is B10's first axis by a written exception in the key, Appendix A.)

## C7. Order inside a leaf

- Kinds: canonical form first, then the secondary key the sub-family states (spec, height, formality, complexity).
- Named forms: non-maker named forms first, by first-attested year, then alphabetically; then maker-bound named forms, by maker (in ledger `name` order), then first-introduction year, then alphabetically.
- Variants: by `variant_code` or year.
- Maker ladders (`line_rank`), newest-first, spec-ladder and benchmark orders are generated views, not stored order.

## C8. Scene vocabulary

- One controlled, sourced list of scene and subculture tags for the whole domain, used in every domain where communities exist (fashion, fragrance, puzzles, knives, watches, audio, electronics, vehicles and others).
- Tagging at maker, kind and named-form level, without automatic inheritance.
- A tag without a definition source is held back until it has one.

| Table | Columns |
|---|---|
| `scene` | `scene_id`, `name`, `native_name`, `domains`, `definition_source` (style guide, Subculture Wiki page, community wiki), `sources` |
| `scene_tag` | `subject_id`, `subject_type` (maker, kind, named form), `scene_id`, `strength` (core, adjacent), `sources` |

## C9. Alias and homonym table

One table: `term`, `language`, `script`, `target_id`, `relation`, `sources`. Relations: alias; regional name; homonym; marketing name (QLED, Neo QLED); trade mark; genericised name. Labels are English, with a native-script label. Examples: JSK = jumper dress; スカジャン = souvenir jacket; カバーオール = chore coat (JP) but coverall = boiler suit (US); longcase = grandfather clock; wristlet → two targets.

## C10. Rule T: technology, power and retail facets

- Power source, technology and connectivity are attributes. They define a kind only when (a) the placement key names that kind (electric blanket, heat pump), or (b) the technology changes the object's physical form or its installation needs, so that one cannot replace the other without new fittings, and a fetched comparison source tests or ranks the types separately.
- **Retail facets.** A retailer facet becomes a kind only when the object's form differs and a fetched source compares or ranks the types separately.

## C11. Rule R: regional names

- A regional name is a kind only when it names a form that no generic kind in the tree already covers; its kind label is then the generic description, with the regional word as its name or synonym (warm-water toilet seat; kiseru, Japanese long pipe; kotatsu, heated low table).
- Where a generic kind exists, the regional name is a named form under it, tagged with the region (zaisu under floor chair; Yixing under teapot).
- A region never names a sub-family or a leaf.
- **Level tie-break.** A regional or variety name becomes a kind only when fetched sellers in two regions give it its own category and no generic kind covers its form; otherwise it is a named form, and it is still in. Two regions decide level only, never inclusion.

## C12. Rule M: mounting and installation

Mounting defines a kind when (a) the object is made only for that mount and its body differs (pendant against floor lamp; window against split air conditioner), or (b) the mount changes what the object can safely do, as a fetched source states (top-of-stairs gate). When the same body is offered with different fixings (wall or floor safe, built-in or freestanding oven, fitted or loose carpet), mounting is an installation attribute.

## C13. Compatibility ledger

- One ledger for sockets, mounts, battery platforms, cap standards, hive systems, hitch categories, operating systems, stores, console platforms and the like, shared by domain I and D5 (and every other domain). Platforms are never levels.
- An app ecosystem that controls devices is a row with `kinds_served`; the app itself is I1.
- Sensor format and similar measured properties are attributes, not platforms.

| Table | Columns |
|---|---|
| `platform` | `platform_id`, `name`, `owner` (maker or standards body), `platform_type`, `kinds_served`, `standard_ref`, `region`, `introduced`, `status`, `sources`; type extensions such as `flange_mm`, `frame_size`, `bayonet_or_screw` (lens mounts), `media_accepted` (consoles), `subscription` and dated `update_promise` (OS and services) |
| `compatibility_relation` | `from_id` (platform or named form), `relation` (supports; requires; fits; backward compatible with; adapts to through an adapter), `to_id`, `sources` |

- `platform_type` values include: CPU socket; chipset; memory standard; bus; form factor; connector or port; operating system; app or book store; voice assistant; finding network; wireless audio or multi-room system; charging standard; radio service; satellite service; lens mount; flash shoe; light-modifier mount; film format; instant film format; console platform; battery platform; hive system; hitch category; cap standard.
- **`delivery`** is an attribute, never a C13 row, with one list: download; boxed or carrier; app store; web or hosted; self-hosted; portable; stream; physical delivery; entry to a place; network connection.

## C14. Multi-use kinds

A kind used in more than one sub-family or leaf goes, in this order, to: (a) the leaf whose rule or standard defines it; (b) the general leaf of the one family that holds all its uses; (c) a category-level "multi-use" sub-family whose leaf axis is stated. A generated view lists it under each use.

## C15. Toy or real

An object made for play by children that imitates a sport, music or weapon object is E1 when it cannot do the real object's job to that object's own standard (a regulation ball, a tuned instrument, a weapon that can injure). The real object made in a child's size stays in its category (size and user are attributes, C6).

## C16. No individual-item facts; grading-scale registry

- Certificates, condition grades, provenance and serial numbers of one particular object are never stored. The data holds kinds, named forms, variants and the ledgers above only.
- **Grading-scale registry** (condition scales included): `scale_id`, `name`, `owner`, `scale_type` (condition grade; measured spec; platform label; classification: a class a kind or named form belongs to, such as an authenticity or reproduction class, never a grade of one object, R-2), `steps` (values in order), `kinds_served`, `sources`. Examples: eBay condition values, Back Market, KEH, Iosys S to J, WATA and VGA, coin and card grading scales. Kinds link to scales; no grade value is ever stored.

## C17. Jurisdiction ledger, standards and legal classes

- Every legal class goes in one ledger and never becomes a level or a tag on the tree: registration, licence, tax, titling and land-use classes; weapons classes (EU Firearms Directive categories, UK sections, US NFA classes); gambling and tobacco regimes; device class (FDA, EU MDR, NMPA); sale class (Rx, OTC, POM, P, GSL, Japanese classes); cosmetic, quasi-drug or OTC-drug status; protected-species and CITES status.

| Column | Content |
|---|---|
| `subject_id` | kind or named form |
| `jurisdiction`, `scheme`, `class`, `criteria` | |
| `source_url`, `date` | |

- A design standard or voluntary standard an object is built to or meets (ISO 4210, EN 15194, CE design category A–D, BS EN 1647, BS 3632, HUD code, ISO 3533) is the attribute `standard_met`, with the standard named.
- Customs headings are evidence only.
- Neither a legal class nor a standard ever defines a kind or a leaf.

---

## Shared attributes

- **`propulsion`** (domain G): none, towed, muscle, wind, combustion engine, electric motor, hybrid, animal-drawn, with a `primary` flag where two apply.
- **Photographic prints** carry both `process` and `mount_format`.

## Sources and attestation

- Every row in every table carries at least one fetched source (one-source rule above). Search excerpts may locate an item; the attestation source must be a fetched page.
- Every S2 sources TSV carries a `fetch_status` column (full, partial, nav-only, failed), added through a tools/ script. Facts held only in search excerpts go to `S2_<CODE>_excerpts.tsv` and are not attestation.

---

## Groceries (domain J)

**JC1. Standards and designations.** Two tables. `standard`: a measured or legal grading scheme (`standard_id`, `name`, `authority`, `steps`, `sources`), with values attached as (`subject_id`, `standard_id`, `value`). `designation`: a protected or legal name of origin or method (`designation_id`, `name`, `scheme`, `register_id`, `authority`, `sources`); the authority is a consortium or body, never a maker. A designation that binds one kind is a non-maker named form of that kind; one that spans several kinds is a tag. A designation is a kind only under C11, with one written exception: wine and spirit designations (Champagne, Port, Cognac and similar) are kinds.

**JC2. Unit-price band.** Groceries carry `unit_price_band` in USD per kg (solids) or per litre (liquids), from a dated, sourced list price; the bands are set at first data load. J7 also keeps the C4(d) item band per 750 or 700 ml bottle.

**JC3. Supply role.** `maker_class` keeps its C1 values; a multi-valued J column `supply_role` sits beside it: farm or ranch; fishery or aquaculture; grower or marketing body; licensor; processor or packer; curer or smokehouse; cannery; cheesemaker or creamery; affineur; dairy or bottler; egg packing centre; mill; roaster; tea house or estate; winery or estate; négociant; cooperative; distillery; brewery; cider maker; independent bottler; importer or trader; retail own-label. Certifications sit on the named form or product.

**JC4. State, process and pack.** Storage state is an attribute. A preserving process that makes a different product compared on its own may define a level, on that level's stated axis only. A pack that keeps the same product is an attribute; a single-serve pack made for a machine system is a kind, with the system in C13. A quality ladder on the same product is an attribute with its `standard`; a legal name fixing a different composition is a kind.

**JC5. Formed, spread and mixed products** follow the spreads, formed-products and mixed-products sentences of step 3 of the key (CATEGORIES_v0_7.md; decisions K-44, K-45, K-46).

**JC6. Tradition and Culinary links.** One J `tradition` vocabulary; `origin` is the place of production; there is no `cuisine` tag anywhere (J5 included). Every kind, and any named form, designation or variety row that Culinary names, carries `culinary_link` rows: `subject_id`, `target_code` (Culinary kind), `relation` (same product, eaten as, used in), `sources`.

**JC7. Variety table.** One reference table for breeds, cultivars, rice and dried-crop varieties, coffee varietals, tea cultivars and grapes: `variety_id`, `species`, `name` (cultivar, breed or varietal), `native_name`, `holder` (breeder or registrant), `sources`.

---

## Not adopted (omitted from this file)

No CV item was rejected outright. These parts of the proposals were departed from or not chosen, and are left out above:
- **C1 sources** "and a second where available"; **C4(e)** "preferably a second from another region" (CV-10); the domain-H clause "a reviewer's grade needs a second source from another region before entry" (CV-12). Owner one-source rule.
- **CV-5** a stated cap per category and "seed from attested lists only" as a limit; identity and platform makers first kept only as an ordering rule. Owner depth-and-breadth and one-source rules.
- **CV-7** "load on demand only" and the per-category cap on named forms. Owner depth-and-breadth rule.
- **CV-8** variants filled "only where an owner-emphasis scene needs depth". Owner depth-and-breadth rule.
- **CV-3** the school table as optional (it is standing). Owner depth-and-breadth rule.
- **CV-22** the scene vocabulary limited to domains A and D. Owner depth-and-breadth rule.
- **CV-17** the E2 exception that would file parts in host leaves.
- **CV-21** domain D's stored order (maker, `line_rank`, year) and a maker-neutral stored order; both are generated views only.
- **CV-27** two regions as a condition of inclusion (they decide level only).
- **CV-40** a designation exception wider than wine and spirits.
- **CV-43** a `cuisine` tag in J5.
- **CV-9** `concentration` as a variant type, unless decision H-4 makes it one.
