from collections import defaultdict

from models.calendar_report import CalendarReport, CalendarStats


class CalendarAnalyzer:

    def __init__(self, starting_capital=1_000_000):
        self.starting_capital = starting_capital

    def analyze(self, trades):

        daily_data = defaultdict(list)

        for trade in trades:
            daily_data[trade.entry_date].append(trade)

        reports = []

        cumulative_equity = self.starting_capital

        for trading_date in sorted(daily_data.keys()):

            day_trades = daily_data[trading_date]

            winners = [t for t in day_trades if t.total_pnl > 0]
            losers = [t for t in day_trades if t.total_pnl < 0]

            gross_profit = sum(t.total_pnl for t in winners)
            gross_loss = abs(sum(t.total_pnl for t in losers))
            net_profit = sum(t.total_pnl for t in day_trades)

            cumulative_equity += net_profit

            total = len(day_trades)

            reports.append(
                CalendarStats(
                    trading_date=str(trading_date),
                    total_trades=total,
                    winning_trades=len(winners),
                    losing_trades=len(losers),
                    gross_profit=round(gross_profit, 2),
                    gross_loss=round(gross_loss, 2),
                    net_profit=round(net_profit, 2),
                    average_pnl=round(net_profit / total, 2) if total else 0,
                    best_trade=round(
                        max((t.total_pnl for t in day_trades), default=0),
                        2
                    ),
                    worst_trade=round(
                        min((t.total_pnl for t in day_trades), default=0),
                        2
                    ),
                    win_rate=round(len(winners) / total * 100, 2)
                    if total else 0,
                    profit_factor=round(gross_profit / gross_loss, 2)
                    if gross_loss > 0 else 0,
                    cumulative_equity=round(cumulative_equity, 2)
                )
            )

        return CalendarReport(reports)