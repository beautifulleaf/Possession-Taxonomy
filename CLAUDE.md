# Possession taxonomy – working rules for Claude Code
- Current instructions: STATUS.md ("Next (session N)") and the highest-numbered SESSION_*_PROMPT.md if one exists.
- Owner decisions live in BRIEF.md. Never change one; ask via the OWNER QUEUE in STATUS.md.
- This is a fresh domain. Do not read or reuse the old Possessions taxonomy or the Possessions references inside the Pleasure taxonomy artifact.
- Web pages only through WebSearch/WebFetch or the authenticated Parallel MCP tools (mcp__Parallel_Auth__web_search / web_fetch, allow_live_fetch on); never curl/wget/python fetching, archives or caches; never guess URLs. Search excerpts may locate items; an attestation source must be a fetched page.
- Data lives in data/*.tsv; change it only through scripts in tools/ (backup to bak/, write via temp files). Pages and reports are generated, never hand-edited.
- Subagents: Sonnet for harvesting, probes, sourcing and blind placers; Opus for cold auditors and verifiers. Agents never run git. Every agent prompt is written to verify/in/<BATCH>.prompt.txt and carries a RESUME RULE; helper files only in verify/work/<BATCH>/.
- Commit after every phase.
