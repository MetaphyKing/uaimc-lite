# HOLES_PROGRESS.md — Scout, Director UNHOLD

Seat: Scout. 2026-09-03 13:29 PT / 20:29 UTC.
host=A_A_9 (machineId 53c3cd96-48c9-4895-8ed0-dfc488b4ebc9, connected). Read-only.
Did not invent A1 cap integer. Did not invent live payload schemas. No live :8767 HTTP. No `.env`. Nothing copied off AA9 except facts quoted here. CopyToBox of D: was refused (outside local-exec root); Shell Get-Content / dir worked.

## Closed this pass

| item | result | evidence |
|---|---|---|
| AGENT_HANDOFF.md independent cite | CLOSED at path-level | File exists `D:\dev\P-CANS\P-CANS\AGENT_HANDOFF.md`, 16065 B, version 0.1.0-dev, 2026-08-07. Quoted into SPEC_PACK Appendix A. |
| Nested uaimc-lite location | CLOSED as two name-lists | Two dirs under NEUROLUX, identical 16 top names. SPEC_PACK Appendix B. |

## Still HOLE (Spec must not invent)

| hole | status | why still open |
|---|---|---|
| 1. A1 cap integer | STILL HOLE | No per-ingest-item fan-out histogram or healthy percentile. This pass did not query the live DB. |
| 2. Mouth-reject / truncate wire | STILL HOLE | Handoff has ingest response `{summary_id, status, annotations_count}` and `status=held` for circuit-open. That is not a mouth-truncate count+class signal. |
| 3. Live Tier A payload schemas | STILL HOLE, partial cite | P-CANS documents ingest **request** JSON and ingest **response** fields, plus GET /context query string. No live GET /health, /query, /recent body. No HTTP this pass. `/context` stays OUT of A. `PCANS_TIMEOUT` default 15s ≠ Vesper 30s/60s wait-never-restart. |
| 4. Sampler vs LOCKED A | STILL HOLE | Nested lite is a service-tree copy (`uaimc_service.py` present), not `C:\dev\uaimc-sampler`. Sampler still polls /ready and /stats. This listing does not place those routes. |

## Related, still open if Spec names them

- kg_nodes in or out of first extraction
- dbstat UNMEASURED
- Byte-identity of the two NEUROLUX uaimc-lite trees UNMEASURED (same names, not unified)
- Stay vs UGDMC queued
- PID 4388 launch identity still INFERENCE

## Nested uaimc-lite names (FACT)

Paths:

- `D:\BEACON_HQ\PROJECTS\00_ACTIVE\NEUROLUX\metaphysics-and-computing\uaimc-lite`
- `D:\BEACON_HQ\PROJECTS\00_ACTIVE\NEUROLUX\Neurolux\uaimc-lite`

Both top: config, config.railway.json, Dockerfile.railway, guardian_prompts.py, guardian_tools.py, ppr_engine.py, railway.toml, requirements.railway.txt, start.railway.sh, tools, uaimc_ambient.py, uaimc_anno.py, uaimc_gpu.py, uaimc_service.py, uaimc_tools.py, uaimc_watcher.py.

Railway filenames listed, not opened, not deployed. Content stays local.

## P-CANS path-level (FACT, not a live probe)

Bridge not replacement. Port 8767. Write POST /ingest. Read GET /query, GET /recent, GET /health. GET /context?mode=cans is P-CANS's live read path and remains gated in LOCKED ①. Duplicate sentinel `summary_id == -2`. High-signal only, never dump chat logs. FastMCP `_tool` suffix PARTIAL. Pending queue in-memory. Dashboard DEMO.

## Coverage, gaps, through-line

**Coverage.** Handoff body read on AA9. Two nested lite trees named. SPEC_PACK appendices A and B. Four original Spec blockers re-checked.

**Gaps.** A1 integer, A2 wire, live HTTP schemas, sampler placement. CopyToBox of D: blocked; quotes are from Shell, not a local file copy.

**Through-line.** The nested "uaimc-lite" under NEUROLUX is a full-looking service copy with Railway files, not the lite extraction this Bible is specifying. P-CANS is still the :8767 bridge. Neither finding invents a cap or a payload.

HOLD for Spec. Scout idle unless a Hunt ask names the next hole.
