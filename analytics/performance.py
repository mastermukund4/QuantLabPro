from analytics.activity import ActivityAnalyzer
from analytics.returns import ReturnsAnalyzer
from analytics.edge import EdgeAnalyzer

from models.performance_report import PerformanceReport


class PerformanceAnalyzer:
    """
    Combines all analytics modules into one report.
    """

    def analyze(self, trades):

        activity = ActivityAnalyzer().analyze(trades)

        returns = ReturnsAnalyzer().analyze(trades)

        edge = EdgeAnalyzer().analyze(trades)

        return PerformanceReport(

            # Trading Activity
            total_trades=activity.total_trades,
            winning_trades=activity.winning_trades,
            losing_trades=activity.losing_trades,
            breakeven_trades=activity.breakeven_trades,

            win_rate=activity.win_rate,
            loss_rate=activity.loss_rate,

            # Returns
            gross_profit=returns.gross_profit,
            gross_loss=returns.gross_loss,
            net_profit=returns.net_profit,

            average_winning_trade=returns.average_winning_trade,
            average_losing_trade=returns.average_losing_trade,
            average_pnl_per_trade=returns.average_pnl_per_trade,

            best_trade=returns.best_trade,
            worst_trade=returns.worst_trade,

            # Strategy Edge
            payoff_ratio=edge.payoff_ratio,
            profit_factor=edge.profit_factor,
            expectancy_r=edge.expectancy_r
        )