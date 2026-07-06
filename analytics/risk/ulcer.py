import math


class UlcerCalculator:

    def calculate(self, drawdown_curve, equity_curve):

        if not drawdown_curve or not equity_curve:
            return 0

        percentages = []

        peak = equity_curve[0]

        for equity, drawdown in zip(equity_curve, drawdown_curve):

            if equity > peak:
                peak = equity

            dd_percent = (
                drawdown / peak * 100
                if peak else 0
            )

            percentages.append(dd_percent ** 2)

        ulcer_index = math.sqrt(
            sum(percentages) / len(percentages)
        )

        return round(ulcer_index, 3)