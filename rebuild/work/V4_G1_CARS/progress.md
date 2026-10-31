started; no steps done
step1 done: probes; VW Group + Toyota lists fetched (in context, not saved)
step2: data1.py (VW Group, Toyota group, Honda, Mazda) written
step3: switched to Wikipedia category API listing (https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:<X>_vehicles&cmlimit=500&cmtype=page|subcat&format=json&formatversion=2). Done: Nissan. Wikidata done: VW Group, Toyota, Honda, Mazda
step4: Subaru, Mitsubishi, Suzuki done (category)
step5: Ford, Chevrolet, Cadillac, Buick done (category). Todo: Ford subcats (Europe, Australia), GMC, Jeep, Lincoln, Mercury, Tesla, Dodge/Chrysler use Wikidata
step6: Ford Europe, Lincoln, Jeep done. Tesla category name 'Tesla,_Inc._vehicles' empty -> try Tesla_vehicles
COORDINATOR NOTE: drop kind 'Pickup truck' (renames {'Pickup truck':'Utility pickup'}); do not hold any pickups (codes I and J) in the part; list pickups held (old Pickup truck x entries + I/J items) in report for COMMERCIAL check. Pickups that are also SUVs (Ridgeline) stay with COMMERCIAL.
step7: BMW, Mercedes-Benz, Tesla, Renault done
step8: Peugeot (Type N early cars omitted), Citroën, Fiat, Opel
step9: Kia, Volvo, Jaguar done; Hyundai category name TBD (try Hyundai_vehicles)
step10: Hyundai, Land Rover, Lotus done. Ferrari category name TBD
step11: Ferrari, Maserati, MG, Rolls-Royce done
step12: Rolls-Royce Motor Cars, Alfa Romeo done. Mini/BYD categories empty.
step13: Mini, Dacia, BYD, Geely, Mahindra done (Tata/ Mini cat empty or thin). All data in data1.py. NEXT: market-share fetch (1 search+1 fetch), then assemble.py
step14: added Aston Martin, Alpine, AC, Abarth, Acura, Infiniti, Datsun, Dodge, Chrysler, AMC, etc. Market: Europe 2024 (best-selling-cars.com), Japan 2024 registrations, China 65% Chinese brands 2024 (best-selling-cars.com china page). NEXT: assemble.py
