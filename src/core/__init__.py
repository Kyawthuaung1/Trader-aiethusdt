"""Core interfaces used by the ETHUSDT trading strategy code."""

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
    """Single OHLCV candle."""

    time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass(slots=True)
class Swing:
    """Swing high/low reference used for liquidity-zone detection."""

    type: SwingType
    price: float
    index: int
    timestamp: datetime | None = None


@dataclass(slots=True)
class SweepEvent:
    """A liquidity sweep candidate detected around a prior swing."""

    swing_index: int
    swing_type: SwingType
    swing_price: float
    sweep_index: int
    wick_high: float | None = None
    wick_low: float | None = None
    close_inside_range: bool = False


@dataclass(slots=True)
class CHOCHEvent:
    """A 1m change-of-character confirmation after a liquidity sweep."""

    index: int
    direction: Direction
    confidence: float = 0.0


@dataclass(slots=True)
class PullbackSignal:
    """A pullback completion signal confirming continuation."""

    start_index: int
    end_index: int
    direction: Direction
    confirmed: bool = False


@dataclass(slots=True)
class StrategyConfig:
    """Minimal strategy configuration aligned with the project spec."""

    bias_timeframe: Timeframe = "4h"
    entry_timeframe: Timeframe = "1m"
    sweep_lookback: int = 50
    min_confirmation_bars: int = 1
    sl_buffer: float = 0.0
    tp_buffer: float = 0.0
