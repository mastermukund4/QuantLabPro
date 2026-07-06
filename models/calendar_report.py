from dataclasses import dataclass


@dataclass
class CalendarStats:

    trading_date: str

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

    cumulative_equity: float


@dataclass
class CalendarReport:

    days: list[CalendarStats]