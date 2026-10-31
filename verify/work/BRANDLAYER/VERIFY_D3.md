# VERIFY D3 Audio & Video

Opus verifier, 2026-10-31. Inputs: D3.json (harvest, 242 brands, 11 regions) and AUDIT_D3.json (170 additions, 5 regions, 10 drops). Output: VERIFY_D3.json. Helpers and saved page texts: VERIFY_D3_tmp/ (pages/index.json maps each URL to its file; build.py, overrides.json, final.py rebuild the JSON).

## Fetches
- Raw texts: mcp__Parallel__web_fetch with full_content. The audit's own raw Parallel fetches in AUDIT_D3_tmp/raw/ (EISA year pages ey_*/et_*, Stereophile 2025/2026 Recommended Components, Crinacle, Wikipedia lists and categories, TAS, Hi-Fi Hall of Fame Luxman, LS3/5A history, DALI factory, the reviews) were imported unchanged as pages a_*.txt and checked again here. They were not fetched a second time.
- New fetches in this pass: Stereophile 2025 digital processors, disc & file players, power amps, phono cartridges, preamps, tonearms and subwoofers; Stereophile 2026 headphones; Stereophile Fall 2021 phono preamps (for Haniwa); Wikipedia categories of audio makers for Japan, France, Italy, Switzerland, South Korea and Russia, plus US page 2; Hi-Fi Hall of Fame business and equipment indexes; the RWHA Roberts Radio page; Stereophile Gramophone Dreams #62 p.2; ecoustics Ruark R1 review; TNW Fluance RT85 review; What Hi-Fi pages (best-radios-2019, best-accessories-2022, Audio Pro C20, Ruark R1S, Chord Company RumourX, Atacama Moseco 6).
- Short pages that came back inline are saved as condensed extracts marked "[condensed extract of raw fetch]". What Hi-Fi pages return an empty full_content: only the title and excerpt come back, and those are saved as "[page excerpt only]".
- Blocked or empty: whathifi best-radios-2025 (no text), nytimes Wirecutter best-turntable (empty).

## Result
- Brands checked: 409. That is the 238 harvest rows (242 minus Avantree, The+Radio, Grace Digital and the duplicate Anker Soundcore), the 170 audit additions and 1 new row, Garrard (turntables).
- Not shown: 0. Every row is shown on its src or src2.
- By tier: quality 249, cultural 127, listed 33. Harvest rows: quality 141, cultural 78, listed 19. Audit additions: quality 108, cultural 48, listed 14.
- Homonyms: 14. Seller role: 1 (Lafayette Radio Electronics).
- Regions: 15. With renown: 1 (Denmark). Without renown: 14.
- Countries: 164 rows have one, each from a fetched page. A country comes from a Wikipedia "Audio equipment manufacturers of X" category membership (location only), the country column of the Wikipedia loudspeaker list, or a statement in the brand's own Stereophile entry or review ("this Polish company", "made-in-Canada", "from Bulgaria"). Everything else is left blank, including Morel, Energy, Kalista, AGD, all EISA-only rows and the TV-list rows. 112 audit additions are blank because the audit's countries came from general knowledge.

