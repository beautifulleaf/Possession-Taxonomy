# Stage 2 domain review: H Body (H1 to H3)

*Batch S2R_H. Cold, offline review (no web, no git) of memos framework/structure/H1.md, H2.md and H3.md and their sources files verify/out/S2_H1_sources.tsv to S2_H3_sources.tsv. They are checked against BRIEF.md, framework/CATEGORIES_v0_6.md, framework/STAGE2_MEMO_TEMPLATE.md and the draft shared conventions C1 to C13 in framework/structure/_conventions.md. C14 to C17 were added later, from the domain E review, and are cited where they settle a point. The conventions were written after these memos, so each memo is also checked against them, and section 3 lists the changes it needs. This is a reviewer's judgement, not an owner decision. H3 is adult content, so this review keeps the memo's clinical, descriptive register. Severity: **high** = breaks a shared rule (BRIEF, Appendix A or a convention), or would file the same object in two places across many objects; **medium** = one rule break, one contradiction or a clear split; **low** = wording, evidence or tidy-up. Where a point rests on the reviewer's own knowledge and not on a fetched page, it is marked "(reviewer knowledge, needs a fetched source)".*

**Mechanical checks.**
- *Sources match.* H1 cites S1 to S34, and its TSV has 34 rows in the same order (URL key in section 11). H2 cites S1 to S34 with a URL key at the head of section 1, and its TSV has 34 rows. H3 cites S1 to S28 with a URL key in section 1, and its TSV has 28 rows. Every key resolves.
- *Depth and genre.* All three memos recommend at most four levels below the category (sub-family, leaf, kind, named form). None divides by content genre. H3 keeps "AV-star" and "cartoon-theme" replicas off the tree, but files them as variants (finding H3-8).
- *Excerpt labelling.* H1 marks 9 kinds with † (named by the key only) and lists its unusable hosts. H2 marks 4 kinds with † and labels search-only sources (Consumer Reports, UCSF, TGA, a second hearing guide), but it still cites two of them as evidence (H2-8). H3 marks `(unattested)` names and says which ISO 3533 clauses and Tenga lines it saw only in excerpts and did not rely on.
- *Owner interest.* All three put brand depth into named forms and a maker ledger, and none makes the maker a level. None puts a tier on a kind. Retailer price branches (Babeland "Luxury", Hismith "Premium", Douglas "Nischendüfte", Boots "premium beauty") become dated platform tags (C4c) in every memo.

## 1. Verdict table

| Code | Verdict | Top three issues |
|---|---|---|
| H1 Personal Care & Beauty | minor fixes | (1) Fragrance makes the strength class (parfum, EdP, EdT) the kind. One scent then spans several kinds, and the memo has to invent a `scent_id` to join them. The labels' percentage ranges also disagree across sources. (2) Three leaves divide by a modifier: "Baby hygiene" by user, "Heat and powered tools" by power source, and face against body by area, which the memo itself lists as an attribute. Body sunscreen, hand cream, hot brushes and baby wipes would split. (3) The `segment` maker column repeats C1 `maker_class`, C4c platform tags and C8 scenes. The memo calls sun sticks and toner pads kinds in section 7 but treats the format as an attribute in its usability table. Sub-families 8 and 9 have no fetched source at all. |
| H2 Health, Medical & Mobility | needs rework (Vision, Medicines and the testing sub-families only) | (1) Spectacles, which the key names, have no kind. Reading glasses, prescription sunglasses and frames have no home. (2) In Medicines the active ingredient is a named form. This fails for combination products and for an ingredient sold for two uses (diphenhydramine, ibuprofen), and it puts brand products and ingredients side by side at the named-form level. (3) Level 1 mixes health function with substance regime (the cut the memo rejected as candidate B). Pregnancy and fertility tests have two homes (H2.1 Home tests and H2.9 Testing). Sub-styles and specifications (CIC, heavy-duty rollator, "predictive" thermometer) are named forms beside maker models. The proposed `regulatory_status` table should be the C17 jurisdiction ledger. |
| H3 Adult Objects | minor fixes | (1) The H1/H3 line for powered massagers depends on "the maker or retailer". When they disagree (a wand sold as a personal massager by its maker and as a vibrator by specialist shops), the object has two homes. (2) Level 1 mixes power (A vibrates, B non-powered), body area (C anal, D penis), function (E) and mechanism (F). Vibration is an attribute in C and D but a sub-family test for A against B. So a dildo with a removable bullet, and a hand-held thrusting machine against a thrusting vibrator, split. (3) Worn restraints are split inconsistently: cuffs are H3, but collars go "A1 or A4 by step 17", although step 9 runs first. The "strap-on dildo" kind duplicates the "harness compatible" attribute. Character replicas are filed as variants with no parent named form. |

## 2. Findings by memo

Each finding gives its severity, the memo, the evidence and an exact proposed fix. "Conforms to" names the convention the fix applies.

### H1 Personal Care & Beauty

**H1-1 (high) Fragrance: making the strength class the kind puts one scent under several kinds, and the classes have no common standard.**
- *Evidence.* In section 4b the kinds are parfum or extrait, eau de parfum, eau de toilette, eau de cologne, eau fraîche and solid perfume. Section 6 admits that "the same scent is sold under several strength labels [S9][S29]" and adds a `scent_id` so that "sister strengths of the same scent" can be joined. In the section 5 table four sources give ranges that do not overlap (EdP 10–14 % at Douglas [S9], 15–25 % at Fourth Sense [S25]), and Douglas puts "EdP Intense" above 20 %, which is the parfum range under an EdP name. Wikipedia: "various sources differ considerably" [S26]. The memo's choice-level argument is price ("the higher the oil concentration, the higher the price tag" [S29]), not comparison. Its own evidence shows that buyers compare at the scent: Fragrances of the World and Fragrantica key every entry by house and scent [S28][S30], and the Douglas niche view lists scents [S10].
- *Objects that would split.* Chanel No. 5 (one named form, or three under parfum, EdP and EdT?); Dior Sauvage EdT, EdP, Parfum and Elixir; any "Eau de Parfum Intense"; Creed Aventus against Aventus Absolu; body mist and hair mist (no kind); attar and perfume oil (no kind).
- *Fix (conforms to C2a, C3, C5b).* Kind = the fragrance format, on one axis. Kinds: alcohol-based fine fragrance (spray or splash); perfume oil (alias attar, C9; a source is needed); solid perfume [S27]; body mist; hair perfume (the last two need sources). That is 12 kinds or fewer, so the leaf is null (C5b), and the leaves "Alcohol-based fine fragrance" and "Other formats" are deleted. Named form = the scent (house plus name), `maker_bound: yes`. Each strength label is a **C3 variant** with a new `variant_type` value `concentration`: the label as printed, plus the source's own percentage range and year. A flanker, which has its own name and formula (Aventus for Her), is its own named form with a field `flanker_of` (a named_form_id). Delete `scent_id`. Owner question 1 becomes this choice, and question 7 is answered: store the printed label and each source's range on the variant.

**H1-2 (high) "Baby hygiene" is a leaf defined by user.**
- *Evidence.* The section 3 table has the leaf "Baby hygiene" in Body, bath and hygiene, and the tree has "Baby hygiene: baby bath †". C6 says that "User ... is always a tag". BRIEF says that baby goods have "no category of their own; each goes to its functional home". The memo is inconsistent with itself: its row 7 files baby shampoo under shampoo with user = baby, and question 8 calls baby a user tag. "Intimate and feminine hygiene" also names a user ("feminine").
- *Objects that would split.* Baby wipes (Bathing and cleansing, or Baby hygiene); baby shampoo; baby lotion; nappy cream; a baby bath seat.
- *Fix (conforms to C6).* Delete "Baby hygiene". Add a function leaf, "Toileting and nappy changing": potty, toilet-training seat, changing mat and nappy (H1 question 5), all with the tag user = baby. Rename "Bath tools" to "Bath equipment" (loofah, bath sponge, baby bath). Baby wipes go under Bathing and cleansing with the user tag. Rename "Intimate and feminine hygiene" to "Intimate and menstrual hygiene".

