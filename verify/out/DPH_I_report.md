# DPH_I report: domain I structure decisions

Scope: I1 (built), I2 and I3 (not built); 21 single points, the session prompt's items among them. Offline; nothing written to data/ or framework/.

## Counts per decision

| Category | new_kind | attribute | covered | display_only | other_category | noted |
|---|---|---|---|---|---|---|
| I1 (9 rows in kinds.tsv) | 1 | 6 | 0 | 1 | 0 | 1 |
| I2 (6 points, memo notes) | 0 | 2 | 1 | 0 | 0 | 3 |
| I3 (6 points, memo notes) | 0 | 2 | 2 | 0 | 1 | 1 |

There are no merges, splits or named-form moves; DPH_I_moves.tsv has a header only.

## New kinds and renames

- **I1.2.07 Firewall software** (parent I1.2, no leaf). Source: heise Sicherheit, which lists Firewall beside Virenschutz. HV_I1_NK3 must fetch a page showing a standalone firewall program.
- **I2.1.03 becomes "Digital comic or manga file (image-page book)"** (unbuilt; id kept). Any book of image pages goes here whatever its container. EPUB, AZW3 and PDF keep their own homes and are cross-linked. Aliases: manga, webtoon, BD, 漫画, 만화.
- **I3 kind 6 is not renamed.** Live-sport services file under kind 5, using `live_access`.

## Attributes

- **I1:** `bundled_adware` (facet), `security_audit` (facet derived as audit history), `bug_bounty`, `reproducible_builds`, `service_jurisdiction` (comparison only, never a facet, since country never divides a category), `certification_held` (standard_values rows; facet).
- **I2:** `abridgement` (not a facet, since titles are not stored), `font_classification` (facet; values harvested from Monotype).
- **I3:** `live_access` (facet), `audiobook_hours` (plan allowance).

## Needs (19 rows)

- **Schemes:** AV-TEST results and awards (ii), AV-Comparatives (ii), Arena (ii), Subger (iii), Expert Reviews (iii), RootMetrics (ii), Ofcom (ii), Showcase-TV (iii).
- **Standards (class i):** AV-TEST Certified, AV-Comparatives Approved, SOC 2 Type II, ISO/IEC 27001, Library of Congress formats.
- **Platforms (C13):**
  - Operating systems for the I1 platform facet. These are not in PF_1 to PF_4, so they need a PF batch.
  - I2 stores and readers, game item platforms, and blockchains and naming roots.
  - I3 host networks.

## Display groups

G-I1-18 is renamed "Malware and network protection" and gains I1.2.07 once it is attested.

## Other calls

- **Warehouse clubs are OUT** under P4: the value is buying goods at member prices.
- **One-off digital rentals are OUT** as one-off services. This departs from the proposal. Purchases are I2.3.01 with a locker licence.
- **Backup is display only.** It stays in G-I1-15.

## Provisional calls (thin evidence)

- **Firewall:** only a navigation page was fetched. ZoneAlarm (NF-I1.2.01-031, no maker) may be a brand that spans the suite and firewall kinds, so the attestation batch should check it.
- **Abridgement:** one store filter (Audiolibrix).
- **Comic and manga widening:** BookWalker tabs and the memo only.
- **Font seed values:** from memory, until a Monotype page is fetched.
- **Warehouse clubs:** Subger's listing only.
- **Rentals:** my reading of BRIEF step 1.
- **Arena class (ii):** uncertain for a vote-based score.
- **I3 kind 6:** still unattested. It folds into kind 5 if no provider page is found.
