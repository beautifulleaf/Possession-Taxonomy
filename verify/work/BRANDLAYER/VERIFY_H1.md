# VERIFY H1 Personal Care & Beauty (brand layer, 2026-10-31)

Inputs verified together: the four harvest files H1.json (45 rows), H1_trad.json (51), H1_quality.json (61) and H1_portfolio.json (97), plus AUDIT_H1.json (49 additions, 7 regions, 57 drops).

Fetching: every distinct source URL (84) was fetched raw with mcp__Parallel__web_fetch (full_content), plus 5 verifier pages: LVMH Perfumes & Cosmetics, Kao EMEA brands, Vasu Healthcare brands, a Marico press release and Marico Bangladesh. Pages are saved in VERIFY_H1_tmp/pages/ and index.json maps each URL to its file. Three pages returned only a title in full mode: Al Jazeera, NZ Herald and NPR. For Al Jazeera and NZ Herald, the raw excerpt-mode text naming the brands was saved instead, marked as such. For NPR, the saved title and lede name Fashion Fair. Firecrawl is out of credit. The decisions are made by VERIFY_H1_tmp/build.py, which reruns from the saved pages. No URL was guessed: the src2 pages come from search results.

## Results

| Measure | Count |
|---|---|
| Rows left in H1 | 265 (harvest 214, audit 49, verifier 2) |
| Not shown | 0 |
| Quality | 23 |
| Cultural | 121 |
| Listed | 121 |
| Homonyms qualified | 15 |
| Rows with a tradition tag (`scene`) | 125 |
| Rows with an owner | 117 |
| Moved to H4 (MOVES_H1.json) | 15 |
| Moved to H2 (MOVES_H1.json) | 4 |
| Out | 2 (Told London, Lacura) |
| Corporate owners turned into owner notes | 13 |
| Regions | 18 (7 renowned, 11 not) |

## Audit applied
- **Owners turned into notes.** The 13 corporate owners are no longer brand rows. They are listed under `owners` with the brands they own, and each brand row carries an `owner` field where a fetched page shows the owner. The 13 are Bajaj, Godrej, Wipro, Honasa, Sundial, CavinKare, KLF Nirmal, Zydus, Good Glamm, Tropical Naturals, KSDL, the Akoma co-op and CellResearch.
- **Merges.** Each variant is now an alias of the register name:
  - Uriage, Avène, Revlon (Colorsilk and Professional), Bobbi Brown, MAC Cosmetics, Dr. Dennis Gross, Gillette, Hada Labo, Yue Sai Beauty, Menard, Simple, Himalaya, Parachute, Dabur (Amla and Almond), Dior, Givenchy Beauty, Yves Saint Laurent (alias YSL Beauty), Balmain, Mecca, Sesa Care and Nihar.
  - Verifier merges:
    - WHOO into The History of Whoo. LG H&H's own page uses "WHOO".
    - Savonnerie Le Sérail into Le Sérail, the same company as its B6 register row.
    - The Touqan factory into Touqan Soap Factory, the same company as its B6 register row.
    - Fashion Fair Cosmetics into Fashion Fair.
- **Owners corrected from fetched pages.** 6Wresearch lists both Trichup and Nihar under HUL, which is wrong.
  - Trichup belongs to Vasu Healthcare. Its own brand page says "Trichup is Vasu's research product in the field of Hair Care ... since 1990".
  - Nihar belongs to Marico. Marico's press release of 25 November 2025 lists Nihar Naturals in its portfolio. The same release lists Parachute and Fiancée, so both also get Marico as owner.
- **How the sources tier.**
  - Pure Beauty 2026 Judges Choice gives quality (11 rows). The page says "an independent panel of beauty industry experts".
  - Pure Beauty 2025 gives cultural, since the page states no method.
  - The Skin Cancer Foundation Seal gives listed (17 rows).
  - The CHOICE test gives quality for Mecca (Mecca Cosmetica passed at SPF 51). Cancer Council is only listed. One of its sunscreens passed, but three tested at SPF 24–33 and were recalled.
  - Vogue India Jury Winner gives quality.
  - The market reports (Mordor, 6Wresearch, Dataintelo, IMARC) give cultural, as market standing only.
  - Owner-portfolio pages give listed, as existence only.
  - Hwahae and Glowpick give cultural, as reader-data standing.
  - Öko-Test "sehr gut" (via CHIP) gives quality.
