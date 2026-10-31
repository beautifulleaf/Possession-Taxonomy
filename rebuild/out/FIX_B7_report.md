# FIX_B7 report

Counts: kinds 25 -> 26; archetypes 0 -> 4; brands 70 -> 71; models 174 -> 150 (flat `m`).

- B7-1 partly: new shelf "Design & vintage fans" (Cooling & fans) with kind "Electric fan (design & vintage)" and 4 sourced archetypes: Emerson Northwind (Wikipedia Emerson_Electric), Vornado air circulator (Vornado_Air), Dyson Air Multiplier, Balmuda GreenFan. Brand "Emerson Electric" added (the register's "Emerson" is a different company). Not added, no fetchable source: Braun HL 1 (Cooper Hewitt host blocked, Wikipedia 404), Toyotomi Rainbow as archetype (company history page returned 503; stays a model), Aladdin Blue Flame (Aladdin page does not mention it), brass/steel-blade Emerson versions, Westinghouse/GE fans.
- B7-2 skipped: already done in the rebuild; only one "Indoor air quality monitor" kind (5 models) exists and there is no separate monitoring department.
- B7-3 done: kinds with 10+ models cut to 8 or fewer (fan heater, window and portable AC, air purifier, humidifier, dehumidifier); trade-code model names removed or shortened to range names. Replacement air filter already two entries.
- B7-4 done: Electric fireplace stays in B7 as freestanding only; definition now points inset and wall units to Home Fixtures. No move entry needed. Optiflame/Opti-myst duplication with G3 left as is (noted, not removed).
- B7-5 done: neck air conditioner stays a type; SKUs trimmed.

validate.py on B7.json: OK. Backups in rebuild/work/FIX_B7/bak/.
