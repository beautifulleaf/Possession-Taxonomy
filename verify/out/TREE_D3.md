# D3 Audio & Video: decided tree

Category: D3 Audio & Video (domain D, Electronics). Membership test (key step 24, third branch): a TV, projector, hi-fi, record player, radio, clock radio, headphones or earbuds, speakers for listening, smart speaker or display, voice assistant, smart-home hub or karaoke machine, together with digital audio players, streaming media players and set-top boxes (K-150), external audio converters and headphone amplifiers, USB-C dongles included (K-150), and parts, attachments and accessories made for one audio or video device (S3, step 8; K-8 mounts, K-16 audio figures). Not here: computer monitors, internal audio cards, standard-connector cables and adapters, generic chargers and microphones made for speech, calls or streaming (D1); phones, tablets, smart glasses, two-way radios and pagers (D2); cameras, film and enlargers (D4); VR and mixed-reality headsets, consoles and coin-operated video cabinets (D5); studio, stage, PA and DJ gear, music microphones and recording interfaces (E3, K-143); toys that imitate a music object (E1); records, discs, tapes, blank media and Playaway-type preloaded players (F1, F-8); car audio (G1, K-6); hearing aids (H2); ear defenders (A1); furniture, racks and TV cabinets (B1); baby monitors (B8); radio-controlled clocks (A5); sunrise lamps (B3); assistant apps and paid licences (I1); catalogue subscriptions (I3). Structure (Candidate A, D-4; memo sections 3 and 10): sub-family (role in a picture-and-sound setup, in signal order; the closing parts sub-family D3.8 is exempt from this axis, C5(d), CV-17), then leaf (device type as shops name it, one stated axis per sub-family; D3.7 and D3.8 store `leaf = null`, C5(b), so their kind ids carry no leaf part; the one-kind Tuners leaf is allowed, R-11), then kind (the one physical class buyers compare inside the type: body form for televisions, body and installation for projectors, amplification stage for amplifiers, cabinet form and placement for speakers, wearing form and enclosure for headphones and earphones, receiver type for radios). Each object gets one kind. Display technology, backlight, resolution, size, throw ratio, light source, drive type, operation, driver technology, wired or wireless, ANC, channel layout, amplification (passive, active), battery, placement, multi-room platform, IP rating (`standard_met`), `form` (desktop, dongle), `unit_of_sale`, era, region, user and price band are attributes, tags, ledgers or views, never kinds (rule T, D-3, C10 to C12); there are no portable-radio, party-speaker, portable-speaker, Bluetooth-speaker or gaming-headset kinds (D-18, O-33). Marketing names (QLED, Neo QLED, QNED, ULED, Triluminos; table radio, portable radio, party speaker, 音箱) are C9 alias rows. Assistant platforms, multi-room systems, codecs, Matter and Thread, and eARC are compatibility-ledger rows or attributes (C13), never kinds. Decided at the build (memo section 14, DPH): `sound_signature` (neutral, warm, bright) on headphone, earphone and speaker named forms, one value per source, a description and never a rank; `use` (travel, sport, gaming, home, office and calls, computer, studio-style) as one facet with generated best-by-use views, replacing the memo's separate `use = computer` and `gaming` tags; a generated "needs an amplifier" view from `impedance_ohm` and `sensitivity_db` on headphone named forms (not a level, not a C13 platform). Maker role: owner (maker_roles.tsv D3, scope all, provisional = yes; the navigation proposal asks to set provisional = no): audio and video models carry the maker; the identity strand in hi-fi, headphones and turntables is served by a brand tab. Display groups (navigation proposal, display only; D3 is not built, so no group ids are issued; the tree keeps the memo's sub-families): level 1 shows the eight sub-families renamed and re-ordered in shoppers' order with headphones first: Headphones and earphones (D3.5); TVs and projectors (D3.1); Speakers and soundbars (D3.4); Hi-fi amplifiers and DACs (D3.3); Turntables, players and streamers (D3.2); All-in-one systems and radios (D3.6); Smart speakers and displays (D3.7); Parts and accessories made for one audio or video device (D3.8); level 2 shows the memo leaves, with D3.7 and D3.8 kinds directly; side views: a brand tab for headphones, hi-fi separates and turntables, and generated views Home cinema and By display technology. Quality markers (display): headphones and earphones by tonal balance (closeness to a neutral target), clarity and detail, dynamics, soundstage, comfort and fit, isolation or noise cancelling, sensitivity and amplifier needs, value; speakers and hi-fi separates by reviewer class from performance and test bench (with a bass-reach sub-class for speakers), measured distortion and noise (SINAD), build and matching; TVs by display technology and contrast, brightness and colour, motion and processing, size; projectors by use, throw type, light source, brightness; turntables by drive and operation, tonearm and cartridge (TV, projector and speaker markers and the level-1 order are provisional on the memo). A kind marked † has no fetched page naming it yet and needs one before it enters the data (D-2; memo attestation list, section 10; section 14).

