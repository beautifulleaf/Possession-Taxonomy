step1 done: fetched List_of_pickup_trucks both windows (rows in context only; need to encode into data_pickups.py)
step2 done: fetched List_of_vans (full, ends at VW Type 2; page is dated; minivans out of scope)
step3 done: fetched Horse-drawn_vehicle, List_of_recreational_vehicle_manufacturers, List_of_Bombardier_recreational_and_snow_vehicles (data in context only)
step4 done: fetched Polaris_Inc., Arctic_Cat, Club_Car, Thor_Industries (context only)
step5 done: fetched Hymer, Winnebago_Industries, Airstream; Swift_Group and Knaus_Tabbert urls 404
step6 done: fetched VW_Transporter, Mercedes-Benz_Sprinter(first window; gens known). Search located Swift_Leisure wiki + knaustabbert.de press page
step7 done: fetched Swift_Leisure, knaustabbert press page, Ski-Doo (little), Yamaha_Motor_Company (nothing). ~22 fetches used
step8 done: fetched Utility_terrain_vehicle, All-terrain_vehicle, List_of_trucks (first window; trade trucks out of scope), Bedford_OB. ~29 fetches
step9 done: wrote raw_pickups.txt (rows C=current, D=discontinued; concepts omitted)
step10 done: wrote raw_vans.txt (minivans excluded)
step11 done: fetched Recreational_vehicle, Snowmobile, Pickup_truck, Golf_cart (market facts). ~31 fetches. Next: write build.py
step12 done: build.py runs -> out/G1_parts/COMMERCIAL.json; next validate + review + report
step13 done: validated OK; remaining: report + final reply
step14 start: coordinator round 2 (trucks offset 100000+, ATV 100000+, owners from pages, Yamaha/Kawasaki/Suzuki ATV, Chieftain, market shares)
step14a done: List_of_trucks fully read (0-269154; windows 100k,200k fetched; rows in context, need raw_trucks.txt); ATV article 100000+ has nothing (fully read). next: owners fetches
