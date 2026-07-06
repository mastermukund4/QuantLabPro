import statistics


class SortinoCalculator:

    def calculate(self, returns):

        downside_returns = [
            r for r in returns if r < 0
        ]

        if not downside_returns:
            return 0

        avg_return = statistics.mean(returns)

        downside_deviation = statistics.stdev(
            downside_returns
        ) if len(downside_returns) > 1 else abs(downside_returns[0])

        if downside_deviation == 0:
            return 0

        return round(avg_return / downside_deviation, 3)