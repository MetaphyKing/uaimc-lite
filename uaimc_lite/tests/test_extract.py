#!/usr/bin/env python3
"""Stage 9 lite extract tests. FIXTURE keep/drop only. H3 still open."""

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from uaimc_lite.extract import (
    FIXTURE_DROP,
    FIXTURE_KEEP,
    apply_extract,
    extract,
    plan_extract,
    verify_enumerable,
)
from uaimc_lite.mouth import LiteClosed

INV = {
    "verbatim": [{"id": 1}, {"id": 2}],
    "summaries": [{"id": 1}],
    "document_links": list(range(50)),
    "annotations": [f"graph:edge:{i}" for i in range(30)] + ["other:x"],
}


def test_fixture_labels():
    assert FIXTURE_KEEP["label"] == "FIXTURE" and FIXTURE_KEEP["locked"] is False
    assert FIXTURE_DROP["label"] == "FIXTURE" and FIXTURE_DROP["locked"] is False
    assert FIXTURE_KEEP["tables"] == ("verbatim", "summaries")
    assert "graph:*" in FIXTURE_DROP["classes"]
    assert "document_links" in FIXTURE_DROP["classes"]


def test_plan_keeps_content_drops_fanout():
    plan = plan_extract(INV)
    assert plan.keep == ["verbatim", "summaries"]
    sig = plan.as_signal()
    classes = {d["class"]: d["count"] for d in sig["drop"]}
    assert classes["document_links"] == 50
    assert classes["graph:*"] == 30
    assert classes["annotations-graph-fanout"] == 30
    for row in sig["drop"]:
        assert "count" in row and "class" in row


def test_refuse_locked_label():
    bad = dict(FIXTURE_KEEP)
    bad["label"] = "LOCKED"
    bad["locked"] = True
    try:
        plan_extract(INV, keep=bad)
    except LiteClosed:
        return
    raise AssertionError("LOCKED keep-list must refuse while H3 is open")


def test_refuse_live_dst():
    plan = plan_extract(INV)
    try:
        apply_extract(plan, INV, r"D:\BEACON_HQ\PROJECTS\00_ACTIVE\UAIMC")
    except LiteClosed as exc:
        assert "live" in str(exc).lower()
        return
    raise AssertionError("live AA9 dst must refuse")


def test_apply_does_not_copy_document_links():
    plan = plan_extract(INV)
    out = apply_extract(plan, INV, "/workspace/praxis/uaimc-lite-20260903/fixtures/lite")
    assert set(out["kept"]) == {"verbatim", "summaries"}
    assert "document_links" not in out["kept"]
    assert "annotations" not in out["kept"]


def test_order_lock():
    try:
        plan_extract(INV, caps_ok=False)
    except LiteClosed:
        return
    raise AssertionError("extract before mouth-caps must fail-closed")


def test_extract_returns_keep_drop_counts_by_class():
    result = extract(INV)
    assert result.label == "FIXTURE"
    assert result.keep_counts == {"verbatim": 2, "summaries": 1}
    assert result.drop_counts["document_links"] == 50
    assert result.drop_counts["graph:*"] == 30
    assert "document_links" not in result.kept
    assert "annotations" not in result.kept
    assert verify_enumerable(result) is True
    sig = result.as_signal()
    assert sig["keep_counts"]["verbatim"] == 2
    assert sig["drop_counts"]["document_links"] == 50


def test_refuse_unknown_table_copy_without_fixture_policy():
    try:
        extract(INV, copy_tables=["kg_nodes"])
    except LiteClosed as exc:
        assert "fixture policy" in str(exc).lower() or "unknown" in str(exc).lower()
        return
    raise AssertionError("unknown table copy must fail-closed without fixture policy")


def test_refuse_copy_drop_class_table():
    try:
        extract(INV, copy_tables=["document_links"])
    except LiteClosed:
        return
    raise AssertionError("document_links copy must fail-closed under FIXTURE drop policy")


class SuiteTest(unittest.TestCase):
    def test_all(self):
        test_fixture_labels()
        test_plan_keeps_content_drops_fanout()
        test_refuse_locked_label()
        test_refuse_live_dst()
        test_apply_does_not_copy_document_links()
        test_order_lock()
        test_extract_returns_keep_drop_counts_by_class()
        test_refuse_unknown_table_copy_without_fixture_policy()
        test_refuse_copy_drop_class_table()


if __name__ == "__main__":
    test_fixture_labels()
    test_plan_keeps_content_drops_fanout()
    test_refuse_locked_label()
    test_refuse_live_dst()
    test_apply_does_not_copy_document_links()
    test_order_lock()
    test_extract_returns_keep_drop_counts_by_class()
    test_refuse_unknown_table_copy_without_fixture_policy()
    test_refuse_copy_drop_class_table()
    print("LITE_EXTRACT_OK")
