import json, os
FW="https://en.wikipedia.org/wiki/Fireworks"
SK="https://en.wikipedia.org/wiki/Skyrocket"
FC="https://en.wikipedia.org/wiki/Firecracker"
SP="https://en.wikipedia.org/wiki/Sparkler"
GAL="https://www.galacticfireworks.co.uk/collections/brothers-pyrotechnics?page=4"
def eff(n,d,a=""):
    return {"n":n,"a":a,"d":d,"mk":"","y":"","s":FW}
BP="Brothers Pyrotechnics"
kinds=[
{"n":"Firework cake","a":"barrage · compound · repeater","d":"Cluster of tubes linked by one fuse that fires a timed series of aerial effects.",
 "t":["Single-shot barrage","Compound (several cakes fused together)","Peony, willow, palm, crossette, crackle effects","EU F2 / F3 · UK Category 2 / 3"],
 "s":"https://dynamicfireworks.co.uk/firework-cakes-barrages/",
 "m":[["Infamous",BP],["Houdini",BP],["RS3",BP],["Primeval",BP],["Starry Nights",BP],["Angel Dust XL",BP],["Carnage",BP],["Indestructible",BP],["Bangalangers",BP],
      ["Beast From The East","Evo Fireworks"],["The Lost World","Evo Fireworks"],["Toxic","Evo Fireworks"],
      ["Bellagio","Primed Pyrotechnics"],["Flush Fury","Primed Pyrotechnics"],["Full House","Primed Pyrotechnics"],["High Roller","Primed Pyrotechnics"],["Poker Punch","Primed Pyrotechnics"],
      ["1UP","Pyroworx"],["Gum Ball","Pyroworx"]]},
{"n":"Firework rocket","a":"skyrocket · rocket","d":"Firework driven upward by its own solid-fuel motor, steadied by a stick or fins, that bursts near the top of its climb.",
 "t":["Stick-stabilised","Fin-stabilised","Single or pack","UK sizes by motor weight"],
 "s":"https://dynamicfireworks.co.uk/firework-cakes-barrages/",
 "x":[{"n":"Bottle rocket","a":"","d":"Small, cheap black-powder skyrocket on a thin bamboo splint, often sold by the pack or gross.","mk":"","y":"early 20th century","s":SK,"dt":"pack size · report or whistle"},
      {"n":"Whistle rocket","a":"","d":"Rocket that burns whistle mix instead of black powder, screaming as it climbs.","mk":"","y":"","s":SK,"dt":"size · burst or report"}],
 "m":[["Space X",BP]]},
{"n":"Aerial shell","a":"consumer mortar · shell kit · reloadable","d":"Shell fired from a mortar tube that bursts high in the air into a patterned break of stars.",
 "t":["Reloadable shell kit with tube","Single or multi-break","Calibre"],
 "s":FW,
 "x":[eff("Peony","Spherical burst of coloured stars without tails; the most common shell type."),
      eff("Chrysanthemum","Spherical burst of coloured stars that leave visible spark trails."),
      eff("Dahlia","Spherical burst with fewer, larger stars that travel farther."),
      eff("Willow","Chrysanthemum with long-burning silver or gold stars that droop into a dome."),
      eff("Kamuro","Chrysanthemum of dense glittering silver or gold stars with a heavy glitter trail."),
      eff("Palm","A few large comet stars with a thick rising tail, like a palm tree."),
      eff("Crossette","Large stars that split into smaller stars in a criss-cross pattern."),
      eff("Horsetail","Directional burst of heavy tailed stars falling a short way.","waterfall shell"),
      eff("Ring","Stars bursting in a circle; variants form hearts or smiley faces."),
      eff("Spider","Fast-burning tailed stars forming radial lines like spider legs."),
      eff("Fish","Stars that dart rapidly away from the burst."),
      eff("Time rain","Large, slow-burning stars that leave glittering, sizzling sparks."),
      eff("Salute","Quick flash of flash powder followed by a loud report.")]},
{"n":"Roman candle","a":"","d":"Long tube that fires stars or small shells one after another at regular intervals.",
 "t":["Shot count","Stars or comet shells","Single tube or pack"],
 "s":"https://dynamicfireworks.co.uk/firework-cakes-barrages/"},
{"n":"Mine","a":"pot à feu · ground mine","d":"Mortar-launched canister that throws all its stars and effects upward at once.",
 "t":["Single mine","Multi-shot mine","Stars, comets or crackling"],
 "s":FW},
{"n":"Firework fountain","a":"gerb","d":"Ground firework that throws up a cone of sparks.",
 "t":["Ground fountain","Hand-held or stake fountain","Indoor cake fountain (ice fountain)","Coloured, crackling or glitter"],
 "s":"https://dynamicfireworks.co.uk/firework-cakes-barrages/",
 "m":[["Chunky Monkey",BP],["Leaping Lizards",BP],["Laser",BP],["Ice Fountain",BP]]},
{"n":"Catherine wheel","a":"pinwheel","d":"Spinning firework on a pin, driven by a powder-filled spiral tube or angled rockets.",
 "t":["Spiral tube","Rocket-driven","Nailed or post-mounted"],
 "s":"https://dynamicfireworks.co.uk/firework-cakes-barrages/"},
{"n":"Ground spinner","a":"spinner · ground bloom","d":"Small firework that spins on the ground throwing a circle of sparks.",
 "t":["Ground spinner","Flying spinner"],
 "s":FW},
{"n":"Firecracker","a":"banger · cracker · bao zhu","d":"Small paper-cased explosive with a fuse, made mainly for a loud bang.",
 "t":["Single cracker","String or roll","Black powder or flash powder"],
 "s":FC,
 "x":[{"n":"Mandarin cracker string","a":"red firecracker string","d":"Strings of small black-powder crackers, mostly red, braided to fire in sequence.","mk":"","y":"before 1920s","s":FC,"dt":"string length · red with a few yellow or green"},
      {"n":"Flash cracker","a":"flash-light cracker","d":"Cracker filled with flash powder for a sharper, brighter bang.","mk":"","y":"c. 1924 onward","s":FC,"dt":"size · label brand (many short-lived 1920s–1970s labels)"},
      {"n":"Cherry bomb","a":"globe salute · kraft salute","d":"Round red salute with a green fuse like a cherry stem; full-power versions banned for US consumers in 1966.","mk":"","y":"1920s–1940s","s":"https://en.wikipedia.org/wiki/Cherry_bomb","dt":"¾–1½ in diameter · colour"},
      {"n":"Bang snap","a":"popper · whipper snapper · snap","d":"Tiny paper twist of gravel and a trace of silver fulminate that pops when thrown.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Bang_snap","dt":"pack size"}]},
{"n":"Smoke device","a":"smoke bomb · coloured smoke · smoke grenade","d":"Firework that releases a large volume of coloured or white smoke.",
 "t":["Coloured smoke","Pull-ring or fuse","Hand-held or ground"],
 "s":"https://en.wikipedia.org/wiki/Smoke_bomb"},
{"n":"Sparkler","a":"phuljhadi","d":"Hand-held wire coated with a slow-burning pyrotechnic that throws sparks.",
 "t":["Length","White, gold or coloured sparks","Heart and shaped wires"],
 "s":"https://www.galacticfireworks.co.uk/collections/pyrotechnics?page=9",
 "x":[{"n":"Wire sparkler","a":"","d":"Thin metal wire, about 20–30 cm, dipped in metal-fuel composition; the fuel sets the spark colour.","mk":"","y":"","s":SP,"dt":"length · aluminium, iron, titanium or ferrotitanium sparks"},
      {"n":"Senko hanabi","a":"Japanese incense-stick sparkler","d":"Twisted tissue-paper stick about 20 cm long tipped with a few grains of black powder, giving fine branching sparks.","mk":"","y":"essays from 1927","s":"https://en.wikipedia.org/wiki/Senko_hanabi","dt":"paper colour · stick length"}]},
]
brands=[
{"n":BP,"c":"United States","seg":"consumer fireworks (made in China)","d":"Fireworks brand known for award-winning cake and compound effects, sold widely in the UK.","lines":[],"sig":["Infamous","Houdini","RS3"],"rel":[],"s":GAL},
{"n":"Standard Fireworks","c":"United Kingdom","f":"1891","seg":"consumer fireworks","d":"Huddersfield firework maker founded by James Greenhalgh; UK production ended in 1998 and the name is now a Black Cat brand.","rel":["Black Cat Fireworks","Brocks Fireworks"],"s":"https://en.wikipedia.org/wiki/Standard_Fireworks"},
{"n":"Brocks Fireworks","c":"United Kingdom","f":"1698","seg":"consumer and display fireworks","d":"Oldest British firework maker, founded by John Brock in Islington; bought by Standard Fireworks in 1988.","rel":["Standard Fireworks"],"s":"https://en.wikipedia.org/wiki/Brocks_Fireworks"},
{"n":"Black Cat Fireworks","c":"China","seg":"consumer fireworks","d":"China-based fireworks company that bought Standard Fireworks in 1998 and trades in the UK under several names.","rel":["Standard Fireworks"],"s":"https://en.wikipedia.org/wiki/Standard_Fireworks"},
{"n":"Weco","c":"Germany","f":"1948","seg":"consumer fireworks","d":"Germany's largest consumer fireworks maker, based in Eitorf.","s":"knowledge"},
]
trads=[{"n":"Liuyang fireworks","g":"Fireworks & pyrotechnics","r":"Liuyang, Hunan, China","p":"Northern Song dynasty to present","d":"China's main centre of firework and firecracker making for over 1,400 years, exporting since 1875.","tech":"hand and factory filling of paper-cased crackers and shells","mat":"black powder, paper, clay","forms":["Firecracker","Aerial shell","Firework cake"],"ctr":["Liuyang (30+ fireworks companies)"],"auth":"Liuyang fireworks are a protected origin product","s":"https://en.wikipedia.org/wiki/Liuyang"}]
notes=("Old 'Other fireworks' dissolved: Brothers/Evo/Primed/Pyroworx items into Firework cake (planner says mostly cakes; Bangalangers type unconfirmed), Space X moved to Firework rocket (retailer lists it as a rocket). "
 "Effect types (peony…salute) are archetypes of Aerial shell, sourced to Wikipedia Fireworks, and appear as t on cakes; strobe not attested so left out. "
 "Dept brief suggestion: classes EU F1–F4 (F2 sold to over-18s; F3/F4 not to consumers in Germany), UK Categories 1–4 (Cat 1 16+, Cat 2–3 18+, Cat 4 professionals only) per Wikipedia Fireworks; US consumer class 1.4G is from knowledge — to verify. "
 "Brands left out: Epic Fireworks (only a search snippet: Batley showroom), Zena (nothing found), Cobra (Cobra Firing Systems is a firing-system maker, not a firework brand; a 'Firing system' kind could be added if wanted). Black Cat Fireworks Wikipedia title redirects to Li & Fung, so Black Cat cites the Standard Fireworks page. "
 "No versions added: none confirmed. Liuyang added as a tradition; Japanese hanabi tradition not added (no source retrieved).")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p="/home/user/Possession-Taxonomy/rebuild/work/B4/shelves/03_03.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
