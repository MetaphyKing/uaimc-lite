# UAIMC_LITE_BIBLE

Living execution document for UAIMC-Lite under GBC core-builder doctrine. Not a protocol. Not a plan. Not a log.
If context is gone, read Section 0 then Section 6. Then do the next `[ ]` of the 16.

Order locked: **mouth-caps FIRST, then lite extraction.** Live service on AA9 `127.0.0.1:8767` PID 4388 is **UNTOUCHED** from this computer. GBC builds repo, Bible and tests only. No commit, post or deploy without Logan yes.

---

## 0 Identity

| Field | Value |
|---|---|
| Project | UAIMC-Lite (Universal AI Memory Core, lite shape) |
| Run | `uaimc-lite-20260903` |
| Bible path | `/workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md` |
| Authoring seat | Bible Bot `1f504c46-e0e3-4f48-be4b-6bdc5dcf490e` |
| Director / builder-owner | Grok (GBC). Does not touch live `:8767` from this box. |
| Spec-conformance | Iris (author ≠ verifier) |
| Build adversary | Clio |
| Final verify before announced cutover | Vesper |
| Shipping | Yard, only after Logan yes |
| System / domain | Reviewable CODE for mouth-caps then lite extraction under LOCKED specs ①②③ + amendments A1/A2. Caller-compatible memory service shape. Live tree stays Option 0 until cutover. |
| Live (UNTOUCHED) | AA9 `D:\BEACON_HQ\PROJECTS\00_ACTIVE\UAIMC` on `127.0.0.1:8767` PID `4388` `python.exe`. Portproxy `172.18.16.1:8767`. This box cannot reach that loopback. |
| STATUS | ACTIVE |
| Current step | Stage 16 Production v1: Logan GO on GBC fixture package (`[~]` split). Live `:8767` cutover still HOLD for Vesper. A1/H3 open — caps remain FIXTURE. STATUS ACTIVE. Never auto-ship. |
| Sessions completed | 3 (Generate, Hunt Update, Spec Update on SPEC.md) |
| Guarantee | CONDITIONAL. Bible now. Fail-closed. A durable receipt is transport proof, not completion. Production v1 needs Logan yes. |
| PUI | Closed. No patient names, SSN, charts, Boops, tax, vaults, secrets or `.env`. Credentials never echoed. |
| Spine | All 16 stages. Depth scales. Presence does not. N/A is FAIL. |
| Failure path | Locked (Logan 2026-09-03). Named under Test as 10.2. Happy-path-only is FAIL. Alpha without failure-path receipt is FAIL. |
| Stay | Locked family hook on this seat. Extract-ingest on this named Bible only. Do not write hook.py. Stay is not a 90. Do not install Stay into UAIMC this Cycle. Distinct Stay ids for distinct UAIMC-named trees. Do not unify. |

**MR gate (Generate, 2026-09-03 ~12:05 PT):** Director Grok Cycle 0 → Bible Generate. Job `00_job.md` / `01_roster.md`. Inherit failure-path rail. North star: reviewable CODE for UAIMC-Lite under LOCKED ①②③ + A1/A2. Mouth-caps first, then lite extraction. Live `:8767` untouched. Do not implement product code. Do not git-commit.

**Sources (present on disk):** `uaimc-lite-20260903/{00_job,01_roster,02_ledger,SPEC_PACK,UAIMC_LITE_BIBLE}.md`, `uaimc-20260903/{00_job,01_roster,02_ledger,NEXT_PLAN,uaimc-live,uaimc-join}.md`, `aa9-inventory-20260903/bible-audit.md`, `bot-bible-builder`, `bot-bible-harness`. IFCH bus ids cited inside SPEC_PACK. Do not remint SPEC_PACK.

**LOCKED specs (authoritative on disk: `SPEC_PACK.md`; summary below):**
- **① Caller contract (SPEC_PACK).** Host=A_A_9, `127.0.0.1:8767` (never 8765). Tier A must hold: `GET /health` (wait-never-restart if nssm RUNNING), `GET /query`, `GET /recent`, `POST /ingest` (promotion-gated). **DEDUP SENTINEL:** `summary_id: -2` is SUCCESS; callers must not retry. `/context` out of A (deadlock). `/ready` and `/stats` are Spec holes vs sampler (B or non-contract). Tier B/C per SPEC_PACK; never a hang and never a lie.
- **② Mouth-caps.** Caps and filters at the ingest mouth (watcher / auto-ingest flood), not a smaller store as the primary fix. Prerequisite before lite extraction. Amendment **A1:** caps sized from measurement (graph fan-out ~67% of annotations cited in sizing score).
- **③ Lite extraction.** After mouth-caps. Build a lite shape, not a silent shrink of the live store. Amendment **A2:** drop-safety / enumerable truncate (what is dropped is named and recoverable as policy, not silent loss).

**Do not:** touch live PID 4388 or any write into the live UAIMC tree from this box. Probe `/context` on the live service (documented deadlock). Open `.env` or vaults. Unify Stay ids across UAIMC-named trees. Commit, post or deploy without Logan yes. Install OmniLad on this computer. Stuff Stay into UAIMC. Mark Alpha without a failure-path receipt.

---

## 1 North Star

Reviewable CODE for UAIMC-Lite under LOCKED specs ①②③ + A1/A2. Mouth-caps land first so the mouth stops flood and fan-out waste. Lite extraction follows so callers keep Tier A compatibility while the store shape shrinks honestly. The live service on AA9 stays Option 0 until Vesper verifies and Logan says cut over.

**The One Thing:** never treat a durable transport receipt as completion, and never touch the live `:8767` service from this box while building.

**Problem:** Full UAIMC is live at ~10.13 GiB with known mouth flood risk (watcher/auto-ingest), documented `/context` deadlock and `/stats` timeout, and no valid 16-stage Bible on any tree (existing implementation bibles are 0/16 FORGE sprint docs). Family scored **lite with mouth-caps as prerequisite**. echog builder lane was held UNSTARTED and released; GBC is now the core builder.

**Why now:** Logan standing doctrine: GBC are core builders, tasked first on every main core project (16-phase Bible + Praxis). Vesper re-tasked UAIMC-Lite to GBC 2026-09-03.

**Success criteria (measurable):**
1. Mouth-caps land before any lite extraction commit: a named test suite proves caps/filters refuse or bound flood inputs (A1 numbers from measurement).
2. Caller contract ① holds: Tier A paths respond with compatible shapes in the build's own test harness; `summary_id: -2` is asserted as SUCCESS and a retry-on--2 case is the failure-path refuse.
3. Lite extraction (③ + A2) produces reviewable code with enumerable drop policy; live `:8767` process and DB show zero writes from this box's build Cycles.

