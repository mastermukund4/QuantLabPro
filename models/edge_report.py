from dataclasses import dataclass


@dataclass
class EdgeReport:
    """
    Strategy Edge Statistics
    """

    payoff_ratio: float

    profit_factor: float

    expectancy_r: float