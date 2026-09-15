# Strategy Spec — ETHUSDT Futures (Code-ready)

Project goal
- Build a rule-based ETHUSDT futures trading bot using multi-timeframe Smart Money Concepts (SMC) logic. Backtest thoroughly before any live/testnet deployment.

Exact strategy rules

Bias (4H)
- 4H uptrend confirmed = long only
- 4H downtrend confirmed = short only
- Trend unclear / ranging = no trade

Liquidity Sweep
- Price wicks beyond previous swing high/low
- Candle closes back inside the range
- This confirms a liquidity grab

Entry Trigger (1m)
- After sweep, wait for 1m CHOCH (Change of Character)
- Wait for pullback to complete
- Enter on pullback confirmation in bias direction

Stop Loss
- Placed behind the sweep wick (beyond the liquidity zone)

Take Profit
- Next liquidity pool, or
- Higher timeframe key level/target

Phase plan
- Phase 1: Project foundation (repo, folders, environment)
- Phase 2: Strategy spec finalized into code-ready rules
- Phase 3: Data collection + rule engine + backtest
- Phase 4: Paper/testnet trading
- Phase 5: Live trading (only after consistent backtest/testnet results)

Current status
- Phase 1 in progress. Repo created. Environment setup pending confirmation.

What to do next (short-term)
- Finish Termux environment setup
- Confirm folder structure in repo
- Push initial commit
- Begin Phase 2: strategy spec in code-ready pseudocode

Code-ready pseudocode (Python-like) — structure for implementation

```python
# High-level objects
class Bar:
    time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

class Swing:
    type: 'high' or 'low'
    price: float
    index: int

# Utilities
def detect_trend_4h(candles_4h):
    """Return 'up', 'down', or 'range' based on swing structure and moving averages."""
    # Example: use successive higher highs + higher lows for 'up', opposite for 'down'
    # Or use SMA/EMA slope + swing count threshold
    pass

def find_last_swings(tf_candles, lookback=50):
    """Identify swing highs/lows to be used for liquidity sweep detection."""
    pass

def is_liquidity_sweep(candles, swing):
    """Return True if price wick pierced the swing then closed back inside the range."""
    # 1. price made wick beyond swing.price (high> swing_high or low < swing_low)
    # 2. same candle or a following candle closed back inside the prior swing range
    pass

def detect_choch_1m(candles_1m):
    """Detect Change Of Character on 1m timeframe after sweep.
    Return event index and direction ('bull' or 'bear') if found, else None.
    """
    pass

def pullback_complete(candles_1m, choch_index, direction):
    """Detect pullback completion.
    Rules: look for structure/confirmation (e.g., bullish engulf, momentum candle, or higher low).
    """
    pass

# Entry decision
def evaluate_entry(candles_1m, sweep_info, bias):
    # 1. Confirm bias matches direction (long only if bias is 'up')
    # 2. Confirm sweep detected and choch occurred
    # 3. Wait for pullback completion signal
    # 4. Place entry order at confirmation candle open/close depending on execution method
    # 5. SL behind sweep wick, TP at next liquidity pool or HTF target
    pass

# Backtest loop outline
for t in range(start_index, end_index):
    update candle windows for 4h, 1h, 15m, 1m
    bias = detect_trend_4h(candles_4h)
    swings_15m = find_last_swings(candles_15m)
    for swing in swings_15m:
        if is_liquidity_sweep(candles_15m, swing):
            wait for choch on 1m
            if detect_choch_1m:
                if pullback_complete and bias allows trade:
                    simulate entry, sl, tp
                    log trade result

Backtest metrics to record
- Net P/L, total trades, win rate, average R:R, max drawdown, expectancy
- Per-strategy filters (only long/short counts, sweep success rate, choch success rate)

Data requirements
- Historical OHLCV for 4H, 1H, 15m, 1m (aligned timezones)
- Prefer exchange futures (Binance Futures) normalized data

Implementation notes
- Keep logic modular: detectors (trend, swings, sweep, choch, pullback) independent and testable
- Add unit tests for each detector using synthetic candles
- Use vectorized/optimized operations where possible, but correctness over speed initially
- Log every candidate sweep and CHOCH event for analysis

Next actions I can take now
1) Create docs/STRATEGY_SPEC.md in the repo (this file). (doing it now)
2) Create folder skeleton: data/, engine/, backtest/, scripts/, docs/ and add README or .gitkeep files
3) Convert pseudocode to a starter Python backtest template under backtest/
4) Create issues from phase checklist

If you want, I will create the docs/STRATEGY_SPEC.md file in the repo and optionally create the folder skeleton next.
```
