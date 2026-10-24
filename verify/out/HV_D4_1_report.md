# HV_D4_1 report (D4.1 Cameras, D4.2 Lenses and optical attachments)

Kinds: 37 of 37 attested, none unattested. Each has at least one full or partial fetched page. Six rest on weaker evidence:
- D4.1.2.01 film SLR: Wikipedia and a partial KEH page.
- D4.1.3.02 peel-apart: Wikipedia only.
- D4.2.08 cine lens: partial MPB category page.
- D4.2.11 lens filter: shop menu only, because the Hoya and B+W product pages returned 403.
- D4.1.1.05 bridge camera: one shop page.
- D4.1.1.08 action camera: GoPro page.

Named forms: 280, in `HV_D4_1_named_forms.tsv`.
Lines: 43, in `HV_D4_1_lines.tsv`. Examples are Sony Alpha, Leica M, Rolleiflex, Panavision anamorphic series and Metabones Speed Booster.
Makers: 100 rows, of which 22 reuse an existing maker_id and 78 are new. Six were renamed to avoid clashing with unrelated brands already in data/makers.tsv: M-sinar-ag, M-toyo-optical, M-atlas-lens-company, M-seagull-camera, M-vantage-film and M-miranda-camera. No country is recorded, because no page stated one.

Catalogues used:
- KEH, mirrorless page: good, listed models. KEH film category pages: brand names only.
- Wikipedia type articles: good for models, with the Fisheye and Macro pages cut off at 100k characters.
- Kamerastore: good, model-level.
- PhotoWorkout: poor, home page only.
- B&H category URLs returned the paper-roll page in place of the cameras and lenses pages; failed, logged.
- Camera-wiki Camera_types: fetched, used only to check the kind list.
- Not reached: Danawa, 7Artisans, SansMirror, CineD.

Skipped: colourways, kits, editions and sizes were not recorded.

Missing kind? (no tree kind for these generic types):
- Subminiature camera, https://camera-wiki.org/index.php?title=Camera_types
- Panoramic film camera, https://www.keh.com/shop/cameras/film-cameras/35mm.html
- Underwater camera, https://www.photospecialist.ie/viltrox-ef-eos-m2-speed-booster-focal-reduc-12249630
- Extension ring or tube and bellows, https://en.wikipedia.org/wiki/Macro_photography (same photospecialist page lists "Macro extension ring")
- Tilt-shift adapter and reverse adapter, the photospecialist page above
- Digital back, not attested

Logs and helper files are in `verify/work/HV_D4_1/`, including `fetched.tsv`.
