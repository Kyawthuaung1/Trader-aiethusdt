"""Data access helpers for ETHUSDT candles.

This repository snapshot does not include the canonical verified candle archive.
The helpers below are intentionally minimal and do not claim any validation.
"""

from __future__ import annotations

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


def resolve_data_dir() -> Path:
    """Return the configured data directory for ETHUSDT candle files."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def list_ethusdt_csvs() -> list[Path]:
    """Return verified CSVs if they are later restored from the canonical archive."""
    return sorted(resolve_data_dir().glob("*ETHUSDT*.csv"))
