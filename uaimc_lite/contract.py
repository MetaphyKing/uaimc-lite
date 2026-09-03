"""LOCKED Tier A path registry (Scout correction). Sampler routes are NON-CONTRACT."""

from __future__ import annotations

TIER_A = (
    ("GET", "/health"),
    ("GET", "/query"),
    ("GET", "/recent"),
    ("POST", "/ingest"),
)

OUT_OF_A = (
    ("GET", "/context"),
    ("GET", "/backup"),
    ("GET", "/ws"),
)

# Sampler polls these; Spec choice: sampler-not-a-contract-caller until H6 ruled.
NON_CONTRACT_SAMPLER = (
    ("GET", "/ready"),
    ("GET", "/stats"),
)


def is_tier_a(method: str, path: str) -> bool:
    return (method.upper(), path) in TIER_A
