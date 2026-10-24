# H2 Health, Medical & Mobility: decided tree

Category: H2 Health, Medical & Mobility (domain H, Body). Membership test (CATEGORIES_v0_7, step 2): made to diagnose, treat, monitor or compensate for an illness, injury or disability of a person, or for pregnancy, fertility or breastfeeding, or for first aid: medical devices and monitors, medicines (prescription or not, H-2) and medical supplies, vitamins and dietary supplements, sports-nutrition and meal-replacement products in every form, mobility and assistive aids (including ones installed in a home, such as a stairlift or grab bar), hearing aids, spectacles that correct vision with their frames and lenses, contact lenses of every kind, white canes, contraceptives, pregnancy tests and fertility monitors, breast pumps, incontinence products, medical braces and supports, prostheses, medical alert bracelets and tags, worn fall and care alarms, beds, mattresses and chairs made to treat a condition, medical software, and first-aid kits for any place or vehicle. Structure (H-9): level 1 is set by two ordered tests. Test 1 files a medicine, a supplement, or a sports, meal or medical nutrition product by what it is (H2.6, H2.7, H2.8). Test 2 files every other device, aid or supply by the health function it serves (H2.1 to H2.5, H2.9 to H2.11). H2.12 holds parts, attachments and consumables made for one kind of device and is exempt from the level-1 axis (C5(d), CV-17). Below the sub-family comes a leaf on the axis stated for that sub-family (condition is a leaf axis only in H2.6), then the kind, at the level where buyers compare quality or makers; named forms (maker models, lens families, brand medicine products) sit below the kind and are not listed here. Attributes and never kinds: size, user (the one domain-wide list: women, men, unisex, couples, baby, child, bariatric, adapted), `max_user_weight_kg` (bariatric and heavy-duty are a user tag plus this attribute, never kinds), strength, dose form, format (tablet, capsule, gummy, liquid, powder, spray), `active_ingredients` (with ATC code and strength), `tradition` (homeopathic, anthroposophic, kampo, TCM, ayurvedic), power source, measuring mode, lens design, material and coating, replacement schedule, correction type, `corrective`, `shell_style`, load rating, `wheel_count`, forearm supports, installed or free-standing, `optic_type`, `function_served`, and `standard_met` (first-aid kit standards and classes, the BIHS blood-pressure validation list, supplement seals such as USP Verified, NSF and Informed Sport). Legal and supply classes (Rx, OTC, POM, P, GSL, Japanese drug classes, device risk class, UK scooter class) are C17 ledger rows and never move an object. A kind marked † is provisional, named only by the framework key, a decision or a review, and needs a fetched page before it enters the data. Maker role: owner (provisional): devices and products are chosen by need and fit, and makers are reached through their products; brand products are named forms and own-label ranges are lines (H-8). Display groups (navigation proposal, display only; the tree keeps the memo's sub-families): Medicines (H2.6); Vitamins and supplements (H2.7); Sports and meal nutrition (H2.8); Monitors and tests (H2.1); Therapy devices (H2.2); Mobility aids (H2.3); Daily living and care (H2.4); Hearing and vision (H2.5); Contraception, sexual health and breastfeeding (H2.9, with H2.2.4 and H2.6.5.1 as a linked view); First aid and wound care (H2.10); Supports, braces and prostheses (H2.11); Parts, refills and consumables (H2.12). Quality markers (display only, ranked as the navigation proposal gives them): monitors by independent validation (BIHS list), then cuff type and fit; mobility aids by fit to the user, then user weight capacity, width, place of use, wheel size, portability, brakes and warranty; supplements by ingredients and form, then third-party testing seal, certificate of analysis, labelling and company reputation; sports nutrition by ingredient type, then batch testing for banned substances; medicines by active ingredient and strength, then sale class; hearing aids by style for the hearing loss, then lab-measured performance.

Ids (R-58): H2.n is a sub-family and H2.n.m a leaf; a kind is H2.n.m.kk, or H2.n.kk where a sub-family has no leaf.

H2's builder ids are adopted as built (R-58; memo section 13, frozen tree audit/KL_H2_tree.md): kind numbers are written without a leading zero (H2.1.1.1, H2.5.2.10) and are kept exactly. Every H2 sub-family has leaves. Retired ids stay listed and are never reused.

## H2.1 Monitoring and testing devices

Leaf axis: quantity measured or condition tested. Every test and monitor is here, whatever condition it serves.

### H2.1.1 Blood pressure
- H2.1.1.1 upper-arm blood-pressure monitor: home device whose cuff wraps the upper arm and which reads blood pressure and pulse.
- H2.1.1.2 wrist blood-pressure monitor: home device worn on the wrist for a blood-pressure reading.
- H2.1.1.3 wearable blood-pressure monitor: watch-style or band-style device that measures blood pressure while worn.

### H2.1.2 Body temperature
- H2.1.2.1 electronic stick thermometer: electronic probe thermometer read orally, rectally or under the arm.
- H2.1.2.2 ear thermometer: infrared thermometer that reads the eardrum. †
- H2.1.2.3 forehead thermometer: infrared thermometer that reads the temple or forehead. †

### H2.1.3 Blood glucose
- H2.1.3.1 blood glucose meter: handheld meter that reads a drop of blood on a test strip (fingerstick).
- H2.1.3.2 continuous glucose monitor: worn sensor that measures glucose under the skin and sends readings on its own at short intervals.
- H2.1.3.3 flash glucose monitor: worn sensor whose readings are fetched by scanning it with a reader or phone.

### H2.1.4 Oxygen saturation
- H2.1.4.1 pulse oximeter: clip or band device that reads blood oxygen saturation and pulse.

### H2.1.5 Heart rhythm
- H2.1.5.1 personal ECG monitor: handheld or worn device that records an electrocardiogram.

### H2.1.6 Infection tests
- H2.1.6.1 at-home infection test kit: self-test kit for an infection (for example COVID-19 or flu; a combined test is this one kind).

### H2.1.7 Fertility and pregnancy
- H2.1.7.1 pregnancy test: one-use urine test that shows whether the user is pregnant.
- H2.1.7.2 ovulation test: one-use urine test that finds the hormone surge before ovulation.
- H2.1.7.3 fertility monitor: reusable reader with test sticks or sensors that tracks the fertile window. †
- H2.1.7.4 basal-body thermometer: sensitive thermometer made to track resting body temperature for fertility.

### H2.1.8 Software
- H2.1.8.1 medical app: software that itself diagnoses, treats or is cleared as a medical device; an app that only records and shows readings from a separate device is not this kind. †

## H2.2 Therapy devices

Leaf axis: therapy delivered.

### H2.2.1 Respiratory
- H2.2.1.1 nebuliser: device that turns liquid medicine into a mist to be breathed in.

### H2.2.2 Electrotherapy and pain
- H2.2.2.1 TENS unit: pulse generator with skin pads, sold to relieve pain by nerve stimulation.
- H2.2.2.2 EMS unit sold for pain: muscle-stimulation unit with skin pads, sold to relieve pain. †

### H2.2.3 Weighted and orthopaedic therapy aids
- H2.2.3.1 weighted blanket: blanket loaded with weight, made to treat a stated condition. †
- H2.2.3.2 orthopaedic pillow: shaped pillow made to treat a stated condition (a therapeutic weighted pillow is this kind with a `weight` value). †

### H2.2.4 Pelvic-floor and sexual function
- H2.2.4.1 pelvic-floor trainer: device that trains the pelvic-floor muscles, sold with a stated medical purpose. †
- H2.2.4.2 vacuum erection device: vacuum cylinder and pump used to obtain an erection, sold with a stated medical purpose. †
- H2.2.4.3 ED ring: ring worn at the base of the penis to keep an erection, sold with a stated medical purpose. †
- H2.2.4.4 vaginal dilator: graduated dilator used to widen or restore vaginal capacity (provisional as a sold kind, H-14). †

## H2.3 Mobility and transfer aids

Leaf axis: how the body is supported or moved.

### H2.3.1 Walking aids
Ordered by support given, least to most.
- H2.3.1.1 walking stick: single hand-held stick or cane.
- H2.3.1.2 forearm crutch: crutch with a forearm cuff and a handgrip.
- H2.3.1.3 underarm crutch: crutch that rests under the armpit.
- H2.3.1.4 walking frame: frame without wheels, or with two front wheels, that the user lifts or pushes (`wheel_count` 0 or 2).
- H2.3.1.5 tri-walker: retired, merged into H2.3.1.6 rollator (memo section 14); kept as status retired, never reused, and not a placement target.
- H2.3.1.6 rollator: walking support on three or four wheels with hand brakes; four-wheeled models usually have a seat and bag (`wheel_count` 3 or 4; Deltarad, delta walker, tri-walker and 3-wheel rollator are aliases of the three-wheel form).
- H2.3.1.7 knee walker: wheeled frame with a knee rest, used in place of crutches for a lower-leg injury.

### H2.3.2 Wheeled seating
- H2.3.2.1 manual wheelchair: wheelchair propelled by the user or a pusher.
- H2.3.2.2 powered wheelchair: wheelchair driven by an electric motor.
- H2.3.2.3 mobility scooter: electric seated vehicle with tiller steering made for a person with limited mobility.

### H2.3.3 Transfer and access
- H2.3.3.1 portable ramp: ramp for a wheelchair or scooter over steps or kerbs.
- H2.3.3.2 patient lift: hoist or lift that raises and moves a person.
- H2.3.3.3 stairlift: chair or platform that carries a person up and down a staircase (installed or free-standing is an attribute). †

## H2.4 Daily-living and care aids

Leaf axis: daily task or care need.

### H2.4.1 Bathing
- H2.4.1.1 shower chair: chair, stool or bench for sitting while washing.
- H2.4.1.2 grab bar: rail fixed or clamped to give a hand-hold, for example by a bath or toilet (UK grab rail).

### H2.4.2 Toileting, continence and stoma care
- H2.4.2.1 commode chair: chair with a seat opening and a removable pail, used as a toilet, also when it is made to be used in a shower.
- H2.4.2.2 raised toilet seat: seat that raises the height of a toilet.
- H2.4.2.3 incontinence product: absorbent pad, brief or similar made for urinary or bowel leakage.
- H2.4.2.4 stoma appliance: bag, flange or similar supply for a stoma.

### H2.4.3 Bed and pressure care
- H2.4.3.1 care bed: adjustable bed for nursing care (a hospital bed is this kind).
- H2.4.3.2 pressure-relief mattress: mattress made to prevent or treat pressure sores.
- H2.4.3.3 pressure-relief cushion: seat cushion made to prevent or treat pressure sores, including cushions used in wheelchairs.

### H2.4.4 Examination and treatment furniture
- H2.4.4.1 examination table: table for a clinical examination. †
- H2.4.4.2 treatment couch: couch for therapy or treatment. †
- H2.4.4.3 dental chair: chair for dental treatment. †

### H2.4.5 Alerting and identification
- H2.4.5.1 medical ID bracelet: wrist band carrying medical information.
- H2.4.5.2 medical ID tag: tag, card or keyring carrying medical information.
- H2.4.5.3 fall detector: worn device made mainly to sense a fall and call for help. †
- H2.4.5.4 care pendant: worn call button that summons help after a fall or medical event; automatic fall sensing on it is an attribute. †
- H2.4.5.5 wandering detector: device that alerts carers when a person leaves a place.

## H2.5 Sensory and communication aids

Leaf axis: sense or channel compensated.

### H2.5.1 Hearing
Ordered behind-the-ear to canal.
- H2.5.1.1 BTE hearing aid: case behind the ear with a tube to an ear mould.
- H2.5.1.2 RIC hearing aid: case behind the ear with a thin wire to a receiver in the ear canal.
- H2.5.1.3 ITE hearing aid: custom shell filling the outer ear.
- H2.5.1.4 canal hearing aid: custom device sitting in or deep in the ear canal (ITC, CIC and IIC are `shell_style` values).

### H2.5.2 Vision
Ordered worn, then held, then on the eye, then the cane.
- H2.5.2.1 prescription spectacles: glasses with lenses made to the wearer's prescription. †
- H2.5.2.2 ready-made reading glasses: glasses with fixed magnifying power, sold without a prescription. †
- H2.5.2.3 prescription sunglasses: tinted spectacles with lenses made to a prescription. †
- H2.5.2.4 low-vision spectacles: spectacles with magnifying, prismatic or telescopic lenses in a spectacle frame, including flip-down magnifiers mounted on a frame. †
- H2.5.2.5 handheld magnifier: magnifier held in the hand, made and sold as a low-vision aid.
- H2.5.2.6 stand magnifier: magnifier on a stand or flat base resting on the page, made and sold as a low-vision aid.
- H2.5.2.7 soft contact lens: flexible lens worn on the eye, of any schedule, correction or colour; a coloured lens without power is this kind with `corrective: no`.
- H2.5.2.8 rigid gas-permeable contact lens: rigid lens worn on the eye. †
- H2.5.2.9 orthokeratology lens: rigid lens worn overnight to reshape the cornea. †
- H2.5.2.10 scleral lens: large rigid lens resting on the white of the eye. †
- H2.5.2.11 white cane: cane made for a blind or low-vision person to detect obstacles. †

### H2.5.3 Speech and communication
- H2.5.3.1 communication aid: device or board that helps a person speak or communicate.

## H2.6 Medicines

Leaf axis: symptom or condition group (the one place in H2 where condition is the leaf axis). All medicines are here, prescription or not; the kind is the labelled use class, and a product labelled for two uses is filed by the use printed first on the pack. A traditional or homeopathic product labelled for a use goes to that use class with `tradition` as an attribute; leaf 0 holds only products with no labelled use.

### H2.6.1 Allergy and sinus
- H2.6.1.1 oral antihistamine: tablet, capsule or liquid taken for allergy symptoms.
- H2.6.1.2 allergy nasal spray: spray used in the nose for allergy symptoms.

### H2.6.2 Cough, cold and flu
- H2.6.2.1 cough suppressant: medicine that suppresses cough.
- H2.6.2.2 expectorant: medicine that loosens phlegm.
- H2.6.2.3 nasal decongestant: medicine that clears a blocked nose.
- H2.6.2.4 cold and flu remedy: combined medicine for cold and flu symptoms.

### H2.6.3 Pain and inflammation
- H2.6.3.1 oral analgesic: tablet, capsule or liquid taken for pain or fever. †
- H2.6.3.2 topical pain-relief gel: gel or cream rubbed on for joint or muscle pain.
- H2.6.3.3 lidocaine patch: adhesive patch with a local anaesthetic.
- H2.6.3.4 migraine medicine: medicine labelled for migraine.

### H2.6.4 Sleep
- H2.6.4.1 sleep aid: medicine labelled first as an aid to fall asleep (the same ingredient labelled first for allergy is an oral antihistamine). †

### H2.6.5 Sexual and reproductive health
- H2.6.5.1 delay spray: topical anaesthetic spray to delay ejaculation. †
- H2.6.5.2 emergency contraceptive pill: pill taken after unprotected sex to prevent pregnancy. †

### H2.6.6 Mouth and teeth
- H2.6.6.1 teething gel: gel applied to the gums of a teething baby. †

### H2.6.7 Digestive
- H2.6.7.1 medicinal enema: enema containing a medicine (a plain enema bulb or anal douche is not a medicine). †

### H2.6.8 Smoking cessation
- H2.6.8.1 nicotine replacement product: patch, gum, lozenge, spray or inhaler that supplies nicotine to help stop smoking. †

### H2.6.0 No labelled use (sub-family-wide slot)
- H2.6.0.1 homeopathic single remedy (no labelled use): registered single homeopathic remedy sold with no indication; provisional, issued only if a fetched pharmacy page sells such remedies as their own category (memo section 14). †

## H2.7 Supplements

Leaf axis: ingredient class. A single-ingredient product is the kind named by its ingredient; a product that mixes ingredient classes is a multi-ingredient supplement. Supplements sold for skin, hair or nails, collagen drinks included, are here. Kinds are seeded from the NIH fact-sheet list and enter on one fetched page each, uncapped (H-3).

### H2.7.1 Vitamins
- H2.7.1.1 multivitamin: supplement that combines many vitamins in one product.
- H2.7.1.2 vitamin D supplement: supplement whose single active ingredient is vitamin D.
- H2.7.1.3 vitamin C supplement: supplement whose single active ingredient is vitamin C.

### H2.7.2 Minerals
- H2.7.2.1 magnesium supplement: supplement whose single active ingredient is magnesium.

### H2.7.3 Botanicals
- H2.7.3.1 ashwagandha supplement: supplement made from ashwagandha root or extract.

### H2.7.4 Other single ingredients
- H2.7.4.1 probiotic: live-microbe supplement.
- H2.7.4.2 fish oil: omega-3 oil supplement from fish.
- H2.7.4.3 collagen supplement: collagen in powder, drink or capsule, including those sold for skin, hair and nails. †
- H2.7.4.4 restorative essence: tonic or essence sold for health (for example essence of chicken). †

### H2.7.5 Blends
- H2.7.5.1 multi-ingredient supplement: product mixing ingredient classes (for example a joint formula, or a hair, skin and nails formula). †

## H2.8 Sports, meal and medical nutrition

Leaf axis: role in training or meals. Sports and meal-replacement products are here in every form (powders, bars, gels, ready-to-drink shakes, tablets).

### H2.8.1 Protein
- H2.8.1.1 protein powder: powder sold for its protein, for training or recovery.
- H2.8.1.2 protein bar: bar sold for its protein.

### H2.8.2 Performance
- H2.8.2.1 creatine: creatine sold as a training supplement.
- H2.8.2.2 pre-workout: powder or drink taken before training.
- H2.8.2.3 amino-acid supplement: amino acids (for example BCAA, arginine, glutamine) sold for training.

### H2.8.3 Hydration and energy
- H2.8.3.1 electrolyte or energy gel: gel, tablet or drink mix for hydration or energy during exercise.

### H2.8.4 Meal replacement
- H2.8.4.1 meal-replacement shake: shake or powder sold to replace a meal. †

### H2.8.5 Medical nutrition
- H2.8.5.1 medical-condition formula: formula made for a medical condition (hypoallergenic, amino-acid or metabolic formulas); a food, not a supplement. †

## H2.9 Contraception, barriers and breastfeeding

Leaf axis: purpose, to prevent pregnancy or infection, or to feed. Tests are in H2.1 and medicines in H2.6.

### H2.9.1 Contraception and barriers
- H2.9.1.1 condom: sheath worn on the penis or in the vagina as a contraceptive and barrier. †
- H2.9.1.2 dental dam: thin sheet used as an oral barrier. †

### H2.9.2 Breastfeeding
- H2.9.2.1 breast pump: pump that expresses milk (power source and single or double are attributes).
- H2.9.2.2 wearable breast pump: pump worn inside the bra, whose form differs from a corded pump. †
- H2.9.2.3 nursing pad: pad worn in the bra to absorb leaked milk. †
- H2.9.2.4 nipple cream: cream for sore nipples while breastfeeding. †

## H2.10 First aid and wound care

Leaf axis: form of supply.

### H2.10.1 Kits
- H2.10.1.1 first-aid kit [Verbandkasten]: kit sold, standardised and compared as one object, whatever place or vehicle it is made for; the standard and class it meets are `standard_met`.

### H2.10.2 Dressings and bandages
- H2.10.2.1 adhesive bandage: small dressing on an adhesive strip (UK plaster).
- H2.10.2.2 triangular bandage: triangle of cloth used as a sling or to hold a dressing.
- H2.10.2.3 roller bandage: long strip of bandage wound on a roll.

## H2.11 Supports, braces and prostheses

Leaf axis: what the object does to the body part. Body region is part of the kind name.

### H2.11.1 Support
- H2.11.1.1 neck support: collar or brace that supports the neck.
- H2.11.1.2 back support: brace or belt that supports the back.
- H2.11.1.3 elbow support: brace or sleeve that supports the elbow.
- H2.11.1.4 wrist and hand support: brace, splint or sleeve that supports the wrist or hand.
- H2.11.1.5 orthotic insole: insole made to treat or support the foot.
- H2.11.1.6 compression stocking: stocking with graded pressure made for a labelled medical purpose. †

### H2.11.2 Replacement
- H2.11.2.1 leg prosthesis: artificial leg or part of a leg.
- H2.11.2.2 arm prosthesis: artificial arm, hand or part of one.
- H2.11.2.3 breast prosthesis: artificial breast, including breast forms and packers.
- H2.11.2.4 eye prosthesis: artificial eye.
- H2.11.2.5 epithesis: prosthesis replacing a facial or other external part.

## H2.12 Parts and accessories made for one device

Leaf axis: device family served. This sub-family is exempt from the level-1 axis (C5(d)).

### H2.12.1 Monitor parts
- H2.12.1.1 blood-pressure monitor cuff or part: cuff, tube or other part made for a blood-pressure monitor.

### H2.12.2 Glucose-monitor consumables
- H2.12.2.1 glucose test strip: one-use strip read by a blood glucose meter. †
- H2.12.2.2 CGM sensor: replacement sensor for a continuous or flash glucose monitor. †

### H2.12.3 Hearing-aid parts
- H2.12.3.1 hearing-aid battery: battery made to power a hearing aid.
- H2.12.3.2 ear tip: dome or tip fitted to a hearing aid in the ear canal.

### H2.12.4 Wheelchair parts
- H2.12.4.1 wheelchair accessory made for one model: part or accessory made to fit one wheelchair model, including a cushion shaped for it.

### H2.12.5 Spectacle parts
- H2.12.5.1 spectacle frame: frame sold for glazing (a frame with plano or no lenses sold as fashion is not here). †
- H2.12.5.2 spectacle lens: lens sold for glazing. †

### H2.12.6 Contact-lens care
- H2.12.6.1 contact-lens solution: solution for cleaning, storing or rinsing contact lenses. †

## Precedence inside H2

- Every test and monitor is H2.1, whatever condition it serves (H-9): a pregnancy test (H2.1.7.1), an ovulation test (H2.1.7.2), a fertility monitor (H2.1.7.3) and a basal-body or women's thermometer (H2.1.7.4) are H2.1.7, not H2.9. A kitchen or room thermometer is not in H2.
- A product sold and labelled as sports nutrition (protein, creatine, pre-workout, BCAA and other amino acids sold for training, electrolytes, gels, bars) is H2.8; the same ingredient sold as a general supplement (L-lysine for health) is H2.7. A contraceptive or emergency pill is H2.6 (H2.6.5.2, a medicine under test 1); a condom or dental dam is H2.9.1 (H2.9.1.1, H2.9.1.2). A formula made for a medical condition is H2.8.5.1 medical-condition formula, a food and not a supplement (H-11).
- Software that itself diagnoses, treats or is cleared as a medical device is H2.1.8.1 medical app, whatever condition it serves, with the condition as `function_served`; an app that only records and shows a separate device's readings is not this kind (R-14).
- A medicine's kind is its labelled use class; a product labelled for two uses is filed by the use printed first on the pack (a diphenhydramine product labelled first as a sleep aid is H2.6.4.1, one labelled first for allergy is H2.6.1.1). Active ingredients, labelled fixed combinations, strength and dose form are attributes (paracetamol with caffeine is H2.6.3.1). A homeopathic, anthroposophic, kampo, TCM or ayurvedic product labelled for a use goes to that use class with `tradition` set (a homeopathic cold remedy is H2.6.2.4); only a registered single remedy with no labelled use goes to H2.6.0.1 †, and only if that id is issued.
- A nicotine patch, gum or lozenge whose labelled main purpose is to stop smoking is H2.6.8.1.
- A three-wheel walker, Deltarad or delta walker is H2.3.1.6 rollator with `wheel_count` 3; H2.3.1.5 tri-walker is retired and takes no objects. A front-wheeled walking frame is H2.3.1.4 with `wheel_count` 2. A knee walker is H2.3.1.7 although it has wheels. A powered wheelchair (H2.3.2.2) or mobility scooter (H2.3.2.3) is H2.3.2.
- A pressure-relief cushion is H2.4.3.3 wherever it is used; only a cushion shaped for one wheelchair model is H2.12.4.1.
- A bed, mattress or chair made to treat or manage a condition is H2.4.3 (care bed H2.4.3.1, a hospital bed included; pressure-relief mattress H2.4.3.2); examination tables, treatment couches and dental chairs are H2.4.4 (H2.4.4.1 to H2.4.4.3). A lift chair (riser recliner) is an adapted recliner and is not in H2 (B1).
- An assistive object with no ordinary counterpart (a reacher, a sock aid, a shower chair H2.4.1.1, a commode chair H2.4.2.1, a care bed H2.4.3.1) is H2.4; a raised toilet seat (H2.4.2.2) or grab bar (H2.4.1.2) made for a person with a disability is H2.4. A chair with a seat opening and a pail is H2.4.2.1 even when also made for the shower.
- A worn alarm made to call help after a fall or medical event (fall detector H2.4.5.3, care pendant H2.4.5.4, wandering detector H2.4.5.5) is H2.4.5; a device made mainly to sense falls is H2.4.5.3, and a call button with optional fall sensing is H2.4.5.4. A medical ID bracelet or tag is H2.4.5.1 or H2.4.5.2.
- Spectacles that correct vision, ready-made reading glasses and prescription sunglasses are H2.5.2 (H2.5.2.1 to H2.5.2.3); a frame or lens sold for glazing is H2.12.5 (H2.12.5.1, H2.12.5.2). Magnifying, prismatic or telescopic lenses in spectacle frames are H2.5.2.4 low-vision spectacles (R-13). A magnifier made and sold as a low-vision aid is H2.5.2.5 or H2.5.2.6. Contact lenses of every kind are H2.5.2 (H2.5.2.7 to H2.5.2.10), and a coloured or costume lens with no power is H2.5.2.7 (or its rigid kind) with `corrective: no`. Contact-lens solution is H2.12.6.1.
- A hearing aid's shell style (full-shell, half-shell, ITC, CIC, IIC) is an attribute: a CIC model is H2.5.1.4; prescription or OTC never moves a hearing aid.
- Parts, attachments and consumables made for one kind of device follow that device into H2.12 (a blood-pressure cuff H2.12.1.1, a glucose test strip H2.12.2.1, a CGM sensor H2.12.2.2, a hearing-aid battery H2.12.3.1, a spectacle frame H2.12.5.1).
- Teething gel (H2.6.6.1) and a medicinal enema (H2.6.7.1) are H2.6; a delay spray is H2.6.5.1; nursing pads (H2.9.2.3) and nipple cream (H2.9.2.4) are H2.9.2.
- A pelvic-floor trainer, vacuum erection device, ED ring or dilator is H2.2.4 (H2.2.4.1 to H2.2.4.4) when the maker states a medical purpose. A TENS unit or EMS unit sold for pain is H2.2.2 (H2.2.2.1, H2.2.2.2).
- Weighted blankets and orthopaedic pillows made to treat a stated condition are H2.2.3 (H2.2.3.1, H2.2.3.2).
- A compression stocking with a labelled medical purpose is H2.11.1.6; an orthotic insole (H2.11.1.5) and a medical brace or support are H2.11.1. Breast forms and packers are H2.11.2.3 with the breast prosthesis.
- A first-aid kit is H2.10.1.1 whatever vehicle, workplace or place it is made for; its standard and class (DIN 13164 for cars, BS 8599-1, ANSI/ISEA Z308.1) are `standard_met`.
- A breast pump's power source and single or double are attributes of H2.9.2.1; a pump worn inside the bra is H2.9.2.2.
- Supplements sold for skin, hair or nails, collagen drinks included, are H2.7 (H2.7.4.3). A single-ingredient product is the kind named by its ingredient; a product mixing ingredient classes is H2.7.5.1.
- A product is filed by what it is and what it is for, not by the legal class it holds in one country (vitamin C tablets are H2.7.1.3 although Japan classes them as a drug); prescription, OTC, device class and scooter class are C17 rows and never move an object. Bariatric and heavy-duty are a user tag and `max_user_weight_kg`, never a kind. A protein shaker is a drink bottle and is not in H2 (B5); it appears only as a cross-link in the sports-nutrition view.
