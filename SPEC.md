# SPEC.md — UAIMC-Lite Stage 8

Seat: Kiln / Grok builder-owner. Written 2026-09-03 ~12:20 PT.
Consume only: UAIMC_LITE_BIBLE.md, SPEC_PACK.md, 00_job.md, 01_roster.md.
No product code. No git-commit. No live :8767. No .env. No OmniLad. No stay/hook.py.

**PATCH 2026-09-03 ~12:11 PT (Director):** Tier A rewritten to Scout LOCKED ① correction. `/ready` `/stats` `/context` removed from A.
Do not invent HOLE items. Do not invent A1 integers. Do not invent A2 drop-list fields. Do not invent HTTP payload shapes.

**Order locked:** mouth-caps FIRST, then lite extraction.
**Fail-closed.** Unknown = refuse or HOLE. Never hang. Never lie.
**Host rule:** every live claim names the host (AA9 vs M1). Both may listen on :8767.

Label legend (from SPEC_PACK):
| tag | meaning |
|---|---|
| FACT | On-disk cite |
| INFERENCE | Reasoning over FACT. Attackable |
| HOLE | Missing. Spec must not invent fill |
| ASSIGNMENT | Who owns the hole or duty |

---

## 0 Scope and non-goals

### In scope (this Spec)
1. Mouth-caps module interfaces (② + A1) — build first.
2. Lite extraction module interfaces (③ + A2) — build second after mouth-caps Test green.
3. Caller contract ① path-level Tier A / B / C obligations for harness.
4. DEDUP SENTINEL refuse behavior (Bible 10.2).
5. Gated `/context` resolution without inventing response body.
6. Safety envelope for this box vs AA9 live tree.
7. Honest open HOLE table H1–H10 with owners and Build-block flags.

### Out of scope (refuse)
- Product code before Spec Preflight PASS.
- Binding harness server to AA9 live loopback or writing into live UAIMC tree.
- Live probe of AA9 or M1 `:8767`.
- Inventing MAX_GRAPH_FANOUT_PER_INGEST or any rate/cap integer.
- Inventing drop-list schema fields or mouth-reject wire fields.
- Installing Stay into UAIMC. Writing `stay/hook.py`. Unifying Stay ids.
- OmniLad. `.env`. Credentials. Commit/post/deploy without Logan yes.

### Suggested Build tree (names only; no code this Stage)

```
/workspace/praxis/uaimc-lite-20260903/uaimc_lite/
  mouth.py
  extract.py
  contract.py
  refuse.py
  config.py
  server.py          # harness only; never live-bind to AA9
  tests/
    test_mouth.py
    test_dedup_sentinel.py
    test_context_gated.py
    test_tier_b_refuse.py
```

Worktree isolated under `/workspace/praxis/uaimc-lite-20260903/` only.
Zero writes to AA9 live tree `D:\BEACON_HQ\PROJECTS\00_ACTIVE\UAIMC` PID 4388.

---

## 1 Mouth-caps module (② + A1) — FIRST

### 1.1 Fact bank

**FACT.** Caps and filters sit at the ingest mouth (watcher / auto-ingest flood). Not a smaller store as the primary fix.
**FACT.** Prerequisite before lite extraction.
**FACT (A1).** Caps sized from measurement. Banked cite: graph fan-out ~67% of annotations (sizing score).
**HOLE H2.** Exact numeric caps table (rates, hub thresholds, `graph:*` patterns, config keys, integer ceilings). Owner: Clio/Scout. Spec does not invent numbers.

### 1.2 Files

| file | duty |
|---|---|
| `uaimc_lite/mouth.py` | Ingest mouth filters and caps. Bound flood and graph fan-out waste. |
| `uaimc_lite/config.py` | Cap/filter knobs as named keys whose *values* come from H2 measurement. No invented defaults that pretend to be LOCKED integers. |
| `uaimc_lite/tests/test_mouth.py` | Prove refuse-or-bound on flood inputs. Cap values injected as fixtures until H2 closes. |

### 1.3 Interfaces

```
# FACT shape of obligation; integers = HOLE H2
MouthDecision = Accept | Reject(reason: str, class: str)

mouth.check(ingest_event) -> MouthDecision
mouth.apply_caps(ingest_event, caps: CapTable) -> MouthDecision
```

