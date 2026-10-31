# OWNERS_SWEEP report

Method: Wikipedia MediaWiki API (rvsection=0, redirects=1), 10-50 titles per call, 25 logged calls in rebuild/work/OWNERS_SWEEP/sources.tsv. Only top-level entries with a maker (`mk`) counted; versions are not entries. Owner set only from an infobox owner/currentowner/parent field or a lead sentence. Tier "Independent" only where the lead says family-owned or independent; otherwise tier left blank (owner not a named global group). Brand registers (`<CODE>_brands.json`) updated where the register name equals the maker.

Yield was low: most makers have no English Wikipedia company article, or the title is a disambiguation or person page. Blank-owner entries stay.

| Category | Entries with maker but no owner, before | after | Makers resolved | Register rows set |
|---|---|---|---|---|
| E2 | 763 | 746 | 6 | 3 |
| H1 | 252 | 234 | 14 | 12 |
| J9 | 343 | 330 | 13 | 13 |

Validation: `validate.py --v3` OK for E2, H1, J9.

## Set
- E2: Easton Archery (Independent, family owned); Black Crows (Independent); CCM Hockey - Altor Equity Partners, 2024; Black Diamond Equipment - Clarus Corporation; Rip Curl - KMD Brands; Head - Head Austria GmbH.
- H1: Mason Pearson (Independent, family); Kent (Independent, Cosby family); Cécred (Beyoncé Knowles-Carter, Independent); Mane 'n Tail - Straight Arrow Products, Inc.; Alpecin - Dr. Wolff Group; Bic - Bich family; Thinx - Kimberly-Clark, 2022; Dollar Shave Club - Nexus Capital Management, LP, 2023; Balenciaga - Kering, 2001; Norton - Saint-Gobain, 1990; Lava - WD-40 Company; Salon Selectives - Evergreen Consumer Brands; Vosene - Lornamead; Coast - Sodalis USA.
- J9: Coco Rico and Belvoir Farm (Independent, family); Chupa Chups - Perfetti Van Melle, 2006; Double Cola - K.J. International, Inc.; Henry Weinhard's - Molson Coors Beverage Company; R.W. Knudsen Family - TruRoots Company, 2022; Kickapoo Joy Juice - Monarch Beverage Company; Lorina - Royal Unibrew, 2018; Cécémel - FrieslandCampina (trademark); Shezan International - Shahnawaz Group; Zamzam Cola - Sina Industrial Food Holding; Yoli - FEMSA (year text conflicts); Panda Pops - Nichols plc, 2005.
- No tier set where the owner is a third party that is not clearly a global group.

## Conflicts or doubts left unset
- E2: Hi-Tec (infobox parent Cherokee Inc. vs lead "privately held"); Marucci Sports (infobox Fox Factory 2023-2026, ended); Schwinn Fitness (redirects to BowFlex, no owner); Bones Bearings/Spitfire (page is Powell Peralta/Deluxe Distribution, maker mismatch).
- H1: Revlon (infobox MacAndrews & Forbes, stale after 2022 restructuring); Zest (split by region: Sodalis USA / Unilever); Fenty Hair (only Fenty Beauty page exists); Libra (page is Libresse); Heno de Pravia ("linked to Puig", not ownership); Muji (shareholder list only); American Safety Razor (historic owner, successor only).
- J9: Lucozade ("marketed by Suntory since 2013"); Virgil's (1999 purchase by Reed's, current owner not stated); Delaware Punch (discontinued); Star Cola (JV, MGS vs Lotte-MGS); Huiyuan ("privately owned" only); Pascual Boing (cooperative).

## Not reached
Roughly 380 E2, 200 H1 and 330 J9 makers were not looked up or have no company article (mostly single-entry small brands). Further gains need non-Wikipedia sources.
