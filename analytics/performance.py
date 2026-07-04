from models.performance_report import PerformanceReport


class PerformanceAnalyzer:
    """
    Institutional Performance Analytics Engine
    """

    def analyze(self, trades):

        basic = self.calculate_basic_statistics(trades)

        returns = self.calculate_return_statistics(trades)

        winloss = self.calculate_win_loss_statistics(
            basic,
            returns
        )

        expectancy = self.calculate_expectancy_statistics(
            basic,
            returns,
            winloss
        )

        return PerformanceReport(

            # Basic
            total_trades=basic["total_trades"],
            winning_trades=basic["winning_trades"],
            losing_trades=basic["losing_trades"],
            breakeven_trades=basic["breakeven_trades"],

            # Returns
            gross_profit=returns["gross_profit"],
            gross_loss=returns["gross_loss"],
            net_profit=returns["net_profit"],

            # Win/Loss
            win_rate=winloss["win_rate"],
            loss_rate=winloss["loss_rate"],

            average_winner=returns["average_winner"],
            average_loser=returns["average_loser"],

            largest_winner=returns["largest_winner"],
            largest_loser=returns["largest_loser"],

            payoff_ratio=winloss["payoff_ratio"],
            profit_factor=winloss["profit_factor"],

            expectancy_rupees=expectancy["expectancy_rupees"],
            expectancy_r=expectancy["expectancy_r"]
        )

    # --------------------------------------------------------
    # BASIC STATISTICS
    # --------------------------------------------------------

    def calculate_basic_statistics(self, trades):

        winners = [t for t in trades if t.total_pnl > 0]

        losers = [t for t in trades if t.total_pnl < 0]

        breakeven = [t for t in trades if t.total_pnl == 0]

        return {

            "total_trades": len(trades),

            "winning_trades": len(winners),

            "losing_trades": len(losers),

            "breakeven_trades": len(breakeven),

            "winners": winners,

            "losers": losers
        }

    # --------------------------------------------------------
    # RETURN STATISTICS
    # --------------------------------------------------------

    def calculate_return_statistics(self, trades):

        winners = [t for t in trades if t.total_pnl > 0]

        losers = [t for t in trades if t.total_pnl < 0]

        gross_profit = sum(t.total_pnl for t in winners)

        gross_loss = abs(sum(t.total_pnl for t in losers))

        net_profit = sum(t.total_pnl for t in trades)

        average_winner = (
            gross_profit / len(winners)
            if winners else 0
        )

        average_loser = (
            gross_loss / len(losers)
            if losers else 0
        )

        largest_winner = (
            max((t.total_pnl for t in winners), default=0)
        )

        largest_loser = (
            min((t.total_pnl for t in losers), default=0)
        )

        return {

            "gross_profit": gross_profit,

            "gross_loss": gross_loss,

            "net_profit": net_profit,

            "average_winner": average_winner,

            "average_loser": average_loser,

            "largest_winner": largest_winner,

            "largest_loser": largest_loser
        }

    # --------------------------------------------------------
    # WIN / LOSS STATISTICS
    # --------------------------------------------------------

    def calculate_win_loss_statistics(
            self,
            basic,
            returns
    ):

        total = basic["total_trades"]

        win_rate = (
            basic["winning_trades"] / total
            if total else 0
        )

        loss_rate = (
            basic["losing_trades"] / total
            if total else 0
        )

        payoff_ratio = (
            returns["average_winner"] /
            returns["average_loser"]
            if returns["average_loser"] > 0
            else 0
        )

        profit_factor = (
            returns["gross_profit"] /
            returns["gross_loss"]
            if returns["gross_loss"] > 0
            else 0
        )

        return {

            "win_rate": round(win_rate * 100, 2),

            "loss_rate": round(loss_rate * 100, 2),

            "payoff_ratio": round(payoff_ratio, 2),

            "profit_factor": round(profit_factor, 2)
        }

    # --------------------------------------------------------
    # EXPECTANCY
    # --------------------------------------------------------

    def calculate_expectancy_statistics(
            self,
            basic,
            returns,
            winloss
    ):

        total = basic["total_trades"]

        expectancy_rupees = (
            returns["net_profit"] / total
            if total else 0
        )

        # Convert percentages back to decimals
        win_rate = winloss["win_rate"] / 100

        loss_rate = winloss["loss_rate"] / 100

        payoff = winloss["payoff_ratio"]

        expectancy_r = (
            (win_rate * payoff)
            -
            loss_rate
        )

        return {

            "expectancy_rupees":
                round(expectancy_rupees, 2),

            "expectancy_r":
                round(expectancy_r, 3)
        }