**H1-3 (medium) A leaf divides tools by power source, and three sub-families mix leaf axes.**
- *Evidence.* Hair care and styling states the leaf axis "job", but its leaves are Wash and condition, Colour and chemical, Styling products, **Heat and powered tools**, **Brushes, combs and accessories** and Hairpieces. Leaves 4 and 5 split the hair tools by power source, an Appendix A modifier (COMMON rule 1; C10 makes power an attribute). Shaving states "method", but its leaves are object roles (razors, blades, preparations, accessories) mixed with methods (trimming, hair removal). Skin care ("Skin tools and devices") and Makeup ("Applicators") each add an object-type leaf beside job or area leaves. Fragrance states two axes ("strength class, then format").
- *Objects that would split.* A hot brush or heated round brush; a heated eyelash curler; a hair clipper (Hair "Heat and powered tools", or Shaving "Trimmers and clippers"); a beard trimmer; a battery facial-cleansing brush (Skin tools, or Cleansing); tweezers (Brows and lashes, Hair removal or Grooming implements); an eyelash curler (Brows and lashes, or Applicators); nail clippers and nail files (Makeup "Nails", or Grooming implements).
- *Fix (conforms to C5c, C10).* Write a two-part axis into each area sub-family's definition: "preparations by job (Makeup: by area coloured); then one final leaf, '<Area> tools and devices', which holds every implement, manual or powered". Hair: merge leaves 4 and 5 into "Hair tools" (hair dryer, flat iron, curling iron, hot brush, hairbrush, comb, plain ties and clips), with power as an attribute. Keep "Hairpieces" as the leaf whose job is to add or replace hair. Shaving: rename it "Shaving and hair removal" with leaf axis "method of removing hair": Blade shaving (razors); Electric shaving and trimming (electric shaver, beard trimmer, hair clipper for any hair, body groomer); Depilation and epilation (wax, depilatory cream, epilator, IPL device, tweezers); Shaving preparations and aftercare (shaving cream, aftershave, beard oil). Blades and refills go to the parts sub-family (X6). Add placement lines: eyelash curlers are "Makeup tools and devices"; nail clippers, files and manicure sets are "Grooming implements" (sub-family 8), and nail polish and artificial nails are Makeup > Nails.

**H1-4 (medium) Face against body is both a sub-family cut and an attribute.**
- *Evidence.* Section 3 lists "area (face or body)" among "Attributes, never levels". Yet Skin care (Douglas "Gesicht" [S4]) and Body, bath and hygiene (body lotion) are separate sub-families, and the kinds are named "face sunscreen" and "face cream". Douglas files sun care both in Gesicht and in Körper [S4][S5]. The FDA skin-care group spans face and "body and hand" [S20].
- *Objects that would split.* Body sunscreen; SPF lip balm; self-tanner; hand cream; foot cream; neck cream; body scrub against face scrub; body serum.
- *Fix.* Skin care holds every leave-on skin-care product for any area, with `area` as an attribute (FDA [S20]). Move "Body and hand care" (body lotion, hand cream, foot cream) into Skin care > Moisturising. Rename the kinds "sunscreen", "face cream / body cream" or "cream", with the area as an attribute. Body, bath and hygiene keeps bathing, deodorants, intimate and menstrual hygiene, toileting and bath equipment.

**H1-5 (medium) Format is an attribute in one place and a kind in another.**
- *Evidence.* Usability row 3 files the TOCOBO sun stick under face sunscreen, with "stick format is an attribute". Section 7 says that "toner pads, sun sticks, sleeping masks [S8] are kinds described generically", and section 10 (C11) repeats this. The tree lists "toner pad [S8]" as a kind. Olive Young treats format (cushion, sheet/patch, stick, pump, tube, wipes) as a facet [S14].
- *Objects that would split.* Sun stick; toner pad; cushion foundation; micellar water against cleansing wipes; sleeping mask.
- *Fix (conforms to C2b, C11).* Write one rule: format (stick, pad, cushion, mist, wipe, roll-on, balm) is the attribute `format`, using Olive Young's vocabulary [S14]. Masks are the one exception, because there the product compared is the mask type (sheet, wash-off, sleeping; Douglas "Tuchmaske" [S8]). Delete "toner pad" as a kind (it becomes toner with format = pad), and correct sections 7 and 10.

**H1-6 (medium) Colour cosmetics against skin care: hybrids have no rule.**
- *Evidence.* Section 7's alias table flags "face mist, setting spray" as a homonym risk (MAC Fix+ sits in Douglas face care [S4]). FDA lists lash and brow serums in eye makeup [S20], while the memo has an "Eye and lip care" leaf in Skin care.
- *Objects that would split.* BB or CC cream; tinted moisturiser; tinted sunscreen; tinted lip balm; primer; setting spray; lash serum.
- *Fix.* Add a sentence to section 9 and to the Makeup definition: "A product that leaves visible colour, or that is applied to prepare or fix makeup (primer, setting spray), is Makeup; a product with no colour is Skin care, whatever it claims. Lash and brow serums are Makeup > Brows and lashes (FDA 03 [S20])."

**H1-7 (medium) The maker column `segment` duplicates C1 `maker_class`, C4c platform tags and C8 scenes.**
- *Evidence.* Section 6 adds `segment` (designer or fashion house, niche, Gulf or Arabian, mass retail, natural or clean, dermocosmetic, professional salon). Section 5 says that segment labels are dated `platform_tag` values, and C1 `maker_class` already has "costume or fashion brand", "licensee or diffusion", "retail own-label" and "independent".
- *Fix (conforms to C1, C4c, C8).* Drop `segment`. Designer or fashion house becomes `maker_class` costume or fashion brand, or licensee where a source says so. Niche becomes a dated `platform_tag` (Douglas Nischendüfte [S10]), plus a C8 scene tag "niche perfumery" once a definition source is fetched. Gulf or Arabian and natural or clean become held-back scene tags (as section 7 already says). Mass retail becomes nothing (the price band covers it). Dermocosmetic becomes a `platform_tag` (Douglas Dermakosmetik [S4][S7]). Professional salon becomes the market modifier on lines. Keep the named-form fields for fragrance (`perfumer`, `year`, `scent_family`, `bottle_designer` [S28]), and make `perfumer` a link to a person table, following the pattern of the optional C1 `school` table.

**H1-8 (medium) Evidence: two sub-families have no fetched source, the tools rest on Wikipedia, and one retailer dominates.**
- *Evidence.* The † kinds are hair dryer, wig, baby bath, electric toothbrush, grooming mirror, bathroom scale, hot-water bottle, massager and pacifier. So sub-families 8 (Grooming implements, mirrors and scales) and 9 (Comfort, warmth and massage) have no fetched page at all: they exist, and have leaf = null, only on the key's word. Of the 11 skin-care kinds, 7 cite S8, one Douglas view. The hair tools rest on Wikipedia [S34] and one ghd listing; the razors on Wikipedia [S31][S32] and one enthusiast guide [S33]. No appliance retailer, no US beauty retailer, and nothing from China, India or the Gulf was fetched.
- *Fix.* Before owner approval, fetch a personal-care-appliance retailer tree (dryers, shavers, toothbrushes, massagers) in two regions, one US beauty retailer tree, one baby-care retailer, a page that names the SPF and PA test standards (ISO 24444 and ISO 24442 by reviewer knowledge; needs a fetched source), and one Gulf or South Asian perfume retailer (for perfume oil and attar). Until then, mark sub-families 8 and 9 as provisional.

**H1-9 (low) "Disposable razor" is not a blade mechanism.** The leaf is ordered "by blade mechanism", but disposable means the whole unit is thrown away, and its head is often a cartridge type. S33's six types leave it out. *Fix:* make `disposable: yes/no` an attribute of the cartridge razor and the single-blade razor, and drop the kind (or define it as "a razor sold to be thrown away whole" and drop it from the mechanism order).

**H1-10 (low) Volume is called a variant.** Section 10 (C3) says "variant ledger used for fragrance volume". Under C6, size is an attribute. *Fix:* volume is an attribute. Price per 100 ml is a derived attribute. The C4d price band uses the USD list price of the reference size, not EUR per litre.