- `CapTable` keys are named in Spec as *slots* only: rate window, hub-link ceiling, graph-pattern allow/deny. Slot values = **HOLE H2**.
- Banked measurement cite (graph fan-out ~67% of annotations) is sizing *context*, not an implementable integer.
- Until H2 closes: Build may land interfaces + fixture-driven tests. Build must not hardcode a pretend LOCKED MAX_* constant into production paths.

### 1.4 Refuse behaviors

| input | refuse |
|---|---|
| Flood / over-cap ingest | Reject at mouth. Named class. No silent accept. |
| Cap table missing (H2 open) | Fail-closed in production path: refuse unbound ingest rather than invent a number. Harness may inject fixture caps labeled FIXTURE not LOCKED. |
| Cap bypass attempt | Reject. Bug-hunt target. |

### 1.5 Gate into lite

Mouth-caps Test green (including path toward failure-path 10.2) before lite Build commits. Skip-forward FAIL.

---

## 2 Lite extraction module (③ + A2) — SECOND

### 2.1 Fact bank

**FACT.** After mouth-caps. Build a lite *shape*. Not a silent shrink of the live store.
**FACT (A2).** Drop-safety / enumerable truncate: what is dropped is named and recoverable as policy. Not silent loss.
**FACT.** Not a live DB purge. Zero writes to AA9 live tree from this box.
**HOLE H3.** Enumerable drop-list schema (table names, age windows, rebuildable vs content classes, recovery procedure, mouth-reject wire format details). Owner: Kiln/Scout after measurement. Spec does not invent schema fields.

### 2.2 Files

| file | duty |
|---|---|
| `uaimc_lite/extract.py` | Lite extraction into a new shape. Enumerable drop policy A2. |
| `uaimc_lite/tests/` (later extract tests) | Dry-run extract; assert every drop is named and recoverable per policy interface. |

### 2.3 Interfaces

```
# Policy shape only; field list = HOLE H3
DropRecord = named entry with: class, source_ref, recoverable: bool, recovery_hint: str
ExtractPlan = keep_set + drop_list[DropRecord]
ExtractResult = new_lite_shape + DropRecord[]

extract.plan(source_inventory, policy) -> ExtractPlan
extract.run(plan) -> ExtractResult   # never against AA9 live DB from this box
extract.verify_enumerable(result) -> bool  # FAIL if any silent drop
```

- Recoverable policy is **named**: every dropped class has a recovery path documented in the plan.
- Wire format of mouth-reject / drop enumeration beyond this interface = **HOLE H3** (related also to H4 for HTTP envelope if reject is returned over the wire).

### 2.4 Refuse behaviors

| action | refuse |
|---|---|
| Live DB purge framed as "lite" | Refuse. Lite is new-shape extraction. |
| Silent drop (no DropRecord) | Refuse. A2 FAIL. |
| Extract before mouth-caps Test green | Refuse. Order locked. |
| Write into AA9 live tree from this box | Refuse. Safety envelope. |

---

## 3 Caller contract ① — path-level

Port does **not** move. Canonical bind target for live claims: `127.0.0.1:8767`.
Path-level obligation only. HTTP payload schemas = **HOLE H4** owner Scout/Iris.
Harness fixtures may be named as placeholders. They are not official live shapes.

### 3.1 Tier A — must hold (path list)

**FACT (Scout correction 2026-09-03, LOCKED ① m_mtlv42zscp2096 + Vesper LOCK m_mtlv669mozinju).** Do **not** use NEXT_PLAN's proposed Tier A. LOCKED Tier A is:

| method | path | obligation |
|---|---|---|
| GET | `/health` | Compatible response shape. Wait-never-restart if nssm RUNNING (live AA9 policy; harness simulates). |
| GET | `/query` | Compatible response shape in harness. |
| GET | `/recent` | Compatible response shape in harness. |
| POST | `/ingest` | Compatible response shape in harness. Promotion-gated. Mouth-caps apply first. Honors DEDUP SENTINEL. |

