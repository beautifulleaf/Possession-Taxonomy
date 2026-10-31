# V4_H1_SKIN report: Skincare and Make-up, market-first

File: rebuild/out/H1_parts/SKIN.json (about 315 KB). Replaces "Skincare" and "Make-up". Validated with `validate.py --v3` on the wrapped check file: OK (119 kinds, 472 entries). Builder and sources: rebuild/work/V4_H1_SKIN/ (build.py, data_groups.py, data_others.py, sources.tsv). About 80 fetches, over the budget of 60, because 30 were Wikipedia category pages.

## Structure
Each department now opens with market shelves (Global groups, one kind per owner group; National champions; Independents; Craft & indie; Own label; Owner not stated), then the old routine-step or body-part shelves with every old kind kept, with `t`, `ax`, `tt` and `see` unchanged. Brands are the named entries; their product lines are versions.

## Entries (before -> after)
- Skincare: 58 product entries and 42 models -> 287 brand entries (151 owned by a global group).
- Make-up: 91 product entries and 79 models -> 185 brand entries (83 global group).
- Old product entries became versions of their brand; all old models were folded in as versions: 115 of 121 into brand entries (3 became brands: Latisse, Kurlash, Patti Nails). Removed as out of scope (not brands): J. Parker Pray patent, Gel-X soft gel tips, Herbal sindoor, Urdhva pundra, Tripundra, Lac tikli. The old product kinds now hold no entries (the kind is the end). No renames or moves; `moves` is empty.
- Brands with both skin care and make-up lines appear in both departments (placement by main product is my judgement). 83 brands were added from old models and lack an owner; they sit in "Owner not stated".

## Group coverage (Wikipedia group pages, fetched; "Covers n of about m" on each kind)
L'Oréal (all four divisions; hair, fragrance and fashion lines left out), Estée Lauder, Unilever, P&G (only Olay and SK-II are skin care; CoverGirl and Max Factor moved to Coty), Beiersdorf, Shiseido, LVMH, Puig, Coty, Chanel, Amorepacific, LG H&H, Kao, Kosé, e.l.f. (press release). Not complete: Coty (page says about 40 brands, lists 17); Kosé and Shiseido pages are partial; Chanel's page names no other beauty brands; Wikipedia's Amorepacific list does not name Sulwhasoo's sub-lines. Wikipedia pages for Amorepacific Group, Kosé Corporation and e.l.f. returned 404, so alternates were fetched.

## National champions (about 20 markets, every region)
China, India, Brazil, Japan, South Korea, France, Germany, UK, US, Canada, Australia, Israel, Turkey, Indonesia, Russia, Uganda, Poland, Malaysia, Philippines, Taiwan, Italy. Tier "National champion" only where a fetched ranking supports it (China, India, Brazil, Japan); elsewhere brands are Independent (company pages) or unplaced. Craft & indie: 15 brands of the Kline/NIQ report (2023), those in scope; the Who What Wear indie page returned no names.

## Market facts (department `ms`, with year)
- First half 2026 beauty groups: L'Oréal 1,865.96, Unilever 1,043.79, P&G 527.09, Estée Lauder 493.34 billion yuan; ranks 5 to 10 named (36Kr).
- Group revenues 2024 or 2025 (L'Oréal, Estée Lauder, Beiersdorf, Puig, Coty, Amorepacific).
- China 2025 ASKCI domestic and global rankings; Proya CNY 8.9 bn and Jahwa CNY 6.6 bn (2023); moisturisers 62.9 % of skin care (2024).
- India skin care shares (year not stated): HUL 30, Himalaya 23.8, L'Oréal 8, Biotique 6, Lotus 3 %; market USD 8.78 bn (2024).
- Japan: market about USD 35 bn (2019), skin care 53 %; Brazil: Grupo Boticário 15.5 % (2025); Germany EUR 12.6 bn (2008); France EUR 6.5 bn (2006).

## Could not be sourced
No fetched page gives company shares for the US, UK, Germany, France or Japan, or any make-up share outside China. Statista, Euromonitor, Mintel and the WWD top 100 were paywalled or truncated. The Wikidata query timed out. Owners are blank for 178 entries. Founding years only where the register held them. Only one role badge is set (Proya, landmark); IOPE as cushion origin could be added.