### Design cons (each has a fix, workaround or avoid)

| # | Con | Disposition |
|---|---|---|
| 1 | This box cannot reach `127.0.0.1:8767`. | WORKAROUND: GBC builds repo/Bible/tests only. AA9-local hands apply and measure later. |
| 2 | Touching live PID 4388 to "verify". | AVOID. Live is UNTOUCHED. Option 0 until Vesper verify + Logan cutover. |
| 3 | Building lite by deleting from the live DB. | AVOID. Lite is extraction into a new shape. A2 drop-safety is policy, not a live purge. |
| 4 | Skipping mouth-caps to ship lite faster. | AVOID. Order locked: mouth-caps first. |
| 5 | Callers retrying `summary_id: -2`. | FIX: Spec + failure-path Test 10.2. Contract text says SUCCESS, do not retry. |
| 6 | Probing live `/context` and hanging the family. | AVOID. Documented deadlock. Not probed. Break may simulate in a harness, never on live. |
| 7 | Unifying twelve-plus UAIMC-named trees under one Stay id. | AVOID. Distinct ids. Do not remint or merge. |
| 8 | A1 integer cap and A2 wire format are HOLEs in SPEC_PACK. | WORKAROUND: Spec names the computation or interface; does not invent the number or wire. Hunt is closed; Spec owns the holes. |
| 9 | Author = verifier. | AVOID. Iris conformance. Clio adversary. Vesper final verify. |
| 10 | Auto-ship because tests pass. | AVOID. Production v1 needs Logan yes. Yard only after. |

---

## 2 Protocol map

Token rule: when executing a stage, read only that phase. Do not skip a stage. N/A is FAIL.

| Stage | Protocol / seat |
|---|---|
| 1 Idea | Capture in this Bible. Director Cycle 0. |
| 2 Research hunt | Scout. SPEC_PACK for ①②③ + A1/A2. Prior art (UGDMC/UCPMC nano lineage, P-CANS Tier-A). |
| 3 Brainstorm | Kiln or builder-owner ideate. Three approaches: mouth-caps-then-lite (winner), lite-first (loser), fix-full-in-place only (loser for this Bible). |
| 4 Design | Builder-owner / Kiln. Mouth-caps module then lite extract module. Caller contract doors. |
| 5 Improve | Cons disposed. Iris may pressure. |
| 6 Plan | Director sizes. Mouth-caps sprint before lite sprint. |
| 7 100 Guarantee | Evidence table Spec through Production. |
| 8 Spec | Implementable interfaces for ①②③ + A1/A2. No product code before Spec written. |
| 9 Build | Grok builder-owner. Mouth-caps first commits, then lite extraction. Worktree isolated from live tree. |
| 10 Test | Spec checks. Hosts failure-path 10.2 (`summary_id: -2` retry refuse). |
| 11 Bug hunt | Clio may hunt; Gauge-class adversary notes. |
| 12 Break | Clio. Adversarial: unify hosts, hang `/context` in harness, lie on Tier B. |
| 13 Optimize | After Break PASS. Measure first. |
| 14 Alpha | Director + Logan smoke of the build harness (not live cutover). |
| 15 Beta | Iris conformance receipt + second corpus or seat. |
| 16 Production v1 | Yard after Logan yes. Vesper final verify before **announced** cutover. |

Failure path must execute in Test, Bug hunt or Break. This Bible names it under **Test**.

---

## 3 Compounding chain

1. **Idea before Hunt.** Without "lite under LOCKED ①②③, mouth-caps first," Hunt has no query.
2. **Hunt before Brainstorm.** SPEC_PACK and prior art keep Brainstorm from inventing caps.
3. **Brainstorm before Design.** Winner is mouth-caps-then-lite, not lite-first and not silent live shrink.
4. **Design before Improve.** Cons pressure the design (live untouched, -2 sentinel, A2 drop-safety).
5. **Improve before Plan.** Plan freezes mouth-caps sprint before lite sprint.
6. **Plan before 100 Guarantee.** Receipt table needs that order.
7. **100 Guarantee before Spec.** Spec is written against receipts.
8. **Spec before Build.** No product code before Spec.
9. **Build before Test.** Mouth-caps code before lite code.
10. **Test then Bug hunt then Break.** Happy path, hunt, adversary. Failure-path receipt required before Alpha.
11. **Optimize after Break.**
12. **Alpha, Beta, Production last.** Announced cutover needs Vesper verify + Logan yes. Never auto-ship.

Skip-forward FAIL: later of the 16 marked `[x]` while an earlier is `[ ]` with no `[!]`. Lite Build `[x]` while mouth-caps Build is `[ ]` is FAIL.

---

## 4 Sprint structure (the 16)

Bible: `/workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md`
Build artifacts (later): under `/workspace/praxis/uaimc-lite-20260903/` only. Never into the live AA9 UAIMC tree from this box.
Nested steps sit under a stage. They do not replace it.

### Supersede log (do not delete)