**OUT of Tier A (FACT):** `GET /context` (deadlock; pcans_context gated), `/backup`, `/ws`, dashboard mock.

**Sampler (Spec choice, closes H6 as a ruling not a LOCK rewrite):** polls `/ready` and `/stats`, neither in LOCKED A. Choice: **B-compat**. Not B-refuse (would break a named caller). Not "not-a-contract-caller" (silent drop). `/stats` must not hang; time-bound then explicit refuse or a bounded document. Payload still HOLE H4.

### 3.2 DEDUP SENTINEL

**FACT.** `POST /ingest` returning `summary_id: -2` is **SUCCESS**. Callers **must not retry**.

| field | status |
|---|---|
| `summary_id: -2` | LOCKED success sentinel |
| Exact JSON envelope beyond that field | **HOLE H4** |

**Refuse (Bible 10.2 failure-path):**
- Retry-on-`-2` is a **failure-path**. Harness asserts: no-retry client PASSes; retrying client FAILs or is refused.
- Treat `-2` like success / idempotent hit. Never like 5xx.
- Happy-path-only Test = FAIL. Alpha without 10.2 Actual = FAIL.

Files:
| file | duty |
|---|---|
| `uaimc_lite/tests/test_dedup_sentinel.py` | Assert SUCCESS on `-2`. Assert refuse/fail on retry-on-`-2`. |

### 3.3 Tier B — implement or explicit documented refuse

| surface | rule |
|---|---|
| `/graph/*` | Implement **or** explicit documented refuse |
| `/guardian/*` | Implement **or** explicit documented refuse |
| `/ambient*` | Implement **or** explicit documented refuse |
| `/knowledge*` | Implement **or** explicit documented refuse |
| `/backup` | Implement **or** explicit documented refuse |
| `WS /ws` | Implement **or** explicit documented refuse |

**Never a hang. Never a lie.**

Default for this Lite Build until a caller claims implementation: **explicit refuse** via `refuse.py` (documented status + reason). Not an empty 200. Not a hang. Not a silent drop of the route from the catalog.

Sampler `/ready` and `/stats` live on **B-compat** (see §3.1). They are not LOCKED A. `/backup` and `WS /ws` default to explicit refuse (OUT of A). Cycle 1 B list for `/graph/*` etc. is INFERENCE vs LOCK; default explicit refuse until a caller is named.

Files:
| file | duty |
|---|---|
| `uaimc_lite/refuse.py` | Documented refuse envelopes for Tier B (and gated paths). Never hang. Never lie. |
| `uaimc_lite/tests/test_tier_b_refuse.py` | Each Tier B surface returns explicit refuse or implemented shape. No hang. |

### 3.4 Tier C — unclaimed

Remaining of **59** routes (live AA9 generation serves 59). Unclaimed until a caller is named.
Nothing moves from C to A/B silently.
No inventing caller names to claim routes.

---

## 4 GET /context — gated resolution

**FACT.** OUT of LOCKED Tier A (Scout correction). Still gated deadlock — never probe live.
**FACT.** Documented deadlock on live. Cycle 1 did not probe. Bible forbids live probe from this box.

### Spec resolution (no invented body)

| rule | text |
|---|---|
| Live probe | **Forbidden.** Never against AA9 or M1 `:8767`. |
| Harness | Harness-only simulation allowed. |
| Hang | Never. Harness must time-bound and return. |
| Lie | Never. Do not claim live compat body while body is unknown. |
| Response body | **HOLE H5** owner Grok/Iris. |

Until H5 closes:
- Path stays OUT of A.
- Harness exposes a stub that returns an explicit gated/refuse marker (not a fabricated live body).
- Build does not require H5 body to start mouth-caps.

Files:
| file | duty |
|---|---|
| `uaimc_lite/tests/test_context_gated.py` | Assert live probe absent. Assert harness never hangs. Assert no fabricated live body. |

**H5 does not block Build** when this gated/harness-only policy is followed.

---

## 5 Safety envelope

