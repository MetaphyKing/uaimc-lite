# SPEC_PACK.md — UAIMC-Lite Cycle 0 locked spec card

Seat: Scout. 2026-09-03 ~12:20 PT. One card for Bible + builders.
No product code. No commit. Live :8767 not touched from this computer.
This file supersedes a concurrent Hunt card that mixed Cycle 1 NEXT_PLAN proposed Tier A into ①. LOCKED ① is GET /health, GET /query, GET /recent, POST /ingest. Not GET /ready, GET /stats, GET /context.

## Label legend

- FACT — named receipt, named file, or a LOCKED ruling quoted from its message id.
- INFERENCE — reasoning over facts. Attackable.
- HOLE — missing for Bible Stage 8 Spec (implementable files, interfaces, fail-closed). Spec cannot invent these.
- QUEUED — real, not this Bible. Named so it cannot rot.

Sources (read, not re-walked): this run 00_job.md 01_roster.md 02_ledger.md; uaimc-20260903/{uaimc-join.md,uaimc-live.md,NEXT_PLAN.md,02_ledger.md}; IFCH wakes on this computer at /home/box/.ifch/wakes/grok.jsonl and /tmp/ifch-80.txt. Cited ids: Clio sizing m_mtlszk6skgp7i4 (host=A_A_9); Vesper verify m_mtlt3icp8s6p91; Grok score m_mtlt8dv3vfj6ez; Vesper score-endorse m_mtlt94hlv8gksk; Grok caller-contract draft m_mtltnxyui71c20; Grok LOCK-candidate ①②③ m_mtlv42zscp2096; Vesper LOCK+A1/A2 m_mtlv669mozinju; Vesper five rulings m_mtlrmp49a861hl; Vesper STANDING GO m_mtlus2kckeikj6. P-CANS AGENT_HANDOFF.md was read by Grok on AA9, not present on this computer. .env not opened.

## Decision (LOCKED by Vesper, family recommendation)

| item | status | source |
|---|---|---|
| UAIMC-lite | CHOSEN | Grok score m_mtlt8dv3vfj6ez; Vesper endorse m_mtlt94hlv8gksk; Logan STANDING GO in m_mtlus2kckeikj6 ② |
| Mouth-caps | PREREQUISITE, before any smaller store is cut | same; 4th branch m_mtlrmp49a861hl |
| Full UAIMC as the build | RETIRED as a distraction | m_mtlt94hlv8gksk |
| Option 0 (harden in place) | live-service posture until announced cutover | m_mtlus2kckeikj6 |
| UAIMC-nano | QUEUED. UGDMC-shaped pointer future, names and locations, zero content. Not this Bible. | m_mtlrmp49a861hl; m_mtlt94hlv8gksk |
| Stay vs UGDMC/UCPMC | QUEUED behind this pack. Two identity registries would mint the family two-Jessica problem. | m_mtltqil1lfjfsc |

FACT. Scoring branches as registered (m_mtlt8dv3vfj6ez, endorsed m_mtlt94hlv8gksk):

1. M6 nano-first DID NOT FIRE. Content already clean (verbatim/summaries distinct_ratio 0.9989).
2. Content-dominates therefore full-in-place DID NOT FIRE. Content is 43.34 percent of payload and about 16 percent of the 10.125 GiB file.
3. derived/log/free over about 60 percent of the 10.13 GiB file DID FIRE. Payload floor 56.66 percent (Clio refused to round). File-level 64.7 percent unattributed sits on 98.9 percent derived rows. SUPPORTED-BY-STRONG-INFERENCE. dbstat would close the label, not reverse the branch. (WSL_DRVFS_REFUSED on dbstat.)
4. Mouth / 4th branch ALSO FIRED, independently. 67.3 percent of annotations are graph:* expansion. 104 hubs with more than 10k links. Lite under an unthrottled mouth refills.

INFERENCE (Grok, endorsed). Live option is lite with mouth-caps as a prerequisite, not a substitute.

## ① Caller contract (LOCKED)

Status: LOCKED by Vesper m_mtlv669mozinju on Grok LOCK-candidate m_mtlv42zscp2096, which revised draft m_mtltnxyui71c20 plus DEDUP SENTINEL addition m_mtltwaf1qyuvwu. Amendments A1/A2 land on ②, not ①.

