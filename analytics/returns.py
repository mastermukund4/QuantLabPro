from models.returns_report import ReturnsReport


class ReturnsAnalyzer:

    def analyze(self, trades):

        winners = [t.total_pnl for t in trades if t.total_pnl > 0]
        losers = [t.total_pnl for t in trades if t.total_pnl < 0]

        gross_profit = sum(winners)
        gross_loss = abs(sum(losers))
        net_profit = gross_profit - gross_loss

        average_winning_trade = (
            gross_profit / len(winners)
            if winners else 0
        )

        average_losing_trade = (
            gross_loss / len(losers)
            if losers else 0
        )

        average_pnl_per_trade = (
            net_profit / len(trades)
            if trades else 0
        )

        best_trade = max(winners) if winners else 0

        worst_trade = min(losers) if losers else 0

        return ReturnsReport(

            gross_profit=round(gross_profit, 2),

            gross_loss=round(gross_loss, 2),

            net_profit=round(net_profit, 2),

            average_winning_trade=round(
                average_winning_trade, 2
            ),

            average_losing_trade=round(
                average_losing_trade, 2
            ),

            average_pnl_per_trade=round(
                average_pnl_per_trade, 2
            ),

            best_trade=round(best_trade, 2),

            worst_trade=round(worst_trade, 2),
        )