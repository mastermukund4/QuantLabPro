from collections import defaultdict
from datetime import datetime, timedelta

from models.duration_report import DurationReport, DurationStats


class DurationAnalyzer:
    """
    Calculates duration-wise trading performance.
    """

    def analyze(self, trades):

        duration_data = defaultdict(list)

        for trade in trades:

            bucket = self.get_duration_bucket(trade)

            duration_data[bucket].append(trade)

        reports = []

        for bucket in self.bucket_order():

            bucket_trades = duration_data.get(bucket, [])

            winners = [t for t in bucket_trades if t.total_pnl > 0]
            losers = [t for t in bucket_trades if t.total_pnl < 0]

            gross_profit = sum(t.total_pnl for t in winners)
            gross_loss = abs(sum(t.total_pnl for t in losers))
            net_profit = sum(t.total_pnl for t in bucket_trades)

            total = len(bucket_trades)

            reports.append(
                DurationStats(
                    bucket=bucket,
                    total_trades=total,
                    winning_trades=len(winners),
                    losing_trades=len(losers),
                    gross_profit=gross_profit,
                    gross_loss=gross_loss,
                    net_profit=net_profit,
                    average_pnl=(net_profit / total if total else 0),
                    best_trade=max((t.total_pnl for t in bucket_trades), default=0),
                    worst_trade=min((t.total_pnl for t in bucket_trades), default=0),
                    win_rate=(len(winners) / total * 100 if total else 0),
                    profit_factor=(gross_profit / gross_loss if gross_loss > 0 else 0)
                )
            )

        return DurationReport(reports)

    def get_duration_bucket(self, trade):

        entry_dt = datetime.combine(trade.entry_date, trade.entry_time)
        exit_dt = datetime.combine(trade.exit_date, trade.exit_time)

        duration = exit_dt - entry_dt

        if duration < timedelta(days=0):
            return "Overnight / Multi-day"

        minutes = duration.total_seconds() / 60

        if trade.entry_date != trade.exit_date:
            return "Overnight / Multi-day"

        if minutes <= 15:
            return "0-15 min"

        if minutes <= 30:
            return "15-30 min"

        if minutes <= 60:
            return "30-60 min"

        if minutes <= 120:
            return "1-2 hrs"

        if minutes <= 240:
            return "2-4 hrs"

        if minutes <= 360:
            return "4-6 hrs"

        return "6+ hrs Same Day"

    def bucket_order(self):

        return [
            "0-15 min",
            "15-30 min",
            "30-60 min",
            "1-2 hrs",
            "2-4 hrs",
            "4-6 hrs",
            "6+ hrs Same Day",
            "Overnight / Multi-day"
        ]