import sys, json, time
sys.path.insert(0, 'tools')
import run
for q in sys.argv[1:]:
    r = json.loads(run.handle_client_tool('J8', '05_00', 'wiki', {'search': q}))
    s = r.get('search')
    print('Q', q, '->', [x.get('title') if isinstance(x, dict) else x for x in s] if isinstance(s, list) else s)
    time.sleep(0.2)