**H1-11 (low) Scene tags need definition sources (C8).** The K-beauty "core/adjacent" tags rest on retail views (Douglas, Boots, Olive Young), which show that the label is used but do not define it. *Fix:* hold back strength values until a definition page is fetched, as the memo already does for Gulf perfumery.

**H1-12 (low) The supplement boundary is not stated.** @cosme files supplements (809) beside beauty [S15], and "beauty from within" collagen is sold in beauty departments. *Fix:* add to section 9: "Supplements sold for skin, hair or nails, including collagen drinks, are H2 (step 2)."

**H1-13 (low) Compatibility rows.** The memo lists cartridge and injector systems. Toothbrush heads, shaver foils and heads, and clipper guards are also maker platforms (reviewer knowledge, needs a fetched source). *Fix:* add them to the C13 ledger only with fetched pages. Give the double-edge blade a `standard_ref` only if a source shows a shared standard.

### H2 Health, Medical & Mobility

**H2-1 (high) Spectacles have no kind.**
- *Evidence.* Step 2 names "spectacles and contact lenses that correct vision". P9 says that "Spectacles that correct vision, including ready-made reading glasses, are H2". Section 4b's Vision row mentions "lens use for glasses". But H2.5 Vision lists only contact lenses, a handheld magnifier and a white cane, and no optician source was fetched. Frames are also a market with identity makers and licensees, which matters for the owner's interest in brand depth.
- *Objects with no home.* Prescription spectacles; ready-made reading glasses; prescription sunglasses (step 2 is tried before step 17, so they are not A4); a spectacle frame sold for glazing; spectacle lenses; AFB's magnifying reading glasses [S24].
- *Fix.* Add to H2.5 Vision, in order: prescription spectacles; ready-made reading glasses; prescription sunglasses; spectacle frame (made for one kind of object, so it follows spectacles under S3); spectacle lens; then magnifiers and contact lenses. Lens design (single-vision, bifocal, progressive), material and coating are attributes. Frame makers enter the maker ledger, with `maker_class` licensee where a source says so. Add the precedence sentence "Frames with plano or no lenses, sold as fashion, are A4." Fetch optician retailer trees in two regions before data entry.

**H2-2 (high) Medicines: the active ingredient as a named form fails for combinations and for ingredients with two uses.**
- *Evidence.* Section 4b: "active ingredient as non-maker-bound form (fexofenadine, acetaminophen, aspirin) ...; brand product as maker-bound form". A named form has one parent kind, and kinds are use classes. Usability row 14 files store-brand ibuprofen as both ("ibuprofen is the non-maker-bound named form; the store brand a maker-bound form"), which needs two named-form levels. Section 7 rejects condition as a level (a view only), yet the Medicines leaves are condition groups (Allergy and sinus; Cough, cold and flu; Pain).
- *Objects that would split.* A diphenhydramine sleep aid (an antihistamine kind or a sleep-aid kind: one ingredient, two homes); a paracetamol-and-caffeine tablet, or a cold-and-flu combination (no single ingredient form); low-dose aspirin (pain, or cardiovascular); ibuprofen gel against ibuprofen tablets.
- *Fix (conforms to C2a).* Kind = the OTC use class as labelled (the U.S. News and Chemist Warehouse categories [S8][S14]). Leaf = the symptom group, and the memo must say that this is the one place where condition is the leaf axis, because medicine aisles are arranged that way [S8][S14]. The active ingredients become a multi-valued attribute `active_ingredients`, with ATC code [S4] and strength. A generated "by ingredient" view then lists one ingredient across every kind. Only maker-bound brand products (and store-brand lines, as retail own-label) are named forms. A product labelled for two uses is filed by the use printed first on the pack. Supplements follow the same pattern: a single-ingredient kind (vitamin D), or the kind "multi-ingredient supplement", with the ingredient list as an attribute. This also settles H2.7 blends, such as joint or "hair, skin and nails" formulas, which the ingredient-class leaf cannot place.

**H2-3 (medium) Level 1 mixes health function with substance regime, and pregnancy and fertility tests have two homes.**
- *Evidence.* Section 3.1 states the level-1 axis as "what the owner uses the object to do for health". But H2.6 to H2.8 are defined by what the object is (medicine, supplement, sports nutrition), which is the regime cut that the memo rejected as candidate B. H2.9 is a life stage, and its leaf axis "stage" does not match its leaves (Testing; Breastfeeding; Contraception). H2.1 has "Home tests" (COVID-19, flu) and "Body temperature", while H2.9 has "Testing" (pregnancy, ovulation), and P1 sends the basal thermometer to H2.9.
- *Objects that would split.* Pregnancy test; ovulation test; fertility monitor; basal-body thermometer; a COVID-19 and flu combination test.
- *Fix (conforms to C5c).* State the level-1 axis as two ordered tests: "(1) a substance taken or applied (medicine, supplement, sports or meal nutrition) is filed by what it is, because pharmacies and health stores sell these in separate departments [S14][S25][S26]; (2) every device, aid or supply is filed by its health function." Move all tests and monitors into H2.1, with a new leaf "Fertility and pregnancy" (pregnancy test, ovulation test, fertility monitor, basal-body thermometer). That keeps H2.1's axis, "quantity measured or condition tested". Rename H2.9 "Contraception and breastfeeding", with leaf axis "purpose" (prevent pregnancy; feed). A "reproductive health" view is generated from tags.

**H2-4 (medium) H2.11 states two leaf axes, and compression goods have two homes.**
- *Evidence.* "Supports, braces and prostheses (leaf axis: body region, then replacement)". The compression stocking sits in H2.2 Therapy devices > Circulation, but the German list groups compression therapy beside bandages and orthoses [S5].
- *Fix.* H2.11 leaf axis = "what the object does to the body part": Support (braces, supports, orthotic insoles, compression garments) and Replacement (prostheses, epitheses, breast prostheses [S5 groups 24, 35–38]). Body region is part of the kind name, or an attribute. Move the compression stocking to H2.11 > Support. Add the boundary line "Compression socks sold for sport or travel with no stated medical class are A1 hosiery (E2 if made for one sport)".

**H2-5 (medium) Generic sub-styles, specifications and measuring modes are named forms beside maker models.**
- *Evidence.* ITE hearing aid [full-shell mb:n; half-shell mb:n]; canal hearing aid [ITC; CIC; IIC mb:n]; rollator [heavy-duty rollator; rollator with forearm rests; Deltarad mb:n], while section 4b says "load class, folding ... are attributes"; electronic thermometer [predictive; actual-measurement mb:n]. Named forms are one level. A maker's CIC model would have to sit under "CIC" and under the canal kind at the same level. C2(b) says that specifications are not named forms. Careco lists the tri-walker as its own type [S21], and "Deltarad" is the German name for that three-wheeled form.
- *Objects that would split.* A maker's CIC model; a bariatric rollator; a three-wheel walker; an infrared forehead thermometer (usability row 2 leaves its form unattested).
- *Fix (conforms to C2a, C2b, C11).* Hearing: keep four style-family kinds (BTE, RIC, ITE, canal), with `shell_style` (full-shell, half-shell, ITC, CIC, IIC) as an attribute. Only maker models are named forms. Rollator: load rating and forearm supports are attributes. Add the kind "tri-walker" [S21], with the alias Deltarad (C9, C11). Thermometer: kinds by measuring site where the form differs (stick, ear, forehead), once a fetched source attests them; "predictive" against "actual-measurement" is an attribute.

**H2-6 (medium) Contact-lens replacement schedule is used as the kind.**
- *Evidence.* The kinds are "monthly contact lens" and "daily contact lens". Alensa shows the schedule as a facet [S20], and VisionPros mixes it into one "type" list [S19]. A maker's lens family is sold in several schedules, so the named form would sit under more than one kind. Rigid gas-permeable, orthokeratology and scleral lenses, which differ in form, are missing.
- *Fix (conforms to C2b).* Kinds by lens form: soft contact lens; rigid gas-permeable lens; orthokeratology lens; scleral lens (the last three need fetched sources). Schedule, correction type, material and pack size are attributes. Lens families are maker-bound named forms. Do the same for H1 formats (H1-5): a retail facet becomes a kind only when the form differs (X8).