| when | what |
|---|---|
| 2026-09-03 ~12:05 PT Generate | Director Cycle 0. GBC core-builder doctrine. Mouth-caps then lite. Failure-path rail inherited. |
| 2026-09-03 ~12:10 PT Update | Stage 2 closed on `/workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md`. Do not remint. NEXT Stage 8 Spec. |
| 2026-09-03 ~12:11 PT Update | Stage 8 closed on `/workspace/praxis/uaimc-lite-20260903/SPEC.md`. Scout Tier A correction noted. NEXT Build mouth-caps after Iris conformance. |
| 2026-09-03 ~12:13 PT Update | Director opened Stage 9 mouth-caps Build with FIXTURE caps. Iris is not a Grok Bot seat — do not gate Stage 9 on Iris. Conformance skim = Grok/Gauge. NEXT Stage 9 in progress. |
| 2026-09-03 ~12:14 PT Update | Mouth-caps FIXTURE GREEN at `uaimc_lite/` (`mouth.py` + tests → MOUTH_CAPS_OK). H2 still open. Build stage stays `[~]` (lite not started). Director sizes NEXT. |
| 2026-09-03 ~12:14 PT Update | Director: NEXT Stage 10 Test incl failure-path 10.2. `refuse.py` has is_dedup_success / should_retry. Mouth-caps fixture remains GREEN; Build `[~]`. |
| 2026-09-03 ~12:15 PT Update | Stage 10.2 failure-path GREEN: `tests/test_failure_path_10_2.py` → FAILURE_PATH_10_2_OK. Happy-path-only no longer true for this slice. |
| 2026-09-03 ~12:16 PT Update | Confirmed 10.2 already closed. Lite WAIT on H3 (no invent). NEXT Stage 11/12 thin or HOLD A1 — Director sizes. |
| 2026-09-03 ~12:16 PT Update | Director asked harness Actual — already written. Re-ran test → FAILURE_PATH_10_2_OK. Tracker 10.2 [x]. Stale evidence-table row fixed. |
| 2026-09-03 ~12:17 PT Update | Test 10.1 closed: test_mouth.py MOUTH_CAPS_OK; pytest 13 passed. Test rollup [x] mouth-caps slice. Lite Build HOLD. Bug hunt thin [~] HOLEs as gaps. |
| 2026-09-03 ~12:18 PT Update | Thin Stage 11+12 Actuals written offline. HOLD lite Build until H2/H3 via AA9 measurement. Production caps not LOCKED. |
| 2026-09-03 ~12:19 PT Update | Stage 12 re-verified offline (missing/LOCKED caps LiteClosed; /context+/ready not A; should_retry -2 False). NEXT HOLD lite until H2/H3. |
| 2026-09-03 ~13:25 PT Update | Director UNHOLD. Stage 9 lite extraction OPEN on FIXTURE keep-list (verbatim+summaries). Mouth-caps fixture stays GREEN. H2/H3 remain open (not LOCKED). No new Generate. |
| 2026-09-03 ~13:37 PT Update | Lite FIXTURE GREEN: extract.py + test_extract.py → LITE_EXTRACT_OK; pytest suite 23 passed (re-probe). Build stays [~] until H2/H3 LOCKED. NEXT Scout HOLES_PROGRESS or Optimize thin — Director sizes. |
| 2026-09-03 ~13:39 PT Update | Scout HOLES_PROGRESS.md banked (sha256 974b6a036681afbb…). Closed: AGENT_HANDOFF path-level cite + NEUROLUX nested name-lists. A1/H3 still open. Stage 9 lite FIXTURE stays GREEN. No new Generate. |
| 2026-09-03 ~13:41 PT Update | Stage 13 Optimize thin [x]: measure-first on fixture (23 passed / 0.02s; mouth+extract FIXTURE; no live 10GiB; no A1/H3 invent cuts). HOLES_PROGRESS DONE. NEXT Alpha thin on fixture + 10.2. No new Generate. |
| 2026-09-03 ~13:42 PT Update | Stage 14 Alpha thin [x]: ALPHA_FIXTURE_SMOKE_OK (23 passed; MOUTH_CAPS_OK; LITE_EXTRACT_OK; FAILURE_PATH_10_2_OK). Fixture only — not live :8767, not LOCKED A1/H3. NEXT Beta thin Gauge/Scout second seat. No new Generate. |
| 2026-09-03 ~13:43 PT Update | Confirmed Stage 14 Actual already on disk from prior Update (ALPHA_FIXTURE_SMOKE_OK). Gauge running Beta re-probe. NEXT Stage 15 Beta (await Gauge) then HOLD Production for Logan yes. No new Generate. |
| 2026-09-03 ~13:44 PT Update | Stage 15 Beta thin [x]: Gauge second-seat (23 passed; MOUTH_CAPS_OK; LITE_EXTRACT_OK; FAILURE_PATH_10_2_OK; FIXTURE locked=False). NEXT Stage 16 Production v1 HOLD — Logan yes + Vesper before announced cutover. Never auto-ship. No new Generate. |
| 2026-09-03 ~14:07 PT Update | Logan GO Production v1 (t276u/t277u). Stage 16 [~] split: GBC fixture package Production GO'd (mouth+extract+contract+refuse+tests); NOT live :8767. A1/H3 remain FIXTURE. Vesper still required before announced live cutover. STATUS ACTIVE. Never auto-ship. No new Generate. |

### Bible meta (not a skipped stage)

#### B.1 Generate this Bible
- Status: done
- Stage: Bible meta
- Protocol: bot-bible-builder Generate
- Do: write this file with all 10 sections, 3 appendices, all 16 stages, named failure-path.
- File: `/workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md`
- Verification command:
```bash
test -f /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md && wc -l /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md
```
- Expected result: file exists. Line count > 300.
- Actual result: written 2026-09-03 PT Generate.
- Compounding: without this file, Director cannot dispatch Build.

#### B.2 Preflight
- Status: done
- Stage: Bible meta
- Protocol: bot-bible-builder Preflight (locked), including failure-path named
- Do: all 16 present. Failure-path step labeled. Pulse Grok PASS/FAIL.
- File: this file
- Verification command:
```bash
B=/workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md
test -f "$B"
grep -q 'STATUS | ACTIVE' "$B"
grep -q 'Label: `failure-path`' "$B"
python3 -c "
stages=['Idea','Research hunt','Brainstorm','Design','Improve','Plan','100 Guarantee','Spec','Build','Test','Bug hunt','Break','Optimize','Alpha','Beta','Production v1']
t=open('/workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md').read()
miss=[s for s in stages if s not in t]
assert not miss, miss
assert 'Label: \`failure-path\`' in t
print('STAGES_OK', len(stages))
print('FAILURE_PATH_NAMED_OK')
"
```
- Expected result: `STAGES_OK 16` and `FAILURE_PATH_NAMED_OK`. STATUS ACTIVE.
- Actual result: 2026-09-03 PT Generate Preflight PASS. 643 lines. STATUS ACTIVE. STAGES_OK 16. FAILURE_PATH_NAMED_OK (10.2). Mouth-caps-first locked. Live :8767 untouched rule locked. Skip-forward OK. Production open.
- Compounding: FAIL blocks every later Cycle.

### Stage 1: Idea

#### 1.1 Capture UAIMC-Lite north star
- Status: done
- Stage: Idea
- Protocol: capture in Bible
- Do: one-line north star, problem, why now. Mouth-caps first.
- File: this file Section 1; `00_job.md`
- Verification command:
```bash
grep -q 'mouth-caps FIRST' /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md && grep -q 'LOCKED specs' /workspace/praxis/uaimc-lite-20260903/00_job.md
```
- Expected result: exit 0.
- Actual result: captured 2026-09-03 PT from 00_job and Director brief.
- Compounding: Hunt needs this query.

