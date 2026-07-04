from models.activity_report import ActivityReport


class ActivityAnalyzer:

    def analyze(self, trades):

        total = len(trades)

        winners = len(
            [t for t in trades if t.total_pnl > 0]
        )

        losers = len(
            [t for t in trades if t.total_pnl < 0]
        )

        breakeven = len(
            [t for t in trades if t.total_pnl == 0]
        )

        return ActivityReport(

            total_trades=total,

            winning_trades=winners,

            losing_trades=losers,

            breakeven_trades=breakeven,

            win_rate=round(
                winners / total * 100, 2
            ) if total else 0,

            loss_rate=round(
                losers / total * 100, 2
            ) if total else 0,

            breakeven_rate=round(
                breakeven / total * 100, 2
            ) if total else 0
        )