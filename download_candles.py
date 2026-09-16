"""Download or restore ETHUSDT candle data.

This file is intentionally a safe placeholder: the authoritative verified archive
for ETHUSDT candles is not present in the current repository snapshot.
"""

from __future__ import annotations

from pathlib import Path


def download_ethusdt_candles(output_dir: str | Path | None = None) -> list[Path]:
    """Placeholder restoration hook.

    The canonical verified data set is not available in this environment, so this
    function raises an explicit error rather than fabricating candle files.
    """
    target_dir = Path(output_dir) if output_dir is not None else Path("data")
    target_dir.mkdir(parents=True, exist_ok=True)
    raise RuntimeError(
        "No canonical verified ETHUSDT candle archive is available in this repo snapshot. "
        "Restore the authoritative archive before downloading or generating data files."
    )
