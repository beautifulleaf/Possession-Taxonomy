# V4_J7_WIB report: wine of Spain and Portugal

Output: rebuild/out/J7_parts/WIB.json (validates OK with --v3: 1 department, 17 shelves, 42 kinds, 185 entries). 
## Structure
One department, "Wine of Spain & Portugal". Shelves are regions (Spain: Rioja/Navarre/Basque Country, Catalonia, Andalusia, Galicia, Castile and León, Aragon, Castilla-La Mancha, Valencia & Murcia, Madrid & Extremadura, the islands, Asturias & Cantabria; Portugal: Minho & Trás-os-Montes, Douro & Port, Beiras & Bairrada, Lisboa & Tejo, Setúbal & Alentejo, Algarve, Madeira & Azores). Kinds are the appellation tier (DO/DOCa, Vino de Pago and Calidad, Vino de la Tierra; DOP, Vinho Regional). Entries are appellations: about 130 Spanish and 55 Portuguese.

## Sources (all fetched)
- Spain: Wikipedia "Spanish wine regions" (all tiers, counts as of 2019).
- Portugal: Wines of Portugal region page (all 31 DOPs), Vine to Wine Circle (Vinho Regional names), Wikipedia "List of Portuguese wine regions" (2009 subregions and special designations).
- Detail pages (Rioja, Sherry, Cava, Priorat, Port, Quinta classification, Madeira, Portuguese wine) logged in rebuild/work/V4_J7_WIB/sources.tsv.

## Versions and roles
Versions are styles and ageing grades with the rank in `d`: Rioja grades, Priorat grades, Sherry styles with VOS/VORS, Manzanilla, Cava sweetness levels, Port styles, Madeira styles and age categories, Setúbal and Vinho Verde special designations. `role` = origin only on Rioja (first DOCa) and Jerez-Xérès-Sherry (first Spanish denominación), both stated by fetched pages. No landmark badge was set.

## Renames (old grape kinds)
Tempranillo, Graciano, Txakoli to the Rioja kind; Monastrell to Valencia & Murcia; Mencía, Verdejo, Albillo Mayor to Castile and León; Albariño, Godello to Galicia; Cava to Catalonia; Sherry to Andalusia; Port, Touriga Nacional to Douro & Port; Encruzado to Beiras; Arinto to Lisboa & Tejo; Loureiro to Minho; Madeira to Madeira & Azores. Producer entries (Vega Sicilia, Clos Mogador) are dropped as unclassified producers.

## Not changed or not done
- Kept by other parts: Grenache (Priorat entry), Red blend (Rioja red, Douro red), Rosé (Spanish rosado, Mateus, Lancers), Regional fortified wine (Moscatel de Setúbal, Montilla-Moriles) hold other countries' wines; Grape brandy and Spanish cider are not wine. No kind was dropped outright.
- No classified-producer lists exist for these countries in the fetched pages. The Douro quinta A-F grading is described, but no graded quinta is named, so none is listed.
- Spanish lists follow the 2019 page; Vinos de Pago added since (24 by 2022/23) and the 2026 register (106 DOPs, 43 IGPs) are not fully covered. Portuguese IG names rest on a 2011-era list plus the 2009 Wikipedia page; eAmbrosia was not read.
- Most entries have only a tier and region sentence, because no fetched page gave more. Grapes are listed only where a fetched page gives them (tt on five kinds).
- Market fields (own, tier, cty, ms) do not apply to appellations; none set. Brand register additions: none. No moves. No alc values (no alcohol-free wine in scope).