**H2-7 (medium) Legal classes belong in the C17 jurisdiction ledger, not in attributes or a new table.**
- *Evidence.* Section 5.2 proposes a `regulatory_status` table, and section 10 lists supply class (OTC or prescription), FDA, EU and NMPA device class, POM, P or GSL, the Japanese drug classes and the UK scooter class as attributes. C17 now defines one ledger (`subject_id`, `jurisdiction`, `scheme`, `class`, `criteria`, `source_url`, `date`) and says "Never a level or a tag on the tree".
- *Fix (conforms to C17, C4b).* Rename the table to the C17 ledger and move every legal class above into it. Usability rows 7 and 9 ("attribute UK class 3", "attribute supply class OTC") become ledger rows. Generate the view "no prescription needed" from the ledger. Voluntary product standards (BS 8599-1 size, ANSI/ISEA Z308.1 class and type, DIN 13157/13169/13164) stay attributes with the standard named (C4b). The blood-pressure "validated" attribute must name the validation list or protocol. Owner question Q5 then leaves the owner queue as "adopt C17".

**H2-8 (medium) Evidence: two structural claims rest on unfetched pages, and some branches rest on one region or one page.**
- *Evidence.* Section 4b's mobility row cites "Consumer Reports tests rollators as one product class (search; not fetched)". Section 8 cites "a second guide in search results, not fetched" for the hearing-aid order. Reproductive goods rest on Canadian pages only [S32][S33], plus the elided Chemist Warehouse tree. Medicines rest on U.S. News [S8] and a Japanese regulator list [S17]. China enters only through a consultancy summary [S13]. The three glucose-monitor kinds rest on one blog [S23]. The breast-pump kinds rest on retailer facets [S32], not on the separate comparison that C10(b) asks for.
- *Fix.* Remove the two excerpt citations from the evidence columns, or fetch the pages. Fetch a pharmacy tree in a second region for medicines, a second source for the glucose-monitor types, and a breast-pump comparison. Under C10(b), manual against electric breast pump becomes an attribute (the shield and bottle are the same), and only the wearable pump, whose form differs, stays a kind, unless a fetched comparison ranks them separately.

**H2-9 (medium) A first-aid kit made for a car splits with G1 under S3.**
- *Evidence.* DIN 13164 is the car kit standard [S28]. S3 sends an object "made to be fitted to or used up in one kind of object" to that object's category (a child car seat goes to G1), and a car kit is made for one kind of vehicle.
- *Fix.* Add to section 9, and log in _framework_conflicts.md: "First-aid kits are H2 whatever vehicle, workplace or place they are made for; the standard (DIN 13164, BS 8599-2 for vehicles if sourced) is an attribute."

**H2-10 (medium) Coloured non-corrective contact lenses have three possible homes.**
- *Evidence.* P4 and Q8 send them to H1 as "a cosmetic attached to the body", but H1 has no such kind. Step 17's A3 branch ("an ornament worn on the body") is tried before step 18, so it could also take them. Reviewer knowledge (needs a fetched source): US and EU rules treat decorative lenses as medical devices, and they come from the same makers, with the same schedules, as corrective lenses.
- *Fix.* This is an owner choice (section 5). The recommendation is H2 Vision > soft contact lens, with `corrective: no`. This needs a key note ("contact lenses of every kind, corrective or not, are H2"), logged in _framework_conflicts.md. Otherwise H1 must add the kind "cosmetic contact lens" under Makeup > Eyes, and the A3 branch must exclude it.

**H2-11 (low) Kinds that the key or the neighbouring memos send to H2 are missing.** Medical-condition infant formula (Q3); restorative tonics (essence of chicken; step 2 note); the condom (†, but H3's Babeland "Condoms + Barriers" [H3 S2], Bestvibe [H3 S6] and Pleasure Point [H3 S9] attest it); dental dams; pelvic-floor trainers and vacuum erection devices (H3 section 9.3); vaginal dilators (H3's "Dilatoren" homonym); breast prostheses and packers (S5 group 37; H3 question 4); stoma articles (S5 group 29); nursing pads and nipple cream; teething gel. *Fix:* give each a kind, or a precedence line naming its home (X5).

**H2-12 (low) Maker ledger.** `platforms_owned` repeats the C13 ledger (derive it from that ledger). The new `maker_class` values (pharmaceutical company, medical-device manufacturer, supplement brand) should be added to the C1 list for all categories, not just this one (X1).

**H2-13 (low) Pressure-relief cushions and knee walkers have two homes.** "Wheelchair cushion" is a part in H2.12, while pressure care is a leaf in H2.4 (S5 group 11). Careco lists knee walkers among walking aids [S21], but they are wheeled. *Fix:* pressure-relief cushions are H2.4 Bed and pressure care, and only a cushion shaped for one wheelchair model is a part. The knee walker is H2.3 Walking aids.

**H2-14 (low) Compatibility.** Hearing-aid battery sizes are a shared standard, glucose test strips are tied to one meter, and CGM sensors are tied to their transmitters. All are C13 rows that need fetched sources. The Omron "Connect" app family is a C13 platform, and the app itself is I1 (as H3 already says for toy apps).

### H3 Adult Objects

**H3-1 (high) The H1/H3 test for powered massagers depends on who presents the object.**
- *Evidence.* Section 9.2: "A powered device is H3 when the maker or retailer presents it for sexual stimulation ..., and H1 when it is presented as a muscle or scalp massager". Usability row 1 files the Magic Wand Mini in H3 because specialist shops list it with vibrators [S2][S23]. Customs law calls it a "massage apparatus" [S14], and the museum notes that vibrators are still marketed "solely as massagers" [S15]. When the maker presents a wand as a personal massager and specialist retailers list it as a wand vibrator, "maker or retailer" gives both answers.
- *Objects that would split.* A wand massager sold both ways; a compact "personal massager" from a general electronics brand; a vibrating facial massager listed by an adult retailer; a 1920s electric vibrator (row 20 sends it to H1).
- *Fix.* Write one ordered test, and print the same sentence in H1 section 9 and with the H1 massager kind: "(1) If the maker's own description or packaging names sexual use, or the maker sells the object in its adult range, it is H3. (2) If the maker is silent and a specialist adult retailer files the object among sex toys, it is H3. (3) Otherwise it is H1 (comfort) or H2 (made to treat a condition)." Under (2), wand-type massagers are H3. Antique objects are tested by how they were presented when made, as row 20 does. This applies S5 to the object's designed purpose, not to the owner's motive.

**H3-2 (medium) Level 1 mixes power, body area, function and mechanism, and vibration is an attribute in some sub-families but the test in others.**
- *Evidence.* The section 3 placement test: A "vibrates, pulses or sucks" (power and mechanism); B "non-powered insertable" (power); C "made for anal use" and D "worn on, around or enclosing the penis" (body area, the axis rejected as candidate B); E acts on a partner (function); F "driven by a motor on a frame" (mechanism); G replicates a body. Section 2 calls the axis "designed form-function", but in practice it is an ordered test. C10 makes vibration an attribute of rings and anal toys (breaks 1 and 2), yet vibration is what separates A from B. Adam & Eve says that some dildos "venture into vibrator territory" with inner bullets [S27]. "Realistic vibrator" is a kind in A2, while "realism" is an attribute of dildos in section 4b.
- *Objects that would split.* A dildo with a removable bullet (A2 realistic vibrator, or B dildo); vibrating kegel balls (B kegel balls, or A2 egg vibrator); a dual-density realistic dildo with a motor.
- *Fix (conforms to C5c, C10).* State the level-1 axis as "the designed action family, decided by the ordered placement test of section 9". An ordered test written into the sub-family definitions meets "one stated axis" when it is printed as the axis. Add the C10 sentence: "A motor makes an object a vibrator (A) only when no earlier sub-family in the test takes it. An object whose motor is removable or optional is filed as the object without it, with `vibration: optional`. Kegel balls with a motor stay kegel balls." Define "realistic vibrator" as "a vibrator with an integral motor and a body-shaped shaft", and treat realism as an attribute in B.

