#!/usr/bin/env python3
"""Bible Test 10.2 failure-path: summary_id:-2 is SUCCESS — must not retry."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from uaimc_lite.refuse import DEDUP_SENTINEL, is_dedup_success, should_retry


def test_dedup_is_success():
    assert DEDUP_SENTINEL == -2
    assert is_dedup_success({"summary_id": -2}) is True
    assert is_dedup_success({"summary_id": "-2"}) is True


def test_must_not_retry_on_dedup():
    assert should_retry({"summary_id": -2}) is False
    assert should_retry({"summary_id": -2, "ok": False}) is False


def test_non_dedup_may_retry():
    assert should_retry({"summary_id": 99, "ok": False}) is True


if __name__ == "__main__":
    test_dedup_is_success()
    test_must_not_retry_on_dedup()
    test_non_dedup_may_retry()
    print("FAILURE_PATH_10_2_OK")
