from dataclasses import dataclass

from models.activity_report import ActivityReport
from models.returns_report import ReturnsReport
from models.edge_report import EdgeReport
from models.equity_report import EquityReport
from models.drawdown_report import DrawdownReport
from models.monthly_report import MonthlyReport
from models.weekly_report import WeeklyReport
from models.weekday_report import WeekdayReport
from models.duration_report import DurationReport
from models.streak_report import StreakReport


@dataclass
class PerformanceReport:

    activity: ActivityReport
    returns: ReturnsReport
    edge: EdgeReport
    equity: EquityReport
    drawdown: DrawdownReport

    monthly: MonthlyReport | None = None
    weekly: WeeklyReport | None = None
    weekday: WeekdayReport | None = None
    duration: DurationReport | None = None
    streak: StreakReport | None = None