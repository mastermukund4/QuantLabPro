from collections import defaultdict

from models.weekly_report import WeeklyReport, WeeklyStats


class WeeklyAnalyzer:
    """
    Calculates week-wise trading performance.
    """

    def analyze(self, trades):

        weekly_data = defaultdict(list)

        # Group trades by ISO week
        for trade in trades:

            year, week, _ = trade.entry_date.isocalendar()

            week_key = f"{year}-W{week:02d}"

            weekly_data[week_key].append(trade)

        reports = []

        for week in sorted(weekly_data.keys()):

            week_trades = weekly_data[week]

            winners = [t for t in week_trades if t.total_pnl > 0]

            losers = [t for t in week_trades if t.total_pnl < 0]

            gross_profit = sum(t.total_pnl for t in winners)

            gross_loss = abs(sum(t.total_pnl for t in losers))

            net_profit = sum(t.total_pnl for t in week_trades)

            total = len(week_trades)

            reports.append(

                WeeklyStats(

                    week=week,

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

        return WeeklyReport(reports)