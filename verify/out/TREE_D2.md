# D2 Phones, Tablets & Personal Devices: decided tree

Category: D2 Phones, Tablets & Personal Devices (domain D, Electronics). Membership test: a phone (mobile, landline, cordless or DECT), two-way radio, pager or other device for personal communication; a tablet, e-reader, electronic organiser or translator, or an electronic writing tablet; a smartwatch, fitness tracker, smart ring or other smart jewellery, smart glasses, GPS unit (golf GPS units included), satellite messenger or tracker; a power bank; and the parts and accessories made for one phone, tablet or wearable (S3). Children's tablets are here. Structure: sub-family (the role the device plays for its owner; D2.8 parts is exempt from the role axis), then leaf (device class as retailers shelve it; only in D2.1, D2.4 and D2.6), then kind (the build or form class buyers compare inside). Operating system and store, finding network, radio service, charging standard, connectivity, screen size, panel, capacity, rugged rating (`ip_rating`, `standard_met`), price band, era, user and maker are attributes, ledger rows or views, not kinds.

Ids (R-58): D2.n is a sub-family and D2.n.m a leaf; a kind is D2.n.m.kk, or D2.n.kk where a sub-family has no leaf.

## D2.1 Phones

Leaf axis: device class as retailers shelve it (smartphones, feature phones, satellite phones, landline phones).

### D2.1.1 Smartphones

- D2.1.1.01 Bar smartphone (slate): touchscreen smartphone in one rigid slab-shaped body.
- D2.1.1.02 Keyboard-bar smartphone: one-piece smartphone with a fixed physical keyboard below the screen (`era` tag).
- D2.1.1.03 Flip foldable smartphone: smartphone whose flexible screen folds across its width into a compact square.
- D2.1.1.04 Book foldable smartphone: smartphone whose flexible screen folds along its length and opens like a book into a tablet-sized screen.

### D2.1.2 Feature phones

- D2.1.2.01 Bar feature phone: non-smartphone mobile phone in one rigid body with a keypad (taco and other one-piece shapes carry a `form_tag`).
- D2.1.2.02 Flip feature phone: non-smartphone mobile phone whose body folds on a hinge (clamshell).
- D2.1.2.03 Slider phone: mobile phone whose screen half slides over the keypad half (`era` tag).
- D2.1.2.04 Swivel phone: mobile phone whose screen half rotates on a pivot to show the keypad (`era` tag).

### D2.1.3 Satellite phones

- D2.1.3.01 Satellite phone: handheld phone that places calls through satellites rather than a cellular network. †

### D2.1.4 Landline phones

- D2.1.4.01 Landline phone: telephone for a fixed line, corded or cordless (DECT); `handset` is an attribute (the corded half is attested at the harvest).

## D2.2 Two-way radios and pagers

No leaf (`leaf = null`). Kind axis: form and mounting of the device; the radio service (FRS, GMRS, PMR446, Part 90, amateur, CB) is an attribute in the compatibility ledger.

- D2.2.01 Handheld two-way radio (walkie-talkie): battery-powered push-to-talk transceiver held in the hand.
- D2.2.02 Vehicle-mounted two-way radio: two-way transceiver made to be installed in a vehicle (provisional until attested). †
- D2.2.03 Base-station transceiver: fixed two-way transceiver run from mains power at one site (provisional until attested). †
- D2.2.04 Pager: small receiver that alerts its carrier and shows short messages sent over a paging network. †

## D2.3 Tablets

No leaf (`leaf = null`).

- D2.3.01 Slate tablet: touchscreen computer in one flat body, sold without a keyboard (an optional keyboard cover is a part); size is an attribute.

## D2.4 E-readers and pocket information devices

Leaf axis: device class as retailers and museums shelve it.

### D2.4.1 Reading and writing devices

- D2.4.1.01 E-reader: device sold for reading e-books, usually on an e-paper screen; size class, `panel` and `platform` are attributes.
- D2.4.1.02 E-paper writing tablet: e-paper device sold for stylus note-taking and handwriting (provisional until attested). †

