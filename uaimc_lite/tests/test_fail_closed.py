#!/usr/bin/env python3
"""Fail-closed regressions for Clio D1–D4 and Iris F-series (F3 withdrawn).

H2/A1 cap integers are still FIXTURE. No live :8767.
"""

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from uaimc_lite.extract import (
    DO_NOT_COPY,
    FIXTURE_DROP,
    FIXTURE_KEEP,
    DropRecord,
    apply_extract,
    extract,
    plan_extract,
    _count,
    _is_live_dst,
)
from uaimc_lite.mouth import FIXTURE_CAPS, LiteClosed, apply_caps, require_caps


INV = {
    "verbatim": [{"id": 1}, {"id": 2}],
    "summaries": [{"id": 1}],
    "document_links": list(range(50)),
    "annotations": [f"graph:edge:{i}" for i in range(30)] + ["other:x"],
}


def _must_close(fn, *needles):
    try:
        fn()
    except LiteClosed as exc:
        text = str(exc).lower()
        for needle in needles:
            if needle.lower() in text:
                return exc
        raise AssertionError(f"LiteClosed text {exc!r} missing {needles}") from exc
    raise AssertionError("expected LiteClosed fail-closed")


def _mouth_refuses(event, caps=FIXTURE_CAPS, class_name=None):
    try:
        d = apply_caps(event, caps)
    except LiteClosed:
        return "liteclosed"
    assert d.action == "refuse", d
    if class_name:
        assert d.class_name == class_name, d
    return d


# --- Clio D1 / Iris F8: negatives fail-closed on mouth and extract ---


def test_d1_mouth_refuses_negative_rate_and_hub():
    d = _mouth_refuses(
        {"annotations": ["graph:tag:a"], "rate_count": -1}, class_name="rate-window"
    )
    assert d.dropped_count == len(d.dropped) > 0
    d = _mouth_refuses(
        {"annotations": ["graph:tag:a"], "hub_links": -3}, class_name="hub-link-ceiling"
    )
    assert d.dropped_count == len(d.dropped) > 0


def test_d1_mouth_refuses_negative_annotation_count():
    _mouth_refuses({"annotations": -5}, class_name="malformed")


def test_d1_negative_fixture_ceiling_is_not_a_slice():
    bad = dict(FIXTURE_CAPS)
    bad["max_graph_fanout_per_ingest"] = -1
    _must_close(lambda: require_caps(bad), "non-negative")
    _must_close(
        lambda: apply_caps({"annotations": ["graph:edge:1", "graph:edge:2"]}, bad),
        "non-negative",
    )


def test_f8_extract_refuses_negative_counts():
    _must_close(lambda: _count(-3), "negative")
    _must_close(
        lambda: extract({"verbatim": -1, "summaries": [{"id": 1}]}),
        "negative",
    )
    _must_close(
        lambda: extract({**INV, "document_links": -7}),
        "negative",
    )


# --- Clio D2: TypeError is refuse, not a bypass around LiteClosed ---


def test_d2_count_typeerror_is_liteclosed_not_zero():
    _must_close(lambda: _count(object()), "typeerror")
    _must_close(lambda: extract({**INV, "verbatim": object()}), "typeerror")


def test_d2_mouth_typeerror_is_closed_not_admit():
    d = _mouth_refuses(
        {"annotations": ["graph:tag:a"], "rate_count": object()},
        class_name="rate-window",
    )
    assert d.action == "refuse"
    d = _mouth_refuses({"annotations": object()}, class_name="malformed")
    assert "typeerror" in d.reason.lower() or "enumerable" in d.reason.lower()


# --- Clio D3: deny is live on non-graph paths ---


def test_d3_deny_refuses_non_graph_annotation():
    caps = dict(FIXTURE_CAPS)
    caps["graph_pattern_deny"] = ("other:evil",)
    d = apply_caps({"annotations": ["other:evil", "graph:tag:a"]}, caps)
    assert d.action == "refuse"
    assert d.class_name == "graph-pattern-deny"


def test_d3_deny_refuses_kind_path():
    caps = dict(FIXTURE_CAPS)
    caps["graph_pattern_deny"] = ("chat-log",)
    d = apply_caps({"kind": "chat-log-adjacent", "annotations": ["graph:tag:a"]}, caps)
    assert d.action == "refuse"
    assert d.class_name == "graph-pattern-deny"


# --- Clio D4: locked identity cannot be implied ---


def test_d4_missing_locked_is_not_fixture():
    bad = dict(FIXTURE_CAPS)
    del bad["locked"]
    _must_close(lambda: require_caps(bad), "locked identity")
    keep = dict(FIXTURE_KEEP)
    del keep["locked"]
    _must_close(lambda: plan_extract(INV, keep=keep), "locked identity")


def test_d4_truthy_locked_is_not_false_identity():
    bad = dict(FIXTURE_CAPS)
    bad["locked"] = 1
    _must_close(lambda: require_caps(bad), "locked identity")
    bad = dict(FIXTURE_KEEP)
    bad["locked"] = 0
    _must_close(lambda: plan_extract(INV, keep=bad), "locked identity")


# --- Iris F1 / F2: as_signal keeps enumeration; dropped_count units match ---


def test_f1_as_signal_includes_dropped_enumeration():
    d = apply_caps({"annotations": [f"graph:edge:{i}" for i in range(20)]}, FIXTURE_CAPS)
    sig = d.as_signal()
    assert "dropped" in sig
    assert sig["dropped"] == d.dropped
    assert sig["dropped_count"] == len(sig["dropped"]) == 12


