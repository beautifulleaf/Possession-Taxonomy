## I1

- **Firewall software: new_kind I1.2.07** under I1.2 (no leaf; the sub-family now holds 7 kinds). Definition: a program that allows or blocks a computer's or phone's network connections by application, port or address, sold or distributed on its own. A security suite that includes a firewall stays I1.2.01, and a firewall appliance is D1. Attestation (HV_I1_NK3) needs a page that shows a standalone firewall program; heise lists Firewall as its own Sicherheit subcategory. Display: G-I1-18 is renamed "Malware and network protection" and gains I1.2.07. Provisional: the stored named form ZoneAlarm (NF-I1.2.01-031, no maker) may be a brand that spans the suite and firewall kinds, so the attestation batch should check it before any re-filing.
- **Installer-adware flag: attribute** `bundled_adware` (no | yes) on the named form, used as a facet. Scope is the distributor; the date checked goes in notes.
- **Audits: attribute** `security_audit` on the named form, one row per audit with the auditor and year. The audit_history facet (none, one, repeated) is derived from these rows.
- **Bug bounty: attribute** `bug_bounty` (yes | no), not a facet.
- **Open source: covered** by licence_class and spdx_id. **Reproducible builds: attribute** (yes | no), not a facet.
- **Jurisdiction: attribute** `service_jurisdiction` (a country code plus the derived surveillance alliance). It is shown in comparisons only and is never a facet or group (country never divides a category).
- **SOC 2 Type II, ISO/IEC 27001, AV-TEST Certified and AV-Comparatives Approved: class (i) standards.** Each is a standards row, and a product that holds one gets a standard_values row on its named form. They drive the "lab certification held" facet. Scored lab results (AV-TEST points and awards, AV-Comparatives levels and awards) are tier entries under their schemes (DPH_I_needs.tsv).
- **Backup under security at heise: display_only.** It stays in I1.1.2.04 and G-I1-15.
- **Steam browsing: noted.** It confirms job-first navigation.
- **Platform facet:** C13 operating-system rows are needed. PF_1 to PF_4 do not cover them.

## I2

- **Abridgement: attribute** `abridgement` (unabridged | abridged) on the audiobook named form (I2.2.2.01), not a facet. I2 stores formats, not titles, so rows will be rare. The tree builder adds the quality marker "unabridged before abridged" to the audiobook kind's "What makes the best" box. Provisional: the only evidence is one store filter (Audiolibrix).
- **Digital comic or manga file: covered by widening I2.1.03** (id kept). Rename it "Digital comic or manga file (image-page book)". Definition: a book whose pages are drawn or photographed images, read page by page or by vertical scroll (comic, manga, bande dessinée, webtoon), held in any container.
- **Precedence sentence for the build:** a book of image pages is I2.1.03 whatever its container. A scanned document or a fixed-page text book stays I2.1.02, and a reflowing book I2.1.01. The kind stays inside the I2.1 layout-form axis, since "image pages" is a layout form.
- **Named forms of I2.1.03:** comic-specific containers (CBZ, CBR, CB7, CBT, CBA) and store comic formats a fetched page names. EPUB, AZW3 and PDF keep their one home (I2.1.01 or I2.1.02), and the I2.1.03 page cross-links them (display only).
- **Aliases (C9):** manga, webtoon, BD, 漫画 and 만화 point to I2.1.03.
- **Light novels: noted.** They are a genre and are barred; as files they are reflowable e-books (I2.1.01).
- **Font style vocabulary: attribute** `font_classification` (non-exclusive tags on the typeface family), used as a facet. The value list is harvested from Monotype's type styles before any row loads; the seed list in DPH_I_attributes.tsv is provisional.
- **Genre-led shop navigation: noted.** It is not imported; at most it becomes a link field to the separate literary, music and film taxonomies.
- **Evidence thin (Kobo, Audible and Amazon blocked): noted.** The calls rest on the memo and the stage-2 sources.
- **Rentals (from the I3 point):** a time-limited digital rental is a one-off service and is OUT (BRIEF step 1). Purchased films are I2.3.01 with rights_state = locker licence, and rights_state gets no "rental" value.
- **C13 rows needed:** stores and readers (Kindle, Kobo, tolino, Apple Books, Audible, BookWalker), game item platforms, and blockchains and naming roots.
- **Display at build (from the proposal):** level-1 groups are Read, Listen, Watch, View, Create with, Use in a game or platform, and Register, mapped to I2.1 to I2.7.

## I3

- **Sport: covered.** Sport is a genre and divides nothing. A live-sport service (DAZN type) is kind 5, on-demand streaming video subscription, as the memo already places DAZN. **Kind 6 is not renamed.** It stays "Live-TV streaming bundle" for linear channel bundles (vMVPD).
- **live_access attribute:** add `live_access` (on demand | live events | live channels, multi-valued) on the named forms of kinds 5 and 6, used as a facet. This lets live-event services be filtered without a new kind.
- **Kind 6 attestation: noted.** The build's harvest uses the Stiftung Warentest and DSLWEB "TV streaming" segment pages to locate providers. It then attests kind 6 on a fetched provider page (I-17). If none is found, kind 6 folds into kind 5 with live_access = live channels (memo risk).
- **Warehouse clubs: other_category OUT (P4).** A warehouse-club membership's value is buying goods at member prices. The shop entry serves the purchase; the membership itself gives no catalogue, play or place to enjoy. This is like Prime Shipping or a Railcard. A bundle that also gives a catalogue (Prime with Video) stays I3 as the bundle. Provisional: only Subger's listing was seen.
- **Rent or buy, free ad-supported platforms: covered or OUT.** Digital purchases are I2 (I2.3.01, locker licence). One-off rentals are OUT (a one-off service). Free ad-supported platforms are OUT (the internet as entertainment). A free tier of a paid service is a plan row in band "0 (free)" (C4(d)).
- **audiobook_hours:** add `audiobook_hours` (hours per period) to the C3 plan allowances, beside cloud_hours and credits_per_period. It is stored on the plan row and is not a facet. It serves kinds 1 and 3.
- **Schemes to register at build:** Expert Reviews Mobile Network Awards (iii), RootMetrics (ii), Ofcom complaints (ii), and Showcase-TV scores (iii, low weight). Stiftung Warentest gets no scheme until a graded test is fetched. Maker plan ladders are C4(b)(i) entries on plan rows. Host mobile networks are C13 rows.
- **Display at build (from the proposal):** level 1 promotes the I3.1 medium leaves (Watch, Listen, Read, Play, Classes and wellness, Bundles and creator memberships), then Online services and storage (including kind 17 for display only), Phone and internet, Memberships and passes, and Boxes and clubs. Kind ids are assigned under R-58 from the memo tree, not from these groups.
