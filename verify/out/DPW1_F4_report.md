# DPW1_F4 report (F4 Religious & Ceremonial Objects)

Inputs: the HV_F4_1 "missing kind?" lists, split into 25 items, plus 5 generic types from the fetch log's "gave" column (bon lantern, vajra-and-bell set, dowsing rods, kinpei, and a spice box split from the Havdalah set). There is no DPMK_1_F4 file. Outputs: verify/out/DPW1_F4_kinds.tsv (30 rows) and verify/out/DPW1_F4_moves.tsv (13 rows).

## Task 1: missing kinds
Decisions: new_kind 11, named_form 6, covered 6, attribute 2, other_category 5.

New kinds take the next free id under their parent, checked against data/kinds.tsv and TREE_F4_map.tsv:
- F4.1.1.03 paper-streamer wand [gohei] (kinpei, Rakuten Miyachu)
- F4.1.3.04 miniature stupa (Gandhanra)
- F4.3.1.04 host vessel (ciborium, pyx, host box; HECK)
- F4.3.1.05 ritual washing cup (judaica.com)
- F4.3.1.06 spice box [besamim box] (no logged page, so source_url is empty)
- F4.3.2.05 ritual spoon or ladle (Gandhanra)
- F4.3.4.05 ritual hand drum (damaru), F4.3.4.06 ritual hand cymbals (tingsha): both are F4 only when made for a rite, otherwise E3 (K-110)
- F4.4.3.03 alms box (collection box, tzedakah box, saisen box; HECK)
- F4.5.2.06 dowsing rod (enjoymedia radiesthesia set)
- F4.6.3.03 memorial register [kakocho] (Hasegawa)

The other decisions:
- **Named forms:** phurba (ritual knife), kapala (ritual cup), conch shankha (ritual horn; the definition should read "horn or shell"), host container and tzedakah box (under the new kinds), and bon lantern (ritual lantern; the full Hasegawa fetch shows bon lanterns sold as altar goods, which settles B4-O2).
- **Covered:** kartika is already stored as a named form. Mass set, Havdalah set and vajra-and-bell set are mixed sets filed by their item of greatest value (K-1). Butsuzou is a devotional statue. Islamic "funeral essentials" is a shop category, filed as burial shroud.
- **Attributes:** Thirteen Buddhas is an iconography tag. Pet butsudan is a user tag.
- **Other category:** tallit, tzitzit and kippah go to A1 (religious dress). The brown scapular goes to A3 (worn, by the step 14 charm rule). The Quran stand goes to F1 (S3: a stand made for one object follows it, here a printed text).

## Task 2: named forms (13 of 94 flagged)
- **Drop, 12 rows:**
  - Tijani, Jerrahi and Naqshbandi tasbih: C3 style variants, as memo 3.4 says.
  - Kokka tasbih: kokka is the bead material.
  - Guru Rinpoche and Tara prayer flags: the figure shown is an iconography tag. Gyaltsen Tsenpo: a print or motif.
  - Tefillin: it restates the kind name, so it is an alias.
  - Bukhoor: home-fragrance incense, so B4.
  - Smith-Waite Centennial and Universal Waite: edition or colourway variants of Rider-Waite.
  - Ouija: a genericised trade mark, so a C9 alias. The branded game is E1.
- **to_line, 1 row:** Magnacum Cremation Urns, a collection name, becomes L-memorials-com-magnacum.
- No row is really a maker or a shop. The four Hasegawa lines stand.

## Task 3: navigation
I confirm R-116: the way in is by use or need, with tradition as a front-door filter. Every harvested shop sits inside one tradition and opens on the object: Gandhanra by implement, Judaica.com by object then holiday, HECK by church-supply object, Hasegawa by butsudan, ihai, juzu and incense, MuslimMall by tasbih, rugs and funeral goods, and Memorials.com by urn capacity. The tarot-publisher tab is thin for now: only 2 of the 28 deck rows name a publisher.

The first three levels:
1. Home altars, shrines and sacred images · Prayer and devotion aids · Ritual vessels, implements and sacred scrolls · Lamps, candles, incense and offerings · Tarot, oracle and divination · Funeral and memorial · Fittings. The tradition filter (and the occasion view) sits above these.
2. Leaves, for example Vessels · Hand implements · Text-bearing objects · Sound-makers.
3. Kinds, for example under Vessels: ritual cup · monstrance · ritual food plate · host vessel · washing cup · spice box. Named forms follow, then makers.

## Rules applied
C2(a)–(d), C3, C6, C9, C11, S3, K-1, K-110, K-114, K-117, the step 14 note, B4-O2, R-58, R-70(a), R-116, R-122(c), memo sections 3.4, 9 and 14, and the TREE_F4 precedence rules.

## Decisions resting on † or thin claims
- Ciborium, host container, collection box, washing cup, tzedakah box, offering spoon and stupa rest on the harvester's report for those URLs. The logged "gave" lists do not name them, so HV_NK should confirm each one on its page.
- Spice box has no logged page.
- Gohei rests on reading the Miyachu item "kinpei" as a gold-foil gohei.
- The brown scapular going to A3 is provisional.
- Magnacum as a collection is inferred from its plural product name.
