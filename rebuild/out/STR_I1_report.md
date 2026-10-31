# STR_I1 report (Software)

Counts before to after: departments 11 to 11; shelves 30 to 37; kinds 139 to 149; archetypes 377 to 364. validate.py --v3 prints OK.

**Category:** added `ax` and an 11-step `key` with precedence note. Lead unchanged (no conflict with RULES.md).

**Departments:** every department has `t` and `ax`; every shelf has `t`, and `ax` where it holds more than three kinds. Shelves regrouped so each answers its department's question:
- Operating systems & system tools: six shelves (operating systems; running other systems' software; cleaning, tuning & repair; backup & recovery; files, search & access; customising & automating).
- Security: two shelves (device & family; accounts, connections & data).
- Office: documents, notes/time, language, money. Video: writing & capture, editing, converting. Music: recording, writing music down, performing & learning, players. Plug-ins: instruments, level & tone, space & time, voice & guitar, repair & measurement. Hobbies: home/family/health, radio, science. Developer: writing code, games & sites, databases/terminals/networks.

**Kinds:** every kind has hand-written `tt` (one question per group); flat `t` removed. No kinds merged or renamed (renames file is empty).

**Added kinds (each with a fetched Wikipedia source):** Word processor, Spreadsheet program, Presentation program (split from Office suite, models moved), Screenshot tool (split from screen recorder, models moved), Feed reader, Authenticator app, CD ripper, Clipboard manager, Disk space analyser, File comparison tool.

**Coverage references fetched:** List of software categories, Utility software, List of music software, Comparison of video editing software, Comparison of raster graphics editors, Screenshot, News aggregator. Not every shelf was checked against a dedicated retailer list; shelves outside these references (security, 3D/CAD, astronomy, developer tools) rely on the earlier stage-3 sourcing.

**Archetypes renamed to a named originator:** Debian, Fedora, Arch Linux, openSUSE, Mandrake Linux, Slackware, Gentoo Linux (from "... lineage"; versions kept), FreeBSD, OS/2 (IBM, 1987), AmigaOS (1985), Slic3r, eDonkey2000. ARP 2600 split out of "ARP 2600 and Oberheim classics" (Arturia SEM V and Matrix-12 V kept in `m`); Lexicon 224 and Lexicon 480L split.

**Generic archetypes demoted (versions kept in `m`, ranges in `r`):** Minecraft mod platforms, Windows built-in savers, Gnutella clients, Direct Connect clients, Vegetable garden planners, Visual Studio Code extensions, JetBrains Marketplace plug-ins, Neural DSP, Valhalla reverbs and delays, Eventide reverbs, Tokyo Dawn free dynamics, Synchro Arts tools, Mastering The Mix meters.

**Cross-links:** about 45 within I1 (all targets verified). None required by STR_SEE.tsv for I1.

**Not done:** no moves (Quad Cortex, a hardware unit, stays in Amp & cabinet simulator `m`); no new archetypes sourced beyond OS/2, AmigaOS and ARP 2600; year left blank for renamed Linux archetypes (unverified); API-client and hex-editor kinds dropped for lack of a fetched list.