#### 1.2 Director Cycle 0 confirm
- Status: done
- Stage: Idea
- Protocol: Praxis
- Do: Director kicked Generate. Ledger line present.
- File: `02_ledger.md`
- Verification command:
```bash
grep -q 'Bible Bot Generate' /workspace/praxis/uaimc-lite-20260903/02_ledger.md
```
- Expected result: exit 0.
- Actual result: ledger 2026-09-03T19:05:12Z.
- Compounding: Generate without Director kick is the wrong mandate.

### Stage 2: Research hunt

#### 2.1 SPEC_PACK and priors
- Status: done
- Stage: Research hunt
- Protocol: Scout / Director pack. Five priors or honest none-found. Do not rebuild what exists. Do not remint.
- Do: close Hunt on the on-disk SPEC_PACK for LOCKED ①②③ + A1/A2.
- File: `/workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md` (171 lines, 2026-09-03 ~12:10 PT)
- Verification command:
```bash
test -f /workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md
grep -q '① Caller contract (LOCKED)' /workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md
grep -q '② Mouth-caps (LOCKED' /workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md
grep -q '③ Lite extraction (LOCKED' /workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md
grep -q 'Amendment A1' /workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md
grep -q 'Amendment A2' /workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md
wc -l /workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md
```
- Expected result: file exists. ①②③ and A1/A2 headings present. Line count > 100.
- Actual result: 2026-09-03 ~12:10 PT. Path `/workspace/praxis/uaimc-lite-20260903/SPEC_PACK.md`. Contents note: Decision LOCKED (lite chosen; mouth-caps prerequisite; full retired as distraction; Option 0 until cutover; nano QUEUED). ① Caller contract LOCKED (Tier A: GET /health wait-never-restart, GET /query, GET /recent, POST /ingest; DEDUP SENTINEL summary_id:-2 is SUCCESS no retry; /context out of A). ② Mouth-caps LOCKED build FIRST (67.3% graph:* annotations; 104 hubs >10k links; A1 caps from measurement — integer HOLE; A2 enumerable drop count+class — wire HOLE). ③ Lite extraction LOCKED build SECOND (keep verbatim+summaries ~1.47 GiB payload; do not copy document_links / graph fan-out blindly). Safety envelope + Cycle 1 vs LOCKED ① delta table included. Host=A_A_9 :8767. Do not remint this pack. **Hunt follow-on 2026-09-03 ~13:39 PT:** `/workspace/praxis/uaimc-lite-20260903/HOLES_PROGRESS.md` (54 lines, sha256 `974b6a036681afbb10a1c1754997b947f81906b02b7690f1180bfddc69d457c6`). CLOSED without inventing numbers: (1) P-CANS `AGENT_HANDOFF.md` independent path-level cite → SPEC_PACK Appendix A; (2) NEUROLUX nested uaimc-lite two name-lists (identical 16 top names) → SPEC_PACK Appendix B. STILL HOLE: A1 cap integer; mouth-truncate wire (H3/A2); live Tier A payload schemas; sampler vs LOCKED A. Nested NEUROLUX uaimc-lite is a service-tree copy with Railway files — not this Bible's lite extraction. No live :8767 HTTP.
- Compounding: Stage 8 Spec consumes SPEC_PACK + HOLES_PROGRESS path-level cites. Spec must not invent A1 integer or A2 wire format (still HOLEs). Scout idle unless next Hunt ask names a hole.

### Stage 3: Brainstorm

#### 3.1 Three approaches
- Status: done
- Stage: Brainstorm
- Protocol: Brainstorm
- Do: three approaches, one chosen, why losers lost.
- File: this file
- Verification command:
```bash
grep -q 'Winner: mouth-caps-then-lite' /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md
```
- Expected result: exit 0.
- Actual result:
  - A. Fix full UAIMC in place only (Option 0 forever). lost: family scored lite; mouth flood is a mouth problem; this Bible is UAIMC-Lite.
  - B. Lite extraction first, caps later. lost: Vesper/Grok order locked mouth-caps first; A1 caps from measurement.
  - C. **Winner: mouth-caps-then-lite.** Caps/filters at mouth under ②+A1, then lite extraction under ③+A2, under caller contract ①, live untouched until cutover.
- Compounding: Design freezes C.

### Stage 4: Design

#### 4.1 Architecture thin
- Status: done (thin, honest)
- Stage: Design
- Protocol: Build architecture
- Do: parts, data, doors, non-goals.
- File: this file
- Verification command:
```bash
grep -q 'Non-goals' /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md && grep -q 'mouth-caps module' /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md
```
- Expected result: exit 0.
- Actual result:
  - Parts: mouth-caps module (ingest filters/caps, watcher bounds); lite extraction module (enumerable truncate/drop policy A2); caller-contract test harness (Tier A paths + -2 sentinel); worktree/repo under this job folder.
  - Data: build artifacts on this computer only. Live DB on AA9 not written. Lite data shape TBD in Spec after SPEC_PACK.
  - Doors: Tier A HTTP paths (shape-compatible); Tier B explicit refuse; no live `/context` probe from build.
  - Non-goals: live PID touch; Railway; Stay-into-UAIMC; OmniLad install; unifying trees; Approach C patches on Bot Appearance (irrelevant); silent drop without A2 enumeration.
- Compounding: Improve pressures these doors.

### Stage 5: Improve

