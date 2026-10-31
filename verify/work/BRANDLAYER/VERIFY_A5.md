# VERIFY A5 Clocks & Watches (brand layer)

Opus verifier, 2026-10-31. Inputs: A5.json (631 harvest rows), AUDIT_A5.json (11 drops, 67 adds, 5 regions). All 108 source pages fetched raw (Parallel web_fetch full_content); copies in VERIFY_A5_tmp/ with index pages.json.

## Counts

- Rows decided: 681 (631 harvest - 11 dropped + 67 audit adds - 6 merged duplicates)
- By tier: listed 370, cultural 218, quality 90, seller 3
- Not shown: 0. 13 names were not on their src page; all were found on a fetched src2 (Category:Clock manufacturing companies of the United States / of the United Kingdom / Clock manufacturing companies; en Wikipedia article Kleynod). 13 Japanese makers are shown in Japanese script on ja Category:日本の時計メーカー.
- Regions: 6 with renown wording, 11 without.

## How tiers were set

- GPHG winners, AHCI members, FHH partners, F.P.Journe Young Talent winners: quality (award or guild).
- Wikipedia category members: cultural. Wikipedia list rows: cultural only when the row itself links to the brand's own article; red links, unlinked rows and links to a parent, founder, town or unrelated page are listed (fetched checks: Aragon, Knot, Nomadic and Thoma link to non-brand pages).
- Directories (Watches of Switzerland, NASS sundial artisans, business directory) and makers' own websites: listed.
- Press pages: quality only where the page states craft, materials, durability or an award; otherwise listed. Museum, V&A collection and regional heritage inventory pages: cultural. Retailers with a page naming them as watch sellers: seller (Seddiqi, Beyer, Ethos); Wako and The Hour Glass have their own Wikipedia articles: cultural.

## Merges

- A.L.B (ALB Watches); Grovana (Grovana Watch, W. & H. Groeflin); Dubey & Schaldenbrand (Dubey Schaldenbrand); Sea-Gull (Tianjin Seagull Watch Group); Ricoh Elemex (Ricoh Watch Ltd.). Harvest name "Polic" is a truncation of "Police".

## Regions

|Region|Renown|Brands shown|Not shown on src|
|---|---|---|---|
|Switzerland (Vallée de Joux, Neuchâtel, Geneva)|yes: "along with Neuchâtel, the birthplace of Swiss horology ... still the home of the most famous Swiss watch factories"|6|F.P. Journe, Philippe Dufour, Greubel Forsey, MB&F, Ulysse Nardin, Parmigiani Fleurier, Girard-Perregaux, Zenith, Rolex, Omega, Richard Mille, Ressence, Laurent Ferrier, H. Moser & Cie.|
|Glashütte, Saxony, Germany|yes: "known as the birthplace of the German watchmaking industry"|8|-|
|Japan|no|9|G-Shock, Orient Star, Rhythm Watch, Hajime Asaoka, Masahiro Kikuno, Kurono Tokyo, Minase, Aichi Tokei Denki|
|Besançon, Franche-Comté, France|yes: "transforming Besançon into the Capitale française de l'horlogerie (French capital of clockmaking)"|8|-|
|England (London) clockmaking|no|7|Charles Frodsham, Smiths, Dent, Gillett & Johnston, Hamilton & Inches, Comitti of London|
|Black Forest, Germany|yes: "the region where the cuckoo clock was popularized and ... exported ... becoming world-famous"|6|Kieninger, Hermle, Kienzle, Gustav Becker, Lenzkirch|
|Soviet Union / Russia|no|6|Slava, Molnija, Luch, Zarya, Chaika, Petrodvorets Watch Factory, Serdobsk Clock Factory (Majak), Konstantin Chaykin|
|China|no|2|Beijing Watch Factory, Hangzhou Watch Company, Fiyta, CIGA Design, Shanghai, Memorigin, Baltany|
|India|no|2|Fastrack, Sonata|
|United States (Connecticut clockmaking and independent microbrands)|no|8|Monta, Nodus, Vaer, Brew, Weiss Watch Company, Shinola, Timex, Hamilton, Bulova|
|United Kingdom independent microbrands|no|1|Bremont, Farer, Elliot Brown, Dennison, Fears, Pinion, Isotope|
|Netherlands, Denmark, Finland, Nordic independents|no|9|-|
|Saint-Nicolas-d'Aliermont, Normandy, France|yes: "Saint-Nicolas d'Aliermont, cité horlogère ... riche patrimoine industriel, témoignage du savoir-faire horloger"|7|-|
|Mora, Dalarna, Sweden|yes: "the iconic curvy form that is recognised as the Mora Clock and still sought after today"|1|-|
|Bornholm, Denmark|no|1|-|
|Morbi, Gujarat, India|no|1|-|
|Haut-Jura (Morez and Morbier), Franche-Comté, France|no|2|-|

## Notes for merge

- 370 of 681 rows are "listed" (existence only): mostly de Liste von Uhrenherstellern rows with red links (268 listed vs 77 with own article).
- Regions without renown wording (Japan, England, Soviet/Russia, China, India, US, UK microbrands, Nordic, Bornholm, Morbi, Haut-Jura) rest on company or list pages; a page naming the region as renowned is still needed before they become divisions. Bornholm ("Bornholm clocks") and Haut-Jura (Comtoise) are the closest.
- Brands in regions are kept only where the region src page shows them; many famous Swiss names (Rolex, Omega, F.P. Journe...) are not on the Vallée de Joux page.
