step0: read briefs; baseline: out/C1.json has no m kinds (step1 already done by V4); backup in bak/. gaps.md stale.
step2: fetched Leatherman table, Metabo(Germany 1924, KKR via HK Holdings 2017), Einhell(Germany 1964), Ridgid(US 1923, Emerson), B+D(1910 US, SBD 2010). Next: Victorinox models, Mora, Stanley #14/#53/#91, EGO, AEG, Porter-Cable, Buck112, Spyderco locks, Facom/KTC/Koken, Hakko
step3: Victorinox sakwiki 91mm list fetched (names only, no years); Mora wiki: no years (searched twice -> leave empty); Chervon wiki 404
step4: Stanley #14/#53/#91 resolved: no such planes (stan3/7/11 pages). Porter-Cable US 1906 SBD 2004 (Pentair Tools Group sold to Black & Decker Oct 2004). AEG wiki disambig only. EGO: Chervon, 56V (WJ), no founding/launch fetched
step5: Spyderco(US,1978,Worker 1981), Kershaw(US 1974,KAI), OKC(US,1889), Ka-Bar(US, KA-BAR name 1923, Cutco sub) fetched; Cold Steel page was disambig
step6: fetched ESEE (1997, Rowen Idaho Falls), Nite Ize (Boulder, ~1989 per '30 years ago'), Cold Steel (US 1980, GSM 2020, TRI-AD), Buck (US 1947, 110=1964), Facom (France 1918, Fimalac 1999; Stanley link not fetched), Circlip, Pipe bending. Hakko FX-888D: DigiKey 2018 blog, no country. Delica/Leek/Voyager/Buck112 locks: 2 attempts failed
step7: KTC (Japan, 1947 implied), Koken(no year), sakwiki 93/111/100mm fetched, Lie-Nielsen adapted Stanley #95 in 1981. Next: search sakwiki 58/84/74mm, Wikipedia Victorinox SwissTool year; then WRITE edit script (ed.py) in this dir
step8: fetched sakwiki 58/84x4 (total fetches ~46). NEXT: write ed.py applying all edits (leatherman versions, swiss list, battery own/g, brand adds Porter-Cable/Metabo/Einhell/Ridgid, planes complete lines, kinds circlip/pipe bender/thermal cam, brands json) then validate + report
step9: ed.py applied (do NOT rerun; backup in bak/). validate OK. Remaining: patch os field, friction xg, report
step10: report written; done
ROUND2 started: tasks 1 sakwiki 65/74/75/130/84-5layer/Wenger+Delemont 85; 2 Veritas via Lee Valley; 3 lock types; 4 Morakniv history. ed.py already applied in round 1 - write new script ed2.py operating on current out/C1.json (backup bak/C1_r2.json)
