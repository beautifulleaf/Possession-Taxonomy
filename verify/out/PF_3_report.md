PF_3 report (B3 lamp caps and smart lighting; C6 optics standards)

Platforms: 45 in verify/out/PF_3_platforms.tsv.
- cap standard: 22 (E10, E12, E14, E17, E26, E27, E39, E40; B15d, B22d; G4, GU4, G5, G5.3, GU5.3, G9, G13, GU10, GX53, GU24; R7s; W2.1x9.5d wedge). IEC 60061-1 sheets given for all except R7s and wedge.
- smart-home protocol: 8 (Zigbee, Matter, Thread, Z-Wave, DALI, Casambi, Philips Hue, IKEA DIRIGERA/TRADFRI).
- C6: 15 (barrels 0.965 in, 1.25 in, 2 in; T2 M42x0.75; M48 filter thread; SCT thread; RMS objective thread; Vixen-style and Losmandy D dovetails; microscope eyepiece tubes 23.2 and 30 mm; ASCOM, INDI, LX200, SynScan). C13 has no value for control protocols, so I used "mount control protocol" (new, owner to decide); barrels and threads use "connector or port", dovetails "rail interface".

Compatibility: 21 rows in PF_3_compatibility.tsv (Hue/IKEA to Zigbee, Matter, Thread and caps; adapter relations for barrels, threads, eyepiece tubes, dovetails; SynScan to ASCOM/INDI; EQ6-R Pro named form to SynScan).

Failed pages: agenaastro GSO diagonal (403, no substitute), agenaastro Tele Vue adapter (403, replaced by optcorp), stellarmate Sky-Watcher (404), IKEA TH TRADFRI 250 lm (no cap/hub text). Agena Baader T2 and Vixen-Losmandy pages: WebFetch 403, read via Parallel web_fetch.

Not attested (no platform row): 3 in barrel, M54 thread, Synta/Arca dovetail (search excerpt only), finder shoe standards, infinity and 160 mm tube length, DIN/JIS naming (only 23.2/30 mm tube sizes attested). Partial: R7s (no sheet or dimensions), Matter page (first 100k characters read). No introduction year for most caps except Edison screw (1881).
