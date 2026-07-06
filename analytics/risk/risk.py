import statistics

from analytics.equity import EquityAnalyzer
from analytics.drawdown import DrawdownAnalyzer
from analytics.risk.sharpe import SharpeCalculator
from analytics.risk.sortino import SortinoCalculator
from analytics.risk.recovery import RecoveryCalculator
from analytics.risk.ulcer import UlcerCalculator
from analytics.risk.calmar import CalmarCalculator
from analytics.risk.var import VarCalculator
from analytics.risk.kelly import KellyCalculator

from models.risk_report import RiskReport


class RiskAnalyzer:

    def analyze(self, trades):

        pnl_values = [
            trade.total_pnl for trade in trades
        ]

        returns = pnl_values

        equity_report = EquityAnalyzer().analyze(trades)

        drawdown_report = DrawdownAnalyzer().analyze(trades)

        net_profit = sum(pnl_values)

        starting_capital = equity_report.starting_capital

        total_return_percent = (
            net_profit / starting_capital * 100
            if starting_capital else 0
        )

        standard_deviation = (
            statistics.stdev(pnl_values)
            if len(pnl_values) > 1 else 0
        )

        downside_values = [
            pnl for pnl in pnl_values if pnl < 0
        ]

        downside_deviation = (
            statistics.stdev(downside_values)
            if len(downside_values) > 1
            else abs(downside_values[0])
            if downside_values else 0
        )

        winners = [
            pnl for pnl in pnl_values if pnl > 0
        ]

        losers = [
            pnl for pnl in pnl_values if pnl < 0
        ]

        win_rate = (
            len(winners) / len(pnl_values) * 100
            if pnl_values else 0
        )

        avg_winner = (
            sum(winners) / len(winners)
            if winners else 0
        )

        avg_loser = (
            abs(sum(losers)) / len(losers)
            if losers else 0
        )

        payoff_ratio = (
            avg_winner / avg_loser
            if avg_loser else 0
        )

        kelly_percent = KellyCalculator().calculate(
            win_rate,
            payoff_ratio
        )

        return RiskReport(

            standard_deviation=round(
                standard_deviation,
                2
            ),

            downside_deviation=round(
                downside_deviation,
                2
            ),

            sharpe_ratio=SharpeCalculator().calculate(
                returns
            ),

            sortino_ratio=SortinoCalculator().calculate(
                returns
            ),

            calmar_ratio=CalmarCalculator().calculate(
                total_return_percent,
                drawdown_report.max_drawdown_percent
            ),

            ulcer_index=UlcerCalculator().calculate(
                drawdown_report.drawdown_curve,
                equity_report.equity_curve
            ),

            recovery_factor=RecoveryCalculator().calculate(
                net_profit,
                drawdown_report.max_drawdown_rupees
            ),

            value_at_risk_95=VarCalculator().calculate_var_95(
                pnl_values
            ),

            conditional_var_95=VarCalculator().calculate_cvar_95(
                pnl_values
            ),

            kelly_percent=kelly_percent,

            half_kelly_percent=round(
                kelly_percent / 2,
                2
            )
        )