Ids (R-58): D3.n is a sub-family and D3.n.m a leaf; a kind is D3.n.m.kk, or D3.n.kk where a sub-family has no leaf.

## D3.1 Displays & projection

Leaf axis: what the device shows (picture type).

### D3.1.1 Televisions
Kind axis: body form. Display technology (LCD-VA, LCD-IPS, WOLED, QD-OLED, Micro LED, plasma, CRT; CRT and plasma with an `era` tag), backlight, quantum dot, resolution, size and tuners are attributes; a "by display technology" view is generated.
- D3.1.1.01 Television: screen sold with television reception or as a television, of any display technology.
- D3.1.1.02 Rear-projection television: television whose picture is projected onto the screen from inside its cabinet; a kind only if a fetched source shows its body differs. †

### D3.1.2 Digital projectors
Kind axis: body and installation. Throw ratio (standard against short throw), light source, imaging chip, native resolution, brightness and battery are attributes; `portable` is a tag.
- D3.1.2.01 Digital projector: projector that throws a picture from a video or computer signal onto a screen or wall from a distance.
- D3.1.2.02 Ultra-short-throw projector: digital projector made to sit at the wall just below the image it throws (C12(a)).

### D3.1.3 Film and slide projectors
Kind axis: medium projected.
- D3.1.3.01 Slide projector: projector that shows photographic slides. †
- D3.1.3.02 Cine film projector: projector that shows motion-picture film. †

## D3.2 Sources & players

Leaf axis: what is played or received (record, disc or tape, stream or broadcast, stored files, radio signal).

### D3.2.1 Record players
Kind axis: playing unit. Drive (belt, direct, idler), operation (manual, semi-automatic, automatic), built-in phono preamp and USB output are attributes.
- D3.2.1.01 Turntable: record-playing deck with platter and tonearm.

### D3.2.2 Disc and tape players
Kind axis: carrier played.
- D3.2.2.01 CD player: player for compact discs.
- D3.2.2.02 Blu-ray/DVD player: player (or recorder) for Blu-ray and DVD video discs.
- D3.2.2.03 Cassette deck: hi-fi component that plays and records compact cassettes.

### D3.2.3 Streamers and set-top boxes
Kind axis: what arrives and how.
- D3.2.3.01 Network streamer: hi-fi source that plays music from the network or streaming services into an audio system.
- D3.2.3.02 Streaming media player: stick or box that plays streamed video and audio on a television (K-150). †
- D3.2.3.03 Set-top receiver (terrestrial, satellite or cable): box that receives broadcast television for a screen (K-150). †

### D3.2.4 Portable players
Kind axis: stored files.
- D3.2.4.01 Digital audio player: portable device sold mainly to play stored or streamed music, with no calling (K-150); a Toniebox-type player for children is filed here by default with `user = child`.

### D3.2.5 Tuners
Kind axis: one kind (R-11).
- D3.2.5.01 FM/DAB tuner (separate component): hi-fi separate that receives radio broadcasts for an amplifier, with no speaker of its own.

## D3.3 Amplification & conversion

Leaf axis: the system stage served (stereo, AV, signal conversion).

### D3.3.1 Stereo amplifiers
Kind axis: stage of amplification. Tube or solid state, class A/B/D, power rating, streaming and phono inputs are attributes.
- D3.3.1.01 Integrated amplifier: stereo amplifier with preamplifier and power stage in one box.
- D3.3.1.02 Stereo receiver: stereo amplifier with a built-in radio tuner.
- D3.3.1.03 Preamplifier: control and switching stage that feeds a separate power amplifier.
- D3.3.1.04 Power amplifier (incl. monoblock): amplifier stage that drives speakers from a preamplifier signal, stereo or one channel per box.

