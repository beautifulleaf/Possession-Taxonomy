step1: marque category existence checked; fetched cats Chery,Haval,Changan,FAW,Hongqi,Roewe,Trumpchi,Aion,BAIC,JAC,Baojun,LiAuto,Zeekr,Leapmotor,Xiaomi,Jetour,Proton,Perodua,VinFast (raw in data1.txt)
step2: fetched Holden,Daewoo,Isuzu,Mitsuoka,Genesis,IKCO,Saipa,Daihatsu,Tata,Lexus; data2.txt written. Great Wall cat name wrong; Tata Motors cat has subcat Category:Tata cars
step3: data3.txt written (Tata,GreatWall,Maruti,Hindustan,Dongfeng,Wuling,Nio(no models),Xpeng,Ora,HSV,SsangYong,Samsung,Naza). Next: covered marques (Toyota..Mahindra) gaps, marque facts, build JSON
step4: marque facts query done; REVISION received (coordinator): unclassified models go to kind 'Car, body style not stated'; prefer List pages w/ years; tier Global group if parent global carmaker else Independent
step5: build.py run -> rebuild/out/G1_parts/cars_add/ASIA.json written and loads; next: report
step6: report written; DONE
ROUND2 started: read list pages (Toyota,Honda,Nissan,Mitsubishi,Subaru,Suzuki,Mazda,Hyundai,Kia,Daihatsu,Isuzu,Holden,Tata,Mahindra,Proton); drop Nissan/Mitsubishi own updates; fill y; rewrite ASIA.json
