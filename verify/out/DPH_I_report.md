# DPH_I report: domain I structure decisions

Scope: I1 (built), I2 and I3 (not built). Inputs were the structure_flags cells in proposals.tsv for I1 to I3, split into 21 single points, plus the items the session prompt named. The pass was offline: no web, no git, and nothing written to data/ or framework/.

## Counts per decision

| Category | new_kind | attribute | covered | display_only | other_category | noted |
|---|---|---|---|---|---|---|
| I1 (9 rows in kinds.tsv) | 1 | 6 | 0 | 1 | 0 | 1 |
| I2 (6 points, memo notes) | 0 | 2 | 1 | 0 | 0 | 3 |
| I3 (6 points, memo notes) | 0 | 2 | 2 | 0 | 1 | 1 |

- **I1 attribute rows:** one of the six (open-source clients and reproducible builds) is partly covered, because open source is already licence_class and spdx_id.
- **I3 covered:** "rent or buy" is covered for purchases (I2.3.01); rentals are OUT.
- **No merges, no splits, no named-form moves.** DPH_I_moves.tsv has a header only.

## New kinds

- **I1.2.07 Firewall software** (parent I1.2, no leaf). The source is the heise Sicherheit page, where Firewall is a subcategory beside Virenschutz. HV_I1_NK3 must fetch a page showing a standalone firewall program.

## Kind renames (unbuilt)

- **I2.1.03 becomes "Digital comic or manga file (image-page book)".** The id is kept. Any book of image pages goes here whatever its container. Generic containers (EPUB, AZW3, PDF) keep their own homes and are cross-linked. Aliases are manga, webtoon, BD, 漫画 and 만화.
- **I3 kind 6 is not renamed.** A live-sport service files under kind 5, using the new `live_access` attribute.

## Attributes (DPH_I_attributes.tsv)

**I1:**
- `bundled_adware`: facet.
- `security_audit`: facet derived as audit history.
- `bug_bounty`.
- `reproducible_builds`.
- `service_jurisdiction`: comparison only, never a facet, since country never divides a category.
- `certification_held`: standard_values rows; facet.

**I2:**
- `abridgement`: not a facet, because titles are not stored.
- `font_classification`: facet, with its values harvested from Monotype.

**I3:**
- `live_access`: facet.
- `audiobook_hours`: a plan allowance in variants.allowances.

## Needs (DPH_I_needs.tsv, 19 rows)

**Schemes:**
- AV-TEST results and AV-TEST Awards (ii).
- AV-Comparatives awards (ii).
- Arena leaderboards (ii).
- Subger picks (iii).
- Expert Reviews network awards (iii).
- RootMetrics (ii).
- Ofcom complaints (ii).
- Showcase-TV (iii).

**Standards (class i):**
- AV-TEST Certified.
- AV-Comparatives Approved.
- SOC 2 Type II.
- ISO/IEC 27001.
- Library of Congress Recommended Formats.

**Platforms (C13):**
- Operating systems for the I1 platform facet. These are not in PF_1 to PF_4, so they need a PF batch.
- I2 stores and readers, game item platforms, and blockchains and naming roots.
- I3 host mobile networks.

## Display groups (DPH_I_groups_changes.tsv)

- G-I1-18 is renamed "Malware and network protection" and gains I1.2.07. Its move waits for attestation.

## Other calls

- **Warehouse clubs are OUT** under P4: the value is buying goods at member prices.
- **One-off digital rentals are OUT** as one-off services. This departs from the proposal's note, which put rentals in I2. Purchases are I2.3.01 with a locker licence.
- **Backup under heise security is display only.** It stays in G-I1-15.
- **Light novels and genre-led store navigation are noted and barred.**

## Provisional calls (thin evidence)

- **Firewall kind:** one navigation page and no product page fetched. ZoneAlarm (NF-I1.2.01-031, no maker) may be a brand that spans the suite and firewall kinds, so the attestation batch should check it before any re-filing.
- **Abridgement:** one store filter (Audiolibrix); Audible and Kobo were blocked.
- **Comic and manga widening:** rests on BookWalker's tabs and the memo. I did not see store comic formats on any fetched page.
- **Font classification seed values:** from general knowledge, until a Monotype page is fetched.
- **Warehouse clubs OUT:** only Subger's listing was seen.
- **Rentals OUT:** my reading of BRIEF step 1. No page was involved.
- **Arena scale class (ii):** a vote-based score, so the class is uncertain.
- **Kind 6:** still unattested. It folds into kind 5 if no provider page is found (memo risk).

Helper: verify/work/DPH_I/write_outputs.py.
