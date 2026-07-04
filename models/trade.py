from dataclasses import dataclass
from typing import Optional


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

    number_of_legs: int = 0