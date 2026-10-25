import sys,json;sys.path.insert(0,'tools');sys.argv=['x']
import run
code='B8';plan=json.load(open('work/B8/plan.json'))
_,ks=run.old_kinds(code);kb={k['id']:k for k in ks}
for job,dp,s in run.shelf_jobs(code,plan):
    if s['n'].startswith(sys.argv[0] if False else 'Locksport'): run.run_web_job(code,plan,job,dp,s,kb)
