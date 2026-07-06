from collections import defaultdict

from models.legs_report import LegsReport, LegGroupStats


class LegsAnalyzer:

    def analyze(self, trades):

        option_type_data = defaultdict(list)

        buy_sell_data = defaultdict(list)

        for trade in trades:

            for leg in trade.legs:

                option_type_data[leg.option_type].append(leg)

                buy_sell_data[leg.buy_sell].append(leg)

        return LegsReport(

            option_type_stats=self._build_stats(option_type_data),

            buy_sell_stats=self._build_stats(buy_sell_data)
        )

    def _build_stats(self, grouped_legs):

        reports = []

        for group_name in sorted(grouped_legs.keys()):

            legs = grouped_legs[group_name]

            winners = [leg for leg in legs if leg.pnl > 0]

            losers = [leg for leg in legs if leg.pnl < 0]

            gross_profit = sum(leg.pnl for leg in winners)

            gross_loss = abs(sum(leg.pnl for leg in losers))

            net_profit = sum(leg.pnl for leg in legs)

            total = len(legs)

            reports.append(

                LegGroupStats(

                    group_name=group_name,

                    total_legs=total,

                    winning_legs=len(winners),

                    losing_legs=len(losers),

                    gross_profit=round(gross_profit, 2),

                    gross_loss=round(gross_loss, 2),

                    net_profit=round(net_profit, 2),

                    average_pnl=round(net_profit / total, 2)
                    if total else 0,

                    best_leg=round(
                        max((leg.pnl for leg in legs), default=0),
                        2
                    ),

                    worst_leg=round(
                        min((leg.pnl for leg in legs), default=0),
                        2
                    ),

                    win_rate=round(
                        len(winners) / total * 100,
                        2
                    ) if total else 0,

                    profit_factor=round(
                        gross_profit / gross_loss,
                        2
                    ) if gross_loss > 0 else 0
                )
            )

        return reports