class CalmarCalculator:

    def calculate(self, total_return_percent, max_drawdown_percent):

        if max_drawdown_percent == 0:
            return 0

        return round(
            total_return_percent / max_drawdown_percent,
            3
        )