exec(open('rebuild/work/GAP_D2/edit2.py').read().split("# OnePlus")[0])
fix_years('Tablet','Galaxy Tab S',{'Galaxy Tab S2':'2015','Galaxy Tab S3':'2017','Galaxy Tab S4':'2018','Galaxy Tab S5e':'2019','Galaxy Tab S6':'2019','Galaxy Tab S7':'2020','Galaxy Tab S8':'2022','Galaxy Tab S9':'2023','Galaxy Tab S10':'2024','Galaxy Tab S11':'2025','Galaxy Tab S12':'2026'})
ent('Tablet','Galaxy Tab S')['s']=W+'Samsung_Galaxy_Tab_S_series'
fix_years('Tablet','Galaxy Tab A',{'Galaxy Tab A 8.0':'2015','Galaxy Tab A 9.7':'2015','Galaxy Tab A 10.1':'2016','Galaxy Tab A 10.5':'2018','Galaxy Tab A6':'2016','Galaxy Tab A7':'2020','Galaxy Tab A8':'2022','Galaxy Tab A9 / A9+':'2023','Galaxy Tab A11 / A11+':'2025'})
ent('Tablet','Galaxy Tab A')['s']=W+'List_of_Samsung_tablets'
e=ent('Tablet','Galaxy Tab A')
if not e.get('y'): e['y']='2015'
fix_years('Smartwatch','Galaxy Watch',{'Galaxy Watch Active':'2019','Galaxy Watch Active 2':'2019','Galaxy Watch 3':'2020','Galaxy Watch 4':'2021','Galaxy Watch 5':'2022','Galaxy Watch 6':'2023','Galaxy Watch 7':'2024','Galaxy Watch Ultra':'2024','Galaxy Watch8':'2025','Galaxy Watch 9':'2026','Galaxy Watch FE':'2024','Galaxy Watch Ultra 2':'2026'})
ent('Smartwatch','Galaxy Watch')['s']=W+'Samsung_Galaxy_Watch_series'
json.dump(d,open('rebuild/work/GAP_D2/D2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('rebuild/work/GAP_D2/D2.tmp','rebuild/out/D2.json')
print(len(log))
