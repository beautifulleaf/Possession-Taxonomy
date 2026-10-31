start: backup done
step1: revolvers 100000-end read (89 rows, page ends at Zulaica); data to be saved in work/CMP_E4/
step2: pistols 100000-end read (list ends Zigana); shotguns 100000-end read (Zastava LP12 PAS last). Years in wiki windows scrambled -> use only confident years. Next: bolt-action, lever-action, cartridges, then write script
step3: bolt-action list fully read (72 rows, in this conversation only; need to save to data file), lever-action done (article after 100000 = refs only)
step4: handgun cartridge list read in full (~255 rows) saved work/CMP_E4/handgun_raw.txt (name|mm bullet diam; excludes rimfires/rifle ones already present)
step5: rifle cartridge list fully read, saved rifle_raw.txt (names only, incl cannon calibres). Next: gauge page, then save revolver/pistol/shotgun/bolt/lever data and write edit script
step6: wrote data_firearms.py (tails: revolvers, pistols 100000-end, bolt, lever, shotguns). Gauge page read (1-50). Discovered earlier first-100000 parts were selective (revolvers/pistols/shotguns) -> re-reading 0-100000 windows (offsets 0,35000,70000) to add missing; then write build script (not yet written)
step7: wrote data_firearms2.py + build_cmp.py (not yet run). Next: run build, validate, sources.tsv, report
step8: build ran, validate OK, sources.tsv written. Remaining: report
