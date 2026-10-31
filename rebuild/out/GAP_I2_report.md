# GAP_I2 report (I2 Digital Media & Items)

Validation: `validate.py --v3 out/I2.json` OK (80 kinds, 872 archetypes). About 22 fetches (work/GAP_I2/sources.tsv); backups in work/GAP_I2/bak/. Firecrawl had no credits.

**1. Loose models (all `m` gone).** Domain name: six endings (.com, .ai, .co.uk, .net, .org, .io) removed as types, not entries; the kind has no entries. Profile-picture NFT: 12 loose names became 10 entries (Azuki, Doodles, Meebits, DeGods, Clone X, Cool Cats, World of Women, Milady Maker, VeeFriends, Solana Monkey Business); Okay Bears and mfers removed (no fetched page). Generative art NFT: Fidenza and Terraforms became entries, Autoglyphs kept. Ordinals: NodeMonkes and Taproot Wizards became entries. Game item NFT: Age of Rust, Spirit Clash, Six Dragons removed (unsourced), replaced by Axie Infinity, NBA Top Shot, Sorare.

**2-3. Coverage lines.** Every kind with entries now ends "Complete", "Covers n of m" or "No complete list exists; follows ...". Built In's list of 24 NFT collections was read in full: 18 PFP entries, 2 generative, 3 game, 1 land (Otherdeed); BAYC's secondary collections are its versions. Decrypt's seven Ordinals projects: 6 added (RSIC Metaprotocol is a mining campaign). Aiwiki.ai text-to-image page: 5 open-weight families and 5 versions added (Complete: 7 of 7 open families; closed services excluded, Kolors/Sana/Lumina-mGPT lack a stated licence). Blockchain name: 9 services added (Complete: 10 of 10 in the Paragraph overview). File formats were re-read as extension lists (the summariser refuses verbatim rows): raster +2 (CR2, DNG), vector +2 (TGAX, V2D), 3D unchanged; all three now say Complete. Wikidata could not subset formats (class held 15,796 items).

**4. Reports' gaps.**
- Typeface designers/years: Wikidata query on class Q17451 returned no rows; entries keep the generic description. Searched: Wikidata SPARQL by label. Remains open.
- Pixel and bitmap typeface: Wikipedia Bitmap font names only formats (PCF, BDF, PSF), no typefaces; kind stays empty.
- Dota 2 Arcana, Fortnite Black Knight: fandom pages blocked, Firecrawl out of credits; not added. Klim, Grilli Type, House Industries, Neuland not retried (earlier 404s).
- Speech and audio model: no page naming open speech models found; Whisper only.
- Market layer: none applies to these kinds.

**5. Sections.** No kind has `xg` with ungrouped entries; the NFT kinds are under 12 entries each, so no sections added.

New register stubs in I2_brands.json: Chiru Labs, Remilia Corporation, Mathcastles, Tyler Hobbs, Dapper Labs, Taproot Wizards, Gary Vaynerchuk, Nike and RTFKT (no country or year unless a page gave it). Terraforms has no year: sources conflict (2021 or 2022).