Host law (FACT, Vesper ruling 4e / LOCK-candidate): every receipt names the HOST. This service is host=A_A_9, 127.0.0.1:8767. Never 8765 (QDAI Hub owns 8765 WebSocket and 8766). M1 also has a UAIMC on :8767. verify-the-pair.

P-CANS (FACT, Grok read of AGENT_HANDOFF.md 2026-08-07 0.1.0-dev at D:\dev\P-CANS\P-CANS\AGENT_HANDOFF.md): a bridge at PlugMemClient, not a UAIMC replacement. Same port. Write POST /ingest. Read GET /query, GET /recent, GET /health. MCP names pcans_handshake, pcans_ingest, pcans_context, pcans_search, pcans_recent, pcans_health, pcans_discover, pcans_promote. Duplicate sentinel summary_id == -2. Circuit breaker plus in-memory pending queue (lost on restart, PARTIAL). Dashboard is DEMO, never a memory store. HOLE: the handoff file is not on this computer; this pack cites Grok's read, not the file.

### Tier A (must hold for any lite)

| route | obligation |
|---|---|
| GET /health | wait-never-restart if nssm RUNNING. Cold-start needs at least 30s timeouts and 60s cold. nssm RUNNING means WAIT, never restart. (Vesper 4c) |
| GET /query | hold |
| GET /recent | hold |
| POST /ingest | promotion-gated, high-signal only; never dump chat logs. P-CANS is a caller of the mouth, so ② graph:* caps apply on this path. |

### GUARANTEE — DEDUP SENTINEL (was folklore; now contract text)

FACT (LOCKED). POST /ingest returning `summary_id:-2` is SUCCESS. The row is already stored. Callers MUST NOT retry a -2. A retry is a contract violation that feeds the duplication metric. Treat -2 like HTTP 200, never like 5xx. Callers that cannot distinguish -2 from hard failure are non-compliant.

### Still OUT of Tier A

- GET /context — documented deadlock. pcans_context stays gated until root-caused. An endpoint with a known deadlock cannot be a contract guarantee. (Vesper m_mtltqil1lfjfsc; Cycle 1 envelope never probed it.)
- /backup, /ws, dashboard mock

### Tier B (compat or explicit refusal — never a hang, never a lie)

LOCKED ① does not enumerate Tier B. Cycle 1 NEXT_PLAN §4.2 named `/graph/*`, `/guardian/*`, `/ambient*`, `/knowledge*`, `/backup`, `WS /ws` as B. That list is INFERENCE relative to the LOCK; only /backup and /ws are explicitly out of A.

Named caller not in LOCKED A (FACT, uaimc-live.md): `C:\dev\uaimc-sampler` polls `127.0.0.1:8767/ready` and `/stats`. `/stats` has a recorded timeout. Cycle 1 proposed A included GET /ready, GET /stats, GET /context, POST /query. LOCKED A dropped /ready, /stats, /context and added GET /recent plus GET /query (GET, not POST). Spec must place /ready and /stats in B (explicit refusal or compat) or name the sampler as a non-contract caller. This is a Spec-stage hole, not a rewrite of the LOCK.

### Tier C

The remaining routes of the running 59. Unclaimed until a caller is named. Nothing moves down silently. FACT: running generation is 59 routes (uaimc-live.md). Payload shapes of every route: UNKNOWN. Cycle 1 made zero HTTP requests. Gate G4 defaulted no HTTP.

## ② Mouth-caps (LOCKED, prerequisite, build FIRST)

Problem (FACT, Clio m_mtlszk6skgp7i4, host=A_A_9):

- annotations total 12,926,101
- graph:* expansion 8,697,865 = 67.3 percent of all annotations (graph:tag 2,909,960; graph:edge 1,807,805; graph:name 1,659,136; graph:path 1,386,673; graph:node_type 771,691; graph:language 162,600)
- hubs: 104 nodes with more than 10,000 document_links
- content layer is clean (verbatim 122,117 / distinct 121,981 = 0.9989; summaries 122,120 / distinct 121,984 = 0.9989)
- the ingest mouth itself is modest (verbatim.source tools 44,412, github_reference 27,139, ifch 8,817). The flood is graph annotation fan-out, not a filesystem watcher. Clio corrected his own first read: document_links has no true origin column.
- kg_nodes frozen since 2026-04-02. verbatim/summaries/annotations halted 2026-08-14. kg_edges still writing 2026-09-03. One 4.5-month era. A recent-bound without mouth-caps cuts almost nothing unless the bound is tighter than 3 weeks.
- config "256" is an ENTRY COUNT, not a byte cap. A docker build once drove UAIMC to 18.44 GB via too-broad WATCHERS. (Vesper m_mtlrmp49a861hl.)

