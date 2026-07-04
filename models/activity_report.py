from dataclasses import dataclass


@dataclass
class ActivityReport:
    """
    Trading Activity Statistics
    """

    total_trades: int

    winning_trades: int

    losing_trades: int

    breakeven_trades: int

    win_rate: float

    loss_rate: float

    breakeven_rate: float