# QS_SEASON_2 report

Output: verify/out/QS_SEASON_2_attributes.tsv, 48 season rows (attribute rows only; no other tables). Fetch log: verify/work/QS_SEASON_2/fetched.tsv. Row form follows the stored rows: months in value, "southern|northern; <country (region)>" in scope.

Rows by region
- J2 southern hemisphere, 27 rows: New Zealand 9 (kina, crayfish/rock lobster, king salmon, green mussel, oyster, Bluff oyster variety, whitebait, snapper, scallop); Australia national 9 (barramundi, king prawn, snapper, native oyster, rock lobster, yellowfin tuna, blue swimmer crab, Chinook salmon, vongole clam); South Australia 8 (mackerel, oyster, prawn, blue swimmer crab, sardine, snapper, cuttlefish, squid; seasons defined as Dec-Feb etc. by the page); Argentina 1 (centolla, Nov-Jan); Chile 1 (red sea urchin, fishing window Jan-Mar).
- J4 Japan, 21 rows: Fukuoka city 9 (watermelon, nashi, apple, persimmon, satsuma, strawberry, loquat, melon, grape); Shizuoka satsuma; Chiba loquat; Saitama grape; Wakayama persimmon (kind, Fuyu, Hiratanenashi); Yamanashi peach; national pear varieties Kosui, Hosui, Nijisseiki, Chojuro (Mynavi Agri).

Gaps and failures
- South Africa: no rows. Pages found give closed seasons, recreational lobster days or "best in winter" without months (not recorded).
- Brazil: no rows. Only defeso (closure) news; tainha safra (May-Jul) found but has no J2 kind.
- Chile and Argentina: little beyond the two rows; no month calendar found. Argentine ministry fish guide has month bars as graphics (unreadable).
- FRDC Seafood by Season calendar: 403, then unreadable graphic OCR. Sydney Fish Market PDFs fetched only through Parallel.
- Japan: MAFF/JA calendar pages not found; Sapporo fruit table PDF lost its columns (not used); Satofull 403; Wakayama biwa PDF, Kagawa, Tochigi strawberry PDFs binary (failed). No strawberry or melon row beyond Fukuoka.
- Kagawa peach page: calendar is an image (no months).

Notes
- Skips: no kinds outside J2/J4 added. Species with no J2 kind not recorded (yellowfin bream, tiger flathead, King George whiting, garfish, sea mullet, snoek, tainha, blue cod).
- Missing variety?: grape varieties (Kyoho, Shine Muscat, Pione, Delaware, Himrod Seedless) and satsuma types (gokuwase, wase, futsu) are not in data/varieties.tsv; rows are at kind level. Australian native oyster (Ostrea angasi) has no variety row.
- NZ whitebait and NZ/Australian snapper are mapped to kinds J2.1.1.53 and J2.1.1.37 (different taxa than the kind text may imply).
- Peak versus availability: 100species and Sydney Fish Market rows record the stated peak months; year-round entries are Jan-Dec.