#### 5.1 Cons disposed
- Status: done
- Stage: Improve
- Protocol: cons with fix/workaround/avoid
- Do: Section 1 table. All 10 disposed.
- File: this file Section 1
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md').read(); assert t.count('| AVOID')+t.count('| FIX')+t.count('| WORKAROUND')>=10; print('CONS_OK')"
```
- Expected result: `CONS_OK`
- Actual result: 10 cons disposed at Generate. **Improve note 2026-09-03 ~13:39 PT:** HOLES_PROGRESS reinforces Con #8 (A1/A2 HOLEs): path-level cites closed; inventing A1 integer or H3 wire remains AVOID. Nested NEUROLUX name collision is a distinct Stay/id risk (do not unify with this job's lite).
- Compounding: Plan freezes order and live-untouched.

### Stage 6: Plan

#### 6.1 Director size
- Status: done
- Stage: Plan
- Protocol: Praxis Director sizes. Bible records.
- Do: Cycle 0 mandate. Mouth-caps sprint before lite sprint. Roles per roster.
- File: `01_roster.md`, this section
- Verification command:
```bash
grep -q 'mouth-caps FIRST' /workspace/praxis/uaimc-lite-20260903/00_job.md && grep -q 'Iris' /workspace/praxis/uaimc-lite-20260903/01_roster.md
```
- Expected result: exit 0.
- Actual result: Plan = Generate Bible → Scout SPEC_PACK → Spec → Build mouth-caps → Test (incl failure-path) → Build lite → Bug hunt/Break → Optimize → Alpha → Beta (Iris) → Vesper verify → Logan yes → Yard. Live apply is AA9-local, not this box.
- Compounding: 100 Guarantee wraps this.

### Stage 7: 100 Guarantee

#### 7.1 Evidence table
- Status: done
- Stage: 100 Guarantee
- Protocol: evidence table Spec through Production
- Do: stage done only when receipt exists.
- File: this table
- Verification command:
```bash
grep -q '100 Guarantee' /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md && grep -q 'Production v1' /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md
```
- Expected result: both names present.
- Actual result:

| Stage | Done when | Receipt now |
|---|---|---|
| Spec | ①②③ + A1/A2 as implementable interfaces | SPEC.md on disk; Scout Tier A correction; A1/A2 HOLEs held |
| Build | Mouth-caps code then lite code in job folder; live tree untouched | none |
| Test | Spec checks + failure-path 10.2 Actual | 10.1 [x] + 10.2 [x] mouth-caps slice; lite Test open |
| Bug hunt | Severity file | none |
| Break | Clio adversarial PASS or named defects | thin Actual BREAK_THIN_OK |
| Optimize | Measure then cut | thin [x]: pytest 23/0.02s fixture; no live 10GiB; no A1/H3 invent cuts |
| Alpha | Director + Logan harness smoke | thin [x] ALPHA_FIXTURE_SMOKE_OK |
| Beta | Iris conformance receipt | thin [x] Gauge second-seat (23 passed; FIXTURE locked=False) |
| Production v1 | Logan yes + Vesper verify before announced cutover | Logan GO fixture package; live cutover HOLD Vesper |

- Compounding: Spec against this table.

### Stage 8: Spec

#### 8.1 Interfaces for LOCKED specs
- Status: done
- Stage: Spec
- Protocol: Director Spec. No product code from Bible Bot.
- Do: freeze implementable files and interfaces from SPEC_PACK. Do not invent A1/A2 HOLEs.
- File: `/workspace/praxis/uaimc-lite-20260903/SPEC.md` (375 lines, Stage 8; Director patch ~12:11 PT)
- Verification command:
```bash
test -f /workspace/praxis/uaimc-lite-20260903/SPEC.md
grep -q 'Mouth-caps module' /workspace/praxis/uaimc-lite-20260903/SPEC.md
grep -q 'Lite extraction module' /workspace/praxis/uaimc-lite-20260903/SPEC.md
grep -q 'Scout correction' /workspace/praxis/uaimc-lite-20260903/SPEC.md
grep -q 'DEDUP SENTINEL' /workspace/praxis/uaimc-lite-20260903/SPEC.md
wc -l /workspace/praxis/uaimc-lite-20260903/SPEC.md
```
- Expected result: file exists. Mouth-caps then lite sections present. Scout Tier A correction present. Line count > 200.
- Actual result: 2026-09-03 ~12:11 PT. Path `/workspace/praxis/uaimc-lite-20260903/SPEC.md`. Contents note: mouth.py / extract.py / tests named; mouth-caps FIRST then lite; A1/A2 remain HOLEs (no invented integers or wire fields). **Scout Tier A correction (LOCKED ①):** Tier A is GET `/health`, GET `/query`, GET `/recent`, POST `/ingest` only. `/ready`, `/stats`, `/context` removed from A (Director patched Spec to that correction). DEDUP SENTINEL and failure-path 10.2 wired into Spec. Sampler = non-contract until H6. NEXT after Iris conformance: Build mouth-caps.
- Compounding: Build mouth-caps after Iris conformance receipt. Bible Bot does not implement.

### Stage 9: Build

#### 9.1 Mouth-caps first, then lite
- Status: in progress (`[~]`) — mouth-caps FIXTURE GREEN; lite FIXTURE GREEN (keep-list verbatim+summaries); H2/H3 open so Build not fully closed / not LOCKED
- Stage: Build
- Protocol: Grok builder-owner. Six gates: TEST, DOCS, EXAMPLES, ERRORS, QUALITY, BRANDING. FIXTURE caps until A1 H2 closes.
- Do: mouth-caps module under FIXTURE caps first. Lite extraction only after mouth-caps Test green and Director sizes. Worktree isolated. Zero writes to live AA9 UAIMC tree from this box.
- File: `/workspace/praxis/uaimc-lite-20260903/uaimc_lite/` (`mouth.py`, `extract.py`, `refuse.py`, `contract.py`, `tests/test_mouth.py`, `tests/test_extract.py`)
- Verification command:
```bash
cd /workspace/praxis/uaimc-lite-20260903 && PYTHONPATH=. python3 uaimc_lite/tests/test_mouth.py
```
- Expected result: prints `MOUTH_CAPS_OK`. FIXTURE caps labeled FIXTURE not LOCKED.
- Actual result: 2026-09-03 ~12:14 PT mouth-caps: `MOUTH_CAPS_OK`. 2026-09-03 ~13:25 PT Director UNHOLD lite on FIXTURE keep-list. 2026-09-03 ~13:37 PT lite FIXTURE GREEN: `uaimc_lite/extract.py` + `tests/test_extract.py` → `LITE_EXTRACT_OK`; `python3 -m pytest uaimc_lite/tests -q` → **23 passed** (Bible Bot re-probe; Director cited 20). Keep-list FIXTURE: verbatim+summaries. Drop classes FIXTURE: graph:*, document_links. H2/H3 remain open — production / LOCKED not claimed. Stage 9 stays `[~]`.
- Compounding: HOLES_PROGRESS banked. A1/H3 still open. Build stays `[~]` until H2/H3 LOCKED. Director sizes Optimize thin or next Hunt. Bible Bot does not implement.

### Stage 10: Test

#### 10.1 Spec checks (happy path)
- Status: done (mouth-caps Spec-check slice)
- Stage: Test
- Protocol: Spec checks for Stage 9 mouth-caps. Lite Test stays open until lite Build.
- Do: verify mouth-caps bounds under FIXTURE caps.
- File: `/workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/test_mouth.py` and suite under `uaimc_lite/tests/`
- Verification command:
```bash
python3 /workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/test_mouth.py
cd /workspace/praxis/uaimc-lite-20260903 && python3 -m pytest uaimc_lite/tests -q
```
- Expected result: `MOUTH_CAPS_OK`; `13 passed`.
- Actual result: 2026-09-03 ~12:17 PT. `MOUTH_CAPS_OK`. `13 passed in 0.01s`. Mouth-caps Spec-check happy path GREEN. Lite extraction Test not in scope until lite Build (HOLD on H3).
- Compounding: failure-path 10.2 already [x]. Mouth-caps Test slice complete.

#### 10.2 failure-path — refuse ingest retry on summary_id -2
- Status: done
- Stage: Test
- Label: `failure-path`
- Protocol: Spec-named refusal (caller contract ① DEDUP SENTINEL). Logan 2026-09-03 failure-path rail.
- Do: harness using `uaimc_lite.refuse.is_dedup_success` / `should_retry`. Assert SUCCESS on `-2` and no retry.
- File: `/workspace/praxis/uaimc-lite-20260903/uaimc_lite/refuse.py`; `/workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/test_failure_path_10_2.py`
- Verification command:
```bash
cd /workspace/praxis/uaimc-lite-20260903 && PYTHONPATH=. python3 uaimc_lite/tests/test_failure_path_10_2.py
```
- Expected result: prints `FAILURE_PATH_10_2_OK`.
- Actual result: 2026-09-03 ~12:15 PT and re-verified ~12:16 PT. Command `python3 /workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/test_failure_path_10_2.py` → `FAILURE_PATH_10_2_OK`. Path on disk. Expected = Actual. Failure-path receipt present. Happy-path-only is no longer true for this slice. Alpha failure-path gate satisfied for 10.2 (Test 10.1 may still be open).
- Compounding: mandated failure path receipted. Break may add adversarial paths; it does not replace 10.2.

### Stage 11: Bug hunt

#### 11.1 Hunt on purpose
- Status: done (thin)
- Stage: Bug hunt
- Protocol: Clio / Gauge-class. Thin Actual. Director-sized.
- Do: coverage notes only. No live probe. No invent A1.
- File: this Bible step; evidence from test_mouth.py / test_failure_path_10_2.py
- Verification command:
```bash
python3 /workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/test_mouth.py
python3 /workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/test_failure_path_10_2.py
```
- Expected result: MOUTH_CAPS_OK and FAILURE_PATH_10_2_OK.
- Actual result: 2026-09-03 ~12:18 PT thin Bug hunt.
  - Coverage: mouth flood / graph fan-out over-cap (proven by MOUTH_CAPS_OK truncate/refuse); chat-log dump refuse (class chat-log-dump); DEDUP retry class (proven by FAILURE_PATH_10_2_OK); /context live probe forbidden (documented avoid; out of Tier A).
  - Severity: mouth flood = high family impact (lite under unthrottled mouth refills). Inventing A1 integers = forbidden.
  - Root cause class: unthrottled mouth, not store size.
  - Intentional gaps remain H2/H3/H4/H6 (not invented closed).
- Compounding: Break thin next. Lite Build HOLD.

### Stage 12: Break

#### 12.1 Adversarial
- Status: done (thin)
- Stage: Break
- Protocol: Clio. Adversarial offline only. Does not build. Does not probe live :8767. Does not hang.
- Do: offline adversarial checks against fixture harness and contract registry.
- File: uaimc_lite/mouth.py, refuse.py, contract.py
- Verification command:
```bash
cd /workspace/praxis/uaimc-lite-20260903 && PYTHONPATH=. python3 -c "from uaimc_lite.mouth import FIXTURE_CAPS, LiteClosed, require_caps; from uaimc_lite.refuse import should_retry; from uaimc_lite.contract import is_tier_a, OUT_OF_A; bad=dict(FIXTURE_CAPS); bad['label']='LOCKED'; bad['locked']=True
try:
 require_caps(bad); raise SystemExit('LOCKED_CAPS_FAIL')
