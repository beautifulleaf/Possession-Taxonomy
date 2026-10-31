# V4_A1_OUTER report (final)

Part file rebuild/out/A1_parts/OUTER.json (about 233 KB). Replaces Coats & jackets; Suits & formalwear; Workwear & uniform clothing (54 kinds). Validates OK (0 errors, 382 entries). No renames or moves; scenes untouched.

## Entries
154 -> 382. Largest: Overcoat 8->21, Business suit 8->23, Tie 6->15, Biker jacket 7->15, Shell jacket 8->18, Puffer jacket 8->17, Parka 4->15, Coach jacket 0->5, Track jacket 2->9. `g` = brand home country, then brand, year; named forms last. 18 origin badges, each per a fetched page. 273 branded entries carry `cty`; 72 carry `own`/`tier` (and `own_y` where stated).

## References
- 56 Wikipedia and brand pages fetched in total; every URL is in rebuild/work/V4_A1_OUTER/sources.tsv or named in the entry `s`.
- The six truncated articles (Suit, Tuxedo, Necktie, Morning dress, Waistcoat, Mackinaw coat) were read to their ends; the tails held citations and navigation only. Added from them: Kareeba suit (Met 2025), Mess jacket, Teba jacket.
- Fetched: Fur clothing (all but last 1,160 characters), Leather jacket (Chapal Type A1 1925, eight-ball jacket, battle jacket added). No dedicated Wikipedia article exists for quilted jacket, deck jacket, coach jacket, work trousers, chef's jacket or scrubs beyond Chef's uniform and Scrubs, which name no brand.
- Restored from data/named_forms.tsv: 75 pieces as entries and 8 as versions, each citing its recorded page (many are retailer pages from the earlier harvest; `fetch_status` partial for some). Eleven further pieces confirmed on fetched brand or review pages: Barbour Classic Northumbria and Corbridge, Patagonia Jackson Glacier, Outdoor Research Coze, Fjallraven Nuuk, Eddie Bauer CirrusLite, Decathlon Simond MT100, Stio Hometown, Arc'teryx Kyanite, Nobis Nord, Ossie Clark Lamborghini (V&A, 1969).

## Not restored (no page found or readable)
Max Mara Ludmilla, Mountain Hardwear Ghost Whisperer, Black Diamond Fineline, Supreme Crest Coaches Jacket (pages returned 403/404/503; Firecrawl is out of credits); REI Stormhenge, Magma 850, Trailmade and Rainier-class own-label items other than Rainier; Los Angeles Apparel raglan coach jacket; Barbour New Eskdale; brandless generics (two cut-off vests, hacking jacket, Donegal tweed sport coat, white-tie and tuxedo waistcoats, two knit ties, Rubinacci tie).

## Empty `d`
120 entries still have no `d` because their page does not name a fact for the piece; most are the restored retailer-page pieces and register pieces. The Wikipedia brand pages checked (Burberry, Canada Goose, The North Face, Arc'teryx, Herno, Rab, Belstaff) do not name those models.

## Market facts (department `ms`, with years)
VF Corporation US$10.45 bn (2024); Moncler EUR 3.13 bn (2025); Canada Goose CA$1.35 bn (year to March 2025); Barbour GBP 225 m (2019); Burberry GBP 2,420 m (2026); Carhartt US$1.8 bn (2024); HUGO BOSS Group EUR 4,307 m, BOSS Menswear 3,329 m (2024); Dickies sold to Bluestar Alliance for about US$600 m (2025, VF paid US$820 m in 2017); Kontoor Brands US$3.15 bn (2025). No category-wide share found. Tiers: Global group for VF, Amer Sports, Moncler, Kontoor, Fast Retailing brands; Independent for family or single-brand owners. Brands with no stated owner have no `own`/`tier`.

## Loose models
145 `m` removed; 83 restored as above, 11 confirmed on new pages, the rest listed above.
