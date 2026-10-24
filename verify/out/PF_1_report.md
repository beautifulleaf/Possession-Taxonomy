# PF_1 report (D1 platforms)

Outputs: verify/out/PF_1_platforms.tsv (113 platforms), verify/out/PF_1_compatibility.tsv (136 rows). Fetch log: verify/work/PF_1/fetched.tsv (generator: verify/work/PF_1/gen.py).

Platforms per type: CPU socket 19 (AM5, AM4, sTR5, sTRX4, TR4, SP5, AM3, AM3+, FM2+, LGA 1700, 1851, 1200, 1151, 2066, 4677, 1150, 1155, 2011, 775); chipset 43 (Intel 800/700/600/500/400 series, X299, W790; AMD 800/600/500 series, TRX50, WRX90, TRX40, X399); memory standard 8 (DDR5, DDR4, DDR3, LPDDR5, LPDDR5X, SO-DIMM, CAMM2, 288-pin DIMM); bus 13 (PCIe 3.0-7.0, M.2 and key types, SATA 1.0-3.0, U.2); form factor 11 (ATX, Micro-ATX, Mini-ITX, E-ATX, FlexATX, SFX, SFX-L, TFX, ATX 3.0, ATX 3.1, ATX12VO); connector or port 19 (USB 2.0/3.0/3.2/C/4 v1/v2, Thunderbolt 3/4/5, HDMI 2.1, DP 1.4/2.1, 12VHPWR, 12V-2x6, Wi-Fi 6/7, Ethernet 2.5G/5G/10G).

Compatibility rows: 136 (chipset requires socket; socket supports memory; 22 CPU named forms fit their socket (12 AMD, 10 Intel); Intel chipset pages for Z890/Z790/Z690/Z490; three ASUS boards fit socket, chipset, ATX; USB4/Thunderbolt/PCIe/SATA/12V-2x6 backward-compatibility rows).

Pages failed: jedec.org node/9357 and DDR5 results (403); all amd.com product and driver pages (503), so AMD CPU sockets rest on Wikipedia List of AMD Ryzen processors (partial). The Intel and AMD chipset lists were read only in part.

Not attested or weak: no maker/standards-body page was fetched for SFX, TFX, E-ATX, M.2 key detail, LPDDR5X, HDMI 2.1 and DP (Wikipedia only); Wi-Fi and Ethernet have no C13 type, so they use "connector or port"; Intel and AMD chipset pages do not state sockets, so chipset-socket rows come from the Wikipedia socket pages; several chipset introduced years are blank; DDR3 and some "discontinued" statuses are inferred from successors; 3 motherboard rows only (ASUS); Core Ultra 5 245K is linked to Z890 but not to a socket (no ARK page fetched).
