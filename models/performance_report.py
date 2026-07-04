from dataclasses import dataclass

from models.activity_report import ActivityReport
from models.returns_report import ReturnsReport
from models.edge_report import EdgeReport
from models.equity_report import EquityReport
from models.drawdown_report import DrawdownReport


@dataclass
class PerformanceReport:
    """
    Master Performance Report
    """

    activity: ActivityReport

    returns: ReturnsReport

    edge: EdgeReport

    equity: EquityReport

    drawdown: DrawdownReport