def test_f2_refuse_dropped_count_matches_enumeration():
    d = apply_caps(
        {"annotations": [f"graph:edge:{i}" for i in range(5)], "rate_count": 99},
        FIXTURE_CAPS,
    )
    assert d.action == "refuse"
    assert d.dropped_count == len(d.dropped) == 5
    sig = d.as_signal()
    assert sig["dropped_count"] == len(sig["dropped"])


# --- Iris F4 / F5 / F7: recoverable and related refuse defaults ---


def test_f4_f5_recoverable_defaults_fail_closed():
    rec = DropRecord("document_links", 3)
    assert rec.recoverable is False
    assert rec.recovery_hint == ""
    _must_close(lambda: DropRecord("x", 1, recoverable=True), "recovery_hint")


def test_f7_missing_allow_is_refuse_not_admit():
    caps = dict(FIXTURE_CAPS)
    del caps["graph_pattern_allow"]
    _must_close(lambda: apply_caps({"annotations": ["graph:tag:a"]}, caps), "missing")


def test_f7_expansion_named_recoverable_only():
    plan = plan_extract(INV)
    by_class = {d.class_name: d for d in plan.drop}
    assert by_class["graph:*"].recoverable is True
    assert by_class["graph:*"].recovery_hint == "FIXTURE-re-run-expansion"
    assert by_class["document_links"].recoverable is False


# --- Iris F6: UNKNOWN TABLE must REFUSE ---


def test_f6_unknown_table_refuses_not_silent_omit():
    inv = {
        "verbatim": [{"id": 1}],
        "summaries": [{"id": 1}],
        "kg_nodes": list(range(10)),
        "kg_edges": list(range(5)),
    }
    _must_close(lambda: extract(inv), "UNKNOWN TABLE")
    _must_close(lambda: plan_extract(inv), "UNKNOWN TABLE")


def test_f6_named_drop_is_not_unknown():
    drop = dict(FIXTURE_DROP)
    drop["classes"] = FIXTURE_DROP["classes"] + ("kg_nodes",)
    inv = {
        "verbatim": [{"id": 1}],
        "summaries": [{"id": 1}],
        "kg_nodes": list(range(4)),
    }
    result = extract(inv, drop=drop)
    assert result.drop_counts["kg_nodes"] == 4
    assert "kg_nodes" not in result.kept


# --- Iris F9 / E1: live-tree write guard is case-insensitive ---


def test_f9_e1_live_dst_case_and_slash_fail_closed():
    assert _is_live_dst(r"D:\BEACON_HQ\PROJECTS\00_ACTIVE\UAIMC") is True
    assert _is_live_dst(r"d:\beacon_hq\projects\00_active\uaimc") is True
    assert _is_live_dst("d:/beacon_hq/projects/00_active/uaimc") is True
    plan = plan_extract(INV)
    _must_close(
        lambda: apply_extract(plan, INV, r"d:\beacon_hq\projects\00_active\uaimc"),
        "live",
    )
    _must_close(
        lambda: extract(INV, dst="D:/BEACON_HQ/PROJECTS/00_ACTIVE/UAIMC"),
        "live",
    )


# --- Iris F10: keep ∩ forbidden cannot KEEP ---


def test_f10_keep_intersect_forbidden_cannot_keep():
    assert "document_links" in DO_NOT_COPY
    assert "annotations" in DO_NOT_COPY
    keep = dict(FIXTURE_KEEP)
    keep["tables"] = ("verbatim", "summaries", "document_links")
    _must_close(lambda: plan_extract(INV, keep=keep), "keep", "forbidden")
    keep["tables"] = ("verbatim", "summaries", "annotations")
    _must_close(lambda: extract(INV, keep=keep), "keep", "forbidden")
    keep["tables"] = ("verbatim", "summaries", "graph_hubs")
    inv = {**INV, "graph_hubs": [{"hub": 1}]}
    drop = dict(FIXTURE_DROP)
    drop["classes"] = FIXTURE_DROP["classes"] + ("graph_hubs",)
    _must_close(lambda: plan_extract(inv, keep=keep, drop=drop), "keep", "forbidden")


class SuiteTest(unittest.TestCase):
    def test_all(self):
        test_d1_mouth_refuses_negative_rate_and_hub()
        test_d1_mouth_refuses_negative_annotation_count()
        test_d1_negative_fixture_ceiling_is_not_a_slice()
        test_f8_extract_refuses_negative_counts()
        test_d2_count_typeerror_is_liteclosed_not_zero()
        test_d2_mouth_typeerror_is_closed_not_admit()
        test_d3_deny_refuses_non_graph_annotation()
        test_d3_deny_refuses_kind_path()
        test_d4_missing_locked_is_not_fixture()
        test_d4_truthy_locked_is_not_false_identity()
        test_f1_as_signal_includes_dropped_enumeration()
        test_f2_refuse_dropped_count_matches_enumeration()
        test_f4_f5_recoverable_defaults_fail_closed()
        test_f7_missing_allow_is_refuse_not_admit()
        test_f7_expansion_named_recoverable_only()
        test_f6_unknown_table_refuses_not_silent_omit()
        test_f6_named_drop_is_not_unknown()
        test_f9_e1_live_dst_case_and_slash_fail_closed()
        test_f10_keep_intersect_forbidden_cannot_keep()


if __name__ == "__main__":
    SuiteTest().test_all()
    print("FAIL_CLOSED_OK")