Rules (LOCKED, ingest-time, all writers including P-CANS), from m_mtlv42zscp2096:

1. Cap graph:* fan-out per ingest item (hard max edges/annotations minted from one write). Excess is dropped or deferred. Never silently expanded into unbounded hubs.
2. Filter low-signal expansion classes at the mouth (watcher/auto-ingest flood class). Entry-count knobs are not byte caps; do not treat them as one.
3. Prefer promote/high-signal gates already in P-CANS handoff; refuse chat-log dumps.
4. Emit an explicit mouth-reject / mouth-truncate signal callers can see (not a silent continue). Failure path must be executed in Test, BugHunt, or Break (Logan 2026-09-03).
5. No change to live :8767 until this spec LOCKed (it has) and a named AA9 worktree build is reviewed. This cloud computer still does not edit the live process.

Out of scope here: vacuum (freelist=0, FACT), recent-bound alone (era is ~4.5 months).

### Amendment A1 (LOCKED into ②)

FACT (Vesper m_mtlv669mozinju). Cap values come from MEASUREMENT, not invention. The hard max on graph:* fan-out per ingest item is derived from the observed healthy percentile in Clio's receipt data, named and justified in the build review, never a round number someone liked. An arbitrary knob is a tuned threshold wearing a cap's badge.

HOLE that blocks Spec. Clio reported class totals and hub counts. He did not report a per-ingest-item fan-out histogram or a healthy percentile. The integer cap is therefore not yet a number. Spec cannot invent it. A1 forbids invention. Bible Stage 8 needs the number, or a named computation over the receipt that produces it, before implementable files can freeze the cap.

### Amendment A2 (LOCKED into ②)

FACT (Vesper m_mtlv669mozinju). Dropping EXCESS DERIVED EXPANSION is safe because the content row is preserved and expansion is re-runnable. Unlike a wake message, the dropped thing is not the only copy (Class-C law respected). The mouth-reject/truncate signal must say WHAT was dropped (count + class), so the drop is enumerable at the moment it happens, not 27 days later.

HOLE that blocks Spec. Wire format of the mouth-reject / mouth-truncate signal is unnamed (status code? JSON fields? header?). A2 names the semantics (count + class, enumerable now). Spec still needs the interface.

## ③ Lite extraction (LOCKED, build SECOND)

Keep (LOCKED, m_mtlv42zscp2096):

- verbatim + summaries content core (~122k rows, distinct_ratio ~0.9989, CLEAN)
- Tier A HTTP/MCP caller surface from ①
- Host A_A_9, port 8767, Option 0 until cutover is announced

Do NOT copy blindly into lite:

- document_links (~17.6M rows, 868 MiB payload)
- annotations (~12.9M rows, 67.3 percent graph:*)
- graph fan-out hubs (104 nodes with more than 10k links)
- derived/log fill that fired the >60 percent branch

Size is an output of the extraction under mouth-caps, never a guessed GB target. FACT payload of verbatim+summaries together is 1,510,410,458 + 65,655,097 = 1,576,065,555 bytes (~1.47 GiB of TEXT/BLOB). That is payload, not pages. dbstat UNMEASURED, so hosted floor/ceiling as page bytes is HOLE not blocking ③'s keep/drop list.

FACT kg_nodes 247,015 rows, frozen since 2026-04-02, distinct on summary 9,361 (26.4x). LOCKED ③ keep-list is verbatim+summaries, not kg_nodes. kg_nodes is identity-shaped and dirty. Putting it in lite without a cap would reimport the fan-out class. INFERENCE: leave kg_nodes out of the first extraction unless Spec names a distinct-only subset. That choice is still open and is a Spec-stage hole (keep-list vs identity-index).

Nano stays UGDMC-shaped hosted-pointer future (names/locations, zero content). Not this lane. Stay vs UGDMC/UCPMC identity discipline stays queued. No nano build until that reconciliation.

## Safety envelope (LOCKED, standing)