### D2.4.2 Organisers and PDAs

- D2.4.2.01 Electronic organiser: pocket device that keeps a diary, address book and notes (digital diary).
- D2.4.2.02 PDA or palmtop: handheld personal digital assistant running applications on a small screen with stylus or keyboard.

### D2.4.3 Language devices

- D2.4.3.01 Electronic dictionary: handheld device holding one or more dictionaries for look-up. †
- D2.4.3.02 Pocket translator: handheld device that translates speech or text between languages. †

## D2.5 Wearables

No leaf (`leaf = null`). Kind axis: the form and build class of the device.

- D2.5.01 Smartwatch: wrist device with a display that runs apps and notifications; a GPS sports watch is this kind with `multisport_gps`.
- D2.5.02 Hybrid smartwatch: analogue-hand watch with built-in sensors and phone connection.
- D2.5.03 Smart band (fitness tracker, activity tracker): slim wrist band with a small display that tracks activity, sleep and heart rate.
- D2.5.04 Screenless band: wrist band with sensors and no display, read through a phone app.
- D2.5.05 Smart ring: finger ring with sensors that tracks health and activity.
- D2.5.06 Smart glasses: glasses with a see-through display, camera or speakers (a headset that encloses the eyes is D5).

## D2.6 Location, navigation and safety devices

Leaf axis: device class as maker catalogues and expert guides separate it.

### D2.6.1 GPS units

- D2.6.1.01 Handheld hiking GPS: portable satellite-navigation unit with maps made to be carried on foot outdoors.
- D2.6.1.02 Handheld GPS with two-way radio: handheld GPS unit with a two-way radio in the same case; `radio_service` is recorded.
- D2.6.1.03 Golf GPS device: handheld or clip-on GPS unit that gives distances on golf courses.
- D2.6.1.04 Portable sat-nav (car navigation unit): portable navigation unit with road maps, sold to be moved between vehicles (a mounted one is G1). †

### D2.6.2 Satellite communicators

- D2.6.2.01 Satellite messenger: handheld device that sends and receives text messages and SOS alerts through satellites.
- D2.6.2.02 Personal locator beacon: one-way distress beacon that sends a position to rescue services via satellite.

### D2.6.3 Trackers

- D2.6.3.01 Bluetooth item tracker: small tag attached to an item and located through a phone's finding network.
- D2.6.3.02 GPS or cellular tracker: tracker with its own GPS and cellular link (SIM, subscription) carried by a person or put in a bag (`user` tag: child or adult; an animal tracker is B10, a vehicle tracker G1). †

## D2.7 Power banks

No leaf (`leaf = null`).

- D2.7.01 Power bank: portable rechargeable battery that charges phones and other devices; `capacity_wh`, `output_w` and `built_in_cable` are attributes.
- D2.7.02 Magnetic power bank: power bank that attaches magnetically to the back of a phone and charges it wirelessly (MagSafe, Qi2); stays a kind only if a comparison source ranks it apart (C10(b)).

## D2.8 Parts and accessories made for one phone, tablet or wearable

No leaf (`leaf = null`); exempt from the role axis (C5(d)). Kind axis: the accessory type, by object served.

- D2.8.01 Phone case: case or cover made to hold and protect one phone model.
- D2.8.02 Tablet case: case or cover made to hold and protect one tablet model.
- D2.8.03 Screen protector: film or glass sheet cut to cover the screen of one device.
- D2.8.04 Watch strap or band: replacement strap made for one smartwatch or band.
- D2.8.05 Device charging dock or puck: dock, stand or puck charger made for one device.
- D2.8.06 Stylus: pen made for the screen of one tablet or phone line.
- D2.8.07 Tablet keyboard cover: cover with a keyboard made for one tablet line. †
- D2.8.08 E-reader cover: case or cover made to protect one e-reader model. †
- D2.8.09 Phone battery case: phone case with a built-in battery that charges the phone.
- D2.8.10 Clip-on phone lens: add-on lens that clips over a phone camera. †
- D2.8.11 Phone gimbal: motorised handheld stabiliser made for a phone. †
- D2.8.12 Selfie stick: extendable pole that holds a phone for self-portraits. †
- D2.8.13 Clip-on phone game controller: game controller that clips onto a phone. †

