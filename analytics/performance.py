from analytics.core.core_analytics import CoreAnalytics
from analytics.strategy.strategy_analytics import StrategyAnalytics

from models.performance_report import PerformanceReport


class PerformanceAnalyzer:

    def analyze(self, trades):

        core = CoreAnalytics().analyze(trades)

        StrategyAnalytics().analyze(trades)

        return PerformanceReport(
            activity=core["activity"],
            returns=core["returns"],
            edge=core["edge"],
            equity=core["equity"],
            drawdown=core["drawdown"],
            monthly=core["monthly"],
            weekly=core["weekly"],
            weekday=core["weekday"],
            duration=core["duration"],
            streak=core["streak"],
            calendar=core["calendar"],
            risk=core["risk"],
        )