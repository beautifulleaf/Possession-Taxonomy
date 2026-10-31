import json, os
W="https://en.wikipedia.org/wiki/"
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Essential oil","a":"volatile oil · ethereal oil · natural oil","d":"Volatile aromatic oil distilled or pressed from plant material, used neat or diluted as a perfumery natural.",
 "t":["steam-distilled","cold-pressed (expressed)","single origin","neat or pre-diluted"],"s":W+"Essential_oil",
 "x":[
  X("Mysore sandalwood oil","Distilled heartwood oil of Indian sandalwood (Santalum album), rich in santalol; scarce and costly.","","1917",W+"Santalum_album",
    [("Indian sandalwood (S. album)","","","about 90% santalol; ISO 3518 standard"),("Australian sandalwood (S. spicatum)","","","cheaper, about 39% santalol"),("New Caledonian sandalwood (S. austrocaledonicum)","","","alternative source")],
    "origin · santalol content · age of heartwood · sustainable plantation vs wild","Indian sandalwood oil · white sandalwood oil"),
  X("Haitian vetiver","Root oil of vetiver grass; Haiti is a leading producer of the floral-leaning grade.","","",W+"Vetiver",
    [("Haiti","","","floral quality"),("Bourbon vetiver (Réunion)","","","floral quality, prized"),("Java vetiver","","","smokier"),("Khus (north India, wild)","","","traditional oil")],
    "origin · smoky vs clean · age","vetiver oil · khus oil"),
  X("Bergamot oil","Cold-pressed rind oil of the bergamot orange; a standard citrus top note.","","",W+"Bergamot_essential_oil",[],"origin · cold-pressed","bergamot essential oil"),
  X("Lavender oil","Oil distilled from lavender flower spikes; a fougère staple.","","",W+"Lavender_oil",
    [("Lavender flower oil","","","from true lavender"),("Lavender spike oil","","","from Lavandula latifolia")],"species · altitude · origin"),
  X("Rose otto","Steam-distilled oil of rose petals, among the most used and costly naturals.","","",W+"Rose_oil",
    [("Rose otto","","","steam distilled"),("Rose absolute","","","solvent extracted; see Absolute & CO2 extract")],"origin · rose species","attar of roses · rose essence"),
  X("Neroli","Oil distilled from bitter orange blossom; honeyed, slightly metallic.","","",W+"Neroli",
    [("Neroli oil","","","distilled"),("Orange blossom extract","","","different extraction; sweeter, warmer")],"extraction method · origin"),
  X("Patchouli oil","Oil from the leaves of Pogostemon cablin, an earthy base note.","","",W+"Patchouli",[],"origin · aged vs fresh"),
  X("Cedarwood oil","Oil from various conifers in the pine and cypress families, a dry woody base.","","",W+"Cedar_oil",[],"species · wood or foliage","cedar oil"),
 ]},
{"n":"Absolute & CO2 extract","a":"absolute · concrete · CO2 extract · resinoid","d":"Concentrated plant extract made by solvent, enfleurage or supercritical CO2 extraction rather than distillation.",
 "t":["absolute (solvent extraction)","concrete (waxy first extract)","enfleurage","CO2 extract (supercritical)","resinoid"],"s":W+"Absolute_(perfumery)",
 "x":[
  X("Orris butter","Waxy oil from iris rhizomes dried for years; one of the costliest perfumery materials.","","",W+"Orris_root",
    [("Iris pallida orris","","",""),("Iris germanica orris","","","")],"iris species · drying age · butter or absolute","orris root butter · butter of iris"),
  X("Rose absolute","Solvent-extracted rose petal extract, used more than rose otto in perfumery.","","",W+"Rose_oil",[],"origin · rose species"),
  X("Oakmoss absolute","Lichen extract (Evernia prunastri) that anchors chypres and fougères; now heavily IFRA-restricted.","","",W+"Oakmoss",
    [("Oakmoss absolute","","","Evernia prunastri, extracted in Grasse"),("Pseudevernia furfuracea substitute","","","used in place of oakmoss")],"species · restricted-use compliance"),
 ]},
{"n":"Aroma chemical","a":"aromachemical · aroma molecule · isolate · synthetic","d":"Single fragrance molecule, synthetic or isolated, sold to hobby perfumers neat or diluted.",
 "t":["neat","10% dilution in DPG or ethanol","natural isolate","captive (house-exclusive) vs commodity","IFRA-restricted"],"s":W+"Fragrance_compound",
 "x":[
  X("Coumarin","Tonka-bean molecule with a sweet hay scent; the first synthetic used in a classic perfume.","","1868",W+"Coumarin",
    [("Isolated from tonka beans","","1820","A. Vogel; named by N. Guibourt"),("First synthesis","","1868","W. H. Perkin"),("Fougère Royale","Houbigant","1882","first perfume use")],"restriction level · purity"),
  X("Vanillin","Main odorant of vanilla; synthetic vanillin largely replaces natural extract.","","",W+"Vanillin",[],"synthetic vs natural-derived"),
  X("Ethyl vanillin","Homologue of vanillin with a stronger vanilla note.","","",W+"Ethylvanillin",[],"purity","ethylvanillin"),
  X("Hedione","Methyl dihydrojasmonate, a transparent jasmine-citrus floral.","Firmenich","1962",W+"Methyl_dihydrojasmonate",
    [("Characterised and synthesised by Edouard Demole","Firmenich","1957–1962",""),("Eau Sauvage","Christian Dior","1966","first commercial success using it")],"racemic vs epimerised","methyl dihydrojasmonate · kharismal"),
  X("Galaxolide","Polycyclic synthetic musk with a clean, sweet, floral-woody odour.","IFF","1965",W+"Galaxolide",[],"dilution (often sold pre-diluted)","HHCB · Abbalide · Pearlide"),
  X("Calone","Methylbenzodioxepinone, the 'watermelon ketone' behind marine and ozonic perfumes.","Pfizer","1966",W+"Calone",[],"dilution","Calone 1951 · watermelon ketone"),
  X("Iso E Super","OTNE, a velvety woody-amber molecule used in large doses.","IFF","1973",W+"Tetramethyl_acetyloctahydronaphthalenes",
    [("Created by John Hall and James Milton Sanders","IFF","1973","patented 1975"),("Fahrenheit","Christian Dior","1988","about 25%"),("Féminité du Bois","Shiseido","1992","about 43%"),("Terre d'Hermès","Hermès","2006","about 55%"),("Molecule 01","Escentric Molecules","2006","diluted Iso E Super alone")],
    "isomer enrichment · trade name","OTNE · Iso Gamma Super · Orbitone"),
  X("Cashmeran","Musk indanone with a spicy, musky, woody and clean odour.","IFF","1973",W+"Cashmeran",[("Discovered by John Hall","IFF","1973","US patent 3,773,836")],"purity","DPMI · musk indanone"),
  X("Ambroxide","Ambergris odorant with woody, musky, slightly salty facets; the modern stand-in for ambergris.","","",W+"Ambroxide",
    [("Ambrox","Firmenich","",""),("Ambrofix","Givaudan","",""),("Ambroxan","Kao","","")],"trade name · purity","Ambroxan · Ambrox · Ambrofix"),
  X("Muscone","Macrocyclic ketone that gives deer musk its smell; almost all used today is synthetic.","","",W+"Muscone",[],"synthetic vs natural"),
 ]},
{"n":"Animalic & resin material","a":"animalics · resins · balsams · gums","d":"Animal-derived fixatives (or their substitutes) and plant resins and balsams that give perfume depth and longevity.",
 "t":["raw material","tincture","absolute or resinoid","synthetic reconstitution","legal status varies by country"],"tg":[],"s":W+"Ambergris",
 "x":[
  X("Ambergris","Waxy sperm-whale secretion that ages into a sweet, earthy fixative; trade banned in the US, Australia and India.","","",W+"Ambergris",
    [("Pale fresh ambergris","","","fresh, faecal-marine"),("Aged grey to black ambergris","","","hardened over months to years")],"colour and age · origin · legality","grey amber · ambra grisea"),
  X("Deer musk","Gland secretion of the endangered musk deer; replaced by synthetic muscone.","","",W+"Muscone",[],"natural vs synthetic substitute","musk"),
  X("Civet","Musky secretion of the African civet; its odorant civetone is now made from palm-oil precursors.","","",W+"Civetone",[("Civetone (synthetic)","","","")],"natural vs synthetic substitute","civet oil"),
  X("Castoreum","Exudate from beaver castor sacs, used as an animalic note.","","",W+"Castoreum",[],"tincture vs absolute · substitute"),
  X("Hyraceum","Petrified excrement of the rock hyrax, used as an animalic perfume material.","","",W+"Hyraceum",[],"tincture strength · origin"),
  X("Labdanum","Sticky rockrose resin; the main material of the amber accord and a chypre component.","","",W+"Labdanum",
    [("Raw resin","","","boiled from leaves and twigs"),("Labdanum absolute","","","solvent extracted"),("Cistus essential oil","","","steam distilled")],"species (Cistus ladanifer, C. creticus) · form","ladanum · ladan"),
  X("Frankincense","Aromatic Boswellia resin used in incense and perfume.","","",W+"Frankincense",
    [("Boswellia sacra","","",""),("Boswellia frereana","","",""),("Boswellia serrata","","",""),("Boswellia papyrifera","","","")],"species · grade · resin, oil or CO2","olibanum"),
  X("Myrrh","Gum-resin of Commiphora trees, an ancient perfume and incense material.","","",W+"Myrrh",[],"form · origin"),
  X("Benzoin","Vanilla-like balsamic resin from Styrax trees.","","",W+"Benzoin_resin",[],"origin · resinoid strength","gum benzoin · benjamin"),
  X("Balsam of Peru","Sweet balsam from Myroxylon balsamum var. pereirae.","","",W+"Balsam_of_Peru",[],"form · allergen restriction","Peru balsam"),
 ]},
{"n":"Perfumer's alcohol & carrier oil","a":"perfume base · diluent · solvent · carrier","d":"Neutral liquid used to dilute perfume concentrate: ethanol for sprays, oils for roll-ons and attars.",
 "t":["perfumer's alcohol (denatured ethanol)","rectified spirit / ethanol-water","dipropylene glycol (DPG)","jojoba oil","fractionated coconut oil","almond oil"],"s":W+"Perfume"},
]
B=[
 {"n":"IFF","c":"United States","f":"1958","seg":"Fragrance & flavour house","d":"International Flavors & Fragrances, New York, formed by merging Polak & Schwarz and van Ameringen-Haebler.","lines":[],"eras":[],"sig":["Iso E Super","Galaxolide","Cashmeran"],"sc":[],"rel":["Givaudan","Firmenich"],"s":W+"International_Flavors_%26_Fragrances"},
 {"n":"Givaudan","c":"Switzerland","f":"1895","seg":"Fragrance & flavour house","d":"Swiss fragrance and flavour maker founded in Zurich by Léon and Xavier Givaudan; based in Vernier, Geneva.","lines":[],"eras":[],"sig":["Ambroxide"],"sc":[],"rel":["IFF","Firmenich"],"s":W+"Givaudan"},
 {"n":"Firmenich","c":"Switzerland","f":"1895","seg":"Fragrance & flavour house","d":"Geneva fragrance house founded as Chuit & Naef; merged with DSM in 2023 to form dsm-firmenich.","lines":[],"eras":[],"sig":["Hedione","Ambroxide"],"sc":[],"rel":["Givaudan","IFF"],"s":W+"Firmenich"},
 {"n":"Pell Wall","c":"United Kingdom","f":"2012","seg":"Perfumery-materials supplier","d":"UK supplier founded by perfumer Chris Bartlett that sold aroma chemicals to hobbyists; entered liquidation in 2026.","lines":[],"eras":["Chris Bartlett, founder"],"sig":[],"sc":[],"rel":["The Perfumer's Apprentice"],"s":"https://thefragrancefoundry.com/blogs/comparisons/uk-perfumery-suppliers-compared"},
 {"n":"The Perfumer's Apprentice","c":"United States","f":"","seg":"Perfumery-materials supplier","d":"Santa Cruz-area supplier of fragrance ingredients that runs perfume-creation workshops; sister company The Flavor Apprentice.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Pell Wall"],"s":"https://www.santacruz.org/listings/the-perfumers-apprentice/"},
]
notes=("New shelf (no old data). Archetypes are named key materials; versions only where the source page gives them (origins, trade names, landmark perfumes). "
 "Rose otto/absolute kept as raw materials; the attar-style rose oil and Taif rose live on the Attar shelf (cross-link). Grasse tradition already on another shelf, so no traditions here. "
 "Left out: jasmine, ylang-ylang and tuberose absolutes and orris irone details (no page retrieved in time; wiki API rate-limited); Lilial (banned for fertility harm, not a current hobby material); "
 "Sclareol (ambroxide precursor, rarely owned); synthetic-musk class beyond Galaxolide/Muscone; Kao and Pfizer brand entries (not fragrance-house pages); Pell Wall kit names and Perfumer's Apprentice founding year (snippet-only). "
 "Hedione year 1962 = end of Demole's 1957–62 synthesis work.")
out={"kinds":kinds,"brands":B,"traditions":[],"notes":notes}
p='work/H4/shelves/03_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