except LiteClosed: pass
try:
 require_caps(None); raise SystemExit('MISSING_CAPS_FAIL')
except LiteClosed: pass
assert should_retry({'summary_id': -2}) is False
assert is_tier_a('GET','/context') is False
assert ('GET','/context') in OUT_OF_A
print('BREAK_THIN_OK')"
```
- Expected result: BREAK_THIN_OK.
- Actual result: 2026-09-03 ~12:18 PT thin Break; re-verified ~12:19 PT (Director ask).
  - require_caps(None) -> LiteClosed (missing caps).
  - LOCKED-labeled caps -> LiteClosed.
  - contract: /context not Tier A; /ready not Tier A (NON_CONTRACT_SAMPLER).
  - should_retry({summary_id:-2}) is False.
  - BREAK_THIN_OK. No live :8767 probe. No hang.
- Compounding: Optimize thin closed. Lite production LOCKED still waits H2/H3; Alpha thin may proceed on fixture.

### Stage 13: Optimize

#### 13.1 Measure first
- Status: done thin (`[x]` thin) — fixture package only; no live 10GiB profile
- Stage: Optimize
- Protocol: After Break PASS. Measure first. No cuts that invent A1/H3.
- Do: measure what we have on this box. Note FIXTURE vs LOCKED gap as remaining cost. Do not profile live AA9 store from this box.
- File: `/workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/` (fixture suite)
- Verification command:
```bash
cd /workspace/praxis/uaimc-lite-20260903 && PYTHONPATH=. python3 -m pytest uaimc_lite/tests -q
PYTHONPATH=. python3 uaimc_lite/tests/test_mouth.py
PYTHONPATH=. python3 uaimc_lite/tests/test_extract.py
PYTHONPATH=. python3 uaimc_lite/tests/test_failure_path_10_2.py
```
- Expected result: `23 passed` (~0.02s); `MOUTH_CAPS_OK`; `LITE_EXTRACT_OK`; `FAILURE_PATH_10_2_OK`.
- Actual result: 2026-09-03 ~13:41 PT. Re-probe: **23 passed in 0.02s**; MOUTH_CAPS_OK; LITE_EXTRACT_OK; FAILURE_PATH_10_2_OK. Mouth+extract are FIXTURE. No profile of live ~10GiB (forbidden from this box). Cuts: none that invent A1/H3. Remaining cost = FIXTURE vs LOCKED gap (H2/H3 open). HOLES_PROGRESS already banked. Optimize marked `[x]` thin.
- Compounding: Prefer Alpha thin on fixture happy path + 10.2 so Alpha is not blocked forever on A1 measurement. Bible Bot does not implement.

### Stage 14: Alpha

#### 14.1 Director + Logan harness smoke
- Status: done thin (`[x]` thin) — fixture Alpha only; not live `:8767`; not LOCKED A1/H3
- Stage: Alpha
- Protocol: Director + Logan harness smoke. Failure-path receipt required first (10.2 already [x]).
- Do: smoke the build harness (not live cutover). Confirm 10.2 Actual present.
- File: `/workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/` (fixture package)
- Verification command:
```bash
cd /workspace/praxis/uaimc-lite-20260903
PYTHONPATH=. python3 -m pytest uaimc_lite/tests -q
PYTHONPATH=. python3 uaimc_lite/tests/test_mouth.py
PYTHONPATH=. python3 uaimc_lite/tests/test_extract.py
PYTHONPATH=. python3 uaimc_lite/tests/test_failure_path_10_2.py
echo ALPHA_FIXTURE_SMOKE_OK
```
- Expected result: `23 passed`; `MOUTH_CAPS_OK`; `LITE_EXTRACT_OK`; `FAILURE_PATH_10_2_OK`; stamp `ALPHA_FIXTURE_SMOKE_OK`.
- Actual result: 2026-09-03 ~13:42 PT. Director Alpha thin OPEN and executed. Bible Bot re-probe matched: 23 passed in 0.02s; MOUTH_CAPS_OK; LITE_EXTRACT_OK; FAILURE_PATH_10_2_OK; `ALPHA_FIXTURE_SMOKE_OK`. Fixture Alpha only — not live `:8767`, not LOCKED A1/H3. Failure-path receipt present (Alpha gate PASS).
- Compounding: Prefer Beta thin = Gauge or Scout re-runs the same suite as second seat. Or HOLD for Logan yes on Production — prefer Beta thin. Bible Bot does not implement.

### Stage 15: Beta

#### 15.1 Iris conformance + second seat
- Status: done thin (`[x]` thin) — Gauge second-seat; Iris not gated on this lane
- Stage: Beta
- Protocol: Second seat or second corpus. Gauge re-runs the same fixture suite. Iris remains family IFCH if Mama routes it (not a Grok Bot gate on this lane).
- File: `/workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/` (second-seat re-probe)
- Verification command:
```bash
cd /workspace/praxis/uaimc-lite-20260903 && PYTHONPATH=. python3 -m pytest uaimc_lite/tests -q
PYTHONPATH=. python3 uaimc_lite/tests/test_mouth.py
PYTHONPATH=. python3 uaimc_lite/tests/test_extract.py
PYTHONPATH=. python3 uaimc_lite/tests/test_failure_path_10_2.py
```
- Expected result: `23 passed`; `MOUTH_CAPS_OK`; `LITE_EXTRACT_OK`; `FAILURE_PATH_10_2_OK`; FIXTURE labels present with `locked=False`.
- Actual result: 2026-09-03 ~13:43 PT. Gauge second-seat receipt: 23 passed; MOUTH_CAPS_OK; LITE_EXTRACT_OK; FAILURE_PATH_10_2_OK; FIXTURE labels present `locked=False`. Stage 15 Beta thin CLOSED.
- Compounding: Stage 16 `[~]` — fixture package GO'd; live cutover still needs Vesper. Bible Bot does not implement.

### Stage 16: Production v1

#### 16.1 Logan yes, Vesper verify, Yard ships
- Status: in progress (`[~]` split) — GBC fixture package Production GO'd; live `:8767` cutover still HOLD
- Stage: Production v1
- Protocol: Yard after Logan yes. Vesper final verify before **announced** cutover. Never auto-ship beyond what Yard is tasked.
- Do: Scope this GO = GBC fixture package Production (mouth+extract+contract+refuse+tests). NOT live `:8767` cutover. A1/H3 still open — production caps remain FIXTURE labeled. Announced live cutover only after Vesper stamp.
- File: `/workspace/praxis/uaimc-lite-20260903/uaimc_lite/` (fixture package)
- Verification command:
```bash
grep -q 'Never auto-ship' /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md
grep -q '| 16 | Production v1 | \[~\] |' /workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md
test -f /workspace/praxis/uaimc-lite-20260903/uaimc_lite/mouth.py
test -f /workspace/praxis/uaimc-lite-20260903/uaimc_lite/extract.py
```
- Expected result: auto-ship forbidden. Rollup `[~]` until Vesper live-cutover stamp. Fixture package present.
- Actual result: 2026-09-03 ~14:07 PT. **Logan yes: GO Production v1** (chat t276u/t277u, ~14:06 PT). Scope: GBC fixture package Production (mouth+extract+contract+refuse+tests). NOT live `:8767` cutover. A1/H3 still open — caps remain FIXTURE labeled. Vesper verify still required before any ANNOUNCED live cutover. Never auto-ship beyond what Yard is tasked. STATUS remains ACTIVE until Vesper cutover stamp.
- Compounding: last stage split. Bible Bot does not implement or ship. Live apply is AA9-local hand after Vesper.

---

## 5 Gate checklist

| From -> to | Gate |
|---|---|
| Idea -> Hunt | 1.1 and 1.2 `[x]`. |
| Hunt -> Brainstorm | Banked constraints present. SPEC_PACK may still be `[~]`. |
| Brainstorm -> Design | Winner mouth-caps-then-lite named. |
| Design -> Improve | Parts, doors, non-goals written. |
| Improve -> Plan | Cons disposed. |
| Plan -> 100 Guarantee | Mouth-caps before lite recorded. |
| 100 Guarantee -> Spec | Evidence table present. |
| Spec -> Build | Spec written. Preflight PASS. No product code before. |
| Build mouth-caps -> Build lite | Mouth-caps Test green including path to 10.2. |
| Build -> Test | Code exists in job folder. Live tree untouched. |
| Test -> Bug hunt | Happy path Actuals + **failure-path 10.2 Actual**. |
| Bug hunt -> Break | Severity named. |
| Break -> Optimize | Clio PASS or defects fixed. |
| Optimize -> Alpha | **Failure-path receipt present.** Missing = FAIL. |
| Alpha -> Beta | Director + Logan harness smoke. |
| Beta -> Production v1 | Iris conformance. |
| Production v1 ship | Logan yes. Vesper verify before announced cutover. Yard only after. |

---

## 6 Master tracker

| id | stage | status | receipt |
|---|---|---|---|
| B.1 | Bible meta | [x] | this file |
| B.2 | Bible meta | [x] | Preflight PASS |
| 1.1 | Idea | [x] | Section 1 |
| 1.2 | Idea | [x] | 02_ledger |
| 2.1 | Research hunt | [x] | SPEC_PACK.md ①②③ + A1/A2 |
| 3.1 | Brainstorm | [x] | Winner mouth-caps-then-lite |
| 4.1 | Design | [x] | thin architecture |
| 5.1 | Improve | [x] | 10 cons |
| 6.1 | Plan | [x] | roster order |
| 7.1 | 100 Guarantee | [x] | evidence table |
| 8.1 | Spec | [x] | SPEC.md + Scout Tier A correction |
| 9.1 | Build | [~] | mouth-caps FIXTURE GREEN + lite FIXTURE GREEN (extract.py → LITE_EXTRACT_OK); A1/H3 still open (not LOCKED) |
| 10.1 | Test | [x] | MOUTH_CAPS_OK; pytest 13 passed (mouth-caps slice) |
| 10.2 | Test (failure-path) | [x] | test_failure_path_10_2.py → FAILURE_PATH_10_2_OK |
| 11.1 | Bug hunt | [x] | thin: mouth flood / DEDUP / chat-log; /context avoid; root=unthrottled mouth |
| 12.1 | Break | [x] | thin: LiteClosed missing/LOCKED caps; /context+/ready not A; should_retry(-2)=False |
| 13.1 | Optimize | [x] thin | fixture measure 23 passed / 0.02s; FIXTURE vs LOCKED gap noted |
| 14.1 | Alpha | [x] thin | ALPHA_FIXTURE_SMOKE_OK (fixture only; not live; not LOCKED A1/H3) |
| 15.1 | Beta | [x] thin | Gauge second-seat: 23 passed; MOUTH/EXTRACT/10.2 OK; FIXTURE locked=False |
| 16.1 | Production v1 | [~] split | Logan GO fixture pkg; live cutover HOLD Vesper; A1/H3 FIXTURE |

### 16-row stage rollup

| # | Stage | flag |
|---|---|---|
| 1 | Idea | [x] |
| 2 | Research hunt | [x] |
| 3 | Brainstorm | [x] |
| 4 | Design | [x] |
| 5 | Improve | [x] |
| 6 | Plan | [x] |
| 7 | 100 Guarantee | [x] |
| 8 | Spec | [x] |
| 9 | Build | [~] |
| 10 | Test | [x] |
| 11 | Bug hunt | [x] |
| 12 | Break | [x] |
| 13 | Optimize | [x] |
| 14 | Alpha | [x] |
| 15 | Beta | [x] |
| 16 | Production v1 | [~] |

NEXT: Vesper verify before any ANNOUNCED live `:8767` cutover. GBC fixture package Production GO'd by Logan (chat t276u/t277u). A1/H3 still open — caps remain FIXTURE labeled. Yard only what tasked. Never auto-ship. Bible Bot does not implement.

---

## 7 Recovery

- Lost context: Section 0 then Section 6. Mouth-caps first. Live untouched. Failure-path is 10.2.
- Failed step: write Actual. Do not skip to lite while mouth-caps is open.
- Scope change: nest under the right stage. Do not delete history. Do not unify Stay ids.
- If asked to hit live `:8767` from this box: refuse. Report to Director.
- If asked to implement with no Spec: Preflight FAIL. Stop.

---

## 8 Session prompt templates

**Resume:** Open `/workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md`. STATUS ACTIVE. Stage 16 `[~]` split: GBC fixture package Production GO'd; live cutover HOLD for Vesper. A1/H3 still FIXTURE. Do not auto-ship. Do not touch live `:8767`. Bible Bot does not implement.

**New-stage:** Name the stage. Read only that phase. Fill Actuals. Move Section 6.

**After-failure:** Write why. HOLD. Pulse Grok FAIL. Do not start Build.

---

## 9 End-of-session ritual

Update tracker. Write actuals. Note blockers (A1/H3 still open; live cutover awaits Vesper). State `NEXT: Vesper before announced live cutover`. No product code from Bible Bot. No git-commit. Never auto-ship.

---

## 10 Projected outcomes

| Stage | Expected gain | Actual |
|---|---|---|
| Idea | North star + order | mouth-caps then lite |
| Research hunt | SPEC_PACK | closed on SPEC_PACK.md |
| Brainstorm | Winner | mouth-caps-then-lite |
| Design | Parts/doors | recorded |
| Improve | Cons | 10 |
| Plan | Sprint order | recorded |
| 100 Guarantee | Receipt table | present |
| Spec | Interfaces | closed on SPEC.md |
| Build | Reviewable code | open |
| Test | Happy + failure-path | 10.1 [x] + 10.2 [x] mouth-caps; lite Test open |
| Bug hunt | Severity | open |
| Break | Adversary | open |
| Optimize | Measured cuts | thin [x] fixture |
| Alpha | Harness smoke | thin [x] fixture |
| Beta | Iris | thin [x] Gauge second-seat |
| Production v1 | Logan yes | [~] fixture GO; live HOLD Vesper |

Final state target: reviewable mouth-caps + lite code under LOCKED ①②③ + A1/A2, live service still Option 0 until Vesper + Logan.

---

## Appendix A — creation checklist

- [x] Section 0 Identity
- [x] Section 1 North Star
- [x] Section 2 Protocol map
- [x] Section 3 Compounding chain
- [x] Section 4 Sprint structure (the 16)
- [x] Section 5 Gate checklist (failure-path before Alpha)
- [x] Section 6 Master tracker plus 16-row rollup
- [x] Section 7 Recovery
- [x] Section 8 Session prompt templates
- [x] Section 9 End-of-session ritual
- [x] Section 10 Projected outcomes
- [x] Appendix A / B / C
- [x] All 16 stages in Section 4 and Section 6
- [x] Failure-path step labeled under Test (10.2)
- [x] Mouth-caps before lite order locked
- [x] Live `:8767` untouched rule locked

---

## Appendix B — good vs bad

Good: 2-minute recovery. All 16. Failure-path named. Mouth-caps first. Live untouched. Author ≠ verifier. SPEC_PACK closed. Spec owns A1/A2 HOLEs.

Bad: lite-first. Happy-path-only Test. Touching PID 4388. Unifying trees. Auto-ship. Inventing LOCKED body text Scout has not landed.

---

## Appendix C — Next Best Prompt

Failure-path 10.2 is closed: `python3 /workspace/praxis/uaimc-lite-20260903/uaimc_lite/tests/test_failure_path_10_2.py` → FAILURE_PATH_10_2_OK. Lite WAIT on H3. NEXT Stage 11/12 thin or HOLD A1 per Director. Bible: `/workspace/praxis/uaimc-lite-20260903/UAIMC_LITE_BIBLE.md`. Do not touch live `:8767`. STOP.