**H3-3 (medium) Thrusting objects are split between F and A2, and the definition of F does not fit its own kind.**
- *Evidence.* F is "driven by a motor on a frame", but F lists a "Hand-held thrusting machine (S17 'Capsule')", which has no frame. A2 has "Thrusting vibrator" [S2][S1]. D1 has "Automatic masturbator", and some are sold with a mount or stand.
- *Objects that would split.* A hand-held thrusting toy; an automatic masturbator on a mount; a thrusting machine that takes a masturbator attachment.
- *Fix (conforms to C12, C13).* F = "a machine whose motor drives an interchangeable attachment and which stands or mounts on its own (frame, saddle, base)". A hand-held thrusting object is A2 thrusting vibrator, unless it takes attachments through a C13 connector (KlicLok, 3XLR), in which case it is F. An automatic masturbator stays D1 with or without a stand, because the stand is a mounting attribute (C12).

**H3-4 (medium) The leaf axis of sub-family A mixes where the object acts with mechanism and wearing.**
- *Evidence.* "Where the stimulation is applied (external, internal, dual or worn, suction)". "Worn" is a mounting and "suction" is a mechanism, and air-pulse stimulators are applied externally.
- *Objects that would split.* A wearable air-pulse toy (A3 or A4); a couples vibrator worn during intercourse (A3 couples or A3 wearable kind); a wearable egg (A2 or A3).
- *Fix (conforms to C5c, C12).* Leaves: External; Internal; Dual-contact (made to touch two areas at once: rabbit, couples). Clitoral air-pulse stimulator, wearable (panty) vibrator, wand, palm, bullet, finger and tongue vibrators are External kinds. Being worn and being remote-controlled are attributes. The vulva and nipple pump: see H3-5.

**H3-5 (low) Body area is an attribute for some pumps and a kind for others.** In A4, "Pump target (nipple, vulva) is an attribute", but the penis pump is its own leaf (D3). The breast-type masturbator is a kind, while the "imitated opening" is an attribute. *Fix:* this can stand if the memo states why: D3 is kept for the H2 boundary (vacuum erection devices), and the breast-type masturbator differs in form factor (it is not an enclosure held in the hand). Put both reasons in section 4b, so that a builder does not copy the pattern to other body areas.

**H3-6 (medium) Worn restraints: cuffs are H3, but collars are sent to step 17, which runs after step 9.**
- *Evidence.* Section 9.1: "Collars and leashes (S18) are worn at the neck: A1 or A4 by step 17, owner to confirm." Cuffs, which are also worn, are H3 (E1). Step 9 is tried before step 17, and the only thing step 9 takes out is garments. The Wikipedia list files collars, cuffs and the armbinder under Restraints [S12].
- *Objects that would split.* A collar with a leash ring; an armbinder; a blindfold against a sensory-deprivation hood (E2, or "hoods and masks are fetish wear, A1").
- *Fix.* Add to section 9.1: "A collar, cuff, armbinder or harness made with fixing points to restrain a person is H3 (step 9 before step 17). A collar made only as an ornament is A3. A garment (hood, corset, hobble skirt, latex suit) is A1 under the step 9 note. A blindfold that covers only the eyes is H3 E2." Owner question 1 then asks only about the strap-on harness.

**H3-7 (medium) "Strap-on dildo" repeats an attribute, and strap-on kits have no filing rule.**
- *Evidence.* B has the kinds "Dildo" and "Strap-on dildo". Babeland lists "harness compatible" as a product feature [S2], and Orion lists "for strap-on" (37) among its dildo sub-lists [S1]. Section 3, break 4, sends the harness to A1. A kit sold as harness plus dildo has no rule, and the framework's set rule covers groceries only (step 3).
- *Fix.* Drop "Strap-on dildo" as a kind: it becomes a dildo with `harness_compatible: yes`. A strapless strap-on (no harness) is a kind only once it is sourced. File a harness-plus-dildo kit by its dildo (H3), with the harness listed in a `contents` attribute, under the shared set rule (X11). A harness sold alone is A1.

**H3-8 (medium) Character and performer replicas are not variants, and theme must not become a view.**
- *Evidence.* In section 7, Yasj's AV-star (236) and cartoon-theme (422) replicas [S8] are filed as "Variant (collaboration or licensed likeness, C3)". A C3 variant needs a parent `named_form_id`, but each replica is its own product, not a colourway of a parent. A theme (cartoon, anime) is a content cut, which BRIEF never lets divide a category.
- *Fix (conforms to C2a, C3).* Each replica is a maker-bound named form, with the licensor recorded on its line (`partner` or `licensor_id`) under the masturbator kind its form fits. There is no tag or view by theme. Use C3 only for colourways and editions (FLIP 360 limited hard and soft editions [S25]).

**H3-9 (medium) Evidence is thin outside vibrators, masturbators and anal toys.**
- *Evidence.* The E kinds rest on two UK shops: blindfold, gag, paddle, flogger, crop or whip, tickler [S19 only]; spreader bar, bondage tape, bed restraint set [S18 only]. F rests on one maker (Hismith [S17]). G rests on two retailer pages, with no doll maker, although dolls are the segment with the highest prices and the strongest maker identity, so the maker ledger and price bands are untested there. Other single-source kinds: tongue vibrator [S1], palm vibrator [S13], double-ended dildo [S1], solid body doll [S8], violet wand [S12]. No mainland Chinese source was fetched, although the memo lists the one machine maker as China/US.
- *Fix.* Before approval, fetch a second restraint and impact retailer outside the UK, a second machine maker, a doll maker's catalogue and a second doll retailer. Mark single-source kinds in the tree.

**H3-10 (low) The maker-ledger extensions belong elsewhere.** `app_platform` is a C13 platform row: one app ecosystem serves many products, and the app itself is I1. `iso_3533_declared` belongs on the named form, because conformity is declared per product (the maker-level field can be dropped). Keep `material_policy`. "Pocket Rocket" is marked `mb:n`, but by reviewer knowledge it is one maker's product name used generically (needs a fetched source). Treat it like "Fleshlight": maker-bound, with a C9 alias of relation `genericised name` pointing to the generic kind. Add that relation value to C9.

**H3-11 (low) "Beginner" is not a user value under C6.** C6's user values are gender, child, baby and adapted. *Fix:* record "beginner" or "starter" as a dated `platform_tag` (Babeland [S23]), or as tier entries under a C4 level scheme ("C4 allows a category-specific skill or level scheme"), each with its source.

