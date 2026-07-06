from models.streak_report import StreakReport, StreakStats


class StreakAnalyzer:

    def analyze(self, trades):

        streaks = []

        current_type = None
        current_length = 0
        current_pnl = 0

        for trade in trades:

            if trade.total_pnl > 0:
                trade_type = "Win"
            elif trade.total_pnl < 0:
                trade_type = "Loss"
            else:
                trade_type = "Breakeven"

            if current_type is None:
                current_type = trade_type
                current_length = 1
                current_pnl = trade.total_pnl

            elif trade_type == current_type:
                current_length += 1
                current_pnl += trade.total_pnl

            else:
                streaks.append(
                    StreakStats(
                        streak_type=current_type,
                        length=current_length,
                        pnl=round(current_pnl, 2)
                    )
                )

                current_type = trade_type
                current_length = 1
                current_pnl = trade.total_pnl

        if current_type is not None:
            streaks.append(
                StreakStats(
                    streak_type=current_type,
                    length=current_length,
                    pnl=round(current_pnl, 2)
                )
            )

        winning_streaks = [
            s for s in streaks if s.streak_type == "Win"
        ]

        losing_streaks = [
            s for s in streaks if s.streak_type == "Loss"
        ]

        longest_winning_streak = max(
            (s.length for s in winning_streaks),
            default=0
        )

        longest_losing_streak = max(
            (s.length for s in losing_streaks),
            default=0
        )

        average_winning_streak = (
            sum(s.length for s in winning_streaks) / len(winning_streaks)
            if winning_streaks else 0
        )

        average_losing_streak = (
            sum(s.length for s in losing_streaks) / len(losing_streaks)
            if losing_streaks else 0
        )

        largest_winning_streak_pnl = max(
            (s.pnl for s in winning_streaks),
            default=0
        )

        largest_losing_streak_pnl = min(
            (s.pnl for s in losing_streaks),
            default=0
        )

        current_streak_type = (
            streaks[-1].streak_type
            if streaks else "None"
        )

        current_streak_length = (
            streaks[-1].length
            if streaks else 0
        )

        return StreakReport(
            longest_winning_streak=longest_winning_streak,
            longest_losing_streak=longest_losing_streak,
            average_winning_streak=round(average_winning_streak, 2),
            average_losing_streak=round(average_losing_streak, 2),
            total_winning_streaks=len(winning_streaks),
            total_losing_streaks=len(losing_streaks),
            current_streak_type=current_streak_type,
            current_streak_length=current_streak_length,
            largest_winning_streak_pnl=round(largest_winning_streak_pnl, 2),
            largest_losing_streak_pnl=round(largest_losing_streak_pnl, 2),
            streaks=streaks
        )