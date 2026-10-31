step1 done: read existing A4 depts (existing.txt), backup in bak/
step2 done: fetched houses Dior/Hermes/Chanel/Celine/Prada/Loewe/LV(links)/Fendi; owners LVMH/Kering/Tapestry/Capri/Richemont; eyewear EL/Safilo/Marcolin/RayBan/Persol/Moscot/Oakley; luggage Rimowa/Samsonite/Tumi; packs Osprey/Gregory/Deuter/Fjallraven/Eastpak/JanSport/Herschel
step3 todo: fetch Ergobaby, BabyBjorn, Babywearing; then build part file via build.py script in this dir
step3 done: ALL.json built via build_part.py, validated
done
step4 start: round 2 (houses, owners, eyewear, luggage); data.py/build_part.py are the sources, append to them
r2 fetched (lines in transcript, to encode in data2.py): Goyard bags page, Mulberry women bags, Coach view-all page, Longchamp le-pliage-by-collection (WebFetch), Gucci handbags (lines list + categories), YSL all-handbags, Bottega women-bags, Balenciaga bags-for-women, Valentino bags (WebFetch), Miu Miu arcadie page (bag lines), Jacquemus bambinos page, Polene numero-un (collections), Givenchy women bags.
r2 todo: LV women+men, Fendi full, Kate Spade, Michael Kors, Marc Jacobs, Telfar; owners (Osprey, Fjallraven, Eastpak, JanSport, Herschel, Bellroy, Ergobaby, Globe-Trotter); eyewear (RayBan, Oakley, Persol, Warby Parker, Gentle Monster, Tom Ford, EL annual report); luggage (Away, Monos, Briggs&Riley, Samsonite brands)
RULE 2: shape kind only where fetched page names it; else general kind Shoulder bag and say so in sel; re-place earlier Dior/Celine/Prada/Loewe/LV/Chanel22/25/Longchamp/Kalimero entries accordingly
