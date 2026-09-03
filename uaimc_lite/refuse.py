"""Explicit refuse helpers. Never hang. Never lie.

DEDUP SENTINEL (LOCKED ①): POST /ingest summary_id:-2 is SUCCESS.
Callers must not retry. Full HTTP envelope is HOLE H4. Bible Test 10.2 owns the harness.
"""

from __future__ import annotations

DEDUP_SENTINEL = -2


def is_dedup_success(payload):
    if not isinstance(payload, dict):
        return False
    sid = payload.get("summary_id")
    try:
        return int(sid) == DEDUP_SENTINEL
    except (TypeError, ValueError):
        return False


def should_retry(payload):
    """False on -2. Do not treat sentinel as 5xx."""
    if is_dedup_success(payload):
        return False
    return True


def refuse_document(reason, class_name="refuse"):
    return {"action": "refuse", "class": class_name, "reason": reason, "hang": False, "lie": False}


def assert_dedup_sentinel_not_retryable(payload=None):
    """Assert summary_id:-2 is SUCCESS and must NOT be treated as retryable failure."""
    payload = {"summary_id": DEDUP_SENTINEL} if payload is None else payload
    if not is_dedup_success(payload):
        raise AssertionError("summary_id:-2 must be treated as SUCCESS (DEDUP SENTINEL)")
    if should_retry(payload):
        raise AssertionError("summary_id:-2 must NOT be treated as retryable failure")