| rule | text |
|---|---|
| This box | Cannot reach live loopback `127.0.0.1:8767`. |
| Worktree | Isolated under `/workspace/praxis/uaimc-lite-20260903/`. |
| Live AA9 | `D:\BEACON_HQ\PROJECTS\00_ACTIVE\UAIMC` on `127.0.0.1:8767` PID **4388** `python.exe`. Portproxy `172.18.16.1:8767`. **Zero writes** from this box. |
| Host identity | AA9 vs M1 both may use `:8767`. Name host on every live claim. verify-the-pair. |
| Stay | Not installed into UAIMC this Cycle. Distinct Stay ids per UAIMC-named tree. Do not unify. Do not write `hook.py`. |
| OmniLad | Off this computer. |
| `.env` / credentials | Never open. Never echo. |
| Ship | No commit/post/deploy without Logan yes. Vesper verify before announced cutover. Never auto-ship. |
| `server.py` | Harness only. Does not live-bind to AA9. |

---

## 6 Open HOLE table (H1–H10)

Copied from SPEC_PACK.md §6. Owners named. Fill not invented.
**BLOCK Build** = mouth-caps or lite production paths cannot honestly close without the hole. Harness/fixture work may still proceed where noted.

| # | hole | owner | BLOCK Build? | notes |
|---|---|---|---|---|
| H1 | Full LOCKED ①②③ body text (Vesper LOCK / Grok LOCK-candidate message bodies) | Scout / Vesper | No (thin path Spec uses banked summaries) | Full paragraphs absent on disk. Path-level banked text is enough to proceed thin. |
| H2 | A1 numeric caps table (rates, hub thresholds, `graph:*` patterns, config keys, integers) | Clio / Scout | **YES** | Blocks production mouth-caps sizing. Fixture caps allowed in tests if labeled FIXTURE not LOCKED. |
| H3 | A2 enumerable drop-list schema (+ mouth-reject wire details) | Kiln / Scout after measurement | **YES** (for lite Build) | Mouth-caps Build may proceed. Lite Build blocked until schema named. |
| H4 | HTTP request/response schemas for Tier A | Scout / Iris | **YES** (for payload-compat claims) | Path-level harness OK with placeholders. Official live shape claims blocked. |
| H5 | `/context` response body | Grok / Iris | **No** | Resolved here as gated / harness-only / never hang / never lie / live probe forbidden. Body remains open. |
| H6 | Sampler vs LOCKED A (`/ready`+`/stats`) | Grok (Spec choice recorded) | **No** after this patch | **B-compat.** Not B-refuse. Not silent drop. `/stats` never hang. Payload still H4. |
| H7 | P-CANS AGENT_HANDOFF.md not on this computer | Scout | No | Co-tenant context. Not required to start mouth-caps interfaces. |
| H8 | Score receipt raw numbers (content %, M6 ratios, dbstat) | Clio / Scout | No for mouth-caps interfaces | Decision already banked lite+mouth-caps. Raw matrix not required to land module files. |
| H9 | NEUROLUX nested `uaimc-lite` tree never opened | Scout | No | Name-collision check before Yard ship. Not Build-start block. |
| H10 | PID 4388 launch identity (image path/cmdline) | Scout / AA9-local | No | Restart/survive story UNKNOWN. Live untouched regardless. |

### Build-blocking holes (rollup)

1. **H2** — A1 cap integer / numeric table. Owner: Clio/Scout.
2. **H3** — A2 drop-list schema / mouth-reject wire (lite path). Owner: Kiln/Scout after measurement.
3. **H4** — Tier A payload schemas. Owner: Scout/Iris.

Related: mouth-reject wire spans H3 and H4; do not invent either side.

Non-blocking for starting mouth-caps module + harness refuse tests: H1, H5 (under §4 resolution), H7, H8, H9, H10.

---

## 7 Fail-closed matrix

| situation | behavior |
|---|---|
| Cap integer unknown (H2) | Refuse unbound production ingest. Fixture-only in tests. |
| Drop schema unknown (H3) | Refuse lite extract run that would silent-drop. |
| Payload schema unknown (H4) | Path-level harness only. No official live shape claim. |
| `/context` body unknown (H5) | Gated harness stub. Live probe forbidden. |
| Sampler `/ready` `/stats` | B-compat. Time-bound `/stats`. Do not hang. Do not drop. Payloads still H4. |
| Tier B unimplemented | Explicit documented refuse. Never hang. Never lie. |
| Tier C unclaimed | Leave unclaimed. |
| Retry on `summary_id: -2` | Failure-path refuse (10.2). |
| Ask to touch AA9 PID 4388 / live tree | Refuse. Report to Director. |
| Ask to implement with no Spec | N/A — Spec is this file. Preflight then Build. |

