from dataclasses import dataclass


@dataclass
class PerformanceReport:

    # Basic
    total_trades: int
    winning_trades: int
    losing_trades: int
    breakeven_trades: int

    # Returns
    gross_profit: float
    gross_loss: float
    net_profit: float

    # Win/Loss
    win_rate: float
    loss_rate: float

    average_winner: float
    average_loser: float

    largest_winner: float
    largest_loser: float

    payoff_ratio: float
    profit_factor: float

    expectancy_rupees: float
    expectancy_r: float