### D3.3.2 AV amplification
Kind axis: stage. Video switching, channel count, HDMI and Atmos are attributes.
- D3.3.2.01 AV receiver: multichannel amplifier with surround decoding, video switching and a tuner in one box.
- D3.3.2.02 AV processor: multichannel surround preamplifier and decoder that feeds separate power amplifiers.

### D3.3.3 Converters and headphone amplifiers
Kind axis: function. `form` (desktop, dongle) is an attribute.
- D3.3.3.01 DAC: external device whose designed function is converting digital audio to analogue.
- D3.3.3.02 Headphone amplifier: external device whose designed function is amplifying a headphone signal.
- D3.3.3.03 DAC/headphone amplifier combo: external device that converts digital audio and drives headphones in one unit.
- D3.3.3.04 Phono preamplifier: stage that raises and equalises a phono cartridge signal to line level.

## D3.4 Loudspeakers

Leaf axis: system role (speakers placed in a room; sound for a TV).

### D3.4.1 Speakers
Kind axis: cabinet form and placement. Passive or active, ways, bass reach, radiation pattern, Atmos-enabled, battery, multi-room platform, outdoor rating (`standard_met`), `unit_of_sale` and `use` (computer among its values) are attributes.
- D3.4.1.01 Standmount (bookshelf) speaker: compact speaker cabinet made to stand on a stand, shelf or desk, passive or active.
- D3.4.1.02 Floor-standing speaker: tall speaker cabinet that stands on the floor.
- D3.4.1.03 Centre-channel speaker: speaker made to carry the centre channel of a surround system, placed at the screen.
- D3.4.1.04 Surround speaker: speaker made for the side, rear or height channels of a surround system.
- D3.4.1.05 In-wall/in-ceiling speaker: speaker without a cabinet, with a mounting flange, built into a wall or ceiling (C12(a)).
- D3.4.1.06 Subwoofer: speaker that reproduces only bass.
- D3.4.1.07 Single-enclosure speaker: self-contained speaker in one box that is neither a bar nor a bass-only speaker; wireless streaming, battery and multi-room membership are attributes, and a party speaker is a non-maker named form here (D-18).

### D3.4.2 Soundbars and TV sound
Kind axis: layout. Channel layout and format, Atmos, wall mounting and subwoofer included are attributes.
- D3.4.2.01 Soundbar: speaker made as a bar for a TV, with or without a separate subwoofer.
- D3.4.2.02 Home-cinema speaker system: package of speakers for a TV sold and compared as one system.

## D3.5 Headphones & earphones

Leaf axis: where the transducer sits (outside the ear; in or at the ear). Driver technology (dynamic, planar, electrostatic, balanced armature, hybrid), wired or wireless, ANC, impedance, sensitivity, `transmitter_base` and `use` are attributes.

### D3.5.1 Headphones
Kind axis: form and enclosure; headset by attached microphone.
- D3.5.1.01 Over-ear open-back headphone: headphone whose cups enclose the ear and are open at the back; semi-open files here.
- D3.5.1.02 Over-ear closed-back headphone: headphone whose sealed cups enclose the ear.
- D3.5.1.03 On-ear headphone: headphone whose pads rest on the ear.
- D3.5.1.04 Headset: headphones with an attached microphone, whatever they are used for (D1-O2).

### D3.5.2 Earphones
Kind axis: wearing form. Driver setup and ANC are attributes.
- D3.5.2.01 Universal in-ear monitor: sealing in-ear earphone with standard tips, sold for listening (K-143).
- D3.5.2.02 Custom in-ear monitor: in-ear earphone with shells moulded to one listener's ear, sold for listening (K-143).
- D3.5.2.03 Earbud (non-sealing): earphone that rests in the outer ear without sealing the canal.
- D3.5.2.04 True wireless earbuds: two separate wireless buds sold with a charging case (C10(b), D-3).
- D3.5.2.05 Bone-conduction / open-ear earphones: earphones that leave the ear canal open, by bone conduction or an open-ear driver.

## D3.6 All-in-one & complete systems

Leaf axis: what is in one housing (music system; receiver for broadcasts).

