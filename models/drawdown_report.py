from dataclasses import dataclass


@dataclass
class DrawdownReport:
    """
    Drawdown Statistics
    """

    max_drawdown_rupees: float

    max_drawdown_percent: float

    current_drawdown_rupees: float

    current_drawdown_percent: float

    drawdown_curve: list