---

## 8 Verification (Bible 8.1)

After this file lands, Bible Stage 8 verification becomes:

```bash
test -f /workspace/praxis/uaimc-lite-20260903/SPEC.md
grep -q 'mouth-caps' /workspace/praxis/uaimc-lite-20260903/SPEC.md
grep -q 'DEDUP' /workspace/praxis/uaimc-lite-20260903/SPEC.md
grep -q 'context' /workspace/praxis/uaimc-lite-20260903/SPEC.md
grep -q 'fail-closed' /workspace/praxis/uaimc-lite-20260903/SPEC.md
wc -c -l /workspace/praxis/uaimc-lite-20260903/SPEC.md
```

Expected: file exists; mouth-caps, DEDUP, context, fail-closed present; Build still closed until Preflight PASS and H2 path for production caps is owned.

---

## 9 What Build may do next (after Preflight)

1. Land `uaimc_lite/mouth.py` + `tests/test_mouth.py` with FIXTURE caps (not LOCKED integers).
2. Land `contract.py`, `refuse.py`, `server.py` (harness only).
3. Land `tests/test_dedup_sentinel.py`, `test_context_gated.py`, `test_tier_b_refuse.py`.
4. Stop before lite `extract.py` production run until H3 named.
5. Never bind to AA9. Never probe live `/context`. Never commit without Logan yes.

---

## Spec status

| check | result |
|---|---|
| Path | `/workspace/praxis/uaimc-lite-20260903/SPEC.md` |
| Mouth-caps before lite | Yes |
| Invented A1 integers? | No — H2 open |
| Invented A2 drop-list fields? | No — H3 open |
| Invented HTTP payloads? | No — H4 open |
| `/context` resolved without body invent? | Yes — gated / harness-only |
| H1–H10 present with owners? | Yes |
| Product code / commit / live touch / `.env` / OmniLad / hook.py? | No |
| NEXT | Iris conformance skim. Then Preflight. Then mouth-caps Build. |

---

## CONFLICT — concurrent Spec write (2026-09-03 ~12:11 PT)

Seat: Grok Bot executor (Stage 8 Spec task). Found this file already present with substantial content (~361 lines / ~16 KiB) authored by Kiln / Grok builder-owner ~12:20 PT.

**Action taken:** DID NOT CLOBBER. Appended this note and stopped.

**Intent of the refused rewrite:** thin honest implementable Spec covering mouth-caps FIRST then lite extraction; files/interfaces/fail-closed; DEDUP SENTINEL `summary_id:-2` SUCCESS no-retry; `/context` gated as HOLE H5 with documented deadlock (no invented resolution); H1–H10 from SPEC_PACK left open with owners; Test harness expectations for failure-path 10.2; no product code / commit / live touch.

**Skim of existing file (for parent):** mouth-caps module first (§1), lite second (§2), Tier A/B/C + DEDUP (§3), `/context` gated (§4; note: existing text claims a "resolution" as gated/harness-only — parent may want Iris to confirm that does not invent H5 body), H1–H10 table (§6) with Build-block flags, fail-closed matrix, Build-next list.

**HOLEs that BLOCK Build (per existing §6):** H2 (A1 caps), H3 (A2 drop schema / lite), H4 (Tier A payloads for compat claims), H6 (sampler vs Tier A).

**HOLEs that can wait:** H1, H5 (under gated policy), H7, H8, H9, H10.

No product code written. No commit. Live :8767 untouched.

---

## Patch 2026-09-03 — LOCKED ① correction

Scout pack superseded Cycle 1 NEXT_PLAN A. Spec Tier A is GET /health, GET /query, GET /recent, POST /ingest. `/ready` `/stats` `/context` are not A. Sampler is B-compat. `/context` is OUT of A and gated. A1 integers and payload schemas still not invented.