## Audit applied
- **EISA (24 Hi-Fi rows, including iFi Audio and Moon by Simaudio).** The history index names no brands, so each src now points to an EISA year page that names the brand. The newest Hi-Fi year page is used, and the note lists every year page that names it. Examples: iFi Audio on 2018-19, 2022-23, 2023-24 and 2024-25; MOON on 2022-23 ("MOON Voice 22 & ACE"); MoFi on 2019-20 and 2023-24. Tier: quality.
- **Fezz Audio.** It is not on the EISA home-theatre page. Src is now the Stereophile 2026 integrated amplifiers page (Fezz Audio Silver Luna Prestige).
- **Clearaudio, Uher and Audio Analogue.** Src is now the Germany or Italy subcategory. They appear there as "Clearaudio Electronic" and "Uher (brand)" (aliases recorded). Tier: cultural.
- **Chario, JansZen Audio and Fleetwood Sound Company.** On the 2026 page they appear only under Deletions, so src is now the 2025 loudspeakers page. The same Deletions check was run on every Stereophile row, and only bold priced entries outside Deletions count:
  - Warwick Acoustics and Dan Clark Audio: their recommendation comes from the Stereophile Gramophone Dreams #62 review.
  - Feliks Audio: from the 2026 headphones page.
  - Doshi Audio: from the 2026 power amps page.
  - Bricasti Design: from the 2026 digital processors page.
  - Music Hall: from the 2025 turntables page.
  - Haniwa and Cyrus: from the Fall 2021 phono preamps page.
  - VAC: cultural, from its Valve Amplification Company article in the US category.
  - Merging Technologies: cultural, from the Switzerland category.
  - Denafrips: listed, because it is only a passing mention.
- **Danish makers.** Scan-Speak (as ScanSpeak), Peerless, Peak-Consult and Gamut now cite the Stereophile DALI factory page. They are mentions only, so they are listed.
- **Libratone.** Its Crinacle grade is B (Track Air Plus), so it is listed. Crinacle tiers were applied the same way to every row: A- or better is quality, B+ or lower is listed. Listed on that basis: Jomo, Unique Melody, FiR, Final.
- **Ruark Audio.** The What Hi-Fi page has no text. Src2 is the Stereophile 2026 loudspeakers entry Ruark Sabre-R, with the ecoustics R1 review also noted. Tier: quality.
- **Fluance.** Wirecutter came back empty. Src2 is the TNW RT85 hands-on review (measured speed variation, "passed with flying colors"). Tier: quality. Its Wikipedia phonograph-list row is a redlink.
- **B&W, Audio Pro and Grado.** None is attested on the Son-Video widget.
  - B&W becomes the register row Bowers & Wilkins (alias B&W), with src EISA 2016-17 and src2 Hi-Fi Hall of Fame.
  - Grado becomes the register row Grado Labs (alias Grado), with src the Stereophile 2026 phono cartridges page.
  - Audio Pro keeps its row, with src2 the What Hi-Fi C20 review.
- **The Master Switch roundup.** C.Crane and Victrola are listed because the roundup is not an independent test.
- **Seller praise.** The Headphones.com buying guide is a shop page. Gizaudio, Hisenior, 7th Acoustics, Subtonic and Simgot (Crinacle C) are listed. 7Hz, DUNU, Symphonium and Etymotic are quality through their Crinacle grades.
- **Other tier decisions.** Le Son International is listed: it appears only in reader comments under the ecoustics article. YL Acoustic is listed: the only source is an interview claim. Stirling Broadcast and Graham Audio are listed: the LS3/5A page only mentions them. Audiomaster and Chartwell are quality as BBC LS3/5A licensees (the licensee table). Audio Technology (Denmark) is listed: mention only.
- **Wikipedia list rows.** Each row's link target was checked:
  - Redlinks, so listed: Brinkmann Audio, TechDAS, Nottingham Analogue Studio, Origin Live, Townshend Audio.
  - Links to another article, so listed: Magnat (Voxx International) and Baird (John Logie Baird).
  - Edison: the row "National Phonograph Company" links to the company article Thomas A. Edison, Inc., which is now the row name. Tier: cultural.
- **Drops.**
  - Merged as aliases into register rows: B&W into Bowers & Wilkins, Grado into Grado Labs, Moondrop into Moondrop Audio, Etymotic into Etymotic Research, Cyrus Audio into Cyrus, and Anker Soundcore into the Soundcore row (which also gets RTINGS as src2).
  - Dropped: Avantree, The+Radio, Grace Digital.
