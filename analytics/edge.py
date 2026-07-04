from models.edge_report import EdgeReport


class EdgeAnalyzer:

    def analyze(self, trades):

        winners = [t.total_pnl for t in trades if t.total_pnl > 0]
        losers = [t.total_pnl for t in trades if t.total_pnl < 0]

        gross_profit = sum(winners)
        gross_loss = abs(sum(losers))

        avg_winner = (
            gross_profit / len(winners)
            if winners else 0
        )

        avg_loser = (
            gross_loss / len(losers)
            if losers else 0
        )

        win_rate = (
            len(winners) / len(trades)
            if trades else 0
        )

        loss_rate = (
            len(losers) / len(trades)
            if trades else 0
        )

        payoff_ratio = (
            avg_winner / avg_loser
            if avg_loser else 0
        )

        profit_factor = (
            gross_profit / gross_loss
            if gross_loss else 0
        )

        expectancy_r = (
            (win_rate * payoff_ratio) - loss_rate
        )

        return EdgeReport(

            payoff_ratio=round(payoff_ratio, 2),

            profit_factor=round(profit_factor, 2),

            expectancy_r=round(expectancy_r, 3)
        )