from analytics.equity import EquityAnalyzer
from models.drawdown_report import DrawdownReport


class DrawdownAnalyzer:

    def __init__(self, starting_capital=1_000_000):
        self.starting_capital = starting_capital

    def analyze(self, trades):

        equity = EquityAnalyzer(
            self.starting_capital
        ).analyze(trades)

        drawdown_curve = []

        peak = equity.equity_curve[0]

        max_drawdown = 0

        current_drawdown = 0

        for value in equity.equity_curve:

            if value > peak:
                peak = value

            drawdown = peak - value

            drawdown_curve.append(round(drawdown, 2))

            if drawdown > max_drawdown:
                max_drawdown = drawdown

            current_drawdown = drawdown

        max_drawdown_percent = (
            max_drawdown / peak * 100
            if peak else 0
        )

        current_drawdown_percent = (
            current_drawdown / peak * 100
            if peak else 0
        )

        return DrawdownReport(

            max_drawdown_rupees=round(
                max_drawdown, 2
            ),

            max_drawdown_percent=round(
                max_drawdown_percent, 2
            ),

            current_drawdown_rupees=round(
                current_drawdown, 2
            ),

            current_drawdown_percent=round(
                current_drawdown_percent, 2
            ),

            drawdown_curve=drawdown_curve
        )