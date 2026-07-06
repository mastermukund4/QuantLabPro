import statistics


class SharpeCalculator:

    def calculate(self, returns):

        if len(returns) < 2:
            return 0

        avg_return = statistics.mean(returns)
        std_dev = statistics.stdev(returns)

        if std_dev == 0:
            return 0

        return round(avg_return / std_dev, 3)