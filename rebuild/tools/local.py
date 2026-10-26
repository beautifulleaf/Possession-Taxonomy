"""In-session pipeline (Claude Code subagents instead of the API). Same plans, shelf files, source gate and merge.

  python3 tools/local.py status [CODES]          shelves done / planned, unfinished job ids
  python3 tools/local.py plan-prompt CODE        write work/CODE/prompts/plan.txt (planner writes work/CODE/plan.raw.json)
  python3 tools/local.py fix-plan CODE           check plan.raw.json (every old id once), repair mechanically -> plan.json
  python3 tools/local.py shelf-prompt CODE JOB   write work/CODE/prompts/JOB.txt (worker writes work/CODE/shelves/JOB.json)
  python3 tools/local.py logsrc CODE JOB STATUS URL [URL ...]   STATUS = fetched (page retrieved) | search (snippet only)
  python3 tools/local.py wd CODE JOB search|ids|sparql ARG      Wikidata via the throttled helper (logs entities as api)
  python3 tools/local.py check CODE JOB          source-gated shelf check; prints OK or the errors to fix
  python3 tools/local.py finish CODE             assemble -> validate -> merge (only if every shelf is done)"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import run  # noqa: E402  (chdirs to rebuild/)
from run import W, jdump, old_kinds, shelf_jobs, shelf_context, check_shelf, retrieved_set, log_source, findings_row, cat_name

LOCAL_RULES = run.WORKER_RULES.replace(
    "Tools: web_search and web_fetch (server side; you may call web_fetch for several URLs inside one code block),\n"
    "wiki (Wikipedia search / page extracts, throttled), wikidata (search, entities, SPARQL), submit (final answer).",
    "Tools: WebSearch, WebFetch, Firecrawl (firecrawl_search to locate, firecrawl_scrape with maxAge 0 to retrieve; never the\n"
    "stealth/enhanced proxy modes), and Wikidata via `python3 tools/local.py wd CODE JOB search|ids|sparql ARG`.")


def plan_path(c): return W(c, 'plan.json')


def status(codes):
    for c in codes:
        if not os.path.exists(plan_path(c)):
            print(f'{c}: no plan'); continue
        plan = json.load(open(plan_path(c)))
        jobs = [j for j, _, _ in shelf_jobs(c, plan)]
        todo = [j for j in jobs if not os.path.exists(W(c, 'shelves', j + '.json'))]
        print(f"{c}: {len(jobs) - len(todo)}/{len(jobs)} done{' (merged)' if c in json.load(open('done.json')) else ''}; todo: {' '.join(todo)}")


def plan_prompt(c):
    p, ks = run.plan_params(c)
    txt = (p['system'] + '\n\n---\n' + p['messages'][0]['content'] +
           f"\n\n---\nWRITE the plan JSON (just the object, no fence) to /home/user/Possession-Taxonomy/rebuild/work/{c}/plan.raw.json, then run "
           f"`python3 tools/local.py fix-plan {c}` from /home/user/Possession-Taxonomy/rebuild and fix any missing/duplicate ids it reports. "
           "Never run git. RESUME RULE: if work/{c}/plan.json already exists, stop and report.")
    out = W(c, 'prompts', 'plan.txt'); open(out, 'w').write(txt); print(out, len(txt), 'chars')


def fix_plan(c):
    plan = json.load(open(W(c, 'plan.raw.json')))
    _, ks = old_kinds(c)
    missing, dup, unknown = run.check_plan(plan, ks)
    print(f'missing {missing} dup {dup} unknown {unknown}')
    run.fix_plan(plan, ks)
    jdump(plan, plan_path(c))
    print('plan.json written:', len(plan['depts']), 'depts', sum(len(d['s']) for d in plan['depts']), 'shelves', len(plan.get('moves', [])), 'moves')


def shelf_prompt(c, job):
    plan = json.load(open(plan_path(c)))
    _, ks = old_kinds(c); kb = {k['id']: k for k in ks}
    for j, dp, s in shelf_jobs(c, plan):
        if j != job: continue
        web = s.get('web', True)
        task = (f"\n\n---\nOUTPUT: write the finished shelf as JSON {{\"kinds\": [...], \"brands\": [...], \"traditions\": [...], \"notes\": \"...\"}} to "
                f"/home/user/Possession-Taxonomy/rebuild/work/{c}/shelves/{job}.json (write via a temp file then rename). Work from "
                f"/home/user/Possession-Taxonomy/rebuild. After EVERY page you successfully retrieve (WebFetch, firecrawl_scrape), log it: "
                f"`python3 tools/local.py logsrc {c} {job} fetched <url> [<url> ...]` (log the URL exactly as you will cite it). Only logged "
                f"fetched/api URLs are accepted as sources. Then run `python3 tools/local.py check {c} {job}` and fix every error until it prints OK. "
                f"Every model, maker, year and version must come from the old data or a page you retrieved and logged; never name models from memory. "
                f"Scratch files only in work/{c}/agent/. Never run git. Never invent URLs or facts.\n"
                f"RESUME RULE: if work/{c}/shelves/{job}.json exists and the check prints OK, stop and report; if work/{c}/agent/{job}.notes.md "
                f"exists, continue from it (keep it updated with sources found and decisions as you go).")
        if not web:
            task += ("\nThis is a RESTRAINT-ONLY shelf: keep, merge, rename or drop the old kinds as planned, attribute variants into \"t\", trim "
                     f"models to ≤{run.MAXM[dp['mode']]} market-covering brands plus test winners, plain one-sentence definitions, keep each kind's old \"s\". "
                     "No archetypes, no new kinds, no brand entries, no web research needed.")
        txt = f"{run.SCHEMA}\n\n---\n{run.RULES}\n\n---\n{LOCAL_RULES}\n\n---\n" + shelf_context(c, plan, dp, s, kb) + task
        out = W(c, 'prompts', job + '.txt'); open(out, 'w').write(txt); print(out, len(txt), 'chars'); return
    print('no such job', job)


def check(c, job):
    plan = json.load(open(plan_path(c)))
    _, ks = old_kinds(c); kb = {k['id']: k for k in ks}
    for j, dp, s in shelf_jobs(c, plan):
        if j != job: continue
        p = W(c, 'shelves', job + '.json')
        if not os.path.exists(p): print('no output file', p); return
        try:
            out = json.load(open(p))
        except Exception as e:
            print('invalid JSON:', e); return
        errs, _, _ = check_shelf(c, dp, s, out, kb, retrieved_set(), final=False)
        print('OK' if not errs else 'ERRORS:\n- ' + '\n- '.join(errs[:80]))
        return
    print('no such job', job)


def wd(c, job, mode, arg):
    print(run.handle_client_tool(c, job, 'wikidata', {mode: (arg.split(',') if mode == 'ids' else arg)}))


def finish(c):
    plan = json.load(open(plan_path(c)))
    todo = [j for j, _, _ in shelf_jobs(c, plan) if not os.path.exists(W(c, 'shelves', j + '.json'))]
    if todo: print('not finished:', todo); return
    if run.assemble(c) and run.validate_and_merge(c): print(open(f'out/{c}_report.md').read())


if __name__ == '__main__':
    cmd, a = sys.argv[1], sys.argv[2:]
    if cmd == 'status': status(a or [c['c'] for c in run.META['cats']])
    elif cmd == 'plan-prompt': plan_prompt(a[0])
    elif cmd == 'fix-plan': fix_plan(a[0])
    elif cmd == 'shelf-prompt': shelf_prompt(a[0], a[1])
    elif cmd == 'logsrc':
        for u in a[3:]: log_source(a[0], a[1], u, a[2])
        print('logged', len(a[3:]))
    elif cmd == 'wd': wd(a[0], a[1], a[2], ' '.join(a[3:]))
    elif cmd == 'check': check(a[0], a[1])
    elif cmd == 'finish': finish(a[0])
