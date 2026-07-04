from dataclasses import dataclass


@dataclass
class ReturnsReport:
    """
    Return Statistics
    """

    gross_profit: float

    gross_loss: float

    net_profit: float

    average_winning_trade: float

    average_losing_trade: float

    average_pnl_per_trade: float

    best_trade: float

    worst_trade: float