**H3-12 (low) Derived and order fields.** `body_safe_class` should be computed from `material` using the two-guide scheme [S20][S21], with the scheme named, not typed in by hand. The section 8 order for B and C, "size-neutral by first appearance in retail trees", cannot be reproduced. *Fix:* name one source order (Orion's printed order [S1]).

**H3-13 (low) Items sent to neighbours that do not yet hold them.** Lubricants, massage oil and anal douches go to H1, but H1 has no such kinds. Toy cleaners go to B6. Neither H1 nor H2 places anaesthetic delay sprays (a medicine, H2), arousal gels or edible body products. *Fix:* see X5.

### Usability test: objects two builders would file differently from the memos as written

Each memo's own 20-object table files cleanly, because each memo picked objects its rules cover. The objects below come from the same markets. Two builders reading the memo as written would file them in different places.

| Memo | Object | Home 1 | Home 2 | Finding |
|---|---|---|---|---|
| H1 | Chanel No. 5 (parfum, EdP, EdT) | one named form | three named forms under three kinds | H1-1 |
| H1 | Eau de Parfum Intense | eau de parfum | parfum or extrait (Douglas: over 20 %) | H1-1 |
| H1 | Baby wipes | Body > Bathing and cleansing | Body > Baby hygiene | H1-2 |
| H1 | Hot brush (heated round brush) | Hair > Heat and powered tools | Hair > Brushes, combs and accessories | H1-3 |
| H1 | Hair clipper | Hair > Heat and powered tools | Shaving > Trimmers and clippers | H1-3 |
| H1 | Tweezers | Makeup > Brows and lashes | Shaving > Hair-removal products and devices, or Grooming implements | H1-3 |
| H1 | Eyelash curler | Makeup > Brows and lashes | Makeup > Applicators | H1-3 |
| H1 | Body sunscreen | Skin care > Sun protection | Body > Body and hand care | H1-4 |
| H1 | Hand cream | Body > Body and hand care | Skin care > Moisturising | H1-4 |
| H1 | Toner pad / sun stick | own kind (sections 7, 10) | toner / sunscreen with a format attribute (row 3) | H1-5 |
| H1 | BB cream; tinted lip balm; primer | Skin care | Makeup | H1-6 |
| H1 | Lash serum | Skin care > Eye and lip care | Makeup > Brows and lashes (FDA 03) | H1-6 |
| H1 | Gillette disposable razor | disposable razor | cartridge razor | H1-9 |
| H2 | Pregnancy test | H2.1 Home tests | H2.9 Testing | H2-3 |
| H2 | Basal-body thermometer | H2.1 Body temperature | H2.9 (P1) | H2-3 |
| H2 | Diphenhydramine sleep aid | oral antihistamine kind | a sleep-aid kind | H2-2 |
| H2 | Paracetamol-and-caffeine tablet | oral analgesic, named form = ? | no single-ingredient named form | H2-2 |
| H2 | A maker's CIC hearing-aid model | named form under canal hearing aid | under the named form "CIC" | H2-5 |
| H2 | Three-wheel walker | rollator, named form "Deltarad" | its own kind (Careco tri-walker) | H2-5 |
| H2 | One lens family sold daily and monthly | daily contact lens | monthly contact lens | H2-6 |
| H2 | Prescription sunglasses; ready-made reading glasses | (no kind in H2) | A4 eyewear | H2-1 |
| H2 | DIN 13164 car first-aid kit | H2.10 Kits | G1 under S3 | H2-9 |
| H2 | Coloured plano contact lens | H1 (P4) | A3 (step 17 runs first), or H2 | H2-10 |
| H2 | Compression stocking | H2.2 Circulation | H2.11 supports; A1 hosiery | H2-4 |
| H2 | Pressure-relief wheelchair cushion | H2.4 Bed and pressure care | H2.12 Wheelchair parts | H2-13 |
| H3 | Wand massager presented both ways | H3 A1 Wand vibrator | H1 massager | H3-1 |
| H3 | Dildo with a removable bullet | A2 Realistic vibrator | B Dildo | H3-2 |
| H3 | Vibrating kegel balls | B Kegel balls | A2 Egg vibrator | H3-2 |
| H3 | Hand-held thrusting toy | F Hand-held thrusting machine | A2 Thrusting vibrator | H3-3 |
| H3 | Automatic masturbator on a mount | D1 Automatic masturbator | F Sex machines | H3-3 |
| H3 | Wearable air-pulse toy | A3 Wearable vibrator | A4 Clitoral air-pulse stimulator | H3-4 |
| H3 | Collar with a leash ring | E1 Restraints (step 9) | A1 or A4 (memo: step 17) | H3-6 |
| H3 | Harness-compatible dildo; strap-on kit | B Dildo | B Strap-on dildo; harness A1 | H3-7 |
| H3 | Licensed character replica | variant (memo) | maker-bound named form | H3-8 |

## 3. Conformance to conventions C1 to C13

"Conforms" means no change is needed. Each other cell is the change the memo needs.

| Conv. | H1 | H2 | H3 |
|---|---|---|---|
| **C1** maker ledger | Drop `segment`, and map its values to `maker_class`, `platform_tag` and held-back scene tags (H1-7). Put fragrance lines (Kilian The Liquors) and K-beauty lines in the lines table. Keep `perfumer` etc. on the named form, with `perfumer` linked to a person table. | Drop `platforms_owned` (derive it from C13). Propose the new `maker_class` values to C1 for all categories, not ad hoc (X1). Otherwise conforms. | Drop `app_platform` (C13 row) and maker-level `iso_3533_declared` (named-form attribute). Keep `material_policy` (H3-10). |
| **C2** kind against named form | `maker_bound` is used. Formats (pad, stick) become attributes, not kinds (H1-5). Strength classes become variants, not kinds (H1-1). | Sub-styles, load classes and measuring modes become attributes (H2-5). The active ingredient becomes an attribute, not a named form (H2-2). | Pocket Rocket becomes maker-bound with a genericised alias (H3-10). Replicas become maker-bound named forms (H3-8). Otherwise conforms. |
| **C3** variants | Add `variant_type` = concentration for strength labels (H1-1). Volume is not a variant (H1-10). | Conforms (sparse; hearing-aid generations only). | Replicas are not variants (H3-8). Editions conform. |
| **C4** tier and price | Conforms: no tier, SPF and PA as attributes (name the standards, H1-8), platform tags. The price band must be USD from the reference-size list price (H1-10). | Legal classes move to C17 (H2-7). Hearing-aid technology levels as maker-scheme tier entries conform, but need a fetched source (C4e). | Conforms (body-safe class as an attribute, reviewer tiers held back under C4e, USD bands). "Beginner" goes under a C4 level scheme or a platform tag (H3-11). |
| **C5** levels and axes | Fix the leaf axes: power-source leaf, tools leaves, shaving, the two fragrance axes (H1-3). Leaf = null in three sub-families conforms. Parts go to a parts sub-family (X6). | Restate the level-1 axis as two ordered tests (H2-3). H2.9 and H2.11 each get one leaf axis (H2-3, H2-4). The parts sub-family conforms. | State the ordered placement test as the level-1 axis (H3-2). Fix the A leaf axis (H3-4). Leaf skipping and the parts sub-family conform. |
| **C6** size and user | Remove the "Baby hygiene" and "feminine" leaves (H1-2). Otherwise conforms. | Conforms (children's and bariatric as tags, sizes as attributes). | "Beginner" is not a user value (H3-11). Otherwise conforms. |
| **C7** order | Conforms (routine order, strength order, razor order). The razor order loses "disposable" (H1-9). | Conforms. | Name a source order for B and C (H3-12). Otherwise conforms. |
| **C8** scenes | The K-beauty strength values need a definition source (H1-11). Otherwise conforms. | Conforms (no scenes). | BDSM's definition source is a list of equipment (S12), not a definition. Fetch a definition, or mark it provisional. Otherwise conforms. |
| **C9** aliases | Conforms (13 seed rows, with homonyms). | Conforms (10 rows). Add Deltarad → tri-walker. | Conforms (seed rows). Add the relation value `genericised name` (Fleshlight, Pocket Rocket, Magic Wand used generically). |
| **C10** technology | Hair-tool leaf by power (H1-3). Otherwise conforms (electric toothbrush and shaver named by the key). | Glucose-monitor and breast-pump kinds need the C10(b) comparison source (H2-8). | Vibration is both an attribute and a sub-family test (H3-2). |
| **C11** regional names | Section 7 calls regional innovations kinds, which contradicts row 3 (H1-5). 化粧水 and 乳液 conform. | Deltarad becomes an alias of a generic kind, not a named form (H2-5). Kampo conforms. | Conforms (onahole as alias). |
| **C12** mounting | n/a. | Conforms ("installed" is an attribute). | Conforms (suction base). Apply it to stands for masturbators (H3-3) and to wearing (H3-4). |
| **C13** compatibility | Conforms in intent. Add toothbrush-head and shaver-head rows only with sources (H1-13). | Platforms are named but unsourced. Add Omron Connect, battery sizes, strips and sensors (H2-14). | Conforms (KlicLok, Vac-U-Lock, 3XLR). Add app ecosystems (H3-10). |

C14 to C17 (later conventions): C17 settles H2's `regulatory_status` (H2-7). C14 (multi-use kinds) settles H1 tools that serve several areas (mirrors, nail tools go to the multi-use sub-family 8 under C14(c)). C16 (no individual-item facts) is met by all three.

## 4. Cross-memo consistency

**X1 (medium) Maker ledger: three memos, three sets of extensions.** H1 adds `segment` plus fragrance named-form fields. H2 adds new `maker_class` values and `platforms_owned`. H3 adds `material_policy`, `app_platform` and `iso_3533_declared`.
*Proposed shared schema for domain H:* the C1 core columns, with the C1 `maker_class` list extended for all categories by **pharmaceutical company**, **medical-device manufacturer** and **supplement brand** ("house or manufacture" already covers cosmetics and fragrance houses). Category extensions: H1 none on the maker, with the fragrance named-form fields `perfumer_id`, `year`, `scent_family` and `bottle_designer`; H2 none; H3 `material_policy`, like A2's `construction_policy`. These are never maker columns: segment (it becomes a platform tag, maker class or scene), platforms or apps owned (C13), regime or legal class (C17), and declared conformity (a named-form attribute).

**X2 (high) Legal status and voluntary standards: one rule for all three.** H2 proposes its own table. H1 handles cosmetic against medicine through a precedence sentence that uses "licensed as a medicine". H3 records ISO 3533 conformity and cites a customs heading.
*Proposed:* every legal class goes in the **C17 ledger**: device class (FDA, EU MDR, NMPA), sale class (Rx, OTC, POM, P, GSL, the Japanese classes), cosmetic, quasi-drug or OTC-drug status, and vehicle-type classes such as the UK scooter classes. By reviewer knowledge (needs fetched sources), US sunscreens are OTC drugs, Japan has a quasi-drug class (医薬部外品), and the EU treats sunscreens as cosmetics, so H1 needs C17 rows as much as H2 does. Every voluntary product standard (ISO 3533, BS 8599-1, ANSI/ISEA Z308.1, DIN 13157/13169/13164, the SPF and PA test standards) is an attribute with the standard named (C4b). Customs headings (HTSUS 9019 [H3 S14]) are evidence only and are not stored.

**X3 (high) The H1/H2 line uses legal class on one side and rejects it on the other.** H1 section 9: "a product sold to treat or diagnose a named condition, *or licensed as a medicine*, is H2". H2 P15: "A product is filed by what it is and what it is for, *not by the legal class it holds in one country*". A medicated shampoo, a benzoyl-peroxide acne wash or a hydrocortisone cream is licensed in some markets and not in others.
*Proposed shared sentence (both memos):* "A product is H2 when its labelled main purpose is to treat, relieve or prevent a named condition, or when it contains an active ingredient sold only as a medicine in every sourced jurisdiction. Cosmetic purposes (clean, perfume, change appearance, protect, keep in good condition, correct body odour [H1 S21]) are H1, sunscreens and anti-dandruff and anti-blemish products included. Legal status goes to C17 and does not move the object." Owner question 11.

**X4 (high) Massagers: three categories, two of them unsourced.** H1 has "massager †" (comfort). H2 sends TENS units and devices that treat a condition to H2 (P3). H3 uses a presentation test (H3-1).
*Proposed shared sentence (all three memos):* "A powered massager is H3 under the H3-1 test; otherwise it is H2 when made to treat a condition (TENS, EMS units sold for pain), and H1 for comfort, including percussion and neck massagers." Heat packs and hot-water bottles are H1 (key). A heat wrap with a stated pain claim follows the X3 sentence.

**X5 (high) Intimate, menstrual and body-replacement goods are named by one memo and held by none.**

| Object | Sent by | Proposed home | Memo that must add the kind |
|---|---|---|---|
| Personal lubricant; massage oil | H3 9.2; H2 Q6 open | H1 Body, bath and hygiene > Intimate and menstrual hygiene (lubricant), Skin care (massage oil); device or medicine status in C17 | H1 |
| Anal douche or enema bulb | H3 9.2 | H1 Intimate hygiene; a medicinal enema is H2 Medicines | H1, H2 |
| Intimate wash | H1 9 | H1 Intimate hygiene | conforms |
| Menstrual pad, tampon, menstrual cup | H1 Q5; H3 S9 lists cups | H1 Intimate and menstrual hygiene | H1 |
| Period underwear | (none) | A1 (step 17, a garment) | A1 boundary line in H1 |
| Nappy (baby) / incontinence product | H1 Q5; H2 H2.4 | nappy H1 Toileting (H1-2); incontinence product H2 (key) | H1 |
| Condom; dental dam | key; H3 9.3 | H2.9 Contraception; attest with H3 S2, S6, S9 | H2 |
| Pelvic-floor trainer; vacuum erection device; ED ring | H3 9.3 | H2 when the maker states a medical purpose, otherwise H3 | H2 |
| Vaginal dilator / Orion "Dilatoren" | H3 C9 | H2 if medical (sourced); otherwise left unplaced (H3 Q9) | H2 |
| Packer; breast form; wig | H3 9.3; H2 P3 | owner question 8: H1 with wigs, or H2 with prostheses (S5 groups 34 and 37 list hair replacement and breast prostheses as aids) | H1 or H2 |
| Coloured plano contact lens | H2 P4 | H2-10 | H2 or H1 |
| Contact-lens solution | H1 9; H2 Q7 | H2 under S3 (both memos agree) | H2 kind |
| Collagen and other beauty supplements | (none) | H2.7 | H1 boundary line (H1-12) |
| Nursing pads; nipple cream | (none) | H2.9 Breastfeeding | H2 |
| Teething gel | (none) | H2 Medicines (pacifier and teether stay H1) | H2 |
| Delay spray; arousal gel | (none) | delay spray H2 Medicines (anaesthetic); arousal gel under the X3 sentence | H2, H1 |

**X6 (medium) Parts: H1 makes them a leaf, H2 and H3 make them a sub-family.** H1 puts "Blades and refills" inside Shaving, and leaves toothbrush heads and shaver foils unplaced. H2.12 and H3 H use a final "Parts and accessories made for one <object>" sub-family, exempt from the level-1 axis (C5d, which is written for domain A).
*Proposed:* domain H follows C5(d). Each category ends with "Parts and accessories made for one <object>", leaf axis = object served. H1's sub-family takes cartridge refills, double-edge blades, shaver foils and heads, toothbrush heads, clipper guards and hair-dryer attachments. Extend C5(d) to "each category in domains A and H". If the owner prefers parts beside their device in H1, H2 and H3 should change to match, so that the three agree.

**X7 (medium) Non-maker named forms are used for attributes.** H2 uses them for sub-styles, load classes, measuring modes and ingredients (H2-2, H2-5), and H3 for a genericised brand (H3-10). H1 uses none.
*Proposed test (all H memos):* a non-maker named form is a design that many makers make and that buyers ask for by name (C2a: penny loafer, Vienna regulator). A measuring mode, load or size class, sub-style that is a fitting variant, active ingredient or material is an attribute.

**X8 (medium) Retail facets turned into kinds.** H1 turns formats into kinds (H1-5), and H2 turns the lens schedule into kinds (H2-6). H3 correctly keeps NLS's weight classes as attributes [H3 S4].
*Proposed test:* a retailer facet becomes a kind only when the object's form differs and a fetched source compares or ranks the types separately (the C10(b) wording, applied to all facets).

**X9 (low) One user vocabulary and department views.** All three use generated department views: H1 men's grooming and baby; H2 children's and bariatric; H3 women, men, couples, gay men, adapted and beginner.
*Proposed:* one user list for domain H (women, men, unisex, couples, baby, child, bariatric, adapted), tagged on kinds or named forms. Generated views come from it, and no leaf name carries a user word (H1-2). "Beginner" is a level scheme, not a user (H3-11).

**X10 (low) Platforms and apps.** H1 has cartridge systems, H2 Omron parts and Connect apps, and H3 machine connectors and app control. *Proposed:* an app ecosystem that controls devices (Omron Connect, toy-control apps) is a C13 row with `kinds_served`, the app itself is I1, and both H2 and H3 say so.

**X11 (medium) Sets and kits need one rule.** H1 Q4 asks the question. H3 files a plug set by its plug and has no rule for harness-plus-dildo kits (H3-7). H2 treats the first-aid kit as a kind. The framework's only set rule is the grocery one (step 3: the item of greatest value).
*Proposed shared sentence (log in _framework_conflicts.md):* "A set of objects of one kind is filed as that kind. A mixed set is filed by its item of greatest value, with its contents listed. A kit that is sold, standardised and compared as one object (first-aid kit, manicure set, wet-shaving starter kit if sourced) is a kind of its own."

**X12 (low) Boundaries the memos agree on (no change).** Bathroom and body scales are H1 (H1, H2 P2). The electric toothbrush is H1 (H1, H2 on Omron). Wigs are H1 (H1, H2 P3). Contact-lens solution is H2 under S3 (H1, H2). Toy cleaners are B6 and condoms H2 (H3, key). Pacifiers, baby baths, changing mats and potties are H1, and breast pumps H2 (H1, H2). Mobility scooters are H2, not G1 (H2, key). Medical alert bracelets are H2 (H2, key).

**X13 (low) Tier treatment is consistent.** All three choose "preference", with measured attributes, platform tags and sparse tier entries on makers or named forms. *Proposed shared detail:* a maker's own technology or range level (hearing-aid levels, "Premium" machines) is a tier entry with `scheme` = the maker's name. A reviewer's grade (S22 in H3, U.S. News in H2) needs a second source from another region before entry (C4e).

**X14 (low) Scene vocabulary for domain H.** Candidates: BDSM and kink (H3; it also tags A1 fetish wear), wet shaving (H1), K-beauty (H1), niche perfumery (H1). Each needs a definition source under C8, and the domain A list should be extended rather than a new list being started.

## 5. Owner decisions raised (merged and de-duplicated)

Source questions are in brackets. "Rec." is the reviewer's recommendation.

*Scope*
1. Are everyday toiletries and cosmetics that are used up (toothpaste, shampoo, soap) in scope, as step 18 says, although BRIEF names consumables "kept or collected"? Yes / no. Rec. yes. [H1 Q9]
2. Are prescription-only medicines in scope? (a) No; (b) only classes people keep at home (insulin, inhalers, antibiotics, contraceptive pills); (c) all. Rec. (b). [H2 Q1]
3. Named-form admission in domain H: (a) only named forms that are attested and iconic, rated or maker-ledgered, with a cap per category (H1 a few hundred to a few thousand, H3 300 to 600); (b) no cap. Rec. (a). Do supplement kinds enter only from the NIH fact-sheet list plus volume sellers? Yes / no. Do H3's thin sub-families (machines, dolls) need a second maker catalogue before approval? Yes / no. [H1 Q6; H2 Q11; H3 Q8]

*Structure choices*
4. Fragrance kind: (a) strength class as kind (memo); (b) one format kind, with strength as a C3 `concentration` variant of the scent named form and flankers as their own named forms (review H1-1); (c) one kind, with strength as a plain attribute. Rec. (b). Store each source's percentage range on the label? Yes / no. Rec. yes. [H1 Q1, Q7]
5. Fragrance family list shared with B4: Edwards wheel, SFP seven groups, or Perfume Society eight? [H1 Q10]
6. Sun care: a leaf in Skin care covering every area (rec.), or its own sub-family? [H1 Q2; review H1-4]
7. Tools in H1: by the area they serve, with one "tools and devices" leaf per area sub-family and multi-area tools in sub-family 8 (rec.), or one tools sub-family? [H1 Q3; review H1-3]
8. Parts in domain H: a final "Parts and accessories made for one <object>" sub-family in all three categories (rec.; extend C5(d) to domain H), or parts beside their device? [review X6]
9. Medicines depth: kind at the OTC use class, active ingredient as an attribute with ATC code, and named forms only for brand products? Yes (rec.) / no (ingredient as named form, memo). [H2 Q2; review H2-2]
10. Should H2 level 1 be stated as two ordered tests (substances by what they are, then devices by function), with all tests and monitors, including pregnancy and fertility tests, in H2.1? Yes (rec.) / no. [review H2-3]

*Boundaries*
11. H1/H2: adopt the shared sentence X3 (labelled purpose; cosmetic purposes are H1; legal status goes to C17)? Yes / no. [review X3]
12. Massagers: adopt the ordered test H3-1 and X4 (maker names sexual use, or a specialist retailer lists it, so H3; treatment, so H2; comfort, so H1)? Yes / no. [H3 Q2]
13. Lubricants, massage oil, anal douches and intimate washes: H1 (rec.), H2 or H3? Condoms H2 and toy cleaners B6: confirm? [H2 Q6; H3 Q5]
14. Medical-purpose sexual-health items (erectile-dysfunction rings and pumps, pelvic-floor trainers, vaginal dilators): H2 when the maker states a medical purpose, otherwise H3? Yes / no. [H3 Q4, Q9]
15. External body replacements (wigs, breast forms, packers): (a) all H1, like wigs under the key; (b) all H2, like prostheses; (c) wigs H1, the others H2. [H2 P3; H3 Q4; review X5]
16. Harnesses, hoods, corsets and fetish clothing are A1; collars, cuffs and armbinders with fixing points are H3; ornamental collars are A3. Confirm? [H3 Q1; review H3-6]
17. Sex furniture: furniture made to restrain or suspend is H3, positioning cushions B2? Yes / no. [H3 Q3]
18. Sets and kits: adopt the shared set rule X11 (one kind, then item of greatest value, then standard kits as kinds)? Yes / no. [H1 Q4; review X11]
19. Items the key does not name: nappies H1, menstrual products H1, baby wipes H1, cotton pads H1, incontinence products H2 (key). Confirm? [H1 Q5]
20. Baby goods: "baby" is only a user tag, and the "Baby hygiene" leaf becomes a function leaf ("Toileting and nappy changing")? Yes / no. [H1 Q8; review H1-2]
21. Care beds, pressure-relief mattresses and lift recliners: H2 when made for care (rec.), or B1? [H2 Q4]
22. Contact-lens solution: H2 under S3 (rec.), or B6? [H2 Q7]
23. Coloured non-corrective contact lenses: H2 with `corrective: no` (rec.; needs a key note), H1 cosmetic, or A3? [H2 Q8; review H2-10]
24. Spectacles: add prescription spectacles, reading glasses, prescription sunglasses, frames and lenses to H2.5, with plano fashion frames A4? Yes / no. [review H2-1]
25. Therapeutic and diabetic footwear: A2 (rec.) or H2? [H2 Q9]
26. Personal alarms, fall detectors and wandering detectors: H2 or B8? [H2 Q10]
27. Medical and surgical face masks: A1 as PPE (rec.) or H2? [H2 Q13]
28. Infant formula made for a medical condition: its own kind "medical nutrition" in H2.7 or H2.8? [H2 Q3]
29. First-aid kits made for a vehicle: H2 whatever they are made for (rec.; needs a key note against S3)? Yes / no. [review H2-9]

*Data model*
30. Legal classes in the C17 jurisdiction ledger for H1, H2 and H3 (supply class, device class, cosmetic or drug status, scooter class), with voluntary standards as attributes? Yes (rec.) / no. [H2 Q5; review X2]
31. Tier entries from maker schemes (hearing-aid technology levels) and reviewer grades (masturbator grades, maker value tiers) enter only with a second source from another region (C4e). Confirm? Record `iso_3533_declared` per named form? Yes / no. [H2 Q12; H3 Q7]
32. Generated user department views (women, men, couples, unisex, baby, child, bariatric, adapted) from one domain-H user list: wanted? Yes / no. [H3 Q6; review X9]
33. Fetch before approval: an H1 appliance retailer and baby-care source, H2 optician and second-region pharmacy trees, and H3 restraint, machine and doll sources outside the current regions. Required before approval (rec.), or allowed after it? [review H1-8, H2-8, H3-9; H3 Q8]

## 6. Report

H1 needs minor fixes, H2 needs rework in its Vision, Medicines and testing sub-families, and H3 needs minor fixes. The high findings are: fragrance strength as the kind (H1-1); a user leaf (H1-2); spectacles missing (H2-1); the active ingredient as a named form (H2-2); the massager test resting on "maker or retailer" (H3-1); the cosmetic/medicine test, which uses legal class in H1 but rejects it in H2 (X3); and intimate, menstrual and replacement goods that one memo names and none holds (X5). Shared fixes proposed: one domain-H maker-ledger schema (X1); the C17 ledger for every legal class (X2); one parts sub-family pattern (X6); tests for non-maker named forms and for retail facets (X7, X8); and a set rule (X11). There are 33 merged owner questions.
