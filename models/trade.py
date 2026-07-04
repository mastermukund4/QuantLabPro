from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date, time


@dataclass
class TradeLeg:
    leg_no: int
    buy_sell: str
    option_type: str
    strike: float
    quantity: int
    entry_price: float
    exit_price: float
    pnl: float


@dataclass
class Trade:
    trade_id: str

    strategy: str

    symbol: str

    expiry_type: str

    entry_date: date
    entry_time: time

    exit_date: date
    exit_time: time

    total_pnl: float

    vix: Optional[float] = None

    legs: List[TradeLeg] = field(default_factory=list)