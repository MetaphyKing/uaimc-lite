# UAIMC-Lite v0.1.0-fixture

GBC Production v1 **fixture package** (Logan GO 2026-09-03). Reviewable code for UAIMC-Lite: mouth-caps at the ingest mouth, then lite extraction into a new shape. Not a live cutover.

Version: `0.1.0-fixture` (see `VERSION`).

## What it is

| path | duty |
|---|---|
| `uaimc_lite/mouth.py` | Mouth-caps (LOCKED ②). FIXTURE CapTable only. |
| `uaimc_lite/extract.py` | Lite extract (LOCKED ③). FIXTURE keep/drop only. |
| `uaimc_lite/contract.py` | Path-level Tier A registry. |
| `uaimc_lite/refuse.py` | DEDUP SENTINEL + explicit refuse. Never hang. Never lie. |
| `uaimc_lite/tests/` | Mouth, extract, Bible 10.2 failure-path. |
| `docs/` | `SPEC.md`, `SPEC_PACK.md`, `HOLES_PROGRESS.md`. |

Harness/fixture only. No live server. No AA9 writes. No secrets. No `.env`.

## FIXTURE vs LOCKED

| label | meaning |
|---|---|
| **LOCKED** | Spec ①②③ + A1/A2 rulings. Path-level contract. Do not invent fill for open holes. |
| **FIXTURE** | Test-only numbers and keep/drop lists: `label="FIXTURE"`, `locked=False`. Not production defaults. |

Missing, unlabeled, or `LOCKED`-labeled caps/keep/drop **fail-closed** while A1/H3 are open. Fixture integers are not A1. Fixture drop classes are not H3 schema.

## Tier A (LOCKED ① — must hold)

Path-level only. HTTP bodies remain HOLE H4.

- `GET /health`
- `GET /query`
- `GET /recent`
- `POST /ingest`

**OUT of A:** `GET /context` (gated deadlock; never probe live), `/backup`, `/ws`. Sampler `/ready` and `/stats` are not LOCKED A.

## DEDUP SENTINEL (LOCKED ①)

`POST /ingest` returning `summary_id: -2` is **SUCCESS**. Callers **must not retry**. Treat `-2` like success / idempotent hit, never like 5xx. Retry-on-`-2` is Bible failure-path **10.2**. Happy-path-only Test is FAIL.

## Order locked

**Mouth-caps first, then extract.** Skip-forward is FAIL. Extract refuses if `caps_ok=False`. Lite is a new shape, not a live DB purge. A2: every drop is named (count + class), not silent loss.

## How to run tests

From this release tree (no live bind):

```bash
cd /workspace/praxis/uaimc-lite-20260903/release/uaimc-lite-v0.1.0-fixture
PYTHONPATH=. python3 -m pytest uaimc_lite/tests -q
PYTHONPATH=. python3 uaimc_lite/tests/test_mouth.py
PYTHONPATH=. python3 uaimc_lite/tests/test_extract.py
PYTHONPATH=. python3 uaimc_lite/tests/test_failure_path_10_2.py
```

Expected: `23 passed`; stamps `MOUTH_CAPS_OK`, `LITE_EXTRACT_OK`, `FAILURE_PATH_10_2_OK`; FIXTURE labels `locked=False`.

## Safety

- **No live `:8767` bind.** No listener in this pack. This box cannot reach AA9 `127.0.0.1:8767` PID 4388. Zero writes to the live UAIMC tree.
- **No Railway.** Content stays LOCAL. This pack does not deploy Railway.
- **No auto-ship.** Logan GO is this fixture package only. Announced live cutover still needs Vesper. No git commit / GitHub unless separately tasked.

## Still open — do not invent

- **A1 / H2** — numeric cap table (rates, hub thresholds, `graph:*` patterns, integer ceilings).
- **H3 / A2 wire** — enumerable drop-list schema and mouth-reject HTTP envelope.

See `docs/HOLES_PROGRESS.md` and `docs/SPEC.md` §6.
