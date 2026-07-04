from models.equity_report import EquityReport


class EquityAnalyzer:

    def __init__(self, starting_capital=1_000_000):
        self.starting_capital = starting_capital

    def analyze(self, trades):

        equity = self.starting_capital
        cumulative = 0

        trade_numbers = []
        cumulative_pnl = []
        equity_curve = []

        for i, trade in enumerate(trades, start=1):

            cumulative += trade.total_pnl
            equity += trade.total_pnl

            trade_numbers.append(i)
            cumulative_pnl.append(round(cumulative, 2))
            equity_curve.append(round(equity, 2))

        return EquityReport(
            starting_capital=self.starting_capital,
            ending_capital=round(equity, 2),
            trade_numbers=trade_numbers,
            cumulative_pnl=cumulative_pnl,
            equity_curve=equity_curve
        )