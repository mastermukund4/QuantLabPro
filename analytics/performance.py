from analytics.activity import ActivityAnalyzer
from analytics.returns import ReturnsAnalyzer
from analytics.edge import EdgeAnalyzer
from analytics.equity import EquityAnalyzer
from analytics.drawdown import DrawdownAnalyzer
from analytics.monthly import MonthlyAnalyzer
from analytics.weekly import WeeklyAnalyzer

from models.performance_report import PerformanceReport


class PerformanceAnalyzer:

    def analyze(self, trades):

        activity = ActivityAnalyzer().analyze(trades)

        returns = ReturnsAnalyzer().analyze(trades)

        edge = EdgeAnalyzer().analyze(trades)

        equity = EquityAnalyzer().analyze(trades)

        drawdown = DrawdownAnalyzer().analyze(trades)

        monthly = MonthlyAnalyzer().analyze(trades)

        weekly = WeeklyAnalyzer().analyze(trades)

        return PerformanceReport(

            activity=activity,

            returns=returns,

            edge=edge,

            equity=equity,

            drawdown=drawdown,

            monthly=monthly,

            weekly=weekly
        )