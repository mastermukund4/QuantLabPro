from collections import defaultdict

from models.monthly_report import MonthlyReport, MonthlyStats


class MonthlyAnalyzer:

    def analyze(self, trades):

        monthly_data = defaultdict(list)

        for trade in trades:

            month = trade.entry_date.strftime("%Y-%m")

            monthly_data[month].append(trade)

        reports = []

        for month in sorted(monthly_data.keys()):

            month_trades = monthly_data[month]

            winners = [t for t in month_trades if t.total_pnl > 0]
            losers = [t for t in month_trades if t.total_pnl < 0]

            gross_profit = sum(t.total_pnl for t in winners)
            gross_loss = abs(sum(t.total_pnl for t in losers))
            net_profit = sum(t.total_pnl for t in month_trades)

            total = len(month_trades)

            reports.append(

                MonthlyStats(

                    month=month,

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
                        (t.total_pnl for t in month_trades),
                        default=0
                    ),

                    worst_trade=min(
                        (t.total_pnl for t in month_trades),
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

        return MonthlyReport(reports)