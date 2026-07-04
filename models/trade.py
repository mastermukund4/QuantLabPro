from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TradeLeg:
    leg_no: int
    buy_sell: str
    option_type: str
    strike: float
    qty: int
    entry_price: float
    exit_price: float


@dataclass
class Trade:
    trade_id: str

    strategy: str

    symbol: str

    expiry_type: str

    entry_date: str
    entry_time: str

    exit_date: str
    exit_time: str

    pnl: float

    vix: Optional[float] = None

    legs: List[TradeLeg] = field(default_factory=list)