- **MOVES_D2 (26 radio makers).** The merge tool picks these up itself, and none is duplicated in the brands. No brand row overlaps them. Region lists name three of them: Blaupunkt (harvest Germany), Goodmans (UK BBC monitors) and Mivar (Italy, historic radio & TV).

## Homonyms (homonym: true, renamed)
- Loewe (televisions): register Loewe is the fashion house.
- Morel (loudspeakers): register Morel is eyewear.
- Göbel (loudspeakers): register has Gobel tart tins, Goebel figurines and Christoph Göbel shoes.
- AVM (audio): register AVM is the FRITZ!Box maker.
- Pathos (amplifiers): register Pathos makes spearguns.
- Kuzma (turntables): register Kuzma is workwear.
- Schick (tonearms): register Schick is razors.
- Pure (DAB radios): register Pure is national dress. It has its own article, Pure (company), in the UK category.
- Tesla (Czechoslovak electronics): register Tesla is the carmaker.
- Vega (Berdsk Vega Production Association): register has Vega protein powder and Vega banjos.
- The Fisher (electronics): register Fisher is a motorsailer maker.
- Aqua (DACs): register AQUA is household goods.
- The Chord Company: kept apart from Chord Electronics.
- Garrard (turntables): see Index cleanup.

## Same company, not flagged
- Esoteric: register F1, high-end audio.
- Kenwood Corporation: the Japanese company, register D2. The row is named so that it cannot merge into the UK kitchen-appliance Kenwood (B5).
- Kondo (Audio Note Japan) and Audio Note (UK) are separate rows.
- Gradiente: alias IGB Eletrônica.
- Also same company: Melco, Victor Talking Machine Company, Telefunken, Hitachi, Sanyo, Magnavox, Realistic, Heathkit, Lafayette Radio Electronics, BenQ, Epson, Tatung Company.

## Regions
- **Denmark: renown true.** The harvest SoundStage region and the audit Stereophile DALI-factory region are merged.
  - Quote (Stereophile): "there are more loudspeaker manufacturers per person than any other country".
  - Quote (SoundStage): "Denmark is chock-full of hi-fi companies making products with global appeal".
  - 22 brands, all named in the Danish-maker passages, and each gets region Denmark. Raidho and Lyngdorf are quality through their Stereophile entries.
- **No renown (14).**
  - Norway: "to a smaller but growing extent" is not a renown statement.
  - Wikipedia category regions (Japan, UK, Germany, France, Italy, Switzerland): location only.
  - Southeast Asia: Headphones.com is a shop.
  - East Asia: Crinacle is a ranking.
  - UK, Royal Warrant: one maker's warrant page.
  - UK (BBC monitors): an enthusiast's history page that does not call the UK renowned.
  - Japan (valve amplification): Luxman alone.
  - Poland: Pylon alone.
  - Italy (historic radio & TV): the Phonola article.
  - Brands not named on the region pages were removed and are listed in dropped_not_shown. Examples: Leben, Dynavector, Technics, Nagaoka for Japan; dCS, Chord Electronics, Arcam for the UK category; Brionvega for Italy; Triangle for France; CH Precision and Revox for Switzerland.
- Brand region fields are set only for the renowned region, so the merge does not attach non-renowned regions to brands.
- REGIONS ARE NOT QUOTAS: hi-fi making is concentrated in Europe, North America and East Asia. The thin coverage of Africa, the Middle East, Central Asia and Latin America is not counted as an omission. Brazil (Gradiente), Indonesia (Polytron, 7th Acoustics), India (Onida, BPL Group, Sonodyne) and Russia (Vega, StereoPravda) have entries.

## Index cleanup
- The register row 'Garrard | Haute maison | crown jewellery | [A3, D3]' mixes the crown jeweller with the turntable maker. Remove D3 from it. VERIFY_D3 creates "Garrard (turntables)" (alias Garrard Engineering and Manufacturing Company; own article in Category:Phonograph manufacturers and the UK audio makers category; cultural; homonym).
