from dataclasses import dataclass


@dataclass
class WeeklyStats:

    week: str

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
class WeeklyReport:

    weeks: list[WeeklyStats]