class KellyCalculator:

    def calculate(self, win_rate, payoff_ratio):

        win_probability = win_rate / 100

        loss_probability = 1 - win_probability

        if payoff_ratio == 0:
            return 0

        kelly = (
            win_probability
            -
            loss_probability / payoff_ratio
        )

        return round(kelly * 100, 2)