| rule | source |
|---|---|
| No live :8767 edit from this cloud computer | 00_job; Vesper split; GBC cannot reach 127.0.0.1:8767 |
| No Railway for content. Full UAIMC and its content store stay LOCAL (Tailscale-reachable, never public). Only a nano pointer index could ever host, after sizing plus scoped credential. | m_mtlrmp49a861hl |
| verify-the-pair: host=A_A_9 on every measurement and receipt | Vesper 4e |
| Worktree isolated from live service. PID 4388 untouched until announced reversible cutover. Vesper final verify before announced cutover. Logan for commit/deploy. | m_mtlv669mozinju; 00_job |
| No /context probe. No /ingest against live. No /backup. No /ws. | Cycle 1 envelope, still standing |
| .env, vaults, tax, Boops closed | standing |
| PUI closed for this mandate cut | 00_job |
| Fail-closed. A durable receipt is transport proof, not completion. | 00_job |
| OmniLad off this computer | standing |

Build order (LOCKED): mouth-caps FIRST, then lite extraction. Hands after doctrine retask: Grok builder-owner (was spec steward); Iris spec-conformance (author≠verifier); Clio build adversary; Vesper final verify. echog released UNSTARTED. This seat (Scout) packs specs, does not build.

## Sizing snapshot the specs sit on (FACT, host=A_A_9)

Clio m_mtlszk6skgp7i4, Vesper independently re-measured five values over SSH (m_mtlt3icp8s6p91): page_count 2,654,349; freelist 0; verbatim 122,117; dup 122,117/121,981; kg_edges MAX(created_at)=2026-09-03T14:10:21. Arithmetic verified. Service PID 4388 RUNNING. quick_check ok. WAL advanced normally. Live file 10,872,213,504 B = 10.125 GiB. WAL 14,840,272 B. Freelist 0: VACUUM reclaims nothing.

| table | rows | payload bytes | class |
|---|---|---|---|
| verbatim | 122,117 | 1,510,410,458 | content, CLEAN |
| summaries | 122,120 | 65,655,097 | content, CLEAN |
| kg_nodes | 247,015 | 61,809,212 | identity-shaped, 26.4x on summary, frozen 2026-04-02 |
| annotations | 12,926,101 | 656,057,772 | derived, 67.3 percent graph:* |
| document_links | 17,633,743 | 868,359,267 | derived, 104 hubs >10k |
| kg_edges | 1,782,514 | 325,901,852 | derived, still writing |
| payload total | — | 3,837,000,155 (3.573 GiB) | 56.66 percent derived / 43.34 percent content |
| unattributed file | — | 7,035,213,349 (64.7 percent) | indexes + integers + overhead, dbstat UNMEASURED |

Five stale backup DBs ~23.4 GiB were in the same folder. Logan GO'd archive (m_mtlt7h6ypbd9sg). Clio posted archive receipt m_mtltuvs45knb60: 13 files / 21.84 GiB moved to F:\_ARCHIVE\UAIMC_stale_db_2026-09-03, live uaimc.db byte-identical, PID 4388 RUNNING, archives UNPROVEN as restores. Grok banked not self-verified. Not this pack's job.

## Cycle 1 contract vs LOCKED ① (delta, so Spec does not mix them)

| route | Cycle 1 NEXT_PLAN proposed A | LOCKED ① |
|---|---|---|
| GET /ready | A | not in A. Sampler still polls it. |
| GET /health | A | A, with wait-never-restart |
| GET /stats | A | not in A. Sampler still polls it. Recorded timeout. |
| POST /query | A | became GET /query |
| GET /query | — | A |
| GET /recent | — | A (from P-CANS handoff) |
| POST /ingest | A | A, plus DEDUP SENTINEL plus mouth-caps |
| GET /context | A | OUT. Deadlock. Gated. |

FACT. Do not implement Cycle 1 A. Implement LOCKED ①. A concurrent Hunt card on this path mixed Cycle 1 A into section 1.1; this file corrects that. Bible §0 already had LOCKED ① right.

## Holes that block Bible Stage 8 Spec

Spec must be implementable: files, interfaces, fail-closed. These four are unnamed. Inventing them would violate A1 or the evidence rule.

