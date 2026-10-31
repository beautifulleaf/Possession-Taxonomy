import sys, json, time
sys.path.insert(0, 'tools')
import run, netlib
for q in ["Manner wafer Vienna", "Kjeldsens butter cookies", "Pim's biscuit LU", "Viennese whirl biscuit", "Tunnock's caramel wafer", "Party Rings biscuit", "Biscoff"]:
    for i in range(6):
        r = json.loads(run.handle_client_tool('J8','01_00','wiki',{'search':q}))
        if isinstance(r.get('search'), list): break
        time.sleep(30)
    print('Q', q, [ (x.get('title')) for x in (r.get('search') or [])][:6] if isinstance(r.get('search'),list) else r)
    time.sleep(1)
