class VarCalculator:

    def calculate_var_95(self, pnl_values):

        if not pnl_values:
            return 0

        sorted_values = sorted(pnl_values)

        index = int(len(sorted_values) * 0.05)

        return round(sorted_values[index], 2)

    def calculate_cvar_95(self, pnl_values):

        if not pnl_values:
            return 0

        sorted_values = sorted(pnl_values)

        index = int(len(sorted_values) * 0.05)

        tail_losses = sorted_values[:index + 1]

        if not tail_losses:
            return 0

        return round(
            sum(tail_losses) / len(tail_losses),
            2
        )