1. **A1 cap integer.** No per-ingest-item fan-out histogram, no healthy percentile. Clio has class totals (graph:tag 2.91M etc.) and hub count (104). That is not a cap. Need a named computation over the receipt, or a Clio/Quarry follow-up query, before Spec can freeze `MAX_GRAPH_FANOUT_PER_INGEST`.
2. **Mouth-reject / mouth-truncate wire format.** A2 names semantics (count + class, enumerable now). Status code, JSON fields, header: unnamed.
3. **HTTP payload schemas for Tier A.** Path-level only. Cycle 1 made zero HTTP requests. G4 default no HTTP. Spec cannot freeze request/response shapes for GET /health, GET /query, GET /recent, POST /ingest without a receipt or the P-CANS handoff file on this computer.
4. **Sampler vs LOCKED A.** `uaimc-sampler` polls /ready and /stats. Neither is in LOCKED A. Spec must say B-compat, B-explicit-refusal, or sampler-is-not-a-contract-caller. Leaving it implicit will ship a silent drop of a named caller.

Related, not blocking ⑧ if Spec names them as open:

- kg_nodes in or out of the first extraction (clean content vs dirty identity index).
- dbstat still UNMEASURED (WSL_DRVFS_REFUSED). Size remains an output.
- GET /context deadlock root cause. Out of A. Do not probe live to fill Spec.
- P-CANS AGENT_HANDOFF.md not on this computer. Grok's read is the citation. A copy into the run folder would close the independent-cite gap; it is not required to LOCK ①, which already happened.
- Stay vs UGDMC/UCPMC. Queued. Blocks nano, not lite Spec.
- Launch identity of PID 4388 still INFERENCE (Session 0, no elevation). Option 0 posture does not need it.

## Coverage, gaps, through-line

**Coverage.** ①②③ LOCKED text packed from the LOCK-candidate plus Vesper A1/A2, quoted from IFCH bodies on this computer, not restated from memory. Decision branches shown. DEDUP SENTINEL as guarantee. Mouth-caps first. Lite keep/drop list. Safety envelope. Cycle 1 A vs LOCKED A delta. Sizing numbers from the verified Clio receipt, host=A_A_9. Five prior Stay UAIMC Claims left in place, not reminted.

**Gaps.** The four Spec-blockers above. No product code. No live touch. No AGENT_HANDOFF.md body on this disk. dbstat unmeasured. Payload schemas unknown.

**Through-line.** UAIMC-lite is the chosen build because the store's bulk is derived fan-out, not memory, and the content core is already clean. Caps at the mouth are the actual fix; a smaller copy of an unthrottled mouth is a refill. Stay does not replace this service (Claim/StayDoesNotReplaceUaimc/s-a6d2 still holds). Stay vs UGDMC stays queued so nano does not mint a second identity graph. Full is retired. Live :8767 stays Option 0 until an announced cutover Vesper verifies.

HOLD. Scout idle for Bible Generate consuming this pack. No commit. Review point is Vesper before announced cutover, Logan for commit/deploy.

## Stay

Root: `/workspace/praxis/stay-pack/stay`. Events used: `promote` only, via `stay.hook.handle`. No `hook.py` written. No id reminted. No git-commit. No new path Artifacts from this seat. (Bible Bot independently minted `Artifact/UAIMC-LITE-BIBLE/u-c5ec` during this window; not this pack.)

Five Claims promoted this Cycle. Prior Cycle 1 UAIMC Claims left in place:

- Claim/UaimcLiveIs00Active/u-1055 (prior)
- Claim/Uaimc8767NotProbed/u-8505 (prior; listen later proved, id not reminted)
- Claim/UaimcTwoLineages/u-e5e9 (prior)
- Claim/UaimcFailureIsIdentity/u-4f04 (prior)
- Claim/StayDoesNotReplaceUaimc/s-a6d2 (prior)
- Claim/UaimcLiteChosen/u-8693
- Claim/DedupSentinelIsSuccess/d-e250
- Claim/MouthCapsPrerequisite/m-45d3
- Claim/VerifyThePairHostIsAA9/v-e0ce
- Claim/FullUaimcIsRetired/f-a4fe

Graph after this promote: 558 rows. Artifact 513, Claim 28, Role 6, Issue 4, System 3, Name 2, Place 1, State 1. This seat added 5 Claims, 0 Artifacts.

## Appendix A — P-CANS AGENT_HANDOFF.md (AA9 read 2026-09-03T20:29Z)

host=A_A_9. Read-only. CopyToBox and Read were refused (path outside local-exec root). Shell Get-Content of `D:\dev\P-CANS\P-CANS\AGENT_HANDOFF.md` succeeded. File exists, 16065 bytes. No `.env` opened. Env *names* below are from the handoff table; no values copied.

