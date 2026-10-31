# GAP_J7 report

Result: validate.py --v3 OK (392 kinds, 5,804 entries). Backups in work/GAP_J7/bak/, sources in work/GAP_J7/sources.tsv. About 43 fetches used.

## 1. Loose models (8 kinds, 20 models)
All `m` removed. Bonal Gentiane-Quina and St. Raphaël became entries (Wikipedia Quinquina); Gancia, Yzaguirre and Fot-Li were added to Vermouth (Wikipedia Vermouth). Removed as unsourced retail SKUs: Kreinbacher, Printhie, AvinoDos, Winding Wood, Hampton Water, Artesans, Lunae, Pierre-Yves Colin-Morey, Vinakoper Capris, Kracher Nouvelle Vague, Iločki Podrumi, Vincent Denis, Bonny Doon, Bodegas de Alberto, Gonzalez Byass La Copa, Casals, Alessio, Bordiga, Lo-Fi.

## 2. Coverage lines
All 269 kinds now end in a coverage line: "Complete: n of n in <reference>" where the sel names a whole-space page, otherwise "No complete list exists; follows <pages>". Ten wine-style kinds that had no sel or nl got both.

## 3. Partial coverage
- Italian DOC (20 kinds): Italian Wine Central's list of 332 DOC (July 2025) read; 43 DOC names missing from Wikipedia added; now Complete.
- France: the 75 IGPs from dico-du-vin.com; new kind "France: other IGP wines" (59); Languedoc-Roussillon IGP now Complete for its list.
- Truncated pages read to their end (Carlsberg, bourbon, Japanese whisky, gins, Croatian, Georgian, Armenian, Chilean, Argentine, NZ wine, Beer in India and Australia, Mezcal, Shōchū, Baijiu): no further entries except the Carlsberg tail (Danish breweries without owners, not added).
- Brand pages added entries: Tennessee whiskey (+6), rye (+10, now sectioned by country), single pot still (+8), arak (+7), grappa (+3), Novo Fogo, Pacific pastis, High Noon.
- French cider: oriGIn list (Cornouaille, Pays d'Auge, Domfront, Cotentin, Perche) now Complete.
- Spanish pagos: Wine With Seth page adds Pago de Cirsus and Inurrieta, and years for seven pagos.
- Barolo (174 of 181 MGAs on Barolo World) and Barbaresco (66 of 66) MGAs added as versions.

## 4/5. Other gaps and sections
Added `g` for Romania (11), Chile, NZ, Cava, Domfront. Owners: Kopparberg page says only "family owned"; WKD is SHS Drinks.

## Remaining
- Cognac houses (25 of about 200): cognac-expert.com 402, Wikipedia category gives 16; deferred to Firecrawl. Searched: BNIC house count.
- Normandy IDAC press kit 403 (deferred).
- Barolo: 7 of 181 MGAs missing (page prints 174). Pago El Rincón (Madrid) has no kind.
- Tequila NOM register, American single malt (Wikipedia page 404; searched "Wikipedia American single malt"), Cachaça brand list, absinthe, Armagnac/Calvados houses: no whole-space page found.
- Lyre's ownership: searched; sources say independent, no fetched page.
- Spanish and Portuguese lists rest on 2019/2009 pages; eAmbrosia is JavaScript-only.
- Entries with `xg` "alphabetical" or "flat list" have no sections by design.

## Round 2 (about 47 fetches)
- Cognac: Wikipedia Category:Cognac brands (16) and Category:Cognac (18) read through the API; each house page fetched for owner, country and year. Owners, tiers and years set (Camus, Delamain, Hine, Otard, Bache-Gabrielsen, Braastad, Gautier, Monnet, Renault, D'Ussé, La Fontaine de La Pouyade); added D'Ussé, Renault, Rome de Bellegarde, Sève Fournier, Fromy Rogée. Noy (Armenian) and Three Barrels (Raynal, William Grant & Sons) went to Grape brandy. Cognac now 30 entries, Complete against the two categories. Louis XIII is a Rémy Martin cuvée, not an entry. cognac-expert.com (about 200 houses) stays deferred (402).
- Armagnac: Category:Armagnac has six pages; added Domaine de Bordeneuve (Guasch family). Calvados: Category:Calvados is empty; added Calvados Roger Groult (1975). Searched for further house lists without a Wikipedia page; none found.
- Tequila: List of tequilas has 37 brands and states no owners; all were already entries. NOM/CRT register is JavaScript-only, logged in firecrawl_deferred.md.
- Cachaça: List of Cachaça brands read in three section calls; 90 entries now, sectioned by wide distribution, small batch and artisan, export only. The page gives no owners.
- Absinthe: no "List of absinthes" exists; Category:Absinthes (10 pages) read; eight brands now carry owner, country and year.
- American single malt: Wikipedia has no article; Single malt whisky names no US distillery. Added ASW Distillery and McCarthy's Oregon Single Malt (Clear Creek). Searched: "American single malt whiskey" Wikipedia, Commission member list.
- Lyre's: VinePair says founded 2019 by two Australians in Britain, no owner or investor named; web search says privately held, no parent. Owner left empty (searched: Lyre's owner, Lyre's acquisition, Lyre's company page).
- Pago El Rincón added under "Madrid & Extremadura: denominations of origin".
