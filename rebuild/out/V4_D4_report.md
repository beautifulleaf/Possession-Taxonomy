# V4_D4 report: named-entry pass, D4 Cameras & Photography

Validator: `validate.py --v3 rebuild/out/D4.json` gives OK (145 kinds, 534 entries). Backups are in rebuild/work/V4_D4/bak/. Scripts: rebuild/work/V4_D4/build_d4.py and films_data.py (re-runnable from the backups).

## Per kind (entries before -> after)
- Camera bodies (Mirrorless 19->24, DSLR 11->14, Digital rangefinder 4, Digital back 2, Film SLR 28, Film rangefinder 14, Medium-format SLR 11, Medium-format rangefinder 6): entries now carry `g` = lens mount (Wikipedia List of lens mounts). Added Canon EOS M (EF-M), Samsung NX, Nikon 1, Pentax Q, Sigma fp (L-mount), Olympus E-System, Panasonic Lumix L and Leica Digilux 3 (Four Thirds), each with bodies and years from the fetched pages. Olympus E-System is badged origin (first Four Thirds body, per page).
- Other camera kinds (fixed-lens, 35 mm compact, half-frame, TLR, folding, view, instant, panoramic, toy, cine, camcorder): entries kept, `g` = maker, `nl`/`sel` added.
- Lenses (8 kinds with entries): kept, `g` = maker. No fetched page lists lens lines per mount, so no new lens entries.
- Film stocks, from Wikipedia's current and discontinued film lists, sections by maker: Colour negative 8->117, Black-and-white 10->112, Slide 5->38, B&W reversal 1->6, Infrared 0->8, Cine colour negative 3->8, Integral instant 6->8, Peel-apart instant 2->5. Discontinued lines are included for Kodak, Fujifilm, Ilford, Agfa, Konica, ORWO, Polaroid, Ferrania and some smaller makers; speeds and relaunches are versions.
- Light meter: 3 entries kept, `nl`/`sel` added.
- Flexible tripod (GorillaPod) and Mechanical stabiliser (Steadicam, Glidecam): entries removed, kinds are now commodity; the makers are in the brand register.

## Former models (`m`) and ranges (`r`)
All `m` and `r` lists are emptied. Camera models (Digilux 3, DMC-L1, E-300, Sigma fp) became versions or entries. Other models (Canonflex, Retina Reflex, Minolta SR-2, Yashica 44 and 635, Ektra, Witness, GA645, GF670, Contax N Digital and similar) were removed as out of scope: no fetched page lists them. Lens, lighting, tripod, bag, darkroom and action/360/drone/trail camera models were removed as SKU-level; their makers went to rebuild/out/D4_brands.json (now 224 makers, stubs with a source page where one exists, no country or year).

## Market facts
Digital cameras department `ms`: 2024 unit share of Nikkei 225 camera makers (Canon 43.2 %, Sony 28.5 %, Nikon 11.7 %, Fujifilm 9 %, Panasonic 3.4 %, OM Digital 1.9 %, Ricoh 0.8 %), from PetaPixel quoting Nikkei Industry Map 2026. WebFetch returned 403; the page was read with Firecrawl (one credit).

## Not done or not sourced
- No `own`/`tier`/`cty` fields on camera entries (market layer is not required for D4 by BRIEF); no national-champion or independent tiers.
- Mounts in the lens-mount list with no sourced page (Konica AR, Contax N, Minolta V, Samsung Kenox, Alpa and others) have no entry. Pentax Q, Sigma fp, Canon EOS M have gaps in body years.
- The lens-mount list gives no years or maker columns; fetch summaries would not return rows verbatim, so mounts were taken as names.
- Last ~90,000 characters of the discontinued film list (after Valca) were not read. Film Photography Project repackaged stocks, Polaroid instant 35 mm slide films, and many small-maker discontinued films are not included.
- The Wikipedia pages were read through WebFetch summaries, not verbatim rows; dates are as the summaries gave them.
- Film `nl`/`sel` text lists the scope cuts above.
