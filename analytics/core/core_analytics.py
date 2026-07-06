from analytics.activity import ActivityAnalyzer
from analytics.returns import ReturnsAnalyzer
from analytics.edge import EdgeAnalyzer
from analytics.equity import EquityAnalyzer
from analytics.drawdown import DrawdownAnalyzer
from analytics.monthly import MonthlyAnalyzer
from analytics.weekly import WeeklyAnalyzer
from analytics.weekday import WeekdayAnalyzer
from analytics.duration import DurationAnalyzer
from analytics.streak import StreakAnalyzer
from analytics.calendar import CalendarAnalyzer
from analytics.risk.risk import RiskAnalyzer


class CoreAnalytics:

    def analyze(self, trades):

        return {
            "activity": ActivityAnalyzer().analyze(trades),
            "returns": ReturnsAnalyzer().analyze(trades),
            "edge": EdgeAnalyzer().analyze(trades),
            "equity": EquityAnalyzer().analyze(trades),
            "drawdown": DrawdownAnalyzer().analyze(trades),
            "monthly": MonthlyAnalyzer().analyze(trades),
            "weekly": WeeklyAnalyzer().analyze(trades),
            "weekday": WeekdayAnalyzer().analyze(trades),
            "duration": DurationAnalyzer().analyze(trades),
            "streak": StreakAnalyzer().analyze(trades),
            "calendar": CalendarAnalyzer().analyze(trades),
            "risk": RiskAnalyzer().analyze(trades),
        }