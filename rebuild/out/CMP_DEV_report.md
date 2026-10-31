# CMP_DEV report: completion pass for D1, D2, D4

All three files pass `validate.py --v3` (D1 110 kinds/385 entries; D2 78/358; D4 145/571). Backups: rebuild/work/CMP_DEV/bak/. Scripts: apply_d1.py, apply_d2.py, apply_d4.py; raw data: nv_raw.txt, nokia_raw.txt, film_raw.txt; fetch log: sources.tsv (all in rebuild/work/CMP_DEV/).

Method note: Wikidata answered one count query but returned no inception years for Nokia models (193 names, almost all undated), and the first query was rate-limited (429). Wikipedia lists were therefore read in WebFetch windows.

## D1 Graphics card (27 entries unchanged; versions +228)
Every desktop GeForce and Titan model with launch date from Wikipedia's List of Nvidia GPUs (windows 0, 80,000, 100,000, 150,000) and the GeForce 20/30/40/50 series articles, added as versions of its generation entry (Celsius to Blackwell). Reference total not countable from the page. Still short: OEM-only and Mac Edition rows were folded or dropped, GeForce 9400/9500 GT, GTX 1660 Super/Ti and GTX 16 mobile parts have no date and are missing, RTX 5090 D has none.

## D2 (entries 342 -> 358; versions +673)
- Nokia: 15 family entries (1000 to 9000 series, C/E/N/X, Symbian 3-digit, Asha, Lumia and X, three-digit feature phones, N-Gage, Mobira) with 669 models and years from Wikipedia's List of Nokia products, read to about character 250,000 of 351,000. Rows with no year on the page are blank. Not read: the page after 300,000 and the 6000 series rows 6000 to 6009.
- Apple Watch: Series 1, 2, 3 added with dates (life-cycle table). Kindle: Kindle 2 International added; the Kindle table (29 devices) is otherwise complete. Pixel: release dates added, Pixel Tablet entry added, Pixel Watch 3 and 4 years filled. iPad was already complete against its tables. Pixel XL/Pro variants stay grouped.

## D4 (entries 534 -> 571)
- Lens mounts: 16 body entries added for Konica AR, Konica F, Canon FL (Pellix), Icarex BM, Rolleiflex SL35 (QBM), Praktiflex, Miranda, Minolta V (Vectis), Olympus Pen F, Hasselblad Xpan, Pentacon Six, Pentax Auto 110, Contax N Digital, Sigma SA, Samsung NX mini, Sony Mavica. No entry (page 404): Contax N1/NX, Fujica X, Kowa Six, Petriflex, Praktina, Visoflex, Alpa, Samsung Kenox, DJI DL; Paxette and Tamron adapters not itemised.
- Discontinued films: the page actually ends at Valca; the unread part was Foma through Tasma. 21 new entries (148 versions): Foma, Forte, Foton, Fotoimpex, Gevaert, Gigabit, Maco, Negra, Tasma, SPUR, Factory No. 5, Polaroid slide films; Svema, ORWO, Konica, Lucky, Rera and Polaroid rows already present were not repeated. Not itemised: older Fujifilm, Ilford and Kodak rows (grouped earlier), Rollei rows without a stated type, Street Candy.
- `sel` lines updated on each changed kind.
