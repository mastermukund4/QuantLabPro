class RecoveryCalculator:

    def calculate(self, net_profit, max_drawdown):

        if max_drawdown == 0:
            return 0

        return round(net_profit / max_drawdown, 3)