FACT. Version `0.1.0-dev`, date 2026-08-07. Package path in the doc: `artifacts/P-CANS/P-CANS/`. On-disk path this read: `D:\dev\P-CANS\P-CANS\AGENT_HANDOFF.md`.

FACT. One-sentence truth in the file: P-CANS is a working Python bridge library + MCP tool surface that can talk to a real CANS instance on port 8767. Dashboard and interactive HTML are demos. Graphs, CLN registry, extraction without a live extract URL, and pending-queue durability are local/in-memory.

FACT. It sits between agents and UAIMC/CANS. Not a UAIMC replacement. No forks of PlugMem or CANS. Bridge attaches at the PlugMemClient boundary.

FACT. Mapped live paths when `PCANS_CANS_URL` points at healthy UAIMC on **8767**:

| P-CANS tool | HTTP |
|---|---|
| pcans_ingest | POST /ingest |
| pcans_context | GET /context?mode=cans |
| pcans_search | GET /query |
| pcans_recent | GET /recent |
| pcans_health | GET /health (+ local circuit/pending) |

FACT. MCP callables named: `pcans_handshake`, `pcans_ingest`, `pcans_context`, `pcans_search`, `pcans_health`, `pcans_discover`, `pcans_promote`, `pcans_recent`. FastMCP registers `pcans_*_tool` (suffix `_tool`). PARTIAL.

FACT. Duplicate sentinel in the handoff, section 5: CANS ingest response `{ "summary_id": int, "status": "ok|duplicate|held|...", "annotations_count": int }`. Duplicate sentinel on CANS: `summary_id == -2`.

FACT. Documented ingest body (P-CANS contract, **not** a live 8767 probe): JSON with `content`, `source`, `author`, `channel`, `metadata` (type fact|reflection|episode, confidence, tags, concepts, graph_id, optional subgoal, plugmem_source), `summary` null.

FACT. Documented context read: `GET /context?agent=...&topic=...&max_chars=6000&mode=cans`. LOCKED ① still keeps `/context` OUT because of the documented deadlock. This appendix does not move `/context` into A.

FACT. Client timeout default `PCANS_TIMEOUT` = 15 seconds. Vesper 4c still says /health cold-start needs ≥30s timeouts and 60s cold, wait-never-restart if nssm RUNNING. Those two numbers are not the same. Spec must not collapse them.

FACT. High-signal only. Never dump chat logs into ingest. Do not use port 8765 (QDAI). Do not point production at `dashboard/server.py`. Do not hammer CANS when circuit is open.

INFERENCE. This closes the independent-cite gap on AGENT_HANDOFF.md. It does **not** close live payload schemas: no HTTP was sent to 8767 this pass. GET /health, GET /query, GET /recent response bodies remain unprobed.

## Appendix B — NEUROLUX nested uaimc-lite (names only)

host=A_A_9. `D:\BEACON_HQ\PROJECTS\00_ACTIVE\NEUROLUX` exists. Two nested dirs, same 16 top names. Not unified. Not copied.

1. `D:\BEACON_HQ\PROJECTS\00_ACTIVE\NEUROLUX\metaphysics-and-computing\uaimc-lite`
2. `D:\BEACON_HQ\PROJECTS\00_ACTIVE\NEUROLUX\Neurolux\uaimc-lite`

Top names in both (FACT, `dir /b`): `config`, `config.railway.json`, `Dockerfile.railway`, `guardian_prompts.py`, `guardian_tools.py`, `ppr_engine.py`, `railway.toml`, `requirements.railway.txt`, `start.railway.sh`, `tools`, `uaimc_ambient.py`, `uaimc_anno.py`, `uaimc_gpu.py`, `uaimc_service.py`, `uaimc_tools.py`, `uaimc_watcher.py`.

`config/` in both: `config.json`, `guardian_config.json` (names only, not opened).

`tools/` in both: ContextCompressor, ContextSynth, ConversationAuditor, ConversationThreadReconstructor, EchoGuard, EmotionalTextureAnalyzer, HashGuard, KnowledgeSync, MemoryBridge, SemanticFirewall, SQLiteExplorer, SQLSchemaDiff, TextTransform, TokenTracker.

INFERENCE. These look like service-tree copies nested under a site, not the C:\dev\uaimc-sampler (2 files). Railway filenames are present. Railway for content stays forbidden; listing the names is not a deploy.

Byte-identity between the two trees: UNMEASURED. Do not unify.
