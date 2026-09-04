"""Mouth-caps (LOCKED ②). Caps at ingest mouth. Not a smaller store.

H2 is open: no LOCKED production integers. Tests inject FIXTURE caps only.
Never binds live :8767. Never writes AA9.
"""

from __future__ import annotations

from dataclasses import dataclass, field


class LiteClosed(Exception):
    """Fail-closed. No disable path."""


# CapTable slot names (Spec §1.3). Values remain HOLE H2 until measurement.
# FIXTURE integers only — never LOCKED / never pretend-A1 production defaults.
CAP_SLOTS = (
    "rate_window",
    "hub_link_ceiling",
    "graph_pattern_allow",
    "graph_pattern_deny",
    "max_graph_fanout_per_ingest",
)

_INT_CAP_SLOTS = (
    "rate_window",
    "hub_link_ceiling",
    "max_graph_fanout_per_ingest",
)

# FIXTURE only. Not LOCKED. Not A1. H2 still open.
FIXTURE_CAPS = {
    "label": "FIXTURE",  # must stay FIXTURE, not LOCKED
    "locked": False,
    "max_graph_fanout_per_ingest": 8,  # FIXTURE
    "rate_window": 16,  # FIXTURE CapTable slot
    "hub_link_ceiling": 64,  # FIXTURE CapTable slot
    "graph_pattern_allow": (  # FIXTURE CapTable slot
        "graph:tag",
        "graph:edge",
        "graph:name",
        "graph:path",
        "graph:node_type",
        "graph:language",
    ),
    "graph_pattern_deny": (),  # FIXTURE CapTable slot
    "refuse_chat_log_dumps": True,
}


def require_fixture_identity(spec, kind, missing_msg):
    """D4: fixture identity is label==FIXTURE and locked is the False singleton."""
    if spec is None:
        raise LiteClosed(missing_msg)
    if spec.get("label") != "FIXTURE":
        raise LiteClosed(f"{kind} must be labeled FIXTURE not LOCKED until holes close")
    locked = spec.get("locked")
    if locked is not False:
        raise LiteClosed(f"{kind} locked identity must be False; got {locked!r}")
    return spec


@dataclass
class MouthDecision:
    action: str  # admit | refuse | truncate
    class_name: str
    reason: str
    admitted_count: int
    dropped_count: int
    dropped: list = field(default_factory=list)

    def __post_init__(self):
        # F2: dropped_count is the enumeration length, never a mixed event/item unit.
        if self.dropped_count != len(self.dropped):
            raise LiteClosed(
                "dropped_count unit mix: count must match dropped enumeration"
            )

    def as_signal(self):
        """A2 semantics (count + class + named drops). HTTP wire format is HOLE."""
        return {
            "action": self.action,
            "class": self.class_name,
            "reason": self.reason,
            "admitted_count": self.admitted_count,
            "dropped_count": self.dropped_count,
            "dropped": list(self.dropped),
        }


def _decision(action, class_name, reason, admitted, dropped):
    dropped = list(dropped)
    return MouthDecision(
        action, class_name, reason, admitted, len(dropped), dropped=dropped
    )


def _refuse(class_name, reason, dropped):
    dropped = list(dropped)
    if not dropped:
        dropped = [class_name]
    return _decision("refuse", class_name, reason, 0, dropped)


def require_caps(caps=None):
    """Production path fail-closes while H2 is unset. Fixtures must be labeled FIXTURE."""
    caps = require_fixture_identity(
        caps, "caps", "H2 open: no LOCKED cap table; refuse unbound ingest"
    )
    for slot in CAP_SLOTS:
        if slot not in caps:
            raise LiteClosed(f"FIXTURE caps missing {slot} slot")
    for slot in _INT_CAP_SLOTS:
        val = caps[slot]
        if type(val) is not int or val < 0:
            raise LiteClosed(f"FIXTURE {slot} must be a non-negative int, not {val!r}")
    allow = caps["graph_pattern_allow"]
    deny = caps["graph_pattern_deny"]
    if allow is None or deny is None:
        raise LiteClosed("graph_pattern allow/deny must be present; missing is not admit")
    if not isinstance(allow, (tuple, list)) or not isinstance(deny, (tuple, list)):
        raise LiteClosed("graph_pattern allow/deny must be sequences")
    return caps


def _as_nonneg_int(value, class_name):
    if type(value) is not int:
        raise LiteClosed(f"{class_name}: count must be a non-negative int, not {type(value).__name__}")
    if value < 0:
        raise LiteClosed(f"{class_name}: negative count fail-closed")
    return value


