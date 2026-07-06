from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.performance import PerformanceAnalyzer

from exports.excel_exporter import ExcelExporter


class TradeService:

    def __init__(self, filepath):
        self.filepath = filepath

    def run(self):

        importer = AlgoTestImporter(self.filepath)
        df = importer.load()

        parser = TradeParser()
        trades = parser.parse(df)

        report = PerformanceAnalyzer().analyze(trades)

        self.print_report(report)

        ExcelExporter().export(report, trades)

    def print_report(self, report):

        print()
        print("=" * 75)
        print("QUANTLAB PRO - PERFORMANCE REPORT")
        print("=" * 75)

        print("\n📊 TRADING ACTIVITY")
        print("-" * 75)
        print(f"{'Total Trades':35}: {report.activity.total_trades}")
        print(f"{'Winning Trades':35}: {report.activity.winning_trades}")
        print(f"{'Losing Trades':35}: {report.activity.losing_trades}")
        print(f"{'Breakeven Trades':35}: {report.activity.breakeven_trades}")
        print(f"{'Win Rate':35}: {report.activity.win_rate:.2f}%")
        print(f"{'Loss Rate':35}: {report.activity.loss_rate:.2f}%")

        print("\n💰 RETURNS")
        print("-" * 75)
        print(f"{'Gross Profit':35}: ₹{report.returns.gross_profit:,.2f}")
        print(f"{'Gross Loss':35}: ₹{report.returns.gross_loss:,.2f}")
        print(f"{'Net Profit':35}: ₹{report.returns.net_profit:,.2f}")
        print(f"{'Average Winning Trade':35}: ₹{report.returns.average_winning_trade:,.2f}")
        print(f"{'Average Losing Trade':35}: ₹{report.returns.average_losing_trade:,.2f}")
        print(f"{'Average P&L / Trade':35}: ₹{report.returns.average_pnl_per_trade:,.2f}")
        print(f"{'Best Trade':35}: ₹{report.returns.best_trade:,.2f}")
        print(f"{'Worst Trade':35}: ₹{report.returns.worst_trade:,.2f}")

        print("\n🎯 STRATEGY EDGE")
        print("-" * 75)
        print(f"{'Payoff Ratio':35}: {report.edge.payoff_ratio:.2f}")
        print(f"{'Profit Factor':35}: {report.edge.profit_factor:.2f}")
        print(f"{'Expectancy (R)':35}: {report.edge.expectancy_r:.3f}")

        print("\n📈 EQUITY")
        print("-" * 75)
        print(f"{'Starting Capital':35}: ₹{report.equity.starting_capital:,.2f}")
        print(f"{'Ending Capital':35}: ₹{report.equity.ending_capital:,.2f}")

        print("\n📉 DRAWDOWN")
        print("-" * 75)
        print(f"{'Maximum Drawdown':35}: ₹{report.drawdown.max_drawdown_rupees:,.2f}")
        print(f"{'Maximum Drawdown %':35}: {report.drawdown.max_drawdown_percent:.2f}%")
        print(f"{'Current Drawdown':35}: ₹{report.drawdown.current_drawdown_rupees:,.2f}")
        print(f"{'Current Drawdown %':35}: {report.drawdown.current_drawdown_percent:.2f}%")

        print("\n📅 ADVANCED ANALYTICS")
        print("-" * 75)

        if report.monthly:
            print(f"{'Monthly Analysis':35}: Available ({len(report.monthly.months)} months)")

        if report.weekly:
            print(f"{'Weekly Analysis':35}: Available ({len(report.weekly.weeks)} weeks)")

        if report.weekday:
            print(f"{'Weekday Analysis':35}: Available ({len(report.weekday.weekdays)} weekdays)")

        if report.duration:
            print(f"{'Duration Analysis':35}: Available ({len(report.duration.durations)} buckets)")

        if report.streak:
            print(f"{'Streak Analysis':35}: Available ({len(report.streak.streaks)} streaks)")

        if report.calendar:
            print(f"{'Calendar Analysis':35}: Available ({len(report.calendar.days)} trading days)")

        if report.risk:
            print(f"{'Risk Analysis':35}: Available")

        print("=" * 75)