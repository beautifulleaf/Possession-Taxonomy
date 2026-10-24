# I3 Subscriptions, Memberships & Online Services: decided tree

Category: I3 Subscriptions, Memberships & Online Services (domain I, Software, Digital & Subscriptions). Membership test (key step 5, third branch): a subscription, membership or online utility service giving ongoing or periodic access to (a) a catalogue of content or play (music and audio, audiobooks and podcasts, film and TV, text, news and magazines, comics, recorded and streamed classes, game catalogues, streaming and online play, single-game subscriptions, in-game battle and season passes, creator memberships), (b) an online utility, free or paid (email, messaging, cloud storage and backup, maps and navigation, personal hosting), (c) connectivity (mobile phone and broadband plans), (d) a shared place, club or venue open to members, or a pass for venues, events or travel valid for a period or a number of visits (car-sharing memberships included), or (e) a recurring delivery of goods curated by the provider, picked by the member from a menu, allocated by a producer, or lent and returned (K-28, K-68, K-70, K-71). Not here: hosted tools valued for what the program does (password manager, VPN, AI assistant, office suite: I1); games and their expansions (D5); in-game items, digital purchases and licensed assets (I2); expired or used-up cards and passes, and physical SIM cards (F5); the goods a box, club or meal kit delivers (filed by what they are); one-off services, single tickets and journeys, one-off rentals, one-off travel eSIM packs, discount-, shipping- or points-only memberships (warehouse clubs included, section 14, provisional), loose credits and in-game currency, free social and ad-supported content platforms (step 1, OUT). Structure (Candidate A, decided I-3; memo sections 3 and 10): sub-family by what the plan gives access to (catalogue and play; online utility; connectivity; member place or pass; curated delivery), then leaf only in I3.1 (the medium of the catalogue) and I3.4 (what the member does there), none in I3.2, I3.3 and I3.5 (C5(b)), then kind (the generic service type within which buyers compare providers: how the catalogue is offered and how many titles it holds, the function, the connection, the way of entering, the arrangement of the delivery), then named form (the provider's service or line, maker-bound, or an agreed product sold by many operators, not maker-bound; not listed here). Each object gets one kind. Seat structure and eligibility, tier and the maker's ladder, term, ads, delivery (shared domain I value list), region, price, allowances (storage_gb, data_gb, speed_mbps, devices, cloud_hours, credits_per_period, audiobook_hours; section 14), live_access (on demand | live events | live channels, multi-valued, on the named forms of I3.1.3.01 and I3.1.3.02, a facet; section 14), connection technology and host network are plan or named-form attributes; content genre, sport, audience, goods type and site type or activity divide nothing (tags, links or views). Maker role: owner (maker_roles.tsv, provisional; the provider owns the service named form). Display only (navigation proposal and section 14; groups never change a home or an id): level 1 promotes the I3.1 medium leaves as Watch (I3.1.3), Listen (I3.1.1, I3.1.2), Read (I3.1.4, I3.1.5), Play (I3.1.7), Classes and wellness (I3.1.6), Bundles and creator memberships (I3.1.9), then Online services and storage (I3.2, with I3.1.8.01 shown here for display only), Phone and internet (I3.3), Memberships and passes (I3.4) and Boxes and clubs (I3.5); quality markers (display): for streaming and catalogues, has the titles you want, annualised price and the ad-free tier's price, picture and sound quality, simultaneous streams and seats, devices, term and ease of cancelling, free trial; for connectivity, coverage, speed, reliability, satisfaction and complaints, value, roaming, perks and family plans; for memberships, passes and boxes, reach of sites or venues, price, curation and flexibility (provisional). Pending kinds: the memo marks 24 kinds provisional (†: named by the key, a classification line, a decision or a review example, with no fetched page showing the type); their ids are allocated here in memo order (wave-2 convention), each line ending in †, and a † kind enters the data only when a fetched page attests it (memo section 10 attestation list; I-17, I-22, K-70). Leaves that hold only † kinds (I3.1.5, I3.1.8, I3.4.4) are provisional with them. If no provider page attests I3.1.3.02 it folds into I3.1.3.01 with live_access = live channels (section 14); if none attests I3.1.3.03 or I3.3.04 they fold into I3.1.3.01 and I3.3.03 with a `technology` attribute; if no renewing plan attests I3.3.07, a renewing travel plan files under I3.3.01 or I3.3.02 with eSIM as an attribute (memo risks).

Ids (R-58): I3.n is a sub-family and I3.n.m a leaf; a kind is I3.n.m.kk, or I3.n.kk where a sub-family has no leaf.

## I3.1 Catalogue and play access

Leaf axis: the medium of the catalogue. Kind axis inside a leaf: how the catalogue is offered (on-demand library, live or linear, periodical delivery, season pass); for periodicals, how many titles the plan holds (print or digital is the plan attribute `delivery`); in Several media, whether the plan bundles several services or gives one creator's mixed feed. Order (memo section 8): on-demand library before live or linear before periodical delivery; one-title periodical before many-title library.

### I3.1.1 Music and audio
- I3.1.1.01 Music streaming subscription: plan giving on-demand access to a library of recorded music.
- I3.1.1.02 Satellite and internet radio subscription: paid subscription to a network of radio channels received by satellite or over the internet. †

### I3.1.2 Audiobooks and podcasts
- I3.1.2.01 Audiobook catalogue subscription: plan giving access to a catalogue of audiobooks to listen to while subscribed (credits it renews are a plan attribute; titles bought with them are I2).
- I3.1.2.02 Paid podcast subscription: paid plan giving access to one or more podcasts' paid episodes or feeds. †

### I3.1.3 Video (film and TV)
- I3.1.3.01 On-demand streaming video subscription: plan giving on-demand access to a streamed library of film, series or sport (SVOD, OTT; a live-sport service is here).
- I3.1.3.02 Live-TV streaming bundle: plan streaming a bundle of linear TV channels over the internet (vMVPD). †
- I3.1.3.03 Pay-TV package (cable, satellite, IPTV): subscription package of TV channels delivered by cable, satellite or IPTV, unless named for the line. †

### I3.1.4 Text, news and periodicals
- I3.1.4.01 Newspaper subscription (one title): subscription to one newspaper title, delivered in print, digitally or both. †
- I3.1.4.02 Magazine subscription (one title): subscription to one magazine title, delivered in print, digitally or both. †
- I3.1.4.03 News and magazine library subscription (many titles): plan giving access to a library of many newspaper and magazine titles.
- I3.1.4.04 E-book library subscription: plan giving access to a library of e-books to read while subscribed.

### I3.1.5 Comics
Leaf provisional until its kind is attested (its only kind is †).
- I3.1.5.01 Comic and manga library subscription: plan giving access to a library of comics or manga to read while subscribed. †

### I3.1.6 Classes (recorded and streamed)
- I3.1.6.01 Recorded class subscription: plan giving access to a library of recorded or streamed lessons, sessions or classes to watch or listen to (the subject divides nothing, I-20).

### I3.1.7 Games
- I3.1.7.01 Game subscription (catalogue, online play, cloud): plan giving access to a catalogue of games, online play or cloud play on a platform or store.
- I3.1.7.02 Single-game subscription: subscription required or sold to play one game.
- I3.1.7.03 In-game season or battle pass: pass bought for a season of one game that unlocks its reward track.

### I3.1.8 Production assets
Leaf provisional until its kind is attested (its only kind is †).
- I3.1.8.01 Asset-library subscription: plan giving access to a library of images, video, sounds, fonts or templates for making work (each asset licensed under it is I2). †

### I3.1.9 Several media (bundles and mixed catalogues)
- I3.1.9.01 Multi-service bundle: one plan bundling several subscription services, filed here when named for none of its components.
- I3.1.9.02 Creator membership: paid membership giving one creator's paid posts, channel or feed, whatever the medium (a free follow is OUT). †

## I3.2 Online utility services

No leaf (leaf = null). Kind axis: the function of the service.

- I3.2.01 Cloud storage and sync plan: plan giving online storage for the user's files, with sync between devices.
- I3.2.02 Online backup plan: plan keeping the user's backup on the provider's servers, even with its own client program. †
- I3.2.03 Email service: mailbox and address service, free or paid (a program used only to read and send mail is I1). †
- I3.2.04 Messaging, calling and video-conferencing service: service for sending messages and making voice or video calls and meetings over the internet. †
- I3.2.05 Maps and navigation service: online map and route-finding service, free or paid. †
- I3.2.06 Personal hosting plan (web hosting, game server): plan renting server space for a personal website or game server (hosting sold as business infrastructure is not filed). †

## I3.3 Connectivity plans

No leaf (leaf = null). Kind axis: the connection. Order: mobile phone plan before data-only, fixed, satellite, bundle.

- I3.3.01 Mobile phone plan (Handytarif): mobile plan for calls, texts and data on a SIM or eSIM, contract or prepaid, with or without a handset (the handset is its own object).
- I3.3.02 Mobile data plan (data-only SIM, dongle, router): mobile plan giving data only, for a data SIM, dongle or mobile router.
- I3.3.03 Fixed-line broadband plan: home internet plan over a fixed line (fibre, copper or cable as `technology`).
- I3.3.04 Satellite internet plan: home internet plan delivered by satellite through a dish. †
- I3.3.05 Home phone line plan: plan for a fixed home telephone line. †
- I3.3.06 Bundled connectivity package (phone, internet, TV) (Kombi-Tarif): one plan bundling a connection with phone or TV, named and sold for the line. †
- I3.3.07 Renewing travel eSIM plan: travel data plan on an eSIM that renews each period (one-off packs are OUT). †

## I3.4 Member places and passes

Leaf axis: what the member does there. Kind axis: the way of entering. The type of site or activity (heritage, museum, zoo, tennis, golf) is a tag, never a kind.

### I3.4.1 Facility or group
- I3.4.1.01 Facility membership: membership of one operator's facility or facilities (gym, pool, sports centre, climbing wall). †
- I3.4.1.02 Members' club: membership of a club joined to take part in its activity (sports, social or hobby). †
- I3.4.1.03 Multi-studio class pass: pass giving bookings at classes across many studios, often paid in renewing credits (`credits_per_period` a plan attribute).

### I3.4.2 Site or collection
- I3.4.2.01 Multi-site membership: membership giving entry to one body's network of sites.
- I3.4.2.02 Multi-venue pass scheme: pass giving entry to many bodies' venues under one scheme.
- I3.4.2.03 Single-venue annual pass: annual pass or membership for one museum, zoo, garden, aquarium or theme park. †

### I3.4.3 Travel
- I3.4.3.01 Period transit pass (定期券): pass for travel on a network or route valid for a period or a number of journeys (alias: season ticket, UK rail).
- I3.4.3.02 Car-sharing membership: membership giving access to a shared vehicle fleet (trips, hire fees and fuel are one-off services, OUT). †

### I3.4.4 Series
Leaf provisional until its kind is attested (its only kind is †).
- I3.4.4.01 Season ticket (venue, club or event series): ticket giving entry to a season or series of events at a venue or of a club. †

## I3.5 Curated deliveries

No leaf (leaf = null). Kind axis: the arrangement of the delivery (who chooses what arrives; or goods lent and returned). The goods type (wine, coffee, beauty, pets) is a link to the goods' own kind, never a kind (I-19). Order: provider-curated box, member-selected menu plan, producer allocation club, goods rental.

- I3.5.01 Provider-curated box: recurring delivery whose contents the provider picks, including a merchant's case plan.
- I3.5.02 Member-selected menu plan: recurring delivery whose contents the member picks from the provider's menu (meal kits, coffee, books).
- I3.5.03 Producer allocation club: a producer's own club that allocates its own goods to members on a schedule.
- I3.5.04 Goods rental subscription: subscription lending goods to be used and returned (clothes, furniture, toys, instruments, art; the rented goods are not owned and not filed). †

## Precedence inside I3

- Bundles: a bundle is filed by the component it is named and sold for (JioFiber, named for broadband, is I3.3.03; iCloud+ and Google One are I3.2.01); a bundle named for none of its components is the multi-service bundle (I3.1.9.01: Apple One, Amazon Prime). A bundle crossing into I1 follows the same rule (Microsoft 365 and Google AI Pro 5 TB are I1; Google One Basic is I3.2.01; P1).
- TV over a line: a TV package is the pay-TV package (I3.1.3.03), an IPTV package sold by a broadband provider included, unless it is named for the line; a "triple play" named for the line is the bundled connectivity package (I3.3.06).
- Sport and genre divide nothing: a live-sport or sports streaming service (DAZN type) is on-demand streaming video (I3.1.3.01) with `live_access`; the live-TV streaming bundle (I3.1.3.02) is for linear channel bundles (section 14).
- Periodicals: one title is a newspaper or magazine subscription (I3.1.4.01, I3.1.4.02) whether print or digital; many titles are the library (I3.1.4.03); delivery is a plan attribute; an issue kept is F1.
- Member places by way of entering: one operator's facility is a facility membership (I3.4.1.01, the activities are tags); a club joined to take part is a members' club (I3.4.1.02); classes booked across many studios are a multi-studio class pass (I3.4.1.03, ClassPass, K-71(j)); one body's network of sites is a multi-site membership (I3.4.2.01); many bodies' venues are a multi-venue pass scheme (I3.4.2.02); one venue is a single-venue annual pass (I3.4.2.03, Kew Gardens); a season or series is a season ticket (I3.4.4.01).
- Homonym "season ticket": UK rail is a period transit pass (I3.4.3.01); venue or club is a season ticket (I3.4.4.01). "Pass" names a game subscription (I3.1.7.01, Game Pass), a season pass (I3.1.7.03, Battle Pass), a multi-venue pass scheme (I3.4.2.02, National Art Pass) or a discount card (Railcard, OUT).
- Curated deliveries by who chooses: the provider picks (I3.5.01, a merchant's case plan included, since a merchant is not a producer); the member picks from a menu (I3.5.02); a producer allocates its own goods (I3.5.03; a winery club with venue benefits stays here, the benefits are attributes); goods lent and returned (I3.5.04). The plan is filed as the plan and each item delivered by what it is; a repeat order at a fixed price with no curation, membership or access is not filed (P5).
- P2: a game subscription or paid store subscription is I3.1.7.01 and a battle pass I3.1.7.03; games and expansions are D5, in-game items I2; credits and in-game currency are OUT, and what they buy is filed by what it is. An asset-library plan is I3.1.8.01 and each licensed asset I2.
- P3, P13: a membership, pass or season ticket is I3 while valid, whatever its form; once expired or used up the card or paper kept is F5. A membership carried by an NFT is I2 unless the same access is also sold as a plan, which is filed once as the plan.
- P4 and section 14: a plan whose only benefit is a discount, shipping, points or buying goods at member prices is OUT (Railcard, Prime Shipping, warehouse clubs), but one that also gives a catalogue is I3 (Prime with Video, I3.1.9.01); a ticket for one journey or event is OUT, a period pass is I3.4.3.01; a one-off rental is OUT; a free tier of a paid service is a plan row in band "0 (free)".
- P6, P14: a connection plan is I3.3 and any handset, router, modem or set-top box sold with it is its own object (D1, D2, D3); an eSIM profile is part of its plan (I3.3.01, I3.3.02, I3.3.07); a physical SIM card is F5.
- P7: membership of a place shared by all members is I3.4; a specific space for the person's own use is a right (OUT).
- P8: a library of recorded or streamed lessons, sessions or classes is I3.1.6.01; a program that does the exercise with the user is I1.
- P9: a plan keeping the backup on the provider's servers is I3.2.02, even with its own client; backup software to the owner's drives, or a security or backup program that includes cloud space, is I1.
- P10: a map or navigation service is I3.2.05; GIS software is I1.
- P11: a paid unlock of a function built into one device is I1; a data connection plan for that device is I3.3; a class catalogue for one device is I3.1.6.01.
- P12: a plan that renews credits is filed as the plan, by what the credits reach (I3.4.1.03 for venues, I3.1.2.01 for a catalogue), with `credits_per_period`; loose credits are OUT.
- P15: goods-rental subscriptions (I3.5.04), personal hosting plans (I3.2.06), creator memberships (I3.1.9.02) and car-sharing memberships (I3.4.3.02) are I3; a travel eSIM and other one-off packs are OUT unless they renew (I3.3.07).
- Messaging and mail: a mailbox or address service is I3.2.03 and messaging and conferencing services I3.2.04; a program used only to read and send mail is I1.
