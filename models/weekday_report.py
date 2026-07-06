from dataclasses import dataclass


@dataclass
class WeekdayStats:

    weekday: str

    total_trades: int

    winning_trades: int

    losing_trades: int

    gross_profit: float

    gross_loss: float

    net_profit: float

    average_pnl: float

    best_trade: float

    worst_trade: float

    win_rate: float

    profit_factor: float


@dataclass
class WeekdayReport:

    weekdays: list[WeekdayStats]