## Precedence inside D2

- A kind is the build or form class; a measured spec, certification, size, panel or display technology, operating system, radio service, price tier, user, setting, scene, era or maker is an attribute, tag or view. Technology or connectivity makes a kind only when the key names it or it changes the physical form and a fetched source ranks the types apart (C10).
- Foldables are two kinds, flip (D2.1.1.03) and book (D2.1.1.04). A rugged phone has no kind: it is filed by its form (D2.1.1.01 to D2.1.1.04, D2.1.2.01 to D2.1.2.04) with `ip_rating` and `standard_met` (MIL-STD-810) and a generated "rugged" view. A gaming phone is a smartphone; gaming is a scene modifier.
- A phone that is also a game machine (Nokia N-Gage) is D2 if sold and used as a phone, and files as a bar feature phone (D2.1.2.01) with `form_tag = taco`.
- A landline phone, corded or cordless (DECT), is one kind (D2.1.4.01) with a `handset` attribute; it splits only if a fetched source ranks corded and cordless apart.
- Two-way radios are filed by form and mounting (D2.2.01 to D2.2.03), never by radio service: amateur, CB, FRS, GMRS, PMR446 and Part 90 radios carry `radio_service`, and push-to-talk over cellular is a connectivity attribute. A radio scanner is D3.
- A tablet sold without a keyboard is a slate tablet (D2.3.01); a keyboard cover sold for one tablet line is a part (D2.8.07); a device sold with its keyboard is D1. A stylus made for one tablet follows it (D2.8.06).
- An e-paper device is filed by what it is sold for: sold for reading, an e-reader (D2.4.1.01, `platform = Android` for a Boox-type device); sold for stylus note-taking, an e-paper writing tablet (D2.4.1.02). If D2.4.1.02 fails attestation, such a device is D2.4.1.01 with a stylus attribute.
- A PDA or electronic organiser is D2 (D2.4.2.01, D2.4.2.02); a programmable pocket computer is D1 unless sold as a PDA or organiser.
- A GPS sports watch is a smartwatch (D2.5.01) with `multisport_gps` and a generated "sport watches" view; a smartwatch with cellular or satellite SOS stays a smartwatch, satellite capability an attribute. Smart band and fitness tracker are one kind (D2.5.03); a band with no display is a screenless band (D2.5.04).
- Smart glasses (D2.5.06) have a see-through display, camera or speakers; a headset that encloses the eyes is D5.
- A device's primary job decides its kind and connectivity is a modifier: a GPS handheld with a two-way radio in one case is D2.6.1.02 with `radio_service`; a wrist device doing a satellite-messenger job stays D2.5.01.
- A portable sat-nav is D2.6.1.04; a sat-nav, bike computer or tracker fitted to a vehicle is G1, and a tracker made for an animal is B10. A golf GPS device (D2.6.1.03) is D2 even though it is made for one sport.
- A Bluetooth item tracker (D2.6.3.01) is one kind whatever its finding network (an attribute); a GPS or cellular tracker (D2.6.3.02) and a magnetic power bank (D2.7.02) stay kinds only if a fetched source ranks them apart from D2.6.3.01 and D2.7.01; otherwise each becomes an attribute of those kinds.
- A power bank (D2.7.01, D2.7.02) is D2; a portable power station is B7; a phone battery case is a part (D2.8.09).
- Parts and accessories are in D2.8 only when made for one phone, tablet or wearable (S3): cases and covers only when made to hold or protect one object at a time; a charger, dock or puck made for one device (D2.8.05) and a cable with a proprietary connector follow the device, while generic chargers and standard cables are D1. Clip-on lenses, gimbals, selfie sticks and clip-on game controllers made only for phones are D2.8.10 to D2.8.13; one made for cameras, consoles or computers that also takes a phone stays with that device.
