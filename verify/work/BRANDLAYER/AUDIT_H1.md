# AUDIT H1 Personal Care & Beauty (cold audit, 2026-10-31)

Inputs audited together: H1.json (45 rows), H1_trad.json (51), H1_quality.json (61), H1_portfolio.json (97). In total that is 254 rows.

## Accuracy
I sampled 25 rows (random.seed(7)) and fetched each src raw with Parallel web_fetch.
- All 25 names are shown on their src page.
- 3 rows are wrong as recorded:
  - Sundial Brands is a corporate owner.
  - Told London's award was for a candle, which belongs in B4.
  - Kaiak is a fragrance, which belongs in H4.
- 3 rows are only partly supported: the Pure Beauty 2025 page does not say the awards were reader-voted.
- Error rate: 3/25 (12%), or 6/25 if partial support counts.

## Main corrections (drop list)
- **Demote corporate owners to owner notes:** Bajaj Consumer Care, Godrej Consumer Products, Wipro Consumer Care, Honasa, Sundial Brands, CavinKare, KLF Nirmal, Zydus Wellness, Good Glamm Group, Tropical Naturals, Karnataka Soaps & Detergents, Akoma Co-op and CellResearch Corp.
- **Move to H4:** 15 fragrance-only lines from the portfolio files (Kaiak, Frédéric Malle, Issey Miyake Parfums, Kenzo, Loewe, Coty celebrity scents and others) plus Secret Alchemist.
- **Move to H2:** Imedeen, Naturactive, Desitin and Parche Leon.
- **Merge variants:** Uriage Eau Thermale, Eau Thermale Avène, Revlon Colorsilk and Revlon Professional, M·A·C, Bobbi Brown Cosmetics, Dr. Dennis Gross Skincare, Gillette Venus, Hada Labo Tokyo, Yue Sai, Simple Skincare, Himalaya Wellness, Parachute Advansed, the Dabur sub-lines, Parfums Christian Dior, Givenchy Parfums, YSL Beauty, Balmain Beauty, Mecca Cosmetica, Sesa and Nihar Naturals.
- **Drop as a private label:** Lacura (Aldi).
- **Homonyms:** qualifiers are listed in the JSON `homonym_flags` (melt and Essential from Kao, ABC, Trixie, Eisenberg, and generic-word lines).

## How the sources tier
- **Pure Beauty 2026 Judges Choice:** quality (the page names an independent expert panel).
- **Pure Beauty 2025:** cultural, per the coordinator, but the voting method is not stated on the page.
- **Skin Cancer Foundation Seal:** not quality. Only members paying the $15,000/yr Corporate Council fee may apply, the Seal goes to products not brands, and the list includes own labels. Tier these rows listed.
- **CHOICE sunscreen test and Vogue India jury winners:** quality.
- **Market reports (Mordor, 6Wresearch, Dataintelo, IMARC):** market standing only. 6Wresearch also gets owners wrong (Trichup and Nihar are not HUL's).
- **Owner-portfolio pages:** existence only.
- **Hwahae and Glowpick awards:** a consumer vote, so cultural.

## Additions
49 brands and 7 regions. See AUDIT_H1.json.
- **India everyday icons:** Cinthol, Boroline, Margo, Afghan Snow, Santoor.
- **Thailand:** Srichand.
- **Russia:** Natura Siberica.
- **US:** Fashion Fair.
- **Lebanon (Tripoli soap):** Khan Al Saboun, Sharkass, Sad-Ein.
- **Mexico:** Grisi.
- **Africa:** Black Like Me, House of Tara, Annique (own site).
- **Monoï de Tahiti AO producers (5):** Parfumerie Tiki and four others.
- **Indigenous makers (7):** Cheekbone, Prados, Ah-Shí, Mother Earth Essentials, Ruwi, Te Mana, Frankie Apothecary.
- **K-beauty from Hwahae/Glowpick (8):** d'Alba, Lilybyred, Too Cool For School, Wakemake, Jumiso, Bbia, Dasique, Naming.
- **Hanbang (6):** Donginbi, Yehwadam, Danahan, Coreana, Eath Library, Hanisul.
- **Öko-Test "sehr gut" (quality):** Hej Organic, Daytox, Martina Gebhardt, I+M, Logona.
- **Own-site existence only:** Najel (Aleppo soap), Shwe Pyi Nann (thanaka), Hashmi (surma).

Regions:
- Five designations: Aleppo ghar soap, Nabulsi soap, Argan (all UNESCO ICH), Monoï de Tahiti (AO) and Mysore Sandal soap (GI).
- Two renowned through independent pages: Tripoli soap (press) and Korean hanbang.

## Blind spots that remain
- No juried K-beauty quality source.
- No independent pages for Kenya or Senegal bodycare.
- No named rhassoul producer, and no Fakhoury or Zeitoun.
- No independent renown page for Marseille soap. The harvest's UPSM page belongs to a maker, so it cannot carry renown.
- No Middle Eastern hammam goods.
- Which? Best Buys were all private labels.
- Wet-shaving houses are already in the register.
