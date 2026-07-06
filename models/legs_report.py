from dataclasses import dataclass


@dataclass
class LegGroupStats:

    group_name: str

    total_legs: int

    winning_legs: int

    losing_legs: int

    gross_profit: float

    gross_loss: float

    net_profit: float

    average_pnl: float

    best_leg: float

    worst_leg: float

    win_rate: float

    profit_factor: float


@dataclass
class LegsReport:

    option_type_stats: list[LegGroupStats]

    buy_sell_stats: list[LegGroupStats]