### D3.6.1 Music systems
Kind axis: what is in one housing.
- D3.6.1.01 Compact hi-fi system: music system with source, amplifier and speakers sold as one unit (`size_label`: mini, midi, lifestyle, music centre).
- D3.6.1.02 Radiogram: furniture-style cabinet combining a radio and a record player with speakers.
- D3.6.1.03 Boombox: portable radio-cassette or CD system with built-in speakers and a carry handle (D-15). †
- D3.6.1.04 Karaoke machine: machine that plays music for singing along with a microphone input.
- D3.6.1.05 Jukebox: machine that plays a selected record or track, however it is paid for, unless sold as an arcade or coin-operated game (K-146). †

### D3.6.2 Radios
Kind axis: receiver type.
- D3.6.2.01 Radio: broadcast receiver with a built-in speaker (`placement`: table, portable; D-18).
- D3.6.2.02 Clock radio: radio combined with a clock or alarm.
- D3.6.2.03 Radio scanner: receiver that scans and listens to radio frequencies (D2 §9.3). †

## D3.7 Voice, smart displays & hubs

No leaf (three kinds, leaf = null); kind ids carry no leaf part. Kind axis: whether there is a screen, then hub. The assistant platform and hub protocols are compatibility-ledger rows.
- D3.7.01 Smart speaker: speaker whose designed function is a voice assistant.
- D3.7.02 Smart display: voice-assistant device with a screen.
- D3.7.03 Smart-home hub: device that links and controls smart-home devices.

## D3.8 Parts and accessories made for one audio or video device

No leaf (closing parts sub-family, leaf = null; exempt from the role axis, C5(d), CV-17). Axis: object served (S3, step 8); fitting variants such as MM/MC cartridge type are attributes. If the harvest takes this well past about 12 kinds, leaves open with object served as the axis (CV-17).
- D3.8.01 Phono cartridge: pickup cartridge made to fit a turntable tonearm.
- D3.8.02 Turntable stylus: replacement stylus made for a phono cartridge. †
- D3.8.03 Tonearm: arm that carries the cartridge across the record, sold separately for a turntable. †
- D3.8.04 Headphone ear pads: replacement cushions made for a headphone. †
- D3.8.05 Earphone ear tips: replacement tips made for in-ear earphones. †
- D3.8.06 Detachable headphone cable with a proprietary or model-specific connector: cable made for one headphone model (K-2; standard-connector cables are D1). †
- D3.8.07 Projection screen: screen made for a projector to throw its image onto. †
- D3.8.08 Remote control: remote made for one TV or audio system; a universal remote is filed here by default (◇). †
- D3.8.09 TV antenna: aerial made to receive broadcast television for a TV or receiver. †
- D3.8.10 Speaker stand made for one speaker model: stand made to hold one speaker model. †
- D3.8.11 Screen or speaker mount: bracket, arm, wall mount or table stand made to hold one TV or speaker (K-8). †
- D3.8.12 Audio figure (Toniebox type): figure that plays its stored content when placed on its player (K-16). †

## Precedence inside D3

