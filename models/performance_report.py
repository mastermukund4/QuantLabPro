from dataclasses import dataclass


@dataclass
class PerformanceReport:

    # Trading Activity
    total_trades: int
    winning_trades: int
    losing_trades: int
    breakeven_trades: int

    win_rate: float
    loss_rate: float

    # Returns
    gross_profit: float
    gross_loss: float
    net_profit: float

    average_winning_trade: float
    average_losing_trade: float
    average_pnl_per_trade: float

    best_trade: float
    worst_trade: float

    # Strategy Edge
    payoff_ratio: float
    profit_factor: float
    expectancy_r: float