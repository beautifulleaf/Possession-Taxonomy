import sys, json, time
sys.path.insert(0, 'tools')
import run
for q in sys.argv[1:]:
    r = json.loads(run.handle_client_tool('J3', '03_07', 'wiki', {'search': q}))
    print('##', q, [x.get('title') for x in r.get('search',[])] if isinstance(r.get('search'),list) else r.get('search'))
    time.sleep(1)