def _annotations(event):
    if not isinstance(event, dict):
        return []
    raw = event.get("annotations")
    if raw is None:
        raw = event.get("graph")
    if raw is None:
        return []
    if isinstance(raw, bool):
        raise LiteClosed("annotations must not be bool")
    if type(raw) is int:
        if raw < 0:
            raise LiteClosed("negative annotation count fail-closed")
        return [f"graph:edge:{i}" for i in range(raw)]
    try:
        items = list(raw)
    except TypeError as exc:
        raise LiteClosed(
            f"annotations not enumerable; TypeError is refuse, not bypass: {exc}"
        ) from exc
    out = []
    for item in items:
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, dict):
            name = item.get("class") or item.get("type") or item.get("name") or ""
            out.append(str(name))
        else:
            out.append(str(item))
    return out


def _graph_fanout(event):
    return [a for a in _annotations(event) if str(a).startswith("graph:")]


def _matches_deny(value, deny):
    s = str(value)
    return any(s.startswith(str(d)) for d in deny if d)


def _apply_caps_inner(event, caps):
    caps = require_caps(caps)
    if not isinstance(event, dict):
        return _refuse("malformed", "ingest event must be a dict", ["malformed"])

    kind = str(event.get("kind") or event.get("source") or "").lower()
    text = str(event.get("text") or event.get("body") or "")
    try:
        anns = _annotations(event)
    except LiteClosed as exc:
        return _refuse("malformed", str(exc), ["malformed"])
    fanout = [a for a in anns if str(a).startswith("graph:")]

    if caps.get("refuse_chat_log_dumps") and (
        kind in {"chat-log", "chat_log", "dump"} or "chat log dump" in text.lower()
    ):
        return _refuse(
            "chat-log-dump",
            "POST /ingest is promotion-gated; never dump chat logs",
            anns or ["chat-log-dump"],
        )

    # CapTable slot: rate_window (FIXTURE). Fail-closed over-cap and negatives.
    if "rate_count" in event or "ingest_rate" in event:
        rate = event.get("rate_count", event.get("ingest_rate"))
        try:
            rate_n = _as_nonneg_int(rate, "rate-window")
        except LiteClosed as exc:
            return _refuse("rate-window", str(exc), anns or ["rate-window"])
        if rate_n > caps["rate_window"]:
            return _refuse("rate-window", "over FIXTURE rate_window cap", anns or ["rate-window"])

    # CapTable slot: hub_link_ceiling (FIXTURE). Fail-closed over-cap and negatives.
    if "hub_links" in event or "hub_link_count" in event:
        hub = event.get("hub_links", event.get("hub_link_count"))
        try:
            hub_n = _as_nonneg_int(hub, "hub-link-ceiling")
        except LiteClosed as exc:
            return _refuse("hub-link-ceiling", str(exc), anns or ["hub-link-ceiling"])
        if hub_n > caps["hub_link_ceiling"]:
            return _refuse(
                "hub-link-ceiling",
                "over FIXTURE hub_link_ceiling cap",
                anns or ["hub-link-ceiling"],
            )

    # D3: deny applies to all annotations and non-graph kind/source paths, not just graph:*.
    deny = caps["graph_pattern_deny"]
    allow = caps["graph_pattern_allow"]
    for candidate in list(anns) + ([kind] if kind else []):
        if _matches_deny(candidate, deny):
            return _refuse(
                "graph-pattern-deny",
                f"denied pattern: {candidate}",
                anns or [str(candidate)],
            )

    for ann in fanout:
        s = str(ann)
        if not any(s.startswith(str(a)) for a in allow):
            return _refuse(
                "graph-pattern-unknown",
                f"unknown graph pattern fail-closed: {s}",
                anns or [s],
            )

    ceiling = caps["max_graph_fanout_per_ingest"]
    if len(fanout) <= ceiling:
        return _decision("admit", "graph:*", "under fixture ceiling", len(fanout), [])

    kept = fanout[:ceiling]
    dropped = fanout[ceiling:]
    return _decision(
        "truncate",
        "graph:*",
        "fixture fan-out cap; not a LOCKED A1 integer",
        len(kept),
        dropped,
    )


def apply_caps(event, caps=None):
    try:
        return _apply_caps_inner(event, caps)
    except LiteClosed:
        raise
    except (TypeError, ValueError) as exc:
        # D2: TypeError on a closed path is refuse, not a bypass around LiteClosed.
        raise LiteClosed(
            f"closed-path type/value error is refuse, not bypass: {exc}"
        ) from exc


def check(event, caps=None):
    return apply_caps(event, caps=caps)
