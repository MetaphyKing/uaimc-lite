"""Lite extraction (LOCKED ③). FIXTURE keep/drop only. H3 schema not invented.

Keep-list FIXTURE: verbatim, summaries.
Drop-list FIXTURE classes: graph:* expansion, document_links.
Never copies live AA9. Never binds :8767. HTTP wire format is HOLE.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .mouth import LiteClosed

LIVE_MARKERS = (
    "D:\\BEACON_HQ\\PROJECTS\\00_ACTIVE\\UAIMC",
    "BEACON_HQ",
    "PID 4388",
)

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
    recoverable: bool = True
    recovery_ref: str = "FIXTURE-re-run-expansion"

    def as_signal(self):
        """A2 semantics: count + class. Not an HTTP envelope."""
        return {
            "class": self.class_name,
            "count": self.count,
            "recoverable": self.recoverable,
            "recovery_ref": self.recovery_ref,
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
    if spec is None:
        raise LiteClosed(f"H3 open: no LOCKED {kind}; refuse unlabeled extract")
    if spec.get("label") != "FIXTURE" or spec.get("locked") is True:
        raise LiteClosed(f"{kind} must be labeled FIXTURE not LOCKED until H3 closes")
    return spec


def _is_live_dst(dst):
    text = str(dst or "")
    return any(m in text for m in LIVE_MARKERS)


def plan_extract(inventory, keep=None, drop=None, caps_ok=True):
    if not caps_ok:
        raise LiteClosed("mouth-caps Test must be green before lite extract")
    keep = _require_fixture(keep if keep is not None else FIXTURE_KEEP, "keep-list")
    drop = _require_fixture(drop if drop is not None else FIXTURE_DROP, "drop-list")
    if not isinstance(inventory, dict):
        raise LiteClosed("inventory must be a table->rows map")

    keep_tables = tuple(keep.get("tables") or ())
    drop_classes = tuple(drop.get("classes") or ())
    records = []

    def add_drop(class_name, count):
        records.append(DropRecord(class_name, int(count)))

    # Named FIXTURE refuse: do not copy these even if present.
    if "document_links" in inventory:
        n = _count(inventory["document_links"])
        if n:
            add_drop("document_links", n)
    annotations = inventory.get("annotations")
    if annotations is not None:
        n_graph = _graph_count(annotations)
        if n_graph:
            add_drop("graph:*", n_graph)
            add_drop("annotations-graph-fanout", n_graph)

    for class_name in drop_classes:
        if class_name in {"graph:*", "document_links", "annotations-graph-fanout"}:
            continue
        if class_name in inventory:
            add_drop(class_name, _count(inventory[class_name]))

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
    if not plan.drop and _src_has_fanout(src):
        raise LiteClosed("silent drop forbidden: fan-out present but drop-list empty")

    out = {}
    if not isinstance(src, dict):
        raise LiteClosed("src must be a table map")
    for table in plan.keep:
        if table in {"document_links", "annotations"}:
            raise LiteClosed(f"refuse to copy {table}")
        out[table] = src[table]
    for banned in ("document_links",):
        if banned in out:
            raise LiteClosed("refuse to copy document_links")
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
        if class_name == "graph:*":
            known.add("annotations")
        elif class_name == "annotations-graph-fanout":
            known.add("annotations")
        else:
            known.add(class_name)
    return known


def _refuse_unknown_copy_request(requested_tables, keep, drop):
    """Fail-closed if asked to copy tables with no FIXTURE keep/drop policy."""
    if not requested_tables:
        return
    known = _policy_known_tables(keep, drop)
    keep_set = set(keep.get("tables") or ())
    unknown = []
    for table in requested_tables:
        if table not in known:
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
        # Prefer first named class count; graph:* and annotations-graph-fanout may both appear.
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
    # keep_counts must name classes (tables) with non-negative ints
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


def _count(rows):
    if isinstance(rows, int):
        return rows
    if isinstance(rows, dict) and "count" in rows:
        return int(rows["count"])
    try:
        return len(rows)
    except TypeError:
        return 0


def _graph_count(annotations):
    if isinstance(annotations, dict) and "graph_count" in annotations:
        return int(annotations["graph_count"])
    if isinstance(annotations, int):
        return annotations
    n = 0
    for item in annotations or []:
        name = item if isinstance(item, str) else str((item or {}).get("class") or item)
        if str(name).startswith("graph:"):
            n += 1
    return n


def _src_has_fanout(src):
    if not isinstance(src, dict):
        return False
    if _count(src.get("document_links") or []) > 0:
        return True
    return _graph_count(src.get("annotations") or []) > 0
