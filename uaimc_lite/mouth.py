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


@dataclass
class MouthDecision:
    action: str  # admit | refuse | truncate
    class_name: str
    reason: str
    admitted_count: int
    dropped_count: int
    dropped: list = field(default_factory=list)

    def as_signal(self):
        """A2 semantics (count + class). HTTP wire format is HOLE."""
        return {
            "action": self.action,
            "class": self.class_name,
            "reason": self.reason,
            "admitted_count": self.admitted_count,
            "dropped_count": self.dropped_count,
        }


def require_caps(caps=None):
    """Production path fail-closes while H2 is unset. Fixtures must be labeled FIXTURE."""
    if caps is None:
        raise LiteClosed("H2 open: no LOCKED cap table; refuse unbound ingest")
    if caps.get("label") != "FIXTURE" or caps.get("locked") is True:
        raise LiteClosed("caps must be labeled FIXTURE not LOCKED until H2 closes")
    if "max_graph_fanout_per_ingest" not in caps:
        raise LiteClosed("FIXTURE caps missing max_graph_fanout_per_ingest slot")
    return caps


def _annotations(event):
    if not isinstance(event, dict):
        return []
    raw = event.get("annotations") or event.get("graph") or []
    if isinstance(raw, int):
        return [f"graph:edge:{i}" for i in range(raw)]
    out = []
    for item in raw:
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


def apply_caps(event, caps=None):
    caps = require_caps(caps)
    if not isinstance(event, dict):
        return MouthDecision("refuse", "malformed", "ingest event must be a dict", 0, 1)

    kind = str(event.get("kind") or event.get("source") or "").lower()
    text = str(event.get("text") or event.get("body") or "")
    if caps.get("refuse_chat_log_dumps") and (
        kind in {"chat-log", "chat_log", "dump"} or "chat log dump" in text.lower()
    ):
        return MouthDecision(
            "refuse",
            "chat-log-dump",
            "POST /ingest is promotion-gated; never dump chat logs",
            0,
            1,
        )

    # CapTable slot: rate_window (FIXTURE). Fail-closed over-cap.
    if "rate_count" in event or "ingest_rate" in event:
        rate = event.get("rate_count", event.get("ingest_rate"))
        try:
            rate_n = int(rate)
        except (TypeError, ValueError):
            return MouthDecision("refuse", "rate-window", "unknown rate_count; fail-closed", 0, 1)
        if rate_n > int(caps["rate_window"]):
            return MouthDecision(
                "refuse",
                "rate-window",
                "over FIXTURE rate_window cap",
                0,
                1,
            )

    # CapTable slot: hub_link_ceiling (FIXTURE). Fail-closed over-cap.
    if "hub_links" in event or "hub_link_count" in event:
        hub = event.get("hub_links", event.get("hub_link_count"))
        try:
            hub_n = int(hub)
        except (TypeError, ValueError):
            return MouthDecision("refuse", "hub-link-ceiling", "unknown hub_links; fail-closed", 0, 1)
        if hub_n > int(caps["hub_link_ceiling"]):
            return MouthDecision(
                "refuse",
                "hub-link-ceiling",
                "over FIXTURE hub_link_ceiling cap",
                0,
                1,
            )

    fanout = _graph_fanout(event)

    # CapTable slots: graph_pattern allow/deny (FIXTURE). Unknown = refuse.
    allow = caps.get("graph_pattern_allow")
    deny = caps.get("graph_pattern_deny") or ()
    for ann in fanout:
        s = str(ann)
        if any(s.startswith(str(d)) for d in deny):
            return MouthDecision("refuse", "graph-pattern-deny", f"denied pattern: {s}", 0, 1)
        if allow is not None and not any(s.startswith(str(a)) for a in allow):
            return MouthDecision(
                "refuse",
                "graph-pattern-unknown",
                f"unknown graph pattern fail-closed: {s}",
                0,
                1,
            )

    ceiling = caps["max_graph_fanout_per_ingest"]
    if len(fanout) <= ceiling:
        return MouthDecision("admit", "graph:*", "under fixture ceiling", len(fanout), 0)

    kept = fanout[:ceiling]
    dropped = fanout[ceiling:]
    return MouthDecision(
        "truncate",
        "graph:*",
        "fixture fan-out cap; not a LOCKED A1 integer",
        len(kept),
        len(dropped),
        dropped=dropped,
    )


def check(event, caps=None):
    return apply_caps(event, caps=caps)
