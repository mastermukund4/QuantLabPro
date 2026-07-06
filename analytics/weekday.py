from collections import defaultdict

from models.weekday_report import WeekdayReport, WeekdayStats


class WeekdayAnalyzer:
    """
    Calculates weekday-wise trading performance.
    """

    WEEKDAY_ORDER = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]

    def analyze(self, trades):

        weekday_data = defaultdict(list)

        # Group trades by weekday
        for trade in trades:

            weekday = trade.entry_date.strftime("%A")

            weekday_data[weekday].append(trade)

        reports = []

        for weekday in self.WEEKDAY_ORDER:

            week_trades = weekday_data.get(weekday, [])

            winners = [t for t in week_trades if t.total_pnl > 0]

            losers = [t for t in week_trades if t.total_pnl < 0]

            gross_profit = sum(t.total_pnl for t in winners)

            gross_loss = abs(sum(t.total_pnl for t in losers))

            net_profit = sum(t.total_pnl for t in week_trades)

            total = len(week_trades)

            reports.append(

                WeekdayStats(

                    weekday=weekday,

                    total_trades=total,

                    winning_trades=len(winners),

                    losing_trades=len(losers),

                    gross_profit=gross_profit,

                    gross_loss=gross_loss,

                    net_profit=net_profit,

                    average_pnl=(
                        net_profit / total
                        if total else 0
                    ),

                    best_trade=max(
                        (t.total_pnl for t in week_trades),
                        default=0
                    ),

                    worst_trade=min(
                        (t.total_pnl for t in week_trades),
                        default=0
                    ),

                    win_rate=(
                        len(winners) / total * 100
                        if total else 0
                    ),

                    profit_factor=(
                        gross_profit / gross_loss
                        if gross_loss > 0
                        else 0
                    )

                )

            )

        return WeekdayReport(reports)