- A screen sold with television reception or as a television is D3.1.1.01; a screen made to connect to a computer and sold as a monitor is D1. The tuner is not the test: a tuner-less TV is still D3.1.1.01; how the maker sells it decides. Display technology is never a kind: OLED, Mini LED, plasma and CRT sets are all D3.1.1.01.
- An ultra-short-throw projector (body at the wall below the image) is D3.1.2.02; a standard or short-throw projector is D3.1.2.01, with throw ratio an attribute. A slide projector or cine film projector is D3.1.3.01 or D3.1.3.02 (D4 §9.8 files it here); film, cameras and enlargers are D4.
- A record player, CD player, cassette deck or disc player is D3 (D3.2.1.01, D3.2.2.01 to D3.2.2.03); the record, CD, tape or disc and blank recording media are F1. A cartridge is a part (D3.8.01), not part of the turntable kind.
- A streaming media player (D3.2.3.02) or set-top receiver (D3.2.3.03) is D3 (K-150); the app it runs is I1 and a catalogue subscription I3. A hi-fi network streamer is D3.2.3.01.
- A portable device sold mainly to play stored or streamed music, with no calling, is D3.2.4.01; one that is also a phone is D2; a Playaway-type player preloaded with one audiobook is F1 (F-8). A Toniebox-type player is D3.2.4.01 with `user = child` (default); its figures are D3.8.12 (K-16).
- An AV receiver is D3.3.2.01 by amplification stage, with video switching an attribute; a stereo receiver is D3.3.1.02.
- An external device whose designed function is converting digital audio or amplifying a headphone signal is D3.3.3.01, D3.3.3.02 or D3.3.3.03, a USB-C dongle included (`form = dongle`; K-150), and an external USB sound card sold as an audio converter with it; an audio card fitted inside a computer is D1 (S3); an audio interface sold for recording music is E3; a passive adapter or cable is D1; a microphone made for speech, calls or streaming is D1, and one sold for both music recording and speech is filed by the maker's stated first use (K-144).
- Computer speakers and speakers for listening are D3 whatever they plug into, filed by cabinet form with `use = computer` (memo section 14). An active pair with a built-in streaming amplifier is filed by its cabinet form (D3.4.1.01 or D3.4.1.02) with `amplification = active`; an all-in-one system with its own source (disc, radio, deck) is D3.6.1.01.
- A speaker made as a bar for a TV is D3.4.2.01, also with a wireless subwoofer, streaming or an assistant (attributes); a bass-only speaker is D3.4.1.06; a self-contained speaker that is neither is D3.4.1.07, including portable, Bluetooth, battery, multi-room and party speakers (D-18; a party speaker is a non-maker named form there).
- Sets are filed by their pieces (K-1, D3-O1): a 2.1 desktop set is its main speakers' kind with `unit_of_sale = set` and `channels = 2.1`; a home-cinema package sold and compared as one system is D3.4.2.02; a pair of one speaker is that speaker kind.
- A speaker, headphone or turntable sold by its maker as studio, stage, PA or DJ equipment is E3; the same type sold for listening is D3; a stage in-ear kit with a transmitter pack is E3; an in-ear monitor its maker sells as a hi-fi earphone is D3.5.2.01 or D3.5.2.02 (K-143).
- A semi-open headphone is D3.5.1.01. Built-in microphones without an attached boom do not make a headset: noise-cancelling headphones are D3.5.1.01 to D3.5.1.03. A headset (headphones with an attached microphone) is D3.5.1.04 whatever it is used for, gaming and calls included, and its boom microphone follows it (step 8); a VR headset, controller or console is D5. A wireless TV headphone set is an over-ear or on-ear kind with `transmitter_base = yes`. Electrostatic headphones are filed by form with `driver = electrostatic` (D-3).
- Glasses with a see-through display, camera or speakers are D2 smart glasses, not D3 headphones; a headset that encloses the eyes (VR or MR) is D5 (K-153).
- A device sold to compensate for hearing loss is H2; earbuds sold for audio with an optional hearing-assist mode are D3 (by wearing form, D3.5.2); ear defenders worn against noise are A1.
- A machine that plays recorded music, however it is paid for, is D3.6.1.05 unless sold as an arcade or coin-operated game (E1; coin-operated video cabinets are D5, K-146, K-155).
- A radio that receives broadcasts is D3.6.2.01 (table and portable are the `placement` attribute, D-18); a radio with a clock or alarm is D3.6.2.02; a clock that only keeps time is A5; a lamp that wakes by light is B3. A radio scanner is D3.6.2.03 (D2 §9.3); a two-way radio, pager or satellite messenger is D2.
- A device whose designed function is a voice assistant with speaker is D3.7.01, with a screen D3.7.02; a tablet or phone used as a smart display or speaker stays D2, also when sold with a dock. The assistant as software is I1.
- The primary job decides and connectivity is a modifier (D-14): a TV with a built-in soundbar is D3.1.1.01, a radio with a Bluetooth speaker D3.6.2.01, a smart display with a clock D3.7.02.
- A part made for one kind of object follows that object into D3.8 (step 8): cartridges, styli, tonearms, ear pads, ear tips, projection screens, remotes, antennas and speaker stands (D3.8.01 to D3.8.10); a cable with a proprietary connector made for one device follows it (D3.8.06, K-2), while cables with standard connectors are D1; a charger made for one device follows it and a generic charger is D1 (K-3); a bracket, arm, mount or table stand made to hold one TV or speaker is D3.8.11 (K-8; a monitor arm is D1); furniture, racks, shelves, TV cabinets and stands with shelves or storage are B1. A universal remote is D3.8.08 by default (◇).
- Audio made to be fitted in a vehicle is G1 (K-6); a home or portable speaker used in a car stays D3.
- A toy that imitates a music object and cannot do its job to the real object's standard is E1 (C15, CV-32); the real object in a child's size stays in its D3 kind with `user = child`.
