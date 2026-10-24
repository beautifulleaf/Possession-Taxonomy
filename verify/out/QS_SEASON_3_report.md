# QS_SEASON_3 report

Output: verify/out/QS_SEASON_3_attributes.tsv, 110 season rows (attributes only). Fetch log: verify/work/QS_SEASON_3/fetched.tsv. Row form follows stored rows (months in value, scope "southern; ZA" or "southern; BR"). Ids continue after the highest season number per kind found in data/attributes.tsv and the QS_SEASON/QS_SEASON_2 outputs.

Rows
- South Africa (J4 only): 40 rows from ECR (Eat Creative Ready) seasonal guide; months taken from its season groups (Sep-Nov, Dec-Feb, Mar-May, Jun-Aug).
- Brazil (J4 only): 67 rows from the Vitat month-by-month list (a wellness site, not an official table; months where the item is listed), plus 3 Santa Catarina rows (strawberry Nov-Mar, grape Jan-Mar, apple mid Feb-mid Jul) from the IFSC 2021 CEASA/SC Sao Jose study (Parallel excerpt fetch, fetch_status partial).
- J2 fish and seafood: no rows for either country.

Gaps and failures
- No CEAGESP or CEASA sazonalidade table was found by search (only price indices); no SASSI or retailer month calendar for South Africa (SASSI gives traffic-light status, not months).
- ZA fish: pages found give only recreational rock lobster days, closed seasons, or fishing-quality ratings; none stated as supply season. Brazil fish: only defeso (closures).
- Dineplan PDF unreadable (binary); Dineplan blog page was a festival page.
- IDEC weekly regional calendar PDF fetched but not used: it describes itself as built on assumptions (continuous harvest for tropical crops) and looks generated.
- captainexperiences Cape Town page fetched, not used (US species list, fishing quality ratings).

Notes
- ECR page was read through WebFetch's summariser; its Nov list is separate from the season grids, so single-month "Nov" rows (cherry, plum, watermelon) are thin.
- Vitat items mapped: naartjie to Mandarin; tangerina/mexerica not merged; cebolinha to Chives (J4.3.11); banana rows not written for Brazil (several types). No new kinds, makers or varieties added; skips: items with no kind (Cape gooseberry, coconut, prunes, caju, acerola, jabuticaba, carambola, etc.).
