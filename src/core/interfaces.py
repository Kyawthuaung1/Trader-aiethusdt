"""Canonical interfaces for the ETHUSDT trading strategy package."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal

Timeframe = Literal["1m", "15m", "1h", "4h"]
TrendBias = Literal["up", "down", "range"]
Direction = Literal["bull", "bear"]
SwingType = Literal["high", "low"]


@dataclass(slots=True)
class Bar:
    """Single OHLCV candle for any timeframe."""

    time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass(slots=True)
class Swing:
    """Swing point used to identify liquidity zones."""

    type: SwingType
    price: float
    index: int
    timestamp: datetime | None = None


@dataclass(slots=True)
class SweepEvent:
    """Candidate liquidity sweep event around a swing high/low."""

    swing_index: int
    swing_type: SwingType
    swing_price: float
    sweep_index: int
    wick_high: float | None = None
    wick_low: float | None = None
    close_inside_range: bool = False


@dataclass(slots=True)
class CHOCHEvent:
    """Change-of-character event that follows a sweep."""

    index: int
    direction: Direction
    confidence: float = 0.0


@dataclass(slots=True)
class PullbackSignal:
    """Pullback completion signal used before entry."""

    start_index: int
    end_index: int
    direction: Direction
    confirmed: bool = False


@dataclass(slots=True)
class StrategyConfig:
    """Minimal configuration contract for the strategy rules."""

    bias_timeframe: Timeframe = "4h"
    entry_timeframe: Timeframe = "1m"
    sweep_lookback: int = 50
    min_confirmation_bars: int = 1
    sl_buffer: float = 0.0
    tp_buffer: float = 0.0
