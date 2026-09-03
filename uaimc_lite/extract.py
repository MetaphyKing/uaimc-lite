"""Lite extraction (LOCKED ③). FIXTURE keep/drop only. H3 schema not invented.

Keep-list FIXTURE: verbatim, summaries.
Drop-list FIXTURE classes: graph:* expansion, document_links.
Never copies live AA9. Never binds :8767. HTTP wire format is HOLE.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .mouth import LiteClosed, require_fixture_identity

LIVE_MARKERS = (
    "D:\\BEACON_HQ\\PROJECTS\\00_ACTIVE\\UAIMC",
    "BEACON_HQ",
    "PID 4388",
)

# LOCKED ③ do-not-copy (SPEC_PACK). Caller FIXTURE keep-list cannot KEEP these.
# "graph hubs" is the hub class named in SPEC_PACK, not a keep-list table.
DO_NOT_COPY = frozenset(
    {
        "annotations",
        "document_links",
        "graph_hubs",
        "graph:*",
        "annotations-graph-fanout",
    }
)

# Expansion classes SPEC A2 names as re-runnable (content row preserved).
RECOVERABLE_EXPANSION = {
    "graph:*": "FIXTURE-re-run-expansion",
    "annotations-graph-fanout": "FIXTURE-re-run-expansion",
}

# FIXTURE only. Not LOCKED H3.
FIXTURE_KEEP = {
    "label": "FIXTURE",
    "locked": False,
    "tables": ("verbatim", "summaries"),
}

FIXTURE_DROP = {
    "label": "FIXTURE",
    "locked": False,
    "classes": (
        "graph:*",
        "document_links",
        "annotations-graph-fanout",
    ),
}


@dataclass
class DropRecord:
    class_name: str
    count: int
    recoverable: bool = False
    recovery_hint: str = ""
    source_ref: str = ""

    def __post_init__(self):
        if self.count < 0:
            raise LiteClosed("drop counts must be enumerable non-negative")
        # F4/F5/F7: recoverable is not a default-True claim; hint must be named.
        if self.recoverable and not self.recovery_hint:
            raise LiteClosed("recoverable drop requires named recovery_hint")
        if not self.recoverable:
            self.recovery_hint = self.recovery_hint or ""

    @property
    def recovery_ref(self):
        return self.recovery_hint

    def as_signal(self):
        """A2 semantics: count + class. Not an HTTP envelope."""
        return {
            "class": self.class_name,
            "count": self.count,
            "recoverable": self.recoverable,
            "recovery_hint": self.recovery_hint,
            "recovery_ref": self.recovery_hint,
            "source_ref": self.source_ref,
        }


@dataclass
class ExtractPlan:
    keep: list
    drop: list
    label: str = "FIXTURE"

    def as_signal(self):
        return {
            "label": self.label,
            "keep": list(self.keep),
            "drop": [d.as_signal() for d in self.drop],
        }


def _require_fixture(spec, kind):
    return require_fixture_identity(
        spec, kind, f"H3 open: no LOCKED {kind}; refuse unlabeled extract"
    )


def _normalize_path_text(text):
    # F9/E1: Windows path compare is case-insensitive and slash-insensitive.
    return str(text or "").replace("\\", "/").casefold()


def _is_live_dst(dst):
    text = _normalize_path_text(dst)
    if not text:
        return False
    return any(_normalize_path_text(m) in text for m in LIVE_MARKERS)


def _as_nonneg_int(value, label):
    if type(value) is not int:
        raise LiteClosed(f"{label}: count must be a non-negative int, not {type(value).__name__}")
    if value < 0:
        raise LiteClosed(f"{label}: negative count fail-closed")
    return value


def _count(rows):
    if isinstance(rows, bool):
        raise LiteClosed("count must be enumerable rows, not bool")
    if type(rows) is int:
        return _as_nonneg_int(rows, "count")
    if isinstance(rows, dict) and "count" in rows:
        return _as_nonneg_int(rows["count"], "count")
    try:
        n = len(rows)
    except TypeError as exc:
        # D2: TypeError is refuse, not a silent zero drop.
        raise LiteClosed(
            f"uncountable rows; TypeError is refuse, not a zero drop: {exc}"
        ) from exc
    return _as_nonneg_int(n, "count")


def _graph_count(annotations):
    if isinstance(annotations, bool):
        raise LiteClosed("annotations must not be bool")
    if isinstance(annotations, dict) and "graph_count" in annotations:
        return _as_nonneg_int(annotations["graph_count"], "graph_count")
    if type(annotations) is int:
        return _as_nonneg_int(annotations, "graph_count")
    try:
        items = list(annotations or [])
    except TypeError as exc:
        raise LiteClosed(
            f"annotations not enumerable; TypeError is refuse, not bypass: {exc}"
        ) from exc
    n = 0
    for item in items:
        name = item if isinstance(item, str) else str((item or {}).get("class") or item)
        if str(name).startswith("graph:"):
            n += 1
    return n


def plan_extract(inventory, keep=None, drop=None, caps_ok=True):
    if not caps_ok:
        raise LiteClosed("mouth-caps Test must be green before lite extract")
    keep = _require_fixture(keep if keep is not None else FIXTURE_KEEP, "keep-list")
    drop = _require_fixture(drop if drop is not None else FIXTURE_DROP, "drop-list")
    if not isinstance(inventory, dict):
        raise LiteClosed("inventory must be a table->rows map")

    keep_tables = tuple(keep.get("tables") or ())
    drop_classes = tuple(drop.get("classes") or ())

    # F10: keep ∩ forbidden cannot KEEP, even if the same name is also in drop.
    overlap = set(keep_tables) & DO_NOT_COPY
    if overlap:
        raise LiteClosed(f"keep∩forbidden cannot KEEP: {sorted(overlap)}")

    known = _policy_known_tables(keep, drop)
    unknown = [t for t in inventory if t not in known]
    if unknown:
        # F6: UNKNOWN TABLE must REFUSE. Silent omit / record-as-unknown-drop rejected.
        raise LiteClosed(f"UNKNOWN TABLE must REFUSE: {sorted(unknown)}")

    records = []

    def add_drop(class_name, count, *, source_ref=""):
        hint = RECOVERABLE_EXPANSION.get(class_name, "")
        records.append(
            DropRecord(
                class_name,
                _as_nonneg_int(count, class_name),
                recoverable=bool(hint),
                recovery_hint=hint,
                source_ref=source_ref,
            )
        )

    if "document_links" in inventory:
        n = _count(inventory["document_links"])
        if n:
            add_drop("document_links", n, source_ref="document_links")
    annotations = inventory.get("annotations")
    if annotations is not None:
        n_all = _count(annotations)
        n_graph = _graph_count(annotations)
        if n_all:
            add_drop("annotations", n_all, source_ref="annotations")
        if n_graph:
            add_drop("graph:*", n_graph, source_ref="annotations")
            add_drop("annotations-graph-fanout", n_graph, source_ref="annotations")

    for class_name in drop_classes:
        if class_name in {"graph:*", "document_links", "annotations-graph-fanout", "annotations"}:
            continue
        if class_name in inventory:
            add_drop(class_name, _count(inventory[class_name]), source_ref=class_name)

    kept = [t for t in keep_tables if t in inventory]
    missing = [t for t in keep_tables if t not in inventory]
    if missing:
        raise LiteClosed(f"FIXTURE keep-list missing tables: {missing}")

    return ExtractPlan(keep=kept, drop=records, label="FIXTURE")


def apply_extract(plan, src, dst):
    if _is_live_dst(dst):
        raise LiteClosed("refuse write to live AA9 UAIMC tree")
    if not isinstance(plan, ExtractPlan):
        raise LiteClosed("plan required")
    if any(d.count < 0 for d in plan.drop):
        raise LiteClosed("drop counts must be enumerable")
    if any(d.class_name in DO_NOT_COPY and d.recoverable and not d.recovery_hint for d in plan.drop):
        raise LiteClosed("recoverable drop requires named recovery_hint")
    if not plan.drop and _src_has_fanout(src):
        raise LiteClosed("silent drop forbidden: fan-out present but drop-list empty")

    out = {}
    if not isinstance(src, dict):
        raise LiteClosed("src must be a table map")
    for table in plan.keep:
        if table in DO_NOT_COPY:
            raise LiteClosed(f"keep∩forbidden cannot KEEP: {table}")
        out[table] = src[table]
    for banned in DO_NOT_COPY:
        if banned in out:
            raise LiteClosed(f"refuse to copy {banned}")
    return {"dst": dst, "kept": out, "signal": plan.as_signal()}


@dataclass
class ExtractResult:
    """FIXTURE extract outcome. keep/drop counts by class. Not LOCKED H3 schema."""

    kept: dict
    keep_counts: dict
    drop_counts: dict
    drop_records: list = field(default_factory=list)
    label: str = "FIXTURE"
    dst: str | None = None

    def as_signal(self):
        return {
            "label": self.label,
            "keep_counts": dict(self.keep_counts),
            "drop_counts": dict(self.drop_counts),
            "drop": [d.as_signal() for d in self.drop_records],
        }


def _policy_known_tables(keep, drop):
    known = set(keep.get("tables") or ())
    for class_name in drop.get("classes") or ():
        # FIXTURE drop classes may name tables or expansion classes.
        if class_name in {"graph:*", "annotations-graph-fanout", "annotations"}:
            known.add("annotations")
        elif class_name == "graph_hubs":
            known.add("graph_hubs")
            known.add("document_links")
        else:
            known.add(class_name)
    # Always-known do-not-copy tables that this module enumerates when present.
    known.update({"document_links", "annotations"})
    return known


def _refuse_unknown_copy_request(requested_tables, keep, drop):
    """Fail-closed if asked to copy tables with no FIXTURE keep/drop policy."""
    if not requested_tables:
        return
    known = _policy_known_tables(keep, drop)
    keep_set = set(keep.get("tables") or ())
    unknown = []
    for table in requested_tables:
        if table in DO_NOT_COPY:
            unknown.append(table)
        elif table not in known:
            unknown.append(table)
        elif table not in keep_set:
            # Known as drop-class only — refuse copy (not keep).
            unknown.append(table)
    if unknown:
        raise LiteClosed(
            f"refuse copy of unknown/unkept tables without fixture policy: {sorted(set(unknown))}"
        )


def extract(inventory, keep=None, drop=None, caps_ok=True, dst=None, copy_tables=None):
    """FIXTURE lite extract. Returns keep/drop counts by class. H3 not invented.

    copy_tables: optional explicit copy request. Unknown tables without a
    FIXTURE keep policy fail-closed (LiteClosed). Never writes live AA9.
    """
    try:
        keep_spec = keep if keep is not None else FIXTURE_KEEP
        drop_spec = drop if drop is not None else FIXTURE_DROP
        keep_spec = _require_fixture(keep_spec, "keep-list")
        drop_spec = _require_fixture(drop_spec, "drop-list")

        if copy_tables is not None:
            _refuse_unknown_copy_request(list(copy_tables), keep_spec, drop_spec)

        plan = plan_extract(inventory, keep=keep_spec, drop=drop_spec, caps_ok=caps_ok)
        if dst is None:
            dst = "/workspace/praxis/uaimc-lite-20260903/fixtures/lite"
        applied = apply_extract(plan, inventory, dst)

        keep_counts = {table: _count(rows) for table, rows in applied["kept"].items()}
        drop_counts = {}
        for rec in plan.drop:
            drop_counts[rec.class_name] = drop_counts.get(rec.class_name, 0) + int(rec.count)

        result = ExtractResult(
            kept=applied["kept"],
            keep_counts=keep_counts,
            drop_counts=drop_counts,
            drop_records=list(plan.drop),
            label="FIXTURE",
            dst=applied["dst"],
        )
        if not verify_enumerable(result):
            raise LiteClosed("silent drop forbidden: extract result not enumerable")
        return result
    except LiteClosed:
        raise
    except (TypeError, ValueError) as exc:
        raise LiteClosed(
            f"closed-path type/value error is refuse, not bypass: {exc}"
        ) from exc


def verify_enumerable(result) -> bool:
    """FAIL if any silent drop (A2). FIXTURE check only — not LOCKED H3 wire."""
    if result is None:
        return False
    records = getattr(result, "drop_records", None)
    if records is None and isinstance(result, dict):
        records = result.get("drop_records") or result.get("drop") or []
        drop_counts = result.get("drop_counts") or {}
        keep_counts = result.get("keep_counts") or {}
    else:
        drop_counts = getattr(result, "drop_counts", {}) or {}
        keep_counts = getattr(result, "keep_counts", {}) or {}
    if records is None:
        return False
    for rec in records:
        count = rec.count if hasattr(rec, "count") else rec.get("count")
        class_name = rec.class_name if hasattr(rec, "class_name") else rec.get("class")
        if count is None or class_name is None:
            return False
        if int(count) < 0:
            return False
        recoverable = rec.recoverable if hasattr(rec, "recoverable") else rec.get("recoverable")
        hint = (
            rec.recovery_hint
            if hasattr(rec, "recovery_hint")
            else rec.get("recovery_hint") or rec.get("recovery_ref")
        )
        if recoverable and not hint:
            return False
    for k, v in keep_counts.items():
        if not isinstance(k, str) or int(v) < 0:
            return False
    for k, v in drop_counts.items():
        if not isinstance(k, str) or int(v) < 0:
            return False
    return True


def run(plan, src, dst):
    """Spec alias: extract.run(plan) -> applied shape. Never against AA9 live DB."""
    return apply_extract(plan, src, dst)


def plan(source_inventory, policy=None, caps_ok=True):
    """Spec alias: extract.plan(...). policy may carry keep/drop FIXTURE maps."""
    keep = drop = None
    if isinstance(policy, dict):
        keep = policy.get("keep")
        drop = policy.get("drop")
    return plan_extract(source_inventory, keep=keep, drop=drop, caps_ok=caps_ok)


def _src_has_fanout(src):
    if not isinstance(src, dict):
        return False
    if _count(src.get("document_links") or []) > 0:
        return True
    return _graph_count(src.get("annotations") or []) > 0
