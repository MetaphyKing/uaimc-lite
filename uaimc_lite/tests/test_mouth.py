#!/usr/bin/env python3
"""Stage 9 mouth-caps tests. FIXTURE caps only. H2 still open."""

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from uaimc_lite.mouth import FIXTURE_CAPS, LiteClosed, apply_caps, require_caps


def test_fixture_label():
    assert FIXTURE_CAPS["label"] == "FIXTURE"
    assert FIXTURE_CAPS["locked"] is False
    require_caps(FIXTURE_CAPS)


def test_production_missing_caps_fail_closed():
    try:
        require_caps(None)
    except LiteClosed as exc:
        assert "H2" in str(exc)
        return
    raise AssertionError("missing caps must fail-closed")


def test_locked_label_refused():
    bad = dict(FIXTURE_CAPS)
    bad["label"] = "LOCKED"
    bad["locked"] = True
    try:
        require_caps(bad)
    except LiteClosed:
        return
    raise AssertionError("LOCKED-labeled caps must refuse while H2 is open")


def test_admit_under_fixture_ceiling():
    event = {"annotations": ["graph:tag:a", "graph:edge:b"]}
    d = apply_caps(event, FIXTURE_CAPS)
    assert d.action == "admit"
    assert d.dropped_count == 0


def test_truncate_over_fixture_ceiling():
    event = {"annotations": [f"graph:edge:{i}" for i in range(20)]}
    d = apply_caps(event, FIXTURE_CAPS)
    assert d.action == "truncate"
    assert d.admitted_count == FIXTURE_CAPS["max_graph_fanout_per_ingest"]
    assert d.dropped_count == 12
    assert d.class_name == "graph:*"
    sig = d.as_signal()
    assert sig["dropped_count"] == 12


def test_refuse_chat_log_dump():
    d = apply_caps({"kind": "chat-log", "text": "chat log dump"}, FIXTURE_CAPS)
    assert d.action == "refuse"
    assert d.class_name == "chat-log-dump"



def test_refuse_over_rate_cap():
    """Fail-closed refuse when over FIXTURE rate_window CapTable slot."""
    d = apply_caps({"annotations": ["graph:tag:a"], "rate_count": 99}, FIXTURE_CAPS)
    assert d.action == "refuse"
    assert d.class_name == "rate-window"


def test_accept_under_hub_cap():
    d = apply_caps({"annotations": ["graph:edge:1"], "hub_links": 1}, FIXTURE_CAPS)
    assert d.action == "admit"
    assert d.dropped_count == 0


def test_dedup_sentinel_stub():
    """DEDUP -2 stub. Full failure-path is Bible Test 10.2. Envelope is H4."""
    from uaimc_lite.refuse import (
        assert_dedup_sentinel_not_retryable,
        is_dedup_success,
        should_retry,
    )
    payload = {"summary_id": -2}
    assert is_dedup_success(payload)
    assert should_retry(payload) is False
    assert_dedup_sentinel_not_retryable(payload)


class SuiteTest(unittest.TestCase):
    def test_all(self):
        test_fixture_label()
        test_production_missing_caps_fail_closed()
        test_locked_label_refused()
        test_admit_under_fixture_ceiling()
        test_truncate_over_fixture_ceiling()
        test_refuse_chat_log_dump()
        test_refuse_over_rate_cap()
        test_accept_under_hub_cap()
        test_dedup_sentinel_stub()


if __name__ == "__main__":
    test_fixture_label()
    test_production_missing_caps_fail_closed()
    test_locked_label_refused()
    test_admit_under_fixture_ceiling()
    test_truncate_over_fixture_ceiling()
    test_refuse_chat_log_dump()
    test_refuse_over_rate_cap()
    test_accept_under_hub_cap()
    test_dedup_sentinel_stub()
    print("MOUTH_CAPS_OK")
