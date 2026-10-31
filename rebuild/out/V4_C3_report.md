# V4_C3 report: C3 Plants & Living Cultures (light pass)

Fetched: 6 Wikipedia pages (Echeveria, Camellia japonica, Sempervivum, Anthurium luxurians (404), Crassula ovata, Kalanchoe blossfeldiana). Logged in rebuild/work/V4_C3/sources.tsv. Backups in rebuild/work/V4_C3/bak/. Script: rebuild/work/V4_C3/apply.py.

## Changes
- All 60 loose models (`m`) removed from 21 kinds; no ranges (`r`) existed. Key `m` no longer present.
- Entries: 1440 archetypes before; 1451 after (+11).
  - Echeveria 10 → 17: Black Prince, Doris Taylor, Blue Curl, Frank Reinelt, Painted Lady, Worfield Wonder, Oliver became entries (all named on the fetched Echeveria page).
  - Houseleek 4 → 8: the four RHS Award of Garden Merit cultivars (Bronco, Lilac Time, Othello, Reinhard) named on the fetched Sempervivum page.
- Every kind with entries (all kinds that had `x`) now has `nl` and `sel`. `t`, `ax`, `tt`, `see` untouched. No `xg`/`g` added.
- Kinds with no entries stay as end kinds.

## Removed as out of scope (not verified on a fetched page)
- Cultivars: Camellia japonica ×8 (not found on the fetched page, which was truncated at 100,000 characters), Crassula ×4, Kalanchoe 'Tessa'/'Wendy', Anthurium luxurians (page 404), Cymbidium ×3, Paphiopedilum Prince Edward of York, apple Ben Davis/Cortland/Empire, Tulip 'Black Hero', potato Red Pontiac, Buddha's Hand and Calamondin Orange (already covered by existing entries).
- Commodity products: Supertunia petunia ×6, cut chrysanthemum ×3, Live Star Moss, mushroom grow kits ×4, wreaths ×2, White Labs/Wyeast yeast ×4, Algae Research Supply cultures ×3.

## Brand register
Added: Algae Research Supply, Oregon Kombucha, House Plants of Australia, Conard Pyle Co., Cants of Colchester (names and short descriptions only; no country or founding year, as no fetched page gave them). Other makers were already registered. Individual breeders named as `mk` (e.g. Barry Meyers-Rice, Pemberton, Laffay) were not added.

## Not sourced
- No whole-space reference (RHS AGM list, genus register, orchid grex register) was fetched, so `sel` says honestly that the list is a representative set following the cited Wikipedia/RHS pages, not complete. Completing each kind needs many more fetches than this pass allowed.
- No market panel (`ms`, `msum`): no fetched page ranks plant breeders.
- Roles (origin/landmark) not added.
