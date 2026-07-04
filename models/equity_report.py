from dataclasses import dataclass


@dataclass
class EquityReport:
    """
    Equity Curve Report
    """

    starting_capital: float
    ending_capital: float

    trade_numbers: list
    cumulative_pnl: list
    equity_curve: list