- **Out of H1.** Told London (its award was for a candle, a B4 candidate; not moved) and Lacura (Aldi's private label).
- **Moves, written fully verified to MOVES_H1.json.**
  - H4: Kaiak (Natura), Ralph Lauren, Maison Margiela, Frédéric Malle, Issey Miyake, Max Mara, Tory Burch, Kenzo, Loewe, Antonio Banderas, Chanson, David Beckham (fragrance), Gabriela Sabatini, Infiniment Coty Paris and Secret Alchemist (quality: a Vogue jury winner). Nine of these were renamed to their register names, which already carry H4, so for those the move adds only the alias.
  - H2: Imedeen, Naturactive, Desitin and Parche Leon.

## Verifier decisions to review
- **Mysore Sandal Soap.** It is not shown on Category:Cosmetics companies of India, so its src is now the GI Registry page (cultural) and the category page is src2.
- **Al-Jamal.** Renamed from "Al-Jamal (camel) Nabulsi soap". The article's caption reads "Al-Jamal (camel) brand".
- **Bader Hassoun & Sons.** Renamed from "Khan Al Saboun (Bader Hassoun & Sons)". Khan Al Saboun is the souk building, so it is kept only as an alias.
- **Two verifier rows (listed), both named in the Nabulsi soap article:** Touqan Soap Factory and Shaka'a soap factory.
- **Shemen Industries.** The article names it only as a Haifa competitor, with a red link. It is listed with no Nablus region.
- **Press pages.** Independent press describing hand or cauldron craft gives quality: Sharkass (Al Jazeera), Sad-Ein (L'Orient Today) and Tighanimine (the first Fairtrade-certified argan producer). Press describing heritage standing gives cultural: Srichand, Fashion Fair, Cinthol, Afghan Snow, Santoor, Grisi, Black Like Me, House of Tara, the 7 Indigenous makers, Bader Hassoun and the China Daily TCM brands.
- **Own sites and lists give listed.** Own sites: Najel, Shwe Pyi Nann, Hashmi, Annique, Targanine, Akoma, Dudu-Osun, Oshima Tsubaki, Phebo and Le Sérail. The hanbang guide rows also give listed, because they are list rows with shop links.
- **Thanaka navbox.** Artistry and Natural Wonder link their own articles, so they are cultural (owner Revlon for Natural Wonder).
- **ABC (Beiersdorf heat plaster)** stays in H1 as the audit has it. It is arguably H2, like Parche Leon.

## Homonyms
Trixie (cosmetics), Eisenberg (skincare), melt (Kao), Essential (Kao shampoo), ABC (Beiersdorf heat plaster), Median (Amorepacific), Chronos (Natura), Ekos (Natura), Même (Pierre Fabre), Cape (Kao), est (Kao), Bub (Kao), The Answer (Kao), Allie (Kao) and Munch (beauty). Munch clashes with Münch (G1) after accent folding.

In the moves file: Kaiak (Natura) and David Beckham (fragrance).

## Traditions (the `scene` field)
| Tradition | Brands |
|---|---|
| J-beauty | 24 |
| K-beauty | 18 |
| Ayurveda | 14 |
| Indian hair oils | 14 |
| K-beauty hanbang | 8 |
| Indigenous makers | 7 |
| Chinese herbal (TCM) | 5 |
| Monoï de Tahiti | 5 |
| Indian heritage soaps and creams | 4 |
| Middle Eastern soaps (Nabulsi 4, Tripoli 3, Aleppo 1) | 8 |
| Moroccan argan | 3 |
| Latin American heritage | 3 |
| African bodycare | 5 |

Also tagged: tsubaki camellia oil, Savon de Marseille, thanaka, Thai scented powder, kohl (surma), Siberian botanicals and Black-owned beauty heritage.

## Regions
Renowned (7):
- **Aleppo ghar soap:** UNESCO 2024 designation; no makers named on the page.
- **Nablus:** Wikipedia gives the renown quote, the UNESCO 2024 designation is src2, and four makers are named.
- **Argan, Souss and Essaouira:** UNESCO 2014 designation. Ajddigue and Tighanimine are named on src2 pages.
- **Monoï de Tahiti:** appellation-of-origin designation; 5 producers.
- **Tripoli:** L'Orient Today says "Tripoli as a whole is renowned for its traditional soap". Three makers: Sad-Ein on the src page, Sharkass and Bader Hassoun on the src2 page (Al Jazeera).
- **Mysore Sandal soap:** GI designation; 1 brand.
- **Myanmar thanaka:** the Wikipedia article says it is "a distinctive feature of the culture of Myanmar". No makers are named.

Not renowned (11):
- Korean hanbang has no renown statement on the Monodist guide or on BusinessKorea, and the MFDS definition is not a place-named designation. The audit had marked it renowned.
- West Africa black soap: the article states the soap's origin, not renown.
- The other West Africa entry (shea butter and black soap) rests on a blog.
- Marseille: only a maker's site, which itself says the soap has no appellation.
- India (2 sources), South Korea, Japan, the UAE, China, St James's and Brazil.

The "region" field is set only where the region's src or src2 page names the brand.

## Thin spots
- No juried K-beauty source.
- No independent page for any Aleppo maker; Najel is shown on its own site only.
- No independent pages for Kenya or Senegal bodycare.
- No renown page for Marseille.
- Portfolio rows were not checked for their own encyclopedia articles, so many stay listed although they may have articles.
