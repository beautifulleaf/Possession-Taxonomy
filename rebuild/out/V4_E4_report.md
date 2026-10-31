# V4_E4 report: named-entry pass, Weapons & Armour (E4)

Entries rose from 377 to 1,050; 341 loose `m` models were removed. Validation (`validate.py --v3`) passes. Fetched URLs are in `rebuild/work/V4_E4/sources.tsv`; backups are in `rebuild/work/V4_E4/bak/`. No market panel was added, as the brief says; no new makers, so `E4_brands.json`, `E4_renames.json` and `E4_moves.json` are unchanged.

## Per kind (entries before to after)
- **Swords, European**: Arming sword 8 to 7 and Longsword 8 to 6, rebuilt as Oakeshott types X to XXII with the subtypes (Xa to XXa) as versions (Oakeshott typology). Short sword 2 to 10, Spatha 0 to 3, Greatsword 2 to 5, Rapier 5 to 9, Smallsword 0 to 3, Sabre 6 to 8, Katzbalger 1 to 2 (Wikipedia, Types of swords).
- **Japanese**: new kind "Sword tradition (den)" with the Gokaden (Yamato, Yamashiro, Bizen, Soshu, Mino) and their schools as versions (nihonto.com); new kind "Ancient and later Japanese forms" (9). Smith and blade kinds keep their entries.
- **Other swords**: new kinds Korean sword (4), South Asian sword (12), Arab, Persian and Central Asian sword (7), African sword (9), Maritime Southeast Asian sword (30), Mesoamerican sword-club (2); Dao +3, Jian +2.
- **Knives**: Dagger 14 to 24 (List of daggers); new kinds Asian dagger (18), African dagger (5), American and military fighting knife (10).
- **Polearms**: about 90 new entries from Wikipedia's Polearm article, placed by family with region sections.
- **Bows**: +4 (Welsh bow, Stellmoor bow, Subeshi culture bow, Austroasiatic crossbow); culture sections on every entry.
- **Firearms**: single-action revolver +9, double-action +29, percussion +12, semi-automatic pistol +25, lever-action +11, bolt-action +38, shotguns about +50 (Lists of revolvers, pistols, bolt-action rifles, shotguns, Lever-action).
- **Ammunition**: 61 handgun, 25 rimfire, 100 rifle cartridges and 13 shotgun gauges (cartridge lists, Gauge page).
- **Armour**: about 70 entries: torso types, 40 helmets, body-armour systems, new kind "Shield of other cultures" (10) plus round shields.

## Scope cuts, stated in each kind's `sel`
- The four long firearm lists were read only to characters 100,000 (revolvers to Ruger GP100, pistols to Glisenti 1910, shotguns to SRM 1216, Lever-action to 100,000); later parts were not read. Pistol, shotgun and rifle lists are cut to civilian, collector and sporting lines, so they are not complete.
- Cartridges are a cut of the two lists (about 185 of roughly 700), leaving out wildcat, experimental and military-only rounds.
- Excluded as out of scope: practice swords, ceremonial regalia, fencing épée and foil, riot and ballistic shields, athletic and work helmets, fictional armour.
- The fetch tool paraphrased rather than quoted, and the revolver, pistol and rifle pages' country and year columns came back scrambled, so most firearm entries carry no year or only one I could state with confidence.

## Not sourced or thin
- Many descriptions of lesser-known forms (Kila, Shuckra, Balarao, several Philippine blades) are one generic line; the references give none.
- No Shinto or Shinshinto dates (the fetched page gives none). No `role` badges were set, since no fetched page names a best-selling or first entry. No `own` or `tier` fields, as these are not branded kinds.
- Kinds without a whole-space list (muzzle-loaders, semi-automatic rifles, air guns, optics) keep earlier entries with a generic `sel` saying so.

## Removed models (`m`), by reason
- Retail replica, knife, bow, air-gun, reloading, powder, case, cleaning and optics products: removed as out of scope (no canon names them).
- Unsourced historical pieces (Janissary kilij, Japanese helmet bowls, grenades and others): removed.
- Became entries or versions: .22 WMR, .17 HMR, .380 ACP, .40 S&W, 10mm Auto, .270 Win, .300 WM, .300 BLK, shotgun gauges, Main gauche, Ops-Core FAST helmets (versions of FAST helmet), Beretta APX.
Full list: `rebuild/work/V4_E4/removed.json`.
