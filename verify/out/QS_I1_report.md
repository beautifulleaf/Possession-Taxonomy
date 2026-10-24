# QS_I1 report

Rows: schemes 7, tier_entries 130, named_forms 37 (new, kind I1.2.01), makers 7, maker_kinds 7. No standards, standard_values or attributes.

Tier entries by scheme and edition
- SCH-av-test-home: Windows 11 2026-08 (15, TOP PRODUCT), macOS Tahoe 2026-06 (9, Certified), Android 2026-07 (12) = 36
- SCH-av-comparatives-rwp: Feb-May 2026, 20
- SCH-av-comparatives-mpt: March 2026 (20), September 2026 (6 Advanced+ names only, page partial) = 26
- SCH-av-comparatives-performance: September 2026, 20 (rank and impact score)
- SCH-av-comparatives-mac: 2026, 7 Approved
- SCH-av-comparatives-mobile: 2026, 9 (8 Approved, Google Play Protect Not Approved)
- SCH-av-comparatives-summary: 2025 Top-Rated 7 (product level) and 2024 at maker level (ESET Product of the Year; Avast, AVG, Bitdefender, Kaspersky Top-Rated) = 12

Notes and failures
- AV-Comparatives Summary Report 2025 PDF failed (encrypted); HTML summary page read only to char 100000 plus a second chunk. No Product of the Year or Outstanding Product named for 2025. 2024 Outstanding Product not named; 2024 page read to char 100000 only.
- September 2026 Malware Protection Test: per-product figures not on the fetched page, so only the six Advanced+ names are entered (partial). No per-product page link was given, so none was fetched.
- AV-TEST pages: score columns inferred by header order (the fetch tool did not label them). macOS and Android pages showed Certified badges only; no TOP PRODUCT marks seen there. G Data Mobile Security (5.5/6/5) was reported as not certified by the tool; the value is entered as scores only, unverified.
- AV-TEST scores were read from the overview tables only, not product pages.
- Named forms reused: Avast One, AVG AntiVirus, Norton 360, Microsoft Defender Antivirus, Trend Micro Internet Security. Tencent reuses M-tencent (existing class game publisher).
- TotalAV is one named form covering TotalAV Premium, Mobile Security, etc.; product names are in scope.
- Skips (not consumer I1.2.01): CrowdStrike Falcon Enterprise for Mac and Trellix Endpoint Security for Mac (2 rows). AV-TEST VPN tests and AV-Comparatives VPN tests not searched (0 rows).
- No earlier editions harvested. Fetch log: verify/work/QS_I1/fetched.tsv; generator verify/work/QS_I1/build.py.
- Missing kind?: none.
